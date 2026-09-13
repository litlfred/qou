---
doc_id: arxiv-math-0108215v1
doc_title: "Möbius Energy of Thick Knots Eric J. Rawdon 2"
section_id: sec-003-3-research-supported-by-nsf-grant-dms9706789
section_title: "Research supported by NSF grant #DMS9706789"
section_number: 3
pages: 1-3
source_pdf: 0108215v1.pdf
source_sha256: 191784d2ccb3415a
doc_brief: "Möbius Energy of Thick Knots Eric J. Rawdon 2 — The M¨ obius energy of a knot is an energy functional for smoot h curves based on an idea of self-repelling."
---
Preprint submitted to Elsevier Preprint 30 October 2018
We and other researchers have deﬁned a number of diﬀerent ener gy functions
for (smooth or polygonal) knots [1–16] based on the idea of inverse -square
repelling energy (so these would correspond to inverse-cube “for ces”). (See
also [17] for a diﬀerent approach). Roughly, these energies are de ﬁned in terms
of integrals over the curve K
∫
x∈K
∫
y∈K
✷
|x − y|2 dx dy .
Here ✷ is a placeholder for any of several kinds of terms that make the inte gral
not give too much weight to the repelling of points that are close to ea ch
other in the sense of arclength along the knot (so the improper inte gral will
converge). The same purpose is accomplished by deﬁning energies a s integrals
of diﬀerences [1,2],
∫
x∈K
∫
y∈K
1
|x − y|2 − 1
|s − t|2 dx dy .
Here s, t lie on a line or circle used for a unit-speed parameterization of the
curve K with s ↦→x and t ↦→y. The energy we study in this paper can be
deﬁned either way [1–3] and we shall use the latter.
In addition to viewing a curve as self-repelling, one also can view it as se lf-
excluding, and deﬁne the ropelength energy EL(K) [4,6,7]: this is the ratio
of the arclength of the curve to the maximum radius of a uniform non self-
intersecting tube along the curve [18], i.e. the ratio of length to radiu s of
the rope (see Section 2 for precise deﬁnitions). Variations on thick ness are
developed in [17,19–25].
We showed in [7] that the normal energy EN (K), which discounts tangential
self-repelling, and the symmetric energy ES(K), which models self-radiation
of a ﬁlament [26], are bounded by the ropelength. These energies, in turn,
dominate the number of crossings in any regular projection of the k not. The
inequalities are of the form shown below in (1). Here acn( K) is the average
crossing number, that is the average, over all spatial directions, of the number
of crossings seen from each direction. This, in turn, is larger than t he crossing
number cr( K), which is the minimum over all regular projections, and cr[ K],
which considers all K in a given knot type.
4π cr[K] ≤ 4π cr(K) < 4π acn(K) ≤ ES(K) ≤ EN (K) ≤ c EL(K)4/ 3 (1)
The coeﬃcient c varies with diﬀerent proofs; the exponent 4 /3 is sharp. A
related idea is the writhe of a knot, wr( K), which is the average over all
spatial directions of the signed crossing numbers. Since wr( K) ≤ acn(K), we
2
get the same bound on 4 π wr(K). But using a diﬀerent analysis of writhe, in
terms of vector ﬁelds ﬂowing in tubes around the knot, it is shown in [2 7] that
wr(K) ≤ 1
4EL(K)4/ 3, which is a lower coeﬃcient than we have for acn( K). The
coeﬃcient, approximately 5, that we obtain in this paper is lower than in [7],
because we do a more subtle analysis. While coeﬃcients might be improv ed,
the exponent 4 /3 in inequality (1) is sharp, because of examples [28,29] where
crossing number grows like the 4 /3 power of ropelength. Similarly, because
M¨ obius energy also bounds crossing number [2], the same examples s how that
the exponent 4 /3 in Theorem 8 of this paper is sharp.
Our main result is that the M¨ obius energy is bounded by the 4 /3 power of the
ropelength (with coeﬃcient ≈ 5). This and the results cited above support our
belief that ropelength is the fundamental measure of knot complex ity: given a
bound on ropelength, one can ﬁnd a bound on any other given knot in variant.
We state the theorem for the version of the energy that equals 4 o n a circle,
EO4(K) =
∫
x∈K
∫
y∈K
1
|x − y|2 − 1
arc(x, y)2 ,
where arc( x, y) denotes the minimum arclength along the curve K between x
and y.
We use one kind of analysis to bound the energy contribution coming f rom
pairs of points ( x, y) where x and y are near each other in arclength along
the knot, and a diﬀerent analysis for pairs where x and y are relatively far
apart. The analysis of proximal pairs will be special for each particu lar energy
function, and yields typically a linear bound on energy in terms of ropelength.
The analysis of distal pairs is identical for the various energy funct ions: with
little work, we can get a bound on energy that is quadratic in ropelength; and
with more work, we obtain a bound that is 4 /3 power in the ropelength. We
add the proximal and distal contributions to get the overall bound .
In a recent book [30], many ideas of energy and thickness for knots are dis-
cussed. Many of us interested in such ideas thought that knots sh ould have
“ideal” forms. It has turned out that the knot conformations tha t minimize the
various ideas of energy diﬀer from one another. The similarities and d iﬀerences
are equally provocative.
