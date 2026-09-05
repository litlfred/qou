#!/usr/bin/env bash
# lean-shadow-verify.sh — verify a .lean file against the library SOURCE, not
# against whatever the restored olean cache happens to hold.
#
# WHY THIS EXISTS
#
# `lean`-direct verification (AGENTS.md §"VERIFY a single file with
# lean-direct") checks a file against the restored `lake-cache/qou-<slug>`
# olean tree.  That tree is a SNAPSHOT.  When a library signature moves after
# the snapshot was taken, a content-block file that calls the OLD signature
# still compiles — `exit 0` — while being red against the source it names.
#
# Measured, 2026-09-05: the cache was built 2026-08-30; commit 794c34897d7
# (2026-09-03) retyped `SeminormalRep.wtrace`'s genericity hypothesis from
# `q ^ 2 ≠ 1` to `GenericParameter.NotRootOfUnity q` across seven library
# consumers.  `descartes-knot-eigenbasis.lean` is a content-block sibling, was
# not among them, kept passing `q ^ 2 ≠ 1`, recorded `exit 0`, and landed on
# main broken.  This script reproduces the two errors in ~2 minutes.
#
# At the time of writing, 305 QOU modules had both a prebuilt olean and a
# source change since the snapshot, so the blind spot is not specific to that
# file.  Bean `qou-56qy`.
#
# WHAT IT DOES
#
#   1. copies the QOU olean tree into a shadow dir (Lean resolves a module
#      from the first LEAN_PATH root holding that package directory, so the
#      shadow must be complete, not a sparse overlay);
#   2. computes the modules whose SOURCE changed since the tree was built,
#      plus everything in the targets' import cone that transitively depends
#      on one, in topological order;
#   3. rebuilds exactly those from source into the shadow;
#   4. runs `lean` on the targets against the shadow.
#
# Mathlib is untouched — only the QOU package is rebuilt, which is why this is
# minutes rather than the 40-minute `lake build` storm.  It never invokes
# `lake`, so it cannot evict the restored cache.
#
# USAGE
#   scripts/lean-shadow-verify.sh <file.lean> [<file.lean> ...]
#   SHADOW=/path/to/reuse scripts/lean-shadow-verify.sh <file.lean>
#
# The shadow is ~2.3 GB.  It is removed on exit unless SHADOW is set, in which
# case it is kept and reused (the rebuild is skipped if it is already current).

set -uo pipefail

ROOT=$(git rev-parse --show-toplevel)
PKG="$ROOT/content/quantum-observable-universe/lean"
export PATH="$HOME/.elan/bin:$PATH"

# A bare `lean` does NOT apply the lakefile's [leanOptions].  That is not
# cosmetic: `autoImplicit` defaults TRUE in `lean` and is set FALSE in both
# lakefiles, so bare lean-direct silently auto-binds unbound identifiers that
# Lake rejects.  Measured 2026-09-05 on QOU/MassTheory/AtomWordShadow.lean,
# same file and same LEAN_PATH: `lean` exit 0 / 0 errors,
# `lean -DautoImplicit=false` exit 1 / 6 errors.  `-s 65536` mirrors the paper
# lakefile's moreLeanArgs.  Bean `qou-56qy`.
LEAN_OPTS="${LEAN_OPTS:--DautoImplicit=false -s 65536}"

[ $# -ge 1 ] || { echo "usage: $0 <file.lean> [...]" >&2; exit 2; }

# WHERE THE QOU OLEANS ARE depends on how the tree was built, and the two
# locations are not interchangeable.  A per-paper `cd $PKG && lake build` writes
# under $PKG/.lake; the `lake-cache/qou-<slug>` restore documented in AGENTS.md
# §"Agents building Lean in a sandbox" seeds the ROOT workspace at $ROOT/.lake.
# Measured 2026-09-05 on a correctly-restored container: 2442 QOU oleans at the
# root, 0 at the per-paper path.  Hardcoding the per-paper path therefore made
# this script exit 2 on exactly the tree it exists to verify against.
# $OLEANS may be set to override.
if [ -z "${OLEANS:-}" ]; then
  for cand in "$PKG/.lake/build/lib/lean" "$ROOT/.lake/build/lib/lean"; do
    [ -d "$cand/QOU" ] && { OLEANS="$cand"; break; }
  done
fi
[ -n "${OLEANS:-}" ] && [ -d "$OLEANS/QOU" ] || {
  echo "no restored olean tree with a QOU/ dir — looked in:" >&2
  echo "  $PKG/.lake/build/lib/lean" >&2
  echo "  $ROOT/.lake/build/lib/lean" >&2
  echo "restore lake-cache first (AGENTS.md §'Agents building Lean in a sandbox')," >&2
  echo "or set OLEANS=<dir containing QOU/>" >&2
  exit 2
}
echo "olean tree: $OLEANS"

KEEP=1
if [ -z "${SHADOW:-}" ]; then
  SHADOW=$(mktemp -d)
  KEEP=0
  trap 'rm -rf "$SHADOW"' EXIT INT TERM
fi

# The documented reuse path (`SHADOW=<dir>`) does not create the directory --
# only the mktemp branch above did -- so `cp` failed with "cannot create
# directory" on the very first documented invocation.  Pre-existing; bean
# `qou-tpdg`.
mkdir -p "$SHADOW"

if [ ! -d "$SHADOW/QOU" ]; then
  # HARDLINK, not copy.  The tree is ~2.3 GB and a container here has a
  # per-session disk quota (AGENTS.md §Disk space), so `cp -a` simply fails
  # with ENOSPC and the sweep judges nothing -- measured on a container with
  # 1.1 GB free.  `cp -al` costs no blocks (`du` reports 2.3 GB, `df` does not
  # move) and is safe because the rebuild below removes its target first, so it
  # never writes through a shared inode into the real olean tree.  Falls back
  # to a real copy if the shadow is on another filesystem.  Bean `qou-tpdg`.
  echo "linking olean tree into shadow ($SHADOW) ..."
  cp -al "$OLEANS/QOU" "$SHADOW/QOU" 2>/dev/null ||
    { echo "  hardlink failed; falling back to a real copy" >&2
      rm -rf "$SHADOW/QOU"; cp -a "$OLEANS/QOU" "$SHADOW/QOU"; }
fi

# Every paper package's build dir, not just qou's: a file may import across
# packages (`content/.../lean/QOU.lean` imports `UGB`), and a missing entry
# shows up as `unknown module prefix`, which reads exactly like a real error.
SIBLINGS=$(ls -d "$ROOT"/content/*/lean/.lake/build/lib/lean 2>/dev/null |
             grep -v "^$OLEANS\$" | tr '\n' ':')
# BOTH package locations, PAPER FIRST.  The root Lake workspace has
# `.lake/packages/` and each paper package has its own
# `content/*/lean/.lake/packages/`; the documented sandbox restore
# (AGENTS.md §"Mathlib cache 403 fallback") fills the PAPER one, so that is the
# tree it GUARANTEES.
#
# The root tree is not reliably broken -- it is not reliably POPULATED, which is
# worse for a gate.  Measured on two containers: on one, root held a 0-byte
# `Mathlib/Tactic.olean`, no `Mathlib/Data/Real/Basic.olean` and 1212 oleans, so
# every Mathlib-importing module failed with "invalid header" / "does not
# exist".  On another, root was a 6990-olean SUPERSET with both files
# byte-identical and the same code was fine.  Globbing the root alone makes this
# correct by luck of environment.  Bean `qou-tpdg`.
# Build this with a LOOP, not `ls -d <pat1> <pat2>`: `ls` SORTS its arguments,
# so it reorders the two patterns ("$ROOT/.lake/..." sorts before
# "$ROOT/content/...") and the root tree would win the pinning above -- which is
# exactly the bug being fixed, reintroduced by the fix.  Shell glob expansion
# keeps the patterns in the order written.
PKGROOTS=""
for d in "$ROOT"/content/*/lean/.lake/packages/*/.lake/build/lib/lean \
         "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$d" ] && PKGROOTS="$PKGROOTS$d:"
done
LP="$SHADOW:$PKGROOTS$SIBLINGS$OLEANS"

ORDER=$(OLEANS="$OLEANS" ROOT="$ROOT" python3 - "$@" <<'PY'
import os, re, pathlib, subprocess, sys
root = pathlib.Path(os.environ["ROOT"])
pkg = root / "content/quantum-observable-universe/lean"
oleans = pathlib.Path(os.environ["OLEANS"])
mod2path = {}
for p in pkg.glob("QOU/**/*.lean"):
    mod2path[str(p.relative_to(pkg).with_suffix("")).replace("/", ".")] = p
imports = {m: [i for i in re.findall(r"^import\s+(\S+)", p.read_text(), re.M) if i in mod2path]
           for m, p in mod2path.items()}

# Staleness is PER MODULE, not against one snapshot date.  The restored tree is
# mixed-age (oleans carry the mtime of whichever build wrote them), so taking
# the newest olean as "the" build time silently declares older modules current.
# Compare each module's own olean mtime against the commit date of its source.
# Source mtimes are useless here — a fresh clone stamps every file with the
# checkout time — so the source side comes from git, in one pass.
lastcommit, ts = {}, None
log = subprocess.run(["git", "log", "--format=%ct", "--name-only", "--",
                      str(pkg / "QOU")], cwd=root, capture_output=True, text=True).stdout
for line in log.splitlines():
    if not line:
        continue
    if line.isdigit():
        ts = int(line)
    elif line.endswith(".lean"):
        lastcommit.setdefault(line, ts)   # log is newest-first, so first wins

changed = set()
for m, p in mod2path.items():
    o = oleans / (m.replace(".", "/") + ".olean")
    if not o.exists():
        changed.add(m)                     # never built
        continue
    c = lastcommit.get(str(p.relative_to(root)))
    if c is None or c > o.stat().st_mtime:
        changed.add(m)

# import cone of the targets
cone, stack = set(), []
for t in sys.argv[1:]:
    txt = pathlib.Path(t).read_text()
    stack += [i for i in re.findall(r"^import\s+(\S+)", txt, re.M) if i in mod2path]
while stack:
    m = stack.pop()
    if m in cone: continue
    cone.add(m); stack += imports[m]

sys.setrecursionlimit(100000)
dirty, clean = set(), set()
def isdirty(m):
    if m in dirty: return True
    if m in clean: return False
    if m in changed or any(isdirty(d) for d in imports[m]):
        dirty.add(m); return True
    clean.add(m); return False
need = sorted(m for m in cone if isdirty(m))

order, done = [], set()
while len(done) < len(need):
    prog = False
    for n in need:
        if n not in done and all(d in done or d not in need for d in imports[n]):
            order.append(n); done.add(n); prog = True
    if not prog:
        print("CYCLE", file=sys.stderr); sys.exit(1)
print(f"# cone={len(cone)} changed_since_snapshot={len(changed)} rebuild={len(need)}",
      file=sys.stderr)
print("\n".join(order))
PY
) || exit 1

n=$(printf '%s' "$ORDER" | grep -c . || true)
echo "rebuilding $n module(s) from source ..."
i=0
for m in $ORDER; do
  i=$((i+1))
  src="$PKG/${m//./\/}.lean"
  out="$SHADOW/${m//./\/}.olean"
  mkdir -p "$(dirname "$out")"
  # The shadow is hardlinked to the real tree: REMOVE the target before
  # `lean -o` writes it, or the write lands on the shared inode and mutates the
  # real olean tree -- the thing the shadow exists to prevent.
  rm -f "$out" "${out%.olean}.olean.hash" "${out%.olean}.ilean"
  if ! (cd "$PKG" && LEAN_PATH="$LP" lean $LEAN_OPTS "${src#$PKG/}" -o "$out") > "$SHADOW/.rb.log" 2>&1; then
    echo "REBUILD FAILED [$i/$n] $m"
    grep -v '^note:' "$SHADOW/.rb.log" | head -30
    exit 1
  fi
  printf '  [%d/%d] %s\n' "$i" "$n" "$m"
done

if [ -n "${REBUILD_ONLY:-}" ]; then
  # Prepare the shadow and stop.  `scripts/lean-content-sweep.sh` uses this to
  # build one shadow for the union cone of many targets, then runs `lean` on
  # them in parallel itself.
  echo "LEAN_PATH=$LP"
  exit 0
fi

rc=0
for f in "$@"; do
  echo "--- $f"
  LEAN_PATH="$LP" lean $LEAN_OPTS "$f" 2>&1 | grep -v '^note:'
  s=${PIPESTATUS[0]}
  echo "EXIT=$s"
  [ "$s" -eq 0 ] || rc=1
done

[ "$KEEP" -eq 1 ] && echo "shadow kept at $SHADOW (reuse with SHADOW=$SHADOW)"
exit $rc
