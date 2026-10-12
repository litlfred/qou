---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-005-91-fondements
section_title: "Fondements"
section_number: 9.1
pages: 50-55
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.948
---
::: defn
[]{#dkim.1 label="dkim.1"} a) Un objet $A\in {\mathcal{A}}$ est *pairement de dimension finie au sens de Kimura* s'il existe un entier $n>0$ tel que $\Lambda^n(A)=0$.\
b) Un objet $A\in {\mathcal{A}}$ est *impairement de dimension finie au sens de Kimura* s'il existe un entier $n>0$ tel que $\mathbf{S}^n(A)=0$.\
c) Un objet $A\in {\mathcal{A}}$ est *de dimension finie au sens de Kimura* s'il admet une décomposition en somme directe $A=A_+\oplus A_-$ telle que $A_+$ soit pairement de dimension finie et $A_-$ soit impairement de dimension finie.
:::

Cette définition a été introduite par Kimura dans [@ki] pour les motifs de Chow. Un grand nombre de ses résultats sont valables, avec leur démonstration, dans notre cadre général. Pour les démonstrations de ce qui suit, nous renvoyons donc à Kimura, sauf pour les énoncés qui ne figurent pas chez lui.

::: nota
Si $A$ est pairement (*resp.* impairement) de dimension finie au sens de Kimura, on note ${\operatorname{kim}}(A)$ le plus petit entier $n>0$ tel que $\Lambda^{n+1}(A)=0$ (*resp.* tel que $\mathbf{S}^{n+1}(A)=0$).
:::

Cette notation abusive ne prêtera pas à confusion car nous préciserons à chaque fois si l'on est dans le cas pair ou impair [@platon][^1].

::: ex
L'objet unité ${\bf 1}$ est pairement de dimension finie; on a ${\operatorname{kim}}({\bf 1})=1$.
:::

::: prop
[]{#pkim.1 label="pkim.1"} a) Toute somme directe, tout facteur direct d'un objet pairement (*resp.* impairement) de dimension finie est pairement (*resp.* impairement) de dimension finie.\
b) Soient $A,B\in {\mathcal{A}}$, pairement ou impairement de dimension finie. Alors $A\bullet B$ est pairement de dimension finie si $A$ et $B$ sont de même parité, impairement de dimension finie sinon. De plus, ${\operatorname{kim}}(A\bullet B)\le{\operatorname{kim}}(A){\operatorname{kim}}(B)$.\
c) Le dual d'un objet pairement (*resp.* impairement) de dimension finie est pairement (*resp.* impairement) de dimension finie.\
d) Si $A$ est pairement de dimension finie, il en est de même de toutes ses puissances extérieures.\
e) Si $A$ est impairement de dimension finie, il en est de même de ses puissances symétriques d'ordre impair, tandis que ses puissances symétriques d'ordre pair sont pairement de dimension finie.
:::

a\) résulte des isomorphismes $$\Lambda^n(A\oplus 
B)\simeq\bigoplus_{p+q=n}
\Lambda^p(A)\bullet\Lambda^q(B)$$ $$\mathbf{ 
S}^n(A\oplus 
B)\simeq\bigoplus_{p+q=n}
\mathbf{S}^p(A)\bullet\mathbf{S}^q(B).$$

b): *cf.* [@ki prop. 5.10].

c\) résulte des isomorphismes $\mathfrak{S}_n$-(anti-)équivariants $$(A^\vee)^{\bullet n}\simeq 
(A^{\bullet n})^\vee.$$

d\) et e) résultent immédiatement de a) et b).$\square$

::: lemme
[]{#lkim.1 label="lkim.1"} a) Soit $A\in {\mathcal{A}}$, pairement de dimension finie. Alors $\dim A$ est un entiernaturel $\le {\operatorname{kim}}
A$.\
b) Soit $A\in {\mathcal{A}}$, impairement de dimension finie. Alors $-\dim A$ est un entier naturel $\le {\operatorname{kim}}A$.
:::

