---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-015-appendix-a1-eigenvalue-analysis
section_title: "Appendix A.1 Eigenvalue analysis"
section_number: null
pages: 26-27
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
In this section, we will brieﬂy review the eigenvalue analysis, the Young diagram analysis and
their connection in the context of the so-called single plaquette model. Interested readers may
refer to [18] for further details.
In the diagonal basis the partition function of the single plaquette model described by the action
(2.2) is given by (up to an overall volume dependent factor),
Z =
Z
N
Y
i=1
dθi
Y
i< j
sin2
 θi −θ j
2
!
exp N
X
n
2βn
n
N
X
i=1
cos nθi.
(A.1)
In the large N limit, the discrete eigenvalues θi goes over to a smooth continuous function θ(x)
where x ∈[0, 1]. One can write down a saddle point equation in the continuum limit which is
given by
−
Z 1
0
dy cot
 θ(x) −θ(y)
2
!
=
X
n
βn cos nθ(x).
(A.2)
26
Deﬁning a distribution function (called eigenvalue density) ρ(θ) for eigenvalues over a unit cir-
cle
ρ(θ) = 1
N
N
X
i=1
δ(θ −θi) = dx
dθ.
(A.3)
the saddle point equation (A.2) can be recast as
−
Z
dθ′ cot
 θ −θ′
2
!
ρ(θ′) =
X
n
βn cos nθ,
with
Z
dθρ(θ) = 1.
(A.4)
