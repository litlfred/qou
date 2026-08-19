---
doc_id: arxiv-2208.14188v2
doc_title: "Prepared for submission to JHEP KIAS-P22064 Resurgence in complex Chern-Simons theory at generic levels Zhihao Duana Jie Gub aKorea Institute for Advanced Study 85 Hoegiro, Dongdae"
section_id: sec-003-22-resurgent-structure-of-complex-chern-simons-t
section_title: "Resurgent structure of complex Chern-Simons theory"
section_number: 2.2
pages: 10-15
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels Zhihao Duana Jie Gub aKorea Institute for Advanced Study 85 Hoegiro, Dongdaemun-gu, Seoul 02455, Korea bSchool of Phyiscs and Shing-Tung Yau"
---
The power series ϕ(k,σ∗)
γ (u,n ;τ) are asymptotic. To make sense of them, we need to apply
the resurgence theory [39, 40] (see reviews [41–43] by physicists). Generically in physics
perturbation series are asymptotic. The coeﬃcients grow factorially due to the proliferation
of Feynman diagrams2,
f(τ) =
∞∑
𝓁=0
anτn, a n∼O (Ann!). (2.40)
The series is divergent and it cannot be summed to an exact ﬁnite value in the traditional
sense. Nevertheless, we can convert it into an analytic function of τ by the means of Borel
resummation.
2Renormalons can also contribute to factorial growth of coeﬃcients in a general QFT, but they are
absent in complex Chern-Simons theory.
– 9 –
We ﬁrst construct the Borel transform of the original series
B[f](t) =
∞∑
𝓁=0
an
n!tn, (2.41)
which is now a convergent series with a ﬁnite radius of convergence 1 /A. The boundary
of the disk of convergence is punctuated by singular points. If the singular points are
sparse, the convergent series can be analytically continued to the entire complex plane,
known as the Borel plane. The Borel transform is said to be resurgent if its singular points
are isolated and it can be analytically continued to inﬁnity in all directions bypassing its
singular points. In this case, we can perform the Laplace transform and deﬁne the Borel
resummation
s[f](τ) =
∫ ∞
0
B[f](τt)e−tdt. (2.42)
This deﬁnition involves integration along a rayρθ of angleθ = argτ. If the Borel transform
has no singular points along the ray, the integral is well-deﬁned and it gives us a function
of τ. If, however, the Borel transform does have a singular point w on the ray ρθ, the
integration is obstructed, and we are missing non-perturbative corrections of the order
e−w/τ coming from another saddle point, and the action of the new saddle point is Vw =
V0 +w, where V0 is the action at the original saddle point associated to the series f we
start with. We can deﬁne a pair of lateral Borel resummations
s±[f](τ) =
∫ e±i0∞
0
B[f](τt)e−tdt, (2.43)
and their diﬀerence, called the Stokes discontinuity
discθ[f](τ) =s+[f](τ)−s−[f](τ), (2.44)
is of the order e−w/τ .
The Borel transform B[f] is in addition called a simple resurgent function if all its
singular points are simple poles or branch points. In this paper, we assume there are only
logarithmic branch points. Then at the vicinity of a singular point at w, the resurgent
functionB[f](t) has the form
B[f](t +w) =−Sw
2πiB[g](t) log(t) + reg(t). (2.45)
where bothB[g](t) and reg(t) are regular at t = 0, and the constantSw is called the Stokes
constant. Here we make it manifest that the regular functionB[g](t) can be regarded as the
Borel transform of another asymptotic series g(τ), which in fact is the perturbation series
at the new saddle point w. Suppose no other singular points of B[f](t) share the same
argumentθ = argw, the Stokes discontinuity of the original Borel resummation across the
Stokes ray ρθ is
discθ[f](τ) =Swe−w/τs−[g](τ). (2.46)
To put it in a more democratic form, we can introduce elementary trans-series
F (τ) = e−V0/τf(τ), G (τ) = e−Vw/τg(τ). (2.47)
– 10 –
S01 S12
S21
S23
S32
S31
0
1
2
3
Figure 1: Demonstration of resurgent structure.
Then the formula of Stokes discontinuity reads
discθ[F ](τ) =s+[F ](τ)−s−[F ](τ) =Sws−[G](τ). (2.48)
Abstractly, it can also be represented as a linear transformation of trans-series, whose
coeﬃcient is the Stokes constant,
SθF =F +SwG. (2.49)
This is called the Stokes automorphism.
In summary, starting from a single perturbation series ϕ0 in a theory, one can ﬁnd
new saddle points and their actions by looking for singular points of the Borel transform
B[ϕ0], and furthermore explore the asymptotic series associated to the new saddle points
by computing the Stokes discontinuity (or expansion of Borel transform at the singular
point) ofϕ0. The same procedure can be repeated on the new asymptotic series to uncover
additional saddle points. In general, all the saddle points of the theory are interconnected in
this way, which is called the resurgent structure of the theory, cf. Fig.1. These relationships
are completely controlled by Stokes constants, which deﬁne for us new invariants of the
theory. We note that Stokes constants are not necessarily symmetric, i.e. Sij⁄=Sji.
In practise we usually do not have the entire asymptotic series f(τ) but only the
truncated power series up to certain (relatively high) order. The Borel transform of the
truncated power series is only a polynomial which has no poles. In order to mimic the
singularity structure of the Borel transform of the full series, we make use of the Pad´ e
approximant to approximateB[f](t),
PN[f](t) = p0 +p1t +··· +pNtN
1 +q1t +··· +qNtN . (2.50)
pi and qi are determined by requiring that the power series expansion of PN[f](t) in t
coincides with B[f](t) up to order 2 N. Thus the poles of PN[f](t) can be used to infer
the singularities of the Borel transform. Then we numerically Laplace transform the Pad´ e
approximant to obtain the Borel resummation. The precision of the Pad´ e approximant
can be improved by utilizing, say, the conformal mapping method. One can ﬁnd more
numerical techniques in [44].
Suppose that the theory in question has ﬁnitely many saddle points σi, with the asso-
ciated trans-series
Fi(τ) = e−Vi/τfi(τ), i = 1,...,r. (2.51)
– 11 –
We represent all the trans-series at once by an r-dimensional vector F (τ)
F (τ) =


