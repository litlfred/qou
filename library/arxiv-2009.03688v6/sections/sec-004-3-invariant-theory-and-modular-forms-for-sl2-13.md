---
doc_id: arxiv-2009.03688v6
doc_title: "E 8 -singularity, invariant theory and modular forms"
section_id: sec-004-3-invariant-theory-and-modular-forms-for-sl2-13
section_title: "Invariant theory and modular forms for SL(2, 13)"
section_number: 3
pages: 16-39
source_pdf: 2009.03688v6.pdf
source_sha256: 8eb9b4cbe2690730
toc_source: inferred
doc_brief: "E 8 -singularity, invariant theory and modular forms — As an algebraic surface, the equation of E8-singularity x5 + y3 + z2 = 0 can be obtained from a quotient CY /SL(2, 13) over the modular curve"
---
The representation of SL(2, 13) which we will consider is the unique six-
dimensional irreducible complex representation for which the eigenvalues of
1
1
0
1

are the exp(a.2πi/13) for a a non-square mod 13. We will give an
explicit realization of this representation. This explicit realization will play a
major role for giving a complete system of invariants associated to SL(2, 13).
At ﬁrst, we will study the six-dimensional representation of the ﬁnite group
SL(2, 13) of order 2184, which acts on the ﬁve-dimensional projective space
P5 = {(z1, z2, z3, z4, z5, z6) : zi ∈C
(i = 1, 2, 3, 4, 5, 6)}. This representation
is deﬁned over the cyclotomic ﬁeld Q(e
2πi
13 ). Put
S = −1
√
13








ζ12 −ζ
ζ10 −ζ3
ζ4 −ζ9
ζ5 −ζ8
ζ2 −ζ11
ζ6 −ζ7
ζ10 −ζ3
ζ4 −ζ9
ζ12 −ζ
ζ2 −ζ11
ζ6 −ζ7
ζ5 −ζ8
ζ4 −ζ9
ζ12 −ζ
ζ10 −ζ3
ζ6 −ζ7
ζ5 −ζ8
ζ2 −ζ11
ζ5 −ζ8
ζ2 −ζ11
ζ6 −ζ7
ζ −ζ12
ζ3 −ζ10
ζ9 −ζ4
ζ2 −ζ11
ζ6 −ζ7
ζ5 −ζ8
ζ3 −ζ10
ζ9 −ζ4
ζ −ζ12
ζ6 −ζ7
ζ5 −ζ8
ζ2 −ζ11
ζ9 −ζ4
ζ −ζ12
ζ3 −ζ10








(3.1)
16
and
T = diag(ζ7, ζ11, ζ8, ζ6, ζ2, ζ5),
(3.2)
where ζ = exp(2πi/13). We have
S2 = −I,
T 13 = (ST)3 = I.
(3.3)
In [30], we put P = ST −1S and Q = ST 3. Then (Q3P 4)3 = −I (see [30], the
proof of Theorem 3.1). Let G = ⟨S, T⟩, then G ∼= SL(2, 13).
Put θ1 = ζ + ζ3 + ζ9, θ2 = ζ2 + ζ6 + ζ5, θ3 = ζ4 + ζ12 + ζ10, and
θ4 = ζ8 + ζ11 + ζ7. We ﬁnd that









θ1 + θ2 + θ3 + θ4 = −1,
θ1θ2 + θ1θ3 + θ1θ4 + θ2θ3 + θ2θ4 + θ3θ4 = 2,
θ1θ2θ3 + θ1θ2θ4 + θ1θ3θ4 + θ2θ3θ4 = 4,
θ1θ2θ3θ4 = 3.
Hence, θ1, θ2, θ3 and θ4 satisfy the quartic equation z4+z3 +2z2−4z+3 = 0,
which can be decomposed as two quadratic equations
 
z2 + 1 +
√
13
2
z + 5 +
√
13
2
! 
z2 + 1 −
√
13
2
z + 5 −
√
13
2
!
= 0
over the real quadratic ﬁeld Q(
√
13). Therefore, the four roots are given as
follows:



























θ1 = 1
4

−1 +
√
13 +
q
−26 + 6
√
13

,
θ2 = 1
4

−1 −
√
13 +
q
−26 −6
√
13

,
θ3 = 1
4

−1 +
√
13 −
q
−26 + 6
√
13

,
θ4 = 1
4

−1 −
√
13 −
q
−26 −6
√
13

.
Moreover, we ﬁnd that















θ1 + θ3 + θ2 + θ4 = −1,
θ1 + θ3 −θ2 −θ4 =
√
13,
θ1 −θ3 −θ2 + θ4 = −
q
−13 + 2
√
13,
θ1 −θ3 + θ2 −θ4 =
q
−13 −2
√
13.
17
Let us study the action of ST ν on P5, where ν = 0, 1, . . . , 12. Put
α = ζ + ζ12 −ζ5 −ζ8,
β = ζ3 + ζ10 −ζ2 −ζ11,
γ = ζ9 + ζ4 −ζ6 −ζ7.
We ﬁnd that
13ST ν(z1) · ST ν(z4)
=βz1z4 + γz2z5 + αz3z6+
+ γζνz2
1 + αζ9νz2
2 + βζ3νz2
3 −γζ12νz2
4 −αζ4νz2
5 −βζ10νz2
6+
+ (α −β)ζ5νz1z2 + (β −γ)ζ6νz2z3 + (γ −α)ζ2νz1z3+
+ (β −α)ζ8νz4z5 + (γ −β)ζ7νz5z6 + (α −γ)ζ11νz4z6+
−(α + β)ζνz3z4 −(β + γ)ζ9νz1z5 −(γ + α)ζ3νz2z6+
−(α + β)ζ12νz1z6 −(β + γ)ζ4νz2z4 −(γ + α)ζ10νz3z5.
13ST ν(z2) · ST ν(z5)
=γz1z4 + αz2z5 + βz3z6+
+ αζνz2
1 + βζ9νz2
2 + γζ3νz2
3 −αζ12νz2
4 −βζ4νz2
5 −γζ10νz2
6+
+ (β −γ)ζ5νz1z2 + (γ −α)ζ6νz2z3 + (α −β)ζ2νz1z3+
+ (γ −β)ζ8νz4z5 + (α −γ)ζ7νz5z6 + (β −α)ζ11νz4z6+
−(β + γ)ζνz3z4 −(γ + α)ζ9νz1z5 −(α + β)ζ3νz2z6+
−(β + γ)ζ12νz1z6 −(γ + α)ζ4νz2z4 −(α + β)ζ10νz3z5.
13ST ν(z3) · ST ν(z6)
=αz1z4 + βz2z5 + γz3z6+
+ βζνz2
1 + γζ9νz2
2 + αζ3νz2
3 −βζ12νz2
4 −γζ4νz2
5 −αζ10νz2
6+
+ (γ −α)ζ5νz1z2 + (α −β)ζ6νz2z3 + (β −γ)ζ2νz1z3+
+ (α −γ)ζ8νz4z5 + (β −α)ζ7νz5z6 + (γ −β)ζ11νz4z6+
−(γ + α)ζνz3z4 −(α + β)ζ9νz1z5 −(β + γ)ζ3νz2z6+
−(γ + α)ζ12νz1z6 −(α + β)ζ4νz2z4 −(β + γ)ζ10νz3z5.
Note that α + β + γ =
√
13, we ﬁnd that
√
13 [ST ν(z1) · ST ν(z4) + ST ν(z2) · ST ν(z5) + ST ν(z3) · ST ν(z6)]
=(z1z4 + z2z5 + z3z6) + (ζνz2
1 + ζ9νz2
2 + ζ3νz2
3) −(ζ12νz2
4 + ζ4νz2
5 + ζ10νz2
6)+
−2(ζνz3z4 + ζ9νz1z5 + ζ3νz2z6) −2(ζ12νz1z6 + ζ4νz2z4 + ζ10νz3z5).
18
Let
ϕ∞(z1, z2, z3, z4, z5, z6) =
√
13(z1z4 + z2z5 + z3z6)
(3.4)
and
ϕν(z1, z2, z3, z4, z5, z6) = ϕ∞(ST ν(z1, z2, z3, z4, z5, z6))
(3.5)
for ν = 0, 1, . . . , 12. Then
ϕν =(z1z4 + z2z5 + z3z6) + ζν(z2
1 −2z3z4) + ζ4ν(−z2
5 −2z2z4)+
+ ζ9ν(z2
2 −2z1z5) + ζ3ν(z2
3 −2z2z6) + ζ12ν(−z2
4 −2z1z6)+
+ ζ10ν(−z2
6 −2z3z5).
(3.6)
This leads us to deﬁne the following senary quadratic forms (quadratic forms
in six variables):























