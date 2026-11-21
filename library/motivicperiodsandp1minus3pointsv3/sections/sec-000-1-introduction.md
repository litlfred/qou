---
doc_id: motivicperiodsandp1minus3pointsv3
doc_title: "Motivic periods and P^1 minus 3 points"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-14
source_pdf: MotivicPeriodsandP1minus3pointsv3.pdf
source_sha256: 7870572b8cc316d0
toc_source: inferred
doc_brief: "Motivic periods and P^1 minus 3 points — This is a review of the theory of the motivic fundamental group of the projective line minus three points, and its relation to multiple zeta values."
---
The role of the projective line minus three points X = P1\{0, 1, ∞} in relation to
Galois theory can be traced back to Belyi’s theorem [4] (1979):
Theorem 1.1. Every smooth projective algebraic curve deﬁned over Q can be
realised as a ramiﬁed cover of P1, whose ramiﬁcation locus is contained in {0, 1, ∞}.
Belyi deduced that the absolute Galois group of Q acts faithfully on the proﬁnite
completion of the fundamental group of X, i.e., the map
Gal(Q/Q) →Aut(bπ1(X(C), b))
(1.1)
where b ∈X(Q), is injective. In his famous proposal ‘Esquisse d’un programme’
in 1984 [21], Grothendieck suggested studying the absolute Galois group of Q via
its action on completions of fundamental groups of moduli spaces of curves Mg,n
of genus g with n ordered marked points (X being isomorphic to M0,4) and their
interrelations.
A few years later, at approximately the same time, these ideas
were developed in somewhat diﬀerent directions in three enormously inﬂuential
papers due to Drinfeld, Ihara, and Deligne [15, 26, 10]. Ihara’s 1990 ICM talk
gives a detailed account of the subject at that time [27]. However, the problem of
determining the image of the map (1.1) remains completely open to this day.
In this talk I will mainly consider the pro-unipotent completion of the funda-
mental group of X, which seems to be a more tractable object than its proﬁnite
version, and closely follow the point of view of Deligne, and Ihara (see [27], §5).
1.1. Unipotent completion. Deligne showed [10] that the pro-unipotent
completion of π1(X) carries many extra structures corresponding to the realisations
of an (at the time) hypothetical category of mixed Tate motives over the integers.
∗Beneﬁciary of ERC Grant 257638
2
Francis Brown
Since then, the motivic framework has now been completely established due to
the work of a large number of diﬀerent authors including Beilinson, Bloch, Borel,
Levine, Hanamura, and Voevodsky. The deﬁnitive reference is [14], §§1-2.
1. There exists an abstract Tannakian category MT (Z) of mixed Tate motives
unramiﬁed over Z. It is a Q-linear subcategory of the category MT (Q) of
mixed Tate motives over Q obtained by restricting certain Ext groups. It is
equivalent to the category of representations of an aﬃne group scheme GdR
which is deﬁned over Q and is a semi-direct product
GdR ∼= U dR ⋊Gm .
The subgroup U dR is pro-unipotent, and its graded Lie algebra (for the action
of Gm) is isomorphic to the free graded Lie algebra with one generator
σ3, σ5, σ7, . . .
in every odd negative degree ≤−3. The essential reason for this is that the
algebraic K-theory of the integers K2n−1(Z) has rank 1 for n = 3, 5, 7, . . .,
and rank 0 otherwise, as shown by Borel [2, 3]. Note that the elements σ2n+1
are only well-deﬁned modulo commutators.
2. The pro-unipotent completion πun
1 (X,
→
10, −
→
11) is the Betti realisation of an
object, called the motivic fundamental groupoid (denoted by πmot
1
), whose
aﬃne ring is a limit of objects in the category MT (Z).
The majority of these notes will go into explaining 2 and some of the ideas
behind the following motivic analogue of Belyi’s injectivity theorem (1.1):
Theorem 1.2. GdR acts faithfully on the de Rham realisation of πmot
1
(X,
→
10, −
→
11).
This theorem has an ℓ-adic version which can be translated into classical Galois
theory ([27], §5.2), and relates to some questions in the literature cited above.
Unlike Belyi’s theorem, which is geometric, the proof of theorem 1.2 is arithmetic
and combinatorial. The main ideas came from the theory of multiple zeta values.
1.2. Multiple zeta values. Let n1, . . . , nr be integers ≥1 such that nr ≥2.
Multiple zeta values are deﬁned by the convergent nested sums
ζ(n1, . . . , nr) =
X
1≤k1<...<kr
1
kn1
1 . . . knr
r
∈R .
The quantity N = n1 + . . . + nr is known as the weight, and r the depth. Multiple
zeta values were ﬁrst studied by Euler (at least in the case r = 2) and were redis-
covered independently in mathematics by Zagier and Ecalle, and in perturbative
quantum ﬁeld theory by Broadhurst and Kreimer. They satisfy a vast array of
algebraic relations which are not completely understood at the time of writing.
Motivic periods and P1\{0, 1, ∞}
3
The relationship between these numbers and the fundamental group comes via
the theory of iterated integrals, which are implicit in the work of Picard and were
rediscovered by Chen and Dyson. In general, let M be a diﬀerentiable manifold and
let ω1, . . . , ωn be smooth 1-forms on M. Consider a smooth path γ : (0, 1) →M.
The iterated integral of ω1, . . . , ωn along γ is deﬁned (when it converges) by
Z
γ
ω1 . . . ωn =
Z
0<t1<...<tn<1
γ∗(ω1)(t1) . . . γ∗(ωn)(tn) .
Kontsevich observed that when M = X(C) and γ(t) = t is simply the inclusion
(0, 1) ⊂X(R), one has the following integral representation
ζ(n1, . . . , nr) =
Z
γ
ω1 ω0 . . . ω0
|
{z
}
n1−1
ω1 ω0 . . . ω0
|
{z
}
n2−1
. . . ω1 ω0 . . . ω0
|
{z
}
nr−1
(1.2)
where ω0 = dt
t and ω1 =
dt
1−t. I will explain in §2.1 that this formula allows one to
interpret multiple zeta values as periods of the pro-unipotent fundamental groupoid
of X. The action of the motivic Galois group GdR on the (de Rham version of)
the latter should translate, via Grothendieck’s period conjecture, into an action
on multiple zeta values themselves. Thus one expects multiple zeta values to be a
basic example in a Galois theory of transcendental numbers ([1], §23.5); the action
of the Galois group should preserve all their algebraic relations.
Of course, Grothendieck’s period conjecture is not currently known, so there
is no well-deﬁned group action on multiple zeta values. This can be circumvented
using motivic multiple zeta values. The action of GdR on the de Rham fundamental
group of X can then be studied via its action on these objects.
1.3. Motivic periods. Let T be a neutral Tannakian category over Q with
two ﬁber functors ωB, ωdR : T →VecQ. Deﬁne the ring of motivic periods to be
the aﬃne ring of functions on the scheme of tensor isomorphisms from ωdR to ωB
Pm
T = O(IsomT (ωdR, ωB)) .
Every motivic period can be constructed from an object M ∈T , and a pair of
elements w ∈ωdR(M), σ ∈ωB(M)∨. Its matrix coeﬃcient is the function
φ 7→⟨φ(w), σ⟩
:
IsomT (ωdR, ωB) →A1
Q
where A1
Q is the aﬃne line over Q, and deﬁnes an element denoted [M, w, σ]m ∈Pm
T .
It is straightforward to write down linear relations between these symbols as well
as a formula for the product of two such symbols. If, furthermore, there is an
element compB,dR ∈IsomT (ωdR, ωB)(C) we can pair with it to get a map
per : Pm
T −→C
(1.3)
called the period homomorphism. The ring Pm
T admits a left action of the group
GdR = IsomT (ωdR, ωdR), or equivalently, a left coaction
Pm
T −→O(GdR) ⊗Q Pm
T .
(1.4)
4
Francis Brown
Example 1.3. Let T be any category of mixed Tate motives over a number ﬁeld.
It contains the Lefschetz motive L = Q(−1), which is the motive H1(P1\{0, ∞}).
Its de Rham cohomology is the Q-vector space spanned by the class [ dz
z ] and its
Betti homology is spanned by a small positive loop γ0 around 0. The Lefschetz
motivic period is
Lm = [L, [ dz
z ], [γ0]]
∈
Pm
T .
Its period is per(Lm) = 2πi. It transforms, under the rational points of the de
Rham Galois group of T , by Lm 7→λLm, for any λ ∈Q×.
This construction can be applied to any pair of ﬁber functors to obtain diﬀerent
notions of motivic periods.
Indeed, the elements of O(GdR) can be viewed as
‘de Rham’ motivic periods, or matrix coeﬃcients of the form [M, w, v]dR, where
w ∈ωdR(M) and v ∈ωdR(M)∨(called framings). Whenever the ﬁber functors
carry extra structures (such as ‘complex conjugation’ on ωB or a ‘weight’ grading
on ωdR), then the ring of motivic periods inherits similar structures.
1.3.1. Motivic MZV’s. Let T = MT (Z). The Betti and de Rham realisations
provide functors ωB, ωdR, and integration deﬁnes a canonical element compB,dR ∈
IsomT (ωdR, ωB)(C). Since the de Rham functor ωdR is graded by the weight, the
ring of motivic periods Pm
MT (Z) is also graded.1 It contains graded subrings
Pm,+
MT (Z),R ⊂Pm,+
MT (Z) ⊂Pm
MT (Z)
of geometric periods (periods of motives whose weights are ≥0), denoted by a
superscript +, and those which are also invariant under complex conjugation (de-
noted by a subscript R, since their periods lie in R as opposed to C).
Next, one has to show that the integral (1.2) deﬁnes a period of an object M
in MT (Z) (this can be done in several ways: [19], [36], [14])).
This deﬁnes a
matrix coeﬃcient [M, w, σ]m, where w encodes the integrand, and σ the domain of
integration, which we call a motivic multiple zeta value (§2.2)
ζm(n1, . . . , nr) ∈Pm
MT (Z) .
Its weight is n1 + . . . + nr and its period is (1.2). Most (but not all) of the known
algebraic relations between multiple zeta values are also known to hold for their
motivic versions. Motivic multiple zeta values generate a graded subalgebra
H
⊂
Pm,+
MT (Z),R .
(1.5)
The description §1.1, (1) of U dR enables one to compute the dimensions of the
motivic periods of MT (Z) in each degree by a simple counting argument:
if
dN := dimQ
 Pm,+
