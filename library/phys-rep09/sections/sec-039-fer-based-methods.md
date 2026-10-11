---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-039-fer-based-methods
section_title: "Fer based methods"
section_number: null
pages: 56-57
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
To obtain integration methods based on the Fer factorization (260) one applies the Baker–Campbell–Hausdorff (BCH)
formula after equating to the Magnus expansion (259). More specifically, in the domain of convergence of expansions (259)
and (260) we can write
eΩ(h) = eF1(h) eF2(h) · · · ,
S. Blanes et al. / Physics Reports 470 (2009) 151–238
207
where F1 = Ω1 is the first term in the Magnus series, F2 = O(h3) and F3 = O(h7). Then, a p-th order algorithm with
3 ≤p ≤6, based on the Fer expansion requires one to compute F [p]
2
such that
Y(tn + h) = eF1(h) eF[p]
2 (h) Y(tn) + O(hp+1).
(263)
Taking into account that
eΩ[p](h) = eF1(h) eF[p]
2 (h) + O(hp+1),
we have (F1 = Ω1)
eF[p]
2 (h) = e−Ω1(h) eΩ[p](h) + O(hp+1).
Then, by using the BCH formula and simple algebra to remove higher order terms we obtain to order four
F [4]
2
= −
1
12

[α1, α2] −
1
2[α1, α1, α2]

,
(264)
so that two commutators are needed in this case. A sixth-order method can be similarly obtained with four
commutators [40]. These methods are slightly more expensive than their Magnus counterpart, and they do not preserve
the time-symmetry of the exact solution. This can be fixed by the self-adjoint version of the Fer factorization in the form
(261) proposed in [134] and presented in a more efficient way in [40]. The schemes based on (261) up to order six are given
by
Y(tn + h) = eS1(h)eS[p]
2 (h)eS1(h)Yn
(265)
with S1 = Ω1/2. A fourth-order method is given by
S[4]
2 (h) = −
1
12[α1, α2]
(266)
and a sixth-order one by
s1 = [α1, α2]
r1 =
1
120 [α1, −4α3 + 3s1]
S[6]
2 (h) =
1
240
[−20α1 −α3 + s1, α2 + r1] .
(267)
To complete the formulation of the scheme, the αi have to be expressed in terms of the matrices Ai evaluated at the
quadrature points (e.g., Eqs. (257) or (258)).
