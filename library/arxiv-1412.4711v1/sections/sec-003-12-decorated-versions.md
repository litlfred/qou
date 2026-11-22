---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-003-12-decorated-versions
section_title: "Decorated versions"
section_number: 1.2
pages: 4-5
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.99
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
From now on, we assume $G=\PGL(n,\bC)$. A key point to study the previous defined spaces is to add a geometric structure on it, as usual in the study of moduli spaces. 
Such a structure is called a \emph{decoration} and will be most easily defined with additional assumption: from now on $\Gamma$ is the fundamental group of a $1$-cusped hyperbolic $3$-variety $M$ (as the figure eight knot complement)\footnote{This assumption is not necessary and one may work with a triangulated $3$-variety (either hyperbolic with more cusps, or with boundary, or even not hyperbolic). We refer to \cite{BFG} for this setting.}. As $M=\mathbb H^3/\Gamma$ is a cusped hyperbolic manifold, we let
 $\mathcal P\subset \mathbb{CP}^1=\partial \mathbb H^3$ be the set of cusps in the boundary of the hyperbolic space. By construction, $\Gamma$ acts on $\mathcal P$.
Let moreover $\mathcal Fl$ be the space of complete flags of $\mathbb{CP}^n$. There is a natural action of $\PGL(n,\bC)$, for which $\mathcal Fl$ becomes the quotient of $\PGL(n,\bC)$ by the subgroup of upper-triangular matrices. Hence, given a representation $\rho$ of $\Gamma$ in $\PGL(n,\bC)$, we have an action of $\Gamma$ on $\mathcal Fl$, through $\rho$.  For these objects and the following, we refer to \cite{BFG}.

\newcommand{\DecHom}{\mathrm{DecHom}}

\begin{defn}
Let $\rho \in \Hom(\Gamma,G)$. Then $\Gamma$ acts both on $\mathbb{CP}^1$ and $\mathcal Fl$. A \emph{decoration} of $\rho$ is a $\Gamma$-covariant map :
$$\phi : \mathcal P\to \mathcal Fl.$$
Let $\DecHom(\Gamma,G)$ be the decorated representations variety:
$$\DecHom(\Gamma,G)=\{(\rho,\phi)|\; \rho\in \Hom(\Gamma,G), \; \phi\textrm{ is a decoration of }\rho\}.$$ 
\end{defn}

As the group $G=\PGL(n,\bC)$ acts on $\mathcal Fl$, it acts on the space of maps $\mathcal P\to \mathcal Fl.$
Moreover, it is easily checked that if $\phi$ is a decoration of $\rho$, then $g\cdot \phi$ is a decoration of the conjugated $g\cdot \rho=g\rho g^{-1} $. 
Hence $G$ acts on the space $\DecHom(\Gamma,G)$. 

\newcommand{\DecMon}{\mathrm{DecMon}}

\begin{defn}
We define the \emph{decorated monodromy varieties} $\DecMon(\Gamma,G)$ as the naive quotient:
$$\DecMon(\Gamma,G)=\DecHom(\Gamma,G)/G.$$
\end{defn}


We now proceed by defining a decorated version of the character variety. 
First of all, note that the space of flags $\mathcal Fl$ is an algebraic variety and the action of $G$ is algebraic. 
Moreover, $\DecHom(\Gamma,G)$ is an algebraic variety: indeed, choose a \emph{finite} fundamental set $\{p_1,\ldots,p_r\}$ for the action of $\Gamma$ on $\mathcal P$. 
Then a decorated representation $(\rho,\phi)$ is uniquely determined by a choice of a flag $F_i$ for each $p_i$ such that $F_i$ is stabilized by $\mathrm{Stab}_\Gamma(p_i)$.

\newcommand{\DecX}{\mathrm{Dec}X}

We now consider the algebraic quotient of $\DecHom(\Gamma,G)$ under this action:
\begin{defn}
We define the \emph{decorated character variety} $\DecX(\Gamma,G)$ as the algebraic quotient:
$$\DecX(\Gamma,G)=\DecHom(\Gamma,G)//G.$$
\end{defn}
