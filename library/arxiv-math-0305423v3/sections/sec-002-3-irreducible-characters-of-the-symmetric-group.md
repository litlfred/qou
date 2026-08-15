---
doc_id: arxiv-math-0305423v3
doc_title: "Stein’s Method and Plancherel Measure of the Symmetric Group"
section_id: sec-002-3-irreducible-characters-of-the-symmetric-group
section_title: "Irreducible characters of the symmetric group"
section_number: 3
pages: 8-14
source_pdf: 0305423v3.pdf
source_sha256: e4554f9084ba4935
doc_brief: "Stein’s Method and Plancherel Measure of the Symmetric Group — We initiate a Stein’s method approach to the study of the Plancherel measure of the symmetric group."
---
This section collects properties we will use about characte rs of irreducible
representations of the symmetric group. For more backgroun d on this topic,
see the book [Sa]. Lemmas 3.1, 3.2, and 3.3 are well known. Lem ma 3.4 is
known but not well known. Lemmas 3.5, 3.6 are elementary cons equences
of known facts but perhaps new.
Throughout
z denotes the complex conjugate of z, and Irr (G) denotes
the set of characters of irreducible representations of a ﬁn ite group G. The
notationdim(χ) denotes the dimension of the representation with characte r
χ.
Lemma 3.1. Let C(g) be the conjugacy class of G containing the element
g. Then for g ∈G, ∑
χ ∈Irr (G)
χ(g)χ(h)
is equal to |G|
|C(g)| if h,g are conjugate and is 0 otherwise.
Lemma 3.2. Let ν be an irreducible character of a ﬁnite group G, and χ
any character of G. Then the multiplicity of ν in χ is equal to
1
|G|
∑
g∈G
ν(g)χ(g).
Lemma 3.3. The irreducible characters of the symmetric group Sn are real
valued.
Note that Lemma 3.4 generalizes Lemma 3.1.
Lemma 3.4. ([Sta], Exercise 7.67) Let G be a ﬁnite group with conjugacy
classes C1, · · ·,C r. Let Ck be the conjugacy class of an element w ∈ G.
Then the number of m-tuples (g1, · · ·,g m) ∈ Gm such that gj ∈ Cij and
g1 · · ·gm =w is
∏ m
j=1 |Cij |
|G|
∑
χ ∈Irr (G)
1
dim(χ)m−1χ(Ci1) · · ·χ(Cim)χ(Ck).
For the application of Stein’s method we shall only need the c ase k = 1
of Lemmas 3.5 and 3.6.
Lemma 3.5. Letχ be a character of the symmetric group Sn. Let ni(g) de-
note the number of cycles of g of length i. Let Res,Ind denote the operations
of restriction and induction. Then for k ≥ 1,
ResSn+k
Sn (Ind Sn+k
Sn (χ))[g] = χ(g)(n1(g) + 1) · · · (n1(g) +k).
9
Ind Sn
Sn− k
(ResSn
Sn− k
(χ))[g] = χ(g)(n1(g)) · · · (n1(g) −k + 1).
Proof. Let us prove the ﬁrst assertion, the second being similar. It is well
known ([Sa]) that if H is a subgroup of a ﬁnite group G, and χ is a character
of H, then
Ind G
H(χ)[g] = 1
|H|
∑
t∈ G
t− 1gt∈ H
χ(t−1gt).
Now apply this to H =Sn,G =Sn+k, using the fact that if two elements of
Sn are conjugate by an element of Sn+k, they are conjugate in Sn. Letting
Cent G(g) denote the centralizer size of an element g in a group G, it follows
that the induced character at g ∈Sn is equal to
χ(g) |Cent Sn+k (g)|
|Cent Sn(g)| =χ(g)(n1(g) + 1) · · · (n1(g) +k).
Here we have used the fact that ∏
jjnjnj! is the centralizer size in S∑
j jnj
of an element with nj cycles of length j. □
In Lemma 3.6 we use the notation that dim(µ/τ ) is the number of paths
in the Young lattice from τ to µ (or equivalently the number of ways of
adding boxes one at a time to get from τ to µ). We let |λ| denote the size
of a partition.
Lemma 3.6. Let µ,λ be partitions of n. Let n1(g) denote the number of
ﬁxed points of a permutation g. Then
∑
τ
|τ |=n+k
dim(τ/λ )dim(τ/µ ) = 1
n!
∑
g∈Sn
χµ (g)χλ (g)(n1(g) + 1) · · · (n1(g) +k)
∑
τ
|τ |=n− k
dim(λ/τ )dim(µ/τ ) = 1
n!
∑
g∈Sn
χµ (g)χλ (g)(n1(g)) · · · (n1(g) −k + 1).
Proof. We prove only the ﬁrst part as the second part is similar. Both
sides of this equation enumerate the multiplicity of µ in the representation
ResSn+k
Sn (Ind Sn+k
Sn (λ)). This multiplicity is equal to the left hand side by the
branching rules for induction and restriction in the symmet ric group (Theo-
rem 2.8.3 in [Sa]). That the right hand side computes the same multiplicity
follows from Lemmas 3.2, 3.3, and 3.5. □
Note that as a special case of Lemma 3.6,
|parents(µ,λ )| = 1
n!
∑
g∈Sn
χµ (g)χλ (g)(n1(g) + 1).
10
4. Stein’s method and Kerov’s central limit theorem
In this section we prove Theorem 1.2. Recall that W (λ) = (n−1)√
2
χ λ (12)
dim(λ ) and
that the Plancherel measure chooses a partition λ with probability dim(λ )2
n! .
If n = 1 we use the convention that W = 0. Then Lemma 3.4 implies the
known fact that the mean and variance of W are 0 and 1 − 1
n respectively.
This will also follow from Stein’s method.
In fact there is an explicit formula (due to Frobenius [Fr])
χλ (12)
dim(λ) = 1( n
2
)
∑
i
( λi
2
)
−
( λ′
i
2
)
where λi is the length of row i of λ and λ′
i is the length of column i of λ.
We shall use this formula only once.
Throughout this section and the remainder of the paper, W ∗ denotes
W (λ∗), where given λ, the partition λ∗ is µ with probability J(λ,µ ) from
Example 1 of Section 2. Recall that ( W,W ∗) is an exchangeable pair. We
also use the notation that χλ denotes the character of the irreducible repre-
sentation of the symmetric group parameterized by the parti tion λ. We let
|λ| denote the size of a partition.
Proposition 4.1 shows that the hypothesis needed to apply th e Stein
method bound are satisﬁed. It also tells us that W is an eigenvector for
the Markov chain J, with eigenvalue (1 − 2
n+1 ). We shall generalize this
observation in Section 5.
Proposition 4.1. EW (W ∗) = (1 − 2
n+1 )W .
Proof. Forn = 1 we have that W = 0 by convention. Otherwise,
Eλ (W ∗) =
∑
|µ |=n
n − 1√
2
χµ (12)
dim(µ)
dim(µ)
(n + 1)dim(λ) |parents(µ,λ )|
= n − 1√
2
1
(n + 1)dim(λ)
∑
|µ |=n
|parents(µ,λ )|χµ (12).
From the representation theory of the symmetric group [Sa], |parents(µ,λ )|
is equal to the multiplicity of χµ in ResSn+1
Sn (Ind Sn+1
Sn (χλ )), since inducing
to Sn+1 corresponds to the possible ways of adding a box to each corne r of
the partition λ, and restricting to Sn corresponds to the possible ways of
removing a corner box. Hence
Eλ (W ∗) = n − 1√
2
1
(n + 1)dim(λ)ResSn+1
Sn (Ind Sn+1
Sn (λ))[(12)].
Applying Lemma 3.5, this simpliﬁes to
n − 1√
2
χλ (12)
(n + 1)dim(λ) (n − 1) = (1 − 2
n + 1 )W.
Since Eλ (W ∗) depends on λ only through W , it is equal to EW (W ∗). □
11
As a consequence of Proposition 4.1, we obtain a Stein’s meth od proof
that the mean E(W ) is equal to 0.
Corollary 4.2. E(W ) = 0 .
Proof. Since the pair ( W,W ∗) is exchangeable, E(W ∗ −W ) = 0. Using
Proposition 4.1, we see that
E(W ∗ −W ) = E(EW (W ∗ −W )) = − 2
n + 1E(W ).
Hence E(W ) = 0. □
Next we shall use Stein’s method to compute Eλ (W ∗)2. Recall that this
notation means the expected value of ( W ∗)2 givenλ. This will be useful for
analyzing the error term in Theorem 1.2.
Proposition 4.3.
Eλ ((W ∗)2) = (1 − 1
n ) + 2(n − 1)(n − 2)2
n(n + 1)
χλ ((123))
dim(λ)
+ (n − 1)(n − 2)(n − 3)2
2n(n + 1)
χλ ((12)(34))
dim(λ) .
Here we use the convention that if n ≤ 3, χλ ((12)(34)) = 0 , and if n ≤ 2,
χλ (123) = 0.
Proof. Ifn = 1 the result is clear. Otherwise,
Eλ (W ∗)2 = (n − 1)2
2
∑
|µ |=n
1
n + 1 |parents(µ,λ )|dim(µ)
dim(λ)
( χµ (12)
dim(µ)
) 2
= (n − 1)2
2(n + 1)
1
dim(λ)
∑
|µ |=n
|parents(µ,λ )|χµ (12)2
dim(µ).
Applying Lemma 3.6, this can be rewritten as
(n − 1)2
2(n + 1)
1
dim(λ)
∑
|µ |=n
χµ (12)2
dim(µ)
1
n!
∑
g∈Sn
χµ (g)χλ (g)(n1(g) + 1)
= (n − 1)2
2(n + 1)
1
dim(λ)
∑
g∈Sn
χλ (g)(n1(g) + 1) 1
n!
∑
|µ |=n
χµ (12)2χµ (g)
dim(µ) .
The next step is to observe that using Lemmas 3.3 and 3.4, one c an com-
pute the expression 1
n!
∑
|µ |=n
χ µ (12)2χ µ (g)
dim(µ ) for any permutation g. Indeed, it
is simply 1
(n
2)
2 multiplied by the number of ordered pairs ( τ1,τ 2) of transpo-
sitions whose product is g. Thus when this expression is non-zero, there are
3 possibilities for the cycle type of g: the identity, a 3-cycle, or a product of
two 2-cycles on disjoint symbols. In all cases it is elementa ry to enumerate
the number of pairs (τ1,τ 2), and these 3 possibilities yield the 3 terms in the
statement of the proposition. □
12
As a consequence of Lemma 4.3, we compute Var (W ).
Corollary 4.4. Var (W ) = (1 − 1
n ).
Proof. SinceW has mean 0, Var (W ) = E(W 2). Since W and W ∗ have the
same distribution, it follows that
E(W 2) = E(W ∗)2 =E(Eλ (W ∗)2).
The quantity Eλ (W ∗)2 was computed in Proposition 4.3 as a sum of three
terms. The Plancherel measure average of the ﬁrst term is (1 − 1
n ). The
Plancherel measure averages of the other terms both vanish. Indeed, if g is
any nonidentity element of the symmetric group, the Planche rel average of
the function χ λ (g)
dim(λ ) is equal to
1
n!
∑
λ
dim(λ)χλ (g) = 1
n!
∑
λ
χλ (1)χλ (g),
which vanishes by Lemma 3.1. □
In order to prove Theorem 1.2, we have to analyze the error ter ms in
Theorem 1.3. To begin we study
E
(
−1 + n + 1
4 Eλ (W ∗ −W )2
) 2
,
obtaining an exact formula. From a well known general princi ple used in
[Stn1] (see Lemma 5 of [Fu4] for a proof) the fact that W is determined by
λ implies that
E[EW (W ∗ −W )2]2 ≤E[Eλ (W ∗ −W )2]2.
Hence Proposition 4.5 gives an upper bound on
E
(
−1 + n + 1
4 EW (W ∗ −W )2
) 2
.
Proposition 4.5.
E
(
−1 + n + 1
4 Eλ (W ∗ −W )2
) 2
= 3n2 − 5n + 6
4n3 .
Proof. First observe (using Proposition 4.1 in the second equality ) that
Eλ (W ∗ −W )2 =W 2 − 2WE λW ∗ +Eλ (W ∗)2 = ( 4
n + 1 − 1)W 2 +Eλ (W ∗)2.
Combining this with Proposition 4.3, it follows that −1 + n+1
4 Eλ (W ∗ −W )2
is equal to A +B +C +D where
(1) A =
( n+1
4 (1 − 1
n ) − 1
)
(2) B = (n−1)(n−2)(n−3)2
8n
χ λ ((12)(34))
dim(λ )
(3) C = (n−1)(n−2)2
2n
χ λ (123)
dim(λ )
13
(4) D = − n+1
4 (1 − 4
n+1 ) (n−1)2
2
(
χ λ (12)
dim(λ )
) 2
We need to compute the Plancherel measure average of ( A +B +C +D)2.
SinceA2 is constant, the average of A2 is
( n+1
4 (1 − 1
n ) − 1
) 2. The Plancherel
averages of B2,C 2 can both be computed using Lemma 3.1. One gets
(n−1)(n−2)(n−3)3
8n3 and 3(n−1)(n−2)3
4n3 respectively. To compute the Plancherel
average of D2 one uses Lemma 3.4 to reduce the computation to counting
the number of ordered triples ( τ1,τ 2,τ 3) of transpositions whose product is
a transposition, which is easy to do. The Plancherel average s of 2AB, 2AC,
2BC are all 0 by Lemma 3.1. The Plancherel average of 2 AD is computed
by Lemma 3.1. The Plancherel average of 2 BD is reduced to counting the
number of ordered pairs of transpositions whose product con sists of two dis-
joint 2 cycles by Lemma 3.4, and similarly the average of 2 CD is reduced
to counting the number of ordered pairs of transpositions wh ose product is
a 3 cycle. Thus all of the enumerations are elementary and add ing up the
terms yields the proposition. □
The ﬁnal ingredient needed to prove Theorem 1.2 is an upper bo und on
E|W ∗ −W |3. Typically this is the crudest term in applications of Stein ’s
method. It is the only point in the argument where we use Frobe nius’
explicit formula for W (and as noted in the introduction even this could be
avoided).
Proposition 4.6.
E|W ∗ −W |3 ≤
(
4e
√
2√n
) 3
+ 2e−2e√n(2
√
2)3
Proof. From Frobenius’ formula,
W =
√
2
n
∑
i
( λi
2
)
−
( λ′
i
2
)
.
Given this and the way that λ∗ is constructed from λ, it follows that
|W ∗ −W | ≤
√
2
n 2max(λ1,λ ′
1).
Indeed, suppose that λ∗ is obtained from λ by moving a box from row a and
column b to row c and column d. Then
W ∗ −W =
√
2
n
(
λc +λ′
b −λa −λ′
d
)
.
Suppose that λ1 (the size of the ﬁrst row of λ) and λ′
1 (the size of the ﬁrst
column of λ) are both at most 2 e√
n. Then by the previous paragraph
|W ∗ −W | ≤ 4e
√
2√n .
14
Next note by the ﬁrst paragraph, even if λ1> 2e√n orλ′
1> 2e√
n occurs,
|W ∗ −W | ≤ 2
√
2. We claim that the chance that at least one of the events
λ1 > 2e√n or λ′
1 > 2e√
n occurs is at most 2 e−2e√n. Indeed, it is a simple
lemma proved on page 7 of [Ste] that the chance that the longes t increasing
subsequence of a random permutation is at least 2 e√n is at most e−2e√n.
But it follows from the Robinson-Schensted-Knuth correspo ndence (see for
instance [Sa]) that when λ is chosen from the Plancherel measure of the
symmetric group on n symbols, both λ1 andλ′
1 have the same distribution as
the longest increasing subsequence of a random permutation on n symbols.
So as claimed, the chance that at least one of the events λ1 > 2e√
n or
λ′
1> 2e√
n occurs is at most 2 e−2e√n.
Combining these observations proves the proposition. □
To close this section, we prove Theorem 1.2.
Proof. We use Theorem 1.3, which is applicable with τ = 2
n+1 by Proposi-
tions 2.1 and 4.1. Since n ≥ 2, Proposition 4.5 implies that the term
2
√
E[1 − 1
2τEW (W ∗ −W )2]2
in Stein’s bound is at most
√
3n−1/ 2 ≤
√
3n−1/ 4. So using Proposition 4.6
and the fact that e−2e√n ≤n−3/ 2, the bound of Theorem 1.3 becomes
√
3n−1/ 4 + (2π)−1/ 4
/radicaltp
/radicalvertex
/radicalvertex
√
n + 1
2
(
( 4e
√
2√n )3 + 2(2
√
2)3
n3/ 2
)
≤ 40.1n−1/ 4.
□
