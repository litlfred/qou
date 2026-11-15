---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem"
section_id: sec-004-14-motivation-for-exact-solutions
section_title: "Motivation for exact solutions"
section_number: 1.4
pages: 4-4
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.988
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem — Given a uniform random permutation π ∈Sn, let Zn,k be equal to the number of increasing"
---
In theoretical physics and in the mathematical physics of spin glasses, one is interested in the
precise form of the second moment and all higher moments, at least to leading order asymptotically
as $n \to \infty$.
Even though 
$\mathbf{E}[Z_{n,k}^2]/(\mathbf{E}[Z_{n,k}])^2$ may be too large to apply the 
Paley-Zygmund second moment method,
one may be interested in $\ln\left(\mathbf{E}[Z_{n,k}^2]\right)/\Big(2\ln\left(\mathbf{E}[Z_{n,k}]\right)\Big)$.
For example, in spin-glass theory, physicists moved from formulas for the moments
to predictions about the actual distribution.
In Appendix \ref{sec:SK}, we review this briefly.

An excellent reference for the limitations of classical mathematical tools when trying to apply
them to spin glass techniques was written by van Hemmen and Palmer \cite{vanHemmenPalmer}.
However, the spin glass techniques have proved effective in illuminating the Sherrington-Kirkpatrick
mean field spin glass problem, and may be useful beyond that.
See for example, the classical physics textbook \cite{MPV}.
The first rigorous proof of Parisi's 
ansatz for the SK model, given by Talagrand, seemed to proceed by very different techniques \cite{Talagrand},
with a starting point the beautiful approach of Guerra \cite{Guerra} and Guerra and Toninelli \cite{GuerraToninelli}.

In Appendix \ref{sec:SK} we give a rapid review of some points of that development.
Our purpose in the appendix is to demonstrate the role of calculating higher moments in the physicists' ``replica 
symmetry breaking'' approach.
In the present paper, we are interested in the higher moments of $Z_{n,k}$, starting with the second moment.
We call this the generalized Ulam problem.
Technically, the generalized Ulam problem should be the problem of stating as much as possible
about the distribution of $Z_{n,k}$ for the doubly-indexed sequence of numbers for $n$ and $k$.
But we are most hopeful to be able to calculate the positive integer moments, in some asymptotic sense.
See Section \ref{sec:Outlook} for a discussion of the relation between the 2nd moment and higher moments.

Another motivation involves Pinsky's second characterization of $A(N,k)$ in terms of the occupation
time of a $d=2$ dimensional simple random walk, where the set for the occupation time is the $y$-axis.


We discuss this more right after Remark \ref{rem:PinskySRW}.
P\'olya calculated the generating function for returns to the origin in the $d=2$ dimensional
simple random walk, in terms of the complete elliptic integral of the first kind.
The main result of our paper is related to that, in so much as it is a direct generalization.
But our formula is more complicated, so that it involves complete elliptic integrals of the third kind (which is 
the most general setting for complete elliptic integrals).
