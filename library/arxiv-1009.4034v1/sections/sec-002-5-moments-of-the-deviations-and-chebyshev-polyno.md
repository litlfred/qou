---
doc_id: arxiv-1009.4034v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 PIERRE-LOÏC MÉLIOT"
section_id: sec-002-5-moments-of-the-deviations-and-chebyshev-polyno
section_title: "Moments of the deviations and Chebyshev polynomials of the second kind"
section_number: 5
pages: 13-23
source_pdf: 1009.4034v1.pdf
source_sha256: 8f8d6d786b60c279
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 PIERRE-LOÏC MÉLIOT — In this article, we show that Kerov’s central limit theorem related to the ﬂuctuations of Young"
---
To make appear the Chebyshev polynomials of the second type, we start by computing the moments
of the deviation∆λ,c of a rescaled Young diagram from its limit shape. Ifλ is a partition of sizen, let
us denote by~qk,c(λ) the following quantity:
~qk,c(λ) = ~pk+1(λ)
(k + 1)nk/2−
⌊k+1
2 ⌋∑
l=1
k↓2l−1
(k + 1−l)l!l− 1!ck+1−2ln1/2
Because of the factorsn−k/2 and n1/2, ~qk,c is not contained in O, but is rather in the localized ring
O+ = O[Σ1
−1/2]. In [IO02], all the computations are done in this ring of generalized observables, and
using the so-called Kerov degree; as we shall see here, this complicated framework is not at all required
for the asymptotic analysis of ﬂuctuations of Plancherel (c = 0) and Schur-Weyl (c> 0) measures.
14 PIERRE-LOÏC MÉLIOT
Lemma 7. Letλ be a partition of sizen, and let us deﬁne the deviation∆λ,c by ∆λ,c(s) =λ∗(s)−Ωc(s).
Then, for anyk≥ 1, √n
2
∫
R
sk ∆λ,c(s)ds = ~qk+1,c(λ)
k + 1 .
Proof. Notice that this lemma is the exact analogue of [IO02, Proposition 7.2]. Besides, the proof is
exactly the same. Hence, by using the second part of Proposition 5, one gets:
~qk,c(λ) =
√n
k + 1
(~pk+1(λ)
n
k+1
2
−~pk+1(Ωc)
)
=√n
(~pk+1(λ∗)−~pk+1(Ωc)
k + 1
)
Then, ∆λ,c(s) =λ∗(s)− Ωc(s) = (λ∗(s)−|s|)− (Ωc(s)−|s|), so:
√n
2
∫
R
sk ∆λ,c(s)ds =√n
(∫
R
skσλ∗(s)ds−
∫
R
skσΩc(s)ds
)
=
√n
(k + 1)(k + 2)
(∫
R
sk+2σ′′
λ∗(s)ds−
∫
R
sk+2σ′′
Ωc(s)ds
)
=
√n
(k + 1)(k + 2)
(
~pk+2(λ∗)−~pk+2(Ωc)
)
= ~qk+1,c(λ)
k + 1
□
Proposition 8 (Asymptotic behaviour of linear functionals of the deviation). Letp(s) be a polynomial
in s. One choosesλ∈ Pn randomly according to the Schur-Weyl measure with parametersα = 1/2 and
c> 0. Then,
√n⟨p(s)| ∆λ,c(s)⟩ =√n
∫
R
p(s) ∆λ,c(s)ds
converges in law towards a centered (gaussian) random variable.
Proof. The important part of Proposition 8 is actually the fact that the limit random variable exists and
is centered, see the proof of Theorem 10 hereafter. Because of Theorem 6, for anyl≥ 2,
√n
(Rl(λ)
n
l
2
−cl−2
)
=√n (Rl(λ∗)−Rl(Ωc))
converges towards a centered gaussian variable, and the result is also true whenl = 1 (in this case the
variables are null for alln). Now, ifµ = (µ1,...,µ r) is a partition, then
√n (Rµ(λ∗)−Rµ(Ωc)) =
r−1∑
i=0
Rµ1...µr−i−1(λ∗)
[√n (Rµr−i(λ∗)−Rµr−i(Ωc))
]
Rµr−i+1...µr(Ωc).
Because of Theorem 1, eachRµ1...µr−i−1(λ∗) converges towards the constant variableRµ1...µr−i−1(Ωc), and
on the other hand, each diﬀerence
[√n (Rµr−i(λ∗)−Rµr−i(Ωc))
]
converges towards a centered gaussian
variable. Moreover, for these diﬀerences of free cumulants√n (Rl(λ∗)−Rl(Ωc)), one has in fact joint
convergence in ﬁnite-dimensional laws towards a centered gaussian process. Consequently, the limit of√n(Rµ(λ∗)−Rµ(Ωc)) is an element of a gaussian space whose variables are all centered:
∀µ, ∆n,c(Rµ) =√n (Rµ(λ∗)−Rµ(Ωc)) −→ N (0, (σµ,c)2)
In fact, the same argument as before shows that given a vector(∆n,c(Rµ(1)),..., ∆n,c(Rµ(s))) of such
ﬂuctuations, one has a joint convergence towards a gaussian vector. Since theRµ’s form a linear basis of
O, the same result holds for any vector(∆n,c(f(1)),..., ∆n,c(f(s))) of scaled ﬂuctuations of observables
of diagrams: it converges in law towards a centered gaussian vector. As Lemma 7 ensures that
√n
2
⟨
sk⏐⏐ ∆λ,c(s)
⟩
= ∆n,c(~pk+2)
(k + 1)(k + 2),
our claim is proved. □
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES 15
Lemma 9. With the same notations as in Lemma 7,
√n
2
∫
R
(s−c)k ∆λ,c(s)ds =
√n
(k + 1)(k + 2)

 ∑
