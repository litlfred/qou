---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd"
section_id: sec-008-a-bonferroni-inequalities-and-bell-polynomials
section_title: "A Bonferroni inequalities and Bell polynomials"
section_number: null
pages: 16-21
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd — Given a uniform random"
---
The principle of inclusion-exclusion (PIE) and the associated inequalit ies related to the PIE are a well-known
topic at the intersection of combinatorics and probability theory. W e will follow the exposition from the
textbook of Charalambides [11] which we appreciate, greatly. The d escriptions there are clear, and also
suﬃciently complete to be useful to newcomers. For us, it is nice tha t he discusses the Bonferroni inequalities
and the Bell polynomials in some detail.
Recall that we are interested in the number of cardinality k subsequences of{1,...,n } which are increasing
for a uniform random permutation π∈Sn. Let us denote by Cn,k the collection of k-tuples i = (i1,...,i k)∈
Zk such that
1≤ i1 < i2 < ... < ik ≤ n. (102)
16
So, for instance, the cardinality of this set is
|Cn,k| =
(n
k
)
. (103)
Given a permutation π∈ Sn and (i1,...,i k)∈ Cn,k, let us denote the indicator for ( i1,...,i k) being an
increasing subsequence of π:
Pn,k(π; (i1,...,i k)) =
k−1∏
a=1
1(0,∞)(πia+1−πia ). (104)
So, for example, we know that
∀(i1,...,i k)∈Cn,k, we have
∑
π∈Sn
Pn,k(π; (i1,...,i k)) = n!
k!, (105)
by the discussion around equations (3), (4) and (5). Now let ~C(r)
n,k denote the collection of all sets
{
i(1),..., i(r)
}
, (106)
satisfying
• for each s∈{ 1,...,r } we have i(s) = (i(s)
1 ,...,i (s)
k )∈Cn,k,
• for each s,t∈{ 1,...,r }, if s⁄=t then there is some a∈{ 1,...,k } such that i(s)
a ⁄=i(t)
a .
Therefore, we have, for instance, that the cardinality is equal to
⏐
⏐
⏐~C(r)
n,k
⏐
⏐
⏐ =
((n
k
)
r
)
= N (N− 1)··· (N−r + 1)
r!
⏐
⏐
⏐
⏐
⏐
N =(n
k)
. (107)
Now, following the notation from Chapter 4 of Charalambides, let us d eﬁne
S(r)
n,k =
∑
π∈Sn
∑
{i(1),...,i(r)}∈ ~C (r)
n,k
r∏
s=1
Pn,k(π; i(s)). (108)
This is equal to the sum over all ( i(1),..., i(r))∈ ~C(r)
n,k of the number of permutations in Sn such that each of
i(1), . . . , i(r) is an increasing subsequence for π. So, for example,
1
n!S(1)
n,k =
(n
k
)
· 1
k!, (109)
as in equation (8). Note that we are following the notation of the combinatorics textbook of Charalambides, so
that we focus on cardinalities, instead of expectations and probab ilities. (That is what we needed to noramlize
by 1/n! on the left-hand-side of the equation above.) Now, following the no tation from Charalambides, let us
deﬁne
L(r)
n,k =
⏐
⏐
⏐
⏐
⏐
{
π∈Sn :∃{i(1),..., i(r)}∈ ~C(r)
n,k, s.t.
r∏
s=1
Pn,k(π, i(s)) = 1
}⏐
⏐
⏐
⏐
⏐. (110)
This is equal to the number of permutations π∈ Sn such that there are at least r distinct subsequences
i(1),..., i(r)∈Cn,k, each of cardinality k, such that all of the r subsequences are increasing for π. Then note
that we have, using the deﬁnition of Zn,k(π) from (6),
1
n!L(r)
n,k = P({π∈Sn : Zn,k(π)≥r}). (111)
In principle, we are most interested in L(1)
n,k because this is the cardinality which arises in the formula for the
length of the longest increasing subsequence:
1
n!L(1)
n,k = P({π∈Sn : Zn,k(π)≥ 1}) = P({π∈Sn : Ln(π)≥k}). (112)
But Charalambides states the Bonferroni inequalities for general r. Therefore, we deﬁned the terms for general
r, in order to most closely match his notation. (Note that that variab le which he calls k is what we call r,
and there are other minor changes mutatis mutandis .)
17
Proposition A.1 (V ersion of the Bonferroni inequalities) Suppose we have n∈ N and we have chosen
k∈{ 1,...,n }. Then, for each r∈{ 1,...,
(n
k
)
} and for each R∈{ 0, 1,..., |~C(r)
n,k|} we have
(−1)R−r+1
(
L(r)
n,k−
R∑
s=r
(−1)s−r
(s− 1
r− 1
)
S(s)
n,k
)
≥ 0. (113)
We will not provide the proof of this proposition, since we have copied it from [11] where it is Theorem 4.5,
equation (4.23). Our main interest is in the case of r = 1. So, summarizing that case, the proposition implies
that for each R∈{ 1,...,
(n
k
)
}, we have:
• if R is even then
L(1)
n,k ≥
R∑
s=1
(−1)s−1S(s)
n,k ; (114)
• whereas, if R is odd then
L(1)
n,k ≤
R∑
s=1
(−1)s−1S(s)
n,k. (115)
Of course, PIE also gives (as in Theorem 4.2 of Charalambides for exa mple)
L(1)
n,k =
|Cn,k|∑
s=1
(−1)s−1S(s)
n,k. (116)
So, if one could calculate S(s)
n,k for all s up to|Cn,k| =
(n
k
)
, then this gives a method of calculating L(1)
n,k from
them, in principle. But the goal of the Bonferroni inequalities is to ho pefully obtain inequalities that are
useful without requiring all S(s)
n,k for s going up to
(n
k
)
, but merely those for s∈{ 1,...,R }. It is hoped that
for some R≤
(n
k
)
this gives an easier method of bracketing L(1)
n,k in order to calculate P(Ln≥k).
The next step is to simplify the calculation of the quantities S(r)
n,k. What Pinsky’s method allow us to
calculate is moments of Zn,k. One may note that Zn,k(π) is the total number of cardinality k subsequences,
i∈Cn,k such that i is increasing for π. Then it is easy to see that
∑
{i(1),...,i(r)}∈ ~C (r)
n,k
r∏
s=1
Pn,k(π; i(s)) =
(Zn,k(π)
r
)
= 1
r!Zn,k(π)
(
Zn,k(π)− 1
)
···
(
Zn,k−r + 1
)
. (117)
In other words, combining the earlier calculations, we have for R∈{ 1,...,
(n
k
)
}:
• if R is even, then
P(Ln≥k) = P(Zn,k≥ 1)≥
R∑
s=1
(−1)s−1E
[( Zn,k
s
)]
; (118)
• while if R is odd, then
P(Ln≥k) = P(Zn,k≥ 1)≤
R∑
s=1
(−1)s−1E
[( Zn,k
s
)]
. (119)
But more generally, for each r∈{ 1,...,
(n
k
)
} and for each R∈{ 0, 1,..., |~C(r)
n,k|} we have
(−1)R−r+1
(
P(Zn,k≥r)−
R∑
s=r
(−1)s−r
(s− 1
r− 1
)
E
[( Zn,k
s
)] )
≥ 0. (120)
Remark A.2 In an earlier version of this article, we promoted the idea of the Bell polynomials, not realizing
the simple connection to the factorial moments.
18
Precisely, the important fact is that, deﬁning exponential Bell par tition polynomials as B0 ≡ 0 and for
r∈ N ={1, 2,... }
Br(x1,...,x r) =
r−1∑
s=0
(r + 1
s
)
xs+1Br−1−s(x1,...,x r−1−s), (121)
we have that the following 1-variable specialization gives the identity
∀r∈{ 0, 1,... }, we have Br(−0!z,−1!z,..., −(r− 1)!z) = 1
r! (z)r, (122)
where (z)r is the Pochhammer symbol, falling factorial from (33). A reference for the Bell polynomials is
Charalambides, Theorem 11.2 [11].
Even though the necessity is now bypassed, let us describe our old o bservations that we largely transcribed
from Charalambides. The reason that the Bell polynomials are releva nt is that according to Newton’s identity
https://en.wikipedia.org/wiki/Newton’s_identities
we have the following relation between symmetric functions
r·er(x1,...,x N ) =
r∑
s=1
(−1)s−1er−s(x1,...,x N )ps(x1,...,x N ), (123)
where the power sum symmetric functions are
pr(x1,...,x N ) =
N∑
κ=1
xr
κ, (124)
and the elementary symmetric functions are
er(x1,...,x N ) =
∑
i1,...,ir ∈{1,...,N }
(r−1∏
s=1
1(0,∞)(is+1−is)
)
xi1xi2··· xir. (125)
Relatedly, there are identities for certain types of generating fun ctions of these symmetric functions:
1 +
N∑
r=1
(−t)ker(x1,...,x N ) = exp
(
−
∞∑
r=1
tr
rpr(x1,...,x N )
)
. (126)
This is relevant because according to (108)
S(r)
n,k =
∑
π∈Sn
er(X1(π),..., XN (π)), (127)
where we enumerate the elements of Cn,k as
Cn,k =
{
i(1),..., i(N )
}
, (128)
and, for each κ∈{ 1,...,N }, we deﬁne
Xκ :Sn→{ 0, 1}, deﬁned by the formula Xκ(π) = Pn,k
(
π; i(κ)
)
. (129)
wherePn,k(·;·) is as in (104). But then, since each Xκ is an indicator function, taking values in {0, 1},
∀r∈ N ={1, 2,... }, we have pr(X1,..., XN ) = Zn,k =
N∑
s=1
Xκ. (130)
If we did not have this simple formula, then a formula for each r∈ N would be useful more generally:
er(x1,...,x N ) = (−1)r
r! Br(−0!p1(x1,...,x N ),..., −(r− 1)!pr(x1,...,x r)), (131)
which essentially restates (126) via (121) (which is equivalent to the generating function identity stating
that∑ ∞
r=1Bn(x1,...,x n)tn/n! is equal to exp ( ∑ ∞
r=1xrtr/r!) as in Charalambides Corollary 11.1). See, for
example, Example 11.5 on page 427 in [11].
19
B Review of the physicists’ replica approach to the SK model
Suppose that for each pair i,j ∈ N ={1, 2,... } there is a standard normal random variable Ji,j , such that
all the Ji,j ’s are independent. Then, for each N∈ N, the N -spin Sherrington-Kirkpatrick Hamiltonian is a
random function
HN :{+1,−1}N→ R, by the formula HN (σ ) = −
N∑
i=1
N∑
j=1
Ji,j
√
2N
σiσj, (132)
for each σ = (σ1,...,σ N )∈{ +1,−1}N. Originally, the simplest question that phyicists sought to answer
was the formula for the limiting free energy.
The ﬁnite-size approximation to the thermodynamic free energy is fN : (0,∞)→ R, given by the formula
fN (β) = − 1
Nβ ln (ZN (β)) , where ZN (β) =
∑
σ1,...,σN ∈{+1,−1}
exp
(
−βHN (σ )
)
. (133)
The original interest was in the limit of the quenched free energy
f Q(β) = lim
N →∞
E[fN (β)], (134)
as well as a proof argument for the fact that fN (β) satisﬁes a weak law of large numbers in the N→∞ limit.
One approach to trying to guess the formula for f Q(β) is to actually calculate positive integer moments
of the random function ZN (β), which is called the random partition function for N spins. An excellent
reference for mathematicians interested in one perspective on th e physicists’ “replica trick,” is the old review
article of van Hemmen and Palmer [36]. Following their notation, let us de ﬁne, for each n∈ N, the function
ϕ(n)
N : (0,∞)→ R given by the formula
ϕ(n)
N (β) = 1
N ln
(
E
[(
ZN (β)
)n])
. (135)
Note that one could extend the deﬁnition to ϕ(ν)
N (β) for all ν∈ (0,∞). Then one would have E[−βfN (β)] is
equal to lim ν→0+ (ϕ(ν)
N (β)−1)/ν, by properties such as convexity, which insures existence of 1-sid ed derivatives.
The real “trick” in the physicists’ method is that they extrapolate from integer n> 1 to the limit ν→ 0+,
in a non-trivial way. Because the Ji,j ’s are all IID standard, normal random variables, we see that the HN (σ )’s
(for varying σ ’s) are jointly distributed (centered) Gaussian normal random var iables, with covariance
E [HN (σ )HN (τ )] = 1
2N
N∑
i=1
N∑
j=1
σiσjτiτj = N
2
(
qN (σ, τ )
)2
, where qN (σ, τ ) = 1
N
N∑
i=1
σiτi. (136)
Using this, and the fact that
(
ZN (β)
)n
=
∑
σ (1),...,σ (n)∈{+1,−1}N
exp
(
−β
n∑
r=1
HN
(
σ (r))
)
, (137)
the usual formula for the moment generating function of a Gaussia n random variable gives
E
[(
ZN (β)
)n]
=
∑
σ (1),...,σ (n)∈{+1,−1}N
exp
(
β2N
4
n∑
r=1
n∑
s=1
(
qN
(
σ (r), σ (s)))2
)
(138)
Therefore, the ϕ(n)
N (β) functions have thermodynamic limits
ϕ(n)(β) = lim
N →∞
ϕ(n)
N (β), (139)
which are calculated by large-deviation theory techniques. Indeed van Hemmen and Palmer deﬁned a matrix-
indexed Hamiltonian, for any Q = (Qr,s)n
r,s=1∈ [−1, 1]n×n,
HQ :{+1,−1}n→ R, by HQ(⃗S) = − 1
2
N∑
r=1
N∑
s=1
(
Qr,sSrSs− 1
2Q2
r,s
)
, (140)
20
for ⃗S = (S1,...,S n)∈{ +1,−1}n. Then they argued that the formula for −ϕ(n)(β)/β is equal to the minimum
of
Φ (n)(Q)
def
:=− 1
β ln

 ∑
