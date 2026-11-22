---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-014-23-the-presentation-in-the-kazhdan-lusztig-gener
section_title: "The presentation in the Kazhdan-Lusztig generators"
section_number: 2.3
pages: 15-16
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 0.812
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
\label{subsec-KLpresentation}


As the elements $H_s$ generate $\HB$, so too do the elements $\un{H}_s$. The corresponding relations are slightly more complicated:
\begin{equation} \un{H}_s^2 = \un{H}_s (v+v^{-1}), \label{rank1hecke} \end{equation}
\begin{equation} \ubr{\un{H}_s\un{H}_t\un{H}_s\ldots}{k+1} = \sum_d  c_{k,d} \un{H}_{\ubr{sts\ldots}{d+1}} \ \mathrm{ for }\ 1 \le k+1 \le m_{st}.  \label{rank2hecke} \end{equation}
The first relation corresponds to \eqref{rank1heckestd}.
The second relation expresses a product of generators in terms of the Kazhdan-Lusztig basis within a given dihedral group. The coefficients $c_{k,d}$ appearing are decomposition
numbers for $\mathfrak{sl}_2$ tensor products. If we let $V_i$ denote the $i+1$-dimensional irreducible of $\mathfrak{sl}_2$, then $V_1^{\ot k} \bigoplus \cong V_d^{\oplus c_{k,d}}$. Roughly
speaking, this is because the Temperley-Lieb algebra at a root of unity ``categorifies" the alternating product $\un{H}_s \un{H}_t \un{H}_s \ldots$ in the dihedral Hecke algebra. More details can be
found in \cite{EDihedral}.

Relation \eqref{rank2hecke} holds even when $m_{st}=\infty$, and for any $m$ can be viewed as a definition or explicit construction of each $\un{H}_w$. When $m=\infty$, this relation does not
impose any new algebraic relations on products of $\un{H}_s$ and $\un{H}_t$. When $m < \infty$, there is one new relation on products of $\un{H}_s$ and $\un{H}_t$ coming from the fact that $\un{H}_{\ubr{sts\ldots}{m}} = \un{H}_{\ubr{tst\ldots}{m}}$.

\begin{ex} \label{rank2heckeEx} The first few examples are: \[\begin{array}{lc} m_{st}=2: & \un{H}_s\un{H}_t=\un{H}_t\un{H}_s \\ m_{st}=3: & \un{H}_s\un{H}_t\un{H}_s-\un{H}_s=\un{H}_t\un{H}_s\un{H}_t-\un{H}_t\\ m_{st}=4: & \un{H}_s\un{H}_t\un{H}_s\un{H}_t-2\un{H}_s\un{H}_t = \un{H}_t\un{H}_s\un{H}_t\un{H}_s - 2 \un{H}_t \un{H}_s \\ m_{st}=5: & \un{H}_s\un{H}_t\un{H}_s\un{H}_t\un{H}_s - 3
\un{H}_s\un{H}_t\un{H}_s + \un{H}_s = \un{H}_t\un{H}_s\un{H}_t\un{H}_s\un{H}_t - 3 \un{H}_t \un{H}_s\un{H}_t + \un{H}_t. \end{array} \] \end{ex}
