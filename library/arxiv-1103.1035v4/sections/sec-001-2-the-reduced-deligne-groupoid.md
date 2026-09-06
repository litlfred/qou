---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS AMNON YEKUTIELI"
section_id: sec-001-2-the-reduced-deligne-groupoid
section_title: "The Reduced Deligne Groupoid"
section_number: 2
pages: 9-23
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS AMNON YEKUTIELI — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
groupoid Delr(g, R) deﬁned as follows. The set of objects of this groupoid is
MC(g, R). For any ω, ω′∈ MC(g, R), the set of morphisms ω→ ω′ is the set
Gr(g, R)(ω, ω′) from formula (2.9). The composition in Delr(g, R) is given by for-
mula (2.11), and the identity morphisms are those of the groups G r(g, R)(ω, ω).
There is a morphism of groupoids (i.e. a functor)
(2.13) η = ( η0, η1) : Del(φ, R)→ Delr(φ, R),
where η0 is the identity on the set of objects MC (g, R), and η1 is the surjective
function in formula (2.10). Hence
(2.14) π0
(
Delr(g, R)
)
= π0
(
Del(g, R)
)
= MC(mˆ⊗ g),
where π0(−) denotes the set of isomorphism classes of objects of a groupoid.
Given a homomorphism f : (R, m) → (S, n) of parameter algebras, and a
homomorphism φ : g→ h of DG Lie algebras, there is an induced DG Lie algebra
homomorphism
f⊗ φ : mˆ⊗ g→ nˆ⊗ h.
Hence there are induced morphisms of groupoids Del(φ, f ) and Delr(φ, f ) such
that the diagram
Del(g, R)
Del(φ, f ) //
η

Del(h, S)
η

Delr(g, R)
Delr(φ, f ) // Delr(h, S)
is commutative. And there is an induced function
π0
(
Delr(φ, f )
)
: π0
(
Delr(g, R)
)
→ π0
(
Delr(h, S)
)
.
10 AMNON YEKUTIELI
Under the equality of sets (2.14), and the corresponding one for h and S, we have
equality of functions
(2.15) π0
(
Delr(φ, f )
)
= π0
(
Del(φ, f )
)
= MC( f⊗ φ).
Proposition 2.16. Let ω∈ MC(g, R). The bijection
exp : mˆ⊗ g0→ G(g, R)
induces a bijection (of sets)
exp : H0((mˆ⊗ g)ω)→ Gr(g, R)(ω, ω).
This bijection is functorial w.r.t. homomorphisms (R, m)→ (R, n) of parameter algebras
and homomorphisms g→ h of DG Lie algebras.
Proof. This is an immediate consequence of Lemma 2.7(1,2) and formula (2.9). □
Remark 2.17. After writing an earlier version of this paper, we were told by
M. Manetti that M. Kontsevich had mentioned the idea of a reduced Deligne
groupoid already in 1994. See [Ko1, page 19] and [Mt].
3. DG L ie Quasi-isomorphisms – Nilpotent Algebras
In this section we prove several lemmas that will be used in Section 4. We
assume that (R, m) is an artinian parameter algebra, but m⁄= 0. Also we have a
DG Lie algebra quasi-isomorphism φ : g→ h.
Let
l(R) := min{l∈ N| ml+1 = 0},
and deﬁne n := ml(R). Thus n is an ideal in R satisfying mn = 0. Let ¯R := R/n and
¯m := m/n. So ( ¯R, ¯m) is a parameter algebra, and there is a canonical surjection
p : R→ ¯R.
Our assumption that m⁄= 0 implies that l(R)≥ 1, and that l( ¯R) < l(R).
The homomorphism p : R→ ¯R induces a surjective homomorphism of DG Lie
algebras
p : m⊗ g→ ¯m⊗ g,
and likewise for h. Thus we get a commutative diagram of morphisms of
groupoids
Delr(g, R)
φ //
p

Delr(h, R)
p

