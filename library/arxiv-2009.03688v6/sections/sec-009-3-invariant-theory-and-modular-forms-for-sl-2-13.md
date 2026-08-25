---
doc_id: arxiv-2009.03688v6
doc_title: "E8-singularity, invariant theory and modular forms"
section_id: sec-009-3-invariant-theory-and-modular-forms-for-sl-2-13
section_title: "Invariant theory and modular forms for SL (2, 13)"
section_number: 3
pages: 16-26
source_pdf: 2009.03688v6.pdf
source_sha256: 8eb9b4cbe2690730
doc_brief: "E8-singularity, invariant theory and modular forms — As an algebraic surface, the equation of E8-singularity x5 + y3 + z2 = 0 can be obtained from a quotient CY /SL(2, 13) over the modular curve"
---
The representation of SL(2 , 13) which we will consider is the unique six-
dimensional irreducible complex representation for which the eigenv alues of(1 1
0 1
)
are the exp( a
.2πi/13) for a a non-square mod 13. We will give an
explicit realization of this representation. This explicit realization will p lay a
major role for giving a complete system of invariants associated to S L(2, 13).
At ﬁrst, we will study the six-dimensional representation of the ﬁn ite group
SL(2, 13) of order 2184, which acts on the ﬁve-dimensional projective s pace
P5 = {(z1, z2, z3, z4, z5, z6) : zi ∈ C (i = 1, 2, 3, 4, 5, 6)}. This representation
is deﬁned over the cyclotomic ﬁeld Q(e
2πi
13 ). Put
S = − 1√
13








