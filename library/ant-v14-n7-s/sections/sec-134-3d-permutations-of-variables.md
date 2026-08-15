---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-134-3d-permutations-of-variables
section_title: "3D. Permutations of variables"
section_number: null
pages: 258-263
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Rademacher method for deducing bounds for maximal moments from nonmaximal moments. To carry
out this argument in our setting, we will need to reorder the variables x1, x2,..., xn in F(x) so that a
corresponding tuple of parameters (k1,..., kn) satisﬁes the ordering k1≤ k2≤···≤ kn. Thus we are led
to consider forms resulting from F when the variables are permuted. For any permutationπ of{1,..., n},
deﬁne the form Fπ(X) from the form F(X) by setting Fπ(X1,..., Xn)= F(Xπ(1),..., Xπ(n)).
Lemma 3.5. Let1≥ 1 and a prime q be ﬁxed. If a form F∈[ x1,..., xn] has the property that its
reduction modulo q is (1, q)-admissible, then for every permutation π on a set of n elements, the
reduction modulo q of Fπ is(1, q)-admissible.
Proof. Letting f denote the reduction of F modulo q, we write f= g1h with h being1-th power-free
over Fq; then correspondingly for the permuted versions, if fπ denotes the reduction of Fπ modulo q
then fπ=(gπ)1hπ with hπ being1-th power-free over Fq. Moreover, h can be made independent of at
least one variable after a GL n(Fq) change of variable if and only if hπ can. □
Burgess bounds for short character sums evaluated at forms 1925
4. The stratiﬁcation of complete character sums
In this section we recall the stratiﬁcation of complete character sums proved in [Xu 2018] and show how
to deduce a slightly stronger formulation that we believe will be of independent interest, as well as being
useful in this paper. In our presentation, we will replace the dimension r in the original work by the
dimension 2r in each instance, but the content of this section would apply in an analogous way for any
dimension r (odd or even).
4A. The stratiﬁcation obtained by Xu. We ﬁrst recall the statement of [Xu 2018, Theorem 1.1 and
Corollary 1.8] in our setting of dimension 2r. For each ﬁxed n, r≥ 1, we deﬁne a set of parameters θ j
for 1≤ j≤ n, as follows:
θ j=



