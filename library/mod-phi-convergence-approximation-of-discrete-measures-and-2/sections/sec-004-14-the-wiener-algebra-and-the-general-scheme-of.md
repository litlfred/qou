---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-004-14-the-wiener-algebra-and-the-general-scheme-of
section_title: "The Wiener algebra and the general scheme of approximation"
section_number: 1.4
pages: 10-14
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
approximation
As explained before, we shall be interested in more general approximation
schemes, with signed measures νn that are closer to µn than the basic
scheme. When d = 1, the appearance of signed measures is natural in
the setting of the Wiener algebra of absolutely convergent Fourier series
(see [37, 39]):
TOME 70 (2020), FASCICULE 3
1124
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Definition 1.8. — The Wiener algebra A = A (T) is the algebra of
continuous functions on the circle whose Fourier series converges absolutely.
It is a Banach algebra for the pointwise product and the norm
∥f∥A :=
X
n∈Z
|cn(f)|,
where cn(f) denotes the Fourier coeﬃcient
R 2π
0
f(eiθ) e−inθ dθ
2π.
Note that the characteristic function of any signed measure µ on Z be-
longs to the Wiener algebra, with
∥bµ∥A =
X
n∈Z
|cn(bµ)| =
X
n∈Z
|µ(n)| = ∥µ∥TV
equal to the total variation norm of the measure. Thus, A is the right
functional space in order to use harmonic analysis tools when dealing with
(signed) measures. To the best of our knowledge, this interpretation of the
total variation distance as the norm of A has not been used before. On the
other hand, another important property of the Wiener algebra is:
Proposition 1.9 (Wiener’s 1
f theorem). — Let f ∈A . Then f never
vanishes on the circle if and only if 1
f ∈A .
We refer to [45] for a short proof of the Wiener theorem. As a conse-
quence, if Xn is a Z-valued random variable and if ν is an inﬁnitely divisible
distribution with exponent φ, then the deconvolution residue
ψn(ξ) = E[eiξXn] e−λnφ(ξ)
belongs to A , so it is a convergent Fourier series ψn(ξ) = P∞
k=−∞ak,n eikξ.
The idea is then to replace this residue ψn by a simpler residue χn ∈A ,
which after reconvolution by eλnφ(ξ) yields a signed measure approximating
the law of Xn. We are thus led to:
Definition 1.10. — Let (Xn)n∈N be a sequence of random variables
in Zd that is mod-φ convergent with parameters (λn)n∈N. A general ap-
proximation scheme for (Xn)n∈N is given by a sequence of discrete signed
measures (νn)n∈N on Zd, such that
c
µn(ξ) = E[ei⟨ξ | Xn⟩] = eλnφ(ξ) ψn(ξ);
c
νn(ξ) = eλnφ(ξ) χn(ξ),
with limn→+∞ψn(ξ) = ψ(ξ) and limn→+∞χn(ξ) = χ(ξ). Here, the residues
ψn, ψ, χn and χ are functions on the torus Td = (R/2πZ)d that have ab-
solutely convergent Fourier series, and with χn(0) = χ(0) = 1 (hence,
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1125
νn(Zd) = 1). The convergence of the residues ψn →ψ and χn →χ is as-
sumed to be at least uniform on the torus, that is in the space of continuous
functions C 0(T).
The basic approximation scheme is the case when χn(ξ) = χ(ξ) = 1.
The residues χn and χ will typically be trigonometric polynomials, and
they will enable us to enhance considerably the quality of our discrete
approximations.
Example 1.11. — An important case of approximation scheme in the
sense of Deﬁnition 1.10 is the approximation scheme of order r ⩾1. Suppose
that d = 1 and that the functions ψn(ξ) can be represented on the torus as
absolutely convergent series
ψn(ξ) = 1 +
∞
X
k=1
bk,n (eiξ −1)k +
n
X
k=1
ck,n (e−iξ −1)k.
The coeﬃcients ak,n of ψn(ξ) = P∞
k=−∞ak,n eikξ are related to the coeﬃ-
cients bk,n and ck,n by the equations
bk,n =
X
l⩾k
l
k

