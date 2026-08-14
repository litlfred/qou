---
# qou-m7py
title: "D2: Rust gram.rs TR_M[5]=z^3 bug is load-bearing under convention D"
status: todo
type: task
created_at: 2026-08-14T16:21:57Z
updated_at: 2026-08-14T16:21:57Z
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
