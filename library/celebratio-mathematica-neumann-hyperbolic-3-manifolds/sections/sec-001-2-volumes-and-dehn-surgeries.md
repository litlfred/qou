---
doc_id: celebratio-mathematica-neumann-hyperbolic-3-manifolds
doc_title: "Jump to Bibliography by Stavros Garoufalidis and Don Zagier Published: 2023"
section_id: sec-001-2-volumes-and-dehn-surgeries
section_title: "Volumes and Dehn surgeries"
section_number: 2
pages: 4-9
source_pdf: Celebratio Mathematica — Neumann — Hyperbolic 3-Manifolds.pdf
source_sha256: 9e541693c60cbd3f
toc_source: inferred
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
duplicate_of: "arxiv-2304.12545v1"
---
As already stated, the original main purpose of [1] was to study the arithmetic of
the set of volumes of all hyperbolic 3-manifolds. It had been observed by Thur‐
ston, using earlier work of Jørgensen, that this volume spectrum is a well-ordered
subset of the positive reals. In other words, there is a smallest volume (which is
known), a second smallest, a third smallest, …, then a smallest limit point, a
second smallest limit point, …, then limits of these, and so on. The proof of well-
orderedness shows that these simple and higher-order limit points arise by “clos‐
ing up” one or more of the cusps of a noncompact hyperbolic 3-manifold 
 by
Dehn surgeries to obtain a countable collection of manifolds with fewer cusps
whose volumes tend from below to that of 
. The object of [1] was to study the
speed with which these volumes converge.
Before studying the effect of surgeries, we must understand the volume of a single
hyperbolic 3-manifold 
. Clearly it can be given as the sum of the volumes of the
tetrahedra of any ideal triangulation, so the first step is to understand these. An
(oriented and nondegenerate) ideal tetrahedron can be parametrized either by a
shape parameter  in the complex upper half-plane, as explained in the preceding
⇧
section, or, in case  is in the upper half-plane, by the three angles , ,  (positive
and with 
) of the Euclidean triangle that one “sees” by looking at
the tetrahedron from any of its four cusps. When 
, the angles and the
shapes are related by 
, with 
 and 
 as
above.
According to Chapter 7 of Thurston’s notes, written by Milnor, the volume of this
tetrahedron when 
 is given in terms of these two parametrizations by
the two formulas
the equality of the two being an identity due to Kummer. (Both formulas are actu‐
ally true for all 
, but the sum of ,  and  is 
 if  is in the lower half-
plane.) Here 
 and 
 are the Bloch–Wigner dilogarithm (see Section 3) and
the Lobachevsky function, defined respectively by
Thus the volume of a hyperbolic manifold 
 triangulated by 
 ideal tetrahedra
with shape parameters  is given in terms of the dilogarithm function by
Now let 
 be a 3-manifold with  cusps. It has a unique complete hyperbolic
structure as a quotient 
 for some lattice 
 isomorphic to 
,
the corresponding shape parameters 
 being a solution of all
 equations (1) and (2). A small deformation of this hyperbolic structure
will have a nearby shape parameter vector 
 satisfying only (1). By
the result of Thurston mentioned earlier, the space of all such deformations has
the structure of a smooth complex manifold of dimension  , so it is isomorphic to
a small neighborhood  of 0 in 
. Thus each 
 depends holomorphically on
 and 
. To make this more visible, and to choose nice coordinates
 on  , we have to look more closely at the structure of the cusps on 
 and at
Dehn surgeries.
Each cusp has the structure 
, where 
 is a totally geodesically em‐
bedded torus in 
 and has a flat Euclidean metric, unique up to homothety, in‐
duced by the hyperbolic metric on 
. More concretely, the cusps of 
are indexed by 
, whose stabilizer 
 is free abelian of rank 2. After con‐
⇧
Л
Л
Л
Л
Л
jugation we can place  at 
, in which case 
 has the form
for some lattice 
, unique up to homothety, and then we can identify  with
 and 
 with 
. There is a canonical quadratic form on  defined as
the square of the length of a vector divided by the volume of 
. If we choose an
oriented basis 
 of 
 (“meridian” and “longitude”) to identify  with 
, then this quadratic form is given by
if we rescale 
 after homothety to be 
 for some  in the complex upper
half-plane.
On the other hand, each element of 
 can be identified with an isotopy
class of closed curves on 
. Doing a 
 Dehn surgery at a cusp, once the basis
of 
 has been chosen, means removing 
 from 
 and replacing
it by a solid torus in such way that the curve on 
 corresponding to the class
 bounds in the solid torus. Here we assume that the integers  and  are
coprime, but we also allow “
” as a value for 
, meaning that we leave this
cusp untouched. The Dehn surgeries on 
 are then described by tuples
