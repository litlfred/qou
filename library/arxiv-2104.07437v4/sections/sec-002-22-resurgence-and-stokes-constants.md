---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-002-22-resurgence-and-stokes-constants
section_title: "Resurgence and Stokes constants"
section_number: 2.2
pages: 7-10
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
Formal power series with factorial growth lead, under some assumptions, to a universal mathe-
matical structure described by the theory of resurgence, see [44, 45] for a formal description and
[17, 46] for applications in gauge and string theory. This mathematical structure involves a family
of numerical data called Stokes constants. When the perturbative series under consideration are
topological invariants of some underlying geometric object, the corresponding Stokes constants
lead to numerical, topological invariants. Surprisingly, these invariants turn out to be integers
in many situations. In this section we will provide the formal deﬁnition of Stokes constants, and
we will then apply this deﬁnition to the perturbative series (2.11).
Let us consider a factorially divergent (or Gevrey-1) series, of the form,
ϕ(τ) =
∑
n≥0
anτn, a n∼n!. (2.12)
The theory of resurgence tells us that, generically, this series will not be on its own, but will be
accompanied by an additional set of formal power series. To understand how this comes about,
we consider the Borel transform of ϕ(τ), deﬁned by
ˆϕ(ζ) =
∑
k≥0
ak
k!ζk. (2.13)
It is a holomorphic function in a neighborhood of the origin. In favorable cases, this function can
be extended to the complex ζ-plane (also called Borel plane), but it will have singularities. Let
us label by an index ω the (perhaps inﬁnite) set of singularities in the Borel plane ζω∈ C. Let
us assume for the moment being that this singularity is a logarithmic branch cut, and consider
the behavior of ˆϕ(ζ) near ζω:
ˆϕ(ζ) =−Sω
log(ξ)
2πi ˆϕω(ξ) +··· (2.14)
In this expression, ξ =ζ−ζω, the dots denote regular terms in ξ, the function
ˆϕω(ξ) =
∑
n≥0
ˆan,ωξn (2.15)
is an analytic function at ξ = 0, and Sω will be later identiﬁed as Stokes constants. As the
notation suggests, we can regard this series as the Borel transform of the Gevrey-1 series
ϕω(z) =
∑
n≥0
an,ωzn, a n,ω =n!ˆan,ω. (2.16)
– 6 –
Figure 1 . The diﬀerence between lateral Borel resummations in (2.23) (left) can be computed as a
contour integral, given by the contribution of the singularities (right).
We then see that, starting with a single formal power series, we can obtain a new family of
them by just looking at the behavior near the singularities of the Borel transform. We can now
repeat the procedure with the series obtained in this way. Eventually, one ends up with a family
of formal power series
Bϕ ={ϕω(z)}ω∈Ω, (2.17)
which we will call theminimal resurgent structureassociated to the original seriesϕ(z). The Borel
transform of the formal power series in the minimal resurgent structure have local expansions
ˆϕω(ζ) =−Sωω′
log(ξ)
2πi ˆϕω′(ξ) +··· . (2.18)
The complex numbers Sωω′ are called Stokes constants. Note that their values depend on a choice
of normalization of the series ϕω(z).
The Stokes constants appear in a diﬀerent type of calculation, which often is easier to perform
in practice. Let ϕ(z) be a generic Gevrey-1 series, and let us assume that the analytically
continued Borel transform ˆϕ(ζ) does not grow too fast at inﬁnity. The Borel resummation of
ϕ(z) is deﬁned as the Laplace transform
s(ϕ)(z) =
∫ ∞
0
e−ζˆϕ(ζz)dζ. (2.19)
This function, when it exists, is locally analytic, but has discontinuities at special rays in the z
plane. Let ζω be a singularity of ˆϕ(ζ). A ray in the Borel plane which starts at the origin and
passes through ζω is called a Stokes ray. It is of the form e iθR+, where
θ = arg(ζω). (2.20)
The integral (2.19) has a discontinuity whenever arg(z) = arg(ζω).
To calculate the discontinuities, we deﬁne the lateral Borel resummations forz near a Stokes
ray by
s±(ϕ)(z) =
∫ e±iϵ∞
0
e−ζˆϕ(ζz)dζ. (2.21)
The discontinuity is then simply given by
discθϕ(z) =s+(ϕ)(z)−s−(ϕ)(z), (2.22)
– 7 –
where θ is deﬁned in (2.20). A simple contour-deformation calculation (see Fig. 1) shows that,
in the case that all singularities are logarithmic, one has
s+(ϕω)(z)−s−(ϕω)(z) =
∑
ω′
Sωω′e−ζω′/zs−(ϕω′)(z), (2.23)
where the sum over ω′ runs over all the singularities located on the Stokes ray. This equation
turns out to give a powerful method to compute Stokes constants, by comparing (lateral) Borel
resummations.
To write the fundamental equation (2.23) in a more convenient form, we note that the ζω′
appearing in the r.h.s. depend implicitly on ω. To have a more symmetric form, we introduce
the basic trans-series Φω(z) as
Φω(z) = e−Vω/zϕω(z), (2.24)
where the Vω are chosen in such a way that ζω′ =Vω′−Vω. The Borel resummation of the basic
trans-series Φω(z) is deﬁned by
s(Φω)(z) = e−Vω/zs(ϕω)(z) (2.25)
To measure the discontinuity of Borel resummations across a Stokes ray, it is also useful to
introduce the Stokes automorphism S as
s+ =s−S. (2.26)
In this way, (2.23) can be written as
S(Φω) = Φω +
∑
ω′
Sωω′Φω′. (2.27)
Let us emphasize that the deﬁnition of Stokes constants given above relies on relatively mild
assumptions. In technical terms, we are assuming that the formal power series ϕω(z) are simple
resurgent functions. The property of being resurgent means that, on every ﬁnite line issuing
from the origin, the Borel transform ˆϕω(ζ) has a ﬁnite number of singularities, and one can
analytically continue it along a path which circumvents these singularities. Simple resurgent
functions have only logarithmic singularities, as in (2.14). However, it is straightforward to
extend this formalism to resurgent functions with more general singularities, like branch cuts of
the form
ˆϕ(ζω +ξ) = (−ξ)−ν Sω
2i sin(πb)
∑
n≥0
ˆanξn + regular, ν ⁄∈ Z. (2.28)
In this case, we regard ˆϕω(ξ) as the Borel transform of
ϕω(z) =z−ν∑
n≥0
anzn, a n = Γ(n + 1−ν)ˆan, (2.29)
and it is easy to check that the discontinuity formula (2.23) still holds in the same form.
In summary, the machinery of resurgence gives a well-deﬁned procedure to obtain a (possibly
inﬁnite) set of Stokes constants: starting from a single perturbative series ϕ, one ﬁrst ﬁnds the
minimal resurgent structure Bϕ, and then the set of Stokes constants. Schematically, we have
ϕ(τ)−→ Bϕ ={ϕω(τ)}ω∈Ω−→{ Sωω′}ω,ω′∈Ω. (2.30)
– 8 –
Remark 2.1. At this point, it might be useful to add some clarifying remarks on the notion of
minimal resurgent structure introduced above. The minimal resurgent structure associated to a
formal seriesϕ(z) is the smallest set of resurgent functions which is needed to ﬁnd a closed system
under Stokes automorphisms. It does not include necessarily all the formal power series in the
theory. A surprising example of this situation occurs in complex CS theory, where formal power
series are associated to perturbative expansions around ﬂat connections on a three-manifold M.
If M is the complement of a hyperbolic knot, there are two special ﬂat connections, namely
the trivial connection, and the so-called geometric connection, which corresponds to the unique
complete hyperbolic metric on M. They lead to two diﬀerent formal power series, which we
denote by Φ 0 and Φg, respectively. It follows e.g. from the results in [11, 12, 47, 48] that the
minimal resurgent structure associated to Φg, BΦg, does not include Φ0. The minimal resurgent
structure associated to Φ 0 is however strictly bigger: BΦg ⊊ BΦ0 [48–50].
