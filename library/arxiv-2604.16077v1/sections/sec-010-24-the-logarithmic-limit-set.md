---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-010-24-the-logarithmic-limit-set
section_title: "The logarithmic limit set"
section_number: 2.4
pages: 18-20
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.936
---
\label{ASYWEIGHTS} Recall the spaces $G_{hyp,N}(T,b)$ and ${}_NX_{hyp}(M)$, where $N\geq 3$ is odd (see Section \ref{GhypN}); we saw that when $M=S^3\setminus 4_1$ these spaces are respectively the solution set of the equations \eqref{eqGN}, and (up to birational isomorphism) the plane curve whose points are  pairs $(\kappa_\bw(\mu_K),\kappa_\bw(\lambda_K))$ as in \eqref{compbord}. Here we introduce a ``limit'' of the tower of spaces $\{G_{hyp,N}(T,b)\}_N$, that will be used in Section \ref{sec:class_int}. It is related in a natural way (via holonomy maps) to a tropical curve associated to the tower of curves $\{{}_NX_{hyp}(M)\}_N$, and to the $PSL(2,\mc)$ $A$-polynomial of $M$ (see Remark \ref{tropremk}). 

We use the notations of the previous section. As we are going to let $N$ vary and consider corresponding sequences of points in the spaces $G_{hyp,N}(T,b)$, we reintroduce the dependence in $N$ in the notations; thus the points of $G_{hyp,N}(T,b)$ are the tuples $(\bu_{0,N},\bu_{1,N},\bv_{0,N},\bv_{1,N})$ satisfying \eqref{eqGN}. Also for ${\bf x}\in \{\bu,\bv\}$ and $k\in\{0,1,2\}$, setting $u_{k,N} := \bu_{k,N}^N$ we get tuples $(u_{0,N},u_{1,N},v_{0,N},v_{1,N})$ in $G_{hyp}(T,b)$, possibly varying with $N$. As in \eqref{ecoldef} we write
\begin{equation}\label{defseqNcolor}\bl_{k,N}^\bu := \frac{1}{N}\left(\Log(u_{k,N})+2\pi i a_{k,N}' \right),\  \bl_{k,N}^\bv := \frac{1}{N}\left(\Log(v_{k,N})+2\pi i b_{k,N}' \right).
\end{equation}
Therefore $a_{k,N}',b_{k,N}'\in \mz/N$ are $N$-colors, and $\bx_{k,N} = \exp(\bl_{k,N}^\bx)$. Put
\begin{equation}\label{deflimlkmars26}
\bl_{k,\infty}^{\bf x} := \lim_{N\rightarrow \infty} \bl_{k,N}^{\bf x}  \in \mc/2\pi i \mz
\end{equation}
assuming the limit exists. In this case, by the relations \eqref{compbord} the sequence $(\kappa_N)_N$ converges in $H^1(\partial \bar M; \mc^*) \cong (\mc^*)^2$. Then we put
$$\kappa_\infty := \lim_{N\rightarrow \infty}\kappa_N  \in H^1(\partial \bar M; \mc^*).$$
Consider the embedding
$$\Theta_N := {\rm Log}\vert \Theta_N\vert \times \mathcal{A}(\Theta_N)\colon G_{hyp,N}(T,b)\rightarrow \mathbb{R}^{4}\times (\mathbb{S}^1)^4$$
where
\begin{align*}
 & \fleche{{\rm Log}\vert \Theta_N\vert\colon G_{hyp,N}(T,b)}{\mathbb{R}^{4}}{(\bu_{0,N},\bu_{1,N},\bv_{0,N},\bv_{1,N})}{\left(\frac{1}{N} {\rm Log}\vert u_{0,N}\vert,\frac{1}{N} {\rm Log}\vert u_{1,N}\vert,\frac{1}{N} {\rm Log}\vert v_{0,N}\vert,\frac{1}{N} {\rm Log}\vert v_{1,N}\vert\right)}\\
