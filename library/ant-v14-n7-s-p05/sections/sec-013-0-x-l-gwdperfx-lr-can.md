---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-013-0-x-l-gwdperfx-lr-can
section_title: "(X, L):= GW(Dperf(X), L[r], can),"
section_number: 0
pages: 41-45
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
doc_brief: "Motivic Gauss–Bonnet formulas — 18 sections: Duality and Euler characteristics; TX/B(1X×B X); TX/B(p∗"
---
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
