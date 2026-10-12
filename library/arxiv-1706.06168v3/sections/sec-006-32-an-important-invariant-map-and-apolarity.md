---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-006-32-an-important-invariant-map-and-apolarity
section_title: "An Important Invariant Map, and Apolarity"
section_number: 3.2
pages: 8-8
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
---
An Important Invariant Map, and Apolarity
To aide in our investigation of inner tensor products of SL2(C) representations, we now deﬁne an important
SL2(C)-invariant linear map, denoted by D. This map has a long history in invariant theory, and we touch
on this below.
Proposition 3.1. The linear map D := (∂x ⊗∂y −∂y ⊗∂x) : V (n + 1) ⊗V (m + 1) →V (n) ⊗V (m) is
SL2(C)-invariant.
Proof. It suﬃces to check this on simple tensors. Fix φ =
 a b
c d

∈SL2(C), p ∈V (n + 1), and q ∈V (m + 1).
We compute:
(φ−1 ◦D ◦φ)(p ⊗q) = (φ−1 ◦D)(p(dx −by, −cx + ay) ⊗q(dx −by, −cx + ay))
= (d∂x −c∂y)p ⊗(−b∂x + a∂y)q −(−b∂x + a∂y)p ⊗(d∂x −c∂y)q
= (ad −bc)(∂xp ⊗∂yq −∂yp ⊗∂xq)
= D(p ⊗q)
That is, D ◦φ = φ ◦D.
Proposition 3.2. The multiplication map V (n) ⊗V (m)
×
−→V (n + m) is SL2(C)-invariant.
Proof. Trivial.
Powers of the D map actually appear in the literature under a few diﬀerent names. The ﬁrst comes from
invariant theory, where the application of the map
V (n) ⊗V (m)
Dr
−−→V (n −r) ⊗V (m −r)
×
−→V (n + m −2r)
to polynomials p ∈V (n) and q ∈V (m) is called the rth transvectant of p and q. This map is also the result
of the rth iteration of Cayley’s Ωprocess. These notions are discussed, for example, in chapters 4 and 5
of [Olv99], where they are used to explicitly compute invariants and covariants of forms. In particular, the
invariance of the Jacobian (1st transvectant map applied to p ⊗q) and the Hessian (2nd transvectant map
applied to p ⊗p) can be determined in this way.
Additionally, the nth transvectant of p, q ∈V (n) is used to deﬁne a notion of apolarity (see, e.g., [ER93]
and [BCF07]), and this notion corresponds to the classical one used in Grace’s theorem. In fact, one of
the original formulations of Grace’s theorem can be found in Grace and Young’s 1903 book, The Algebra of
Invariants [GY03]. This suggests a connection between invariant theory and the analytic consequences of
apolarity theory via the D map, and we will indeed see this map play a crucial role in the proof of Grace’s
theorem (Theorem 5.1).
We are now ready to deﬁne the homogeneous apolarity form via the D map. This form and its SL2(C)-
