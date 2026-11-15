#!/usr/bin/env bash
# Light platform install: just enough of litlfred/folio-assistant to run
# `state-mount.ts` (put beans/ and fsh-guts/ on disk) and
# `branch-store.ts push --id beans` (write bean edits back).
#
# Why this exists. scripts/setup-folio-assistant.sh installs the WHOLE
# platform: every layer in index.lock.json plus a full `bun install`.
# Measured 2026-11-15 at pin 82b389982: 1.7 GB on disk (729 MB of it
# node_modules), and in two sessions it either timed out after 30 min or ran
# the container out of disk. A session that only needs its bean work-plan
# pays all of that at start.
#
# What this does instead, measured the same day at the same pin:
#   - fetches 6 layers (cat-harness without library/ and docs/,
#     cat-harness-tools, bootstrap, bootstrap-tools, folio-assistant-core,
#     folio-assistant-sci), each a depth-1, blob-filtered fetch of the exact
#     SHA pinned in index.lock.json;
#   - links them under node_modules/@litlfred/ so workspace imports resolve;
#   - installs zod, the one npm package the two scripts need.
#   About 20 s and 165 MB.
#
# It does NOT replace setup-folio-assistant.sh for anything else (validate,
# qa-sweep, rendering). If you need those, run the full setup: it repoints
# the folio-assistant symlink at the full clone and this tree is ignored.
#
# Usage: scripts/mount-platform-lite.sh [dest]
#   dest defaults to <repo>/../folio-assistant-lite. On success,
#   <repo>/folio-assistant is a symlink to dest (only if that path is absent
#   or is already a symlink), so the usual commands work unchanged:
#     bun folio-assistant/cat-harness-tools/scripts/state-mount.ts
#     bun folio-assistant/cat-harness-tools/scripts/branch-store.ts push --id beans
#
# Note: branch-store.ts `push` has NO --dry-run; an unknown flag is ignored
# and the push happens (measured 2026-11-15).
set -euo pipefail
ROOT=$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)
DEST=${1:-$ROOT/../folio-assistant-lite}
case "$DEST" in /*) ;; *) DEST="$ROOT/$DEST" ;; esac
PIN=$(grep -oE '^[0-9a-f]{40}' "$ROOT/.folio-assistant-pin" | head -1)
[ -n "$PIN" ] || { echo "mount-platform-lite: no SHA in .folio-assistant-pin" >&2; exit 1; }
mkdir -p "$DEST"

fetch_one() { # <owner/repo> <sha> <dir> [sparse patterns...]
  local repo=$1 ref=$2 dir=$3; shift 3
  if [ -f "$dir/.lite-ref" ] && [ "$(cat "$dir/.lite-ref")" = "$ref" ]; then return 0; fi
  rm -rf "$dir"; git init -q "$dir"
  git -C "$dir" remote add origin "https://github.com/$repo"
  local i
  for i in 1 2 3 4; do
    git -C "$dir" fetch -q --depth 1 --filter=blob:none origin "$ref" && break
    [ "$i" = 4 ] && { echo "mount-platform-lite: fetch of $repo@$ref failed" >&2; return 1; }
    sleep $((2 ** i))
  done
  if [ $# -gt 0 ]; then git -C "$dir" sparse-checkout set --no-cone "$@"; fi
  git -C "$dir" checkout -q FETCH_HEAD
  rm -rf "$dir/.git"; echo "$ref" > "$dir/.lite-ref"
}

fetch_one litlfred/folio-assistant "$PIN" "$DEST/.platform" /index.lock.json /package.json /bunfig.toml
cp "$DEST/.platform/package.json" "$DEST/.platform/bunfig.toml" "$DEST/"

LAYERS="cat-harness cat-harness-tools bootstrap bootstrap-tools folio-assistant-core folio-assistant-sci"
mkdir -p "$DEST/node_modules/@litlfred"
for h in $LAYERS; do
  read -r repo ref < <(python3 - "$DEST/.platform/index.lock.json" "$h" <<'PY'
import json, sys
m = [x for x in json.load(open(sys.argv[1]))["mounts"] if x["harness"] == sys.argv[2]][0]
print(m["repository"], m["ref"])
PY
)
  if [ "$h" = cat-harness ]; then
    fetch_one "$repo" "$ref" "$DEST/$h" '/*' '!/library/' '!/docs/'
  else
    fetch_one "$repo" "$ref" "$DEST/$h"
  fi
  name=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1])).get('name',''))" "$DEST/$h/package.json" 2>/dev/null || true)
  case "$name" in @litlfred/*) ln -sfn "../../$h" "$DEST/node_modules/$name" ;; esac
done

# zod: the only npm dependency of state-mount / branch-store. Installed in a
# side directory so bun does not resolve the whole workspace.
ZV=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['overrides']['zod'])" "$DEST/package.json")
if [ ! -d "$DEST/.deps/node_modules/zod" ]; then
  mkdir -p "$DEST/.deps"
  echo '{"name":"lite-deps","private":true}' > "$DEST/.deps/package.json"
  (cd "$DEST/.deps" && bun add "zod@$ZV" >/dev/null)
fi
ln -sfn "$DEST/.deps/node_modules/zod" "$DEST/node_modules/zod"

if [ ! -e "$ROOT/folio-assistant" ] || [ -L "$ROOT/folio-assistant" ]; then
  # Never repoint a link that already reaches a full clone.
  if [ ! -L "$ROOT/folio-assistant" ] || [ -f "$(readlink -f "$ROOT/folio-assistant")/.lite-ref" ] \
     || [ ! -d "$ROOT/folio-assistant/cat-harness-tools/scripts" ]; then
    ln -sfn "$DEST" "$ROOT/folio-assistant"
  fi
fi
echo "mount-platform-lite: light platform at $DEST ($(du -sh "$DEST" | cut -f1))"
