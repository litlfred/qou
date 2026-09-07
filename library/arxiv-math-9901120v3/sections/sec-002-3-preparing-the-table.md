---
doc_id: arxiv-math-9901120v3
doc_title: "A table of boundary slopes of Montesinos knots Nathan M. Dunfield1 Revised version of June 2010 email: nathan@dunfield.info"
section_id: sec-002-3-preparing-the-table
section_title: "Preparing the table"
section_number: 3
pages: 3-4
source_pdf: 9901120v3.pdf
source_sha256: 782034b674f958af
doc_brief: "A table of boundary slopes of Montesinos knots Nathan M. Dunfield1 Revised version of June 2010 email: nathan@dunfield.info — This note corrects errors in Hatcher and Oertel’s table of boundary"
---
In this section I brieﬂy describe the precautions taken to
insure that the table in Section 2 is correct. I ﬁrst noticed
errors in the table in [ HO] when comparing it with the
output of a program that computes the normal boundary
slopes of a knot (that is, the boundary slopes of all sur-
faces which are normal with respect to a choice of trian-
gulation of the exterior of the knot). The data in Section2
is consistent with the normal boundary slope data. Fol-
lowing the algorithm given in [HO], but without reference
to the program used in computing the table there, I wrote
a completely new program to compute boundary slopes.
I then compared its output with the output of Hatcher and
Oertel’s program. When the output differed, I debugged
both programs until I found the source of the problem,
and then ﬁxed the appropriate program. Eventually, af-
ter the new program and the ﬁxed version of Hatcher and
Oertel’s program had agreed for thousands of trial Mon-
tesinos knots, I declared victory and went home.
Unfortunately, there remained several cases where I
implemented the algorithm incorrectly and Hatcher and
Oertel’s program also made a very similar mistake. Com-
paring the 1999 version of this note with Marc Culler’s
computations of A-polynomials [ C], Thomas Mattman
found some additional errors, leading to this 2010 revi-
sion. For the table of knots with at most 10 crossings,
the 1999 version of this note is strictly better than [ HO],
i.e. some errors were corrected but no new ones were in-
troduced. Hopefully, the tables are now completely cor-
rect, but it is possible that errors remain.
One source of problems in the table in [HO] is a slight
error in the main body of [ HO]. The remark immedi-
ately preceding Proposition 2.7 gives conditions that are
claimed to be equivalent to certain hypotheses of Propo-
sitions 2.6 and 2.7. It was this reformulation of these
propositions which was used in Hatcher and Oertel’s pro-
gram. However, the conditions given in the remark are
not in fact equivalent to those given in the propositions.
3
My program used the original formulation.
