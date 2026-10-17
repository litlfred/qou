---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-012-1341-la-construction-de-mac-lane
section_title: "La construction de Mac Lane"
section_number: 13.4.1
pages: 67-70
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
doc_brief: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002 — 31 sections: Front matter; Introduction; Alg`ebres `a plusieurs objets"
---
(A, •), on associe une petite cat´egorie mono¨ıdale stricte (Astr, ⊤), et deux foncteurs
mono¨ıdaux B
u
→
←
v A, avec u strict, tels que le compos´e uv soit le foncteur mono¨ıdal
identique de A (les foncteurs sous-jacents `a u et v sont donc quasi-inverses).
Rappelons cette construction : on prend pour objets de Astr les mots (ﬁnis) dont
les lettres sont les objets de A. Les morphismes entre mots sont les morphismes
entre les objets de A correspondants obtenus par parenth´esage canonique (toutes
les parenth`eses commencent au d´ebut du mot). Le produit ⊤, souvent omis de la
notation, est donn´e au niveau des objets par la concat´enation des mots ; v est donn´e
par la “formation de mots d’une lettre”, tandis que u est donn´e par le “parenth´esage
canonique” (e.g. u(ABC) = (A • B) • C)). L’unit´e est le mot vide : u(∅) = 1.
C’est une K-cat´egorie si A l’´etait, et u, v sont alors des K-foncteurs.
Noter que lorsque A est K-lin´eaire, la construction A⊕est un cas particulier de
cette construction, en prenant • = ⊕.
Si s : B →A est un foncteur, on lui associe canoniquement comme suit un
foncteur mono¨ıdal strict sstr : Bstr →Astr : on associe au mot w = B1 . . . Bn de
Bstr le mot sstr(w) = s(B1) . . . s(Bn) de Astr (sstr(∅) = ∅).
On associe `a f ∈Bstr(w, w′) = B(u(w), u(w′)) le morphisme sstr(f) = s(f) ∈
A(u(sstr(w)), u(sstr(w′))) = Astr(sstr(w), sstr(w′)).
Si s est sous-jacent `a un foncteur mono¨ıdal strict, on a usstr = su (donc s =
uA ◦sstr ◦vB).
Vu la construction de Mac Lane et le sorite 13.3.3, pour d´emontrer le th´eor`eme
13.2.1, on peut supposer A stricte. Le th´eor`eme 13.2.1 r´esulte alors de la proposition
plus pr´ecise suivante :
13.4.2. Proposition. Soient (A, •), ¯
A, πA comme dans le th´eor`eme 13.2.1. Si en
outre A est mono¨ıdale stricte,
a) Il existe une section mono¨ıdale stricte s de πA.
b) Toute autre section mono¨ıdale stricte de πA est isomorphe `a s.
68
YVES ANDR´E ET BRUNO KAHN
c) Toute section mono¨ıdale de πA est naturellement isomorphe `a une section mono-
¨ıdale stricte de πA.
13.5. R´eductions. Commenc¸ons par une r´eduction du probl`eme en deux lemmes.
13.5.1. Lemme. La proposition 13.4.2 d´ecoule de l’´enonc´e correspondant pour la
cat´egorie mono¨ıdale stricte K-lin´eaire A⊕.
D´emonstration. Soit S une section mono¨ıdale stricte de πA⊕. Le foncteur mono¨ıdal
strict (pleinement) ﬁd`ele A v⊕
→A⊕induit un diagramme commutatif
¯
A
¯v
−−−−→
¯
A⊕
s
y
S
y
A
v
−−−−→A⊕.
R´eciproquement, si s est donn´ee, on peut prendre S = s⊕.
□
En identiﬁant ( ¯
Astr)⊕et (Astr)⊕, ce lemme nous ram`ene `a prouver la proposi-
tion 13.4.2 dans le cas strictement K-lin´eaire, strictement mono¨ıdal.
13.5.2. Lemme. Supposons que A soit strictement K-lin´eaire, et mono¨ıdale stricte.
Soit s une section fonctorielle K-lin´eaire de πA (vue comme simple K-foncteur).
Supposons que s(f • g) = s(f) • s(g) pour tout couple d’endomorphismes (f ∈
¯
A⊕(A, A), g ∈¯
A⊕(B, B)), et que s(11) = 11. Alors s⊕d´eﬁnit une unique section
mono¨ıdale stricte de πA⊕.
D´emonstration. Il s’agit de v´eriﬁer l’identit´e s⊕(f • g) = s⊕(f) • s⊕(g) pour tout
couple (f ∈¯
A⊕(w1, w′
1), g ∈¯
A⊕(w2, w′
2)), et
s⊕(∅) = 1∅(ce second point est imm´ediat).
Nous utilisons transitoirement la notation w des mots de 13.4, dans le cas o`u la
structure mono¨ıdale est donn´ee par ⊕; au lieu de u(w), la somme directe (dans la
cat´egorie strictement K-lin´eaire A) des lettres de w sera not´ee
⊕w (
⊕
∅= 1). Via les
identiﬁcations canoniques
A⊕(w, w′) = A(
⊕w,
⊕w
′
),
on peut ´ecrire s⊕(f) = s(f), s⊕(g) = s(g), s⊕(f • g) = s(f • g).
Les identiﬁcations ci-dessus sont compatibles `a • (
⊕
\
w1 • w2 =
⊕w •
•plusw′).
On peut donc ´ecrire s⊕(f) • s⊕(g) = s(f) • s(g) (en revanche, on prendra garde
que s n’est pas suppos´ee stricte vis-`a-vis de ⊕, i.e. on ne suppose pas que le mor-
phisme canonique
⊕
\
s⊕(w) →s(
⊕w) soit l’´egalit´e).
L’hypoth`ese du lemme se traduit donc par l’identit´e s⊕(f • g) = s⊕(f) • s⊕(g)
dans
A⊕(w1 • w2, w1 • w2) = A(
⊕
w1 •
⊕
w2,
⊕
w1 •
⊕
w2)
pour tout couple d’endomorphismes (f ∈¯
A⊕(w1, w1), g ∈¯
A⊕(w2, w2)).
Or s⊕est strict vis-`a-vis de ⊕par construction (par contraste avec s).
Cela permet de ramener l’identit´e ci-dessus pour tout couple de morphismes
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
69
(f ∈
¯
A⊕(w1, w′
1), g ∈
¯
A⊕(w2, w′
2)) au cas d’un couple d’endomorphismes en
remplac¸ant w1 et w′
1 par w1 ⊕w′
1, et w2 et w′
2 par w2 ⊕w′
2.
□
Ce lemme nous ram`ene `a traiter d’endomorphismes, plutˆot que d’homomorphis-
mes.
Notation abr´eg´ee. Nous ´ecrirons A(A) (resp. R(A)) au lieu de A(A, A) (resp.
R(A, A)) dans ce paragraphe. Pour un objet A ∈A et a, b ∈A(A), nous noterons
comme d’habitude [a, b] = ab −ba le commutateur de a et b, et ad(a) l’application
b 7→[a, b].
13.6. Au cœur du probl`eme : d´emonstration de la proposition 13.4.2. Compte
tenu des lemmes pr´ec´edents, on suppose d´esormais que A est une petite cat´ego-
rie, strictement K-lin´eaire, mono¨ıdale stricte (notons que ¯
A a la mˆeme propri´et´e).
On proc`ede par ´etapes. Nous commencerons par d´emontrer c), cette d´emonstration
´etant la plus simple des trois et servant de prototype `a celles de a) et b).
13.6.1. D´ebut de la preuve de c). Soit s une section K-fonctorielle mono¨ıdale de
πA. On a donc des isomorphismes
A • B = s(A) • s(B)
˜sA,B
−−−−→s(A • B) = A • B.
Les ˜sA,B appartiennent `a 1+R(A•B) et v´eriﬁent la relation de coh´erence (dans
1 + R(A • B • C))
(13.3)
˜sA•B,C ◦(˜sA,B • 1C) = ˜sA,B•C ◦(1A • ˜sB,C).
Nous allons montrer :
13.6.1. Lemme. Il existe une famille double (u(r)
A )A∈A,r≥1, avec u(r)
A ∈1 + R(A),
ayant les propri´et´es suivantes :
(i)
On a u(r+1)
A
≡u(r)
A
(mod R(A)r) pour tout A ∈A et tout r ≥1.
(ii)
En posant
sr(f) = u(r)
B ◦s(f) ◦(u(r)
A )−1
pour A, B ∈A et f ∈¯
A(A, B), on a
(˜sr)A,B = u(r)
A•B ◦˜sA,B ◦(u(r)
A • u(r)
B )−1 ∈1 + R(A • B)r
pour tout couple d’objets (A, B).
Supposons le lemme 13.6.1 d´emontr´e. Pour tout A, choisissons un entier r(A)
tel que R(A)r(A) = 0. Posons
uA = u(r(A))
A
= u(r(A)+1)
A
= · · · ∈1 + R(A)
et
s′(f) = uB ◦s(f) ◦(uA)−1
pour A ∈A et f ∈¯
A(A). Pour A, B ∈A, on a donc
˜s′
A,B = (˜sr)A,B
d`es que r ≥sup(r(A), r(B), r(A • B)). De plus, le membre de droite de cette
´egalit´e est ´egal `a 1A•B. Ainsi, la section s′ v´eriﬁe les conclusions de c).
70
YVES ANDR´E ET BRUNO KAHN
Nous allons d´emontrer le lemme 13.6.1 par r´ecurrence sur r, partant du cas trivial
r = 1 o`u l’on prend u(1)
A = 1A pour tout A.
