---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-019-32-dans-ce-qui-suit-nous-laisserons-de-nombreux
section_title: "Dans ce qui suit, nous laisserons de nombreux signes ambigus . Plusieurs conventions"
section_number: 3.2
pages: 28-31
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
sont possibles, et aucune ne nous semble clairement meilleu re. Elles n’importent gu` ere, car
26
elles conduisent ` a des complexes isomorphe, avec pour l’is omorphisme au pis l’ambigu ¨ ıt´ e
d’un signe global. Typiquement, changer de convention remplace un complexe par un autre
ayant les mˆ emes composantes, et l’isomorphisme est donn´ epar des signes d´ ependant de
multidegr´ es.
3.3. Fixons a, b ∈ X et consid´ erons dansX n les sous-espaces b = t1, t1 = t2, . . . , tn = a,
not´ esY0, . . . , Yn. Pour J ⊂ ∆ n := {0, 1, . . . , n}, soient YJ l’intersection des Yj (j ∈ J) et
kJ le faisceau constant k sur YJ , prolong´ e par z´ ero surX n. Pour J ⊂ K, on a YK ⊂ YJ
et on dispose d’un morphisme de restriction kJ → kK. Si, pour K = {k0, . . . , kp}, les kℓ
´ etant pris dans l’ordre croissant, etJ = {k0, . . . ,ˆki, . . . , kp}, on l’aﬀecte du signe ( −1)i, on
obtient les composantes de la diﬀ´ erentielle d’un complexe de faisceaux sur X n:
(3.3.1) k¯ → ⊕k{j} → · · · → ⊕
|J|=p
kJ → · · · → k∆ n .
Noter que le dernier terme k∆ n est nul sauf pour n = 0 ou a = b, auxquels cas il est
r´ eduit ` ak en t1 = . . . = tn = a. Si on supprime le premier terme et qu’on convient que les
degr´ es vont de 0 ` an, on obtient la r´ esolution ˇCechiste altern´ ee du faisceau constantk sur
la r´ eunion∪Yi des Yi pour le recouvrement ferm´ e ﬁni par les Yi, prolong´ ee par 0 sur X n.
D´ eﬁnissonsbKa ⟨n⟩, ou simplement bKa, comme ´ etant le complexe (3.3.1), avec k∆ n
omis, et les degr´ es allant de 0 ` a n. Si n > 0 et que a ⁄= b, c’est une r´ esolution du prolonge-
ment par 0 du faisceau constant k sur X n − ∪Yi, et
(3.3.2) H∗(X n, bKa) = H ∗(X n mod ∪ Yi, k) (pour n ⁄= 0, a ⁄= b)
Si a = b, la derni` ere diﬀ´ erentielle (3.3.1) fournit un morphisme de complexes
aKa → kt1=···=tn=a[−n],(3.3.3)
qui induit
Hn(X n, aKa) → k.(3.3.4)
27
Si on r´ ep` ete ces constructions en prenant a et b comme param` etres, on obtient un
complexe ∗Ka sur X × X n × X, et, pour p la projection X × X n × X → X × X, la restric-
tion de ∗K∗ ` a X n ∼− →p−1(b, a) s’identiﬁe ` a bKa. Traitant seulement b comme param` etre,
on obtient de mˆ eme ∗Ka sur X × X n. Les Hi(X n, bKa) sont les ﬁbres du syst` eme local
Rip∗(∗K∗) sur X × X.
Nous allons, d’apr` es Beilinson, v´ eriﬁer la
Proposition 3.4. (i) Pour i < n , Hi(X n, bKa) = 0 . (ii) Pour b variable, le syst` eme local
sur X des Hn(X n, bKa), muni en b = a de (3.3.4), est le dual du syst` eme local (Λ /I n+1)˜
de 3.1, muni du transpos´ e de (3.1.1).
Preuve. Pour n = 0, X n est r´ eduit ` a un point, bKa est le faisceau constant k en degr´ e 0
et (i) (ii) sont clairs. Prouvons 3.4 par r´ ecurrence sur n ≥ 1; l’hypoth` ese de r´ ecurrence est
la validit´ e de 3.4 pour m si m < n .
Soit q la premi` ere projection: X n → X. Nous utiliserons la suite spectrale de Leray
pour q. Ceci revient ` a ´ ecrire queRΓ( X n, ) = RΓ( X, Rq∗ ) et ` a ﬁltrer Rq∗ par la ﬁltra-
tion canonique τ . Plus pr´ ecis´ ement, nous utiliserons une ﬁltration ayant une description
uniforme pour a = b ou a ⁄= b, et qui revient ` a la ﬁltration canonique si a ⁄= b.
Un d´ evissage montre que la formation de Rq∗bKa commute au passage aux ﬁbres. Si
on ´ ecritX n comme X × X n−1, bKa sur X n s’identiﬁe au cˆ one[−1] de
∗Ka ⟨n − 1⟩ → bKa ⟨n − 1⟩ sur {b} × X n−1(3.4.1)
⊕ kt
¯
=a sur {a} × X n−1
(complexe simple associ´ e au complexe double de premi` ere ( resp. deuxi` eme) colonne la
source (resp. but) de (3.4.1)).
On reconna ˆ ıt ` a gauche leskJ pour 0 /∈ J et J ⁄= {1, . . . , m}, ` a droite les kJ d’une part
pour 0 ∈ J, de l’autre pour J = {1, . . . , n}.
Si a ⁄= b, la restriction de bKa ` a q−1(t) = X n−1 est donc: pour t ⁄= a, b: tKa ⟨n − 1⟩;
pour t = b: le cˆ one[−1] de l’application identique de bKa ⟨n − 1⟩; pour t = a: le cˆ one[−1]
de (3.3.3). D’apr` es l’hypoth` ese de r´ ecurrence,Riq∗bKa = 0 si i < n − 1. Pour i = n − 1,
28
c’est un sous-faisceau du syst` eme local (Λ /I n)˜
∨
. Il co ¨ ıncide avec (Λ/I n)˜
∨
si t ⁄= a, b, est
nul en t = b et la ﬁbre en a est le noyau du transpos´ e de (3.3.1). Pour i ≥ n, Riq∗bKa est un
syst` eme local sur X − {b} prolong´ e par 0 sur X. La suite spectrale de Leray v´ eriﬁe donc
Epq
2 = 0 pour q ≤ n − 2 ou p = 0, et
Hi(X n, bKa) = 0 pour i < n(3.4.2)
Hn(X n, bKa) = H1(X, Rn−1q∗bKa) (pour a ⁄= b).
Ce H1 est le groupe des extensions du faisceau constant k par (Λ /I n)˜
∨
, trivialis´ ees en
t = b, et trivialis´ ees apr` es avoir pouss´ e par (Λ/I n)∨ → k en t = a. Dualement, c’est le
groupe des extensions ~E de (Λ /I n)˜ par k, trivialis´ ees ent = b, et trivialis´ ees au-dessus de
k ⊂ Λ /I n en t = a.
Traduisons en termes de Λ-modules. A ~E correspond un Λ-module E, extension de
Λ /I n par le module d’augmentation k. Il est annul´ e par I n+1. La donn´ ee additionelle
en a est celle d’un rel` evement ˜
1 du g´ en´ erateur 1 de Λ/I n dans E. Soit α: I n/I n+1 → k
la restriction ` a I n/I n+1 du morphisme de Λ /I n+1 dans E: λ ↦→λ˜
