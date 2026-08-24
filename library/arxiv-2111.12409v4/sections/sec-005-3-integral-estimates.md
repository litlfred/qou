---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem Paolo Dolce Francesco Zucconi 0 Introduction 1 0.1 History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
section_id: sec-005-3-integral-estimates
section_title: "Integral estimates"
section_number: 3
pages: 8-19
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmi"
---
This technical section is “the heart” of the proof of our resu lts since here we will prove some integral
bounds for very particular integrable functions θ : S ⊂ Ω → R≥0. We continue with all the notations
ﬁxed in section 2 since we want to make full use of Proposition 2.3.
Consider an adelic curve ( K, Ω , φ) and a set of vectors α 1, . . . ,α n, β ∈ KN which are compo-
nentwise diﬀerent. We construct the following matrices T := T (α 1, . . .α n) ∈ M (n × N, K) and
T (β ) ∈ M (n + 1 × N, K):
T :=


α(1)
1 α(2)
1 . . . α (N)
1
α(1)
2 α(2)
2 . . . α (N)
2
...
...
...
...
α(1)
n α(2)
n . . . α (N)
n


; T (β ) =


α(1)
1 α(2)
1 . . . α (N)
1
α(1)
2 α(2)
2 . . . α (N)
2
...
...
...
...
α(1)
n α(2)
n . . . α (N)
n
β(1) β(2) . . . β (N)


We denote by α (j), j = 1, . . . , N the columns of T , that is:
α (j) =


α(j)
1
α(j)
2
...
α(j)
n


