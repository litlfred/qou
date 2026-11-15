---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-004-41-representation-of-the-remainder-term-rp
section_title: "Representation of the remainder term R(p)"
section_number: 4.1
pages: 9-10
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.968
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
In this subsection we are concerned with an alternative representation of the remainder term $R^{(p)}$ and its derivatives.
Let us first recall the following result.

\begin{lemma}[Regularity of the remainder integrand, \protecting{\cite[Lemma 4.4]{BlattReiter:2015:Menger}}]
    \label{lemma:regularityIntegrandRemainder}\ \\
    Let $\g\in W^{(3p-4)/2+\s,2}(\R/\Z,\R^n)$ be a simple curve parametrized by arc-length.
    \begin{itemize}
        \item If $\s=0$, then $\gp\in L^{1}(\R/\Z\times D,\R^{n})$ and
        \item if $\s>0$, then $((v,w) \mapsto \gp(\cdot,v,w;\dots))\in L^{1}(D,\W[\tilde\s,1](\R/\Z, \R^{n}))$ for any $\tilde\s<\s$.
    \end{itemize}
    The respective norms are bounded independently of $s_{1},\dots,s_{K}$.
\end{lemma}

We then derive a representation of the remainder term $R^{(p)}$ corresponding to the $L^2$-re\-pre\-sen\-ta\-tion of the main term $Q^{(p)}$ in the first variation of $\Mpz$. Recall that  $\otimes$ denotes any kind of bilinear product structure, such as cross product, dot product, scalar or matrix multiplication.

\begin{lemma}
    \label{lemma:L2formRemainder}
    Let $\gamma \in C^\infty(\R/\Z,\R^n)$ be parametrized by arc-length and let $h \in W^{\frac 3 2 p -2,2}(\R/\Z,\R^n)$. 
    Then,
    \[
        R^{(p)}(\gamma,h)=\int_{\R/\Z} \left<\Rpt(\gamma)(u), h(u)\right>  \d u
    \]
    with
    \[	
        \Rpt(\gamma)_o(u) := \sum_{k=1}^{k_{\max}} \iint_{D} \idotsint\limits_{[0,1]^K} \frac \d {\d u} g^p_k(u - s_{K-1}v - s_K w,v,w;s_{1},\dots,s_{K-2}) \d\theta_{1}\cdots\d\theta_{K}\d v \d w \otimes e_o.
    \]
    Here, $e_o \in \R^n$ is the $o$-th canonical unit vector, each $g^p_k$ is of the same form as $g^p$ in \thref{lemma:formRemainder} and neither $K$ nor $k_{\max}$ depend on $\gamma$.
    Furthermore, $u \mapsto g^p_k(u,v,w;s_1,\ldots,s_K) \in C^\infty(\R/\Z,\R^n)$ for all $k \in \set{1,\ldots,k_{\max}}$.
