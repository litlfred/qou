---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume"
section_id: sec-008-31-the-schreier-normal-form-for-3-braids-and-vol
section_title: "The Schreier normal form for 3-braids and volume"
section_number: 3.1
pages: 12-13
source_pdf: 1406.7337v4.pdf
source_sha256: 5bae8237742733b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 1.0
doc_brief: "Semi-Adequate Closed Braids and Volume — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and below in terms of the twist number, the number of"
---
\label{normformsec}



A useful development in the history of 3-braids was the solution to the Conjugacy Problem (\cite{Schreier}). During this time, an algorithm was developed that produces from an arbitrary 3-braid word $\beta$ a conjugate 3-braid word $\beta'$, called the \emph{Schreier normal form}, which is the unique representative of the conjugacy class of $\beta$. A version of this algorithm is presented below. 









\bigskip

\noindent \textbf{Schreier Normal Form Algorithm:} 

\begin{itemize}
\item[(1)] Let $\beta \in B_{3}=\langle \sigma_{1}, \sigma_{2}\ \vert\ \sigma_{1}\sigma_{2}\sigma_{1}=\sigma_{2}\sigma_{1}\sigma_{2}\rangle$ be cyclically reduced into syllables. Introduce new variables $x=\left(\sigma_{1}\sigma_{2}\sigma_{1}\right)^{-1}$ and $y=\sigma_{1}\sigma_{2}$. Thus we have that $\sigma_{1}=y^2x$, $\sigma_{2}=xy^2$, $\sigma_{1}^{-1}=xy$, and $\sigma_{2}^{-1}=yx$. Possibly using cyclic permutation, rewrite $\beta$ as a cyclically reduced word (that is positive) in $x$ and $y$. 
\item[(2)] Introduce $C=x^{-2}=y^{3} \in Z(B_{3}),$ where $Z(B_{3})$ denotes the center of the 3-braid group $B_{3}$. By using these relations and the commutativity of $C$ as much as possible, group all powers of $C$ at the beginning of the braid word and reduce the exponents of $x$ and $y$ as much as possible. Rewrite $\beta$ as $\beta=C^{j}\eta$, where $j \in \mathbb{Z}$ and where
$$\eta = \left\{
\begin{array}{ll} 
\left(xy\right)^{p_{1}}\left(xy^2\right)^{q_{1}}\cdots \left(xy\right)^{p_{s}}\left(xy^2\right)^{q_{s}} & \mathrm{for\ some}\ s, p_{i}, q_{i} \geq 1 \\
\left(xy\right)^{p} & \mathrm{for\ some}\ p \geq 1 \\
\left(xy^{2}\right)^{q} & \mathrm{for\ some}\ q \geq 1 \\
y & \ \\
y^2 & \ \\
x & \ \\
1 & \ \\
\end{array}  \right.
$$
\item[(3)] Possibly using cyclic permutation and the commutativity of $C$, rewrite $\beta$ back in terms of $\sigma_{1}$ and $\sigma_{2}$ as $\beta'=C^{k}\eta'$, where $k \in \mathbb{Z}$ and where
$$ \eta' = \left\{
\begin{array}{ll} 
\sigma_{1}^{-p_{1}}\sigma_{2}^{q_{1}}\cdots \sigma_{1}^{-p_{s}}\sigma_{2}^{q_{s}} & \mathrm{for\ some}\ s, p_{i}, q_{i} \geq 1 \\
\sigma_{1}^{p} & \mathrm{for\ some}\ p\in \mathbb{Z} \\
\sigma_{1}\sigma_{2} & \ \\
\sigma_{1}\sigma_{2}\sigma_{1} & \ \\
\sigma_{1}\sigma_{2}\sigma_{1}\sigma_{2} & \ 
\end{array}  \right.
$$
\end{itemize}

\begin{definition} We call $\beta'=C^{k}\eta' \in B_{3}$ the \emph{Schreier normal form} of $\beta \in B_{3}$. The braid word $\beta'$ is the unique representative of the conjugacy class of $\beta$. Following \cite{Cusp}, we will call a braid $\beta$ \emph{generic} if it has Schreier normal form 
$$\beta'=C^{k}\sigma_{1}^{-p_{1}}\sigma_{2}^{q_{1}}\cdots \sigma_{1}^{-p_{s}}\sigma_{2}^{q_{s}}.$$ 
\end{definition}

Using the Schreier normal form of a 3-braid, Futer, Kalfagianni, and Purcell (\cite{Cusp}) classified the hyperbolic 3-braid closures. Furthermore, given such a hyperbolic closed 3-braid, they gave two-sided bounds on the volume of the link complement, expressing the volume in terms of the parameter $s$ from the Schreier normal form of the 3-braid. By using the more recent machinery built by the same authors in \cite{Guts}, we aim to obtain a sharper lower bound on volume. To begin our study, we first recall two propositions from \cite{Cusp}. 

\begin{proposition}[\cite{Cusp}, Theorem 5.5] Let $D(K)=\widehat{\beta}$ denote the closure of a 3-braid $\beta \in B_{3}$. Then $K$ is hyperbolic if and only if 
\begin{itemize}
\item[(1)] $\beta$ is generic, and 
\item[(2)] $\beta$ is not conjugate to $\sigma_{1}^p\sigma_{2}^q$ for any integers $p$ and $q$. 
\end{itemize}
\label{hypgeneric}
\end{proposition}

\begin{proposition}[\cite{Cusp}, Theorem 5.6]\label{svolbound}
Let $D(K)=\widehat{\beta}$ denote the closure of a 3-braid $\beta \in B_{3}$. Then, assuming that $K$ is hyperbolic, we have that
$$4v_{3}\cdot s-276.6 < \mathrm{vol}(S^3 \backslash K) < 4v_{8}\cdot s.$$ 
\end{proposition}
