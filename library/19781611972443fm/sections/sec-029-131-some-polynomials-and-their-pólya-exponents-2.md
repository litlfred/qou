---
doc_id: 19781611972443fm
doc_title: "AlgebrAic And geometric ideAs in the theory of discrete optimizAtion MO14_FM-10-24-12.indd 1 11/2/2012 2:14:52 PM Downloaded 08/31/26 to 85.5.100.194 . Redistribution subject to SI"
section_id: sec-029-131-some-polynomials-and-their-pólya-exponents-2
section_title: "Some polynomials and their Pólya exponents . . ............. 2 7 0"
section_number: 13.1
pages: 12-16
source_pdf: 1.9781611972443.fm.pdf
source_sha256: 3f958da310c0deb5
doc_brief: "AlgebrAic And geometric ideAs in the theory of discrete optimizAtion MO14_FM-10-24-12.indd 1 11/2/2012 2:14:52 PM Downloaded 08/31/26 to 85.5.100.194 . Redistribution subject to SIAM license or copyri"
---
xiii
Downloaded 08/31/26 to 85.5.100.194 . Redistribution subject to SIAM license or copyright; see https://epubs.siam.org/terms-privacy
List of Algorithms
A l g o r i t h m 1 . 1 F o u r i e r – M o t z k i n e l i m i n a t i o n................... 7
Algorithm 1.2 Ellipsoid method . ........................ 2 5
Algorithm 2.1 Lattice basis reduction . . .................... 5 2
A l g o r i t h m 3 . 1 G r a v e r - b e s t a u g m e n t a t i o n a l g o r i t h m............... 6 6
A l g o r i t h m 3 . 2 N o r m a l f o r m a l g o r i t h m...................... 7 1
Algorithm 3.3 Pottier’s algorithm ........................ 7 2
A l g o r i t h m 3 . 4 P r o j e c t - a n d - l i f t a l g o r i t h m ..................... 7 3
A l g o r i t h m 4 . 1 G r a v e r p r o x i m i t y a l g o r i t h m .................... 1 0 0
Algorithm 6.1 Regular triangulation algorithm . . . . ............. 1 2 1
Algorithm 7.1 Barvinok’s algorithm, primal half-open variant ......... 1 3 4
A l g o r i t h m 7 . 2 O u t p u t - s e n s i t i v e e n u m e r a t i o n w i t h g e n e r a t i n g f u n c t i o n s ..... 1 4 1
A l g o r i t h m 7 . 3 B i n a r y s e a r c h f o r t h e o p t i m a l v a l u e ............... 1 4 3
A l g o r i t h m 7 . 4 D i g g i n g a l g o r i t h m ........................ 1 4 6
Algorithm 8.1 Summation method for optimizing polynomials ......... 1 6 1
A l g o r i t h m 8 . 2 A p p r o x i m a t i o n o f t h e r a n g e o f t h e o b j e c t i v e f u n c t i o n ...... 1 7 3
A l g o r i t h m 1 0 . 1 D i v i s i o n a l g o r i t h m ........................ 1 9 5
A l g o r i t h m 1 0 . 2 E x t e n d e d E u c l i d e a n a l g o r i t h m .................. 1 9 6
A l g o r i t h m 1 0 . 3 M u l t i v a r i a t e d i v i s i o n a l g o r i t h m .................. 2 0 5
A l g o r i t h m 1 0 . 4 B u c h b e r g e r ’ s a l g o r i t h m...................... 2 1 0
A l g o r i t h m 1 1 . 1 G e o m e t r i c B u c h b e r g e r a l g o r i t h m ................. 2 2 6
A l g o r i t h m 1 1 . 2 M a x i m a l d e c r e a s i n g p a t h a l g o r i t h m ( M D P A ) .......... 2 2 7
A l g o r i t h m 1 1 . 3 P r o j e c t - a n d - l i f t .......................... 2 3 0
A l g o r i t h m 1 2 . 1 N u l L A a l g o r i t h m......................... 2 4 3
A l g o r i t h m 1 3 . 1 T h e P o s i t i v s t e l l e n s a t z m e t h o d .................. 2 7 5
xv
Downloaded 08/31/26 to 85.5.100.194 . Redistribution subject to SIAM license or copyright; see https://epubs.siam.org/terms-privacy
Preface
It is undeniable that geometric ideas have been very important to the foundations
of modern discrete optimization. The inﬂue nce that geometric algorithms have in opti-
mization was elegantly demonstrated in the, now classic, book Geometric Algorithms and
Combinatorial Optimization [145] written more than 25 years ago by M. Grötschel, L.
Lovász, and A. Schrijver. There, in a masterful way, we were introduced to the power
that the geometry of ellipsoids, hyperplanes, convex bodies, and lattices can wield in opti-
mization. After many years, students of integer programming today are exposed to notions
such as the equivalence of separation and optimization, convex hulls, and membership, and
to the many examples of successful applica tion of these ideas such as efﬁcient algorithms
for matchings on graphs and other problems with good polyhedral characterizations [298],
[299], [300] and the solution of large-scale traveling salesman problems [14]. These results
were a landmark success in the theory of integer optimization.
But in just the past 15 years, there have been new developments in the understanding
of the structure of polyhedra, convex sets, and their lattice points that have produced new
algorithmic ideas for solving integer programs. These techniques add a new set of powerful
tools for discrete optimizers and have already proved very suitable for the solution of a
number of hard problems, including attempts to deal with nonlinear objective functions and
constraints in discrete optimization. Unfortunately, many of these powerful tools are not
yet widely known or applied. Perhaps this is because many of the developments have roots
in areas of mathematics that are not normally part of the standard curriculum of students in
optimization and have a much more algebraic ﬂavor. Examples of these new tools include
algebraic geometry, commutative algebra, representation theory, and number theory.
We feel that the unfamiliar technical natureof these new ideas and the lack of expos-
itory accounts have unnecessarily delayed the popularity of these techniques among those
working in optimization. We decided to write a text that would not demand any background
beyond what we already assume from people in mathematical programming courses. This
monograph is then intended as a short, self-contained, introductory course in these new
ideas and algorithms with the hope of populariz ing them and inviting new applications.
We were deeply inspired by the inﬂuential book [145] and we humbly try to follow in its
footsteps in the hope that future generations continue to see the interdependence between
beautiful mathematics and the creation of efﬁcient optimization algorithms.
This book is meant to be used in a quick, intense course, no longer than 15 weeks.
This is not a complete treatise on the subject, but rather an invitation to a set of new ideas
and tools. Our aim is to popularize these new ideas among workers in optimization.
• We want to make it possible to read this book even if you are a novice of integer
and linear programming (and we have taught courses with some students in that
category). For this reason, we open in Part I with some of the now well-established
techniques that originated before the beginning of the 1990s, a time when linear and
xvii
Downloaded 08/31/26 to 85.5.100.194 . Redistribution subject to SIAM license or copyright; see https://epubs.siam.org/terms-privacy
xviii Preface
convex programming and integer programming underwent major changes thanks to
the ellipsoid method, semideﬁnite programming, lattice basis reduction, etc. Most of
what is contained in Part I is a short summary of tools that students in optimization
normally encounter in a course based on the excellent books [50, 145, 206, 259, 296]
and probably should be skipped by such readers. They should go directly to the new
exciting techniques in Parts II, III, IV , and V . Readers that start with Part I will add
an extra three or four weeks to the course.
• Parts II, III, IV , and V form the core of this book. Roughly speaking, when the reader
works in any of these sections, nonlinear, nonconvex conditions are central, making
the tools of algebra necessary. When studying only these parts, the course is planned
to take about 12 weeks. In fact, all the par ts are quite independent from each other
and each can be the focus of independent student seminars.
– We begin in Part II with the idea of test sets and Graver bases. We show how
they can be used to prove results about integer programs with linear constraints
and convex objective functions.
– Part III discusses the use of generating functions to deal with integer programs
with linear constraints but with nonlinear polynomial objectives and/or with
multiobjectives.
– Part IV discusses the notion of Gröbner bases and their connection with integer
programming.
– Part V discusses the solution of global optimization problems with polynomial
constraints via a sequence of linear algebra or semideﬁnite programming sys-
tems. These are generated based on Hilbert’s Nullstellensatz and its variations.
The book contains several exercises to help students learn the material. A course
based on these lectures should be suitable for advanced undergraduates with a solid math-
ematical background (i.e., very comfortable with proofs in linear algebra and real analysis)
or for graduate students who have already taken an introductory linear programming class.
Acknowledgments. We are truly grateful to many people who helped us both on produc-
ing the research presented here and later on presenting it to a larger audience of students
and colleagues.
First and foremost our collaborators and coauthors in many parts of this book were
fundamental for arriving at this point; their energy and ideas show on every page. In fact
several portions of the book are taken partially from our joint work. So many, many thanks
for everything to Robert Hildebrand, Chris Hillar, Jon Lee, Peter N. Malkin, Susan Mar-
gulies, Mohamed Omar, Shmuel Onn, Pablo Parrilo, Uriel Rothblum, Maurice Queyranne,
Christopher T. Ryan, Rüdiger Schultz, Sven Verdoolaege, Robert Weismantel, and Kevin
Woods. Thanks!
Many other friends have been faithful supporters and collaborators in other closely
related projects or have developed ideas of great importance to this book. We learned so
much about discrete optimization from talking to Karen Aardal, Alper Atamtürk, David
Avis, Egon Balas, Velleda Baldoni, Imre Bárány, Sasha Barvinok, Amitabh Basu, Nicole
Berline, Dmitris Bertsimas, Lou Billera, Greg Blekherman, Sam Burer, Bill Cook, San-
jeeb Dash, Antoine Deza, Etienne de Klerk, Matthias Ehrgott, Fritz Eisenbrand, Komei
Fukuda, Bernd Gärtner, Michel Goemans, Jo ˜ao Gouveia, David Haws, Nicolai Hähnle,
Martin Henk, Serkan Ho¸sten, Peter Huggins, Michael Joswig, V olker Kaibel, Gil Kalai,
Downloaded 08/31/26 to 85.5.100.194 . Redistribution subject to SIAM license or copyright; see https://epubs.siam.org/terms-privacy
Preface xix
Victor L. Klee, Steve Klee, Jean Bernard Lasserre, Monique Laurent, Jim Lawrence, Hen-
drik W. Lenstra, Sven Leyffer, Jeff Linderoth, Diane Maclagan, Jirka Matoušek, Nimrod
Megiddo, Bernard Mourrain, Walter Morris, Jiawang Nie, Jorge Nocedal, Edwin O’Shea,
Dima Pasechnik, Javier Peña, Vicky Powers, Scott Provan, Franz Rendl, Bruce Reznick,
Maurice Rojas, Paco Santos, András Sebö, Bernd Sturmfels, Levent Tunçel, Tamás Ter-
laky, Rekha R. Thomas, Mike Todd, Frank Vallentin, Santosh Vempala, Michèle Vergne,
Cynthia Vinzant, Emo Welzl, Laurence Wolsey, Yinyu Ye, Ruriko Yoshida, and Günter M.
Ziegler.
We received comments, corrections, great questions, suggestions, encouragement,
and help from Ilan Adler, Egon Balas, Dave Bayer, Matthias Beck, Victor Blanco, David
Bremner, Winfried Bruns, Katherine Burgraf, Samantha Capozzo, Gérard Cornuéjols, Persi
Diaconis, Brandon E. Dutra, Jennifer Galovich, Harvey Greenberg, Peter Gritzmann, Ok-
tay Günlük, Christian Haase, Ilya Hicks, Dorit Hochbaum, Mark Junod, Yvonne Kem-
per, Eddie Kim, Bala Krishnamoorthy, Jeff Lagarias, Karla Lanzas, Adam Letchford,
Quentin Louveaux, Laci Lovász, François Margot, Tyrrell McAllister, Juan Meza, Ga-
bor Pataki, Amber Puha, Mihai Putinar, Eric Rains, Jörg Rambau, Jürgen Richter-Gebert,
Carla Savage, Lex Schrijver, Markus Schweighofer, Renata Sotirov, Frank Sottile, Tamon
Stephen, Seth Sullivant, Richard Tapia, Andreas Waechter, Roger Wets, Angelika Wiegele,
Mark C. Wilson, Peter Winkler, Alexander Woo, David Woodruff, Doron Zeilberger, Yuriy
Zinchenko, and Uri Zwick. We received help from many students that heard lectures from
us on the topic. Thanks for your patience and effort! We give special thanks to Astrid
Köppe for the artwork she provided for the cover.
We are truly grateful to the NSF for the ﬁnancial support that made this book pos-
sible. Research and lectures about this topics were also produced with the support of
the following institutions: University of California, Davis, Universität Magdeburg, Tech-
nische Universität Darmstadt, and Technische Universität München. We must stress that
IMA (Institute for Mathematics and its Applications) at the University of Minnesota, the
Rocky Mountains Mathematics Consortium, Banff International Research Station, MSRI
(Mathematical Sciences Research Institute) at UC Berkeley, IPAM (Institute for Pure and
Applied Mathematics) at UCLA, AIM (American Institute of Mathematics) at Palo Alto,
MAA (Mathematical Association of America), and St. John’s University deserve special
acknowledgment as they allowed parts of these notes to be presented in short courses or be
the focus of special workshops.
Finally, our families are very special in our lives and this project is partly theirs too,
built with their love and patience in our long crazy hours and very distracted minds.
Jesús is truly grateful to his wife Ingrid who has put up with him and his difﬁcult
workaholic nature for a long, long time. Mil gracias amor mio de todo corazón, todo te lo
debo a ti. Their two sons Antonio and Andrés were just little kids when the research on
this book began to ﬂourish. It is a great pleasure to see them both grow so strong in spirit
and intellect. Muchas, muchas gracias hijo s míos y perdón por la falta de atención, estoy
orgulloso de ustedes. Mil gracias a doña Antonia y Judith, queridas madre y hermana, que
siempre me quieren y me apoyan. Gracias a toda la familia y amigos en México por lo
mucho que me dan.
Raymond thanks his wife Susi for her understanding and love and for the two little
bright stars in their lives, Carina and Paula. You three are the best that ever happened to
me!
Jesús A. De Loera, Raymond Hemmecke, Matthias Köppe
Downloaded 08/31/26 to 85.5.100.194 . Redistribution subject to SIAM license or copyright; see https://epubs.siam.org/terms-privacy
