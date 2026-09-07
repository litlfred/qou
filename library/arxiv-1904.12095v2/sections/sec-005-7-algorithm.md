---
doc_id: arxiv-1904.12095v2
doc_title: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner"
section_id: sec-005-7-algorithm
section_title: "Algorithm"
section_number: 7
pages: 15-20
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
doc_brief: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed"
---
7.1 Overview
Let T be an oriented, ﬁnite 3-dimensional triangulation. Let o = V (T ) be the number
of vertices and index the edges E(T ) = {e1, .. .,em}. Assume we are given ﬂoating-point
3For example, Manifold("m003(-3.3,1.1)") in SnapPy gives a geometric spun triangulation for the
singular hyperbolic structure on the closed Weeks manifold m003(-3,1) with cone angle 2π/1.1.
16
approximations for the edge parameters νe1,. .. ,νem such that the Θe1,. .. ,Θem are ap-
proximately 2π (e.g, using the program Orb [Hea] based on the methods described in
[Hea05, Section 2.2]).
We will either fail in one of the steps or obtain intervals νe1, .. .,νem guaranteed to con-
tain values for νe1, .. .,νem yielding a hyperbolic structure on T as follows:
I. Find a subsystem of equations of full rank:
Since the given approximations for the edge parameters are close to a hyperbolic
structure, evaluating the Jacobian
M =
( ∂Θe j
∂νei
)
i =1,...,m;j =1,...,m
(7.1)
gives a matrix close to a singular matrix that we expect to have rank m − 3o (see
Conjecture 9.1). Pick a suitable set of m − 3o rows and columns such that the
resulting submatrix of M has full rank.
This corresponds to picking two partitions of the edges of T
E(T ) = E ∼ ∪ E = with E ∼ = {e∼
1 ,. .. ,e∼
3o}, E = = {e=
1 , .. .,e=
m−3o}
E(T ) = E ﬁxed ∪ E var with E ﬁxed = {eﬁxed
1 , .. .,eﬁxed
3o }, E var = {evar
1 ,. .. ,evar
m−3o}
such that
M ′ =
( ∂Θe=
j
∂νevar
i
)
i =1,...,m−3o;j =1,...,m−3o
has full rank near the given values. Keep the values of νeﬁxed
i
ﬁxed from now on.
II. Find an interval solution to the above subsystem of equations:
Using interval Newton method or Krawczyk test, ﬁnd large enough intervals
νevar
1
,. .. ,νevar
m−3o
for the edges in E var such that they contain a point where Θe=
j
= 2π for every
e=
j ∈ E =. To have intervals νe1,. .. ,νem for all edges of the triangulation, simply use
the interval [νeﬁxed
i
, νeﬁxed
i
] containing only the ﬁxed value νeﬁxed
i
for each remaining
edge eﬁxed
i ∈ E ﬁxed .
III. Ensure solutions are valid for a simplex:
Using the intervals for each edge, use interval arithmetic to verify the conditions
of Lemma 2.2 for each simplex ∆.
IV . Ensure that the remaining edge equations are “approximately” fulﬁlled:
Use these intervals to compute intervals Θe∼
1 ,. .. ,Θe∼
3o for the sums of dihedral an-
gles adjacent to an edge in E ∼ to ensure that 2π ∈ Θe∼
j
for every such edge.
17
V . Ensure that the remaining edge equations are fulﬁlled exactly:
Find a gimbal loop Γ1,. .. ,Γo for each vertex and consider the resulting gimbal
function g . Ensure that K = Θe∼
1 × · · · ×Θe∼
3o avoids gimbal lock for the intervals
computed in the previous step using interval arithmetics.
7.2 Computing the Jacobian
Note that the formulas given in [Hea05, Lemma 2.5] for the derivatives∂θi j /∂vmn (where
vmn = vnm ) run into a division by zero whenθi j = π/2. To obtain formulas avoiding this
problem, we take the total derivative of Equation 2.1
∂θi j
∂vmn
= −1√
ci ic j j − c2
i j
( ∂ci j
∂vmn
−
ci j
2ci i
· ∂ci i
∂vmn
−
ci j
2c j j
·
∂c j j
∂vmn
)
and note that each∂ckl /∂vmn = (−1)k+l ∂(detGkl )/∂vmn is, up to sign, the sum of at most
two cofactors of Gkl , namely, the ones corresponding to the 2 × 2-matrices that can be
obtained by deleting from Gkl the row and column corresponding to row m or n and
column n, respectively, m of G.
Using this, we can compute the Jacobian M in (7.1) using ﬂoating point (in Step I), re-
spectively, interval arithmetics (in Step II) avoiding the need for automatic differentia-
tion.
7.3 Step I: Finding a submatrix of full rank
This step is necessary since interval methods (e.g., interval Newton method or Krawczyk
test) only work for systems with invertible Jacobian. To obtain a subsystem of full rank,
we apply the following algorithm to M with h = m − 3o:
18
Input: Square-matrix M = (mr,c) with expected rank h.
Output: Sets R and S of indices ofh rows, respectively,h columns.
The submatrix M ′ of M formed by these rows and
columns will have full rank.
Algorithm:
1. R ← {}. C ← {}.
2. Repeat h times:
1. Let ( r,c) be the index of the entry mr,c in M with the largest
absolute value when ignoring the rows inR and columns in C .
2. Add multiples of row r to all other rows of M to make all en-
tries except for mr,c in column c zero.
3. Add multiples of column c to all other columns of M to make
all entries except for mr,c in row r zero.
4. R ← R ∪ {r }. C ← C ∪ {c}.
Remark 7.1. Note that the algorithm has the following stability properties:
(a) We obtain the same set of rows and columns of M when permuting the rows or
columns of the input matrix M, i.e., the result is obtained by applying the same
permutation to R, respectively,C — unless there are ties in Step 2.1.
(b) Transposing M results in interchanging R and C .
Remark 7.2. This algorithm is a simpliﬁed version of LDU -factorization with full piv-
oting, i.e., a decomposition M = P LDU P′ where P and P ′ are permutation matrices, L
and U unit-lower, respectively, unit-upper triangular matrices andD a diagonal matrix.
7.4 Step II
This step is a straightforward application of the interval Newton method or Krawczyk
test to the equations Θe=
j
− 2π = 0 in variables νevar
i
(keeping νeﬁxed
i
ﬁxed). Note that even
for high precision solutions, computing the approximate inverse in the Krawczyk test
using IEEE754 double-precision ﬂoating point numbers is usually sufﬁcient.
If we are interested in increasing the precision of the solution, we can optionally per-
form the ordinary Newton method to the subsystem from Step I before Step II.
7.5 Steps III and IV
These conditions are straightforward to check with interval arithmetics given the com-
ment about the Budan-Fourier theorem in Lemma 2.2.
19
7.6 Step V: Finding gimbal loops
We need to pick a gimbal loop Γk in each “vertex link” ( Lk,L=
k ). Note that this com-
plex consists of the small hexagons (with alternating β- and γ-edges) of the doubly-
truncated simplices (see Figure 2) and polygons coming from the ends of the prisms
(see Figure 3 and 9). For a vertex vk, pick a hexagon in L=
k , mark it as “used” and starting
with its boundary (oriented such that it traverses a γσ(0)σ(1)σ(2) with σ ∈ A4), expand this
edge-loop until it touches each boundary component of L=
k as follows: pick a β-edge of
the edge-loop that is adjacent to an unused hexagon H and replace the β-edge by the
ﬁve other edges of H, marking H as “used” (see Figure 10). It is faster to exhaust all β-
edges of one hexagon ﬁrst in breadth-ﬁrst search manner (vs depth-ﬁrst search) before
moving on to the next hexagon.
u u u u
u
u
u
u
u
u
u
u
u
u
Figure 10. Procedure to ﬁnd a gimbal loop Γ.
7.7 Step V: Computing the gimbal function’s derivative
We then need to compute [Dg (K )] which boils down to computing the derivatives∂mΓk /∂Ti
of the gimbal matrices mΓk associated to the gimbal loops Γk. Focusing on one i and k,
note that mΓk is given by an alternating product the form
∏
1 ·RTi ·
∏
2 ·RTi ·
∏
3 ·RTi · · ·
∏
q
where ∏
k stands for a product of β- and γ-matrices and rotations RTi ′ with i ′ ⁄= i (q is
actually at most three since an edge of T has two ends which might or might not end in
the same vertex). We can then compute the derivative as
∂mΓk
∂Ti
=
∏
1 ·R ′
Ti ·
∏
2 ·RTi ·
∏
3 · · ·RTi ·
∏
q
+ · · ·
+
∏
1 ·RTi ·
∏
2 ·RTi ·
∏
3 · · ·R ′
Ti ·
∏
q where R ′
ω =


−sin ω −cos ω
cos ω −sin ω
0

.
We need to evaluate this using the intervals from Step II for the β- and γ-matrices and
the intervals Θe∼
1 , ... ,Θe∼
3o from Step IV for R ′
Ti
and all the RT j .
20
7.8 Step V: Verifying invertibility
To show that a square matrix m with real interval entries is invertible (in the sense
used in Deﬁnition 4.8 and 5.1), we can ﬁnd an approximate inverse n (usually IEEE754-
double precision is sufﬁcient) and verify that each entry of mn − Id has absolute value
strictly less than 1/r 2 where r is the number of rows.
