---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-009-6-a-central-extension-of-bmw
section_title: "A central extension of BMW"
section_number: 6
pages: 24-32
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
6.1. Deﬁnition. We deﬁne an algebra Fn over A = Q [a,x,x−1]/(a2 = 1) by generators
s1,...,s n−1, e1,...,e n−1,C and relations
(i) sisi+1si =si+1sisi+1, sisj =sjsj
(ii) (si−a)(s2
i−xsi + 1) = 0
(iii) ei =a
(s−1
i +si
x − 1
)
(iv) siei =aei
(v) eisi+1ei =ei +C
(vi) eisi−1ei =ei +C
(vii) eis−1
i+1ei =ei +C
(viii) eis−1
i−1ei =ei +C
(ix) siC =Csi =aC.
Letting ˜δ = 2−ax, we have e2
i = ˜δx−1ei. Immediate consequences of these relations are
s−1
i C = Cs−1
i = aC, eiC = Cei = x−1˜δC, C2 = (x−2˜δ2a−x−1˜δ)C = x−1˜δ(ax−1˜δ− 1)C =
2x−2˜δ(a−x)C. Note that, in the specializations x =a and x = 2a, we have C2 = 0.
The following is easily checked
Proposition 6.1. (i) The S††-algebra Fn⊗A S†† is a quotient of Hn⊗R S†† through
si↦→ si and A→ S†† being given by x↦→ b +c. This quotient factorizes through
BMW††
n .
MARKOV TRACES ON THE BMW-ALGEBRAS 25
(ii) There is a surjective morphism ofS††
± -algebrasFn⊗AS††
± ↠BMW±
n⊗S±S††
± satisfying
si↦→si, ei↦→ei, C↦→ 0. Its kernel is the linear span of C.
(iii) The automorphism and antiautomorphism of A-algebras of the group algebra ABn
deﬁned by si↦→s−1
i induce an automorphism and a antiautomorphism of Fn.
(iv) Every Markov trace (tn) factorizing throughFn is uniquely determined byt3(1),t3(s1)
and t3(s1s2).
Proof. We start with (i). Only the fact that we have a factorization throughBMW††
n requires
a justiﬁcation. According to proposition 4.3, it is suﬃcient to show that s1e2s1 ands−1
2 e1s−1
2
are mapped to the same element. Using the same computations as in the proof of proposition
3.3 we easily get that both are sent to xe1s−1
2 +axC +xe2s1−s2e1s−1
2 , and this proves the
claim. (ii) is easy, because the linear span of C is clearly a two-sided ideal of Fn. (iii) is
easily checked from the deﬁning relations of Fn. We now prove (iv). From the arguments of
proposition 5.3 one easily gets that such a Markov trace is uniquely determined byt3 together
with the collection of the tn(C), since C = en−1snen−1−en−1. Because Csn = aC we get
atn+1(C) = tn(C), whence the Markov trace is uniquely determined by t3, and therefore by
t3(1), t3(s1) together with t3(s1s2) by proposition 5.5.
□
Corollary 6.2. If (tn) is a Markov trace factoring through Fn, then the associated link in-
variant does not distinguish mirrors and does not detect non-invertible links.
Proof. This follows from the items (iii) and (iv) of the proposition : the mirror of the closed
braid ˆβ is the closure of the image of β under the automorphism si ↦→ s−1
i , the mirror
of the inverse is the closure of the image of β under the antiautomorphism si↦→ s−1
i . Since
t3(s1) =t3(s−1
1 ),t3(1) =t3(1−1),t3(s1s2) =t3(s−1
1 s−1
2 ), such a Markov trace coincides by (iv)
with its composite with the (anti-)automorphisms deﬁned in (iii), whence the conclusion. □
Proposition 6.3. If (tn) is a Markov trace factoring through Fn, then
(i)∀n≥ 3 tn+1(C) =atn(C)
(ii)∀n≥ 2 tn+1(C) =atn+1(1)−ax−1(˜δ + 2)tn(1) + 2a˜δx−2tn−1(1)
(iii) For all n≥ 1,
tn+3(1) =
(
a +
˜δ + 2
x
)
tn+2(1)− 1
x
(
2
˜δ
x +a(˜δ + 2)
)
tn+1(1) + 2a
˜δ
x2tn(1)
Proof. (i) is trivially deduced fromsnC =aC and the Markov property. FromC =en−1snen−1−
en−1 we gettn+1(C) =tn+1(e2
n−1sn)−t3(en−1) = ˜δx−1tn+1(en−1sn)−tn+1(en−1) = ˜δx−1tn(en−1)−
tn+1(en) by the Markov property and because en−1 and en are conjugates. Expanding ei =
(a/x)(si+s−1
i )−a and using the Markov property again we gettn+1(C) = ˜δx−1(2a/xtn−1(1)−
atn(1))− (2a/xtn(1)−atn+1(1)) =atn+1(1)−ax−1(˜δ + 2)tn(1) + 2a˜δx−2tn−1(1), namely (ii).
By (i) we know tn+1(C) = atn+2(C) hence, by (ii), we get tn+1(C) = atn+2(C) = tn+2(1)−
x−1(˜δ+2)tn+1(1)+2 ˜δx−2tn(1) hence, again by (ii),tn+2(1)−x−1(˜δ+2)tn+1(1)+2 ˜δx−2tn(1) =
atn+1(1)−ax−1(˜δ + 2)tn(1) + 2a˜δx−2tn−1(1) hence
tn+2(1) =
(
a +
˜δ + 2
x
)
tn+1(1)− 1
x
(
2
˜δ
x +a(˜δ + 2)
)
tn(1) + 2a
˜δ
x2tn−1(1)
which proves (iii). □
26 Ivan Marin & Emmanuel Wagner
At this stage, C could well be 0. We now prove that this is not the case.
6.2. A genuine extension of BMW±
n . Using the abelianization morphism Bn ↠ Z we can
deﬁne a 3-dimensional Hn⊗RS††-module by
si↦→


