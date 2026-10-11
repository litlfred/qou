---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-014-36-some-logarithmic-limits-of-log-parameters
section_title: "Some logarithmic limits of log-parameters"
section_number: 3.6
pages: 34-35
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.819
latex_coverage_ratio: 0.908
---
\label{loglimmars25} In this section we focus on the peculiar logarithmic limits of log-parameters \eqref{deflimlkmars26} selected by the two situations (a)-(b) of Theorem \ref{asyinvteo}. These log-parameters have the form \eqref{recapuvarmars25} (at least for $N$ large enough); that is, they have constant shape parameters $u_k\in \mc_*$ and constant edge colors $a_k\in\mz$. In this situation, and assuming \eqref{situation2}, as usual we put, for $k\in\{0,1\}$:
$$\bl_{k,\infty}^\bu := \lim_{N\ra +\infty} \bl_{k,N}.$$
The edge colors $a_0,a_1,a_2$ solve the linear system \eqref{tetrel41}-\eqref{edgerel41}-\eqref{standardf3}, where $a_0$ is a free variable. Then, taking $a_0$ even and $\geq 2$ if necessary (so that $\textstyle \mathfrak{I}(\Log(u_{0}) +\pi ia_{0})>0$), the assumption \eqref{situation2} implies
\begin{equation}\label{l0inftymars25}
\bl_{0,\infty}^\bu = -2i\pi.
\end{equation}
By the equations \eqref{standardf3} and the comments thereafter, when $a_0$ is positive and big enough, $a_1$ is negative. Then, again by \eqref{situation2}, we have the following alternative:
\begin{equation}\label{l1inftymars25}
\bl_{1,\infty}^\bu = \left \{\begin{matrix}
i\pi & \text{(case} (a): a_1 \ \text{is\ odd}),\\
2i\pi & \text{(case} (b): a_1 \ \text{is\ even}).
\end{matrix}
\right.
\end{equation}
Note that \eqref{l0inftymars25}-\eqref{l1inftymars25} describe the possible limits of the parameters of the integral representation of $\Sigma_N(\bu_{0,N},\bu_{1,N})$ in \eqref{int1}. 

Next consider $\Sigma_N(\bv_{0,N}^*,\bv_{1,N}^*)$. As usual set $\bv_{k,N} := \exp(\bl_{k,N}^\bv)$, $\textstyle \bl_{k,N}^\bv:= \frac{1}{N}(\Log(v_{k}) +\pi ib_{k}) + \pi i b_k$, $\bl_{k,\infty}^\bv := \textstyle \lim_{N\ra +\infty} \bl_{k,N}^\bv$. Then $\textstyle \bl_{k,N}^{\bv^*}= \frac{1}{N}(\Log(v_{k})^* -\pi ib_{k}) - \pi i b_k$, and we consider $\bl_{k,\infty}^{\bv^*} := \textstyle \lim_{N\ra +\infty} \bl_{k,N}^{\bv^*}$ assuming $\mathfrak{I}((\bl_{k,N}^{\bv^*}))$ satisfies \eqref{situation2}. By using the expressions of $b_0$, $b_1$ in the equations \eqref{standardf3}, the same analysis as above shows that, again for $a_0$ even, positive, and big enough, we have
\begin{equation}\label{l01inftymars25}
\bl_{0,\infty}^{\bv^*} = -2i\pi
\quad ,\quad \bl_{1,\infty}^{\bv^*} = \left \{\begin{matrix}
i\pi & \text{(case} (a): a_1 \ \text{is\ odd}),\\
2i\pi & \text{(case} (b): a_1 \ \text{is\ even}).
\end{matrix}
\right.
\end{equation}
These values give the possible limits of the parameters of the integral representation of $\Sigma_N(\bv_{0,N}^*,\bv_{1,N}^*)$.

\begin{lem}\label{rem:reduction:sigma:integral} The two cases (a) and (b) of Theorem \ref{asyinvteo} correspond respectively to the cases (a) and (b) of Theorem \ref{thm:main_triang} and to the cases (a):  $\bl_{0,\infty}^\bx = -2i\pi$, $\bl_{1,\infty}^\bx = i\pi$ and (b): $\bl_{0,\infty}^\bx = -2i\pi$, $\bl_{1,\infty}^\bx = 2i\pi$, for both $\bx = \bu$ and $\bv^*$. 
\end{lem}
\begin{proof} By the equations \eqref{standardf3} the parity of $a_1$ and $b_1$ is the parity of $h_\rho(\lambda_K)/2i\pi$. The conclusion then follows from \eqref{l0inftymars25}-\eqref{l1inftymars25}-\eqref{l01inftymars25}.
\end{proof}
