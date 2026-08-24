---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-019-0-eπq
section_title: "(E,π,Q ) :"
section_number: 0
pages: 39-42
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
⨂
e∈I +
HF (Le,0,Le,1)−→
⨂
e∈I −
HF (Le,0,Le,1).
This is a modiﬁed version of the frameworks described in [24] , [19] and [25]. The
fact that Φ rel
0 goes from positive to negative ends has to do with the use of Fl oer
cohomology, which we think of as behaving contravariantly. Th is is of course
largely a matter of convention. In any case, there is no real d iﬀerence between
positive and negative ends, as one can be turned into the othe r by switching
fromγe(s,t ) to γe(−s, 1−t). Doing that does not change the relative invariant,
up to the “Poincar´ e duality” isomorphism HF (Le,0,Le,1)∼= HF (Le,1,Le,0)∨.
One could therefore formulate the theory using only one kind of ends, bring-
ing it closer to a (1+1)-dimensional TQFT. Finally, we shoul d mention that
the transverse intersection condition can be lifted. This g oes by a standard
argument, using the same “continuation map” technique as th e proof of isotopy
invariance of Floer cohomology. We will not discuss that fur ther, since it is not
necessary for our immediate purpose.
To begin with, a brief review of Floer cohomology, just to rem ind the reader of
the special features of the “exact” situation. Let M be an exact symplectic man-
ifold and (L0,L 1) a pair of transversally intersecting exact Lagrangian sub mani-
folds. The action functional on the path space P(L0,L 1) ={c∈C∞([0; 1],M ) :
c(0)∈L0, c(1)∈L1} is
aL0,L1(c) =−
∫
c∗θ +KL1(c(1))−KL0(c(0))
(as pointed out to me by Oh, this form of the action functional appears in [17],
and is then used crucially in his papers with Milinkovic). It s critical points are
the constant paths cx at points x∈L0∩L1. We write aL0,L1(x) = aL0,L1(cx) =
KL1(x)−KL0(x) for their action. The Floer cochain space CF (L0,L 1) is the
vector space over Z/2 with a basis given by these points; we denote the canonical
basis vectors by ⟨x⟩. Let J(M ) be the space of smooth families J = (Jt)0≤t≤1
of almost complex structures on M , each of which is ω-compatible and convex
near the boundary. For J∈ J(M ) and x±∈ L0∩L1, one considers the space
FJ (x−,x +) of maps



