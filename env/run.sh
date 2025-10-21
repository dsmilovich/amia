#!/usr/bin/bash

set -e

REPO_DIR=$(pwd)

docker run -p 8888:8888 -v "$REPO_DIR:/workspace" -w /workspace --rm -it python-ceia:1.0