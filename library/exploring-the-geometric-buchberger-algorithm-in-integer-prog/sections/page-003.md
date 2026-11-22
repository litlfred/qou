---
doc_id: exploring-the-geometric-buchberger-algorithm-in-integer-prog
doc_title: "Exploring the Geometric Buchberger Algorithm in Integer Programming"
section_id: page-003
section_title: "Page 3"
pages: 3-3
pdf_page: 3
source_pdf: Exploring the Geometric Buchberger Algorithm in Integer Programming.pdf
source_sha256: 73854bc5e3bcffb0
text_source: ocr
granularity: page
doc_brief: "exploring-the-geometric-buchberger-algorithm-in-integer-prog — 8 sections: Page 1; Page 2; Page 3"
---
Exploring the Geometric Buchberger Algorithm in Integer Programming,

Project-and-lift uses the Hermite Normal Form algorithm to com-
pute a lexicographical Grébner basis of the group relaxation for
some o with |o| = rank A, which, by definition, is a Markov basis of
IP, ()- This is the projection step of project-and-lift. Next, it suc-
cessively computes Grébner bases G°\{4} of pti (-) where e; is
the i-th canonical basis vector of R”, obtaining thus a Markov basis
for the group relaxation of the o — {i} variables. We call this process
Md ‘computing a Markov basis of Phe cy (b) from a Markov basis of

A e60) the lift operation of the project -and-lift algorithm. When
cis is empty, IPS 4,c(0) corresponds to the original integer program
and thus we obtain a Markov basis of IP4,(b). Similar truncation
ideas as presented above for Grébner bases apply for Markov bases
and the project-and-lift algorithm. For more details, see [21].

An initial feasible solution for IP4,(b) can be obtained from
project-and-lift with essentially no cost as follows. First, for o with
|o| = rank A, a feasible solution x for the group relaxation Pac (b)
can be obtained via Hermite Normal Form. Next, it can be shown
that applying the augmentation algorithm to improve x by Go\tt

leads to a feasible solution of py

(b). Iteratively applying these
augmentations eventually leads to a feasible solution for IP4,(b).

Even though the project-and-lift algorithm described above is
enough to solve IP4,-(b) together with the Geometric Buchberger
algorithm, the connection to group relaxations can also be used
for early termination. More precisely, the group relaxation satisfies
IPS of) < IP4-(b) for any o, so if x* is optimal for Pr AU) and
feasible for IP4._(b), it is also optimal for IP 4-(b). In ie project-
and-lift algorithm, after computing a Markov basis for IP? ,(b), we
can compute a Grébner basis G? for this group relaxation and use
G to obtain its optimal solution. Then, if this solution is feasi-
ble for the original problem, the algorithm can immediately termi-
nate. Although this requires additional Grébner basis computations,
these calls to the Geometric Buchberger algorithm involve fewer
non-negative variables than the original problem, so they can be
expected to be less costly. Furthermore, [34] shows that the choice
of o can strongly influence how early the group relaxation value
can be optimal. Currently, o is taken as an optimal basis returned
by Simplex algorithm ran on the linear relaxation of IP4-(b).

Another optimization proposed in [21] that is available whenever
some feasible solution z € F is known, is to add the constraint
cx < clzto P. ’A,c(b) since this can help with truncation. It can
be shown that this change can only reduce the size of the Grébner
bases. A slight improvement to this idea is to use any intermediate
Grébner bases obtained in project-and-lift with respect to the <,
order to improve z as much as possible during the execution, thus
tightening the upper bound above and further improving truncation.
In the best case, z is improved to optimality, and it suffices to
prove that the corresponding truncated Grébner basis is empty
to terminate early.

From the description above, we remark that there are at least
three important differences from the application of Grébner bases
to integer programming to the classical general case. First, the poly-
nomials can be represented by exponent vectors, avoiding both
the exponential growth in coefficients and number of terms per
polynomial of the general case. Second, an initial generating set
of I4 is often unknown from the description of IP 4,-(b), so it is

336

ISSAC ’24, July 16-19, 2024, Raleigh, NC, USA

necessary to develop algorithms to compute one. Finally, when one
is interested in solving a single integer program or a small amount
thereof, it may be possible to terminate the Grébner basis compu-
tation early, as only enough elements to guarantee the optimality
of the integer programming solutions are required, instead of the
full Grébner basis.

3 THE BINARY CASE

Many combinatorial optimization problems can be formulated as
integer programs with binary variables. Although the definition of
IP4-(b) does not explicitly allow the use of binary variables, one
can easily work with them by replacing the condition x; € {0, 1}
by a constraint of the form

xji+sj=1 (1)
with x;,s; € Z, where s; is an additional slack variable. In matrix
form, if A is the original constraint matrix involving binary vari-
ables and b is the original right-hand side vector, we need to solve
Par e(b’) with

>_ {A Omxn »_(% ri {e
ar=(i In ) v=(P), “= lon

where I, is the n X n identity matrix, 1, is a vector of n ones and
On; Omxn are respectively the zero vector and matrix of the specified
dimensions.

However, this turns a problem with n binary variables and m
constraints into a new problem with 2n variables and n + m con-
straints, and, as is well known, the size of a Grébner basis is very
sensitive to the number of variables of the problem. While it is pos-
sible to work with these n new slack variables implicitly, as shown
in [35], this does not affect the size of the output Grébner bases
and the amount of operations needed by the Geometric Buchberger
algorithm remains roughly the same, even though some memory is
saved. In this context, it is thus even more critical to use truncated
Grébner bases, as otherwise we allow arbitrary upper bounds for
each binary variable. This can be done even if multiple integer
programs in the family IP4,-(-) must be solved as long as an upper
bound of all the relevant right-hand sides b with respect to < is
available.

Interestingly, many steps of the Geometric Buchberger algorithm
can be specialized to binary variables. We start by showing an
efficient sufficient criterion for truncation in this context that can
be applied along the GCD and cancellation criteria for S-binomial
elimination.

THEOREM 3.1. If G is a partial Grébner basis obtained by the
Geometric Buchberger algorithm and g1, 92 € G, then h = S(g1, 92)
can be b’ -truncated whenever h; ¢ {-1, 0, 1}.

Proor. Suppose that h cannot be truncated, that is, deg 4, h < b’.
By definition, b’ — A’h* € Cyy, the set of feasible right-hand sides
for IP4/,¢’(-). Thus there exists a feasible solution x € Z2” such that
A’ (ht +x) =b.

From the form of A’ and b’, it follows that for all j = n+1,...,2n
(2)

+ + =
hj thin tx +Xj-n=1.
