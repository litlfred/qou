---
doc_id: arxiv-1908.11677v1
doc_title: "Variational formulae and estimates of O’Hara’s knot energies"
section_id: sec-003-31-strategy
section_title: "Strategy"
section_number: 3.1
pages: 11-12
source_pdf: 1908.11677v1.pdf
source_sha256: c53663eeb457daf9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.895
latex_coverage_ratio: 0.943
doc_brief: "Variational formulae and estimates of O’Hara’s knot energies — O’Hara’s energies, introduced by Jun O’Hara, were proposed to answer the question of what is the canonical shape in a given knot type"
---
Let
$\vecf$,
$\vecphi$,
$\vecpsi \in W^{1+\sigma , 2p}(\R/\calL\Z , \R^n) \cap W^{1,\infty}(\R/\calL\Z , \R^n)$,
and assume that
$\vecf$
is bi-Lipschitz.
By \cite{B12},
we already know the estimate
\begin{equation}\label{Malpha Lp}
	\| \scrM_\alpha(\vecf) \|_{L^p} \leq C.
\end{equation}
Combining Theorem \ref{variation} and H\"{o}lder's inequality,
if
$p>1$,
we have
\begin{align*}
	\| \scrG_1(\vecf)[\vecphi] \|_{L^1}
	&\leq
	p \| \scrM_\alpha(\vecf) \|_{L^p}^{p-1} \| \delta \scrM_\alpha(\vecf)[\vecphi] \|_{L^p},
\\
	\| \scrG_2(\vecf)[\vecphi] \|_{L^1}
	&\leq
	2 \| \scrM_\alpha(\vecf) \|_{L^p}^p \| \vecphi^\prime \|_{L^\infty},
\\
	\| \scrH_1(\vecf)[\vecphi,\vecpsi] \|_{L^1}
	&\leq
	p \| \scrM_\alpha(\vecf) \|_{L^p}^{p-1} \| \delta^2 \scrM_\alpha(\vecf) [\vecphi,\vecpsi] \|_{L^p},
\\
	\| \scrH_2(\vecf)[\vecphi,\vecpsi] \|_{L^1}
	&\leq
	p(p-1) \| \scrM_\alpha(\vecf) \|_{L^p}^{p-2}
	\| \delta \scrM_\alpha(\vecf) [\vecphi] \|_{L^p} \| \delta \scrM_\alpha(\vecf) [\vecpsi] \|_{L^p},
\\
	\| \scrH_3(\vecf)[\vecphi,\vecpsi] \|_{L^1}
	&\leq
	2 \| \scrG_1(\vecf)[\vecphi] \|_{L^1} \| \vecpsi^\prime \|_{L^\infty},
\\
	\| \scrH_4(\vecf)[\vecphi,\vecpsi] \|_{L^1}
	&\leq
	2 \| \scrG_1(\vecf)[\vecpsi] \|_{L^1} \| \vecphi^\prime \|_{L^\infty},
\\
	\| \scrH_5(\vecf)[\vecphi,\vecpsi] \|_{L^1}
	&\leq
	6 \| \scrM_\alpha(\vecf) \|_{L^p}^p
	\| \vecphi^\prime \|_{L^\infty} \| \vecpsi^\prime \|_{L^\infty},
\\
	\| \scrH_6(\vecf)[\vecphi,\vecpsi] \|_{L^1}
	&\leq
	4 \| \scrM_\alpha(\vecf) \|_{L^p}^p
	\| \vecphi^\prime \|_{L^\infty} \| \vecpsi^\prime \|_{L^\infty}.
\end{align*}
Hence,
if there exists
$C=C(\vecf)>0$
such that
\begin{equation}\label{what to prove Malpha}
\begin{split}
	\| \delta \scrM_\alpha(\vecf)[\vecphi] \|_{L^p}
	&\leq C \| \vecphi^\prime \|_{W^{\sigma,2p} \cap L^\infty},
\\
	\| \delta^2 \scrM_\alpha(\vecf)[\vecphi,\vecpsi] \|_{L^p}
	&\leq
	C \| \vecphi^\prime \|_{W^{\sigma,2p} \cap L^\infty}
	\| \vecpsi^\prime \|_{W^{\sigma,2p} \cap L^\infty},
\end{split}
\end{equation}
then the desired
$L^1$-estimates for
$\scrG_{(\alpha,p)}(\vecf)$
and
$\scrH_{(\alpha,p)}(\vecf)$
follow.

Next we observe that since
$\| \Delta \vecf \|_{\R^n} \leq \scrD(\vecf)$
holds,
and using the bi-Lipschitz estimate,
we deduce that there exists
$\tilde{C}=\tilde{C}(\vecf)>0$
such that
$0 \leq \scrN(\vectau) \leq \tilde{C}$.
Hence,
we have
\[
	| \vphi_\alpha^{(j)} (\scrN(\vectau)) | \leq
	\max_{t \in [0,\tilde{C}]} | \vphi_\alpha^{(j)} (t) | < \infty
\]
for
$j=0,1,2$.
By Proposition \ref{variation Malpha},
H\"{o}lder's inequality,
and \eqref{Malpha Lp},
we can show \eqref{what to prove Malpha} if there exists
$C=C(\vecf)>0$
such that
\begin{align*}
	\left\|
	\frac{ \delta \scrN(\vectau)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right\|_{L^p}
	&\leq
	C \| \vecphi^\prime \|_{W^{\sigma,2p} \cap L^\infty},
\\
	\left\|
	\frac{ \delta^2 \scrN(\vectau)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha }
	\right\|_{L^p}
	&\leq
	C \| \vecphi^\prime \|_{W^{\sigma,2p} \cap L^\infty}
	\| \vecpsi^\prime \|_{W^{\sigma,2p} \cap L^\infty},
\\
	\left\|
	\frac{ \delta\| \Delta \vecf \|_{\R^d}^2[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^2 }
	\right\|_{L^\infty}
	&\leq
	C \| \vecphi^\prime \|_{L^\infty},
\\
	\left\|
	\frac{ \delta^2\| \Delta \vecf \|_{\R^d}^2[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^2 }
	\right\|_{L^\infty}
	&\leq
	C \| \vecphi^\prime \|_{L^\infty} \| \vecpsi^\prime \|_{L^\infty}.
\end{align*}
Similarly,
to obtain the desired
$L^\infty$-estimates and continuity,
it suffices to consider the corresponding properties of
\begin{equation}\label{what to prove}
	\frac{ \delta \scrN(\vectau)[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^\alpha },
	\quad
	\frac{ \delta^2 \scrN(\vectau)[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^\alpha },
	\quad
	\frac{ \delta\| \Delta \vecf \|_{\R^d}^2[\vecphi] }{ \| \Delta \vecf \|_{\R^n}^2 },
	\quad
	\frac{ \delta^2\| \Delta \vecf \|_{\R^d}^2[\vecphi,\vecpsi] }{ \| \Delta \vecf \|_{\R^n}^2 }.
\end{equation}
