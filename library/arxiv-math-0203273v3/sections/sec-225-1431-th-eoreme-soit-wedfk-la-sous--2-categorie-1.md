---
doc_id: arxiv-math-0203273v3
doc_title: "Nilpotence, radicaux et structures monoïdales"
section_id: sec-225-1431-th-eoreme-soit-wedfk-la-sous--2-categorie-1
section_title: "Th ´eor`eme. Soit Wedf{K} la sous- 2-cat´egorie 1-pleine et 2-pleine de"
section_number: 14.3.1
pages: 84-85
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "Nilpotence, radicaux et structures monoïdales — 302 sections: YVES ANDR ´E ET BRUNO KAHN; Introduction; YVES ANDR ´E ET BRUNO KAHN"
---
Wed{K} form´ee des cat ´egoriesA telles que dimKA(A,B ) < ∞ pour tout
(A,B )∈A×A .
a) Soit A ∈Wedf{K}. Alors il existe un K-groupo¨ıde afﬁne scind´e unipotent
Γ(A) = ( E,S ), transitif sur S, tel que pour toute extension L de K, on ait
S(L) = Ob(G(AL)) et E(s1,s 2)(L) = G(AL)(s1,s 2) pour tout couple de sec-
tions (s1,s 2) deπAL.
b) Cette construction provient d’un2-foncteur 1-contravariant et 2-covariant
∆ : Wedf{K}→ Hmg(Sch/K )
`a valeurs dans les K-espaces homog `enes unipotents, via le 2-foncteur
Hmg(Sch/K )→ Gr(Sch/K ) de 14.2.3.
c) Les 2-foncteurs ∆ et Γ commutent `a l’extension des scalaires.
D´emonstration. Compte tenu de l’hypoth` ese de ﬁnitude, pour tout objetA le fonc-
teur desK-alg` ebres commutatives vers les groupes
R↦→(1A +R(A,A )⊗KR,◦)
est repr´ esentable par unK-sch´ ema en groupes afﬁne unipotent UA. Soit UA =∏
A
UA leur produit ; c’est un K-groupe pro-unipotent, i.e. une limite projective
ﬁltrante lim
←−Uα deK-groupes unipotents ; en tant que sch´ ema, c’est juste un produit
d’espaces afﬁnes.
Pour tout couple (A,B ) d’objets deA, soit Sec(A,B ) l’ensemble des sections
K-lin´ eaires de la projectionA(A,B )→ ¯A(A,B ) : il est repr´ esentable par unK-
espace afﬁne Sec(A,B ). Posons SecA =∏
A,B Sec(A,B ) : c’est aussi un produit
d’espaces afﬁnes.
Consid´ erons le sous-sch´ ema ferm´ e deSec
SA ={(sA,B)|∀A,B,C ∈A,∀(f,g )∈ ¯A(A,B )× ¯A(B,C ),
sA,C(g◦f ) = sB,C (g)◦sA,B(f )}.
On a une action ´ evidente deUA surSA
µ : UA×KSA→SA
(u,s )↦→usu−1
qui est transitive grˆ ace au th´ eor` eme 12.1.1 b). Notons∆(A) ceK-espace homog` ene
unipotent : le groupo¨ ıdeΓ(A) cherch´ e est l’image de ∆(A) par le foncteur de
14.2.3.
Il reste ` a voir que∆ d´ eﬁnit un2-foncteur. SoitT :B→A un foncteur pleine-
ment ﬁd` ele : il induit un ´ epimorphismeUA→ →UB deK-sch´ emas afﬁnes grˆ ace au
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 85
diagramme ∏
A∈A
UA


↓
∏
B∈B
UB ∼−−−−→
∏
B∈B
UT (B)
et de mˆ eme un ´ epimorphismeSecA→ →SecB, ce dernier envoyant SA dans SB.
Ces morphismes d´ eﬁnissent clairement un morphisme de K-espaces homog` enes
∆( T ) : ∆(A)→ ∆(B).
SoitT′ un autre tel foncteur, et u : T ⇒ T′ un isomorphisme naturel, d’o` u un
autre ¯u : ¯T⇒ ¯T′, o` u¯T, ¯T′ : ¯B→ ¯A sont les foncteurs induits. Pour tout B∈B
et toute section s deπA, l’´ el´ ements(¯uB)−1uB appartient ` a1 +R(T (B),T (B)) :
on en d´ eduit un ´ el´ ementT−1(s(¯uB)−1uB)∈ 1 +R(B,B ). Cette r` egle d´ eﬁnit un
morphisme
∆( u) : SA→ UB
dont on v´ eriﬁe facilement qu’il satisfait les conditions d’une homotopie ∆( T )⇒
∆( T′). □
