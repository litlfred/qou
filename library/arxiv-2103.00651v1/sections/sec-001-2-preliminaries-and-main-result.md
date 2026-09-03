---
doc_id: arxiv-2103.00651v1
doc_title: "On Concentration Inequalities for Vector-Valued Lipschit z Functions Dimitrios Katselis katselis@illinois.edu"
section_id: sec-001-2-preliminaries-and-main-result
section_title: "Preliminaries and Main Result"
section_number: 2
pages: 2-3
source_pdf: 2103.00651v1.pdf
source_sha256: c5505d3e4891168e
---
Let (X, dX) be a Polish space and ρ be a (Borel) probability measure on ( X, dX). The triplet
(X, dX, ρ) deﬁnes a metric probability space in the sense of Gromov Rag insky and Sason
(2014), Gromov (2007). Given two metric spaces ( X, dX) and (Y, dY), let f : X → Y be a Lip-
schitz mapping with Lipschitz constant ‖f ‖Lip, i.e., dY(f (x), f(˜x)) ≤ ‖f ‖LipdX(x, ˜x), ∀x, ˜x ∈
X. In the following, the set of all such mappings will be denote d by Lip( X, Y, dX, dY). More-
over, let P1(X) denote the set of all probability measures ρ on X such that Eρ[dX(X, x0)] < ∞
holds for an arbitrary (and therefore for all) x0 ∈ X. The L1 Wasserstein distance between
ρ, ˜ρ ∈ P1(X) is deﬁned as
W1(ρ, ˜ρ) = inf
X∼ρ, ˜X∼˜ρ
E[dX(X, ˜X)] = inf
γ∈Π( ρ,˜ρ)
∫
X×X
dX(x, ˜x)γ(dx, d˜x). (1)
The inﬁmum in the ﬁrst part is taken over all jointly distribu ted pairs (X, ˜X) on the product
space X2 = X × X with marginals ρ, ˜ρ, respectively. In the last part, Π( ρ, ˜ρ) denotes the set
of all possible couplings of ρ, ˜ρ. An optimal coupling γ∗ ∈ Π( ρ, ˜ρ) achieving the inﬁmum
exists Raginsky and Sason (2014), Villani (2008). Addition ally, a diﬀerent measure gauging
the dissimilarity between two probability measures ρ, ˜ρ is the relative entropy or Kullback-
Leibler divergence D(˜ρ‖ρ) = E˜ρ
[
log d˜ρ
dρ
]
= Eρ
[
d˜ρ
dρ log d˜ρ
dρ
]
for ˜ρ ≪ ρ and D(˜ρ‖ρ) = ∞
2
otherwise, where d˜ρ/dρ is the Radon-Nikodym derivative of ˜ρ with respect to ρ and ˜ρ ≪ ρ
denotes that ˜ρ is absolutely continuous with respect to ρ.
The following theorem provides a concentration inequality for f (X) when the deviation
from Eν[f (X)] is measured in terms of the ℓ2-metric.
Theorem 1 Let (X, dX) and (Y, dY) be two Polish spaces, where Y ⊆ Rk and dY(y, ˜y) =
‖y − ˜y‖2 with ‖ · ‖ 2 being the Euclidean norm. Let X be a random variable taking values
in X and assume that X ∼ ν, where ν is a probability measure on (X, dX). Then, the
inequality W1(µ, ν) ≤
√
2σ2D(µ‖ν), ∀µ implies that ∀ǫ > 0, ∀ε ∈ (0, 1] and for any f ∈
Lip(X, Y, dX, ‖ · ‖2) such that ‖Eν [f ]‖∞ < ∞,
P (‖f (X) − Eν[f (X)]‖2 ≥ ǫ) ≤ min
{(
1 + 2
ε
)k
e
− ǫ2(1−ε)2
2σ2‖ f ‖ 2
Lip , 2
k
2 e
− ǫ2
4σ2‖ f ‖ 2
Lip
}
. (2)
The proof of this theorem is provided in Section 3. This resul t can be straightforwardly
extended to any ℓp-metric for p ≥ 1, p ⁄= 2. Deﬁne
τp = sup
y∈f (X)
‖y − Eν[f (X)]‖p
‖y − Eν[f (X)]‖2
. (3)
Here, y is assumed diﬀerent from Eν[f (X)] if Eν [f (X)] ∈ f (X), since for y = Eν[f (X)] (if
Eν[f (X)] ∈ f (X)) the inequality ‖y − Eν[f (X)]‖p ≤ τp‖y − Eν [f (X)]‖2 trivially holds for
any τp > 0. Then, (2) can be replaced by
P (‖f (X) − Eν[f (X)]‖p ≥ ǫ) ≤ min
{(
1 + 2
ε
)k
e
− ǫ2(1−ε)2
2τ 2p σ2‖ f ‖ 2
Lip , 2
k
2 e
− ǫ2
4σ2τ 2p ‖ f ‖ 2
Lip
}
(4)
due to {‖f (X) − Eν [f (X)]‖p ≥ ǫ} ⊆ {‖ f (X) − Eν[f (X)]‖2 ≥ ǫ/τp} by (3).
