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
PKG="$ROOT/folio/quantum-observable-universe/lean"
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
#
# ...but "first candidate WITH a QOU/ dir" is not the same test as "the restored
# tree", and what breaks it is the DEFAULT state of a fresh session here.
#
# Measured 2026-09-08.  The cache was restored to the ROOT (2442 QOU oleans),
# and `scripts/lean-build-bg.sh` -- started by a SessionStart hook -- was running
# `lake build` with cwd = $PKG, filling the PAPER tree from scratch.  So the
# paper path HAD a QOU/ dir, the loop took it, and it held exactly TWO oleans.
# The rebuild set was computed against that, and the run died on the first
# Mathlib-importing module.  Watched over the next few minutes the same tree went
# 2 -> 17 QOU oleans and 2352 -> 2950 mathlib oleans: not a stale stub, a tree
# mid-build.  It is present, incomplete, and CHANGING, and "has a QOU/ dir"
# cannot tell that from a restored cache.
#
# So pick by COMPLETENESS, not by order.  This is also the criterion that is
# right in BOTH directions -- see the PKGROOTS note below, where the same
# disagreement runs the other way.  $OLEANS may be set to override.
#
# LIMITATION, stated because it is real: the count is a snapshot of a tree
# another process may be writing.  It is the right call at the moment it is
# taken, and a build that finishes mid-run can make it the wrong one.  Hence the
# warning below -- AGENTS.md §"QUIESCE THE SESSIONSTART BUILD" is the actual fix.
if pgrep -f 'lake build' >/dev/null 2>&1; then
  echo "WARNING: a 'lake build' is running (likely scripts/lean-build-bg.sh from" >&2
  echo "  the SessionStart hook).  It writes into an olean tree this script reads," >&2
  echo "  so the counts below are a snapshot of a MOVING target.  Prefer to let it" >&2
  echo "  finish, or pass OLEANS=<dir> explicitly." >&2
fi
if [ -z "${OLEANS:-}" ]; then
  _best_n=-1
  for cand in "$PKG/.lake/build/lib/lean" "$ROOT/.lake/build/lib/lean"; do
    [ -d "$cand/QOU" ] || continue
    _n=$(find "$cand/QOU" -name '*.olean' -size +0 2>/dev/null | wc -l)
    if [ "$_n" -gt "$_best_n" ]; then _best_n=$_n; OLEANS="$cand"; fi
  done
  [ -n "${OLEANS:-}" ] && echo "olean tree chosen by count: $_best_n QOU oleans"
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
# packages (`folio/.../lean/QOU.lean` imports `UGB`), and a missing entry
# shows up as `unknown module prefix`, which reads exactly like a real error.
SIBLINGS=$(ls -d "$ROOT"/folio/*/lean/.lake/build/lib/lean 2>/dev/null |
             grep -v "^$OLEANS\$" | tr '\n' ':')
# BOTH package locations, PAPER FIRST.  The root Lake workspace has
# `.lake/packages/` and each paper package has its own
# `folio/*/lean/.lake/packages/`; the documented sandbox restore
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
#
# THE PIN STAYS. `scripts/lean-sync-olean-trees.sh` (`182c59191`, bean
# `qou-4h26`) reached this same asymmetry independently and answered it the
# right way round: instead of choosing an order, hardlink the UNION of every
# package tree into every package tree, so which one wins stops mattering.  Its
# header says explicitly that this script's paper-first pinning "is correct and
# is NOT changed here", and an earlier version of this file reordered anyway.
# Reverted -- their fix removes the asymmetry, ordering only re-aims it.
#
# So this block DIAGNOSES, and since 2026-11-21 also runs the union script when
# it finds an imbalance.  Before that the union script had no callers, so until
# an agent ran it by hand, an incomplete
# paper `Mathlib/` still shadows a complete root one and every `import
# Mathlib.Tactic` still fails naming a path for a file that exists in the other
# tree.  Measured here 2026-09-08: paper mathlib 2352 oleans with NO
# `Mathlib/Tactic.olean`, root 3469 with it.
#
# Non-empty oleans only, so the 0-byte `Mathlib/Tactic.olean` of bean
# `qou-tpdg` counts as the absence it behaves like.
PKGROOTS=""
for d in "$ROOT"/folio/*/lean/.lake/packages/*/.lake/build/lib/lean \
         "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$d" ] && PKGROOTS="$PKGROOTS$d:"
done

