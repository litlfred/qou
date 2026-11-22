---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-055-splitting-methods
section_title: "Splitting methods"
section_number: null
pages: 63-64
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Frequently, one has to exponentiate a matrix which can be split into several parts which are either solvable or easy to
deal with. Let us assume for simplicity that C = A+ B, where the computation e‘ is very expensive, but e“ and e® are cheap
and easy to evaluate. In such circumstances, it makes sense to approximate e®¢ with ¢, a small parameter, by the following
scheme:

ye = etbmBgeamA .., gebiByraA —_ g&(A+8) 4 @(gPt1) (279)

with appropriate parameters aj, bj. This can be seen as the approximations to the solution at t = e of the equation
Y’ = (A+ B)Y by a composition of the exact solutions of the equations Y’ = AY and Y’ = BY at timest = aje and
t = bje, respectively. Two instances of this kind of approximation are given by the well known Lie-Trotter formula

whl! = ee (280)
and the second order symmetric composition
ye = @A/2 928 QeA/2 (281)

referred to as Strang splitting, Stormer, Verlet and leap-frog, depending on the particular area where it is used.

Splitting methods have been considered in different contexts: in designing symplectic integrators, for constructing
volume-preserving algorithms, in the numerical integration of partial differential equations etc. An extensive survey of the
theory and practice of splitting methods can be found in [154,79,127-129] and references therein.

Splitting methods are particularly useful in geometric numerical integration. Suppose that the matrix C = A+ B resides
in a Lie algebra g. Then, obviously, exp(C) belongs to the corresponding Lie group , and one is naturally interested in also
getting approximations in g. In this respect, notice that if A, B € g, then the scheme (279) also provides an approximation
in g. It is worth noticing that other methods for the approximation of the matrix exponential (e.g., Padé approximants and
Krylov subspace techniques) are not guaranteed to map elements from g to ¢. Although diagonal Padé approximants map
the Lie algebra o, to the underlying group, it is possible to show that the only analytic function that maps sl(n) into the
special linear group SL(n) approximating the exponential function up to a given order, is the exponential itself [155]. In
consequence, diagonal Padé approximants only provide results in SL(n) if the computation is accurate to machine precision.
214 S. Blanes et al. / Physics Reports 470 (2009) 151-238

In [156], Celledoni and Iserles devised a splitting technique for obtaining an approximation to exp(C) in the Lie group 9
based on a decomposition of C € g into low-rank matrices C; € g. Basically, given an x n matrix C € g, they proposed to
split it in the form

k
C= > G,
i=1

such that

(1) G €g,fori=1,...,k.
(2) Each exp(C;) is easy to evaluate exactly.
(3) Products of such exponentials are computationally cheap.

For instance, for the Lie algebra so(n), the choice

1 .T 1 T ;
Gi= Scie; — 5eibi i=1,...,n,

where cj, ..., Cn are the columns of C and e; is the i-th vector of the canonical basis of R", satisfies the above requirements
(with k = n), whereas in the case of g = sI(n) other (more involved) alternatives are possible [156].
Proceeding as in (280), with

yl = exp(eCy) exp(eQ) -- - exp(eC.)
we get an order one approximation in ¢ to exp(€C), whereas the symmetric composition

yl = erika zeCk-1 os ere e378 bee e28Ck-1936Ck (282)
provides an approximation of order two in ¢, and this can be subsequently combined with different techniques for increasing
the order.

With respect to the computational cost, the results reported in [156] show that, up to order four in ¢, this class of
splitting schemes is competitive with the Matlab built-in function expm when machine accuracy is not required in the final
approximation. Running expm on randomly generated matrices, it is possible to verify that computing exp(C) to machine
accuracy requires about (20-30)n? floating point operations, depending on the eigenvalues of C, whereas the 4th-order
method constructed from (282) involves (12-15)n? operations when C € so0(100) [156]. In the case of the approximation
of exp(C)v and v € R", the cost of low-rank splitting methods drop down to Kn?, where K is a constant, and thus they are
comparable to those achieved by polynomial approximants [153].

Splitting methods of the above type are by no means the only way to express exp(C) as a product of exponentials of
elements in g. For instance, the Wei-Norman approach (111) can also be implemented in this setting. Suppose that dim g = s
and let {X;, X2,..., X;} be a basis of g. In that case, as we have seen (Section 2.10.3), it is possible to represent exp(tC) for
C € gand sufficiently small |t| in canonical coordinates of the second kind,

eS — p81 (OX1 Q2(OX2 , . , es (t)Xs

where the scalar functions g, are analytic at t = 0. Although the g;s are implicitly defined, they can be approximated by
Taylor series. The cost of the procedure can be greatly reduced by adequately choosing the basis and exploiting the Lie-
algebraic structure [157].

Yet another procedure to get approximations of exp(C) in a Lie-algebraic setting, which has received considerable
attention during the last years, is based on generalized polar decompositions (GPD), an approach introduced in [158] and
further elaborated in [159,160]. In particular, in [159], by bringing together GPD with techniques from numerical linear
algebra, new algorithms are presented with complexity @(n?), both when the exponential is applied to a vector and to
a matrix. This is certainly not competitive with Krylov subspace methods in the first case, but represents at least a 50%
improvement on the execution time, depending on the Lie algebra considered, in the latter. Another difference with respect
to Krylov methods is that the algorithms based on generalized polar decompositions approximate the exponential to a given
order of accuracy and, thus, they are well suited to exponential approximations within numerical integrators for ODEs,
since the error is subsumed in that of the integration method. For a complete description of the procedure and its practical
implementation, we refer the reader to [159].
