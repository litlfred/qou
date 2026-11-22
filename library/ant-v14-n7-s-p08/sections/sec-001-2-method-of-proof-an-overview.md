---
doc_id: ant-v14-n7-s-p08
doc_title: "Burgess bounds for short character sums evaluated at forms"
section_id: sec-001-2-method-of-proof-an-overview
section_title: "Method of proof: an overview"
section_number: 2
pages: 8-11
source_pdf: ant-v14-n7-s-p08.pdf
source_sha256: 81b8f00fe5fbd0f6
toc_source: inferred
doc_brief: "Burgess bounds for short character sums evaluated at forms — 11 sections: Front matter; Introduction; Method of proof: an overview"
---
In this section we recall the main points of the Burgess method in dimension 1, outline the difﬁculties that
arise in n ≥2 dimensions, and then sketch how we overcome these difﬁculties to obtain our main theorem.
At its heart, the Burgess method in the classical 1-dimensional setting builds from a character sum
S(N; H) of length H < q, a character sum over a complete set of residues modulo q. Doing so by a
Fourier expansion only works efﬁciently if the sum is not too short, that is, if the character sum is of
length at least H ≫q1/2+ε (see Section A.3). When H ≪q1/2+ε, Burgess’s method instead dissects
and translates the “short” sum into many “short-short” sums of length H/p for some prime p of size
roughly P (with P to be chosen optimally in terms of H and q). Averaging this process over sufﬁciently
many choices of p, the short-short sums become distributed across a long interval of length q. If this
process is done with enough redundancy, the starting points of these short-short sums nearly cover a full
set of residues modulo q. Simultaneously, Burgess considers not just an average of these short-short
sums, but a 2r-th moment, leading to the study of a sum over starting points m, of the form
X
m
max
k≤2H/P |S(m, k)|2r.
(2-1)
At this point, positivity allows one to sum over all 1 ≤m ≤q so that the sum over m is a complete
set of residues. The Menshov–Rademacher technique allows one to deduce a bound for this maximal
moment (2-1) from a bound for the nonmaximal moment
X
m (mod q)
|S(m, k)|2r
(2-2)
in which we think of m as varying over the starting points of the short-short sums and k ≤2H/P as being
the new short-short length. We may write (2-2) equivalently as
X
x1,...,x2r∈(0,k]
X
m (mod q)
χ(F{x}(m)),
(2-3)
in which F{x}(m) = (m + x1)(m + x2)1−1 · · · (m + x2r)1−1. If F{x}(m) is not a perfect 1-th power
modulo q, then the Weil bound O(q1/2) applies to the sum over m, and we say the tuple x is “good”
(which is the generic case); otherwise x is “bad” (which is a sparse case) and we apply the trivial bound
O(q) to the sum over m. Balancing the contributions of these two cases leads to the optimal choice of P
and the Burgess bound (1-1).
Generalizing this argument to the n-dimensional case, we will prove in (5-9) that for any r ≥1,
|S(F; N, H)| ≪(log P)Pn−1/2r∥H∥−1/2r
 X
m
|mi|≤2q
max
k≤2H/P |S(F; m, k)|2r
1/(2r)
.
(2-4)
Burgess bounds for short character sums evaluated at forms
1919
This will ultimately reduce the problem of bounding |S(F; N, H)| to bounding
X
m (mod q)
|S(F; m, k)|2r ≤
X
x(1),...,x(2r)
x(i)∈(0,k]

X
m (mod q)
χ(F{x}(m))

,
(2-5)
where we deﬁne for each collection {x} = {x(1), . . . , x(2r)} with x(i) ∈Zn the polynomial
F{x}(X) = F{x}(X1, . . . , Xn) =
2r
Y
i=1
(F(X + x(i)))δ(i),
(2-6)
where δ(i) = +1 if i is odd and 1 −1 if i is even. One would hope that if the x(i) are appropriately
independent (that is, the “good” case), a generalization of the Weil bound would yield square-root
cancellation, that is an O(qn/2) bound for

X
m (mod q)
χ(F{x}(m))

.
(2-7)
But achieving such a bound has been a critical barrier to generalizing the Burgess method to this
n-dimensional setting. One difﬁculty is that the leading form of F{x}(X) (the homogeneous part of highest
degree) deﬁnes a highly singular projective variety, whereas previous literature on Weil bounds required
this either to be a nonsingular projective variety [Katz 2002], or could only allow certain singular varieties
that are not general enough for our application; see, e.g., [Rojas-León 2005; 2006].
Moreover, in dimensions n ≥2, as well as the two extremal cases in which the sum (2-7) is O(qn/2)
or O(qn), there may be intermediate cases O(q(n+ j−1)/2) for j = 1, . . . , n + 1. Indeed, suppose we
partition the {x(1), . . . , x(2r)} ∈(0, k]2r into the following types: those belonging to a good set denoted
by Good(k), are such that

X
m (mod q)
χ(F{x}(m))

 ≤Cqn/2
for a certain constant C, and those belonging to the j-th bad set, denoted by Bad j(k), are such that

X
m (mod q)
χ(F{x}(m))

 > Cq(n+ j−1)/2
