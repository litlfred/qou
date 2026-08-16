---
doc_id: equations-aux-q-differences
doc_title: "´Equations aux q-diﬀ´erences"
section_id: sec-013-32-conﬂuence-des-solutions-locales
section_title: "Conﬂuence des solutions locales"
section_number: 3.2
pages: 12-13
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
doc_brief: "Équations aux q-différences — 28 sections: Di Vizio, J-P. Ramis, J. Sauloy ∗,; Introduction; L. DI VIZIO, J.-P. RAMIS, J. SAULO"
---
Nous voudrions donner un sens `a l’id´ee que, « lorsque q → 1, la q-d´erivation
δq = σq −1
q−1 tend vers la d´erivation δ = x d
dx ». Cette id´ee a ´et´e la source,
depuis Heine, de nombreuses q-analogies. Nous consid´ererons donc une famille
de syst`emes
σqX = AqX,
o`u les coeﬃcients de Aq d´ependent de q. Pour respecter l’analogie, on peut
r´e´ecrire ces syst`emes `a l’aide de l’op´erateur δq :
δqX = BqX, avec Bq = Aq − In
q − 1 ,
ce qui nous conduit `a supposer que Bq tend vers la matrice ~B d´eﬁnissant le
syst`eme diﬀ´erentiel
x d
dxX = ~BX.
Si l’on suppose ce dernier fuchsien non r´ esonnant en 0 (au sens expliqu´ e
pr´ec´edemment), il en est de mˆeme de Aq pour q a s s e zp r o c h ed e1 .I lyaa l o r s
une solution canonique Xq = Mqeq,Aq(0) du syst`eme (2.3.1) et une solution
canonique ~X = ~M(−x) eB(0) du syst`eme diﬀ´erentiel, cette derni`ere ´etant fournie
par la th´eorie de Fuchs-Frobenius2.
Lorsque q varie, le comportement num´erique des solutions est « chaotique »
au voisinage de leurs lieux singuliers. Pour assurer la convergence de Xq vers
~X sur un domaine raisonnable lorsque q tend vers 1, nous nous laisserons donc
guider par la g´eom´etrie des singularit´es. La convergence deBq entraˆıne que les
exposants de Aq tendent vers 1. Nous supposerons que q tend vers 1 le long
d’une q0-spirale continue
qR
0 = e−2ıπτ0R,o `u q0 = e−2ıπτ0 ,I m (τ0) > 0;
autrement dit, q = e−2ıπτ et τ = τ0ε, ε → 0+. Ainsi les lieux singuliers des
eq,Aq(0) se condensent en qR
0 . Nous supposerons de plus que les singularit´es de
Aq (et donc de Bq) tendent vers les pˆoles x1,x2,... de ~B,d es o r t eq u el e sl i e u x
singuliers des Mq se condensent en des demi-spirales continues xiqR+
0 .S o i t
U0 = C∗ /integerdivide
(⋃
xiqR+
0
)
/integerdivideqR
0
l’ouvert compl´ementaire dans C∗ de la r´eunion de toutes ces demi-spirales et
spirales continues.
2 La d´etermination de log( −x) utilis´ee ici est celle qui s’annule en −1 et dont la coupure
est la spirale continue qR
0 introduite plus bas.
SMF – Gazette – 96, Avril 2003
32 L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
Th´eor`eme 3.6. [Sau00a] On suppose que Bq → ~B uniform´ement sur tout
compact de U0. On suppose, de plus, que « la structure de Jordan en 0 varie
continˆument », autrement dit, qu’une matrice de passage de Bq(0) `as af o r m e
de Jordan converge vers une matrice de passage de~B(0) `a sa forme de Jordan.
Alors la solution canoniqueXq converge vers ~X uniform´ement sur tout compact
de U0.
Pour le prouver, on ´etudie s´epar´ement les composantes Mq et eq,Aq(0) de la
solution canonique Xq.L ap r e m i `ere est solution de l’´equation aux q-diﬀ´erences
σqMq = AqMq (Aq(0))−1 ,
avec condition initiale Mq(0) = In. C’est essentiellement la m´ethode d’Euler
d’int´egration num´erique d’une ´equation diﬀ´erentielle (ici, avec pas g´eom´etrique)
qui garantit sa convergence vers la solution~M.P o u rl ad e u x i `eme composante,
on utilise des formules asymptotiques :
lim
ε→0+
eq,qγ (x)=( −x)γ, lim
ε→0+
(q − 1)lq(x) = log(−x).
C e sf o r m u l e ss ep r o u v e n te n´etudiant le comportement de θq lorsque q → 1, `a
l’aide de l’´equation fonctionnelle satisfaite par
Θ(τ,z )= θe−2ıπτ (e2ıπz),
qui relie Θ(−1/τ, z/τ)`aΘ (τ,z )[ L a n 8 7 ] ,[ M u m 8 2 ]:
Θ(τ,z )=
√
i/τ
e(iπ/τ)(z−(τ+1)/2)2 Θ(−1/τ, z/τ).
Sous les hypoth`eses du th´eor`eme, on en tire la convergence de eq,Aq(0) vers
(−x) eB(0). L’importance de la g´eom´etrie des singularit´es (les q-spirales discr`etes
de singularit´es se condensent en des coupures en forme deq0-spirales continues)
j u s t i ﬁ el et e r m ed e« conﬂuence » appliqu´e`a cette situation.
Exemple 3.7.
Tous les exemples pr´ec´edents rentrent dans le cadre de ce th´eor`eme, qui per-
met ainsi d’expliquer et de pr´eciser de nombreuses formules « bien connues ».
L’exemple de la s´erie binomiale (cf. (1.0.1) et (1.0.2)) est trait´e dans [Sau00b],
l’exemple 2.2 est d´etaill´e dans [Sau00a]. 2
