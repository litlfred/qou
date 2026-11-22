---
doc_id: exploring-the-geometric-buchberger-algorithm-in-integer-prog
doc_title: "Exploring the Geometric Buchberger Algorithm in Integer Programming"
section_id: page-007
section_title: "Page 7"
pages: 7-7
pdf_page: 7
source_pdf: Exploring the Geometric Buchberger Algorithm in Integer Programming.pdf
source_sha256: 73854bc5e3bcffb0
text_source: ocr
granularity: page
doc_brief: "exploring-the-geometric-buchberger-algorithm-in-integer-prog — 8 sections: Page 1; Page 2; Page 3"
---
Exploring the Geometric Buchberger Algorithm in Integer Programming,

n LP GR rd(%) #Lifts
5 1812.60 1707.25 6.07 0.00
10 3710.53 3549.40 4.29 0.00
20 7919.06 7844.80 0.94 0.00
30 11517.17 11415.20 0.88 0.00

Table 4: Average linear relaxation value (LP), group relax-
ation value (GR), relative deviation between LP and GR (Equa-
tion (3)) and number of lift operations to optimal solution
computed by IPGBs.jl’s project-and-lift implementation over
the same small binary knapsacks presented in Table 1.

Grébner bases according to Table 1. This indicates that project-and-
lift early termination via group relaxations can be quite effective at
finding optimal solutions of integer programs. However, a greater
variety of tests with instances of larger sizes is necessary to deter-
mine how often the group relaxation will be optimal and how many
lift operations are usually necessary to solve integer programs in
terms of n.

To our knowledge, the only previous work that compares LP
and GR values empirically is [9]. Our results are consistent with
this previous work from the perspective that the relative deviation
tends to be small when only binary variables are present in the
integer program. It is important to note, however, that part of the
reason for the small relative deviation in our results is that the linear
relaxation is a reasonably good relative bound for these instances
and that the group relaxation is already optimal for them.

5 CONCLUSION

In this paper, we introduced a new efficient criterion for trunca-
tion of Grébner basis elements for integer programs with binary
variables. We have also introduced a new Grébner basis implemen-
tation of an integer programming solver with the package IPGBs.jl,
which we have empirically shown to be more efficient than the
previous state-of-the-art, specially in cases where our new binary
truncation criterion applies.

Even so, our experiments have shown that pure Grébner ba-
sis methods have difficulty solving even moderately sized integer
programs in reasonable time. We believe that, for the majority of
integer programming applications, this is inevitable, but that it is
still possible to both improve these Grébner basis methods and
to integrate them with classical integer programming algorithms
profitably. Moreover, current applications in integer programming
with non-linear constraints [10] and multiobjective integer pro-
gramming [12] are already able to profit from the improvements to
Grébner basis computations available in IPGBs.

Further improvements to the Geometric Buchberger algorithm
may be possible by adapting other ideas developed in the context
of Grébner bases of arbitrary ideals to the particular case of toric
ideals, such as the use of sparse linear algebra for reduction [7] and
signature algorithms [6, 8]. However, such specializations are not
guaranteed to lead to good empirical results, since reductions and
useless S-polynomial elimination are already much more efficient
in the toric case.

340

ISSAC ’24, July 16-19, 2024, Raleigh, NC, USA

In order to expand the applicability of Grébner basis techniques
to a wider variety of optimization problems, it would be interesting
to be able to work with mixed integer programming, containing
both real and integer variables. A step in this direction was given in
[13], where finite representations of Graver bases for mixed integer
programs were defined. Other open questions include potential uses
of partial Grébner bases as primal heuristics in branch-and-bound
algorithms and as generic neighborhoods in local search meta-
heuristics, as well as using group relaxations as a way to tighten
dual bounds in branch-and-bound. We consider that using Grébner
bases in such a hybrid fashion with classical integer programming
methods is the most likely path to the usefulness of Grébner bases
in general-purpose integer programming.

ACKNOWLEDGMENTS