A0 = z1z4 + z2z5 + z3z6,
A1 = z2
1 −2z3z4,
A2 = −z2
5 −2z2z4,
A3 = z2
2 −2z1z5,
A4 = z2
3 −2z2z6,
A5 = −z2
4 −2z1z6,
A6 = −z2
6 −2z3z5.
(3.7)
Hence,
√
13ST ν(A0) = A0+ζνA1+ζ4νA2+ζ9νA3+ζ3νA4+ζ12νA5+ζ10νA6. (3.8)
Let H := Q5P 2 · P 2Q6P 8 · Q5P 2 · P 3Q where P = ST −1S and Q = ST 3.
Then (see [31], p.27)
H =








0
0
0
0
0
1
0
0
0
1
0
0
0
0
0
0
1
0
0
0
−1
0
0
0
−1
0
0
0
0
0
0
−1
0
0
0
0








.
(3.9)
Note that H6 = 1 and H−1TH = −T 4. Thus, ⟨H, T⟩∼= Z13 ⋊Z6. Hence, it
is a maximal subgroup of order 78 of PSL(2, 13) with index 14. We ﬁnd that
ϕ2
∞is invariant under the action of the maximal subgroup ⟨H, T⟩. Note that
ϕ∞=
√
13A0,
ϕν = A0 +ζνA1 +ζ4νA2 +ζ9νA3 +ζ3νA4 +ζ12νA5 +ζ10νA6
19
for ν = 0, 1, . . . , 12. Let w = ϕ2, w∞= ϕ2
∞and wν = ϕ2
ν. Then w∞, wν for
ν = 0, . . . , 12 form an algebraic equation of degree fourteen, which is just the
Jacobian equation of degree fourteen (see [18], pp.161-162), whose roots are
these wν and w∞:
w14 + a1w13 + · · · + a13w + a14 = 0.
On the other hand, we have
−13
√
13ST ν(z1) · ST ν(z2) · ST ν(z3)
= −r4(ζ8νz3
1 + ζ7νz3
2 + ζ11νz3
3) −r2(ζ5νz3
4 + ζ6νz3
5 + ζ2νz3
6)
−r3(ζ12νz2
1z2 + ζ4νz2
2z3 + ζ10νz2
3z1) −r1(ζνz2
4z5 + ζ9νz2
5z6 + ζ3νz2
6z4)
+ 2r1(ζ3νz1z2
2 + ζνz2z2
3 + ζ9νz3z2
1) −2r3(ζ10νz4z2
5 + ζ12νz5z2
6 + ζ4νz6z2
4)
+ 2r4(ζ7νz2
1z4 + ζ11νz2
2z5 + ζ8νz2
3z6) −2r2(ζ6νz1z2
4 + ζ2νz2z2
5 + ζ5νz3z2
6)+
+ r1(ζ3νz2
1z5 + ζνz2
2z6 + ζ9νz2
3z4) + r3(ζ10νz2z2
4 + ζ12νz3z2
5 + ζ4νz1z2
6)+
+ r2(ζ6νz2
1z6 + ζ2νz2
2z4 + ζ5νz2
3z5) + r4(ζ7νz3z2
4 + ζ11νz1z2
5 + ζ8νz2z2
6)+
+ r0z1z2z3 + r∞z4z5z6+
−r4(ζ11νz1z2z4 + ζ8νz2z3z5 + ζ7νz1z3z6)+
+ r2(ζ2νz1z4z5 + ζ5νz2z5z6 + ζ6νz3z4z6)+
−3r4(ζ7νz1z2z5 + ζ11νz2z3z6 + ζ8νz1z3z4)+
+ 3r2(ζ6νz2z4z5 + ζ2νz3z5z6 + ζ5νz1z4z6)+
−r3(ζ10νz1z2z6 + ζ4νz1z3z5 + ζ12νz2z3z4)+
+ r1(ζ3νz3z4z5 + ζ9νz2z4z6 + ζνz1z5z6),
where
r0 = 2(θ1 −θ3) −3(θ2 −θ4),
r∞= 2(θ4 −θ2) −3(θ1 −θ3),
r1 =
q
−13 −2
√
13,
r2 =
s
−13 + 3
√
13
2
,
r3 =
q
−13 + 2
√
13,
r4 =
s
−13 −3
√
13
2
.
This leads us to deﬁne the following senary cubic forms (cubic forms in six
20
variables):

























































