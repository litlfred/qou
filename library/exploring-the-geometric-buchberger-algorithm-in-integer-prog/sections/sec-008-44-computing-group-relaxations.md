---
doc_id: exploring-the-geometric-buchberger-algorithm-in-integer-prog
doc_title: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br"
section_id: sec-008-44-computing-group-relaxations
section_title: "Computing group relaxations"
section_number: 4.4
pages: 6-7
source_pdf: Exploring the Geometric Buchberger Algorithm in Integer Programming.pdf
source_sha256: 73854bc5e3bcffb0
doc_brief: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br — The Geometric Buchberger algorithm is a specialization of the clas- sical"
---
A potential use of the Geometric Buchberger algorithm when com-
bined with project-and-lift is the computation of group relaxations
of integer programs, since branch-and-bound algorithms tend to
be slower to solve group relaxations than the original, non-relaxed
problems [9]. As described in Section 2, it is sufficient to run the
Geometric Buchberger algorithm only once to obtain the value of a
group relaxation and the optimal solution to this relaxed problem.
In addition to allowing for early termination, this group relaxation
value could potentially be used inside other integer programming
methods, such as the branch-and-bound algorithm, to strengthen
dual bounds that are usually obtained via linear programming re-
laxation.

Table 4 shows the linear programming relaxation values (LP),
the group relaxation values (GR) and the corresponding relative
deviation
LP—-GR
oR (3)
for some binary knapsacks. In all cases, GR gives a strictly tighter
bound on the cost of the optimal solution than LP.

Furthermore, for all of these instances, the group relaxation was
optimal, since no lift operations were necessary for project-and-lift
to prove optimality. Surprisingly, this happened even for the binary
knapsacks with n = 30 variables, which have moderately large

rd(LP,GR) = 100
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
