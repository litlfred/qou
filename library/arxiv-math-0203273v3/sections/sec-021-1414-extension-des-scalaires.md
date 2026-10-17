---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-021-1414-extension-des-scalaires
section_title: "Extension des scalaires"
section_number: 14.1.4
pages: 112-115
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
---
pos´e de caract´eristique nulle), pour un K-groupe afﬁne G et une extension L/K, il
y a lieu de distinguer entre les L-groupes afﬁnes pRed(G×K L) et pRed(G)×K L.
Par la propri´et´e universelle de pRed, on a toujours un morphisme naturel
(19.4)
pRed(G ×K L) →pRed(G) ×K L.
Nous verrons ci-dessous que ce morphisme n’est pas un isomorphisme en g´en´eral.
Par contre :
19.6.1. Th´eor`eme. Si L/K est ﬁnie, (19.4) est un isomorphisme.
(Il sufﬁt en fait que L/K soit alg´ebrique, cf. th. C.3.)
D´emonstration. Rappelons que dans ce cas, l’extension des scalaires `a la Saavedra
est d´eﬁnie sur A = RepK(G), et que l’on a un isomorphisme de cat´egories A(L) ≃
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
113
RepL(G) (remarque 5.1.3 c)). Consid´erons le diagramme commutatif, o`u une barre
sup´erieure d´esigne la r´eduction modulo le radical :
(19.5)
A(L)
π′
y
π(L) ց
A(L)
α
−−−−→
¯
A(L).
Pour justiﬁer l’existence de ce diagramme (au moyen de 1.4.7), remarquons que
la cat´egorie ¯
A(L) est semi-simple en vertu de la remarque 5.1.3 c), et que π(L) est,
tout comme π, un foncteur plein (et d’ailleurs aussi essentiellement surjectif).
Toute section s de π d´eﬁnit une section s(L) de π(L), ce qui montre que α est
plein et essentiellement surjectif. On a une section de α
s(L) = π′ ◦s(L) : ¯
A(L) →A(L)
qui donne un diagramme naturellement commutatif :
A(L)
ω(L)
−−−−→V ecL
s(L) ր
σ
x
¯
A(L)
s(L)
−−−−→A(L).
D’autre part, on a un diagramme (naturellement) commutatif de cat´egories et
foncteurs :
V ecK
−−−−→
V ecL
ω
x
ω(L)
x
A
−−−−→AL −−−−→A♮
L
≃
−−−−→A(L)
π
y
y
y
y
¯
A
−−−−→
¯
AL −−−−→
¯
A♮
L
¯
A(L).
En effet, le corollaire 4.1.4 montre que le foncteur A →AL est radiciel et que
( ¯
A)L ≃AL (isomorphisme de cat´egories). De mˆeme pour le carr´e suivant, par le
lemme 1.3.10. L’´equivalence de cat´egories A♮
L ∼= A(L) provient du th´eor`eme 5.3.2.
Il en r´esulte en particulier que α est une ´equivalence de cat´egories. Alors s(L) est
une ´equivalence de cat´egories, ce qui termine la d´emonstration.
□
19.7. Enveloppes pro-r´eductives des groupes pro-unipotents. Si G est un K-
groupe pro-unipotent, on sait d´ej`a que pRed(G) est pro-semi-simple simplement
connexe (proposition 19.4.2). Nous allons voir que pRed(G) est en g´en´eral de di-
mension inﬁnie et que son calcul est un probl`eme “insoluble”, le cas de G = Ga
´etant `a cet ´egard exceptionnel.
Consid´erons d’abord le cas de G = Ga × Ga. On peut voir que pRed(G) n’est
pas de dimension ﬁnie en remarquant que les homomorphismes G →Ga, (a, b) 7→
ax + by, (x, y ∈K), donnent lieu `a une inﬁnit´e (param´etr´ee par y/x ∈P1(K))
de repr´esentations ind´ecomposables non ´equivalentes de dimension 2. Elles sont du
reste toutes sous-quotients de la repr´esentation standard de dimension 4 donn´ee par
114
YVES ANDR´E ET BRUNO KAHN

