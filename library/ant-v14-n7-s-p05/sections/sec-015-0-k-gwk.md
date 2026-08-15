---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-015-0-k-gwk
section_title: "(k)≃ GW(k). □"
section_number: 0
pages: 45-50
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
doc_brief: "Motivic Gauss–Bonnet formulas — 18 sections: Duality and Euler characteristics; TX/B(1X×B X); TX/B(p∗"
---
Corollary 8.7. Let k be a perfect ﬁeld of characteristic different from two. Let H∈ GW(k) denote the
class of the hyperbolic form x 2− y2. Let X be a smooth and projective k-scheme.
(1) Suppose X has odd dimension 2n− 1. Let
m:=
∑
i+ j<2n−1
(−1)i+ j dimk Hi(X, j
X/k)−
∑
0≤i< j
i+ j=2n−1
dimk Hi(X, j
X/k).
Thenχ( X/k)= m· H∈ GW(k).
(2) Assume X has even dimension 2n. Let
m:=
∑
i+ j<2n
(−1)i+ j dimk Hi(X, j
X/k)+
∑
0≤i< j
i+ j=2n
dimk Hi(X, j
X/k)
and let Q be the symmetric bilinear form
Hn(X, n
X/k)× Hn(X, n
X/k) ∪−→H2n(X, 2n
X/k) Tr−→k.
Thenχ( X/k)= m· H+ Q∈ GW(k).
1846 Marc Levine and Arpon Raksit
Proof. For V a ﬁnite-dimensional k-vector space andn∈ Z, we have the symmetric bilinear form inDperf(k)
hn:(V[n]⊕ V∨[−n])⊗(V[n]⊕ V∨[−n])→ k
whose restriction to V[n]⊗ V∨[−n] is the canonical pairing of V[n] with V∨[−n]≃ V[n]∨, and(−1)n
times this pairing on V∨[−n]⊗ V[n]. The corresponding class of hn in GW(k) is(−1)n times the
class of h0, as (V[n]⊕ V∨[−n], hn) is the image of the class of V[n] in K0(k) under the hyperbolic
map H: K0(−)→ KO[0]
0 (−) (see, e.g., [Walter 2003, Theorem 2.6]), and [V[n]]= (−1)n[V[0]] in
K0(Dperf(k))≃ K0(k).
With this in mind, we may deduce the claim from the formula
χ( X/k)=
( dimB X⨁
i, j=0
Hi(X, j
X/k)[ j− i], Tr
)
of Theorem 8.6. Indeed, in the case dim X= 2n− 1, the symmetric bilinear form Tr is the sum of the
“hyperbolic” forms as above on
Hi(X, j
X/k)[ j− i]⊕ H2n−1−i(X, 2n−1− j
X/k )[i− j]
for i+ j< 2n− 1, or 0≤ i< j and i+ j= 2n− 1; and the argument in the even-dimensional case is the
same, except that one has the remaining factor coming from the symmetric pairing on Hn(X, n
X/k). □
The next result was obtained independently by Abelson [1976, Theorem 1] and Kharlamov [1974,
Theorem A] using an argument of Milnor’s relying on the Lefschetz ﬁxed point theorem.
Corollary 8.8. Let k be a ﬁeld equipped with an embeddingσ: k↪→ R. Let X be a smooth projective
k-scheme of even dimension 2n. Then
|χ top(X(R))|≤ dimk Hn(X, n
X/k).
Proof. We know that χ top(X(R)) is the signature of σ∗(χ( X/k))∈ GW(R); see [Levine 2017b,
Remarks 1.11]. The description of χ( X/k) given by Corollary 8.7 gives the desired inequality
|sigσ∗(χ( X/k))|≤ dimk Hn(X, X/k). □
Remark 8.9. Let k be a perfect ﬁeld of characteristic different from two. The formula for the Euler
characteristic given in Theorem 8.6 shows that the invariantχ( X/k) is “motivic” in the following sense.
Let X and Y be smooth projective k-schemes of respective even dimensions2n and 2m and letα: X99K Y
be a correspondence with k-coefﬁcients of degree n, that is, an element α∈ CHm+n(X× Y)k. The
correspondenceα induces the map of k-vector spacesα∗: Hm(Y, m
Y/k)→ Hn(X, n
X/k). Suppose thatα∗
is an isomorphism and is compatible with the trace pairings on Hm(Y, m
Y/k) and Hn(X, n
X/k) appearing
in Corollary 8.7. Then χ( X/k)=χ(Y/k) in the Witt ring W(k).
Motivic Gauss–Bonnet formulas 1847
For instance, supposingk has characteristic zero, if the motives ofX and Y (for homological equivalence
with respect to de Rham cohomology) have a Künneth decomposition
h(X)≃
2n⨁
i=0
hi(X)⟨i⟩, h(Y)≃
2m⨁
i=0
hi(Y)⟨i⟩
andα induces an isomorphismα∗: hm(Y)⟨m⟩→ hn(X)⟨n⟩, compatible with the respective intersection
products
hm(Y)⟨m⟩⊗ hm(Y)⟨m⟩→ h2m(Y)⟨2m⟩ πY∗−→h0(k)≃ Q,
hn(X)⟨n⟩⊗ hn(X)⟨n⟩→ h2n(X)⟨2n⟩ πX∗−→h0(k)≃ Q,
thenχ(Y/k)=χ( X/k) in W(k).
Presumably, merely having an isomorphism of motives hn(X)⟨n⟩≃ hm(Y)⟨m⟩ would not sufﬁce to
yieldχ(Y/k)=χ( X/k) in W(k), but we do not have an example.
8E. Descent for the motivic Euler characteristic. Let k be a perfect ﬁeld of characteristic different from
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
