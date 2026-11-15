---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-012-c1-expectation-value-of-a-single-characteristic
section_title: "C.1 Expectation value of a single characteristic polynomial"
section_number: null
pages: 23-24
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
Expectation value of a single characteristic polynomial
We now compute the expectation value of a single characteristic polynomial eq.
(C.5) using the
supersymmetric method for ﬁnite-N. As we have shown already this yields the subset of the even
skew-orthogonal polynomials R2n(x) from which the odd polynomials are constructed. At the same
time this also gives the one ﬂavour partition function, which we can compare to the known result from
Wilson chiral perturbation theory [20] in the large-N limit as a consistency check.
The calculation we present here for ν ≥0 is slightly more general than needed in eq. (4.6). Using
the deﬁnitions (2.1) and (2.11) for the Hermitian matrices A and B of sizes n×n and (n+ν)×(n+ν)
as well as matrices W, Ωof sizes n × (n + ν) with weights eqs. (2.2) we have for N = 2n + ν
⟨det[z + /D5]⟩N
=
1
Z(0)
0
Z
dAdBdWdΩdet
 (z + m)11n + A
W + Ω
W † + Ω†
(z −m)11n+ν + B

e
−
1
2(1−a2)Tr(W W †)
×e−
1
4a2 Tr(A2+B2+2ΩΩ†)
(C.6)
Expressing the determinant through integrals over complex Grassmann variables ηi, i = 1, . . . , n and
ψb, b = 1, . . . , n + ν,
det[. . .]
=
Z
d2ηd2ψeη∗
i ((z+m)δij+Aij)ηj+ψ∗
b (W †
bj+Ω†
bj)ηi+η∗
i (Wib+Ωib)ψb+ψ∗
c ((z−m)δcb+Bcb)ψb , (C.7)
we obtain the following result after performing the Gaussian integrals over the matrices A, B, W, Ω:
⟨det[z + /D5]⟩N
∼
Z
d2ηd2ψ e(z+m)η∗
i ηi+(z−m)ψ∗
b ψb−a2((η∗
i ηi)2+(ψ∗
b ψb)2)−2ψ∗
b ψbη∗
i ηi
=
Z
d2ηd2ψ
Z ∞
−∞
dt
Z
C
d2u
π e−t2−|u|2 exp[(z + m −2iat)η∗
j ηj + (z + m −2iat)ψ∗
b ψb]
× exp[−i
p
2(1 −a2)(uη∗
j ηj + u∗ψ∗
bψb)]
=
Z ∞
−∞
dt
Z
C
d2u
π e−t2−|u|2
z + m + 2iat + i
p
2(1 −a2)u
n
×

z −m + 2iat + i
p
2(1 −a2)u∗n+ν
.
(C.8)
In the second step we have linearised upon using one real and one complex variable in our Hubbard-
Stratonovich transformation. As a last step we use the following integral representation for generalised
Laguerre polynomials Lν
n(x) [39]
Z
C
d2u
π e−|u|2(iu + γ)n(iu∗+ λ)n+ν = (−)nλνL(ν)
n (λγ) ,
(C.9)
to obtain
⟨det[z + /D5]⟩N
=
n! (2(1 −a2))n+ ν
2
(−)n√π
Z ∞
−∞
dt e−t2z + 2iat −m
p
2(1 −a2)
ν
L(ν)
n
(z + 2iat)2 −m2
2(1 −a2)

.(C.10)
Here we have put the correct normalisation coeﬃcient that can be read oﬀfrom ⟨det[z + /D5]⟩N =
zN + O(zN−1) for large z. For ν = 0 this reduces to the result given in eq. (4.6). It can be easily seen
that in the microscopic limit eq. (5.1) using eq. (5.2) this reduces to the Nf = 1 ﬂavour partition
function eq. (A.7)