\end{lemma}
\begin{proof}
	Since $\gamma \in C^\infty(\R/\Z,\R^n)$, \thref{lemma:regularityIntegrandRemainder} yields that the integrand is in fact integrable on the integration domain, allowing us to substitute $u$ by $\tilde u := u +s_{K-1}v + s_K w$.
	We also obtain that $u \mapsto g^p(u,v,w;s_1,\ldots,s_K) \in C^\infty(\R/\Z,\R^n)$ and note that $\otimes$ is a bilinear operation. Thus we may use integration by parts component-wise to obtain that \eqref{lemma:formRemainder:formula} is equal to
	\[
	\iiint\limits_{\mathbb R / \mathbb Z \times D} \idotsint\limits_{[0,1]^K} (\tfrac \d {\d \tilde u} g^p(\tilde u - s_{K-1}v - s_K w,v,w;s_{1},\dots,s_{K-2}) ) \otimes h(\tilde u)
	\d\theta_{1}\cdots\d\theta_{K}\d v \d w \d \tilde u.
	\]
	Note that we have no boundary terms because both $h$ and $g^p$ are periodic.
	Using the bilinearity of $\otimes$, we may write \Rpt{} as
    \[
        \int_{\R/\Z} \overline{R}^{(p)}(\gamma)(u) \otimes h(u) \d u 
    \]
    with
    \[
        \overline{R}^{(p)}(\gamma)(u) := \sum_{k=1}^{k_{\max}} \iint_{D} \idotsint\limits_{[0,1]^K} \frac \d {\d u} g^p_k(u - s_{K-1}v - s_K w,v,w;s_{1},\dots,s_{K-2}) \d\theta_{1}\cdots\d\theta_{K}\d v \d w.
    \]
    Seeing as $x \mapsto \overline{R}^{(p)}(\gamma)(u) \otimes x \in \R$ is linear, we may set
    \[
        \Rpt(\gamma)_o(u) := \overline{R}^{(p)}(\gamma)(u) \otimes e_o
    \]
    and obtain for $x = \sum_{o=1}^n x_oe_o \in \R^n$:
    \[
        \overline{R}^{(p)}(\gamma)(u) \otimes x = \sum_{o=1}^n x_o \cdot \overline{R}^{(p)}(\gamma)(u) \otimes e_o = \sum_{o=1}^n x_o \cdot \Rpt(\gamma)_o(u) = \left<\Rpt(\gamma)(u),x\right>.
    \]
\end{proof}

The $l$-th derivative of the remainder representation \Rpt{} can be computed as follows.
\begin{lemma}
    Let $\gamma \in C^\infty(\R/\Z,\R^n)$ be parametrized by arc-length.
    Then, 
    \[
        \begin{split}
            &\frac {\d^l} {\d u^l} \Rpt(\gamma)_o(u)\\
            =& \sum_{k=1}^{k_{\max}} \iint_{D} \idotsint\limits_{[0,1]^K} \frac {\d^{l+1}} {\d u^{l+1}} g^p_k(u - s_{K-1}v - s_K w,v,w;s_{1},\dots,s_{K-2}) \d\theta_{1}\cdots\d\theta_{K}\d v \d w\otimes e_o
        \end{split}
    \]
    for all $l \in \N$.
\end{lemma}
Note that we do not need the assumption of arc-length parametrization here, as $\Rpt$ is well-defined without it.
However, for other parametrizations, we do not expect $\Rpt(\gamma)$ to be related to $R^{(p)}(\gamma,\cdot)$.
\begin{proof}
    Since $X \mapsto X \otimes e_o$ is a fixed linear map, $\frac {\d^l} {\d u^l} (X(u) \otimes e_o) = ( \frac {\d^l} {\d u^l} \partial^l X(u)) \otimes e_o$, so we only need to worry about the integral term.
    By \thref{lemma:regularityIntegrandRemainder}, $((v,w) \mapsto \gp_k(\cdot,v,w;\dots))\in L^{1}(D,W^{\tilde \sigma,1}(\R/\Z, \R^{n}))$ for all $\tilde\sigma>0$ and its norm is independent of $s_1, \ldots, s_K$.
    This means that $g^p_k$ is differentiable with respect to $u$ arbitrarily many times and the derivatives are all integrable with the majorant
    \[
        \norm[L^\infty]{\partial_1^{l+1} g^p_k(\cdot,v,w;s_1,\ldots,s_K)}.
    \]
    By the Morrey- (see e.g.\ \cite[Paragraph~4.16]{AdamsFournier:2003:SobolevSpaces}) and Sobolev-embedding theorems, we can bound this above by
    \[
        C\norm[W^{1,2}]{\partial_1^{l+1} g^p_k(\cdot,v,w;s_1,\ldots,s_K)}
        \le \widetilde C \norm[W^{l + \frac 5 2,1}]{g^p_k(\cdot,v,w;s_1,\ldots,s_K)}.
    \]
    As we have a uniform $L^1$-bound on the latter, we may exchange integration and differentiation.
\end{proof}
