---
doc_id: sigma12-065
doc_title: ""
section_id: sec-006-43-understanding-the-isomorphism-f
section_title: "Understanding the isomorphism f"
section_number: 4.3
pages: 9-15
source_pdf: sigma12-065.pdf
source_sha256: a6e0e0da5cc5ff9b
doc_brief: "Bring’s Curve: its Period Matrix and the Vector of Riemann Constants ⋆ — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
---
We now turn our attention to the isomorphism, f, mentioned in (4.1). Clearly there won’t be
a single isomorphism since if a is an automorphism of H and σ of an automorphism of the
HC curve then σ◦f◦a will also be an isomorphism from the hyperbolic model H to the HC
representation. We will exploit this fact.
There are two key ingredients to our identification. First is the rotation of the entire hy-
perbolic polygon about its centre by 2 π/5 (the automorphism cd above). This automorphism
allows us to express all twenty of the polygon’s edges in terms of just four, a great simplification
of our problem. If we knew the values of f on four edges, and the matrix representing f∗(cd),
the induced action of cd on the HC curve, then
f(edge k + 4) =f ((cd)(edge k)) =f∗(cd)f(edge k),
which allows us to compute the values of f on the remaining 16 edges.
Second is a geodesic reflection of the hyperbolic disc which will correspond to our real struc-
ture; the geodesic is denoted by the dashed lines in Fig. 2. The line starts at P3, goes through C
to P1, along edge 1 to P2 and along edge 3 back to P3. If we knew how this acted on the HC
model, we would know its fixed points correspond in some manner to edges 1/14 and 3/12,
and the marked diameter. Identifying points P1, P2 and P3 on the HC representation would
then complete the picture by dividing this fixed line up into just the intervals needed to draw
homology paths around known branch points.
Starting with the central rotationcd on the hyperbolic model and some isomorphism f to the
HC representation, since all order 5 elements of S5 are conjugate there is an HC-automorphism
σ∈S5 such that
σf∗(cd)σ−1 =Zk,
10 H.W. Braden and T.P. Northover
where k∈{ 0,..., 4} and
Z : [ x,y,z ]↦→
[
ζx,ζ 2y,z
]
.
We are being flexible about which power of Z occurs here because later choices (specifically
rotations about R in Fig. 2) will modify any decision made at this stage. But then
(σ◦f)∗(cd) =σ∗(f∗(cd)) =σf∗(cd)σ−1 =Zk.
So the isomorphism σ◦f from the hyperbolic model to the HC model sends cd to Zk.
Now consider a rotation about R in Fig. 2 which cyclically permutes the fixed points of cd.
The fixed points on the hyperbolic side are C, P1, P2, P3 and on the HC side [0 , 1, 0], [0, 0, 1],
[1, 0, 0]1, [1, 0, 0]2. Let integers i and n be defined by the equations
Pi = (σ◦f)−1([0, 0, 1]), R n(Pi) =C.
Then
(σ◦f◦R−n)(C) = (σ◦f◦R−n)(Rn(Pi)) = (σ◦f)(Pi) = [0, 0, 1],
and further
(
σ◦f◦R−n)
∗ (cd) = (σ◦f)∗
(
R−n
∗ (cd)
)
= (σ◦f)∗
(
(cd)j)
=Zjk =Zm,
for some integers j and more importantly m. Since we haven’t fixed the power of Z up to now
this means that σ◦f◦R−n serves our purposes just as well as σ◦f did.
Although we have used most of the available freedoms to constrain the relation between f,Z
and C, we actually still have the ability to apply a central rotation, if it would help since that
would alter neither of the properties above.
Next consider complex conjugation on the HC model. This is a symmetry that reverses
orientation (and so not part of the S5 symmetry group). It fixes an entire line (the real axis)
including the fixed points of Z. In the hyperbolic picture this means it must be a reflection
about some diameter. We use our final remaining freedom to demand that it is reflection about
the dashed diameter in Fig. 2, i.e. that the real axis in the HC model corresponds to these
dashed edges (and diameter).
We now have two tasks remaining:
• Find out what P1, P2 and P3 become on the HC model so we can describe edge 1/14 as
the real path from P2 to P1 and edge 3/12 as the real path from P2 to P3.
• Find out what power of Z the central rotation of 2 π/5 becomes so we can describe (for
example) edge 4/15 as Zk applied to the real path from P2 to P3.
The second task is actually easier to accomplish at this stage. Consider the structure near
[0, 0, 1] (which we demanded was the centre of the polygon, C, hyperbolically); there are three
sheets coming together at this branch so unwrapping it will effectively divide angles by 3. Ma-
thematically this means that any set of manifold coordinates φ :C→ C centred on [0, 0, 1] will
satisfy
φ([x,y, 1])3 =αx +O
(
x2)
.
In these coordinates, since [0 , 0, 1] is a fixed point Z : [x,y,z ]↦→ [ζx,ζ 2y,z ] acts locally as a
rotation
Zφ(t) =βt +O
(
t2)
,
Bring’s Curve: its Period Matrix and the Vector of Riemann Constants 11
Sheet 1
Sheet 2
Sheet 3
ǫ
Z(ǫ)?
Z(ǫ)
Z(ǫ)?
Figure 4. Intuitive action of Z near [0, 0, 1].
where β is characteristic of Z and independent of φ. Now, on the one hand
Zφ (φ([x,y, 1]))3 =φ (Z([x,y, 1]))3 =φ
(
[ζx,ζ 2y, 1]
)3 =αζx +O
(
x2)
,
but also
Zφ (φ([x,y, 1]))3 =
(
βφ([x,y, 1]) +O
(
φ2))3
=β3φ([x,y, 1])3 +O
(
φ4)
=β3αx +O
(
x2)
.
So β3 =ζ, or
β = exp
(2πi
15 + 2πik
3
)
for some k∈{ 0, 1, 2}. But since Z has order 5 we also know that β5 = 1, which in terms of k
means that
2πi
3 + 10πik
3 = 2πi
3 (1 + 5k)∈ 2πiZ,
or β = exp( 4πi
5 ) and at last we can conclude that Z corresponds to a rotation of 2 2πi
5 about C
in the hyperbolic model.
Intuitively we have unwrapped the three sheets coming together at [0 , 0, 1] to obtain Fig. 4
in x. We know that Z sends (say) [ϵ,y, 1] to [ζϵ,y′, 1] on some sheet y′, which makes it one of
the labelled destinations. But only one of these gives an order 5 transformation so we know Z
completely.
Using this information, together with our knowledge that complex conjugation on the HC
model is the dashed reflection in Fig. 2, allows us to deduce the outline structure in Fig. 5. The
dots are the branch-points of the HC model and the grey lines are the images of the hyperbolic
polygon’s edges under the isomorphism to the HC model. It remains to establish which parts
(and sheets) of each spoke in Fig. 5 correspond to which hyperbolic edges (for example, does
edge 1/14 correspond to x> 0 or x< 0, and what about y?).
Similar analysis of the other fixed points of Z will allow us actually to identify the remai-
ning Pi. We first discover
• Near [0, 1, 0], Z is a rotation of 3
( 2π
5
)
.
• Near [1, 0, 0]1∼ [1,t 4,t ], Z is a rotation of 4
( 2π
5
)
.
12 H.W. Braden and T.P. Northover
1/14 and 3/12
2/9 and 11/20
10/17 and 8/19
5/18 and 7/16
6/13 and 4/15
Figure 5. Hyperbolic polygonal edges in the Hulek–Craig model.
T able 1. Values for [x,y, 1] on hyperbolic edges.
1/14 [ R+, R+, 1] 2/9 [ ζR+,ζ 2R+, 1]
3/12 [ R+, R−, 1] 4/15 [ ζ4R+,ζ 3R−, 1]
5/18 [ ζ3R+,ζ R+, 1] 6/13 [ ζ4R+,ζ 3R+, 1]
7/16 [ ζ3R+,ζ R−, 1] 8/19 [ ζ2R+,ζ 4R−, 1]
10/17 [ ζ2R+,ζ 4R+, 1] 11/20 [ ζR+,ζ 2R−, 1]
• Near [1, 0, 0]2∼ [1,t,t 4], Z is a rotation of 2π
5 .
But hyperbolically, it is easy to see that a rotation of 2
( 2π
5
)
about C (whichZ is) is the same
as one of 4
( 2π
5
)
about P1, 3
( 2π
5
)
about P2 or 2π
5 about P3 so we can deduce that [0, 1, 0]↔P2,
[1, 0, 0]1∼ [1,t 4,t ]↔P1 and [1, 0, 0]2∼ [1,t,t 4]↔P3.
Therefore, edge 1/14 corresponds to the real path from [0, 1, 0] to [1, 0, 0]1∼ [1,t 4,t ]; referring
to Fig. 1 we see that this is the path where y starts out large and positive near x = 0 (and
remains positive). Edge 3 corresponds to the real path from [0 , 1, 0] to [1, 0, 0]2∼ [1,t,t 4] which
turns out to be the one starting out large and negative near x = 0 (and remaining negative).
The remaining paths (y small nearx = 0) correspond to the diameter of the hyperbolic model
and have no large role to play in describing the homology basis.
Other edges can now be obtained by applying a rotation of 2 π/5 on the hyperbolic side
and Z3 on the HC side. The results are in Table 1.
4.4 Riera and Rodr´ ıguez basis algebraically
We are now in a position to express the Riera and Rodr´ ıguez basis on this branched cover.
Recall that
αi = (2i− 1) + (2i)
as a prescription on which edges to traverse in the hyperbolic model.
Bring’s Curve: its Period Matrix and the Vector of Riemann Constants 13
α1 α2
Figure 6. α1 andα2 homology cycles for the Hulek–Craig branched cover. Graphs of subsequent αi are
rotations of these by 2πi
5 .
This becomes a specification to look up the relevant edges in Table 1, and construct a path
that has its main component in the specified regions (circling x = 0 and outside all finite branch
points enough times to reach the correct sheets). In fact, just like Riera and Rodr´ ıguez we only
need to construct α1 and α2 and then repeatedly apply (x,y )↦→ (ζx,ζ 2y) to obtain the rest.
To be explicit and referring to Table 1, α1 must go out along x> 0 with y≫ 0 near 0, loop
around infinity until it can come back in to x = 0 along a ray with arg x = 2π
5 and argy = 4π
5
before looping around 0 until it can join up with the beginning again. A path conforming to
this description is shown in Fig. 6.
Similarly α2 goes out along x > 0 with y < 0, loops and comes back with argument of x
as−2π/5 and argument of y as 6π/5; it is also depicted in Fig. 6.
Using the software 6 introduced in [2] with Klein’s curve as an illustrative example, we may
read these paths into extcurves and convert them into a full basis with the commands
> curve, hom, names := read_pic("homology.pic"):
> zeta := exp(2*Pi*I/5):
> trans := (x,y) -> [zeta^3*x,zeta*y]:
> for i from 1 to 3 do
hom := [op(hom),
transform_extpath(curve, hom[-2], trans),
transform_extpath(curve, hom[-1], trans)];
od:
An immediate check to this calculation is provided by calculating the intersection matrix of
this constructed basis. The command
> Matrix(8, (i,j) -> isect(curve, hom[i], hom[j]));
produces (with considerably less work and chance of error) precisely the matrix claimed by Riera
and Rodr´ ıguez, namely


