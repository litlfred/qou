---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 4-5
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.726
latex_coverage_ratio: 0.997
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Originating from the pioneering work of Alexander
\cite{Alexander2} and Artin \cite{Artin,Artin2}, braid
theory has become intrinsically interwoven with knot theory,
and over the years, braid representations of different types
have been studied, many of them with motivation coming
from fields outside of knot theory, for example dynamical
systems \cite{Williams} or 4-dimensional QFTs \cite{Kreimer}.

The systematic study of closed 3-braids was begun by Murasugi
\cite{Murasugi2}. Later 3-braid links have been classified
in \cite{BirMen}, in the sense that 3-braid representations
of the same link are exactly described. This is, up to
a few exceptions, mainly just conjugacy. The conjugacy
problem of 3-braids has a series of solutions, starting with
Schreier's algorithm \cite{Sc}, going over Garside
\cite{Garside} (for arbitrary braid groups), Xu \cite{Xu}
(and later more generally Birman-Ko-Lee \cite{BKL}), until,
for example, a recent algorithm of linear complexity due to
Fiedler and Kurlin \cite{FK}. So Birman-Menasco's work allows
to decide if two 3-braids have the same closure link.

However, many properties of links (except achirality and
invertibility) are not evident from (3-strand) braid
representations, and thus to classify 3-braid links with
special properties remains a non-trivial task. A first result
was given in \cite{Murasugi} for rational links, and then
improved in \cite{3br}, where we completed this project for
alternating links.

{}From the opposite point of view, a natural question concerning
braid representations of links is: 

\begin{question}\label{q1}
If a braid representation of a particular type exists, does
also one exist with the minimal number of strands (among all
braid representations of the link)?
\end{question}

The minimal number of
strands for a braid representation of a link $L$ is called the
\em{braid index} of the link, and will be denoted by $b(L)$.

In \cite{Bennequin}, Bennequin studied in relation to contact
structures braid representations by bands, independently considered
by Rudolph \cite{Rudolph} in the context of algebraic curves, and
more recently in \cite{BKL} from a group theoretic point of view.
A band representation naturally spans a Seifert surface of the
link. See figure \reference{figbd}.
 
\begin{figure}[h]
\[

\epsfs{5cm}{fig1}

\]\\[-14mm]
\caption{A braided Seifert surface obtained from a band representation
\label{figbd}}
\end{figure}
 




























Bennequin proved in \cite{Bennequin} that a minimal genus band
representation always exists on 3-braids. Such surface was called
by Birman-Menasco \cite{BirMen2} a Bennequin surface. Later, by
examples found by Ko and Lee, and Hirasawa and myself, the
existence of Bennequin surfaces on the minimal number of strands
was found not to extend to 4-braids. (We will see in this paper,
though, among many other things, that it does extend for
alternating links.) Since by Rudolph's work \cite{Rudolph},
a Bennequin surface exists for any link, on a possibly large
number of strands, the answer to the question \reference{q1}
is negative for minimal genus band representations. 

A special case of band representations are the positive ones,
called strongly quasi-positive in \cite{Rudolph}. For such
representations the above examples do not apply. The existence
of minimal such representations is a question of Rudolph, whose
answer is not known. Our first result is a positive answer to
Rudolph's question for 3-braids. 

\begin{theorem}\label{thqp}
If $L$ is a strongly quasi-positive link, and has braid index 3,
then $L$ is has a strongly quasi-positive 3-braid representation.
\end{theorem}

This result is an application of the work in \cite{3br} on
Xu's normal form \cite{Xu}. It legitimizes the term ``strongly
quasi-positive 3-braid link'', which otherwise would be
linguistically sloppy, for it may mean a 3-braid link that is strongly
quasi-positive, or the link (which is the closure) of a strongly
quasi-positive 3-braid.


As an (\em{a-priori}-so-seeming) improvement of Bennequin's
theorem, Birman-Menasco proved \cite{BirMen2} that
for 3-braid links not only some but in fact \em{any} minimal genus
surface is a Bennequin surface. Xu used this result and the
classification in \cite{BirMen} to conclude that most 3-braid links
have a unique minimal genus surface. Unfortunately, she failed to
deal (in the oriented sense) with some exceptions, which we complete
in section \reference{SA} (see theorem \reference{wu}).

The following work involves a further study of Xu's normal form.


A natural relation of this form to the skein polynomial was
exhibited in \cite{3br}. Here we extend this study to the Alexander
polynomial $\Dl$. As a result, we can describe 3-braid links with
given $\Dl$, and in particular show no non-trivial 3-braid
knot has trivial polynomial. In \cite{Birman}, Birman constructed
some pairs of different 3-braid links with the same polynomials
and proposed the problem to understand the values of the various
link polynomials on 3-braid links. Our work solves (to a large
extent at least) Birman's problem for the Alexander polynomial.
We also have a solution for the Jones and Brandt-Lickorish-
Millett-Ho $Q$ polynomial. 

Parallel to the Alexander polynomial description, and using
a recent result of Hirasawa-Murasugi, we classify among 3-braid
links the fibered ones. (This result was proved independently
by Yi Ni in \cite{Ni}, apparently unaware of this work, which
I did to make widely public immediately.) We will see then
that a 3-braid knot is fibered if (and only if) its Alexander
polynomial is monic, but that this is \em{not} true for 2- or
3- component links.

