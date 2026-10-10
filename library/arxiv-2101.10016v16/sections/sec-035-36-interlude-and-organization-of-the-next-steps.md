---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-035-36-interlude-and-organization-of-the-next-steps
section_title: "Interlude and organization of the next steps"
section_number: 36
pages: 222-224
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
36. Interlude and organization of the next steps
In Sect. 8 we outlined our strategy for the proof Theorem 2.11. Recall Def. 8.8 of
V-preassociator of CFT-type. In Sect. 19 we started to develop and apply the strategy to
quantum group fusion categories. Our aim is to complete the proof of Theorem 2.8.
So far regarding this theorem, we have worked on the side of quantum groups. We have
constructed a unitary coboundary weak quasi-bialgebra structure on A(Vgk), which induces
a unitary ribbon modular tensor category structure on Rep(A(Vgk)). We have proved parts
(a) and (b) of Theorem 2.8. In Theorem 33.7 we have shown that the associator of A(Vgk)
induced from the quantum group, restricts to a V-preassociator of CFT-type, building on
the work of Wenzl on the unitary structure of the fusion category. We need to prove part
(c) of the same theorem.
On the side of vertex operator algebras, Huang and Lepowsky have introduced and
constructed a vertex modular tensor category structure in module categories of a general
class of vertex operator algebras [85], [86], [87], [88]. They have shown that a vertex
modular tensor category structure induces in a natural way a modular tensor category
structure on the same category [84].
In Sect. 37 we sketch a description of Huang-Lepowsky vertex tensor category structure
and the associated tensor category structure. Let us consider their ribbon tensor category
structure in the case of Rep(Vgk), with k a positive integer. This special case has been
studied in [89].
Part (c) of Theorem 2.8 is reformulated in Theorem 2.11 (c), and diagram (2.4) describes
the methods that we intend to use to study this part. The proof of tensor preserving
equivalence of the first map of the diagram (2.4) will be considered in Subsects. 37.3, 37.4.
We refer the reader to [149] for further explanations on this program, and for the developments of the abstract aspects of the original remark.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 223
We were not aware at the time of working on our paper, of the beautiful paper [127]2
where transport methods similar to these of our Sect. 15 are developed. Note that McRae
does not use of weak quasi-Hopf algebras, but we strongly advise this paper. For the
present paper we follow methods as discussed in the last years for this project, and we
have kept the original arguments in the presentation of Sects. 37, 38.
The arguments are as follows. The mentioned proof will break in two steps. The first
step transports Huang-Lepowsky vertex ribbon tensor category structure of Rep(V ) to the
representation category of the Zhu algebra Rep(A(V )) via Zhu’s functor Z, and this is the
content of Subsect. 37.3, except for the braiding that is considered separately in Sect. 34
and relies on Toledano-Laredo exposition in the application V = Vgk
.
The second step compares this transported vertex tensor category structure of the Zhu
algebra for V = Vgk with the structure arising from side of quantum groups summarized
in the first two paragraphs of this section.
The comparison with the transported associativity morphisms of Huang and Lepowsky
relies on the notion of primary field introduced by Knizhnik and Zamolodchikov [114], the
work Tsuchiya and Kanie and Fenkel and Zhu in Subsect. 37.3, which reduces infinite
dimensional representations to finite dimensional representations of the Zhu algebra in a
natural (vertex) tensor categorical way. This is a specific property of the model and the
identification is given by certain linear maps, part of a natural transformation, that uses
the clarity of the work by Wenzl on the unitary structure on triples of representations
of which two terms are the fundamental representation and the remaining term is an
arbitrary irreducible, for all Lie types on the side of quantum groups, which we show to be
a significative class of triples. On the side of conformal field theory, the identifying linear
maps uses the lack of logarithmic terms of certain solutions of a one-variable KZ equation,
considered in [170] and [91]. This indicates that an approach via unitarity is parallel to
that vis the KZ equation.
The comparison between the Huang-Lepowsky associator on the Zhu algebra and the
CFT-type pre-associator on the same algebra from Theorem 2.8 is discussed in Subsect.
37.4. This part relies on the fact that the two tensor product bifunctors may be identified.
At the level of affine Lie algebras, an explanation of this identification was given in Theorem
34.7, and already at this level in turn relies on the central notion of primary field first
introduced by Knizhnik and Zamolodchikov and studied by Tsuchiya and Kanie [114],
[170]. In the setting of vertex operator algebras, identification of the two tensor product
bifunctors on the Zhu algebra again based on the corresponding notion of primary field
will be discussed in Sect. 38.
More precisely, to discuss tensor equivalence of the second step we first need to compare
the two pre-tensor structures. Theorem 34.7 relates the spaces of initial terms of primary
fields in the setting of loop groups with the tensor product of Rep(A(Vgk)) constructed in
Sect. 33. To make this result useful, we need to relate primary fields in the setting of loop
groups with primary fields in the setting of vertex operator algebras. This will be done in
2CP is grateful to M. Yamashita for a discussion leading to [127]

