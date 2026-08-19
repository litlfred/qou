---
doc_id: equations-aux-q-differences
doc_title: "´Equations aux q-diﬀ´erences"
section_id: sec-011-28-l-di-vizio-j-p-ramis-j-sauloy-c-zhang
section_title: "L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG"
section_number: 28
pages: 9-11
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
doc_brief: "Équations aux q-différences — 28 sections: Di Vizio, J-P. Ramis, J. Sauloy ∗,; Introduction; L. DI VIZIO, J.-P. RAMIS, J. SAULO"
---
`a produire des solutions formelles (comme au §4). Sans surprise, dans le cas
fuchsien, ces solutions formelles convergent.
Exemple 3.1.
(1) L’´equation diﬀ´erentielle (1.0.1) est fuch sienne en 0, d’exposant 0 et
l’´equation aux q-diﬀ´erences (1.0.2) est fuchsienne en 0 d’exposant 1 : elles sont
en fait r´eguli`eres en 0. Il en est de mˆeme dans l’exemple 2.1.
(2) Dans l’exemple 2.2, l’´equation diﬀ´erentielle est fuchsienne en 0, d’expo-
sants 0 et 1 − γ et l’´equation aux q-diﬀ´erences est fuchsienne en 0 d’exposants
1e t q/c.O np e u td em ˆeme (par le changement de variablesz =1 /x) constater
qu’elles sont fuchsiennes `a l’inﬁni (exposants respectifs : α, β et a, b).
Lemme 3.2. [Sau00a] Pour un syst`eme fuchsien σqX = AX non r´esonnant,
il existe une unique transformation de jauge formelle tangente `a l’identit´e:
F(x)= In + xF1 + ··· ,
telle que (σqF)−1 AF = A(0). De plus elle est convergente (donc prolongeable
en une matrice m´eromorphe sur C).
L e sc o e ﬃ c i e n t sd el am a t r i c eF(x) sont construits inductivement `ap a r t i r
de la relation AF =( σqF)A(0). Il s’ensuit qu’une matrice Y de rang maximal
v´eriﬁe l’´equation σqY = A(0)Y si et seulement si la matrice X = FY est solu-
tion du syst`eme σqX = AX. Ce lemme permet donc de ramener la r´esolution
des syst`emes fuchsiens `a celle des syst`emes `a coeﬃcients constants. En fait,
associ´e aux consid´erations pr´ec´edentes, il permet facilement de d´emontrer que,
comme pour les ´equations diﬀ´erentielles, tout syst`eme fuchsien est localement
´equivalent `au ns y s t `eme `a coeﬃcients constants.
Nous nous sommes donc ﬁnalement ramen´es `ar ´esoudre un syst`eme aux q-
diﬀerences σqX = AX `a coeﬃcients constants, i.e. tel que A ∈ GLn(C). Pour
ce faire, ´ecrivons A = DU la d´ecomposition de Dunford multiplicative de A,
autrement dit,D est semi-simple, U est unipotente et elles commutent. Il suﬃt,
pour conclure, de con struire deux matrices eq,D et eq,U qui commutent entre
elles et avec D et U et telles que σqeq,D = Deq,D, σqeq,U = Ueq,U :e nf a i t
eq,A = eq,Deq,U est alors une solution de σqX = AX. Le lecteur est invit´e`a
essayer les cas les plus simples dans chaque classe :
(1) Si A = D et n =1 , A est une constante c ∈ C∗ et l’on veut savoir
r´esoudre l’´equation σqf = cf.
(2) Si A = U est unipotente de rang 2, on peut prendre par exemple :
A =
(11
01
)
,
et l’on voit qu’il faut savoir r´esoudre l’´equation σqf = f +1 .
Cela peut se faire `a l’aide de la fonction thˆeta de Jacobi :
θq(x)=
∑
n∈Z
q−n(n−1)/2xn.
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES 29
La fonction θq est donc holomorphe sur C∗. Elle v´eriﬁe de plus l’´equation
fonctionnelle :
θq(qx)= qxθq(x).
Cette ´equation, qui s’´ecrit σqf = qxf, n’est pas fuchsienne : elle a une seule
pente, qui vaut 1. On peut donc consid´erer θq comme l’un des q-analogues de
l’exponentielle, car celle-ci v´eriﬁe l’´equation diﬀ´erentielle δy = xy qui n’est pas
fuchsienne en 0, o`u elle a pour seule pente 1. L’algorithme est maintenant le
suivant :
(1) Soit D = P diag(c1, ··· ,c n)P −1. Pour chaque exposant ci,c ’ e s t - `a-dire
chaque valeur propre de A,l ’ ´equation σqf = cif est fuchsienne, d’exposant ci.
Elle admet pour solution non triviale le « q-caract`ere »
eq,ci (x)= θq(−x)
θq(−c−1
i x).
Son analogue diﬀ´erentiel est la solution xγ de l’´equation diﬀ´erentielle δf = γf
(fuchsienne d’exposant γ):l ad i ﬀ ´erence essentielle ´etant que cette derni`ere
est en g´en´eral ramiﬁ´ee. On obtient une solution de σqX = DX en posant
eq,D = P diag(eq,c1 , ··· ,e q,cn )P −1.O nv ´eriﬁe ais´ement que cette matrice ne
d´epend pas du choix de la diagonalisation de D.
(2) Soit U = In + N (donc N est une matrice nilpotente). On pose eq,U =
Ulq =e x p (lq log(In + N)) (qui est donc un polynˆome en N et en U), o`u lq est
solution de σqf = f + 1. Nous prendrons pour lq le « q-logarithme » :
lq(x)= −xθ′
q(−x)
θq(−x).
Son analogue classique est la solution log x de l’´equation diﬀ´erentielle δf =1 .
Chacune des ´equations σqf − f =1e t δf = 1 est une variante non homog`ene
d’une ´equation lin´eaire d’ordre 2, fuchsienne, d’exposant double 1 (cas d’une
´equation aux q-diﬀ´erences) ou 0 (cas d’une ´equation diﬀ´erentielle).
Les premiers auteurs (Adams, Birkhoﬀ, Carmichael...) utilisaient d’ailleurs
pour q-caract`eres et q-logarithme des fonctions ramiﬁ´ees et pouvaient r´esoudre
le syst`eme `a coeﬃcients constants σqX = AX en posant X = xlogq A,o `u
logq A est une matrice constante telle queqlogq A = A.N o t r em a t r i c eeq,A n’est
pas ramiﬁ´ee, mais elle est m´eromorphe sur C∗ : c’est cette propri´et´e, et plus
pr´ecis´ement le contrˆole de son lieu singulier, qui nous permettra d’obtenir une
bonne caract´erisation du ph´enom`ene de conﬂuence. Pour conclure, revenons au
cas g´en´eral :
Th´eor`eme 3.3. Tout syst`eme σqX = AX fuchsien en 0 admet une solu-
tion X = Meq,A(0) m´eromorphe sur C∗. En particulier, la matrice M est
m´eromorphe sur C et A(0) est une matrice constante non r´esonnante.
Si de plus le syst`eme σqX = AX est non r´esonnant, il y a un choix canonique
de X caract´eris´ep a rA(0) = A(0) et M(0) = In.
SMF – Gazette – 96, Avril 2003
