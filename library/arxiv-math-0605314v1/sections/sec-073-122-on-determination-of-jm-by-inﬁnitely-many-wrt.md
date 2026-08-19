---
doc_id: arxiv-math-0605314v1
doc_title: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO"
section_id: sec-073-122-on-determination-of-jm-by-inﬁnitely-many-wrt
section_title: "On determination of JM by inﬁnitely many WRT invariants. In this"
section_number: 12.2
pages: 39-40
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the"
---
subsection, we prove the following.
Proposition 12.2. IfZ ′⊂Z has no limit point, then the ring homomorphism
evZ ′ in (1.3) is not injective.
Here, recall from Section 1.2 that a “limit point” of a subset Z ′ ⊂ Zis an
element ξ∈Z such that there are inﬁnitely many ζ∈Z ′ adjacent to ξ. (Recall
thatξ andζ are adjacent if ord(ζξ −1) is a prime power.) Any ﬁnite subset Z ′⊂Z
has no limit point. There are many inﬁnite subset Z ′⊂Z without limit points, for
example{6i| i≥ 0}.
Proposition 12.2 shows that Conjecture 6.1 in our previous p aper [18] is false.
It follows that we can not prove, using only properties of ˆZ[q], that the τζ (M ) for
any inﬁnitely many ζ ∈Z would determine JM and hence τ (M ). It should be
remarked that it is still open whether the WRT invariants at a ny inﬁnitely many
roots of unity determine JM or not.
Proposition 12.2 follows easily from Proposition 12.3 belo w. Two elements m,n∈
N are said to be adjacent to each other (written m⇔n) if m/n =pe withp prime
and e∈ Z. For a subset S⊂ N, a limit point of S is deﬁned to be an element
m∈ N which is adjacent to inﬁnitely many elements of S. Note that if ζ,ξ ∈Z
are adjacent, then ord( ζ) and ord( ξ) are adjacent. (One can deﬁne a topology on
N whereS⊂ N is open if for each m∈S,S contains all but ﬁnitely many elements
adjacent to m. The map ord : Z→ N, ζ↦→ord(ζ), turns out to be a continuous
map.)
Proposition 12.3. If S⊂ N is a subset with no limit point, then the ring homo-
morphism
evS : ˆZ[q]→
∏
m∈S
Z[q]/(Φ m(q)), f (q)↦→(f (q) mod (Φ m(q)))m∈S,(12.1)
is not injective.
Proof. Let S ={m1,m 2,... } with 1 ≤ m1 < m2 <··· . Choose a∈ N\S. We
construct f (q)∈ ˆZ[q] such that f (q)∈ (Φ mi(q)) for all i≥ 1 and f (q)⁄∈(Φ a(q)).
For this purpose, it suﬃces to construct a sequence fi(q)∈ Z[q], i≥ 1, such that
40 KAZUO HABIRO
(1) fi(q)→ 1 in ˆZ[q] as i→∞ (i.e., for each j there is i such that fk(q)− 1 is
divisible by (q)j for all k≥i),
(2) fi(q)∈ (Φ mi(q)) for i≥ 1,
(3) fi(q)⁄∈(Φ a(q)) for i≥ 1.
Suppose there is such a sequence fi(q). Set f (q) = ∏
i≥1fi(q), which is well deﬁned
by (1). By (2) we have f (q)∈ (Φ mi(q)) for all i≥ 1. (1) and (3) implies that
f (q)⁄∈(Φ a(q)), hence f (q)⁄= 0.
Now we show that there is a sequence fi(q) as above. For i≥ 0, set
bi = max({0}∪{ b∈ N|b<m i; b⁄⇔mj for all j≥i}).
The assumption in the statement implies:
(a) 0 ≤b1≤b2≤··· and lim ibi =∞,
(b) if 1 ≤n≤bi and i≤j, then mj and n are not adjacent.
It follows from (b) that, for i≥ 1, there is ui(q)∈ Z[q] such that ( q)biuq(q)≡ 1
mod (Φ mi (q)). Set
fi(q) =
{
Φ mi(q) if bi<a,
1− (q)biui(q) if bi≥a,
(2) and (3) can be easily veriﬁed. (1) follows from (a).
Proof of Proposition 12.2. Set S ={ord(ζ)| ζ∈Z ′}⊂ N. By assumption, S has
no limit point. Hence, by Proposition 12.3, ev S is not injective. It follows that ev Z ′
is not injective, since it factors through ev S.
Remark 12.4. By slightly modifying the deﬁnition of fi(q) in the proof of Proposi-
tion 12.3, we see that if S⊂ N has no limit point and if d : S→{ 0, 1,... } is any
function, then the ring homomorphism
gS,d : ˆZ[q]→
∏
m∈S
Z[q]/(Φ m(q)d(m)), f (q)↦→(f (q) mod (Φ m(q)d(m)))m∈S,
is not injective. (It suﬃces to replace fi(q) with the d(mi)th power of the original
deﬁnition of fi(q).) Using this, one can show that if Z ′⊂Z has no limit point and
if d : Z ′→{ 0, 1,... } is any function, then the ring homomorphism
gZ ′,d : ˆZ[q]→
∏
ζ∈Z ′
Z[q]/((q−ζ)d(m)), f (q)↦→(f (q) mod (( q−ζ)d(ζ)))ξ∈Z ′,
is not injective.
Remark 12.5. In the situation of Proposition 12.3, suppose moreover that the ele-
ments of S are pairwise non-adjacent. Then the homomorphism ev S is surjective.
Since S ={6n| n≥ 0} is such an example of S and it is inﬁnite, it follows that
ˆZ[q] is not Noetherian.
