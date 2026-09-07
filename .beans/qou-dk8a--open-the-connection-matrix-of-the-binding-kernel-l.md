---
# qou-dk8a
title: 'OPEN: the connection matrix of the binding kernel L_K between 0 and infinity — the one surviving resurgence route'
status: todo
type: task
priority: normal
created_at: 2026-09-07T07:17:06Z
updated_at: 2026-09-07T07:17:06Z
---

**The target is the binding gap.** As of `docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md` the gap is a SHAPE gap (22.5 % p5–p95), not a scale gap (0.99 %), and its one unlocated piece is the irreducibly many-body term: the connected 3-body cumulant `b3 = +1.4262 MeV` against a model value of exactly `0`. The audit locates the cause — `b3 = 0` is a shadow of semisimplicity (`HH^k(H_n(q),H_n(q)) = 0` at generic q), so a trace on that algebra has nowhere to store a 3-body datum.

**What is already EXCLUDED (do not re-attempt).** `QOU/Mass/BindingNoAlienPlane.lean` (this session, sorry-free, lean-direct exit 0): the binding series has no alien plane on EITHER side.

- q-side: `L_K = (q^2 x - 1)s^2 - (q-1)s - (q-1)` is pure isoclinic of slope 1/2 (`BindingScalarKernelParityExclusion`, sorry-free); Ramis–Sauloy math/0611521 §2.2 verbatim — pure modules "are irregular objects WITHOUT WILD MONODROMY". No q-alien derivations, no Stokes operators.
- classical side: `BindingGevreyHalf` proves Gevrey-1/2, so the level-1 Borel transform is entire — no alien derivatives in that plane either.

Prior art for the dimension-count half: bean `qou-qbp5` / the Bugeaud note in `references.ts`, which adds that Bugeaud's NON-INTEGRAL generalisation is still a TWO-slope theory — so ramifying to integralise the slope does not manufacture a second slope.

**THIS BEAN IS THE CRACK THOSE EXCLUSIONS LEAVE.** `RSZIsoformalInterface.lean`'s docstring separates two objects that were conflated three times before, at the cost of three retracted claims:

- LOCAL isoformal moduli at `∞` — dimension 0 for `L_K`. **Closed.**
- GLOBAL connection matrix `P = Y0^{-1} Y_inf` between theta-normalised solutions at `0` and at `∞`, and its invariant `chi = P00·P11/(P01·P10)`. **Untouched for `L_K`.**

The second is not a local Stokes datum, so purity says nothing about it. For C1 it is settled (`qou-wgnx`: trivial, target dissolved) — but `L_K` is a DIFFERENT MODULE that merely shares a Newton polygon with C1's `L1`. Do not transfer that verdict.

**FIRST BRICK, cheap and decisive — do this before anything else.** Morita, *The Stokes phenomenon for the Ramanujan's q-difference equation and its higher order extension* (`library/arxiv-1404.2541v1`, held) computes exactly this object: "connection formulae of local solutions between the origin and the infinity", by two q-Borel–Laplace resummations, for a rank-2 q-difference equation. Question: **is `L_K` equivalent to (a twist of) the Ramanujan / q-Airy equation Morita solves?** If yes, `chi` is already in the literature and is read off, no bespoke resummation. If no, the route needs one built. Either answer is progress and neither needs compute.

**ANTI-FIT GATE — read before extracting any number.** `chi` is ONE number and `b3` is ONE number. Matching them without deriving WHY is a fit, and this arc has been burned once already: `qou-brng` records the saturated-fraction ≈ ℏ_q² coincidence as "more likely numerology than a derived prediction" after its one candidate mechanism was refuted. Do not wire a `chi`-to-`b3` match. The deliverable is a derivation of the map, or an honest negative.

**SECOND GATE, upstream and load-bearing.** `G(x;q)`'s relation to `b3` is CONDITIONAL on `conj:binding-manybody-eq-jet-filtration`, an open conjecture. So even a computed `chi` attaches to `B_3` in the generating function, not to the measured AME cumulant, until that conjecture closes. State the conditionality in anything written.
