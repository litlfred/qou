---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-007-22-a-relative-homology-for-state-integrals-conto
section_title: "A relative homology for state integrals contours"
section_number: 2.2
pages: 12-14
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
toc_source: outline
text_source: latex
latex_prose_ratio: 0.795
latex_coverage_ratio: 0.932
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜no [9] that perturbative series associated with the hyperbolic knots 41 and 52 are resurgent and"
---
In this section, we define the homology $H_\bullet(\Sigma,D_{\infty,\theta})$ relative to a region $D_{\infty,\theta}$. The first relative homology group $H_1(\Sigma,D_{\infty,\theta})$ contains lifts of the state integral contours $\calJ_{\ell,\tau}$ to $\Sigma$ and the thimbles $\calC_{p_0,\vartheta}$. First, we construct a finite dimensional homology $H_\bullet(X_{\epsilon,M},D_{\infty,\theta})$ defined for a compact surface $X_{\epsilon,M}\subset\Sigma$. Then, $H_\bullet(\Sigma,D_{\infty,\theta})$ will be defined via the limits $\epsilon\to0$ and $M\to\infty$.


\subsubsection{The surface $X_{\epsilon,M}$}\label{sec:X_eps_M}

We choose the set of coordinates $z_{m,\pm}$ for $m=0,\ldots, A-1$. For given constants $M,\epsilon>0$, we define the surface $X_{\epsilon, M}$ by gluing different local coordinate charts. Let $m\in\{0,\dots,A-1\}$, on the $m$-sheet of $\Sigma$ we define 
\begin{align}
{\calU}_{\epsilon,M,m}^{\pm}&\;:=\;\left\lbrace p\in\Sigma\colon |\Re(z_{m,\pm}(p))|\leq M\,,\; \Im(\pm z_{m,\pm}(p))\geq-\frac{\epsilon}{M} \right\rbrace\,, \\
{\calV}_{\epsilon,m}^{\pm}&\;:=\;\bigcup_{k\in\BZ}\Big\{p\in\Sigma \colon |z_{m,\pm}(p)-k|\geq\frac{\epsilon}{1+|k|}\Big\}\,,\\
{\calW}_{\epsilon,M,m}^{\pm}&\;:=\;\left\lbrace p\in\Sigma\colon \Im(\pm z_{m,\pm}(p))\geq\frac{\epsilon}{M} \right\rbrace\,.
\end{align}
Then, we define the surface
\be
  X_{\epsilon, M}
  \=
  \Sigma_{\epsilon,M}^{+}\cup\Sigma_{\epsilon,M}^{-}\subset\Sigma\,,
  \qquad\text{where}\qquad 
  \Sigma_{\epsilon,M}^{\pm}
  \;:=\;\bigcup_{m=1}^A{\calU}_{\epsilon,M,m}^{\pm}\cap{\calV}_{\epsilon,m}^{\pm}\cup{\calW}_{\epsilon,M,m}^{\pm}\,.
\ee
We represent one of the sheets defining $\Sigma_{\epsilon,M}^{+}$ in Figure~\ref{fig:sigma_eps_M}.
\begin{figure}[ht]
\begin{tikzpicture}[scale=0.9]
\filldraw[fill=pink!30,color=pink!30] (-4,0) rectangle (8,2.5);
\filldraw[fill=pink!30,color=pink!30] (-4,-0.2) rectangle (8,0);



