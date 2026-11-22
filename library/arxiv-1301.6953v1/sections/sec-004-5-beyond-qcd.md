---
doc_id: arxiv-1301.6953v1
doc_title: "Chiral Perturbation Theory and Mesons"
section_id: sec-004-5-beyond-qcd
section_title: "Beyond QCD"
section_number: 5
pages: 8-10
source_pdf: 1301.6953v1.pdf
source_sha256: 8c9231d0832df3b6
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.865
doc_brief: "Chiral Perturbation Theory and Mesons — 7 sections: Front matter; Chiral Perturbation Theory; Introduction"
---
The methods of effective field theory and in particular ChPT can also be
used for extensions. A simple extension is to take QCD with $N$ light
flavours but one can also envisage using $N$ fermions in different
representations of the gauge group. The representations can be complex, real or
pseudo-real so we have in general three generic cases to study for
the spontaneous breaking of the global symmetries \cite{Peskin,Preskill}
\begin{equation}
SU(N)\times SU(N)\to SU(N),\quad
SU(2N)\to SO(2N),\quad
SU(2N)\to Sp(2N)\,.
\end{equation}
The cases correspond to a complex, real and pseudo-real representation for
the $N$ fermions. The global symmetry group in the latter two cases
is $SU(2N)$ since both fermion and antifermion are in the same representation
of the gauge group.
Many one-loop results existed especially for the first case,
the equal mass case has been pushed to two-loop order in
\cite{BL1,BL2,BL3}. The main observation \cite{BL1} is that the whole
machinery developed for ChPT can be brought over with a few simple
modifications to the three cases given above. This allowed us to perform
the calculations for the mass and decay constants \cite{BL1},
meson-meson scattering \cite{BL2} and the electroweak precision
parameters \cite{BL3}. The main idea was that lattice calculation can use
our formulas to extrapolate to the massless case, see e.g. \cite{Buchoff}.

