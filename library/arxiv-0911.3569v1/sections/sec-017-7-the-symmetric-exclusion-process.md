---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-017-7-the-symmetric-exclusion-process
section_title: "The symmetric exclusion process."
section_number: 7
pages: 19-19
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
This section summarizes an application of stable polynomials to probability
and statistical mechanics from a 2009 paper of Borcea, Br\"and\'en and Liggett
\cite{BBL}.

Let $\Lambda$ be a set of \emph{sites}.  A symmetric exclusion process
(SEP) is a type of Markov chain with state space a subset of $\{0,1\}^\Lambda$.
In a state $S:\Lambda\goesto\{0,1\}$, the sites in
$S^{-1}(1)$ are \emph{occupied} and the sites in $S^{-1}(0)$ are \emph{vacant}.
This is meant to model a physical system of particles interacting by means of
hard-core exclusions.  Such models come in many varieties -- to avoid technicalities
we discuss only the case of a finite system $\Lambda$ and continuous time $t$.
(The results of this section extend to countable $\Lambda$ under a reasonable
finiteness condition on the interaction rates.)  Symmetry of the interactions turns 
out to be crucial, but particle number conservation is unimportant.

Let $E$ be a set of two-element subsets of $\Lambda$.  For each $\{i,j\}\in E$,
let $\lambda_{ij}>0$ be a positive real, and let $\tau_{ij}:\Lambda
\goesto\Lambda$ be the permutation that exchanges $i$ and $j$ and fixes all 
other sites.  Our SEP Markov chain $\MM$ proceeds as follows.
Each $\{i,j\}\in E$ has a Poisson process ``clock''
of rate $\lambda_{ij}$, and these are independent of one another.
With probability one, no two clocks ever ring at the same time.  When the clock
of $\{i,j\}$ rings, the current state $S$ is updated to the new state
$S\circ\tau_{ij}$.  In other words, when the $\{i,j\}$ clock rings,
if exactly one of the sites $\{i,j\}$ is occupied then a particle hops
from the occupied to the vacant of these two sites.

Let $\Lambda=[m]$ and $\Omega=\{0,1\}^\Lambda$,
let $\varphi_0$ be an initial probability distribution on $\Omega$,
and let $\varphi_t$ be the distribution of the state of $\MM$, starting
at $\varphi_0$, after evolving for time $t\geq 0$.  We are concerned with
properties of the distribution $\varphi_t$ that hold for all $t\geq 0$.
