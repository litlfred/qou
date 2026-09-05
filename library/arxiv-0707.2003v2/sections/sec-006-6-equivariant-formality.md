---
doc_id: arxiv-0707.2003v2
doc_title: "A geometric model for Hochschild homology of Soergel bimodules BEN WEBSTER GEORDIE WILLIAMSON School of Mathematics Mathematisches Institut Institute for Advanced Study der Univers"
section_id: sec-006-6-equivariant-formality
section_title: "Equivariant formality"
section_number: 6
pages: 15-19
source_pdf: 0707.2003v2.pdf
source_sha256: 0b8fe37aabeee412
doc_brief: "A geometric model for Hochschild homology of Soergel bimodules BEN WEBSTER GEORDIE WILLIAMSON School of Mathematics Mathematisches Institut Institute for Advanced Study der Universität Freiburg — An"
---
Now, we will carry out some actual computations of B -equivariant cohomol-
ogy , and thus of Hochschild homology .
Of course, the best setting in which to compute equivariant c ohomology of a
variety is when that variety (or more precisely , the sheaf on e intends to com-
pute the hypercohomology of) is equivariantly formal.
Deﬁnition/Theorem 6.1 We callF∈ Db
T (X) on a T -variety X equivariantly
formal if one of the following equivalent conditions holds:
(1) The S module H∗
T (X,F) is free.
(2) The differentials in the spectral sequence
H∗(X,F)⊗ S⇒ H∗
T (X,F)
are trivial, that is, if H∗(X,F)⊗ S∼= H∗
T (X,F) as S -modules.
(3) We have the equality dimC H ∗(X) = dim C H ∗(X T ).
15
The equivariant formality of the Bott-Samelsons of SL(n) has been proven by
Rasmussen in different language.
Proposition 6.2 If G = SL( n) or GL(n), the T -space Gi is equivariantly for-
mal for all i.
Proof By Theorem 1.2, HH∗(Ri) is free as an S -module if and only if H ∗
T (Gi)
is. By [Ra, Propositon 4.6], the module HH∗(Ri) is free in type A, so by Deﬁ-
nition/Theorem 6.1 above Gi is equivariantly formal.
This in turn implies that m∗CGi is equivariantly formal, where m : Gi→ G is
the multiplication map. Since all summands of equivariant f ormal sheaves are
themselves equivariantly formal, and each IC(Gw) appears as a summand of
such a sheaf (if, for example, i is a reduced word for w), this completes the
proof of Theorem 1.3 and the ﬁrst part of Theorem 1.6.
While the most obvious consequence of equivariant formalit y , calculating the
equivariant cohomology from ordinary or vice versa, is a rat her useful one, it
has less obvious ones as well.
Proposition 6.3 (Goresky , Kottwitz, MacPherson [GKM, Theorem 6.3]) IfF
is equivariantly formal, then the pullback map
i∗
T : H ∗
T (X,F)→ H ∗
T (X T ,F)
is injective.
As we mentioned earlier, we are interested in the Hochschild homology of
Soergel bimodules as a bigraded object (so that we get a tripl y-graded knot
homology theory), but the grading on equivariant hypercoho mology is only
one of these. From now on, we consider H ∗
T (Gw) as a bigraded S -module,
with the bigrading deﬁned by the isomorphism with Hochschild homology
given by Proposition 4.1.
Proof of Theorems 1.4 and 1.6 Since the pullback map H ∗
T (Gi)→ H ∗
T (GT
i ) is
induced by a map of Soergel bimodules, it is homogeneous in bo th gradings.
Similarly with the map induced by the inclusion of a summand IC(Gw)֒→
m∗CGi . Thus we need only establish the theorem for GT
i . As this is a union of
complex tori with the trivial action, we need only establish the theorem for T .
This case follows immediately from applying HH0 to the Koszul resolution of
HT ×T (T )∼= S as a bimodule over itself.
16
Let us turn to the case where Gw is smooth. Since H ∗
T (Gw)∼= S⊗ H ∗(Gw), it
will prove very interesting to understand H ∗(Gw). Surprisingly , no descrip-
tion of this cohomology seems to be in the literature, but in f act there is a very
beautiful one.
As is well known (and we reprove in the course of Lemma 6.6 belo w), there
exists a unique decreasing sequence of positive integers k1,··· kn such that the
Hilbert series of H ∗(Gw/B) is of the form
ℓ(w)∑
i=1
qi/2 dim H i(Gw/B) =
n∏
j=1
1− qkj
1− q
Theorem 6.4 If Gw is smooth, then as an algebra,
H ∗(Gw)∼=∧•(γ1, . . . γn) (1)
where deg(γi) = 2 ki− 1, and as an S -algebra,
H ∗
T (Gw)∼= HHi(Rw)∼= S⊗ H ∗(Gw).
In the standard double grading on HHi(Rw), we have deg(1⊗ γi) = (1 , 2ki).
This explicitly describes the Hilbert series of HHi(Rw), proving a conjecture of
Rasmussen.
Corollary 6.5 The Hilbert series of HHi(Rw) is given by
∑
i,j
aiqjHHi(Rw)2j =
n∏
ℓ=1
1 + aqkℓ
1− q
Since dim H ∗(Gw) = 2 rkG , Deﬁnition/Theorem 6.1(3) establishes the equivari-
ant formality of Gw independently of the earlier results of this paper (and for
all types).
As usual in Lie theory , we deﬁne the height h(α) =⟨ρ∨, α⟩ of a root α to be its
evaluation against the fundamental coweight.
Lemma 6.6 The cohomology ring H ∗(Gw/B) is a quotient of the polynomial
ring S by a regular sequence (f1, . . . , fn). Deﬁne ki = deg(fi).
The number of times the integer m appears in the list k1, . . . , kn is precisely the
number of roots in R+∩ w−1(R−) of height m− 1 minus the number of such
roots of height m, where R+ is the set of positive roots of G and R− =−R+ .
17
Proof For ease, assume Gw is not contained in a parabolic subgroup. By re-
sults of Akyıldız and Carrell [AC], the ring H ∗(Gw/B) is a quotient of C[BwB/B ]
by a regular sequence of length ℓ(w) by a regular sequence (g1, . . . , gk) where
k = ℓ(w).
In this grading, C[BwB/B ] is a polynomial algebra generated by elements of
degree 2h(α) for each root α∈ R+∩ w−1(R−), and the degrees of gi are given
by 2h(α) + 2 as α ranges over the same roots. Corresponding to the simple
roots are n− 1 generators x1, . . . xn of degree 2, which are the ﬁrst Chern
classes of line bundles on G/B corresponding the fundamental weights, and
for the other roots we have ℓ(w)− n + 1 other generators yn,··· yℓ(w) of higher
degree. Here, we assume these are in increasing order by degr ee.
It is a well known fact that the cohomology ring H ∗(G/B) is generated by the
Chern classes xi . Since the natural pullback map H ∗(G/B)→ H ∗(Gw/B) is
onto, the ring H ∗(Gw/B) is as well. That is, if p = deg yk > 2, then
yk−
∑
deg(gi)=p
βigi∈
∑
deg(gj )<p
Sgj.
Since yk /∈ ∑
deg(gj )<p Sgj , we can eliminate yk and any single relation gi
such that βi ⁄= 0 . Obviously , (g1, . . . , gn)\{ gi} is again a regular sequence
in C[x1, . . . , xn, yn, . . . , yk−1]. Applying this argument inductively , we obtain a
subsequence (gi1 , . . . , gin ) which is regular in S , which is the desired sequence.
Since the number of relations of degree j which have been eliminated is the
number of generators of degree j , the remaining number of relations is pre-
cisely the difference between these, which is also the numbe r of roots of height
j/2− 1 minus the number of height j/2 in R+∩ w−1(R−).
Proof of Theorem 6.4 Applying the Hirsch lemma (as stated in the paper [DGMS])
to the ﬁbration B→ Gw→ Gw/B , we see that the cohomology ring H ∗(Gw) is
the cohomology of the dg-algebra H ∗(Gw/B)⊗S KT where KT is the Koszul
complex of S (the natural free resolution of C as an S -module equipped with
the Yoneda product).
Since (f1, . . . , fn) is regular, H ∗(Gw/B) is quasi-isomorphic to the Koszul com-
plex Kf . Thus, the cochain complex of Gw is quasi-isomorphic to Kf⊗S C.
This is just an exterior algebra over C with generators γ1, . . . , γn with degree
given by deg(γi) = 2 ki− 1.
Since we used a Koszul complex, the generators γ land in Hochschild degree
1 under the restriction map to T , so the degree of γi is (2ki, 1).
18
If w∈ W ′ , where W ′ is a proper parabolic subgroup of W (with correspond-
ing Levi subgroup G′ ⊂ G), and W ′ is the minimal such parabolic. Then
Gw ∼= G′
w× T /T′× N∩ w′
0N w′
0 . Since N∩ w′
0N w′
0 is unipotent and thus
contractible, by K ¨ unneth, we have
dimC H ∗(Gw)∼= dimC H ∗(Gw′) dimC H ∗(T /T′) = 2 dim T ′
2dim T /T′
= 2 dim T .
Thus, Gw is equivariantly formal and the degrees ki for Gw are simply those
of Gw′ extended by adding 1’s.
