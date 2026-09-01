---
doc_id: arxiv-1011.0679v2
doc_title: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS"
section_id: sec-001-11-affine-hecke-algebras
section_title: "Affine Hecke algebras"
section_number: 1.1
pages: 3-4
source_pdf: 1011.0679v2.pdf
source_sha256: 6fa4bbcf4e908373
---
for admissible representations π,π ′ of L. Here the space C ell denotes the space of
regular semisimple elliptic conjugacy classes of L, equipped with the canonical “el-
liptic measure” dγ as deﬁned by Kazhdan [Kaz], and θπ denotes the locally constant
function on C ell determined by the distributional character of π. Thus “Kazhdan’s
conjecture” expresses EP (π,π ′) as an orthogonality pairing of the characters of π
and π′ with respect to the elliptic measure d γ on the set C ell.
The second ingredient is Arthur’s formula expressing the ri ght hand side of (2) in
terms of R-groups. More precisely, let P ⊂L be a rational parabolic subgroup with
Levi component M , and let σ be a smooth irreducible representation of M , square
integrable modulo the center of M . The representation I L
P (σ), the smooth normal-
ized parabolically induced representation from σ, is a tempered admissible unitary
representation ofL. The decomposition of I L
P (σ) is governed by the analytic R-group
Rσ, a ﬁnite group which acts naturally on the real Lie algebra Ho m(X ∗(M ), R) of
the center of M . For r ∈ Rσ we denote by d(r) the determinant of the linear
transformation 1 −r on Hom(X ∗(M ), R). Let π be an irreducible tempered repre-
sentation of L which occurs in I L
P (σ) (denoted by π ≺ I L
P (σ)). The theory of the
analytic R-group asserts that ρ = Hom L(π, I L
P (σ)) is an irreducible projective Rσ-
representation. We still assume that F has characteristic zero and that the center
ofL is compact. Applying the local trace formula for L, Arthur [Art, Corollary 6.3]
showed that for all tempered irreducible representations π,π ′ ≺ I L
P (σ) one has
(3)
∫
Cell
θπ(c−1)θπ′(c)dγ(c) = |Rσ|−1 ∑
r∈Rσ
|d(r)| trρ(r) trρ′(r)
(In fact Arthur allowed L to have noncompact center, but he had to adjust (3) to
make the integral converge.) Combining (2) and (3), one arri ves at the following
formula provided that F has characteristic zero :
(4) EPL(π,π ′) = |Rσ|−1 ∑
r∈Rσ
|d(r)| trρ(r) trρ′(r).
This is the “formula of Arthur” referred to in the title of thi s paper. Before we
assumed that L had compact center, but that is not necessary for (4). If the c enter
of L is not compact, the equality is not very interesting however , as both sides are
zero. The left hand side by the argument of [ScSt, Lemma III.4 .18.ii] and the right
hand side because every r ∈ Rσ ﬁxes the subspace of Hom(X ∗(M ), R) corresponding
to the F-split part of the center of L pointwise, so d(r) = 0.
The main results of the present paper are:
Theorem 1. (See Theorem 3.1.)
The natural analog of equation (4) for EPH for aﬃne Hecke algebras with arbitrary
positive parameters holds true.
In this result we use the notion of analytic R-groups for aﬃne Hecke algebras as
introduced in [DeOp2]. The proof of Theorem 1 is completely d iﬀerent from the
arguments sketched above leading to equation (4), and is rat her elementary in com-
parison to the aforementioned deep results in p-adic harmonic analysis. Although
we wrote it down only in the case of aﬃne Hecke algebras, this p roof of Theorem 1
applies to all reductivep-adic groups. In particular this observation proves:
4 ERIC OPDAM AND MAARTEN SOLLEVELD
Theorem 2. (See Remark 3.2.)
Let L be a connected reductive group deﬁned over an arbitrary non- archimedian local
ﬁeld F. Then (4) holds for L = L(F).
The elliptic integral in (2) and (3) does not seem to have an ob vious counterpart
in the setting of aﬃne Hecke algebras. Analogues are known fo r the Euler–Poincar´ e
pairing of representations of either a ﬁnite Weyl group [Ree ] or of an (extended) aﬃne
Weyl group W e [OpSo1, Theorem 3.3]. To relate these to EPH one must compare
EPH and EPW e, which is done in [Ree, Section 5.6] (for aﬃne Hecke algebras with
equal parameters) and in [OpSo1, Chapter 3]. Recent results from [Sol3] allow us
to conclude that GC(H) modulo the radical of EPH equals the vector space Ell( H)
of ”elliptic characters”, and that this space does not depen d on the parameters q
(Theorem 2.3).
Arthur’s formula applies only to the Euler-Poincar´ e pairi ng of tempered char-
acters. In an abstract sense this no restriction, as it follo ws from the Langlands
classiﬁcation of irreducible characters of H in terms of standard induction data in
Langlands position, that modulo the radical of the pairing EPH any irreducible
character is equivalent to a virtual tempered character. Bu t this is complicated in
practice, and therefore our formula does not qualify as an ex plicit formula for EPH
for general non-tempered irreducible characters. It would therefore be desirable to
extend the result to general ﬁnite dimensional representat ions of H. In the ﬁnal
section of this paper we make a ﬁrst step by extending the deﬁn ition of the analytic
R-group to non-tempered induction data. We show that its irre ducible characters
are in natural bijection with the Langlands quotients assoc iated to the induction
datum. However, we have not been able to generalize the Arthu r formula to this
case.
