---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-020-5-asymptotics-of-the-quantum-integral
section_title: "Asymptotics of the quantum integral"
section_number: 5
pages: 47-66
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.672
---
\label{sec:rect:contour}

Recall that in Section \ref{sec:SPM} we defined the functions
\begin{itemize}
\item (case (a), function $f_-$) $\mathcal{L}_-(z;-2i\pi,i\pi) = {\rm Li}_2(e^{z})+z^2 - i\pi z$,
\item (case (a), function $f_+$)  $\mathcal{L}_+(z;-2i\pi,i\pi) = {\rm Li}_2(e^{z})+z^2 +i\pi  z$,
\item (case (b), function $f_-$) $\mathcal{L}_-(z;-2i\pi,2i\pi) = {\rm Li}_2(e^{z})+z^2 - 2i\pi z$,
\item (case (b), function $f_+$) $ \mathcal{L}_+(z;-2i\pi,2i\pi) = {\rm Li}_2(e^{z})+z^2$,
\end{itemize}
and we studied the asymptotics of the integrals $\textstyle \int_{[is_N^-,2i\pi-is_N^+]} e^{\frac{N}{2i\pi} \mathcal{L}_{\pm}(z,-2i\pi,\ell)}dz$ for $\ell=i\pi$ (case (a)) or $\ell=2i\pi$ (case (b)).

In this section we extend this study to obtain asymptotics of the integral on the right side of \eqref{int1}, $\textstyle \int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}z)}\hat S_N(\bl_{0,N} + z)\textstyle \coth(\frac{Nz}{2}) dz$, thus finishing the proof of Theorem \ref{asyinvteo} (see the steps IX and X in Section \ref{sec:sketchproof}).

Because the integrand depends on $N$ in a complicated way, we need a preliminary result, Lemma \ref{qcintjui25} below, to approximate the integral. 

To state this lemma, denote by $C^+_N$ and $C^-_N$ the intersections of the contour $C_N$ (defined in \eqref{choiceCN}) with the right and left half-spaces; see Figure \ref{fig:contours:CN+-}. Recall that we assume $\textstyle s_N^- := \alpha \frac{\pi}{N}$ with $\alpha\in ]0,1[$ (see \eqref{sNvalue}), and $s_N^+\in ]0,\textstyle \frac{2\pi}{N}[$. Consider the following shift of the function $\Psi_N$ that we studied in the lemmas \ref{estimatehatS}-\ref{extboundPsiNjanv26}: \begin{equation}\label{defPsiu0N}
{\Psi_{u_0,N}(z)} := \Psi_N\left(\frac{1}{N}\Log(u_{0}) +z\right).
\end{equation}
It is holomorphic on the domain \eqref{holdomPsiN} shifted by $\textstyle -\frac{1}{N}\Log(u_{0})$. Finally, recall the log-parameters ${\bf l}_k' := \Log(u_{k}) +i\pi a_k$ from \eqref{tetcol}, and that the edge colors $a_0,a_1\in \mz$ were specified in Sections \ref{4_1} and \ref{loglimmars25}. Define
\begin{equation}\label{defrho0}
\rho(z) := e^{-\frac{{\bf l}_1'}{2i\pi}z}(1-e^{z})^{-\frac{{\bf l}_0'}{2i\pi}-\frac{1}{2}}.
\end{equation}
Note that our choice of $a_0\geq 2$ makes $\textstyle \mathfrak{R}(\frac{{\bf l}_0'}{2i\pi}+\frac{1}{2}) >0$, so $\rho(z)$ has poles at the points $z\in (2i\pi)\mz$. This will have important consequences in the analysis of the integrals in Lemma \ref{qcintjui25}, which will be done in Lemma \ref{lem:reformintqjui25}.

\begin{figure}[!h]
\scalebox{.8}{
	\begin{tikzpicture}
		\draw[color=lightgray,->] (-5,0)--(5,0);
		\draw[color=lightgray,->] (0,-1)--(0,6.5);
		\draw (4,-.05) node {\Huge $\cdot$};
		\draw (4,-.25) node {$\varepsilon$};
		
		
		\draw (+.025,-.05) node {\Huge $\cdot$};
		\draw (+.25,-.25) node {$0$};
		\draw (+.025,6-.05) node {\Huge $\cdot$};
		\draw (+.25+.2,6) node {$2 \pi i$};
		\draw (+.025,4.5-.05) node {\Huge $\cdot$};
		\draw (.55+.25+.2,4.5) node {$\textstyle 2\pi i - \frac{2\pi}{N}i$};		
		\draw (+.025,1.5-.05) node {\Huge $\cdot$};
		\draw (.3+.25+.2,1.5) node {$\textstyle \frac{2\pi}{N}i$};	
		
		\draw[color=red,->,thick] (0,1)--(3,1)--(3,5)--(0,5)	;
		\draw[color=blue] (+.025,1-.05) node {\Huge $\cdot$};		
		\draw[color=red] (3.5,3-.3) node {$C^+_N$};		
		\draw[color=red,<-,thick] (0,1)--(-3,1)--(-3,5)--(0,5)	;		
		\draw[color=blue] (+.025,5-.05) node {\Huge $\cdot$};		
		\draw[color=red] (-3.5,3-.3) node {$C^-_N$};
		





		
		
		\draw[color=blue] (-.3,1-.4) node{$i s_N^-$};	

		
		\draw[color=blue] (-.8,5+.3) node{$2\pi i - i s_N^+$};
		
		\draw [color=blue,very thick] (0,1)--(0,5);		
		
	\end{tikzpicture}
	}
	\caption{The contour $C_N$ and its subcontours  $C^+_N$ and $C^-_N$}
	\label{fig:contours:CN+-}
\end{figure}

\begin{lem}\label{qcintjui25} If $\textstyle \bl_{0,\infty} = -2i\pi$ and $\textstyle \bl_{1,\infty} =: \ell\in \{\pi i, 2\pi i\}$ (as in Lemma \ref{rem:reduction:sigma:integral}) we have
	\begin{multline*} \int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}z)}\hat S_N(\bl_{0,N} + z)\textstyle \coth(\frac{Nz}{2}) dz   \\
= \int_{C^+_N} \left( e^{\frac{N}{2i\pi} \mathcal{L}_{-}(z;-2i\pi,\ell)} - u_0 e^{\frac{N}{2i\pi} \mathcal{L}_{+}(z;-2i\pi,\ell)}\right) \rho(z) \exp\left(\frac{1}{N}{\Psi_{u_0,N}(z)}\right) \left(1 + \frac{1}{N}R_N(z)\right) dz \\ -\int_{C^-_N} \left( e^{\frac{N}{2i\pi} \mathcal{L}_{-}(z;-2i\pi,\ell)}  - u_0 e^{\frac{N}{2i\pi} \mathcal{L}_{+}(z;-2i\pi,\ell)}\right)\rho(z)  \exp\left(\frac{1}{N}{\Psi_{u_0,N}(z)}\right) \left(1 + \frac{1}{N}R_N(z)\right) dz\\
= 2\int_{C^+_N} \left( e^{\frac{N}{2i\pi} \mathcal{L}_{-}(z;-2i\pi,\ell)} - u_0 e^{\frac{N}{2i\pi} \mathcal{L}_{+}(z;-2i\pi,\ell)}\right) \rho(z) \exp\left(\frac{1}{N}{\Psi_{u_0,N}(z)}\right) \left(1 + \frac{1}{N}R_N(z)\right) dz,
	\end{multline*}
