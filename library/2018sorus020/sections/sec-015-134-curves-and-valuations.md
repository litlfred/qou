---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-015-134-curves-and-valuations
section_title: "Curves and valuations"
section_number: 1.3.4
pages: 33-34
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
Curves and valuations
Examples of ﬁeld extensions of k together with k-valuations are given by algebraic
varieties deﬁned over k. In particular, pick X ⊂X(Γ) an irreducible component of
the character variety, its function ring k[X] is a domain, and we denote by k(X) =
Frac(k[X]) its quotient ﬁeld, called the function ﬁeld of X. It is a general fact
that this ﬁeld is a k-valuated ﬁeld, with valuations corresponding to hypersurfaces
W ⊂X. We will be interested in the case where X is one dimensional, and we
refer to [Ful08] for details on what follows : there exists an unique curve ˆX, which is
smooth and compact, called the smooth projective model of X, with a birational map
ν : ˆX 99K X that is an isomorphism between open subsets and induces a canonical
ﬁeld isomorphism ν∗: k(X)
∼−→k( ˆX). There is a homeomorphism
ˆX →{k-valuations on k(X)}
x 7→vx : f 7→ordx(f)
32
where the set of valuations is endowed with the coﬁnite topology.
Remark 1.3.8. When the context will be clear, a curve X being given, we will
often denote by v a point in the smooth projective model ˆX.
Deﬁnition 1.3.9. Let v ∈ˆX be a point in the projective model of X. We will call
it an ideal point if ν is not deﬁned at v, equivalently the function ring k[X] is not a
subring of Ov. Otherwise we will call v a ﬁnite point.
Example 1.3.10. Let X be the plane curve {x2−y3 = 0} in C2. It is a singular aﬃne
curve, with function ring C[X] = C[U, V ]/(U 2 −V 3). The map C[X] →C[T] that
maps U to T 3 and V to T 2 induces an isomorphism between of ﬁelds Frac(C[X]) ≃
C(T). Moreover, it deﬁnes a birational map ν : CP1 →X ⊂C2 by t 7→(t3, t2).
Hence the smooth projective model of X is isomorphic to CP1 (remark that the
singular point (0, 0) is "smoothed" through ν), and the ideal point is ∞. As a map
CP1 →CP2, ν sends ∞to [1 : 0 : 0], the curve X ∪{∞} ⊂CP2 is a (non smooth)
compactiﬁcation of X.
