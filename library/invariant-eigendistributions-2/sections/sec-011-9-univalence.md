---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-011-9-univalence
section_title: "Univalence"
section_number: 9
pages: 21-22
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 18 sections: Front matter; Contents; Introduction."
---
If one uses explicitly the identiﬁcation h = ho × ho and ho
∗= ho one can get a formula for cΓ (λ) which
does not involve the arbitrary regular x ∈h and an analogous formula for pO. To see this we can place
ourselves momentarily in the following general situation envisaged by Lusztig and Spaltenstein [1979].
Until further notice, let ho denote any ﬁnite dimensional complex vector space, Wo any ﬁnite group
of linear transformations of ho. C[ho] denotes the complex polynomial functions on ho, C[Wo] the group
algebra of Wo. We shall assume that ho
∗≈ho as Wo-module so that we can identify the two whenever
convenient. (Nevertheless we generally distinguish ho
∗fom ho in notation. The assumption ho
∗≈ho
could be avoided at the expense of some complications irrelevant here.) Call an irreducible representation
σ of Wo univalent if it occurs with multiplicity one in the homogeneous polynomials of degree eo on ho
and does not occur in lower degree (some eo deﬁned by this condition). Fix such a univalent representation
σ of Wo and write χσ for its character. Denote by Cσ[Wo] the subspace of C[Wo] transforming by σ ⊗σ
under the biregular representation of Wo × Wo. For any a =  a(w)w in Cσ[Wo] deﬁne functions ϕa and
fa on ho
∗× ho by
ϕa(λ, x) =

y∈Wo
a(y)e⟨λ,y·x⟩
(1)
fa(λ, x) = 1
eo!

y∈Wo
a(y)⟨λ, y · x⟩eo
(2)
fa(λ, x) is evidently a polynomial on ho
∗× ho, homogeneous of degree eo in either variable separately.
Write Ceo,eo[ho
∗× ho] for the space of all such polynomials, and indicate by a subscript “σ” the part
thereof transforming by σ ⊗σ under Wo × Wo.
9.1 Lemma. The map
Cσ[Wo] →Cσ
eo,eo [ho
∗× ho], a →fa,
is a Wo × Wo −isomorphism. One has
ϕa(λ, x) = fa(λ, x) + o(|λ|eo, |x|eo)
REPRESENTATIONS OF WEYL GROUPS
22
with o(|λ|eo, |x|eo) indicating a power series in λ and x whose terms are of degree > eo both in λ and in x.
Proof. This is obvious from the univalence property of σ.
Write h = ho × ho and W = Wo × Wo with Wo embedded as the diagonal in W. An element a ∈Cσ[Wo]
may be considered as an element of C[W] via
a(w1, w2) = a(w1w2−1)
As element of C[W], a is right Wo-invariant and transforms by σ ⊗σ by W on the left. We denote the
subspace of these a in C[W] by Cσ[W/Wo]. For such an a deﬁne functions Φ and F on h∗× h by
Φa(λ, x) =

y∈W
a(y)e⟨λ,y·x⟩
(3)
Fa(λ, x) = 1
e!

y∈W
a(y)⟨λ, y · x⟩e
(4)
where we put e = 2eo. Φa(λ, x) and Fa(λ, x) transform according to σ ⊗σ in λ and are Wo-invariant in
x. F(λ, x) is also polynomial, homogeneous of degee e in λ and x separately.
