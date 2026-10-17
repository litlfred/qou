---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-003-13-structure-of-the-proof-of-theorem
section_title: "Structure of the proof of Theorem"
section_number: 1.3
pages: 6-8
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.961
doc_brief: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement — We compute the real part of the semi-classical limit of the sequence of quantum hyperbolic invariants (QHI) of"
---
\label{sec:sketchproof} Let us denote by $PM(N)$ (for \textit{positive monomial}) the set of complex-valued functions of $N$ of the form $$\exp\left (O_{N\to \infty}(1) + \log(N) O_{N\to \infty}(1)\right ).$$
In other words, a function $f(N)$ is in $PM(N)$ if there exist constants $C, C'>0$ and $\alpha,\beta \in \R$ such that
$$ C N^\alpha \leqslant \vert f(N)\vert \leqslant C' N^\beta$$
for any $N$ large enough. 
Consequently, it satisfies $\lim_{N\ra +\infty} \textstyle \frac{2\pi}{N}\Log \left \vert f(N) \right \vert = 0$.

The following basic lemma will be used several times in this paper.
\begin{lem}\label{lem:PM:SE}
Let $f(N)$ and $g(N)$ be functions of $N$ such that $\lim_{N\ra +\infty} \textstyle \frac{2\pi}{N}\Log \left \vert f(N) \right \vert = a > 0$, and $g(N)$ is in $PM(N)$. Then we have
$$\lim_{N\ra +\infty} \dfrac{2\pi}{N}\Log \left \vert g(N)\cdot f(N) \right \vert = a \quad ,\quad  \lim_{N\ra +\infty}  \frac{2\pi}{N}\Log \left \vert f(N) + g(N) \right \vert = a.$$
\end{lem}

\begin{proof}
The first property is immediate. For the second one, note that since $a>0$ we have $\textstyle \frac{1}{2}|f(N)|>|g(N)|$ for any $N$ large enough, and thus $\textstyle \left \vert \vert f(N) \vert - \frac{\vert f(N) \vert}{2} \right \vert \leqslant \left \vert f(N) + g(N) \right \vert \leqslant \left \vert f(N)\right \vert + \vert f(N) \vert  $ by triangle inequalities; the limit follows. 
\end{proof}
\medskip

The proof of Theorem \ref{asyinvteo} takes the following steps I -- X (for the sake of brevity we do not define all the terms that appear in the formulas):
\medskip

\begin{enumerate}[label=\Roman*)]
\item (On the QHI of cusped manifolds, Section \ref{sec:QHIcusped}) This part recalls some features of the invariant $\Hh_{N}(M,\rho,h_\rho,k_c)$, using the structures introduced in Section \ref{NOTA}. In particular, we observe that:
\smallskip

\begin{itemize}
\item (Formula \eqref{splitHNteo1.1}) $\Hh_{N}(M,\rho,h_\rho,k_c)$ can be split into the product of two invariants, $\alpha_N(M,\rho,k_c;\mathfrak{s})$ (the \textit{symmetry defect}) and $\Hh_N^{red}(M,\rho,\kappa;\mathfrak{s})$ (the \textit{reduced QHI}).
\item (Formula \eqref{ssumrednonred}) Refomulating this factorization on the triangulation $(T,b)$ of $M:=S^3\setminus K$ shown in Figure \ref{Teight}, one can write the state sum $\Hh_{N,(T,b,c)}(\bu_N,\bv_N)$ of $\Hh_{N}(M,\rho,h_\rho,k_c)$ (the subject of Theorem \ref{thm:main_triang}) as 
$$\Hh_{N,(T,b,c)}(\bu_N,\bv_N) = (\bu_{0,N}^{-1}\bv_{0,N}^{-1})^{\frac{N-1}{2}}\Hh_{N}^{red}(\bu_{0,N},\bu_{1,N},\bv_{0,N},\bv_{1,N}).$$
\end{itemize}
\smallskip

\item (Getting rid of the symmetry defect, Lemma \ref{lem:lim:sym:defect}) With a quick computation, we check that $\textstyle \lim_{N\ra +\infty} (2\pi/N) \Log \left \vert (\bu_{0,N}^{-1}\bv_{0,N}^{-1})^{\frac{N-1}{2}} \right \vert =0$.
\end{enumerate}
\medskip

These two steps imply that in the proof of Theorem \ref{thm:main_triang} we can replace $\Hh_{N,(T,b,c)}(\bu_N,\bv_N)$ with $\Hh_{N}^{red}(\bu_{0,N},\bu_{1,N},\bv_{0,N},\bv_{1,N})$. From known results it has the factorization formula (\ref{form1}):
$$\Hh_{N}^{red}(\bu_{0,N},\bu_{1,N},\bv_{0,N},\bv_{1,N})   = \frac{g_N(\bu_{0,N})g_N(\bv_{0,N}^*)^*}{|g_N(1)|^2}\ \Sigma_N(\bu_{0,N},\bu_{1,N})\ \Sigma_N(\bv_{0,N}^*,\bv_{1,N}^*)^*.$$
\medskip 

