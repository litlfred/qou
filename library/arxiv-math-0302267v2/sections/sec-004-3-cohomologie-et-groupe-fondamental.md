---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-004-3-cohomologie-et-groupe-fondamental
section_title: "Cohomologie et groupe fondamental"
section_number: 3
pages: 28-43
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
toc_source: inferred
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
3.1. Soit X un espace topologique s´epar´e et connexe. On note bPa l’ensemble des classes
d’homotopie de chemins de a `a b, et δγ la composition des chemins cPb × bPa →cPa. Noter
l’ordre des facteurs, choisi pour que si V est un syst`eme local sur X et que γv ∈Vb denote
le transport de v ∈Va le long de γ ∈bPa, on ait (δγ)v = δ(γv).
Nous ferons sur X les hypoth`eses (a) (b) (c) suivantes. (a) La th´eorie classique du π1
s’applique. Par exemple: X localement connexe par arcs et localement simplement connexe.
(b) Le groupe fondamental est de type ﬁni. (c) Pour une projection p: Xn×Xm →Xn et un
faisceau constant, Rp∗commute au passage aux ﬁbres. Ces conditions sont remplies pour
X hom´eomorphe au compl´ement dans un poly`edre ﬁni d’un sous-poly`edre, par exemple
pour X une vari´et´e alg´ebrique complexe.
Fixons un corps k, le corps des coeﬃcients. Soient a ∈X, Λ l’alg`ebre de groupe
k[π1(X, a)] et I son id´eal d’augmentation. La donn´ee d’un Λ-module `a gauche V , i.e. d’une
repr´esentation lin´eaire de π1(X, a) sur un k-espace vectoriel, ´equivaut `a celle d’un syst`eme
local V˜ sur X de ﬁbre V en a. Si on prend pour V le Λ-module Λ, on obtient le syst`eme
local de ﬁbre en x l’espace vectoriel k[xPa] de base xPa. La structure de Λ-module `a droite
de Λ en fournit une sur ce syst`eme local Λ˜, i.e. une action `a droite de π1(X, a). L’´el´ement γ
de π1(X, a) agit sur xPa par composition `a droite. Le syst`eme local (Λ/In)˜ est le quotient
Λ˜ ⊗Λ Λ/In de Λ˜.
Le syst`eme local (Λ/In)˜ est extension it´er´ee des n syst`emes locaux triviaux Ip/Ip+1
(0 ≤p < n). Sa ﬁbre (Λ/In)a˜ en a est Λ/In et l’unit´e 1 d´eﬁnit
(3.1.1)
k →(Λ/In)a˜: λ 7−→λ.1.
Le syst`eme local (Λ/In)˜ est universel parmi les syst`emes locaux E extension it´er´ee de
n syst`emes locaux triviaux et munis de k →Ea, car (Λ/In, 1) est universel parmi les
Λ-modules M tels que InM = 0 munis de m0 ∈M.
3.2. Dans ce qui suit, nous laisserons de nombreux signes ambigus. Plusieurs conventions
sont possibles, et aucune ne nous semble clairement meilleure. Elles n’importent gu`ere, car
26
elles conduisent `a des complexes isomorphe, avec pour l’isomorphisme au pis l’ambigu¨ıt´e
d’un signe global. Typiquement, changer de convention remplace un complexe par un autre
ayant les mˆemes composantes, et l’isomorphisme est donn´e par des signes d´ependant de
multidegr´es.
3.3. Fixons a, b ∈X et consid´erons dans Xn les sous-espaces b = t1, t1 = t2, . . ., tn = a,
not´es Y0, . . ., Yn. Pour J ⊂∆n := {0, 1, . . ., n}, soient YJ l’intersection des Yj (j ∈J) et
kJ le faisceau constant k sur YJ, prolong´e par z´ero sur Xn. Pour J ⊂K, on a YK ⊂YJ
et on dispose d’un morphisme de restriction kJ →kK. Si, pour K = {k0, . . ., kp}, les kℓ
´etant pris dans l’ordre croissant, et J = {k0, . . ., ˆki, . . ., kp}, on l’aﬀecte du signe (−1)i, on
obtient les composantes de la diﬀ´erentielle d’un complexe de faisceaux sur Xn:
(3.3.1)
k¯ →⊕k{j} →· · · →
⊕
|J|=p kJ →· · · →k∆n.
Noter que le dernier terme k∆n est nul sauf pour n = 0 ou a = b, auxquels cas il est
r´eduit `a k en t1 = . . . = tn = a. Si on supprime le premier terme et qu’on convient que les
degr´es vont de 0 `a n, on obtient la r´esolution ˇCechiste altern´ee du faisceau constant k sur
la r´eunion ∪Yi des Yi pour le recouvrement ferm´e ﬁni par les Yi, prolong´ee par 0 sur Xn.
D´eﬁnissons bKa ⟨n⟩, ou simplement bKa, comme ´etant le complexe (3.3.1), avec k∆n
omis, et les degr´es allant de 0 `a n. Si n > 0 et que a̸ = b, c’est une r´esolution du prolonge-
ment par 0 du faisceau constant k sur Xn −∪Yi, et
(3.3.2)
H∗(Xn, bKa) = H∗(Xn mod ∪Yi, k)
(pour n̸ = 0, a̸ = b)
Si a = b, la derni`ere diﬀ´erentielle (3.3.1) fournit un morphisme de complexes
aKa →kt1=···=tn=a[−n],
(3.3.3)
qui induit
Hn(Xn, aKa) →k.
(3.3.4)
27
Si on r´ep`ete ces constructions en prenant a et b comme param`etres, on obtient un
complexe ∗Ka sur X × Xn × X, et, pour p la projection X × Xn × X →X × X, la restric-
tion de ∗K∗`a Xn
∼
−→p−1(b, a) s’identiﬁe `a bKa. Traitant seulement b comme param`etre,
on obtient de mˆeme ∗Ka sur X × Xn. Les Hi(Xn, bKa) sont les ﬁbres du syst`eme local
Rip∗(∗K∗) sur X × X.
Nous allons, d’apr`es Beilinson, v´eriﬁer la
Proposition 3.4. (i) Pour i < n, Hi(Xn, bKa) = 0. (ii) Pour b variable, le syst`eme local
sur X des Hn(Xn, bKa), muni en b = a de (3.3.4), est le dual du syst`eme local (Λ/In+1)˜
de 3.1, muni du transpos´e de (3.1.1).
Preuve. Pour n = 0, Xn est r´eduit `a un point, bKa est le faisceau constant k en degr´e 0
et (i) (ii) sont clairs. Prouvons 3.4 par r´ecurrence sur n ≥1; l’hypoth`ese de r´ecurrence est
la validit´e de 3.4 pour m si m < n.
Soit q la premi`ere projection: Xn →X. Nous utiliserons la suite spectrale de Leray
pour q. Ceci revient `a ´ecrire que RΓ(Xn,
) = RΓ(X, Rq∗
) et `a ﬁltrer Rq∗par la ﬁltra-
tion canonique τ. Plus pr´ecis´ement, nous utiliserons une ﬁltration ayant une description
uniforme pour a = b ou a̸ = b, et qui revient `a la ﬁltration canonique si a̸ = b.
Un d´evissage montre que la formation de Rq∗bKa commute au passage aux ﬁbres. Si
on ´ecrit Xn comme X × Xn−1, bKa sur Xn s’identiﬁe au cˆone[−1] de
∗Ka ⟨n −1⟩→bKa ⟨n −1⟩
sur
{b} × Xn−1
(3.4.1)
⊕kt¯
=a
sur
{a} × Xn−1
(complexe simple associ´e au complexe double de premi`ere (resp. deuxi`eme) colonne la
source (resp. but) de (3.4.1)).
On reconnaˆıt `a gauche les kJ pour 0 /∈J et J̸ = {1, . . ., m}, `a droite les kJ d’une part
pour 0 ∈J, de l’autre pour J = {1, . . ., n}.
Si a̸ = b, la restriction de bKa `a q−1(t) = Xn−1 est donc: pour t̸ = a, b: tKa ⟨n −1⟩;
pour t = b: le cˆone[−1] de l’application identique de bKa ⟨n −1⟩; pour t = a: le cˆone[−1]
de (3.3.3). D’apr`es l’hypoth`ese de r´ecurrence, Riq∗bKa = 0 si i < n −1. Pour i = n −1,
28
c’est un sous-faisceau du syst`eme local (Λ/In)˜
∨. Il co¨ıncide avec (Λ/In)˜
∨si t̸ = a, b, est
nul en t = b et la ﬁbre en a est le noyau du transpos´e de (3.3.1). Pour i ≥n, Riq∗bKa est un
syst`eme local sur X −{b} prolong´e par 0 sur X. La suite spectrale de Leray v´eriﬁe donc
Epq
2 = 0 pour q ≤n −2 ou p = 0, et
Hi(Xn, bKa) = 0
pour
i < n
(3.4.2)
Hn(Xn, bKa) = H1(X, Rn−1q∗bKa)
(pour a̸ = b).
Ce H1 est le groupe des extensions du faisceau constant k par (Λ/In)˜
∨, trivialis´ees en
t = b, et trivialis´ees apr`es avoir pouss´e par (Λ/In)∨→k en t = a. Dualement, c’est le
groupe des extensions eE de (Λ/In)˜ par k, trivialis´ees en t = b, et trivialis´ees au-dessus de
k ⊂Λ/In en t = a.
Traduisons en termes de Λ-modules. A eE correspond un Λ-module E, extension de
Λ/In par le module d’augmentation k. Il est annul´e par In+1. La donn´ee additionelle
en a est celle d’un rel`evement ˜1 du g´en´erateur 1 de Λ/In dans E. Soit α: In/In+1 →k
la restriction `a In/In+1 du morphisme de Λ/In+1 dans E: λ 7→λ˜1. L’extension E est
l’extension Eα de l’extension Λ/In+1 de Λ/In par In/In+1 en poussant par α:
(3.4.3)
0 −→In/In+1 −→Λ/In+1 −→
Λ/In
−→0
yα
y
y
0 −→
Q
−→
E
−→Λ/In+1 −→0.
Pour α: In/In+1 →k. L’extension Eα˜ de (Λ/In)˜ par le syst`eme local trivial k se
d´eduit de (Λ/In+1)˜ en poussant par
α: (syst`eme local trivial In/In+1) →k.
La trivialisation β en b fournit un diagramme
(3.4.4)
0 −→In/In+1 −→(Λ/In+1)b˜ −→(Λ/In)b˜ −→0
yα
y

0 −→
Q
−→
(Eα)b˜
β
⇆(Λ/In)b˜ −→0.
29
De α et β on d´eduit une forme lin´eaire γ sur (Λ/In+1)b˜: `a x ∈(Λ/In+1)b˜, d’image ¯x dans
(Λ/In)b˜, attacher
γ(x) := image(x) −β(¯x) ∈Q ⊂(Eα˜)b.
On a α = γ|(In/In+1), et γ d´etermine β. Ceci fournit l’isomorphisme
Hn(Xn, bKa) = ((Λ/In+1)b˜)
∨
annonc´e.
Pr´esent´es un peu diﬀ´erement, ces arguments continuent `a s’appliquer pour a = b.
L’image par Rq∗du complexe bKa, cˆone[−1] de (3.4.1) est encore un cˆone[−1]. On d´eﬁnit
sa ﬁltration croissante Fil en ﬁltrant source et but par la ﬁltration canonique τ ≤. Le gradu´e
GrFil
i
s’envoie par un quasi-isomorphisme sur le complexe
(3.4.5)
Riq∗∗Ka ⟨n −1⟩→(sa ﬁbre en a)a ⊕(k si i = n −1)
en degr´es 0 et 1, translat´e par [−i]. Pour i < n−1, (3.4.5) est nul. Pour tout i, H0((3.4.5)) =
0. La suite spectrale pour RΓ(X,
) et Fil donne donc
Hi(Xn, bKa) = 0
pour i < n
(3.4.6)
Hn(Xn, bKa) = H1(X, (3.4.5)i=n−1).
Ce H1 classiﬁe les extensions du faisceaux constant k par (Λ/In)˜
∨= Rn−1q∗∗Ka ⟨n −1⟩,
trivialis´ees apr`es avoir pouss´e par le morphisme (3.4.5), et les arguments donn´es pour a̸ = b
peuvent ˆetre r´ep´et´e.
Il reste, pour a = b, `a identiﬁer (3.3.4). Le complexe (3.3.1) (degr´es 0 `a n + 1) est le
complexe simple associ´e au complexe triple de faisceaux sur Xn = X × Xn−1:
∗Ka ⟨n −1⟩
−−−−→aKa ⟨n −1⟩sur q−1(a)
y
y
k[−(n −1)]t¯
=a
∼
−−−−→
k[−(n −1)]t¯
=a
30
et (3.3.4) est induit par le morphisme
∗Ka ⟨n −1⟩
−−−−→aKa ⟨n −1⟩sur pr−1(a)
y
y
k[−(n −1)]t¯
=a −−−−→
0
−→
0 −−−−→
0
y
y
0 −−−−→k[−(n −1)].
Filtrant comme pr´ec´edemment, on en d´eduit que (3.2.1) est le H1 du morphisme de
complexes
(Λ/In)∨˜ −−−−→(Λ/In)a˜ ⊕ka
y
y
0
−−−−→
ka
(La ﬂ`eche verticale droite donnant le morphisme est la diﬀ´erence entre l’´evaluation sur
k ⊂Λ/In et l’identit´e de ka.)
Une extension de k par (Λ/In)∨˜, trivialis´ee apr`es avoir poun´e par (3.3.4), se dualise
en une extension de (Λ/In)˜ par k qui en a est et trivialis´ee, et trivialis´ee au-desus de
k ⊂Λ/In = (Λ/In)a˜. On lui attache la diﬀ´erence au-desus de k entre ces deux triviali-
sations. On laisse au lecteur le soin de v´eriﬁer que cela revient `a ´evaluer en 1 une forme
lin´eaire sur Λ/In+1.
3.5 Remarque. Dans cette identiﬁcation de (k[bPa] ⊗Λ Λ/In+1)∨avec le groupe des
extensions de (Λ/In)˜ par k, munies de trivialisations convenables en a et b, le sous-espace
(k[bPa] ⊗Λ Λ/In)∨est celui des extensions triviales, avec la trivialisation ´evidente en a et
une trivialisation en b. L’injection de (k[bPa]/In)∨→(kaPb]/In+1)∨est donc le Hn de
(3.5.1)
 bKa ⟨n −1⟩sur {b} × Xn+1
[−1] →bKa sur Xn
d´eduit de la description du second membre comme cˆone[−1] de (3.4.1).
3.6. Nous regarderons un objet simplicial tantˆot comme un foncteur contravariant sur
la cat´egorie de tous les ensembles totalement ordonn´es ﬁnis non vides, tantˆot comme un
foncteur sur la sous-cat´egorie des ∆n = {0, . . ., n}. Cela revient au mˆeme (´equivalence
de cat´egories). Si la valeur sur ∆n d’un objet simplicial S est not´ee Sn, on notera SI sa
31
valeur sur I totalement ordonn´e. Elle est fonctorielle en I et si I a n + 1 ´el´ement, l’unique
isomorphisme de I avec ∆n fournit un isomorphisme de SI avec Sn.
Le morphismes ∆n →∆1 sont les
(3.6.1)
ϕi: 0, . . ., i −1 7−→0; i, . . ., n 7−→1
(0 ≤i ≤n + 1).
Nous identiﬁerons par cette num´erotation XHom(∆n,∆1) `a X×Xn×X. L’ensemble simplicial
∆n 7→Hom(∆n, ∆1) contient l’ensemble simplicial ∆n 7→Hom(∆n, ∂∆1) = {ϕ0, ϕn+1}.
L’espace cosimplicial ∆n 7→XHom(∆n,∆1) se projette donc sur l’espace cosimplicial ∆n 7→
XHom(∆n,∂∆1) = X × X. Prenant la ﬁbre en (b, a), on obtient un espace cosimplicial
∆n 7→Xn. Les ∂i: Xn−1 →Xn (0 ≤i ≤n) sont les
t1, . . ., tn−1 7−→b, t1, . . ., tn−1
(i = 0)
t1, . . ., ti, ti, . . ., tn−1
(i̸ = 0, n)
t1, . . ., tn−1, a
(i = n) ,
d’images les Yi de 3.3. Plus g´en´eralement, pour J ⊂{0, . . ., n} de compl´ement I, suppos´e
non vide, p = |I|−1 et ϕI l’inclusion de I, le morphisme cosimplicial ϕI: Xp →Xn identiﬁe
Xp avec YJ ⊂Xn. Pour J, J′ de compl´ements I, I′ et p = |I|−1, p′ = |I′|−1, si J ⊂J′ et
que ϕII′ est l’inclusion de I′ dans I, le morphisme cosimplicial ϕII′: Xp′ →Xp s’identiﬁe
`a l’inclusion de YJ′ dans YJ. Noter que pour J = {j0, . . ., ˆk, . . ., jp} ⊂J′ = {j0, . . ., jp}
donnant lieu `a I′ = {i0, . . . ,ˆıℓ, . . ., iq} ⊂I = {i0, . . ., iq} (les i et j sont pris dans l’ordre
croissant), on a p + q = n, k + ℓ= iℓ= jk, et le signe (−1)k que nous avons employ´e en
3.3 peut se r´ecrire
(−1)k = (−1)ℓ· (−1)jk = ε(J)(−1)ℓε(J′)
pour
(3.6.2)
ε(J) =
Y
j∈J
(−1)j.
32
3.7. Choisissons des complexes S∗
m qui calculent la cohomologie des Xm, et soient fonc-
toriels pour les morphismes cosimpliciaux entre les Xm. Plus pr´ecis´ement: on prend pour
S∗
m le complexe des sections globales d’une r´esolution fonctorielle S∗
m du faisceau constant
k sur Xm, telle que Γ(Xm, S∗
m) →RΓ(Xm, S∗
m) soit un quasi-isomorphisme. A m variable,
les S∗
m forment un syst`eme simplicial de complexes. Les S∗
m fournissent une r´esolution de
bKa ⟨n⟩sur Xn: avec les notations de 3.6, r´esoudre kJ par ϕI∗S∗
I et utiliser la fonctorialit´e
de S∗
I en I.
Un syst`eme de coeﬃcients c sur le simplexe standard ∆n, `a valeurs dans une cat´egorie
additive, attache `a chaque facette F ⊂∆m un objet c(F), contravariant en F pour les
morphismes d’inclusion. Il d´eﬁnit un complexe de chaˆınes
Cp(∆n, c) =
M
|F |=p+1
c(F).
Dualement, un cosyst`eme: c(F) covariant en F, d´eﬁnit un complexe de cochaˆınes.
Si s• est un objet simplicial, on note encore C∗(∆n, s•) le complexe C∗(∆n, c) pour
c(F) := sF . Dualement pour s• cosimplicial.
Le complexe
Γ(Xn, r´esolution de bKa d´eﬁnie par S•),
calcule l’hypercohomologie de bKa. Il s’identiﬁe (avec les signes (3.6.2)) au complexe simple
associ´e au complexe double (= complexe de complexes)
C∗(∆n, S∗
•),
translat´e par [−n], et 3.4 (ii) se r´ecrit
(3.7.1)
(k[bPa] ⊗Λ Λ/In+1)
∨= H0C∗(∆n, S∗
•).
3.8 Exemple: prenons pour S∗
m le complexe des cochaˆınes singuli`eres de Xm. Il ne rentre
pas tout `a fait dans le cadre pr´ec´edent, mais on peut l’y ramener: si S∗
m est le complexe
des cochaˆınes singuli`eres localis´ees sur Xm (le faisceau associ´e au pr´efaisceau des cochaˆınes
singuli`eres), S∗
m →Γ(Xm, S∗
m) est un quasi-isomorphisme. Le complexe S∗
m des cochaˆınes
33
singuli`eres est le dual du complexe Sm
∗
des chaˆınes singuli`eres. A m variable, Sm
∗
est
cosimplicial en m, et C∗(∆n, S∗
•) est le dual de C∗(∆n, S•
∗). On a donc
(3.8.1)
k[bPa] ⊗Λ Λ/In+1 = H0C∗(∆n, S
•
∗)
Pour X = [0, 1], a = 0 et b = 1, bPa est r´eduit `a un ´el´ement et chaque k[bPa]⊗ΛΛ/In+1
est r´eduit `a k. Au membre de gauche, les C∗(∆n, S•
∗) forment un syst`eme projectif, de
morphismes de transition d´eduit, apr`es dualisation, de (3.5.1
):
C∗(∆n, S
•
∗) →C∗(∆n−1, S
•
∗)
est induit par ∂0: ∆n−1֒ →∆n.
Pour qu’un cocycle de degr´e zero de C∗(∆n, S•
∗) corresponde au chemin de 0 `a 1, il faut
et il suﬃt que sa valeur en {n} = ∂n
0 (∆0) ⊂∆n soit 1 ∈S0, le complexe des chaˆınes sin-
guli`eres du point. On a [0, 1] = |∆1|. Soit σm le simplexe |∆m| →|∆1|m = [0, 1]m de coor-
donn´ees les d´eg´en´erescences ϕi (1 ≤i ≤m) de (3.6.1). Son image est {t¯|1 ≥t1 ≥. . . ≥tm ≥0}.
Comme cocycle, on peut prendre celui qui `a chaque face de dimension p de ∆n attache
±σp, le signe ´etant + pour p = 0 et d´ependant des conventiones de signes d´eﬁnissant
C∗(∆n, S•
∗) pour p > 0.
Par fonctorialit´e en X, on en d´eduit que, pour X, l’image dans H0C∗(∆n, S∗) d’un
chemin γ: [0, 1] →X de a `a b est repr´esent´ee par le cocycle qui `a chaque face de dimension
p de ∆n attache ±γ ◦σp: |∆p| →[0, 1]p →Xp, le signe ´etant comme ci-desssus.
3.9. La litt´erature donne une autre recette pour d´eduire (k[bPa] ⊗Λ Λ/In+1)∨de l’objet
simplicial S∗
• de la cat´egorie des complexes consid´er´e en 3.7:
(a) prendre le complexe normalis´e NS∗
• de cet objet simplicial;
(b) prendre le tronqu´e σ ≥−nNS∗
• qui ne garde que les NS∗
m pour m ≤n;
(c) prendre le complexe simple associ´e au complexe double σ ≥−nNS∗
• et son H0.
L’´equivalence entre les deux constructions r´esulte du lemme suivant. Rappelons qu’une
cat´egorie karoubienne est une cat´egorie additive dans laquelle tout endomorphisme idem-
34
potent admet un noyau, et que l’´equivalence de Dold-Puppe: (objet simplicial S•)→(com-
plexe NS• `a degr´es ≤0) est disponible dans une telle cat´egorie (NSk est facteur direct de
Sk)
Proposition 3.10. Si S• est un objet simplicial d’une cat´egorie karoubienne, le complexe
C∗(∆n, S•) et le tronqu´e normalis´e σ ≥−nNS• sont fonctoriellement homotopes.
Nous v´eriﬁerons par la m´ethode des mod`eles acycliques l’´enonc´e dual, pour un objet
cosimplicial S•, σ ≤nNS• et C∗(∆n, S•).
Preuve. Nous noterons CZ la cat´egorie pr´eadditive ayant les mˆemes objets qu’une cat´egorie
C, pour laquelle Hom(A, B) est le groupe ab´elien librement engendr´e par HomC(A, B). Nous
noterons Ckar son enveloppe karoubienne, obtenue par adjonction formelle de sommes ﬁnies
et de facteurs directs noyaux d’endomorphismes idempotents. Le foncteur contravariant
X 7−→hX
Z : Ckar →Hom(C, Ab),
hX
Z (Y ) = HomCkar(X, Y )
est pleinement ﬁd`ele. Il induit une ´equivalence de Ckar avec la sous-cat´egorie de la cat´egorie
ab´elienne Hom(C, Ab) d’objets les facteurs directs de sommes ﬁnies de foncteurs
Y 7−→groupe ab´elien librement engendr´e par HomC(X, Y ),
pour X dans C. Ces foncteurs sont des objets projectifs de la cat´egorie ab´elienne Hom(C, Ab),
car pour C dans C
Hom(hC
Z , F) = F(C)
(variante du lemme de Yoneda).
Si ∆est la cat´egorie des ∆n, l’objet cosimplicial (∆n) de ∆kar est universel en ce sens
que, pour A une cat´egorie karoubienne, F 7→F((∆n)) est un ´equivalence
(foncteurs ∆kar →A) →(objets cosimpliciaux de A)
Pour v´eriﬁer l’´enonc´e (3.10)∗dual de 3.10, et montrer que l’´equivalence d’homotopie peut
ˆetre donn´ee par des formules universelles, il suﬃt de v´eriﬁer (3.10)∗dans le cas universel:
35
pour l’objet (∆n) de ∆kar. Si ∆≤n est la sous-cat´egorie de ∆d’objets les ∆m pour m ≤n,
tant σ ≥−nN∆• que C∗(∆n, ∆•) sont dans (∆≤n)kar, et c’est dans (∆≤n)kar que nous
travaillerons.
Appliquons le foncteur X 7→hX
Z `a σ ≤nN∆• et `a C∗(∆n, ∆•). On obtient deux com-
plexes d’objets projectifs de la cat´egorie ab´elienne Hom(∆≤n, Ab). Nous montrerons qu’il
sont l’un et l’autre une r´esolution projective du foncteur constant Z, donc sont homotopes,
et on conclut par la pleine ﬁd´elit´e de X 7→hX
Z . Si on ´evalue en ∆p (p ≤n), on obtient les
complexes σ ≥−nNS• et C∗(∆n, S•) de 3.10 pour S• le complexe chaˆınes simpliciales de
∆p. Ce sont
(a) le complexe des chaˆınes non d´eg´en´er´ees de ∆p, ´egal `a son tronqu´e car p ≤n.
(b) le complexe des chaˆınes combinaisons lin´eaires de ∆q →∆n × ∆p, avec la premi`ere
projection injective.
Ces deux complexes sont augment´es vers Z, fonctoriellement en ∆p. Puisque |∆p|
est contractile, et que le complexe (a) calcule son homologie, il est une r´esolution de Z.
Le complexe (b) est le complexe des chaˆınes non d´eg´en´er´ees du sous-polytope simplicial
suivant de |∆n × ∆p|:
(3.10.1)
la r´eunion, pour ϕ: ∆n →∆p, des graphes Γϕ des morphismes |ϕ|: |∆n| →|∆p|.
Pour v´eriﬁer que le complexe (b) est une r´esolution de Z, il suﬃt donc de v´eriﬁer le
Lemme 3.10.2. L’espace (3.10.1) est contractile.
Preuve. Ordonnons lexicographiquement l’ensemble des applications croissantes
ϕ: {0, . . ., n} →{0, . . ., p}.
Montrons que pour tout ϕ̸ = 0,
Γϕ ∩
[
ϕ′<ϕ
Γϕ′
est une union non vide de faces du simplexe Γϕ, mais non de toutes les faces de Γϕ, de
sorte que
S
ϕ′<ϕ
Γϕ′ est r´etracte par d´eformation de
S
ϕ′ ≤ϕ
Γϕ′.
36
Quels que soient ϕ′ et ϕ, si F ⊂{0, . . ., n} est l’ensemble des i tels que ϕ(i) = ϕ′(i),
et |F| la facette correspondante ∆m, Γϕ ∩Γϕ′ est le graphe de la restriction de |ϕ| ou |ϕ′|
`a |F|.
Identiﬁons Γϕ `a |∆m| par la projection sur ∆m. Si ϕ′ < ϕ, soit i minimal tel que
ϕ′(i) < ϕ(i). Si ϕ′′ est d´eﬁni par ϕ′′(j) = ϕ′(j) (resp. ϕ(j)) pour j ≤i (resp. j > i), on
a ϕ′′ < ϕ et Γϕ ∩Γϕ′ ⊂Γϕ ∩Γϕ′′, qui s’identiﬁe `a la face d’indice i de |∆m|. L’intersection
Γϕ ∩
S
ϕ′<ϕ
Γϕ′ est donc r´eunion non vide de faces.
Pour que la face d’indice i soit obtenue, il faut et il suﬃt que ϕ(i)̸ = 0, et que, si
i̸ = 0, on ait ϕ(i −1) < ϕ(i). Parce que n ≥p, toute les faces ne sont pas obtenues: soit
ϕ(i) = ϕ(i + 1) pour un i, soir n = m, ϕ est l’identit´e, et ϕ(0) = 0.
3.11. Si X est une vari´et´e diﬀ´erentiable, que k = R et que, dans 3.7, on calcule la coho-
mologie de Xn `a l’aide du complexe de de Rham, on obtient un objet simplicial Ωp(Xn) de
la cat´egorie des complexes (degr´e diﬀ´erentiel gradu´e p, degr´e simplicial n). Soit NΩ∗(X∗)
son normalis´e, et sNΩ∗X∗le complexe simple associ´e, dont la composante de degr´e k est
⊕
p−n=k NΩp(Xk). C’est un proche cousin du complexe des int´egrales it´er´ees de Chen. Nous
nous proposons d’expliquer la relation entre les deux.
Une q-forme β sur l’espace bΩa(X) des chemins C∞de a `a b est pour Chen la donn´ee,
pour toute vari´et´e U et toute famille C∞: U →bΩa(X) de chemins de a `a b param´etr´ee
par U, d’une q-forme (not´ee γ∗β) sur U, cette donn´ee v´eriﬁant que pour f: V →U on a
(γf)∗β = f ∗(γ∗β). A une p-forme sur Xn, Chen attache comme suit une (p−n)-forme sur
bΩa(X):
(a) r´ep´etant avec param`etres la construction de 3.8, on attache `a une famille γ de chemins
param´etr´ee par U un morphisme
γn = γ ◦σn: U × |∆n| →U × [0, 1]n →Xn;
(b) `a la forme α sur Xn on attache l’int´egrale de γ∗
nα le long des ﬁbres de U × |∆n| →U.
Plus pr´ecis´ement, on attache
⟨α⟩= (−1)n(n+1)/2
Z
U×|∆n|/U
γ∗
nα,
37
o`u l’int´egrale le long des ﬁbres est d´eﬁnie de sorte que pour β′ sur U et β′′ sur |∆n|, on ait
Z
U×|∆n|/U
pr∗
1β′ ∧pr∗
2β′′ = β′.
Z
|∆n|
β′′.
Le signe est choisi pour avoir, si α est de degr´e p
d ⟨α⟩= ⟨dα⟩+ (−1)p DX
(−1)ij∗
i α
E
:
compatibilit´e de la diﬀ´erentielle ext´erieure sur bΩa(X) avec la diﬀ´erentielle D du complexe
simple associ´e au complexe double des Ω∗(Xn) (pour * le premier degr´e).
Pour la diﬀ´erentielle transpos´ee de Sing∗X∗, si γ est un chemin de a `a b, c’est
P(−1)pγ ◦σp qui est un cycle.
Chen remplace les Ω∗Xn par le syst`eme simplicial de sous-complexes
n⊗Ω∗(X). Le
complexe des int´egrale it´er´ees de Chen est l’image par ⟨
⟩de la somme des
n⊗Ω∗(X).
Cette image est form´ee des sommes de
⟨α1| . . .|αn⟩:= ⟨pr∗
1α1 ∧. . . ∧pr∗
nαn⟩.
Les d´eg´en´erescences si: Xn →Xn−1 sont les projections (x1 . . . xn) →(x1 . . . ˆxi . . . xn)
et le complexe normalis´e de
n⊗Ω∗X, dans sa version “diviser par les Im(si)” est
(3.11.1)
N
n⊗Ω∗X =
n⊗(Ω∗X/constantes).
Par K¨unneth, les
n⊗Ω∗X sont quasi-isomorphes aux Ω∗Xn, et donc les N
n⊗Ω∗X aux
NΩ∗Xn.
Si un des αi est de degr´e 0, ⟨α1| . . .|αn⟩est nul et ⟨
⟩induit donc
⟨
⟩: N
n⊗Ω∗X →complexe des int´egrales it´erees.
Les deux membres sont ﬁltr´es par n; par les
⊕
m ≤n N
m⊗Ω∗X et leurs images. Chen (1973)
(Lemme 4.3.1) prouve que, pour cette ﬁltration Fil du complexe des int´egrales it´eries, GrFil
n
est le quotient
n⊗(τ ≥1Ω∗X) de
n⊗Ω∗X. Le complexe τ ≥1Ω∗X est le quotient de Ω∗X par
38
Ω0X et son image par d. La vari´et´e X ´etant connexe, le morphisme de (Ω∗X/constantes)
dans τ ≥1Ω∗X est un quasi-isomorphisme, et les
FilnN
n⊗Ω∗X →Filn(int´egrales it´er´ees)
sont donc des quasi-isomorphismes.
Remarque. On peut donner du complexe des int´egrales it´er´ees une description directe, en
terme de l’alg`ebre gradu´ee Ω∗(X) et des morphismes d’´evaluation en a et b, sans invoquet
les formes diﬀ´erentielles sur bΩa: l’image de
⊕
m ≤n
m⊗Ω∗
X est son quotient par les α1⊗. . .⊗αm
tels qu’un αi soit de degr´e 0, et leurs diﬀ´erentielles (construction bar r´eduite de Chen 1976).
3.12. Soit X une vari´et´e alg´ebrique lisse connexe sur un corps K et a, b ∈X(K). Comme
dans le cas topologique 3.6, le sch´ema cosimplicial XHom(∆n,∆1) s’envoie dans le sch´ema
cosimplicial constant X × X = XHom(∆n,∂∆1) et, prenant la ﬁbre en (b, a) ∈X × X, on
obtient un sch´ema cosimplicial ∆n 7→Xn. Regardons-le comme un objet cosimplicial de
la cat´egorie additive SmCor(K). Quel que soit n, on peut lui attacher le complexe
C∗(∆n, X∗)[n]
(3.7) de SmCor(K), ou, dans l’enveloppe karoubienne SmCor(K)kar de SmCor(K), le com-
plexe homotope σ ≤nNX∗. Ces complexes fournissent des objets, naturellement isomorphes
d’apr`es 3.10, de la cat´egorie triangul´ee motivique DM(K). Notons les bΩ[n]
a (X).
Appliquons `a bΩ[n]
a (X) le foncteur “r´ealisation” cohomologique, suivi de H0. D’apr`es
3.4, pour tout plongement complexe σ de K, dans la r´ealisation de Betti Hσ correspondante
(coeﬃcients rationnels), on obtient (Q[bPa] ⊗Λ Λ/In+1)∨pour X(C).
Supposons que X, comme objet de DM(K), soit de Tate mixte, i.e. dans DMT(K).
Les bΩ[n]
a (X) sont alors ´egalement dans DMT(K). Si K est un corps de nombres, ou plus
g´en´eralement quand on dispose de la conjecture d’annulation de Beilinson-Soul´e, on peut,
apr`es tensorisation avec Q, appliquer H0 et dualiser pour obtenir un objet de la cat´egorie
MT(K) des motifs de Tate mixtes sur K.
39
Si on travaille avec σ ≤nNX∗, les formules classiques en topologie (voir Wojtkowiak
(1993)) fournissent, apr`es passage `a la limite inductive en n, une structure d’alg`ebre com-
mutative dans la cat´egorie des Ind-objets de MT(K), et
bAa(X) := colim
n
(H0σ ≤nNX∗)
∨
m´erite le nom d’alg`ebre aﬃne de l’espace motivique des chemins de a `a b. Pour trois points
a, b, c, on dispose aussi (loc. cit.)d’un coproduit
cAa(X)(X) →cAb(X) ⊗bAa(X)
correspondant `a la composition des chemins. Pour a = b, Spec(aAa(X)) est le groupe
fondamental rendu unipotent motivique.
3.13. Prenons pour X le compl´ement, dans une droite projective P sur K, d’un ensemble
ﬁni de points rationnels, et montrons comment comparer ces constructions `a celles de
Deligne (1989). En r´ealisation de de Rham, X fournit le complexe (`a diﬀ´erentielle nulle)
des formes diﬀ´erentielles `a pˆoles logarithmiques:
(3.13.1)
K
0
−→Ω1
P (log S).
Pour Xn, on obtient la uissance tensorielle ni`eme de (3.13.1). Ces puissances tensorielles
forment un syst`eme simplicial de complexes. Normalisant, ce qui revient `a supprimer K
dans (3.13.1) (cf. (3.11.1)), on obtient apr`es troncation en n
(3.13.2)
⊕
m ≤n Ω1
p(log S)⊗m.
La comparaison avec la r´ealisation de Betti est par les int´egrales it´er´ees de Chen, et ceci
est compatible aux constructions de Deligne (1989). Quant `a la r´ealisation en cohomologie
ℓ-adique, les arguments prouvant 3.4 s’appliquent aussi bien dans le cadre ℓ-adique.
40