ζ 12 − ζ ζ 10 − ζ 3 ζ 4 − ζ 9 ζ 5 − ζ 8 ζ 2 − ζ 11 ζ 6 − ζ 7
ζ 10 − ζ 3 ζ 4 − ζ 9 ζ 12 − ζ ζ 2 − ζ 11 ζ 6 − ζ 7 ζ 5 − ζ 8
ζ 4 − ζ 9 ζ 12 − ζ ζ 10 − ζ 3 ζ 6 − ζ 7 ζ 5 − ζ 8 ζ 2 − ζ 11
ζ 5 − ζ 8 ζ 2 − ζ 11 ζ 6 − ζ 7 ζ − ζ 12 ζ 3 − ζ 10 ζ 9 − ζ 4
ζ 2 − ζ 11 ζ 6 − ζ 7 ζ 5 − ζ 8 ζ 3 − ζ 10 ζ 9 − ζ 4 ζ − ζ 12
ζ 6 − ζ 7 ζ 5 − ζ 8 ζ 2 − ζ 11 ζ 9 − ζ 4 ζ − ζ 12 ζ 3 − ζ 10
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
T = diag(ζ 7, ζ11, ζ8, ζ6, ζ2, ζ5), (3.2)
where ζ = exp(2πi/13). We have
S2 = −I, T 13 = (ST )3 = I. (3.3)
In [30], we put P = ST −1S and Q = ST 3. Then ( Q3P 4)3 = −I (see [30], the
proof of Theorem 3.1). Let G = ⟨S, T ⟩, then G ∼= SL(2, 13).
Put θ1 = ζ + ζ 3 + ζ 9, θ2 = ζ 2 + ζ 6 + ζ 5, θ3 = ζ 4 + ζ 12 + ζ 10, and
θ4 = ζ 8 + ζ 11 + ζ 7. We ﬁnd that
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
Hence, θ1, θ2, θ3 and θ4 satisfy the quartic equation z4 + z3 + 2z2 −4z + 3 = 0,
which can be decomposed as two quadratic equations
(
z2 + 1 +
√
13
2 z + 5 +
√
13
2
)(
z2 + 1 −
√
13
2 z + 5 −
√
13
2
)
= 0
over the real quadratic ﬁeld Q(
√
13). Therefore, the four roots are given as
follows: 
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
(
−1 +
√
13 +
√
−26 + 6
√
13
)
,
θ2 = 1
4
(
−1 −
√
13 +
√
−26 − 6
√
13
)
,
θ3 = 1
4
(
−1 +
√
13 −
√
−26 + 6
√
13
)
,
θ4 = 1
4
(
−1 −
√
13 −
√
−26 − 6
√
13
)
.
Moreover, we ﬁnd that
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
θ1 + θ3 − θ2 − θ4 =
√
13,
θ1 − θ3 − θ2 + θ4 = −
√
−13 + 2
√
13,
θ1 − θ3 + θ2 − θ4 =
√
−13 − 2
√
13.
17
Let us study the action of ST ν on P5, where ν = 0, 1, . . . ,12. Put
α = ζ + ζ 12 − ζ 5 − ζ 8, β = ζ 3 + ζ 10 − ζ 2 − ζ 11, γ = ζ 9 + ζ 4 − ζ 6 − ζ 7.
We ﬁnd that
13ST ν(z1) · ST ν(z4)
=βz1z4 + γz2z5 + αz3z6+
+ γζ νz2
1 + αζ 9νz2
2 + βζ 3νz2
3 − γζ 12νz2
4 − αζ 4νz2
5 − βζ 10νz2
6+
+ (α − β)ζ 5νz1z2 + (β − γ)ζ 6νz2z3 + (γ − α)ζ 2νz1z3+
+ (β − α)ζ 8νz4z5 + (γ − β)ζ 7νz5z6 + (α − γ)ζ 11νz4z6+
− (α + β)ζ νz3z4 − (β + γ)ζ 9νz1z5 − (γ + α)ζ 3νz2z6+
− (α + β)ζ 12νz1z6 − (β + γ)ζ 4νz2z4 − (γ + α)ζ 10νz3z5.
13ST ν(z2) · ST ν(z5)
=γz1z4 + αz2z5 + βz3z6+
+ αζ νz2
1 + βζ 9νz2
2 + γζ 3νz2
3 − αζ 12νz2
4 − βζ 4νz2
5 − γζ 10νz2
6+
+ (β − γ)ζ 5νz1z2 + (γ − α)ζ 6νz2z3 + (α − β)ζ 2νz1z3+
+ (γ − β)ζ 8νz4z5 + (α − γ)ζ 7νz5z6 + (β − α)ζ 11νz4z6+
− (β + γ)ζ νz3z4 − (γ + α)ζ 9νz1z5 − (α + β)ζ 3νz2z6+
− (β + γ)ζ 12νz1z6 − (γ + α)ζ 4νz2z4 − (α + β)ζ 10νz3z5.
13ST ν(z3) · ST ν(z6)
=αz1z4 + βz2z5 + γz3z6+
+ βζ νz2
1 + γζ 9νz2
2 + αζ 3νz2
3 − βζ 12νz2
4 − γζ 4νz2
5 − αζ 10νz2
6+
+ (γ − α)ζ 5νz1z2 + (α − β)ζ 6νz2z3 + (β − γ)ζ 2νz1z3+
+ (α − γ)ζ 8νz4z5 + (β − α)ζ 7νz5z6 + (γ − β)ζ 11νz4z6+
− (γ + α)ζ νz3z4 − (α + β)ζ 9νz1z5 − (β + γ)ζ 3νz2z6+
− (γ + α)ζ 12νz1z6 − (α + β)ζ 4νz2z4 − (β + γ)ζ 10νz3z5.
Note that α + β + γ =
√
13, we ﬁnd that
√
13 [ST ν(z1) · ST ν(z4) + ST ν(z2) · ST ν(z5) + ST ν(z3) · ST ν(z6)]
=(z1z4 + z2z5 + z3z6) + (ζ νz2
1 + ζ 9νz2
2 + ζ 3νz2
3) − (ζ 12νz2
4 + ζ 4νz2
5 + ζ 10νz2
6)+
− 2(ζ νz3z4 + ζ 9νz1z5 + ζ 3νz2z6) − 2(ζ 12νz1z6 + ζ 4νz2z4 + ζ 10νz3z5).
18
Let
ϕ∞(z1, z2, z3, z4, z5, z6) =
√
13(z1z4 + z2z5 + z3z6) (3 .4)
and
ϕν(z1, z2, z3, z4, z5, z6) = ϕ∞(ST ν(z1, z2, z3, z4, z5, z6)) (3 .5)
for ν = 0, 1, . . . ,12. Then
ϕν =(z1z4 + z2z5 + z3z6) + ζ ν(z2
1 − 2z3z4) + ζ 4ν(−z2
5 − 2z2z4)+
+ ζ 9ν(z2
2 − 2z1z5) + ζ 3ν(z2
3 − 2z2z6) + ζ 12ν(−z2
4 − 2z1z6)+
+ ζ 10ν(−z2
6 − 2z3z5).
(3.6)
This leads us to deﬁne the following senary quadratic forms (quadra tic forms
in six variables): 
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
1 − 2z3z4,
A2 = −z2
5 − 2z2z4,
A3 = z2
2 − 2z1z5,
A4 = z2
3 − 2z2z6,
A5 = −z2
4 − 2z1z6,
A6 = −z2
6 − 2z3z5.
(3.7)
Hence,
√
13ST ν(A0) = A0 +ζ νA1 +ζ 4νA2 +ζ 9νA3 +ζ 3νA4 +ζ 12νA5 +ζ 10νA6. (3.8)
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
0 0 0 0 0 1
0 0 0 1 0 0
0 0 0 0 1 0
0 0 −1 0 0 0
−1 0 0 0 0 0
0 −1 0 0 0 0








