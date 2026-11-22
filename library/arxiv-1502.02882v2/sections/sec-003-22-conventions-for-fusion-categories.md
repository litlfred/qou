---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-003-22-conventions-for-fusion-categories
section_title: "Conventions for fusion categories"
section_number: 2.2
pages: 5-7
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.98
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
A fusion category is a rigid semisimple linear monoidal category with finitely many isomorphism classes of simple objects and whose unit object is simple \cite{e06-2vect}. In a fusion category, the associators feature explicitly in the graphical calculus as follows. Suppose we fix a representative set of simple objects $X_i$, $i \in I$, and choose trivalent bases
\begin{equation} \label{basis_choice}
 e_\alpha : X_i \rightarrow X_j \otimes X_k  \quad \text{ drawn as } \ig{d81.pdf}
 \end{equation}
for each hom-set $\Hom(X_i, X_j \otimes X_k)$. (We will always choose the canonical basis elements for the 1-dimensional hom-spaces $\Hom(1, 1 \otimes 1)$, $\Hom(X_i, 1 \otimes X_i)$ and $\Hom(X_i, X_i \otimes 1)$). Then we can form two different bases for $\Hom(X_i, X_j \otimes (X_k \otimes X_l))$ and so we have a change of basis transformation
\begin{equation} \label{associator_eqn}
\ig{d79.pdf} = \sum_{\gamma, n, \delta} (F^i_{jkl})^{\gamma n \delta}_{\alpha m \beta} \ig{d80.pdf} \, .
\end{equation}
Note that according to our diagram conventions, in the parenthesis scheme $X_j \otimes (X_k \otimes X_l)$ for the output objects, the left-hand side diagram of \eqref{associator_eqn} evaluates as
\[
X_i \stackrel{e_\alpha}{\longrightarrow} X_j \otimes X_m \stackrel{\id \otimes e_\beta}{\longrightarrow} X_j \otimes (X_k \otimes X_l )
\]
while the right-hand side diagram evaluates as
\[
X_i \stackrel{e_\gamma}{\longrightarrow} X_n \otimes X_l \stackrel{e_\delta \otimes \id}{\longrightarrow} (X_j \otimes X_k) \otimes X_l \stackrel{a_{X_j, X_k, X_l}}{\longrightarrow} X_j \otimes (X_k \otimes X_l) 
\]
where $a$ is the associator of the fusion category. We call the scalars $(F^i_{jkl})^{\gamma n \delta}_{\alpha m \beta}$ the {\em associator matrix elements}. 

Given a trivalent basis choice \eqref{basis_choice}, we define the {\em dual basis} $\hat{e}_\alpha : X_j \otimes X_k \rightarrow X_i$ as the one satisfying $\hat{e}_\beta \circ e_\alpha = \delta_{\alpha \beta} \id_{X_i}$. Graphically, this is drawn as:
\begin{equation} \label{dual_basis}
\left\{ \ig{d73.pdf} \right\} \text{ and } \left\{ \ig{d74.pdf} \right\} \text{ satisfying } \ig{d75.pdf} = \delta_{\alpha \beta} \ig{d76.pdf} \,.
\end{equation}
We will often write both $e^\alpha$ and $\hat{e}_\beta$ simply as $\alpha$ and $\hat{\beta}$ respectively; also we often write $i$ instead of $X_i$. Basis vectors satisfying \eqref{dual_basis} provide a resolution of the identity, 
\begin{equation} \label{res_id}
\sum_{i, \alpha} \ig{d77.pdf} = \ig{d78.pdf} \, .
\end{equation}

\begin{example} The Yang-Lee category (see eg. \cite{wang2010-topological}) has two simple objects $1$ (drawn as a dotted line) and $\tau$ (drawn as a solid line) with $\tau^2 = 1 + \tau$. So, the only nontrivial trivalent basis elements are
\[
 \ig{d82.pdf} \quad \text{and} \quad \ig{d83.pdf}.
\]
The associators are
\begin{align}
\ig{d84.pdf} & = a \ig{d86.pdf} + \ig{d87.pdf} \label{yl1}  \\
\ig{d85.pdf} & = a \ig{d86.pdf} - a \ig{d87.pdf}
\end{align}
and
\begin{equation} \label{yl2}
 \ig{d105.pdf} = \ig{d106.pdf}
\end{equation}
where $a = -\frac{1}{2} (1 + \sqrt{5})$. 
\end{example}
\begin{example} The category $\mathcal{E}$ associated with the even part of the $E_6$ subfactor \cite{hh09-snbfcor3, ostrik2013pivotal} has 3 simple objects: $1$ (drawn as a dotted line), $x$ (drawn as a solid line), $y$ (drawn as a wiggly line) and fusion rules $xy = yx =x$, $xx = 1 + 2x + y$, $yy=1$. So, the nontrivial trivalent basis elements are:
\[
\ig{d88.pdf}, \ig{d89.pdf}, \ig{d90.pdf}, \ig{d91.pdf} , \ig{d94.pdf}, \ig{d95.pdf} \, .
\]
Some relevant associators are
\begin{equation} \label{cate1}
\ig{d84.pdf} = \frac{1}{d} \left( \ig{d86.pdf} + \ig{d96.pdf} \right) + \frac{1}{\sqrt{2} v} \left( \ig{d97.pdf} + \ig{d98.pdf} + \ig{d99.pdf} - \ig{d100.pdf} \right) 
\end{equation}
and:
\begin{align}
\ig{d101.pdf} & = \frac{1}{\sqrt{2}} e^{\frac{-7 \pi i}{12}} \left( \ig{d102.pdf} + \ig{d103.pdf}  \right) \label{cate2} \\
\ig{d104.pdf} & = \frac{1}{\sqrt{2}} e^{\frac{-7 \pi i}{12}} \left( -i \ig{d102.pdf} + i \ig{d103.pdf} \right) \label{cate3}
\end{align}
Here $d = 1 + \sqrt{3}$ and $v = \sqrt{d}$. See \cite{hong2009onsymmetrization} for a full list. Note that we are using the inverses of the matrices in \cite{hong2009onsymmetrization} due to our conventions.
\end{example}
