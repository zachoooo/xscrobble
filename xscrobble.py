import argparse 
import click
import os
import pickle
import pylast
import time

from user import User

FILE_NAME = "xscrobble.data"
config_loaded = False
config = {
    "API_KEY": "",
    "API_SECRET": "",
    "users": [],
    "cached_scrobbles": []
}

def get_config() -> dict:
    global config
    if config_loaded:
        return config
    load_config()
    return config


def get_user(username) -> User:
    users = get_config()["users"]
    for user in users:
        if user.username == username:
            return user
    return None


@click.group()
def main():
    pass


@main.command(name="list")
@click.option("--verbose", default=False, is_flag=True, help="should all info be shown")
def list_command(verbose):
    num_users = 0
    num_macro_users = 0
    print("xscrobble users:")
    print("=======================================")
    for i, user in enumerate(get_config()["users"]):
        num_users += 1
        if user.is_macro:
            num_macro_users += 1
        print(f"   {i + 1}. {user}")
        if verbose:
            print(f"        session_key: {user.session_key}")
            print(f"        is_macro: {user.is_macro}")
            print(f"        macro_users:")
            for user in user.macro_users:
                print(f"            - {user}")
    print("=======================================")
    print(f"Total Users: {num_users}  Total Macro Users: {num_macro_users}")

@main.command()
@click.argument("username")
@click.option("--password", help="password associated with username")
@click.option("--key", help="session key associated with username")
@click.option("--macro", is_flag=True, default=False, help="toggle if account is a macro account")
def add(username, password, key, macro):
    if key is None and password is None and not macro:
        print("You must provide a password or a session key. Neither were provided")
        return
    password_hash = pylast.md5(password)
    network = None
    if not macro:
        try:
            if key is not None:
                network = pylast.LastFMNetwork(api_key=get_config()["API_KEY"], api_secret=get_config()["API_SECRET"], username=username, session_key=key)
            else:
                network = pylast.LastFMNetwork(api_key=get_config()["API_KEY"], api_secret=get_config()["API_SECRET"], username=username, password_hash=password_hash)
        except:
            print("Invalid authentication credentials provided. Please verify api key/secret and username/password.")
            return
    user = User()
    user.username = username
    if macro:
        user.session_key = "N/A MACRO USER"
    else:
        user.session_key = network.session_key
    user.is_macro = macro
    get_config()["users"].append(user)
    save_config()
    pass


@main.command()
@click.argument("key", required=False)
@click.argument("secret", required=False)
def api(key, secret):
    if key is None or secret is None:
        print(f"API Key: {get_config()['API_KEY']}")
        print(f"API Secret: {get_config()['API_SECRET']}")
        return
    get_config()["API_KEY"] = key
    get_config()["API_SECRET"] = secret
    print("Key and secret were set in config. This does not test your key.")
    save_config()


@main.command()
@click.argument("macro")
@click.argument("username")
def add_macro(macro, username):
    print(get_config()["users"])
    macro_user = get_user(macro)
    sub_user = get_user(username)
    if macro is None:
        print(f"No macro user named {macro} was found. Try adding it.")
        return
    elif not macro_user.is_macro:
        print(f"The given macro username {macro} is not listed as a macro user in database.")
        return
    if sub_user is None:
        print(f"No user named {username} was found. Try adding it.")
        return
    if username in macro_user.macro_users:
        print(f"The user {username} is already macro'd by {macro}")
        return
    macro_user.macro_users.append(username)
    print(get_config()["users"])
    save_config()
    print(get_config()["users"])
    print("Macro user successfully added")
    pass


def process_scrobble(username, artist, album, track):
    user = get_user(username)
    if user is None:
        print(f"No user called {username} found.")
        return
    if user.is_macro:
        for muser in user.macro_users:
            process_scrobble(muser, artist, album, track)
    else:
        network = pylast.LastFMNetwork(api_key=get_config()["API_KEY"], api_secret=get_config()["API_SECRET"], username=user.username, session_key=user.session_key)
        network.scrobble(artist, track, int(time.time()), album=album)


@main.command()
@click.argument("username", type=str)
@click.argument("artist", type=str)
@click.argument("album", type=str)
@click.argument("track", type=str)
def scrobble(username, artist, album, track):
    process_scrobble(username, artist, album, track)

def load_config():
    global config, config_loaded
    if not os.path.exists(FILE_NAME):
        return
    with open(FILE_NAME, "rb") as f:
        config = pickle.load(f)
    config_loaded = True


def save_config():
    global config
    with open(FILE_NAME, "wb") as f:
        pickle.dump(config, f)

if __name__ == "__main__":
    main()