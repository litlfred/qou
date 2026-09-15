---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-008-8-delignelusztig-theory
section_title: "Deligne–Lusztig Theory"
section_number: 8
pages: 52-61
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the W eyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
8.1. The goal of this section is to prove Theorems 7, 8, and 9. Throughout, we
assume that W is a Weyl group and use the notation and hypotheses of Section s
1-2. In particular, we continue to assume that F is of large characteristic. We will
write H ∗
! (−) = H ∗
! (−, ¯Qℓ) to denote cohomology with compact support.
8.2. The proofs of Theorems 7 and 8 rely on properties of the virtual characters
of GF introduced by Deligne–Lusztig [ DL], which we now review.
For all w ∈ W , the Deligne–Lusztig variety Xw ⊆ B × B is the transverse
intersection of Ow with the graph of the Frobenius map F : B → B . The G-action
on B × B restricts to a GF -action on Xw, so the formal sum
Rw =
∑
n
(−1)nHn
! (Xw)
deﬁnes a virtual representation of GF . In general, a virtual representation of GF
is unipotent iﬀ it occurs with nonzero multiplicity in Rw for some w.
We haveX1 = BF , a scheme of ﬁnitely many points, and R1 = ¯Qℓ[BF ], the ¯Qℓ-
vector space of functions on BF . For all B ∈ BF , let 1B be the indicator function
on {B}. Recall, cf. Remark 2.5.1, that Iwahori constructed an isomorphism
¯Qℓ ⊗HW |q1/2=q1/2
∼
− →EndGF (R1).
In terms of the functions 1B, the action of σw ∈HW on R1 is given by
˜σw · 1B =
∑
(B,B ′)∈OF
w
1B′,(21)
where ˜σw =q
|w|
2 σw.
Irreducible representations of W give rise to unipotent virtual representations of
GF in two ways:
8.2.1. For any φ ∈ ˆW , the formal Q-linear combination
Rφ = 1
|W |
∑
w∈W
φ(w)Rw(22)
has nonzero multiplicity in R1 (where we mean 1 ∈ W , not 1 ∈ ˆW ), so it is
unipotent. The characters of the virtual representations Rφ are called almost-
characters, being very close to irreducible characters: See Lemma-Pos tulate 8.3.1,
below.
8.2.2. For any φ ∈ ˆW , the trace φq : Q(q
1
2 ) ⊗HW → Q(q
1
2 ) (see § A.7) restricts
to a function HW → Z[q± 1
2 ] [ GP, Thm. 9.3.5]. So we can set
φq =φq|q1/2=q1/2 :HW → Z[q± 1
2 ].
Then the double centralizer theorem gives an isomorphism of (HW ×GF )-modules
R1 ≃
⨁
φ∈ ˆW
Vφ,q ⊗ρφ,(23)
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 53
where Vφ,q, resp. ρφ, is a simple HW -module of character φq, resp. a unipotent
irreducible representation of GF . The representations ρφ are called the unipotent
principal series .
Ifρ is a representation of GF , then HomGF (R1,ρ ) forms an End GF (R1)-module
under precomposition. In particular, applying Hom GF (R1, −) to both sides of ( 23)
yields an isomorphism of HW -bimodules:
EndGF (R1) ≃
⨁
φ∈ ˆW
Vφ,q ⊗ HomGF (R1,ρφ).
By Artin–Wedderburn, we deduce:
Lemma 8.2.1. For all φ ∈ ˆW , we have HomGF (R1,ρφ) ≃ Vφ,q as EndGF (R1)-
modules, hence as HW -modules.
The map ρ ↦→HomGF (R1,ρ ) extends uniquely to an additive map from virtual
representations to virtual modules. We emphasize that Hom GF (R1,ρ ) may still be
nonzero even when its virtual dimension (R1,ρ )GF is zero .
8.3. Lusztig showed that the unipotent irreducible represe ntations of GF can be
indexed by a set that only depends on W [L84-1, Ch. 4]. This is the set denoted
Uch(W ) in § A.9. Abusing notation, we will conﬂate the elements of Uch( W ) with
the unipotent irreducible representations themselves. Th en the embedding ˆW →
Uch(W ) is precisely the map φ ↦→ρφ. Cor. 4.24-4.25 of [ L84-1] entail:
Lemma-Postulate 8.3.1. There is a function ∆ : Uch( W ) → {±1} such that for
all φ ∈ ˆW , we have:
(1) ∆(ρφ) = 1.
(2) The transformation rule
Rφ =
∑
ρ∈Uch(W )
{ρφ,ρ }∆(ρ)ρ.
Equivalently, (∆(ρ)ρ,Rφ) = {ρφ,ρ } for all ρ ∈ Uch(W ).
Remark 8.3.2. We haveRφ(1) = Fegφ(q) and ρφ(1) = Degφ(q) for all φ ∈ ˆW .
8.4. Springer conjectured [ S76], and Kazhdan proved [ Kaz], a remarkable identity
relating the character values of the virtual representatio ns Rw to the action of W
on the ﬁbers of the Grothendieck–Springer map. To state it, l et Bg denote the ﬁber
of ˜G →G aboveg ∈GF , and let
Qg(w) =
∑
n
tr(wF | H2n(Bg)).
(By [ DLP], Bg has no odd cohomology.) The main result of [ Kaz] implies:
Theorem 8.4.1 (Kazhdan). For all g ∈GF andw ∈W , we have Qg(w) = Rw(g).
Remark 8.4.2. Lusztig generalized the functions Qg to bad characteristic in [ L81],
and similarly generalized Kazhdan’s theorem in [ L90].
54 MINH-TÂM QUANG TRINH
8.5. In this subsection, we state our arguments in such a way t hat we do not
need to assume G is semisimple . The following result recovers Theorem 7 in the
semisimple case.
Theorem 8.5.1. For all β ∈ Br +
W , we have
(⟨ ˜β⟩ q ·ε[Sym(V)]q)|q1/2=q1/2 = (−1)r
|GF |
∑
u∈U F
|U(β)F
u |Qu
in Q(q
1
2 ) ⊗R(W ), where ˜β =q
|β|
2 β.
Remark 8.5.2. An algebraic group H is special iﬀ every principal H-bundle in the
étale topology is Zariski-locally trivial [ Gr]. If G is special, then [ HR, Appendix]
and [ Jo, Thm. 4.10] together imply that the right-hand side of the id entity is the
virtual weight series of [ Z(β)/G]. In this case, the identity is essentially a corollary
of Theorem 5. The sign character appears when we use Verdier duality to ma tch the
dual of Borel–Moore homology with compactly-supported coh omology, cf. [AHJR,
Lem. 4.5].
However, not all reductive algebraic groups are special. If X0 is a G0-variety and
G is not special, then the virtual weight series of [ X/G] need not be the quotient
of the virtual weight polynomial of X by that of G: See [ Jo, Ex. 4.9]. The force of
Theorem 7 is that for X0 = Z(β)0, that property holds anyway.
The following orthogonality result for the characters Qu will reduce our work to
computing the multiplicities (Qu, ⟨ ˜β⟩ q)W . We are using the version quoted by Shoji
in [ S, 510], in turn based on [ S76, Thm. 5.6]. The counterpart for the characters
Rw is [ DL, Thm. 6.9], which holds in any characteristic.
Theorem 8.5.3 (Deligne–Lusztig, Springer) . For all φ ∈R(W ), we have
qNφ ·εQ1 =
∑
u∈U F
(Qu,φ )WQu
in R(W ).
Before we can use Theorem 8.5.3, we must rewrite the left-hand side of the
orthogonality identity:
Lemma 8.5.4. We have [Sym(V)]q = (−1)r
|GF | qNQ1.
Proof. We have B1 = B, so the Borel isomorphism states that Q1 is the algebra of
W -coinvariants of V, graded by q. That is,
Q1 = [Sym(V)]q ·
∏
1≤i≤r
(1 − qdi),
whered1,...,d r are the invariant degrees of the W -action on V [GP, 149]. (If G is
not semisimple, then we might have di = 1 for one or more i.) At the same time,
if B0 ⊆G0 is a ﬁxed Borel, then
|GF | = |BF ||BF | = qN (q − 1)r ∑
w∈W
q|w|.
By the Bott–Solomon formula [ Sol],∑
w∈W q|w| =∏
i:di⁄=1
qdi −1
q−1 =∏
i
qdi −1
q−1 . □
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 55
Combining Theorem 8.5.3 and Lemma 8.5.4, it remains to prove the following
multiplicity formula:
Proposition 8.5.5. For any G-orbit C ⊆ U and β ∈ Br +
W , we have
∑
u∈C F
(Qu, ⟨ ˜β⟩ q)W |q1/2=q1/2 =
∑
u∈C F
|U(β)F
u |,
where ˜β =q
|β|
2 β.
Lemma 8.5.6. For all β ∈HW and w ∈W , we have
⟨β⟩ q(w)|q1/2=q1/2 = tr(β | HomGF (R1,Rw)).
Proof. By Lemma 8.2.1 and Lemma-Postulate 8.3.1, the left-hand side equals
∑
φ,ψ∈ ˆW
(ρφ,Rψ)GF tr(β | HomGF (R1,ρφ))ψ(w).
Ifρ ∈ Uch(W ) does not take the form ρφ for some φ ∈ ˆW , then HomGF (R1,ρ ) = 0.
So above, the sum over φ ∈ ˆW can be extended to a sum over ρ ∈ Uch(W ), giving
∑
ψ∈ ˆW
∑
ρ∈Uch(W )
(ρ,Rψ)GF tr(β | HomGF (R1,ρ ))ψ(w)
=
∑
ψ∈ ˆW
tr(β | HomGF (R1,Rψ))ψ(w).
By (22) and Schur orthogonality, the last expression is tr( β | HomGF (R1,Rw)). □
Lemma 8.5.7. For all β ∈ Br +
W and g ∈GF , we have
|G(β)F
g | = tr( ˜β ×g |R1),
where ˜β =q
|β|
2 β.
Proof. Fix B0 ∈ BF . Suppose that β =σs1 · · ·σsℓ , where s1,...,s ℓ ∈S. Then
G(β)F
g,B0 ≃
{
(B1,...,B ℓ) ∈ (BF )ℓ : B0 =g−1Bℓg,
(Bi−1,Bi) ∈Osi for 1 ≤i ≤ℓ
}
.
By ( 21), the cardinality of the right-hand side is precisely the co eﬃcient of 1B0 in
the expansion of ( ˜β,g ) · 1B0 with respect to the basis {1B}B∈BF of R1. Summing
overB0 gives the result. □
Proof of Proposition 8.5.5. By Schur orthogonality, Lemma 8.5.6, and Theorem
8.4.1,
(Qu, ⟨ ˜β⟩ q)W = 1
|W |
∑
w∈W
⟨β⟩ q(w)Qu(w)
= 1
|W |
∑
w∈W
tr(β | HomGF (R1,Rw))Rw(u).
56 MINH-TÂM QUANG TRINH
On the other hand, by Lemma 8.5.7, ( 23), and Lemma 8.2.1,
|U(β)F
u | = tr( ˜β ×u |R1)
=
∑
φ∈ ˆW
φq( ˜β)ρφ(u)
=
∑
ρ∈Uch(W )
tr(β | HomGF (R1,ρ ))ρ(u).
So the following result concludes the proof. □
Proposition 8.5.8 (Geck–Lusztig). We have
∑
u∈C F
ρ(u) =
∑
u∈C F
1
|W |
∑
w∈W
(ρ,Rw)GFRw(u)
for any G-orbit C ⊆ U and ρ ∈ Uch(W ).
Proof. This is shown on pages 497-498 of [ L11], relying on [ G96, Prop. 1.3]. □
Remark 8.5.9. IfG is of type A, then the identity holds without summing over CF
on both sides, i.e., at the level of individual u ∈CF .
8.6. Recall from Section 7 that for any topological braid β, we write ˆβ for its link
closure and [ ˆβ]q ∈ Z( (q
1
2 ) )[a±1] to denote the HOMFLY series of the link; for any
ﬁnite Coxeter group W , we write tr :HW → Z[q± 1
2 ](a) to denote Gomi’s Markov
trace. In [ Kál], Kálmán proved the following result.
Theorem 8.6.1 (Kálmán). For all n and β ∈ Brn, we have an equality of q
1
2 -
series:
coeﬃcient of a|β|+n−1 in [ˆβπ ] = coeﬃcient of a|β|−n+1 in [ ˆβ].
More generally, if W is any ﬁnite Coxeter group of rank r, then we have an equality
coeﬃcient of a2r in tr(βπ) = coeﬃcient of a0 in tr(β),
where tr =
(
1−a2
1−q
)r
tr.
More precisely, [ Kál] includes two proofs of the statement about HOMFLY. The
second proof only uses the structure of HW , so it generalizes to a proof of the
statement about tr. By Proposition 7.4.3, we deduce:
Corollary 8.6.2. For any ﬁnite Coxeter group W and β ∈ BrW , we have
(ε, ⟨βπ⟩ 0
q)W = q
|π|
2 (1, ⟨β⟩ 0
q)W.
Corollary 8.6.3. Under the hypotheses of Theorem 8.5.1, we have
|X (βπ)F | = |U(β)F |.
Proof. The proof is similar to that of Corollary 4 in Section 6. Namely, by Springer
theory, we have:
(1) (1,Qu)W = 1 for all u ∈ UF .
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 57
(2) (ε,Q 1)W = qdim B and (ε,Qu)W = 0 for all u ⁄= 1.
Now, Theorem 8.5.1 and the preceding corollary together imply qdim B|X (βπ)F | =
q
|π|
2 |U(β)F |. But we have dim B =N = |w0| = 1
2 |π|. □
Remark 8.6.4. We claim that, in the case where β = σw, Corollary 8.6.3 recovers
Proposition 2.2 of [ L21]. In our notation, the latter states that
|U(σw)F | =qN |BF |R1,w(q),(24)
whereR1,w(q) ∈ Z[q] is the so-called R-polynomial deﬁned in [ KL]. If B+,B − ∈ BF
are ﬁxed Borels in opposite position, then
R1,w = |{B ∈ BF : (B+,B ) ∈Ow, (B,B −) ∈Ow0 }|
by [ KL, Lem. A.4]. So, by the transitivity of the GF -action on OF
w0 , we have
|X (σwπ)F | = |OF
w0 |R1,w(q) = qdim B|BF |R1,w(q).
Now Corollary 8.6.3 implies ( 24).
8.7. In the next subsection, we will prove Theorem 8. Before doing so, we set
notation for parabolic subgroups and review how they intera ct with the virtual
representationsRw.
Fix a split torus T0 ⊆G0. We identify the character lattice X in the root datum
of G with the character lattice of T . We identify the set S ⊆ W with the set of
reﬂections in V∨ corresponding to a system of simple roots in X. This system of
simple roots determines a Borel B0 =T0 ⋉U0.
If P0 is a parabolic subgroup of G0 containing B0, then the Weyl group of the
Levi quotient of P0 is an S-parabolic subgroup of W (see §A.4). (Conversely, every
S-parabolic subgroup of W arises in this way.) We ﬁx such a parabolic P0. We write
UP,0 and L0 for its unipotent radical and Levi quotient, respectively. In general,
we will distinguish the data attached to L0 with a subscript. Thus,
(1) WL is the Weyl group of L0.
(2) BL,0 is the ﬂag variety of L0.
(3) UL,0 is the unipotent locus of L0.
(4) If β ∈ Br +
WL , then we write OL(β)0 for the analogue of O(β) with L0 in
place of G0.
(5) If w ∈WL, then RL,w is the Deligne–Lusztig virtual character with LF in
place of GF .
The following formula for the parabolic restriction of the Rw is [ C, Prop. 7.4.4],
though it originates in [ DL, §8].
Proposition 8.7.1 (Deligne–Lusztig). For all w ∈W , we have
(Rw)U F
P = 1
|WL|
∑
x∈W
xwx−1∈WL
RL,xwx−1
as virtual representations of LF , where (−)U F
P means we take UF
P -invariants.
58 MINH-TÂM QUANG TRINH
8.8. We now use Theorem 7 to prove Theorem 8. In what follows, let W ′ ⊆W be
a parabolic subgroup, and let d ≥ 0 be the diﬀerence in their ranks.
8.8.1. First, we establish the commutative diagram:
(25)
BrW ′ R(W ′)[ [q] ]
BrW R(W )[ [q] ]
⟨−⟩ 0
q
1
(1−q)d IndW
W ′
⟨−⟩ 0
q
We can and will assume that W ′ =WL in the setup of the previous subsection.
To disambiguate notation, we will write ⟨−⟩ 0
q, resp. ⟨−⟩ 0′
q , for the function on
BrW , resp. Br W ′ . For all w ∈ W ′, let the G0-schemes Uw,0, UL,w,0 over F be
deﬁned by the cartesian squares:
Ow,0 Uw,0
B0 × B0 U0 × B0
act
OL,w,0 UL,w,0
BL,0 × BL,0 UL,0 × BL,0
act
Let V′ = V/VW ′
, so that V′ is a realization of W ′ satisfying ( V′)W ′
= 0. Then
d = dim V − dim V′. So for all x ∈W ′, Theorems 8.4.1 and 8.5.1 give
⟨σw⟩ 0
q(x)|q=q = (−1)r−|β|
|GF |
∑
u∈U F
|(Uw)F
u |Rx(u),
(IndW
W ′ ⟨σw⟩ 0′
q )(x)|q=q
(1 −q)d = (−1)r−|β|
|LF ||W ′|
∑
u′∈U F
L
∑
y∈W
yxy −1∈W ′
|(UL,w)F
u′ |RL,yxy −1(u′).
Since β ↦→(−q− 1
2 )|β|⟨β⟩ 0
q is linear as a function on HW , it remains to match the
right-hand sides above for all w andx. By Proposition 8.7.1, we further reduce the
problem to:
1
|GF |
∑
u∈U F
|(Uw)F
u |Rx(u) = 1
|LF |
∑
u′∈U F
L
|(UL,w)F
u′ |(ResGF
P F Rx)U F
P (u′).(26)
We will rewrite the point counts on both sides. Let ( Uw)B ⊆ Uw be the ﬁber of
Uw → U × B → B above our ﬁxed Borel B ∈ BF , so that
(Uw)F
B = {u ∈ UF : (u−1Bu,B ) ∈Ow}.
Let BF act on GF , resp. (Uw)F
B, by right multiplication, resp. right conjugation.
(Thus its action on ( Uw)F
B ×GF is free.) Analogously to Lemma 4.5.2, we have:
Lemma 8.8.1. We have a GF -equivariant bijection
((Uw)F
B ×GF )/BF ∼
− → UF
w
[u,g ] ↦→ gug −1
whereGF acts on ((Uw)F
B ×GF )/BF by left multiplication on the factor of GF .
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 59
Let {UF
i }i be the set of GF -orbits of UF . For each i such that UF
i intersects
(Uw)F
B, we pick a point ui ∈ UF
i . Using Lemma 8.8.1, we expand:
1
|GF |
∑
u∈U F
|(Uw)F
u |Rx(u) = 1
|BF |
∑
i
|UF
i ∩ (Uw)F
B|Rx(ui)
= 1
|BF |
∑
u∈(Uw)F
B
Rx(u).
Let BL =L ∩B. As above, let {UF
L,j}j be the set of LF -orbits of UF
L . For each j
such that UF
L,j intersects ( UL,w)F
BL , we pick a point u′
j ∈ (UL,j)F
BL . Then we can
also expand:
1
|LF |
∑
u′∈U F
L
|(UL,w)F
u′ |(Rx)U F
(u′) = 1
|BF
L |
∑
j
|(UL,j)F
B|(Rx)U F
(u′
j)
= 1
|BF
L |
∑
u′∈(UL,j )F
B
(Rx)U F
(u′)
= 1
|BF
L ||UF
P |
∑
u′∈(UL,j )F
B
u′′∈U F
P
Rx(u′u′′).
Above, |BF
L ||UF
P | = |BF |. So the following lemma concludes the proof of ( 26).
Lemma 8.8.2. For all w ∈WL, we have (Uw)B = (UL,w)BLUP ≃ (UL,w)BL ×UP .
Proof. Lifting w ∈WL ≃NL(T )/T to a point ˙w ∈NL(T ), we observe that
B ˙wB =UPBL ˙wBLUP = (BL ˙wBL)UP ≃BL ˙wBL ×UP.
But ( Uw)B =B ˙wB ∩ U and ( UL,w)BL =BL ˙wBL ∩ UL. □
8.8.2. We claim that commutativity of ( 25) implies commutativity of:
HW ′ R(W ′)[q± 1
2 ]
HW R(W )[q± 1
2 ]
⟨−⟩ q
IndW
W ′
⟨−⟩ q
This follows from the projection formula for induced repres entations, as we now
explain. If [Λ( V)]q =∑
i (−q)i Λi(V), then ε[Λ(V)]q is the multiplicative inverse
of ε[Sym(V)]q in R(W )[ [q] ]. By the projection formula, we have
(−q
1
2 )|β| IndW
W ′ ⟨β⟩ q = IndW
W ′ (⟨β⟩ 0
q ·εW ′[Λ(V′)]q)
= IndW
W ′ (⟨β⟩ 0
q · ResW
W ′ (εW [Λ(V′)]q))
= (IndW
W ′ ⟨β⟩ 0
q) ·εW [Λ(V′)]q
Since d = dim V − dim V′, we have
(−q
1
2 )|β|⟨β⟩ q = ⟨β⟩ 0
q ·εW [Λ(V)]q
= 1
(1 − q)d ⟨β⟩ 0
q ·εW [Λ(V′)]q.
So the commutativity of ( 25) implies Ind W
W ′ (⟨β⟩ q) = ⟨β⟩ q, as needed.
60 MINH-TÂM QUANG TRINH
8.9. Finally, we prove Theorem 9, stating that
⟨β⟩ 0
q ∈ 1
(1 − q)r(w) R(W )[q],
where w is the image of β in W and r(w) = dim Vw.
First, we introduce a function δ :W → Z. For all w ∈W , we claim that
δ(w) = lim
q→1
det(1 − qw | V)
(1 − q)r(w)
exists and takes values in Z. Indeed, since w has ﬁnite order, its action on V is
diagonalizable. Thus r(w) equals the multiplicity of 1 − q in the characteristic
polynomial det(1 − qw | V). This shows that δ(w) exists. It is an integer because
QW = Q and character values are algebraic integers. We can now stat e:
Theorem 8.9.1 (Lusztig). IfG is semisimple and β ∈ Br +
W maps to w ∈W , then
the isotropy groups of the G-action on G(β) are diagonalizable groups D such that
|DF | divides (q − 1)r(w)δ(w)|Z(G)|,
whereZ(G) is the center of G. In particular, the isotropy groups of the GF -action
on G(β)F satisfy the same divisibility condition.
Proof. Fix a maximal split torus T0 ⊆G0 and a lift ˙w ∈NG(T ) of w. In the case
whereG is adjoint and w is elliptic, meaning Tw is discrete, the proof is analogous
to the proof of [ L11, Thm. 5.2]. However, the argument there actually shows more :
For general G and w, it shows that we can assume D ⊆ T ˙w, independently of β.
Let ¯G = G/Z(G), the adjoint group of G, and let ¯T, ¯D be the images of T,D in
¯G. Writing ¯T ′ for the identity component of ¯T ˙w, we see that ¯T ′ is a split torus of
rank r(w) such that ¯T ˙w/ ¯T ′ is discrete. So we get |( ¯T ˙w)F | = (q − 1)r(w)δ(w) from
the elliptic case. Finally, |(T ˙w)F | = |( ¯T ˙w)F ||Z(G)|. □
Proof of Theorem 9. Combining Theorems 7 and 8.9.1, we see that
⟨β⟩ 0
q|q=q ∈ 1
(1 −q)r(w)δ(w)|Z(G)|R(W )(27)
for all q ≫ 0. At the same time, by Proposition 7.5.1,
⟨β⟩ 0
q ∈ 1
(1 − qd1) · · · (1 − qdr )R(W )[q0],(28)
where q0 is deﬁned by ( 20) and di ∈ Z for all i. Therefore, ( 27) simpliﬁes to
⟨β⟩ 0
q|q=q ∈ 1
(1 −q)r(w) R(W )
for all q ≫ 0. Therefore, ( 28) simpliﬁes to
⟨β⟩ 0
q ∈ 1
(1 − q)r(w) R(W )[q],
as needed. □
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 61