but

X
m (mod q)
χ(F{x}(m))

 ≤Cq(n+ j)/2.
Then according to this dissection,
X
m (mod q)
|S(F; m, k)|2r ≤C|Good(k)|qn/2 + C
n
X
j=1
|Bad j(k)|q(n+ j)/2.
(2-8)
Certainly |Good(k)| ≤∥k∥2r. The real question is how to bound |Bad j(k)| for each j = 1, . . . , n.
The recent work of the second author [Xu 2018] proves a set of bounds that are perfectly suited for our
purposes. This takes the form of a “stratiﬁcation,” in the spirit of [Fouvry 2000, Proposition 1.0; Laumon
2000, Proposition 3.2, Theorem 3.3; Fouvry and Katz 2001, Theorems 1.1 and 1.2].
1920
Lillian B. Pierce and Junyan Xu
To give the ﬂavor of this stratiﬁcation, we state here a special case in dimension n = 2 (see Section 4
and in particular Theorem 4.4 for the full setting). Let k = (k, k, . . . , k) be a ﬁxed tuple in Zn, with
k ≥1. We will consider tuples x ∈Zn that lie in the box x ∈(0, k], and more generally, a collection
{x} = {x(1), . . . , x(2r)} ∈(0, k]2r of 2r such n-tuples.
Theorem 2.1. Let n =2 and let r, 1, D ≥1 be ﬁxed. There exists a constant C =C(n,r, D) and a constant
C′′ = C′′(n,r, 1, D) such that the following holds. For any prime q, for any nonprincipal multiplicative
Dirichlet character χ of order 1 modulo q, and for any F ∈Fq[x1, x2] that is (1, q)-admissible, for
every tuple k = (k, k),
#

{x(1), . . . , x(2r)} ∈(0, k]2r :

X
m (mod q)
χ(F{x}(m))

 > Cq(n+ j−1)/2

≤C′′



k4r
if j = 0,
k3r+1
if j = 1,
k2r
if j = 2.
We can interpret this as follows: for n = 2, the trivial bound for the number of collections {x} in the
box (0, k]2r ⊂Z2nr is k4r. When j = 1, we see that at most O(k3r+1) collections can violate square-root
cancellation, i.e., as soon as r ≥2, generically square-root cancellation holds. This stratiﬁcation, in its
general formulation (Theorem 4.4) is the key input which allows us to prove the Burgess bound for all
dimensions n ≥2. (See Section A.1 for a further demonstration of why the full stratiﬁcation is useful.)
We stated Theorem 2.1 for simplicity in the case where the length k has identical values in each coordi-
nate. In our argument, we must instead allow k = (k1, . . . , kn) with ki varying independently; in particular
this arises in the step when we deduce a bound for the maximal moment in (2-4) from the nonmaximal
moment in (2-5). This raises another difﬁculty in the multi-dimensional setting, which we now outline.
Xu’s stratiﬁcation (Theorem A, Theorem 4.1) shows that for each j = 1, . . . , n, the collections
{x(1), . . . , x(2r)} counted by Bad j(k) lie on a certain subscheme over Fq with a certain codimension. In
general, ﬁx a dimension R, let X ⊂AR
Fq be a subscheme of codimension ϖ and let U be the sum of the
degrees of its irreducible components. Given subsets Mi ⊂Fq, deﬁne the “box” M = QR
i=1 Mi ⊂AR
Fq.
We require a bound for
IX(M) := #

X(Fq) ∩
R
Y
i=1
Mi

,
(2-9)
which depends only on the codimension of X and the degree of the irreducible components of X. A trivial
bound, best possible if codim X = 0, is IX(M) ≤∥M∥:= QR
i=1 |Mi|. We need to improve on this when
codim X ≥1.
To gain an intuition, consider the case of R = 2 and X of codimension 1. A naive hope might be
that IX(M) ≤∥M∥1/2 = ∥M∥· |M1|−1/2|M2|−1/2. But this need not be true. Supposing for example that
|M1| ≈1 is very small while |M2| is very large, it could happen that X of codimension 1 lies along the
subset M2 of M, thus leading to the bound IX(M) ≫|M2| = ∥M∥· |M1|−1 ≈∥M∥. Thus in general, in
estimating IX(M) we can only expect to save factors corresponding to the smallest components of the
“box” M.
Burgess bounds for short character sums evaluated at forms
1921
Concretely, for X of codimension ϖ, we use the fact that if
1 ≤|M1| ≤|M2| ≤· · · ≤|MR| < ∞,
(2-10)
then by [Xu 2018, Lemma 1.7],
IX(M) ≤U∥M∥· |M1|−1|M2|−1 · · · |Mϖ|−1,
(2-11)
where U is the sum of the degrees of the irreducible components of X. In our setting, we will apply such
bounds in Section 6 when using a Menshov–Rademacher technique to deduce a bound for a maximal
moment from a nonmaximal moment. Here, in order to guarantee the ordering (2-10) we must permute
variables in a delicate argument, and apply rearrangement inequalities in order to conclude. This is
another novel aspect of our method.