F1(τ)
...
Fr(τ)

. (2.52)
If saddle point j appears as a singular point at Vj−Vi of the Borel transform of Fi(τ) and
the Stokes constant is Sij, and it is the only singular point on the Stokes ray ρθij where
θij = arg(Vj−Vi), then the Borel resummation above and below ρθij are related by the
Stokes automorphism
s+[F ](τ) = Sθijs−[F ](τ), (2.53)
where Sθij is an r×r matrix called the Stokes matrix, and it has the form
Sθij =I +SijEij (2.54)
withI the identity matrix, and Ei,j the elementary matrix with (i,j )-entry 1 and all other
entries zero.
If there are multiple singular points on the ray ρθ, we assume the locality condition:
the Stokes matrices of any two Borel plane singular points commute if they are on the same
Stokes ray. In this case, (2.53) should be generalised to
s+[F ](τ) = Sθs−[F ](τ), Sθ =
∏
argι=θ
Sι. (2.55)
The order of the product of the local Stokes matrices is irrelevant due to the locality
condition. Furthermore, given two raysρθ+ andρθ− whose arguments satisfy 0<θ +−θ−≤
π, we deﬁne the global Stokes automorphism
sθ+[F ](τ) = Sθ−→θ+sθ−[F ](τ) (2.56)
where both sides should be analytically continued to the same value ofτ. The global Stokes
automorphism Sθ−→θ+ has the property of unique factorisation
Sθ−→θ+ =
←∏
θ−<θ<θ+
Sθ. (2.57)
The superscript← indicates that the product is ordered so that θ increases from right to
left.
We can apply this theory to the trans-series Φ(k,σi)
γ (u,n ;τ) with (i = 1,...,r ) in (2.32)
coming from the state integral of sl(2, C) Chern-Simons theory. We also deﬁne the vector
of trans-series
Φ(k)
γ (u,n ;τ) =


Φ(k,σ1)
γ
...
Φ(k,σr)
γ

 (u,n ;τ). (2.58)
