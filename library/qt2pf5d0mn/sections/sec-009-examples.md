---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-009-examples
section_title: "Examples"
section_number: null
pages: 54-59
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
toc_source: outline
doc_brief: "UC Santa Barbara — 19 sections: Front matter; Abstract; Introduction"
---
3.3
Examples
In this section, we give several examples of the partition function deﬁned in Section
3.1. Some of the known invariants in literature emerge as special cases of our construction.
3.3.1
Crane-Yetter invariant
The Crane-Yetter invariant was introduced in [22], where the authors gave a state
sum construction of 4-manifold invariants with the modular tensor category Rep(Uq(sl2))
as input, where Rep(Uq(sl2)) is the category of representations of Uq(sl2) with q some
principal 4r-th root of unity. Later on the construction was generalized so that it takes
any semi-simple ribbon category as input [23] 2. This generalized state sum invariant is
still called the Crane-Yetter invariant denoted by CYC(M).
For a G-BSFC D = C×
G = L
g∈G
Cg, if G = {e} is the trivial group, then D has only
one sector C = Ce and it is a ribbon fusion category. In this case, the only color on a
1-simplex is the unit e, so we can just assume there is no color at all on 1-simplices.
The colors on each 2-, 3-simplex run through a complete set of representatives in C. For
each colored 4-simplex, the partition function is given by Figure 3.3 where all the relevant
group elements are trivial, and this is equal to that deﬁned in [23]. It is then trivial to see
that the resulting partition function ZC×
{e}(M) is the exactly the Crane-Yetter invariant
CYC(M).
3.3.2
Yetter’s invariant from homotopy 2-types
A (strict) categorical group is a rigid tensor category G such that (⊗, 1, (·)∗) satisﬁes
the axioms of groups strictly and that every morphism is invertible.
Note that here
the morphism spaces are not required to be a vector space. Namely, in a categorical
2In the paper, such a category was called semi-simple tortile category.
45
Section 3.3
Examples
group, all the structural isomorphisms α, l, r are identity maps and A∗⊗A = A ⊗A∗=
1, f ⊗(f −1)∗= I, (f −1)∗⊗f = I for any object A and morphism f.
There is a one-to-one correspondence between categorical groups and crossed modules
which are deﬁned below.
Let G, H be two ﬁnite groups. A crossed module is a quad (H, G, ρ, a), where ρ :
H −→G is a group morphism, and a : G × H −→H is a group action of G on H, such
that the following two conditions are satisﬁed.
1. ρ commutes with the G-action, i.e., for any g ∈G, h ∈H, ρ(a(g, h)) = ρ(h)
g
, where
the right hand side is the conjugation action.
2. The action a extends the conjugation action of H on itself, i.e., for any h, h′ ∈H,
a(ρ(h′), h) =
h
h′ .
We will usually write the action a(g, h) = h
g .
Given a categorical group G, let G = G0 and H = ⊔g∈G Hom(1, g). It is clear that
G is a group with the product ⊗, the unit e = 1, and the inverse (·) = (·)∗. Deﬁne
ρ : H −→G by ρ(h) = t(h), and deﬁne the G-action by a(g, h) = Ig ⊗h ⊗I¯g. It is an
exercise to check that H is also a group, and (H, G, ρ, a) is a crossed module, which we
denote by Mod(G).
For the converse direction, given a crossed module (H, G, ρ, a), deﬁne the categorical
group Cat(H, G, ρ, a) as follows.
1. Objects are elements of G. For g1, g2 ∈G, Hom(g1, g2) := ρ−1( ¯g1g2) ⊂H. The
composition of morphisms are the product in H.
2. For h ∈Hom(g1, g2), h′ ∈Hom(g′
1, g′
2), g1 ⊗g′
1 := g1g′
1, and h ⊗h′ =
h
g′
1 h′. The
unit 1 is the unit in G. The α, l, r ′s are identity maps.
3. For g ∈G, the dual g∗:= ¯g, and the bg, dg ′s are identities.
46
Section 3.3
Examples
Again, it can be checked that Cat(H, G, ρ, a) is a categorical group.
Proposition 3.3.1 If (H, G, ρ, a) is a crossed module and G is a categorical group, then
Mod(Cat(H, G, ρ, a)) = (H, G, ρ, a)) and Cat(Mod(G)) = G.
Proof:
Direct veriﬁcation.
From a crossed module (H, G, ρ, a) we can construct a G-BSFC denoted by D =
D(H, G, ρ, a) = L
g∈G
Cg. As a category, D(H, G, ρ, a) is the same as VectH, the H-graded
category. We identify the simple objects in D with elements of H. For each g ∈G, the
g-sector Cg is spanned by all simple objects in ρ−1(g). This deﬁnes a G-grading on D due
to the fact that ρ is a group morphism. The G-action on simple objects of D is deﬁned to
be the action a on H. It can be checked that this is a well-deﬁned action, and Condition
(1) above guarantees that the G-action g sends the g′-sector to the g′
g
-sector.
Let h ∈Cg, h′ ∈Cg′, namely, ρ(h) = g, ρ(h′) = g′, then h ⊗h′ = hh′ ∈Cgg′, and
h′
g
⊗h =
h′
ρ(h)
⊗h = h′
h
⊗h = hh′ ∈Cgg′, where the second equality is due to Condition
(2). We deﬁne the G-crossed braiding by the identity map, namely,
ch,h′ := Id : h ⊗h′ −→h′
g
⊗h
We now describe the partition function associated with D(H, G, ρ, a). Let ˆF = (g, f, t)
be an extended coloring. Then for each 2-simplex (012), f012 ∈C¯g02g01g12. For any 3-
simplex (0123), if the space V ±(0123) is to be non-zero, we need to have
f034
f012
¯g34
= f013f123 = t0123
(3.6)
Thus the color on a 3-simplex is uniquely determined by those on its boundary faces.
Given an extended coloring such that the condition from Equation 3.6 is satisﬁed for
every 3-simplex, it is direct to see that for each 4-simplex σ, ˆZ±(σ) = 1 by Figure 3.3.
47
Section 3.3
Examples
Deﬁnition 3.3.2 Given a crossed module (H, G, ρ, a) and an ordered triangulation T of
M, an admissible coloring is a map F = (g, f), g : T 1 −→G, f : T 2 −→H, such that,
1. for any 2-simplex (012), ρ(f012) = ¯g02g01g12;
2. for any 3-simplex (0123), f034
f012
¯g34
= f013f123.
An admissible coloring is a C(H, G, ρ, a)-color in the sense of [26].
The following
property shows actually the partition function associated with D(H, G, ρ, a) is exactly
the Yetter’s invariant YC(H,G,ρ,a) associated with Cat(H, G, ρ, a) in [26].
Proposition 3.3.3 Let D = D(H, G, ρ, a) be the G-BSFC obtained from a crossed mod-
ule, then
ZD(M; T ) = |H||T 0|−|T 1|
|G||T 0|
#(H, G, ρ, a) = YC(H,G,ρ,a)(M),
(3.7)
where #(H, G, ρ, a) is the number of admissible colorings.
Proof:
In D, it is clear that the quantum dimension of each simple object is 1,
and the total dimension square D2 = |H|. Then the ﬁrst equality follows from Equation
3.1.3. The second equality follows from [26].
If H = {e} is the trivial group, there is a unique group morphism ρ0 from H to G,
and a unique action (the trivial action) a0 of G on H. Then according to Deﬁnition
3.3.2, an admissible coloring is simply a map g : T 1 −→G, such that for each 2-simplex
(012), ¯g02g01g12 = e.
In this case our partition function is reduced to the untwisted
Dijkgraaf-Witten invariant DWG(M) [20].
Proposition 3.3.4 Let D0 = D({e}, G, ρ0, a0), then
ZD0(M; T ) =
1
|G||T 0|#({e}, G, ρ0, a0) = | Hom(π1(M), G)|
| Hom(π0(M), G)| = DWG(M),
(3.8)
48
Section 3.3
Examples
where π0(M) is the set of connected components of M and Hom(π0(M), G) is the set of
maps from π0(M) to G.
Proof:
The ﬁrst equality is by Proposition 3.3.3.
Note that both of the two sides of the second equality is multiplicative with respect
to disjoint union of connected components. Thus it suﬃces to prove the equality for a
connected manifold M, namely, |π0(M)| = 1.
Choose a maximal spanning tree K, which is a sub complex of T 1 with |T 0|−1 edges.
Then it is easy to see that there is a |G||T 0|−1 to one correspondence between the set of
admissible colorings and Hom(π1(M), G).
3.3.3
Trivial G-grading with trivial G-action
Given a ribbon fusion category C and a ﬁnite group G, we can construct a G-BSFC
D = L
g∈G
Cg, where Cg = C if g = e, and Cg = 0 otherwise, and G acts on D by identity.
We consider the partition function associated to D.
Since the nontrivial part of D is constrained in the trivial sector, the coloring g
on 1-simplices needs to satisfy the Dijkgraaf-Witten coloring, namely, ¯g02g01g12 = e for
each 2-simplex (012). The colorings on 2- and 3-simplices are independent of those on
1-simplices, and they are the same as the colorings of Crane-Yetter model. Moreover,
the partition function corresponding to each colored 4-simplex is the same as that of
Crane-Yetter since the group action here is trivial.
Proposition 3.3.5 If D has a trivial G-grading and a trivial G-action where the trivial
sector of D is C, then ZD(M; T ) = CYC(M)DWG(M).
49
Section 3.4
