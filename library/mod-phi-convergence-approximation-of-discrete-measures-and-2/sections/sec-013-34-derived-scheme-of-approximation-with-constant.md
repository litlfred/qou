---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-013-34-derived-scheme-of-approximation-with-constant
section_title: "Derived scheme of approximation with constant residue"
section_number: 3.4
pages: 35-38
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
To conclude this section, let us simplify a bit the general setting of ap-
proximation of discrete measures presented in Deﬁnition 1.10. Until now,
we have worked with measures νn such that
c
νn(ξ) = eλnφ(ξ) χn(ξ),
where the residues χn(ξ) converge to a residue χ(ξ), and on the other
hand approximate the residues ψn(ξ) associated to the random variables
Xn. For instance, χn(ξ) can be the Laurent polynomial of degree r in eiξ
derived from ψn(ξ) (scheme of approximation of order r). In this setting, the
residues χn(ξ) are usually very good approximations of the residues ψn(ξ),
but on the other hand they vary with n, which is quite a complication
for explicit computations. Hence, for applications, it is simpler to work
with a constant residue χ(ξ) that does not depend on n. This leads to the
following deﬁnition:
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1149
Definition 3.14. — Let (νn)n∈N be a general scheme of approximation
of a sequence of random variables (Xn)n∈N that converges mod-φ with
parameters λn. The derived scheme of approximation with constant residue
is the new scheme (σn)n∈N, deﬁned by the Fourier transforms
c
σn(ξ) = eλnφ(ξ) χ(ξ),
where χ(ξ) = limn→∞χn(ξ) is the limit of the residues of the law νn (with
the notations of Deﬁnition 1.10).
Example 3.15. — Suppose that νn = ν(r)
n
is the scheme of approximation
of order r of (Xn)n∈N (see Example 1.11), and that the convergence ψn →ψ
occurs in C r(T). Then, the derived scheme with constant residue (σn)n∈N
is deﬁned by the Fourier transforms
c
σn(ξ) = eλnφ(ξ) P (r)(eiξ),
where P (r)(eiξ) is the Laurent polynomial of degree r associated to the limit
ψ of the mod-φ convergence. Thus, to compute σn(f) with f : Z →C, one
can take a random variable Yn with law of exponent λnφ, and then calculate
E[(P (r)(S)f)(Yn)]
where T = P (r)(S) is a ﬁxed linear operator, which is a ﬁnite linear com-
bination of discrete diﬀerence operators. This is clearly convenient for con-
crete applications.
Informally, if the derived scheme with constant residue (σn)n∈N is suﬃ-
ciently close to the initial scheme (νn)n∈N, then the conclusions of Theo-
rems 3.3, 3.6 and 3.11 hold also for (σn)n∈N (under the appropriate con-
dition (H1) or (H2) for (νn)n∈N). Practically, this happens as soon as the
size of χn −χ is negligible in comparison to negative powers of λn. More
precisely, we have:
Theorem 3.16. — Let (νn)n∈N be a general scheme of approximation
of a sequence (Xn)n∈N that is mod-φ convergent. We denote (σn)n∈N the
derived scheme with constant residue.
(1) Suppose that (νn)n∈N satisﬁes the hypothesis (H1). If ∥χn −χ∥∞=
o

1
(λn)
r
2 +1

, then
dL(µn, σn) = |β| |Gr+1(zr+2)|
√
2π (σ2λn)
r
2 +1 + o

1
(λn)
r
2 +1

.
TOME 70 (2020), FASCICULE 3
1150
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
(2) Suppose that (νn)n∈N satisﬁes the hypothesis (H1). If ∥χ′
n−χ′∥∞=
o

1
(λn)
r+1
2

, then
dK(µn, σn) = |β| |Gr(zr+1)|
√
2π (σ2λn)
r+1
2
+ o
 
1
(λn)
r+1
2
!
.
(3) Suppose that (νn)n∈N satisﬁes the hypothesis (H2). If ∥χ′
n−χ′∥∞=
o

1
(λn)
r
2 + 5
4

, then
dTV(µn, σn) =
|β|
√
2π (σ2λn)
r+1
2
Z
R
|Gr+1(α)| dα

+ o
 
1
(λn)
r+1
2
!
.
Proof. — In each case, we have to bound the distance between νn and
the derived scheme σn. For the local distance, one has
dL(νn, σn) = sup
k∈Z

Z
T
(χn(ξ) −χ(ξ)) eλnφ(ξ) e−ikξ dξ
2π

⩽∥χn −χ∥∞= o

1
(λn)
r
2 +1

,
hence the estimate on dL(µn, σn). For the Kolmogorov distance, notice that

χn(ξ) −χ(ξ)
1 −e−iξ

 ⩽∥χ′
n −χ′∥∞

ξ
1 −e−iξ

 ⩽π ∥χ′
n −χ′∥∞
for any ξ ∈(−π, π). Therefore,
dK(νn, σn) = sup
k∈Z

Z
T
χn(ξ) −χ(ξ)
1 −e−iξ
eλnφ(ξ) e−ikξ dξ
2π

⩽π∥χ′
n −χ′∥∞= o
 
1
(λn)
r+1
2
!
,
hence the estimate on dK(µn, σn). Last, for the total variation distance, we
use Proposition 2.1:
dTV(νn, σn) =

(χn −χ)(ξ) eλnφ(ξ)

A
⩽∥χn −χ∥∞+ CH ∥((χn −χ)′(ξ) + λn φ′(ξ) (χn −χ)(ξ)) eλnφ(ξ)∥L 2
⩽π∥χ′
n −χ′∥∞+ CH (∥χ′
n −χ′∥∞+ λn ∥φ′∥∞∥χn −χ∥∞) ∥eλnφ(ξ)∥L 2
⩽∥χ′
n −χ′∥∞

π + CH(1 + πλn ∥φ′∥∞) ∥eλnφ(ξ)∥L 2

.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1151
Since |eφ(ξ)| ⩽e−Mξ2, we have the estimate ∥eλnφ(ξ)∥L 2 = O(
1
(λn)1/4 ), so
in the end
dTV(νn, σn) = O

∥χ′
n −χ′∥∞(λn)
3
4

= o
 
1
(λn)
r+1
2
!
,
whence the estimate on dTV(µn, σn).
□
