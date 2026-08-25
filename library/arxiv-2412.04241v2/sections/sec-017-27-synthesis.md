---
doc_id: arxiv-2412.04241v2
doc_title: "THE HABIRO RING OF A NUMBER FIELD"
section_id: sec-017-27-synthesis
section_title: "Synthesis"
section_number: 2.7
pages: 35-37
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
doc_brief: "THE HABIRO RING OF A NUMBER FIELD — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
the one hand and formal Gaussian integration on the other. It identifies the two collections
fA(t,q ) and f FGI
A (t,q ) and deduces a stronger property for their ring of coefficients. This
will allow us to specialise to t = 1 later and obtain elements of modules of the Habiro ring.
Firstly, we will prove Theorem 3 of Section 1.7 in the following refined form.
Theorem 8. For every symmetric matrix A with integer entries, positive integer m and
residue class k∈{ 0,...,m − 1}N, we have:
FA,m,k(t1/m,q ) = Ω FGI
A,m,k(t,q ), q = ζmm′ +x, (163)
for any positive integer m′, where these functions are defined by equations (32) and (126).
Proof. We will show that for every positive integer m′, we have
FA,m,k(t1/m,ζmm′ +x) = Ω FGI
A,m,k(t,ζmm′ +x) ∈ Q[ζmm′]( (x) )[ [t] ]. (164)
The proof of this equality uses crucially the fact that FA,m,k(t1/m,q ) is the unique solution
to a system of linear q-difference equations with initial condition F (0,q ) = 1. We discuss in
detail the case where A is a 1× 1 matrix, in which case the linear q-difference equation is
mX
ℓ=0
(−1)ℓq−ℓ(ℓ−1)/2
m
ℓ

q−1
σℓ
j

tkFA,m,k(t,q )

= (−1)Am(m+1)/2qAm(m+1)/2tmσAm

tkFA,m,k(t,q )

.
(165)
The first thing to note is that (165) has a unique solution in the set tkQ[ζmm′]( (x) )[ [tm] ].
Indeed, if tkF (t,q ) =P
j≥0aj(x)tk+mj is a solution to (165) with q = ζmm′ +x, then aj(x)
satisfies
mX
ℓ=0
(−1)ℓq−ℓ(ℓ−1)/2
m
ℓ

q−1
qkℓ+mjℓaj(x)− (−1)Am(m+1)/2qAm(m+1)/2+Am(j−1)aj−1(x)
= (qk+mj+1−m;q)maj(x)− (−1)Am(m+1)/2qAm(m+1)/2+Am(j−1)aj−1(x) = 0
(166)
for all j≥ 0, which together with the initial condition a0(x) = 1 uniquely determines aj(x).
36 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
In fact, the above calculation and the definition of FA,m,k(t,q ) prove that FA,m,k(t,q )
satisfies (165). Lemma 2.15 of Section 2.5 shows that ΩFGI
A,m,k(tm,q ) is also a solution to (165).
Moreover, the fact that det(Λ−1) =O(t) dominates thet−1 appearing from the denominators
of Li≤0(z) shows that Ω FGI
A,m,k(t,ζmm′ +x)∈ Q[ζmm′]( (x) )[ [t] ].
This concludes the proof of the first part of the theorem when A is a 1 × 1 symmetric
matrix. The proof in the general case is identical using equation (137), and is omitted. □
A consequence of Theorem 8 is that the power series defined in equations (65), (94), (66),
and (67) for the admissible series and those defined in equations (116), (120), and (121) for
the FGI series coincide:
δ = δFGI, V = V FGI, U m = U FGI
m . (167)
Proof of Lemma 2.6 of Section 2.3 and Lemma 2.9 of Section 2.4. These follow from Theo-
rem 8 and the explicit formula of Ω FGI
A,m,k(t,q ) given in equation (118). □
Corollary 2.18. If FA(t,q ) is the series (31) and V = VA(t) is the associated potential,
then V determines A and hence FA.
Proof. We have
tj∂tjV (t) = log zj(t), j = 1,...,N (168)
Hence V determines zj for j = 1,...,N , and consequently the Hessian
∂2
∂zi∂zj
V (t) = −A− diag
 z(t)
1−z(t)

. (169)
The result follows. □
Note that the proof of Theorem 8 uses the expansion of a solution of (165) into power
series in t whose coefficients are power series in x, unlike the WKB method, which uses an
expansion of a solution into power series in x whose coefficients are power series in t.
Proof of Theorem 4 of Section 1.7. Theorem 8 together with Lemmas 2.10 and 2.13 imply
the coefficients of x in equation (39) are in Z[t1/m,ζm][ [t] ]∩S(m)
p [ 1
p,z 1/m]. To complete the
proof we will show that
Z[t1/m,ζm][ [t] ]∩ S(m)
p [ 1
p,z 1/m] ⊆ S(m)
p [z1/m]. (170)
Elements in S(m)
p [ 1
p,z 1/m] can be represented by polynomials in t1/m of degree less than m
whose coefficients are polynomials in z±1/m, t±1 and δ−1. Firstly, we find that z(t)±1/m∈
1 +tZ[ 1
m][ [t] ] as the LHS of the equation
(−1)diag(A)z−A(1−z) = t, (171)
is integral and therefore inverting the series and solving for 1 −z in terms of t leads to an
integral power series in t. Secondly, as δ is a polynomial in z times a monomial in z±1 and
has δ(0) = 1 we see that δ±1∈ 1 +tZ[ [t] ]. Thirdly, in any expression with t we can replace
it with z using the functional equations (34). Therefore, for any element of S(m)[ 1
pm,z 1/m]
we can remove all t from the coefficients of t1/m and factor out all denominators given that
multiplying by z±1/m,δ−1 preserve integrality of the power series. Therefore, elements in
THE HABIRO RING OF A NUMBER FIELD 37
S(m)[ 1
pm,z 1/m] can be represented by a unit in Z[ 1
m,t 1/m,ζm][ [t] ] times a polynomial in (1−z).
Assuming that this element is in the intersection in equation (170), we see that this implies
that this polynomial is in Z[t1/m,ζm][ [1−z] ]. This implies that the polynomials in 1−z are
p-integral and therefore implies the inclusion of equation (170). □
