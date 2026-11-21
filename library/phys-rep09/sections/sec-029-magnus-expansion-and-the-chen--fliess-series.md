---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-029-magnus-expansion-and-the-chen--fliess-series
section_title: "Magnus expansion and the Chen--Fliess series"
section_number: null
pages: 36-38
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Suppose that f in Eq. (159) has the form f(t, x) = an uj(t)f;(x), ie., we are dealing with the nonlinear differential
equation

XO) = Do ui(t) f(D), x(0) = p, (171)
i=1

where u;(t) are integrable functions of time. Systems of the form (171) appear, for instance, in nonlinear control theory. In
that context, the functions u; are the controls and f; are related to the non-varying geometry of the system. Observe that this
problem constitutes the natural (nonlinear) generalization of the case studied in Section 2.11.

One of the most basic procedures for obtaining x(T) for a given T is by applying simple Picard iteration. For an analytic
output function g : R" —> R, from (153) it is clear that

4 m
GF XO) = Couns) = Vue), gO) =g@), (172)

i=1
S. Blanes et al. / Physics Reports 470 (2009) 151-238 187

where, for simplicity, we have denoted by E; the Lie derivative L¢,. This can be particularized to the case g = xj, the ith
component function.
By rewriting (172) as an equivalent integral equation and iterating we get

tom
8(x(0)) = e+ | Yo ui, (4) (Eng) xe

ij=1

tm tm
= g(p)+ | Yo ui, (4) («ems | ¥ webs 8,e006) 4) dt,
0

ij=1 0 ig=1

tm tm
= g(p) + | uit) (cers | Yo ua (2) (EnEng)@)
0 0

ij=1 in=1

+ il “Yowscorttasierotey) tn) dt, (173)
0

iz=1

and so on. Notice that, in this expression, the time dependence of the solution is separated from the non-varying geometry of
the system, which is contained in the vector fields E; and need to be computed only once, at the beginning of the calculation.
Next, we reverse the names of the integration variables and indices used (e.g., rename i, to become i3 and vice versa), so
that

m t m om t pty
g(x(t)) = gp) + > ( i u(t) ,8)@)+ 0 >> ( i | tn) 2b) (Ei, E,8)()
0 0 0

= ip=1iy=1

m om om

t pts pty
+yoyyr(/ i] i] (a) (add) (E818) += (174)

ig=1 Q=1 i) =1

Observe that the indices in the Lie derivatives and in the integrals are in the opposite order. This procedure can be further
iterated, thus yielding the formal infinite series

t pts ts pty
g(x(t)) = g(x(0)) + > > il il os | | Ui, (ts) © Ui, (tr)dty «= dtsEi, «=~ Fi,g(x(0)), (175)
0 0 0 0

S21 iyevis

where each ij € L = {1,..., m}. An expression of the form (175) is referred to as the Chen-Fliess series, and it can be proved
that, under certain circumstances, it actually converges uniformly to the solution of (172) [90]. This series originates in K.T.
Chen’s work [117] on geometric invariants and iterated integrals of paths in R". Later, Fliess [118] applied the theory to the
analysis of control systems.

One of the great advantages of the Chen-Fliess series is that it can be manipulated with purely algebraic and combinatorial
tools, instead of working directly with nested integrals. To emphasize this aspect, observe that each term in the series can
be identified by a sequence of indices or word w = iyi2 - - - is in the alphabet L through the following two maps:

My: Ww = itis ++is > (¢ > (Evg)(P) = (Ej, Ei, «++ £i,8)(P)) .

t ts b
My: w = ijig- ++ is HO (« be | wit) [ ff Uj, (t)dty +d) .
0 ) )

In fact, the nested integral appearing in the map M2 can be expressed in a simple way, as we did for the linear case in (114)

t ts b
Qi, a= wit) [ ff uj, (ty)dty «+» dt,_1dty. (176)
0 0 0

With this notation, the series of linear differential operators appearing at the right-hand side of (175) can be written in the
compact form [91]

Ye ow Ew, (177)
wel*
where L* denotes the set of words on the alphabet L = {1, 2, ..., m}, the function q,, is given by (176) for each word w € L*

and
Ey =Fi,---E,, ifw=i,---is € L*.

It was proved by Chen that the series (177) is an exponential Lie series [117], i-e., it can be rewritten as the exponential of a
series of vector fields obtained as nested commutators of Ey, ..., Em. Such an expression is referred to in nonlinear control
188 S. Blanes et al. / Physics Reports 470 (2009) 151-238

as the formal analogue of a continuous Baker-Campbell—-Hausdorff formula and also as the logarithm of the Chen-Fliess
series [119].

Notice the similarities of this procedure with the more general treatment carried out in Section 3.4 for the nonlinear
differential equation (150). Thus, expression (164) constitutes the generalization of (175) to an arbitrary function f in (150).
Conversely, the logarithm of the Chen-Fliess series can be viewed as the corresponding nonlinear Magnus series for the
particular nonlinear system (171).

From these considerations, it is clear that, in principle, one can obtain an explicit formula for the terms of the logarithm
of the Chen-Fliess series in a basis of the Lie algebra generated by E,, ... , Em, but this problem has been only recently solved
for any number of operators m and arbitrary order, using labeled rooted trees [91]. Thus, for instance, when m = 2, it holds
that

> OwyEw = exp(BiE + B2E2 + Br2lE1, Eo] + Bri2lE1, [E1, E2)) + Bor2lE2, [E1, F2]]+---), (178)

wel*

where, not surprisingly, the expressions of the coefficients are given by (113) with the corresponding change of sign in
B12 due to the nonlinear character of Eq. (171).

Another relevant consequence of the connection between Magnus series and the Chen-Fliess series is the following: the
Lie series defining the logarithm of the Chen-Fliess series can be obtained explicitly from the recurrence (49)-(50), valid in
principle for the linear case. Of course, the successive terms of the Chen-Fliess series itself can be generated by expanding
the exponential.
