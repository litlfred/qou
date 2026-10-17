---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-023-a1-objets-projectifs-et-injectifs
section_title: "Objets projectifs et injectifs"
section_number: A.1
pages: 119-126
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
---
gorie ab´elienne K-lin´eaire A–Mod des A-modules (`a gauche) poss`ede assez d’in-
jectifs et de projectifs. Pour les projectifs, nous allons retrouver ce fait de mani`ere
constructive.
A.1.1. Lemme. Soit f : M →N un homomorphisme de A-modules. Alors
a) f est un ´epimorphisme si et seulement si f(A) : M(A) →N(A) est un ´epimor-
phisme pour tout A ∈A.
b) f est un monomorphisme si et seulement si f(A) : M(A) →N(A) est un
monomorphisme pour tout A ∈A.
c) f est un isomorphisme si et seulement si f(A) : M(A) →N(A) est un isomor-
phisme pour tout A ∈A.
D´emonstration. a) Soit C = Coker f : on a C(A) = Coker f(A) pour tout A ∈A,
et C = 0 ⇐⇒C(A) = 0 pour tout A ∈A.
b) R´esulte de a) par dualit´e (ou par le mˆeme raisonnement).
c) est clair.
□
A.1.2. Lemme. Pour tout objet A ∈A, le A-module AA est projectif.
D´emonstration. Soit f : M →AA un ´epimorphisme. Par le lemme A.1.1, f(A)
est surjectif. Soit m ∈M(A) tel que f(A)(m) = 1A. Par le lemme de Yoneda
(proposition 1.3.6 a)), m d´eﬁnit un homomorphisme ˜m : AA →M, et on voit tout
de suite que ˜m est une section de f.
□
A.1.3. D´eﬁnition. Un A-module de la forme L AAi est appel´e un A-module libre.
Tout A-module libre est projectif. Si A est K-lin´eaire, tout A-module libre est
de la forme AA pour un objet A convenable.
A.1.4. Proposition. Supposons A petite.
a) Tout A-module M est quotient d’un A-module libre.
b) Un A-module P est projectif si et seulement s’il est facteur direct d’un A-module
libre.
D´emonstration. a) Pour tout objet A ∈A, choisissons un syst`eme g´en´erateur
(mA
i )i∈IA de M(A). Alors l’homomorphisme
M
A∈A
M
i∈IA
AA →M
d´eﬁni par le lemme de Yoneda est un ´epimorphisme par le lemme A.1.1 a).
120
YVES ANDR´E ET BRUNO KAHN
b) La n´ecessit´e r´esulte de a). La sufﬁsance r´esulte du lemme A.1.2, puisqu’un
facteur direct d’un module projectif est ´evidemment projectif.
□
A.1.5. Corollaire. Si P est un A-module projectif, PL : A 7→L ⊗K P(A) est un
AL-module projectif pour toute extension L/K.
D´emonstration. D’apr`es la proposition A.1.4 b), il sufﬁt de le voir pour P de la
forme AA, auquel cas c’est ´evident.
□
A.2. Cat´egories semi-simples. Les d´eﬁnitions suivantes sont adapt´ees de [57].
A.2.1. D´eﬁnition. Soit A une K-cat´egorie.
a) Un objet de A est simple s’il n’est pas nul et s’il n’a pas d’autre sous-objet que
lui-mˆeme et 0.
b) Un objet de A est semi-simple s’il est somme directe d’objets simples.
c) Un objet A de A est artinien si toute chaˆıne d´ecroissante de sous-objets de A est
stationnaire.
d) La cat´egorie A est artinienne si, pour tout A ∈A, AA est un objet artinien de
A-Mod.
e) La cat´egorie A est simple si elle l’est en tant qu’objet de Ae-Mod.
A.2.2. D´eﬁnition. Soit (Aα) une famille de cat´egories ayant les mˆemes objets.
a) Le produit local des Aα est la cat´egorie Qλ
α Aα ayant les mˆemes objets que
les Aα et telle que, pour tout couple d’objets (A, B), on ait (Qλ
α Aα)(A, B) =
Q
α Aα(A, B).
b) A est somme directe locale des Aα si elle est produit local des Aα et que, de plus,
pour tout objet A, l’ensemble des α tels que (Aα)A̸ = 0 est ﬁni.
c) Supposons que les Aα soient des K-cat´egories. Le coproduit des Aα est la K-
cat´egorie A = `
α Aα dont la collection d’objets est la r´eunion des collections
d’objets des Aα, avec
A(A, B) =
(
Aα(A, B)
si ∃α : A, B ∈Aα
0
sinon.
A.2.3. Lemme. Soit A une K-cat´egorie.
a) Toute somme directe d’objets semi-simples est semi-simple.
b) Soit A ∈A un objet tel que tout sous-objet de A soit facteur direct. Alors A est
semi-simple dans les cas suivants :
(i)
A est artinien.
(ii)
A est de la forme R-Mod, o`u R est une K-cat´egorie.
Supposons de plus A ab´elienne.
c) Soit A ∈A un objet semi-simple et soit B un sous-objet de A. Alors il existe une
famille (Si)I∈I de sous-objets simples de A telle que A = B ⊕L
i∈I Si.
d) Tout quotient, tout sous-objet d’un objet semi-simple est semi-simple.
D´emonstration. a) est ´evident. Dans b), supposons d’abord A artinien. Si A n’est
pas semi-simple, soit B un sous-objet de A minimal parmi ceux qui ne sont pas
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
121
semi-simples. Alors B n’est pas simple, donc poss`ede un sous-objet C̸ = 0, B.
Comme C est facteur direct de A, il est facteur direct de B, soit B = C ⊕D. Mais
C et D sont semi-simples, contradiction. L’autre cas se traite comme la sufﬁsance
dans [11, d´em. de la prop. 4.1] (cf. [57, bas p. 140]). c) se d´emontre comme la
n´ecessit´e dans loc. cit. d) r´esulte imm´ediatement de c).
□
A.2.4. Contre-exemple. Soit A la cat´egorie des espaces vectoriels de dimension
d´enombrable sur un corps k, et soit ¯
A la cat´egorie quotient de A par la sous-cat´e-
gorie ´epaisse des espaces vectoriels de dimension ﬁnie. Soit V un espace vectoriel
de dimension inﬁnie, vu comme objet de ¯
A. Alors tout sous-objet de V est facteur
direct, mais V ne contient aucun sous-objet simple.
A.2.5. Lemme. Soit A une cat´egorie ab´elienne. Consid´erons les ´enonc´es suivants :
(1) Tout objet de A est semi-simple.
(2) Tout objet de A est projectif.
(3) Tout objet de A est injectif.
Alors 1 =⇒2 ⇐⇒3. De plus, 1 ⇐⇒2 ⇐⇒3 dans les deux cas suivants :
(i)
Tout objet de A est artinien.
(ii)
A est de la forme R-Mod, o`u R est une K-cat´egorie.
D´emonstration. Il est bien connu que 2 ⇐⇒3, et 1 =⇒2 r´esulte du lemme A.2.3
a). Les implications inverses r´esultent du lemme A.2.3 b).
□
A.2.6. Contre-exemple. Dans la cat´egorie ¯
A du contre-exemple A.2.4, tout objet
est projectif, mais ¯
A ne contient aucun objet simple (cf. [48, p. 324]).
A.2.7. Lemme (cf. [25]). Soit A une petite cat´egorie K-lin´eaire pseudo-ab´elienne
et dont tout objet est semi-simple. Alors A est ab´elienne si et seulement si, pour tout
objet simple S ∈A, l’anneau A(S, S) est un corps.
D´emonstration. La n´ecessit´e r´esulte du lemme de Schur. Sufﬁsance : soit T l’ensem-
ble des types d’objets simples de A, et pour tout t ∈T soit At la sous-cat´egorie
pleine de A form´ee des objets isotypiques de type t. Alors At v´eriﬁe encore l’hy-
poth`ese, et il sufﬁt de montrer que At est ab´elienne. En d’autres termes, on peut
supposer A isotypique. Soit S un objet simple de A, et notons D = A(S, S) son
corps d’endomorphismes. Le foncteur Ao
S s’enrichit en un foncteur T `a valeurs dans
les Do-espaces vectoriels, o`u Do est le corps oppos´e `a D. En utilisant l’hypoth`ese,
on voit tout de suite que T est pleinement ﬁd`ele et d’image essentielle la cat´egorie
des Do-espaces vectoriels de dimension ≤c, o`u c est le plus grand cardinal tel qu’il
existe un ensemble I de cardinal c tel que S(I) ∈A. En particulier, A est ab´elienne.
□
A.2.8. Contre-exemple. Soit Q[ε] l’alg`ebre des nombres duaux (ε2 = 0). La cat´e-
gorie des Q[ε]-modules libres de rang ﬁni est Q-lin´eaire, pseudo-ab´elienne, artini-
enne, et tout objet est semi-simple, mais elle n’est pas ab´elienne.
122
YVES ANDR´E ET BRUNO KAHN
A.2.9. Lemme. Soient A une K-cat´egorie pseudo-ab´elienne, A ∈A et AA =
L
α∈I Mα une d´ecomposition de AA en somme directe de sous-modules non nuls.
Alors I est ﬁni et il existe une unique d´ecomposition en somme directe A = L Aα
telle que, pour tout α, Mα = AAα. Si A est ind´ecomposable, AA est ind´ecomposa-
ble.
D´emonstration. ´Ecrivons IdA = P eα avec eα ∈Mα(A) pour tout α. Alors, pour
tout B ∈A et tout f ∈AA(B) = A(A, B), on a f = P feα. Par cons´equent,
Mα̸ = 0 =⇒eα̸ = 0. Les Mα sont donc en nombre ﬁni. De plus, le lemme de
Peirce montre que les eα forment un syst`eme d’idempotents orthogonaux, d’o`u la
deuxi`eme assertion en utilisant le lemme de Yoneda. La derni`ere assertion en r´esulte
imm´ediatement.
□
Le th´eor`eme qui suit clariﬁe le lien entre diverses notions de semi-simplicit´e, et
montre qu’elles ne d´ependent pas de la K-structure.
A.2.10. Th´eor`eme. Soit A une K-cat´egorie. Les conditions suivantes sont ´equiva-
lentes :
(1) Tout objet de A-Mod est projectif.
(2) Tout objet de A-Mod est injectif.
(3) Tout objet de A-Mod est semi-simple.
(4) Pour tout A ∈A, AA est semi-simple.
(5) A est artinienne et le Ao ⊠K A-module A est semi-simple.
(6) A est ´equivalente au sens de Morita `a une cat´egorie de la forme `
α Dα,
o`u, pour tout α, Dα est un corps gauche.
On dit alors que A est semi-simple (cf. d´eﬁnition 2.1.1).
Si de plus A est K-lin´eaire, les conditions ci-dessus ´equivalent `a :
(7) Pour tout objet A ∈A, l’anneau A(A, A) est semi-simple.
(8) rad(A) = 0 et pour tout A ∈A, A(A, A) est un anneau artinien (`a
gauche).
Enﬁn, si A est en outre pseudo-ab´elienne, les conditions ci-dessus ´equivalent
`a :
(9) A est somme directe locale d’une famille de cat´egories artiniennes simples
(ayant les mˆemes objets).
(10) A est ab´elienne et tout objet de A est semi-simple et de longueur ﬁnie.
(11) A est ab´elienne, artinienne, et tout objet de A est semi-simple.
(12) A est ab´elienne, tout objet de A est de longueur ﬁnie, et rad(A) = 0.
D´emonstration. Il est clair que les six premi`eres conditions ne changent pas si
l’on remplace A par une K-cat´egorie ´equivalente au sens de Morita. De mˆeme
les septi`eme et huiti`eme condition sont v´eriﬁ´ees pour une cat´egorie K-lin´eaire A
si et seulement si elles le sont pour son enveloppe pseudo-ab´elienne A♮: en ef-
fet, pour tout couple d’objets ((A, e), (A′, e′)) de A♮, on a A♮((A, e), (A′, e′)) =
e′A(A, A′)e et rad(A♮)((A, e), (A′, e′)) = e′rad(A)(A, A′)e, cf. aussi lemme
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
123
1.3.10 d). Ceci permet en particulier de supposer dans la suite A K-lin´eaire pseudo-
ab´elienne.
1 ⇐⇒2 ⇐⇒3 r´esulte du lemme A.2.5 ; 3 =⇒4 est ´evident.
4 =⇒3 : soient M un A-module `a gauche, A ∈A et a ∈M(A). Alors
Ann(a)(B) = {f ∈AA(B) | f ∗a = 0} d´eﬁnit un A-id´eal `a gauche de A et l’appli-
cation f 7→f ∗a induit un morphisme de A-modules AA/Ann(a) →M. En faisant
varier A et a, on obtient un ´epimorphisme L
A∈A,a∈M(A) AA/Ann(a) −→
→M.
Il r´esulte alors du lemme A.2.3 que M est semi-simple.
4 =⇒10 : le lemme A.2.9 montre que si S ∈A est simple, alors AS est simple ;
en r´eappliquant ce mˆeme lemme, on voit que tout objet de A est semi-simple et de
longueur ﬁnie.
Enﬁn, pour tout objet simple S ∈A, A(S, S) = A-Mod(AS, AS) est un corps,
donc A est ab´elienne d’apr`es le lemme A.2.7.
10 =⇒11 : si S ∈A est simple, A(S, S) est un corps (lemme de Schur), donc
ne contient aucun id´eal̸ = 0 et AS est simple. Il en r´esulte que AA est de longueur
ﬁnie, donc artinien, pour tout A ∈A.
11 =⇒10 : le lemme de Yoneda implique que tout objet de A est artinien, donc
de longueur ﬁnie.
10 =⇒3 : comme dans la d´emonstration du lemme A.2.7, on se ram`ene au cas
o`u A est isotypique. Soit M un A-module `a gauche. Choisissons un objet simple S
de A, et soit D le corps des endomorphismes de S (voir ci-dessus). Alors D op`ere
naturellement `a gauche sur M(S). Pour tout objet A de A, on a un homomorphisme
naturel
A(S, A) ⊗D M(S) →M(A)
o`u le produit tensoriel sur D est relatif `a l’action `a droite de D sur A(S, A), et
l’hypoth`ese sur A montre que c’est un isomorphisme de groupes ab´eliens. On d´eﬁnit
ainsi une ´equivalence
M 7→M(S)
de A-Mod sur la cat´egorie des D-espaces vectoriels `a gauche, dont tout objet est
´evidemment semi-simple.
6 =⇒10 est ´evident. (3 et 11) =⇒6 : la premi`ere hypoth`ese implique que A est
semi-primitive au sens de [57, def. 2] (pour toute ﬂ`eche non nulle f de A, il existe
un module simple S tel que S(f)̸ = 0). La conclusion r´esulte alors de [57, th. 16].
6 =⇒5 : pour tout α, soit Iα l’id´eal bilat`ere de A tel que A/Iα = `
β̸=α Dα. Il
est clair que chaque Iα est simple et que A = L Iα.
5=⇒9 : d´ecomposons le bimodule A en L Iα, o`u chaque id´eal bilat`ere Iα est
simple. Soit Aα = A/ L
β̸=α Iβ. Alors Aα s’identiﬁe canoniquement `a Iα, donc
est simple ; en d’autres termes, Aα est simple, et elle est ´evidemment artinienne. Le
lemme A.2.9 montre que A s’identiﬁe `a la somme directe locale des Aα.
9 =⇒6 : on se ram`ene imm´ediatement au cas o`u A est simple. La conclusion
r´esulte alors de [57, prop. 12 et th. 16].
11=⇒7 : cela r´esulte du lemme de Schur.
7 =⇒11 : cela r´esulte de [25, lemma 2] (o`u l’on peut remplacer l’hypoth`ese que
A(A, A) soit de dimension ﬁnie sur K par : A(A, A) est artinienne.)
124
YVES ANDR´E ET BRUNO KAHN
7 ⇐⇒8 : cela vient de ce que toute K-alg`ebre artinienne de radical nul est
semi-simple.
3 =⇒5 : AA est semi-simple, donc de longueur ﬁnie, donc artinien. Soit I
l’ensemble des types d’objets simples de A-Mod et, pour tout α ∈I, choisis-
sons un module simple Sα de type α. Pour tout A-module `a gauche M, notons
Ann(M) = {f | M(f) = 0} : c’est un id´eal bilat`ere de A. On va montrer l’´egalit´e
A = L
α∈I Ann(L
β̸=α Sβ) et que Ann(L
β̸=α Sβ) est un id´eal bilat`ere simple
pour tout α. Pour cela, ´etant donn´e A ∈A, d´ecomposons Ao
A en une somme di-
recte L
α∈I Mα de sous-modules isotypiques. Ecrivons d’abord IdA = P eα, avec
eα ∈Mα(A) pour tout α. On remarque que les Mα(A) sont des id´eaux bilat`eres de
l’anneau A(A, A) ; il en r´esulte que les eα forment un syst`eme d’idempotents or-
thogonaux. En particulier, comme Sβ(A) est facteur direct de Mβ(A), eα op`ere par
0 sur Sβ(A) pour β̸ = α et par l’identit´e pour β = α. Soit maintenant f ∈A(A, B),
et soit f = P fα sa d´ecomposition sur les Mα(B). On a fα = feα, donc fα op`ere
sur Mβ(B) par 0 pour β̸ = α et par f pour β = α. On a donc bien prouv´e que
A(A, B) = L
α∈I Ann(L
β̸=α Sβ)(A, B). Enﬁn, montrons que, pour tout α ∈I,
Iα = Ann(L
β̸=α Sβ) est simple. Soit J un sous-module non nul de Iα. Choisis-
sons A, B ∈A tels que J (A, B)̸ = 0 et soit 0̸ = f ∈J (A, B). On a Sβ(f) = 0
pour tout β̸ = α. Si Sα(f) = 0, on a donc M(f) = 0 pour tout A-module M, ce
qui est absurde en choisissant M = AA. Par cons´equent, Sα(f)̸ = 0.
10 =⇒12 : Pour tout objet semi-simple A, l’alg`ebre A(A, A) est semi-simple
donc rad(A)(A, A) = 0 ; on conclut grˆace `a l’additivit´e des id´eaux sur les objets.
12 =⇒10 : Comme A est suppos´ee ab´elienne et que tout objet est suppos´e
de longueur ﬁnie, tout objet est somme directe ﬁnie d’ind´ecomposables. Tout se
ram`ene `a montrer que tout ind´ecomposable A est simple. Cela r´esulte du lemme
1.4.9 appliqu´e au monomorphisme S֒ →A, o`u S est un sous-objet simple de A
(dans ce cas, le lemme dit que S est facteur direct de A, donc ´egal `a A).
□
A.2.11. Corollaire (`a la d´emonstration). Une K-cat´egorie A est simple (d´eﬁnition
A.2.1) si et seulement si elle est semi-simple et n’a qu’un seul type de module simple.
D´emonstration. Cela r´esulte de la preuve de 6 =⇒5.
□
A.2.12. Contre-exemple. La cat´egorie du contre-exemple A.2.4 est semi-simple au
sens de [57, d´ef. 4], mais pas au sens de la d´eﬁnition 2.1.1 ci-dessus.
A.2.13. Lemme. Dans une cat´egorie ab´elienne semi-simple A, tout morphisme est
somme directe d’un morphisme nul et d’un isomorphisme.
D´emonstration. Soit u : A →B un morphisme de A. On peut d´ecomposer
A = Ker u ⊕A′
B = B′ ⊕Im u.
Sur cette d´ecomposition, u a la forme d´esir´ee.
□
A.2.14. Lemme. Tout foncteur additif F : A →B entre cat´egories ab´eliennes
semi-simples est exact. De plus, les conditions suivantes :
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
125
(i)
F est ﬁd`ele
(ii)
F est conservatif
(iii)
F n’envoie aucun objet non nul de A sur un objet nul de B
sont ´equivalentes.
D´emonstration. Comme tout foncteur additif transforme une suite exacte courte
scind´ee en une suite exacte courte scind´ee, la premi`ere afﬁrmation est claire. (i)
=⇒(iii) est ´evident ; (iii) =⇒(ii) et (ii) =⇒(i) r´esultent imm´ediatement du lemme
A.2.13.
A.3. Cat´egories s´eparables (ou absolument semi-simples).
A.3.1. Th´eor`eme. Soit A une K-cat´egorie. Les conditions suivantes sont ´equiva-
lentes :
(1) Le Ao ⊠K A-module A est projectif.
(2) Le Ao
L ⊠L AL-module AL est projectif pour toute extension L/K.
(3) dimK A(A, B) < ∞pour tous A, B ∈A et AL est semi-simple pour toute
extension L/K.
(4) AL est semi-simple pour toute extension L/K.
(5) dimK A(A, B) < ∞pour tous A, B ∈A et rad(AL) = 0 pour toute
extension L/K.
(6) La cat´egorie Ao ⊠K A est semi-simple.
On dit alors que A est s´eparable.
Si A est K-lin´eaire, ces conditions sont encore ´equivalentes `a
(7) La K-alg`ebre A(A, A) est s´eparable pour tout objet A de A.
D´emonstration. Les conditions 1–6 ´etant manifestement invariantes par passage `a
l’enveloppe K-lin´eaire, on peut supposer A K-lin´eaire.
3 =⇒4 et 3 =⇒5 sont ´evidents. 4 ⇐⇒7 r´esulte de la caract´erisation 7 du
th´eor`eme A.2.10 et de la d´eﬁnition d’une K-alg`ebre s´eparable (d´eﬁnition 2.2.2 a)).
7 =⇒3 r´esulte de la caract´erisation 3 des K-alg`ebres s´eparables dans la proposition
2.2.1. 7 =⇒6 r´esulte du lemme 2.2.5. 5 =⇒7 r´esulte de la caract´erisation 5 des K-
alg`ebres s´eparables dans la proposition 2.2.1. 6 =⇒1 r´esulte de la caract´erisation 1
du th´eor`eme A.2.10. 1 =⇒2 r´esulte du corollaire A.1.5.
Il reste `a d´emontrer que 2 =⇒4. Il sufﬁt de traiter le cas L = K. Pour cela, nous
allons reproduire la raisonnement de [11, ch. IX, d´em. de la prop. 7.1] “`a la main”.
Si M et N sont deux A-modules, on leur associe le Ae-module
HomK(M, N) : (A, B) 7→HomK(M(A), N(B)).
Le foncteur Hom : (A–Mod)o × A–Mod →Ae–Mod est bi-exact.
Soit 0 →N →E →M →0 une extension de M par N. On lui associe une
extension ˜E du Ae-module A par HomK(M, N) par pull-back via le diagramme
0→HomK(M, N) −−−−→HomK(E, N) −−−−→HomK(N, N)→0
||
ρ
x
x
0→HomK(M, N) −−−−→
˜E
π
−−−−→
A
→0.
126
YVES ANDR´E ET BRUNO KAHN
Soit s une section de π. Alors ρ◦s d´eﬁnit un homomorphisme A →HomK(E, N).
Celui-ci correspond `a un homomorphisme f : E →N, et la commutativit´e du dia-
gramme montre que f est une r´etraction du monomorphisme N →E. Ainsi, A est
semi-simple.
□
