---
doc_id: equations-aux-q-differences
doc_title: "´Equations aux q-diﬀ´erences"
section_id: sec-004-2-breviaire
section_title: "Br´eviaire"
section_number: 2
pages: 5-6
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
doc_brief: "Équations aux q-différences — 28 sections: Di Vizio, J-P. Ramis, J. Sauloy ∗,; Introduction; L. DI VIZIO, J.-P. RAMIS, J. SAULO"
---
Nous consid´ererons des ´equations aux q-diﬀ´erences lin´eaires d’ordre n :
(2.0.3) P.f(x)=
def
a0(x)f(qnx)+ a1(x)f(qn−1x)+ ··· + an(x)f(x)=0 ,
o`u P d´esigne l’op´erateur aux q-diﬀ´erences
n∑
i=0
ai σn−i
q ,
que l’on suppose, sans perte de g´en´eralit´e, non d´eg´en´er´e: a0an ⁄=0 .L e sai sont
´el´ements d’un anneau de fonctionsK : fractions rationnelles sur un corps de co-
eﬃcients C, fonctions analytiques ou m´eromorphes sur un domaine convenable,
voire s´eries de Laurent formelles... et cet anneau est muni de l’automorphisme
σq qui, `a f(x), associe f(qx).
Les ´el´ements σq-invariants de K, i.e. les solutions de l’´equation σqf = f
forment un sous-anneau Kσq ,a p p e l ´el ’anneau des constantes de K.L o r s q u e
K est un corps, Kσq en est un sous-corps. Ce sera le cas aux §3e t §4, et l’on
aura alors Kσq = C, le corps des coeﬃcients. Il en est de mˆeme dans les deux
exemples suivants, o`u l’on consid`ere le corps K = C(x).
Exemple 2.1. L’´equation σqf = f,´equivalente `al ’ ´equation δqf =0 ,e s tu nq-
analogue (et une d´eformation) de l’´equation diﬀ´erentielle xdy
dx =0:i ls ’ a g i td ’ u n
cas particulier des ´equations (1.0.1) et (1.0.2) obtenu en posant respectivement
α =0e t a =1 .
Si l’on s’impose (comme nous le ferons aux§3e t §4) de chercher les solutions
dans le corps M(C∗)d e sf o n c t i o n sm ´eromorphes sur C∗, on obtient pour corps
des constantes le corps M(C∗)σq des fonctions m´eromorphes σq-invariantes ;
celui-ci s’identiﬁe naturellement au corps M(Eq)d e sf o n c t i o n sm ´eromorphes
sur la surface de Riemann Eq = C∗/qZ. Par le choix d’un « logarithme » τ
dans le demi-plan de Poincar´e H,t e lq u ee−2ıπτ = q,l as u r f a c eEq s’identiﬁe
`a la courbe elliptique C/ (Z + Zτ). Le corps des constantes de la th´eorie est
un corps de fonctions elliptiques : ce n’est donc pas le corps des coeﬃcients
Kσq = C, contrairement `a ce qui se passe pour les ´equations diﬀ´erentielles. 2
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES 25
Exemple 2.2. Soient a, b, c∈ C∗.L as ´erie hyperg´eom´etrique basique :
(2.2.1) 2Φ1(a, b, c; q,x )=
∑
n/greaterorequalslant0
(a; q−1)n(b; q−1)n
(c; q−1)n(q−1; q−1)n
xn
est une s´erie convergente, et elle est solution de l’´equation aux q-diﬀ´erences
lin´eaire rationnelle d’ordre 2 :
(2.2.2) σ2
q f − λσqf + µf =0 a v e c



λ = (a + b)x − (1 +c/q)
abx − c/q
µ = x − 1
abx − c/q
La s´erie 2Φ1 a´et´ed ´eﬁnie par Heine, puis ´etudi´ee par Ramanujan. C’est un q-
analogue (et une d´eformation) de la s´erie hyperg´eom´etrique classique d’Euler-
Gauss :
(2.2.3) 2F1(α, β, γ; x)=
∑
n/greaterorequalslant0
(α)n(β)n
(γ)n(1)n
xn.
On retrouve cette derni`ere par limite continue (ou « conﬂuence ») des coeﬃ-
cients lorsque q → 1, avec les contraintes a = qα,b = qβ, c = qγ. On verra
plus loin en quel sens pr´ ecis on peut faire conﬂuer l’´ equation fonctionnelle
(2.2.2) elle-mˆeme vers une ´equation diﬀ´erentielle. Cependant, en rempla¸cant
σq par 1 + (q − 1)δq et en faisant (comme le sugg`ere l’introduction) conﬂuer
δq vers δ = x d
dx , le lecteur retrouvera sans peine l’´equation hyperg´eom´etrique
classique :
(2.2.4) δ2y −~λδy +~µy =0 , avec



~λ = (α + β)x +( 1 − γ)
1 − x
~µ = αβx
1 − x.
2
2.3. ´Equations et syst`emes. Comme dans le cas des ´equations diﬀ´erentielles,
l’´equation (2.0.3) permet de d´eﬁnir un syst`eme de rang n :
(2.3.1) σqX = AX,
o`u A ∈ GLn(K) est une matrice inversible de fonctions. Par exemple en posant
X =
(f
σqf
)
dans (2.2.2), on trouverait le syst`eme de matrice :
A =
(
01
−µλ
)
∈ GLn(C(x)).
