---
doc_id: milnor-1982-hyperbolic-geometry-the-first-150-years
doc_title: "BULLETIN (New Series) OF THE AMERICAN MATHEMATICAL SOCIETY"
section_id: sec-004-18-john-milnor
section_title: "JOHN MILNOR"
section_number: 18
pages: 10-12
source_pdf: milnor-1982-hyperbolic-geometry-the-first-150-years.pdf
source_sha256: d444d7a61af54c7c
doc_brief: "BULLETIN (New Series) OF THE AMERICAN MATHEMATICAL SOCIETY HYPERBOLIC GEOMETRY: THE FIRST 150 YEARS BY JOHN MILNOR This will be a description of a few highlights in the early history of — 9 sections"
---
Integrating the negative log absolute value of both sides we obtain 
n-\ 
(1) Ji(n0)/n = 2 ^{9 + itk/ri) + constant. 
A:=0 
For example, if n = 2, then 
JI(20)/2 = JI(0) + JI(9 + TT/2) + constant. 
Substituting 9 = TT/2 or 9 = 0 in this last equation and subtracting, we see 
that JI(TT) — JI(0) = 0. Since the derivative J\'{0) = -log|2 sin 9\ is periodic of 
period 77, this proves that JI itself is also periodic of period 77. 
Finally, to prove that the constant in equation (1) is zero, we can simply 
average over all values of 9 mod 77, noting that JI has average zero since it is 
an odd function. • 
This function JI(0) is closely related to the dilogarithm function 
which has been studied by Euler, Abel, and many others. The precise 
relationship is described by the identity 
L2(em) = TT2/6 - 9{<TT - 0) + 2iji(tf) 
for 0 < 9 < 77. (Compare Lewin [1958].) This identity can be verified by 
differentiating both sides f or 0 < 9 < IT, using the limiting value as 9 -> 0 to 
compute the constant TT2/6. 
Taking the imaginary part of both sides, we obtain the uniformly conver­
gent Fourier series expansion 
(2) ^(sin2n9)/n2 = 2ji(9), 
which is valid for all values of 9. 
For actual computation, it is much better to work with the series 
„W-^-.^i + E^^), 
which converges for |0| < 77 and hence converges quite rapidly for small 9. 
Here 
^1 = 6» ^2 == 30' * • ' 
are Bernoulli numbers. This equation can be proved by twice integrating the 
usual Laurent series expansion for -cot 9. 
Here is an illustration of the utility of this function in computing hyper­
bolic volumes. 
LEMMA 2. Consider an ideal hyperbolic 2>-simplex, that is a simplex A with all 
four vertices on the sphere of points at infinity. If a, fi, y are the dihedral angles 
along three edges meeting at a common vertex, then a + fi + y = IT, and 
volume(A) = Ji(a) + Ji({i) + Ji(y). 
HYPERBOLIC GEOMETRY 19 
It does not matter which particular vertex we choose, since it follows easily 
that opposite dihedral angles are equal so that we obtain the same three 
dihedral angles a, /?, y incident to any vertex. 
This computation would follow easily from formulas of Lobachevsky 
[1836], although as far as I know he never worked out this particular example. 
(Compare Coxeter [1935].) 
PROOF. We will use the Beltrami upper half-space model, with metric 
ds2 = (dx2 + ay2 + dz2)/z2 and associated volume element dx ay dz/'z3, 
where z > 0. Let us position the ideal simplex A so that one of its faces lies in 
the hemisphere z = (1 — x2 — y2)ï/2, and its opposite vertex lies at the 
infinite point. Projecting A orthogonally to the unit disk in the x9 y -plane, we 
obtain a triangle inscribed in this disk with angles a, /?, y. These are the 
angles of a euclidean triangle; so evidently a + /? + y = 77. 
It follows easily from this picture that these angles determine A up to 
congruence (compare Andreev [1970]), and are subject to no other restric­
tions. 
FIGURE 6. A triangle inscribed in the unit disk 
If all three angles are acute, then barycentrically subdividing from the 
origin, we obtain six right triangles as illustrated in Figure 6. (The case of an 
obtuse angle can be handled by a similar argument, or by analytic continua­
tion.) Take the region in the upper half space lying over just one of these 
triangles, namely the shaded one. We must integrate the Beltrami volume 
element dx ay dz/z3 over the region defined by inequalities 
>yi-*2- 0 < y < x tan a, 0 < x < cos a. 
Integrating with respect to z, we obtain \ dx dy/(\ — x2 — y2). Integrating 
with respect to y, we obtain 
dx ri (A , . 1 (A x-ixtana dx, A cos a + x sin a - [\og{A +y)- log(A -y)]0 = 4^1°gi<C0.a_Jcril|g
