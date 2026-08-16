---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a ﬁnite set of points(: GalMot ⟳cMot 1 (-−(,E 0)"
section_id: sec-029-the-weight-4-case-euler-complexes
section_title: "The weight 4 case: Euler complexes"
section_number: null
pages: 109-112
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a finite set of points(: GalMot ⟳cMot 1 (-−(,E 0). (1) — On the"
---
Let us show how the map in Theorem 3.13 generalizes those constructed by [GL, G8]. To be consistent with
those sources, we use the motivic language in this section, but the same results hold in the Hodge realization
as well.
The elements\
For torsion points0,1,2 ∈ with0+1+2= 0, elements\(0,1,2) are constructed by [G8] as follows.
For an elliptic curve over a ﬁeld:,p⊂ End a prime over?, andI a nonzerop-torsion point of,
there are elements\(I), which are?-torsion elements in:
∗
I⊗ Z
[
1
?
]
, where:I is the extension generated
by the coordinates ofI. They are identiﬁed with weight-2 elements in the mixed Tate Lie coalgebra Lie∨
MT/:.
The real period of the motive\(I) is− log|\(I)|.
The elements\(0 : 1 : 2) lie in the Bloch group of:, which is identiﬁed with the weight-4 part of
Lie∨
MT/:. We also use the notation\(0,1,2) = \(0 : 0+1 : 0+1+2), which is unambiguous when
0+1+2= 0becausethe \(0 :1 :2) areinvariantundertranslation. Theyarecharacterizedbythefollowing
properties:
(1) The coproduct is given by
X\(0,1,2)=\(0)∧ \(1)+ \(1)∧ \(2)+ \(2)∧ \(0).
101
(2) The real period of\(0 : 1 : 2) is given up to a constant multiple by the averaged Chow dilogarithm
([G7]). The latter can be rewritten as
1
?5
Õ
G∈[?]
„
()
log

50,G

 3C log

51,G

∧3C log

52,G

, (3.21)
where 50,1 is a function on with div50,1 = ?({0}−{1}).
The elements\ and motivic correlators
According to [G9], §10.5.5, for0,1 ∈ [?], the elements\(0−1) are equal up to a constant multiple to
Corav(0,1). There is a version for the depth 2 elements.
Lemma3.15. Let beanellipticcurveoveranumberﬁeld. Then,for 0,1,2 ∈[p]\{0}with0+1+2= 0,
the elements\(0 :1 :2) are equal up to a constant multiple toCorav(0,1,2).
Proof. The coproduct formulas for the\ and the Corav coincide ([G9], Lemma 10.9). It remains to see the
periods are equal. Indeed, we take50,G such thatlog

50,G(I)

= ?
G(0,I), and likewise for1 and2. Then
the formula (3.21) is evidently a constant multiple of the Hodge correlator
1
|[p]|
Õ
G∈[p]
CorH,G(0,1,2),
where CorH,G denotes the Hodge correlator function computed using the Green’s function with base pointG,
as desired. □
The map constructed by [G8], forO= Z[8] or Z[d] is:
\′ : Z[Γ1(p)\ GL2(O)]⊗ Γ1(p) "•
2→ Lie∨
Mot(,[p]),
(U1,U 2)⊗[ E1,E 2]7→ \(U1,U 2,−(U1+U2)),
(U1,U 2)⊗ ([E1]∧[ E2])7→\(U1)∧ \(U2).
Theorem 3.16. The map\′ is a constant multiple of the component of\◦k corresponding to the constant
term of the local system)2.
Proof. Afterunravelingthedeﬁnitions, indegree1, thisisexactlyLemma3.15, whileindegree2itamounts
to showing that
Corav(0,0)∧ Corav(0,1)= 1
|[p]|
Õ
B∈[p]
CorB(0,0)∧ CorB(0,1).
102
ExpandingthesumsandusingthatCor B(G,H)∼ \(G−H)− \(G−B)− \(H−B) (whereweset \(0)= 0),
this simpliﬁes to
Õ
B
\(B)∧ \(1−B)+
Õ
B
\(0−B)∧ \(B)+
Õ
B
\(0−B)∧ \(1−B)= 0.
The three sums are both symmetric and antisymmetric under the involutionsB7→ 1−B, B7→ 0−B, and
B7→0+1−B, respectively, so the sum is 0. □
A slight abuse of notation has taken place:\ maps to grLie∨
sym(,[p]) and \′ to Lie∨
MT(,[p]).
However, there is no discrepancy, as the second shuﬄe relation in weight 4 and depth 2 holds without the
lower-depth correction terms, and so the constant term of\ can be viewed as a map to Lie∨
sym(,[p]), by
the following lemma.
Lemma 3.17. For any elliptic curve and0,1 ∈[p],
Corav(0,1,( 0,0∗(0,0)= 0,
Corav(0,( 0,0∗(0,0∗(0,0)= 0.
Proof. For the ﬁrst equality, recall that
(0,0∗(0,0=− 1
2(l⊗l−l⊗l).
It is easily veriﬁed that the coproduct is 0. For the periods, there are two trees contributing to the integral
expansion of the correlator. For the tree wherel,l are not incident to a common interior vertex, the terms
withl⊗l and withl⊗l sum to 0. The other tree contributes a constant multiple of
Õ
B∈[p]
„


B(I,F)3C
B(F,0)∧ 3C
B(F,1)∧ l(I)∧ l(I)
=
Õ
B∈[p]
„


Ar(B−F)3C
B(F,0)∧ 3C
B(F,1)
=
Õ
B∈[p]
„


Ar(B−F)3C(
Ar(0−F)− 
Ar(B−F))∧ 3C(
Ar(1−F)− 
Ar(B−F)) = 0.
This follows from the distribution relations for the function
Ar, which state that
Õ
B∈[p]−0

Ar(B)= 0.
103
The second equality follows simply from dihedral symmetry. □
