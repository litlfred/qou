---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A ≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods"
section_id: sec-023-evaluation-of-the-magnetic-multipoles
section_title: "Evaluation of the magnetic multipoles"
section_number: null
pages: 24-25
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
toc_source: outline
doc_brief: "Magnetic structure of A ≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods — 26 sections: Magnetic structure of A 10 nuclei ; Introduction; Theory"
---
Using Eq. (18) we can evaluate the value of the reduced
matrix elements for the magnetic multipole operators. To
do that we need a number of linear equations equal to the
number of the multipoles allowed by the transition.
As stated in Ref. [67] for VMC and GFMC, in order
to obtain the linear equations we need for the extraction
of the reduced matrix elements, is more computationally
efficient to change the direction of ˆq rather than repeat-
ing the calculation of the matrix elements for different
projection of the total angular momentum. Therefore, if
we have n possible multipoles, we select n values for the
angle θ (that is the angle between the ˆz axis and the di-
rection of ˆq) obtaining n linear equations to invert. The
choice of θ is arbitrary: we choose the ones that simplify
as much as possible the solution of the linear equations.
Below we report the solution of the linear equations for
the cases studied in this work. To simplify the notation
we indicate the matrix element computed using Monte
Carlo as
XJ
θ = ⟨J J |jγ,y(q(θ))| J J⟩,
(B1)
and by
M J
L = ⟨J||ML||J⟩,
(B2)
the reduced matrix elements of the magnetic multipole
L among states J.
For nuclei with J = 1/2 and J = 1 only the multi-
pole with L = 1 is allowed. In this case we need only
one equation for which we chose θ = π/2 (ˆq ∥ˆx). The
resultant reduced matrix element for J = 1/2 and J = 1
is
M 1/2,1
1
=
1
√π X1/2,1
π/2
.
(B3)
The situation for the J = 3
2 case is more involved since
both the M1 and M3 multipoles contributes to the mag-
netic f.f. In order to obtain the two magnetic multipoles
we have to compute two matrix elements changing the di-
rection of ˆq. For this case we select θ = π/2 and θ = π/4.
By inverting the linear equations we obtain the magnetic
multipoles as function of the computed matrix elements,
as
M 3/2
1
=
r
2
5π
"
X3/2
π/2 + 2
√
2
3 X3/2
π/4
#
,
(B4)
M 3/2
3
=
8
√
15π
h
X3/2
π/2 −
√
2X3/2
π/4
i
.
(B5)
For the J = 2 case we use the same angle as J = 3/2.
The final result reads
M 2
1 =
3
2
√
5π
"
X2
π/2 + 2
√
2
3 X2
π/4
#
,
(B6)
M 2
3 = 4
√
2
√
15π
h
X2
π/2 −
√
2X2
π/4
i
.
(B7)
For J = 3 three different multipoles with L = 1, 3,
and 5 can be excited. Therefore, we need to have three
independent linear equations that we obtain selecting θ =
π/2, θ = π/4 and cos θ = 2
√
2/3. The solution of the
linear equations reads
M 3
1 =
r
1
7π

53
280
√
2X3
π/2 + 232
735X3
π/4 −
81
1960
√
2X3
1/3

,
(B8)
M 3
3 =
1
√π
"
13
√
2
20 X3
π/2 −32
35X3
π/4 −81
√
2
140 X3
1/3
#
,
(B9)
M 3
5 = 6
r
35
π
"√
2
35 X3
π/2 −32
245X3
π/4 + 27
√
2
245 X3
1/3
#
,
(B10)
where X3
1/3 = ⟨3 3| jγ,y(q(cos θ = 1/3)) |3 3⟩.