MT (Z),R

N
then
X
N≥0
dNtN =
1
1 −t2 −t3 .
(1.6)
This implies a theorem proved independently by Goncharov and Terasoma [14],[36].
1In the ﬁeld of multiple zeta values, the ‘weight’ refers to one half of the Hodge-theoretic
weight, so that Lm has degree 1 instead of 2. I shall adopt this terminology from here on.
Motivic periods and P1\{0, 1, ∞}
5
Theorem 1.4. The Q-vector space spanned by multiple zeta values of weight N
has dimension at most dN, where the integers dN are deﬁned in (1.6).
So far, this does not use the action of the motivic Galois group, only a bound
on the size of the motivic periods of MT (Z). The role of P1\{0, 1, ∞} is that the
automorphism group of its fundamental groupoid yields a formula for the coaction
(1.4) on the motivic multiple zeta values (§2.5).
The main theorem uses this
coaction in an essential way, and is inspired by a conjecture of M. Hoﬀman [25].
Theorem 1.5. The following set of motivic MZV’s are linearly independent:
{ζm(n1, . . . , nr)
for
ni = {2, 3}} .
(1.7)
From the enumeration (1.6) of the dimensions, we deduce that H = Pm,+
MT (Z),R,
and that (1.7) is a basis for H. From this, one immediately sees that U dR acts
faithfully on H, and theorem 1.2 follows easily. As a bonus we obtain that U dR
has canonical generators σ2n+1 (deﬁned in §3.1), and, furthermore, by applying
the period map we obtain the
Corollary 1.6. Every multiple zeta value of weight N is a Q-linear combination
of ζ(n1, . . . , nr), where ni ∈{2, 3} and n1 + . . . + nr = N.
The point of motivic periods is that they give a mechanism for obtaining infor-
mation on the action of GdR, via the period map, from arithmetic relations between
real numbers. For theorem 1.5, the required arithmetic information comes from a
formula for ζ(2, . . . , 2, 3, 2, . . ., 2) proved by Zagier [38] using analytic techniques.
1.4. Transcendence of motivic periods. With hindsight, theorem 1.5
has less to do with mixed Tate motives, or indeed P1\{0, 1, ∞}, than one might
think. Deﬁne a category H whose objects are given by the following data:
1. A ﬁnite-dimensional Q-vector space MB equipped with an increasing ﬁltra-
tion called the weight, which is denoted by W.
2. A ﬁnite-dimensional Q-vector space MdR equipped with an increasing ﬁltra-
tion W and a decreasing ﬁltration F (the Hodge ﬁltration).
3. An isomorphism compB,dR : MdR ⊗C
∼
→MB ⊗C which respects the weight
ﬁltrations. The vector space MB, equipped with W and the ﬁltration F on
MB ⊗C induced by compB,dR is a Q-mixed Hodge structure.
The category H is Tannakian ([10], 1.10), with two ﬁber functors, so it has a ring
of motivic periods Pm
H. Furthermore, the Betti and de Rham realisations deﬁne a
functor M 7→(MB, MdR, compB,dR) : MT (Z) →H, and hence a homomorphism
Pm
MT (Z) −→Pm
H .
(1.8)
This map is known to be injective, but we do not need this fact.
The main
theorem 1.5 is equivalent to saying that the images ζH(n1, . . . , nr) ∈Pm
H of (1.7)
6
Francis Brown
for ni ∈{2, 3} are linearly independent. In this way, we could have dispensed with
motives altogether and worked with objects in Pm
H, which are elementary.2 This
leads to the following philosophy for a theory of transcendence of motivic periods
in H (or another suitable category of mixed Hodge structures). It diﬀers from
standard approaches which emphasise ﬁnding relations between periods [28].
• Write down arithmetically interesting elements in, say Pm
H, which come from
geometry (i.e., which are periods in the sense of [28]).
• Compute the coaction (1.4) on these motivic periods, and use it to prove
algebraic independence theorems.
Indeed, there is no reason to restrict oneself to mixed Tate objects, as the cate-
gory H does not rely on any conjectural properties of mixed motives. The role
of P1\{0, 1, ∞} was to give an integral representation for the numbers (1.2) and
provide a formula for the coaction.
1.4.1. Multiple modular values. Therefore, in the ﬁnal part of this talk I want
to propose changing the underlying geometry altogether, and replace a punctured
projective line with (an orbifold) M = Γ\\H, where H is the upper half plane,
and Γ ≤SL2(Z) is a subgroup of ﬁnite index. Because of Belyi’s theorem 1.1,
every smooth connected projective algebraic curve over a number ﬁeld is isomor-
phic to an Γ\H. Therefore the (pure) motivic periods obtained in this way are
extremely rich3. It is reasonable to hope that the action of the Tannaka group
on the mixed motivic periods of M should be correspondingly rich and should
generate a large class of new periods suitable for applications in arithmetic and
theoretical physics. Many of these periods can be obtained as regularised iterated
integrals on M = Γ\H (building on those considered by Manin in [32, 33]), and the
philosophy of §1.4 concerning their Galois action can be carried out by computing
a suitable automorphism group of non-abelian group cocyles. There still remains a
considerable amount of work to put this general programme in its proper motivic
context and extract all the arithmetic consequences.
1.5. Contents. In §2, I review the motivic fundamental group of X from its
Betti and de Rham view points, deﬁne motivic multiple zeta values, and derive
their Galois action from ﬁrst principles. The only novelty is a direct derivation of
the inﬁnitesimal coaction from Ihara’s formula. In §3, I state some consequences
of theorem 1.5. In §4 I explain some results of Deligne concerning the motivic
fundamental group of the projective line minus N th roots of unity, and in §5 discuss
the depth ﬁltration on motivic multiple zeta values and its conjectural connection
with modular forms. In §6 I mention some new results on multiple modular values
for SL2(Z), which forms a bridge between multiple zeta values and modular forms.
For reasons of space, it was unfortunately not possible to review the large
2In fact, we should never need to compute relations explicitly using ‘standard operations’ such
as those described in [28]; these are taken care of automatically by the Tannakian formalism, and
the bound on the Ext groups of MT (Z) coming from Borel’s theorems on algebraic K-theory.
3Grothendieck refers to SL2(Z) as ‘une machine `a motifs’
Motivic periods and P1\{0, 1, ∞}
7
recent body of work relating to associators, double shuﬄe equations ([1] §25, [16],
[34]) and applications to knot theory, the Kashiwara-Vergne problem, and related
topics such as deformation quantization; let alone the vast range of applications of
multiple zeta values to high-energy physics and string theory. Furthermore, there
has been recent progress in p-adic aspects of multiple zeta values, notably by H.
Furusho and G. Yamashita, and work of M. Kim on integral points and the unit
equation, which is also beyond the scope of these notes.
Many technical aspects of mixed Tate motives have also been omitted. See [14],
§1-2 for the deﬁnitive reference.
2. The motivic fundamental group of P1\{0, 1, ∞}
Let X = P1\{0, 1, ∞}, and for now let x, y ∈X(C). The motivic fundamental
groupoid of X (or rather, its Hodge realisation) consists of the following data:
1. (Betti). A collection of schemes πB
1 (X, x, y) which are deﬁned over Q, and
which are equipped with the structure of a groupoid:
πB
1 (X, x, y) × πB
1 (X, y, z) −→πB
1 (X, x, z)
for any x, y, z ∈X(C). There is a natural homomorphism
πtop
1 (X, x, y) −→πB
1 (X, x, y)(Q)
(2.1)
where the fundamental groupoid on the left is given by homotopy classes of
paths relative to their endpoints. The previous map is Zariski dense.
2. (de Rham). An aﬃne group scheme4 over Q denoted by πdR
1 (X).
3. (Comparison). A canonical isomorphism of schemes over C
compB,dR : πB
1 (X, x, y) ×Q C
∼
−→πdR
1 (X) ×Q C .
(2.2)
These structures are described below. Deligne has explained ([10], §15) how to
replace ordinary base points with tangential base points in various settings. Denote
such a tangent vector by
→vx = the tangent vector v ∈Tx(P1(C)) at the point x .
Identifying Tx(P1(C)) with C, one obtains natural tangent vectors
→
10 and −
→
11 at
the points 0 and 1 respectively, and a canonical path, or ‘droit chemin’
dch ∈πtop
1
(X,
→
10, −
→
11)
4It shall also be written πdR
1
(X, x, y) but does not depend on the choice of base points. The
fact that there is a canonical isomorphism πdR
1
(X, x, y) = πdR
1
(X) is equivalent to saying that
there is a ‘canonical de Rham path’ between the points x and y.
8
Francis Brown
given by the straight line which travels from 0 to 1 in R with unit speed.
The reason for taking the above tangential base points is to ensure that the
corresponding motive (theorem 2.1) has good reduction modulo all primes p: in
the setting of P1\{0, 1, ∞} there are no ordinary base points with this property.
The following theorem states that the structures 1 −3 are motivic.
Theorem 2.1. There is an ind-object (direct limit of objects)
O(πmot
1
(X,
→
10, −
→
11)) ∈Ind (MT (Z))
(2.3)
whose Betti and de Rham realisations are the aﬃne rings O(πB
1 (X,
→
10, −
→
11)), and
O(πdR
1 (X)), respectively.
Proof. (Sketch) The essential idea is due to Beilinson ([18], theorem 4.1) and Wo-
jtkowiak [39]. Suppose, for simplicity, that M is a connected manifold and x, y ∈M
are distinct points. Consider the submanifolds in M × . . . × M (n factors):
Ni = M i−1 × ∆× M n−i−1
for i = 1, . . . , n −1
where ∆is the diagonal M ⊂M×M. Set N0 = {x}×M n−1 and Nn = M n−1×{y},
and let N ⊂M n be the union of the Ni, for i = 0, . . . , n. Then
Hk(M n, N) =
(
Q[πtop
1 (M, x, y)]/In+1
if k = n
0
if k < n
(2.4)
where the ﬁrst line is the nth unipotent truncation of the fundamental torsor of
paths from x to y (I is the image of the augmentation ideal in Q[πtop
1 (M, x)]; see
below). In the case when M = P1\{0, 1, ∞}, the left-hand side of (2.4) deﬁnes
a mixed Tate motive. The case when x = y, or when x or y are tangential base
points, is more delicate [14], §3.
The Betti and de Rham realisations can be described concretely as follows.
1. (Betti). The Betti fundamental groupoid is deﬁned to be the pro-unipotent
completion of the ordinary topological fundamental groupoid. For simplicity,
take x = y ∈X(C). Then there is an exact sequence
0 −→I −→Q[πtop
1 (X(C), x)] −→Q −→0
where the third map sends the homotopy class of any path γ to 1 (thus I is
the augmentation ideal). Then one has (Malˇcev, Quillen)
O(πB
1 (X, x)) = lim
N→∞

Q[πtop
1 (X, x)]/IN+1∨
The case when x̸ = y is deﬁned in a similar way, since Q[πtop
1 (X(C), x, y)] is
a rank one module over Q[πtop
1 (X(C), x)].
Motivic periods and P1\{0, 1, ∞}
9
2. (de Rham). When X = P1\{0, 1, ∞}, one veriﬁes that
O(πdR
1 (X)) ∼=
M
n≥0
H1
dR(X)⊗n
which is isomorphic to the tensor coalgebra on the two-dimensional graded
Q-vector space H1
dR(X) ∼= Q(−1)⊕Q(−1). We can take as basis the elements
[ωi1| . . . |ωin]
where ωik ∈{ dt
t ,
dt
1−t}
where the bar notation denotes a tensor product ωi1 ⊗. . .⊗ωin. It is a Hopf
algebra for the shuﬄe product and deconcatenation coproduct and is graded
in degrees ≥0 by the degree which assigns dt
t and
dt
1−t degree 1.
Denoting
→
10 and −
→
11 by 0 and 1 respectively, one can write, for x, y ∈{0, 1}
xΠ•
y = Spec(O(π•
1(X, x, y))
where
• ∈{B, dR, mot} .
It is convenient to write xΠy instead of xΠdR
y . It does not depend on x or y, but
admits an action of the motivic Galois group GdR which is sensitive to x and y. If
R is any commutative unitary Q-algebra,
xΠy(R) ∼= {S ∈R⟨⟨x0, x1⟩⟩× : ∆S = S ⊗S}
is isomorphic to the group of invertible formal power series in two non-commuting
variables x0, x1, which are group-like for the completed coproduct ∆deﬁned by
∆(xi) = xi ⊗1 + 1 ⊗xi. The group law is given by concatenation of series.
2.1. Periods. The periods of the motivic fundamental groupoid of P1\{0, 1, ∞}
are the coeﬃcients of the comparison isomorphism compB,dR (2.2) with respect to
the Q-structures on the Betti and de Rham sides. Let
01B
1
∈
πB
1 (X,
→
10, −
→
11)(Q)
⊂
O(πB
1 (X,
→
10, −
→
11))∨
denote the image of dch under the natural map (2.1). It should be viewed as a
linear form on the aﬃne ring of the Betti π1. For all ωik ∈{ dt
t ,
dt
1−t},
⟨compB,dR([ωi1| . . . |ωin]), 01B
1 ⟩=
Z
dch
ωi1 . . . ωin
(2.5)
The right-hand side is the iterated integral from 0 to 1, regularised with respect to
the tangent vectors 1 and −1 respectively, of the one-forms ωik. No regularisation is
necessary in the case when ωi1 =
dt
1−t and ωin = dt
t , and in this case the right-hand
side reduces to the formula (1.2). In general, one can easily show:
Lemma 2.2. The integrals (2.5) are Z-linear combinations of MZV’s of weight n.
The Drinfeld associator is the de Rham image of dch
Z = compB,dR(01B
1 ) ∈0Π1(C)
10
Francis Brown
Explicitly, it is the non-commutative generating series of the integrals (2.5)
Z =
X
ik∈{0,1}
xi1 . . . xin
Z
dch
ωi1 . . . ωin
(2.6)
= 1 + ζ(2)[x1, x0] + ζ(3)([x0, [x0, x1]] + [x1, [x1, x0]]) + · · ·
(2.7)
It is an exponential of a Lie series.
2.2. Motivic multiple zeta values. By the previous paragraph, the
aﬃne ring of the de Rham fundamental group is the graded Hopf algebra
O(xΠy) ∼= Q⟨e0, e1⟩
independently of x, y ∈{0, 1}. Its product is the shuﬄe product, and its coproduct
is deconcatenation. Its basis elements can be indexed by words in {0, 1}. By a
general fact about shuﬄe algebras, the antipode is the map w 7→w∗where
(a1 . . . an)∗= (−1)nan . . . a1
is signed reversal of words. Thus any word w in {0, 1} deﬁnes a de Rham element
in O(xΠy). The augmentation map Q⟨e0, e1⟩→Q corresponds to the unit element
in the de Rham fundamental group and deﬁnes a linear form x1dR
y
∈O(xΠy)∨.
Deﬁne Betti linear forms x1B
y ∈O(xΠB
y )∨to be the images of the paths
dch if x = 0, y = 1
;
dch−1 if y = 1, x = 0
;
cx if x = y ,
where dch is the straight path from 0 to 1, dch−1 is the reversed path from 1 to 0,
and cx is the constant (trivial) path based at x.
Out of this data we can construct the following motivic periods.
Deﬁnition 2.3. Let x, y ∈{0, 1} and let w be any word in {0, 1}. Let
Im(x; w; y) = [O(xΠmot
y
), w, x1B
y ]m
∈
Pm,+
MT (Z),R
(2.8)
We call the elements Im motivic iterated integrals. The ‘de Rham’ motivic
period is the matrix coeﬃcient [O(xΠmot
y
), w, x1dR
y ] on MT (Z) with respect to
the ﬁber functors ωdR, ωdR. It deﬁnes a function on GdR. Its restriction to the
prounipotent group U dR deﬁnes an element Iu(x; w; y) ∈O(U dR). The latter are
equivalent to objects deﬁned by Goncharov (which he also called motivic iterated
integrals).
Deﬁnition 2.3.1. Deﬁne motivic (resp. unipotent) multiple zeta values by
ζ•(n1, . . . , nr) = I•(0; 10n1−1 · · · 10nr−1; 1) ,
• = m, u
It is important to note that ζm(2) is non-zero, whereas ζu(2) = 0.5 We imme-
diately deduce from the deﬁnitions that
(i).
Im(x; w; x) = δw,∅
for x ∈{0, 1}
(ii).
Im(x; w; y) = Im(y; w∗; x)
(2.9)
5One can deﬁne a homomorphism Pm,+
MT (Z),R →Pu
MT (Z) which sends ζm(n1, . . . , nr) to
ζu(n1, . . . , nr) and prove that its kernel is the ideal generated by ζm(2).
Motivic periods and P1\{0, 1, ∞}
11
The ﬁrst property holds because the constant path is trivial, the second follows
from the antipode formula and because dch◦dch−1, or dch−1◦dch, is homotopic to
a constant path. Finally, replacing multiple zeta values with their motivic versions,
we can deﬁne a motivic version of the Drinfeld associator
Zm =
X
i1,...,in∈{0,1}
xi1 . . . xinIm(0; i1, . . . , in; 1) .
(2.10)
It satisﬁes the associator equations deﬁned by Drinfeld [15], on replacing 2πi by
Lm (using the fact that ζm(2) = −(Lm)2
24
), and the double shuﬄe equations of [34].
2.3. Action of the motivic Galois group. The category MT (Z) is
a Tannakian category with respect to the de Rham ﬁber functor. Therefore the
motivic Galois group acts on the aﬃne ring O(0Π1) of the de Rham realisation of
the motivic fundamental torsor of path (2.3). A slight generalisation of theorem
2.1 shows that GdR acts on the de Rham fundamental schemes
xΠy
for all x, y ∈{0, 1}
and furthermore, is compatible with the following structures:
• (Groupoid structure). The multiplication maps
xΠy × yΠz −→xΠz
for all x, y, z ∈{0, 1}.
• (Inertia). The action of U dR ﬁxes the elements
exp(x0) in 0Π0(Q)
and
exp(x1) in 1Π1(Q)
The groupoid structure is depicted in ﬁgure 1.
0
0Π1
1
1Π0
0Π0
1Π1
Figure 1. The groupoid xΠy for x, y ∈{0, 1}. The diagram only represents the groupoid
structure; the paths shown do not accurately depict the tangential base points.
The local monodromy map πtop
1
(Gm,
→
10) →πtop
1
(X,
→
10) (where we write Gm
for P1\{0, ∞}), corresponding to monodromy around 0, has a motivic analogue
which gives rise to the inertial condition. Its de Rham realisation is the map
πdR
1 (Gm,
→
10) →πdR
1 (X,
→
10) = 0Π0
and is respected by GdR. One shows that U dR acts trivially on πdR
1 (Gm,
→
10), and
furthermore that the element exp(x0) ∈0Π0(Q) is in the image of the previous
map. This gives the ﬁrst inertial condition.
12
Francis Brown
Remark 2.4. It is astonishing that one obtains much useful information at all from
such symmetry considerations. Nonetheless, it is enough to show the faithfulness
of the action of GdR (below). There are further structures respected by GdR, such
as compatibilities with automorphisms of P1\{0, 1, ∞}. They are not required.
2.4. Ihara action. Let A denote the group of automorphisms of the groupoid
xΠy for x, y ∈{0, 1} which respects the structures 1, 2 described in §2.3.
Proposition 2.5. The scheme 0Π1 is an A-torsor. In particular, the action of A
on 1 ∈0Π1 deﬁnes an isomorphism of schemes
a 7→a(1) : A −→0Π1 .
(2.11)
The action of A on 0Π1 deﬁnes, via this isomorphism, a new group law
◦: 0Π1 × 0Π1 →0Π1 .
It is given explicitly on formal power series by Ihara’s formula
A(x0, x1) ◦G(x0, x1) = G(x0, Ax1A−1)A
(2.12)
Proof. For the basic geometric idea, see [27], §2.3. Let a ∈A, and write axy(ξ) for
the action of a on ξ ∈xΠy. Write a = a01(1). Since 0Π0 is a group, a acts trivially
on its identity element, and so a00(1) = 1. Via the map 0Π1 × 1Π0 →0Π0 we have
a01(1)a10(1) = a00(1) and hence a10(1) = a−1. The inertial conditions give
a00(exp(x0)) = exp(x0)
and
a11(exp(x1)) = exp(x1)
(2.13)
Now the composition of paths 1Π0 × 0Π0 × 0Π1 →1Π1 gives rise to an equation
1. exp(x1).1 = exp(x1). Applying a to this gives by the second equation in (2.13)
a00(exp(x1)) = a exp(x1)a−1 = exp(ax1a−1)
(2.14)
which completely determines the action of A on 0Π0. Via the map 0Π0×0Π1 →0Π1
we have the equation g.1 = g, and hence
a01(g) = a00(g).a .
(2.15)
Formula (2.12) follows from (2.13), (2.14), (2.15). One easily checks that a uniquely
determines a, and so (2.11) is an isomorphism (see also [14], 5.9.)
The groupoid and inertia structures are preserved by U dR, giving a morphism
ρ : U dR −→A
(2.11)
∼=
0Π1
(2.16)
such that the following diagram commutes
U dR × 0Π1 −→0Π1
(2.17)
ρ×id ↓
↓id
0Π1 × 0Π1
◦
−→0Π1
In principle this describes the action of the motivic Galois group on 0Π1. Note,
however, that the map (2.16) is mysterious and very little is known about it.
Motivic periods and P1\{0, 1, ∞}
13
2.5. Dual formula. The coaction on motivic iterated integrals is dual to
Ihara’s formula. Dualising (2.17), we have
∆: O(0Π1) −→O(U dR) ⊗O(0Π1)
It is equivalent, but more convenient, to consider the inﬁnitesimal coaction
D : O(0Π1) −→L ⊗O(0Π1)
 D(x) = ∆(x) −1 ⊗x
mod O(U dR)2
>0

where L = O(U dR)>0/
 O(U dR)>0
2 is the Lie coalgebra of indecomposables in
O(U dR).
The following formula is an inﬁnitesimal variant of a formula due to
Goncharov [20], relating to slightly diﬀerent objects. In order to ﬁll a gap in the
literature, I will sketch how it follows almost immediately from Ihara’s formula.
Proposition 2.6. Let a0, . . . , an+1 ∈{0, 1}. The coaction D is given by
D(Im(a0; a1, . . . , an; an+1)) =
X
0≤p<q≤n

Iu(ap; ap+1, . . . , aq; aq+1)

(2.18)
⊗Im(a0; a1, . . . , ap, aq+1, . . . , an; an+1) .
where the square brackets on the left denote the map [ ] : O(U dR)>0 →L.
Proof. Denote the action of Lie A on Lie 0Π0 by ◦0. By (2.11), Lie A ∼= Lie 0Π1
is the set of primitive elements in its (completed) universal enveloping algebra
which we denote simply by U(0Π1). By (2.13) and (2.14) we have a ◦0 x0 = 0 and
a ◦0 x1 = ax1 −x1a. The antipode on U(0Π1) is given by the signed reversal ∗.
Since a ∈U(0Π1) is primitive, a = −a∗and also
a ◦0 x0 = 0
and
a ◦0 x1 = ax1 + x1a∗.
This extends to an action on U(0Π0) via a ◦0 w1w2 = (a ◦0 w1)w2 + w1(a ◦0 w2).
Now consider the action a◦0· on the following words. All terms are omitted except
those terms where a or a∗is inserted in-between the two bold letters:
a ◦0 w1x0x0w2 = · · · + 0 + · · ·
a ◦0 w1x0x1w2 = · · · + w1x0ax1w2 + · · ·
a ◦0 w1x1x0w2 = · · · + w1x1a∗x0w2 + · · ·
a ◦0 w1x1x1w2 = · · · + w1x1ax1w2 + w1x1a∗x1w2
|
{z
}
0
+ · · ·
These four equations are dual to all but the ﬁrst and last terms in (2.18), using
the fact that Iu(x; w; x) = 0 for x = 0, 1 (ﬁrst and fourth lines), and the fact that
Iu(1; w∗; 0) = Iu(0; w; 1) (third line). A straightforward modiﬁcation of the above
argument taking into account the initial and ﬁnal terms (using (2.15)) shows that
the action ◦1 of Lie A on 0Π1 is dual to the full expression (2.18).
14
Francis Brown
Armed with this formula, we immediately deduce that for all n ≥2,
D ζm(n) = [ζu(n)] ⊗1
(2.19)
where we recall that ζu(2n) = 0. One easily shows that ζu(2n + 1)̸ = 0 for n ≥1.
See also [22].
Denote the map w 7→[Iu(0; w; 1)] : O(0Π1)>0 →L simply by
ξ 7→[ξu]. From the structure §1.1, 1 of GdR we have the following converse to
(2.19) ([5], §3.2).
Theorem 2.7. An element ξ ∈O(0Π1) of weight n ≥2 satisﬁes Dξ = [ξu] ⊗1 if
and only if ξ ∈Q ζm(n).
This theorem, combined with (2.18), provides a powerful method for proving
identities between motivic multiple zeta values. Applications are given in [6].
