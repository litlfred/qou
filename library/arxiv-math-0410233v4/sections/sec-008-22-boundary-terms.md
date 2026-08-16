---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMA TION JESSICA S. PURCELL"
section_id: sec-008-22-boundary-terms
section_title: "Boundary terms"
section_number: 2.2
pages: 9-10
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION JESSICA S. PURCELL — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
ary terms. In this section, we deﬁne these terms. We explain h ow they arise
and recall certain properties. They will be used in the proof of Theorem 1.2.
Using results of the last section, we may always assume that w e have a
harmonic representative ω = η + i ∗ Dη. Thus η satisﬁes equation (2).
Let N be any submanifold of X = M − Σ with boundary ∂N oriented
by the outward normal. When we take the L2 inner product of equation (2)
with η and integrate by parts over N , we obtain the boundary formula ([14,
Lemma 2.3]):
(7) B(N ) =
∫
∂N
η ∧ ∗Dη = ‖η‖2
N + ‖ ∗ Dη‖2
N
Here ‖ · ‖ denotes the L2–norm on N . We will apply equation (7) to sub-
manifolds of X = M − Σ involving tubular or horoball neighborhoods.
First, we will introduce some notation. Let Vj be a tubular neighborhood
of a component (the j-th component) of the singular locus, or a horoball
neighborhood of a cusp. Using similar notation to that of [14 ], deﬁne
bVj (ζ, ξ) =
∫
∂Vj
∗Dζ ∧ ξ,
where ∂Vj is oriented such that the tangent vector orthogonal to ∂Vj is an
outward normal when viewed from Vj. We will be considering bVj (η, η) in
this paper, and we review results concerning this term.
10 JESSICA S. PURCELL
The decomposition (3) of ω in Vj into ω0+ωc, and η into η0+ηc decomposes
the term bVj (η, η):
(8) bVj (η, η) = bVj (η0, η0) + bVj (ηc, ηc).
That is, cross terms vanish ([14, Lemma 2.5]). Additionally , the term
bVj (ηc, ηc) is actually non-positive ([14, Lemma 2.6]), so we ﬁnd
(9) bVj (η, η) ≤ bVj (η0, η0)
Now, let V be a tubular neighborhood of the entire singular locus Σ,
as well as horoball neighborhoods of cusps. Thus V is a union of tubu-
lar neighborhoods Vj of components Σ j of the singular locus and horoball
neighborhoods Uj. Then letting N = X − V in equation (7),
B(X − V ) = ‖η‖2
X−V + ‖ ∗ Dη‖2
X−V =
∫
∂V
∗Dη ∧ η(10)
=
∑
j
bVj (η, η) +
∑
k
bUj (η, η).(11)
The ﬁrst sum is over all components of the singular locus, the second over
all horoball neighborhoods of cusps. This equation, along w ith equation (9),
implies
(12) 0 ≤
∑
j
bVj (η, η) +
∑
k
bUk (η, η) ≤
∑
j
bVj (η0, η0) +
∑
k
bUk (η0, η0).
Notice η0 = ( η0)j depends on the neighborhood Vj or Uj. However,
using the notation bVj (η0, η0), it should be clear that we are referring to the
decomposition of η particular to Vj in this context, and similarly for Uj. We
will further simplify notation, using the following deﬁnit ion.
Deﬁnition 2.2. Let Σ j be a component of the singular locus Σ. Let Vj be
a tubular neighborhood of Σ j of radius R. We let bj be the boundary term:
bj = bVj (η0, η0).
Remark. Note that for our applications of the results of this section , the
one–form ω corresponds to an inﬁnitesimal deformation of hyperbolic s truc-
ture at time t. Thus ω, η, η0, bj, etc. will all depend on time t in our
applications in future sections.
To avoid a notational nightmare, in the sequel we will assume the time
t has been ﬁxed, and continue writing these terms without refe rence to t,
except occasionally where we feel recalling the dependency on t will help
avoid confusion.
