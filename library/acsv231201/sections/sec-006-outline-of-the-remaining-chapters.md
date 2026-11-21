---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-006-outline-of-the-remaining-chapters
section_title: "Outline of the remaining chapters"
section_number: null
pages: 30-35
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
This book is divided into three parts, of which the third part is the heart of the
subject: deriving asymptotics in the multivariate setting once a meromorphic
generating function is known. Nevertheless, some discussion is required on
how generating functions are obtained, how to interpret them, what the chief
motivating examples and applications are, and what we knew how to do be-
fore the line of research described in Part III. These topics also make the book
into a self-contained reference, and allow one to obtain asymptotics by deriv-
ing new forms of a generating function, turning an intractable analysis into
a tractable one by changing variables, re-indexing, aggregating, and so forth.
Consequently, the ﬁrst three chapters comprising Part I form a crash course
in univariate analytic combinatorics. Chapter 2 explains generating functions
and their uses, introducing formal power series, their relation to combinatorial
enumeration, and the combinatorial interpretation of rational, algebraic, and
transcendental operations on power series. Chapter 3 is a review of univariate
asymptotics, much of which serves as mathematical background for the multi-
variate case. While some excellent sources are available in the univariate case,
for example [dBru81; Wil06; FS09], none of these is concerned with provid-
ing the brief yet reasonably complete summary of analytic techniques that we
1.3 Outline of the remaining chapters
13
provide here. It seems almost certain that someone trying to understand the
main subject of this text will proﬁt from a review of the essentials of univariate
asymptotics.
Carrying out the multivariate analyses described in Part III requires a fair
amount of mathematical background. Most of this is at the level of graduate
coursework, ideally already known by practicing mathematicians but in reality
often forgotten, never learned, or not learned in suﬃcient depth. The required
background is composed of small to medium-sized chunks taken from many
areas: undergraduate complex analysis, calculus on manifolds, saddle point in-
tegration (both univariate and multivariate), algebraic topology, computational
algebra, and Morse theory. Many of these background topics would require a
full semester’s course to learn from scratch. That is too much material to in-
clude here, but we also want to avoid the scenario where a reference library is
required each time a reader picks up this book. Accordingly, we have included
substantial background material.
This background material is separated into two pieces. The ﬁrst piece is
the three chapters that comprise Part II, which contains material that we feel
should be read or skimmed before the central topics are tackled. The topics in
Part II have been suﬃciently pared down that it is possible to learn them from
scratch if necessary. Chapters 4 and 5 describe how to asymptotically evalu-
ate saddle point integrals in one and several variables, respectively. Familiar-
ity with these results is needed for the ﬁnal steps in the analyses in Part III
to make sense. Most of the results in these chapters can be found in a refer-
ence such as [BH86]; the treatment here diﬀers from the usual sources in that
Fourier and Laplace type integrals are treated as instances of a single complex-
phase case. Working in the holomorphic setting, analytic techniques (contour
deformation) are used whenever possible, after which comparisons are given
to the corresponding C∞approach (which uses integration by parts in place
of contour deformation). Chapter 6 covers domains of convergence of mul-
tivariate power series and Laurent series, the notion of polynomial amoebas,
and results relating amoebas to domains of convergence of Laurent series. We
also note that much of Chapter 8, which recalls several tools from polynomial
system solving such as Gr¨obner bases, morally belongs with the background
material in Part II; we have placed it in Part III so that we can compute quan-
tities appearing in our multivariate analyses that are introduced in Chapter 7.
It is possible to skip Chapter 8, if one wants to understand the theory and does
not care about computation; however, few users of analytic combinatorics live
in a world where computation does not matter.
The remaining background material is relegated to the four appendices, each
of which contains a reduction of a semester’s worth of material. It is not ex-
14
Introduction
pected that the reader will go through these in advance. Rather, they serve as
references so that frequent library visits will not be necessary. Appendix A
presents for beginners all relevant knowledge about calculus on manifolds and
algebraic topology. Manifolds and tangent and cotangent vectors are deﬁned,
diﬀerential forms in Rn are constructed from scratch, and integration of forms
is developed. The appendix ends with a short treatment of complex diﬀerential
forms. Appendix B reviews the essentials of algebraic topology: chain com-
plexes, homology and cohomology, relative homology, Stokes’s Theorem, and
some important exact sequences. Appendix C summarizes classical Morse the-
ory – roughly the ﬁrst few chapters of Milnor’s classic text [Mil63] – after
which Appendix D introduces the notion of stratiﬁed spaces and describes
stratiﬁed Morse theory as developed by Goresky and MacPherson [GM88].
Part II and the appendices also have a second function: some of the results
used in Part III are often quoted in the literature from sources that do not pro-
vide a proof. On more than one occasion, when organizing the material in this
book, we found that a purported reference to a proof ultimately led to nothing.
Beyond serving as a mini-reference library, therefore, the background sections
provide some key proofs and corrected citations to eliminate ghost references
and the misquoting of existing results.
The heart of this book, Part III, is devoted to new results in the asymptotic
analysis of multivariate generating functions. Chapter 7 sets out the theory
by which multivariate asymptotics are derived, greatly expanding the outline
given in Section 1.2. The internal structure of Chapter 7 is described at length
in the beginning of the chapter. Because some of the material in this long chap-
ter relies on specialized topological knowledge, it is possible to take a concep-
tual oﬀ-ramp after most sections, which get progressively more general as the
chapter proceeds. We begin with extended examples in Section 7.1, before de-
scribing the argument in the simpler case when V is a smooth manifold in
Section 7.2. Section 7.3 covers the general case, ultimately deriving the fun-
damental result of the chapter: a decomposition (7.2) for ar as an integer sum
of quasi-local cycles near critical points, without any speciﬁcation of the set
contrib(r) or the asymptotic series Φz.
Having reduced the computation of ar to saddle point integrals with com-
putable parameters, plugging in results on saddle point integration yields the-
orems for the end user. These break into several types. Chapter 9 discusses the
case when the singular variety V is smooth near the contributing points. This
case is simpler than the general case in several respects: the residues are more
straightforward, so multivariate residue theory is not always needed, and only
classical Morse theory is required. Chapter 10 discusses the case where V
is locally the union of smooth hypersurfaces near contributing points, which
1.3 Outline of the remaining chapters
15
is also a case that is reasonably well understood. Finally, we discuss ratio-
nal functions with singularities having non-trivial monodromy. In this case
our knowledge is limited, but some known results are derived in Chapter 11.
This chapter is not quite as self-contained as the preceding ones; in particular,
some results from [BP11] are quoted without proof. This is because the tech-
nical background for these analyses exceeds even the relatively large space
we have allotted for background. The paper [BP11], which is self-contained,
already reduces by a signiﬁcant factor the body of work presented in the cel-
ebrated paper [ABG70], and further reduction is only possible by quoting key
results. Chapter 12 works out a large number of examples following the the-
ory in Chapters 9–11. Finally, Chapter 13 is devoted to further topics, includ-
ing higher order asymptotics, algebraic generating functions, diagonals, and a
number of open problems.
Notes
The overall viewpoint on enumeration discussed here is heavily inﬂuenced
by [Sta97] and [FS09]. The two, very diﬀerent, motivating problems alluded
to in Section 1.2 were the hitting time generating function from [LL99] and
the Aztec Diamond placement probability generating function from [JPS98].
The ﬁrst versions of the seven step program at the end of Section 1.2 that were
used to obtain multivariate asymptotics involved expanding a torus of integra-
tion until it was near a critical point on the boundary of the domain of conver-
gence of the series under consideration, and then doing some surgery to isolate
the main asymptotic contribution as the integral of a univariate residue over
a complementary (d −1)-dimensional chain. This was carried out in [PW02;
PW04] and was brought to the attention of the authors by several analysts at
Wisconsin, among them S. Wainger, J.-P. Rosay, and A. Seeger. Although their
names do not appear in any bibliographic citations associated with this project,
they are acknowledged in these early publications and should be credited with
useful contributions to this enterprise.
Additional exercises
Exercise 1.2. (asymptotic expansions need not converge) Find an asymptotic
expansion f ≈P∞
j=0 gj for a function f as x ↓0 such that P∞
j=0 g j(x) is not
convergent for any x > 0. Conversely, suppose that f(x) = P∞
j=0 g j(x) for
x > 0 and g j+1 = o(gj) as x ↓0 — does it follow that P∞
j=0 gj is an asymptotic
expansion of f at the origin?
16
Introduction
Exercise 1.3. Prove or give a counterexample: if g is a continuous function
and for each λ we have ars = g(λ) + O