2≤l≤k+2
(k + 2
l
)
(−c)k+2−l ~pl(λ)
nl/2 −
∑
2≤2m≤k+2
(k + 2
m
)
(−c)k+2−2m


Proof. Of course, one applies Newton’s binomial theorem in order to expand the power(s−c)k:
√n
2
⟨
(s−c)k⏐⏐ ∆λ,c(s)
⟩
=
k∑
l=0
(k
l
)
(−c)k−l
√n
2
∫
R
sl ∆λ,c(s)ds = 1
k + 1
k∑
l=0
(k + 1
l + 1
)
(−c)k−l~ql+1,c(λ)
= 1
k + 1
k+1∑
l=1
(k + 1
l
)
(−c)k+1−l~ql,c(λ)
=
( √n
(k + 1)(k + 2)
k+2∑
l=2
(k + 2
l
)
(−c)k+2−l ~pl(λ)
nl/2
)
−√nA (c)
where A(c) is the following quantity (one just uses the deﬁnition of~ql,c(λ)):
A(c) =
⌊k
2⌋+1∑
m=1
k+1∑
l=2m−1
k!
k + 1−l!l− 2m + 1!m!m− 1! (l + 1−m) (−1)k+1−lck+2−2m
=
⌊k
2⌋∑
m=0
k!
k− 2m!m!m + 1!
{k−2m∑
u=0
(k− 2m
u
) (−1)k−u−2m
u +m + 1
}
ck−2m
The term between brackets can be computed by writing 1
u+m+1 =
∫ 1
0 xu+mdx. So,
k−2m∑
u=0
(k− 2m
u
) (−1)k−u−2m
u +m + 1 =
∫ 1
0
k−2m∑
u=0
(k− 2m
u
)
(−1)k−u−2mxu+mdx
=
∫ 1
0
xm (x− 1)k−2mdx = (−1)k−2m k− 2m!m!
k−m + 1!
and consequently,A(c) =∑⌊k
2⌋
m=0
k!
k−m+1!m+1! (−c)k−2m = 1
(k+1)(k+2)
∑⌊k
2⌋
m=0
(k+2
m+1
)
(−c)k−2m, whence the
formula announced. □
In the following, we denote byUk(s) the Chebyshev polynomial of the second kind renormalized so
that Uk(2 cosθ) = sin(k+1)θ
sinθ . These polynomials satisfy the relation
Uk+2(X) =XUk+1(X)−Uk(X),
and the ﬁrst values areU0(X) = 0 , U1(X) = X, U2(X) = X2− 1, U3(X) = X3− 2X and U4(X) =
X4− 3X2 + 1. The end of this paragraph is devoted to the proof of the following theorem:
Theorem 10 (Linear functionals of the deviation associated to translated Chebyshev polynomials). For
any non-negative integerk,
√n
2 ⟨Uk(s−c)| ∆λ(s)⟩ is equal to
1
k + 1
k−1∑
l=0
(k + 1
l
)
(−c)lXk+1−l(λ),
plus some observables that under Schur-Weyl measures of parameter1/2 converge towards0 when n goes
to inﬁnity.
16 PIERRE-LOÏC MÉLIOT
Examples. Since the proof is quite tricky, we have found useful to include in our paper the complete
computations fork = 0, 1, 2, 3, 4 (one has to go up tok = 4 to see all the tricks). In particular, this will
make Lemma 12 much more natural. One will use the relations between the~p’s and theΣ’s presented
at the end of §2.
k = 0. Since ∆λ,c(s) is the diﬀerence between two normalized continuous Young diagrams,
⟨U0(s−c)| ∆λ,c(s)⟩ =⟨1| ∆λ,c(s)⟩ = 0,
and this agrees with the formula of Theorem 10.
k = 1. ⟨U1(s−c)| ∆λ,c(s)⟩ = ⟨s−c| ∆λ,c(s)⟩ = ⟨s| ∆λ,c(s)⟩ can be computed by using Lemma 7.
Thus,√n
2 ⟨U1(s−c)| ∆λ,c(s)⟩ = ~q2(λ)
2 = ~p3(λ)
6n − c√n
2 =
√n
2
(Σ2(λ)
n3/2 −c
)
= X2(λ)
2 .
k = 2. ⟨U2(s−c)| ∆λ,c(s)⟩ =
⟨
(s−c)2− 1
⏐⏐ ∆λ,c(s)
⟩
=
⟨
(s−c)2⏐⏐ ∆λ,c(s)
⟩
is the second translated
moment of the deviation, so it can be computed thanks to Lemma 9.√n
2 ⟨U2(s−c)| ∆λ,c(s)⟩ =
√n
12
(~p4(λ)
n2 − 4c~p3(λ)
n3/2 + 6c2~p2(λ)
n − 6− 4c2
)
=
√n
12
(4Σ3(λ)
n2 + 6Σ1,1(λ)
n + 2
n− 12cΣ2(λ)
n3/2 + 12c2− 6− 4c2
)
=
√n
3
(Σ3(λ)
n2 −c2
)
−c√n
(Σ2(λ)
n3/2 −c
)
− 1
3n1/2
= X3(λ)
3 −cX2(λ)− 1
3√n
Here, we’ve used the relation2 Σ1,1 = (Σ1)2−Σ1, and in general we shall use extensively the
factorization of symbolsΣµ in top homogeneous component.
k = 3. ⟨U3(s−c)| ∆λ,c(s)⟩ =
⟨
(s−c)3− 2(s−c)
⏐⏐ ∆λ,c(s)
⟩
is the diﬀerence of the third translated mo-
ment, minus two times the ﬁrst translated moment; this latter term will bring a contribution of
−X2. Then, by using again Lemma 9, one sees that
√n
2
⟨
(s−c)3⏐⏐ ∆λ,c(s)
⟩
is equal to
√n
20
(~p5(λ)
n5/2 − 5c~p4(λ)
n2 + 10c2~p3(λ)
n3/2 − 10c3~p2(λ)
n + 10c + 5c3
)
=
√n
20
(5Σ4(λ)
n5/2 + 20Σ2(λ)
n3/2 − 25Σ2(λ)
n5/2 − 20cΣ3(λ)
n2 + 20c
n + 30c2Σ2(λ)
n3/2 − 20c− 15c3
)
=
√n
4
(Σ4(λ)
n5/2 −c3
)
−c√n
(Σ3(λ)
n2 −c2
)
+
(3c2√n
2 +√n
)(Σ2(λ)
n3/2 −c
)
+ c√n− 5Σ2(λ)
4n2
= X4(λ)
4 −cX3(λ) + 3c2X2(λ)
2 +X2(λ) + c√n− 5Σ2(λ)
4n2 .
Again, we have used the relationΣ2,1 =Σ2Σ1−2Σ2. By adding the contribution−X2(λ), one re-
covers the formula of Proposition 10, becauseΣ2(λ) =O(n3/2) under a Schur-Weyl measure, and
as a consequence−5Σ2(λ)/4n2 =O(n−1/2)→ 0. In the general case, we shall use the weight ﬁl-
tration on observables to neglict some terms: indeed, for any observablef, the order of magnitude
is aO(nwt(f)/2), so one can for instance neglict terms of the kindf/nk/2 withk> wt(f). Notice
that there are some other simpliﬁcations in the calculation of
⟨
(s−c)3⏐⏐ ∆λ,c(s)
⟩
; essentially, they
are due to Lemma 8 that ensures that the mean of a scaled ﬂuctuation is asymptotically equal
to zero.
2Such a relation can be obtained if one considers the symbolsΣµ as elements of the algebra of partial permutations,
see [IK99]. As a consequence, any product of termsΣµ is a sum over certain partial matchingsM of symbolsΣρ(M ), see
[FM10, §3.3] for a precise statement.
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES 17
k = 4. Finally, another kind of trick has to be used in order to compute⟨U4(s−c)| ∆λ,c(s)⟩, and this
is due to the appearance of a termΣ2,2 in the expansion of~p6 in the basis of central characters.
Because of Lemma 9,
√n
2
⟨
(s−c)4⏐⏐ ∆λ,c(s)
⟩
is equal to
√n
30
(~p6(λ)
n3 − 6c~p5(λ)
n5/2 + 15c2~p4(λ)
n2 − 20c3~p3(λ)
n3/2 + 15c4~p2(λ)
n − 20− 15c2− 6c4
)
=
√n
30
(6Σ5(λ)
n3 + 30Σ3(λ)
n2 − 90Σ3(λ)
n3 + 15(Σ2(λ))2
n3 − 60
n + 42
n2
−30cΣ4(λ)
n5/2 − 120cΣ2(λ)
n3/2 + 150cΣ2(λ)
n5/2 + 60c2Σ3(λ)
n2 − 60c2
n − 60c3Σ2(λ)
n3/2 + 75c2 + 24c4
)
In order to simplify the calculations, we have used the relationsΣ1,1,1 = (Σ1)3− 3(Σ1)2 + 2Σ1,
Σ3,1 = Σ3Σ1− 3Σ3 and Σ2,2 = (Σ2)2− 4Σ3− 2(Σ1)2 + 2Σ1. Now, the new trick consists in
writing:
(Σ2(λ))2
n3 =
(Σ2(λ)
n3/2
)2
=
(Σ2(λ)
n3/2 −c
)2
+ 2c
(Σ2(λ)
n3/2 −c
)
+c2 = (X2(λ))2
n + 2cX2(λ)√n +c2
Multiplying by the factor√n, one sees that the term(X2(λ))2/√n will disappear in the limit
n→∞ , becauseX2(λ) =O(1). So, the previous expression may be written as:
X5(λ)
5 −cX4(λ) +
(
2c2 + 1
)
X3(λ)− (3c + 2c3)X2(λ)
+ (X2(λ))2
2√n + 5cΣ2(λ)
n2 − 3Σ3(λ)
n5/2 − 2 + 2c2
√n + 7
5n3/2
If one adds
√n
2
⟨
−3(s−c)2 + 1
⏐⏐ ∆λ,c(s)
⟩
in order to obtain
√n
2 ⟨U4(s−c)| ∆λ,c(s)⟩, one ﬁnally
gets
X5(λ)
5 −cX4(λ) + 2c2X3(λ)− 2c3X2(λ)
+ (X2(λ))2
2√n + 5cΣ2(λ)
n2 − 3Σ3(λ)
n5/2 − 1 + 2c2
√n + 7
5n3/2
and every term on the second line can be neglicted whenn goes to inﬁnity; on the other hand,
the ﬁrst line is precisely the formula of Theorem 10.
Now, we certainly have enough numerical evidences in order to believe in Theorem 10, and on the other
hand, we also have a precise idea of the technicities needed for a general proof.
Lemma 11. For any positive integerss≥l,
∑
|µ|=s
𝓁(µ)=l
1∏
i≥1mi(µ)! = 1
l!
(s− 1
l− 1
)
.
Similarly, given (random) variablesYp≥1, one has
∑
|µ|=s
𝓁(µ)=l
1∏
i≥1mi(µ)!
(∑
p∈µ
Yp
)
= 1
l− 1!
s−l∑
u=0
(l− 2 +u
u
)
Ys−l+1−u.
Proof. The ﬁrst formula is equivalent to
∑
|µ|=s
𝓁(µ)=l
( l
m1(µ),...,m s(µ)
)
=
(s− 1
l− 1
)
,
18 PIERRE-LOÏC MÉLIOT
and both sides of this equation correspond to the number ofl-uplets of positive integers(s1,...,s l) such
that s1 +··· +sl =s, so this is indeed true. As for the second formula, one sees that:
S2 =
∑
|µ|=s
𝓁(µ)=l
1∏
i≥1mi(µ)!
(∑
p∈µ
Yp
)
=
∑
|µ|=s
𝓁(µ)=l
1∏
i≥1mi(µ)!
(s−l+1∑
i=1
mi(µ)Yi
)
=
∑
|µ|=s
𝓁(µ)=l
s−l+1∑
i=1
1(∏
j≥1
j⁄=i
mj(µ)!
)
(max(0,mi(µ)− 1))!
Yi
because the biggest possible part of a partition of lengthl and sizes is s−l + 1. Then, by reverting the
order of summation, one obtains:
S2 =
s−l+1∑
i=1
Yi


