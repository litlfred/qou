---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-007-3-asymptotic-second-order-freeness-for-unitary-r
section_title: "Asymptotic second order freeness for unitary random matrices"
section_number: 3
pages: 10-30
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
matrices
Notation 3.1. Suppose ǫ : [2 l] → {− 1, 1} is such that ∑ 2l
i=1 ǫi = 0.
We write ǫ−1(1) = {p1, p2, . . . , pl} and ǫ−1(−1) = {q1, q2, . . . , ql}, with
p1 < p 2 < · · · < p l and q1 < q 2 < · · · < q l. Let S(ǫ)
2l be the permutations
π in S2l such that π takes {p1, . . . , pl} onto {q1, . . . , ql} and vice versa.
Given a π in S(ǫ)
2l we may extract a pair of permutations απ and βπ in
Sl from the equations
(6) π(pαπ(k)) = qk and π(qk) = pβπ(k)
and conversely: ( α, β) ↦→πα,β. Thus we have a bijection of sets between
S(ǫ)
2l and Sl × Sl.
Given π ∈ S(ǫ)
2l we let ˜π ∈ Sl be deﬁned by
π2(pk) = p˜π(k)
Note that ˜πα,β = βα −1.
Also we have
#(π) = #(˜π),
and thus
|π| = |˜π| + l.
Lemma 3.2. Fix l ∈ N and γ ∈ S2l. Let, for N ∈ N, U be a Haar
distributed unitary N × N random matrix. Let ǫ : [2l] → {−1, 1} such
that ∑ 2l
i=1 ǫi = 0 . Then we have for all 1 ≤ r1, . . . , r2l, s1, . . . , s2l ≤ N
that
(7) E
(
U ǫ1
r1,sγ(1) · · · U ǫ2l
r2l,sγ(2l)
)
=
∑
π∈S(ǫ)
2l
2l∏
k=1
δrk,sγ(π(k)) Wg(N, ˜π).
Proof. Let ik, i′
k, jk, j′
k (1 ≤ k ≤ l) be such that
E
(
U ǫ1
r1,sγ(1) · · · U ǫ2l
r2l,sγ(2l)
)
= E
(
Ui′
1,j′
1 · · · Ui′
l,j′
l
U −1
j1,i1 · · · U −1
jl,il
)
,
FLUCTUATIONS OF UNITARY RANDOM MATRICES 11
i.e. let ǫ−1(1) = {p1, . . . , pl} with p1 < · · · < p l and ǫ−1(−1) =
{q1, . . . , ql} with q1 < · · · < q l and i′
k = rpk, j′
k = sγ(pk), ik = sγ(qk), and
jk = rqk.
Now suppose that α and β in Sl and π ∈ S(ǫ)
2l is as in equation (6)
above.
Thus we have
ik = sγ(qk) = sγ(π(pα(k))), and i′
α(k) = rpα(k),
and
j′
β(k) = sγ(pβ(k)) = sγ(π(qk)), and jk = rqk
which shows that
ik = i′
α(k) ⇐ ⇒ rpα(k) = sγ(π(pα(k)))
and
jk = j′
β(k) ⇐ ⇒ rqk = sγ(π(qk)).
Thus
l∏
k=1
δik,i′
α(k)
δjk,j′
β(k)
=
2l∏
k=1
δrk,sγ(π(k)).
Hence
E
(
U ǫ1
r1,sγ(1) · · · U ǫ2l
r2l,sγ(2l)
)
= E
(
Ui′
1,j′
1 · · · Ui′
l,j′
l
U −1
j1,i1 · · · U −1
jl,il
)
=
∑
α,β∈Sn
δi1i′
α(1)
· · · δini′
α(n)
δj1j′
β(1)
· · · δjnj′
β(n)
Wg(βα −1)
=
∑
π∈S(ǫ)
2l
2l∏
k=1
δrk,sγ(π(k)) Wg(˜π).
We can now address the question how to calculate expectations of
products of traces of our matrices. The following result is exact fo r
each N; later on we will look on its asymptotic version.
Note that the notation Tr π(D1, . . . , Dn) for π ∈ Sn is deﬁned in the
usual multiplicative way, as was done in Notation 2.6 for ϕ1.
We shall need the following standard lemma. For D1, . . . , Dp ∈
MN (A) let the entries of Di be ( D(i)
r,s).
Lemma 3.3. Let π ∈ Sn and D1, . . . , Dn ∈ MN (A). Then
Trπ(D1, D2, . . . , Dn) =
∑
j1,j2,...,jn
D(1)
j1,jπ(1)
D(2)
j2,jπ(2)
· · · D(n)
jn,jπ(n)
12 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
Given m1, . . . , mk, let γm1,...,mk be the permutation of [ m1 + · · ·+ mk]
with k cycles where the ith cycle is (m1+· · ·+mi−1+1, . . . , m1+· · ·+mi).
Proposition 3.4. Fix m1, . . . , mk ∈ N such that m1 + · · · + mk = 2 l
is even. Let, for ﬁxed N ∈ N, U be a Haar distributed unitary N × N-
random matrix and D1, . . . , D2l be N × N-random matrices which are
independent from U. Let ǫ : [2 l] → {− 1, 1} with ∑ 2l
i=1 ǫi = 0 . Put
γ = γm1,...,mk. Then
(8) E
(
Tr(D1U ǫ1 · · · Dm1U ǫm1 )
× Tr(Dm1+1U ǫm1+1 · · · Dm1+m2U ǫm1+m2 ) × · · ·
× Tr(Dm1+···+mk−1+1U ǫm1+···+mk−1+1 · · · Dm1+···+mkU ǫm1+···+mk )
)
=
∑
π∈S(ǫ)
2l
Wg(N, ˜π) · E
(
Trγπ −1(D1, . . . , D2l)
)
.
Proof. Summations over r’s and s’s in the following formulas are from
1 to N.
E
(
Tr(D1U ǫ1 · · · Dm1U ǫm1 )Tr(Dm1+1U ǫm1 +1 · · · Dm1+m2U ǫm1 +m2 )
· · · × Tr(Dm1+···+mk−1+1U ǫm1+···+mk−1+1 · · · Dm1+···+mkU ǫm1 +···+mk )
)
=
∑
r1,...,r2l
s1,...,s2l
E
(
U ǫ1
s1,rγ(1) · · · U ǫ2l
s2l,rγ(2l)
)
· E
(
D(1)
r1,s1 · · · D(2l)
r2l,s2l
)
=
∑
r1,...,r2l
s1,...,s2l
∑
π∈S(ǫ)
2l
2l∏
k=1
δsk,rγ(π(k)) Wg(˜π) · E
(
D(1)
r1,s1 · · · D(2l)
r2l,s2l
)
=
∑
π∈S(ǫ)
2l
Wg(˜π)
∑
r1,...,r2l
s1,...,s2l
2l∏
k=1
δsk,rγ(π(k)) · E
(
D(1)
r1,s1 · · · D(2l)
r2l,s2l
)
=
∑
π∈S(ǫ)
2l
Wg(˜π)
∑
r1,...,r2l
E
(
D(1)
r1,rγ(π(1)) · · ·D(2l)
r2l,rγ(π(2l))
)
=
∑
π∈S(ǫ)
2l
Wg(˜π)E
(
Trγπ (D1, . . . , D2l)
)
=
∑
π∈S(ǫ)
2l
Wg(˜π)E
(
Trγπ −1(D1, . . . , D2l)
)
In the last equality we used that Wg(˜π) depends only on the conjugacy
class of π.
FLUCTUATIONS OF UNITARY RANDOM MATRICES 13
Motivated by the result of Voiculescu [Voi1, Voi2] that Haar dis-
tributed unitary random matrices and constant matrices are asym p-
totically free, we want to investigate now the corresponding quest ion
for second order freeness. It will turn out that one can replace t he
constant matrices by another ensemble of random matrices, as lon g as
those are independent from the unitary random matrices. Of cour se,
we have to assume that the second ensemble has some asymptotic lim it
distribution. This is formalized in the following deﬁnition. Note that
we make a quite strong requirement on the vanishing of the higher
order cumulants. This is however in accordance with the observatio n
that in many cases the unnormalized traces converge to Gaussian r an-
dom variables. Of course, if we have a non-probabilistic ensemble of
constant matrices, then the only requirement is the convergence of k 1;
all other cumulants are automatically zero.
Deﬁnition 3.5. 1) Let {A1, . . . , As}N be a sequence of N × N-random
matrices. We say that they have a second order limit distribution if
there exists a second order non-commutative probability space ( A, ϕ1,
ϕ2) and a1, . . . , as ∈ A such that for all polynomials p1, p2, . . . in s
non-commuting indeterminates we have
(9) lim
N →∞
k1
(
tr(p1(A1, . . . , As)
))
= ϕ1
(
p1(a1, . . . , as)
)
,
(10) lim
N →∞
k2
(
Tr(p1(A1, . . . , As)), Tr(p2(A1, . . . , As))
)
= ϕ2
(
p1(a1, . . . , as), p2(a1, . . . , as)
)
,
and, for r ≥ 3,
(11) lim
N →∞
kr
(
Tr(p1(A1, . . . , As)), . . . ,Tr(pr(A1, . . . , As))
)
= 0.
2) We say that two sequences of N ×N-random matrices, {A1, . . . , As}N
and {B1, . . . , Bt}N , are asymptotically free of second order if the se-
quence {A1, . . . , As, B1, . . . , Bt}N has a second order limit distribution,
given by ( A, ϕ1, ϕ2) and a1, . . . , as, b1, . . . , bt ∈ A , and if the unital
algebras
A1 := alg(1, a1, . . . , as) and A2 := alg(1, b1, . . . , bt)
are free with respect to ( ϕ1, ϕ2).
Notation 3.6. Fix m, n ∈ N and let ǫ : [1 , m + n] → {− 1, +1}. We
deﬁned S(ǫ)
m+n in Notation 3.1, for the case where ∑ m+n
k=1 ǫ(k) = 0, as
those permutations in Sm+n for which ǫ alternates cyclically between
−1 and +1 on all cycles. Note that this deﬁnition also makes sense
14 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
in the case where the sum of the ǫ’s is not equal to zero, then we just
have S(ǫ)
m+n = ∅. Let ǫ1 and ǫ2 be the restrictions of ǫ to [1 , m] and to
[m + 1, m + n], respectively. Then we put
S(ǫ)
N C(m, n) := S(ǫ)
m+n ∩ SN C(m, n)
and
N C(ǫ1)(m) := S(ǫ1)
m ∩ N C(m), N C (ǫ2)(n) := S(ǫ2)
n ∩ N C(n).
Theorem 3.7. Let {U}N be a sequence of Haar distributed unitary
N × N-random matrices and {A1, . . . , As}N a sequence of N × N-
random matrices which has a second order limit distribution , given by
(A, ϕ1, ϕ2) and a1, . . . , as ∈ A . Furthermore, assume that {U}N and
{A1, . . . , As}N are independent. Fix now m, n ∈ N and consider poly-
nomials p1, . . . , pm+n in s non-commuting indeterminates. If we put
(for i = 1, . . . , m+ n)
Di := pi(A1, . . . , As) and di := pi(a1, . . . , as),
then we have for all ǫ(1), . . . , ǫ(m + n) ∈ {−1, +1} that
lim
N →∞
k2
(
Tr(D1U ǫ1 · · · DmU ǫm), Tr(Dm+1U ǫm+1 · · · Dm+nU ǫm+n)
)
(12)
=
∑
π∈S(ǫ)
N C(m,n)
µ(˜π) · ϕ1(γm,nπ−1)[d1, . . . , dm+n]
+
∑
π1∈N C(ǫ1)(m)
π2∈N C(ǫ2)(n)
(
µ2(˜π1, ˜π2) · ϕ1(γmπ−1
1 × γnπ−1
2 )[d1, . . . , dm+n]
+ µ(˜π1 × ˜π2) · ϕ2(γmπ−1
1 , γnπ−1
2 )[d1, . . . , dm+n]
)
.
Note that in the case where the sum of the ǫ’s is diﬀerent from zero
this just states that the limit of k 2 vanishes.
Proof. For notational convenience, we will sometimes write m + n = 2l
in the following, and also use γ := γm,n.
We have
k2
(
Tr(D1U ǫ1 · · · DmU ǫm), Tr(Dm+1U ǫm+1 · · · D2lU ǫ2l)
)
= E
(
Tr(D1U ǫ1 · · ·DmU ǫm)Tr(Dm+1U ǫm+1 · · · D2lU ǫ2l)
)
− E
(
Tr(D1U ǫ1 · · · DmU ǫm)
)
· E
(
Tr(Dm+1U ǫm+1 · · · D2lU ǫ2l)
)
=
∑
π∈S(ǫ)
2l
Wg(˜π) · E
(
Trγπ −1(D1, . . . , D2l)
)
FLUCTUATIONS OF UNITARY RANDOM MATRICES 15
−
∑
π1∈S(ǫ1)
m
π2∈S(ǫ2)
n
Wg(˜π1)Wg(˜π2) · E
(
Trγmπ−1
1
(D1, . . . , Dm)
)
· E
(
Trγnπ−1
2
(Dm+1, . . . , D2l)
)
=
∑
π∈S(ǫ)
2l
π connected
Wg(˜π) · E
(
Trγπ −1(D1, . . . , D2l)
)
+
∑
π1∈S(ǫ1)
m
π2∈S(ǫ2)
n
(
Wg(˜π1 × ˜π2) · E
(
Trγmπ−1
1 ×γnπ−1
2
(D1, . . . , D2l)
)
− Wg(˜π1)Wg(˜π2)E
(
Trγmπ−1
1
(D1, . . . , Dm)
)
· E
(
Trγnπ−1
2
(Dm+1, . . . , D2l)
) )
Note that if either m or n is odd then the last two terms are zero,
which is consistent with equation (12), as in this case N C(ǫ1)(m) and
N C(ǫ2)(n) are empty. So for the remainder of the proof we shall assume
that m and n are even.
The leading order in the ﬁrst summand for a connected π is given
by
µ(˜π)N −(|˜π|+(m+n)/2) · N #(γπ −1) · E
(
trγπ −1(D1, . . . , Dm+n)
)
=
= N m+n−|π|−|γπ −1| · µ(˜π) · E
(
trγπ −1(D1, . . . , Dm+n)
)
.
Recall that, for a connected π, we always have
m + n − |π| − |γπ −1| ≤ 0,
and equality is exactly achieved in the case where π is annular non-
crossing. Thus, in the limit N → ∞ the ﬁrst sum gives the contribution
∑
π∈S(ǫ)
N C(m,n)
µ(˜π) · ϕ1(γπ −1)[d1, . . . , dm+n].
We can rewrite the second sum as
∑
π1∈S(ǫ1)
m
π2∈S(ǫ2)
n
{
Wg(˜π1 × ˜π2) − Wg(˜π1)Wg(˜π2)
}
(13)
× E
(
Trγmπ−1
1 ×γnπ−1
2
(D1, . . . , Dm+n)
)
+ Wg(˜π1)Wg(˜π2)
{
E
(
Trγmπ−1
1 ×γnπ−1
2
(D1, . . . , Dm+n)
)
− E
(
Trγmπ−1
1
(D1, . . . , Dm)
)
· E
(
Trγnπ−1
2
(Dm+1, . . . , Dm+n)
) }
16 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
For a disconnected π1 × π2 the leading orders in N of all relevant
terms are given as follows: Wg(˜π1 × ˜π2) and Wg(˜π1)Wg(˜π2) both have
leading order (note that µ is multiplicative)
µ(˜π1)µ(˜π2)N −(m+n)+#(π1)+#(π2);
E
(
Trγmπ−1
1
(D1, . . . , Dm)
)
· E
(
Trγnπ−1
2
(Dm+1, . . . , Dm+n)
)
and
E
(
Trγmπ−1
1 ×γnπ−1
2
(D1, . . . , Dm+n)
)
are both asymptotic to
ϕ1(γmπ−1
1 × γnπ−1
2 )[d1, . . . , dm+n]N #(γmπ−1
1 )+#(γnπ−1
2 );
Wg(˜π1 × ˜π2) − Wg(˜π1)Wg(˜π2) has leading order
µ2(˜π1, ˜π2) · N −(m+n)+#(π1)+#(π2)−2.
Now
− (m + n) + #(π1) + #(π2) − 2 + #(γmπ−1
1 ) + #(γnπ−1
2 )
= −(m + 1 − #(π1) − #(γmπ−1
1 )) − (n + 1 − #(π2) − #(γnπ−1
2 )) ≤ 0
with equality only if both π1 ∈ N C(ǫ1)(m) and π2 ∈ N C(ǫ2)(n).
Thus
lim
N
{
Wg(˜π1 × ˜π2) − Wg(˜π1)Wg(˜π2)
}
E(Trγm,n(π1×π2)−1(D1, . . . , Dm+n)
=









µ2(˜π1, ˜π2)ϕ1(γmπ−1
1 × γnπ−1
2 )[d1, . . . , dm+n]





π1 ∈ N C(ǫ1)(m)
and
π2 ∈ N C(ǫ2)(n)
0 otherwise
To deal with the second term of the second sum (13) we will use the
following notation. Let the cycles of γmπ−1
1 be c1 · · · cr and the cycles
of γnπ−1
2 be cr+1 · · · cr+s. Let ai = Trci(D1, . . . Dm) for 1 ≤ i ≤ r and
bj = Trcr+j(Dm+1, . . . , Dm+n) for 1 ≤ j ≤ s. Then
k2(Trγmπ−1
1
(D1, . . . , Dm), Trγnπ−1
2
(Dm+1, . . . , Dm+n)
= k 2(a1 · · · ar, b1 · · · bs)
So let us ﬁnd for which π1 ∈ S(ǫ1)
m , π2 ∈ S(ǫ2)
n , and τ ∈ P (r + s) we
have a non-zero limit of
(14) Wg(˜ π1) Wg(˜π2) kτ (a1, . . . , ar, b1, . . . , bs)
As noted above the order of Wg(˜ π1) Wg(˜π2) is N −(m+n)+#(π1)+#(π2).
By equation (1) and the deﬁnition of a second order limit distribution,
FLUCTUATIONS OF UNITARY RANDOM MATRICES 17
kτ (a1, . . . , ar, b1, . . . , bs) is O(N c) where c is the number of singletons
of τ . Thus the order of (14) is
−(m + n) + #(π1) + #(π2) + c
= −
(
m + 1 − #(π1) − #(γmπ−1
1 )
)
−
(
n + 1 − #(π2) − #(γnπ−1
2 )
)
+ c + 2 − (r + s)
Hence (14) will vanish unless three conditions are satisﬁed: we must
have that π1 and π2 are non-crossing and c = r + s − 2, i.e. τ has one
pair and the rest of its blocks are singletons.
Thus
lim
N
∑
π1∈S(ǫ1)
m ,π2∈S(ǫ2)
n
Wg(˜π1)Wg(˜π2)
× k2
(
Trγmπ−1
1
(D1, . . . , Dm), Trγnπ−1
2
(Dm+1, . . . , D2l)
)
=
∑
π1∈N C(ǫ1)(m)
π2∈N C(ǫ2)(n)
µ(˜π1)µ(˜π2)
× lim
N
N r+s−2
∑
τ ∈P(r+s)
kτ (a1, . . . , ar, b1, . . . , bs)
where the τ ’s in the sum have one pair and the remainder are singletons
and τ ∨ 1r,s = 1 r+s.
So the remainder of the proof is to show that
lim
N
N r+s−2 ∑
τ ∈P(r+s)
kτ (a1, . . . , ar, b1, . . . , bs)
= ϕ2(γmπ−1
1 , γnπ−1
2 )[d1, . . . , dm+n]
where the sum runs over τ ’s as above.
Let τ ∈ P (r + s) be as above with pair ( i, j) where 1 ≤ i ≤ r and
1 ≤ j ≤ s and all other blocks singletons. Then
kτ (a1, . . . , ar, b1, . . . , bs)
= k 1(a1) · · · ˆk1(ai) · · · k1(ar)k1(b1) · · · ˆk1(bj) · · ·k1(bs)k2(ai, bj)
where the hatted elements are deleted. So after multiplying by N r+s−2
and taking a limit we get (after omitting the arguments d1, . . . , dm+n
which are the same for each factor)
ϕ1(c1) · · · ˆϕ1(ci) · · · ϕ1(cr)ϕ1(cr+1) · · · ˆϕ1(cr+j) · · · ϕ1(cr+s)ϕ2(ci, cr+j)
18 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
Now summing over all τ , which is equivalent to summing over all i and
j, we get via the derivation property of ϕ2 (see equations (4) and (5))
ϕ2(γmπ−1
1 , γnπ−1
2 )[d1, . . . , dm+n]
as required.
Remark 3.8. When all the D’s are equal to 1, equation (12) implies
the following well known result of Diaconis and Shahshahani [DS]: for
integers r and s
(15) lim
N
k2
(
Tr(U r), Tr(U s)
)
=
{
0 r ⁄= −s
|r| r = −s
Indeed let m = |r| and for 1 ≤ i ≤ m, let ǫi = sgn( r), where sgn( r)
denotes the sign of r; let n = |s| and for m + 1 ≤ i ≤ m + n, let
ǫi = sgn(s). Then ǫ1 + · · ·+ ǫm+n = r + s. So if r + s ⁄= 0 then equation
(12) says that
lim
n
k2
(
Tr(U r), Tr(U s)
)
= 0
Suppose that r + s = 0. The second term on the right hand side of (12)
is zero since both N C(ǫ1)(m) and N C(ǫ2)(n) are empty. For the ﬁrst
term in (12), note that the only elements of S(ǫ)
N C(m, n) which connect
in this alternating way are pairings, where each block must contain on e
U and one U ∗. This forces m and n to be equal. In that case, we have
the freedom of pairing the ﬁrst U with any of the n U ∗’s. After this
choice is made, the rest is determined. Thus there are n possibilities for
such pairings. Since µ(˜π) is always 1 for a pairing we get the claimed
formula.
Let ǫ : [2 l] → {− 1, 1} be such that ∑ 2l
i=1 ǫi = 0. For π ∈ S(ǫ)
2l
let ˜π ∈ Sl be as in 3.1. A π-invariant partition A of [2 l] gives ˜A,
a ˜π-invariant partition of [ l] as follows. For each block V of A let
˜V = {k | pk ∈ V }, where we have used the notation of 3.1. Also each
˜π-invariant partition of [ l] comes from a unique π-invariant partition
of [2 l].
Let M¨ ob be the M¨ obius function on the partially ordered set of par-
titions of [ l] ordered by inclusion. Let π ∈ Sl and A be a π-invariant
partition of [ l]. In [C, §2.3] Collins denotes the relative cumulant by
CΠ π,A(π, N ), which we will denote by Cπ,A. In our notation
Cπ,A =
∑
C∈[π,A]
C={V1,...,Vk}
M¨ ob(C, A)Wg(π|V1) · · ·Wg(π|Vk)
FLUCTUATIONS OF UNITARY RANDOM MATRICES 19
where π|Vi denotes the restriction of π to the invariant subset Vi and
where necessary we have identiﬁed π with the partition given by its
cycles. Conversely given A = {V1, . . . , Vk} a π-invariant partition of [ l]
we write Wg A(π) for Wg( π|V1) · · · Wg(π|Vk). Then by M¨ obius inversion
we have
WgA(π) =
∑
C∈[π,A]
Cπ,C
Remark 3.9. When π ∈ S(ǫ)
2l and A ∈ P (2l) is π-invariant the equation
above can also be written
(16) Wg A(˜π) =
∑
C∈[π,A]
C˜π, ˜C
In [C, Cor. 2.9] Collins showed that the order of C˜π, ˜C is at most
N −2l−#(π)+2#(C).
In the following we address the estimates for higher order cumulant s,
kr for r ≥ 3.
If D1, . . . , D2l are random matrices and π ∈ S2l is a permutation
with cycle structure π = π1 × · · · × πr with πi = ( πi,1, . . . , πi,l(i)) we
denote
kπ(D1, . . . , Dl) = k r
(
Tr(Dπ1,1 · · · Dπ1,l(1)), Tr(Dπ2,1 · · · Dπ2,l(2)), . . .
)
.
When A = {A1, . . . , Ak} is a π-invariant partition of [2l] we can write
π = π1 × · · · × πk where πi = π|Ai is a permutation of the set Ai. We
denote the multiplicative extension of k π by
kπ,A(D1, . . . , D2l) = k π1(D1, . . . , D2l) · · · kπk(D1, . . . , D2l)
M¨ obius inversion gives us that
E
(
Trπ(D1, . . . , D2l)
)
=
∑
A∈P(2l)
A π -inv.
kπ,A(D1, . . . , D2l)
where the sums run over all π-invariant partitions A in P(2l).
Theorem 3.10. Let {U}N be a sequence of Haar distributed unitary
N × N-random matrices and {A1, . . . , As}N a sequence of N × N-
random matrices which has a second order limit distribution , given by
(A, ϕ1, ϕ2) and a1, . . . , as ∈ A . Furthermore, assume that {U}N and
{A1, . . . , As}N are independent.
Suppose r > 1 and m1, · · · , mr are positive integers such that m1 +
· · · + mr = 2 l and ǫ1, . . . , ǫ2l ∈ {− 1, +1} are such that ∑ 2l
i=1 ǫi = 0 .
Consider polynomials p1, . . . , p2l in s non-commuting indeterminates.
For i = 1, . . . ,2l we set
20 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
Di := pi(A1, . . . , As)
and for 1 ≤ i ≤ r let
Xi = Tr
(
Dm1+···+mi−1+1U ǫ(m1+···+mi−1+1) · · · Dm1+···+miU ǫ(m1+···+mi))
Then
(17) k r
(
X1, . . . , Xr) =
∑
π∈S(ǫ)
n
∑
A,B
A∨B=1[1,2l]
C˜π, ˜A · kγπ −1,B(D1, . . . , D2l),
where the second sum runs over pairs (A, B) of partitions of [1, 2l]
such that A is π-invariant and B is γπ −1-invariant and furthermore
A ∨ B = 1 [1,2l].
Secondly, we have for r ≥ 3 that
(18) lim
N →∞
kr
(
X1, . . . , Xr
)
= 0.
If we have m1, . . . , mr for which m1 + · · · + mr is odd or ǫ1, . . . , ǫ2l for
which ∑ 2l
i=1 ǫi ⁄= 0 then kr(X1, . . . , Xr) = 0 .
Proof. In order to simplify the writing we shall write ⃗D for ( D1, . . . ,
D2l). Let Ii be the interval [ m1 + · · · + mi−1 + 1, m1 + · · · + mi] and for
any subset V ⊂ [r], IV = ∪j∈V Ij.
If C = {V1, . . . , Vk} is a partition of [ r] we let S(ǫ)
Vi the set of permu-
tations of IVi that take ǫ−1(1) ∩ IVi onto ǫ−1(−1) ∩ IVi. If these two sets
have diﬀerent cardinalities then S(ǫ)
Vi is empty. Let 1 C be the partition
{IV1, . . . , IVk} of [2 l]. Let γi be the cyclic permutation of Ii given by
(m1 + · · · + mi−1 + 1, . . . , m1 + · · · + mi)
With this notation
EC(X1, . . . , Xr) = E V1(X1, . . . , Xr) · · ·EVk (X1, . . . , Xr)
=
∑
π1∈S(ǫ)
V1
· · ·
∑
πk∈S(ǫ)
Vk
Wg(˜π1) · · ·Wg(˜πk)E
(
Trγ1π−1
1
( ⃗D)
)
· · · E
(
Trγkπ−1
k
( ⃗D)
)
=
∑
π∈S(ǫ)
2l
1cπ-inv.
Wg1C (˜π)EC
(
Trγπ −1( ⃗D)
)
=
∑
π∈S(ǫ)
2l
1cπ-inv.
∑
A∈[π,1C ]
C˜π, ˜A
∑
B∈P(2l)
B γπ −1-inv.
kγπ −1,B( ⃗D)
Thus
kr(X1, . . . , Xr)
FLUCTUATIONS OF UNITARY RANDOM MATRICES 21
=
∑
C∈P(r)
M¨ ob(C, 1r)EC(X1, . . . Xr)
=
∑
C∈P(r)
M¨ ob(C, 1r)
∑
π∈S(ǫ)
2l
1C π-inv.
∑
A∈[π,1C ]
C˜π, ˜A
∑
B∈P(2l)
B γπ −1-inv.
kγπ −1,B( ⃗D)
=
∑
π∈S(ǫ)
2l
∑
C∈P(r)
1C π-inv.
∑
A∈[π,1C ]
∑
B∈P(2l)
B γπ −1-inv.
M¨ ob(C, 1r) C˜π, ˜A kγπ −1,B( ⃗D)
=
∑
π∈S(ǫ)
2l
∑
A∈P(2l)
π-inv.
∑
B∈P(2l)
B γπ −1-inv.
∑
C∈P(r)
A,B≤1C
M¨ ob(C, 1r) C˜π, ˜A kγπ −1,B( ⃗D)
=
∑
π∈S(ǫ)
2l
∑
A,B∈P(2l)
A∨B=12l
C˜π, ˜A kγπ −1,B( ⃗D)
where the sum is over all A and B which are π and γπ −1-invariant
respectively. The last equality followed from the identity
∑
C∈P(r)
A,B≤1C
M¨ ob(C, 1r) =
{
1 A ∨ B = 1 2l
0 otherwise
This proves (17).
We know that the order of C˜π, ˜A is N −2l−#(π)+2#(A). Let ci be the
number of blocks of B that contain i cycles of γπ −1. By our assumption
on the second order limiting distribution of {A1, . . . , As}N
kγπ −1,B( ⃗D) =
{
O(N c1) c3 + c4 + · · · = 0
o(N c1) c3 + c4 + · · · > 0
Suppose ﬁrst that c3 + c4 + · · · > 0. Then
∑
i≥2
ici = (c2 + c3 + · · ·) +
∑
i≥1
(i − 1)ci ≥ 1 + #(γπ −1) − #(B)
So
c1 = #(γπ −1) −
∑
i≥2
ici ≤ #(B) − 1
By Lemma 2.2 (1), #( A) + #(B) ≤ 2l + 1. Thus
−2l − #(π) + 2#(A) + c1 ≤ −2l − #(π) + 2#(A) + #(B) − 1 ≤ 0
Hence C˜π, ˜A · kγπ −1( ⃗D) = o(N 0) as required.
22 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
So now suppose that c3 + c4 + · · · = 0. Then #( γπ −1) = c2 + #(B).
In this case
C˜π, ˜A · kγπ −1( ⃗D) = O(N −2l−#(π)+2#(A)+c1)
and thus it remains to show that
(19) −2l − #(π) + 2#(A) + c1 ≤ 2 − r
Note that
|(12l, γ)| = 2|12l| − |γ| = 2l − 2 + r,
|(A, π)| = 2|A| − |π| = 2l − 2#(A) + #(π)
and
|(B, γπ −1)| = 2|B| − |γπ −1| = 2l − 2#(B) + #(γπ −1)
So by Lemma 2.2 (2)
(20) 2
(
#(A) + #(B)) − 2l − #(π) − #(γπ −1) ≤ 2 − r
However
2#(B) − #(γπ −1) = #( B) − c2 = c1
together with (20) proves (19)
Remark 3.11. As a corollary of Theorem 3.10 we obtain that if {U}N
is a sequence of Haar distributed unitary random matrices, then {U}N
has a second order limit distribution given by equation (15). Indeed,
relative to E
(
Tr(·)
)
, U is already a Haar unitary so condition (9) of
Deﬁnition 3.5 is satisﬁed. We have observed in Remark 3.8 that condi-
tion (10) is satisﬁed and by Theorem 3.10 above we have that conditio n
(11) is satisﬁed.
Then {U}N has a second order limit distribution which is given by
lim
N →∞
k2
(
Tr(U ǫ1 · · · U ǫm), Tr(U ǫm+1 · · · U ǫm+n)
)
(21)
=
∑
π∈S(ǫ)
N C(m,n)
µ(˜π) +
∑
π1∈N C(ǫ1)(m)
π2∈N C(ǫ2)(n)
µ2(˜π1, ˜π2)
Combining this formula with equation (15) allows one to derive the
values of µ2. These kind of questions will be considered elsewhere.
Theorem 3.12. Let {U}N be a sequence of Haar distributed unitary
N ×N random matrices and {A1, . . . , As}N a sequence of N ×N random
matrices which has a second order limit distribution. If {U}N and
{A1, . . . , As}N are independent, then they are asymptotically free of
second order.
FLUCTUATIONS OF UNITARY RANDOM MATRICES 23
Proof. The asymptotic freeness with respect to k 1
(
tr(·)
)
is essentially
the same argument as Voiculescu’s proof [Voi1, Voi2] for the case of
constant matrices, see also the proof of Collins [C].
Theorem 3.10 provides the bound on higher order cumulants so we
need to prove now only the second order statement.
We have to consider cyclically alternating and centered words in
the U’s and the A’s. For the U’s, every centered word is a linear
combination of non-trivial powers of U, thus it suﬃces to consider such
powers. Thus we have to look at expressions of the form
(22) k 2
(
Tr(B1U i(1) · · · BpU i(p)), Tr(U j(r)Cr · · · U j(1)C1)
)
,
where the B’s and the C’s are centered polynomials in the A’s and
i(1), . . . , i(p), j(1), . . . , j(r) are integers diﬀerent from zero. We have
to show that in the limit N → ∞ the expression (22) converges to
(23)
lim
N
δpr
p−1∑
k=0
ϕ1(B1C1+k)ϕ1(U i(1)U j(1+k)) · · · ϕ1(BpCp+k)ϕ1(U i(p)U j(p+k)).
We can bring the expression (22) into the form considered in Theore m
3.7 by inserting 1’s between neighbouring factors U or neighbouring
factors U ∗. If we relabel the B’s, C’s, and 1’s as D’s then we have to
look at the following situation: For polynomials pi in s non-commuting
indeterminates we consider
Di := pi(A1, . . . , As),
which are either asymptotically centered or equal to 1. The latter
case can only appear if we have cyclically the pattern . . . U DiU . . . or
. . . U∗DiU ∗ . . . . Formally, this means:
• if ǫγ−1(i) = ǫi then either Di = 1 (for all N, i.e., pi = 1) or
lim
N →∞
k1
(
tr[Di]
)
= 0.
• if ǫγ−1(i) ⁄= ǫi then
lim
N →∞
k1
(
tr[Di]
)
= 0.
We can now use Theorem 3.7 for calculating the limit
lim
N →∞
k2
(
Tr(D1U ǫ1 · · ·DmU ǫm), Tr(Dm+1U ǫm+1 · · · Dm+nU ǫm+n)
)
,
and we will argue that most terms appearing there will vanish. First
consider the last two sums in equation (12), corresponding to π1 ∈
N C(m) and π2 ∈ N C(n). Since π1 is non-crossing we have that #(π1)+
24 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
#(γmπ−1
1 ) = m + 1. Since each cycle of π1 must contain at least one U
and one U ∗, we have
#(π1) ≤ m
2 ,
which implies #( γmπ−1
1 ) ≥ m/2 + 1. However, this can only be true if
γmπ−1
1 contains at least two singletons. Note that if ( i) is a singleton
of γmπ−1
1 and if we have Di = 1 for that i, then we have
γmπ−1
1 (i) = i, thus π−1
1 (i) = γ−1
m (i) = γ−1(i),
and hence
ǫπ−1
1 (i) = ǫγ−1(i) = ǫi,
which is not allowed because π1 is from N C(ǫ1)(m), i.e., it must connect
alternatingly U with U ∗. Hence Di ⁄= 1 and so ϕ1(di) = lim N k1(tr(Di))
= 0. Thus, both
ϕ1(γmπ−1
1 × γnπ−1
2 )[d1, . . . , dm+n]
and
ϕ2(γmπ−1
1 , γnπ−1
2 )[d1, . . . , dm+n]
are zero, because at least one singleton ( i) gives the contribution ϕ1(di)
= 0.
Consider now the ﬁrst summand of equation (12). Suppose π ∈
S(ǫ)
N C(m, n). Let us again put γ := γm,n. Since π is annular non-crossing
we have
|π| + |γπ −1| = m + n,
or
#(π) + #(γπ −1) = m + n.
Again, each cycle of π must contain at least two elements, i.e.,
#(π) ≤ m + n
2 ,
thus
#(γπ −1) ≥ m + n
2 .
If γπ −1 has a singleton ( i), then this will contribute ϕ1(di) and since,
as above the case di = 1 is excluded for a singleton, we get a van-
ishing contribution in this case. This implies that, in order to get a
non-vanishing contribution, γπ −1 must contain no singletons, which,
however, means that we must have
#(γπ −1) = m + n
2 , and thus also #( π) = m + n
2
i.e., all cycles of γπ −1 and of π contain exactly two elements. This,
however, can only be the case if each cycle connects one point on th e
FLUCTUATIONS OF UNITARY RANDOM MATRICES 25
outer circle to one point on the inner circle. Being non-crossing ﬁxes
the permutation up to a rotation of the inner circle. Thus, in order t o
get a non-vanishing contribution, we need m = n and
π = (1, γk(2n))(2, γk(2n − 1)), . . . ,(n, γk(n + 1))
for some k = 0, 1, . . . , n−1. Note that π must always couple a U with a
U ∗ and the factor µ(˜π) is always 1 for such pairings. This gives exactly
the contribution as needed for second order freeness.
Of course, a natural question in this context is how the result of Di-
aconis and Shahshahani (Remark 3.8) generalizes to the case of se veral
independent unitary random matrices. Note that as we have estab -
lished the existence of a second order limit distribution for Haar dis-
tributed unitary random matrices we can use an independent copy o f
them as the ensemble {A1, . . . , As} in our Theorem 3.12. By Remark
2.7 this can be iterated to give the following.
Theorem 3.13. Let {U (1)}N , . . . ,{U (r)}N be r sequences of Haar dis-
tributed unitary N × N-random matrices. If {U (1)}N , . . . ,{U (r)}N are
independent, then they are asymptotically free of second or der.
This contains the information about the ﬂuctuation of several inde -
pendent Haar distributed unitary random matrices. Again, it suﬃce s
to consider traces of reduced words in our random matrices, i.e., ex -
pressions of the form
(24) Tr( U k(1)
i(1) · · · U k(n)
i(n) )
for n ∈ N, and k(r) ∈ Z\{0} and i(r) ⁄= i(r + 1) for all r = 1 , . . . , n
(where i(n + 1) = i(1)). But these are now products in cyclically
alternating and centered variables, so that by the very deﬁnition o f
second order freeness we get
lim
N →∞
k2
(
Tr(U k(1)
i(1) · · ·U k(m)
i(m) ), Tr(U l(n)
j(n) · · · U l(1)
j(1))
)
(25)
= δmn
n−1∑
r=0
ϕ1
(
U k(1)
i(1) U l(1+r)
j(1+r)
)
· · · ϕ1
(
U k(n)
i(n) U l(n+r)
j(n+r)
)
.
The contribution of ϕ1 in these terms vanishes unless the matrices and
their powers match. Note also that the vanishing of higher cumulant s
can be rephrased in a more probabilistic language by saying that the
random variables (24) converge to a Gaussian family.
Corollary 3.14. Let {U(1)}N , . . . ,{U(r)}N be independent sequences of
Haar distributed unitary N × N-random matrices. Then, the collection
(24) of unnormalized traces in cyclically reduced words in t hese random
26 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
matrices converges to a Gaussian family of centered random v ariables
whose covariance is given by the number of matchings between the two
reduced words,
lim
N →∞
k2
(
Tr(U k(1)
i(1) · · · U k(m)
i(m) ), Tr(U l(n)
j(n) · · · U l(1)
j(1))
)(26)
= δmn · #
{
r ∈ {1, . . . , n} | i(s) = j(s + r),
k(s) = −l(s + r) ∀s = 1, . . . , n
}
This result was also obtained independently in the recent work of
R˘ adulescu [R] around Connes’s embedding problem.
The following theorem gives an easy way to construct families of
random matrices which are asymptotically free of second order.
Theorem 3.15. Let {U}N be a sequence of Haar distributed unitary
N × N-random matrices. Suppose that {A1, . . . , As}N and {B1, . . . ,
Bt}N are sequences of N × N random matrices each of which has a
second order limit distribution. Furthermore, assume that {A1, . . . ,
As}N , {B1, . . . , Bt}N , and {U}N are independent. Then the sequences
{A1, . . . , As}N and {U B1U ∗, . . . , U BtU ∗}N are asymptotically free of
second order.
Proof. The proof is a repetition of the proof of Theorem 3.12 except
that we cannot assume that {A1, . . . , As, B1, . . . , Bt}N has a second
order limit distribution. Instead we have the independence of the Ai
from the Bi’s and a special ǫ. So we shall only indicate how the proof
has to be modiﬁed.
The ﬁrst order freeness follows as in the proof of Theorem 3.12. In
the proofs of Theorems 3.7, 3.10, and 3.12 the cumulants we need ar e all
sums over S(ǫ)
2n for various n’s. Now we have a special form of ǫ, namely
ǫi = (−1)i+1. Thus if π ∈ S(ǫ)
2n then π takes even numbers to odd num-
bers and vice versa. Since the same applies to any of the γ’s, we have
that γπ −1 takes even numbers to even numbers and odd numbers to
odd numbers. Thus the orbits of γπ −1 consist either of all odd numbers
or of all even numbers. Hence if P1, . . . , Pn are words in A1, . . . , As and
Q1, . . . , Qn are words in B1, . . . , Bt, then by the independence of the
A’s and the B’s
E
(
Trγπ −1(P1, Q1, . . . , Pn, Qn)
)
= E
(
Tr(W1) · · ·Tr(Wj)
)
· E
(
Tr(Wj+1) · · · Tr(Wk)
)
where k = #( γπ −1) and Wi for 1 ≤ i ≤ j is a word only in A’s and
for j + 1 ≤ i ≤ k is a word only in B’s. This means that as far as
FLUCTUATIONS OF UNITARY RANDOM MATRICES 27
the asymptotic behaviour of E
(
Trγπ −1(P1, Q1, . . . , Pn, Qn)
)
is concerned
we may assume that {A1, . . . , As, B1, . . . , Bt}N has a second order limit
distribution. Hence our claim follows from Theorem 3.12
We say that a tuple {B1, . . . , Bs} of N ×N-random matrices is U(N)–
invariant if for every U ∈ U (N) the joint probability distribution of
the random matrices {B1, . . . , Bs} coincides with the joint probability
distribution of the random matrices {U B1U ∗, . . . , U BsU ∗}.
Corollary 3.16. Let {A1, . . . , As}N be a sequence of N × N-random
matrices which has a second order limit distribution and let {B1, . . . ,
Bt}N be a sequence of U(N)–invariant N × N-random matrices which
has a second order limit distribution. Furthermore assume t hat the ma-
trices {A1, . . . , As}N and the matrices {B1, . . . , Bt}N are independent.
Then the sequences {A1, . . . , As}N and {B1, . . . , Bt}N are asymptoti-
cally free of second order.
4. F ailure of Universality for multi-matrix models
In this section we want to make the meaning of second order freene ss
for ﬂuctuations of random matrices more explicit and relate this with
the question of universality of such ﬂuctuations. There has been m uch
interest in global ﬂuctuations of random matrices, in particular, sin ce
it was observed that for large classes of one-matrix models these ﬂ uctu-
ations are universal. In the physical literature this observation go es at
least back to Politzer [P], culminating in the paper of Ambjørn et al.
[AJM], whereas a proof on the mathematical level of rigour is due to
Johansson [J]. Universality for one-matrix models lets one expect th at
one would also have such universality for multi-matrix models. Indeed ,
this expectation was one of the starting points of our investigation s.
However, our machinery around second order freeness shows th at such
universality is not present in multi-matrix models.
Before we address multi-matrix models let us ﬁrst recall the relevan t
result of Johansson [J]. We consider Hermitian N ×N-random matrices
A = (aij)N
i,j=1 equipped with the probability measure
(27) dµN (A) = 1
ZN
exp
{
−NTr[P (A)]
}
dA,
where
dA =
∏
1≤i<j≤N
d Re aij d Im aij
N∏
i=1
daii.
Here, P is a polynomial in one variable, which we will address as “po-
tential” in the following, and ZN is a normalization constant. If one
28 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
restricts to a special class V of potentials P (the most important con-
dition being that the limit eigenvalue distribution has a single interval
as support – which we normalize in the following to [ −2, 2]) then Jo-
hansson proved the following universality of ﬂuctuations for this cla ss:
Consider the sequence of N ×N-random matrices {AN }N given by (27).
Then this sequence has a second order limit distribution which can be
described as follows:
(1) We have
lim
N →∞
k1{tr[An
N ]} =
∫
tndνP (t) ( n ∈ N),
where νP is a probability measure on R (“limiting eigenvalue
distribution”) which is given as the solution of the singular in-
tegral equation
(28)
∫ dνP (t)
t − s = −1
2 P ′(s) for all s ∈ supp νP .
(2) Let Tn (n ∈ N) be the Chebyshev polynomials of ﬁrst kind
(which are the orthogonal polynomials with respect to the arc-
sine law on [ −2, 2]). Then
lim
N →∞
k2{Tr[Tn(AN )], Tr[Tm(AN )]} = δmn · n.
Whereas the limiting eigenvalue distribution νP depends on the form
of the potential P , the ﬂuctuations are the same for all potentials in
the class V – they are always diagonalized by the same polynomials
{Tn | n ∈ N}. Note that the most prominent example for the considered
class of random matrices is given by P (A) = A2, which corresponds
to the Gaussian random matrix ensemble. So one can phrase this uni-
versality also in the way that all considered random matrices have th e
same ﬂuctuations as Gaussian random matrices (but their eigenvalu e
distributions are of course diﬀerent from Wigner’s semi-circle law).
Let us now consider multi-matrix models. For notational convenienc e
we restrict to the case of two-matrix models. Take now a polynomial
P (A, B) in two non-commuting variables and consider pairs of hermit-
ian N × N-matrices A = (aij)N
i,j=1 and B = (bij)N
i,j=1 equipped with the
probability measure
(29) dµN (A, B) = 1
ZN
exp{−NTr[P (A, B)]}dAdB,
where ZN is a normalization constant. The simplest ensemble of this
kind is the case of two independent Gaussian random matrices which
corresponds to the choice P (A, B) = A2 + B2. The above mentioned
universality result for the one-matrix case lets one expect that on e
FLUCTUATIONS OF UNITARY RANDOM MATRICES 29
might also have universality for multi-matrix ensembles which are close
to the ensemble of independent Gaussian random matrices. How-
ever, we will now show that even restricted to potentials of the for m
P (A, B) = P1(A) + P2(B) we do not have universal ﬂuctuations.
Let us ﬁrst observe that our concept of second order freeness tells
us how to diagonalize ﬂuctuations. We spell this out in the following
theorem which is an easy consequence of Deﬁnition 2.5 of second ord er
freeness.
Theorem 4.1. Let {AN }N and {BN }N be two sequences of N × N-
random matrices which are asymptotically free of second ord er. Let
{QA
n | n ∈ N} and {QB
n | n ∈ N} be the orthogonal polynomials for the
limiting eigenvalue distribution of AN and BN , respectively, determined
by the requirements that QA
n and QB
n are polynomials of degree n and
that
lim
N →∞
k1{tr[QA
n (AN )QA
m(AN )]} = δnm,
lim
N →∞
k1{tr[QB
n (BN )QB
m(BN )]} = δnm.
Then the ﬂuctuations of mixed traces in AN and BN are diagonalized
by cyclically alternating products of QA
n and QB
n and the covariances
are given by the number of cyclic matchings of these products :
lim
N →∞
k2
{
Tr[QA
i(1)(AN )QB
j(1)(BN ) · · ·QA
i(m)(AN )QB
j(m)(BN )],
Tr[QB
l(n)(BN )QA
k(n)(AN ) · · ·QB
l(1)(BN )QA
k(1)(AN )]
}
= δmn·#{r ∈ {1, . . . , n} |i(s) = k(s+r), j(s) = l(s+r) ∀s = 1, . . . , n}
To come back to our problem of universality for multi-matrix mod-
els we only have to observe that Corollary 3.16 tells us that we have
asymptotic freeness of second order if we choose a potential of t he form
P (A, B) = P1(A) + P2(B).
Theorem 4.2. Let P (A, B) = P1(A) + P2(B) where P1 and P2 are
polynomials from the class V. Consider the two-matrix model {AN ,
BN }N given by the probability measure (29). Let ν1 and ν2 be the
limiting eigenvalue distribution for P1 and P2, respectively (as described
in Eq. (28)) and denote by {Q1
n | n ∈ N} and {Q2
n | n ∈ N} the
respective orthogonal polynomials. Then the sequence {AN , BN }N has
a second order limit distribution given by (A, ϕ1, ϕ2) and a, b ∈ A which
can be described as follows:
(1) ϕ1 is the free product of ν1 and ν2.
(2) ϕ2 is diagonalized by the following collection of polynomials :
{Tn(a) | n ∈ N}
30 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
{Tn(b) | n ∈ N}
{Q1
i(1)(a)Q2
j(1)(b) · · · Q1
i(n)(a)Q2
j(n)(b)},
where in the last set we choose one representative from each
cyclic equivalence class, i.e. for all n ∈ N, n-tuples
(
(i(1), j(1)),
. . . ,(i(n), j(n))
)
which are diﬀerent modulo cyclic rotation
Proof. Note that the additive form of the potential P (A, B) = P1(A) +
P2(B) means that AN and BN are independent, AN is a one-matrix
ensemble corresponding, via (27), to a potential P1, and BN is a one-
matrix ensemble corresponding to a potential P2. Thus the statement
about the diagonalizing polynomials in either only AN or in only BN
is just Johansson’s result. For getting the statement about the d iag-
onalizing polynomials in both AN and BN we have to note that the
random matrices AN (and also BN ) are U(N)-invariant, thus Corol-
lary 3.16 implies that {AN }N and {BN }N are asymptotically free of
second order. Hence we can apply Theorem 4.1 above.
Note that whereas the polynomials in only one of the matrices are
universal (namely equal to the Chebyshev polynomials {Tn}n), the
polynomials which involve both matrices are not universal but depend
on the eigenvalue distributions ν1 and ν2. Since the latter vary with
the potentials P1 and P2, the polynomials Q1
n and Q2
n, and thus also
the alternating products in them, depend on the choice of P . Thus
we can conclude that even within the very restricted class of P ’s of
the form P (A, B) = P1(A) + P2(B) we have no universality of global
ﬂuctuations in multi-matrix models.
