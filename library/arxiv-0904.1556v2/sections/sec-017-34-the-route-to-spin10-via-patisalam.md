---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-017-34-the-route-to-spin10-via-patisalam
section_title: "The Route to Spin(10) via Pati–Salam"
section_number: 3.4
pages: 55-62
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
doc_brief: "The Algebra of Grand Unified Theories — The Standard Model is the best tested and most widely accepte d theory of elementary particles we have today."
---
In the last section, we showed how the Pati–Salam model answers tw o questions
about the Standard Model:
Why are quarks and leptons so similar? Why are left and right so
diﬀerent?
We were able to describe leptons as a fourth color of quark, ‘white’, a nd treat
right-handed and left-handed particles on a more equal footing. N either of these
ideas worked on its own, but together, they made a full-ﬂedged ext ension of the
Standard Model, much like SU(5) and Spin(10), but based on seeming ly diﬀerent
principles.
55
Yet thinking of leptons as ‘white’ should be strangely familiar, not jus t from the
Pati–Salam perspective, but from the binary code that underlies bo th the SU(5)
and the Spin(10) theories. There, leptons were indeed white: they all have color
r ∧g ∧b ∈ Λ C5.
Alas, while SU(5) hints that leptons might be a fourth color, it does no t deliver
on this. The quark colors
r,g,b ∈ Λ 1C5
lie in a diﬀerent irrep of SU(5) than does r ∧g ∧b ∈ Λ 3C5. So, leptons in the
SU(5) theory are white, but unlike the Pati–Salam model, this theory does not
unify leptons with quarks.
Yet SU(5) theory is not the only game in town when it comes to the bina ry
code. We also have Spin(10), which acts on the same vector space a s SU(5). As
a representation of Spin(10), Λ C5 breaks up into just two irreps: the even grades,
Λ evC5, which contain the left-handed particles and antiparticles:
Λ evC5 ∼
= ⟨
νL⟩ ⊕ ⟨e+
L ⟩ ⊕
⟨ uL
dL
⟩
⊕ ⟨
uL⟩ ⊕
⟨ νL
e−
L
⟩
⊕ ⟨
dL⟩
and the odd grades Λ oddC5, which contain the right-handed particles and antipar-
ticles:
Λ oddC5 ∼
= ⟨νR⟩ ⊕ ⟨e−
R⟩ ⊕
⟨
dR
uR
⟩
⊕ ⟨uR⟩ ⊕
⟨
e+
R
νR
⟩
⊕ ⟨dR⟩.
Unlike SU(5), the Spin(10) GUT really does unify r ∧g ∧b with the colors r,g and
b, because they both live in the irrep Λ oddC5.
In short, it seems that the Spin(10) GUT, which we built as an extens ion of the
SU(5) GUT, somehow managed to pick up this feature of the Pati–Sa lam model.
How does Spin(10) relate to Pati–Salam’s gauge group SU(2) × SU(2) × SU(4),
exactly? In general, we only know there is a map SU( n) → Spin(2n), but in low
dimensions, there is much more, because some groups coincide:
Spin(3) ∼
= SU(2)
Spin(4) ∼
= SU(2) × SU(2)
Spin(5) ∼
= Sp(2)
Spin(6) ∼
= SU(4)
What really stands out is this:
SU(2) × SU(2) × SU(4) ∼
= Spin(4) × Spin(6).
This brings out an obvious relationship between the Pati–Salam model and the
Spin(10) theory, because the inclusion SO(4) ×SO(6)֒→SO(10) lifts to the universal
covers, so we get a homomorphism
η: Spin(4) × Spin(6) → Spin(10).
A word of caution is needed here. While η is the lift of an inclusion, it is not an
inclusion itself: it is two-to-one. This is because the universal cover Spin(4)×Spin(6)
of SO(4) × SO(6) is a four-fold cover, being a double cover on each factor.
So we can try to extend the symmetries SU(2) × SU(2) × SU(4) to Spin(10),
though this can only work if the kernel of η acts trivially on the Pati–Salam repre-
sentation. What is this representation like? There is an obvious repr esentation of
56
Spin(4) × Spin(6) that extends to a Spin(10) rep. Both Spin(4) and Spin(6) h ave
Dirac spinor representations, so their product Spin(4) ×Spin(6) has a representation
on Λ C2 ⊗ Λ C3. And in fact, the obvious map
g: Λ C2 ⊗ Λ C3 → Λ C5
given by
v ⊗w ↦→v ∧w
is an isomorphism compatible with the actions of Spin(4) × Spin(6) on these two
spaces. More concisely, this square:
Spin(4) × Spin(6)
η /d47/d47
/d15/d15
Spin(10)
/d15/d15
U(Λ C2 ⊗ Λ C3)
U(g) /d47/d47 U(Λ C5)
commutes.
We will prove this in a moment. First though, we must check that this r ep-
resentation of Spin(4) × Spin(6) is secretly just another name for the Pati–Salam
representation of SU(2) × SU(2) × SU(4) on the space we discussed in Section 3.3:
(
(C2 ⊗ C) ⊕ (C ⊗ C2)
)
⊗
(
C4 ⊕ C4∗)
.
Checking this involves choosing an isomorphism between SU(2) × SU(2) × SU(4)
and Spin(4) × Spin(6). Luckily, we can choose one that works:
Theorem 4. There exists an isomorphism of Lie groups
α: SU(2) × SU(2) × SU(4) → Spin(4) × Spin(6)
and a unitary operator
k:
(
(C2 ⊗ C) ⊕ (C ⊗ C2)
)
⊗
(
C4 ⊕ C4∗)
→ Λ C2 ⊗ Λ C3
that make this square commute:
SU(2) × SU(2) × SU(4) α /d47/d47
/d15/d15
Spin(4) × Spin(6)
/d15/d15
U
((
(C2 ⊗ C) ⊕ (C ⊗ C2)
)
⊗
(
C4 ⊕ C4∗)) U(k) /d47/d47 U(Λ C2 ⊗ Λ C3)
where the left vertical arrow is the Pati–Salam representat ion and the right one is
a tensor product of Dirac spinor representations.
Proof. We can prove this in pieces, by separately ﬁnding a unitary operator
(C2 ⊗ C) ⊕ (C ⊗ C2) ∼
= Λ C2
that makes this square commute:
SU(2) × SU(2) ∼ /d47/d47/d15/d15
Spin(4)
/d15/d15
U(C2 ⊗ C ⊕ C ⊗ C2)
∼ /d47/d47 U(Λ C2)
57
and a unitary operator
C4 ⊕ C4∗ ∼
= Λ C3
that make this square:
SU(4) ∼ /d47/d47/d15/d15
Spin(6)
/d15/d15
U(C4 ⊕ C4∗)
∼ /d47/d47 U(Λ C3)
commute.
First, the Spin(6) piece. It suﬃces to show that the Dirac spinor re p of Spin(6) ∼
=
SU(4) on Λ C3 is isomorphic to C4 ⊕ C4∗ as a rep of SU(4). We start with the action
of Spin(6) on Λ C3. This breaks up into irreps:
Λ C3 ∼
= Λ evC3 ⊕ Λ oddC3
called the left-handed and right-handed Weyl spinors , and these are dual
to each other because 6 = 2 mod 4, by a theorem that can be found in Adams’
lectures [1]. Call these representations
ρev: Spin(6) → U(Λ evC3), ρ odd: Spin(6) → U(Λ oddC3).
Since these reps are dual, it suﬃces just to consider one of them, s ayρodd.
Passing to Lie algebras, we have a homomorphism
dρodd: so(6) → u(Λ oddC3) ∼
= u(4) ∼
= u(1) ⊕ su(4).
Homomorphic images of semisimple Lie algebras are semisimple, so the ima ge of
so(6) must lie entirely in su(4). In fact so(6) is simple, so this nontrivial map must
be an injection
dρodd: so(6) → su(4),
and because the dimension is 15 on both sides, this map is also onto. Th usdρodd is
an isomorphism of Lie algebras, so ρodd is an isomorphism of the simply connected
Lie groups Spin(6) and SU(4):
ρodd: Spin(6) → SU(Λ oddC3) ∼
= SU(4).
Furthermore, under this isomorphism
Λ oddC3 ∼
= C4
as a representation of SU(Λ oddC3) ∼
= SU(4). Taking duals, we obtain an isomor-
phism
Λ evC3 ∼
= C4∗
Putting these together, we get an isomorphism C4 ⊕ C4∗ ∼
= Λ C3 that makes this
square commute:
Spin(6)
/d15/d15
ρodd /d47/d47 SU(4)
/d15/d15
U(Λ C3) /d47/d47 U(C4 ⊕ C4∗)
which completes the proof for Spin(6).
58
Next, the Spin(4) piece. It suﬃces to show that the spinor rep Λ C2 of Spin(4) ∼
=
SU(2) × SU(2) is isomorphic to C2 ⊗ C ⊕ C ⊗ C2 as a rep of SU(2) × SU(2). We
start with the action of Spin(4) on Λ C2. This again breaks up into irreps:
Λ C2 ∼
= Λ oddC2 ⊕ Λ evC2.
Again we call these representations
ρev: Spin(4) → U(Λ evC2), ρ odd: Spin(4) → U(Λ oddC2).
First consider ρev. Passing to Lie algebras, this gives a homomorphism
dρev: so(4) → u(Λ evC2) ∼
= u(2) ∼
= u(1) ⊕ su(2)
Homomorphic images of semisimple Lie algebras are semisimple, so the ima ge of
so(4) must lie entirely in su(2). Similarly, dρodd also takes so(4) to su(2):
dρodd: so(4) → su(2)
and we can combine these maps to get
dρodd ⊕dρev: so(4) → su(2) ⊕ su(2),
which is just the derivative of Spin(4)’s representation on Λ C2. Since this repre-
sentation is faithful, the map dρodd ⊕dρev of Lie algebras is injective. But the
dimensions of so(4) and su(2) ⊕ su(2) agree, so dρodd ⊕dρev is also onto. Thus it is
an isomorphism of Lie algebras. This implies that ρodd ⊕ρev is an isomorphism of
the simply connected Lie groups Spin(4) and SU(2) × SU(2)
ρodd ⊕ρev: Spin(4) → SU(Λ oddC2) × SU(Λ evC2) ∼
= SU(2) × SU(2)
under which SU(2) × SU(2) acts on Λ oddC2 ⊕ Λ evC2. The left factor of SU(2) acts
irreducibly on Λ oddC2, which the second factor is trivial on. Thus Λ oddC2 ∼
= C2 ⊗ C
as a rep of SU(2) × SU(2). Similarly, Λ evC2 ∼
= C⊗ C2 as a rep of this group. Putting
these together, we get an isomorphism C2 ⊗ C ⊕ C ⊗ C2 ∼
= Λ C2 that makes this
square commute:
Spin(4)
/d15/d15
ρev⊕ρodd /d47/d47 SU(2) × SU(2)
/d15/d15
U(Λ C2) /d47/d47 U(C2 ⊗ C ⊕ C ⊗ C2)
which completes the proof for Spin(4). ⊓ ⊔
In the proof of the preceding theorem, we merely showed that the re exists an
isomorphism
k:
(
(C2 ⊗ C) ⊕ (C ⊗ C2)
)
⊗
(
C4 ⊕ C4∗)
→ Λ C2 ⊗ Λ C3
making the square commute. We did not say exactly what k was. In the proof, we
built it after quietly choosing three unitary operators, giving these isomorphisms:
C2 ⊗ C ∼
= Λ oddC2, C ⊗ C2 ∼
= Λ evC2, C4 ∼
= Λ oddC3.
Since the remaining map Λ evC3 ∼
= C4∗ is determined by duality, these three oper-
ators determine k, and they also determine the Lie group isomorphism α via the
construction in our proof.
59
There is, however, a speciﬁc choice for these unitary operators t hat we prefer,
because this choice makes the particles in the Pati–Salam represent ation Λ C2 ⊗Λ C3
look almost exactly like those in the SU(5) representation Λ C5.
First, since C2 = Λ 1C2 = Λ oddC2 is spanned by u and d, the (left-handed)
isospin states of the Standard Model, we really ought to identify the left-isospin
states uL and dL of the Pati–Salam model with these. So, we should use this
unitary operator:
C2 ⊗ C
∼
− → Λ oddC2
uL ↦→ u
dL ↦→ d.
Next, we should use this unitary operator for right-isospin states :
C ⊗ C2 ∼
− → Λ evC2
uR ↦→ u ∧d
dR ↦→ 1.
Why? Because the right-isospin up particle is the right-handed neut rino νR, which
corresponds to u ∧d ∧r ∧g ∧b in the SU(5) theory, but uR ⊗w in the Pati–Salam
model. This suggests that u ∧d and uR should be identiﬁed.
Finally, because C3 is spanned by the colors r, g and b, while C4 is spanned by
the colors r, g, b and w, we really ought to use this unitary operator:
C4 ∼
− → Λ oddC3
r ↦→ r
g ↦→ g
b ↦→ b
w ↦→ r ∧g ∧b
Dualizing this, we get the unitary operator
C4∗ ∼
− → Λ evC3
r ↦→ g ∧b
g ↦→ b ∧r
b ↦→ r ∧g
w ↦→ 1
These choices determine the unitary operator
k:
(
(C2 ⊗ C) ⊕ (C ⊗ C2)
)
⊗
(
C4 ⊕ C4∗)
→ Λ C2 ⊗ Λ C3.
With this speciﬁc choice of k, we can combine the commutative squares built in
Theorems 3 and 4:
GSM
β /d47/d47
/d15/d15
SU(2) × SU(2) × SU(4) α /d47/d47
/d15/d15
Spin(4) × Spin(6)
/d15/d15
U(F ⊕F ∗)
U(ℓ) /d47/d47 U
((
(C2 ⊗ C) ⊕ (C ⊗ C2)
)
⊗
(
C4 ⊕ C4∗)) U(k) /d47/d47 U(Λ C5)
to obtain the following result:
60
Theorem 5. Takingθ =αβ and h =kℓ, the following square commutes:
GSM
θ /d47/d47
/d15/d15
Spin(4) × Spin(6)
/d15/d15
U(F ⊕F ∗)
U(h) /d47/d47 U(Λ C2 ⊗ Λ C3)
where the left vertical arrow is the Standard Model represen tation and the right one
is a tensor product of Dirac spinor representations.
The map h, which tells us how to identify F ⊕F ∗ and Λ C2 ⊗ Λ C3, is given by
applying k to the ‘Pati–Salam code’ in Table 5. This gives a binary code for the
Pati–Salam model:
The Binary Code for Pati–Salam
Λ oddC2 ⊗ Λ oddC3 Λ evC2 ⊗ Λ oddC3 Λ oddC2 ⊗ Λ evC3 Λ evC2 ⊗ Λ evC3
νL =u ⊗rgb ν R =ud ⊗rgb e +
R =u ⊗ 1 e+
L =ud ⊗ 1
e−
L =d ⊗rgb e −
R = 1 ⊗rgb
νR =d ⊗ 1 νL = 1 ⊗ 1
uc
L =u ⊗c u c
R =ud ⊗c
d
c
R =u ⊗
c d
c
L =ud ⊗
c
dc
L =d ⊗c d c
R = 1 ⊗c
uc
R =d ⊗
c uc
L = 1 ⊗
c
Table 6: Pati–Salam binary code for ﬁrst-generation fermions, whe rec =r,g,b and
c =gb,br,rg .
We have omitted wedge product symbols to save space. Note that if we apply the
obvious isomorphism
g: Λ C2 ⊗ Λ C3 → Λ C5
given by
v ⊗w ↦→v ∧w
then the above table does more than merely resemble Table 4, which g ives the
binary code for the SU(5) theory. The two tables become identical!
This fact is quite intriguing. We will explore its meaning in the next sectio n.
But ﬁrst, let us start by relating the Pati–Salam model to the Spin(1 0) theory:
Theorem 6. The following square commutes:
Spin(4) × Spin(6)
η /d47/d47
/d15/d15
Spin(10)
/d15/d15
U(Λ C2 ⊗ Λ C3)
U(g) /d47/d47 U(Λ C5)
where the right vertical arrow is the Dirac spinor represent ation, the left one is the
tensor product of Dirac spinor representations, and
η: Spin(4) × Spin(6) → Spin(10)
is the homomorphism lifting the inclusion of SO(4) × SO(6) in SO(10).
61
Proof. At the Lie algebra level, we have the inclusion
so(4) ⊕ so(6)֒→so(10)
by block diagonals, which is also just the diﬀerential of the inclusion SO (4) ×
SO(6)֒→SO(10) at the Lie group level. Given how the spinor reps are deﬁned
in terms of creation and annihilation operators, it is easy to see that
so(4) ⊕ so(6)/d31 /d127 /d47/d47
/d15/d15
so(10)
/d15/d15
gl(Λ C2 ⊗ Λ C3)
gl(g) /d47/d47 gl(Λ C5)
commutes, because g is an intertwining operator between representations of so(4) ⊕
so(6). That is because the so(4) part only acts on Λ C2, while the so(6) part only
acts on Λ C3.
But these Lie algebras act by skew-adjoint operators, so really
so(4) ⊕ so(6)/d31 /d127 /d47/d47
/d15/d15
so(10)
/d15/d15
u(Λ C2 ⊗ Λ C3)
u(g) /d47/d47 u(Λ C5)
commutes. Since the so(n)’s and their direct sums are semisimple, so are their
images. Therefore, their images live in the semisimple part of the unita ry Lie
algebras, which is just another way of saying the special unitary Lie algebras. We
get that
so(4) ⊕ so(6)/d31 /d127 /d47/d47
/d15/d15
so(10)
/d15/d15
su(Λ C2 ⊗ Λ C3)
su(g) /d47/d47 su(Λ C5)
commutes, and this gives a commutative square in the world of simply c onnected
Lie groups:
Spin(4) × Spin(6)
η /d47/d47
/d15/d15
Spin(10)
/d15/d15
SU(Λ C2 ⊗ Λ C3)
SU(g) /d47/d47 SU(Λ C5)
This completes the proof. ⊓ ⊔
This result shows us how to reach the Spin(10) theory, not throug h the SU(5)
theory, but through the Pati–Salam model. For physics texts that treat this issue,
see for example Zee [40] and Ross [31].
