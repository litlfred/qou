---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-005-3-negative-dependence-in-mathematics-and-physics
section_title: "Negative Dependence in Mathematics and Physics"
section_number: 3
pages: 13-15
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — W e introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polyno mials that amount"
---
3.1. Real Stable Polynomials and T ranscendental Entire F unctio ns. In
[15] it was proved that a multi-aﬃne polynomial f ∈ R[z1, . . . , zn] is stable (in the
sense of Deﬁnition 2.9) if and only if
∂f
∂zi
(x) ∂f
∂zj
(x) ≥ ∂2f
∂zi∂zj
(x)f (x) (5)
14 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
for all x ∈ Rn and 1 ≤ i < j ≤ n (see also Theorem 4.1 in §4 below). Therefore, a
stable multi-aﬃne polynomial with non-negative coeﬃcients is Rayleigh /h-NLC+.
As we will prove in §4, such polynomials are in fact CNA+.
Clearly, by setting all variables equal in a stable polynomial one gets a uni-
variate stable polynomial. Hence, if f (z1, . . . , zn) is stable then so is its diagonal
specialization (see Deﬁnition 2.8)
∆( f )(t) =
n∑
k=0
(n
k
)
cktk.
A univariate polynomial with real coeﬃcients is stable if and only if it has all real
zeros, so the familiar Newton inequalities (cf., e.g., [22, 38]) imply that f satisﬁes
the conclusion of Conjecture 2.4 if f is stable with non-negative coeﬃcients.
Multivariate generalizations of Newton’s inequalities for homogeneous real stable
polynomials with non-negative coeﬃcients were obtained in [8, Theore m 3]. Corol-
laries 2 and 3 of op. cit. show that the coeﬃcients of (symmetric) such polynomials
also satisfy unimodality properties in the sense of majorization/sto chastic domina-
tion [61]. In §4.3 we establish natural analogs of these results for truncations o f
(non-homogeneous) multi-aﬃne stable polynomials with non-negativ e coeﬃcients.
The well-known Laguerre-Tur´ an inequalities for univariate polynomials and tran-
scendental entire functions in the Laguerre-P´ olya class [22] amo unt to saying that
the sequence of Taylor coeﬃcients of such a function is SLC (Deﬁnit ion 2.8). One
can argue that both Newton’s inequalities and the Laguerre-Tur´ an inequalities are
natural manifestations of negative dependence properties enco ded in the geometry
of the zero sets of these functions. Indeed, as we will see in §4, the geometric
features of real stability (Deﬁnition 2.9) are a key tool in our study of negative de-
pendence properties for strongly Rayleigh measures and allow us to establish many
such properties for this class of measures, including:
• the strongest form of negative association (CNA+);
• closure under operations (i)–(vi) deﬁned in §2.1;
• closure under symmetric homogenization;
• stochastic domination properties for truncations;
• the ULC property for rank sequences.
Rayleigh polynomials that are not stable do not seem to have a geomet ric de-
scription by means of their zero sets similar to that of stable polynom ials. This may
explain why several negative dependence properties fail for arbit rary (non-strongly)
Rayleigh polynomials/measures (see §7).
We summarize below some of the closure properties of real stable po lynomials
(see [8, 9] for their proofs) that we need for later use.
Proposition 3.1. Let Hn(R) be the set of all real stable polynomials in n variables.
(1) f ∈ H n(R) if and only if for any λ ∈ Rn
+ and µ ∈ Rn the univariate
polynomial t ↦→f (λt + µ) has all real zeros;
(2) If f ∈ H n(R) has degree dj in variable zj, j ∈ [n], then
• ∂jf ∈ H n(R) ∪ {0} for 1 ≤ j ≤ n;
• f (z1, . . . , zj−1, αzj, zj+1, . . . , zn) ∈ H n(R) for j ∈ [n], α > 0;
• f (z1, . . . , zj−1, β, zj+1, . . . , zn) ∈ H n−1(R) ∪ {0} for j ∈ [n], β ∈ R;
• zd1
1 · · · zdn
n f (λ1z−1
1 , . . . , λnz−1
n ) ∈ H n(R) if ±(λ1, . . . , λn) ∈ Rn
+;
• f (z1, . . . , zi−1, zj, zi+1, . . . , zn) ∈ H n−1(R) for i ⁄= j ∈ [n].
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 15
(3) If {fj}∞
j=1 ⊂ H n(R) and f ∈ R[z1, . . . , zn] \ {0} is the limit, uniformly on
compact subsets of Cn, of the sequence {fj}∞
j=1 then f ∈ H n(R).
Important examples of real stable polynomials are given by the follow ing con-
struction (see, e.g., [8, 9]).
Proposition 3.2. Let A1, . . . , Am be (complex) positive semi-deﬁnite matrices and
let B be a (complex) Hermitian matrix, all matrices being of the sa me size.
(1) The polynomial
z = (z1, . . . , zn) ↦→f (z) = det( z1A1 + · · · + zmAm + B) (6)
is either identically zero or real stable;
(2) If B is also positive semi-deﬁnite then f has all non-negative coeﬃcients.
In particular, if Z = diag( z1, . . . , zm) and A is a positive semi-deﬁnite m × m
matrix then det(A + Z) is a multi-aﬃne real stable polynomial with all non-negativ e
coeﬃcients, hence a (positive) constant multiple of a stron gly Rayleigh polynomial
(cf. Deﬁnition 2.10).
Proof. By the second part of Proposition 3.1 and a density argument, it suﬃ ces to
prove (1) in the case when all matrices Aj, 1 ≤ j ≤ m, are positive deﬁnite. Set
z(t) = λt + µ with λ = (λ1, . . . , λn) ∈ Rn
+, µ = (µ1, . . . , µn) ∈ Rn, and t ∈ C. Note
that P :=∑ m
j=1 λj Aj is positive deﬁnite and thus it is invertible and has a square
root Q (recall that R+ = (0, ∞)). Then
f (z(t)) = det( P ) det(tI + QHQ ∗),
where H := B +∑ m
j=1 µjAj is a Hermitian matrix. Therefore, f (z(t)) is a polyno-
mial in t that is a constant multiple of the characteristic polynomial of a Herm itian
matrix and so it must have all real zeros. By the ﬁrst part of Propo sition 3.1, this
proves (1), and then (2) follows by noticing that the coeﬃcients of the polynomial in
(6) are products of non-negative numbers, namely principal minor s of the positive
semi-deﬁnite matrices A1, . . . , Am, B. □
Further properties of (not necessarily multi-aﬃne) real stable po lynomials, their
linear preservers and applications to entire function theory in one o r several vari-
ables, matrix theory, combinatorics, convex optimization and stat istical mechanics
may be found in [7, 8, 9, 15, 19, 36, 51].
