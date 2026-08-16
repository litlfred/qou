---
doc_id: equations-aux-q-differences
doc_title: "´Equations aux q-diﬀ´erences"
section_id: sec-002-22-l-di-vizio-j-p-ramis-j-sauloy-c-zhang
section_title: "L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG"
section_number: 22
pages: 3-5
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
doc_brief: "Équations aux q-différences — 28 sections: Di Vizio, J-P. Ramis, J. Sauloy ∗,; Introduction; L. DI VIZIO, J.-P. RAMIS, J. SAULO"
---
peut aussi remarquer que l’´equation fonctionnelle (1.0.2), r´e´ecrite en utilisant
l’op´erateur δq, tend vers l’´equation (1.0.1) lorsque q → 1 (toujours avec a =
qα). Le lien g´en´eral entre ces deux « conﬂuences » (des ´equations et de leurs
solutions) sera explicit´ep l u sl o i n .
∗∗∗
Reprenons notre bref historique. Apr`es Jacobi, on retrouve les ´equations aux
q-diﬀ´erences chez Poincar´e et Picard, puis Ramanujan (cf. en particulier leLost
Notebook), G. Watson... puis un peu plus tard (et apparemment dans le cadre de
motivations assez diﬀ´erentes) chez G. Birkhoﬀ et certains de ses ´el`eves. On aura
une bonne id´ee de l’histoire du sujet, de son int´erˆet et de l’ampleur du travail
qu’il a suscit´ea uc o u r sd e ss i `ecles en feuilletant la consid´erable bibliographie de
[GR90]. Ceci ´etant, il est clair que ce th`eme a ´et´e largement oubli´ee tap r e s q u e
totalement disparu du courant dominant des math´ematiques pendant un bon
demi-si`ecle apr`es la ﬁn des ann´ees quarante.
La situation a commenc´e`a changer il y a environ dix ans et apparemment
pour des raisons tr`es vari´ees, dans le cadre de divers courants de recherche
´emergents (ou r´e´emergents...) :
– q-combinatoire, q-analogues des polynˆomes orthogonaux;
–p h ´enom`enes al´eatoires discrets ;
– groupes quantiques, repr´esentations;
– physique th´eorique (travaux de Baxter, discr´etisations, d´eformations...);
–a r i t h m ´etique (q-identit´es, transcendance, exponentielles en caract´eristique
positive);
.........
Il y a ainsi aujourd’hui un foisonnement impressionnant de travaux en
math´ematique et physique faisant intervenir des ´equations aux q-diﬀ´erences
(souvent `a plusieurs variables et parfois non lin´ eaires). Il est donc assez
paradoxal de constater que le sujet manquait jusqu’` a une date tr`es r´ecente
de fondations solides, mˆeme dans le cas le plus simple des ´equations lin´eaires
ordinaires. Ceci est en fait similaire ` ac eq u is ’ e s tp a s s ´ep o u rl e s´equations
diﬀ´erentielles ordinaires au xxe si`ecle : entre la ﬁn des ann´ ees quarante et
le d´ebut des ann´ees soixante-dix le sujet fut consid´ er´e comme clos et sans
grand int´erˆet autre qu’historique (cf. par exemple sa « densit´e bourbachique »
presque nulle). La th´eorie des ´equations diﬀ´erentielles ordinaires analytiques
a´et´e d’abord renouvel´ee par la « red´ecouverte » des ´equations du type de
Fuchs, puis par celle des ´equations `a singularit´es irr´eguli`eres et de tous les
probl`emes diﬃciles et non r´ esolus qu’elles posaient. Un retour ` ad e si d ´ees
essentielles de Birkhoﬀ (en particulier ` a son article de 1913 sur le c´ el`ebre
probl`eme de Riemann-Hilbert [Bir13]) a jou´eu nr ˆole central dans les progr`es
tr`es importants faits `al aﬁ nd u xxe si`ecle sur le sujet. Pour les ´ equations
aux q-diﬀ´erences l’histoire se r´ep`ete avec quelque retard. L`a aussi le retour `a
Birkhoﬀ a jou´eu nr ˆole essentiel. Nous nous proposons d’expliquer dans cet
article comment la r´ecente r´esolution compl`ete d’une s´erie de questions pos´ees
par G. Birkhoﬀ en 1941 (peu avant sa mort) fournit une base raisonnable pour
la th´eorie des ´equations aux q-diﬀ´erences lin´eaires analytiques et ouvre une
s´erie d’interrogations que nous trouvons assez passionnantes vers la th´ eorie
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES 23
de Galois, l’arithm´etique, la g´eom´etrie non-commutative... Nous voudrions en
particulier convaincre le lecteur qu’au del`a de formules que l’on peut trouver
un peu d´ecourageantes (faute d’avoir le talent de Ramanujan ou des outils
performants de calcul formel [Chy98]) se dessine une assez jolie g´ eom´etrie
nouvelle greﬀ´ee sur la g´eom´etrie alg´ebrique classique.
Up to the present time, the theory of linearq-diﬀerence equa-
tions has lagged noticeably behind the sister theories of linear
diﬀerence and diﬀerential equations. In the opinion of the au-
thors, the use of the canonical system, as formulated above in
a special case, is destined to carry the theory of q-diﬀerence
equations to a comparable degree of completeness. This pro-
gram includes in particularthe complete theory of convergence
and divergence of formal series, the explicit determination of
the essential transcendental invariants (constants in the cano-
nical form), the inverse Riemann theory both for the neighbo-
rhood of x = ∞ and in the complete plane (case of rational
coeﬃcients), explicit integral representation of the solutions,
and ﬁnally the deﬁnition of q-sigma periodic matrices, so far
deﬁned essentially only in the case n = 1. Because of its ex-
tensiveness this material cannot be presented here.
G.D. Birkhoﬀ et P.E. Guenther, 1941
Au del`a de l’ach`evement de ce programme, pour |q| ⁄= 1, se posent de nom-
breuses questions naturelles. En voici deux :
– Quelle est la relation entre les invariants alg´ebriques et transcendants « de
Birkhoﬀ » (invariants locaux, matrice de connection de Birkhoﬀ, q-Stokes) et
la th´eorie de Galois aux q-diﬀ´erences ([vdPS97]) ? (Rappelons que dans le cas
diﬀ´erentiel la question est totalement ´elucid´ee : caract`ere galoisien de la mo-
nodromie et des multiplicateurs de Stokes, th´ eor`emes de Zariski-densit´ed e
Schlesinger et Ramis [Ram93].)
– Y a-t-il conﬂuence des q-invariants vers les invariants diﬀ´erentiels quand on
« passe `a la limite continue » pour q → 1 dans des conditions raisonnables.
Ces deux probl`emes sont compl`etement r´esolus dans le cas fuchsien. (Notons
par exemple que dans ce cas la q-monodromie locale en 0 ou ∞ s’interpr`ete `a
l’aide d’un ﬁbr´e plat sur la courbe elliptique C
∗/qZ [Sau02c].) La th´eorie reste
incompl`ete dans le cas irr´egulier.
∗∗∗
Dans la derni`ere partie de cet article, nous changeons de point de vue
et dirigeons notre attention vers des probl` emes de nature arithm´ etique.
L’´etude arithm´etique des s´eries solutions d’´equations aux q-diﬀ´erences n’est
pas compl`etement nouvelle; cependant, nous ne disposons pas d’une th´ eorie
syst´ematique. La question a ´ et´es o u l e v ´ee r´ecemment par Y. Andr´ ed a n s
[And00a], [And00b], o`u plusieurs questions dans cette directionr e s t e n ts a n s
r´eponse. Les r´esultats dont nous parlerons au §5 signiﬁent qu’un analogue na¨ıf
de la th´eorie diﬀ´erentielle ne donne que des objets triviaux. En autres termes,
une th´eorie arithm´etique des ´equations aux q-diﬀ´erence ne peut ˆetre un simple
SMF – Gazette – 96, Avril 2003
