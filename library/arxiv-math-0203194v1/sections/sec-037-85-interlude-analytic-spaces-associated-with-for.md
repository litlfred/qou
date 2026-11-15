---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-037-85-interlude-analytic-spaces-associated-with-for
section_title: "Interlude : analytic spaces associated with formal schemes and tubes."
section_number: 8.5
pages: 83-84
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.712
latex_coverage_ratio: 0.912
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:3.5}

\begin{para}\label{para:3.5.1} Let us first review the Raynaud-Berthelot
construction of the analytic space attached to a  
$\mathfrak{v}$-formal scheme $\mathfrak{X}$. It will be convenient for
later purpose to formulate the construction in the frame of Berkovich
spaces rather than rigid geometry (we refer to \cite[1.6]{ecfnas} for the
translation).


As in \ref{para:2.2.5}, we assume that $\mathfrak{X}$ is adic, locally
noetherian; moreover, we assume that 
${\mathfrak{X}}_{\mathrm{red}}=\Spec(\mathcal{O}_{\mathfrak{X}}/\mathcal{J})$ is a
separated $k$-scheme locally of finite type (in particular,
$p\in \mathcal{J}$). However, we {\it do not} assume that $\mathfrak{X}$ is
$p$-adic, \ie that the topology of $\mathcal{O}_{\mathfrak{X}}$
is $p$-adic.

 We describe the construction in the affine case ${\mathfrak{X}} =
 \Spf(\mathcal{A})$; the general case follows by gluing. One chooses
 generators $f_1,\ldots, f_r$ of 
 $J=\Gamma({\mathfrak{X}},\mathcal{J})$, and defines, for any $n>0$,
 \begin{equation*}
 \mathcal{B}_n=\mathcal{A}\{T_1,\ldots,T_r\}/(f_1^n-\varpi T_1,\ldots,
 f_r^n-\varpi T_r)
 \end{equation*}
 where $\mathcal{A}\{T_1,\ldots,T_r\}$ stands for the $\varpi$-adic
 completion of $\mathcal{A}[T_1,\ldots,T_r]$. One has
 $\mathcal{B}_n/\varpi\mathcal{B}_n\cong
 (\mathcal{A}/(\varpi,f_1^n,\ldots,f_r^n))[T_1,\ldots,T_r]$, a
 $k$-algebra of finite type; hence $\mathcal{B}_n$ is a
 $\mathfrak{v}$-algebra topologically of finite type (\ie quotient of an
 algebra of the form $\mathcal{A}\{T_1,\ldots,T_{r_n}\}$), so that
 $\mathcal{B}_n[\frac{1}{p}]$ is an affinoid algebra. Let
 $\matheur{M}(\mathcal{B}_n)$ be its Berkovich spectrum. The
 homomorphism $\mathcal{B}_{n+1}\rightarrow \mathcal{B}_n$ sending $T_i$
 to $f_iT_i$ identifies $\matheur{M}(\mathcal{B}_n)$ with an affinoid
 subdomain of $\matheur{M}(\mathcal{B}_{n+1})$ \cite[0.2.6]{crecrasp}.


 The analytic space $\mathfrak{X}^{\mathrm{an}}$ is defined as the union
 $\bigcup_n \matheur{M}(\mathcal{B}_n)$. It does 
 not depend on the choice of $f_1,\ldots, f_r$. This is a {\it
 paracompact (strictly) analytic space} over the fraction 
 field $K$ of $\mathfrak{v}$  (one can replace the nested ``ball-like''
 $\matheur{M}(\mathcal{B}_n)$ by nested ``annulus-like'' 
 spaces in order to obtain locally finite coverings). 
\end{para}

\begin{exs}\label{para:3.5.2}
 (i) if ${\mathfrak{X}}=\Spf(\mathfrak{v}\{t\})$,
 ${\mathfrak{X}}^{\mathrm{an}}$ is the closed unit disc.
 
 (ii) if ${\mathfrak{X}}=\Spf({\mathfrak{v}[[t]]}),
 \;\mathcal{J}=(\varpi, t)$, then $\matheur{M}(\mathcal{B}_n)$ is the 
 closed disc $\matheur{D}_K(0,|\varpi|^{1/n})$, and
 ${\mathfrak{X}}^{\mathrm{an}}$ is the open unit disc. 
\end{exs}

\begin{para}\label{para:3.5.3} Let $S_0$ be a closed subscheme of
$\mathfrak{X}_{\mathrm{red}}$, and let ${\mathfrak{X}}_{S_0}$ be the formal
completion of $\mathfrak{X}$ along $S_0$. The {\it tube of $S_0$ in
$\mathfrak{X}$} is $\mathfrak{X}_{S_0}^{\mathrm{an}}$. It is denoted by
$]S_0[_{\mathfrak{X}}$ (and considered as a subspace of
$\mathfrak{X}^{\mathrm{an}}$). It depends only on $S_{0,\mathrm{red}}$.  

\medskip
 \noindent {\it Example}: if $\mathfrak{X}$ is as in example (i) above
 (so that $\mathfrak{X}_{\mathrm{red}}=\A^1_k$), and $S_0$ is the point $0$,
 then $\mathfrak{X}_{S_0}$ is as in example (ii) above:
 $]0[_{\mathfrak{X}}\;=\matheur{D}(0,1^-)\subset \matheur{D}(0,1^+)$. 

 \noindent More generally, the polydiscs mentioned in \ref{para:3.4.3}
 are the tubes of closed points.
\end{para}
