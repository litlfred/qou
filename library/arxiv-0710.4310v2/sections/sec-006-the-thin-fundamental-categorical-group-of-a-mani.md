---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto"
section_id: sec-006-the-thin-fundamental-categorical-group-of-a-mani
section_title: "The thin fundamental categorical group of a manifold"
section_number: null
pages: 12-13
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
doc_brief: "On Two-Dimensional Holonomy João Faria Martins Centro de Matemática da Universidade do Porto — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold ( M, ∗) as the"
---
Let M be a smooth manifold.
1.3.1 1-T racks
Deﬁnition 15 (1-path) A 1-path is given by a smooth map γ : [0, 1] → M
such that there exists an ǫ > 0 such that γ is constant in [0,ǫ ] ∪ [1 −ǫ, 1]; in
the terminology of [CP], this can be abbreviated by saying th at each end point of
γ has a sitting instant. Given a 1-path γ, deﬁne the source and target of γ as
σ(γ) = γ(0) and τ (γ) = γ(1), respectively.
Given two 1-paths γ and φ with τ (γ) = σ(φ), their concatenation γφ is
deﬁned in the usual way:
(γφ)(t) =
{ γ(2t), if t ∈ [0, 1/2]
φ(2t − 1), if t ∈ [1/2, 1]
Note that the concatenation of two 1-paths is also a 1-path. The f act that any
1-path has sitting instants at its end points needs to be used to pro ve this.
Deﬁnition 16 (2-paths) A 2-path Γ is given by a smooth map Γ : [0, 1]2 →M
such that there exists an ǫ> 0 for which:
1. Γ(t,s ) = Γ(0, 0) if 0 ≤t ≤ǫ and s ∈ [0, 1],
2. Γ(t,s ) = Γ(1, 0) if 1 −ǫ ≤t ≤ 1 and s ∈ [0, 1],
3. Γ(t,s ) = Γ(t, 0) if 0 ≤s ≤ǫ and t ∈ [0, 1],
4. Γ(t,s ) = Γ(t, 1) if 1 −ǫ ≤s ≤ 1 and t ∈ [0, 1].
Given a 2-path Γ, deﬁne the following 1-paths:
∂l(Γ)(s) = Γ(0,s ),s ∈ [0, 1], ∂ r(Γ)(s) = Γ(1,s ),s ∈ [0, 1],
∂d(Γ)(t) = Γ(t, 0),t ∈ [0, 1], ∂ u(Γ)(t) = Γ(t, 1),t ∈ [0, 1].
Note that the paths ∂l(Γ) and ∂r(Γ) are necessarily constant, thus each of them
can be identiﬁed with a point of M . In addition, given a 2-path Γ then the
1-paths∂u(Γ) and ∂d(Γ) have the same initial and end points. If x is a point of
M the constant 1- and 2-paths with value x are both denoted by x.
If Γ and Γ ′ are 2-paths such that ∂r(Γ) = ∂l(Γ ′) their horizontal concatena-
tion Γ ◦h Γ ′ is deﬁned in the obvious way, in other words:
12
(
Γ ◦h Γ ′)
(t,s ) =
{ Γ(2t,s ), if t ∈ [0, 1/2] and s ∈ [0, 1]
Γ ′(2t − 1,s ), if t ∈ [1/2, 1] and s ∈ [0, 1]
Similarly, if ∂u(Γ) = ∂d(Γ ′) we can deﬁne a vertical concatenation Γ ◦v Γ ′ as:
(
Γ ◦v Γ ′)
(t,s ) =
{ Γ(t, 2s), if s ∈ [0, 1/2] and t ∈ [0, 1]
Γ ′(t, 2s − 1), if s ∈ [1/2, 1] and t ∈ [0, 1]
We will also represent the 2-paths Γ of M in the following suggestive way:
Γ =
∂u(Γ)
↑Γ
∂d(Γ)
In this notation, the vertical concatenation of two 2-paths Γ and Γ ′ with∂d(Γ ′) =
∂u(Γ) can be represented as:
Γ ◦v Γ ′ =
∂u(Γ ◦v Γ ′)
↑Γ ◦v Γ ′
∂d(Γ ◦v Γ ′)
=
∂u(Γ ′)
↑Γ ′
∂d(Γ ′) = ∂u(Γ)
↑Γ
∂d(Γ)
Deﬁnition 17 Two 1-paths φ and γ are said to be rank-1 homotopic (and we
write φ ∼=1γ) if there exists a 2-path Γ such that:
1. ∂u(Γ) = γ and ∂d(Γ) = φ.
2. Rank(DvΓ) ≤ 1, ∀v ∈ [0, 1]2.
Here D denotes derivative.
In particular, if γ and φ are rank-1 homotopic, then they have the same ini-
tial and end-points. Note also that rank-1 homotopy is an equivalen ce rela-
tion. Given a 1-path γ, the equivalence class to which it belongs is denoted
by [γ]. Rank-1 homotopy is one of a number of notions of “thin” equivalenc e
between paths or loops, and was introduced in [CP], following a sugge stion by
A. Machado.
We denote the set of 1-paths of M byS1(M ). The quotient of S1(M ) by the
relation of thin homotopy is denoted by S1(M ). We call the elements of S1(M )
