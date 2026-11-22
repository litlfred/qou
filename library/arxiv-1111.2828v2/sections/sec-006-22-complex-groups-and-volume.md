---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-006-22-complex-groups-and-volume
section_title: "Complex groups and volume"
section_number: 2.2
pages: 9-10
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.946
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sub.cvolume}

Recall that there is a $1$-$1$ correspondence between flat $G$-bundles over 
$M$ and representations $\pi_1(M)\to G$ up to conjugation. This correspondence 
takes a flat bundle to its holonomy representation. If 
$\rho\colon\pi_1(M)\to G$ is a representation, we let $E_\rho$ denote the 
corresponding flat bundle.
In the following $G$ denotes a simply connected, simple, complex Lie group, 
and $M$ a closed, oriented $3$-manifold. 
The following definition is motivated by Theorem~\ref{SL2complexvolume} 
below.

\begin{definition}
\lbl{compvoldefn} 
The \emph{complex volume} $\Vol_\C(\rho)$ of a representation 
$\rho\colon\pi_1(M)\to G$ is defined by
\begin{equation}
\widehat c(E_\rho)(M)=i\Vol_\C(\rho)\in\C/4\pi^2\Z.
\end{equation}
The \emph{volume} $\Vol(\rho)$ of $\rho$ is the real part of $\Vol_\C(\rho)$.
\end{definition}

The bundle $E_\rho$ is isomorphic to $\widetilde M\times_\rho G$, and we thus have a $1$-$1$ correspondence between
sections of $E_\rho$ and $\rho$-equivariant maps $\widetilde M\to G$ such that $f\colon\widetilde M\to G$ 
corresponds to the section $s(x)=[\widetilde x,f(\widetilde x)]$. 
\begin{lemma}
\lbl{rhomapandVolC}
For any $\rho$-equivariant map $f\colon\widetilde M\to G$, we have 
$i\Vol_\C(\rho)=\int_D f^*(\sigma(P))$, where $D$ is a fundamental domain for $M$ in $\widetilde M$.
\end{lemma}
\begin{proof}
For any invariant form $\eta\in\Omega^3(G)^G$, the form $\theta(\eta)\in \Omega^3(E_\rho;\F)$ 
is induced by the pullback of $\eta$ under the projection $\widetilde M\times G\to G$. Letting $\eta=\sigma(P)$, the result follows from~\eqref{CSintegral}.
\end{proof}

Let $\H^3=\SL(2,\C)/\SU(2)$ be hyperbolic $3$-space. We identify the 
orthonormal frame bundle $F(\H^3)$ of $\H^3$ with $\PSL(2,\C)$.


\begin{lemma}
\lbl{sigmaPandCS} 
For $G=\SL(2,\C)$, $\sigma(P)=-h^*\wedge e^*\wedge f^*$, where
$h=\Mat{1}{0}{0}{-1}$, $e=\Mat{0}{1}{0}{0}$ and $f=\Mat{0}{0}{1}{0}$ are the 
standard generators of $\mathfrak{sl}(2,\C)$ over $\C$.
\end{lemma}

\begin{proof}
As in Example~\ref{SLnExample}, $P=\frac{1}{2}\Tr$. Using the fact that 
$\Tr(AB)=\Tr(BA)$, it follows from~\eqref{sigmaPformula} that 
$\sigma(P)\in\Omega^3(G)^G=\wedge^3(\mathfrak g^*)$ is given by
\begin{equation}
\mathfrak g\times\mathfrak g\times\mathfrak g\to \C,\quad (A,B,C)\mapsto -\frac{1}{2}\Tr(A[B,C]).
\end{equation}
A simple computation shows that if $A=\Mat{a}{b}{c}{-a}$, $B=\Mat{e}{f}{g}{-e}$ and $C=\Mat{i}{j}{k}{-i}$
\begin{equation}
-\frac{1}{2}\Tr(A[B,C])=-\det\left(\begin{smallmatrix}a&b&c\\e&f&g\\i&j&k\end{smallmatrix}\right)=-h^*\wedge e^*\wedge f^*(A,B,C).
\end{equation}
This proves the result.

\end{proof}

\begin{theorem}
\lbl{SL2complexvolume} 
Let $M=\H^3/\Gamma$ be a closed hyperbolic $3$-manifold, and let $\rho\colon\pi_1(M)\to\SL(2,\C)$ be a lift of the geometric representation. We have
\begin{equation}
\widehat c(E_\rho)([M])=i(\Vol(M)+i\CS(M))\text{ in }\C/2\pi^2\Z,
\end{equation}
where $\CS(M)=2\pi^2\cs(M)$, and $\cs(M)$ is the (Riemannian) Chern-Simons invariant~\cite[(6.2)]{ChernSimons}.
\end{theorem}

\begin{proof} 
The fact that the imaginary part equals volume is well known, and follows from the fact (see Dupont~\cite{Dupont}) that the imaginary part of $\sigma(P)$ is cohomologous to the pullback of the hyperbolic volume form. Yoshida~\cite[Lemma~3.1]{Yoshida} shows that the real part of the form $h^*\wedge e^*\wedge f^*$ equals $2\pi^2\cs$, where $\cs$ is the Riemannian Chern-Simons form on $F(\H^3)=\PSL(2,\C)$ (pulled back to $\SL(2,\C)$. Note that the Riemannian connection on $F(\H^3)=\PSL(2,\C)$ descends to the Riemannian connection on $F(M)=\PSL(2,\C)/\Gamma$. If $f\colon\widetilde M\to\SL(2,\C)$ is $\rho$-equivariant, the composition
\begin{equation}
\xymatrix{{\widetilde M}\ar[r]^-f&{\SL(2,\C)}\ar[r]&{\PSL(2,\C)}\ar[r]&{\PSL(2,\C)/\Gamma=F(M)}}
\end{equation}
is $\rho$-invariant, and thus descends to a section of $F(M)$. The result now follows from Yoshida's result together with Lemma~\ref{sigmaPandCS} and Lemma~\ref{rhomapandVolC}. 
\end{proof}

\begin{remark} 
Note that Theorem~\ref{SL2complexvolume} implies that modulo $2\pi^2$, the complex volume of a representation lifting the geometric representation only depends on $M$ and not on the choice of lift.
\end{remark}

\begin{remark} 
Since $P$ is real on $K$, the imaginary part of $\sigma(P)$ is cohomologous to an invariant $3$-form on $G/K$. Since $H^3(\mathfrak g,\mathfrak k;\R)=\R$, there is a unique such form up to scaling. We may thus think of $\Imag(\sigma(P))$ as a volume form. 
\end{remark}
