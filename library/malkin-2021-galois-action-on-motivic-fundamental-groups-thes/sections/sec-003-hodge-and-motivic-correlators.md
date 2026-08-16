---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a ﬁnite set of points(: GalMot ⟳cMot 1 (-−(,E 0)"
section_id: sec-003-hodge-and-motivic-correlators
section_title: "Hodge and motivic correlators"
section_number: null
pages: 10-12
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a finite set of points(: GalMot ⟳cMot 1 (-−(,E 0). (1) — On the"
---
1.1.1 Hodge correlator integrals
Let - be a complex curve (in this thesis,- = P1(C) or an elliptic curve). The Hodge correlator functions,
deﬁned in [G9], are functions
CorH(G0,...,G =),
whereeach G8 iseitherapointof - ora1-formrepresentingaclassin 
1(-; C). Thedepthofthisexpression
isthenumberofpointsamongthe G8 minusone,if - isanellipticcurve,orthenumberofpointsdistinctfrom
0 among theG8 minus one, if- = P1. Theweightis= plus the depth.
The Hodge correlators depend on the choice of atangential base point– a base pointB∈ - and a tangent
vectorE0 atB. If== 1 andG0,G 1∈ -, then CorH(G0,G 1) is a (normalized) Green’s function with pole atB.
In particular,
– If- = P1 andB=∞, then
CorH(G0,G 1)=
∞(G0,G 1)=(2c8)−1 log|G0−G1|+.
The constant depends on the choice of tangent vector at∞, but the correlator is independent of this
constant in weight> 2, so we will ignore it when convenient. (WhenE0 = −1
I2
m
mI = m
mF withF = I−1, we
have= 0.) Thecorrelatorforothertangentialbasepointscanbederivedusingthefactthatitisinvariant
under automorphisms ofP1 acting on the base point and the arguments.
– If- istheellipticcurve C/(Z+ Zg),where Im(g) > 0,withcoordinate Iinheritedfromthecomplexplane,
then
CorH(G0,G 1)=
B(G0,G 1)=
Ar(G0,G 1)− 
Ar(G0,B)− 
Ar(B,G 1)+ .
Here 
Ar is the Arakelov Green’s function, the unique (up to constant) solution to the elliptic partial
diﬀerential equation(2c8)−1mm
 Ar(G)= vol−X0. It has the Fourier expansion

Ar(I)= 2Im(g)
2c8
Õ
W∈( Z+Zg)\{0}
exp(2c8 Im(IW)/Im(g))
|W|2 . (1.2)
2
The Arakelov Green’s function has a logarithmic singularity at 0. Hence, the function CorH(G0,G 1) has
singularities of the formlog|I| at the divisorsG0=G1,G0=B,G1=B.
–Remark: The Green’s function onP1 is a specialization of the one on. To be exact, write
g for the
Green’sfunctionon = C/(Z+ Zg) withbasepoint0. Then,taking I tobethecoordinateon g inherited
from the complex plane, such that the sectionI∈ g approaches42c8I ∈ P1, with appropriate choice of
tangential base points,
lim
g→+8∞

g(I1,I 2)=
1
(
42c8I 1,4 2c8I 2
)
= log

1
42c8I 1− 1− 1
42c8I 2− 1

.
(This can be shown by a residue computation or an application of the Kronecker limit formula. We will
require this fact in §3.4.2.)
If=≥ 2,theHodgecorrelatorsaredeﬁnedassumsofintegralsdeterminedbyplanetrivalenttrees. Picture
theG0,...,G = writtencounterclockwisealongtheboundaryofadiscandconsideratrivalenttree ) embedded
in the disc with leaves at the=+ 1 boundary points. The tree has=− 1 interior vertices+◦ and 2=− 1 edges
0,..., 2=−2. The embedding into the plane gives a canonical orientationOr) ∈{±1} (an ordering of the
edges up to even permutation).
Assign to each interior vertexE∈ +◦ a copy of-, called-E, with coordinateGE. Then assign to each
edge8 either a function58 or a 1-forml8, as follows:
(1) If8 =(D,E) is an interior edge, let58 =
B(GD,GE), a function on-D×-E.
(2) If 8 =(D,G 9) is a boundary edge with the leaf decorated by a pointG9 ∈ -, let 58 = 
B(GD,G 9), a
function on-D.
(3) If8 =(D,G 9) is a boundary edge withG9 =l a 1-form, letl8 =l(GD), a 1-form on-D.
Without loss of generality,0,..., : are the edges labeled by functions (i.e., not boundary edges
decorated by 1-forms). Suppose also that each form is either purely holomorphic or purely antiholomorphic
(which we may do because the Hodge correlators are linear in the forms); let there be? and@ forms of these
types, respectively. Then, setting3C=m−m, we deﬁne
2)(G0,...,G =)=(−2):
( :
1
2(:+?−@)
)−1
Or)
„
-+◦
503C51∧···∧ 3C5:∧l:+1∧···∧ l2=−2. (1.3)
3
/u1D44E /u1D44F
/u1D450/u1D714
/u1D4671 /u1D4672
„
I1,I 2

(I1,0)3C
(I1,I 2)∧ 3C
(I2,1)∧ 3C
(I2,2)∧ l(I1)
Figure 1.1. One of the trees contributing to CorH(0,1,2,l ).
The Hodge correlator is the sum of such expressions over all plane trivalent trees,
CorH(G0,...,G =)=
Õ
)
2)(G0,...,G =). (1.4)
The Hodge correlator is independent of the choice of ordering of edges. As a function of the arguments that
are points on-, it is either purely real or purely imaginary.
Figure 1.1 shows the integral corresponding to one of the two trees contributing to CorH(0,1,2,l ).
The Hodge correlators satisfy a family of(ﬁrst) shuﬄe relations. For 8,9 > 0, letΣ8,9 be the set of
(8,9)-shuﬄes, permutationsf∈ (8+9 such thatf(1) <··· < f(8) and f(8+ 1) <··· < f(8+ 9). The
(8,9)-shuﬄe relation states:
Õ
f∈Σ8,9
CorH(G0,Gf−1(1),Gf−1(2),...,G f−1(8+9))= 0. (1.5)