& \fleche{\mathcal{A}(\Theta_N)\colon G_{hyp,N}(T,b)}{(\mathbb{S}^1)^4}{(\bu_{0,N},\bu_{1,N},\bv_{0,N},\bv_{1,N})}{\left(e^{2\pi i \frac{a_{0,N}'}{N}},e^{2\pi i \frac{a_{1,N}'}{N}},e^{2\pi i \frac{b_{0,N}'}{N}}, e^{2\pi i \frac{b_{1,N}'}{N}}\right).}
\end{align*}
The maps ${\rm Log}\vert \Theta_N\vert$ factor to maps defined on $G_{hyp}(T,b)$, for which we keep the same notation. The subspace $\mathbb{R}^{4}\times (\mathbb{S}^1)^4\subset \mathbb{R}^{4}\times\mathbb{R}^{4}$ has the metric $d$ induced from the Euclidean distance, and the set of its subsets inherits the corresponding Hausdorff (pseudo-)distance: $\textstyle d(X,Y) = \max(\sup_{x\in X}(d(x,Y)), \sup_{y\in Y}(d(X,y)))$ for all $X,Y\subset \mathbb{R}^{4}\times (\mathbb{S}^1)^4$. 
\begin{lem}\label{lemYo} The sequence $\left(\Theta_N( G_{hyp,N}(T,b))\right)_N$ converges to $ \mathcal{C}(T,b)\times \mathcal{A}(T,b)\subset \mathbb{R}^{4}\times (\mathbb{S}^1)^4$ as $N\rightarrow +\infty$, $N$ odd, where $\mathcal{A}(T,b):= \{(z_1,z_2,z_3,z_4)\in (S^1)^4\ \vert \ z_1^2z_2z_3^2z_4=1\}$, and $\mathcal{C}(T,b)$ is the union of the following four half lines in $\mr^4$ (parametrized in $\mr^2\times \mr^2$):
$$\begin{array}{ccc} L_1 = \{t((-1,0),2(0,1)), t\geq 0\} & ,& L_2 = \{t(2(0,1),(-1,0)), t\geq 0\}\\
L_3 = \{t((-1,0),2(1,-1)), t\geq 0\} & , & L_4 = \{t(2(1,-1),(-1,0)), t\geq 0\}.
\end{array}$$ 
\end{lem}  
\proof The convergence of ${\rm Log}\vert \Theta_N\vert(G_{hyp}(T,b))$ to $\mathcal{C}(T,b)$ is the only non obvious fact; it follows from the Neumann-Zagier combinatorics \cite{NZ}, and is shown in Example 3.1 of \cite{Yo} (changing notations $z_1$, $z_2$ to $u_0^{-1}$, $v_0^{-1}$, respectively). The vectors $(-1,0)$, $(0,1)$, $(1,-1)$ used to define the half-lines $L_1,\ldots, L_4$ are the directions where $({\rm Log}\vert u_0\vert,{\rm Log}\vert u_1\vert)$ (resp. $({\rm Log}\vert v_0\vert,{\rm Log}\vert v_1\vert)$) tends as $u_0$ (resp. $v_0$) tends to $0$, $1$ or $\infty$. The images of the bounded subsets of $G_{hyp}(T,b)$ by the maps ${\rm Log}\vert \Theta_N\vert$ converge to $\{0\}\subset \mathbb{R}^{4}$ as $N\rightarrow +\infty$, hence the limit of ${\rm Log}\vert \Theta_N\vert(G_{hyp}(T,b))$ is the cone over its asymptotic directions, and the task is to compute these directions. 

