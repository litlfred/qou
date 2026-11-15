---
doc_id: arxiv-hep-th-9212088v1
doc_title: "arXiv:hep-th/9212088v1 14 Dec 1992"
section_id: sec-004-4-sum-rules-for-one-and-two-ﬂavors
section_title: "Sum rules for one and two ﬂavors"
section_number: 4
pages: 9-12
source_pdf: 9212088v1.pdf
source_sha256: ecb2c02ec6fe11bd
toc_source: inferred
doc_brief: "arXiv:hep-th/9212088v1 14 Dec 1992 — We construct a random matrix model that, in the large N limit, reduces to the low energy limit of the QCD partition function put forward by Leutwyler and Smilga."
---
Sum rules for moments of the inverse squares of the eigenvalues of the Dirac operator
can be derived for an arbitrary number of ﬂavors and for any value of the total topological
charge [2]. In this section we only present a derivation for the simplest two cases of one
ﬂavor and of two ﬂavors with equal masses. Proofs of the general results can be found in
[2].
For Nf = 1 there is no integration and the result for the ratio of the massive and
massless partition function is particularly simple
ZNf =1 = exp(NmΣ cos θ),
(4.1)
which was ﬁrst obtained in [2].
In the case of two ﬂavors the integral over SU(2) can be performed for an arbitrary
mass matrix. Here, we restrict ourselves to the simpler case of equal quark masses. In
this case the ratio of the massive and the massless partition function reduces to
ZNf =2 =
Z 2π
0
dφ
π sin2 φ
2 exp(2NmΣ cos φ
2 cos θ
2),
(4.2)
where the factor sin2 φ
2 results from the invariant measure of SU(2).
The integral is
elementary and results in
ZNf=2 = I1(2mNΣ cos θ
2)
mNΣ cos θ
2
.
(4.3)
The partition function can also be evaluated by writing the fermion determinant as a
product over eigenvalues. For Nf = 1, we obtain sum rule
exp(ΣmN cos θ) =< mν Y
n
′(1 + m2
λ2n
) >Z(m=0),
(4.4)
where the average is with respect to the partition function Z with m = 0, which also
includes the weight factor
Q ′λ2
n involving the product of the nonzero eigenvalues of the
Dirac operator. The exclusion of zero eigenvalues in the product is denoted by a prime.
For two ﬂavors a similar sum rule can be derived
Y
x1n≥0
(1 + 4m2N2 cos2 θ
2
x2
1n
) =< m2ν Y
n
′(1 + m2
λ2n
)2 >Z(m=0) .
(4.5)
Here, the x1n is the n’th zero of the Bessel function J1. By expanding both the r.h.s.
and the l.h.s. of eqs. (4.4) and (4.5) in powers of m we obtain sum rules for the inverse
moments of the eigenvalues λn. Additional sum rules for Nf = 2 can be derived from
the expansion in powers of both mu and md of the general expression for the partition
function.
The sum rules (4.4) and (4.5) are for a ﬁxed value of θ. However, we will investigate
the validity of the Leutwyler-Smilga sum rules in an interacting instanton vacuum where,
for technical reasons, the total topological is taken to be zero. The corresponding partition
function Z0 is given by the Fourier transform of Z(θ),
Z0 =
Z 2π
0
dθ
2πZ(θ).
(4.6)
which can be derived from the the decomposition
Z =
X
ν
eiνθZν.
(4.7)
For one and two ﬂavors, the integrals over θ are elementary. The results
Z0
=
I0(NmΣ)
for
Nf = 1,
(4.8)
Z0
=
I2
0(NmΣ) −I2
1(NmΣ)
for
Nf = 2,
(4.9)
were ﬁrst derived by Leutwyler and Smilga [2]. Sum rules are obtained by equating (4.8)
and (4.9) to the r.h.s. of (4.4) and (4.5) restricted to zero topological charge, respectively.
For Nf = 1 one ﬁnds
I0(NmΣ) =<
Y
n
(1 + m2
λ2n
) >ν=0,
(4.10)
and for Nf = 2 we have
I2
0(NmΣ) −I2
1(NmΣ) =<
Y
n
(1 + m2
λ2n
)2 >ν=0 .
(4.11)
The expansion of both sides of this equation in powers of mN yields sum rules for moments
of the inverse eigenvalues of the Dirac operator. The ﬁrst two sum rules are
<
X
n>0
1
N2λ2n
>ν=0
=
Σ2
4Nf
,
(4.12)
< (
X
n>0
1
N2λ2n
)2 >ν=0 −<
X
n>0
1
N2λ2n
>2
ν=0
=
<
X
n>0
1
N4λ4n
>ν=0 −
Σ4
16N2
f (Nf + 1).
(4.13)
As was shown by Leutwyler and Smilga, both sum rules hold for arbitrary Nf and also
be worked out for arbitrary topological charge. The only modiﬁcation is to replace Nf
by Nf + |ν|. In the case of two or more ﬂavors additional sum rules can be derived by
varying the quarks masses independently [2]. We only quote the result
<
1
N4λ4n
>ν=0=
Σ4
16Nf(N2
f −1).
(4.14)
Again, the result for arbitrary topological charge is obtained by replacing Nf by Nf + |ν|.
Formally, this sum rule diverges for Nf = 1. That this is indeed the case can be understood
from the behavior of the spectral density at small λ. For N+ = N−we expect ρ(λ) ∼
λNf+2, where the factor λNf originates from the fermion determinant and the factor λ2
from the Jacobian of the unitary transformation that diagonalizes the overlap matrix.
The above sum rules diverge for Nf = 0. Consequently, we expect that in this case, and
therefore in the quenched approximation, that the thermodynamic limit of the spectral
density near zero is approached in a completely diﬀerent way.
The sum rules (4.12-14) can be expressed in the microscopic spectral density by writing
the sum over the eigenvalues as the integral
X
1
Npλp
n =
Z dx
xp ρS(x)|mN=0.
(4.15)
The second sum rule expresses an integral over the correlation function < ρS(x)ρS(x′) >ν=0
in terms of integrals over the average microscopic spectral density < ρS(x) >ν=0.
Finally, let us write down a sum rule for nonzero values of mN. In the case of one
ﬂavor one obtains from the inﬁnite product expansion for the Bessel function I0,
X
n
mNΣ2
x2
0n + m2N2Σ2 =
Z ∞
0
dx < ρS(x)|mN ﬁxed >ν=0
mN
x2 + m2N2,
(4.16)
where x0n is the n’th zero of the Bessel function J0. One is tempted to invert this equality
in order to obtain an analytical answer for the microscopic spectral density. Since ρS
depends on mN there is no unique solution, but a trivial solution can be written down
readily,
ρS(x) =
X
n
δ(x −x0n
Σ ).
(4.17)
Because there is no reason to believe that the dispersion (4.13) is zero, we do not expect
that this is the exact microscopic level density.
In appendix A it is shown that for one ﬂavor sum rules can also be derived at ﬁnite
N. These results provide an explicit proof that the thermodynamic limit has been taken
correctly.
