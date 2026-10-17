---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE"
section_id: sec-002-1-the-flyspeck-project
section_title: "The Flyspeck project"
section_number: 1
pages: 3-5
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.996
doc_brief: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
The purpose of a long-term project, called the Flyspeck project, is to give a formal proof of the Kepler conjecture.  This section makes some preliminary remarks about
formal proofs and gives a general overview of the current status of this project.



\subsection{Formal proof}

A formal proof is a proof in which every logical inference has been checked, all the way back to the foundational axioms of mathematics.  No step is skipped no matter how obvious it may be to a mathematician.  
A formal proof may be less intuitive, and yet is less susceptible to logical
errors.  Because of the large number of inferences involved, a computer is used to check the steps of a formal proof.

It is a large labor-intensive
undertaking to transform a traditional proof
into a formal proof.   The first stage is to expand the traditional proof in greater detail.  This stage fills in steps that a mathematician would regard as obvious,  works out arguments that the original proof leaves to the reader,  and supplies the assumed background knowledge.  
In a final stage, the detailed text is transcribed into a computer-readable format inside
a computer proof assistant.  The proof assistant  contains  mathematical axioms, logical rules of inference, and a collection of previously proved theorems. 
It validates each new lemma by stepping through each inference.  No other currently available technology is able to provide levels of certification of a complex mathematical proof that is remotely comparable to that available by formal computer verification.  A general overview
of formal proofs can be found at~\cite{gonthier:2008:formal}, \cite{Hales:2008:formal}, \cite{Harrison:2008:formal}.

Proof assistants differ in detail in the way they treat the formalization
of  a theorem that is itself a computer verification (such as
the proof of the four color theorem or the proof of the Kepler conjecture).
In general, a formal proof of a computer verification can be viewed
as a formal proof of the correctness of the computer code used in the
verification.  That is, the formal proof certifies that the the code
is a bug-free implementation of its specification.






\subsection{Formal proof of the Kepler conjecture}
\label{sec:intro}

As mentioned above, the purpose of the Flyspeck project is to give a formal proof of the Kepler conjecture.  (The project name {\it Flyspeck} comes from the acronym {\it FPK}, for the {\it Formal} {\it Proof} of the {\it Kepler} conjecture.)  This is the most complex formal proof ever undertaken.  We estimate that it may take about twenty work-years to complete this formalization project.  

The Flyspeck project is introduced in the article~\cite{hales:DSP:2006:432}.
The project page gives the latest developments~\cite{website:FlyspeckProject}.
The project is now at an advanced stage; in fact, we estimate that the project is now about half-way complete.  
One of the main purposes of this article is to present a summary of the current status of this project.

In the original proof of the Kepler conjecture, there was a long mathematical text
and  three major pieces of computer code.
The written part of the proof has been substantially revised with aims of the Flyspeck project in mind.   Section~\ref{sec:blueprint} compares this revised text with the original.  There is now a good match between the mathematical background assumed in the text and the mathematical material that is available in the proof assistant HOL Light.  Section~\ref{sec:ordinary} describes the current level of support in HOL Light for the formalization of Euclidean space and measure theory.
 In the years following the publication of the original proof, S. McLaughlin has  reworked and largely rewritten the entire body of code in a form that is more transparent and more amenable to formalization.  Section~\ref{sec:code} points out some difficulties
in verifying the computer code in its original form and
documents the reimplementation.

There have been three Ph.D. theses written on the Flyspeck
project, one devoted to each of the three major pieces of computer code.
The first piece of computer code uses interval arithmetic to verify nonlinear inequalities.  R. Zumkeller's thesis~\cite{roland-thesis} develops nonlinear inequality proving inside the proof assistant Coq.  Section~\ref{sec:zumkeller} gives an example of this work.
The second piece of computer code enumerates all tame graphs.
(The definition of tameness is rather intricate; its key property is that the set of tame graphs 
includes all graphs that give a potential counterexample to the conjecture.)
G. Bauer's thesis, together with subsequent 
work with T. Nipkow, completes the formal
proof of the enumeration of tame graphs~\cite{NipkowBS-IJCAR06}.
Section~\ref{sec:graph} gives a summary of this formalization project.
The third piece of computer code generates and runs some $10^5$ linear
programs.   These linear programs show that none of the potential counterexamples
to the Kepler conjecture are actual counterexamples.  S. Obua's thesis develops the
technology to generate and verify the linear programs inside the proof assistant Isabelle~\cite{obua:phd}. 
Section~\ref{sec:lp} describes this research.
 



The ultimate aim is to develop a complete formal proof of the Kepler
conjecture within a single proof assistant.  Because of the scope of 
the problem and the number of researchers involved, different proof
assistants have been used for different parts of the proof:
HOL Light for background
in Euclidean geometry and the text,
Coq for
nonlinear inequality verification, and
Isabelle/HOL for graph enumeration and linear programming.  This raises the issue of how
to translate a formal proof automatically from one proof assistant to another.
Implementations of automated translation among the
proof assistants HOL, Isabelle, and Coq can be found 
at~\cite{obua:import}, \cite{McLaughlin:2006:IJCAR}, \cite{wiedijk:encoding},
\cite{695027}.
