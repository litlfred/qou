---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-058-variations-on-the-basic-algorithm
section_title: "Variations on the basic algorithm"
section_number: null
pages: 66-67
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The examples collected in Sections 5.5 and 5.7 show that the numerical methods constructed from the Magnus expansion
can be, computationally, very efficient indeed. It is fair to say, however, that this efficiency can be seriously affected when
dealing with certain types of problems.

Suppose, for instance, that one has to numerically integrate a problem defined in SU(n). Although Magnus integrators
are unconditionally stable in this setting (since they preserve unitarity up to round-off, independently of the step size h), in
practice only small values of h are used for achieving accurate results. Otherwise the convergence of the series is not assured.
Of course, the use of small time steps may render the algorithm exceedingly costly.

In other applications, the problem depends on several parameters, so that the integration has to be carried out for
different values of the parameters. In that case, the overall integration procedure can be computationally very expensive.

In view of all these difficulties, it is hardly surprising that several modifications of the standard algorithm of Magnus
integrators had been developed to try to minimize these undesirable effects and get specially adapted integrators for
particular problems.

One basic tool, used time and again in this context, is performing a preliminary linear transformation, similarly to those
introduced in Section 2.9. These transformations can be carried out either for the whole integration interval or at each step
in the process. Given an appropriately chosen transformation, Yo (t), one factorizes Y(t) = Yo(t)Y; (t), where the unknown
Y (t) satisfies the equation

Yj = Bt); (285)

and B(t) depends on A(t) and Yo(t). This transformation makes sense, of course, if ||B(t)|| < ||A(t)|| and thus typically Yo is
chosen in such a way that the norm of B verifies the above inequality. As a consequence, Magnus integrators can be applied
on (285) with larger time steps also providing more accurate results.

Alternatively, for problems where, in addition to the time step h there is another parameter (E, say), one may analyze the
Magnus expansion in terms of h and E. This allows us to identify which terms at each order in the series expansion give the
main contribution to the error, and to design methods which include these terms in their formulation. The resulting schemes
should then provide more accurate results at a moderate computational cost without altering the convergence domain. As
a general rule, it is always desirable to have, in advance, as much information about the equation and the properties of its
solution as possible, and then to try to incorporate all this information into the algorithm.

Let us review some useful possibilities in this context. From (241) one has

A(t) = a9 + ta, 4+ 17a) +---, (286)

where t = t — f1/2. The first term is exactly solvable (4p) = A(ti/2)) and, for many problems, it just provides the main
contribution to the evolution of the system. In that case, it makes sense to take

Yo(t) = ef tn40 = elt—tAltr2)
S. Blanes et al. / Physics Reports 470 (2009) 151-238 217

and subsequently integrate Eq. (285) with
B(t) = e7 Alta) (Aw) — A(ty2)) elf—tnA(tyj2)_

This approach has been considered in [161,162], and shows an extraordinary improvement when the system is highly
oscillatory and the main oscillatory part is integrated with Yo. In those cases, the norm of B(t) is considerably smaller than
\|A(t)||, but B(t) is still highly oscillatory, so that specially adapted quadrature rules have to be used in conjunction with the
Magnus expansion [163,164].

In some other problems, the contributions from the derivatives can also be significant, so that a more appropriate
transformation is defined by

t
Yo(t) = exp (/ (ryan) . (287)
th

The resulting methods can be considered, then, as a combination of the Fer or Wilcox expansions and the Magnus expansion.
This approach has been pursued in [165].

On the other hand, it is known that several physically relevant systems evolve adiabatically or almost-adiabatically. In
that case, it seems appropriate to consider the adiabatic picture which instantaneously diagonalizes A(t) (Section 2.9). This
analysis is carried out in [166-168]. In [167] the adiabatic picture is used perturbatively, whereas in [166] it is shown that
Magnus in the new picture leads to significant improvements.

Alternatively, one can analyze the structure of the leading error terms in order to identify the main contribution to
the error at each 2; in the Magnus series expansion. In most cases, they correspond to terms involving only a and its
nested commutators with a2. Thus, in particular, the standard fourth-order method given by (243) can be easily improved
by including the dominant error term at higher orders, i.e.,

1 1 1
2! = a, — —[a1, —[1q, 1, &1, Az] — ———[Q}q, 4, 4, 1, 4, see
1 pra ta al + Fogle 1,1, 2] 302401 151, 1, 1, &2] +
We recall that using the fourth-order Gauss—Legendre quadrature rule we can take a; = BA, +A), a2 = inf (Az — Ai)
with Aj, A2 given in (252). The new method requires additional commutators but the accuracy can be improved a good deal.
This procedure is analyzed in [70], where it is shown how to sum up all terms of the form [a1, @1,...,@1, @2]. An error
analysis in the limit of very large values of ||q|| is done in [169,170].
