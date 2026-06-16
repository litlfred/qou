# Color vs charge: which weighted crossing closes the T-vs-³He split

**Status:** FINDING (reproducible). The inter-nucleon interface is currently
the **color-blind** averaged crossing `σ − h/2`. Two weighted refinements
are candidates for the bond-type asymmetry that splits ³H (8.482 MeV) from
³He (7.718 MeV) — a **0.764 MeV ≈ 9.5 %** gap. This doc quantifies which one.

Probe: [`binding_color_vs_charge_tn3he.py`](../../computations/binding_color_vs_charge_tn3he.py)
(witness `binding-color-vs-charge-tn3he.witness.json`). Zero fit; E₀ = CAL-3.

## The two candidate weightings

| weighting | crossing | scale | source |
|-----------|----------|-------|--------|
| **COLOR** (`bring_color_weighted`) | `f = z − h·(1/2 − δ/4)` | δ ≈ **1.4e-3** | `flavor_split_subleading` (QCD flavor / Δm_pn) |
| **CHARGE** (Coulomb) | EM repulsion of like charges | α_EM ≈ **7.3e-3** | α_EM sector (PR #1521/#1523/#1549) |

Per-bond color weight `(1 + δ·asym + δ²·sym)`, `asym = (N−Z)/(3A)`:
pp → −1/3, pn → 0, nn → +1/3.

## Result — color is the right sign but ~2 orders too small

| bond | B₀ (color-blind) | color weight | shift |
|------|------------------|--------------|-------|
| pp | +2.2856 | 0.99954 | **−0.046 %** |
| pn | +2.3043 | 1.00000 | +0.0001 % |
| nn | +2.2488 | 1.00046 | **+0.046 %** |

- needed T−³He split: **+0.764 MeV** (9.5 %)
- color-weighted split: **−0.035 MeV** → color supplies **−4.55 %** of needed
  (right local sign B_nn > B_pp, but ~**22× too small** and net wrong sign,
  because the base sub-braid bonds already favour ³He by 1.6 %).

The color per-bond shift scale is `δ/4 ≈ 3.4e-4` vs the needed ~0.095. This
matches `_li_2_q_util.py:246`: Bring-color-tube quark weighting is
"structurally insufficient" for mass *gaps* — it lives at the **Δm_pn scale
(0.14 %)**, not the T-vs-³He scale.

## Conclusion

- **The T-vs-³He split is CHARGE (Coulomb), not color.** ³He's two protons
  repel (α_EM sector, ~5× larger than δ, reaching ~MeV with the geometric
  factor), reducing ³He binding → T > ³He. That is the charge-weighted
  crossing (task 1), to be built against PR #1521/#1523/#1549.
- **Color averaging is still wired everywhere** (the audit task): it is the
  correct, derived Δm_pn-scale refinement and reproduces Δm_pn to 0.14 %.
  It is simply not the dominant T-vs-³He mechanism.
- Neither addresses the dominant A=3 residual (~15 %), which is **per-bond
  growth** (separate, task 2).

Three independent effects, three scales:

| effect | weight | scale | closes |
|--------|--------|-------|--------|
| color-averaged crossing | QCD flavor δ | 0.14 % | Δm_pn |
| charge-averaged crossing | α_EM | ~MeV / 9.5 % | T−³He |
| per-bond growth | embedding density | ~15 % | bulk A=3 |
