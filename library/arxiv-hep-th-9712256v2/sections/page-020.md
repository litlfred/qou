---
doc_id: arxiv-hep-th-9712256v2
doc_title: "On structure constants and fusion rules in the SL(2,C)/SU(2) WZNW model"
section_id: page-020
section_title: "Page 20"
section_number: null
pages: 20-20
source_pdf: 9712256v2.pdf
source_sha256: 9939add0a5823a43
toc_source: undetermined
doc_brief: "On structure constants and fusion rules in the SL(2,C)/SU(2) WZNW model — A closed formula for the structure constants in the SL(2,C)/SU(2) WZNW model is derived by a method previously used in"
---
20
J. TESCHNER
7. Appendix
7.1. Solutions to the Liouville decoupling equations. In order to write down the solutions,
introduce the parameters
u = b(α1 + α3 + α4 −3b/2) −1
¯u = b−1(α1 + α3 + α4 −3b−1/2) −1
v = b(α1 + α3 −α4 −b/2)
¯v = b−1(α1 + α3 −α4 −b−1/2)
w = b(2α1 −b)
¯w = b−1(2α1 −b−1)
Then the solutions to the decoupling equation (59) that correspond to s-channel conformal blocks
are given by
F
L2,1
s+
=
zbα1(1 −z)bα3F(u, v, w; z)
F
L2,1
s−
=
z1−b(α1−b)(1 −z)bα3F(u −w + 1, v −w + 1, 2 −w; z),
whereas the solutions for the t-channel are
F
L2,1
t+
=
zbα1(1 −z)bα3F(u, v, u + v −w + 1; 1 −z)
Ft−−L2,1
=
zbα1(1 −z)1−b(α3−b)F(w −u, w −v, w −u −v + 1; 1 −z).
Similarly, the solutions in the (1,2) case are obtained by replacing b →b−1 and u, v, w →¯u, ¯v, ¯w.
7.1.1. Fusion and braiding. If a basis for the space of conformal blocks with diagonal monodromy
around the origin is chosen then fusion matrix and the phases ΩL2,1
sσ , σ = +, −deﬁned by 10
F L2,1
sσ (eπiz) = ΩL2,1
sσ F L2,1
sσ (z)
form a complete set of duality data, i.e. completely determine the monodromies of conformal
blocks. Here the phases ΩL2,1
sσ
are read oﬀas
Ω
L2,1
s+ = eπibα1
Ω
L2,1
s−= eπi(1−b(α1−b))
The fusion matrix is calculated by using the standard results on analytic continuation of hyper-
geometric functions:
GL(0)
+
=
Γ(w)Γ(w −u −v)
Γ(w −u)Γ(w −v)GL(1)
+ + Γ(w)Γ(u + v −w)
Γ(u)Γ(v)
GL(1)
−
GL(1)
−
=
Γ(2 −w)Γ(w −u −v)
Γ(1 −u)Γ(1 −v)
GL(1)
+ −
Γ(2 −w)Γ(u + v −w)
Γ(u −w + 1)Γ(v −w + 1)GL(1)
−
7.2. Solutions to decoupling equations (2,1). This case is of course well-known [FZ, TK].
For the sake of a coherent presentation, I will nevertheless present the relevant results.
Equation ∂xF = 0 of course implies F(x, z) = F+(z) + xF−(z). It straightforward to re-
duce the system of two ordinary diﬀerential equations that follows from the KZ-equations to
hypergeometric equations for F+(z), F−(z). The normalization prescription is
F(x, z) ∼zh21−h2−h1xj1+j2−j21(1 + O(x) + O(z))
10It will be assumed throughout that zλ is deﬁned by the principal value of the logarithm and that arg(z) ∈
(−π, 0]
