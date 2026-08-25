---
# qou-gwio
title: 'GAP: alpha_em structural residual -468 ppb survives exact resummation — what is missing from the CS tower''s STRUCTURE (not its order)?'
status: todo
type: task
priority: normal
created_at: 2026-08-07T01:00:00Z
updated_at: 2026-08-07T01:00:00Z
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
