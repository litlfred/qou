---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-006-formulae-for-the-first-terms-in-magnus-expansion
section_title: "Formulae for the first terms in Magnus expansion"
section_number: null
pages: 11-12
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Suppose now that A is of first order in some parameter ¢ and try a solution in the form of a series

Q(t) = > A(t), (40)

n=1

where £2, is supposed to be of order e". Equivalently, we replace A by ¢A in (30) and determine the successive terms of

ES
Q(t) = D> e"2,(0). (41)
n=1
This can be done explicitly, at least for the first terms, by substituting the series (41) in (39) and equating powers of e.
Obviously, the Magnus series (40) is recovered by taking « = 1. Thus, using the notation A(t;) = Aj, the first four orders
read

(1) 2, =A,so that
t
Q(t) -|/ dtyAy. (42)
0

(2) 25 = —$[Q;, A]. Thus

ire t
2Q7(t) = al ar | dt,[Ai, Az]. (43)
0 0

(3) Qs, = —4[Qo, Aj+ SIs, [92,, A]]. After some work, and using the formula

| dx [ fixydy = | dy i] fx, y)dx (44)
0 i) 0 y
162 S. Blanes et al. / Physics Reports 470 (2009) 151-238

we obtain
ifr ty ty
23(t) = al an [ at, [ dts{[A1, [A2, As] + [[A1, Aa], As}. (45)
0 0 0

(4) 24 = — F123, A] + 1122, [21, AN + F121, (22, Al], which yields

ifr th to t3
at) = 4 i ty [ dt, [ dts | dta{{I[Ar, Az]. AslAa]
12 0 0 0 0

+1A1, [[A2, As], Al] + [A1, [A2, [A3, Aal]] + (Aa, (As, [Aa, Ar] ]]}- (46)

The apparent symmetry in the formulae above is deceptive. High orders require repeated use of (44) and become unwieldy.
Prato and Lamberti [49] give explicitly the fifth order using an algorithmic point of view. One can also find in the literature,
quite involved explicit expressions for an arbitrary order [50-54]. In the next subsection we describe a recursive procedure
to generate the terms in the expansion.