\begin{enumerate}
\item[III)] (Getting rid of $g_N(1)$, $g_N(\bu_{0,N})$ and $g_N(\bv_{0,N}^*)$, Formula (\ref{cstBBP}) and Lemma \ref{factorest}) With quick computations, we establish that $|g_N(1)|=\sqrt{N}$, and thus $g_N(1)$ is in $PM(N)$. Also, by using a uniform estimate of the quantum dilogarithm functions (Lemma \ref{estimatehatS}) we show that in the situation of Theorem \ref{thm:main_triang} the functions $g_N(\bu_{0,N})$ and $g_N(\bv_{0,N}^*)$ are in $PM(N)$.

\end{enumerate}
\medskip

Together with the steps I-II, this further step implies that, in order to prove Theorem \ref{thm:main_triang}, it is enough to show that $\textstyle \lim_{N\ra +\infty} (2\pi/N) \Log \left \vert \Sigma_N(.,.)\right \vert$ is equal to either ${\rm Vol}(M)/2$ (case (a)) or $0$ (case (b)), both for $\Sigma_N(\bu_0,\bu_1)$ and for $\Sigma_N(\bv_{0,N}^*,\bv_{1,N}^*)$. 
\medskip 

\begin{enumerate}
\item[IV)] (Writing $\Sigma_N$ as as an integral, Lemma \ref{lemintrep}) Using properties of the quantum dilogarithm $\hat S_N(.)$, we re-write $\Sigma_N(\bu_{0,N},\bu_{1,N})$ as in formula (\ref{int01}) :
$$\Sigma_N(\bu_{0,N},\bu_{1,N}) = 1 + \frac{1}{\hat S_N(\bl_{0,N})}\sum_{\beta=1}^{N-1} e^{\frac{2\pi i}{N} \beta^2 -\bl_1\beta} \textstyle \hat S_N(\bl_{0,N}+2\beta i\pi/N),$$
where $(\bl_{k,N})$ is a sequence of logarithms of $(\bu_{k,N})$ of a specific form. Using the residue theorem, we re-write this formula as in (\ref{int1}):
$$\Sigma_N(\bu_{0,N},\bu_{1,N}) =1+ \frac{1}{\hat S_N(\bl_{0,N})} \frac{N}{4i\pi}\int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}z)}\hat S_N(\bl_{0,N} + z)\textstyle \coth(\frac{Nz}{2})dz$$
where $C_N$ is a closed rectangular contour circling the segment $\textstyle [\frac{2i\pi}{N}, 2i\pi - \frac{2i\pi}{N}]$ and close to it. We denote by $is_N^-$ and $2i\pi-is_N^+$ its  intersection points with $i\mr$; by construction $\textstyle s_N^\pm:=\alpha^\pm\frac{\pi}{N}$ with $\alpha^\pm\in ]0,2[$.
\smallskip

\item[V)] (Getting rid of $\hat S_N(\bl_{0,N})$, Lemma \ref{factorest}) With properties of the quantum dilogarithms, we establish that $\hat S_N(\bl_{0,N})$ is in $PM(N)$.
\smallskip

\item[VI)] (Equivalence of Theorem \ref{asyinvteo} and Theorem \ref{thm:main_triang}, Section \ref{loglimmars25}) Using the description of the quantum gluing variety in Section \ref{4_1}, we show that the two cases (a) and (b) in Theorem \ref{asyinvteo} correspond to the cases (a) and (b) in Theorem \ref{thm:main_triang}. Moreover, in the above integral these cases correspond to having $\bl_{k,\infty}:= \textstyle \lim_{N\rightarrow +\infty} \bl_{k,N}$ such that $\bl_{0,\infty} = -2i\pi$, $\bl_{1,\infty} = i\pi$, and $\bl_{0,\infty} = -2i\pi$, $\bl_{1,\infty} =2i\pi$ respectively. The same facts occur for $\Sigma_N(\bv_0^*,\bv_1^*)$.
\end{enumerate}
\medskip

