---
doc_id: arxiv-math-0702128v3
doc_title: "PENTAGON AND HEXAGON EQUATIONS"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-3
source_pdf: arxiv-math-0702128v3.pdf
source_sha256: f298954dfde00525
toc_source: outline
doc_brief: "PENTAGON AND HEXAGON EQUATIONS — The author will prove that Drinfel’d’s pentagon equation im plies his two hexagon equations in the Lie algebra, pro-unipotent , pro- l and pro- nilpotent contexts."
---
1. Lie algebra case 3
2. Proof of Theorem 1 5
3. Proof of Theorem 2 8
References 9
0. Introduction
In his celebrated papers on quantum groups [Dr86, Dr90, Dr91 ] Drinfel’d came
to the notion of quasitriangular quasi-Hopf quantized univ ersal enveloping algebra.
It is a topological algebra which diﬀers from a topological H opf algebra in the sense
that the coassociativity axiom and the cocommutativity axi om is twisted by an
associator and an R-matrix satisfying a pentagon axiom and t wo hexagon axioms.
One of the main theorems in [Dr91] is that any quasitriangula r quasi-Hopf quantized
universal enveloping algebra modulo twists (in other words gauge transformations
[K]) is obtained as a quantization of a pair (called its class ical limit) of a Lie algebra
and its symmetric invariant 2-tensor. Quantizations are co nstructed by universal
associators. The set of group-like universal associators f orms a pro-algebraic variety,
denoted M . Its non-emptiness is another of his main theorem (reproved in [B]).
Our ﬁrst theorem is on the deﬁning equations of M .
Let us ﬁx notation and conventions: Let k be a ﬁeld of characteristic 0, ¯k its
algebraic closure and U F2 =k⟨⟨X,Y ⟩⟩a non-commutative formal power series ring
with two variables X and Y . Its element ϕ = ϕ (X,Y ) is called group-like if it
satisﬁes ∆( ϕ ) = ϕ ⊗ϕ with ∆( X) = X⊗ 1 + 1⊗X and ∆( Y ) = Y⊗ 1 + 1⊗Y
and its constant term is equal to 1. Its coeﬃcient of XY is denoted by c2(ϕ ).
For any k-algebra homomorphism ι : U F2→ S the image ι(ϕ )∈ S is denoted by
ϕ (ι(X),ι (Y )). Let a4 be the completion (with respect to the natural grading) of th e
Lie algebra over k with generators tij (1 ⩽ i,j ⩽ 4) and deﬁning relations tii = 0,
tij =tji, [tij,t ik +tjk ] = 0 (i,j,k: all distinct) and [ tij,t kl] = 0 (i,j,k,l: all distinct).
Theorem 1. Let ϕ = ϕ (X,Y ) be a group-like element of U F2. Suppose that ϕ
satisﬁes Drinfel’d’s pentagon equation:
(1) ϕ (t12,t 23 +t24)ϕ (t13 +t23,t 34) = ϕ (t23,t 34)ϕ (t12 +t13,t 24 +t34)ϕ (t12,t 23).
1
2 HIDEKAZU FURUSHO
Then there exists an element (unique up to signature) µ ∈ ¯k such that the pair
(µ,ϕ ) satisﬁes his two hexagon equations:
(2) exp {µ (t13 +t23)
2 } =ϕ (t13,t 12) exp{µt 13
2 }ϕ (t13,t 23)−1 exp{µt 23
2 }ϕ (t12,t 23),
(3)
exp{µ (t12 +t13)
2 } =ϕ (t23,t 13)−1 exp{µt 13
2 }ϕ (t12,t 13) exp{µt 12
2 }ϕ (t12,t 23)−1.
Actually this µ is equal to ±(24c2(ϕ ))
1
2 .
It should be noted that we need to use an (actually quadratic) extension of a
ﬁeld k in order to obtain the hexagon equations from the pentagon eq uation. The
associator set M is the pro-algebraic variety whose set of k-valued points consists
of pairs ( µ,ϕ ) satisfying (1), (2) and (3) and M is its open subvariety deﬁned by
µ ⁄= 0. The theorem says that the pentagon equation is essential ly a single deﬁning
equation of the associator set. The Drinfel’d associator Φ KZ ∈ R⟨⟨X,Y ⟩⟩is a
group-like series constructed by solutions of KZ-equation [Dr91]. It satisﬁes (1),
(2) and (3) with µ =±2π√−1. Its coeﬃcients are expressed by multiple zeta values
[LM] (and also [F03]). The theorem also says that the two hexa gon equations do
not provide any new relations under the pentagon equation.
The category of representations of a quasitriangular quasi -Hopf quantized uni-
versal enveloping algebra forms a quasitensored category [ Dr91], in other words,
a braided tensor category [JS]; its associativity constrai nt and its commutativ-
ity constraint are subject to one pentagon axiom and two hexa gon axioms. The
Grothendieck-Teichm¨ uller pro-algebraic groupGT is introduced in [Dr91] as a group
of deformations of the category which change its associativ ity constraint and its
commutativity constraint keeping all three axioms. It is al so conjecturally related
to the motivic Galois group of Z (explained in [A]). Relating to the absolute Galois
group Gal( ¯Q/ Q) of Q its proﬁnite group version ˆGT is discussed in [I, S]. Our
second theorem is on deﬁning equations of GT .
Theorem 2. LetF2(k) be the the free pro-unipotent algebraic group with two vari-
ables x and y. Suppose that its element f = f (x,y ) satisﬁes Drinfel’d’s pentagon
equation:
(4) f (x12,x 23x24)f (x13x23,x 34) = f (x23,x 34)f (x12x13,x 24x34)f (x12,x 23)
in K4(k). Then there exists an element (unique up to signature) λ ∈ ¯k such that
the pair (λ,f ) satisﬁes his hexagon equations (3- and 2-cycle relation):
(5) f (z,x )zmf (y,z )ymf (x,y )xm = 1 with xyz = 1 and m = λ− 1
2 ,
(6) f (x,y )f (y,x ) = 1.
Actually this λ is equal to ±(24c2(f ) + 1)
1
2 wherec2(f ) stands for c2(f (eX,e Y )).
Here K4(k) stands for the unipotent completion of the pure braid group K4 =
ker{B4→ S4} of 4 strings ( B4: the Artin braid group and S4: the symmetric
group) with standard generators xij (1 ⩽ i,j ⩽ 4).
It should be noted again that we need to use an (actually quadr atic) exten-
sion of a ﬁeld k in order to obtain the hexagon equations from the pentagon
PENTAGON AND HEXAGON EQUATIONS 3
equation. The set of pairs ( λ,f ) satisfying (4), (5) and (6) determines a pro-
algebraic variety GT andGT is its open subvariety deﬁned by λ ⁄= 0. The product
structure on GT (k) is given by ( λ 1,f 1)◦ (λ 2,f 2) := ( λ,f ) with λ = λ 1λ 2 and
f (x,y ) = f1(f2xλ 2f −1
2 ,y λ 2)f2. The theorem says that the pentagon equation is
essentially a single deﬁning equation of GT .
The construction of the paper is as follows: §1 is a crucial part of the paper.
The implication of the pentagon equation is proved for Lie se ries. In §2 we give a
proof of theorem 1 by using Drinfel’d’s gadgets. §3 gives a proof of theorem 2 and
its analogue in the pro- l group and pro-nilpotent group setting.
