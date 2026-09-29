#!/usr/bin/env bash
# lean-orphan-modules.sh — list library modules that nothing imports.
#
# A module under lean/<Lib>/ that no other module imports is unreachable from
# the library root. It is still COMPILED: the lakefile sets
# `globs = ["QOU", "QOU.+"]` (bean qou-rc7b), and `QOU.+` is
# `Glob.andSubmodules`, so `lake build` covers the whole tree.
#
# What an orphan costs is VISIBILITY, not compilation. It is invisible to
# everything that walks imports — blueprint, doc-gen, dependency analysis, an
# import cone rooted at the library root. A theorem no tooling can reach is a
# theorem nobody finds. That is the only thing this script is evidence for:
# do NOT quote it as evidence about what gets built.
#
# Wiring an orphan up is ordinary work, not owner-scoped. Read-only: this
# script reports, and never edits a lakefile.
#
# Usage:
#   scripts/lean-orphan-modules.sh                 # QOU, summary only
#   scripts/lean-orphan-modules.sh --list          # + every orphan module
#   scripts/lean-orphan-modules.sh --root folio/unital-groebner-bases/lean --lib UGB
#
# ⚠ CORRECTION 2026-08-30 (bean qou-si7d), kept because the superseded text was
# acted on. This header used to open "list library modules no build ever
# elaborates", describe the lakefile as having "no `globs` key", and state that
# wiring orphans up "is owner-scoped (bean qou-kljb) because turning on hundreds
# of unbuilt modules at once could be very red".
#
# All three were true when written and none is true now. qou-rc7b added the
# globs; qou-kljb then CLOSED on exactly that finding — widening the build
# exposed one real breakage, not hundreds, and it was fixed. But the header was
# never updated, and an agent read the owner-scoped line as a live gate and
# reported wiring work as blocked on it several times.
# `.github/workflows/lean-orphan-gate.yml` had carried the correction since
# 2026-08-15; this file was simply missed.
#
# The measured orphan count is still large and still worth reducing — for
# reachability, which is a different claim from coverage.
set -euo pipefail

ROOT="folio/quantum-observable-universe/lean"
LIB="QOU"
LIST=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --root) ROOT="$2"; shift 2 ;;
    --lib)  LIB="$2";  shift 2 ;;
    --list) LIST=1;    shift ;;
    -h|--help) sed -n '2,21p' "$0" | sed 's/^# \?//'; exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

[ -f "$ROOT/$LIB.lean" ] || { echo "no root module $ROOT/$LIB.lean" >&2; exit 2; }

ROOT="$ROOT" LIB="$LIB" LIST="$LIST" python3 - <<'PY'
import os, re, sys
root = os.environ["ROOT"]; lib = os.environ["LIB"]; show = os.environ["LIST"] == "1"

def path_of(mod): return os.path.join(root, mod.replace(".", "/") + ".lean")
def imports(p):
    try:
        with open(p, encoding="utf-8") as fh: text = fh.read()
    except OSError:
        return []
    return re.findall(rf'^import\s+({lib}[\w.]*)', text, re.M)

seen, stack = set(), imports(os.path.join(root, f"{lib}.lean"))
while stack:
    m = stack.pop()
    if m in seen: continue
    seen.add(m); stack += imports(path_of(m))

allmods = set()
for d, _, files in os.walk(os.path.join(root, lib)):
    for f in files:
        if f.endswith(".lean"):
            allmods.add(os.path.relpath(os.path.join(d, f), root)[:-5].replace("/", "."))

orphans = sorted(allmods - seen)
reach = len(allmods & seen)
print(f"{lib}: {len(allmods)} modules, {reach} reachable from {lib}.lean, "
      f"{len(orphans)} UNREACHABLE ({100*len(orphans)//max(len(allmods),1)}%)")
print("  (unreachable = imported by nothing, so invisible to blueprint/doc-gen/"
      "dependency analysis. They ARE compiled -- globs covers the tree.)")
if show:
    for m in orphans: print(f"  {m}")
elif orphans:
    print("  (re-run with --list to see them)")
sys.exit(1 if orphans else 0)
PY
