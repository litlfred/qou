---
doc_id: ram1991-frobenius-formula
doc_title: "A Frobenius formula for the characters of the Hecke algebras"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: "0"
pages: 1-2
source_pdf: ram1991-frobenius-formula.pdf
source_sha256: 26b2fc85338d9150
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
doc_brief: "A Frobenius formula for the characters of the Hecke algebras — This paper uses the theory of quantum groups and the quantum Yang-Baxter equation as a guide in order to produce a method of computing"
---
O Introduction
In 1900, in a remarkable paper [Fr], Frobenius gave a formula and a method of
computing the characters of the symmetric group. This method was later used to
give a completely combinatorial rule for the computation of the characters of the
symmetric group, often referred to as the Murnaghan-Nakayama rule, see [Mac,
Chapter I. Example 9J. In his study of the representations of the general linear
group Gl(n), I. Schur [Sc1, Sc2J showed that the Frobenius method can be
obtained by way of a reciprocity between the Gl(n) and the symmetric group, now
known as Schur-Weyl duality. Specifically, there are actions of each group on
tensor space under which each group action generates the full centralizer algebra of
the other.
462 A. Ram
In 1986, Jimbo [Jil recognized that there exists a similar duality between the
quantum group Ug(gl(n) and the Hecke algebras of type A. Guided by this
observation, we develop a “Frobenius" formula and a combinatorial rule for
computing the characters of the Hecke algebras. The presentation given in this
paper allows one to avoid the quantum group completely. The derivation of the
combinatorial rule shows that there are connections, apparently unexplored,
between characters of Hecke algebras, Hall-Littlewood symmetric functions, and
Kronecker products of symmetric group representations. The combinatorial rule
which is derived in this paper is essentially a q-analogue of the Murnaghan-
Nakayama rule, in the sense that when one specializes q =- 1 it trivially reduces to
the classical rule for the symmetric group.
The paper is organized as follows. In the first section we develop the needed
notation and give the necessary basic facts about the symmetric group and the
Hecke algebra. In Sect. 2 we give a brief description of the duality between the
quantum group and the Hecke algebra and the motivation behind our approach to
the characters of the Hecke algebra. In Sect. 3 we show that the irreducible
characters of the Hecke algebra are determined by traces arising from a certain
action of the Hecke algebra on tensor space. In Sect. 4 we show that these traces
are, up to a scalar multiple, Hall-Littlewood symmetric functions and give
a Frobenius type formula for the characters of the Hecke algebra. In Sect. 5 we use
the Frobenius formula to derive formulas for the irreducible characters of the
Hecke algebra. In Sect. 6 we develop a connection between the characters of the
Hecke algebra and Kronecker products of symmetric group representations and
derive a combinatorial rule for computing characters of the Hecke algebras.
Section 7 gives a brief summary of work of King and Wybourne and of Vershik and
Kerov on the characters of the Hecke algebra. In the final section we give explicit
formulas for some special cases and tables of characters.
Acknowledgements. I would like to thank H. Wenzl for teaching me about quantum groups and
for explaining to me how the calculation I wanted to do could actually be done. I would like to
thank A. Garsia for showing me how to do computations via a-ring notation and for all the
support (both grant support and otherwise) and encouragement he has given me. I don't think
I would have pushed this all the way through without it. I would also like to thank M. Haiman
and S.T. Whitehead for enlightening discussions.
