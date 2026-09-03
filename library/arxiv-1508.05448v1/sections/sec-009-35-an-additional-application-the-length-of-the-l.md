---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-009-35-an-additional-application-the-length-of-the-l
section_title: "An Additional Application: The Length of the Longest Increasing Subsequence of a Random Walk Evolving under the Asymmetric Exclusion Process"
section_number: 3.5
pages: 47-55
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
doc_brief: "Concentration of Measure Techniques and Applications — 23 sections: Biographical Sketch; Acknowledgments; Abstract"
---
Longest Increasing Subsequence of a Random
Walk Evolving under the Asymmetric Exclu-
sion Process
Consider a random walk X on {1,...,n }. Represent X by some element in {0, 1}n,
where Xi = 0 corresponds to a step down in the walk at position i and Xi = 1
corresponds to a step up. We will assume that
n∑
i=1
Xi = n
2
so that we have the same number of up steps as down steps. We can now look
at this random walk as the initial conﬁguration of a particle process with Xi = 1
corresponding to a particle in position i and Xi = 0 corresponding to no particle at
position i. Consider the asymmetric exclusion process acting on this conﬁguration
with the following dynamics. At each step of the process, a number i is chosen
uniformly in{1,...,n − 1}. If Xi =Xi+1, then the conﬁguration stays the same. If
Xi = 1 and Xi+1 = 0, then the values of Xi andXi+1 switch with probability 1−q/2
and if Xi = 0 and Xi+1 = 1, then the values switch with probability q/2. Viewed in
this way, the asymmetric exclusion process can be viewed as a Markov process on the
set of random walks. See [Liggett, 1985] for an in depth discussion of the asymmetric
exclusion process.
Theorem 3.5.1 ([Koma and Nachtergaele, 1997],[Alcaraz, 1994],[Caputo and Mar-
tinelli, 2003]) . The spectral gap of the ASEP is λn = 1 − ∆−1 cos(π/n), where
∆ = q+q−1
2 for a parameter q satisfying 0<q < 1.
In our case, take q = 1 −c/nα, for a constant c, and 0 < α < 1, such that
39
q≈e−c/nα
. Then Taylor approximating and simplifying gives
λn =c2/2n2α
Now let MX denote the height of the midpoint of the random walk at a ﬁxed time
during the process. In other words, MX = Xn/2, assuming n is even. Note that the
range of this function is [−n/2,n/ 2]. Let M′
x be the evolution of Mx after one step
of the process. Notice that
‖Mx−M′
x‖∞≤ 1
since switching the position of two adjacent particles can change the height of the
midpoint by at most 1. Then
‖|M||2
∞ = 1
2 max
X
E(Mx−M′
x)2
≤ 1
2(1)2
( 1
n− 1
)
= 1
2(n− 1)
The 1
n−1 appears because the only choice of i that will eﬀect the midpoint is i =n/2.
Now plugging into the Chatterjee Ledoux theorem, we have the following result.
Theorem 3.5.2. Letting MX denote the height of the midpoint of the random walk
after evolution under the asymmetric exclusion process, for all r >0 andq = 1−c/nα,
P(|MX− EMX|≥ r)≤ 6 exp
(
−r/2
√
c2/2n2α
1/(2(n− 1))
)
= 6 exp
(
−r/2
√
c2(n− 1)
n2α
)
Notice that this implies that the height of the midpoint has ﬂuctuations bounded
above by a constant nα−1/2 for 0 <α< 1.
Consider the length of the longest increasing (non-decreasing) subsequence of the
40
Figure 3.1: A longest increasing subsequence of a random walk
random walk. This is deﬁned as
LX = max{k : i1 <i 2 <··· <i k andXi1≤Xi2≤···≤ Xik}
See [Angel et al., 2014] for a more in depth description of this topic and results for the
simple random walk. Notice that the height of the midpoint gives a lower bound on
the length of the longest increasing subsequence. Using ASEP as our Markov process
and the spectral gap above, we can prove concentration of measure for LX. Notice
that switching the position of two adjacent particles via ASEP can only change LX
by at most 1. As before, let X′ be the evolution of X after one step of the process.
41
Then, bounding the probability above by 1, we have
‖|L‖|2
∞ = 1
2 max
X
E(LX−LX′)2
≤ 1
2(1)2 = 1
2
so plugging into the Chatterjee Ledoux formula, we get the following result.
Theorem 3.5.3. LettingLX denote the length of the longest increasing subsequence
of the random walk after evolution under the asymmetric exclusion process, for all
r >0 and q = 1−c/nα,
P(|LX− ELX|≥ r)≤ 6 exp
(
−r/2
√
c2
n2α
)
This implies that the ﬂuctuations are bounded above by a constant times nα. In
particular, for q = 1−c/√n, the ﬂuctuations are bounded above by a constant times
√n.
In order to give some context to the size of the ﬂuctuations, we calculate height
of the midpoint, which gives a lower bound on the length of the longest increasing
subsequence of the walk under this distribution.
Theorem 3.5.4. Forq <1−c/n and c =−20 log(3/5), the height of the midpoint
of the random walk is kn for some constant k >0.
Before we give the proof, we will need the following lemma.
Lemma 3.5.5. Consider a random walk with independent steps. Assume that P(Xk =
0) = 1
aqk+1 and P(Xk = 1) = aqk
aqk+1 for some a >0, q∈ (0, 1) and k∈ Z+. Consider
NX =∑n
i=1Xi. This gives us the number of up steps in our random walk, or equiva-
lently, the number of particles in our particle process. The ﬂuctuations of NX are at
most order√n.
42
Proof. We begin by calculating the variance of NX. We can then use Chebyshev’s
inequality to bound the ﬂuctuations. Since the Xi are independent,
Var(NX) =
n∑
i=1
Var(Xi)
Using the probabilities given in the lemma, we know that
Var(Xi) = aqi
aqi + 1−
( aqi
aqi + 1
)2
= aqi
aqi + 1
(
1− aqi
aqi + 1
)
This gives
Var(NX) =
n∑
i=1
aqi
aqi + 1
(
1− aqi
aqi + 1
)
A derivative calculation show that aqi
aqi+1
(
1− aqi
aqi+1
)
is decreasing in i, so
Var(NX)≤n
( aq
aq + 1
)(
1− aq
aq + 1
)
Since we only care about the order of the ﬂuctuations, we can bound the positive
value ( aq
aq + 1
)(
1− aq
aq + 1
)
by 1, giving us
Var(NX)≤n
Plugging into Chebyshev’s inequality tells us that
P (|NX− E(NX)|≥ k)≤ n
k2
which proves our result.
43
We are now set to prove theorem 3.5.4
Proof. The basic idea of the proof of theorem 3.5.4 is as follows. We will begin by
assuming that the steps of our random walk are independent, so that our measure is
a product measure. Recall, the steps are not independent, since we are conditioning
on the fact that we have exactly n/2 steps up and n/2 steps down. However, if n is
large, the steps are close to independent. By bounding the ﬂuctuations of the number
of particles in our product system, we can then relate our non-independent state to
the product state.
Begin by assuming that
P (Xk = 0)
P (Xk = 1) =aqk
so that we have a product measure. Then we know that
P (Xk = 0) = 1
aqk + 1
and
P (Xk = 1) = aqk
aqk + 1
Then
E
( k∑
i=1
Xi
)
=
k∑
i=1
aqi
aqi + 1
Since the summand is decreasing in i, we get the bounds
k
( aqk
aqk + 1
)
≤ E
( k∑
i=1
Xi
)
≤k
( aq
aq + 1
)
We will work in this generality for now, and add in appropriate values of a and k
later. Using this information, we can get bounds on the height of the random walk
at point k. Let Hk be the height of the random walk at position k. For convenience
44
later, we will assume that Xi = 1 corresponds to a step down in the walk, and that
Xi = 0 corresponds to a step up. Provided that we can prove that our height is cn
for c< 0, our theorem will be proved. We have
E(Hk) = (−1)
k∑
i=1
Xi +
(
k−
k∑
i=1
Xi
)
=k− 2
( k∑
i=1
Xi
)
Plugging in our bounds on E
(∑k
i=1Xi
)
, we get
−k
(
2
( aq
aq + 1
)
− 1
)
≤ E(Hk)≤−k
(
2
( aqk
aqk + 1
)
− 1
)
At this point, we need a bound on the number of particles in the system. Since we
are assuming theXi are independent, we can use the result from the previous lemma,
which gives us
P
(⏐⏐⏐⏐⏐
n∑
i=1
Xi−M
⏐⏐⏐⏐⏐>u
)
≤ 4 exp(−u2/4M)
where M is a median for the number of particles. Estimating the median by the
expectation of the number of particles, we see that M should at least be close to
n/2
(
aq
aq+1
)
. If we choose a appropriately corresponding to q, we should be able to
make the constant order 1, making our expectation order n. Then, by the concen-
tration of measure inequality, ∑n
i=1Xi has ﬂuctuations on the order of √n. This is
reasonably small compared with the expected number of particles in the system.
Recall that we are actually concerned with ﬁnding the height of the midpoint, so
plugging in k =n/2, we have that
−n/2
(
2
( aq
aq + 1
)
− 1
)
≤ E(Hn/2)≤−n/2
(
2
( aqn/2
aqn/2 + 1
)
− 1
)
At this point, we can ignore the lower bound, using the fact that that a lower bound
is−n/2 anyway, regardless of the conﬁguration. We will refer to our interface as the
position in which P(X = 0) = P(X = 1). For now, we will put our interface at 9n/20,
45
which will be just to the left of the midpoint. In other words, a = q−9n/20 and at
position 9n/20, P(X = 0) = P(X = 1). We will push it to the edge at n/2 at the end,
since moving the interface to the right only increases the probability of moreXi being
equal to 1, hence lowering the expectation of the midpoint. Using this interface, we
will ﬁrst look at the height of the random walk at position 8 n/20. Using the upper
bound from above, we have that
E(H8n/20)≤−8n
20
(
2
( q−n/20
q−n/20 + 1
)
− 1
)
Beyond this point, if we assume that all of the remaining steps between 8 n/20 and
n/2 are steps up, we have that
E(Hn/2)≤−8n
20
(
2
( q−n/20
q−n/20 + 1
)
− 1
)
+ 2n
20
The important thing to notice here, is this actually gives us an upper bound on the
height of the midpoint in the ﬁxed particle number (ASEP) random walk. In the
product state conﬁguration, with our interface at 9n
20 , we know that the ﬂuctuations
in the number of down steps are less than n
20. By assuming that all steps after site
8n
20 are up, we have accounted for the worst case scenario where we actually have √n
less down steps then we expect. If some of the steps after site 8n
20 are actually down
instead of up, this will only serve to lower the height of our midpoint. Hence, we
have, that in the ASEP (ﬁxed number of down steps) random walk generated using
the blocking measures,
E(Hn/2)≤ E(Hn/2)≤−8n
20
(
2
( q−n/20
q−n/20 + 1
)
− 1
)
+ 2n
20
We would like to show that for an appropriate choice ofq, this iscn for some constant
46
c< 0. This is true provided that
8
20
(
2
( q−n/20
q−n/20 + 1
)
− 1
)
> 2
20
Solving this inequality gives a condition on q, which is
q >
(3
5
) 20
n
or
q >e20/n log(3/5)
Taylor expanding the exponential gives
q >1 + 20
n log(3/5) + 400
2n2 (log(3/5))2 +...
As n→∞ , taking q >1−α/n with α =−20 log(3/5) should be suﬃcient. As long
as this condition is satisﬁed, our expectation is cn for a constant c< 0.
At this point, we do want to move the interface to a =q−n/2, such that P(Xn/2 =
0) = P(Xn/2 = 1). This simply increases our probability of down steps between 9n
20
and n
2 . Since adding extra down steps only decreases the expectation of the height of
the midpoint, the theorem is proved.