D0 = z1z2z3,
D1 = 2z2z2
3 + z2
2z6 −z2
4z5 + z1z5z6,
D2 = −z3
6 + z2
2z4 −2z2z2
5 + z1z4z5 + 3z3z5z6,
D3 = 2z1z2
2 + z2
1z5 −z4z2
6 + z3z4z5,
D4 = −z2
2z3 + z1z2
6 −2z2
4z6 −z1z3z5,
D5 = −z3
4 + z2
3z5 −2z3z2
6 + z2z5z6 + 3z1z4z6,
D6 = −z3
5 + z2
1z6 −2z1z2
4 + z3z4z6 + 3z2z4z5,
D7 = −z3
2 + z3z2
4 −z1z3z6 −3z1z2z5 + 2z2
1z4,
D8 = −z3
1 + z2z2
6 −z2z3z5 −3z1z3z4 + 2z2
3z6,
D9 = 2z2
1z3 + z2
3z4 −z2
5z6 + z2z4z6,
D10 = −z1z2
3 + z2z2
4 −2z4z2
5 −z1z2z6,
D11 = −z3
3 + z1z2
5 −z1z2z4 −3z2z3z6 + 2z2
2z5,
D12 = −z2
1z2 + z3z2
5 −2z5z2
6 −z2z3z4,
D∞= z4z5z6.
(3.10)
Then
−13
√
13ST ν(D0)
=r0D0 + r1ζνD1 + r2ζ2νD2 + r1ζ3νD3 + r3ζ4νD4+
+ r2ζ5νD5 + r2ζ6νD6 + r4ζ7νD7 + r4ζ8νD8+
+ r1ζ9νD9 + r3ζ10νD10 + r4ζ11νD11 + r3ζ12νD12 + r∞D∞.
−13
√
13ST ν(D∞)
=r∞D0 −r3ζνD1 −r4ζ2νD2 −r3ζ3νD3 + r1ζ4νD4+
−r4ζ5νD5 −r4ζ6νD6 + r2ζ7νD7 + r2ζ8νD8+
−r3ζ9νD9 + r1ζ10νD10 + r2ζ11νD11 + r1ζ12νD12 −r0D∞.
Let
δ∞(z1, z2, z3, z4, z5, z6) = 132(z2
1z2
2z2
3 + z2
4z2
5z2
6)
(3.11)
and
δν(z1, z2, z3, z4, z5, z6) = δ∞(ST ν(z1, z2, z3, z4, z5, z6))
(3.12)
for ν = 0, 1, . . . , 12. Then
δν = 132ST ν(G0) = −13G0 + ζνG1 + ζ2νG2 + · · · + ζ12νG12,
(3.13)
21
where the senary sextic forms (i.e., sextic forms in six variables) are given as
follows:















































































































G0 =D2
0 + D2
∞,
G1 = −D2
7 + 2D0D1 + 10D∞D1 + 2D2D12+
−2D3D11 −4D4D10 −2D9D5,
G2 = −2D2
1 −4D0D2 + 6D∞D2 −2D4D11+
+ 2D5D10 −2D6D9 −2D7D8,
G3 = −D2
8 + 2D0D3 + 10D∞D3 + 2D6D10+
−2D9D7 −4D12D4 −2D1D2,
G4 = −D2
2 + 10D0D4 −2D∞D4 + 2D5D12+
−2D9D8 −4D1D3 −2D10D7,
G5 = −2D2
9 −4D0D5 + 6D∞D5 −2D10D8+
+ 2D6D12 −2D2D3 −2D11D7,
G6 = −2D2
3 −4D0D6 + 6D∞D6 −2D127+
+ 2D2D4 −2D5D1 −2D8D11,
G7 = −2D2
10 + 6D0D7 + 4D∞D7 −2D1D6+
−2D2D5 −2D8D12 −2D9D11,
G8 = −2D2
4 + 6D0D8 + 4D∞D8 −2D3D5+
−2D6D2 −2D11D10 −2D1D7,
G9 = −D2
11 + 2D0D9 + 10D∞D9 + 2D5D4+
−2D1D8 −4D10D12 −2D3D6,
G10 = −D2
5 + 10D0D10 −2D∞D10 + 2D6D4+
−2D3D7 −4D9D1 −2D12D11,
G11 = −2D2
12 + 6D0D11 + 4D∞D11 −2D9D2+
−2D5D6 −2D7D4 −2D3D8,
G12 = −D2
6 + 10D0D12 −2D∞D12 + 2D2D10+
−2D1D11 −4D3D9 −2D4D8.
(3.14)
We have that G0 is invariant under the action of ⟨H, T⟩, a maximal subgroup
of order 78 of PSL(2, 13) with index 14. Note that δ∞, δν for ν = 0, . . . , 12
form an algebraic equation of degree fourteen. However, we have
Φ6 = Φ0,1 = δ∞+
12
X
ν=0
δν = 0.
22
Hence, it is not the Jacobian equation of degree fourteen.
Recall that the theta functions with characteristic
ǫ
ǫ′

∈R2 is deﬁned
by the following series which converges uniformly and absolutely on compact
subsets of C × H (see [10], p. 73):
θ

ǫ
ǫ′

(z, τ) =
X
n∈Z
exp

2πi
1
2

n + ǫ
2
2
τ +

n + ǫ
2
 
z + ǫ′
2

.
The modiﬁed theta constants (see [10], p. 215) ϕl(τ) := θ[χl](0, kτ), where
the characteristic χl =
2l+1
k
1

, l = 0, . . . , k−3
2 , for odd k and χl =
 2l
k
0

,
l = 0, . . . , k
2, for even k. We have the following:
Proposition 3.1. (see [10], p. 236). For each odd integer k ≥5, the
map Φ : τ 7→(ϕ0(τ), ϕ1(τ), . . . , ϕ k−5
2 (τ), ϕ k−3
2 (τ)) from H∪Q∪{∞} to C
k−1
2 ,
deﬁnes a holomorphic mapping from H/Γ(k) into CP
k−3
2 .
In our case, the map Φ : τ 7→(ϕ0(τ), ϕ1(τ), ϕ2(τ), ϕ3(τ), ϕ4(τ), ϕ5(τ))
gives a holomorphic mapping from the modular curve X(13) = H/Γ(13) into
CP5, which corresponds to our six-dimensional representation, i.e., up to the
constants, z1, . . . , z6 are just modular forms ϕ0(τ), . . . , ϕ5(τ). Let



















































a1(z) := e−11πi
26 θ
11
13
1

(0, 13z) = q
121
104 X
n∈Z
(−1)nq
1
2(13n2+11n),
a2(z) := e−7πi
26 θ
 7
13
1

(0, 13z) = q
49
104
X
n∈Z
(−1)nq
1
2(13n2+7n),
a3(z) := e−5πi
26 θ
 5
13
1

(0, 13z) = q
25
104
X
n∈Z
(−1)nq
1
2(13n2+5n),
a4(z) := −e−3πi
26 θ
 3
13
1

(0, 13z) = −q
9
104
X
n∈Z
(−1)nq
1
2(13n2+3n),
a5(z) := e−9πi
26 θ
 9
13
1

(0, 13z) = q
81
104 X
n∈Z
(−1)nq
1
2(13n2+9n),
a6(z) := e−πi
26θ
 1
13
1

