---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
toc_source: inferred
doc_brief: "The Dilogarithm Function — 14 sections: Front matter; The dilogarithm function in geomet; Special values"
---
The Dilogarithm Function
Don Zagier
Max-Planck-Institut f¨ur Mathematik, Vivatsgasse 7, D-53111 Bonn, Germany
and Coll`ege de France, 3 rue d’Ulm, F-75005 Paris, France
zagier@mpim-bonn.mpg.de
I.
The dilogarithm function in geometry and number theory
5
1. Special values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2. Functional equations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
3. The Bloch-Wigner function D(z) and its generalizations . . . . . . . . . . . . 10
4. Volumes of hyperbolic 3-manifolds . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . 13
5. . . . and values of Dedekind zeta functions . . . . . . . . . . . . . . . . . . . . . . . . . 16
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
Notes on Chapter I . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
II.
Further aspects of the dilogarithm . . . . . . . . . . . . . . . . . . . . . . . 22
1. Variants of the dilogarithm function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2. Dilogarithm identities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3. Dilogarithms and modular functions: the Nahm equation . . . . . . . . . . . 41
4. Higher polylogarithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
The dilogarithm function, deﬁned in the ﬁrst sentence of Chapter I, is
a function which has been known for more than 250 years, but which for
a long time was familiar only to a few enthusiasts. In recent years it has
become much better known, due to its appearance in hyperbolic geometry
and in algebraic K-theory on the one hand and in mathematical physics (in
particular, in conformal ﬁeld theory) on the other. I was therefore asked to
give two lectures at the Les Houches meeting introducing this function and
explaining some of its most important properties and applications, and to
write up these lectures for the Proceedings.
The ﬁrst task was relatively straightforward, but the second posed a prob-
lem since I had already written and published an expository article on the
dilogarithm some 15 years earlier. (In fact, that paper, originally written as
a lecture in honor of Friedrich Hirzebruch’s 60th birthday, had appeared in
two diﬀerent Indian publications during the Ramanujan centennial year—see
footnote to Chapter I). It seemed to make little sense to try to repeat in
4
Don Zagier
diﬀerent words the contents of that earlier article. On the other hand, just
reprinting the original article would mean omitting several topics which were
either developed since it was written or which were omitted then but are of
more interest now in the context of the appearances of the dilogarithm in
mathematical physics.
The solution I ﬁnally decided on was to write a text consisting of two
chapters of diﬀerent natures. The ﬁrst is simply an unchanged copy of the
1988 article, with its original title, footnotes, and bibliography, reprinted by
permission from the book Number Theory and Related Topics (Tata Institute
of Fundamental Research, Bombay, January 1988). In this chapter we deﬁne
the dilogarithm function and describe some of its more striking properties:
its known special values which can be expressed in terms of ordinary log-
arithms, its many functional equations, its connection with the volumes of
ideal tetrahedra in hyperbolic 3-space and with the special values at s = 2
of the Dedekind zeta functions of algebraic number ﬁelds, and its appearance
in algebraic K-theory; the higher polylogarithms are also treated brieﬂy. The
second, new, chapter gives further information as well as some more recent
developments of the theory. Four main topics are discussed here. Three of
them—functional equations, modiﬁcations of the dilogarithm function, and
higher polylogarithms—are continuations of themes which were already be-
gun in Chapter I. The fourth topic, Nahm’s conjectural connection between
(torsion in) the Bloch group and modular functions, is new and especially fas-
cinating. We discuss only some elementary aspects concerning the asymptotic
properties of Nahm’s q-expansions, referring the reader for the deeper parts of
the theory, concerning the (in general conjectural) interpretation of these q-
series as characters of rational conformal ﬁeld theories, to the beautiful article
by Nahm in this volume.
As well as the two original footnotes to Chapter I, which are indicated by
numbers in the text and placed at the bottom of the page in the traditional
manner, there are also some further footnotes, indicated by boxed capital
letters in the margin and placed at the end of the chapter, which give updates
or comments on the text of the older article or else refer the reader to the
sections of Chapter II where the topic in question is developed further. Each of
the two chapters has its own bibliography, that of Chapter I being a reprint of
the original one and that of Chapter II giving some references to more recent
literature. I apologize to the reader for this somewhat artiﬁcial construction,
but hope that the two parts of the paper can still be read without too much
confusion and perhaps even with some enjoyment. My own enthusiasm for this
marvelous function as expressed in the 1988 paper has certainly not lessened
in the intervening years, and I hope that the reader will be able to share at
least some of it.
The reader interested in knowing more about dilogarithms should also
consult the long article [22] of A.N. Kirillov, which is both a survey paper
treating most or all of the topics discussed here and also contains many new
results of interest from the point of view of both mathematics and physics.
The Dilogarithm Function
5
