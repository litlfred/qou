---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-002-3-estimate-of-the-main-term-qp
section_title: "Estimate of the main term Q(p)"
section_number: 3
pages: 7-9
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.991
---
\label{sec:EstimateMainTerm}

Next we investigate the order of the main term $Q^{(p)}$, for which we need to examine its $L^2$-representation first.

\begin{lemma}
    \label{lemma:L2MainTermViaFourier}
    Let $p \in (\tfrac 7 3,\tfrac 8 3)$, $s \ge 0$ and $\gamma \in H^{3p-4+s}(\R/\Z,\R^n)$ be parametrized by arc-length.
    Then, there is $\Qpt(\gamma) \in H^s(\R/\Z,\R^n)$ such that for all $h \in H^{\frac 3 2 p -2}(\R/\Z,\R^n)$,
    \[
        \Qp(\gamma,h) = \int_{\R/\Z} \left<\Qpt(\gamma)(u), h(u)\right> \d u.
    \]
    In particular, $\Qpt$ maps $C^\infty(\R/\Z,\R^n)$ into itself.
    The Fourier coefficients of $\Qpt$, for all $k\in \Z$, are given by
    \begin{align*}\label{eq:fouriercoeffQ}
        \widehat{\Qpt(\gamma)}(k) = q_k^{(p)} \abs{k}^{3p-4} \hat{\gamma} (k).
    \end{align*}
    The constants $q_k^{(p)}$ are bounded independently of $n$, and satisfy 
    \[
        0 \leq q_k^{(p)} = c + o(1)
    \]
    as $\abs{k} \rightarrow \infty$ for $c>0$.
\end{lemma}
\begin{proof}
    By \cite[Proposition 4.1]{BlattReiter:2015:Menger}, we have
    \[
        \Qp(\gamma,h) = \sum_{k \in \Z}\rho_k \left< \hat \gamma(k),\hat h(k)\right>_{\C^n}, \text{ where } \rho_k = c\abs{k}^{3p-4} + o(\abs{k}^{3p-4}) \text{ as } \abs{k} \to \infty,
    \]
    for any $h \in H^{\frac 3 2 p -2}(\R/\Z,\R^n)$. In particular,  the $\rho_k$ are independent of $n$, cf.\ their definition in the proof of \cite[Proposition 4.1]{BlattReiter:2015:Menger}.
    Setting $q_k^{(p)} := \abs{k}^{4-3p} \rho_k$, which implies that the $q_k^{(p)}$ are also independent of $n$, we obtain
    \[
        \begin{split}
            (1+k^2)^{\frac s 2}\abs[\big]{q_k^{(p)}\abs{k}^{3p-4}\hat \gamma(k)}
            &= (1+k^2)^{\frac s 2}\abs{c+o(1)}\abs{k}^{3p-4} \abs{\hat \gamma(k)}\\
            &\le (1+k^2)^{\frac s 2} \tilde c \abs{k}^{3p-4} \abs{\hat \gamma(k)}
            \le \tilde c (1+k^2)^{\frac {3p-4+s} {2}} \abs{\hat \gamma(k)} \text{ as } \abs{k} \to \infty
        \end{split}
    \]
    for some $\tilde c>0$.
    The right hand side, taken as a sequence in $k \in \Z$, is in $\ell^2(\Z)$ because $\gamma \in H^{3p-4+s}(\R/\Z,\R^n)$, see \cite[Chapter~4, (3.8)]{Taylor:1996:PartialDifferentialEquationsa},
    and so $\Qpt(\gamma)$, the inverse Fourier transform of $q_k^{(p)}\abs{k}^{3p-4}\hat \gamma(k)$, is well-defined and in $H^s(\R/\Z,\R^n)$.
    All $q_k^{(p)}\abs{k}^{3p-4}$ are real as $\Qp$ maps real functions to real numbers and $\overline{\hat \gamma(k)} = \hat \gamma (-k)$ due to the real image of $\gamma$.
    Thus, $\Qpt(\gamma)(u) = \sum_{k\in \Z} q_k^{(p)}\abs{k}^{3p-4} \hat{\gamma}(k) e^{-2\pi i k u} = \hat \gamma(0) + \sum_{k \in \N} q_k^{(p)}\abs{k}^{3p-4} \Re(\hat \gamma(k) e^{-2 \pi i k u})$ for almost all $u \in \R/\Z$ meaning that $\Qpt(\gamma)$ maps into the real numbers.
    
    By Parseval's relation \cite[Proposition~3.2.7~(3)]{Grafakos:2014:ClassicalFourierAnalysis}, we have
    \[
        \int_{\R/\Z} \left<\Qpt(\gamma)(u),h(u)\right> \d u
        = \sum_{k\in \Z} \left< q_k^{(p)}\abs{k}^{3p-4}\hat \gamma(k), \hat h(k)\right>_{\C^n}
        = \sum_{k \in \Z}\rho_k \left< \hat \gamma(k),\hat h(k)\right>_{\C^n}
        = \Qp(\gamma,h).
    \]
