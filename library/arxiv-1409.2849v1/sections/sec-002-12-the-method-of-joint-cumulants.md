---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-002-12-the-method-of-joint-cumulants
section_title: "The method of joint cumulants"
section_number: 1.2
pages: 5-7
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.955
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
\label{subsec:methjoint}
The appearance of an exponential of a monomial $Kx^{r \geq 3}$ as the limiting residue in mod-Gaussian convergence is a phenomenon that occurs not only for sums of i.i.d.~random variables, but more generally for sums of possibly non identically distributed and/or dependent random variables. For instance, \vspace{1mm}
\begin{enumerate}
\item the number of zeroes of a random Gaussian analytic function $\sum_{k=0}^\infty (\mathcal{N}_{\CC})_k\,z^k$ in the disk of radius $1-\frac{1}{n}$;\vspace{1mm}
\item the number of triangles in a random Erd\"os-R\'enyi graph $G(n,p)$;\vspace{1mm}
\end{enumerate}
are both mod-Gaussian convergent after proper rescaling, and with limiting function of the form $\exp(Lz^3)$, with the constant $L$ depending on the model (see again \cite{FMN13}). The reason behind these universal asymptotics lies in the following method of cumulants. If $X$ is a random variable with convergent Laplace transform $\esper[\E^{zX}]$ on a disk, we recall that its cumulant generating function is 
\begin{equation}
\log \esper[\E^{zX}]=\sum_{r \geq 1}\frac{\kappa^{(r)}(X)}{r!}\,z^r,\label{eq:cumulant}
\end{equation}
which is also well-defined and holomorphic on a disk around the origin. Its coefficients $\kappa^{(r)}(X)$ are the cumulants of the variable $X$, and they are homogenenous polynomials in the moments of $X$; for instance, $\kappa^{(1)}(X)=\esper[X]$, $\kappa^{(2)}(X)=\esper[X^2]-\esper[X]^2$, and $\kappa^{(3)}(X)=\esper[X^3]-3\,\esper[X^2]\,\esper[X]+2\,\esper[X]^3$. \bigskip

Consider now a sequence of random variables $(W_n)_{n \in \N}$ with $\kappa^{(1)}(W_n)=0$, and for $r \geq 2$, 
\begin{equation}\kappa^{(r)}(W_n) = K_r \,\alpha_n\,(1+o(1)),\label{asymptoticscumulant}
\end{equation}
with $\alpha_n \to +\infty$. This assumption is inspired by the case of a sum $W_n=\sum_{i=1}^n Y_i$ of centred i.i.d.~random variables for which $\kappa^{r}(W_n)=n\,\kappa^{(r)}(Y)$. If it is satisfied, then  one can formally write
\begin{align*}
\log &\,\esper\!\left[\E^{z\, \frac{W_n}{(\alpha_n)^{1/3}}}\right]\\
&= (\alpha_n)^{-2/3}\,\frac{\kappa^{(2)}(W_n)\,z^2}{2}+(\alpha_n)^{-1}\,\frac{\kappa^{(3)}(W_n)\,z^3}{6}+\sum_{r \geq 4}\frac{\kappa^{(r)}(W_n)}{r!} ((\alpha_n)^{-1/3} z)^r\\
&\simeq (\alpha_n)^{1/3}\,\frac{K_2\,z^2}{2}+\frac{K_3\,z^3}{6}+\sum_{r \geq 4}\frac{K_r\,z^r}{r!} (\alpha_n)^{1-r/3}\\
&\simeq (\alpha_n)^{1/3}\,\frac{K_2\,z^2}{2}+\frac{K_3\,z^3}{6}
\end{align*}
whence the mod-Gaussian convergence of $X_n=(\alpha_n)^{-1/3}\,W_n$, with parameters $t_n=K_2\,(\alpha_n)^{1/3}$ and limiting function $\exp(K_3 \,z^3/6)$. The approximation is valid if the $o(1)$ in the asymptotics of $\kappa^{(2)}(W_n)$ is small enough (namely $o((\alpha_n)^{-1/3})$), and if the series $\sum_{r \geq 4}$ can be controlled, which is the case if
\begin{equation}\forall r,\,\, |\kappa^{(r)}(W_n)|\leq (Cr)^r\,\alpha_n\label{eq:boundcumulant}
\end{equation}
for some constant $C$. The method of cumulants in the setting of mod-Gaussian convergence amounts to prove \eqref{asymptoticscumulant} for the first cumulants of the sequence $(X_n)_{n \in \N}$, and \eqref{eq:boundcumulant} for all the other cumulants. From such estimates one then obtains mod-Gaussian convergence for an appropriate renormalisation of $(W_n)_{r \geq 3}$, with limiting function $\exp(K_r\,z^r/r!)$, where $r$ is the smallest integer greater or equal than $3$ such that $K_r \neq 0$.\bigskip

