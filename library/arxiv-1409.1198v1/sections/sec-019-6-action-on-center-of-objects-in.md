---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-019-6-action-on-center-of-objects-in
section_title: "Action on center of objects in"
section_number: 6
pages: 43-45
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
This section is devoted to the proof of Theorem 1.3. The action of th e current algebra on the trace
of any 2-representation follows directly from the functotiality of t he trace. The rest of the section
establishes the action on the center.
6.0.1. Centers of categories. The center Z(C) of an additive category C is the endomorphism ring
of the identity functor Id C on C. Note that an endomorphism of Id C is a natural transformation
α : Id C ⇒ IdC. Such a natural transformation consists of a map αx : x → x for each object x of C
satisfying the requirement that for any map f : x →y in C, we get a commutative square
x
f /d47/d47
αx
/d15/d15
y
αy
/d15/d15x f
/d47/d47y
Exercise 24. Show that Z(C) is commutative ring. Hint: use the Eckmann–Hilton argument .
An additive category is an object of the linear 2-category AdCat of additive categories, additive
functors, and natural transformations. For an arbitrary, linea r 2-category C we deﬁne the center Z(x)
of an object x ∈ Ob(C) as the ring of endomorphisms C(1x, 1x), see [22]. Deﬁne the center of objects
of the 2-category C as the Z(C) = ⨁
x∈Ob(C)Z(x).
The relationship between Hochschild homology and cohomology descr ibed in section 2.2.3 can now
be recast in a more general framework.
Exercise 25. Let C be a linear 2-category C. Show that for each x ∈ Ob(C), the abelian group
Tr(C(x,x )) is a module over the ring Z(x).
Example 12. In the 2-category U(sl2), an element in the center Z(λ) for an object λ ∈ Ob(U(sl2)) is
given by any closed diagram in the graphical calculus. It was shown in S ection 8 of [37] that any such
closed diagram can be reduced to a product of non-nested dotted bubbles with the same orientation.
As explained in section 4.3, this provides an isomorphism between Z(λ) and the ring Sym of symmetric
functions.
Given a 2-endomorphism f : 1λ′x1λ ⇒ 1λ′x1λ in U ∗(sln), we can interpret the class [ f ] as a diagram
on the annulus. If we forget that the diagram is on an annulus, we ar e left with a diagram representing
44 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
an endomorphism of 1λ′ .
λλ′
/d15/d15/d79/d79
/d79/d79/d79/d79 /d15/d15 /d15/d15
/d15/d15/d79/d79 ii
• ∈ Tr(U ∗) ↝
λ
λ′
/d15/d15/d79/d79
/d79/d79/d79/d79 /d15/d15 /d15/d15
/d15/d15/d79/d79 ii
• ∈Z(λ′)
By choosing scalars tij = tji = 1 for all i ⁄= j, the 2-category U(sln)) = UQ(sln)) is cyclic and the
resulting diagram is independent of the choice of representative fo r the class [ f ] ∈ Tr(U(sln)). In this
way, [f ] gives rise to a map Z(λ) →Z(λ′) given by placing an element from Z(λ) inside the annulus
and regarding the result as an element in Z(λ′). Hence, we have the following proposition.
Proposition 6.1. The linear category Tr( U ∗(sln)) acts by endomorphisms on the commutative ring
Z (U ∗(sln)). Under this action the class [ f ] of endomorphisms f : 1λ′x1λ ⇒ 1λ′x1λ in U ∗(sln) is sent
to the linear operator sending a closed diagram D representing an element of Z(λ) to the element in
Z(λ′) obtained by removing the annulus from the diagram [ f.D].
Remark for experts . Being able to deﬁne an action of the trace on the center of object s in a 2-
category essentially amounts to having enough “coherent” duality in the 2-category so that the trace
takes values in the center of objects. This idea is captured by the n otion of a pivotal 2-category [52].
This can be seen as a many object version of a pivotal monoidal cate gory, see [24] where traces in this
context are studied. M¨ uger points out in [52, page 11] a strict piv otal 2-category can be deﬁned from
Mackaay’s work [47] on spherical 2-categories by ignoring the mon oidal structure. It is also equivalent
to a 2-category in which every 1-morphism has a speciﬁed cyclic biadj oint (see [20, 37]).
6.0.2. A current algebra action on centers. In what follows we represent a generic 2-morphismf ∈Z(λ),
f : 1λ ⇒ 1λ, by the diagram
∗
λ
where we use the ∗ to represent any linear combination of closed diagrams describing f .
Theorem 6.2. The vector space
(6.1) Z :=
⨁
λ∈ ˙U
Z(λ)
is a U(sln[t])-module with
1λ : Z − → Z(λ)(6.2)
∗
λ′
↦→ δλ,λ′

 ∗
λ 

x+
i,r : Z(λ) − → Z(λ +αi)(6.3)
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 45
∗
λ
↦→ (−1)(i+1)r /d15/d15/d79/d79
i•r
∗
λ λ +αi
x−
i,s : Z(λ) − → Z(λ −αi)(6.4)
∗
λ
↦→ (−1)(i+1)s /d79/d79/d15/d15
i•s
∗
λ λ −αi
ξi,r : Z(λ) − → Z(λ)(6.5)
∗
λ
↦→ (−1)(i+1)rpi,r(λ) ∗
λ
(6.6)
Proof. This theorem follows immediately from Proposition 23. In particular, t he fact that the current
algebra relations hold in the trace Tr( U ∗(sln)) imply that these relations hold under the action described
above. □
6.0.3. An action of the current algebra on centers of 2-representat ions.
Deﬁnition 6.3. A 2-representation of ˙UQ(sln) is a graded additive k -linear 2-functor Ψ : ˙UQ(sln) → K
for some graded, additive 2-category K.
When all of the Hom categories K(x,y ) between objects x and y of K are idempotent complete, in
other words Kar( K) ∼= K, then any graded additive k -linear 2-functor UQ(sln) → K extends uniquely
to a 2-representation of ˙UQ(sln).
Any 2-representation Ψ induces a map on traces
Tr( ˙UQ(sln)) → Tr(K)(6.7)
[f ] ↦→[Ψ(f )].
When looking at U ∗ as
U ∗(x,y ) :=
⨁
t∈ /CI
U(x,y ⟨t⟩),
we can easily extend this map to
Tr(U ∗(sln)) → Tr(K).
Hence by the same procedure described in Proposition 6.1, the trac e Tr(U ∗(sln)) acts on the center
Z(K) of any 2-representation. Since Proposition 23 shows that the cu rrent algebra is contained in the
trace, it follows that the current algebra acts on any 2-represen tation.
