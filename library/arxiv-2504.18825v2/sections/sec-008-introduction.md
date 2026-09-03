---
doc_id: arxiv-2504.18825v2
doc_title: "MURNAGHAN\u2013NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS NAIHUAN JING AND NING LIU"
section_id: sec-008-introduction
section_title: "Introduction"
section_number: 1
pages: 2-7
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
doc_brief: "MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS NAIHUAN JING AND NING LIU — 16 sections: Introduction; Preliminaries; Murnaghan–Nakayama rule for the cy"
---
1.1. Background. The Murnaghan–Nakayama rule [Mur37, Nak41a, Nak41b] serves as
a combinatorial algorithm for calculating the irreducible characters of symmetric groups
Sn . The Iwahori–Hecke algebra Hn (q) in type A, which is the q-deformation of Sn , is a
unital associative algebra over the field of rational functions C(q). Ram [Ram91] used the
quantum Schur–Weyl duality [Jim86] to establish a Frobenius-type character formula for
Hn (q), linking it to one-row Hall-Littlewood functions and Schur symmetric functions (see
also [KV89, KW92]). He also introduced the q-Murnaghan–Nakayama rule, an iterative
combinatorial method for computing irreducible characters using smaller partitions. An
alternative approach was explored in [Pfe94]. Recent work [JL22] employed the vertex
operator realization of Schur functions to revisit the q-Murnaghan–Nakayama rule. This
approach has led to the formulation of a Murnaghan–Nakayama rule for the Hecke–Clifford
algebra [JL23], utilizing the vertex operator realization of Schur Q-functions.
At the end of [Pfe97], Pfeiffer noted the potential for deriving irreducible character formulas for the cyclotomic Hecke algebra Hm,n (q, u) over some specific elements, yet evidence
was lacking to show that these character values could yield a complete character table. This
raises the question of which elements can determine the characters and how to derive the
character values for others. In 1998, inspired by Greene’s derivation of the Murnaghan–
Nakayama formula via Young’s seminormal representations [Gre92], Halverson and Ram
[HR98] established an analogue of the Murnaghan–Nakayama rule for Hm,n (q, u), focusing on certain “standard elements”. They claimed, without proof, that these values would
completely determine the characters. Subsequently, a result by Mak [Mak08] confirms that
the characters of Hm,n (q, u) can be determined by the values of the “standard elements”
through a highly complicated process.
In 2000, Shoji [Sho00] utilized Schur–Weyl reciprocity between Hm,n (q, u) and a Levi
subalgebra of the quantized enveloping algebra Uq (glm ) [SS99] to provide a Frobenius-type
formula for the characters of Hm,n (q, u). He introduced a new presentation and standard
elements for Hm,n (q, u), proving that the characters are completely determined by their
values on these elements [Sho00, Proposition 7.5], addressing Pfeiffer’s earlier question.
In contrast to the “standard elements” mentioned above, Shoji’s version of “standard
elements” has simpler forms.
In 2013, Regev [Reg13] obtained an elegant formula, now usually referred to as the Regev
formula, for the characters of super representations of the symmetric group. This result was
derived through the super analogue of the classical Schur–Weyl duality (sometimes called
the Schur-Sergeev duality), combined with the combinatorial theory of Lie superalgebras,
which was initially developed by Sergeev [Ser84] and later expanded in detail by Berele
and Regev [BR87]. Taylor [Tay17] provided a new proof of Regev’s work by utilizing the
Murnaghan–Nakayama formula for the skew characters of symmetric groups. Building on
Taylor’s work, Zhao [Zha19] extended the (quantum) Regev formula to the Iwahori–Hecke
algebra of type A by employing the corresponding Murnaghan–Nakayama rule for skew
characters. An alternative proof of the quantum Regev formula was recently presented in
[JL22] using the vertex operator realization of Schur functions.


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS3

