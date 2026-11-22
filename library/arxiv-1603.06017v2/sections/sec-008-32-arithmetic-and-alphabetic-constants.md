---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-008-32-arithmetic-and-alphabetic-constants
section_title: "Arithmetic and Alphabetic Constants"
section_number: 3.2
pages: 9-9
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:arithmetic and alphabetic constants}
Arithmetic constants in a predicate are allowed to be natural
numbers only. There is, however, another type of constant:  the alphabetic
constant. Alphabetic constants are useful when referring to symbols at
particular positions in automatic words. For example, the predicate that
accepts positions for which the automatic word $W$ is $1$ is written as
$W[i]=@1$. In order to draw the distinction between alphabetic and
arithmetic constants, we use alphabetic constants with a prefix of $@$.
The reason we call these constants alphabetic (as opposed to
arithmetic) is due to the fact that Walnut does not allow (and it does
not make much sense to allow) predicates that are comparing indexing
expressions \ref{sec:indexing expressions} and arithmetic expressions
\ref{sec:arithmetic expressions}, e.g., expressions such as
$W[i]=a+b$ is not allowed. As
we will see in Section \ref{sec:relative expressions}, the only objects
that can be compared with indexing expressions are alphabetic constants
and indexing expressions themselves.

Alphabetic constants are ordered like ordinary integers, so we can
compare alphabetic constants, just like we can compare arithmetic
constants. For example, $@-1<@1$ is a valid predicate, and it is always
true; see Sections \ref{sec:indexing expressions} and \ref{sec:relative
expressions}. \emph{However, we cannot use alphabetic constants in arithmetic
expressions.}
