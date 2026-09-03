---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-002-2-a-borodin-a-okounkov-and-g-olshanski
section_title: "A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI"
section_number: 2
pages: 2-4
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
We denote the Plancherel measure on partitions of n by Mn
Mn(λ) = (dim λ)2
n! , |λ| = n ,(1.1)
where dim λ is the dimension of the corresponding representation of
S(n). The asymptotic properties of these measures as n → ∞ have
been studied very intensively, see the References and below .
In the seventies, Logan and Shepp [21] and, independently, V ershik
and Kerov [36, 38] discovered the following measure concent ration phe-
nomenon for Mn as n → ∞ . Let λ be a partition of n and let i and
j be the usual coordinates on the diagrams, namely, the row num ber
and the column number. Introduce new coordinates u and v by
u = j − i
√n , v = i + j√n ,
that is, we ﬂip the diagram, rotate it 135 ◦ as in Figure 1, and scale it
by the factor of n−1/ 2 in both directions.
Figure 1. The limit shape of a typical diagram.
After this scaling, the Plancherel measures Mn converge as n → ∞
(see [21, 36, 38] for precise statements) to the delta measur e supported
on the following shape:
{|u| ≤ 2, |u| ≤ v ≤ Ω( u)} ,
where the function Ω( u) is deﬁned by
Ω( u) =
{
2
π
(
u arcsin(u/2) +
√
4 − u2)
, |u| ≤ 2 ,
|u| , |u| > 2 .
ASYMPTOTICS OF PLANCHEREL MEASURES 3
The function Ω is plotted in Figure 1. As explained in great de tail in
[20], this limit shape Ω is very closely connected to Wigner’ s semicircle
law for distribution of eigenvalues of a random matrices, se e also [17,
18, 19].
From a diﬀerent point of view, the connection with random mat rices
was observed in [2, 3], and also in the earlier papers [14, 25, 26]. In
[2], Baik, Deift, and Johansson made the following conjectu re. They
conjectured that in the n → ∞ limit and after proper scaling the
joint distribution of λi, i = 1 , 2, . . . becomes identical to the joint
distribution of largest eigenvalues of a Gaussian random He rmitian
matrix (which is known to be the so-called Airy ensemble, see Section
1.4). They proved this for the individual distribution of λ1 and λ2 in
[2] and [3], respectively. A combinatorial proof of the full conjecture
was given by one of us in [23]. It was based on an interplay betw een
maps on surfaces and ramiﬁed coverings of the sphere.
In this paper we study the local structure of a typical Planch erel
diagram both in the bulk of the limit shape Ω and on its edge, wh ere
by the study of the edge we mean the study of the behavior of λ1, λ2,
and so on.
We employ an analytic approach based on an exact formula in te rms
of Bessel functions for the correlation functions of the so- called pois-
sonization of the Plancherel measures Mn, see Theorem 1 in the follow-
ing section, and the so-called depoissonization techniques, see Section
1.4.
The exact formula in Theorem 1 is a limit case of a formula from
[6], see also the recent paper [24] for a more general result. The use
of poissonization and depoissonization is very much in the s pirit of
[2, 14, 35] and represents a well known in statistical mechan ics principle
of the equivalence of ensembles.
Our main results are the following two. In the bulk of the limi t
shape Ω, we prove that the local structure of a Plancherel typ ical par-
tition converges to a determinantal point process with the d iscrete sine
kernel, see Theorem 3. This result is parallel to the corresp onding re-
sult for random matrices. On the edge of the limit shape, we gi ve an
analytic proof of the Baik-Deift-Johansson conjecture, se e Theorem 4.
These results will be stated in Subsections 1.3 and 1.4 of the present
Introduction, respectively.
Simultaneously and independently, results equivalent to o ur Theo-
rems 2 and 4 were obtained by K. Johansson [15].
