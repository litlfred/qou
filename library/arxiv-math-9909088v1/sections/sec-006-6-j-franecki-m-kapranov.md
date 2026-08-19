---
doc_id: arxiv-math-9909088v1
doc_title: "THE GAUSS MAP AND A NONCOMP ACT RIEMANN-ROCH FORMULA FOR CONSTRUCTIBLE SHEA VES ON SEMIABELIAN V ARIETIES"
section_id: sec-006-6-j-franecki-m-kapranov
section_title: "J. FRANECKI, M. KAPRANOV"
section_number: 6
pages: 6-8
source_pdf: 9909088v1.pdf
source_sha256: 52cfb568951f195f
doc_brief: "THE GAUSS MAP AND A NONCOMPACT RIEMANN-ROCH FORMULA FOR CONSTRUCTIBLE SHEAVES ON SEMIABELIAN VARIETIES — For an irreducible subvariety Z in an algebraic group G we deﬁne an integer gdeg( Z)≥ 0 as the"
---
For ν = 0, . . . , n let An
ν⊂ P n be the aﬃne chart given by tν⁄= 0. This is an aﬃne
space with coordinates z(ν )
i , i∈{ 0, . . . , n}\{ ν} given by z(ν )
i = ti
tν
. Denote by
(C∗)n jν
֒→An
ν
kν
֒→P n
the embeddings. For ν = 0 we have z(0)
i = zi.
We now apply Theorem 3.4 to U = (C∗)n, X = An
0 , fi = zi, and our constructible
complex F. The recipe of the theorem requires us to introduce the famil y of 1-forms
ωs =
n∑
i=1
si d log zi , s = (s1, . . . , sn)∈ (C∗)n.
These forms are precisely the invariant 1-forms on G = ( C∗)n. We can view s as
an element of g∗, where g = Cn is the Lie algebra of G. Theorem 3.4 then gives us:
(4.1) CC (Rj0∗F) = CC (Rj∗F)|An
0 = lim
s→0
(CC (F) + ωs),
the limit being taken in T ∗An
0 .
Next, we apply Theorem 3.4 to U = ( C∗)n and X = An
ν with arbitrary ν ∈
{0, . . . , n}. Then we should take fi = z(ν )
i , i∈{ 0, . . . , n}\{ ν} and consider the
1-forms
ω(ν )
s′ =
∑
i⁄=ν
s′
i d log z(ν )
i , s ′∈ (C∗){0,...,n }\{ν }.
Now, each z(ν )
i is a Laurent monomial in the z1, . . . , zn, so d log z(ν )
i is an (integer)
linear combination of d log z1, . . . , dlog zn. Therefore, ω(ν )
s′ = ωs where s = φν (s′)
is an image of s under a linear transformation φν : C{0,...,n }\{ν }→ Cn. It is clear
that φν is invertible; in particular, s→ 0 iﬀ s′→ 0. This means that the answers
given by Theorem 3.4 for the CC (Rjν ∗F), glue together into one global answer:
(4.2) CC (Rj∗F) = lim
s→0
s∈E
(CC (F) + ωs).
Here the limit is taken in T ∗P n and s runs over the set
E ={(s1, . . . , sn)∈ (C∗)n : si⁄= sj , i ⁄= j}.
(The condition s∈ E is equivalent to φ−1
ν (s)∈ (C∗){0,...,n }\{ν } for any ν.)
Now, Theorem 1.3 for G = (C∗)n would follow from (4.2) and the next lemma.
(4.3) Lemma. Let Λ⊂ T ∗(C∗)n be an irreducible conic Lagrangian variety. Then
lim
s→0
s∈E
(Λ + ωs), [P n])T ∗Pn = gdeg(Λ) .
Proof: Let Ω s⊂ T ∗(C∗)n be the graph of ωs. If s∈ E, then Ω s is closed in T ∗Pn
as well. By translation, intersecting Λ + ωs with [ P n] is equivalent to intersecting
Λ with Ω −s. By Proposition 2.2, there exists a Zariski open, nonempty s et F⊂ Cn
such that for s(0) ∈ F the intersection Λ ∩ Ω −s(0) consists of gdeg(Λ) smooth
transverse points. Since E is also Zariski open, F∩ E meets any polydisk
Pε ={(z1, . . . , zn)∈ (C∗)n : 0 <|zi| < ε}
in an open dense set. By the “continuity of intersection” it f ollows that for |ε|≪ 1
and s(0)∈ Pε∩ F∩ E(
lim
s→0
s∈E
Λ + ωs), [P n]
)
T ∗P n
=|Ω −s(0)∩ Λ| = gdeg(Λ)
and this completes the proof.
NONCOMPACT RIEMANN-ROCH 7
Proof of Theorem 1.3 in general
Let A be an abelian variety. We recall some elementary properties of line bundles
on A, see [10] [16]. If L is such a bundle, by La, a∈ A we denote its ﬁber at a.
By L0 we denote the total space of L with the zero section deleted, so L0 is a
principal C∗-bundle on A. As for any base variety, the correspondence L↦→L0
is an equivalence between the category of line bundles and is omorphisms and the
category of principal C∗-bundles.
Assume that L has degree 0. Then the theorem of the square [16] provides
identiﬁcations
L0∼
= C , L a⊗ Lb ~−→La+b
which make L0 into a group, namely a semiabelian variety ﬁtting into an ext ension
(5.1) 0 → C∗→ L0 p
−→ A→ 0.
Next, any bundle L of degree 0 has a ﬂat connection. All such connections form
an aﬃne space Conn( L) over the vector space H 0(A, Ω 1) = a∗. Here a is the Lie
algebra of A. Let L be the Lie algebra of the group L0, so that we have the exact
sequence
(5.2) 0 → a∗→ L∗ π−→ C→ 0.
Denote by ~L = p∗L the pullback of L to L0. For any ∇∈ Conn(L) let ~∇ be its
pullback to a connection in ~L. Denote also by f the tautological section of ~L over
L0 (given by the identity map).
(5.3) Proposition. The 1-forms ~∇ log f ,∇∈ Conn(L), are invariant (with re-
spect to the group structure on L0). Their images in L∗ under the evaluation at 0
form the subspace π−1(1), where π is as in (5.2).
Proof: Let us ﬁrst show the invariance. Note that ~∇ log f is just the Lie algebra-
valued 1-form on the total space of the principal C∗-bundle L0, describing the
connection∇ in L0 in the standard approach of diﬀerential geometry. So its in-
variance follows from the fact that the line bundle ( L,∇) (or, what is equivalent,
the C∗-bundle ( L0,∇)) satisﬁes the theorem on the square as a bundle with con-
nection. More precisely, if m, q1, q2 : A× A→ A are the group structure and the
two projections, then the isomorphism
µ : q∗
1L⊗ q∗
2L→ m∗L
given by the theorem on the square is an isomorphism of bundle s with connection.
In particular, the induced isomorphism µa : La⊗ L→ l∗
aL is an isomorphism of
bundles with connection on A. But the translation l(a,λ ), λ∈ La\{ 0} on L0 is
just given by µa(λ⊗− ). This shows the invariance. As for the second assertion
of Proposition 5.3, it is again obvious from the interpretat ion of ~λ log f as the Lie
algebra-valued 1-form describing the connection and the id entiﬁcation L0
0 = C∗.
(5.4) Corollary. The 1-forms s ~∇ log f , s∈ C∗,∇∈ Conn(L), form a nonempty
Zariski open set in the space of all invariant 1-forms on L0.
Consider now several line bundles of degree 0, say L1, . . . , Ln, on A, and let
(5.5) 0 → (C∗)n→ G = L0
1×A . . .×AL0
n
p
−→ A→ 0
