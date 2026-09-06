---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-012-31-discrete-groups-of-isometries
section_title: "Discrete groups of isometries"
section_number: 3.1
pages: 81-86
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We deﬁne hyperbolic manifolds and prove a crucial theorem, that says that
every complete hyperbolic manifold is isometric to a quotientHn/Γ for some
discrete group Γ< Isom(Hn) acting freely onHn.
3.1.1. Hyperbolic, ﬂat, and elliptic manifolds.We introduce three im-
portant classes of Riemannian manifolds.
Deﬁnition 3.1.1. Ahyperbolic (resp. ﬂator elliptic) manifold is a con-
nected Riemanniann-manifold that may be covered by open sets isometric to
open sets ofHn (resp. Rn oSn).
A hyperbolic (resp. ﬂat or elliptic) manifold has constant sectional curva-
ture−1 (resp. 0 or +1). We show that the modelHn is indeed unique.
Theorem 3.1.2. Every complete simply connected hyperbolicn-manifold
M is isometric toHn.
Proof. Pick a pointx∈M and choose an isometryD :U→V between an
open ballU containingx and an open ballV ⊂ Hn. We show thatD extends
(uniquely) to an isometryD :M→ Hn.
For everyy ∈ M, choose an arcα: [0, 1]→ M from x to y. By com-
pactness there is a partition 0 = t0 < t1 < ... < tk = 1 and for each
73
74 3. HYPERBOLIC MANIFOLDS
i = 0,...,k − 1 an isometryDi :Ui→Vi from an open ballUi inM containing
α([ti,ti+1]) to an open ballVi⊂ Hn.
We may suppose thatU0⊂U and D0 =D|U0. Inductively oni, we now
modify Di so thatDi−1 and Di coincide on the componentC of Ui−1∩Ui
containingα(ti ). To do so, note that
Di−1◦D−1
i :Di (C)−→Di−1(C)
is an isometry of open connected sets inHn and hence extends to an isometry
of Hn. Then it makes sense to composeDi withDi−1◦D−1
i , so that the new
mapsDi−1 andDi coincide onC. Finally, we deﬁneD(y ) =Dk−1(y ).
The proof thatD(y ) is well-deﬁned is a standard argument. First, it is
easy to check that diﬀerent partitions0 = t0 < ... < tk = 1 do not vary
D(y ), just by considering a common reﬁnement. Then we consider another
pathβ connectingx toy. SinceM is simply-connected, there is a homotopy
connecting α and β. The image of the homotopy is compact and is hence
covered by ﬁnitely many open ballsUi isometric to open ballsVi⊂ Hn via some
mapsDi. By the Lebesgue number theorem, there is aN >0 such that in the
grid in [0, 1]× [0, 1] of 1
N× 1
N squares, the image of every square is entirely
contained in at least oneUi. We can now modify as above the isometriesDi
inductively on the grid, starting from the bottom-left square, so that they all
glue up and show thatD(y ) does not depend onα orβ.
The resulting mapD :M→ Hn is a local isometry by construction. Since
M is complete, the mapD is a covering by Proposition 1.2.19. SinceHn is
simply connected, the coveringD is a homeomorphism andD is actually an
isometry. □
The isometryD :M→ Hn constructed in the proof is called adeveloping
map. The same proof shows that every complete simply connected ﬂat (or
elliptic)n-manifold is isometric toRn (orSn).
3.1.2. Complete hyperbolic manifolds.We have determined the unique
complete simply connected hyperbolicn-manifold, and we now look at com-
plete hyperbolic manifolds with arbitrary fundamental group. We ﬁrst note
that if Γ < Isom(Hn) is a group of isometries that acts freely and properly
discontinuously on Hn, the quotient manifoldHn/Γ has a natural Riemannian
structure that promotes the covering
π : Hn−→ Hn/Γ
to a local isometry, see Proposition 1.5.9. The quotientHn/Γ is a complete
hyperbolic manifold. We now show that every complete hyperbolic manifold is
realised in this way:
Proposition 3.1.3.Every complete hyperbolicn-manifoldM is isometric to
Hn/Γ for some subgroupΓ< Isom(Hn) acting freely and properly discontinu-
ously.
3.1. DISCRETE GROUPS OF ISOMETRIES 75
Proof. The universal cover ofM inherits a Riemannian structure that is
complete (by Proposition 1.2.19), hyperbolic, and simply connected: hence
it is isometric toHn by Theorem 3.1.2. The deck transformationsΓ of the
covering Hn → M are necessarily locally isometries, hence isometries. We
conclude thatM = Hn/Γ and Γ acts freely and properly discontinuously using
Proposition 1.5.1. □
Note that Γ is isomorphic to the fundamental groupπ1(M).
Remark 3.1.4. A group Γ < Isom(Hn) acts freely if and only if it does
not contain elliptic isometries: that is, every non-trivial isometry inΓ is either
hyperbolic or parabolic.
Note also thatΓ acts properly discontinuously if and only if it is discrete,
see Proposition 1.5.8.
Remark 3.1.5. The same proofs show that every complete ﬂat or spherical
n-manifoldisisometricto Rn/Γ orSn/Γ forsomediscretegroup Γofisometries
acting freely onRn orSn.
Corollary 3.1.6.There is a natural 1-1 correspondence
{ complete hyperbolic
manifoldsM up to isometry
}
←→