a 1 0
0 b 1
0 0 b−1


It is easily checked thatR1 acts by 0 in this module, hence we get a 3-dimensional BMW††
n -
module. We get that ei =a((si +s−1
i )/x− 1) is mapped to


(ab−1)(−b+a)
b2+1
ab−1
b2+1
b
b2+1
0 0 0
0 0 0


while eisi+1ei−ei and eis−1
i+1ei−ei are both mapped to
2ab−b2− 1
(b2 + 1)2


(ab− 1)(a−b) ab− 1 b
0 0 0
0 0 0


This proves that this module induces a Fn⊗A S††-module, and therefore a Fn⊗A S††
± -
module, which do not factorize through BMW±
n . It follows that BMW††
n andFn are genuine
extensions of the Birman-Wenzl-Murakami algebra. We need to prove a similar result for
the specializations appearing in the previous section. However, for one of them the above
argument does not work, because it corresponds to a root of ab−b2− 1. Nevertheless, we
know by proposition 4.2 (iii) that BMW††
n is ﬁnitely generated as a S††-module. Because
of this, the dimension of every specialization is at least the dimension of BMW††
n over the
ﬁeld of fractions of S†† (this classical fact follows for instance from Nakayama’s lemma, by
replacing S†† by its localization at the deﬁning ideal of the specialization). This proves the
following.
Proposition 6.4. For every morphism λ : S††→ C , BMW††
n ⊗λ C and (Fn⊗AS††)⊗λ C
have dimension at least 1 + dimBMW +
n .
Corollary 6.5. For every morphism λ :S†† ↪→ C , the image of C inside (Fn⊗AS††)⊗λ C
is nonzero.
Corollary 6.6. The A-moduleFn is free of rank 1 + dimBMW±
n
Proof. Let us denote A± = Q [a,x,x−1]/(a∓ 1) ≃ Q [x,x−1]. By the natural A-module
decomposition A≃A+⊕A− it is enough to prove that F±
n =Fn⊗AA± is a free A±-module
of rank 1+N withN = dimBMW±
n . Now notice that BMW±
n⊗S±S††
± is actually deﬁned by
a presentation with coeﬃcients in A±, and that the corresponding A±-form is free of rank N
by [19]. Therefore, as in proposition 6.1 (ii), we get a surjective A±-morphismeF±
n ↠AN
± by
mappingC to 0. Letting s± denote a section of this morphism, we get a surjective morphism
u± : A1+N
± ≃ (A±C)⊕AN
± → F±
n by (λC,m )↦→ λC +s±(m). Letting K± denote the
quotient ﬁeld of A±, it follows that u±⊗A± K± is surjective. But proposition 6.4 implies
that F±
n ⊗A±K± has dimension 1 +N. Therefore the source and target of u±⊗A±K± have
MARKOV TRACES ON THE BMW-ALGEBRAS 27
the same dimension hence u±⊗K± is injective. Since the source of u± is a free module this
implies that u± is injective and this proves the claim.
□
Corollary 6.7. The natural algebra morphism Fn→Fn+1 is injective.
Proof. As before, using the notations of the previous proof, it is equivalent to show that
the natural maps F±
n → F±
n+1 are injective. This is true because the following diagram of
horizontal short exact sequences is commutative, and because its two extremal vertical arrows
are known to be injective.
0 //A±C //

