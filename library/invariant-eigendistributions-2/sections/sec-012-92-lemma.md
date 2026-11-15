---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-012-92-lemma
section_title: "Lemma."
section_number: 9.2
pages: 21-24
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
---
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
9.2 Lemma.
Φa(λ, x) = Fa(λ, x) + o(|λ|e, |x|e).
Furthermore,
Fa(λ, x) = fa(λ1, λ2)fσ(x1, x2)
where λ = (λ1, λ2),
x = (x1, x2) and ho
∗is identiﬁed with ho; fa is deﬁned as in (2) :
fa(λ1, λ2) = 1
eo!

y∈Wo
a(y)⟨λ1, y · λ2⟩eo
and fσ is deﬁned by
fσ(x1, x2) = 1
eo!

y∈Wo
χσ(y)⟨x1, y · x2⟩eo
(5)
Proof. A typical term in the expansion of Φa(λ, x) looks like
1
k1!k2!

y∈W
a(y)⟨λ1, y1 · x1⟩k1⟨λ2, y2 · x2⟩k2
where y = (y1, y2). By univalence, this = 0 if either k1 or k2 < eo. For the same reason
Fa(λ, x) =
1
eo!eo!

y∈W
a(y)⟨λ1, y1 · x1⟩eo⟨λ2, y2 · x2⟩eo
(6)
REPRESENTATIONS OF WEYL GROUPS
23
The assumption that a ∈C[W] transforms by σ ⊗σ on the left and is invariant by Wo on the right allows
one to write for w ∈W
a(y) = degσ
|W|

w∈W
χσ(y−1w)a(w)
where χσ(y) = χσ(y1y2−1) if y = (y1, y2) in W = Wo × Wo. In terms of the pairing ⟨a, b⟩=  a(w)b(w)
on C[W] this may be written as
a(y) = degσ
|W| ⟨y · χσ, a⟩.
Also, in terms of the pairing ⟨λi, xj⟩/i! = ⟨λ, x⟩iδij on polynomials on ho and ho
∗, one checks that
⟨λ1, y1 · x1⟩eo⟨λ2, y2 · x2⟩eo =
1
eo!eo!⟨(λ1 ⊗λ2)eo, y · (x1 ⊗x2)eo⟩.
Thus (6) can be written as
Fa(λ, x) =
1
eo!eo!
degσ
|W|

y∈W
⟨y · χσ, a⟩⟨(λ1 ⊗λ2)eo, y · (x1 ⊗x2)eo⟩.
In this equation (λ1⊗λ2)eo and (x1⊗x2)eo may be replaced by their components (λ1⊗λ2)eo
σ and (x1⊗x2)eo
σ
which transform by σ ⊗σ under W, by Schur’s relations for irreducible matrix coeﬃcients, which give
further that
Fa(λ, x) =
1
eo!eo!⟨(λ1 ⊗λ2)σ
eo, a⟩⟨χσ, (x1 ⊗x2)σ
eo⟩
(7)
where the pointed brackets denote a W-invariant, nondegenerate, bilinear form on Cσ[W] × C σ
eo,eo[h].
Lemma 9.1 says that under the identiﬁcation h = ho × ho such a form is given by
⟨(x1 ⊗x2)σ
eo, a⟩=

y∈Wo
a(y)⟨x1, y · x2⟩eo.
Thus (7) becomes
Fa(λ, x) = fa(λ1, λ2)fσ(x1, x2)
with fa and fσ as speciﬁed. This is just the assertion of the lemma.
Returning now to the situation of section 8, we have :
9.3 Addendum to theorem 8.2. The polynomials cΓ and pO are given by
cΓ (λ) = kO

y∈Wo
my⟨λ1, y · λ2⟩eo
(8)
pO(x) =
1
e!kO

y∈Wo
χσ(y)⟨x1, y · x2⟩eo
(9)
REPRESENTATIONS OF WEYL GROUPS
24
for some constant kO depending only on O.
(Note that in these equations my = m(y,1) in accordance with the identiﬁcation W/Wo = Wo.)
Proof. This follows by comparing the relation (8.6):

y∈W
my⟨λ, y · x⟩e = cΓ (λ)pO(x)
with the relation
1
e!

y∈W
my⟨λ, y · x⟩e = fa(λ1, λ2)fσ(x1, x2)
from Lemma 9.2 when we take χσ = χO and a = the component of m which transforms by χO ⊗χO on
the left. In the formula
fa(λ1, λ2) =

y∈Wo
a(y)⟨λ1, y · λ2⟩eo
we may then again replace a(y) by my, because the component of m of type χO is the only one which
contributes in degree eo in this sum, as follows from
Γ ∈H2n(S( ¯O)) ≈H2n(S(O)) +

O′<O
H2n(S(O′)).
