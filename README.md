# xScrobble

xScrobble is a stupidly simple Last.fm CLI made in python. 

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Installation](#installation)
* [License](#license)
* [Acknowledgements](#acknowledgements)

## About The Project

I specifically made this version as a way of scrobbling to multiple accounts at once. My roommate and I both like to track our listening religiously, but pretty much all music players only allow you to connect one account for scrobbling. We live in the same place though and we frequently listen to music over speakers at the same time from a single player. How the ***hell*** are we supposed to both get our precious scrobbles in this situation!?!? Well that is what xScrobble is here to do!

xScrobble works as a totally normal scrobbler... *but wait theres more!* xScrobble allows you to define a "macro" user which is like a regular user except its **NOTHING LIKE** a regular user. A macro user is composed of underlying regular users and macro users. Whenever a scrobble is targeted at a macro user, it will scrobble for all users listed underneath it as well! This lets you scrobble for any number of users at once!

Problem solved! I use Plex with Tautulli personally, but this should be able to work with any music player that can execute a simple command. Yeah... I know thats not exactly ideal. This is a bring your own glue situation. I wrote this for me anyways and it works, so if you need to change it then do it.

### Built With

* [Python 3.8](https://www.python.org/)

## Installation

Listen, if you need instructions to get this running then you should probably not even be on this page. You literally just need to clone the repo, install the requirements, and run the script. I know these instructions suck, but this is free software and you sure as hell haven't paid me for support.

## License

Distributed under the GNU Affero General Public License. See `LICENSE.md` for more information.

## Acknowledgements

Developed by Zachary Sugano - [zachoooo](https://github.com/zachoooo)

Special thanks to:

* [Scootyrooty](https://github.com/Scootyrooty) for inspiring me to make this project
* Tilly for always being there for me

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/zachoooo/xscrobble.svg?style=flat-square
[contributors-url]: https://github.com/zachoooo/xscrobble/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/zachoooo/xscrobble.svg?style=flat-square
[forks-url]: https://github.com/zachoooo/xscrobble/network/members
[stars-shield]: https://img.shields.io/github/stars/zachoooo/xscrobble.svg?style=flat-square
[stars-url]: https://github.com/zachoooo/xscrobble/stargazers
[issues-shield]: https://img.shields.io/github/issues/zachoooo/xscrobble.svg?style=flat-square
[issues-url]: https://github.com/zachoooo/xscrobble/issues
[license-shield]: https://img.shields.io/github/license/zachoooo/xscrobble.svg?style=flat-square
[license-url]: https://github.com/zachoooo/xscrobble/blob/master/LICENSE.md