224 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Sect. 38. Then the equivalence of the two associativity morphisms follows from the fact
that Huang-Lepowsky associativity morphisms on the Zhu algebra is of CFT-type.
In Subsect. 38.1 we discuss the notion of primary fields in the setting of vertex operator
algebras. In Subsect. 38.2 we discuss the correspondence with the setting of Sect. 34 and
re-interpret Theorem 34.7 in this setting. This gives a correspondence of the two pre-tensor
category structures on the Zhu algebra.
Then we will identify the two tensor product bifunctors on Rep(A(Vgk
)) arising from
Huang-Lepowsky tensor product theory and from Theorem 2.8.
Since the second and last maps of the diagram (2.4) are a ribbon tensor equivalences
by the indicated Theorems, completion of the proof of Theorems 2.8 (c) and also of the
main Theorem 2.11 reduces to prove the identification of the associativity morphisms and
braiding morphisms of the first map in (2.4) by comparing the braided tensor category
structure on Rep(A(Vgk
)) obtained in parts (a) and (b) of the same Theorem 2.8 with
those of the braided tensor category structure on Rep(A(Vgk
)) induced by Huang-Lepowsky
braided tensor category structure of Rep(Vgk).
Regarding the comparison of the two associativity morphisms and the two braiding morphisms on Rep(A(Vgk
)), we recall that on the side of quantum groups, Theorem 33.7 gives
the explicit evaluation of the associator of A(Vgk
) derived from Theorem 2.8 (a) on the special triples of representations with two terms occupied by the fundamental representation
of the classical Lie algebra and the remaining term occupied by an arbitrary irreducible
representation in the Weyl alcove. The theorem describes this associator as an associator
extending the V-pre-associator of CFT-type associated to (F0, G0) and to the collection V
of these special triples. For the braided symmetries, theorems 33.11 and Corollary 35.1
identify the braiding morphisms for all pairs with one term occupied by the fundamental
representation. We show in Subsect. 37.4 that the associator on Rep(A(Vgk)) arising from
Huang-Lepowsky tensor category structure restricts to the CFT-type pre-associator associated to (F0, G0) on the same special triples V. The conclusion will follow as an application
of the uniqueness Theorem 8.21, provided the assumption on the generating properties of
the braid group are satisfied. These assumptions have been verified in Sect. 11 of [149],
based on the existing literature, and leads to the restricted Lie types as stated.
We note that an interesting problem is to develop more explicitly the connection between
our unitary structure on the Zhu algebra, the CPT operator and also with the papers by
Gui, a statement of which may be found in 2.8 (d). The Hermitian form of the unitary wqh
A(Vgk) conjecturally coincides with that of Gui in the setting of vertex operator algebras
[73, 74]. We postpone the development of Theorem 2.8 (d).