\end{proof}
\begin{remark}
    Assuming $C^5$-regularity of $\gamma$, one may explicitly calculate
    \begin{align*}
        \Qpt(\gamma)(u) :=& \iint_D \abs{v-w}^{-p} \abs{v}^{2-p} \abs{w}^{2-p} \cdot \Biggl(
        \frac {\frac{\difference{-w,0} \gamma} {-w} - \frac {\difference{w,0} \gamma} {w}} {w}
        + \frac {\frac {\difference{-v,0} \gamma} {-v} - \frac {\difference{v,0} \gamma} {v}} {v}\\
        &+ \frac {\frac {\difference{v,0} \gamma} {v} - \frac {\difference{v-w,-w} \gamma} {v}} {w}
        + \frac {\frac {\difference{w,0} \gamma} {w} - \frac {\difference{w-v,-v} \gamma} {w}} {v}
        \Biggr)
        \d w \d v.
    \end{align*}
    The proof works via first restricting to the case $\abs{v},\abs{w}>\epsilon$ to obtain the formula and then showing existence for $\epsilon = 0$ by means of several Taylor approximations.
    Since this method is quite technical and long, we choose to omit it here.
\end{remark}

From the previous \thref{lemma:L2MainTermViaFourier}, we deduce the following indispensable corollary regarding the order of the main term $Q^{(p)}$.


\begin{corollary}  \label{cor:Ql}
	Given real numbers $p\in (\tfrac 73, \tfrac 83)$ and $m\geq 0$, there exists a constant $ \widetilde{C}=\widetilde{C}(p)>0$ such that for all curves $\gamma \in C^\infty(\R/\Z, \R^n)$ and  integers $l\geq 0$ 
	\begin{align*}
	\|\gamma^{(l+3)} \|_{H^{m+3p-7}} \leq \widetilde{C} \|\partial^{l} \Qpt(\gamma)\|_{H^m}
	\end{align*}
	holds.
\end{corollary}
\begin{proof}
	By applying \thref{lemma:L2MainTermViaFourier}, well-known properties of Fourier coefficients and the elementary estimate $(1+k^2)^{3p-7} \leq (2|k|)^{2(3p-7)}$ for any $k\in \Z  \setminus 0$,  we get
	\begin{align*}
	\|\partial^{l}\Qpt (\gamma) \|_{H^m}^2 &= \sum_{k\in \Z} (1+|k|^2)^m|\widehat{\partial^{l}\Qpt (\gamma)}(k)|^2 \\
	&= \sum_{k\in \Z} (1+|k|^2)^m (2\pi| k|)^{2l} |\widehat{\Qpt (\gamma)}(k)|^2 \\
	&= \sum_{k\in \Z} (1+|k|^2)^m (2\pi| k|)^{2l} (q_k^{(p)})^2 |k|^{2(3p-4)} |\hat{\gamma} (k)|^2\\
	&\geq \inf_{k\in\Z\setminus 0} \{(q_k^{(p)})^2 (2\pi)^{-6} 2^{2(7-3p)} \} \sum_{k \in \Z} (1+|k|^2)^{m+3p-7} (2\pi| k|)^{2(l+3)}   |\hat{\gamma} (k)|^2 \\
	&= \widetilde{C}^{-2} \sum_{k \in \Z} (1+|k|^2)^{m+3p-7} |\widehat{\gamma^{(l+3)} } (k)|^2 \\
	&= \widetilde{C}^{-2}   \|\gamma^{(l+3)} \|_{H^{m+3p-7}}^2,
	\end{align*}
	where $\widetilde{C}:=\inf_{k\in\Z\setminus{0}} \{\abs{q_k^{(p)}} (2\pi)^{-3} 2^{7-3p}\}^{-1}$ is a positive constant only depending on $p$.
    In particular, independence of $n$ follows from  \thref{lemma:L2MainTermViaFourier}.
\end{proof}
