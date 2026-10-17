---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-104-5-motivic-gaussbonnet
section_title: "Motivic Gauss–Bonnet"
section_number: 5
pages: 159-161
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
1825
The triangle commutes by the functoriality of ϑ−, as expressed by Remark 3.16.
To see that square commutes, we have the diagram
61−d+TV −p∗ω−1
Y/Bπ∗
V E ∼/ 61−d+p∗(TY +V −ω−1
Y/B)π∗
V E ∼/ p∗61−d+TY +V −ω−1
Y/Bπ∗
Y E
6r+1−p∗det−1 V π∗
V E
6r
Tϑp∗ω−1
Y/B−TV/B
O
6r+1−p∗det−1 V π∗
V E
∼
/
6r
Tϑp∗(ω−1
Y/B−TY/B−V )
O
p∗6r+1−det−1 V π∗
Y E
p∗6r
Tϑω−1
Y/B−TY/B−V
O
The ﬁrst square commutes using the exact sequence 0 →p∗V →TV/B →p∗TY/B →0 and the second
by the naturality of ϑ−. Applying the adjunction p# ⊣p∗, the identity p#s∗= 6V and applying 6−V to
yield the isomorphism [6V x, y]SH(Y) ≃[x, 6V y]SH(Y), applying HomSH(V )(s∗(1Y), −) to the last map
gives the commutative square
HomSH(V )(s∗(1Y), p∗61−d+TY +V −ω−1
Y/Bπ∗
Y E)
∼
+
HomSH(Y)(1Y, 61−d+TY −ω−1
Y/Bπ∗
Y E)
HomSH(V )(s∗(1Y), p∗6r+1−det−1 V π∗
Y E)
p∗6r
P1ϑω−1
Y/B−TY/B−V ∗
O
∼
+
HomSH(Y)(1Y, 6r+1−V −det−1 V π∗
Y E)
6r−V ϑω−1
Y/B−TY/B−V ∗
O
Applying HomSH(V )(s∗(1Y), −) to the ﬁrst diagram, putting these two diagrams together and using the
isomorphisms (4.5.2) and Remark 4.2 gives the commutativity of the square in (4.5.4).
It follows from the commutativity of (4.5.3) that φ∗◦(s∗)∗◦ρY,Y,ω−1
Y/B = ρY,Y,ω−1
Y/B. The commutativity
of (4.5.1) and (4.5.4) then shows that ρ−V ◦ψ ◦s∗= id. By Remarks 3.15 and 3.16 the map ρ−V ◦ψ
is the inverse of the canonical Thom isomorphism ϑV : E0,0(Y) →E2r,r
0V (V, det−1 V ). Thus s∗= ϑV so
s∗(1E
Y) = thV .
□
Remark 4.6. If we have a GL-orientation on E, we have functorial pushforward maps
f∗: Ea,b
W (Y) →Ea−2d,b−d
Z
(X)
for f : Y →X a projective morphism in SmB, of relative dimension d, with W ⊂Y, Z ⊂X closed subsets
with f (W) ⊂Z. All the results of this section hold in the oriented context after deleting the twist by line
bundles. This follows from Remark 3.18.
1826
Marc Levine and Arpon Raksit
5. Motivic Gauss–Bonnet
Deﬁnition 5.1. Let p : V →X be a rank r vector bundle on some X ∈SmB, and let E ∈SH(B) be an
SL-oriented motivic ring spectrum. The Euler class eE(V ) ∈E2r,r(X, det−1 V ) is deﬁned as
eE(V ) := s∗s∗(1E
X);
1E
X ∈E0,0(X) the unit.
Remark 5.2. By Lemma 4.5, eE(V ):=s∗s∗(1E
X)= ¯s∗thV , where ¯s : X →ThX(V ) is the map induced by s.
Theorem 5.3 (motivic Gauss–Bonnet). Let E ∈SH(B) be an SL-oriented motivic ring spectrum, πX :
X →B a smooth and projective B-scheme, let uE : 1B →E be the unit map. Then
πX/B∗(eE(TX/B)) = uE∗(χ(X/B)) ∈E0,0(B).
Proof. We have the canonical Thom isomorphism
ϑE
−TX/B : Ea,b(X; ωX/B) →Ea−2 dim X,b−dim X(Th(−TX/B)).
By Lemma 2.15, it sufﬁces to show that the map
β∗
X/B : E0,0(X) →E0,0(Th(−TX/B))
sends 1E
X to ϑE
−TX/B(eE(TX/B)); by Remark 5.2, this is the same as ϑ−TX/B(¯s∗thTX/B), where
¯s : X+ →Th(TX/B)
is the map induced by the zero-section s : X →TX/B.
We use our description of βX/B as πX# applied to (2.14.3). Applying HomSH(X)(−, π∗
XE) to βX/B and
using the adjunction HomSH(B)(πX#(−), E) ≃HomSH(X)(−, π∗
XE), we have that β∗
X/B is given by the
composition
E0,0(X)
a
∼
−→HomSH(X)(1X, π∗
XE)
b
∼
−→HomSH(X)(6−TX/B ◦6TX/B(1X), π∗
XE)
c
∼
−→HomSH(X)(ThX(TX/B)), 6TX/Bπ∗
XE) ¯s∗
→HomSH(X)(1X, 6TX/Bπ∗
XE)
≃HomSH(X)(6−TX/B(ThX(TX/B)), π∗
XE)
where the isomorphisms a, b, c are the canonical ones.
The functoriality of the canonical Thom isomorphisms gives us the commutative diagram
E0,0(X)
ϑTX/B
/
a
≀

E2dX,dX(Th(TX/B), ωX/B)
ϑE
−TX/B

HomSH(X)(1X, π∗
XE)
b
≀

HomSH(X)(6−TX/B6TX/B(1X), π∗
XE)
c
∼
/ HomSH(X)(ThX(TX/B), 6TX/Bπ∗
XE)
Motivic Gauss–Bonnet formulas
1827
Thus
(c ◦b ◦a)(1E
X) = ϑE
−TX/B(thTX/B).
Applying ϑE
−TX/B as above gives us the commutative diagram
E2dX,dX(Th(TX/B), ωX/B)
¯s∗
/
ϑE
−TX/B 
E2dX,dX(X, ωX/B)
ϑE
−TX/B

HomSH(X)(ThX(TX/B), 6TX/Bπ∗
XE)
¯s∗
/
≀

HomSH(X)(1X, 6TX/Bπ∗
XE)
≀

HomSH(X)(6−TX/BThX(TX/B), π∗
XE)
6−TX/B (¯s∗)
/ HomSH(X)(6−TX/B(1X), π∗
XE)
and thus
β∗
X/B(1E
X) = ϑ−TX/B(¯s∗(thTX/B)) = ϑ−TX/B(eE(TX/B)),
as desired.
□
