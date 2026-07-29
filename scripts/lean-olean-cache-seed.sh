#!/usr/bin/env bash
# Seed / reseed the lean-cache GitHub Release with a tar.zst olean archive.
#
# Creates (or updates) a GitHub Release tagged `lean-cache/v<version>`
# containing a single asset `lake-oleans.tar.zst` — the full build
# output (QOU + UGB + Fred2005 + Mathlib + dependency packages).
#
# Compared to the legacy orphan-branch approach:
#   - No 100 MB chunk splitting (release assets support up to 2 GB)
#   - No git object bloat (release assets don't count against repo size)
#   - zstd compression (~40% smaller than gzip, 3× faster decompress)
#   - Single `gh release download` to restore (no FETCH_HEAD assembly)
#
# Usage:  scripts/lean-olean-cache-seed.sh [--push]
#   (dry by default: builds the tarball, prints size; --push uploads it)
set -euo pipefail
ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
cd "$ROOT"

VERSION="$(cut -d: -f2 lean-toolchain | tr -d '\r')"    # v4.24.0
SLUG="$(echo "$VERSION" | tr . -)"                        # v4-24-0
TAG="lean-cache/$VERSION"
ASSET="/tmp/lake-oleans.tar.zst"
PUSH=0; [ "${1:-}" = "--push" ] && PUSH=1

echo "seed: toolchain=$VERSION  tag=$TAG"

# ── Collect build artifacts ────────────────────────────────────────────
echo "seed: packing oleans with zstd ..."
tar cf - \
  content/quantum-observable-universe/lean/.lake/build \
  content/unital-groebner-bases/lean/.lake/build \
  content/fred2005-formal-groups/lean/.lake/build \
  .lake/packages/*/.lake/build \
  2>/dev/null | zstd -19 -T0 -o "$ASSET"

sz=$(du -h "$ASSET" | cut -f1)
echo "  tarball: $sz ($ASSET)"

# Count what we're shipping
n_qou=$(find content/quantum-observable-universe/lean/.lake/build -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
n_ugb=$(find content/unital-groebner-bases/lean/.lake/build -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
n_fred=$(find content/fred2005-formal-groups/lean/.lake/build -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
n_ml=$(find .lake/packages/mathlib -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
n_deps=$(find .lake/packages -not -path '*/mathlib/*' -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
echo "  QOU=$n_qou  UGB=$n_ugb  Fred2005=$n_fred  Mathlib=$n_ml  deps=$n_deps"

if [ "$PUSH" -ne 1 ]; then
  echo "DRY RUN — rerun with --push to upload to GitHub Release $TAG"
  exit 0
fi

# ── Upload to GitHub Release ──────────────────────────────────────────
if ! command -v gh >/dev/null 2>&1; then
  echo "seed: ERROR — gh CLI not found; cannot upload release asset." >&2
  exit 1
fi

# Create the release if it doesn't exist
if ! gh release view "$TAG" --repo litlfred/qou >/dev/null 2>&1; then
  echo "seed: creating release $TAG ..."
  gh release create "$TAG" \
    --repo litlfred/qou \
    --title "Lean olean cache @ $VERSION" \
    --notes "Prebuilt Lean oleans for toolchain $VERSION.

Restore with:
\`\`\`bash
scripts/lean-cache-restore.sh
\`\`\`

Contents: QOU=$n_qou  UGB=$n_ugb  Fred2005=$n_fred  Mathlib=$n_ml  deps=$n_deps oleans.
Compressed with zstd -19.
Seeded: $(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    --latest=false
fi

echo "seed: uploading $sz asset to $TAG ..."
gh release upload "$TAG" \
  "$ASSET" \
  --repo litlfred/qou \
  --clobber

echo "seed: ✅ uploaded lake-oleans.tar.zst to release $TAG"
echo "seed: restore with:  scripts/lean-cache-restore.sh"
