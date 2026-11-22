---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: page-011
section_title: "Page 11"
section_number: null
pages: 11-11
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
toc_source: undetermined
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of symmet- ric groups."
---
APPROXIMATE FACTORIZATION AND CONCENTRATION
11
In this last section we shall consider the representation of Sq on H⊗q, given by
(i i + 1)(v1 ⊗. . . vi ⊗vi+1 . . . ⊗vq) = (−1)ε(vi)ε(vi+1)v1 ⊗. . . vi+1 ⊗vi . . . ⊗vq
where vk are graded vectors, with graduation ε(vk) ∈{0, 1}. The positive deﬁnite
function on Sq determined by this representation and the state τ ⊗q is given by
(3.2.1)
τ ⊗q(ρ) =
Y
c|ρ
p|c|+1
where the product is over the non trivial cycles c of ρ. Recall that for a cycle c
one has |c| + 1 = s(c). This is of course a direct generalization of Section 3.1 where
we had t1,0 = t2,0 = . . . = tN,0 =
1
N , the other eigenvalues being 0. We shall now
investigate the asymptotic decomposition of the associated probability measure on
Young diagrams, under the hypothesis that τ := τq depends on q as q →∞, and
that the moments Tr(T n
q ) satisfy
q(n−1)/2Tr(T n
q ) →q→∞wn+1
n ≥1
for some sequence of real numbers wn, with |wn| ≤Cn for some constant C > 0.
This last condition insures that the positive deﬁnite functions (3.2.1) belong to the
sets Fn
c,0 as in Section 3.1. Using the same arguments as in the preceding section,
we see that the measure on rescaled diagrams converges towards the Dirac mass
at the diagram with cumulants (wn)n≥1, with w1 = 0, w2 = 1. These cumulants
have the form wn =
R
R |t|tn−2µ(dt); n ≥2 for some positive measure µ on [−C, C],
satisfying
R
R |t|µ(dt) = 1. The R-transform of the measure with cumulants wn is
thus
R(z) =
∞
X
n=1
wnzn−1 =
Z
R
z
1 −zt|t|µ(dt)
Comparing with the free L´evy-Khintchine formula of [BV], we see that the measure
corresponding to the limit diagram is freely indeﬁnitely divisible, with correspond-
ing L´evy measure ν(dt) =
1
|t|µ(dt)
Remark. One can give an explicit expression for the weight of a given diagram
λ ∈Yq, under the measure associated with the function (3.2.1), in terms of the
Schur functions (see also [M] formula (7.8)). It would be interesting to rederive the
results of Sections 3.1 and 3.2 directly from this explicit expression.
References
[B]
P. Biane, Representations of symmetric groups and free probability, Adv. Math. 138
(1998), 126–181.
[BV]
H. Bercovici and D. Voiculescu, Free convolution of measures with unbounded support,
Indiana University Mathematics Journal 42 (1993), 733-773.
[K]
S. V. Kerov, Interlacing measures, Kirillov’s seminar on representation theory, Amer.
Math. Soc. Transl. Ser. 2 Appl., vol. 181, Amer. Math. Soc., Providence, RI, 1998, pp. 35–
83.
[LS]
B. F. Logan and L. A. Shepp, A variational problem for random Young tableaux, Adv.
Math. 26 (1977), 206–222.
[Mac]
I. G. Macdonald, Symmetric functions and Hall polynomials, 2nd Ed., Oxford Univ. Press,
O f
d 1995
