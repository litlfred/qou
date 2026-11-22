---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-000-preface-to-the-second-edition
section_title: "Preface to the second edition"
section_number: null
pages: 9-12
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
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
a way that many end users found diﬃcult to follow. Having been given the
opportunity to create a second edition of this text, after a decade of further
development, we are now able to improve both the content and presentation of
the ﬁeld. We have been conscious in this rewriting of making the book more
useful for a variety of readers having diﬀerent motivations, including making
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
xii
Preface to the second edition
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
will need for ACSV.
• We have greatly increased the number of exercises and examples, and added
many more signposts and guides so that readers with diﬀerent motivations
Preface to the second edition
xiii
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
Geoﬀrey Pritchard, Stephan Ramon Garcia, and Josip Smolˇci´c. We thank the
anonymous reviewers consulted by the publisher, and in particular one re-
viewer who set us straight on the inner workings of Thom’s Isotopy Theorem.
We thank Herman Gluck for help with topology and Frank Sottile for con-
siderable help with computational algebra. A special word of thanks is due to
Yuliy Baryshnikov. Not only did we learn most of the recent material from
him or with him, but he has remained available for consultation during the en-
tire production of the second edition. The authors each thank their families for
their patience and support.
