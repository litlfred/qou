---
doc_id: arxiv-2505.00799v2
doc_title: "QUANTUM MODULAR FORMS AND RESURGENCE"
section_id: sec-004-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 7-11
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
doc_brief: "QUANTUM MODULAR FORMS AND RESURGENCE — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
2.1. Resurgence. Resurgence is a theory of divergent series developed by ´Ecalle in the
1980s, building on work dating back to Borel. It begins with classical Borel resummation, but
leverages how exponentially small corrections to Borel-Laplace sums “resurge” by expanding
around different singularities of the Borel transform. For a more thorough recollection of
Borel resummation and resurgence, see [5,12,27].
8 ELEANOR MCSPIRIT AND LARRY ROLEN
The initial objects of interest in the theory of resurgence are formal power series
φ(z) =
∞X
n=0
anzn∈ C[[z]].
A rich source of such series are asymptotic series; we write f(z)∼φ(z) if
f(z)−
N−1X
n=0
anzn =O(zN)
as z→ 0 for all N ≥ 1. If this is the case, we say that φ(z) is an asymptotic expansion
of f(z) at z = 0. For our purposes, we will consider asymptotic expansions where z = it
2π
and t→ 0+. We will be interested in factorially divergent series, as characterized by the
following definition.
Definition 2.1. We say that a formal power series φ(z) is Gevrey-1 if there exist A,B > 0
such that
|an|≤ ABnΓ(n + 1), (n≥ 0),
where Γ is the gamma function.
Here, we note that Γ(n + 1) equalsn! since n∈ N. We choose to use the gamma function
throughout the paper, even when the factorial suffices, since it will allow for a uniform
treatment of all of our cases.
In order to build the theory of resurgence, we will first need to define the Borel and Laplace
transforms. Here, we introduce shifted versions of these transforms which will more readily
suit our needs.
Definition 2.2. The (formal) Borel transform with shift κ∈ C is defined on formal power
series by
Bκ
 ∞X
