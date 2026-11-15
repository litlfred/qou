---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-015-32-the-ordinary-unit-root-f-crystal
section_title: "The ordinary unit-root $F$-crystal."
section_number: 3.2
pages: 40-41
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.964
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub-ordinary-unit-root}

On completing $\widehat{{\Z}_p^{\mathrm{ur}}}[z,\frac{1}{{2z(1-z)}}]$
$p$-adically, $(\mathrm{H}^1_{\mathrm{dR}}(X), \nabla)$ gives rise to an
overconvergent $F$-crystal $(\mathcal{H}, \nabla, F)$. We do not discuss
here the construction of the Frobenius structure, which is a general
$p$-adic feature of Gauss-Manin connections. In fact, various analytic
or geometric constructions are available, but in our present case, the
Frobenius structure can be made quite explicit, \cf \cite{pc}.

\medskip
Let us introduce a few notations:
\begin{itemize}
 \item $\mathcal{R}$ = the $p$-adic completion of
       $\widehat{{\Z}_p^{\mathrm{ur}}}\bigl[z,\frac{1}{{h_p(z)}}\bigr]$ 
 \item $\mathcal{R}_{\mathrm{ord}}$ = the $p$-adic completion of
       $\widehat{{\Z}_p^{\mathrm{ur}}}\bigl[z,\frac{1}{{z(1-z)h_p(z)}}\bigr]$
 \item $S=\matheur{M}(\mathcal{R}
       [\frac{1}{p}]) = \matheur{D}(0,1^+) \setminus
       \bigl(\bigcup \matheur{D}(\zeta_j,1^-)\bigr)$
 \item $S_{\mathrm{ord}}=\matheur{M}(\mathcal{R}_{\mathrm{ord}}
       [\frac{1}{p}]) = S\setminus
       \bigl(\matheur{D}(0,1^-)\cup \matheur{D}(1,1^-)\bigr)$
       is the {\it ordinary locus} 
 \item $S_{\mathrm{nss}}= {\A}^1\setminus
       \bigl(\bigcup \matheur{D}(\zeta_j,1^-)\bigr)$
       is the {\it non-supersingular locus}.
\end{itemize}
\noindent The restriction of $(\mathcal{H},\nabla, F)$ to the ordinary
locus possesses a unique non-zero unit-root sub-$F$-crystal
$(\mathcal{U}, \nabla, F)$. This unit-root $F$-crystal extends over $S$
(and even over $S_{\mathrm{nss}}$ as an $F$-isocrystal with logarithmic
singularity at $\infty$ in the sense of \cite{atfff}) \cf also
\cite{ogus00:_ellip}; we use the same
symbol for the extension. It can be described along the following lines:
\begin{itemize}
 \item $\mathcal{U}$ is the unique rank-one horizontal
       submodule of $\mathcal{H}$.
 \item $\mathcal{U}\otimes_{\mathcal{R}_{\mathrm{ord}}}
       \widehat{\mathcal{R}_{\mathrm{ord}}^{\mathrm{et}}} = (\mathcal{H}
       \otimes_{\mathcal{R}_{\mathrm{ord}}}
       \widehat{\mathcal{R}_{\mathrm{ord}}^{\mathrm{et}}})^{\nabla}
       \otimes_{\widehat{{\Z}_p^{\mathrm{ur}}}}
       \widehat{\mathcal{R}_{\mathrm{ord}}^{\mathrm{et}}}.$ (Here
       $\widehat{\mathcal{R}_{\mathrm{ord}}^{\mathrm{et}}}$ is defined
       as in \ref{para:r}.)
 \item for any ordinary $s_0 \in \ovl{\F}_p$, the
       associated $p$-adic representation of
       $\pi_1^{\mathrm{alg}}(S_0,s_0)$ is
       $(\mathcal{H}\otimes_{\mathcal{R}_{\mathrm{ord}}}
       \widehat{\mathcal{R}_{\mathrm{ord}}^{\mathrm{et}}})^{\nabla =0,
       F(\phi)=\id} \simeq \mathrm{H}^1_{\mathrm{et}}(X_{s_0},{\Z}_p).$
 \item For any $u \in (\mathcal{U}\otimes_\mathcal{R}
       \widehat{\mathcal{R}^{\mathrm{et}}})^{\nabla}$, ``the'' image of
       $u$ in $\mathcal{O}(\matheur{D}(s_0,1^-))$ is a bounded solution of the
       differential operator $L_{\frac{1}{2},\frac{1}{2},1}$ on
       $\matheur{D}_{\C_p}(s_0,1^-)$; this also characterizes $\mathcal{U}$.
 \item $\mathcal{U}|_{\matheur{D}(0,1^-)}^{\nabla}$ has a
       canonical $\Z$-submodule, which can be identified with
       $\mathrm{H}^1((X_z)^{\mathrm{an}},{\Z})$ for any $z\in
       \matheur{D}(0,1^-)\setminus \lbrace 0\rbrace$; for a generator
       $u$, one has
       \begin{equation*}
	\an{\omega,u}=\sqrt{-1}F\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr)
	 \text{ in } \mathcal{O}(\matheur{D}(0,1^-))
       \end{equation*}
       ($\sqrt{-1}$ appears as residue of $\frac{dx}{y}\big|_{z=0}$ at
       $x=0$), \cf \cite{pbl}.  Similarly,
       $\mathcal{U}|_{\matheur{D}(1,1^-)}^{\nabla}$ has a canonical
       $\Z$-submodule; for a generator $u$, one has
       \begin{equation*}
	\an{\omega,u} = \sqrt{-1}F\Bigl(\frac{1}{2},\frac{1}{2},1;1-z\Bigr)
	 \text{ in } \mathcal{O}(\matheur{D}(1,1^-)).
       \end{equation*}
\end{itemize}

\noindent The existence of the unit-root $F$-crystal $(\mathcal{U},
\nabla, F)$ over $\mathcal{R}$ then amounts to the two
function-theoretic facts:
\begin{equation*}
 \dlog F\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr)\;\text{ and }\;
 f_p(z) =
 \Bigl(\sqrt{-1}F\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr)\Bigr)^{1-\sigma}
\end{equation*}
both extend to units in $\mathcal{R}$. 

The inertia at any supersingular point maps \emph{onto} $\Aut
\mathrm{H}^1_{\mathrm{et}}(X_{s_0},{\Z}_p)\simeq {\Z}_p^{\times}$ (J.-I. 
Igusa, \cf \eg \cite{anopu}).  The inertia at $\infty$ acts as $\pm1$.
According to Crew's criterion, the $F$-crystal $(\mathcal{U},\nabla,F)$
is \emph{not} overconvergent.

We refer to \cite{opm} for a study in the same spirit of more general
hypergeometric equations and other differential equations ``coming from
geometry''.
