---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-010-42-stability-implies-negative-association
section_title: "Stability Implies Negative Association"
section_number: 4.2
pages: 24-29
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
---
of the following theorem goes back to Feder-Mihail [29] although the proof of the
full theorem is scattered over the literature [24, 57, 58, 72].
Theorem 4.8. Let S be a class of probability measures satisfying:
(1) Each µ ∈ S is a measure on 2E, where E is a ﬁnite subset of {1, 2, . . .}
depending on µ;
(2) S is closed under conditioning;
(3) For each µ ∈ S the variables Xe, e ∈ E, are pairwise negatively correlated;
(4) Each µ ∈ S has a homogeneous generating polynomial.
Then all measures in S are CNA (conditionally negatively associated).
The homogeneity condition in (4) above is essential and ensures the existence of
a variable of so-called “positive inﬂuence” [24] (various notions of “in ﬂuence” have
been studied by Bourgain et al in [14]).
A sketch of the proof of Theorem 4.8 is as follows. Recall from §2.1 the deﬁni-
tion of an increasing event. Since any increasing function depending on a set E0
can be written as a positive linear combination of characteristic func tions, χA, of
increasing events A depending on E0, it is enough to prove the theorem for such
characteristic functions. The proof of negative association in the case when F = χA
and G = Xe in Deﬁnition 2.7 are such that A does not depend on e is recovered
from Feder-Mihail’s proof [29, 58]. The general case – when F = χA1 and G = χA2
in Deﬁnition 2.7 are such that A1 and A2 depend on disjoint sets of variables –
then follows from the proof of [57, Theorem 6.5].
Using Theorem 4.8 we can establish the following result.
Theorem 4.9. If µ ∈ Pn is strongly Rayleigh then it is CNA +.
Proof. Let S be the class of all probability measures µ such that
• each µ ∈ S is a measure on 2 E, where E is a ﬁnite subset of {1, 2, . . .}
depending on µ, and
• µ has a stable homogeneous generating polynomial.
Since stable homogeneous polynomials are pairwise negatively correla ted and are
also closed under conditioning (cf. §2.1), the class S satisﬁes all the hypotheses
required in Theorem 4.8. Therefore, all the measures in S are negatively associated.
Let further ˆS be the class of all probability measures µ such that
• each µ ∈ ˆS is a measure on 2 E, where E is a ﬁnite subset of {1, 2, . . .}
depending on µ, and
• µ has a stable generating polynomial.
Now by Theorem 4.2 every measure in ˆS is the projection of a measure in S. Since
negative association is closed under projections and the strongly R ayleigh property
is closed under conditioning and external ﬁelds, the theorem follows . □
Note that since the Rayleigh/h-NLC+ property is also closed under c onditioning,
projections, and external ﬁelds, Theorem 4.8 and slight modiﬁcatio ns of the above
arguments actually yield the following stronger version of Theorem 4 .9.
Theorem 4.10. If µ ∈ Pn is PHR then it is CNA +.
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 25
Since homogeneous Rayleigh polynomials need not be stable, strongly Rayleigh
⇒ PHR strictly. As we will see in §7, one also has PHR ⇒ CNA+ strictly.
4.3. Stochastic Domination and T runcations. Recall the notion of stochastic
domination from Deﬁnition 2.14 in §2.5. It turns out that for strongly Rayleigh
measures, stochastic domination is intimately connected with centr al notions in
the theory of stable and real-rooted polynomials, namely the notion s of interlacing
zeros and proper position [7, 8, 9, 15, 50, 66]. In particular, this co nnection allows
us to extend one of Lyons’ main results [57] and to answer Pemantle ’s questions
on stochastic domination for truncations of “negatively dependen t” measures [65]
(cf. §2.5).
4.3.1. Partial Orders for Strongly Rayleigh Measures and Polynomi als. Let α1 ≤
α2 ≤ · · · ≤ αn and β1 ≤ β2 ≤ · · · ≤ βm be the zeros of two real-rooted polynomials
p, q ∈ R[z]. These zeros are interlacing if they can be ordered so that either α1 ≤
β1 ≤ α2 ≤ β2 ≤ · · · or β1 ≤ α1 ≤ β2 ≤ α2 ≤ · · · . If the zeros of p, q interlace
then the Wronskian W [p, q] := p′q − pq′ is either non-negative or non-positive on
the whole real axis R, see, e.g., [50, 66]. We say that p and q are in proper position,
denoted p ≪ q, if the zeros of p and q interlace and W [p, q] ≤ 0. For technical
reasons, we also say that the zeros of the polynomial 0 interlace th e zeros of any
(non-zero) real-rooted polynomial and write 0 ≪ p and p ≪ 0.
The following theorem proved in [9] provides a notion of proper positio n for
multivariate polynomials.
Theorem 4.11. Let f, g ∈ R[z1, . . . , zn]. The following are equivalent:
(1) The polynomial g + if ∈ C[z1, . . . , zn] is stable;
(2) The polynomial g + zn+1f ∈ R[z1, . . . , zn, zn+1] is real stable;
(3) For all λ ∈ Rn
+ and µ ∈ Rn we have
f (λt + µ) ≪ g(λt + µ),
where f (λt + µ) = f (λ1t + µ1, . . . , λnt + µn), t ∈ C.
We say that the polynomials f, g ∈ R[z1, . . . , zn] are in proper position, written
f ≪ g, if any of the equivalent conditions in Theorem 4.11 are satisﬁed.
Remark 4.1. The typical proper position is between a real stable polynomial and
any of its partial derivatives: if f ∈ R[z1, . . . , zn] is real stable then ∂jf ≪ f
for all j ∈ [n]. If f ≪ g and α is a real number then either f (α, z2, . . . , zn) ≪
g(α, z2, . . . , zn) or f (α, z2, . . . , zn) = g(α, z2, . . . , zn) ≡ 0, see [9]. Note also that by
Theorem 4.11 (3) one has f ≪ g ⇔ αf ≪ βg for any α, β ∈ R+.
We deﬁne a partial order ✂ on the set of strongly Rayleigh probability measures
on 2 [n] as follows.
Deﬁnition 4.1. Let SR n be the set of strongly Rayleigh probability measures on
2[n]. First, deﬁne a (preliminary) partial order ✂′ on SR n by setting µ ✂′ ν if there
exists a sequence of strongly Rayleigh probability measures µ = µ0, µ1, . . . , µℓ = ν
such that gµ0 ≪ gµ1 ≪ · · · ≪ gµℓ. Then deﬁne the partial order ✂ on SRn as the
closure of ✂′, i.e., set µ ✂ ν if there are two sequences {µj}∞
j=0, {νj}∞
j=0 ⊂ SR n such
that
lim
j→∞
µj = µ, lim
j→∞
νj = ν, and µj ✂′ νj for all j ∈ N
26 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
(as the measures are deﬁned on 2 [n] it does not matter what notion of limit we use).
We will also consider ✂ to be a partial order on the set of generating polynomials
of strongly Rayleigh measures and write gµ ✂ gν whenever µ ✂ ν.
Remark 4.2. It seems likely that the partial orders ✂′ and ✂ on SR n deﬁned above
are actually the same. However, since it is irrelevant for the presen t purposes we
do not further pursue this issue here.
As we noted in §2.5, the stochastic domination relation ≼ deﬁnes a partial order
on Pn (cf. [61]). The anti-symmetry of ✂ follows from our next result.
Proposition 4.12. Let µ and ν be strongly Rayleigh probability measures on 2[n].
Then µ ✂ ν =⇒ µ ≼ ν.
Proof. Clearly, we may assume that gµ ≪ gν, so that by Theorem 4.11 the polyno-
mial in n + 1 variables G = (gν + zn+1gµ)/2 is stable. Let γ ∈ Pn+1 be the measure
with generating polynomial G. By Theorem 4.9, γ is NA. Let A be an increasing
event not depending on the last coordinate and set B = {S ∈ 2[n+1] : n + 1 ∈ S}.
Then
1
2 µ(A) = γ(A ∩ B) ≤ γ(A)γ(B) =
(1
2 µ(A) + 1
2 ν(A)
) 1
2 ,
which gives µ(A) ≤ ν(A). □
Recall that the standard partial order on the set of all Hermitian n × n matrices
– often referred to as the Loewner order [61] – is induced by the cone of all positive
semi-deﬁnite n × n matrices: A ≤ B (respectively, A < B ) means that B − A is
positive semi-deﬁnite (respectively, positive deﬁnite). Using our dis cussion so far
and the arguments further below, we can prove the following exten sion of one of
the main results in [57]:
Theorem 4.13. Let A and B be positive contractions such that A ≤ B and let µ
and ν be their corresponding determinantal measures. Then µ ✂ ν and thus µ ≼ ν.
In [57, Theorem 8.1] Lyons proved the last statement ( µ ≼ ν) in Theorem 4.13
under the additional hypothesis [ A, B] = 0.
We will need the following elementary lemma.
Lemma 4.14. If A, B are positive semi-deﬁnite n×n matrices such that A ≤ B < I
then A(I − A)−1 ≤ B(I − B)−1.
Proof. By a standard density argument it is enough to prove the lemma for p ositive
deﬁnite matrices. Note ﬁrst that if C is a positive deﬁnite n × n matrix such that
C ≤ I then C−1 ≥ I. Moreover, if D is a positive deﬁnite n × n matrix such that
C ≤ D then M ∗CM ≤ M ∗DM for any n × n matrix M since
⟨M ∗CM u, u⟩ = ⟨CM u, M u⟩ ≤ ⟨DM u, M u⟩ = ⟨M ∗DM u, u⟩
for any u ∈ Cn. The latter property with M = D−1/2 yields D−1/2CD −1/2 ≤ I,
then by taking inverses and using the ﬁrst property we get D1/2C−1D1/2 ≥ I, and
ﬁnally by using again the second property with M = D−1/2 we obtain C−1 ≥ D−1.
Therefore, if A, B are positive deﬁnite matrices as in the lemma it follows that
I − A−1 ≤ I − B−1, hence
A(I − A)−1 = −
(
I − A−1)−1
≤ −
(
I − B−1)−1
= B(I − B)−1,
which is the desired conclusion. □
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 27
Proposition 4.15. Let A and B be positive semi-deﬁnite n × n matrices such that
A ≤ B and set Z = diag(z1, . . . , zn). Then
det(I + AZ)
det(I + A) ✂ det(I + BZ )
det(I + B) and det(B + Z)
det(B + I) ✂ det(A + Z)
det(A + I) .
Moreover, if A and B are positive contractions, then
det(I − A + AZ) ✂ det(I − B + BZ ).
Proof. We just prove the ﬁrst inequality. The second inequality then follows upon
considering the operation
det(I + M Z) := fM (z1, . . . , zn) ↦→z1 · · ·znfM (z−1
1 , . . . , z−1
n )
with M = A and M = B, respectively, which preserves the set of stable polynomials
with non-negative coeﬃcients (Proposition 3.1) and obviously rever ses the partial
order ✂ (Theorem 4.11). Similarly, for the third inequality note that if A ≤ B and
A, B are positive contractions then by continuity we may assume that B < I . But
then A′ = A(I − A)−1 ≤ B(I − B)−1 = B′ by Lemma 4.14, hence
det(I − A + AZ) = det(I + A′Z)
det(I + A′) ✂ det(I + B′Z)
det(I + B′) = det(I − B + BZ ).
We claim that the polynomial f ∈ R[z1, . . . , zn, y] deﬁned by
f (z, y) = det( y(I + AZ) + I + BZ ) := ynP0(z) + yn−1P1(z) + · · · + Pn(z),
where z = (z1, . . . , zn), is real stable with non-negative coeﬃcients. Assuming this
claim we see that since Pk(z) = ( n − k)!−1∂n−kf /∂yn−k⏐⏐
y=0, by Remark 4.1 we
have that
det(I + AZ) = P0 ≪ P1 ≪ · · · ≪ Pn = det(I + BZ ),
which then settles the lemma (note that Pk(0) =
(n
k
)
, so none of the Pk’s is iden-
tically zero). To prove the remaining claim, note that the polynomial G(z, y) =
det(A + y(B − A) + Z) is stable with non-negative coeﬃcients by Proposition 3.2.
Hence, so are the polynomials
F (z, y) = z1 · · · znynG(z−1
1 , . . . , z−1
n , y−1) = det( y(I + AZ) + (B − A)Z)
and F (z, y + 1) = det( y(I + AZ) + I + BZ ) = f (z, y). □
Proof of Theorem 4.13. The generating polynomials of µ and ν are det(I −A+AZ)
and det( I − B + BZ ), respectively. Combine Propositions 4.12 and 4.15. □
We end this section with an open question, namely whether the followin g con-
verse to Proposition 4.15 holds.
Question 4.1. Let A and B be positive semi-deﬁnite n × n matrices such that
det(I + AZ)
det(I + A) ✂ det(I + BZ )
det(I + B) , or equivalently, det(B + Z)
det(B + I) ✂ det(A + Z)
det(A + I) ,
where Z = diag(z1, . . . , zn). Is it true that A ≤ B?
Note that an aﬃrmative answer to Question 4.1 would give a characte rization of
the Loewner order on the cone of all positive semi-deﬁnite n × n matrices in terms
of determinantal stable polynomials.
28 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
Remark 4.3. Stochastic domination is closely related to the notion of majorization
(or spectral order) for real vectors that was axiomatized by Ha rdy-Littlewood-P´ olya
and Schur [38, 61]. The latter also induces a partial order (though n ot the same as
the proper position) on univariate real-rooted polynomials, see, e.g ., [6].
4.3.2. Truncations of Strongly Rayleigh Measures and Polynomials . We will now
discuss certain truncations of stable polynomials and strongly Rayle igh measures.
Lemma 4.16. Suppose that f (z) =∑
α∈Nn a(α)zα ∈ R[z1, . . . , zn] is stable of total
degree at most d and has non-negative coeﬃcients. For 0 ≤ k ≤ d let
Ek(z) =
∑
|α|=k
a(α)zα.
If 0 ≤ p ≤ q ≤ d, then
q∑
k=p
(q − p
k − p
)Ek(z)(d
k
) yq−k (12)
is a stable polynomial in the variables z1, . . . , zn, y.
Proof. Deﬁne a sequence of polynomials in R[z1, . . . , zn, y] as follows:
f1(z, y) =
∑
a(α)zαyd−|α| =
d∑
k=0
Ek(z)yd−k,
f2(z, y) = ∂d−qf1/∂y d−q,
f3(z, y) = yqzd
1 · · · zd
nf2(z−1
1 , . . . , z−1
n , y−1),
f4(z, y) = ∂pf3/∂y p,
f5(z, y) = yq−pzd
1 · · · zd
nf4(z−1
1 , . . . , z−1
n , y−1).
By Theorem 4.5, f1 is a stable polynomial, and by the closure properties of stable
polynomials (Proposition 3.1) we also have that f2, . . . , f5 are stable. The polyno-
mial f5 is a constant multiple of (12). □
The above lemma gives the following generalization of Newton’s inequalit ies,
which correspond to the special case when f (z) = (1 + z1) · · ·(1 + zn).
Corollary 4.17. Let f (z) and Ek(z), k = 0 , . . . , d, be as in the statement of
Lemma 4.16. Then
E2
k(z)
(d
k
)2 ≥ Ek−1(z)( d
k−1
) Ek+1(z)( d
k+1
) , z ∈ Rn, 1 ≤ k ≤ d − 1. (13)
Proof. By Lemma 4.16, the polynomial
(z, y) ↦→Ek−1(z)( d
k−1
) y2 + 2 Ek(z)(d
k
) y + Ek+1(z)( d
k+1
) (14)
is stable. Hence, for any ﬁxed z ∈ Rn the resulting (univariate) polynomial in y is
real-rooted. The corollary follows upon taking the discriminant in (14 ). □
Recall from Deﬁnition 2.15 the truncation µp,q of a measure µ to [ p, q]. It has
been discussed whether truncations of measures preserve nega tive dependence prop-
erties, cf. [45, 65] and references therein. As we show in Corollary 4.18 below, this is
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 29
the case for strongly Rayleigh measures and truncations of length q − p ≤ 1. Trun-
cations of length q − p ≥ 2 do not preserve the strong Rayleigh property. However,
the weighted truncation suggested by (12) obviously does.
Corollary 4.18. Suppose that µ is a strongly Rayleigh probability measure on 2[n]
and that 0 ≤ p ≤ q ≤ n with q − p ≤ 1. Then µp,q is strongly Rayleigh.
Proof. We prove the corollary for q − p = 1. Let f be the generating polynomial of
µ and let Ek be as in the statement of Lemma 4.16. Then the polynomial
g(z, y) = Ep(z)(n
p
) y + Eq(z)(n
q
) (15)
is stable. Clearly, the generating polynomial of µp,q is a (positive) constant multiple
of g(z, q/(n − p)). The corollary follows since stable polynomials are closed under
setting variables equal to real numbers, see Proposition 3.1. □
In §7 we show that Pemantle’s Conjecture 2.9 (see §2.5) fails in its full generality.
However, it is true for strongly Rayleigh measures:
Theorem 4.19. Let µ be a strongly Rayleigh probability measure on 2[n], and let
1 ≤ k ≤ n. If µ({S : |S| = k − 1})µ({S : |S| = k}) ⁄= 0, then µk−1 ≼ µk.
Proof. Let f be the generating polynomial of µ and let Ek be as in the statement
of Lemma 4.16. By assumption one has Ek−1(1)Ek(1) ⁄= 0, where 1 ∈ Rn
+ is as
before the “all ones vector”. From Lemma 4.16 and the last part of Remark 4.1 we
deduce that the polynomial
F (z1, . . . , zn+1) = zn+1
Ek−1(z1, . . . , zn)
Ek−1(1) + Ek(z1, . . . , zn)
Ek(1)
is stable. Since the above quotients are the generating polynomials o f µk−1 and µk,
respectively, we have µk−1 ✂ µk by Theorem 4.11 and Deﬁnition 4.1. The desired
conclusion follows from Proposition 4.12. □
