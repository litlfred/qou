---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-005-31-fusion-and-frobenius-peron-dimensions
section_title: "Fusion and Frobenius-Peron dimensions"
section_number: 3.1
pages: 7-8
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.613
latex_coverage_ratio: 0.991
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
\label{fusion_frobenius}

We recall the following from \cite{eno02-ofc}. In a fusion  category $\cat{C}$ over $\mathbb{C}$, every simple object $X_i$ has two canonical dimensions, which are positive real numbers: its {\em Frobenius-Perron} dimension $d^+_i$ and its {\em fusion} dimension $d_i$. 

\begin{defn}[see \cite{eno02-ofc}] The {\em Frobenius-Perron dimensions} $d^+_j$ of the simple objects $X_j$ are the unique positive real numbers satisfying
\begin{equation}
 d^+_j d^+_k = \sum_i N^i_{jk} d^+_i  \label{FPeqn}
\end{equation}
where $N^i_{jk} = \dim \Hom(X_i, X_j \otimes X_k)$. That is, they furnish the unique homomorphism from the Grothendieck ring of $\cat{C}$ to $\mathbb{C}$ taking positive real values on the simple objects $X_i$. 
\end{defn}
Note that, since taking duals is a ring anti-homomorphism from the Grothendieck ring of $\cat{C}$ to itself, it follows from uniqueness of the Frobenius-Perron dimensions that $d^+_j = d^+_{j^*}$ for all $j \in I$.

To define the fusion dimensions, we first need to define paired dimensions\footnote{The notion of a paired dimension is due to M\"{u}ger \cite[Prop 2.4]{m03-sct1}, where it is written as $d^2(X)$, but not named explicitly. The terminology and notation is our own.}.

\begin{defn} Let $X_i$ and $X_i^*$ be dual simple objects in $\cat{C}$. Their {\em paired dimension}   is
\begin{equation} \label{pair1}
  d_{\{i, i^*\}} = \ba \ig{e277.pdf} \ea,
 \end{equation}
where $(\eta, \epsilon)$ is some choice of unit and counit maps exhibiting $X_i^*$ as a right dual of $X_i$, and $(n, e)$ is some choice of unit and counit maps exhibiting $X_i^*$ as a {\em left} dual of $X_i$. 
\end{defn}
Observe that the product \eqref{pair1} is independent of the choices of unit and counit maps made in the definition because it is invariant under rescaling
 \[
 \eta \mapsto \lambda \eta, \epsilon \mapsto \frac{1}{\lambda} \epsilon, n \mapsto \mu n, e \mapsto \frac{1}{\mu} e.
\]
Note that the paired dimensions are certainly nonzero complex numbers. Indeed, $e \circ \eta$ is zero if
and only if one of $e$ or $\eta$ is zero
(by semisimplicity), which would contradict the duality equations \eqref{snake_eqns}.
Similarly for $\epsilon \circ n$. In Section \ref{piv_ind_sec} we will show how to compute the paired dimensions explicitly in terms of the associator matrix elements.

In fact, we will show in Theorem \ref{realpositive} that the paired dimensions are always positive real numbers. Anticipating this, we make the following definition.
\begin{defn}\label{fusion_dim}The {\em fusion dimension} $d_i$ of a simple object $X_i$ in a fusion category over $\mathbb{C}$ is the positive square root of its paired dimension $d_{\{i, i^*\}}$.
\end{defn}
In Corollary \ref{paired_cor}, we show how to read off the fusion dimensions directly from the associators.
\begin{example} In the Yang-Lee category, $d^+_\tau = \frac{1}{2}(1 + \sqrt{5})$ and we read off from \eqref{yl1} that $d_\tau = \frac{1}{2}(-1 + \sqrt{5})$. In category $\mathcal{E}$, $d^+_x = 1 + \sqrt{3}$ and $d^+_y = 1$, while we read off from \eqref{cate1} that $d_x = d^+_x$; similarly $d_y = d^+_y = 1$.
\end{example}
The {\em global dimension} $D_\cat{C}$ of a fusion category is the sum of its paired dimensions, $D_\cat{C} = \sum_{i \in I} d_{\{i, i^*\}}$. The {\em Frobenius-Perron dimension} $FP_\cat{C}$ of a fusion category is the sum of the squares of the Frobenius-Perron dimensions, $FP_\cat{C} = \sum_{i \in I} (d^+_i)^2$. The fusion category is called {\em pseudo-unitary} if $FP_\cat{C} = D_\cat{C}$. 


\subsection{The pairing convention} \label{pairing_sec}

\begin{defn} A {\em root choice} on a fusion category is a symmetric choice $\{d_i\}$ of square roots of the paired dimensions; that is, one which satisfies
 \[
  d_i^2 = d_{\{i,i^*\}} \text{ and } d_i = d_{i^*} \text{ for all $i \in I$.}
 \]
\end{defn}
The utility of a root choice is that it allows the following  diagrammatic convention.
\vskip 0.3cm
\framebox{\parbox[b]{11cm}{\textbf{Pairing convention.} Whenever a unit $\ba \ig{e284.pdf} \ea$ which is part of a unit-counit pair expressing a simple object $X_i^*$ as a {\em right} dual of $X_i$ appears together in some equation with a counit $\ba \ig{e287.pdf} \ea$ which is part of a unit-counit pair expressing $X_i^*$ as a {\em left} dual of $X_i$, it will always be understood that the former is arbitrary while the latter is determined uniquely by the requirement that
 \[
  \ba \ig{e288.pdf} \ea = d_i 
 \]
Similarly (and equivalently), whenever $\ba \ig{e285.pdf} \ea$ appears in a diagram together with $\ba \ig{e286.pdf} \ea$, the latter will always be fixed uniquely by the requirement that 
\[
\ba \ig{e289.pdf} \ea = d_i.
\]}}
\vskip 0.3cm
The pairing convention is the key diagrammatic idea in this paper. Using this convention, we only need to fix a root choice (and not a pivotal structure, which is not known to exist in general) on the fusion category in order to unambiguously perform string diagram calculations where both left and right duals appear. Note that the pairing convention extends uniquely to the whole category and not just the simple objects, see Section \ref{piv_monoidal}.

\begin{rem}
We will presently show in Theorem \ref{realpositive} that the paired dimensions $d_{\{i, i^*\}}$ are positive real numbers. From then on, we will always work with the {\em canonical} root choice on a fusion category given by the positive square roots.
\end{rem}

Although we will not need it in this paper, we can extend the pairing convention to {\em all} objects in $\cat{C}$, not just simple ones. Namely, suppose $V \in \cat{C}$. For each representative simple object $X_i$, choose a basis $e_{i, \alpha} : X_i \rightarrow V$ for $\Hom(X_i, V)$, with corresponding dual basis $\hat{e}_{i, \alpha} : V \rightarrow X_i$. If, in a diagram, a unit
\[
\ig{h14.pdf} 
\] 
which is part of a unit-counit pair $(\eta, \epsilon)$ expressing $V^*$ as a {\em right} dual of $V$ appears together with a counit
\[
\ig{h15.pdf}
\]
which is part of a unit-counit pair $(n, e)$ expressing $V^*$ as a {\em left} dual of $V$, it will be understood that the former is arbitrary while the latter is defined as
\[
\ba \ig{h15.pdf} \ea := \sum_{i, \alpha} \ba \ig{h16.pdf} \ea \, .
\]
Note that this definition is independent of the choice of basis $e_{i, \alpha}$.