Consider now the sets $\mathcal{A}(\Theta_N)(G_{hyp,N}(T,b))$. By rewriting the system \eqref{eqlog} in terms of the parameters $\bl_{k,N}^\bu$, $\bl_{k,N}^\bv$ in \eqref{defseqNcolor} and assuming the limits \eqref{deflimlkmars26} exist, as $N\rightarrow +\infty$ we get
\begin{equation}\label{eqloginfinity}
\left\lbrace\begin{array}{rcl}
\bl_{0,\infty}^{\bu}+\bl_{1,\infty}^{\bu}+\bl_{2,\infty}^{\bu} & = &0 \quad {\rm mod}(2\pi i)\\
\bl_{0,\infty}^{\bv}+\bl_{1,\infty}^{\bv}+\bl_{2,\infty}^{\bv} & = & 0 \quad {\rm mod}(2\pi i)\\
\bl_{1,\infty}^{\bu}+2\bl_{2,\infty}^{\bu}-2\bl_{0,\infty}^{\bv}-\bl_{1,\infty}^{\bv} & = & 0 \quad {\rm mod}(2\pi i)\\
2\bl_{0,\infty}^{\bu}-2\bl_{2,\infty}^{\bu}& = &\Log(\kappa^\infty(\lambda_K))  \quad {\rm mod}(2\pi i)\\
\bl_{2,\infty}^{\bu}+\bl_{2,\infty}^{\bv} & = & \Log(\kappa^\infty(\mu_K))  \quad {\rm mod}(2\pi i).
\end{array}\right.
\end{equation}
Note that the following limits take values in $\mr/2\pi\mz$:
$$\alpha_k^\infty := \mathfrak{I}(\bl_{k,\infty}^{\bu}) =  \textstyle \lim_{N\rightarrow \infty} \frac{2\pi a_{k,N}'}{N}\ ,\ \beta_k^\infty := \mathfrak{I}(\bl_{k,\infty}^{\bv}) =  \textstyle \lim_{N\rightarrow \infty} \frac{2\pi b_{k,N}'}{N}.$$ In particular the classical shape parameters $u_{k,N}$ and $v_{k,N}$ do not contribute to these limits. Taking imaginary parts in the system \eqref{eqloginfinity}, we find that $\alpha_k^\infty, \beta_k^\infty\in \mr/2\pi \mz$, for $k\in \{0,1,2\}$, satisfy the relations:
\begin{equation}\label{eqarginfinity}
\left\lbrace\begin{array}{rcl}
\alpha_0^\infty+\alpha_1^\infty+\alpha_2^\infty & = &0 \quad {\rm mod}(2\pi )\\
\beta_0^\infty+\beta_1^\infty+\beta_2^\infty & = & 0 \quad {\rm mod}(2\pi )\\
\alpha_1^\infty+2\alpha_2^\infty-2\beta_0^\infty-\beta_1^\infty & = & 0 \quad {\rm mod}(2\pi )\\
2\alpha_0^\infty-2\alpha_2^\infty & = &\arg(\kappa^\infty(\lambda_K))  \quad {\rm mod}(2\pi )\\
\alpha_2^\infty+\beta_2^\infty & = & \arg(\kappa^\infty(\mu_K))  \quad {\rm mod}(2\pi ).
\end{array}\right.
\end{equation}
The first three relations are the only constraints on $\alpha_k^\infty, \beta_k^\infty$, where $k\in \{0,1,2\}$ (in particular there is no contribution of the argument of the classical dilation factors $\arg(\delta_{w_N})$ in $\arg(\kappa^\infty(\cdot))$). Clearly then $(e^{i\alpha_0^\infty}, e^{i\alpha_1^\infty},e^{i\beta_0^\infty},e^{i\beta_1^\infty})\in \mathcal{A}(T,b)$, which shows that the sets $\mathcal{A}(\Theta_N)(G_{hyp,N}(T,b))$ degenerate to $\mathcal{A}(T,b)$ as $N\ra+\infty$.\endproof
\medskip

Assigning angles $(\alpha_0^\infty,\alpha_1^\infty,\alpha_2^\infty - \pi)$ and $(\beta_0^\infty,\beta_1^\infty,\beta_2^\infty-\pi)$ to $\Delta^0$ and $\Delta^1$, the system \eqref{eqarginfinity} shows that $\mathcal{A}(T,b)$ is a space of generalized angle structures on $T$, in a sense similar to \cite{LT}. These angle structures determine an asymptotic angular holonomy $\arg(\kappa^\infty(\cdot )) \in H^1(\partial \bar M;\mr/2\pi)$ by the relations (equivalent to the last two ones in \eqref{eqarginfinity}):
\begin{align}
4\alpha_0^\infty+2\alpha_1^\infty & = \arg(\kappa^\infty(\lambda_K)) \quad {\rm mod}(2\pi ),\label{asycurve}\\
\alpha_0^\infty+\alpha_1^\infty+\beta_0^\infty+\beta_1^\infty & =  -\arg(\kappa^\infty(\mu_K))  \quad {\rm mod}(2\pi ).\label{asycurvemu}
\end{align}

