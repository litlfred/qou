# lake-cache/ugb-v4-24-0 — UGB oleans addon (lean-direct, NO .trace files)

Toolchain: `leanprover/lean4:v4.24.0`  ·  mathlib rev `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`
(the rev in all three `lake-manifest.json` — root, qou, ugb — at seed time).

## What this is

All **29** modules of the `ugb` package (`UGB` + 28 under `UGB/`), built
**`lean`-direct** against the restored Mathlib/QOU olean trees on 2026-09-05.
Payload path inside the tarball:

    content/unital-groebner-bases/lean/.lake/build/lib/lean/UGB/**.olean (+ .ilean)

## Why it exists

`content/quantum-observable-universe/lean/QOU/PhotonThreading.lean` carries
`import UGB.GrobnerShirshov.HeckeGS`, and `lake-cache/qou-v4-24-0` carries
Mathlib + QOU oleans but **no UGB**. Without this addon, `lean` on any file that
does `import QOU` dies immediately with:

    error: unknown module prefix 'UGB'

## 🛑 This is NOT a Lake cache seed

It came from a `lean`-direct build, so the oleans have **no `.trace` siblings**.
Lake treats untraced oleans as stale, rebuilds them and **evicts** the restore
(bean `02kc`). Restore it for `lean`-direct verification only; never run a
`lake build` against it. Same class as
`lake-cache/qou-v4-24-0-h4-wedderburn-cone`.

## Restore

```bash
ROOT=$(git rev-parse --show-toplevel); T=$(mktemp)
trap 'rm -f "$T"' EXIT INT TERM
git fetch --depth=1 origin lake-cache/ugb-v4-24-0
git show FETCH_HEAD:addon-oleans.tgz > "$T"
tar xzf "$T" -C "$ROOT"
```

Then put `$ROOT/content/unital-groebner-bases/lean/.lake/build/lib/lean` on
`LEAN_PATH` alongside the QOU and Mathlib olean dirs.

## Build command that produced it

From `content/unital-groebner-bases/lean`, per module in topological order:

    lean -o .lake/build/lib/lean/<Mod/Path>.olean -i .lake/build/lib/lean/<Mod/Path>.ilean <Mod/Path>.lean

with `LEAN_PATH` = the UGB output dir + every
`.lake/packages/*/.lake/build/lib/lean` under the repo root and under
`content/quantum-observable-universe/lean`. All 29 exit 0; wall time ~4 min,
dominated by `UGB.GrobnerShirshov.HeckeCompletion` (170 s).

A per-package `lake build` was **not** used: this container had 674 MB free and
the `ugb` package has no `.lake/`, so Lake would have cloned and built Mathlib
from source (~3.3 GB).
