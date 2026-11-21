---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-011-32-proof-of-theorem-14
section_title: "Proof of Theorem 1.4"
section_number: 3.2
pages: 19-21
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
toc_source: outline
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜no [9] that perturbative series associated with the hyperbolic knots 41 and 52 are resurgent and"
---
theorem.
The main idea is to compute the asymptotics of the function Ip0,V0,ϑ(τ) for
20
VERONICA FANTINI AND CAMPBELL WHEELER
arg(−1/τ) = θ ∈(−π
2 + ϑ, π
2 + ϑ). We will state this in the following theorem, which is
essentially equivalent to Theorem 1.4.
Theorem 3.4. If [a, b] ⊆arg(C\S(V0)) ∩( π
2, 3π
2 ), ϑ ∈[a, b], arg(−1/τ) = θ ∈(a −π
2, b −π
2)
and |τ| →∞, then there exists constants C = C(a, b), ε = ε(a, b) > 0
|e(−V0τ)Ip0,V0,ϑ(τ) −Φ(K)
Ξ (−2πi/τ)| < C ε−K K! |τ|−K ,
(63)
where Φ(K)
Ξ (ℏ) is the truncation of the series ΦΞ(ℏ) to O(ℏK).
Proof. Firstly, as we vary arg(−1/τ) = θ ∈(ϑ −π
2, ϑ + π
2), we can deform the contours of
the state integrals of Ip0,V0,ϑ(τ) so that they are contained in Z+ besides tails based at the
set {p ∈X ∩Z+ : Im(z(p)e−iθ) ∈sin(2πθ)Z}. Considering this deformation we can now
compute the asymptotics.
The ﬁrst iteration of the algorithm gives a collection of state integrals (from step III)
whose asymptotics is determined by the saddle point approximation at p0 with the addition
of the asymptotics of the tails (from in step II). The tail at (z, m) is
Z ±eiθ∞
z

Φ((w −ℓ)τ; τ)B −Φ((w −ℓ−1)τ; τ)B
e
A
2 w(w + 1 + 1
τ )τ + mwτ

dw .
(64)
Step IV produces a new collection of cycles γ(z,m±k) (described in Equation (62)) whose
asymptotics is equal to the asymptotics of the remaining tails. Therefore, at any iteration
of the algorithm, the asymptotics are determined by the asymptotics of a ﬁnite collection of
tails and the saddle point approximation at p0.
By construction, after a ﬁnite number of steps, the starting points of these tails will be
outside W (see Corollary 3.2). Notice that the volumes of the tails’ base points are always
decreasing, and therefore eventually they leave the ﬁnite set P. If a tail starts outside W its
asymptotics are exponentially smaller than the asymptotics coming from the saddle point
approximation at p0. This can be seen from the proof of Corollary 2.12.
Therefore, the tails in Ip0,V0,ϑ(τ) only make exponentially small contributions and the
asymptotics are determined by the integral along the set Z+. For (ϑ −π
2, ϑ + π
2), the set Z+
is contained in the region where Im(V (p)τ) > 0 for the local lift of V (p) ∈C. We therefore
see that Ip0,V0,ϑ(τ) has asymptotics determined by the stationary phase approximation at p0
(see for example [22, Chap. 9, Sec. 2.2, Theorem 2.1]). This was exactly how ΦΞ was deﬁned
in Equation (11) and therefore this completes the proof.
□
Proof of Theorem 1.4. To transfer this result to a proof of the main theorem, we simply
follow the same proof as in Corollary 1.3. Given these asymptotics we can apply Nevanlinna’s
theorem [21] or simply just take Mordell’s inverse Laplace transform to deﬁne the analytic
continuation of the Borel transform in the cone θ ∈(a, b). This proves the Borel summability.
We can run exactly the same construction and proof for Re(τ) < 0 using the functions given
in Remark 1.5 to give the full result including Re(τ) < 0.
□
Proof of Theorem 1.1. The result follows immediately by specialising Theorem 1.4 to the
cases of (A, B) equal to (1, 2) for 41 and (2, 3) for 52.
□
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS
