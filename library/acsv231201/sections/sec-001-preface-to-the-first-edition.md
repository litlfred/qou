---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-001-preface-to-the-first-edition
section_title: "Preface to the first edition"
section_number: null
pages: 12-15
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
The term “Analytic Combinatorics” refers to the use of complex analytic meth-
ods to solve problems in combinatorial enumeration. Its chief objects of study
are generating functions [FS09, page vii]. Generating functions have been used
for enumeration for over a hundred years, going back to Hardy and, arguably,
to Euler. Their systematic study began in the 1950s [Hay56]. Much of the im-
petus for analytic combinatorics comes from the theory of algorithms, arising
for example in the work of Knuth [Knu06]. The recent, seminal work [FS09]
describes the rich univariate theory with literally hundreds of applications.
The multivariate theory, as recently as the mid-1990s, was still in its in-
fancy. Techniques for deriving multivariate generating functions have been
well understood, sometimes paralleling the univariate theory and sometimes
achieving surprising depth [FIM99]. Analytic methods for recovering coef-
ﬁcients of generating functions once the functions have been derived have,
however, been sorely lacking. A small body of analytic work goes back to
the early 1980s [BR83]; however, even by 1995, of 100+ pages in the Hand-
book of Combinatorics devoted to asymptotic enumeration [Odl95], multivari-
ate asymptotics received fewer than six.
This book is the result of work spanning nearly 15 years. Our aim has been
to develop analytic machinery to recover, as eﬀectively as possible, asymp-
totics of the coeﬃcients of a multivariate generating function. Both authors
feel drawn to this area of study because it combines so many areas of modern
mathematics. Functions of one or more complex variables are essential, but
also algebraic topology in the Russian style, stratiﬁed Morse theory, computa-
tional algebraic methods, saddle point integration, and of course the basics of
combinatorial enumeration. The many applications of this work in areas such
as bioinformatics, queueing theory, and statistical mechanics are not surprising
when we realize how widespread is the use of generating functions in applied
combinatorics and probability.
xiv
Preface to the ﬁrst edition
xv
The purpose of this book is to pass on what we have learned, so that others
may learn it and use it before we forget it. The present form of the book grew
out of graduate-level mathematics courses that developed, along with the the-
ory, at the University of Wisconsin, Ohio State University, and the University
of Pennsylvania. The course was intended to be accessible to students in their
second year of graduate study. Because of the eclectic nature of the required
background, this presents something of a challenge. One may count on students
having seen calculus on manifolds by the end of a year of graduate studies, and
some complex variable theory. One may also assume some willingness to do
some outside reading. However, some of the more specialized areas on which
multivariate analytic combinatorics must draw are not easy to get from books.
This includes topics such as the theory of amoebas [GKZ08] and the Leray–
Petrovsky–Gårding theory of inverse Fourier transforms. Other topics such as
saddle point integration and stratiﬁed Morse theory exist in books but require
being summarized in order not to cause a semester-long detour.
We have dealt with these problems by summarizing a great amount of back-
ground material. Part I contains the combinatorial background and will be
known to students who have taken a graduate-level course in combinatorial
enumeration. Part II contains mathematical background from outside of com-
binatorics. The topics in Part II are central to the understanding and execution
of the techniques of analytic combinatorics in several variables. Part III con-
tains the theory, all of which is new since the turn of the millennium and only
parts of which exist in published form. Finally, there are appendices, almost
equal in total size to Part II, which include necessary results from algebraic
and diﬀerential topology. Some students will have seen these but for the rest,
the inclusion of these topics will make the present book self-contained rather
than one that can only be read in a library.
We hope to recruit further researchers into this ﬁeld, which still has many in-
teresting challenges to oﬀer, and this explains the rather comprehensive nature
of the book. However, we are aware that some readers will be more focused
on applications and seek the solution of a given problem. The book is struc-
tured so that after reading Chapter 1, it should be possible to skip to Part III,
and pick up supporting material as required from previous chapters. A list of
papers using the multivariate methods described in this book can be found on
our website: http://acsvproject.org.
The mathematical development of the theory belongs mostly to the two au-
thors, but there are a number of individuals whose help was greatly instrumen-
tal in moving the theory forward. The complex analysts at the University of
Wisconsin-Madison, Steve Wainger, Jean-Pierre Rosay, and Andreas Seeger,
helped the authors (then rather junior researchers) to grapple with the prob-
xvi
Preface to the ﬁrst edition
lem in its earliest incarnation. A similar role was played several years later by
JeﬀMcNeal. Perhaps the greatest thanks are due to Yuliy Baryshnikov, who
translated the Leray–Petrovsky theory and the work of Atiyah–Bott–Gårding
into terms the authors could understand, and coauthored several papers. Frank
Sottile provided help with algebra on many occasions; Persi Diaconis arranged
for a graduate course while the ﬁrst author visited Stanford in 2000; Richard
Stanley answered our numerous miscellaneous queries. Thanks are also due to
our other coauthors on papers related to this project, listed on the project web-
site linked from the book website. Alex Raichev and Torin Greenwood helped
substantially with proofreading and with computer algebra implementations of
some parts of the book. All software can be located via the book website.
On a more personal level, the ﬁrst author would like to thank his wife, Diana
Mutz, for encouraging him to follow this unusual project wherever it took him,
even if it meant abandoning a still productive vein of problems in probability
theory. The sentiment in the probability theory community may be otherwise,
but the many connections of this work to other areas of mathematics have been
a source of satisfaction to the authors. The ﬁrst author would also like to thank
his children, Walden, Maria, and Simi, for their participation in the project via
the Make-A-Plate company (see Figure 0.1).
Figure 0.1 Customized “asymptotics of a multivariable generating function” din-
ner plates.
The second author thanks his wife Golbon Zakeri, children Yusef and Yahya,
and mother-in-law Shahin Sabetghadam for their help in carving out time for
him to work on this project, sometimes at substantial inconvenience to them-
selves. He hopes they will agree that the result is worth it.