The author would like to thank Marcus Ritt for the productive
discussions about this work. The author would also like to thank the
anonymous referees for their valuable comments and suggestions.

This work was partially financed by the Coordenacao de Aper-
feigoamento de Pessoal de Nivel Superior - Brasil (CAPES) Finance
Code 001.

REFERENCES

[1] 4ti2 team. 2006. 4ti2 — A Software Package for Algebraic, Geometric and Combi-
natorial Problems on Linear Spaces.

[2] Victor Blanco and Justo Puerto. 2009. Partial Grébner Bases for Multiobjective
Integer Linear Optimization. SIAM Journal on Discrete Mathematics 23, 2 (Jan.
2009), 571-595. https://doi.org/10.1137/070698051

[3] Diego Cifuentes and Shmuel Onn. 2019. On the Complexity of Toric Ideals.
arXiv:1902.01484 [cs, math]

[4] Pasqualina Conti and Carlo Traverso. 1991. Buchberger Algorithm and Integer
Programming. In Applied Algebra, Algebraic Algorithms and Error-Correcting
Codes.

[5] Jestis A. De Loera, Raymond Hemmecke, and Matthias Képpe. 2012. Algebraic
and Geometric Ideas in the Theory of Discrete Optimization. Society for Industrial
and Applied Mathematics.

[6] Christian Eder and Jean-Charles Faugére. 2017. A Survey on Signature-Based
Algorithms for Computing Grébner Bases. Journal of Symbolic Computation 80
(May 2017), 719-784. https://doi.org/10.1016/j.jsc.2016.07.031

[7] Jean Charles Faugére. 1999. A New Efficient Algorithm for Computing Grébner
Bases (F4). Journal of Pure and Applied Algebra 139, 1 (June 1999), 61-88. https:
//doi.org/10.1016/S0022-4049(99)00005-5

[8] Jean Charles Faugére. 2002. A New Efficient Algorithm for Computing Grébner

Bases without Reduction to Zero (F5). In Proceedings of the 2002 International

Symposium on Symbolic and Algebraic Computation (ISSAC ’02). Association for

Computing Machinery, New York, NY, USA, 75-83. https://doi.org/10.1145/

780506.780516

Matteo Fischetti and Michele Monaci. 2008. How Tight Is the Corner Relaxation?

Discrete Optimization 5, 2 (May 2008), 262-269. https://doi.org/10.1016/j.disopt.

2006.11.010

J. Gago, I. Hartillo, J. Puerto, and J. M. Ucha. 2013. Exact Cost Minimization of

a Series-Parallel Reliable System with Multiple Component Choices Using an

Algebraic Method. Computers & Operations Research 40, 11 (Nov. 2013), 2752-2759.

https://doi.org/10.1016/j.cor.2013.05.019

J. Gago-Vargas, I. Hartillo, J. Puerto, and J. M. Ucha. 2015. An Improved Test

Set Approach to Nonlinear Integer Problems with Applications to Engineering

Design. Computational Optimization and Applications 62, 2 (Nov. 2015), 565-588.

https://doi.org/10.1007/s10589-015-9739-3

Maria Isabel Hartillo-Hermoso, Haydee Jiménez-Tafur, and José Maria Ucha-

Enriquez. 2020. An Exact Algebraic €-Constraint Method for Bi-Objective Linear

Integer Programming Based on Test Sets. European Journal of Operational Re-

search 282, 2 (April 2020), 453-463. https://doi.org/10.1016/j.ejor.2019.09.032

Martin Henk, Matthias Képpe, and Robert Weismantel. 2003. Integral Decompo-

sition of Polyhedra and Some applications in Mixed Integer Programming. Math-

ematical Programming 94, 2 (Jan. 2003), 193-206. https://doi.org/10.1007/s10107-

002-0315-0

Serkan Hosten and Bernd Sturmfels. 1995. GRIN: An Implementation of Gréb-

ner Bases for Integer Programming. In Integer Programming and Combinatorial

Optimization.

S

fio

ieee

[12)

[13

[14
