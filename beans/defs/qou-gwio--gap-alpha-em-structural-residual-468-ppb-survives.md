---
# qou-gwio
title: 'GAP: alpha_em structural residual -468 ppb survives exact resummation — what is missing from the CS tower''s STRUCTURE (not its order)?'
status: in-progress
type: task
priority: normal
tags:
    - compute-accuracy
    - reorg-2026-10-04
created_at: 2026-08-07T01:00:00Z
updated_at: 2026-11-27T20:10:00Z
parent: qou-3l2l
---

## What changed (PR #4647)

The Chern–Simons correction tower for `α_em` was shipped as an order-2
truncation `1 + c₁ + c₁²κ`. It is geometric with ratio `c₁κ`, so it sums
exactly:

    α_em⁻¹ = bare · (1 + c₁/(1 − c₁κ))

with `bare = q·[9]_q·[10]_q`, `c₁ = (CS(T₂,₉)+CS(T₃,₅))·([2]_q/2)·ℏ_q²/bare`,
`κ = det G_cl / det G_q`. Truncating cost 11.06 ppb; that is now fixed in
`pyhecke`, `hecke_core_symbolic.alpha_em_inv_sym_exact`, and the meson script.

## The gap

**Exactly resummed, `α_em⁻¹ = 137.035935094` sits −467.6 ppb from CODATA
137.035999177.** Verified symbolically (ℚ(q,π)) and in mpmath, agreeing to
0 ppb. Order sweep for context:

| order | α_em⁻¹ | vs CODATA |
|---|---|---|
| 0 (bare) | 136.8232088536 | −1.55×10⁶ ppb |
| 1 | 137.0353672131 | −4611.7 ppb |
| 2 (old shipped) | 137.0359335780 | −478.7 ppb |
| 3 | 137.0359350899 | −467.7 ppb |
| **exact** | **137.0359350940** | **−467.6 ppb** |

Converged to 9 digits by order 3. **No further orders exist to add.** So the
residual is a defect in the tower's *structure*, not its truncation — a
qualitatively different (and sharper) target than before, when the truncation
could have been blamed.

## Candidate directions

1. **Is `κ` itself right?** It is a ratio of two Gram determinants of the CS
   pairing, classical over q-deformed. The classical Gram uses literal
   integers `m,n` (so no q enters, and it cancels nothing); the q-deformed one
   substitutes `[m]_q`. Whether that substitution is the correct deformation
   of the pairing — as opposed to, say, deforming the linking form too — is
   not derived anywhere I could find.
2. **Is the tower's *shape* right?** `1 + c₁ + c₁²κ + c₁³κ² + …` assigns one
   factor of `κ` per extra order. That is an assumption about how the damping
   iterates, not a derivation.
3. **Missing carriers.** The tower uses only `T₂,₉` and `T₃,₅`. Those are the
   genus-4 pair (`prop:torus-knot-genus-four-unique`), so the *selection* is
   derived — but whether the CS correction sees only them is a separate claim.

## Discipline

Anti-fit gated. Tuning `κ` or adding a coefficient to land on CODATA is a
**fit**, must be labelled one, and may not be wired. A derived change to the
structure that happens to reduce the residual is the only acceptable close;
a derived change that *increases* it is still a valid finding and should be
reported, not discarded.

Note the residual is ~468 ppb while the L2 target for a 100× pass on a
CODATA-precision observable is far tighter — so this is not a near-miss to
be polished, it is a real structural gap.

## Round 50 Formalization & 50-dps Witness (PR #8177)
- **Lean 4 Module (`0 sorry`, `0 axiom`, `0 vacuity`):** `folio/quantum-observable-universe/lean/QOU/AlphaEM/ChernSimonsTowerAndT35Linchpin.lean`
  - `csTower_order2_tail_identity` and `csTower_order3_tail_identity`: exact closed-form geometric tail identities $\text{full} - S_2 = -a_0 \varepsilon^3 / (1 + \varepsilon)$ ($+11.063\text{ ppb}$) and $\text{full} - S_3 = a_0 \varepsilon^4 / (1 + \varepsilon)$ ($+0.030\text{ ppb}$).
  - `csTower_tail_lt_30_of_ge_one`: for $\varepsilon = 1/366 > 0$, the geometric tail magnitude past order 2 is strictly below $30\text{ ppb}$, and the $-467.636\text{ ppb}$ CODATA residual (`csTower_structural_defect_decomposition`) is an order-independent structural defect of the single-ratio $\varepsilon = \kappa/([9]_q[10]_q)$ ansatz.
- **50-dps Witness:** `computations/probes/round50-zeta4-bridge-and-alpha-em-cs-tower.witness.json` (`scriptHash: e7bf4a93b887`, `scriptCommitSha: cf283b8e199f4643fb9e0259ec0a2702096bdd9b`).
- **PR:** `litlfred/qou#8177` (`https://github.com/litlfred/qou/pull/8177`, head SHA `3fdbeeb87a6b1821ff8d57a95f95d4d20cf72628`).
- **Status:** Kept at `status: in-progress` per reviewer-separated closure discipline.

## 2026-11-20 (PR #8562, bean qou-q0pl)
Four alpha functionals measured side by side at the one-term proton / two-term
(#8554) / muon pins (docs/audits/2026-11-20-alpha-em-two-term-q0-pull.md):
form B -0.365/+75.970/+78.998 ppb; form A +0.994/+77.329/+80.357; CS tower
-467.636/-390.982/-387.942; ruled-out 45[3]_q +2.588/+5.885/+6.016. Form B and
the CS tower are different functions of q (additive term 8/(12 pi) constant vs
pi^2(98/45)[2]_q/2 hbar_q^2), coincident only at q0 — not truncations of one
another. The gram_kappa_numerical_value sorry was a false statement and is
replaced by a sorry-free refutation; kappa = 1.7216 is det G_cl/det G_q and
never used gramKappa (bean qou-wkgp). Status unchanged: the CS-tower conjecture
class still has no instance.

## 2026-11-27 — Seifert κ at the convention-D Alexander variable (PR #9626)
Not previously recorded here: the 16-reading [m]_q family all miss (alpha_em_kappa_qdeformation_family_probe.py) and the 8×8 Seifert pairing κ(u) = 1/(u⁸Δ₂₉(u)Δ₃₅(u)) at u = q⁻¹ gives −24.53 ppb proton / +55.16 muon (alpha_em_seifert_kappa_pairing_probe.py, 2026-11-24). Convention D fixes the Burau variable at t = q^{∓2} (eigenvalue ratio −q⁻², same variable as AlphaEmT35Linchpin.lean Δ_{T(3,5)}(q²)). Pre-registered u = q⁻²: closed form κ_D = q¹⁶[2][9][3][5]/([18][15]) (exact sympy); result +1726.8 ppb proton / +1806.5 muon. Scope-limited negative (a). The −24.5 ppb figure is one of four members u ∈ {q^{±1}, q^{±2}} and uses a variable convention D does not supply: selection until t = q is derived. Pin floor: every member moves ≈80 ppb between pins, so sub-80-ppb closure waits on qou-2002. Audit docs/audits/2026-11-27-alpha-em-kappa-alexander-variable.md. Status unchanged.
