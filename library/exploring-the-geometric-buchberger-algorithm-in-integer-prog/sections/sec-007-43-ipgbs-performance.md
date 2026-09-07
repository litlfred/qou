---
doc_id: exploring-the-geometric-buchberger-algorithm-in-integer-prog
doc_title: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br"
section_id: sec-007-43-ipgbs-performance
section_title: "IPGBs performance"
section_number: 4.3
pages: 6-6
source_pdf: Exploring the Geometric Buchberger Algorithm in Integer Programming.pdf
source_sha256: 73854bc5e3bcffb0
doc_brief: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br — The Geometric Buchberger algorithm is a specialization of the clas- sical"
---
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
