---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-086-186-a-triadic-analogue-of-gauss-formula-and-spec
section_title: "A triadic analogue of Gauss' formula, and special values of $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; z)$ at CM points."
section_number: 18.6
pages: 208-211
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.944
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::6.6}


\begin{para}\label{para::6.6.1} For our hypergeometric function, Gauss'
 formula reads
 \begin{equation*}
  F\Bigl(\frac{1}{24}, \frac{7}{24},\frac{5}{6};1\Bigr)=
 \frac{\Gamma(\frac{5}{6})\Gamma(\frac{1}{2})}
 {\Gamma(\frac{19}{24})\Gamma(\frac{13}{24})}.
 \end{equation*}

\noindent If one considers $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6};
 z)$ as a multivalued analytic function on
 $\P^1\setminus\{0,1,\infty\}$, the values at $1$ generate a
 $\ovl{\Q}$-subspace of $\C$ of dimension $\leq 2$, namely:  
\begin{equation*}
 \frac{\Gamma(\frac{5}{6})\Gamma(\frac{1}{2})}
  {\Gamma(\frac{19}{24})\Gamma(\frac{13}{24})}\ovl{\Q} \,+ \,
  \frac{\Gamma(\frac{5}{6})\Gamma(-\frac{1}{2})}
  {\Gamma(\frac{1}{24})\Gamma(\frac{7}{24})}\ovl{\Q}.
\end{equation*}
Similarly, its values at $\infty$ generate the $\ovl{\Q}$-subspace 

\begin{equation*}
 \frac{\Gamma(\frac{5}{6})\Gamma(\frac{1}{4})}
  {\Gamma(\frac{19}{24})\Gamma(\frac{7}{24})}\ovl{\Q} \, +\,
  \frac{\Gamma(\frac{5}{6})\Gamma(-\frac{1}{4})}
  {\Gamma(\frac{1}{24})\Gamma(\frac{13}{24})}\ovl{\Q}.
\end{equation*}   
\end{para}

\begin{para}\label{para::6.6.2} Let us consider our hypergeometric
 function as a triadic function $F(\frac{1}{24},
 \frac{7}{24},\frac{5}{6}; 1)_3$, and more precisely as a multivalued
 $3$-adic analytic function on a suitable finite \'etale covering of
 $\P^1\setminus\{0,1,\infty\}$. 
 
 The values taken by $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; z)_3$ at
 $1$ belong to $\ovl{\Q}$: this follows from \ref{para::5.6.3}, together
 with the fact that the ``periods'' (in the sense of
 I.\ref{sub-p-adic-betti-lattice-supersing}) attached to the 
 abelian surface with complex multiplication by $M_2(\Q[\sqrt{-24}])$ 
 parametrized by $z=1$, belong to $\ovl{\Q}$, by I.\ref{para-ramif}, 
 I.\ref{thm-cm-period}. 

 \medskip In the same way, one shows that the values taken by
 $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; z)_3$ at $\infty$ belong to 
 $(\Gamma_3(\frac{3}{4})/\Gamma_3(\frac{1}{4}))^{-1/2}
 \ovl{\Q}=\Gamma_3(\frac{1}{4})\ovl{\Q}$.
 Conjecture I.\ref{coj-no-complex-multi} predicts that
 $\Gamma_3(\frac{1}{4})$ is a transcendental number.
\end{para}

\begin{para}\label{para::6.6.3} In \cite[Table 2]{elkies98:_shimur}, one finds a
 table of rational CM points $z$ (rational points which correspond to
 abelian surfaces with complex multiplication by an order in
 $M_2(\Q(\sqrt{-d}))$ for some fundamental discriminant $-d$); with the
 notation of {\it loc.~cit.}, they are given by $z=B/(B-A)= \pm B /|
 C|$. Some of them are: 

\vspace{5mm}
\begin{center}
 \renewcommand{\arraystretch}{1.2}
 \begin{tabular}{c @{\quad\qquad}l}
 $ z            $ & $ d=-\mathrm{disc}   $ \\ \hline 
 $ -3^3/2^2 7^2 $ & $ d=2^2.3.7$ \\
 $ -5^3/3^7     $ & $ d=2^3.5  $ \\
 $ 2^{10}/7^4   $ & $ d=3.17   $ \\
 $ -2^{10}/3^7  $ & $ d=19.    $ 
 \end{tabular} 
\end{center}
\vspace{3mm}

 Notice that for the first value of $z$, $F(\frac{1}{24},
 \frac{7}{24},\frac{5}{6}; \frac{-3^3}{2^2 7^2})_3$ converges. Moreover,
 since $(\frac{2^2.7}{3})=+1$, it follows from I.\ref{para-ramif},
 I.\ref{thm-cm-period}, that 
 the triadic ``periods'' attached to the abelian surface $A_{-3^3/ 2^2 7^2}$ 
 with complex multiplication by $M_2(\Q[\sqrt{-d}])$
 parametrized by $z=1$, is algebraic (like the periods of $A_0$). By 
 \ref{para::5.6.3}, it follows that the triadic number
 $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; \frac{-3^3}{2^2 7^2})_3 $ is
 algebraic (can one compute this algebraic number?). 
 
 \medskip 
 On the other hand since
 $\Q(\sqrt{-d})\neq \Q(\sqrt{-3})$ in that case ($d=2^2.3.7 $), the real
 number $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; \frac{-3^3}{2^2 7^2})$
 is transcendental; this follows from Wolfart's theorem 
 \cite{wolfart88:_werteh_funkt}
 (whose proof has been recently completed by work of Cohen-W\"ustholz
 \cite{cohen01:_number_theor} and Edixhoven-Yafaev).

 \medskip It can be proved, a contrario, that if the complex evaluation
 $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; \xi)$ is algebraic for some
 algebraic value $\xi$ in the disc of convergence, then any $p$-adic
 evaluation $F(\frac{1}{24}, \frac{7}{24},\frac{5}{6}; \xi)_p$ which makes
 sense is also algebraic: indeed, by 
 \cite{wolfart88:_werteh_funkt}, \cite{cohen01:_number_theor}, such a
 $\xi$ parametrizes a CM abelian surface by some order in
 $M_2(\Q[\sqrt{-3}])$, and one concludes again using $p$-adic Betti
 lattices as in I.\ref{sub-p-adic-betti-lattice-supersing}.
 
 This is actually a very special case of a general, 
 but conjectural, ``principle of global relations'' for special values of
 solutions of Gauss-Manin connections, \cf \cite{tdmeigdvpdg}.
\end{para}
