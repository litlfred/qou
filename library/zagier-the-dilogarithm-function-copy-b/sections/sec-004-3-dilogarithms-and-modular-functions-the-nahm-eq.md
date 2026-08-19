---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-004-3-dilogarithms-and-modular-functions-the-nahm-eq
section_title: "Dilogarithms and modular functions: the Nahm equation . . . . . . . . . . . 41"
section_number: 3
pages: 1-3
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The Dilogarithm Function Don Zagier — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
4. Higher polylogarithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
References ................................................... .. 6 3
The dilogarithm function, deﬁned in the ﬁrst sentence of Chapter I, is
a function which has been known for more than 250 years, but which for
a long time was familiar only to a few enthusiasts. In recent years it h as
become much better known, due to its appearance in hyperbolic geomet ry
and in algebraic K-theory on the one hand and in mathematical physics (in
particular, in conformal ﬁeld theory) on the other. I was therefore asked to
give two lectures at the Les Houches meeting introducing this func tion and
explaining some of its most important properties and applications, and to
write up these lectures for the Proceedings.
The ﬁrst task was relatively straightforward, but the second posed a pr ob-
lem since I had already written and published an expository article on t he
dilogarithm some 15 years earlier. (In fact, that paper, originally writte n as
a lecture in honor of Friedrich Hirzebruch’s 60th birthday, had appear ed in
two diﬀerent Indian publications during the Ramanujan centennial y ear—see
footnote to Chapter I). It seemed to make little sense to try to rep eat in
4 Don Zagier
diﬀerent words the contents of that earlier article. On the other hand , just
reprinting the original article would mean omitting several topics wh ich were
either developed since it was written or which were omitted then b ut are of
more interest now in the context of the appearances of the dilogarithm in
mathematical physics.
The solution I ﬁnally decided on was to write a text consisting of two
chapters of diﬀerent natures. The ﬁrst is simply an unchanged copy of t he
1988 article, with its original title, footnotes, and bibliography, repri nted by
permission from the book Number Theory and Related Topics (Tata Institute
of Fundamental Research, Bombay, January 1988). In this chapter we deﬁne
the dilogarithm function and describe some of its more striking proper ties:
its known special values which can be expressed in terms of ordinary log-
arithms, its many functional equations, its connection with the volum es of
ideal tetrahedra in hyperbolic 3-space and with the special values at s =2
of the Dedekind zeta functions of algebraic number ﬁelds, and its appe arance
in algebraic K-theory; the higher polylogarithms are also treated brieﬂy. The
second, new, chapter gives further information as well as some more rece nt
developments of the theory. Four main topics are discussed here. Thr ee of
them—functional equations, modiﬁcations of the dilogarithm function, an d
higher polylogarithms—are continuations of themes which were already be-
gun in Chapter I. The fourth topic, Nahm’s conjectural connection betwe en
(torsion in) the Bloch group and modular functions, is new and especial ly fas-
cinating. We discuss only some elementary aspects concerning the asy mptotic
properties of Nahm’s q-expansions, referring the reader for the deeper parts of
the theory, concerning the (in general conjectural) interpretation of these q-
series as characters of rational conformal ﬁeld theories, to the beautifu l article
by Nahm in this volume.
As well as the two original footnotes to Chapter I, which are indicated by
numbers in the text and placed at the bottom of the page in the traditional
manner, there are also some further footnotes, indicated by boxed cap ital
letters in the margin and placed at the end of the chapter, which give up dates
or comments on the text of the older article or else refer the reader to t he
sections of Chapter II where the topic in question is developed furt her. Each of
the two chapters has its own bibliography, that of Chapter I being a rep rint of
the original one and that of Chapter II giving some references to more rece nt
literature. I apologize to the reader for this somewhat artiﬁcial constru ction,
but hope that the two parts of the paper can still be read without too muc h
confusion and perhaps even with some enjoyment. My own enthusiasm f or this
marvelous function as expressed in the 1988 paper has certainly not lesse ned
in the intervening years, and I hope that the reader will be able to sh are at
least some of it.
The reader interested in knowing more about dilogarithms should also
consult the long article [22] of A.N. Kirillov, which is both a survey pap er
treating most or all of the topics discussed here and also contains many ne w
results of interest from the point of view of both mathematics and physi cs.
The Dilogarithm Function 5
Chapter I. The dilogarithm function
in geometry and number theory 1
The dilogarithm function is the function deﬁned by the power serie s
Li2(z)=
∞∑
n=1
zn
n2 for |z| < 1 .
The deﬁnition and the name, of course, come from the analogy with the Taylor
series of the ordinary logarithm around 1,
− log(1 − z)=
∞∑
n=1
zn
n for |z| < 1,
which leads similarly to the deﬁnition of the polylogarithm
Lim(z)=
∞∑
n=1
zn
nm for |z| < 1,m =1 , 2,... .
The relation d
dz Lim(z)= 1
z Lim−1(z)( m ≥ 2)
is obvious and leads by induction to the extension of the domain of deﬁnit ion
of Li m to the cut plane C/integerdivide[1, ∞); in particular, the analytic continuation of
the dilogarithm is given by
Li2(z)= −
∫ z
0
log(1 − u) du
u for z ∈ C/integerdivide[1, ∞) .
