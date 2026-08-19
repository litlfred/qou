---
doc_id: arxiv-0707.3682v2
doc_title: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS"
section_id: sec-002-7-examples
section_title: "Examples"
section_number: 7
pages: 29-34
source_pdf: 0707.3682v2.pdf
source_sha256: 609a6f67a0cd5fc8
doc_brief: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS — We formulate a conjectural p-adic analogue of Borel’s theorem re- lating regulators for higher K-groups of number ﬁelds to special values of the"
---
ducible 2-dimensional representations Wa witha ⁄= 1 of S3 × Z/3Z in Example 5.7,
as the L-functions of Abelian characters over quadratic ﬁelds. For later u se we also
note how to write some of them in terms of ζ-functions of certain ﬁelds.
We take the ﬁeld of coeﬃcients E to be C in the remainder of this section, and
denote the trivial 1-dimensional representation of any group G by 1G.
Example 6.5. Let AltS3 be the 1-dimensional representation of S3 through the
sign character, and V the irreducible 2-dimensional representation. Since
IndS3
A3 ◦ IndA3
{e}(1{e}) ∼
= IndS3
{e}(1{e}) ∼
= 1S3 ⊕ AltS3 ⊕V 2
and IndS3
A3(1A3) ∼
= 1S3 ⊕AltS3 it follows that IndS3
A3(V ′) ∼
=V for either non-trivial 1-
dimensional representation V ′ ofA3. Applying this to the situation of Example 5.3
we see that L(s,V, Q) = L(s,V ′,q ). Similarly, if H is any subgroup of S3 of
30AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
order 2, then Ind S3
H (1H) ∼
= 1S3 ⊕V . In the situation of Example 5.3 this means
thatζc(s) = ζQ(s)L(s,V, Q).
Example 6.6. If D8 is as in Example 5.5, Va,b for a,b = ±1 the 1-dimensional
representation of D8 where σ acts as multiplication by a and τ by b, and V the
irreducible 2-dimensional representation, then for any subgroup H
IndD8
H ◦ IndH
{e}(1{e}) ∼
= (⊕a,b=±1Va,b) ⊕V 2.
If we takeH = ⟨τ,σ 2⟩ then IndH
{e}(1{e}) ∼
= ⊕a,b=±1Wa,b withWa,b the 1-dimensional
representation of H where σ2 acts as multiplication by a and τ by b. Because
IndD8
H (W1,b) ∼
= ⊕a=±1Va,b we have Ind D8
H (W−1,1) ∼
= IndD8
H (W−1,−1) ∼
= V , so with
notation as in Figure 5.1 we get L(s,V, Q) = L(s,W −1,1,q 1) = L(s,W −1,−1,q 1).
Similarly, IndD8
⟨τ ⟩(1⟨τ ⟩) ∼
= (⊕a=±1Va,1) ⊕V so that ζk1 (s) = ζq1 (s)L(s,V, Q) as
well.
Remark 6.7. If H = ⟨σ⟩ in Example 6.6 then Ind H
{e}(1{e}) ∼
= ⊕4
m=1Uim with Ua
the 1-dimensional representation of ⟨σ⟩ where σ acts as multiplication by a. Now
IndD8
H (Ua) ∼
=Va,1 ⊕Va,−1 when a = ±1 so that Ind D8
H (Ua) ∼
=V when a ⁄= ±1, and
in Example 5.5 we also have L(s,V, Q) = L(s,Ui,q 2) = L(s,U −i,q 2).
Example 6.8. If G =S3 × Z/3Z and H =A3 × Z/3Z then
IndG
H ◦ IndH
{(e,0)}(1{(e,0)}) ∼
=W ⊕W 2
1 ⊕W 2
ζ3 ⊕W 2
ζ2
3
withW the direct sum of the 1-dimensional representations of G and the Wa as in
Example 5.7. Write Ind H
{(e,0)}(1{(e,0)}) ∼
= ⊕a,bVa,b where, for a and b cubic roots
of unity, Va,b is the 1-dimensional representation of H on which ( σm,n ) acts as
multiplication byambn. Since Ind G
H (⊕bV1,b) ∼
=W we ﬁnd by considering the action
of (e, 1) that Ind G
H (Va,b) ∼
= Wb when a ⁄= 1. In particular, in the notation of
Example 5.7, we have L(s,Wb, Q) = L(s,Va,b,q ) since q =kH .
It is easy to see that the coeﬃcients of p−s in the Euler factors of L(s,Wζ3, Q)
and L(s,Wζ2
3
, Q) are conjugate, but since not all of them can be real it is not
possible to express those functions in terms of ζ-functions of subﬁelds of k.
7. Examples
In this section we describe the evidence for Conjecture 3.18 in the c ase of prim-
itive idempotents π in E[Gal(k/Q)] as in Examples 5.3, 5.5 and 5.7, with E = Q
in the ﬁrst two and E = Q(ζ3) in the last. In the ﬁrst two cases part (1) of the
conjecture is known by Proposition 5.9, but in the last case our evide nce for this
part is numerical; the same holds for parts (2) through (4) in all cas es.
We would like to stress that the numerical veriﬁcation of part (4) of the conjecture
actually proves this part for all cases that we considered since we c an check that a
element ofE ⊗ Qp is a unit of that ring by computing a close enough approximation
of it.
For the numerical calculations of the p-adic regulator, Rn,p(ME
π ), we assumed
that the syntomic regulator map on the subgroup of K2n−1(k)Q described in Zagier’s
Conjecture 4.5 is given by the ~Pσ
n,p (as in Remark 4.15). Out of the many possible
choices for Pn,p(z) as described in (4.12) we used
Pn,p(z) = Lin,p(z) − logn−1
p (z)Li1(z)/n! = Lin,p(z) + logn−1
p (z) logp(1 −z)/n!
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 31
since it is relatively simple from a computational point of view. The calcu lations
of the Pn,p(z) for the branch with log p(p) = 0 were done in versions 2.11-7, 2.12-19
and 2.12-21 of [52], using an implementation of the algorithm described in [6].
Note that the primitive idempotents in Examples 5.3 and 5.5 are unique u p to
conjugation in Q[G] since they all correspond to π2. But in Example 5.7 replacing ζ3
withζ2
3 changes a primitive idempotent corresponding to π3 into one corresponding
to π4, and conversely. Because the same holds for the classical and p-adic L-
functions (with values in E ⊗Q C and E ⊗Q Qp respectively), as well as the Euler
factor for p, the conjectures for primitive idempotents corresponding to π3 and π4
are actually equivalent.
In Examples 7.1, 7.4 and 7.5 we have E = Q so that we identify E ⊗Q C with C,
etc., and use notation as in Remark 3.17.
Example 7.1. Letk be a totally real S3-extension of Q. Use notation as in Case 1
of Example 5.3, and let π be the primitive idempotent corresponding to π2 of that
example. Since E = Q we shall write Mπ instead of ME
π in all notation referring
to Conjecture 3.18.
Since πK2n−1(k)Q = π2K2n−1(c)Q by Remark 3.22 we computed the K-theory
of c using the (numerical) methods of Section 5 and tried to recognize th e number
(7.2) e(n,Mπ) = L(n,χπ, Q) ·D(Mπ)1/2,∞/Rn,∞(Mπ)
for n = 3 and 5 as an element of Q∗ by employing the same methods as described
in Section 5 for number ﬁelds, where L(n,χπ, Q) was computed as ζc(n)/ζQ(n)
(see Example 6.5) using Pari-GP [53]. We succeeded in all cases, and th en veriﬁed
numerically for p = 2, 3, 5, 7 and 11 if Lp(n,χπω1−n
p , Q) ⁄= 0 and
(7.3) e(n,Mπ) · Eulp(n,χπ, Q) · Rn,p(Mπ)
D(Mπ)1/2,p ·Lp(n,χπω1−n
p , Q)−1
in Q∗
p was equal to 1.
We put our results for the four totally real S3-extensionsk of Q with smallest dis-
criminants in Tables 1 through 4. Note that by Lemma 3.7 Rn,p(Mπ)/D(Mπ)1/2,p
is in Qp and the same holds for Lp(n,χπω1−n
p , Q) by Lemma 3.15, so that (ap-
proximations of) those numbers can be easily represented in our ta bles. We have
denoted an element ( a0 +a1p +a2p2 + · · · ) ×ps in Q∗
p with all aj in {0,...,p − 1}
and a0 ⁄= 0 by (a0.a1a2 · · · )p ×ps, writing A to represent 10 when p = 11.
For the p-adic regulators we computed each Pn,p(z) up to O(pL(p)) with pL(p)
approximately equal to 10 30. The relevant part of Rn,p(Mπ)/D(Mπ)1/2,p has been
given in the tables whenever it ﬁtted. For the values of the p-adic L-function we
can only prove that the relative error is at most 1 + O(pM(p)), where M (2) =
72, M (3) = 47, M (5) = 32, M (7) = 26 and M (11) = 22. This proves that
Lp(n,χπω1−n
p , Q) does not vanish; together with the veriﬁcation that (7.2) equals
1 numerically this proves part (4) of Conjecture 3.18. The value tha t we found
for (7.3) was 1 + O(pN (p)) with N (2) ≥ 82, N (3) ≥ 52, N (5) ≥ 36, N (7) ≥ 27 and
N (11) ≥ 24, giving numerical evidence for parts (2) and (3) of the conject ure, but
also suggesting that the relative precision of the value of the p-adic L-function is
slightly higher than we can prove, justifying the higher precision give n in the tables.
Similar calculations were carried out for the next four such S3 extensions and
the same primes, with very similar results.
32AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
The other examples proceed mostly along the same lines as Example 7.1 . The
values of L(n,χπ, Q) in Examples 7.4 and 7.5 below were computed using the for-
mula at the end of Example 6.6, but in Example 7.6 the values of L(n,χE
π, Q),
with E = Q(ζ3) for ζ3 a primitive cube root of unity, were computed using the
algorithms described in [24] and its associated program. In Examples 7.4 and 7.5
we determined if e(n,χπ) (as in (7.2)) was in Q∗ using the methods of Section 5,
and for Example 7.6 we wrote e(n,M E
π )−1 = 1 ⊗a +ζ3 ⊗b in E ⊗Q R and then
recognizeda andb as integers divided by products of some relatively small primes.
In each case we then veriﬁed for p = 2,..., 11 if (7.3) (or its equivalent) was equal
to 1 in Qp or, for Example 7.6, in Qp(ζ3) ⊗Q Q = Qp(ζ3). The precision for Pn,p(z)
and the p-adic L-functions in Examples 7.4 and 7.5 was as in Example 7.1. In
Example 7.6 all Pn,p(z) were computed up to O(pL(p)) with pL(p) approximately
1016 since in this case the check if the equivalent of (7.3) is 1 is done in Q(ζ3) ⊗Q Qp
so two coeﬃcients are checked; the values of the p-adicL-function in this case, also
in Q(ζ3) ⊗Q Qp, were determined up to multiplication by 1 ⊗ (1 +O(pM(p))) with
M (p) as in Example 7.1.
Example 7.4. Letk be a totally real D8-extension of Q as in Case 1 of Example 5.5,
and use notation as in that example. We again write Mπ instead ofME
π sinceE = Q
and consider odd n ≥ 2. Because πK2n−1(k)Q = π2K2n−1(k1)Q we computed
K2n−1(k1)Q numerically using the methods of Section 4. Our results with n = 3
and 5 for the ﬁrst four such extensions when ordered according t o the discriminant
are in Tables 5 through 8. The value that we found for (7.3) in this cas e was
1 +O(pN (p)) where N (2) ≥ 76,N (3) ≥ 52,N (5) ≥ 34,N (7) ≥ 29 and N (11) ≥ 22.
Such calculations were also carried out for the next four such exte nsions, with
similar results.
Example 7.5. Let k be a CM Galois extension of Q with Gal(k/Q) ∼
= D8 as
in Case 2 of Example 5.5, and use notation as in that example. We again w rite
Mπ instead of ME
π since E = Q, and consider even n ≥ 2. Again πK2n−1(k)Q =
π2K2n−1(k1)Q, so we computed K2n−1(k1)Q numerically using the methods of Sec-
tion 4. We put our results at n = 2 and 4 for the ﬁrst four such extensions when
ordered by the value of the (positive) discriminant in Tables 9 throug h 12. The
value that we found for (7.3) in this case was 1 + O(pN (p)) where N (2) ≥ 79,
N (3) ≥ 53, N (5) ≥ 35, N (7) ≥ 27 and N (11) ≥ 25. Such calculations were also
carried out for the next four such extensions, with similar results.
Example 7.6. Let k be a totally real S3 × Z/3Z extension of Q, as in Case 1 of
Example 5.7. We use notation as in that example, taking E = Q(ζ3) for a primitive
cubic root of unity ζ3. A diﬀerent identiﬁcation of Gal( k/Q) with S3 × Z/3Z might
interchangeπ3 and π4 as well as corresponding primitive idempotents, but, as we
noted before, the validity of the conjecture for either is equivalen t.
Since πK2n−1(k)E = π3K2n−1(s1)E we computed K2n−1(s1)Q as before. Also,
in order to speed up the calculations of the regulator we note that t he action of
(e, 1) and (σ2, 0) on s1 =k⟨(σ,1)⟩ is the same, so that π =π3πH1 and
(1 −π1)((e, 0) +ζ3(σ, 0) +ζ2
3 (σ2, 0))/3 = ((e, 0) +ζ3(σ, 0) +ζ2
3 (σ2, 0))/3
give the same result when applied to K2n−1(s1)E. We put our results for the ﬁrst
fours1, when ordered according to their discriminant, for n = 3 and 5 in Tables 13
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 33
through 16. In Table 16 the number e(5,M E
π )−1 is given by
−25 · 310 · 5−2 · 134 · (7 + 3ζ3) · (68 − 43ζ3) · (1547202 − 1603487ζ3) · (a +bζ3)
with
a = 8482255892311139091186217686741233
and
b = 3527440500058817421018094757947617,
presumably because we experimentally found a subgroup of K2n−1(s1)Q that is not
close to actually being K2n−1(s1). In all cases Lp(n,χπ ⊗ω1−n
p , Q) is a unit in
E ⊗Q Qp, and when we write the equivalent of (7.3) in the form 1 ⊗α +ζ3 ⊗β then
we ﬁnd that α − 1 and β are O(pN (p)) with N (2) ≥ 50, N (3) ≥ 24, N (5) ≥ 20,
N (7) ≥ 14 and N (11) ≥ 12, with in this case the precision bounded by that of
the Rn,p(ME
π ). Since e(n,M E
π ), D(ME
π )1/2,p and Eulp(n,χπ ⊗ id, Q) are units in
E ⊗Q Qp this also shows that Rn,p(ME
π ) is a unit in E ⊗Q F , as conjectured in
Conjecture 3.18(4).
Such calculations were also carried out for the next four such s1 with similar
results.
Remark 7.7. By Proposition 4.17 and Remark 3.21(1), the conjecture for π in
Example 7.1 is equivalent to Conjecture 2.17 for the ﬁeld k1 in the example. The
same statement holds for π and k1 in Example 7.4 below.
Remark 7.8. In the tables we have also included the value of the constant C(χπ ⊗
id) = C(χ∨
π ⊗ id) in the functional equation (3.25) of L(s,χπ ⊗ id, Q) to make
possible a comparison between its prime factors and those of e(n,Mπ). Namely, for
the D(ME
π )1/2,∞ used in the calculations, the en in (3.26) (which in our case are
independent of n) are as follows.
Table en Table en Table en Table en
1 3 5 4 9 4 13 1 ⊗ 9 +ζ3 ⊗ 9
2 3 6 4 10 4 14 1 ⊗ 9 +ζ3 ⊗ 9
3 3 7 4 11 −4 15 1 ⊗ 0 +ζ3 ⊗ 9
4 3 8 4 12 4 16 1 ⊗ 0 +ζ3 ⊗ (−9)
As can be seen from these values and Tables 1-16, in the number
δnen((n − 1)!/2)mC(χ∨
π ⊗ id)n−1e(n,M E
π )
of (3.27) the larger prime factors occurring in e(n,M E
π ) are often cancelled by those
of C(χ∨
π ⊗ id)n−1. This suggests that the formulation of Beilinson’s conjecture at
s = 1 −n normally involves simpler prime factors in E∗ than the formulation at
s =n in Conjecture 3.18(1), with the remaining complicated factors in our examples
quite possibly due to an awkward choice of basis for K2n−1(ME
π ).
34AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