C'est une reformulation de la proposition [\[nouvelle\]](#nouvelle){reference-type="ref" reference="nouvelle"} ii).$\square$

::: prop
[]{#lkim.2 label="lkim.2"} Soit $A\in{\mathcal{A}}$, pairement ou impairement de dimension finie. Supposons que $\dim A=0$. Alors $A=0$.
:::

Soit ${\mathcal{B}}$ la plus petite sous-catégorie pleine rigide épaisse (*i.e.* stable par facteurs directs) de ${\mathcal{A}}$ contenant $A\bullet A^\vee$. D'après la proposition [\[pkim.1\]](#pkim.1){reference-type="ref" reference="pkim.1"}, tout objet de ${\mathcal{B}}$ est pairement de dimension finie. D'après le lemme [\[lkim.1\]](#lkim.1){reference-type="ref" reference="lkim.1"}, cela implique que la dimension de tout objet de ${\mathcal{B}}$ est un entier naturel. De plus, $\dim(A\bullet
A^\vee)=\dim(A)^2=0$. D'après la proposition [\[nouvelle\]](#nouvelle){reference-type="ref" reference="nouvelle"} i), ${\mathcal{N}}(A,A)$ est donc un idéal nilpotent de ${\mathcal{A}}(A,A)={\mathcal{B}}(A,A)$, et d'après la proposition [\[new p5/2\]](#new p5/2){reference-type="ref" reference="new p5/2"} a), ${\mathcal{B}}/{\mathcal{N}}(A,A)=0$. Il en résulte bien que $A=0$.$\square$

::: thm
[]{#pkim.2 label="pkim.2"} a) Soit $A\in {\mathcal{A}}$ pairement de dimension finie. Alors ${\operatorname{kim}}A\allowbreak=\dim A$.\
b) Soit $A\in{\mathcal{A}}$ impairement de dimension finie. Alors ${\operatorname{kim}}A = 
-\dim
A$.
:::

a\) Soit $m'=\dim A$. Vu le lemme [\[lkim.1\]](#lkim.1){reference-type="ref" reference="lkim.1"} a), il suffit de montrer que $\Lambda^{m'+1}(A)=0$. Mais d'après la proposition [\[a 
la
Deligne\]](#a 
la
Deligne){reference-type="ref" reference="a 
la
Deligne"}, on a $\dim\Lambda^{m'+1}(A)=\binom{m'}{m'+1}=0$. L'assertion résulte donc de la proposition précédente.

b\) Même démonstration, en utilisant une puissance symétrique.$\square$

Le corollaire suivant n'est pas démontré chez Kimura.

::: cor
[]{#ckim.1 label="ckim.1"} a) Si $A$ et $B$ sont pairement de dimension finie, alors ${\operatorname{kim}}(A\oplus
B)={\operatorname{kim}}A+{\operatorname{kim}}
B$.\
b) Si $A$ et $B$ sont impairement de dimension finie, alors ${\operatorname{kim}}(A\oplus
B)={\operatorname{kim}}A+{\operatorname{kim}}
B$.$\square$
:::

