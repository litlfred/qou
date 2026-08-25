---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-103-8d-hermitian-k-theory-and-witt-theory
section_title: "8D. Hermitian K-theory and Witt theory"
section_number: null
pages: 175-181
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
separated base-scheme of ﬁnite Krull dimension, but now assume that 2 invertible on B. Our goal in
this subsection is to explain how the description of the “rank” of χ( X/B) given by Theorem 8.3 can be
reﬁned to give a formula for χ( X/k) itself in terms of Hodge cohomology by using hermitian K-theory.
By work of Panin and Walter [2018], Schlichting [2010], and Schlichting and Tripathi [2015], hermitian
K-theory KO[∗]
∗ (−) is represented by a motivic commutative ring spectrum BO∈ SH(B) (we use the
notation of [Ananyevskiy 2016b]). Panin and Walter gaveBO an SL-orientation. BO-theory also represents
particular cases of Schlichting’s Grothendieck–Witt groups [2010], via functorial isomorphisms
BO2r,r(X; L)≃ KO[r]
0 (X, L):= GW(Dperf(X), L[r], can),
where L→ X is a line bundle andGW(Dperf(X), L[r], can) is the Grothendieck–Witt group ofL[r]-valued
symmetric bilinear forms on Dperf(X); we recall a version of the deﬁnition here.
1842 Marc Levine and Arpon Raksit
Deﬁnition 8.5. Let L→ X be a line bundle and let r∈ Z. An L[r]-valued symmetric bilinear form on
C∈ Dperf(X) is a map
φ: C⊗L C→ L[r]
in Dperf(X) which satisﬁes the following conditions.
(i) φ is nondegenerate: the induced map C→ RHom(C, L[n]) is an isomorphism in D perf(X).
(ii) φ is symmetric:φ◦τ=φ, whereτ: C⊗L C→ C⊗L C is the commutativity isomorphism.
(Note that we are assuming nondegeneracy in the deﬁnition but leaving this out of the terminology for the
sake of brevity.)
Similar to the case of algebraic K-theory discussed in Section 8B, for a rankr vector bundle p: V→ X,
the Thom class θ BO
V ∈ BO2r,r(V; p∗ det−1 V) is given by the Koszul complex Kos(p∗V∨, s∨
can), where
the symmetric bilinear form
φV: Kos(p∗V∨, s∨
can)⊗ Kos(p∗V∨, s∨
can)→ p∗ det−1 V[r]= 3r V∨[r]
is given by the usual exterior product
−∧−: 3i V∨⊗3r−i V∨→3r V∨.
Moreover, there are isomorphisms for i< 0
BO2r−i,r(X; L)≃ Wr−i(Dperf(X), L[r], can)
where Wr−i(Dperf(X), L[r], can) is Balmer’s triangulated Witt group. In the case B= Spec k for k a ﬁeld
of characteristic different from two, Ananyevskiy [2016b, Theorem 6.5] showed that this isomorphism
induces an isomorphism ofη-inverted hermitian K-theory with Witt-theory,
BO[η−1]∗,∗≃ W∗[η,η−1],
where one givesη bidegree(−1,−1) and an elementαηn withα∈ Wm has bidegree(m− n,−n); the
same proof works over out general base B (with assumptions as at the beginning of this subsection).
For f: Y→ X a proper map of relative dimension d f in SmB and L a line bundle on X, we follow
[Calmès and Hornbostel 2011] in deﬁning a pushforward map
ˆf∗: BO2r,r(Y,ω Y/B⊗ f∗L)→ BO2r−2d f,r−d f(X,ω X/B⊗ L)
by Grothendieck–Serre duality. In [op. cit.], this is worked out for the η-inverted theory BOη when the
base is a ﬁeld; however, the same construction works for BO over the general base-scheme B and goes
as follows. For r≥ 0, given an L[r]-valued symmetric bilinear formφ: C⊗L C→ωY/B⊗ f∗L[r], we
have the corresponding isomorphism
˜φ: C→ RHom(C,ω Y/B⊗ f∗L[r])≃ RHom(C,ω Y/ X⊗ f∗(ωX/B⊗ L[r])).
Motivic Gauss–Bonnet formulas 1843
Grothendieck–Serre duality gives the isomorphism
R f∗RHom(C,ω Y/ X⊗ f∗(ωX/B⊗ L[r])) ψ
∼−→RHom(R f∗C,ω X/B⊗ L[r− d f]).
Composing these, we obtain the isomorphism
ψ◦˜φ: R f∗C→ RHom(R f∗C,ω X/B⊗ L[r− d f]),
corresponding to the (nondegenerate) bilinear form
R f∗(φ): R f∗C⊗L R f∗C→ωX/B⊗ L[r− d f],
which one can show is symmetric. We explicitly deﬁne the above pushforward map by settingˆf∗(C,φ):=
(R f∗C, R f∗(φ)).
Applying this in the situation that f=πX: X→ B is a smooth and proper B-scheme of relative
dimension dX, we may obtain the formula
ˆπX∗(eBO(TX/B))=
( dimB X⨁
i, j=0
RiπX∗ j
X/B[ j− i], Tr
)
,
where
Tr:
( dimk X⨁
i, j=0
RiπX∗ j
X/B[ j− i]
)
⊗
( dimk X⨁
i, j=0
RiπX∗ j
X/B[ j− i]
)
→ OB
is the symmetric bilinear form in D perf(B) determined by the pairings
(RiπX∗ j
X/B)⊗(RdX−iπX∗dX− j
X/B ) ∪−→RdXπX∗dX
X/B
Tr−→OB.
Indeed, if s: X→ TX/B denotes the zero-section, we have
eBO(TX/B)= s∗(Kos(TX/B),φ)=
( dX⨁
j=0
 j
X/B[ j], s∗φ
)
with s∗φ determined by the product maps
 j
