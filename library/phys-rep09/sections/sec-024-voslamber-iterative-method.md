---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-024-voslamber-iterative-method
section_title: "Voslamber iterative method"
section_number: null
pages: 27-29
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Let us consider Eq. (30) when there is a perturbation parameter ¢ in the (in general, complex) matrix A, i-e., Eq. (105).
Theorem 9 guarantees that, for sufficiently small values of t, Y(t; ¢) = exp 2(t; €), where

A(tre)= vie" Qy(t). (115)
n=1

The advantages of this representation and the approximations obtained when the series is truncated have been sufficiently
recognized in the treatment done in previous sections. There is, however, a property of the exact solution not shared by any
truncation of the series (115) which could be relevant in certain physical applications: (1/¢) a é"92,(t) with m > 1 is
unbounded for ¢ + oo even when {2(t, €)/é is bounded uniformly with respect to ¢ under rather general assumptions on
the matrix A(t) [92]. Notice that this is the case, in particular, for the adiabatic problem (93).
When Schur’s unitary triangularization theorem [44] is applied to the exact solution Y(t; ¢) one has

T, =UtYU, (116)
where T, is an upper triangular matrix and U is unitary. In other words, Y is unitarily equivalent to an upper triangular
matrix T,. Differentiating (116) and using (105), one arrives at

T, = eU'AUT, + [T;, UTU’].

Since the second term on the right hand side is not upper triangular, it follows at once that

T(t) = exp («/ (U'AU),<s) .
0

where the subscript a denotes the upper triangular part (including terms on the main diagonal) of the corresponding matrix.
Taking into account (116) one gets

t
Q(t, e) =U (/ (U'AU).€s) ui. (117)
0
Considering now the Frobenius norm (which is unitarily invariant, Section 1.2) of both sides of this equation, one has

|2llr = lel

t
[ (U'AU) ds
0

C
<|el | I(U*AU) qlleds
F 0

t t
< if |UtAU||eds = ie [ [Alleds. (118)
0 0

If the spectral norm is considered instead, from inequalities (28), (29) and (118), one concludes that

t
|2ll2 < yrank(A) il f [|Allads.
0

In any case, what is important to stress here is that for the exact solution Q(t; ¢)/e is bounded uniformly with respect
to the « parameter. Voslamber proceeds by deriving an algorithm for generating successive approximations of Y(t; ¢) =
exp(2(t; €)) which, contrarily to the direct series expansion (115), preserve this property. His point of departure is to get a
series expansion for the so-called dressed derivative of 2 [93]

Pee? Qe, (119)
178 S. Blanes et al. / Physics Reports 470 (2009) 151-238
This is accomplished by inserting (39) in (119). Specifically, one has

ad
P= e422 Q! = 42/24 expz! (cA) = e422 wie 7 4)
eade —

a

a 20 ogy 2 > BA) sa con

sinh 2/2 par n!
and finally [92,93]
gin 4
r= > =n ad", (eA), (120)

where, as usual, B,, denote Bernoulli numbers. In order to express I” as a power series of ¢ one has to insert the Magnus
series (115) into Eq. (120). Then we get

oo
r&e)=yie"hO, (121)
n=1
where the terms I, can be expressed as a function of 82, with k < n — 2 through the recursive procedure [93]
r=A, Ih =0, (122)
N= : ado,A, n> 3.
Here
2-4
G= 7 B;,
with e241 = 0, cy = —1/24, cy = 7/5760, etc. In particular,
1
T3 = ——[21,[21,A
3 wal 1, [21, A]]

1
= 5g 121, [12, A]] + [22, [21, Al).
Now, from the definition of I”, Eq. (119), we write
OD! =e 8/2 P82,

which, after integration over t, can be used for constructing successive approximations to 2 once the terms J), are known
in terms of 92y, k < n — 2. Thus, the nth approximant 2 is defined by

t
2m = | 222" 9H PM (e372 Ods, n= 1,2,... (123)
0

where the ¢ dependence has been omitted by simplicity and P™ = S“V_, el, 2 = O. The first two approximants
explicitly read

t
2%, 0) =e Qt) = ef A(s)ds
0

C
22 (t, 6) =e f eH 22 GAS) @T LOG) As. (124)
0

In this approach, the solution is approximated by Y(t) ~ exp(2). Observe that 2) contains contributions from an
infinity of orders in e, whereas the nth term in the Magnus series (115) is proportional to e”. Furthermore, 2“ contains
Yen e* 2, and also higher powers ¢” (m > n). In particular, one easily gets

G0 k-1 t
(-)) _
2% e) = EAO+E? WO+Y! TE et f adi ()A(s)ds.
k=3 (k—1)! 0

From the structure of the expression (123) it is also possible to find the asymptotic behavior of 2 /e (n > 3) for ¢ > 00
and prove that it remains bounded [92], just as the exact solution does. This property of the Voslamber iterative algorithm
may lead to better approximations of Y(t) when the parameter ¢ is not very small, since in that case 2“ /e is expected to
remain close to 2/e, as shown in [93].
S. Blanes et al. / Physics Reports 470 (2009) 151-238 179
