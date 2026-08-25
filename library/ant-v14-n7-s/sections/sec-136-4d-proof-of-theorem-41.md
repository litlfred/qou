---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-136-4d-proof-of-theorem-41
section_title: "4D. Proof of Theorem 4.1"
section_number: null
pages: 263-265
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
in [Xu 2018]. To be clear, we will state exactly the change that is made (recalling that in our setting we
use 2r where [Xu 2018] uses r; our modiﬁcations would of course work for any dimension r).
The main idea is that even if there is ani∈{ 1,..., 2r} such that Fi is not di-th power-free, we can write
Fi= Gdi
i ~Fi in which ~Fi is di-th power-free, and has T~Fi ﬁnite, under the assumption that the reduction of
Fi modulo q is(di, q)-admissible, and then at a key moment in the proof we work with ~Fi instead of Fi.
To be precise, recall that for any(x(1),..., x(2r))∈κ2nr,
S(x(1),..., x(2r)):=
∑
m∈κn
2r∏
i=1
χi(Fi(m+ x(i))). (4-10)
We also deﬁne for any tuple (m(1),..., m(2s))∈κ2ns and each 1≤ i≤ 2r the function
Ti(m(1),..., m(2s))=
∑
x∈κn
χi(Fi,{m}(x)),
in which
Fi,{m}(x):=
s∏
j=1
Fi(m( j)+ x)
2s∏
j=s+1
Fi(m( j)+ x)di−1.
The proof of Theorem A and hence of Corollary B relies on four ingredients.
(I) The ﬁrst ingredient [Xu 2018, Proposition 1.2] is an identity between 2s-moments of the sums S with
2r-multilinear averages of the sums Ti, namely
∑
(x(1),...,x(2r))∈κ2nr
|S(x(1),..., x(2r))|2s=
∑
(m(1),...,m(2s))∈κ2ns
2r∏
i=1
Ti(m(1),..., m(2s)). (4-11)
We will refer to the left-hand side as the moment Mκ(r, s); it has a natural generalization to a moment
Mk(r, s) deﬁned in an appropriately analogous manner over any ﬁnite extension k/κ, withχi(·) replaced
byχi(Nk/κ(·)).
1930 Lillian B. Pierce and Junyan Xu
(II) The second ingredient [Xu 2018, Proposition 1.5] relates the momentsMk(r, s) for ﬁnite extensionsk/κ
to the dimension of the subschemes X j.
(III) The third ingredient [Xu 2018, Proposition 1.6 (a)] is an upper bound of O((#k)ns) (that is, of
square-root strength) for the number of tuples (m(1),..., m(2s))∈ k2ns such that Fi,{m}(x) is a perfect
di-th power in k(x1,..., xn).
(IV) The fourth ingredient [Xu 2018, Proposition 1.6 (b)] is an application of the Weil bound to save one
factor of(#k)1/2 off the trivial bound(#k)n for an n-dimensional character sum that is a generalization
of Ti in an extension k/κ. Precisely, it is the statement that uniformly in ﬁnite extensions k/κ and tuples
(m(1),..., m(2s))∈ k2ns, if Fi,{m}∈ k(x1,..., xn) is not a perfect di-th power in k(x1,..., xn), then
∑
x∈kn
χi(Nk/κ(Fi,{m}(x))= O((#k)n−1/2). (4-12)
These four ingredients are applied in a bootstrapping process. The general philosophy is that a weak
bound with very few exceptions can be bootstrapped into a stronger bound with possibly more exceptions.
More precisely, ingredients (III) and (IV) are the initial input, showing that a small savings holds for
the sums Ti, aside from possibly O((#k)ns) many (that is, square-root many) exceptional choices of
(m(1),..., m(2s))∈ k2ns. For the possible exceptional choices, a trivial upper bound ofO((#k)n) is applied
in place of (4-12).
This input step provides a savings, on average, for the sums Ti on the multilinear right-hand side of the
identity (4-11) in ingredient (I) and hence for the moment of S on the left-hand side of (I). Ingredient (II)
then expresses this savings on the moment ofS as a stratiﬁcation in terms of a lower bound oncodimX j for
each j. This result holds uniformly for sums S of the shape (4-10). Since each Ti is also a sum of this shape
(with s,χ i, Fi deﬁned appropriately), the resulting bound for sums S can be applied to each Ti, yielding
an improvement over the initial savings for Ti. This argument then bootstraps to prove the ﬁnal result.
With this outline in hand, we may now brieﬂy verify Theorem 4.1. The only point at which this
argument utilized the assumption that each Fi is di-th power-free and has TFi ﬁnite was at the initial input
to the bootstrapping, when ingredient (III) was used once; see [Xu 2018, §2.3]. Thus all we must do is
show that this step, namely [Xu 2018, Proposition 1.6 (a)] can be proved under the alternate assumption
that for each i, the reduction of Fi modulo q is(di, q)-admissible, and that deg Fi< q. We will replace
[Xu 2018, Proposition 1.6 (a)] with the following proposition.
Proposition 4.5. Letκ= Fq with q prime and ﬁx a rational function F∈κ(x1,..., xn) with deg F< q
such that the reduction of F modulo q is(d, q)-admissible. Fix s∈ N. Then for each ﬁnite extension k/κ,
the number of (m(1),..., m(2s))∈ k2ns such that F{m}(x) is a perfect d-th power over κ is at most
O((#k)ns).
Once this has been proved, this replaces [Xu 2018, Proposition 1.6 (a)] as ingredient (III) in Xu’s
proof, and the results of Theorem A and Corollary B follow under our alternative hypotheses, thus
verifying Theorem 4.1.
Burgess bounds for short character sums evaluated at forms 1931
We prove Proposition 4.5 as follows. Suppose that F has the property that its reduction modulo q
is(d, q)-admissible. Write F= Gd~F in which G,~F∈κ(x1,..., xn) and ~F is d-th power-free, with
deg~F< charκ. Under the assumption that the reduction modulo q of F is(d, q)-admissible, by deﬁnition
there is no linear change of variablesA∈GLn(Fq) such that~F(x A)∈ Fq[x2,..., xn]. Hence by Lemma 3.3
(which we may apply sincedeg~F<q), the only value ofm∈κn such that~F(x)≡~F(x+m) is m=0, so that
T~F:={ m∈κn|~F(x)≡~F(x+ m)}
is certainly ﬁnite. Thus we may apply the following lemma to ~F (which we quote without repeating
the proof):
Lemma 4.6 [Xu 2018, Lemma 3.16]. Fix r, D≥ 1. There exists C0= C0(r, D) such that the following
holds. Letκ be a ﬁnite ﬁeld andκ0 its prime ﬁeld. Let H∈κ(x1,..., xn) be a d-th power-free rational
function of degree at most D, and assume that
TH={ m∈κn| H(x)≡ H(x+ m)}
is ﬁnite. For any ﬁnite extension k/κ and{ai}2r
i=1⊂ Z such that gcd(d, ai)= 1 for each 1≤ i≤ 2r, let PH
be the collection of tuples(m(1),..., m(2r))∈ k2nr such that the rational function∏2r
i=1 H(x+ m(i))ai is
a perfect d-th power overκ. Then
#PH≤ C0(#k)nr(#TH)r. (4-13)
Now note that for any such set of exponents{ai}2r
i=1, we have that∏2r
i=1~F(x+ m(i))ai is a perfect d-th
power if and only if
2r∏
i=1
F(x+ m(i))ai=
2r∏
i=1
~F(x+ m(i))ai
( 2r∏
i=1
G(x+ m(i))ai
)d
is. Thus if we deﬁne PF, respectively P~F, to be the collection of tuples (m(1),..., m(2r))∈ k2nr such
that the rational function∏2r
i=1 F(x+ m(i))ai is a perfect d-th power overκ (or analogously for ~F), we
have by Lemma 4.6 that
#PF= #P~F≤ C0(#k)nr.
This concludes the veriﬁcation of Proposition 4.5 and hence of Theorem 4.1.
