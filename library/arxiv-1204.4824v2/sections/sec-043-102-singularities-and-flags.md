---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-043-102-singularities-and-flags
section_title: "Singularities and flags"
section_number: 10.2
pages: 64-65
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.991
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:flags}

The twisted flat connection $({\hat E}, \nabla)$
produced by our nonabelianization construction carries a
bit of extra structure which will be important in what follows.
In this section we briefly describe it.

Let us consider
$({\hat E}, \nabla)$ in a neighborhood $\CU \subset \tilde C$ of one of the singular points
$\mathfrak{s}_n$.  On $\CU$ we can trivialize the covering $\tilde\Sigma \to \tilde C$ and hence
there is a decomposition into line bundles (cf. \eqref{eq:simple-pushforward}),
\begin{equation} \label{eq:e-simp-decomp}
E = \bigoplus_i \CL^{(i)},
\end{equation}
preserved by the connection $\pi_* \nabla^\ab$.
We do not generally have such a decomposition for
${\hat E}$, because the gluing transformations $\CT^{\alpha,\beta}_c$ mix the
different $\CL^{(i)}$.  Still, the $\CT^{\alpha,\beta}_c$ do preserve some structure, as follows.
Recall that the walls $p_c$ of $\wnet$ which end at $\fs_n$ carry labels $ij$ which
obey a constraint:  both $i$ and $j$ must belong to $o(\fs_n)$ and we must
have $i < j$.  Using \eqref{eq:tran-fn} it then follows that all the
$\CT^{\alpha,\beta}_c$ are ``upper triangular'':
for $i \notin o(\fs_n)$ they preserve $\CL^{(i)}$, and for $i \in o(\fs_n)$ they
preserve the subspace
\begin{equation}
 F^{(i)} = \bigoplus_{j \ge i} \CL^{(j)}.
\end{equation}
So we find that ${\hat E}$ decomposes
over $\CU$ as
\begin{equation} \label{eq:e-decomp}
{\hat E} = \left( \bigoplus_{i \notin o(\fs_n)} \CL^{(i)} \right) \oplus \hat E_{\fs_n}
\end{equation}
where each $\CL^{(i)}$ is $\nabla$-invariant, and
$\hat E_{\fs_n}$ has rank $\abs{o(\fs_n)}$ and
carries various $\nabla$-invariant subbundles $F^{(i)}$.  The ranks of these subbundles
and of their intersections are determined by the structure of the partial ordering in $o(\fs_n)$.

In the simplest case $o(\fs_n)$ is a totally ordered set containing all $K$ sheets.
In that case we may as well identify the labels with integers $1 \le i \le K$,
and write the ordering as $1 < 2 < \cdots < K$.  Then the
extra structure just discussed is simply a $\nabla$-invariant filtration of ${\hat E}$,
\begin{equation}
 0 = F^{(K)}  \subset F^{(K-1)} \subset F^{(K-2)} \subset \cdots \subset F^{(0)} = {\hat E},
\end{equation}
where $F^{(i)}$ has dimension $K-i$.  If the monodromy of $\nabla$ around $\fs_n$ is diagonalizable
with all eigenvalues distinct, then there exist $K!$ such invariant filtrations, and
our construction picks one out of those $K!$.

What we have found is that our construction naturally produces not just $({\hat E}, \nabla)$, but a bit of extra structure around each $\fs_n$, namely the decomposition \eqref{eq:e-decomp} and
the subbundles $F^{(i)}$.  We refer to this extra structure as \ti{flag data}.
