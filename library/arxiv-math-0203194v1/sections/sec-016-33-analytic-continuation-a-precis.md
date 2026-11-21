---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-016-33-analytic-continuation-a-precis
section_title: "Analytic continuation: a pr'ecis."
section_number: 3.3
pages: 41-43
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.971
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub-analytic-cont}

\begin{para}
 We have seen that Dwork's hypergeometric function extends to an analytic
 function on the whole of $S_{\mathrm{nss}}$. Some of its special values
 have been computed.  Let us mention \cite{thfwpp}, \cite{anjsasvogphf}
 \begin{enumerate}
 \item $f_p(1)=1$ (Koblitz),
 \item if $p \equiv 1\pmod{4}$,
       \[
       f_p(-1) =
       (-1)^\frac{p-1}{4}\frac{\Gamma_p(1/4)^2}{\Gamma_p(1/2)} =
       \frac{\Gamma_p(1/4)}{\Gamma_p(1/2)\Gamma_p(3/4)} \quad\text{ (Young).}
       \]
 \end{enumerate}
 (the condition $p \equiv 1\pmod{4}$ ensures that $-1$ is an
 ordinary modulus); $f_p(-1)$ is a Gauss integer (Van Hamme).
\end{para}

\begin{para}
 We have seen that the logarithmic derivative
 $\dlog F(\frac{1}{2},\frac{1}{2},1;z) $ also extends to an analytic
 function on $S_{\mathrm{nss}}$.  It satisfies the functional equations
 \begin{align*}
  \dlog F\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr)
   & = -\dlog F\Bigl(\frac{1}{2},\frac{1}{2},1;1-z\Bigr)\\
   & = -\frac{1}{2z} - \frac{1}{z^2}
   \dlog F\Bigl(\frac{1}{2},\frac{1}{2},1;\frac{1}{z}\Bigr).
 \end{align*}
\end{para}

\begin{para}
 Let us turn to the more subtle case of $F(\frac{1}{2},\frac{1}{2},1;z)$
 itself. The general discussion of
 \ref{para-analytic-cont}/\ref{para-unit-root} applies to the ordinary
 unit-root $F$-crystal and tells us that $F(\frac{1}{2},\frac{1}{2},1;z)$
 \emph{admits an extension to any unit disk $\matheur{D}(s,1^-) \subset S$,
 analytic in that disk, and well-defined up to multiplication by a unit
 in ${\Z}_p$}. In other words, $\;F(\frac{1}{2},\frac{1}{2},1;z)$ is the
 specialization of an element (in fact, a unit) of
 $\widehat{\mathcal{R}^{\mathrm{et}}_{\mathrm{nss}}}$.
 It may be suggestive to denote
 such an element by $\;F(\frac{1}{2},\frac{1}{2},1;\eta)$, where $\eta$
 stands for the Berkovich generic point of $S$ corresponding to the
 sup-norm).

 \noindent In $\matheur{D}(1,1^-)$, this extension is
 $F(\frac{1}{2},\frac{1}{2},1;1-z)$ (up to $\Z_p^{\times}$). The
 refined structure of $F$-isocrystal with logarithmic singularity at
 $\infty$ allows to construct an extension of
 $F(\frac{1}{2},\frac{1}{2},1;z)^2$ to $\matheur{D}(\infty,1^-)$,
 analytic in that disk: it is $\frac{1}{z} F(\frac{1}{2},\frac{1}{2},1;\frac{1}{z})^2$ (up to $\Z_p^{\times}$); notice the
 square, which comes from the exponent $\pm 1/2$ at $\infty$.
\end{para}

\begin{para}
 The Krasner representation of $f_p(z)$ and $\dlog
 F(\frac{1}{2},\frac{1}{2},1;z)$ as uniform limits of rational functions
 without pole (nor zero) on $S$ can be made explicit: for $n>0$, let
 $g_n$ be the polynomial obtained by truncating
 $F(\frac{1}{2},\frac{1}{2},1;z)$ at order $p^n-1$; then $f_p(z)= \lim
 (-1)^{\frac{p-1}{2}}\frac{g_{n+1}(z)}{g_n(z^p)}$ and $\dlog
 F(\frac{1}{2},\frac{1}{2},1;z)=\lim\dlog g_n(z)$ \cite[3.4]{pc}.  On
 the other hand, $F(\frac{1}{2},\frac{1}{2},1;z)$ cannot be approximated
 by rational functions on $S$, but $L_{\frac{1}{2},\frac{1}{2},1}(g_n)$
 tends uniformly to $0$ on $\matheur{D}(0,1^+)$ \cite{sbdsdlaafh}.  One
 has

