---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POL YNOMIAL LINK INVARIANT"
section_id: sec-006-31-parameters
section_title: "Parameters"
section_number: 3.1
pages: 6-12
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POL YNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant J n K and the so(2n + 1) knot invariant soJ n K studied by"
---
Notation 3.1. We borrow much of our notation in this section from [10]. Given an element m in
some /CI × /CI
2-graded module M , we denote p(m) to be the parity of m, |m| denotes the /CI -degree of m
and ||m|| = (|m|, p(m)).
Let us review some notions from [ 10, Section 2.2].
Let t ∈ C such that t2 = −1. Let q be a formal parameter, let τ be a formal parameter such that
τ 4 = 1, and deﬁne π := τ 2. Recall the notation Rπ = R[π]/(π2 − 1) and Rτ = R[τ ]/(τ 4 − 1) for a
commutative ring R with 1. Our base ring is Q(q, t)τ .
For x ∈ {±1, ±t}, let Q(q, t)x := Q(q, t) viewed as a Q(q, t)τ -module where τ acts by multiplication
by x.
Deﬁnition 3.2. The specialization of Q(q, t)τ -module M at x is the Q(q, t)-module
M |τ =x = Q(q, t)x ⊗Q(q,t)τ M
Q(q, t)τ has orthogonal idempotents
εtk = 1 + (tkτ ) + (tkτ )2 + (tkτ )3
4 0 ≤ k ≤ 3,
such that Q(q, t)τ =⨁
k∈ /CI
4 Q(q, t)εtk .
Furthermore, since τ εx = xεx, we see that
M |τ =x = εxM.
A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INV ARIANT AND CATEGORIFICATION 7
3.2. Quantum covering group.
Deﬁnition 3.3. [7] The quantum covering group Uq,π := Uq,π(sl2) is the Q(q, t)τ -algebra with gener-
ators E, F, K ±1, J, subject to the relations
J 2 = 1 J K = KJ(3.1)
J E = EJ J F = F J(3.2)
KE = q2EK KF = q−2F K(3.3)
EF − πF E = J K − K −1
πq − q−1(3.4)
It has structure of a Hopf superalgebra[ 7, 8, 10] but with braiding replaced by x⊗ y → πp(x)p(y)y ⊗ x.
The coproduct ∆ : Uq,π → Uq,π ⊗ Uq,π is
∆( E) = E ⊗ 1 + J K ⊗ E ∆( F ) = F ⊗ K −1 + 1 ⊗ F ∆( K) = K ⊗ K ∆( J) = J ⊗ J
The antipode S : Uq,π → Uq,π is
S(E) = −J −1K −1E S (F ) = −F K S (K) = K −1 S(J) = J
The counit ε : U → Q(q, t)τ
ε(E) = ε(F ) = 0 ε(J) = ε(K) = 1
3.3. Uq,π-modules.
Deﬁnition 3.4. [10, Section 2.4] A weight Uq,π-module M is a /CI × /CI
2 graded U -module, whose grading
is compatible with the grading on U such that
M =
⨁
λ∈ /CI
Mλ,0 ⊕ Mλ,1 Mλ,s = {m ∈ M | p(m) = s, J m = πλm, Km = qλm}
The simple weight U -module of highest weight m with highest weight vector vm of even parity
(||vm|| = ( m, 0)) is denoted V (m). It has basis {vm−2k := F (k)vm}0≤k≤m. By convention we have
p(vm−2k) ≡ k(mod 2). The action of Uq,π on V (m) is given by
Evm−2k = πk−1[m + 1 − k]vm−2(k−1) Kv m−2k = qm−2kvm−2k
F vm−2k = [k + 1]vm−2(k+1) J vm−2k = πm−2kvm−2k
Deﬁne the parity reversed module Π M to be M as a vector space equipped with the same action
of Uq,π, but with (Π M )λ,s = Mλ,1−s. In particular, the identity map induces an odd U -module
isomorphism γV (m) : V (m) → Π V (m).
For the purposes of this paper, it is enough to consider the case wh ere m = 1. As a superspace, the
Uq,π-module V := V (1) is given by the span of elements {v+, v−} with /CI × /CI
2 degrees ||v+|| = (1 , 0)
and ||v−|| = (−1, 1). The action of Uq,π on V is given by
Ev− = v+ Ev+ = 0 Kv ± = q±1v±
F v+ = v− F v− = 0 J v± = π±1v±
Then Π V = span {v′
+, v′
−} as a superspace where the /CI × /CI
2 degrees of the basis elements are
||v′
+|| = (1 , 1) and ||v′
−|| = ( −1, 0). By deﬁnition, the action of Uq,π on Π V is the same as the action
on V .
Ev ′
− = v′
+ Ev ′
+ = 0 Kv ′
± = q±1v′
±
F v′
+ = v′
− F v′
− = 0 J v′
± = π±1v′
±
8 MARK EBERT
Thus, the identity map induces an odd U -module isomorphism γV : V → Π V which sends v± → v′
±.
The dual module M ∗ is deﬁned to be
M ∗ =
⨁
λ∈ /CI
(Mλ,0)∗ ⊕ (Mλ,1)∗ (Mλ,s)∗ = Hom Q(q,t)τ (Mλ,s, Q(q, t)τ )
The action on M ∗ is induced by the Hopf superalgebra structure of Uq,π: For x ∈ Uq,π,
xf (v) = πp(f )p(x)f (S(x)v).
Let us consider M = V (m). Then V (m)∗ has a dual basis {v∗
m−2k}0≤k≤m with ||v∗
m−2k|| = (2 k −
m, k).
Ev ∗
m−2k = −(πq−1)m−2k[m − k]v∗
m−2(k+1)
F v∗
m−2k = −πkqm−2k+2[k]v∗
m−2(k−1)
We prove the action of F is correct.
F v∗
m−2k(vα) = πkv∗
m−2k(S(F )vα) = πkv∗
m−2k(−F Kvα)
= −πkδα−2,m−2kqαv∗
m−2k(F vα) = −δα−2,m−2kπkqm−2k+2v∗
m−2k(F vm−2(k−1))
= −δα−2,m−2kπkqm−2k+2[k]v∗
m−2k(vα−2) = −πkqm−2k+2[k]v∗
m−2(k−1)(vα)
V (m)∗ is a weight module with highest weight vector v∗
−m. This has degree ||v∗
−m|| = ( m, m), so
there is an even Uq,π-module isomorphism Π mV (m) → V (m)∗.
3.4. Clark’s osp(1|2) invariant. In this subsection, we review how Clark obtains the uncolored
osp(1|2) link invariant in simplest case done in [ 10, Example 3.10]. Clark actually deﬁnes a colored
osp(1|2n)-invariant, but we only consider the uncolored case with n = 1. All of the material in this
subsection comes from [ 10, Section 2, Section 3].
Notation 3.5. We use the ordered basis
{v+ ⊗ v+, v+ ⊗ v−, v− ⊗ v+, v− ⊗ v−} for V ⊗ V
{v∗
+ ⊗ v+, v∗
+ ⊗ v−, v∗
− ⊗ v+, v∗
− ⊗ v−} for V ∗ ⊗ V
{v+ ⊗ v∗
+, v+ ⊗ v∗
−, v− ⊗ v∗
+, v− ⊗ v∗
−} for V ⊗ V ∗
Recall the Q(q, t)τ -linear maps from [ 10, Lemma 2.7].
• ev : V (1)∗ ⊗V (1) → Q(q, t)τ is the map v∗ ⊗w → v∗(w). It is given by the matrix
(
1 0 0 1
)
• qtr : V (1) ⊗ V (1)∗ → Q(q, t)τ is the map v ⊗ w∗ → πp(v)p(w)q−|v|w∗(v). It is given by the
matrix
( q−1 0 0 πq)
• coev : Q(q, t)τ → V (1)∗ ⊗ V (1) given by 1 → qv+ ⊗ v+ + πq−1v− ⊗ v− It is given by the matrix

