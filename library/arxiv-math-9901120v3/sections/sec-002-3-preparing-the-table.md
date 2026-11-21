---
doc_id: arxiv-math-9901120v3
doc_title: "A table of boundary slopes of Montesinos knots"
section_id: sec-002-3-preparing-the-table
section_title: "Preparing the table"
section_number: 3
pages: 3-4
source_pdf: 9901120v3.pdf
source_sha256: 782034b674f958af
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 1.0
doc_brief: "A table of boundary slopes of Montesinos knots — This note corrects errors in Hatcher and Oertel’s table of boundary slopes of Montesinos knots which have projec- tions with 10 or fewer crossings."
---
[]{#method label="method"}

In this section I briefly describe the precautions taken to insure that the table in Section [\[table\]](#table){reference-type="ref" reference="table"} is correct. I first noticed errors in the table in [@HatcherOertel] when comparing it with the output of a program that computes the *normal* boundary slopes of a knot (that is, the boundary slopes of all surfaces which are normal with respect to a choice of triangulation of the exterior of the knot). The data in Section [\[table\]](#table){reference-type="ref" reference="table"} is consistent with the normal boundary slope data. Following the algorithm given in [@HatcherOertel], but without reference to the program used in computing the table there, I wrote a completely new program to compute boundary slopes. I then compared its output with the output of Hatcher and Oertel's program. When the output differed, I debugged both programs until I found the source of the problem, and then fixed the appropriate program. Eventually, after the new program and the fixed version of Hatcher and Oertel's program had agreed for thousands of trial Montesinos knots, I declared victory and went home.

Unfortunately, there remained several cases where I implemented the algorithm incorrectly and Hatcher and Oertel's program also made a very similar mistake. Comparing the 1999 version of this note with Marc Culler's computations of $A$-polynomials [@Culler], Thomas Mattman found some additional errors, leading to this 2010 revision. For the table of knots with at most 10 crossings, the 1999 version of this note is strictly better than [@HatcherOertel], i.e. some errors were corrected but no new ones were introduced. Hopefully, the tables are now completely correct, but it is possible that errors remain.

One source of problems in the table in [@HatcherOertel] is a slight error in the main body of [@HatcherOertel]. The remark immediately preceding Proposition 2.7 gives conditions that are claimed to be equivalent to certain hypotheses of Propositions 2.6 and 2.7. It was this reformulation of these propositions which was used in Hatcher and Oertel's program. However, the conditions given in the remark are not in fact equivalent to those given in the propositions. My program used the original formulation.
