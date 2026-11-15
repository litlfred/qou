---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-018-71-negative-correlation-and-negative-association
section_title: "Negative correlation and negative association."
section_number: 7.1
pages: 19-20
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.971
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
Consider a probability distribution $\varphi$ on $\Omega$.
An \emph{event} $\E$ is any subset of $\Omega$.  The probability of the event
$\E$ is $\Pr[\E] = \sum_{S\in\E} \varphi(S)$.
An event $\E$ is \emph{increasing} if whenever $S\leq S'$ in $\Omega$
and $S\in\E$, then $S'\in\E$.  For example, if $K$ is any subset of 
$\Lambda$ and $\E_{K}$ is the event that all sites in $K$ are occupied, 
then $\E_{K}$ is an increasing event.  Notice that this event has the 
form $\E_{K}=\E' \times \{0,1\}^{\Lambda\drop K}$ for some event 
$\E'\subseteq\{0,1\}^{K}$.  Two events $\E$ and $\F$ are 
\emph{disjointly supported} when one can partition $\Lambda = A\cup 
B$ with $A\cap B=\none$ and $\E=\E' \times \{0,1\}^{B}$
and $\F=\{0,1\}^{A}\times\F'$ for some events 
$\E'\subseteq\{0,1\}^{A}$ and $\F'\subseteq\{0,1\}^{B}$.

A probability distribution on $\Omega$ is \emph{negatively associated}
(NA) when $\Pr[\E\cap\F]\leq \Pr[\E]\cdot\Pr[\F]$ for any two
increasing events that are disjointly supported.  It is 
\emph{negatively correlated} (NC) when $\Pr[\E_{\{i,j\}}]\leq
\Pr[\E_{\{i\}}]\cdot\Pr[\E_{\{j\}}]$  for any two distinct sites 
$\{i,j\}\subseteq \Lambda$.  Clearly NA implies NC.

It is useful to find conditions under which NC implies NA, since NC
is so much easier to check.  The following originates with Feder and 
Mihail, but many others have contributed their insights -- see Section
4.2 of \cite{BBL}.  The \emph{partition function} of any
$\varphi:\Omega\goesto\RR$ is the real multiaffine polynomial
$$
Z(\varphi)=Z(\varphi;\x) = \sum_{S\in\Omega} \varphi(S) \x^{S}
$$
in $\RR[\x]^{\ma}$.
If $\varphi$ is nonzero and nonnegative, then for any $\a\in\RR^{\Lambda}$
with $\a>\zero$, this defines a probability distribution
$\varphi^{\a}:\Omega\goesto[0,1]$  by setting $\varphi^{\a}(S) =
\varphi(S)\a^{S}/Z(\varphi;\a)$ for all $S\in\Omega$.\\

\noindent
\textbf{Feder-Mihail Theorem} (Theorem 4.8 of \cite{BBL})\textbf{.}\
\emph{
Let $\S$ be a class of nonzero nonnegative functions satisfying the following
conditions.\\
\textup{(i)}\  Each $\varphi\in\S$ has domain $\{0,1\}^{\Lambda}$
for some finite set $\Lambda=\Lambda(\varphi)$.\\
\textup{(ii)}\  For each $\varphi\in\S$, $Z(\varphi)$ is a homogeneous 
polynomial.\\
\textup{(iii)}\  For each $\varphi\in\S$ and $i\in\Lambda(\varphi)$,
$Z(\varphi)|_{x_{i}=0}$ and $\partial_{i}Z(\varphi)$ are partition
functions of members of $\S$.\\
\textup{(iv)}\  For each $\varphi\in\S$ and $\a\in\RR^{\Lambda(\varphi)}$
with $\a>\zero$, $\varphi^{\a}$ is NC.\\
Then for every $\varphi\in\S$ and $\a\in\RR^{\Lambda(\varphi)}$
with $\a>\zero$, $\varphi^{\a}$ is NA.}
