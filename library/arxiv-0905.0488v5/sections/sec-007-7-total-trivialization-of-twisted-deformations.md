---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-007-7-total-trivialization-of-twisted-deformations
section_title: "Total Trivialization of Twisted Deformations"
section_number: 7
pages: 33-36
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
In this section we assume Setup 2.6. Acyclic open sets were introduced in Deﬁ-
nition 2.4.
LetA be anR-deformation ofOU (associative of Poisson) , for some open set
U⊂X. By [Ye9, Corollary 3.8], for everyp≥1 the sheaf ofR-modules mpA is m-
adically complete. As explained in Section 2, there is a sheaf of pronilpotent groups
Exp(mpA) on U, with an isomorphism of sheaves of setsexp : mpA
≃
− →Exp(mpA).
If V ⊂U is anOX-acyclic open set, then by [Ye9, Proposition 4.5] the algebra
A := Γ(V,A) is anR-deformation ofC := Γ(V,OX).
Lemma 7.1. Let U⊂X be an open set, and letA be anR-deformation ofOU.
WriteG := IG(A) = Exp(mA), andNp := Exp(mpA) for p≥1.
(1) Np is a sheaf of normal subgroups ofG, andNp/Np+1 is central inG/Np+1.
The canonical homomorphismG→lim←pG/Np is an isomorphism.
(2) Suppose V ⊂U is anOX-acyclic open set. Let A := Γ(V,A), and let
Np := Exp(mpA). Then the cohomology groupsHi(V,Np/Np+1) are trivial
for all p,i ≥1, and the canonical group homomorphismsNp→Γ(V,Np)
and Np/Nq→Γ(V,Np/Nq) are bijective for allq≥p≥1.
34 AMNON YEKUTIELI
Proof. (1) We know that the Lie bracket satisﬁes[mA, mpA]⊂mp+1A. Hence
[G,Np]⊂Np+1, soNp is normal inG andNp/Np+1 is central inG/Np+1. Now
G/Np∼= Exp(Rp−1⊗R mA), and by deﬁnitionExp(mA) = lim←p Exp(Rp⊗R mA).
(2) Since exp : mpA→Np and exp : mpA/mqA→Np/Nq are isomorphisms of
sheaves of sets, andexp : mpA/mp+1A→Np/Np+1 is an isomorphism of sheaves
of abelian groups, we are allowed to switch from groups to Lie algebras. Namely,
it suﬃces to prove the assertions forNp := mpA and Np := mpA.
For the vanishing of cohomology we use the isomorphism of sheaves of abelian
groupsNp/Np+1∼= (mp/mp+1)⊗OU induced by the augmentationA→OU (cf.
[Ye5, Proposition 5.3]) to deduce
Hi(V,Np/Np+1)∼= (mp/mp+1)⊗Hi(V,OU) = 0
fori≥1. The claim that the functionsNp→Γ(V,Np) andNp/Nq→Γ(V,Np/Nq)
are bijective is [Ye9, Corollary 3.6], forR and Rq−1 respectively. □
Theorem7.2 (TotalTrivialization). Assume Setup2.6. We consider the two cases:
⊿ The associative case, in which P(R,X ) is the stack of crossed groupoids
AssDef(R,OX) on X.
⊿ The Poisson case, in which P(R,X ) is the stack of crossed groupoids
PoisDef(R,OX) on X.
Let (G, A, cp) be a twisted object inP(R,X ), and letU be an open set ofX.
(1) If H2(U,OX) = 0 then the groupoidG(U) is nonempty.
(2) If H1(U,OX) = 0 then the groupoidG(U) is connected.
Proof. Letibealocalobjectofthegaugegerbe G, deﬁnedonsomeopenset U⊂X.
We writeAi := A(i)∈P(R,X )(U), which is anR-deformation ofOU. There is
an isomorphism of sheaves of groups cp : G(i)
≃
− →IG(Ai) on U. By deﬁnition
IG(Ai) = Exp(mAi), and hence for anyp≥1 we get a sheaf of normal subgroups
Np(i) := cp−1(
Exp(mpAi)
{
⊂G(i).
By Lemma 7.1(1) the sequence{Np(i)}p≥1 is a central ﬁltration of the sheaf of
groups G(i), in the sense of [Ye4, Deﬁnition 6.1] (except that here the ﬁltration
starts atp = 1, whereas in [Ye4] it starts atp = 0). Also G(i)∼= lim←p G(i)/Np(i).
Next suppose j is another object of G(U), and g∈G(U)(i,j ). Since A(g) :
Ai→Aj is anR-linear sheaf isomorphism, and sincecp : AutG
≃
=⇒IG◦A is a
natural isomorphism of functors, it follows thatAd(g)
(
Np(i)
{
= Np(j). This says
that for ﬁxedp, the collection{Np(i)}is a normal subprestack of groupoids of the
gerbe G, in the sense of [Ye4, Deﬁnition 3.6]. Moreover, there is a central extension
of gerbes
(7.3) 1→Np/Np+1→G/Np+1
F
− →G/Np→1,
and an isomorphism
Np/Np+1∼= (mp/mp+1)⊗OX
of sheaves of abelian groups onX. See [Ye4, Deﬁnition 3.10]. As we letp vary, we
have a central ﬁltration{Np}p≥1 of the gerbe G, and G is complete with respect
to this ﬁltration, as in [Ye4, Deﬁnition 6.5].
LetU andAi be as above, and letV ⊂U be anOX-acyclic open set. According
to Lemma 7.1(2), the open setV is acyclic with respect to the central ﬁltration
{Np(i)}p≥1 of the sheaf of groupsG(i), in the sense of [Ye4, Deﬁnition 6.2].
Now take an open covering U = {Uk}k∈K of X such that Ob(G(Uk)) ⁄= ∅
for every k∈K. This is possible because G is locally nonempty. Since X has
enoughOX-acyclic open sets, we can ﬁnd an open coveringU′={U′
k}k∈K′which
reﬁnesU, and such that each ﬁnite intersectionU′
k0,...,km isOX-acyclic. Note
TWISTED DEFORMATION QUANTIZATION 35
that Ob(G(U′
k0,...,km))⁄=∅. The discussion in the previous paragraph (forV :=
U′
k0,...,km) tells us that the coveringU′is acyclic with respect to the central ﬁltration
{Np}p≥1 of the gerbeG. We conclude that there are enough acyclic coverings with
respect to{Np}p≥1, in the sense of [Ye4, Deﬁnition 6.9].
Finally letU be an open set ofX. Then
Hq(U, Np/Np+1)∼= (mp/mp+1)⊗Hq(U,OX).
According to [Ye4, Theorem 6.10], ifH2(U, Np/Np+1) is trivial for allp≥1, then
then the groupoid G(U) is nonempty; and if H1(U, Np/Np+1) is trivial for all
p≥1, then then the groupoidG(U) is connected. □
Here is an immediate consequence of Theorem 7.2:
Corollary 7.4.In the situation of Setup2.6, and withP(R,X ) as in Theorem7.2,
suppose thatU is anOX-acyclic open covering ofX. Then U totally trivializes
the stack of crossed groupoidsP(R,X ).
For a crossed groupoidG we denote byOb(G) the set of1-isomorphism classes
of objects.
Corollary 7.5. In the situation of Theorem 7.2, suppose that H2(X,OX) =
H1(X,OX) = 0. Then the function
(7.6) Ob
(
P(R,X )(X)
{
→TwOb
(
P(R,X )
{
constructed in Example6.23 is a bijection.
Proof. Let (G, A, cp) be a twisted object of P(R,X ). By Theorem 7.2(1) there
exists an objecti∈Ob
(
G(X)
{
. Let Ai := A(i)∈Ob
(
P(R,X )(X)
{
.Then A is
twisted gauge equivalent to the twisted object generated byAi. We see that the
function (7.6) is surjective.
Now suppose thatA,A′∈Ob(P(R,X )(X)) are such that the corresponding
twisted objects A, A′∈TwOb(P(R,X )) are twisted equivalent. Let
(Φ gau, Φ rep) : (G, A, cp)→(G′, A′, cp′)
be a twisted gauge equivalence. There is an objecti∈Ob(G(X)) such thatA =
A(i), and there is an objecti′∈Ob(G′(X)) such thatA′= A′(i′). Let j′:=
Φ gau(i)∈Ob(G′(X)); so there is an isomorphismΦ rep :A = A(i)
≃
− →A′(j′) in
P(R,X ).
On the other hand, since the groupoidG′(X) is connected, there is some iso-
morphism g′: j′≃
− →i′in it. Therefore we get an isomorphismA′(g′) : A′(j′)
≃
− →
A′(i′) =A′in P(R,X )(X). We see thatA∼=A′in P(R,X )(X). This proves that
function (7.6) is injective. □
We end this section with an example.
Example 7.7. It is easy to construct an example of a commutative twisted as-
sociative (or Poisson) K[[ℏ]]-deformation ofOX that is really twisted (Deﬁnition
4.16). Take an algebraic varietyX with nonzero cohomology classc∈H2(X,OX).
Let U be an aﬃne open covering ofX, and let{ck0,k1,k2}be a normalized Čech
2-cocycle representing c on this covering. Now consider the geometric descent
datum d =
(
{Ak0},{gk0,k1},{ak0,k1,k2}
{
withAk0 :=OUk0 [[ℏ]], gk0,k1 := 1 and
ak0,k1,k2 := exp(ℏck0,k1,k2). The corresponding twisted deformationA that we get
by Theorem 6.22 (namelyA := glu(d) in Lemma 6.21) will have obstruction class
c in the ﬁrst order central extension. More precisely, in the central extension of
36 AMNON YEKUTIELI
gerbes (7.3), withp = 1, the obstruction class for the unique (up to isomorphism)
object j of (G/N 1)(X) is
cl2
F (j) =cℏ∈H2(
X, (m/m2)⊗OX
{
,
which is nonzero. According to [Ye4, Theorem 4.17] we haveOb
(
(G/N 2)(X)
{
=∅,
implying that Ob
(
G(X)
{
=∅.
