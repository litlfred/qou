---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-038-83-defining-new-number-systems
section_title: "Defining New Number Systems"
section_number: 8.3
pages: 33-34
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.988
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:define new number systems}

Based on Definition \ref{def:walnut_number_system}, to define a new
number system $\mathbf{S}$, we need to define automata for
$R_{\mathbf{S}}$, $+_{\mathbf{S}}$, and $<_{\mathbf{S}}$. We do not
need to define an automaton for $=_{\mathbf{S}}$, because it can be
generated easily, since we assumed that $w_1=_{\mathbf{S}} w_2$ if and
only if $w_1 = w_2$ for any two words $w_1$ and $w_2$ of the same
length. The automata for number systems must be defined in the
directory ``/Walnut/Custom Bases/''. For example, for the number system
$\mathbf{S}$, assuming it is $\MSD$, one needs to create msd\_S.txt,
msd\_S\_addition.txt, and msd\_S\_less\_than.txt for $R_{\mathbf{S}}$,
$+_{\mathbf{S}}$, and $<_{\mathbf{S}}$ respectively.  If $\mathbf{S}$
is $\LSD$, file names must be lsd\_S.txt, lsd\_S\_addition.txt, and
lsd\_S\_less\_than.txt respectively. The number system $\mathbf{S}$
defined in this way can be used in predicates by typing ?msd\_S or
?lsd\_S depending on whether $\mathbf{S}$ is $\MSD$ or $\LSD$. If the
automaton for $<_{\mathbf{S}}$ is not defined by the user, Walnut
assumes that $<_{\mathbf{S}}$ is the lexicographic ordering, i.e., if
$w_1$ and $w_2$ are of the same length, then $w_1 <_{\mathbf{S}} w_2$
if and only if $w_1$ comes before $w_2$ in lexicographic
order\footnote{Lexicographic ordering on symbols is assumed to be
$\cdots<-2<-1<0<1<2<\cdots$.}. If the automata for $R_{\mathbf{S}}$ is
not given, then $R_{\mathbf{S}}$ is assumed to be
$\Sigma_{\mathbf{S}}^*$. The alphabet $\Sigma_{\mathbf{S}}$ is inferred
from the automaton for $+_{\mathbf{S}}$ which is always given.

Note that reversing all automata for $\MSD[n]$ we get the corresponding
automata for $\LSD[n]$. The same goes with $\MSD[fib]$ and $\LSD[fib]$.
Thus for a number system $\MSD[S]$ if we only define files for
$\MSD[S]$, but then typing ?lsd\_S in a predicate, Walnut automatically
creates automata for $\LSD[S]$ by reversing those of $\MSD[S]$ and vice
versa. However the user should be cautious since there could very well
be number systems for which the difference between $\MSD$ and $\LSD$ is
more than the direction of the arrows in their corresponding automata.
