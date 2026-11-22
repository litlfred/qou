---
doc_id: exploring-the-geometric-buchberger-algorithm-in-integer-prog
doc_title: "Exploring the Geometric Buchberger Algorithm in Integer Programming"
section_id: page-006
section_title: "Page 6"
pages: 6-6
pdf_page: 6
source_pdf: Exploring the Geometric Buchberger Algorithm in Integer Programming.pdf
source_sha256: 73854bc5e3bcffb0
text_source: ocr
granularity: page
doc_brief: "exploring-the-geometric-buchberger-algorithm-in-integer-prog — 8 sections: Page 1; Page 2; Page 3"
---
ISSAC 24, July 16-19, 2024, Raleigh, NC, USA

Problem n m_  t(%) mem(%) #Rs (%)
0-1KP 5 1 75.69 99.08 77.25,
0-1KP 10 1 56.75 85.80 72.36
0-1KP 20 1 83.10 72.74 72.37
0-1KP 30 1 77.78 67.56 68.98
0-1KP 40 1 85.75 68.44 69.23
0-1KP 50 1 94.14 74.98 75.50
0-1MDKP 10 2 60.69 81.09 60.72
0-1MDKP 10 3 56.36 66.33 49.80
0-1MDKP 10. 4 52.75 67.08 49.27
0-1MDKP 10 5 54.52 54.65 42.78
0-1MDKP 15 2 66.92 55.53 51.68
0-1MDKP 15 3 59.36 46.67 45.24
0-1MDKP 15 4 58.84 39.90 37.33
0-1MDKP 15 5 51.36 31.56 28.88
0-1MDKP 20 2 69.96 55.33 55.95
0-IMDKP 20 3. 52.20 38.37 37.69
0-IMDKP 20 4 = 55.72 32.74 31.74
0-1MDKP 20 5 60.29 27.00 25.53
0-1MDKP 25 2 67.94 54.16 54.18
0-1MDKP 25 3 66.46 41.61 40.88
SCP 30 15 17.93 17.22 7.58
SCP 30 16 19.51 22.02 9.85
SCP 30 17 30.06 12.43 4.77
SCP 30 18 37.28 12.68 5.92
SCP 30 19 28.58 13.30 8.99
SPP 100 25 50.28 59.52 28.42
SPP 100 30 47.34 46.88 21.45
SPP 100 35 77.44 35.22 24.34

Table 2: Percentage of time (t), memory (mem) and number
of reductions (#Rs) of IPGBs with the binary truncation cri-
terion in relation to the same data obtained by IPGBs-NC
(no-criterion).

criteria. Even so, the use of this criterion leads to speedups of about
100% to 500%.

4.3 IPGBs performance

The results of Table 1 show that, in spite of being a work in progress,
the current version of IPGBs already has comparable performance
to 4ti2 even without the binary truncation criterion. In fact, IPGBs
achieves shorter running times than 4ti2 in nearly all binary in-
stance families tested, with the exception of some set cover prob-
lems. Similar results are also shown in Table 3, which includes only
problems with no binary variables.

The results from the single-constraint knapsacks when compared
to their multiknapsack variants in Tables 1 and 3 show that for both
integer and binary variables, adding even a single constraint to
the integer program makes the corresponding Grébner bases much
larger and, thus, the problem becomes much more difficult with a
naive application of the Geometric Buchberger algorithm. It follows
that in order to solve even moderately sized integer programs it is
necessary to use the early termination techniques of project-and-lift
described in Section 2.

339

Langeloh

Problem n |G| t(IPGBs, ins)  t (4ti2, in s)
UKP. 50 80.80 0.00 0.02
UKP. 60 88.50 0.00 0.03
UKP 70 107.80 0.00 0.03
UKP 80 115.50 0.01 0.05
UKP 90 121.00 0.00 0.06
UKP. 100 135.40 0.01 0.05

MDKP 50 7434.40 17.10 19.95
MDKP 60 6772.20 13.16 16.03
MDKP 70 10275.50 31.85 38.44
MDKP 80 16200.10 85.94 96.01
MDKP 90 15766.40 79.36 95.63
MDKP 100 14885.70 80.21 98.91

Table 3: Grébner basis size and computation times for
IPGBs.jl and 4ti2 over knapsacks and multiknapsacks con-
taining only integer variables. All results are the averages
over 10 random instances generated for each value of n.

On the other hand, we observe that the UKP and MDKP instances
whose results are shown in Table 3 correspond to integer programs
that appear in the exact solution of multiobjective problems, as in
[12]. In this application, the Grébner basis computation time domi-
nates the overall running time, so the values given in Table 3 are a
good approximation of the solution time of this type of multiobjec-
tive problem. Furthermore, branch-and-bound algorithms tend to
be much slower for these multiobjective problems, showing that
there are cases where full truncated Grébner basis computations
are worthwhile.

4.4 Computing group relaxations

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
