---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-010-133-sorites
section_title: "Sorites"
section_number: 13.3
pages: 65-67
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
---
Pour cela, quelques sorites sont n´ecessaires.
13.3.1. Sorite. Soit (s, ˜s) : (B, ⊤) →(A, •) un foncteur mono¨ıdal, et soit u : s ⇒t
un isomorphisme naturel de s sur un autre foncteur t. Alors il existe une unique
structure mono¨ıdale ˜t sur t faisant de u un morphisme de foncteurs mono¨ıdaux.
D´emonstration. D´eﬁnissons
˜tA,B = uA⊤B˜sA,B(uA • uB)−1
(cf. (13.1)). Il faut voir que ˜t est compatible avec les contraintes d’associativit´e et
d’unit´e. Cela r´esulte de calculs triviaux (d’o`u le terme “sorite”), ce que nous laissons
au lecteur sceptique le soin de v´eriﬁer.
□
19Une cat´egorie mono¨ıdale v´eriﬁant cette hypoth`ese est appel´ee cat´egorie de Penrose dans [9].
C’est par exemple le cas si End(1) = K, ou en pr´esence d’un tressage.
66
YVES ANDR´E ET BRUNO KAHN
13.3.2. Sorite. Soient (A, •), ¯
A, πA comme dans le th´eor`eme 13.2.1. Alors le th´e-
or`eme 13.2.1 r´esulte de l’´enonc´e plus faible obtenu en remplac¸ant dans a) et b) le
mot “section” par “quasi-section”, o`u une quasi-section mono¨ıdale de πA est par
d´eﬁnition un foncteur mono¨ıdal s0 :
¯
A →A tel que πA ◦s0 soit naturellement
isomorphe `a Id ¯
A.
D´emonstration. Supposons donn´ee une telle quasi-section mono¨ıdale (s0, ˜s0). Soit
¯u : Id ¯
A
∼
−→πAs0 un isomorphisme naturel. Pour tout A ∈A, choisissons un
´el´ement uA ∈A(A, s0(A)) se projetant sur ¯uA, avec u1 = 11. D´eﬁnissons un
foncteur s : ¯
A →A par les formules :
s(A) = A
s(f) = u−1
B s0(f)uA
pour f ∈¯
A(A, B). Alors s est une section de πA naturellement isomorphe `a s0 via
u = (uA), et le sorite 13.3.1 montre qu’il lui est associ´e une unique structure mo-
no¨ıdale faisant de u un morphisme de foncteurs mono¨ıdaux. Ceci fournit la partie
a) du th´eor`eme 13.2.1, et le point concernant la partie b) est trivial.
□
13.3.3. Sorite. Soient (A, •), ¯
A, πA et (B, ⊤), ¯B, πB comme dans le th´eor`eme 13.2.1.
Soit (f, ˜f) : (B, ⊤) →(A, •) un K-foncteur mono¨ıdal tel que f soit une ´equivalence
de cat´egories. Alors f est radiciel, et les parties a) et b) du th´eor`eme 13.2.1 sont
vraies pour A si et seulement si elles sont vraies pour B.
D´emonstration. Le fait que f est radiciel est clair (et ne d´epend pas des structures
mono¨ıdales). Le reste de l’´enonc´e r´esulte du sorite 13.3.2, en remarquant que les
conditions dudit sorite sont manifestement invariantes par ´equivalence mono¨ıdale
de cat´egories mono¨ıdales.
□
13.4. Cat´egories mono¨ıdales strictes. Une petite cat´egorie mono¨ıdale (B, ⊤) est
dite stricte si l’ensemble des objets muni de la loi ⊤est un mono¨ıde (i.e. si ⊤est
strictement associative).
Un foncteur mono¨ıdal (s, (˜sAB)) : (A, •) →(B, ⊤) est dit strict si s(A)•s(B) =
s(A⊤B) et si ˜sAB est l’identit´e pour tout couple (A, B). C’est par exemple le cas
du foncteur identique.
Dans le cas strict, la situation se simpliﬁe pour les morphismes de foncteurs
mono¨ıdaux : si u : s ⇒s′ est un tel morphisme, alors il v´eriﬁe l’identit´e
uA•B = uA⊤uB
pour tout couple d’objets (A, B).
13.4.1. Remarque. Soit AA la cat´egorie des endofoncteurs additifs de A. Munie
de la composition, c’est une cat´egorie mono¨ıdale stricte. Pour toute cat´egorie mo-
no¨ıdale, le foncteur A 7→A•? de A vers AA admet une structure mono¨ıdale d´eﬁnie
par les contraintes d’associativit´e et d’unit´e. Ce foncteur est strict si et seulement si
(A, •) est mono¨ıdale stricte.
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
67
Si B est mono¨ıdale stricte, il en est alors de mˆeme de B⊕: en effet, rappelons que
les objets de B⊕sont des suites ﬁnies A = (A1, A2, . . . , Ar) d’objets de B, not´ees
A1 ⊕A2 ⊕· · · ⊕Ar (cf. §1.2) ; les composantes de A⊤A′ sont par d´eﬁnition les
Ai⊤A′
j, num´erot´ees selon l’ordre lexicographique. Il est clair qu’on obtient ainsi
une cat´egorie mono¨ıdale stricte. Si B est K-lin´eaire, les foncteurs ´evidents B⊕u⊕
→
←
v⊕B
(formation du mot `a une lettre, resp. parenth´esage canonique) sont sous-jacents `a
des foncteurs mono¨ıdaux stricts (vis-`a-vis de •).
Tout foncteur mono¨ıdal s : B →A, il induit, composante par composante, un
foncteur mono¨ıdal s⊕: B⊕→A⊕, strict si s l’est.
Une petite cat´egorie K-lin´eaire C sera dite strictement K-lin´eaire si son biproduit
⊕(et l’objet nul) fait de C une cat´egorie mono¨ıdale stricte. C’est le cas de B⊕, pour
toute petite K-cat´egorie B. Dans une cat´egorie strictement K-lin´eaire, les sommes
directes ﬁnies A1 ⊕· · · ⊕An sont d´eﬁnies sans ambig¨uit´e.
