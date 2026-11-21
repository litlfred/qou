---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-015-further-discussion
section_title: "Further discussion"
section_number: null
pages: 19-21
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Theorem 9 provides sufficient conditions for the convergence of the Magnus series based on an estimate by the norm
of the operator A. In particular, it guarantees that the operator 2(t) in Y(t) = exp &2(t) can safely be obtained with the
convergent series Mer y(t) for 0 < t < T when the terms §2;(t) are computed with (51). A natural question at this stage
is — what is the optimal convergence domain? In other words, is the bound estimate r, = 7 given by Theorem 9 sharp or
is there still room for improvement? In order to clarify this issue, we next analyze two simple examples involving 2 x 2
matrices.

Example 1. Moan and Niesen [71] consider the coefficient matrix

A(t) = (5 ‘) (74)
170 S. Blanes et al. / Physics Reports 470 (2009) 151-238

If we introduce, as before, the complex parameter ¢ in the problem, the corresponding exact solution Y(t; ¢) of (70) is given
by

1 1 1
2et 2et —et
e —e —({—+2t]e
Y(t; e) = 9e (+ 3 ) (75)

and therefore

2t t; . t(1 — e* + 3er)
log Y(t; aC se), with g(t: ©) = Sy

The Magnus series can be obtained by computing the Taylor expansion of log Y(t; ¢) around ¢ = 0. Notice that the function
g has a singularity when et = i, and thus, by taking « = 1, the Magnus series only converges up tot = 2m, On the

other hand, condition fo \|A(s)||ds < w leads toT © 1.43205 < an, In consequence, the actual convergence domain of the
Magnus series is larger than the estimate provided by Theorem9. O

Example 2. Let us introduce the matrices

X= (0 a) =o, = (5 0) (76)

and define

—J|BX Ox<t<1
a= [ee t>1

with aw, 6 complex constants. Then, the solution of Eq. (30) at t = 2 is

Y¥(2) = e% fk — (S a)

0 e*
so that

2a
log Y (2) = log(e**1e8%2) = aX, + a X, (77)
— en
an analytic function if |a| < 2 with first singularities at a = iz. Therefore, the Magnus series cannot converge at t = 2 if
|a| > z, independently of 6 4 0, even when it is possible in this case to get a closed-form expression for the general term.
Specifically, a straightforward computation with the recurrence (49)-(50) shows that

3) 3) 2"-1B, 4
So 2p (2) = @X1 + BX. + (1) a "BX. (78)
n=1 n=2 (n— 1)!

If we take the spectral norm, then ||X;|| = ||X2|| = 1 and

t=2
| IAG) Ids = lel +161,
0

so that the convergence domain provided by Theorem 9 is |a| + |8| < 2 for this example. Notice that in the limit |8| > 0
this domain is optimal. O

From the analysis of Examples 1 and 2 we can conclude the following. First, the convergence domain of the Magnus series
provided by Theorem 9 is the best result one can get for a generic bounded operator A(t) in a Hilbert space, in the sense that
one may consider specific matrices A(t), as in Example 2, where the series diverges for any time t such that to \|A(s)||ds > zr.
Second, there are also situations (as in Example 1) where the bound estimate r = zz is still rather conservative: indeed, the
Magnus series converges for a larger time interval than that given by Theorem 9. This is particularly evident if one takes A(t)
as a diagonal matrix: then, the exact solution Y(t; €) of (70) is a diagonal matrix whose elements are non-vanishing entire
functions of ¢, and obviously log Y(t; €) is also an entire function of ¢. In such circumstances, the convergence domain
le| So \|A(s)||ds < a for the Magnus series does not make much sense. Thus, a natural question arises: is it possible to
obtain a more precise criterion of convergence? In trying to answer this question, in [31] an alternative characterization
of the convergence has been developed which is valid for n x n complex matrices. More precisely, a connection has been
established between the convergence of the Magnus series and the existence of multiple eigenvalues of the fundamental
matrix Y(t; €) for a fixed t, which we denote by Y;(¢). By using the theory of analytic matrix functions, and in particular, of
the logarithm of an analytic matrix function (such as is done, e.g. in [76]), the following result has been proved in [31]: if the
analytic matrix function Y;(¢) has an eigenvalue po(€o) of multiplicity ! > 1 for a certain €9 such that: (a) there is a curve in
S. Blanes et al. / Physics Reports 470 (2009) 151-238 171

the e-plane joining ¢ = 0 with e = €p, and (b) the number of equal terms in log p1(€o), log p2(E0), ..., log p)(€o) such that
Pr(Eo) = po, k = 1,..., Lis less than the maximum dimension of the elementary Jordan block corresponding to po, then
the radius of convergence of the series 2;(€) = Mer EK Qe p verifying exp 92;(€) = Y;(e) is precisely r = |eo|. An analysis
along the same line has been carried out in[77].

When this criterion is applied to Example 1, it gives, as the radius of convergence of the Magnus series corresponding to
Eq. (70) for a fixed t,

00
28) = Vek Qe, (79)
k=1
the value
20
r=|e| = —. 80
lel= 3 (80)

To get the actual convergence domain of the usual Magnus expansion we have to take ¢ = 1, and so, from (80), we get
2m /(3t) = 1, or equivalently t = 27/3, i.e., the result achieved from the analysis of the exact solution.
With respect to Example 2, one gets [31]

is
|e| = ———_.
lal(t— 1)
If we now fix ¢ = 1, the actual t-domain of convergence of the Magnus series is
ca
t=14+—.
la|

Observe that, when t = 2, we get |a| = z and thus the previous result is recovered: the Magnus series converges only for
lal <z.

It should also be mentioned that the case of a diagonal matrix A(t) is compatible with this alternative
characterization [31].
