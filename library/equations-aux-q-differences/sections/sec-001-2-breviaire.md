---
doc_id: equations-aux-q-differences
doc_title: "Équations aux q-différences"
section_id: sec-001-2-breviaire
section_title: "Br´eviaire"
section_number: 2
pages: 5-7
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
toc_source: inferred
doc_brief: "Équations aux q-différences — 14 sections: Front matter; Introduction; Br´eviaire"
---
Nous consid´ererons des ´equations aux q-diﬀ´erences lin´eaires d’ordre n :
(2.0.3)
P.f(x) =
def a0(x)f(qnx) + a1(x)f(qn−1x) + · · · + an(x)f(x) = 0,
o`u P d´esigne l’op´erateur aux q-diﬀ´erences
n

i=0
ai σn−i
q
,
que l’on suppose, sans perte de g´en´eralit´e, non d´eg´en´er´e : a0an̸ = 0. Les ai sont
´el´ements d’un anneau de fonctions K : fractions rationnelles sur un corps de co-
eﬃcients C, fonctions analytiques ou m´eromorphes sur un domaine convenable,
voire s´eries de Laurent formelles... et cet anneau est muni de l’automorphisme
σq qui, `a f(x), associe f(qx).
Les ´el´ements σq-invariants de K, i.e. les solutions de l’´equation σqf = f
forment un sous-anneau Kσq, appel´e l’anneau des constantes de K. Lorsque
K est un corps, Kσq en est un sous-corps. Ce sera le cas aux §3 et §4, et l’on
aura alors Kσq = C, le corps des coeﬃcients. Il en est de mˆeme dans les deux
exemples suivants, o`u l’on consid`ere le corps K = C(x).
Exemple 2.1. L’´equation σqf = f, ´equivalente `a l’´equation δqf = 0, est un q-
analogue (et une d´eformation) de l’´equation diﬀ´erentielle x dy
dx = 0 : il s’agit d’un
cas particulier des ´equations (1.0.1) et (1.0.2) obtenu en posant respectivement
α = 0 et a = 1.
Si l’on s’impose (comme nous le ferons aux §3 et §4) de chercher les solutions
dans le corps M(C∗) des fonctions m´eromorphes sur C∗, on obtient pour corps
des constantes le corps M(C∗)σq des fonctions m´eromorphes σq-invariantes;
celui-ci s’identiﬁe naturellement au corps M(Eq) des fonctions m´eromorphes
sur la surface de Riemann Eq = C∗/qZ. Par le choix d’un « logarithme » τ
dans le demi-plan de Poincar´e H, tel que e−2ıπτ = q, la surface Eq s’identiﬁe
`a la courbe elliptique C/ (Z + Zτ). Le corps des constantes de la th´eorie est
un corps de fonctions elliptiques : ce n’est donc pas le corps des coeﬃcients
Kσq = C, contrairement `a ce qui se passe pour les ´equations diﬀ´erentielles. 2
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES
25
Exemple 2.2. Soient a, b, c ∈C∗. La s´erie hyperg´eom´etrique basique :
(2.2.1)
2Φ1(a, b, c; q, x) =

n⩾0
(a; q−1)n(b; q−1)n
(c; q−1)n(q−1; q−1)n
xn
est une s´erie convergente, et elle est solution de l’´equation aux q-diﬀ´erences
lin´eaire rationnelle d’ordre 2 :
(2.2.2)
σ2
qf −λσqf + µf = 0
avec





λ = (a + b)x −(1 + c/q)
abx −c/q
µ =
x −1
abx −c/q
La s´erie 2Φ1 a ´et´e d´eﬁnie par Heine, puis ´etudi´ee par Ramanujan. C’est un q-
analogue (et une d´eformation) de la s´erie hyperg´eom´etrique classique d’Euler-
Gauss :
(2.2.3)
2F1(α, β, γ; x) =

n⩾0
(α)n(β)n
(γ)n(1)n
xn.
On retrouve cette derni`ere par limite continue (ou « conﬂuence ») des coeﬃ-
cients lorsque q →1, avec les contraintes a = qα, b = qβ, c = qγ. On verra
plus loin en quel sens pr´ecis on peut faire conﬂuer l’´equation fonctionnelle
(2.2.2) elle-mˆeme vers une ´equation diﬀ´erentielle. Cependant, en rempla¸cant
σq par 1 + (q −1)δq et en faisant (comme le sugg`ere l’introduction) conﬂuer
δq vers δ = x d
dx, le lecteur retrouvera sans peine l’´equation hyperg´eom´etrique
classique :
(2.2.4)
δ2y −
λδy + 
µy = 0, avec






λ = (α + β)x + (1 −γ)
1 −x

µ = αβx
1 −x.
2
2.3. ´Equations et syst`emes. Comme dans le cas des ´equations diﬀ´erentielles,
l’´equation (2.0.3) permet de d´eﬁnir un syst`eme de rang n :
(2.3.1)
σqX = AX,
o`u A ∈GLn(K) est une matrice inversible de fonctions. Par exemple en posant
X =
 f
σqf

dans (2.2.2), on trouverait le syst`eme de matrice :
A =

0
1
−µ
λ

∈GLn(C(x)).
2.4. Transformation de jauge. Pour un syst`eme diﬀ´erentiel δX = AX, on
sait que toute transformation de jauge lin´eaire inversible X = FY d´eﬁnit un
nouveau syst`eme δY = BY , o`u B = −F −1δF + F −1AF. Un rapide calcul
montre que la mˆeme transformation de jauge ram`ene le syst`eme (2.3.1) au
syst`eme σqY = BY , o`u
(2.4.1)
B = (σqF)−1 AF.
SMF – Gazette – 96, Avril 2003
26
L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
Ceci justiﬁe de d´eﬁnir une relation d’´equivalence entre de tels syst`emes : on
parlera d’´equivalence globale (ou rationnelle) si F est `a coeﬃcients rationnels,
d’´equivalence locale (en 0) si les coeﬃcients de F sont analytiques dans un voi-
sinage de 0, d’´equivalence formelle si les coeﬃcients sont des s´eries de Laurent
formelles. Comme dans la th´eorie des ´equations diﬀ´erentielles, un « lemme du
vecteur cyclique », valable sur un corps de base quelconque, implique que tout
syst`eme (2.3.1) de rang n est ´equivalent `a une ´equation d’ordre n ([Sau00a]
dans le cas complexe, [DV02a] en g´en´eral). On peut donc indiﬀ´eremment par-
ler d’´equivalence (locale ou globale) entre syst`emes ou ´equations.
2.5. Modules aux q-diﬀ´erences. Les solutions du syst`eme (2.3.1) sont
les invariants de l’application X →A−1σqX. C’est l’analogue multiplicatif
de la caract´erisation des solutions du syst`eme diﬀ´erentiel δX = AX comme
´el´ements du noyau d’une connexion X →δX −AX. Dans ce dernier cas, l’objet
alg´ebrique intrins`eque qui mod´elise la situation est le module `a connexion ou
le module diﬀ´erentiel associ´e. Nous sommes ainsi conduits `a d´eﬁnir un module
aux q-diﬀ´erences comme un couple (M, Φ) form´e d’un K-espace vectoriel de
dimension ﬁnie et d’un automorphisme σq-lin´eaire de M ; autrement dit, Φ
v´eriﬁe le q-analogue de la relation de Leibnitz :
∀a ∈K, x ∈M, Φ(ax) = σq(a)Φ(x).
Alternativement, c’est un module `a gauche de longueur ﬁnie sur l’anneau (non-
commutatif) Dq = K

σq, σ−1
q

des op´erateurs aux q-diﬀ´erences. Le syst`eme
(2.3.1) est ainsi mod´elis´e par le module (Kn, ΦA), o`u ΦA(X) = A−1σqX et tout
module est de cette forme modulo le choix d’une base ; de plus, l’´equivalence
entre syst`emes correspond `a l’isomorphisme entre les modules aux q-diﬀ´erences
associ´es. Par exemple, en partant de la matrice constante identit´e A = In, on
obtient un module banal, c’est-`a-dire un module (isomorphe `a) (Kn, Φ) o`u Φ
est d´eﬁnie par l’action de σq composante par composante.
2.6. Prolongement m´eromorphe. Un des buts de la th´eorie est la classi-
ﬁcation locale et globale des ´equations `a coeﬃcients rationnels. Dans le cas
complexe, sous l’hypoth`ese |q|̸ = 1, on peut remarquer que toute matrice F
d’´equivalence locale entre deux tels syst`emes admet automatiquement un pro-
longement m´eromorphe `a C en vertu de l’´equation fonctionnelle (2.4.1) :
F(qx) = A(x)F(x) (B(x))−1 ,
qui permet, it´erativement, d’agrandir le disque de d´eﬁnition de F. Ce
ph´enom`ene de propagation de la m´eromorphie est caract´eristique des ´equations
aux q-diﬀ´erences complexes, mais aussi p-adiques, et est en contraste marqu´e
avec la th´eorie des ´equations diﬀ´erentielles.
