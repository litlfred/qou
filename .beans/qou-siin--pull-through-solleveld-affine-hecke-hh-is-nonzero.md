---
# qou-siin
title: 'Pull through Solleveld: affine-Hecke HH is nonzero in higher degrees, and nothing cites it'
status: todo
type: task
priority: normal
created_at: 2026-08-25T21:16:54Z
updated_at: 2026-08-25T21:24:53Z
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
