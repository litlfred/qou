---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-025-61-technical-preliminaries
section_title: "Technical preliminaries"
section_number: 6.1
pages: 45-46
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.903
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
In this section, we make the following assumptions:\vspace{2mm}
\begin{enumerate}
\item The random variables $X_{n}$ satisfy the hypotheses of Definition \ref{def:modphi} with $c=+\infty$ (in particular, $\psi$ is entire on $\C$). \vspace{2mm}
\item The Legendre-Fenchel transform $F$ is essentially smooth, that is to say that it takes finite values on a non-empty closed interval $I_{F}$ and that $\lim F'(x)=\lim h = \pm \infty$ when $x$ goes to a bound of the interval $I_{F}$ (\emph{cf.} \cite[Definition 2.3.5]{DZ98}). \vspace{2mm}
\end{enumerate}
The latter point is verified if $\phi$ is a Gaussian or Poisson law, which are the most important examples.
\begin{lemma}
Let $C$ be a closed subset of $\R$. Either $\inf_{u \in C}F(u)=+\infty$, or $\inf_{u \in C}F(u)=m$ is attained and $\{x \in C \,\,|\,\,F(x)=\min_{u \in C}F(u)\}$ consists of one or two real numbers $a \leq b$, with $a < \eta'(0) < b$ if $a \neq b$.
\end{lemma}
\begin{center}
\begin{figure}[ht]
\includegraphics{minimum.pdf}
\vspace{-5mm}
\caption{The infimum of $F$ on an admissible closed set $C$ is attained either at $a=\sup (C \cap (-\infty,\eta'(0)])$, or at $b=\inf( C \cap [\eta'(0),+\infty))$, or at both if $F(a)=F(b)$.}
\end{figure}
\end{center}
\begin{proof}
Recall that $F$ is strictly convex, since its second derivative is $1/\eta''(h)$, which is the inverse of the variance of a non-constant random variable. Also, $\eta'(0)$ is the point where $F$ attains its global minimum, and it is the expectation of the law $\phi$. If $C \cap I_{F}=\emptyset$, then $F_{|C}=+\infty$ and we are in the first situation. Otherwise, $F_{|C}$ is finite at some points, so there exists $M \in \R_{+}$ such that $C \cap \{x \in \R \,\,|\,\,F(x) \leq M\} \neq \emptyset$. However, the set $ \{x \in \R \,\,|\,\,F(x) \leq M\}$ is compact by the hypothesis of essential smoothness: it is closed as the reciprocal image of an interval $]-\infty,M]$ by a lower semi-continuous function, and bounded since $\lim_{x \to (I_{F})^{\mathrm{c}}} |F'(x)|=+\infty$. So, $C \cap \{x \in \R \,\,|\,\,F(x) \leq M\}$ is a non-empty compact set, and the lower semi-continuous $F$ attains its minimum on it, which is also $\min_{u\in C}F(u)$. Then, if $a \leq b$ are two points in $C$ such that $F(a)=F(b)=\min_{u \in C}F(u)$, then by strict convexity of $F$, $F(x)<F(a)$ for all $x \in (a,b)$, hence, $(a,b) \subset C^{\mathrm{c}}$. Also, $F(x)>F(a)$ if $a \neq b$ and $x \notin [a,b]$, so either $a=b$, or $\eta'(0) \in (a,b)$.
\end{proof}\bigskip

We take the usual notations $B^{\mathrm{o}}$ and $\overline{B}$ for the interior and the closure of a subset $B \subset \R$. Call \emph{admissible} a (Borelian) subset $B \subset \R$ such that there exists $b \in B$ with
$F(b) < +\infty$, and denote then 
$$F(B)=\inf_{u \in B}F(u)=\min_{u \in \overline{B}}F(u),$$
and $B_{\min}= \{a \in \overline{B}\,\,|\,\,F(a)=F(B)\}$; according to the previous discussion, $B_{\min}$ consists of one or two elements.
