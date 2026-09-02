---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-000-preface-to-the-second-edition
section_title: "Preface to the second edition"
section_number: null
pages: 9-15
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
There is no perfect time to write a textbook for a ﬁeld in its infancy. Act too
early and the theory might not have the cohesive structure it will eventually
develop, but act too late and you might miss an opportunity to encourage new
collaborators to enter and shape the area. The ﬁrst edition of this book was
timed to strike a balance between these two extremes: after a suﬃcient frame-
work for analytic combinatorics in several variables had been developed, but
during a time when fundamental results were still being discovered and incor-
porated.
As a consequence of this choice, the ﬁrst edition of the text, while inﬂuential
and put to use by many others in enumerative combinatorics, was presented in
a way that many end users found di ﬃcult to follow. Having been given the
opportunity to create a second edition of this text, after a decade of further
development, we are now able to improve both the content and presentation of
the ﬁeld. We have been conscious in this rewriting of making the book more
useful for a variety of readers having di ﬀerent motivations, including making
it easier to look up and cite desired asymptotic results.
For the second edition, the original authors welcome our active collabora-
tor Stephen Melczer, whose own introductory book on this topic [Mel21] was
published recently, and who has rejuvenated the entire enterprise. In contrast
to [Mel21], which skips much of the advanced topological and geometric ap-
proach to analytic combinatorics in several variables (ACSV) to focus more on
elementary arguments and explicit computation, this text remains dedicated to
developing the theory in its most general, and most powerful, form. The ﬁeld
of ACSV has ﬂourished since the publication of the ﬁrst edition, including nu-
merous workshops, seminars, summer school courses, and many publications
exploring applications of the theory [Wil15; dALN15; MM16; Pan17; Vid17;
Kov19; Mis19; MW19; RWZ20; GE20; Geo21; GFS21; KLM21; GWW21;
Len+23].
xi
xii Preface to the second edition
Over the last ten years, we have gained an improved understanding of the
technical parts of the theory. Perhaps the largest change is to give ACSV a
rigorous foundation using stratiﬁed Morse theory, whereas in the ﬁrst edition
Morse-theoretic arguments were used to motivate constructions that were then
veriﬁed with other techniques. In addition to ﬁxing numerous typographical
and other errors in the ﬁrst edition, some the fault of the authors and some of
the publisher, the following content changes have been made to improve the
book.
• The chapters in Parts I (Combinatorial Enumeration) and II (Mathemati-
cal Background) have mainly kept their general structure, however much of
their discussion has been rewritten. Of particular note, Section 2.4 has been
revised to better explain how ACSV for rational functions extends to alge-
braic functions via diagonal embeddings, and Section 5.4 has been revised
to better explain the proof of Theorem 5.3 (formerly Theorem 5.4.8). Chap-
ter 6 in the ﬁrst edition has also been moved after the former Chapters 7
and 8 so that Part II now ends in Chapter 6 (which was Chapter 7 in the ﬁrst
edition).
• Part III (Multivariate Enumeration) begins with Chapter 7, which has been
completely overhauled and is almost entirely new. The second edition is
constructed to put the large majority of the topological and homological
arguments in this chapter and the appendices. The main output of the chapter
is an expression for coeﬃcient asymptotics as a ﬁnite integer sum of saddle-
point-like integrals, and those wanting to skip the homological material can
simply assume this decomposition in later chapters.
• Chapter 8, which is a complete re-imagining of Chapter 6 in the ﬁrst edition,
discusses how to compute the quantities needed for an asymptotic analysis
in a computer algebra system. In contrast to the ﬁrst edition, we now put ad-
ditional focus on computing the quantities needed for ACSV – this explains
its postponement until Part III.
• Chapters 9–11 have been reworked to begin from the decomposition de-
scribed in Chapter 7, streamlining their presentation, and to have more ex-
plicit results that can be easily cited. Section 11.4 has also been expanded
to include a worked example of solving a connection problem via creative
telescoping.
• The appendices have been revised and enlarged to be more self-contained,
and to give readers a more complete explanation of the constructions they
will need for ACSV .
• We have greatly increased the number of exercises and examples, and added
many more signposts and guides so that readers with di ﬀerent motivations
Preface to the second edition xiii
can ﬁnd what they are looking for. Exercises have been split into in-text
(shorter and more straightforward, meant to help the reader think over the
material) and end-of-chapter (more challenging) problems. We have also
listed open problems and ongoing research in Chapter 13.
• Finally, we have created Sage worksheets that cover most of the examples
in the book, and some of the exercises.
Supplementary material, including Sage worksheets and a maintained list of
errata, are available from the book website
http://acsvproject.org/acsvbook
More general resources for the ACSV project are available at
http://acsvproject.org
The authors thank our colleagues who helped with proofreading and other-
wise checking the manuscript, including Nick Beaton, Jeremy Chizewer, Ja-
cob Cordeiro, William Dugan, Stephen Gillen, Kaitian Jin, Alexander Kroitor,
Geoﬀrey Pritchard, Stephan Ramon Garcia, and Josip Smol ˇci´c. We thank the
anonymous reviewers consulted by the publisher, and in particular one re-
viewer who set us straight on the inner workings of Thom’s Isotopy Theorem.
We thank Herman Gluck for help with topology and Frank Sottile for con-
siderable help with computational algebra. A special word of thanks is due to
Yuliy Baryshnikov. Not only did we learn most of the recent material from
him or with him, but he has remained available for consultation during the en-
tire production of the second edition. The authors each thank their families for
their patience and support.
Preface to the ﬁrst edition
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
the early 1980s [BR83]; however, even by 1995, of 100 + pages in the Hand-
book of Combinatorics devoted to asymptotic enumeration [Odl95], multivari-
ate asymptotics received fewer than six.
This book is the result of work spanning nearly 15 years. Our aim has been
to develop analytic machinery to recover, as e ﬀectively as possible, asymp-
totics of the coe ﬃcients of a multivariate generating function. Both authors
feel drawn to this area of study because it combines so many areas of modern
mathematics. Functions of one or more complex variables are essential, but
also algebraic topology in the Russian style, stratiﬁed Morse theory, computa-
tional algebraic methods, saddle point integration, and of course the basics of
combinatorial enumeration. The many applications of this work in areas such
as bioinformatics, queueing theory, and statistical mechanics are not surprising
when we realize how widespread is the use of generating functions in applied
combinatorics and probability.
xiv
Preface to the ﬁrst edition xv
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
xvi Preface to the ﬁrst edition
lem in its earliest incarnation. A similar role was played several years later by
Jeﬀ McNeal. Perhaps the greatest thanks are due to Yuliy Baryshnikov, who
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