where the function $R_N$, with formula \eqref{defRNjanv26}, is holomorphic on the domain
\begin{equation}\label{domRN}
\mc \setminus \left(\bigcup_{k\in \mz} \left(2i\pi k  -\frac{1}{N}\Log(u_{0})+[0,+\infty[\right)\bigcup \left(\bigcup_{k\in \mz} \left(2i\pi k +[0,+\infty[\right)\right)\right),
\end{equation}
and $\vert R_N\vert$ is bounded from above by a constant independent of $N$ on any compact subset of a strip $\textstyle \mr + i(2\pi k + [\delta + \frac{\pi}{N}, 2\pi-\delta - \frac{\pi}{N}])$, $\textstyle \delta\in ]0,\pi[$, $k\in \mz$, contained in this domain. 
\end{lem}

\proof \underline{Step 1: Rephrasing $\textstyle  \hat S_N(\bl_{0,N} + z)$.}

Recall from \eqref{recapuvarmars25}-\eqref{situation2}-\eqref{l0inftymars25} that $\textstyle \bl_{0,N}= -2i\pi + \frac{1}{N}(\Log(u_{0}) +\pi ia_{0})$ where $a_0$ is even and $\mathfrak{I}(\Log(u_{0}) +\pi ia_{0})>0$. We can use the functional equation $\textstyle\hat S_{N}(z) = \hat S_{N}(z+\frac{2i\pi}{N})(1-e^{z+\frac{2i\pi}{N}})$ (see \eqref{eqfunchatS}) in order to shift $N-\textstyle \frac{a_0}{2}$ times the argument $\bl_{0,N} + z$: since $\textstyle \bl_{0,N} + z+\frac{2i\pi}{N}(N-\frac{a_0}{2}) = \frac{1}{N}\Log(u_{0}) +z$ we have
\begin{equation}\label{prodShatdec25prooflem51}
\hat S_N(\bl_{0,N} + z) = \hat S_N\left(\frac{1}{N}\Log(u_{0}) +z\right) \prod_{k=1}^{N-a_0/2}\left(1-e^{\bl_{0,N} + z+\frac{2i\pi}{N}k}\right).
\end{equation}


\

\underline{Step 2: Approximating $\textstyle \hat S_N\left(\frac{1}{N}\Log(u_{0}) +z\right)$.}

Let us approximate $\textstyle \hat S_N\left(\frac{1}{N}\Log(u_{0}) +z\right)$. Since  $-\pi < \mathfrak{I}\left(\Log(u_{0})\right)<  \pi$, for every $z\in C_N$ we have
\begin{equation}\label{stripjuil25}
-\frac{\pi}{N}+s_N^-\leq \mathfrak{I}\left(\frac{1}{N}\Log(u_{0}) +z\right) \leq 2\pi -s_N^+ + \frac{\pi}{N}.
\end{equation}
We can get finer bounds, depending on $u_0$. Indeed, assume that $\Im(\Log(u_0))$ satisfies 
\begin{equation}\label{uniformu0janv26}
-\pi  \upsilon < \Im(\Log(u_0)) < \pi \upsilon',
\end{equation} where $0<\upsilon,\upsilon'<1$. Let $\upsilon''>0$ be such that $\upsilon'<\upsilon''<1$. Take
\begin{equation}\label{fixsN+-}
\left\lbrace \begin{array}{l} s_N^- := \alpha^- \frac{\pi}{N}, \mathrm{with\ } \alpha^-:= \frac{1+\upsilon}{2},\\ \\ s_N^+ := \alpha^+ \frac{\pi}{N}, \mathrm{with\ } \alpha^+:= 1+\upsilon''.
\end{array}\right.
\end{equation}
Then the inequalities \eqref{stripjuil25} become:
\begin{equation}\label{eq:ineq:u0:depends:on:N}
 0<\frac{(1-\upsilon)\pi}{2N}= \frac{-\pi\upsilon}{N}+s_N^-\leq \mathfrak{I}\left(\frac{1}{N}\Log(u_{0}) +z\right) \leq 2\pi -s_N^+ + \frac{\upsilon'\pi}{N} < 2\pi -\frac{(\upsilon''-\upsilon')\pi}{N}-\frac{\pi}{N}.
\end{equation}
Note that the choices of $\textstyle s_N^-= \alpha^- \frac{\pi}{N}$, with $\alpha^-\in ]0,1[$, and of $\textstyle s_N^+= \alpha^+ \frac{\pi}{N}$, with $\alpha^+\in ]1,2[$, satisfy the assumptions of Section \ref{sec:SPM} (see \eqref{sNvalue}); moreover $\textstyle \alpha^-= \frac{1+\upsilon}{2}$ ensures that strips like \eqref{eq:ineq:u0:depends:on:N} avoid cuts. The choice of $\alpha^+$, which must lie within $]0,2[$ by the definition of $s_N^+$, in the subinterval $]1,2[$ is relevant only for Remark \ref{sharpdeltaN+-janv26} below.

By Remark \ref{rem:largeN} (ii) we can use  the equality \eqref{equalitylemmaasyoct25}. Taking the exponential we get 
$$\hat S_N\left(\frac{1}{N}\Log(u_{0}) +z\right)  = \exp\left(\frac{N}{2i\pi}{\rm Li}_2\left(e^{\frac{1}{N}\Log(u_{0}) + z}\right)-\frac{1}{2}\Log(1-e^{\frac{1}{N}\Log(u_{0}) + z})+\frac{1}{N}{\Psi_{u_0,N}(z)}\right)$$
where $\textstyle {\Psi_{u_0,N}(z)} = \Psi_N\left(\frac{1}{N}\Log(u_{0}) +z\right)$ (see \eqref{defPsiu0N}). Using that
\begin{align}
{\rm Li}_2\left(e^{\frac{1}{N}\Log(u_{0}) + z}\right)  & = {\rm Li}_2\left(e^z\right) -\frac{\Log(u_{0})}{N}\int_0^1 \Log\left(1-e^{\frac{\Log(u_{0})}{N}t + z}\right)dt\label{approx1dec25}\\
\Log\left(1-e^{\frac{\Log(u_{0})}{N}t + z}\right) & = \Log(1-e^z)- \frac{\Log(u_{0})}{N}e^{z}\int_0^t \frac{e^{\frac{\Log(u_{0})}{N}s}}{1-e^{\frac{\Log(u_{0})}{N}s + z}}ds \notag
\end{align}
we can write
\begin{align*} \hat S_N\left( \frac{1}{N}\Log(u_{0}) +z\right)   & =  \exp\left(\frac{N}{2i\pi}{\rm Li}_2\left(e^{z}\right)\right) \exp\left({\mathcal{T}_{u_0,N}(z)}+\frac{1}{N}{\Psi_{u_0,N}(z)}\right)\\ & = \exp\left(\frac{N}{2i\pi}{\rm Li}_2\left(e^{z}\right)\right) \exp\left(-\frac{1}{2}\left(1+\frac{\Log(u_0)}{i\pi}\right)\Log(1-e^{z})\right)\\ &  \hspace*{5cm} \times \exp\left(\frac{1}{N}\left({\Psi_{u_0,N}(z)}+
	{\mathcal{I}_{u_0,N}(z)}\right)\right),
\end{align*}
where 
\begin{align*} 
{\mathcal{T}_{u_0,N}(z)}
&:=  - \frac{N}{2i\pi}{\rm Li}_2\left(e^{z}\right)
+\frac{N}{2i\pi}{\rm Li}_2\left(e^{\frac{1}{N}\Log(u_{0}) + z}\right)-\frac{1}{2}\Log(1-e^{\frac{1}{N}\Log(u_{0}) + z})
\\
	&= -\frac{1}{2}\Log\left(1-e^{\frac{1}{N}\Log(u_{0}) + z}\right) -\frac{\Log(u_{0})}{2i\pi}\int_0^1 \Log\left(1-e^{\frac{\Log(u_{0})}{N}t + z}\right)dt \\  
	&  =
-\frac{1}{2}\left(1+\frac{\Log(u_0)}{i\pi}\right)\Log(1-e^{z})\\ & \hspace*{0.5cm}+\frac{\Log(u_0)}{N}e^z\left(\frac{\Log(u_0)}{2i\pi}\int_0^1\left(\int_0^t \frac{e^{\frac{\Log(u_{0})}{N}s}}{1-e^{\frac{\Log(u_{0})}{N}s + z}}ds\right)dt + \frac{1}{2}  \int_0^1 \frac{e^{\frac{\Log(u_{0})}{N}s}}{1-e^{\frac{\Log(u_{0})}{N}s + z}}ds\right)\\  
&= -\frac{1}{2}\left(1+\frac{\Log(u_0)}{i\pi}\right)\Log(1-e^{z}) + \mathcal{I}_{u_0,N}(z)
\end{align*}
and
$$\mathcal{I}_{u_0,N}(z):=\frac{\Log(u_0)}{N}e^z\left(\frac{\Log(u_0)}{2i\pi}\int_0^1\left(\int_0^t \frac{e^{\frac{\Log(u_{0})}{N}s}}{1-e^{\frac{\Log(u_{0})}{N}s + z}}ds\right)dt + \frac{1}{2}  \int_0^1 \frac{e^{\frac{\Log(u_{0})}{N}s}}{1-e^{\frac{\Log(u_{0})}{N}s + z}}ds\right)$$
is the last summand of $\mathcal{T}_{u_0,N}(z)$ made of the integrals.

By its definition the function ${\mathcal{T}_{u_0,N}(z)}$ is holomorphic on the domain \eqref{domRN}. Then so is ${\mathcal{I}_{u_0,N}(z)}$. Applying several times the triangle inequality on  $\textstyle \vert {\mathcal{I}_{u_0,N}(z)} \vert$, and using Lemma \ref{lem:bound:exp:1-exp} as at the end of Lemma \ref{estimatehatS}, we find
\begin{equation}\label{majorjanv26_2} \vert {\mathcal{I}_{u_0,N}(z)}\vert  \leq  \dfrac{B_M}{\delta\sqrt{1- \frac{\pi^2}{24}}}
\end{equation}
for every $\textstyle z\in ]-\infty,M] + i(2\pi k + [\delta+\frac{\pi}{N}, 2\pi-\delta - \frac{\pi}{N}])$, $\textstyle \delta\in ]0,\pi[$, $k\in \mz$ (so that $\textstyle \delta \leq \mathfrak{I}\left(\frac{1}{N}\Log(u_{0})s +z\right) \leq 2\pi -\delta$ for every $s\in [0,1]$), where $B_M>0$ is a constant independent of $N$, $\delta$ and $k$.


\

\underline{Step 3: Approximating $\textstyle \prod_{k=1}^{N-a_0/2}\left(1-e^{\bl_{0,N} + z+\frac{2i\pi}{N}k}\right)$.}

Next consider the product in \eqref{prodShatdec25prooflem51}. By factoring out 
$a_0/2$
 terms, and using that $\textstyle\bl_{0,N} = -2i\pi + O_{N\ra \infty}(\frac{1}{N})$, for every $z\in C_N$ we get
\begin{align}
\prod_{k=1}^{N-a_0/2}(1-e^{\bl_{0,N} + z+\frac{2i\pi}{N}k}) & =  \prod_{k=1}^{N}(1-e^{\bl_{0,N} + z+\frac{2i\pi}{N}k}) \prod_{k=N+1-a_0/2}^{N}(1-e^{\bl_{0,N} + z+\frac{2i\pi}{N}k})^{-1}\notag\\
& =  (1-e^{N(z+\bl_{0,N})}) \prod_{k=N+1-a_0/2}^{N}\left(1-e^{z+ \frac{1}{N}O_{N\ra \infty}(1)}\right)^{-1} \notag \\
& = (1-u_0 e^{Nz}) \left(1-e^{z+ \frac{1}{N} O_{N\ra \infty}(1)}\right)^{-a_0/2} \notag \\
& = \frac{1-u_0 e^{Nz}}{(1-e^{z})^{a_0/2}} \ .\ \frac{1}{(1-\frac{e^{z}}{e^z-1}\ . \frac{1}{N}O_{N\ra \infty}(1))^{a_0/2}}\notag \\ & = \frac{1-u_0 e^{Nz}}{(1-e^{z})^{a_0/2}} \left(1+ \frac{1}{N}O_{N\ra \infty}\left(1\right)\right), \label{facterrmars25}
\end{align}
where the last $\textstyle O_{N\ra \infty}(1)$ term is a sequence of holomorphic functions on $\mc\setminus \{2i\pi k, k\in \mz\}$, where each singularity $2i\pi k$ is removable, and with moduli bounded from above by some constant independent of $N$ on any fixed compact subset of $\mc$.
\smallskip

\underline{Step 4: Approximating $\textstyle \coth\left(\frac{Nz}{2}\right)$ and $e^{\frac{N}{2i\pi} (z^2 - \bl_{1,N}z)}$.}

Finally, for every $z$ in $\textstyle C_N \setminus \{is_N,2i\pi-is_N - \frac{2i\pi}{N}\}$ we have
$$\coth\left(\frac{Nz}{2}\right) = \mathrm{sign}\left(\mathfrak{R}(z)\right) \left(1+ o_{N\ra \infty}\left(\frac{1}{N}\right)\right),$$ where the $\textstyle o_{N\ra \infty}\left(\frac{1}{N}\right)$ term is a sequence of holomorphic functions on $\C \setminus \{2i\pi k, k \in \Z\}$, where each singularity $2i\pi k$ is a simple pole, and with moduli bounded from above by some constant independent of $N$ on any compact subset of this domain. 

Moreover, since $\textstyle \bl_{1,N}= \frac{1}{N}{\bf l}'_1+\pi i a_1$, with ${\bf l}'_1 =\Log(u_{1}) +\pi ia_{1}$, and $\pi i a_1 = \ell$ mod$(2i\pi)$, with $\ell\in \{\pi i,2\pi i\}$, by the comment after \eqref{int01} for every $z\in C_N$ we can replace $e^{-\frac{N}{2i\pi}\bl_{1,N}z}$ with
$$e^{-\frac{N}{2i\pi}(\frac{1}{N}(\Log(u_{1}) +\pi ia_{1})+\ell) z} = e^{-\frac{1}{2i\pi}(\Log(u_{1}) +\pi ia_{1})z} e^{-\frac{N}{2i\pi}\ell z} = e^{-\frac{{\bf l}'_1}{2i\pi}z} e^{-\frac{N}{2i\pi}\ell z}.$$

\underline{Step 5: Putting all together towards the RHS.}

Recalling the formula \eqref{defrho0}, the approximations we have obtained 
in Steps 2 to 5
imply that for all $z\in C_N$ one has:
\begin{align*}
e^{\frac{N}{2i\pi} (z^2 - \bl_{1,N}z)} & \hat S_N(\bl_{0,N} + z)\textstyle \coth(\frac{Nz}{2}) & \\
& = 
	\mathrm{sign}\left(\mathfrak{R}(z)\right)
	\exp\left(\frac{N}{2i\pi}\left({\rm Li}_2\left(e^{z}\right)+ z^2 - \ell z\right)\right){(1-u_0 e^{Nz})}\\ &\hspace*{4cm} \times \rho(z)    \exp\left(\frac{1}{N}{\Psi_{u_0,N}(z)}\right) \left(1 + \frac{1}{N}R_N(z)\right) 
\\ 
& = \mathrm{sign}\left(\mathfrak{R}(z)\right) 
\left( e^{\frac{N}{2i\pi} \mathcal{L}_{-}(z;-2i\pi,\ell)} - u_0 e^{\frac{N}{2i\pi} \mathcal{L}_{+}(z;-2i\pi,\ell)}\right) \\ & \hspace*{4cm} \times \rho(z)   \exp\left(\frac{1}{N}{\Psi_{u_0,N}(z)}\right) \left(1 + \frac{1}{N}R_N(z)\right),
\end{align*}
where
\begin{equation}\label{defRNjanv26}
1+\frac{1}{N}R_N(z) := \exp\left(\frac{1}{N}{\mathcal{I}_{u_0,N}(z)}\right)\left(1+\frac{1}{N}O_{N\ra \infty}\left(1\right)\right)
{
\dfrac{ \coth\left(\frac{Nz}{2}\right) }{ \mathrm{sign}\left(\mathfrak{R}(z)\right)}
}
\end{equation} satisfies the expected properties (the term $\textstyle \frac{1}{N}O_{N\ra \infty}(1)$ comes from \eqref{facterrmars25}, and recall that $\textstyle \frac{ \coth\left(\frac{Nz}{2}\right) }{ \mathrm{sign}\left(\mathfrak{R}(z)\right)}= \left(1+ o_{N\ra \infty}\left(\frac{1}{N}\right)\right)$
 from Step 5). More precisely, $R_N(z)$ is of the form
$$R_N(z)= \mathcal{I}_{u_0,N}(z)+O_{N\ra \infty}\left(1\right)+o_{N\ra \infty}\left(1\right) +O_{N\ra \infty}\left(\frac{1}{N}\right),$$
where the second, third and fourth terms in the right hand side are of course functions of $z$ as before. Denote by $C^+_N$ and $C^-_N$ the intersections of $C_N$ with the right and left half-spaces. Because of the term $\textstyle \mathrm{sign}\left(\mathfrak{R}(z)\right)$ in the above expressions, we can write
\begin{multline*} \int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}z)}\hat S_N(\bl_{0,N} + z)\textstyle \coth(\frac{Nz}{2}) dz = 
			  \\
\int_{C^+_N} \left( e^{\frac{N}{2i\pi} \mathcal{L}_{-}(z;-2i\pi,\ell)} - u_0 e^{\frac{N}{2i\pi} \mathcal{L}_{+}(z;-2i\pi,\ell)}\right) \rho(z) \exp\left(\frac{1}{N}{\Psi_{u_0,N}(z)}\right) \left(1 + \frac{1}{N}R_N(z)\right) dz\\
		-  \int_{C^-_N} \left( e^{\frac{N}{2i\pi} \mathcal{L}_{-}(z;-2i\pi,\ell)}  - u_0 e^{\frac{N}{2i\pi} \mathcal{L}_{+}(z;-2i\pi,\ell)}\right)\rho(z)  \exp\left(\frac{1}{N}{\Psi_{u_0,N}(z)}\right) \left(1 + \frac{1}{N}R_N(z)\right) dz.
	\end{multline*}
