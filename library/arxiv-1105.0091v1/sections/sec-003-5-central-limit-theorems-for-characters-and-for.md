---
doc_id: arxiv-1105.0091v1
doc_title: "E-mail: meliot@phare.normalesup.org"
section_id: sec-003-5-central-limit-theorems-for-characters-and-for
section_title: "Central limit theorems for characters and for partitions"
section_number: 5
pages: 36-42
source_pdf: 1105.0091v1.pdf
source_sha256: 7d6f72e016b25027
doc_brief: "E-mail: meliot@phare.normalesup.org — In this paper, we review the representation theory of the inﬁnite symmetric group, and we extend the works of Kerov and Vershik by proving that the irreducible"
---
In the previous paragraph, it was shown that all the coherent systems of
measures (Pn,ω)n∈N have a property of concentration, that can be seen at the
level of characters or directly for the geometry of the random partitions. In this
section, we shall prove that the concentration is always gaussian, which is quite
a striking fact. However, the geometric version of our central limit theorem will
be a little less precise than the algebraic one: indeed, one cannot study with
our method of moments the ﬂuctuations of rows or columns corresponding to
equal coordinates of the pointω of the Thoma simplex. This will be done in
§6 by entirely diﬀerent methods, that relie essentially on the interpretation of
the measures Pn,ω as push-forwards of the measuresQn,ω.
A central limit theorem for the characters ofS∞ and H (S∞) 37
5.1 Central limit theorem for the irreducible characters
In this paragraph, we ﬁx permutationsσ(1),...,σ (r)∈ S∞ of cycle types
µ(1),...,µ (r); the partitionsµ(i) are all deﬁned up to parts of size1, but this
will not change our results. For convenience, we shall denotepµ(A−B +γE ) =
pµ(ω).
Theorem 17. We consider the random vector(∆n,ω(σ(1)),...,∆ n,ω(σ(r))),
with
∆n,ω(σ) =√n
(
χλ(σ)−χω(σ)
)
andλ chosen randomly according toPn,ω. Asn goes to inﬁnity, this vector con-
verges in joint law to a centered gaussian vector(∆∞,ω(σ(1)),...,∆ ∞,ω(σ(r))),
and the covariance matrix of this vector is:
k(∆∞,ω(σ(i)),∆∞,ω(σ(j)))
=
∑
a∈µ(i), b∈µ(j)
ab pµi⊔µj\{a,b}(ω) (pa+b−1(ω)−pa(ω)pb(ω)).
In particular,k(∆∞,ω(σ),∆∞,ω(τ )) = lm (pl+m−1(ω)−pl(ω)pm(ω)) if σ and
τ are cycles of lengthsl and m.
Proof. For any partitionµ,
√n
(
χλ(µ⊔ 1n−|µ|)−pµ(ω)
)
=√n
(Σµ(λ)− En,ω[Σµ]
n|µ|
)
+O
( 1√n
)
,
so it is suﬃcient to show that the random vector
V =√n
(Σµ(1)
n|µ(1)|,..., Σµ(r)
n|µ(r)|
)
convergestoagaussianvectorwiththeannouncedcovariancematrix.However,
for s≥ 3, by using Theorem 12, one sees that
kn,ω
(
Σµ(i1 ),...,Σ µ(is )
)
=O
(
n|µ(i1 )|+···+|µ(is )|−s+1
)
kn,ω
(√n Σµ(i1 )
n|µ(i1 )|,..., √n Σµ(is )
n|µ(is )|
)
=O
(
n1−s
2
)
→ 0.
Thus, V converges indeed towards a gaussian vector. To compute the covari-
ances, we use the following trick:
kn,ω(Σµ,Σν) = En,ω[ΣµΣν]− En,ω[Σµ] En,ω[Σν]
= En,ω[ΣµΣν−Σµ⊔ν] +
(
En,ω[Σµ⊔ν]− En,ω[Σµ] En,ω[Σν]
)
.
38 Pierre-Loïc Méliot
The term of higher degree in the ﬁrst part of the right-hand side is exactly the
expectation of the subdominant term of a productΣµΣν. We have calculated
this subdominant term after Proposition 10; hence,
En,ω[ΣµΣν−Σµ⊔ν] =
∑
a∈µ,b∈ν
ab En,ω[Σ(µ⊔ν⊔{a+b−1})\{a,b}]
≃

 ∑
a∈µ,b∈ν
ab pµ⊔ν\{a,b}(ω) pa+b−1(ω)

