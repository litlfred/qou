---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-009-9-from-lie-descent-to-geometric-descent
section_title: "From Lie Descent to Geometric Descent"
section_number: 9
pages: 39-42
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
SupposeG is a sheaf of abelian groups on a topological spaceX. Let us recall
how to construct the Čech cosimplicial abelian groupC(U,G) associated toG and
to an open coveringU ={Uk}k∈K of X. Forp∈N we take the abelian group
(9.1) Cp(U,G) :=
∏
k∈∆ p(K)
Γ(Uk,G).
See formula (6.1) regarding the set ∆ p(K). If k ∈∆ q(K) and α∈∆ q
p, then
α(k)∈∆ p(K), and there is an inclusion of open setsUk⊂Uα(k), so by restriction
there is an induced homomorphismCp(U,G)→Cq(U,G). If G is a sheaf of DG
Lie algebras, thenC(U,G) is a cosimplicial DG Lie algebra.
Now supposeU′={Uk}k∈K′is another open covering ofX, andρ:U′→U is
a reﬁnement. Then there is a homomorphism of cosimplicial DG Lie algebras
(9.2) ρ∗: C(U,G)→C(U′,G),
with an obvious formula.
Setup 9.3. K is a ﬁeld of characteristic0; (R, m) is a parameter algebra overK;
and X is a smooth algebraic variety overK, with structure sheafOX.
This is the same as Setup 2.6, except that hereX is a smooth algebraic variety.
In Section 3 we discussed the sheaves of DG Lie algebrasTpoly,X,Dpoly,X and
Dnor
poly,X on the variety X. Lie descent data Desc(Del((g,R )) for a cosimplicial
quantum type DG Lie algebra g was introduced in Section 8, and its functorial
properties were shown.
40 AMNON YEKUTIELI
Recall the stacks of crossed groupoidsAssDef(R,OX) and PoisDef(R,OX) from
Section 4. Let us writeP(R,X ) for either of these stacks. The geometric descent
data Desc
(
C(U, P(R,X ))
{
was introduced in Section 6. The functorial dependence
of Desc
(
C(U, P(R,X ))
{
on the open coveringU is shown in formula (6.18). Re-
garding the dependence on R, consider a homomorphism of parameter algebras
σ:R→R′. Given a descent datum
d =
(
{Ak0}k0∈K,...
{
∈Desc
(
C(U, P(R,X ))
{
as in (6.4), letA′
k0 :=R′ˆ⊗RAk0, which by Proposition 2.15 is anR′-deformation of
OUk0. There are inducedR′-linear gauge transformationsg′
k0,k1 and induced gauge
elementsa′
k0,k1,k2, andtogetherthesemakeupadescentdatum σ(d) =
(
{A′
k0},...
{
.
This construction is a function
(9.4) σ: Desc
(
C(U, P(R,X ))
{
→Desc
(
C(U, P(R′,X ))
{
,
which respects gauge equivalence.
Theorem 9.5(Geometrization of Descent Data). Let (R, m) andX be as in Setup
9.3, and letU be a ﬁnite aﬃne open covering ofX. We consider two cases:
⊿ The associative case, in which
P(R,X ) := AssDef(R,OX) and g(U) := C(U,Dnor
poly,X).
⊿ The Poisson case, in which
P(R,X ) := PoisDef(R,OX) and g(U) := C(U,Tpoly,X).
So C(U, P(R,X )) and Del(g(U),R ) are cosimplicial crossed groupoids.
In both cases there is a bijection
geo : Desc
(
Del(g(U),R )
{≃
− →Desc
(
C(U, P(R,X ))
{
,
which we callgeometrization. The bijectiongeo respect homomorphisms of param-
eter algebrasR→R′, and reﬁnements of coveringsU′→U.
Proof. By Theorem 3.6 there is a weak equivalence of cosimplicial crossed groupoids
geo : Del(g(U),R )→C(U, P(R,X )).
(Actuallythisisanequivalenceofcrossedgroupoidsineachcosimplicialdimension.)
Theorem 5.6 says thatgeo := Desc(geo) is a bijection. The functorial dependence
on R andU is clear. □
Remark 9.6. More generally, ifG is any sheaf of quantum type DG Lie algebras
on a topological space X, U is an open covering of X, g(U) := C( U,G) and
δ∈Desc
(
Del(g(U),R )
{
, then geo(δ) is a geometric descent datum for a gerbeH
on X. For an index k∈K there is an objectk∈Ob(H(Uk)), and its sheaf of
automorphisms is H(k) = Exp( mˆ⊗G−1)ωk. It might be interesting to study the
kind of gerbes that arise in this way.
Suppose X′is another smooth algebraic variety, andg : X′→X is an étale
morphism. It follows from [Ye2, Proposition 4.6] that there are induced homomor-
phisms of sheaves of DG Lie algebras
(9.7) g∗:Tpoly,X→g∗(Tpoly,X′)
and
(9.8) g∗:Dnor
poly,X→g∗(Dnor
poly,X′)
on X, extending the ring homomorphismg∗:OX→g∗(OX′).
Let U ={Uk}k∈K be an open covering ofX, and U′={U′
k}k∈K′an open
covering ofX′. A morphism of coverings extendingg is a functionρ: K′→K,
TWISTED DEFORMATION QUANTIZATION 41
such that g(U′
k)⊂Uρ(k) for every k∈K′. We also say that ρ: U′→U is a
morphism of coverings extendingg.
Suppose V = {Vl}l∈L is another open covering of X. We get a new open
coveringU∐V :={Wm}m∈M of X, whereM := K∐L, Wm := Um if m∈K,
andWm :=Vm ifm∈L. (Ofcourse U∐V hasalotofredundancy.) If τ:V′→V
is a morphism of coverings extendingg, thenρ∐τ:U′∐V′→U∐V is also a
morphism of coverings extendingg.
Given a morphism of coveringsρ: U′→U extending g, there is an induced
homomorphism of cosimplicial DG Lie algebrasρ∗: g(U)→g(U′). Here we use the
notation of Theorem 9.5, with obvious modiﬁcations; e.g.g(U′) := C(U′,Tpoly,X′)
in the Poisson case.
Theorem 9.9. Let R and X be as in Setup 9.3, let g : X′→X be an étale
morphism of varieties, and let σ: R →R′be a homomorphism of parameter
algebras. We use the notation of Theorem9.5, with obvious modiﬁcations pertaining
to the varietyX′and the algebraR′. Then, both in the Poisson case and in the
associative case, there is a unique function
indσ,g: TwOb
(
P(R,X )
{
→TwOb
(
P(R′,X′)
{
with this property:
(♦) SupposeU (resp.U′) is a ﬁnite aﬃne open covering ofX (resp.X′), and
ρ:U′→U is a morphism of coverings extendingg. Then the diagram of
sets (9.10) is commutative.
(9.10)
Desc
(
Del(g(U),R )
{ geo //
Desc(Del(ρ∗,σ))

Desc
(
C(U, P(R,X ))
{
TwOb
(
P(R,X )
{decoo
indσ,g

Desc
(
Del(g(U′),R′)
{ geo // Desc
(
C(U′, P(R′,X′))
{
TwOb
(
P(R′,X′)
{decoo
Here dec is the decomposition from Theorem6.22, geo is the geometrization from
Theorem 9.5, and Desc(Del(ρ∗,σ)) is the function from Theorem8.8.
Proof. Choose coveringsU andU′, and a morphism of coveringsρ:U′→U, as
in property (♦). This is possible of course. The horizontal arrows in the diagram
are bijections. Deﬁne
indσ,g: TwOb
(
P(R,X )
{
→TwOb
(
P(R′,X′)
{
to be the unique function that makes the diagram commute.
It remains to show that the functionindσ,gis independent of the choice of open
coveringsU andU′, and the of morphismρbetween them. So letV be another
ﬁnite aﬃne open covering ofX, let V′be another such covering ofX′, and let
τ:V′→V be a morphism of coverings extendingg. Consider the open covering
W :=U∐V ofX, the open coveringW′:=U′∐V′ofX′, and the morphism of
coveringsχ:= ρ∐τ:W′→W extending g. We obtain a commutative diagram
of morphisms of coverings
(9.11) U //W Voo
U′
ρ
OO
//W′
χ
OO
V′oo
τ
OO
extendingg vertically, and extending1X and 1X′horizontally. The functoriality in
Theorem 9.5 and in Proposition 6.19, applied to the left square in diagram (9.11),
and to the homomorphismσ: R→R′, yields a big commutative diagram in the
42 AMNON YEKUTIELI
shape of a rectangular box. The front face of this big diagram is the diagram in
property (♦), and the rear face is the same diagram but withW instead ofU. All
horizontal arrows in the big diagram are bijections. It follows that the function
indσ,gis the same when deﬁned usingχ:W′→W. But then, working with the
right square in diagram (9.11), we see that the functionindσ,gis also the same when
deﬁned usingτ:V′→V . □