q
0
0
πq−1


• coqtr : Q(q, t)τ → V (1) ⊗ V (1)∗ is map 1 → v+ ⊗ v+ + v− ⊗ v−. It is given by the matrix


1
0
0
1


as well as the quasi R-matrix
A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INV ARIANT AND CATEGORIFICATION 9
R1,1 : V (1) ⊗ V (1) → V (1) ⊗ V (1) given by the matrix


1 0 0 0
0 0 q 0
0 πq 1 − πq2 0
0 0 0 1


and its inverse R−1
1,1 given by the matrix


1 0 0 0
0 1 − πq−2 πq−1 0
0 q−1 0 0
0 0 0 1

.
So far, we can do everything in this section in the subring Q(q)π ⊂ Q(q, t)τ , but need to renormalize
the maps using π = τ 2 to get a link invariant. In particular, the maps qtr and R1,1 pick up a factor of τ ,
while coev and R−1
1,1 pick up a factor of τ 3. The renormalized maps have a diagrammatic interpretation
using red strands that can be used to obtain the Uq(osp(1|2)) link invariant.
= τ 3coev =


τ 3q
0
0
τ q−1

 = coqtr =


1
0
0
1


(3.5)
= τ qtr =
(
τ q−1 0 0 τ 3q
)
= ev =
(
1 0 0 1
)(3.6)
= τ R1,1 =


