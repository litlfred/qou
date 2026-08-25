---
# qou-siin
title: 'Pull through Solleveld: affine-Hecke HH is nonzero in higher degrees, and nothing cites it'
status: todo
type: task
priority: normal
created_at: 2026-08-25T21:16:54Z
updated_at: 2026-08-25T21:17:20Z
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
