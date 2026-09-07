---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
Among knot invariants, the colored Jones polynomials {JK,n}n≥2 and the Kashaev invari-
ants{⟨K⟩N}N≥2 are of particular interest, by their relation to quantum ﬁeld theory, and
the geometry of hyperbolic manifolds [40, 28]. We refer to e.g. [28, 42] for their deﬁnitions;
by [28], the two invariants are related by ⟨K⟩N = JK,N(e2πi/N). We refer to [22, 23, 13] for
more results and references on this topic.
The Kashaev invariant is extended to a function on roots of unity by setting, for (h,k ) = 1,
JK,0(e2πih/k) := JK,k(e2πih/k). For ﬁxed k, the values ( JK,0(e2πih/k))(h,k)=1 are simply the
Galois conjugates of⟨K⟩N in Q(e2πi/k). In the case of K = 41, the simplest hyperbolic knot,
we have explicitly
J41,0(q) =
∞∑
r=0
|(1−q)(1−q2)··· (1−qr)|2(1.1)
for a root of unity q. In general, JK,0(q) can be written as a series of this kind, involving a
ratio of q-Pochhammer symbols of various indexes. See Section 2.4 for some more examples
and the precise deﬁnition of JK,0(q) in the cases we will consider.
The volume conjecture [28, Section 5] predicts that
(1.2) lim
N→∞
log|⟨K⟩N|
N = lim
N→∞
log|JK,0(e2πi/N)|
N =‖K‖
2π v3,
where‖K‖ is related to the Gromov simplicial volumes of the complement of K, and v3 is
a suitable constant (the volume of the ideal regular tetrahedron in H3). All the knots we
will refer to in this paper will be hyperbolic; in this case, the asymptotic formula (1.2) was
conjectured by Kashaev [24], and‖K‖v3 = Vol(K), the hyperbolic volume of the complement
ofK in the 3-sphere. This is motivated by the analogy between the usual dilogarithm, which
Date: March 5, 2020.
2010 Mathematics Subject Classiﬁcation. 11B65 (primary), 57M27, 11F03, 60F05 (secondary).
Key words and phrases. q-Pochhammer symbol, dilogarithm, quantum knot invariants, modularity, limit
law.
1
arXiv:1905.02045v3  [math.NT]  4 Mar 2020
2 S. BETTIN AND S. DRAPPEAU
measures volumes of tetrahedra in the hyperbolic space, and the quantum dilogarithm, which
are the building blocks of Kashaev’s invariant.
This conjecture was extended in [20] to a full asymptotic expansion, referred to as the
arithmeticity conjecture in [12], whereas the corresponding question for the imaginary part of
the logarithm is conjectured to involve the Chern-Simons invariant cs( K) of K [29, 20]. The
arithmeticity conjecture has been proved for all knots with up to seven crossings in [2, 32, 34,
33]. We refer to [15, 31, 30, 27, 25] and the references therein for more results and information
on the volume conjecture.
In [43], Zagier studies several examples of what is called “quantum modular forms”. Mo-
tivated by extensive numerical computations, he predicts that JK,0 satisﬁes an approximate
modularity property which relates, in the limit as x→∞ among rationals of bounded denom-
inator,JK,0(e2πi(ax+b)/(cx+d)) withJK,0(x) for any ( a b
c d)∈ SL(2, Z). More speciﬁcally, given
a hyperbolic knot K, the following conjecture is made (cf. also [17])
Conjecture 1 (Zagier’s modularity conjecture for K). For all γ∈ SL2(Z) such that 1 α :=
γ(∞)∈ Q, there exist CK(α)∈ C and a sequence (DK,n(α))n≥0 of complex numbers such
that, for all M∈ N and x∈ Q, with x→∞ , there holds
(1.3)
JK,0(e(γ(x)))
JK,0(e(x)) =
(2π
ℏ
)3/2
ei V ol(K)−i cs(K)
ℏ CK(α)
( ∑
0≤n<M
DK,n(α)ℏn+O(ℏM)
)
, ℏ := 2πi
x−γ−1(∞),
where e(x) := e2πix and the implied constant depends at most on α, on the denominator of x
and on M. Moreover, if FK is the invariant trace ﬁeld of K, and FK,α :=FK(e(α)), then:
• CK(α) is a product of rational powers of elements of FK,α;
• DK,n(α)∈FK,α for n≥ 0.
In the case K = 41, Garoufalidis and Zagier [18] announced a proof of Theorem 1, and also
numerically investigated the conjecture for other knots. The case of the 4 1 knot is special
and rather simpler than that of other knots, due to the fact that in this case all the sum-
mands in the deﬁnition (1.1) of J41,0 are positive. One can then use Laplace’s method to
extract the asymptotic expansion (1.3). In general, this positivity is not present and there
is a remarkable amount of cancellation among the terms. Indeed, JK,0(e(1/N)) is typically
exponentially smaller than the largest summands in its deﬁnition, and this prevents one from
applying a direct estimation based on Laplace’s method. We circumvent this serious obstacle
by obtaining a new modularity relation, with a precise description of the holomorphic and pe-
riodic behaviour of the error terms, for the q-Pochhammer symbol. This symbol is of crucial
importance in the theory of q-series and often appears in the theory of modular forms and
combinatorics (see for example [7] and references therein). For r∈ Z≥0, it is deﬁned as
(1.4) ( q)r :=
r∏
i=0
(1−q)r, q ∈ C.
When|q| < 1, one can also take r = +∞ and obtain the Dedekind η-function η(z) :=
e(z/24)(e(z))∞, an important example of a (half-integral weight) modular form. As such, η
satisﬁes the relation
η(γz) =ϑ(γ)(cz +d)
1
2η(z), γ = (a b
c d)∈ SL(2, Z),
1In what follows, a matrix in SL(2 , R) acts on C by homography.
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 3
for a certain “multiplier system” ϑ (see [21, Section 2.8]). This modularity relation can be
naturally extended to the partial product at root of unities. Indeed, in Theorem 6 below we
show that for α∈ Q, 1≤r< den(γα) we have
(1.5) e
(γα
24
)
(e(γα))r =ϑ(γ) e
(α
24
)
(e(α))r′ψγ(α,r )
for some 1 ≤ r′ < den(α) and where ψγ(α,r ) is an explicit function with suitable holomor-
phicity properties. We refer to Section 2 for the precise formulation of this reciprocity formula
which we believe to be of independent interest. With this new tool, we can reduce Zagier’s
modularity conjecture to a slightly modiﬁed form of the arithmeticity conjecture, thus show-
ing that the two conjectures are “morally equivalent”. In particular, we are able to prove the
conjecture for all hyperbolic knots K⁄= 7 2 with at most seven crossings, since for these the
arithmeticity conjecture is known by works of Andersen and Hansen [2] (in the case K = 41),
Ohtsuki [32, 33] (in the case K = 52 and with 7 crossings) and Ohtsuki and Yokota [34] (in
the case of 6 crossings).
Theorem 1. Let K⁄= 72 be a hyperbolic knot with at most 7 crossings. Then Conjecture 1
holds for K. The constant CK(α) has the shape
(1.6) CK(α) = e
(νK
2 s(α)
)
cνK/2Λ1/c
K,αδ−1/2
K ,
wherec is the denominator of α, ΛK,α∈FK,α, νK∈ Z, and δK∈FK, νK is given in Figure 4
below and s(α) is the Dedekind sum (see (2.4)).
Remark 1. By the works [35, 32, 34, 33], the number ±2iδ−1
K can be interpreted as the
conjugate of a twisted Reidemeister torsion of K. Our method gives the constant term CK·
DK,0 as an explicit product of algebraic numbers; in Remark 6 in Section 3 we give as examples
its value in the cases of K = 41 and K = 51.
Remark 2. Recently, Calegari, Garoufalidis and Zagier [12] made a more precise conjecture
onCK(α), predicting it naturally factors as µK,8c·εK(α)1/c/√δK, where c is the denominator
of α, µK,8c is a 8c root of unity, εK(α) is a unit of FK,α and δK∈FK. We do not at present
have such a precise description ofCK(α). This would presumably require a ﬁne understanding
of the congruence sums (3.7).
By the work of Ohtsuki [33], the arithmeticity conjecture is known also for K = 72 and we
expect that our method would give Theorem 1 also in this case. However, the proof of this
case is more involved, so we decided to exclude this case for simplicity. In any case, we want
to stress again that the scope of our work is more general and suggests that any proof of the
arithmeticity conjecture should be adaptable into a proof of the modularity conjecture via the
use of the reciprocity relation (1.5).
The modularity and the volume conjectures likely don’t give the full picture on the sym-
metries ofJK,0 nor on its values at roots of unity. Indeed, in the case of K = 41 we can show
that Theorem 1 can be complemented by a second reciprocity formula relating X = h
k with
X′ = h
k , where the overline indicates the multiplicative inverse modulo the denominator. This
new reciprocity formula involves the “cotangent sum” (which appears also in the main term
in the variation, eﬀective for other ranges of the parameters, of the reciprocity formula given
in Theorem 8 below)
c0(h/k) :=−
k−1∑
m=1
m
k cot
(πmh
k
)
, (h,k ) = 1,k≥ 1,
4 S. BETTIN AND S. DRAPPEAU
which is itself a quantum modular form [9] and has been widely studied due to its connection to
the B´ aez-Duarte-Nyman-Beurling criterion for the Riemann hypothesis (see, for example, [5,
3, 4, 39]).
Theorem 2. Let 1≤h≤k with (h,k ) = 1. Then
(1.7) J41,0
(
e(h/k)
)
J41,0
(
e(k/h)
) = exp
(Vol(41)
2π
k
h +E(h,k )
)
,
where
E(h,k )≪ 1
k max
0≤r′<h
⏐⏐⏐
∑
1≤n≤r′
cot
(
πnk
h
)n
h
⏐⏐⏐ + 1
h
⏐⏐⏐ c0
(k
h
)⏐⏐⏐ + logk
h + k
h2.(1.8)
This may be compared with (1.3). Note that cs(4 1) = 0, so there is no corresponding
contribution on the right-hand side of (1.7).
In this case as well, the reciprocity formula (1.7) stems from a corresponding relation for
the q-Pochhammer symbol (see Theorem 7 below). Notice that, despite not giving a full
asymptotic expansion, (1.7) is completely uniform. In particular, it permits to be successfully
iterated for “typical” roots of unity, allowing us to deduce the following law of large numbers
for logJ41,0.
Theorem 3. Forα∈ Q∩ (0, 1) with continued fraction expansion [0;b1,...,b r], br > 1, let
r(α) :=r, Σ(α) :=
r∑
𝓁=1
b𝓁.
Then, as Σ(α)/r(α)→∞ , we have
(1.9) logJ41,0(e(α))∼ Vol(41)
2π Σ(α).
In particular, for almost all roots of unity q of order n≤N, one has
(1.10) log J41,0(q)∼ 12
π2
Vol(41)
2π logn log logn
as N→∞ .
Equation (1.10) can be seen as a version of the volume conjecture (1.2) for typical roots
of unity. Indeed, the volume conjecture provides the asymptotic behavior of log J41,0 at the
root of unity e(1 /N), whereas our result gives the asymptotic for almost all roots of unity
of denominator≤N. Notice then in both cases the leading constant involves the hyperbolic
volume Vol(41), but the size of J41,0 changes dramatically.
Equation (1.9) is stronger than (1.10), which will be readily deduced by [10], and gives an
asymptotic formula in most cases, e.g. when α is restricted to rational numbers with bounded
r(α) as the denominator of α goes to inﬁnity. In particular, it generalises the volume conjec-
ture, which corresponds to the case α = 1/N = [0;N]. It is very likely that the assumption
Σ(α)/r(α)→∞ cannot be removed in general. Indeed, if for example αn = Fn−1/Fn with
Fn the n-th Fibonacci number so that Σ( αn) = r(αn) + 1 =n− 1, then Theorem 1.9 would
give logJ41,0(e(αn))∼Cn, with C = Vol(41)
2π ≈ 0.323... , whereas numerically it appears that
F (αn) grows like C′n, for C′≈ 1.1 (cf. also [43, Figure 6]).
Our proof of Theorems 3 depends crucially on the positivity of the summands in (1.1) which
is missing if K⁄= 4 1. Nonetheless, we expect a similar result holds for all hyperbolic knots.
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 5
Also, since Σ(α) is distributed according to a stable law [10], we expect the same to hold for
log|JK,0(e(α))| for any hyperbolic knot K.
Conjecture 2. Let K be a hyperbolic knot. There exists a constant DK∈ R such that for
any interval [a,b ]⊂ R there holds
|QN|−1
⏐⏐⏐
{
q∈QN
⏐⏐⏐
(log|JK,0(q)|
Vol(K)
2π logN
− 12
π2 log logN−DK
)
∈ [a,b ]
}⏐⏐⏐
=
∫ b
a
f1(x; 6
π, 1, 0)dx +o(1)
(1.11)
as N→∞ , where QN is the set of roots of unity of order ≤N, and c↦→f1(c; 6
π, 1, 0) is the
density of the stable law S1( 6
π, 1, 0). In particular,
log|JK,0(q)|∼ 12
π2
Vol(K)
2π logn log logn
for almost all roots of unity q of order n≤N as N→∞ .
In [43] Zagier discusses the continuity with respect to the real topology of
H41(h/k) := log|J41,0(e(h/k))|− log|J41,0(e(k/h))|
and suggests thatH41 is discontinuous butC∞ from the right and the left at non-zero rationals2
and continuous but not diﬀerentiable as one approaches irrational numbers. Using Lebesgue’s
integrability condition and [10], one can easily show that this continuity condition together
with a suitable continuity condition at zero implies Conjecture 2.
Theorem 4. LetK be a hyperbolic knot. Assume the following:
• HK(h/k) := log |JK,0(e(h/k))|− log|JK,0(e(k/h))| has a limit as h/k tends to any
positive irrational number,
• HK(h/k)− Vol(K)
2π
k
h− 3
2 log(k/h) is uniformly bounded.
Then Conjecture 2 holds with DK = 1−γ0−log 2
π2/12 + 24
πVol(K)
∫ 1
0
HK (1/t)− V ol(K)
2πt
1+t dt, the function HK
being extended to R>0 by taking limits over the rationals.
Remark 3. One could replace the second assumption in Theorem 4 with the assumption that
HK(h/k)− Vol(K)
2π
k
h− 3
2 log(k/h) is left and right continuous as h/k approaches any rational
number.
In the case of torus knots, the invariant JK,0 can still be constructed and a formula of
type (1.3) is expected to hold with Vol( K) replaced by 0. In this situation, the works [6, 10]
would suggest that log|JK,0(q)|√logn becomes distributed according to a Gaussian law. In this case
however, the conditions of Theorem 4 are not suﬃcient to conclude.
In view of Theorem 2, it is natural to wonder if also the functionH∗
K(h/k) := log|JK,0(e(h/k))|−
log|J41,0(e(k/h))| could be regular at irrational points. We can answer this question in the
negative in the case of K = 41.
Theorem 5. For all x∈ [0, 1] we have lim supy→x±,y∈Q|H∗
41(y)| = +∞.
2This continuity property at rationals follows from the modularity conjecture but only when approaching a
rational h/k = [0; b1, . . . , br] with fractions essentially of the form [0; b1, . . . , br, N] with N → ∞; and not, for
example, with [0; b1, . . . , br, N1, N2] with both N1, N2 ∈ N going to inﬁnity.
6 S. BETTIN AND S. DRAPPEAU
Figure 1. Global graph of H41 and H∗
41
Figure 2. Graph of H41 and H∗
41 around x = 0.485
