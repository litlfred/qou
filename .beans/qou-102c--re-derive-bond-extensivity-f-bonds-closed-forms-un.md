---
# qou-102c
title: Re-derive bond_extensivity f_bonds closed forms under convention D (q^3/2 terms are C)
status: completed
type: task
priority: normal
created_at: 2026-08-11T11:21:04Z
updated_at: 2026-08-15T23:15:14Z
---


## Closed 2026-08-15 — it was never a re-derivation

All four files migrated. The premise of this bean was wrong in an instructive
way: the `q^{3/2}` terms that made these look like convention-C *derivations*
were the convention-C *substitution* of a form generic in `z`, expanded.
Verified symbolically in every case, not assumed:

| file | structural form | verified |
|---|---|---|
| `bond_extensivity_equal_weight` | `f_pp = z`, `f_nn = z − h`, `f_pn = z − h/2` | `f_nn == z_C − h` ✓, `f_pn == z_C − h/2` ✓ |
| `charge_symmetric_coulomb_binding` | same #2089 kernel | same |
| `mirror_split_coulomb_diagnosis` | same #2089 kernel | same |
| `lepton_t2n_torus_tower` | `W₂ = (qz+1)/(q²+1)`, `W₁₁ = q(q−z)/(q²+1)`, `tr_M(σ₁²) = 1 + hz` | exact match at `z_C` ✓ |

Writing the structural form back both migrates the convention and deletes the
expansion. Under D every factor is rational — D never leaves ℚ(q):

    f_pp = q³/(q²+1)   f_nn = 1/(q³+q)   f_pn = (q⁴+1)/(2q(q²+1))
    W₂ = (q⁴+q²+1)/(q²+1)²              W₁₁ = q²/(q²+1)²

**Independent confirmation.** Those W's are exactly `[3]_q/[2]_q²` and
`[1]_q/[2]_q²` — the convention-D weight formula `y_λ = [n−2k+1]_q/[2]_q^n` at
n=2, proved sorry-free in `TwoRowNormalisation.lean`. The Wenzl axiom solve and
the Lean formula agree without being told about each other.

**Costs, reported both ways.** `bond_extensivity` and `lepton_t2n` keep
`allPassed: True` — their conclusions are robust to the convention.
`mirror_split`'s headline `strong_csb_overshoots_3x` now fails; not attributed
to the convention, because that probe could not run on main at all (a
pre-existing `ALPHA_HBAR_C_MEV_FM` ImportError, fixed here) so it has no clean
before-value.

**Mistake worth keeping.** I migrated `lepton_t2n`'s numeric path and left its
symbolic path on C — an internal straddle. Its own
`trM_T2_3_symbolic_eq_numeric` assertion caught it, with a diagnostic
signature: computed unchanged, expected moved.