\begin{remark}\label{tropremk} {\rm (1) In the terminology of tropical geometry (\cite{V}) the set ${\rm Log}\vert \Theta_1\vert(G_{hyp}(T,b))$ is the {\it amoeba} of $G_{hyp}(T,b)$, and $\mathcal{C}(T,b)$ the {\it tropical curve} of $G_{hyp}(T,b)$. Also, let us identify $\mr^4$ with the interior of its closed unit ball $D^{4}$ by means of the map $x\mapsto x/(1+ \vert \vert \cdot \vert \vert)$, where $\vert \vert \cdot \vert \vert$ is the euclidian norm in $\mr^4$. Then the closure $\overline{\mathcal{C}(T,b)}$ of $\mathcal{C}(T,b)$ in $D^{4}$ has boundary $\partial_\infty \mathcal{C}(T,b) := \overline{\mathcal{C}(T,b)}\setminus \mathcal{C}(T,b)\subset S^3$,  $\mathcal{C}(T,b)$ is the cone over $\partial_\infty \mathcal{C}(T,b)$, and $\partial_\infty \mathcal{C}(T,b)$ is the {\it logarithmic limit set} of ${\rm Log}\vert \Theta_1\vert(G_{hyp}(T,b))$ in the sense of \cite{Berg}.\\
By means of Culler-Shalen theory (\cite{CS,Shalen}) such spaces play an important role in the detection of boundary slopes of incompressible surfaces in cusped manifolds $M$. These slopes are projective classes $[p\mu_K + q\lambda_K]\in \mathbb{P}^1_\mr(H_1(\partial \bar M;\mr))$. In particular, using also the Neumann-Zagier combinatorics \cite{NZ}, Yoshida showed that for $M=S^3\setminus 4_1$ the logarithmic limit set $\partial_\infty \mathcal{C}(T,b)$ determines the slopes (see \cite{Yo}, p. 160):
\begin{equation}\label{bslopes}
{\rm slope}(L_1) = {\rm slope}(L_3) = [4\mu_K - \lambda_K]\ ,\ {\rm slope}(L_2) = {\rm slope}(L_4) = [4\mu_K + \lambda_K].
\end{equation}
The map $\tilde{hol}\colon G_{hyp}(T,b))\ra \tilde{X}_{hyp}(M)$ of Section \ref{GhypN} identifies these boundary slopes with those detected by the Newton polygon of the factor of the $PSL(2,\mc)$ $A$-polynomial of $M$ corresponding to the curve $\tilde{X}_{hyp}(M)$ \cite{CCGLS,BD,Champ}. We refer to \cite{Tillmann0,Tillmann,Kabaya} for further developments and applications of this method to arbitrary cusped manifolds.\\
(2) As in Lemma \ref{lemYo} one can define a limit space $\mathcal{C}(\tilde X_{hyp}(M))\times (\mathbb{S}^1)^2$ of the tower of curves $\{{}_NX_{hyp}(M)\}_N$; the $(\mathbb{S}^1)^2$ factor is realized by the pairs $(e^{i\arg(\kappa^\infty(\lambda_K))},e^{\arg(\kappa^\infty(\mu_K))})$. As $N\to +\infty$, the maps $\widetilde{hol}\colon G_{hyp,N}(T,b) \rightarrow {}_NX_{hyp}(M)$ of Section \ref{GhypN} yields a map $\mathcal{C}(T,b)\times \mathcal{A}(T,b)\longrightarrow \mathcal{C}(\tilde X_{hyp}(M))\times (\mathbb{S}^1)^2$, where $\mathcal{C}(\tilde X_{hyp}(M))$ is the tropical curve assigned to the amoeba of $\tilde X_{hyp}(M)$, as in (1) above.} 
\end{remark}
