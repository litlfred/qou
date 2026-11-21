---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-012-26-categorical-aspects
section_title: "Categorical aspects"
section_number: 2.6
pages: 23-24
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.86
latex_coverage_ratio: 0.956
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sub.cat}

In this section we briefly recall some categorical aspects of modules over
the $q$-Weyl algebra and give a proof of Lemma~\ref{lem.cat}.

To begin with, a gauge transformation $X=P^{-1}Y$ changes~\eqref{qdiff} to
$\s Y = B Y$ where $B=\s P A P^{-1}$, changes a fundamental solution $U$ of
~\eqref{qdiff} to $P^{-1}U$, and consequently changes $\Om_\gamma$ to
$(P|_{\kappa}\gamma)^{-1} \Om P$. Hence, if $P \in \GL_r(\BQ(t,q))$, then modularity
is a property of the gauge equivalence class of a linear $q$-difference equation,
i.e., a property of a $q$-holonomic module, independent of a choice of a cyclic
vector. This concludes part (a) of Lemma~\ref{lem.cat}.

For part (b), we use the convariant function
$M \mapsto \Sol(M):=\Ker(\s, \calF \otimes_{\BQ(t,q)} M)$ where $\calF$ denotes a
universal $q$-difference field; see for
example~\cite[Sec.2.2]{Singer:galois-differential} for the case of modules over the
Weyl algebra and~\cite{Hardouin} for its extension for the $q$-Weyl algebra $\calW$.
This functor by definition satisfies~\cite[Lem.2.16]{Singer:galois-differential}
\be
\Sol(M) \cong \{y \in \calF^r \,\, | \,\, \s y=A y\}
\ee
where $A$ is the matrix obtained by a choice of a cyclic vector of $M$. Moreover,
if
$$
0 \to M' \to M \to M'' \to 0
$$
is a short exact sequence of finitely generated $\calW$-modules, then
\be
\label{solexact}
0 \to \Sol(M') \to \Sol(M) \to \Sol(M'') \to 0
\ee
is a short exact sequence of vector spaces over $\BQ(t,q)$;
see~\cite[Sec.2.2]{Singer:galois-differential}. In addition, $M$ has a canonical
filtration at $t=0$ (and also at $t=\infty$) independent of the choice of cyclic
vector~\cite{Sauloy:filtration} compatible with submodules and quotient modules.
Converting the above into matrices, it follows that the filtration preserving
fundamental matrices $U$, $U'$ and $U''$ of $M$, $M'$ and $M''$ (and likewise,
$V$, $V'$ and $V''$) and their corresponding cocycles are related by
\be
U = \begin{pmatrix} U' & * \\ 0 & U'' \end{pmatrix}, \qquad
\Om_U = \begin{pmatrix} \Om_{U'} & * \\ 0 & \Om_{U''} \end{pmatrix} \,.
\ee
It follows that if $\Om_U$ extends to the cut plane, so does $\Om_{U'}$
and $\Om_{U''}$, concluding part (b). It is unlikely that the converse to
part (b) holds, namely if extensions of modular $q$-holonomic modules are
$q$-holonomic, but not necessarily modular.

For part (c), observe that if $U$ is a fundamental matrix for $M$, then
$U^\wedge(t,q):=U(t,q^{-1})$ and $U^\vee=(U^{-1})^t$ are fundamental matrices for
$M^\wedge$ and $M^\vee$. It follows that if $\Om$ is a cocycle of $M$ then
$\Om^\wedge(z,\tau):=\Om(z,-\tau)$ and $\Om^\vee=(\Om^{-1})^t$ are cocycles for
$M^\wedge$ and $M^\vee$. Part (c) follows. This concludes the proof of
Lemma~\ref{lem.cat}.  
\qed
