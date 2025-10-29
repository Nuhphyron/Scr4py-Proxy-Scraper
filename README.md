# Scr4py — Proxy Fetcher & CLI

```
  ███████╗ ██████╗██████╗ ██╗  ██╗██████╗ ██╗   ██╗
  ██╔════╝██╔════╝██╔══██╗██║  ██║██╔══██╗╚██╗ ██╔╝
  ███████╗██║     ██████╔╝███████║██████╔╝ ╚████╔╝
  ╚════██║██║     ██╔══██╗╚════██║██╔═══╝   ╚██╔╝  
  ███████║╚██████╗██║  ██║     ██║██║        ██║   
  ╚══════╝ ╚═════╝╚═╝  ╚═╝     ╚═╝╚═╝        ╚═╝   
                              v1.0 by Nuhphyron <3
```

> *Simple, fast, and friendly proxy fetcher with a retro CLI vibe.*

---

## Table of Contents

* [About](#about)
* [Disclaimer](#disclaimer)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [How It Works)](#How-It-Works)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [License](#license)

---

## About

Scr4py is a tiny CLI tool that fetches HTTP proxy lists and saves them to `proxies.txt` using a friendly terminal UI. It's designed to be easy to run, tweak, and extend — perfect for quick proxy collection workflows.

---

## Disclaimer

* Respect the terms of service of proxy providers.
* Do not use proxies for abusive or illegal actions.

---

## Features

* Fetch HTTP proxy lists via a public API.
* Option to route the API request through a local VPN/proxy.
* Saves output to `proxies.txt` for downstream use.
* Retro ASCII banner and colored terminal output (via `colorama`).
* Helpful error messages and recovery hints.

---

## Installation

**Requirements:**

* Python 3.8+
* `requests` and `colorama` packages

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from a terminal. On Windows use the PowerShell/CMD that has Python in PATH; on Linux/macOS use your shell.

```bash
python scr4py.py
```

You'll see a menu with options:

1. Direct Connection — fetch proxies directly from the public API.
2. Local VPN Proxy — route the request through `http://127.0.0.1:8080` (customize in code or make sure your vpn is routed through that port).
3. Exit — quit the CLI.

Successful fetches are saved to `proxies.txt` in the working directory.

---

## How It Works

* The script calls `https://www.proxy-list.download/api/v1/get?type=http` to obtain a newline-separated list of HTTP proxies.
* If you choose the VPN/proxy option, it configures a `proxies` dict for `requests`.
* Output is written to `proxies.txt` and the CLI prints a status code and helpful messages in case of any errors.

---

## Configuration

You can tweak a few variables at the top of `scr4py.py`:

* `proxies` dict (if you want to point to a different local proxy service, will add an update with proxies in the future)
* API URL (if you prefer a different provider, will update it for multiple API's)
* The banner art and gradient (for style lovers)

---

## Contributing

Contributions welcome! A few ways to help:

* Open issues for bugs or feature ideas.
* Send PRs to add more proxy sources, rate-limiting, or filtering (anonymity, country, port range).
* Beautify the star-checker (SVG badges, GitHub Actions to update a badge automatically).

---

## License

This project is provided as-is under the MIT License.

---

> Built with ❤️ by Nuhphyron — if you like this little tool, drop a star and watch the star checker change!
