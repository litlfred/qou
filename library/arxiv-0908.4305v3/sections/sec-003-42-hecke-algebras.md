---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidification"
section_id: sec-003-42-hecke-algebras
section_title: "Hecke Algebras"
section_number: 4.2
pages: 36-41
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
doc_brief: "Higher Dimensional Algebra VII: Groupoidification — Groupoidiﬁcation is a form of categoriﬁcation in which vect or spaces are replaced by groupoids and linear operators are replaced by spans of"
---
Here we sketch how to groupoidify a Hecke algebra when the parame ter q is a
power of a prime number and the ﬁnite reﬂection group comes from a Dynkin
diagram in this way. More details will appear in future work [2].
Let D be a Dynkin diagram. We write d ∈ D to mean that d is a dot in
this diagram. Associated to each unordered pair of dots d,d ′ ∈D is a number
mdd′ ∈ {2, 3, 4, 6}. In the usual Dynkin diagram conventions:
• mdd′ = 2 is drawn as no edge at all,
• mdd′ = 3 is drawn as a single edge,
• mdd′ = 4 is drawn as a double edge,
• mdd′ = 6 is drawn as a triple edge.
For any nonzero number q, our Dynkin diagram gives a Hecke algebra. Since
we are using real vector spaces in this paper, we work with the Heck e algebra
over R:
Deﬁnition 28. LetD be a Dynkin diagram and q a nonzero real number. The
Hecke algebra H(D,q ) corresponding to this data is the associative algebra
over R with one generator σd for each d ∈D, and relations:
σ2
d = (q − 1)σd +q
for all d ∈D, and
σdσd′σd · · · =σd′σdσd′ · · ·
for all d,d ′ ∈D, where each side has mdd′ factors.
Hecke algebras are q-deformations of ﬁnite reﬂection groups, also known as
Coxeter groups [20]. Any Dynkin diagram gives rise to a simple Lie group ,
and the Weyl group of this simple Lie algebra is a Coxeter group. To be gin
understanding Hecke algebras, it is useful to note that when q = 1, the Hecke
36
algebra is simply the group algebra of the Coxeter group associated to D:
that is, the group with one generator sd for each dot d ∈D, and relations
s2
d = 1, (sdsd′)mdd′ = 1.
So, the Hecke algebra can be thought of as a q-deformation of this Coxeter
group.
If q is a power of a prime number, the Dynkin diagram D determines a
simple algebraic group G over the ﬁeld with q elements, Fq. We choose a Borel
subgroup B ⊆ G, i.e., a maximal solvable subgroup. This in turn determines
a transitive G-set X =G/B. This set is a smooth algebraic variety called the
ﬂag variety ofG, but we only need the fact that it is a ﬁnite set equipped with
a transitive action of the ﬁnite group G. Starting from just this G-set X, we
can groupoidify the Hecke algebra H(D,q ).
Recalling the concept of ‘action groupoid’ from Section 1, we deﬁne t he
groupoidiﬁed Hecke algebra to be
(X ×X)//G.
This groupoid has one isomorphism class of objects for each G-orbit in X ×X:
(X ×X)//G ∼= (X ×X)/G.
The well-known ‘Bruhat decomposition’ [9] ofX/G shows there is one such orbit
for each element of the Coxeter group associated to D. Since the Hecke algebra
has a standard basis given by elements of the Coxeter group [20], it follows that
(X ×X)//G degroupoidiﬁes to give the underlying vector space of the Hecke
algebra. In other words, we obtain an isomorphism of vector space s
R(X×X)/G ∼=H(D,q ).
Even better, we can groupoidify the multiplication in the Hecke algebra. In
other words, we can ﬁnd a span that degroupoidiﬁes to give the linea r operator
H(D,q ) ⊗H(D,q ) → H(D,q )
a ⊗b ↦→ ab
This span is very simple:
(X×X×X)/ /G
(X×X)/ /G × (X×X)/ /G(X×X)/ /G
(p1,p 2)×(p2,p 3)
/d124/d124/d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121
(p1,p 3)
/d34/d34/d69/d69/d69/d69/d69/d69/d69/d69/d69/d69/d69/d69/d69/d69/d69
(8)
where pi is projection onto the ith factor.
37
For a proof that this span degroupoidiﬁes to give the desired linear o perator,
see [18]. The key is that for each dot d ∈D there is a special isomorphism class
in (X ×X)//G, and the function
ψd : (X ×X)/G → R
that equals 1 on this isomorphism class and 0 on the rest correspond s to the
generator σd ∈H(D,q ).
To illustrate these ideas, let us consider the simplest nontrivial exam ple, the
Dynkin diagram A2:
• •
The Hecke algebra associated to A2 has two generators, which we call P andL,
for reasons soon to be revealed:
P =σ1, L =σ2.
The relations are
P 2 = (q − 1)P +q, L 2 = (q − 1)P +q, PLP =LPL.
It follows that this Hecke algebra is a quotient of the group algebra o f the 3-
strand braid group, which has two generators P andL and one relation PLP =
LPL , called the Y ang–Baxter equation or third Reidemeister move . This
is why Jones could use traces on the An Hecke algebras to construct invariants
of knots [21]. This connection to knot theory makes it especially inter esting to
groupoidify Hecke algebras.
So, let us see what the groupoidiﬁed Hecke algebra looks like, and whe re the
Yang–Baxter equation comes from. The algebraic group correspo nding to the
A2 Dynkin diagram and the prime power q isG = SL(3, Fq), and we can choose
the Borel subgroupB to consist of upper triangular matrices in SL(3, Fq). Recall
that a complete ﬂag in the vector space F3
q is a pair of subspaces
0 ⊂V1 ⊂V2 ⊂ F3
q.
The subspace V1 must have dimension 1, while V2 must have dimension 2.
Since G acts transitively on the set of complete ﬂags, while B is the subgroup
stabilizing a chosen ﬂag, the ﬂag variety X = G/B in this example is just the
set of complete ﬂags in F3
q—hence its name.
We can think of V1 ⊂ F3
q as a point in the projective plane FqP2, and
V2 ⊂ F3
q as a line in this projective plane. From this viewpoint, a complete
ﬂag is a chosen point lying on a chosen line in FqP2. This viewpoint is natural
in the theory of ‘buildings’, where each Dynkin diagram corresponds t o a type
of geometry [10, 15]. Each dot in the Dynkin diagram then stands for a ‘type
of geometrical ﬁgure’, while each edge stands for an ‘incidence relat ion’. The
A2 Dynkin diagram corresponds to projective plane geometry. The do ts in this
diagram stand for the ﬁgures ‘point’ and ‘line’:
point • • line
38
The edge in this diagram stands for the incidence relation ‘the point p lies on
the line ℓ’.
We can think of P and L as special elements of the A2 Hecke algebra,
as already described. But when we groupoidify the Hecke algebra, P and L
correspond to objects of (X ×X)//G. Let us describe these objects and explain
how the Hecke algebra relations arise in this groupoidiﬁed setting.
As we have seen, an isomorphism class of objects in ( X ×X)//G is just a
G-orbit in X ×X. These orbits in turn correspond to spans of G-sets from X
to X that are irreducible: that is, not a coproduct of other spans of G-sets.
So, the objects P and L can be deﬁned by giving irreducible spans of G-sets:
P
/d126/d126/d126/d126 /d126 /d126/d126 /d126 /d126
/d32/d32/d64/d64/d64/d64/d64/d64/d64 L
/d127/d127/d126/d126 /d126/d126 /d126/d126 /d126
/d31/d31/d64/d64/d64/d64/d64/d64/d64
X X X X
In general, any span of G-sets
S
q
/d127/d127/d126 /d126/d126 /d126/d126 /d126/d126 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
X X
such that q ×p : S → X ×X is injective can be thought of as G-invariant
binary relation between elements of X. Irreducible G-invariant spans are always
injective in this sense. So, such spans can also be thought of as G-invariant
relations between ﬂags. In these terms, we deﬁne P to be the relation that says
two ﬂags have the same line, but diﬀerent points:
P = {((p,ℓ ), (p′,ℓ )) ∈X ×X |p ⁄=p′}
Similarly, we think of L as a relation saying two ﬂags have diﬀerent lines, but
the same point:
L = {((p,ℓ ), (p,ℓ ′)) ∈X ×X |ℓ ⁄=ℓ′}.
Given this, we can check that
P 2 ∼= (q − 1) ×P +q × 1, L 2 ∼= (q − 1) ×L +q × 1, PLP ∼=LPL.
Here both sides refer to spans of G-sets, and we denote a span by its apex.
Addition of spans is deﬁned using coproduct, while 1 denotes the iden tity span
from X to X. We use ‘ q’ to stand for a ﬁxed q-element set, and similarly for
‘q − 1’. We compose spans of G-sets using the ordinary pullback. It takes a
bit of thought to check that this way of composing spans of G-sets matches the
product described by Equation 8, but it is indeed the case [18].
To check the existence of the ﬁrst two isomorphisms above, we jus t need to
count. In FqP2, the are q + 1 points on any line. So, given a ﬂag we can change
the point in q diﬀerent ways. To change it again, we have a choice: we can
39
either send it back to the original point, or change it to one of the q − 1 other
points. So, P 2 ∼= (q − 1) ×P +q × 1. Since there are also q + 1 lines through
any point, similar reasoning shows that L2 ∼= (q − 1) ×L +q × 1.
The Yang–Baxter isomorphism
PLP ∼=LPL
is more interesting. We construct it as follows. First consider the lef t-hand side,
PLP . So, start with a complete ﬂag called ( p1,ℓ 1):
p1
ℓ1
Then, change the point to obtain a ﬂag ( p2,ℓ 1). Next, change the line to obtain
a ﬂag ( p2,ℓ 2). Finally, change the point once more, which gives us the ﬂag
(p3,ℓ 2):
p1
ℓ1
p1
ℓ1
p2
p1
ℓ1
p2
ℓ2
p1
ℓ1
p2
ℓ2
p3
The ﬁgure on the far right is a typical element of PLP .
On the other hand, consider LPL . So, start with the same ﬂag as before,
but now change the line, obtaining ( p1,ℓ ′
2). Next change the point, obtaining
the ﬂag (p′
2,ℓ ′
2). Finally, change the line once more, obtaining the ﬂag ( p′
2,ℓ ′
3):
p1
ℓ1
p1
ℓ1
ℓ′
2
p1
ℓ1
ℓ′
2
p′
2
p1
ℓ1
ℓ′
2
p′
2
ℓ′
3
The ﬁgure on the far right is a typical element of LPL .
Now, the axioms of projective plane geometry say that any two dist inct
points lie on a unique line, and any two distinct lines intersect in a unique
point. So, any ﬁgure of the sort shown on the left below determines a unique
ﬁgure of the sort shown on the right, and vice versa:
40
Comparing this with the pictures above, we see this bijection induces an isomor-
phism of spansPLP ∼=LPL . So, we have derived the Yang–Baxter isomorphism
from the axioms of projective plane geometry!
To understand groupoidiﬁed Hecke algebras, it is important to keep straight
the two roles played by spans. On the one hand, objects of the gro upoidi-
ﬁed Hecke algebra ( X ×X)//G can be described as certain spans from X to
X, namely the injective G-invariant ones. Multiplying these objects then cor-
responds to composing spans. On the other hand, Equation 8 gives a span
describing the multiplication in ( X ×X)//G. In fact, this span describes the
process of composing spans. If this seems hopelessly confusing, r emember that
any matrix describes a linear operator, but there is also a linear oper ator de-
scribing the process of matrix multiplication. We are only groupoidifyin g that
idea.
Other approaches to categoriﬁed Hecke algebras and their repre sentations
have been studied by a number of authors, building on Kazhdan–Lus ztig theory
[24]. One key step was Soergel’s introduction of what are nowadays c alled
Soergel bimodules [36, 42]. Also important were Khovanov’s categor iﬁcation of
the Jones polynomial [25] and the work by Bernstein, Frenkel, Khov anov and
Stroppel on categorifying Temperley–Lieb algebras, which are quo tients of the
type A Hecke algebras [7, 38]. A diagrammatic interpretation of the Soerg el
bimodule category was developed by Elias and Khovanov [12], and a geo metric
approach led Webster and Williamson [44] to deep applications in knot ho mology
theory. This geometric interpretation can be seen as going beyond the simple
form of groupoidiﬁcation we consider here, and considering groupo ids in the
category of schemes.
