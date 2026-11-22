---
doc_id: arxiv-hep-th-0006111v2
doc_title: "arXiv:hep-th/0006111v2 14 Jul 2003"
section_id: page-002
section_title: "Page 2"
section_number: null
pages: 2-2
source_pdf: 0006111v2.pdf
source_sha256: e024febd3d0886a3
toc_source: undetermined
doc_brief: "arXiv:hep-th/0006111v2 14 Jul 2003 — 6 sections: Page 1; Page 2; Page 3"
---
where the integrals are over complex, real, and quaternion real (N + ν) × N matrices W for β = 2, 1, 4, respectively.
These chiral random matrix ensembles provide exactly equivalent descriptions of the eﬀective ﬁeld theory partition
functions in the microscopic ﬁnite-volume scaling regime [3,5]. Moreover, all microscopic spectral properties of the
Dirac operator coincide exactly with the corresponding microscopically rescaled Random Matrix Theory eigenvalues
[8]. This means that either formulation can be used to derive identical results, and in the case of the individual
distributions of the smallest Dirac operator eigenvalues it is presently more simple to use the Random Matrix Theory
formulation. Since the results turn out to be universal, i.e. independent of the detailed form of the Random Matrix
Theory potential v(W †W) [24–26], it suﬃces for us to concentrate on Gaussian ensembles with v(x) = x. This choice
leads to Wigner’s semi-circle law ρ(λ) = (2/π)
√
2N −λ2.
The partition functions (1) of such chiral Gaussian ensembles corresponding to Nf massive ﬂavors and topological
charge ν can then be written in terms of eigenvalues {xi} of the positive-deﬁnite Wishart matrices W †W,
Z(β)
ν
(m1, . . . , mNf ) =
Nf
Y
i=1
mi
ν Z ∞
0
· · ·
Z ∞
0
N
Y
i=1

dxi xβ(ν+1)/2−1
i
e−βxi
Nf
Y
j=1
(xi + m2
j)
 N
Y
i>j
|xi −xj|β ,
(2)
up to an overall irrelevant factor which is independent of the m’s.
Because everything will be symmetric under
ν →−ν, we for convenience take ν to be non-negative. In the following, we impose the one single technical restriction
that for β = 1 the topological charge ν be odd.
The unnormalized joint probability distributions for N eigenvalues {0 ≤x1 ≤· · · ≤xN} in the above Random
Matrix Theory ensembles take the form
ρ(β)
N (x1, . . . , xN; {m2}) =
N
Y
i=1

xβ(ν+1)/2−1
i
e−βxi
Nf
Y
j=1
(xi + m2
j)
 N
Y
i>j
|xi −xj|β .
(3)
The joint probability distribution of the k smallest eigenvalues {0 ≤x1 ≤· · · ≤xk−1 ≤xk} can be written as (the
order of x1, . . . , xk−1 can be relaxed):
Ω(β)
N,k(x1, . . . , xk−1, xk; {m2}) ≡
1
Ξ(β)
N ({m2})
1
(N −k)!
Z ∞
xk
dxk+1 · · ·
Z ∞
xk
dxN ρ(β)
N (x1, . . . , xN; {m2})
=
1
Ξ(β)
N ({m2})
k
Y
i=1

xβ(ν+1)/2−1
i
e−βxi
Nf
Y
j=1
(xi + m2
j)

k
Y
i>j
|xi −xj|β
×
1
(N −k)!
Z ∞
xk
dxk+1 · · ·
Z ∞
xk
dxN
N
Y
i=k+1

xβ(ν+1)/2−1
i
e−βxi
Nf
Y
j=1
(xi + m2
j)
k
Y
j=1
(xi −xj)β
N
Y
i>j≥k+1
|xi −xj|β ,
(4)
where Ξ(β)
N
stands for the normalizing integral
Ξ(β)
N ({m2}) = 1
N!
Z ∞
0
dx1 · · ·
Z ∞
0
dxN ρ(β)
N (x1, . . . , xN; {m2}) .
(5)
We now shift xi →xi + xk in the integrand of (4):
Ω(β)
N,k(x1, . . . , xk−1, xk; {m2}) = e−(N−k)βxk
Ξ(β)
N ({m2})
1
(N −k)!
k
Y
i=1

xβ(ν+1)/2−1
i
e−βxi
Nf
Y
j=1
(xi + m2
j)

k
Y
i>j
|xi −xj|β
×
Z ∞
0
N
Y
i=k+1

dxi e−βxixβ
i (xi + xk)β(ν+1)/2−1
Nf
Y
j=1
(xi + m2
j + xk)
k−1
Y
j=1
(xi + xk −xj)β
N
Y
i>j≥k+1
|xi −xj|β .
(6)
To get the probability distributions of the Dirac operator eigenvalues we must change the picture back to chiral
Gaussian ensembles, and take the microscopic limit
xi →0
m2
j →0 ,
N →∞,
with the rescaled variables
ζi = πρ(0)√xi = √8N xi
µj = πρ(0)mj
=
√
8Nmj
kept ﬁxed.
(7)
In this large-N limit the diﬀerence between partition functions based on N−k and N eigenvalues becomes insigniﬁcant.
Moreover, one notices that the new terms in the integrand of (6) can be interpreted as arising from new additional
2
