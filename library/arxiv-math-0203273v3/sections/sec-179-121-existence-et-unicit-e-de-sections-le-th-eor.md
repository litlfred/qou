---
doc_id: arxiv-math-0203273v3
doc_title: "Nilpotence, radicaux et structures monoïdales"
section_id: sec-179-121-existence-et-unicit-e-de-sections-le-th-eor
section_title: "Existence et “unicit ´e” de sections. Le th´ eor` eme de structure fondamental"
section_number: 12.1
pages: 60-63
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "Nilpotence, radicaux et structures monoïdales — 302 sections: YVES ANDR ´E ET BRUNO KAHN; Introduction; YVES ANDR ´E ET BRUNO KAHN"
---
pour lesK-alg` ebres de Wedderburn (th´ eor` eme de Wedderburn) dit que toute exten-
sion d’uneK-alg` ebre s´ eparable de dimension ﬁnie par un id´ eal nilpotent se scinde.
En suivant la preuve cohomologique classique de Hochschild et Whitehead, nous
g´ en´ eralisons ce r´ esultat aux alg` ebres “` a plusieurs objets”.
12.1.1. Th ´eor`eme. SoitA une petite K-cat´egorie de Wedderburn, de radical R.
Posons ¯A =A/R. Alors :
a) LeK-foncteur de projectionπA :A→ ¯A admet une sections.
b) Si s′ est une autre section, il existe une famille (uA)A∈A,u A∈ 1A +R(A,A ),
telle que pour tousA,B∈A et toutf∈ ¯A(A,B ), on aits′(f ) = uBs(f )(uA)−1.
D´emonstration. 1) Supposons d’abordR2 = 0. AlorsR h´ erite d’une structure de
¯Ae-module par passage au quotient de l’action deA.
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 61
Pour toutA,B∈A , choisissons une sectionK-lin´ eaire
σA,B : ¯A(A,B )→A (A,B )
de la projection naturelle. SiC est un troisi` eme objet deA et si (f,g )∈ ¯A(A,B )×
¯A(B,C ), notons
γ(g,f ) = σA,C (gf )−σB,C (g)σA,B(f ).
C’est un ´ el´ ement deR(A,C ), et, si D est un quatri` eme objet eth∈ ¯A(C,D ),
on a la relation
γ(h,gf ) +hγ(g,f ) = γ(hg,f ) +γ(h,g )f.
Ain si γ d´ eﬁnit un2-cocycle de Hochschild de ¯A ` a valeurs dansR. D’apr` es le
§11, ce 2-cocycle est un 2-cobord ; autrement dit, il existe une fonctionρ telle que,
pour tousf,g composables, on ait
γ(g,f ) = ρ(gf )−gρ(f )−ρ(g)f.
La nouvelle section s(f ) = σ(f )−ρ(f ) v´ eriﬁe alorss(gf ) = s(g)s(f ) pour
tout couple (f,g ) composable.
2) Posonsδ(f ) = s′(f )−s(f )∈R (A,B ). On a, pour tout couple (f,g ) com-
posable,
δ(gf ) = δ(g)f +δ(f )g
doncδ est un 1-cocycle de Hochschild. C’est donc un cobordf↦→nBf−fn A pour
un choix convenable d’´ el´ ementsnA∈R (A,A ). En posant uA = 1 A +nA, on a
biens′(f ) = uBs(f )(uA)−1.
3) Supposons maintenantR nilpotent d’´ echelonr+1. On raisonne par r´ ecurrence
sur r, le cas r = 1 ´ etant trait´ e ci-dessus. SoitA(r) =A/Rr : le radicalR(r) =
R/Rr deA(r) est nilpotent d’´ echelonr, donc il existe une section ¯s : ¯A→A (r)
comme dans l’´ enonc´ e, et toute autre section s’en d´ eduit par “conjugaison” par une
famille de ¯uA∈ 1A +R(r)(A,A ).
Soit ¯s( ¯A) l’image d’une telle section ¯s dansA(r). Pour tout morphisme f dans
A, notonsf (r) son image dansA(r). Posons
˜A(A,B ) ={f∈A (A,B )|f (r)∈ ¯s( ¯A)(A,B )}
˜R(A,B ) =R(A,B )∩ ˜A(A,B ).
Alors ˜A est une sous-cat´ egorie (non pleine) deA, ˜R est son radical, ˜R2 = 0, et
˜A/ ˜R = ¯A. Il existe donc une section ˜s : ¯s( ¯A)→ ˜A ; la compos´ ees = ι◦ ˜s◦ ¯s :
¯A→ ¯s( ¯A)→ ˜A→A , o` uι est l’inclusion canonique, est la section cherch´ ee.
Sis′ est une autre section, notons ¯s′ la composition ¯A s′
→A→A (r), et soit (¯uA)
une famille d’´ el´ ements de1A +A(r)(A,A ) tels que ¯s′(f ) = ¯uB ¯s(f )(¯uA)−1 pour
toutf ∈A (r)(A,B ). Choisissons des relev´ esuA des ¯uA dansA(A,A ). Quitte ` a
changers′ en la section conjugu´ ee par les(uA)−1, on se ram` ene au cas o` u¯s′ = ¯s.
On conclut par l’´ etape2).
4) ´Etablissons maintenant l’assertiona) du th´ eor` eme dans le cas g´ en´ eral. Si l’on
supposaitA strictement de Wedderburn, il sufﬁrait de la voir comme limite projec-
tive desA(r) du num´ ero pr´ ec´ edent, cette limite ´ etant alors localement stationnaire
62 YVES ANDR ´E ET BRUNO KAHN
sur lesHoms, et d’appliquer directement ce num´ ero. Mais nous supposonsA seule-
ment de Wedderburn, ce qui complique la d´ emonstration.
Consid´ erons l’ensemble des couples(B,s ) form´ es d’une sous-cat´ egorie pleineB
deA et d’une section fonctorielles de la projectionB→ ¯B ( ¯B peut ˆ etre vue comme
sous-cat´ egorie pleine de¯A). Cet ensemble est non vide : d’apr` es les pas pr´ ec´ edents,
il contient par exemple des couples (B,s ) d` es queOb(B) est ﬁni.
On ordonne cet ensemble en d´ ecr´ etant que(B′,s′) ≺ (B,s ) siB′ ⊂ Bet si
s′ est la restriction de s ` a¯B′. Il est clair que cet ensemble ordonn´ e est inductif,
donc admet un ´ el´ ement maximal(B,s ) d’apr` es Zorn. D´ emontrons par l’absurde
queB =A. Sinon, soit X un objet deA qui n’est pas dansB. On peut remplacer
A par sa sous-cat´ egorie pleine dont les objets sontX et ceux deB, et il s’agit de
construire une extension des ` a¯A. Pour cela, on peut derechef remplacerA par toute
sous-cat´ egorie non pleineA′ ayant mˆ emes objets, et telle queA′/(A′∩R ) = ¯A.
Il y a un choix minimal d’une telle A′ : celle dont les morphismes sont des
sommes ﬁnies de compositions de ﬂ` eches des(B) et de ﬂ` eches deA de source ou
de butX. Le radical de cetteK-cat´ egorieA′ n’est autre queA′∩R : en effet, tous
les (A′∩R )(A,A ) sont des nil-id´ eaux, ce qui entraˆ ıne que(A′∩R )⊂ rad(A′) ;
r´ eciproquement,A′/(A′∩R ) = ¯A est semi-simple, donc rad(A′)⊂A′∩R .
Le point est queA′∩R est (globalement) nilpotent, ce qui permet, par le pas 3),
d’´ etendres comme souhait´ e. En fait, nous allons voir que sin est l’´ echelon de nilpo-
tence de l’id´ ealR(X,X ) deA(X,X ), alors rad(A′)(2n+1) = 0. En effet, comme le
radical des(B) est nul, on observe que pour tout couple d’objets (A,B ) deA, tout
´ el´ ement derad(A′)(A,B ) s’´ ecrit comme combinaison lin´ eaire ﬁnie∑ f i
XB◦gi
AX,
avec f i
XB ∈ A(X,B ),g i
AX ∈ A(A,X ). Tout ´ el´ ement derad(A′)(2n+1)(A,B )
s’´ ecrit comme somme ﬁnie de termes de la forme
∑
i1,i3,...,i2n+1
f i2n+1
XB gi2n+1
A2nX
(∑
i2n
f i2n
XA 2ngi2n
A2n−1X
)
f i2n−1
XA 2n−1...
(∑
i2
f i2
XA 2gi2
A1X
)
f i1
XA 1gi1
AX.
Or chaque fragmentgi2k+1
A2kX(∑
i2kf i2k
XA 2k
gi2k
A2k−1X)f i2k−1
XA 2k−1
est dans
A(A2k,X )◦ rad(A′)(A2k−1,A 2k)◦A (X,A 2k−1)⊂R (X,X ).
Comme ces fragments apparaissent n fois cons´ ecutives, on trouve bien que
rad(A′)(2n+1)(A,B ) = 0 . Ceci ach` eve la preuve de l’assertiona).
5) Un argument analogue s’applique pour l’assertionb). Soients ets′ deux sec-
tions ﬁx´ ees. Par Zorn, il existe une sous-cat´ egorie pleine maximaleB deA telle
que les restrictions de s et s′ ` a¯B soient conjugu´ ees au sens de l’assertion b).
Raisonnant par l’absurde comme ci-dessus, on peut encore supposer queOb(A) =
Ob(B)∪{X}. Quitte ` a conjuguers au-dessus de ¯B, on peut supposer que les re-
strictions de s et s′ ` a¯B co¨ ıncident. On observe alors ques et s′ prennent alors
leurs valeurs dans la sous-cat´ egorieA′ non pleine deA d´ eﬁnie comme ci-dessus.
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 63
Comme on l’a vu, son radical est globalement nilpotent, ce qui permet d’appliquer
le pas 3) et de conclure que s et s′ sont conjugu´ ees via une famille d’´ el´ ements
uA∈ 1A +R(A,A ). □
Le lemme suivant, souvent utile, r´ esulte imm´ ediatement de la proposition 2.3.4
b) et du fait que ¯A est semi-simple :
