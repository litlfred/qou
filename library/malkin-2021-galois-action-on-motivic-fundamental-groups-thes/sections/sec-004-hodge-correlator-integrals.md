---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-004-hodge-correlator-integrals
section_title: "Hodge correlator integrals"
section_number: null
pages: 10-12
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
toc_source: outline
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
Hodge correlator integrals
Let 푋be a complex curve (in this thesis, 푋= P1(C) or an elliptic curve). The Hodge correlator functions,
deﬁned in [G9], are functions
CorH(푥0, . . . , 푥푛),
where each 푥푖is either a point of 푋or a 1-form representing a class in 퐻1(푋; C). The depth of this expression
is the number of points among the 푥푖minus one, if 푋is an elliptic curve, or the number of points distinct from
0 among the 푥푖minus one, if 푋= P1. The weight is 푛plus the depth.
The Hodge correlators depend on the choice of a tangential base point – a base point 푠∈푋and a tangent
vector 푣0 at 푠. If 푛= 1 and 푥0, 푥1 ∈푋, then CorH(푥0, 푥1) is a (normalized) Green’s function with pole at 푠.
In particular,
– If 푋= P1 and 푠= ∞, then
CorH(푥0, 푥1) = 퐺∞(푥0, 푥1) = (2휋푖)−1 log |푥0 −푥1| + 퐶.
The constant 퐶depends on the choice of tangent vector at ∞, but the correlator is independent of this
constant in weight > 2, so we will ignore it when convenient. (When 푣0 = −1
푧2
휕
휕푧=
휕
휕푤with 푤= 푧−1, we
have 퐶= 0.) The correlator for other tangential base points can be derived using the fact that it is invariant
under automorphisms of P1 acting on the base point and the arguments.
– If 푋is the elliptic curve C/(Z+Z휏), where Im(휏) > 0, with coordinate 푧inherited from the complex plane,
then
CorH(푥0, 푥1) = 퐺푠(푥0, 푥1) = 퐺Ar(푥0, 푥1) −퐺Ar(푥0, 푠) −퐺Ar(푠, 푥1) + 퐶.
Here 퐺Ar is the Arakelov Green’s function, the unique (up to constant) solution to the elliptic partial
diﬀerential equation (2휋푖)−1휕휕퐺Ar(푥) = vol퐸−훿0. It has the Fourier expansion
퐺Ar(푧) = 2Im(휏)
2휋푖
Õ
훾∈(Z+Z휏)\{0}
exp (2휋푖Im(푧훾)/Im(휏))
|훾|2
.
(1.2)
The Arakelov Green’s function has a logarithmic singularity at 0. Hence, the function CorH(푥0, 푥1) has
singularities of the form log |푧| at the divisors 푥0 = 푥1, 푥0 = 푠, 푥1 = 푠.
– Remark: The Green’s function on P1 is a specialization of the one on 퐸. To be exact, write 퐺퐸휏for the
Green’s function on 퐸= C/(Z + Z휏) with base point 0. Then, taking 푧to be the coordinate on 퐸휏inherited
from the complex plane, such that the section 푧∈퐸휏approaches 푒2휋푖푧∈P1, with appropriate choice of
tangential base points,
lim
휏→+푖∞퐺퐸휏(푧1, 푧2) = 퐺1

푒2휋푖푧1, 푒2휋푖푧2

= log

1
푒2휋푖푧1 −1 −
1
푒2휋푖푧2 −1

 .
(This can be shown by a residue computation or an application of the Kronecker limit formula. We will
require this fact in §3.4.2.)
If 푛≥2, the Hodge correlators are deﬁned as sums of integrals determined by plane trivalent trees. Picture
the 푥0, . . . , 푥푛written counterclockwise along the boundary of a disc and consider a trivalent tree 푇embedded
in the disc with leaves at the 푛+ 1 boundary points. The tree has 푛−1 interior vertices 푉◦and 2푛−1 edges
퐸0, . . . , 퐸2푛−2. The embedding into the plane gives a canonical orientation Or푇∈{±1} (an ordering of the
edges up to even permutation).
Assign to each interior vertex 푣∈푉◦a copy of 푋, called 푋푣, with coordinate 푥푣. Then assign to each
edge 퐸푖either a function 푓푖or a 1-form 휔푖, as follows:
(1) If 퐸푖= (푢, 푣) is an interior edge, let 푓푖= 퐺푠(푥푢, 푥푣), a function on 푋푢× 푋푣.
(2) If 퐸푖= (푢, 푥푗) is a boundary edge with the leaf decorated by a point 푥푗∈푋, let 푓푖= 퐺푠(푥푢, 푥푗), a
function on 푋푢.
(3) If 퐸푖= (푢, 푥푗) is a boundary edge with 푥푗= 휔a 1-form, let 휔푖= 휔(푥푢), a 1-form on 푋푢.
Without loss of generality, 퐸0, . . . , 퐸푘are the edges labeled by functions (i.e., not boundary edges
decorated by 1-forms). Suppose also that each form is either purely holomorphic or purely antiholomorphic
(which we may do because the Hodge correlators are linear in the forms); let there be 푝and 푞forms of these
types, respectively. Then, setting 푑C = 휕−휕, we deﬁne
푐푇(푥0, . . . , 푥푛) = (−2)푘

푘
1
2 (푘+ 푝−푞)
−1
Or푇
∫
푋푉◦푓0 푑C 푓1 ∧· · · ∧푑C 푓푘∧휔푘+1 ∧· · · ∧휔2푛−2.
(1.3)
푎
푏
푐
휔
푧1
푧2
∫
푧1,푧2
퐺(푧1, 푎) 푑C퐺(푧1, 푧2) ∧푑C퐺(푧2, 푏) ∧푑C퐺(푧2, 푐) ∧휔(푧1)
Figure 1.1. One of the trees contributing to CorH(푎, 푏, 푐, 휔).
The Hodge correlator is the sum of such expressions over all plane trivalent trees,
CorH(푥0, . . . , 푥푛) =
Õ
푇
푐푇(푥0, . . . , 푥푛).
(1.4)
The Hodge correlator is independent of the choice of ordering of edges. As a function of the arguments that
are points on 푋, it is either purely real or purely imaginary.
Figure 1.1 shows the integral corresponding to one of the two trees contributing to CorH(푎, 푏, 푐, 휔).
The Hodge correlators satisfy a family of (ﬁrst) shuﬄe relations. For 푖, 푗> 0, let Σ푖, 푗be the set of
(푖, 푗)-shuﬄes, permutations 휎∈푆푖+푗such that 휎(1) < · · · < 휎(푖) and 휎(푖+ 1) < · · · < 휎(푖+ 푗). The
(푖, 푗)-shuﬄe relation states:
Õ
휎∈Σ푖, 푗
CorH(푥0, 푥휎−1(1), 푥휎−1(2), . . . , 푥휎−1(푖+ 푗)) = 0.
(1.5)
