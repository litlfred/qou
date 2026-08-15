---
# qou-m7py
title: 'D2: Rust gram.rs TR_M[5]=z^3 bug is load-bearing under convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-08-14T16:21:57Z
updated_at: 2026-08-14T21:56:37Z
---

## The coupling

`tools/hecke-engine/src/gram.rs` **is** convention D already. Per the banner in
`tools/pyhecke/python/pyhecke/gram.py` (lines 44–130), it survives convention
D's degeneracy **only because** it still carries the pre-2026-05-19
`TR_M[5] = z^3` bug that the Python side fixed.

So the Rust bug is not independently fixable: correcting `TR_M[5]` is expected
to make the Gram form singular in the native path too, exactly as it is in the
Python path. The two must be planned together with `qou-w8zz` (D1(b), invert
`G` on the quotient `H_3/rad`).

**Do not "just fix the Rust bug."** That is the trap this bean exists to name.

## Live split, and a caveat on where it was measured

The prior session measured, with `pyhecke_native` v0.9.0 installed:

- `pyhecke_native` → `markov_z(q0) = 0.6126880371464652` = **convention D**
- `pyhecke.gram.z` → `0.4993203341836945` = **convention C**

and `tests/test_gram_values.py:50` *pins* the C value deliberately.

**Caveat — not reproduced in this container.** The session that took over
PR #4928 (2026-08-14) found `pyhecke_native` **not installed**
(`ModuleNotFoundError`). So the split above is not currently observable here,
and `build_atom_nf` / `atom_per_generator_volumes` fall back to the pure-Python
path. Anyone picking this up should first record whether the native wheel is
present, because the whole failure mode is conditional on it. Do not assume the
earlier measurement still holds without re-taking it.

## Why it matters

`gram.py` exports `G_INV` **at import** into `constants.py`, `atom.py`,
`molecular.py`, `sdp.py` and nine corpus consumers. Once the wheel is rebuilt
from a branch carrying the Rust fix, those two functions return D while `z` /
`TR_M` / `G` / `G_INV` in the same module stay C — a silent mixed-convention
module, which is worse than the stale convention held consistently.

And `np.linalg.inv` does not protect anyone: on the D matrix it raises nothing
and returns entries to 7.6e15 with `||G @ G_INV − I|| = 1.64`.

## Related

- `qou-w8zz` — D1(b), the Python-side quotient inverse. Same repair.
- `qou-fu8c` — the `a_K` LP dual degenerating under D. Third instance of the
  same shape (the `ℓ(λ) ≥ 3` blocks are the radical under D).
- `qou-j6il` — a Rust binary returning convention C while its source read D.


## Update 2026-08-14 — the coupling is PROVED, not asserted (PR #5025)

`computations/probes/gram_radical_exact_probe.py`. The banner's claim was that
the Rust mirror "survives the degeneracy **only because** it still carries the
pre-2026-05-19 `TR_M[5] = z^3` bug". Decided by building the same **exact**
Gram (rational arithmetic, no floating point) with each value of `TR_M[5]`:

| q | `TR_M[5] = h·z² + z` (correct) | `TR_M[5] = z³` (the Rust value) |
|---|---|---|
| 11/10 | det = **0 exactly**, rank 5 | det ≠ 0, rank **6** |
| 7/5 | det = **0 exactly**, rank 5 | det ≠ 0, rank **6** |
| 13/7 | det = **0 exactly**, rank 5 | det ≠ 0, rank **6** |

So the coupling is real: **fixing the Rust bug WILL make the native Gram
singular.** The two cannot be planned independently, exactly as recorded.

**The bug is still live.** `tools/hecke-engine/src/gram.rs:89` ends
`trace_weights` with `[1.0, z, z, z*z, z*z, z*z*z]`; the crate's own module
docstring (lines 9–10, 724) documents the divergence from `pyhecke.gram.TR_M`.

**Size of the error.** At the proton pin under convention D:

```
z                        = 0.6126880371464652
TR_M[5]  correct h·z²+z  = 0.6911664783584445
TR_M[5]  Rust    z³      = 0.2299948980341014     -66.72 %
```

The Markov trace of the 3-strand cap element is off by two thirds, and that
error is precisely what has been holding the form non-degenerate.

## What this changes for the plan

The repair now has its projector in closed form (from the same probe, under
`qou-w8zz`): the radical is spanned by the q-antisymmetriser
`Σ_w (−1/q)^ℓ(w) T_w`. So both sides — `pyhecke/gram.py` and
`hecke-engine/src/gram.rs` — need the same quotient construction, and it is
explicit rather than numerically extracted.

Sequencing follows: fix `TR_M[5]` and adopt the quotient **together**, in one
change, on both sides. Fixing the trace alone lands a singular Gram in the
native path with `np.linalg.inv`-equivalent behaviour downstream.

**Not attempted here:** `pyhecke_native` is not installed in this container, so
the compiled wheel's live behaviour was not measured — only the mathematics it
implements. Anyone picking this up should record whether the wheel is present,
since the observable split is conditional on it.
