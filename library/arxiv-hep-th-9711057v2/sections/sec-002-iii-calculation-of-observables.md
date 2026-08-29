---
doc_id: arxiv-hep-th-9711057v2
doc_title: "The microscopic spectrum of the QCD Dirac operator with finite quark masses"
section_id: sec-002-iii-calculation-of-observables
section_title: "CALCULATION OF OBSERVABLES"
section_number: III
pages: 6-6
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
doc_brief: "The microscopic spectrum of the QCD Dirac operator with finite quark masses — 7 sections: INTRODUCTION; RANDOM-MATRIX THEORY FOR FINITE QU; CALCULATION OF OBSERVABLES"
---
The microscopic spectral correlators, in particular the microscopic spectral density, are computed in Sec. III A. In
Sec. III B, we derive the distribution of the smallest eigenvalue.
A. Microscopic spectral correlators and density
To calculate the spectral correlations, we insert the polynomials p(Nf)
n
(x, M) in Eq. (11) for the kernel
K(Nf)
N
(x, y, M).
The microscopic limit is obtained according to Eq. (1) by rescaling energies and quark masses
by 2NΣ. We deﬁne λ = 2NΣ√x and mf = 2NΣMf. In the limit N →∞, we want both λ and mf to be of order
unity. The quenched approximation then corresponds to taking mf →∞(or, of course, setting Nf = 0). In the limit
mf →0, our results must reduce to those obtained earlier in the chiral limit [5]. After rescaling the parameters one
uses the asymptotic relation limN→∞L(α)
N (z/N)/N α = z−α/2Jα(2√z), where Jα denotes the Bessel function of the
ﬁrst kind and order α. To obtain the correct large-N limit one has to use the recurrence relations for the Laguerre
polynomials [23] in Eq. (13). The properties of the determinant can be used to simplify the expression. After summing
up one uses
z2
N
α
L(α)
N−1
z2
N

=
N
N + α
z2
N
α
L(α)
N
z2
N

+
1
N + α
z2
N
α+1
L(α+1)
N
z2
N

−
1
N + α
z2
N
α+1
L(α)
N
z2
N

.
(25)
Note that the ﬁrst, second, and third term on the right-hand side is of O(1), O(1/N), and O(1/N 2), respectively.
Using the properties of the determinant and collecting the terms of O(1) carefully, one obtains the microscopic limit
of (11). We arrive at
K(Nf)(λ, λ′, m) = lim
N→∞
2
√
λλ′
(2NΣ)2 K(Nf)
N

(λ/2NΣ)2 , (λ′/2NΣ)2 , m/2NΣ

=
√
λλ′
λ′2 −λ2
B(Nf)(λ, m) PNf
f=0 eB(Nf )
f
(λ′, m) −B(Nf)(λ′, m) PNf
f=0 eB(Nf)
f
(λ, m)
[C(Nf)(m)]2 QNf
f=1
q
(λ2 + m2
f)(λ′2 + m2
f)
,
(26)
where the normalization C(Nf)(m) is the microscopic limit of the normalization C(Nf)
N
(M) of Eq. (14),
C(Nf )(m) =
lim
N→∞C(Nf )
N
(m/2NΣ) = det
h
mf−1
f ′
If−1(−mf ′)
i
f,f ′=1,...,Nf
.
(27)
The determinant B(Nf)(λ, m) in Eq. (26) is given by
B(Nf )(λ, m) =

J0(λ)
I0(−m1)
· · ·
I0(−mNf )
λJ1(λ)
m1I1(−m1)
· · ·
mNf I1(−mNf )
...
...
...
λNf JNf (λ) mNf
