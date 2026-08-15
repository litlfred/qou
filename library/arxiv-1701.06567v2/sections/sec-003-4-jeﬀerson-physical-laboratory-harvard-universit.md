---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-003-4-jeﬀerson-physical-laboratory-harvard-universit
section_title: "Jeﬀerson Physical Laboratory, Harvard University, Cambridge, MA 02138, USA"
section_number: 4
pages: 1-6
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Abstract: We provide a physical deﬁnition of new homological invariants Ha(M3) of 3-
manifolds (possibly, with knots) labeled by abelian ﬂat connections. The physical system in
question involves a 6d ﬁvebrane theory onM3 times a 2-disk,D2, whose Hilbert space of BPS
states plays the role of a basic building block in categoriﬁcation of various partition functions
of 3dN = 2 theory T [M3]: D2×S1 half-index, S2×S1 superconformal index, and S2×S1
topologically twisted index. The ﬁrst partition function is labeled by a choice of boundary
condition and provides a reﬁnement of Chern-Simons (WRT) invariant. A linear combination
of them in the unreﬁned limit gives the analytically continued WRT invariant ofM3. The last
two can be factorized into the product of half-indices. We show how this works explicitly for
many examples, including Lens spaces, circle ﬁbrations over Riemann surfaces, and plumbed
3-manifolds.
CALT-TH-2016-039
arXiv:1701.06567v2  [hep-th]  24 May 2017
Contents
1. Introduction 2
2. Fivebranes on 3-manifolds and categoriﬁcation of WRT invariant 5
2.1 Preliminaries 5
2.2 D2×S1 partition function of T [M3] and WRT invariant 6
2.3 Realization in terms of counting solutions of diﬀerential equations 13
2.4 Surgeries, triangulations, and Atiyah-Floer 15
2.5 Superconformal index of T [M3] and its factorization 17
2.6 Further reﬁnement 18
2.7 Topologically twisted index of T [M3] 19
2.8 Generalization to U(N) 20
2.9 Relation to open GW invariants on T∗M3 21
2.10 Langlands duality and ﬂat connections 23
2.11 3-manifolds and the “bottom row” 23
3. Examples 26
3.1 M3 =S3 26
3.1.1 Categorifying the index 28
3.1.2 The t =qβ reduction from BPS spectral sequence 29
3.2 M3 =L(p, 1) 31
3.2.1 Reﬁned superconformal index 31
3.2.2 Topologically twisted index of T [L(p, 1)] 33
3.2.3 t =qβ reduction 35
3.2.4 Cyclotomic expansion 38
3.2.5 Positivity of coeﬃcients 40
3.2.6 Comparison with reﬁned CS 42
3.3 M3 =O(−p)→ Σg 45
3.3.1 Homological blocks and WRT invariant 46
3.3.2 Factorization of the superconformal index 47
3.3.3 Comparison with reﬁned CS 49
3.4 M3 = plumbed 50
3.4.1 Homological blocks ˆZa 51
3.4.2 Problems on the T [M3] side 54
– 1 –
4. Adding knots and links into M3 54
4.1 Links in M3 and line operators in T [M3] 55
4.2 Links in S2×S1 and Rozansky’s proposal 59
4.3 Links in L(p, 1) 62
4.3.1 Unreﬁned index of T [L(p, 1)] with Wilson loops 63
4.3.2 Reﬁnement and categoriﬁcation 64
4.4 Comparison with reﬁned CS 65
A. Z[[q]]-valued invariant for negative deﬁnite plumbed 3-manifolds 67
B. Cabling in M3 versus color in T [M3] 71
C. Categoriﬁcation of the Turaev-Viro invariants 73
1. Introduction
Can we hear the shape of a drum? Much like harmonics of a musical instrument, spectra of
quantum systems contain wealth of useful information. Of particular interest are supersym-
metric or the so-called BPS states which, depending on the problem at hand, can manifest
themselves either as minimal surfaces, or solutions to partial diﬀerential equations, or other
“extremal” objects. Thus, a spectrum of BPS states in Calabi-Yau compactiﬁcations can be
used to reconstruct the geometry of the Calabi-Yau space itself and, as we explain in this
paper, spectra of BPS states play a similar role in low-dimensional topology.
The old approach to constructing numerical invariants of 3- and 4-manifolds, as well as the
corresponding homological invariants of 3-manifolds, is based on gauge theory. The famous
examples are Donaldson-Witten and Seiberg-Witten (SW) invariants of 4- and 3-manifolds,
and corresponding instanton and monopole [1] Floer homologies of 3-manifolds. All of them
were extensively studied in mathematical literature and have appropriate rigorous deﬁnitions
that go back to the previous century. The numerical invariants are realized in terms of count-
ing solutions to certain partial diﬀerential equations, while the homological invariants build
on the ideas of Andreas Floer [2]. In particular, Seiberg-Witten invariants of 4-manifolds had
great success distinguishing some homeomorphic but non-diﬀeomorphic 4-manifolds. And, in
the world of 3-manifolds, the so-called Heegaard Floer homology constructed by Ozsvath and
Szabo [3] gives a much simpler and non-gauge theoretic deﬁnition of a homological invariant,
which is believed to be equivalent to the monopole Floer homology.
A seemingly diﬀerent class of 3-manifold invariants, the so-called Witten-Reshetikhin-
Turaev (WRT) invariants [4, 5], comes from a diﬀerent type of TQFT, which sometimes is
called “of Schwarz type” to distinguish it from the TQFTs “of cohomological type” mentioned
in the previous paragraph [6]. At the turn of the century, however, the distinction between
– 2 –
the two types started to blur and the ideas of the present paper suggest it may even go away
completely in the future. In fact, the ﬁrst hints for this go back to the early work [7–10]
that relates Seiberg-Witten theory in three dimensions to Chern-Simons theory with U(1|1)
super gauge group. The latter provides a much simpler invariant compared to the usual
Chern-Simons theory, say, with SU (2) gauge group, due to cancelations between bosonic
and fermionic contributions. Therefore, if one can ﬁnd a 4d TQFT that categoriﬁes SU (2)
Chern-Simons theory in 3d, similar to how 4d SW theory categoriﬁes 3d SW theory, it would
help a great deal with the classiﬁcation problem of smooth 4-manifolds. The ﬁrst step in
constructing such categoriﬁcation is, of course, to ﬁnd a homological invariant of 3-manifolds
whose (equivariant) Euler characteristic gives the WRT invariant.
The existence of such 4d TQFT was envisioned by Crane and Frenkel [11] more than
20 years ago, and the ﬁrst evidence came with the advent of knot homology [12–14] which
categoriﬁes WRT invariants of knots and links (realized by Wilson lines in CS theory) in S3,
also known as the colored Jones polynomial. The physical understanding of a homological
approach to HOMFLY polynomials was independently initiated in the physics literature in
[15], which later led to the physical interpretation of Khovanov-Rozansky homology as certain
BPS Hilbert spaces [16–19] (see e.g. [20,21] for an overview and an extensive list of references).
The physical construction suggests that there should be a homological invariant that
categoriﬁes (in a certain sense) the WRT invariant of general 3-manifolds with knots inside.
Namely, such homological invariant can be understood as the BPS sector of the Hilbert space
of the 6d N = (2, 0) theory (that is a theory describing dynamics of coincident M5-branes
in M-theory) on M3×D2× R with a certain supersymmetry preserving background along
M3×D2. Equivalently, if one ﬁrst reduces the 6d theory on M3, it can be understood as the
BPS Hilbert space of the eﬀective 3d N = 2 theory T [M3] on D2× R. On the other hand, if
one ﬁrst compactiﬁes on D2, one does not get an ordinary 4d gauge theory on M3× R like
4d SW gauge theory 1:
6d (2, 0) theory on R×D2×M3
↙ ↘
space of BPS states HBPS Hilbert spaceHM3 of
of 3dN = 2 theory T [M3] 4d “Crane-Frenkel TQFT”
on D2 on M3
(1.1)
There is another natural SUSY-preserving background on which one can quantizeT [M3].
Since the IR physics of T [M3] is governed by a non-trivial 3dN = 2 SCFT, one can consider
its radial quantization and study its Hilbert space on S2× R. This should provide us with
another non-trivial homological invariant of M3 which should have roughly the same level of
complexity as the BPS Hilbert space on D2× R which categoriﬁes the WRT invariant, but
1Roughly speaking, the eﬀective 4d theory is an inﬁnite KK-like tower on 4d gauge theories. However one
needs to appropriately sum it up. The decategoriﬁed counterpart of such summation was studied in [22].
– 3 –
with several advantages due to the presence of operator-state correspondence and no need to
specify a boundary condition at ∂D2 =S1.
The set of boundary conditions that one can put at ∂D2∼=S1 in the path integral can be
understood as follows. Let us represent D2 as an elongated cigar, which asymptoically looks
likeS1× R. After compactiﬁcation of the stack of ﬁvebranes on S1 we obtain 5d maximally
supersymmetric gauge theory. The supersymmetric vacua of such theory on M3× R (where
R is the original time direction) are given by ﬂat connections 2 on M3. The number of such
supersymetric vacua is the same as the number of boundary conditions ( cf. [18, 23–26]). As
we will see later, the subset of such boundary conditions that corresponds to abelian ﬂat
connections plays an important role; for convenience, here we summarize various clues that
all point to a special role of abelian ﬂat connections:
• charges of BPS states in the target space theory [15];
• relation between homological invariants of diﬀerent rank [27];
• resurgent analysis of complex Chern-Simons theory [22];
• similar analysis of 3d N = 2 theories (section 2 below);
• Langlands duality for ﬂat connections on 3-manifolds (section 2.10).
Moreover, in this paper we give many examples of q-series invariants for various 3-manifolds
which exhibit integrality, and in many cases we also write the corresponding homological
invariants. All of these invariants are labeled by (connected components of) abelian ﬂat
connections; we do not have any such example associated with a non-abelian ﬂat connection.
In this paper we study the relation between such homological invariants and their decat-
egoriﬁed counterparts — superconformal indices. The structure described above, of course,
will also manifest itself at the level of partition functions, i.e. indices, once we compactify
the time on S1. For some of the examples in this paper for there are no cancellations among
states in computing the reﬁned index. In those cases, the homological invariants are faithfully
captured by the reﬁned index computation.
The organization of the paper is as follows. In Section 2 we review some results of [27] and
summarize general conjectures about homological invariants of closed 3-manifolds mentioned
here and their decategoriﬁed versions. In Section 3 we consider various examples for which
we explicitly verify these conjectures. In Section 4 we extend it to the case of 3-manifolds
with knots. Note, the main part of Section 4 is written in jargonish shorthand, using the
concepts and notations introduced earlier. Various details and generalizations of this work
can be found in the appendices. Thus, Appendix A explains how the WRT invariants of
general negative deﬁnite plumbed 3-manifolds can be analytically continued away from roots
of unity to produce power series in q with integer powers and integer coeﬃcients, required
2The choice of such ﬂat connections should not be confused with the choice of ﬂat connections in CS theory
on M3. As will be explained later in detail they are related by S-transform.
– 4 –
for categoriﬁcation. In Appendix B, we compare the ordinary Khovanov homology of the
n-th cabling of the unknot in a 3-sphere to the reﬁned partition function of 3d N = 2 theory
T [S3] in the presence of line operators, cf. Figure 1. Finally, in Appendix C we explain how
categoriﬁcation of the index ofT [M3] relates to categoriﬁcation of the Turaev-Viro invariants.
BPS 
time
impurity
2d space
Figure 1: The space of BPS states in 3d N = 2 theory on R×D2 with an impurity, relevant to the
physical realization of Heegaard Floer homology HF (M3), monopole Floer homology HM (M3), as
well as categoriﬁcation of WRT invariants of 3-manifolds with knots.
