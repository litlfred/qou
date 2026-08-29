---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd"
section_id: sec-002-12-set-up
section_title: "Set-up"
section_number: 1.2
pages: 2-4
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd — Given a uniform random"
---
Ulam’s problem is a problem that involves a combination of tools and tech niques from the intersection of
various subﬁelds and specialities in mathematics, statistics and phys ics. It has been studied by many top
researchers. The main results are beautiful but diﬀﬁcult.
The depth of the results related to Ulam’s problem is well-known. Ther e are good reviews. See, for
example, the review article of Aldous and Diaconis [5]. Many new and impo rtant results have been discovered
since the publication of that particular paper. One notable recent d evelopment is the directed landscape
perspective [12].
We will state the actual problem known as Ulam’s problem. Let π be a random permutation in Sn, chosen
according to the uniform measure. So for any permutation in Sn, the probability for π to equal that one
permutation is 1/n!. Ulam’s problem involves increasing subsequences for π. Given a cardinality k subset of
{1,...,n }, we may write the set as {i1,...,i k} for
1≤i1<··· <i k≤n. (1)
Then we say that ( i1,...,i k) is an increasing subsequence for π if
πi1 < ... < πik. (2)
If we ﬁx (i1,...,i k) and vary overπ, then the probability of the event, “(i1,...,i k) is an increasing subsequence
for π,” is equal to 1 /k!. This is because if we are given k numbers{j1,...,j k} satisfying
1≤ j1 < ... < jk ≤ n, (3)
and we are told that we have equality of the sets
{πi1,...,π ik} ={j1,...,j k}, (4)
then there are still k! possible permutations σ = (σ1,...,σ k)∈Sk such that
∀r∈{ 1,...,k }, we have πir =jσr. (5)
But for ( i1,...,i r) to be an increasing subsequence for π, then we want πir = jr for all r. That means
σ = (1, 2,...,k ), the identity element of Sk, which is just one of the k! possible permutations.
Ulam’s problem is to determine the distribution of L(n), the length of the longest increasing subsequence
for π: the largest k such that there is at least one subsequence ( i1,...,i k) which is increasing for π. Ham-
mersley used Markov’s bound and Kingman’s subadditive theorem to g arner information about L(n) in the
large n limit. Let Zn,k(π) denote the number of subsequences of cardinality k which are increasing for π:
Zn,k(π) =
n∑
i1,...,ik=1
n−1∏
r=1
(
1(0,∞)(ir+1−ir)· 1(0,∞)(πir+1−πir )
)
. (6)
Then∑ n
i1,...,ik=1
∏ n−1
r=1 1(0,∞)(ir+1−ir) is equal to n-choose-k, and for each ( i1,...,i k) we know
P(πi1 <··· <π ik ) = 1
k!, (7)
where the probability is over the uniform measure on π∈Sn (with (i1,...,i k) held ﬁxed). Therefore,
E[Zn,k] =
(n
k
)
· 1
k!. (8)
2
Then, using Markov’s inequality, it is easily seen that
P(Zn,k > 0) = P(L(n)≥k)≤ E[Zn,k]. (9)
Then, by Stirling’s formula, writing x for k/√n,
(n
k
)
· 1
k! ∼ exp
(
−2xn1/2 ln (x/e)− 1
2x2 +δn(x)
)
2πxn1/2(1−xn−1/2)1/2 , (10)
in the limit k→∞ , n−k→∞ , where
δn(x) = xn1/2 ln
(
1−xn−1/2
)
−n ln
(
exn− 1/ 2(
1−xn−1/2
))
+ x2
2 , (11)
which would be o(1) as long as xn−1/2 =o(1). In [18], Hammersley used the subadditive ergodic theorem to
prove that
lim inf
n→∞
n−1/2 E[Ln] = lim sup
n→∞
n−1/2 E[Ln] = c, (12)
for some number c which a priori could have been in (0 ,∞]. But by equation (10), he noted c≤e. In fact,
an equally simple argument using the Erd¨ os-Szekeres theorem give sc≥ 1/2. See, for example, Section 1.4 of
J.M. Steele’s monograph [33].
The actual mean is approximately cn 1/2 forc = 2, by a result of Vershik and Kerov [35], and a partial result
of Logan and Shepp [20]. Moreover, there is a complete characteriz ation of the leading-order ﬂuctuations for
largen, according to the Baik-Deift-Johannson theorem [9]. And new resu lts are being continually discovered
for the leading-order ﬂuctuations, such as the “directed landsca pe” picture [12].
1.3 Higher moments for the generalized Ulam’s problem
Suppose one seeks information for the distribution of Zn,k. The event that Zn,k > 0 is equal to the event that
Ln≥k. Thus, ﬁnding the distribution of Zn,k generalizes Ulam’s problem, so it can be called the “generalized
Ulam problem.” The easy bounds above for the event Zn,k > 0 follows from Markov’s bounds. But more
precise bounds could in principle be obtained if we knew higher moments of Zn,k.
In principle, the Bonferroni inequalities would give sharp bounds if on e had suﬃcient information on the
moments. A good reference for this topic is the combinatorics text book of Charalambides [11]. In Appendix
A we will review this. The ﬁrst author, Samen Hossein, has an earlier u npublished article, submitted to a
private organization, which treats this topic in more detail. That is av ailable upon request. But, we will
summarize it in the appendix. Because of all this, it is interesting to kn ow the distribution of Zn,k, beyond
just its mean.
In [28], Pinsky investigated the second moment. He obtained an exac t combinatorial formula. He then
rigorously analyzed the formula obtaining upper and lower bounds of matching exponential growth rates
although with diﬀerent constant multipliers.
Proposition 1.1 (Pinsky’s First Result) If there is a sequence kn such that limn→∞kn/n2/5 = 0 then
E[Z 2
n,kn]
(
E[Zn,kn ]
)2− 1 = O
(
k5/2
n
n
)
. (13)
If instead lim infn→∞kn/n2/5> 0 and lim supn→∞kn/n2/5<∞ then
0 < lim inf
n→∞
E[Z 2
n,kn ]
(
E[Zn,kn]
)2 ≤ lim sup
n→∞
E[Z 2
n,kn]
(
E[Zn,kn]
)2 <∞. (14)
If limn→∞n2/5/kn = 0 then (
E[Zn,kn ]
)2
E[Z 2
n,kn] =O
( n
k5/2
n
)
. (15)
Using this, he could determine exactly the criteria for the Paley-Zyg mund second moment method to guarantee
thatZn,k satisﬁes a weak law of large numbers type result. Namely, that cond ition is that lim n→∞kn/n2/5 = 0.
Pinsky noted that just because the Paley-Zygmund method does n ot imply a weak law, that does not
mean that a weak law may not still be true, since it does not necessar ily require vanishing of the variance of
3
the rescaled quantity. So in [29], Pinsky proved a threshold to be ab le to disprove a weak law for Zn,k. He
showed
∀ǫ> 0, lim
n→∞
1
n!
⏐
⏐
⏐
⏐
{
π∈Sn :
⏐
⏐
⏐
⏐
Zn,kn(π)
E[Zn,kn]− 1
⏐
⏐
⏐
⏐<ǫ
}⏐
⏐
⏐
⏐ = 1 ⇒ lim inf
n→∞
n4/9
kn
> 0. (16)
He also proved interesting equivalent formulations of his questions, and he has conjectures which remain as
fascinating open problems.
We may follow the paradigm of iterating a random optimization problem. See for example the objective
method of Aldous and Steele [6]. Especially, see the section on the “Stalking h orse,” and distributional
identities. For the higher moments of the generalized Ulam problem, t he stalking horse is the covariance or
even just the mixed moments
Qn(k,ℓ ) = E[Zn,kZn,ℓ].
This seems to be the ﬁrst step towards iterating to go from the sec ond moment to higher moments. For
example, for the third moment E[Zn,k(Zn,k)2], we may want to start with Qn(k, 2k). More precisely, the
product A(k−i,i )·B(n, 2k−i) gives the expected number of pairs of increasing subsequence of π∈ Sn,
where each of the two subsequences is of length k, and the number of points in the intersection is i. As before,
B(N,j ) = C(N,j )/j! where C(N,j ) is the usual binomial coeﬃcient N !/(j!(N−j)!), throughout this article.
We would want to calculate the expectation for the pair of increasing subsequences of π∈Sn where the
ﬁrst subsequence has length k and the second subsequence has length ℓ, and the intersection has cardinality
i. Even though this seems like a clear goal, we will not pursue that goal in this article. We hope to carry it
out in a future article, either together or perhaps in a diﬀerent colla boration with one or both of the current
authors. Or perhaps, another researcher will do it ﬁrst. We hope that this is okay: we believe that the results
already contained in the present article are of interest to some rea ders, even without that further work (which
is not done yet). In this article, we just study the 2nd moment.
