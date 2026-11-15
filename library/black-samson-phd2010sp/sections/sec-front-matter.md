---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-9
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
toc_source: inferred
doc_brief: "REPRESENTATIONS OF HECKE — 16 sections: Front matter; INTRODUCTION; ILL Links and Braids"
---
REPRESENTATIONS OF HECKE
ALGEBRAS AND THE
ALEXANDER POLYNOMIAL
by
SAMSON BLACK
A DISSERTATION
Presented to the Department of Mathematics
and the Graduate School of the University of Oregon
in partial fulfillment of the requirements
for the degree of
Doctor of Philosophy
June 2010
ii
University of Oregon Graduate School
Confirmation of Approval and Acceptance of Dissertation prepared by:
Samson Black
Title:
"Representations of Heeke Algebras and the Alexander Polynomial"
This dissertation has been accepted and approved in partial fulfillment of the requirements for
the degree in the Department of Mathematics by:
Arkady Vaintrob, Co-Chairperson, Mathematics
Jonathan Brundan, Co-Chairperson, Mathematics
Victor Ostrik, Member, Mathematics
Dev Sinha, Member, Mathematics
Paul van Donkelaar, Outside Member, Human Physiology
and Richard Linton, Vice President for Research and Graduate Studies/Dean of the Graduate
School for the University of Oregon.
June 14,2010
Original approval signatures are on file with the Graduate School and the University of Oregon
Libraries.
iii
An Abstract of the Dissertation of
Samson Black
for the degree of
in the Department of Mathematics
to be taken
Doctor of Philosophy
June 2010
Title: REPRESENTATIONS OF HECKE ALGEBRAS AND THE ALEXANDER
POLYNOMIAL
Approved:
_
Dr. Arkady Vaintrob, Co-Chair
Approved:
_
Dr. Jonathan Brundan, Co-Chair
Vve study a certain quotient of the Iwahori-Hecke algebra of the symmetric group Sd, called
the super Temperley-Lieb algebra STLd. The Alexander polynomial of a braid can be computed
via a certain specialization of the Markov trace which descends to STLd. Combining this point
of view with Ocneanu's formula for the Markov trace and Young's seminormal form, we deduce a
new state-sum formula for the Alexander polynomial. We also give a direct combinatorial proof of
this result.
CURRICULUM VITAE
NAJVIE OF AUTHOR: Samson Black
PLACE OF BIRTH: Dallas, TX
DATE OF BIRTH: July 29, 1979
GRADUATE AND UNDERGRADUATE SCHOOLS ATTENDED:
University of Oregon, Eugene, OR
Pitzer College, Claremont, CA
DEGREES AWARDED:
Doctor of Philosophy, University of Oregon, 2010
Master of Science, University of Oregon, 2005
Bachelor of Arts, Pitzer College, 2002
AREAS OF SPECIAL INTEREST:
knot theory, representation theory
PROFESSIONAL EXPERIENCE:
Graduate Teaching Fellow, University of Oregon, 2003 to 2010
GRANTS, AWARDS AND HONORS:
Johnson Research Fellowship, University of Oregon Department of Mathematics, 2007
iv
v
ACKNOWLEDGMENTS
I would like to thank my advisor Arkady Vaintrob for being a great teacher, and for showing
me how to ask good questions. I am grateful to Jonathan Brundan for helping me enormously
when I felt stuck and for teaching me how to write mathematics well.
I would also like to thank Victor Ostrik for insisting that I make statements precise. And,
of course, I must acknowledge all the help and camaraderie provided by my office mates past and
present: Chad, Aaron, and Jonathan, thank you.
Finally, I would like to thank my loving wife Margot, who has supported me in so many
ways. Thank you.
This dissertation is dedicated to my parents,
Hank and Mara Black,
who showed me the beauty and power of mathematics,
beginning when I was very young,
and who believed in me unceasingly.
vi
vii
TABLE OF CONTENTS
Chapter
Page
I.
INTRODUCTION
1
I.1.
1.2.
Historical Background .
Summary of Thesis ..
1
3
II.
BRAIDS, LINKS, AND THE JONES POLYNOMIAL.
ILL
Links and Braids. . . . . . . . . . . . . . . . . .
II.2.
Representations of the Braid Group and the Iwahori-Hecke Algebra
II.3.
The Temperley-Lieb Algebra
IIA.
Diagram Algebras . . . . . . . . . . . . . . . . . . . . . . . . ....
6
6
9
14
16
III.
SCHUR-WEYL DUALITY AND QUOTIENTS OF THE HECKE ALGEBRA
21
III. I.
Schur-Weyl Duality
.
III.2.
Representations of the Iwahori-Hecke Algebra
IlI.3.
The Quantum Group Uv (.6'[(2)) ....
IlIA.
The Quantum Supergroup Uv (g[(111))
III.5.
The Super Temperley-Lieb Algebra
.
IV.
A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL
21
22
24
28
31
34
IV.l.
IV.2.
IV.3.
Semi-normal Representations of the Hecke Algebra.
Construction of the State-sum
An Example .....
34
37
40
V.
COMBINATORIAL PROOF
V.l.
Braid Group Invariance
V.2.
Markov JVloves
REFERENCES
.
41
41
43
49
LIST OF FIGURES
Figure
1.1.
The Conway skein relation:
'\7(L+) - '\7(L_) = z '\7(Lo)
1.2.
A (1, I)-tangle and its associated endomorphism of W ..
11.1. A diagram of the braid 0: = 0'2 1d and its closure a.
11.2. The cyclic Markov move.
.
.
11.3. The stabilization Markov move
.
11.4. The five Temperley-Lieb diagrams on 3 strands.
.,
II.5. The correspondence between (d, d)-diagrams and (0,2d)-diagrams.
II.6. The generating diagrams 14 and U{, U~, U~ in TL~(o).
11.7. An example of the closure operation on arc diagrams.
.
.
IV.1. The partition A = (3,1) E Par(4) and standard tableaux T and S2T..
V.l. Possible states x and y, organized according to 1r.
.
V.2. A state (xy,c-) for 0:(3 and the corresponding state ((3o:,1r(Y).c-) for (30:.
V.3. The states (y,c-+) and (y,€-) for O:O'n associated to the state (x,c-) for 0:.
VA. The Conway skein relation on links: 6(£+) - 6(£_) = (v - v- 1)6(£0) .
viii
Page
1
3
8
9
9
16
17
17
18
34
44
45
45
46
1
CHAPTER I
