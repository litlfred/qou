---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-025-0-eπq-remains-invariant-under-de
section_title: "(E,π,Q ) remains invariant under de-"
section_number: 0
pages: 43-45
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
formations of the geometric data, that is to say of Q or (E,π ) itself, as long as
the structure of the ends remains unchanged. Finally, we sho uld prove that the
relative invariant is independent of the Je, which more accurately means that it
commutes with the canonical isomorphisms between Floer coh omology groups
for diﬀerent Je. We omit this entirely, both because it is not important for o ur
purpose, and because it would require a digression concerni ng “continuation
maps”.
Two ways of gluing together surfaces with strip-like ends wi ll play a role
later on. One of them is a close cousin of that considered as in Section 2.1. It
can be formulated in various degrees of generality, but we wi ll need only one
special case. Suppose then that S1 is a surface with strip-like ends, and S2 a
compact surface, together with points ζk∈∂Sk (ζ1 should not lie on any end;
that can of course always be achieved by making the ends small er). Let (Ek,πk)
be exact Lefschetz ﬁbrations over Sk with Lagrangian boundary conditions Qk;
(E1,π 1) should be trivial over the ends. We also want to have M , L, maps
φk : M→ (Ek)ζk , and trivializations ( ψk, Ψ k), with the same properties as in
Section 2.1. The boundary connected sum S =S1#ζ1∼ζ2S2 is a surface with the
same kind of strip-like ends as S1. As before one constructs an exact Lefschetz
ﬁbration ( E,π ) on it with a Lagrangian boundary condition Q, modelled over
the ends on the same Lagrangian submanifolds as Q1.
Choose complex structures jk onSk such that (ψk)∗jk is standard; j1 should
also be standard on the ends. Take {Je} and J 1∈ Jreg (E1,π 1,Q 1,j 1,{Je}) as
when deﬁning the relative invariant of ( E1,π 1,Q 1); as an additional condition,
we want (Ψ 1)∗J 1 to be the product of the standard complex structure on ¯D+(1)
and some ﬁxed almost complex structure on M . By Lemma 2.20 this can be
done while still achieving regularity. Using Lemmas 2.4 and 2.5 one ﬁnds a
J 2∈ Jreg(E2,π 2,Q 2,j 2) with the same restriction on (Ψ 2)∗J 2, and such that
the evaluations
evζ1| MJ 1 ({xe}) : MJ 1 ({xe})−→Q1
ζ1∼=L,
evζ2| MJ 2 : MJ 2−→Q2
ζ2∼=L
(2.27)
are transverse to each other for every {xe}. Let J ∈ J(E,π,j, {Je}) be the
almost complex structure constructed from J 1,J 2. As in Proposition 2.7, this
will be regular for small values of the parameter ρ, and
MJ ({xe})[0]∼= (MJ 1({xe})×L MJ 2)[0], (2.28)
where the [0] denotes on both sides the zero-dimensional com ponent of these
43
manifolds. We will not need the full “gluing formula” which o ne can obtain
from this, but only a special case:
Lemma 2.21. If Φ 1(E2,π 2,Q 2) = 0 then Φ rel
0 (E,π,Q ) = 0 .
Proof. For simplicity, suppose that Φ 1(E2,π 2,Q 2) vanishes even when taken
in the cobordism ring MO ∗(L). This means that there is a compact manifold
with boundary G and a smooth map g : G→ L, such that ∂G = MJ 2 and
g|∂G = evζ2. After perturbing it slightly, one can assume that g is transverse
to all maps evζ1 in (2.27). Then the ﬁbre products
G({xe}) = MJ 1({xe})×LG (2.29)
are smooth manifolds. The evaluation map extends continuou sly to the Gromov-
Floer compactiﬁcation, so that one can deﬁne compactiﬁcati ons G({xe}) in the
obvious way. It is not diﬃcult to see, using (2.25), that the z ero-dimensional
part G({xe})[0] is a ﬁnite set; one counts the points ξJ,G,g({xe}) ∈ Z/2 in
it, and uses that to deﬁne a map k between the Floer cochain groups asso-
ciated to (E1,π 1,Q 1), as in (2.26). We claim that this is a homotopy between
CΦ 0
rel(E,π,Q,J ) and the zero map. As usual, the proof is based on analyzing
the ends of the one-dimensional moduli spaces. The closure i n G({xe}) of the
one-dimensional part G({xe})[1] is a compact one-manifold with boundary, and
its boundary points are of two kinds: ﬁrst, boundary points o f G({xe})[1] itself,
∂G({xe})[1] = ( MJ 1 ({xe})×L∂G)[0]∼= MJ ({xe})[0]; their number modulo two
is νJ ({xe}) by deﬁnition. The second kind of boundary points are of the f orm
(u,σf,1)×q∈ MJ ({xe})×LG. This means that for some end f , and points
{ˆxe} with ˆxe =xe for all e⁄=f , one has
u×q∈ G({ˆxe})[0], σ f,1∈
{
(F∗(xf, ˆxf )/R)[0] if e is a negative end,
(F∗(ˆxf,xf )/R)[0] if e is a positive end.
The number of such boundary points is
∑
f ∈I −
∑
ˆxf
nJf (xf, ˆxf )ξJ,G,g({ˆxe}) +
∑
f ∈I +
∑
ˆxf
ξJ,G,g({ˆxe})nJf (ˆxf,xf )∈ Z/2.
The fact that this is equal to νJ ({xe}) gives precisely the desired equality dk +
kd =CΦ rel
0 (E,π,Q,J ).
The other and maybe more obvious gluing process is to join tog ether two ends.
Assume that S1,S 2 are surfaces with strip-like ends, such that S1 has a single
positive end e1, and S2 a single negative end e2 (this is not really a restriction
since, as has been mentioned before, positive ends can be tur ned into negative
ones and vice versa). Choose some σ >0, and deﬁne S =S1#e1∼e2S2 by taking
S1\γe1 ((σ;∞)× [0; 1]) and S2\γe2 ((−∞;−σ)× [0; 1]), and identifying γe1 (s,t )
with γe2 (s−σ,t ) for (s,t )∈ [0;σ]× [0; 1]. The ends of S are the negative ends
of S1 together with the positive ends of S2. After choosing complex structures
44
jk onSk which are standard over the ends, there is an obvious induced complex
structure j on S.
Let (L0,L 1) be a pair of exact Lagrangian submanifolds in M . Suppose that
we have exact Lefschetz ﬁbrations ( Ek,πk) over Sk, trivial over the ends, and
Lagrangian boundary conditions Q1,Q 2 for them modelled on ( L0,L 1) over e1
and overe2, respectively. Then one can form an exact Lefschetz ﬁbratio n (E,π )
overS by identifying Γ e1 (s,t,y )∈E1 with Γ e2 (s−σ,t,y )∈E2, in parallel with
the construction on the base. This comes with an obvious Lagr angian boundary
conditionQ. Choose almost complex structures Jk onEk so as to deﬁne relative
invariantsCΦ rel
