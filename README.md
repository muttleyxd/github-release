# github-release

Simple Python script for creating draft releases. PyGithub is required (`python-pygithub` on Arch Linux)

## What it does?

1. Get latest draft release (if there isn't one, then it will be created).
2. Upload files to it.

## Usage

```
usage: github-release.py [-h] --token TOKEN --file-glob FILE_GLOB --repository REPOSITORY

optional arguments:
  -h, --help            show this help message and exit
  --token TOKEN         GitHub access token
  --file-glob FILE_GLOB
                        Glob to upload
  --repository REPOSITORY
                        Repository to use
```

example:
```
./github-release.py --token <github_access_token> --file-glob "*.py" --repository "muttleyxd/github-release"
```
