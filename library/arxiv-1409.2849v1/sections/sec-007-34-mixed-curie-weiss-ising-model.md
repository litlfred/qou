---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-007-34-mixed-curie-weiss-ising-model
section_title: "Mixed Curie-Weiss-Ising model"
section_number: 3.4
pages: 17-19
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
parameter α = 0, and β arbitrary. We have shown in Section 2 the complex mod-
Gaussian convergence of (n−1/4 Mn)n∈N with parameters n1/2 e2β and limiting func-
tion ψ(z) = exp(−(3e6β− e2β) z4/24). Restricted to R, this limiting function is inte-
grable, and again one has L1-mod-convergence. Indeed, recall that
E[etMn] = Zn(I, t, β)
Zn(I, 0, β) = 1
2
(
a+(t, β)
( λ+(t, β)
2 cosh β
)n−1
+ a−(t, β)
( λ−(t, β)
2 cosh β
)n−1)
.
18 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
It will be convenient to work with n−1/4 Mn+1 instead of n−1/4 Mn in order to work
with n-th powers. Then,
ψn(t) = E
[
et
Mn+1
n1/4
]
e− n1/2e2βz2
2
∫
R
ψn(t)dt = n1/4
2
∫
R
a+(u, β)
( λ+(u, β)
2 cosh β e− e2βu2
2
)n
+ a−(u, β)
( λ−(u, β)
2 cosh β e− e2βu2
2
)n
du
and for every parameter β≥ 0, the functions
u↦→ λ+(u, β)
2 cosh β e− e2βu2
2 and u↦→ λ−(u, β)
2 cosh β e− e2βu2
2
attain their unique maximum at u = 0, see Figure 3 for the graph of the ﬁrst function.
FIGURE 3. The function f (u, β) = λ+(u,β)
2 cosh β e− e2βu2
2 (using MATHEMATICA ).
Their Taylor expansions at u = 0 are respectively
1− 3e6β− e2β
24 u4 + o(u4) and tanh β + o(1),
so again by the Laplace method we get lim n→∞
∫
R ψn(t) dt = ∫
R ψ(t) dt and the L 1-
mod-convergence. As a consequence, consider the random conﬁguration of spins σ on
[ [1, n] ]with probability proportional to
exp

β
(
n−1
∑
i=1
σ(i)σ(i + 1)
)
+ 1
2ne2β
(
n
∑
i=1
σ(i)
)2
 .
This model has a local interaction with coefﬁcient β and a global interaction with coef-
ﬁcient 1
e2β , so it is a mix of the Ising model and of the Curie-Weiss model. The previous
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS19
discussion and Theorem 6 show that its magnetization satisﬁes the non standard limit
theorem
Mn
n3/4 ⇀n→∞
ψ(x) dx∫
R ψ(x) dx with ψ(x) = exp
(
−3e6β− e2β
24 x4
)
.
