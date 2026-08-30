---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-020-91-lemma-the-map
section_title: "Lemma. The map"
section_number: 9.1
pages: 21-23
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 25 sections: Introduction; Construction of Weyl group represe"
---
Cσ[Wo]→ Cσ
eo,eo
[ho
∗ ×ho],a →fa,
is a Wo ×Wo −isomorphism. One has
ϕa(λ,x)= fa(λ,x)+ o(|λ|eo,|x|eo)
REPRESENTATIONS OF WEYL GROUPS 22
with o(|λ|eo,|x|eo) indicating a power series in λ and x whose terms are of degree >eo both in λ and in x.
Proof. This is obvious from the univalence propertyofσ.
Writeh = ho ×ho and W = Wo ×Wo with Wo embedded as the diagonal inW. An elementa∈ Cσ[Wo]
maybe considered as an element ofC[W]v i a
a(w1,w 2)= a(w1w2−1)
As element ofC[W], a is rightWo-invariant and transforms byσ⊗σ by W on the left. We denote the
subspace of these a inC[W]b y Cσ[W/Wo]. For such an a deﬁne functions Φ and F onh∗ ×h by
Φa(λ,x)=
∑
y∈W
a(y)e⟨λ,y·x⟩ (3)
Fa(λ,x)= 1
e!
∑
y∈W
a(y)⟨λ,y ·x⟩e (4)
where we pute =2 eo.Φ a(λ,x)a n dFa(λ,x) transform according toσ⊗σ in λ and areWo-invariant in
x. F(λ,x) is also polynomial, homogeneous of degeee in λ and x separately.
9.2 Lemma.
Φa(λ,x)= Fa(λ,x)+ o(|λ|e,|x|e).
Furthermore,
Fa(λ,x)= fa(λ1,λ 2)fσ(x1,x 2)
where λ =(λ1,λ 2),x =(x1,x 2) and ho
∗ is identiﬁed with ho; fa is deﬁned as in (2) :
fa(λ1,λ 2)= 1
eo!
∑
y∈Wo
a(y)⟨λ1,y ·λ2⟩eo
and fσ is deﬁned by
fσ(x1,x 2)= 1
eo!
∑
y∈Wo
χσ(y)⟨x1,y ·x2⟩eo (5)
Proof. A typical term in the expansion of Φa(λ,x) looks like
1
k1!k2!
∑
y∈W
a(y)⟨λ1,y 1 ·x1⟩k1⟨λ2,y 2 ·x2⟩k2
where y =(y1,y 2). Byunivalence, this = 0 if eitherk1 or k2 <eo. For the same reason
Fa(λ,x)= 1
eo!eo!
∑
y∈W
a(y)⟨λ1,y 1 ·x1⟩eo⟨λ2,y 2 ·x2⟩eo (6)
REPRESENTATIONS OF WEYL GROUPS 23
The assumption thata∈ C[W] transforms byσ⊗σ on the left and is invariant byWo on the right allows
one to write forw ∈W
a(y)= degσ
|W|
∑
w∈W
χσ(y−1w)a(w)
where χσ(y)= χσ(y1y2−1)i fy =(y1,y 2)i nW = Wo ×Wo. In terms of the pairing⟨a,b⟩= ∑ a(w)b(w)
on C[W] this maybe written as
a(y)= degσ
|W| ⟨y·χσ,a⟩.
Also, in terms of the pairing⟨λi,xj⟩/i!= ⟨λ,x⟩iδij on polynomials onho and ho
∗, one checks that
⟨λ1,y 1 ·x1⟩eo⟨λ2,y 2 ·x2⟩eo = 1
eo!eo!⟨(λ1 ⊗λ2)eo,y ·(x1 ⊗x2)eo⟩.
Thus (6) can be written as
Fa(λ,x)= 1
eo!eo!
degσ
|W|
∑
y∈W
⟨y·χσ,a⟩⟨(λ1 ⊗λ2)eo,y ·(x1 ⊗x2)eo⟩.
Inthis equation(λ1⊗λ2)eo and(x1⊗x2)eo maybe replacedbytheircomponents( λ1⊗λ2)eo
σ and(x1⊗x2)eo
σ
which transform byσ ⊗σ under W, bySchur’s relations for irreducible matrix coeﬃcients, which give
further that
Fa(λ,x)= 1
eo!eo!⟨(λ1 ⊗λ2)σ
eo
,a⟩⟨χσ,(x1 ⊗x2)σ
eo
⟩ (7)
where the pointed brackets denote aW-invariant, nondegenerate, bilinear form onCσ[W]× C σ
eo,eo[h].
Lemma 9.1 says that under the identiﬁcationh =ho ×ho such a form is given by
⟨(x1 ⊗x2)σ
eo,a⟩=
∑
y∈Wo
a(y)⟨x1,y ·x2⟩eo.
Thus (7) becomes
Fa(λ,x)= fa(λ1,λ 2)fσ(x1,x 2)
with fa and fσ as speciﬁed. This is just the assertion of the lemma.
Returning now to the situation of section 8, we have :
