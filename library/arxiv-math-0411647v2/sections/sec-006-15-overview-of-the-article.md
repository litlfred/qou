---
doc_id: arxiv-math-0411647v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS"
section_id: sec-006-15-overview-of-the-article
section_title: "Overview of the article"
section_number: 1.5
pages: 6-13
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear combination of indicators of many"
---
the normalized indicators of conjugacy classes Σ k1 ,...,k l and the Jucys–
Murphy element J. We also outline brieﬂy how important properties of
Young diagrams and representations of Sq are encoded by the distribution
of J. It will be convenient to use in this article the language of t he proba-
bility theory (‘distribution’ and ‘moments’ of ‘random variables’) therefore
we also introduce the necessary conventions, however a reader might easily
translate all statements into her/his favorite language. We also recall brieﬂy
some notions connected with partitions of ﬁnite ordered set s: fat partitions
and non–crossing partitions.
In the central part of this paper, Section 3, we introduce the calculus of
partitions and study its properties. This part is written as a ‘user–friendly
user guide’: we postponed all technical and boring proofs to Section 5 in
order to allow the readers to use the calculus of partitions without troubling
why the machinery works.
In Section 4 we study general properties of free cumulants of the Jucys–
Murphy element; in particular in Section 4.4 we ﬁnd explicitly the second–
order asymptotic expansion of these cumulants.
Section 5 is devoted to proofs of some technical results.
In Section 6 we present some ﬁnal remarks. Especially intere sting are
Sections 6.1 and 6.2 where we present connections with the wo rk of Biane
[Bia98] and Okounkov [Oko00]. Section 6.2 provides a natura l geometric
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 7
interpretation of pushing partitions and it can be used to rephrase the results
of Okounkov in a more combinatorial language.
2. P RELIMINARIES
2.1. Symmetric group. There are many equivalent deﬁnitions of the tran-
sition measure of a Young diagram [VK85, Ker93, Ker99, OV96, Bia98,
Oko00] and for the sake of completeness we shall recall them i n the fol-
lowing. Nevertheless, we shall use in this article only the d escription from
Section 2.1.8.
2.1.1. Transition measure of a Young diagram—the eigenvalues appr oach.
The following description of the transition measure is due to Biane [Bia98]
and probably it is the simplest one.
Consider an element Γ ∈ Mq +1
(
C(Sq )
)
given by
(2.1) Γ =








0 (1, 2 ) ( 1, 3 ) . . . (1, q ) 1
(1, 2 ) 0 (2, 3 ) . . . (2, q ) 1
(1, 3 ) ( 2, 3 ) 0 . . . (3, q ) 1
.
.
. .
.
. .
.
. ... .
.
. .
.
.
(1, q ) ( 2, q ) ( 3, q ) . . . 0 1
1 1 1 . . . 1 0








