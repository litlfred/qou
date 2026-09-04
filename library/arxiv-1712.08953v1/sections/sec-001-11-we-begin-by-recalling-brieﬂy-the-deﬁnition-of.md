---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-001-11-we-begin-by-recalling-brieﬂy-the-deﬁnition-of
section_title: "We begin by recalling brieﬂy the deﬁnition of the category FOT of framed oriented"
section_number: 1.1
pages: 1-2
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t ) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an orien ted link, in the"
---
tangles; this is the framed analog of the oriented tangle category OT introduced by
Turaev in [T2] and also appears in [EGNO, Remark 8.10.3] where it is deno tedFT .
By deﬁnition, it is the strict monoidal category with objects given by the set⟨↑,↓⟩ of
all words in the letters ↑ and↓. Tensor product of objects is given by concatenation,
e.g.,↑⊗↑⊗↓ =↑↑↓, and the unit object 1 is the empty word ∅ . For two words
a = am··· a1, b = bn··· b1∈⟨↑,↓⟩, morphisms f : a→ b are isotopy classes of framed
oriented tangles in [0 , 1]× [0, 1]× R with boundary
{( m+1−i
m+1 , 0, 0
) ⏐⏐⏐i = 1,...,m
}
∪
{( n+1−j
n+1 , 1, 0
) ⏐⏐⏐j = 1,...,n
}
,
such that the orientation in the y-direction near the boundary points
( m+1−i
m+1 , 0, 0
)
and( n+1−j
n+1 , 1, 0
)
are ai and bj, respectively. We will draw such tangles by projecting onto
thexy-plane in such a way that the implicit framing is “blackboard,” and there are no
triple intersections or tangencies; we also keep track of “over” or “under” data at each
crossing. We call the resulting diagrams ( a, b)-ribbons for short. For example, here is
a (↓↑↑↓,↓↓↑↑)-ribbon:
. (1.1)
Isotopy translates into the equivalence relation on diagrams gener ated by planar isotopy
ﬁxing the boundary, together with the oriented Reidemeister move s (FRI) ( not the
full (RI) due to framing!), (RII) and (RIII) displayed in Figure 1. Co mposition of
morphisms in FOT is given by vertically stacking diagrams, i.e., f◦g := fg, while
tensor product is given by horizontal concatenation, i.e., f⊗g :=fg .
Now let k be some ﬁxed commutative ground ring and ﬁx parameters z,t∈ k ×. The
extended oriented skein category ˆOS (z,t ) is the quotient of the k -linearization ofFOT
2010 Mathematics Subject Classiﬁcation : 17B10, 18D10.
Research supported in part by NSF grant DMS-1700905.
1
