---
# qou-siin
title: 'Pull through Solleveld: affine-Hecke HH is nonzero in higher degrees, and nothing cites it'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T21:16:54Z
updated_at: 2026-11-18T08:59:30Z
parent: qou-k4oq
---

`arxiv-1108.5286v3` (Solleveld, *Hochschild homology of affine Hecke algebras*)
is registered in `content/schema/references.ts` as `solleveld2022`, with the
library dir wired — and is **cited by zero content blocks**. Corpus-grepped
2026-08-25: `spectral sequence` and `filtration` return **nothing** from
`library/INDEX.md` across all 332 documents; `Hochschild` returns exactly this
one.

Its §3.1 gives, for the affine algebra,

    HH_*(H (x) Gamma)  ~=  (+)_{w in <W'>}  Omega^*(t_{rho_w})^{G_{rho_w}}

— algebraic forms of every degree, independent of q, by Morita invariance +
Hochschild-Kostant-Rosenberg.

**Why it matters here.** `prop:spectral-sequence-collapse` asserts HH^k = 0 for
k >= 1 and concludes everything sits in Z(A). That is right for the FINITE
generic H_n(q) (semisimple, Whitehead) and Solleveld does not contradict it. What
he establishes is the SCOPE of the no-go: the vanishing is a property of
finiteness, not of Hecke algebras. Higher degrees exist as soon as you leave the
finite algebra, and the corpus has an inductive-limit tower to leave it into
(`markov-trace-inductive-limit`, whose Lean already names "the infinite-dim
affine Hecke algebra" as open R&D).

**Lead, not a claim:** the classes are indexed by conjugacy classes of W — in
type A, partitions again — but valued in `Omega^j`, a de Rham degree the finite
centre does not have. A grading by form degree over a partition index is the
shape the body-order series of `conj:binding-manybody-eq-jet-filtration` wants.
Shape match only; the specialization has to be exhibited, not asserted.

**Two gates before spending real time.** (i) Solleveld's parameters are unequal
and not roots of unity, and the corpus evaluates at one real q0 ~ 1.10998.
(ii) The 2021 correction in the abstract touches the families-of-representations
construction rather than the HH computation, but read it before citing.

Analysis: `docs/audits/2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md` §5.


## Gates checked 2026-08-25 — there are THREE, not two; (i)+(ii) pass, (iii) is open

**(i) Parameter regime — PASSES.** Section 1.1 defines *equal* parameters
(q(s) constant on S_aff) and *positive* parameters (q(s) in R_{>0}).
"Possibly unequal" in the abstract is a GENERALISATION; equal is the special
case. The corpus sits at a single real q0 ~ 1.10998 — positive, not a root of
unity. Nothing excludes it.

**CONVENTION TRAP inside that gate.** Solleveld's Hecke relation (eq. 2) is

    (N_s - q(s)^{1/2})(N_s + q(s)^{-1/2}) = 0

against the corpus's `(sigma_i - q)(sigma_i + q^-1) = 0` (AGENTS.md §7a). So
**Solleveld's q is the corpus's q^2**; his q^{1/2} is our q. At the anchor that
is q_Sol = q0^2 ~ 1.23206, NOT 1.10998. He notes the literature also defines the
algebra via q(s)^{1/2} N_s. Any numeric transfer that skips this is off by a
square root — the same shape as the convention-C/D confusion.

**(ii) The 2022 correction — DOES NOT BLOCK, with two hedges.** It lands in §2.1
and §2.2 (pp. 16-22) on the construction of families of representations, and it
DOES reach §3.1, which picks its families "as in Corollary 2.5". But the repair
is in the same note: families satisfying Lemma 2.3 exist when the parameters are
of "geometric type" (via [AMS, §3.3]), and "for most positive-valued q one can
use the technique with parameter deformations from [Sol4, proof of Lemma 6.4]",
after which "the remainder of the paper is valid without further changes." The
corpus is positive-valued, so it is inside the rescued regime.

Hedges: "most" is not "all"; and **"geometric type" is undefined in this paper** —
one occurrence, in the correction, pointing outward to [AMS]. (My own reading,
not on the page: type-A equal-parameter affine Hecke is the
Kazhdan-Lusztig/Steinberg-variety case and should BE geometric type, making the
first bullet apply directly. Confirm against [AMS §3.3] before relying on it.)

**(iii) HOMOLOGY IS NOT COHOMOLOGY — OPEN. This one is a gate on my own framing.**
`prop:spectral-sequence-collapse` is about HH^k (COhomology). Solleveld computes
HH_* (homology). For a separable finite-dimensional algebra both vanish above
degree 0, so the corpus's §1 claim is unaffected — but non-vanishing of HH_* does
NOT formally imply non-vanishing of HH^* for an infinite-dimensional algebra.
Whatever relates them here (a duality, smoothness, the Schwartz completion of
§3.3) must be supplied, not assumed. Until it is, Solleveld bounds the SCOPE of
the corpus's claim rather than contradicting its dual.

**Next step, cheapest first:** settle (iii). If HH_* and HH^* are not related for
this algebra, the shape-match lead is weaker than the note first suggested and
should be re-scoped before anyone builds on it. §3.3 (Schwartz algebras) is the
place to look.


## Gate (iii) CHECKED — not closed, and it SPLITS the lead (2026-08-25)

Read §3, §3.1, §3.3 for a bridge between homology and cohomology. **There is
none.** `HH^` never appears; no duality or Poincare statement anywhere; the sole
"cohomology" occurrence is about CYCLIC homology of smooth commutative algebras.

Theorem 3.1 is proved at the COMPLEX level, in the Hochschild CHAIN complex
`C_n(A) = A^{(x)n+1}` with boundary `b_n`, by exhibiting representative CYCLES:
"every element of HH_*(H (x) Gamma) can be represented by a Hochschild cycle in
(+)_w ^w C_*(O(t_w))". The cochain complex `Hom(A^{(x)n}, A)` has no automatic
dual of that step. **The cohomological statement is not a transport — it is a
separate piece of work.**

(My own reading, NOT on the page, so do not cite it as corpus: for the smooth
commutative local model O(t) that HKR governs here, both sides are nonzero in
higher degrees — HH_n = Omega^n and HH^n = wedge^n Der. So no a-priori
obstruction; the EXPECTATION is that cohomology also carries higher degrees.
Expectation, not result.)

**The split, which is the useful part:**

| reading of Solleveld | needs HH^*? | status |
|---|---|---|
| scopes the corpus no-go ("vanishing is a property of finiteness") | YES — the corpus claim is cohomological | WEAKENED; qualify it |
| supplies a graded home for the body-order series | NO — any extra grading serves | UNTOUCHED |

The second was the interesting half and it survives intact. So the lead is NOT
dead; it is narrowed to the half that never needed cohomology.

**Bonus from the proof.** Theorem 3.1's hypothesis is "there exists eps in C^x
such that k_alpha in eps*R for all alpha in R" — real parameters up to scaling.
The corpus's real positive q0 gives real k, so it holds. Independently
reinforces gates (i) and (ii).

**Next step is no longer gate (iii).** With the split established, the live
question is the one the second row points at: does `Omega^j` over a
conjugacy-class index specialize to the body-order series of
`conj:binding-manybody-eq-jet-filtration`? That needs the specialization
exhibited (and the q-vs-q^2 offset above applied), not asserted.


## The specialization question, first measurement (2026-08-25)

Probe: `computations/probes/solleveld_form_degree_vs_body_order_probe.py`
(exact — Fractions and ints only, Gaussian elimination over Q, no float, emits
no witness).

**Measured, n = 2..7, every conjugacy class of S_n:**

    dim t_w  =  dim( t / (w-1)t )  on the reflection rep  =  #cycles(w) - 1

so the top de Rham degree the summand `Omega^*(t_{rho_w})^{G_{rho_w}}` can carry
at class `w` is `#cycles(w) - 1`.

**DIRECTION — this is the finding.** The grading is DEEPEST on the identity class
(n cycles, top degree n-1) and COLLAPSES to a scalar on an n-cycle (1 cycle,
degree 0). Under the natural reading of binding — an n-body bound cluster merges
n strands into ONE closure component, i.e. one longer cycle — more binding means
FEWER cycles, hence a LOWER top degree. The body-order series of
`conj:binding-manybody-eq-jet-filtration` needs depth that GROWS with cluster
size. **It shrinks.**

**SCOPE-(a), explicitly not (b).** This refutes the de Rham degree as the
body-order index UNDER THAT READING of body order as cycle merging. It does not
prove no map exists: a different assignment of body order to cycle data, or a
sum ACROSS classes rather than a degree WITHIN one, is untouched, and no proved
invariant forbids either. Do not upgrade this to an exclusion.

**Index-set caution, NOT an obstruction.** Solleveld sums over CONJUGACY CLASSES;
the corpus's Wedderburn form `tr_M = sum_lambda y_lambda chi_lambda` sums over
IRREPS. For S_n both are partitions of n, but they are different roles paired by
the character table — and the corpus's Frobenius pairing already carries BOTH
indexings (`chi_lambda` evaluated at the class of `rho(beta)`). So the two index
sets meet exactly where the corpus already works. Do not read the shared word
"partition" as an identification; equally, do not treat the difference as a
barrier.

**Next.** The surviving route is the sum ACROSS classes, not the degree within
one: whether `sum_w` over classes with a fixed cycle count reproduces a
body-order term. That is a different calculation and this probe says nothing
about it.


## The ACROSS-class route: survives every test here, then waits on an open bridge

Probe PART 2, same file, same exactness discipline (ints and `comb` only).

    rank HH_j  =  sum_{lam |- n} C(#parts(lam) - 1, j)

since `dim t_w = c(w) - 1` (PART 1) and `Omega^j` of a d-dimensional space is
free of rank `C(d, j)`.

     n  #classes  top deg  rank at j = 0..5
     4         5        3  [5, 7, 4, 1, 0, 0]
     8        22        7  [22, 64, 94, 92, 63, 29]
    12        77       11  [77, 322, 711, 1113, 1350, 1292]
    15       176       14  [176, 892, 2421, 4741, 7398, 9484]

**1. Degree 0 reduces to the corpus's centre.** `rank HH_0 = #classes = p(n)`,
and the Wedderburn centre is indexed by irreps, also `p(n)`. So the affine object
RESTRICTS in degree 0 to exactly the per-lambda form the corpus already uses, and
adds degrees `1..n-1` on top — the "graded home" shape wanted. **Caution kept in
the probe output:** `p(n)` counts classes and irreps BY DEFINITION, so this is a
count agreement showing the reduction is dimensionally consistent, not a
structural identification. Do not cite it as one.

**2. It PASSES the invariant that killed the within-class reading.**
`prop:jet-filtration-binding-extensive` needs the number of graded pieces to GROW
with the cutoff A. The atom word sits in `H_{3A}(q)`, so `n = 3A` and the top
degree is `3A - 1`, against `A - 1` body orders needed. `3A - 1 >= A - 1` for
every A and both grow linearly. **ROOM IS NOT A MAP** — no assignment of body
order to degree is exhibited, and finding one is the open work.

**3. The real blocker is structural, and the corpus already named it.**
Solleveld's theorem is about the AFFINE algebra. The corpus's atom word lives in
the FINITE `H_{3A}(q)`, semisimple at generic q — so for it the whole grading
COLLAPSES to degree 0 and none of the above exists. Using any of this requires
the inductive limit, and `markov-trace-inductive-limit.lean` says of exactly
that construction, verbatim:

> "The full operator-theoretic construction (von Neumann inductive limit on the
> infinite-dim affine Hecke algebra) is the open R&D content."

**So the honest status of this bean:** the lead is not refuted and not confirmed.
It clears the direction test, the growth test and the degree-0 reduction, and
then stops at a bridge the corpus has independently marked open. Anyone picking
it up should know the mathematical work is not the obstacle — the missing object
is.


## CROSS-LINK 2026-08-30 — this bean's OBSERVATION 3 is also `qou-o6ml`'s route-(3) blocker

`qou-o6ml` (EM-linking invariant attack, front 4-B) lists as its route (3) *"the
h-graded per-pair Hecke trace channel at H_2A with Hochschild-homology
classification of trace functionals (Solleveld 1108.5286, uploaded)"* — the same
theorem this bean pulls through, aimed at the EM per-pair weight `w_ij` instead
of at the body-order series.

It inherits this bean's finite-vs-affine wall unchanged: the corpus's word lives
in the **finite** `H_{3A}(q)`, the grading collapses to degree 0, and reaching
the higher degrees needs the inductive limit that
`markov-trace-inductive-limit.lean` marks open R&D. `qou-o6ml` did not name that
blocker and was listing route (3) as its unblocked front; corrected there today.

**One thing `qou-o6ml`'s framing adds that this bean did not state.** It asks for
an **h-graded** channel. Solleveld's grading is by **de Rham form degree** and
Theorem 2 says `HH_*` is *independent of `q`* — which this bean records — so
there is no grading by powers of `h = ℏ_q` to look for at all. `h` enters only
through the centre's action, i.e. the `c_{w,i}(q)` shifts of Theorem 1.c. That is
a finite, explicit datum rather than a grading, and it is the *encouraging* half
of the reading: a no-tuned-constant object of exactly the kind 4-B's GATE wants.
Worth stating here because anyone taking this bean forward for either target will
otherwise search for the wrong object.

Also carried across: the convention trap in this bean's gate (i) — Solleveld's
`q` is the corpus's `q²`, so `q_Sol = q₀² ≈ 1.23206` — now recorded on
`qou-o6ml` too.

- Round 76 (`lane-e667`): Formalized `qou-gmfz`, `qou-img9`, `qou-phir`, `qou-siin`, `qou-l25z` in `QOU.Foundations.TriangularBarInvolutionLengthTwoQuadraticDefectRightMultiplicationDichotomyRootParameterRescalingWritheHomomorphism` with 80-dps `mpmath` 2-commit witness stamp (`1d514d8cc14cab86cdbfe50f0bca4313a91a6db7` -> `8fbc40e0a853ba6aa21eab5cf4d1947155a2d115`, `scriptHash=b5b4b562fbd04cd73aa5a68e31eebc858e55abd805cb24915d3a249d657d689c`) in PR `litlfred/qou#8409` (`status: in-progress`).
