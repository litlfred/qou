---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMA TION JESSICA S. PURCELL"
section_id: sec-003-12-cone-deformations
section_title: "Cone deformations"
section_number: 1.2
pages: 2-5
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION JESSICA S. PURCELL — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
we found similar bounds on volumes for another class of knots [21]. Using
negatively curved metrics, we recently improved these resu lts with Futer
and Kalfagianni [11].
CUSP SHAPES UNDER CONE DEFORMATION 3
However, as far as we are aware, the results of this paper are t he ﬁrst of
their kind giving actual geometric bounds on cusp shape base d only on a
diagram.
1.2. Cone deformations. Our primary technique is cone deformation, which
we will now describe. Using properties of cone deformations , we obtain geo-
metric information on the topological process of Dehn ﬁllin g.
Deﬁnition 1.1. Given a manifold M with torus boundary ∂M and speciﬁed
slope s on ∂M , we obtain a new manifold by gluing a solid torus to ∂M such
that s bounds a disk in the solid torus. This is called the Dehn ﬁlling of M
along s, or sometimes Dehn surgery , and the resulting manifold is denoted
M (s). More generally, if M has n torus boundary components with slopes
s1, . . . , sn, then we obtain M (s1, . . . , sn) in the same manner.
A geometric description of Dehn ﬁlling was investigated by T hurston [23].
Given a complete hyperbolic structure on a manifold M with torus bound-
ary, he showed the structure could be deformed through incom plete hyper-
bolic structures with singularities at the core of the added solid torus to
structures whose completion is again non-singular. These s tructures are ex-
actly hyperbolic structures on Dehn ﬁlled manifolds M (s). The space of
deformations is called hyperbolic Dehn surgery space.
We restrict our attention to particular paths through hyper bolic Dehn
surgery space in which the incomplete hyperbolic manifolds are all cone
manifolds. That is, the completion gives a manifold with con e singularities
along the core of the added solid torus, with cone angle α. (A more complete
deﬁnition of a cone deformation is given in Deﬁnition 2.1 bel ow.)
We have some control over cone deformations. Local rigidity results due
to Hodgson and Kerckhoﬀ [13], extended by Bromberg in the cas e of geo-
metrically ﬁnite manifolds [9], give control on the change i n geometry of the
entire manifold, knowing only information on the change in a neighborhood
of the singular locus.
This geometric control has been used recently to prove sever al interesting
results in 3–manifold theory. Hodgson and Kerckhoﬀ used it t o give universal
bounds on the number of exceptional Dehn surgery slopes for ﬁ nite volume
manifolds [14]. In the inﬁnite volume case, cone deformatio ns lie at the
heart of drilling and grafting theorems, described by Bromb erg in [8]. These
have recently been used to resolve problems in the ﬁeld of Kle inian groups,
such as the Bers density conjecture [7], and existence of typ e preserving
sequences of Kleinian groups [6]. This paper gives another a pplication of
cone deformations, to ﬁnite volume manifolds with cusps.
1.3. Cusp shapes. Let M be a manifold admitting a hyperbolic structure,
with a torus boundary component T . Under the hyperbolic structure on
M , T will be a cusp. We take a horoball neighborhood of this cusp. I ts
boundary is a horospherical torus, which inherits a Euclide an structure from
the hyperbolic structure on M . The structure is independent of choice of
4 JESSICA S. PURCELL
horoball neighborhood, up to scaling of the Euclidean metri c. Thus we
obtain a class of Euclidean similarity structures on T , which we call the
cusp shape of the torus T .
Now, suppose the hyperbolic structure of M is changing under a cone
deformation with singularities along a link Σ in M disjoint from T . Σ is
called the singular locus of the deformation. T will remain a cusp throughout
the deformation, and its cusp shape will be changing with the change of
geometry of M . We bound this change in terms of the change in geometry
in a neighborhood of Σ.
Theorem 1.2. Suppose we have the following:
• M a complete ﬁnite volume hyperbolic 3–manifold with a cusp T .
• X = X0 a complete ﬁnite volume hyperbolic 3–manifold which can be
joined to M = Xτ by a smooth one–parameter family of hyperbolic
cone manifolds Xt, such that cone angles go from 0 at time t = 0 to
2π at time τ .
• A singular locus, say with n components, such that the tube radius
about each component is larger than R1 ≥ 0.56 for all t.
• A horoball neighborhood Ut of the cusp of Xt which deforms to T at
time τ . Let γ(t) denote the path ∂Ut travels through the Teichm¨ uller
space of the torus, endowed with Teichm¨ uller metric ‖ · ‖.
Then there exists a parameterization of the deformation such that we have
the following bound for ∂Ut:
2 ‖γ′(t)‖2Area(∂Ut) ≤ n C(R1)
Here C(R1) is a strictly decreasing function of R1 which approaches 0 as R1
approaches inﬁnity. Moreover, we can assume τ ≤ (2π)2.
Also interesting is the application of Theorem 1.2 to length s of curves on
the cusp in question. Let β be a slope on the cusp torus, and again let γ(t)
be the path that the cusp shape ∂Ut traces through the Teichm¨ uller space
of the torus. Let Lt be the normalized length of β under the deformation,
with derivative ˙L = d
dt Lt (see section 3.3 for more information). Then Lt
will satisfy:
(1) − ‖γ′(t)‖ Lt ≤ ˙L ≤ ‖γ′(t)‖ Lt.
Combining equation (1) with the result of Theorem 1.2, we may bound
the change in normalized length of a curve under a cone deform ation.
Theorem 1.3. Let the set up be as in Theorem 1.2 above. Let Lt be the
normalized length of a slope on a cusp torus under the cone def ormation,
with derivative ˙L = d
dt Lt. Then there exists a parameterization of the cone
deformation such that the change in Lt is bounded by the following inequality:
−
( √
n C(R1)
2Area(∂Ut)
)
Lt ≤ ˙L ≤
( √
n C(R1)
2Area(∂Ut)
)
Lt
CUSP SHAPES UNDER CONE DEFORMATION 5
Finally, we use Theorem 1.3 to bound the normalized length of the arc
perpendicular to the shortest curve on the cusp torus, and th en bound the
length of this shortest curve below. We then obtain an estima te that is
independent of time.
Theorem 1.4. Let the notation be as in Theorem 1.2 above. Denote by
h(M ) the normalized height of the cusp torus ∂Uτ . That is, h(M ) is the
normalized length of the arc perpendicular to the shortest c urve on ∂Uτ that
runs from the shortest curve back to the shortest curve (this arc might not
be closed). Similarly, let h(X) denote the normalized height of ∂U0. Then
there exists a parameterization of the cone deformation suc h that the change
in normalized height is bounded in terms of R1 alone:
−(2π)2
√
n C(R1)
(1 − e−2R1)
√
2
≤ h(M ) − h(X) ≤ (2π)2
√
n C(R1)
(1 − e−2R1 )
√
2
.