In [LP21], Lübeck and Prasad established a character identity that connects the irreducible character values of the Weyl group W2,n to those of the symmetric group S2n using
the Frobenius character formula for symmetric groups. Subsequently, Adin and Roichman [AR22] provided a combinatorial proof of this identity and extended it to the setting
of wreath products. We collectively refer to these results as the Lübeck–Prasad–Adin–
Roichman formula.
The second orthogonality relation for the irreducible characters of a finite group plays
a crucial role in computing these characters. The second orthogonality relation for the
irreducible characters of a split semisimple algebra also makes sense. An explicit form
of the second orthogonality relation for the irreducible characters of the Brauer algebra
was given in [Ram97]. The q-analogue of the second orthogonality relation for the Hecke
algebra of type A formulated in terms of the bitrace was determined in [HLR97, JL22].
A spin analogue of the bitrace was recently developed for the Hecke–Clifford algebra in
[JL23].
1.2. Aims. While the earlier Murnaghan–Nakayama-type formulas of Halverson–Ram are
fundamental, they are not fully suited to our present purposes. In particular, Halverson
and Ram computed characters only on certain “standard elements” and did not prove in
that paper that these values determine the full character table (although they indicated a
method for doing so later). Moreover, their approach relies on explicit seminormal/Hoefsmittype representations together with double-centralizer (Clifford-theoretic) arguments and a
bitrace reduction. This framework is structurally powerful, but less convenient for the
Frobenius-formula-based combinatorial recursions and applications that we pursue here.
Mak later resolved the determinacy issue from a structural viewpoint via a reducibility
theorem for trace functions on Ariki–Koike algebras, but this is of a different nature and
does not directly provide an explicit iterative combinatorial character formula. By contrast,
Shoji’s Frobenius-type formula and his choice of standard elements offer a natural starting
point for such a development.
This paper has two main goals. First, we formulate a Murnaghan–Nakayama rule for
the cyclotomic Hecke algebra based on Shoji’s Frobenius-type formula, together with an
effective operational procedure for computing character values. Compared with earlier formulations, our rule has a more canonical form and specializes uniformly to several known
formulas, including those for the complex reflection group of type G(m, 1, n) and the
Iwahori–Hecke algebras of types A and B. In addition, combined with Shoji’s result [Sho00,
Proposition 7.5], it provides a simpler route to the complete character table of Hm,n (q, u).
Second, in a dual framework based on the vertex-operator realization of Schur functions,
we derive an iterative formula on upper multipartitions, which may be viewed as a dual
Murnaghan–Nakayama rule for the cyclotomic Hecke algebra.
Our second aim is to demonstrate the scope of these rules through several applications.
We obtain a Regev-type formula for the cyclotomic Hecke algebra, establish a Lübeck–
Prasad–Adin–Roichman-type formula that computes character values via partitions rather
than multipartitions, and introduce the notion of multiple bitrace together with a general combinatorial formula. These applications illustrate the practical strength of the new


4

NAIHUAN JING AND NING LIU

Algebras

Symmetric functions

Skew diagrams

symmetric group Sn

Schur function sλ

ribbon

Hecke algebra (type A) Hn

Schur function sλ

generalized ribbon

Hecke algebra (type B) Bn

double Schur function s(λ,µ)

double generalized ribbon

Sergeev algebra Cn ⋊ Sn

Schur Q-function Qλ

double strip

Hecke–Clifford algebra
Cn ⋊ Hn

Schur Q-function Qλ

generalized double strip

complex reflection group
Wm,n

multi-Schur function sλ

multi-ribbon

cyclotomic Hecke algebra
Hm,n (q, u)

multi-Schur function sλ

generalized multi-ribbon

Table 1. Murnaghan–Nakayama rules for various algebras
Murnaghan–Nakayama rule and do not seem to be readily accessible from the earlier formulas. They also extend the corresponding formulas discussed in Subsection 1.1.
1.3. Main results. We now summarize the main results of the paper. In the Hecke algebra
of type A, the Murnaghan–Nakayama rule is naturally expressed in terms of generalized
ribbons. In the cyclotomic setting, the corresponding combinatorial objects become generalized multi-ribbons, namely m-tuples of generalized ribbons. When m = 1, the cyclotomic
Hecke algebra reduces to the Hecke algebra of type A, and generalized multi-ribbons reduce
exactly to generalized ribbons. In this sense, our construction is a genuine extension of the
type A picture.
More broadly, our result fits into a unified pattern relating character formulas, symmetric functions, and skew-diagram combinatorics. Table 1 summarizes Murnaghan–Nakayama
rules for several algebras. The present work completes the last line of the table and simultaneously generalizes the cases of the symmetric group, Hecke algebras of types A and B,
and the complex reflection group Wm,n .
Our first main result is a recursive Murnaghan–Nakayama rule for irreducible characters
of the cyclotomic Hecke algebra, formulated directly on Shoji’s standard elements.


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS5

Theorem A (Corollary 3.4). Let λ and µ be two multipartitions of n, and let χλµ be the
value of the irreducible character indexed by λ at the standard element g(µ). Then
(r)

χλµ =

X q µj
wt(λ/ν; q −2 , u, r)χνµ\µ(r) ,
−1
q−q
j
ν

(1.1)
(r)

where the sum runs over all multipartitions ν ⊂ λ such that λ/ν is a µj -generalized
(r)
multi-ribbon. Here µ \ µj is obtained from µ by deleting the j-th row of the r-th partition,
and wt(λ/ν; q −2 , u, r) is the explicit weight defined in (3.4).
Iterating Theorem A yields a tableau-type expansion formula: the character value χλµ can
be written as a weighted sum over generalized multi-ribbon tableaux of shape λ and content
µ (Corollary 3.7). This provides a fully combinatorial global formula, complementing the
recursive version above.
In addition to the above (“lowering”) recursion, we establish a dual iterative formula
in the opposite direction (Corollary 5.6), derived from the vertex operator realization of
Schur functions. This dual formula expresses a character as a linear combination of characters indexed by multipartitions with strictly smaller upper data, and therefore gives a
complementary computational mechanism to the Murnaghan–Nakayama rule.
We next turn to applications. The first application is a Regev-type formula for the
permutation super representation of Hm,n (q, u).
Theorem B (Theorem 6.1). Let µ be a m-multipartition of n. Then the value of the
character of the permutation super representation on the standard element g(µ) is given
by
χu,q
k|l;n (g(µ))
(r)

