---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-000-2-introduction
section_title: "INTRODUCTION"
section_number: 2
pages: 5-8
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
Purpose of this book.
This book stems from lectures given at the Universities of T¯ ohoku and
Hokkaid¯ o.
Its main purpose is to introduce the reader to p-adic analytic geometry
and to the theory of p-adic analytic functions and diﬀerential equations, by
focusing on the theme of period mappings. Of course, this approach is not
meant to replace more systematic expositions of p-adic analysis or geometry
found in a number of good treatises, but to complement them.
It is our general rule, in this book, to follow as closely as po ssible the
complex theory, and to go back and forth between the complex a nd the p-
adic worlds. We hope that this will make the text of interest b oth to some
complex geometers and to some arithmetic geometers.
In the course of Chapter I, this approach will eventually bec ome a kalei-
doscope of half-correspondences and broken echoes. We hope that the reader
will then have gained enough hindsight and wariness about th ese analogies,
and will enjoy seeing unity being restored at a deeper level i n Chapters II
and III.
We have chosen the theme of period mappings because of its cen tral
role in the nineteen-century mathematics as a fertile place of interaction
between diﬀerential equations, group theory, algebraic an d diﬀerential ge-
ometry, topology (and even number theory). In fact, it was a g uiding thread
in the early harmonious development of these branches of mat hematics, from
Gauss and Riemann to Klein and Poincar´ e ( cf. [Gray86]).
The origins lie in Gauss’ largely unpublished work on ellipt ic functions
on one hand (rediscovered and extended by Abel and by Jacobi) , and on
the hypergeometric diﬀerential equation in the complex dom ain on the other
hand. Gauss knew the connection between the two topics: the i nverse of
the indeﬁnite integral
∫ dx√
(1−x2)(1−k2x2) is a single-valued function with two
independent periods ω1 and ω2 which are solutions of the hypergeometric
diﬀerential equation with parameters ( 1
2, 1
2 ; 1) in the variable k2.
Riemann’s point of view of the ‘Riemann surface’ of a multiva lued com-
plex function has given a geometric framework for all of comp lex analysis.
He applied this idea with equal success to Jacobi’s inversio n problem for
more general indeﬁnite algebraic integrals on one hand; and to the eluci-
dation of the paradoxical polymorphism of hypergeometric f unctions which
had puzzled Gauss and Kummer by introducing the concept of mo nodromy,
on the other hand. He studied in detail the monodromy of the mu ltivalued
map k2↦→τ =ω2/ω1 , the ﬁrst and basic example of a ‘period mapping’ ,
whose inverse is single-valued. He also showed (and Schwarz rediscovered)
2 INTRODUCTION
that under certain conditions, the quotient of two solution s of more gen-
eral hypergeometric equations maps the upper half-plane on to a curvilinear
triangle.
Group-theoretic aspects of monodromy were studied by Jorda n, and
the geometrization of complex analysis around the concept o f automorphic
function was carried on by Klein, who once described his work as ‘blending
Galois with Riemann’ (1). The achievement fell to Poincar´ e. Starting from
Fuchs’ problem of ﬁnding all second-order diﬀerential equa tions for which a
quotient of solutions τ admits a single-valued inverse, Poincar´ e founded the
theory of ‘uniformizing diﬀerential equations’ (in modern terminology), and
eventually recognized that every Riemann surface of genus > 1 should arise
from the action of a discrete group of non-euclidean moves on the upper
half-plane.
What about non-archimedean analogues of this saga?
It is clear that the development of p-adic analysis and geometry took a
strikingly diﬀerent route.
The very beginnings looked similar, indeed: J. Tate introdu ced rigid ge-
ometry as a proper framework for the uniformization C×
p/qZ of elliptic curves
with multiplicative reduction; B. Dwork developed p-adic analysis start-
ing from the hypergeometric diﬀerential equation with para meters ( 1
2, 1
2 ; 1),
where he discovered the essential notion of ‘Frobenius stru cture’. But it
was immediately clear that since solutions of p-adic diﬀerential equations do
not converge up to the next singularity, no faithful counter part of complex
monodromy could take place.
From there on, diﬀerent p-adic theories grew apart, with their own lan-
guages, most of them relying on sophisticated parts of conte mporary alge-
braic geometry, and all claiming some analogy with “the comp lex case”:
– the theory of diﬀerential equations matured slowly (with a s trong
orientation toward applications to exponential sums), str uggling with
the problems of singularities, without being able to tackle global prob-
lems,
– crystalline theory oﬀered a global viewpoint on diﬀerentia l equations
(oriented toward the cohomology of varieties in positive ch aracteris-
tic), but did not help to understand singularities,
– the theory of p-adic representations and p-adic Hodge theory devel-
oped independently of diﬀerential equations, as did the sev eral avatars
of rigid geometry, motivated by idiosyncratic problems.
However, it is the author’s opinion that the situation has so mewhat
changed over the last years, that isolated branches are merg ing by ﬁts and
(1)quoted from [ Gray86, p. 179].
3
starts(2), and that a synthesis is gradually emerging. This encourage s to
hope that, after many twists and turns, period mappings can i ndeed become
a unifying theme in the p-adic context. This book is intended to be a
contribution in this direction, by bringing closer the p-adic theory to its
complex precursor — from periods and monodromy up to triangl e groups.
Much remains to be done in order to achieve comparable harmon y and
clarity.
Contents of this book.
Chapter I is preparatory. It deals with the problems of analytic conti n-
uation — with emphasis on the case of solutions of diﬀerentia l equations —
and periods of abelian integrals, in the p-adic context.
Multivalued complex-analytic functions can be handled in t wo diﬀerent,
but essentially equivalent, ways:
1) in a geometric way using Riemann surfaces, coverings and p aths;
2) as limits of algebraic functions; this less orthodox way l eads to a more
Galois-theoretic viewpoint on analytic continuation.
Both ways are practicable in the p-adic context, but eventually lead to
completely diﬀerent theories of analytic continuation.
Following the ﬁrst way demands to have at disposal p-adic spaces which
are locally arcwise connected. Surprisingly enough in view of the fractal
nature of p-adic numbers, such a nice p-adic geometry does exist: it has
been built by V. Berkovich (from the categorical viewpoint, it is essentially
equivalent to rigid geometry, in the sense of Tate and Raynau d). In this
framework, the monodromy of diﬀerential equations can be an alyzed in the
usual way; but a new phenomenon occurs: it is no longer true th at there
exists a basis of solutions around every ordinary point. Thi s approach is
therefore limited to a rather special class of connections. We shall see in
the sequel how the theory of p-adic period mappings provides interesting
examples in this class.
Following way 2), one encounters Dwork’s notion of Frobeniu s structure,
which has often been considered as a plausible substitute fo r monodromy
in the p-adic context. We discuss so-called unit-root crystals and overcon-
vergence, and illustrate these notions by Dwork’s treatmen t of the p-adic
Gamma function Γ p, the Gross-Koblitz formula, and by a detailed study of
the p-adic hypergeometric function F ( 1
2, 1
2, 1;z).
Abelian periods show themselves in two diﬀerent ways:
1) as integrals of algebraic diﬀerentials over loops,
(2)let us mention notably the incursion of rigid geometry into t he crystalline viewpoint
and into the geometric theory of ﬁnite coverings, the maturi ty of index theory and its
applications to algebraic geometry in positive characteri stic, the new connections between
p-adic representations and diﬀerential equations on annuli ...