τ 0 0 0
0 0 τ q 0
0 τ 3q τ − τ 3q2 0
0 0 0 τ

 = τ 3R−1
1,1 =


τ 3 0 0 0
0 τ 3 − τ q−2 τ q−1 0
0 τ 3q−1 0 0
0 0 0 τ 3


(3.7)
Theorem 3.6. [10, Theorem 3.8, Corollary 3.9] There is a covariant functor J from the category
of oriented tangles to the category of ﬁnite dimensional Uq,π-modules that sends a tangle T to the
associated Uq,π-module homomorphism deﬁned using 3.5 and multiplying the resulting homomorphism
by (πq)wr(T ). In particular, L is an oriented link, then J 1
L = J(L) is Clark’s osp(1|2)-link invariant
[10, Example 3.10] .
In [ 10, Example 3.10], Clark showed that the red maps 3.5 satisfy
− q2 = ( τ − τ 3q2)
This shows that J 1
L satisﬁes the skein relation 1.1. Then taking the specialization τ = t, which
correpsonds to π = −1, he concludes that the uncolored Uq(osp(1|2)) link invariant is equal to the
Uτ −1q(sl2) link invariant.
3.5. Representation theoretic deﬁniton of ˆJ. For the purposes of categoriﬁcation, we want to
deﬁne the invariant ˆJ deﬁned in section 1 using Uq,π-module homomorphisms. To do this, we need
to deﬁne Uq,π-module homomorphisms u : Q(q, t)τ → V ⊗ V and n : V ⊗ V → Q(q, t)τ satisfying the
relation τ R1,1 = τ Id − qun. Then this gives the sl2 invariant in the variable τ −1q as desired.
Deﬁnition 3.7. Let n : V ⊗ V → Q(q, t)τ be the odd Q(q, t)τ -linear map deﬁned on basis elements by
v+ ⊗ v+ → 0 v+ ⊗ v− → −τ 3
v− ⊗ v− → 0 v− ⊗ v+ → τ 3q
10 MARK EBERT
Theorem 3.8. n is a odd weight Uq,π-module homomorphism.
Proof. We need to show that n(∆( E)v ⊗ w) = n(∆( F )v ⊗ w) = 0. We know that ∆( E)(v+ ⊗ v+) =
∆( F )(vi⊗v−) = 0, so it holds in these cases. It is also trivial to see that ∆( E)(v±⊗v∓) ∈ span{v+⊗v+},
which is sent to 0 by n. Likewise, ∆( F )(v± ⊗ v∓) ∈ span{v− ⊗ v−}, which is sent to 0 by n. Thus, all
that remains to check is that ∆( F )(v+ ⊗ v+) and ∆( E)(v− ⊗ v−) are sent to 0 by n.
n((E ⊗ 1 + J K ⊗ E)(v− ⊗ v−)) = n(v+ ⊗ v− + πJ Kv− ⊗ Ev−) = n(v+ ⊗ v− + q−1v− ⊗ v+) = 0
n((F ⊗ K −1 + 1 ⊗ F )(v+ ⊗ v+)) = n(q−1v− ⊗ v+ + v+ ⊗ v−) = 0
Therefore, n(∆( x)(v ⊗ w)) = x · n(v ⊗ w) = 0 for all x ∈ { E, F } and v, w ∈ V , which implies n is a
module homomorphism. □
We associate a blue cap with no orientation to this map
= n =
(
0 −τ 3 τ 3q 0
)
(3.8)
Deﬁnition 3.9. Let u : Q(q, t)τ → V ⊗ V be the odd Q(q, t)τ -linear map deﬁned by
1 → −πq−1v+ ⊗ v− + v− ⊗ v+
Theorem 3.10. u is a an odd weight Uq,π-module homomorphism.
Proof. We need to show that ∆( x)u(1) = 0 for x ∈ {E, F }.
∆( E)u(1) = ( E ⊗ 1)(v− ⊗ v+) + (J K ⊗ E)(−πq−1v+ ⊗ v−) = v+ ⊗ v+ − πq−1J Kv+ ⊗ Ev−
= v+ ⊗ v+ − v+ ⊗ v+ = 0
∆( F )u(1) = ( F ⊗ K −1)(−πq−1v+ ⊗ v−) + (1 ⊗ F )(v− ⊗ v+) = −πq−1v− ⊗ K −1v− + πv− ⊗ v−
= −πv− ⊗ v− + πv− ⊗ v− = 0
□
We associate a cup without orientation to the map u
= u =


