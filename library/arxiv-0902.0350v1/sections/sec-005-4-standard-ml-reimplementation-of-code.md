---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE"
section_id: sec-005-4-standard-ml-reimplementation-of-code
section_title: "Standard ML reimplementation of code"
section_number: 4
pages: 10-12
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.987
doc_brief: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
\label{sec:code}

This section describes a reimplementation of the computer code 
used in the proof of the Kepler conjecture. 
The code has been substantially
redesigned to avoid various difficulties
with the original implementation.


\subsection{Code}

The original proof of the Kepler conjecture relies significantly on
computation. Computer code is used extensively and is central both to
the correctness of the result and to a thorough understanding of the
proof.

  There are four major difficulties with understanding and verifying
the original code base. The first and most glaring difficulty is
simply the amount of code. At the website~\cite{website:Hales:1998:Code}
that posts the code for the original proof
there are well over 50,000 lines of programs in Java, C++, and
Mathematica (among others). This represents only the calculations that Hales did himself.
Samuel Ferguson also completed many of the calculations with an entirely
different code base\footnote{There is a large amount of
code copying in Ferguson's code, resulting in a much larger code base.
The number of distinct lines is difficult to measure} of 137,000 lines of C. By
contrast, the proof of the four color theorem by Robinson \textit{et
al.}~\cite{Robertson:1997:JCTB} is less than 3,000 lines of C.

The second difficulty is in the organization of the code. The
calculations were done over the space of four years and involved
thousands of executions of a multitude of independent programs. 
Section~\ref{sec:intro} identifies  three main computational
tasks: tame graph generation, linear program
bounding, and nonlinear inequality verification.  Each of these main
tasks consists of several subtasks.  For example, verifying the
inequalities required dozens of relatively complicated preprocessing
phases where second derivatives of the relevant functions were bounded
over fixed domains.  As another example, many linear programs were
solved only after a branch and bound period which were recorded in
voluminous log files.  In an attempt to organize the complex 
web of calculations, Hales
devised a labeling scheme to uniquely identify the calculations.
However, even now some computations relied upon by the proof are
difficult to find in the original source code.  To locate, for
instance, computation ``\calc{821707685}'' from the original
proof~\cite[p.159]{Hales:2006:DCG}, one can search on the
website~\cite{website:Hales:1998:Code} in vain.  While records of the
computations were made, it is not always an easy matter to find them
without guidance from the authors.

The third difficulty lies in the complexity of the implementation. For
instance, the software developed to prove the inequalities upon which
the original proof rests is relatively complicated. Processing power
at the time (1994-1998) was just barely capable of completing the
computations requested. To keep the length of execution to days or
weeks instead of months or years, the code is extensively
optimized. The optimizations were often implemented without comment in
the source and in some cases are difficult to understand.

The fourth difficulty is that
the original code uses C and C++ to carry out \emph{interval
arithmetic} calculations based on \emph{floating point arithmetic}. In
the process, it explicitly sets the IEEE 754~\cite{IEEE:1985:IEE754}
rounding modes on the processor's floating point unit.  While floating
point is desirable for its speed, there are difficulties with using
floating point for software that requires a very high level of rigor
such as that supporting mathematical proof.  The first is that
reasoning about floating point instructions requires a relatively deep
understanding of the machine architecture~\cite{Monniaux:2008:TOPLAS}.
For instance, setting the rounding mode changes the state of the
processor itself. Such an instruction has a global effect on all
subsequent floating point computations.  In the original code base the
rounding modes are explicitly changed at least 400 times.  Moreover,
compilers, libraries, and even processors are notorious for unsound
implementations of the 754 standard.  






\subsection{Reimplementation}
\label{sec:sean}

In 2004 we decided to reimplement the original code
base.  We decided that the new implementation should not require 
floating point numbers and rounding modes.  Though speed
was important, we wanted the code to be independent of any particular
interval arithmetic implementation.  This meant we could use a fast
floating point implementation of interval arithmetic for our daily
work, but could use a slower but more trustworthy implementation such
as MPFI~\cite{Revol:2005:MPFI} to double check important computations.
We also wanted to organize the new implementation such that any of the
many computations upon which the proof relies could be evaluated from
a single interface.  This would allow Flyspeck developers to 
find and easily check the text of the proof during the formalization process.
Finally, we wished to bring the computational aspects of the
Kepler conjecture closer to the level of simplicity and clarity
necessary for formalization by a proof assistant.  We began this work
in the spirit of Robinson \textit{et
al.}~\cite{Robertson:1997:JCTB}, which simplified the original code of
Appel and Haken~\cite{Appel:1986:FourColor}, and was used by Gonthier
to construct the fully formal proof~\cite{gonthier:2008:formal} in the
Coq proof assistant.

We chose Standard ML for the reimplementation for a number of reasons.
It has a formal definition~\cite{Milner:1990:SML}, and thus programs
have a meaning apart from the particular compiler used.  It has an
efficient compiler, named MLton~\cite{website:MLton}.  (Our
reimplementation runs between 50\% and 200\% the speed of the original
implementation compiled with GCC.)  MLton has the ability to use
external libraries written in languages other than SML with relative
ease.  This allowed us, from one programming environment, to control multiple linear programming solvers,
interval arithmetic implementations, and nonlinear optimization
packages.
SML has an expressive module system, and thus it was simple to write
our code with respect to an abstract type of interval arithmetic. 
Thus we could use multiple independent implementations
with ease.  As of 2008, most of the code has been completely
rewritten in SML and is executable
from a single command-line program.  The code is freely available
at the project website~\cite{McLaughlin:2008:KeplerCode}.

In the original implementation, the myriad computations were done with
many different programs written in a half dozen programming languages.
The results of these computations are not always easy to find or
interpret.  Now all the computations are executed from the same
source, with organized output.  In addition to giving us added
confidence that the original computations were sound, we have a fairly
complete suite of software support for the Flyspeck project. We are
now in the process of organizing and reevaluating the thousands of
computations upon which the proof depends.
