---
# qou-dk8a
title: 'OPEN: the connection matrix of the binding kernel L_K between 0 and infinity — the one surviving resurgence route'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T07:17:06Z
updated_at: 2026-10-04T15:13:25Z
parent: qou-v2om
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


---
**FIRST BRICK ANSWERED 2026-09-07 — literature only, no compute. The answer is NO for the formulae and YES for the method, and there is a convergence worth recording.**

The brick asked: *is `L_K` a twist of the Ramanujan equation Morita solves in `library/arxiv-1404.2541v1`?*

**Morita's family, exactly** (§4, Def 4.1 and eq. (10)):

    ( K·x·σ_q²  −  σ_q  +  1 ) u(x) = 0 ,    K ∈ C*

**`L_K`, from `binding-genfun-qdifference.md`:**

    ( (q²x − 1)·σ²  −  (q−1)·σ  −  (q−1) ) G = 0

**NO — and the obstruction survives the obvious twists.** Normalising `L_K` by `−(q−1)` gives coefficient triple `( −(q²x−1)/(q−1), 1, 1 )` against Morita's `( Kx, −1, 1 )`. A q-character twist `u ↦ μ^{log_q x}u` scales the triple as `(μ²a, μb, c)`, so `μ = −1` fixes the sign mismatch in `b`. What it cannot fix is the **leading coefficient's shape**: Morita's `Kx` is a *monomial*, vanishing only at `x = 0`, a **fixed point** of the q-action; `L_K`'s `q²x − 1` is a *binomial*, vanishing at `x = q⁻²`, a **non-fixed point** generating a q-spiral. A change of variable `x ↦ cx` fixes `0` and maps spirals to spirals, so it cannot carry a spiral zero onto the fixed point. **The finite singular locus differs in kind, not merely in position.**

Consequence: **`χ` is not in the literature.** There is no published connection formula to read off, and the "look it up" version of this bean is closed.

**But Def 4.1 is stated for a GENERAL second-order equation**, `a(x)u(q²x) + b(x)u(qx) + c(x)u(x) = 0` — not for his family only. So the *covering transformation* applies to `L_K` verbatim; only the *solved cases* do not. The route is therefore **"apply his method to `L_K`"**, not "cite his result", which is a substantially larger job: it needs the local solutions of `L_K` at both ends and two q-Borel–Laplace resummations, none of which exist.

**THE CONVERGENCE.** `binding-genfun-qdifference.md`'s own scope note predicts the needed structure: *"after a degree-2 **ramified** base change (adjoining `q^{1/2}`, `x^{1/2}`) the slope becomes the integer 1 and a scalar kernel does exist on the double cover, relating half-shifts — that is, even and odd body orders separately. That ramification is the missing structure, not a gap in the argument."*

Morita's Def 4.1 **is** that base change: `t² = x`, `p := √q`. Two independent lines — the corpus's Newton-slope argument and Morita's covering transformation — arrive at the same degree-2 ramified cover, and the corpus reached it without holding the paper. That raises confidence the ramified route is the right one; it does **not** supply any number.

**Re-scoping this bean.** Cost is now known to be large, not small. It sits behind `qou-brng` (which has a live, cheap, falsifiable target in `ρ_pp`) and should not be started until either that resolves or someone wants the resummation for its own sake. The anti-fit gate recorded above is unchanged and still applies.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 66 — PR #8274)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8274`](https://github.com/litlfred/qou/pull/8274) (branch `feat/round66-young-alien-lp-dt-spectral-43c1`, Commit 1 `efa6ab9e44128d259563d9e6208d6ab9d32edd74`, Commit 2 / Head `5423d4a1b0e6c19be96012412c48bd64329fdf2c`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/Mass/BindingNoAlienPlane.lean (`isoformalDim_two_slope_closed_form`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/young_kernel_alien_lp_dt_spectral_probe.py` (`scriptHash: 68202cff458f`) + `test/results/witnesses/young-kernel-alien-lp-dt-spectral.witness.json` (`allPassed: true`).
