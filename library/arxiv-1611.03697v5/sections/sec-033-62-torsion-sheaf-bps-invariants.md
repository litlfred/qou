---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-033-62-torsion-sheaf-bps-invariants
section_title: "Torsion sheaf BPS invariants"
section_number: 6.2
pages: 30-33
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.966
---
Let $\cA=\Coh_{\leq 1}(X)$ denote the abelian category of coherent sheaves on $X$ supported in dimension $\leq 1$.  Any  sheaf $E\in \cA$ has a Chern character $\ch(E)\in H^*(X,\bZ)$, which via Poincar{\'e} duality we can view as an element
\[\ch(E)=(\beta,n)\in \Gamma=H_2(X,\bZ)\oplus \bZ.\]
We note that for any objects $E_1,E_2$ of $\cA$, the Riemann-Roch theorem tells us that
\[\chi(E_1,E_2)=\sum_{i\in \bZ} (-1)^i \dim_\bC \Ext^i_X(E_1,E_2)=\int_X \ch(E_1)^{\dual}\ch(F)\td(X) =0,\]
because the intersection number of any two curves on a threefold is zero. We therefore take $\<-,-\>$ to be the zero form  on  $\Gamma$. We define a central charge
$Z\colon \Gamma\to \bC$ via the formula \[Z(\beta,n)=2\pi(\beta\cdot \omega_\bC-n),\]
where $\omega_\bC=B+i\omega\in H^2(X,\bC)$ is a complexified K{\"a}hler class.
The assumption that $\omega$ is  K{\"a}hler  ensures that for any nonzero object $E\in \cA$ the complex number $Z(E)\in \bC$ lies in the semi-closed upper half-plane
\[\bar{\cH}= \{z=r\exp(i\pi \phi): r\in \bR_{>0}\text{ and }0<\phi\leq 1\}\subset \bC^*.\]

It follows that $Z$  defines a stability condition on the abelian category $\cA$.
 
For each class $\gamma\in \Gamma$ there is an associated BPS invariant
$\Omega(\gamma)\in \bQ$  first constructed by Joyce and Song (\cite{JS}, see particularly Sections 6.3--6.4). They  are defined using moduli stacks of semistable objects in $\cA$, and should not be confused with the ideal sheaf curve-counting invariants appearing in the famous MNOP conjectures \cite{MNOP}.  Joyce and Song prove that the numbers $\Omega(\gamma)$  are independent of the complexified K{\"a}hler class $\omega_\bC$. This is to be expected, since wall-crossing is trivial when the form $\<-,-\>$ vanishes: see Remark \ref{abelian} below.

A direct calculation \cite[Section 6.3]{JS} shows that
 \begin{equation}\label{montreux}\Omega(0,n)=-\chi(X),\qquad n\in \bZ\setminus\{0\}.\end{equation}
It is expected \cite[Conjecture 6.20]{JS} that when $\beta>0$ is a positive curve class
\begin{equation}
\label{lausanne}
\Omega(\pm \beta,n)=\GV(0,\beta),\end{equation}
and, in particular, is independent of $n$.  We shall assume this in what follows.
 We emphasise that the higher genus Gopakumar-Vafa invariants are invisible from the point-of-view of the  torsion sheaf invariants $\Omega(\gamma)$.
 





\subsection{Formal computation of the $\tau$-function}

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