(0, 13z) = q
1
104 X
n∈Z
(−1)nq
1
2 (13n2+n)
(3.15)
be the theta constants of order 13 and
A(z) := (a1(z), a2(z), a3(z), a4(z), a5(z), a6(z))T .
23
The signiﬁcance of our six dimensional representation of SL(2, 13) comes from
the following:
Proposition 3.2 (see [31], Proposition 2.5). If z ∈H, then the following
relations hold:
A(z + 1) = e−3πi
4 TA(z),
A

−1
z

= e
πi
4 √zSA(z),
(3.16)
where S and T are given in (3.1) and (3.2), and 0 < arg√z ≤π/2.
Note that it is (3.16) that gives an explicit realization of the isomorphism
between the unique sub-representation of parabolic modular forms of weight
1
2 on X(13) and the six-dimensional complex representation of SL(2, 13) gen-
erated by S and T.
Recall that the principal congruence subgroup of level 13 is the normal
subgroup Γ(13) of Γ = SL(2, Z) deﬁned by the exact sequence 1 →Γ(13) →
Γ(1)
f→SL(2, 13) →1 where f(γ) ≡γ (mod 13) for γ ∈Γ = Γ(1). There
is a representation ρ : Γ →GL(6, C) with kernel Γ(13) deﬁned as follows:
if t =
1
1
0
1

and s =
0
−1
1
0

, then ρ(t) = T and ρ(s) = S. To see
that such a representation exists, note that PSL(2, Z) := Γ/{±I} is deﬁned
by the presentation ⟨s, t; s2 = (st)3 = 1⟩satisﬁed by s and t and we have
proved that S and T satisfy these relations (in the projective coordinates).
Moreover, we have proved that PSL(2, 13) is deﬁned by the presentation
⟨S, T; S2 = T 13 = (ST)3 = 1⟩. Let p = st−1s and q = st3. Then
h := q5p2 · p2q6p8 · q5p2 · p3q =
 4, 428, 249
−10, 547, 030
−11, 594, 791
27, 616, 019

satisﬁes that ρ(h) = H. The oﬀ-diagonal elements of the matrix h, which
corresponds to H, are congruent to 0 mod 13. The connection to Γ0(13)
should be obvious.
Put xi(z) = η(z)ai(z), yi(z) = η3(z)ai(z) and ui(z) = η9(z)ai(z) (1 ≤i ≤
6). Let





X(z) = (x1(z), . . . , x6(z))T,
Y (z) = (y1(z), . . . , y6(z))T .
U(z) = (u1(z), . . . , u6(z))T .
24
Then





X(z) = η(z)A(z)
Y (z) = η3(z)A(z),
U(z) = η9(z)A(z).
Recall that η(z) satisﬁes the following transformation formulas η(z + 1) =
e
πi
12η(z) and η
 −1
z

= e−πi
4 √zη(z). By Proposition 3.2, we have
X(z + 1) = e−2πi
3 ρ(t)X(z),
X

−1
z

= zρ(s)X(z),
Y (z + 1) = e−πi
2 ρ(t)Y (z),
Y

−1
z

= e−πi
2 z2ρ(s)Y (z).
U(z + 1) = ρ(t)U(z),
U

−1
z

= z5ρ(s)U(z).
Deﬁne j(γ, z) := cz + d if z ∈H and γ =
a
b
c
d

∈Γ(1). Hence,





X(γ(z)) = u(γ)j(γ, z)ρ(γ)X(z),
Y (γ(z)) = v(γ)j(γ, z)2ρ(γ)Y (z),
U(γ(z)) = j(γ, z)5ρ(γ)U(z)
(3.17)
for γ ∈Γ(1), where u(γ) = 1, ω or ω2 with ω = e
2πi
3
and v(γ) = ±1 or
±i. Since Γ(13) = ker ρ, we have X(γ(z)) = u(γ)j(γ, z)X(z), Y (γ(z)) =
v(γ)j(γ, z)2Y (z) and U(γ(z)) = j(γ, z)5U(z) for γ ∈Γ(13). This means that
the functions x1(z), . . ., x6(z) are modular forms of weight one for Γ(13) with
the same multiplier u(γ) = 1, ω or ω2 and y1(z), . . ., y6(z) are modular forms
of weight two for Γ(13) with the same multiplier v(γ) = ±1 or ±i.
From now on, we will use the following abbreviation
Aj = Aj(a1(z), . . . , a6(z))
(0 ≤j ≤6),
Dj = Dj(a1(z), . . . , a6(z))
(j = 0, 1, . . . , 12, ∞)
and
Gj = Gj(a1(z), . . . , a6(z))
(0 ≤j ≤12).
25
We have

VS YS wea wma WH WH

q)):

ye YHaewow wa wHa wH WH

35
04
43

59

qt

D

D;

Ds

Dy
Dio
Du =q
Di

qd Tor
67
quot

17+ O(q)).

Ye Here wa wH WH

q=

Gi =

~~
= -— > —~ a
a
~~ Sr am oO

=I

(1+ O(q)),

-14+0(q¢

co)
+
N
a
ae oe 8E oE AE aE se
oa oa oa oa oa oa oa
How od ow wb odd
og Ne

AGA AAAA

and

Hence,

(1+ O(q)),

(13 + O(q)),

Fe eS
his Sho Shs i

(—22 + O(q)),
(—21 + O(q)),
(-1+0(q)),
(2+ O(q),
(2+ O(q),

eof
a

e

=e

TT TFT TFT Fo SF FS

°o

o

4

o

nN

o

iar)

o

x

o

ite}

oO

o

26
Note that
wν = (A0 + ζνA1 + ζ4νA2 + ζ9νA3 + ζ3νA4 + ζ12νA5 + ζ10νA6)2
= A2
0 + 2(A1A5 + A2A3 + A4A6)+
+ 2ζν(A0A1 + A2A6) + 2ζ3ν(A0A4 + A2A5)+
+ 2ζ9ν(A0A3 + A5A6) + 2ζ12ν(A0A5 + A3A4)+
+ 2ζ10ν(A0A6 + A1A3) + 2ζ4ν(A0A2 + A1A4)+
+ ζ2ν(A2
1 + 2A4A5) + ζ5ν(A2
3 + 2A1A2)+
+ ζ6ν(A2
4 + 2A3A6) + ζ11ν(A2
5 + 2A1A6)+
+ ζ8ν(A2
2 + 2A3A5) + ζ7ν(A2
6 + 2A4A2),
where
A2
0 + 2(A1A5 + A2A3 + A4A6) = q
1
2(−1 + O(q)),























A0A1 + A2A6 = q
41
26(−3 + O(q)),
A0A4 + A2A5 = q
19
26(−3 + O(q)),
A0A3 + A5A6 = q
5
26(1 + O(q)),
A0A5 + A3A4 = q
11
26(−1 + O(q)),
A0A6 + A1A3 = q
7
26(−1 + O(q)),
A0A2 + A1A4 = q
47
26(−1 + O(q)),
and























