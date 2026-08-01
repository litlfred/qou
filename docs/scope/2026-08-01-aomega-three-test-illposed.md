# qou-l15q: the 4₁→5₂ test for "why 3" is ill-posed as designed — rank 2 vs rank 3

**Date:** 2026-08-01 · **Bean:** `qou-l15q` (arc successor to `qou-bbsy`) · **Tier:** scope correction, pre-compute.
**No probe was run. Nothing fitted, nothing wired.** This note exists because reading
the corpus before computing (AGENTS.md §anti-guessing) invalidated the test design.

## The design that failed

#4447 certified that `A_ω = 3` is the **Stokes structure constant** of 4₁:

$$
S^+_{12}(q) + S^+_{21}(q) = 3\,S^+_{11}(q)
$$

exact as an integer q-series (GGM 2012.00062 symmetry eq 65), Lean-formalized in
[`StokesSymmetryConstant.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstant.lean).
Bean `qou-l15q` proposed deciding **why 3** by computing the analogous constant `c`
for 5₂, since two structural candidates split sharply there:

| candidate | 4₁ | 5₂ prediction |
|---|---|---|
| (A) \|disc(trace field)\| | \|−3\| = 3 ✓ | **23** |
| (B) \|Alexander middle coeff\| | \|+3\| = 3 ✓ | **3** |

## Why it does not work

The corpus already carries the 5₂ Stokes machinery
([`qbeta_5two_stokes_barodd_index_probe.py`](../../computations/probes/qbeta_5two_stokes_barodd_index_probe.py),
GGM §6 eqs 24–29, 100a/b, 102, 112–124). Reading it:

| knot | Stokes matrix | q→0 limit | off-diagonal integers |
|---|---|---|---|
| 4₁ | **2×2** | `[[1,3],[0,1]]` (eq 60) | **one**: 3 |
| 5₂ | **3×3** | `[[1,4,0],[0,1,0],[−3,−9,1]]` (eq 100a) | **three**: 4, −3, −9 |

The rank is the number of flat connections, which tracks the degree of the trace
field (4₁: quadratic, `ℚ(√−3)`; 5₂: cubic, disc −23). So:

1. **There is no single "the 5₂ Stokes constant"** to compare against 23 or 3.
   The test presupposed a scalar that does not exist at rank 3.
2. **The symmetry eq (65) is a rank-2 statement.** It has no 3×3 analogue in GGM;
   the structural relation they give for 5₂ is the *inversion* relation
   `S⁺(q)ᵀ·S⁻(q) = 1` (Conjecture 1(b), eq 4), which constrains a matrix pair and
   does not isolate an integer.

## What the 5₂ integers do and do not say

- **23 does not appear** among {4, −3, −9}. That is *not* a clean refutation of
  candidate A, because the quantity A predicts (a single Stokes constant) is not
  defined here — one cannot refute a prediction the test cannot evaluate.
- **3 does appear**, as `|−3|` (the (3,1) entry). This is **not evidence for
  candidate B.** Selecting one of three off-diagonal integers *post hoc* because it
  matches is precisely the numerology this repo forbids (AGENTS.md §anti-fit). With
  three integers available, hitting any given small number is unremarkable.
- Likewise, combinations that reach 23 (e.g. `3·9 − 4`) are **not** recorded as
  findings. Free choice of combining rule over three integers can reach almost any
  target; a rule must be *derived* before its output counts.

**Both candidates therefore remain untested, not decided.** No support and no
refutation for either.

## What a well-posed test needs

Before any 5₂ number can adjudicate "why 3", one must first fix **which Stokes
datum plays the `A_ω` role at rank > 2** — a derivation, not a choice. That is the
same channel-identification gap #4447 recorded on the 4₁ side (`A_ω` is σ₁σ₂ while
the proven x-refinement is σ₁σ₁, and the σ₁σ₂ x-refinement is absent from the
literature). Concretely, one of:

1. **Derive the role from the T5 channel.** `A_ω` enters as
   `S_K = A_ω·κ·(ln²q₀ − ϑ_K²)`; deriving which matrix element that coefficient is
   would fix the rank-3 generalization by construction rather than by pattern.
2. **Find a rank-general symmetry.** If GGM's eq (65) is the rank-2 shadow of a
   general relation, its rank-3 form would supply the constant. The inversion
   relation is the candidate to interrogate.
3. **Test candidate A on another rank-2 knot instead** — a knot whose trace field
   is quadratic, where "the" Stokes constant is well-defined exactly as for 4₁, and
   where |disc| ≠ |Alexander middle coefficient| so the candidates still separate.
   This is the cheapest well-posed route and does not require solving (1) or (2).

Route 3 is the recommended next step: it keeps the original falsifiable structure
and only changes the test knot to one where the question is meaningful.


## Addendum (same day): route 3 is **also** blocked — there is no second rank-2 knot

Route 3 above ("re-run on a different rank-2 knot") was the recommended redesign.
Checking it against the corpus before acting kills it too.

Rank 2 means a **quadratic imaginary invariant trace field**. For knot complements
in S³ that is essentially the figure-eight alone: **Reid (1991) established 4₁ as
the unique arithmetic hyperbolic knot** — already cited in-corpus at
[`hyperbolic-volume-transcendence.md`](../../content/quantum-observable-universe/predicted-spectra/hyperbolic-volume-transcendence.md)
and [`three-knot-jet-order-independence.md`](../../content/quantum-observable-universe/predicted-spectra/three-knot-jet-order-independence.md).
Strictly, Reid gives *arithmetic ⇒ 4₁*, and quadratic-imaginary-trace-field ⇒
arithmetic needs integral traces (non-integral traces would force a closed
essential surface, Bass), so a non-arithmetic knot with quadratic trace field is
not excluded by Reid alone. But **no second example is known in the corpus or the
standard census**, so route 3 has no candidate to run on. Recorded as
*no-known-candidate*, not as a theorem.

### What is actually available at rank 2: links, not knots

| manifold | invariant trace field | \|disc\| | in-corpus compute |
|---|---|---|---|
| 4₁ | ℚ(√−3) | 3 | GGM sandwich (#4447) |
| Whitehead link | ℚ(i) | **4** | [`2026-07-26-whitehead-vc-verification-and-p-exponent.md`](../audits/2026-07-26-whitehead-vc-verification-and-p-exponent.md); #4400 |
| Borromean rings | ℚ(i) | **4** | `borromean_3d_index.py`, `borromean_kashaev_positive_sum_probe.py` |

Both are arithmetic with trace field ℚ(i), and both already have corpus machinery.
Candidate A predicts a Stokes constant of **4** for each.

**But the test degrades from two-sided to one-sided**, and this must be stated
plainly rather than glossed:

1. **Candidate B becomes inapplicable.** Links have *multivariable* Alexander
   polynomials; "the middle coefficient" is not defined without an extra choice.
   So a link test can support or refute A, but **cannot adjudicate A against B** —
   which was the entire point of the original design.
2. **Rank must be verified, not assumed.** Quadratic trace field does not by itself
   guarantee a 2×2 Stokes matrix; the rank is the number of boundary-parabolic
   representations. For 4₁ these are the geometric rep and its conjugate. That the
   same holds for Whitehead/Borromean is **plausible but unverified here**.
3. **Confound to control.** The 5₂ q→0 matrix already contains a 4 among
   {4, −3, −9}, and \|disc ℚ(i)\| = 4. A "4" appearing for Whitehead or Borromean
   would need to be shown *not* to be the generic small-integer coincidence before
   it counts as support for A.

### Honest status of the arc

The "why 3" question now has **no cheap well-posed test**. The original two-candidate
design required a second rank-2 *knot*, and none is available. What remains:

- **One-sided link test** (Whitehead/Borromean, prediction 4) — cheapest, but only
  probes A, with confound (3) to control.
- **Close the channel gap** (routes 1–2 above): derive which matrix element the T5
  `A_ω` is, which would define the rank-3 generalization and re-open 5₂ properly.
  This is the principled route and the one the arc actually needs.

Recommendation: do **not** run the link test as a candidate-adjudicator — it cannot
do that job. Run it only if a *derived* rule for "which Stokes datum is `A_ω`"
exists first, in which case 5₂ becomes available too and is the better test.

## Cross-references

- Bean `qou-l15q` (re-scoped by this note); predecessor `qou-bbsy` (#4447).
- [`2026-08-01-3bp8-entirety-and-channel-correctness.md`](../audits/2026-08-01-3bp8-entirety-and-channel-correctness.md) §2 (the channel gap), §4 (the structure constant).
- AGENTS.md §"Before declaring refuted" (why this is *untested*, not refuted);
  §"Axiomatization is NOT a Proof"; §anti-fit.