\foreach \x in {0,...,147}
\draw[red,xshift=\x*0.1 cm] (-6.5,0.3)--(-4.3,2.5);
\foreach \x in {0,...,21}
\draw[red] (8.3+\x*0.1,0.3)--(10.5,2.5-\x*0.1);
\foreach \x in {0,...,21}
\draw[red] (-6.5,2.5-\x*0.1)--(-6.5+\x*0.1,2.5);
\filldraw[color=pink!30,pattern=north east lines,pattern color=red] (-5,-3) rectangle (-5.5,-3.5);
\filldraw[fill=pink!30,color=pink!30] (-2,-3) rectangle (-2.5,-3.5);
\filldraw[fill=white,thick] (0.5,-3.25) circle (0.25);
\node[right,font=\tiny] at (-5,-3.25) {$\calW^+_{\epsilon,M,m}$};
\node[right,font=\tiny] at (-2,-3.25) {$\calU^+_{\epsilon,M,m}$};
\node[right,font=\tiny] at (0.75,-3.25) {$\BC\setminus \calV^+_{\epsilon,m}$};
\filldraw[fill=white,thick](2,0) circle (0.6);
\filldraw[fill=white,thick](0,0) circle (0.5);
\filldraw[fill=white,thick](4,0) circle (0.5);
\filldraw[fill=white,thick](-4,0) circle (0.3);
\filldraw[fill=white,thick](8,0) circle (0.3);
\filldraw[fill=white,thick](-6,0) circle (0.2);
\filldraw[fill=white,thick](10,0) circle (0.2);
\filldraw[fill=white,thick](6,0) circle (0.4);
\filldraw[fill=white,thick](-2,0) circle (0.4);
\draw[red,snake it] (2,0) -- (2,-2.5);
\draw[red,snake it] (-2,0) -- (-2,-2.5);
\draw[red,snake it] (0,0) -- (0,-2.5);
\draw[red,snake it] (4,0) -- (4,-2.5);
\draw[red,snake it] (-4,0) -- (-4,-2.5);
\draw[red,snake it] (6,0) -- (6,-2.5);
\draw[red,snake it] (8,0) -- (8,-2.5);
\draw[red,snake it] (-6,0) -- (-6,-2.5);
\draw[red,snake it] (10,0) -- (10,-2.5);
\foreach \x in {-6,-4,-2,0,2,4,6,8,10}
\filldraw (\x,0) circle (2.5pt);
\draw[->] (-7,0) -- (10.5,0);
\draw[->] (2,-2.5)--(2,3);
\end{tikzpicture}
\caption{The $m$-sheet of $\Sigma_{\epsilon,M}^+$ in the $z_{m,+}$ coordinates.}\label{fig:sigma_eps_M}
\end{figure}

\subsubsection{Behaviour at infinity}
The dilogarithm $\Li_{2}(\e(z))$ is exponentially small as $\Im(z)\to\infty$. Therefore, the behaviour of the thimbles at infinity is governed by the quadratic functions
\be
\begin{aligned}
  &P_{+}:\Sigma_{\epsilon,M}^{+}\rightarrow\BC\,,
  &\qquad\text{such that}\qquad&
  P_{+}(p)\=\frac{A}{2}\,z_{+}(p)^2\,,\\
  &P_{-}:\Sigma_{\epsilon,M}^{-}\rightarrow\BC\,,
  &\qquad\text{such that}\qquad&
  P_{-}(p)\=\frac{A-B}{2}\,z_{-}(p)^2\,.
\end{aligned}
\ee
We define the sets $D_{L,\theta}^{\pm}\subseteq P_{\pm}^{-1}\big(\{w\in\BC\;|\;-\Im(we^{-i\theta})>L\}\big)$ to be the connected components containing points $p$ such that $z_{+}(p)=e^{i\theta/2}e^{-iA\epsilon}\in D_{L,\theta}^{+}$ and $z_{-}(p)=-e^{i\theta/2}e^{-i(A-B)\epsilon}\in D_{L,\theta}^{-}$ respectively. For large enough $L$, these sets have arguments with $\theta\in(0,2\pi)$
\be\label{eq:D.angles}
\begin{aligned}
  \arg(D_{L,\theta}^{+})
  &\=
  \Big(\max\big\{0,\tfrac{\theta}{2}-\tfrac{\pi}{2}\big\},\min\big\{\pi,\tfrac{\theta}{2}\big\}\Big)\,,\\
  \arg(D_{L,\theta}^{-})
  &\=
  \Big(\max\big\{\pi,\tfrac{\theta}{2}+\tfrac{3\pi}{4}-\tfrac{(A-B)\pi}{4|A-B|}\big\},\min\big\{2\pi,\tfrac{\theta}{2}+\tfrac{5\pi}{4}-\tfrac{(A-B)\pi}{4|A-B|}\big\}\Big)\,.
