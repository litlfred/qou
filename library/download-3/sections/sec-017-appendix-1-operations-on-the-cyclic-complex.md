---
doc_id: download-3
doc_title: "Algebraic index theorem"
section_id: sec-017-appendix-1-operations-on-the-cyclic-complex
section_title: "Operations on the Cyclic Complex"
section_number: Appendix 1
pages: 34-37
source_pdf: Download (3).pdf
source_sha256: 7c2b83ba9f9baad7
toc_source: inferred
doc_brief: "Algebraic index theorem — We prove the Atiyah-Singer index theorem where the algebra of pseudo- differential operators is replaced by an arbitrary deformation quantization of the algebra of functions"
---
Let A be an associative unitary algebra over an associative commutative unitary ring
k. Let A = A/k 
1;
define the operations
LD : Cm(A) -+ Cm(A} 
io : Cm(A)
SD : Cm(A)
k. Let A = A/k 
1; Cm(A) = A ® A®
m . For any ^-linear map D : A -» A, D(l) = 0,
LD(aQ (8) . - . (8) am) = 
(-l)
/ ?'-
l D« 0 0 
0 D(0/) 0 
0 am ,
/=o
where ^ = Σ;=o(l
flyl ~ 0;
ώ(αo 0 
(8> am) = (- 1 )
(k/ol + 1 )|D| + l*
o lfl 0 
D(aλ ) 0 a2 (8) 0 ί/Λ
x(l Θα, 0 ..
For any a G ^4, define the operations
m+\ 
i
/ = ! / = !
x (1 0α, 0 ... 0αw &α 0® •• 0fl ( /-i)(S)fl(X) ••• 0α/-ι).
Let g — Der(/4) be the graded Lie algebra of derivations of A. Let A be the
usual g-module A with the grading shifted by 1 : for a £ A, we write a £ 4 and
β = |α + 1. Let QxA be the semi-direct product;
[D + a,E + b] = [D,E]+D(b) + (-\}\
a
Define the derivation δ : ax A —» qx^;
Let (7(cjx4) be the universal enveloping algebra of $xA. The grading of
A and the derivation δ induce the structure of a differential graded algebra on
Algebraic Index Theorem 
257
U(c\xA). We need the following map
U(QxA) -> Homk(A,A)+A 
(Al)
for D, G g and a £ A, the image of D\ ... Dp is Z>ι o 
o Z)/; : A ^ A and the image
Z)ι . . . £>/;α is DI o 
o Dp(a) G 4.
For 7 G £/(g x4)> we shall denote by Y the image of Y under the map (Al).
Put
SY = i$y; 
ίγ = ί-y\ 
LY = Ly .
Finally, put IY = ίγ + (-\)\
Y\SY.
Let A : £/(gx,4) — » U($xA)®
2 
be the standard comultiplication. We denote
AY = £7ι 0 72 = Γ 0 1
Let b be the Hochschild differential and B be the cyclic differential from Sect. 2.
Theorem Al. Let D, E £ $xA. Then
[B + b, LD] = LδD-9 
(A3)
•/ y++^y, 
(A4)
, 
D[...Dk = LDl - LDk.
The proof follows from the direct computations.
Let us say a few words about the meaning of this theorem. If [ID, IE] were equal
to zero, then there would be no need in the operators Iγ, where 7 is in ί/(g x^)
but not in g xA. Let ε be an odd formal parameter, ε
2 = 0; let ($xA)[ε] = (g x
A) 0A k[έ\; put (d/dε)(D + εE) = -E\ then ((g xA)[ε] 
9 δ + δ/δε) is a differential
graded Lie algebra. If [//), /^] were equal to zero, this would mean together with
(A2), (A3) that the differential ^-graded algebra ((g xA)[ε]', δ + d/cε) acts on the
Z2-graded complex (CCf
r (A); b + B).
In reality [/£>, /^JΦO. We claim that, because of (A4), (gx4)M acts on
CCΓ'(^) up to homotopy. What we will in fact show is that another differential
graded algebra, which is homotopicallyat equivalent to ί/(g xA), acts on CC£
el (A).
Let (α,(5) be a differential graded Lie algebra. Define BQ(a ) to be the free
algebra with the generators 7y, 7 G ί/(α )
+ (the augmentation ideal); we assume
that Iγ is linear in 7 and that \Iγ\ = \Y\ + 1. Let d be the derivation of BQ(CL ) such
that
dIY = -IδY - Σ(-0
| r ι l/r Γ 
/r+ . 
(A5)
The algebra ί/(α ) acts on BQ(CL ) in the obvious way. Let U(a )x5o(α ) be the
semidirect product. The differentials d on BQ and δ on ί/(α ) combine to provide
the obvious differential d on C/(α ) x#o(α ). We modify this differential a little bit;
put
d'Y = δY, 
Y G ί/(α ); d
/IY=dIY + Y. 
(A6)
We denote the differential graded algebra (ί/(α ) xBG(a ); J
7) by B(a ).
258 
R. Nest, B. Tsygan
Theorem A2. The differential 
TL^-graded algebra B($xA) acts on the ^-graded
complex CCΓ(A).
Proof. This is obvious from (A2)-(A5).
Theorem A3. The embedding k 
1
 c—» B(a ) is a quasi-isomorphism for any α .
Proof. The algebra (Bo(a ) , d ) is a partial case of the well known construction; this
is the cobar construction of the chain complex of the Abelian algebra α 
ε C α [ε].
It is well known that there is a quasi-isomorphism BQ(a ) —» ^(
α 
ε) — Λ*(α ).
The theorem follows easily. 
D
We can conclude that the algebra #o(
α ) is a free α -module resolution of the
trivial α -module k. Let R*(a ) be the standard resolution. Then there is the chain
map /^(α ) —> B(a ).
Combining this with the action of B(Q xA_) on CC*
eι(A) we obtain the crucial
functorial chain map
R*($xA) ® CCf
l(A) Λ CCf'OO. 
(A7)
This map is (g x 4)-equivariant (QxA acts only on the tensor factor R*($xA)
of the left-hand side; it acts on the right-hand side by the operators LD).
For example, let τ : A/$A —>• k be a trace. Then τ extends to a (g x /4)-invariant
functional on CC*
eι(A). Consider the composition
C*(g xA) (8) CCf
r(/ί) = k
we obtain the map
from Subsect. 2.3.
Let us make a few concluding remarks. Let (C*, (5) be a differential graded
coalgebra. Let Cobar (C*) be the tensor algebra of C* with shifted grading; we
denote the free generators by Jc, c G C*, and \JC\ = c\ -\- 1. Let d be the derivation
of Cobar (C*) such that
where Ac = ]P cj 0 Q is the comultiplication in C*. Then d
2 = 0 and Cobar (C*, J)
is a differential graded algebra (cf. [Q]). Let α be a differential graded Lie alge-
bra, C*(α ) the standard chain complex of α (Sect. 2); C5k
f(α ) = 0/>0 Λ' α then
C+(α ) is a coalgebra. The homomorphism of differential graded algebras
φ : Cobar C+(α ) -» ί/(α ) ,
φ(JD) = D, 
Z ) G α ; 
φ(Jc) = Q, c G A
> ! a ,
is a homotopy equivalence of complexes.
Algebraic Index Theorem 
259
Theorem A4. 
There 
exists 
an action of 
the differential 
graded 
algebra
Cobar C£($xA) on the ^-graded complex CC*
cl(A) such that:
i) for D G /\
l(QxA), the generator Jo acts via the operator Lol
ii) for εD G /\
l(ε($xA))9 the generator Jί:D acts via the operator ID.
Sketch of the proof. First, note that (for any α ), as a coalgebra and as an α -
module, ί/(α ) ~ 5(α ). Let us modify the definition of the algebra #(α ) above.
The only difference is in the differential; if d is the differential in (7(α ) xBo(a ),
then put
Y G5
1 > 1α .
The algebra (£/(α )x$o(
α W) is denoted by #ι(α ). One checks easily that
#o(α )
 and ^ι(
α )
 are in fact isomorphic and that B\(a ) is a homomorphic image
of Cobar C+(α). 
D
Saying that C+(α ) acts on a complex C* is the same as saying that there is
a twisting cochain of α with coefficients in End C*. A twisting cochain is an odd
cochain p G C*(α End C*) such that
The operators /,£>, //), 5/), where D G Der(g) were introduced by Rinehart [R];
he proved that [B + bJD] = LD.
From our point of view, the map given by (A7) is crucial for understanding
differential geometric nature of periodic cyclic homology. If the periodic complex is
the non-commutative analogue of the de Rham complex then (A7) is the analogue
for the classical formula
Finally we would like to mention that our approach to operations is close to Get-
zler's, cf. [Ge]; the algebra cj xA can be extended to the algebra of all Hochschild
cochains ([Ge, DT]). This extension plays an important role in Getzler's construc-
tion of Gauss-Manin connection in periodic cyclic homology, in Nistor's study of
the bi variant Chern character, [N], and in [CFS].