discrete subgroups Γ < Isom(Hn)
without elliptics
up to conjugation



Proof. When passing from the complete hyperbolic manifoldM to the
group Γ, the only choice we made is an isometry between the universal cover
ofM and Hn. Diﬀerent choices produce conjugate groupsΓ. □
3.1.3. Discrete groups. We investigate some basic properties of discrete
groups Γ of isometries ofHn.
Exercise 3.1.7. IfΓ< Isom(Hn) is discrete then it is countable.
Note that Γ is not necessarily ﬁnitely generated. We denote byΓp < Γ
the stabiliser of a pointp∈ Hn.
Proposition 3.1.8. Let Γ< Isom(Hn) be discrete andp∈ Hn be a point.
The stabiliser Γp is ﬁnite and the orbitΓ(p) ={g(p)|g∈ Γ} is discrete.
Proof. Both are obvious consequence of the fact that Γ acts properly
discontinuously. □
Of course Γ acts freely onHn if and only ifΓp is trivial for allp∈ Hn. A
set of subspaces inHn is locally ﬁniteif every compact subset inHn intersects
only ﬁnitely many of them.
Proposition 3.1.9.Let Γ< Isom(Hn) be discrete. The pointsp∈ Hn with
trivial stabiliser Γp form an open dense set inHn.
76 3. HYPERBOLIC MANIFOLDS
Proof. The ﬁxed-points setFix(g) of a non-trivial isometryg is a proper
subspace ofHn. The subspacesFix(g) withg∈ Γ are locally ﬁnite: if inﬁnitely
many of them intersect a compact set they accumulate andΓ does not act
properly discontinuously. The complement of a locally ﬁnite set of proper
subspaces is open and dense. □
Recall that a grouphas no torsionif every non-trivial element has inﬁnite
order.
Proposition 3.1.10. A discrete group Γ < Isom(Hn) acts freely on Hn if
and only if it has no torsion.
Proof. ByProposition2.4.6parabolicandhyperbolicelementshaveinﬁnite
order. On the other hand, an elliptic elementg∈ Γ has ﬁnite order sinceΓp
is ﬁnite forp∈ Fix(g). □
Corollary 3.1.11.The fundamental group of a complete hyperbolic mani-
fold has no torsion.
It is now time to exhibit some examples. Recall thatH2 is the half-plane
model, see Section 2.3.
Example 3.1.12. Themodular group
Γ = PSL2(Z)< PSL2(R) = Isom +(H2)
consists of all matrices in PSL2(R) having integer entries and is clearly a
discrete subgroup. It does not act freely onH2, however: the matrix
( 0 1
−1 0
)
represents the elliptic transformationz↦→− 1
z with ﬁxed pointi.
3.1.4. Coverings. We now make a simple but crucial observation: ifΓ<
Isom(Hn) acts freely and properly discontinuously, then also every subgroup
Γ′< Γ does; we get a manifolds covering
Hn/Γ′−→ Hn/Γ
whose degreed is precisely the index ofΓ′ in Γ. Recall from Proposition 1.2.20
that we get
Vol
(
Hn/Γ′
)
=d· Vol
(
Hn/Γ
)
where some of the terms in the formula may be inﬁnite. Moreover, every
covering of a hyperbolic completeM = Hn/Γ is constructed in this way: there
is a nice bijective correspondence
{
coverings of M
}
←→
{
subgroups of Γ
}
.
This holds of course also for ﬂat and spherical manifolds.
3.1. DISCRETE GROUPS OF ISOMETRIES 77
3.1.5. Congruence subgroups. We can now exhibit a family of two-
dimensional hyperbolic manifolds.
Pick an integerm> 2. Let SL2(Z/mZ) be the group of2× 2 matrices
with coeﬃcients inZ/mZ and determinant 1. We deﬁne the quotient
PSL2(Z/mZ) = SL 2(Z/mZ)/{±I}.
The reduction modulom homomorphism Z→ Z/mZ induces the group homo-
morphisms SL2(Z)→ SL2(Z/mZ) and
PSL2(Z)−→ PSL2(Z/mZ).
The kernel of this homomorphism is theprincipal congruence subgroupΓ(m)
of PSL2(Z). It is clearly discrete, since PSL2(Z) is. It has ﬁnite index in
PSL2(Z) because PSL2(Z/mZ) is ﬁnite.
Proposition 3.1.13. Ifm> 4 the group Γ(m) acts freely onH2.
Proof. An elementA∈ Γ(m) is a matrix
(a b
c d
)
congruent to
(1 0
0 1
)
modulo
m. In particulara +d is congruent to 2 modulom, and hence is not−1, 0, 1.
ThereforeA is never elliptic. □
The quotient H2/Γ(m) is a hyperbolic surface. We will construct many
hyperbolic surfaces in Section 6.2 via some more geometric methods.
3.1.6. Selberg’s lemma.The discrete groupΓ = PSL2(Z) does not act
freely onH2, but its ﬁnite-index normal subgroupΓ(m)does as soon asm> 4.
Is this the instance of a more general principle? Yes, it is.
Proposition 3.1.14.Every ﬁnitely generated discrete groupΓ< Isom(Hn)
contains a ﬁnite-index normal subgroupΓ′◁ Γ that acts freely onHn.
Proof. The groupIsom(Hn) is isomorphic toO+(n, 1)< GL(n + 1, C), so
Selberg’s Lemma 1.4.19 applies toΓ, and it furnishes a ﬁnite-index torsion-free
normal subgroup Γ′◁ Γ. This subgroup acts freely by Proposition 3.1.10.□
Every ﬁnitely generated discrete groupΓ< Isom(Hn) contains at least one
ﬁnite-index subgroup that acts freely. But how many such subgroups does it
contain? Quite a lot, in fact.
Proposition 3.1.15.Every ﬁnitely generated discrete groupΓ< Isom(Hn)
is residually ﬁnite.
Proof. See Lemma 1.4.20. □
The following corollary shows that there is an abundance of torsion-free
subgroups. Although algebraic in nature, it has some remarkable geometric
consequences, that will be revealed soon in Section 4.3.5.
Corollary 3.1.16.Let Γ< Isom(Hn)be discrete and ﬁnitely generated. For
every non-trivialg∈ Γ there is a ﬁnite-index normal subgroupΓ′◁ Γ that acts
freely on Hn and does not containg.
78 3. HYPERBOLIC MANIFOLDS
