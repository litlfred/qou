---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-008-23-a-state-integral-basis
section_title: "A state integral basis"
section_number: 2.3
pages: 14-16
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜ no [ 9] that perturbative series associated with the hyperbolic knots 4 1 and 5 2 are resurgent and"
---
z+ coordinates. The following proposition shows that such classes gen erate the homology
H1(Σ , D∞,θ) of Equation (
55).
Proposition 2.6. Let ǫ, M > 0. A subset of the state integral contours ˜Jℓ,m,τ for|ℓ| < M
and m∈{ 0, . . . , A− 1} deﬁne a basis for H1(Xǫ,M , D∞,θ), where θ = arg(−1/τ )∈ (0, 2π).
Proof. By construction we ﬁnd that [ ˜Jℓ,m,τ ]∈ H1(Xǫ,M , D∞,θ), where |ℓ|≤ M. Recall, as
we show in the proof of Proposition 2.5, that for every L≥ M there is an isomorphism
H1(Xǫ,M , DL,θ)∼= H0(Σ +
ǫ,M∩ Σ −
ǫ,M ), which induces the isomorphism
H1(Xǫ,M , D∞,θ)∼
= H0(Σ +
ǫ,M∩ Σ −
ǫ,M ) (56)
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 15
as deduced from Equation ( 54). Then, through the isomorphism in Equation ( 56), the
contours [ ˜Jℓ,m,τ ] can be identiﬁed with the class of points [ pℓ,m]∈ H0(Σ +
ǫ,M∩ Σ −
ǫ,M ) for some
m = 0, . . . , A− 1 and|ℓ| < M . □
2.3.1. The class of the thimble Cp0,ϑ. We can now describe the class of the thimble Cp0,ϑ.
Lemma 2.7. If eiϑ /∈S (V0) and ϑ∈ ( π
2 , 3π
2 ), then there exists an M0 > 0 such that for
M > M 0 we have
[
Cp0,ϑ
]
∈ H1(Xǫ,M , D∞,θ), for all θ∈ (ϑ− π
2 , ϑ + π
2 ).
Proof. By Corollary 2.3, the thimbleCp0,ϑ has a smooth parametrization given by γ : R→ Σ.
In addition, from Corollary 2.3, there exists ǫ, M > 0 such that Cp0,ϑ⊂ Σ ǫ and for|z| > M
the tangent is approximated by Equation ( 33). Therefore using Equations ( 52), we see that
arg(i
√
ieiϑ)∈ arg(D+
∞,θ) , and arg
(
− i
√
ieiϑ|(A− B)|
A− B
)
∈ arg(D−
∞,θ) , (57)
for each θ∈ (ϑ− π
2 , ϑ + π
2 ). The proof by pictures is given in Figures 6 and 7. □
Figure 6. For−1/τ = eiϑ = eiθ, Re( τ ) > 0 and A− B < 0, these pictures
illustrate from left to right the regions near inﬁnity with exponential decay
D∞,θ in blue for Im( τ ) < 0, Im( τ ) = 0, and Im( τ ) > 0. A state integral
contour ˜J +
ℓ,m,τ is depicted in teal and the thimble Cp0,ϑ is depicted in orange.
Figure 7. This reproduces Figure 6 with the change A− B > 0.
We see that Lemma 2.7 and Proposition 2.6 imply the following corollary.
Corollary 2.8. If eiϑ /∈S (V0) and ϑ∈ ( π
2 , 3π
2 ), the thimble [Cp0,ϑ] can be written in terms
of a ﬁnite collection of state integral contours [ ˜Ji,m,τ ] for all τ∈ C\R≤0.
16 VERONICA F ANTINI AND CAMPBELL WHEELER
2.3.2. A mix of state integrals and steepest descent contours. It turns out that we are inter-
ested in more classes than just the steepest descent contours a nd the state integral contours.
Indeed, we want a combination of both. For a point p∈ Σ such that V (p)∈ V0−ieiϑR>0 +Z,
we can deﬁne an element of the homology H1(Σ , D∞,θ) from Equation (
55). We assume that
eiϑ /∈S (V0). For V (p) = V0− ieiϑλ + Z, we deﬁne γp,θ as follows (see also Figure 8):
Deﬁnition 2.9. For V (p) = V0− ieiϑλ + Z, the contour γp,θ is the curve that contains the
connected component of p in the set {r∈ Σ | V (r)∈ V0− ieiϑR≥λ + Z} union the straight
line in the direction eiθ/2−iAǫ for Im( z+(p)) > 0 and−eiθ/2−i(A−B)ǫR≤0 for Im( z+(p)) < 0.
One can see that γp,θ is a straight line connected to Γ p,θ from Deﬁnition 2.1. We call
the straight line segment a tail. Similarly, associated to any connected segment e⊆{ r∈
Σ| V (r)∈ V0− ieiϑR≥λ + Z} with boundary ∂e = p+∪ p− we can deﬁne the contour γe,θ as
follows (see also Figure 9):
Deﬁnition 2.10. Let γe,θ be the union of e and the straight lines in the direction eiθ/2−iAǫ
for Im( z+(p±)) > 0 and−eiθ/2−i(A−B)ǫR≤0 for Im( z±(p)) < 0.
Again we call the straight line segments tails. Essentially by deﬁnition, these contours give
elements of the homology H1(Σ , D∞,θ) from Equation ( 55), which is completely analogous
to the results of Corollary 2.8 and Lemma 2.7. One can see that at the level of homology
[γe,θ] = [ γp+,θ]− [γp−,θ]. Moreover, Lemma 2.7 and Proposition 2.6 imply the following
corollary:
Corollary 2.11. If eiϑ∈ C\S(V0), θ∈ (ϑ− π
2 , ϑ + π
2 ), p∈ Σ is such that V (p)∈ V0−
ieiϑR>0 + Z, and e⊆ Σ is a segment with V (e)⊆ V0− ieiϑR>0 + Z, then the contours [ γp,θ]
and [γe,θ] can each be written in terms of a ﬁnite collection of state integral c ontours [ ˜Ji,m,τ ].
In fact, for most choices of e and p we ﬁnd that [ γp,θ] = 0 and [ γe,θ] = 0. They can only
give rise to non-trivial classes when either the ﬂow from p crosses the reals or similarly when
e intersects the reals. For example, in Figure 8 we see that [ γp1,θ] = 0 and in Figure 9 we
see that [ γe1,θ] = 0. More precisely, denoting the set Wǫ,M :={p∈ Xǫ,M|| z±(p)|≤ M}, we
have the following result:
Corollary 2.12. If eiϑ ∈ C\S(V0), and θ∈ (ϑ− π
2 , ϑ + π
2 ), then there exists constants
M, ǫ > 0 such that for any p∈ Σ ǫ\Wǫ,M or e⊆ Σ ǫ\Wǫ,M with V (p), V (e)⊂ V0− ieiϑR>0 + Z,
we ﬁnd that [ γp,θ] = [ γe,θ] = 0∈ H1(Σ , D∞,θ).
Proof. From Equation ( 46) in the proof of Lemma 2.2, there exists constants ǫ, M > 0 such
that for x∈ Σ ǫ\Wǫ,M with Re( z±(x))⁄= 0 and V (x)∈ V0− ieiϑR>0 + Z the imaginary part
of the tangent to Γ p,θ (or Γ pe,θ) always has the same sign as Im( z±(p)) (or Im( z±(pe))). This
implies that the curves γp,θ and γe,θ satisfying the assumptions would never cross the real
line and therefore represent trivial classes. □
