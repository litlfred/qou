---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-022-52-asymptotics-of-distances-in-the-multi-dimensi
section_title: "Asymptotics of distances in the multi-dimensional setting"
section_number: 5.2
pages: 69-72
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
As in the one-dimensional case, a combination of the Laplace method
and of the norm estimates given by Corollary 5.6 yields under appropri-
ate hypotheses the asymptotics of dL(µn, νn) and of dTV(µn, νn), where
(νn)n∈N is a general scheme of approximation of the laws µn of the mod-φ
convergent random variables Xn in Zd. The only diﬀerence is that, for the
computation of the total variation distance, we shall need to assume the
order of approximation r to be larger than some minimal value ⌊d
2⌋.
Until the end of this paragraph, (Xn)n∈N is a sequence of random vari-
ables with values in Zd, which converges mod-φ with parameters λn →∞
and limit residue ψ(ξ1, . . . , ξd). In the sequel, we shall write (νn)n∈N a se-
quence of signed measures on Zd such that c
νn(ξ) = eλnφ(ξ) χn(ξ1, . . . , ξd),
with limn→∞χn(ξ1, . . . , ξd) = χ(ξ1, . . . , ξd). The multi-dimensional ana-
logue of the hypothesis (H1) is:
(H1d)
ψn(ξ)−χn(ξ) =
X
α1+···+αd=r+1
β(α1,...,αd)
n
(iξ1)α1 · · · (iξd)αd (1+oξ(1));
ψ(ξ)−χ(ξ) =
X
α1+···+αd=r+1
β(α1,...,αd) (iξ1)α1 · · · (iξd)αd (1+oξ(1))
with limn→∞βα
n = βα for any choice of index α = (α1, . . . , αd) with |α| =
r + 1. On the other hand, we write in the following ∥x∥2 = Pd
i=1(xi)2,
Hα(x) = Qd
i=1 Hαi(xi), σα = Qd
i=1(σi)αi, and ﬁnally
k −λnm
√λn σ
=
ki −λnmi
√λn σi

i∈[[1,d]]
if k ∈Zd.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1183
Proposition 5.7. — Under the assumption (H1d) with any r ⩾0, one
has
(λn)
r+d+1
2
(µn(k1, . . . , kd) −νn(k1, . . . , kd))
=

X
|α|=r+1
βα
σα
1
Qd
i=1(
√
2π σi)
e
−1
2

k−λnm
√
λnσ

2
Hα
k −λnm
√λn σ

+ o(1)
with a remainder that is uniform over Zd.
Proof. — The same arguments as in dimension 1 (d-dimensional Fourier
inversion formula and Laplace method) yield
µn(k1, . . . , kd) −νn(k1, . . . , kd)
≃
X
|α|=r+1
βα
n
(2π)d
Z
[−ε,ε]d
 d
Y
i=1
(iξi)αi eλn(φi(iξi)−imiξi) e−i (k−λnmi)ξi
!
dξ
(2π)d
≃
X
|α|=r+1
βα
n
(2π)
d
2
d
Y
i=1
 
1
(√λn σi)αi+1
Z
R
(ix)αi e−x2
2 e
−i

ki−λnmi
√
λn σi

x dx
√
2π
!
,
where the symbol ≃means that the two sides diﬀer by a o((λn)−r+d+1
2
)
which does not depend on k1, . . . , kd. We now observe that the same Her-
mite polynomials as in Proposition 3.2 appear.
□
We now use the same argument as in the proof of Theorem 3.3. The
sequence of lattices { k−λnm
√λn σ , k ∈Zd} becomes dense, therefore:
Theorem 5.8. — Under the hypothesis (H1d), one has
dL(µn, νn)
= sup
x∈Rd

e−∥x∥2
2

X
|α|=r+1
βα Hα(x)
σα


