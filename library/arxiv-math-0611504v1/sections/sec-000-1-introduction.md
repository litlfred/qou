---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
doc_brief: "Quantum hyperbolic geometry STEPHANE BASEILHAC RICCARDO BENEDETTI — 19 sections: Introduction; Universal QHG; Building blocks"
duplicate_of: "agt-v7-n2-p13-s"
---
2. Universal QHG 4
2.1. Building blocks 4
2.2. QHG triangulated pseudomanifolds 7
2.3. QHG universal functor 9
2.4. Towards geometric specializations 10
3. Parameters for PSL (2, C)-characters of surfaces 12
3.1. Eﬃcient triangulations 13
3.2. Cocycle parameters 14
3.3. Cross-ratio parameters 16
4. The QHFT bordism category 20
4.1. Marked topological bordisms 20
4.2. Boundary structures 21
5. The QHFT functor 22
5.1. From QHFT bordisms to QHG-triangulated pseudomanifolds 22
5.2. Amplitudes 24
5.3. QHFT variants 26
5.4. Mapping class group representations 26
5.5. Tunneling the (+)/( −) states 27
6. Partition functions 28
6.1. QHFT vs QHFT 0 partition functions 29
6.2. Invariants of cusped manifolds and surgery formulas 29
6.3. Manifolds that ﬁber over S1 - Examples 35
References 40
Abstract. W e construct a new family, indexed by the odd integers N ≥ 1, of (2 + 1)-dimensional
quantum ﬁeld theories called quantum hyperbolic ﬁeld theories (QHFT), and we study its main
structural properties. The QHFT are deﬁned for (marked) (2 + 1)-bordisms supported by compact
oriented 3-manifolds Y with a properly embedded framed tangle LF and an arbitrary P SL(2, C)-
character ρ of Y \ LF (covering, for example, the case of hyperbolic cone manifol ds). The marking of
QHFT bordisms includes a speciﬁc set of parameters for the sp ace of pleated hyperbolic structures
on punctured surfaces. Each QHFT associates in a constructi ve way to any triple ( Y, L F , ρ ) with
marked boundary components a tensor built on the matrix dilo garithms, which is holomorphic in the
boundary parameters. W e establish surgery formulas for QHFT partitions functions and describe
their relations with the quantum hyperbolic invariants of [4, 5] (either deﬁned for unframed links in
closed manifolds and characters trivial at the link meridia ns, or hyperbolic cusped 3-manifolds). For
every P SL(2, C)-character of a punctured surface, we produce new families of conjugacy classes of
“moderately projective” representations of the mapping cl ass groups.
1
2 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
Keywords: hyperbolic geometry, quantum ﬁeld theory; mapping class gr oups, quantum invariants,
Cheeger-Chern-Simons class, dilogarithms.
1. Introduction
In this paper we construct a new family {HN }, indexed by the odd integers N ≥ 1, of (2 + 1)-
dimensional quantum ﬁeld theories (QFT) that we call Quantum Hype rbolic Field Theories (QHFT).
Here, following [2, 30], by QFT we mean a functor from a (2 + 1)-bordis m category, possibly non
purely topological, to the tensorial category of ﬁnite dimensional c omplex linear spaces.
The QHFT bordism category is based on triples ( Y,L F,ρ ), where Y is a compact oriented 3-manifold,
possibly with non-empty boundary ∂Y , LF is a properly embedded framed tangle (ie. a framed 1-
dimensional non oriented submanifold) in Y , and ρ is a ﬂat sl(2, C)-connection on Y \LF up to gauge
equivalence (ie. a PSL (2, C)-character of Y \LF ), with arbitrary holonomy at the meridians of the
tangle components. We require furthermore that LF is non-empty when N >1, and that it intersects
each of the boundary component, if any.
We will also consider a variant, denoted QHFT 0, such that the tangles L are unframed, while the
characters ρ are deﬁned on the whole of Y , that is the meridian holonomies are trivial. Finally we
consider a “fusion” of QHFT and QHFT 0 (still denoted QHFT) that incorporates both, by considering
tangles having a framed part LF as well as an unframed one L0 (see Section 5.3).
The objects of the bordism category are suitably marked surfaces. Every such a QHFT surface is a
diﬀeomorphism f : (S, T,p (β)) → Σ, where T is a so called “eﬃcient triangulation” of a ﬁxed base
oriented surface S with genus g and r marked framed points pi (r > 0 and r > 2 if g = 0), and β
is any PSL (2, C)-character of S \ {pi}, represented by points p(β) in speciﬁc parameter spaces for
Hom(π,PSL (2, C)), built on T and particularly suited to the QHFT. In fact we construct several such
parameter spaces with small “residual gauge groups” acting on th em, and we point out the relations
to each other. One of them, the so called ( −)-exponential I-parameter space, is deﬁned in terms
of cross-ratios and incorporates the Bonahon-Thurston shear bend coordinates for pleated hyperbolic
surfaces with punctures.
Every QHFT bordism has marked boundary and is considered as a “tr ansition” from its input QHFT
surfaces towards the output ones. We understand that the cha ractersρ and β are compatible. Every
QHFT functor associates to such a transition a tensor called the amplitude, deﬁned up to a sign and
multiplication by N th roots of unity.
When Y = W is closed (that is ∂Y = ∅), the amplitudes HN (W,L F,ρ ) are numerical invariants
called partition functions . The QHFT 0 partition functions HN (W,L,ρ ) coincide with the “quantum
hyperbolic invariants” constructed in [4, 5], while the QHFT ones yield n ew wide families of numerical
invariants, covering interesting geometric situations, such as com pact hyperbolic cone manifolds. We
will analyze the relations between HN and HN partition functions. In [5] we deﬁned also quantum
hyperbolic invariants HN (M ) for non-compact complete hyperbolic 3-manifolds M of ﬁnite volume,
ie. for cusped manifolds. Although these invariants are not immediately QHFT partition funct ions, we
will show how they can be obtained in terms of these last. For that we establish a “surgery formula” for
quantum hyperbolic invariants of cusped manifolds and QHFT partitio n functions that generalizes the
one for Cheeger-Chern-Simons classes, and makes a crucial use o f some of W. Neumann’s arguments
in [25], sections 11 and 14.
By restricting QHFT to the trivial bordisms (the cylinders) we get a n ew family of conjugacy classes
of “moderately projective” representations of the mapping class groups of punctured surfaces, that is,
deﬁned up to a sign and multiplication by N th roots of unity.
We stress that we need that any bordism includes a non-empty link, in tersecting each boundary
component (so that the QHFT surfaces have punctures), in orde r to build a consistent functor when
N > 1 (see [5], Lemma 6.4). Even when the holonomy is trivial around the pu nctures, we cannot
forget them, in particular for what concerns the mapping class gro ups.
We show that QHFT are in fact restrictions to a geometric bordism category of “universal functors”
called Quantum Hyperbolic Geometry (QHG). QHG includes the deﬁnitio n of a speciﬁc category of
triangulated 3-dimensional pseudomanifolds equipped with additiona l structures, and modeled on the
QUANTUM HYPERBOLIC GEOMETRY 3
functional properties of the matrix dilogarithms studied in [5]. The QHG functors associate determined
tensors to every such a decorated triangulation, obtained by tra cing the matrix dilogarithms supported
by each tetrahedron. The key point is that such tensors are invar iant up to QHG triangulated
pseudomanifold isomorphism. The main step in order to construct sp ecializations with a strong
geometric content, such as QHFT, consists in converting each QHF T (marked) bordism to a QHG
triangulated pseudomanifold, unique up to QHG triangulated pseudo manifold isomorphism.
Hence we view this paper as a kind of achievement of the fundation of the theory initiated in [4, 5].
A main interest in the QHFT comes from the fact that they relate clas sical 3-dimensional hyperbolic
geometry to the world of quantum ﬁeld theories, two main themes of low-dimensional topology that
remained essentially disjoint since their spectacular developments in the early eighties. In particular,
the celebrated Kashaev’s Volume Conjecture for hyperbolic knots in S3 [21] appears as a special
instance of the challenging general problem of understanding the r elations between the asymptotic
behaviour of QHFT partition functions and fundamental invariants coming from diﬀerential geometry,
like the Cheeger-Chern-Simons class (see [4], section 5, [5], section 7, and section 6.1 of the present
paper). We plan to face the asymptotics of QHFT partition function s in future works.
In [3] the spectrum of the mapping class group representations of Section 5.4 is studied by using
geometric quantization of the Bonahon-Thurston complex interse ction 2-form.
A natural problem left unsettled is to determine the relations betwe en the QHFT and Turaev’s Homo-
topic QFT [31]. This and formulas describing the behaviour of the QHFT amplitudes under framing
changes will be treated in a sequel to this paper, as they rely mainly o nR-matrix computations.
We refer to [7] for a discussion about QHG in the framework of gravit y in dimension 3.
Remark 1.1. The results of this paper can be repeated almost verbatim to deﬁne Cheeger-Chern-
Simons invariants for QHFT bordisms, by replacing the matrix dilogarit hms for N > 1 with Neu-
mann’s extended Rogers dilogarithm, corresponding to N = 1 (see Remark 5.5). This is described
with all details in [5] for the case of cusped manifolds and triples ( W,L,ρ ) (ie. for quantum hyperbolic
invariants). Hence in the following we concentrate on the quantum t heoryN >1, which is technically
harder.
Here is the content of the paper.