S1,...,Sn∈{+1,−1}
exp
(
−β2HQ(⃗S)
)

 , (141)
varying over all matrices Q∈ [−1, 1]n×n. The matrix Q is akin to a Lagrange multiplier for the optimization
problem associated to the large deviation type problem in (138).
There are various ways of arriving at this framework, some of which do not seem equivalent until extra
work is done. We have presented van Hemmen and Palmer’s particular approach, which is somewhat diﬀerent
than the original approach of Sherrington and Kirkpatrick [32]. In [36], they comment on the relation between
the two works. In their paper, they show that the arg-min is of the form
Q =







1 q0 q0 ... q 0
q0 1 q0 ... q 0
q0 q0 1 ... q 0
.
.
. .
.
. .
.
. . . . .
.
.
q0 q0 q0 ... 1







, (142)
for some number q0 which could then be calculated in terms of a self-consistency formula or in terms of certain
Gaussian integrals (against hyperbolic trigonometric functions).
A good reference for the physicists’ perspective on replica symme try breaking is the monograph of Mezard,
Parisi and Virasoro [23]. In Chapter 3 they consider the analogous p roblem to the presentation above, but
with an eye towards “extrapolating” from n∈ N to ν∈ (0, 1). This means guessing, but they must make a
good educated guess to get something that is not senseless. Even Sherrington and Kirkpatrick noted in their
original paper the unphysical property that the entropy become s negative below the critical temperature,
using their approach. Instead Parisi considered a sequence of ult rametric generalizations of the Q-matrix
starting with the structure
Q =














1 q1 ... q 1
q1 1 ... q 1
.
.
. .
.
. . . . .
.
.
q1 q1 ... 1
q0
q0
1 q1 ... q 1
q1 1 ... q 1
.
.
. .
.
. . . . .
.
.
q1 q1 ... 1














, (143)
for a pair of numbers 0 ≤ q0 < q1≤ 1. In the matrix, the oﬀ-diagonal blocks, with just a q0 are meant to
indicate blocks of the matrix wherein every matrix entry is equal to q0. Similar to this, in the diagonal blocks,
every matrix is equal to q1 except for the diagonal matrix entries which are Qi,i = 1 for each i∈{ 1,...,n }.
This would be considered 1 level of replica symmetry breaking. Becau se of the role of the parameter
ν− 1, one seeks the maximum of the analogue of equation (141) when ν∈ (0, 1), instead of the maximum.
The motivation for this particular choice is beyond our ability to review . We do recommend consulting the
textbook [23]. An example of a Q matrix with 2 levels of replica symmetry breaking is shown in Figure 6.