0
−πq−1
1
0

(3.9)
Then nu = τ q−1 + τ 3q.
Deﬁne E′ = un : V ⊗ V → V ⊗ V . E′ is the even map
= E′ = un =


0
−πq−1
1
0


( 0 −τ 3 τ 3q 0)
=


0 0 0 0
0 τ q−1 −τ 0
0 −τ 3 τ 3q 0
0 0 0 0


We can derive all the relations in ( 2.1), ( 2.2), and ( 2.3) with this understanding of the cap and cup
as Uq,π-module homomorphisms.
A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INV ARIANT AND CATEGORIFICATION 11
=


τ 0 0 0
0 0 τ q 0
0 τ 3q τ − τ 3q2 0
0 0 0 τ

 = τ Id − q


0 0 0 0
0 τ q−1 −τ 0
0 −τ 3 τ 3q 0
0 0 0 0

 = τ − q
=


τ 3 0 0 0
0 τ 3 − τ q−2 τ q−1 0
0 τ 3q−1 0 0
0 0 0 τ 3

 = τ 3Id − q−1


0 0 0 0
0 τ q−1 −τ 0
0 −τ 3 τ 3q 0
0 0 0 0

 = τ 3 − q−1
= nu =
( 0 −τ 3 τ 3q 0)


0
−πq−1
1
0

 = τ q−1 + τ 3q
= (1 ⊗ n) ◦ (u ⊗ 1) : V → V
This is the map sending
v±
u⊗1
→ − πq−1v+ ⊗ v− ⊗ v± + v− ⊗ v+ ⊗ v±
1⊗n
→ − πq−1v+ ⊗ n(v− ⊗ v±) + πv− ⊗ n(v+ ⊗ v±) = −τ v±.
Hence,
= −τ
The other zig-zag straightens up to a diﬀerent power of τ .
= (n ⊗ 1) ◦ (1 ⊗ u) : V → V
Note that (1 ⊗ u) : V → V ⊗ V ⊗ V is the map sending
v± = v± ⊗ 1 → πp(v±)v± ⊗ u(1) = πp(v±)(−πq−1v± ⊗ v+ ⊗ v− + v± ⊗ v− ⊗ v+).
Thus, ( n ⊗ 1) ◦ (1 ⊗ u) is the map sending
v+
1⊗u
→ (−πq−1v+ ⊗ v+ ⊗ v− + v+ ⊗ v− ⊗ v+)
n⊗1
→ − τ 3v+
v−
1⊗u
→ π(−πq−1v− ⊗ v+ ⊗ v− + v− ⊗ v− ⊗ v+)
n⊗1
→ − τ 3v−.
Hence,
= −τ 3
12 MARK EBERT
Therefore, we also have the relation
= =
Therefore, ˆJ can be understood using representation theory of Uq,π.
Deﬁnition 3.11. Let d := τ 3q + τ q−1. Deﬁne σi ∈ Bn using the positive crossing involving strands i
and i + 1. Then deﬁne ρq,τ : Bn → T Ln(d) given by
ρq,τ (σi) = ( τ Id − qEi).
Theorem 3.12. ρq,τ : Bn → T Ln(d) deﬁnes a Bn-representation inside T Ln(d), namely a group
homomorphism from Bn to the group of invertible elements of T Ln(d).
