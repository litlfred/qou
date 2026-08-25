---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-002-11-main-result-in-this-paper-we-compute-the-real
section_title: "Main result. In this paper we compute the real part of the semi-classical l imit of the"
section_number: 1.1
pages: 2-4
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
sequence of quantum hyperbolic invariants (or QHI ) associated to the (oriented) complement
M :=S3 \K of the ﬁgure-eight knot K := 41. We notably obtain exponential growth of the
invariants, with rate equal to the hyperbolic volume Vol( M )/2π, or subexponential growth,
depending on a choice of parameters of the QHI.
Let us state our main result. Denote by λK the canonical longitude of K, and by Xhyp(M )
the irreducible component of the PSL (2, C)-character variety of M containing the character
of the discrete faithful representations. The terms hρ and kc in the statement below will
be described later (see Section 3.3), but should be thought o f as additional geometric and
topological structures on M . In particular hρ is a function on the set of curves on ∂ ¯M , the
boundary torus at inﬁnity, with values in (2 iπ)Z. The QHI, denoted HN , depend on an odd
integerN ≥ 3 and take values in C modulo multiplication by 2 N -th roots of unity.
Theorem 1.1. For every character ρ ∈Xhyp(M ) and charge weight kc, the following holds:
(a) If hρ(λK) ∈ 2πi(2Z + 1), then
lim
N →+∞
2π
N Log|HN (M,ρ,h ρ,kc)| = Vol(M ).
(b) If hρ(λK ) ∈ 4πiZ, then
lim
N →+∞
2π
N Log|HN (M,ρ,h ρ,kc)| = 0.
This result belongs to the realm of the Volume Conjectures, a set of conjectures ﬁrst con-
sidered by Kashaev-Murakami-Murakami [40, 45], which pred ict that the semi-classical limit
of certain sequences of quantum invariants of ﬁnite volume c omplete hyperbolic manifolds is
equal to their volume. Theorem 1.1 shows new phenomena, due t o the fact that the QHI
depend on geometric data: they satisfy some kind of semi-cla ssical rigidity, since the choice
of character ρ has no eﬀect on their semi-classical limit, and their growth, exponential or not,
is determined by a geometrico-topological datum, the parit y of 1
2πihρ(λK ).
The proof of Theorem 1.1 is based on an (easily obtained) inte gral representation of the QHI, a
description of the so-called quantum gluing varieties , which form parameter spaces of the QHI
and come from previous works of the ﬁrst author with R. Benede tti, and elementary uses of
the saddle point method and Perron’s method to estimate the i ntegrals when N → +∞. The
crux of the proof lies in ﬁnding deformations of the integrat ion contours to “good positions” in
order to apply these methods. A technical diﬃculty is that th e endpoints of contours converge
to poles of the integrand as N → +∞. The analysis of case (b) is far more demanding than
that of case (a).
Many tools of this proof should generalize to study the QHI as ymptotics for arbitrary cusped
manifolds, in situations more general than those implement ed by the two kinds of values of
hρ(λK ) in Theorem 1.1. For this reason, since the QHI theory is not w ell known, in some
parts of the paper we allow ourselves to present relevant gen eral aspects of this theory, in a
hopefully pedestrian way, and introduce notions that shoul d appear to be useful mainly for
generalizations of Theorem 1.1 (we do this in Sections 2.1, 2 .2, 2.4, 3.3 and 4.1, see the plan of
the paper below). In particular, we discuss the space of loga rithmic limits of log-parameters,
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 3
on which the QHI asymptotics can be studied, and where the cas es (a)-(b) of Theorem 1.1
correspond to very peculiar situations.
We remark that, beyond the semi-classical limit shown in The orem 1.1, sub exponential terms
can be obtained (see Remark 5.8). Also, the alternative betw een the cases (a) and (b) of
Theorem 1.1 seemingly reﬂects that the QHI could detect lift s to SL(2, C) of PSL (2, C)-
characters; we plan to develop this in a future work.
In a forthcoming version of this work we will consider also si milar asymptotics of QHI for
hyperbolic Dehn ﬁllings of M .
In the rest of this introduction we present the QHI and the str ucture of the proof of Theorem
1.1.
The QHI and their relations to other invariants . The QHI refer to two main types of
invariants:
• either invariants of a pair ( N,L ), where N is a compact oriented 3-manifold (with or
without boundary) and L ⊂N is a properly embedded tangle;
• or invariants of a cusped manifold M , i.e., M is an oriented non-compact 3-manifold
admitting a complete hyperbolic structure with ﬁnite volum e.
In both cases the manifold is endowed with additional geomet ric structures, including a
PSL (2, C)-character of the fundamental group. We will refer to the ﬁr st type as QHI of pairs .
These QHI generalize the Kashaev invariants deﬁned in [38, 3 9] (see [3, 6]). In particular
the Kashaev invariants ⟨L⟩N of a link L inS3, which are specializations of the colored Jones
polynomials ([45]), coincide with the QHI of the pair ( S3,L ) ([6]). The QHI of cusped
manifolds have been deﬁned in [4], and further reﬁned in [7, 8 ]. By means of a hyperbolic
Dehn ﬁlling theorem proved in [5], we can relate some QHI of M with the QHI of pairs ( N,L )
where N \L =M .
Both types of QHI are deﬁned by state sums over triangulation s very similar to Neumann’s
simplicial formulas for the Chern-Simons invariant of PSL (2, C)-characters ([48]); in these
state sums the classical dilogarithm functions are replace d with tensors called “matrix” dilog-
arithms, satisfying a ﬁve term identity similar to the Roger ’s one for dilogarithms. Because
of this strong structural relationship, it is natural that e xpect that a “Volume Conjecture for
the QHI” should occur, relating their semi-classical limit with the Chern-Simons invariant of
PSL (2, C)-characters. This was proposed in [2]; Theorem 1.1 (a) prov es it for the ﬁgure-eight
knot complement. Numerical evidences of the parity phenome non (a) vs. (b) in Theorem 1.1
were provided in [7, Section 9] also for the complement of the knot 5 2.
The QHI of mapping cylinders are easier to deal with, essenti ally because the mapping cylin-
der axis trivializes asymmetrical features of the QHI const ruction. It was shown in [9] that
the reduced QHI (see Section 3.3) of mapping tori of pseudo-Anosov diﬀeom orphisms of a
punctured surface S are the trace of intertwiners between local representations of the quan-
tum Teichm¨ uller space ofS (in the sense of [10]). This has been greatly clariﬁed recent ly
by Ishibashi ([35]), who provided, in particular, an altern ative construction of these reduced
QHI based on quantum cluster algebras associated to “dotted ” ideal triangulations of S, in
the sense of Kashaev ([41]). Also, Garoufalidis-Yu ([33]) o btained a decomposition of these
reduced QHI (in the case where the holonomy is boundary-para bolic and the log weight
lκ = 0) in terms of the Bonahon-Liu-Wong-Yang intertwiners of i rreducible representations
of the Kauﬀman bracket skein algebra of S ([16], [18, Theorem 16]) and the gl1-invariants of
mapping classes studied by Gocho ([30]) and Murakami-Ohtsu ki-Okada ([46]).
In particular, the results of this paper can be compared with those of Bonahon-Wong-Yang
in [19], which uses a diﬀerent approach. In another direction , the Andersen–Kashaev [1]
partition functions, which are derived from inﬁnite dimens ional quantum Teichm¨ uller theory,