The integrand is holomorphic on the intersection $U$ of the domains \eqref{holdomPsiN} shifted by $\textstyle -\frac{1}{N}\Log(u_{0})$ and the domain \eqref{domRN}. Since $-\pi <\mathfrak{I}(\Log(u_0))< \pi$ one can choose $s_N^-$, $s_N^+$ in \eqref{fixsN+-} so that $s_N^\pm > \textstyle \frac{1}{N} \mathfrak{I}(\Log(u_0))$, and therefore the contours $C^+_N$ and $C^-_N$ are homotopic within $U$ to $[is_N^-,2i\pi-is_N^+]$ relatively to their endpoints, with upwards and downwards orientations respectively. So the opposite of the integral over $C_N^-$ coincides with the integral over $C_N^+$, and the last expression reduces to $2$ times the integral over $C_N^+$ on the RHS. This concludes the proof.\cvd

\begin{remark}\label{sharpdeltaN+-janv26}{\rm We can give sharp uniform bounds on $\vert {\Psi_{u_0,N}(z)}\vert$ for points $z\in C_N$, as follows. Define (with $\upsilon,\upsilon',\upsilon''$ as in \eqref{uniformu0janv26}--\eqref{fixsN+-}):
\begin{align*}
\delta^-_N & := \frac{(1-\upsilon)\pi}{2N} + \frac{\pi}{N},\\
\delta^+_N & := \frac{(\upsilon''-\upsilon')\pi}{N}.
\end{align*}
Then the inequalities \eqref{eq:ineq:u0:depends:on:N} become
\begin{equation}\label{ineqdelta+-janv26}
\delta^-_N - \frac{\pi}{N}\leq \mathfrak{I}\left(\frac{1}{N}\Log(u_{0}) +z\right) \leq 2\pi -\delta^+_N - \frac{\pi}{N},
\end{equation} and thus define strips as in Lemma \ref{estimatehatS} and Remark \ref{rem:largeN} (iii) (with the variable $\textstyle \frac{1}{N}\Log(u_{0}) +z$ in place of $z$). In that lemma take now $M$ equal to the constant $\varepsilon$ used in the definition of the contours $C_N$. Then, by \eqref{UboundPsi}, for every $z$ in the strip \eqref{ineqdelta+-janv26} satisfying  $\textstyle \mathfrak{R}(z)\leq \varepsilon'$ for some $\varepsilon'>\varepsilon$ (so that $\textstyle \mathfrak{R}(\frac{1}{N}\Log(u_{0}) +z)\leq \varepsilon$ for $N$ large enough), we have 
\begin{equation}\label{majorjanv26_1}
\vert {\Psi_{u_0,N}(z)}\vert \leq \frac{B'}{\delta_N^+}+\dfrac{\pi e^{\varepsilon/2}}{2\delta_N^+}\sqrt{1- \frac{\pi^2}{24}}+B'',
\end{equation}
for constants $B',B''>0$ independent of $N$ and of $\delta_N^+$ (note that $\delta_N^+=\min(\delta_N^-,\delta_N^+)$). Since $N\delta_N^+ = \pi (\upsilon''-\upsilon')>0$, \eqref{majorjanv26_1} shows that $\textstyle \frac{1}{N}\vert {\Psi_{u_0,N}(z)}\vert$ is bounded from above by a constant independent of $N$, $\delta_N^-$, and $\delta_N^+$ on any half-strip given by \eqref{ineqdelta+-janv26} and $\textstyle \mathfrak{R}(z)\leq \varepsilon'$.

By Remark \ref{rem:largeN} (i), the bound \eqref{majorjanv26_1} holds true also when $\delta_N^-$ in \eqref{ineqdelta+-janv26} is replaced with any $\delta\in ]0,\pi[$, as long as $\textstyle \frac{1}{N}\Log(u_{0}) +z$ is not contained in a cut of the domain \eqref{holdomPsiN} shifted by $\textstyle -\frac{1}{N}\Log(u_{0})$. In particular we can take $\delta_N^-$ of the form $\delta_N^- = \alpha'\textstyle \frac{\pi}{N}$, with $\alpha'>0$ arbitrary. Since  $N\delta_N^- = \alpha'\pi >0$, as in the proof of Lemma \ref{extboundPsiNjanv26} (ii) we find that $\textstyle \frac{1}{N}\vert {\Psi_{u_0,N}(z)}\vert$ is bounded from above by a constant independent of $N$, $\delta_N^+$, and such a $\delta_N^-$ on any half-strip given by \eqref{ineqdelta+-janv26} and $\textstyle \mathfrak{R}(z)\leq \varepsilon'$.}
\end{remark}

By Lemma \ref{qcintjui25} we have 
\begin{equation}\label{finalestimatefev26}\int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N} z)}\hat S_N(\bl_{0,N} + z)\textstyle \coth(\frac{Nz}{2}) dz =
 2I_{N,-}(\ell) -2u_0  I_{N,+}(\ell),
 \end{equation}
 where
\begin{equation} I_{N,\pm}(\ell)  := \int_{C_N^+} g_N(z)e^{\frac{N}{2i\pi} \mathcal{L}_{\pm}(z;-2i\pi,\ell)} dz,\label{defINpmellfev26}
\end{equation}
and we put
\begin{align}
g_N(z)& := \rho(z) \exp\left(\frac{1}{N}\Psi_{u_0,N}(z)\right)\left(1 + \frac{1}{N}R_N(z)\right)\label{defgNjanv26}\\
& =\rho(z) \exp\left(\frac{1}{N}\Psi_{u_0,N}(z)\right)
\exp\left(\frac{1}{N}\mathcal{I}_{u_0,N}(z)\right)\left(1+\frac{1}{N}O_{N\ra \infty}\left(1\right)\right)
	\dfrac{ \coth\left(\frac{Nz}{2}\right) }{ \mathrm{sign}\left(\mathfrak{R}(z)\right)}.\notag