Thurston’s theorem [e7] tells us that if all 
 are near enough to 
 (meaning
that 
 or 
 is large), the surgered manifold 
 is hyperbolic, in
which case both the shape parameters 
 and the volume 
 be‐
come functions of  . Explicitly, the deformed shape parameters 
that tend to 
 as all the pairs 
 tend to infinity are given by adding to the
original gluing equations (1) the  new equations given by the product of the 
-th
power of the first expression by the -th power of the second one in (2), and then
 is given by (6) with 
 replaced by 
.
⇧
We now get two real numbers at each cusp: the value 
 of the quadratic
form corresponding to that cusp at the pair 
 (with the convention 
) and the length 
 of the short geodesic on 
, which is
the core of the solid torus added by the Dehn surgery (or 0 if the -th cusp has not
been surgered). They are related by
([1], Proposition 4.3) as all 
 tend to infinity. The main volume result
of [1], proved by using (6) and analyzing the changes of the dilogarithms under
small changes of the  ’s, is then given by the pair of asymptotic formulas
(Theorems 1A and 1B in [1]), which are equivalent to one another by virtue of (7).
These volumes, as 
 ranges over all -tuples of sufficiently large pairs of
coprime integers or the symbol 
 meaning unsurgered, all belong to the hyper‐
bolic volume spectrum, and equation  (8a) has as an immediate corollary a de‐
scription of the local structure of this volume spectrum near its limit point, be‐
cause the asymptotics of the number of lattice points, or of primitive lattice points,
in a large ellipse, is well known. The precise asymptotic statement, which we will
not repeat here, is formulated explicitly as a corollary to Theorem 1A in [1].
All of this is only for integral (and coprime) values of 
 and  . However, as is ex‐
plained in [1] in detail, the shape parameters 
 and the lengths 
 are
defined for  and  real rather than just integral and coprime in pairs, and equa‐
tions (7) and (8) still remain true. The only point is that in the definition of the 
’s we had to take the 
-th and 
-th powers of the equations in (2), and one can‐
not in general take real powers of complex numbers in a well-defined way, but
since the left-hand sides of the expressions in (2) are near to 1 for small deforma‐
tions of the original value 
 and since a complex number near 1 has a well-
defined logarithm near 0, there is no problem. When the 
 and  are not integral,
we are no longer “filling in” the cusp by gluing on a solid torus, but are simply
changing the hyperbolic structure on the original open topological manifold 
,
with the new hyperbolic structures in general being incomplete. If we now define
⇧
 complex numbers 
 and 
 by
then from the symplectic properties of the gluing equations it follows that ([2],
Lemma 4.1)
and we can take  as canonical coordinates for the above-mentioned neighbor‐
hood  of 
, in which case each 
 becomes an odd power series in the ’s
with linear term 
 and we can write 
 and 
 instead of 
 and 
. We should mention that  and  can be defined invariantly, without us‐
ing any triangulation, as follows: the deformed hyperbolic structure on 
 corres‐
ponds to a homomorphism 
 near to the inclusion map, and then
 and  are simply the logarithms of the ratios of the eigenvalues of the images un‐
der  of the meridians and longitudes, respectively.
In terms of the new coordinates, equation (8b) becomes
with 
 as  tends to 0 in 
. Theorem 2 of [1] was the statement
that the function 
 defined by (9) is harmonic, and hence is the real part of a
holomorphic function 
 near 0 (uniquely determined if we fix 
). The‐
orem  3, proved using equation  (3), said that 
 is symmetric in  and ,
which implies that there is a single function 
 with 
 for all  , and
that 
 is given in terms of 
 by 
 (or equivalently by
, where 
 is the Euler operator), so that the
volume correction 
 in (9) is given by
The function  is now often called the Neumann–Zagier potential function, al‐
though this name was used in the original paper for  instead. It should perhaps
also be mentioned that simpler proofs of the last results described could probably
have been obtained by using the second rather than the first volume formula
in (4).
There is one more important point about volumes. Another insight by Thurston
was that the volume of a hyperbolic 3-manifold, which is a positive real number, is
⇧
actually in a natural way the imaginary part of a complexified volume whose real
part is the Chern–Simons invariant, an important topological invariant taking val‐
ues in 
 whose definition we omit here. It was conjectured in [1], and
proved soon afterwards by Yoshida [e2], that the above formulas remain true with
the volumes replaced by their complexified versions, the functions 
 also lif‐
ted suitably from  to  , and 
 replaced by 
. Later, in [2], Walter showed
how to lift  (6) to an explicit and computable expression for the complexified
volume of 
 in terms of the complex dilogarithm.