::: prop
[]{#kimnil label="kimnil"} Soient $A_+$ (*resp.* $A_{-}$) un objet de ${\mathcal{A}}$ pairement (*resp.* impairement) de dimension finie. Soient $m={\operatorname{kim}}
A_+$ et $n={\operatorname{kim}}A_{-}$. Alors pour tout $f\in 
{\mathcal{A}}(A_+,A_{-})$ et tout $g\in {\mathcal{A}}(A_{-}, A_+)$, on a $f^{\bullet 
(mn+1)}=0$, $g^{\bullet (mn+1)}=0$.
:::

Voici une variante de [@ki dém de la prop. 6.1], un peu plus simple: grâce à la proposition [\[pkim.1\]](#pkim.1){reference-type="ref" reference="pkim.1"} b) et par dualité, on se ramène à traiter le cas de $f$ avec $A_+={\bf 1}$. Le morphisme $f^{\bullet (n+1)}:{\bf 1}={\bf 1}^{\bullet (n+1)}\to A_-^{\bullet 
(n+1)}$ est $\mathfrak{S}_n$-équivariant, ce qui implique qu'il se factorise à travers $\mathbf{S}^{n+1}(A_-)=0$.$\square$

::: prop
[]{#pkim.3 label="pkim.3"} Soit $A$ un objet de dimension finie au sens de Kimura, et supposons données deux décompositions $A\simeq
A_+\oplus A_-\simeq B_+\oplus B_-$, avec $A_+,B_+$ pairement de dimension finie et $A_-,B_-$ impairement de dimension finie. Alors $A_+\simeq B_+$ et $A_-\simeq B_-$.
:::

[@ki dém. de la prop. 6.3]. On remarquera que cette démonstration utilise le corollaire [\[ckim.1\]](#ckim.1){reference-type="ref" reference="ckim.1"} a).$\square$

::: lemme
[]{#lkim.3 label="lkim.3"} Soit $A\in{\mathcal{A}}$, et soit $A=A_+\oplus A_-$ une décomposition en somme directe. Posons $$s\Lambda^n(A_+,A_-)= \bigoplus_{i+j=n}\Lambda^i 
A_+\bullet \mathbf{S}^j
A_-.$$ Alors les conditions suivantes sont équivalentes:

::: thlist
Il existe un entier $n>0$ tel que $s\Lambda^n(A_+,A_-)=0$.

$A_+$ est pairement de dimension finie et $A_-$ est impairement de dimension finie.
:::

De plus, dans (i), on peut prendre $n={\operatorname{kim}}A_+ +{\operatorname{kim}}A_-+1$, et ceci est le plus petit choix possible.
:::

Laissée au lecteur (pour voir que ${\operatorname{kim}}A_+ +{\operatorname{kim}}A_-+1$ est le plus petit choix possible, observer que $$\dim s\Lambda^{{\operatorname{kim}}
A_++{\operatorname{kim}}A_-}(A_+,A_-)=\dim s\Lambda^{\dim
A_+-\dim A_-}(A_+,A_-)=1,$$ en utilisant le corollaire [\[ckim.1\]](#ckim.1){reference-type="ref" reference="ckim.1"}).$\square$

::: prop
[]{#pkim.4 label="pkim.4"} Tout facteur direct d'un objet de dimension finie est de dimension finie.$\square$
:::

::: defn
[]{#dkim.2 label="dkim.2"} Soit $A$ un objet de dimension finie au sens de Kimura. On définit $${\operatorname{kim}}A ={\operatorname{kim}}A_+ +{\operatorname{kim}}A_-=\dim A_+ -\dim A_-$$ $$s\Lambda^n A= \bigoplus_{i+j=n}\Lambda^i A_+\bullet \mathbf{S}^j A_-$$ où $A=A_+\oplus A_-$ est une décomposition de $A$ en somme d'un objet pairement de dimension finie et d'un objet impairement de dimension finie.
:::

La proposition [\[pkim.3\]](#pkim.3){reference-type="ref" reference="pkim.3"} montre que ${\operatorname{kim}}A$ *ne dépend que de $A$ et que $s\Lambda^n A$ ne dépend que de $A$ à isomorphisme près*.

On a maintenant la généralisation suivante de la proposition [\[nouvelle\]](#nouvelle){reference-type="ref" reference="nouvelle"}:

::: prop
[]{#nouvellekim label="nouvellekim"} Soit $A\in {\mathcal{A}}$ un objet de dimension finie au sens de Kimura. Alors ${\mathcal{N}}(A,A)$ est un idéal nilpotent de ${\mathcal{A}}(A,A)$, d'échelon borné en termes de ${\operatorname{kim}}(A)$. En particulier, pour $A\ne 0$, l'image de $A$ n'est pas nulle dans ${\mathcal{A}}/{\mathcal{N}}$.
:::

D'après [\[naghig\]](#naghig){reference-type="ref" reference="naghig"}, il suffit de faire voir que ${\mathcal{N}}(A,A)$ est un nilidéal d'échelon borné en termes de ${\operatorname{kim}}(A)$. L'argument est analogue à celui de [@ki prop. 7.5]: tout élément $f$ de ${\mathcal{N}}(A,A)$ peut s'écrire comme une matrice $2\times
2$ sur la décomposition $A=A_+\oplus A_-$. On écrit $f=f_+ + f_- +
f_\pm$, où $f_+$ est le terme préservant $A_+$, $f_-$ le terme préservant $A_-$ et $f_\pm$ est la somme des deux termes antidiagonaux. Comme $f_+f_-=f_-f_+=0$, un monôme typique intervenant dans le développement de $f^n$ est de la forme $$m=f_{\varepsilon_1}^{k_1}\circ f_\pm\circ f_{\varepsilon_2}^{k_2}\circ
f_\pm\circ\dots\circ f_\pm\circ f_{\varepsilon_r}^{k_r}$$ avec $\varepsilon_i\in \{+,-\}$.

D'après la proposition [\[nouvelle\]](#nouvelle){reference-type="ref" reference="nouvelle"}, on a $m=0$ dès que l'un des $k_i$ est assez grand. D'autre part, d'après la proposition [\[kimnil\]](#kimnil){reference-type="ref" reference="kimnil"} et le lemme [\[l8.1\]](#l8.1){reference-type="ref" reference="l8.1"} i), on a $f_\pm^{\bullet N}=0$ pour $N$ assez grand (indépendamment de $f$), ce qui implique (lemme [\[l8.1\]](#l8.1){reference-type="ref" reference="l8.1"} ii)) que $m=0$ dès que le nombre de fois où $f_\pm$ apparaı̂t est $\ge N$. Ceci conclut la démonstration.$\square$

::: rem
On pourrait aussi utiliser le raisonnement de la démonstration de la proposition [\[P3/2\]](#P3/2){reference-type="ref" reference="P3/2"} c) à partir de la proposition [\[nouvelle\]](#nouvelle){reference-type="ref" reference="nouvelle"}. Ceci donne l'estimation suivante pour l'échelon de nilpotence $N$ de ${\mathcal{N}}(A,A)$: $$N\le 2^{{\operatorname{kim}}A_++1}+2^{{\operatorname{kim}}A_-+1}\le 2^{{\operatorname{kim}}A+1}+1$$ bien meilleure que celle fournie par la démonstration ci-dessus.
:::

::: defn
[]{#defki label="defki"} Une *catégorie de Kimura*[^2] sur un corps de caractéristique nulle $K$ est une catégorie $K$-linéaire monoı̈dale symétrique rigide, vérifiant $End({\bf 1})=K$, pseudo-abélienne, et dont tout objet est de dimension finie au sens de Kimura.
:::

## Catégories de Kimura et "projecteurs de Künneth\"

 

Soient $K$ un corps de caractéristique nulle et ${\mathcal{A}}$ une catégorie $K$-linéaire monoı̈dale symétrique rigide, vérifiant $End({\bf 1})=K$, pseudo-abélienne. Soit ${\mathcal{A}}_{\operatorname{kim}}$ la plus grande sous-catégorie de Kimura de ${\mathcal{A}}$, *i.e.* la sous-catégorie pleine de ${\mathcal{A}}$ formée des objets de dimension finie au sens de Kimura: c'est une sous-catégorie épaisse et rigide de ${\mathcal{A}}$, d'après les propositions [\[pkim.1\]](#pkim.1){reference-type="ref" reference="pkim.1"} et [\[pkim.4\]](#pkim.4){reference-type="ref" reference="pkim.4"}.

::: thm
[]{#tkim.1 label="tkim.1"} Supposons que $\sqrt[\otimes]{0}=0$. Alors\
a) La catégorie ${\mathcal{A}}_{{\operatorname{kim}}}$ est munie d'une $\mathbf{Z}/2$-graduation compatible à la structure monoı̈dale.\
b) Pour tout $A\in {\mathcal{A}}_{{\operatorname{kim}}}$, notons $\pi^+_A$ le projecteur de $A$ définissant $A_+$ et $\varepsilon_A=2\pi_A^+-1$: on a $\varepsilon_A^2=1$. Définissons une nouvelle contrainte de commutativité $R'$ sur ${\mathcal{A}}_{{\operatorname{kim}}}$ par la formule [\[kunneth\]](#kunneth){reference-type="eqref" reference="kunneth"}. Alors

::: thlist
Pour tout $n\ge 0$, l'objet $s\Lambda^n(A)$ est la $n$-ième puissance symétrique de $A$ relative à $R'$.

La dimension de $A$ relative à $R'$ est égale à ${\operatorname{kim}}A$; en particulier, c'est un entier $\ge 
0$.

Cette propriété caractérise d'ailleurs la graduation dont il est question en $a)$.
:::

c\) Soient $L$ une $K$-algèbre semi-simple commutative et $H:{\mathcal{A}}\to
Modf_L^\pm$ un foncteur vérifiant les hypothèses de la proposition [\[new p4\]](#new p4){reference-type="ref" reference="new p4"}. Alors avec les notations de *loc. cit.* , on a ${\mathcal{A}}_{{\operatorname{kim}}}={\mathcal{A}}^\pm$. Munie de la contrainte induite par $R'$, le quotient de ${\mathcal{A}}_{{\operatorname{kim}}}$ par son radical est un catégorie tannakienne semi-simple.
:::

a\) Puisque $\sqrt[\otimes]{0}=0$, la proposition [\[kimnil\]](#kimnil){reference-type="ref" reference="kimnil"} montre que si $A$ et $B$ sont $\varepsilon$-ment de dimension finie à la Kimura avec des parités différentes, alors ${\mathcal{A}}(A,B)=0$. Ceci permet de renforcer la proposition [\[pkim.3\]](#pkim.3){reference-type="ref" reference="pkim.3"} en l'énoncé suivant: si $A\in{\mathcal{A}}_{{\operatorname{kim}}}$, la décomposition de $A$ en somme directe d'un objet pair et d'un objet impair est *unique*. Il en résulte immédiatement que cette décomposition est fonctorielle en $A$; les autres propriétés résultent de la proposition [\[pkim.1\]](#pkim.1){reference-type="ref" reference="pkim.1"}.

b\) ne présente pas de difficulté.

c\) Pour voir l'inclusion ${\mathcal{A}}_{{\operatorname{kim}}}\subset{\mathcal{A}}^\pm$, il suffit de voir que $H(\pi_A^+)=p_A^+$ (avec les notations de la proposition [\[new
p4\]](#new
p4){reference-type="ref" reference="new
p4"}). En effet, on voit immédiatement que $H(A_+)$ est pair et que $H(A_-)$ est impair (*cf.* [@ki dém. de la prop. 3.9]). Pour voir l'inclusion opposée, il suffit de voir que si $A=A_+\oplus A_-\in
{\mathcal{A}}^\pm$, alors $A_+$ est pairement de dimension finie et $A_-$ est impairement de dimension finie. Choisissons $n$ tel que $H(\Lambda^n(A_+))=\Lambda^n(H(A_+))=0$. Comme $H$ est fidèle, cela entraı̂ne que le morphisme identité de

$\Lambda^n(A_+)$ est nul, donc $\Lambda^n(A_+)=0$; de même pour $A_-$. Le changement de contrainte de commutativité comme en [\[new p4\]](#new p4){reference-type="ref" reference="new p4"} ramène à la situation du théorème [\[nouveau\]](#nouveau){reference-type="ref" reference="nouveau"}, qui permet de conclure que la catégorie quotient par ${\mathcal{R}}= {\mathcal{N}}$ munie de la contrainte induite par $R'$ est tannakienne semi-simple.$\square$

::: thm
[]{#tctki label="tctki"} Toute catégorie de Kimura ${\mathcal{A}}$ est de Wedderburn. Son radical ${\mathcal{R}}$ est le plus grand idéal monoı̈dal distinct de ${\mathcal{A}}$. Le quotient de ${\mathcal{A}}$ par ${\mathcal{R}}$ est une catégorie tannakienne semi-simple (après changement approprié de la contrainte de commutativité).
:::

On a ${\mathcal{A}}={\mathcal{A}}_{\operatorname{kim}}$. La première affirmation résulte de la proposition [\[nouvellekim\]](#nouvellekim){reference-type="ref" reference="nouvellekim"}. Pour le reste, on se ramène au théorème [\[tkim.1\]](#tkim.1){reference-type="ref" reference="tkim.1"} en quotientant par $\sqrt[\otimes]{0}$ (*cf.* le lemme [\[l8.1\]](#l8.1){reference-type="ref" reference="l8.1"} iii))$\square$

::: rem
[]{#nilplusplus label="nilplusplus"} Étant donné une catégorie de Kimura ${\mathcal{A}}$, le théorème [\[tctki\]](#tctki){reference-type="ref" reference="tctki"} nous permettra d'appliquer les théorèmes de scindage monoı̈dal [\[T2\]](#T2){reference-type="ref" reference="T2"} et [\[t4\]](#t4){reference-type="ref" reference="t4"} à la projection ${\mathcal{A}}\to {\mathcal{A}}/{\mathcal{R}}$. En particulier, *on pourra munir ${\mathcal{A}}$ d'une $\mathbf{Z}/2$-graduation compatible à celle de ${\mathcal{A}}/\sqrt[\otimes]{0}$, unique à équivalence monoı̈dale près*. Voir le théorème [\[kimsplit\]](#kimsplit){reference-type="ref" reference="kimsplit"}.
:::

::: ex
[]{#cj kimura label="cj kimura"} Kimura [@ki 7.1] conjecture que tout motif de Chow est de dimension finie en son sens (c'est-à-dire, avec la terminologie ci-dessus, que la catégorie des motifs de Chow est une $\mathbf{Q}$-catégorie de Kimura). Cette conjecture implique donc que tout motif "fantôme\", *i.e.* numériquement nul, est nul. Réciproquement, modulo l'existence pour chaque motif de Chow $A$ d'un projecteur $\pi^+_A$ qui s'envoie sur le projecteur de Künneth pair $p^+_A$, la non-existence de motifs fantômes non nuls implique la conjecture de Kimura (considérer le motif $s\Lambda^n A$ pour $n$ assez grand).

Par ailleurs, la conjecture de Murre mentionnée en [\[BBM\]](#BBM){reference-type="ref" reference="BBM"} implique l'existence d'un tel $p^+_A$, et, jointe aux conjectures standard de Grothendieck (équivalence homologique = équivalence numérique), implique la non-existence de motifs fantômes non nuls. On voit ainsi que la conjecture de Murre (ou, ce qui est équivalent, la conjecture de Bloch-Beilinson) jointe aux conjectures standard implique la conjecture de Kimura.
:::

# Exemples et compléments

[^1]: Du reste, on verra ultérieurement qu'un objet à la fois pairement et impairement de dimension finie est nul.

[^2]: Cette notion a été introduite indépendamment par P. O'Sullivan sous le nom de "semi-positive category\", comme nous l'avons appris après la soumission de ce texte à publication (*cf.* postscriptum à l'introduction générale).
