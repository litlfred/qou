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

## Update 2026-08-15 — Python side has LANDED; crate re-read; one prior claim corrected

`pyhecke.gram` and `pyhecke.trace_formal` are now convention D (PR #5055).
That makes this bean the last split, and it is now *guarded* rather than
merely noted: `build_atom_nf` / `atom_per_generator_volumes` REFUSE to
dispatch to the native wheel (`_native_ok()` raises), because with Python
on D and the crate diverging, merely installing the wheel would silently
change results on some machines and not others. Override with
`QOU_ALLOW_NATIVE_DIVERGENCE=1`. So the ~100× speedup is off until this
bean lands — that is the cost of the guard and the reason to prioritise it.

### CORRECTION: the crate is NOT "on convention C"

Earlier wording (mine, and in this bean's title context) said the Rust was
convention C. **It is not.** Re-read of `tools/hecke-engine/src/gram.rs`:

```rust
/// z = q³/(q² + 1) — Markov closure parameter, **trace convention D**
pub fn trace_weights(q: f64) -> [f64; 6] {
    let z = markov_z(q);
    [1.0, z, z, z * z, z * z, z * z * z]   // <-- TR_M[5] = z³, the unported bug
}
pub const Q_0: f64 = 1.1099785955541805;   // <-- the MUON pin
```

So `markov_z` is already D. Two real divergences remain:

| # | Divergence | Rust | Python | Size |
|---|---|---|---|---|
| 1 | `TR_M[5]` | `z*z*z` | `h*z² + z` | structural — see below |
| 2 | `Q_0` anchor | 1.1099785955541805 (muon) | 1.1099785827513808 (proton) | 2.19e-8 rel on z |

### Why #1 and the quotient must land in ONE commit

`z³` is what keeps the crate's Gram **non-singular**. Fix the trace alone
and a singular Gram drops into a native path that has no radical, no
pseudoinverse, and no notion that either is needed. Verified on the exact
probe at three rational q: correct TR_M[5] → rank 5, det 0 exactly; `z³` →
rank 6. So the port is: TR_M[5] fix **+** `RADICAL` **+** quotient inverse
in a single change.

### #2 is independently a violation

The hardcoded muon `Q_0` contradicts AGENTS.md's owner directive
(2026-08-07): all production compute defaults to the experimental/proton
pin. Worth fixing in the same PR since it is a one-constant change, but it
is a *separate* defect from the trace rule — do not let fixing one imply
the other is done.

### Reference implementation to port against

- `tools/pyhecke/python/pyhecke/gram.py` — `TR_M`, `RADICAL`, `G_PINV`,
  `gram_quotient_inverse()`, and `gram_inverse()` raising `NotImplementedError`.
- `tools/pyhecke/tests/test_gram_values.py::test_gram_determinant_is_exactly_zero_over_Q`
  — the exact-ℚ rank/determinant test. Worth mirroring in Rust: a float64
  determinant (3.998e-17) cannot distinguish singular from tiny, so an
  `f64`-only Rust test cannot actually assert the degeneracy either.
- The crate's own `z_at_q0_matches_python` test pins the muon value
  0.6126880505455892 and will need the proton value 0.6126880371464652.

### Definition of done

1. `trace_weights` → `[1, z, z, z², z², h*z² + z]`.
2. `Q_0` → proton pin; update `z_at_q0_matches_python`.
3. Radical + quotient inverse exposed; no 6×6 inverse.
4. Exact-rational (not f64) test asserting rank 5 / det 0.
5. Remove the `_native_ok()` guard in `pyhecke/gram.py` and its three
   tests in `test_gram_values.py`, restoring the native speedup.

## 2026-08-15 (2) — my own definition-of-done above was WRONG; PR #5069

The 5-step "definition of done" I wrote earlier today treated this as a
port. It is not. Reading the prior agent's decline note in `gram.rs` and
measuring the consumers, **that decline was correct** and this bean
under-scoped the work. Correcting it here rather than leaving a plan that
would have walked the next agent into a breaking change.

### Why the z³ fix is NOT a port

`z³` is what keeps the crate's Gram non-singular. Correcting it deletes
`gram_inverse` — and unlike Python's `G_INV` (measured at **zero**
consumers before removal), this one has a live downstream family:

| consumer | use |
|---|---|
| `pyhecke-native/src/lib.rs:50` | exposed as a pyfunction |
| `gram.rs:619` | certificate builder |
| `borromean-axial-coupling.py:197` | `GRAM_INV[np.ix_(A, A)]` — arithmetic |
| `delta_lambda_master_formula_h3_probe.py` | reads the witness field |
| `delta_lambda_full_variance_phase5e_1.py` | calls the pyfunction |
| `bound_state_observable_validator.py` | **requires** the field |
| `audit_frobenius_pairing.py` | **requires** the field |

The honest replacement is dualisation on `H_3(q)/rad`, which is a
**different object** from what those witnesses hold — so it cannot be
swapped under the same key. Owner decision.

### Why the Q_0 re-pin is separately gated

Measured: **53** `certificate-*.json`, **657** files carrying the muon
literal. AGENTS.md posture for this (bean `tnjb`) is "do not
mass-regenerate" without scoped sign-off. The prior agent's note said the
same. Not taken.

### What PR #5069 landed instead (additive, non-breaking)

`trace_weights_markov`, `gram_from_weights`, `gram_matrix_markov`,
`gram_radical`, `gram_quotient_inverse` — correct objects, 16 cargo tests,
including a cross-language check against `numpy.linalg.pinv` (1e-9) run at
the proton pin passed **explicitly**, so it does not prejudge the Q_0 call.
The switch is now a one-line repoint of `gram_matrix`.

### Revised definition of done

1. **[OWNER]** decide the `gram_inverse` deletion + what replaces the
   dualisation for the seven consumers.
2. **[OWNER]** decide the `Q_0` re-pin (53 certificates).
3. Repoint `gram_matrix` → `trace_weights_markov`; update
   `det_at_q0_convention_d` and `gram_first_row_matches_trace_weights`.
4. Migrate the seven consumers to the quotient inverse under a NEW key.
5. Rebuild `pyhecke_native`; only THEN remove the `_native_ok()` guard in
   `pyhecke/gram.py` and its three tests.

### Related regression found while scoping this (fixed in #5055)

Two producers build their Gram from `pyhecke.gram.TR_M` and call
`np.linalg.inv` themselves — which does NOT raise on the singular D Gram
(entries 7.6e15, ‖G@inv − I‖ = 4.14). Guarded by
`pyhecke.gram.safe_inverse()`.

## 2026-08-15 (3) — Q_0 DONE; trace flip measured

**Q_0 re-pin: owner-approved and landed** (PR #5069). muon
1.1099785955541805 → proton 1.1099785827513808. `markov_z(Q_0)` is now
bit-identical to `pyhecke.gram.z`. 183 cargo tests pass; one pinned
determinant moved by 2.28e-8, consistent with the 1.15e-8 q shift.

**53 certificates NOT regenerated** — they record a superseded anchor and
nothing enforces them (no test cross-checks a committed certificate against
the live Q_0). That is the `tnjb` mass-migration and still needs its own
sign-off.

### Measured impact of the remaining flip (`z³` → `h·z² + z`)

| | value |
|---|---|
| `TR_M[5] = z³` | 0.2299948980341014 |
| `TR_M[5] = h·z² + z` | 0.6911664783584446 |
| change | **+200.5 %** — a tripling, not a correction |

Gram: 19/36 entries change; rank 6 → 5; det −0.152 → 0; cond 12 → 4.9e16.

**‖G⁺ − G⁻¹‖ = 4.26, i.e. 73.3 % relative.** The replacement object is
*substantially* different, so every downstream number derived from
`gram_inverse` moves — this is a re-derivation, not a patch.

### The split that must not be lumped

The two defects hit different consumers:

* **Rust-fed** (`z³` trace rule): `delta_lambda_full_variance_phase5e_1.py`,
  via `pyhecke_native.gram_inverse`.
* **Python-witness-fed** (inverting a singular D Gram):
  `borromean-axial-coupling.py`, `delta_lambda_master_formula_h3_probe.py`,
  `bound_state_observable_validator.py`, `audit_frobenius_pairing.py`.
  Guarded by `safe_inverse` in #5055.

Do not describe all five as "broken by the z³ bug" — only the first is.

### Remaining

1. **[OWNER]** flip `trace_weights`, given the 73 % re-derivation cost.
2. Migrate consumers to the quotient inverse under a NEW key.
3. Rebuild `pyhecke_native`; only then drop the `_native_ok()` guard.
4. **[OWNER/tnjb]** regenerate the 53 certificates.