A2
1 + 2A4A5 = q
17
26(6 + O(q)),
A2
3 + 2A1A2 = q
23
26(8 + O(q)),
A2
4 + 2A3A6 = q
25
26(−1 + O(q)),
A2
5 + 2A1A6 = q
9
26(−3 + O(q)),
A2
2 + 2A3A5 = q
29
26(2 + O(q)),
A2
6 + 2A4A2 = q
1
26(1 + O(q)).
In the introduction, the invariant homogeneous polynomials Φm,n are de-
ﬁned. Now we give the normalization for the following four families of poly-
nomials of degrees d = 12, 16, 20 and 30. For d = 12, there are two such
27
invariant homogeneous polynomials Φ3,0 and Φ0,2:











Φ3,0 := −
1
13 · 30
 12
X
ν=0
w3
ν + w3
∞
!
,
Φ0,2 := −
1
13 · 52
 12
X
ν=0
δ2
ν + δ2
∞
!
,
(3.18)
For d = 16, there are two such invariant homogeneous polynomials Φ4,0
and Φ1,2 which need not to be normalized. For d = 20, there are two such
invariant homogeneous polynomials Φ5,0 and Φ2,2:











Φ5,0 :=
1
13 · 25
 12
X
ν=0
w5
ν + w5
∞
!
,
Φ2,2 :=
1
13 · 26
 12
X
ν=0
w2
νδ2
ν + w2
∞δ2
∞
!
(3.19)
For d = 30, there are three such invariant homogeneous polynomials Φ0,5,
Φ3,3 and Φ6,1:























Φ0,5 := −
1
13 · 1315
 12
X
ν=0
δ5
ν + δ5
∞
!
,
Φ3,3 := −
1
13 · 27
 12
X
ν=0
w3
νδ3
ν + w3
∞δ3
∞
!
,
Φ6,1 := −
1
13 · 285
 12
X
ν=0
w6
νδν + w6
∞δ∞
!
,
(3.20)
Theorem 3.3. The G-invariant homogeneous polynomials Φm,n of de-
grees d = 4, 8, 10, 12, 14, 16, 20 and 30 in x1(z), . . ., x6(z) can be identiﬁed
28
with modular forms as follows:





















































Φ4(x1(z), . . . , x6(z)) = 0,
Φ8(x1(z), . . . , x6(z)) = 0,
Φ10(x1(z), . . . , x6(z)) = 0,
Φ3,0(x1(z), . . . , x6(z)) = ∆(z),
Φ0,2(x1(z), . . . , x6(z)) = ∆(z),
Φ14(x1(z), . . . , x6(z)) = 0,
Φ4,0(x1(z), . . . , x6(z)) = 0,
Φ1,2(x1(z), . . . , x6(z)) = 0,
Φ5,0(x1(z), . . . , x6(z)) = η(z)8∆(z)E4(z),
Φ2,2(x1(z), . . . , x6(z)) = η(z)8∆(z)E4(z),
Φ0,5(x1(z), . . . , x6(z)) = ∆(z)2E6(z),
Φ3,3(x1(z), . . . , x6(z)) = ∆(z)2E6(z),
Φ6,1(x1(z), . . . , x6(z)) = ∆(z)2E6(z).
(3.21)
Proof. We divide the proof into four parts (see also [32]). The ﬁrst part
is the calculation of Φ5,0 and Φ3,0. Up to a constant, Φ5,0 = w5
0 + w5
1 +
· · · + w5
12 + w5
∞. As a polynomial in six variables, Φ5,0(z1, z2, z3, z4, z5, z6) is
a G-invariant polynomial. Moreover, for γ ∈Γ(1),
Φ5,0(Y (γ(z))T ) = Φ5,0(v(γ)j(γ, z)2(ρ(γ)Y (z))T )
=v(γ)20j(γ, z)40Φ5,0((ρ(γ)Y (z))T) = j(γ, z)40Φ5,0((ρ(γ)Y (z))T).
Note that ρ(γ) ∈⟨ρ(s), ρ(t)⟩= G and Φ5,0 is a G-invariant polynomial, we
have
Φ5,0(Y (γ(z))T ) = j(γ, z)40Φ5,0(Y (z)T ),
for γ ∈Γ(1).
This implies that Φ5,0(y1(z), . . . , y6(z)) is a modular form of weight 40 for
the full modular group Γ(1). Moreover, we will show that it is a cusp form.
29
In fact,
Φ5,0(a1(z), . . . , a6(z)) = 135q
5
2(1 + O(q))5+
+
12
X
ν=0
[q
1
2(−1 + O(q))+
+ 2ζνq
41
26(−3 + O(q)) + 2ζ3νq
19
26(−3 + O(q)) + 2ζ9νq
5
26(1 + O(q))+
+ 2ζ12νq
11
26(−1 + O(q)) + 2ζ10νq
7
26(−1 + O(q)) + 2ζ4νq
47
26(−1 + O(q))+
+ ζ2νq
17
26(6 + O(q)) + ζ5νq
23
26(8 + O(q)) + ζ6νq
25
26(−1 + O(q))+
+ ζ11νq
9
26(−3 + O(q)) + ζ8νq
29
26(2 + O(q)) + ζ7νq
1
26(1 + O(q))]5.
We will calculate the q
1
2-term which is the lowest degree. For the partition
13 = 4 · 1 + 9, the corresponding term is

5
4, 1

(ζ7νq
1
26)4 · (−3)ζ11νq
9
26 = −15q
1
2.
For the partition 13 = 3 · 1 + 2 · 5, the corresponding term is

5
3, 2

(ζ7νq
1
26)3 · (2ζ9νq
5
26)2 = 40q
1
2.
Hence, for Φ5,0(y1(z), . . . , y6(z)) which is a modular form for Γ(1) with weight
40, the lowest degree term is given by
(−15 + 40)q
1
2 · q
3
24 ·20 = 25q3.
Thus,
Φ5,0(y1(z), . . . , y6(z)) = q3(13 · 25 + O(q)).
The leading term of Φ5,0(y1(z), . . . , y6(z)) together with its weight 40 suﬃce
to identify this modular form with Φ5,0(y1(z), . . . , y6(z)) = 13·25∆(z)3E4(z).
Consequently,
Φ5,0(x1(z), . . . , x6(z)) = 13 · 25∆(z)3E4(z)/η(z)40 = 13 · 25η(z)8∆(z)E4(z).
Up to a constant, Φ3,0 = w3
0 + w3
1 + · · · + w3
12 + w3
∞, The calculation of
Φ3,0 is similar as that of Φ5,0. We ﬁnd that
Φ3,0(x1(z), . . . , x6(z)) = −13 · 30∆(z).
30
The second part is the calculation of Φ4, Φ8 and Φ4,0. The calculation of
Φ4 has been done in [31], Theorem 3.1. We will give the calculation of Φ4,0.
Up to a constant, Φ4,0 = w4
0 + w4
1 + · · · + w4
12 + w4
∞. Similar as the above
calculation for Φ5,0, we ﬁnd that Φ4,0(y1(z), . . . , y6(z)) is a modular form of
weight 32 for the full modular group Γ(1). Moreover, we will show that it is
a cusp form. In fact,
Φ4,0(a1(z), . . . , a6(z)) = 134q2(1 + O(q))4+
+
12
X
ν=0
[q
1
2(−1 + O(q))+
+ 2ζνq
41
26(−3 + O(q)) + 2ζ3νq
19
26(−3 + O(q)) + 2ζ9νq
5
26(1 + O(q))+
+ 2ζ12νq
11
26(−1 + O(q)) + 2ζ10νq
7
26(−1 + O(q)) + 2ζ4νq
47
26(−1 + O(q))+
+ ζ2νq
17
26(6 + O(q)) + ζ5νq
23
26(8 + O(q)) + ζ6νq
25
26(−1 + O(q))+
+ ζ11νq
9
26(−3 + O(q)) + ζ8νq
29
26(2 + O(q)) + ζ7νq
1
26(1 + O(q))]4.
We will calculate the q-term which is the lowest degree. For example, consider
the partition 26 = 3 · 1 + 23, the corresponding term is
 4
