---
doc_id: arxiv-0707.3682v2
doc_title: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS"
section_id: sec-001-3-a-motivic-version-of-the-conjecture
section_title: "A motivic version of the conjecture"
section_number: 3
pages: 9-29
source_pdf: 0707.3682v2.pdf
source_sha256: 609a6f67a0cd5fc8
doc_brief: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS — We formulate a conjectural p-adic analogue of Borel’s theorem re- lating regulators for higher K-groups of number ﬁelds to special values of the"
---
If E is any extension of Q, and k/Q is ﬁnite and Galois with Galois group G,
then we let ME = E ⊗Qk and K2n−1(k)E = E ⊗QK2n−1(k)Q, which are E[G]-
modules. The goal of this section is to reﬁne Conjecture 2.17 to a co njecture for
10AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
Artin motives with coeﬃcients in E, or equivalently, idempotents in the group ring
E[G], when E is a number ﬁeld.
Deﬁnition 3.1. For an idempotentπ inE[G] we letME
π =πME andK2n−1(ME
π ) =
πK2n−1(k)E.
Now ﬁx an embedding φ∞ :k → C. The pairing G ×k → C mapping (σ,a ) to
φ∞(σ(a)) leads to an E-bilinear pairing
(3.2)
E[G] ×ME →E ⊗Q C
(eσ,e ′ ⊗a) ↦→ee′ ⊗φ∞(σ(a)).
and we consider its restriction
( ·, · )∞ :E[G]π ×ME
π →E ⊗Q C.
Similarly, replacing φ∞ with a ﬁxed embedding φp :k → Qp we obtain
( ·, · )p :E[G]π ×ME
π →E ⊗QF.
whereF ⊂ Qp is the topological closure of φp(k), which is independent of φp since
k/Q is Galois.
Lemma 3.3. Letπ in E[G] be an idempotent. Then dimE(ME
π ) = dimE(E[G]π).
Proof. Sinceπ2 =π, (3.2) is identically 0 on E[G]π ×ME
1−π andE[G](1 −π) ×ME
π .
But the determinant of this pairing is, up to multiplication by E∗, equal to D1/2,∞
k ,
hence non-zero. This implies the lemma. □
We now introduce pairings similar to ( ·, ·)∞ and ( ·, ·)p but replacing ME
π with
K2n−1(ME
π ). If we denote the map K2n−1(k)Q → K2n−1(C)Q induced by φ∞ by
φ∞∗ and let Φ ∞ be the composition with the Beilinson regulator map reg ∞ for C,
Φ ∞ = reg ∞ ◦φ∞∗ :K2n−1(k)Q →K2n−1(C)Q → R(n − 1) ⊂ C,
then the pairing G ×K2n−1(k)Q → C given by mapping ( σ,α ) to Φ ∞(σ(α)) gives
rise to an E-bilinear pairing
(3.4)
E[G] ×K2n−1(ME) →E ⊗Q C
(eσ,e ′ ⊗α) ↦→ee′ ⊗ Φ ∞(σ(α))
and we consider its restriction
[ ·, · ]∞ :E[G]π ×K2n−1(ME
π ) →E ⊗Q C.
By Lemma 2.15 and the deﬁnition of F the syntomic regulator gives us
regsyn :K2n−1(OF )Q →F.
If we write φp∗ for the composition K2n−1(k)Q ∼
= K2n−1(Ok)Q → K2n−1(OF )Q,
with the second map induced by φp :k →F , and let Φ p be the composition
regsyn ◦φp∗ :K2n−1(k)Q →K2n−1(F )Q →F,
then we can similarly obtain a pairing
[ ·, · ]p :E[G]π ×K2n−1(ME
π ) →E ⊗QF.
We now ﬁx ordered E-bases of E[G]π, ME
π , and K2n−1(ME
π ).
Deﬁnition 3.5. For ∗ = ∞ or p we let D(ME
π )1/2,∗ be the determinant of the
pairing ( ·, ·)∗, computed with respect to our ﬁxed bases of E[G]π and ME
π .
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 11
Note that D(ME
π )1/2,∞ is non-zero by the proof of Lemma 3.3, and the same
argument works for D(ME
π )1/2,p.
Deﬁnition 3.6. If dimE(E[G]π) equals dim(K2n−1(ME
π )) then for ∗ = ∞ orp we
let Rn,∞(ME
π ) be the determinant of the pairing [ ·, ·]∗, computed with respect to
our ﬁxed bases of E[G]π and K2n−1(ME
π ).
For future use we prove the following.
Lemma 3.7. If dimE(E[G]π) = dim(K2n−1(ME
π )) then
(1) Rn,∞(ME
π )/D(ME
π )1/2,∞ is independent of the basis of E[G]π, of φ∞, and
lies in E ⊗ R;
(2) Rn,p(ME
π )/D(ME
π )1/2,p is independent of the basis of E[G]π, of φp, and
lies in E ⊗ Qp.
Proof. We prove the second statement, the proof of the ﬁrst being entir ely similar.
Choosing a diﬀerent E-basis of E[G]π corresponds to letting an E-linear transfor-
mation act on E[G]π, and in the given quotient the resulting determinant cancels.
Since k/Q is Galois we get all possible embeddings of k into Qp by replacing φp
with φp ◦σ for σ in G. For both Rn,p(ME) and D1/2,p(ME) this corresponds to
letting σ act on E[G]π, and the resulting determinant cancels as before. That the
quotient lies in E ⊗ Qp follows because it lies in E ⊗F and we have just proved
that it is invariant under Gal( F/Qp) by Lemma 2.15. □
We now investigate when the two dimensions in Deﬁnition 3.6 are equal. T he
answer is given by Proposition 3.12 below, but we need some preliminary results.
Proposition 3.8. If k/Q is a ﬁnite Galois extension with Galois group G and π
is an idempotent in E[G] then dimE(K2n−1(ME
π )) ≤ dimE(E[G]π). Equality holds
precisely when any (hence every ) τ in the image in G of the conjugacy class of
complex conjugation in Gal(Q/Q) acts by (−1)n−1 on E[G]π.
Proof. For the statement we can ﬁrst replace E by a ﬁnitely generated subﬁeld
since π contains only ﬁnitely many elements of E, next embed E into C and use
this embedding to enlarge E to C. So we may assume that E = C.
According to Theorem 2.2 the pairing (3.4) gives an injection
(3.9)
R ⊗QK2n−1(k)Q → R[G]∨ = Hom R(R[G], R)
α ↦→fα with fα(σ) = 1
(2πi)n−1 Φ ∞(σ(α))
and by extending the coeﬃcients we get an injection C ⊗QK2n−1(k)Q → C[G]∨.
The image of π(K2n−1(k)Q ⊗Q C) under the last map vanishes on C[G](1 −π) since
(1−π)π = 0 so that πK2n−1(k)Q ⊗Q C injects into (C[G]/C[G](1−π))∨ ∼
= (C[G]π)∨,
which proves our ﬁrst inequality.
As for equality, we know by Theorem 2.2 that (3.9) has as its image the subspace
of R[G]∨ where, under the action of Gal(
Q/Q) on R[G]∨ via (˜σf )(σ) = f (˜σ−1σ),
the conjucagy class of complex conjugation in Gal( Q/Q) acts as multiplication by
(−1)n−1. The same will therefore hold with complex coeﬃcients. Since any elem ent
τ in the conjugacy class of complex conjugation has order 1 or 2, C[G]π decomposes
into eigenspaces for the eigenvalues ±1 and the desired equality can only hold if τ
acts as multiplication by ( −1)n−1 on all of C[G]π. □
12AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
We now determine precisely when the equality of dimensions as in Propo sition 3.8
can occur, and for this we need a preliminary result.
Proposition 3.10. Letψ be a representation of Gal(
Q/Q) over Q that factorizes
through the Galois group of a ﬁnite Galois extension of Q and for which ψ(τ ) acts as
multiplication by (−1)n−1 for any τ in the conjugacy class of complex conjugation
in Gal(Q/Q). Then the ﬁxed ﬁeld of Ker(ψ) is a ﬁnite Galois extension of Q that
is totally real if n is odd, and CM if n is even.
Proof. That the ﬁxed ﬁeld k of Ker(ψ) is a ﬁnite Galois extension of Q is clear.
When n is odd ψ(τ ) = 1 for any τ in the conjugacy class of complex conjugation
so that k is totally real. For even n we let ω be the composition Gal( Q/Q) →
Gal(Q(µ4)/Q)
∼
→ {± 1} ⊂ Q
∗
. Then Ker( ψω) contains τ and Ker(ψ) ∩ Ker(ω),
hence its ﬁxed ﬁeld is a totally real Galois extension k+ of Q, contained in k(µ4).
Similarly k is contained in the CM ﬁeld k+(µ4) so, since k is not totally real, it
must be CM. □
Remark 3.11. For a CM ﬁeld k withk/Q Galois, its maximal totally real subﬁeld
is Galois over Q and is the ﬁxed ﬁeld of an element of order two in the centre of
Gal(k/Q), which we shall refer to as the complex conjugation of k.
Proposition 3.12. Let k/Q be a ﬁnite Galois extension with Galois group G,
E any extension of Q, and π an idempotent of E[G]. Let k′ be the ﬁxed ﬁeld
of the kernel of the representation of G on E[G]π. Then for n ≥ 2 the equality
dimE(E[G]π) = dimE(K2n−1(ME
π )) holds precisely in the following cases:
(1) k′ is totally real and n is odd;
(2) k′ is a CM ﬁeld, n is even, and the complex conjugation of k′ acts on E[G]π
as multiplication by −1.
Proof. From Propositions 3.8 and 3.10 we see that there cannot be any othe r cases.
Conversely, by Proposition 3.8 equality holds in both. □
We now recall and introduce some terminology for later use.
Deﬁnition 3.13. Let G be a ﬁnite group and E any extension of Q.
(1) If π is a central idempotent of E[G] such that E[G]π is a minimal (non-zero)
2-sided ideal of E[G] then π is a primitive central idempotent.
(2) If π is a primitive central idempotent of E[G] such that E[G]π ∼
= Mm(E)
as E-algebras for some m then we call a primitive idempotent correspond-
ing to π any element in E[G]π ⊆ E[G] that maps to a matrix in Mm(E)
that is conjugate to a matrix with 1 in the upper left corner and 0’s els e-
where. (Since all automorphisms of Mm(E) as E-algebra are inner this is
independent of the isomorphism E[G]π ∼
=Mm(E).)
Remark 3.14. (1) If E[G]π ∼
= Mm(E) then any idempotent in E[G]π can be
written as a sum of orthogonal primitive idempotents correspondin g to π as one
sees immediately by diagonalizing the matrix A that π maps to, which satisﬁes
A2 =A.
(2) If G = Gal(k/Q) and π is a primitive central idempotent of E[G] then the
dimensions of E[G]˜π and ˜πK2n−1(k)E are equal for some non-zero idempotent ˜ π
in E[G]π if and only if the same holds for one (hence any) primitive idempotent
corresponding to π. Indeed, the dimensions for π do not change if we replace it
with a conjugate in E[G], and they add up for sums of orthogonal idempotents.
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 13
We now introduceL-functions, both classical and p-adic, in the following context.
Let E be a ﬁnite extension of Q, k a number ﬁeld, and consider a character ψ of
a representation of G = Gal(k/k) on a ﬁnite dimensional E-vector space V that
factorizes through Gal( k/k ′) for some ﬁnite extension k′ of k. Then for every
embedding σ : k → C we have the Artin L-function L(s,σ (ψ),k ), with for every
prime P ofk the reciprocal Eul P(s,σ (ψ),k ) of the Euler factor corresponding to P.
Under the natural isomorphism E ⊗Q C
∼
→ ⊕σCσ the L(s,σ (ψ),k ) correspond to
a canonical E ⊗Q C-valuedL-function that we denote by L(s,ψ ⊗ id,k ). Similarly,
for every prime P of k we have an E ⊗Q C-valued Eul P(s,ψ ⊗ id,k ) corresponding
to the Eul P(s,σ (ψ),k ).
We now move on to the p-adic L-functions, and assume that k is totally real, p
a prime number, a any integer and ωp the Teichm¨ uller character Gal(Q/k) → Q∗
p
(2.14). If τ : E →
Qp is an embedding and kτ (ψ)ωap is totally real then from
Section 2 we have the p-adic L-function Lp(s,τ (ψ)ωa
p,k ), which is not identically
zero. In this case, using the natural isomorphism E ⊗Q Qp
∼
→ ⊕τ Qp,τ , they give
us an E ⊗Q Qp-valued p-adic L-function on Zp or Zp \ { 1} that we denote by
Lp(s,ψ ⊗ωa
p,k ).
Lemma 3.15. The values of Lp(s,ψ ⊗ωa
p,k ) are in E ⊗Q Qp.
Proof. Using Brauer induction for ψ (cf. (2.10)) it suﬃces to do prove this when ψ
is 1-dimensional. But then for each τ :E → Qp the function Lp(s,τ (ψ)ωa
p,k ) can
be described as in (6.3) with l = −1, from which the result is clear. □
Remark 3.16. It follows from Remark 2.13 that Lp(s,ψ ⊗ωa
p,k ) satisﬁes
Lp(m,ψ ⊗ωa
p,k ) = Eulp(m,ψ ⊗ id,k )L(m,ψ ⊗ id,k )
for integers m ≤ 0 congruent to 1 −a modulo φ(q), where both sides lie in E =
E ⊗Q Q inside E ⊗Q Qp and E ⊗Q C respectively, and
Eulp(s,ψ ⊗ id,k ) =
∏
P|p
EulP(s,ψ ⊗ id,k )
the product being over all primes of k dividing p.
Remark 3.17. If E = Q we shall identify E ⊗Q C with C, and write L(s,ψ,k ),
etc., instead of L(s,ψ ⊗ id,k ), etc. Similarly we identify E ⊗Q Qp with Qp and write
Lp(s,ψωa
p,k ) instead of Lp(s,ψ ⊗ωa
p,k ).
We now have all the ingredients for the generalization and reﬁnemen t of Con-
jecture 2.17. Starting with a ﬁnite Galois extension k/Q with Galois group G,
E a ﬁnite extension of Q, and π an idempotent in E[G], we let ψπ be the nat-
ural representation of Gal( Q/Q) on E[G]π and χπ its associated character. If
dimE(E[G]π) = dimE(πK2n−1(k)E) for some n ≥ 2 then, for any prime p and any
embeddingτ :E → Qp,τ (ψπ)ω1−n
p is trivial on the conjugacy class of complex con-
jugation in Gal( Q/Q) by Proposition 3.8. In particular, Qτ (ψπ )ω1−n
p
is totally real
and therefore Lp(n,χπ ⊗ id, Q) is not identically zero. With F ⊂ Qp the topological
closure of φp(k) as before, using ordered bases for E[G]π,ME
π andK2n−1(ME
π ), we
haveD(ME
π )1/2,∞ and the regulator Rn,∞(ME
π ) in E ⊗ C as well as D(ME
π )1/2,p
and Rn,p(ME
π ) in E ⊗F .
14AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
Conjecture 3.18. With notation as above, if dimE(E[G]π) = dimE(πK2n−1(k)E)
for some n ≥ 2, then
(1) in E ⊗Q C we have
L(n,χπ ⊗ id, Q)D(ME
π )1/2,∞ =e(n,M E
π )Rn,∞(ME
π )
for some e(n,M E
π ) in (E ⊗Q Q)∗;
(2) in E ⊗QF we have
Lp(n,χπ⊗ω1−n
p , Q)D(ME
π )1/2,p =ep(n,M E
π ) Eulp(n,χπ⊗ id, Q)Rn,p(ME
π )
for some ep(n,M E
π ) in (E ⊗Q Q)∗;
(3) in fact, ep(n,M E
π ) = e(n,M E
π );
(4) Lp(n,χπ ⊗ω1−n
p , Q) and Rn,p(ME
π ) are units in E ⊗Q Qp and E ⊗Q F
respectively.
Remark 3.19. (1) One sees as in the proof of Lemma 3.7 that the validity of
each part of the conjecture is independent of the chosen bases o f E[G]π, ME
π and
K2n−1(ME
π ).
(2) Since E ⊗Q C
∼
→ ⊕σEσ, where the sum is over all embeddings σ : E → C,
an identity in E ⊗Q C is equivalent to the corresponding identities for all such
embeddings. The same holds if we replace C with Qp.
In Remark 3.24 we shall make explicit how part (1) of this conjecture is equivalent
with Beilinson’s conjecture [2, Conjecture 3.4] for an Artin motive as sociated with
π. First, we make various remarks about its dependence on E, etc., and on its
relation with Conjecture 2.17.
Remark 3.20. (1) An equivalent for Conjecture 3.18(1) can be formulated for an y
idempotent π if k/Q is any ﬁnite Galois extension (see the end of Section 5), in
which case it is a conjecture by Gross (see [39, p. 210]). In that cas e it was proved
by Beilinson if the action of G = Gal(k/Q) on E[G]π is Abelian (see loc. cit.). One
can deduce that it holds for any π in E[G] if this action factors through S3 or D8
(see Proposition 5.9).
(2) If the action of G on E[G] is Abelian then parts (1)-(3) of Conjecture 3.18
also hold for any π to which the conjecture applies (see Remark 4.18).
(3) Extending and simplifying earlier work by F. Calegari [13], F. Beuk ers in [8]
proved that ζp(2) is irrational when p = 2 or 3. This value equals Lp(2,χω −1
p , Q)
with χ the primitive character on ( Z/4Z)∗ for p = 2, and the primitive character
on ( Z/3Z)∗ for p = 3. Moreover, if χ is the odd primitive character on ( Z/8Z)∗
then he also shows that L2(2,χω −1
2 , Q) is irrational. It follows that the conjecture
holds in full for π corresponding to the non-trivial representation of Gal( k/Q) and
n = 2 when ( k,p ) is one of ( Q(√
−1), 2), ( Q(√−2), 2) and ( Q(√−3), 3).
(4) We have veriﬁed numerically that part (4) of the conjecture ho lds in certain
cases; see Remark 4.19 as well as Section 7.
Remark 3.21. (1) If π =π1 +· · ·+πm withπ2
i =πi andπiπj = 0 when i ⁄=j, then
the conjecture for π is implied by the conjecture for all πi becauseD(⊕iME
i )1,2/∞ =∏
iD(ME
i )1/2,∞, etc., as one easily sees by using bases.
(2) If π is in E[G] and E′ is an extension of E, then we may view π as an
element of E′[G] as well, and the conjectures for ME
i and ME′
i are equivalent: we
can use the same bases over E′ as over E, so that D(ME
i )1/2,∞ = D(ME′
i )1/2,∞
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 15
inE ⊗ C ⊆E′ ⊗ C, and the same holds for all the other ingredients (including the
L-functions).
(3) By comparing bases one sees immediately that if π and π′ are conjugate
under the action of E[G]∗ then the conjectures for π and for π′ are equivalent.
(4) If, for a primitive central idempotent πi of E[G],E[G]πi ∼
=Mm(E) for some
m, and π is a primitive idempotent corresponding to πi, then the conjecture for
πi is implied by the conjecture for π. Indeed, we can decompose πi into a sum
of orthogonal primitive idempotents as in Remark 3.14(1), and the t ruth of the
conjecture for πi is implied by its truth for each such primitive idempotent. But
all such primitive idempotents are conjugate to π hence part (3) above applies.
Remark 3.22. Ifk/Q is a Galois extension with Galois group G andH a subgroup
of G with ﬁxed ﬁeld kH , then Km(k)H
Q = Km(kH )Q, a result known as Galois
descent. With πH = |H|−1∑
h∈Hh, an idempotent in E[G], this implies that
πHKm(k) = Km(kH ).
Remark 3.23. (1) Let k/Q be a Galois extension with Galois group G. If N
is a normal subgroup of G corresponding to k′ = kN and πN = |N |−1∑
h∈Nh,
then π2
N =πN and the natural map φ :E[G] →E[G/N] has kernel E[G](1 −πN )
and induces an isomorphism E[G]πN → E[G/N]. Indeed, it is clear that πN is
central in E[G] since N is normal in G and that 1 −πN is in the kernel of φ.
Also, since N acts trivially on E[G]πN this is an E[G/N]-module generated by one
element, so its dimension over E cannot be bigger than |G/N|. Since φ is obviously
surjective our claims follow. Therefore in this situation for any idemp otent π in
E[G/N] there is a canonical idempotent ˜ π lifting π to E[G]πN , and the natural
map E[G]˜π →E[G/N]π is an isomorphism of E[G]- and E[G/N]-modules.
Then the statements of Conjecture 3.18 for π in E[G/N] or for ˜π in E[G] are
equivalent. Namely,
˜πK2n−1(k)E = ˜ππNK2n−1(k)E = ˜πK2n−1(k′)E =πK2n−1(k′)E
insideK2n−1(k)E so that we can use the same bases for either side. The same holds
for ˜π(E ⊗k) and π(E ⊗k′) inside E ⊗k. Moreover, E[G]˜π is the pullback to G of
theG/N-representationE[G/N]π, so that L(s,E [G]˜π, Q) = L(s,E [G/N]π, Q) and
similarly for the p-adic L-functions.
(2) If k is a totally real number ﬁeld k let ˜k be its (totally real) Galois closure
over Q. Then k = ˜kH for some subgroup H of G = Gal( ˜k/Q), π = |H|−1∑
h∈Hh
is an idempotent in Q[G], and for n ≥ 2 odd Conjecture 3.18 for π is equivalent
to Conjecture 2.17 for k. Namely, K2n−1(k)Q =πK2n−1(˜k)Q ⊆K2n−1(˜k)Q by Re-
mark 3.22 and π˜k =k so that we can use the same Q-bases in each case. Moreover,
Q[G]π ∼
= IndG
H (1H ) = Q[G] ⊗Q[H] 1H with 1H the trivial 1-dimensional representa-
tion of H, as one easily sees by mapping β in Q[G]π toβ ⊗v and∑
σaσσ ⊗ (λv) to
λ∑
σaσσπ, {v} being a basis of 1 H. By well-known properties of Artin L-functions
[40, Prop. 10.4(iv)] this implies that ζk(s) = L(n, Q[G]π, Q) and similarly for the
p-adicL-functions.
Remark 3.24. We make the relation between Conjecture 3.18(1) and Beilinson’s
conjecture [2, Conjecture 3.4] for (Artin) motives explicit since th e relation between
the two elements of E∗ involved also shows up very explicitly in our computer
calculations, suggesting that the element for the formulation at s = 1 −n is simpler
16AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
than for our formulation at s =n (see Remark 7.8). We provide some details since
we could not ﬁnd a detailed enough reference in the literature.
With notation as in Conjecture 3.18 and (2.6) we have
(3.25)
L(1 −s,χ ∨
π ⊗ id, Q) = W (χ∨
π ⊗ id)C(χ∨
π ⊗ id)s− 1
2 (2(2π)−sΓ(s))χ∨ (1)
× (cos(πs/2))n+
(sin(πs/2))n−
L(s,χπ ⊗ id, Q),
withχ∨
π the dual character of χπ,W (χ∨
π ⊗id) in E ⊗C, and C(χ∨
π ⊗id) = C(χπ ⊗id)
in Q∗. If m = dimE(E[G]π), then n+ = m and n− = 0 for n odd, and n− = m
and n+ = 0 for n even. In either case L(s,χ ∨
π ⊗ id, Q) has a zero of order m at
s = 1 −n. Moreover
(3.26) W (χ∨
π ⊗ id)C(χ∨
π ⊗ id)1/2 =enim(n−1)D(ME
π )1/2,∞
for some en in E∗ = (E ⊗Q Q)∗ by [20, Propositions 5.5 and 6.5] since D1/2,∞ can
be taken to be the same for ME
π and the associated determinant representation
(cf. [31, p.360]). Hence the ﬁrst non-vanishing coeﬃcient in its Taylo r expansion
around s = 1 −n,L♯(1 −n,χ ∨
π ⊗ id, Q), equals
δnen(2πi)m(1−n)((n − 1)!/2)mC(χ∨
π ⊗ id)n−1D(ME
π )1/2,∞L(n,χπ ⊗ id, Q)
with δn = (−1)m(n−1)/2 when n is odd, and δn = (−1)m(n+2)/2 when n is even. In
particular, Conjecture 3.18(1) is equivalent with
(3.27) L♯(1−n,χ ∨
π ⊗id, Q) = δnen((n−1)!/2)mC(χ∨
π ⊗id)n−1e(n,M E
π )~Rn,∞(ME
π )
with the renormalized regulator ~Rn,∞(ME
π ) = (2πi)m(1−n)Rn,∞(ME
π ).
Let us compare this with Beilinson’s conjecture for a motive associat ed with π.
We associate motives covariantly to smooth projective varieties ov er Q as in [2,
§ 2.4]. The Galois group G acts on the left on k, hence on the right on Spec( k),
and we let Mπ be the motive corresponding to π under this action. Then G acts
on the left on the cohomology theories on Spec( k) as well as its K-theory, and after
tensoring with E the corresponding groups for Mπ are the images under π. Thus,
the relevant motivic cohomology of Mπ is H 1
M (Mπ/Z, Q(n)) = K2n−1(ME
π ).
We shall need the non-degenerate E-bilinear pairing
E[G] ×
⨁
τ :k→C
E →E
(∑
σaσσ, (bτ )τ ) ↦→∑
σaσbφ∞◦σ−1.
It factors through the left E[G]-action on ⊕τE (given by σ((bτ )τ ) = ( bτ ◦σ−1)τ ),
hence is trivial on E[G](1 −π) ×π(⊕τE) and E[G]π × (1 −π)(⊕τE). We therefore
obtain a non-degenerate E-bilinear pairing
(3.28) ⟨ ·, · ⟩ :E[G]π ×π(⊕τE) →E
that identiﬁes E[G]π and π(⊕τE) as dual E[G]-modules.
Tensoring (2.1) with E and applying π we get
H 1
D(Mπ/R, R(n)) ∼
=π
(⨁
τ :k→C
E ⊗ R(n − 1)
)
.
Note that the left hand side is a subspace of the right hand side by (2 .1), but because
the regulator map (2.3) tensored with R is injective, and dim E(K2n−1(ME
π )) =
dimE(E[G]π) = dimE(π(⊕τE)) by our assumption on π and sinceD(ME
π )1/2,∞ ⁄= 0
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 17
(as was noticed right after Deﬁnition 3.5), equality must hold. For th e Beilinson reg-
ulator we therefore have to compare the two E-structures on det H 1
D(Mπ/R, R(n))
coming from Betti cohomology,
H 0
B(Mπ/R, Q(n − 1)) ∼
=π(
⨁
τ :k→C
E ⊗ Q(n − 1)) ⊆π
(⨁
τ :k→C
E ⊗ R(n − 1)
)
,
and that induced by the Beilinson regulator map (2.3),
H 1
M (Mπ/R, Q(n)) →H 1
D(Mπ/R, R(n)) = π
(⨁
τ :k→C
E ⊗ R(n − 1)
)
.
Choosing an E-basis of π(⊕τE), and multiplying it by (2 πi)n−1 to obtain an E-
basis of π(⊕τE ⊗ Q(n − 1)), it is easy to see that Beilinson’s regulator RBei for Mπ
satisﬁes
RBei = (2πi)m(1−n) det[ ·, · ]∞/ det⟨ ·, · ⟩ = ~Rn,∞(ME
π )/ det⟨ ·, · ⟩
where all determinants are computed using the chosen E-bases.
Finally, we compare L-functions. We have
H 0
et(Spec(k) ⊗
Q, Ql) ∼
=
⨁
τ :k→
Q
Ql ∼
= Ql ⊗Q
( ⨁
τ :k→
Q
Q
)
so that H 0
et(Mπ, Ql) ∼
= Ql ⊗π(⊕τE) as Ql ⊗E[G]-modules. The Ql plays no role,
and as in (3.28) we see that π(⊕τ :k→
QE) is dual to E[G]π as E[G]-module. As
the motivic L-function uses the geometric rather than the arithmetic Frobeniu s
(cf. [34, p.26]), we obtain that L(s, Mπ) of [2, § 3] is equal to L(s,χπ ⊗ id, Q).
If θ : E[G] → E[G] is the E-linear involution obtained by replacing each σ in G
with σ−1, then we need to consider M0
π = Mθ(π) instead of Mπ. But the map
E[G]π ×E[G]θ(π) →E mapping (α,β ) to the coeﬃcient of the neutral element of
G inθ(β)α is easily seen to identify E[G]θ(π) and E[G]π as dual E[G]-modules, so
thatL(s, M0
π) = L(s,χ ∨
π ⊗ id, Q).
4. More explicit K-groups and regulators
In this section we ﬁrst describe an inductive procedure that conje cturally gives
K2n−1(k)Q (n ≥ 2) for any number ﬁeld k. It is originally due to Zagier [54], but we
essentially give a reformulation by Deligne [21]. We also describe results concerning
Conjecture 3.18 when the action of G on E[G]π is Abelian.
In order to describe Zagier’s conjecture we need the functions
(4.1) Li n(z) =
∑
k≥1
zk
kn (n ≥ 0)
forz in C with |z|< 1 if n = 0 or 1, and |z| ≤ 1 if n ≥ 2. In particular, Li 1(z) is the
main branch of − log(1 −z). Using that d Li n+1(z) = Li n(z) d log(z) they extend
to multi-valued analytic functions on C \ {0, 1}. By simultaneously continuing all
Lin along the same path one obtains single-valued functions on C \ {0, 1} (see [54,
§ 7] or [19, Remark 5.2]) by putting
(4.2) Pn(z) = πn−1
(n−1∑
j=0
bj
j! (2 log |z|)jLin−j(z)
)
(n ≥ 1),
18AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
withbj thej-th Bernoulli number and πn−1 the projection of C = R(n − 1) ⊕ R(n)
onto R(n − 1). These functions satisfy Pn(¯z) = Pn(z) as well as
(4.3) Pn(z) + (−1)nPn(1/z) = 0
and
(4.4) Pn(zm) = mn−1 ∑
ζm=1
Pn(ζz )
when m ≥ 1 and zm ⁄= 1.
We can now describe the conjecture. Let d = [k : Q], and for n ≥ 2 let ~Bn(k) be
a free Abelian group on generators [ x]∼
n with x ⁄= 0, 1 in k. Deﬁne
~Pn : ~Bn(k) →
(
R(n − 1)d) +
[x]∼
n ↦→(Pn(σ(x)))σ:k→C,
with
(
R(n − 1)d) +
= {(aσ)σ in R(n − 1)d such that a¯σ =
aσ}. Then we deﬁne
inductively, for n ≥ 2,
dn : ~Bn(k) →



