# Building a trustworthy `lean`-direct harness

Read on demand from `MEMORY.md` §TRAP — false greens and corrupt oleans.
Everything here was measured on 2026-08-30 (PR #6097) unless dated otherwise.

## 1. A green run against a stale dependency olean is a FALSE GREEN

`lean`-direct resolves imports from the **on-disk oleans**. Change module `M`,
check consumer `C`, and `C` is compiled against the olean `M` had *before* your
edit. It exits 0. This is the failure mode this agent exists to prevent, and it
reads as success.

Measured: `QOU/Hecke/WedderburnRankDegeneracy.lean` gave **exit 0** against the
tree and **exit 1, 2 errors** once `QOU.Hecke.Wedderburn` was rebuilt from
current source. It had been red on `main` for six days, through several
sessions that had every reason to look at it.

The companion mistake is on the search side: a blast-radius grep for consumers
taking `[Foo …]` as a **hypothesis binder** does not find a file that
*constructs an instance*. Compute the reverse-import cone from the import
graph instead of guessing at the syntax of a use.

## 2. A partial `LEAN_PATH` overlay shadows the WHOLE namespace

The obvious cheap harness — a small dir holding only the rebuilt oleans, first
on `LEAN_PATH` — **cannot work**. Lean's `SearchPath.findWithExt` picks the
first root that *contains a directory named `QOU`* and then resolves every
`QOU.*` module under that root unconditionally:

```lean
let root? ← sp.findM? fun p => (p / pkg).isDir <||> ((p / pkg).addExtension ext).pathExists
return root?.map (fun root => modToFilePath root mod ext)
```

One file in the overlay therefore makes every *other* `QOU` module report
`object file '/tmp/ovl/QOU/X.olean' … does not exist`. The mirror must be
complete.

## 3. The harness that does work

```bash
ROOT=/home/user/qou; LEANLIB="$ROOT/content/quantum-observable-universe/lean"
BASE="$LEANLIB/.lake/build/lib/lean"
for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do BASE="$BASE:$d"; done
MIRROR=/tmp/qoumir
rm -rf "$MIRROR"; cp -al "$LEANLIB/.lake/build/lib/lean" "$MIRROR"   # hardlinks: ~0 disk
export LEAN_PATH="$MIRROR:$(echo "$BASE" | cut -d: -f2-)"
# then, in topological order over the reverse-import cone:
rm -f "$MIRROR/QOU/Path/To/Mod.olean"        # break the hardlink FIRST
lean -o "$MIRROR/QOU/Path/To/Mod.olean" "$LEANLIB/QOU/Path/To/Mod.lean"
```

`rm -f` before each write is load-bearing: without it a truncate-in-place write
would corrupt the **shared inode**, i.e. the real build tree.

Compute the cone with a small Python pass over `^\s*import\s+(QOU[A-Za-z0-9_.]*)`
across `QOU/**/*.lean`, invert it, take the transitive closure of the changed
module, and topologically sort. For `QOU.Hecke.Wedderburn` that is 8 modules and
about 90 s end to end — cheap enough that there is no excuse for the grep.

## 4. A disk-full `lake build` writes TRUNCATED oleans that segfault

Distinct from the eviction trap, and it masquerades as broken source. A
truncated olean mmaps fine and dies on a pointer chase. A **zero**-length one
gives a clean `failed to read file … invalid header` — so the clean error is
the *benign* case and the segfault is the ambiguous one.

**Signature: exit 139, ZERO errors, 0–1 seconds.** Real elaboration failures
take seconds and print errors.

Measured: after the session-start background build filled this container's
disk, a whole-library `lake build` reported 11 failing modules. **Ten were this
artifact.** `QOU/MathlibExt/OctonionSU3Stabilizer.olean` was **61,440 bytes**,
written inside the disk-full window, against **1,764,224 bytes** for its
healthy sibling `OctonionDerivationsBound.olean`. Only 1 of the 11 —
`QOU.Mass.QIntegerBarParity` — was a real defect.

Reporting "11 broken modules on main" was one step away and would have been
wrong. Triage: `df` first, then olean size against a sibling, then rebuild the
suspect from source. **Never conclude a module is broken from exit 139 alone.**

## 5. Disk is the binding constraint, and `df` lies about it

`df` shows 252 G nominal; the real limit is a per-session quota near 38 G. A
full `cp -r` of the QOU build tree is **2.1 G** — three of those plus a leaked
restore tarball took this container to 740 K free, at which point the Bash
harness cannot write its own output capture and every command fails. `cp -al`
makes the same mirror for ~0 bytes. Use it.