– 12 –
We will be concerned with the regime where |u|≪ 1, which is equivalent to |x|∼ 1. We
note that in this regime both holonomy parameters (u,n ) can be read oﬀ uniquely from x:
u is given by
u = log(xk), (2.59)
after which n∈ Zk is chosen such that
ζnx = eu. (2.60)
The Borel transformB[Φ(k,σi)
γ ](u,n ;t) has singularities at
Λ(k),0
i ={ιi,j/k|j = 1,...,r, j ⁄=i} (2.61)
where
ιi,j = U0,0(σi)−U0,0(σj)
2πi . (2.62)
They correspond to the ﬂat connections j ⁄= i as predicted by the resurgence theory.
Furthermore, there are additional singularities on top of and slightly away from these
singular points and on the imaginary axis as well; the full set of singular points is
Λ(k)
i =
{
ιi,j + 2πi𝓁 + log(xk)m
k
⏐⏐⏐j = 1,...,r, 𝓁 ∈
{
Z j⁄=i
Z⁄=0 j =i
, m∈I(i,j,𝓁 )
}
. (2.63)
Here I(i,j,𝓁 ) are ﬁnite and continuous sets of integers centered on 0. These singularities
form inﬁnite towers in the imaginary direction (see Figs. 2, 5 for illustrations), and the
Stokes rays passing through them are said to form “peacock patterns” [31]. This type
of distribution of Borel plane singularities is in fact quite univeral. Similar patterns have
already been seen in largeN expansion of Chern-Simons matrix integral [45, 46], in closedly
related topological string free energies [47–50], in earlier studies of complex Chern-Simons
theory [23], and in other related works [30]. In the context of complex Chern-Simons theory,
this reﬂects the fact that due to ambiguity of the Chern-Simons action 3, each trans-series
Φ(k,σi)
γ (u,n ;τ) should be upgraded to a family of trans-series with the same power series
but with shifted instanton action. Recall the deﬁnition
˜q = exp
(
−2πi
kτ − 2πi
k
)
, ˜x = exp
(log(xk)
kτ + 2πin
k
)
. (2.64)
It is convenient to parametrise the trans-series in each family as
Φ(k,σi)𝓁,m
γ (u,n ;τ) = ˜xm˜q𝓁Φ(k,σi)
γ (u,n ;τ), 𝓁,m ∈ Z. (2.65)
On the other hand, the Stokes constant that relates two trans-series labelled by ( σi)𝓁,m
and (σj)𝓁′,m′ only depends on σi,σj and the diﬀerences 𝓁−𝓁′, m−m′, and we denote it
bySi,j;𝓁−𝓁′,m−m′. As a consequence, we only need to study the resurgent properties of the
3For instance by a large gauge transformation the Chern-Simons action changes by 2π. This will change
the complexiﬁed hyperbolic volume U0,0/(2πi) in (2.38), whose imaginary part is the Chern-Simons action.
– 13 –
vector of trans-series Φ (k)
γ (u,n ;τ) deﬁned in (2.58). The Stokes automorphism associated
to the Borel plane singularity ιi,j;𝓁,m/k = (ιi,j + 2πi𝓁 + log(xk)m)/k is given by
s+[Φ(k)
γ ](u,n ;τ) = Sιi,j;𝓁,m/k(˜x, ˜q)s−[Φ(k)
γ ](u,n ;τ) (2.66)
where the Stokes matrix is
Sιi,j;𝓁,m/k(˜x, ˜q) =I +Si,j,𝓁,m˜xm˜q𝓁Ei,j. (2.67)
Due to the factorisation property (2.57), in order to compute all the Stokes constants,
it suﬃces to compute a suitable choice of ﬁnite number of global Stokes automorphisms,
and extract the Stoks constants from their factorised form. For instance we can choose to
compute
S(k)
+ (˜x, ˜q) = S(k)
0−→π+0−(˜x, ˜q), S(k)
− (˜x, ˜q) = S(k)
π+0−→2π+0−(˜x, ˜q). (2.68)
The entries of the global Stokes automorphisms are no longer constants, but elements in
Z[˜x±1][[˜q]] (upper half plane) or Z[˜x±1][[1/˜q]](lower half plane). See [24, 31] for concrete
examples.
In the case of the two simplest hyperbolic knots 41, 52, at level k = 1 and for|u|≪ 1,
the global Stokes automorphisms S(1)
± (˜x, ˜q) have been conjectured in [31, 32]. In this paper,
we generalise the studies of these two knots to generic level k≥ 1, and the main result of
this paper is that the Stokes automorphisms are independent of the level k
S(k)
± (˜x, ˜q) = S(1)
± (˜x, ˜q). (2.69)
This is rather surprising because the power seriesϕ(k,σ∗)
γ (u,n ;τ) are very diﬀerent at diﬀer-
ent levels. We will demonstrate the complexity of power series at higher levels and provide
numerical evidence of (2.69) in Sections 3, 4. But before ending this section, we give some
philosophical argument for (2.69). The following subsection is more speculative.
