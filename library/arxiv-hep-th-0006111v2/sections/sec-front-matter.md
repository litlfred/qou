---
doc_id: arxiv-hep-th-0006111v2
doc_title: "Distribution of the k-th smallest Dirac operator eigenvalu e"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 0006111v2.pdf
source_sha256: e024febd3d0886a3
doc_brief: "Distribution of the k-th smallest Dirac operator eigenvalu e — 7 sections: Front matter; (ζ, {µ }) = ζ; (ζ) = ζ"
---
arXiv:hep-th/0006111v2  14 Jul 2003
Distribution of the k-th smallest Dirac operator eigenvalu e
Poul H. Damgaard
The Niels Bohr Institute, Blegdamsvej 17, DK-2100 Copenhag en Ø, Denmark
Shinsuke M. Nishigaki
Department of Physics, Tokyo Institute of Technology, O-ok ayama, Meguro, Tokyo 152-8551, Japan
(June 15, 2000; revised July 14, 2003)
Based on the exact relationship to Random Matrix Theory, we d erive the probability distribution
of the k-th smallest Dirac operator eigenvalue in the microscopic ﬁ nite-volume scaling regime of QCD
and related gauge theories.
PACS number(s): 12.38.Aw, 12.38.Lg
While index theorems have for long been known to re-
late the number of exact zero modes of the Dirac operator
to gauge ﬁeld topology, it is only during the 1990’s that
it has been realized how much further one can push such
exact predictions. When the gauge theory in question
is in a phase with spontaneously broken chiral symme-
try, Goldstone’s Theorem allows for much more detailed
statements, beyond the zero modes. The bridge between
the Dirac operator spectrum and the Goldstone degrees
of freedom is the eﬀective partition function of the asso-
ciated chiral Lagrangian [1,2]. The inﬁnite-volume chiral
condensate will be denoted by Σ. By considering the the-
ory at ﬁnite four-volume V , one can choose a microscopic
scaling regime in which this volume is sent to inﬁnity at
a rate correlated with the chiral limit m → 0 such that
µ ≡ Σ V m is kept ﬁxed. Then exact statements can be
made for an inﬁnite sequence of Dirac operator eigenval-
ues that accumulate towards the origin. This realization
was ﬁrst made on the basis of a universal Random Ma-
trix Theory reformulation of the problem [3–6], but it has
since then also been established directly at the level of
the eﬀective Lagrangian [7,8].
Conventionally, the exact analytical statements that
can be made about this infrared region of the Dirac oper-
ator spectrum in ﬁnite-volume gauge theories have been
phrased in terms of the microscopic spectral n-point func-
tions, and in particular the microscopic spectral density
ρS(ζ; {µ }) itself (here ζ ≡ Σ V λ is the microscopically
rescaled Dirac operator eigenvalue λ) [3,4,9–18]. Also
the exact distribution of just the lowest Dirac operator
eigenvalue has been derived on the basis of the relation-
ship to Random Matrix Theory [10,19–23,15,16]. In fact
also the distribution of the second-smallest eigenvalue in
what corresponds to the massless limit of SU (Nc ≥ 3)
gauge theories with fermions in the fundamental repre-
sentation can be extracted from the work of Forrester
and Hughes [21]. In this paper, we push these compu-
tations one step further and provide analytical expres-
sions for both the joint probability distribution of the
ﬁrst k eigenvalues and the distribution of the k-th eigen-
value. We do so for the chiral unitary ( β = 2), orthogonal
(β = 1, corresponding to SU (2) gauge theories with fun-
damental fermions), and symplectic ensembles ( β = 4,
corresponding to SU (Nc ≥ 2) gauge theories with ad-
joint fermions). We will treat the most general case of
massive fermions, and (with one exception noted below)
a sector of arbitrary topological charge ν. In the micro-
scopic scaling limit this can be done to arbitrarily high
order k as long as the volume V is taken large enough.
This gives us an inﬁnite sequence of distributions of Dirac
operator eigenvalues that all, on the macroscopic scale,
build up the spectral density at the origin ρ(0). We stress
that there is much more information in these individual
eigenvalue distributions than in the summed-over micro-
scopic spectral density ρS(ζ; {µ }) itself. In particular,
from the point of view of lattice gauge theory simulations
it is far more convenient to be able to perform compar-
isons with individual eigenvalue distributions than with
just the average eigenvalue density.
There are by now detailed analytical predictions for
the microscopic spectral densities of the Dirac operator
for all three universality classes. These microscopic spec-
tral densities show a typical oscillatory structure, which
clearly is closely connected to the individual eigenvalue
peaks at the microscopic scale where units are given by
the average eigenvalue spacing. We thus expect that the
distribution of the k-th smallest Dirac operator eigen-
value corresponds closely to the k-th peak in the mi-
croscopic eigenvalue density, a feature that indeed had
already been noticed in the case of just the smallest
eigenvalue [23]. In particular, we expect that the k-th
eigenvalue distribution as computed in the framework of
Random Matrix Theory is universal, which indeed turns
out to be the case (see below). Of course, as one further
additional check, the sequential summing-up of the in-
dividual eigenvalue distributions should simply build up
the full microscopic eigenvalue densities, which are now
known in closed analytical form.
The chiral Random Matrix Theory ensembles are de-
ﬁned by [3–5]:
Z (β )
ν (m1, . . . , m Nf ) =
∫
dW e−β tr v(W † W )
Nf∏
i=1
det
( mi W
− W † mi
)
, (1)
1
where the integrals are over complex, real, and quaternion real ( N + ν) × N matrices W for β = 2, 1, 4, respectively.
These chiral random matrix ensembles provide exactly equivalent de scriptions of the eﬀective ﬁeld theory partition
functions in the microscopic ﬁnite-volume scaling regime [3,5]. Moreove r, all microscopic spectral properties of the
Dirac operator coincide exactly with the corresponding microscopic ally rescaled Random Matrix Theory eigenvalues
[8]. This means that either formulation can be used to derive identical results, and in the case of the individual
distributions of the smallest Dirac operator eigenvalues it is present ly more simple to use the Random Matrix Theory
formulation. Since the results turn out to be universal, i.e. independent of the detailed form of the Random Matrix
Theory potential v(W †W ) [24–26], it suﬃces for us to concentrate on Gaussian ensembles wit h v(x) = x. This choice
leads to Wigner’s semi-circle law ρ(λ) = (2 /π )
√
2N − λ 2.
The partition functions (1) of such chiral Gaussian ensembles corr esponding to Nf massive ﬂavors and topological
charge ν can then be written in terms of eigenvalues {xi} of the positive-deﬁnite Wishart matrices W †W ,
Z (β )
ν (m1, . . . , m Nf ) =
( Nf∏
i=1
mi
) ν ∫ ∞
0
· · ·
∫ ∞
0
N∏
i=1
(
dxi xβ (ν +1)/ 2−1
i e−βx i
Nf∏
j=1
(xi + m2
j )
) N∏
i>j
|xi − xj |β , (2)
up to an overall irrelevant factor which is independent of the m’s. Because everything will be symmetric under
ν → − ν, we for convenience take ν to be non-negative. In the following, we impose the one single technic al restriction
that for β = 1 the topological charge ν be odd.
The unnormalized joint probability distributions for N eigenvalues {0 ≤ x1 ≤ · · · ≤ xN } in the above Random
Matrix Theory ensembles take the form
ρ(β )
N (x1, . . . , x N ; {m2}) =
N∏
i=1
(
xβ (ν +1)/ 2−1
i e−βx i
Nf∏
j=1
(xi + m2
j )
) N∏
i>j
|xi − xj |β . (3)
The joint probability distribution of the k smallest eigenvalues {0 ≤ x1 ≤ · · · ≤ xk−1 ≤ xk} can be written as (the
order of x1, . . . , x k−1 can be relaxed):
Ω (β )
N,k (x1, . . . , x k−1, x k; {m2}) ≡ 1
Ξ (β )
N ({m2})
1
(N − k)!
∫ ∞
xk
dxk+1 · · ·
∫ ∞
xk
dxN ρ(β )
N (x1, . . . , x N ; {m2})
= 1
Ξ (β )
N ({m2})
k∏
i=1
(
xβ (ν +1)/ 2−1
i e−βx i
Nf∏
j=1
(xi + m2
j )
) k∏
i>j
|xi − xj |β
× 1
(N − k)!
∫ ∞
xk
dxk+1 · · ·
∫ ∞
xk
dxN
N∏
i=k+1
(
xβ (ν +1)/ 2−1
i e−βx i
Nf∏
j=1
(xi + m2
j )
k∏
j=1
(xi − xj)β
) N∏
i>j≥k+1
|xi − xj |β , (4)
where Ξ (β )
N stands for the normalizing integral
Ξ (β )
N ({m2}) = 1
N !
∫ ∞
0
dx1 · · ·
∫ ∞
0
dxN ρ(β )
N (x1, . . . , x N ; {m2}) . (5)
We now shift xi → xi + xk in the integrand of (4):
Ω (β )
N,k (x1, . . . , x k−1, x k; {m2}) = e−(N −k)βx k
Ξ (β )
N ({m2})
1
(N − k)!
k∏
i=1
(
xβ (ν +1)/ 2−1
i e−βx i
Nf∏
j=1
(xi + m2
j )
) k∏
i>j
|xi − xj|β
×
∫ ∞
0
N∏
i=k+1
(
dxi e−βx ixβ
i (xi + xk)β (ν +1)/ 2−1
Nf∏
j=1
(xi + m2
j + xk)
k−1∏
j=1
(xi + xk − xj)β
) N∏
i>j≥k+1
|xi − xj |β . (6)
To get the probability distributions of the Dirac operator eigenvalue s we must change the picture back to chiral
Gaussian ensembles, and take the microscopic limit
xi → 0
m2
j → 0 , N → ∞ , with the rescaled variables ζi = πρ (0)√ xi = √ 8N xi
µ j = πρ (0)mj =
√
8N mj
kept ﬁxed . (7)
In this large- N limit the diﬀerence between partition functions based on N − k and N eigenvalues becomes insigniﬁcant.
Moreover, one notices that the new terms in the integrand of (6) c an be interpreted as arising from new additional
2
fermion species, with the partition function now being evaluated in a ﬁ xed topological sector of eﬀective charge
ν = 1 + 2 /β . Taking into account the deﬁnition (2), we then get, with Z (β )
ν ({µ }) denoting the partition functions in
the microscopic limit,
ω (β )
k (ζ1, . . . , ζ k; {µ }) = lim
N →∞
( k∏
i=1
|ζi|
8N
)
Ω (β )
N,k ( ζ2
1
8N , . . . , ζ2
k
8N ; { µ 2
8N })
= const. e−βζ 2
k/ 8ζ
β ν +1
2 −ν −1+ 2
β
k
Nf∏
j=1
(µ 2
j + ζ2
k )
1
2 − 1
β
k−1∏
i=1
(
ζβ (ν +1)−1
i (ζ2
k − ζ2
i )
β
2 −1
Nf∏
j=1
(ζ2
i + µ 2
j )
) k−1∏
i>j
(ζ2
i − ζ2
j )β
Nf∏
j=1
µ ν
j
×
Z (β )
1+2/β (
√
µ 2
1 + ζ2
k , . . . ,
√
µ 2
Nf
+ ζ2
k ,
β
/bracehtipdownleft /bracehtipupright/bracehtipupleft/bracehtipdownright√
ζ2
k − ζ2
1 , . . . ,
√
ζ2
k − ζ2
1 , . . . ,
β
/bracehtipdownleft /bracehtipupright/bracehtipupleft/bracehtipdownright√
ζ2
k − ζ2
k−1, . . . ,
√
ζ2
k − ζ2
k−1,
β (ν +1)/ 2−1
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
ζk, . . . , ζ k )
Z (β )
ν (µ 1, . . . , µ Nf )
. (8)
This is the main result of our paper. It shows that the joint probabilit y distribution of the ﬁrst k eigenvalues is given,
apart from the relatively simple prefactor, by a ratio of ﬁnite-volum e partition functions. The new partition function
that enters in the numerator of Eq.(8) has the Nf original fermion masses shifted according to µ i →
√
µ 2
i + ζ2
k ,
contains β (k − 1) new fermions of masses
√
ζ2
k − ζ2
1 , . . . ,
√
ζ2
k − ζ2
k−1 (each mass β -fold degenerate), β (ν + 1)/ 2 − 1
additional degenerate fermion species of common mass ζk, and this whole partition function is evaluated in a sector of
ﬁxed topological charge ν = 1 + 2/β . While this topological index is fractional for β = 4, there is no diﬃculty with the
evaluation of the pertinent partition function. (Indeed, it can alte rnatively be viewed as a partition function in a sector
of topological charge ν = 0 and 3 additional massless fermions.) This expression entirely in ter ms of the eﬀective ﬁeld
theory partition functions strongly suggests that it should be possible to d erive these analytical expressions starting
directly from the eﬀective ﬁeld theory, perhaps partially quenched as in Ref. [8]. The proportionality constant in
Eq.(8) depends on the normalization conventions of the involved par tition functions. We ﬁx this numerical factor
uniquely by the requirement that the total probability of ﬁnding any given eigenvalue is normalized to unity.
Correlation functions of the rescaled eigenvalues {ζk1 , . . . , ζ kp− 1 , ζ k} are obtained from ω (β )
k (ζ1, . . . , ζ k; {µ }) by inte-
grating out the remaining eigenvalues in a cell 0 ≤ ζ1 ≤ · · · ≤ ζk. In particular, the distribution of the k-th smallest
eigenvalue ζ, p(β )
k (ζ; {µ }), is given by
p(β )
k (ζ; {µ }) =
∫ ζ
0
dζ1
∫ ζ
ζ1
dζ2 · · ·
∫ ζ
ζk− 2
dζk−1 ω (β )
k (ζ1, . . . , ζ k−1, ζ ; {µ }) . (9)
We note that this gives a very simple representation of the probabilit y distribution of the k-th smallest Dirac operator
eigenvalue. In particular, already for the most elementary case of just the lowest Dirac operator eigenvalue in the
β = 2 universality class we obtain a very simple expression for an arbitra ry topological sector ν. In the normalization
convention of, e.g. , [7],
p(2)