∑
|µ|=s−i
𝓁(µ)=l−1
1∏
i≥1mi(µ)!

 = 1
l− 1!
s−l+1∑
i=1
(s−i− 1
l− 2
)
Yi,
and this is exactly the second formula up to the change of indexu =s−l + 1−i. □
Lemma 12. Fix a parameterc> 0, and a positive integerk. The scaled observable~pk(λ)/n
k−1
2 is equal
to
√n


⌊k
2⌋∑
l=1
k!
(k−l)k− 2l!l− 1!l!ck−2l

 +
⌊k
2⌋∑
l=1
k!
k−l!l− 1!
(k−2l∑
u=0
(l− 2 +u
u
)
cuX1+k−2l−u
)
,
plus a random variable Vk(c) that under the Schur-Weyl measures SWn,1/2,c converges in probability
towards a constantLk(c) as n goes to inﬁnity.
Proof. Because of Proposition 2, one can write
~pk =

 ∑
|µ|+𝓁(µ)=k
k↓𝓁(µ)
∏
i≥1mi(µ)!
∏
i≥1
(Σi)mi

 +Dk−1,
where Dk−1 is an observable of weightk− 1. Let us decomposeDk−1 in the basis of free cumulants:
Dk−1 =
∑
|µ|≤k−1
m1(µ)=0
dµ,kRµ
Then, one knows that Rµ/n|µ|/2 converges in probability towardsc|µ|−2𝓁(µ), so Vk(c) = Dk−1/n
k−1
2
converges in probability to
Lk(c) =
∑
|µ|=k−1
m1(µ)=0
dµ,kc|µ|−2𝓁(µ).
We won’t need the precise value ofLk(c), so let us focus on the remaining part~pk−Dk−1. One uses the
same trick as for the term(Σ2)2 in the expansion of~p6/n5/2:
~pk−Dk−1
n
k−1
2
=√n

 ∑
