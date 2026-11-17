---
# qou-q7ga
title: 'ROAST: the q-deformation is NET-NEGATIVE on binding — derived asymmetry +2(q0-1)(N-Z) has the wrong sign (data wants ~-0.15), and layout-free bond counting (A-1) beats every isospin-resolved variant'
status: in-progress
pr: 8265
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T07:07:35Z
updated_at: 2026-10-04T15:13:50Z
parent: qou-v2om
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
**(d) The missing term is the symmetry energy** — measured at -0.804, and
the route I pointed it at is CLOSED. **CORRECTED 2026-09-04, same day.** `qou-ubsl` is **completed and closed**,
and I promoted it off its title without reading its body. It is closed twice
over, and the first reason is *this arc's own Lean result*: the trace annihilates
every partition with `ℓ(λ) > 2` (`QOU/Hecke/RowCap.lean`), so the SU(4)-
distinguishing shapes — which need up to four rows — carry **zero weight**; and
on the two-row shapes that survive, `C₂^{GL(4)} − C₂^{GL(2)} = 2n`, a constant at
fixed strand number, so the SU(4) label collapses to the SU(2) isospin the trace
already carries. Its own text also concedes that the Casimir yields `(N−Z)²`,
not `(N−Z)²/A` — the `1/A` is Fermi-gas level density, a separate dynamical
input this framework does not have.

**So the measurement stands and the inference does not.** The residual's
dominant shape IS the symmetry energy (−0.804). What is *not* true is that this
points at a live route: the natural algebraic source is structurally forbidden.
That is worse news than "top lead", not better — the symmetry energy is a named
gap with **no available route**, and the tractable open item is back to the
2.656 scale factor (`qou-59j5`).

> 🛑 **SUPERSEDED 2026-09-05.** There IS a route — the p-n interface count — and
> it is **sign-locked** rather than absent. A bond sum is additive in
> `L = −log b`, so it compares `b_pn` against the *geometric* mean of `b_pp`,
> `b_nn`, while the construction delivers an *arithmetic* one; AM ≥ GM, so the
> sign is backwards structurally. `√(b_pp·b_nn) = 1/[2]_q` exactly, the AM−GM gap
> is `h²/(2[2]_q)` (the Hecke parameter itself), and the crossing weight
> `1/(q²+1)` is `½` only at `q = 1` — the corpus sits **11.7 %** above it.
> `QOU/Hecke/SymmetrySignAmGm.lean` (7 decls),
> `qbeta_symmetry_sign_is_am_gm_locked_probe.py`, bean `qou-i01a`. A repair must
> move ONE quantity: the convex weight `w` below `1/(q²+1)`.


## Independent corroboration from main — `pn-bond-cannot-be-extremal` (merged 2026-09-04)

A sibling landed `folio/quantum-observable-universe/mass-theory/pn-bond-cannot-be-extremal.md`
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


## 2026-09-04 (qou-hfjc) — the wrong-signed asymmetry has a derived explanation: it is the writhe factor nu^e of the UN-normalised trace. The forced link-invariant normalisation (nu = q⁻², mu = [2]_q, both from the two Markov moves) gives every single-crossing bond the weight q/(q²+1), so κ_derived = 0 identically and the law is pure bond counting — the shape this bean measured as empirically best (p5–p95 1.1809, reproduced to 5 figures). Lean sorry-free; see docs/audits/2026-09-04-forced-link-normalisation-bond-counting.md.

## 2026-09-05 — synthesis landed

`docs/audits/2026-09-05-binding-law-arc-synthesis.md` §6 item 2 carries this
bean's result: the derived isospin asymmetry has the wrong sign and layout-free
bond counting beats every isospin-resolved variant. Recorded there alongside the
route the corpus has already CLOSED for the symmetry energy (`qou-ubsl`: the
`l(lambda) > 2` row cap gives SU(4) labels zero weight), which is why the
dominant missing term has no obvious algebraic source. That is the honest
headline of what remains.

## 🛑 REVERSED 2026-09-05 — the deformation is net-negative only on ONE bar branch

This bean concluded that "the q-deformation is NET-NEGATIVE on binding" because
layout-free bond counting beat every isospin-resolved variant. **That holds for
the branch the corpus took, and not for the other one.**

`qbeta_asymmetry_sign_is_a_bar_branch_probe.py` (6/6):

    law                            p5-p95    full    corr (N-Z)^2/A^2
    as built    p-p = sigma        1.22497  10.18       -0.804
    BAR-SWAPPED p-p = sigma^-1     1.16633   7.37       -0.493
    no asymmetry (count only)      1.18054   8.21       -0.697

The bar-swapped branch **beats bond counting** on p5-p95 and full range and
nearly halves the symmetry-energy correlation. So the deformation is
net-negative as built and net-POSITIVE swapped, and this bean's headline needs
that qualifier.

Also corrected: this bean's asymmetry coefficient `2(q_0-1) = 0.21996` is the
FIRST-ORDER value. The exact one is `2 ln q_0 = 0.2086814` — from
`b_pp = q^2/[2]_q`, `b_nn = q^-2/[2]_q` (`qou-xf14`), the bond energies are
`ln[2]_q -/+ 2 ln q` identically. Use the exact value.

Full working and the unpinnedness result: `qou-y2np`.
## 2026-09-04 (qou-yau0) — one row revised on the artifact-free law: the residual's asymmetry correlation is −0.6965 (not −0.804) and the surface correlation is −0.298 (not −0.178) once the writhe artifact is removed; 'wrong by 4×' becomes 2.3×, and the surface term is a live lead again. Control reproduces the un-normalised numbers to 3 dp. docs/audits/2026-09-04-normalised-law-residual-shape.md.


## 2026-09-05 (later) — SECOND supersession: the corpus already HAS a T(T+1)/A term

Independent of the AM-GM finding above. `mass-theory` carries the Wigner energy
`-Delta_W . T(T+1)/A`, built from SELF-CONJUGATE shadow prices
(`unified-iterative-correction-proof.md`, `figure-eight-branching-rule-proof.md`).
The symmetry energy has a derived route -- in the MASS channel. This bean's
"named gap with no available route" was wrong about the corpus, not just about
the mechanism.

Tension, stated as one: self-conjugacy forces `l(lambda) = lambda_1`, so the row
cap `l <= 2` leaves exactly three self-conjugate shapes -- `(1)`, `(2,1)`,
`(2,2)`, none at any level >= 5. Of the two the mechanism names, `(2,2)`
survives and `(3,1,1)` has zero Markov weight. **Whether `y_lambda = 0` forces
`C_lambda = 0` is NOT established** and is not assumed. `qou-a5jk`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