0 1 −1 1 −1 0 1 −1
−1 0 1 −1 1 0 0 0
1 −1 0 1 −1 1 −1 0
−1 1 −1 0 1 −1 1 0
1 −1 1 −1 0 1 −1 1
0 0 −1 1 −1 0 1 −1
−1 0 1 −1 1 −1 0 1
1 0 0 0 −1 1 −1 0


.
6Located at http://gitorious.org/riemanncycles.
14 H.W. Braden and T.P. Northover
Finally we can calculate the period matrix. This may be done analytically (as in [17]) or
numerically via the extcurves package which calculates the period matrix for any homology
basis (implicitly using the Riemann period matrix given by algcurves[periodmatrix]). Using
the the transformation from (4.2) both methods yield
Theorem 2. The homology cycles α1 and α2 for the Hulek–Craig branched cover reproduce the
cycles of Riera and Rodr´ ıguez and their corresponding period matrix
τ =τ0


4 1 −1 1
1 4 1 −1
−1 1 4 1
1 −1 1 4

,
whereτ0 is deﬁned by (4.3).
We also note that the action on the homology basis α1,...,8 associated with the antiinvolution
of the real structure is given by
S′ :=


0 0 0 0 0 0 −1 0
0 0 0 0 0 −1 0 0
0 0 0 0 −1 0 0 0
0 0 0 −1 0 0 0 0
0 0 −1 0 0 0 0 0
0 −1 0 0 0 0 0 0
−1 0 0 0 0 0 0 0
0 1 0 1 0 1 0 1


.
It is algorithmic to show that
S :=TS′T−1 =


1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 0
0 0 1 0 0 0 1 0
0 0 0 1 0 0 0 1
0 0 0 0 −1 0 0 0
0 0 0 0 0 −1 0 0
0 0 0 0 0 0 −1 0
0 0 0 0 0 0 0 −1


,
where T is the symplectic transformation (with respect to the canonical symplectic form)
T =


−1 2 1 2 −1 1 0 1
0 1 0 −3 0 0 0 −1
−2 1 2 −1 0 1 0 0
0 0 −1 0 −1 0 −1 0
2 −2 −3 −2 0 −1 −1 −1
−1 0 1 3 0 1 0 1
1 −1 −1 −2 0 −1 0 −1
−1 2 3 2 0 1 1 1


.
HereS is the canonical form for an antiholomorphic involution where there is one nondividing
real oval (see for example [18]), again showing there is one real oval.