al,n ;
ck,n =
X
l⩾k
l
k

a−l,n
for all k ⩾1. Set then
χ(r)
n (ξ) = P (r)
n (eiξ) = 1 +
r
X
k=1
bk,n (eiξ −1)k +
r
X
k=1
ck,n (e−iξ −1)k.
The χ(r)
n (ξ) are the Laurent polynomials of degree r that approximate the
residues ψn around 0 at order r ⩾1. Then, if Xn is a random variable
with law µn with characteristic function c
µn(ξ) = eλnφ(ξ) ψn(ξ), the ap-
proximation scheme of order r of µn is given by the signed measures ν(r)
n ,
with
d
ν(r)
n (ξ) = eλnφ(ξ) χ(r)
n (ξ).
We shall prove in Section 3 that dL(µn, ν(r)
n ), dK(µn, ν(r)
n ) and dTV(µn, ν(r)
n )
get smaller when r increases; in particular, ν(r⩾1)
n
is asymptotically a better
approximation of µn than the basic scheme ν(0)
n .
One can give a functional interpretation to the approximation schemes of
order r ⩾1. Denote as before P (r)
n
the Laurent approximation of order r of
ψn, and introduce the shift operator S on functions f : Z →C, deﬁned by
(Sf)(k) = f(k + 1).
TOME 70 (2020), FASCICULE 3
1126
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
If ν(r)
n
is the signed measure with Fourier transform given by
d
ν(r)
n (ξ) = eλnφ(ξ) P (r)
n (eiξ),
then for any square-integrable function f : Z →C, if bf(ξ) = P
k∈Z f(k) eikξ,
then
ν(r)
n (f) =
X
k∈Z
ν(r)
n ({k}) f(k) = 1
2π
Z 2π
0
d
ν(r)
n (ξ) bf(ξ) dξ
= 1
2π
Z 2π
0
d
ν(0)
n (ξ) P (r)
n (eiξ) bf(ξ) dξ
= 1
2π
Z 2π
0
d
ν(0)
n (ξ)
\
(P (r)
n (S)f)(ξ) dξ
= ν(0)
n (P (r)
n (S)f).
Moreover, the operator P (r)
n (S) is a linear combination of discrete diﬀerence
operators:
P (r)
n (S) = id +
r
X
k=1
bk,n (∆+)k +
r
X
k=1
ck,n (∆−)k
with
(∆k
+(f))(j) =
k
X
l=0
(−1)k−l
k
l

f(j + l);
(∆k
−(f))(j) =
k
X
l=0
(−1)k−l
k
l

f(j −l).
Therefore:
Proposition 1.12. — In the previous setting, if (ν(r)
n )n∈N is the
approximation scheme of order r
⩾
1 of a sequence of probability
measures (µn)n∈N that is mod-φ convergent, then for any square-integrable
function f,
ν(r)
n (f) = E[(P (r)
n (S)(f))(Yn)],
where Yn follows an inﬁnitely divisible law with exponent λnφ. Thus, to
estimate at order r the expectation µn(f) = E[f(Xn)]:
(1) one replaces Xn by an inﬁnitely divisible random variable Yn;
(2) and one also replaces the function f by P (r)
n (S)(f), which is better
suited for discrete approximations.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1127
Remark 1.13. — Our notion of approximation scheme should be com-
pared to the one of [34], which is the particular case where the reference
inﬁnitely divisible law is Poissonian, and the residues χn are constant equal
to one. One of the main interest of our approach is that we are able to con-
struct better schemes of approximation, by allowing quite general residues
χn in the Fourier transform of the laws νn that approximate the ran-
dom variables Xn. On the other hand, we consider only three distances
among those studied in [34], but there should be no diﬃculty in adapting
our results to the other distances, such as the Wasserstein metric and the
Hellinger/Matusita metric.
Remark 1.14. — The approximation scheme of order r ⩾1 can be con-
sidered as a discrete analogue of the Edgeworth expansion in the central
limit theorem, which is with respect to the Gaussian approximation, and
thus gives results for a diﬀerent scale of ﬂuctuations [47, Chapter VI].