Delr(g, ¯R)
φ // Delr(h, ¯R) ,
where, for the sake of brevity, we write p instead of Delr(g, p), etc.
Given elements ω, ω′∈ MC(g, R), let ¯ω := p(ω) and ¯ω′ := p(ω′) in MC(g, ¯R).
For any element ¯g∈ G(g, ¯R)( ¯ω, ¯ω′) we deﬁne
(3.1) G (g, R)(ω, ω′)/ ¯g :={g∈ G(g, R)(ω, ω′)| p(g) = ¯g}.
Next, given an element ¯ω∈ MC(g, ¯R), let us denote by Del(g, R)/ ¯ω the ﬁber
over ¯ω of the morphism of groupoids
p : Del(g, R)→ Del(g, ¯R).
Thus the set of objects of Del(g, R)/ ¯ω is the set
(3.2) MC (g, R)/ ¯ω :={ω∈ MC(g, R)| p(ω) = ¯ω}.
MC ELEMENTS 11
The set of morphisms ω→ ω′ in Del(g, R)/ ¯ω is
(3.3) G (g, R)(ω, ω′)/1 :={g∈ G(g, R)(ω, ω′)| p(g) = 1}.
We shall need some of this construction also for the groupoidDelr(g, R). Given
elements ω, ω′∈ MC(g; R), let ¯ω := p(ω) and ¯ω′ := p(ω′) in MC(g, ¯R). Suppose
¯g∈ Gr(g, ¯R)( ¯ω, ¯ω′). We deﬁne the subset
(3.4) G r(g, R)(ω, ω′)/ ¯g :={g∈ Gr(g, R)(ω, ω′)| p(g) = ¯g}.
We now recall the obstruction functions o2 and o1 introduced in [GM, Section
2.6]. Let us denote by Z i(g) the K-module of i-cocycles in g. For α∈ m⊗ Zi(g)
we shall denote its cohomology class by [α]∈ m⊗ Hi(g)∼= Hi(m⊗ g).
Let
cur : m⊗ g1→ m⊗ g2
be the function
(3.5) cur (ω) := d(ω) + 1
2 [ω, ω].
(“cur” stands for “curvature”.) Thus ω is an MC element iff cur (ω) = 0. Given
¯ω∈ MC(g, ¯R), choose any lift to an element ω∈ m⊗ g1. Then cur (ω)∈ n⊗
Z2(g), and we deﬁne
(3.6) o2( ¯ω) := [cur(ω)]∈ n⊗ H2(g).
It is shown in [GM] that o2( ¯ω) is independent of the choice, and the resulting
obstruction function
o2 : MC(g, ¯R)→ n⊗ H2(g)
has the property that an element ¯ω∈ MC(g, ¯R) lifts to an element of MC (g, R) iff
o2( ¯ω) = 0.
Consider an element ¯ω∈ MC(g, ¯R). The set MC(g, R)/ ¯ω, if it is nonempty, has
a simply transitive action by the additive group n⊗ Z1(g), namely ω↦→ ω + β for
β∈ n⊗ Z1(g). Given ω, ω′∈ MC(g, R)/ ¯ω, deﬁne
(3.7) o1(ω, ω′) := [ ω− ω′]∈ n⊗ H1(g).
The obstruction function
o1 : MC(g, R)/ ¯ω × MC(g, R)/ ¯ω→ n⊗ H1(g)
has the property that the set G (g, R)(ω, ω′)/1 is nonempty iff o1(ω, ω′) = 0.
The obstruction functions o2 and o1 are functorial in g (in the obvious sense).
Remark 3.8. It is possible to deﬁne the obstruction o0 here too, but we will not
use it. Consider the exact sequence of complexes
0→ n⊗ g→ (m⊗ g)ω
p
−→( ¯m⊗ g) ¯ω→ 0.
From the cohomology exact sequence we get a homomorphism
H−1(( ¯m⊗ g) ¯ω)→ n⊗ H0(g).
For g, g′∈ Gr(g, R)(ω, ω′)/ ¯g, the obstruction class o0(g, g′) lives in the cokernel
of this homomorphism.
Lemma 3.9. Let ¯χ∈ MC(h, ¯R), ¯ω∈ MC(g, ¯R), χ∈ MC(h, R)/ ¯χ and
¯h∈ G(h, ¯R)(φ( ¯ω), ¯χ).
Then there exist
ω∈ MC(g, R)/ ¯ω
12 AMNON YEKUTIELI
Figure 1. Illustration for the proof of Lemma 3.9. The diagram is commutative.
and
h∈ G(h, R)(φ(ω), χ)/¯h.
Proof. The proof is very similar to the proof of “Surjective on isomorphism
classes” in [GM, Subsection 2.11]. It is illustrated in Figure 1.
Let
¯χ′ := Af(¯h)−1( ¯χ) = φ( ¯ω)∈ MC(h, ¯R).
Choose any h′∈ G(h, R) lying above ¯h, and let
χ′ := Af(h′)−1(χ)∈ MC(h, R)/ ¯χ′.
Since χ′ exists, the obstruction class o2( ¯χ′) is zero. Now φ( ¯ω) = ¯χ′, so by functo-
riality of the obstruction classes we get
H2(φ)(o2( ¯ω)) = o2( ¯χ′) = 0.
The assumption is that H 2(φ) is injective; hence o2( ¯ω) = 0, and we can ﬁnd
ω′′∈ MC(g, R) lying above ¯ω.
Let χ′′ := φ(ω′′) ∈ MC(h, R)/ ¯χ′. Consider the pair of elements χ′′, χ′ ∈
MC(h, R)/ ¯χ′. There is an obstruction class
o1(χ′′, χ′)∈ n⊗ H1(h).
By assumption the homomorphism H 1(φ) is surjective, so there is is a cohomol-
ogy class c∈ n⊗ H1(g) such that H 1(φ)(c) = o1(χ′′, χ′). Let γ∈ n⊗ Z1(g) be a
cocycle representing c, and deﬁne
ω := ω′′− γ∈ m⊗ g1.
Then ω∈ MC(g, R)/ ¯ω (it is an easy calculation done in [GM]). Let
χ′′′ := φ(ω)∈ MC(h, R)/ ¯χ′.
Now o1(ω′′, ω′) = c, so
o1(χ′′′, χ′) = o1(χ′′, χ′)− o1(χ′′, χ′′′ ) = o1(χ′′, χ′)− H1(φ)(o1(ω′′, ω′)) = 0.
Therefore there exists h′′′∈ G(g, R)(χ′′′, χ′)/1. And we have
h := h′· h′′′∈ G(g, R)(χ′′′, χ)/¯h.
□
MC ELEMENTS 13
Lemma 3.10. Let ω∈ MC(g, R) and χ := φ(ω)∈ MC(h, R).
(1) The homomorphism of DG Lie algebras
φ : (m⊗ g)ω→ (m⊗ h)χ
is a quasi-isomorphism.
(2) The group homomorphism
φ : Gr(g, R)(ω, ω)→ Gr(h, R)(χ, χ)
is an isomorphism.
Proof. (1) This is done by induction on l(R). If l(R) = 1 then m2 = 0, so d ω = d
and dχ = d. Since φ : g→ h is a quasi-isomorphisms, and since m is ﬂat over K,
the assertion is true.
Now assume that l(R)≥ 2. Since mn = 0 it follows that d ω|n⊗g = d|n⊗g; and
likewise for n⊗ h. Let ¯ω := p(ω) and ¯χ := p(χ). We get a commutative diagram
of complexes of R-modules
0 // n⊗ g //
φ

