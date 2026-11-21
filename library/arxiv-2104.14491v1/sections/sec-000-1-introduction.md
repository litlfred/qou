---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mos"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
toc_source: outline
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
Introduction
Why satellites?
One can image a satellite knot as a knot inside (i.e., non-tivially embedded into) a solid
torus tied in the form of another (companion) knot [1]. In this paper, we study the Khovanov polynomials
of the satellite knots. We see at least two reasons to do this.
First, the satellite knots are interesting in themselves. Being rare among relatively simple prime knots,
the satellite knots can actually predominate in the entire knot space [2, 3]. This is already a reason to
develop eﬃcient calculus for associated knot polynomials.Apart from that, the Khovanov polynomial of a
satellite is actually the polynomial of a knot in a solid torus. Thus we get another approach to the knots in
the simplest handled body, for which these invariants invariants are yet little studied [4].
Second, the satellite knots play a major role in deﬁnition the coloured knot polynomials, both of the
Jones/HOMFLY [5] and Khovanov/-Rozansky [6, 7] types. However, a relation between the satellite polyno-
mials and “irreducible” coloured polynomials is much more involved in the latter case [8, 9, 10, 11]. In fact,
the corresponding polynomials are well studied only in extreme cases, such as higher colour [12] and inﬁnite
braid [13] limits. Only very simpliﬁed versions of these invariants were studied for more or less general knots
[8, 14]. Although several “combinatorial” deﬁnitions of the coloured Khovanov-Rozansky homology were
constructed [15, 16], none of them (as far as we know) is still realised as an eﬀective homology calculator.
In contrast, there are such calculators for plain Khovanov and for particular cases of Khovanov-Rozansky
homologies and polynomials [17]. Hence one can try to extract a candidate for a “coloured Khovanov-type
invariant” of a knot from the explicitly computed Khovanov polynomials of its satellites.
Another part of the story is the knot Floer homology, which is believed to be an other (“dual” to
Khovanov) “reduction” of the superpolynomial [18, 19]. The Floer homologies were studied both for the
Whitehead doubles [20] and cables [21, 22]. Hence the next step is to “embed” the Floer and Khovanov
results into a new knowledge about the knot superpolynomials.
Particular problem we study.
In [23], a simple procedure was suggested to build the double-graded
HOMFLY-PT polynomials [24, 25, 26, 5] for satellite knots, especially for the Whitehead doubles (ﬁg.1, on
the right). It is based on the R-matrix formalism for HOMFLY polynomials [27, 28, 5, 29] and reduces to
calculating a peculiar “lock” block and the uniform adjoint polynomials [30]. This is a powerful approach,
straightforwardly generalisable to other knot families and to the coloured polynomials. Yet, an extension
to the triply graded superpolynomials [31, 32], or to quadruply graded hyperpolynomials [33, 34] is still a
big puzzle. An attempt to ﬁnd one was already made in [23], but at that time there was no practical way
to check and improve the suggested answers. Now we can do this, at least partly, by comparing conjectures
with the explicitly calculated Khovanov polynomials. This is the goal of the present study.
Summary of results.
Below we summarize our main observations and conclusions of the explicitly com-
puted Khovanov polynomials of the simplest satellite knots and knot families by means of the (slightly
improved) program from [35].
I. STw−2
Tor3
II. STw−2
Tw−2
Figure 1: Torus and twist satellites of the ﬁgure-eight knot
I. Tor3
II. Tw−2
Figure 2: Two-stand torus and twist knots
♦Positive pattern-companion decomposition (PPCD).
Our main conjecture is an extension of
the pattern-companion decomposition from [23] to the Khovanov polynomials.
Namely, the Khovanov
polynomial of a twisted Whitehead double or two-strand cable (the two simplest satellite families) can be
presented as a naively deformed linear combination of the positive polynomial invariants of the pattern and
companion,
HSK
e
K(A, q) = f(A, q)H eK(A, q) + g(A, q)HK(A, q) −→KhSK
e
K(q, t) = F(q, t)Kh eK(q, t) + G(q, t)KK(q, t).
(1)
In sec.3.2 we give explicit formulas (16) and (15) for the torus and twist cases.
⋄The pattern invariant in Kh eK(q, t) is the Khovanov polynomial of the pattern-deﬁning twisted or
torus knot, respectively.
⋄The companion invariant in KK(q, t) is a positive polynomial, which is likely to be a “tail” of the
adjoint Khovanov that survives in the satellite polynomial (unlike the true adjoint Khovanov itself).
We determine both these quantities explicitly for the simplest companion knots and knot families by
writing and solving the diﬀerence “evolution” equations for the computed satellite knot polynomials, treating
the half-twist number in the pattern as a variable.
♦Critical point of evolution ﬂow and the s-invariant.
For a given companion, the satellite poly-
nomial “smoothly” depends on the pattern but for a single “Θ-jump” in Kh eK(q, t) (see sec.4.1). This jump
happens when an invariant combination of the pattern’s hail-twist number and the companion’s writhe
equals three times Rasmussen s-invariant, which coincides with the knot signature for all considered knots
(see sec.2.3).
A similar phenomenon is known for the knot Floer homology and Ozsv´ath-Szab´o τ-invariant1 for the
same kind of satellites [20, 21, 22].
