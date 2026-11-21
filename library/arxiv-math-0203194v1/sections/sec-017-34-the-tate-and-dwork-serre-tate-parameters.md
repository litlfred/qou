---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-017-34-the-tate-and-dwork-serre-tate-parameters
section_title: "The Tate and Dwork-Serre-Tate parameters."
section_number: 3.4
pages: 43-44
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.98
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub-serre-tate-para}

\begin{para}\label{para-tate-para}
 It turns out that the formal group
 ${\widehat{X}}_{(\widehat{\mathcal{R}_{\mathrm{ord}}^{\mathrm{et}}})}$
 of $X$ over $\widehat{\mathcal{R}_{\mathrm{ord}}^{\mathrm{et}}}$ is
 isomorphic to ${\widehat{\G}}_m$ (\cf~\cite[I]{fgade}). Any such
 isomorphism transforms the canonical differential
 $\omega_{\mathrm{can}}$ on ${\widehat{\G}}_m$ into
 $\Theta \frac{dx}{y}$, for a suitable element $\Theta \in
 \widehat{\mathcal{R}_{\mathrm{ord}}^{\mathrm{et}}}$ well-defined up to
 multiplication by an element of ${\Z}_p^{\times}$. It is possible to
 arrange normalizations so that the following relation hold (loc. cit.):
 
 \begin{equation*}
  \Theta
   = \biggl(\sqrt{-1}F\Bigl(\frac{1}{2},\frac{1}{2},1;\eta\Bigr)\biggr)^{-1}.
 \end{equation*}
 Let $\zeta\in \widehat{{\Z}_p^{\mathrm{ur}}}, \zeta \neq 0,1,$ be a point of
 $S$. By specialization, the element $\Theta(\zeta) \in
 \widehat{{\Z}_p^{\mathrm{ur}}}^{\times}$ (well-defined up to
 ${\Z}_p^{\times}$) links up $\omega_{\mathrm{can}}$ and $\frac{dx}{y}$ on
 $\widehat{X}_{\zeta}\simeq{\widehat{\G}}_m$; it is called the {\it Tate
 parameter} or {\it Tate constant} of $X_{\zeta}$.  It is well-defined
 up to multiplication by an element of ${\Z}_p^{\times}$.

 This is the $p$-adic analogue of the following familiar situation: let
 us consider the two-step uniformization of a complex elliptic curve
 \begin{equation*}
  \C \xrightarrow{\exp\bigl(\frac{2i\pi}{\omega_1}\cdot \;\,\bigr)}
   {\C}^{\times}
   \longrightarrow \C^{\times}/q^{\Z} \simeq
   {\C}/(\omega_1{\Z}+\omega_2{\Z})
 \end{equation*}
 with $q=\exp(2i\pi\frac{\omega_2}{\omega_1})$.  If the elliptic curve
 is $X_{\zeta}$ with $\zeta\in \matheur{D}(0,1^-)\setminus \lbrace
 0\rbrace$, and if $\omega_1$ and $\omega_2$ are fundamental periods of
 $\frac{dx}{y}$ ($\omega_1$ being the period attached to the vanishing
 cycle), then $\frac{2i\pi}{\omega_1}$ appears as the analogue of
 $\Theta(\zeta)$, and it is well-known that $\omega_1/2i\pi =
 iF(\frac{1}{2},\frac{1}{2},1;\zeta)$ (up to sign).
\end{para}

\begin{para}\label{para-dwork-para}
 We come back to the symplectic basis $v_{\ovl{\zeta}}, u_{\ovl{\zeta}}$
 and write $\frac{1}{{\sqrt{-1} F_{\ovl{\zeta}}}} \omega$ in the form
 $v_{\ovl{\zeta}} + \tau u_{\ovl{\zeta}}$, where

 \begin{equation*}
 \tau = -\frac{\an{\omega,v_{\ovl{\zeta}}}}{\an{\omega,u_{\ovl{\zeta}}}}
  \in
  (z-{\zeta_{\mathrm{can}}})\widehat{{\Q}_p^{\mathrm{ur}}}[[z-{\zeta_{\mathrm{can}}}]].
 \end{equation*}
 This defines an unbounded element of
 $\mathcal{O}(\matheur{D}_{{\C}_p}(\zeta_{\mathrm{can}},1^-))$ (notice that
 another choice of $u_{\ovl{\zeta}}$ multiplies $\tau$ by an element of
 $\Z_p^{\times}$).

 \noindent Applying $\nabla(d/dz)$ to
 $\frac{1}{{\sqrt{-1}F_{\ovl{\zeta}}}} \omega = v_{\ovl{\zeta}} + \tau 
 u_{\ovl{\zeta}}$ and using $\lan{\omega,\nabla(\frac{d}{dz})(\omega)} =
 \frac{2}{z(z-1)}$, one derives:
 \begin{equation*}
 \frac{d\tau}{dz} = \frac{2}{z(1-z) F_{\ovl{\zeta}}^2}.
 \end{equation*}
 The exponential of $\tau$ is called the {\it Dwork-Serre-Tate
 parameter}.  We shall recall later its meaning as a parameter for
 $p$-divisible groups. It satisfies
 the following remarkable integrality property \cite[Th.4]{pc}, \cite{tdd}
 \begin{equation*}
 q = e^{\tau} \in 1 + (z-{\zeta_{\mathrm{can}}})
 \widehat{{\Z}_p^{\mathrm{ur}}}[[z-{\zeta_{\mathrm{can}}}]].
 \end{equation*}
 This suggests the following question: does $q$ arise from an element of
 $\widehat{\mathcal{R}_{\mathrm{ord}}^{\mathrm{et}}}\;$? The answer is
 \emph{no}. This may be seen by considering $q\pmod{p}$: the 
 formula for $d\tau/dz = \dlog(q)$ shows that $q\pmod{p}$ is non-constant
 ($\dlog(q) \equiv \frac{2(h_p)^{2/p-1}}{z(z-1)}\pmod{p}$).  If $q$ comes
 from an element of $\widehat{\mathcal{R}_{\mathrm{ord}}^{\mathrm{et}}}$ which
 specializes to $1$ at every canonical modulus $\zeta_{\mathrm{can}}$, one has 
 $q\equiv 1\pmod{p}$, a contradiction.
\end{para}
