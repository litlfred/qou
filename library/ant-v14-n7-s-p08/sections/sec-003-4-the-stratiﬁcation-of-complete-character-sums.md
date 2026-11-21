---
doc_id: ant-v14-n7-s-p08
doc_title: "Burgess bounds for short character sums evaluated at forms"
section_id: sec-003-4-the-stratiﬁcation-of-complete-character-sums
section_title: "The stratiﬁcation of complete character sums"
section_number: 4
pages: 15-21
source_pdf: ant-v14-n7-s-p08.pdf
source_sha256: 81b8f00fe5fbd0f6
toc_source: inferred
doc_brief: "Burgess bounds for short character sums evaluated at forms — 11 sections: Front matter; Introduction; Method of proof: an overview"
---
In this section we recall the stratiﬁcation of complete character sums proved in [Xu 2018] and show how
to deduce a slightly stronger formulation that we believe will be of independent interest, as well as being
useful in this paper. In our presentation, we will replace the dimension r in the original work by the
dimension 2r in each instance, but the content of this section would apply in an analogous way for any
dimension r (odd or even).
4A. The stratiﬁcation obtained by Xu. We ﬁrst recall the statement of [Xu 2018, Theorem 1.1 and
Corollary 1.8] in our setting of dimension 2r. For each ﬁxed n,r ≥1, we deﬁne a set of parameters θ j
for 1 ≤j ≤n, as follows:
θ j =



