---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-048-fer-based-methods
section_title: "Fer based methods"
section_number: null
pages: 56-57
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
To obtain integration methods based on the Fer factorization (260) one applies the Baker-Campbell-Hausdorff (BCH)
formula after equating to the Magnus expansion (259). More specifically, in the domain of convergence of expansions (259)
and (260) we can write

2) = gFill) oa) |.
S. Blanes et al. / Physics Reports 470 (2009) 151-238 207

where F; = , is the first term in the Magnus series, F; = O(h*) and F; = O(h’). Then, a p-th order algorithm with
3 < p <6, based on the Fer expansion requires one to compute Fpl such that

Y (ty +h) = ef @2" y(¢,) + OchPt), (263)
Taking into account that

er") — eri ef) +0(ht),
we have (F; = 21)

FO — gilt) Q2HPliy och),

Then, by using the BCH formula and simple algebra to remove higher order terms we obtain to order four

1 1
oe 1, 2] — —[11, 4, a: ; 264
2 Tp (lor a2 glen, a1, a2] (264)
so that two commutators are needed in this case. A sixth-order method can be similarly obtained with four
commutators [40]. These methods are slightly more expensive than their Magnus counterpart, and they do not preserve
the time-symmetry of the exact solution. This can be fixed by the self-adjoint version of the Fer factorization in the form
(261) proposed in [134] and presented in a more efficient way in [40]. The schemes based on (261) up to order six are given
by

V(t) +h) = eS" 952M pSiy, (265)
with S$; = 92,/2. A fourth-order method is given by

14] 1
Sy (h) = pyle a] (266)

and a sixth-order one by

$1 = [a1, a2]

1
ry) = — [a1, —4a3 + 3s
1 a0 | 1 3 + 351]
1

sh) = —~ [-200; — 03 +51, «2 +r]. 267

3 (h) aa | 1 3+51, +1] (267)
To complete the formulation of the scheme, the a; have to be expressed in terms of the matrices Aj evaluated at the
quadrature points (e.g., Eqs. (257) or (258)).
