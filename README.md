# lake-cache/qou-v4-24-0-root-import-closure — makes `lean QOU.lean` exit 0

Toolchain `leanprover/lean4:v4.24.0` · mathlib rev `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`
(identical in all three `lake-manifest.json`). Built 2026-09-05 from the source at
`b4587c54b2` on `claude/route-e-pgl3-flavour-screen-2026-09-05`.

**53 QOU modules** (`.olean` + `.ilean`, 42 MB raw / 14 MB packed), all `lean`-direct,
all exit 0. Two groups:

* **19 modules with no olean in either restored tree at all** — 4 `QOU.Hecke.*`,
  2 `QOU.Mathlib.*`, 13 `QOU.QBeta.*`. These are the genuine post-seed additions.
* **34 modules rebuilt from current source because their cached olean was STALE**
  — the `SchurWeyl`/`Specht`/`MathlibExt` cone plus `QOU.Mathlib.HeckeAlgebra`.
  Without these, `lean QOU.lean` fails on *declaration collisions*, not on missing
  files: e.g. `environment already contains
  'QOU.SchurWeyl.Seminormal.S1_eq_seminormalParam' from QOU.SchurWeyl.SeminormalParam`,
  because a declaration moved between modules after the cache was seeded and only one
  side's olean knew.

## 🛑 NOT a Lake seed

`lean`-direct output — no `.trace` siblings. Restore for `lean`-direct verification only;
a `lake build` treats untraced oleans as stale, rebuilds and evicts (bean `02kc`).

## Restore — the union mirror is part of the recipe, not optional

QOU oleans are split across TWO roots (`$ROOT/.lake/build/lib/lean` and
`$ROOT/content/quantum-observable-universe/lean/.lake/build/lib/lean`) and **the first
root on `LEAN_PATH` that holds a `QOU/` directory resolves every `QOU.*` module**, so
listing both does not union them — it hides the second. Build one mirror:

```bash
ROOT=$(git rev-parse --show-toplevel); MIR=$ROOT/.lake/union/lean; T=$(mktemp)
trap 'rm -f "$T"' EXIT INT TERM
mkdir -p "$MIR"
for d in "$ROOT"/.lake/build/lib/lean \
         "$ROOT"/content/quantum-observable-universe/lean/.lake/build/lib/lean \
         "$ROOT"/content/unital-groebner-bases/lean/.lake/build/lib/lean \
         "$ROOT"/.lake/packages/*/.lake/build/lib/lean \
         "$ROOT"/content/quantum-observable-universe/lean/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$d" ] && cp -aln "$d/." "$MIR/"
done   # hardlinks: ~26 MB real cost for ~6200 oleans

git fetch --depth=1 origin lake-cache/qou-v4-24-0-root-import-closure
git show FETCH_HEAD:addon-oleans.tgz > "$T"
tar xzf "$T" -C "$MIR" --unlink-first     # --unlink-first is REQUIRED
```

`--unlink-first` is load-bearing: the mirror entries are hardlinks shared with the real
trees, and extracting through one would rewrite the shared inode and corrupt the source
tree. The same rule applies to `lean -o` — `rm -f` the mirror olean before rebuilding it.

`lake-cache/ugb-v4-24-0` must also be restored (QOU/PhotonThreading imports UGB), or the
union has no `UGB/` and every `import QOU` dies at `unknown module prefix 'UGB'`.

Then:

```bash
LEAN_PATH="$MIR" lean content/quantum-observable-universe/lean/QOU.lean   # exit 0, ~11 s warm
```

## What this does and does not certify

It certifies that the **root library's import graph elaborates**: all 864 direct imports
of `QOU.lean` resolve and load without collision. It does **not** certify the whole
library against current source — the other ~2500 QOU oleans are still the cache's
snapshot, and a module whose source moved since is checked against the old olean.
Full certification is the dirty-closure rebuild (`MEMORY.md` §library rebuild).
