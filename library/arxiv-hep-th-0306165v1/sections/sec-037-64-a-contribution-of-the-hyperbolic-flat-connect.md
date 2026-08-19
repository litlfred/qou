---
doc_id: arxiv-hep-th-0306165v1
doc_title: "which has many interesting connections with three-dimensi onal quantum gravity and ge- ometry of hyperbolic 3-manifolds. We show that, in the prese nce of a single knotted Wilson l"
section_id: sec-037-64-a-contribution-of-the-hyperbolic-flat-connect
section_title: "A Contribution of the “Hyperbolic” Flat Connection"
section_number: 6.4
pages: 50-52
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting connections with three-dimensi onal quantum gravity"
---
Now let us explain the relation to the volume conjecture and i ts generalization (5.12)
discussed in the previous section. In the path integral inte rpretation, the exponential
growth of the colored Jones polynomial means that its asympt otic behavior is dominated
by the non-trivial SL(2,C) ﬂat connection, associated with the hyperbolic structur e on
the knot complement, M . We shall denote this connection by A(hyperb). Comparing (5.12)
with (6.15), we conclude that the Chern-Simons action for th is complex-valued connection
is given by
SCS (A(hyperb)) =−2i
(
Vol(m) +i2π2CS (m)
)
(6.24)
For hyperbolic knots, the imaginary part of this expression does not vanish and, hence,
leads to the exponential growth of JN (K,q ) in the limit (5.11). Notice, that in order to
see this exponential growth it is crucial to allow the parame ter a = N/k to take generic
(non-rational) values, which is more natural in the SL(2,C) Chern-Simons theory, rather
than in the SU (2) theory, cf. Table 1.
This means that we have to ﬁnd a suitable generalization of th e Melvin-Morton con-
jecture (6.4) for non-rational values of a. Such a generalization can be found using path
integral arguments, similar to the above. Indeed, let us loo k at the loop expansion (6.15)
of the Chern-Simons-Witten invariant around the ﬂat connec tion A(hyperb). The leading
term in this expansion is given by the classical action (6.24 ). In the next, 1-loop term we
have
h0(A(hyperb)) = 0 , h 1(A(hyperb)) = 0 (6 .25)
This follows from eq.(6.17) and the fact that the ﬂat connect ion A(hyperb), associated
with the hyperbolic structure on the knot complement, is irr educible and rigid, so that
dim(Hhyperb) = 0. (In fact, the same relations describe the contribution of a non-trivial ﬂat
connection to the Reshetikhin-Turaev-Witten invariant fo r torus knots [29].) Therefore,
from (6.15) we get,
Z(hyperb)
SU (2) (WRj,k ) =
√
T (A(hyperb))e
ik
4π
(
S(hyperb)
CS +
∑
n>1(2π/k )nS(hyperb)
n
)
(6.26)
where we ignore a constant phase. In this expression, T (A(hyperb)) denotes the SL(2,C)
Ray-Singer torsion of the knot complement twisted by A(hyperb). Normalizing by
ZSU (2)(S3), we ﬁnd the asymptotic behavior of the N -colored Jones polynomial,
JN (K,q ) =
√
k√
2 sin(π/k)
√
T exp
(
k
2π (Vol(m) +i2π2CS (m)) + i
2
∞∑
n=1
(2π/k)nSn+1
)
49
It is convenient to write this expression in the logarithmic form:
logJN (K,q ) = k
2π (Vol(m) +i2π2CS (m)) + log
( √
kT√
2 sin(π/k)
)
+ i
2
∞∑
n=1
(2π/k)nSn+1
(6.27)
Notice, that this expansion is very similar to the perturbat ive expansion of the SL(2,C)
partition function, cf. (3.38) – (3.39). It would be very interesting to ﬁnd a better u nder-
standing of this relation.
Now, by analogy with (6.1), let us deﬁne a properly normalize d version of the colored
Jones polynomial that would remain ﬁnite in the limit (5.11) . In eq.(6.1) this was achieved
by dividing by the colored Jones polynomial of the unknot, wh ich automatically removed
the linear k-dependence from (6.22), as well as the universal factor of s in(πa). By con-
sidering speciﬁc examples (see below), we ﬁnd that the Ray-S inger torsion, T (A(hyperb)),
does not have the universal factor sin( πa) in the present case. Moreover, as can be eas-
ily seen from (6.27), the polynomial growth of JN (K,q ) comes from the normalization of
the Chern-Simons partition function (6.26) by ZSU (2)(S3). Therefore, in the present case,
it is natural to deﬁne the reduced Jones polynomial ~VN (K,q ) by restoring the original
normalization in (6.26),
~VN (K,q ) = JN (K,q )·ZSU (2)(S3)· exp
(
− k
2π (Vol(m) +i2π2CS (m))
)
(6.28)
where we also explicitly eliminated the exponential growth using the volume and the Chern-
Simons functions introduced in (5.7). It follows from the lo op expansion (6.26), that the
resulting Jones polynomial has the following asymptotic be havior,
~VN (K,q ) =
√
T (A(hyperb))· exp
(
i
2
∞∑
n=1
(2π/k)nSn+1
)
In particular, this expression remains ﬁnite in the limit (5 .11). Hence, as in the case of the
trivial ﬂat connection, we can consider the Melvin-Morton e xpansion of ~VN (K,q ),
~VN (K,q ) =
∑
m,n ≥0
~Dm,nN mhn (6.29)
The perturbative expansion (6.15) of the Chern-Simons path integral implies that the
coeﬃcients ~Dm,n should vanish unless m ≤ n. Moreover, the following analog of the
Melvin-Morton conjecture should hold in the limit (5.11), w ith non-rational a,
50
The Generalized Melvin-Morton Conjecture:
~Dm,n = 0 for m>n
∑
m≥0
~Dm,mam =
√
T (A(hyperb)) (6.30)
To get further insights into geometric information encoded in the power series (6.29),
following [90], let us write it in terms of the variable z =qN/ 2−q−N/ 2 = 2i sin(πa),
~VN (K,q ) =
∑
n≥0
~V (n)(K,z )hn =
∑
n≥0
hn∑
m≥0
~d(n)
m zm (6.31)
In contrast to the case of the reducible connection, the numb ers ~d(n)
m do not appear to be
integer. However, it is plausible that ~d(n)
m take values in Q(√−1), or in some other number
ﬁeld, which might be related to the arithmetic properties of the knot complement.
Questions:
1) What is the geometric interpretation of the numbers ~Dm,n and ~d(n)
m ?
2) What is the relation, if any, between ~d(n)
m and the coeﬃcients bm,n in the perturbative
expansion (3.39) of the SL(2,C) partition function?
Example. The Figure-eight Knot
As we explained above, in order to verify the generalized ver sion of the Melvin-
Morton conjecture (6.30), it is enough to check that the colo red Jones polynomial has
asymptotic expansion of the form (6.27). For the ﬁgure-eigh t knot we ﬁnd the following
asymptotic behavior of the colored Jones polynomial,
log JN (41, e2πi/k ) = k
2π Vol(41) + 3
2 log k + i