|µ|+𝓁(µ)=k
k↓𝓁(µ)
∏
i≥1mi(µ)!
∏
i≥1
( Σi
n
i+1
2
)mi(µ)


=√n

 ∑
|µ|+𝓁(µ)=k
k↓𝓁(µ)
∏
i≥1mi(µ)!
∏
i≥1
(Xi√n +ci−1
)mi(µ)


KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES 19
With µ ﬁxed, one expands the product∏
i≥1
(
Xi√n +ci−1
)mi(µ)
; the two leading terms are
A(µ) +B(µ)√n =c|µ|−𝓁(µ) + 1√n
∑
p∈µ
Xpc|µ|−𝓁(µ)−p+1,
and the remainder is aO(n−1). So,
~pk−Dk−1
n
k−1
2
=√n

 ∑
|µ|+𝓁(µ)=k
k↓𝓁(µ)A(µ)∏
i≥1mi(µ)!

 +

 ∑
|µ|+𝓁(µ)=k
k↓𝓁(µ)B(µ)∏
i≥1mi(µ)!

 +O(n−1/2).
The ﬁrst part is equal to
√n


⌊k
2⌋∑
l=1
∑
µ∈Pk−l
|µ|=l
k!
k−l!
ck−2l
∏
i≥1mi(µ)!

 =√n