×
1 + o(1)
(Qd
i=1
√
2π σi) (λn)
r+d+1
2
.
The proof of the multi-dimensional analogue of Theorem 3.11 is a bit
more involved, but the main diﬃculty was lying in the proof of the norm
estimate (Corollary 5.6). In the following we ﬁx r ⩾⌊d
2⌋; then, r + 1 ⩾Kd.
The multi-dimensional version of the hypothesis (H2) is the following. We
assume the residues ψ, ψn, χ and χn to be of class C Kd on Td, with
∂δ(ψn −χn)(0) = ∂δ(ψ −χ)(0) = 0 for any |δ| < Kd. We also assume that
there exist families of coeﬃcients (βα
n)|α|=r+1,n∈N and (γα
n)|α|=r+2,n∈N, such
TOME 70 (2020), FASCICULE 3
1184
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
that for any multi-index δ with |δ| = Kd,
(H2d)
∂δ(ψn −χn)(ξ) = i|δ|


X
|ρ|=r+1−|δ|
βρ+δ
n
(ρ + δ)!
ρ!
(iξ)ρ
+
X
|ρ|=r+2−|δ|
γρ+δ
n
(ρ + δ)!
ρ!
(iξ)ρ(1 + oξ(1))

;
∂δ(ψ −χ)(ξ) = i|δ|


X
|ρ|=r+1−|δ|
βρ+δ (ρ + δ)!
ρ!
(iξ)ρ
+
X
|ρ|=r+2−|δ|
γρ+δ (ρ + δ)!
ρ!
(iξ)ρ(1 + oξ(1))


with limn→∞βα
n = βα and limn→∞γα
n = γα. Here, given a multi-index α,
we write α! = Q
i=1(αi)! and (iξ)α = Qd
i=1(iξi)αi. These hypotheses are
satisﬁed e.g. if the convergences ψn →ψ and χn →χ occur in C r+2(Td),
and if (νn)n∈N is the scheme of approximation of order r of the sequence
of random variables (Xn)n∈N (its deﬁnition in dimension d ⩾2 is similar
to the deﬁnition in dimension 1 given in Example 1.11, see also the two
worked examples hereafter).
Under the hypothesis (H2d), if one wants to prove a bound on dTV(µn, νn)
of order O((λn)−r+1
2 ), then one can replace νn with the measure ρn deﬁned
by the Fourier transform
c
ρn(ξ) = eλnφ(ξ)

ψn(ξ) −
X
|α|=r+1
βα
n
d
Y
i=1
(eiξi −1)αi

.
Indeed, denoting f
ψn(ξ) the residue associated to ρn, the hypothesis (H2d)
implies that, for any |δ| ⩽Kd,

∂δ(f
ψn −χn)(ξ)

 ⩽C |ξ|r+2−|δ|
with a constant C that is uniform, and also valid for the partial derivatives
|∂δ( eψ−χ)(ξ)|. This bound is the only one useful in the proof of Theorem 5.3
and its Corollary 5.6, and therefore, one can apply Corollary 5.6 with a
parameter r + 1 instead of r. We thus get
dTV(ρn, νn) = O
 
(log λn)r+2
(λn)
r+1
2 + 1
4
!
= o
 
1
(λn)
r+1
2
!
.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1185
From there, the proofs are essentially identical to the one dimensional case
(Theorem 3.11), and one obtains:
Theorem 5.9. — Consider a general approximation scheme (νn)n∈N of
a mod-φ convergent sequence (Xn)n∈N in Zd. We assume that r ⩾⌊d
2⌋and
that the hypothesis (H2d) is satisﬁed. Then,
dTV(µn, νn) =
1 + o(1)
(2π)
d
2 (λn)
r+1
2


Z
Rd e−∥x∥2
2

X
|α|=r+1
βα Hα(x)
σα

dx

.
Last, the discussion of Section 3.4 holds mutatis mutandis in the multi-
dimensional setting, and if ∥χn −χ∥C Kd is asymptotically smaller than any
negative power of λn, then one can replace (νn)n∈N by the derived scheme
(σn)n∈N with constant residue and keep the conclusions of Theorems 5.8
and 5.9.
