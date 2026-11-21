---
doc_id: arxiv-2105.07724v2
doc_title: "SL2 tilting modules in the mixed case"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2105.07724v2.pdf
source_sha256: bc649dfaa1e76ec4
toc_source: outline
doc_brief: "SL2 tilting modules in the mixed case — Using the non-semisimple Temperley–Lieb calculus, we study the additive and monoidal structure of the category of tilting modules for SL2 in the mixed case."
---
Introduction
1
2.
Preliminaries
4
3.
Additive structure
11
4.
Monoidal structure
22
Appendix A.
Fusion rules for eves
29
Appendix B.
Applications
37
Appendix C.
Some additional comments and details
42
References
51
1. Introduction
Let k be a field of characteristic p, fix a non-zero element q ∈k∗, and let K be an algebraically
closed field containing k. Tilting modules for SL2, the reductive group SL2(K) if q = ±1 or
Lusztig’s divided power quantum group for sl2 if q̸ = ±1, are among the most well-studied
objects in representation theory. In this paper, we use diagrammatic methods to study monoidal
categories of tilting modules in the mixed case, i.e. for arbitrary (k, q). As a modern day
perspective, the mixed case can be thought of as a simultaneous generalization of the case of
the complex quantum group (at a root of unity), the case of the algebraic group in positive
characteristic, as well as the classical semisimple situation.
Tilting modules form a monoidal category, so one can ask questions concerning objects,
morphisms, and how these behave under the tensor product. Concentrating on objects and their
characters is the classical approach in representation theory. Recently, the focus has shifted
to understanding morphisms between tilting modules, especially from a monoidal perspective,
which has been driven by work from quantum topology and categorification. A more thorough
understanding of the associated diagrammatic and combinatorial model that underpins the
behavior of these tilting modules, known as the Temperley–Lieb category, was a key ingredient in
recent progress.
In this paper, we let Tiltk,q for arbitrary (k, q) denote the monoidal category obtained by
idempotent completion from the Temperley–Lieb category TLk,q, see Remark 2.15. We study
Mathematics Subject Classification 2020. Primary: 18M15, 20G42; Secondary: 17B10, 20C20, 20G05.
Keywords. Tilting modules in the mixed case, diagrammatic algebra, Temperley–Lieb algebras and categories,
fusion rules, braided structures.
1
arXiv:2105.07724v2  [math.RT]  7 Sep 2026
2
Tiltk,q with a focus on the behavior of objects and morphisms with respect to its monoidal
structure, a natural progression of previous work [TW21] and [TW20]. The main results of this
paper are contained within Sections 3 and 4 and can be summarized as follows.
In Section 3B we define mixed JW projectors Ev−1 in TLk,q for v ∈N and show that they
correspond to indecomposable tilting modules T(v −1) of highest weight v −1. These idempotents
have been constructed independently in [MS21] and they are a simultaneous generalization of the
classical Jones–Wenzl (short: JW) projectors [Jo83], [We87], the projectors of Goodman–Wenzl
[GW93], and the pJones–Wenzl projectors of Burrull–Libedinsky–Sentinelli [BLS19].
In Section 3C we study morphisms between mixed JW projectors in TLk,q and obtain a
presentation of Tiltk,q as an additive category by generators and relations. Specifically, we
exhibit Tiltk,q as the category of projective modules for the path algebra of a quiver with relations
explicitly described in Theorem 3.21, which can be interpreted as the (semi-infinite) Ringel dual
of SL2.
In Section 4 we turn to the monoidal structure and study fusion rules for Tiltk,q and their
categorified analogs in TLk,q. Classically, fusion rules express the structure constants for the
representation ring, i.e. the decomposition multiplicities of tensor products of modules, such
as T(v) ⊗T(w), into indecomposable modules. On the categorified level one is interested in
explicitly describing the projection and inclusion maps realizing such decompositions. In the
Temperley–Lieb context this means decomposing the tensor products Ev ⊗Ew of projectors into
idempotents that project onto the indecomposable summands predicted by the fusion rule.
A famous example is the recursion for the classical Jones–Wenzl projectors
v−1
=
v
+ 1
g∗
·
v−1
v−1
v−2
,
1
g∗
= −[v −1]q
[v]q
,
(1-1)
which describes the decomposition T(v −1) ⊗T(1) ∼= T(v) ⊕T(v −2) whenever all involved tilting
modules are simple. In fact, the Jones–Wenzl recursion (1-1) is often taken as (part of) the
definition of the Jones–Wenzl projectors.
In Theorem 4.8 we establish decompositions analogous to (1-1) in the mixed setting of TLk,q.
These provide a recursive description of the mixed JW projectors, which appear to be new in this
generality, even new when specialized to the positive characteristic or complex quantum group
cases, cf. [BDRM19]. As an example, we show an instance going beyond (1-1), which describes a
decomposition T(v −1) ⊗T(1) ∼= T(v) ⊕T(v −2) with summands that need not be simple:
v−1
=
v
+


