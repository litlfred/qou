---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-011-11-twisted-quantization
section_title: "Twisted Quantization"
section_number: 11
pages: 45-48
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
LetX be a smooth algebraic variety overK, andR a parameter algebra. We have
the stacks of crossed groupoidsPoisDef(R,OX) and AssDef(R,OX) onX. Recall
that a twisted object ofPoisDef(R,OX) is a twisted PoissonR-deformation ofOX,
and a twisted object ofAssDef(R,OX) is a twisted associativeR-deformation of
OX. We denote byTwOb(−)the sets of twisted gauge equivalence classes of twisted
objects. First order brackets were deﬁned in Deﬁnition 4.15.
Here is the main result of our paper (the expanded form of Theorem 0.10.1).
Theorem 11.1.Let K be a ﬁeld containing the real numbers, letR be a parameter
K-algebra, and letX be a smooth algebraic variety overK. Then there is a bijection
of sets
tw.quant : TwOb
(
PoisDef(R,OX)
{ ≃
− →TwOb
(
AssDef(R,OX)
{
called twisted quantization, having these properties:
(i) If g : X′→X is an étale morphism of varieties, and ifσ: R→R′is a
homomorphism of parameter algebras, then the diagram
TwOb
(
PoisDef(R,OX)
{ tw.quant //
indσ,g

TwOb
(
AssDef(R,OX)
{
indσ,g

TwOb
(
PoisDef(R′,OX′)
{ tw.quant // TwOb
(
AssDef(R′,OX′)
{
(cf. Theorem9.9) is commutative.
(ii) The bijection tw.quant preserves ﬁrst order brackets. Namely ifA is a
twisted PoissonR-deformation ofOX, and B := tw.quant(A), then
{−,−}A ={−,−}B.
Proof. We shall use the diagram in Figure 1 (that appears in Subsection 0.10 of the
Introduction). Let (U,s) be a ﬁnite aﬃne open covering with étale coordinates of
X. By Theorem 6.22 and Corollary 7.4 we get the bijectionsdec in the diagram.
46 AMNON YEKUTIELI
From Theorem 9.5 we get the bijectionsgeo in that diagram. By applying Theorem
8.8 to the diagram in Theorem 10.6 we obtain the bijections
mix := Desc(Del)(C(U, mix), 1R)
and
Ψ s := Desc(Del)(C(U, Ψ s), 1R)
in the diagram in Figure 1. We deﬁnetw.quant to be the unique bijection making
this diagram commutative.
The whole diagram in Figure 1 is functorial w.r.t.R and (U,s); this is a conse-
quence of Theorems 9.9 and 10.6.
Consider another ﬁnite aﬃne open covering with étale coordinates(V,t) of X,
and a morphism of coverings with coordinates(V,t)→(U,s). The functoriality
of the diagram in Figure 1 implies that the bijectiontw.quant is the same when
deﬁned with respect(V,t).
Now suppose (V,t) is any ﬁnite aﬃne open covering with étale coordinates of
X. As in the proof of Theorem 9.9, we get a third covering with étale coordinates
(W,r), whereW := U∐V and r := s∐t. There are morphisms of coverings
(U,s)→(W,r) and (V,t)→(W,r). By the previous paragraph, the bijection
tw.quantis the same when deﬁned with respect to any of these three coverings with
étale coordinates. We conclude thattw.quant is independent of the choices made.
Let g : X′→X be an étale morphism of varieties, and letσ: R→R′be
a homomorphism of parameter algebras. Choose any morphism of coverings with
coordinate ρ: (U′,s′)→(U,s) extending g. The functoriality of the diagram in
Figure 1 implies that there is a commutative diagram as stated in property (i).
It remains to prove that property (ii) holds. Let A and B be such twisted
R-deformations. Consider the corresponding Lie descent data
(ω,g,a)∈Desc
(
Del(C(U,Tpoly,X),R )
{
and
(χ,h,b)∈Desc
(
Del(C(U,Dnor
poly,X),R )
{
.
They are related by the equation
(χ,h,b) = Desc(Del)(C(U, Ψ s), 1R)((ω,g,a))
∈Desc
(
Del(C(U, MixU(Dpoly,X)),R )
{
,
where (χ,h,b) and (ω,g,a) are the equivalence classes. We have to show that the
ﬁrst order brackets{−,−}A and{−,−}B onOX are equal.
The ﬁrst order brackets{−,−}A and{−,−}B depend only onωandχ. Indeed,
by Deﬁnitions 4.15 and 2.20 we have{c1,c 2}A ={c1,c 2}ωand{c1,c 2}B ={c1,c 2}χ
forlocalsections c1,c 2∈OX, where{c1,c 2}ω:=ψ+(Υ 1(ω)(c1,c 2))and{c1,c 2}χ:=
ψ+(χ(c1,c 2)). Here ψ+ is the homomorphism from equation (2.18), andΥ 1 is the
antisymmetrization. Property (iii) of Theorem 8.8 says thatχ= MC(1R⊗Ψ s)(ω)
in
MC
(
mˆ⊗C0(U, MixU(Dpoly,X))
{
.
The ﬁrst order brackets are functorial inR, and hence we can assume that
m2 = 0, so m/m2 = m. Now the contribution of the higher order terms Ψ s;i,
i≥2, to MC(1R⊗Ψ s) is zero, because m2 = 0. Therefore the elements χand
χ′:= ( 1R⊗Ψ s;1)(ω) of m⊗C0(U, MixU(Dpoly,X)) are gauge equivalent. We
conclude that{−,−}χ={−,−}χ′.
A little calculation shows that the ﬁrst order bracket{−,−}χ′depends only
on the cohomology class [χ′] of χ′in m⊗C0(
U, H1(MixU(Dpoly,X))
{
; this is a
manifestation of the gauge invariance of ﬁrst order brackets. But according to
Theorem 10.3(2) we have[χ′] = [Υ 1(ω)]. We see that{−,−}χ′={−,−}ω. □
TWISTED DEFORMATION QUANTIZATION 47
Corollary 11.2. In the situation of Theorem11.1, assume the cohomology groups
H1(X,OX) and H2(X,OX) vanish. Then there is a bijection
quant :{PoissonR-deformations ofOX}
gauge equivalence
≃
− →{associative R-deformations ofOX}
gauge equivalence .
It preserves ﬁrst order brackets, and commutes with homomorphismsR→R′and
étale morphismsX′→X (such thatX′also has these cohomology vanishing prop-
erties).
Proof. Combine Theorem 11.1 and Corollary 7.5. □
A formal Poisson bracketon the augmented commutativeR-algebra Rˆ⊗OX is
anR-bilinear Poisson bracket{−,−}that vanishes modulom; so it makesRˆ⊗OX
into a PoissonR-deformation ofOX. A star producton the augmentedR-module
Rˆ⊗OX is an associative unital R-bilinear multiplication, with unit 1⊗1, that
reduces modulo m to the commutative multiplication ofOX; so it makesRˆ⊗OX
into an associativeR-deformation ofOX.
By deﬁnitionT 0
poly,X =TX, the sheaf of derivations, andD0
poly,X =DX, the
sheaf of diﬀerential operators.
Corollary 11.3. In the situation of Theorem11.1, assume the cohomology groups
H1(X,OX), H2(X,OX), H1(X,TX) and H1(X,DX) all vanish. Then there is a
canonical bijection
quant :{formal Poisson brackets onRˆ⊗OX}
gauge equivalence
≃
− →{star products onRˆ⊗OX}
gauge equivalence .
It preserves ﬁrst order brackets, and commutes with homomorphismsR→R′and
étale morphismsX′→X (such thatX′also has these cohomology vanishing prop-
erties).
Proof. Theorem 3.6 implies the following: if H1(X,Dnor,0
poly,X) = 0 , then every as-
sociative R-deformationA ofOX is sheaf theoretically trivial, namely there is an
isomorphismA∼=Rˆ⊗OX of sheaves ofR-modules, that commutes with the aug-
mentations toOX and preserves the units. The proof is the same as that of [Ye1,
Theorem 1.13], using Remark 3.7. Since there is an isomorphism of sheaves of
K-modulesDX∼=OX⊕Dnor,0
poly,X, our assumptions imply thatH1(X,Dnor,0
poly,X) = 0.
Hence associative deformations are the same, up to gauge equivalence, as star prod-
ucts.
Similarly, the vanishing of H1(X,TX) implies, via Theorem 3.6, that Poisson
deformations are the same as formal Poisson brackets.
The quantization statement is now the same as in Corollary 11.2. □
Example 11.4.The conditions of Corollary 11.3 hold forX := Pn
K,n≥1. Indeed,
since X is aD-aﬃne variety, we know thatHi(X,DX) = 0 for all i > 0. The
vanishing ofHi(X,OX) and Hi(X,TX) for i> 0 follows from [Ha, Theorem III.5.1
and Example II.8.20.1]. We thank Van den Bergh for mentioning this to us.
Remark 11.5. When X is an aﬃne variety, the quantization map of Corollary
11.3 coincides with that of [Ye1, Theorem 0.1]. This can be seen by looking at the
construction of these quantization maps. (For [Ye1, Theorem 0.1] please consult
the corrected proof in the Erratum.)
48 AMNON YEKUTIELI
Remark 11.6. The reason we require thatK contains R is because we rely on the
original universal L∞formality quasi-isomorphism
(11.7) Υ = {Υi}i≥1 :Tpoly(R[t])→Dpoly(R[t])
of Kontsevich for the polynomial ringR[t] = R[t1,...,tn]; see [Ko1]. However Υ
can be replaced with any other L∞quasi-isomorphism Υ′in the proof of [Ye1,
Theorem 0.2], as long asΥ′has properties (P)-(P5) of [Ko1].
Now D.E. Tamarkin found a construction of such anL∞quasi-isomorphism Υ′
over Q(see [Ta], and [CV, Appendix] for a complete proof.) Therefore the condition
R⊂K can in fact be removed.
We end the paper with a few questions. A twistedK[[ℏ]]-deformation A ofOX is
called symplectic if the ﬁrst order bracket{−,−}A is a symplectic Poisson bracket
onOX (cf. Proposition 2.21(3)). This is the most noncommutative deformation
possible: the center of a local objectA of A is the subsheafK[[ℏ]]⊂A.
Question 11.8. It is easy to construct an example of acommutative twisted as-
sociative K[[ℏ]]-deformation ofOX that is really twisted – see Deﬁnition 4.16 and
Example 7.7. But does there exist a varietyX, with asymplectictwisted associative
K[[ℏ]]-deformation A ofOX which is really twisted? Perhaps the results of [BK]
can be useful here.
A more concrete (but perhaps much more challenging) question is:
Question 11.9.LetX be a Calabi-Yau surface overK (e.g. an abelian surface or a
K3 surface), and letαbe a symplectic Poisson bracket onOX (namely any nonzero
section of Γ(X,⋀2
OX
TX)). Consider the Poisson K[[ℏ]]-deformationA :=OX[[ℏ]],
withformalPoissonbracket ℏα, andlet Abethecorrespondingtwisteddeformation
(see Example 6.23). LetB := tw.quant(A). Is B really twisted? If so, what is the
signiﬁcance of this phenomenon? Note that the obstruction classes forB can be
calculated explicitly; but these calculations look quite complicated. Kontsevich
[private communication] appears to think that the twisted deformationB is really
twisted, and he has an indirect argument for that.
Question 11.10. The construction of theL∞quasi-isomorphism Ψ s in Theorem
10.3 relied on the explicit universal formality quasi-isomorphismΥ of Kontsevich;
see (11.7) above. But suppose another universal formality quasi-isomorphismΥ′
is used. Then the twisted quantization map tw.quant may change. Indeed, it
is claimed by Kontsevich [Ko3] that the Grothendieck-Teichmüller group acts on
the quantizations by changing the formality quasi-isomorphism (or in other words,
the Drinfeld associator), and sometimes this action is nontrivial. The question is:
does this action change the geometric nature of the resulting twisted associative
deformation – namely can it change from being really twisted to being not really
twisted?
