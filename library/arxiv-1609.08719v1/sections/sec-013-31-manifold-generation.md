---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-013-31-manifold-generation
section_title: "Manifold generation"
section_number: 3.1
pages: 10-11
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.788
latex_coverage_ratio: 0.978
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
The code we used to collect manifold information can be found at
\url{https://github.com/s-gilles/maps-reu-code}. We considered all
orientable, cusped, hyperbolic manifolds which can be triangulated
using 9 tetrahedra or less (the \codebit{OrientableCuspedCensus} within
\prog{SnapPy} at the time of work), as well as all link complements
using 3 crossings or more (a subset of \codebit{LinkExteriors}). We
also considered additional manifolds in the \codebit{LinkExteriors}
and \codebit{HTLinkExteriors} collections.

Of these manifolds, we performed Dehn surgery of type $(p,q)$ over
each of the $n$ cusps, with $p \in [0, L(n)]$ and
$q \in [-L(n), L(n)]$, (and $(p,q) = 1$) where $L(n)$ is given by
figure~\ref{fig:ln}.

\begin{figure}[h]
  \begin{tabular}{|l|cccccccc|} \hline $L(n)$ & $16$ & $12$ & $8$ &
    $6$ & $4$ & $3$ & $3$ & $2$ \\ \hline $n $ & $ 1$ & $ 2$ & $3$ &
    $4$ & $5$ & $6$ & $7$ & $ \ge 8$ \\ \hline
  \end{tabular}
  \caption{$L(n)$}
  \label{fig:ln}
\end{figure}

Of the resulting manifolds, we discarded those whose invariant trace
field resulted in a polynomial with degree $9$ or more (or if
\prog{SnapPy} or \prog{Snap} were unable to triangulate the
result). For each remaining manifold, we we stored intermediate
information about the manifold.  The resulting file, available at
\url{http://www.curve.unhyperbolic.org/linComb/finalized_data/volumes/all_volumes.csv},
contains over 790,000 manifolds, representing over 6,300 distinct
invariant trace fields, with volumes accurate to at least 50 decimal
places. The work was performed on the University of Maryland's
computation cluster.


\subsection{Lattice matching}

With the data stored in \codebit{all\_volumes.csv}, we have enough
data to conjecture partial lattice generators for 5,900 invariant
trace fields. Of those, for 312 invariant trace fields we have
enough data to conjecture not only generating volumes for the full
lattice, but also representative manifolds associated to the invariant
trace field which exhibit those volumes. This data can be found at
\url{http://www.curve.unhyperbolic.org/linComb/finalized_data/volume_spans.csv},
and the code we used for conjecturing lattice generators is available
at \url{https://github.com/s-gilles/maps-reu-code}, an implementation
of algorithm~\ref{alg:lattice-match}.

Sample data can be found in section~\ref{sec:lattice-examples}.
