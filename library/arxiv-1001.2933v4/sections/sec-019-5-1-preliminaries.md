---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-019-5-1-preliminaries
section_title: "Preliminaries"
section_number: "5.1"
pages: 86-94
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
5.1 Preliminaries
To apply the Morse theory machinery, we need to start at some point in the complex γ plane
where we know how to express the integration cycle of Chern-Simons theory as a sum over
Lefschetz thimbles. With this in hand, one can then vary γ and take Stokes phenomena into
account.
If k and n are positive integers, so γ > 0, Chern-Simons theory is defined by an integral
over SU(2)-valued connections modulo gauge transformations. In the framework of the
present paper, this means that the integration cycle for A = A + iφ is the real cycle φ = 0,
which we call CR. This cycle can be expressed in terms of Lefschetz thimbles as described
22The relevant metrics look near the knot like ds2 = dz2/z2 + z2
(dx
2 + dy2
), where the knot is located at
z = 0, the “infrared” region in gauge/gravity duality. The “ultraviolet” region for z → ∞ is cut off by the
embedding in S
3
.
86

most precisely in eqn. (3.39):
CR =
X
σ∈ΣR
Jσ +
X
σ∈Σ−
nσJσ, (5.1)
Here Σ is the set of critical points – or rather critical gauge orbits, but we will speak
loosely of critical points. The critical points are flat connections on S
3\K with appropriate
monodromy. ΣR consists of the real critical points (the ones with φ = 0), and Σ− consists
of complex critical points corresponding to flat connections A for which the real part of the
exponent of the path integral is negative. This exponent, including the contribution from
the knot, is
I = ikW(A) + (n − 1) ln l. (5.2)
The coefficients nσ must be computed by counting solutions of flow equations. Because of
the difficulty of actually doing this, our results for the figure-eight knot will be incomplete.
An important topological fact about SU(2) gauge theory is that for the case of a knot in
S
3 and monodromy sufficiently close to the identity, the only real critical point corresponds to
the abelian flat connection Aab. So for sufficiently small values of γ = n/k, the contribution
to CR from the sum over ΣR is simply the cycle Jab associated to Aab.
CR is initially defined as a real integration cycle in UC, the space of complex-valued
connections. To analytically continue to complex values of k, we must lift and extend CR
to a cycle C ⊂ UbC; recall that UbC is a cover of UC where the Chern-Simons function W(A)
is well-defined as a complex-valued function. This process was described schematically in
section 2.5. Concretely, analytic continuation can be made by choosing a lift to C of the
Chern-Simons invariant W(Aσ) for each critical point that appears in (5.1) with a nonzero
coefficient. In section 2.5.3, a geometrical interpretation was given for a choice in which, for
some given real number α, one requires α < Im I < α + 2π for all σ. The most general
possible choice was described in section 2.5.2.
The choice that we will make of analytic continuation is guided by the fact that for fixed
n, the colored Jones polynomial has a unique analytic continuation to a function Jn(q) with
no essential singularity at k = ∞ (or equivalently at q = 1). Moreover [9], in the semiclassical
limit, Jn(q) is bounded as n → ∞ for sufficiently small γ. We take these facts to mean that
there is a unique choice of C such that, in a sufficiently small neighborhood of γ = 0, the
path integral has no exponentially growing contributions; it receives contributions only from
critical points for which Re I is zero or negative. This should hold regardless of the direction
in which one approaches the point γ = 0 in the complex plane.
The Chern-Simons invariant of the abelian flat connection Aab vanishes modulo 2π.
Avoiding exponential growth tells us how to lift Jab to UbC: we must pick the lift such that
the Chern-Simons invariant W(Aab) is 0 (rather than a non-zero multiple of 2π). Similarly,
we pick the branch of the logarithm such that ln l = 0. Henceforth, when we refer to Aab as
87

