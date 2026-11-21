---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-040-92-examples
section_title: "Examples."
section_number: 9.2
pages: 87-89
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.653
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:4.2}
 We take $\ovl{\Lambda} ={\ovl{A}}[p^\infty]$, the $p$-primary
 torsion of an {\it elliptic curve ${\ovl{A}}$ over ${\ovl{\F}}_p$} ($h=2$).

\begin{para}\label{para:4.2.1}
 {\it The ordinary case}, \ie ${\ovl{A}}[p]({\ovl{\F}}_p)\neq 0$. 

 Then $\ovl{\Lambda}\cong\hat {\G}_m \oplus {\Q}_p/{\Z}_p$, and
 $J=({\G_m}_{{\Q}_p})^2$. For any $(\Lambda,\rho)$ in $\mathfrak{M}(S)$,
 the separable rank of $\Ker[p]$ is constant (due to the quasi-isogeny
 $\rho$). Therefore $\Lambda$ is an extension 
 \begin{equation*}
  \hat{\Lambda}\rightarrow \Lambda\rightarrow \Lambda^{\mathrm{et}}.
 \end{equation*}
 The quasi-isogeny $\rho$ respects this extension,
 hence splits into two parts $({\hat\rho},\rho^{\mathrm{et}})$. We have
 ${\hat\Lambda}\cong \hat {\G}_m ,\;\Lambda^{\mathrm{et}}\cong
 {\Q}_p/{\Z}_p$. Up to isomorphism, the pair
 $({\hat\rho},\rho^{\mathrm{et}})$ thus amounts to an element of
 $({\Q}_p^\times/{\Z}_p^\times)^2\cong {\Z}^2$. Therefore
 \begin{equation*}
  \mathfrak{M}=\coprod_{\Z^2}\;\mathfrak{M}^0
 \end{equation*}
 is a disjoint sum of copies of a formal (group) scheme
 $\mathfrak{M}^0$ which parametrizes extensions of ${\Q}_p/{\Z}_p$ by $
 \hat {\G}_m$. It is known that
 \begin{equation*}
  \mathfrak{M}^0 =\hat {\G}_m
 \end{equation*} 
 This identification is given by the
 following recipe. Recall that if $S=\Spec(R),\;R$ local artinian with
 residue field ${\ovl{\F}}_p$ and radical $\mathfrak{m}$
 ($\mathfrak{m}^{n+1}=0$), then $\hat {\G}_m(S)=1+\mathfrak{m}$; in
 particular $\hat {\G}_m(S)$ is killed by $[p^n]$. Let us choose any lift
 $q_n$ of $1/p^n\in {\Q}_p/{\Z}_p$ in $\Lambda$. Then $[p^n]q_n$ is a
 well-defined element $q$ in $ {\hat\Lambda}(S)\cong 1+\mathfrak{m}$,
 which is unchanged if $n$ is replaced by a bigger integer (but another
 choice of the isomorphism ${\hat\Lambda}\cong \hat {\G}_m$ would change
 $q$ into $q^a,\; a\in {\Z}_p^\times$).
 

 \noindent As a formal $W$-scheme, $\mathfrak{M}^0=
 \Spf(\mathfrak{v}[[q-1]])$, with the $(p,q-1)$-adic topology. 
 The associated analytic space $\mathcal{M}^0$ over $\C_p$ is the open
 unit disc $| q-1| <1$.
 
 The parameter $q$ is thus the local modulus for deformations of
 ${\ovl{A}}[p^\infty]$.  
 On the other hand, if
 $p\neq 2$, we have an algebraic local modulus for deformations of
 ${\ovl{A}}$ (say, with level two structure): the Legendre parameter
 $z=\lambda$ around the Legendre parameter $\zeta_{\mathrm{can}}$ of the
 canonical lifting $A_{\mathrm{can}}$ of ${\ovl{A}}$ (\cf 
 I.\ref{para-dwork-para}).
 The $p$-divisible group $A_{\mathrm{can}}[p^\infty]$ splits: its parameter is
 $q=1$. Therefore, in this special case, the Serre-Tate theorem \ref{thm:2.2.4}
 asserts that $q\in
 1+(z-\zeta_{\mathrm{can}}){\widehat{\Z}^{\mathrm{ur}}}[[z-\zeta_{\mathrm{can}}]]$. It has been
 proved by W. Messing and N. Katz that $q$ is the Dwork-Serre-Tate
 parameter discussed in I.\ref{sub-serre-tate-para}, 
 (\cite{q}, \cite{slm}) --- which explains the terminology.
\end{para}

\begin{para}\label{para:4.2.2} {\it The supersingular case}, \ie
 ${\ovl{A}}[p]({\ovl{\F}}_p)= 0$. 
 
 In this case ${\ovl{\Lambda}}
 =\hat{\ovl{\Lambda}}$ is a so-called Lubin-Tate formal group,
 $\;\End\;{\ovl{\Lambda}}=\mathcal{B}_p$, ``the'' maximal order in 
 the (non-split) quaternion algebra $B_p$ over ${\Q}_p$, and $J=B_p^\times$.
 
 
 Here again, there is a discrete invariant: the ``height'' of the
 quasi-isogeny $\rho$, which amounts to the 
 $p$-adic valuation of the norm of its image in $J=B_p^\times$.
 Therefore 
 \begin{equation*}
  \mathfrak{M}=\coprod_{\Z}\;\mathfrak{M}^0
 \end{equation*}
 is a disjoint sum of copies of a formal scheme $\mathfrak{M}^0$
 which parametrizes deformations of the Lubin-Tate group
 $\hat{\ovl{\Lambda}}$. According to Lubin-Tate, $\mathfrak{M}^0\cong
 \Spf(\mathfrak{v}[[t]])$, with the $(p,t)$-adic topology. The
 associated analytic space $\mathcal{M}^0$ over $\C_p$ is the open unit
 disc $|t|<1$.

 Assume for simplicity that ${\ovl{A}}$ is defined over ${\F}_p$. Then
 one can describe the universal formal deformation $\Lambda$ over
 $\Spf{\Z_p[[t]]}$ through its logarithm $\sum b_n(t)X^{p^{2n}}$, which
 is given recursively by
 \begin{equation*}
  b_0(t)=1,\;b_n(t)=\frac{1}{p}\sum_{0\leq m < n}b_m(t)t_{n-m}^{p^{2m}}
 \end{equation*} 

 
The so-called canonical lifting, corresponding to $t=0$, has formal complex
multiplication by $\Z_{p^2}$, \cf \cite{gross94:_equiv_lubin_tate}, \cite{trapmlsasht}.
\end{para}
