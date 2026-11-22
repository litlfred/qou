---
doc_id: arxiv-math-0105186v2
doc_title: "A long exact sequence for symplectic Floer cohomology"
section_id: sec-009-24-relative-invariants
section_title: "Relative invariants"
section_number: 2.4
pages: 38-45
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
toc_source: inferred
doc_brief: "A long exact sequence for symplectic Floer cohomology — 17 sections: Front matter; Introduction; Dehn twists, and all that"
---
Relative invariants
A surface with strip-like ends is an oriented connected surface S, together with
ﬁnite sets I−, I+ and oriented proper embeddings {γe : R−× [0; 1] →S}e∈I−,
{γe : R+ × [0; 1] →S}e∈I+, such that γ−1
e (∂S) = R± × {0; 1}. The images of
the γe (the ends of S) should be mutually disjoint, and the complement of the
union of all ends should be a relatively compact subset of S. We will always
assume that there is at least one end.
Deﬁne an exact Lefschetz ﬁbration trivial over the ends of S to be an exact
Lefschetz ﬁbration (E, π), whose regular ﬁbres are isomorphic to some exact
symplectic manifold M, together with smooth trivializations {Γe : R−× [0; 1] ×
M →γ∗
eE}e∈I−, {Γe : R+ × [0; 1] × M →γ∗
eE}e∈I+, such that Γ∗
eΩ, Γ∗
eΘ are
equal to the pullbacks of ω,θ by the projection R± × [0; 1] × M →M. When
considering a Lagrangian boundary condition Q for such an exact Lefschetz
ﬁbration, we will always impose the additional condition that κQ vanishes on
im(γe) ∩∂S. To see the signiﬁcance of this, recall that the family Qz ⊂Ez of
Lagrangian submanifolds is preserved by symplectic parallel transport along ∂S.
Since the symplectic connection is trivial on the ends, it follows that Γ−1
e (Q) =
(R± × {0} × Le,0) ∪(R± × {1} × Le,1) for some pair of Lagrangian submanifolds
Le,0, Le,1 ⊂M; we say that Q is modelled on (Le,0, Le,1) over the end e. Using
the deﬁnition of a Lagrangian boundary condition, one ﬁnds that
d(KQ ◦Γe) | R± × {k} × Le,k = (θ|Le,k) −(γ∗
eκQ|R± × {k}).
Our assumption is that the second term on the right vanishes, which implies
that KQ(Γe(s, k, y)) is independent of s. It follows that Le,k is an exact La-
grangian submanifold in a canonical way, with associated function KLe,k(y) =
KQ(Γe(s, k, y)).
38
In this situation, and under the additional assumption that the intersections
Le,0 ∩Le,1 are transverse for all e, we will associate to (E, π) and Q a relative
invariant, which is a map between Floer cohomology groups
Φrel
0 (E, π, Q) :
O
e∈I+
HF(Le,0, Le,1) −→
O
e∈I−
HF(Le,0, Le,1).
This is a modiﬁed version of the frameworks described in [24], [19] and [25]. The
fact that Φrel
0
goes from positive to negative ends has to do with the use of Floer
cohomology, which we think of as behaving contravariantly. This is of course
largely a matter of convention. In any case, there is no real diﬀerence between
positive and negative ends, as one can be turned into the other by switching
from γe(s, t) to γe(−s, 1 −t). Doing that does not change the relative invariant,
up to the “Poincar´e duality” isomorphism HF(Le,0, Le,1) ∼= HF(Le,1, Le,0)∨.
One could therefore formulate the theory using only one kind of ends, bring-
ing it closer to a (1+1)-dimensional TQFT. Finally, we should mention that
the transverse intersection condition can be lifted.
This goes by a standard
argument, using the same “continuation map” technique as the proof of isotopy
invariance of Floer cohomology. We will not discuss that further, since it is not
necessary for our immediate purpose.
To begin with, a brief review of Floer cohomology, just to remind the reader of
the special features of the “exact” situation. Let M be an exact symplectic man-
ifold and (L0, L1) a pair of transversally intersecting exact Lagrangian submani-
folds. The action functional on the path space P(L0, L1) = {c ∈C∞([0; 1], M) :
c(0) ∈L0, c(1) ∈L1} is
aL0,L1(c) = −
Z
c∗θ + KL1(c(1)) −KL0(c(0))
(as pointed out to me by Oh, this form of the action functional appears in [17],
and is then used crucially in his papers with Milinkovic). Its critical points are
the constant paths cx at points x ∈L0 ∩L1. We write aL0,L1(x) = aL0,L1(cx) =
KL1(x) −KL0(x) for their action. The Floer cochain space CF(L0, L1) is the
vector space over Z/2 with a basis given by these points; we denote the canonical
basis vectors by ⟨x⟩. Let J(M) be the space of smooth families J = (Jt)0≤t≤1
of almost complex structures on M, each of which is ω-compatible and convex
near the boundary. For J ∈J(M) and x± ∈L0 ∩L1, one considers the space
FJ(x−, x+) of maps