a critical point in UbC or to Jab as a cycle in UbC, we have in mind this lifting, which we call
the canonical lifting.
For any K, the contribution of Aab to the integration cycle is always precisely Jab, regardless of γ. In fact, Stokes phenomena never cause a jumping in the coefficients with which
abelian critical points contribute to the integration cycle. This is explained in sections 3.3.4
and 3.4.2. Jumping definitely can occur for the coefficients of Lefschetz thimbles associated
to nonabelian critical points.
For a typical knot, nonabelian critical points have nonzero I near γ = 0; let us assume
this to be the case. At first sight, the argument of section 3.2.1 seems to show that if flat
connections with nonzero I contribute to the path integral near γ = 0, then an essential
singularity for k → ∞ is unavoidable. If this were the case, we would conclude that in a
neighborhood of γ = 0, the desired integration cycle C must precisely coincide with Jab for
all knots. There seem to be two fallacies in this reasoning.
First, the argument in section 3.2.1 assumed that the flow equations conserve Im I.
However, as discussed in section 4.2.6, in the presence of a knot, this is only so if one
replaces the loop space of G/TC by its universal cover, as one should do if one wishes to
analytically continue Jn(q) to non-integral values of n. In this case, a choice of branch of ln l
is regarded as part of the data specifying a critical point. If the concept of a critical point is
understood in this way, then Im I is conserved in the Chern-Simons flow equations and the
argument of section 3.2.1 is applicable. Otherwise, we cannot make this argument.
At best (since we note another problem shortly), the conclusion from section 3.2.1 is that
if Jn(q), after being analytically continued to non-integral n, has no essential singularity for
k → ∞ or q → 1, then the integration cycle for sufficiently small γ is simply C = Jab.
Unfortunately, although it seems clear in the framework of the present paper that Jn(q)
can be analytically continued away from integer values of n, this does not seem to have been
explored in the literature. The claim that Jn(q) has no essential singularity at k = ∞ is only
known in general for integer n, and we have little guidance about whether this remains so
after analytic continuation in n.
The simplest example is the unknot K0. The explicit formula23 is
Jn(q; K0) = r
2
k + 2
sin 
πn
k + 2
. (5.3)
Clearly, this function can be analytically continued in n, and the analytically continued
23Recall that in our normalization, Jn(q) is defined by a path integral rather than a ratio of path integrals;
for an explanation of the relation of this to the usual normalization in the mathematical literature, see the
last paragraph of section 2.5.3.
88

function has no essential singularity at k = ∞. For the trefoil, we will see at the end of
section 5.2.4 that for n 6∈ Z, there is an essential singularity at infinity,24 but the situation
for more general knots is very unclear.
The second problem is that Chern-Simons theory is more complicated than the situation
considered in section 3.2.1. It is assumed there that the Stokes curves are straight rays,
which is not the case in Chern-Simons theory, and perhaps more important, it is assumed
that there are only finitely many critical points and Stokes curves. In Chern-Simons theory,
once one analytically continues away from integer k, there are infinitely many critical orbits
(corresponding to different liftings of the Chern-Simons invariant of a flat connection) meeting at γ = 0, and this can play an important role. In the case of the trefoil knot, we will
see that along the positive imaginary γ axis, arbitrarily close to γ = 0, an infinite number
of critical points must be included to describe the integration cycle.
We do not have a general theory of how to determine the integration cycle so as to avoid
exponential growth of the path integral for k → ∞, so we will have to take an exploratory
point of view in our examples. In our study of the trefoil, we will show that Jab is indeed
the correct integration cycle if one approaches γ = 0 along any direction except the positive
imaginary axis. For the figure-eight knot, we will not make an equally detailed analysis.
Once one knows the correct integration cycle near γ = 0, whether it is simply Jab or not,
the appropriate integration cycle for any γ can be found in the usual way by varying γ and
taking account of Stokes phenomena.
5.1.1 Local Models
Since studying the behavior near a singularity of the moduli space of flat connections is
an important technique for understanding Stokes phenomena, it may be helpful for some
readers if we briefly discuss the deformation theory of a flat bundle. (When we consider
examples later, we do so in a more informal language, and some readers may omit the
following discussion.)
Let E be a flat bundle over a manifold M, with structure group G and connection A = A0.
Let Y be the automorphism group of E, and set25 V = H1(M, ad(E)), V
′ = H2
(M, ad(E)).
V parametrizes first order deformations of E, and V
′ parametrizes obstructions to such
deformations. In deformation theory, it is shown that there is a Y -invariant map σ : V → V
′
24I am informed by C. Beasley that this can also be verified for more general torus knots using formulas
of [34].
25Here ad(E) is the sheaf of infinitesimal gauge transformations, leaving fixed the structure along the knot
if a knot is present.
89

