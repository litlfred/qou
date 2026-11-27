---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-001-11-background
section_title: "Background"
section_number: 1.1
pages: 1-3
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
involutive Lie algebra automorphism. Let k = {x ∈ g |θ(x) = x} denote the ﬁxed
Lie subalgebra. We call the pair of Lie algebras ( g, k) a symmetric pair. Assume
thatθ is of the second kind, which means that the standard Borel subalge bra b+ of
g satisﬁes dim(θ(b+) ∩ b+)< ∞. In this case the universal enveloping algebra U (k)
has a quantum group analog Bc,s =Bc,s(θ) which is a right coideal subalgebra of
the Drinfeld-Jimbo quantized enveloping algebraUq(g), see [Let99], [Let02], [Kol14].
We call (Uq(g),B c,s) a quantum symmetric pair.
The theory of quantum symmetric pairs was ﬁrst developed by M. No umi,
T. Sugitani, and M. Dijkhuizen for all classical Lie algebras in [Nou96], [N S95],
[NDS97], [Dij96]. The aim of this program was to perform harmonic analy sis on
quantum group analogs of compact symmetric spaces. This allowed a n interpre-
tation of Macdonald polynomials as quantum zonal spherical functio ns. Indepen-
dently, G. Letzter developed a comprehensive theory of quantum symmetric pairs
for all semisimple g in [Let99], [Let02]. Her approach uses the Drinfeld-Jimbo pre-
sentation of quantized enveloping algebras and hence avoids casew ork. Letzter’s
theory also aimed at applications in harmonic analysis for quantum gro up analogs
of symmetric spaces [Let04], [Let08]. The algebraic theory of quant um symmetric
pairs was extended to the setting of Kac-Moody algebras in [Kol14].
Over the past two years it has emerged that quantum symmetric pa irs play an
important role in a much wider representation theoretic context. I n a pioneering
2010 Mathematics Subject Classiﬁcation. 17B37; 81R50.
Key words and phrases. Quantum groups, coideal subalgebras, universal K-matrix, quantum
symmetric pairs, reﬂection equation.
Research supported by EPSRC grant EP/K025384/1.
1
2 MARTINA BALAGOVI ´C AND STEF AN KOLB
paper H. Bao and W. Wang proposed a program of canonical bases f or quan-
tum symmetric pairs [BW13]. They performed their program for the symmetric
pairs ( sl2N, s(glN × glN )) and ( sl2N +1, s(glN × glN +1)) and applied it to establish
Kazhdan-Lusztig theory for the category O of the ortho-symplectic Lie superalge-
bra osp(2n+1 | 2m). Bao and Wang developed the theory for these two examples
in astonishing similarity to Lusztig’s exposition of quantized enveloping algebras
in [Lus94]. In a closely related program M. Ehrig and C. Stroppel show ed that
quantum symmetric pairs for ( gl2N, glN × glN ) and ( gl2N +1, glN × glN +1) appear
via categoriﬁcation using parabolic category O of type D [ES13]. The recent devel-
opments as well as the previously known results suggest that quan tum symmetric
pairs allow as deep a theory as quantized enveloping algebras themse lves. It is
reasonable to expect that most results about quantized envelopin g algebras have
analogs for quantum symmetric pairs.
One of the fundamental properties of the quantized enveloping alg ebra Uq(g) is
the existence of a universal R-matrix which gives rise to solutions of the quantum
Yang-Baxter equation for suitable representations of Uq(g). The universal R-matrix
is at the heart of the origins of quantum groups in the theory of qua ntum integrable
systems [Dri87], [Jim85] and of the applications of quantum groups to invariants
of knots, braids, and ribbons [RT90]. Let ∆ : Uq(g) → Uq(g) ⊗Uq(g) denote the
coproduct of Uq(g) and let ∆op denote the opposite coproduct obtained by ﬂipping
tensor factors. The universal R-matrix RU of Uq(g) is an element in a completion
U (2)
0 ofUq(g) ⊗Uq(g), see Section 3.2. It has the following two deﬁning properties:
(1) In U (2)
0 the element RU satisﬁes the relation ∆(u)RU =RU∆op(u) for all
u ∈Uq(g).
(2) The relations
(∆ ⊗ id)(RU ) = RU
23RU
13, (id ⊗∆)(RU ) = RU
12RU
13
hold. Here we use the usual leg notation for threefold tensor prod ucts.
The universal R-matrix gives rise to a family ˆR = (RM,N ) of commutativity iso-
morphisms ˆRM,N : M ⊗N → N ⊗M for all category O representations M,N of
Uq(g). In our conventions one has ˆRM,N =RU ◦ ﬂipM,N where ﬂipM,N denotes the
ﬂip of tensor factors. The family ˆR can be considered as an element in an extension
U (2) of the completion U (2)
0 of Uq(g) ⊗Uq(g), see Section 3.3 for details. In U (2)
property (1) of RU can be rewritten as follows:
(1’) In U (2) the element ˆR commutes with ∆(u) for all u ∈Uq(g).
By deﬁnition the family of commutativity isomorphisms ˆR = ( ˆRM,N ) is natural in
M and N . The above relations mean that ˆR turns category O for Uq(g) into a
braided tensor category.
The analog of the quantum Yang-Baxter equation for quantum sym metric pairs
is known as the boundary quantum Yang-Baxter equation or (quan tum) reﬂection
equation. It ﬁrst appeared in I. Cherednik’s investigation of facto rized scattering
on the half line [Che84] and in E. Sklyanin’s investigation of quantum inte grable
models with non-periodic boundary conditions [Skl88], [KS92]. In [KS92, 6.1] an
element providing solutions of the reﬂection equation in all represen tations was
called a ‘universal K-matrix’. Explicit examples of universal K-matrice s for Uq(sl2)
appeared in [CG92, (3.31)] and [KSS93, (2.20)].
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 3
A categorical framework for solutions of the reﬂection equation w as proposed by
T. tom Dieck and R. H¨ aring-Oldenburg under the name braided tens or categories
with a cylinder twist [tD98], [tDHO98], [HO01]. Their program provides an exten-
sion of the graphical calculus for braids and ribbons in C × [0, 1] as in [RT90] to
the setting of braids and ribbons in the cylinder C∗ × [0, 1], see [HO01]. It hence
corresponds to an extension of the theory from the classical bra id group of type
AN −1 to the braid group of type BN . Tom Dieck and H¨ aring-Oldenburg called the
analog of the universal R-matrix in this setting a universal cylinder t wist. They
determined a family of universal cylinder twists for Uq(sl2) by direct calculation
[tDHO98, Theorem 8.4]. This family essentially coincides with the univers al K-
matrix in [KSS93, (2.20)] where it was called a universal solution of the reﬂection
equation.
