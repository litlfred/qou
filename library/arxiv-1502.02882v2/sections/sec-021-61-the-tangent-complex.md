---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-021-61-the-tangent-complex
section_title: "The tangent complex"
section_number: 6.1
pages: 30-32
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.979
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
In this subsection we recall the definition of the Yetter-Davydov cohomology of a fusion category $\cat{C}$ \cite{yetter1998-braided, yetter2003-abelian, davydov1997-twisting}. Define the functor 
\[
T_n : \underbrace{\cat{C} \boxtimes \cdots \boxtimes \cat{C}}_{n \text{ times}} \rightarrow \cat{C}
\]
by $T_n(A_1, \ldots, A_n) = A_1 \otimes \cdots \otimes A_n$, parenthesized from left-to-right for definiteness, and define $C^n = \End(T_n)$, the vector space of natural endomorphisms of $T_n$. For $n=0$, set $C^0 = \mathbb{C}$. In terms of representative simple objects $X_i$, $i \in I$, we have
\[
C^n = \bigoplus_{i_1, \ldots, i_n} \Hom(X_1 \otimes \cdots \otimes X_n, \, X_1 \otimes \cdots \otimes X_n) \, .
\]
In string diagrams, we can write the components of $c \in C^n$ as
\[
\ig{d21.pdf} \, .
\]
For instance, a 1-cochain $c \in C^1$ is simply a collection of scalars $c_i \in \mathbb{C}$, $i \in I$. A 2-cochain $A \in C^2$ is a collection of morphisms $A_{ij} : X_i \otimes X_j \rightarrow X_i \otimes X_j$; this amounts to a collection of linear operators
\begin{equation} \label{2cocycle1}
A^i_{jk} : \Hom(X_k, X_i \otimes X_j) \rightarrow \Hom(X_k, X_i \otimes X_j) \, .
\end{equation}

\begin{defn} The {\em tangent complex} of a fusion category $\cat{C}$ is the sequence of $\mathbb{C}$-vector spaces and linear maps
\[
C^0 \stackrel{d^0}{\longrightarrow} C^1 \stackrel{d^1}{\longrightarrow} C^2 \stackrel{d^2}{\longrightarrow} C^3 \rightarrow \ldots, \qquad d^n = \sum_{k=0}^{n+1}(-1)^kf^n_k
\]
where the maps $f^n_k : C^n \rightarrow C^{n+1}$ are defined by
\[
\ig{d22.pdf} = \ig{d23.pdf}, \qquad \ig{d24.pdf} = \ig{d25.pdf} 
\]
\[
\ig{d26.pdf} = \sum_{k, \alpha} \ig{d27.pdf}
\]
(Note that for $c \in C^0 = \mathbb{C}$, $(f^0_0(c))_i = \id_{X_i} = (f^0_1(c))_i$ so that $d^0 = 0$.)
\end{defn}
\begin{lem} The tangent complex is a complex, i.e. $d^{n+1} d^n = 0$. 
\end{lem}
\begin{proof}
Follows from the identity 
\begin{equation} \label{chain_eqn}
f^{n+1}_k f^n_m = f^{n+1}_{m+1} f^n_k \quad 0 \leq k \leq m \leq n+1 \, . 
\end{equation}
For $k=m=0$ or $k=m=n+1$, \eqref{chain_eqn} is just the resolution of the identity \eqref{res_id}. For $k \neq m$, \eqref{chain_eqn} is just the interchange law in a monoidal category. In the other cases, \eqref{chain_eqn} takes the following form (we do the case $k=m=1$, $n=2$):
\begin{equation} \label{chain2}
\sum_{m, \alpha, p, \beta} \ig{d29.pdf} = \sum_{n, \delta, q, \gamma} \ig{d30.pdf}
\end{equation}
Pre-composing both sides of \eqref{chain2} with
\[
\ig{d31.pdf}
\]
and inserting the associator expansion \eqref{associator_eqn}, the left and right sides become the same expression, namely
\[
\sum_{m, \alpha, \beta} (F^s_{ijk})^{\beta m \alpha}_{\theta t \omega} \ig{d32.pdf} \, .
\]
\end{proof}
\begin{example} \label{2-cocycle-example}A 1-cocycle $c \in Z^1(C)$ is a collection of numbers $c_i$ such that $c_k = c_i + c_j$ whenever $X_k$ is a summand of $X_i \otimes X_j$. A 2-cocycle $A \in Z^2(C)$ is a collection of linear operators $A^i_{jk}$ as in \eqref{2cocycle1} such that 
\[
\ig{d33.pdf} - \ig{d34.pdf} + \sum_{\gamma, m, \delta} (F^s_{ijk})^{\gamma m \delta}_{\alpha t \beta} \left[ \ig{d35.pdf} - \ig{d36.pdf} \right] = 0.
\]
Expanded out fully, this is the equation
\begin{equation} \label{2cocycle2}
\sum_\alpha (A^t_{jk})_{\alpha \omega} F^{\gamma' m' \delta'}_{\theta t \alpha} - \sum_\beta (A^s_{it})_{\beta \theta} F^{\gamma' m' \delta'}_{\beta t \omega} + \sum_\gamma (A^s_{m' k})_{\gamma' \gamma} F^{\gamma m' \delta'}_{\theta t \omega} - \sum_\delta (A^m_{ij})_{\delta' \delta} F^{\gamma' m' \delta}_{\theta t \omega}
\end{equation}
for all values of the free indices, where $F\equiv F^s_{ijk}$.
\end{example}

\begin{defn} The {\em Yetter-Davydov} cohomology $H^i(\cat{C})$ of a fusion category $\cat{C}$ is the cohomology of its tangent complex.
\end{defn}
The low-dimensional cohomology groups have the following interpretations \cite{yetter1998-braided, yetter2003-abelian, davydov1997-twisting, k05-aes}. The group $H^1(\cat{C})$ classifies first-order deformations of $\Aut_\otimes (\id_{\cat{C}})$, $H^2(\cat{C})$ classifies first-order deformations of the tensor product functor, and $H^3(\cat{C})$ classifies first-order deformations of the associator.