3, 1

(ζ7νq
1
26)3 · 8ζ5νq
23
26 = 32q.
For the other partitions, the calculation is similar. In conclusion, we ﬁnd that
the coeﬃcients of the q-term is an integer. Hence, for Φ4,0(y1(z), . . . , y6(z))
which is a modular form for Γ(1) with weight 32, the lowest degree term is
given by
some integer · q · q
3
24·16 = some integer · q3.
This implies that Φ4,0(y1(z), . . . , y6(z)) has a factor of ∆(z)3, which is a cusp
form of weight 36. Therefore, Φ4,0(y1(z), . . . , y6(z)) = 0. The calculation of
Φ8 is similar as that of Φ4,0.
The third part is the calculation of Φ0,2 and Φ0,5. Up to a constant, Φ0,2 =
δ2
0+δ2
1+· · ·+δ2
12+δ2
∞. As a polynomial in six variables, Φ0,2(z1, z2, z3, z4, z5, z6)
is a G-invariant polynomial. Moreover, for γ ∈Γ(1),
Φ0,2(X(γ(z))T) = Φ0,2(u(γ)j(γ, z)(ρ(γ)X(z))T)
=u(γ)12j(γ, z)12Φ0,2((ρ(γ)X(z))T ) = j(γ, z)12Φ0,2((ρ(γ)X(z))T).
31
Note that ρ(γ) ∈⟨ρ(s), ρ(t)⟩= G and Φ0,2 is a G-invariant polynomial, we
have
Φ0,2(X(γ(z))T ) = j(γ, z)12Φ0,2(X(z)T),
for γ ∈Γ(1).
This implies that Φ0,2(x1(z), . . . , x6(z)) is a modular form of weight 12 for
the full modular group Γ(1). Moreover, we will show that it is a cusp form.
In fact,
Φ0,2(a1(z), . . . , a6(z)) = 134q
7
2(1 + O(q))2+
+
12
X
ν=0
[−13q
7
4(1 + O(q))+
+ ζνq
43
52(13 + O(q)) + ζ2νq
47
52(−22 + O(q)) + ζ3νq
51
52(−21 + O(q))+
+ ζ4νq
3
52(−1 + O(q)) + ζ5νq
7
52(2 + O(q)) + ζ6νq
11
52(2 + O(q))+
+ ζ7νq
15
52(−2 + O(q)) + ζ8νq
19
52(−8 + O(q)) + ζ9νq
23
52(6 + O(q))+
+ ζ10νq
27
52(1 + O(q)) + ζ11νq
31
52(−8 + O(q)) + ζ12νq
35
52(17 + O(q))]2.
We will calculate the q
1
2-term which is the lowest degree. For the partition
26 = 3 + 23, the corresponding term is

2
1, 1

ζ4νq
3
52 · (−1) · ζ9νq
23
52 · 6 = −12q
1
2.
For the partition 26 = 7 + 19, the corresponding term is
 2
1, 1

ζ5νq
7
52 · 2 · ζ8νq
19
52 · (−8) = −32q
1
2.
For the partition 26 = 11 + 15, the corresponding term is
 2
1, 1

ζ6νq
11
52 · 2 · ζ7νq
15
52 · (−2) = −8q
1
2.
Hence, for Φ0,2(x1(z), . . . , x6(z)) which is a modular form for Γ(1) with weight
12, the lowest degree term is given by (−12 −32 −8)q
1
2 · q
12
24 = −52q. Thus,
Φ0,2(x1(z), . . . , x6(z)) = q(−13 · 52 + O(q)).
The leading term of Φ0,2(x1(z), . . . , x6(z)) together with its weight 12 suﬃce
to identify this modular form with
Φ0,2(x1(z), . . . , x6(z)) = −13 · 52∆(z).
32
Up to a constant, Φ0,5 = δ5
0 + δ5
1 + · · · + δ5
12 + δ5
∞. As a polynomial in six
variables, Φ0,5(z1, z2, z3, z4, z5, z6) is a G-invariant polynomial. Similarly as
above, we can show that Φ0,5(x1(z), . . . , x6(z)) is a modular form of weight
30 for the full modular group Γ(1). Moreover, we will show that it is a cusp
form. In fact,
Φ0,5(a1(z), . . . , a6(z)) = 1310q
35
4 (1 + O(q))5+
+
12
X
ν=0
[−13q
7
4(1 + O(q))+
+ ζνq
43
52(13 + O(q)) + ζ2νq
47
52(−22 + O(q)) + ζ3νq
51
52(−21 + O(q))+
+ ζ4νq
3
52(−1 + O(q)) + ζ5νq
7
52(2 + O(q)) + ζ6νq
11
52(2 + O(q))+
+ ζ7νq
15
52(−2 + O(q)) + ζ8νq
19
52(−8 + O(q)) + ζ9νq
23
52(6 + O(q))+
+ ζ10νq
27
52(1 + O(q)) + ζ11νq
31
52(−8 + O(q)) + ζ12νq
35
52(17 + O(q))]5.
We will calculate the q
3
4-term which is the lowest degree. (1) For the partition
39 = 4 · 3 + 27, the corresponding term is

5
4, 1

(ζ4νq
3
52 · (−1))4 · ζ10νq
27
52 = 5q
3
4.
(2) For the partition 39 = 3 · 3 + 7 + 23, the corresponding term is

5
3, 1, 1

(ζ4νq
3
52 · (−1))3 · ζ5νq
7
52 · 2 · ζ9νq
23
52 · 6 = −240q
3
4.
(3) For the partition 39 = 3 · 3 + 11 + 19, the corresponding term is

5
3, 1, 1

