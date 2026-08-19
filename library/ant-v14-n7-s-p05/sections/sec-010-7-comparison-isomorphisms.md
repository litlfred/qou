---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-010-7-comparison-isomorphisms
section_title: "Comparison isomorphisms"
section_number: 7
pages: 31-36
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
doc_brief: "Motivic Gauss–Bonnet formulas — 18 sections: Duality and Euler characteristics; TX/B(1X×B X); TX/B(p∗"
---
We recall the elementη∈ HomSH(B)(1B, S−1,−1∧1B) induced by the map of B-schemesη: A2\{0}→ P1,
η(a, b)=(a: b). As every E∈ SH(B) is a module for 1B, we have the map×η: E→ S−1,−1∧ E for
each x∈ SH(B). We say thatη acts invertibly on E if×η is an isomorphism in SH(B).
We consider the following situation: ﬁx an SL-oriented motivic spectrum E∈ SH(B). This gives us the
twisted cohomology theoryE∗,∗ underlying the oriented cohomology deﬁned byE. Let(E∗,∗,˜E∗,∗) be an ex-
tension of E∗,∗ to an oriented cohomology theory onSmB, in other words, we deﬁne new pushforward maps
ˆf∗: E∗,∗
W (Y,ω Y/B⊗ f∗L)→ E∗−2d,∗−d
Z (X,ω X/B⊗ L)
The main result of this section is a comparison theorem. Before stating the result we recall the decom-
position of SH(B)[1/2] into plus and minus parts.
We have the involutionτ: 1B→ 1B induced by the symmetry isomorphismτ: P1∧ P1→ P1∧ P1. In
SH(B)[1/2], this gives us the idempotents(id+τ)/2,(id−τ)/2, and so decomposes SH(B)[1/2] into
+1 and -1 “eigenspaces” forτ:
SH(B)[1/2]= SH(B)+× SH(B)−
We decompose E∈ SH(B)[1/2] as E= E+⊕ E−.
Theorem 7.1. Suppose the pushforward maps
f∗, ˆf∗: E∗,∗
W (Y,ω Y/B⊗ f∗L)→ E∗−2d,∗−d
Z (X,ω X/B⊗ L)
1832 Marc Levine and Arpon Raksit
agree for W, Z, L, X= V a vector bundle over Y and f: Y→ V the zero-section. Suppose in addition
that one of the following conditions holds:
(i) The SL-orientation of E extends to a GL-orientation.
(ii) η acts invertibly on E.
(iii) 2 acts invertibly on E and E−1,0
+ (U)= 0 for afﬁne U in SmB.
Then f∗= ˆf∗ for all X, Y, Z, W, L, f for which the pushforward is deﬁned.
Proof. By the standard argument of deformation to the normal cone, it follows that f∗= ˆf∗ for all
f : Y→ X a closed immersion, Z, W, L. As every proper map in SmB is projective, f admits a
factorization f= p◦ i, with i: Y→ X×B PN a closed immersion and p: X×B PN→ X the projection.
By functoriality of the pushforward maps, it sufﬁces to check that p∗=ˆp∗.
In case (i), this follows from the uniqueness assertion in [Panin 2009, Theorem 2.5(i)]. Indeed, the
cohomology theory associated to a GL-oriented motivic spectrum E satisﬁes the axioms of Panin and
Smirnov and the associated Thom isomorphisms give rise to an “orientation” in the sense of [Panin 2009,
Deﬁnition 1.9], so we may apply the results cited. We note that in [Panin 2009] the base-scheme is Spec k,
with k a ﬁeld, so [loc. cit .] does not immediately apply to our setting of a more general base-scheme; we
say a few words about the extension of this result to our base-scheme B. As a proper map f: Y→ X
in SmB is projective, one factors f as f= p◦ i, with i: Y→ Pn
X a closed immersion and p: Pn
X→ X
the projection. The uniqueness for a closed immersion in SmB reduces to the case of the zero-section of
a vector bundle by the usual method of deformation to the normal bundle, and as the pushforward by
the zero-section of our two theories are the same by assumption, we have agreement in the case of a
closed immersion. For the projection p, the proof of [Panin 2009, Theorem 2.5(i)] relies on [Panin 2004,
Theorem 1.1.9], where for p, using the projective bundle formula, the key point is to show that both
pushforwards have the same value on the unit 1Pn
X∈ E0,0(Pn
X). The proof of this relies on the formula for
the pushforward of 1Pn
X under the diagonal1Pn
X: Pn
X→ Pn
X×X Pn
X given by [Panin 2004, Lemma 1.9.4].
As1Pn
X is a closed immersion, the two pushforwards under 1Pn
X agree, and the proof of the formula in
[Panin 2004, Lemma 1.9.4] uses only formal properties of pushforward and pullback as expressed in our
axioms, plus the projective bundle formula. This latter in turn relies only on properties of the Thom class
of O(−1) and localization with respect to Am
X⊂ Pm
X, and thus we may use [Panin 2004, Lemma 1.9.4] in
our more general setting. The argument that the pushforward of 1Pn
X under p can be recovered from the
formula for the pushforward of 1Pn
X under1Pn
X is elementary and formal, and only uses the restriction of
the two theories to Sm-LX, and not the fact that these restrictions come from theories over k. Thus, the
argument used in the proof of [Panin 2004, Lemma 1.9.4] may be used to prove our result in case (i).
In case (ii), we use Lemma 7.2 below. Indeed, if N is odd, we may apply the closed immersion
X×B PN→ X×B PN+1 as a hyperplane, so we reduce to the case N even, in which case both p∗ andˆp∗
are inverse to the mapi∗, where i: X→ X×B PN is the section associated to the point(1: 0:...: 0) of PN.
Motivic Gauss–Bonnet formulas 1833
In case (iii) we may work in the category SH(B)[1/2]. We decompose E∈ SH(B)[1/2] as E= E+⊕ E−
and similarly decompose the pushforward maps f∗ and ˆf∗. By Lemma 7.5, η acts invertibly on SH(B)−
and the projection of η to SH(B)+ is zero. By Lemma 7.3 below, the SL-orientation of E induces an
SL-orientation on the projection E+ that extends to a GL-orientation. By (i), this implies that f+
∗ = ˆf+
∗ .
By (ii), f−
∗ = ˆf−
∗ , so f∗= ˆf∗. □
Lemma 7.2 [Ananyevskiy 2016a, Theorem 1]. Let E∈ SH(B) be an SL-oriented motivic spectrum on
whichη acts invertibly. Let 0∈ PN(Z) be the point(1: 0...: 0). For X∈ SmB, L→ X a line bundle and
Z⊂ X a closed subset, the pushforward map
i∗: E∗−2N,∗−N
Z (X,ω X/B⊗ L)→ E∗,∗
p−1(Z)(X×B PN,ω PN/B⊗ p∗L)
is an isomorphism.
Proof. Using a Mayer–Vietoris sequence, we see that the statement is local on X for the Zariski topology,
so we may assume that L= OX. If we prove the statement for the pair (X, X) and(X\ Z, X\ Z) the
local cohomology sequence gives the result for (X, Z), thus we may assume that Z= X, and we reduce
to showing that
i∗: E∗−2N,∗−N(X,ω X/B)→ E∗,∗(X×B PN,ω PN/B)
is an isomorphism.
This is [Ananyevskiy 2016a, Theorem 4.6] in case B= Spec k, k a ﬁeld. The proof over a general
base-scheme is essentially the same, we say a few words about this generalization. Most of the results
that are used in the proof of [loc. cit .] are already proved in the required generality here, for example,
the Thom isomorphism (3.10.1) of Construction 3.10 generalizes Ananyevskiy’s construction [2016a,
Corollary 1] from B= Spec k to general B. The proof of [Ananyevskiy 2016a, Theorem 4.6] relies
also on [Ananyevskiy 2016a, Lemma 4.1], which in our setting reduces to the fact that for X∈ SchB,
and u∈0(X, O×
X) a unit, the automorphism of X× P1 sending(x,( t0: t1)) to(x,( ut0, u−1t1) induces
the identity on X+∧ P1/ X in H•(X). This follows by identifying P1
X with P(A2
X) and noting that the
diagonal matrix with entries u, u−1 is an elementary matrix in GL 2(0(X, OX)). □
Lemma 7.3. Suppose that E∈ SH(B) is SL oriented and that E−1,0(U)= 0 for all afﬁne U in SmB. Then
the induced SL orientation on E+∈ SH(B)+ extends to a GL orientation.
Proof. Let u∈0(X, O×
X) be a unit on some X∈ SmB. Then the map
×u: X×B P1→ X×B P1; (x,[t0: t1])↦→(x,[ut0: t1])
induces the identity on S2,1∧ X/B in SH(B)+. Indeed, let[u]: X/B→ X/B∧ Gm be the map induced
by u: X→ Gm. The argument given by Morel [2004, 6.3.4], that
×u/B= id+η[u]
1834 Marc Levine and Arpon Raksit
in case B= Spec k, k a ﬁeld, is perfectly valid over a general base-scheme: this only uses the fact that
for X and Y pointed spaces over B, one has
6∞
S1 X×B Y≃6∞
S1 X⊕6∞
S1 Y⊕6∞
S1(X∧ Y)
and that the map×u: S1∧ Gm∧ X+→ S1∧ Gm∧ X+ is the S1-suspension of the composition
S1∧ Gm∧ X+
id∧u−−→S1∧(Gm× Gm)∧ X+
id∧µ∧id−−−−→S1∧ Gm∧ X+,
whereµ: Gm× Gm→ Gm is the multiplication. As η goes to zero in SH(B)+, it follows that×u/B= id
in SH(B)+.
Now take g∈0(X, GLn(OX)), let u= det g, let mu∈0(X, GLn(OX)) be the diagonal matrix with
entries u, 1,..., 1 and let h= m−1
u · g∈0(X, SLn(OX)). We have
ThX(On
X)=(P1)∧n∧ X+.
Since E is SL-oriented, the map Th(h): ThX(On
X)→ ThX(On
X) induces the identity on E∗∗ and thus
Th(g)∗= Th(mu)∗: E∗,∗
+ (ThX(On
X))→ E∗,∗
+ (ThX(On
X)).
But as Th(mu)=(×u)∧ id, our previous computation shows that Th(mu)∗= id.
Now let V→ X be a rank r vector bundle on some X∈ SmB, choose a trivializing afﬁne open cover
U={ Ui} of X and letφi: V|Ui→ Ui× Ar be a local framing. We have the suspension isomorphism
Th(VUi)≃ Th(Ui× Ar)=6r
TUi+
giving the isomorphism
θi: Ea,b
+ (Ui)→ E2r+a,r+b
+0V|Ui
(V|Ui).
Since GLr(OUi) acts trivially on E∗∗
+(Th(Ui× Ar)), the isomorphismθi is independent of the choice of
framingφi. In addition, the assumption E−1,0(Ui∩ U j)= 0 implies
E2r−1,r
+0V|Ui∩U j
(V|Ui∩U j)= 0
for all i, j. By Mayer–Vietoris, the sections
θi(1Ui)∈ E2r,r
+0V|Ui
(V|Ui)
uniquely extend to an element
θV∈ E2r,r
+0V(V).
The independence of the θi on the choice of framing and the uniqueness of the extension readily
implies the functoriality of θV and similarly implies the product formula θV⊕W= p∗
1θV∪ p∗
2θW . By
construction,θV is the suspension of the unit over Ui, another application of independence of the choice
of framing and the uniqueness of the extension shows that this is the case over every open subset U⊂ X
Motivic Gauss–Bonnet formulas 1835
for which V|U is the trivial bundle. Finally, the independence and uniqueness shows that V↦→θV is an
extension of the SL orientation on E+ induced by that of E. □
Lemma 7.4. For u∈0(X, O×
X) we have
[u]η=η[u]: 6∞
T X+→6∞
T X+.
Proof. We use the decomposition
6∞
T X+∧ Gm× Gm=6∞
T X+∧ Gm⊕6∞
T X+∧ Gm⊕6∞
T X+∧ Gm∧ Gm.
Via this,η is the map
[s]∧[ t]↦→[ st]−[ s]−[ t],
soη[u] sends[t] to[ut]−[ u]−[ t] and idGm∧η[u] sends[s]∧[ t] to[s]∧[ ut]−[ s]∧[ u]−[ s]∧[ t], so
[u]η is given by
[s]∧[ t]↦→[ st]−[ s]−[ t]↦→[ u]∧[ st]−[ u]∧[ s]−[ u]∧[ t].
We have the automorphismξ of G∧3
m sending[u]∧[ s]∧[ t] to[s]∧[ t]∧[ u]. We have the isomorphism in
H•(B),66
S1G∧3
m ≃ A3/A3\{ 0}, via which66
S1ξ is induced by the linear map (u, s, t)↦→(s, t, u). As this
latter linear map has matrix in the standard basis a product of elementary matrices, 66
S1ξ is A1-homotopic
to the identity, so after stabilizing, id Gm∧η[u] is the map
[s]∧[ t]↦→[ s]∧[ t]∧[ u]↦→[ u]∧[ s]∧[ t]↦→[ u]∧[ st]−[ u]∧[ s]−[ u]∧[ t]=[ u]η([s]∧[ t]). □
Lemma 7.5. The projectionη− ofη to SH(B)− is an isomorphism and the projectionη+ ofη to SH(B)+
is zero.
Proof. Morel [2004, §6] proves this in the case of a ﬁeld, but the proof works in general. In some detail,
the mapτ is the map on A2/(A2\{ 0}) induced by the linear map (x, y)↦→(y, x). The matrix identity
(0 1
1 0
)
=
(1 1
0 1
)
·
( 1 0
−1 1
)
·
(1 1
0 1
)
·
(−1 0
0 1
)
shows that the maps (x, y)→(y, x) and(x, y)↦→(−x, y) are A1-homotopic. By the arguments in
Lemma 7.3, this latter map induces the map 1+η[−1]= 1+[− 1]η in SH(B), giving the identity
(1+η[−1])−=(1+[− 1]η)−=− id⇒η·(−[−1]/2)=(−[−1]/2)·η= idSH(B)−
Forη+, the projector to SH(B)+ is given by the idempotent (1/2)(τ+ 1)=(1/2)(2+η[−1]), so
η+=(1/2)η·(2+η[−1]). Since the map τ: P1∧ P1→ P1∧ P1 is 1+η[−1] and P1= S1∧ Gm, the
symmetryϵ: Gm∧ Gm→ Gm∧ Gm is−(1+η[−1]). From our formula for η([s]∧[ t]) we see that
ηϵ=η which givesη·(2+η[−1])= 0. □
1836 Marc Levine and Arpon Raksit