X/B[ j]⊗dX− j
X/B[dX− j]→ ωX/B[dX],
and therefore ˆπX∗(eBO(TX/B)) is⨁dimk X
i, j=0 RiπX∗ j
X/B[ j− i] with the symmetric bilinear form Tr as
described above.
Passing to theη-inverted theory BOη, our comparison Theorem 7.1 gives
q◦ˆπX∗= q◦πX∗
as maps BO2dX,dX
η (X,ω X/B)→ BOη(B). We check that the conditions of the comparison theorem
hold just as we did for algebraic K-theory. Firstly, as mentioned above, the SL-orientation for BO
deﬁned by Panin-Walter can be described as follows: the Thom class for an oriented vector bundle
1844 Marc Levine and Arpon Raksit
(p: V→ X, ρ: OX−→∼ det V ) is given by the Koszul complex Kos(p∗V∨, s∨
can) equipped with the
symmetric bilinear formφV deﬁned by the product in the exterior algebra followed by the isomorphism
p∗ρ∨: p∗ det−1 V→ OV . On the other hand, the Calmès-Hornbostel pushforward for the zero-section
s: X→ V of a rank r vector bundle p: V→ X with isomorphism ρ: OX−→∼ det V is as described
above, sending a symmetric bilinear form ψ: C⊗L C→ωX/B⊗ s∗L[n] to the symmetric bilinear form
Rs∗(ψ): Rs∗C⊗L Rs∗C→ωV/B⊗ L[n+ r].
Since s is ﬁnite, Rs∗C≃ C, which in Dperf(V) is canonically isomorphic to p∗C⊗OV Kos(p∗V∨, s∨
can).
We may thus view Rs∗(ψ) instead as a map
[p∗C⊗OV Kos(p∗V∨, s∨
can)]⊗ L[p∗C⊗OV Kos(p∗V∨, s∨
can)]→ ωV/B⊗ L[n+ r];
tracing through its deﬁnition, one ﬁnds that this map is given by the composition
[p∗C⊗OV Kos(p∗V∨, s∨
can)]⊗ L[p∗C⊗OV Kos(p∗V∨, s∨
can)]
−→∼ [p∗C⊗L p∗C]⊗[ Kos(p∗V∨, s∨
can)⊗ Kos(p∗V∨, s∨
can)]
p∗ψ⊗φV−−−−→ωX/B⊗ L[n]⊗ p∗ det−1 V[r]−→∼ ωV/B⊗ L[n+ r].
As this is exactly p∗(C,φ)⊗ thV,ρ, we see that the Calmès-Hornbostel pushforward for s is the same as
that deﬁned by the Panin-Walter SL-orientation on BOη, which veriﬁes the hypothesis in our Theorem 7.1.
Having veriﬁed this, we can prove our main result.
Theorem 8.6. Let B be a regular noetherian separated scheme of ﬁnite Krull dimension with 2 invertible
in0(B, OB). Let X be a smooth projective B-scheme. Then :
(1) We have
uBOη(χ( X/B))=
( dimk X⨁
i, j=0
RiπX∗ j
X/B[ j− i], Tr
)
in BO0,0
η (B)≃ W(Dperf(B))≃ W(B).
(2) Let f: GW(B)→ K0(B) denote the forgetful map discarding the symmetric bilinear form. Suppose
that the map
( f, q): GW(B)→ K0(B)× W(B)
is injective (this is the case if for example B is the spectrum of a local ring). Then
uBO(χ( X/B))=
( dimB X⨁
i, j=0
Hi(X, j
X/B)[ j− i], Tr
)
in GW(Dperf(B))≃ GW(B).
Motivic Gauss–Bonnet formulas 1845
(3) Suppose B is in Smk for k a perfect ﬁeld. Then the image ~χ( X/B) ofχ( X/B) inπ0,0(1B)(B)≃
H0(B, GW) is given by
~χ( X/B)=
( dimB X⨁
i, j=0
RiπX∗ j
X/B[ j− i], Tr
)
∈ H0(B, GW).
In particular, if B= Spec k, then
χ( X/k)=
( dimB X⨁
i, j=0
Hi(X, j
X/k)[ j− i], Tr
)
∈ GW(k).
Proof. The ﬁrst statement follows from our comparison Theorem 7.1, as detailed above, together with the
motivic Gauss–Bonnet Theorem 5.3. Statement (2) follows from (1) and our result for algebraic K-theory,
Theorem 8.3. Finally, (3) follows from (2), after we check that the unit map uBO induces the identity map
on GW(k) via
GW(k)
(Morel)
∼−−−→10,0
k (Spec k) uBO
∼−→BO0,0(Spec k)≃ KO[0]
0 (k)= GW(k),
where the ﬁrst isomorphism arises from Morel’s theorem [2004, Theorem 6.4.1, Remark 6.4.2; 2012,
Theorem 6.40] identifying 10,0
k (Spec k) with GW(k). The one-dimensional forms⟨λ⟩∈ GW(k),λ∈ k×,
generate GW(k), and via Morel’s isomorphism⟨λ⟩ maps to the automorphism of 1k induced by the
automorphismφλ: P1
k→ P1
k, φλ((x0: x1))=(x0:λ· x1). By [Ananyevskiy 2016b, Corollary 6.2],
the image ofφλ under the unit map uBO is also⟨λ⟩, after the canonical identiﬁcation BO0,0(Spec k)≃
KO[0]
0 (k)≃ GW(k). □
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
