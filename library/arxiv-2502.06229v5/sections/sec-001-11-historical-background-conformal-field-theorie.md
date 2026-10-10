---
doc_id: arxiv-2502.06229v5
doc_title: "Constructing equivalences between fusion categories of quantum groups and of vertex operator algebras via quantum gauge groups"
section_id: sec-001-11-historical-background-conformal-field-theorie
section_title: "Historical Background: Conformal Field Theories and Quantum Groups"
section_number: 1.1
pages: 1-4
source_pdf: 2502.06229v5.pdf
source_sha256: 3499c40ea150a617
toc_source: outline
doc_brief: "Constructing equivalences between fusion categories of quantum groups and of vertex operator algebras via quantum gauge groups — This paper establishes connections between a problem posed by"
---
Primary fields, introduced under a different name by Mack and Salam in the context
of higher-dimensional conformal field theories [68], were investigated in 2D by Belavin,
Polyakov, and Zamolodchikov. They recognized that the local symmetry algebra is given
by the infinite-dimensional Virasoro algebra [5], building upon previous work by Feigin
and Fuchs [29] and Kac [62] on its representation theory.
Witten introduced an interacting 2D conformal field theory, now known as the Wess-
Zumino-Witten (WZW) model [103]. He showed that this model possesses a symmetry
1
arXiv:2502.06229v5  [math.OA]  14 Apr 2026
2
C. PINZARI
satisfying the relations of an affine Kac-Moody algebra. In the same year, Knizhnik and
Zamolodchikov showed that the correlation functions of a WZW model satisfy a system of
partial differential equations [65]. This Kac-Moody framework was related to the Virasoro
algebras by Goddard, Kent and Olive [37], who introduced the coset construction to realize
Virasoro minimal models directly from WZW models.
The mathematical formulation of the KZ equations was made rigorous by Tsuchiya and
Kanie [95], who studied the model for ˆsl2 and showed that the associated monodromy
yields representations of the braid group that factor through the Hecke algebra at a root
of unity.
The discovery of quantum groups first arose in physics literature in the work by Faddeev,
introduced as noncommutative function algebras. In the mid 80s breakthrough papers by
Drinfeld and Jimbo discovered them as quantization of universal enveloping algebras, and
developed their properties.
We refer to [8] for an in-depth presentation and historical
information.
Kohno proved that the monodromy representations of the KZ equations are equivalent
to those derived from the universal R-matrix of a quantum group [66]. Before recalling
the subsequent deep developments of the theorem by Kohno, we need first review the
emergence of tensor categories in constructive conformal field theory.
Moore and Seiberg [73], [74] derived certain equations from rational conformal field
theory and discovered a connection between their equations and the structure of a tensor
category. The corresponding mathematical framework, specifically the notion of ribbon
braided tensor category, has since been settled in mathematics, we refer to [26], [27], and
references therein.
An independent derivation of strict braided tensor C∗-categories arose from the ax-
iomatic operator algebraic approach to QFT in the 1970s, see [20], [76], [45] and references
therein. The connections between tensor C∗-categories and compact quantum groups are
studied [80].
Turaev gave a definition of modular tensor category, based on previous work with
Reshetikhin on the construction of knot and 3-manifold invariants see [96]. Several au-
thors contributed to construct modular fusion categories form quantum groups at roots of
unity, and a more complete historical account on the quantum group side may be found
in [90], [92], see also the introduction of [10]. We denote by C(g, q) the resulting modular
fusion category, with q = eiπ/dℓ, and d ∈{1, 2, 3} a suitable integer structure constant from
Lie theory. Unitary tensor structures have been constructed by Wenzl and Xu [99], [105].
Wenzl’s work plays a major role in our work, and we try to explain this in this paper.
In the constructive approach to CFT, the Wess-Zumino-Witten model is of central in-
terest.
Modular, or more generally ribbon rigid braided tensor category constructions
involved many authors among physicists and mathematicians. A main difficulty in con-
structing tensor categories from models of conformal field theories is the construction of
the associativity morphisms compatible with naturally assigned braiding morphisms via
the two hexagonal equations. Another main difficulty is to show rigidity of the category.
Non-strict examples motivated by conformal field theory arose from the work of Drin-
feld on quasi-Hopf algebras [24]. Let g be a complex simple Lie algebra. The mentioned
3
problems were first solved by Drinfeld in [22], [24] [25] for the Drinfeld category with the
introduction of the notion and construction of non-trivial examples of quasi-Hopf algebras
over U(g)[[h]], via the KZ differential equation. Drinfeld used this equation to construct
the associativity morphisms compatible with naturally assigned braiding morphisms. Fur-
thermore he established rigidity of this category by showing a remarkable ribbon, braided
tensor equivalence with the module category arising from the quantized universal envelop-
ing algebra Uh(g), which is a Hopf algebra. To construct the ribbon, braided, tensor equiv-
alence, he used Drinfeld coboundary matrix R, which is a modification of the R-matrix by
a square root of the coboundary defined by the ribbon structure.
This is his remarkable Drinfeld-Kohno theorem, expanding the earlier theorem by Kohno
[66]. Drinfeld-Kohno theorem connects via a Drinfeld twist, the quasi-Hopf algebra U(g)[[h]]
with the quantized universal enveloping algebra Uh(g). In particular, the representations of
the braid group arising from monodromy of the KZ equation are shown equivalent to those
arising from the action of the R-matrix of Uh(g) with respect to the vector representation,
for the classical Lie types.
Major work was carried out in a series of papers by Kazhdan and Lusztig in the mid 90s
in the setting of affine Lie algebras. The authors construct rigid braided tensor structures
for certain module categories of affine Lie algebras associated to g at shifted levels excluding
the non negative rationals. For convenience we denote by −ℓthe shifted levels allowed by
Kazhdan and Lusztig. In their work they proved a braided tensor equivalence of their
category O−ℓwith the non-semisimple category of certain modules of the Drinfeld-Jimbo
quantum group Uq(g) at the root of unity q = eiπ/dℓ, with d the ratio of the square lenghts
of the long to the short root, with the exception of some cases [63].
With k a positive integer, defined as the physical level, and ℓ= k + ˇh, with ˇh the dual
Coxeter number of g, Finkelberg considered a certain semisimple subquotient ˜O−ℓof the
representation category constructed by Kazhdan and Lusztig, paralleling the subquotient
construction of the quantum group fusion category C(g, q) in the setting of quantum groups
at roots of unity. He defined an equivalence ˜Oℓ→˜O−ℓfrom the category ˜Oℓof certain
integral modules of the affine Lie algebra at level k introduced by Beilinson, Feigin, and
Mazur to the subquotient rigid braided tensor category ˜O−ℓ. Combining with the equiva-
lence by Kazhdan and Lusztig, Finkelberg derived an equivalence between ˜Oℓ→C(g, q).
See the introduction and Theorem 4.3 in [30].
While the equivalence between quantum group fusion categories and categories of mod-
ules of affine Lie algebras at positive integer level was proposed in the mid 1990s, the
complete proof of rigidity of ˜Oℓand derivation of the tensor equivalence was given in 2013
using the Verlinde formula [31] building on work by Faltings and Teleman. We refer the
reader to the appendix for more historical remarks concerning the proof of rigidity for
affine vertex operator algebras and affine Lie algebras at positive integer levels.
The ribbon braided tensor equivalence established in [30], [31] relies on a passage through
negative levels and then applies the equivalence with the quantum group fusion category by
Kazhdan and Lusztig. As a consequence, Finkelberg’s proof excludes certain exceptional
cases like g = E8 at level k = 2 since this case is excluded in [63].
4
C. PINZARI
1.2. Huang’s Problem. This led us to consider the following problem posed by Y.-Z.
Huang in [58].
Problem 4.4 in [58]. Find a direct construction of this equivalence without using the
equivalence given by Kazhdan-Lusztig so that this equivalence covers all the cases, including
the important g = E8 and k = 2 case.
Moreover, in light of Drinfeld’s construction of the ribbon braided tensor equivalence in
Drinfeld-Kohno theorem, and his consequent derivation of rigidity of the Drinfeld category,
is natural to ask whether the Verlinde formula is necessary to prove rigidity, and whether
rigidity is necessary to prove the ribbon braided tensor equivalence ˜Oℓ→C(g, q).
We also mention Gannon’s observation in Sect. 6.2.3 of [35] regarding the desire of
finding a direct connection between quantum groups and CFT. Our work provides a direct
constructive method–addressing Huang’s Problem 4.4 in [58]–by utilizing a global quantum
gauge group method originating in algebraic quantum field theory, and the Zhu algebra to
establish the equivalence.
From the side of mathematical axiomatizations of CFT, Huang and Lepowsky have
done extensive work on the construction of tensor structures of modules and showing all
the properties of modular tensor category [47], [48], [49], [50], [51], [52], [53], [54], [55], [56].
An explicit construction of the equivalence is helpful to see how rigidity, modularity or
unitarity in the setting of CFT may be transported from corresponding results in the setting
of quantum groups at roots of unity, which seem simpler, by our explicit equivalence.
