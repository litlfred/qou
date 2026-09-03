---
doc_id: arxiv-2103.00651v1
doc_title: "On Concentration Inequalities for Vector-Valued Lipschit z Functions Dimitrios Katselis katselis@illinois.edu"
section_id: sec-002-3-proof-of-theorem-1-and-additional-results
section_title: "Proof of Theorem 1 and Additional Results"
section_number: 3
pages: 3-5
source_pdf: 2103.00651v1.pdf
source_sha256: c5505d3e4891168e
doc_brief: "On Concentration Inequalities for Vector-Valued Lipschit z Functions Dimitrios Katselis katselis@illinois.edu — We derive two upper bounds for the probability of deviation of a vect or-valued"
---
Proof of the ﬁrst bound in (2) : The proof of the ﬁrst bound relies on covering arguments;
see Vershynin (2018); Wainwright (2019); Lattimore and Sze pesv´ ari (2020) and references
therein for results based on such arguments. For some ε in the interval (0 , 1], let N (ε) be an
ε-net of the unit Euclidean sphere Sk−1 in Rk with cardinality |N (ε)| ≤
(
1 + 2
ε
)k Vershynin
(2018). Additionally, by Exercise 4.4.2 in Vershynin (2018 ),
‖f (X) − Eν [f (X)]‖2 ≤ 1
1 − ε sup
w∈N (ε)
⟨w, f (X) − Eν[f (X)]⟩ a.s. (5)
By (5) and by Boole’s inequality (union bound) we have that
P (‖f (X) − Eν [f (X)]‖2 ≥ ǫ) ≤ P
(
sup
w∈N (ε)
⟨w, f (X) − Eν[f (X)]⟩ ≥ ǫ(1 − ε)
)
≤
∑
w∈N (ε)
P (⟨w, f (X) − Eν [f (X)]⟩ ≥ ǫ(1 − ε))
≤ |N (ε)| inf
λ>0
e−λǫ(1−ε)Eν
[
eλ⟨w∗,f (X)−Eν [f (X)]⟩
]
, (6)
3
where the last inequality follows from the Chernoﬀ bound Rag insky and Sason (2014) and
w∗ = arg max
w∈N (ε)
P (⟨w, f (X) − Eν [f (X)]⟩ ≥ ǫ(1 − ε)) .
We now note that the function ⟨w∗, f(x) − Eν [f (X)]⟩ is ‖f ‖Lip-Lipschitz by the Cauchy—
Schwarz inequality and ⟨w∗, f(X) − Eν[f (X)]⟩ is mean zero. Assuming that W1(µ, ν) ≤√
2σ2D(µ‖ν), ∀µ holds, an application of the theorem of Bobkov and G¨ otze imp lies that
P (‖f (X) − Eν[f (X)]‖2 ≥ ǫ) ≤ |N (ε)| inf
λ>0
e−λǫ(1−ε)+
λ2σ2‖ f ‖ 2
Lip
2 . (7)
The exponent in the right-hand side of (7) is minimized for λ∗ = ǫ(1−ε)
σ2‖f ‖2
Lip
> 0 leading to
P (‖f (X) − Eν[f (X)]‖2 ≥ ǫ) ≤ |N (ε)|e
− ǫ2(1−ε)2
2σ2‖ f ‖ 2
Lip . (8)
By employing the bound on |N (ε)| the desired result follows.
Proof of the second bound in (2) : Using a similar argument as in Hsu et al. (2012),
let Z ∼ N (0, Ik) be a standard Gaussian random vector, which is independent of X. Recall
that E[e⟨Z,q⟩] = e
‖ q‖ 2
2
2 , ∀q ∈ Rk. For any λ ∈ R we note that
E
[
eλ⟨Z,f (X)−Eν [f ]⟩
]
≥
E
[
eλ⟨Z,f (X)−Eν [f ]⟩
⏐⏐⏐‖f (X) − Eν [f (X)]‖2 ≥ ǫ
]
P (‖f (X) − Eν[f (X)]‖2 ≥ ǫ) =
Eν
[
EZ
[
eλ⟨Z,f (X)−Eν [f ]⟩
] ⏐⏐⏐‖f (X) − Eν[f (X)]‖2 ≥ ǫ
]
P (‖f (X) − Eν[f (X)]‖2 ≥ ǫ) =
Eν
[
e
λ2‖ f (X)−Eν [f ]‖ 2
2
2
⏐⏐⏐⏐‖f (X) − Eν[f (X)]‖2 ≥ ǫ
]
P (‖f (X) − Eν[f (X)]‖2 ≥ ǫ) ≥
e
λ2ǫ2
2 P (‖f (X) − Eν [f (X)]‖2 ≥ ǫ)
or
P (‖f (X) − Eν[f (X)]‖2 ≥ ǫ) ≤ e− λ2ǫ2
2 E
[
eλ⟨Z,f (X)−Eν [f ]⟩
]
. (9)
We now note that the function ⟨Z, f(x)−Eν [f (X)]⟩ is ‖Z‖2‖f ‖Lip-Lipschitz when Z is ﬁxed
(by the Cauchy—Schwarz inequality) and ⟨Z, f(X) − Eν [f (X)]⟩ is mean zero. Assuming
that W1(µ, ν) ≤
√
2σ2D(µ‖ν), ∀µ holds, an application of the theorem of Bobkov and G¨ otze
implies that
E
[
eλ⟨Z,f (X)−Eν [f ]⟩
]
= EZ
[
Eν
[
eλ⟨Z,f (X)−Eν [f ]⟩
]]
≤ EZ
[
e
λ2‖ Z‖ 2
2σ2‖ f ‖ 2
Lip
2
]
.
Moreover, ‖Z‖2
2 is a chi-squared random variable with k degrees of freedom and for such a
random variable E
[
et‖Z‖2
2
]
= 1
(1−2t)k/2 , t < 1
2 . Therefore, we conclude that
E
[
eλ⟨Z,f (X)−Eν [f ]⟩
]
≤ EZ
[
e
λ2‖ Z‖ 2
2σ2‖ f ‖ 2
Lip
2
]
= 1
(
1 − λ2σ2‖f ‖2
Lip
)k/2 , (10)
4
where the last equality holds for any λ ∈ R such that λ2σ2‖f ‖2
Lip < 1. By combining (9)
and (10) we obtain
P (‖f (X) − Eν [f (X)]‖2 ≥ ǫ) ≤ e− λ2ǫ2
2
(
1 − λ2σ2‖f ‖2
Lip
)k/2 , |λ| < 1
σ‖f ‖Lip
. (11)
Choosing λ = 1√
2σ‖f ‖Lip
, we conclude that
P (‖f (X) − Eν[f (X)]‖2 ≥ ǫ) ≤ 2
k
2 e
− ǫ2
4σ2‖ f ‖ 2
Lip . (12)
□
In the previous proof and more speciﬁcally in (7) and (10), th e theorem of Bobkov and
G¨ otze for the mean zero, vector-valued function f (X) − Eν[f (X)] has been applied via a
real-valued function of the form ⟨g, f (X) − Eν[f (X)]⟩ with g = w∗ and g = Z, respectively.
This suggests the following extension of the theorem of Bobk ov and G¨ otze for vector-valued
Lipschitz functions:
Proposition 1 (Theorem of Bobkov and G¨ otze for Vector-Valued Functions) Let
(X, dX) and (Y, dY) be two Polish spaces, where Y ⊆ Rk and dY is an ℓp-metric for some
p ≥ 1. Let X be a random variable taking values in X and assume that X ∼ ν, where ν is
a probability measure on (X, dX). Then, the following statements are equivalent:
1. W1(µ, ν) ≤
√
2σ2D(µ‖ν), ∀µ
2. f (X) − Eν [f (X)], for every function f ∈ Lip(X, Y, dX, dY) such that ‖Eν[f ]‖∞ < ∞,
is a sub-Gaussian vector with σ2‖h‖2
q ‖f ‖2
Lip-sub-Gaussian one-dimensional marginals
⟨h, f(X) − Eν[f (X)]⟩, i.e.,
Eν
[
eλ⟨h,f (X)−Eν [f (X)]⟩
]
≤ e
λ2‖ h‖ 2q σ2‖ f ‖ 2
Lip
2 , ∀h ∈ Rk, ∀λ ∈ R. (13)
Here, ‖ · ‖q corresponds to the dual norm of ‖ · ‖p.
The direction “1 . implies 2.” can be obtained by the theorem of Bobkov and G¨ otze for
the real-valued function ⟨h, f(x) − Eν[f (X)]⟩ by invoking H¨ older’s inequality to show that
the corresponding Lipschitz constant is at most ‖h‖q‖f ‖Lip. The direction “2 . implies 1.”
is a direct consequence of the theorem of Bobkov and G¨ otze by choosing f to have only
one nonzero coordinate, e.g., f = ˜f e1 and h = e1. Here, ˜f : X → R is any real-valued
‖f ‖Lip-Lipschitz function and e1 is the ﬁrst element of the canonical basis in Rk.
