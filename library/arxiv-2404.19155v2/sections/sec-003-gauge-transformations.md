---
doc_id: arxiv-2404.19155v2
doc_title: "Octahedral coordinates from the Wirtinger presentation Calvin McPhail-Snyder Duke University calvin@sl2.site"
section_id: sec-003-gauge-transformations
section_title: "Gauge transformations"
section_number: null
pages: 13-14
source_pdf: 2404.19155v2.pdf
source_sha256: 45b9ed90006536b3
doc_brief: "Octahedral coordinates from the Wirtinger presentation Calvin McPhail-Snyder Duke University calvin@sl2.site — Letρ be a representation of a knot group (or more generally, the funda- mental group of"
---
D
h
D′
h
(a) D′ is obtained from D by a type (A) gauge transformation by h.
D
h
D′′
h
(b) D′′ is obtained from D by a type (B) gauge transformation by h.
Figure 8: Graphical description of gauge transformations. The thick strands represent bundles
of incoming and outgoing segments (possibly empty) with arbitrary colorings.
4. Gauge transformations
In this section we discuss how gauge transformation (conjugation) of the representation
ρ interacts with the decorations and shadows. In this context it is natural to break gauge
transformations into two separate types. We then use gauge transformations to prove that
every decorated representation is gauge-equivalent to an admissible one (i.e. one that is the
holonomy of an octahedral coloring).
Definition 4.1. Leti7→ (gi,Li),j7→uj be a decorated shadow SL2(C) coloring of a tangle
diagramD. A gauge transformation of it is a coloring of the form
(A) i7→ (h−1gih,Lih) andj7→g−1uj
(B) i7→ (gi,Li) andj7→h−1uj
for someh∈ SL2(C). We say the new colorings are the images of type (A) and type (B) gauge
transformations byh.
It is not hard to see that the gauge transformation of a coloring is still a coloring and
that the corresponding representation ρ : π(D)→ SL2(C) is conjugated under a type (A)
transformation and unchanged under type (B). We can use type (B) transformations to choose
the shadow of a single region arbitrarily as in Lemma 2.9.
The letters A and B are chosen because a type (A) transformation comes from pulling a
strand colored byh across and Above the diagram, while for type (B) we pull across and Below.
Both are shown in Figure 8. These are quite similar to the diagrammatic gauge transformations
of Blanchet et al. [Bla+20, Section 3.3]. Combinatorially they come from Reidemeister moves
for shadow colored diagrams.
Leti7→χi be the octahedral coloring associated to a shadow coloring. We can immediately
compute that under a type (A) transformation byh the new associated coloring is
(21) i7→ ˜χi =
det(h−1ui↓, e2)
det(h−1ui↑, e2),− vihe2
vihh−1uj
,mi

=
det(ui↓,h e2)
det(ui↑,h e2),−vihe2
viui↑
,mi

