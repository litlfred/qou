---
doc_id: aif-2000-50-4-1021-0
doc_title: "Systèmes aux q-différences singuliers réguliers : classification, matrice de connexion et monodromie"
section_id: sec-026-332-étude-globale
section_title: "Étude globale"
section_number: 3.3.2
pages: 31-33
source_pdf: AIF_2000__50_4_1021_0.pdf
source_sha256: a7ca398590a266d8
toc_source: inferred
doc_brief: "Systèmes aux q-différences singuliers réguliers : classification, matrice de connexion et monodromie — 41 sections: Front matter; Comportement de la matrice de conn; Introduction et notations"
---
3.3.2. Étude globale.
0
On va maintenant sortir du disque -D(0,r) le long de segments de
spirales de la forme % ' qui ne rencontrent pas les pôles zi. On suppose
dorénavant que B converge vers B uniformément sur tout tel segment (c'est
par exemple le cas si la convergence est uniforme sur tout compact de ^o).
ANNALES DE L'INSTITUT FOURIER
SYSTÈMES AUX ^-DIFFÉRENCES SINGULIERS RÉGULIERS 
1051
Fixons un point z\ ç SÎQ où l'on veut démontrer que X —> X.
—\ 
°
Pour un certain A > 0, et un certain a > 0, ZQ = q^ z\ € D(0,r) et
r— 
• i 
°
q^°° 
ZQ C D(0,r) (c'en est un compact). On passe aux variables réelles
en posant z = q^Zo et Y^(t) = X(z), Y(t) = X(z). Notre but est donc de
démontrer que Y(,(\) —> Y (A).
On note Ce(t) = ( q - l ) / e B ( z ) et C(t) = -2mB(z). Ainsi, Ce
converge uniformément vers C sur [0 ; A].
On peut maintenant traduire le système différentiel Y1 (y) = C(t)Y(t)
et le système aux ^-différences YçÇt+e) = (In -\-eC e(t))Y^(t). Nous n'aurons
pas besoin des conditions initiales. La proposition ci-dessus implique
que Yç(t) converge vers Y(t) uniformément sur [0 ; a].
On invoquera maintenant la méthode d'Euler pour la résolution
approchée d'équations différentielles linéaires (vectorielles, d'ordre 1), dans
sa version multiplicative et à pas non constant. Faute d'une référence
exactement appropriée à nos besoins, nous invoquerons [18] (problème
d'analyse, III.5 et IV.l).
THÉORÈME. — Soit A e C( }a ; &[, Mn(C)) et soient to < ti dans }a ; b[.
On se donne^ pour p entier > 1, une subdivision
fo=^)<^)<...<4^<^)=^
de diamètre e? := maxo<i<p-i A^^ (012 note A^^ = s^\ — s' ). On
suppose que linip-^oo ^p = 0- AJors, la résolvante du système différentiel
^ ' = ^[^ est donnée par la formule :
UÇt^to) = ^{In + ^(^A^i) • • • {In + A^AS^).
Appliquons ce théorème pour calculer la résolvante U(\, u) du système
différentiel Y ' = CY : nous aurons donc V(A) = U(\0)Y{0). On subdivise
[0 ; A] avec le pas ve puis 7V fois le pas e, où N = E( ^ ) et v = A/e — N. On
trouve :
U(\ 0) = lim (In + eC(\ - e)) • • • (in + eC(\ - Ne)) (in + ^G(O)).
Mais nous voulons utiliser C et non C. Nous remplacerons donc [18], III.6
par une version améliorée que l'on déduit du
TOME 50 (2000), FASCICULE 4
1052 
JACQUES SAULOY
LEMME. — Soient Ai,..., Am, ^i,..., Em des éléments de Mn(C) et
notons A'i = Ai + fa,..., A^ = A^ + Em. Alors
||(J,+Ai)...(J,+A^)-(J,+A'i)...(J,+A^)||
m 
m
<(^||^|l)exp(^(||A,||+H^ID).
î=l 
i=l
COROLLAIRE. — Soient (Ap^) et (Bp^) deux familles de matrices
indexées par des couples d'entiers (p,i) tels que 1 ^ i < p. On
considère les suites de terme général Up = (In + Ap^) • • • (In + Ap^p) et
Vp = (In + Bp^) ' • • (In + -Bp^). Oïl suppose que, lorsque p —^ oo :
(i) Ja suite de terme général Ei<î<p 11^^11 est bornée',
(ii) Ja suite de terme général ^i<,<p ||Ap^ - Bp^\\ converge vers 0.
AJors limp-^ ||[7p - VpH = 0.
Nous utiliserons ce corollaire avec pour matrices Ap^ et Bp^ les valeurs
respectives de C et C aux points de la subdivision introduite plus haut.
La preuve du lemme est immédiate, ainsi que celles du corollaire et du fait
que les conditions de celui-ci sont remplies dans notre situation. On conclut
donc que Yç{\) —> V(A), ce qui achève la preuve. 
D
