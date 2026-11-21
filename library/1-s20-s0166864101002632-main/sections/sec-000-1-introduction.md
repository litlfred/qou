---
doc_id: 1-s20-s0166864101002632-main
doc_title: "PII: S0166-8641(01)00263-2"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1-s2.0-S0166864101002632-main.pdf
source_sha256: bc5aa8a7663b2a9f
toc_source: inferred
doc_brief: "PII: S0166-8641(01)00263-2 — The Möbius energy of a knot is an energy functional for smooth curves based on an idea of self- repelling."
---
In this paper, we exhibit a bound for the Möbius energy of a knot, in terms of the amount
of “rope” needed to make the knot. This is the energy introduced in [25] and studied
extensively in [15,18]. We follow an overall approach suggested by G. Buck for showing
that any inverse-square knot energy should be bounded by the 4/3 power of the ropelength.
We and other researchers have deﬁned a number of different energy functions for
(smooth or polygonal) knots [3–6,11,15,16,18,22,25–28,32–34] based on the idea of
inverse-square repelling energy (so these would correspond to inverse-cube “forces”). (See
also [24] for a different approach.) Roughly, these energies are deﬁned in terms of integrals
over the curve K

x∈K

y∈K
✷
|x −y|2 dx dy.
Here ✷is a placeholder for any of several kinds of terms that make the integral not give too
much weight to the repelling of points that are close to each other in the sense of arclength
* Corresponding author. Research supported by NSF grant #DMS9706789.
E-mail addresses: rawdon@mathcs.duq.edu (E.J. Rawdon), jsimon@math.uiowa.edu (J. Simon).
1 Research supported by Chatham College, the University of Iowa, and NSF grant #DMS0074315.
0166-8641/01/$ – see front matter 2001 Elsevier Science B.V. All rights reserved.
PII: S0166-8641(01)00263-2
98
E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
along the knot (so the improper integral will converge). The same purpose is accomplished
by deﬁning energies as integrals of differences [15,25],

x∈K

y∈K
1
|x −y|2 −
1
|s −t|2 dx dy.
Here s,t lie on a line or circle used for a unit-speed parameterization of the curve K with
s →x and t →y. The energy we study in this paper can be deﬁned either way [15,18,25]
and we shall use the latter.
In addition to viewing a curve as self-repelling, one also can view it as self-excluding,
and deﬁne the ropelength energy EL(K) [3,5,6]: this is the ratio of the arclength of the
curve to the maximum radius of a uniform non self-intersecting tube along the curve [21],
i.e., the ratio of length to radius of the rope (see Section 2 for precise deﬁnitions). Variations
on thickness are developed in [12–14,17,19,24,29,30].
We showed in [6] that the normal energy EN(K), which discounts tangential self-
repelling, and the symmetric energy ES(K), which models self-radiation of a ﬁlament [1],
are bounded by the ropelength. These energies, in turn, dominate the number of crossings
in any regular projection of the knot. The inequalities are of the form shown below in (1).
Here acn(K) is the average crossing number, that is the average, over all spatial directions,
of the number of crossings seen from each direction. This, in turn, is larger than the
crossing number cr(K), which is the minimum over all regular projections, and cr[K],
which considers all K in a given knot type.
4π cr[K] ⩽4π cr(K) < 4π acn(K) ⩽ES(K) ⩽EN(K) ⩽cEL(K)4/3.
(1)
The coefﬁcient c varies with different proofs; the exponent 4/3 is sharp. A related idea
is the writhe of a knot, wr(K), which is the average over all spatial directions of the signed
crossing numbers. Since wr(K) ⩽acn(K), we get the same bound on 4π wr(K). But using
a different analysis of writhe, in terms of vector ﬁelds ﬂowing in tubes around the knot, it
is shown in [7] that wr(K) ⩽1
4EL(K)4/3, which is a lower coefﬁcient than we have for
acn(K). The coefﬁcient, approximately 5, that we obtain in this paper is lower than in [6],
because we do a more subtle analysis. While coefﬁcients might be improved, the exponent
4/3 in inequality (1) is sharp, because of examples [2,8] where crossing number grows
like the 4/3 power of ropelength. Similarly, because Möbius energy also bounds crossing
number [15], the same examples show that the exponent 4/3 in Theorem 3 of this paper is
sharp.
Our main result is that the Möbius energy is bounded by the 4/3 power of the ropelength
(with coefﬁcient ≈5). This and the results cited above support our belief that ropelength
is the fundamental measure of knot complexity: given a bound on ropelength, one can ﬁnd
a bound on any other given knot invariant.
We state the theorem for the version of the energy that equals 4 on a circle,
EO4(K) =

x∈K

y∈K
1
|x −y|2 −
1
arc(x,y)2,
where arc(x,y) denotes the minimum arclength along the curve K between x and y.
E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
99
We use one kind of analysis to bound the energy contribution coming from pairs of
points (x,y) where x and y are near each other in arclength along the knot, and a different
analysis for pairs where x and y are relatively far apart. The analysis of proximal pairs
will be special for each particular energy function, and yields typically a linear bound on
energy in terms of ropelength. The analysis of distal pairs is identical for the various energy
functions: with little work, we can get a bound on energy that is quadratic in ropelength;
and with more work, we obtain a bound that is 4/3 power in the ropelength. We add the
proximal and distal contributions to get the overall bound.
In a recent book [36], many ideas of energy and thickness for knots are discussed. Many
of us interested in such ideas thought that knots should have “ideal” forms. It has turned
out that the knot conformations that minimize the various ideas of energy differ from one
another. The similarities and differences are equally provocative.
