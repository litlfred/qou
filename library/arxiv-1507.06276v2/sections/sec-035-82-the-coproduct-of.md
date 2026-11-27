---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-035-82-the-coproduct-of
section_title: "The coproduct of"
section_number: 8.2
pages: 43-45
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
ample 3.4. Let f :P →P be any map. For every M,N ∈Ob(Oint) deﬁne a linear
map
κf
M,N :M ⊗N →M ⊗N, (m ⊗n) ↦→q(f (µ),ν)m ⊗n if m∈Mµ, n∈Nν.(8.4)
As in Example 3.4 the collection κf = (κf
M,N )M,N ∈Ob(Oint) deﬁnes an element in
U (2).
Remark 8.3. In the following we will apply this notion in the case f = −Θ =
wX ◦τ , see Section 5.1. To this end we need to assume that the minima l realization
(h, Π, Π ∨) is compatible with the involution τ ∈ Aut(I,X ) as in [Kol14, 2.6] . This
means that the map τ : Π ∨ → Π ∨ extends to a permutation τ : Π ∨
ext → Π ∨
ext such
that ατ (i)(dτ (s)) = αi(ds). In this case τ may be considered as a map τ :P →P .
We will make this assumption without further comment. In the ﬁnite case, which
is our only interest in Section 9, it is always satisﬁed.
Recall from Example 3.3 that the function ξ deﬁned by (8.1) may be considered
as an element in U and hence we can take its coproduct, see Section 3.2. The
coproduct ∆(ξ) ∈ U (2) can be explicitly determined.
Lemma 8.4. The element ξ ∈ U deﬁned by (8.1) satisﬁes the relation
(8.5) ∆(ξ) = (ξ ⊗ξ) ·κ−1 ·κ−Θ.
Proof. Let M,N ∈Ob(Oint) and m ∈Mµ,n ∈Nν for some µ,ν ∈P . Then m ⊗n
lies in the weight space ( M ⊗N )µ+ν . Hence one gets
∆(ξ)(m ⊗n) = ξ(µ +ν)m ⊗n
(8.3)
= ξ(µ)ξ(ν)q−(µ,ν)q−(Θ( µ),ν)m ⊗n
= ( ξ ⊗ξ) ·κ−1 ·κ−Θ (m ⊗n)
which proves formula (8.5). □
44 MARTINA BALAGOVI ´C AND STEF AN KOLB
For the rest of this paper the symbol ξ will always denote the function given by
(8.1) and the corresponding element of U .
8.3. The action of ξ on Uq(g). Conjugation by the invertible element ξ ∈ U
gives an automorphism
Ad(ξ) : U → U, u ↦→Ad(ξ)(u) = ξuξ −1.
For any M ∈Ob(Oint) one has
ξ(um) = Ad(ξ)(u)ξ(m) for all u ∈ U and m ∈M .(8.6)
Recall that we consider Uq(g) as a subalgebra of U .
Lemma 8.5. The automorphism Ad(ξ) : U → U restricts to an automorphism of
Uq(g). More explicitly one has
Ad(ξ)(Eν ) = ξ(ν)EνK −1
ν+Θ( ν),(8.7)
Ad(ξ)(Fν ) = ξ(ν)−1Kν+Θ( ν)Fν,(8.8)
Ad(ξ)(Ki) = Ki(8.9)
for all Eν ∈U +
ν and Fν ∈U −
−ν and all i ∈I.
Proof. By deﬁnition the elements ξ and Ki commute in U . This proves (8.9). To
verify the remaining two formulas let M ∈Ob(Oint) and m ∈Mµ for some µ ∈P .
Then one has
ξEνξ−1m = ξ(µ +ν)
ξ(µ) Eνm
(8.3)
= ξ(ν)q−(µ+Θ( µ),ν)Eνm =ξ(ν)EνK −1
ν+Θ( ν)m
which proves formula (8.7). Formula (8.8) is obtained analogously usin g the relation
ξ(ν)−1 =ξ(−ν)q(ν+Θ( ν),ν) which also follows from (8.3). □
For g of ﬁnite type the above lemma allows us to identify the restriction of
Ad(ξ) to the subalgebra MXU 0
Θ
′ of Uq(g). Recall the conventions for the diagram
automorphisms τ0 in the ﬁnite case from Remark 7.2.
Lemma 8.6. Assume that g is of ﬁnite type. Then one has
Ad(ξ)
⏐⏐
MXU 0
Θ
= (Tw0TwXττ 0)
⏐⏐
MXU 0
Θ
.
Proof. Consider µ ∈ Q+
X and elements Eµ ∈ U +
µ and Fµ ∈ U −
−µ. By Lemma 8.5
and relations (7.2) one has
Ad(ξ)(Eµ) = q−(µ,µ)EµK −2
µ =Tw0TwXττ 0(Eµ),
Ad(ξ)(Fµ) = q(µ,µ)K 2
µFµ =Tw0TwXττ 0(Fµ).
Moreover, if ν ∈QΘ then Lemma 8.5 implies that
Ad(ξ)(Kν) = Kν =Tw0τ0TwXτ (Kν )
which completes the proof of the lemma. □
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 45
8.4. Extending γ from Q to P . In this ﬁnal subsection, we illustrate how dif-
ferent choices of c and s inﬂuence the extension of the group homomorphism
γ : Q → K(q1/d)× to the weight lattice P . As an example consider the root
datum of type A3 with I = {1, 2, 3}, that is g = sl4(C), and the admissible pair
(X,τ ) given by X = {2} and τ (i) = 4 −i. In this case the constraints (5.17) and
(5.2) reduce to the relations
c3 =q2c1, s (3) = −s(1).
The group homomorphism γ :Q → K(q1/d)× is deﬁned by
γ(α1) = s(3)c1, γ (α2) = 1, γ (α3) = s(1)c3.
The weight lattice P is spanned by the fundamental weights
̟1 = 3α1 + 2α2 +α3
4 , ̟ 2 = α1 + 2α2 +α3
2 , ̟ 3 = α1 + 2α2 + 3α3
4
and we want to extend γ from Q to P .
Choice 1. Let c1 = c3 = q, s(1) = 1, s(3) = −1. Then γ(α1) = −q, γ(α3) = q,
and γ can be extended to P by
γ(̟1) = e3πi/4q, γ (̟2) = eπi/2q, γ (̟3) = eπi/4q.
Choice 2. Let c1 = 1 −q2, c3 = q2 − 1, s(1) = 1, s(3) = −1. Then γ(α1) =
γ(α3) = q2 − 1, and γ can be extended to P by
γ(̟1) = γ(̟2) = γ(̟3) = q2 − 1.
The advantage of Choice 1 is that the parameters ci specialize to 1 as q → 1. This
property is necessary to show that Bc,s specializes to U (k) for q → 1, see [Kol14,
Section 10]. The drawback of Choice 1 is that, for γ to extend to P , the ﬁeld K
must contain some 4-th root of −1. Choice 2, one the other hand, has the advantage
thatγ can be deﬁned on P with values in Q(q)×. The drawback of Choice 2 is that
ci → 0 as q → 1 and hence Bc,s does not specialize to U (k).
For any quantum symmetric pair of ﬁnite type it is possible to ﬁnd analo gs of
Choice 1 and Choice 2 above. We can choose ci =qai for some ai ∈ Z, see [BK15,
Remark 3.14]. If X = ∅ or τ = id then γ extends to a group homomorphism
P → K(q1/d) and no ﬁeld extension is necessary. Now assume that X ⁄= ∅ and
τ ⁄= id. If we keep the choice ci = qai then the extension of γ to P requires the
ﬁeld to contain certain roots of unity. Alternatively, as in Choice 2, o ne can choose
ci ∈ {qai, (1 −qbi )qai} for some ai ∈ Z, bi ∈ Z and s(i) = ±1 in such a way that γ
can be extended from Q to P with values in Q(q1/d)×.
