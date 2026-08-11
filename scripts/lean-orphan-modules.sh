#!/usr/bin/env bash
# lean-orphan-modules.sh — list library modules no build ever elaborates.
#
# A module under lean/<Lib>/ that nothing imports is NOT built. The lakefile
# declares `[[lean_lib]] name = "QOU"` with no `globs` key, and Lake's default
# is then `globs = #[.one "QOU"]` — only the root module and its transitive
# imports. Verified by experiment (throwaway package, toolchain v4.24.0):
# without `globs` an unimported module is not built; with `globs = ["Lib",
# "Lib.+"]` it is.
#
# So an orphan can be syntactically broken, carry an uncited `sorry`, or fail
# to typecheck, and nothing will say so. Combined with two standing gaps —
# a library .lean with no .ts/.md sibling has no .qa.json sidecar, and CI
# auto-triggers are disabled repo-wide — these modules have NO automated check.
#
# Read-only: reports, never edits a lakefile. Wiring orphans up is owner-scoped
# (bean qou-kljb) because turning on hundreds of unbuilt modules at once could
# be very red.
#
# Usage:
#   scripts/lean-orphan-modules.sh                 # QOU, summary only
#   scripts/lean-orphan-modules.sh --list          # + every orphan module
#   scripts/lean-orphan-modules.sh --root content/unital-groebner-bases/lean --lib UGB

set -euo pipefail

ROOT="content/quantum-observable-universe/lean"
LIB="QOU"
LIST=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --root) ROOT="$2"; shift 2 ;;
    --lib)  LIB="$2";  shift 2 ;;
    --list) LIST=1;    shift ;;
    -h|--help) sed -n '2,22p' "$0" | sed 's/^# \?//'; exit 0 ;;
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
      f"{len(orphans)} NOT BUILT ({100*len(orphans)//max(len(allmods),1)}%)")
if show:
    for m in orphans: print(f"  {m}")
elif orphans:
    print("  (re-run with --list to see them)")
sys.exit(1 if orphans else 0)
PY
