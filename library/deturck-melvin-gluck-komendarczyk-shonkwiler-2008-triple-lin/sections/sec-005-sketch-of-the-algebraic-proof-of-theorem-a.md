---
doc_id: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-005-sketch-of-the-algebraic-proof-of-theorem-a
section_title: "Sketch of the algebraic proof of Theorem A"
section_number: null
pages: 17-23
source_pdf: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-linking-numbers.pdf
source_sha256: db149864ce367da2
toc_source: outline
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
---
Sketch of the algebraic proof of Theorem A
This proof is organized around the following key diagram:
The left half represents the geometric-topological problem we are trying
to solve, and is devoid of algebraic structure. The right half represents the
algebraic structures that we impose on the left half via the two horizontal
maps in order to solve the problem.
In the upper left corner of (∗) we have the set of link-homotopy classes
of three-component links in the 3-sphere S3, and in the lower left corner
the set of homotopy classes of maps of the 3-torus to the 2-sphere. The
vertical map g between them assigns to the link-homotopy class of L the
homotopy class of its characteristic map gL. Theorem A describes g and
asserts that it is one-to-one.
In the upper right corner of (∗) we have the group H(3) of link-homotopy
classes of three-component string links. A k-component string link con-
sists of k oriented intervals embedded disjointly in a cube, with their tails
on the bottom face, their tips on the top face directly above their tails,
and their interiors in the interior of the cube. The terminology was coined
by Habegger and Lin [1990]. The product of two k-component string links
with endpoints in a common position is given by stacking the second one
on top of the first. When a string link moves by a link homotopy, each
268
DETURC, GLUCK, KOMENDARCZYK, MELVIN et al
strand is allowed to cross itself, while different strands must remain dis-
joint, just as for links. Then the above product induces a group structure
on the set H(k) of link homotopy classes of k-component string links.
Figure 9: Generators for H(3)
Following Habegger and Lin, we derive the following presentation for
H(3):
H(3) = ⟨P, Q, R, B | [P, Q] = [Q, R] = [R, P] = B,
[P, B] = [Q, B] = [R, B] = 1⟩
The string links P, Q, R and B are those shown in Figure 9.
Using this presentation, elements of H(3) can be written uniquely in
the form
P pQqRrBµ ,
for p, q, r, µ ∈Z.
Two elements P pQqRrBµ and P p∗Qq∗Rr∗Bµ∗are conjugate if and only if
p = p∗, q = q∗, r = r∗and µ ≡µ∗mod gcd(p, q, r).
A string link S can be closed up to a link bS by joining the tops of the
strands to their bottoms outside the cube, without introducing any more
crossings. For example, the closure of the three-component string link B
is the Borromean rings, as shown in Figure 10.
Thus the Borromean rings, a “primitive example” in the world of links,
is the closure of a string link which is itself a commutator of simpler string
links.
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS
269
Figure 10: The string link B closes up to the Borromean rings bB
The closing-up operation descends to link homotopy classes and pro-
vides the upper horizontal map in (∗). That the closure of the string link
P pQqRrBµ has pairwise linking numbers p, q and r is apparent for the
generators P, Q and R depicted in Figure 9, and then follows in general
because pairwise linking numbers of the closure are additive under compo-
sition of string links. That the Milnor invariant of the closure is congruent
to µ mod gcd(p, q, r) follows from the formula for this invariant given in
Mellor and Melvin [2003] which we referred to in the previous section.
It then follows from Milnor’s theorem that the closing-up map is onto.
Furthermore, its point inverse images are the conjugacy classes in H(3), a
special circumstance for links with three components which fails for four
or more components.
In the lower right corner of (*) we have the union of the fundamen-
tal groups of the components of the space of continuous maps of the
2-torus to the 2-sphere, with one group π1Mapsp(S1 × S1, S2) for each
choice of degree p of these maps. The work of Fox [1948] on torus ho-
motopy groups (the case p = 0) can be generalized to provide explicit
presentations for these groups:
π1Mapsp(S1 × S1, S2) = ⟨Up, Vp, Wp | [Up, Vp] = W 2
p , W 2p
p
= 1,
[Up, Wp] = [Vp, Wp] = 1⟩.
These presentation also follow as a special case of a more general result
of Larmore and Thomas [1980] on the fundamental groups of the con-
nected components of the space of sections of certain 3-plane bundles over
270
DETURC, GLUCK, KOMENDARCZYK, MELVIN et al
surfaces, which is proved using Postnikov invariants.
Using this presentation, elements of π1Mapsp(S1×S1, S2) can be written
uniquely in the form
Uq
p V r
p W ν
p ,
for q, r, ν ∈Z with 0 ≤ν < 2|p|.
Two elements Uq
p V r
p W ν
p and Uq∗
p V r∗
p W ν∗
p
are conjugate if and only if
q = q∗, r = r∗and ν ≡ν∗mod 2 gcd(p, q, r).
A direct argument using framed links shows how the generators Up,
Vp and Wp of π1Mapsp(S1 × S1, S2) can be represented by specific maps
S1 × S1 × S1 →S2, all agreeing with some fixed map of degree p on
∗× S1 × S1. In addition to this common feature, the representatives for
Up, Vp, Wp have degrees q = 1, 0, 0 on S1 × ∗× S1, degrees r = 0, 1, 0 on
S1 × S1 × ∗, and Pontryagin invariants ν = 0, 0, 1 relative to the chosen
basepoint for π1Mapsp(S1 × S1, S2).
The lower horizontal map in the key diagram takes a homotopy class of
based loops in the space Maps(S1 × S1, S2), ignores basepoints, identifies
S1 × S1 with ∗× S1 × S1, and then regards this class as a homotopy class
of maps of S1 × S1 × S1 →S2. Given a loop λ : S1 →Maps(S1 × S1, S2),
the map f : S1 × S1 × S1 →S2 is defined by f(s, t, u) = λ(s)(t, u). In
particular, the element Uq
p V r
p W ν
p of π1Mapsp(S1 × S1, S2) is taken to a
map with degrees p, q and r on the 2-dimensional coordinate subtori, and –
this is the key observation – with Pontryagin invariant ν mod 2 gcd(p, q, r)
relative to the image of the basepoint map. This lower horizontal map is
onto, and point inverse images are conjugacy classes in π1Mapsp(S1 ×
S1, S2).
The final step will be to define the vertical map G on the right side of
the key diagram to make the whole diagram commutative, and to be a
group homomorphism, insofar as possible. The hedge “insofar as possible”
refers to the fact that we have a group H(3) in the upper right corner of
the diagram, but only a union of groups π1Mapsp(S1×S1, S2) in the lower
right corner. We deal with this disparity by demoting H(3) to a union of
groups as follows.
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS
271
Let H0(3) denote the subgroup of H(3) consisting of string links with
the second and third strands unlinked, and with presentation:
H0(3) = ⟨Q, R, B | [Q, R] = B , [Q, B] = [R, B] = 1⟩.
Consider the left cosets Hp(3) = P pH0(3) of H0(3), and convert each
of them into a subgroup isomorphic to H0(3) by using left translation
to transfer the group structure from subgroup to coset.
Adopting the
notations Qp = P pQ, Rp = P pR and Bp = P pB for the generators of
Hp(3) in this borrowed group structure, we get the presentation
Hp(3) = ⟨Qp, Rp, Bp | [Qp, Rp] = Bp , [Qp, Bp] = [Rp, Bp] = 1⟩.
We are now ready to define the vertical map G on the right side of
(∗) so as to make the whole diagram commutative, and at the same time
to be a union of homomorphisms from the groups Hp(3) to the groups
π1Mapsp(S1 × S1, S2).
To do this, we start with specific string links to represent the elements
of Hp(3).
For purposes of illustration, we choose p = 2, and show in
Figure 11 the string links 12 = P 2, Q2 = P 2Q and R2 = P 2R, and under
them the three-component links we get by closing them up.
The 3-component links 12, Q2 and R2 shown in Figure 11 differ only
in their first (blue) component, and even these have the same “bottom
point”. Thus the corresponding characteristic maps from S1 × S1 × S1 →
S2 all restrict to the same map of degree 2 on ∗×S1×S1, and therefore all
three represent elements of the fundamental group π1Maps2(S1 × S1, S2)
based at this map. We denote these three images by G2(P 2), G2(P 2Q) and
G2(P 2R), with the intent of forcing commutativity in the key diagram. In
fact, we can do this for all the string links P 2QqRrBµ, and a simple
geometric argument shows that composition in the group H2(3) carries
over in this way to multiplication in the group π1Maps2(S1 × S1, S2).
Furthermore, a direct argument using framed links shows that the el-
ements G2(P 2Q) and G2(P 2R) may serve as the elements U2 and V2 in
the above presentation for π1Maps2(S1 ×S1, S2), so that G2 takes P 2Q to
272
DETURC, GLUCK, KOMENDARCZYK, MELVIN et al
Figure 11: Closing up the generators of H2(3)
U2 and P 2R to V2. It then follows that G2 maps P 2B = [P 2Q, P 2R] to
[U2, V2] = W 2
2 .
The value p = 2 used above was just for purposes of illustration, and
the corresponding results are true for all values of p. Thus we have defined
the vertical map G on the right side of our key diagram to be a union of
homomorphisms Gp : Hp(3) →π1Mapsp(S1 × S1, S2) making the whole
diagram commutative.
Now let L be any three-component link in S3 with pairwise linking num-
bers p, q and r and Milnor invariant µ. Then L is link homotopic to the clo-
sure of P pQqRrBµ. By commutativity of the key diagram, the homotopy
class of the characteristic map gL is the image under the lower horizontal
map of the element Gp(P pQqRrBµ) = Uq
p V r
p W 2µ
p
of π1Mapsp(S1×S1, S2),
and therefore has Pontryagin invariant 2µ, as desired.
This completes our sketch of the algebraic proof of Theorem A.
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS
273