n=0
anzn
!
:=
∞X
n=0
an
Γ(n +κ)un.
When κ = 1, we simply call this the Borel transform, dropping the subscript. The
subsequent lemma can be readily proven from these definitions.
Lemma 2.3. If φ(z) is a Gevrey-1 formal power series, its Borel transform is analytic in a
neighborhood ofu = 0.
We also require the Laplace transform. We will consider integral transforms of functions
ψ(u) that are analytic on a half-strip{u∈ C: dist(u,eiθR+)<ε} with exponential type less
than some α∈ R, i.e. there exists an M such that|ψ(reiθ)|≤ Meαr as r tends to infinity.
QUANTUM MODULAR FORMS AND RESURGENCE 9
Definition 2.4. Suppose ψ(u) is analytic on a half-strip {u∈ C: dist(u,eiθR+) < ε} with
exponential type less than some α∈ R. Then the Laplace transform with shift κ in direction
θ, when it exists, is defined by
Lθ
κ(ψ)(z) :=z−κ
Z eiθ∞
0
e−u/zψ(u)uκ−1 du.
With the given conditions on ψ, the functionLθ
1(ψ)(z) is defined and analytic in the right
half-plane{ℜ(ze−iθ) > max(α, 0)}, and is locally analytic as one varies θ, as long as the
directions remain in the sector where ψ is analytic. As with the Borel transform, we drop
the subscript when κ = 1.
We note that instead of defining the κ-shifted Borel and Laplace transforms, which we do
to simplify exposition, one can multiply the underlying asymptotic series by zκ and proceed
accordingly.
Definition 2.5. The compositionLθ
κBκ is called the Borel-Laplace sum with shift κ in direc-
tion θ, which we will denote by Sθ
κ. If the Borel-Laplace sum converges for a formal power
series φ, we say that φ is 1-summable in direction θ.
The Borel and Laplace transforms are formally inverses on monomialszn withℜ(n+κ)> 0,
and ifφ is a series which converges in a neighborhood of 0, thenφ =Lθ
κBκ(φ) for allθ and for
all κ such thatℜ(κ)> 0. Despite the fact that in general φ̸=Lθ
κBκ(φ), the Borel–Laplace
sum of a Gevrey-1 divergent series is of interest to us since φ appears as the asymptotic
expansion ofSθ(φ).
Before we describe resurgence, we need a result which will allow us to move between shifted
Borel–Laplace sums. The result below follows from a straightforward application of results
for the unshifted Borel and Laplace transforms (e.g. Lemma 3, Section 3.2, and Theorem 2,
Section 3.3, of [5]) translated to our setting.
Lemma 2.6. Let φ(z) be a Gevrey-1 formal power series. Suppose κ,κ′∈ 1
2 Z and θ∈ R
are such that Sθ
κ(φ) andSθ
κ′(φ) are analytic for {ℜ(ze−iθ)> 0}. Then we have
Sθ
κ(φ) =Sθ
κ′(φ).
Thus, we drop the subscript κ when appropriate. We will also use the fact that taking
Borel-Laplace sums is linear (Theorem 2, Section 3.3 of [5]).
Returning to Gevrey-1 formal power series, we will be interested in when Borel trans-
forms of such series admit an analytic continuation beyond their original neighborhood of
convergence. The functions which will be the subject of later sections will primarily have
10 ELEANOR MCSPIRIT AND LARRY ROLEN
particularly nice analytic continuations and will be of exponential type 0 in the directions
we sum.
We will say an analytic function ψ(u) defined on the unit disk |u| < 1 is resurgent if it
admits endless analytic continuation (see [13] for a precise definition). Further, if ψ(u) has
only simple poles and logarithmic branch points, we say it is simple resurgent.
In the cases we will entertain for the remainder of the paper, the Borel transforms of our
formal power series φ(z) will be simple resurgent and will admit only simple poles which
are located along finitely many rays, called Stokes rays. These rays divide the u-plane into
finitely many sectors, and to each sector one associates a directional Laplace transform by
the above definition.
If ψ is simple resurgent with a simple pole at ω, it has the local expansion
ψ(u) =− Sω
2πi(u−ω) +F (u),
whereF is holomorphic in a neighborhood of ω. We call the constantSω the Stokes constant
corresponding to ω.
Now we investigate what happens as we vary the argument of the Laplace transform to
cross a Stokes ray. Suppose Ω is the set of poles of ψ and set θ := arg(ω) where ω∈ Ω. If
Ωθ is the subset of all poles lying along this ray, then there exists ε >0 such that for any
(θ−,θ +) satisfying 0 <θ +−θ <ε and 0 <θ −θ− <ε , we have
Lθ+
κ (ψ)(z)−Lθ−
κ (ψ)(z) =z−κ
X
ω∈Ωθ
Sωωκ−1e−ω/z =: discθ
κ(ψ(u)),
which we will call the discontinuity of ψ. In order to define a “canonical” Borel-Laplace
sum of a divergent series, one must determine how resum independent of a choice of angle
θ. This motivates the construction of the median resummation of a divergent series φ. In
general, median resummation is a more complex procedure than averaging, but in the case
whereSθ(φ) is analytic in a sector around eiθR+, it takes the form
Sθ
med(φ) :=Sθ+
(φ) +Sθ−
(φ)
2 .
This function is analytic in the sector with bisecting direction θ and opening π. In the case
whereB(φ) admits a single Stokes ray, this defines a unique function corresponding to φ.
We may also write
Sθ
med(φ) =



Sθ−
(φ) + 1
2discθ
κ(Bκ(φ)), ℜ(ze−iθ−
),ℜ(ze−iθ)> 0,
Sθ+
(φ)− 1
2discθ
κ(Bκ(φ)), ℜ(ze−iθ+
),ℜ(ze−iθ)> 0.
QUANTUM MODULAR FORMS AND RESURGENCE 11
This decomposition will be essential to our later realization of quantum modularity.
