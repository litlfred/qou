---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-015-30-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 30
pages: 30-33
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
We further elucidate the situation in Definition 9.1. For finiteN, each ˜R(n) is a pre-YBO modulo
factors of degreeℏ n+1, forn= 0,...,N−1. However, when considering ˜R(N), it is assumed in the
definition that this operator satisfies the YBE exactly, in the sense that the YBE is satisfied even
without quotienting moduloℏ N+1. A similar assumption is made forR −1
(n). Moreover, the operators
˜R(N) and ˜R−1
(N) are inverse to each others when the condition ˆℏ=ℏ −1 is imposed. WhenN=∞,
we have that ˜R(n) and ˜R−1
(n) are pre-YBOs for eachn∈N, but the full power series satisfy the YBE
exactly, and they are inverse to each other. When deformations are integrable, we can automatically
find such ˜R(∞) and ˜R−1
(∞). We will provide two examples of finite order Laurent deformations that
correspond to the Jones and Alexander polynomials below. They are both Laurent deformations of
order 2, and we will see that while the first order deformations are only pre-YBOs, hence they are
invertible only modulo degrees of order 2, the second order deformations satisfy the YBE exactly,
and are invertible exactly.
Lemma 9.2.Suppose that ˜R(n) andR −1
(n) are pre-YBOs, and thatϕ n+1 and ˆϕn+1 satisfy Equa-
tion 18:
δ2
YBϕn+1 + Θn+1 = 0 andδ 2
YB ˆϕn+1 + Θn+1 = 0
respectively, for alln= 1,...,n, and that ˜R(n+1) andR−1
(n+1) are inverses to each other inV, then
( ˜R(n+1), ˜R−1
(n+1))is a Laurent deformation of(ϕ 0, ˆϕ0).
Proof.In the proof of the first statement of Theorem 8.1, it was not assumed that ˜R(n) is invertible
for anyn, and that Equation (18) is sufficient for ˜R(n) to be a YBO. This also holds forR −1
(n) as
well. □
Definition 9.3.Let ( ˜R(N), ˜R−1
(N)) be a Laurent deformation of (ϕ0, ˆϕ0) as in Definition 9.1. If ˜R(N)
and ˜R−1
(N) are both enhanced YBO, then we call the pair ( ˜R(N), ˜R−1
(N)) aLaurent enhanced YBO
(LEYBO).
Lemma 9.4.Let( ˜R(N), ˜R−1
(N))be a Laurent enhanced YBO. Letb m be anm-braid whose closure
represents a knotK. (end replace, belowDis replaced byb m) LetΨ ( ˜R(N), ˜R−1
(N))(bm)be the braid
representation defined from( ˜R(N), ˜R−1
(N)). Let
Φ( ˜R(N), ˜R−1
(N))(bm) =
X
(i,j1,...,jm)∈Γmn
α−w(bm)β−m Tr(Ψ( ˜R(N), ˜R−1
(N))(bm)(µj1⊗···⊗µ jm))
be as in Theorem 8.3. ThenΦ ( ˜R(N), ˜R−1
(N))(bm)defines a knot invariantΦ ( ˜R(N), ˜R−1
(N))(K), called a
quantum cocycle invariant from LEYBO.
Proof.The proof of Theorem 8.3 applies without assumption of invertibility of ˜R(n) and ˜R−1
(n) for
n<N, and only requires invertibility of ˜R(N) and ˜R−1
(N).□
Theorem 9.5.The Jones polynomial is a quantum cocycle invariant from LEYBO. Moreover,
letDbe a closed braid diagram of the knotKonnstrings, withm + positive andm − negative
crossings. Then, we have
(ℏ+ℏ −1)J(K) =ℏ m+−m−−nΦ( ˜R(N), ˜R−1
(N))(K)
for some ˜R(N) and ˜R−1
(N).
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 31
Proof.We explicitly construct ˜R(N) and ˜R−1
(N).
Recall (e.g. [16]) that the Jones polynomial (up to a factor oft
1
2 +t− 1
2 ) can be obtained as a
trace invariant of an appropriate EYBO (J,µ,1,1). We use this EYBO and rewrite it using the
formalism developed in this article. By settingt
1
2 =ℏwe have
J=


t
1
2 0 0 0
0 0t0
0t t
1
2−t
3
2 0
0 0 0t
1
2

 =ℏ


1 0 0 0
0 0ℏ0
0ℏ1−ℏ 2 0
0 0 0 1

.
This form ofJcan be rewritten as
J=J 0 +ℏJ 1 +ℏ 2J2,
where
J0 =


