---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-037-63-formal-computation-of-the--function
section_title: "Formal computation of the -function"
section_number: 6.3
pages: 31-33
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.993
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
The discussion of the last subsection gives rise to a framed variation of BPS structures  over the complexified K{\"a}hler cone of  $X$, in which the  BPS invariants $\Omega(\gamma)$ are constant.   Let us consider the family of double  structures as defined in Section \ref{double}.
 We can identify
\[\Gamma\oplus\Gamma^\vee=H_*(X,\bZ)\]
equipped with the standard intersection form, and the resulting BPS structures are all uncoupled. 

\begin{remarks}
\begin{itemize}
\item[(i)] We can easily extend this to a miniversal variation if required, by first introducing an extra factor $q\in \bC^*$ rescaling the central charge $Z$, and also adding a component $Z^\dual\colon \Gamma^\vee \to \bC$ as in Section \ref{double}. The resulting central charge is
\[Z((\beta,n),\lambda)=2\pi q(\beta\cdot \omega_\bC-n)+Z^\vee(\lambda).\]
Nothing interesting is gained by doing this however.\smallskip

\item[(ii)]
We view the doubled structures defined here as an approximation to the correct BPS structures, which should also incorporate BPS invariants corresponding to objects of the full derived category $\D^b\Coh(X)$ supported in all dimensions. To define these rigorously would involve constructing stability conditions on $\D^b\Coh(X)$, which for $X$ a general compact Calabi-Yau threefold is a well-known unsolved problem (see \cite{BMS} and \cite{PT} for more on this).
\end{itemize}
\end{remarks}

Although our BPS structures are not finite, we can nonetheless try to solve the associated Riemann-Hilbert problem by superposing infinitely many gamma functions. Let us formally apply \eqref{em} to compute for $g\geq 2$ the coefficient 
\[\sum_{\gamma\in \Gamma}   \frac{\Omega(\gamma)\cdot B_{2g}}{4g(2g-2) } \cdot \frac{1}{Z(\gamma)^{2g-2}}\]
of $(2\pi it)^{2g-2}$ in the asymptotic expansion of the $\tau$-function.\footnote{This calculation was worked out jointly with K. Iwaki.}
The contribution from zero-dimensional sheaves is
\[ - \frac{\chi(X) B_{2g}}{2g(2g-2) (2\pi)^{2g-2}} \cdot\sum_{k\geq 1} \frac{1}{ k^{2g-2}}=
\frac{\chi(X) (-1)^{g-1}B_{2g} \,B_{2g-2} }{4g (2g-2)(2g-2)!},\]
which agrees with \eqref{cons}. The contribution from one-dimensional sheaves is
\begin{equation}\label{blox}\frac{B_{2g}}{2g(2g-2) (2\pi)^{2g-2}} \sum_{\beta>0}\sum_{k\in \bZ}  \frac{\GV(0,\beta) }{    {(v_\beta-k)}^{2g-2}},\end{equation}
where $v_\beta=\omega_\bC\cdot \beta$.
Using the identity
\[ \sum_{k\in \bZ} \frac{1}{(z-k)^{2g-2}}= \frac {(2\pi i)^{2g-2}}{(2g-3)!} \Li_{3-2g}(e^{2\pi i z}),\]
valid for $\Im(z)>0$ and $g\geq 2$, 
we can rewrite \eqref{blox} as
\begin{equation}
\label{greg}
\frac{(-1)^{g-1} B_{2g} }{2g(2g-2)!} \sum_{\beta>0}\GV(0,\beta)\cdot \Li_{3-2g}(e^{2\pi i v_\beta}),\end{equation}
which then agrees with \eqref{blag}.
We conclude that under the variable change
\[\lambda=2\pi it, \quad x_\beta=\exp(2\pi i v_\beta),\]
the $\log$ of the $\tau$-function reproduces the genus 0 degenerate contributions to the Gromov-Witten generating function \eqref{help},
at least for positive powers of $\lambda$. 

\begin{remark}
In the paper \cite{tocome} we give a rigorous solution to the Riemann-Hilbert problem in the case when $X$ is the resolved conifold. This involves writing down a non-perturbative function which has the above asymptotic expansion. \end{remark}
