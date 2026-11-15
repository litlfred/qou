---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-004-23-qhg-universal-functor
section_title: "QHG universal functor"
section_number: 2.3
pages: 9-10
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
toc_source: outline
doc_brief: "Quantum hyperbolic geometry — 25 sections: Front matter; Introduction; Universal QHG"
duplicate_of: "agt-v7-n2-p13-s"
---
pseudomanifold (Z, T ) a trace tensor HN(T ), as follows. Deﬁne an N-state of T as a function that
gives every 2-simplex an index, with values in {0, . . . , N −1}. Every N-state determines an entry
for each matrix dilogarithm RN(∆, b, w, f, c). As two tetrahedra induce opposite orientations on a
common 2-face, an index is down for the RN of one tetrahedron while it is up for the other (see Figure
1). By summing over repeated indices we get the total contraction of the tensors {RN(∆, b, w, f, c)},
that we denote Q
∆⊂T RN(∆, b, w, f, c). Let vI and vδ be the number of vertices of T \ ∂T and ∂T ,
respectively, that correspond to manifold points. We set
(11)
HN(T ) = N −(vδ/2+vI) Y
∆⊂T
RN(∆, b, w, f, c)
The type of a trace tensor HN(T ) depends on the b-signs of the boundary triangles of (T, b). The
matrix dilogarithms themselves are special instances of trace tensors.
We have
Proposition 2.5. For every odd N ≥1, up to sign and multiplication by Nth roots of unity the trace
tensor HN(T ) is invariant up to QHG isomorphism.
This result is a restatement of Theorem 2.1 (2) and Lemma 6.7 of [5], and summarizes the fundamental
functional relations satisﬁed by the matrix dilogarithms. In particular those corresponding to 2 ↔3
QHG transits are usually called ﬁve terms identities. In Figure 5 we show one instance in dual terms.
The normalization factor N −vI in (11) is due to the bubble move, that changes by 1 the number of
internal vertices.
y
x2
x
x3
x1
=
Figure 5.
A 2 ↔3 QHG move (x1 = y/x, x2 = y(1 −x)/x(1 −y), and x3 =
(1 −x)/(1 −y)).
The notions of “boundary” (also allowing only portions of the standard boundary - see eg. [30]),
bordism, and bordism gluing are well deﬁned for the category of QHG triangulated pseudomanifolds
considered up to QHG isomorphisms . Hence, for every odd N ≥1, the association of the trace tensor
to each bordism deﬁnes a functor. Note that the identities between trace tensors hold up to the phase
ambiguity of Proposition 2.5. Also, the normalization factor N −vδ/2 in (11) compensates the change
in the number of internal vertices when gluing along complete connected components of the (usual)
boundary (this is easily adapted to more general gluings).
10
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
Any bordism is the gluing of ﬂat/charged I-tetrahedra, considered as elementary bordisms between
the couples of 2-faces having b-sign equal to −1 or +1. The matrix dilogarithms can be interpreted as
the amplitudes of a diagonal exchange that relates two quadrilateral triangulations (recall the above
discussion about the geometric quantization derivation of matrix dilogarithms.)