such that the moduli space of deformations of E is σ
−1
(0)/Y . (Rather than dividing by Y ,
it may be more convenient to think of the moduli space as the space σ
−1
(0) with an action
of Y .) We can expand σ as a power series in a variable v ∈ V . The lowest order term is
quadratic and comes from the cup product. Higher order terms come from Massey products.
(For example, see [58]. From a physical point of view, these higher order terms arise by
integrating out massive modes of the gauge field; see section 4.2 of [59].)
If M is a three-manifold, then V
′
is dual to V and the discussion simplifies. In this case,
there is a Y -invariant function Φ on V , and the map σ is dΦ, the differential of Φ. Again Φ
can be expanded as a power series in v. The leading term is cubic and comes by evaluating
the classical action I(A) as a function on V . From a physical point of view, Φ is the effective
action for the zero modes of the gauge field; it contains cubic couplings that can be read
off from I(A), and higher order couplings (described mathematically in terms of Massey
products) that arise by integrating out massive modes.
In our application, there will be an additional parameter γ, controlling the monodromy
around a knot. Suppose that the flat bundle E appears for γ = γ0. To include γ in the above
discussion, simply set ǫ = γ − γ0. The effective action Φ can be extended from a function
on V to a function on V × Cǫ, where Cǫis a copy of the complex plane parametrized by ǫ,
in such a way that flat connections, for any ǫ, correspond to points in V × Cǫ at which the
equation dV Φ = 0 is obeyed. Here dV is the exterior derivative in the V direction. In other
words, flat connections for a given ǫ correspond to critical points of the restriction of Φ to
the fiber of the projection V × Cǫ → Cǫ that lies above that value of ǫ.
The question now arises of how many Massey products must be included to get a good
model of the behavior near the flat bundle E that we started with. The answer, assuming26
that for ǫ = 0 (and hence any ǫ near 0), there are only finitely many flat bundles near E, is
that one must go far enough to lift all degeneracies. If the cubic form obtained by evaluating
W(A) as a function on V is nondegenerate, this gives a complete answer for Φ; otherwise,
one must carry out a power series to higher order, including enough Massey products to get
a nondegenerate result.
Singularity theory gives a convenient framework for this discussion. Pick a transversal U
to the gauge orbit of the flat bundle E. Consider I(A) as a function on U. This function has
a singularity (that is, a degenerate critical point) at the point A = A0. Though U is infinitedimensional, the singularity can be modeled in finite dimensions. In fact, after making some
choices, one can embed V in U and write U as V × N, where N is an infinite-dimensional
space that parametrizes the nonzero modes of A; we assume that A = A0 corresponds to
the product of the origin in V and a point in N that we call the origin. The decomposition
26This is not always true in three-manifold theory, since in general the moduli space of flat connections
may have components of positive dimension. It is true in our applications involving knots. In general, one
needs to include enough Massey products to lift whatever degeneracies do get lifted.
90