σ =σ(s,t ) : R× [0; 1]−→M,
σ(R×{ 0})⊂L0, σ(R×{ 1})⊂L1,
∂σ/∂t =Jt∂σ/∂s,
lims→±∞σ(s,·) = cx±
(2.22)
where the limit is understood to be in the C1-topology on P(L0,L 1). There
is a natural R-action on FJ (x−,x +) by translation in s-direction. We denote
39
by F∗
J (x−,x +) the subspace of maps which are not R-invariant. Solutions σ
of (2.22) can be interpreted as negative gradient ﬂow lines f or aL0,L1 in an
L2-metric on P(L0,L 1); of course, this implies that F∗
J (x−,x +) = ∅ whenever
aL0,L1(x−)≤aL0,L1(x+).
To each σ∈ FJ (x−,x +) one can associate an operator Dσ,J which linearizes
(2.22), and which is Fredholm in suitable Sobolev spaces. Th ere is a dense
subspace Jreg (M,L 0,L 1) ⊂ J(M ) of almost complex structures J for which
all Dσ,J are onto, and then the spaces FJ (x−,x +), as well as the quotients
F∗
J (x−,x +)/R, are smooth manifolds. In that case one deﬁnes nJ (x−,x +)∈ Z/2
to be the number mod 2 of isolated points in F∗
J (x−,x +)/R. The map
dJ⟨x+⟩= ∑
x−nJ (x−,x +)⟨x−⟩
has square zero, making CF (L0,L 1) into a diﬀerential vector space. HF (L0,L 1)
is deﬁned to be its cohomology ker dJ/imdJ . Unlike dJ itself, Floer cohomology
can be shown to be independent of J up to canonical isomorphism. It is also
invariant under deformations of L0 or L1 as exact Lagrangian submanifolds.
We now start constructing the relative invariant associate d to (E,π ) and Q.
Choose a point xe∈Le,0∩Le,1 for each end e, and write B({xe}) for the space
of smooth sections u : S→ E such that u(∂S )⊂ Q, and which over the ends
have the form Γ −1
e ◦u◦γe(s,t ) = (s,t,σ e(s,t )) with maps σe : R±× [0; 1]→M
satisfying lims→±∞σe(s,·) = cxe, in the same sense as in (2.22). The action
integralA(u) =
∫
Su∗ω is convergent for all u∈ B({xe}), and one gets a formula
analogous to (2.7):
A(u) =
∑
e∈I −
aLe, 0,Le, 1(xe)−
∑
e∈I +
aLe, 0,Le, 1(xe) +
∫
∂S
κQ. (2.23)
Take a complex structure j onS (equal to j0 nearScrit as always) which, on the
ends, is induced from the standard complex structure j± on R±× [0; 1]. Choose
also a Je = (Je,t)0≤t≤1∈ J(M ) for each e. Then J(E,π,j, {Je}) denotes the
contractible space of almost complex structures J on E which are compatible
relative to j, and such that Γ ∗
eJ, for each e, is the almost complex structure on
R±×[0; 1]×M given byj±×Je,t at a point (s,t,y ). For any such J, we denote by
MJ ({xe})⊂ B({xe}) the subspace of sections u which are (j,J )-holomorphic.
The formal picture from Section 2.1 still applies: one has th e vector bundle
EJ→ B({xe}), its canonical section ¯∂J whose zero-set is MJ ({xe}), as well as
their “universal” versions Euniv, ¯∂univ. Turning this picture into an analytically
realistic one is more complicated than in the compact case. S till, the procedure
is by now standard, and so we will not say more about it, except to mention
that the derivative Du,J of ¯∂J again extends to a Fredholm operator from a
suitably deﬁned W 1,p-version W1
u ofT B({xe})u to an Lp-version W0
u,J of Eu,J .
This allows one to deﬁne the notion of regularity of u ∈ MJ ({xe}), and of
J∈ J(E,π,j, {Je}), in the same way as before. The subspace of regular J is
denoted by Jreg(E,π,Q,j, {Je}).
40
Remark 2.18. It is maybe helpful to mention that Floer’s equation (2.22) itself
can be made to ﬁt into this framework. Namely, take the surfac e S = R× [0; 1]
and the trivial exact symplectic ﬁbration π : E = S×M → S, with the La-
grangian boundary condition Q = ( R×{ 0}× L0)∪ (R×{ 1}× L1); it is a
tautology that this is modelled over the two ends of S on (L0,L 1). Take the
standard complex structure j on S, the same Je∈ J(M ) for both ends e, and
deﬁne J ∈ J(E,π,j, {Je}) to be the product j×Je,t at a point (s,t,y ). Sec-
tions u : S→ E with u(∂S )⊂ Q are of the form u(s,t ) = (s,t,σ (s,t )), where
σ : R× [0; 1]→M is a map satisfying the boundary condition in (2.22). More-
over, u is (j,J )-holomorphic iﬀ ∂σ/∂t = Je,t∂σ/∂s , so that one can identify
MJ (x−,x +) = FJe(x−,x +) for all x±.
In parallel with the exposition in Section 2.1, we will now di scuss the ba-
sic properties of the spaces MJ ({xe}). The next two results are analogues of
Lemmas 2.2 and 2.4, and their proofs are the same.
Lemma 2.19. For every J∈ J(E,π,j, {Je}) there is a closed subset K⊂E\
∂hE such that π|K : K→ S is proper, and which over the ends has the form
Γ −1
e (K) = R±×[0; 1]×Ke for some compact Ke⊂M\∂M , such that u(S)⊂K
for all u∈ MJ ({xe}) and all points {xe}.
Lemma 2.20. Jreg (E,π,Q,j, {Je}) isC∞-dense in J(E,π,j, {Je}). More pre-
cisely, given some nonempty open subset U⊂S which is disjoint from the ends,
and a J∈ J(E,π,j, {Je}), there are J ′∈ Jreg (E,π,Q,j, {Je}) arbitrarily close
to J, such that J =J ′ outside π−1(U ).
The remaining issue is compactness. After taking a symplect ic form Ω + π∗β
onE as in Lemma 2.1, and the associated metric, one ﬁnds that 1
2
∫
W||Du||2≤
A(u) +
∫
W β for any compact subset W ⊂ S and u∈ MJ ({xe}). Repeating
the argument in Lemma 2.3, one derives from this that any sequ ence (ui) in
MJ ({xe}) has a subsequence which is Cr-convergent on compact subsets. It is
necessary to go beyond this somewhat coarse result, and to st udy sequences (ui)
in the more appropriate Gromov-Floer topology. A compactiﬁcation MJ ({xe})
of MJ ({xe}) in this topology can be constructed by adding “broken secti ons”.
Since a very similar notion is part of the standard analytica l package underlying
Floer theory, we will not deﬁne the topology, and only descri be the compactiﬁ-
cation as a set. Each point of it consists of
(i) the “principal component” u∈ MJ ({ˆxe}) for some {ˆxe};
(ii) for each end e∈I ±, a ﬁnite sequence of points ˆ xe,0,..., ˆxe,le∈Le,0∩Le,1,
le≥ 0. If the end is negative (positive), this should satisfy ˆ xe,0 =xe and
ˆxe,le = ˆxe (ˆxe,0 = ˆxe and ˆxe,le =xe);
(iii) Floer ﬂow lines σe,m∈ F∗
Je(ˆxe,m−1, ˆxe,m)/R, for each e and 1≤m≤le.
41
Suppose that a sequence ( ui) converges to such a limit. One sees from (2.23)
that for all i,
A(ui) = A(u) +
∑
e
∑
1≤m≤le
(aLe, 0,Le, 1(ˆxe,m−1)−aLe, 0,Le, 1(ˆxe,m)) (2.24)
Note that all terms of the ∑ are > 0; therefore A(u)≤A(ui), with equality iﬀ
le = 0 for all ends e. We will need another piece of information about the limit,
which can be derived from the deﬁnition of the Gromov-Floer t opology and a
“gluing theorem” for linear elliptic operators. Namely, fo r i≫ 0,
indDui,J = indDu,J +
∑
e
∑
1≤m≤le
indDσe,m ,Je. (2.25)
From now on assume that Je∈ Jreg (M,Le,0,Le,1) for all e, and that J ∈
Jreg(E,π,Q,j, {Je}). Then ind Du,J ≥ 0 and ind Dσe,m ,Je > 0 on the right
hand side of (2.25), so that the left hand side can be zero only if indDu,J = 0
and le = 0 for all e. It follows that the zero-dimensional part of MJ ({xe}), for
any{xe}, is compact, hence a ﬁnite set. Write νJ ({xe})∈ Z/2 for the number
of points modulo two in this set, and consider the map
CΦ rel