We then turn to the semi-classical limit of the integral
\begin{equation}\label{intclejuil25}\int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}z)}\hat S_N(\bl_{0,N} + z)\textstyle \coth(\frac{Nz}{2})dz .
\end{equation}
Somewhat counter-intuitively, we begin with simpler integrals, over the segment $[is_N^-,2i\pi-is_N^+]$ instead of $C_N$, where we fix $\textstyle s_N^-=\alpha^-\frac{\pi}{N}$, $\alpha^-\in ]0,1[$ (whereas $\textstyle s_N^+=\alpha^+\frac{\pi}{N}$ has $\alpha^+\in ]0,2[$ arbitrary), and with integrands defined by using functions $f_{\pm}(z)$, depending on $\bl_{0,\infty}$ and $\bl_{1,\infty}$, which can be regarded as semi-classical approximations of the above integrand when $\bl_{0,\infty}=-2i\pi$ and $\bl_{1,\infty} = i\pi$ or $2i\pi$. 
\begin{enumerate}
\item[VII)] (Saddle point method on a classical integral: contour $[is_N^-,2i\pi-is_N^+]$, case (a): $\bl_{1,\infty} = i\pi$, sections \ref{sub:small:vert:int} and \ref{sub:SPM:a}) In this case we prove that
$$\lim_{N\rightarrow +\infty} \dfrac{2\pi}{N}\Log \left \vert \int_{I_N} e^{\frac{N}{2i\pi} f_{-}(z)}dz \right \vert  = \frac{1}{2}{\rm Vol}(M)\ \ \ {\rm and}\ \ \ \int_{I_N} e^{\frac{N}{2i\pi} f_{+}(z)}dz = O_{N\rightarrow +\infty}(1).$$
\item[VIII)] (Saddle point method on a classical integral: contour $[is_N^-,2i\pi-is_N^+]$,  case (b): $\bl_{1,\infty} = 2i\pi$, sections \ref{sub:small:vert:int} and \ref{sub:SPM:b}) In this case we prove that
$$\int_{I_N} e^{\frac{N}{2i\pi} f_{\pm}(z)}dz  = \dfrac{\text{Constant}_\pm}{\sqrt{N}}(e^{i r_\pm N}+o_{N\to\infty}(1))$$
where $\text{Constant}_-$, $\text{Constant}_+$ are distinct non-zero complex numbers and $r_+,r_-\in \R$ are distinct as well (see \eqref{Cst+}-\eqref{Cst-}).
\smallskip

\item[IX)]  (Lemma \ref{qcintjui25}) We split the contour $C_N$ in its subcontours $C_N^+$, $C_N^-$ lying in the right and left half planes, and we show that the integral \eqref{intclejuil25} is a linear combination of integrals of the form  
$$\int_{C_N^+} e^{\frac{N}{2i\pi} f_{\pm}(z)}\rho(z)\exp\left(\frac{1}{N}{\Psi_{u_0,N}(z)}\right)\left(1+\frac{1}{N}R_N(z)\right) dz,$$
where the functions $f_\pm$ are as in steps VII and VIII, and $\rho(z)$, $\Psi_{u_0,N}(z)$ and $R_N(z)$ are holomorphic functions of $z$ in a domain containing the strip $\mr + i]0,2\pi[$ with some cuts, with moduli bounded by constants independent of $N$ on compact subsets of this strip with cuts. The function $\Psi_{u_0,N}(z)$ measures $\hat S_N(\bl_{0,N} + z)e^{-\frac{N}{2i\pi} f_{\pm}(z)}$; its properties are studied in Lemma \ref{extboundPsiNjanv26}. 

\item[X)]  (Lemma \ref{lem:reformintqjui25} and Corollary \ref{cor:reductionintjui25}) By deforming the contours $C_N^\pm$ to $[is_N^-,2i\pi-is_N^+]$ relatively to the endpoints, one checks that the analysis of steps VII and VIII can be adapted to describe the asymptotics of the integrals of steps IX, and gives similar semi-classical asymptotics. Then, we can deduce easily that
$$ \dfrac{2\pi}{N}\Log \left \vert \int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}z)}\hat S_N(\bl_{0,N} + z)\textstyle \coth(\frac{Nz}{2})dz \right \vert $$
and finally
$$\dfrac{2\pi}{N}\Log \left \vert \Sigma_N(\bu_{0,N},\bu_{1,N}) \right\vert \quad \mathrm{and} \quad \dfrac{2\pi}{N}\Log \left \vert \Sigma_N(\bv_{0,N}^*,\bu_{1,N}^*) \right\vert$$
tend to either ${\rm Vol}(M)/2$ when $\bl_{0,\infty} = -2i\pi$ and $\bl_{1,\infty} = i\pi$ (case (a)), or to $0$ when $\bl_{0,\infty} = -2i\pi$ and $\bl_{1,\infty} =2i\pi$ (case (b)).
\end{enumerate}
By the conclusions of steps III and VI, this will complete the proof.

\begin{remark}{\rm The factorization formula of $\Hh_{N}^{red}(\bu_{0,N},\bu_{1,N},\bv_{0,N},\bv_{1,N})$ in step II is specific to the QHI of $M=S^3\setminus K$. On another hand, the integral representation in step IV immediately generalizes to the QHI state sums of arbitrary cusped manifolds, as well as the steps I, III and V.}
\end{remark}
