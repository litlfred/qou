---
doc_id: equations-aux-q-differences
doc_title: "´Equations aux q-diﬀ´erences"
section_id: sec-019-41-quelques-generalites
section_title: "Quelques g´en´eralit´es"
section_number: 4.1
pages: 19-21
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
doc_brief: "Équations aux q-différences — 28 sections: Di Vizio, J-P. Ramis, J. Sauloy ∗,; Introduction; L. DI VIZIO, J.-P. RAMIS, J. SAULO"
---
Dans la th´eorie des ´equations diﬀ´erentielles lin´eaires dans le champ com-
plexe, il y a des s´ eries formelles divergentes qui sont solutions formelles.
L’exemple « mod`ele » est la (variante de) s´erie d’Euler :
(4.0.1) ˆy(x)=
∑
n≥0
n! xn+1.
Elle est solution formelle de l’´equation :
(4.0.2) x2y′− y = −x
Le type de divergence d’une solution formelle ˆy(x)= ∑
n≥0 anxn d’une
´equation diﬀ´erentielle analytique (lin´eaire ou non) n’est pas du tout arbitraire;
il est Gevrey : | an |≤ Ann!s ; A> 0,s ≥ 0. (C’est un r´esultat de Maillet 1904,
pr´ecis´e plus tard par Ramis et Malgrange, [Ram93].)
Les ´equations lin´eaires aux q-diﬀ´erences admettent aussi des solutions s´eries
formelles divergentes. Par exemple, la s´erie de Tschakaloﬀ (qui est, rappelons
le, un q-analogue de la s´erie d’Euler (4.0.1)) :
(4.0.3) ˆy(x)=
∑
n≥0
qn(n−1)/2xn
est de rayon de convergence nul (car |q| > 1), et elle v´eriﬁe formellement
l’´equation fonctionnelle
(4.0.4) xy(qx) − y(x)= −1.
La suite {qn(n−1)/2}n≥0 augmente beaucoup plus vite qu’une suite Gevrey de
la forme {Ann!s}n≥0, quelles que soient les constantes positivesA et s choisies.
Autrement dit, la s´erie ˆy d´eﬁnie par (4.0.3) n’appartient `a aucun espace de
s´eries enti`eres Gevrey habituel. On est alors conduit `a une nouvelle famille de
s´eries enti`eres divergentes, que, depuis [B´ez92] et [Ram93], on a baptis´ee famille
des s´eries q-Gevrey.
D´eﬁnition 4.1. ´Etant donn´e s ≥ 0, on dit qu’une s´erie enti`ere ∑
n≥0 anxn est
q-Gevrey d’ordre s si ∑
n≥0
anq−sn(n−1)/2xn
admet un rayon de convergence non nul. On notera C[[x]]q;s l’ensemble des
s´eries q-Gevrey d’ordre s.
Toute solution s´erie formelle d’une ´equation aux q-diﬀ´erences lin´eaire analy-
tique est q-Gevrey d’ordre s pour un s optimal rationnel convenable [B´ez92]. La
situation est ainsi analogue `a celle du cas diﬀ´erentiel et il est alors raisonnable
de se poser le probl`eme de la (multi)sommabilit´ed ec e ss o l u t i o n ss ´eries for-
melles puisqu’il est r´esolu dans le cas diﬀ´erentiel [Ram93]. Nous allons donner
une id´ee de la (ou plutˆot des) solution(s) de ce probl`eme.
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES 39
Dans le cas diﬀ´erentiel les th´eories de la k-sommabilit´ee tp l u sg ´en´eralement
de la multisommabilit´es o n to r c h e s t r ´ees par les transformations de Borel et
Laplace.
D´eﬁnition 4.2. Si ˆf = ∑
n≥1 anxn, on appelera transform´ee de Borel formelle
(d’ordre un) de ˆf la s´erie enti`ere
ˆBˆf =
∑
n≥1
an
(n − 1)!ξn−1.
Exemple 4.3. Si ˆy est la s´erie d’Euler, on a ˆBˆy = 1
1 − ξ.
Si l’on veut une version q-analogue de la m´ethode de sommation de Borel-
Laplace, il est raisonnable de commencer par la transform´ee deq-Borel formelle
mod`ele suivante ([Ram93], p. 22).
D´eﬁnition 4.4. Si ˆf = ∑
n≥0 anxn, on appeleratransform´ee de q-Borel formelle
(d’ordre un) de ˆf la s´erie enti`ere
ˆBq;1 ˆf =
∑
n≥0
anq−n(n−1)/2ξn.
Exemple 4.5.
(1) Si ˆy est la s´erie de Tschakaloﬀ, on a ˆBq;1ˆy = 1
1−ξ .
(2) Si ˆf = ∑
n≥0
xn
(q−1;q−1)n
,o na ˆBq;1 ˆf =( ξ; q−1)∞ et c’est le d´eveloppement
d’une fonction enti`ere.
Dans le reste de ce paragraphe, nous allons d’abord examiner la sommabilit´e
de la s´erie (4.0.3), consid´erant cette derni`ere comme un q-analogue de la s´erie
d’Euler (4.0.1). En r´esolvant l’´equation (4.0.4) par vari ation des constantes,
nous arriverons `a (au moins) deux int´egrales de q-Laplace diﬀ´erentes. Cette
« souplesse » est li´ee au caract`ere suivant de l’op´erateur aux q-diﬀ´erences σq :
le corps de ses constantes (i.e. des fonctions invariantes par l’op´erateur de
dilatation σq),n ’ e s tp a sC, contrairement `a ce qui se passe pour la d´erivation
usuelle d
dx . L’ambigu¨ıt´e des processus de q-sommation est reli´ee `a la taille des
corps de q-constantes. Le choix judicieux esquiss´e`a la ﬁn de ce paragraphe nous
ap e r m i sd er ´eduire cette ambigu¨ıt´e au corps des fonctions elliptiques de Eq.
(On comparera avec la d´emarche d´ecrite au paragraphe pr´ec´edent pour obtenir
une matrice de Birkhoﬀ `a coeﬃcients elliptiques.)
Nous passerons ensuite `al ’ ´etude de la sommabilit´ed uc a r r ´e ˆy2 de la s´erie
(4.0.3). L`au np h ´enom`ene nouveau apparaˆıt : ˆy2 n’a pas le mˆeme ordre de
sommabilit´eq u el as ´erie initiale ˆy. On verra que ce d´ efaut de sommabilit´e
pour la multiplication est essentiellement dˆua uf a i tq u eσq(fg)
fg = σqf
f × σqg
g ,
par opposition `al ’ ´egalit´e (fg)′
fg = f ′
f + g′
g dans le cas de la d´erivation usuelle
′= d
dx . Nous terminerons ce paragraphe par une description tr`es sommaire de
la multisommabilit´e des solutions formelles d’une ´equation lin´eaire analytique
aux q-diﬀ´erences.
SMF – Gazette – 96, Avril 2003
40 L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
4.2. ´E t u d ed el ’ ´equation xy(qx) − y(x)= −1
Comme nous venons de le remarquer, la formule de Leibniz est remplac´ee par
la relation (fg)(qx)= f(qx)g(qx). On va appliquer la m´ethode de la variation
des constantes. Soit λ ∈ C∗ et soit yλ une solution de l’´equation xy(qx) −
λy(x)=0;s i y(x)= yλ(x)C(x), l’´equation (4.0.2) devient
(4.5.1) λC(qx) − C(x)= − 1
yλ(x).
Nous allons regarder les cas suivants : λ =1e t y1 = q−(logq x)(logq x−1)/2
(cf. 4.6); λ ⁄∈ qZ et yλ = 1
θq(λ/x) (cf. 4.8).
4.6. Cas o`u λ =1 et y1 = q−(logq x)(logq x−1)/2.
Si t =l o gq x et z(t)= C(qt), l’´equation (4.5.1) donne celle-ci :
(4.6.1) z(t +1 ) − z(t)= −q−t(t−1)/2,
qui se r´esout par transformation de Fourier. En eﬀet, avec la relation F(z(t +
1)) = eχFz,o na
(eχ − 1)Fz(χ)= −Fq−t(t−1)/2(χ),
ce qui correspond, par transformation de Fourier inverse, aux solutions zα de
(4.6.1) :
zα(t)= 1
√
2π log q
∫+∞+iα
−∞+iα
q− 1
