---
doc_id: arxiv-1806.09450v1
doc_title: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗"
section_id: sec-004-32-the-magic-square
section_title: "The magic square"
section_number: 3.2
pages: 8-10
source_pdf: 1806.09450v1.pdf
source_sha256: 8556b67d97856446
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.993
doc_brief: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗ — We continue the study undertaken in [DV] of the exceptional Jordan algebra"
---
Equivalent constructions of the Lie algebras ${\mathfrak e}_n$ with $n  = 6,7,8$ have been proposed by Freudenthal and Tits around 1958, with improved formulations published later. In the summary below we follow [@BS], as well as [@B] where more references to the early work can be found.

Let ${\mathbb K}$ be a real composition algebra and $J$ a real Jordan algebra with unit ${\rm 1\mkern-4mu I}$ and with an inner product satisfying $\langle X , Y \circ Z \rangle = \langle X \circ Y , Z \rangle$ ([\[eq210\]](#eq210){reference-type="ref" reference="eq210"}). Let further ${\mathbb K}_0$ and $J_0$ be the subspaces of ${\mathbb K}$ and $J$ orthogonal to the unit element. Denote by $*$ the product in $J_0$ obtained from the Jordan product projected back to $J_0$: $$\label{eq312}
X * Y = X \circ Y - \frac1n \, \langle X,Y \rangle \, {\rm 1\mkern-4mu I}\quad \mbox{where} \quad n = \langle {\rm 1\mkern-4mu I}, {\rm 1\mkern-4mu I}\rangle = {\rm tr} \, {\rm 1\mkern-4mu I}$$ (the notation being chosen to fit the case $J = H_n ({\mathbb K}')$). Tits defines (in 1966) a Lie algebra structure on the vector space $$\label{eq313}
T ({\mathbb K} , J) = {\rm Der} \, ({\mathbb K}) \, \dot + \, {\rm Der} \, (J) \, \dot + \, {\mathbb K}_0 \otimes J_0$$ by setting $$\label{eq314}
[x \otimes X , y \otimes Y] = \frac1n \, \langle X,Y \rangle \, D_{x,y} - \langle x,y \rangle [L_X , L_Y] + [x,y] \otimes X * Y$$ where $x,y \in {\mathbb K}_0$, $X,Y \in J_0$ and the square brackets in the right hand side denote commutators in ${\mathbb K}_0$ and ${\rm End} \, (J)$; $D_{x,y}$ is the derivation in ${\mathbb K}_0$ defined by ([\[eq24\]](#eq24){reference-type="ref" reference="eq24"}). Tits proves that the brackets ([\[eq314\]](#eq314){reference-type="ref" reference="eq314"}) define a Lie algebra structure using the identity $$\label{eq315}
n \, X^3 - ({\rm tr} \, X^3) \, {\rm 1\mkern-4mu I}= ({\rm tr} \, X^2) \, X \quad \mbox{for} \quad X \in J_0 \, , \ J = H_n ({\mathbb K}')$$ (for ${\mathbb K}' = {\mathbb O}$, $n \leq 3$). Tits obtains the magic square of Lie algebras by viewing $T({\mathbb K} , J)$ for $J = H_3 ({\mathbb K}')$ as a Lie algebra $L({\mathbb K} , {\mathbb K}')$ depending on two composition algebras ${\mathbb K}$ and ${\mathbb K}'$: $$\label{eq316}
L({\mathbb K} , {\mathbb K}') = T ({\mathbb K} , H^3 ({\mathbb K}')) \, .$$ For the Lie algebras of compact real forms one thus obtains the following symmetric table:

::: tabular
\|C1cm\|C2cm\|C2cm\|C2cm\|C2cm\| ${\mathbb K} \ \backslash \ {\mathbb K}'$ &${\mathbb R}$ &${\mathbb C}$ &${\mathbb H}$ &${\mathbb O}$\
${\mathbb R}$ &$so \, (3)$ &$su \, (3)$ &$sp \, (6)$ &${\mathfrak f}_4$\
${\mathbb C}$ &$su \, (3)$ &$su \, (3) \oplus u(3)$ &$su \, (6)$ &${\mathfrak e}_6$\
${\mathbb H}$ &$sp \, (6)$ &$su \, (6)$ &$so \, (12)$ &${\mathfrak e}_7$\
${\mathbb O}$ &${\mathfrak f}_4$ &${\mathfrak e}_6$ &${\mathfrak e}_7$ &${\mathfrak e}_8$\
:::

> Magic square of Lie algebras $L({\mathbb K} , {\mathbb K}')$ ($sp \, (6)$ being the rank 3 unitary symplectic Lie algebra).

Following Tits construction the symmetry of the square comes as a surprise. In fact, it has been predicted in a non-rigorous visionary 1956 paper of the Russian mathematician and historian of science Boris Rosenfeld who proposed to view $E_6 , E_7 , E_8$ as isometry groups of projective planes over the algebras ${\mathbb K} \, \otimes \, {\mathbb O}$ for ${\mathbb K} = {\mathbb C} , {\mathbb H}, {\mathbb O}$, respectively, just as $F_4$ is the isometry group of ${\mathbb P}^2 ({\mathbb O})$ $=$ ${\mathbb P}^2 ({\mathbb R} \, \otimes \, {\mathbb O})$ (see [@B] for references and for a more detailed discussion; Rosenfeld provides a later expositon of his views in Chapter VII of [@R]). The realization of this idea has problems since ${\mathbb K} \otimes {\mathbb O}$ is not a division algebra except for ${\mathbb K} = {\mathbb R}$. A construction of the exceptional Lie algebras generalizing ([\[eq311\]](#eq311){reference-type="ref" reference="eq311"}), however, does exist with ${\rm Der} \, ({\mathbb K}) \oplus {\rm Der} \, ({\mathbb O})$ instead of ${\rm Der} \, ({\mathbb O})$ and $sa_3 ({\mathbb O})$ substituted by $sa_3 ({\mathbb K} \otimes {\mathbb O})$. This is Vinberg's (1966) approach to constructing $L({\mathbb K} , {\mathbb K}')$, that is manifestly symmetric with respect to the two algebras ${\mathbb K}$ and ${\mathbb K}'$. The Lie brackets in $L({\mathbb K} , {\mathbb K}')$ are given as follows.

1.  ${\rm Der} \, ({\mathbb K})$ and ${\rm Der} \, ({\mathbb K}')$ are commuting Lie subalgebras of $L ({\mathbb K} , {\mathbb K}')$.

2.  The bracket of $D \in {\rm Der} \, ({\mathbb K}) \oplus {\rm Der} \, ({\mathbb K}')$ with $X \in sa_3 ({\mathbb K} \otimes {\mathbb K}')$ is given by applying $D$ to every entry of the matrix $X$ using the natural action of ${\rm Der} \, ({\mathbb K})$ and ${\rm Der} \, ({\mathbb K}')$ as derivations on ${\mathbb K} \otimes {\mathbb K}'$.

3.  Given $X,Y \in sa_3 ({\mathbb K} \otimes {\mathbb K}')$, we set $$\label{eq317}
    [X,Y] = [X,Y]_0 + \frac13 \sum_{i,j=1}^3 D_{x_{ij} , y_{ij}} \, .$$ Here $[X,Y]_0$ is the traceless part of the $3 \times 3$ matrix $[X,Y]$, and given $x,y \in {\mathbb K} \otimes {\mathbb K}'$, we define $D_{x,y} \in {\rm Der} \, ({\mathbb K}) \oplus {\rm Der} \, ({\mathbb K}')$ as real bilinear in $a,b \in {\mathbb K}$, $a',b' \in {\mathbb K}'$ such that $$\label{eq318}
    D_{a \otimes a' \, b \otimes b'} = \langle a',b' \rangle \, D_{a,b} + \langle a,b \rangle \, D_{a',b'}$$ where $a,b \in {\mathbb K}$, $a',b' \in {\mathbb K}'$, and $D_{a,b}$, $D_{a',b'}$ are defined as in Eq. ([\[eq24\]](#eq24){reference-type="ref" reference="eq24"}).

For the equivalence of Tits' and Vinberg's constructions of the magic square and for its triality construction we refer to [@B; @BS].