F±
n //

BMW±
n //

0
0 //A±C //F±
n+1 //BMW±
n+1 // 0
□
6.3. The algebra Fn as a specialization of ~BMW n. The goal of this section is to prove
the following theorem.
Theorem 6.8. The morphism of S††-algebrasBMW††
n →Fn⊗AS†† induces an isomorphism
after tensorisation by S††[(x + 2a)−1].
We deﬁneSi =eisi+1ei−ei,S′
i =eis−1
i+1ei−ei∈Hn⊗RS††, and alsoˆRi = (sisi+1si)Ri(sisi+1si)−1,
and similarly ˆSi = (sisi+1si)(Si)(sisi+1si)−1. The two formulas below hold inside H3⊗S††
and can be checked computationally by using the morphism Φ H3, as we did for lemma 4.6
(these formulas were found by a similar procedure, too).
(6.9)
S1−S′
1 = 1
xR1s2− 1
x2s−1
1 R1s2− 1
x2s1R1s2 = 1
x2 (x−s−1
1 −s1)R1s2 = 1
(b +c)2 (s1−b)(s1−c)s−1
1 R1s2
(6.10) 2 x2
(
S1− ˆS1
)
= (x−s−1
1 −s1)R1s2−R 1 + (−x +s−1
2 +s2)ˆR1s1 +ˆR1
We now want to show that S1−S 2 also belongs to the ideal generated by R1. For this
we need to work inside H4⊗S††. Since the computations become quite complicated, we
specialize at a = 1. There is no loss of generality in doing this, as we justify it now. The
natural decomposition S†† =S††
+⊕S††
− induces a Q -vector space decomposition Hn⊗RS†† =
H+
n ⊕H−
n with projectors p+,p− given by the multiplication by ( a− 1)/2 and (a + 1)/2.
It is straightforward to check that the involutive automorphism E† of Hn⊗R S†† induced
by ˆE and η (see the notations of proposition 4.9 and before) exchanges H+
n and H−
n , maps
Si↦→−S i,Ri↦→−R i and intertwines p+ and p− up to a sign (that is: E†◦p+ =−p−◦E†,
E†◦p− = −p+◦E†). Because of this, any expression of p+(S1−S 2) = (S1)+− (S2)+
immediately yields an expression of p−(S1−S 2) and therefore of S1−S 2.
We now use the fact thatH4 is a freeR-module of rank 648 in order to do explicit computa-
tions. More precisely, the computations are made as follows. First of all, we build a basis ofH4
as follows. We consider the collectionB2 of 27 words insi,s−1
i given in proposition 4.8 of [16].
They form a basis ofH4 as aH3-module. Together with the list of 24 wordsB1 given by propo-
sition 2.1 (ii), which induces a basis of H3, we get a collectionB3 ={g1g2; (g1,g 2)∈B 1×B 2}
28 Ivan Marin & Emmanuel Wagner
of 24× 27 = 648 words which induces a basis of H4. From this and the implicit rewriting
rules of [16] we build an explicit regular representation H4 ↪→ Mat 648(R) and therefore an
injective map ΦH4 :H4⊗RS††
+→Mat 648(S††
+ ), that we use in order to check equalities.
Letting (S1)± =S±, we let (S2)± = (s1s2)(S1)±(s1s2)−1. Inside H4⊗RR/(a− 1,y− 1)
we ﬁnd that 2(x + 2)2x4((S1)+− (S2)+) can be expressed as a sum of 161 terms obviously
belonging to I4, see Figures 5, 6, 7.
These terms were found as follows. For computational reasons (and the limited power of
the computers we have at disposal) it is too diﬃcult to compute the linear span of I4 inside
the ﬁeld of fractions Q (x) or Q (b), so we need to circumvent this obstacle by computing
inside specialisations in x. For some speciﬁc value of x we get a basis B1 of the linear span
of the image of I4 inside Q 648. The one we get is made of terms of the form gR1g′ where
g,g′ are products of elements si,s−1
i (chosen inside the basis of H4 mentionned above), or
gR2g′ or gˆR1g′ or gˆR2g′. The same elements form a basis of the specializations of H4 for
inﬁnitely many values of x. We chose a number of values for which we got an expression
ofS1−S 2 as linear combination of the elements of B1. Assuming that these coeﬃcients
should be rational fractions in x whose denominators have low degree, we get these rational
fractions by interpolation. We then check that the corresponding equality is correct by direct
computation insideH4⊗Q (x). It so happens that the choices we made in this process provide
an expression of (x− 1)(x + 2)2(x2 +x− 1)x4(S1−S 2). Recall that, in order to deal with the
odd cases of the previous section, we need to specialize at x = 1. For this alone, we need to
start again with this specialization, and we get this time, as a linear combinations of another
basisB2, a polynomial expression of ( x + 1)(x + 2)2x4(S1−S 2). By Bezout theorem both
results combined provide an expression of 2(x + 2)2x4((S1)+− (S2)+) as a linear combination
ofB1∪B 2, and this is the result that is expressed here (the cardinality of B1∪B 2 is 161).
Needless to say, one could have hoped to get a nicer expression. Unfortunately we failed
to ﬁnd one.
Thex4 factor in this expression prevents the specialization x = 0, which is to be expected.
Thex+2 factor prevents the specializationx =−2a, which was not expected, but is explained
by the proposition below. This proposition implies that the morphism under consideration
does not induce an isomorphism under this specialization, since the algebras BMW±
4 have
dimension 105. Note that ( S††
± )/(x + 2a)≃ Q [b]/(b +b−1± 2)≃ Q [b]/(b± 1)2.
Proposition 6.11. The Q -algebrasBMW††
4 ⊗S†† Q [b]/(b± 1) both have dimension 115.
Proof. Direct computations prove that their deﬁning ideals insideH4⊗RR/(a∓1,b±1,c±1)≃
Q 648 have dimension 533, hence the corresponding quotients have dimension 648 − 533 =
115. □
We will elaborate a bit more on the casex =−2a in section 6.8. For now, letπ :BMW††
n ⊗
S††[(x + 2a)−1] ↠ Fn⊗A S††[(x + 2a)−1] be the obvious projection. We need to ﬁnd a
section f such that f◦π = Id, and for this it is enough to check that the natural projection
f :Hn⊗S††[(x+2a)−1] ↠BMW††
n ⊗S††[(x+2a)−1] factorizes throughFn⊗AS††[(x+2a)−1].
Using the decomposition S†† =S††
+⊕S††
− and the Galois automorphism mapping a↦→−a, it
is suﬃcient to check this for f+ :Hn⊗S††
+ [(x + 2)−1] ↠BMW††
n ⊗S††
+ [(x + 2)−1]. It is clear
that the relators associated to (i)− (iv) are mapped to 0. Now C =e1s2e1−e1 is mapped to
S1, and the relations 6.9, 6.10 and the fact that S1−S 2∈In (henceSi−Si+1∈In for all i)
then imply, using conjugation by elements of the braid groups, that the relators associated to
MARKOV TRACES ON THE BMW-ALGEBRAS 29
(x + 2)(x7 + 4x6−x5− 12x4− 5x3 + 9x2− 1)xR1 + (−x7− 4x6 + 8x4 + 2x3− 8x2− 2x + 6)R1s−1
3
+ (2 x + 4)R1s−1
3 s−1
2 s−1
1 + (x + 2)(x2−x− 1)(x5 + 3x4− 3x3− 5x2 + 3x− 2)xR1s1
+ ( x + 2)(x2−x− 1)x2R1s1s−1
3 + (−x− 2)(x2−x− 1)(x3 + 3x2− 2x− 3)x2R1s1s3
+ ( −x8− 5x7− 3x6 + 13x5 + 17x4− 4x3− 10x2 + 6x + 6)R1s3 + (2x + 4)R1s3s2s1
+ ( −x− 2)(x3 + 2x2 + 2x− 1)xR2 + (x5 + 4x4 + 3x3− 3x2− 2x− 2)R2s−1
1
+ ( x + 1)(x + 2)(x2−x− 1)(x4 + 4x3 + 2x2− 2x− 4)xR2s−1
1 s3 + (x5 + 4x4 + 3x3− 3x2− 2x− 2)R2s1
+ ( x + 1)(x + 2)(x2−x− 1)(x4 + 4x3 + 2x2− 2x− 4)xR2s1s3
+ ( −x− 1)(x + 2)(x2−x− 1)(x4 + 3x3− 2x2−x + 2)xR2s2
+ ( −x− 2)(x5 + 2x4− 6x3− 7x2 + 2x + 9)xˆR1 + (2x7 + 9x6 + 2x5− 26x4− 29x3−x2 + 12x + 4)ˆR1s−1
3
+ ( −2x− 4)ˆR1s−1
3 s−1
2 s−1
1 + (x8 + 5x7 + 4x6− 11x5− 25x4− 14x3 + 9x2 + 14x + 4)ˆR1s3
+ ( −2x− 4)ˆR1s3s2s1 + (−x− 1)(x + 2)(x6 + 3x5− 4x4− 9x3 + 2x2 + 9x + 1)xˆR2
+ ( x9 + 7x8 + 14x7− 4x6− 47x5− 49x4 + 5x3 + 34x2 + 10x− 4)ˆR2s−1
1
+ ( x9 + 7x8 + 14x7− 3x6− 44x5− 52x4 + 32x2 + 12x− 4)ˆR2s1
+ ( −x8− 5x7− 2x6 + 17x5 + 25x4 + 3x3− 24x2− 20x− 2s−1
3 )R1 + (2x + 4)(x2 +x + 2)s−1
3 R1s−1
3
+ ( −x6− 3x5− 4x4− 2x3 + 7x2 + 10x + 4)s−1
3 R1s−1
1
+ ( −x8− 5x7−x6 + 14x5 + 9x4− 11x3− 10x2 + 4x + 4)s−1
3 R1s1
+ ( x− 1)(x + 2)(x2−x− 1)(x2 + 4x + 2)xs−1
3 R1s1s3
+ ( −x8− 4x7 +x6 + 12x5 + 12x4 + 5x3− 4x2− 12x− 10)s−1
3 R1s2
+ ( x + 1)(x5 + 3x4− 4x3− 9x2 + 2x + 10)xs−1
3 R1s3 + (2x + 4)s−1
3 R1s3s−1
2
+ ( −x8− 5x7− 3x6 + 13x5 + 25x4 + 15x3− 5x2− 12x− 4)s−1
3 ˆR1
+ ( −x− 2)(x5 + 3x4− 3x3− 7x2− 4x + 2)s−1
3 ˆR1s−1
3 + (x + 2)(x4 +x3 + 2x2− 3)xs−1
3 ˆR1s−1
2
+ ( x7 + 4x6− 2x5− 14x4− 15x3− 2x2 + 14x + 8)s−1
3 ˆR1s−1
1
+ ( x5− 4x4− 12x3− 4x2 + 10x + 6)s−1
3 ˆR1s1
+ ( −x7− 4x6 + 10x4 + 12x3 + 3x2− 4x− 6)s−1
3 ˆR1s3 + (−x− 1)(x + 2)(x2 +x− 1)xs−1
3 ˆR2
+ ( x5 + 4x4 + 3x3− 3x2− 2x− 2)s−1
3 ˆR2s−1
1 + (x5 + 4x4 + 3x3− 3x2− 2x− 2)s−1
3 ˆR2s1
+ ( x− 1)(x2 + 4x + 2)s−1
3 s−1
2 ˆR1s3 + (2x + 4)s−1
3 s−1
2 s1R2 + (−2x− 4)s−1
3 s−1
2 s1ˆR2
+ ( −x− 2)(x5 + 3x4− 3x3− 7x2− 4x + 2)s−1
3 s2R1s−1
3 + (−x5− 3x4 + 4x3 + 10x2 + 4x− 4)s−1
3 s2R1s3
+ ( x + 1)(x5 + 3x4− 4x3− 8x2 + 6x + 11)x2s−1
2 R2 + (−x5− 4x4− 5x3−x2 + 2x− 2)s−1
2 R2s−1
1
+ ( −x7− 4x6−x5 + 6x4 + 6x3−x2− 2)s−1
2 R2s1 + (x + 2)(x4 + 3x3− 6x + 1)xs−1
2 ˆR1
+ ( −x4− 3x3 + 3x + 2)xs−1
2 ˆR1s−1
3 + (−x4− 4x3− 3x2 + 5x + 4)xs−1
2 ˆR1s3
+ ( x + 1)(x5 + 2x4− 6x3−x2 + 10x + 6)xs−1
2 ˆR2
+ ( −x8− 5x7− 4x6 + 10x5 + 18x4 + 6x3− 7x2− 4x− 2)s−1
2 ˆR2s−1
1
+ ( −x8− 5x7− 4x6 + 10x5 + 18x4 + 6x3− 7x2− 4x− 2)s−1
2 ˆR2s1 + (−2x− 4)s−1
2 s1R2s−1
1
+ (2 x + 4)s−1
2 s3ˆR1s−1
3 + (−x7− 4x6 + 8x4− 7x2−x− 4)xs−1
1 R1
+ ( −x8− 3x7 + 5x6 + 13x5− 9x3 + 2x2 + 4x− 2)s−1
1 R1s−1
3 + (x7 + 4x6− 9x4− 3x3 + 4x2− 2)s−1
1 R1s3
+ ( −x7− 3x6− 2x5 + 2x4 + 7x3 + 2x2− 4x + 2)s−1
1 R2
+ ( x7 + 4x6− 2x5− 10x4 +x3 + 2x2− 7x− 6)xs−1
1 R2s−1
2
+ ( x8 + 4x7− 2x6− 10x5 +x4 + 2x3− 7x2− 4x + 4)xs−1
1 R2s2
+ ( −x7− 4x6 + 2x5 + 10x4−x3− 2x2 + 7x + 6)xs−1
1 R2s3
+ ( −x + 1)(x + 1)(x4 + 2x3− 5x2 + 2x + 14)xs−1
1 ˆR1
+ ( −x7− 4x6 + 11x4 + 15x3 + 5x2− 2x− 6)s−1
1 ˆR1s−1
3
+ ( −x− 1)(x6 + 2x5− 5x4− 3x3− 5x2 + 2x + 6)s−1
1 ˆR1s3
+ ...
Figure 5. Fora = 1, 2(x + 2)2x4(S1−S 2) to be continued.
30 Ivan Marin & Emmanuel Wagner
...
+ ( −x7− 4x6 + 2x5 + 10x4−x3 + 15x + 14)xs−1
1 ˆR2
+ ( −x7− 3x6− 2x5 + 2x4 + 7x3 + 2x2− 4x + 2)s−1
1 ˆR2s−1
3
+ (2 x6 + 7x5− 6x4− 11x3 + 2x2− 10x− 4)xs−1
1 ˆR2s−1
2
+ ( −x + 1)(x + 1)2(x2−x− 1)(x2 + 4x + 2)s−1
1 ˆR2s−1
1
+ ( −x7− 4x6 + 10x4 + 11x3− 2x2− 6x− 4)s−1
1 ˆR2s1 + (−2x− 4)s−1
1 ˆR2s1s−1
2
+ (2 x8 + 8x7− 3x6− 24x5− 10x4 + 12x3 + 6x2− 2x− 2)s−1
1 ˆR2s2
+ ( x7 + 4x6−x5− 13x4− 10x3 +x2− 6)s−1
1 s−1
3 R1s−1
3 + (−x3− 5x2− 2x− 2s−1
1 )s−1
3 R1s3
+ ( x6 + 4x5− 10x3− 13x2− 4x− 2)s−1
1 s−1
3 ˆR1s−1
3
+ ( x6 + 3x5− 3x4− 7x3− 6x2− 2x + 4)s−1
1 s−1
3 ˆR1s3
+ ( −x7− 4x6 +x5 + 13x4 + 10x3−x2 + 6)s−1
1 s−1
2 R2s−1
1
+ ( −x7− 3x6 + 5x5 + 13x4− 12x2 + 8)s−1
1 s−1
2 R2s1 + (2x + 4)s−1
1 s−1
2 s−1
3 R1 + (−2x− 4)s−1
1 s−1
2 s−1
3 ˆR1
+ (2 x + 4)s−1
1 s−1
2 s3R1 + (−2x− 4)s−1
1 s−1
2 s3ˆR1
+ ( −x− 2)(x2−x− 1)(x5 + 3x4− 4x3− 2x2 + 3x− 4)xs−1
1 s2R2
+ ( x + 1)(x5 + 3x4− 4x3− 10x2− 4x + 4)xs−1
1 s3R1s−1
3 + (−x− 1)(x + 2)(x2 + 2x− 2)s−1
1 s3R1s3
+ ( −x + 1)(x + 1)2(x2−x− 1)(x2 + 4x + 2)s−1
1 s3R2s−1
1
+ ( −x7− 4x6 + 10x4 + 11x3− 2x2− 6x− 4)s−1
1 s3R2s1
+ ( x + 1)(x6 + 4x5−x4− 13x3− 9x2 + 2x + 6)s−1
1 s3ˆR1s−1
3
+ ( x + 2)(x6 + 3x5− 4x4− 9x3−x2 + 2x + 6)s−1
1 s3ˆR1s3
+ ( −x8− 4x7 + 2x6 + 17x5 + 5x4− 22x3− 18x2 + 2x + 10)xs1R1
+ ( −x7− 4x6−x5 + 10x4 + 18x3 + 7x2− 2x− 6)s1R1s−1
3
+ ( x8 + 3x7− 5x6− 13x5 + 5x4 + 21x3 + 9x2− 8x− 6)s1R1s3
+ ( −x6− 2x5−x4− 4x3− 8x2− 8x + 2)s1R2
+ ( x5 + 3x4 + 4x3− 3x2− 9x− 2)xs1R2s−1
2 + (2x + 4)s1R2s−1
1 s2
+ ( x7 + 5x6 + 2x5− 9x4− 11x3− 4x2− 2)xs1R2s2
+ ( x7 + 4x6− 2x5− 16x4− 12x3 + 10x2 + 17x + 4)xs1R2s3
+ ( x8 + 5x7 + 4x6− 10x5− 23x4− 20x3 + 3x2 + 19x + 12)xs1ˆR1
+ ( −x7− 6x6− 8x5 + 11x4 + 34x3 + 22x2− 5x− 10)xs1ˆR1s−1
3
+ ( −2x7− 9x6− 3x5 + 24x4 + 33x3 + 7x2− 15x− 8)xs1ˆR1s3
+ ( x7 + 4x6− 2x5− 16x4− 12x3 + 10x2 + 17x + 4)xs1ˆR2
+ ( −x6− 2x5−x4− 2x3 + 2)s1ˆR2s−1
3
+ ( −x6− 3x5 + 6x4 + 13x3 + 3x2− 14x− 10)xs1ˆR2s−1
2
+ ( −x8− 5x7− 3x6 + 15x5 + 24x4− 2x3− 20x2− 8x + 8)s1ˆR2s−1
1
+ ( −x8− 5x7− 3x6 + 14x5 + 21x4 +x3− 15x2− 6x + 6)s1ˆR2s1
+ ( x9 + 5x8 + 3x7− 14x6− 22x5 + 3x4 + 20x3 + 4x2− 8x− 2)s1ˆR2s2
+ ( x + 2)(x2−x− 1)(x5 + 5x4 + 3x3− 2x2− 2x− 2)s1s−1
3 R1
+ ( x6 + 4x5− 10x3− 13x2− 4x− 2)s1s−1
3 R1s−1
3
+ ( −x7− 3x6 + 5x5 + 12x4− 5x3− 16x2− 6x + 4)s1s−1
3 R1s3
+ ( x7 + 5x6 + 4x5− 10x4− 21x3− 11x2 + 2x + 6)s1s−1
3 ˆR1s−1
3
+ (2 x + 2)(x2 + 4x + 2)(x4−x3− 3/2x2 + 1)s1s−1
3 ˆR1s3
+ ...
Figure 6. Fora = 1, 2(x + 2)2x4(S1−S 2), continued.
MARKOV TRACES ON THE BMW-ALGEBRAS 31
+ ( −x− 1)(x5 + 3x4− 3x3− 7x2− 6x + 2)s1s−1
2 R2s−1
1 + (2x + 4)xs1s−1
2 R2s1
+ ( x− 1)(x + 1)2(x2−x− 1)(x2 + 4x + 2)s1s−1
2 ˆR2s−1
1
+ ( x− 1)(x + 1)2(x2−x− 1)(x2 + 4x + 2)s1s−1
2 ˆR2s1
+ ( −x− 2)(x2−x− 1)(x4 + 5x3 + 3x2−x− 4)xs1s2R2
+ ( x− 1)(x + 1)2(x2−x− 1)(x2 + 4x + 2)s1s2R2s−1
1
+ ( x− 1)(x + 1)2(x2−x− 1)(x2 + 4x + 2)s1s2R2s1
+ ( −x + 1)(x + 1)2(x2−x− 1)(x2 + 4x + 2)s1s2ˆR2s−1
1
+ ( −x + 1)(x + 1)2(x2−x− 1)(x2 + 4x + 2)s1s2ˆR2s1 + (2x + 4)s1s2s−1
3 R1
+ ( −2x− 4)s1s2s−1
3 ˆR1 + (2x + 4)s1s2s3R1 + (−2x− 4)s1s2s3ˆR1
+ ( x + 2)(x2−x− 1)(x4 +x3− 4x2− 2)s1s3R1
+ ( x + 1)(x6 + 4x5−x4− 13x3− 9x2 + 2x + 6)s1s3R1s−1
3
+ ( x + 2)(x5 + 2x4− 6x3− 5x2 + 6)s1s3R1s3
+ ( −x8− 5x7− 3x6 + 15x5 + 24x4− 2x3− 20x2− 8x + 8)s1s3R2s−1
1
+ ( −x8− 5x7− 3x6 + 14x5 + 21x4 +x3− 15x2− 6x + 6)s1s3R2s1
+ ( x + 1)2(x2 + 4x + 2)(x4−x3−x2−x + 1)s1s3ˆR1s−1
3
+ ( x + 2)(x6 + 4x5−x4− 13x3− 9x2 + 4x + 8)xs1s3ˆR1s3
+ ( −x− 2)(x5 + 2x4− 6x3− 7x2 + 4x + 5)xs2R1 + (x3− 2x− 2)(x4 + 5x3 + 5x2−x− 1)s2R1s−1
3
+ ( x6 + 3x5− 4x4− 13x3− 6x2 + 4x + 2)s2R1s3
+ ( x + 1)(x7 + 4x6−x5− 12x4− 5x3 + 8x2 + 6x + 2)xs2R2
+ ( −x8− 5x7− 4x6 + 10x5 + 18x4 + 6x3− 7x2− 4x− 2)s2R2s−1
1
+ ( −x8− 5x7− 4x6 + 10x5 + 18x4 + 6x3− 7x2− 4x− 2)s2R2s1
+ ( x6 + 4x5−x4− 12x3− 4x2 + 13x + 11)x2s2ˆR2
+ ( −x9− 6x8− 9x7 + 7x6 + 34x5 + 31x4− 9x3− 26x2− 6x + 8)s2ˆR2s−1
1
+ ( −x9− 6x8− 9x7 + 7x6 + 34x5 + 31x4− 9x3− 26x2− 6x + 8)s2ˆR2s1 + (−2x− 4)s2s−1
3 R1s3
+ (2 x + 4)s2s−1
1 ˆR2s1 + (−x7− 3x6 + 4x5 + 14x4 + 6x3− 10x2− 12x− 2)s3R1
+ ( −x− 1)(x + 1)(x5 + 2x4− 6x3− 4x2 + 4)s3R1s−1
3 + (−x− 1)(x5 + 2x4−x3−x2− 4x− 4)s3R1s−1
1
+ ( −x7−x6 + 7x5 + 2x4− 13x3− 10x2 + 4x + 4)s3R1s1
+ ( x− 1)(x + 2)(x2−x− 1)(x2 + 4x + 2)xs3R1s1s3
+ ( −x + 1)(x8 + 6x7 + 9x6− 6x5− 29x4− 28x3− 16x2− 14x− 10)s3R1s2
+ ( x + 2)(x3 + 3x2− 6)s3R1s3
+ ( −x− 1)(x + 2)(x6 + 3x5− 4x4− 9x3 + 2x2 + 7x + 1)xs3R2
+ ( x8 + 6x7 + 7x6− 13x5− 27x4− 9x3 + 10x2 + 2x− 4)s3R2s−1
1
+ ( x8 + 6x7 + 8x6− 10x5− 30x4− 14x3 + 8x2 + 4x− 4s3)R2s1
+ ( −x7− 3x6 + 3x5 + 11x4 + 13x3 + 7x2− 2x− 4)s3ˆR1
+ ( −x− 1)(x7 + 4x6− 10x4− 12x3− 3x2 + 4x + 6)s3ˆR1s−1
3 + (−2x− 4)s3ˆR1s−1
3 s2
+ ( x5 + 3x4 +x3−x− 8)xs3ˆR1s−1
2 + (x6 +x5− 7x4− 5x3− 4x2 + 10x + 8)s3ˆR1s−1
1
+ ( −x6− 2x5 + 2x4− 3x3− 4x2 + 6x + 6)s3ˆR1s1
+ ( −x− 1)(x + 2)(x6 + 3x5− 4x4− 9x3 + 4x + 4)s3ˆR1s3
+ ( x− 1)(x + 1)(x2 + 4x + 2)s3s−1
2 ˆR1s−1
3 + (x− 1)(x + 2)(x2 + 4x + 2)s3s−1
2 ˆR1s3
+ ( −x− 1)(x5 + 3x4− 4x3− 10x2− 4x + 4)s3s2R1s−1
3 + (x + 1)(x + 2)(x2 + 2x− 2)s3s2R1s3
+ (2 x + 4)s3s2s−1
1 R2 + (−2x− 4)s3s2s−1
1 ˆR2.
Figure 7. Fora = 1, 2(x + 2)2x4(S1−S 2), last part.
32 Ivan Marin & Emmanuel Wagner
(v) and (viii) are also mapped to 0. Since s1e1 =e1s1 =ae1 it is clear thats1S1 =S1s1 =as1
and this implies siC−aC↦→ 0,Csi−aC↦→ 0 for all i, which justiﬁes that the 9th type of
relator is also mapped to 0. This completes the proof of the theorem.
Corollary 6.12. Let (tn) be a Markov trace on (BMW††
n ) with value in some S††-moduleM,
andt′
n its composite with M→M⊗S††[(a−x)−1, (2a−x)−1, (2a+x)−1]. Then t′
n is a linear
combinationtH
n , tK
n , t††
n with coeﬃcients in M⊗RS††[(a−x)−1, (2a−x)−1, (2a +x)−1].
Proof. We know from proposition 5.11 (ii) that t′
3 is a linear combination of tH
3 , tK
3 , t††
3 . The
statement is then a consequence of theorem 6.8 together with proposition 6.1 (iv). □
