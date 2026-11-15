---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-074-163-uniformizing-differential-equations
section_title: "Uniformizing differential equations."
section_number: 16.3
pages: 166-167
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.626
latex_coverage_ratio: 0.877
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::4.3}

\begin{para}\label{para::4.3.1} We follow the exposition in \cite[4,
 5.2]{fde} and \cite[4]{aeoaafg}. We now assume that $\ovl{S}$ is a 
complex smooth projective {\it curve}. Then $Z=\{\zeta_0,\ldots
 ,\zeta_n\}$ is just a finite set of points and $S=\ovl{S}\setminus Z$.

 We assume that $\mathcal{S}$ is uniformizable. By Riemann's
 uniformization theorem, the universal orbifold-covering
 $\tilde{\mathcal{S}}$ is then isomorphic to either
 $\P^1, \A^1$ or the open unit disk $\matheur{D}$.  We fix such an
 isomorphism\footnote{in some cases, it will be more 
 convenient to work with $\mathfrak{h}$ instead of $\matheur{D}$.}; the
 group $\Aut 
 \tilde{\mathcal{S}}\;$ is then a Lie subgroup of $PSL_2(\C)$. The
 orbifold fundamental group $\pi_1^{\mathrm{orb}}(\mathcal{S},s)$ is a discrete
 subgroup of $\Aut\, \tilde{\mathcal{S}}$ acting properly on
 $\tilde{\mathcal{S}}$, and the quotient space is
 $\tilde{\mathcal{S}}/\pi_1^{\mathrm{orb}}(\mathcal{S},s)=\ovl{S}$.      
\end{para}

\begin{para}\label{para::4.3.2} We fix a non-constant rational function $z\in
 \C(\ovl{S})$. We shall assume for simplicity that $z$ has no 
 pole on $S$. 

 \noindent Having identified $\tilde{\mathcal{S}}$ with a domain of
 $\P^1$ allows us to consider the canonical map 
 \begin{equation*}
  \tilde S\to \tilde{\mathcal{S}}\subset \P^1
 \end{equation*}
 as an analytic\footnote{in the case $\tilde{\mathcal{S}}=\P^1$,
 it is only meromorphic a priori. But in that case $\ovl{S}=\P^1$ and
 the covering $\P^1\to \P^1$ is finite. It will be convenient to
 normalize things so that $\infty$ lies above $\infty$ and $z$ is the
 standard coordinate on $\P^1$. With this choice, $\tau$ has no pole.} 
 function $\tau$ on $\tilde S$ (in loose terms, this is the multivalued
 inverse of the projection
 $\tilde{\mathcal{S}}\to
 \ovl{S}=\tilde{\mathcal{S}}/\pi_1^{\mathrm{orb}}(\mathcal{S},s)$,
 restricted to $S$). Notice that the derivation 
 $\frac{d}{dz}$ extends canonically to $\mathcal{O}(\tilde S)$. 
\end{para}

\begin{pro}\label{pro::4.3.3} There is a unique differential equation of
 the form
 \begin{equation*}
  y''- qy=0,\;\;\; q\in \C(\ovl{S}),
 \end{equation*}
 the {\rm uniformizing differential equation}, such that $\tau$ is the
 quotient of two solutions in $\mathcal{O}(\tilde S)$ of this
 differential equation. It is fuchsian and has singularities only at
 $Z=\{\zeta_0,\ldots ,\zeta_n\}$.  The monodromy group pointed at $s$ is
 a discrete finitely generated subgroup of $SL_2(\C)$ whose image in
 $PSL_2(\C)$ is $\pi_1^{\mathrm{orb}}(\mathcal{S},s)$.

 \hfill\break If $\ovl{S}=\P^1$ and $\zeta_n=\infty$, the exponents are
 rational numbers given by the Riemann scheme:
 \begin{equation*}
  \begin{pmatrix}
   \zeta_0 & \ldots & \zeta_{n-1} & \zeta_n=\infty \\
   &&&\\
   \frac{1}{2}(1+\frac{1}{e_0})& \ldots &\frac{1}{2}(1+\frac{1}{e_{n-1}})&
   \frac{-1}{2}(1+\frac{1}{e_{n}}) \\
   \\
   \frac{1}{2}(1-\frac{1}{e_0})& \ldots &\frac{1}{2}(1-\frac{1}{e_{n-1}})&
   \frac{-1}{2}(1-\frac{1}{e_{n}}) \\
  \end{pmatrix}.
 \end{equation*}
\cf {\it loc.~cit.}
\end{pro}

\begin{proof}
 Existence: $q$ is nothing but the Schwarz derivative
 \begin{equation*}
  \{\tau, z\}=
   \Bigl(\frac{d\tau}{dz}\Bigr)^{1/2}\frac{d^2}{dz^2}
   \Bigl[\Bigl(\frac{d\tau}{dz}\Bigr)^{-1/2}\Bigr],
 \end{equation*} 
 which is single-valued on $\ovl{S}$. A basis of solutions of the
 uniformizing differential equation is given by
 $(\frac{d\tau}{dz})^{-1/2}$ and $\tau.(\frac{d\tau}{dz})^{-1/2}$. The
 fact that $q\in \C(\ovl{S})$ follows immediately from the invariance of
 the Schwarz derivative under homographic transformations.

 Unicity: this is a purely algebraic fact: $q$ is determined by
 the projective connection attached to the differential equation $y''- qy=0$. 

 The determination of the Riemann scheme comes from this
 expression and the fact that around $\zeta_{i<n}$ (\resp around
 $\infty$) $\tau$ is given by $z-\zeta_i\mapsto c_i.(z-\zeta_i)^{1/e_i} +
 h.o.t.$ (\resp $1/z\mapsto c_n/z^{e_n} + h.o.t.$).
\end{proof}

\begin{rems}
  (i) The case of three singularities
 will be detailed in the next section. In the case of more than three
 singularities, it is extremely difficult in general to write down
 explicitly the uniformizing differential equations.

 (ii) In \cite{fde}, an extension of the theory of
 uniformizing differential equations to higher dimensions is
 developed. Its practical scope seems limited however to the case when
 $\tilde{\mathcal{S}}$ is a symmetric domain.

 (iii) The projective equivalence class of the uniformizing
 differential equation is a variant of what is called the Schwarz
 structure or canonical indigenous $\P^1$-bundle over $\ovl{S}$, \cf 
 \cite{gunning67:_special_rieman}, \cite{mochizuki96}.
\end{rems}
