---
doc_id: arxiv-hep-th-9212088v1
doc_title: "arXiv:hep-th/9212088v1 14 Dec 1992"
section_id: sec-002-2-random-matrix-model
section_title: "Random matrix model"
section_number: 2
pages: 3-6
source_pdf: 9212088v1.pdf
source_sha256: ecb2c02ec6fe11bd
toc_source: inferred
doc_brief: "arXiv:hep-th/9212088v1 14 Dec 1992 — We construct a random matrix model that, in the large N limit, reduces to the low energy limit of the QCD partition function put forward by Leutwyler and Smilga."
---
was inspired by the semiclassical approximation to the QCD partition function where
instantons are the main degrees of freedom [10, 11, 12]. Therefore, it is natural to check
the validity of these sum rules for an instanton liquid model [13] of the QCD vacuum, a
task which is carried out in section 5. Concluding remarks are made in section 6. Finally,
in appendix A sum rules for a ﬁnite number of degrees of freedom are derived.
2. Random matrix model
The Euclidean QCD partition function for Nf ﬂavors and nonzero vacuum angle θ can
be written as
ZQCD =
X
ν
eiθν <
Nf
Y
f=1
Y
n
′(λ2
n + m2
f)mν
f >Sν(A),
(2.1)
where the product is over the positive eigenvalues of the Dirac operator, and the aver-
age < · · · >Sν(A) is over gauge ﬁeld conﬁgurations with topological quantum number ν
weighted by the gauge ﬁeld action Sν(A). The topological part of the action, exp iθν,
has been displayed explicitly. Here and below, the mass matrix is taken to be diago-
nal. According the the Atiyah-Singer theorem, the Dirac equation in a gauge ﬁeld with
topological quantum number ν has exactly ν zero eigenvalues. However, conﬁgurations
with zero total topological charge may actually be composed of spatially well-separated
components with opposite topological charge. Such conﬁgurations will give rise to al-
most zero modes and thus will play an important role in the chiral dynamics of the QCD
partition function. Our starting point is that the chiral properties of the QCD partition
function are determined by zero modes and almost zero modes only. Although it is not
necessary for the sake of the argument, it is instructive to think of the ﬁeld conﬁgurations
as a superposition of N+ instantons and N−anti-instantons. Each isolated instanton or
anti-instanton has exactly one fermionic zero mode with a deﬁnite chirality [14]. In total
we have ν = N+ −N−exact zero modes. At ﬁnite separation of instantons and anti-
instantons the remaining modes are no longer exact zero modes of the Dirac equation and
give rise to nonzero overlap matrix elements T of the Dirac operator [15].
A model describing the zero mode part of the QCD partition function with N zero
modes or almost zero modes in the Euclidean volume V is deﬁned by
Z(θ) =
X
N
µ(N)
X
N+
 
N
N+
!
eiθ(N+−N−)
Z
DTP(T)
Nf
Y
f
det
 
mf
iT
iT †
mf
!
.
(2.2)
Zero modes of each chirality are treated as independently distributed identical particles,
hence the binomial factor. The distribution function µ(N) of the total number of zero
modes N = N++N−is peaked at some average value N with a width that is much smaller
than N. As long as a large number of diﬀerent values of N contribute to the partition
function with roughly equal probability2, our results do not depend on the detailed shape
of µ(N). The average over all gauge ﬁeld conﬁgurations in eq. (2.1) is replaced by an
average over gaussian distributed overlap matrix elements with distribution function given
by
P(T) = exp(−N
2λ2TT †).
(2.3)
The integration measure DT is the Haar measure. The structure of the overlap matrix,
with oﬀ-diagonal blocks T and T † and diagonal blocks equal to the quark masses mf times
the identity, is dictated by the chirality of the zero modes. The matrix T is a N+ × N−
matrix, and for zero quark masses, the total overlap matrix has |N+ −N−| exact zero
eigenvalues. The density N/V of the total number of zero modes is kept ﬁxed. As in
the instanton liquid approximation to the QCD partition function [16], it is considered
to be an external parameter. The thermodynamic limit can thus be taken by letting
N →∞, where here and below we will omit the bar. A similar model with N+ = N−was
considered in [17, 18].
The order parameter in the study of chiral symmetry breaking is the quark condensate
< ¯qfqf > deﬁned by
< ¯qfqf >= lim
mf →0 lim
N→∞−1
N
d
dmf
log Z(θ),
(2.4)
where the order of the limits should be taken as indicated in the formula. In general,
< ¯qfqf > depends on θ. Its value at θ = 0 in the limit where for all ﬂavors mf →0 is
approached from above is denoted by −Σ. By writing the determinant as the product
2If µ(N) ∼δ(N −N) the parity of N+ −N−is the same as the parity of N = N+ + N−, and the
partition function has the additional symmetry Z(θ = 0) = Z(θ = π).
Q′(λ2
n + m2
f) one obtains the Banks-Casher formula [6] for Σ
Σ = π < ρC(0) >Z(θ=0),
(2.5)
where the average < · · · >Z(θ) is with respect to the partition function (2.2) (or (2.1) in
the case of QCD). The continuum spectral density is deﬁned by
ρC(λ) =
lim
all mf ↓0 lim
N→∞
1
N ρ(λ),
(2.6)
and the spectral density ρ(λ) is
ρ(λ) =
X
δ(λ −λn),
(2.7)
where the eigenvalues ±λn are the nonzero eigenvalues of the overlap matrix in the chiral
limit.
We will also consider a diﬀerent limit of the derivative with respect of m of the partition
function, namely,
lim
N→∞
Nmf ﬁxed
1
Np
dp
dmp
f
log Z(θ).
(2.8)
Let us consider the case p = 1 in more detail. Again writing the determinant as a product
over eigenvalues, one ﬁnds
lim
N→∞
Nmf ﬁxed
*X
n>0
Nmf
λ2nN2 + m2
fN2
+
Z(θ)
=
lim
N→∞
Nmf ﬁxed
Z ∞
0
dx

 1
N ρ( x
N )

Z(θ)
Nmf
x2 + m2
fN2.
(2.9)
What enters in this expression is what we call the microscopic spectral density deﬁned by
ρS(x) =
lim
N→∞
Nmf ﬁxed
1
N ρ( x
N ),
(2.10)
as opposed to the continuum spectral density deﬁned by in eq. (2.6). In this limit, the
spectral density function near zero is enlarged proportional to the size (given by N) of
the system. Note that ρS(x) depends on Nmf.
