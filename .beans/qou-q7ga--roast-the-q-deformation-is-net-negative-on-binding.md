---
# qou-q7ga
title: 'ROAST: the q-deformation is NET-NEGATIVE on binding — derived asymmetry +2(q0-1)(N-Z) has the wrong sign (data wants ~-0.15), and layout-free bond counting (A-1) beats every isospin-resolved variant'
status: in-progress
type: task
created_at: 2026-09-04T07:07:35Z
updated_at: 2026-09-04T07:07:35Z
---

Measured 2026-09-04 on 2548 AME nuclides with MEASURED binding energies
(`computations/qbeta/qbeta_tower_log_z_and_roast_probe.py`, 9/9).

**The structure.** At `q = 1` all five closed-form factors equal exactly `z = 1/2`
(verified symbolically), so the additive law degenerates to a pure bond count.
Expanding in `e = q - 1`: `b_pp = 1/2 + e`, `b_pn = 1/2 + 0.e`, `b_nn = 1/2 - e`
— the p-n interface has NO first-order term and the like-species bonds split
symmetrically. Hence

    B = E_0.[ ln2.(A-1) + 2(q0-1).(N-Z) ] + O(e^2)

**(a) The asymmetry has the wrong sign.** Derived `+2e = +0.2200`; scanning
`kappa` in `B ~ ln2(A-1) + kappa(N-Z)` the data optimum is `kappa ~ -0.15`.
Adding the derived term makes p5-p95 WORSE, 1.1809 -> 1.2230.

**RETRACTION.** `docs/audits/2026-09-04-binding-law-options-decision-frame.md`
read `b_pp > b_nn` as "the sign Coulomb repulsion would give ... a prediction,
not a fit". Correct as ALGEBRA, wrong as EVIDENCE: in aggregate the splitting
pushes the wrong way. Corrected in that note and in
`qbeta_binding_law_options_probe.py`.

**(b) Bond counting wins.** p5-p95: segregated 1.2250, alternating 1.2323,
all-pairs 1.2262, **layout-free `(A-1)` 1.1809**. So the measured content of the
additive law is `B ~ const.A` — the SEMF volume term — and the q-deformation's
contribution to it is net-negative.

**What this does NOT refute.** That the algebra produces an EXTENSIVE quantity at
all, which Option A did not; and the closed form itself, whose `q=1` collapse and
`b_pp = z` identity are exact.

**Open.** Is the deformation wrong, or is it right and being read through the
wrong edge set / the wrong observable? Note (c) below says the edge set is not
the culprit. The live suspect is that `-ln b` is not the per-bond energy.

**(c) The ordering gap barely touches B** -> see `qou-48is`.
**(d) The missing term is the symmetry energy** -> see `qou-ubsl`.

## Independent corroboration from main — `pn-bond-cannot-be-extremal` (merged 2026-09-04)

A sibling landed `content/quantum-observable-universe/mass-theory/pn-bond-cannot-be-extremal.md`
reaching the same defect from `A = 2` instead of from 2548 nuclides, with the
same numbers: `L_pp = 0.489899`, `L_pn = 0.676822`, `L_nn = 0.907262`, and
`alpha = 2.0507 MeV` — which is exactly this arc's `E_0.|ln z|`, so the two
calibrations are the same object.

Its argument: `d_pn` is a convex combination of `d_pp` and `d_nn` with weights
`(1/2 +/- delta/4)`, the two-strand trace is affine in the offset, and
`L = -log(z+d)` is strictly decreasing, so **`L_pp < L_pn < L_nn` for every
`q > 0` and every `delta in (0,2)`** — not just to first order. At `A = 2`
exactly one of the three binds and it is `pn`, so a constant ranking binding
strength must put `pn` at an EXTREME, and a convex combination never is. The
deuteron is overshot by `1.274x` — the same figure measured here.

**The two findings are one fact.** Their convexity is why `b_pn`'s first-order
term in `e = q-1` vanishes (this bean's symbolic result: `+1, 0, -1`), and that
vanishing is why the aggregate asymmetry comes out `+2e(N-Z)` with the wrong
sign. Structural at `A = 2`; measured at `-0.15` vs `+0.2200` over the table.

Their caveat is worth carrying: `L` is spinless and the real distinction is the
`3S1` triplet, so a spinless constant should not be expected to separate bound
from unbound — but that does not excuse the ORDER, which comes from the
averaging convention and would survive into a spin-resolved theory keeping the
same letter.
