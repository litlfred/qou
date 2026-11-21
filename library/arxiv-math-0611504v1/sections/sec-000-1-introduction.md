---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
toc_source: outline
doc_brief: "Quantum hyperbolic geometry — 25 sections: Front matter; Introduction; Universal QHG"
duplicate_of: "agt-v7-n2-p13-s"
---
In this paper we construct a new family {HN}, indexed by the odd integers N ≥1, of (2 + 1)-
dimensional quantum ﬁeld theories (QFT) that we call Quantum Hyperbolic Field Theories (QHFT).
Here, following [2, 30], by QFT we mean a functor from a (2 + 1)-bordism category, possibly non
purely topological, to the tensorial category of ﬁnite dimensional complex linear spaces.
The QHFT bordism category is based on triples (Y, LF, ρ), where Y is a compact oriented 3-manifold,
possibly with non-empty boundary ∂Y , LF is a properly embedded framed tangle (ie. a framed 1-
dimensional non oriented submanifold) in Y , and ρ is a ﬂat sl(2, C)-connection on Y \ LF up to gauge
equivalence (ie. a PSL(2, C)-character of Y \ LF), with arbitrary holonomy at the meridians of the
tangle components. We require furthermore that LF is non-empty when N > 1, and that it intersects
each of the boundary component, if any.
We will also consider a variant, denoted QHFT0, such that the tangles L are unframed, while the
characters ρ are deﬁned on the whole of Y , that is the meridian holonomies are trivial. Finally we
consider a “fusion” of QHFT and QHFT0 (still denoted QHFT) that incorporates both, by considering
tangles having a framed part LF as well as an unframed one L0 (see Section 5.3).
The objects of the bordism category are suitably marked surfaces. Every such a QHFT surface is a
diﬀeomorphism f : (S, T , p(β)) →Σ, where T is a so called “eﬃcient triangulation” of a ﬁxed base
oriented surface S with genus g and r marked framed points pi (r > 0 and r > 2 if g = 0), and β
is any PSL(2, C)-character of S \ {pi}, represented by points p(β) in speciﬁc parameter spaces for
Hom(π, PSL(2, C)), built on T and particularly suited to the QHFT. In fact we construct several such
parameter spaces with small “residual gauge groups” acting on them, and we point out the relations
to each other. One of them, the so called (−)-exponential I-parameter space, is deﬁned in terms
of cross-ratios and incorporates the Bonahon-Thurston shearbend coordinates for pleated hyperbolic
surfaces with punctures.
Every QHFT bordism has marked boundary and is considered as a “transition” from its input QHFT
surfaces towards the output ones. We understand that the characters ρ and β are compatible. Every
QHFT functor associates to such a transition a tensor called the amplitude, deﬁned up to a sign and
multiplication by Nth roots of unity.
When Y = W is closed (that is ∂Y = ∅), the amplitudes HN(W, LF, ρ) are numerical invariants
called partition functions. The QHFT0 partition functions HN(W, L, ρ) coincide with the “quantum
hyperbolic invariants” constructed in [4, 5], while the QHFT ones yield new wide families of numerical
invariants, covering interesting geometric situations, such as compact hyperbolic cone manifolds. We
will analyze the relations between HN and HN partition functions. In [5] we deﬁned also quantum
hyperbolic invariants HN(M) for non-compact complete hyperbolic 3-manifolds M of ﬁnite volume,
ie. for cusped manifolds. Although these invariants are not immediately QHFT partition functions, we
will show how they can be obtained in terms of these last. For that we establish a “surgery formula” for
quantum hyperbolic invariants of cusped manifolds and QHFT partition functions that generalizes the
one for Cheeger-Chern-Simons classes, and makes a crucial use of some of W. Neumann’s arguments
in [25], sections 11 and 14.
By restricting QHFT to the trivial bordisms (the cylinders) we get a new family of conjugacy classes
of “moderately projective” representations of the mapping class groups of punctured surfaces, that is,
deﬁned up to a sign and multiplication by Nth roots of unity.
We stress that we need that any bordism includes a non-empty link, intersecting each boundary
component (so that the QHFT surfaces have punctures), in order to build a consistent functor when
N > 1 (see [5], Lemma 6.4). Even when the holonomy is trivial around the punctures, we cannot
forget them, in particular for what concerns the mapping class groups.
We show that QHFT are in fact restrictions to a geometric bordism category of “universal functors”
called Quantum Hyperbolic Geometry (QHG). QHG includes the deﬁnition of a speciﬁc category of
triangulated 3-dimensional pseudomanifolds equipped with additional structures, and modeled on the
QUANTUM HYPERBOLIC GEOMETRY
3
functional properties of the matrix dilogarithms studied in [5]. The QHG functors associate determined
tensors to every such a decorated triangulation, obtained by tracing the matrix dilogarithms supported
by each tetrahedron.
The key point is that such tensors are invariant up to QHG triangulated
pseudomanifold isomorphism.
The main step in order to construct specializations with a strong
geometric content, such as QHFT, consists in converting each QHFT (marked) bordism to a QHG
triangulated pseudomanifold, unique up to QHG triangulated pseudomanifold isomorphism.
Hence we view this paper as a kind of achievement of the fundation of the theory initiated in [4, 5].
A main interest in the QHFT comes from the fact that they relate classical 3-dimensional hyperbolic
geometry to the world of quantum ﬁeld theories, two main themes of low-dimensional topology that
remained essentially disjoint since their spectacular developments in the early eighties. In particular,
the celebrated Kashaev’s Volume Conjecture for hyperbolic knots in S3 [21] appears as a special
instance of the challenging general problem of understanding the relations between the asymptotic
behaviour of QHFT partition functions and fundamental invariants coming from diﬀerential geometry,
like the Cheeger-Chern-Simons class (see [4], section 5, [5], section 7, and section 6.1 of the present
paper). We plan to face the asymptotics of QHFT partition functions in future works.
In [3] the spectrum of the mapping class group representations of Section 5.4 is studied by using
geometric quantization of the Bonahon-Thurston complex intersection 2-form.
A natural problem left unsettled is to determine the relations between the QHFT and Turaev’s Homo-
topic QFT [31]. This and formulas describing the behaviour of the QHFT amplitudes under framing
changes will be treated in a sequel to this paper, as they rely mainly on R-matrix computations.
We refer to [7] for a discussion about QHG in the framework of gravity in dimension 3.
Remark 1.1. The results of this paper can be repeated almost verbatim to deﬁne Cheeger-Chern-
Simons invariants for QHFT bordisms, by replacing the matrix dilogarithms for N > 1 with Neu-
mann’s extended Rogers dilogarithm, corresponding to N = 1 (see Remark 5.5). This is described
with all details in [5] for the case of cusped manifolds and triples (W, L, ρ) (ie. for quantum hyperbolic
invariants). Hence in the following we concentrate on the quantum theory N > 1, which is technically
harder.
Here is the content of the paper.
The universal QHG functors are deﬁned in section 2, where we recall also from [4, 5] and [24, 25]
(section 2.4 in particular) the notions and results we need.
The QHFT bordism category is described in section 4, while its objects, the QHFT surfaces, are
developed starting with section 3.
The QHFT functors are deﬁned in section 5.
This includes the construction of the distinguished
QHG triangulated pseudomanifolds associated to any triple (Y, LF, ρ) with marked boundary compo-
nents, and of the trace tensors computed on them. The conjugacy classes of moderately projective
representations of the mapping class groups are treated in section 5.4.
The partition functions HN(W, LF, ρ) are considered in section 6. We show in section 6.1 that when
ρ is deﬁned on the whole of W, HN(W, LF, ρ) coincides with HN(W, L ∪L′, ρ), where L′ is a parallel
copy of the unframed link L given by the framing F. In section 6.2 we prove the surgery formula for
quantum hyperbolic invariants of cusped manifolds and QHFT partition functions. In fact the QHG
pseudomanifolds used to compute the trace tensors carry certain cohomological weights (see Section
2.4) and the partition function values actually depend also on them. These weights play indeed a subtle
role in the surgery formulas. This eventually leads to realize HN(M) as the limit of HN(Mn, Ln, ρn),
where Mn is a sequence of closed hyperbolic manifolds converging geometrically to M, Ln is the link
of geodesic cores of the hyperbolic Dehn ﬁllings of M that produce Mn, and ρn is the hyperbolic
holonomy of Mn. In section 6.3 we discuss alternative computations of the QHFT partition functions
for manifolds that ﬁber over S1. For ﬁbred cusped manifolds, this allows in particular to identify each
HN(M) with a special instance of QHFT partition function. We conclude with an example in section
6.3.
4
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
Convention. Unless otherwise stated all manifolds are oriented, and the boundary is oriented via
the convention: last is the ingoing normal. Often we denote “=N” the equality of tensors up to sign
and multiplication by Nth roots of unity.
