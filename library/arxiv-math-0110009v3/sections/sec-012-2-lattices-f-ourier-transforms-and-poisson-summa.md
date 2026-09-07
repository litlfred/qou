---
doc_id: arxiv-math-0110009v3
doc_title: "New upper bounds on sphere packings I"
section_id: sec-012-2-lattices-f-ourier-transforms-and-poisson-summa
section_title: "Lattices, F ourier transforms, and Poisson summation"
section_number: 2
pages: 4-26
source_pdf: 0110009v3.pdf
source_sha256: bb0c97f2de33b0dd
doc_brief: "New upper bounds on sphere packings I — We develop an analogue for sphere packing of the linear progr amming bounds for error-correcting codes, and use it to prove upper bounds for the density of"
---
Given a lattice Λ ⊂ Rn, the dual lattice Λ ∗ is deﬁned by
Λ ∗ = {y | ⟨x, y ⟩ ∈Z for all x ∈ Λ };
it is easily seen to be the lattice with basis given by the dual basis to any
basis of Λ. The covolume |Λ | = vol(Rn/ Λ) of a lattice Λ is the volume of any
fundamental parallelotope. It satisﬁes |Λ ||Λ ∗| = 1. Given any lattice Λ with
NEW UPPER BOUNDS ON SPHERE PACKINGS I 693
shortest nonzero vectors of length r, the density of the corresponding lattice
packing is
π n/ 2
(n/ 2)!
( r
2
) n 1
|Λ | ,
and the center density is therefore ( r/ 2)n/ |Λ |.
The Fourier transform of an L1 function f : Rn → R will be deﬁned by
ˆf (t) =
∫
Rn
f (x)e2πi ⟨x,t ⟩dx.
Proposition 2.1. Let α = n/ 2 − 1. If f : Rn → R is a radial function ,
then
ˆf (t) = 2 π |t|−α
∫ ∞
0
f (r)Jα (2πr |t|)rn/ 2 dr,
where “ f (r)” denotes the common value of f on vectors of length r.
For a proof, see Theorem 9.10.3 of [AAR]. Here Jα denotes the Bessel
function of order α .
We will deal with functions f : Rn → R to which the Poisson summation
formula applies; i.e., for every lattice Λ ⊂ Rn and every vector v ∈ Rn,
(2.1)
∑
x∈Λ
f (x + v) = 1
|Λ |
∑
t∈Λ ∗
e−2πi ⟨v,t ⟩ˆf (t),
with both sides converging absolutely. It is not hard to veri fy that the right-
hand side of the Poisson summation formula is the Fourier ser ies for the left-
hand side (which is periodic under translations by elements of Λ), but of course
even when the sum on the left-hand side converges, some condi tions are needed
to make it equal its Fourier series.
For our purposes, we need only the following suﬃcient condit ion:
Deﬁnition 2.2. A function f : Rn → R is admissible if there is a constant
δ > 0 such that |f (x)| and |ˆf (x)| are bounded above by a constant times
(1 + |x|)−n−δ .
Admissibility implies that f and ˆf are continuous, and that both sides of
(2.1) converge absolutely. These two conditions alone do no t suﬃce for Poisson
summation to hold, but admissibility does. For a proof for th e integer lattice
Zn, see Corollary 2.6 of Chapter VII of [SW]. The general case ca n be proved
similarly, or derived by a linear change of variables.
We could deﬁne admissibility more broadly, to include every function to
which Poisson summation applies, but the restricted deﬁnit ion above appears
to cover all the useful cases, and is more concrete.
694 HENRY COHN AND NOAM ELKIES
3. Principal theorems
Our principal result is the following theorem. It is similar in spirit to work
of Siegel [S], but is capable of giving much better bounds. Go rbachev [Go] has
independently discovered essentially the same result, wit h a slightly diﬀerent
proof. (He concentrates on deriving Levenshtein’s bound us ing functions f
for which ˆf has fairly small support, but mentions that one could let the size
of the support go to inﬁnity.)
Theorem 3.1. Suppose f : Rn → R is an admissible function , is not
identically zero, and satisﬁes the following two conditions :
(1) f (x) ≤ 0 for |x| ≥ 1, and
(2) ˆf (t) ≥ 0 for all t.
Then the center density of n-dimensional sphere packings is bounded above by
f (0)
2nˆf (0)
.
Notice that because ˆf is nonnegative and not identically zero, we have
f (0) > 0. If ˆf (0) = 0, then we treat f (0)/ ˆf (0) as + ∞, so the theorem is still
true, although only vacuously.
Proof. It is enough to prove this for periodic packings, since they c ome
arbitrarily close to the greatest packing density (see Appe ndix A). In particu-
lar, suppose we have a packing given by the translates of a lat tice Λ by vectors
v1, . . . , v N , whose diﬀerences are not in Λ. If we choose the scale so that t he
radius of the spheres in our packing is 1 / 2 (i.e., no two centers are closer than
1 unit), then the center density is given by
δ = N
2n|Λ | .
By the Poisson summation formula (2.1),
∑
x∈Λ
f (x + v) = 1
|Λ |
∑
t∈Λ ∗
e−2πi ⟨v,t ⟩ˆf (t)
for all v ∈ Rn. It follows that
∑
1≤j,k ≤N
∑
x∈Λ
f (x + vj − vk) = 1
|Λ |
∑
t∈Λ ∗
ˆf (t)
⏐⏐⏐⏐⏐⏐
∑
1≤j≤N
e2πi ⟨vj ,t ⟩
⏐⏐⏐⏐⏐⏐
2
.
Every term on the right is nonnegative, so the sum is bounded f rom below by
the summand with t = 0, which equals N 2ˆf (0)/ |Λ |. On the left, the vector
NEW UPPER BOUNDS ON SPHERE PACKINGS I 695
x+vj−vk is the diﬀerence between two centers in the packing, so |x+vj −vk| < 1
if and only if x = 0 and j = k. Whenever |x + vj − vk| ≥ 1, the corresponding
term in the sum is nonpositive, so we get an upper bound of N f(0) for the
entire sum. Thus,
N f(0) ≥ N 2ˆf (0)
|Λ | ,
i.e.,
δ ≤ f (0)
2nˆf (0)
,
as desired.
This theorem was ﬁrst proved by a more complicated argument, which is
given in the companion paper [C].
The hypotheses and conclusion of Theorem 3.1 are invariant u nder rotat-
ing the function f . Hence, we can assume without loss of generality that f has
radial symmetry, since otherwise we can replace f with the average of its ro-
tations. The Fourier transform maps radial functions to rad ial functions, and
Proposition 2.1 gives us the corresponding one-dimensiona l integral transform.
As an example of how to apply Theorem 3.1 in one dimension, con sider
the function (1 − |x|)χ [−1, 1](x). It satisﬁes the hypotheses of Theorem 3.1 in
dimension n = 1, because it is the convolution of χ [−1/ 2, 1/ 2](x) with itself, and
therefore its Fourier transform is
( sin πt
πt
) 2
.
Thus, this function satisﬁes the hypotheses of Theorem 3.1. We get a bound
of 1 / 2 for the center density in one dimension, which is a sharp bou nd. This
example generalizes to higher dimensions by replacing χ [−1/ 2, 1/ 2](x) with the
characteristic function of a ball about the origin. However , the bound obtained
is only the trivial bound (density can be no greater than 1), s o we omit the
details. In later sections we apply Theorem 3.1 to prove nont rivial bounds.
It will be useful later to have the following alternative for m of Theorem 3.1:
Theorem 3.2. Suppose f : Rn → R is an admissible function satisfying
the following three conditions :
(1) f (0) = ˆf (0) > 0,
(2) f (x) ≤ 0 for |x| ≥ r, and
(3) ˆf (t) ≥ 0 for all t.
Then the center density of sphere packings in Rn is bounded above by (r/ 2)n.
696 HENRY COHN AND NOAM ELKIES
Theorem 3.2 can be obtained either from rescaling the variab les in The-
orem 3.1 or from the following direct proof. For simplicity w e deal only with
the case of lattice packings, but as in the proof of Theorem 3. 1 the argument
extends to all periodic packings (and hence to all packings) .
Proof for lattice packings. For lattice packings, the density bound in the
theorem statement simply amounts to the claim that every lat tice of covolume 1
contains a nonzero vector of length at most r. We will prove this ﬁrst for lattices
Λ of covolume 1 − ε , and then let ε → 0+. For such lattices,
∑
x∈Λ
f (x) = 1
1 − ε
∑
t∈Λ ∗
ˆf (t),
by Poisson summation. If all nonzero vectors in Λ had length g reater than r,
then all terms except f (0) on the left-hand side would be nonpositive. Because
all terms on the right-hand side are nonnegative, we would ha ve
f (0) ≥
∑
x∈Λ
f (x) = 1
1 − ε
∑
t∈Λ ∗
ˆf (t) ≥
ˆf (0)
1 − ε .
However,
ˆf (0)
1 − ε = f (0)
1 − ε > f (0),
which is a contradiction. Thus, every lattice of covolume st rictly less than 1
must have a nonzero vector of length r or less, and it follows that the same
holds for covolume 1.
It seems natural to try to prove Theorem 3.2 by applying Poiss on summa-
tion directly to a lattice of covolume 1, but some sort of resc aling and limiting
argument seems to be needed. We included the proof to illustr ate how to do
this.
Logan [Lo] has studied the optimization problem from Theore m 3.2 in the
one-dimensional case (for reasons unconnected to sphere pa cking), but we do
not know of any previous study of the higher-dimensional cas es. Unfortunately,
these cases seem much more diﬃcult than the one-dimensional case.
4. Homogeneous spaces
The space Rn is a 2- point homogeneous space; i.e., its isometry group acts
transitively on ordered pairs of points a given distance apa rt. By studying
packing problems in homogeneous spaces, one can put Theorem 3.1 into a
broader context, in which it can be seen to be analogous to pre viously known
theorems about compact homogeneous spaces.
NEW UPPER BOUNDS ON SPHERE PACKINGS I 697
We start by reviewing the theory of compact homogeneous spac es. See
Chapter 9 of [CS] for a more detailed treatment of this materi al. Suppose X
is a compact 2-point homogeneous space. We assume that X is a connected
Riemannian manifold, of positive dimension. We can write X as G/H , where
(G, H ) is a Gelfand pair of Lie groups. Then L2(X) is a Hilbert space direct
sum of distinct irreducible representations of G, say ˆ⨁ ∞
j=0Vj. For each j,
evaluation gives a map fj : X → V ∗
j , because Vj turns out to consist of
continuous functions. We deﬁne
Kj(x, y ) = ⟨fj(x), f j(y)⟩.
This is a positive deﬁnite kernel: for every ﬁnite subset C ⊆ X, we have
∑
x,y ∈C
Kj(x, y ) =
⏐⏐⏐⏐⏐
∑
x∈C
fj(x)
⏐⏐⏐⏐⏐
2
≥ 0.
Because of G-invariance, Kj(x, y ) depends only on the distance between x and
y. This function of the distance is a zonal spherical function ; we can deﬁne a
way of measuring distance t(x, y ) and an ordering of the Vj’s so that Kj(x, y )
is a polynomial Pj of degree j evaluated at t(x, y ). In general, t maps X × X
to [0 , 1], and t(x, y ) = 1 if and only if x = y (note that it is not a metric). For
the unit sphere in Rn, we take t(x, y ) = (1 + ⟨x, y ⟩)/ 2, and the polynomial Pj
is the Jacobi polynomial P (α,β )
j (t), where α = β = (n − 3)/ 2.
Now suppose C is a ﬁnite subset of X. We get inequalities on C from the
fact that for each j, the sum ∑
x∈C fj(x) has nonnegative norm. We can apply
these inequalities as follows to get an upper bound for the si ze of C, in terms
of the minimal distance between points of C:
Theorem 4.1 (Delsarte [D]). Suppose
f (t) =
m∑
j=0
ajPj(t)
with aj ≥ 0 for all j and f (t) ≤ 0 for 0 ≤ t ≤ τ . If t(x, y ) ≤ τ whenever x and
y are distinct points of C, then
|C| ≤ f (1)/a 0.
Proof. Suppose C satisﬁes t(x, y ) ≤ τ for all distinct x, y ∈ C. Then
consider ∑
x,y ∈C
f (t(x, y )).
This sum is bounded above by |C|f (1) since t(x, y ) ≤ τ unless x = y, and
is bounded below by |C|2a0 since f − a0 is a positive deﬁnite kernel. Thus,
|C| ≤ f (1)/a 0.
698 HENRY COHN AND NOAM ELKIES
Theorem 4.1 is the analogue of Theorem 3.1 for compact homoge neous
spaces. To see the analogy clearly, we need to study Rn as a homogeneous
space.
We can write Rn as G/H , where G is the group of isometries of Rn and
H = O(n). Then we need to decompose L2(Rn) in terms of irreducible repre-
sentations of G. It is no longer a direct sum, but it can be written as a direct
integral; speciﬁcally, L2(Rn) =
∫ ∞
0 π r dr, where π r is the irreducible represen-
tation of G consisting of functions whose Fourier transforms are distr ibutions
with support on the sphere of radius r.
We can ﬁnd the zonal spherical functions as follows. The repr esentation π r
is generated by the functions x ↦→e2πi ⟨x,y ⟩ with |y| = r, so π ∗
r consists of
functions on the sphere of radius r. The evaluation map from Rn to π ∗
r takes
a point x ∈ Rn to the function y ↦→e2πi ⟨x,y ⟩ on the sphere of radius r. Thus,
the zonal spherical functions are given by
Kr(x1, x 2) =
∫
|y|=r
e2πi ⟨y,x 1−x2⟩dy.
(This of course depends only on |x1 − x2|, and can be evaluated explicitly in
terms of Bessel functions using Proposition 2.1.) In other w ords, they are given
by functions whose Fourier transforms are delta functions o n spheres centered
at the origin. See Section 4.15 of [DM] for a more detailed dis cussion of this
point of view.
Now the analogue of positive combinations of the zonal spher ical func-
tions Pj(t) from the compact case is radial functions with nonnegative Fourier
transform, and we can see that Theorem 3.1 corresponds to 4.1 .
5. Conditions for a sharp bound
In one dimension, we have already seen how to use Theorem 3.1 t o solve
the (admittedly trivial) sphere packing problem. Based on n umerical evidence
and analogy with the kissing problem, we conjecture that it c an also be used
to get sharp bounds in dimensions 2, 8, and 24. For reasons to b e explained
shortly, it is more convenient to work with Theorem 3.2 inste ad of Theorem 3.1,
so we shall do so; we can convert everything to the framework o f Theorem 3.1
by rescaling the variables.
In each of dimensions 1, 2, 8, and 24, the densest known packin g is a lattice
packing, given by a lattice that is homothetic to its dual. Th is lattice is Z in
dimension 1, the A2 root lattice (i.e., the hexagonal lattice) in dimension 2, t he
E8 root lattice in dimension 8, and the Leech lattice in dimensi on 24. See [CS]
for information about these lattices. Each of these lattice s except A2 actually
equals its dual, but that is not true for A2. However, we can rescale A2 so that
the rescaled lattice is isodual, i.e., isometric with its own dual (in this case,
via a rotation).
NEW UPPER BOUNDS ON SPHERE PACKINGS I 699
Suppose Λ is any lattice of covolume 1, such as an isodual latt ice, and f
is a radial function giving a sharp bound on Λ via Theorem 3.2 ( i.e., r is the
length of the shortest nonzero vector of Λ). By Poisson summa tion, we have
∑
x∈Λ
f (x) =
∑
x∈Λ ∗
ˆf (x).
Given the inequalities on f and ˆf , the only way this equation can hold is if f
vanishes on Λ \ {0} and ˆf vanishes on Λ ∗ \ {0}. This puts strong constraints
on f and ˆf . When Λ is isodual, the vector lengths in Λ and Λ ∗ are the same,
so f and ˆf must both vanish on Λ \ {0}.
Of course, there are similar constraints on f for a sharp bound in Theo-
rem 3.1 (as opposed to Theorem 3.2), but we prefer to work with this context,
since the isodual normalizations are more pleasant, and are the standard nor-
malizations for E8 and the Leech lattice.
It is natural to try to guess f from our knowledge of its roots. For example,
in one dimension we could try
f (x) = (1 − x2)
∏
k≥2
(
1 − x2
k2
) 2
= 1
1 − x2
( sin πx
πx
) 2
,
which clearly satisﬁes f (x) ≤ 0 for |x| ≥ 1 and has the right zeros. In fact, one
can compute its Fourier transform and check that ˆf is nonnegative everywhere
(it has support [ −1, 1] and is positive in ( −1, 1)), so it solves the sphere packing
problem in dimension 1, in a diﬀerent way from the function in the previous
section.
Unfortunately, it seems diﬃcult to generalize this approac h to higher di-
mensions. One can generalize this function by replacing the sine function with
a Bessel function (see Proposition 6.1), but that does not yi eld a sharp bound
in dimensions greater than 1. Attempts to write down a produc t with zeros at
the right places for a sharp bound lead to products that seem i ntractable.
One important thing to note is that for a sharp bound above dim ension 1,
it is not possible for ˆf to have compact support, as it does in the examples
involving sine and Bessel functions. If it did, then f could not have suﬃciently
densely-spaced zeros. To be precise, if ˆf is a radial function with support in
the ball B(0, R ) of radius R about the origin, then the common value f (r) on
vectors of radius r satisﬁes
f (r) =
∫
B(0,R )
ˆf (t)e2πi ⟨rx,t ⟩dt,
where x is any vector with |x| = 1. This deﬁnes an entire function of r, and
for all complex r,
|f (r)| ≤ e2πR |r|
∫
B(0,R )
|ˆf (t)| dt,
700 HENRY COHN AND NOAM ELKIES
so f is a function of exponential type, and Jensen’s formula impl ies that f can
have at most linearly spaced zeros (see Section 15.20 of [Ru] ). However, the
nonzero vectors in the Leech lattice have lengths
√
2k for integers k > 1, and
those in E8 have lengths
√
2k for integers k > 0. The function f must vanish
at those vector lengths, and these roots are too densely spac ed for ˆf to have
compact support. Of course, f also cannot have compact support (because ˆf
vanishes on Λ ∗ \ {0}).
One might wonder whether the restriction to radial function s is misleading:
perhaps a nonradial function could be constructed more natu rally. We cannot
rule out that possibility, but consider it unlikely. Even if f is not radial, a
sharp bound implies that f and ˆf must vanish on concentric spheres centered
at the origin and passing through the nonzero points of Λ and Λ ∗, respectively.
The simplest reason is that if f proves that Λ is optimal, then it proves the
same for every rotation of Λ. Alternatively, after rotation al symmetrization
f and ˆf must vanish on these spheres, and the inequalities on their v alues
then imply that they must have vanished before symmetrizati on (the average
of nonnegative values vanishes if and only if the values all d o). It would seem
strange for f to vanish on these spheres without being radial, but of cours e we
cannot rule it out.
6. Stationary points
We do not know how to use Theorem 3.1 to match the best density b ound
known in high dimensions, that of Kabatiansky and Levenshte in [KL]. How-
ever, it provides a new proof of the second-best bound known, due to Leven-
shtein [Lev]:
∆ ≤
jn
n/ 2
(n/ 2)!24n ,
where jt is the smallest positive zero of the Bessel function Jt. (For more
information about the asymptotics of this bound and how it co mpares with
other bounds, see page 19 of [CS], but note that equation (42) is missing the
exponent in jn
n/ 2.) We will show how to use a calculus of variations argument
to ﬁnd functions that prove that bound. This approach is anal ogous to that
used by Levenshtein. Yudin [Y] has also given a proof of Leven shtein’s bound
that seems reminiscent of our general approach, but not iden tical.
To construct a function f for use in Theorem 3.1, we begin by supposing
that there is a function g such that f (x) = (1 − |x|2)ˆg(x)2, so that f auto-
matically satisﬁes the inequality f (x) ≤ 0 for |x| ≥ 1. (We write ˆg instead of
g for convenience later.) Assume that g is radial, and has support in the ball
of radius R about the origin; we discuss these assumptions later. Notic e that
nothing in our setup requires ˆf to be nonnegative, so we must check for this
property later.
NEW UPPER BOUNDS ON SPHERE PACKINGS I 701
We have ˆf = g ∗ (g + Lg), where ∗ denotes convolution and
L = 1
4π 2
n∑
j=1
∂ 2
∂t 2
j
,
so that under the Fourier transform, L corresponds to multiplication by −|x|2.
We require f (0) = 1, i.e.,
∫
Rn g = 1. We want to maximize ˆf (0), subject to
this constraint. Notice that
ˆf (0) =
∫
Rn
g(0 − t)(g + Lg)(t) dt =
∫
Rn
g(t)(g + Lg)(t) dt =
∫
Rn
g(g + Lg),
because g is radial (and hence even).
Perturb g to g+h, where h has integral zero (so that f (0) does not change)
and has support in the ball of radius R. Then the ﬁrst order change in ˆf (0) is
∫
Rn
(gh + hg + gLh + hLg) = 2
∫
Rn
h(g + Lg)
(where the equality comes from integration by parts).
In order to have this vanish whenever
∫
Rn h = 0, the function g + Lg must
be constant (within the support of g), so for some constant c we have
g + Lg = cχ R,
where χ R is the characteristic function of the ball of radius R about 0. Then
it follows from Proposition 2.1 that
(1 − |x|2)ˆg(x) = c(R/ |x|)n/ 2Jn/ 2(2πR |x|).
Now 2 πR must be a zero of Jn/ 2 for the right-hand side to vanish at
|x| = 1, and c is determined (given R) by
1 =
∫
Rn
g =
∫
Rn
g + Lg =
∫
Rn
cχ R = cRnπ n/ 2/ (n/ 2)! .
(The function g + Lg has the same integral as g, because integration by parts
shows that Lg has integral 0.)
In fact, we take 2 πR to be the ﬁrst positive root jn/ 2 of Jn/ 2, in order
to make ˆf nonnegative everywhere. To check that it is indeed nonnegat ive
everywhere then, we use the equation
ˆf = g ∗ (g + Lg) = g ∗ (cχ R).
If g is nonnegative everywhere, then so is ˆf . We can now determine g explicitly:
We know that g + Lg = cχ R. The diﬀerential operator 1 + L takes a radial
function u(|t|) to
u′′(|t|)
4π 2 + n − 1
4π 2|t| u′(|t|) + u(|t|).
702 HENRY COHN AND NOAM ELKIES
It follows from this and the diﬀerential equation satisﬁed b y the Bessel func-
tions that
Jα (2π |t|)/ |t|α
is in the kernel of 1 + L, if α = n/ 2 − 1. From that, one can check that
g(t) =
(
− Rα
Jα (2πR )
Jα (2π |t|)
|t|α + 1
)
χ R(t).
One can check that the minimum of Jα (2π |t|)/ |t|α occurs at
|t| = jn/ 2/ (2π ) = R,
so g is nonnegative everywhere, as desired, since Jα (2πR ) = Jα (jn/ 2) < 0 (the
roots of the functions Jα and Jα +1 = Jn/ 2 are interlaced).
Thus, we have constructed a function f satisfying the hypotheses of The-
orem 3.1. It has f (0) = 1 and
ˆf (0) =
∫
Rn
g(g + Lg) = c
∫
Rn
g = c = (n/ 2)!
π n/ 2Rn .
Because R = jn/ 2/ (2π ), this function proves Levenshtein’s sphere packing
bound:
Proposition 6.1. The function
f (x) = Jn/ 2(jn/ 2|x|)2
(1 − |x|2)|x|n
satisﬁes the hypotheses of Theorem 3.1, and leads to the upper bound
jn
n/ 2
(n/ 2)!24n
for the densities of n-dimensional sphere packings.
This function does not optimize the bound in Theorem 3.1, but it does
optimize it within the class of functions whose Fourier tran sforms have sup-
port in the ball of radius jn/ 2/π about the origin. This was ﬁrst proved by
Gorbachev [Go]. For another proof, see [C].
It is not a coincidence that this proves exactly the same boun d as in
Levenshtein’s paper [Lev]. Levenshtein studies spherical codes with minimal
angular separation θ , and derives his sphere packing bound from letting θ → 0.
Under that limit, the functions he uses in the linear program ming bounds for
spherical codes become our Bessel function example. This ca n be proved using
the limit
(6.1) lim
j→∞
j−α P (α,β )
j
(
cos z
j
)
= (z/ 2)−α Jα (z),
which is 10.8 (41) in [EMOT].
NEW UPPER BOUNDS ON SPHERE PACKINGS I 703
The functions we have obtained are not optimal in any dimensi on above 1.
There are two reasons for this. First, we restricted our atte ntion to functions
such that ˆf has compact support, and as we have seen in Section 5, that can not
be true if we are to get sharp bounds. Second, and more importa ntly, we
implicitly considered only functions such that ˆf is positive within its support.
The problem is that if ˆf vanishes somewhere, then the perturbations h must
be chosen so as not to push ˆf below zero. We made no attempt to do so, and
therefore could not ﬁnd any stationary points for which ˆf has zeros within its
support. We have seen in Section 5 that zeros are essential fo r sharp bounds.
Unfortunately, it seems diﬃcult to adapt the stationary poi nt argument
to deal with these diﬃculties. One approach is to assume that ˆf has zeros at
certain locations, and look at only the perturbations h that, up to ﬁrst order,
do not push ˆf below zero. Although we can set up such problems, we have not
been able to solve them.
7. Numerical results
It is possible to get numerical results by using linear progr amming to
ﬁnd functions for use in Theorem 3.1, as was done for the kissi ng problem by
Odlyzko and Sloane in [OS]. The idea is to ﬁx one of f (0) and ˆf (0), and view
extremizing the other as an inﬁnite-dimensional linear pro gramming problem.
One can try to approximate it with a ﬁnite-dimensional probl em, and solve it
on a computer. Although we obtained some numerical results t his way, it was
cumbersome and generally ineﬀective. Instead, we use the fo llowing approach.
First, consider trying to use our techniques to bound the den sity of an
isodual lattice. There is no reason for optimal sphere packi ngs to be isodual
lattices, and for example in three dimensions they are known not to be, but it
is convenient to use this case as a stepping stone.
Proposition 7.1. Suppose g : Rn → R is a radial , admissible function ,
is not identically zero , and satisﬁes the following three properties :
(1) g(0) = 0,
(2) g(x) ≥ 0 for |x| ≥ r, and
(3) ˆg = −g.
Then every isodual lattice in dimension n must contain a nonzero vector of
length at most r.
Proof of special case. For simplicity, we deal only with the case in which
g(x) > 0 for |x| ≫ 0. Let Λ ∼= Λ ∗ be an isodual lattice. By Poisson summation,
∑
x∈Λ
g(x) =
∑
x∈Λ ∗
ˆg(x) = −
∑
x∈Λ
g(x),
704 HENRY COHN AND NOAM ELKIES
so ∑
x∈Λ
g(x) = 0 .
In order for the sum not to be positive, the lattice Λ must cont ain some nonzero
vector of length at most r.
We can actually remove the hypothesis that g(x) > 0 for |x| ≫ 0 from the
proof of Proposition 7.1, by using a scaling trick, as in the p roof of Theorem 3.2.
However, we omit the details, because the hypothesis holds i n all our numerical
examples.
Notice that given any function f that proves a bound in Theorem 3.2,
we can produce a g that proves the same bound in Proposition 7.1, by taking
g = ˆf − f . Thus, the bound we get for isodual lattices is at least as goo d
as that for general sphere packings. In principle, it could b e better, but in
practice we ﬁnd that it is not (as we explain below).
We can ﬁnd excellent functions for use in Proposition 7.1 as f ollows. Let
Lα
k (x) be the Laguerre polynomials orthogonal with respect to the measure
e−xxα dx on [0 , ∞). Set α = n/ 2 − 1, and deﬁne
gk(x) = Lα
k (2π |x|2)e−π |x|2
for k ≥ 0; we suppress the dependence on n in our notation. These func-
tions form a basis for the radial eigenfunctions of the Fouri er transform, with
eigenvalues (−1)k (see Section 4.23 and equation (4.20.3) of [Leb]).
To ﬁnd a function g for use in Proposition 7.1, we consider a linear com-
bination of g1, g 3, . . . , g 4m+3, and require it to have a root at 0 and m double
roots at z1, . . . , z m. (Counting degrees of freedom suggests that there should
be a unique such function, up to scaling.) We then choose the l ocations of
z1, . . . , z m to minimize the value r of the last sign change of g. To make this
choice, we do a computer search. Speciﬁcally, we make an init ial guess for
the locations of z1, . . . , z m, and then see whether we can perturb them to de-
crease r. We repeat the perturbations until reaching a local optimum . Strictly
speaking, we cannot prove that it ever converges, or comes an ywhere near the
global optimum. However, it works well in practice. At any ra te this cannot
aﬀect the validity of our bounds, only their optimality give n m. As we increase
m, this method should give better and better bounds, which sho uld converge
to the best bounds obtainable using Proposition 7.1.
This method gives good functions for use in Proposition 7.1, but naturally
bounds on all sphere packings would be better than bounds onl y on isodual
lattices. We can turn these functions into functions satisf ying the hypotheses
of Theorem 3.2, without changing r, as follows.
Let h be a linear combination of g0, g 2, . . . , g 4m+2 with double zeros at
z1, . . . , z m, such that g + h has a double zero at r. Then in the examples we
have computed, g + h has constant sign, which we can take to be positive. We
NEW UPPER BOUNDS ON SPHERE PACKINGS I 705
end up with a function f = −g + h that is nonpositive outside radius r, and
whose Fourier transform ˆf = g + h is nonnegative everywhere; furthermore,
f (0) = ˆf (0). Thus, we can apply Theorem 3.2 to get the same bound for
general sphere packings that g proves for isodual lattices. Notice that it is not
clear a priori that f must satisfy all the hypotheses of Theorem 3.2, but it
happens in all of our numerical examples.
Figure 1 (from §1) and Table 3 (from Appendix C) illustrate the bounds
this method produces, using m = 6 as the number of forced double zeros
(except in dimension 7 and lower, where m = 5 suﬃces for the accuracy we
desire). We also list for comparison Rogers’ bound [Ro], whi ch was previously
the best bound known in dimensions 4 through 36. The choices o f forced double
roots are described in Table 4 (from Appendix C).
These bounds were calculated using a computer. However, the mathe-
matics behind the calculations is rigorous. In particular, we use exact rational
arithmetic, and apply Sturm’s theorem to count real roots an d make sure we
do not miss any sign changes. More precisely, we take the quan tities 2 πz 2
i
to be rational numbers. That is convenient, because the func tions gk(x) are
polynomials in 2 π |x|2 with rational coeﬃcients (times Gaussians, which have
no sign changes). The one subtlety is that in constructing h, we want g + h to
have a double root at r, and 2 πr 2 is generally not rational. Instead of doing
this computation using ﬂoating point arithmetic, we replac e 2 πr 2 by a nearby
rational number and then determine h exactly, using that value of r. To do so,
we must increase r slightly, but of course we can make the increase as small as
we wish.
In dimensions 8 and 24, we carried out the calculations for m = 11. The
resulting upper bounds are within factors of 1 . 000001 and 1. 0007071 of equality,
respectively. More precisely, in dimension 8 we take
2πr 2 = 12. 56637375,
and in dimension 24 we take
2πr 2 = 25. 1342216.
The forced double roots we used to achieve these bounds are gi ven in Tables 1
and 2.
i 1 2 3 4 5 6
2πz 2
i 25. 1328 37 . 6995 50 . 2678 62 . 8463 75 . 4579 88 . 2463
i 7 8 9 10 11
2πz 2
i 101. 3618 115 . 6443 131 . 0298 150 . 0861 174 . 2876
Table 1. Forced double roots for m = 11, n = 8.
706 HENRY COHN AND NOAM ELKIES
i 1 2 3 4 5 6
2πz 2
i 37. 705 50 . 285 62 . 893 75 . 578 88 . 454 101 . 737
i 7 8 9 10 11
2πz 2
i 115. 776 131 . 035 148 . 162 168 . 215 193 . 766
Table 2. Forced double roots for m = 11, n = 24.
Our numerical results lead us to the following conjectures.
Conjecture 7.2. The smallest possible value of r in Proposition 7.1
equals that in Theorem 3.2, and for each optimal g from Proposition 7.1, there
exists an optimal f from Theorem 3.2 such that g = ˆf − f .
Conjecture 7.3. There exist functions that satisfy the hypotheses of
Theorem 3.2 and solve the sphere packing problem in dimensions 2, 8, and 24.
Conjecture 7.4. The numerical method described above gives bounds
that converge (as m → ∞) to the optimal bounds obtainable using Theorem 3.2.
8. Uniqueness
It is natural to ask whether the densest sphere packing in Rn is unique.
Of course, it is trivially not unique, since for example remo ving a single sphere
does not change the global density. However, it is conjectur ed that E8 and the
Leech lattice are unique among periodic packings. By contra st, in R3 there are
inﬁnitely many distinct periodic packings of maximal densi ty. Our techniques
can be used to prove this uniqueness in 8 and 24 dimensions, gi ven the following
slight strengthening of Conjecture 7.3. At the same time, we will deal with the
hexagonal lattice, although uniqueness in that case has lon g been known.
Let Λ 2, Λ 8, and Λ 24 denote the isodual scaling of the hexagonal lattice,
the E8 root lattice, and the Leech lattice, respectively.
Conjecture 8.1. For n ∈ {2, 8, 24}, there exists a function that satisﬁes
the hypotheses of Theorem 3.2 to prove that Λ n is the densest packing in Rn.
Furthermore, this function and its Fourier transform have roots only at th e
vector lengths in Λ n.
First, let n be 8 or 24, so that Λ n is an even unimodular lattice (we will
discuss the n = 2 case below). Let f be a function satisfying the conclusions
of Conjecture 8.1. Suppose we have a maximally dense packing given by the
translates of a lattice Λ by vectors v1, . . . , v N , whose diﬀerences are not in Λ.
NEW UPPER BOUNDS ON SPHERE PACKINGS I 707
Without loss of generality, we can assume that |Λ | = N and v1 = 0. Note that
|Λ | = N implies that the packing uses balls of the same radius as thos e in Λ n.
By Poisson summation,
∑
1≤j,k ≤N
∑
x∈Λ
f (x + vj − vk) = 1
|Λ |
∑
t∈Λ ∗
ˆf (t)
⏐⏐⏐⏐⏐⏐
∑
1≤j≤N
e2πi ⟨vj ,t ⟩
⏐⏐⏐⏐⏐⏐
2
,
and the f (0) terms cancel the ˆf (0) term, so we can draw the usual conclusions
from the inequalities on each side. In particular, each vect or x + vj − vk must
occur at a root of f . Now we can apply the following lemma:
Lemma 8.2. Suppose S is a subset of Rn such that 0 ∈ S, there are n
linearly independent vectors in S, and for all x, y ∈ S, the distance |x − y| is
the square root of an even integer. Then the subgroup of Rn generated by S is
an even integral lattice.
Recall that an integral lattice is a lattice in which the inner product of
each pair of vectors is an integer; it is even if every vector has even norm.
Proof. For all x, y ∈ S, their inner product ⟨x, y ⟩is an integer, because
⟨x, y ⟩= (|x − 0|2 + |y − 0|2 − |x − y|2)/ 2 ∈ Z,
and the norm |x|2 of any element x ∈ S is an even integer. It follows that
the same facts hold for integer linear combinations of eleme nts of S. The
restriction on norms implies that S generates a discrete subgroup of Rn, and
hence a lattice (because S spans Rn by assumption). Now the conditions above
on inner products and norms amount to the deﬁnition of an even integral
lattice.
Let L be the subgroup of Rn generated by our periodic packing. By
Lemma 8.2, it is an even integral lattice. In any integral lat tice, the covolume
is always the square root of an integer, since its square is th e determinant of
a Gram matrix, which is an integral matrix. Thus, L has at most one point
per unit volume in Rn, with equality if and only if L is unimodular. However,
the periodic packing has one sphere per unit volume in Rn, because |Λ | = N .
It follows that the periodic packing is in fact the lattice pa cking determined
by L: if any spheres from the lattice packing were missing from th e periodic
packing, then by periodicity the numbers of spheres per unit volume would be
strictly smaller. Thus, our packing comes from an even unimo dular lattice,
and that lattice must have minimal norm 2 in R8 and 4 in R24 for the density
to be right. Such lattices are unique (see Chapters 16 and 18 o f [CS]). Thus,
we have shown that Conjecture 8.1 implies that E8 and the Leech lattice are
the only periodic packings of maximal density in R8 and R24, respectively.
708 HENRY COHN AND NOAM ELKIES
For R2, this argument requires a slight modiﬁcation, because the i sodual
scaling of the hexagonal lattice is not an even unimodular la ttice. However, the
modiﬁcation is not hard. As above, in any maximally dense per iodic packing,
the distances between points must occur among the distances in the hexagonal
lattice. Of course, we can choose any scaling we prefer; the m ost convenient is
that of the A2 root lattice, given by
A2 = {(x0, x 1, x 2) ∈ Z3 : x0 + x1 + x2 = 0},
because A2 is an even integral lattice. As above, our periodic packing m ust
then be contained in an even integral lattice L. However, the unimodularity
argument no longer applies. Fortunately, we do not need it: b ecause L is even,
its minimal norm is at least 2, so L determines a sphere packing with spheres
of the same radius as in our periodic packing. This sphere pac king contains the
original periodic packing. If the periodic packing did not u se all these spheres,
then its density would be lower than that of L. Thus, it is a lattice packing,
and it is well known and easy to prove that A2 is the unique densest lattice in
two dimensions.
It is worth noting that the arguments above do not require the full strength
of Conjecture 8.1. In particular, we never make use of restri ctions on the
roots of the Fourier transform. Furthermore, in the n = 2 case, we do not
even require as strong a condition on the function’s roots: A2 does not have
vectors of every even norm, but our argument allows the funct ion to have roots
corresponding to the missing norms.
Appendix A. T echnicalities about density
In this appendix, we provide precise statements and referen ces for what it
means for a packing to have a density and whether there is a max imally dense
packing. Much of our discussion closely follows Section I of [K].
Let P be any sphere packing in Rn. We say that P has density ∆ if for
all p ∈ Rn, we have
∆ = limr→∞
vol(B(p, r ) ∩ P)
vol B(p, r ) ,
where B(p, r ) is the ball of radius r centered at p, and B(p, r ) ∩ P consists of
those parts of the balls in P that lie within B(p, r ). It is proved in [Gr] that
if this limit exists for one p, then it exists for all p and is equal for all p. We
say that the packing has uniform density if the limit exists u niformly for all p.
In that case, [Gr] shows that for every compact set R that is the closure of its
interior and every point p,
∆ = limr→∞
vol((rR + p) ∩ P)
vol rR ,
where of course rR + p denotes R scaled by a factor of r and translated by p.
NEW UPPER BOUNDS ON SPHERE PACKINGS I 709
Although not every packing has a density, every packing has a n upper
density, deﬁned by
∆ = lim sup
r→∞
sup
p∈Rn
vol(B(p, r ) ∩ P)
vol B(p, r ) .
It is proved in [Gr] that the supremum of all upper densities i s achieved by a
uniformly dense packing.
Periodic packings are the most convenient ones for our purpo ses. Using the
above results, it is easy to see that they come arbitrarily cl ose to the greatest
possible density, as follows. Suppose ∆ is the maximum packi ng density in Rn,
and let P be a uniformly dense packing of density ∆. Let R be the fundamental
parallelotope of any lattice Λ ⊂ Rn. We know that
∆ = limr→∞
vol(rR ∩ P)
vol rR .
Let ε > 0. If we choose r large enough, then the total volume of the spheres
in P that lie entirely within rR is within ε vol rR of ∆ vol rR, because only
a negligible fraction of the spheres can intersect the sides of rR. Deﬁne a
periodic packing P ′ by taking all the spheres of P that lie entirely within rR,
and also including all translations of them by rΛ. Then this periodic packing
has density at least ∆ − ε .
Appendix B. Other convex bodies
Our methods are not limited to studying sphere packings, but instead
apply to packings with translates of any convex, symmetrica l body. In fact, it
is straightforward to prove the following generalization o f our main theorem:
Theorem B. 1. Let C be a convex body in Rn, symmetric with respect to
the origin. Suppose f : Rn → R is an admissible function , is not identically
zero, and satisﬁes the following two conditions :
(1) f (x) ≤ 0 for x ⁄∈C, and
(2) ˆf (t) ≥ 0 for all t.
Then all packings with translates of C have density bounded above by
vol(C)f (0)
2nˆf (0)
.
Unfortunately, when C is not a sphere, there does not seem to be a good
analogue of the reduction to radial functions in Theorem 3.1 . That makes these
cases somewhat less convenient to deal with. There always ex ist functions that
710 HENRY COHN AND NOAM ELKIES
prove the trivial density bound of 1: let χ C/ 2 be the characteristic function of
the scaled body C/ 2, and let f = χ C/ 2 ∗ χ C/ 2.
Appendix C. Numerical data
Table 3 compares the best packings known, the previous best u pper bound
known, and our bound. The packings and previous bounds are fr om [CS] (see
in particular Tables I.1(a) and I.1(b) on pages xix and xx). T able 4 lists the
choices of forced double roots that lead to our new bounds.
Acknowledgements. We thank Richard Askey, Tom Brennan, Harold Di-
amond, Pavel Etingof, George Gasper, David Jerison, Greg Ku perberg, Ben
Logan, L´ aszl´ o Lov´ asz, Steve Miller, Amin Shokrollahi, N eil Sloane, Jeﬀrey
Vaaler, David Vogan, and Michael Weinstein for helpful disc ussions.
NEW UPPER BOUNDS ON SPHERE PACKINGS I 711
Dimension Best Packing Known Rogers’ Bound New Upper Bound
1 0.5 0.5 0.5
2 0.28868 0.28868 0.28868
3 0.17678 0.1847 0.18616
4 0.125 0.13127 0.13126
5 0.08839 0.09987 0.09975
6 0.07217 0.08112 0.08084
7 0.0625 0.06981 0.06933
8 0.0625 0.06326 0.06251
9 0.04419 0.06007 0.05900
10 0.03906 0.05953 0.05804
11 0.03516 0.06136 0.05932
12 0.03704 0.06559 0.06279
13 0.03516 0.07253 0.06870
14 0.03608 0.08278 0.07750
15 0.04419 0.09735 0.08999
16 0.0625 0.11774 0.10738
17 0.0625 0.14624 0.13150
18 0.07508 0.18629 0.16503
19 0.08839 0.24308 0.21202
20 0.13154 0.32454 0.27855
21 0.17678 0.44289 0.37389
22 0.33254 0.61722 0.51231
23 0.5 0.87767 0.71601
24 1.0 1.27241 1.01998
25 0.70711 1.8798 1.48001
26 0.57735 2.8268 2.18614
27 0.70711 4.3252 3.28537
28 1.0 6.7295 5.02059
29 0.70711 10.642 7.79782
30 1.0 17.094 12.30390
31 1.2095 27.880 19.71397
32 2.5658 46.147 32.06222
33 2.2220 77.487 52.90924
34 2.2220 131.94 88.55925
35 2.8284 227.71 150.29783
36 4.4394 398.25 258.54994
Table 3. Lower and upper bounds on center density, using m = 6.
712 HENRY COHN AND NOAM ELKIES
Dimension 2πr 2 2πz 2
1 2πz 2
2 2πz 2
3 2πz 2
4 2πz 2
5 2πz 2
6
2 7.25520 21.77 29.02 50.79 65.34 90.19
3 8.19385 22.00 31.63 49.10 61.80 80.01
4 9.10543 22.46 33.49 48.69 62.03 79.73
5 9.99512 23.04 34.87 48.90 63.04 80.44
6 10.86682 23.70 35.98 49.43 64.07 81.61
7 11.72351 24.41 36.94 50.13 65.04 82.94
8 12.56674 25.14 37.74 50.50 64.08 79.03 99.37
9 13.39945 25.89 38.57 51.30 64.99 80.13 100.44
10 14.22261 26.66 39.38 52.13 65.89 81.24 101.56
11 15.03741 27.44 40.18 52.97 66.79 82.34 102.71
12 15.84481 28.23 40.98 53.82 67.69 83.44 103.89
13 16.64565 29.02 41.77 54.67 68.61 84.51 105.08
14 17.44063 29.82 42.57 55.53 69.53 85.58 106.28
15 18.23036 30.61 43.37 56.39 70.46 86.65 107.48
16 19.01538 31.42 44.18 57.25 71.39 87.71 108.68
17 19.79617 32.22 44.99 58.12 72.34 88.77 109.88
18 20.57315 33.02 45.80 58.99 73.29 89.84 111.08
19 21.34670 33.82 46.62 59.86 74.24 90.90 112.28
20 22.11717 34.63 47.45 60.74 75.20 91.97 113.48
21 22.88488 35.44 48.27 61.63 76.17 93.04 114.68
22 23.65012 36.24 49.10 62.51 77.14 94.12 115.88
23 24.41314 37.05 49.94 63.41 78.12 95.20 117.08
24 25.17419 37.86 50.78 64.30 79.09 96.28 118.29
25 25.93349 38.66 51.62 65.20 80.08 97.37 119.50
26 26.69125 39.47 52.46 66.11 81.07 98.46 120.71
27 27.44766 40.28 53.31 67.02 82.06 99.55 121.92
28 28.20290 41.09 54.17 67.93 83.06 100.64 123.13
29 28.95711 41.90 55.02 68.85 84.06 101.74 124.34
30 29.71046 42.72 55.88 69.77 85.06 102.84 125.56
31 30.46307 43.53 56.74 70.69 86.07 103.94 126.77
32 31.21508 44.34 57.61 71.62 87.08 105.05 127.99
33 31.96659 45.16 58.47 72.56 88.09 106.16 129.21
34 32.71772 45.97 59.34 73.49 89.10 107.27 130.43
35 33.46857 46.79 60.21 74.43 90.12 108.38 131.65
36 34.21922 47.60 61.09 75.37 91.14 109.49 132.88
Table 4. Values of 2 πr 2 and 2 πz 2
i for 1 ≤ i ≤ 6.
NEW UPPER BOUNDS ON SPHERE PACKINGS I 713
Microsoft Research, One Microsoft W ay, Redmond, W A
E-mail address : cohn@microsoft.com
Harvard University, Cambridge, MA
E-mail address : elkies@math.harvard.edu
References
[AAR] G. Andrews, R. Askey , and R. Roy , Special Functions , Cambridge University
Press, Cambridge, 1999.
[C] H. Cohn , New upper bounds on sphere packings II, Geom. Topol. 6 (2002), 329–
353, arXiv:math.MG/0110010.
[CS] J. H. Conw ay and N. J. A. Sloane , Sphere Packings, Lattices and Groups , third
edition, Springer-Verlag, New York, 1999.
[D] P. Delsarte, Bounds for unrestricted codes, by linear programming, Philips Res.
Rep. 27 (1972), 272–289.
[DM] H. Dym and H. P. McKean , Fourier Series and Integrals , Academic Press, New
York, 1972.
[EMOT] A. Erd ´elyi, W. Magnus, F. Oberhettinger , and F. G. Tricomi , Higher Tran-
scendental Functions, Vol. II , based, in part, on notes left by Harry Bateman,
McGraw-Hill, New York, 1953.
[Go] D. V. Gorbachev , Extremal problem for entire functions of exponential sphe rical
type, connected with the Levenshtein bound on the sphere pac king density in
Rn (Russian), Izvestiya of the Tula State University Ser. Mathematics Mec hanics
Informatics 6 (2000), 71–78.
[Gr] H. Groemer , Existenzs¨ atze f¨ ur Lagerungen im Euklidischen Raum, Math. Z . 81
(1963), 260–278.
[Ha] T. Hales , The Kepler conjecture, 1998, arXiv:math.MG/9811078.
[Hs] W.-Y. Hsiang , The optimal density of sphere packings in dimension 8 and th e
uniqueness theorem on ﬁnal packings with optimal density, B erkeley Mathematics
Department Colloquium, March 15, 2001.
[KL] G. A. Kabatiansky and V. I. Levenshtein , Bounds for packings on a sphere and
in space, Problems of Information Transmission 14 (1978), 1–17.
[K] G. Kuperberg , Notions of denseness, Geom. Topol . 4 (2000) 277–292, arXiv:
math.MG/9908003.
[Leb] N. N. Lebedev , Special Functions and Their Applications , Dover Publications,
Inc., New York, 1972.
[Lev] V. I. Levenshtein , Bounds for packings in n-dimensional Euclidean space, Soviet
Math. Dokl . 20 (1979), 417–421.
[Lo] B. F. Logan , Extremal problems for positive-deﬁnite bandlimited func tions II:
eventually negative functions, SIAM J. Math. Anal . 14 2 (1983), 253–257.
[MRR W] R. J. McEliece, E. R. Rodemich, H. C. Rumsey, Jr., and L. R. Welch , New upper
bounds on the rate of a code via the Delsarte-MacWilliams ine qualities, IEEE
Trans. Information Theory 23 (1977), 157–166.
[OS] A. M. Odlyzko and N. J. A. Sloane , New bounds on the number of unit spheres
that can touch a unit sphere in n dimensions, J. Combin. Theory A 26 (1979),
210–214.
[Ro] C. A. Rogers , The packing of equal spheres, Proc. London Math. Soc . 8 (1958),
609–620.
[Ru] W. Rudin , Real and Complex Analysis , third edition, McGraw-Hill, New York,
1987.
[S] C. L. Siegel , ¨Uber Gitterpunkte in convexen K¨ orpern and ein damit zusam-
menh¨ angendes Extremalproblem,Acta Math . 65 (1935), 307–323.
714 HENRY COHN AND NOAM ELKIES
[SW] E. M. Stein and G. L. Weiss , Introduction to Fourier Analysis on Euclidean Spaces,
Princeton Math. Series 32, Princeton Univ. Press, Princeton, NJ, 1971.
[Y] V. A. Yudin , The Laplace operator and packings of balls in a Euclidean sp ace,
Diﬀerential Equations 31 (1995), 837–840.
(Received October 2, 2001)