\begin{equation*}
\sqrt{-1}F\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr) \equiv
 \bigl(h_p(z)\bigr)^{-\frac{1}{p-1}}
\pmod{p}
\end{equation*}
but we do not know any explicit representation of 
$F(\frac{1}{2},\frac{1}{2},1;z)$ as a $p$-adic limit of algebraic
functions on $S$.
\end{para}

\begin{para}
 Any solution of $L_{\frac{1}{2},\frac{1}{2},1}$ on an ordinary disk
 $\matheur{D}(s,1^-)$, which is not proportional to (the extended)
 $F(\frac{1}{2},\frac{1}{2},1;z)$, is not bounded in
 $\matheur{D}_{\C_p}(s,1^-)$,
 hence does not extend to neighboring disks in any reasonable
 \emph{analytic} sense. In spite of this obstruction to continuation,
 one can nevertheless ``jump from disk to disk'' (see figure \ref{fig7})
 \begin{figure}[h]
  \begin{picture}(300,100)(0,-10)
   \put(0,0){\includegraphics{fig7.eps}}
   \put(10,0){{\scriptsize $\matheur{D}(\zeta_{\mathrm{can}},1^-)$}}
  \end{picture}
  \caption{}
  \label{fig7}
 \end{figure}
 and extend them as locally analytic functions, in the following way.

 For each $\ovl{\zeta} \in S_0 \setminus \lbrace 0,1\rbrace$,
 there is a {\it canonical lifting} $\;\zeta_{\mathrm{can}} \in
 {\Z}_p^{\mathrm{ur}}$: namely, the modulus $\zeta_{\mathrm{can}}$ for which
 $X_{\zeta_{\mathrm{can}}}$ has complex multiplication by the quadratic
 order $\End(X_{\ovl{\zeta}})$.  Let us fix a branch of
 $F(\frac{1}{2},\frac{1}{2},1;z)$ in
 $\matheur{D}(\zeta_{\mathrm{can}},1^-)$, \ie an analytic solution
 $F_{\ovl{\zeta}}\in \widehat{{\Z}_p^{\mathrm{ur}}}[[z-{\zeta_{\mathrm{can}}}]]$
 of $L_{\frac{1}{2},\frac{1}{2},1}$ in
 $\matheur{D}(\zeta_{\mathrm{can}},1^-)$ which is a specialization of
 $F(\frac{1}{2},\frac{1}{2},1;\eta)\in
 (\widehat{\mathcal{R}^{\mathrm{et}}})^{\times}$ (any other branch is of
 the form $c.F_{\ovl{\zeta}}$ with $c \in {\Z}_p^{\times}$. Let
 $u_{\ovl{\zeta}} \in
 \mathcal{U}|_{\matheur{D}(\zeta_{\mathrm{can}},1^-)}^{\nabla}$ be
 defined by

 \begin{equation*}
 \an{\omega,u_{\ovl{\zeta}}}=\sqrt{-1}F_{\ovl{\zeta}}\;\text{ in }\;
 \mathcal{O}(\matheur{D}({\zeta_{\mathrm{can}}},1^-)).
 \end{equation*}
 On the other hand, let $v_{\ovl{\zeta}} \in
 \mathcal{M}|_{\matheur{D}(\zeta_{\mathrm{can}},1^-)}^{\nabla}$ be defined by
 \begin{equation*}
 \sqrt{-1} F_{\ovl{\zeta}}({\zeta_{\mathrm{can}}}).v_{\ovl{\zeta}}
  = \omega({\zeta_{\mathrm{can}}}),
  \;\text{ so that }\; \an{v_{\ovl{\zeta}},u_{\ovl{\zeta}}}=1.
 \end{equation*}
 Then $\an{\omega,v_{\ovl{\zeta}}}$ defines an
 unbounded solution of
 $L_{\frac{1}{2},\frac{1}{2},1}$ in
 $\matheur{D}_{\C_p}(\zeta_{\mathrm{can}},1^-)$.
\end{para}

\begin{para}
 Finally, in any supersingular disk $\matheur{D}_{{\C}_p}(\zeta_{i},1^-)$,
 there is no non-zero bounded solution of $L_{\frac{1}{2},\frac{1}{2},1}$.
\end{para}
