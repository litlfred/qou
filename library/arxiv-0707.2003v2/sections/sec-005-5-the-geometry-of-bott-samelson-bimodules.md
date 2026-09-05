---
doc_id: arxiv-0707.2003v2
doc_title: "A geometric model for Hochschild homology of Soergel bimodules BEN WEBSTER GEORDIE WILLIAMSON School of Mathematics Mathematisches Institut Institute for Advanced Study der Univers"
section_id: sec-005-5-the-geometry-of-bott-samelson-bimodules
section_title: "The geometry of Bott-Samelson bimodules"
section_number: 5
pages: 14-15
source_pdf: 0707.2003v2.pdf
source_sha256: 0b8fe37aabeee412
doc_brief: "A geometric model for Hochschild homology of Soergel bimodules BEN WEBSTER GEORDIE WILLIAMSON School of Mathematics Mathematisches Institut Institute for Advanced Study der Universität Freiburg — An"
---
In this section, we discuss Bott-Samelson bimodules, calcu late their B× B -
equivariant cohomology and obtain the formality results ne eded above.
Since we have already described the geometric realization o f indecomposable
bimodules, as intersection cohomology of subvarieties of G, we know ab-
stractly that the Bott-Samelson bimodule Ri must be the hypercohomology
of a perverse sheaf obtained by taking a direct sum of IC-sheaves of these
subvarieties with appropriate multiplicities.
However, this is deeply dissatisfying from a geometric view point, and totally
at odds with our viewpoint that Bott-Samelson bimodules are very natural
objects. Thus we would like a more natural geometric realiza tion of them.
For each simple reﬂection s, let Ps be the minimal parabolic containing s. For
a sequence i = (s, t, . . . , u) of simple reﬂections, let
Gi = Ps×B Pt . . .···× B Pu.
We call this the Bott-Samelson variety corresponding to i. Note that this vari-
ety still carries a B× B -action, and thus a diagonal B -action.
Furthermore, we have a projective B× B -equivariant map mi : Gi→ G given
by multiplication, intertwining the diagonal B -action on Gi with the conjuga-
tion B -action on G.
The quotient of Gi by the right Borel action is the familiar projective Bott-
Samelson variety which is used to construct resolutions of s ingularities for
Schubert varieties. It is worth noting that just like in the ﬂ ag variety case, if i
is a reduced expression (i.e. if ℓ(st . . . u) is the length of i), then the multipli-
cation map is a resolution of singularities.
Let us explain how to calculate the B× B -equivariant cohomology of the Bott-
Samelson varieties. Actually , we will calculate the corres ponding dg-module
over S⊗ S . We start with a lemma:
Lemma 5.1 SupposeF∈ DB×B(pt) and let s be a simple reﬂection. Then:
Γ B×B(resB×B
Ps×BindPs×B
B×BF) = S⊗Ss Γ B×B(F)
Proof Thanks to Theorem 3.3 we know that Γ Ps×B(indPs×B
B×BF) is equal to
Γ B×B(F) regarded as an Ss⊗ S -module. Hence
Γ B×B(resB×B
Ps×BindPs×B
B×BF) = ( S⊗ S)
L
⊗Ss⊗S Γ B×B(F).
14
However, S⊗ S is free as a module over Ss⊗ S and is hence K-projective.
Thus the derived tensor product coincides with the naive ten sor product and
the result follows.
We can now prove the crucial “formality” claim mentioned abo ve:
Proposition 5.2 The direct images of the sheaves CGi and IC(Gw) in DB×B(pt)
are formal.
Proof First notice that we can can write the sheaf (mi)∗CGi as a iterated in-
duction and restriction:
(mi)∗CGi
∼= resB×B
Ps×BindPs×B
B×B . . . resB×B
Pt×BindPt×B
B×B (CB)
Hence by the above lemma, letting p be the projection to a point:
Γ B×B(p∗CGi) = S⊗Ss S⊗St⊗···⊗ Su S in DAB×B
Thus the proposition is true for CGi . Now, by the decomposition theorem of
[BBD] or more precisely , its equivariant version in [BL], wemay obtain IC(Gw)
as a direct summand of (mi)∗Gi , if i = ( s, . . . , s) is a reduced expression for
w. Thus p∗IC(Gw) is a direct summand of p∗CGi and is also formal.
