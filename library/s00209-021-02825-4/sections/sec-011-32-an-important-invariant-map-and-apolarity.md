---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-011-32-an-important-invariant-map-and-apolarity
section_title: "An important invariant map, and apolarity"
section_number: 3.2
pages: 9-10
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
To aide in our investigation of inner tensor products of SL2(C) representations, we now
deﬁne an important SL2(C)-invariant linear map, denoted by D. This map has a long history
in invariant theory, and we touch on this below.
Proposition 3.1 The linear map D := (∂x ⊗∂y −∂y ⊗∂x) : V (n + 1) ⊗V (m + 1) →
V (n) ⊗V (m) is SL2(C)-invariant.
Proof It sufﬁces to check this on simple tensors. Fix φ =

 a b
c d

∈SL2(C), p ∈V (n + 1),
and q ∈V (m + 1). We compute:
(φ−1 ◦D ◦φ)(p ⊗q) = (φ−1 ◦D)(p(dx −by, −cx + ay) ⊗q(dx −by, −cx + ay))
= (d∂x −c∂y)p ⊗(−b∂x + a∂y)q −(−b∂x + a∂y)p ⊗(d∂x −c∂y)q
= (ad −bc)(∂x p ⊗∂yq −∂y p ⊗∂xq)
= D(p ⊗q)
That is, D ◦φ = φ ◦D.
⊓⊔
Proposition 3.2 The multiplication map V (n) ⊗V (m)
×
−→V (n + m) is SL2(C)-invariant.
Proof Trivial.
⊓⊔
Powers of the D map actually appear in the literature under a few different names. The
ﬁrst comes from invariant theory, where the application of the map
V (n) ⊗V (m)
Dr
−→V (n −r) ⊗V (m −r)
×
−→V (n + m −2r)
to polynomials p ∈V (n) and q ∈V (m) is called the rth transvectant of p and q. This map
is also the result of the rth iteration of Cayley’s  process. These notions are discussed, for
example, in chapters 4 and 5 of [13], where they are used to explicitly compute invariants
1368
J. Leake
and covariants of forms. In particular, the invariance of the Jacobian (1st transvectant map
applied to p ⊗q) and the Hessian (2nd transvectant map applied to p ⊗p) can be determined
in this way.
Additionally, the nth transvectant of p, q ∈V (n) is used to deﬁne a notion of apolarity
(see, e.g., [5] and [4]), and this notion corresponds to the classical one used in Grace’s
theorem. In fact, one of the original formulations of Grace’s theorem can be found in Grace
and Young’s 1903 book, The Algebra of Invariants [9]. This suggests a connection between
invariant theory and the analytic consequences of apolarity theory via the D map, and we
will indeed see this map play a crucial role in the proof of Grace’s theorem (Theorem 5.1).
We are now ready to deﬁne the homogeneous apolarity form via the D map. This form
and its SL2(C)-invariance are then the next main step toward the deﬁnition of the symbol
of an operator. In the next section, we will use this bilinear form to deﬁne an important
construction called the dual of a representation. This will serve as the link to viewing spaces
of linear operators as representations themselves.
Deﬁnition 3.3 We call the nth transvectant
V (n) ⊗V (n)
Dn
−→V (0) ⊗V (0) ∼= C
the apolarity form of V (n). This is the unique (up to scalar) nondegenerate SL2(C)-invariant
bilinear form on V (n), and therefore it is the homogenization of the classical apolarity form.
We now want to extend this deﬁnition to act on V (λ) ⊗V (λ) for λ ∈Nm
0 . Note that for
p ∈V (λ), we have m pairs of variables given by p(x1, y1, . . . , xm, ym), which allows us to
naturally deﬁne:
Dλ :=
m

i=1
(∂xi ⊗∂yi −∂yi ⊗∂xi )λi
With this, we can deﬁne the apolarity form for V (λ) as follows.
Deﬁnition 3.4 We call the map
V (λ) ⊗V (λ)
Dλ
−→V (0m) ⊗V (0m) ∼= C
the apolarity form of V (λ). This is the unique (up to scalar) nondegenerate (SL2(C))m-
invariant bilinear form on V (λ), and therefore it is the homogenization of the multivariate
apolarity form deﬁned by Borcea and Brändén in [2].
Since V (0) ⊗V (0) ∼= C and V (0m) ⊗V (0m) ∼= C, we will often consider the maps
Dn and Dλ to output a element of C. And as a ﬁnal note, we do not justify here the claims
of uniqueness and nondegeneracy stated above. Proving these claims involves decomposing
V (n) ⊗V (n) and V (λ) ⊗V (λ) into their irreducible components, and we leave this work to
Appendix A for the interested reader (see Corollaries A.9 and A.12 speciﬁcally).
