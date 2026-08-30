---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-053-72-melvin-morton-expansions-and-rozanskys-ration
section_title: "Melvin-Morton expansions and Rozansky’s rationality theo rem. Rozan-"
section_number: 7.2
pages: 26-28
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the polynomial ring"
---
sky [74] proved that the colored Jones polynomials of a knot K can be repackaged
into one invariant J MMR
K ∈ Z[[q− 1,α 2]], which is an integer-coeﬃcient version of
the Melvin-Morton expansion [61]. (In fact, Rozansky prove d much stronger results
there, see below.)
Let
γ : Λ → Z[[q− 1,α 2]]
be the ring homomorphism induced by id Z[q,q−1,α2]. This is well-deﬁned since σ2k∈
(α2k, (q−1)2k) in Z[q,q −1,α 2] fork≥ 0. As mentioned in [17, Section 3.3], γ(JK)∈
Z[[q− 1,α 2]] is equal to the Rozansky’s integral version of the Melvin- Morton
expansion.
The ﬁrst half of the following proposition was mentioned in [ 17] without proof,
and implies that JK and J MMR
K have the same strength.
Proposition 7.2. The map γ is injective and non-surjective.
Proof. Let us prove injectivity. Let f = ∑ ∞
n=0fn(q)σn∈ Λ, where fn(q)∈ Z[q,q −1]
for n≥ 0, and suppose that γ(f ) = 0. We can express each σn as
σn =
n∑
k=0
gn,k(q)(2−q−q−1)2n−2kα2k,
where gn,k(q)∈ Z[q,q −1]. Hence, we obtain
γ(f ) =
∞∑
k=0
( ∞∑
n=k
fn(q)gn,k(q)(2−q−q−1)2n−2k
)
α2k.
Sinceγ(f ) = 0, we have
∞∑
n=k
fn(q)gn,k(q)(2−q−q−1)2n−2k = 0 (7.3)
for all k≥ 0.
One can show that gn,k(q) is not divisible by q−1. (Indeed, one can use induction
onn to show that gn,k(1)∈ Z is positive.) Using this fact and (7.3), one can prove
using induction that for any n,d≥ 0,fn(q) is divisible by (q− 1)d. Hence fn(q) = 0
for all n.
Non-surjectivity of γ can be veriﬁed in several ways. For example, let u : Z[[q−
1,α 2]]→ Z[[q− 1]] be the continuous Z[[q− 1]]-algebra homomorphism such that
u(α2) = 0. Then we have
uγ(Λ) = Z[q,q −1] ⊊ Z [[q− 1]] = u(Z[[q− 1,α 2]]).
It follows that γ is not surjective.
Rozansky [74] also proved that the coeﬃcient of ( q− 1)n of the integral Melvin-
Morton expansion of a knot K is a rational function in α2 with denominator a power
of the Alexander polynomial ∆ K(t)∈ Z[t +t−1] of K. (This result generalizes a
conjecture of Melvin and Morton [61], proved in [2].) More pr ecisely, Rozansky
proved that J MMR
K has the following power series expansion
J MMR
K =
∑
n≥0
PK,n(t)
∆ K(t)2n+1 (q− 1)n∈ Z[t +t−1, 1
∆ K(t) ][[q− 1]],
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 27
where PK,n(t)∈ Z[t +t−1] for n≥ 0. The PK,n(t) are uniquely determined by K
and n. Thus γ(JK) is contained in a much smaller ring than Z[[q− 1,α 2]]. Melvin
and Morton’s conjecture (essentially) states that
J MMR
K
⏐
⏐
q=1= 1
∆ K(t).
Thus we have PK,0(t) = 1.
The following conjecture (supported by some computer calcu lations) generalizes
Rozansky’s rationality theorem.
Conjecture 7.3. LetK be a knot and let d : N→{ 0, 1, 2,... } be a function which
vanishes for all but ﬁnitely many elements of N. Set
∆ d
K(t) =
∏
r∈N,d(r)>0
∆ K (tr)2d(r)−1∈ Z[t +t−1].
Then we have
∆ d
K(t)JK∈ Z[t +t−1,q,q −1] + Φ d(q)Λ .
Conjecture 7.3 implies that J MMR
K is contained in the image of the natural (in-
jective) homomorphism
lim
←−kZ[q,q −1,t +t−1, 1
∆ K(ti) (i≥ 1)]/((q)k)→ Z[[q− 1,α 2]].
Conjecture 7.3 also implies the following conjecture, in wh ich the case ζ = 1 is
Rozansky’s rationality theorem.
Conjecture 7.4. Letζ∈Z with r = ord(ζ). Let
γζ : Λ → Z[ζ][[α2,q−ζ]]
be the homomorphism induced by Z[q,q −1,α 2]⊂ Z[ζ][q,q −1,α 2]. Deﬁne PK,ζ,k (t)∈
Z[ζ][[α2]] for k≥ 0 by
γζ(JK) =
∑
k≥0
PK,ζ,k (t)
∆ K (tr)2k+1 (q−ζ)k.
Then we have PK,ζ,k (t)∈ Z[ζ][t +t−1].
Using the injectivity of γ = γ1, one can prove that the homomorphism γζ is
injective.
Conjecture 7.4 implies that
JK(t,ζ ) = PK,ζ,0(t)
∆ K(tr) ∈ 1
∆ K (tr) Z[ζ][t +t−1].
Some computer calculations support the following conjectu re.
Conjecture 7.5. We have
JK(t,−1) = ∆ K (−t)
∆ K(t2).
Thus we have PK,−1,0(t) = ∆ K(−t) in the notation of Conjecture 7.4.
