---
doc_id: 0307092v2
doc_title: "Published: 14 February 2004"
section_id: sec-007-13-unordered-simplices
section_title: "Unordered simplices"
section_number: 13
pages: 49-58
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class Walter D Neumann — We deﬁne an extended Bloch group and show it is naturally isom orphic to H3(PSL(2, C)δ; Z)."
---
As we have shown in Proposition 11.2, our complexes can be qua si-simplicial
(closed simplices not required to embed). The triangulatio ns that arise in prac-
tice (eg, ideal triangulations of complete ﬁnite volume 3–m anifolds, see section
14) are often not simplicial. However, a quasi-simplicial t riangulation does not
always admit vertex-orderings of its 3–simplices that agre e on common faces.
Thus, to use such a triangulation one may either have to subdi vide, or do
without vertex-orderings.
In this section we describe how the theory changes if we disca rd the orderings of
vertices of 3–simplices in the deﬁnition of ˆB(C) in terms of ﬂattened simplices.
We show that the result is to quotient ˆB(C) by its cyclic subgroup of order 6.
Suppose we have a ﬂattened simplex with parameter ( z; p, q) with z in the
upper half plane. If we retain its geometry but reorder its ve rtices by an even
permutation (which preserves orientation) then the ﬂatten ing is replaced by one
of
(1/(1 − z); q, −1 − p − q) or (1 − 1/z; −1 − p − q, q),
so the element in ˆB(C) is changed by subtracting one of
[z; p, q] − [1/(1 − z); q, −1 − p − q] or [ z; p, q] − [1 − 1/z; −1 − p − q, p].
Similarly, if we reorder its vertices by an odd permutation t hen the element in
ˆB(C) is changed by subtracting one of
[z; p, q] + [1/z; −p, 1 + p + q], [z; p, q] + [1 − z; −q, −p],
or [ z; p, q] + [z/(z − 1); 1 + p + q, −q].
Geometry & Topology, Volume 8 (2004)
462 Walter D Neumann
Proposition 13.1 If z is in the upper half plane then, with χ as in Proposition
7.4 and Theorem 7.5
[z; p, q] − [1/(1 − z); q, −1 − p − q] = χ(eπi/3+qπi )
[z; p, q] − [1 − 1/z; −1 − p − q, p] = χ(e−πi/3+pπi)
[z; p, q] + [1/z; −p, 1 + p + q] = χ(epπi)
[z; p, q] + [1 − z; −q, −p] = χ(eπi/3)
[z; p, q] + [z/(z − 1); 1 + p + q, −q] = χ(e2πi/3+qπi )
Proof The last three of the above equations correspond to permutat ions which
exchange two vertices. Since two of these involutions, toge ther with the Klein
four-group (which leaves ﬂattenings unchanged) generate t he full symmetric
group, it suﬃces to prove the third and fourth equations; the others are then
easy consequences. We start with the third equation. Recall that
[x; p0, q0] − [y; p1, q1] + [ y
x ; p1 − p0, q2] −
− [ 1−x−1
1−y−1 ; p1 − p0 + q1 − q0, q2 − q1] + [ 1−x
1−y ; q1 − q0, q2 − q1 − p0] = 0 (14)
is an instance of the ﬁve-term relation whenever all ﬁve of x, y , y
x , 1−x
1−y , and
1−x−1
1−y−1 are in the upper half plane. Similarly one checks that it is an instance of
the ﬁve-term relation if the ﬁrst three are in the lower half p lane and the last
two in the upper half plane. In particular, if all ﬁve are in th e upper half plane,
then replacing x by x−1 and y by y−1 we get a relation
[x−1; p0, q0] − [y−1; p1, q1] + [ x
y ; p1 − p0, q2] −
− [ 1−x
1−y ; p1 − p0 + q1 − q0, q2 − q1] + [ 1−x−1
1−y−1 ; q1 − q0, q2 − q1 − p0] = 0 . (15)
Putting p0 = p1 = q0 = q1 = 0 and q2 = q in equation (14) and p0 = p1 = 0,
q0 = q1 = 1, q2 = q + 1 in (15) and then adding, we get:
([x; 0, 0] + [x−1; 0, 1]) − ([y; 0, 0] + [y−1; 0, 1]) + ([y
x ; 0, q] + [x
y ; 0, q + 1]) = 0 (16)
This equation holds if x, y and y
x are suitably positioned in the upper half
plane. It will continue to hold by analytic continuation if w e vary x and y so
long as none of x, y , or y
x strays out of the upper half plane. If we vary x
and y in the upper half plane so that y
x crosses interval (0 , 1) and x
y therefore
crosses (1 , ∞) we get the equation
([x; 0, 0] + [x−1; 0, 1]) − ([y; 0, 0] + [y−1; 0, 1]) + ([ y
x ; 0, q] + [ x
y ; 0, q − 1]) = 0 ,
and exchanging x and y in this equation gives
([y; 0, 0] + [y−1; 0, 1]) − ([x; 0, 0] + [x−1; 0, 1]) + ([y
x ; 0, q − 1] + [x
y ; 0, q]) = 0 , (17)
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 463
Replacing q by q + 1 in equation (17) and then adding to equation (16) gives,
with z := y/x ,
2
(
[z; 0, q] + [z−1; 0, q + 1]
)
= 0 .
Here z is now arbitrary in the upper half plane. Thus [ z; 0, q] + [z−1; 0, q + 1]
is in the cyclic subgroup of order 2 in ˆB(C). On the other hand, we know by
the proof of Proposition 7.4 that R is an isomorphism on the torsion subgroup
of ˆB(C) and one checks easily that R([z; 0, q] + [ z−1; 0, q + 1]) = 0. Thus
[z; 0, q] + [z−1; 0, q + 1] = 0. As we analytically continue this relation by letting
z go repeatedly around the origin crossing the intervals ( −∞, 0) and (0 , 1) (so
z−1 crosses ( −∞, 0) and (1 , ∞)) we get the relations
[z; p, q] + [z−1; −p, p + q + 1] = 0
for all even p.
Now, using the notation of the proof of Proposition 7.4 and Le mma 7.1 we ﬁnd
[z; −1, q] + [z−1; 1, q] = ([ z; 0, q] + [z−1; 0, q + 1]) + ([z; −1, q] − [z; 0, q])+
+ ([z−1; 1, q] − [z−1; 0, q]) + ([z−1; 0, q] − [z−1; 0, q + 1])
= 0 + {1 − z, 0} − {1 − z−1, 0} − {z, 0}
= χ(1−z) − χ(1−z−1) − χ(z) = χ
( 1−z
(1−z−1)z
)
= χ(−1) .
Analytically continuing this as z circles the origin as before gives us the equa-
tions
[z; p, q] + [z−1; −p, p + q + 1] = χ(−1)
for all odd p. Thus the third equation of the proposition is proved.
For the fourth equation of the proposition, we already know b y Lemma 7.3 that
[z; p, q] + [1 − z; −q, −p] = 2[1 /2; 0, 0], so we need to show that 2[1 /2; 0, 0] =
χ(eπi/3). Denote ω = eπi/3 . Then 1 − ω = ω−1 so [ ω; 0, 0] + [ ω−1; 0, 0] =
2[1/2; 0, 0]. We have just shown that [ ω; 0, 0]+[ ω−1; 0, 1] = 0. And by deﬁnition
of χ, we have [ ω−1; 0, 0] − [ω−1; 0, 1] = −χ(ω−1) = χ(ω). Adding the last two
equations gives [ ω; 0, 0] + [ ω−1; 0, 0] = χ(ω), whence 2[1 /2; 0, 0] = χ(ω), as
desired (in fact, [1 /2; 0, 0] = χ(eπi/6), as can be seen now by applying R).
Corollary 13.2 If we deﬁne groups analogous to ˆP(C) and ˆB(C) using ﬂat-
tened simplices modulo the lifted ﬁve term relation, but ign oring orderings
of vertices, we obtain the quotients ˆP(C)/C6 and ˆB(C)/C6 , where C6 is the
unique cyclic subgroup of order 6.
Geometry & Topology, Volume 8 (2004)
464 Walter D Neumann
14 Invariants of 3–manifolds
Suppose we have a compact oriented hyperbolic 3–manifold M , or, more gen-
erally, a compact oriented manifold 3–manifold with a ﬂat G–bundle (equiv-
alently, a homomorphism π1(M ) → G; as usual G denotes PSL(2 , C)). Then
Theorems 4.6 and 2.6 give a computation of the corresponding homology class
in H3(G; Z) and its Cheeger–Chern–Simons class from a triangulation o f M .
In this section we extend this to the case that M is an oriented hyperbolic
manifold which is complete of ﬁnite volume but not necessari ly compact. We
will also extend to the sort of ideal triangulations that the programs Snap
[10, 4] and Snappea [22] use for compact hyperbolic manifold s. The underlying
complex of such a “Dehn ﬁlling triangulation” is homeomorph ic not to M itself,
but to the result of collapsing to a point a simple closed curv e of M , so Theorem
4.6 does not apply directly.
Suppose M is a non-compact oriented complete hyperbolic manifold of ﬁ nite
volume. It is known by Epstein and Penner [9] that M has a triangulation by
ideal hyperbolic polytopes, and by subdividing these polyt opes we may obtain
a triangulation by ideal simplices. As has often been pointe d out (eg, [15]),
after subdividing the polytopes into ideal simplices, the s ubdivisions may not
match across faces of the polytopes. One can mediate between non-matching
subdivisions by including ﬂat ideal simplices in the triang ulation. It is still
unknown if this is actually necessary in any example. It has b een shown by
Petronio and Weeks [18] that ﬂat ideal simplices are usually not a serious issue.
This is so for our arguments, in fact for us even “folded back t etrahedra” are
allowed.
In [13] it is shown that any ideal triangulation of a hyperbol ic 3–manifold has
a ﬂattening in the sense of Theorem 4.6. If we can appropriate ly order vertices
then the arguments of this paper imply that we get an element o f ˆB(C). In
general we cannot do this, so, by the previous section, we onl y get an element
of ˆB(C)/C6 . We can reﬁne our triangulation to make sure that we can order
the 0–simplices. The triangulations we must consider for th is are hybrids of
usual triangulations and ideal ones.
Suppose M has h cusps, and consider the end compactiﬁcation of M , obtained
by adding points pi , i = 1, . . . , h, to compactify each cusp. If K is a complex
that triangulates this compactiﬁcation of M then p1, . . . , ph will be 0–simplices
of K . We consider K0 := K − {p1, . . . , ph} to be a “triangulation” of the non-
compact manifold M . Some of the simplices of K have one or more vertices
among {p1, . . . , ph}; we call these “ideal vertices.”
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 465
We wish to assign ideal simplex shapes to all the simplices of K in an appro-
priate fashion. This is maybe most easily visualized as foll ows. We position our
triangulation of M = H3/Γ so that it triangulates M by geodesic hyperbolic
simplices, with vertices pi ideal. We then lift to a triangulation of ˜M = H3 .
Finally, we move each non-ideal vertex to ∂H
3
in a Γ–equivariant fashion, mak-
ing sure that the resulting ideal simplices are non-degener ate (all four vertices
distinct).
Remark 14.1 We can also describe this is terms of a G–valued 1–cocycle
“relative to the cusps.” We choose a lift ˜ pi ∈ H3 for each pi and denote by Pi
the parabolic subgroup of G that ﬁxes ˜pi . The G–valued 1–cocycle relative to
the cusps is a 1–cocycle in the usual sense except that its val ue on an edge that
ends (resp. starts) in an ideal vertex pi is only well deﬁned modulo right (resp.
left) multiplication by elements of Pi . This 1–cocycle is well deﬁned up to the
usual action of 0–cocycles, but only 0–cocycles that take va lue 1 ∈ G on ideal
vertices are permitted. The 1–cocycle depends on the choice of the lifts ˜pi ; a
change of lift changes the cocycle on edges to pi by right multiplication by the
element of G that moves the new lift to the old.
There is then an equivalent G–labeling of the 3–simplices as in Section 4.1,
except that the label of an ideal vertex is only deﬁned up to ri ght multipli-
cation by elements of the corresponding parabolic subgroup . We then assign
ideal simplex shapes to the simplices of K by choosing a point z ∈ ∂
H
3
for
each 0–simplex of K , as in Remark 10.5, but with the restriction that the
point z chosen for an ideal vertex is the ﬁxed point ˜ pi of the corresponding
parabolic subgroup. A simplex with G–labels g1, g2, g3, g4 and whose vertices
have been assigned points z1, . . . , z4 in ∂H
3
receives the ideal simplex shape
⟨g1z1, . . . , g4z4⟩.
Suppose we have triangulated M and assigned ideal simplex shapes to the
simplices as above. We also assume that we have chosen the res ulting complex
K so that it admits orderings of its 3–simplices that agree on c ommon faces,
and we ﬁx such an ordering. The arguments of sections 9 and 10 t hen go
through to show the following theorem:
Theorem 14.2 There exists a strong ﬂattening of K as in Theorem 4.5. The
resulting element ∑
i ǫi[xi; pi, qi] ∈ ˆP(C) is in ˆB(C) and only depends on the
hyperbolic manifold M . We denote it ˆβ(M ).
Since ˆB(C) ∼
= H3(G; Z), this gives a “fundamental class” in H3(G; Z) for
any oriented complete ﬁnite volume hyperbolic 3–manifold ( as usual, G =
PSL(2, C) with discrete topology).
Geometry & Topology, Volume 8 (2004)
466 Walter D Neumann
We pointed out in the Introduction that this class is easy to d eﬁne algebraically
if M is compact. I am grateful to the referee for a comment that led me to
a similar elementary description of this class if M has cusps. M can be com-
pactiﬁed to a manifold ¯M with ∂ ¯M consisting of tori. The fundamental class
[ ¯M , ∂ ¯M ] ∈ H3( ¯M , ∂ ¯M ) determines a class in β( ¯M , ∂ ¯M ) ∈ H3(BG, BP ; Z),
where P =
{( 1 ∗
0 1
)}
⊂ PSL(2, C) (as usual, all groups are considered with their
discrete topology). The long exact sequence for the pair ( BG, BP ) simpliﬁes
to
0 → Hi(BG; Z) → Hi(BG, BP ; Z) → Hi−1(BP ; Z) → 0 ,
for i > 1, since the inclusion P → G factors through the Borel subgroup
B =
{( ∗ ∗
0 ∗
)}
⊂ PSL(2, C) and Hi(BP ; Z) → Hi(BB ; Z) is zero for i > 0.
Proposition 14.3 There is a natural splitting
ρ : Hi(BG, BP ; Z) → Hi(BG; Z)
of the above sequence for i > 1.
Proof Denote
P2 :=
{( 2k b
0 2 −k
)
| k ∈ Z, b ∈ C
}
.
One computes that Hi(BP2; Z) = 0 for i > 0. Thus the diagram
0 − − − − →Hi(BG; Z) − − − − →Hi(BG, BP ; Z) − − − − →Hi−1(BP ; Z) − − − − →0