⌊k
2⌋∑
l=1
k!
(k−l)k− 2l!l− 1!l!ck−2l


because of the ﬁrst part of Lemma 11. As for the second part, we setYp = Xp/cp−1 and we apply the
second part of Lemma 11, so we obtain
⌊k
2⌋∑
l=1
∑
µ∈Pk−l
𝓁(µ)=l
∑
p∈µ
k!
k−l!
ck−2lYp∏
i≥1mi(µ)! =
⌊k
2⌋∑
l=1
k!
k−l!l− 1!
(k−2l∑
u=0
(l− 2 +u
u
)
Y1+k−2l−u
)
ck−2l.
Since Y1+k−2l−uck−2l =X1+k−2l−ucu, the proof is achieved. □
Lemma 13. Up to a random variable that converges in probability to zero under the Schur-Weyl measures
SWn,1/2,c, the translatedk-th moment of the deviation
√n
2
∫
R (s−c)k ∆λ,c(s)ds is equal to
1
k + 1
k−1∑
l=0


⌊l
2⌋∑
m=0
(k + 1
m
)(k + 1− 2m
l− 2m
)
(−c)l−2m

Xk+1−l(λ).
Proof. Because of Lemma 9 and Lemma 12, the translatedk-th moment of the deviation is the combi-
nation of the following terms:
A =√n

 ∑