0 if j= 0,
j⌊(r− 1)/(n− 1)⌋ if j= 1,..., n− 2,
r− 1 if j= n− 1,
nr if j= n.
(4-1)
Note that this differs superﬁcially from the deﬁnition of θ j in [Xu 2018, p. 2]: we are working with
dimension 2r in place of r and the ﬂoor function results in slightly different formulas. (Precisely, from
Xu’s work we may take
θ1=⌊(2r− 1)/(2n− 2)⌋=⌊ (r− 1)/(n− 1)⌋ (4-2)
and then we setθ j= jθ1 for 1≤ j≤ n− 1. In particular for j= n− 1,
θn−1=⌊(2r− 1)/2⌋= r− 1.
In fact, Xu’s original theorem allows a slightly larger value ofθ j≥ jθ1; it is later apparent in (7 -13) that
this slightly larger choice, leading to a slightly stronger version of Theorem A, would not signiﬁcantly
improve our current application.)
Theorem A [Xu 2018, Theorem 1.1]. Let integers n, r,1, D≥ 1 be ﬁxed. There exist integers C=
C(n, r, D)≥ 1 and C′= C′(n, r,1, D)≥ 1 and a ﬁnite set S= S(n, r,1, D) of primes such that the
following holds.
Letκ denote a ﬁnite ﬁeld with algebraic closure denoted byκ. For each 1≤ i≤ 2r, letχi:κ×→ C×
be a multiplicative character (extended toκ by settingχi(0)= 0) and assume that di:= ord(χi)|1> 0.
Let Fi∈κ(x1,..., xn) be a di-th power-free rational function of degree at most D and assume that
TFi:={ m∈κn: Fi(x)≡ Fi(x+ m)} (4-3)
is ﬁnite for each 1≤ i≤ 2r. Then upon deﬁning
S(x(1),..., x(2r)):=
∑
m∈κn
2r∏
i=1
χi(Fi(m+ x(i))), (4-4)
1926 Lillian B. Pierce and Junyan Xu
we have that whenever charκ⁄∈ S, there exist subschemes
A2nr
κ = X0⊃ X1⊃ X2⊃···⊃ Xn
such that for each 1≤ j≤ n,
(1) the sum of the degrees of irreducible components of X j is at most C′;
(2) dim X j≤ 2nr−θ j withθ j deﬁned as in (4-1);
(3) for all(x(1),..., x(2r))∈ A2nr(κ)\ X j(κ),
|S(x(1),..., x(2r))|≤ C(#κ)(n+ j−1)/2.
Remark. The hypothesis that for each 1≤ i≤ 2r, χi has order di> 0 could allow thatχi is the principal
character. However, ifχi is principal then di= 1 and hence to be di-th power-free Fi∈κ(x1,..., xn)
must be a constant function. This implies that TFi is inﬁnite, thus excluding this possibility from the
theorem. This remark applies to Corollary B, below, and the resulting Theorem 4.1 and Corollary 4.2.
Remark. Note that while the subschemes X j may depend on the Fi, the parameters C, C′,θ j depend
only on the maximum degree D of the Fi. The constant C= C(n, r, D) noted above is bounded above
by(4r(D+ 1)+ 1)n as computed in [Katz 2001, Theorem 11] (see the remarks following Theorem 1.1 in
[Xu 2018], again recalling that we have 2r in place of r). The constant C′ (and later C′′ in Corollary 4.3)
only depends on n, r, D,1 but is not explicitly determined. For further details on the dependence of C′
and C′′ see [Xu 2018, Section 2.1, and the remark following Theorem 1.1] and Corollary 4.3.
Next, we must convert Theorem A into a count for the number of points (x(1),..., x(2r))∈ A2nr(κ)
(later denoted as collections{x(1),..., x(2r)}) such that a given upper bound for|S(x(1),..., x(2r))| holds.
It is convenient to deﬁne for each 0≤ j≤ n and any sequence 1≤ k1≤ k2≤···≤ kn<∞ the function
Bn,r( j; k)= Bn,r( j; k1,..., kn)=



1 if j= 0,
k
θ j
1 = k j⌊(r−1)/(n−1)⌋
1 if j= 1,..., n− 2,
kθn−1
1 = kr−1
1 if j= n− 1,
(k1··· kn/2)2r if j= n, n even,
(k1··· k(n−1)/2)2rkr
(n+1)/2 if j= n, n odd.
(4-5)
(To aid comparison to Xu’s original notation [2018] involving parameters denoted by n0,η , we make the
simple observation that for j= n andθ j= nr , if n is even we write nr=(n/2)2r (with n0= n/2 and
η= 0) and when n is odd we write nr=((n− 1)/2)· 2r+ r (with n0=(n− 1)/2 andη= r), so that
Xu’s original notation results in the expression stated above for Bn,r( j, k) in the case j= n, and with
ambient dimension 2r.)
Corollary B [Xu 2018, Corollary 1.8]. Let integers n, r,1, D≥ 1 be ﬁxed. There exist integers
C= C(n, r, D)≥ 1 and C′= C′(n, r,1, D)≥ 1 and a ﬁnite set S= S(n, r,1, D) of primes such
that the following holds.
Burgess bounds for short character sums evaluated at forms 1927
Letκ denote a ﬁnite ﬁeld with algebraic closure denoted byκ. For each 1≤ i≤ 2r, letχi:κ×→ C×
be a multiplicative character (extended toκ by settingχi(0)= 0) and assume that di:= ord(χi)|1> 0.
Let Fi∈κ(x1,..., xn) be a di-th power-free rational function of degree at most D and assume that TFi as
deﬁned in (4-3) is ﬁnite for each 1≤ i≤ 2r.
Let{Mi}n
i=1 be subsets ofκ such that 1≤| M1|≤| M2|≤···≤| Mn|<∞, and deﬁne M:=∏n
i=1 Mi⊂κn
and‖M‖:= ∏n
i=1|Mi|. Then whenever charκ /∈ S, for each 1≤ j≤ n,
#
{
(x(1),..., x(2r))∈ M2r:| S(x(1),..., x(2r))|> C(#κ)(n+ j−1)/2}
≤ C′‖M‖2r Bn,r( j;| M1|,..., |Mn|)−1. (4-6)
4B. The stratiﬁcation in our setting. Now we state the new versions of Theorem A and Corollary B
that we use in this paper.
Theorem 4.1. Letκ= Fq, q prime. The result of Theorem A holds if we replace the hypothesis that
for each 1≤ i≤ 2r, the form Fi is di-th power-free and TFi is ﬁnite, by the weaker hypothesis that for
each 1≤ i≤ 2r, the reduction modulo q of the form Fi is(di, q)-admissible, and for each 1≤ i≤ 2r,
deg Fi< q.
Corollary 4.2. Letκ= Fq, q prime. The result of Corollary B holds if we replace the hypothesis that for
each 1≤ i≤ 2r, the form Fi is di-th power-free and TFi is ﬁnite, by the weaker hypothesis that for each
1≤ i≤ 2r, the reduction modulo q of the form Fi is(di, q)-admissible.
In the above corollary, we are able to omit the condition deg Fi< q seen in Theorem 4.1 by possibly
enlarging C′; see (4-9). Through similar considerations, we can remove consideration of the set S, as we
record here:
Corollary 4.3. In addition, given n, r,1, D in either Corollary B or Corollary 4.2, we may take the set
S= S(n, r,1, D) to be the empty set , at the expense of replacing C′= C′(n, r,1, D) by a possibly
larger constant C′′= C′′(n, r,1, D).
Within the Burgess argument, we will consider the sum
∑
m(mod q)
χ( F{x}(m))=
∑
m(mod q)
2r∏
i=1
χi(F(m+ x(i)))
in which we have ﬁxed a multiplicative Dirichlet character χ of order1 modulo a prime q and then set
χi=χ if i is odd andχi=χ if i is even. This is then clearly of the form S(x(1),..., x(2r)) as deﬁned
in (4-4), with the choice that all the Fi are equal to our ﬁxed F∈ Fq[x1,..., xn] of degree D. For later
reference, we record the following immediate consequence of Theorem 4.1 and Corollary 4.3 (choosing
the subset Mi ofκ to be(0, ki] for each 1≤ i≤ 2r).
Theorem 4.4. Let integers n, r,1, D≥ 1 be ﬁxed. Then there exist constants C= C(n, r, D) and
C′′= C′′(n, r,1, D) such that the following holds.
1928 Lillian B. Pierce and Junyan Xu
Fix a prime q and let χ be a multiplicative Dirichlet character of order 1 modulo q. Suppose
F∈ Z[x1,..., xn] has the property that its reduction modulo q is(1, q)-admissible and deﬁne F{x}(X)
accordingly as in (2-6). Then for every 1≤ j≤ n, for every tuple k= (k1,..., kn)∈ Zn with
1≤ k1≤ k2≤···≤ kn≤ q,
#
{
(x(1),..., x(2r))∈(0, k]2r:
⏐⏐⏐
∑
m(mod q)
χ( F{x}(m))
⏐⏐⏐> Cq(n+ j−1)/2
}
≤ C′′‖k‖2r Bn,r( j; k)−1, (4-7)
in which Bn,r( j; k) is deﬁned as in (4-5).
Remark. Note that the trivial upper bound in (4-7) is‖k‖2r. The fundamental consequence of Theorem 4.4
is that it shows that generically among{x}∈ (0, k]2r, square-root cancellation holds, as soon as r is
sufﬁciently large relative to n. Precisely, as soon as r≥ n, so that the exponent⌊(r−1)/(n−1)⌋ appearing
in Bn,r(1; k) is strictly positive, the number of{x}∈ (0, k]2r such that square-root cancellation is violated
is O(‖k‖2rk−1
1 ), which sufﬁces for our claim, as long as k1 is at least a positive power of‖k‖.
Also, to aid in understanding the role of the function Bn,r( j; k) in this result, we note that the
bound (4-7) is in the format of (2-11) with the choice R= 2nr and with the R-dimensional box being
(0, k1]×···× (0, k1]×···× (0, kn]×···× (0, kn],
in which each factor (0, ki] appears 2r times. Thus when θ j≤ 2r (this holds for j≤ n− 1), we only
save factors of k1. In the ﬁnal case j= n whenθn= nr , we save some factors of ki for 1≤ i≤⌈ n/2⌉ as
well. This leads to the deﬁnition of Bn,r( j; k). Finally, we remark for later reference that by construction,
under the hypotheses of the theorem, we always have
‖k‖2r Bn,r( j; k)−1≥ 1. (4-8)
Remark. Conjecturally, one might hope to improve the result of Theorem 4.4 by proving that one can take
larger values for the codimensionθ j used to deﬁne the savings factor Bn,r( j; k)−1. (Precise implications
may be found in Section A.2, where we show that even the conjecturally best possible values for the
codimension do not signiﬁcantly change our main result.) For comparison, in the most extreme case, it is
not hard to see that we must have θn≤ nr, and hence certainly must also have θ j≤ nr for all j≤ n. For
recall from Theorem A that Xn is a subscheme of A2nr
κ such that for all (x(1),..., x(2r))∈ A2nr
κ \ Xn(κ),
|S(x(1),..., x(2r))|≤ C(#κ)n−1/2. In fact, Xu’s paper shows the stronger result that for all ﬁnite extensions
k/κ and(x(1),..., x(2r))∈ A2nr
k \ Xn(k), it holds that |Sk(x(1),..., x(2r))|≤ C(#k)n−1/2; here Sk is
deﬁned analogously to S but summing over m∈ kn and withχi replaced byχi(Nk/κ(·)). That is, all
(x(1),..., x(2r)) such that|Sk(x(1),..., x(2r))|> C(#k)n−1/2 must lie in Xn(k). Then we claim that
dim Xn≥ nr (and consequentlyθn≤ nr ). To see this, we consider any tuple (x(1),..., x(2r)) for which
x( j)= x( j+r) for j= 1,..., r. There are (#k)nr such tuples, and each of them has the property that
|Sk(x(1),..., x(2r))|=(#k)n. This is> C(#k)n−1/2 if #k is sufﬁciently large (which we can choose it to be).
Burgess bounds for short character sums evaluated at forms 1929
