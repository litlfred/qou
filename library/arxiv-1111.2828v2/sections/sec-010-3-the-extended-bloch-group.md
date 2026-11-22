---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-010-3-the-extended-bloch-group
section_title: "The extended Bloch group"
section_number: 3
pages: 11-12
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.881
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sec.bloch}

We use the conventions of Zickert~\cite{ZickertAlgK}; the original 
reference is Neumann~\cite{Neumann}.

\begin{definition} 
\lbl{def.bloch}
The \emph{pre-Bloch group} $\Pre(\C)$ is the free abelian group on $\C\setminus\{0,1\}$ modulo the \emph{five term relation}
\begin{equation}
x-y+\frac{y}{x}-\frac{1-x^{-1}}{1-y^{-1}}+\frac{1-x}{1-y}=0,\quad \text{for }x\neq y\in\C\setminus\{0,1\}.
\end{equation}
The \emph{Bloch group} is the kernel of the map $\nu\colon \Pre(\C)\to\wedge^2(\C^*)$ taking $z$ to $z\wedge(1-z)$.
\end{definition}

\begin{definition} 
\lbl{def.ebloch}
The \emph{extended pre-Bloch group} $\widehat\Pre(\C)$ is the free abelian group on the set
\begin{equation}
\widehat\C=\left\{(e,f)\in\C^2 \bigm\vert \exp(e)+\exp(f)=1\right\}
\end{equation} 
modulo the \emph{lifted five term relation}
\begin{equation}
(e_0,f_0)-(e_1,f_1)+(e_2,f_2)-(e_3,f_3)+(e_4,f_4)=0
\end{equation}
if the equations
\begin{equation}
\begin{gathered}\lbl{fiveeq}
e_2=e_1-e_0,\quad e_3=e_1-e_0-f_1+f_0,\quad f_3=f_2-f_1\\
e_4=f_0-f_1,\quad f_4=f_2-f_1+e_0
\end{gathered}
\end{equation}
are satisfied. The \emph{extended Bloch group} is the kernel of the map $\widehat\nu\colon\widehat\Pre(\C)\to\wedge^2(\C)$ taking $(e,f)$ to $e\wedge f$.
\end{definition}

An element $(e,f)\in\widehat \C$ with $\exp(e)=z$ is called a \emph{flattening} with \emph{cross-ratio} $z$.
Letting $\mu_{\C}$ denote the roots of unity in $\C^*$, we have a
commutative diagram. 
\begin{equation}
\lbl{bigdiagram}
\cxymatrix{{&0\ar[d]&0\ar[d]&0\ar[d]&&\\0\ar[r]&\mu_{\C}\ar[r]^-{2\log}\ar[d]^-{\chi}&{\C/4\pi i\Z}\ar[r]\ar[d]^{\chi}&{\C^*/\mu_{\C}}\ar[r]\ar[d]&0\ar[d]&\\
0\ar[r]&{\widehat \B(\C)}\ar[r]\ar[d]^-\pi&{\widehat \Pre(\C)}\ar[r]^-{\widehat \nu}\ar[d]^-\pi&{\wedge^2(\C)}\ar[r]\ar[d]&
{K_2(\C)}\ar@2{-}[d]\ar[r]&0\\0\ar[r]&{\B(\C)}\ar[r]\ar[d]&{\Pre(\C)}\ar[r]^-\nu\ar[d]&{\wedge^2(\C^*)\ar[d]}\ar[r]&{K_2(\C)}\ar[r]\ar[d]&0\\&0&0&0&0}}
\end{equation}
The map $\pi$ is induced by the map taking a flattening to its cross-ratio, and $\chi$ is the map taking $e\in\C/4\pi i\Z$ to $(e,f+2\pi i)-(e,f)$, where $f\in\C$ is any element such that $(e,f)\in\widehat\C$.
