---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-047-0-otherwise-using-hölder-and-bienaymé-chebyshev
section_title: "Otherwise, using Hölder and Bienaymé-Chebyshev inequalities,"
section_number: 0
pages: 37-39
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
|Cov(A+
i,n,Aj,n)|≤
√
E[(Ai,n)2 1|Ai,n|≥Ln] E[(Aj,n)2 1|Ai,n|≥Ln]
≤
√
E[(Ai,n)2+δ]
2
2+δ P[|Ai,n|≥ Ln]
2δ
2+δ E[(Aj,n)2+δ]
2
2+δ
≤A2
( A
Ln
)δ
.
Similarly,
|Cov(A+
i,n,A +
j,n)|≤ E[|A+
i,nA+
j,n|] + E[|A+
i,n|] E[|A+
j,n|]
≤A2
(( A
Ln
)δ
+
( A
Ln
)2+2δ)
,
hence, assuming that the level of truncationLn is larger thanA,
|Var(Sn)−− Var(Sn)|
Var(Sn) ≤ NnDn
Var(Sn) 3A2
( A
Ln
)δ
.
Let us now place ourselves in the setting of Hypothesis (U1); we set
Vn = Var(Sn)
NnDn
(Nn
Dn
)1/3 1
(Nn)2/(2+δ).
Suppose thatLn =Kn (Nn)
1
2+δ, withKn going to inﬁnity. We then havea≤ A2+δ
(Kn)2+δ, and on the other
hand,
⏐⏐⏐⏐
Var(S−
n )
Var(Sn)− 1
⏐⏐⏐⏐≤ 3A2+δ
( NnDn
Var(Sn)
1
(Nn)δ/(2+δ)
1
(Kn)δ
)
≤ 3A2+δ
( 1
Vn (Dn)1/3 (Nn)2/3 (Kn)δ
)
→ 0
since by hypothesis,limn→∞ 1
Vn
= 0. So,
38 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
c≤ 3A2+δ
√
2πe
1
Vn (Dn)1/3 (Nn)2/3 (Kn)δ≤ 3A2+δ
√
2πe
1
Vn (Kn)δ.
Now, the sequence(S−
n/Ln)n∈N is a sequence of sums of centered random variables all bounded by1, and
to apply Corollary 30 to this sequence, we need
lim
n→∞
Var(S−
n )
NnDn
(Nn
Dn
)1/3 1
(Ln)2 = +∞.
However, the previous computation shows that one can replaceVar(Sn) by Var(S−
n ) in this expression
without changing the asymptotic behavior, so
lim
n→∞
Var(S−
n )
NnDn
(Nn
Dn
)1/3 1
(Ln)2 = lim
n→∞
Vn
(Kn)2,
which is +∞ if (Kn)2 is not growing too fast to +∞ (in comparison to the sequenceVn). Then, by
Corollary 30,
b =dKol(Y−
n ,NR(0, 1))≤ 77 (Kn)3
(Vn)3/2
for n large enough. SetKn =B(Vn)
3
2(5+δ). Then,
dKol(Yn,NR(0, 1))≤a +b +c≤
(A2+δ
B2+δ + 77B3 +o(1)
)( 1
Vn
) 3(2+δ)
2(5+δ)
≤
(( 231
2 +δ
) 2+δ
5+δ
+ 77
(2 +δ
231
) 3
5+δ
)(A2
Vn
) 3(2+δ)
2(5+δ)
for n large enough, and by choosingB in an optimal way. The term in parenthesis is maximal when
δ = 229, and is then equal to78. This ends the proof of (U1), and one gets a better constant smaller
than 39 when δ = 5.
Under the Hypothesis (U2), we set
Wn = Var(Sn)
NnDn
(Nn
Dn
)ε 1
(Nn)2/(2+δ).
In order to prove the convergence in lawYn ⇀NR(0, 1), it suﬃces to have:
• Sn− S−
n = S+
n that converges in probability to 0. This happens as soon as the level Ln is
Kn (Nn)1/(2+δ) with Kn→ +∞.
• |Var(Sn)−Var(S−
n )|
Var(Sn) → 0. WithLn =Kn (Nn)1/(2+δ), the previous computations show that this quantity
is a
O
( 1
Wn (Nn)1−ε (Dn)ε (Kn)δ
)
,
which goes to0.
• and by Theorem 32,
Var(Sn)
NnDn
(Nn
Dn
)ε 1
(Ln)2→ +∞.
This follows from the Hypothesis (U2) ifKn is chosen to grow suﬃciently slow.
Thus, the second part of Theorem 39 is proven. ⊓ ⊔
Example 41.Let (Xi)i∈[ [1,N] ]be a centered Gaussian vector withE[(Xi)2] = 1 for anyi, and with the
covariance matrix(Cov(Xi,Xj))1≤i,j≤N that is sparse in the following sense: for anyi, the set of indices
Mod-φ convergence, II: Estimates on the speed of convergence 39
j such thatCov(Xi,Xj)⁄= 0 has cardinality smaller thanD. We setAi = exp(Xi); the random variables
Ai follow thelog-normal distributionof density
1√
2π
1
u1+ logu
2
1u>0du,
and they have moments of all order:E[(Ai)k] = E[ekXi] = e
k2
2 .
Fig. 9 The density of the log-normal distribution.
The variablesAi have the same dependency graph as the variablesXi. Moreover, ifρij = Cov(Xi,Xj),
then the covariance of two variablesAi andAj is e(eρij− 1). Using moments of order2 +δ, we see that if
YN =
∑N
i=1(Ai− e
1
2 )√
e∑
1≤i,j≤N(eρij− 1)
VN,δ =
e∑
1≤i,j≤N(eρij− 1)
ND
N
1
3− 2
2+δ
D
1
3
→ +∞,
then dKol(YN,NR(0, 1))≤ 78
(
eδ+2
VN,δ
) 3(δ+2)
2(δ+5)
for N large enough.
To make this result more explicit, let us consider the following dependency structure for the Gaussian
vectorX = (Xi)i∈[ [1,N] ]:
Cov(X) =


1 ∗ ···∗
∗ 1 ... ...
... ... ...∗
∗··· ∗ 1


,
where the non-diagonal terms∗ are all smaller thanρ
D in absolute value, and with less thanD non-zero
terms on each row or column. Whenρ∈ [0, 1), the matrix is diagonally dominant, hence positive-deﬁnite,
so there exists indeed a Gaussian vectorX with these covariances. We then have
VN,δ≥ e (1−D(e
ρ
D− 1))N
1
3− 2
2+δ
D
4
3
,
so if 1≪D≪N
1
4−ε, then one can apply Theorem 39 to get
dKol(YN,NR(0, 1))≤ 78
(
e
3
2ε−1
1−ρ
)3
