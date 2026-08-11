# lake-cache addon — H4 Wedderburn cone

Prebuilt oleans for the `H₄(q)` Wedderburn cone, **absent from the base
`lake-cache/qou-v4-24-0`** because it sits outside the QOU dependency closure
that seeded the base.

Restore **after** the base restore:

```bash
ROOT=$(git rev-parse --show-toplevel); T=$(mktemp)
git fetch --depth=1 origin lake-cache/qou-v4-24-0-h4-wedderburn-cone
# Pin the commit ONCE. FETCH_HEAD is mutable: if a parallel agent fetches
# mid-loop the parts silently resolve against the wrong commit, the tarball is
# truncated, and tar fails with "not in gzip format".
C=$(git rev-parse FETCH_HEAD)
git ls-tree --name-only "$C" | grep '"'"'^addon-oleans\.tgz\.part'"'"' | sort \
  | while read -r p; do git show "$C:$p"; done > "$T"
tar xzf "$T" -C "$ROOT"
```

## What it saves

Measured on the build that produced it (`lean`-direct, **sequential** — these
peak at 5–6.5 GB RSS, so building two at once OOMs a 15 GB box):

| module | wall | peak RSS |
|---|---|---|
| `HeckeH4BlockMap31` | 941 s | 5.5 GB |
| `HeckeH4BlockMap211` | 916 s | 6.5 GB |
| `HeckeH4WedderburnCoord` | 584 s | 6.5 GB |
| `HeckeH4WedderburnMulB` | 457 s | 6.5 GB |
| `HeckeH4WedderburnMulA` | 335 s | 6.5 GB |
| `HeckeH4AlgebraLaws` | 222 s | 5.2 GB |
| `HeckeH4BlockMap22` | 87 s | 5.2 GB |

~65 min of wall clock. Bean `qou-x64l` warns *">25 min each at ~6 GB"* for
`BlockMap31`/`211`: right on memory, about 60 % over on time.

Also included: the 13 Mathlib oleans in the cone of
`Mathlib.Algebra.Module.LinearMap.Polynomial`, which the base cache also lacks
(bean `qou-py7e` — the base carries 2970 of Mathlib's 6996 modules).
`scripts/build-missing-oleans.py` rebuilds those in minutes; shipping them is
free here.

## When you do NOT need this

`QOU/Machinery/H4Cyclicity.lean` proves `trM4_cyclic` from the generator actions
with a cone **under 10 minutes**, and never touches the block maps. This addon is
only for work that needs the Wedderburn blocks themselves.