1
a
0
1

×

1
b
0
1

. Cela indique aussi que le morphisme (19.4) d’“extension des
scalaires” n’est pas un isomorphisme en g´en´eral (ne serait-ce que pour raison de car-
dinalit´e). On notera l’analogie formelle entre d’une part ce fait et le th´eor`eme 19.6.1,
et d’autre part le comportement conjectural des groupes de Galois motiviques [55,
6.3? et remarque].
En fait, il s’av`ere que la d´etermination de
Ga × Ga֒ →pRed(Ga × Ga)
est (en un sens convenable) un probl`eme insoluble. En effet, elle inclut la classiﬁca-
tion des repr´esentations ind´ecomposables de Ga × Ga, ou ce qui revient au mˆeme,
des A-modules ﬁnis ind´ecomposables pour A = K[[T1, T2]] (cf. remarque 17.1.2
b)). Or la classiﬁcation des A-modules ﬁnis ind´ecomposables o`u l’action de A se
factorise par le cube du radical m est d´ej`a un probl`eme insoluble, car A/m3 est de
type de repr´esentation inﬁni sauvage (cf. e.g. [43]26) ; plus pr´ecis´ement, la th´eorie
des A/m3-modules ﬁnis est ind´ecidable (cf. [49]).
Les travaux r´ecents de Ginzburg et Panyushev sur les paires nilpotentes [20, 45]
permettent peut-ˆetre toutefois de d´ecrire de nombreux quotients de pRed(Ga×Ga).
19.7.1. Th´eor`eme. Soit G un K-groupe pro-unipotent. Les propri´et´es suivantes
sont ´equivalentes :
a) dim G ≤1,
b) pRed(G) est de dimension ﬁnie,
c) pour toute extension L/K, le morphisme pRed(GL) →pRed(G)L est un isomor-
phisme,
d) le radical inﬁni radω(RepKG) est nul, i.e. RepKG est strictement de Wedder-
burn,
e) radω(RepKG) est nilpotent.
D´emonstration. D’apr`es la discussion des cas Ga et Ga × Ga et le lemme 19.4.6,
il sufﬁt pour l’´equivalence de a), b), c) de d´emontrer que Ga × Ga est quotient de
G d`es que dim G > 1. Passant aux alg`ebres de Lie, il s’agit de voir que pour toute
alg`ebre de Lie nilpotente n de dimension > 1, nab est de dimension > 1. Mais il est
bien connu que dim nab est une borne inf´erieure pour le nombre de g´en´erateurs de
n.
L’implication d) =⇒e) est triviale.
L’implication a) =⇒d) est la proposition 19.5.3.
Pour terminer, prouvons e) =⇒a) par l’absurde. Fixons un ´epimorphisme G →
Ga × Ga. Identiﬁons RepK (Ga × Ga) `a A-Modf avec A = K[[T1, T2]] d’une
part, et `a une sous-cat´egorie pleine de RepKG d’autre part. Soit m le radical de A,
et consid´erons la sous-cat´egorie pleine (A/m3)-Modf de A-Modf. D’apr`es l’hy-
poth`ese et le lemme 3.1.2, le radical inﬁni de (A/m3)-Modf serait donc nilpotent,
en contradiction, d’apr`es [31], avec le caract`ere sauvage de A/m3.
□
26Qui donne aussi une formalisation de la notion de probl`eme de classiﬁcation insoluble ou de
difﬁcult´e maximale.
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
115
Au-del`a du cas unipotent, on peut se poser la question suivante :
19.7.2. Question. Pour quels groupes alg´ebriques lin´eaires G l’enveloppe pro-r´e-
ductive pRed(G) est-elle de dimension ﬁnie ? Sa formation est-elle alors compatible