(r + s)−1
as r, s →∞with r/s →λ,
then ars ∼g(r/s) when r, s →∞as λ varies over a compact interval in R+.
Exercise 1.4. (Laplace transform asymptotics) Let A be a smooth real function
in a neighborhood of zero and deﬁne its Laplace transform by
ˆA(τ) :=
Z ∞
0
e−τxA(x) dx .
Writing A(x) = P
n≥0 cnxn with cn = A(n)(0)/n! and integrating term by term
using
Z ∞
0
xne−τx dx = n!τ−n−1
suggests the series
X
n≥0
A(n)(0)τ−n−1
(1.7)
as a possible asymptotic expansion for ˆA. Although the term-by-term integra-
tion is completely unjustiﬁed, show that the series (1.7) is a valid asymptotic
expansion of ˆA in decreasing powers of τ as τ →∞.
Exercise 1.5. Recall Stirling’s approximation from Example 1.4. Use a com-
puter algebra system to experiment, for 1 ≤m ≤5, with the mth order approx-
imation for n = 1, . . . , 50. For each such value of n, ﬁnd the best value m at
which to truncate the asymptotic series. For each n, what is the best relative
error in the approximation to n! that we can obtain in this way?
Exercise 1.6. Use a computer algebra system to experiment for 1 ≤m ≤20
with the error in the mth order Stirling approximation to n! when n = 1. After
which value of m does the error become noticeably bad?
