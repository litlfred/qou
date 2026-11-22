---
doc_id: sigma12-065
doc_title: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants"
section_id: sec-012-44-riera-and-rodríguez-basis-algebraically
section_title: "Riera and Rodríguez basis algebraically"
section_number: 4.4
pages: 12-15
source_pdf: sigma12-065.pdf
source_sha256: a6e0e0da5cc5ff9b
toc_source: outline
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
---
We are now in a position to express the Riera and Rodr´ıguez basis on this branched cover.
Recall that
αi = (2i −1) + (2i)
as a prescription on which edges to traverse in the hyperbolic model.
α1
α2
Figure 6. α1 and α2 homology cycles for the Hulek–Craig branched cover. Graphs of subsequent αi are
rotations of these by 2πi
5 .
This becomes a specification to look up the relevant edges in Table 1, and construct a path
that has its main component in the specified regions (circling x = 0 and outside all finite branch
points enough times to reach the correct sheets). In fact, just like Riera and Rodr´ıguez we only
need to construct α1 and α2 and then repeatedly apply (x, y) 7→(ζx, ζ2y) to obtain the rest.
To be explicit and referring to Table 1, α1 must go out along x > 0 with y ≫0 near 0, loop
around infinity until it can come back in to x = 0 along a ray with arg x = 2π
5 and arg y = 4π
5
before looping around 0 until it can join up with the beginning again. A path conforming to
this description is shown in Fig. 6.
Similarly α2 goes out along x > 0 with y < 0, loops and comes back with argument of x
as −2π/5 and argument of y as 6π/5; it is also depicted in Fig. 6.
Using the software6 introduced in [2] with Klein’s curve as an illustrative example, we may
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
and Rodr´ıguez, namely












0
1
−1
1
−1
0
1
−1
−1
0
1
−1
1
0
0
0
1
−1
0
1
−1
1
−1
0
−1
1
−1
0
1
−1
1
0
1
−1
1
−1
0
1
−1
1
0
0
−1
1
−1
0
1
−1
−1
0
1
−1
1
−1
0
1
1
0
0
0
−1
1
−1
0












.
6Located at http://gitorious.org/riemanncycles.
Finally we can calculate the period matrix. This may be done analytically (as in [17]) or
numerically via the extcurves package which calculates the period matrix for any homology
basis (implicitly using the Riemann period matrix given by algcurves[periodmatrix]). Using
the the transformation from (4.2) both methods yield
Theorem 2. The homology cycles α1 and α2 for the Hulek–Craig branched cover reproduce the
cycles of Riera and Rodr´ıguez and their corresponding period matrix
τ = τ0




4
1
−1
1
1
4
1
−1
−1
1
4
1
1
−1
1
4



,
where τ0 is deﬁned by (4.3).
We also note that the action on the homology basis α1,...,8 associated with the antiinvolution
of the real structure is given by
S′ :=












0
0
0
0
0
0
−1
0
0
0
0
0
0
−1
0
0
0
0
0
0
−1
0
0
0
0
0
0
−1
0
0
0
0
0
0
−1
0
0
0
0
0
0
−1
0
0
0
0
0
0
−1
0
0
0
0
0
0
0
0
1
0
1
0
1
0
1












.
It is algorithmic to show that
S := TS′T −1 =












1
0
0
0
1
0
0
0
0
1
0
0
0
1
0
0
0
0
1
0
0
0
1
0
0
0
0
1
0
0
0
1
0
0
0
0
−1
0
0
0
0
0
0
0
0
−1
0
0
0
0
0
0
0
0
−1
0
0
0
0
0
0
0
0
−1












,
where T is the symplectic transformation (with respect to the canonical symplectic form)
T =












−1
2
1
2
−1
1
0
1
0
1
0
−3
0
0
0
−1
−2
1
2
−1
0
1
0
0
0
0
−1
0
−1
0
−1
0
2
−2
−3
−2
0
−1
−1
−1
−1
0
1
3
0
1
0
1
1
−1
−1
−2
0
−1
0
−1
−1
2
3
2
0
1
1
1












.
Here S is the canonical form for an antiholomorphic involution where there is one nondividing
real oval (see for example [18]), again showing there is one real oval.
