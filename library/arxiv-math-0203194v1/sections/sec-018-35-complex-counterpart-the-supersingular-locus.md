---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-018-35-complex-counterpart-the-supersingular-locus
section_title: "Complex counterpart: the supersingular locus."
section_number: 3.5
pages: 44-47
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.976
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub-complex-supersing}

 Let us now revert things and try to understand the complex situation
 from the $p$-adic viewpoint!

 Let $\matheur{D}^+$ and $\matheur{D}^-$ be the (complex-conjugate)
 connected components of $\matheur{D}(\frac{1}{2},\frac{3}{2}^-)\setminus
 \bigl(\matheur{D}(\frac{-1}{4},\frac{3}{4}^+) \cup
 \matheur{D}(\frac{5}{4},\frac{3}{4}^+)\bigr)$. Let $S$ 
 be the complement of $\matheur{D}^+ \cup \matheur{D}^-$ in the complex plane.
 Note that $S$ is closed and arcwise connected, and that
 $\pi_1^{\mathrm{top}}(S)$ 
 is a free group with two generators $\gamma^+,\gamma^-$ (see figure
 \ref{pic3}). Its 
 interior $S^{\circ}$ has three connected (simply-connected) components
 $\matheur{D}_0= \matheur{D}(\frac{-1}{4},\frac{3}{4}^-),\; \matheur{D}_1=
 \matheur{D}(\frac{5}{4},\frac{3}{4}^-)\;$ and $\matheur{D}_{\infty}$.

\begin{figure}[h]
 \begin{picture}(150,180)(0,0)
  \put(0,0){\includegraphics[clip]{fig8.eps}}
  \put(69,105){$\matheur{D}^{+}$}
  \put(69,30){$\matheur{D}^{-}$}
  \put(175,90){$\matheur{D}_{\infty}$}
  \put(42,82){$\matheur{D}_0$}
  \put(98,82){$\matheur{D}_1$}
  \put(0,58){$-1$}
  \put(55,58){$0$}
  \put(55,66.7){\makebox(0,0)[c]{$\bp$}}
  \put(80,58){$\FRAC{1}{2}$}
  \put(95,58){$1$}
  \put(95,66.7){\makebox(0,0)[c]{$\bp$}}
  \put(138,58){$2$}
  \put(145,108){$\gamma^{+}$}
  \put(150,40){$\gamma^{-}$}
 \end{picture}
 \caption{}
 \label{pic3}
\end{figure}

 Let $\mathcal{O}(S)$ denote the ring of continuous functions on $S$
 analytic in $S^{\circ}$. According to Mergelyan's theorem
 \cite{uatfoacv}, they are uniform limits of rational functions on every
 compact $K\subset S$ such that $\pi_0(\C\setminus K,0)$ is finite.
 This ring is however not stable under differentiation, and we consider
 its differential closure $\mathcal{R}$ in $\mathcal{O}(S^{\circ})$. We
 also consider the integral closure $\mathcal{R}^{\mathrm{et}}$ of
 $\mathcal{R}$ in $\mathcal{O}(S^{\circ})$. Every element of
 $\mathcal{R}^{\mathrm{et}}$ defines a multivalued locally analytic
 function on $S$, \ie an analytic germ which may be analytically
 continued along any path of $S$ not ending at $-1,\frac{1}{2}, 2$, in
 such a way that the germ at the other extremity is analytic.

 For instance, $F(\frac{1}{2},\frac{1}{2},1;z)$ may be viewed as an element
 of $\mathcal{R}^{\mathrm{et}}$: in fact,
 $F(\frac{1}{2},\frac{1}{2},1;z)^4 \in \mathcal{O}(S)$. An explicit
 continuous extension of $F(\frac{1}{2},\frac{1}{2},1;z)^4$ from
 $\matheur{D}_0$ to $S$ is given by $F(\frac{1}{2},\frac{1}{2},1;1-z)^4$
 in $\matheur{D}_1$, $\frac{1}{z^2 }
 F(\frac{1}{2},\frac{1}{2},1;\frac{1}{z})^4$ in $\matheur{D}_{\infty}$,
 and the values
 $\frac{{\Gamma(1/4)}^8}{64\pi^6},\;\frac{{\Gamma(1/4)}^8}{16\pi^6} ,
 \;\frac{{\Gamma(1/4)}^8}{64\pi^6}$ at $-1,\;\frac{1}{2},\;2$
 respectively \cite[p.189]{f2}.  On the other hand, note that $\dlog
 F(\frac{1}{2},\frac{1}{2},1;z)$ is in $\mathcal{R}$ but not
 in $\mathcal{O}(S)$.














































































