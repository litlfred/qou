---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-016-43-state-integrals
section_title: "State integrals"
section_number: 4.3
pages: 17-19
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
cally rigorous as a full TQFT, in contrast to Chern-Simons theory with a compact gauge
group [Wit89] and the Reshetikhin-Turaev construction [RT91]. Nevertheless, there exist
state-integral models, based on ideal triangulations, that provide a deﬁnition of complex
Chern-Simons partition functions for a certain class of 3-manifolds [Dim14, AK14a]. These
state-integral models generalize earlier work [Hik07, DGLZ09, Dim13, AK14b, AK13] that
computed Chern-Simons partition functions at level k = 1.
In the present paper, we use the asymptotic expansion of these state integrals in the limit
(t, ˜t)→ (2k, 0) to motivate the deﬁnition of the power series φγ,ζ(ℏ) given in Section 2.
Before we discuss the state-integral Zγ associated to a Neumann-Zagier datum γ of an
ideal triangulation, it is worth mentioning that convergence of the state-integral requires
certain positivity assumptions, which are satisﬁed when the ideal triangulation supports a
strict angle structure. This is discussed at length in [AK14a, Dim14]. In the rest of this
section, we will assume that the background ideal triangulation admits such a structure.
Although positivity is required for the convergence of the state-integral, the formula that we
will obtain for its asymptotic expansion makes sense without any positivity assumptions.
It was shown in [Dim13, DG13a] that a Neumann-Zagier datum γ = ( A, B,ν,z,f,f ′′)
with non-degenerate matrix B leads to a state-integral partition function for SL(2, C) Chern-
Simons at level k = 1, given by
Zγ = 1√
det B
(i)f B−1νe
1
k ( ℏ
8−π2
8ℏ )f B−1ν
∫ dNZ
(−2πiℏ)
N
2
e− 1
2k (1+ 2πi
ℏ )ZB−1ν+ 1
2kℏZB−1AZ
N∏
i=1
Zℏ[∆](Zi),
(42)
where the integral runs over some mid-dimensional contour in the space CN parametrized
by Z = (Z1,...,Z N), andZℏ[∆](Zi) is a quantum dilogarithm function associated to every
tetrahedron, given forℜ(ℏ)< 0 by
(43) Zℏ[∆](Zi) =
∞∏
r=0
1−e(r+1)ℏ−Zi
1−er 4π2
ℏ )− 2πi
ℏ Zi
= (eZi+ℏ,e ℏ)∞
(e
2πi
ℏ Zi,e
4π2
ℏ )∞
.
18 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
This function has an asymptotic expansion as ℏ→ 0,
Zℏ[∆](Zi)∼ (eZ+ℏ,e ℏ)∞∼ exp
∞∑
n=0
ℏn−1
n! Bn(1)Li2−n(e−Z) (44)
= 1
ℏLi2(e−Z) + 1
2Li1(e−Z) + ℏ
12Li0(e−Z) +... .
Using Li2(e−(Z∗+δZ)) = Li2(e−Z∗
) + log(1−e−Z∗
)δZ +..., it follows that at leading order in
ℏ, the integrand of (42) has critical points at
(45) AZ∗ + B log(1−e−Z∗
) =iπν,
which are a logarithmic version of the gluing equations. In particular, if γ is a positive
Neumann-Zagier datum, then the equations are satisﬁed byZ∗
i = log(zi) for alli = 1,...,N .
By performing formal Gaussian integration around this “geometric” critical point, order by
order in the formal parameter ℏ, we obtained in [DG13a] a diagrammatic formula for the
series φK,1(ℏ).
The actual contour of integration appropriate for (42) and its level- k generalization has
been carefully described in [AK14b, Dim14, AK14a]. We emphasize, however, that in order
to perform a formal perturbative expansion around a given critical point, a choice of contour
is irrelevant.
The level-k generalization of the state integral, as developed in [Dim14], reads
Z(k)
γ = 1
kN
√
det B
ζ
1
4f B−1νe
1
k ( ℏ
8−π2
8ℏ )f B−1ν
×
∑
m∈(Z/kZ)N
∫ dNZ
(−2πiℏ)
N
2
(−ζ
1
2 )mB−1Ame− 1
2k (1+ 2πi
ℏ )ZB−1ν+ 1
2kℏZB−1AZ
N∏
i=1
Z(k)
ℏ [∆](Zi,mi),(46)
where ζ =e
2πi
k as usual, and (−ζ
1
2 )C is understood as e(iπ
k−iπ)C for any C; and
(47) Z(k)
ℏ [∆](Zi,mi) =
(
ζmi+1e
ℏ
k−Zi
k ;ζe
ℏ
k
)
∞
(
ζ−mie− 2πi
kℏZi;ζ−1e
4π2
kℏ
)
∞
=
∏
0≤s,t<k
s−t≡mi (modk)
Zℏ[∆]
(Zi
k + ℏs
k + 2πit
k
)
.
Recall some well-known facts about the asymptotic expansion of the quantum dilogarithm
that can be found, for instance, in [Zag07, Sec. II.D].
Lemma 4.2. We have:
log (qx;q)∞ =−
∞∑
n=1
qnxn
n(1−qn)∼
∞∑
n=0
ℏn−1 (−1)nBn
n! Li2−n(x)
when q = eℏ and ℏ→ 0, where Bn is the n-th Bernoulli number and Li n(x) =∑∞
k=1xk/nk
is the n-th polylogarithm. Since x∂xLi2−n(x) = Li2−n−1(x), it follows that
log (eℏe−(u+w);eℏ)∞∼ exp
( ∞∑
n,k=0
ℏn−1 (−1)n+kBn
n!k! Li2−n−k(e−u)wk
)
QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY 19
The asymptotic expansion ofZ(k)
ℏ follows from its product representation,
Z(k)
ℏ [∆](Zi,mi)∼
k−1∏
s=0
(ζmi−se(1−s
k )ℏ− 1
kZi;eℏ)∞
∼ exp
∞∑
n=0
k∑
s=1
ℏn−1
n! Bn
(s
k
)
Li2−n(ζmi+se−Zi/k) (48)
= exp
[ 1
k ℏLi2(e−Zi)−
k∑
s=1
(1
2− s
k
)
Li1(ζmi+se−Zi/k) +...
]
(where we have substituted s byk−s in the second sum). Notably, the leading asymptotic
1
kLi2(e−Zi) is independent of mi. Indeed, this remains true for the entire integrand in (46).
The critical points Z∗ of the integrand at order ℏ−1 simply satisfy the standard gluing
equation (45). Let us assume that the Neumann-Zagier has all zi strictly in the upper half-
plane and focus on the geometric critical point Z∗ = log(z). The value of the integrand at
the critical point, at order ℏ−1, then becomes (after some manipulation)
(49) exp 1
k ℏ
[
− 1
2(Z∗−iπf )· ((Z∗)′′ +iπf′′) +
N∑
i=1
Li2(e−Z∗
i )
]
,
where (Z∗)′′ = log(1−e−Z∗
) = logz′′. The quantity (49) appears to agree with the complex
hyperbolic volume of a manifold M with Neumann-Zagier datum γ, modulo π2/6 [DG13a],
though knowing this is unnecessary for obtaining the series φγ,ζ. On the other hand, it is
crucial for our computation that the value at the leading-order saddle point is independent
of m — so all terms in the sum over m contribute equally to the higher-order asymptotics.
By using (48), or (better) the double series expansion around the critical point Z∗,
(50) Z(k)
ℏ [∆](Z∗
i +δZi,mi)∼ exp
∞∑
n=0
∞∑
j=0
ℏn−1(−δZi)j
kjn!j!
k∑
s=1
Bn
(s
k
)
Li2−n−j(ζmi+se−Z∗
i/k)
a saddle-point approximation or formal Gaussian integration of (46) leads immediately to
the deﬁnition ofφγ,ζ(ℏ) in Section 2. Indeed, in the ﬁnite-dimensional Feynman calculus, the
propagator Π is the inverse of the Hessian matrix, appearing at order ℏ−1 in the exponent of
(46) as 1
kδZ· (−B−1A + ∆(z∗)′)·δZ; while each vertex factor Γ (j)
i is the coeﬃcient of (δZi)j
in the exponent of (46).