1 0 0 0
0 0 0 0
0 0 1 0
0 0 0 1

, J 1 =


0 0 0 0
0 0 1 0
0 1 0 0
0 0 0 0

, J 2 =


0 0 0 0
0 0 0 0
0 0−1 0
0 0 0 0

.
By computer calculations, we findJ0 is a pre-YBO, i.e. it satisfies the YBE but it is not invertible,
andJ 1 is a YB 2-cocycle. However, since the YBE forJholds exactly, as opposed as being up to
higher orders ofℏthan 2, it means that the deformation is integrable by adding zero maps of all
orders.
To find an inverse, we proceed analogously by using the matrix
J−1 =


1 0 0 0
0 1−ℏ −2 ℏ−1 0
0ℏ −1 0 0
0 0 0 1

,
and decompose this in terms ofℏ −1, denoting the matrices by ˆJi,i= 0,1,2. The same discussion
as forJapplies here too, mutatis mutandis.
Next, we have
µ=
"
t− 1
2 0
0t
1
2
#
=ℏ−1
1 0
0ℏ 2

.
It follows that
ℏµ=µ 0 +µ 2 =
1 0
0 0

+ℏ−1
0 0
0ℏ 2

.
To show that
(ℏ+ℏ −1)J(K) =ℏ m+−m−−nΦ( ˜R(N), ˜R−1
(N))(K),
we setϕ= P2
i=0 ℏiJi and ˆϕ= P2
i=0 ℏi ˆJi. Then, Φ ( ˜R(N), ˜R−1
(N))(K) differs from the Jones polynomial
J(K) by only a multiplying power ofℏ, which was initially factored out when constructing the
matricesJandJ −1. SinceJneeds to be multiplied byℏandJ −1 byℏ−1, it follows thatℏ m+−m−
corrects this deficiency and givesJ(K) as needed. Lastly, eachµcontributes with a factorℏ −1,
and there arenof them sinceKis obtained as the closure of a braid onnstrings.□
32 MASAHICO SAITO AND EMANUELE ZAPPALA
Although the trace is taken only in the factors 2,...,mleaving the first factor in the following
theorem, so that it is not fully LEYBO as defined, it provides a similar description for the Alexander
polynomial, and we make the following statement.
Theorem 9.6.The Alexander polynomial∆(K)of a knotKis a quantum cocycle invariant in
the following sense. LetKbe represented by a closed braid form of anm-braidb m. Assume that
bm hasm + positive andm − negative crossings. Then, we have
∆(K)·1=ℏ −m++m−+m−1 Tr2,...,m(Ψ( ˜R(N), ˜R−1
(N))(bm)(1⊗µ ⊗(m−1))),
for someϕand its inverse ˆϕ, whereTr 2,...,m is the trace over the2,3,...,mfactors ofV.
Proof.The proof is analogous to the case of the Jones polynomial above. We have, from [16], the
equality
∆(K)·1= Tr 2,...,m(ψ ˆ∆(bm)(1⊗µ ⊗(m−1))),
whereψ ˆ∆(bm) is the operator obtained fromb m by replacing crossings with the matrix
ˆ∆ =


t− 1
2 0 0 0
0 0 1 0
0 1t − 1
2−t
1
2 0
0 0 0−t
1
2

,
and
µ=
"
t
1
2 0
0−t
1
2
#
=ℏ
1 0
0−1

.
We factor out a term ofℏ −1 =t− 1
2 from the matrix ˆ∆ to obtain
∆ =


1 0 0 0
0 0ℏ0
0ℏ1−ℏ 2 0
0 0 0−ℏ 2

.
Its inverse is given by
∆−1 =


1 0 0 0
0 1−ℏ −2 ℏ−1 0
0ℏ −1 0 0
0 0 0−ℏ −2

.
In this case one needs to have ∆ i withi= 0,1,2. As in the case of the Jones polynomial,
computer calculations show that ∆ 0 is a pre-YBO and ∆ 1 is a YB 2-cocycle.
Sinceℏ −1 is factored out for ∆, andℏis factored out for ∆ −1 (i.e.,ℏ∆ −1 = ˜∆−1), we find
that the generalized quantum cocycle invariant needs to be multiplied byℏ −m++m−
to give the
Alexander polynomial. The mapµintroduces a factor ofℏ m−1, one for each copy ofµ. The details
are analogous to the case of the Jones polynomial in Theorem 9.5, except the fact that the trace is
a partial trace on the entries 2,...,mofV ⊗m.□
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 33
