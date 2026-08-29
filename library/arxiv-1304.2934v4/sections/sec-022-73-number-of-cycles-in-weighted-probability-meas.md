---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-022-73-number-of-cycles-in-weighted-probability-meas
section_title: "Number of cycles in weighted probability measure"
section_number: 7.3
pages: 55-58
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
ber of cycles of random permutations under the so-called weighted probability mea-
sure. This example was already considered in [NZ13] and we follow the presentation
of this article.
Denote Xn(σ) the number of disjoint cycles (including ﬁxed points) of a permutation
σ in the symmetric group S(n). We write Cj(σ) for the number of cycles of length j in
the decomposition of σ as a product of disjoint cycles; thus, Xn(σ) = ∑n
j=1 Cj(σ) and
n = ∑n
j=1 j Cj(σ). Let Θ = ( θm)m≥1 be given with θm≥ 0. The generalized weighted
measure is deﬁned as the probability measure PΘ on the symmetric group S(n):
PΘ[σ] = 1
hn n!
n
∏
m=1
(θm)Cm(σ)
with hn a normalization constant (or a partition function) and h0 = 1. This model is
coming from statistical mechanics and the study of Bose quantum gases (see [NZ13]
for more references and details). It generalizes the classical cases of the uniform mea-
sure (corresponding to θm ≡ 1) and the Ewens measure (corresponding to the case
θm≡ θ > 0). It has been an open question to prove a central limit theorem for the
total number of cycles Xn under such measures (or more precisely under some speciﬁc
regimes related to the asymptotic behavior of theθm’s; such a central limit theorem was
already known for Ewens measure). We refer to [EU14] for a nice survey of this ques-
tion. The difﬁculty comes from the fact the there is nothing such as the Feller coupling
anymore, and we cannot apply the same method as in Example 2.3. We now show how
singularity analysis allows us to prove mod-Poisson convergence, and hence the cen-
tral limit theorem, but also distributional approximations and precise large deviations.
56 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
We consider the generating series
gΘ(t) =
∞
∑
n=1
θn
n tn.
It is well known that
∞
∑
n=0
hn tn = exp(gΘ(t)). (35)
Set F(t, w) = exp(wgΘ(t)). Using elementary combinatorial arguments (which are
detailed in [NZ13]), one can prove for each z ∈ C the following identity as formal
power series:
∞
∑
n=0
hn EΘ[exp(zXn)] tn = exp(ezgΘ(t)) = F(t, ez). (36)
Our goal is to obtain an asymptotic for hn and for the moment generating function
of Xn. Note that in general (and unlike the case of Ewens measure), neither hn nor
EΘ[exp(zXn)] have a closed expression. Nevertheless, they correspond to the coefﬁ-
cient of tn in F(t, 1) (respectively F(t, ez)) and, thus, using Cauchy formula, they can
be expressed as a contour integral. The idea of singularity analysis is to choose the
contour in a clever way such that, asymptotically, the main part of this contour inte-
gral comes from the integral near the singularity. In this way, the integral depends
asymptotically only of the type of singularity of F(t, 1) (resp. F(t, ez)).
We note r the radius of convergence of gΘ(t). We need suitable assumptions on the
analyticity properties of g together with assumptions on the nature of its singularity at
the point r on the circle of convergence. This motivates the next deﬁnition:
Deﬁnition 7.16. Let 0 < r < R and 0 < φ < π/2 be given. We then deﬁne
∆0 = ∆0(r, R, φ) ={z∈ C;|z| < R, z⁄= r,| arg(z− r)| > φ},
see Figure 8. Assume we are further given g (t), θ≥ 0 and r > 0. We then say that g (t) is in
the classF (r, θ) if
(i) there exists R > r and 0 < φ < π/2 such that g(t) is holomorphic in ∆0(r, R, φ);
(ii) there exists a constant K such that
g(t) = θ log
( 1
1− t/r
)
+ K + O(t− r) as t→ r.
r
R
φ ∆0 = domain inside
the blue curve
12
FIGURE 8. Domain ∆0(r, R, φ).
MOD-φ CONVERGENCE, I 57
One readily notes that the generating series corresponding to the Ewens measure
(i.e. θm≡ θ) is of classF (1, θ) since in this case
gΘ(t)≡ θ log
( 1
1− t
)
.
Consequently our results will provide alternative proofs to this case as well. The next
theorem due to Hwang plays a key role in our example (we use the following notation:
if G(t) = ∑∞
n=0 gntn, we denote [tn][G]≡ gn the coefﬁcient of tn in G(t)).
Theorem 7.17 (Hwang, [Hwa94]). Let F(t, w) = exp(wg(t)) S(t, w) be given. Suppose
(i) g (t) is of classF (r, θ),
(ii) S (t, w) is holomorphic in a domain containing{(t, w)∈ C2; |t|≤ r,|w|≤ ˆr}, where
ˆr > 0 is some positive number.
Then
[tn][F(t, w)] = eKwnwθ−1
rn
(S(r, w)
Γ(θw) + O
( 1
n
))
uniformly for|w|≤ ˆr and with the same K as in the deﬁnition above.
The idea of the proof consists in taking a suitable Hankel contour and to estimate the
integral over each piece. There exist several other versions of this theorem where one
can replace log(1− t/r) by other functions and we refer the reader to the monograph
[FS09], chapter VI.5. As an application of Theorem 7.17, we obtain an asymptotic for
hn.
Lemma 7.18. Let θ > 0 and assume that gΘ(t) is of classF (r, θ). We then have
hn = eKnθ−1
rn Γ(θ)
(
1 + O
( 1
n
))
.
Proof. We have already noted that ∑∞
n=1 hntn = exp(gΘ(t)). We can apply Theorem
7.17 with g(t) = gΘ(t), w = 1 and S(t, w) = 1. □
Using identity (36) and Theorem 7.17, we can also obtain an asymptotic for the
Laplace transform EΘ[exp(wXn)]:
Theorem 7.19 (Nikeghbali-Zeindler, [NZ13]). If gΘ(t) is of classF (r, θ), then
EΘ[exp(zXn)] = nθ(ez−1)eK(ez−1)
( Γ(θ)
Γ(θez) + O
( 1
n
))
.
Consequently, the sequence (Xn)n∈N converges in the mod-Poisson sense, with parameters
tn = K + θ log n and limiting function ψ(z) = Γ(θ)
Γ(θez). The convergence takes place of the
whole complex plane with speed O(1/n).
Proof. An application of Theorem 7.17 yields
[tn][exp(ezgΘ(t))] = eKez
nezθ−1
rn
( 1
Γ(θez) + O
( 1
n
))
,
with O(·) uniform for bounded z∈ C. Now a combination of identity (36) and Lemma
7.18 gives the desired result. □
58 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
The above theorem not only implies the central limit theorem, but also Poisson ap-
proximations and precise large deviations. We only state here the precise large devia-
tion result which extends earlier work of Hwang in the case θ = 1 as a consequence of
Theorem 3.4 and refer to [NZ13] for the distributional approximations results.
Proposition 7.20 (Nikeghbali-Zeindler, [NZ13]). Let Yn = Xn− 1 and let x∈ R such that
tnx∈ N with tn = K + θ log n. We note k = tnx. Then
P[Yn = xtn] = e−tn (tn)k
k!
( Γ(θ)
x Γ(θx) + O
( 1
tn
))
.
In fact, an application of Theorem 3.4 would immediately yield an arbitrary long ex-
pansion for P[Yn = xtn] and also for P[Yn≥ xtn], since the speed of convergence is
fast enough.
Remark 7.21. Equations (35) and (36) ﬁt naturally in the framework of labelled combi-
natorial classes [FS09, Chapter II]: a permutation is a set of cycles and the weighted
exponential generating series of cycles is gΘ(t). Using this framework, one could give
a more general statement with the same proof. Let A be a (weighted) labelled com-
binatorial class and consider the class B = SET(A). We denote Xn the number of
components in a random element of size n ofB (the probability of taking an element
ofB being proportional to its weight). Assume that the generating series ofA is in the
classF (r, θ). Then (Xn)n∈N converges in the mod-Poisson sense as in Theorem 7.19.
We refer to [Hwa96, Section 4.1] for a similar discussion.
However, the hypothesis that the generating series of A is in the class F (r, θ) is
mainly natural in the case of cycles and permutations, which explains why we focused
on this example here.
Remark 7.22. Singularity analysis is closely related to the Selberg-Delange method used
in previous Section. In both cases we do not have a closed expression for the Laplace
transform of our variable, but for an appropriate sum of them — Dirichlet series for
arithmetic functions and exponential generating functions for cycles in weighted per-
mutations. From Perron’s or Cauchy’s formula, we get an integral formula for the
Laplace transform. Then choosing an appropriate integral contour allows to ﬁnd the
asymptotics. It is quite striking that these closely related methods both yield mod-
Poisson convergence. However, we are not aware of a way to bring both under one
roof.
