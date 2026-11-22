---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-017-43-number-of-disjoint-cycles-of-a-random-permuta
section_title: "Number of disjoint cycles of a random permutation"
section_number: 4.3
pages: 45-48
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
In this section, we study the number ℓn of disjoint cycles of a random
permutation σn ∈Sn. If the permutation σn is chosen according to the uni-
form probability measure (Example 1.6), then the discussion of Section 4.1
applies, with the parameters pj taken equal to 1
j , and
λn =
n
X
j=1
1
j = Hn ≃log n;
+∞
X
j=n+1
(pj)2 ≃1
n = o

1
(λn)r

for every r ⩾0.
Therefore, if one looks for instance at the derived scheme with constant
residue from the approximation scheme of order r = 2:
d
σ(2)
n (ξ) = eHn(eiξ−1)

1 −π2
12 (eiξ −1)2

then
dL(ℓn, σ(2)
n ) =
(
√
6 −2) ζ(3)
p
2π e3−
√
6 (log n)2 + o

1
(log n)2

,
and one has similar estimates for the Kolmogorov distance and for the total
variation distance.
One can extend this result to more general models of random permuta-
tions, namely, random permutations σn ∈Sn under the so-called general-
ized weighted measures
PΘ,n[σn] =
1
n! hn(Θ)
n
Y
k=1
(θk)mk(σn),
where Θ = (θk)k⩾1 is a sequence of non-negative parameters, mk(σ) is the
number of cycles of length k in σ ∈Sn, and hn(Θ) is the normalization con-
stant so that each PΘ,n is a probability measure on Sn. If Θ = (θ, θ, . . .) is
a constant sequence, then one recovers the Ewens measures of parameter θ:
Pn[σn] =
θℓ(σn)
θ(θ + 1) · · · (θ + n −1).
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1159
The generalized weighted measures have been studied previously in [10,
11, 12, 24, 46], and they are related to the quantum Bose gas of statistical
mechanics. Denote as before ℓn = ℓ(σn) = Pn
k=1 mk(σn) the number of
disjoint cycles of a random permutation under the measure PΘ,n. We also
introduce the generating series of the parameter Θ:
gΘ(z) =
∞
X
k=1
θk
k zk.
Note that exp(gΘ(z)) = P∞
n=0 hn(Θ) zn is the generating series of the par-
tition functions of the models.
If Θ is the constant sequence equal to θ, then gΘ(z) = θ log(
1
1−z). On the
other hand, in this setting, one can represent ℓn as a sum of independent
Bernoulli variables (Feller coupling):
ℓn =
n
X
j=1
B

θ
θ + j −1

.
We can then use the discussion of Section 4.1, and the mod-Poisson conver-
gence of (ℓn)n∈N with parameters λn = Pn
j=1
θ
θ+j−1 ≃θ log n and limiting
residue
ψ(ξ) =
∞
Y
j=1

1 +
θ
θ + j −1 (eiξ −1)

e−
θ
θ+j−1 (eiξ−1) = eγθ(eiξ−1) Γ(θ)
Γ(θeiξ).
The last formula relies on the inﬁnite product representation
1
Γ(z+1) =
eγz Q∞
k=1(1 + z
k) e−z
k .
More generally, the article [46] shows that if one has a good understand-
ing of the analytic properties of the generating series gΘ(z), then one can
establish the mod-Poisson convergence of (ℓn)n∈N, with a limiting residue
ψ(ξ) similar to the previous expressions. Thus:
Theorem 4.2 ([46, Lemma 4.1]). — Assume that gΘ(z) is holomorphic
on a domain
∆0(r, R, φ) = {z ∈C, |z| < R, z̸ = r, |arg(z −r)| > φ}
with 0 < r < R and φ ∈(0, π
2 ), see Figure 4.1.
Suppose moreover that the singularity of gΘ at z = r is logarithmic:
gΘ(z) = θ log

1
1 −z
r

+ K + O(|z −r|).
Then, one has the asymptotics
EΘ,n

ezℓn
= e(θ log n+K)(ez−1)
 Γ(θ)
Γ(θez) + O
 1
n

,
TOME 70 (2020), FASCICULE 3
1160
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
R
0
r
φ
Figure 4.1. Domain of analyticity of the generating series gΘ(z).
with a uniform remainder on compact subsets of C. Hence, (ℓn)n∈N con-
verges mod-Poisson with parameters λn = θ log n + K and limit
ψ(ξ) =
Γ(θ)
Γ(θeiξ).
Moreover, the convergence of residues ψn →ψ happens in every space C r,
with a norm ∥ψn −ψ∥C r which is each time O( 1
n).
Note that the last part of the theorem (convergence in every space C r)
is an immediate consequence of the estimate of EΘ,n[ezℓn], and of the ana-
lyticity of all terms in
EΘ,n[eiξℓn] e−(θ log n+K)(eiξ−1) = ψn(ξ).
On the other hand, in the case of the Ewens measure, one has K = 0 and
r = 1, and in the case of the uniform measure, one has moreover θ = 1.
Because of the inﬁnite product representation of
Γ(θ)
Γ(θeiξ), one can restate
Theorem 4.2 as follows. If one looks at a generalized weighted measure with
a generating series gΘ(z) that satisﬁes the hypotheses of Theorem 4.2, then
E[eiξℓn]
= e(θ(log n+γ)+K)(eiξ−1)


∞
Y
j=1

1 + θ(eiξ −1)
θ + j −1

e−θ(eiξ−1)
θ+j−1 + O
 1
n

.
Therefore, in this setting, one can deal with the asymptotics of (ℓn)n∈N in
the same way as in Section 4.1, but with parameters λn = θHn + K, and
(Θ)
p1(Θ) = 0 ;
pk⩾2(Θ) =
∞
X
j=1

θ
θ + j −1
k
.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1161
Thus, one has the following:
Theorem 4.3. — We consider a generalized weighted measure PΘ,n,
with a generating series gΘ(z) which satisﬁes the hypotheses of Theo-
rem 4.2. For any r ⩾1, we introduce the scheme of approximation (σ(r)
n )n∈N,
deﬁned by the Fourier transforms
d
σ(r)
n (ξ) = e(θHn+K)(eiξ−1)
 r
X
k=0
ek(Θ) (eiξ −1)k
!
,
where Θ is the specialisation of Sym speciﬁed by Equation (Θ). Note that
the residue is equal to 1 for r = 1 (basic scheme of approximation). One
has the asymptotics:
dL(ℓn, σ(r)
n ) = |er+1(Θ) Gr+1(zr+2)|
√
2π (θ log n)
r
2 +1
+ o

1
(log n)
r
2 +1

;
dK(ℓn, σ(r)
n ) = |er+1(Θ) Gr(zr+1)|
√
2π (θ log n)
r+1
2
+ o
 
1
(log n)
r+1
2
!
;
dTV(ℓn, σ(r)
n ) =
R
R |er+1(Θ) Gr+1(α)| dα
√
2π (θ log n)
r+1
2
+ o
 
1
(log n)
r+1
2
!
.