U = V × N can be made in a Y -invariant fashion. Singularity theory says that one can
choose the decomposition so that I(A) near A = A0 is the sum of a function on V and a
function on N, such that the function on V is the effective action Φ, and the function on
N has a nondegenerate critical point at the origin. The function Φ : V → C thus gives a
finite-dimensional model of the singularity of the function I(A) : U → C. Because of the
choices that are made in identifying U as V ×N, Φ is only determined up to a diffeomorphism
of V (more exactly, a Y -invariant diffeomorphism that leaves fixed the origin). Within its
equivalence class, one can take Φ to be a polynomial, determined by finitely many Massey
products.
The importance of this for Chern-Simons theory is as follows. The integral over Y behaves
in the semiclassical limit as an infinite-dimensional Gaussian integral (with perturbative
corrections). It does not contribute to Stokes phenomena near A = A0. The interesting
subtleties in the behavior of the Chern-Simons path integral near the flat bundle E in the
semiclassical limit are all contained in the integral over V .
We will encounter three examples of this construction. Conceptually, the most simple
example arises for the figure-eight knot at γ = 1/3, where two nonabelian flat connections
meet. The flat bundle E is irreducible, and its automorphism group Y is trivial. The space
V is one-dimensional, and Φ is the function Φ = x
3/3 − ǫx related to the Airy integral. As
Φ is cubic, Massey products play no role. The other two examples involve the case that
A0 = Aab is the abelian flat connection, so the group Y is C
∗
. For either the trefoil or the
figure-eight knot, there is a critical value of γ at which Aab meets one or more non-abelian
flat connections. In each case V is two-dimensional and Y acts with weights 1 and −1. We
write u, v for coordinates on V corresponding to these weights. For the trefoil knot, it turns
out that the appropriate local model is Φ = (uv)
2/2 − ǫuv. The quartic term in Φ comes
from a Massey product. For the figure-eight knot, one gets instead Φ = (uv)
3/3−ǫuv, where
now a Massey product of rather high order is involved in generating the (uv)
3
term.
5.1.2 Normalization Of The Path Integral
Instead of simply saying, as we have just done, that the contribution to the Chern-Simons
path integral of a degenerate critical point can be modeled by a corresponding finitedimensional integral, it is possible, as we will briefly sketch, to be more precise and to
describe the normalization factors. The facts we will describe could be used to sharpen the
comparisons that we will describe later between the Chern-Simons path integral and computations in the mathematical literature that are based on the exact solution of Chern-Simons
theory, obtained by combinatorial methods. (We will not do so in this paper and the reader
might choose to omit this explanation.)
91

