# lake-cache addon — H4 Wedderburn cone

> ## 🛑 NOT A LAKE CACHE SEED — read before restoring
>
> These oleans came from a **`lean`-direct** build (`lean f.lean -o out.olean`),
> so they have **no `.trace` siblings**. Lake treats untraced oleans as stale:
> it rebuilds them and **evicts** them (bean `02kc`).
>
> * ✅ **Restore for `lean`-direct verification.** `LEAN_PATH` + `lean file.lean`
>   never consults `.trace`. These compiled
>   `QOU/Machinery/HeckeH4RepDecomp.lean` to exit 0.
> * ❌ **Do NOT restore before a `lake build`.** No benefit, and it can evict.
> * ❌ **This is not what `scripts/lean-olean-cache-seed.sh` produces.** That
>   script's 90 % trace guard refuses a set like this, correctly. It was
>   bypassed here because the author hand-rolled a `tar` + orphan-commit script
>   instead of running it — the mistake is recorded so nobody repeats it.
>
> Corrected by its author the same day it was pushed. The oleans are real and
> the timings below are real; only the *claim that this seeds the Lake cache*
> was wrong.

Prebuilt oleans for the `H₄(q)` Wedderburn cone, absent from the base
`lake-cache/qou-v4-24-0` because it sits outside the QOU dependency closure that
seeded the base.

Restore (for `lean`-direct work only), after the base restore:

```bash
ROOT=$(git rev-parse --show-toplevel); T=$(mktemp)
git fetch --depth=1 origin lake-cache/qou-v4-24-0-h4-wedderburn-cone
# Pin the commit ONCE. FETCH_HEAD is mutable: if a parallel agent fetches
# mid-loop the parts silently resolve against the wrong commit, the tarball is
# truncated, and tar fails with "not in gzip format".
C=$(git rev-parse FETCH_HEAD)
git ls-tree --name-only "$C" | grep '^addon-oleans\.tgz\.part' | sort \
  | while read -r p; do git show "$C:$p"; done > "$T"
tar xzf "$T" -C "$ROOT"
```

## What it saves

Measured `lean`-direct, **sequential** — these peak at 5–7.5 GB RSS, so building
two at once OOMs a 15 GB box:

| module | wall | peak RSS |
|---|---|---|
| `HeckeH4WedderburnMulC` | 1011 s | 7.5 GB |
| `HeckeH4BlockMap31` | 941 s | 5.5 GB |
| `HeckeH4BlockMap211` | 916 s | 6.5 GB |
| `HeckeH4WedderburnCoord` | 584 s | 6.5 GB |
| `HeckeH4WedderburnMulB` | 457 s | 6.5 GB |
| `HeckeH4WedderburnMulA` | 335 s | 6.5 GB |
| `HeckeH4AlgebraLaws` | 222 s | 5.2 GB |

~65 min total. Bean `qou-x64l` warns *">25 min each at ~6 GB"* for
`BlockMap31`/`211`: right on memory, ~60 % over on time. A separate session
measured the same cone markedly slower (`BlockMap31` 1504 s, `BlockMap211`
1987 s, `WedderburnMulC` 2427 s), so treat these as a floor, not a promise.

Also included: the 13 Mathlib oleans in the cone of
`Mathlib.Algebra.Module.LinearMap.Polynomial`, which the base cache also lacks
(bean `qou-py7e` — the base carries 2970 of Mathlib's 6996 modules).

## When you do NOT need this at all

`QOU/Machinery/H4Cyclicity.lean` proves `trM4_cyclic` from the generator actions
with a cone **under 10 minutes** and never touches the block maps. Only work that
needs the Wedderburn blocks themselves wants this.
