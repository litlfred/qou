---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-019-8-inequalities-for-mixed-discriminants
section_title: "Inequalities for mixed discriminants."
section_number: 8
pages: 23-27
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
---
This section summarizes a powerful application of stable polynomials from a
2008 paper of Gurvits [11].
We will use without mention the facts that log and exp are strictly increasing
functions on (0,∞). A function ρ : I→ R deﬁned on an interval I⊆ R is convex
provided that for all a1,a 2∈ I, ρ((a1 +a2)/2)≤ (ρ(a1) +ρ(a2))/2. It is strictly
convex if it is convex and equality holds here only when a1 = a2. A function
ρ :I→ R is (strictly) concave if−ρ is (strictly) convex. For example, for positive
realsa1,a 2 > 0 one has (√a1−√a2)2≥ 0, with equality only if a1 =a2. It follows
that log((a1 +a2)/2)≥ (log(a1) + log(a2))/2, with equality only if a1 =a2. That
is, log is strictly concave.
24 DAVID G. WAGNER
Jensen’s Inequality (Theorem 90 of [12]). Letρ :I→ R be deﬁned on an interval
I⊆ R, let ai∈I for i∈ [n], and let bi > 0 for i∈ [n] be such that ∑n
i=1bi = 1. If
ρ is convex then
ρ
( n∑
i=1
biai
)
≤
n∑
i=1
biρ(ai).
If ρ is strictly convex and equality holds, then a1 =a2 =··· =an.
For integer d ≥ 1, let G( d) = (1 − 1/d)d−1, and let G(0) = 1. Note that
G(1) = 0 0 = 1, and that G( d) is a strictly decreasing function for d≥ 1. For
homogeneousf∈ R[x] with nonnegative coeﬃcients, deﬁne the capacity off to be
cap(f) = inf
c>0
f(c)
c1··· cm
,
with the inﬁmum over the set of all c∈ Rm with ci > 0 for all i∈ [m].
Lemma 8.1 (Lemma 3.2 of [11]). Letf =∑d
i=0bix∈ R[x] be a nonzero univariate
polynomial of degree d with nonnegative coeﬃcients. If f is real stable then b1 =
f′(0)≥ G(d)cap(f), and if cap(f) > 0 then equality holds if and only if d≤ 1 or
f(x) =bd(x +ξ)d for some ξ >0.
Proof. If cap(f) = 0 then there is nothing to prove, so assume that cap( f) > 0.
If d = 0 then f′(0) = b1 = 0 = G(0)cap( f), and if d = 1 then f′(0) = b1 =
G(1)cap(f), so assume that d≥ 2. If f(0) = 0 then f′(0) = lim c→0f(c)/c≥
cap(f)> G(d)cap(f). Thus, assume that d≥ 2 andf(0) =b0 > 0. We may rescale
the polynomial so that b0 = 1. Now there are ai > 0 for i∈ [d] such that
f(x) =
d∏
i=1
(1 +aix),
and b1 =a1 +··· +ad. For any c> 0 we have
log(cap(f)c)
d ≤ log(f(c))
d = 1
d
d∑
i=1
log(1 +aic)≤ log
(
1 +b1c
d
)
,
by Jensen’s Inequality. It follows that cap( f)c≤ (1 +b1c/d)d for all c >0. Let
g(x) = (1 +b1x/d)d. Elementary calculus shows that
cap(g) = inf
c>0
g(c)
c = g(c∗)
c∗
= b1
G(d), in which c∗ = d
b1(d− 1).
Since cap(f)≤ cap(g), this yields the stated inequality. If equality holds, then
equality holds in the application of Jensen’s Inequality, and so f has the stated
form. □
Lemma 8.2 (Theorem 4.10 of [11]) . Let f ∈ SR[x1,...,x m] be real stable, with
nonnegative coeﬃcients, and homogeneous of degree m. Let g =∂mf|xm=0. Then
cap(g)≥ G(degm(d))cap(f).
Proof. We may assume that d = degm(f)≥ 1. Let ci > 0 for i∈ [m− 1], and let
pc(x) = f(c1,...,c m−1,x ). Since f has nonnegative coeﬃcients, pc⁄≡ 0. As in the
proof of Lemma 2.4(f), pc has degreed. By specialization, pc is real stable. Lemma
8.1 implies that
g(c) =p′
c(0)≥ G(d)cap(pc)≥ G(d)cap(f)
MULTIVARIATE STABLE POLYNOMIALS 25
for all c∈ Rm−1 with c > 0. If m = 1 then g = cap(g) is a constant. If m≥ 2
then for any such c letb = (c1··· cm−1)−1/(m−1). Since g is homogeneous of degree
m− 1,
g(c)
c1··· cm−1
=g(bc1,...,bc m−1)≥ G(d)cap(f).
It follows that cap(g)≥ G(d)cap(f). □
Theorem 8.3 (Theorem 2.4 of [11]) . Let f ∈ SR[x1,...,x m] be real stable, with
nonnegative coeﬃcients, and homogeneous of degree m. Let degi(f) = di and
ei = min{i,di} for each i∈ [m]. Then
∂1f(0)≥ cap(f)
m∏
i=2
G(ei).
Proof. Let gm = f and let gi−1 = ∂igi|xi=0 for all i∈ [m]. By contraction and
specialization, gi is real stable for each i ∈ [m]. Notice that g0 = ∂1f(0) =
cap(g0). By Lemma 8.2. cap( gi−1)≥ cap(gi)· G(degigi) for each i∈ [m]. But
degigi≤ degif =di, and degigi is at most the total degree ofgi, which isi. Hence
degigi≤ei, and thus G(degigi)≥ G(ei). Thus cap(gi−1)≥ cap(gi)·G(ei) for each
i∈ [m]. Combining these inequalities (and G( e1) = 1) gives the result. □
With the notation of Theorem 8.3, since ei≤ i for all i∈ [m] and G(d) is a
decreasing function of d, one has the inequality
m∏
i=2
G(ei)≥
m∏
i=2
G(i) =
m∏
i=2
(i− 1
i
)i−1
= m!
mm.
Thus, the following corollary is immediate.
Corollary 8.4. Letf∈ SR[x1,...,x m] be real stable, with nonnegative coeﬃcients,
and homogeneous of degree m. Then
∂1f(0)≥ m!
mm· cap(f).
Theorem 8.5 (Theorem 5.7 of [11]) . Let f ∈ SR[x1,...,x m] be real stable, with
nonnegative coeﬃcients, and homogeneous of degreem. Equality holds in the bound
of Corollary 8.4 if and only if there are nonnegative reals ai≥ 0 for i∈ [m] such
that
f(x) = (a1x1 +··· +amxm)m.
(We omit the proof.)
Lemma 8.6 (Fact 2.2 of [11]) . Let f ∈ R[x1,...,x m] be homogeneous of degree
m, with nonnegative coeﬃcients. Assume that ∂if(1) = 1 for all i∈ [m]. Then
cap(f) = 1.
Proof. Let f = ∑
αb(α)xα, so that if b(α)⁄= 0 then |α| = ∑m
i=1α(i) = m. By
hypothesis, for all i∈ [m],∑
αb(α)α(i) = 1. Averaging these over all i∈ [m] yields
f(1) = ∑
αb(α) = 1, so that cap( f)≤ 1. Conversely, let c∈ Rm with c > 0.
26 DAVID G. WAGNER
Jensen’s Inequality implies that
log(f(c)) = log
(∑
α
b(α)cα
)
≥
∑
α
b(α) log(cα) =
m∑
i=1
log(ci)
∑
α
b(α)α(i) = log(c1··· cm).
It follows that cap(f)≥ 1. □
Example 8.7 (van der Waerden Conjecture) . An m-by-m matrix A = (aij) is
doubly stochastic if all entries are nonnegative reals and every row and column
sums to one. In 1926, van der Waerden conjectured that if A is an m-by-m doubly
stochastic matrix then per(A)≥m!/mm, with equality if and only if A = (1/m)J,
the m-by-m matrix in which every entry is 1 /m. In 1981 this lower bound was
proved by Falikman, and the characterization of equality was proved by Egorychev.
These results follow immediately from Corollary 8.4 and Theorem 8.5, as follows.
It suﬃces to prove the result for an m-by-m doubly stochastic matrix A = (aij)
with no zero entries, by a routine limit argument. The polynomial
fA(x) =
m∏
j=1
(a1jx1 +··· +amjxm)
is clearly homogeneous and real stable, with nonnegative coeﬃcients and of degree
m, and such that degi(fA) =m for alli∈ [m]. Since A is doubly stochastic, Lemma
8.6 implies that cap(fA) = 1. Since
per(A) = ∂1fA(0),
Corollary 8.4 and Theorem 8.5 imply the results of Falikman and Egorychev, re-
spectively. Gurvits [11] also uses a similar argument to prove a reﬁnement of the
van der Waerden conjecture due to Schrijver and Valiant – see also [13].
Givenn-by-n matricesA1,...,Am, the mixed discriminant of A = (A1,...,A m) is
Disc(A) = ∂1 det(x1A1 +··· +xmAm)
⏐⏐
x=0.
This generalizes the permanent of an m-by-m matrix B = (bij) by considering the
collection of matrices A(B) = (A1,...,A m) deﬁned by Ah = diag(ah1,...,a hm) for
eachh∈ [m]. In this case one sees that
det(x1A1 +··· +xmAm) =fB(x)
with the notation of Example 8.7, and it follows that Disc( A(B)) = per(B).
Example 8.8 (Bapat’s Conjecture) . Generalizing the van der Waerden conjec-
ture, in 1989 Bapat considered the set Ω( m) of m-tuples of m-by-m matrices
A = (A1,...,A m) such that each Ai is positive semideﬁnite with trace tr( Ai) = 1,
and∑m
i=1Ai = I. For any doubly stochastic matrix B, A(B) is in this set. The
natural conjecture is that for all A∈ Ω(m), Disc(A)≥ m!/mm, and equality is
attained if and only if A = A((1/m)J). This was proved by Gurvits in 2006 –
again, it follows directly from Corollary 8.4 and Theorem 8.5. It suﬃces to prove
the result for A∈ Ω(m) such that each Ai is positive deﬁnite, by a routine limit
argument. By Proposition 2.1, for A∈ Ω(m), the polynomial
fA(x) = det(x1A1 +··· +xmAm)
MULTIVARIATE STABLE POLYNOMIALS 27
is real stable. Since eachAi is positive deﬁnite, all coeﬃcients offA are nonnegative,
fA is homogeneous of degreem, and degi(fA) =m for alli∈ [m]. Since A∈ Ω(m),
Lemma 8.6 implies that cap(fA) = 1. Thus, fA satisﬁes the hypothesis of Theorems
8.3 and 8.5, and since Disc( A) = ∂1fA(0), the result follows.