σ = σ(s, t) : R × [0; 1] −→M,
σ(R × {0}) ⊂L0, σ(R × {1}) ⊂L1,
∂σ/∂t = Jt ∂σ/∂s,
lims→±∞σ(s, ·) = cx±
(2.22)
where the limit is understood to be in the C1-topology on P(L0, L1). There
is a natural R-action on FJ(x−, x+) by translation in s-direction. We denote
39
by F∗
J(x−, x+) the subspace of maps which are not R-invariant. Solutions σ
of (2.22) can be interpreted as negative gradient ﬂow lines for aL0,L1 in an
L2-metric on P(L0, L1); of course, this implies that F∗
J(x−, x+) = ∅whenever
aL0,L1(x−) ≤aL0,L1(x+).
To each σ ∈FJ(x−, x+) one can associate an operator Dσ,J which linearizes
(2.22), and which is Fredholm in suitable Sobolev spaces.
There is a dense
subspace Jreg(M, L0, L1) ⊂J(M) of almost complex structures J for which
all Dσ,J are onto, and then the spaces FJ(x−, x+), as well as the quotients
F∗
J(x−, x+)/R, are smooth manifolds. In that case one deﬁnes nJ(x−, x+) ∈Z/2
to be the number mod 2 of isolated points in F∗
J(x−, x+)/R. The map
dJ⟨x+⟩= P
x−nJ(x−, x+)⟨x−⟩
has square zero, making CF(L0, L1) into a diﬀerential vector space. HF(L0, L1)
is deﬁned to be its cohomology ker dJ/im dJ. Unlike dJ itself, Floer cohomology
can be shown to be independent of J up to canonical isomorphism. It is also
invariant under deformations of L0 or L1 as exact Lagrangian submanifolds.
We now start constructing the relative invariant associated to (E, π) and Q.
Choose a point xe ∈Le,0 ∩Le,1 for each end e, and write B({xe}) for the space
of smooth sections u : S →E such that u(∂S) ⊂Q, and which over the ends
have the form Γ−1
e
◦u ◦γe(s, t) = (s, t, σe(s, t)) with maps σe : R± × [0; 1] →M
satisfying lims→±∞σe(s, ·) = cxe, in the same sense as in (2.22). The action
integral A(u) =
R
S u∗ω is convergent for all u ∈B({xe}), and one gets a formula
analogous to (2.7):
A(u) =
X
e∈I−
aLe,0,Le,1(xe) −
X
e∈I+
aLe,0,Le,1(xe) +
Z
∂S
κQ.
(2.23)
Take a complex structure j on S (equal to j0 near Scrit as always) which, on the
ends, is induced from the standard complex structure j± on R± ×[0; 1]. Choose
also a Je = (Je,t)0≤t≤1 ∈J(M) for each e. Then J(E, π, j, {Je}) denotes the
contractible space of almost complex structures J on E which are compatible
relative to j, and such that Γ∗
eJ, for each e, is the almost complex structure on
R±×[0; 1]×M given by j±×Je,t at a point (s, t, y). For any such J, we denote by
MJ({xe}) ⊂B({xe}) the subspace of sections u which are (j, J)-holomorphic.
The formal picture from Section 2.1 still applies: one has the vector bundle
EJ →B({xe}), its canonical section ¯∂J whose zero-set is MJ({xe}), as well as
their “universal” versions Euniv, ¯∂univ. Turning this picture into an analytically
realistic one is more complicated than in the compact case. Still, the procedure
is by now standard, and so we will not say more about it, except to mention
that the derivative Du,J of ¯∂J again extends to a Fredholm operator from a
suitably deﬁned W 1,p-version W1
u of T B({xe})u to an Lp-version W0
u,J of Eu,J.
This allows one to deﬁne the notion of regularity of u ∈MJ({xe}), and of
J ∈J(E, π, j, {Je}), in the same way as before. The subspace of regular J is
denoted by Jreg(E, π, Q, j, {Je}).
40
Remark 2.18. It is maybe helpful to mention that Floer’s equation (2.22) itself
can be made to ﬁt into this framework. Namely, take the surface S = R × [0; 1]
and the trivial exact symplectic ﬁbration π : E = S × M →S, with the La-
grangian boundary condition Q = (R × {0} × L0) ∪(R × {1} × L1); it is a
tautology that this is modelled over the two ends of S on (L0, L1). Take the
standard complex structure j on S, the same Je ∈J(M) for both ends e, and
deﬁne J ∈J(E, π, j, {Je}) to be the product j × Je,t at a point (s, t, y). Sec-
tions u : S →E with u(∂S) ⊂Q are of the form u(s, t) = (s, t, σ(s, t)), where
σ : R × [0; 1] →M is a map satisfying the boundary condition in (2.22). More-
over, u is (j, J)-holomorphic iﬀ∂σ/∂t = Je,t∂σ/∂s, so that one can identify
MJ(x−, x+) = FJe(x−, x+) for all x±.
In parallel with the exposition in Section 2.1, we will now discuss the ba-
sic properties of the spaces MJ({xe}). The next two results are analogues of
Lemmas 2.2 and 2.4, and their proofs are the same.
Lemma 2.19. For every J ∈J(E, π, j, {Je}) there is a closed subset K ⊂E \
∂hE such that π|K : K →S is proper, and which over the ends has the form
Γ−1
e (K) = R±×[0; 1]×Ke for some compact Ke ⊂M \∂M, such that u(S) ⊂K
for all u ∈MJ({xe}) and all points {xe}.
Lemma 2.20. Jreg(E, π, Q, j, {Je}) is C∞-dense in J(E, π, j, {Je}). More pre-
cisely, given some nonempty open subset U ⊂S which is disjoint from the ends,
and a J ∈J(E, π, j, {Je}), there are J′ ∈Jreg(E, π, Q, j, {Je}) arbitrarily close
to J, such that J = J′ outside π−1(U).
The remaining issue is compactness. After taking a symplectic form Ω+π∗β
on E as in Lemma 2.1, and the associated metric, one ﬁnds that 1
2
R
W ||Du||2 ≤
A(u) +
R
W β for any compact subset W ⊂S and u ∈MJ({xe}). Repeating
the argument in Lemma 2.3, one derives from this that any sequence (ui) in
MJ({xe}) has a subsequence which is Cr-convergent on compact subsets. It is
necessary to go beyond this somewhat coarse result, and to study sequences (ui)
in the more appropriate Gromov-Floer topology. A compactiﬁcation MJ({xe})
of MJ({xe}) in this topology can be constructed by adding “broken sections”.
Since a very similar notion is part of the standard analytical package underlying
Floer theory, we will not deﬁne the topology, and only describe the compactiﬁ-
cation as a set. Each point of it consists of
(i) the “principal component” u ∈MJ({ˆxe}) for some {ˆxe};
(ii) for each end e ∈I±, a ﬁnite sequence of points ˆxe,0, . . . , ˆxe,le ∈Le,0 ∩Le,1,
le ≥0. If the end is negative (positive), this should satisfy ˆxe,0 = xe and
ˆxe,le = ˆxe (ˆxe,0 = ˆxe and ˆxe,le = xe);
(iii) Floer ﬂow lines σe,m ∈F∗
Je(ˆxe,m−1, ˆxe,m)/R, for each e and 1 ≤m ≤le.
41
Suppose that a sequence (ui) converges to such a limit. One sees from (2.23)
that for all i,
A(ui) = A(u) +
X
e
X
1≤m≤le
(aLe,0,Le,1(ˆxe,m−1) −aLe,0,Le,1(ˆxe,m))
(2.24)
Note that all terms of the P are > 0; therefore A(u) ≤A(ui), with equality iﬀ
le = 0 for all ends e. We will need another piece of information about the limit,
which can be derived from the deﬁnition of the Gromov-Floer topology and a
“gluing theorem” for linear elliptic operators. Namely, for i ≫0,
ind Dui,J = ind Du,J +
X
e
X
1≤m≤le
ind Dσe,m,Je.
(2.25)
From now on assume that Je ∈Jreg(M, Le,0, Le,1) for all e, and that J ∈
Jreg(E, π, Q, j, {Je}).
Then ind Du,J ≥0 and ind Dσe,m,Je > 0 on the right
hand side of (2.25), so that the left hand side can be zero only if ind Du,J = 0
and le = 0 for all e. It follows that the zero-dimensional part of MJ({xe}), for
any {xe}, is compact, hence a ﬁnite set. Write νJ({xe}) ∈Z/2 for the number
of points modulo two in this set, and consider the map
CΦrel
0 (E, π, Q, J) :
O
e∈I+
CF(Le,0, Le,1) −→
O
e∈I−
CF(Le,0, Le,1)
(2.26)
given by the matrix with entries νJ({xe}), that is to say
CΦrel
0 (E, π, Q, J)( ⊗
e∈I+⟨xe⟩) =
X
{xe}e∈I−
νJ({xe}e∈I−∪I+)( ⊗
e∈I−⟨xe⟩).
A standard argument, involving the structure at inﬁnity of the one-dimensional
part of MJ({xe}), shows is that there is an even number of points in MJ({xe})
of the following form: le is 1 for a single end e = f, and zero for all other e, so
that the point is a pair (u, σf,1); and moreover ind Du,J = 0, ind Dσf,1,Jf = 1.
Algebraically, what this says is that CΦrel
0 (E, π, Q, J) is a chain map.
The
relative invariant Φrel
0 (E, π, Q) is deﬁned to be the induced map on cohomology.
The next step is to show that this is independent of the choice of j and J,
keeping the Je ﬁxed for the moment. Any two j0, j1 can be connected by a
family jµ, 0 ≤µ ≤1, which remains constant on the ends; correspondingly, for
J0 ∈Jreg(E, π, Q, j0, {Je}), J1 ∈Jreg(E, π, Q, j1, {Je}) one can ﬁnd a family
Jµ joining them, which is regular in the parametrized sense (this is not the same
as saying that each Jµ should itself be regular, which would be impossible to
achieve in general). The parametrized moduli spaces
Mpara
(Jµ)({xe}) =
[
0≤µ≤1
{µ} × MJµ({xe})
42
are then smooth manifolds, and they have a parametrized version of the Gromov-
Floer compactiﬁcation. In particular, the zero-dimensional parts are again ﬁnite
sets, so that one can use the number of points λ({xe}) ∈Z/2 in them to deﬁne
a map h(E, π, Q, (Jµ)) between the same groups as in (2.26). Arguing along
the same lines as when proving that CΦrel
0
is a chain map, one can show that
h is a homotopy between CΦrel
0 (E, π, Q, J0) and CΦrel
0 (E, π, Q, J1). The same
argument can be used to show that Φrel
0 (E, π, Q) remains invariant under de-
formations of the geometric data, that is to say of Q or (E, π) itself, as long as
the structure of the ends remains unchanged. Finally, we should prove that the
relative invariant is independent of the Je, which more accurately means that it
commutes with the canonical isomorphisms between Floer cohomology groups
for diﬀerent Je. We omit this entirely, both because it is not important for our
purpose, and because it would require a digression concerning “continuation
maps”.
Two ways of gluing together surfaces with strip-like ends will play a role
later on. One of them is a close cousin of that considered as in Section 2.1. It
can be formulated in various degrees of generality, but we will need only one
special case. Suppose then that S1 is a surface with strip-like ends, and S2 a
compact surface, together with points ζk ∈∂Sk (ζ1 should not lie on any end;
that can of course always be achieved by making the ends smaller). Let (Ek, πk)
be exact Lefschetz ﬁbrations over Sk with Lagrangian boundary conditions Qk;
(E1, π1) should be trivial over the ends. We also want to have M, L, maps
φk : M →(Ek)ζk, and trivializations (ψk, Ψk), with the same properties as in
Section 2.1. The boundary connected sum S = S1#ζ1∼ζ2S2 is a surface with the
same kind of strip-like ends as S1. As before one constructs an exact Lefschetz
ﬁbration (E, π) on it with a Lagrangian boundary condition Q, modelled over
the ends on the same Lagrangian submanifolds as Q1.
Choose complex structures jk on Sk such that (ψk)∗jk is standard; j1 should
also be standard on the ends. Take {Je} and J1 ∈Jreg(E1, π1, Q1, j1, {Je}) as
when deﬁning the relative invariant of (E1, π1, Q1); as an additional condition,
we want (Ψ1)∗J1 to be the product of the standard complex structure on ¯D+(1)
and some ﬁxed almost complex structure on M. By Lemma 2.20 this can be
done while still achieving regularity. Using Lemmas 2.4 and 2.5 one ﬁnds a
J2 ∈Jreg(E2, π2, Q2, j2) with the same restriction on (Ψ2)∗J2, and such that
the evaluations
evζ1 | MJ1({xe}) : MJ1({xe}) −→Q1
ζ1 ∼= L,
evζ2 | MJ2 : MJ2 −→Q2
ζ2 ∼= L
(2.27)
are transverse to each other for every {xe}. Let J ∈J(E, π, j, {Je}) be the
almost complex structure constructed from J1, J2. As in Proposition 2.7, this
will be regular for small values of the parameter ρ, and
MJ({xe})[0] ∼= (MJ1({xe}) ×L MJ2)[0],
(2.28)
where the [0] denotes on both sides the zero-dimensional component of these
43
manifolds. We will not need the full “gluing formula” which one can obtain
from this, but only a special case:
Lemma 2.21. If Φ1(E2, π2, Q2) = 0 then Φrel
0 (E, π, Q) = 0.
Proof. For simplicity, suppose that Φ1(E2, π2, Q2) vanishes even when taken
in the cobordism ring MO∗(L). This means that there is a compact manifold
with boundary G and a smooth map g : G →L, such that ∂G = MJ2 and
g|∂G = evζ2. After perturbing it slightly, one can assume that g is transverse
to all maps evζ1 in (2.27). Then the ﬁbre products
G({xe}) = MJ1({xe}) ×L G
(2.29)
are smooth manifolds. The evaluation map extends continuously to the Gromov-
Floer compactiﬁcation, so that one can deﬁne compactiﬁcations G({xe}) in the
obvious way. It is not diﬃcult to see, using (2.25), that the zero-dimensional
part G({xe})[0] is a ﬁnite set; one counts the points ξJ,G,g({xe}) ∈Z/2 in
it, and uses that to deﬁne a map k between the Floer cochain groups asso-
ciated to (E1, π1, Q1), as in (2.26). We claim that this is a homotopy between
CΦ0
rel(E, π, Q, J) and the zero map. As usual, the proof is based on analyzing
the ends of the one-dimensional moduli spaces. The closure in G({xe}) of the
one-dimensional part G({xe})[1] is a compact one-manifold with boundary, and
its boundary points are of two kinds: ﬁrst, boundary points of G({xe})[1] itself,
∂G({xe})[1] = (MJ1({xe}) ×L ∂G)[0] ∼= MJ({xe})[0]; their number modulo two
is νJ({xe}) by deﬁnition. The second kind of boundary points are of the form
(u, σf,1) × q ∈MJ({xe}) ×L G. This means that for some end f, and points
{ˆxe} with ˆxe = xe for all e̸ = f, one has
u × q ∈G({ˆxe})[0],
σf,1 ∈
(
(F∗(xf, ˆxf)/R)[0]
if e is a negative end,
(F∗(ˆxf, xf)/R)[0]
if e is a positive end.
The number of such boundary points is
X
f∈I−
X
ˆxf
nJf (xf, ˆxf) ξJ,G,g({ˆxe}) +
X
f∈I+
X
ˆxf
ξJ,G,g({ˆxe}) nJf (ˆxf, xf) ∈Z/2.
The fact that this is equal to νJ({xe}) gives precisely the desired equality dk +
kd = CΦrel
0 (E, π, Q, J).
The other and maybe more obvious gluing process is to join together two ends.
Assume that S1, S2 are surfaces with strip-like ends, such that S1 has a single
positive end e1, and S2 a single negative end e2 (this is not really a restriction
since, as has been mentioned before, positive ends can be turned into negative
ones and vice versa). Choose some σ > 0, and deﬁne S = S1#e1∼e2S2 by taking
S1 \ γe1((σ; ∞) × [0; 1]) and S2 \ γe2((−∞; −σ) × [0; 1]), and identifying γe1(s, t)
with γe2(s −σ, t) for (s, t) ∈[0; σ] × [0; 1]. The ends of S are the negative ends
of S1 together with the positive ends of S2. After choosing complex structures
44
jk on Sk which are standard over the ends, there is an obvious induced complex
structure j on S.
Let (L0, L1) be a pair of exact Lagrangian submanifolds in M. Suppose that
we have exact Lefschetz ﬁbrations (Ek, πk) over Sk, trivial over the ends, and
Lagrangian boundary conditions Q1, Q2 for them modelled on (L0, L1) over e1
and over e2, respectively. Then one can form an exact Lefschetz ﬁbration (E, π)
over S by identifying Γe1(s, t, y) ∈E1 with Γe2(s−σ, t, y) ∈E2, in parallel with
the construction on the base. This comes with an obvious Lagrangian boundary
condition Q. Choose almost complex structures Jk on Ek so as to deﬁne relative
invariants CΦrel
0 (Ek, πk, Qk, Jk). We require that the Jek ∈Jreg(M, L0, L1) on
which Jk is modelled over the end ek should be the same for k = 1, 2. Then J1
and J2 match up to an almost complex structure J on E, which is compatible
relative to j.
Proposition 2.22. For ﬁxed J1, J2, if one chooses σ to be suﬃciently large,
then J is regular. Moreover, denoting again by [0] the zero-dimensional compo-
nents, and by I−, I+ the negative and positive ends of S, one has
MJ({xe})[0] ∼=
[
x∈L0∩L1
MJ1({xe}e∈I−, x)[0] × MJ2(x, {xe}e∈I+)[0]
for any {xe}e∈I−∪I+.
The method used in the proof of this is the same as when setting up Floer
cohomology. A thorough exposition of a closely related result can be found in
[24, Section 4.4]. The implication for the relative invariants is clear:
CΦrel
0 (E, π, Q, J) = CΦrel
0 (E1, π1, Q1, J1) ◦CΦrel
0 (E2, π2, Q2, J2),
(2.30)
which proves the main TQFT-style property of relative invariants, namely, that
they are functorial if one regards the gluing S = S1#e1∼e2S2 as composition of
the surfaces S1, S2.
