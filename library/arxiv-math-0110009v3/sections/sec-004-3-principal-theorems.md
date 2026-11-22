---
doc_id: arxiv-math-0110009v3
doc_title: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003"
section_id: sec-004-3-principal-theorems
section_title: "Principal theorems"
section_number: 3
pages: 6-8
source_pdf: 0110009v3.pdf
source_sha256: bb0c97f2de33b0dd
toc_source: inferred
doc_brief: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003 — We develop an analogue for sphere packing of the linear programming bounds for error-correcting codes, and use it to prove upper bounds for the density of"
---
Our principal result is the following theorem. It is similar in spirit to work
of Siegel [S], but is capable of giving much better bounds. Gorbachev [Go] has
independently discovered essentially the same result, with a slightly diﬀerent
proof. (He concentrates on deriving Levenshtein’s bound using functions f
for which bf has fairly small support, but mentions that one could let the size
of the support go to inﬁnity.)
Theorem 3.1.
Suppose f : Rn →R is an admissible function, is not
identically zero, and satisﬁes the following two conditions:
(1) f(x) ≤0 for |x| ≥1, and
(2) bf(t) ≥0 for all t.
Then the center density of n-dimensional sphere packings is bounded above by
f(0)
2n bf(0)
.
Notice that because bf is nonnegative and not identically zero, we have
f(0) > 0. If bf(0) = 0, then we treat f(0)/ bf(0) as +∞, so the theorem is still
true, although only vacuously.
Proof. It is enough to prove this for periodic packings, since they come
arbitrarily close to the greatest packing density (see Appendix A). In particu-
lar, suppose we have a packing given by the translates of a lattice Λ by vectors
v1, . . . , vN, whose diﬀerences are not in Λ. If we choose the scale so that the
radius of the spheres in our packing is 1/2 (i.e., no two centers are closer than
1 unit), then the center density is given by
δ =
N
2n|Λ|.
By the Poisson summation formula (2.1),
X
x∈Λ
f(x + v) = 1
|Λ|
X
t∈Λ∗
e−2πi⟨v,t⟩bf(t)
for all v ∈Rn. It follows that
X
1≤j,k≤N
X
x∈Λ
f(x + vj −vk) = 1
|Λ|
X
t∈Λ∗
bf(t)

X
1≤j≤N
e2πi⟨vj,t⟩

2
.
Every term on the right is nonnegative, so the sum is bounded from below by
the summand with t = 0, which equals N 2 bf(0)/|Λ|. On the left, the vector
NEW UPPER BOUNDS ON SPHERE PACKINGS I
695
x+vj−vk is the diﬀerence between two centers in the packing, so |x+vj−vk| < 1
if and only if x = 0 and j = k. Whenever |x + vj −vk| ≥1, the corresponding
term in the sum is nonpositive, so we get an upper bound of Nf(0) for the
entire sum. Thus,
Nf(0) ≥N 2 bf(0)
|Λ|
,
i.e.,
δ ≤
f(0)
2n bf(0)
,
as desired.
This theorem was ﬁrst proved by a more complicated argument, which is
given in the companion paper [C].
The hypotheses and conclusion of Theorem 3.1 are invariant under rotat-
ing the function f. Hence, we can assume without loss of generality that f has
radial symmetry, since otherwise we can replace f with the average of its ro-
tations. The Fourier transform maps radial functions to radial functions, and
Proposition 2.1 gives us the corresponding one-dimensional integral transform.
As an example of how to apply Theorem 3.1 in one dimension, consider
the function (1 −|x|)χ[−1,1](x). It satisﬁes the hypotheses of Theorem 3.1 in
dimension n = 1, because it is the convolution of χ[−1/2,1/2](x) with itself, and
therefore its Fourier transform is
sin πt
πt
2
.
Thus, this function satisﬁes the hypotheses of Theorem 3.1. We get a bound
of 1/2 for the center density in one dimension, which is a sharp bound. This
example generalizes to higher dimensions by replacing χ[−1/2,1/2](x) with the
characteristic function of a ball about the origin. However, the bound obtained
is only the trivial bound (density can be no greater than 1), so we omit the
details. In later sections we apply Theorem 3.1 to prove nontrivial bounds.
It will be useful later to have the following alternative form of Theorem 3.1:
Theorem 3.2.
Suppose f : Rn →R is an admissible function satisfying
the following three conditions:
(1)
f(0) = bf(0) > 0,
(2)
f(x) ≤0 for |x| ≥r, and
(3)
bf(t) ≥0 for all t.
Then the center density of sphere packings in Rn is bounded above by (r/2)n.
696
HENRY COHN AND NOAM ELKIES
Theorem 3.2 can be obtained either from rescaling the variables in The-
orem 3.1 or from the following direct proof. For simplicity we deal only with
the case of lattice packings, but as in the proof of Theorem 3.1 the argument
extends to all periodic packings (and hence to all packings).
Proof for lattice packings. For lattice packings, the density bound in the
theorem statement simply amounts to the claim that every lattice of covolume 1
contains a nonzero vector of length at most r. We will prove this ﬁrst for lattices
Λ of covolume 1 −ε, and then let ε →0+. For such lattices,
X
x∈Λ
f(x) =
1
1 −ε
X
t∈Λ∗
bf(t),
by Poisson summation. If all nonzero vectors in Λ had length greater than r,
then all terms except f(0) on the left-hand side would be nonpositive. Because
all terms on the right-hand side are nonnegative, we would have
f(0) ≥
X
x∈Λ
f(x) =
1
1 −ε
X
t∈Λ∗
bf(t) ≥
bf(0)
1 −ε.
However,
bf(0)
1 −ε = f(0)
1 −ε > f(0),
which is a contradiction. Thus, every lattice of covolume strictly less than 1
must have a nonzero vector of length r or less, and it follows that the same
holds for covolume 1.
It seems natural to try to prove Theorem 3.2 by applying Poisson summa-
tion directly to a lattice of covolume 1, but some sort of rescaling and limiting
argument seems to be needed. We included the proof to illustrate how to do
this.
Logan [Lo] has studied the optimization problem from Theorem 3.2 in the
one-dimensional case (for reasons unconnected to sphere packing), but we do
not know of any previous study of the higher-dimensional cases. Unfortunately,
these cases seem much more diﬃcult than the one-dimensional case.
