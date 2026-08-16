---
doc_id: equations-aux-q-differences
doc_title: "´Equations aux q-diﬀ´erences"
section_id: sec-014-33-classiﬁcation-globale
section_title: "Classiﬁcation globale"
section_number: 3.3
pages: 13-15
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
doc_brief: "Équations aux q-différences — 28 sections: Di Vizio, J-P. Ramis, J. Sauloy ∗,; Introduction; L. DI VIZIO, J.-P. RAMIS, J. SAULO"
---
Avant d’´enoncer le r´esultat g´en´eral, revenons `a l’exemple 2.2 des s´eries hyper-
g´eom´etriques et ´etudions le d’un point de vue global, c’est-`a-dire sur la sph`ere
de Riemann S. On constate que l’´equation hyperg´eom´etrique de Gauss
δ2y −~λδy + ~µy =0 , avec



~λ = (α + β)x +( 1 − γ)
1 − x
~µ = αβx
1 − x.
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES 33
y admet pour seules singularit´es 0, 1 et∞ et que ces singularit´es sont r´eguli`eres.
La m´ethode de Frobenius en fournit des syst`emes fondamentaux de solutions
en 0 et en ∞ :
{
2F1(α, β, γ; x)
x1−γ 2F1(α − γ +1 ,β − γ +1 , 2 − γ; x)
{
(1/x)α 2F1(α, α− γ +1 ,α − β +1 ;1/x)
(1/x)β 2F1(β,β − γ +1 ,β − α +1 ;1/x)
On peut de mˆeme en donner une base de solutions explicites en 1, mais nous
n’en aurons pas l’usage. Le prolongement analytique d’un syst`eme fondamental
de solutions au voisinage d’une singularit´e fournit encore un syst`eme fondamen-
tal de solutions et s’exprime donc `a partir d’un autre syst`eme fondamental par
une matrice de constantes : ce sont les fameuses formules de connexion de la
th´eorie classique [In56], [Was65], [WW27]. Par exemple, on peut relier 0 `a l’in-
ﬁni par l’une des matrices suivantes, selon que l’on reste dans le demi-plan de
Poincar´e ou dans son oppos´e:
(3.7.1) ~P
+ =


eiπα Γ(γ)Γ(β − α)
Γ(β)Γ(γ − α) eiπ(α−γ+1) Γ(2 − γ)Γ(β − α)
Γ(1 − α)Γ(1 − γ + β)
eiπβ Γ(γ)Γ(α − β)
Γ(α)Γ(γ − β) eiπ(β−γ+1) Γ(2 − γ)Γ(α − β)
Γ(1 − β)Γ(1 − γ + α)


(3.7.2) ~P − =


e−iπα Γ(γ)Γ(β − α)
Γ(β)Γ(γ − α) e−iπ(α−γ+1) Γ(2 − γ)Γ(β − α)
Γ(1 − α)Γ(1 − γ + β)
e−iπβ Γ(γ)Γ(α − β)
Γ(α)Γ(γ − β) e−iπ(β−γ+1) Γ(2 − γ)Γ(α − β)
Γ(1 − β)Γ(1 − γ + α)


L am a t r i c ed em o n o d r o m i ee nl ep ˆole 1 est (~P+)−1 ~P − : elle repr´esente l’eﬀet sur
le syst`eme fondamental choisi du prolongement analytique le long d’un petit
lacet simple autour de 1 [IKSY91], [Sau00a].
La correspondance de Riemann-Hilbert est n´ ee de la caract´erisation par
Riemann de l’´equation hyperg´eom´etrique `a partir de ses invariants locaux (les
exposants) et des matrices de connexi on [IKSY91]. En termes modernes, on
reconnaˆıt que l’objet classiﬁant est la repr´esentation de monodromie : ceci est
dˆu au fait que les matrices qui interviennent ci-dessus ne d´ependent en fait que
des classes d’homotopie des chemins le long desquels se fait le prolongement
analytique. Ces chemins doivent ´eviter les singularit´es et l’on obtient ici une
repr´esentation du groupe fondamental de la droite projective moins trois points
(donc d’un groupe libre `ad e u xg ´en´erateurs), objet c´el`ebre dans de nombreux
domaines ! Dans l’exemple ci-dessus, la classe du petit lacet simple autour de
1 a pour image (dans cette repr´ esentation) ( ~P+)−1 ~P −. Nous allons tenter,
suivant Birkhoﬀ [Bir13], d’adapter cette d´emarche au cas des ´equations aux
q-diﬀ´erences.
Supposons donc maintenant le syst`eme (2.3.1) fuchsien en 0 et en ∞ (ceci,
relativement `al av a r i a b l ew =1 /x). On d´emontre qu’`a´equivalence rationnelle
SMF – Gazette – 96, Avril 2003
34 L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
pr`es, on peut supposer A(0),A(∞) ∈ GLn(C). On peut alors d´eﬁnir des solu-
tions locales en 0 et en∞ comme ci-dessus, respectivement m´eromorphes sur C
et surS/integerdivide{0} (sph`ere de Riemann priv´ee de l’origine), soientX(0) = M(0)eq,A(0)
et X(∞) = M(∞)eq,A(∞) . Ces solutions sont reli´ees par la matrice de connexion
de Birkhoﬀ :
P =
(
X(∞)
)−1
X(0),
qui est m´eromorphe sur C∗ et σq-invariante. On peut donc la consid´erer comme
une matrice (inversible) de fonctions elliptiques ( « q-sigma periodic » dans la
terminologie de Birkhoﬀ). Elle joue ici le rˆ ole des matrices de monodromie
dans la th´eorie de Riemann-Hilbert, mais il faut prendre garde qu’elle n’est pas
`a coeﬃcients complexes ! C’est l’une des diﬃcult´es et l’un des charmes de la
th´eorie.
Reprenons l’exemple 2.2. Pour l’´equation hyperg´eom´etrique basique
σ2
q f − λσqf + µf =0 a v e c



λ = (a + b)x − (1 +c/q)
abx − c/q ,
µ = x − 1
abx − c/q,
en se basant sur les formules de connexion de Barnes-Mellin-Watson ( voir
[GR90] p. 106), on calcule explicitement la matrice de Birkhoﬀ [Sau00a] :
(3.7.3) P =( D(∞))−1MD(0),
o`u
D(0) =
(10
0 eq,q/c(x)
)
,D (∞) =
(eq,a(1/x)0
0 eq,b(1/x)
)
et
M =


2Φ1
(c
b,a ; c; q,q
)Θq
(bx
cq
)
Θq
(abx
cq
) 2Φ1(q
b, aq
c ; q2
c ; q,q )
Θq
(bx
q2
)
Θq
(abx
cq
)
2Φ1(c
a,b ; c; q,q )
Θq
(ax
cq
)
Θq
(abx
cq
) 2Φ1(q
a, bq
c ; q2
c ; q,q )
Θq
(ax
q2
)
Θq
(abx
cq
)


De mˆeme que dans la th´eorie de Riemann une ´equation est caract´eris´ee
(`a´equivalence pr`es) par la nature de ses singularit´es et sa repr´esentation de
monodromie, Birkhoﬀ d´emontre que la donn´ee de la matrice de connexionP et
des structures de Jordan du syst`eme en 0 et en ∞ (i.e. des structure de Jordan
de A(0) et de A(∞)), fournit un syst`eme complet d’invariants, et il r´esout le
probl`eme inverse. Une version pr´ecis´ee de ce th´eor`eme est donn´ee dans [Sau00a].
Nous en donnerons plutˆot ici une version intrins`eque, dans l’esprit du th´eor`eme