0
if j = 0,
j⌊(r −1)/(n −1)⌋
if j = 1, . . . , n −2,
r −1
if j = n −1,
nr
if j = n.
(4-1)
Note that this differs superﬁcially from the deﬁnition of θ j in [Xu 2018, p. 2]: we are working with
dimension 2r in place of r and the ﬂoor function results in slightly different formulas. (Precisely, from
Xu’s work we may take
θ1 = ⌊(2r −1)/(2n −2)⌋= ⌊(r −1)/(n −1)⌋
(4-2)
and then we set θ j = jθ1 for 1 ≤j ≤n −1. In particular for j = n −1,
θn−1 = ⌊(2r −1)/2⌋= r −1.
In fact, Xu’s original theorem allows a slightly larger value of θ j ≥jθ1; it is later apparent in (7-13) that
this slightly larger choice, leading to a slightly stronger version of Theorem A, would not signiﬁcantly
improve our current application.)
Theorem A [Xu 2018, Theorem 1.1]. Let integers n,r, 1, D ≥1 be ﬁxed. There exist integers C =
C(n,r, D) ≥1 and C′ = C′(n,r, 1, D) ≥1 and a ﬁnite set S = S(n,r, 1, D) of primes such that the
following holds.
Let κ denote a ﬁnite ﬁeld with algebraic closure denoted by κ. For each 1 ≤i ≤2r, let χi : κ× →C×
be a multiplicative character (extended to κ by setting χi(0) = 0) and assume that di := ord(χi)|1 > 0.
Let Fi ∈κ(x1, . . . , xn) be a di-th power-free rational function of degree at most D and assume that
TFi := {m ∈κn : Fi(x) ≡Fi(x + m)}
(4-3)
is ﬁnite for each 1 ≤i ≤2r. Then upon deﬁning
S(x(1), . . . , x(2r)) :=
X
m∈κn
2r
Y
i=1
χi(Fi(m + x(i))),
(4-4)
1926
Lillian B. Pierce and Junyan Xu
we have that whenever char κ̸ ∈S, there exist subschemes
A2nr
κ
= X0 ⊃X1 ⊃X2 ⊃· · · ⊃Xn
such that for each 1 ≤j ≤n,
(1) the sum of the degrees of irreducible components of X j is at most C′;
(2) dim X j ≤2nr −θ j with θ j deﬁned as in (4-1);
(3) for all (x(1), . . . , x(2r)) ∈A2nr(κ) \ X j(κ),
|S(x(1), . . . , x(2r))| ≤C(#κ)(n+ j−1)/2.
Remark. The hypothesis that for each 1 ≤i ≤2r, χi has order di > 0 could allow that χi is the principal
character. However, if χi is principal then di = 1 and hence to be di-th power-free Fi ∈κ(x1, . . . , xn)
must be a constant function. This implies that TFi is inﬁnite, thus excluding this possibility from the
theorem. This remark applies to Corollary B, below, and the resulting Theorem 4.1 and Corollary 4.2.
Remark. Note that while the subschemes X j may depend on the Fi, the parameters C, C′, θ j depend
only on the maximum degree D of the Fi. The constant C = C(n,r, D) noted above is bounded above
by (4r(D +1)+1)n as computed in [Katz 2001, Theorem 11] (see the remarks following Theorem 1.1 in
[Xu 2018], again recalling that we have 2r in place of r). The constant C′ (and later C′′ in Corollary 4.3)
only depends on n,r, D, 1 but is not explicitly determined. For further details on the dependence of C′
and C′′ see [Xu 2018, Section 2.1, and the remark following Theorem 1.1] and Corollary 4.3.
Next, we must convert Theorem A into a count for the number of points (x(1), . . . , x(2r)) ∈A2nr(κ)
(later denoted as collections {x(1), . . . , x(2r)}) such that a given upper bound for |S(x(1), . . . , x(2r))| holds.
It is convenient to deﬁne for each 0 ≤j ≤n and any sequence 1 ≤k1 ≤k2 ≤· · · ≤kn < ∞the function
Bn,r( j; k) = Bn,r( j; k1, . . . , kn) =



1
if j = 0,
k
θ j
1 = k j⌊(r−1)/(n−1)⌋
1
if j = 1, . . . , n −2,
kθn−1
1
= kr−1
1
if j = n −1,
(k1 · · · kn/2)2r
if j = n, n even,
(k1 · · · k(n−1)/2)2rkr
(n+1)/2
if j = n, n odd.
(4-5)
(To aid comparison to Xu’s original notation [2018] involving parameters denoted by n0, η, we make the
simple observation that for j = n and θ j = nr, if n is even we write nr = (n/2)2r (with n0 = n/2 and
η = 0) and when n is odd we write nr = ((n −1)/2) · 2r + r (with n0 = (n −1)/2 and η = r), so that
Xu’s original notation results in the expression stated above for Bn,r( j, k) in the case j = n, and with
ambient dimension 2r.)
Corollary B [Xu 2018, Corollary 1.8]. Let integers n,r, 1, D ≥1 be ﬁxed. There exist integers
C = C(n,r, D) ≥1 and C′ = C′(n,r, 1, D) ≥1 and a ﬁnite set S = S(n,r, 1, D) of primes such
that the following holds.
Burgess bounds for short character sums evaluated at forms
1927
Let κ denote a ﬁnite ﬁeld with algebraic closure denoted by κ. For each 1 ≤i ≤2r, let χi : κ× →C×
be a multiplicative character (extended to κ by setting χi(0) = 0) and assume that di := ord(χi)|1 > 0.
Let Fi ∈κ(x1, . . . , xn) be a di-th power-free rational function of degree at most D and assume that TFi as
deﬁned in (4-3) is ﬁnite for each 1 ≤i ≤2r.
Let {Mi}n
i=1 be subsets of κ such that 1≤|M1|≤|M2|≤· · ·≤|Mn|<∞, and deﬁne M :=Qn
i=1 Mi ⊂κn
and ∥M∥:= Qn
i=1 |Mi|. Then whenever char κ /∈S, for each 1 ≤j ≤n,
#

(x(1), . . . , x(2r)) ∈M2r : |S(x(1), . . . , x(2r))| > C(#κ)(n+ j−1)/2	
≤C′∥M∥2r Bn,r( j; |M1|, . . . , |Mn|)−1.
(4-6)
4B. The stratiﬁcation in our setting. Now we state the new versions of Theorem A and Corollary B
that we use in this paper.
Theorem 4.1. Let κ = Fq, q prime. The result of Theorem A holds if we replace the hypothesis that
for each 1 ≤i ≤2r, the form Fi is di-th power-free and TFi is ﬁnite, by the weaker hypothesis that for
each 1 ≤i ≤2r, the reduction modulo q of the form Fi is (di, q)-admissible, and for each 1 ≤i ≤2r,
deg Fi < q.
Corollary 4.2. Let κ = Fq, q prime. The result of Corollary B holds if we replace the hypothesis that for
each 1 ≤i ≤2r, the form Fi is di-th power-free and TFi is ﬁnite, by the weaker hypothesis that for each
1 ≤i ≤2r, the reduction modulo q of the form Fi is (di, q)-admissible.
In the above corollary, we are able to omit the condition deg Fi < q seen in Theorem 4.1 by possibly
enlarging C′; see (4-9). Through similar considerations, we can remove consideration of the set S, as we
record here:
Corollary 4.3. In addition, given n,r, 1, D in either Corollary B or Corollary 4.2, we may take the set
S = S(n,r, 1, D) to be the empty set, at the expense of replacing C′ = C′(n,r, 1, D) by a possibly
larger constant C′′ = C′′(n,r, 1, D).
Within the Burgess argument, we will consider the sum
X
m (mod q)
χ(F{x}(m)) =
X
m (mod q)
2r
Y
i=1
χi(F(m + x(i)))
in which we have ﬁxed a multiplicative Dirichlet character χ of order 1 modulo a prime q and then set
χi = χ if i is odd and χi = χ if i is even. This is then clearly of the form S(x(1), . . . , x(2r)) as deﬁned
in (4-4), with the choice that all the Fi are equal to our ﬁxed F ∈Fq[x1, . . . , xn] of degree D. For later
reference, we record the following immediate consequence of Theorem 4.1 and Corollary 4.3 (choosing
the subset Mi of κ to be (0, ki] for each 1 ≤i ≤2r).
Theorem 4.4. Let integers n,r, 1, D ≥1 be ﬁxed. Then there exist constants C = C(n,r, D) and
C′′ = C′′(n,r, 1, D) such that the following holds.
1928
Lillian B. Pierce and Junyan Xu
Fix a prime q and let χ be a multiplicative Dirichlet character of order 1 modulo q. Suppose
F ∈Z[x1, . . . , xn] has the property that its reduction modulo q is (1, q)-admissible and deﬁne F{x}(X)
accordingly as in (2-6).
Then for every 1 ≤j ≤n, for every tuple k = (k1, . . . , kn) ∈Zn with
1 ≤k1 ≤k2 ≤· · · ≤kn ≤q,
#

(x(1), . . . , x(2r)) ∈(0, k]2r :

X
m (mod q)
χ(F{x}(m))

 > Cq(n+ j−1)/2

≤C′′∥k∥2r Bn,r( j; k)−1, (4-7)
in which Bn,r( j; k) is deﬁned as in (4-5).
Remark. Note that the trivial upper bound in (4-7) is ∥k∥2r. The fundamental consequence of Theorem 4.4
is that it shows that generically among {x} ∈(0, k]2r, square-root cancellation holds, as soon as r is
sufﬁciently large relative to n. Precisely, as soon as r ≥n, so that the exponent ⌊(r −1)/(n−1)⌋appearing
in Bn,r(1; k) is strictly positive, the number of {x} ∈(0, k]2r such that square-root cancellation is violated
is O(∥k∥2rk−1
1 ), which sufﬁces for our claim, as long as k1 is at least a positive power of ∥k∥.
Also, to aid in understanding the role of the function Bn,r( j; k) in this result, we note that the
bound (4-7) is in the format of (2-11) with the choice R = 2nr and with the R-dimensional box being
(0, k1] × · · · × (0, k1] × · · · × (0, kn] × · · · × (0, kn],
in which each factor (0, ki] appears 2r times. Thus when θ j ≤2r (this holds for j ≤n −1), we only
save factors of k1. In the ﬁnal case j = n when θn = nr, we save some factors of ki for 1 ≤i ≤⌈n/2⌉as
well. This leads to the deﬁnition of Bn,r( j; k). Finally, we remark for later reference that by construction,
under the hypotheses of the theorem, we always have
∥k∥2r Bn,r( j; k)−1 ≥1.
(4-8)
Remark. Conjecturally, one might hope to improve the result of Theorem 4.4 by proving that one can take
larger values for the codimension θ j used to deﬁne the savings factor Bn,r( j; k)−1. (Precise implications
may be found in Section A.2, where we show that even the conjecturally best possible values for the
codimension do not signiﬁcantly change our main result.) For comparison, in the most extreme case, it is
not hard to see that we must have θn ≤nr, and hence certainly must also have θ j ≤nr for all j ≤n. For
recall from Theorem A that Xn is a subscheme of A2nr
κ
such that for all (x(1), . . . , x(2r)) ∈A2nr
κ
\ Xn(κ),
|S(x(1), . . . , x(2r))|≤C(#κ)n−1/2. In fact, Xu’s paper shows the stronger result that for all ﬁnite extensions
k/κ and (x(1), . . . , x(2r)) ∈A2nr
k
\ Xn(k), it holds that |Sk(x(1), . . . , x(2r))| ≤C(#k)n−1/2; here Sk is
deﬁned analogously to S but summing over m ∈kn and with χi replaced by χi(Nk/κ( · )). That is, all
(x(1), . . . , x(2r)) such that |Sk(x(1), . . . , x(2r))| > C(#k)n−1/2 must lie in Xn(k). Then we claim that
dim Xn ≥nr (and consequently θn ≤nr). To see this, we consider any tuple (x(1), . . . , x(2r)) for which
x( j) = x( j+r) for j = 1, . . . ,r. There are (#k)nr such tuples, and each of them has the property that
|Sk(x(1), . . . , x(2r))|=(#k)n. This is >C(#k)n−1/2 if #k is sufﬁciently large (which we can choose it to be).
Burgess bounds for short character sums evaluated at forms
1929
4C. Deduction of the corollaries. Corollary 4.2 follows from Theorem 4.1 in an identical fashion to
how Corollary B follows from Theorem A in [Xu 2018] (see Corollary 1.8 in that paper) and we do not
repeat the proof here. We only note that in Corollary 4.2 we no longer need to assume that deg Fi < q.
For indeed, suppose that for some 1 ≤i ≤2r we have deg Fi ≥char κ. Then we note that trivially
|S(x(1), . . . , x(2r))| ≤(#κ)2nr = q2nr ≤D2nr
(4-9)
for all (x(1), . . . , x(2r)) ∈A2nr
κ
, so that upon enlarging C′ if necessary so that C′ ≥D2nr the results of
Corollary 4.2 hold (here we also use the fact (4-8)).
To obtain Corollary 4.3 in which formally S = ∅, we note that for any q ∈S(n,r, 1, D), we may
write the trivial upper bound C′∥M∥2r ≤C′q2nr on the right-hand side of (4-6). Thus in order to state a
version of Corollary B or Corollary 4.2 with S = ∅, we simply replace C′ in the statement of the corollary
by C′′(n,r, 1, D) = max{C′, q2nr : q ∈S(n,r, 1, D)}.
4D. Proof of Theorem 4.1. Theorem 4.1 follows from a small modiﬁcation inside the proof of Theorem A
in [Xu 2018]. To be clear, we will state exactly the change that is made (recalling that in our setting we
use 2r where [Xu 2018] uses r; our modiﬁcations would of course work for any dimension r).
The main idea is that even if there is an i ∈{1, . . . , 2r} such that Fi is not di-th power-free, we can write
Fi = Gdi
i eFi in which eFi is di-th power-free, and has TeFi ﬁnite, under the assumption that the reduction of
Fi modulo q is (di, q)-admissible, and then at a key moment in the proof we work with eFi instead of Fi.
To be precise, recall that for any (x(1), . . . , x(2r)) ∈κ2nr,
S(x(1), . . . , x(2r)) :=
X
m∈κn
2r
Y
i=1
χi(Fi(m + x(i))).
(4-10)
We also deﬁne for any tuple (m(1), . . . , m(2s)) ∈κ2ns and each 1 ≤i ≤2r the function
Ti(m(1), . . . , m(2s)) =
X
x∈κn
χi(Fi,{m}(x)),
in which
Fi,{m}(x) :=
sY
j=1
Fi(m( j) + x)
2s
Y
j=s+1
Fi(m( j) + x)di−1.
The proof of Theorem A and hence of Corollary B relies on four ingredients.
(I) The ﬁrst ingredient [Xu 2018, Proposition 1.2] is an identity between 2s-moments of the sums S with
2r-multilinear averages of the sums Ti, namely
X
(x(1),...,x(2r))∈κ2nr
|S(x(1), . . . , x(2r))|2s =
X
(m(1),...,m(2s))∈κ2ns
2r
Y
i=1
Ti(m(1), . . . , m(2s)).
(4-11)
We will refer to the left-hand side as the moment Mκ(r, s); it has a natural generalization to a moment
Mk(r, s) deﬁned in an appropriately analogous manner over any ﬁnite extension k/κ, with χi( · ) replaced
by χi(Nk/κ( · )).
1930
Lillian B. Pierce and Junyan Xu
(II) The second ingredient [Xu 2018, Proposition 1.5] relates the moments Mk(r, s) for ﬁnite extensions k/κ
to the dimension of the subschemes X j.
(III) The third ingredient [Xu 2018, Proposition 1.6 (a)] is an upper bound of O((#k)ns) (that is, of
square-root strength) for the number of tuples (m(1), . . . , m(2s)) ∈k2ns such that Fi,{m}(x) is a perfect
di-th power in k(x1, . . . , xn).
(IV) The fourth ingredient [Xu 2018, Proposition 1.6 (b)] is an application of the Weil bound to save one
factor of (#k)1/2 off the trivial bound (#k)n for an n-dimensional character sum that is a generalization
of Ti in an extension k/κ. Precisely, it is the statement that uniformly in ﬁnite extensions k/κ and tuples
(m(1), . . . , m(2s)) ∈k2ns, if Fi,{m} ∈k(x1, . . . , xn) is not a perfect di-th power in k(x1, . . . , xn), then
X
x∈kn
χi(Nk/κ(Fi,{m}(x)) = O((#k)n−1/2).
(4-12)
These four ingredients are applied in a bootstrapping process. The general philosophy is that a weak
bound with very few exceptions can be bootstrapped into a stronger bound with possibly more exceptions.
More precisely, ingredients (III) and (IV) are the initial input, showing that a small savings holds for
the sums Ti, aside from possibly O((#k)ns) many (that is, square-root many) exceptional choices of
(m(1), . . . , m(2s)) ∈k2ns. For the possible exceptional choices, a trivial upper bound of O((#k)n) is applied
in place of (4-12).
This input step provides a savings, on average, for the sums Ti on the multilinear right-hand side of the
identity (4-11) in ingredient (I) and hence for the moment of S on the left-hand side of (I). Ingredient (II)
then expresses this savings on the moment of S as a stratiﬁcation in terms of a lower bound on codimX j for
each j. This result holds uniformly for sums S of the shape (4-10). Since each Ti is also a sum of this shape
(with s, χi, Fi deﬁned appropriately), the resulting bound for sums S can be applied to each Ti, yielding
an improvement over the initial savings for Ti. This argument then bootstraps to prove the ﬁnal result.
With this outline in hand, we may now brieﬂy verify Theorem 4.1. The only point at which this
argument utilized the assumption that each Fi is di-th power-free and has TFi ﬁnite was at the initial input
to the bootstrapping, when ingredient (III) was used once; see [Xu 2018, §2.3]. Thus all we must do is
show that this step, namely [Xu 2018, Proposition 1.6 (a)] can be proved under the alternate assumption
that for each i, the reduction of Fi modulo q is (di, q)-admissible, and that deg Fi < q. We will replace
[Xu 2018, Proposition 1.6 (a)] with the following proposition.
Proposition 4.5. Let κ = Fq with q prime and ﬁx a rational function F ∈κ(x1, . . . , xn) with deg F < q
such that the reduction of F modulo q is (d, q)-admissible. Fix s ∈N. Then for each ﬁnite extension k/κ,
the number of (m(1), . . . , m(2s)) ∈k2ns such that F{m}(x) is a perfect d-th power over κ is at most
O((#k)ns).
Once this has been proved, this replaces [Xu 2018, Proposition 1.6 (a)] as ingredient (III) in Xu’s
proof, and the results of Theorem A and Corollary B follow under our alternative hypotheses, thus
verifying Theorem 4.1.
Burgess bounds for short character sums evaluated at forms
1931
We prove Proposition 4.5 as follows. Suppose that F has the property that its reduction modulo q
is (d, q)-admissible. Write F = Gd eF in which G, eF ∈κ(x1, . . . , xn) and eF is d-th power-free, with
deg eF < char κ. Under the assumption that the reduction modulo q of F is (d, q)-admissible, by deﬁnition
there is no linear change of variables A∈GLn(Fq) such that eF(x A)∈Fq[x2, . . . , xn]. Hence by Lemma 3.3
(which we may apply since deg eF <q), the only value of m∈κn such that eF(x)≡eF(x+m) is m=0, so that
TeF := {m ∈κn | eF(x) ≡eF(x + m)}
is certainly ﬁnite. Thus we may apply the following lemma to eF (which we quote without repeating
the proof):
Lemma 4.6 [Xu 2018, Lemma 3.16]. Fix r, D ≥1. There exists C0 = C0(r, D) such that the following
holds. Let κ be a ﬁnite ﬁeld and κ0 its prime ﬁeld. Let H ∈κ(x1, . . . , xn) be a d-th power-free rational
function of degree at most D, and assume that
TH = {m ∈κn | H(x) ≡H(x + m)}
is ﬁnite. For any ﬁnite extension k/κ and {ai}2r
i=1 ⊂Z such that gcd(d, ai) = 1 for each 1 ≤i ≤2r, let PH
be the collection of tuples (m(1), . . . , m(2r)) ∈k2nr such that the rational function Q2r
i=1 H(x + m(i))ai is
a perfect d-th power over κ. Then
#PH ≤C0(#k)nr(#TH)r.
(4-13)
Now note that for any such set of exponents {ai}2r
i=1, we have that Q2r
i=1 eF(x + m(i))ai is a perfect d-th
power if and only if
2r
Y
i=1
F(x + m(i))ai =
2r
Y
i=1
eF(x + m(i))ai
 2r
Y
i=1
G(x + m(i))ai
d
is. Thus if we deﬁne PF, respectively PeF, to be the collection of tuples (m(1), . . . , m(2r)) ∈k2nr such
that the rational function Q2r
i=1 F(x + m(i))ai is a perfect d-th power over κ (or analogously for eF), we
have by Lemma 4.6 that
#PF = #PeF ≤C0(#k)nr.
This concludes the veriﬁcation of Proposition 4.5 and hence of Theorem 4.1.
