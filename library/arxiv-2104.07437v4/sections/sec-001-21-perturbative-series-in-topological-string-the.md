---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-001-21-perturbative-series-in-topological-string-the
section_title: "Perturbative series in topological string theory"
section_number: 2.1
pages: 5-7
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
---
In this section, X will be a CY threefold, compact or non-compact. We will denote by T =
(T1,··· ,Tr) its complexiﬁed K¨ ahler moduli. In the case of toric CY threefolds, K¨ ahler moduli
can be of two types: “true” moduli, denoted by t, or mass parameters m = (m1,··· ,ms) (see
e.g. [37]). In topological string theory, the basic objects are the genus g free energies Fg(T ),
which can be regarded as generating functions of Gromov–Witten invariants at genus g:
Fg(T ) =
∑
d
Ng,d e−d·T. (2.1)
In this equation, d = (d1,··· ,dr) are non-negative integers representing a two-homology class
(or vector of degrees), and Ng,d is the Gromov–Witten invariant.
From the point of view of the global picture of the moduli space provided by mirror symme-
try, the series (2.1) is an expansion near the large radius point. The moduli space is covered by
overlapping open patches, each of which is parametrised by a diﬀerent set of so-called ﬂat coordi-
nates, related by electromagnetic duality transformations in Sp(2 r, Z), or changes of frames. In
each frame we have diﬀerent genus g free energies, related among themselves by formal Fourier
transforms [38]. In addition, there are preferred choices of frame associated to particular points
in moduli space. We will be interested in particular in the free energies associated to a special
point in the conifold locus of moduli space. When there is a single K¨ ahler parameter, the conifold
locus is a point. In the multi-parameter, toric case, it has been noted in [19] that there exists
a particular point in the conifold locus where its connected components cross transversally. We
will call this point the maximal conifold point, as in [19, 39] 1. There is a special choice of frame
and ﬂat coordinates λ = (λ1,··· ,λr) such that the maximal conifold point is located at
λ = 0. (2.2)
The free energies in this frame will be denoted by Fg(λ), and we will call them conifold free
energies. These free energies are given by the sum of a singular part Fs
g(λ) with a universal
structure [40], and a regular part Fr
g(λ):
Fg(λ) =Fs
g(λ) +Fr
g(λ). (2.3)
The singular part has a pole of order 2 g− 2 at the maximal conifold point, for g ≥ 2, and
logarithmic singularities for g = 0, 1. More precisely, it has the structure
Fs
g(λ) = B2g
2g(2g− 2)
r∑
i=1
λ2−2g
i , g ≥ 2. (2.4)
The regular partFr
g(λ) is of the form
Fr
g(λ) =
∑
ni≥0
cg;n1,···,nrλn1
1 ··· λnr
r , (2.5)
and it is an analytic function at the maximal conifold point. The coeﬃcients cg;n1,···,nr (except
for a ﬁnite number) belong to an algebraic number ﬁeld which depends on the geometry of the
1In the compact case there seem to exist analogues of the maximal conifold point in various examples, but
points where components cross transversally might not be unique.
– 4 –
CY threefold. For example, in the case of local P2 (the canonical bundle of P2), which has a
single modulus, the number ﬁeld is Q[√−3], and we have
Fr
0(λ) =− 3V
4π2λ− π2
9
√
3λ3 + π4
486λ4 + 56π6
10935
√
3λ5− 1058π8
492075λ6 +O(λ7), (2.6)
where
V = 2 Im
(
Li2
(
e
πi
3
))
. (2.7)
The expansion of the free energy around the conifold point is probably one of the less explored
aspects of topological string theory. The large radius expansion (2.1) is well understood and it
can be reformulated in terms of BPS invariants, as ﬁrst noted in [2]. The expansions around
orbifold points also have an algebro-geometric interpretation in terms of orbifold Gromov–Witten
invariants (see e.g. [38]), but as far as we know, there is no direct geometric interpretation of
the coeﬃcients cn1,···,nr appearing in (2.5). The conifold expansion should however play an
important rˆ ole in view of large N dualities between string theory and gauge theory. In these
dualities, string moduli are regarded as ’t Hooft parameters in an underlying gauge theory, and
perturbative gauge theory corresponds to the small radius, or tensionless limit of the string. In
the case of the topological string, large N dualities and the TS/ST correspondence suggest that
the small radius regime corresponds to the conifold locus of moduli space. In addition, we should
regard the conifold ﬂat coordinates as ’t Hooft parameters, 2
λi =−Nigs, (2.8)
where Ni are non-negative integers and gs is the string coupling constant. The perturbative
gauge theory regime corresponds to Ni ﬁxed and gs→ 0, which means that we should consider
the conifold expansion around λ = 0. If we consider the total free energy, summed over all
genera,
F(λ,gs) =
∑
g≥0
Fg(λ)(−gs)2g−2, (2.9)
we conclude that the analogue of a perturbative gauge theory expansion is obtained by setting
(2.8) in (2.4) and (2.5). This produces a series in gs for each choice of the integers N =
(N1,··· ,Nd):
FN(gs) =
∑
g≥0
Fg(−Ngs)(−gs)2g−2. (2.10)
For our purposes, the singular part of the conifold expansion is not relevant, and we will often
consider the partition function, or exponential of the total free energies. This deﬁnes a family of
formal power series in the string coupling constant
ΦN(gs) = exp

∑
g≥0
Fr
g(−Ngs)(−gs)2g−2

. (2.11)
The series (2.11) will be the basic object in this paper. It is the simplest and more natural
formal power series in one variable obtained from topological string theory on a wide class of
CY manifolds. As we have suggested, it corresponds to a perturbative gauge theory expansion
2Note that we choose a slightly unusual convention for gs with an additional minus sign, for reasons explained
in footnote 4.
– 5 –
in a conjectural large N dual gauge theory. In some cases, the large N dual can be identiﬁed
explicitly. For example, if X is the resolved conifold, the large N dual is U(N) Chern–Simons
theory on S3 [41], and the formal power series (2.11) is the perturbative expansion of its partition
function at ﬁxed N.
We should note that, if we know the series ΦN(gs) for allr-tuples of non-negative integersN,
we can reconstruct the power series Fg(λ) for all g≥ 0. Therefore, the collection of asymptotic
series ΦN(gs) contain the all-genus information of perturbative, topological string theory.
Another important motivation to consider the series (2.11) is the TS/ST correspondence
formulated in [18, 19]. This correspondence provides a spectral theory interpretation for Φ N(gs),
as well as a matrix model interpretation [42, 43]. This will be relevant in concrete calculations
of the integer invariants deﬁned in this section.
