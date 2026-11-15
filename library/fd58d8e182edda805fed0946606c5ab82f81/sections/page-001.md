---
doc_id: fd58d8e182edda805fed0946606c5ab82f81
doc_title: "GRÖBNER-SHIRSHOV BASES FOR TEMPERLEY-LIEB ALGEBRAS"
section_id: page-001
section_title: "Page 1"
section_number: null
pages: 1-1
source_pdf: fd58d8e182edda805fed0946606c5ab82f81.pdf
source_sha256: 292cb048e7097935
toc_source: undetermined
doc_brief: "GRÖBNER-SHIRSHOV BASES FOR TEMPERLEY-LIEB ALGEBRAS — For Temperley-Lieb algebras of type B, we construct their Gröbner-Shirshov bases and the corresponding standard monomials, which give another"
---
Palestine Journal of Mathematics
Vol. 7(Special Issue: I, 2018) , 11–17
© Palestine Polytechnic University-PPU 2018
GRÖBNER-SHIRSHOV BASES FOR TEMPERLEY-LIEB
ALGEBRAS
Sungsoon Kim† and Dong-il Lee*
Communicated by Ayman Badawi
MSC 2010 Classiﬁcations: Primary 20F55; Secondary 05E15, 16Z05.
Keywords and phrases: Temperley-Lieb algebra, Gröbner-Shirshov basis.
Abstract For Temperley-Lieb algebras of type B, we construct their Gröbner-Shirshov bases
and the corresponding standard monomials, which give another combinatorial interpretation for
the fully commutative elements.
1 Introduction
Originally, the Temperley-Lieb algebra appears in the context of statistical mechanics [19], and
later its structure has been studied in connection with knot theory, where it is known to be a
quotient of the Hecke algebra of type A [8].
Our approach to understanding the structure of Temperley-Lieb algebras is from the non-
commutative Gröbner basis theory, called the Gröbner-Shirshov basis theory, which provides a
powerful tool for understanding the structure of (non)associative algebras and their representa-
tions, especially in computational aspects. With the ever-growing power of computers, it is now
viewed as a universal engine behind algebraic or symbolic computation.
The main interest of the notion of Gröbner-Shirshov bases stems from Shirshov’s Compo-
sition Lemma and his algorithm [15] for Lie algebras and independently from Buchberger’s
algorithm [4] of computing Gröbner bases for commutative algebras. In [2], Bokut applied Shir-
shov’s method to associative algebras, and Bergman mentioned the diamond lemma for ring
theory [1].
The Gröbner-Shirshov bases for Coxeter groups of classical and exceptional types were com-
pletely determined in [3, 12, 13, 18]. The cases for Hecke algebras and Temperley-Lieb algebras
of type A were calculated in [9].
In this paper, we deal with Temperley-Lieb algebras of type B, extending the result in [9,
§6]. By completing the relations coming from a presentation of the Temperley-Lieb algebra, we
compute its Gröbner-Shirshov basis to obtain the corresponding set of standard monomials. The
explicit multiplication table between the monomials follows naturally. We remark that the set
of standard monomials we constructed as a Gröbner-Shirshov basis corresponds to that of fully
commutative elements which indexes a basis of the Temperley-Lieb algebra [6, 17].
2 Basic Deﬁnitions and Notations
In this section, we recall a basic theory of Gröbner-Shirshov bases for associative algebras so as
to make the paper self-contained. There will be some properties listed without proofs which are
well-known and necessary for this paper.
Let X be a set and let ⟨X⟩be the free monoid of associative words on X. We denote the
empty word by 1 and the length (or degree) of a word u by l(u). We deﬁne a total-order < on
⟨X⟩, called a monomial order as follows ;
if x < y implies axb < ayb for all a, b ∈⟨X⟩.
† She is grateful to KIAS for its hospitality during this work.
∗The corresponding author. This research was supported by NRF Grant # 2014R1A1A2054811 and a research grant from
Seoul Women’s University(2018).
