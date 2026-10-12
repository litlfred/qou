---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-123-2b-rational-points-on-twisted-hurwitz-spaces-ove
section_title: "2B. Rational points on twisted Hurwitz spaces over finite fields"
section_number: null
pages: 232-238
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
result about the average size of the subspace of Jac(C)[ℓ](Fq) on which Frobenius acts by some speciﬁed
scalar a, as C ranges over hyperelliptic curves over Fq. More precisely, we study the variation as we range
over y2 = f (x) with f ranging over squarefree polynomials in Fq[x]; this amounts to the same, since each
isomorphism class of hyperelliptic curves is represented in this form the same number of times (assuming,
of course, that the isomorphism classes are weighted inversely to the number of automorphisms they
possess.)
Proposition 2.1. Let a ∈(Z/ℓZ)×. With notation as in Section 2A, there exist constants Cℓ, Nℓ, Qℓonly
depending on ℓsuch that

P
f ∈Qn,q ma( f )
|Qn,q|
−1

 ≤Cℓq−1/2
for all n ≥Nℓand q ≥Qℓ.
Remark 2.2. While this paper was in proof, we learned that Proposition 2.1 follows from the proof of
Theorem 1.1 of [Lipnowski and Tsimerman 2019], which is in fact more general, and the arguments used
are essentially the same as those here. We have left the proof of Proposition 2.1 in the present paper
Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds
1899
because the form in which we present the proof here is conducive to proving the explicit bounds for
the stable range obtained in Proposition 2.7 below. It would be interesting to address the questions of
explicit bounds for the stable range in the more general situations considered by [loc. cit.], where the
group-theoretic part of the proof of Proposition 2.7 would presumably be more complicated.
When a = 1 and n is odd, Proposition 2.1 is essentially Theorem 8.8 of [Ellenberg et al. 2016], and
indeed the proof here is a modiﬁcation of the proof of that theorem.
The reader may note that [Ellenberg et al. 2016, Theorem 8.8] requires not only that q is not a multiple
of ℓbut that q is not congruent to 1 modulo ℓ. We face no such restriction here. That’s because [loc. cit.,
Theorem 8.8] computes arbitrary moments of the Cohen–Lenstra distribution, whereas we are only
studying the analogue of the average size of the ℓ-part of the class group. In the language of [loc. cit.,
Theorem 8.8], we are only considering the case A = Z/ℓZ. The difference is as follows. In the proof, we
will end up estimating the number of Fq-points on a moduli space over Fp, and the result will depend
on that space having just one geometrically irreducible component deﬁned over Fq. In the more general
setting treated in [loc. cit., Theorem 8.8], that space has many geometric components, all but one of which
have ﬁelds of deﬁnition containing µℓ; so when q is congruent to 1 mod ℓthere are multiple Fq-rational
components. In the case treated here, the moduli space in question is geometrically irreducible, so this
issue does not arise.
Proof. We begin by observing that P
f ∈Qn,q ma( f ) can be interpreted as the number of Fq-rational points
of a certain moduli space.
To this end we brieﬂy recall the setup of [Ellenberg et al. 2016, Section 7].
Let k be a ﬁeld, let G be a ﬁnite group with trivial center, denote by e the identity element of G, and
let c be a conjugacy-closed subset of G\e. By a tame G-cover of P1 with monodromy type c we mean a
triple (X, f, φ) where
• X is a smooth proper geometrically connected curve X/k;
• f : X →P1 is a tamely ramiﬁed ﬁnite cover;
• The image of tame inertia at each branch point of f excepting ∞lies in c;
• f is Galois with group G; that is, Aut( f ) acts transitively on the geometric ﬁbers of f and φ is an
automorphism from G to Aut( f ).
Here by an isomorphism between two covers f : X →P1 and f ′ : X′ →P1 we mean a morphism
ψ : X →X
′ with f ′ ◦ψ = f , not a pair (ψ, ι) with ι a nontrivial automorphism of P1 and f ′ ◦ψ = ι ◦f .
In other words, our P1 is “labeled”.
Then, as in [Ellenberg et al. 2016, Section 7] (more or less immediate from a theorem of Romagny and
Wewers [2006]), there is a scheme Hnc
G,n over Z[1/|G|] whose k-points (as long as k has characteristic
prime to |G|) are in bijection with the isomorphism classes of tame G-covers of P1 which have n branch
1900
Jordan S. Ellenberg, Wanlin Li and Mark Shusterman
points on A1 with monodromy type c. (We do not specify whether or how the cover is branched at ∞.)2
In fact [Romagny and Wewers 2006, Theorem 2.1], for a scheme S, the set Hnc
G,n(S) corresponds to
isomorphism classes of tame G-covers over S, suitably deﬁned; we will not need to spell out that deﬁnition
here. Once the n branch points are chosen on A1 there are ﬁnitely many choices for f and φ. Thus the
dimension of Hnc
G,n equals to n.
From now on, we suppose that k is Fq, that G is the dihedral group Z/ℓZ ⋊Z/2Z, and that c is the
conjugacy class of an involution in G. We will now explain the relationship between the space of G-covers
and the ℓ-torsion in the Jacobian of hyperelliptic curves. The key point is that, for any algebraic curve C,
the set of surjections Jac(C)[ℓ] →(Z/ℓZ)k is naturally identiﬁed with the set of étale (Z/ℓZ)k covers
of C. For details, see Section 3.9 of [Milne 2008].
If f : X →P1 is a G-cover, the product structure of G allows us to factor f as
X
g
−→C
h
−→P1
where h is a hyperelliptic cover and g is a Galois cover with group Z/ℓZ; that is, g is endowed with an
isomorphism φ : Z/ℓZ →Aut(g). What’s more, the fact that the monodromy in f is of type c implies
that g is an étale cover, at least away from the points of C over ∞∈P1.
What happens over ∞is slightly more delicate. The double cover h is branched at n points on A1, but
the total number of branch points of h must be even as C is a smooth proper hyperelliptic curve. Thus, if
n is odd, h is branched at ∞. The monodromy around ∞in the cover X →P1 is thus an element of G
projecting to the nontrivial element of Z/2Z. Such an element must be an involution, and it follows that
g is unramiﬁed at ∞. If n is even, on the other hand, it is possible for g to be ramiﬁed. We thus wish to
restrict our attention to those G-covers X →C which are unramiﬁed over ∞. These are parametrized by
a closed and open subscheme of Hnc
G,n (indeed, it is the second term in the disjoint union in the paragraph
following (7.3.1) of [Ellenberg et al. 2016]). Let Xn be this subscheme of Hnc
G,n when n is even, and
Hnc
G,n when n is odd. In both cases, dim Xn = n. We have explained how every point of Xn(k) gives rise
to a triple (g, φ, h)/k up to isomorphism, and in fact it is not hard to check that the converse holds as
well. (This is essentially the last paragraph of the proof of [Ellenberg et al. 2016, Proposition 8.7].)
If a is an element of (Z/ℓZ)∗, we denote by ⟨a⟩the automorphism of Xn which sends (g, φ, h) to
(g, aφ, h). We then write Xa
n for the twist of Xn by the homomorphism
Gal(Fq/Fq) →Aut(Xn)
which sends Frobq to a [Poonen 2017, Section 4.5].
Lemma 2.3. With notation as in Section 2A,
X
f ∈Qn,q
ma( f ) = (q −1)|Xa
n(Fq)|.
2The somewhat artiﬁcial special treatment of ∞in this deﬁnition, as in [Ellenberg et al. 2016], stems from the need to
compare with topology, where branched covers of the disc are technically easier to handle than branched covers of the sphere.
Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds
1901
Proof. A point of Xa
n(Fq) is a point of Xn(Fq) such that Frobq ·x = ⟨a⟩· x. In other words, it is a triple
(g, φ, h)/Fq such that Frobq ·(g, φ, h) is isomorphic to (g, aφ, h). The fact that the isomorphism class
of h is ﬁxed by Frobenius implies that the branch locus of h is an Fq-rational divisor. Let f (x) ∈Fq[x]
be the unique monic squarefree polynomial which vanishes precisely at the branch locus of h. Then C is
isomorphic (over Fq) to the smooth completion of the hyperelliptic curve deﬁned by y2 = f (x).
Fixing such an h, and thus such a C, we now consider the set of points of Xa
n(Fq) lying over this h.
First of all, the choices of (g, φ) such that (g, φ, h) ∈Xa
n(Fq) = Xn(Fq) for a speciﬁed h are in bijection
with the ℓ2g(C) −1 surjections from J(C)[ℓ](Fq) to Z/ℓZ. Two such surjections s, s′ are isomorphic (that
is, are parametrized by the same point of Xa
n(Fq)) if and only if s = ±s′. The action of Frobenius on the
set of surjections sends s to a−1 Frobq s; so s descends to a point of Xa
n(Fq) if and only if Frobq ·s = ±as.
We conclude that the number of points of Xa
n(Fq) lying over h is
  1
