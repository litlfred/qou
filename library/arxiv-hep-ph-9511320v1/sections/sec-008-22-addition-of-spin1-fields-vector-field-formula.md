---
doc_id: arxiv-hep-ph-9511320v1
doc_title: "TK 95 31 CHIRAL LAGRANGIANS FOR BARYONS COUPLED TO MASSIVE SPIN–1 FIELDS ⋆"
section_id: sec-008-22-addition-of-spin1-fields-vector-field-formula
section_title: "Addition of Spin–1 Fields: Vector Field Formulation"
section_number: 2.2
pages: 8-11
source_pdf: 9511320v1.pdf
source_sha256: 4336112cecabdfdf
doc_brief: "TK 95 31 CHIRAL LAGRANGIANS FOR BARYONS COUPLED TO MASSIVE SPIN–1 FIELDS ⋆ — We analyze the eﬀective low–energy ﬁeld theory of Goldstone b osons and baryons chirally coupled to massive spin–1 ﬁelds."
---
We now consider the three vector Vµ representing the three degrees of freedom
of a massive spin–1 vector ﬁeld (the generalization to axials is straigh tforward).
We do not assign any particular microscopic dynamics to this vector ﬁ eld,
8
like it is e.g the case in the hidden symmetry [24] or the massive Yang–Mills
approaches [12]. Vµ is assumed to have the standard transformation properties
of any matter ﬁeld under the non–linearly realized chiral symmetry,
Vµ → h(φ, g) Vµ h(φ, g)−1 . (23)
The corresponding free–ﬁeld Lagrangian reads
L0 = −1
4 Tr
(
Vµν V µν − 2 M 2
V Vµ V µ
)
, (24)
with the (abelian) ﬁeld strength tensor
Vµν = Dµ Vν − Dν Vµ . (25)
The relation to the massive Yang–Mills or hidden symmetry approach is dis-
cussed in Ref.[10]. The propagator is readily evaluated,
Gµρ (x, y) = < 0| T { Vµ (x) , V ρ(y) } |0 >
= −i
∫ d4k
(2π)4 e−ik·(x−y) gµρ − kµ kρ/M2
V
k2 − M 2
V + iǫ . (26)
For the eﬀective action discussed below, we also need the following th ree– and
four–point functions
− i ∆ µν,ρ (x, y) = < 0| T { Vµν (x) , V ρ(y) } |0 > ,
−i ∆ µν,ρσ (x, y) = < 0| T { Vµν (x) , V ρσ (y) } |0 > ,
−i ∆ †
µν,ρσ (x, y) = < 0| T { ¯Vµν (x) , ¯Vρσ (y) } |0 > , (27)
with ¯Vµν = Dµ Vν + Dν Vµ . These three- and four–point functions are related
to the tensor ﬁeld propagator, Eq.(16), and its derivative via
1
i ∂σ
y Gµν,ρσ (x, y) = −∆ µν,ρ (x, y) ,
1
i Gµν,ρσ (x, y) = − 1
M 2
V
∆ µν,ρσ (x, y) + 1
M 2
V
( gµρ gνσ − gµσ gνρ ) δ(4)(x − y) ,
(28)
where the contact terms in the second relation will be of importance later on
(see also Ref.[10]). The interaction Lagrangian of the vectors with p ions and
external vector and axial–vector sources takes the form
Lint = − 1
2
√
2
(
fV Tr(Vµν f µν
+ ) + igV Tr(Vµν [uµ , uν])
)
, (29)
9
and equivalence to the tensor ﬁeld formulation for the spin–1 pole co ntribu-
tions (which are of order q6) is achieved by setting [10]
fV = FV
MV
, g V = GV
MV
. (30)
Including the baryon octet B leads to the following terms at order O(q) for the
BφV interactions (see again appendix A for some details on the construc tion
of these terms)
L(1)
BφV = KD/F Tr [ ¯B σµν (Vµν , B ) ]
+ GD/F Tr [ ¯B γµ (Vµ , B ) ]
+ LD/F Tr [ ¯B σµν (Vµλ , [Dλ , [Dν, B]] ) ]
+ HD/F Tr [ ¯B σµν ( ¯Vµλ , [Dλ , [Dν, B]] ) ] , (31)
The ﬁrst term in Eq.(31) when contracted with two u′
µ s or a ﬁeld strength ten-
sor contributes to order q3 while the other terms only start one order higher.
However, for the equivalence of the spin–1 pole contributions they have to be
retained, as shown in the next subsection (compare to the spin–1 p ole terms in
the meson sector which are of order q6). The fourth term in Eq.(31) is of rele-
vance for some additional q4 terms. Because it includes the symmetric tensor
¯Vµν = ¯Vνµ , it apparently has no counterparts in the tensor ﬁeld formulation,
where only the antisymmetric tensor Wµν appears. That there is, however, no
inequivalence is shown in appendix A. The real constants ( K, G, H, L)D/F are
not ﬁxed by chiral symmetry, we only assume that they are non–va nishing.
The corresponding eﬀective action takes the form
Seﬀ = −
∫
d4x d4y
{
KD/F Tr
[
¯B(y) σλρ ∆ µν,λρ (x, y) ( J µν (x) , B (y) )
]
+ GD/F Tr
[
¯B(y) γρ ∆ µν,ρ (x, y) ( J µν (x) , B (y) )
]
+ LD/F Tr
[
¯B(y) σλρ ∆ µν,λσ (x, y) ( J µν (x) , [Dρ, [Dσ , B(y)]] )
]
+ HD/F Tr
[
¯B(y) σλρ ∆ †
µν,λσ (x, y) ( J µν (x) , [Dσ , [Dρ, B(y)]] )
]}
,
(32)
and the antisymmetric currents Jµν are expressed in terms of the constants
fV and gV . Notice that terms of the type Tr( ¯BDµ V µ B) do not contribute
to the eﬀective action as shown in appendix A. This completes the for mal-
ism necessary to proof the equivalence between the tensor and ve ctor ﬁeld
approaches.
10
