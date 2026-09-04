---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-006-32-an-important-invariant-map-and-apolarity
section_title: "An Important Invariant Map, and Apolarity"
section_number: 3.2
pages: 8-9
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨ and´ en characterized all linear oper ators on multivariate polynomials which preserve the"
---
To aide in our investigation of inner tensor products of SL 2(C) representations, we now deﬁne an important
SL2(C)-invariant linear map, denoted by D. This map has a long history in invariant theory, and we touch
on this below.
Proposition 3.1. The linear map D := (∂x ⊗∂y −∂y ⊗∂x) : V (n + 1) ⊗V (m + 1) → V (n) ⊗V (m) is
SL2(C)-invariant.
Proof. It suﬃces to check this on simple tensors. Fix φ =
[ a b
c d
]
∈ SL2(C), p ∈V (n + 1), and q ∈V (m + 1).
We compute:
(φ−1 ◦D ◦φ)(p ⊗q) = (φ−1 ◦D)(p(dx −by, −cx +ay) ⊗q(dx −by, −cx +ay))
= (d∂x −c∂y)p ⊗ (−b∂x +a∂y)q − (−b∂x +a∂y)p ⊗ (d∂x −c∂y)q
= (ad −bc)(∂xp ⊗∂yq −∂yp ⊗∂xq)
=D(p ⊗q)
That is, D ◦φ =φ ◦D.
Proposition 3.2. The multiplication map V (n) ⊗V (m)
×
− →V (n +m) is SL2(C)-invariant.
Proof. Trivial.
Powers of the D map actually appear in the literature under a few diﬀerent names. Th e ﬁrst comes from
invariant theory, where the application of the map
V (n) ⊗V (m)
Dr
− − →V (n −r) ⊗V (m −r)
×
− →V (n +m − 2r)
to polynomials p ∈V (n) and q ∈V (m) is called the rth transvectant of p and q. This map is also the result
of the rth iteration of Cayley’s Ω process. These notions are discussed, for example, in chapters 4 and 5
of [ Olv99], where they are used to explicitly compute invariants and covariant s of forms. In particular, the
invariance of the Jacobian (1 st transvectant map applied to p ⊗q) and the Hessian (2 nd transvectant map
applied to p ⊗p) can be determined in this way.
Additionally, the nth transvectant of p,q ∈V (n) is used to deﬁne a notion of apolarity (see, e.g., [ ER93]
and [ BCF07]), and this notion corresponds to the classical one used in Grace’s t heorem. In fact, one of
the original formulations of Grace’s theorem can be found in Grace a nd Young’s 1903 book, The Algebra of
Invariants [GY03]. This suggests a connection between invariant theory and the ana lytic consequences of
apolarity theory via the D map, and we will indeed see this map play a crucial role in the proof of Gr ace’s
theorem (Theorem 5.1).
We are now ready to deﬁne the homogeneous apolarity form via the D map. This form and its SL 2(C)-
invariance are then the next main step toward the deﬁnition of the s ymbol of an operator. In the next
section, we will use this bilinear form to deﬁne an important construc tion called the dual of a representation.
This will serve as the link to viewing spaces of linear operators as repr esentations themselves.
Deﬁnition 3.3. We call the nth transvectant
V (n) ⊗V (n)
Dn
− − →V (0) ⊗V (0) ∼= C
the apolarity form of V (n). This is the unique (up to scalar) nondegenerate SL 2(C)-invariant bilinear form
on V (n), and therefore it is the homogenization of the classical apolarity f orm.
8
We now want to extend this deﬁnition to act on V (λ) ⊗V (λ) for λ ∈ Nm
0 . Note that for p ∈ V (λ), we
havem pairs of variables given by p(x1,y 1,...,x m,y m), which allows us to naturally deﬁne:
Dλ :=
m∏
i=1
(∂xi ⊗∂yi −∂yi ⊗∂xi )λi
With this, we can deﬁne the apolarity form for V (λ) as follows.
Deﬁnition 3.4. We call the map
V (λ) ⊗V (λ)
Dλ
− − →V (0m) ⊗V (0m) ∼= C
the apolarity form of V (λ). This is the unique (up to scalar) nondegenerate (SL 2(C))m-invariant bilinear
form on V (λ), and therefore it is the homogenization of the multivariate apolarit y form deﬁned by Borcea
and Br¨ and´ en in [BB09b].
Since V (0) ⊗V (0) ∼= C and V (0m) ⊗V (0m) ∼= C, we will often consider the maps Dn and Dλ to output
a element of C. And as a ﬁnal note, we do not justify here the claims of uniqueness and nondegeneracy
stated above. Proving these claims involves decomposing V (n) ⊗V (n) and V (λ) ⊗V (λ) into their irreducible
components, and we leave this work to Appendix A for the interested reader (see Corollaries A.9 and A.12
speciﬁcally).