The main trick involved is that in all cases mesons can be described by a
unitary matrix $U=\exp(i\phi^a X^a/(\sqrt{2}F))$ with the $X^a$
a different set of generators for the three cases. All flavour sums in
the equal mass case can be done using the relations
\newcommand{\trfa}[1]{\langle #1\rangle}
\begin{align}

\trfa{X^a A X^a B}&= \trfa{A}\trfa{B}
 -\frac{1}{N_F}\trfa{AB}\,,&
\trfa{ X^a A}\trfa{X^a B}&=
 \trfa{AB}
 -\frac{1}{N_F}\trfa{A}\trfa{B}\,.
\nonumber\\

\trfa{X^a A X^a B}&= \frac{\trfa{A}\trfa{B}}{2}
 +\frac{1}{2}\trfa{AJ_S B^T J_S}-\frac{\trfa{AB}}{2N_F}\,,&
\trfa{ X^a A}\trfa{X^a B}&=
 \frac{1}{2}\trfa{AB}+\frac{1}{2}\trfa{AJ_S B^T J_S}
 -\frac{\trfa{A}\trfa{B}}{2N_F}\,.
\nonumber\\

\trfa{X^a A X^a B}&= \frac{\trfa{A}\trfa{B}}{2}
+\frac{1}{2}\trfa{AJ_A B^T J_A} -\frac{\trfa{AB}}{2N_F}\,,&
\trfa{ X^a A}\trfa{X^a B}&=
 \frac{1}{2}\trfa{AB}-\frac{1}{2}\trfa{AJ_A B^T J_A}
 -\frac{\trfa{A}\trfa{B}}{2N_F}.
\end{align}
The lines are for the complex, real and pseudo-real case and
$J_S=
\left(\begin{array}{cc} 0 & I\\
I & 0\end{array}\right)$, $J_A=
\left(\begin{array}{cc} 0 & -I\\
I & 0\end{array}\right)$.

As an example I quote the results for the vacuum expectation value $\langle\bar q q\rangle$ for all three cases.
\begin{align}
\langle \overline q q\rangle &=
\langle \overline q q\rangle_\mathrm{LO}+
\langle \overline q q\rangle_\mathrm{NLO}+
\langle \overline q q\rangle_\mathrm{NNLO}\,.
\nonumber\\
\langle \overline q q\rangle_\mathrm{LO} &\equiv \sum_{i=1,N_F}
\langle \overline q_{Ri}q_{Li}+\overline q_{Li}q_{Ri}\rangle_\mathrm{LO}
= -N_F B_0 F^2
\nonumber\\
\langle \overline q q\rangle_\mathrm{NLO}
 &= \langle \overline q q\rangle_\mathrm{LO}
\left(a_V \frac{\overline A(M^2)}{F^2}+b_V\frac{M^2}{F^2}\right)\,,
\nonumber\\
\langle \overline q q\rangle_\mathrm{NNLO}
 &= \langle \overline q q\rangle_\mathrm{LO}
\Bigg(c_V \frac{\overline A(M^2)^2}{F^4}
     +\frac{M^2\overline A(M^2)}{F^4}\left(d_V+\frac{e_V}{16\pi^2}\right)
  +\frac{M^4}{F^4}\left(f_V+\frac{g_V}{16\pi^2}\right)\Bigg)\,.
\label{xvev}
\end{align}
I used here 
$M^2 = 2 B_0\hat m$ and $
\overline A(M^2) = -\frac{M^2}{16\pi^2}\log\frac{M^2}{\mu^2}\,.
$ The coefficients appearing are given in Tab.~\ref{tab3}.
Note the similarity between the different results and the existence of
a number of large $n$ relations between the various cases \cite{BL1}.
\begin{table}
\begin{tabular}{|c|c|c|c|}
\hline
 & QCD & Adjoint & 2-colour \\
\hline
$a_V$ & $n-\frac{1}{n}$ & $ n+\frac{1}{2}-\frac{1}{2n}$
 & $ n-\frac{1}{2}-\frac{1}{2n}$\\
$b_V$ & $16 n L_6^r+8 L_8^r +4 H_2^r$& $32 n L_6^r+8 L_8^r +4 H_2^r$
 & $32 n L_6^r+8 L_8^r +4 H_2^r$ \\
$c_V$ & $\frac{3}{2}\left(-1+\frac{1}{n^2}\right)$& $\frac{3}{8}\left(-1+\frac{1}{n^2}-\frac{2}{n}+2n\right)$
 & $\frac{3}{8}\left(-1+\frac{1}{n^2}+\frac{2}{n}-2n\right)$ \\
$d_V$ & $-24\left(n^2-1\right)\,
  \left(L_A+\frac{L_B}{n}\right)$& $-12\left(2n^2+n-1\right)
  \left(2L_A+\frac{L_B}{n}\right)$
 &  $-12\left(2n^2-n-1\right)
  \left(2L_A+\frac{L_B}{n}\right)$\\
$e_V$ & $1-\frac{1}{n^2}$&$\frac{1}{4}\left(1-\frac{1}{n^2}+\frac{2}{n}-2n\right)$
& $\frac{1}{4}\left(1-\frac{1}{n^2}-\frac{2}{n}+2n\right)$ \\
$f_V$ & $48\left(K_{25}^r+n K_{26}^r+n^2 K_{27}^r\right)$& $r^r_{VA}$ 
& $r^r_{VT}$ \\
$g_V$ & $8\left(n^2-1\right)\,
\left(L_A+\frac{1}{n}L_B\right)$& $4\left(2n^2+n-1\right)
  \left(2L_A+\frac{1}{n}L_B\right)$
 & $4\left(2n^2-n-1\right)
  \left(2L_A+\frac{1}{n}L_B\right)$ \\
\hline
\end{tabular}
\caption{\label{tab3} The coefficients appearing 
the corrections to the vacuum-expectation-value for the three generic cases
with $n$ flavours. Table from \cite{BL1}.
We have defined the abbreviations 
 $L_A=L_4^r-2L_6^r$ and
$L_B=L_5^r-2L_8^r$.}
\end{table}