1
g∗
·
v−1
v−1
v−2
−f∗
g∗
·
v−1
v−1
v−2
v−2


.
(1-2)
(Here and throughout the paper we use colored boxes to encode mixed JW projectors corresponding
to tilting modules that need not be simple.) The middle part of the rightmost diagram in (1-2)
corresponds to a nilpotent endomorphism of T(v −2). In particular, if T(v −2) is simple, then the
rightmost diagram is zero and we recover (1-1). In general, however, the decompositions provided
by Theorem 4.8 are more complex than suggested by the example (1-2). In particular, arbitrary
many summands can appear, with multiplicities up to two.
A bit of historical background and other works. Tilting modules for SL2 have played a
crucial role in representation theory and low-dimensional topology, even before their introduction
by Donkin [Don93] and Ringel [Rin91]. Let us recall parts of this story.
In the semisimple case, Tiltk,q is well-understood on the level of objects and morphisms: The
characters are given by Weyl’s character formula and the fusion rules by the Clebsch–Gordan rule.
3
On the morphism level, Tiltk,q was given a diagrammatic presentation early on by Rumer–Teller–
Weyl [RTW32] using what is nowadays called the Temperley–Lieb algebra or category TLk,q.
This diagrammatic presentation, in its quantum version, lies at the heart of constructions and
calculations for the Jones-type invariants of links and 3-manifolds via Jones–Wenzl projectors
and recoupling theory, see e.g. [KL94].
In the complex quantum group case, many of our results have previously appeared in the
literature. The fusion rules on the object level in this case are certainly well-known since the
end of the 1980s, but a bit hard to track down, see however [Don98] for a slightly later reference.
The category TLk,q plays a major role as it provides the diagrammatic and integral model of
Tiltk,q. (While we don’t know an explicit exposition, this can be deduced from [DPS98].) The
appropriate analog of JW projectors in this case were defined by Goodman–Wenzl [GW93], the
Ringel dual quiver was computed in [AT17], and (parts of) recoupling theory was developed
under the umbrella of non-semisimple 3-manifold invariants, see e.g. [BDRM19] or [DGGPR22].
Historically speaking, the characteristic p case came long before the complex quantum group
case, for example, due to its relationship to projective modules of the finite group SL2(Fpk). On
the level of objects, the characteristic p case is intensively studied throughout the literature,
see e.g. [CC76], [AJL83], [Don93], [EH02a], [EH02b] and [DH05]. Of particular importance,
are Steinberg’s and Donkin’s tensor product formulas, which give the characters of simple and
tilting modules. However, not much appears to be known about fusion of objects beyond special
cases, e.g. coming from studying Verlinde quotients, see for example [And19] or [BEO20], or
the situation of the finite group SL2(Fpk), see for example [Cra13]. On the morphism level, the
use of TLk,q is crucial, specifically in the work of Burrull–Libedinsky–Sentinelli [BLS19], which
introduced the pJW projectors, a main ingredient to find the quiver with relations and the center
of Tiltk,q, see [TW21] and [TW20]. When it comes to fusion for morphisms, our results are new.
In the (strictly) mixed case, most of the results in the present paper are new. See, however,
e.g. [Don98] and [And19] for character and fusion formulas, and [MS21] for their (independent)
construction of the mixed JW projectors.
Further directions. A potential application concerns quotients of Tiltk,q, especially in the
characteristic p and the strictly mixed cases, when the category Tiltk,q has infinitely many
⊗-ideals. This is in stark contrast to the semisimple and the complex quantum group case, where
one has no or only one non-trivial ⊗-ideal. The strictly mixed cases turn out to be very appealing
in two directions. First, in generalizing e.g. the results of [BEO20] to the mixed situation, where
Tiltk,q may have universal properties that are similar to those studied in the characteristic p
case. Second, it is easy to see that Tiltk,q1/2 has a non-degenerate braiding in the mixed case.
This is particularly interesting from the viewpoint of non-semisimple 3d TQFT, where one could
try to apply the strategy of modified traces from e.g. [GKPM11] and [GKPM13], to obtain new
non-semisimple 3d TQFTs.
The fusion rules for Tiltk,q are also of importance in physics (from which its name arose),
although the focus has been on the semisimple and complex quantum group cases. In fact, this
was one motivation to develop the Temperley–Lieb calculus [KL94] and its variations, which
appear under different names in the physics- and mathematics-oriented literature. For example,
idempotent truncations by tensor products of classical JW projectors are studied under the names
valenced Temperley–Lieb algebras in [FP18] and symmetric webs in [RT16]. (See also [Spe21]
for a discussion using the pℓJW projectors.) Other recent work concerns the non-semisimple
complex quantum group case and its relation to mathematical physics, see e.g. [KS10], but a
non-semisimple recoupling theory along the lines of [KL94] seems largely undeveloped.
Finally, the algorithm given in [JW17] to compute p-Kazhdan–Lusztig basis elements of affine
type A1 played a key role in [BLS19], and one could hope that this is a two-way street. For
4
example, via quantum Satake [Eli17] and the approach in [RW18] it might be possible to study
analogs of mixed Kazhdan–Lusztig bases.
Further remarks. Before we start with the main bulk of the paper, we remark:
(a) We tried to make the exposition of this paper self-contained by introducing all relevant
concepts and definitions, many of which are identical or very similar to those in [TW21].
Some results that we need, for example Theorem 3.21, can then be proved analogously as
in [TW21]. Instead of repeating these proofs here, we decided to only include detailed
commentary about the necessary changes. In summary, while some of our results here
depend on those of [TW21], a reader who wants to skip the proofs does not need to be
familiar with that paper.
(b) The comparison of the various (non-)semisimple JW projectors in the literature and their
relation to this paper is as follows. Our mixed projectors agree (modulo illustrations
conventions) with the projectors constructed independently in [MS21]. In the semisimple
case they agree with the classical JW projectors, and over C and at a root of unity they
agree with the projectors from [GW93], again modulo conventions. For p = ℓ< ∞and
q = 1, our projectors agree with the projectors from [BLS19]. In each case, constructing
the projectors and proving that they are well-defined, e.g. our Theorem 3.18, require non-
trivial numerical data. In our approach, these are the tilting characters, see Section 3A.
There are two other ways to get equivalent numerical data: First, one could use the Soergel
category for affine type A1 and the p-Kazhdan–Lusztig basis as in [BLS19]. This works
for the quantum parameter being 1, but for general quantum parameter the situation
is more complicated. A second method is to calculate the simple multiplicities within
the projective cover of the trivial Temperley–Lieb module, as done in [MS21] (which is a
follow-up of [Spe20] where the decomposition numbers of the Temperley–Lieb algebra
are computed). This works in the mixed case. However, a crucial upshot of the tilting
characters approach taken in this paper is that it might generalize beyond SL2, e.g. see
[Soe97] and [Soe98] for the complex quantum group case, very explicitly worked out in
[Str97].
Acknowledgments. We thank Elijah Bodish, David Craven, Nicolle González, Amit Hazi,
Robert Spencer and Catharina Stroppel for stimulating discussions and helpful exchanges of
emails. Special thanks to a referee and Robert Spencer for comments on a draft of this paper,
and to Jonas Antor for drawing our attention to an error in an earlier version.
Significant parts of this work were done when all the authors met at the Hausdorff Research
Institute for Mathematics (HIM) in the fall 2020 during the Junior Trimester Program New Trends
in Representation Theory. Hospitality and support of the HIM are gratefully acknowledged.
Parts of this paper needed extensive computer-based experiments, and all these calculations
were done using Mathematica 12. The first author thanks the Heilbronn Institute for Mathematical
Research for financial support; the second author’s computer literacy was sponsored by Covid19.
