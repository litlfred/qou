---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-030-51-cohomology-and-duality
section_title: "Cohomology and duality"
section_number: 5.1
pages: 18-21
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
---
introduced for homology in (3.1). Let A be an algebra, and let σ be an algebra
automorphism of A. The twisted Hochschild cohomology groups HH ∗
σ(A) of A with
respect to σ were deﬁned in [KMT] in a way exactly analogous to the twisted
homology groups discussed in (3.1). When σ is diagonalisable the argument of
[HK1, Proposition 2.1] applies to show that, for all i ≥ 0,
HH i
σ(A) ∼= H i(A, σA).
Moreover [We, Corollary 9.1.5] can be invoked to show that, for all i ≥ 0,
H i(A, σA) ∼= Exti
Ae(A, σA).
Deﬁnition. (a) The Hochschild cohomological dimension of A is
Hcdim A = max{i | HH i(A) = H i(A, A) ⁄= 0}.
(b) The twisted Hochschild cohomological dimension of A is
tHcdim A = max{i | H i(A, σA) ⁄= 0 for some automorphism σ of A}.
(c) We say that A has ﬁnite homological dimension if there is an integer d such
that H i(A, −) = 0 for all i > d .
In the presence of the Van den Bergh condition introduced in (4.3) t here is a
beautiful twisted version of Poincar´ e duality for A. An object X in the derived
category D(A-Mod) is called compact if the functor Hom D(A−Mod)(X, −) commutes
with coproducts. It is well-known that X is compact if and only X is quasi-
isomorphic to a perfect complex over A (namely, X is quasi-isomorphic to a bounded
complex of ﬁnitely generated projective A-modules).
Proposition. [VdB1] Let A be an algebra of ﬁnite homological dimension d. Sup-
pose that the Van den Bergh condition holds, and that A is a compact object in
D(Ae-Mod). Then for every A-bimodule N ,
H i(A, N) = Hd−i(A, U ⊗A N )
NOETHERIAN HOPF ALGEBRAS 19
for all i, where U is the invertible A-bimodule Extd
Ae(A, Ae).
The above result provides further evidence that, at least for rigid Gorenstein
algebras, twisted (co)homology is an important and necessary par t of the study
of Hochschild homology and cohomology. Note that the hypothesis o f A being
compact in D(Ae-Mod) does not appear in [VdB1]; it has been pointed out to us
by Van den Bergh that this is an oversight.
Corollary . Let A be a noetherian rigid Gorenstein algebra with Nakayama auto -
morphism ν. Suppose that A has ﬁnite homological dimension d and that A is a
compact object in D(Ae-Mod).
(a)
Hd(A, Aν ) ∼= Z(A) ⁄= 0,
and so tHdim A = d.
(b)
H d(A, ν A) ∼= A/[A, A].
If A has a non-zero module of ﬁnite k-dimension then tHcdim A = d.
Proof. By deﬁnition U = 1Aν . Let V = U −1 = ν A1.
(a) By Proposition 5.1,
Hd(A, 1Aν) ∼= H 0(A, A) ∼= Z(A) ⊃ k.
(b) By Proposition 5.1,
H d(A, ν A1) ∼= H0(A, U ⊗A νA1) ∼= H0(A, A) = A/[A, A].
Suppose that A has a non-zero ﬁnite dimensional module. We claim that 1 ⁄∈
[A, A], so that A/[A, A] ⁄= 0. To see this we can pass to a ﬁnite dimensional factor
ring of A and assume that A is a simple ﬁnite dimensional algebra, hence a central
simple algebra. In that case it is well-known that 1 ⁄∈[A, A].
When A/[A, A] ⁄= 0, then H d(A, ν A1) ⁄= 0 and hence tHcdim A = d. □
5.2. Poincar´ e duality for Hopf algebras. In parallel to Proposition 3.3 for
Hochschild dimension, there is an easy upper bound for the twisted c ohomological
dimension of a Hopf algebra. Throughout this subsection we assume S is bijective.
Lemma. Let A be a Hopf algebra of ﬁnite global dimension d.
(a) A has ﬁnite homological dimension, bounded by d. This says that A has
a resolution of projective left Ae-modules bounded at position −d. Conse-
quently, tHcdim A ≤ d.
(b) If A is noetherian, then k is a compact object in D(A-Mod).
(c) If A is noetherian, then A is a compact object in D(Ae-Mod).
Proof. (a) By [We, Corollary 9.1.5], for all i ≥ 0,
H i(A, M) ∼= Exti
Ae (A, M)
for every A-bimodule M . By Lemma 2.4(b),
Exti
Ae(A, M) ∼= Exti
A(k, L(M )) = 0
for all i > d .
(b) This is trivial since A is noetherian and k has a bounded resolution of ﬁnitely
generated projective left A-modules.
20 K.A. BROWN AND J.J. ZHANG
(c) By part (b) k is quasi-isomorphic to a prefect complex in D(A-Mod). Hence,
for each i, Ext i
A(k, −) commutes with inductive direct limits in A-Mod. Recall
that A-Mod is a Grothendieck category and, in particular, inductive direct limits
are exact [Po, Chapter 2]. Since L(−) is a composition of a restriction functor
with an invertible functor, it also commutes with inductive direct limits. Hence
Exti
A(k, L(−)) commutes with inductive direct limits in Ae-Mod. By Lemma 2.4(b),
for any Ae-module M ,
Exti
Ae(A, M) ∼= Exti
A(k, L(M ))
for all i. Therefore Ext i
Ae (A, −) commutes with inductive direct limits for all i.
Together with part (a) and the claim in the next paragraph we show t hat A is
compact in D(Ae-Mod).
It remains to show the following: if M is a left Ae-module of ﬁnite projective
dimension such that Exti
Ae(M, −) commutes with inductive direct limits for all i,
then M has a projective resolution such that each term in the resolu tion is a ﬁnitely
generated projective left Ae-module. Since Hom Ae(M, −) commutes with inductive
direct limits, M is ﬁnitely presented by [Po, Theorem 3.5.10]. So we have a short
exact sequence
0 → M −1 → P 0 → M → 0
where P 0 is a ﬁnitely generated projective left Ae-module. Clearly Ext i
Ae(P 0, −)
commutes with inductive direct limits for all i. Using the long exact sequence we
obtain that Ext i
Ae(M −1, −) commutes with inductive direct limits for all i. Then
induction on the projective dimension of the Ae-module M shows that M has a
resolution by ﬁnitely generated projective left Ae-modules. □
The following corollary is an immediate consequence of Propositions 5.1 and 4.5
and the above lemma.
Corollary . Let A be a noetherian AS-regular Hopf algebra of global dimension d.
Suppose that S is bijective, and let ξ be the winding automorphism induced by the
left integral, (2.5.1). Then for every A-bimodule M and for all i, 0 ≤ i ≤ d,
H i(A, M) = Hd−i(A, ξ−1S−2
M ).
5.3. Proof of Theorem 0.4(b). Given an A-bimodule M, we let [ A, M] denote
the k-subspace of M spanned by {am − ma : a ∈ A, m ∈ M }. It is easy to see that
H0(A, M) = A ⊗Ae M = M/[A, M].
The following result follows from Corollary 5.2, and incorporates the r emainder of
Theorem 0.4(b).
Theorem. Let A be a noetherian AS-regular Hopf algebra of global dimension d
and having bijective antipode S. Deﬁne ν = ξS 2.
(a) For every algebra automorphism σ of A,
H d(A, σA) ∼= A ⊗Ae ν−1σA = ν−1σA/[A, ν−1σA].
(b) In particular,
H d(A, ν A) ∼= A/[A, A] ⁄= 0,
and so tHcdim A = d.
(c) Hcdim A = d if and only if Aν/[A, Aν] ⁄= 0.
NOETHERIAN HOPF ALGEBRAS 21