We first recall the nondegenerate case. The contribution of a nondegenerate critical point
to the Chern-Simons path integral was evaluated in [51], compared to the exact solution
(and slightly corrected27) in [22], and further refined in [23, 27]. In Chern-Simons theory on
a three-manifold M with compact gauge group H, let E → M be an H-bundle and suppose
that H0(M, ad(E)) = H1(M, ad(E)) = 0. The automorphism group P of E is then a finite
group (in general, the Lie algebra of P is H0(M, ad(E))). Let IE = ikW be the action of
Chern-Simons theory, evaluated for the critical point E. The contribution of the flat bundle
E to the Chern-Simons path integral is then
1
#P
exp(IE) exp(iπη(ad(E))/4)p
T(ad(E)). (5.4)
where η(ad(E)) is the Atiyah-Patodi-Singer η-invariant of the operator ⋆d+d⋆ acting on odd
degree forms with values in ad(E); T(ad(E)) is the Ray-Singer analytic torsion of this flat
bundle; and #P is the order of the finite group P. The expression (5.4) arises by performing
the path integral for fluctuations around the flat bundle E, in the Gaussian approximation.
Higher order corrections will multiply this expression by an asymptotic series in powers of
1/k (the same is true for eqn. (5.5) below), as explored in [60, 61].
Now let us assume that E corresponds to a degenerate critical point. We continue to
assume that H0(M, ad(E)) = 0, but we take V = H1(M, ad(E)) to be nonzero. We can still
carry out a Gaussian integral over the nonzero modes of the gauge field (the modes that in
the terminology of section 5.1.1 parametrize N). The result of integrating over the nonzero
modes is still given by the formula (5.4), if properly interpreted. There is one essential point:
for an acyclic flat connection, the torsion is a number, but in the general case, as explained
in the original construction of analytic torsion [62], and used in the present context in [23],
it is a linear form on a certain one-dimensional space – constructed as a tensor product of
the determinants of the cohomology groups of the flat bundle in question. In the present
situation, the only nonzero cohomology group is V = H1(M, ad(E)), and p
T(ad(E)) is a
linear form on det V . It determines a translation-invariant measure on V that we will denote
as dv.
What we want to integrate over V , using this measure, is essentially exp(Φ), where the
function Φ was described in section 5.1.1. The generalization of (5.4) for V 6= 0 is
1
#P
exp(iπη(ad(E))/4)(k/2π
2
)
dim V /2
Z
V
dv exp(Φ), (5.5)
where we replace p
T(ad(E)) by the measure dv and use it to integrate over V . (The
factor exp(IE) has disappeared as IE is simply the value of Φ at v = 0. If v = 0 were
a nondegenerate critical point of Φ, the factor k
dim V /2 would be canceled upon doing the
Gaussian integral over V . That this factor is precisely a power of k/2π
2 was found for
27A normalization was used in [51] in which η and log T were both two times smaller than usual.
92

H = SU(2) in [27]. This has apparently not been established in complete generality, though
it can plausibly be done using localization formulas [32].) The idea of (5.5) is that the
integrand exp(iπη(ad(E))/2) dv exp(Φ)/#P comes from the path integral over N and we
complete the path integral by integrating over V .
In the general case (and in fact in two of the three examples mentioned at the end of
section 5.1.1), we must consider a flat bundle E such that H0(M, ad(E)) 6= 0. The automorphism group P of E then has dimension dP = dim H0
(M, ad(E)). Moreover, p
T(ad(E)) is
now the ratio of a measure on V and one on the Lie algebra p of P. A convenient way to
proceed is to pick a metric on p (such as the usual one in which short coroots have length
squared two) and let Vol(P) be the volume of P using this metric. Once we have picked a
metric and hence a measure on p,
p
T(ad(E)) can be regarded just as before as a measure
dv on V . The generalization of (5.5) is then
1
Vol(P)
exp(iπη(ad(E))/4)(k/2π
2
)
(dim V −dim P)/2
Z
V
dv exp(Φ). (5.6)
The factor exp(iπη(ad(E))/4) depends on the metric of M. The metric dependence can
be removed (by subtracting a “counterterm”) once a framing (or two-framing) of M is picked;
this was the approach in [51]. A canonical two-framing exists [63] and is often used. The
formulas specialized to this two-framing were described in detail in [22] for H = SU(2).
5.1.3 Orientation Of The Integration Cycle
As a last preliminary comment, we should perhaps discuss the fact that although the invariant
Jn(q; K0) of the unknot – given in eqn. (5.3) – has no essential singularity at k = ∞, it
does have a square root singularity there. This square root singularity is common for all
knots.28 The meaning of the square root singularity is that under analytic continuation
around k = ∞, the orientation of the integration cycle C is reversed.
This reversal of orientation under analytic continuation is not an exotic phenomenon. It
occurs for the simple Gaussian integral R ∞
−∞ dx exp(ikx2
) = p
π/ik, where the square root
shows that under analytic continuation around k = ∞, the orientation of the integration
cycle is reversed. (Concretely, this happens because if k is rotated by an angle φ in the
complex plane, the integration cycle in the x-plane should be rotated by an angle φ/2 to
maintain convergence of the integral. For φ = 2π, we get back the original integration cycle
with opposite orientation.) The existence of this monodromy shows that the treatment of
the orientation of the integration cycle will be subtle in Chern-Simons theory, but we will
phrase our discussion to minimize the role of such details.
28It cancels in ratios Jn(q; K)/Jn(q; K0), which are the functions usually considered in the mathematical
literature. These ratios are Laurent polynomials in q = exp(2πi/(k + 2)).
93
