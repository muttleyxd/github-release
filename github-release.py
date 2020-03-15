#!/usr/bin/env python3
import argparse
from github import Github
import glob

parser = argparse.ArgumentParser()
parser.add_argument('--token',
                    type=str,
                    required=True,
                    help='GitHub access token')
parser.add_argument('--file-glob',
                    type=str,
                    required=True,
                    help='Glob to upload')
parser.add_argument('--repository',
                    type=str,
                    required=True,
                    help='Repository to use')
args = parser.parse_args()

g = Github(args.token)
repo = g.get_repo(args.repository)
releases = repo.get_releases()
latest_release = releases[0]
if not latest_release.draft:
    latest_release = repo.create_git_release('', 'draft', 'draft', draft=True)

for file in glob.glob(args.file_glob):
    try:
        latest_release.upload_asset(file)
    except Github.GithubException:
        print(f'{file} already exists')
