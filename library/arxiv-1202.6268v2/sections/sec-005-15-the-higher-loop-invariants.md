---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-005-15-the-higher-loop-invariants
section_title: "The higher-loop invariants"
section_number: 1.5
pages: 6-7
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
for n≥ 2. They are analyzed in detail in Section 5, using a state integral ( 5.2). The result,
however, may be summarized as follows. Let us introduce a formal p ower series
(1.9) ψℏ(x;z) = exp

 ∑
n, k, 2n+k−2>0
ℏn+ k
2 −1(−x)kBn
n!k! Li2−n−k(z−1)

∈ Q(z)[ [x, ℏ
1
2 ] ]
whereBn is thenth Bernoulli number (withB1 = +1/2), andLm(z) is themth polylogarithm.
Note that Li m(z)∈ (1−z)−m−1Z[z] is a rational function for all nonpositive integers m. This
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 7
formal series comes from the asymptotic expansion of the quantu m dilogarithm function after
removal of its two leading asymptotic terms [ Bar99, FK94, Fad95]. The quantum dilogarithm
is the Chern-Simons partition function of a single tetrahedron and it s asymptotics are studied
in detail in Section 5.
We ﬁx an enhanced Neumann-Zagier datum ˆβT = (z, A, B,f ) of an oriented 1-cusped
manifoldM and a regular ideal triangulation T withN tetrahedra. Let ν = Af + Bf ′′. We
assume that
det(B)⁄= 0, τ M⁄= 0.
The condition det( B)⁄= 0 is always satisﬁed with a suitable labeling of shapes; see Lemma
A.3. In that case, Lemma A.2 implies that
(1.10) H =−B−1A + ∆ z′,
is a symmetric matrix, where ∆ z′ = diag(z′
1,...,z ′
N ). We deﬁne
(1.11) fT , ℏ(x;z) = exp
(
− ℏ
1
2
2 xT B−1ν + ℏ
8f T B−1Af
) N∏
i=1
ψℏ(xi,z i)∈ Q(z)[ [x, ℏ
1
2 ] ],
where x = (x1,...,x N )T and z = (z1,...,z N ). Assuming that H is invertible, a formal power
series fℏ(x)∈ Q(z)[ [x, ℏ
1
2 ] ] has a formal Gaussian integration , given by ( cf. [BIZ80])
(1.12) ⟨fℏ(x)⟩ =
∫
dxe − 1
2 xT H xfℏ(x)∫
dxe − 1
2 xT H x .
This integration is deﬁned by expanding fℏ(x) as a series in x, and then formally integrating
each monomial, using the quadratic form H−1 to contract x-indices pairwise.
Deﬁnition 1.9. With the above conventions, we deﬁne
(1.13) exp
( ∞∑
n=2
ST ,n (z)ℏn−1
)
:=⟨fT , ℏ(x;z)⟩.
Remark 1.10. Notice that the result involves only integral powers of ℏ and each term is
a rational function in the complex numbers z. Moreover, ST ,n ∈ τ −3n+3
T Q[z,z ′,z ′′] for all
