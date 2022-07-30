# youtubeVideoDownloader

Youtube Video Downloader with Python

pytube pytube is a genuine, lightweight, dependency-free Python library (and command-line utility) for downloading YouTube videos.

Documentation Detailed documentation about the usage of the library can be found at pytube.io. This is recommended for most cases. If you want to hastily download a single video, the quick start guide below might be what you're looking for.

Description pytube is a lightweight library written in Python. It has no third-party dependencies and aims to be highly reliable.

pytube also makes pipelining easy, allowing you to specify callback functions for different download events, such as on progress or on complete.

Furthermore, pytube includes a command-line utility, allowing you to download videos right from the terminal.

Features Support for both progressive & DASH streams Support for downloading the complete playlist Easily register on_download_progress & on_download_complete callbacks Command-line interfaced included Caption track support Outputs caption tracks to .srt format (SubRip Subtitle) Ability to capture thumbnail URL Extensively documented source code No third-party dependencies

Quickstart This guide covers the most basic usage of the library. For more detailed information, please refer to pytube.io.


Installation Pytube requires an installation of Python 3.6 or greater, as well as pip. (Pip is typically bundled with Python installations.)

To install from PyPI with pip:

$ python -m pip install pytube
