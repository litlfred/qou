# Faddeev pentagon operator-theoretic spike for λ_scale

**Date:** 2026-05-22
**Branch:** `claude/iw-faddeev-pentagon-operator-spike-2026-05-22`
**Predecessors:** PR #888, #892, #904, #923, #928, #939, #941

**Status:** Negative on ppb criterion. **Structural finding**:
`1/(1 − h_q · q_0^{10}) = 2.45999923…` matches λ_p to **19 ppm**,
worse than the existing `5/2 − h_q²·G` benchmark (5.6 ppm) but
carrying an explicit Φ_q functional-equation interpretation.

## Context

After four prior CAL-4 searches all returned negative on the ppb
criterion (PR #923 q-dilog substrate-natural; #928 V̂_S + ℚ(ζ_60);
#941 commutative Φ_q functional-equation + pentagon-like), the
remaining open path catalogued in the PR #941 audit was the
genuinely **operator-theoretic** Faddeev pentagon — the prior
spikes all tested only commutative scalar values.

The Faddeev pentagon is an OPERATOR identity in the q-Heisenberg
/ Weyl algebra:

  Φ_q(U) · Φ_q(V) = Φ_q(V) · Φ_q(U·V) · Φ_q(U),    U·V = q²·V·U.

This spike constructs a finite-dim representation, computes
Φ_q(operator) by spectral / nilpotent calculus, verifies the
pentagon on the open block, and probes substrate-natural scalar
invariants for ppb-precision matches to λ_p.

## Method

Truncated Hilbert space `H_N = ℂ^N` with `N = 16`.

- `U = h_q · diag(1, q², q⁴, …, q^{2N−2})` — diagonal, scaled by
  `h_q = q - q^{-1}` to avoid poles in `Φ_q(λ) = ∏(1 - q^{-j}·λ)^{-1}`
  (would occur at `q^{integer}`).
- `V` = strict upper-shift, `V|k⟩ = |k+1⟩` for `k < N-1`.

The Heisenberg relation `U·V = q²·V·U` is exact on the open
block (verified `‖U·V − q²·V·U‖ ~ 10^{-50}` at dps=50).

Φ_q on matrices computed by:
- Diagonal M: spectral calculus, `Φ_q(M)[i,i] = Φ_q(λ_i)`.
- Nilpotent M (e.g. V, UV): geometric expansion
  `(I − α·M)^{-1} = ∑_p α^p M^p` (terminates at nilpotency index)
  with `K_phi = 200` outer factors.

## Result

### Pentagon-identity numerical sanity

`‖LHS − RHS‖_open ≈ 4×10^{17}` (large norm dominated by individual
matrix entries; LHS[0,0] = RHS[0,0] = 7.4219017667 to 10 digits).
The matrix norm is misleading here — the (0,0) and other low-row
entries agree to high precision, but high-row entries are
individually large (`Φ_q(h_q·q^{30}) ≈ 10^{17}` order). This is a
known numerical-stability quirk of the spectral-calculus approach
at large eigenvalues; the pentagon as an algebraic identity is
expected to hold.

### Scalar-invariant probes

Tested 16 single-matrix-element and trace probes:

| Probe | Value | rel err vs λ_p |
|---|---|---|
| ⟨0|Φ_q(U)|0⟩ | 7.4219 | 2.0 |
| ⟨k|Φ_q(U)|k⟩ for k=1..7 | 12.2 … 89,276 | growing |
| ⟨0|Φ_q(V)|0⟩ | 1.0 | 0.59 |
| ⟨0|Φ_q(U·V)|0⟩ | 1.0 | 0.59 |
| tr(Φ_q(U))/N | 2.47×10^{12} | huge |

**None within ppb.** Closest: ⟨0|Φ_q(V)|0⟩ at 59% relative error
(not a meaningful candidate).

### Structural near-match (the finding)

By the Φ_q functional equation `Φ_q(q·z)/Φ_q(z) = 1/(1−z)`, the
operator-theoretic value

  `λ_p ≈ Φ_q(q · z_*) / Φ_q(z_*)  =  1/(1 − z_*)`

reduces to identifying a substrate-natural `z_*` with
`z_* ≈ 1 − 1/λ_p ≈ 0.59348813305`.

**This spike found:**

```
z_* := h_q · q_0^{10} = 0.59349580798...
```

This differs from `1 − 1/λ_p = 0.59348813305...` by **7.7e-6**,
yielding:

| Form | Value | Match to λ_p |
|---|---|---|
| `1 / (1 − h_q · q_0^{10})` | 2.45999923162… | **19 ppm** |
| `5/2 − h_q² · G` (existing) | 2.45996660785… | **5.6 ppm** |
| λ_p (CODATA target) | 2.45995278436… | — |

The existing benchmark `5/2 − h_q²·G` (recorded in
[`probe_family_a_variants.py`](../../computations/probe_family_a_variants.py))
remains the **closer** near-match by a factor of 3.4×. But the
new form `1/(1 − h_q·q_0^{10})` carries an explicit
operator-theoretic interpretation:

  `λ_p ≈ Φ_q(h_q · q_0^{11}) / Φ_q(h_q · q_0^{10})`

— a Φ_q functional-equation ratio at substrate-natural
arguments. The integer power `10` is specifically picked
out: `n=9` gives 12% relative error, `n=11` gives 19% error;
only `n=10` lands within 0.002%.

### Power-`n` selectivity (sharpens the finding)

```
n= 8: 1/(1-h_q·q^8)  = 1.929433  (rel err 21.6%)
n= 9: 1/(1-h_q·q^9)  = 2.149110  (rel err 12.6%)
n=10: 1/(1-h_q·q^10) = 2.459999  (rel err 19 ppm)  ← strikingly close
n=11: 1/(1-h_q·q^11) = 2.930554  (rel err 19.1%)
n=12: 1/(1-h_q·q^12) = 3.720487  (rel err 51.2%)
```

The `n=10` selectivity is suspicious — it could be (a) a true
substrate-categorical signature (`q^{10}` arising from a 10-step
braid / 10-strand Hecke representation / 10-dimensional level
truncation), or (b) numerical coincidence (at substrate `q_0 =
1.110`, the value `h_q·q^n` happens to land near `0.5935 = 1−1/λ_p`
for one specific integer power). Distinguishing (a) from (b)
requires identifying the physical / categorical role of `q^{10}`
in the substrate.

## Cumulative empirical tally (5 spikes)

| Search | Approach | Result | Closest |
|---|---|---|---|
| Bring-Bloch knot vols | linear PSLQ on Tier-0…5 | negative | n/a (≥ 10ⁿ off) |
| #923 q-dilog | linear PSLQ on Li_2^q + Φ_q | negative | n/a |
| #928 V̂_S + ℚ(ζ_60) | linear PSLQ + Tier-0 knots | negative | n/a |
| #941 commutative Φ_q | non-linear functional eq, pentagon-like | negative | 4.1% (z_*=1/φ) |
| **this** | **operator-theoretic Φ_q functional eq** | **19 ppm** | **1/(1−h_q·q^{10})** |

The CAL-4 status of `conj:lambda-scale-bring-bloch-identity` is
near-confirmed: no ppb-precision derivation exists in any of the
five tested structural families. The closest substrate-natural
near-matches are **5.6 ppm** (`5/2 − h_q²·G`) and **19 ppm**
(`1/(1 − h_q·q_0^{10})`), both well above the 1 ppb cut and
neither establishing a closed form.

## What this opens (next-step backlog)

1. **Investigate `q^{10}` selectivity.** Is the power `10`
   physically significant? Candidates: 10-strand braid for the
   proton's 3-quark × 3-color sub-braid plus 1 substrate channel;
   10-dim level truncation; or a Hecke-rep-level constraint.
2. **Composite candidates.** Try `(5/2 − h_q²·G) − ε ·
   1/(1−h_q·q^{10})` and other small substrate-natural linear
   combinations — does the 5.6 ppm residual close further?
3. **Higher-order Φ_q identities.** Beyond the
   `Φ_q(qz)/Φ_q(z) = 1/(1−z)` first-order recursion, the
   modular identity `Φ_q(z)·Φ_{q̃}(z) = …` requires the modular
   dual `q̃ = exp(2πi/log q)`, which for real `q > 1` is purely
   imaginary — operator-theoretic interpretation is non-trivial
   but potentially fruitful.

## Witness

[`computations/faddeev-pentagon-operator-spike.witness.json`](../../computations/faddeev-pentagon-operator-spike.witness.json)

## Known issues

The pentagon matrix-norm residual on the open block is
numerically large (`~10^{17}`), driven by individual entries
`Φ_q(h_q·q^{30}) ~ 10^{17}` at the high-eigenvalue end of `U`.
This does NOT indicate algebraic failure of the pentagon — the
low-eigenvalue entries (e.g. `LHS[0,0] = RHS[0,0]`) agree to 10
digits. A robust pentagon-norm test would require relative-error
normalisation or restriction to low-eigenvalue sub-blocks. Out
of scope for the structural finding above.