\end{aligned}
\ee
The regions are depicted in blue for $\theta\in(\tfrac{\pi}{2},\tfrac{3\pi}{2})$ in Figure~\ref{fig:good.region.I} and Figure~\ref{fig:good.region.II}.
We denote with $D_{L,\theta}$ the union of the regions $D_{L,\theta}^+$ and $D_{L,\theta}^{-}$.


\subsubsection{The relative homology} 































\begin{proposition}\label{prop:relative-homology} 
For $\epsilon,M,L>0$, and $\theta\in(0,2\pi)$, the relative homology group $H_1(X_{\epsilon,M},D_{L,\theta})$ is finite dimensional. 
\end{proposition}
\begin{proof}
We consider the Mayer--Vietoris sequence:
\[
\begin{tikzcd}
 0\arrow[r]& H_1(\Sigma_{\epsilon,M}^{+}\,;D_{L,\theta}^{+})\oplus H_1(\Sigma_{\epsilon,M}^{-}\,;D_{L,\theta}^{-})\arrow[r]&H_1(X_{\epsilon,M}\,,D_{L,\theta})\arrow[dll,controls={(3.5,-0.5) and (-3.5,0.5)}] \\
H_0(\Sigma_{\epsilon,M}^{+}\cap\Sigma_{\epsilon,M}^{-})\arrow[r]&H_0(\Sigma_{\epsilon,M}^{+}\,,D_{L,\theta}^{+})\oplus H_0(\Sigma_{\epsilon,M}^{-}\,,D_{L,\theta}^{-})\arrow[r]&H_0(X_{\epsilon,M}\,,D_{L,\theta})\arrow[r]&0
\end{tikzcd}
\]
Notice that $H_n(\Sigma_{\epsilon,M}^{-}\,,D_{L,\theta}^{-})\cong H_n(\Sigma_{\epsilon,M}^{+}\,,D_{L,\theta}^{+})\cong \{0\}$ for every $n\ge 0$, because $\Sigma_{\epsilon,M}^{\pm}$ are homeomorphic to a disjoint union of discs and $D_{L,\theta,\pm}$ are connected; therefore $H_1(X_{\epsilon,M}\,,D_{L,\theta})\cong H_0(\Sigma_{\epsilon,M}^{+}\cap\Sigma_{\epsilon,M}^{-})$.

\medskip

In addition, $\Sigma_{\epsilon,M}^{-}\cap\Sigma_{\epsilon,M}^{+}$ is homeomorphic to the disjoint union of finitely many discs (see Figure~\ref{fig:intersection}), hence $H_0(\Sigma_{\epsilon,M}^{-}\cap\Sigma_{\epsilon,M}^{+})$ is generated by a subset of the class of points $[p_{m,\ell}]$ labeled by $m=0,\ldots, A-1$ and $\ell=-M,\dots,M$. Thus, we deduce that $H_1(X_{\epsilon,M}\,,D_{L,\theta})$ is finite dimensional too. 
\begin{figure}[ht]
\begin{tikzpicture}
\filldraw[fill=pink!30,color=pink!30] (-3,-0.2) rectangle (7,0);
\filldraw[fill=pink!30,color=pink!30] (-3.2,0) rectangle (7.2,0.2);