This method of cumulants works well with sequences $(W_n)_{n \in \N}$ that write as sums of (weakly) dependent random variables. Indeed, cumulants admit the following generalization to families of random variables, see \cite{LS59}. Denote $\qym_r$ the set of partitions of $\lle 1,r\rre = \{1,2,3,\ldots,r\}$, and $\mu$ the M\"obius function of this poset (see \cite{Rot64} for basic facts about M\"obius functions of posets): 
$$\mu(\Pi)=(-1)^{\ell(\Pi)-1}\,(\ell(\Pi)-1)!$$
where $\ell(\Pi)=s$ if $\Pi=\pi_1 \sqcup \pi_2 \sqcup \cdots \sqcup \pi_s$ has $s$ parts. The joint cumulant of a family of $r$ random variables with well defined moments of all order is
$$\kappa(X_1,\ldots,X_r)=\sum_{\Pi \in \qym_r} \mu(\Pi)\,\prod_{i=1}^{\ell(\Pi)}\esper\!\left[\prod_{j \in \pi_i} X_j\right].$$
It is multilinear and generalizes Equation \eqref{eq:cumulant}, since
\begin{align*}
\kappa(X_1,\ldots,X_r)&=\left.\frac{\partial^r}{\partial z_1 \partial z_2 \cdots \partial z_r}\right|_{z_1=\cdots=z_r=0}\big(\log \esper[\E^{z_1X_1+\cdots+z_rX_r}]\big)\\
\kappa\big(\underbrace{X,\ldots,X}_{r\text{ times}}\big)&=\kappa^{(r)}(X).
\end{align*}
Suppose now that $W_n=W=\sum_{i=1}^n Y_i$ is a sum of dependent random variables. By multilinearity,
\begin{equation}\kappa^{(r)}(W)=\sum_{i_1,\ldots,i_r} \kappa(Y_{i_1},\ldots,Y_{i_r}),\label{eq:multilinearity}
\end{equation}
so in order to obtain the bound \eqref{eq:boundcumulant}, it suffices to bound each "elementary" joint cumulant $\kappa(Y_{i_1},\ldots,Y_{i_r})$. To this purpose, it is convenient to introduce the dependency graph of the family of random variables $(Y_{1},\ldots,Y_{n})$, which is the smallest subgraph $G$ of the complete graph on $n$ vertices such that the following property holds: if $(Y_i)_{i \in I}$ and $(Y_j)_{j \in J}$ are disjoint subsets of random variables with no edge of $G$ between a variable $Y_i$ and a variable $Y_j$, then $(Y_i)_{i \in I}$ and $(Y_j)_{j \in J}$ are independent. Then, in many situations, one can write a bound on the elementary cumulant $\kappa(Y_{i_1},\ldots,Y_{i_r})$ that only depends on the induced subgraph $G[i_1,\ldots,i_r]$ obtained from the dependency graph by keeping only the vertices $i_1,\ldots,i_r$ and the edges between them. In particular:\vspace{2mm}
\begin{enumerate}
\item $\kappa(Y_{i_1},\ldots,Y_{i_r})=0$ if the induced graph $G[i_1,\ldots,i_r]$  is not connected.
 \vspace{2mm}
\item if $|Y_i| \leq 1$ for all $i$, then $|\kappa(Y_{i_1},\ldots,Y_{i_r})| \leq 2^{r-1}\,\mathrm{ST}(G[i_1,\ldots,i_r])$, where $\mathrm{ST}(H)$ is the number of spanning trees on a (connected) graph $H$. \vspace{1mm}
\end{enumerate}
By gathering the contributions to the sum of Formula \eqref{eq:multilinearity} according to the nature and position of the induced subgraph $G[i_1,\ldots,i_r]$ in $G$, one is able to prove efficient bounds on cumulants of sums of dependent variables, and to apply the method of cumulants to get their mod-Gaussian convergence. We refer to \cite{FMN13} for precise statements, in particular in the case where each vertex in $G$ has less than $D$ neighbors, with $D$ independent of the vertex and of $n$. In Section \ref{sec:cumulantspin}, we shall apply this method to a case where $G$ is the complete graph on $n$ vertices, but where one can still find correct bounds (and in fact exact formulas) for the joint cumulants $\kappa(Y_{i_1},\ldots,Y_{i_r})$: the one-dimensional Ising model.
\medskip
