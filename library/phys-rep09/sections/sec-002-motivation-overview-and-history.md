---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-002-motivation-overview-and-history
section_title: "Motivation, overview and history"
section_number: null
pages: 3-6
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The outstanding mathematician Wilhelm Magnus (1907-1990) made important contributions to a wide variety of fields
in mathematics and mathematical physics [1]. Among them, one can mention combinatorial group theory [2] and his
collaboration in the Bateman project on higher transcendental functions and integral transforms [3]. In this report we review
another of his long-lasting constructions: the so-called Magnus expansion (hereafter referred to as ME). ME was introduced
as a tool to solve non-autonomous linear differential equations for linear operators. It is interesting to observe that, in his
seminal paper of 1954, [4], although it is essentially mathematical in nature, Magnus recognizes that his work was stimulated
by results of K.O. Friedrichs on the theory of linear operators in Quantum Mechanics [5]. Furthermore, as the first antecedent
of his proposal, he quotes a paper by R.P. Feynman in the Physical Review [6]. We stress these facts to show that already, at
its very beginning, ME was strongly related to Physics, and has been ever since, and there is no reason to doubt that it will
continue to be. This is the first motivation to offer here a review as the present one.

Magnus’ proposal has the very attractive property of leading to approximate solutions which exhibit, at any order of
approximation, some qualitative or physical characteristics, which the first principles guarantee for the exact (but unknown)
solution of the problem. Important physical examples are the symplectic or unitary character of the evolution operator when
dealing with classical or quantum mechanical problems, respectively. This is at variance with most standard perturbation
theories, and is apparent when formulated in a correct algebraic setting: Lie algebras and Lie groups. But this great advantage
has sometimes been tainted in the past, by the difficulties both in constructing explicitly higher order terms, and in assuring
existence and convergence of the expansion.

In our opinion, recent years have witnessed great improvement in this situation. Concerning general questions of
existence and convergence, new results have appeared. From the point of view of applications, some new approaches in
old fields have been published, while completely new and promising avenues have been opened by the use of the Magnus
expansion in Numerical Analysis. It seems reasonable to expect fruitful cross fertilization between these new developments
and the most conventional perturbative approach to ME and, from it, further applications and new calculations.

This new scenario makes it desirable for the Physics community in different areas (and scientists and engineers in general)
to have access, in as unified a way as possible, to all the information concerning ME which, so far, has been treated in very
different settings, and has appeared scattered through very different bibliographic sources.

As implied by the preceding paragraphs, this report is mainly addressed to a Physics audience, or close neighbors, and
consequently we shall keep the treatment of its mathematical aspects within reasonable limits and refer the reader to more
detailed literature where necessary. By the same token, the applications presented will be limited to examples from Physics,
or from the closely related field of Physical Chemistry. We shall also emphasize its instrumental character for numerically
solving physical problems.

In the present section, as an introduction, we present a brief overview and sketch a history of more than 50 years of ME.
To start with, let us consider the initial value problem associated with the linear ordinary differential equation

Y(t) =AMY(O), — Y(to) = Yo, (1)

where, as usual, the prime denotes the derivative with respect to the real independent variable which we take as time t,
although much of what will be said also applies to a complex independent variable. In order of increasing complexity, we
may consider the equation above in different contexts:

(a) Y : R—> C,A: R —> C. This means that the unknown Y and the given A are complex scalar valued functions of one
real variable. In this case, there is no problem at all: the solution reduces to a quadrature and an ordinary exponential
evaluation:

Y(t) = exp (/ or) Yo. (2)
to

(b) Y: R—> C",A: R—> M,C), where M,,(C) is the set of n x n complex matrices. Now Y is a complex vector valued
function, and A a complex n x n matrix valued function. At variance with the previous case, only in very special cases is
the solution easy to state: when for any pair of values of t, t; and t2, one has A(t; )A(t2) = A(t2)A(t1), which is certainly
the case if A is constant. Then the solution reduces to a quadrature (trivial or not) and a matrix exponential. With the
obvious changes in the meaning of the symbols, Eq. (2) still applies. In the general case, however, there is no compact
expression for the solution and (2) is no longer the solution.
154 S. Blanes et al. / Physics Reports 470 (2009) 151-238

(c) Y: R—> M,(C),A : R — M,(C). Now both Y and A are complex matrix valued functions. A particular case, but still
general enough to encompass the most interesting physical and mathematical applications, corresponds to Y(t) € ,
A(t) € g, where 9, and g are, respectively, a matrix Lie group and its corresponding Lie algebra. Why this is of interest,
is easy to grasp: the key reason for the failure of (2) is the non-commutativity of matrices in general. So one can expect
that the (in general non-vanishing) commutators play an important role. But when commutators enter the play, one
immediately thinks in Lie structures. Furthermore, plainly speaking, the way from a Lie algebra to its Lie group is covered
by the exponential operation — a fact that will be of no surprise in this context. The same comments of the previous case
are valid here. In this report, we shall mostly deal with this matrix case.

