---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-005-5-motivic-gaussbonnet
section_title: "Motivic Gauss–Bonnet"
section_number: 5
pages: 26-27
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
toc_source: inferred
doc_brief: "Motivic Gauss–Bonnet formulas — 12 sections: Front matter; Introduction; X+ ∈SH(k) is dualizable. In partic"
---
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