(m⊗ g)ω
p //
φ

( ¯m⊗ g) ¯ω //
φ

0
0 // n⊗ h // (m⊗ h)χ
p // ( ¯m⊗ h) ¯χ // 0
with exact rows. By induction the right vertical arrow is a quasi-isomorphism;
and the left vertical arrow is a quasi-isomorphism by the same argument given in
the case l(R) = 1. Therefore the middle vertical arrow is a quasi-isomorphism.
(2) Combine item (1) above and Proposition 2.16. □
Lemma 3.11. Let ω, ω′∈ MC(g, R), and deﬁne ¯ω := p(ω), ¯ω′ := p(ω′), χ := φ(ω),
χ′ := φ(ω′), ¯χ := φ( ¯ω) and ¯χ′ := φ( ¯ω′). Let
¯g∈ Gr(g, ¯R)( ¯ω, ¯ω′),
¯h := φ( ¯g)∈ Gr(h, ¯R)( ¯χ, ¯χ′),
and
h∈ Gr(h, R)(χ, χ′)/¯h.
Then there exists a unique element
g∈ Gr(g, R)(ω, ω′)/ ¯g
such that φ(g) = h.
Proof. The proof is very similar to the proof of “Full” in [GM, Subsection 2.11].
(Note however that there is a mistake in loc. cit. In our notation, what is done
there is referring to the obstruction class o1(ω, ω′), but this is not deﬁned since
p(ω)⁄= p(ω′) in general.) The proof is illustrated in Figure 2.
Choose an arbitrary lift g′′∈ G(g, R) of ¯g, namely ¯g = p(η1(g′′)). Deﬁne
ω′′ := Af(g′′)(ω)∈ MC(g, R),
h′′ := φ(g′′)∈ G(h, R),
χ′′ := φ(ω′′)∈ MC(h, R)
and
h′ := h· (h′′)−1∈ G(h, R)(χ′′, χ′)/1.
14 AMNON YEKUTIELI
Figure 2. Illustration for the proof of Lemma 3.11. Some of the
arrows, like g and h, belong to the groupoid Delr(−,−). Other
arrows, like g′′ and h′′, belong to the groupoid Del(−,−). The
function φ sends ω↦→ χ, ¯ω↦→ ¯χ, g↦→ h, etc. The whole diagram
is commutative.
Since ω′′, ω′ ∈ MC(g, R)/ ¯ω′ the obstruction class o1(ω′′, ω′) is deﬁned, and it
satisﬁes
H1(φ)(o1(ω′′, ω′)) = o1(χ′′, χ′) = 0
because h′ exists. By assumption the homomorphism H 1(φ) is injective, and we
conclude that o1(ω′′, ω′) = 0. So there exists some g′∈ G(g, R)(ω′′, ω′)/1. Let
g′′′ := g′· g′′∈ G(g, R)(ω, ω′).
Then p(η1(g′′′ )) = ¯g, and hence
η1(g′′′ )∈ Gr(g, R)(ω, ω′)/ ¯g.
By Lemma 3.10(2) we have a group isomorphism
φ : Gr(g, R)(ω, ω)/1→ Gr(h, R)(χ, χ)/1.
Since the set G r(g, R)(ω, ω′)/ ¯g is nonempty (it contains η1(g′′′ )), it admits a sim-
ply transitive action by the group G r(g, R)(ω, ω)/1. Therefore the function
φ : Gr(g, R)(ω, ω′)/ ¯g→ Gr(h, R)(χ, χ′)/¯h
is bijective. We see that there is a unique element g∈ Gr(g, R)(ω, ω′)/ ¯g such that
φ(g) = h. □
4. DG L ie Quasi-isomorphisms – Pronilpotent Algebras
In this section we extend [GM, Theorem 2.4] (attributed to Deligne) to the
case of complete noetherian local rings and unbounded DG Lie algebras. This is
Theorem 4.2.
Let (R, m) be a complete parameter algebra, and let φ : g→ h be a DG Lie
algebra quasi-isomorphism. As in Section 1, for any j∈ N we write Rj := R/mj+1
and mj := m/mj+1. We denote by pj : R→ Rj and pj,i : Rj→ Ri the canonical
MC ELEMENTS 15
projections (for j ≥ i). Let nj := mj/mj+1, which is an ideal in Rj satisfying
mjnj = 0 and
nj = Ker(pj,j−1 : Rj→ Rj−1).
Thus Rj−1∼= Rj/nj.
Lemma 4.1. (1) Let ω∈ MC(g, R) and χ := φ(ω)∈ MC(h, R). Then the homo-
morphism of DG Lie algebras
φ : (mˆ⊗ g)ω→ (mˆ⊗ h)χ
is a quasi-isomorphism.
(2) The canonical function
MC(g, R)→ lim
←j
MC(g, Rj)
is bijective.
(3) For any ω, ω′∈ MC(g, R) the canonical function
Gr(g, R)(ω, ω′)→ lim
←j
Gr(g, Rj)
(
pj(ω), pj(ω′)
)
is surjective.
Of course items (2-3) refer also to h.
Proof. (1) We forget the Lie brackets. Let M be the mapping cone of the homo-
morphism of complexes of R-modules
φ : (mˆ⊗ g)ω→ (mˆ⊗ h)χ.
So
M = ( mˆ⊗ g)ω[1]⊕ (mˆ⊗ h)χ,
with a suitable differential. For any j≥ 0 let ωj := pj(ω) and χj := pj(χ). We
have an inverse system of homomorphisms of complexes
φj : (mjˆ⊗ g)ωj→ (mjˆ⊗ h)χj,
and we denote by Mj the mapping cone of φj. Then each pj : M → Mj is
surjective, and M∼= lim←j Mj. According to Lemma 3.10(1) the complexes Mj
are acyclic. Therefore, using the Mittag-Lefﬂer argument, the complex M is also
acyclic.
(2) This is because mˆ⊗ g1 is m-adically complete, and MC(g, R) is a closed subset
in it (w.r.t. the m-adic metric).
(3) Write ω′
j := pj(ω′). Suppose we are given a sequence {gj}j∈N of elements
gj∈ Gr(g, Rj)(ωj, ω′
j)
such that pj,j−1(gj) = gj−1. We are going to ﬁnd a sequence { ˜gj}j∈N of elements
˜gj∈ G(g, Rj)(ωj, ω′
j)
such that pj,j−1( ˜gj) = ˜gj−1 and η1( ˜gj) = gj for all j. Since the group G (g, R) is
complete w.r.t. its m-adic ﬁltration, the limit
˜g := lim
←j
˜gj∈ G(g, R)
exists; and by continuity ˜g∈ G(g, R)(ω, ω′). Then the element
g := η1( ˜g)∈ Gr(g, R)(ω, ω′)
satisﬁes pj(g) = gj for all j.
16 AMNON YEKUTIELI
Here is the recursive construction of the sequence { ˜gj}j∈N. For j = 0 we
take ˜g0 := 1. Now assume that j≥ 1 and we have a sequence ( ˜g0, . . . ,˜gj−1) as
required. Choose any element ˜g′
j∈ G(g, Rj)(ωj, ω′
j) such that η1( ˜g′
j) = gj. Then
η1(pj,j−1( ˜g′
j)) = pj,j−1(η1( ˜g′
j)) = pj,j−1(gj) = gj−1 = η1( ˜gj−1).
There is some ¯a∈ Nr(g, Rj−1)ωj−1 such that ¯a· pj,j−1( ˜g′
j) = ˜gj−1. Choose any
a ∈ Nr(g, Rj)ωj lifting ¯a. Then ˜gj := a· ˜g′
j will satisfy pj,j−1( ˜gj) = ˜gj−1 and
η1( ˜gj) = gj. □
Here is the main result of this section. We denote the identity automorphism
of R by 1R.
Theorem 4.2. Let (R, m) be a parameter algebra over K, and let φ : g→ h be a DG Lie
algebra quasi-isomorphism over K. Then the function
MC(1R⊗ φ) : MC(mˆ⊗ g)→ MC(mˆ⊗ h)
is bijective. Moreover, the morphism of groupoids
Delr(φ, R) : Delr(g, R)→ Delr(h, R)
is an equivalence.
Observe that there are no ﬁniteness nor boundedness conditions on g and h.
Proof. We will prove these assertions:
(a) The function MC(1R⊗ φ) is surjective.
(b) The function MC(1R⊗ φ) is injective.
(c) For any ω∈ MC(g, R) the group homomorphism
Gr(φ, R) : Gr(g, R)(ω, ω)→ Gr(h, R)
(
φ(ω), φ(ω)
)
is bijective.
Assertions (a-b) say that the function MC(1R⊗ φ) is bijective. Then assertion
(c) implies that the function
φ : Gr(g, R)(ω, ω′)→ Gr(h, R)(φ(ω), φ(ω′))
is bijective for every ω, ω′∈ MC(g, R). Hence Delr(φ, R) is an equivalence.
Proof of (a). Here it is more convenient to work with the groupoids Del(−,−).
Suppose we are given χ∈ MC(h, R). We will ﬁnd elements ω∈ MC(g, R) and
h∈ G(h, R)(φ(ω), χ).
Deﬁne χj := pj(χ)∈ MC(h, Rj). We are going to ﬁnd a sequence {ωj}j∈N of
elements ωj∈ MC(g, Rj), and a sequence{hj}j∈N of elements
hj∈ G(h, Rj)(φ(ωj), χj),
such that pj,j−1(ωj) = ωj−1 and pj,j−1(hj) = hj−1 for all j. This is done by
induction on j. For j = 0 we take ω0 := 0 and h0 := 1 = exp(0). Now consider
j≥ 1. Assume that we have found sequences (ω0, . . . ,ωj−1) and (h0, . . . ,hj−1)
satisfying the required conditions. By Lemma 3.9, applied to the artinian local
ring Rj, and the elements χj, ωj−1 and hj−1, there exist elements ωj and hj as
required.
Now the R-module mˆ⊗ g1 is m-adically complete, and the set MC (g, R) is
closed inside mˆ⊗ g1 (with respect to the m-adic metric). Hence the limit ω :=
MC ELEMENTS 17
lim←j ωj belongs to MC (g, R). The gauge group G (h, R) is complete, since it is
pronilpotent (with respect to its m-adic ﬁltration). We get an element
h := lim
←j
hj∈ G(h, R).
By continuity we see that Af (h)(φ(ω)) = χ.
Proof of (b). Here we prefer to work with the groupoids Delr(−,−). Take ω, ω′∈
MC(g, R), and deﬁne χ := φ(ω) and χ′ := φ(ω′). Suppose we are given h∈
Gr(h, R)(χ, χ′); we will ﬁnd g∈ Gr(g, R)(ω, ω′). (We do not care whether φ(g) =
h or not.)
Deﬁne ωj := pj(ω), ω′
j := pj(ω′), χj := pj(χ), χ′
j := pj(χ′) and hj := pj(h).
We will ﬁnd a sequence {gj}j∈N of elements gj ∈ Gr(g, Rj)(ωj, ω′
j) such that
φ(gj) = hj and pj,j−1(gj) = gj−1. Then, by Lemma 4.1(3) there is an element
g∈ Gr(g, R)(ω, ω′) such that pj(g) = gj for every j.
We construct the sequence{gj}j∈N by induction on j. For j = 0 we take g0 := 1.
Now let j≥ 1, and suppose that we have a sequence (g0, . . . ,gj−1) as required.
According to Lemma 3.11, applied to the artinian local ring Rj, there exists an
element gj∈ Gr(g, Rj)(ωj, ω′
j) such that pj,j−1(gj) = gj−1 and φ(gj) = hj.
Proof of (c). This is the complete version of the proof of Lemma 3.10(2). By
Lemma 4.1(1) the function H 0(φR,ω) is bijective. The claim now follows from
Proposition 2.16. □
Remark 4.3. Assume g is abelian (i.e. the Lie bracket is zero), so that mˆ⊗ g is just
a complex of R-modules, and
MC(g, R) = H1(mˆ⊗ g).
In this case the Deligne groupoid Del(g, R) is the truncation
···→ 0→ mˆ⊗ g0→ Ker
(
d : mˆ⊗ g1→ mˆ⊗ g2)
→ 0→··· ,
whereas as the reduced Deligne groupoid Delr(g, R) is the truncation
···→ 0→ Im
(
d : mˆ⊗ g−1→ mˆ⊗ g0)
→ Ker
(
d : mˆ⊗ g1→ mˆ⊗ g2)
→ 0→··· ,
both concentrated in the degree range [0, 1]. Let h be another abelian DG Lie
algebra. It is clear that a quasi-isomorphism of complexes φ : g→ h will induce
a quasi-isomorphism
Delr(φ, R) : Delr(g, R)→ Delr(h, R).
This is a special case of Theorem 4.2.
Remark 4.4. Presumably Theorem 4.2 can be extended to the following more
general situation: g and h are R-linear DG Lie algebras, such that all the R-
modules gi and hi are m-adically complete, and the graded Lie algebras gr m(g)
and grm(h) are abelian. We are given an R-linear DG Lie algebra homomorphism
φ : g→ h such that
grm(φ) : grm(g)→ grm(h)
is a quasi-isomorphism. Then
MC(φ) : MC(g)→ MC(h)
is bijective. Cf. [Ge, Theorem 2.1] for the corresponding nilpotent case.
18 AMNON YEKUTIELI
5. S ome Facts on 2-Groupoids
Let us recall that a (strict) 2 -groupoid G is a groupoid enriched in the monoidal
category of groupoids. Another way of saying this is that a 2-groupoid G is a
2-category in which all 1-morphisms and 2-morphisms are invertible. A com-
prehensive review of 2-categories and related constructions is available in [Ye3,
Section 1]. See also [Ma, Bw, Ge].
We wish to make things as explicit as possible, to make calculations (both in
Section 6 of this paper, and in the new version of [Ye4]) easier. A (small strict) 2-
groupoid G is made up of the following ingredients: there is a set Ob (G), whose
elements are the objects of G. For any x, y∈ Ob(G) there is a set G(x, y), whose
elements are called the 1 -morphisms from x to y. Given f ∈ G(x, y), we write
f : x→ y. For any f , g∈ G(x, y) there is a set G(x, y)( f , g), whose elements are
called the 2-morphisms from f to g. For a∈ G(x, y)( f , g) we write a : f⇒ g.
There are three types of composition operations in G. There is horizontal com-
position of 1-morphisms: given f1 : x0→ x1 and f2 : x1→ x2, their composition
is f2◦ f1 : x0→ x2. Suppose we are also given 1-morphisms gi : xi−1→ xi and
2-morphisms ai : fi⇒ gi. Then there is a 2-morphism
a2◦ a1 : f2◦ f1⇒ g2◦ g1.
This is horizontal composition of 2-morphisms. If we are also given
1-morphisms hi : xi−1 → xi and 2-morphisms bi : gi ⇒ hi, then there is the
vertical composition (of 2-morphisms) bi∗ ai : fi⇒ hi. There are pretty diagrams
to display all of this (see [Ye3, Section 1] or many other references).
For every x∈ Ob(G) there is the identity 1-morphism 1x : x→ x, and for
every f∈ G(x, y) there is the identity 2-morphism 1 f : f⇒ f .
Here are the conditions required for the structure G to be a 2-groupoid:
• The set Ob (G), together with the 1-morphisms f : x → y, horizontal
composition g◦ f , and the identity morphisms 1x, is a groupoid. We refer
to this groupoid as the 1-truncation of G.
• For every x, y∈ Ob(G), the set G(x, y), together with the 2-morphisms
a : f⇒ g, vertical composition b∗ a, and the identity morphisms 1 f , is a
groupoid. We refer to it as the vertical groupoid above (x, y).
• Horizontal composition of 2-morphisms is associative, 1g◦ f = 1g◦ 1 f
whenever g and f are composable, and the 2-morphisms 11x are iden-
tities for horizontal composition.
• The exchange condition: given fi, gi, hi : xi−1 → xi, ai : fi ⇒ gi and
bi : gi⇒ hi, one has
(b2∗ a2)◦ (b1∗ a1) = ( b2◦ b1)∗ (a2◦ a1),
as 2-morphisms f2◦ f1⇒ h2◦ h1.
A consequence of these four conditions is that 2-morphisms are invertible for
horizontal composition. Indeed, given a : f⇒ g in G(x, y), its horizontal inverse
a−◦ : f−1⇒ g−1 is given by the formula a−◦ = 1g−1◦ a−∗◦ 1 f−1, where a−∗ : g⇒
f is the vertical inverse of a.
Suppose H is another 2-groupoid. A (strict) 2 -functor F : G→ H is a collection
of functions
MC ELEMENTS 19
F : Ob(G)→ Ob(H)
F : G(x0, x1)→ H
(
F(x0), F(x1)
)
F : G(x0, x1)(g0, g1)→ H
(
F(x0), F(x1)
)(
F(g0), F(g1)
)
that respect the various compositions and identity morphisms. We denote by
2-Grpd the category consisting of 2-groupoids and 2-functors between them.
Consider a 2-groupoid G. There is an equivalence relation on the set Ob (G),
given by existence of 1-morphisms, i.e. x∼ y if G(x, y)⁄= ∅. We let π0(G) :=
Ob(G)/∼.
For objects x, y∈ Ob(G) there is an equivalence relation on the set G(x, y),
given by existence of 2-morphisms: f∼ g if G(x, y)( f , g)⁄= ∅. We let
π1(G, x, y) := G(x, y)/∼.
We deﬁne π1(G) to be the groupoid with object set Ob (G),
morphism sets π1(G, x, y), and composition induced by horizontal composition
in G. Thus π1(G) is a quotient groupoid of the 1-truncation of G, and
π0(π1(G)) = π0(G). We write π1(G, x) := π1(G, x, x), which is a group. We
also deﬁne
π2(G, x) := G(x, x)(1x, 1x).
This is an abelian group.
The homotopy set π0(G) and groups πi(G, x) are functorial in an obvious way.
A morphism F : G→ H in 2-Grpd is called a weak equivalence if the functions
π0(F) : π0(G)→ π0(H)
π1(F, x) : π1(G, x)→ π1(H, F(x))
π2(F, x) : π2(G, x)→ π2(H, F(x))
are bijective for all x∈ Ob(G).
It will be useful to relate the concept of 2-groupoid to the less familiar concept
of crossed module over a groupoid, recalled below.
For a groupoid G and an object x∈ Ob(G) we denote by G(x) := G(x, x), the
automorphism group of x. The composition in G is◦ =◦G.
Let G and N be groupoids, such that Ob (G) = Ob(N). An action Ψ of G on N
is a collection of group isomorphisms
Ψ(g) : N(x) ≃− →N(y)
for all x, y∈ Ob(G) and g∈ G(x, y), such that
Ψ(h◦ g) = Ψ(h)◦ Ψ(g)
whenever g and h are composable, and Ψ(1x) = 1N(x).
Example 5.1. Let G be any groupoid. The adjoint action Ad G of G on itself is
deﬁned by
AdG(g)(h) := g◦ h◦ g−1
for g∈ G(x, y) and h∈ G(x).
A crossed module over a groupoid , or a crossed groupoid for short, is data
(G, N, Ψ, D) consisting of:
• Groupoids G and N, such that N is totally disconnected, and Ob (N) =
Ob(G).
• An action Ψ of G on N, called the twisting.
20 AMNON YEKUTIELI
• A morphism of groupoids (i.e. a functor) D : N→ G, called the feedback,
which is the identity on objects.
These are the conditions:
(i) The morphism D is G-equivariant with respect to the actions Ψ and AdG.
Namely
D(Ψ(g)(a)) = AdG(g)(D(a))
in the group G(y), for any x, y∈ Ob(G), g∈ G(x, y) and a∈ N(x).
(ii) For any x∈ Ob(G) and a∈ N(x) there is equality
Ψ(D(a)) = AdN(x)(a),
as automorphisms of the group N(x).
Example 5.2. If G and N are groups, namely Ob (G) = Ob(N) = {0}, then a
crossed groupoid is just a crossed module.
Example 5.3. Let G be a group acting on a set X. For x∈ X let G(x) denote
the stabilizer of x. Let{Nx}x∈X be a collection of groups. Assume that for every
g ∈ G and x ∈ X there is given a group isomorphism Ψ(g) : Nx
≃− →Ng(x),
and these satisfy the functoriality conditions of an action. Also assume there are
group homomorphisms D x : Nx→ G(x) such that
AdG(g)◦ Dx = Dg(x)◦ Ψ(g)
for any g∈ G and x∈ X.
Deﬁne G to be the transformation groupoid associated to the action of G on
X. And deﬁne N to be the totally disconnected groupoid with Ob (N) := X
and N(x) := Nx. Then (G, N, Ψ, D) is a crossed groupoid, which we call the
transformation crossed groupoid associated to the action of G on{Nx}x∈X.
Example 5.4. Suppose G is any groupoid, and N is a normal subgroupoid of G,
in the sense of [Bw, Ye4]. Let D : N → G be the inclusion, and let Ψ be the
restriction of AdG to N. Then (G, N, Ψ, D) is a crossed groupoid.
It is known that crossed groupoids are the same as 2-groupoids (cf. [Bw]). We
will now give a precise statement of this fact.
Proposition 5.5. Let (H, N, Ψ, D) be a crossed groupoid. Then there is a unique 2-
groupoid G with these properties:
(i) The 1-truncation of G is the same groupoid as H. Namely Ob(G) = Ob(H),
G(x, y) = H(x, y), the identity morphisms 1x are the same, and the horizontal
composition is g◦G f = g◦H f for f : x→ y and g : y→ z.
(ii) For any f , g : x→ y in G we have
G(x, y)( f , g) ={a∈ N(x)| g = f◦H D(a)}.
The identity morphism 1 f ∈ G(x, y)( f , f ) is 1x∈ N(x). Given h : x→ y,
a : f⇒ g and b : g⇒ h, the vertical composition is b∗G a = a◦N b.
(iii) For any x 0, x1, x2∈ Ob(G), any f i, gi : xi−1→ xi and any a i : fi⇒ gi in G,
the horizontal composition a 2◦G a1 satisﬁes
a2◦G a1 = Ψ( f−1
1 )(a2)◦N a1.
Moreover, any 2-groupoid G arises this way.
MC ELEMENTS 21
Proof. It is easy to verify that the conditions of a 2-groupoid hold.
Conversely, suppose G is any 2-groupoid. Deﬁne the groupoid G1 to be the
1-truncation of G.
For any x∈ Ob(G) consider the set of 2-morphisms
(5.6) G2(x) := ∐
g∈G(x,x)
G(x, x)(1x, g).
This is a group under horizontal composition ◦G of 2-morphisms, with identity
element 11x. There is a group homomorphism D : G2(x)→ G1(x), deﬁned by
(5.7) D (a : 1x⇒ g) := g.
Let G2 be the totally disconnected groupoid with set of objects Ob (G), and auto-
morphism groups G2(x) as deﬁned above. Then D : G2→ G1 is a morphism of
groupoids.
A 1-morphism f : x→ y in G induces a group isomorphism
AdG1↷G2 ( f ) : G2(x)→ G2(y),
with formula
(5.8) Ad G1↷G2 ( f )(a) := 1 f◦ a◦ 1 f−1
for a∈ G2(x). It is a simple veriﬁcation that (G1, G2, AdG1↷G2, D) is a crossed
groupoid. □
Remark 5.9. An amusing consequence of the proof above is that the vertical
composition in a 2-groupoid can be recovered from the horizontal compositions.
In view of Proposition 5.5, in a 2-groupoid G we can talk about the group of
2-morphisms G2(x) for any object x. There is a feedback homomorphism
D : G2(x)→ G1(x),
and a twisting
Ad(g) = AdG1↷G2 (g) : G2(x)→ G2(y)
for any g : x→ y. These satisfy the conditions of a crossed groupoid.
6. T he Deligne 2-Groupoid
Deﬁnition 6.1. A DG Lie algebra g = ⨁
i∈Z gi is said to be of quantum type if
gi = 0 for all i <−1.
A DG Lie algebra ˜g =⨁
i∈Z ˜gi is said to be of quasi quantum type if there exists a
quantum type DG Lie algebra g, and a DG Lie algebra quasi-isomorphism ˜g→ g.
Example 6.2. Let C be a commutative K-algebra. The DG Lie algebras Tpoly(C)
andDpoly(C) that occur in deformation quantization are of quantum type (and
hence the name).
Let g be a quantum type DG Lie algebra. Consider the DG Lie algebra ˜g :=
(L◦ C)(g); this is the bar-cobar construction discussed in Section 7. There is a
quasi-isomorphism ζg : ˜g→ g, so ˜g is of quasi quantum type (but is unbounded
in the negative direction).
Suppose g is a quantum type DG Lie algebra, and R is artinian. Then the
Deligne 2-groupoid of m⊗ g is deﬁned; see [Ge]. In this section we show how this
construction can be extended in two ways: g can be of quasi quantum type, and
R can be complete (i.e. not artinian).
22 AMNON YEKUTIELI
Now let g be any DG Lie algebra, and (R, m) any parameter algebra. We have
the set MC(mˆ⊗ g) of MC elements, and the gauge group exp (mˆ⊗ g0).
Given ω ∈ MC(mˆ⊗ g) there is an R-bilinear function [−,−]ω on mˆ⊗ g−1,
whose formula is
(6.3) [α1, α2]ω := [dω(α1), α2],
where dω = d + ad(ω).
Deﬁne
(6.4) aω := Coker(dω : mˆ⊗ g−2→ mˆ⊗ g−1),
so there is an exact sequence of R-modules
(6.5) mˆ⊗ g−2 dω
−→mˆ⊗ g−1→ aω→ 0.
Proposition 6.6. Take any ω∈ MC(mˆ⊗ g).
(1) Let α∈ mˆ⊗ g−1 and β∈ mˆ⊗ g−2. Write α′ := dω(β)∈ mˆ⊗ g−1. Then
[α, α′]ω, [α′, α]ω∈ dω(m⊗ g−2).
(2) The induced R-bilinear function [−,−]ω on aω is a Lie bracket. Thus aω is a Lie
algebra.
(3) Let g∈ exp(mˆ⊗ g0), and let ω′ := Af(g)(ω)∈ MC(mˆ⊗ g). Then
Ad(g) : aω→ aω′
is an isomorphism of Lie algebras.
Proof. (1) and (2) are easy direct calculations. (3) is a consequence of Proposition
1.15. □
Proposition 6.7. Assume either of these two conditions holds :
(i) R is artinian.
(ii) g is of quasi quantum type.
Then for any ω∈ MC(mˆ⊗ g) the R-module aω is m-adically complete. Hence aω is a
pronilpotent Lie algebra.
Proof. If R is artinian then any R-module is m-adically complete.
Now assume R is not artinian (namely it is a complete noetherian ring). If g
is of quantum type then aω = mˆ⊗ g−1, which is m-adically complete (cf. [Ye5,
Corollary 3.5]).
For any DG Lie algebra g the canonical homomorphism
(6.8) τω : aω→ˆaω = lim
←i
(Ri⊗R aω)
is surjective. Here is the reason: the completion functor M↦→ ˆM is not exact
(neither right nor left exact), but it does preserve surjections (see [Ye5, Proposition
1.2]). Combining this with the exact sequence (6.5), and the fact that mˆ⊗ g−1 is
complete, it follows that the homomorphism τω is surjective.
It remains to prove that if there exists a DG Lie algebra quasi-isomorphism
φ : g→ h, for some quantum type DG Lie algebra h, then the homomorphism τω
is injective. Since d ω : aω→ mˆ⊗ g0 factors through ˆaω, it follows that
Ker(τω)⊂ Ker(dω : aω→ mˆ⊗ g0) = H−1(mˆ⊗ g)ω.
MC ELEMENTS 23
Let χ := φ(ω). We have a commutative diagram with exact rows
0 // H−1(mˆ⊗ g)ω //
H−1(1ˆ⊗ φ)

