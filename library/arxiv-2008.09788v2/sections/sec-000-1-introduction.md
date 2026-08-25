---
doc_id: arxiv-2008.09788v2
doc_title: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETR Y"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 2008.09788v2.pdf
source_sha256: 460f4f5432cb1f0c
doc_brief: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY — This paper surveys results related to well-known works of B. Plotkin and V."
---
2. Model-theoretical aspects 5
2.1. Algebraic geometry over algebraic systems 5
2.2. Plotkin’s problem: automorphisms of endomorphism sem igroups and groups
of polynomial automorphisms 13
2.3. On the independence of the B-KK isomorphism of inﬁnite p rime and Plotkin
conjecture for symplectomorphisms 13
3. Algorithmic aspects of algebraic geometry 23
3.1. Finite Gr¨ obner basis algebras with unsolvable nilpot ency problem and zero
divisors problem 23
Key words and phrases. universal algebraic geometry, aﬃne algebraic geometry, el ementary equiv-
alence, isotypic algebras, ﬁrst order rigidity, Ind-group , Aﬃne spaces, Automorphisms, Free associative
algebras, Weyl algebra automorphisms, polynomial symplec tomorphisms, deformation quantization, in-
ﬁnite prime number, semi-inner automorphism, embeddabili ty of varieties, undecidability, Noncommu-
tative Gr¨ obner-Shirshov basis, ﬁnitely presented algebr aic systems, Algorithmic unsolvability, Turing
machine.
The ﬁrst three authors were supported by the Russian Science Foundation grant No. 17-11-01377,
fourth, ﬁfth and seventh named authors were supported by the ISF (Israel Science Foundation) grant
1994/20.
We would like to thank the anonymous referee for suggestions regarding this paper.
1
2 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKIN , YU, AND ZHANG
3.2. On the algorithmic undecidability of the embeddabilit y problem for algebraic
varieties over a ﬁeld of characteristic zero 25
References 28
1. Introduction
The connections between algebraic geometry and mathematic al logic are extremely
important. First of all, notice a deep connection between al gebra, category theory and
model theory inspired by the results of Plotkin and his schoo l (see [79, 81, 82, 83, 84]. Note
that this research is related to the one of most striking exam ples of interaction between
model theory and geometry given by solutions of the famous Ta rskii’s problem, see [46, 99].
Another outstanding achievement is the theory of Zariski ge ometries developed by B.Zilber
and E.Hrushovski [26] and [116, 117]. In addition, the use of non-standard analysis has
allowed progress in the theory of polynomial 64 automorphis ms. See the work of Belov
and Kontsevich [37, 38]. For a detailed bibliography see [85 ].
The foundations of algebraic geometry had an important part of the translation of
topological and arithmetical properties into a purely alge braic language ([22]). Translation
of the algebraic properties of a variety into the language of mathematical logic can be
considered somehow in the spirit of this program.
This short survey is related to ideas contained in the works o f B. Plotkin and V.
Remeslennikov and their followers. We assume that lots of qu estions still require further
illumination.
In particular, the following question is of interest: given two algebraic sets. Is there
an algorithm for checking isomorphism? Similarly for birat ional equivalence. Is there a
solution to the nesting problem of two varieties? For charac teristics 0, the answer is no
[36], but for a positive characteristic the answer is unknow n.
On should mention a number of conjectures related to the theo ry of models and polyno-
mial automorphisms expressed in the paper by Belov-Kontsev ich [37]. The investigations
of the Plotkin school are far from completion, thus the relat ionship between the theory of
medallions and the theory of categories is relevant.
One of the goals of this paper is to narrow the gap and to draw at tention to this topic.
We deal with commutative and non-commutative algebraic geo metry. The latter notion
can be understood in several ways. There are many points of vi ew on the subject. We
touch universal algebraic geometry, some of its relations w ith reformational quantization
and Gr¨ obner basis in non-commutative situation.
The paper is organized as follows. Section 2 is devoted to various model-
theoretical aspects and their applications . More precisely, Section 2.1 deals with
universal algebraic geometry and is focused around the inte raction between algebra, logic,
model theory and geometry. All these subjects are collected under the roof of the diﬀerent
kinds of logical rigidity of algebras. Under logical rigidi ty we mean some logical invariants
of algebras whose coincidence gives rise to structural clos eness of algebras in question. If
such an invariant is strong enough then there is a solid groun d to look for isomorphism of
algebras whose logical invariants coincide.
We are comparing three types of logical description of algeb ras. Namely, we describe
geometric equivalence of algebras, elementary equivalenc e of algebras and isotypicity of
algebras. We look at these notions from the positions of univ ersal algebraic geometry
and logical geometry. This approach was developed by B. Plot kin and resulted in the
consistent series of papers where algebraic logic, model th eory, geometry and categories
come together. In particular, an important role plays the st udy of automorphisms of
categories of free algebras of the varieties. This question is highly related to description
of such objects as Aut(Aut)( A) and Aut(End)( A), where A is a free algebra in a variety.
SOME LOGICAL ASPECTS 3
We formulate the principal problems in this area and make a su rvey of the known
results. Some of them are very recent while the others are qui te classical. In any case we
shall emphasize that we attract attention to the widely open important problem whether
the ﬁnitely generated isotypic groups are isomorphic.
The line started in Section 2.1 is continued in Section 2.2 . Problems related to
universal algebraic geometry (i.e. algebraic geometry ove r algebraic systems) and logi-
cal foundations of category theory gave rise to natural ques tions on automorphisms of
categories and their auto-equivalences. The latter ones st imulate a new motivation to
investigation of semigroups of endomorphisms and groups of automorphisms of universal
algebras (Plotkin’s problem) (see [80]).
Let Θ be a variety of linear algebras over a commutative-asso ciative ring K and W =
W (X) be a free algebra from Θ generated by a ﬁnite set X. Let H be an algebra from Θ
and AGΘ (H) be the category of algebraic sets over H. Throughout the work, we refer to
[85, 86] for deﬁnitions of the Universal Algebraic Geometry (UAG).
The category AGΘ (H) is considered as the logical invariant of an algebra H. By
Deﬁnition 2.3, two algebras H1 and H2 are geometrically similar if the categories AGΘ (H1)
and AGΘ (H2) are isomorphic. It has been shown in [86], (cf., Propositio n 2.10) that
geometrical similarity of algebras is determined by the str ucture of the group Aut( T heta0),
where Θ 0 is the category of free ﬁnitely generated algebras of Θ. The l atter problem is
treated by means of Reduction Theorem (see [86], [43], [59], [93]). This theorem reduces
investigation of automorphisms of the whole category Θ 0 of free algebras in Θ to studying
the group Aut(End( W (X))) associated with W (X) in Θ 0.
In Section 2.2 we provide the reader with the results, descri bing Aut(End( A)), where
A is ﬁnitely generated free commutative or associative algeb ra, over a ﬁeld K.
We prove that the group Aut(End( A)) is generated by semi-inner and mirror auto-
morphisms of End( A) and the group Aut( A◦) is generated by semi-inner and mirror
automorphisms of the category of free algebras A◦.
Earlier, the description of Aut( A◦) for the variety A of associative algebras over alge-
braically closed ﬁelds has been given in [60] and, over inﬁni te ﬁelds, in [5]. Also in the
same works, the description of Aut(End( W (x1, x 2))) has been obtained.
Note that a description of the groups Aut(End( W (X))) and Aut(Θ ◦) for some other
varieties Θ has been given in [4, 5, 6, 18, 44, 50, 51, 60, 61, 62 , 59, 112].
A group of automorphisms of ind-schemes was computed in [42] . In investigating
the Jacobian conjecture and automorphisms of the Weyl algeb ra, Plotkin’s problem for
symplectomorphisms is also extremely important. Such prob lems are associated with
mathematical physics and the theory of D-modules.
Section 2.3 is devoted to mathematical physics and model theory. This relation
deals with nonstandard analysis. We refer the reader to the r eview [52].
The Belov–Kontsevich conjecture [37], sometimes Kanel-Be lov–Kontsevich conjecture,
dubbed B−KKC n for positive integer n, seeks to establish a canonical isomorphism be-
tween automorphism groups of algebras
Aut(An, C) ≃ Aut(Pn, C).
Here An, C is the n-th Weyl algebra over the complex ﬁeld,
An, C = C⟨x1, . . . , x n, y 1, . . . , y n⟩/ (xixj − xjxi, y iyj − yjyi, y ixj − xjyi − δij),
and Pn, C ≃ C[z1, . . . , z 2n] is the commutative polynomial ring viewed as a C-algebra and
equipped with the standard Poisson bracket:
{zi, z j} = ω ij ≡ δi,n +j − δi+n,j .
The automorphisms from Aut( Pn, C) preserve the Poisson bracket.
Let ζi, i = 1 , . . . , 2n denote the standard generators of the Weyl algebra (the imag es
of xj, y i under the canonical projection). The ﬁltration by total deg ree on An, C induces
4 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKIN , YU, AND ZHANG
a ﬁltration on the automorphism group:
Aut≤N (An, C) := {f ∈ Aut(An, C) | deg f (ζi), deg f −1(ζi) ≤ N, ∀i = 1, . . . , 2n}.
The obvious maps
Aut≤N (An, C) → Aut≤N+1(An, C)
are Zariski-closed embeddings, the entire group Aut( An, C) is a direct limit of the induc-
tive system formed by Aut ≤N together with these maps. The same can be said for the
symplectomorphism group Aut( Pn, C).
The Belov–Kontsevich conjecture admits a stronger form, wi th C being replaced by the
rational numbers. The latter conjecture will not be treated here in any way.
Since Makar-Limanov [53], [54], Jung [32] and van der Kulk [1 10], the B-KK conjecture
is known to be true for n = 1. The proof is essentially a direct description of the auto mor-
phism groups. Such a direct approach however seems to be comp letely out of reach for all
n > 1. Nevertheless, at least one known candidate for isomorphi sm may be constructed
in a rather straightforward fashion. The idea is to start wit h an arbitrary Weyl algebra
automorphism, lift it after a shift by a certain automorphis m of C to an automorphism
of a larger algebra (of formal power series with powers takin g values in the ring ∗Z of
hyperintegers) and then restrict to a subset of its center is omorphic to C[z1, . . . , z 2n].
This construction goes back to Tsuchimoto [106], who devise d a morphism
Aut(An, C) → Aut(Pn, C) in order to prove the stable equivalence between the Jacobi an
and the Dixmier conjectures. It was independently consider ed by Kontsevich and Kanel-
Belov [38], who oﬀered a shorter proof of the Poisson structu re preservation which does
not employ p-curvatures. It should be noted, however, that Tsuchimoto’ s thorough in-
quiry into p-curvatures has exposed a multitude of problems of independ ent interest, in
which certain statements from the present paper might appea r.
The construction we describe in detail in the following sect ions diﬀers from that of
Tsuchimoto in one aspect: an automorphism f of the Weyl algebra may in eﬀect undergo
a shift by an automorphism of the base ﬁeld γ : C → C prior to being lifted, and this
extra procedure is homomorphic. Taking γ to be the inverse nonstandard Frobenius
automorphism (see below), we manage to get rid of the coeﬃcie nts of the form a[p], with
[p] an inﬁnite prime, in the resulting symplectomorphism. The key result here is that for a
large subgroup of automorphisms, the so-called tame automo rphisms, one can completely
eliminate the dependence of the whole construction on the ch oice of the inﬁnite prime [ p].
Also, the resulting ind-group morphism ϕ [p] is an isomorphism of the tame subgroups.
In particular, for n = 1 all automorphisms of A1, C are tame (Makar-Limanov’s theorem),
and the map ϕ [p] is the conjectured canonical isomorphism.
These observations motivate the question whether for any n the group homomorphism
ϕ [p] is independent of inﬁnite prime.
The next Section 3 makes emphasis on algorithmic questions. First we dwell
on Non-Commutative Gr¨ obner basis. Questions of algorithm ic decidability in algebraic
structures have been studied since the 1940s. In 1947 Markov [63] and independently
Post [95] proved that the word equality problem in ﬁnitely pr esented semigroups (and in
algebras) cannot be algorithmically solved. In 1952 Noviko v constructed the ﬁrst example
of the group with unsolvable problem of word equality (see [7 0] and [71]). In 1962 Shirshov
proved solvability of the equality problem for Lie algebras with one relation and raised a
question about ﬁnitely deﬁned Lie algebras [100]. In 1972 Bo kut settled this problem. In
particular, he showed the existence of a ﬁnitely deﬁned Lie a lgebra over an arbitrary ﬁeld
with algorithmically unsolvable identity problem [8].
Nevertheless, some problems become decidable if a ﬁnite Gr¨ obner basis deﬁnes a rela-
tions ideal. In this case it is easy to determine whether two e lements of the algebra are
equal or not (see [3]). In his work, D. Piontkovsky extended t he concept of obstruction,
introduced by V. Latyshev (see [75, 76, 77, 78]). V.N. Latysh ev raised the question con-
cerning the existence of an algorithm that can ﬁnd out if a giv en element is either a zero
SOME LOGICAL ASPECTS 5
divisor or a nilpotent element when the ideal of relations in the algebra is deﬁned by a
ﬁnite Gr¨ obner basis.
Similar questions for monomial automaton algebras can be so lved. In this case the
existence of an algorithm for nilpotent element or a zero div isor was proved by Kanel-
Belov, Borisenko and Latyshev [35]. Note that these algebra s are not Noetherian and not
weak Noetherian. Iyudu showed that the element property of b eing one-sided zero divisor
is recognizable in the class of algebras with a one-sided lim ited processing (see [27], [28]).
It also follows from a solvability of a linear recurrence rel ations system on a tree (see [33]).
An example of an algebra with a ﬁnite Gr¨ obner basis and algor ithmically unsolvable
problem of zero divisor is constructed in [30].
A notion of Gr¨ obner basis(better to say Gr¨ obner-Shirshov basis) ﬁrst appeared in
the context of noncommutative (and not Noetherian) algebra . Note also that Poincar´ e-
Birkhoﬀ-Witt theorem can be canonically proved using Gr¨ ob ner bases. More detailed
discussions of these questions see in [8], [109], [35].
To solve these two problems we simulate a universal Turing ma chine, each step of which
corresponds to a multiplication from the left by a chosen let ter.
The problem of the algorithmic decidability of the existenc e of an isomorphism between
two algebraic varieties is extremely interesting and funda mental. A closely related problem
is the embeddability problem. In the general form, it is form ulated as follows.
Embeddability problem. Let A and B be two algebraic varieties. Determine
whether or not there exists an embedding of A in B. Find an algorithm or prove its
nonexistence.
In this paper, a negative solution to this problem is given ev en for aﬃne varieties over
an arbitrary ﬁeld of characteristic zero whose coordinate r ings are given by generators and
deﬁning relations.