=q

n−l(µ)

m l(µ
Y
Y)

X

r=1 j=1 (α;β)∈C(µ(r) ;k|l)
j

→
(1 − q −2 )l(α;β)−1 (−q −2 )|β|−l(β)
ur−
l (α;β)



m 
Y
ki
li
.
l(α(i) ) l(β (i) )
i=1
(1.2)

→
−
(r)
Here C(µj ; k | l) is defined in Sec. 6, l (α; β) := max{1 ≤ i ≤ m | l(α(i) ) + l(β (i) ) > 0},
and l(α; β) := l(α) + l(β).
A special case of Theorem B yields a hook-sum formula (Cor. 6.3) for irreducible characters indexed by multipartitions all of whose components are hooks. We also provide an
alternative proof of this formula in Appendix A.
Our second application is a cyclotomic Hecke algebra analogue of the Lübeck–Prasad–
Adin–Roichman formula. It expresses irreducible characters indexed by multipartitions in
terms of data attached to the corresponding partition with empty m-core.


6

NAIHUAN JING AND NING LIU

Theorem C (Theorem 7.10). Let λ = (λ(1) , λ(2) , · · · , λ(m) ) and µ ∈ Pn,m , and let λ be the
unique partition with empty m-core and m-quotient λ. Then
χλµ = q n−l(µ)

m
X

X

ητλ;r ,

(1.3)

r=1 τ ∈Pm (µ(r) )

where ητλ;r is the partition-based quantity introduced in Definition 7.9.
Under the specialization u = ζ = (1, ζ, ζ 2 , · · · , ζ m−1 ), q = 1, and µ = (∅, · · · , ∅, µ),
Theorem E specializes to the Adin-Roichman formula for the complex reflection group
Wm,n .
Finally, we introduce the notion of multiple bitrace for Hm,n (q, u) and derive an explicit
combinatorial formula. This may be viewed as a cyclotomic analogue of the bitrace formulas
known in types A and related settings.
Theorem D (Theorem 8.3). Let µ and ν be two multipartitions of n. Then
m
X
Y
q 2n
mbtr(µ, ν) =
uM uN
wtq−2 (A(i) ),
(q − q −1 )l(µ)+l(ν) M ,N ,A
i=1

(1.4)

where the sum runs over pairs of m-multimatrices (M , N ) and m-tuples of matrices A satisfying the conditions stated in Theorem 8.3. Here uM and wtq (A(i) ) are the corresponding
weight polynomials attached to M and A(i) , respectively.
P
By specialization, the left-hand side and right-hand side of (1.4) reduce to λ∈Pn,m ϕλµ ϕλν
Q
and δµ,ν ml(µ) m
i=1 zµ(i) , respectively, and thus Theorem F recovers the second orthogonality
relation for irreducible characters of Wm,n :

m
ml(µ) Q z (i) , if µ = ν,
X
µ
ϕλµ ϕλν =
(1.5)
i=1

0,
otherwise,
λ∈Pn,m
Q
where zλ := i≥1 imi (λ) mi (λ)! for a partition λ.
1.4. Organization. The layout of this paper is as follows. In the next section, we will
briefly review key terminologies related to multipartitions and symmetric functions indexed by multipartitions, along with a recapitulation of Shoji’s Frobenius formula. In Sec.
3, we will present our Murnaghan–Nakayama rule, accompanied by several straightforward
examples. Sec. 4 focuses on three special cases of the Murnaghan–Nakayama rule, demonstrating how our rule recovers existing formulas for the complex reflection group of type
G(m, 1, n), as well as for Hecke algebras of type A and type B. In Sec. 5, we provide an
alternative computational formula (dual Murnaghan–Nakayama rule) for the irreducible
characters in a dual picture, utilizing the vertex operator realization of Schur functions.
In Sec. 6, we present the first application of our Murnaghan–Nakayama rule: the Regev


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS7

formula for the cyclotomic Hecke algebra. We extend the work of Lübeck–Prasad–Adin–
Roichman to the setting of the cyclotomic Hecke algebra in Sec. 7. Sec. 8 concentrates on
the multiple bitrace of irreducible characters, followed by the presentation of a combinatorial formula for it. In Appendix B, we show how to use the Sagemath program [Sag25] to
compute the irreducible character tables (χλµ )λ,µ∈Pn,m via our Murnaghan–Nakayama rule.