. (3.9)
Note that H 6 = 1 and H −1T H = −T 4. Thus, ⟨H, T ⟩ ∼= Z13 ⋊ Z6. Hence, it
is a maximal subgroup of order 78 of PSL(2 , 13) with index 14. We ﬁnd that
ϕ2
∞ is invariant under the action of the maximal subgroup ⟨H, T ⟩. Note that
ϕ∞ =
√
13A0, ϕ ν = A0 + ζ νA1 + ζ 4νA2 + ζ 9νA3 + ζ 3νA4 + ζ 12νA5 + ζ 10νA6
19
for ν = 0 , 1, . . . ,12. Let w = ϕ2, w∞ = ϕ2
∞ and wν = ϕ2
ν. Then w∞, wν for
ν = 0, . . . ,12 form an algebraic equation of degree fourteen, which is just the
Jacobian equation of degree fourteen (see [18], pp.161-162), wh ose roots are
these wν and w∞:
w14 + a1w13 + · · · + a13w + a14 = 0.
On the other hand, we have
− 13
√
13ST ν(z1) · ST ν(z2) · ST ν(z3)
= − r4(ζ 8νz3
1 + ζ 7νz3
2 + ζ 11νz3
3) − r2(ζ 5νz3
4 + ζ 6νz3
5 + ζ 2νz3
6)
− r3(ζ 12νz2
1z2 + ζ 4νz2
2z3 + ζ 10νz2
3z1) − r1(ζ νz2
4z5 + ζ 9νz2
5z6 + ζ 3νz2
6z4)
+ 2r1(ζ 3νz1z2
2 + ζ νz2z2
3 + ζ 9νz3z2
1) − 2r3(ζ 10νz4z2
5 + ζ 12νz5z2
6 + ζ 4νz6z2
4)
+ 2r4(ζ 7νz2
1z4 + ζ 11νz2
2z5 + ζ 8νz2
3z6) − 2r2(ζ 6νz1z2
4 + ζ 2νz2z2
5 + ζ 5νz3z2
6)+
+ r1(ζ 3νz2
1z5 + ζ νz2
2z6 + ζ 9νz2
3z4) + r3(ζ 10νz2z2
4 + ζ 12νz3z2
5 + ζ 4νz1z2
6)+
+ r2(ζ 6νz2
1z6 + ζ 2νz2
2z4 + ζ 5νz2
3z5) + r4(ζ 7νz3z2
4 + ζ 11νz1z2
5 + ζ 8νz2z2
6)+
+ r0z1z2z3 + r∞z4z5z6+
− r4(ζ 11νz1z2z4 + ζ 8νz2z3z5 + ζ 7νz1z3z6)+
+ r2(ζ 2νz1z4z5 + ζ 5νz2z5z6 + ζ 6νz3z4z6)+
− 3r4(ζ 7νz1z2z5 + ζ 11νz2z3z6 + ζ 8νz1z3z4)+
+ 3r2(ζ 6νz2z4z5 + ζ 2νz3z5z6 + ζ 5νz1z4z6)+
− r3(ζ 10νz1z2z6 + ζ 4νz1z3z5 + ζ 12νz2z3z4)+
+ r1(ζ 3νz3z4z5 + ζ 9νz2z4z6 + ζ νz1z5z6),
where
r0 = 2(θ1 − θ3) − 3(θ2 − θ4), r ∞ = 2(θ4 − θ2) − 3(θ1 − θ3),
r1 =
√
−13 − 2
√
13, r 2 =
√
−13 + 3
√
13
2 ,
r3 =
√
−13 + 2
√
13, r 4 =
√
−13 − 3
√
13
2 .
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
2z6 − z2
4z5 + z1z5z6,
D2 = −z3
6 + z2
2z4 − 2z2z2
5 + z1z4z5 + 3z3z5z6,
D3 = 2z1z2
2 + z2
1z5 − z4z2
6 + z3z4z5,
D4 = −z2
2z3 + z1z2
6 − 2z2
4z6 − z1z3z5,
D5 = −z3
4 + z2
3z5 − 2z3z2
6 + z2z5z6 + 3z1z4z6,
D6 = −z3
5 + z2
1z6 − 2z1z2
4 + z3z4z6 + 3z2z4z5,
D7 = −z3
2 + z3z2
4 − z1z3z6 − 3z1z2z5 + 2z2
1z4,
D8 = −z3
1 + z2z2
6 − z2z3z5 − 3z1z3z4 + 2z2
3z6,
D9 = 2z2
1z3 + z2
3z4 − z2
5z6 + z2z4z6,
D10 = −z1z2
3 + z2z2
4 − 2z4z2
5 − z1z2z6,
D11 = −z3
3 + z1z2
5 − z1z2z4 − 3z2z3z6 + 2z2
2z5,
D12 = −z2
1z2 + z3z2
5 − 2z5z2
6 − z2z3z4,
D∞ = z4z5z6.
(3.10)
Then
− 13
√
13ST ν(D0)
=r0D0 + r1ζ νD1 + r2ζ 2νD2 + r1ζ 3νD3 + r3ζ 4νD4+
+ r2ζ 5νD5 + r2ζ 6νD6 + r4ζ 7νD7 + r4ζ 8νD8+
+ r1ζ 9νD9 + r3ζ 10νD10 + r4ζ 11νD11 + r3ζ 12νD12 + r∞D∞.
− 13
√
13ST ν(D∞)
=r∞D0 − r3ζ νD1 − r4ζ 2νD2 − r3ζ 3νD3 + r1ζ 4νD4+
− r4ζ 5νD5 − r4ζ 6νD6 + r2ζ 7νD7 + r2ζ 8νD8+
− r3ζ 9νD9 + r1ζ 10νD10 + r2ζ 11νD11 + r1ζ 12νD12 − r0D∞.
Let
δ∞(z1, z2, z3, z4, z5, z6) = 13 2(z2
1z2
2z2
3 + z2
4z2
5z2
6) (3 .11)
and
δν(z1, z2, z3, z4, z5, z6) = δ∞(ST ν(z1, z2, z3, z4, z5, z6)) (3 .12)
for ν = 0, 1, . . . ,12. Then
δν = 13 2ST ν(G0) = −13G0 + ζ νG1 + ζ 2νG2 + · · · + ζ 12νG12, (3.13)
21
where the senary sextic forms (i.e., sextic forms in six variables) are given as
follows: 
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
G1 = − D2
7 + 2D0D1 + 10D∞D1 + 2D2D12+
− 2D3D11 − 4D4D10 − 2D9D5,
G2 = − 2D2
1 − 4D0D2 + 6D∞D2 − 2D4D11+
+ 2D5D10 − 2D6D9 − 2D7D8,
G3 = − D2
8 + 2D0D3 + 10D∞D3 + 2D6D10+
− 2D9D7 − 4D12D4 − 2D1D2,
G4 = − D2
2 + 10D0D4 − 2D∞D4 + 2D5D12+
− 2D9D8 − 4D1D3 − 2D10D7,
G5 = − 2D2
9 − 4D0D5 + 6D∞D5 − 2D10D8+
+ 2D6D12 − 2D2D3 − 2D11D7,
G6 = − 2D2
3 − 4D0D6 + 6D∞D6 − 2D127+
+ 2D2D4 − 2D5D1 − 2D8D11,
G7 = − 2D2
10 + 6D0D7 + 4D∞D7 − 2D1D6+
− 2D2D5 − 2D8D12 − 2D9D11,
G8 = − 2D2
4 + 6D0D8 + 4D∞D8 − 2D3D5+
− 2D6D2 − 2D11D10 − 2D1D7,
G9 = − D2
11 + 2D0D9 + 10D∞D9 + 2D5D4+
− 2D1D8 − 4D10D12 − 2D3D6,
G10 = − D2
5 + 10D0D10 − 2D∞D10 + 2D6D4+
− 2D3D7 − 4D9D1 − 2D12D11,
G11 = − 2D2
12 + 6D0D11 + 4D∞D11 − 2D9D2+
− 2D5D6 − 2D7D4 − 2D3D8,
G12 = − D2
6 + 10D0D12 − 2D∞D12 + 2D2D10+
− 2D1D11 − 4D3D9 − 2D4D8.
(3.14)
We have that G0 is invariant under the action of ⟨H, T ⟩, a maximal subgroup
of order 78 of PSL(2 , 13) with index 14. Note that δ∞, δν for ν = 0 , . . . ,12
form an algebraic equation of degree fourteen. However, we have
Φ 6 = Φ 0,1 = δ∞ +
12∑
ν=0
δν = 0.
22
Hence, it is not the Jacobian equation of degree fourteen.
Recall that the theta functions with characteristic
[ ǫ
ǫ′
]
∈ R2 is deﬁned
by the following series which converges uniformly and absolutely on co mpact
subsets of C × H (see [10], p. 73):
θ
[
ǫ
ǫ′
]
(z, τ ) =
∑
n∈Z
exp
{
2πi
[ 1
2
(
n + ǫ
2
) 2
τ +
(
n + ǫ
2
) (
z + ǫ′
2
)]}
.
The modiﬁed theta constants (see [10], p. 215) ϕl(τ ) := θ[χl](0, kτ ), where
the characteristic χl =
[ 2l+1
k
1
]
, l = 0 , . . . , k−3
2 , for odd k and χl =
[ 2l
k
0
]
,
l = 0, . . . , k
2 , for even k. We have the following:
Proposition 3.1. (see [10], p. 236). For each odd integer k ≥ 5, the
map Φ : τ ↦→(ϕ0(τ ), ϕ1(τ ), . . . , ϕk− 5
2
(τ ), ϕ k− 3
2
(τ )) from H∪Q∪ {∞} to C
k− 1
2 ,
deﬁnes a holomorphic mapping from H/Γ( k) into CP
k− 3
2 .
In our case, the map Φ : τ ↦→(ϕ0(τ ), ϕ1(τ ), ϕ2(τ ), ϕ3(τ ), ϕ4(τ ), ϕ5(τ ))
gives a holomorphic mapping from the modular curve X(13) = H/Γ(13) into
CP5, which corresponds to our six-dimensional representation, i.e., up to the
constants, z1, . . . , z6 are just modular forms ϕ0(τ ), . . . , ϕ5(τ ). Let
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
a1(z) := e− 11πi
26 θ
[ 11
13
1
]
(0, 13z) = q
121
104
∑
n∈Z
(−1)nq
1
2 (13n2+11n),
a2(z) := e− 7πi
26 θ
[ 7
13
1
]
(0, 13z) = q
49
104
∑
n∈Z
(−1)nq
1
2 (13n2+7n),
a3(z) := e− 5πi
26 θ
[ 5
13
1
]
(0, 13z) = q
25
104
∑
n∈Z
(−1)nq
1
2 (13n2+5n),
a4(z) := −e− 3πi
26 θ
[ 3
13
1
]
(0, 13z) = −q
9
104
∑
n∈Z
(−1)nq
1
2 (13n2+3n),
a5(z) := e− 9πi
26 θ
[ 9
13
1
]
(0, 13z) = q
81
104
∑
n∈Z
(−1)nq
1
2 (13n2+9n),
a6(z) := e− πi
26 θ
[ 1
13
1
]
(0, 13z) = q
1
104
∑
n∈Z
(−1)nq
1
2 (13n2+n)
(3.15)
be the theta constants of order 13 and
A(z) := ( a1(z), a2(z), a3(z), a4(z), a5(z), a6(z))T .
23
The signiﬁcance of our six dimensional representation of SL(2 , 13) comes from
the following:
Proposition 3.2 (see [31], Proposition 2.5). If z ∈ H, then the following
relations hold:
A(z + 1) = e− 3πi
4 T A(z), A
(
−1
z
)
= e
πi
4
√zS A(z), (3.16)
where S and T are given in (3.1) and (3.2), and 0 < arg√z ≤ π/2.
Note that it is (3.16) that gives an explicit realization of the isomorphis m
between the unique sub-representation of parabolic modular form s of weight
1
2 on X(13) and the six-dimensional complex representation of SL(2 , 13) gen-
erated by S and T .
Recall that the principal congruence subgroup of level 13 is the no rmal
subgroup Γ(13) of Γ = SL(2 , Z) deﬁned by the exact sequence 1 → Γ(13) →
Γ(1)
f
→ SL(2, 13) → 1 where f (γ) ≡ γ (mod 13) for γ ∈ Γ = Γ(1). There
is a representation ρ : Γ → GL(6, C) with kernel Γ(13) deﬁned as follows:
if t =
(1 1
0 1
)
and s =
(0 −1
1 0
)
, then ρ(t) = T and ρ(s) = S. To see
that such a representation exists, note that PSL(2 , Z) := Γ /{±I} is deﬁned
by the presentation ⟨s, t; s2 = ( st)3 = 1 ⟩ satisﬁed by s and t and we have
proved that S and T satisfy these relations (in the projective coordinates).
Moreover, we have proved that PSL(2 , 13) is deﬁned by the presentation
⟨S, T ; S2 = T 13 = (ST )3 = 1⟩. Let p = st−1s and q = st3. Then
h := q5p2 · p2q6p8 · q5p2 · p3q =
( 4, 428, 249 −10, 547, 030
−11, 594, 791 27 , 616, 019
)
satisﬁes that ρ(h) = H. The oﬀ-diagonal elements of the matrix h, which
corresponds to H, are congruent to 0 mod 13. The connection to Γ 0(13)
should be obvious.
Put xi(z) = η(z)ai(z), yi(z) = η3(z)ai(z) and ui(z) = η9(z)ai(z) (1 ≤ i ≤
6). Let 




