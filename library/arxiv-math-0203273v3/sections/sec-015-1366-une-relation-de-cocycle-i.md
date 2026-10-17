---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-015-1366-une-relation-de-cocycle-i
section_title: "Une relation de cocycle, I"
section_number: 13.6.6
pages: 71-73
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
---
tenant en mesure d’interpr´eter (13.4) comme relation de 2-cocycle de Hochschild
pour l’alg`ebre K⟨Ob(A)⟩.
En effet, reprenons la famille (nA,B) ci-dessus. Avec les notations pr´ec´edentes,
on a une famille induite
¯nAB ∈R(AB)[r].
On d´eﬁnit alors une 2-cochaˆıne de Hochschild ¯n pour K⟨Ob(A)⟩`a valeurs dans
le K⟨Ob(A)⟩-bimodule R[r], en associant `a tout couple de mots non vides (w0, w1)
l’´el´ement ¯nw0,w1 ∈R[r] d´eﬁni par
¯nw0,w1(w) =
(
¯n •
w0,
•
w1
si w0w1 = w,
0
sinon.
Calculons le bord de Hochschild de ¯n :
(d2(¯n))w0,w1,w2 = w0 · ¯nw1,w2 −¯nw0w1,w2 + ¯nw0,w1w2 −¯nw0,w1 · w2.
Sa w-composante est nulle, par d´eﬁnition, si w0w1w2̸ = w. Si w0w1w2 = w,
elle est ´egale `a
1 •
w0 • ¯n •
w1,
•
w2 −¯n •
w0•
•
w1,
•
w2 + ¯n •
w0,
•
w1•
•
w2 −¯n •
w0,
•
w1 • 1 •
w2 = 0 d’apr`es (13.4).
Donc ¯n est un 2-cocycle. Comme K⟨Ob(A)⟩est une K-alg`ebre libre, c’est un
2-cobord, cf. [11, ch. IX, ex. 2 ou ch. X.5]. En d’autres termes, il existe une famille
d’´el´ements ¯mw ∈R[r] telle que l’on ait l’identit´e
¯nw0,w1 = w0 · ¯mw1 + ¯mw0 · w1 −¯mw0w1.
Soient A, B ∈A. Pour w0 = A, w1 = B, la composante de cette identit´e dans
R(w0w1)[r] n’est autre que
¯nAB = 1A • ¯mB −¯mA•B + ¯mA • 1B.
En relevant les ¯mA en des mA ∈R(A)r, on obtient la famille (u(r+1)
A
= 1A −
mA) cherch´ee.
72
YVES ANDR´E ET BRUNO KAHN
13.6.5. D´ebut de la preuve de a). Soit s une section K-fonctorielle de πA. L’exis-
tence en est garantie par le th´eor`eme 12.1.1.
Comme les End(1)-bimodules A(A, B) sont commutatifs par hypoth`ese, il est
loisible de remplacer chaque s(f) par s(11)−1 ◦s(f), et donc de supposer s(11) =
11.
En outre, d’apr`es la proposition 12.2.1 appliqu´ee `a B = A ⊠K A, il existe une
famille (uA,B ∈1A•B + R(A • B)) v´eriﬁant , pour tout (f, g) ∈¯
A(A) × ¯
A(B) :
s(f • g) = uA,B(s(f) • s(g))u−1
A,B.
Nous allons montrer :
13.6.2. Lemme. Il existe une famille double (u(r)
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
sr(f • g) ≡sr(f) • sr(g)
(mod R(A • B)r)
pour tout couple d’objets (A, B) et tout (f, g) ∈¯
A(A) × ¯
A(B).
L e lemme 13.6.2 implique a) de la mˆeme mani`ere que le lemme 13.6.1 impliquait
c). On proc`ede de nouveau par r´ecurrence sur r.
13.6.6. Une relation de cocycle, I. Supposons r ≥1 et trouv´ee une famille u(r)
A
v´eriﬁant la condition (ii) du lemme 13.6.2. Quitte `a remplacer s par sr, on peut
supposer sr = s, u(r) = 1. Posons
nA,B = uA,B −1A•B.
On a alors
ad(nA,B)(s(f) • s(g)) ∈R(A • B)r
pour tout (f, g) ∈¯
A(A) × ¯
A(B).
Soit h ∈¯
A(C). Nous allons calculer de deux fac¸ons s(f • g • h) modulo R(A •
B • C)r+1, compte-tenu de l’associativit´e stricte de •.
On a, modulo R(A • B • C)r+1,
s((f • g) • h) = s(f • g) • s(h) + [nA•B,C, (s(f) • s(g)) • s(h)]
= (s(f) • s(g)) • s(h) + [nA,B, s(f) • s(g))] • s(h)
+ [nA•B,C, (s(f) • s(g)) • s(h)]
= (s(f) • s(g)) • s(h) + [nA,B • 1C + nA•B,C, (s(f) • s(g)) • s(h)]
et de mˆeme
sr(f • (g • h)) =
s(f) • (s(g) • s(h)) + [1A • nB,C + nA,B•C, s(f) • (s(g) • s(h))].
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
73
Puisque A est mono¨ıdale stricte, on en d´eduit que
(13.6)
ad(1A • nB,C −nA•B,C + nA,B•C −nA,B • 1C)(s(f • g • h))
∈R(A • B • C)r+1
pour tous endomorphismes f, g, h comme ci-dessus.
D’autre part, si (u(r+1)
A
= 1 + mA)A∈A est une famille d’´el´ements comme dans
la conclusion du lemme 13.6.2 (donc mA ∈R(A)r pour tout A), un calcul analogue
donne l’identit´e
(13.7) ad(nA,B −mA • 1B −1A • mB + mA•B)(s(f) • s(g)) ∈R(A • B)r+1
pour (f, g) ∈¯
A(A) × ¯
A(B) ; r´eciproquement, la donn´ee d’´el´ements mA v´eriﬁant
(13.7) implique l’existence d’une famille u(r+1) comme dans l’´enonc´e du lemme
