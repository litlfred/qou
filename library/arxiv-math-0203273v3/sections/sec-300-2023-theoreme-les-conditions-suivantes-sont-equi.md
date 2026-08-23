---
doc_id: arxiv-math-0203273v3
doc_title: "Nilpotence, radicaux et structures monoïdales"
section_id: sec-300-2023-theoreme-les-conditions-suivantes-sont-equi
section_title: "Th´eor`eme. Les conditions suivantes sont ´equivalentes :"
section_number: 20.2.3
pages: 117-132
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "Nilpotence, radicaux et structures monoïdales — 302 sections: YVES ANDR ´E ET BRUNO KAHN; Introduction; YVES ANDR ´E ET BRUNO KAHN"
---
a)S2V est ind´ecomposable,
b) pour toutn≥ 0,SnV est ind´ecomposable.
D´emonstration. Supposons a). Il est ´ equivalent de dire que SnV est une repr´ e-
sentation ind´ ecomposable deG ou que vue comme repr´ esentation deGV ,SnV est
irr´ eductible. On est donc ramen´ e au cas ouG est r´ eductif connexe, et le r´ esultat
est alors prouv´ e dans [4, app.] (en outre, loc. cit. montre que GV est ´ egal soit ` a
Z(GV ).SL(V ) soit ` aZ(GV ).Sp(V ) pour une forme symplectique convenable, et
le centreZ(GV ) deGV est r´ eduit aux homoth´ eties deGV ). □
118 YVES ANDR ´E ET BRUNO KAHN
20.2.4. Proposition. SoientV,W deux repr´esentations de G, et n un entier > 0.
Les conditions suivantes sont ´equivalentes :
i)V∼
=W ,
ii)V⊗n∼
=W⊗n.
D´emonstration. Comme pr´ ec´ edemment, le probl` eme se ram` ene au probl` emeana-
logue avec G remplac´ e par le groupe r´ eductif connexeGV⊕W . Via l’homomor-
phisme “caract` ere”,i) (resp. ii)) se traduit par l’´ egalit´ ech(V ) = ch( W ) (resp.
ch(V )n = ch(W )n) de polynˆ omes de Laurent en les poids fondamentaux, ` a coef-
ﬁcients entiers positifs. Or tout polynˆ ome de Laurent ` a coefﬁcients entiers positifs
est d´ etermin´ e par sa puissancen-i` eme. □
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 119
APPENDICE A. D ES CAT ´EGORIES SEMI -SIMPLES
L’objet de cet appendice est de clariﬁer la notion de semi-simplicit´ e dans lesK-
cat´ egories (non n´ ecessairement ab´ eliennes), un anneaucommutatif unitaireK ´ etant
ﬁx´ e. On renvoie au§1.3 et au d´ ebut du§2 pour les d´ eﬁnitions de base.
Sauf mention du contraire,A-module signiﬁeA-module `a gauche dans tout l’ap-
pendice.
A.1. Objets projectifs et injectifs. Par un raisonnement classique [19], la cat´ e-
gorie ab´ elienneK-lin´ eaireA–Mod desA-modules (` a gauche) poss` ede assez d’in-
jectifs et de projectifs. Pour les projectifs, nous allons r etrouver ce fait de mani` ere
constructive.
A.1.1. Lemme. Soitf :M→N un homomorphisme deA-modules. Alors
a)f est un ´epimorphisme si et seulement sif (A) : M (A)→N (A) est un ´epimor-
phisme pour toutA∈A .
b) f est un monomorphisme si et seulement si f (A) : M (A) → N (A) est un
monomorphisme pour toutA∈A .
c)f est un isomorphisme si et seulement si f (A) : M (A)→N (A) est un isomor-
phisme pour toutA∈A .
D´emonstration. a) SoitC = Cokerf : on aC(A) = Cokerf (A) pour toutA∈A ,
etC = 0 ⇐⇒ C(A) = 0 pour toutA∈A .
b) R´ esulte de a) par dualit´ e (ou par le mˆ eme raisonnement).
c) est clair. □
A.1.2. Lemme. Pour tout objetA∈A , leA-moduleAA est projectif.
D´emonstration. Soitf : M→A A un ´ epimorphisme. Par le lemme A.1.1,f (A)
est surjectif. Soit m∈ M (A) tel que f (A)(m) = 1 A. Par le lemme de Yoneda
(proposition 1.3.6 a)),m d´ eﬁnit un homomorphisme˜m :AA→M, et on voit tout
de suite que ˜m est une section def. □
A.1.3. D´eﬁnition. UnA-module de la forme⨁ AAi est appel´ e unA-module libre.
ToutA-module libre est projectif. Si A estK-lin´ eaire, toutA-module libre est
de la formeAA pour un objetA convenable.
A.1.4. Proposition. SupposonsA petite.
a) ToutA-moduleM est quotient d’unA-module libre.
b) UnA-moduleP est projectif si et seulement s’il est facteur direct d’unA-module
libre.
D´emonstration. a) Pour tout objet A ∈ A, choisissons un syst` eme g´ en´ erateur
(mA
i )i∈IA deM (A). Alors l’homomorphisme
⨁
A∈A
⨁
i∈IA
AA→M
d´ eﬁni par le lemme de Yoneda est un ´ epimorphisme par le lemme A.1.1 a).
120 YVES ANDR ´E ET BRUNO KAHN
b) La n´ ecessit´ e r´ esulte de a). La sufﬁsance r´ esulte du lemme A.1.2, puisqu’un
facteur direct d’un module projectif est ´ evidemment projectif. □
A.1.5. Corollaire. SiP est unA-module projectif,PL : A↦→L⊗K P (A) est un
AL-module projectif pour toute extensionL/K.
D´emonstration. D’apr` es la proposition A.1.4 b), il sufﬁt de le voir pour P de la
formeAA, auquel cas c’est ´ evident. □
A.2. Cat´egories semi-simples. Les d´ eﬁnitions suivantes sont adapt´ ees de [57].
A.2.1. D´eﬁnition. SoitA uneK-cat´ egorie.
a) Un objet deA est simple s’il n’est pas nul et s’il n’a pas d’autre sous-objet que
lui-mˆ eme et0.
b) Un objet deA est semi-simple s’il est somme directe d’objets simples.
c) Un objetA deA est artinien si toute chaˆ ıne d´ ecroissante de sous-objets deA est
stationnaire.
d) La cat´ egorieA est artinienne si, pour tout A∈A ,AA est un objet artinien de
A-Mod.
e) La cat´ egorieA est simple si elle l’est en tant qu’objet deAe-Mod.
A.2.2. D´eﬁnition. Soit (Aα) une famille de cat´ egories ayant les mˆ emes objets.
a) Le produit local desAα est la cat´ egorie∏ λ
αAα ayant les mˆ emes objets que
lesAα et telle que, pour tout couple d’objets (A,B ), on ait (∏ λ
αAα)(A,B ) =∏
αAα(A,B ).
b)A est somme directe localedesAα si elle est produit local desAα et que, de plus,
pour tout objetA, l’ensemble desα tels que (Aα)A⁄= 0 est ﬁni.
c) Supposons que lesAα soient des K-cat´ egories. Lecoproduit desAα est la K-
cat´ egorieA = ∐
αAα dont la collection d’objets est la r´ eunion des collections
d’objets desAα, avec
A(A,B ) =
{
Aα(A,B ) si∃α :A,B∈A α
0 sinon.
A.2.3. Lemme. SoitA uneK-cat´egorie.
a) Toute somme directe d’objets semi-simples est semi-simple.
b) SoitA∈A un objet tel que tout sous-objet de A soit facteur direct. AlorsA est
semi-simple dans les cas suivants :
(i) A est artinien.
(ii) A est de la formeR-Mod, o`uR est uneK-cat´egorie.
Supposons de plusA ab´elienne.
c) SoitA∈A un objet semi-simple et soitB un sous-objet deA. Alors il existe une
famille (Si)I∈I de sous-objets simples deA telle queA =B⊕⨁
i∈ISi.
d) Tout quotient, tout sous-objet d’un objet semi-simple est semi-simple.
D´emonstration. a) est ´ evident. Dans b), supposons d’abordA artinien. Si A n’est
pas semi-simple, soit B un sous-objet de A minimal parmi ceux qui ne sont pas
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 121
semi-simples. Alors B n’est pas simple, donc poss` ede un sous-objet C ⁄= 0,B .
CommeC est facteur direct deA, il est facteur direct deB, soitB =C⊕D. Mais
C etD sont semi-simples, contradiction. L’autre cas se traite comme la sufﬁsance
dans [11, d´ em. de la prop. 4.1] ( cf. [57, bas p. 140]). c) se d´ emontre comme la
n´ ecessit´ e dansloc. cit. d) r´ esulte imm´ ediatement de c). □
A.2.4. Contre-exemple. SoitA la cat´ egorie des espaces vectoriels de dimension
d´ enombrable sur un corpsk, et soit ¯A la cat´ egorie quotient deA par la sous-cat´ e-
gorie ´ epaisse des espaces vectoriels de dimension ﬁnie. SoitV un espace vectoriel
de dimension inﬁnie, vu comme objet de ¯A. Alors tout sous-objet de V est facteur
direct, maisV ne contient aucun sous-objet simple.
A.2.5. Lemme. SoitA une cat´egorie ab´elienne. Consid´erons les ´enonc´es suivants :
(1) Tout objet deA est semi-simple.
(2) Tout objet deA est projectif.
(3) Tout objet deA est injectif.
Alors 1 =⇒ 2 ⇐⇒ 3. De plus, 1 ⇐⇒ 2 ⇐⇒ 3 dans les deux cas suivants :
(i) Tout objet deA est artinien.
(ii) A est de la formeR-Mod, o`uR est uneK-cat´egorie.
D´emonstration. Il est bien connu que 2⇐⇒ 3, et 1 =⇒ 2 r´ esulte du lemme A.2.3
a). Les implications inverses r´ esultent du lemme A.2.3 b). □
A.2.6. Contre-exemple. Dans la cat´ egorie ¯A du contre-exemple A.2.4, tout objet
est projectif, mais ¯A ne contient aucun objet simple (cf. [48, p. 324]).
A.2.7. Lemme (cf. [25]). SoitA une petite cat´egorieK-lin´eaire pseudo-ab´elienne
et dont tout objet est semi-simple. AlorsA est ab´elienne si et seulement si, pour tout
objet simpleS∈A , l’anneauA(S,S ) est un corps.
D´emonstration. La n´ ecessit´ e r´ esulte du lemme de Schur. Sufﬁsance : soitT l’ensem-
ble des types d’objets simples de A, et pour tout t∈ T soitAt la sous-cat´ egorie
pleine deA form´ ee des objets isotypiques de typet. AlorsAt v´ eriﬁe encore l’hy-
poth` ese, et il sufﬁt de montrer queAt est ab´ elienne. En d’autres termes, on peut
supposerA isotypique. Soit S un objet simple deA, et notons D =A(S,S ) son
corps d’endomorphismes. Le foncteurAo
S s’enrichit en un foncteurT ` a valeurs dans
lesDo-espaces vectoriels, o` uDo est le corps oppos´ e ` aD. En utilisant l’hypoth` ese,
on voit tout de suite que T est pleinement ﬁd` ele et d’image essentielle la cat´ egorie
desDo-espaces vectoriels de dimension≤c, o` uc est le plus grand cardinal tel qu’il
existe un ensembleI de cardinalc tel queS(I)∈A . En particulier,A est ab´ elienne.
□
A.2.8. Contre-exemple. Soit Q[ε] l’alg` ebre des nombres duaux (ε2 = 0). La cat´ e-
gorie des Q[ε]-modules libres de rang ﬁni est Q-lin´ eaire, pseudo-ab´ elienne, artini-
enne, et tout objet est semi-simple, mais elle n’est pas ab´ elienne.
122 YVES ANDR ´E ET BRUNO KAHN
A.2.9. Lemme. SoientA une K-cat´egorie pseudo-ab ´elienne, A ∈ AetAA =⨁
α∈IMα une d´ecomposition deAA en somme directe de sous-modules non nuls.
AlorsI est ﬁni et il existe une unique d ´ecomposition en somme directeA =⨁ Aα
telle que, pour toutα,Mα =AAα. SiA est ind´ecomposable,AA est ind´ecomposa-
ble.
D´emonstration. ´EcrivonsId A =∑ eα aveceα∈Mα(A) pour toutα. Alors, pour
toutB∈A et tout f ∈A A(B) = A(A,B ), on a f = ∑ fe α. Par cons´ equent,
Mα ⁄= 0 =⇒ eα ⁄= 0 . Les Mα sont donc en nombre ﬁni. De plus, le lemme de
Peirce montre que les eα forment un syst` eme d’idempotents orthogonaux, d’o` u la
deuxi` eme assertion en utilisant le lemme de Yoneda. La derni` ere assertion en r´ esulte
imm´ ediatement. □
Le th´ eor` eme qui suit clariﬁe le lien entre diverses notions de semi-simplicit´ e, et
montre qu’elles ne d´ ependent pas de laK-structure.
A.2.10. Th´eor`eme. SoitA uneK-cat´egorie. Les conditions suivantes sont ´equiva-
lentes :
(1) Tout objet deA-Mod est projectif.
(2) Tout objet deA-Mod est injectif.
(3) Tout objet deA-Mod est semi-simple.
(4) Pour toutA∈A ,AA est semi-simple.
(5)A est artinienne et leAo ⊠KA-moduleA est semi-simple.
(6)A est ´equivalente au sens de Morita `a une cat ´egorie de la forme ∐
αDα,
o`u, pour toutα,Dα est un corps gauche.
On dit alors queA est semi-simple (cf. d´eﬁnition 2.1.1).
Si de plusA estK-lin´eaire, les conditions ci-dessus ´equivalent `a :
(7) Pour tout objetA∈A , l’anneauA(A,A ) est semi-simple.
(8) rad(A) = 0 et pour tout A ∈ A,A(A,A ) est un anneau artinien ( `a
gauche).
Enﬁn, siA est en outre pseudo-ab´elienne, les conditions ci-dessus´equivalent
`a :
(9)A est somme directe locale d’une famille de cat´egories artiniennes simples
(ayant les mˆemes objets).
(10)A est ab´elienne et tout objet deA est semi-simple et de longueur ﬁnie.
(11)A est ab´elienne, artinienne, et tout objet deA est semi-simple.
(12)A est ab´elienne, tout objet deA est de longueur ﬁnie, et rad(A) = 0 .
D´emonstration. Il est clair que les six premi` eres conditions ne changent pa s si
l’on remplaceA par une K-cat´ egorie ´ equivalente au sens de Morita. De mˆ eme
les septi` eme et huiti` eme condition sont v´ eriﬁ´ ees pour une cat´ egorieK-lin´ eaireA
si et seulement si elles le sont pour son enveloppe pseudo-ab ´ elienneA♮ : en ef-
fet, pour tout couple d’objets ((A,e ), (A′,e′)) deA♮, on aA♮((A,e ), (A′,e′)) =
e′A(A,A′)e et rad(A♮)((A,e ), (A′,e′)) = e′rad(A)(A,A′)e, cf. aussi lemme
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 123
1.3.10 d). Ceci permet en particulier de supposer dans la suiteAK-lin´ eaire pseudo-
ab´ elienne.
1 ⇐⇒ 2 ⇐⇒ 3 r´ esulte du lemme A.2.5 ; 3=⇒ 4 est ´ evident.
4 =⇒ 3 : soient M unA-module ` a gauche,A ∈ Aet a ∈ M (A). Alors
Ann(a)(B) ={f∈A A(B)|f∗a = 0} d´ eﬁnit unA-id´ eal ` a gauche deA et l’appli-
cationf↦→f∗a induit un morphisme deA-modulesAA/Ann(a)→M. En faisant
varierA eta, on obtient un ´ epimorphisme⨁
A∈A,a∈M (A)AA/Ann(a)−→ →M.
Il r´ esulte alors du lemme A.2.3 queM est semi-simple.
4 =⇒ 10 : le lemme A.2.9 montre que siS∈A est simple, alorsAS est simple ;
en r´ eappliquant ce mˆ eme lemme, on voit que tout objet deA est semi-simple et de
longueur ﬁnie.
Enﬁn, pour tout objet simple S∈A ,A(S,S ) =A-Mod (AS,AS) est un corps,
doncA est ab´ elienne d’apr` es le lemme A.2.7.
10 =⇒ 11 : si S∈A est simple,A(S,S ) est un corps (lemme de Schur), donc
ne contient aucun id´ eal⁄= 0 etAS est simple. Il en r´ esulte queAA est de longueur
ﬁnie, donc artinien, pour toutA∈A .
11 =⇒ 10 : le lemme de Yoneda implique que tout objet deA est artinien, donc
de longueur ﬁnie.
10 =⇒ 3 : comme dans la d´ emonstration du lemme A.2.7, on se ram` eneau cas
o` uA est isotypique. SoitM unA-module ` a gauche. Choisissons un objet simpleS
deA, et soitD le corps des endomorphismes de S (voir ci-dessus). AlorsD op` ere
naturellement ` a gauche surM (S). Pour tout objetA deA, on a un homomorphisme
naturel
A(S,A )⊗DM (S)→M (A)
o` u le produit tensoriel surD est relatif ` a l’action ` a droite deD surA(S,A ), et
l’hypoth` ese surA montre que c’est un isomorphisme de groupes ab´ eliens. On d´eﬁnit
ainsi une ´ equivalence
M↦→M (S)
deA-Mod sur la cat´ egorie desD-espaces vectoriels ` a gauche, dont tout objet est
´ evidemment semi-simple.
6 =⇒ 10 est ´ evident. (3 et 11)=⇒ 6 : la premi` ere hypoth` ese implique queA est
semi-primitive au sens de [57, def. 2] (pour toute ﬂ` eche nonnullef deA, il existe
un module simpleS tel queS(f )⁄= 0). La conclusion r´ esulte alors de [57, th. 16].
6 =⇒ 5 : pour toutα, soitIα l’id´ eal bilat` ere deA tel queA/Iα =∐
β⁄=αDα. Il
est clair que chaqueIα est simple et queA =⨁ Iα.
5=⇒ 9 : d´ ecomposons le bimoduleA en⨁ Iα, o` u chaque id´ eal bilat` ereIα est
simple. SoitAα =A/⨁
β⁄=αIβ. AlorsAα s’identiﬁe canoniquement ` aIα, donc
est simple ; en d’autres termes,Aα est simple, et elle est ´ evidemment artinienne. Le
lemme A.2.9 montre queA s’identiﬁe ` a la somme directe locale desAα.
9 =⇒ 6 : on se ram` ene imm´ ediatement au cas o` uA est simple. La conclusion
r´ esulte alors de [57, prop. 12 et th. 16].
11=⇒ 7 : cela r´ esulte du lemme de Schur.
7 =⇒ 11 : cela r´ esulte de [25, lemma 2] (o` u l’on peut remplacer l’hypoth` ese que
A(A,A ) soit de dimension ﬁnie surK par :A(A,A ) est artinienne.)
124 YVES ANDR ´E ET BRUNO KAHN
7 ⇐⇒ 8 : cela vient de ce que toute K-alg` ebre artinienne de radical nul est
semi-simple.
3 =⇒ 5 : AA est semi-simple, donc de longueur ﬁnie, donc artinien. Soit I
l’ensemble des types d’objets simples de A-Mod et, pour tout α ∈ I, choisis-
sons un module simple Sα de type α. Pour tout A-module ` a gaucheM, notons
Ann(M ) ={f|M (f ) = 0} : c’est un id´ eal bilat` ere deA. On va montrer l’´ egalit´ e
A = ⨁
α∈IAnn(⨁
β⁄=αSβ) et que Ann(⨁
β⁄=αSβ) est un id´ eal bilat` ere simple
pour tout α. Pour cela, ´ etant donn´ eA∈A , d´ ecomposonsAo
A en une somme di-
recte⨁
α∈IMα de sous-modules isotypiques. Ecrivons d’abordId A =∑ eα, avec
eα∈Mα(A) pour toutα. On remarque que lesMα(A) sont des id´ eaux bilat` eres de
l’anneauA(A,A ) ; il en r´ esulte que leseα forment un syst` eme d’idempotents or-
thogonaux. En particulier, commeSβ(A) est facteur direct deMβ(A),eα op` ere par
0 surSβ(A) pourβ⁄=α et par l’identit´ e pourβ =α. Soit maintenantf∈A (A,B ),
et soitf =∑ fα sa d´ ecomposition sur lesMα(B). On afα =fe α, doncfα op` ere
sur Mβ(B) par 0 pour β⁄= α et par f pour β = α. On a donc bien prouv´ e que
A(A,B ) = ⨁
α∈IAnn(⨁
β⁄=αSβ)(A,B ). Enﬁn, montrons que, pour tout α∈ I,
Iα =Ann(⨁
β⁄=αSβ) est simple. SoitJ un sous-module non nul deIα. Choisis-
sonsA,B ∈A tels queJ (A,B )⁄= 0 et soit 0⁄= f∈J (A,B ). On a Sβ(f ) = 0
pour toutβ⁄= α. Si Sα(f ) = 0 , on a donc M (f ) = 0 pour toutA-moduleM, ce
qui est absurde en choisissantM =AA. Par cons´ equent,Sα(f )⁄= 0.
10 =⇒ 12 : Pour tout objet semi-simple A, l’alg` ebreA(A,A ) est semi-simple
donc rad(A)(A,A ) = 0 ; on conclut grˆ ace ` a l’additivit´ e des id´ eaux sur les objets.
12 =⇒ 10 : Comme A est suppos´ ee ab´ elienne et que tout objet est suppos´ e
de longueur ﬁnie, tout objet est somme directe ﬁnie d’ind´ ec omposables. Tout se
ram` ene ` a montrer que tout ind´ ecomposableA est simple. Cela r´ esulte du lemme
1.4.9 appliqu´ e au monomorphisme֒→A, o` uS est un sous-objet simple de A
(dans ce cas, le lemme dit queS est facteur direct deA, donc ´ egal ` aA). □
A.2.11. Corollaire (` a la d´ emonstration). UneK-cat´egorieA est simple (d´eﬁnition
A.2.1) si et seulement si elle est semi-simple et n’a qu’un seul type de module simple.
D´emonstration. Cela r´ esulte de la preuve de 6=⇒ 5. □
A.2.12. Contre-exemple. La cat´ egorie du contre-exemple A.2.4 est semi-simple au
sens de [57, d´ ef. 4], mais pas au sens de la d´ eﬁnition 2.1.1 ci-dessus.
A.2.13. Lemme. Dans une cat´egorie ab´elienne semi-simpleA, tout morphisme est
somme directe d’un morphisme nul et d’un isomorphisme.
D´emonstration. Soitu :A→B un morphisme deA. On peut d´ ecomposer
A = Keru⊕A′
B =B′⊕ Imu.
Sur cette d´ ecomposition,u a la forme d´ esir´ ee. □
A.2.14. Lemme. Tout foncteur additif F :A → Bentre cat ´egories ab ´eliennes
semi-simples est exact. De plus, les conditions suivantes :
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 125
(i) F est ﬁd`ele
(ii) F est conservatif
(iii) F n’envoie aucun objet non nul deA sur un objet nul deB
sont ´equivalentes.
D´emonstration. Comme tout foncteur additif transforme une suite exacte cou rte
scind´ ee en une suite exacte courte scind´ ee, la premi` ere afﬁrmation est claire. (i)
=⇒ (iii) est ´ evident ; (iii)=⇒ (ii) et (ii) =⇒ (i) r´ esultent imm´ ediatement du lemme
A.2.13.
A.3. Cat´egories s´eparables (ou absolument semi-simples).
A.3.1. Th´eor`eme. SoitA uneK-cat´egorie. Les conditions suivantes sont ´equiva-
lentes :
(1) LeAo ⊠KA-moduleA est projectif.
(2) LeAo
L ⊠LAL-moduleAL est projectif pour toute extensionL/K.
(3) dimKA(A,B )<∞ pour tousA,B ∈A etAL est semi-simple pour toute
extensionL/K.
(4)AL est semi-simple pour toute extensionL/K.
(5) dimKA(A,B ) <∞ pour tous A,B ∈ Aet rad(AL) = 0 pour toute
extensionL/K.
(6) La cat´egorieAo ⊠KA est semi-simple.
On dit alors queA est s´ eparable.
SiA estK-lin´eaire, ces conditions sont encore ´equivalentes `a
(7) LaK-alg`ebreA(A,A ) est s´eparable pour tout objetA deA.
D´emonstration. Les conditions 1–6 ´ etant manifestement invariantes par passage ` a
l’enveloppeK-lin´ eaire, on peut supposerAK-lin´ eaire.
3 =⇒ 4 et 3 =⇒ 5 sont ´ evidents. 4⇐⇒ 7 r´ esulte de la caract´ erisation 7 du
th´ eor` eme A.2.10 et de la d´ eﬁnition d’uneK-alg` ebre s´ eparable (d´ eﬁnition 2.2.2 a)).
7 =⇒ 3 r´ esulte de la caract´ erisation 3 desK-alg` ebres s´ eparables dans la proposition
2.2.1. 7 =⇒ 6 r´ esulte du lemme 2.2.5. 5=⇒ 7 r´ esulte de la caract´ erisation 5 desK-
alg` ebres s´ eparables dans la proposition 2.2.1. 6=⇒ 1 r´ esulte de la caract´ erisation 1
du th´ eor` eme A.2.10. 1=⇒ 2 r´ esulte du corollaire A.1.5.
Il reste ` a d´ emontrer que 2=⇒ 4. Il sufﬁt de traiter le casL =K. Pour cela, nous
allons reproduire la raisonnement de [11, ch. IX, d´ em. de laprop. 7.1] “` a la main”.
SiM etN sont deuxA-modules, on leur associe leAe-module
Hom
K(M,N ) : (A,B )↦→Hom K(M (A),N (B)).
Le foncteur Hom : (A–Mod )o×A –Mod→A e–Mod est bi-exact.
Soit 0→ N→ E→ M→ 0 une extension de M parN. On lui associe une
extension ˜E duAe-moduleA par HomK(M,N ) par pull-back via le diagramme
0→HomK(M,N ) −−−−→HomK(E,N ) −−−−→HomK(N,N )→ 0
|| ρ
↑


↑


0→Hom
K(M,N ) −−−−→ ˜E π−−−−→ A → 0.
126 YVES ANDR ´E ET BRUNO KAHN
Soits une section deπ. Alorsρ◦s d´ eﬁnit un homomorphismeA→ HomK(E,N ).
Celui-ci correspond ` a un homomorphismef :E→N, et la commutativit´ e du dia-
gramme montre quef est une r´ etraction du monomorphismeN→E. Ainsi,A est
semi-simple. □
APPENDICE B. E RRATUM `A [1]
O. Gabber nous a fait remarquer que la preuve de [1, Prop. 6] ´ e tait (encore)
incompl` ete. Le probl` eme est que la d´ emonstration donn´ ee dans loc. cit. s’applique ` a
un motif de la formeh(X), o` uX est une vari´ et´ e projective lisse, mais pasa priori ` a
un motif g´ en´ eralM. Plus pr´ ecis´ ement, siM est effectif (pour ﬁxer les id´ ees) et que
le projecteur de K¨ unneth pair deM est alg´ ebrique, il n’est pas clair qu’on puisse
choisir une vari´ et´ eX telle que h(X) contienneM en facteur direct et telle que le
projecteur de K¨ unneth pair deX soit alg´ ebrique.
V oici deux mani` eres de corriger ce point (la premi` ere est en substance celle que
nous a propos´ ee Gabber). Les notations sont celles de [1].
B.1. Premi`ere correction. Comme remarqu´ e au d´ ebut de la preuve deloc. cit. , il
sufﬁt de supposer que le corps de basek est de type ﬁni sur Fp.
B.1.1. Lemme. SoientH :Mot rat→Modf-L une cohomologie de Weil classique
`a coefﬁcients dans une Q-alg`ebre commutative semi-simpleL etMot H la cat´ego-
rie des k-motifsH-homologiques `a coefﬁcients rationnels. Pour tout A∈ Mot H,
notons
H +(A) =
⨁
i pair
H i(A), H−(A) =
⨁
i impair
H i(A).
Alors, pourA,B∈Mot H, on a
RH(A,B ) =
{f∈Mot H (A,B )|∀g∈Mot H (B,A ),∀i∈ Z,trH i(g◦f ) = 0}
={f∈Mot H(A,B )|∀g∈Mot H(B,A ),trH +(g◦f ) = trH−(g◦f ) = 0},
o`uRH est le radical deMot H.
D´emonstration. D’apr` es [1, prop. 5],Mot H est semi-primaire, donc son radical de
Kelly co¨ ıncide avec son radical de Gabriel. L’´ enonc´ e r´ esulte alors du lemme 1.4.3.
□
B.1.2. Lemme. Avec les notations du lemme B.1.1, l’image r ´eciproque snum de
RH dans la cat´egorieMot rat des motifs de Chow ne d´epend pas du choix deH.
D´emonstration. ´Etant donn´ e le lemme B.1.1, il sufﬁt de voir que, pour toute k-
vari´ et´ e projective lisseX et toute correspondance c∈ CH dim X(X×X) et tout
i∈ Z,trH i(c) est un nombre rationnel qui ne d´ epend pas deH. Par changement
de base propre et lisse et par sp´ ecialisation des cycles alg´ ebriques, on se r´ eduit par
r´ ecurrence sur le degr´ e de transcendance dek sur Fp au cas o` uk est ﬁni (cf. [1, d´ em.
de la prop. 5]). L’assertion r´ esulte alors de [29]. □
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 127
B.1.3. Lemme (cf. [1, lemme 7]). Soient, pour ﬁxer les id´ees,ℓ⁄=ℓ′⁄=p deux nom-
bres premiers. Alors le noyau du foncteurMot ℓℓ′→Mot ℓ est un id´eal localement
nilpotent.
D´emonstration. Cela r´ esulte des lemmes B.1.1 et B.1.2. □
B.1.4. Lemme. Les foncteurs pleins Mot ℓ→ Mot snum,Mot ℓ′ → Mot snum in-
duisent des bijections sur les classes d’isomorphisme d’objets. En particulier, pour
tout objetM deMot ℓ,bi(M ) = dim H i
ℓ(M ) ne d´epend pas deℓ, et ne d´epend que
de la classe d’isomorphisme de l’image deM dansMot snum.
D´emonstration. Par le lemme B.1.3, ces foncteurs sont essentiellement surjectifs et
conservatifs. □
B.1.5. Lemme. L’imageM∗
snum deM∗
ℓ dansMot snum consiste en la sous-cat´ego-
rie pleine form´e des objets isomorphes `a des sommes ﬁnies d’objets n’ayant qu’un
seul nombre de Betti non nul. En particulier,M∗
snum est ind´ependant deℓ. De mˆeme
avecM±.
D´emonstration. C’est clair par le lemme B.1.4, car on a la mˆ eme propriet´ e au
niveau deM∗
ℓ . □
B.1.6. Lemme. M∗
snum =M∗
num etM±
snum =M±
num.
D´emonstration. C’est clair. □
B.2. Seconde correction. Celle-ci ne marche que pour les M± mais s’applique ` a
toute cohomologie de Weil, classique ou non.
D’apr` es le th´ eor` eme 9.2.1 c), pour toute cohomologie de WeilH on aMot±
H =
(Mot H)kim. D’autre part, la proposition 9.1.14 implique que le foncteur (Mot H)kim
→ (Mot num)kim est essentiellement surjectif. Ainsi, Mot±
num = ( Mot num)kim
pour toute cohomologie de WeilH. □
Table de concordance pour les r´ef´erences de [1].
– Preuve du th´ eor` eme 1 : remplacer [3, 6.7.3] par [3, 8.2.2].
– Preuve de la proposition 2 : remplacer [3, 6.7.9 et 1.4.2b] p ar [3, 8.3.1 et
1.4.4b].
– D´ ebut de2 : remplacer [3, 9.2.1, 9.7.3, 11.3.5] par [3, 13.2.1, 13.7.1, 15.3.5].
APPENDICE C. F INITE DIMENSIONALITY OF REDUCTIVE ENVELOPES , BY
PETER O’SULLIVAN
The object of this appendix is to determine when proreductiv e envelopes are ﬁ-
nite dimensional and when their formation is compatible wit h extension of scalars.
Letk be a ﬁeld of characteristic 0, and letH be an afﬁne k-group. Then the prore-
ductive envelope of H is ﬁnite dimensional if and only if H is ﬁnite dimensional
with prounipotent radical of dimension≤ 1 (Theorem C.5). This is a consequence
128 YVES ANDR ´E ET BRUNO KAHN
of Theorem C.1 characterising the afﬁne k-groups with prounipotent radical of di-
mension≤ 1 as those whose representations are “rigid”. If the prounipo tent rad-
ical U of H has dimension 1 the proreductive envelope of H is the semidirect
product of H/U by SL(2) (Theorem C.4). Let k′ be an extension of k. Then
p Red(Hk′)→ p Red(H)k′ is an isomorphism if and only if either k′ is algebraic
overk or the prounipotent radical of H is of dimension≤ 1 (Theorem C.3). This
follows from Theorem C.2 which gives the conditions under which every represen-
tation ofH overk′ is a direct summand of one deﬁned overk.
Throughout this appendixk denotes a ﬁeld of characteristic 0. Unless otherwise
stated, representations are assumed to be ﬁnite dimensional.
C.1. Families of representations. The object of this section is to prove Theo-
rems C.1 and C.2. The proofs are based on Lemmas C.4 and C.5. Le mma C.5 is
necessary also for the proof of Theorem C.4.
Lemma C.1. Suppose thatk is algebraically closed. LetM be a connected reduc-
tivek-group and letV be a representation ofM. Denote by P the set of dominant
weights ofM relative to some maximal torus T and Borel subgroupB⊃T ofM,
and for eachµ∈P letVµ be a representation ofM with highest weightµ. Then if
τ∈ P is such that τ +λ∈ P for eachλ in the set Λ of weights of V , there is an
M-isomorphismV⊗kVτ≃⨁
λ∈Λ V m(λ)
τ +λ , wherem(λ) is the multiplicity of λ in
V .
Proof. Denote by χ andχµ forµ∈ P the respective restrictions of the characters
ofV andVµ toT . It sufﬁces to show thatχχτ =∑
λ∈Λ m(λ)χτ +λ.
Let W be the Weyl group of M relative to T and let δ be half the sum of the
positive roots ofM relative toT andB. For anyπ in the character group ofT , write
e(π) forπ regarded as an element ofk[T ]. Then we have
∑
λ∈Λ
m(λ)e(λ)
∑
w∈W
(detw)e(w(τ +δ)) =
∑
w∈W
(detw)e(w(τ +δ))
∑
λ∈Λ
m(wλ)e(wλ)
=
∑
λ∈Λ
m(λ)
∑
w∈W
(detw)e(w(τ +λ +δ))
since Λ is stable under W and m(wλ) = m(λ) for w∈ W and λ∈ Λ . Thus if
Q =∑
w∈W (detw)e(wδ), we have by Weyl’s character formula
Qχχτ =Q
∑
λ∈Λ
m(λ)χτ +λ,
whence the required result, sinceQ⁄= 0. □
Lemma C.2. Suppose thatk is algebraically closed. LetM be a non-commutative
connected reductive k-group and let V be a faithful irreducible representation of
M. Suppose that V has, relative to some maximal torus of M, at most 3 distinct
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 129
non-zero weights. Then either the derived groupM′ ofM is simple of typeA1 and
V is of dimension 2 or 3, orM′ is simple of typeA2 andV is of dimension 3.
Proof. We may suppose thatM =M′ is semisimple. Let ˜M be the universal cover
ofM, so thatV may also be regarded as a representation of ˜M. LetT be a maximal
torus and B⊃ T a Borel subgroup of M, let X be the character group of T and
W the Weyl group of M relative toT , and let λ∈ X be the highest weight of V
relative toT andB. SinceV has at most 3 distinct non-zero weights, the orbit Λ of
λ underW has at most 3 elements. There is a decompositionW =W1×···× Wr
corresponding to the simple factors of ˜M such that the representation of W on
X⊗ R is the direct sum of non-trivial irreducible representatio ns Xi of Wi for
i = 1,...,r . By faithfulness of the M-representationV , the projection of λ onto
eachXi is non-zero. Thusr = 1 and ˜M is simple, since otherwise Λ would have at
least 4 elements. The afﬁne subspace ofX⊗ R generated by Λ is of dimension≤ 2
and is stable under W , so by irreducibility the rank dimR(X⊗ R) of ˜M is≤ 2.
SinceW contains a rotation of order 4 when ˜M is of type B2 and of order 6 when
˜M is of typeG2, it follows that ˜M must be of typeA1 orA2.
If ˜M is of typeA1 any ˜M-representation of dimension≥ 4 has at least 4 distinct
non-zero weights. If ˜M is of typeA2, letτ1 andτ2 be the highest weights of the two
fundamental representations of ˜M relative toT andB, so that the simple positive
roots of ˜M are µ1 = 2τ1−τ2 and µ2 = −τ1 + 2τ2, and λ = m1τ1 +m2τ2
for integers mi≥ 0. One of m1,m 2 must be 0, since otherwise Λ would contain
6 elements. Thus either λ = τ1 or λ = τ2, since if for example λ = m1τ1 with
m1≥ 2 thenλ−µ1 would be a non-zero weight ofV not conjugate toλ underW ,
soV would have at least 6 distinct non-zero weights. □
Lemma C.3. Suppose thatk is algebraically closed. LetM be a connected reduc-
tivek-group and let V be a representation of M which is either the direct sum of
two non-isomorphic 1-dimensional representations or is irreducible of dimension 2
or 3. Then there exists a family (V i
j,r i
j,s i
j)i,j∈N, with the V i
j irreducible represen-
tations of M and the ri
j : V⊗kV i
j → V i+1
j andsi
j : V⊗kV i
j+1→ V i
j non-zero
M-homomorphisms, such that :
(i) for each integerm theV i
j withi−j =m are pairwise non-isomorphic ;
(ii) the restrictions of
ri+1
j ◦ (V⊗ri
j) : V⊗kV⊗kV i
j→V i+2
j ,
si
j−2◦ (V⊗si
j−1) : V⊗kV⊗kV i
j →V i
j−2,
si+1
j−1◦ (V⊗ri
j) +ri
j−1◦ (V⊗si
j−1) : V⊗kV⊗kV i
j →V i+1
j−1,
respectively to⋀ 2V⊗kV i
j ,⋀ 2V⊗kV i
j ,⋀ 2V⊗kV i
j , are 0 fori,j∈ N.
Proof. We may suppose thatV is a faithful representation ofM. IfV≃V1⊕V2 with
V1 andV2 1-dimensional and p1 : V → V1 andp2 : V → V2 are the projections,
takeV i
j = V⊗i
1 ⊗k (V∨
2 )⊗j and (modulo canonical isomorphisms) ri
j = p1⊗V i
j
andsi
j =p2⊗V i
j+1. It is immediately checked that (i) and (ii) hold.
130 YVES ANDR ´E ET BRUNO KAHN
Now suppose that V is irreducible of dimension 2 or 3. Let T andB⊃ T be a
maximal torus and Borel subgroup ofM, and writeλ andλ∨ for the respective high-
est weights ofV andV∨ relative toT andB. LetV i
j be an irreducible representation
ofM with highest weightiλ +jλ∨. Then (i) clearly holds becauseλ +λ∨⁄= 0. All
weights of⋀ 2V⊗kV i
j are of the form (i + 2)λ +jλ∨−π whereπ⁄= 0 is a sum
of positive roots ofM, so HomM (⋀ 2V⊗kV i
j,V i+2
j ) = 0 . Similarly
HomM (
2⋀
V⊗kV i
j+2,V i
j ) = Hom M (V i
j+2,
2⋀
V∨⊗kV i
j ) = 0.
Thus it sufﬁces to constructri
j⁄= 0 andsi
j⁄= 0 fori,j∈ N such that the restriction
of the third homomorphism of (ii) to⋀ 2V⊗kV i
j+1 is 0.
Letti
j⁄= 0 be an element of the highest weight space of V i
j and let u+⁄= 0 be
an element of the highest weight space of V andu−⁄= 0 an element of the lowest
weight space of V . The weights of ti
j,u+ andu− are thus respectively iλ +jλ∨,
λ and−λ∨. The k-linear map V → k which sends u− to 1 and which is 0 on the
other weight spaces ofV is an elementu∨
+⁄= 0 of the highest weight space of V∨.
NowV⊗kV i
j contains the weight (i + 1)λ +jλ∨ with multiplicity 1, and all of its
other weights are of the form (i + 1)λ +jλ∨−π whereπ⁄= 0 is a sum of positive
roots. Thus there is a uniqueM-homomorphismri
j :V⊗kV i
j→V i+1
j such that
(C.1) ri
j(u+⊗ti
j) = ti+1
j .
Similarly there is a unique M-homomorphism qi
j : V i
j+1→ V∨⊗k V i
j such that
qi
j(ti
j+1) = u∨
+⊗ti
j, whence for any constant Cn = Cn(M,V ) there is a unique
M-homomorphismsi
j :V⊗kV i
j+1→V i
j such that
(C.2) si
j(u−⊗ti
j+1) = Ci+jti
j.
ChooseCn as follows. By Lemma (C.2), either the derived group M′ of M is of
typeA1 andV is of dimension 2 or 3, orM′ is of typeA2 andV is of dimension 3.
Set
(C.3) Cn =