2

(ma( f ) + m−a( f )).
Now if f in Qn,q is not monic then f = ϵF for some ϵ ∈F∗
q and some monic F. The curve C f
is isomorphic to CF if ϵ is a quadratic residue and to the nontrivial quadratic twist of CF otherwise.
In the former case, ma( f ) = ma(F), and in the latter, ma( f ) = m−a(F). In particular, the quantity
  1
2

(ma( f ) + m−a( f )) is the same for all q −1 nonzero multiples of F. We conclude that
X
f ∈Qn,q
  1
2

(ma( f ) + m−a( f )) = (q −1)|Xa
n(Fq)|.
Moreover, taking ϵ to be a nonresidue in F∗
q,
X
f ∈Qn,q
ma( f ) =
X
f ∈Qn,q
ma(ϵ f ) =
X
f ∈Qn,q
m−a( f )
from which we obtain
X
f ∈Qn,q
ma( f ) = (q −1)|Xa
n(Fq)|
as desired.
□
We now argue exactly as in the proof of [Ellenberg et al. 2016, Theorem 8.8].
Since |Qn,q| = (q −1)(qn −qn−1), it sufﬁces to prove that
|q−n|Xa
n(Fq)| −1| ≤Cℓq−1/2
(2.4)
for some Cℓdepending only on ℓand for all n > Nℓ, q > Qℓ.
Via the Grothendieck–Lefschetz trace formula, we have
|Xa
n(Fq)| =
X
i
(−1)i Tr(Frobq | Hi
c,ét((Xa
n)Fq; Qλ).
(2.5)
where λ is a prime greater than max{2ℓ, q, n}.
Note that the étale cohomology is that of the base change of Xa
n to Fq, where it becomes isomorphic
to the untwisted space Xn; in particular, the choice of a affects the action of Frobenius on the étale
cohomology, but not the étale Betti numbers, bounds on which are the main engine of the argument.
1902
Jordan S. Ellenberg, Wanlin Li and Mark Shusterman
We begin by computing the main term:
Tr(Frobq | H2n
c,ét((Xa
n)Fq; Qλ) = qn.
This follows immediately from the fact that (Xa
n)Fq ∼= (Xn)Fq is irreducible. When n is odd, this is shown
in the proof of [Ellenberg et al. 2016, Theorem 8.8] as a consequence of a big monodromy theorem
of J.K. Yu. (This is actually the only place where we need n to be large, and indeed n = 3 would be
enough.) When n is even, we argue as follows. The map from Xn to the conﬁguration space Confn A1
sending a G-cover to its branch locus is a ﬁnite cover [loc. cit., Section 2.2], and irreducibility of Xn is
equivalent to the monodromy group of this cover acting transitively on the ﬁber. It sufﬁces to check that
this holds on a closed subvariety of the base. So write Z for the subvariety of Confn A1 consisting of
those conﬁgurations containing some speciﬁed point p0 ∈P1(Fq), and let Y be the preimage of Z in Xn.
An automorphism of P1 taking p0 to ∞now identiﬁes Y with Hnc
G,n−1, which we know to be irreducible
since n −1 is odd. This implies that Xn is irreducible.
We now turn to the error term. The moduli space Xn is a closed and open subscheme of Hnc
G,n, so its
Betti numbers are bounded by those of Hnc
G,n; by [loc. cit., (7.8.1)] we have
dim H2n−i
c,ét ((Xa
n)Fq; Qλ) ≤Kℓ(Bℓ)i
where Kℓ, Bℓare constants depending only on ℓ.
Using the Deligne bound [1980], the eigenvalue of Frobenius on Hi
c,ét((Xa
n)Fq; Qλ) is bounded in
absolute value by qi/2; so the absolute value of the contribution of all i < 2n to (2.5) is bounded above by
the sum of a geometric series which converges for all q > B2
ℓ. In particular, as in [Ellenberg et al. 2016,
Section 1.8], this contribution is at most
KℓBℓq−1/2(1 −Bℓq−1/2)−1qn.
So if we take Qℓ= 4B2
ℓand q > Qℓ, we may take Cℓ= 2KℓBℓand conclude
|Xa
n(Fq) −qn| =

2n−1
X
i=0
(−1)i Tr(Frobq | Hi
c,ét((Xa
n)Fq; Qλ)

 < Cℓqn−1/2
which proves (2.4) and thus the desired result.
□
Proposition 2.1 allows us to bound the proportion of hyperelliptic curves whose étale cohomology has
a Frobenius eigenvalue congruent to a mod ℓ. Recall from Section 2A that Qa,ℓ
n,q is the set of squarefree
polynomials over Fq of degree n such that ma( f ) is greater than 0.
Corollary 2.6. There are constants C′
ℓ, Qℓ, Nℓsuch that for any a ∈(Z/ℓZ)× we have
|Qa,ℓ
n,q|
|Qn,q| ≤
1
ℓ−1 + C′
ℓq−1/2
for all n ≥Nℓ, q ≥Qℓ.
Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds
1903
Proof. Write δ for the quantity |Qn,q|−1|Qa,ℓ
n,q| to be bounded.
Since ma( f ) is the number of nonzero elements of a vector space over Z/ℓZ, it is at least ℓ−1 if it is
greater than 0. In particular,
|Qn,q|−1 X
f ∈Qn,q
ma( f ) ≥|Qn,q|−1(ℓ−1)|Qa,ℓ
n,q| = (ℓ−1)δ
By Proposition 2.1, we now have
(ℓ−1)δ < 1 + Cℓq−1/2
for all sufﬁciently large n, q, which yields the desired result by taking C′
ℓ= Cℓ/(ℓ−1).
□
So far, we have used the results of [Ellenberg et al. 2016] as they appear in that paper. However, for
the present application, it is useful to compute explicit values Cℓ, Qℓfor which Corollary 2.6 holds. We
do so by going back to the main body of [loc. cit.] and working out explicit bounds for quantities that are
given in [loc. cit., (7.8.1)] only as unspeciﬁed constants.
Proposition 2.7. Corollary 2.6 holds with C′
ℓ= 2(ℓ−1)−1(4ℓ)138 and Qℓ= 4 · (4ℓ)156.
Proof. By the proof of Corollary 2.6, we may take C′
ℓto be Cℓ/(ℓ−1), where Cℓis the constant appearing
in the statement of Proposition 2.1. Moreover, we may take Cℓto be 2KℓBℓand Qℓto be 4B2
ℓ, where
Bℓ, Kℓare the constants appearing in the proof of Proposition 2.1 controlling the exponential growth of
the Betti numbers of the relevant Hurwitz space. We now explain how to bound Bℓexplicitly.
In [Ellenberg et al. 2016, 7.8.1], the bound
dim Hi
ét((Xa
n)Fq; Qλ) ≤Kℓ(Bℓ)i
arises from two facts. First, there is a stability theorem [loc. cit., 6.2], which tells us in this context that
dim Hi
ét((Xa
n)Fq; Qλ) = dim Hi
ét((Xa
n+D)Fq; Qλ)
(2.8)
for all n > Ai + B, where A, B, and D are constants we shall specify. Second, there is an absolute bound
[loc. cit., 2.5] which tells us that
dim Hi
ét((Xa
n)Fq; Qλ) ≤(4ℓ)n.
These two facts together imply that
dim Hi
ét((Xa
n)Fq; Qλ) ≤(4ℓ)Ai+B+D
so we may take Bℓ= (4ℓ)A and Kℓ= (4ℓ)B+D. It remains to compute A, B, and D.
The key object of computation is the ring R deﬁned in [Ellenberg et al. 2016, Section 3]. This ring is
deﬁned for any ﬁnite group G and any conjugacy-closed subset of G; we will consider here just the case
relevant to us, which is that where G is the dihedral group of order 2ℓand c is the class of involutions
in G. The set of n-tuples of involutions (τ1, . . . , τn) ∈Gn carries a natural action of the n-strand braid
1904
Jordan S. Ellenberg, Wanlin Li and Mark Shusterman
group; the ring R is a graded Q-algebra whose degree-n part is spanned by the set of orbits of that action,
which set we denote 6n. The multiplication in R is given by concatenation of n-tuples.
The key fact about R is that it contains a central element U with the property that R[U] and R/U R
both have ﬁnite degree (that is, they are supported in only ﬁnitely many grades.) In the dihedral case, R
and U are particularly easy to describe. For any n, there is map from 6n to G sending (τ1, . . . , τn) to the
product τ1 · · · τn, which is called the boundary monodromy. Each n-tuple in 6n also has a monodromy
group; namely, the group generated by τ1, . . . , τn. The possible monodromy groups are just the order-2
subgroups of G and G itself. It is not hard to check that, for all n ≥4, the elements of 6n are determined by
their boundary monodromy and their monodromy group; to be precise, 6n consists of ℓorbits consisting
of the single element (τ, τ, . . . , τ) as τ ranges over the ℓinvolutions, and ℓmore orbits, each of which
consists of all n-tuples with monodromy group G and boundary monodromy g, as g ranges over the
index-2 cyclic subgroup of G (when n is even) or its nontrivial coset (when n is odd.) In particular,
dim Rn = 2ℓfor all n ≥4. We may take U to be the degree-2 central operator
U =
X
τ∈c
(τ, τ)
and check that U induces an isomorphism from Rn to Rn+2 for all n ≥4. In particular, deg R[U] and
deg R/U R are both at most 4, where by the degree of a graded ring we mean the highest grade represented
in its support.
This combinatorial information about the dihedral group is what goes into the computation of constants
in [Ellenberg et al. 2016]. The constant D in [loc. cit., 6.1] is just the degree of U, which is 2. The stability
result in [loc. cit., 6.1] is derived from a general theorem [loc. cit., 4.2] about R-modules. The R-module
M governing the Hi of Hurwitz space, to which we apply [loc. cit., 4.2] is the one called Mi in [loc. cit.,
6.1]. So (using the constants appearing in those theorems) stability begins when n = max(h0, h1) + A0,
where h j is the quantity denoted deg Hj(K(Mi) in [loc. cit., 6.1]. In turn, as asserted in the ﬁrst paragraph
of the proof of [loc. cit., 6.1], we have
deg Hj(K(Mi)) ≤A2 + A0(3i + j).
So we ﬁnd that (2.8) holds for all n ≤A2 + A0(3i + 1) + A0 = 3A0i + (2A0 + A2). In other words, we
may take A = 3A0 and B = 2A0 + A2.
Finally, the values of A0 and A2 are given in [Ellenberg et al. 2016, 4.5.3]. They are deﬁned in
terms of A(R) = max(deg R[U], deg R/U R), which for us is 4. Now A0 = 6A(R) + deg U = 26 and
A2 = A(R) + deg U = 6. Thus, A = 78 and B = 58. Since D = 2, we conclude that we may take
Bℓ= (4ℓ)78 and Kℓ= (4ℓ)60. So we have Qℓ= 4 · (4ℓ)156 and C′
ℓ= 2(ℓ−1)−1(4ℓ)138, as claimed. □
