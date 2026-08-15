---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-002-21-parametrized-vc
section_title: "Parametrized VC"
section_number: 2.1
pages: 6-9
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
doc_brief: "Quantum Field Theory and the Volume Conjecture — 14 sections: Preliminaries; The many dimensions of the volume ; Parametrized VC"
---
The original volume conjecture only held for a special root of unity q =e
2πi
N . In order
to generalize to arbitrary q =e
2πi
k , the appropriate limit to consider is
k→∞ , N →∞ , u :=iπN
k ﬁxed (2.1)
5One method involves analytically continuing the summand as a ratio of quantum dilogarithm
functions (cf. [17, 11]), approximating the sum by an integral, and evaluating it at its saddle point.
5
(or q→ 1, qN =e2u ﬁxed). The question, then, is how to understand
lim
k,N→∞
JN(K;q)1/k ? (2.2)
The answer, described in [10], uses the fact that in correspondence with the “defor-
mation” in the colored Jones polynomial, there exists a one-parameter deformation of
the hyperbolic structure on a knot complement S3\K. To understand this, let µ be a
small loop linking the excised knotK, as in Figure 2a. In terms of ﬂatSL(2, C) connec-
tions, the geodesically complete hyperbolic metric has a parabolic SL(2, C) holonomy
around µ,
Hol(µ, complete) =±
(1 1
0 1
)
, (2.3)
whereas the incomplete, u-deformed hyperbolic metric/SL(2, C) connection is deﬁned
to have a holonomy conjugate to
Hol(µ,u ) =
(eu 1
0 e−u
)
. (2.4)
(As long as eu⁄=e−u, this deformed holonomy is also conjugate to the purely diagonal
matrix diag(eu,e−u).) The resulting metric is not complete. For example, when u is
purely imaginary, theu-deformed metric has a conical cusp of angle 2Im(u) at the knot
K.
The complexiﬁed hyperbolic volume for this one-parameter family of metrics can
again be deﬁned in terms of the Chern-Simons functional ICS(A) appearing in (1.9).
Now, however,A =A(u) should be a ﬂat SL(2, C) connection with prescribed holon-
omy (2.4). The ”parametrized” volume conjecture then takes the form [10]
JN(K;q)
k,N→∞
∼ e− k
4πiICS (A(u)) . (2.5)
The quantity ICS(A(u)) can be described very explicitly. Indeed, suppose that
we require a hyperbolic metric (expressed in terms of a ﬂat SL(2, C) connection) to
have holonomies conjugate to diag( eu,e−u) and diag(ev,e−v), respectively, along the
meridian and longitude loops depicted in Figure 2a. Such a metric exists if and only if
the so-called A-polynomial of K vanishes [18],
A(𝓁,m ) = 0 for 𝓁 =ev, m =eu. (2.6)
Given a ﬁxed eu∈ C∗, exactly one of the solutions v =vhyp(u) of this equation corre-
sponds to the u-deformed hyperbolic metric. The Chern-Simons functional evaluated
at the ﬂat connectionA(u) can then be written as
ICS(A(u)) =ICS(A(iπ)) + 4
∫
γ
θ, (2.7)
6
Ka) b)
Figure 2: a) The “longitude” λ and “meridian”µ holonomy paths in the knot comple-
ment S3\K. b) Integration on the A-polynomial curve to ﬁnd the deformed complex
volume.
whereA(iπ) is the non-deformed hyperbolic ﬂat connection,
θ =−(v′ +iπ)du′ (2.8)
is a one-form on the curve A(ev′
,eu′
) = 0, and γ is a path on this curve that connects
the complete hyperbolic structure at (ev′
,eu′
) = (−1,±1) to the u-deformed metric at
(ev′
,eu′
) = (evhyp(u),eu), as in Figure 2b. 6
As our recurrent example, consider again the ﬁgure-eight knot. The complete col-
ored Jones polynomial, cf. [16], is
JN(41;q) = q
N
2−q−N
2
q
1
2−q− 1
2
N−1∑
j=0
qNj
j∏
k=1
(1−qk−N)(1−q−k−N). (2.10)
The A-polynomial of the ﬁgure-eight knot is
A(𝓁,m ) = (𝓁− 1)(m4𝓁2− (1−m2− 2m4−m6 +m8)𝓁 +m4𝓁2), (2.11)
and from (2.7) and (1.16), it results (after some algebra) that the Chern-Simons func-
tional can be written as
ICS(A(u)) = 2Li2(e−p−u)− 2Li2(ep−u) + 8(p−iπ)(u−iπ), (2.12)
wherex =ep is the solution to m3x2 + (1−m2−m4)x +m3 = 0 with smallest negative
imaginary part. For irrational u/iπ in a neighborhood of u =iπ it can then be shown
6The actual complexiﬁed volume that appears in the literature on hyperbolic geometry ( cf. [19,
20, 21]) is related to ICS(A(u)) as
Vol(S3\K;u) +iCS(S3\K;u) = i
2ICS(A(u)) + 2iv(u)Re(u)− 2πu + 2π2i. (2.9)
Note that ICS(A(u)) is analytic in u, whereas Vol(u) +iCS(u) is not.
7
(cf. [22, 23]) that the proposed asymptotics (2.5) indeed hold.
The necessity for taking u/iπ irrational here may appear a little strange at ﬁrst
glance. It stems fundamentally from the fact that the Jones polynomials JN(K;q =
e
2πi
k ) are really only deﬁned for N,k ∈ Z. A subtle analytic continuation in either N
or k is necessary to achieve u/iπ = N/k /∈ Q. As anticipated in [10] and explained
recently in [24], it is this continuation that causes the growth of the colored Jones
polynomial to be exponential. We will remark on this further in Section 3.3.2.
In light of this argument, one might ask now why the original volume conjecture
at the rational value k = N or u = iπ held in the ﬁrst place. Recall that JN(K;q)
actually vanished at k = N, so it was necessary to divide by JN(
 ;q) to obtain
the non-vanishing ratio VN(K;q). Examining VN(K;q) at u → 0 is equivalent to
considering the derivative ofJN(K;q) atu =iπ, which of course knows about analytic
continuation.7
