---
doc_id: equations-aux-q-differences
doc_title: "´Equations aux q-diﬀ´erences"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
doc_brief: "Équations aux q-différences — 28 sections: Di Vizio, J-P. Ramis, J. Sauloy ∗,; Introduction; L. DI VIZIO, J.-P. RAMIS, J. SAULO"
---
Une ´equation diﬀ´erentielle ordinaire est une relation G(x; f,...,f (n))=0
entre une fonction inconnuef et ses transform´ees par it´eration de « l’automor-
phisme inﬁnit´esimal » f ↦→ d
dx f.D ef a ¸c o na n a l o g u eo np e u ts ’ i n t ´eresser au cas
o`u l’automorphisme inﬁnit´esimal est remplac´ep a ru nv ´eritable automorphisme
ϕ d’un domaine en x. Le cas le plus simple et le seul que nous consid´ererons
ici, est celui o`u x varie dans la sph`e r ed eR i e m a n n( o up l u sg ´en´eralement un
ouvert de celle-ci invariant par ϕ ou un germe de voisinage d’un point ﬁxe
de cet automorphisme) et o`u de plus l’automorphisme ϕ est une homogra-
phie. On obtient alors des ´equations fonctionnelles G(x; f,...,σ nf)=0( o `u
l’on a pos´e σf(x)= f(ϕ(x))). Nous nous int´eresserons uniquement au cas o`u
G(x; y0,...,y n) est analytique en toutes les variables sur un domaine r´eel ou
complexe oup-adique. Nous parlerons alors d’´equations « aux diﬀ´erences » ana-
lytiques. Par conjugaison homographique sur x on se ram`ene imm´ediatement
aux deux cas suivants :
– ϕ(x)= qx,o `u q ∈ C∗ (C est le corps de base) : on a une ´ equation aux
q-diﬀ´erences;
– ϕ(x)= x+ 1 : on a une ´equation aux diﬀ´erences (on dit aussi aux diﬀ´erences
ﬁnies).
Le premier cas correspond `a une homographie ϕ `a deux points ﬁxes distincts,
le second `a une homographie ϕ `a point ﬁxe double. Le cas g´en´erique est donc
le premier et il est raisonnable qu’il soit (bien que moins classique) plus simple
que le second. Nous noterons
σqf(x)= f(qx)e t τεf(x)= f(x + ε).
On retrouve le cas diﬀ´ erentiel par « passage `a la limite continue » ou
« conﬂuence » :
δq = σq − 1
q − 1 −→ x d
dx, lorsque q → 1,
et
∆ε = τε − 1
ε −→ d
dx, lorsque ε → 0.
∗∗∗
∗ Lucia Di Vizio, Jean-Pierre Ramis, Jacques Sauloy, Laboratoire ´Emile Picard, U.F.R.
M.I.G., 118, route de Narbonne, 31062 Toulouse CEDEX 4
† Changgui Zhang, Laboratoire AGAT, U.F.R. de Math´ ematiques Pures et Appliqu´ees,
59655 Villeneuve d’Ascq CEDEX
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES 21
L’´etude des ´equations auxq-diﬀ´erences commence auxviiie si`ecle avec Euler
dans le cadre de probl`emes de d´enombrement en th´eorie des nombres (parti-
tio numerorum). Une ´etape importante est due `a Heine qui introduit les q-
analogues des fonctions hyperg´eom´etriques d’Euler et Gauss : les fonctions
hyperg´eom´etriques basiques qui sont solutions d’´ equations aux q-diﬀ´erences
lin´eaires alg´ebriques du second ordre, analogues des ´ equations diﬀ´erentielles
hyperg´eom´etriques classiques (cf. 2.2). Il faut citer ensuite les travaux de Ja-
cobi : ses fonctions thˆe t ae ts ac ´el`ebre formule du triple produit jouent un rˆole
central dans la th´eorie (cf. §3e t §4).
Consid´erons, par exemple, la s´erie binomiale, que nous ´ecrivons ici en utili-
sant la notation classique des s´eries hyperg´eom´etriques :
1F0(α; −; x)=
def
+∞∑
n=0
(α)n
n! xn,
o`u( α)n = α(α +1 ) ··· (α + n − 1) est le symbole de Pochhammer. Elle est
solution de l’´equation diﬀ´erentielle
(1.0.1) (1 − x)y′− αy =0 ,
ce qui permet de d´emontrer le th´eor`eme binomial :
1F0(α; −; x)=( 1 − x)−α.
Il existe un q-analogue de cette identit´e (Cauchy 1843, Heine, cf. [GR90, 1.3]).
En eﬀet la s´erie 1F0(α; −; x)p e u tˆetre « d´eform´ee » de la fa¸con suivante :
1Φ0(a; −; q,x )=
def
+∞∑
n=0
(a; q)n
(q; q)n
xn,
o`u l’on a pos´e, pour q ∈ C, |q| < 1e t n ∈ N ∪{ ∞ }:
(a; q)n =
n−1∏
i=0
(1 − aqi).
Cette s´erie fait partie de la famille des s´eries hyperg´eom´etriques basiques intro-
duites par Heine. C’est une d´eformation de la pr´ec´edente en ce sens que, si l’on
impose a = qα, alors les coeﬃcients de1Φ0 tendent terme `a terme vers ceux de
1F0 lorsque q → 1. Par ailleurs, elle est solution de l’´equation aux q-diﬀ´erences
(1.0.2) (1 − ax)y(qx) − (1 − x)y(x)=0 ,
tout comme la fonction m´eromorphe d´eﬁnie par
(ax; q)∞
(x; q)∞
=
def
lim
n→∞
(ax; q)n
(x; q)n
,
ce qui permet de d´emontrer le th´eor`eme q-binomial :
1Φ0(a; −; q,x )= (ax; q)∞
(x; q)∞
.
L’id´ee de « d´eformation » peut ˆetre pr´ecis´ee comme suit : pour |x| < 1, la
fonction 1Φ0(a; −; q,x ) tend vers la fonction 1F0(α; −; x)l o r s q u eq → 1. On
SMF – Gazette – 96, Avril 2003
