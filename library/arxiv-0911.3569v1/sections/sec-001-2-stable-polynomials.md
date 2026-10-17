---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-001-2-stable-polynomials
section_title: "Stable polynomials."
section_number: 2
pages: 2-2
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
we use parts of the forgoing for Borcea and Br¨and´en’s splendid proof of the Grace-
Walsh-Szeg˝o Coincidence Theorem. In Section 5, the Grace-Walsh-Szeg˝o Theorem
is used to extend the results of Section 3 from multiaﬃne to arbitrary stable polyno-
mials. This culminates in an amazing multivariate generalization of the P´olya-Schur
Theorem, the proof of which requires the development of a multivariate extension
of the Szasz Principle (which is omitted, regretfully, for lack of space). Section 6
presents Borcea and Br¨and´en’s resolution of some matrix-theoretic conjectures of
Johnson. Section 7 presents the derivation by Borcea, Br¨and´en, and Liggett of neg-
ative association inequalities for the symmetric exclusion process, a fundamental
model in probability and statistical mechanics. Section 8 presents Gurvits’s sweep-
ing generalization of the van der Waerden Conjecture. Finally, Section 9 brieﬂy
mentions a few further topics that could not be included fully for lack of space.
I thank Petter Br¨and´en kindly for his helpful comments on preliminary drafts of
this paper.
2. Stable polynomials.
We use the following shorthand notation for multivariate polynomials. Let [m] =
{1, 2, ..., m}, let x = (x1, ..., xm) be a sequence of indeterminates, and let C[x] be the
ring of complex polynomials in the indeterminates x. For a function α : [m] →N,
let xα = xα(1)
1
· · · xα(m)
m
be the corresponding monomial. For S ⊆[m] we also let
xS = Q
i∈S xi.
Similarly, for i ∈[m] let ∂i = ∂/∂xi, let ∂= (∂1, ..., ∂m), let
∂α = ∂α(1)
1
· · · ∂α(m)
m
and let ∂S = Q
i∈S ∂i. The constant functions on [m] with
images 0 or 1 are denoted by 0 and 1, respectively. The x indeterminates are always
indexed by [m].
Let H = {z ∈C : Im(z) > 0} denote the open upper half of the complex plane,
and H the closure of H in C. A polynomial f ∈C[x] is stable provided that either
f ≡0 identically, or whenever z = (z1, ..., zm) ∈Hm then f(z)̸ = 0. We use S[x]
to denote the set of stable polynomials in C[x], and SR[x] = S[x]∩R[x] for the set
of real stable polynomials in R[x]. (Borcea and Br¨and´en do not consider the zero
polynomial to be stable, but I ﬁnd the above convention more convenient.)
We rely on the following essential fact at several points.
Hurwitz’s Theorem (Theorem 1.3.8 of [14]). Let Ω⊆Cm be a connected open
set, and let (fn : n ∈N) be a sequence of functions, each analytic and nonvanishing
on Ω, which converges to a limit f uniformly on compact subsets of Ω. Then f is
either nonvanishing on Ωor identically zero.
Consequently, a polynomial obtained as the limit of a convergent sequence of
stable polynomials is itself stable.
