---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:introduction}
Walnut is a software package that implements a \emph{mechanical
decision procedure} for deciding certain combinatorial properties of
some special words referred to as \emph{automatic words} or
\emph{automatic sequences}. To learn more about automatic words and
their applications, see \cite{Allouche&Shallit:book}. To learn about
decision procedures for automatic words, see Schaeffer's Master's
thesis \cite{Schaeffer:thesis} and the survey paper
\cite{Shallit:survey}. To read more about decidable properties of
automatic words, refer to
\cite{Charlier&Rampersad&Shallit:enumeration}. To read about another
software package that provided a similar mechanical decision procedure
for automatic words, and was developed before Walnut, read Goc's
Master's thesis \cite{Goc:thesis}. To see applications of Walnut, refer
to \cite{paperfolding,tribonacci,fib1,fib2,fib3,balanced}.

The aim of this article is to introduce Walnut and explain its core
features. This article consists of four parts: basics, syntax,
implementation, and the Walnut guide. In the first part, Section
\ref{sec:basics}, we establish the basic notation and concepts. We go
over words, automata, number systems, automatic words, and Presburger
arithmetic. We learn what it means for an automaton to accept a
predicate. We also learn how to automatically decide properties of
automatic words.

The second part, Section \ref{sec:syntax and semantic}, talks about the
building blocks of predicates: constants, variables, operators, and
different types of expressions. The semantics of predicates in
Presburger arithmetic are well-known and are not explained, whereas
semantic rules for calling and indexing, with which we extend the
Presburger arithmetic to include automatic words, are explained in
detail.

The third part, Sections \ref{sec:decision procedure} and
\ref{sec:special automata}, explains the decision procedure implemented
in Walnut. The cross product of two automata, which is behind the
construction of automata for all binary logical operators, is
introduced. Building on that, we see how to construct automata for
predicates from automata for subpredicates. In Section \ref{sec:special
automata}, we talk about two types of automata that do not appear often
in Walnut, but are nevertheless important to understand.

The fourth and last part, Sections
\ref{sec:installation}--\ref{sec:working with input and output}, starts
with Walnut's installation and goes over all of its commands, i.e.,
exit, eval, def, reg, and load. In Section \ref{sec:working with input
and output}, we learn how to manually define automata in text files. We
also learn how to define new number systems.

If you are already familiar with the objects described in the first
sentence of this introduction, you can skip Section \ref{sec:basics}
and come back to it only as a reference.  For a more comprehensive
treatment of the theory behind decision procedures for automatic words
refer to
\cite{Schaeffer:thesis,Shallit:survey,Charlier&Rampersad&Shallit:enumeration}.

Since this article is more about Walnut than the theory behind it, when
we explain the latter, we use Walnut's notation as opposed to the more
familiar mathematical notation. For example, we use $\AND$ and $\A$ for
conjunction and universal quantifier as opposed to $\wedge$ and
$\forall$ of mathematical logic \footnote{Users enter logical
predicates in a terminal when they use Walnut. We find that entering
latex-like commands in the terminal, e.g., \textbackslash forall, does
not improve the readability.}. As another example, when we define
structures such as number systems or objects such as automatic words,
we give the definitions that are closer to Walnut's capabilities than
the most general theoretical ones possible. This will help the reader make
a smoother transition from the theory to its application in Walnut.

You can download Walnut from Jeffrey Shallit's
\href{https://cs.uwaterloo.ca/~shallit/papers.html}{website}, or alternatively from \href{https://github.com/hamoonmousavi/Walnut.git}{GitHub}. Walnut is
written in Java and is open source. It is licensed under GNU General
Public License. We would appreciate it if users cite this article in
their publications. For automata minimization Walnut relies on Valmari's minimization algorithm \cite{valmari:2012}. In order to use this minimization algorithm in Walnut, we manually translated Valmari's C++ implementation \cite{dfa.minimizer} almost varbatim to Java. For converting regular
expressions to automata, Walnut relies on the automata library in
\cite{dk.brics}. We would greatly appreciate it if users report bugs to
\href{mailto:sh2mousa@uwaterloo.ca}{sh2mousa@uwaterloo.ca}. The author would like to thank Jeffrey Shallit for revising this article.