aω
dω //

(mˆ⊗ g0)ω

0 // H−1(mˆ⊗ h)χ // aχ
dχ // (mˆ⊗ h0)χ .
Because φ is a quasi-isomorphism, so is
1ˆ⊗ φ : (mˆ⊗ g)ω→ (mˆ⊗ h)χ
(we are using Lemma 4.1(1)). Hence the vertical arrow H−1(1ˆ⊗ φ) in the diagram
is an isomorphism of R-modules. It sends Ker (τω) bijectively to Ker (τχ : aχ→
ˆaχ). We know that aχ is complete, so Ker (τχ) = 0. □
Corollary 6.9. In the situation of Proposition 6.7, for every ω∈ MC(mˆ⊗ g) there is a
pronilpotent group Nω := exp(aω), and a group homomorphism
Dω := exp(dω) : Nω→ exp(mˆ⊗ g0)(ω).
Given any g ∈ exp(mˆ⊗ g0) and ω ∈ MC(mˆ⊗ g), let ω′ := Af(g)(ω) ∈
MC(mˆ⊗ g). Then there is a group isomorphism
Ψ(g) := exp(Ad(g)) : Nω
≃− →Nω′,
and the diagram
Nω
Ψ(g)

Dω // exp(mˆ⊗ g0)(ω)
Ad(g)

Nω′
Dω′ // exp(mˆ⊗ g0)(ω′)
is commutative. The isomorphisms Ψ(g) are an action of the group exp(mˆ⊗ g0) on the
collection of groups{Nω}ω∈MC(mˆ⊗ g).
Moreover, for any a, a′∈ Nω we have
Ψ(Dω(a))(a′) = AdNω (a)(a′).
Proof. Combine Propositions 1.15, 6.6 and 6.7. □
Remark 6.10. The Lie algebra ar
ω and the group Nr
ω that occur in Section 2 are
quotients, respectively, of the Lie algebra aω and the group Nω that occur here.
Deﬁnition 6.11. Let g be a DG Lie algebra and R a parameter algebra. Assume
either of these two conditions holds:
(i) R is artinian.
(ii) g is of quasi quantum type.