,
where (i, j ) ∈ Sq denotes the transposition exchanging i and j.
Let ρλ : C(Sq ) → Mk(C) be an irreducible representation of Sq 
corresponding to the Young diagram λ. We apply map ρλ to every en-
try of the matrix Γ ∈ Mq +1(Sq ) and denote the outcome by ρλ(Γ) ∈
Mq +1
(
Mk(C)
)
= M(q +1)k(C). Alternatively, if we treat Γ as an element
of Mq +1(C) ⊗ C(Sq ) then ρλ(Γ) = ( 1 ⊗ ρλ)Γ ∈ Mq +1(C) ⊗ Mk(C) =
M(q +1)k(C).
Let ζ1, . . . , ζ (q +1)k ∈ R be the eigenvalues of the matrix ρλ(Γ) ∈
M(q +1)k(C); then the transition measure of the Young diagramλ is the prob-
ability measure on R which (up to a normalization) is the counting measure
of eigenvalues of ρλ(Γ):
µ λ =
δζ1 + · · · + δζ(q+1)k
(q + 1)k .
2.1.2. Generalized Young diagrams. Let λ be a Young diagram. We assign
to it a piecewise afﬁne function ω λ : R → R with slopes ±1, such that
ω λ(x) = |x|for large |x|as it can be seen on the example from Figure 2.2.
By comparing Figure 2.1 and Figure 2.2 one can easily see thatthe graph of
ω λ can be obtained from the graphical representation of the Young diagram
by an appropriate mirror image, rotation and scaling by the f actor
√
2. We
8 PIOTR ´SNIADY
FIGURE 2.1. Young diagram associated with a partition 8 =
4 + 3 + 1.
x1 y1 x2 y1 x3 y3 x4
FIGURE 2.2. Generalized Young diagram associated with a
partition 8 = 4 + 3 + 1.
call ω λ the generalized Young diagram associated with the Young diagram
λ [Ker93, Ker98, Ker99]. Alternatively, we can encode the Young diagram
λ using the sequence of local minima of ω λ (denoted by x1, . . . , x m ) and
the sequence of local maxima of ω λ (denoted by y1, . . . , y m − 1), which
form two interlacing sequences of integers [Ker98].
The class of generalized Young diagrams consists of all func tions ω :
R → R which are Lipschitz with constant 1 and such that ω (x) = |x|for
large |x|and of course not every generalized Young diagram can be obtained
by the above construction from some Young diagram λ.
The setup of generalized Young diagrams is very useful in the study of
the asymptotic properties since it allows us to deﬁne easily various notions
of convergence of the Young diagram shapes.
2.1.3. Transition measure—the analytic approach. To any generalized
Young diagram ω we can assign the unique probability measure µ ω on
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 9
R, called transition measure of ω , which fulﬁlls
(2.2) log
∫
R
1
z − xdµ ω (x) = − 1
2
∫
R
log(z − x)ω ′′(x)dx
for every z /∈ R [OV96, Bia98, Oko00]. A great advantage of this deﬁnition
is that after applying integration by parts one can easily se e that the map
ω ↦→ µ ω is continuous in many reasonable topologies.
The generalized Young diagram ω pλ : x ↦→ pω λ( x
p
)
corresponds to the
Young diagramλ geometrically scaled by factor p > 0 ; it is easy to see that
(2.2) implies that the corresponding transition measure µ pλ is a dilation of
µ λ:
(2.3) µ pλ = Dpµ λ.
The above deﬁnition (2.2) becomes simpler in the case of the ( usual)
Young diagrams
∫
R
1
z − x dµ λ(x) =
∏
1≤i≤m − 1(z − yi)∏
1≤i≤m (z − xi)
and implies that the transition measure is explicitly given by
µ λ =
∑
1≤k≤n
∏
1≤i≤n− 1(xk − yi)∏
i⁄=k(xk − xi) δxk .
2.1.4. Transition measure—the representation theoretic approac h. It is
possible to ﬁnd another interpretation of transition measure in the language
of representation theory [OV96, Bia98, Oko00]: let us consi der the repre-
sentation [λ] ↑
Sq+1
Sq of Sq +1 induced from the representation [λ] of Sq . By
the branching rule [λ] ↑
Sq+1
Sq decomposes as a direct sum of representations
corresponding to the Young diagrams obtained from λ by adding one box.
It is possible to add a box exactly at the minimaxk. The measure µ λ assigns
a mass to each point xk which is proportional to the dimension of the irre-
ducible representation of Sq +1 corresponding to the diagram λ augmented
in point xk.
2.1.5. Partial permutations. The following notion was introduced and
studied by Ivanov and Kerov [IK99]. A partial permutation of the set
A is a pair α = ( d, w ), where d ⊆ A and w : A → A is any bijec-
tion such that d(x) = x for every x ∈ A \ d. Set d is called the sup-
port of α . The set of partial permutations of A will be denoted by ~SA .
Given two partial permutations (d1, w 1), (d2, w 2) we consider their prod-
uct (d1, w 1) · (d2, w 2) := ( d1 ∪ d2, w 1w2); given this multiplication the
set~SA of partial permutations becomes a semigroup. By SA we denote the
permutation group of the set A. There is an important homomorphism of
10 PIOTR ´SNIADY
semigroups~SA → SA given by forgetting the support (d, w ) ↦→ w; there-
fore every partial permutation can be regarded as a (usual) p ermutation as
well.
For A ⊆ B there is a homomorphism θB
A : C(~SB) → C(~SA ) of partial
permutation algebras given by
θB
A (d, w ) =
{
(d, w ) if d ⊆ A,
0 otherwise.
By C(~S∞) we denote the projective limit of algebras C( ~S{1,...,q }) with re-
spect to the morphisms θ.
2.1.6. Abelian algebras in the language of probability theory. Usually as a
primary object of the probability theory one considers a Kolmogorov space
(Ω, M, P )—where Ω is a set, M is a σ–ﬁeld of measurable sets and P
is a probability measure— but equally well we may consider an Abelian
algebra A of all random variables on Ω with all moments ﬁnite and the
expected value EC : A → C. More generally, if M ′ is a σ–subﬁeld of M
we may consider an algebra B of M ′–measurable random variables and a
conditional expectation EB : A → B. In this way the probability theory
becomes a theory of Abelian algebras A equipped with a linear functional
EC or, more generally, a theory of pairs of Abelian algebras B ⊂ A and
maps EB : A → B.
By turning the picture around we may regard any Abelian algeb ra A
equipped with a linear map E as an algebra of random variables even if A
does not arise from any Kolmogorov space (this observation was a starting
point of the non–commutative probability theory [Mey93]). Now we can
use the probability theoretic language when speaking about A: elements of
A can be called random variables and the numbersE(Xk) can be called mo-
ments of the random variable X ∈ A. Similarly we shall interpret pairs of
Abelian algebras B ⊂ A equipped with a map E : A → B.
In the classical probability theory any real–valued randomvariable X can
be alternatively viewed as a selfadjoint multiplication operator on the alge-
bra A and according to the spectral theorem can be written as an ope rator–
valued integral X =
∫
R z dQ(z), where Q denotes the spectral measure of
X. It is easy to see that the distribution µ of the random variable X and the
spectral measure of the operator X are related by equality µ (F) = EC[Q(F)]
for any Borel set F ⊆ R. This simple observation can be used in our new
setup to deﬁne a distribution µ of an element X = X⋆ ∈ A to be a B–valued
measure on R such that µ (F) = EB [Q(F)] for any Borel set F ⊆ R. If X is
bounded then its distribution can be alternatively described by the moment
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 11
formula ∫
R
xn dµ (x) = EB (Xn).
2.1.7. Symmetric group in the language of probability theory. Let A be a
ﬁnite set and let ∗ be an extra distinguished element such that ∗ /∈ A. In the
following, if not stated otherwise, we set A = {1, 2, . . . , q }. Group SA will
be regarded as a subgroup of SA ∪{∗}. In our case the role of the algebra A of
random variables will be played by some Abelian subalgebra o f C(SA ∪{∗})
and the role of the smaller algebraB will be played by the center ofC(SA ).
The conditional expectation EC(SA ) : C(SA ∪{∗}) → C(SA ) will be given by
the orthogonal projection, i.e.
EC(SA )(σ ) =
{
σ if σ ∈ SA 
0 if σ / ∈ SA 
=
{
σ if σ (∗) = ∗,
0 if σ (∗) ⁄= ∗.
In the rest of this article, when it does not lead to confusion s, instead of
EC(SA) we shall simply write E.
Suppose that some ﬁnite–dimensional representation ρ : SA → Mk(C)
is given. This allows us to deﬁne a scalar–valued expectatio n EC :
C(SA ∪{∗}) → C by
(2.4) EC(X) = 1
k Tr ρ
(
EC(SA)(X)
)
and to consider the distribution µ ρ of a random variable X ∈ C(SA ∪{∗})
with respect to this new expectation; in this new setupµ ρ is a usual (scalar–
valued) probability measure on R.
2.1.8. Jucys–Murphy element. Transition measure—the algebraic a p-
proach. The algebra P. In the group algebra C(SA ∪{∗}) we consider the
Jucys–Murphy element
J =
∑
a∈A 
(a∗),
where (ij) denotes the transposition exchangingi and j. We deﬁne moments
of the Jucys–Murphy element by
(2.5) MJM
k = E(Jk) =
∑
a1,...,a k∈A 
E[(a1∗) · · ·(ak∗)] ∈ C(SA ).
In Section 4.2.2 of we shall consider an extension of this concept.
For a given Young diagram λ ⊢ |A|we consider ρ = ρλ to be an irre-
ducible representation of SA corresponding to λ and consider the distribu-
tion µ λ := µ ρ λ
of the element J with respect to the expected value (2.4). We
call µ λ the transition measure of λ [VK85, Ker93, OV96, Bia98, Oko00].
12 PIOTR ´SNIADY
This deﬁnition is very algebraic and for this reason it will b e our favorite
deﬁnition of the transition measure.
We can treat the momentsMJM
k of the Jucys–Murphy element as elements
of the partial permutations algebra C(~SA ); in order to do this we treat every
non–zero summand on the right–hand side of (2.5) as a partial permuta-
tion with the support {a1, . . . , a k}. It is easy to check that for A ⊆ B the
morphism θB
A maps MJM
k ∈ C(~SB) to MJM
k ∈ C(~SA ) hence the projective
limit of the elements MJM
k ∈ C(~Sq ) exists and will be denoted by the same
symbol MJM
k ∈ C(~S∞).
We denote by P the algebra generated by elements MJM
k ∈ C(~S∞). It is
easy to check that P is commutative. Elements of P can be also regarded
as elements of C(~Sq ) and C(Sq ).
2.1.9. Gradation on P. Since we would like to study asymptotic proper-
ties of Young diagrams, we need to specify what kind of scalin g we are
interested in.
Let a sequence of Young diagrams (λN ) be given, λN ⊢ N. It is natural
to consider generalized Young diagrams which correspond togeometrically
scaled diagrams 1
√
N λN (observe that all such scaled diagrams have the same
area equal to 2). Suppose that the shape of the scaled diagrams converges
in some sense toward a generalized Young diagram λ. In many natural
topologies this implies the convergence of scaled moments of the transition
measure, cf (2.3)
lim
N →∞
1
Nk/2 EC(MJM
k ) = lim
N →∞
EC
[( 1
N1/2 J
) k]
=
lim
N →∞
1
Nk/2
∫
R
xkdµ λ N (x) =
∫
R
xkdµ λ(x).
In the study of asymptotic properties of some elements of the group alge-
bra C(SN ) we would like to group summands which have asymptotically
the same growth for large N and for this reason MJM
k can be treated as a
monomial in
√
N of degree k.
More formally, we consider a gradation on P by setting
(2.6) deg MJM
k = k.
In Corollary 4.8 we will show that MJM
2 , M JM
3 , · · · ∈ C(~S∞) are alge-
braically free and therefore this gradation is well deﬁned. This gradation
coincides with the weight gradation considered by Ivanov an d Olshanski
[IO02].
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 13
2.1.10. Normalized conjugacy class indicators. Let integer numbers
k1, . . . , k m ≥ 1 be given. We deﬁne the normalized conjugacy class in-
dicator Σ k1 ,...,k m ∈ C(SA ) as follows [KO94, Bia03]:
(2.7) Σ k1 ,...,k m =
∑
a
(a1,1 , a 1,2 , . . . , a 1,k 1) · · ·(am ,1, a m ,2, . . . , a m ,km),
where the sum runs over all one–to–one functions
a :
{
{r, s }: 1 ≤ r ≤ m, 1 ≤ s ≤ kr
}
→ A
and (a1,1 , a 1,2 , . . . , a 1,k 1) · · ·(am ,1, a m ,2, . . . , a m ,km ) is a product of dis-
joint cycles. Of course, if |A|< k 1 + · · ·+ km then the above sum runs over
an empty set and Σ k1 ,...,k m = 0. If any of the numbers k1, . . . , k m is equal
to 0 we set Σ k1 ,...,k m = 0.
In other words, let k ′
1 ≥ · · · ≥ k ′
m be the sequence k1, . . . , k m sorted
decreasingly; we consider a Young diagram (k ′
1, . . . , k ′
m ) and all ways of
ﬁlling it with the elements of the setA in such a way that no element appears
more than once. Each such a ﬁlling can be interpreted as a perm utation
when we treat rows of the Young tableau as disjoint cycles.
We can also treat Σ k1 ,...,k m as a an element of the partial permu-
tations algebra C(~SA ); in order to do this, we treat every summand
(a1,1 , a 1,2 , . . . , a 1,k 1) · · ·(am ,1, a m ,2, . . . , a m ,km) as a partial permutation
with support {aij : 1 ≤ i ≤ m, 1 ≤ j ≤ ki}. It is easy to check that for
A ⊆ B the morphism θB
A maps Σ k1 ,...,k m ∈ C(~SB) to Σ k1 ,...,k m ∈ C(~SA )
hence the projective limit of the elements Σ k1 ,...,k m ∈ C(~Sq ) exists and will
be denoted by the same symbol Σ k1 ,...,k m ∈ C(~S∞). It is easy to check that
elements Σ k1 ,...,k m ∈ C(~S∞) commute.
2.1.11. Filtration. We consider a ﬁltration on the commutative algebra
generated by Σ k1 ,...,k m ∈ C(~S∞) by setting
(2.8) deg Σ k1 ,...,k m = (k1 + 1) + (k2 + 1) + · · · + (km + 1).
It is easy to check that the elements from the family Σ k1 ,...,k m ∈ C(~S∞)
indexed by integer m ≥ 0 and k1 ≥ · · · ≥ km ≥ 1 are linearly independent
and therefore this deﬁnition makes sense but it is not clear that this formula
indeed deﬁnes a ﬁltration; we shall prove it in Corollary 3.8. The reason for
studying this ﬁltration is that—as we shall see in Theorem 4. 9—elements
MJM
k ∈ C(~S∞) and Σ k1 ,...,k m ∈ C(~S∞) generate the same commutative
algebra denoted by P and ﬁltration (2.8) is induced by the gradation (2.6).
