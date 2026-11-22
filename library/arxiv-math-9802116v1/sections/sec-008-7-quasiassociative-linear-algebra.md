---
doc_id: arxiv-math-9802116v1
doc_title: "arXiv:math/9802116v1 [math.QA] 25 Feb 1998"
section_id: sec-008-7-quasiassociative-linear-algebra
section_title: "Quasiassociative linear algebra"
section_number: 7
pages: 30-33
source_pdf: 9802116v1.pdf
source_sha256: be7999751ffb6db3
toc_source: inferred
doc_brief: "Quasialgebra structure of the octonions — We show that the octonions are a twisting of the group algebra of Z2 × Z2 × Z2 in the quasitensor category of representations of a quasi-Hopf algebra asso"
---
Quasiassociative linear algebra
In this section we use our categorical approach to octonions to provide the natural ‘quasiasso-
ciative’ setting for the basic linear algebra associated to them. We deﬁne the natural notion
of ‘representation’. We also provide the deﬁnition of V ∗for any ﬁnite-dimensional G-graded
vector space, and the associated endomorphism quasialgebra V ⊗V ∗. These constructions are
the specialization to the G-graded quasi-algebra setting of standard constructions for braided
categories.
Thus, the notion of representations, indeed of all linear algebra and quantum group construc-
tions, make sense in any braided category, see [12]. One writes all constructions as compositions
of morphisms, inserting the associator Φ as necessary. For example, in the case of the category
of (kG, φ)-comodules, we clearly have:
Deﬁnition 7.1 A representation or ‘action’ of a G-graded quasialgebra A is a G-graded vector
space V and a degree-preserving map ⊲: A ⊗V →V such that
(ab)⊲v = φ(|a|, |b|, |v|)a⊲(b⊲v),
1⊲v = v
on elements of homogeneous degree. Here |a⊲v| = |a||v|.
This is the obvious polarization of the quasi-associativity of the product of A. Clearly, a
quasialgebra acts on itself by the product map (the regular representation).
Next, we recall that an object V in a braided category is called ‘rigid’ if there is an object
V ∗and morphisms
ev : V ∗⊗V →1,
coev : 1 →V ⊗V ∗
such that
(id ⊗ev)ΦV,V ∗,V (π ⊗id) = id,
(ev ⊗id)Φ−1
V ∗,V,V ∗(id ⊗π) = id
holds.
In the case of the comodule category of a dual quasiHopf algebra, these maps exist
whenever V is ﬁnite-dimensional, see [2] for the explicit formulae, cf[1]. For the dual quasiHopf
algebra kG, φ, i.e. for the category of G-graded vector spaces, these maps are given by
ev(f i ⊗ej) = δij,
coev(1) =
X
i
ei ⊗f iφ−1(|i|, |i|−1, |i|)
in terms of a basis of V with degree |ei| ≡|i| ∈G and its usual dual, i.e. ev can be taken as
the usual evaluation, V ∗as the usual dual, but coev is modiﬁed by the group 3-cocycle. Here
|f i| = |i|−1 so that ev, coev are degree preserving.
Proposition 7.2 If V is rigid then End(V ) = V ⊗V ∗becomes a G-graded quasialgebra. The
product map is
(v ⊗f)(w ⊗h) = v ⊗h < f, w > φ(|v|, |f|, |w||h|)
φ(|f|, |w|, |h|) .
Moreover, ﬁnite-dimensional representations V of a quasialgebra A are in 1-1 correspondence
with quasialgebra maps A →End(V ).
Proof
This is proven by commuting diagrams exactly as one would prove these statements in
linear algebra, only inserting the associator Φ wherever needed to change bracketing. Thus (in
any monoidal category) one ﬁnds
(id ⊗(ev ⊗id)) ◦(id ⊗Φ−1
V ∗,V,V ∗) ◦ΦV,V ∗,V ⊗V ∗: (V ⊗V ∗) ⊗(V ⊗V ∗) →V ⊗V ∗
as the natural product on End(V ) = V ⊗V ∗. Its action on V is the map
(id ⊗ev) ◦ΦV,V ∗,V : (V ⊗V ∗) ⊗V →V.
If A acts on V then
ρ = (⊲⊗id) ◦ΦA,V,V ∗◦(id ⊗coev) : A →V ⊗V ∗
is an algebra map. Conversely, given ρ,
(id ⊗ev) ◦ΦV,V ∗,V ◦(ρ ⊗id) : A ⊗V →V
is an action on V . We then specialize to the case of G-graded quasialgebras using the form of Φ
in terms of the 3-cocycle φ. ⊔⊓
In lieu of all the commutative diagrams here, we will prove this more explicitly in a concrete
form for our particular setting. First, we identify V ⊗V ∗with matrices in the usual way relative
to our basis, i.e.
α =
X
αijEij,
Eij = ei ⊗f j
as a deﬁnition of the components of α ∈V ⊗V ∗. Then the preceding proposition translates into
the following proposition. We write n = dim(V ) and |i| ∈G as the further data provided by V ,
which we also use.
Proposition 7.3 Let |i| ∈G for i = 1, · · · , n be a choice of grading function. Then the usual
n × n matrices Mn with the new product
(α · β)ij =
X
k
αikβkj
φ(|i|, |k|−1, |k||j|−1)
φ(|k|−1, |k|, |j|−1) ,
∀α, β ∈Mn
form a G-graded quasialgebra Mn,φ, where |Eij| = |i||j|−1 ∈G is the degree of the usual basis
element of Mn. An action of a G-graded quasialgebra in the n-dimensional vector space with
grading |i| is equivalent to an algebra map ρ : A →Mn,φ.
Proof
The product suggested by the preceding proposition is
Eij · Ekl = δj
kEil φ(|i|, |j|−1, |j||l|−1)
φ(|j|−1, |j|, |l|−1) ,
which yields the formula shown for α = P αijEij, etc. This product is quasiassociative since
(Eij · Ekl) · Emn = δj
kδl
mEin φ(|i|, |m|−1, |m||n|−1)φ(|i|, |k|−1, |k||l|−1)
φ(|m|−1, |m|, |n|−1)φ(|k|−1, |k|, |l|−1)
Eij · (Ekl · Emn)φ(|Eij|, |Ekl|, |Emn|)
= δlmδjk
φ(|i||j|−1, |k||l|−1, |m||n|−1)φ(|k|, |m|−1, |m||n|−1)φ(|i|, |k|−1, |k||n|−1)
φ(|m|−1, |m|, |n|−1)φ(|k|−1, |k|, |n|−1)
which are equal since
φ(|i||k|−1, |k||m|−1, |m||n|−1) = φ(|k|−1, |k|, |n|−1)φ(|i|, |k|−1, |k||m|−1)φ(|i|, |m|−1, |m||n|−1)
φ(|k|−1, |k|, |m|−1)φ(|k|, |m|−1, |m||n|−1)φ(|i|, |k|−1, |k||n|−1)
by repeated use of the cocycle property of φ.
Note also that the grading function |i| is equivalent to specifying a G-graded vector space
V = {ei} with grading |ei| = |i|.
An action of a G-graded quasialgebra G is equivalent to
structure constants vαij such that
cαβγvγij = vβikvαkjφ(|α|, |β|, |i|),
v0ij = δj
i
where {xα} (say) is a basis of A with x0 = 1 and xα⊲ei = vαijej. The corresponding map
A →Mn,φ is
ρ(xα)ij =
vαji
φ(|j|, |j|−1, |j|)φ(|i||j|−1, |j|, |j|−1).
That ρ is an algebra map is (from the deﬁnitions stated) is
cαβγvγji
1
φ(|j|, |j|−1, |j|)φ(|i||j|−1, |j|, |j|−1)
= vαaivβja
φ(|i|, |a|−1, |a||j|−1)
φ(|a|−1, |a|, |j|−1)φ(|a|, |a|−1, |a|)φ(|i||a|−1, |a|, |a|−1)φ(|j|, |j|−1, |j|)φ(|a||j|−1, |j|, |j|−1).
Since the structure maps are degree preserving, we know that |a| = |β||j|,
|i| = |α||a| for
nonzero terms on the right and side. That ρ is an algebra map is then equivalent to vαij an
action in view of the identity
φ(|α||β|, |j|, |j|−1)φ(|α||β||j|, |j|−1|β|−1, |β|)
= φ(|β|, |j|, |j|−1)φ(|β||j|, |β|−1|j|−1, |β||j|)φ(|α|, |β||j|, |β|−1|j|−1)φ(|β|−1|j|−1, |β||j|, |j|−1)φ(|α|, |β|, |j|)
which holds by repeated use of the 3-cocycle property. ⊔⊓
For example, the left regular representation of a quasialgebra on itself provides representation
ρ : A →Mn,φ where n = dim(A). For the octonions, for example, we have a representation in
8 × 8 quasimatrices.
