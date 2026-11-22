---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-001-the-nearby-cycles-formalism-for-parity-sheaves
section_title: "The nearby cycles formalism for parity sheaves"
section_number: null
pages: 5-7
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
toc_source: inferred
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algebraic Lie theory from the geometric and categorical"
---
Pramod N. Achar
This talk is based on the results of [1, 6]. Let X be a complex algebraic variety,
and let f : X →C be an algebraic map. Consider the diagram
X0
X
Xη
{0}
C
C×
i
f0
f
j
fη
Let Db
c (X, C) be the derived category of constructible complexes of sheaves of
C-vector spaces on X. The classical (unipotent) nearby cycles functor is a functor
Ψf : Db
c (Xη, C) →Db
c (X0, C)
Following [7, 12], this functor can be deﬁned as
Ψf(F) = i∗j∗(f ∗
η L∞⊗L F),
where L∞is the (inﬁnite-rank) pro-unipotent local system on C×. This functor
enjoys the following properties:
(1) The object Ψf(F) is equipped with a canonical unipotent automorphism
T : Ψf(F) →Ψf(F), called the monodromy automorphism.
(2) The object Ψf(F) is constructible. (Since L∞is not constructible, this
statement is nontrivial.)
(3) The functor Ψf is t-exact for the perverse t-structure.
If we take the logarithm of the operator T , we can replace (1) above by:
(1′) The object Ψf(F) is equipped with a canonical nilpotent endomorphism
N : Ψf(F) →Ψf(F).
Here are some ways in which one might hope to generalize this theory:
• One can replace ordinary constructible sheaves by mixed sheaves—either
mixed Hodge modules or mixed ℓ-adic sheaves. In both settings, the “log-
arithm of monodromy” becomes a map of weight 2, i.e., we have a map
N : Ψf(F) →Ψf(F)(−1).
• One can replace constructible C-sheaves by constructible k-sheaves, where
k is a ﬁeld of positive characteristic. In this case, “logarithm” no longer
makes sense, but properties (1), (2), and (3) still hold.
A third setting where one might want to have a nearby cycles formalism is that
of the mixed modular derived category from [4]. This notion is based on the theory
of parity sheaves [10], and it exists and behaves well only under very restrictive
circumstances, such as on ﬂag varieties. Nevertheless, it has found important appli-
cations in a number of recent advances in modular geometric representation theory
3086
Oberwolfach Report 52/2018
(see, for instance, [5, 3]). Building on these results, it has long been expected that
there should be a mixed modular analogue of Gaitsgory’s construction of central
sheaves on the aﬃne ﬂag variety [9]. This expectation is the main motivation to
look for a nearby cycles formalism for parity sheaves.
The principal diﬃculty is that it is rather diﬃcult to even deﬁne a sheaf functor
on Dmix(X, k) if its classical version does not send parity sheaves to parity sheaves.
Even worse, the classical nearby cycles construction involves the nonconstructible,
nonsemisimple local system L∞.
The framework of [10, 4] does not allow for
nonconstructible objects or for nonsemisimple local systems.
The goal of this talk is to explain a way around these diﬃculties. A key technical
tool in [1] is a new category Dmix
mon(X, k), called the monodromic derived category.
This category (whose deﬁnition is closely modeled on that of the “free-monodromic
category” in [2]) is still deﬁned in terms of the homological algebra of parity
sheaves, but it does allow both nonconstructible objects and nonsemisimple local
systems. One preliminary result of [1] is the existence of a fully faithful functor
Mon : Dmix(X, k) →Dmix
mon(X, k).
Its image is precisely the subcategory of constructible objects.
Under some assumptions on X, the paper [1] also deﬁnes a functor
J : Dmix
Gm (X, k) →Dmix
mon(X, k)
that can be thought of as a parity-sheaf analogue of the operation f ∗
η L∞⊗L (−).
Its output is always nonconstructible, and is equipped with a endomorphism N of
weight 2.
Theorem ([1]). For any F ∈Dmix
Gm (Xη, k), the object i∗j∗J (F) is constructible.
The main content of [1] is a deﬁnition, rather than a theorem. Thanks to the
result above, it makes sense to deﬁne a functor
Ψf : Dmix
Gm (Xη, k) →Dmix(X0, k)
by
Ψf(F) = Mon−1(i∗j∗J (F)(1)).
(The (1) is a Tate twist that is included as a normalization.) It comes with a
canonical nilpotent endomorphism
N : Ψf(F) →Ψf(F)(−1).
This map plays the same conceptual role as the “logarithm of the monodromy” in
the classical setting, but here, it is not the logarithm of anything. (When k has
positive characteristic, it does not make sense to exponentiate N.) It is reasonable
to expect Ψf to be t-exact for the perverse t-structure, but this remains conjectural
at the moment.
In the companion paper [6], L. Rider and I explicitly computed Ψf(k) in the
mixed modular derived category in two important and related settings:
(1) X = Cn, and f : X →C is the function f(x1, . . . , xn) = x1 · · · xn.
(2) X is the “global Schubert variety” associated to the ﬁrst fundamental
coweight of the group PGLn. This variety comes equipped with a map
Enveloping Algebras and Geometric Representation Theory
3087
to C. Its generic ﬁbers are isomorphic to Pn−1, and its special ﬁber is
identiﬁed with a certain closed subset of the aﬃne ﬂag variety of PGLn.
In the former case, we obtained results that closely resemble known facts about
the classical nearby cycles functor for mixed ℓ-adic sheaves [11, 13].
The latter case is the ﬁrst nontrivial example where one might hope to obtain
instances of Gaitsgory’s central sheaves. The explicit objects obtained in [6] as the
nearby cycles sheaves on the aﬃne ﬂag variety were discovered independently by
Elias [8] from a diﬀerent perspective, not involving the nearby cycles formalism.
Elias has shown that these objects enjoy many of the expected properties of central
sheaves.
References
[1] P. Achar, How to glue parity sheaves, arXiv:1812.07920.
[2] P. Achar, S. Makisumi, S. Riche, and G. Williamson, Free-monodromic mixed tilting sheaves
on ﬂag varieties, arXiv:1703.05843.
[3] P. Achar, S. Makisumi, S. Riche, and G. Williamson, Koszul duality for Kac–Moody groups
and characters of tilting modules, J. Amer. Math. Soc. 32 (2019), 261–310.
[4] P. Achar and S. Riche, Modular perverse sheaves on ﬂag varieties II: Koszul duality and
formality, Duke Math. J. 165 (2016), 161–215.
[5] P. Achar and S. Riche, Dualit´e de Koszul formelle et th´eorie des repr´esentations des groupes
alg´ebriques r´eductifs en caract´eristique positive, arXiv:1807.08690.
[6] P. Achar and L. Rider, Nearby cycles for parity sheaves on a divisor with simple normal
crossings, arXiv:1812.07924.
[7] A. Be˘ılinson, How to glue perverse sheaves, K-theory, arithmetic and geometry (Moscow,
1984–1986), Lecture Notes in Math., vol. 1289, Springer, 1987, pp. 42–51.
[8] B. Elias, Gaitsgory’s central sheaves via the diagrammatic Hecke category, arXiv:1811.-
06188.
[9] D. Gaitsgory, Construction of central elements in the aﬃne Hecke algebra via nearby cycles,
Invent. Math. 144 (2001), 253–280.
[10] D. Juteau, C. Mautner, and G. Williamson, Parity sheaves, J. Amer. Math. Soc. 27 (2014),
1169–1212.
[11] M. Rapoport and T. Zink, ¨Uber die lokale Zetafunktion von Shimuravariet¨aten. Mon-
odromieﬁltration und verschwindende Zyklen in ungleicher Charakteristik, Invent. Math.
68 (1982), 21–101.
[12] R. Reich, Notes on Beilinson’s “How to glue perverse sheaves”, J. Singul. 1 (2010), 94–115.
[13] T. Saito, Weight spectral sequences and independence of ℓ, J. Inst. Math. Jussieu 2 (2003),
583–634.
