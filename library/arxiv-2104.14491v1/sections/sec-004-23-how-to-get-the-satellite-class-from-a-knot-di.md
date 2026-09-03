---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗ A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mo"
section_id: sec-004-23-how-to-get-the-satellite-class-from-a-knot-di
section_title: "How to get the satellite class from a knot diagram"
section_number: 2.3
pages: 5-6
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗ A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
The ﬁrst Reidemeister of the companion and the full twist in the pattern. The parameter k of
the satellite deﬁned by (4,5) is a topological invariant, since it enters in the relations of the topologically
invariant quantities. On the other hand, a satellite is often presented with its the planar diagram, e.g.,
with one in ﬁg.1. Then k must be expressed via the number of the half-twists in the pattern, w, and
the writhe number of the companion knot K, ν. Both these quantities change under the same continuous
transformation of the knotted tube, which deletes a crossing with adjacent contractible loop on the knot
diagram (the RI transformation [1]) and causes a full twist of the tube. The attached two-strand braid
gains then two more half-twists of the same orientating as the deleted crossing 2 [1]. Hence, 2ν +w =inv.
Only one linear combination of ν an w must be a topological invariant, since the both numbers would be
invariants otherwise. Hence, k = 2ν +w +c, for some constant c. The form of the Khovanov polynomial as
function of the pattern dictates the natural chose of c = ShK given by (18) (see sec.3.2 for further details).
Satellite class in the cabling formula. The invariance of k = 2ν +w also follows from computation
of the HOMFLY polynomial using the knot diagram. E.g., one can take the cabling formulae for torus
satellites [5]. These formulae are originally applied to the renormalised ˇH polynomials and read
ˇHSK
Tork =−qw ˇHK
asm +q−w ˇHK
sym, (9)
Each of the knot polynomials H, Hasm, Hsym diﬀers from ˇH, ˇHasm, ˇHsym, respectively, by the known factor
whose power depends on the knot diagram 3. The explicit form of the factors is such that (9) becomes
A−4ν−wHSK
Tork = −qwA−2νq2νHK
asm +q−wA−2νq−2νHK
sym,
HSK
Tork = −(Aq)2ν+wHK
asm + (A/q)2ν+wHK
sym, (10)
and the comparison with (9) gives k = 2ν +w. Again, one can redeﬁne the topological class by adding an
arbitrary constant, k→k +c.
2The m-strand case is discussed in App.A
3The ratio of the topological and the vertical framings [5], sec.5.
5
What is k on the standard diagram? A satellite knot is commonly presented with a standard planar
diagram, where a “thick” companion is attached to an “extra” element. In our cases this element has a form
of the two-strand or Whitehead tangle (as in ﬁg.1). Then it seems natural to use the torus or twist knot
that is the closure of this tangle (ﬁg.2) to determine the pattern. Yet this is generally wrong, because (as
follows from the above discussion) the “extra” tangle has a sense only together with the companion knot,
and moreover with the framing of its “thickened” version.
However, the half-twist number in the attached tangle does deﬁne the pattern for a given framed com-
panion. We introduce for each companion its own pattern variable k = w + 2ν + ShK with the respective
last term from (18). In ﬁg.1, ν = 0 and Sh = 0, and hence k =w (but this is not so generally).
