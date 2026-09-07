---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE"
section_id: sec-010-9-errata-listing
section_title: "Errata listing"
section_number: 9
pages: 35-38
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
doc_brief: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
The abridged version of the Kepler conjecture in the Annals [11] was gener-
ated by the same tex files as the unabridged version in [22]. For this reason,
it seems that every correction to the abridged version should also be a cor-
rection to the unabridged version. We list errata in the unabridged version.
The same list applies to corresponding passages in the abridged version.
Each correction gives its location in [22]. The location𝓁+n counts down
from the top of the page, or if a section or lemma number is provided, it
counts from the top of that organizational unit. The location𝓁-n counts
up from the bottom of the page. Footnotes are not included in the count
from the bottom. Every line containing text of any sort is included in the
count, including displayed equations, section headings, and so forth. The
material to the left of↝ indicates original text, and material to the right
of the arrow gives replacement text. The original text and replacement text
appear in italic. Comments about the corrections appear in roman.
In addition to the corrections to the text mentioned below, there have been
some corrections to the computer code, including some typos in the listings
of nonlinear inequalities. They are described in detail in [8].
9.1. Listing.
[p.47,Lemma 5.16]Q↝ F
[p.49,𝓁+2] supposed↝suppose
[p.63,Lemma 7.10]S-system ↝Q-system
[p.75,Remark 8.11]show↝shows
[p.78,𝓁-7] constraints↝constraint
[p.86,𝓁+14] Let{0,v} be the diagonal of an upright quarter in theQ0 ↝Let v be
a vertex with 2t0 <|v| <
√
8. Section 9 assumes that the diagonal belongs to a
quarter in theQ-system, but Lemma 10.14 uses these results when{0,v} has 0 or
1 anchors. To make this coherent, we should assume throughout Section 9 that we
have the weaker condition that whenever{0,v} has two or more anchors, it is a
diagonal of a quarter in theQ-system. The proofs of Section 9 all go through in
this context. (Lemma 9.7 is all that is relevant here.)
[p.87,Definition 9.3] In definition of∆(v,W e), we can have someQ (as in Fig 9.1)
with negative orientation. In this case,Ev∩Ei can clip the other side. We want the
object without clipping. ∆(v,W e) should be understood as the unclipped object.
36 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
[p.88,Definition 9.6] The definition is poorly worded. First of all, it requires that
the subscript to ϵ to be a vertex, but then in the displayed equation, it makes
w/2 the subscript, which is not a vertex. To defineϵ′, move fromw/2 along the
ray throughx′ until an edge of the Voronoi cell is encountered. Ifv,w,u are the
three vertices defining that edge, then setϵ′
v(Λ,x ) = u. Degenerate cases, such as
when two different edges are encountered at the same time, can be resolved in any
consistent fashion. In [19], these degeneracies are avoided altogether, by replacing
functions ϵ,ϵ′ with sets Φ, Φ′.
[p.88,Lemma 9.7,𝓁+2] w and v↝w and u
[p.88,L. 9.7,Claim 1]with |w−w′|≤ 2t0, and ↝ with
[p.88,L. 9.7,𝓁+5] Then: ↝ Let R′
w ={x∈ Rw∩ (0,{u,w})| ϵ0(x,{u,w}) = u}.
Assume thatR′
w is not empty. Then:
[p88,L. 9.7,Claim 3]Rw ↝ R′
w
[p.89,𝓁+2]{w,v}↝{w,u}
[p.92,𝓁+16,𝓁+21] maxjuj ↝ maxj|uj|
[p.93,𝓁-4] obstructed fromw↝ obstructed fromw′
[p.93,𝓁-2] from some↝ for some
[p.99,𝓁+1] start↝ star
[p.105,Lemma 10.14] In the proof of the cases involving0or 1anchor, a combination
of the decompositions from Section 8.4 and Section 9 are used. These decompo-
sitions haven’t been shown to be compatible. Instead, it is better to combine
∆(v,W ) with t0-truncation on the rest of the quad-cluster. With at0 truncation,
we no longer have the non-positivity results from Section 8. (The quoins give a
positive contribution.) However, a routine calculation shows that the estimate on
∆(v,W ) is sufficiently small so that we still obtain a constant less than−1.04pt.
[p.116][p.121] Definition 11.7 allows masked flat in definition of3-unconfined. Def-
inition 11.24 requires no masked flats in the same definition. Use Definition 11.24
(no masked flats), rather than 11.7. Where masked flats occur, treat them with
Lemma 11.23, parts (1) and (2).
[p.116,𝓁+1] Lemma 4.16↝ Lemma 4.17
[p.117,before Lemma 11.9]two others↝ three others
[p.117,Def 11.8]y1↝ y1
[p.119,Definition 11.5] By definition, we require a masked flat quarter to be a strict
quarter.
[p.121] See p.116.
[p.121,𝓁-5] 0.2274↝ 0.02274
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 37
[p.123. flat case (2)] It is missing isolated quarters cut from the side. To fix this,
in condition 2(f), η456≥
√
2↝η456≥
√
2 or η234≥
√
2
[p.124,Lemma 11.27] The bound of 0 is established in Theorem 8.4↝The bound
of 0 for upright quarters appears in Lemma 8.12. The bound of0 for the other
anchored simplex appears in Lemma 8.7 or 8.13, depending on the circumradius.
[p.126] Theorem 12.1 should includeσR(D)≤ sn with s3 = 1pt ands4 = 0, and
τR(D)≥t3 = 0.
[p.131] Section 8 gives the deformation arguments that produce a biconnected
graph.
[p.139,Lemma 12.18,proof,𝓁+3] C0(|v|,π )↝ C u
0 (|v|,π )
[p.139,Lemma 12.18,proof,𝓁+6] τ0(C u
0 (2t0,π ))−πmax↝ τ0(C u
0 (2.2,π ))−πmax
[p.144,𝓁+11,𝓁+17] 2t2
0↝ (2t0)2
[p.146] S±
n ↝of 3-crowded, 3-undefined, and 4-crowded combinations
[p.148,§13.6] This entire section is misplaced. It belongs with§25.5 and§25.6.
[p.149,before 13.7]the diagrams↝Figs 25.1–25.4
[p.149,p.156] The definition ofδloop was accidently dropped from the published ver-
sion. Set δloop(4, 2) = 0 .12034 δloop(5, 1) = 0 .24939. These constants and their
properties appear in the earlier 2002 arXiv preprint of the proofThe Kepler con-
jecture (Sphere Packings VI).
[p.156,Lemma13.5,𝓁+4]respectively forτR(D)↝respectively, forσR(D) and τR(D)
[p.164,𝓁-1] This shows... occur. ↝This completes the proof.
[p.173,𝓁+4] Insert the subscript onb, as in Proposition 15.5, starting on page 173:
b ↝bq.
[p.182,Lemma 16.7] The bound of0 has not been shown to hold on each half. This
is not a direct consequence of Theorem 8.4 as claimed. This can be fixed as follows.
Letv1,v3 be the corners giving the endpoints of the long edge of the acute triangle
at 0, and letv2,v 4 be the other two corners. If either vertexv1,v 3 has height greater
than 2.3 show that the vor0-scored quad cluster scores less than−1.04pt. For this,
we may use the deformations of Lemmas 12.10. The length of the diagonal along
the acute face remains fixed and at least
√
8. We claim these deformations produce
a diagonal of length less than
√
8 between opposite corners of the quadrilateral. (If
not, the deformations produce a rhombus with side2 and diagonals both greater
than
√
8, which is a geometric impossibility.) We cut the quad cluster along the
diagonal of length
√
8 and continue with deformations until the top edges on each
simplex are (y4,y 5,y 6) = (2, 2,
√
8). We may applycalc-474496219 and calc-
8990938295to the two separate simplices to obtain the result. Now we may assume
that the heights ofv1,v 3 are at most2.3. If either height is at least2.1, the result
follows fromcalc-5127197465, which gives the bound of0 on each half.
38 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
Finally, we have the case where both heights are at most 2.1. We may apply
dimension-reduction techniques so that that the each of the two remaining corners
v⁄= v1,v 3 of the quad cluster either has height2 or has distance2 from v1 or v3.
We then reprove Lemma 16.8 without using the bound of0 and Lemma 16.9 for
tetrahedra without the bound−1.04 pt. This appears in calc-1551562505 and
calc-3013446042.
If the dimension reduction drops the cross-diagonal{v2,v 4} all the way to
√
8, then
we may swap diagonals and continue, until both diagonals are exactly
√
8. In this
case, by the cases already considered, we may assume that each corner has height
at most 2.1. Also, geometric considerations give that the other edges are at most
2.02:
E(2, 2, 2,
√
8, 2.1, 2.1, 2, 2, 2.02)>
√
8.
The result follows in this case bycalc-4723770703.
[p.241] Mixed is defined so as to include the pure analytic case. In earlier articles,
‘mixed’ excludes the pure analytic.mixed↝mixed or pure
[p.243,𝓁+13,𝓁+14,𝓁+15] Delete three sentences:‘Letv12 be... We let... Break the
pentagon... ’
[p.248,last displayed formula]= ↝ + so that it reads
∑
i
fRi(D)≤ ˆσ(Qi) +vorR′,0(D) +πR
[p.252,§25.7,Cases 2 and 3] ‘The flat quarter’ is mentioned, but there are no flat
quarters that have been introduced into the context. This passage has been dis-
placed from its original context.
[p.254,𝓁+7] to branch combine↝to combine