_mlfirst=""; _mlworst=""; _mlbest=""
for _loc in "$ROOT"/folio/*/lean/.lake/packages "$ROOT"/.lake/packages; do
  [ -d "$_loc/mathlib/.lake/build/lib/lean" ] || continue
  _c=$(find "$_loc/mathlib/.lake/build/lib/lean" -name '*.olean' -size +0 2>/dev/null | wc -l)
  [ -z "$_mlfirst" ] && _mlfirst=$_c            # the one that actually shadows
  { [ -z "$_mlbest" ] || [ "$_c" -gt "$_mlbest" ]; } && _mlbest=$_c
  { [ -z "$_mlworst" ] || [ "$_c" -lt "$_mlworst" ]; } && _mlworst=$_c
done
if [ -n "$_mlfirst" ] && [ -n "$_mlbest" ] && [ "$_mlfirst" -lt "$_mlbest" ]; then
  echo "WARNING: the mathlib tree FIRST on LEAN_PATH has $_mlfirst non-empty oleans," >&2
  echo "  but another location has $_mlbest.  Lean resolves a package from the first" >&2
  echo "  root holding that PACKAGE dir, so the smaller one answers for all of" >&2
  echo "  Mathlib and you will see MISSING-OLEAN errors naming files that exist." >&2
  if [ "${LEAN_NO_TREE_SYNC:-0}" = 1 ]; then
    echo "  Fix: scripts/lean-sync-olean-trees.sh   (bean qou-4h26; LEAN_NO_TREE_SYNC=1 set, not run)" >&2
  else
    # Wired 2026-11-21 (bean qou-4h26): the union script had no callers, so
    # this diagnosis fired and nothing fixed it.  It hardlinks (no disk cost),
    # is idempotent, and the trees agree afterwards whichever one wins.
    echo "  Running scripts/lean-sync-olean-trees.sh (set LEAN_NO_TREE_SYNC=1 to skip)." >&2
    "$ROOT/scripts/lean-sync-olean-trees.sh" >&2 || echo "  WARNING: tree sync failed; results may show phantom MISSING-OLEAN." >&2
  fi
fi
LP="$SHADOW:$PKGROOTS$SIBLINGS$OLEANS"

ORDER=$(OLEANS="$OLEANS" ROOT="$ROOT" python3 - "$@" <<'PY'
import os, re, pathlib, subprocess, sys
root = pathlib.Path(os.environ["ROOT"])
pkg = root / "folio/quantum-observable-universe/lean"
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

# Emit topological LEVELS, one per line, not a flat order.  Every module in a
# level has all of its dirty imports in a STRICTLY EARLIER level, so a level's
# modules are mutually independent and can be compiled concurrently.
#
# The frozen `done` snapshot is what makes that true, and the previous version
# did not take one: it mutated `done` inside the scan, so a module appearing
# later in `need` than one it imports saw that import already `done` and joined
# the SAME pass.  Flattened into a serial order that was still correct -- the
# dependency preceded the dependent in the list -- so this is not a latent bug
# being fixed, it is the invariant parallelism needs being established.
# Computing `ready` against a frozen `done` is the whole difference.
levels, done = [], set()
while len(done) < len(need):
    ready = [n for n in need
             if n not in done and all(d in done or d not in need for d in imports[n])]
    if not ready:
        print("CYCLE", file=sys.stderr); sys.exit(1)
    levels.append(ready)
    done.update(ready)
print(f"# cone={len(cone)} changed_since_snapshot={len(changed)} rebuild={len(need)} "
      f"levels={len(levels)} widest={max((len(l) for l in levels), default=0)}",
      file=sys.stderr)
for lv in levels:
    print(" ".join(lv))
PY
) || exit 1

# PARALLEL REBUILD, LEVEL BY LEVEL (bean qou-srb1).
#
# $ORDER is one topological LEVEL per line; every module in a level has all its
# dirty imports in a strictly earlier level, so a level compiles concurrently
# and levels run in sequence.
#
# WHAT IT BUYS, AND WHERE IT COSTS -- both measured, 4-core container.
#
# The win is real and it is nearly linear.  Controlled A/B over 40 MUTUALLY
# INDEPENDENT modules (one level, no barriers), same modules both arms, page
# cache pre-warmed:
#
#     1 job  x 4 threads   3m05.2 wall   user 2m36.5  sys 51.7   1.12 cores
#     2 jobs x 2 threads   1m34.3 wall   user 2m40.3  sys 47.1   2.20 cores
#                          ^^^^^^ 1.96x, and CPU time is UNCHANGED (3m28 vs
#                          3m27) -- no overhead penalty, the same work spread.
#
# The reason it pays is the 1.12: Lean's OWN threading gets barely one core on
# these modules even at LEAN_NUM_THREADS=4, so the parallelism has to come from
# running separate modules, not from inside one.
#
# 🛑 But it LOSES on a narrow cone, and that is not hypothetical.  A cone-40
# target (39 modules over 15 levels, i.e. 2.6 per level) measured 2m52.8 here
# against 2m45.5 serial -- 4.4% SLOWER, with user and sys both up.  A level of
# one module is serial plus an xargs spawn.  The full content-sweep cone is the
# other regime (1478 modules, 27 levels, widest 555, ~55 per level) and is
# where this is worth having.  NOT measured end-to-end at that size: the A/B
# would have cost ~12 h of machine time, so what is established is the
# mechanism (1.96x on a wide level) and the shape, not a sweep-level number.
#
# The narrow-cone loss is a LEVEL-BARRIER artifact, not a mechanism one: a
# global work queue -- start a module the moment its own deps are done, rather
# than when its whole level is -- would remove it.  That is the follow-up.
#
# Three properties are load-bearing and must survive any future edit:
#
#   1. The per-module `rm -f` STAYS, and stays per module.  The shadow is
#      hardlinked to the real olean tree, so `lean -o` without the unlink writes
#      through the shared inode and mutates the tree the shadow exists to
#      protect.  Parallelism does not change this; it multiplies it.  Verified:
#      the real tree is byte-identical (path, mtime, size, 2793 oleans) after a
#      parallel rebuild AND after one killed with SIGKILL mid-write.
#   2. A worker writes ONLY inside $SHADOW.  Its log goes to $SHADOW/.rb/, one
#      file per module -- the serial version shared a single `.rb.log`, which
#      concurrent workers would interleave into an unreadable failure report.
#   3. Jobs should DIVIDE nproc, and LEAN_NUM_THREADS is nproc/jobs, matching
#      `lean-library-sweep.py --jobs`: a non-divisor wastes the remainder.
#      Only 2x2 and 1x4 were measured here (above); the 3x1 comparison in that
#      script's docs is ITS workload, not this one.  Override REBUILD_JOBS=<n>.
_np=$(nproc 2>/dev/null || echo 2)
REBUILD_JOBS="${REBUILD_JOBS:-$(( _np >= 2 ? _np / 2 : 1 ))}"
[ "$REBUILD_JOBS" -ge 1 ] || REBUILD_JOBS=1
LNT=$(( _np / REBUILD_JOBS )); [ "$LNT" -ge 1 ] || LNT=1

rebuild_one() {
  local m="$1"
  local src="$PKG/${m//./\/}.lean"
  local out="$SHADOW/${m//./\/}.olean"
  local log="$SHADOW/.rb/$m.log"
  mkdir -p "$(dirname "$out")" "$SHADOW/.rb"
  # See property 1 above -- do not hoist, do not drop.
  rm -f "$out" "${out%.olean}.olean.hash" "${out%.olean}.ilean"
  if ! (cd "$PKG" && LEAN_PATH="$LP" LEAN_NUM_THREADS="$LNT" \
          lean $LEAN_OPTS "${src#$PKG/}" -o "$out") > "$log" 2>&1; then
    echo "REBUILD FAILED $m"
    grep -v '^note:' "$log" | head -30
    return 1
  fi
  printf '  ok  %s\n' "$m"
  return 0
}
export -f rebuild_one
export PKG SHADOW LP LEAN_OPTS LNT

n=$(printf '%s' "$ORDER" | tr ' ' '\n' | grep -c . || true)
nlev=$(printf '%s' "$ORDER" | grep -c . || true)
echo "rebuilding $n module(s) from source, $nlev level(s), ${REBUILD_JOBS}x${LNT} (jobs x threads) ..."
mkdir -p "$SHADOW/.rb"
i=0
lv=0
while IFS= read -r level; do
  [ -n "$level" ] || continue
  lv=$((lv+1))
  cnt=$(printf '%s\n' $level | grep -c .)
  # On a failure `xargs` lets the siblings ALREADY IN FLIGHT finish, so one or
  # two `ok` lines can follow the REBUILD FAILED.  That is correct and is not a
  # missing kill: the next LEVEL never starts, which is the only thing that
  # could compile against a module that did not build.  Verified with a seeded
  # failure -- error body printed, exit 1, later levels not entered.
  if ! printf '%s\n' $level \
       | xargs -r -n1 -P "$REBUILD_JOBS" bash -c 'rebuild_one "$@"' _; then
    echo "rebuild failed in level $lv/$nlev"
    exit 1
  fi
  i=$((i+cnt))
  printf '  [%d/%d] level %d/%d done (%d module(s))\n' "$i" "$n" "$lv" "$nlev" "$cnt"
done <<< "$ORDER"

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
