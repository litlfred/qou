---
doc_id: arxiv-2412.02281v1
doc_title: "u + A"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
doc_brief: "Explicit evaluation of the q-Stokes matrices for certain confluent hypergeometric q-difference equations — We prove a connection formula for the basic hypergeomtric fu nction nϕn−1 (a1,...,a n−1"
---
Set q ∈ R with 0 <q < 1. Take the Lie algebra gln over the ﬁeld of complex numbers with a positive integer
n. Consider the conﬂuent hypergeometric q-diﬀerence system
DqFq(z) := σqFq(z) −Fq(z)
qz −z =
Å
u + A
z
ã
Fq(z), (1)
where σqF (z) = F (qz), u = diag (u1,...,u n−1,u n) and A = (aij) ∈ gln. The inﬁnity z = ∞ is a Fuchsian
singularity of (1) if the diagonal matrix u is invertible. One can use the method of isomonodromy deform ation
to study the connection problem of the equation (1) (see e.g. , [14, 17, 23, 27, 26]). It is parallel to the
corresponding diﬀerential system case studied in [13, 32, 3 5, 41]. In this method, the monodromy data of the
system (1) with u = diag(0,..., 0, 1) are needed.
In this paper, we focus on the irregular case of the form
DqFq(z) =
Å
Enn + A
z
ã
Fq(z), (2)
with Enn = diag(0,..., 0, 1). Denote by A(k) the upper left k ×k submatrix of A = (aij) ∈ gln, and by
λ (k)
1 ,...,λ (k)
k the k eigenvalues of A(k). Set the complex numbers
µi := logq
Ä
1 − (1 −q)λ (n)
i
ä
, 1 ≤i ≤n,
νi := logq
Ä
1 − (1 −q)λ (n−1)
i
ä
, 1 ≤i ≤n − 1,
where we take the principal branch of the logarithmic functi on.
Under the following assumption
νi −νj /∈ Z, for all 1 ≤i ⁄=j ≤n − 1, (3)
the system (2) has a unique formal fundamental solution ˆFq aroundz = ∞. The theory of q-Borel resummation
states that for λ ∈ C∗\ − 1−q
qν j qZ, 1 ≤j ≤n − 1, there exists a meromorphic fundamental solution F (∞)
q (z,λ )
which is asymptotic to ˆFq of q-Gevrey order 1 along the direction λ . For diﬀerent directions, these solutions
are in general diﬀerent (which reﬂects the q-Stokes phenomenon), and the transition between them can be
measured by aq-Stokes matrix (see e.g., [18, 29, 30, 31, 42, 43, 45] for the d etailed study ofq-Borel resummation,
q-Gevrey order and so on). The main result of this paper is the f ollowing theorem, which gives the q-Stokes
matrix of the system (2) explicitly. See Section 3.6 for a pro of.
Theorem 1.1. If the following condition holds for the matrix A:
µi −µj /∈ Z, for all 1 ≤i ⁄=j ≤n,
νi −νj /∈ Z, for all 1 ≤i ⁄=j ≤n − 1,
λ (n−1)
j ⁄=λ (n−2)
l , for all 1 ≤j ≤n − 1, 1 ≤l ≤n − 2,
1
and the following condition holds for z,λ,µ :
λ,µ ∈ C∗, µ /∈λq Z, λ,µ / ∈ − 1 −q
qν l
qZ, for 1 ≤l ≤n − 1, and z ∈ C∗, z /∈ − 1
µqZ, z /∈ − 1
λqZ,
then the q-Stokes matrix Sq (z,λ,µ ;Enn,A ) of the system (2) takes the block matrix form
Sq (z,λ,µ ;Enn,A ) =
Å Idn−1 0
bq 1
ã
,
wherebq =
(
(bq)1,..., (bq)n−1
)
with
(bq)k =
n−1∑
j=1
(− 1)n+k∆ 1,...,n −2,n
1,...,n −1
Ä
A − λ (n−1)
j · Idn
ä
∆ 1,..., ˆk,...,n −1
1,...,n −2
Ä
A − λ (n−1)
j · Idn
ä
∏ n−1
l=1,l ⁄=j
Ä
λ (n−1)
l − λ (n−1)
j
ä ∏ n−2
l=1
Ä
λ (n−2)
l − λ (n−1)
j
ä
n∑
s=1
∏ n−1
l=1 (q1+µ s −ν l ;q)∞∏ n
l=1,l ⁄=s(q1+µ s−µ l ;q)∞
∏ n
l=1,l ⁄=sθq((1 −q)q1−µ l/λ )
∏ n−1
l=1 θq((1 −q)q1−ν l/λ )
θq
(
qµ s−ν nλz
)
θq(λz )
×
∏ n
l=1,l ⁄=s(q1+µ l−ν j ;q)∞
∏ n−1
l=1,l ⁄=j(qν l−µ s ;q)∞
∏ n−1
l=1,l ⁄=j(q1+ν l−ν j ;q)∞
∏ n
l=1,l ⁄=s(qµ l −µ s ;q)∞
θq
( qν j −µ s −1µz)
θq (µz )
θq (qµ sµ/ (1 −q))
θq (qν j −1µ/ (1 −q))
zν j
zν n+1.
Here the deﬁnitions of the q-Pochhammer symbol (a;q)∞ and the q-theta function θq(z) are given in Section
2.1 and ∆ 1,...,n −2,n
1,...,n −1
Ä
A −λ (n−1)
j · Idn
ä
is a minor of the matrix A −λ (n−1)
j · Idn introduced in Section 3.2.
Under the nonresonant condition
µi −µj /∈ Z>0, for all 1 ≤i,j ≤n, (4)
the system (2) has a convergent fundamental solution F (0)
q (z) around z = 0. The transition between F (0)
q (z)
and F (∞)
q (z,λ ) is measured by some connection matrix given explicitly in T heorem 3.8.
The computation of the q-Stokes matrix and the connection matrix mainly relies on th e following connection
formula of the conﬂuent hypergeometric q-diﬀerence equation of the form
z
n−1∏
l=1
(1 −alσq)y(z) = (1 −σq)
n−1∏
l=1
Å
1 − bl
qσq
ã
y(z), (5)
which expresses the solutions of (5) around the origin as a su m of the solutions of (5) around inﬁnity with
pseudo-constant coeﬃcients (see Deﬁnition 2.21). Here σq is the q-shift operator deﬁned by σqy(z) = y(qz).
See Section 2.4 for a proof of the following theorem.
Theorem 1.2. Fora1,a 2,...,a n−1,b 1,b 2,...,b n−1 such that
ai ⁄= 0, ai/a j /∈qZ, for 1 ≤i ⁄=j ≤n − 1, and bl /∈ {0} ∪q−N, for 1 ≤l ≤n − 1,
and for λ,z such that
λ ∈ C∗, λ /∈ −aiqZ, for 1 ≤i ≤n − 1, and z ∈ C∗, z /∈qZ, z /∈ −
∏ n−1
l=1 bl
λ ∏ n−1
l=1 al
qZ,
we have
nϕn−1 (a1,...,a n−1, 0;b1,...,b n−1;q,z )
=
n−1∑
i=1
(a1,..., “ai,...,a n−1,b 1/a i,...,b n−1/a i;q)∞
(b1,...,b n−1,a 1/a i,..., ’ai/a i,...,a n−1/a i;q)∞
θq(−aiz)
θq(−z) zlogqai ·f (∞)
q (z,λ )i
+ (a1,...,a n−1;q)∞
(b1,...,b n−1;q)∞
∏ n−1
s=1 θq
( ∏ n−1
l=1 al
/( λ ∏ n−1
l=1,l ⁄=sbl
))
∏ n−1
s=1 θq
Ä
as
∏ n−1
l=1 al
/(
λ ∏ n−1
l=1 bl
) ä
θq
Ä
λz ∏ n−1
l=1 bl
/ ∏ n−1
l=1 al
ä
θq (λz )
∏ n−1
l=1 zlogqbl
∏ n−1
l=1 zlogqal
f (∞)
q (z)n,
where the basic hypergeometric series nϕn−1 (a1,...,a n−1, 0;b1,...,b n−1;q,z ) (see Deﬁnition 2.1) is a solution
of (5) around the origin, and f (∞)
q (z,λ )1,...,f (∞)
q (z,λ )n−1,f (∞)
q (z)n is a fundamental system of meromorphic
solutions of (5) around inﬁnity (see Proposition 2.20). Here “ai and ’ai/a i mean the corresponding i-th terms
ai and ai/a i are skipped.
2
At the end of this article, we show that Theorem 1.1 and Theore m 1.2 recover the corresponding Stokes
matrices and connection formula in the diﬀerential case as q → 1. See Section 4.
