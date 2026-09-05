---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-011-33-compactly-supported-cohomology
section_title: "Compactly supported cohomology"
section_number: 3.3
pages: 38-42
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
Let E be a spectrum object of PShv∗(B), a model for which is as a functor Bop→ Spectra. Now,
Corollary 1.4.4.5 of [Lu2] grants that a ﬁnite limit preserving functor f rom a stable ∞-category to
Spaces canonically factors through Spectra
Ω ∞
−−→Spaces. In particular, for S a stable ∞-category,
the Yoneda functor Sop× S→ Spaces canonically factors through Spectra
Ω ∞
−−→Spaces. In particular,
there is a factorization of the Yoneda functor
MapPShv∗(B)(−, Ω ∞E) : PShv∗(B)op E−
−−→Spectra
Ω ∞
−−→Spaces∗ ,
the ﬁrst of which is symmetric monoidal with respect to coproduct o n the source and on the target,
and the second of which is symmetric monoidal with respect to copro duct on the source and product
on the target. We will denote the composite symmetric monoidal fun ctor
(3.3.1) Ec : Mﬂd(B)ﬁn τ +
−−→PShvﬁn
∗ (B)op E−
−−→Spectra
where here the target is equipped with the symmetric monoidal stru cture given by wedge sum. We
will use the notation
AE := ( Ec)| Disk(B)∈ AlgDisk(B)(Spectra)
for the restriction. We give notation for the relative version:
EX + : Mﬂd(B)/X +
τ X+
−−−→PShv∗(B)
E−
−−→Spectra .
38
Proposition 3.5 (Compactly supported cohomology) . Let E be a spectrum object of PShv∗(B).
Then the symmetric monoidal functor Ec : Mﬂd(B)→ Spectra satisﬁes⊗-excision. In particular,
the canonical map ∫
−
AE
≃
−−→Ec(−)
is an equivalence of symmetric monoidal functors Mﬂd(B)ﬁn→ Spectra.
Proof. Let X∼=X−
⋃
R×X0
X+ be a collar-gluing among B-manifolds. After Lemma 3.4, there is the
pullback diagram among spectra
Ec(X +) /d47/d47
/d15/d15
EX + (X+)
/d15/d15
EX + (X−) /d47/d47 EX + (R×X0) .
Thereafter, using the canonical identiﬁcation Ω EX + (R×X0)≃ Ec(R×X0) and Lemma 3.4 again,
there is the pushout diagram of spectra
Ec(X0) /d47/d47
/d15/d15
Ec(X+)
/d15/d15
Ec(X−) /d47/d47 Ec(X +) .
Because we are equipping spectra with wedge sum, which is its catego rical coproduct, the forgetful
functor AlgAssRL (Spectra)
≃
− →Fun
(
(−← 0→ +), Spectra
)
is an equivalence; and, for ( P←A→Q)
an object of this functor category, regarded as an AssRL-algebra in Spectra, then the canonical map
from the pushout P ∐
A
Q
≃
− →P ⨂
A
Q is an equivalence of spectra. And so, we have veriﬁed that Ec
satisﬁes⊗-excision.
□
Specializing Proposition 3.5 to the case that E = S : Bop→ Spectra is the constant functor at the
sphere spectrum, we have the following classical consequence. Fo r this case, we will use the special
notation
D
(
(−)+)
:= Sc(−) , and ω := AS .
This notation is invoked because, for each B-manifold X, the spectrum D(X +) is the Spanier-
Whitehead dual of the 1-point compactiﬁcation of the underlying sp ace of X; and the value of ω on
a basic U is D(U +), the stalk of the dualizing sheaf for the site Mﬂd(B) at U .
Immediate from the present deﬁnitions is the following result.
Proposition 3.6. Let B = BO(n), so that a B-manifold is an ordinary smooth n-manifold. Let
X be smooth n-manifold that is the interior of a compact manifold with bou ndary. Then there is a
canonical identiﬁcation
X −τX≃
∫
X
ω
from the Thom spectrum of the virtual negative of the tangent bundle of X.
Corollary 3.7 (Atiyah duality). Let X be a ﬁnitary B-manifold. Then there is a canonical iden-
tiﬁcation ∫
X
ω ≃ D(X +) .
More generally, for each functor E : Bop→ Spectra, there is a canonical identiﬁcation∫
X
E∧ω ≃ Ec(X) .
39
Example 3.8 (Classical Poincar´ e duality). Let us consider the case B = Dor
n so that a B-manifold
is an oriented smooth n-manifold; and an oriented n-manifold X that is the interior of a compact
manifold with boundary; and E = HZ : ( Dor
n )op→ Spectra is the constant functor at the Eilenberg-
MacLane spectrum for Z. Identify HZc(X)≃ HZX +
as the mapping spectrum from the 1-point
compactiﬁcation. For each object U∈ Dor
n there is a canonical identiﬁcation HZ∧ω(U )≃ HZ∧S−n≃
Ω nHZ. And so, there is a canonical equivalence of spectra
∫
X HZ∧ω ≃ Ω nHZ∧X+. Putting these
identiﬁcation into Corollary 3.7 arrives at a canonical equivalence of s pectra: Ω nHZ∧X+ ≃ HZX +
.
Upon taking homotopy groups, indexed appropriately, we arrive at classical Poincar´ e duality:
H∗(X; Z)∼= Hn−∗
c (X; Z) .
3.4. Non-abelian Poincar´ e duality
Deﬁnition 3.9 (Coeﬃcient system) . A coeﬃcient system (for B-manifolds) is a pointed presheaf
on B. Let E be a coeﬃcient system. The compactly supported sections functor is the composition
of the symmetric monoidal functors
Γ E
c : Mﬂd(B)ﬁn τ +
−−→PShvﬁn
∗ (B)op MapPShv∗ (B)(−,E)
−−−−−−−−−−−→Spaces∗
where the target is equipped with the symmetric monoidal structur e given by product. We denote
the resulting Disk(B)-algebra
AE :=
(
Γ E
c
)
| Disk(B) ∈ AlgDisk(B)(Spaces∗) .
Example 3.10. Consider a ﬂag of maps of based spaces Zop
≥0
Z•
− − →Spaces∗. It corresponds to a right
ﬁbrationZ→ Z≥0, equipped with a section. In [AFT] is constructed the functor Depth : Bsc→ Z≥0.
There results the coeﬃcient system Depth∗Z→ Bsc.
Example 3.11. Let B = Dfr
n≃∗ . Then a coeﬃcient system is equivalent to the datum of a based
space Z. Such a coeﬃcient system is connective, in the sense of Deﬁnition 3.1 4, exactly if Z is
n-connective.
Example 3.12. A coeﬃcient system on D∂
n is map of ﬁbrations
En−1 /d47/d47
/d15/d15
En
/d15/d15
BO(n− 1) /d47/d47 BO(n)
together with a pair of (compatible) sections of each.
Consider the more elaborate example D⟨n⟩ codifying smooth n-manifolds with corners. A coeﬃ-
cient system on D⟨n⟩ is the data of a ﬁbration ES→ BO(RS) for each subset S⊂{ 1,...,n }, and for
each inclusion S⊂T a map ES→ET over the inclusion BO(RS)
−⊕RT /integerdivideS
−−−−−−→BO(RT ), which respect
composition; together with a compatible section of each of these ﬁb rations.
We now concern ourselves with the question of when Γ E
c is a homology theory. We will only
consider this question in the case that there is an integer n≥ 0 such that each basic U∈ B has
pure dimension n – that is to say, the local topological dimension at each point in the un derlying
stratiﬁed space equals n. To address the problem, it is convenient to extend Γ E
c to stratiﬁed spaces
X equipped with a B-structure on Rn−k×X for somek. Here are the relevant temporary deﬁnitions.
40
Deﬁnition 3.13 (Mﬂd(Bk)). Letk be an integer. Denote the ∞-categories which are the pullbacks
Bk /d47/d47
/d15/d15
Mﬂd(Bk)
Rn−r×− /d47/d47
/d15/d15
Mﬂd(B)
/d15/d15
Bsc ι /d47/d47 Snglr
Rn−k×− /d47/d47 Snglr.
Denote the composite functor
Γ E
c : Mﬂd(Bk)
(
(−1,1)n−k⊂Rn−k
)
×−
−−−−−−−−−−−−−−−→Fun
(
[1], Mﬂd(B)
) Entr
(
ev0(−)ev1(−)+
)
−−−−−−−−−−−−−→Spaces∗ .
Explicitly, this functor evaluates as
Γ E
c : X ↦→ Entr
( (
(−1, 1)n−k×X
)
(Rn−k×X)+
)
which we think of as “sections of E|Rn−k×X that are compactly supported in the X-direction”.
Deﬁnition 3.14. Let B be a category of basics each of pure dimension n. Say the coeﬃcient system
E is connective if the based space Γ E
c (V ) is connected for every V ∈ Bk with k <n.
Example 3.15. Consider the case B = Dfr
n≃∗ . Here, a connective coeﬃcient system is the datum
of an n-connective based space Z, and the associated Diskfr
n-algebra is Ω nZ. This Diskfr
n-algebra is
group-like. Through May’s recognition principle there is an equivalence of ∞-categories between
connective coeﬃcient systems for framed n-manifolds, and that of group-like En-spaces. Accordingly,
one can think of the data of a connective coeﬃcient system as a gen eralization of the notion of a
group-like algebra, for the structured stratiﬁed setting.
Example 3.16. Let us return to Example 3.12 for the case of D∂
n. For simplicity, let us assume the
two ﬁbrations are trivialized with (based) ﬁbers Zn andZn−1 respectively. This coeﬃcient system is
connective exactly if Zn isn-connective and the map Zn−1→Zn isn-connective; the last condition
being equivalent to saying the homotopy ﬁber F of the map Zn−1 → Zn is (n− 1)-connective.
Indeed, for this coeﬃcient system to be connective, then both Γ E
c (Rk)≃ Ω kZn and Γ E
c (Hk)≃ Ω kF
must be connected for each k < n. Now, recall from Example 2.13 a consolidation of the data of
a Disk∂
n-algebra. The associated Disk∂
n-algebra AE is the data (Ω nZn, Ω n−1F,α ) where α is the
action of Ω nZn on Ω n−1F from the Ω-Puppe sequence of the ﬁbration F→Zn−1→Zn.
Remark 3.17. The previous example can be generalized to the case of D⟨n⟩, as we indicate here.
For simplicity, let us assume each of the said ﬁbrations is trivial with re spective ﬁbers ZS. Denote
by FT = hoﬁb(ZT → holimS⊊ TZS) the total homotopy ﬁber of the T -subcube. This coeﬃcient
system is connective exactly if each FT is (n−|T|)-connective. The associated Disk⟨n⟩-algebra AE
is the data
(
(Ω n/integerdivideSFS
)
S⊂{1,...,n};
(
aS⊂T )
)
whereaS⊂T is the action of Ω n/integerdivideSFS on Ω n/integerdivideTFT from an
elaboration of the Ω-Puppe sequence.
Theorem 3.18. (Non-abelian Poincar´ e duality) Let B be an ∞-category of basics each of pure
dimension n. Let E be a connective coeﬃcient system for B-manifolds. Then the canonical arrow
∫
−
AE
≃
−−→Γ E
c (−)
is an equivalence of functors Mﬂd(B)ﬁn→ Spaces∗.
Proof. From Theorem 2.43, we must show Γ E
c : Mﬂd(B)→ Spaces satisﬁes excision. Consider a
collar-gluing X ∼= X−
⋃
R×X0
X+ among Bk-manifolds where −1≤ k≤ n. We will show that the
canonical map
Γ E
c (X−)
⨂
Γ Ec (R×V )
Γ E
c (X+)−→ Γ E
c (X) ,
41
is an equivalence; the desired case is k =n. There is the sequence of maps of pointed spaces
(3.4.1) Γ E
c (X−)× Γ E
c (X+)→ Γ E
c (X)→ Γ E
c (X0) ,
which is a ﬁber sequence because of Lemma 3.4 applied to the modiﬁed c ollar-gluing X∼= (X−⊔
X+) ⋃
R×(X0⊔X0)
R×X0. It is suﬃcient to show that the base of this ﬁber sequence is conne cted. We
will do this by induction on k.
Let Y be a ﬁnitary Bk manifold. If k =−1, then Γ E
c (Y )≃∗ is terminal. In particular it is
connected. So suppose Γ E
c (W ) is connected for each Bj manifold W for j < k. From Theorem 1,
Y can be witnessed as a ﬁnite iteration of collar-gluings of basics. We pr ove Γ E
c (Y ) is connected by
induction on the minimal number r of iterated collar-gluings to obtain Y . If r = 0 the statement
is vacuously true. If Y is a basic then Γ E
c (Y ) is connected, by the connectivity assumption. If
r≥ 2, write Y = Y−
⋃
R×W
Y+ with each of the Bk-manifolds Y± witnessed through strictly fewer
than r collar-gluings, and with W a Bk−1-manifold. By induction on r, each of the spaces Γ E
c (Y±)
is connected. As in (3.4.1), there is the ﬁber sequence of pointed sp aces
Γ E
c (Y−)× Γ E
c (Y+)→ Γ E
c (Y )→ Γ E
c (W ) ;
now the base is connected, by induction on k. It follows that Γ E
c (Y ) is connected. □
Remark 3.19. We elaborate on Example 3.15. The space of stratiﬁed continuous ma ps is a
homotopy invariant of the underlying stratiﬁed space X. In this sense, Theorem 3.18 tells us that
connective coeﬃcient systems (think, ‘ Disk(B)-spaces that are group-like’) cannot detect more than
the stratiﬁed proper homotopy type of B-manifolds.
