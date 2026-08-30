---
doc_id: arxiv-math-ph-0010012v1
doc_title: "From random polynomials to symplectic geometry Steve Zelditch"
section_id: sec-001-2-mathematical-tools
section_title: "Mathematical Tools"
section_number: 2
pages: 2-3
source_pdf: 0010012v1.pdf
source_sha256: cd6eca5ccb81ff90
doc_brief: "From random polynomials to symplectic geometry Steve Zelditch — We review some recent results on random polynomials and their generalizations in complex and symplectic geometry."
---
We give a quick summary of some basic tools and methods that are used below. We will concentrate on
general ideas and refer to [ShZe, ShZe2, BSZ3] for detailed expositions.
2.1. Vector spaces of large dimension. In deﬁning our ensembles of polynomials, we will be dealing
with a sequence (HN, ⟨, ⟩N) of Hilbert spaces of increasing dimension dN = dimHN, where N is the ‘degree of
the polynomial’, a large integral (semiclassical) parameter. The dimension is given by a (Hilbert) polynomial
of the form dN ∼a0N m in the complex case (with m = dimCM) and by a function of polynomial growth
dN ∼a0N m−1 in the real case (with m = dimRM).
In our applications, the spaces HN will be one of the following.
2.1.1. Spherical harmonics and real eigenfunctions. We denote by ∆the standard Laplacian on Sm
and by HN(Sm) the space of spherical harmonics of degree N on Sm. They are the eigenfunctions of ∆of
eigenvalue λm,N = N(N+m−1) and form a real vector space of dimension dm,N = 2N+m−1
N+m−1


N + m −1
m −1

.
More generally, we may consider the Laplacian ∆of any compact Riemannian manifold (M, g). In place of
spherical harmonics of degree N, we partition the spectrum of
√
∆into intervals [N log N, (N +1) log(N +1)]
(the reason for the longer length is given in [Ze2]), and let HN denote the span of the eigenfunctions with
eigenvalues in the Nth interval. Linear combinations of such eigenfunctions are of course not eigenfunctions of
∆, but they behave like polynomials of degree N and their random linear combinations give a replacement for
random spherical harmonics. Their use for modelling quantum ergodic and quantum mixing eigenfunctions
is discussed [Ze2, HKZ].
2.1.2. Holomorphic sections of positive line bundles. For any K¨ahler manifold (M, ω) of complex dimen-
sion m there exists a holomorphic hermitian line bundle (L, h) →(M, ω) whose Ricci curvature Ric(h) = ω.
L is called positive since it posseses a metric of positive curvature, i.e. ω(X, JY ) deﬁnes a Riemannian
metric. We denote by LN the Nth power of L and by H0(M, LN) the space of holomorphic sections. Its
dimension dN = dimH0(M, LN) is given by the Hilbert polynomial dN = c1(L)m
m!
N m + · · · for suﬃciently
large N, where · · · represent the lower order terms. We equip M with the volume form dVω = ωm
m! and
H0(M, LN) with the inner product ||s||2 =
R
M h(s(z), s(z))dV. For background we refer to [GH].
In the simplest case of Riemann surfaces, examples include:
• M = CP1, L = O(1), L2 = T CP1, h = hF S, ω = ωF S (Fubini study hermitian metric and curvature
(1,1)-form). That (CP1, ωF S) is positively curved in the usual Riemannian sense is equivalent to posi-
tivity of T CP1. H0(CP1, O(2N)) may be interpreted as the space of holomorphic vector ﬁelds of type
( ∂
∂z)N. More simply put, sections are homogeneous holomorphic polynomials s = PN
j=0 ckzk
0zN−k
1
of
degree N in two complex variables. Such polynomials are known as the SU(2)-ensemble.
• M = H2/Γ, L = T ∗M, hF S = hyperbolic metric. Hyperbolic surfaces are negatively curved in the
Riemannian sense, so their tangent bundles are negatively curved, and their co-tangent bundles are
positively curved. Holomorphic sections are holomorphic diﬀerentials of type (dz)N.
• M = C/Z2, ω0 = dz ∧d¯z. The complex torus is ﬂat in the Riemannian sense, so neither its tangent
nor cotangent bundles are positively curved. The ‘quantizing line bundle’ with curvature ω0 is rather
FROM RANDOM POLYNOMIALS TO SYMPLECTIC
3
the bundle Θ whose sections are the classical theta-functions. The sections of ΘN are known as
theta-functions of level N.
2.1.3. Almost holomorphic sections. Symplectic almost-complex manifolds (M, J, ω) possess a similar
but analytically more complicated geometric quantization as spaces H0
J(M, LN) of ‘almost-holomorphic’
sections. They are deﬁned by a ¯D complex over the S1-bundle X due to Boutet de Monvel -Guillemin
[BoGu]. What we need to know about these spaces is that their orthogonal projectors ΠN have the same
scaling asymptotics as in the complex case, if one works in suitable (Heisenberg) coordinates [ShZe2].
2.2. Gaussian measures and spherical measures. We will restrict attention to two related ensem-
bles:
• Gaussian ensembles: We ﬁx an orthonormal basis {fj} of HN and write functions as orthonormal
sums f = PdN
j=1 cjfj. We then deﬁne the (complex) Gaussian measure by
γ = e−||f||2Df, i.e. γ = e−|c|2dc.
More generally we ﬁx a symmetric matrix ∆on CdN with positive (semi-)deﬁnite imaginary part and
deﬁne:
γ∆=
e−⟨∆−1c,c⟩
(2π)p/2 det ∆dc ,
(1)
Gaussian ensembles come in both real and complex ﬂavors. In the real case, the exponents acquire
factors of 1/2 and the denominator acquires a square root.
• Spherical ensembles: We denote by SHN = {f ∈HN : ||f|| = 1}. We then equip SHN with the
uniform (Haar) probability measure νN.
We will denote the expected value of a random variable X with respect to the Gaussian ensemble by
Eγ(X) (resp. Eν(X) for the spherical ensemble).
These two ensembles are equivalent in the sense that the two large dimension limits give equivalent
results when scaled properly. A more precise formulation goes as follows:
Let TN : RdN →Rk, N = 1, 2, . . ., be a sequence of linear maps, where dN →∞.
Suppose that
1
dN TNT ∗
N →∆. Then TN∗νdN →γ∆.
2.3. Sequences of random polynomials. We are often interested in sequences of polynomials {sN}
chosen independently and at random from HN from either a Gaussian or spherical ensemble. We thereform
form the product probability space (H∞, µ∞), deﬁned by
H∞= H1 × H2 × · · · × HN × · · · ,
µ∞= ×∞
N=1µN, (µN = γN or νN).
When we say that a sequence of polynomials {sN} of increasing degerees does something almost surely, we
mean that the set of such sequences has measure one in this product ensemble.
2.4. Szeg¨o kernels. Our results depend on the fact that certain statistical properties of polynomials
can be expressed in terms of the reproducing kernels ΠN(x, y) (orthogonal projections) of the Hilbert spaces
HN. They are known as Szego kernels, and are essentially the same as the ‘coherent states’ of the physics
literature. The local structure of the Szeg¨o kernel is given by the following scaling asymptotics:
Theorem 2.1. As N →∞, we have:
• [BSZ2, ShZe2] Complex case:
ΠN(z0 +
u
√
N
, θ
N , z0 +
v
√
N
, ϕ
N ) ∼
1
πm ei(θ−ϕ)eu·¯v−1