\foreach \x in {1,2,3,4}
\filldraw[fill=white,thick] (-6+2*\x+\x*0.1+0.1,0) arc (0:180:\x*0.1+0.1);
\foreach \x in {1,2,3}
\filldraw[fill=white,thick] (10-2*\x+\x*0.1+0.1,0) arc (0:180:\x*0.1+0.1);
\filldraw[fill=white,thick] (-4+0.15,0) arc (0:-180:0.15);
\filldraw[fill=white,thick] (-2+0.4,0) arc (0:-180:0.4);
\filldraw[fill=white,thick] (0+0.3,0) arc (0:-180:0.3);
\filldraw[fill=white,thick] (2+0.4,0) arc (0:-180:0.4);
\filldraw[fill=white,thick] (4+0.2,0) arc (0:-180:0.2);
\filldraw[fill=white,thick] (6+0.5,0) arc (0:-180:0.5);
\filldraw[fill=white,thick] (8+0.3,0) arc (0:-180:0.3);
\foreach \x in {-4,-2,0,2,4,6,8}
\draw node at (\x,0) {$\bullet$};

















\draw (-4.5,0) -- (8.5,0);
\node[below,font=\tiny] at (1,0) {$p_{m,-1}$};
\node[font=\tiny] at (1,0) {$\bullet$};
\node[below,font=\tiny] at (3,0) {$p_{m,0}$};
\node[font=\tiny] at (3,0) {$\bullet$};
\node[below,font=\tiny] at (5,0) {$p_{m,1}$};
\node[font=\tiny] at (5,0) {$\bullet$};
\node[below,font=\tiny] at (7,0) {$p_{m,2}$};
\node[font=\tiny] at (7,0) {$\bullet$};
\node[below,font=\tiny] at (-1,0) {$p_{m,-2}$};
\node[font=\tiny] at (-1,0) {$\bullet$};
\node[below,font=\tiny] at (-3,0) {$p_{m,-3}$};
\node[font=\tiny] at (-3,0) {$\bullet$};
\end{tikzpicture}
\caption{The projection of $\Sigma_{\epsilon,M}^+\cap\Sigma_{\epsilon,M}^{-}$ on the $m$-sheet in the $z_{m,+}$ coordinates.}\label{fig:intersection}
\end{figure} 


\end{proof}


Let $M,\epsilon>0$ and $\theta\in(0,2\pi)$, we define


the homology 
\be
H_\bullet(X_{\epsilon,M},D_{\infty,\theta}):= H_{\bullet}\left(\varprojlim_{L\ge M} C_\bullet(X_{\epsilon,M},D_{L,\theta})\right)\,.
\ee 
For every $L>L'\geq M>0$, the homotopy equivalence between $D_{L,\theta}$ and $D_{L',\theta}$ induces an isomorphism of chain complex $C_\bullet(X_{\epsilon,M},D_{L,\theta})\to C_\bullet(X_{\epsilon,M},D_{L',\theta})$. Hence, there exists a long exact sequence 
\be\label{eq:exact_sequence}
\ldots\to H_{n}(D_{L,\theta})\to H_{n}(X_{\epsilon,M})\to H_n(X_{\epsilon,M},D_{\infty,\theta})\to\ldots 
\ee
for $L$ large enough. From Proposition~\ref{prop:relative-homology}, we deduce that $H_1(X_{\epsilon,M},D_{\infty,\theta})$ is finite dimensional too.

By a similar argument, we can define the homology of $\Sigma$ relative to $D_{\infty,\theta}$: notice that for every $M'\geq M>0$ and $\epsilon\geq\epsilon'>0$ the homotopy equivalence between $X_{\epsilon,M}$ and $X_{\epsilon',M'}$ induces an isomorphism of chain complexes $C_\bullet(X_{\epsilon,M},D_{\infty,\theta})\to C_\bullet(X_{\epsilon',M'},D_{\infty,\theta})$, thus 
\be\label{eq:full_H}
H_\bullet(\Sigma,D_{\infty,\theta}):=H_\bullet\left(\varprojlim_{M,\epsilon} C_\bullet(X_{\epsilon,M},D_{\infty,\theta})\right)
\ee 
defines the infinite dimensional homology group of $\Sigma$ relative to $D_{\infty,\theta}$.