n|µ|+|ν|−1.
On the other hand,En,ω[Σµ⊔ν]− En,ω[Σµ] En,ω[Σν] is easily computed to be
equal to
pµ⊔ν(ω)
[
n↓|µ|+|ν|−n↓|µ|n↓|ν|
]
≃−| µ||ν| pµ⊔ν(ω) n|µ|+|ν|−1
Dividing everything byn|µ|+|ν|−1 and writing
|µ||ν| pµ⊔ν(ω) =
∑
a∈µ,b∈ν
ab pµ⊔ν\{a,b}(ω) pa(ω)pb(ω),
we obtain exactly the announced formula.
So, for any integerk≥ 2, ifσ is ak-cycle, then
√n
(χλ(σ)−χω(σ)
k
)
converges under the laws Pn,ω to a centered gaussian variable of variance
p2k−1(ω)−pk(ω)2. Again, this result is not precise enough whenω = 0 —
fortunately, this is the only problematic point. Actually, it has been shown in
[IO02, Theorem 6.1] that under Plancherel measures, ifσ is ak-cycle, then
n
k
2
(χλ(σ)√
k
)
converges to a centered gaussian variable of variance1. We shall say a little
bit more on these kind of results in the conclusion of our paper.
5.2 Gaussian behaviour of the rows and of the columns
Now, let us look at the consequences of Theorem 17 for the geometry of
the random partitions. First, let us give a central limit theorem for the ran-
dom measuresXλ under coherent systems of probability measures(Pn,ω)n∈N.
In the following,C 1([−1, 1]) is endowed with the topology of uniform conver-
gence of the functions and of their derivatives, and measures are now consid-
ered as elements of the dual space ofC 1([−1, 1]) — this dual space contains
P([−1, 1])⊂ M ([−1, 1]) = C 0([−1, 1])∗.
A central limit theorem for the characters ofS∞ and H (S∞) 39
Theorem 18. We consider the random measure∇n,ω =√n (Xλ−Xω), with
λ chosen randomly according toPn,ω. As n goes to inﬁnity,∇n,ω converges
to a centered gaussian element∇∞,ω in C 1([−1, 1])∗, and for any functions
f,g ∈ C 1([−1, 1]),
k(∇∞,ω(f ),∇∞,ω(g)) = Xω((xf (x))′(xg(x))′)−Xω((xf (x))′)Xω((xg(x))′).
Proof. Wehaveshowninour“algebraic” centrallimittheoremthattherandom
vector (√n
(Σk
nk−pk(ω)
))
k≥1
converges to a centered gaussian vector with covariance matrix
lm (pl+m−1(ω)−pl(ω)pm(ω)).
By using the same arguments as before, one can replaceΣk bypk, and there-
fore, the same results holds for
(√n
(pk(λ)
nk −pk(ω)
))
k≥1
=
(√n
(
Xλ(xk)−Xω(xk)
))
k≥0
= (∇n,ω(xk))k≥0,
although with a shift of index:
k(∇∞,ω(xl),∇∞,ω(xm)) = (l + 1)(m + 1) (pl+m+1(ω)−pl+1(ω)pm+1(ω)).
Now, this computation of covariances can be rewritten as:
k(∇∞,ω(xl),∇∞,ω(xm)) = (l + 1)(m + 1) (Xω(xlxm)−Xω(xl)Xω(xm))
=Xω((xl+1)′(xm+1)′)−Xω((xl+1)′)Xω((xm+1)′).
By multilinearity, for any polynomialsf and g in R[x],∇n,ω(f ) and∇n,ω(g)
converge towards centered gaussian variables, and the covariance of the limit-
ing distibutions writes as
k(∇∞,ω(f ),∇∞,ω(g)) = Xω((xf (x))′(xg(x))′)−Xω((xf (x))′)Xω((xg(x))′).
Finally, one uses the density ofR[x] in C 1([−1, 1]) to get the same result for
any functionsf,g ∈ C 1([−1, 1]). However, notice that one has ﬁrst to apply
a random version of the Banach-Steinhaus theorem for the (random) linear
forms∇n,ω : C 1([−1, 1])→ R (see [Tha87] or [VV95]). Indeed, because of
the factor√n, it is not cleara priori that one can get a uniform bound on
expressions like √n (Xλ(f−fk)−Xω(f−fk))
with (fk)k∈N sequence of polynomials approximatingf in C 1([−1, 1]) — this
point was left unexplained in [FM10].
40 Pierre-Loïc Méliot
Unfortunately, Theorem 18 is suﬃcient to describe the ﬂuctuations of the
row λi or the columnλ′
j only whenαi−1 > αi > αi+1 or whenβj−1 > βj >
βj+1. Indeed, our method of moments will not allow to distinguish at order√n the parts corresponding to equal coordinates. We ﬁx distinct coordinates
αi1⁄=αi2⁄=···⁄ =αir⁄= 0 and βj1⁄=βj2⁄=···⁄ =βjs⁄= 0 of the pointω∈Ω,
and we denote bymk (respectively,wk) the multiplicity ofαik (resp., ofβjk),
so
αik−1 >α ik =αik+1 =··· =αik+mk−1 >α ik+mk
and similarly forβjk. We then denote
Λik,mk,n =√n
(λik
n + λik+1
n +··· + λik+mk−1
n −mkαik
)
;
Λ′
jk,wk,n =√n
(λ′
jk
n + λ′
jk+1
n +··· + λ′
jk+wk−1
n −wkβjk
)
.
Theorem 19. As n goes to inﬁnity, the random vector
(Λi1,m1,n,...,Λ ir,mr,n,Λ′
j1,w1,n,...,Λ ′
js,ws,n)
converges to a centered gaussian vector(Λi1,m1,∞,...,Λ ′
js,ls,∞), with the fol-
lowing covariances:
k(Λik,mk,∞,Λil,ml,∞) = δklmkαik−mkmlαikαil ;
k(Λ′
jk,wk,∞,Λ′
jl,wl,∞) = δklwkβjk−wkwlβjkβjl ;
k(Λik,mk,∞,Λ′
jl,wl,∞) =−mkwlαikβjl.
In particular, ifαi and αj are two “isolated” coordinates of the sequenceα,
then the random variablesXi,n =√n
(λi
n−αi
)
and Xj,n =√n
(
λj
n −αj
)
converge jointly in law to centered gaussian variablesXi,∞ and Xj,∞, with
k(Xi,∞,Xj,∞) = δijαi−αiαj.
Proof. We consider test functionsfk and gl such that:
1. All these functions are inC 1([−1, 1]), non-negative and with values in[0, 1].
2. Forany k,thereisaneighbourhood Wk = [αik−εk,αik +εk]ofαik suchthat
Wk does not contain any element of the set{αi≥1,−βj≥1, 0}\{ αik}, and
the support offk is contained inWk. Moreover, there is a neighboorhood
Vk⊂Wk of αik such thatf|Vk = 1.
3. Similarly, for anyl, there is a neighbourhoodW′
l = [−βjl−ε′
l,−βjl +ε′
l] of
−βjl such thatW′
l does not contain any element of{αi≥1,−βj≥1, 0}\{βjl},
and the support ofgl is contained inW′
l. Moreover, there is a neighboor-
hood V′
l ⊂W′
l of−βjl such thatg|V′
l
= 1.
A central limit theorem for the characters ofS∞ and H (S∞) 41
−1 10 αikαik +mk αik −1
fk
4
Fig. 4 Test functions for the proof of the geometric central limit theorem.
We ﬁx an indexk. Since λi
n → αi for alli, with probability going to1 as n
goes to inﬁnity, the intersection of the support ofXλ withWk consists exactly
in {λik
n ,λik+1
n ,..., λik+mk−1
n
}
,
that are even inVk with big probability. So,
Xλ(fk) = λik +λik+1 +··· +λik+mk−1
n
with probability going to1; on the other hand,Xω(fk) = mkαik. Hence,
Λik,mk,n =∇n,ω(fk)
for anyk with probability going to1; similarly,Λ′
jl,wl,n =∇n,ω(gl) with big
probability. Then, by Theorem 18, the random vector of the statement of our
theorem converges in law to a centered gaussian vector
(Λi1,m1,∞,...,Λ ir,mr,∞,Λ′
j1,l1,∞,...,Λ ′
js,ls,∞),
with k(Λik,mk,∞,Λil,ml,∞) equal to
Xω((xfk(x))′(xfl(x))′)−Xω((xfk(x))′)Xω((xfl(x))′),
andthesamekindofformulawithvariables Λ′
jk,wk,∞.Now,noticethat f′
k(x) =
0 for anyx in the support ofXω, and anyk. Hence, the previous covariance
may be written as
Xω(fkfl)−Xω(fk)Xω(fl) = δklmkαik−mkmlαikαil,
and the proof for the other covariance formulas is the same with functionsgl
instead of functionsfk.
42 Pierre-Loïc Méliot