\end{align}
Lemma \ref{lem:reformintqjui25} below extends to the integrals $I_{N,\pm}(\ell)$ in \eqref{defINpmellfev26} the asymptotics obtained for the integrals in Section \ref{sec:SPM}. The proof requires the following generalizations of Proposition \ref{prop:SPM:PV}; why we need these generalizations is explained before Lemma \ref{lem:reformintqjui25}. First, we will need a special case of Perron's method for a contour starting at a maximum.
\begin{prop} \label{Perronfev26} (i) {\rm (\cite[Theorem 1.2, case of $\mu=1$ and $S=1$]{O'Sul})} Assume that $\lambda$ is a compact piecewise $\mathcal{C}^1$ contour from $z_0$ to $z_1$ in $\mc$, and $f$ and $g$ are holomorphic functions on a domain containing $\lambda$. Assume furthermore that $f'(z_0)\ne 0$, and $\mathfrak{I}(f(z)) < \mathfrak{I}(f(z_0))$ for all $z\in \lambda$, $z\ne z_0$. Then we have 
\begin{equation}\label{1Perronmars26} \int_{\lambda} g(z) e^{n (-i) f(z)} dz = 
e^{n (-i) f(z_0)} \left (\dfrac{g(z_0)}{i f'(z_0)}\dfrac{1}{n}+ O_{n \to \infty}\left(\frac{K_g}{n^2}\right) \right ),
\end{equation} 
where $\textstyle K_g:= \sup_{z\in \lambda \cup \mathcal{B}}\vert g(z)\vert$ and $\textstyle O_{n \to \infty}\left(\frac{K_g}{n^2}\right)\leq C\cdot \frac{K_g}{n^2}$ for a constant $C>0$ independent of $g$ and $n$.\\
(ii) Suppose that the assumptions in (i) on $\lambda$ and $f$ hold, and a sequence of holomorphic functions $(g_n)$ converges uniformly to a function $g$ on a domain containing $\lambda$. Then 
\begin{equation}\label{2Perronmars26}\int_{\lambda} g_n(z) e^{n (-i) f(z)} dz =  e^{n (-i) f(z_0)} \left (\dfrac{g(z_0)}{i f'(z_0)}\dfrac{1}{n}+ o_{n \to \infty}\left(\dfrac{1}{\vert f'(z_0)\vert}\cdot \frac{1}{n}\right) \right ),
\end{equation}
where $\textstyle o_{n \to \infty}\left(\frac{1}{\vert f'(z_0)\vert}\cdot \frac{1}{n}\right) \leq \varepsilon_n \frac{1}{\vert f'(z_0)\vert}\cdot \frac{1}{n}$ for a sequence of real positive numbers $(\varepsilon_n)$ converging to $0$ and independent of $f$ and $n$.\\
(iii) The $\textstyle O_{n \to \infty}$ and $\textstyle o_{n \to \infty}$ error terms in \eqref{1Perronmars26} and \eqref{2Perronmars26} do not depend on $z_0$ when $z_0$ varies in a fixed compact set which does not contain critical points of $f$.
\end{prop}
Note that (iii) says that the expansions \eqref{1Perronmars26} and \eqref{2Perronmars26} are {\it uniform} with respect to $z_0$ in the given range; see \cite[Chapter VII]{W} for the notion of uniform asymptotic expansions.
\medskip

\noindent {\it Proof of (ii) and (iii).} The statement (ii) is a direct consequence of the proof of (i) given in \cite{O'Sul}. Indeed write $g_n = g + (g_n-g)$, and apply (i) to the integrals with integrands $g$ and $g_n-g$. The uniform convergence of $(g_n-g)$ to the $0$ function implies an asymptotic expansion like \eqref{1Perronmars26} for the integral with integrand $g_n-g$, with coefficients $\textstyle \frac{(g_n-g)(z_0)}{i f'(z_0)} $ and $K_{g_n-g}$ arbitrarily close to $0$ as $n\to +\infty$. As there is no assumption on the convergence speed of the sequence $(g_n)$, the error term is only known to be an $\textstyle o_{n \to \infty}\left(\frac{1}{\vert f'(z_0)\vert}\cdot \frac{1}{n}\right)$.\\
For the statement (iii) one uses an estimate of the constant $C$ in (i). Namely, by the equations (3-10) to (3-15) of \cite{O'Sul} in the case $\mu=1$ and $S=1$, we have a lower bound for $C$ of the following form, described below:
\begin{equation}\label{impliedCfev26}
O_{n \to \infty}\left(\frac{K_g}{n^2}\right) \leq \frac{16K_\phi}{\vert f'(z_0)\vert^2}\cdot \frac{K_g}{n^2} +  O_{n \to \infty}\left(K_ge^{-\varepsilon n} \right).
\end{equation}
Here $O_{n \to \infty}\left(K_ge^{-\varepsilon n} \right)\leq C' K_ge^{-\varepsilon n}$, with $C'>0$ a constant bounded by the length of $\lambda$, and $\varepsilon>0$ depends only on the contour $\lambda$ and a constant $R_f(z_0)>0$; precisely, $\varepsilon$ is chosen so that $\mathfrak{I}(f(z)-f(z_0))\leq -\varepsilon$ for all $z$ satisfying $\vert z-z_0\vert \geq R_f(z_0)$ and belonging to a small deformation of $\lambda$, where the deformation occurs in the disk $D(z_0,R_f(z_0)]$ (see the proof of \cite[Proposition 1.3]{O'Sul}). The constant $R_f(z_0)$ is such that the following properties hold (\cite[Proposition 2.1]{O'Sul}): (*)  the solutions $(r,\theta)$ of the equation $\mathfrak{I}(f(z_0+re^{i\theta})-f(z_0))/r=0$ have the form $(r,\theta)=(r,h_k(r))$ when $r$ belongs to on an interval containing $[0, R_f(z_0)]$, where the functions $h_k(r)$, $k\in \{0,1\}$,  are all defined and differentiable, and $\textstyle h_k(0) = -\arg(if'(z_0))+\pi(k+\frac{1}{2})$.\\
Now assume that $z_0$ varies in a compact set $E$ which does not contain critical points of $f$. Then $R_f(z_0)$ as above is defined and can be chosen continuously as a function of $z_0\in E$. We have $\textstyle R_f:= \min_{z_0\in E} (R_f(z_0))>0$, and the above properties (*) hold true uniformly for all $z_0\in E$, replacing $R_f(z_0)$ with $R_f$. Using $R_f$ to define the $\varepsilon>0$ above,  it depends only on the compact set $E$. Also, in \eqref{impliedCfev26} we have (see \cite[equations (2-1) and (3-1)]{O'Sul})
$$K_\phi := \max_{z\in D_{z_0}} \left \vert 1-\frac{f(z)-f(z_0)}{f'(z_0)(z-z_0)}\right\vert,$$
where $D_{z_0}$ is a small closed disk neighborhood of $z_0$.  Then $\textstyle \frac{16K_\phi}{\vert f'(z_0)\vert^2}$ is bounded from above by a constant independent of $z_0\in E$.\\
It follows that the error term $\textstyle e^{n (-i) f(z_0)} O_{n \to \infty}\left(K_g/n^2\right)$ in \eqref{1Perronmars26} is a $\textstyle o_{n \to \infty}$ of the leading order term $\textstyle e^{n (-i) f(z_0)} e^{i \theta} \frac{g(z_0)}{f'(z_0)}\frac{1}{n}$, independent of $z_0\in E$, as claimed.\hfill $\Box$
\medskip

The second generalization of Proposition \ref{prop:SPM:PV} that we will need is for contours passing {\it through} a maximum. It is a classical result that the general form of Perron's method, which generalizes Proposition \ref{Perronfev26} (i), implies Proposition \ref{prop:SPM:PV} (see \cite[Corollary 1.4, case of $\mu=2$ and $k_2=k_1+1$]{O'Sul}). In the situation of a sequence $(g_n)$ converging uniformly to $g$ as in Proposition \ref{Perronfev26} (ii), the proof of this classical result generalizes immediately to give the statement (ii) in the next Proposition. In particular, the arguments show that if we are in the situation of a sequence $(g_n)$ converging to $g$ as in the statement (i), the error term $\textstyle o_{n \to \infty}\left(1/\sqrt{n}\right)$ is in fact a $O_{n \to \infty}\left(1/n\right)$, as stated. We point out this particular case, as it can be found verbatim in the litterature.
\begin{prop}\label{gensaddlen} Keep the same assumptions on the path $\lambda$ and the function $f$ as in Proposition \ref{prop:SPM:PV}.\\
(i) {\rm (\cite[Remark 3.3]{Oh}, \cite[page 145, note of $\S$5]{W})} If there is a neighborhood of the critical point $z_0$ of $f$ where for all $n$ large enough $\textstyle g_n(z) = g(z)+ g_{n,1}(z)\frac{1}{n}$, with $g$ holomorphic and independent of $n$, and $\vert g_{n,1} \vert$ bounded from above by a constant independent of $n$, then we have
$$ \int_{\lambda} g_n(z) e^{n (-i) f(z)} dz = 
e^{n (-i) f(z_0)} \left ( \sqrt{2\pi} e^{i \theta} \dfrac{g(z_0)}{\sqrt{|f''(z_0)|}}\dfrac{1}{\sqrt{n}} + O_{n \to \infty}\left(\frac{1}{n}\right) \right )
$$
for some explicit constant $\theta\in \mr$.\\
(ii) Suppose $(g_n)$ is a sequence of holomorphic functions converging uniformly to a function $g$ on a domain containing $\lambda$. Then we have, with $\theta$ as in (i):
$$ \int_{\lambda} g_n(z)  e^{n (-i) f(z)} dz = e^{n (-i) f(z_0)} \left ( \sqrt{2\pi} e^{i \theta} \dfrac{g(z_0)}{\sqrt{|f''(z_0)|}}\dfrac{1}{\sqrt{n}} + o_{n \to \infty}\left(\frac{1}{\sqrt{n}}\right) \right ).$$
\end{prop}
We now describe in Lemma \ref{lem:reformintqjui25} some asymptotics of the integrals $I_{N,\pm}(\ell)$ in \eqref{defINpmellfev26}. The proof will follow the main lines of the analysis of Section \ref{sec:SPM}. We will use Proposition \ref{Perronfev26} because $\rho(z)$ (and hence $g_N(z)$, see \eqref{defgNjanv26}) has poles at $z=0$ and $z=2i\pi$; indeed, some subintegrals of $I_{N,\pm}(\ell)$, which were negligible in the context of Section \ref{sec:SPM} (by the results of Sections \ref{smallpijuil25}-\ref{smallIsN}), will now dominate its asymptotics in case (b) ($\ell = 2i\pi$). Proposition \ref{gensaddlen} (ii) will play the same role as Proposition \ref{prop:SPM:PV} in Section  \ref{sec:SPM}, to estimate the integrals (where now $g_N$ depends on $N$) on subcontours with endpoints away from $0$ and $2i\pi$. Recall that ${\bf l}_0' := \Log(u_{0}) +i\pi a_0$, and the endpoint $s_N^-$ of $C_N^\pm$ is written as $\textstyle \alpha^-\frac{\pi}{N}$.
\begin{lem}\label{lem:reformintqjui25} For $g_N(z)$ as in \eqref{defgNjanv26} we have
\begin{align*} \lim_{N\to +\infty} \frac{2\pi}{N}\left\vert I_{N,-}(i\pi) \right\vert & = \frac{1}{2}{\rm Vol}(M),\\
\vert I_{N,+}(i\pi) \vert & \sim_{N\to +\infty} \dfrac{N^{\frac{{\bf l}_0'}{2i\pi}-\frac{1}{2}+\frac{\alpha^-}{2}}}{\Log(N)} \left(\frac{1}{\alpha^-\pi}\right)^{\frac{{\bf l}_0'}{2i\pi}+\frac{1}{2}+\frac{\alpha^-}{2}} \vert v_N\vert,\\
\vert I_{N,+}(2i\pi) \vert & \sim_{N\to +\infty} \dfrac{N^{\frac{{\bf l}_0'}{2i\pi}-\frac{1}{2}+\frac{\alpha^-}{2}}}{\Log(N)} \left(\frac{1}{\alpha^-\pi}\right)^{\frac{{\bf l}_0'}{2i\pi}+\frac{1}{2}+\frac{\alpha^-}{2}}\vert v_N\vert,\\ 
\vert I_{N,-}(2i\pi) \vert  & \sim_{N\to +\infty} \dfrac{N^{\frac{{\bf l}_0'}{2i\pi}-\frac{1}{2}+\frac{\alpha^-}{2}}}{\Log(N)} \left(\frac{1}{\alpha^-\pi}\right)^{\frac{{\bf l}_0'}{2i\pi}+\frac{1}{2}+\frac{\alpha^-}{2}} e^{-\alpha^-\pi}\vert v_N\vert, 
\end{align*}
where $(v_N)$  (the same in the last three asymptotic formulas) is a bounded sequence, bounded from below by a constant $>0$, and we choose $a_0\geq 4$ (even, as usual) so that $\textstyle \mathfrak{R}(\frac{{\bf l}_0'}{2i\pi}-\frac{1}{2}) >-\frac{1}{2}$. 
\end{lem}
\medskip

The choice of $a_0\geq 4$ will be explained in Step 6 of the proof. When $a_0=2$ the asymptotics of the integrals $I_{N,+}(i\pi)$, $I_{N,+}(2i\pi)$ and $I_{N,-}(2i\pi)$ depend on the sign of $\mathfrak{I}(\Log(u_0))$; for instance, if it is negative, then $I_{N,+}(2i\pi)$ and $I_{N,-}(2i\pi)$ are of the form in \eqref{asyIjui25c}. The choice $a_0=2$ would not affect the conclusions of the subsequent results.

\begin{remark}{\rm One could worry about the factor $e^{-\alpha^-\pi}$ in the asymptotic formula of $I_{N,-}(2i\pi)$ but not of $I_{N,+}(2i\pi)$; indeed, by \eqref{finalestimatefev26} these formulas combine to give the leading order term as $N\to +\infty$ of the LHS integral for $\ell=\bl_{1,\infty}= 2i\pi$, which does not depend on $\alpha^-$. However, one should be careful that a full asymptotic expansion of this integral is needed to describe it faitfully. In the present situation $I_{N,-}(\ell)$ and $I_{N,+}(\ell)$ emerged from the different asymptotical behaviours of the integrand on the half-spaces $\mathfrak{R}(z)<0$ and $\mathfrak{R}(z)>0$, with terms becoming exponentially small in the former region and exponentially large in the latter (see \eqref{facterrmars25}, and also \eqref{equiv3mars26}). Therefore $\mathfrak{R}(z)=0$ is an anti-Stokes line of the asymptotics of the integrand, and exponentially small terms coming from a full asymptotic expansion of $I_{N,-}(\ell)$ and $I_{N,+}(\ell)$ are required to recover the LHS integral of \eqref{finalestimatefev26} as $N\to +\infty$.}
\end{remark}
\proof \underline{Step 1: Conditions on moving the contours.}\\
We adapt the analysis of Sections \ref{sub:SPM:a} (case (a), $\ell=i\pi$) and \ref{sub:SPM:b} (case (b), $\ell=2i\pi$) to the integrals $I_{N,\pm}(\ell)$. Recall that the integrals in Section \ref{sub:SPM:a}-\ref{sub:SPM:b} have $g_N\equiv 1$ and $C_N^-$ or $C_N^+$ replaced by $[is_N^-,2i\pi-is_N^+]$ (the two being homotopic relatively to their endpoints, with the opposite or the same orientation respectively). 

First we show that the function $g_n:z\mapsto g_N(z)$, $\textstyle n:=\frac{N}{2\pi}$, is holomorphic on a domain where we can deform $C_N^-$ or $C_N^+$ to a contour very close to those in Figure \ref{fig:contour:a:+}, Figure \ref{fig:contour:b:+:perron}, and Figure \ref{fig:contourC':b:+}. In each situation the difference between the two contours will occur on short subcontours close to $0$ or $2i\pi$, where the integrals will have polynomial growth at worst.

These deformations occur in the set $\mathcal{S}_\eta$ formed by the strip $-\eta \leq \mathfrak{I}(z)\leq 2\pi$ with cuts $[0,+\infty[$ and $2i\pi + [0,+\infty[$, where $\eta>0$ is defined in the path $C'_3$ below Figure \ref{fig:contour:b:+:perron}. By definition  $\rho(z)$ and the term $\textstyle O_{N\ra \infty}(1)$ in \eqref{defRNjanv26} are holomorphic on $\mathcal{S}_\eta$. The function $\Psi_{u_0,N}$ is holomorphic on the domain \eqref{holdomPsiN} shifted by $\textstyle -\frac{1}{N}\Log(u_{0})$, and $\mathcal{I}_{u_0,N}$ on \eqref{domRN}, whence the two on $\mathcal{S}_\eta$ minus the two half-lines (the poles $\textstyle -\frac{1}{N}\Log(u_{0})+ 2i\pi+2pi\pi/N$ are not in $S_\eta$ since $-\pi < \mathfrak{I}\left(\Log(u_{0})\right)<  \pi$):
$$ L_1:=  -\frac{1}{N}\Log(u_{0})+[0,+\infty[ \ ,\  L_2:= -\frac{1}{N}\Log(u_{0})+2i\pi + [0,+\infty[.$$
In Figure \ref{fig:contour:b:+:shifted:cuts}, these two shifted cuts are represented with teal half-lines, either dashed or dotted. The dotted part around the y-axis covers the case when $\Re\Log(u_0)>0$. For each of $L_1, L_2$, two copies are drawn, according to the sign of $\Im\Log(u_0)=\arg(u_0)$.\\

\underline{Step 2: Deformed contour in case (b), integral $I_{N,-}(2i\pi)$, or case (a), integral $I_{N,-}(i\pi)$.}\\
Figure \ref{fig:contour:b:+:shifted:cuts} actually expands Figure \ref{fig:contourC':b:+}, so let us justify the shifted cuts are where they seem to be in the corresponding case (case (b), integral $I_{N,-}(2i\pi)$). Recall that we assume that there exists some $\upsilon \in (0,1)$ such that 
$-\upsilon \pi\leq \mathfrak{I}(\Log(u_{0}))\leq \upsilon \pi$
(which makes sense even in a more general case when $u_0$ depends on $N$). In this situation, choosing $\textstyle \alpha^-=\frac{1+\upsilon}{2}$ and  $\textstyle s_N^-=\alpha^-\frac{\pi}{N}$ as in the proof of Lemma \ref{qcintjui25}, we conclude that  $\textstyle \alpha^-> \frac{1}{\pi}\vert \mathfrak{I}(\Log(u_{0})\vert$ and thus $\textstyle s_N^-> \frac{1}{N}\vert \mathfrak{I}(\Log(u_{0})\vert$. 
Hence we can deform $C_N^\pm$ to the contour shown in Figures \ref{fig:contourC':b:+} and \ref{fig:contour:b:+:shifted:cuts} without crossing the cuts $L_1$, $L_2$.

By the same arguments $g_N(z)$ is also holomorphic on a domain where we can deform $C_N^\pm$ to $[is_N^-,is_N^+]$, which is the contour occuring in case (a) for the integral $I_{N,-}(i\pi)$.

\begin{figure}[!h]
	\begin{tikzpicture}
		\begin{scope}[xshift=4cm,yshift=2cm]
			\draw[black,fill=gray!50,opacity=0.5, ] (0,0) circle (2ex); 		
			\draw[black,fill=gray!50,opacity=0.5, ] (-.6,0) circle (2.5ex);  
			\draw[black,fill=gray!50,opacity=0.5, ] (-1.2,0) circle (3ex);  
			\draw[black,fill=gray!50,opacity=0.5, ] (-1.8,0) circle (3.2ex);  
			\draw[black,fill=gray!50,opacity=0.5, ] (-2.4,0) circle (3ex);  
			\draw[black,fill=gray!50,opacity=0.5, ] (-2.9,0) circle (2.7ex);  
			\draw[black,fill=gray!50,opacity=0.5, ] (-3.4,0) circle (1.9ex);  
			\draw[black,fill=gray!50,opacity=0.5, ] (-3.65,0) circle (1.4ex);  
			\draw[black,fill=gray!50,opacity=0.5, ] (-4,0) circle (2ex);
		\end{scope}	
		
		
		\draw[red] (1,3) node {$\Im f_- <0$};		
		\draw[red] (3.2,1.2) node {$\Im f_- <0$};				
		\draw[red] (3,3) node {$\Im f_- >0$};		
		\draw[red] (1,1) node {$\Im f_- >0$};				
		
		
		
		
		
		
		
		\draw[color=black,->] (-2,0)--(8,0);		
		\draw[color=black,->] (0,-2)--(0,5);
		
		
		\draw (2.25+.75,2+.3) node {$b+i\pi$};
		\draw[red,fill=red] (2.25,2) circle (.5ex); 
		
		
		
		\draw (-.25-.2,-.1-.25) node {$0$};
		\draw[red,fill=red] (0,2) circle (.5ex); 
		\draw (-.25-.2,0.3+.2) node {\color{blue}$i s_N^-$};
		\draw[blue,fill=blue] (0,.3) circle (.5ex); 		
		
		
		\draw (-.25-.2,2-.25) node {$i \pi$};
		\draw[red,fill=red] (0,4) circle (.5ex); 
		\draw (-0.9,4-.4) node {\small \color{blue}$2i\pi - i s_N^+$};
		\draw[blue,fill=blue] (0,4-.3) circle (.5ex); 		
		
		
		\draw (-.25-.2,4+.25+.1) node {$2i \pi$};
		\draw[color=red,very thick] (0,2)--(8,2);
		
		
		
		
		
		
		
		
		\draw[color=blue,thick] (0,0)--(0,4);
		\draw[color=red, very thick, dashed] (0,0) ..controls +(3,0) and +(3,0).. (0,4);
		
		
		
		
		
		\draw[red,fill=red] (0,0) circle (.5ex); 
		
		\draw[color=blue,very thick,dashed] (0,0.3)--(4,.3);
		
		\draw (4+.9,0.3+0.2) node {\color{blue}$1+i s_N^-$};
		\draw[blue,fill=blue] (4,.3) circle (.5ex); 	
		
		\draw[color=blue,very thick,dashed] (4,.3)--(4,2-.15);		
		\draw[blue,fill=blue] (4,2-.15) circle (.3ex); 			
		\draw (4+1.1,2-.3) node {\color{blue}\small $1+i (\pi-\epsilon)$};		
		\draw[color=blue,very thick,dashed] (4,2-.15)--(2.4,2-.15)--(2.15,2.15)--(0,2.15);		
		\draw[blue,fill=blue] (0,2+.15) circle (.3ex); 					
		\draw (-.95,2+.3) node {\color{blue}\small $i (\pi+\epsilon)$};		
		
		
		\draw[color=violet , very thick ] (0,0)--(8,0);		
		\draw[color=violet ] (2+6.5,0) node {Cut};
		
		\draw[color=violet , very thick ] (0,0+4)--(8,0+4);		
		\draw[color=violet ] (2+6.5,4) node {Cut};		
		
		\draw[color=teal ,dotted, very thick ] (0-.5,0+.15)--(0+.5,0+.15);			
		\draw[color=teal ,dashed, very thick ] (0+.5,0+.15)--(8,0+.15);		
		\draw[color=teal ] (2+6,+.3+.15) node {\tiny Shifted cut $L_1$ (if $\arg(u_0)<0$)};

		\draw[color=teal ,dotted, very thick ] (0-.5,4+0+.15)--(0+.5,4+0+.15);					
		\draw[color=teal,dashed , very thick ] (0+.5,0+4+.15)--(8,0+4+.15);		
		\draw[color=teal ] (2+6,.3+4+.15) node {\tiny  Shifted cut $L_2$ (if $\arg(u_0)<0$)};
		
		\draw[color=teal ,dotted, very thick ] (0-.5,0-.15)--(0+.5,0-.15);					
		\draw[color=teal ,dashed, very thick ] (0+.5,0-.15)--(8,0-.15);		
		\draw[color=teal ] (2+6,-.3-.15) node {\tiny Shifted cut $L_1$ (if $\arg(u_0)>0$)};
		
		\draw[color=teal ,dotted, very thick ] (0-.5,0+4-.15)--(0+.5,0+4-.15);					
		\draw[color=teal,dashed , very thick ] (0+.5,0+4-.15)--(8,0+4-.15);		
		\draw[color=teal ] (2+6,-.3+4-.15) node {\tiny  Shifted cut $L_2$ (if $\arg(u_0)>0$)};
		
	\end{tikzpicture}
	\caption{The deformed contour of Figure \ref{fig:contourC':b:+} with the shifted cuts}\label{fig:contour:b:+:shifted:cuts}	
\end{figure}
\smallskip

\underline{Step 3: Deformed contour in case (b), integral $I_{N,+}(2i\pi)$.}\\
Consider the situation of Figure \ref{fig:contour:b:+:perron}, expanded upon in Figure \ref{fig:contour:b:+:perron:shifted:cuts} with the shifted cuts $L_1, L_2$. Since $\eta,\eta'>0$ are fixed constants, and $\eta'\geq  s_N^+$ with $\textstyle s_N^+=\alpha^+\frac{\pi}{N}$, $\alpha^+\in ]1,2[$, we have
$\textstyle \alpha^+> \vert \mathfrak{I}(\Log(u_{0}))\vert$ and then $\textstyle \eta'>\vert \frac{1}{N}\mathfrak{I}(\Log(u_{0}))\vert$; we can also take $N$ large enough so that $\textstyle \eta>\vert \frac{1}{N}\mathfrak{I}(\Log(u_{0}))\vert$. Then we can deform $C_N^\pm$ to the contour shown in Figure \ref{fig:contour:b:+:perron} without crossing $L_1$ and $L_2$, except in the case $\mathfrak{R}(\Log(u_{0}))>0$, where  the contour must circumvent $L_1$ in a small subarc $C_a$ close to $0$, joining $-i\eta$ to $i\textstyle s_N^-$ (drawn in dashed black in Figure \ref{fig:contour:b:+:perron:shifted:cuts}). 

\begin{figure}[!h]
	\begin{tikzpicture}
		
		\draw[black,fill=gray!50,opacity=0.5, ] (0,0) circle (2ex); 		
		\draw[black,fill=gray!50,opacity=0.5, ] (-.6,0) circle (2.5ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-1.2,0) circle (3ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-1.8,0) circle (3.2ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-2.4,0) circle (3ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-2.9,0) circle (2.7ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-3.4,0) circle (1.9ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-3.65,0) circle (1.4ex);  
		\draw[black,fill=gray!50,opacity=0.5, ] (-4,0) circle (2ex);
		
		
		\draw[red] (-.5,.8) node {$\Im f_+ >0$};
		\draw[red] (-.5,-.95) node {$\Im f_+ <0$};		
		\draw[red] (-4.5,-1.2) node {$\Im f_+ >0$};		
		\draw[red] (-4,2) node {$\Im f_+ <0$};		
		
		\draw[color=black,->] (-5,0)--(4,0);		
		\draw[color=black,->] (0,-2)--(0,5);
		
		
		
		
		
		
		
		
		\draw (-4-.35,-.3) node {$a$};
		\draw[red,fill=red] (-4,0) circle (.5ex); 
		\draw (-4,+.25+4-.65) node {\small \color{blue} $a+2i\pi-i\eta'$};
		\draw[blue,fill=blue] (-4,4-.7) circle (.3ex); 		
		
		\draw (+.25+.2,-.25) node {$0$};
		\draw[red,fill=red] (0,2) circle (.5ex); 
		\draw (+.25+.2,0.5) node {\color{blue}$i \textstyle s_N^-$};
		\draw[blue,fill=blue] (0,.3) circle (.5ex); 		
		\draw (+.25+.2,2-.25) node {$i \pi$};
		\draw[red,fill=red] (0,4) circle (.5ex); 
		\draw (-.9,4-.4) node {\small \color{blue}$2i\pi - i \textstyle s_N^+$};
		\draw[blue,fill=blue] (0,4-.3) circle (.5ex); 		
		\draw (-.8,4-.95) node {\small \color{blue}$2i\pi - i \eta'$};
		\draw[blue,fill=blue] (0,4-.7) circle (.4ex); 		
		\draw (+.25+.2,4+.25) node {$2i \pi$};
		\draw[color=red,very thick] (0,0)--(-5,0);
		
		
		\draw[color=blue,very thick,dashed] (0,0+4-.7)--(-4,0+4-.7);
		
		
		\draw[color=blue,very thick,dashed ] (-4,0)--(-4,4-.7);
		
		
		\draw[color=blue,thick] (0,0)--(0,4);
		\draw[color=red, very thick, dashed] (-4,0) ..controls +(0,-.5) and +(-1,1).. (0,-2);
		\draw[color=red,very thick, dashed] (-4,0) ..controls +(0,.5) and +(-1,-1).. (0,2);
		\draw[color=red,very thick, dashed] (0,2) ..controls +(1,1) and +(1,-.5).. (0,4);
		\draw[color=red, very thick,dashed] (0,4) ..controls +(-1,.5) and +(1,-.5).. (-1,4.5);
		
		\draw[color=blue , very thick, dashed] (-4,0) ..controls +(0.5,-.3) and +(-.5,0).. (0,-.2-.05);
		\draw[blue,fill=blue] (0,-.2-.05) circle (.4ex); 
		\draw (+.2,-0.5) node {\color{blue}$-i \eta $};		
		
		\draw[red,fill=red] (0,0) circle (.5ex); 
		
		
		\draw[color=violet , very thick ] (0,0)--(8-4,0);		
		\draw[color=violet ] (2+6.5-4,0) node {Cut};
		
		\draw[color=violet , very thick ] (0,0+4)--(8-4,0+4);		
		\draw[color=violet ] (2+6.5-4,4) node {Cut};		
		
		\draw[color=teal ,dotted, very thick ] (0-.5,0+.15)--(0+.5,0+.15);			
		\draw[color=teal ,dashed, very thick ] (0+.5,0+.15)--(8-4,0+.15);		
		\draw[color=teal ] (2+6-4,+.3+.15) node {\tiny Shifted cut $L_1$ (if $\arg(u_0)<0$)};
		
		\draw[color=teal ,dotted, very thick ] (0-.5,4+0+.15)--(0+.5,4+0+.15);					
		\draw[color=teal,dashed , very thick ] (0+.5,0+4+.15)--(8-4,0+4+.15);		
		\draw[color=teal ] (2+6-4,.3+4+.15) node {\tiny  Shifted cut $L_2$ (if $\arg(u_0)<0$)};
		
		\draw[color=teal ,dotted, very thick ] (0-.5,0-.15)--(0+.5,0-.15);					
		\draw[color=teal ,dashed, very thick ] (0+.5,0-.15)--(8-4,0-.15);		
		\draw[color=teal ] (2+6-4,-.3-.15) node {\tiny Shifted cut $L_1$ (if $\arg(u_0)>0$)};
		
		\draw[color=teal ,dotted, very thick ] (0-.5,0+4-.15)--(0+.5,0+4-.15);					
		\draw[color=teal,dashed , very thick ] (0+.5,0+4-.15)--(8-4,0+4-.15);		
		\draw[color=teal ] (2+6-4,-.3+4-.15) node {\tiny  Shifted cut $L_2$ (if $\arg(u_0)>0$)};
		
		\draw[color=black , very thick, dashed] (0,0.3) ..controls +(-1.7,-.3) and +(-.5,0).. (0,-.2-.05);
		
		
	\end{tikzpicture}
	\caption{The deformed contour of Figure \ref{fig:contour:b:+:perron} with the shifted cuts.}\label{fig:contour:b:+:perron:shifted:cuts}
\end{figure}

To be more precise, recall that $a$ is the critical point of $f_+$, and let $r,\upsilon''\in ]0,a[$ be such that $\eta,\upsilon''>r\textstyle >\frac{1}{N}|\Re(\Log(u_0))|$. We define $C_a$ as the concatenation of
\begin{itemize}
\item $C^-_a$, going from $-i\eta$ to $-\upsilon''$, while staying in the domain where $\mathfrak{I}f_+<0$ and $\mathfrak{R}(z)<0$, at a distance $\geq \textstyle r$ from $0$, and avoiding $L_1$ if $\arg(u_0)>0$;
\item $C^{+}_a$, going from $-\upsilon''$ to $is_N^-$, while staying at a distance $\geq \textstyle s_N^-$ from $0$, and avoiding $L_1$ if $\arg(u_0)<0$.
\end{itemize}

See Figure \ref{fig:contour:Ca} for an illustration of this. One should understand Figure \ref{fig:contour:Ca} as a zoomed part of Figure \ref{fig:contour:b:+:perron:shifted:cuts} around the origin.

\begin{figure}[!h]
	\begin{tikzpicture}
		
		\draw[color=black,->] (-6,0)--(2,0);		
		\draw[color=black,->] (0,-3)--(0,2+.3);



	\draw[color=black , very thick, dashed] (-4,0) ..controls +(0.5,-.3) and +(-.5,0).. (0,-2-0.5);
	
				


				\draw[black,fill=black] (-4,0) circle (.4ex); 
\draw (-4,0+.4) node {\color{black}$-\upsilon''$};

			\draw[color=black , very thick, dashed] (-4,0) ..controls +(0.5,.3) and +(-.5,0).. (0,.9);
				\draw[blue,fill=blue] (0,.9) circle (.4ex); 
\draw (+.3+.2,1) node {\color{blue}$i s_N^- $};		
				\draw[blue,fill=blue] (0,-2-.5) circle (.4ex); 
				\draw (+.3+.2,-2-0.5) node {\color{blue}$-i \eta $};		

			
		\draw[color=violet , very thick ] (0,0)--(4,0);		
		\draw[color=violet ] (2+6.5-4,0) node {Cut};
		
		
		\draw[color=teal ,dotted, very thick ] (0-.5,0+.15+.5)--(0+.5,0+.15+.5);			
		\draw[color=teal ,dashed, very thick ] (0+.5,0+.15+.5)--(4,0+.15+.5);		
		\draw[color=teal ] (2+6-4,+.3+.15+.5) node {\tiny Shifted cut $L_1$ (if $\arg(u_0)<0$)};
		
		
		\draw[color=teal ,dotted, very thick ] (0-.5,0-.15-.5)--(0+.5,0-.15-.5);					
		\draw[color=teal ,dashed, very thick ] (0+.5,0-.15-.5)--(8-4,0-.15-.5);		
		\draw[color=teal ] (2+6-4,-.3-.15-.5) node {\tiny Shifted cut $L_1$ (if $\arg(u_0)>0$)};
		
		
		
		\draw[color=black] (-2+.4,-1.1) node {$C_{a}^-$};				
		\draw[color=black] (-2+.4,1.3) node {$C_{a}^{+}$};						
	\end{tikzpicture}
	\caption{The small contour $C_a$, which avoids the shifted cut $L_1$}\label{fig:contour:Ca}	
\end{figure}
\smallskip

Let us compute asymptotics of the integral $I_{N,+}(2i\pi)$ on the subcontours $C_a^-$, $C_a^+$.  
\smallskip

\underline{On the subarc $C_a^-$:} we can use the fact that $\Im(f_+(z))< \Im(f_+(\upsilon''))=0$ for all $z$ in the interior of $C_a^-$. Let us decompose $C_a^-$ into consecutive subarcs $C_a^{--}$, $C_a^{-+}$ with initial endpoint $-i\eta$ and final endpoint $-\upsilon''$ respectively, such that along $C_a^{--}$ we have $\Im(f_+)<-c$ for some $c>0$. Then:
\begin{align}
	\left \vert \int_{C_a^{--}} g_N(z) e^{\frac{N}{2i\pi}\mathcal{L}_+(z,-2i\pi,2i\pi)}dz\right \vert 
	&\leq \max_{C_a^{--}}(|g_N(z)|)
	\int_{C_a^{--}} e^{\frac{N}{2\pi}\Im(f_+(z))}\vert dz\vert \notag\\
	&\leq  \max_{C_a^{--}}(|g_N(z)|)\int_{C_a^{--}} e^{-\frac{N}{2\pi}c}\vert dz\vert = o_{N\to\infty}\left (\frac{1}{{N}}\right ).\label{intCa-Ofev26}
\end{align}
Here we use that $\textstyle |g_N(z)|$ is bounded from above by a constant independent of $N$ on $C_a^-$. Indeed $C_{a}^-$ is compact and stays away from a fixed small disc centered at $0$, so \eqref{defrho0} implies that $\vert \rho(z)\vert$ is bounded from above by a constant independent of $N$ on $C_{a}^-$. The formula of ${\mathcal{I}_{u_0,N}(z)}$ above \eqref{majorjanv26_2} and Lemma \ref{extboundPsiNjanv26} imply this as well for $\textstyle \vert \exp\left(\frac{1}{N}{\mathcal{I}_{u_0,N}(z)}\right)\vert$ and $\textstyle \exp\left(\frac{1}{N}{\Psi_{u_0,N}(z)}\right)$, respectively, and clearly it holds for the term $\textstyle \left(1+\frac{1}{N}O_{N\ra \infty}\left(1\right)\right)\coth\left(\frac{Nz}{2}\right)$ in \eqref{defRNjanv26}. Hence $\textstyle g_N(z) = \rho(z)\exp\left(\frac{1}{N}{\Psi_{u_0,N}(z)}\right)\textstyle (1 + \frac{1}{N}R_N(z))$ has modulus bounded on $C_{a}^-$ by a constant independent of $N$.\\
Along the subarc $C_a^{-+}$ we can apply Proposition \ref{Perronfev26} (ii) with $n=N/2\pi$, $f=f_+$, and $(g_n)$ the sequence $(g_N)$; indeed, $C_a^{-+}$ is a compact subset of $U$, so Lemma \ref{extboundPsiNjanv26} (iii) and the bounds discussed above for $R_N(z)$ imply that $(g_N)$ converges uniformly to $\rho(z)$ on $C_a^{-+}$. We have $\Im(f_+(\upsilon''))=0$,  $f_+'(\upsilon'')\ne 0$, and $\rho(\upsilon'') \ne 0$, so from \eqref{2Perronmars26} we deduce 
$$\left \vert \int_{C_a^{-+}} g_N(z) e^{\frac{N}{2i\pi}\mathcal{L}_+(z,-2i\pi,2i\pi)}dz \right \vert \sim_{N\to +\infty} D\cdot \frac{1}{N}$$
for a scalar $D\ne 0$ (we will not use its actual value). 

\smallskip

\underline{Consider now the subarc $C_a^{+}$.} Unlike in the case of $C_a^-$ above, the function $g_N$ is not bounded on $C_a^+$ since its factor $\rho(z)$ satisfies $\vert \rho(z) \vert \to +\infty$ as $z:=is_N^-\to 0$. Let us see precisely what happens.\\
Part of the above discussion about $C_a^-$ is still true. Namely, by Lemma \ref{extboundPsiNjanv26} (ii) the function $\textstyle \vert \exp\left(\frac{1}{N}{\Psi_{u_0,N}}(z)\right) \vert$ is bounded from above by a constant independent of $N$ and $z\in C_{a^+}$. Also, by the comment after \eqref{facterrmars25} the same is true for obvious reasons for the modulus of the factor $\textstyle \left(1+\frac{1}{N}O_{N\ra \infty}\left(1\right)\right)\coth(Nz/2)$ in \eqref{defgNjanv26}, since $\coth(Nis_N^-/2) = \coth(i\alpha^-\pi/2)$.\\
Consider $\rho(z)$. We claim that, because $z=is_N^-$ is the point of $C_a^+$ which is the closest to the singularity $z=0$ of $\rho(z)$, it is enough to consider the behaviour of $\rho(is_N^-)$. Indeed, we can deform $C_a^+$ slightly upwards near $is_N^-$, so that it reaches a point $i\eta$ with $s_N^-< \eta< \pi$, and then goes vertically to $is_N^-$. By the same arguments as for $C_{a}^-$, $\vert \rho(z) \vert$ is bounded from above by a constant independent of $N$ on the subarc from $-\upsilon''$ to $i\eta$. For $z=it$ on the vertical subarc from $i\eta$ to $is_N^-$, it is readily checked from the formula \eqref{defrho0} that
$$\vert \rho(it) \vert = {\rm (Constant})\cdot \exp\left(-t\left(\frac{\Log\vert u_1\vert}{2\pi}+\frac{\Log\vert u_0\vert}{4\pi}\right)-\frac{\mathfrak{I}({\bf l}_0')+\pi}{2\pi}\cdot\ln(\sin(t/2))\right).$$
Our choice of $a_0\geq 2$ makes $\mathfrak{I}({\bf l}_0'+\pi)/2\pi = \mathfrak{R}(({\bf l}_0'+i\pi)/2i\pi) >0$, and the derivative of $\vert \rho(it) \vert$  is 
$$\left(-\left(\frac{\Log\vert u_1\vert}{2\pi}+\frac{\Log\vert u_0\vert}{4\pi}\right)-\frac{\mathfrak{I}({\bf l}_0')+\pi}{2\pi} {\rm cotan}\left(\frac{t}{2}\right)\right)\cdot\vert \rho(it) \vert,$$
which is negative for $t>0$ and small, as $\textstyle \lim_{t\to 0^+} {\rm cotan}\left(\frac{t}{2}\right) = +\infty$. The maximum of $\vert \rho(it) \vert$ is therefore attained at $\vert \rho(is_N^-)\vert$ on the subarc from $-\upsilon''$ to $i\eta$. This concludes the proof of our claim.\\
Now we have $1-e^{z} = \textstyle \frac{1}{N}O(1)\ne 0$ for every $\textstyle z\sim_{N\to +\infty} \frac{u}{N}$, $u\in \mc^*$, so the formula \eqref{defrho0} implies that $N^{-({\bf l}_0'+i\pi)/2i\pi}\vert \rho(is_N^-)\vert$ has modulus bounded from above by a constant independent of $N$ (note again that our choice of $a_0\geq 2$ makes $\mathfrak{R}(({\bf l}_0'+i\pi)/2i\pi) >0$, whence $N^{({\bf l}_0'+i\pi)/2i\pi}\to +\infty$ as $N\to +\infty$). A similar argument applied to the integral formula of ${\mathcal{I}_{u_0,N}(z)}$ shows that the same conclusion holds true for $\textstyle \exp\left(\frac{1}{N}{\mathcal{I}_{u_0,N}(is_N^-)}\right)$.\\
Summing up, we obtain that $N^{-({\bf l}_0'+i\pi)/2i\pi}g_N$ is bounded from above by a constant independent of $N$ on $C_{a^+}$. Then let us write
\begin{equation}\label{intWatsonjanv26}\int_{C_a^+} g_N(z) e^{\frac{N}{2i\pi}\mathcal{L}_+(z,-2i\pi,2i\pi)}dz =  N^{({\bf l}_0'+i\pi)/2i\pi} \int_{C_a^+} \frac{g_N(z)}{N^{({\bf l}_0'+i\pi)/2i\pi}} e^{\frac{N}{2\pi}\Im(f_+(z))}dz.
\end{equation}
Now, from Section \ref{sub:b:+:perron} we have
$$\dfrac{\partial}{\partial x} \Im (f_+(x+it))  = 2t - \arg\left (1-e^{x+it}\right ).$$
Since $\arg\left (1-e^{x+it}\right )<0$ when $x<0$ and $t>0$ is close to $0$, it follows that, if one initially chooses $\upsilon''$ small enough (which, by the definition of $C_a^+$ and $C_a^-$ is always possible by letting $N$ be large enough), then $\textstyle \frac{\partial}{\partial x} \Im (f_+(z))>0$ for any $z\in C_a^{+}$, and thus for any such $z=x+it$ we have 
\begin{equation}\label{boundf+caseQbjanv26}
e^{\frac{N}{2\pi}\Im(f_+(z))} \leq e^{\frac{N}{2\pi}\Im(f_+(it))}=e^{\frac{N}{2\pi}{\rm Cl}_2(t)}.
\end{equation}
Then, a simple upper bound of the modulus of the RHS integral in \eqref{intWatsonjanv26} is
\begin{align}
\max_{C_a^+}\left(\frac{|g_N(z)|}{N^{({\bf l}_0'+i\pi)/2i\pi}}\right) \int_{C_a^+} e^{\frac{N}{2\pi}\Im(f_+(z))}dz\ & \leq  \max_{C_a^+}\left(\frac{|g_N(z)|}{N^{({\bf l}_0'+i\pi)/2i\pi}}\right) \cdot  O_{N\to\infty}(1) \cdot \int_{0}^{s_N} e^{\frac{N}{2\pi}{\rm Cl}_2(t)}dt \notag \\ &= O_{N\to\infty}\left (\frac{1}{N^{1-\frac{\alpha^-}{2}}}\right )=  o_{N\to\infty}\left (\frac{1}{\sqrt{N}}\right ),\label{domCa+1fev26}
\end{align}
where we used \eqref{boundf+caseQbjanv26} in the inequality, and the asymptotics of the last integral computed in Section \ref{smallIsN} in the equality. Note that the factor $O_{N\to\infty}(1)$ on the RHS of the inequality comes from the change of measure from the (compact) contour $C^{+}_a$ to the vertical contour $[0,i s_N]$.\\
This estimate is not enough for our purposes, because it only implies that the integral \eqref{intWatsonjanv26} has order $\leq \textstyle N^{({\bf l}_0'+i\pi)/2i\pi}o_{N\to\infty}\left (\frac{1}{\sqrt{N}}\right )$, whereas the integral over the subpath $C_3'\cup C_4'$ (going from $a+2i\pi-i\eta'$ to $-i\eta$, see Figure \ref{fig:contour:b:+:perron:shifted:cuts}) will have order exactly $\textstyle \frac{1}{\sqrt{N}}$ as in the classical case of Section \ref{sub:b:+:perron} (see Step 5). There could be cancellations between these two integrals (the ones over the other subpaths in Figure \ref{fig:contour:b:+:perron:shifted:cuts} will have asymptotics of order $\textstyle o_{\to \infty}(\frac{1}{\sqrt{N}})$), and therefore we have to compute more precisely the order of the integral on the RHS of \eqref{intWatsonjanv26}. We do this by using Proposition \ref{Perronfev26}.\\ 
Let us deform the arc $C_a^+$ slightly downwards near its endpoint $is_N^-$, so that it reaches the axis $i\mr$ in a point $is_N'$, where $s_N':= \textstyle \frac{\alpha'}{N}<s_N^-$, and then goes vertically upwards to $is_N^-$. Denote by $C_a^{+-}$ the subarc from $-\upsilon''$ to $is_N'$, and write
\begin{multline}\label{decompintfev26}
\int_{C_a^+} \frac{g_N(z)}{N^{({\bf l}_0'+i\pi)/2i\pi}} e^{\frac{N}{2\pi}\Im(f_+(z))}dz = \int_{C_a^{+-}} \frac{g_N(z)}{N^{({\bf l}_0'+i\pi)/2i\pi}} e^{\frac{N}{2\pi}\Im(f_+(z))}dz \\ +  \int_{[is_N',is_N^-]} \frac{g_N(z)}{N^{({\bf l}_0'+i\pi)/2i\pi}} e^{\frac{N}{2\pi}\Im(f_+(z))}dz.
\end{multline}
Instead of the integral over $[is_N',is_N^-]$ on the RHS, let us consider for a while the same integral but with the contour $[i\eta_1,i\eta_2]$, with $\textstyle \frac{\pi}{3}>\eta_2>\eta_1>0$ fixed. We know that for $z=it$, we have $\Im(f_+(z)) := \Im(\mathcal{L}_+(z,-2i\pi,2i\pi))= \Im({\rm Li}_2(e^{it}) -t^2) = {\rm Cl}_2(t)$, and the function ${\rm Cl}_2(t)$ is strictly increasing and ${\rm Cl}_2'(t)= -\Log\vert 2\sin(t/2)\vert \ne 0$ for $t\in \textstyle ]0,\frac{\pi}{3}[$. In particular $\Im(f_+(z)) <\Im(f_+(i\eta_2))$ for every $z\in [i\eta_1,i\eta_2]$. All the other assumptions of Proposition \ref{Perronfev26}(ii) are clearly satisfied (the uniform convergence of $(g_N)$ to $\rho$ on $[i\eta_1,i\eta_2]$ follows from Lemma \ref{extboundPsiNjanv26} and the properties of $R_N$ discussed in Lemma \ref{qcintjui25}), so this result implies (the sign in front of the RHS is because $[i\eta_1,i\eta_2]$ {\it ends} at the maximum $i\eta_2$ of $\Im(f_+(i\eta_2))$):
\begin{multline}\label{estimateshortstep3fev26}\int_{[i\eta_1,i\eta_2]} \frac{g_N(z)}{N^{({\bf l}_0'+i\pi)/2i\pi}} e^{\frac{N}{2\pi}\Im(f_+(z))}dz \\ \sim_{N\to +\infty} -\dfrac{e^{\frac{N}{2i\pi}( {\rm Li}_2(e^{i\eta_2}) -\eta_2^2)}}{N^{({\bf l}_0'+i\pi)/2i\pi}} \dfrac{\rho(i\eta_2)}{-i\Log\vert 2\sin(\eta_2/2)\vert}\cdot \dfrac{1}{N}.  
\end{multline}
Now we come back to $\eta_2:=s_N^- = \textstyle \alpha^-\frac{\pi}{N}$, $\eta_1 := s_N'=\textstyle \frac{\alpha'}{N}< s_N^-$. By Proposition \ref{Perronfev26} (iii) the equivalent \eqref{estimateshortstep3fev26} is uniform in $i\eta_2$ as long as it stays a maximum of $\Im(f_+)$ along the contour, it varies in a compact set not containing a critical point of $f_+$, and $(g_N)$ converges uniformly to $\rho$ on this compact set. As noted above, the first two conditions are satisfied here. As for the convergence of $(g_N)$, $i\eta_2=is_N^-$ leaves any compact subset of $\textstyle ]0,i\frac{\pi}{3}[$ as $N\to +\infty$, but the bounds \eqref{boundPsiNseqstripjanv26} and \eqref{majorjanv26_2} (with $\delta:=\alpha\textstyle \frac{\pi}{N}$) on any strip $\textstyle (\alpha+1)\frac{\pi}{N}< \mathfrak{I}(z)< 2\pi-(\alpha+1)\frac{\pi}{N}$, $\alpha>0$, imply that $g_N(\textstyle \alpha^-\frac{\pi}{N}) = \rho(\textstyle \alpha^-\frac{\pi}{N})v_N$, $\textstyle v_N:= \exp\left(\frac{1}{N}{\Psi_{u_0,N}(\alpha^-\frac{\pi}{N})}\right)\textstyle (1 + \frac{1}{N}R_N(\alpha^-\frac{\pi}{N}))$, where $(v_N)$ is a bounded sequence, bounded from below by a constant $>0$. Then, an immediate adaptation of the proof of Proposition \ref{Perronfev26} (ii) implies that \eqref{estimateshortstep3fev26} remains valid with $\eta_2:=s_N^-$ and $\eta_1 := s_N'$, by multiplying $\rho(i\eta_2)=\rho(is_N^-)$ with $v_N$.\\
The result is as follows. We have ${\rm Cl}_2'(s_N^-) = -\Log\vert 2\sin(\alpha^-\pi N/2)\vert \sim_{N\to \infty} \Log(N)$, and hence $\textstyle o_{n \to \infty}\left(1/n\vert f'(z_0)\vert \right) = o_{n \to \infty}\left(1/N\Log(N)\right)$ in the asymptotic formula of Proposition \ref{Perronfev26} (ii). Also ${\rm Cl}_2(s_N^-)\sim_{N\to +\infty} -s_N^-\Log(s_N^-)$, $e^{-\frac{N}{2i\pi} (s_N^-)^2}\sim_{N\to +\infty} 1$, and
$$\frac{\rho(is_N^-) }{-i\Log\vert 2\sin(s_N^-/2)\vert} \sim_{N\to +\infty} 
\frac{1}{i}\cdot e^{-\frac{{\bf l}_1'\alpha^-}{2N}}\left(\frac{Ni}{\alpha^-\pi}\right)^{\frac{{\bf l}_0'}{2i\pi}+\frac{1}{2}}\cdot \frac{1}{\Log(\frac{N}{\alpha^-\pi})}.$$
Therefore, taking the bounded sequence $(v_N)$ into account as explained above, from \eqref{estimateshortstep3fev26} we get
\begin{align}
\int_{[is_N',is_N^-]} & \frac{g_N(z)}{N^{({\bf l}_0'+i\pi)/2i\pi}} e^{\frac{N}{2\pi}\Im(f_+(z))}dz \notag \\ & \sim_{N\to +\infty} i^{\frac{{\bf l}_0'}{2i\pi}+\frac{3}{2}}e^{\frac{N}{2\pi}(\alpha^-\frac{\pi}{N}\cdot \Log(\frac{N}{\alpha^-\pi}))} e^{-\frac{{\bf l}_1'\alpha^-}{2N}}\left(\frac{1}{\alpha^-\pi}\right)^{\frac{{\bf l}_0'}{2i\pi}+\frac{1}{2}}v_N\cdot \frac{1}{\Log(\frac{N}{\alpha^-\pi})}\cdot \dfrac{1}{N}
\notag
\\ & \sim_{N\to +\infty} \dfrac{i^{\frac{{\bf l}_0'}{2i\pi}+\frac{3}{2}}}{N^{1-\frac{\alpha^-}{2}}\Log(N)}\left(\frac{1}{\alpha^-\pi}\right)^{\frac{{\bf l}_0'}{2i\pi}+\frac{1}{2}+ \frac{\alpha^-}{2}}v_N.\label{equiv6fev26}
\end{align}
We can now conclude. Consider the integral over $C_a^{+-}$ on the RHS of \eqref{decompintfev26}. As in \eqref{domCa+1fev26} one finds
\begin{align*}\left \vert \int_{C_a^{+-}} g_N(z)e^{\frac{N}{2i\pi}\mathcal{L}_+(z,-2i\pi,2i\pi)}dz\right \vert = O_{N\to\infty}\left (\frac{1}{N^{1-\frac{\alpha'}{2}}}\right ).\end{align*}
Since $\alpha'< \alpha^-$, it is a $o_{N\to +\infty}$ of \eqref{equiv6fev26}. From this and \eqref{intWatsonjanv26} we deduce
\begin{multline}\label{intCa+8fev26}
\int_{C_a^+} g_N(z) e^{\frac{N}{2i\pi}\mathcal{L}_+(z,-2i\pi,2i\pi)}dz \\ \sim_{N\to +\infty} i^{\frac{{\bf l}_0'}{2i\pi}+\frac{3}{2}}\cdot \dfrac{N^{\frac{{\bf l}_0'}{2i\pi}-\frac{1}{2}+\frac{\alpha^-}{2}}}{\Log(N)} \left(\frac{1}{\alpha^-\pi}\right)^{\frac{{\bf l}_0'}{2i\pi}+\frac{1}{2}+ \frac{\alpha^-}{2}}v_N.
\end{multline}}
\smallskip

This concludes Step 3.

\

\underline{Step 4: Deformed contour in case (a), integral $I_{N,+}(i\pi)$.}\\
Similarly, in the situation of Figure \ref{fig:contour:a:+} we can deform $C_N^\pm$ to the contour shown in the figure except in the case $\mathfrak{R}(\Log(u_{0}))>0$, where the contour must circumvent $L_1$ in a small subarc close to $0$ and joining a point $-\upsilon''$, $\upsilon''>0$, to $is_N^-$, if $\mathfrak{I}(\Log(u_{0}))<0$, or the contour must circumvent $L_2$ in a small subarc close to $2i\pi$ and joining $-\upsilon''+2i\pi$ to $2i\pi - is_N^+$, if $\mathfrak{I}(\Log(u_{0}))>0$. Indeed, we can take such subarcs to be $C^+_a$ in the first case, and $\bar{C}^+_a +2i\pi$ in the second case, with $C^+_a$ defined as in Step 3, and $\bar{C}^+_a$ the complex conjugate of $C^+_a$ but with endpoint $-is_N^+$ instead of $-is_N^-$. 

Here we get the following horizontal derivative:
$$\dfrac{\partial}{\partial x} \Im (f_+(x+it))  
= 2t - \arg\left (1-e^{x+it}\right )+\pi,$$
which is positive when $t>0$. Thus the integrals of $e^{\frac{N}{2\pi}\Im(f_+(z))}$ over the subarcs $C^+_a$ or $\bar{C}^+_a +2i\pi$ will be dominated by a constant times the same integrals over the projections of these sub-arcs on the vertical axis, where we know that $\Im(f_+(z)) = {\rm Cl}_2(t)$. By the same arguments as in Step 3 for $C_a^+$ one proves that $\textstyle \max_{\bar{C}^+_a +2i\pi}\left(\frac{|g_N(z)|}{N^{({\bf l}_0'+i\pi)/2i\pi}}\right)<+\infty$. Then, the same reasoning as from \eqref{intWatsonjanv26} to the inequality in \eqref{domCa+1fev26} gives
\begin{align}
	\left \vert \int_{\bar{C}^+_a +2i\pi} g_N(z)\right.
 &\left. e^{\frac{N}{2i\pi}\mathcal{L}_+(z,-2i\pi,i\pi)}dz\right \vert \notag
	\\ &\leq  N^{({\bf l}_0'+i\pi)/2i\pi} \max_{\bar{C}^+_a +2i\pi}\left(\frac{|g_N(z)|}{N^{({\bf l}_0'+i\pi)/2i\pi}}\right) \cdot  O_{N\to\infty}(1) \cdot 
	\int_{2\pi-s_N}^{2\pi} e^{\frac{N}{2\pi}{\rm Cl}_2(t)}dt \notag \\
	&\quad \quad \quad \quad = N^{({\bf l}_0'+i\pi)/2i\pi} O_{N\to\infty}\left (\frac{1}{N}\right ).\label{intbarCa+step48fev26}
\end{align}
where the asymptotics of the last integral were obtained in Section \ref{smallpijuil25}. On the other hand, as in \eqref{intCa+8fev26} we have:
\begin{equation}\label{intCa+step48fev26}
 \int_{C_a^+}g_N(z) e^{\frac{N}{2i\pi}\mathcal{L}_+(z,-2i\pi,i\pi)}dz \sim_{N\to +\infty} i^{\frac{{\bf l}_0'}{2i\pi}+\frac{3}{2}}\cdot \dfrac{N^{\frac{{\bf l}_0'}{2i\pi}-\frac{1}{2}+\frac{\alpha^-}{2}}}{\Log(N)} \left(\frac{1}{\alpha^-\pi}\right)^{\frac{{\bf l}_0'}{2i\pi}+\frac{1}{2}+ \frac{\alpha^-}{2}}v_N.
\end{equation}
For future reference in Step 6, we note that \eqref{intbarCa+step48fev26} is negligible with respect to \eqref{intCa+step48fev26}, since $\alpha^->0$ and $(v_N)$ is bounded from below by a constant $>0$, and \eqref{intCa+step48fev26} tends to $+\infty$ as $N\to +\infty$, since $\textstyle \mathfrak{R}(\frac{{\bf l}_0'}{2i\pi}-\frac{1}{2}) >0$ by our choice $a_0\geq 2$.

\


\underline{Step 5: Checking the assumptions of Proposition \ref{gensaddlen} away from the ends $is_N^-$, $is_N^+$.}\\
By Steps 2 to 4 the function $g_N(z)e^{\frac{N}{2i\pi}\mathcal{L}_\pm(z,-2i\pi,\ell)}$ is holomorphic on a domain where we can deform the contour $C_N^-$ or $C_N^+$ to those described in Step 2 (Figure \ref{fig:contour:b:+:shifted:cuts} or $[is_N^-,is_N^+]$), Step 3 (Figure \ref{fig:contour:b:+:perron:shifted:cuts}), and Step 4.  By Cauchy's theorem the integral $I_{N,\pm}(\ell)$ is unchanged if one replaces its contour by any of these ones.\\ 
By following the analysis of Sections \ref{sub:SPM:a}--\ref{sub:SPM:b} we now check that the hypothesis of Proposition \ref{gensaddlen}(ii) are satisfied by the integral $I_{N,\pm}(\ell)$, restricted to subcontours that stay away from the ends $is_N^-$ and $is_N^+$ in the situations of Figures \ref{fig:contour:b:+:shifted:cuts} and \ref{fig:contour:b:+:perron:shifted:cuts}, and by the integral $I_{N,-}(i\pi)$ on a subcontour of $[is_N^-,is_N^+]$. Namely, these subcontours go from $2i\pi-i\eta'$ to $-i\eta$ in Figure \ref{fig:contour:b:+:perron:shifted:cuts}, and from $i\eta$ to $2i\pi - i\eta'$ in Figure \ref{fig:contour:b:+:shifted:cuts}, where $\eta>s_N^-$, $\eta'>s_N^+$, and one deformes slightly the contour near $s_N^-$ and $2i\pi - is_N^+$ so that it goes first vertically to $i\eta$ and finishes vertically from $2i\pi - i\eta'$ to $2i\pi - is_N^+$, respectively. The subcontour goes from $i\eta$ to $2i\pi-i\eta'$ vertically in the situation of the integral $I_{N,-}(i\pi)$.\\
Recall that the critical point $z_0$ of $\mathcal{L}_{\pm}(z,-2i\pi,\ell)$, where $\ell=i\pi$ or $2i\pi$, is: $\textstyle z_0= i\frac{\pi}{3}$ for $\mathcal{L}_{-}(z;-2i\pi,i\pi)$, $\textstyle z_0= \Log((\sqrt{5}-1)/2)$ for $\mathcal{L}_{+}(z;-2i\pi,2i\pi)$, and $\textstyle z_0= \Log((\sqrt{5}+1)/2+i\pi$ for $\mathcal{L}_{-}(z;-2i\pi,2i\pi)$.

In each case $g_N(z)e^{\frac{N}{2i\pi}\mathcal{L}_\pm(z,-2i\pi,\ell)}$ is holomorphic in a neighborhood of $z_0$, and by the formulas \eqref{defrho0} and \eqref{defgNjanv26} we see immediately that it is non vanishing at $z=z_0$, since $\rho(z_0)\ne 0$. In Lemma \ref{extboundPsiNjanv26} we proved that $\textstyle \exp\left(\frac{1}{N}\Psi_{u_0,N}(z_0)\right)$ converges uniformly to $1$ on compact neighborhoods of $z_0$ in $U$, and from \eqref{defRNjanv26} and the defining formula of $\mathcal{I}_{u_0,N}(z)$ one finds easily an upper bound for $\vert R_N(z)\vert$, independent of $N$, in a sufficiently small compact neighborhood of $\textstyle z_0$. Hence the hypothesis of Proposition \ref{gensaddlen}(ii) are satisfied in each case.  

\

\underline{Step 6: Comparing the asymptotics on subcontours, and conclusion.}\\
Here we combine the Steps $1$ to $5$ to describe asymptotics of the integrals $I_{N,\pm}(\ell)$.\\
Consider the integral $I_{N,+}(i\pi)$. The analysis of Section \ref{sec:case(a)In+} can be repeated verbatim for the integral restricted to the subcontour from $2i\pi-\upsilon''$ to $-\upsilon''$ in Step 4 (Figure \ref{fig:contour:a:+}). This analysis shows again that this integral is a $O_{N\to +\infty}(1)$ summand of $I_{N,+}(i\pi)$. By Step 4 the integrals \eqref{intbarCa+step48fev26} and \eqref{intCa+step48fev26}, along the arcs $\bar{C}^+_a +2i\pi$ and $C_a^+$, have distinct growths, and \eqref{intCa+step48fev26} dominates \eqref{intbarCa+step48fev26} and is not bounded. Then the integral \eqref{intCa+step48fev26} dominates the asymptotics of $I_{N,+}(i\pi)$, which are therefore of the form stated in Lemma \ref{lem:reformintqjui25}.

Consider the integral $I_{N,-}(i\pi)$. By Step 5 and Proposition \ref{gensaddlen}(ii) the analysis of Section \ref{sec:case(a)In+} can be repeated verbatim for the integral restricted to the subcontour $[i\eta,2i\pi-i\eta']$. This analysis shows again that this integral grows exponentially, with growth rate equal to $\textstyle \frac{1}{2}{\rm Vol}(M)$. The integrals on the subcontours $[is_N^-,i\eta]$ and $[2i\pi-i\eta', 2i\pi-is_N^+]$ have polynomial or subpolynomial growth, like in \eqref{intbarCa+step48fev26} and \eqref{intCa+step48fev26}, so the asymptotics of $I_{N,-}(i\pi)$ are of the form stated in Lemma \ref{lem:reformintqjui25}.

A similar reasoning applies to the integrals $I_{N,-}(2i\pi)$ and $I_{N,+}(2i\pi)$ by using the asymptotics computed in Step 3 for these integrals restricted to the small subcontours near $0$ or $2i\pi$, and the asymptotics computed from Step 5 for the integrals restricted to the subcontour from $i\eta$ to $2i\pi - i\eta'$ in Figure \ref{fig:contour:b:+:shifted:cuts}, and to the subcontour from $2i\pi-i\eta'$ to $-i\eta$ in Figure \ref{fig:contour:b:+:perron:shifted:cuts}. These asymptotics from Step 5 have equivalents of order $1/\sqrt{N}$, as in \eqref{asyIjui25c}. The integral $I_{N,+}(2i\pi)$ restricted to the small subcontour $C_a^+$ has the asymptotics \eqref{intCa+8fev26}, and the integral $I_{N,-}(2i\pi)$ restricted to the small subcontour $[is_N^-,i\eta]$ has the asymptotics \eqref{intCa+8fev26} multiplied with $-e^{-\alpha^-\pi}$ (the sign is because the contour starts at $is_N^-$, and the factor $e^{-\alpha^-\pi}$ comes for the change of $\mathcal{L}_+(z,-2i\pi,2i\pi)$ to $\mathcal{L}_-(z,-2i\pi,2i\pi)$). 
Since $a_0\geq 4$, we have $\textstyle \mathfrak{R}(\frac{{\bf l}_0'}{2i\pi}-\frac{1}{2}) >-\frac{1}{2}$, and therefore these small integrals dominate the asymptotics of $I_{N,+}(2i\pi)$ and $I_{N,-}(2i\pi)$, respectively. This concludes the proof.\cvd
\medskip

Recall Lemma \ref{rem:reduction:sigma:integral}: the two cases (a) and (b) correspond to $\bl_{1,\infty}^\bx=i\pi$, $\bl_{0,\infty}^\bx=-2i\pi$ and $\bl_{1,\infty}^\bx=2i\pi$, $\bl_{0,\infty}^\bx=-2i\pi$ respectively, for both $\bx=\bu$ and $\bv^*$.
\begin{cor}\label{cor:reductionintjui25} We have
$$\lim_{N\rightarrow +\infty}\dfrac{2\pi}{N}\Log \left \vert \int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}^\bx z)}\hat S_N(\bl_{0,N}^\bx + z)\textstyle \coth(\frac{Nz}{2})dz \right \vert  = \left \{\begin{matrix}
\dfrac{1}{2}{\rm Vol}(M) & \text{in\ case} \ (a),\\
0  & \text{in\ case}\  (b),
\end{matrix}
\right.$$
and 
$$\lim_{N\rightarrow +\infty}\dfrac{2\pi}{N}\Log \left \vert \Sigma_N(\bx_{0,N},\bx_{1,N})\right \vert = \lim_{N\rightarrow +\infty}\dfrac{2\pi}{N}\Log \left \vert \int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}^\bx z)}\hat S_N(\bl_{0,N}^\bx + z)\textstyle \coth(\frac{Nz}{2})dz \right \vert$$
for $\bx =\bu$ or $\bv^*$.
\end{cor}
\proof By Lemma \ref{qcintjui25} and the first two asymptotics in Lemma \ref{lem:reformintqjui25}, if $\ell = i\pi$ we have $\textstyle \lim_{N\to +\infty}\textstyle \frac{2\pi}{N}\Log  \vert 2I_{N,-}(\ell) -2u_0  I_{N,+}(\ell)\vert = \textstyle \frac{1}{2}{\rm Vol}(M)$. When $\ell = 2i\pi$, we can always choose $\alpha_-$ so that $\vert u_0\vert e^{-\alpha^-\pi} \ne 1$. Then the two terms in the Log have different growths, and Lemma \ref{lem:reformintqjui25} implies $\textstyle \lim_{N\to +\infty}\textstyle \frac{2\pi}{N}\Log  \vert 2I_{N,-}(2i\pi) -2u_0  I_{N,+}(2i\pi)\vert=0$. The first claim follows.

Consider the second claim. By Lemma \ref{lem:PM:SE} the limit on the right does not change if we multiply the integral by $N/4i\pi \hat S_N(\bl_{0,N}^\bx)$, since it is in $PM(N)$ by Lemma \ref{factorest}, using that ${\bf l}_{k,N}^\bx \in (\pi i) \mz + O(N^{-1})$ by \eqref{recapuvarmars25} and \eqref{l0inftymars25}-\eqref{l1inftymars25}. And it does not change either if we add $1$ to the term inside $\Log|.|$, again because of its asymptotics given by Lemma \ref{lem:reformintqjui25}.\cvd

\begin{remark}\label{fulldev}{\rm The proof of Lemma \ref{lem:reformintqjui25} gives more than the stated limits or equivalents, and expliciting the phase factor $e^{i\theta}$ in Proposition \ref{gensaddlen} and improving the asymptotics of Lemma \ref{factorest}, one can deduce subexponential terms of $\Sigma_N(\bx_{0,N},\bx_{1,N})$ (see Lemma \ref{lemintrep}), and therefore of $\Hh_{N}^{red}(M,\rho,\kappa; \mathfrak{s})$ by using the formula \eqref{form1}. 

Indeed, consider for instance the case $\ell = i\pi$. In this case $f_-(z) = {\rm Li}_2(e^z)+z^2-i\pi z$, and the computations in Section \ref{sub:a:-} and the formula $\textstyle \mathfrak{R}({\rm Li}_2(e^{it})) = \sum_{n\geq 1} \frac{\cos(nt)}{n^2} = \frac{\pi^2}{6} - \frac{\pi t}{2}+\frac{t^2}{4}$ (\cite{Z}) imply that $f_-$ has the critical point $\textstyle z_0=\frac{i\pi}{3}$, and $\textstyle f_-(\frac{i\pi}{3}) = \frac{\pi^2}{4} + i\frac{1}{2}{\rm Vol(M)}$, $f''_-(e^{\frac{i\pi}{3}}) = 1+ e^{\frac{i\pi}{3}}$. Also, from \eqref{defrho0} we get $\textstyle g(e^{\frac{i\pi}{3}}):=\rho(e^{\frac{i\pi}{3}}) = e^{-\frac{{\bf l}_1'}{2i\pi}\cdot \frac{i\pi}{3}}(1-e^{\frac{i\pi}{3}})^{-\frac{{\bf l}_0'}{2i\pi}-\frac{1}{2}}=e^{-\frac{{\bf l}_1'}{6}-\frac{{\bf l}_0'}{3}-\frac{i\pi}{3}}$, where we recall that ${\bf l}_k' = \Log(u_k) + i\pi a_k$, for $x=u$ or $v^*$. Therefore 
\begin{align*} \int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}^\bx z)} \hat S_N(\bl_{0,N}^\bx + z) \textstyle & \coth(\frac{Nz}{2}) dz\\ & \sim_{N\to +\infty} 2I_{N,-}(i\pi) \\
& \sim_{N\to +\infty} 2\cdot \frac{4\pi}{\sqrt{N}} e^{i\theta} \cdot e^{-\frac{{\bf l}_1'}{6}-\frac{{\bf l}_0'}{3}-\frac{i\pi}{3}} \cdot \frac{1}{3^\frac{1}{4}} e^{\frac{N}{2\pi}(\frac{1}{2}{\rm Vol}(M)-i\frac{\pi^2}{4})}
\end{align*}
where $\theta := \pi -\textstyle \frac{1}{2}\arg(-\frac{1}{f''_-(e^{\frac{i\pi}{3}})})$ (see e.g. \cite[equation (19)]{PV}).}
\end{remark}
\color{black}