and by α h, for h ∈ {1, 2, . . . , n}, the rows:
α h =
(
α(1)
h , α(2)
h , . . . , α(N)
h
)
Note that we are asking for the matrices T and T (β ) to have componentwise diﬀerent rows. Now we
need to deﬁne a list of properties depending on the aforement ioned matrices:
8
Deﬁnition 3.1. For the matrix T (β ), consider the following real numbers for any j = 1, . . . , N:
ρj := 4 2N!H(β(j))
n∏
h=1
H(α(j)
h )
2N !
n (11)
ρ′
j := 4 N!H(β(j))
n∏
h=1
H(α(j)
h )
N !
2n (12)
We say that T (β ) satisﬁes the h-gap property if the following inequality is satisﬁed:
log ρj
log ρ′
j+1
< 1
4nN 2N ! , ∀j = 1, . . . , N − 1
Deﬁnition 3.2. Fix a measurable set S = S1 ⊔ . . . ⊔ Sn. We say that an integrable function
θ : S → R≥0 is a column bounding function for T (β ) on S if the following inequality holds:
− 1
log ρj
log|α(j)
h − β(j)|ω ≥ θ(ω) ∀j = 1, . . . , N , ∀h = 1, . . . , n , ∀ω ∈ Sh (13)
Deﬁnition 3.3. Fix a measurable set S = S1 ⊔ . . . ⊔ Sn. For any column α (j) ∈ KN of the matrix
T and any b ∈ K we deﬁne the following quantity:
λ(α (j), b) := 1
V (s) log4 + h(b) + 1
V (s)
n∑
h=1
V (th)h(α(j)
h )
Deﬁnition 3.4. We say that T (β ) satisﬁes the λ-gap property of width η ∈ R+ if
max
1≤j≤N−1
λ(α (j), β(j))
λ(α (j+1), β(j+1)) < η
2n
Deﬁnition 3.5. Fix a matrix T (β ). An integrable function θ : S → R≥0 is λ-bounding if:
−1
λ(α (j), β(j)) log|α(j)
h − β(j)|ω ≥ θ(ω) ∀j = 1, . . . , N; ∀h = 1, . . . , n; ∀ω ∈ Sh (14)
Remark 3.6. Note that if θ is λ-bounding or column bounding then it follows immediately th at
|α(j)
h − β(j)|ω ≤ 1 for any j = 1, . . . , N, h = 1, . . . , n, ω ∈ Sh.
The following easy lemma will be useful:
Lemma 3.7. Let x, y ∈ K and let ω such that |x − y|ω ≤ 1. Then log+ |x|ω ≤ log+ |2|ω + log+ |y|ω.
Proof. We distinguish two cases:
| · |ω is ultrametric. Then
|x|ω = |x − y + y|ω ≤ max {|x − y|ω, |y|ω} ≤ max {1, |y|ω} .
If |y|ω ≥ 1, then clearly log + |x|ω ≤ log+ |y|ω. If |y|ω < 1, then |x|ω ≤ 1 which means 0 = log + |x|ω ≤
log+ |2|ω + log+ |y|ω.
| · |ω is archimedean. By Ostrowski’s theorem | · |ω = | · |ε(ω), therefore
|x|
1
ε(ω)
ω ≤ |x − y|
1
ε(ω)
ω + |y|
1
ε(ω)
ω ≤ 1 + |y|
1
ε(ω)
ω .
This clearly means |x|
1
ε(ω)
ω ≤ 2 max
{
1, |y|
1
ε(ω)
ω
}
. After raising each side to the power of ε(ω) and
applying log + we get the claim.
Now we prove the analogue of [ Cor97, Proposition 3.1].
Proposition 3.8. Let (K, Ω , φ) be a proper adelic curve. Fix a matrix T (β ). Let η, s, t1, . . . , tn ∈ R
such that all the hypotheses of Proposition 2.3 are satisﬁed. Assume that T (β ) satisﬁes the λ-gap
property of width η (see Deﬁnition 3.4) and that θ : S → R≥0 is λ-bounding for T (β ) (see Deﬁnition
3.5), then
n∑
h=1
(
th − s − 2ηN 2
V (s)
)∫
Sh
θdµ ≤ N
9
Proof. Fix a real number D > 0, and for every j = 1, . . . , N, we put
dj := D
λ(α (j), β(j))
and d :=∏ N
j=1 dj . Note that here we use the λ-gap property to ensure that dj +1
dj
< γ since η = 2nγ
as explained before Proposition 2.3. So, the hypotheses of Proposition 2.3 are all satisﬁed and we
have the interpolation polynomial δ such that δ(β ) ⁄= 0. We start by distinguishing two cases.
First case: ω ∈ Sh. By the Taylor expansion for δ at α h we write
δ(β ) =
∑
i
∆ iδ(α h)
N∏
j=1
(β(j) − α(j)
h )ij where i = (i1, . . . , iN ) (15)
Notice that each term
∆ iδ(α h)
N∏
j=1
(β(j) − α(j)
h )ij
is bounded from above by:
(
max
i
∆ iδ(α h)
)(
∗
max
i
N∏
j=1
(β(j) − α(j)
h )ij
)
,
where in order to simplify the notation we deﬁne
∗
max
i
:= max
i
∆ iδ(α h)⁄=0
Let’s put M :=∏ N
j=1(1 + deg Xj δ); so by taking the absolute value | · |ω in equation ( 15) we get
log |δ(β )|ω ≤ log+ |M |ω + max
i
log
⏐⏐⏐∆ iδ(α h)
⏐⏐⏐
ω
+
∗
max
i
log
⏐⏐⏐⏐⏐
N∏
j=1
(β(j) − α(j)
h )ij
⏐⏐⏐⏐⏐
ω
(16)
The last summand of equation ( 16) is bounded from above by
−Indα h,d(δ) min
{
d1 log 1
|β(1) − α(1)
h |ω
, . . . , dN log 1
|β(N) − α(N)
h |ω
}
.
We use Lemma 1.11 to give an upper bound for log
⏐⏐∆ iδ(α h)
⏐⏐
ω, hence from equation ( 16) we deduce:
∫
Sh
log |δ(β )|ωdµ(ω) ≤
≤
∫
Sh
log+|M |ωdµ(ω) +
∫
Sh
(
hω(δ) + log +|M |ω +
N∑
j=1
(log+ |2|ω + log+ |α(j)
h |ω) degXj δ
)
dµ(ω)+
−
∫
Sh
Indα h,d(δ) min
{
d1 log 1
|β(1) − α(1)
h |ω
, . . . , dN log 1
|β(N) − α(N)
h |ω
}
dµ(ω)
So, by rearranging the terms and summing over all h = 1, . . . , n we get
n∑
h=1
Indα h,d(δ)
∫
Sh
min
{
d1 log 1
|β(1) − α(1)
h |ω
, . . . , dN log 1
|β(N) − α(N)
h |ω
}
dµ(ω) ≤ −
∫
S
log |δ(β )|ωdµ(ω)
+ 2
∫
S
log+ |M |ωdµ(ω) +
∫
S
hω(δ)dµ(ω) +
n∑
h=1
∫
Sh
N∑
j=1
(log+ |2|ω + log+ |α(j)
h |ω) degXj δdµ(ω) (17)
At this point we can use Lemma 3.7 and Remark 3.6 for the following bound:
n∑
h=1
∫
Sh
N∑
j=1
(log+ |2|ω + log+ |α(j)
h |ω) degXjδdµ(ω) ≤
∫
S
N∑
j=1
(log+ |4|ω + log+ |β(j)
h |ω) degXjδdµ(ω)
(18)
10
to obtain
n∑
h=1
Indα h,d(δ)
∫
Sh
min
{
d1 log 1
|β(1) − α(1)
h |ω
, . . . , dN log 1
|β(N) − α(N)
h |ω
}
dµ(ω) ≤ −
∫
S
log |δ(β )|ωdµ(ω)+
+ 2
∫
S
log+ |M |ωdµ(ω) +
∫
S
hω(δ)dµ(ω) +
∫
S
N∑
j=1
(log+ |4|ω + log+ |β(j)
h |ω) degXjδdµ(ω) . (19)
Second case: ω ⁄∈S. Consider the expression:
δ(β ) =
∑
i
∆ iδ(0)β(1)i1 . . . β(N)iN where i = (i1, . . . , iN )
We take the absolute value:
log |δ(β )|ω ≤ hω(δ) +
N∑
j=1
(log+ |β(j)|ω degXjδ) + log + |M |ω
Hence
∫
Ω \S
log |δ(β )|ωdµ(ω) ≤
∫
Ω \S
hω(δ)dµ(ω)+
N∑
j=1
∫
Ω \S
(log+ |β(j)|ω degXjδ )dµ(ω)+
∫
Ω \S
log+ |M |ωdµ(ω)
(20)
Since ( K, Ω , φ) is proper
−
∫
S
log |δ(β )|ωdµ(ω) =
∫
Ω \S
log |δ(β )|ωdµ(ω) . (21)
The distinction of the two cases is now ﬁnished, so by using eq uation ( 21) and estimate ( 20) inside
(19) we get
n∑
h=1
Indα h,d(δ)
∫
Sh
min
{
d1 log 1
|β(1) − α(1)
h |ω
, . . . , dN log 1
|β(N) − α(N)
h |ω
}
dµ(ω) ≤ 2h(M )+
+
∫
Ω
hω(δ)dµ(ω)+
N∑
j=1
∫
Ω \S
(log+ |β(j)|ω degXjδ )dµ(ω)+
∫
S
N∑
j=1
(log+ |4|ω +log+ |β(j)
h |ω) degXjδdµ(ω)
(22)
Since we can always assume that µ is adequately normalised, we have
∫
Ω log+ |4|ωdµ(ω) = h(4) ≤
log 4, therefore:
N∑
j=1
∫
Ω \S
(log+ |β(j)|ω degXjδ )dµ(ω) +
∫
S
N∑
j=1
(log+ |4|ω + log+ |β(j)
h |ω) degXjδdµ(ω) ≤
≤
N∑
j=1
(
h(β(j)) + log 4
)
degXjδ
By plugging everything inside equation ( 22) we get
n∑
h=1
Indα h,d(δ)
∫
Sh
min
{
d1 log 1
|β(1) − α(1)
h |ω
, . . . , dN log 1
|β(N) − α(N)
h |ω
}
dµ(ω) ≤
≤ 2h(M ) + h(δ) +
N∑
j=1
(
h(β(j)) + log 4
)
degXjδ (23)
By the λ-bounding hypothesis for T (β ) we can write
− D
λ(α (j), β(j)) log |β(j) − α(j)
h |ω ≥ Dθ(ω) .
Then we use Proposition 2.3(3), so we can conclude
D
n∑
h=1
dV (s)
(
th − s − 2N 2η
V (s)
)∫
Sh
θdµ ≤
≤
n∑
h=1
Indα h,d(δ)
∫
Sh
min
{
d1 log 1
|β(1) − α(1)
h |ω
, . . . , dN log 1
|β(N) − α(N)
h |ω
}
dµ(ω) (24)
11
Now we are going to use again Proposition 2.3 to ﬁnd upper bounds for the terms on the right hand
side of equation ( 23). By Proposition 2.3(2):
N∑
j=1
(
h(β(j)) + log 4
)
degXjδ ≤
N∑
j=1
(
h(β(j)) + log 4
)
(ddjV (s) + O(d)) . (25)
Proposition 2.3(4) says that,
h(δ) ≤ d
N∑
j=1
dj
(
log 2 +
n∑
h=1
V (th)h(α(j)
h )
)
+ O(d log d) (26)
So now ( 23) can be written in the following way:
D
n∑
h=1
dV (s)
(
th − s − 2N 2η
V (s)
)∫
Sh
θdµ ≤ 2h(M ) + d
N∑
j=1
dj
(
log 2 +
n∑
h=1
V (th)h(α(j)
h )
)
+
+ O(d log d) +
N∑
j=1
(
h(β(j)) + log 4
)
(ddjV (s) + O(d)) (27)
Notice that since s ≤ 1 and N ≥ 2 then V (s) ≤ 1
2 , which is equivalent to the inequality V (s) log 4 +
log 2 ≤ log 4. Then the expression
d
N∑
j=1
dj
(
log 2 +
n∑
h=1
V (th)h(α(j)
h )
)
+ O(dlogd) +
N∑
j=1
(
h(β(j)) + log 4
)
(ddjV (s) + O(d))
is bounded by
d
N∑
j=1
dj
(
V (s)h(β(j)) + log 4 +
n∑
h=1
V (th)h(α(j)
h )
)
+ O(d log d)
But by the deﬁnitions of dj and the function λ it holds that
dV (s)
N∑
j=1
dj
(
h(β(j)) + log 4
V (s) +
n∑
h=1
V (th)
V (s) h(α(j)
h )
)
= dV (s)N D . (28)
Therefore equation ( 27) becomes
dDV (s)
n∑
h=1
(
th − s − 2N 2η
V (s)
)∫
Sh
θdµ ≤ dV (s)N D + O(d log d)
since the terms 2 h(M ) and O(d) can be put together inside O(d log d). Finally we divide both sides
by dDV (s) and we take the limit for D → +∞ (i.e. d → +∞) to conclude the proof.
Theorem 3.9. Let (K, Ω , φ) be a proper adelic curve. Assume that the matrix T (β ) ∈ M (n × N, K)
satisﬁes the h-gap property (see Deﬁnition 3.1). Moreover ﬁx N > 212 log 2n and let θ : S → R≥0 be
a column-bounding function for T (β ) (see Deﬁnition 3.2). Then
∫
S
θdµ < 2 + 7√log 2n√
N
Proof. The proof is based on the exact calculation of the volume V (s) of [ Sch91, Chap. 2, Lemma
5A, 5B]. It shows that for N ≥ 2, s, ρ ∈ R>0 with 0 < s ≤ 1 and 0 < ρ < N
2 , we have:
V (s) = sN
N ! (29)
V
(N
2 − ρ
)
< e
−ρ2
N (30)
We take t1 = t2 = . . . = tn = N
2 − ρ, η = 1
2N 2N! where ρ is a number such that:
V
(N
2 − ρ
)
= 1 − ηN 2
n
Note that 1−ηN 2
n > 1
2n . Now from equation ( 30) we get
−ρ2
N > log
(1 − ηN 2
n
)
12
which implies easily
ρ <
√
N log 2n .
Now let’s take s as a solution of:
(1 + η)N − 1 + ηN 2 < V (s) < 2N η + ηN 2 (31)
Here recall that 1 − ηN 2 = nV (th) =∑ n
h=1 V (th) (compare with the condition ( 10)). From equation
(31) we get the following two conditions
N ! < 1
V (s) < 2N !
N !
2n < V (th)
V (s) < 2N !
n
Now we show that by using such conditions since T (β ) satisﬁes h-gap property, then it satisﬁes
also the λ-gap property of width η. First let’s use the inequalities 1
V (s) < 2N ! and V (th)
V (s) < 2N!
n to
bound λ(α (j), β(j)) from above:
λ(α (j), β(j)) = 1
V (s) log4 + h(β(j)) + 1
V (s)
n∑
h=1
V (th)h(α(j)
h ) <
< 2N ! log 4 + h(β(j)) + 2N !
n
n∑
h=1
h(α(j)
h ) = log ρj .
Then we use the inequalities N ! < 1
V (s) and N!
2n < V (th)
V (s) to bound λ(α (j+1), β(j+1)) from below:
λ(α (j+1), β(j+1)) = 1
V (s) log4 + h(β(j+1)) + 1
V (s)
n∑
h=1
V (th)h(α(j+1)
h ) >
> N ! log 4 + h(β(j+1)) + N !
2n
n∑
h=1
h(α(j+1)
h ) = log ρ′
j .
Therefore now:
λ(α (j), β(j))
λ(α (j+1), β(j+1)) < log ρj
log ρ′
j
< 1
4nN 2N ! = η
2n .
Note that as an immediate consequence of the last inequality it follows that all the hypotheses of
Proposition 2.3 are satisﬁed. Moreover, since θ is a column-bounding function for T (β ), then it is
λ-bounding for T (β ). It means that we can apply Proposition 3.8 to get:
∫
S
θdµ ≤ N
N
2 − ρ − s − 2ηN 2
V (s)
(32)
Since ρ < √N log 2n, N 2η < V (s) and in particular N > max
{
36
log 2n , 9 log 2n
}
, we obtain:
2(ρ + s)
N + 4ηN
V (s) < 2√N log 2n + 2 + 4
N < 3√N log 2n
N = 3√log 2n√
N
< 1
Therefore
N
N
2 − ρ − s − 2ηN 2
V (s)
= 2
1 − 2(ρ+s)
N − 4ηN
V (s)
< 2
1 − 3√log 2n√
N
< 2 + 7√log 2n√
N
.
Where the last inequality follows by the assumption N > 212 log 2n.
4 Roth’s theorem for adelic curves (A)
Deﬁnition 4.1. A proper adelic curve X = ( K, Ω , µ) satisﬁes the strong µ-equicontinity condition
if for any measurable set S ⊂ Ω of ﬁnite measure and any real number ε > 0 there exists a ﬁnite
measurable cover C1, . . . , Cm of S satisfying the following conditions: for all β ∈ K× there exists a
measurable set Uβ ⊂ Ω ∞ such that µ(Uβ) = 0 and
⏐⏐− log− |β|ω + log− |β|ω′
⏐⏐ < εh(β) , ∀ω, ω′ ∈ Cj \ Uβ , ∀j = 1, . . . , m
The following lemma is a simpliﬁed version of [ Voj21, Lemma 8.10]. It can be seen as a generali-
sation of the Arzel` a-Ascoli theorem for measure spaces, wi th the advantage that one doesn’t need to
provide a uniform bound for the involved family of functions .
13
Lemma 4.2. Let X = ( K, Ω , φ) be a proper adelic curve satisfying the strong µ-equicontinuity con-
dition. Fix α ∈ K× and a measurable subset S ⊂ Ω of ﬁnite measure. Let {βk} be a sequence in K×
such that βk ⁄= α, and h(βk) → +∞. Then for any ε > 0 there exists a subsequence
{
βkj
}
such that
for any j, ℓ ∈ N big enough the following inequality holds on S \ U , where U ⊂ Ω ∞ and µ(U ) = 0 :
⏐⏐⏐⏐⏐− log− |α − βkj |ω
h(βkj ) + log− |α − βkℓ |ω
h(βkℓ )
⏐⏐⏐⏐⏐ < ε
Proof. Put h0 = min k h(βk) and λk(ω) = − log− |α − βk|ω. Fix ε > 0 and let C1, . . . , Cr be a ﬁnite
measurable cover as in Deﬁnition 4.1. Clearly by possibly passing to a reﬁnement we can assume
that the cover is made of mutually disjoints sets. Let k ∈ N; if i ∈ { 1, . . . , r} is such that µ(Ci) = 0
we deﬁne mk,i = 0, otherwise if i is such that µ(Ci) > 0 we put
mk,i = inf
{
t ∈ R : µ
({
ω ∈ Ci : λk(ω)
h(βk) ≥ t
})
≤ µ(Ci)
2
}
Notice that the sets:
Vk,i = {ω ∈ Ci : λk(ω) ≤ h(βk)mk,i} , T k,i = {ω ∈ Ci : λk(ω) ≥ h(βk)mk,i}
have both measure at least µ(Ci)
2 . Hence we get:
µ(Ci)
2 h(βk)mk,i ≤
∫
Tk,i
h(βk)mk,idµ ≤
∫
Tk,i
λkdµ ≤
∫
S
λkdµ (33)
But by Proposition 1.13(6) we know that
∫
S
λkdµ ≤ h(βk)
( log 2
h(βk) + h(α)
h(βk) + 1
)
≤ h(βk)
(log 2
h0
+ h(α)
h0
+ 1
)
(34)
So by putting ci = 2
µ(Ci)
(
log 2
h0
+ h(α)
h0
+ 1
)
, equations ( 33) and ( 34) show that mk,i ≤ ci. Note that
the constant ci doesn’t depend on k. It follows that all the vectors mk = ( mk,1, . . . , mk,r) ∈ Rr, lie in
the hyper-parallelepiped ∏ r
i=1[0, ci]. Now consider the small hyper-cubes Qk =∏ r
i=1[mk,i − ε, mk,i +
ε], clearly there exists an index k ∈ N and a sequence {kj } such that mkj ∈ Qk for any j ∈ N. We
now show that the subsequence {βkj } has exactly the properties that we are searching for.
Consider any two elements βkj βkℓ of the subsequence and ω ∈ S \ (Uβkj
∪ Uβkℓ
). Let i be the
unique index such that ω ∈ Ci; pick ω′ ∈ Ci \ Uβkj
and ω′′ ∈ Ci \ Uβkℓ
such that:
λkj (ω′) ≤ mkj ,ih(βkj ) ,
λkℓ (ω′′) ≥ mkℓ,ih(βkℓ ) .
Note that this is possible since Vkj ,i and Tkℓ,i have positive measure. In the following chain of
inequalities we use twice the strong µ-equicontinuity condition (ﬁrst for ω, ω′ and later for ω, ω′′) and
the fact that |mkj ,i − mkℓ,i| < 2ε.
λkj (ω)
h(βkj ) < λkj (ω′)
h(βkj ) + h(α − βkj )
h(βkj ) ε < (Pr. 1.13(4)) λkj (ω′)
h(βkj ) +
(
1 + log 2 + h(α)
h(βkj )
)
ε ≤
≤ mkj ,i +
(
1 + log 2 + h(α)
h(βkj )
)
ε ≤ mkℓ,i +
(
3 + log 2 + h(α)
h(βkj )
)
ε ≤ λkℓ (ω′′)
h(βkℓ ) +
(
3 + log 2 + h(α)
h(βkj )
)
ε <
< λkℓ (ω)
h(βkℓ ) +
(
4 + log 2 + h(α)
h(βkj ) + log 2 + h(α)
h(βkℓ )
)
ε
Since h(βk) → +∞ for j and ℓ big enough the above inequalities say:
λkj (ω)
h(βkj ) < λkℓ(ω)
h(βkℓ ) + 5ε
By swapping the roles of j and ℓ we obtain in the same way
λkℓ (ω)
h(βkℓ ) < λkj (ω)
h(βkj ) + 5ε
The claim ﬁnally follows by the arbitrariness of ε.
14
Proof of theorem (A). When n ≤ 2, from Proposition 1.13(6) we deduce that any approximant
β such that
h(β) > n log 2 +∑ n
i=1 h(αi)
2 − n + ε
satisﬁes the desired inequality.
Assume n ≥ 3. We consider the following matrix of dimension n × N , where N > 212 log 2n will
be a big enough ﬁxed integer:
T =


α1 α1 . . . α 1
α2 α2 . . . α 2
...
...
...
...
αn αn . . . α n


notice that we have repeated N times the same column vector. Assume by contradiction that t he
theorem is false. Namely that there exists an ε0 > 0 such that the inequality
n∑
i=1
∫
Si
log− |βk − αi|ωdµ(ω) ≤ −(2 + ε0)hX(βk) (35)
is satisﬁed by a sequence {βk}k∈N in K with the properties that h(βk) → +∞. Pick a constant:
L > log
(
42N!
n∏
i=1
H(αi)
2N !
n
)
Since h(βk) → +∞, by eventually passing to a subsequence, we can assume that {h(βk)} is increasing
and bounded from below by a very big value. Therefore we can as sume
ε0 > 2L
h(βk) + L + h(βk)
h(βk)
8√log 2n√
N
, ∀k ∈ N (36)
Choose any N elements from the sequence {βk}, call them β(1), . . . β(N) and consider the following
matrix T (β ):
T (β ) =


α1 α1 . . . α 1
α2 α2 . . . α 2
...
...
...
...
αn αn . . . α n
β(1) β(2) . . . β (N)


We are ready to construct some functions θk ∈ L1(S, µ) which will give the desired contradiction.
We deﬁne them as piecewise functions by putting for any ω ∈ Si and any k ∈ N:
θk(ω) = − log− |βk − αi|ω
L + h(βk)
Now we can write
∫
S
θkdµ =
n∑
i=1
∫
Si
θkdµ = −1
L + h(βk)
n∑
i=1
∫
Si
log− |βk − αi|ωdµ(ω) ≥eq.(35) (2 + ε0)h(βk)
L + h(βk) (37)
By plugging inequality ( 36) inside ( 37) and simplifying the expressions, we ﬁnally get:
∫
S
θkdµ > 2 + 8√log 2n√
N
∀k ∈ N (38)
Thanks to Proposition 1.13(6): ∫
Si
θk ≤ Bi + h(βk)
L + h(βk)
for Bi ∈ R>0. So, if B = max i{Bi} we obtain:
∫
S
θkdµ ≤ nB + nh(βk)
L + h(βk) ≤ n .
Then after possibly passing to a subsequence of {θk}, we can assume that
∫
S θkdµ admits limit and
by inequality ( 38):
lim
k→∞
∫
S
θkdµ ≥ 2 + 8√log 2n√
N
> 2 + 7√log 2n√
N
. (39)
15
Put by simplicity λi,k(ω) := − log− |βk − αi|ω for ω ∈ Si, so
θk(ω) = λi,k(ω)
L + h(βk) .
Then we have:
θk(ω) = λi,k(ω)
h(βk) Ak
where Ak := 1 − L
L+h(βk) < 1 and Ak → 1. By Lemma 4.2 from
{
1
Ak
θk
}
we can extract a subsequence
{
1
Akj
θkj
}
uniformly convergent to a function θ on S \ U , where µ(U ) = 0. We extend θ on the whole
S by putting θ|U = 0. Since on a set of ﬁnite measure the uniform convergence im plies the L1-
convergence, we can write:
∫
S
θdµ =
∫
S\U
θdµ = lim
j→∞
∫
S\U
1
Akj
θkj dµ = lim
j→∞
∫
S
1
Akj
θkj dµ =
=
(
lim
j→∞
1
Akj
)(
lim
j→∞
∫
S
θkj dµ
)
> 2 + 7√log 2n√
N
.
(40)
Consider a positive real number C such that
Cµ(S) <
∫
S
θdµ −
(
2 + 7√log 2n√
N
)
and deﬁne the set
T := {ω ∈ S : θ(ω) < C } .
Note that T contains the previously introduced U . We obtain the following chain of inequalities:
∫
T
θdµ ≤ Cµ(T ) ≤ Cµ(S) <
∫
S
θdµ −
(
2 + 7√log 2n√
N
)
which gives ∫
S\T
θdµ > 2 + 7√log 2n√
N
Now we deﬁne the function ˆθ : S → R≥0 such that
ˆθ(ω) =
{
θ(ω) if ω ∈ S \ T
0 otherwise
Clearly ˆθ(ω) ≥ C for any ω ∈ S \ T and moreover
∫
S
ˆθdµ =
∫
S\T
θdµ > 2 + 7√log 2n√
N
.
We can choose γ ∈ ]0, 1[ such that
∫
S
γ ˆθdµ > 2 + 7√log 2n√
N
. (41)
We want to show that the function γ ˆθ satisﬁes the hypotheses of Theorem 3.9. Choose δ ∈ R>0 such
that
0 < δ < (1 − γ)C
so that for any ω ∈ S \ T we have
γ ˆθ(ω) < ˆθ(ω) − δ .
Denote by {θm} the previously extracted subsequence that converges unifo rmly to θ on S \ T . We
can ﬁnd a positive integer M such that if m > M the following chain of inequalities holds for any
ω ∈ S \ T :
0 < γ ˆθ(ω) < ˆθ(ω) − δ < θ m(ω) < − log− |βm − αi|ω
h(βm) + log
(
42N!∏ n
i=1 H(αi)
2N !
n
) (42)
We choose β := (β(1), . . . , β(N)) in the set {βm}m>M with the following properties:
• The elements β(j) are separated by big enough gaps, so that the matrix T (β ) satisﬁes the h-gap
condition.
16
• The elements β(j) are chosen in a way that |β(j) −αi|ω ≤ 1 for any i = 1, . . . , n and any ω ∈ S \T .
Note that this is possible because we can iterate n-times Lemma 4.2 starting with the sequence
{βm} and extracting at each step i = 1 , . . . , n a sequence {βj } such that ω ↦→
− log− |βj −αi|ω
h(βj )
converges uniformly almost everywhere to a function bounde d from below by a positive number.
In this way inequality ( 42) ensures that γ ˆθ is column bounding.
Finally we can apply Theorem 3.9 for γ ˆθ to get:
∫
S
γ ˆθdµ < 2 + 7√log 2n√
N
which contradicts inequality ( 41). □
Now we show that Theorem 0.2 can be immediately recovered from Theorem (A).
Proposition 4.3. Theorem (A) implies Theorem 0.2.
Proof. Let K be the Galois closure of k(α1, . . . , αn) over k and consider the adelic curve X = (K, Ω , µ)
naturally lying over ( k, Vk). The strong µ-equicontinuity condition trivially holds on X since all
singletons of Ω are measurable and inf ω∈Ω µ({ω}) > 0. For any vi of Theorem 0.2 consider the set
~Si := {ω ∈ Ω : ω extends vi} = {ωij : j = 1, . . . , r(i)} for i = 1, . . . , n
The set ~Si are orbits under the action of Gal( K/k) on Ω. For each i, j there is αij ∈ K such that
|β − αij|ωij = |β − αi|vi , ∀β ∈ k
Now we apply Theorem (A) on the set ~S = ∪ℓ~Sℓ partitioned along the ﬁbers of the map ωij ↦→aij.
Hence we get the following inequality
∑
i,j
∫
{ωij }
log− |β − αij|ωij dµ(ω) > −(2 + ε)hX(β).
Note that the summation over i and j doesn’t reﬂect the partition. But
∑
i,j
∫
{ωij }
log− |β − αij|ωij dµ(ω) =
∑
ij
log− |β − αij|ωij µ({ωij}) =
=
∑
i
(
log− |β − αi|vi
∑
j
µ({ωij})
)
=
∑
i
log− |β − αi|vi
Where the last equality follows from [ Neu99, Ch. II, Corollary 8.4]:
r(i)∑
j=1
µ({ωij}) =
r(i)∑
j=1
[Kωij : kvi ]
[K : k] = 1 .
5 Roth’s theorem for adelic curves (B)
We weaken Deﬁnition 4.1 by requiring the “equicontinuity property” outside from se ts of arbitrary
small measure:
Deﬁnition 5.1. A proper adelic curve X = (K, Ω , µ) satisﬁes the µ-equicontinuity condition if for any
measurable set S ⊂ Ω of ﬁnite measure and any real numbers ε, δ > 0 there exists a ﬁnite measurable
cover C1, . . . , Cm of S satisfying the following conditions. For all β ∈ K× there exists a measurable
set Uβ ⊂ Ω ∞ such that µ(Uβ) < δ and
⏐⏐− log− |β|ω + log− |β|ω′
⏐⏐ < εh(β) , ∀ω, ω′ ∈ Cj \ Uβ , ∀j = 1, . . . , m
In [ Voj21, Proposition 8.9] it is shown that arithmetic function ﬁeld s satisfy the µ-equicontinuity
condition.
Deﬁnition 5.2. A proper adelic curve X = ( K, Ω , µ) satisﬁes the uniform integrability condition if
for any ε > 0 there exists δ > 0 such that if T ⊂ Ω ∞ is a measurable subset satisfying µ(T ) < δ , then
∫
T
− log− |β|ωdµ(ω) < εh X(β) , ∀β ∈ K× .
17
Vojta shows that arithmetic function ﬁelds satisfy the unif orm integrability condition in [ Voj21,
Lemma 8.8]. The following lemma provides a key step in our pro of:
Lemma 5.3. Let X = (K, Ω , φ) be a proper adelic curve satisfying the µ-equicontinuity condition and
the uniform integrability condition. Assume that Theorem (B) doesn ’t hold for certainS, α1, . . . , αn ∈
K, ε0 ∈ R>0 and c ∈ R. Let N > 0 an integer, ε ∈ ]0, ε0[, and r0, r1 > 1 two real numbers. Then
there exist β(1), . . . , β(N) ∈ K satisfying the following conditions:
(1) h(β(1)) > r 0
(2) h(β(k))
h(β(k−1)) > r 1 for any k = 2, . . . , N.
(3) There is a partition S = S1 ⊔ . . . ⊔ Sn such that:
n∑
i=1
∫
Si
min
1≤k≤N
(− log− |β(k) − αi|ω
h(β(k))
)
dµ(ω) > 2 + ε
Proof. The rather technical proof can be found in [ Voj21, Proposition 8.12] for arithmetic function
ﬁelds, and it can be repeated line by line for our case. The pro of uses [ Voj21, Lemmas 8.10, 8.11],
that in turn rely on 3 assumptions denoted in [ Voj21] by (i), (ii), (iii). Vojta needs to show that such
assumptions are satisﬁed in his case, and the proofs are quit e involved. On the other hand, we now
explain why the assumptions hold immediately in our setting : assumption (i) follows by the integral
Liouville inequality (see Proposition 1.13(6)) if we put Ξ = {βk}, q = n, λβk,j = − log− |αj − βk|
and c9 = log 2 + max j h(αj) for j = 1 , . . . , n. Assumption (ii) is the µ-equicontinuity condition.
Assumption (iii) is the uniform integrability condition.
Finally, note that in the statement of [ Voj21, Proposition 8.12] the condition (1) is not explicitly
mentioned as a consequence of the hypotheses, but it can be ea sily deduced from the proof.
Proof of theorem (B). When n = 1, from Proposition 1.13(6) we deduce that any approximant
β such that
h(β) > log 2 + h(α1) + c
1 + ε
satisﬁes the desired inequality.
Fix n ≥ 2. Assume by contradiction that the theorem is false for some ε0 > 0 and that the
counterexample is given by a sequence of approximants {βk} such that h(βk) → +∞. We apply
Lemma 5.3; so for any r0, r1 > 1 and ε < ε 0 there exist β(1), . . . , β(N) ∈ {βm} satisfying the properties
(1)-(3). Consider the matrix constructed with the vector β = (β(1), . . . , β(N)):
T (β ) =


α1 α1 . . . α 1
α2 α2 . . . α 2
...
...
...
...
αn αn . . . α n
β(1) β(2) . . . β (N)


Pick a constant:
L > log
(
42N!
n∏
i=1
H(αi)
2N !
n
)
We are ready to construct a function θ ∈ L1(S, µ) which will give the desired contradiction. We
deﬁne it as a piecewise function by putting for any ω ∈ Si:
θ|Si (ω) = min
k
− log− |β(k) − αi|ω
L + h(β(k)) = min
k
− log− |β(k) − αi|ω
h(β(k)) Ak
where Ak = 1 − L
L+h(β(k)) . Let’s ﬁx the set:
ˆSi := {ω ∈ Si : |β(k) − αi|ω < 1 , for k = 1, . . . , N}
and put ˆS =⋃ n
i=1
ˆSi; note that θ|S\ ˆS = 0. We can choose h(β(1)) ≫ L ≫ N > 212 log 2n in a way
that we can assume:
ε > 2
A1
+ 7√log 2n
A1
√
N
− 2 > 0 (43)
18
By using property (3) of Lemma 5.3 and ( 43) we get:
∫
ˆS
θdµ =
∫
S
θdµ =
n∑
i=1
∫
Si
θ|Si dµ > A 1
n∑
i=1
∫
Si
min
k
− log− |β(k) − αi|ω
h(β(k)) dµ(ω) >
> A 1 (2 + ε) > 2 + 7√log 2n√
N
. (44)
Now we want to show that we can apply Theorem 3.9.
• T (β ) satisﬁes the h-gap condition since we can choose the β(k) such that the heights h(β(k)) are
separated enough by property (2) of Lemma 5.3.
• Since |αi − β(k)|ω < 1 for ω ∈ ˆSi, the function θ is column bounding for T (β ) on ˆS. Indeed for
any k = 1, . . . , N and ω ∈ ˆSi we have that:
θ(ω) ≤ − log− |β(k) − αi|ω
L + h(β(k)) ≤ − log− |β(k) − αi|ω
log
(
42N!∏ n
i=1 H(αi)
2N !
n
)
+ h(β(k))
Therefore we can apply Theorem 3.9 to conclude that:
∫
ˆS
θdµ < 2 + 7√log 2n√
N
which contradicts inequality ( 44).
□
Note that in the proofs of Theorems (A) and (B) we didn’t assume Northcott property for our
adelic curve.
Example 5.4. Consider the adelic curve X = ( Q, Ω , id) naturally obtained from the ﬁeld K = Q
as in Example ( 1.4). We prove that the adelic curve X = ( Q, Ω , id) doesn’t satisfy the (strong)
µ-equicontinuity condition by showing that the generalised Roth’s theorem doesn’t hold.
The Thue equation X 3 − 2Y 3 = 1 has inﬁnitely many solutions ( xk, yk) =
(3√
2k3 + 1, k
)
for
k = 1 , 2, . . . in the algebraic integers. Note that by a theorem of Mahler su ch solutions cannot be
contained in a number ﬁeld (see for instance [ Zan09, Theorem 3.12]). Consider now the approximants
βk = xk
yk
= 3
√
2 + 1
k3 for α =
3√
2. First of all notice that
h
(
3
√
2 + 1
k3
)
= log k + O(1)
whereas by using the identity ζ 2
3 + ζ3 + 1 = 0 where ζ3 is a primitive cubic root of the unity we obtain
the following equality for the euclidean absolute value:
− log |βk − α| = − log
⏐⏐⏐⏐
xk −
3√
2yk
k
⏐⏐⏐⏐ = − log
⏐⏐⏐⏐
x3
k − 2y3
k
k(xk − ζ3
3√
2yk)(xk − ζ 2
3
3√
2yk)
⏐⏐⏐⏐ =
= log k + log
⏐⏐⏐xk − ζ3
3√
2yk
⏐⏐⏐+ log
⏐⏐⏐xk − ζ 2
3
3√
2yk
⏐⏐⏐ = 3 log k + O(1)
With the same strategy employed in the proof of Proposition 4.3 it is easy to show that these
calculations give a counterexample to Theorem (A) for the adelic curve X. Hence we conclude that
X cannot satisfy the (strong) µ-equicontinuity condition.