X(z) = ( x1(z), . . . , x6(z))T ,
Y (z) = ( y1(z), . . . , y6(z))T .
U(z) = ( u1(z), . . . , u6(z))T .
24
Then 
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
12 η(z) and η
(
− 1
z
)
= e− πi
4
√zη(z). By Proposition 3.2, we have
X(z + 1) = e− 2πi
3 ρ(t)X(z), X
(
−1
z
)
= zρ(s)X(z),
Y (z + 1) = e− πi
2 ρ(t)Y (z), Y
(
−1
z
)
= e− πi
2 z2ρ(s)Y (z).
U(z + 1) = ρ(t)U(z), U
(
−1
z
)
= z5ρ(s)U(z).
Deﬁne j(γ, z) := cz + d if z ∈ H and γ =
(a b
c d
)
∈ Γ(1). Hence,





X(γ(z)) = u(γ)j(γ, z)ρ(γ)X(z),
Y (γ(z)) = v(γ)j(γ, z)2ρ(γ)Y (z),
U(γ(z)) = j(γ, z)5ρ(γ)U(z)
(3.17)
for γ ∈ Γ(1), where u(γ) = 1 , ω or ω2 with ω = e
2πi
3 and v(γ) = ±1 or
±i. Since Γ(13) = ker ρ, we have X(γ(z)) = u(γ)j(γ, z)X(z), Y (γ(z)) =
v(γ)j(γ, z)2Y (z) and U(γ(z)) = j(γ, z)5U(z) for γ ∈ Γ(13). This means that
the functions x1(z), . . ., x6(z) are modular forms of weight one for Γ(13) with
the same multiplier u(γ) = 1 , ω or ω2 and y1(z), . . ., y6(z) are modular forms
of weight two for Γ(13) with the same multiplier v(γ) = ±1 or ±i.
From now on, we will use the following abbreviation
Aj = Aj(a1(z), . . . , a6(z)) (0 ≤ j ≤ 6),
Dj = Dj(a1(z), . . . , a6(z)) ( j = 0, 1, . . . ,12, ∞)
and
Gj = Gj(a1(z), . . . , a6(z)) (0 ≤ j ≤ 12).
25
We have 
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

A0 = q
1