The fact that most 3-braid links were found fibered,
and this could be proved independently from Bennequin and
Birman-Menasco, opened the hope for a more natural approach to
some of their results. Finally we were indeed able to complete this
project, with the assistance of M. Hirasawa and M. Ishiwata, obtaining

\begin{theorem}\label{thuq}
Any 3-braid link has a unique (non-closed) incompressible surface.
\end{theorem}

This result subsumes all previous uniqueness theorems. Besides,
its proof is entirely different, in that it fully avoids the contact
geometry approach of Bennequin and the considerable complexity
in Birman-Menasco's subsequent braid foliation work. Instead,
we use the sutured manifold theory of Gabai \cite{Gabai,Gabai2}
(to deal with the fibered links) and Kobayashi-Kakimizu \cite{
Kobayashi,Kakimizu} (for the remaining cases), as well as some
of our preceding work on the Alexander polynomial (to rule out
disconnected Seifert surfaces). Since Kobayashi-Kakimizu use
a slightly stronger notion of uniqueness (see the beginning of
\S\reference{Uq}), theorem \reference{thuq} is an improvement even
for minimal genus surfaces. Moreover, its proof underscores the
geometric meaning of Xu's form, that remained unclear in \cite{BirMen}.
While we still cannot provide an ``easy'' proof of Birman-Menasco's
classification theorem (see remark on p.~34 of \cite{BirMen}), our
work will likely lead to simplifications in their very lengthy
treatment, which makes heavy use of incompressible surfaces.

The study and applications of Xu's form occupy the first main
part of the paper. Then some related results are included,
whose treatment requires different methods. These
results are dealt with in the later sections of the paper.

As a first such topic, more substantial effort will be made to
prove an analogous result to theorem \reference{thqp} for
positive (in the usual Artin generators) braid representations.

\begin{theorem}\label{thg}
If $L$ is a positive braid link, and has braid index 3, then 
$L$ is a positive 3-braid link.
\end{theorem}

So our work here can be understood to answer question
\reference{q1} for braid index 3 and strongly quasi-positive
or positive braid links. (The state of quasi-positive links,
and of quasi-positive braid representations with regard to 
question \reference{q1}, in contrast remains open. There is,
however, an algorithm, found by orevkov \cite{Orevkov}
to decide if a 3-braid is quasi-positive.)

The proof of theorem \reference{thg} requires a study of positive
braids where the braid index bound in the Morton-Williams-Franks
inequality \cite{Morton,WilFr} is 3. This study builds on and extends
(but also considerably simplifies) the work of Nakamura
\cite{Nakamura} for Morton-Williams-Franks bound 2. Then some
detailed case distinction and calculation are necessary.
In \cite{posex_bcr} it was shown, again, that theorem
\reference{thg} is not true for 4-braids: there are two 16 crossing
knots that have positive 16 crossing 5-braid representations,
but braid index 4 (and consequently only non-positive 4-braid
representations). It is in fact for these examples that I was
led to investigate about the theorem.

In section \ref{Spos},




using the arguments in the proof of theorem \reference{thg}
and a criterion of Yokota \cite{Yokota}, we consider 3-braid
representations of links that are (diagrammatically) positive.
We obtain strong restrictions on such representations,
and in particular determine which of the links are not fibered.
(See theorem \ref{thposq}.)












Another problem proposed by Birman, in \cite{MortonPb},
was to understand the relation of alternation of links
(as a pre-eminent diagram defined property) and braid
representations. Early substantial results on the braid
index of alternating links were due to Murasugi \cite{Murasugi},
who determined the braid index for rational and fibered
alternating links. In \cite{3br} we used Xu's form to classify
the braid index 3 alternating links. Here, in \S\reference{Sfg},
we will easily recover this result and push it forward to braid
index 4. For this we use an argument based on the Jones polynomial,
and connect the celebrated Kauffman-Murasugi-Thistlethwaite work
\cite{Kauffman2,Murasugi3,Thistle2} to braid representations.
The existence of the Bennequin surface of alternating links on a
4 string braid (corollary \reference{cfT}) is among several easy
consequences we obtain.

The last section \S\reference{SBurau} discusses some applications
of the Squier unitarization \cite{Squier} of the Burau
representation, that concern also braids on more strings. A
first series of conditions are estimates on the norm of special
values of the Alexander and Jones polynomial. They relate to and
partly extend estimates of Jones in \cite{Jones}. In particular, we
will see that the Alexander polynomial provides conditions for every
given braid index. Some properties of the skein polynomial, and a
relation to Mahler measure are also discussed.

In the case of a 4-braid, one can go further and (almost)
identify the Eigenvalues of the Burau matrix
from the Alexander and Jones polynomial (of its closure).
Using this, a criterion for braid index 4 is derived.
We show examples exhibiting the efficiency of this test, including
such where not only the Morton-Williams-Franks inequality itself,
but also its 2-cable version fails (and so our test seems the only
practicable option).



In the appendix we collect some work of Hirasawa, Ishiwata and
Murasugi, which completes the proof of several of our results.
