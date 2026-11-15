---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-036-84-crystals-and-connections
section_title: "Crystals and connections."
section_number: 8.4
pages: 82-83
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.975
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:3.4} 

\begin{para}\label{para:3.4.1}
 We have already encountered the terms ``$F$-crystal'', ``unit-root
 $F$-crystal'' in I.\ref{para:f-cris}, \ref{para-unit-root} in the more
 down-to-earth context of 
 connections. This comes as follows. Assume for simplicity that $S_0$ is
 affine of characteristic $p$ and lifts to a formally smooth $p$-adic
 affine formal scheme $\mathcal{S}$ over $\mathfrak{v}=W$.  Then there
 is an equivalence of categories between finite locally free crystals on
 $(S_0/W)_{\mathrm{cris}}$ and finite locally free
 $\mathcal{O}(\mathcal{S})$-modules with integrable topologically
 nilpotent connection (this interpretation of crystals extends to much
 more general situations, \cf \cite[2.2.2]{jong95:_cryst_dieud}).

 \noindent Using this equivalence of categories, the Katz (covariant) functor
 \begin{equation*}
  \begin{pmatrix}\text{continuous }{\Z}_p\text{-representations} \\
   \text{of } \pi_1^{\mathrm{alg}}(S_0,s_0)
  \end{pmatrix}
  \longrightarrow \text{(unit-root $F$-crystals)}
 \end{equation*}
 is the composite of the following (anti)equivalences of categories
 \begin{align*}
  \begin{pmatrix}\text{continuous } {\Z}_p\text{-representations} \\
   \text{of } \pi_1^{\mathrm{alg}}(S_0,s_0)
  \end{pmatrix}& \longrightarrow
  \text{(ind-etale $p$-divisible groups over $S_0$)}\\
  & \overset{\D}{\longrightarrow}
  \text{(unit-root $F$-crystals over $S_0$)}.
 \end{align*} 
\end{para}

\begin{para}\label{para:3.4.2}
 Let us briefly recall the construction of the connection attached to a
 finite locally free crystal $\mathcal{E}$ on
 $(S_0/W)_{\mathrm{cris}}$. It depends on the technique of formally
 adding divided powers to an ideal (the pd-hull). Let $\Delta_0$ be the
 diagonal in $S_0\times S_0$, and let $\hat\Delta$ be the $p$-completion
 of the pd-hull of the diagonal in $\mathcal{S}\hat\times\mathcal{S}$,
 endowed with the two projections $p_1,p_2$ to $\mathcal{S}$. Then by
 rigidity of crystals, we have for any $n$ an isomorphism
 \begin{equation*}
  p_2^\ast(\mathcal{E}_{S_0,\mathcal{S}/p^n})\;\cong
   \;\mathcal{E}_{\Delta_0,\hat\Delta/p^n}\;\cong
   \;p_1^\ast(\mathcal{E}_{S_0,\mathcal{S}/p^n})
 \end{equation*}
 and at the limit $n\rightarrow \infty$, an isomorphism of finite
 locally free $\mathcal{O}({\hat\Delta})$-modules  
 \begin{equation*}
  \epsilon:\; p_2^\ast(\mathcal{E}_{S_0,\mathcal{S}})\;\cong
   \;p_1^\ast(\mathcal{E}_{S_0,\mathcal{S}})
 \end{equation*}
 satisfying a cocycle condition. Such an isomorphism is the ``Taylor series'' 
 \begin{equation*}
  \epsilon(1\otimes e) = \sum_{n_1,\ldots,n_d\geq
   0}\biggl(\nabla\Bigl(\frac{\partial}{\partial t_1}\Bigr)^{n_1}
   \ldots\nabla\Bigl(\frac{\partial}{\partial t_d}\Bigr)^{n_d}\biggr)(e)
   \otimes \prod_i \frac{\text{``$(1\otimes t_i-t_i\otimes 1)^{n_i}$''}}{n_i!}
 \end{equation*}
 of an integrable connection $\nabla$ on the finite
 locally free $\mathcal{O}(\mathcal{S})$-module
 $\;\mathcal{E}_{S_0,\mathcal{S}}$ (here $t_1,\ldots t_d$ denote local
 coordinates on $\mathcal{S}$).
\end{para}

\begin{para}\label{para:3.4.3}
 In general, the Taylor series converges only in polydiscs of radius
 $| p |^{1/p-1}$, due to the presence of the factorials. One
 says that $\nabla$ is {\it convergent} if its Taylor series converges
 in (open) unit polydiscs. A well-known argument due to Dwork shows that
 $F$-crystals give rise to convergent connections $\nabla$ (\cite{tdd}).

 In order to put the discussion of convergence on proper foundations, we
 need the notion of tube in analytic geometry.
\end{para}