↓
‖
‖
‖
0 − − − − →Hi(BP2, BP ; Z)
∼
=− − − − →Hi−1(BP ; Z) − − − − →0
splits the top sequence. Note that the splitting Hi−1(BP ) → Hi(BG, BP ) is
not canonical, since it depends on the “2” in the deﬁnition of P2 , but it is
not hard to see that its image does not depend on this choice, s o the resulting
splitting
ρ : Hi(BG, BP ; Z) → Hi(BG; Z)
is canonical.
We omit the proof that ρ(β( ¯M , ∂ ¯M )) is indeed the element ˆβ(M ) of Theorem
14.2.
Example 14.4 Figure 8 gives a well-known ideal triangulation for the com-
plete hyperbolic structure on the ﬁgure eight knot compleme nt (see, eg, [23, 16]).
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 467
This manifold is denoted m004 in the Callahan-Hildebrand-Weeks cusped cen-
sus (see [2, 22, 10]). Both simplices are regular ideal simpl ices but the vertex-
order of the second simplex is opposite to its orientation. T he cross-ratio
parameters are therefore ω := eπi/3 and ω−1 respectively, and ˆβ(m004) =
[ω; p, q] − [ω−1; r, s] for suitable p, q, r, s. In the next section we will see that we
get a ﬂattening of the complex K if and only if q = −1−2p and ( r, s) = −(p, q).
Choosing, eg, p = 0, we see
ˆβ(m004) = [ ω; 0, −1] − [ω−1; 0, 1].
If
V0 = 1.014941606409653625021202554 . . .
denotes the volume of the regular ideal tetrahedron, then
R(ω; p, q) = (2p − 2q − 1)π2
12 + V0i ,
R(ω−1; −p, −q) = (2p − 2q − 1)π2
12 − V0i .
Thus
(vol +i cs)(m004) = 2 V0 ,
recovering the known volume and Chern–Simons invariant of t he ﬁgure eight
knot complement.
We now describe what happens when we deform our hyperbolic st ructure by
hyperbolic Dehn surgery to perform a Dehn ﬁlling on M (see, eg, [23, 16]).
Topologically, the Dehn ﬁlled manifold M ′ diﬀers from M in that some of the
cusps have been ﬁlled by solid tori, which adds new closed geo desics at these
cusps (the cores of the solid tori). Let λj be the complex length of the geodesic
(length plus i times torsion) added at the j -th cusp. If no geodesic has been
added at the j -th cusp we put λj = 0.
The deformation deforms the representation Γ = π1(M ) → G. If we keep
the points ˜pi at ﬁxed points of the images of the cusp subgroups of Γ then our
triangulation deforms to what is called a “degree one ideal t riangulation” in [15]
(it is not a genuine triangulation because the topology of K has not changed,
so its topology is not the topology of M ′ ). By deforming the ﬂattened ideal
simplex parameters continuously we obtain ﬂattened ideal s implex parameters
[x′
i; p′
i, q′
i] after deformation.
Geometry & Topology, Volume 8 (2004)
468 Walter D Neumann
Theorem 14.5 With the above notation, the element in ˆB(C) represented by
the Dehn ﬁlled manifold M ′ is
ˆβ(M ′) = −
h∑
j=1
χ(eλj ) +
∑
i
ǫi[x′
i; p′
i, q′
i]
with χ as in Theorem 7.5. Moreover,
(vol +i cs)(M ′) = − π
2
h∑
j=1
λj − i
∑
i
ǫiR(x′
i; p′
i, q′
i)
The second formula of this theorem was proved up to a constant (depending on
K but independent of the Dehn ﬁlling) in [13]. The constant was conjectured
to be a multiple of iπ2/6. Since [13] used unordered simplices, the constant
in that version is indeed a multiple of iπ2/6. Versions prior to 1.10.2 of the
program Snap [10, 4] use this formula but ignores the parity c ondition, giving
answers accurate to iπ2/12. Snappea [22] uses a version, also from [13], that
is accurate to an unknown constant. Both programs then boots trap this to
an accurate computation of the Chern–Simons invariant for a ny manifold that
can be related by a sequence of Dehn drillings and ﬁllings to o ne with known
Chern–Simons invariant. The value they print is cs( M )/2π2 , hence well deﬁned
modulo 1 /2.
Snap now uses the formulae of this paper and can compute Chern –Simons for
any manifold. For compact manifolds accessible by the boots trapping method,
Snap also computes the eta-invariant using a related formul a of [12]; from this
the Riemannian Chern–Simons (deﬁned modulo 2 π2 , hence modulo 1 in their
normalization) is then computed.
Proof of Theorem 14.5 For simplicity of exposition we assume M has just
one cusp represented by the ideal vertex p of K .
The proof depends on the fact that the deformed ﬂattening par ameters [ x′
i; p′
i, q′
i]
still satisfy our ﬂattening conditions around edges, but th ere is a natural ﬂat-
tening condition at the ﬁlled cusps that is not satisﬁed, whi ch leads to the
“correction term” ∑ h
j=1 χ(eλj ) in the theorem.
The link Lp of vertex p of K is a torus. Let C be a simplicial curve in Lp
that is a meridian of the solid torus that the cusp has been rep laced by. We
can obtain a genuine triangulation of M ′ by the blow-up procedure of Section
11, blowing up using the curve C . As in that section, we want to extend the
ﬂattening after blowing up so that matching pairs of added si mplices have the
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 469
same ﬂattening and therefore cancel in the computation of ˆβ(M ′). To be able
to extend the ﬂattening of K after blowing up, we need that the log-parameter
along a normal curve parallel to C is zero. As it stands, it is not zero, since
it represents the logarithm of the derivative of the holonom y of the meridian
curve. It was zero before deformation, but after deformatio n the meridian curve
represents a full rotation about the core curve of the solid t orus added by the
Dehn ﬁlling, so the logarithm of the derivative of its holono my is 2 πi (see, eg,
[23, 16] for more detail). We can use the procedure of Section 11 to correct
this: we must modify ﬂattenings on the simplices traversed b y a normal curve
representing a longitude of the added solid torus as indicat ed in Figure 7 (the
longitude runs horizontally across the center of the ﬁgure) . The eﬀect on each
modiﬁed simplex is to change its contribution to ∑
i ǫi[xi; pi, qi] by something of
the form [ x; p, q ± 1] − [x; p, q] or the equivalent after a permutation of vertices.
By the calculations of Proposition 7.4 this is ±χ(z), where z is the cross-ratio
parameter corresponding to the edge of the 3–simplex that th e curve passes
(so z is one of x, 1 /(1 − x), 1 /x, etc.). As we sum these contributions over
the aﬀected simplices with appropriate signs, they sum to −χ(L), where L is
product of the corresponding cross-ratio parameters or the ir inverses for the
edges passed by the normal curve. This L is the derivative of holonomy of the
longitude and log( L) is the complex length λ of the core curve of the solid torus
added by the Dehn ﬁlling (see, eg, [23, 16]). This proves the ﬁ rst equation of
the theorem.
For the second equation we use the fact that R( ˆβ(M ′)) = i(vol +i cs)(M ′). We
know this if M ′ is compact and we will deduce it below if M ′ is non-compact,
so we assume it for now. R ◦ χ : C∗ → C/π2Z is the map z ↦→πi
2 log z , so
Rχ(eλ) = πi
2 λ. Applying 1
i R to the ﬁrst equation of the theorem thus gives the
second.
Meyerhoﬀ’s extension of Chern–Simons invariant to cusped h yperbolic mani-
folds in [11] is given by deﬁning (vol + i cs)(M ) to be the limit of (vol + i cs)(M ′)
+ π
2
∑ h
j=1 λj as M ′ approaches M in hyperbolic Dehn surgery space. The case
that M ′ is compact in the above Theorem thus implies:
Corollary 14.6 For any oriented complete ﬁnite volume hyperbolic 3–mani-
fold M
i(vol +i cs)(M ) = R( ˆβ(M )) ∈ C/π2Z,
where cs(M ) is Meyerhoﬀ’s extension of the Chern–Simons invariant if M is
non-compact.
Geometry & Topology, Volume 8 (2004)
470 Walter D Neumann
The “correction term” − ∑ h
j=1 χ(eλj ) in Theorem 14.5 arises because the sum
of ﬂattening parameters corresponding to a meridian of the a solid torus added
at a cusp by Dehn ﬁlling is 2 πi rather than zero. The proof of the theorem
shows that ﬂattening parameters can be chosen so that this su m is zero, and
then the correction term is not there. This gives an analog of Theorem 4.6 for
these triangulations:
Theorem 14.7 Consider the degree one triangulation of M ′ of Theorem 14.5.
Then there exists ﬂattenings [x′
i; p′′
i , q′′
i ] of the ideal simplices which satisfy the
conditions
• parity along normal paths is zero;
• log-parameter about each edge is zero;
• log-parameter along any normal path in the neighborhood of a 0–simplex
that represents an unﬁlled cusp is zero;
• log-parameter along a normal path in the neighborhood of a 0–simplex
that represents a ﬁlled cusp is zero if the path is null-homot opic in the
added solid torus.
For any such choice of ﬂattenings we have
ˆβ(M ′) =
∑
i
[x′
i; p′′
i , q′′
i ] ∈ ˆB(C)
so
i(vol +i cs)(M ′) =
∑
i
R(x′
i; p′′
i , q′′
i ) .
