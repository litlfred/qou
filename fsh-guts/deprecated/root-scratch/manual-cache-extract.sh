#!/bin/bash
set -euo pipefail
echo "Fetching cache branch..."
git fetch origin lake-cache/qou-v4-24-0 --depth 1
TMP=$(mktemp -d)
mkdir -p "$TMP/extract"
echo "Extracting chunks..."
git ls-tree --name-only FETCH_HEAD | grep "lake-oleans\.tgz\.part" | sort | while read -r part; do
    git cat-file blob "FETCH_HEAD:$part"
done | tar -xzf - -C "$TMP/extract"
echo "Removing broken .git from cache if it exists..."
rm -rf "$TMP/extract/.lake/packages/mathlib/.git"
echo "Copying contents into .lake..."
cp -r "$TMP/extract/.lake/." ".lake/"
rm -rf "$TMP"
echo "Cache extracted successfully."