(ζ4νq
3
52 · (−1))3 · ζ6νq
11
52 · 2 · ζ8νq
19
52 · (−8) = 320q
3
4.
(4) For the partition 39 = 3 · 3 + 2 · 15, the corresponding term is
 5
3, 2

(ζ4νq
3
52 · (−1))3 · (ζ7νq
15
52 · (−2))2 = −40q
3
4.
(5) For the partition 39 = 2 · 3 + 3 · 11, the corresponding term is

5
2, 3

(ζ4νq
3
52 · (−1))2 · (ζ6νq
11
52 · 2)3 = 80q
3
4.
33
(6) For the partition 39 = 2 · 3 + 2 · 7 + 19, the corresponding term is

5
2, 2, 1

(ζ4νq
3
52 · (−1))2 · (ζ5νq
7
52 · 2)2 · ζ8νq
19
52 · (−8) = −960q
3
4.
(7) For the partition 39 = 2 · 3 + 7 + 11 + 15, the corresponding term is

5
2, 1, 1, 1

(ζ4νq
3
52 · (−1))2 · ζ5νq
7
52 · 2 · ζ6νq
11
52 · 2 · ζ7νq
15
52 · (−2) = −480q
3
4.
(8) For the partition 39 = 1 · 3 + 3 · 7 + 15, the corresponding term is

5
1, 3, 1

ζ4νq
3
52 · (−1) · (ζ5νq
7
52 · 2)3 · ζ7νq
15
52 · (−2) = 320q
3
4.
(9) For the partition 39 = 1 · 3 + 2 · 7 + 2 · 11, the corresponding term is

5
1, 2, 2

ζ4νq
3
52 · (−1) · (ζ5νq
7
52 · 2)2 · (ζ6νq
11
52 · 2)2 = −480q
3
4.
(10) For the partition 39 = 4 · 7 + 11, the corresponding term is

5
4, 1

(ζ5νq
7
52 · 2)4 · ζ6νq
11
52 · 2 = 160q
3
4.
Hence, for Φ0,5(x1(z), . . . , x6(z)) which is a modular form for Γ(1) with weight
30, the lowest degree term is given by
(5 −240 + 320 −40 + 80 −960 −480 + 320 −480 + 160)q
3
4 · q
30
24 = −1315q2.
Thus,
Φ0,5(x1(z), . . . , x6(z)) = q2(−13 · 1315 + O(q)).
The leading term of Φ0,5(x1(z), . . . , x6(z)) together with its weight 30 suﬃce
to identify this modular form with
Φ0,5(x1(z), . . . , x6(z)) = −13 · 1315∆(z)2E6(z).
The last part is the calculation of Φ10, Φ14, Φ1,2, Φ2,2, Φ3,3 and Φ6,1. For
Φ10 = w0δ0 + w1δ1 + · · · + w12δ12 + w∞δ∞. As a polynomial in six variables,
Φ10(z1, z2, z3, z4, z5, z6) is a G-invariant polynomial. Moreover, for γ ∈Γ(1),
Φ10(U(γ(z))T ) = Φ10(j(γ, z)5(ρ(γ)U(z))T ) = j(γ, z)50Φ10((ρ(γ)U(z))T ).
34
Note that ρ(γ) ∈⟨ρ(s), ρ(t)⟩= G and Φ10 is a G-invariant polynomial, we
have
Φ10(U(γ(z))T ) = j(γ, z)50Φ10(U(z)T ),
for γ ∈Γ(1).
This implies that Φ10(u1(z), . . . , u6(z)) is a modular form of weight 50 for
the full modular group Γ(1). Moreover, we will show that it is a cusp form.
In fact,
Φ10(a1(z), . . . , a6(z)) = 133q
9
4(1 + O(q))2+
+
12
X
ν=0
[q
1
2(−1 + O(q))+
+ 2ζνq
41
26(−3 + O(q)) + 2ζ3νq
19
26(−3 + O(q)) + 2ζ9νq
5
26(1 + O(q))+
+ 2ζ12νq
11
26(−1 + O(q)) + 2ζ10νq
7
26(−1 + O(q)) + 2ζ4νq
47
26(−1 + O(q))+
+ ζ2νq
17
26(6 + O(q)) + ζ5νq
23
26(8 + O(q)) + ζ6νq
25
26(−1 + O(q))+
+ ζ11νq
9
26(−3 + O(q)) + ζ8νq
29
26(2 + O(q)) + ζ7νq
1
26(1 + O(q))]
× [−13q
7
4(1 + O(q))+
+ ζνq
43
52(13 + O(q)) + ζ2νq
47
52(−22 + O(q)) + ζ3νq
51
52(−21 + O(q))+
+ ζ4νq
3
52(−1 + O(q)) + ζ5νq
7
52(2 + O(q)) + ζ6νq
11
52(2 + O(q))+
+ ζ7νq
15
52(−2 + O(q)) + ζ8νq
19
52(−8 + O(q)) + ζ9νq
23
52(6 + O(q))+
+ ζ10νq
27
52(1 + O(q)) + ζ11νq
31
52(−8 + O(q)) + ζ12νq
35
52(17 + O(q))]
We will calculate the q
1
4-term which is the lowest degree:
2q
5
26 · q
3
52 · (−1) + q
1
26 · 1 · q
11
52 · 2 = 0.
Hence, for Φ10(u1(z), . . . , u6(z)) which is a modular form for Γ(1) with weight
50, the lowest degree term is given by
some integer · q
5
4 · q
9
24 ·10 = some integer · q5.
This implies that Φ10(u1(z), . . . , u6(z)) has a factor of ∆(z)5, which is a
cusp form of weight 60. Therefore, Φ10(u1(z), . . . , u6(z)) = 0. Consequently,
Φ10(x1(z), . . . , x6(z)) = 0. The calculation of Φ14 and Φ1,2 is similar as that
of Φ10.
35
For Φ2,2 = w2
0δ2
0 + w2
1δ2
1 + · · · + w2
12δ2
12 + w2
∞δ2
∞. As a polynomial in six
variables, Φ2,2(z1, z2, z3, z4, z5, z6) is a G-invariant polynomial. Moreover, for
γ ∈Γ(1),
Φ2,2(U(γ(z))T ) = Φ2,2(j(γ, z)5(ρ(γ)U(z))T ) = j(γ, z)100Φ2,2((ρ(γ)U(z))T ).
Note that ρ(γ) ∈⟨ρ(s), ρ(t)⟩= G and Φ2,2 is a G-invariant polynomial, we
have
Φ2,2(U(γ(z))T ) = j(γ, z)100Φ2,2(U(z)T ),
for γ ∈Γ(1).
This implies that Φ2,2(u1(z), . . . , u6(z)) is a modular form of weight 100 for
the full modular group Γ(1). Moreover, we will show that it is a cusp form.
In fact,
Φ2,2(a1(z), . . . , a6(z)) = 136q
9
2(1 + O(q))2+
+
12
X
ν=0
[q
1
2(−1 + O(q))+
+ 2ζνq
41
26(−3 + O(q)) + 2ζ3νq
19
26(−3 + O(q)) + 2ζ9νq
5
26(1 + O(q))+
+ 2ζ12νq
11
26(−1 + O(q)) + 2ζ10νq
7
26(−1 + O(q)) + 2ζ4νq
47
26(−1 + O(q))+
+ ζ2νq
17
26(6 + O(q)) + ζ5νq
23
26(8 + O(q)) + ζ6νq
25
26(−1 + O(q))+
+ ζ11νq
9
26(−3 + O(q)) + ζ8νq
29
26(2 + O(q)) + ζ7νq
1
26(1 + O(q))]2
× [−13q
7
4(1 + O(q))+
+ ζνq
43
52(13 + O(q)) + ζ2νq
47
52(−22 + O(q)) + ζ3νq
51
52(−21 + O(q))+
+ ζ4νq
3
52(−1 + O(q)) + ζ5νq
7
52(2 + O(q)) + ζ6νq
11
52(2 + O(q))+
+ ζ7νq
15
52(−2 + O(q)) + ζ8νq
19
52(−8 + O(q)) + ζ9νq
23
52(6 + O(q))+
+ ζ10νq
27
52(1 + O(q)) + ζ11νq
31
52(−8 + O(q)) + ζ12νq
35
52(17 + O(q))]2
We will calculate the q
1
2-term which is the lowest degree, there are ﬁve such
terms:
(1)
(ζ7νq
1
26 · 1)2 × [(ζ6νq
11
52 · 2)2 + 2 · ζ5νq
7
52 · 2 · ζ7νq
15
52 · (−2)+
+ 2 · ζ4νq
3
52 · (−1) · ζ8νq
19
52 · (−8)]
=12q
1
2.
36
(2)
2 · 2ζ9νq
5
26 · 1 · ζ7νq
1
26 · 1 × [(ζ5νq
7
52 · 2)2 + 2ζ4νq
3
52 · (−1) · ζ6νq
11
52 · 2] = 0.
(3)
2 · 2ζ10νq
7
26 · (−1) · ζ7νq
1
26 · 1 × 2ζ4νq
3
52 · (−1) · ζ5νq
7
52 · 2 = 16q
1
2.
(4)
2 · ζ11νq
9
26 · (−3) · ζ7νq
1
26 · 1 × [ζ4νq
3
52 · (−1)]2 = −6q
1
2.
(5)
(2ζ9νq
5
26 · 1)2 × (ζ4νq
3
52 · (−1))2 = 4q
1
2.
Hence, for Φ2,2(u1(z), . . . , u6(z)) which is a modular form for Γ(1) with weight
100, the lowest degree term is given by
(12 + 0 + 16 −6 + 4)q
1
2 · q
9
24 ·20 = 26q8.
Thus,
Φ2,2(u1(z), . . . , u6(z)) = q8(13 · 26 + O(q)).
The leading term of Φ2,2(u1(z), . . . , u6(z)) together with its weight 100 suﬃce
to identify this modular form with Φ2,2(u1(z), . . . , u6(z)) = 13·26∆(z)8E4(z).
Consequently,
Φ2,2(x1(z), . . . , x6(z)) = 13 · 26∆(z)8E4(z)/η(z)160 = 13 · 26η(z)8∆(z)E4(z).
The calculation of Φ3,3 and Φ6,1 is similar as that of Φ2,2. We have
Φ3,3(x1(z), . . . , x6(z)) = −13 · 27∆(z)2E6(z).
Φ6,1(x1(z), . . . , x6(z)) = −13 · 285∆(z)2E6(z).
After normalization, this completes the proof of Theorem 3.3.
Now we give the normalization for the following three families of invariant
homogeneous polynomials of degrees d = 18, 22 and 34. For d = 18, there
are two such invariant homogeneous polynomials Φ3,1 and Φ0,3:











Φ3,1 :=
1
13 · 2
 12
X
ν=0
w3
νδν + w3
∞δ∞
!
,
Φ0,3 :=
1
13 · 6
 12
X
ν=0
δ3
ν + δ3
∞
!
,
(3.22)
37
For d = 22, there are two such invariant homogeneous polynomials Φ1,3 and
Φ4,1. For d = 34, there are three such invariant homogeneous polynomials
Φ1,5, Φ4,3 and Φ7,1.
Theorem 3.4. The G-invariant homogeneous polynomials Φm,n of de-
grees d = 18, 22 and 34 in x1(z), . . ., x6(z) can be identiﬁed with modular
forms as follows:























Φ3,1(x1(z), . . . , x6(z)) = ∆(z)E6(z),
Φ0,3(x1(z), . . . , x6(z)) = ∆(z)E6(z),
Φ1,3(x1(z), . . . , x6(z)) = 0,
Φ4,1(x1(z), . . . , x6(z)) = 0,
Φ1,5(x1(z), . . . , x6(z)) = 0,
Φ4,3(x1(z), . . . , x6(z)) = 0,
Φ7,1(x1(z), . . . , x6(z)) = 0.
(3.23)
Proof. The proof is similar as that of Theorem 3.3.
As a consequence of Theorem 3.3 and Theorem 3.4, we ﬁnd an image of
the modular curve X = X(13) in CP5 given by the complete intersection
curve Y .
Theorem 3.5. There is a morphism
Φ : X →Y ⊂CP5
with Φ(z) = (x1(z), . . . , x6(z)), where Y is a complete intersection curve
corresponding to the ideal
I = I(Y ) = (Φ4, Φ8, Φ10, Φ14).
(3.24)
Moreover, there is a morphism Ψ : X →Z ⊂CP5, where Z is the scheme
corresponding to the ideal
J = J(Z) = (Φ4, Φ8, Φ10, Φ14, Φ4,0, Φ1,2, Φ1,3, Φ4,1, Φ1,5, Φ4,3, Φ7,1).
(3.25)
38
Proof. Theorem 3.3 and Theorem 3.4 imply that











































Φ4(x1(z), . . . , x6(z)) = 0,
Φ8(x1(z), . . . , x6(z)) = 0,
Φ10(x1(z), . . . , x6(z)) = 0,
Φ14(x1(z), . . . , x6(z)) = 0,
Φ4,0(x1(z), . . . , x6(z)) = 0,
Φ1,2(x1(z), . . . , x6(z)) = 0,
Φ1,3(x1(z), . . . , x6(z)) = 0,
Φ4,1(x1(z), . . . , x6(z)) = 0,
Φ1,5(x1(z), . . . , x6(z)) = 0,
Φ4,3(x1(z), . . . , x6(z)) = 0,
Φ7,1(x1(z), . . . , x6(z)) = 0.
This complete the proof of Theorem 3.5.