1/(n + 2) ifM′ is typeA1 andV is of dimension 2,
(n + 1)/(2n + 3) ifM′ is of typeA1 andV is of dimension 3,
1/(n + 3) ifM′ is of typeA2.
TheV i
j,r i
j,s i
j just constructed are compatible with restriction fromM toM′, so
to check that the third homomorphism of (ii) has restriction 0 to⋀ 2V⊗kV i
j+1 we
may suppose that M′ = M. We show ﬁrst that HomM (⋀ 2V ⊗k V i
j+1,V i+1
j ) is
1-dimensional. This is immediate when M is of type A1, since then V i
j ≃ V i+j
0
and⋀ 2V is either trivial 1-dimensional or M-isomorphic to V according as V is
2-dimensional or 3-dimensional. When M is of type A2, V and V∨ are the two
fundamental representations of M, so the dominant weights of M relative to T
and B are the iλ +jλ∨ for i,j ≥ 0. The weights of V are λ,−λ +λ∨,−λ∨,
and⋀ 2V ≃ V∨. Applying Lemma C.1 with V replaced by ⋀ 2V and with τ =
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 131
iλ + (j + 1)λ∨ shows that⋀ 2V⊗kV i
j+1 containsV i+1
j with multiplicity 1 when
i≥ 1,j ≥ 0. Similarly, whenj≥ 1,⋀ 2V∨⊗kV 1
j containsV 0
j+1 with multiplicity
1, whence ⋀ 2V ⊗k V 0
j+1 contains V 1
j with multiplicity 1. That ⋀ 2V ⊗k V 0
1 ≃
V∨⊗k V∨ containsV 1
0 ≃ V with multiplicity 1 is clear. Thus HomM (⋀ 2V⊗k
V i
j+1,V i+1
j ) is in all cases 1-dimensional. The restriction to ⋀ 2V⊗k V i
j+1 of the
third homomorphism of (iii) will thus be 0 provided that that the images of (u+⊗
u−−u−⊗u+)⊗ti
j+1 underri
j◦ (V⊗si
j) and−si+1
j ◦ (V⊗ri
j+1) are non-zero
and coincide. Now
(C.4) si
j(u+⊗ti
j+1) = 0
because the difference between the weight (i + 1)λ + (j + 1)λ∨ ofu+⊗ti
j+1 and
the highest weightiλ +jλ∨ ofV i
j is non-zero and dominant. Thus by (C.1), (C.2)
and (C.3) it is enough to show that
(C.5) si+1
j (u+⊗ri
j+1(u−⊗ti
j+1)) = (Ci+j+1−Ci+j)ti+1
j .
Write m for the Lie algebra of M. Suppose ﬁrst that M is of type A1 andV is
of dimension 2. Let e be an element of the positive root subspace of m, chosen so
that eu− = u+, and let f,h be such that f is in the negative root subspace of m
and [e,f ] = h, [h,e ] = 2 e, and [h,f ] = −2f. Then hu+ = u+, hu− =−u−,
fu + =u−, andhti
j = (i +j)ti
j. We have
ri
j+1(u−⊗ti
j+1) = 1
i +j + 2ft i+1
j+1,
u+⊗ft i+1
j+1 =f (u+⊗ti+1
j+1)−u−⊗ti+1
j+1,
where the constant 1/(i +j + 2) in the ﬁrst equality is determined by acting withe
and using (C.1). Using (C.4), (C.2), and (C.3) we obtain (C.5).
When M is of type A1 and V is of dimension 3, choose e and f, h such that
e2u− = u+ and [e,f ] = h, [h,e ] = 2 e, and [h,f ] = −2f. Then hu+ = 2u+,
hu− =−2u−,fu + = 2eu−,f 2u+ = 4u−, andhti
j = 2(i +j)ti
j. We have
ri
j+1(u−⊗ti
j+1) = 1
4(i +j + 2)(2i + 2j + 3)f 2ti+1
j+1,
u+⊗f 2ti+1
j+1 =f (u+⊗ft i+1
j+1−fu +⊗ti+1
j+1) + 4u−⊗ti+1
j+1,
where the constant in the ﬁrst equality is determined by acting withe2. The images
undersi+1
j ofu+⊗ft i+1
j+1 andfu +⊗ti+1
j+1 are 0 by weights, so using (C.2) and (C.3)
we obtain (C.5).
Finally suppose that M is of type A2. Then the simple positive roots of M are
µ = 2λ−λ∨ andµ∨ =−λ + 2λ∨. Lete ande∨ be elements of the root subspaces
of m corresponding respectively toµ andµ∨. We may supposee ande∨ chosen so
thatee∨u− =u+. Letf,f∨,h,h∨ be the unique elements of m such thatf andf∨
lie in the root subspaces corresponding respectively to−µ and−µ∨ and [e,f ] = h,
[h,e ] = 2 e, [h,f ] = −2f, [e∨,f∨] = h∨, [h∨,e∨] = 2 e∨, [h∨,f∨] = −2f∨.
Then [h,h∨] = 0 , [h,e∨] = −e∨, [h∨,e ] = −e, [h,f∨] = f∨, [h∨,f ] = f,
and [e,f∨] = [ e∨,f ] = 0 . Also eu− = f∨u+ = 0 , e∨u− = fu +, hu+ = u+,
132 YVES ANDR ´E ET BRUNO KAHN
h∨u+ = 0 ,hu− = 0 ,h∨u− =−u−,f∨fu + = u−, and hti
j = iti
j,h∨ti
j = jti
j,
eti
j =e∨ti
j = 0. We have
ri
j+1(u−⊗ti
j+1) = 1
(i + 1)(i +j + 3) ((i + 2)f∨f− (i + 1)ff∨)ti+1
j+1,
u+⊗f∨ft i+1
j+1 =f∨(u+⊗ft i+1
j+1),
u+⊗ff∨ti+1
j+1 =f (u+⊗f∨ti+1
j+1)−f∨(fu +⊗ti+1
j+1) +u−⊗ti+1
j+1,
where the coefﬁcients in the ﬁrst equality are determined by acting withee∨ ande.
The respective weights of u+⊗ft i+1
j+1,u+⊗f∨ti+1
j+1, andfu +⊗ti+1
j+1 differ from
the highest weight of V i+1
j by the positive rootsµ∨,µ andµ∨, so the image under
si+1
j of all three elements is 0. Using (C.2) and (C.3) we obtain (C.5). □
LetH be an afﬁnek-group and letS be ak-scheme. A family of representations
ofH overS, or simply a representation ofH overS, is a locally freeOS-moduleV
of ﬁnite type together with a homomorphism HS→ GL(V) overS. Suppose that
H is a semidirect productU ⋊M. ThenM acts onU by group automorphisms. A
representation ofH overS is the same as a representationV ofM together with an
M-homomorphismρ :US→GL(V) overS. IfU is of ﬁnite type and V is its Lie
algebra, the M-structure on U deﬁnes a structure of M-Lie algebra on V . ¿From
ρ we then obtain a homomorphism σ : V ⊗kOS → EndOS (V) of (M,OS )-Lie
algebras.
Suppose thatU is a vector group andS is quasi-compact. Then theρ correspond
uniquely to the σ for whichσn = 0 for somen. It follows that a representation of
H overS is the same as a pair (V,µ ), whereV is a representation ofM overS and
whereµ is anM-homomorphism
(C.6) µ :V⊗kV→V
ofOS-modules such that the
(C.7) µ(n) :V⊗n⊗kV→V ,
deﬁned inductively byµ(0) = 1V andµ(n) =µ◦ (V⊗kµ(n−1)), are 0 forn large,
and such that the restriction ofµ(2) to⋀ 2V⊗kV is 0 (corresponding to [σ,σ ] = 0 ).
When S = Spec(k) the images of the µ(n) deﬁne an H-invariant ﬁltration on