2⋀
Zk∗ if n = 2
Bn−1(k) ⊗Zk∗ if n> 2
by
[x]∼
n ↦→
{
(1 −x) ∧x if n = 2
[x]n−1 ⊗x if n> 2 ,
where [x]n−1 denotes the class of [ x]∼
n−1 in Bn−1(k), which is deﬁned as
Bn(k) = ~Bn(k)/ Ker(dn) ∩ Ker(~Pn).
There are some universal relations, one of which is that [ x]n + (−1)n[1/x]n = 0, a
consequence of (4.3).
Conjecture 4.5. If n ≥ 2 then
(1) there is an injection
Ker(dn)
Ker(dn) ∩ Ker(~Pn)
→K2n−1(k)Q
with image a ﬁnitely generated group of rank equal to dimQ(K2n−1(k)Q);
(2) Beilinson’s regulator map is given by ~Pn:
Ker(dn)
Ker(dn) ∩ Ker(~Pn)
/d47/d47
(n−1)! ePn /d39/d39/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79
K2n−1(k)Q
Q
σ :k→C reg∞◦σ∗
/d15/d15(
R(n − 1)d) +
commutes.
Remark 4.6. For n = 2 the corresponding results were already known before
Zagier made his conjecture ([9, 51]; see also [26, § 2]).
From the results in [19, § 5] one obtains the following.
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 19
Theorem 4.7. Letk be a number ﬁeld and let n ≥ 2 be an integer. Then there is
an injection
Ψ n : Ker(dn)
Ker(dn) ∩ Ker(~Pn)
→K2n−1(k)Q
with ﬁnitely generated image, such that the diagram in Conje cture 4.5(2) commutes.
Remark 4.8. The part of Zagier’s conjecture that remains open is the question if
the rank of the image of Ψ n equals dim Q(K2n−1(k)Q). For a cyclotomic ﬁeld k this
holds for any n ≥ 2 as we shall recall in Example 4.10 below, but it is also known
for arbitrary number ﬁelds for n = 2, as mentioned above, or n = 3 (see [25, § 3]
and [27, Appendix]).
Remark 4.9. Although not stated explicitly in [19], it is clear from the construction
there that the map Ψ n in Theorem 4.7 is natural in k. In particular, if k/Q is Galois
then Gal(k/Q) acts on Ker(d n)/ Ker(dn) ∩ Ker(~Pn) (through the obvious action on
the generators [x]∼
n ) as well as on K2n−1(k)Q, and Ψ n is Gal(k/Q)-equivariant.
Example 4.10. If k is a cyclotomic ﬁeld then Zagier’s conjecture is known in
full. By Theorem 4.7 it suﬃces to see that the rank of the image of Ψ n equals
dimQK2n−1(k)Q. For an N -th root of unity ζ ⁄= 1, N [ζ]n is in Ker(d n)/ Ker(dn) ∩
Ker(~Pn). If k = Q(ζ) for a primitive N -th root of unity ζ with N > 2 then
dimQK2n−1(k)Q = [k : Q]/2 for n ≥ 2, and the N [ζj]n with 1 < j < N/2 and
gcd(j,N ) = 1 have R-independent images under ~Pn [54, pp.420–422] so that they
are Z-independent in Ker(d n)/ Ker(dn) ∩ Ker(~Pn), and the same holds for their
images under the injective map Ψ n. For k = Q one can easily check directly from
Theorem 4.7 and (4.2) that for odd n ≥ 2 the element 2Ψ([ −1]n) is non-zero.
For thep-adic regulator we need to describe the p-adic polylogarithms introduced
in [16]. We ﬁrst make a choice of a branch of the p-adic logarithm. Recall that a
homomorphism logp : O∗
Cp → Cp is uniquely determined by the requirement that
for |x|p < 1 it is given by the usual power series for log(1 + x). To extend it to a
homomorphism logp : Cp
∗ → Cp it suﬃces to make an arbitrary choice of log p(p).
Any such extension will be called a branch of the p-adic polylogarithm. In what
follows we ﬁx one such choice.
Coleman ﬁrst produced the p-adic polylogarithm out of a more extensive theory
of what is now called Coleman integration. For the p-adic polylogarithm it is,
however, possible to give a more elementary and explicit theory. To d o this, consider
the class of functions f : Cp \ {1} → Cp that satisfy the following properties:
(1) for any a ∈ Cp with |a − 1|p = 1 we have a power series expansion for f (z)
in z −a that converges for |z −a|p < 1;
(2) for 0 < |z − 1|p < 1 (resp. |z|p > 1) f (z) is given by a polynomial in
logp(z − 1) (resp. log p(1/z)) with coeﬃcients that are Laurent series in
z − 1 (resp. 1/z), convergent for 0 < |z − 1|p< 1 (resp. |z|p> 1).
It is easy to see that diﬀerentiation sends this class surjectively on to itself. The
p-adic polylogarithms are functions Li n,p(z) (n ≥ 0) in this class with the following
properties:
(1) Li 0,p(z) = z
1−z ;
(2) Li n,p(0) = 0 for n ≥ 0;
(3) dLi n+1,p(z) = Lin,p(z) dz
z for n ≥ 0;
20AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
(4) for every n ≥ 0 there is a power series gn(v), convergent for |v|p <p 1/(p−1),
such that gn(1/(1 −z)) = Lin,p(z) − 1
pn Lin,p(zp) when |z − 1|p>p −1/(p−1).
Note that 1 /z has a singularity at 0 but Li n,p(z)/z does not, because of the as-
sumption that Li n,p(0) = 0. In fact, it is easy to see that Li n,p(z) is given by the
p-adically convergent power series (4.1) for |z|p< 1.
In [6] two of the authors of the present work described an eﬃcient algorithm for
the computation of p-adic polylogarithms up to a prescribed precision. This will be
used in Section 7 to compute the p-adic regulator for n ≥ 2 that we now proceed
to describe in terms of suitable combinations of log n−m
p (z)Lim(z).
By Proposition 6.4 and the correct version of Proposition 6.1 of [16] t he Lin,p(z)
for n ≥ 0 and z in Cp \ {1} satisfy
Lin,p(z) + (−1)nLin,p(1/z) = − 1
n! logn
p (z)
when z ⁄= 0, and
(4.11) Li n,p(zm) = mn−1 ∑
ζm=1
Lin,p(ζz )
when m ≥ 1 and zm ⁄= 1.
Forz in Cp \ {0, 1} and ﬁxed n ≥ 2, we deﬁne
(4.12) Pn,p(z) =
n−1∑
j=0
cj logj
p(z)Lin−j(z) ( n ≥ 2)
for any cj in Cp satisfying c0 = 1 and ∑ n−1
j=0 cj/(n −j)! = 0, so that Pn,p(z) +
(−1)nPn,p(1/z) = 0. This is the case for cj =bj withbj thej-th Bernoulli numbers
as before, although the resulting formula is diﬀerent from (4.2). An other possible
natural candidate for the function Pn,p(z) is Ln(z) +Ln−1(z) logp(z)/n, where
Ln(z) =
n−1∑
m=0
(−1)m
m! logm
p (z)Lin−m(z)
(see [5, (1.3) and Remark 1.5]).
The relations corresponding to (4.3) and (4.11) for Pn,p(z) (n ≥ 2) are then
Pn,p(z) + (−1)nPn,p(1/z) = 0
when z ⁄= 0, 1, and
(4.13) Pn,p(zm) = mn−1 ∑
ζm=1
Pn,p(ζz )
when m ≥ 1 and zm ⁄= 0, 1.
For any branch of the p-adic logarithm one then has the following result for the
p-adic regulator map (see [5, Theorem 1.10 or page 909]). Since its for mulation
depends on the embedding of k we deal with one such embedding at a time.
Theorem 4.14. Letk be a number ﬁeld, and let F ⊂
Qp be the topological closure
of the Galois closure of any embedding k → Qp. For σ :k →F let
Bσ
n(k) = ⟨[x]n | σ(x), 1 −σ(x) are in O∗
Cp ⟩ ⊆Bn(k) =
~Bn(k)
Ker(dn) ∩ Ker(~Pn)
.
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 21
Then
~Bn(k) →F
[x]n ↦→Pn,p(σ(x))
induces a map
Pσ
n,p :Bσ
n(k) →F
and the solid arrows in
Bσ
n(k) ∩ Ker(dn) /d31 /d127 /d47/d47
(n−1)!P σ
n,p
/d43/d43/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88
Ker(dn)
Ker(dn) ∩ Ker(~Pn)
Ψ n /d47/d47
(n−1)!P σ
n,p
/d39/d39
K2n−1(k)Q
regp◦σ∗
/d15/d15
F
form a commutative diagram.
Remark 4.15. It was conjectured in [5, Conjecture 1.14] that the dotted arrow
exists and that the full diagram commutes. This is known to hold for N [ζ]n if ζ is
anyN -th root of unity other than 1 (see Theorem 1.12 of loc. cit.).
Remark 4.16. The formulae for the complex and p-adic regulators involved in The-
orems 4.7 and 4.14 are stated up to sign in [19, Proposition 4.1] (with a n ormalizing
factor) and [5, Theorem 1.10(2) or Proposition 7.14] respectively, since they depend
on the choice of Ψ n, which is natural only up to sign. In the p-adic case it is clear
from [5, Proposition 7.10] that the sign is ( −1)n if the “relativity isomorphism” in
the p-adic case is normalized as in Proposition 5.7 of loc. cit. and the K-theoretic
relativity isomorphism as in (3.1) of loc. cit. corresponds to this unde r the naturality
of the regulator map. In order to see that the sign for the complex regulator is the
same with the same choice of Ψ n, we observe that one can use the techniques of [5,
Appendix A and Section 5] to describe the target for the complex re gulator of [z]n
withz in C\{0, 1} in [19] by means of a complex with the same formal structure as in
[5, Deﬁnition 5.2], but using R(n − 1)-valuedC∞-formsψ with logarithmic poles on
copies of ( P1
C\{1,z })j indexed by increasing functions f : [1,...,j ] → [1,...,n − 1].
Using the maps ψ ↦→
∫
(P1
C)j d arg(tf (1)) ∧ · · · ∧ d arg(tf (j)) ∧ψ for a j-form ψ with
index f : [1,...,j ] → [1,...,n − 1], and suitable normalizing factors, one writes
down an R-linear map Π ∞ on such forms, with values in R(n − 1), that vanishes
on exact forms and satisﬁes the analogous normalization condition a s Π = Π p in
[5, Proposition 5.7]. Moreover, as in [19, Section 2.5] one sees that t he subcom-
plex of forms on the component where j = n − 1 that vanish if some tl = 0 or
∞ gives a quasi-isomorphism under inclusion, and that the image of the r egulator
of [z]n is given by εn(z) as in Section 4 of loc. cit. (up to sign since one has to
use the correct formula for ωn, which can be obtained as in [5, Section 6]). Using
the computations on pages 236 and 237] of [19] one then sees tha t Π ∞ maps εn(z)
to ( −1)n(n − 1)!P♭
n(z), where P♭
n(z) = πn−1
(∑ n−1
l=0
1
l! (− log |z|)lLin−l(z)
)
, which
induces the same map on Ker(d n)/ Ker(dn) ∩ Ker(~Pn) as ( −1)n(n − 1)!Pn(z). Since
the relativity isomorphism in K-theory only depends on a choice of tl = 0 or ∞
for l = 1,...,n − 1 this shows that the signs in the formulae for the complex and
p-adic regulators of [z]n match for the same choice of Ψ n, and we adjust Ψ n so that
those signs disappear.
22AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
We conclude this section by considering Conjecture 3.18 when the ac tion of G
on E[G]π is Abelian.
Proposition 4.17. LetN ≥ 2, k = Q(µN ), G = Gal(k/Q) = ( Z/NZ)∗ wherea in
(Z/NZ)∗ corresponds toψa inG satisfyingψa(ζ) = ζa for all roots of unity ζ ink.
Assume that E contains a root of unity of order equal to the exponent of G and let
π inE[G] be the idempotent corresponding to an irreducible characte rχ ofG. Then
parts (1), (2) and (3) of Conjecture 3.18 hold for π andn ≥ 2 ifχ(−1) = ( −1)n−1.
Proof. That Conjecture 3.18(1) holds in this case is well-known (cf. [39]) bu t we
make it explicit here for part (3) of the conjecture (cf. [30, Prop osition 3.1]).
We deal with the case N = 2 later so by Remark 3.23(1) we may assume N >2
andχ primitive. The idempotent π corresponding to χ is |G|−1∑ ′N
a=1χ−1(a) ⊗ψa,
where the prime indicates that we sum over a that are relatively prime to N .
Note that by our assumption on χ(−1) and Proposition 3.8 the dimension of
K2n−1(ME
π ) equals 1. Fixing a generator ζ of µN ⊂ k∗ we use π, π(1 ⊗ζ) and
π(1 ⊗ [ζ]n) as basis vectors of E[G]π, ME
π and K2n−1(ME
π ) respectively, where we
simplify notation by writing [ ζ]n instead of Ψ n([ζ]n) as in Theorem 4.7.
In order to verify (1) in E ⊗Q C it suﬃces by Remark 3.19(2) to consider all
embeddings σ : E → C. If η = φ∞(ζ) with φ∞ as in Section 3 then the σ-
component of D(ME
π )1/2,∞ becomes
D(ME
π )1/2,∞
σ = |G|−1
N∑
a=1
′χ−1
σ (a)ηa =N |G|−1
( N∑
a=1
′χσ(a)η−a
) −1
by [36, (3) on p.84]. Similarly, by Theorem 4.7 the σ-component of Rn,∞(ME
π ) is
Rn,∞(ME
π )σ = (n − 1)! |G|−1
N∑
a=1
′χ−1
σ (a)Pn(ηa) = (n − 1)! |G|−1
N∑
a=1
′χ−1
σ (a)Lin(ηa)
because Pn(ηa) = (Li n(ηa) + χ−1
σ (−1)Lin(η−a))/2 by our assumption on χ(−1),
where Li n is computed using the power series in (4.1). They relate to the σ-
component of L(n,χ, Q) via L(n,χσ, Q) = ( n − 1)!−1Rn,∞(ME
π )σ/D(ME
π )1/2,∞
σ
according to (2) on page 172 of [16] with the correct sign in the expo nent of the
Gauss sum as used here (cf. [54, p. 421]). Since L(n,χσ, Q) ⁄= 0 this also shows
thatπ(1 ⊗ [ζ]n) gives a basis of K2n−1(ME
π ) as claimed.
Similarly, for (2) and (3) we consider all embeddings τ :E →
Qp. If φp(ζ) = ηp
then the τ -component of D(ME
π )1/2,p is N |G|−1(∑ ′N
a=1χτ (a)η−a
p )−1 and the τ -
component ofRn,p(ME
π ) equals (n−1)! |G|−1∑ ′N
a=1χ−1
τ (a)Pn,p(ηa
p ) by Remark 4.15,
independent of our assumption on χ(−1). By (3) on page 172 of [16] we have
Lp(n,χτω1−n
p , Q) = (n − 1)!−1Eulp(k,χτ, Q)Rn,p(ME
π )τ/D(ME
π )1/2,p
τ .
Therefore Conjecture 3.18(1)-(3) hold with e(n,M E
π ) = ep(n,M E
π ) in Q∗ ⊆E∗.
Now assume that N = 2 so that χ is the trivial character 1, π = 1 and n ≥ 2
is odd. Taking 1, 1 ⊗ 1 and 1 ⊗ [−1]n as bases of E[G] = E, ME
π = E ⊗ Q and
K2n−1(Q)E we ﬁnd from Theorem 4.7, (4.1), (4.2) and (4.4) that
L(n, 1, Q) = ζ(n) = 2n−1
1 − 2n−1Pn(−1) = 2n−1
(n − 1)!(1 − 2n−1)Rn,∞(ME
1 ),
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 23
again proving that [ −1]n gives a basis for K2n−1(Q)Q. Coleman proves that
Lp(n,ω 1−n
p , Q) = (1 −p−n) lim
x→1
′ Lin,p(x)
where the limit is taken in any subﬁeld of Cp that is of ﬁnite ramiﬁcation degree
over Qp. But by (4.12) and (4.13) we can rewrite this as
Lp(n,ω 1−n
p , Q) = (1 −p−n)2n−1
1 − 2n−1 Pn,p(−1) = (1 −p−n)2n−1
(n − 1)!(1 − 2n−1)Rp
n,∞(M1).
□
Remark 4.18. The π in the proof of Proposition 4.17 are primitive in the sense
of Deﬁnition 3.13. So, by Remarks 3.21(4) and 3.23(1), if Conjectur e 3.18 applies
to π inE[G], then parts (1), (2) and (3) of it hold for π for any E if the action on
E[G]π is Abelian. In particular, parts (1) and (2) of Conjecture 2.17 hold f or any
totally real Abelian number ﬁeld by Remark 3.21.
Remark 4.19. Computer calculations show that Lp(n,ω 1−n
p , Q) is in Q∗
p when
p = 2,..., 19 and n = 2,..., 20 is odd, verifying Conjecture 2.17(3) in those cases.
Similarly, with notation and assumptions as in Proposition 4.17, for the 470 primi-
tive charactersχ of Gal(Q(µN )/Q) = ( Z/NZ)∗ with 2 ≤N ≤ 50,Lp(n,χ ⊗ω1−n
p , Q)
lies in (E ⊗Qp)∗ for those values of p andn = 2,..., 20 wheneverχ(−1) = ( −1)n−1.
Thus Conjecture 3.18(4) also holds in those cases.
5. Computing K-groups in practice
Let n ≥ 2. It follows from Theorem 4.7 that Zagier’s approach as described
in Section 4 can be used to obtain at least some part of K2n−1(k)Q. Using the
notation introduced in Section 4, in order to carry this approach ou t in practice
one starts with two sets S ⊆S′ of primes of Ok and considers only [ x]∼
n where x is
anS-unit and 1 −x is an S′-unit. When we consider several hundred of such [ x]∼
n ’s
(and avoid using both [ x]∼
n and [1/x]∼
n since [x]n + (−1)n[1/x]n = 0 as mentioned
in Section 4) this method is well suited to computer calculations. The o nly point
in Zagier’s approach that cannot be carried out algebraically is to det ermine which
elements in Ker( ˜dn) are actually in Ker( ˜dn) ∩ Ker(~Pn). This is done using standard
methods for ﬁnding linear relations between the ~Pn(αj)’s for a basis {αj} of Ker(˜dn)
with small integral coeﬃcients. Typically, we used about the ﬁrst 50 decimals after
the decimal point of all the polylogarithms of all elements of k involved in the αj
embedded into C in all possible ways. The relations that were found this way were
then veriﬁed to hold up to at least 30 additional decimal places. As a ﬁ nal check,
when Ker(dn) had the same rank as K2n−1(k) the number q in (2.4) (but now using
the regulator ~Vn(k) for the subgroup of K2n−1(k)Q we obtained rather than Vn(k);
cf. Remark 2.19) was computed with a working precision of up to 120 d ecimals. It
turned out that its reciprocal looked rational rather convincingly .
For example, for the cubic ﬁeld k = Q[x]/(x3 −x2 − 3x + 1) with discriminant
148, one of the ﬁelds used in Example 7.1, we ﬁnd for ζk(n)|Dk|1/2/~Vn(k) the values
− 1.7531044558071585098612125639152666179693206722 × 10−2 (n = 3)
− 4.1170685884062518549452525064367732455835167754 × 10−9 (n = 5)
24AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
with reciprocals
− 57.041666666666666666666666666666666666666666662 ( n = 3)
− 242891265.59999999999999999999999999999999999998 ( n = 5).
As the calculation of a basis of K2n−1(k)Q, using the method outlined above,
tends to take (substantially) longer when [ k : Q], the absolute value of the discrim-
inant of k, or n increase, we describe two straightforward methods to reduce th is.
They, and most of our arguments below, will rely on Remark 3.22.
Method 5.1. Ifk is an Abelian extension of Q, hence is contained in a cyclotomic
ﬁeld k′, then we can ﬁnd K2n−1(k)Q by computing K2n−1(k′)Q as in Example 4.10
and applying Remark 3.22 (using Remark 4.9 ).
Since parts (1), (2) and (3) of Conjecture 3.18 are known for all id empotents of
E[G] to which it applies if G is Abelian by Remark 3.21 and Proposition 4.17, this
will not be used for verifying Conjecture 3.18. Instead, in the case s that we shall
consider we rely on the following method in order to ﬁnd the K-groups.
Method 5.2. Letk/Q be Galois with Galois group G, E/Q any extension, and M
an irreducible E[G]-module in K2n−1(k)E. If H is a subgroup of G with MH ⁄= 0
thenM ⊆E[G]·K2n−1(kH )Q. If for every irreducible M we can take H ⁄= {e}, then
we reduce to ﬁnding K2n−1(l)Q together with the action of G on it inside K2n−1(k)Q
for proper subﬁelds l of k.
We now discuss in Examples 5.3, 5.5 and 5.7 how to use Method 5.2 for cer tain
Galois extensions k/Q. In the decomposition of K2n−1(k)E according to central
idempotentsπi ofE[G] as in Section 3 we concentrate on those primitive central πi
for which the action on E[G]πi is not Abelian and describe corresponding primitive
idempotents π (as in Deﬁnition 3.13(2)) for later use. Due to restrictions on when
we can calculate the p-adicL-functions numerically (see Section 6) we only consider
k that are Abelian over a quadratic subﬁeld. Of course Proposition 3.1 2 describes
when Conjecture 3.18 applies to π, but we work out the structure of the K-groups
and the Galois action in more detail.
Example 5.3. Let k/Q be an S3-extension with quadratic subextension q. With
E = Q and σ in G of order three, π1 = (e +σ +σ2)/3 and π2 = 1 −π1 are
orthogonal central idempotents with π2 primitive (as in Deﬁnition 3.13(2)). In
Q[G] = Q[G]π1 ⊕ Q[G]π2 the ﬁrst summand consists of Abelian representations
of G and the last of two copies of the irreducible 2-dimensional represen tation V
of G. A corresponding primitive idempotent for π2 is π =π2πH for any subgroup
H = ⟨τ ⟩ of G of order 2 where πH = (e +τ )/2.
By Remark 3.22 we have π1K2n−1(k)Q =K2n−1(q)Q so that
(5.4) K2n−1(k)Q =K2n−1(q)Q ⊕π2K2n−1(k)Q.
The last summand is a Q[G]-module isomorphic to Vtn for some tn ≥ 0. As
V =πV ⊕τ ′πV for any τ ′ ⁄=τ of order 2, we ﬁnd, if c =kH ,
π2K2n−1(k)Q =π2K2n−1(c)Q ⊕τ ′π2K2n−1(c)Q
again by Remark 3.22. So we reduce to the calculation of K2n−1(q)Q andK2n−1(c)Q
together with the action of G on the latter.
A dimension count in (5.4) using Theorem 2.2 determines tn. We distinguish
two cases.
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 25
Case 1. If q is real then tn = 0 for n even and 2 for n odd.
Case 2. If q is imaginary then tn = 1.
Conjecture 3.18 applies to π when tn = 2.
Example 5.5. Letk/Q be a D8-extension where D8 = ⟨σ,τ |σ4 =τ 2 = (στ )2 =e⟩.
We ﬁx an isomorphism G = Gal(k/Q) ∼
=D8 and use notation as in Figure 5.1.
{e}
/d111/d111/d111/d111/d111/d111/d111/d111/d111/d111/d111
/d127/d127/d127/d127/d127/d127
/d63/d63/d63/d63/d63/d63
/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79
⟨τ ⟩ ⟨σ2τ ⟩ ⟨ σ2⟩ ⟨στ ⟩ ⟨σ3τ ⟩
⟨τ,σ 2⟩
/d63/d63/d63/d63/d63/d63
/d127/d127/d127/d127/d127
⟨σ⟩ ⟨στ,σ 2⟩
/d63/d63/d63/d63/d63
/d127/d127/d127/d127/d127
D8
/d63/d63/d63/d63/d63/d63
/d127/d127/d127/d127/d127/d127
k
/d111/d111/d111/d111/d111/d111/d111/d111/d111/d111/d111/d111/d111
/d127/d127/d127/d127/d127/d127
/d63/d63/d63/d63/d63/d63
/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79/d79
k1 k2 k3 k4 k5
q1
/d63/d63/d63/d63/d63/d63
/d127/d127/d127/d127/d127/d127 q2 q3
/d63/d63/d63/d63/d63/d63
/d127/d127/d127/d127/d127/d127
Q
/d63/d63/d63/d63/d63/d63
/d127/d127/d127/d127/d127/d127
Figure 5.1. The subgroups of G =D8 and their ﬁxed ﬁelds in k/Q.
Then Q[G] = Q[G]π1⊕Q[G]π2 whereπ1 = (1+σ2)/2 andπ2 = 1 −π1 are orthogonal
central idempotents. The ﬁrst term is an Abelian representation o f G and the
second as a Q[G]-module is isomorphic to V 2 for V the irreducible 2-dimensional
representation ofG over Q. Then π2 is a primitive central idempotent andπ =π2πH
a corresponding primitive idempotent if we let H = ⟨τ ⟩ and πH = (1 + τ )/2.
Since π1K2n−1(k)Q =K2n−1(k3)Q by Remark 3.22, for K2n−1(k)Q we ﬁnd
(5.6) K2n−1(k)Q =K2n−1(k3)Q ⊕π2K2n−1(k)Q
with the second term a Q[G]-module isomorphic with Vtn for some tn ≥ 0. If τ ′
in G has order two and does not commute with τ then V = πV ⊕τ ′πV , so by
Remark 3.22 we obtain
K2n−1(k)Q =K2n−1(k3)Q ⊕π2K2n−1(k1)Q ⊕τ ′π2K2n−1(k1)Q
and we reduce to the calculation of K2n−1(k3)Q andK2n−1(k1)Q together with the
action of G on the latter.
We can ﬁnd tn by counting dimensions in (5.6), and distinguish three cases.
Case 1. Fork3 and k totally real tn = 0 for n even and tn = 2 for n odd.
Case 2. Fork3 totally real but k not tn = 2 for n even and tn = 0 for n odd.
Case 3. Fork3 not totally real tn = 1.
Again Conjecture 3.18 applies to π when tn = 2.
Example 5.7. Let k/Q be an S3 × Z/3Z-extension, identify G = Gal(k/Q) and
S3 × Z/3Z via a ﬁxed isomorphism, and choose a generator σ of A3 ⊂ S3. Let q
be the quadratic subﬁeld of k, s′ the ﬁxed ﬁeld of A3 × {0}, s′′ the ﬁxed ﬁeld of
{e} × Z/3Z and si for i = 1, 2 the ﬁxed ﬁeld of Hi = ⟨(σ,i )⟩.
If E is an extension of Q that contains a primitive third root of unity ζ3 then
(5.8)
E[G] = E[G]π1 ⊕E[G]π2 ⊕E[G]π3 ⊕E[G]π4
∼
=E[Z/6Z] ⊕W 2
1 ⊕W 2
ζ3 ⊕W 2
ζ2
3
26AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
where
π1 = ((e, 0) + (σ, 0) + (σ2, 0))/3
π2 = (1 −π1)((e, 0) + (e, 1) + (e, 2))/3
π3 = (1 −π1)((e, 0) +ζ2
3 (e, 1) +ζ3(e, 2))/3
π4 = (1 −π1)((e, 0) +ζ3(e, 1) +ζ2
3 (e, 2))/3
are orthogonal central idempotents of E[G] satisfying π1 +π2 +π3 +π4 = (e, 0), and
Wa is the irreducible representation of G given by (ρ,m )(v) = amρ(v) for v in the
irreducible 2-dimensional representation of S3. With πHi = 1
3
∑
h∈Hih, a primitive
idempotent corresponding to the primitive central idempotent πj (j = 3, 4) is
π =πjπHi .
Using Remark 3.22 for A3 × {0} and {e} × Z/3Z we see that
K2n−1(k)E =π1K2n−1(k)E ⊕π2K2n−1(k)E ⊕π3K2n−1(k)E ⊕π4K2n−1(k)E
=K2n−1(s′)E ⊕ (1 −π1)K2n−1(s′′)E ⊕π3K2n−1(k)E ⊕π4K2n−1(k)E.
Because Wa =WH1
a ⊕WH2
a when a ⁄= 1 we have
πjK2n−1(k)E =πjK2n−1(s1)E ⊕πjK2n−1(s2)E (j = 3, 4)
so that we reduce to the calculation of K2n−1(s)Q for the sextic subﬁelds s of k,
together with the action of G when s =s′′,s1 or s2.
We have π3K2n−1(k)E ∼
=Wtn
ζ3 and π4K2n−1(k)E ∼
=Wtn
ζ2
3
for the same tn as one
sees by taking E = Q(ζ3) and considering the obvious action of Gal( E/Q) on E[G].
Since the dimension of (1 −π1)K2n−1(s′′)E was obtained in Example 5.3 we get the
following results for tn.
Case 1. Forq real tn = 0 when n is even and tn = 2 when n is odd.
Case 2. Forq imaginary tn = 1.
Conjecture 3.18 applies to π corresponding to πj (j = 3, 4) when tn = 2.
We ﬁnish this section with a result that was promised in Remark 3.20(1) . Note
that the assumption dim E(E[G]π) = dim E(πK2n−1(k)E) is not needed here: we
consider the regulator map with values in π(⊕τ :k→CE ⊗ R(n − 1))+ obtained
from (2.3), and use Beilinson’s regulator RBei comparing E-structures as in Re-
mark 3.24. Beilinson’s conjecture [2, Conjecture 3.4] states that the order of van-
ishing at s = 1 −n of L(s,χ ∨
π ⊗ id, Q) should be dim E(πK2n−1(k)E) and that the
ﬁrst non-vanishing coeﬃcient at s = 1 −n equals
L♯(1 −n,χ ∨
π ⊗ id, Q) = eRBei
for some e in E∗.
Proposition 5.9. Letk be aG =S3-extension (resp.G =D8-extension) of Q, and
let n ≥ 2. Then this conjecture holds for any primitive idempotent π corresponding
to π2 in Example 5.3 (resp. Example 5.5 ).
Proof. Clearly it suﬃces to prove this when E = Q. If G = S3 then by Re-
mark 3.21(3) we may assume πH =π1πH +π withπ1πH andπ =π2πH orthogonal
idempotents, where we use notation as in Example 5.3. The conjectu re for πH
follows from Theorem 2.2 for c = kH by the arguments of Remark 3.23 and the
functional equation (2.6) of ζc(s). Similarly, it holds for π1πH = 1
6
∑
g∈Gg, where
it corresponds to that theorem for kG = Q, and it follows that it must hold for π
as well. If G =D8 the argument is identical, using Theorem 2.2 for k1 and q1. □
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 27
6. Computing p-adic L-functions
We brieﬂy sketch the method used to compute values of p-adic L-functions of
1-dimensional Artin characters. Values of p-adicL-functions of characters of higher
dimension can then be deduced using (2.11). The method we employ is s omewhat
similar to, but more technical than the construction in [18], and gene ralizes the
one used in [45] to compute values of p-adic L-functions of real quadratic ﬁelds at
s = 1. Note that several modiﬁcations are necessary compared to [1 8] since the
construction there is for partial ζ-functions of the ray class modulo p whereas we
need to work with partial ζ-functions of arbitrary class groups. Also, we need to
replace p = 2 in a certain number of results by q = 4. We leave it to the careful
reader to check that these changes are indeed possible, or refer to the forthcoming
article [44] where the details of the actual method used will be given.
Let k be a totally real number ﬁeld and let d = [k : Q]. Let χ be a Qp-valued
1-dimensional Artin character of Gal(k/k). As in Section 2, we let q =p ifp is odd,
and q = 4 if p = 2.
By class ﬁeld theory, χ can be viewed as a character of a suitable ray class group
of k. We denote by f the conductor of χ, which is an integral ideal of k, and we
let g be the modulus with inﬁnite part g∞ consisting of all inﬁnite places of k,
and ﬁnite part g0 equal to the least common multiple of f and q. Let a1,..., ah
be representatives of the classes of the ray class group of k modulo g, and let
ζai(s), i = 1,...,h , be the corresponding partial ζ-functions. According to [40,
Chapter VII, p.526] we have, for any isomorphism σ : Qp → C,
h∑
i=1
σ ◦χ(ai)ζai (s) = Eulp(s,σ ◦χ,k )L(s,σ ◦χ,k ).
Since all ζai (m) are rational for integers m ≤ 0 by loc. cit. Chapter VII, Corol-
lary 9.9, we may identify them with σ−1(ζai (m)) in Qp. Thus for such m we have
(6.1)
h∑
i=1
χ(ai)ζai (m) = Eul ∗
p(m,χ,k )L∗(m,χ,k )
where L∗(m,χ,k ) and Eul ∗
p(m,χ,k ) are as in (2.7) and (2.8).
Now let β ⁄= 1 in Ok be such that
(1) β ≡ 1 (mod g0) and v(β)> 0 for every inﬁnite place v of k;
(2) Ok/(β) ≃ Z/bZ, where b = N (β) is the norm of the principal ideal ( β).
Scaling the measures obtained in [18, Lemme 4.4] for the ai we obtain Qp-valued
measures~λi (i = 1,...,d ) on Zd
p, depending on β and ai, such that for all integers
m ≤ 0,
(bm−1 − 1)ζai (m) = ( −1)dmN (ai)−m
∫
(x1 · · ·xd)−md~λi.
The proof of Lemma 4.3 of loc. cit. shows, contrary to the stateme nt of that lemma,
that the measures ~λi are supported on ( −1 +qZp)d. Therefore pulling back over
multiplication by −1 on Zd
p we obtain measures λi on Zd
p, supported on (1 + qZp)d,
such that, for the same m,
(6.2) ( bm−1 − 1)ζai (m) = N (ai)−m
∫
(x1 · · ·xd)−mdλi.
28AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XA VIER-FRA NC ¸ OIS ROBLOT
For a ﬁxed x in 1 + qZp the function s ↦→xs is deﬁned and analytic on Zp.
Since, in general, N (ai) will not be congruent to 1 modulo q, we do the following.
For any integer l and any integral ideal a of k that is coprime to p, the function
s ↦→ωp(a)l⟨Na⟩−s is an analytic Zp-valued function on Zp, whose value equals
N (a)−m at any integer m withm +l ≡ 0 (mod ϕ(q)). We deﬁne the p-adic partial
ζ-function of the class of ai by mapping s in Zp \ {1} to
ζp,ai (s) =
(
bs−1 − 1
) −1
⟨N(ai)⟩−s
∫ ′
(x1 · · ·xd)−sdλi,
where ′ indicates that we restricted the domain of integration to (1 + qZp)d.
Let Ψ i be the function deﬁned by the above integral, that is, for s in Zp,
Ψ i(s) =
∫ ′
(x1 · · ·xd)−sdλi.
Fora in Zp with |a − 1|p ≤q−1, and s in Zp, one can write a−s = expp(−s logp(a)),
where expp and logp are thep-adic exponential and logarithm functions respectively;
and thus the function s ↦→a−s can be expressed as a power series with coeﬃcients in
Zp, where the coeﬃcient of sm has absolute value at most q−mpm/(p−1). Developing
(x1 · · ·xd)−s in this way as a power series of s and using the fact that the measures
λi have bounded norm by [18, Lemme 4.2 bis], we see that Ψ i(s) can also be
expressed as a power series in Qp[[s]] where the absolute value of the coeﬃcient
of sm is at most Ciq−mpm/(p−1) for some Ci > 0. In the same way, the function
s ↦→ ⟨N(ai)⟩−s can be expressed as a power series in Zp[[s]] whose coeﬃcients
satisfy the same bounds. Similarly, since the only solution for s of bs−1 = 1 with
|s|<qp −1/(p−1) iss = 1, it follows from the p-adic Weierstrass preparation theorem
that the function s ↦→bs−1 − 1 can be expressed as the product of a power of p, the
polynomials − 1, and an invertible power series in Zp[[s]] with the absolute value of
the coeﬃcient of sm bounded by q−mpm/(p−1). Therefore ζp,ai (s) can be expressed
as the quotient of a power series in Qp[[s]] with the absolute value of the coeﬃcient
of sm bounded by C′
iq−mpm/(p−1) with C′
i > 0, and s − 1.
If we deﬁne p-adic functions of s,
(6.3) L(l)
p (s,χ,k ) =
h∑
i=1
ωp(ai)lχ(ai)ζp,ai (s) ( l modulo φ(q)),
then it follows from (6.1), (6.2), and the equality ζp,ai (m) = ωp(ai)mζai(m) for any
integerm ≤ 0, that
(6.4) L(l)
p (m,χ,k ) = Eul ∗
p(m,χ,k )L∗(m,χ,k )
for all non-positive m such that l +m ≡ 0 modulo ϕ(q). In particular, the p-adic
L-function of χ is given by Lp(s,χ,k ) = L(−1)
p (s,χ,k ). Moreover, its residue at
s = 1 is zero if χ is non-trivial because the functions ωp(ai)−1ζp,ai (s) all have the
same residue there by [18, Corollaire on page 388].
The estimates on the coeﬃcients of the power series expansions ab ove imply the
claims in Theorem 2.9(1). Through the p-adic Weierstrass preparation theorem
they also imply that the function in (2.11) can be written as the quotie nt of a
power series in Qp(χ)[[s]] that converges for s in Cp with |s| < qp−1/(p−1), and a
polynomial in Qp(χ)[s].
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS 29
We note in passing that if l is any integer then
Lp(s,χωl
p,k ) =
h∑
i=1
ωp(ai)l−1χ(ai)ζp,ai(s) = L(l−1)
p (s,χ,k ),
so that we obtain from (6.4) that
Lp(m,χωl
p,k ) = Eul ∗
p(m,χ,k )L∗(m,χ,k )
for all m ≤ 0 with l +m ≡ 1 modulo ϕ(q), as stated in Remark 2.13.
In order to compute L(s,χ,k ) for a ﬁxed s in Zp, it suﬃces to compute ζp,ai (s),
for which one mainly has to compute the Ψ i(s). The measures λi can be represented
as power series in d variables,
Fi(w1,...,w d) =
∑
n1,...,nd≥0
ai,n1,...,ndwn1
1 · · ·wnd
d ,
with (bounded) coeﬃcients
ai,n1,...,nd =
∫ (x1
n1
)
· · ·
(xd
nd
)
dλi
that can be computed using Shintani’s method [49], which is practical for calcula-
tions if the base ﬁeld k is Q or real quadratic. On the other hand, the function h
on Zp deﬁned by
x ↦→
{
x−s if x is in 1 + qZp,
0 otherwise ,
is continuous and thus admits a Mahler expansion ∑
n≥0cs,n
(x
n
)
, where the coeﬃ-
cients satisfy cs,n → 0 when n → ∞ and can be easily computed recursively. Then
we have
Ψ i(s) =
∫
h(x1) · · ·h(xd)dλi =
∑
n1,...,nd≥0
ai,n1,...,ndcs,n1 · · ·cs,nd.
Thus, by computing enough terms in the above sum, we can get a goo d approx-
imation of the integral, and therefore, putting everything togeth er, of the p-adic
L-function.
In order to apply this we make (2.10) explicit in the cases we are intere sted
in, writing L-functions of representations for the L-functions of the correspond-
ing characters. In particular, we write the classical L-functions of the irreducible
