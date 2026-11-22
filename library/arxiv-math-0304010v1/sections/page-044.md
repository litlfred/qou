---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-044
section_title: "Page 44"
section_number: null
pages: 44-44
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
To any matrix X ∈HN we assign a certain probability measure µX on R, which
we prefer to view as a generalized function:
µX(x) = 1
N (δ(x −x1) + · · · + δ(x −xN)),
(9.6)
where x1 , . . ., xN are the eigenvalues of X, and δ(x) is the delta function. Dropping
X, which we view as the random element of the probability space (HN, GaussN), we
regard (9.6) as the random generalized function µ(x). Then we have the following
central limit theorem for the Gaussian unitary ensemble (we state it informally):
µ(x) ∼µs-c(x) + 1
N
e∆(x),
N →∞,
(9.7)
where e∆(x) is the Gaussian process on [−2, 2] deﬁned by the random series
e∆(x) =
∞
X
k=1
√
k ξktk(x)
2π
√
4 −x2
(9.8)
with independent standard Gaussians ξ1, ξ2, . . . .
For the rigorous formulation and proof of this result (and its generalizations),
see [Jo2]. Note that similar results hold for other random matrix ensembles, see
[DE], [DS], [Jo1]. As explained in [Jo1], [Jo2], this subject has close links with the
famous Szeg¨o theorem on asymptotics of Toeplitz determinants.
Comparing (9.3) and (9.8) we see that the Gaussian processes b∆(x)and e∆(x)
look rather close. Another observation is that
−1
2 · d
dx ∆(x) =
∞
X
k=2
√
k ξktk(x)
2π
√
4 −x2 .
(9.9)
That is, the derivative of the process ∆(x) coincides, up to factor −1/2 and the
ﬁrst term, with the process e∆(x). This is readily seen from the following formulas.
All the three series ∆(x), b∆(x), e∆(x) look especially simply after change of a
variable, x = 2 cos θ. Using (7.4), (8.6) we get
∆(2 cos θ) = 1
π
∞
X
k=2
ξk
√
k
sin(kθ) ,
b∆(2 cos θ) = 1
2π
∞
X
k=3
√
k −1 ξk−1 cos(kθ)
sin θ
,
e∆(2 cos θ) = 1
2π
∞
X
k=1
√
k ξk cos(kθ)
sin θ
.
§10. Free cumulants and Biane’s theorem
Let, as above,
H(t) = 1 +
∞
X
j=1
hjtj ∈Λ[[t]]
44