2≤l≤k+2
⌊l
2⌋∑
m=1
k!
(l−m)k + 2−l!l− 2m!m− 1!m! (−1)k+2−lck+2−2m


B =
∑
2≤l≤k+2
⌊l
2⌋∑
m=1
l−2m∑
u=0
k!
k + 2−l!l−m!m− 1!
(m− 2 +u
u
)
(−1)k+2−lck+2−l+uX1+l−2m−u
C =
∑
2≤l≤k+2
k!
l!k + 2−l! (−c)k+2−lVl(c)
D =−√n

 ∑
2≤2m≤k+2
k!
m!k + 2−m! (−c)k+2−2m


In A, we revert the order of summation:
A√n =
∑
2≤2m≤k+2
k!
m!k + 2− 2m!m− 1!(−c)k+2−2m
{k+2∑
l=2m
(−1)l k + 2− 2m!
(l−m)k + 2−l!l− 2m!
}
20 PIERRE-LOÏC MÉLIOT
The sum between brackets can be written as:
k+2−2m∑
u=0
(k + 2− 2m
u
) (−1)u
u +m =
∫ 1
0
(k+2−2m∑
u=0
(k + 2− 2m
u
)
(−x)u
)
xm−1dx
=
∫ 1
0
(1−x)k+2−2mxm−1dx = k + 2− 2m!m− 1!
k + 2−m!
Hence, A +D = 0. Then, B is asymptotically a centered gaussian variable, andC converges towards∑
2≤l≤k+2
k!
l!k+2−l! (−c)k+2−lLl(c). But because of Proposition 8, the translated k-th moment of the
deviation converges in law towards a centered gaussian variable, so
∑
2≤l≤k+2
k!
l!k + 2−l! (−c)k+2−lLl(c) = 0
(this is why we did not need the precise values of theLl(c)’s). Finally, one can simplifyB as follows. The
index 1 +l−2m−u takes its values in the interval[ [1,k + 1] ], soB can be written as a linear combination∑k+1
v=1f(v,c )Xv. SinceX1 = 0, one can actually takev in [ [2,k + 1] ], so let us make the change of index
1 +l− 2m−u =k + 1−x with x∈ [ [0,k− 1] ]. Then,
B =
k−1∑
x=0
Xk+1−x


