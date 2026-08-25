---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-104-8e-descent-for-the-motivic-euler-characteristic
section_title: "8E. Descent for the motivic Euler characteristic"
section_number: null
pages: 181-184
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
two. With the explicit formula for χ( X/k) given by Theorem 8.6, we may ﬁnd χ( X/k) for forms X
of some k-scheme X0 by the usual twisting construction; this works for all manners of descent but we
conﬁne ourselves to the case of Galois descent here.
Let X0, X be smooth projective k-schemes of even dimension 2n. Let K be a ﬁnite Galois extension
ﬁeld of k with Galois group G. Let X K:= X×k K , X0K:= X0×k K , and suppose we have an isomorphism
φ: X×k K→ X0×k K . This gives us the cocycle{ψσ∈AutK(X0×k K)}σ∈G, whereψσ:=φσ◦φ−1. Letting
b0: Hn(X0, n
X0/k)× Hn(X0, n
X0/k)→ k,
b: Hn(X, n
X/k)× Hn(X, n
X/k)→ k
denote the respective symmetric bilinear forms Tr(x∪ y), the isomorphismφ induces an isometry
φ∗:(Hn(X0K, n
X0K/K), b0K)→(Hn(X K, n
X K/K), bK),
and the cocycle{ψσ}σ∈G determines a cocycle{(ψ∗
σ)−1∈ O(b0)(K)}σ∈G. Twisting by the latter cocycle
allows one to recovers b from b0; explicitly, this works as follows.
Firstly, as usual, one recovers thek-vector spaceHn(X,n
X/k) from the K -vector spaceHn(X0K,n
X0K/K)
as the G-invariants for the map x↦→ ψ∗−1
σ (xσ). Secondly, letting A∈ GL(Hn(X0K, n
X0K/K)) be a
change of basis matrix comparing the k-forms Hn(X0, n
X0/k)⊂ Hn(X0K, n
X0K/K) and Hn(X, n
X/k)⊂
Hn(X0K, n
X0K/K), we recover b (up to k-isometry) as
b(x, y)= b0(Ax, Ay)=: b A
0(x, y).
Having performed this twist at the level of symmetric bilinear forms, we may now pass Grothendieck–
Witt classes to describe the Euler characteristic of X: namely, Corollary 8.7(2) gives
χ( X0/k)=[ b0+ m· H], χ( X/k)=[ b A
0+ m· H]
in GW(k).
1848 Marc Levine and Arpon Raksit
Remark 8.10. In the case of a smooth projective surface S with pg(S)= 0, over a characteristic zero
ﬁeld k, the twisting construction reduces to a computation involving CH1(S¯k)/∼num as a Gal(k)-module;
here¯k is the algebraic closure of k and∼num is numerical equivalence. Indeed, the assumption pg(S)= 0
implies that the cycle class map in Hodge cohomology
cycHdg: CH1(S¯k)→ H1(S¯k, 1
S/¯k)
induces an isomorphism
CH1(S¯k)/∼num⊗Z¯k−→∼ H1(S¯k, 1
S/¯k)≃ H1(S, 1
S/k)⊗k¯k
and the cycle class map cycHdg transforms the intersection product on CH1(S¯k)/∼num to the quadratic
form b0 on H1(S¯k, 1
S/¯k), induced by cup product and the trace map. Thus, our quadratic form b on
H1(S, 1
S/k) is equivalent to the one gotten by twisting the ¯k-linear extension of the intersection product
on CH1(S¯k)/∼num by the natural Galois action.
Analogous comments hold for a “geometrically singular” variety, by which we mean a smooth projective
k-scheme X of dimension 2n such that Hn(X¯k, n
X¯k/¯k) is spanned by cycle classes, where we replace
CH1/∼num with CHn/∼num. For example, one could take a K3 surface with Picard rank 20 over ¯k or a
cubic fourfold X with H2(X¯k, 2
X¯k/k)≃¯k21 spanned by algebraic cycles.
Examples 8.11. (1) As a simple example, take S to be a quadric surface in P3
k deﬁned by a degree two
homogeneous form q(X0,..., X3); we may assume that q is a diagonal form,
q(X0,..., X3)= a0X 2
0+
3∑
i=1
ai X 2
i
= a0(X0+
√
−a1/a0X1)(X0−√−a1X1)+ a2(X2−
√
−a3/a2X3)(X2+
√
−a3/a2X3).
This trivializes CH1(S) over K:= k(√−a0a1,√−a2a3), namely CH1(S)= Z𝓁1⊕ Z𝓁2 with 𝓁1
deﬁned by (X0−√−a1X1)=(X2−√−a3/a2X3)= 0 and with𝓁2 deﬁned by (X0−√−a1X1)=
(X2+√−a3/a2X3)= 0. Embedding Gal(K/k)⊂ Gal(k(√−a0a1)/k)× Gal(k(√−a2a3)/k)=
⟨σ1⟩×⟨σ2⟩, the Galois action is given byσ1(𝓁1,𝓁 2)=σ2(𝓁1,𝓁 2)=(𝓁2,𝓁 1). A Galois-invariant basis
is thus given by((𝓁1+𝓁2),√a0a1a2a3(𝓁1−𝓁2)), and the intersection form in this basis has matrix
(2 0
0−2a0a1a2a3
)
.
In other words,χ( S/k)=⟨ 2⟩+⟨− 2a0a1a2a3⟩.
(2) Suppose S is the blowup of P2
k along a 0-dimensional closed subscheme Z⊂ P2
k, with Z étale over
k. Let 𝓁 denote the class of a line in CH1(P2). Writing Z¯k={ p1,..., pr}, we have CH1(S¯k)≃
Z·𝓁⊕
(⨁r
i=1 Z· pr
)
, with the evident Galois action and with intersection form the diagonal matrix
(1,−1,..., −1). It is then easy to show that the twisted quadratic form χ( S/k) is⟨1⟩− TrZ/k(⟨1⟩).
Motivic Gauss–Bonnet formulas 1849
These last two examples have been computed by different methods before: (1) is a special case of
[Levine 2017b, Corollary 13.2] and (2) is a special case of [Levine 2017b, Proposition 1.10]. Here is a
more interesting example.
Example 8.12. Letπ: S→ C be a conic bundle over a smooth projective curve C, all deﬁned over k;
we assume for simplicity that k⊂ C. Let Z⊂ C be the degeneracy locus ofπ: that is, Z is the reduced
proper closed subscheme of C over whichπ is not smooth. For each geometric point z of Z, the ﬁber
π−1(z) is isomorphic to two distinct lines in P2:π−1(z)=𝓁z∪𝓁′
z. There is a “double section” D⊂ S
with D→ C a ﬁnite degree two morphism, and with D·𝓁z= 1= D·𝓁′
z for all z∈ Z(¯k).
Over¯k, the bundle S is isomorphic to the blow-up of a P1-bundle S¯k→ C¯k along a ﬁnite set Z′⊂ S¯k
with Z′−→∼ Z¯k viaπ.
Suppose Z¯k={ z1,... zr}. If we ﬁx a closed point c0∈ C\ Z of degree d over k, we have the following
basis for CH1(S¯k)Q/∼num:
𝓁z1−𝓁′
z1,...,𝓁 zr−𝓁′
zr, D,π−1(c0).
We have the ﬁnite degree two extension p:˜Z→ Z, where for each z∈ Z, p−1(z) corresponds to the pair
of lines𝓁z,𝓁′
z. Let L:= k({z1,..., zr})⊃ k and let G:= Aut(L/k). Writing k(˜Z)= k(Z)(
√
δ) for some
δ∈ O×
Z , we have a basis of CH 1(SL)Q/∼num given by
v1,...,v r, D,π−1(c0),
withvi:=
√
d(𝓁zi−𝓁′
zi). The intersection form on⟨v1,...,v r⟩ is the diagonal matrix
(−4δ(z1),..., −4δ(zr)),
the subspaces⟨v1,...,v r⟩ and⟨D,π−1(c0)⟩ are perpendicular and⟨D,π−1(c0)⟩ is hyperbolic. Moreover,
the automorphism group Aut(L/k) acts on⟨v1,...,v r⟩ just as it does on⟨z1,..., zr⟩. From this it follows
that the twisted intersection form b is given by
b= H− Trk(Z)/k(⟨δ⟩),
and hence
χ( S/k)= m· H− Trk(Z)/k(⟨δ⟩)
with
m= 2− dimk H0(S, 1
S/k)− dimk H1(S, OX)= dimQ H0(San, Q)− dimQ H1(San, Q)+ 1,
where San is the complex manifold associated to SC.
As a particular example, we may take S to be a cubic surface V⊂ P3
k with a line𝓁. Projection from 𝓁
realizes V as a conic bundleπ: V→ P1
k, with degeneracy locus Z⊂ P1
k a reduced closed subscheme of
degree 5 over k. The above implies that the symmetric bilinear form bV is given by
bV= H− TrZ/k(⟨δ⟩)
and computesχ( S/k)= 2H− TrZ/k(⟨δ⟩).
1850 Marc Levine and Arpon Raksit
Remark 8.13. Bayer-Fluckiger and Serre [2019] considered the ﬁnite k-scheme W representing the 27
lines on a cubic surface V and computed the trace form TrW/k(⟨1⟩) in [Bayer-Fluckiger and Serre 2019,
Theorem 5, Interpretation 7.3]. They identiﬁed their form q6,V with the trace form on H1(V, V/k) and
showed that
TrW/k(⟨1⟩)=λ2bV+(⟨−1⟩−⟨ 2⟩)bV+ 7−⟨− 2⟩.
