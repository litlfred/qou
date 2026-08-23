---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-023-02-given-a-reductive-complex-algebraic-group-g-s
section_title: "Given a reductive complex algebraic group G, Schieder [9] constructed a"
section_number: 0.2
pages: 47-48
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algeb raic Lie theory from the geometric and categorical"
---
bialgebraA playing the role of ⨁
nH 2n
c (Schn, C) for the aﬃne Grassmannian Gr G
in place of Gr. In order to explain his construction, we set up the bas ic notations
for G and GrG.
We ﬁx a Borel and a Cartan subgroup G⊃B⊃T , and denote by W the Weyl
group of ( G,T ). Let N denote the unipotent radical of the Borel B, and let N−
stand for the unipotent radical of the opposite Borel B−. Let Λ (resp. Λ ∨) be
the coweight (resp. weight) lattice, and let Λ +⊂ Λ (resp. Λ ∨+⊂ Λ ∨) be the cone
of dominant coweights (resp. weights). Let also Λ +⊂ Λ (resp. Λ ∨
+⊂ Λ ∨) be the
submonoid spanned by the simple coroots (resp. roots) αi, i∈I (resp.α∨
i, i∈I).
We denote by G∨⊃ T ∨ the Langlands dual group, so that Λ (resp. Λ ∨) is the
weight (resp. coweight) lattice of G∨.
LetO denote the formal power series ring C[[z]], and let K denote its fraction
ﬁeld C((z)). The aﬃne Grassmannian Gr G =GK/GO is an ind-projective scheme,
the union ⨆
λ∈Λ + Grλ
G of GO-orbits. The closure of Gr λ
G is a projective variety
Grλ
G = ⨆
µ≤λ Grµ
G. The ﬁxed point set Gr T
G is naturally identiﬁed with the coweight
lattice Λ; and µ∈ Λ lies in Gr λ
G iﬀ µ∈Wλ .
For a coweightν∈ Λ = Gr T
G, we denote by Sν⊂ GrG (resp.Tν⊂ GrG) the orbit
ofN (K) (resp. of N−(K)) through ν. The intersections Sν∩
Grλ
G (resp.Tν∩
Grλ
G)
are the attractors (resp. repellents) of C× acting via its homomorphism 2 ρ to the
Cartan torus T acting on
Grλ
G : Sν∩
Grλ
G ={x∈
Grλ
G : lim
c→0
2ρ(c)·x = ν} and
1terminology of [9, 6.2.7].
3128 Oberwolfach Report 52/2018
Tν∩Grλ
G ={x∈
Grλ
G : lim
c→∞
2ρ(c)·x =ν}. Going to the limit Gr G = lim
λ∈Λ +
Grλ
G, Sν
(resp.Tν) is the attractor (resp. repellent) of ν in GrG. The closure
Sν is the union⨆
µ≤νSµ, while Tν = ⨆
µ≥νTµ.
Deﬁnition 1. (a) For θ∈ Λ + we denote by Sch θ (resp. Schθ) the intersection
Sθ∩T0 (resp. Sθ∩T 0).2 It is equidimensional of dimension ⟨ρ∨,θ⟩.
(b) We set Aθ :=H ⟨2ρ∨,θ⟩
c (Schθ, C) = H ⟨2ρ∨,θ⟩
c (Schθ, C), andA := ⨁
θ∈Λ +Aθ.
Given a smooth curve X and θ∈ Λ +, the open zastava space
◦
Zθ (see e.g. [2])
is equipped with the projection πθ :
◦
Zθ→Xθ to the degree θ conﬁguration space
ofX. It enjoys the factorization property, and for any x∈X, we have a canonical
isomorphism π−1
θ (θ·x)
∼
−→ Schθ. Given θ1,θ 2∈ Λ + such that θ1 +θ2 = θ, the
coproduct ∆ θ1,θ2 :Aθ→A θ1⊗Aθ2 is deﬁned just like in 0.1 via the cospecialization
morphism for the subfamily π−1
θ (θ1·x +θ2·y).
To construct the product m : ⨁
θ1+θ2=θAθ1⊗Aθ2→A θ we need the Drinfeld-
Gaitsgory interpolation ~Schθ→ A1 [4] constructed with respect to the C×-action
on Schθ arising from the cocharacter 2 ρ of T . The key property of ~Schθ→ A1 is
that the ﬁbers over a⁄= 0 are all isomorphic to Schθ, while the zero ﬁber ( ~Schθ)0
is isomorphic to the disjoint union ⨆
λ
Sch+,λ
θ × Sch−,λ
θ . Here λ (a coweight in
Λ + such that λ≤θ) runs through the set of C×-ﬁxed points of Schθ, and Sch+,λ
θ
(resp. Sch−,λ
θ ) stands for the corresponding attractor (resp. repellent). It is easy to
see that H ⟨2ρ∨,θ⟩
c ((~Schθ)0, C) = ⨁
θ1+θ2=θH ⟨2ρ∨,θ1⟩
c (Schθ1, C)⊗H ⟨2ρ∨,θ2⟩
c (Schθ2, C),
and the desired product m is nothing but the cospecialization morphism for the
compactly supported cohomology of the ﬁbers of the Drinfeld-Gait sgory family.
Schieder conjectured that the bialgebra A is isomorphic to the universal en-
veloping algebra U (n∨) of Lie(N ∨) where N ∨⊂B∨⊂G∨ is the unipotent radical
of Borel subgroup of G∨. The goal of the present work is a proof of Schieder’s
conjecture.