∑
k+2≥l≥2m≥2
l−2m≥k−x
(−1)k+2−lcx−2m+2k!l−m−k +x− 2!
k + 2−l!l−m!m− 1!m− 2!l− 2m−k +x!


=
k−1∑
x=0
Xk+1−x


⌊x
2⌋∑
y=0
x−2y∑
z=0
(−1)x−2y−zcx−2yk!y +z− 1!
y!y− 1!z!k + 1−x +y +z!x− 2y−z!


with y =m− 1 and z =l− 2m−k +x. Then we use another hypergeometric identity
Z∑
z=0
α +z!
β +z!
(Z
z
)
(−1)z = α!β−α +Z− 1!
β−α− 1!β +Z!
that holds for anyβ > α, and that can again be shown by using methodsà la Wilf-Zeilberger, see
[PWZ97]. It implies that:
B =
k−1∑
x=0
Xk+1−x


⌊x
2⌋∑
y=0
(−c)x−2yk!
y!y− 1!x− 2y!
Z=x−2y∑
z=0
y− 1 +z!
y +k + 1−x +z!
(Z
z
)
(−1)z


=
k−1∑
x=0
Xk+1−x


⌊x
2⌋∑
y=0
(−c)x−2yk!k + 1− 2y!
y!x− 2y!k + 1−x!k + 1−y!


= 1
k + 1
k−1∑
x=0
Xk+1−x


⌊x
2⌋∑
y=0
(k + 1
y
)(k + 1− 2y
x− 2y
)
(−c)x−2y


Notice that a slight abuse of notation has been made when considering expressions such asy− 1! with
y = 0; nethertheless, it can be checked that in the end our formal computation does give the exact
result. □
Proof of Theorem 10.The explicit expansion ofUk(X) is
Uk(X) =
⌊k
2⌋∑
m=0
(−1)m
(k−m
m
)
Xk−2m
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES 21
see [IO02, p. 33]. Moreover, given two set of variables a0,a 1,... and b0,b 1,... , the following set of
relations are equivalent


bk =
⌊k
2⌋∑
m=0
(k
m
)
ak−2m



k≥0
⇐⇒


ak =
⌊k
2⌋∑
m=0
(−1)m k
k−m
(k−m
m
)
bk−2m



k≥0
see [IO02, p. 36]. We denote byBk+1
k+1 the random variable computed in the previous lemma. Then, the
linear functional of the deviation associated to the translated Chebyshev polynomialUk(s−c) is:
√n
2 ⟨Uk(s−c)| ∆λ,c(s)⟩ =
⌊k
2⌋∑
m=0
(−1)m
(k−m
m
) Bk+1−2m
k + 1− 2m =
⌊k
2⌋∑
m=0
(−1)m
(k + 1−m
m
) Bk+1−2m
k + 1−m
Since B0 = B1 = 0, the indexm can in fact be taken up to⌊k+1
2 ⌋, so the expression is exactlyAk+1
k+1 ,
where theA’s and theB’s are related as mentioned before. Consequently, it is suﬃcient to identify the
random variablesAk such that:
∀k,
k−1∑
l=0