The de Rham cohomology of the Legendre elliptic pencil gives
rise to an $\mathcal{R}[1/z(1-z)]$-module with connection
$(\mathcal{H},\nabla)$.  It admits a \emph{unique} non-zero horizontal
submodule $\mathcal{U}$ which extends to $S$; we use the same
symbol for the extension. It can be described along the following lines:

\begin{itemize}
 \item For any $u \in (\mathcal{U}\otimes_\mathcal{R}
       {\mathcal{R}^{\mathrm{et}}})^{\nabla}$, ``the'' image of $u$ in
       $\mathcal{O}(\matheur{D}_j) (j=0,1, \text{ or } \infty),$ is a
       bounded solution of the differential operator $L_{\frac{1}{2},\frac{1}{2},1}$.
 \item $\mathcal{U}\otimes_\mathcal{R}
       {\mathcal{R}^{\mathrm{et}}[\frac{1}{z(1-z)}]} =
       \bigl(\mathcal{H}\otimes_{\mathcal{R}[\frac{1}{z(1-z)}]}
       {\mathcal{R}^{\mathrm{et}}[\frac{1}{z(1-z)}]}\bigr)^{\nabla}\otimes_\C
       {\mathcal{R}^{\mathrm{et}}[\frac{1}{z(1-z)}]}.$
 \item $\bigl(\mathcal{H}\otimes_{\mathcal{R}[\frac{1}{z(1-z)}]}
       {\mathcal{R}^{\mathrm{et}}[\frac{1}{z(1-z)}]}\bigr)^{\nabla}$ has a
       canonical ${\Z}[i]$-submodule ($i=\sqrt{-1}$) which can be
       locally identified with the part
       $\mathrm{H}^1(X_z^{\mathrm{an}},{\Z}[i])_{\mathrm{isotriv}}$ of
       $\mathrm{H}^1(X_z^{\mathrm{an}},{\Z}[i])$ where
       $\pi_1^{\mathrm{top}}(S,z)$ acts through a finite group.
 \item $\mathcal{U}|_{\matheur{D}_0}^{\nabla}$ has a
       canonical $\Z$-submodule, which can be identified with the part
       of $\mathrm{H}^1(X_z^{\mathrm{an}},{\Z}[i])_{\mathrm{isotriv}}$ invariant
       under complex conjugation. One of the two generators $u$ satisfies
       \begin{equation*}
	\Lan{\omega,\frac{u}{2i\pi}}=
	 i F\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr)
	 \;\text{ in }\; \mathcal{O}(\matheur{D}_0).
       \end{equation*}
       Similarly, $\mathcal{U}|_{\matheur{D}_1}^{\nabla}$ has a canonical
       $\Z$-submodule, and for one of the two generators $u$, one has
       \begin{equation*}
	\Lan{\omega,\frac{u}{2i\pi}} =
	 i F\Bigl(\frac{1}{2},\frac{1}{2},1;1-z\Bigr)\;\text{ in }\;
	 \mathcal{O}(\matheur{D}_1).
       \end{equation*}
       Note the occurrence of $2i\pi$ in these formulas. 
 \item The local monodromy $\gamma^+$ around $\matheur{D}^+$
       maps \emph{onto}
       \[\Aut \mathrm{H}^1(X_{s},{\Z}[i])_{\mathrm{isotriv}}\simeq
       {\Z}/4{\Z}.\]
       Same for $\gamma^-$.
       The local monodromy at $\infty$ acts as $\pm1$.
 \item In $\matheur{D}^+$ and in $\matheur{D}^-$, there is no non-zero
       bounded analytic solution
       of $L_{\frac{1}{2},\frac{1}{2},1}$.
\end{itemize}


This is quite similar to \subsecref{sub-ordinary-unit-root},
\subsecref{sub-analytic-cont}, $\matheur{D}^+\cup \matheur{D}^-$ playing
the role of the \emph{supersingular locus}. This picture is assuredly
very different from the traditional view of monodromy for
$F(\frac{1}{2},\frac{1}{2},1;z)$, and may shed some light upon the
divergences between the topological and algebraic approaches to analytic
continuation in the $p$-adic case (here of course, the coexistence of
the two pictures is explained by the fact that the principle of unique
continuation (\defref{dfn-unique-cont}) fails for the sheaf
of germs of continuous functions on $S$, analytic on $S^{\circ}$).

The tale of $F(\frac{1}{2},\frac{1}{2},1;z)$ is not finished: we have
not yet explored the islands of supersingularity. We shall reach them in
\subsecref{sub-p-adic-betti-lattice}.

\newpage