(d) The most general situation one can think of corresponds to Y(t) and A(t) being operators in some space, e.g., Hilbert space
in Quantum Mechanics. Perhaps the most paradigmatic example of (1) in this setting is the time-dependent Schrodinger
equation.

Observe that case (b) above can be reduced to case (c). This is easily seen if one introduces what, in mathematical
literature, is called the matrizant, a concept dating back at least to the beginning of the 20th century in the work of Baker
[7]. It is the n x n matrix U(t, to) defined through

Y(t) = U(t, to) Yo. (3)

Without loss of generality, we will take t) = O unless otherwise explicitly stated, for the sake of simplicity. When no
confusion may arise, we write only one argument in U and denote U(t, 0) = U(t), which then satisfies the differential
equation and initial condition

U(t)=A(U(t), U0) = 1, (4)

where | stands for the n-dimensional identity matrix. The reader will have recognized U(t) as what, in physical terms, is
known as the time evolution operator.
We are now ready to state Magnus’ proposal: a solution to (4) which is a true matrix exponential

U(t) =expQ(t), 2(0)=0, (5)

and a series expansion for the matrix in the exponent

Q(t) = > A(t), (6)

k=1

which is what we call the Magnus expansion. The mathematical elaborations explained in the next section determine 92;(t).
Here we just write down the three first terms of that series:

t
a= | A(ty)dty,
0
ire t
Q2(t) = al an [ dty [A(t1), A(ta)] (7)
0 0

ire t to
23(t) = al at, [ ar | dts ([A(ti), [A(t2), A(ts)]] + [A(ts), [A(t2), A(t) I)
0 0 0

where [A, B] = AB — BA is the matrix commutator of A and B.

The interpretation of these equations seems clear: (2;(t) coincides exactly with the exponent in (2). But this equation
cannot give the whole solution, as has already been said. So, if one insists on having an exponential solution, the exponent
has to be corrected. The rest of the ME in (6) gives that correction, necessary to keep the exponential form of the solution.

The terms appearing in (7) already suggest the most appealing characteristic of ME. Remember that a matrix Lie algebra
is a linear space in which one has defined the commutator as the second internal composition law. If, as we suppose, A(t)
belongs to a Lie algebra g for all t, so does any sum of multiple integrals of nested commutators. Then, if all terms in ME have
a structure similar to that of the ones shown before, the whole §2(t) and any approximation to it obtained by truncation of
ME, will also belong to the same Lie algebra. In the next section, it will be shown that this turns out to be the case and, a
fortiori, its exponential will be in the corresponding Lie group.

Why is this so important for physical applications? Just because many of the properties of evolution operators derived
from first principles are linked to the fact that they belong to a certain Lie group: e.g. unitary group in Quantum Mechanics,
symplectic group in Classical Mechanics. In that way, use of (truncated) ME leads to approximations which share, with the
exact solution of Eq. (4), important qualitative (very often, geometric) properties. For instance, in Quantum Mechanics every
approximant preserves probability conservation.

From the present point of view, we could say that the last paragraphs summarize, in a nut shell, the main contents of the
famous paper of Magnus of 1954. With no exaggeration, its appearance can be considered a turning point in the treatment
of the initial value problem defined by (4).
S. Blanes et al. / Physics Reports 470 (2009) 151-238 155

But important as it certainly was, Magnus’ paper left some problems, at least partially, open:

e First, for what values of t and for what operators A does Eq. (4) admit a true exponential solution? This, we call the
existence problem.

e Second, for what values of t and for what linear operators A does the series in Eq. (6) converge? This we describe as the
convergence problem. We want to emphasize that, although related, these are two different problems. To see why, think
of the scalar equation y’ = y? with y(0) = 1. Its solution y(t) = (1 — t)~! exists for t 4 1, but its form in power series
y(t) = yo t" converges only for |t| < 1.

e Third, how does one construct higher order terms 2;(t),k > 3, in the series? Moreover, is there a closed-form expression
for 2,(t)?

e Fourth, how does one calculate in an efficient way exp 2!%!, where Q!N! = ae Q(t) is a truncation of the ME?

All these questions, and many others, will be dealt with in the rest of the paper. But before entering that analysis, we
think it is interesting to present a view, however brief, from the historical perspective of the half-century of developments
on the Magnus series. Needless to say, we by no means try to present a detailed and exhaustive chronological account of
the many approaches followed by authors from very different disciplines. To minimize duplication with later sections, we
simply mention some representative samples, so that the reader can understand the evolution of the field.

Including some precedents, and with a (as undeniable as unavoidable) dose of arbitrariness, we may distinguish four
periods in the history of our topic:

(1) Before 1953. The problem which ME solves has a centennial history dating back at least to the work of Peano, by the
end of 19th century, and Baker, at the beginning of the 20th (for references to the original papers see e.g. [8]). They
combine the theory of differential equations with an algebraic formulation. Intimately related to these treatments from
the very beginning, is the study of the so called Baker-Campbell-Hausdorff (or BCH formula for short) [9-11] which
gives C in terms of A, B and their multiple nested commutators when expressing exp(A) exp(B) as exp(C). This topic
has a long history in its own right, and will also be discussed in Section 2. As one of its early hallmarks, we quote [12].
In Physics literature, the interest in the problem posed by Eq. (4) was very much revived with the advent of Quantum
Electrodynamics (QED). The works of Dyson [13] and, in particular, Feynman [6] in the late forties and early fifties, are
worth mentioning here.

1953-1970. We have quoted as the ‘birth certificate’ of ME, the paper [4] by Magnus in 1954. This is not strictly true:
there is a Research Report [14] dated June 1953 which differs from the published paper in the title and in a few minor
details, and which should in fact be taken as a preliminary draft of it. In both publications, the result summarized above
on ME appears, in almost identical words. The work of Pechukas and Light [15] gave, for the first time, a more specific
analysis of the problem of convergence than the rather vague considerations in Magnus’ paper. Wei and Norman [16,
17] did the same for the existence problem. Robinson, to the best of our knowledge, seems to have been the first to apply
ME to a physical problem [18]. Special mention in this period should be given to a paper by Wilcox [19], in which useful
mathematical tools are given, and ME is presented together with other algebraic treatments of Eq. (4), in particular
Fer’s infinite product expansion [20]. Also worth mentioning here, is the first application of ME as a numerical tool for
integrating the time-independent Schrédinger equation for potential scattering, by Chang and Light [21].

(3) 1971-1990. During these years, ME was consolidated on different fronts. It was successfully applied to a wide spectrum
of fields in Physics and Chemistry: from atomic [22] and molecular [23] Physics to Nuclear Magnetic Resonance
(NMR) [24,25] to Quantum Electrodynamics [26] and elementary particle Physics [27]. A number of case studies also
helped to clarify its mathematical structure, see for example [28]. The construction of higher order terms was approached
from different angles. The intrinsic and growing complexity of ME allows for different schemes. One which has shown
itself very useful in tackling other questions like the convergence problem, was the recurrent scheme by Klarsfeld and
Oteo [29].

Since 1991. The last decade of the 20th century witnessed a renewed interest in ME, which still continues now. It has
followed different lines. Concerning the basic problems of existence and convergence of ME, there has been definite
progress [30-33]. ME has also been adapted for specific types of equations: Floquet theory when A(t) is a periodic
function [34], stochastic differential equations [35] or equations of the form Z’ = AZ — ZB [36]. Special mention should
be made of the new field, open in this most recent period, that uses Magnus’ scheme to build novel algorithms [37]
for the numerical integration of differential equations within the widest field of geometric integration [38]. After
optimization [39,40], these integrators have proved to be highly competitive.

(2

(4

As proof of the persistent impact the 1954 paper by Magnus has had in scientific literature, we present in Figs. 1 and 2, the
number of citations per year and the cumulative number of citations, respectively, as December 2007 with data taken from
ISI Web of Science. The original paper appears about 750 times of which, roughly, 50, 320 and 380 correspond, respectively,
to each of the last three periods we have considered. The enduring interest in that seminal paper is clear from the figures.

The presentation of this report is organized as follows. In the remainder of this section, we include some mathematical
tools and notations that will be used time and again in our treatment. In Section 2 we formally introduce the Magnus
expansion, study its main features and thoroughly analyze the convergence issue. Next, in Section 3 several generalizations
of the Magnus expansion are reviewed, with special emphasis in its application to general nonlinear differential equations.
In order to illustrate the main properties of ME, in Section 4 we consider simple examples for which the computations
156 S. Blanes et al. / Physics Reports 470 (2009) 151-238

35

Source: ISI Web of Science (2007)

20

15

Number of citations

va

od
1

0 fe, 1 1 1 1
1960 1970 1980 1990 2000

Year

Fig. 1. Persistency of Magnus’ original paper: number of citations per year.

800

»
700 + | Source: ISI Web of Science (2007) ”

600 F

500 -

400 F

300 F

Cumulative no. citations

200

100

1960 1970 1980 1990 2000
Year

Fig. 2. Persistency of Magnus’ original paper: cumulative number of citations.

required are relatively straightforward. Section 5 is devoted to an aspect that has been most recently studied in this setting:
the design of new algorithms for the numerical integration of differential equations based on the Magnus expansion. There,
after a brief characterization of numerical integrators, we present several methods that are particularly efficient, as shown
by the examples considered. Given the relevance of the new numerical schemes, we briefly review in Section 6 some of its
applications in different contexts, ranging from boundary-value problems to stochastic differential equations. In Section 7,
on the other hand, applications of the ME to significant physical problems are considered. Finally, the paper ends with some
concluding remarks.