⌊l
2⌋∑
m=0
(k + 1
m
)(k + 1− 2m
l− 2m
)
(−c)l−2m

Xk+1−l =
⌊k+1
2 ⌋∑
m=0
(k + 1
m
)
Ak+1−2m
In the left-hand side, we revert the order of summation and thus obtain:
Bk+1 =
⌊k−1
2 ⌋∑
m=0
(k + 1
m
)(k−1∑
l=2m
(k + 1− 2m
l− 2m
)
(−c)l−2mXk+1−l
)
=
⌊k−1
2 ⌋∑
m=0
(k + 1
m
)(k−1−2m∑
l=0
(k + 1− 2m
l
)
(−c)lXk+1−2m−l
)
=
⌊k+1
2 ⌋∑
m=0
(k + 1
m
)(k−1−2m∑
l=0
(k + 1− 2m
l
)
(−c)lXk+1−2m−l
)
because X0 =X1 = 0.
As a consequence,
Ak+1 =
k−1∑
l=0
(k + 1
l
)
(−c)lXk+1−l,
and since Ak+1
k+1 =
√n
2 ⟨Uk(s−c)| ∆λ,c(s)⟩, the proof of Theorem 10 is completed. □
6. An extension of Kerov’s central limit theorem
Let us denote by(Xk,∞)k≥2 the limit in law of the random process(Xk)k≥2 under the Schur-Weyl
measures SWn,1/2,c; the covariance matrix of this centered gaussian process has been computed in §4.
One sees easily that in the gaussian space generated by the process(Xk,∞)k≥2, the orthogonal basis
deduced from (Xk,∞)k≥2 by performing the Gram-Schmidt orthogonalisation procedure is:
Yk,∞ =
k−2∑
l=0
(k
l
)
(−c)lXk−l,∞
As a consequence, the joint limit in law of the random variables(
√n
2 ⟨Uk(s−c)| ∆λ,c(s)⟩)k≥1 is simply
(Yk+1,∞
k+1 )k≥1. So, Theorem 10 can be restated in the following way:
22 PIERRE-LOÏC MÉLIOT
Theorem 14 (Central limit theorem for Schur-Weyl measures). Under the measures SWn,1/2,c, the
random process of scaled deviations
(√n
2 ⟨Uk(s−c)| ∆λ,c(s)⟩
)
k≥1
converges in ﬁnite dimensional laws towards a gaussian process(ξk+1)k≥1 whose coordinatesξk+1 are
independant normal variables of mean0 and variance1/(k+1). Consequently, in the interval[c−2,c +2],
the scaled deviation
√n
2 ∆λ,c(s) converges in distribution towards the generalized gaussian process
∆c(s) = ∆c(c + 2 cosθ) = 1
π
∞∑
k=2
ξk
k sin(kθ).
Hence, Kerov’s central limit theorem as enounced in [IO02] for Plancherel measures also holds for Schur-
Weyl measures, with exactly the same limit up to a translation on thex-axis. In other words, Kerov’s
gaussian process has a universality property. It would be very interesting to extend this universality
property further; as for now, it looks more as a miracle of computations than as a profound result about
random partitions.
Figure 8. Partial sum of the 5000 ﬁrst terms of the random serie that deﬁnes the
limiting gaussian process associated to the deviations∆λ,c(s).
Notice that the random serie∆c(s) does not converge ponctually — this is the same phenomenon as
for the well-known free gaussian ﬁeld, see [She07] and also our ﬁgure 8. However, it makes sense as a
distribution, meaning that for any functionf∈ C∞([c− 2,c + 2]),
√n
2 ⟨f(s)| ∆λ,c(s)⟩→ 1
π
∞∑
k=2
ξk
k
(∫ c+2
c−2
f(s) sin(kθ(s))ds
)
,
where the right-hand side converges with probability1.
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES 23
Proof. The ﬁrst part has just been proved (setξk+1 = Yk+1,∞
k+1 ), and for the second part, it is exactly the
same discussion as in [IO02, §9]. □
