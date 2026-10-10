#!/bin/bash
set -e
echo "1. Fetching lake cache..."
./scripts/lake-cache-fetch.sh --force
echo "2. Saving oleans..."
mkdir -p /tmp/mathlib_oleans
mv .lake/packages/mathlib/.lake/build/lib /tmp/mathlib_oleans/lib
echo "3. Removing incomplete mathlib dir..."
rm -rf .lake/packages/mathlib
echo "4. Cloning mathlib manually..."
git clone https://github.com/leanprover-community/mathlib4 .lake/packages/mathlib
cd .lake/packages/mathlib
git checkout f897ebcf72cd16f89ab4577d0c826cd14afaafc7
echo "5. Restoring oleans..."
mkdir -p .lake/build
mv /tmp/mathlib_oleans/lib .lake/build/lib
echo "Done!"
