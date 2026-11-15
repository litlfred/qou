---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-001-t-x-shk-is-dualizable-in-particular-we-can-assoc
section_title: "X+ ∈SH(k) is dualizable. In particular, we can associate to X a natural Euler characteristic χ(X/k) ∈EndSH(k)(1k), deﬁned as the composition"
section_number: T
pages: 1-4
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
toc_source: inferred
doc_brief: "Motivic Gauss–Bonnet formulas — 12 sections: Front matter; Introduction; X+ ∈SH(k) is dualizable. In partic"
---
associate to X a natural Euler characteristic χ(X/k) ∈EndSH(k)(1k), deﬁned as the composition
1k
δ→6∞
T X+ ∧k (6∞
T X+)∨τ→(6∞
T X+)∨∧k 6∞
T X+
ϵ→1k,
where the maps δ and ϵ are the coevaluation and evaluation that comprise the duality, and τ is the
symmetry isomorphism.
MSC2010: primary 14F42; secondary 55N20, 55N35.
Keywords: motivic homotopy theory, Chow ring, Euler characteristics, hermitian K-theory.
1801
1802
Marc Levine and Arpon Raksit
For k perfect, a theorem of Morel identiﬁes EndSH(k)(1k) with the Grothendieck–Witt group GW(k),
i.e., the Grothendieck group of k-vector spaces equipped with a nondegenerate symmetric bilinear form.
Hence, we may think of the Euler characteristic χ(X/k) as a class in GW(k). It is then natural to wonder
whether there is an explicit interpretation of this Euler characteristic in terms of symmetric bilinear forms.
An intuitive speculation is that the Euler characteristic should be given by the value of some cohomology
theory on X, equipped with an intersection pairing.
One of the main results in this paper is to make precise and conﬁrm this speculation. To state the
result, we recall that classes in GW(k) can be represented not just by nondegenerate symmetric bilinear
forms on k-vector spaces, but also by nondegenerate symmetric bilinear forms on perfect complexes
over k (see Section 8D for a review of what this means). With this in mind, we give the following explicit
interpretation of the Euler characteristic χ(X/k).
Construction 1.2. Suppose that X is of pure dimension d. Then we have the Hodge cohomology groups
Hi(X;  j
X/k) for 0 ≤i, j ≤d and the canonical trace map
Tr : Hd(X; d
X/k) →k.
We deﬁne a perfect complex of k-vector spaces (with zero differential),
Hdg(X/k) :=
d
M
i, j=0
Hi(X,  j
X/k)[ j −i],
and the trace map deﬁnes a nondegenerate symmetric bilinear form on Hdg(X/k) via the pairings
Hi(X,  j
X/k) ⊗k Hd−i(X, d−j
X/k) ∪→Hd(X, d
X/k)
Tr
−→k,
where the ﬁrst map denotes the cup product (that this is indeed a nondegenerate symmetric bilinear form
will be shown in Section 8D). We thus obtain a Grothendieck–Witt class (Hdg(X/k), Tr) ∈GW(k). This
construction extends in an evident manner to the case that X is not necessarily of pure dimension.
The next formula for χ(X/k) was proposed by J-P. Serre (private communication to Levine, 28.07.2017).
Theorem 1.3. Assume that k is a perfect ﬁeld of characteristic different from two. Then χ(X/k) =
(Hdg(X/k), Tr) ∈GW(k).
We prove a more general result over a base-scheme B; see Theorem 8.6 and Corollary 8.7 for details.
If k =R, a class in GW(k) is determined by two Z-valued invariants, rank and signature, and Theorem 1.3
reproves the following known result (see [Abelson 1976, Theorem 1; Kharlamov 1974, Theorem A]).
Corollary 1.4. Suppose that k = R and X is of even pure dimension 2n. Then the symmetric bilinear form
Hn(X, n
X/R) × Hn(X, n
X/R) ∪→H2n(X, 2n
X/R)
Tr
−→R
has signature equal to χtop(X(R)), the classical Euler characteristic of the real points of X in the analytic
topology. In particular, we have
|χtop(X(R))| ≤dimR Hn(X, n
X/R).
Motivic Gauss–Bonnet formulas
1803
This is Corollary 8.8 in the text.
Besides giving an explicit formula for the rather abstractly deﬁned χ(X/k), Theorem 1.3 opens the way
to computing χ(X/k) in the situation that X is a twisted form of another k-scheme Y, namely by twisting
the symmetric bilinear form (Hdg(Y/k), Tr) by the descent data for X. This cannot be done with the class
χ(Y/k) ∈GW(k), as GW(−) does not satisfy Galois descent. This is discussed in detail in Section 8E.
Let us now explain our methods for proving Theorem 1.3. The idea is to use the theory of Euler classes
in motivic cohomology theories. More speciﬁcally, our focus is on cohomology theories represented
by SL-oriented motivic ring spectra; recall that this refers to a commutative monoid object E in SH(k)
equipped with a compatible system of Thom classes for oriented vector bundles (where an orientation is a
speciﬁed trivialization of the determinant line bundle). The example of interest for proving Theorem 1.3 is
hermitian K-theory; other examples of interest include Chow–Witt theory, ordinary motivic cohomology,
and algebraic K-theory (the last two are actually GL-oriented, meaning they have Thom classes for all
vector bundles). The assumption that k has characteristic different from two in Theorem 1.3 arises from
this use of hermitian K-theory, which at present is only known to satisfy the properties we need when
char(k)̸ =2; we do not know of any counter-examples to our formula for χ(X/k) for k of characteristic two.
Given an SL-oriented motivic ring spectrum E ∈SH(k), one may deﬁne certain pushforward maps in
twisted E-cohomology. Namely, if Y and Z are smooth quasiprojective k-schemes, f : Z →Y is a proper
morphism of relative dimension d ∈Z, and L is a line bundle on Y, then there is a pushforward map
f∗: Ea,b(Z; ωZ/k ⊗f ∗L) →Ea−2d,b−d(Y; ωY/k ⊗L),
where ω−/k denotes the canonical bundle. This is deﬁned abstractly via the six-functor formalism for
motivic stable homotopy theory.
We note two key examples of these pushforwards, assuming our smooth projective variety X is of pure
dimension d for simplicity:
– The structural morphism π : X →Spec (k) gives a pushforward map
π∗: E2d,d(X, ωX/k) →E0,0(Spec k).
– Given a vector bundle p : V →X, the zero section s : X ,→V gives a pushforward map
s∗: E0,0(X) →E2d,d(V ; p∗det−1(V )).
The ﬁrst should be thought of as a kind of integration map. The second allows us to deﬁne the Euler
class of a vector bundle V →X,
eE(V ) := s∗s∗(1) ∈E2d,d(X; det−1(V )),
where s again denotes the zero-section, and 1 ∈E0,0(X) denotes the unit element.
Using the above notions, we may state the following motivic version of the classical Gauss–Bonnet
formula equating the Euler characteristic with the integral of the Euler class of the tangent bundle; this
result is a fairly immediate consequence of [Levine 2017b, Lemma 1.5]:
1804
Marc Levine and Arpon Raksit
Theorem 1.5 (motivic Gauss–Bonnet). Let E be an SL-oriented motivic ring spectrum in SH(k). Let
u : 1k →E denote the unit map, inducing the map u∗: GW(k) ≃10,0
k (Spec k) →E0,0(Spec k). Then
u∗(χ(X/k)) = π∗(eE(TX/k)) ∈E0,0(Spec k).
A general motivic Gauss–Bonnet formula is also proven in [Déglise et al. 2018, Theorem 4.6.1], which
implies the above formula by applying the unit map. Our method is somewhat different from [Déglise
et al. 2018] in that we replace their general theory of Euler classes with the more special version for
SL-oriented theories used here; see Theorem 5.3 below for our general statement of this result.
As stated above, we deduce Theorem 1.3 from Theorem 1.5 by considering the example of hermitian
K-theory, E = BO. In this case, the map u∗: GW(k) →BO0,0(Spec k) is an isomorphism. The deduction
requires an explicit understanding of both the Euler class eE(TX/k) and the pushforward π∗in hermitian
K-theory; the former is fairly straightforward, but the latter requires new input.
What we do is identify the abstractly deﬁned projective pushforward maps in hermitian K-theory with the
concrete ones deﬁned in terms of pushforward of sheaves and Grothendieck–Serre duality. This comparison
follows from a uniqueness result we prove for pushforward maps in an SL-oriented theory E, characterizing
them, under certain further hypotheses on E, in terms of their behavior in the case of the inclusion of
the zero-section of a vector bundle (which is governed by Thom isomorphisms). We leave the detailed
statement of this result to the body of the paper (see Theorem 7.1), as it would take too long to spell out here.
Remark 1.6. Bachmann and Wickelgren [2020] discussed results closely related to those discussed here.
For example, they identiﬁed the abstract pushforward maps in hermitian K-theory with those deﬁned by
Grothendieck–Serre duality in the case of a ﬁnite syntomic morphism (as opposed to the case of a smooth
and proper morphism between smooth schemes addressed here). Moreover, combining their identiﬁcations
of various Euler classes with our motivic Gauss–Bonnet formula, one may recover Theorem 1.3 above.
Outline. The paper is organized as follows. In Section 2, we review the basic framework of motivic
homotopy theory, as well as relevant aspects of the dualizability result Proposition 1.1. In Section 3, we
review basic facts about SL-oriented motivic ring spectra. In Section 4, we describe the abstractly deﬁned
pushforwards in the twisted cohomology theory arising from an SL-oriented motivic ring spectrum. In
Section 5, we prove the general Gauss–Bonnet formula for SL-oriented motivic ring spectra. In Section 6,
we axiomatize the features of the twisted cohomology theory arising from an SL-oriented motivic ring
spectrum. In Section 7, we use these axioms to prove our unicity/comparison theorem characterizing the
pushforward maps in SL-oriented theories. Finally, in Section 8, we apply the previous results in speciﬁc ex-
amples of SL-oriented theories to obtain various concrete consequences, in particular proving Theorem 1.3.
