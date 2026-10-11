---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-009-332-factorization-of-the-superconformal-index
section_title: "Factorization of the superconformal index"
section_number: 3.3.2
pages: 48-81
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.729
---
The superconformal index of 3d $\CN=2$ theory \eqref{TCircFib} reads
\begin{multline}
	\CI_{T[M_3]}(q,t)=\sum_{m\geq 0}\frac{1}{|\CW_m|}\int_{|z|=1}\frac{dz}{2\pi i z}\,z^{2pm}\,
(1-z^{\pm 2}q^m)\,q^{-2m(1-g)}\,t^{-2m(1-g)}
\times \\
\frac{(z^{\pm2}q^mt^{-1};q)_\infty(t^{-1};q)_\infty}{(z^{\pm 2}q^{m+1}t)_\infty(qt;q)_\infty}\times \\
\prod_{i=1}^g	
\frac{(z^{\pm2}u_i^{-1}q^{m+1};q)_\infty(u_i^{-1}q;q)_\infty}{(z^{\pm2}u_iq^{m};q)_\infty(u_i;q)_\infty}\cdot
\frac{(z^{\pm2}tu_iq^{m+1};q)_\infty(tu_iq;q)_\infty}{(z^{\pm2}t^{-1}u_i^{-1}q^m;q)_\infty(t^{-1}u_i^{-1};q)_\infty}.
\label{TCircFibIndex}
\end{multline}
Unlike in the case of Lens spaces ($g=0$), now there is some ambiguity in the choice of the contour,
because if $|t|=1$ there are poles at $|z|=1$. The natural
physical choice assumes that $|q|<1$ and $|u_i|=|t^{-1}u_i^{-1}|=q^{\epsilon}$ with $\epsilon>0$, which corresponds to choosing an infinitesimally small R-charge for adjoint hypers. However, such choice of the contour is different from the one in (\ref{TCircFibBlock}) and (\ref{WRTCircFibBlock}), illustrated in Figure~\ref{fig:TCircFib-contour}.

\FIGURE{
\centering
 \includegraphics[scale=0.8]{TCircFib-contour-1}
\caption{Pole structure of the integrands in (\ref{TCircFibBlock}) and (\ref{TCircFibIndex}). The green contour corresponds to a choice of the contour $\gamma$ such that in the $t\rightarrow 1$ limit it agrees with the principal-value prescription in  (\ref{WRTCircFibBlock}) which reproduces the WRT invariant. The blue contour is the standard physical choice of contour for the superconformal index (\ref{TCircFibIndex}).}
\label{fig:TCircFib-contour}
}

Next, we would like to show that
\begin{equation}
	\CI_{T[M_3]}(q,t,u) \; = \; \sum_{a}|\CW_a|\hat{Z}_a(q,t,u)\hat{Z}_a(1/q,1/t,1/u).
	\label{FactorizationCircFib}
\end{equation}
As before, the problem with checking it directly is that we only have the expression for $\hat{Z}_a(q,t)$ which is valid inside a unit disc $|q|<1$, without any systematic way of analytically continuing it outside. Again, we can instead try to check (\ref{FactorizationCircFib}) in a particular limit of flavor fugacities such that $\hat{Z}_a(q,t)$ becomes a rational function and has canonical analytic continuation outside of $|q|<1$. However, one finds that there are several new technical complications compared to the case of Lens spaces ($g=0$). First, there is an ambiguity in the choice of the contours (\ie~whether we encircle the poles at $z^2=t^{\pm1/2}$ or not), illustrated in Figure~\ref{fig:TCircFib-contour}. Second,
for $g>1$ the limit $u_i\rightarrow 1$, $t\rightarrow q^{\beta}$ with $\beta\in \Z_{\geq 0}$ does not give a rational function, but rather a lacunary function that cannot be analytically continued outside $|q|<1$ due to the Fabry gap theorem.
In particular, one cannot repeat the trick with the cyclotomic expansion due to the absence of closed form expression for $t=1$.

However, one can avoid all these problems by taking the limit $u_i\rightarrow 1$, $t\rightarrow q^\beta$, with $\beta<0$.
In this limit, all poles at $|z|\approx 1$ disappear and the contour ambiguity becomes irrelevant.
Namely, for $\beta\in\Z_{-}$, let us define
\begin{equation} \hat{Z}_a^{(\beta)}(q) \; \equiv \; \left.\hat{Z}_a(q,t)\,(qt;q)_\infty\,\prod_{i=1}^g\frac{(u_i;q)_\infty}{(tu_iq;q)_\infty}\right|_{t=q^{\beta},u_i=1}
\end{equation}
and
\begin{equation}
	\CI^{(\beta)}(q) \; \equiv \; \left.\CI(q,t)\,\frac{(qt;q)_\infty}{(1/t;q)_\infty}
	\prod_{i=1}^g\frac{(u_i;q)_\infty(t^{-1}u_i^{-1};q)_\infty}{(u_i^{-1}q;q)_\infty(tu_iq;q)_\infty}
	\right|_{t=q^{\beta},u_i=1}.
\end{equation}
Then, one can check for various values of $g,p,\beta<0$ that indeed
\begin{equation}
	\CI^{(\beta)}(q) \; = \; \sum_a|\CW_a|\hat{Z}_a^{(\beta)}(q)\hat{Z}_a^{(\beta)}(1/q).
\end{equation}
For example, let us take $g=2$ and $p=5$. Then, we have the following.

$\beta=-1$:
\begin{equation}
	\begin{array}{c}
	2\hat{Z}_0^{(-1)}(q)=1 \,,\quad
	\hat{Z}_1^{(-1)}(q)=0 \,,\quad
	\hat{Z}_2^{(-1)}(q)=0.\; \\
		2\CI^{(-1)}(q)=1.
	\end{array}
\end{equation}

$\beta=-2$:
\begin{equation}
	\begin{array}{c}
	2\hat{Z}_0^{(-2)}(q)=q^{-2}+1 \,,\quad
	\hat{Z}_1^{(-2)}(q)=q^{-4/5} \,,\quad
	\hat{Z}_2^{(-2)}(q)=0.\; \\
		2\CI^{(-2)}(q)=4+q^2+\frac{1}{q^2}.
	\end{array}
\end{equation}

$\beta=-3$:
\begin{equation}
	\begin{array}{c}
	2\hat{Z}_0^{(-3)}(q)=\frac{1}{q^6}+\frac{1}{q^4}+\frac{2}{q^3}+\frac{1}{q^2}+1,\;
	\hat{Z}_1^{(-3)}(q)=-\frac{(q+1)^2
   \left(q^2-q+1\right)}{q^{24/5}},\;
	\hat{Z}_2^{(-3)}(q)=\frac{1}{q^{11/5}}.\; \\
		2\CI^{(-3)}(q)=q^6+\frac{1}{q^6}+4 q^4+\frac{4}{q^4}+8 q^3+\frac{8}{q^3}+5 q^2+\frac{5}{q^2}+8 q+\frac{8}{q}+18.
		\\
		\ldots
	\end{array}
\end{equation}
And indeed one can verify that in each case
\begin{equation}
	\CI^{(\beta)}(q)=2\hat{Z}_0^{(\beta)}(q)\hat{Z}_0^{(\beta)}(1/q)+
	\hat{Z}_1^{(\beta)}(q)\hat{Z}_1^{(\beta)}(1/q)+
	\hat{Z}_2^{(\beta)}(q)\hat{Z}_2^{(\beta)}(1/q).
\end{equation}
Note, when $g>1$ the fundamental group $\pi_1(M_3)$ is non-abelian and $\CM_\text{flat}(M_3,SL(2,\C))$ has irreducible flat connections.
We confirmed, however, that the WRT invariant and the superconformal index both have a natural decomposition into contributions labelled by connected components of \textit{abelian} flat connections.\footnote{It is important to keep in mind that the terms in this decomposition are not merely contributions of the corresponding connected components of abelian flat connections to the path integral, but rather contain contributions of irreducible flat connections as well \cite{Gukov:2016njj}. In other words, even though the sum in the decomposition runs only over abelian flat connections, all flat connections are accounted properly, reducible and irreducible; no one is left behind.}
This ``completeness'' of the homological blocks is a striking and highly non-trivial phenomenon.
Its physical origin was already discussed in section \ref{sec:summary} from the viewpoint of resurgent analysis
and charges which label BPS states / enumerative invariants in the physical system \eqref{CatGeom1}.
It would be interesting to explore it further in various duality frames and from other vantage points.


\subsubsection{Comparison with refined CS}

In the notations of section~\ref{sec:refCS},
the partition function of refined Chern-Simons theory on $M_3=O(-p)\rightarrow \Sigma_g$ reads \cite{Aganagic:2011sg}:
\begin{multline}
	Z_{SU(2)}^\text{ref.~CS}[M_3]=\sum_{n=1}^{k-1} g^{g-1}_n\,(S_{1n})^{2-2g}(T_{nn})^{-p}=\\
	=
	\sum_{n=1}^{k-1}q^{-\frac{pn^2}{4}-\frac{pn\beta}{2}-\frac{p\beta^2}{4}}
	\prod_{j=0}^\beta (q^{-\frac{n+j+\beta}{2}}-q^{\frac{n+j+\beta}{2}})^{1-g}
	(q^{-\frac{n-j+\beta}{2}}-q^{\frac{n-j+\beta}{2}})^{1-g}.
\end{multline}
By repeating manipulations in section~\ref{sec:refCS}, we arrive at (up to a simple overall factor)
\begin{equation}
	Z_{SU(2)}^\text{ref. CS}[M_3]
	=\sum_{a,b\in \Z_p /\Z_2} e^{2\pi i (k+2\beta)\text{CS}(a)}\cdot
	S_{ab}\cdot \,\hat{Z}^\text{(ref.CS;$\beta$)}_b(q)
\end{equation}
with
\begin{multline}
	|\CW_a|\hat{Z}^\text{(ref.CS;$\beta$)}_a(q)=\text{v.p.}\int_{|z|=1}\frac{dz}{2\pi iz}\,(z^{\pm2};q)_{\beta+1}^{1-g}\sum_{n\in p\Z+a}q^{n^2/p}\,z^{2n}=\\
	=\left.\text{v.p.}\int_{|z|=1}\frac{dz}{2\pi iz}\,\left(\frac{(z^{\pm2};q)_\infty}{(z^{\pm2}qt;q)_\infty}\right)^{1-g}\sum_{n\in p\Z+a}q^{n^2/p}\,z^{2n}\right|_{t=q^\beta}
\end{multline}
where ``v.p.'' stand for principal value integration.
This indeed agrees with the partition function of $T[M_3]$ on $D^2\times S^1$, {\it cf.} (\ref{TCircFibBlock}),
\begin{equation}	 \hat{Z}^\text{(ref.CS;$\beta$)}_a(q)=\left.\hat{Z}_a(q,t,u)\cdot(qt;q)_\infty\,\prod_{i=1}^g\frac{(u_i;q)_\infty}{(tu_iq;q)_\infty}\right|_{t=q^\beta,u_i=1}.
\end{equation}



\subsection{${M_3}=\text{plumbed}$}
\label{sec:plumbed}

Now we move to consider another very large class of 3-manifolds $M_3(\Gamma)$ associated to a plumbing graph $\Gamma$. There are various ways to define $M_3$ for a given $\Gamma$. One of them is to say that $M_3$ is obtained by a Dehn surgery on the corresponding link $\CL(\Gamma)$ of unknots (see Figure~\ref{fig:plumbing-example}). For simplicity, we also assume that $\Gamma$ is connected. Such class of 3-manifolds contains Seifert fibrations over $S^2$, which correspond to star-shaped plumbing graphs. Denote by $L$ the number of vertices of $\Gamma$. It is equal to the number of components of the link $\CL(\Gamma)$. We will also need $L\times L$ linking matrix of $\CL(\Gamma)$ which will be denoted by $M$:
\begin{equation}
 M_{v_1,v_2}=\left\{
\begin{array}{ll}
 1,& v_1,v_2\text{ connected}, \\
 a_v, & v_1=v_2=v, \\
0, & \text{otherwise}.
\end{array}
\right.\qquad v_i \in \text{Vertices of }\Gamma \;\cong\;\{1,\ldots,L\}.
\label{linking}
\end{equation}
\begin{figure}[ht]
\centering
 \includegraphics[scale=3]{plumbing-example}
\caption{An example of a plumbing graph $\Gamma$ (left) and the corresponding link $\CL(\Gamma)$ of framed unknots in $S^3$ (right). The associated 3-manifold $M_3(\Gamma)$ can be constructed by performing a Dehn surgery on $\CL(\Gamma)$.}
\label{fig:plumbing-example}
\end{figure}


The first homology group of $M_3(\Gamma)$ is given by the cokernel (over $\Z$) of the linking matrix:
\begin{equation}
H_1(M_3,\Z) \cong \Coker M = \Z^L/M\Z^L.
\end{equation}
In what follows we assume for simplicity that $M_3(\Gamma)$ is a rational homology sphere ($b_1(M_3)=0$), which implies that $\Gamma$ has no loops ({\it i.e.} it is a tree). The linking form on $H_1(M_3,\Z)$ is then given by
\begin{equation}
\lk(a,b) =(a,M^{-1}b)\;\mod \Z,\qquad a,b\in  \Z^L/M\Z^L.
\end{equation}
Different plumbing graphs can give homeomorphic 3-manifolds --- $M_3(\Gamma)\cong M_3(\Gamma')$ \textit{iff} $\Gamma$ and $\Gamma'$ can be connected by a sequence of 3d Kirby moves, as shown in Figure~\ref{fig:moves}\footnote{There is also a move which relates a connected graph to a disconected one. For the sake of brevity we don't discuss the case of disconnected plumbing graphs here.}.
\begin{figure}[ht]
\centering
\includegraphics[scale=1.7]{move1}
\includegraphics[scale=1.7]{move2}
\includegraphics[scale=1.7]{move3}
\caption{3d Kirby moves that relate plumbing graphs which result in homeomorphic 3-manifolds.}
\label{fig:moves}
\end{figure}

The theory $T[M_3,SU(2)]$ can in principle be obtained by combining together the following 3d theories (see \eg~\cite{Gadde:2013sca}):
\begin{itemize}
	\item edge: $S$-duality wall in $\CN=4$ $SU(2)$ super-Yang-Mills ({\it i.e.} theory $T[SU(2)]$),
	\item 2-valent vertex: $T^a$-duality wall $~=~$ ``supesymmetric Chern-Simons term at level $a$,''
	\item $n$-valent vertex: $T[(\text{sphere with $n$ holes})\times S^1]$ =  $n$ copies of $T[SU(2)]$ gauged together.
\end{itemize}



\subsubsection{Homological blocks ${\hat{Z}_a}$}
\label{sec:plumbing-blocks}

The homological blocks can be calculated by the following formula (see appendix~\ref{app:Zq-from-WRT} for a derivation):
\begin{multline}
	\hat{Z}_b(q)=q^{-\frac{3L+\sum_v a_{v}}{4}}\cdot\text{v.p.}\int\limits_{|z_v|=1}
\prod_{v\;\in\; \text{Vertices}}
\frac{dz_v}{2\pi iz_v}\,
\left({z_v-1/z_v}\right)^{2-\text{deg}(v)}\cdot\Theta^{-M}_b(z)
	\\
	\equiv q^{-\frac{3L+\sum_v a_{v}}{4}}\cdot\text{v.p.}\int\limits_{|z_v|=1}
\prod_{v\;\in\; \text{Vertices}}
\frac{dz_v}{2\pi iz_v}\,
\left({z_v-1/z_v}\right)^{2}\times\\
\times\prod_{(v_1,v_2)\in \text{Edges}}\frac{1}{(z_{v_1}-1/z_{v_1})(z_{v_2}-1/z_{v_2})}
\cdot\Theta^{-M}_b(z)
	\label{Z-hat-def-0}
\end{multline}
where $\text{deg}(v)$ is the degree of a vertex $v$ and, as before, ``v.p.'' means taking principle value integral (\ie~take half-sum of contours ``dodging'' poles from both sides) and $\Theta^{-M}_b(x)$ is the theta function of the lattice corresponding to minus the linking form $M$ given by
\begin{equation}
	\Theta^{-M}_b(x)=\sum_{\ell \in 2M\Z^L+b}q^{-\frac{(\ell,M^{-1}\ell)}{4}}
	\prod_{i=1}^Lx_i^{\ell_i}.
\end{equation}

{\bf Remarks on} \eqref{Z-hat-def-0} {\bf :}
\begin{enumerate}

\item In the special case when the plumbing graph has just one vertex, the expression for the homological block reduces to (\ref{BlockBeta1}) with $\beta=0$.
	
\item Generically it is well-defined only if $M$ is negative definite, \ie~$M_3(\Gamma)$ is a link of a normal singularity, with $\Gamma$ being a resolution graph of the singularity.
	
\item The formula (\ref{Z-hat-def-0}) defines homological blocks $\hat{Z}_a(q)$ in terms of a plumbing graph $\Gamma$, but one can show that they are invariant under Kirby moves (Figure~\ref{fig:moves}) acting on $\Gamma$. Therefore, $\hat{Z}_a(q)$ actually depends only on the homeomorphism class of $M_3(\Gamma)$, and is indeed a topological invariant. A priori this is not obvious, since (\ref{Z-hat-def-0}) has been obtained (see Appendix  \ref{app:Zq-from-WRT}) as an analytic continuation of WRT invariant, which, in principle, does not have to be unique.
	
\item Even though the formula has the structure of the ``index of a quiver theory'', it is not clear how to properly realize it as a partition function of $T[M_3(\Gamma)]$ on $D^2_b\times S^1$ with some boundary condition.
				
\item Suppose $M<0$. Then $\hat{Z}_a(q)$ is a well-defined series in $q$ convergent in the unit disk $|q|<1$. Unless $M_3$ is a Lens space, $\hat{Z}_a(q)$ does not admit analytic continuation (in the usual sense) outside of $|q|<1$ due to Fabry gap theorem (because the powers of $q$ with non-zero coefficients grow quadratically).

\item We have
	\begin{equation}
	\hat Z_b(q)
	\;\in\; 2^{-c}q^{\Delta_b}\Z[[q]]
	\end{equation}
	where
	\begin{equation}
	 c\in \Z_+,\qquad c\leq L,
	\end{equation}
	\begin{equation}
	  b\in (2\text{Coker}\,M+\delta)\,/\Z_2
	\stackrel{\text{Set}}{\cong} H_1(M_3,\Z)\,/\Z_2,
	\end{equation}
	\begin{equation}
	    \delta\in \Z^L/2\Z^L,\qquad \delta_v = \text{deg}\,v \mod 2.
	\end{equation}
	\begin{equation}
	 \Delta_b=-\frac{3L+\sum_v a_{v}}{4}-\max_{\ell \in 2M\Z^L+b}\frac{(\ell,M^{-1}\ell)}{4}\,\in \Q
	\end{equation}
	where $\Z_2$ acts as
	\begin{equation}
	 b\mapsto -b
	\end{equation}
	and is a symmetry of (\ref{Z-hat-def-0}).
	
\end{enumerate}

\paragraph{Example 1:}
\begin{equation}
	\includegraphics{plumbing-E8}
\end{equation}
\begin{equation}
	H_1(M_3)=0
\end{equation}
\begin{equation}
	\hat{Z}_0=q^{-3/2}(1-q-q^3-q^7+q^8+q^{14}+q^{20}+q^{29}-q^{31}-q^{42}+\cdots)
\end{equation}


\paragraph{Example 2:}
\begin{equation}
{\,\raisebox{-2.0cm}{\includegraphics[width=8.0cm]{plumbing-2a}}\,}
\stackrel{\text{Kirby}}{\sim}
{\,\raisebox{-2.0cm}{\includegraphics[width=4.0cm]{plumbing-2b}}\,}

\end{equation}
\begin{equation}
	H_1(M_3)=\Z_{3}
\end{equation}
\begin{equation}
	\hat{Z}=
	\left(
	\begin{array}{c}
	 1-q+q^6-q^{11}+q^{13}-q^{20}+q^{35}+O\left(q^{41}\right) \\
	 q^{5/3}\left(-1+q^3-q^{21}+q^{30}+O\left(q^{41}\right)\right) \\
	\end{array}
	\right)
\end{equation}

\paragraph{Example 3:} (non-Seifert)
\begin{equation}
	\includegraphics{plumbing-1}
\end{equation}
\begin{equation}
	H_1(M_3)=\Z_{13}
\end{equation}
\begin{equation}
	\hat{Z}=
	\frac{1}{4}\left(\tiny
	\begin{array}{c}
	q^{-1/2}(2-2q+2q^2-2q^4+4q^5+6q^{10}+8q^{11}-4q^{13}+2q^{14}+4q^{15}+O\left(q^{18}\right)) \\
	q^{5/26}(-3+2q+2q^2-4q^3-2q^7-q^8+2q^9-q^{10}+2q^{12}-4q^{13}+2q^{16}+O\left(q^{18}\right)) \\
	q^{7/26}(4+q+2q^3-2q^4-2q^6-3q^7-2q^8-2q^{10}-q^{11}-2q^{13}-4q^{14}-2q^{15}-4q^{16}+O\left(q^{18}\right)) \\
	q^{-7/26}(-3-3q^2+2q^4-2q^5+4q^7+2q^8+2q^9+2q^{10}+4q^{12}+4q^{13}+4q^{14}+2q^{15}+O\left(q^{18}\right)) \\
	q^{-11/26}(-1+2q-2q^2+4q^3-3q^6-2q^7+4q^8-2q^9+2q^{11}+2q^{13}+q^{14}-2q^{16}+O\left(q^{17}\right)) \\
	q^{-5/26}(2+2q^2-q^3-3q^5-2q^6+2q^7-4q^8-2q^{10}-2q^{11}-2q^{12}-2q^{13}-5q^{15}-2q^{16}+O\left(q^{17}\right))\\
	 q^{-15/26}(-1-2q+2q^2-q^4+2q^6-2q^7+2q^8+4q^{10}+2q^{12}+2q^{13}+2q^{15}+O\left(q^{17}\right)) \\
	\end{array}
	\right)
\end{equation}


\subsubsection{Problems on the ${T[M_3]}$ side}

One may wish to carry out the categorification program for $M_3(\Gamma)$ as well. However, it is not obvious how to write a correct expression for superconformal or topologically twisted index of the 3d $\CN=2$ theory $T[M_3]$ because the UV description with $\CN=2$ supersymmetry of its certain components (see the paragraph above Section~\ref{sec:plumbing-blocks}) is not known. In particular, there is no known Lagrangian description for half-BPS T-duality walls in $\CN=4$ super-Yang-Mills theory, and understanding the theory $T[M_3(\Gamma)]$ and its Hilbert space poses a challenge. We hope to study this problem in the future.

Let us note that a certain expression of the superconformal index of $T[M_3]$, with $M_3$ being an $SL(2,\Z)$-mapping class torus of punctured $T^2$ (which, without a puncture, would be homeomorphic to $M_3(\Gamma)$ with circular plumbing $\Gamma$) was considered in \cite{Gang:2012ff,Gang:2013sqa}. In particular, there it was checked that it was invariant under the first two of the Kirby moves in Figure~\ref{fig:moves} that correspond to relations in the $SL(2,\Z)$ group. However, as it was argued in \cite{Gang:2013sqa} it coincides with the result given by triangulation decomposition, as in \cite{Dimofte:2011ju,Dimofte:2011py}, and therefore, if interpreted as the partition function of the complex Chern-Simons theory, it misses contributions of the reducible flat connections \cite{Chung:2014qpa}. The latter as we have seen, play a major role for categorification of WRT invariant. Also, in principle one can extend their prescription for calculating superconformal indices associated with plumbing graphs with vertices of degree other than two, by requiring invariance under the third Kirby move in Figure~\ref{fig:moves}.





\section{Adding knots and links into ${M_3}$}

The goal of this section is to incorporate knots and links in a non-trivial 3-manifold $M_3$
and produce the corresponding homological invariants.
In particular, it will give us the very first examples where {\it both} knots and 3-manifolds are non-trivial.

The physical setup that we use to make concrete predictions for the new homological invariants $\CH_a[M_3;K,\CR]$
was already briefly mentioned in \eqref{conifoldphases}. As before, $K$ denotes a knot in $M_3$ while $\CR$ denotes a representation (color) of CS gauge group $G$. The case of links is similar and involves assigment of color to each component of the link. The space $\CH_a[M_3;K,\CR]$ can be explored from a number of vantage points
and in a variety of duality frames (all of which lead to the same result). In particular, from the vantage point
of the theory $T[M_3]$ on fivebrane world-volume, incorporating knots and links corresponds to introducing
a 1d defect (``impurity'') which preserves the same supersymmetry as the background along $D^2 \cong \R^2_q$
in our previous discussion, {\it cf.} Figure~\ref{fig:impurity}.

Alternatively, starting from the brane system \eqref{CatGeom1}, there are many possibilities \cite{Gukov:2015gmm}
to accommodate knots inside $M_3$. We focus on those which give rise to line operators in $T[M_3]$.\footnote{The other options lead to a 3d ``space-time filling defect,'' deforming the theory to a new one $T[M_3,K]$.} They correspond to codimension-four defects in the 6d (2,0) theory, engineered by either M2- or M5-branes (see \eg~\cite{Gang:2015bwa} for a discussion in the context of 3d-3d correspondence). For example, one can insert a stack of M2-branes in the following way:
\beq
\begin{matrix}
{\mbox {\textrm{$N$ fivebranes:}}}~~~\qquad & \R & \times & M_3& \times & D^2  \\ \qquad & &
&   \cap &  & \cap \\
{\mbox{\rm space-time:}}~~~\qquad & \R&  \times  & T^*M_3 & \times & TN   \\ \qquad & &
&   \cup &  & $\rotatebox[origin=c]{90}{$\in$}$ \\
{\mbox{\rm M2-branes:}}~~~\qquad &\R & \times & T^*K & \times  & O   \\
\end{matrix}.
\label{CatGeom2}
\eeq
We have chosen the line defect in $T[M_3]$ to sit at the tip $O\in D^2$ (also the Taub-NUT center) to preserve the $U(1)_q$ rotational symmetry.
Naively, the way the stack of M2-branes ends on $N$ fivebranes is determined by a partition of the number of M2 branes into $N$. Such partitions are in one-to-one correspondence with Young tableaux with at most $N$ rows, which are in turn can be identified with irreducible representations of $U(N)$. In the case of $SU(N)$ we have to mod out configurations where M2 branes are equally distributed among $N$ fivebranes. This leads to Young tableaux with at most $N-1$ rows that label irreducible representations of $SU(N)$.
In reality, mapping line operators in 3d/3d correspondence and in the fivebrane setup is a delicate business and should be dealt with care.

If one wishes to use M5-branes to represent knots, then besides $\R_{\text{time}}\times K$ they would also occupy
the two-dimensional co-normal bundle $N^*K$ of $K$ inside $T^*M_3$ and the cotangent space $T^*|_O$ to $D^2$ at $O$ \cite{Ooguri:1999bv}.
Both constructions, based on M2- and M5-branes, lead to Wilson loops --- in fact,
they are related by the Hanany-Witten type effect in M-theory or, in TQFT on $M_3$, by the Fourier transform
from representation basis to holonomy basis.

Using this physical setup, we compute the new homological invariants $\CH_a[M_3;K,\CR]$ for some simple examples
of non-trivial knots and 3-manifolds. In particular, we verify that suitable variants of the Conjectures~\ref{Conjecture1} and \ref{Conjecture2}
hold in the presence of knots and links.


\subsection{Links in ${M_3}$ and line operators in ${T[M_3]}$}
\label{sec:knots}

Consider a knot $K$ in $M_3$ colored by a representation $\CR$ of $G$.
As described above, it corresponds to a certain half-BPS line operator $\Gamma_{K,\CR}$ in $T[M_3;G]$:
\begin{equation}
	(K,\CR)\;\longmapsto \; \Gamma_{K,\CR}\;\in\;\CC.
	\label{Knots-LineOps}
\end{equation}
where $\CC$ is the category of BPS line operators in $\CN=2$ SCFT $T[M_3,G]$.
The homological invariant for a combined system of a knot and a 3-manifold
is then given by the BPS Hilbert space of $T[M_3]$ on the disk $D^2$ with $\Gamma_{K,\CR}$ inserted at $O$,
the center of the disk (see Figure~\ref{fig:impurity}):
\begin{equation}
	\CH_a[M_3;K,\CR]\equiv \CH_{T[M_3]}(D^2,\Gamma_{K,\CR};a),\qquad a\in (\text{Tor}\,H_1(M_3,\Z))^N/S_N
\end{equation}
where $a$ denotes the choice of boundary condition, the same as in the case without a knot.
It has the same gradings as before, namely the $q$-grading $i$ and the homological (R-charge) grading $j$:
\begin{equation}
	\CH_a[M_3;K,\CR]=\bigoplus_{i\in \Delta_a+\Z,\,j\in\Z}\CH_a^{i,j}[M_3;K,\CR]
\end{equation}
And, as before, the graded Euler characteristic gives the partition function on $D^2\times S^1$:
\begin{equation}
	\hat{Z}_a(q;\Gamma_{K,\CR})\equiv Z_{T[M_3]}(D^2\times S^1,\Gamma_{K,\CR};a)=
	\sum_{i,j}(-1)^jq^i\CH_a^{i,j}[M_3;K,\CR]
\end{equation}
now, in 3d $\CN=2$ theory $T[M_3]$ with an extra 1d ``impurity'' $\Gamma_{K,\CR}$ supported on $O\times S^1$.
The analogue of the Conjecture \ref{Conjecture1} is then the following:
\begin{conj}
The WRT invariant of $M_3$ with a knot $K$ colored by representation $\CR$ can be decomposed into the following form:
\begin{equation}
	Z_{SU(2)_k}[M_3;K,\CR]=(i\sqrt{2k})^{b_1(M_3)-1}\sum_{a,b\;\in \;\atop\Tor H_1(M_3,\Z)/\Z_2}e^{2\pi ik\lk(a,a)}\,S_{ab}
	\, \hat{Z}_b(q;\Gamma_{K,\CR})|_{q\rightarrow e^{\frac{2\pi i }{k}}}
	\label{WRT-knot-decomposition}
\end{equation}
where
\begin{equation}
	\hat{Z}_b(q;\Gamma_{K,\CR}) \in \, 2^{-c} q^{\Delta_b} \Z[[q]]\qquad \Delta_b\in \Q,\qquad c\in\Z_+
	\label{Block-knot-qSeries}
\end{equation}
convergent in $|q|<1$ and $S_{ab}$ is the same as in Conjecture \ref{Conjecture1}
\label{Conjecture3}
\end{conj}
For certain 3-manifolds with an extra symmetry, preserved by the knot $K$, we have an extra grading whose value we denote by $\ell$:
\begin{equation}
	\CH_a[M_3;K,\CR]=\bigoplus_{i\in \Delta_a+\Z,\,j,\ell\in\Z}\CH_a^{i,j;\ell}[M_3;K,\CR]
\end{equation}
In practice, to compute these homological invariants, one needs a convenient ultra-violet (UV) description of
the fivebrane setup \eqref{CatGeom2} or, better yet, of the IR superconformal theory $T[M_3]$.
In general, the brane system \eqref{CatGeom2} and the 3d theory $T[M_3]$ may admit many such UV descriptions,
in various duality frames, all of which flow to the same IR physics and produce the same homological invariants (space of BPS states).

In a given UV gauge theory description of $T[M_3]$,
the objects in the tensor category $\CC$ of BPS line operators can be understood as vector spaces ---
the ``Hilbert spaces of $\CN=2$ quantum mechanics on the line, coupled to the bulk gauge theory''.
The most familiar line operators are Wilson operators $W_\lambda$, labeled by a representation $\lambda$
of the UV gauge group\footnote{In general, $\CG$ is different from $G$.
For a quiver theory, it may be given by a product $\times_i G_i$ over the vertices.} $\CG$ (which, in general, has little to do with $G$).
The corresponding object of the category $\CC$ is, tautologically, the representation $\lambda$.
The Wilson lines are expected to form a complete basis of line operators in the IR theory,
in the sense that any line operator (not necessarily associate to a knot) should have the following decomposition:
\bea

\overbrace{\rule{1.0cm}{0pt}}^{\text{IR}} &  & ~~~\overbrace{\rule{2.5cm}{0pt}}^{\text{UV}} \label{Line-UV} \\
\Gamma_{K,\CR} & ~=~ & \bigoplus_{\lambda,i,j,\ell} W_\lambda\otimes \CH_{K,\CR}^{\lambda;i,j;\ell} \,. \nonumber
\eea
The reason is very simple --- one can always decompose the ``defect Hilbert space'' into representations of $\CG$,
with the multiplicity space $\CH_{\Gamma}^{\lambda}$ associated with the representation $\lambda$.
The symmetry $\CG$ plays the role of the flavor symmetry in QM on the line, which couples to 3d theory $T[M_3]$ by gauging $\CG $ in the bulk.
If $\Gamma$ is a generic physical line operator (\textit{cf.} superposition of physical line operators),
the corresponding multiplicity spaces $\CH_{\Gamma}^{\lambda}$ are honest vector space that are at least doubly-graded,
with the $(i,j)$-grading coming from $U(1)_q\times U(1)_R$ symmetry of the brane system \eqref{CatGeom2}.
When the flavor symmetry $U(1)_{\beta}$ is a symmetry of both $T[M_3]$ and $\Gamma$, the third $\ell$-grading is also present.

As a trivial example, consider a line defect given by a quantum mechanics that is completely decoupled from the bulk. Then,
\be
\Gamma_{\text{QM}} \; = \; W_0\otimes \CH_{\text{QM}} \,,
\label{babyexmpl}
\ee
where $\CH_{\text{QM}}$ is the Hilbert space of the quantum mechanics and $W_0$ is the trivial Wilson loop. So, we see that \eqref{Line-UV} has a chance of being correct, even if there are infinitely many possibilities of engineering defects via 1d-3d coupled systems. In this sense, $\lambda$ is analogous to the label ``$a$'' of the homological blocks, which reduces infinitely many possible boundary conditions to a finite set. In fact, this isn't just an analogy --- it comes from the equivalence of two categories
\be\label{C=CB}
\CC\cong \CC_B.
\ee
Namely, a line operator can be viewed as the interface between two boundary conditions, and picking a ``reference boundary condition'' (\eg~the one giving $\hat{Z}_0$ with zero brane charge) will identify the two categories. This equivalence is a special feature of 3d quantum field theories, which associate categories to $S^1$, with the objects that can be interpreted either as line operators or as boundary conditions at spatial infinity.

At this point, $\lambda$ can still be an arbitrary representation of the UV gauge group $\CG$, and one might naively think that $\CC$ is
\be\label{CUV}
\CC_{\text{UV}}=\mathrm{Rep}(\CG),
\ee
given by the representation category of $\CG$. But in light of the equivalence \eqref{C=CB}, we expect $\CC$ to be much smaller, since $\CC_B$ is generated by finitely many simple objects (boundary conditions that give homological blocks), as we have seen in all our examples.

Indeed, \eqref{CUV} is often redundant, due to presence of Chern-Simons couplings in $T[M_3]$. There is a set $\Lambda_{M_3}$ of ``integrable representations'' of $\CG$ giving a complete basis of $W_\lambda$ in $T[M_3;G]$, and every Wilson loop labeled by a non-integrable representation can be decomposed as
\be\label{WilsonDec}
W_{\nu}=\bigoplus_{\lambda\in \Lambda_{M_3}\atop i,j,\ell\in\Z}W_{\lambda}\otimes \CH_{\nu}^{\lambda;i,j;\ell}.
\ee
All such relations generate an ideal (in the categorical sense) of $\CC_{\text{UV}}$, and $\CC$ is given by the quotient
\begin{equation}
	\CC=\CC_{UV}/\CI. 	
\end{equation}
As a vector space, $\CC$ is the same as $\Lambda_{M_3}\otimes\C$, but the algebra structure depends on $\CI$ and is determined by the theory $T[M_3]$ in a non-trivial way. Both $\CC_{\text{UV}}$ and $\CI$ depend on the duality frame (presentation of $M_3$), but it is expected that the quotient category $\CC$ is a topological invariant of $M_3$. It describes line operators / boundary conditions in the IR theory, which is what usually meant by $T[M_3]$.

We expect, for arbitrary $M_3$, the independent Wilson loops in the theory $T[M_3;G]$ are labeled by elements in\footnote{So far, we have ignored the difference between $G$ and the Langlands dual group $G^\vee$ because the quantities considered so far are not sensitive to the global structure of the group. However, the spectrum of Wilson loops is sensitive to this difference, and \eqref{WilsonCharge} is stated for the adjoint form $G=G_{\text{ad}}$. If $G$ has a center, one needs to add the representations of $G$ where the center acts non-trivially. Reader interested in this subject may consult \cite{EVFCBI} where this issue was extensively discussed in a similar brane system.\label{ft:Global}}
\be\label{WilsonCharge}
\Lambda_{M_3}=\mathrm{Tor}\,H_1(M_3,\Lambda_{\text{rt}})/W_G,
\ee
where $\Lambda_{\text{rt}}$ is the root lattice of $\frak{g}$ and $W_G$ is the Weyl group (not to be confused with Wilson line $W_{\lambda}$ in UV description of $T[M_3]$). The argument for this statement parallels our discussion of boundary conditions given by M2-brane charges ``$a$'', which take values in exactly the same set. And the fundamental Wilson loops are expected to come from knots $K$ wrapping torsion 1-cycles, colored by a representation $\CR$ of $G$ (\ie~$\CR\in \Lambda_{\text{char}}(G)/W_G$).

If $G$ is abelian, then $\Lambda_{M_3}$ is a group and one can introduce an action of line operators on boundary conditions, which we call the {\it shift} action in what follows. This action is expected because Wilson line operators $W_\lambda,\;\lambda\in \Lambda_{M_3}$, can be engineered using M2-branes\footnote{{\it i.e.} $W_\lambda=\Gamma_{K,\CR}$ when torsion homology class of $\CR$-cable of $K$ is given by $\lambda\in  \Lambda_{M_3}$} as in \eqref{CatGeom2}, and the label ``$a$'' for homological blocks also measures M2-brane charges.
In other words, a Wilson loop $W_\lambda$ relates two Hilbert spaces
\be
\CH_{T[M_3]}(D^2,W_\lambda;a) \; \sim \; \CH_{T[M_3]}(D^2,W_\lambda;a-\lambda).
\ee
One does not \textit{a priori} know whether this is an isomorphism or not, or how the gradings on the two sides are related.
However, in various examples below we observe that, at the level of homological blocks $\hat{Z}_a(q)$,
Wilson loop acts as a simple shift operator, even for $G=SU(2)$ if the Weyl group action is properly taken into account.

As before, our main tools for probing the new homological invariants are SUSY-protected quantities.
In particular, using a UV descriptions of $T[M_3]$ and a half-BPS impurity $\Gamma_{K,\CR}$,
one can compute the partition function of $T[M_3]$ on $D^2\times S^1$ with $\Gamma_{K,\CR}$ inserted along $O\times S^1$ as follows:
\begin{multline}\label{BlockKnot}
	\hat{Z}_a(q,t;\Gamma_{K,\CR})\equiv Z_{T[M_3]}(D^2\times S^1,\Gamma_{K,\CR};a)=\\ =\int \frac{dz}{2\pi i z}
	\,[\text{same as without $\Gamma_{K,\CR}$}] \sum_{\lambda\in \Lambda_{M_3}\atop i,j,\ell \in\Z}\chi_\lambda(z)q^it^\ell(-1)^{j}
	\dim\CH_{K,\CR}^{\lambda;i,j;\ell}
\end{multline}
where $z$ stands for the gauge fugacities of the UV gauge group $\CG$
and $\chi_\lambda$ is the character of the $\CG$-representation $\lambda$.

Similarly, we can consider the $S^2 \times S^1$ superconformal index with half-BPS impurities inserted at one (or both) poles of $S^2$.
The UV localization formula for the index is modified as follows (when the impurity is at the north pole):
\begin{multline}\label{IndexKnot}
	\CI(q,t;\Gamma_{K,\CR})\equiv Z_{T[M_3]}(S^2\times S^1;\Gamma_{K,\CR})= \\ =\sum_{m}\int \frac{dz}{2\pi i z}
	\,[\text{same as without $\Gamma$}] \sum_{\lambda\in\Lambda_{M_3} \atop i,j,\ell \in \Z}\chi_\lambda(zq^{m/2})q^i t^\ell (-1)^{j}
	\dim\CH_{K,\CR}^{\lambda;i,j;\ell}.
\end{multline}
As we demonstrate in a variety of examples, it obeys the modified factorization formula
\begin{equation}
\CI(q,t;\Gamma_{K,\CR}) \; = \; \sum_a|\CW_a| \hat{Z}_a(q,t;\Gamma_{K,\CR})\hat{Z}_a(q^{-1},t^{-1}) \,.
\end{equation}
Note, all of the above relations depend only on the IR data, namely on $K$ and its color $\CR$, not on the UV description of $\Gamma_{K,\CR}$.
In particular, note that $\lambda$ is always summed over in these relations, which goes back to the basic relation
between IR line operators $\Gamma_{K,\CR}$ (``impurities'') and their description \eqref{Line-UV} in the UV theory via $W_{\lambda}$.

The reader should keep in mind that there are two non-trivial maps (dualities) involved in the study of knots.\footnote{This aspect is
a surprising exception to the rule that knot homology is easier than 3-manifold homology.}
First, there is a rather non-trivial map \eqref{Line-UV} between line operators in the IR theory $T[M_3]$
and its UV description (or, rather, one of many UV descriptions).
This UV/IR map has nothing to do with applications to low-dimensional topology and is a standard phenomenon in quantum field theory.
In addition, there is a map between knots and links colored by $\CR$ in a TQFT on $M_3$
and half-BPS line operators (``impurities'') in the 3d $\CN=2$ theory $T[M_3]$.
This map is a chapter in the so-called 3d/3d correspondence.
The reason one should pay attention to both of these maps is that it is their composition which relates
homological invariants of $K \subset M_3$ to concrete calculations in $T[M_3;G]$,
$$
\boxed{{\text{UV line} \atop \text{operators}~W_{\lambda}}}
\quad \xleftrightarrow[~]{\text{UV/IR map}} \quad
\boxed{{\frac12\text{-BPS impurity} \atop \Gamma_{K,\CR} }}
\quad \xleftrightarrow[\text{~}]{\text{3d/3d correspondence}} \quad
\boxed{{\text{link}~K \subset M_3 \atop \text{colored by}~\CR}}
$$
Because each of these maps can be rather non-trivial, one should not confuse the representation $\lambda$
that labels half-BPS line operators in the UV description with the ``color'' of $K$.
The latter is denoted by $\CR$ and, whenever non-trivial, leads to the $\CR$-colored link homology \cite{Gukov:2011ry,Fuji:2012pm}
in our setup \eqref{CatGeom2}.

So far, the discussion in this section is very general and, as such, may be somewhat abstract.
We will now give some very concrete examples for $G=SU(2)$.


\subsection{Links in $S^2\times S^1$ and Rozansky's proposal}
\label{sec:Roz}

For $M_3=S^2\times S^1$, the theory $T[M_3]$ is a particular case of (\ref{TCircFib}) with $p=0$ and $g=0$, that is the theory of 3d $\CN=2$ vector multiplet with gauge group $\CG=G=SU(2)$. In this case  $\mathrm{Tor}\,H_1(M_3,\Z)=0$ and the only independent Wilson loop in $T[M_3]$ is the trivial Wilson loop. Also, there is only one homological block $\hat{Z}_0$. Therefore, for an arbitrary representation $\lambda$ of $SU(2)$,
the decomposition \eqref{WilsonDec} allows to write the Wilson loop $W_\lambda$ as \eqref{babyexmpl}:
\be
W_\lambda \; = \; W_0\otimes \CH_{\lambda}^{0;i,j;\ell} \,.
\ee
In other words, in this case we expect a factorization
\begin{equation}
\CH_a[S^2\times S^1;K^{\lambda},\CR_\lambda] \; = \; \bigoplus_{i,j,\ell\in\Z}\CH_{\lambda}^{0;i,j;\ell}\otimes {\CH}_a[S^2\times S^1]
\end{equation}
where the first factor on the right-hand side is the $S^2\times S^1$ analogue of the Khovanov-Rozansky homology
of the corresponding link $K^{\lambda}$ colored by $\CR_{\lambda}$. What is $K^{\lambda}$? And, what is $\CR_{\lambda}$?

As we shall see below, already in this relatively simple case of $M_3 = S^1 \times S^2$ the map between
colored knots and links in $M_3$ and the UV line operators $W_{\lambda}$ in $T[M_3]$ is rather non-trivial.
Since Wilson loops in $T[M_3]$ come from M2-branes wrapping the $S^1$ circle of $S^1 \times S^2$,
we expect that the precise dictionary $W_{\lambda} \leftrightarrow (K^{\lambda}, \CR_{\lambda})$
maps $\lambda$ to a certain link in $M_3$ that winds around $S^1$,
and the total winding number (counted with multiplicities given by $\CR_{\lambda}$) is equal to $|\lambda|$.
Regarding $M_3 = S^1 \times S^2$ as a special case of the Hopf fibration (namely, the trivial fibration),
in the rest of this section we present evidence for the following identification\footnote{Note,
in the unrefined / decategorified setting, $K^{\lambda}$ is simply the unknot colored by $\CR_{\lambda} = \lambda$.
Although this is no longer the case in homological world, there is still a close relation between ``cabling''
and ``color'' \cite{khovanov2005categorifications,Gukov:2005qp}.}
\be
\boxed{\phantom{\int}
W_\lambda \quad \leftrightarrow \quad (K^{\lambda}, \CR_{\lambda}) \; = \; \text{``$\lambda$-cable'' of the unknot along the Hopf fiber}
\phantom{\int}}
\label{Gamma-Lp1}
\ee
Specifically, $\lambda = {\square}^{\otimes 2n}$ corresponds to a link $L_{2n}$ made of $2n$ copies of the unknot
along the Hopf fiber, all colored by the fundamental representation of $SU(2)$.
And $(K^{\lambda}, \CR_{\lambda})$ for general $\lambda$ is a linear combination of $L_{2n}$'s
that replicates the decomposition of $\lambda$ into ${\square}^{\otimes 2n}$'s.
Such decomposition is usually referred to as the ``cabling formula'' (see Appendix~\ref{app:cabling}).

Curiously, a similar problem was already considered by Rozansky from a purely mathematical point of view in \cite{rozansky2010categorification}.
Specifically, the Conjecture~6.10 in \cite{rozansky2010categorification} gives a concrete description for the homological invariant
of the link $L_{2n}$.
We shall verify that Rozansky's proposal\footnote{The Conjecture~6.10 in \cite{rozansky2010categorification} contains a typo in the description of the ideal $I_{\text{rel}}$. Namely,
\be\label{OldRelation}
a_i p_i({\bf x})=\theta_i p_i({\bf x})=0
\ee
should be replaced by
\be\label{NewRelation}
a_i p_{n-i+1}({\bf x})=\theta_i p_{n-i+1}({\bf x})=0.
\ee
} matches exactly with the quantum field theory computation if the generators $a_i$ and $\theta_i$ are assigned flavor charges $i$, that is
\be
\mathrm{deg}_t \, a_i=\mathrm{deg}_t \, \theta_i=i.
\ee

Using the decomposition of tensor products of $SU(2)$ representations, we can write the expectation value of $2n$ Wilson loops in $T[M_3]$
as a sum over expectation values of Wilson loops labeled by irreducible representations. Only even representations with highest weight $2l=0,2,\ldots,2n$ appear in this decomposition:
\be\label{WilsonDec1}
\langle W_{{\square}^{\otimes 2n}}\rangle =\sum_{l=0}^n \left[{{2n}\choose {n-l}}-{{2n}\choose {n-l-1}}\right] \langle W_{2l}\rangle.
\ee
The expectation value of the Wilson loop $W_{2l}$ in $T[M_3]$,
which gives the graded Euler characteristic of $\CH_\lambda$,\footnote{In this normalization, we have
\be\label{WilsonNorm}
\langle W_0\rangle=1,
\ee
enabling us to directly extract the information about the space $\CH_{\lambda}^{i,j;\ell}$.}
\be
\sum_{i,j,\ell}(-1)^jq^it^\ell\dim\CH_\lambda^{0;i,j,\ell} \equiv\chi_{q,t}(\CH_\lambda)=\langle W_{2l}\rangle\equiv \frac{\hat{Z}_0(q,t;W_{2l})}{\hat{Z}_0(q,t)}
\ee
can be computed using \eqref{BlockKnot}, with $T[S^1\times S^2,SU(2)]$ now being the 3d $\CN=4$ super-Yang-Mills theory.
We obtain
\begin{equation}
	\langle W_{2l}\rangle \; = \; \frac{(qt)^{l} (1/t;q)_l}{(q^2t;q)_l},
\end{equation}
and the expectation values of $W_{2l+1}$ all vanish.

On the other hand, as a vector space, the homological invariant $H^\bullet(S^1\times S^2,L_{2n})$ proposed in Conjecture~6.10 of \cite{rozansky2010categorification} admits a similar decomposition into subspaces of pure ${\bf x}$-degree\footnote{This decomposition doesn't respect the ring structure as each subspace is not closed under multiplication.}
\be
H^\bullet_{\text{Rozansky}}(L_{2n})=\bigoplus_{l=0}^{n} V_l \otimes \Q[a_1,\theta_1,a_2,\theta_2,\ldots, a_l,\theta_l].
\ee
Here, $V_l$ is a quotient of the vector space spanned by monomials of $x_1,\ldots,x_{2n}$, with degree $n-l$, by the relations
\be
x_i^2=0 \quad \text{and} \quad \sum_{i=1}^{2n} x_i=0.
\ee
It is easy to check that\footnote{Basically, there are ${{2n}\choose {n-l}}$ non-vanishing degree $(n-l)$ monomials, and they are subject to ${{2n}\choose {n-l-1}}$ independent relations, obtained by multiplying $\sum_i x_i$ with degree $(n-l-1)$ monomials.}
\be
\dim V_l= {{2n}\choose {n-l}}-{{2n}\choose {n-l-1}}
\ee
are exactly the coefficients in \eqref{WilsonDec1}. In particular, $V_j$ with $j<0$ is empty, and the dimension of $V_0$ is given by the $n$-th Catalan number.
Then
\be\label{EquiEuler2}
\chi_t(H^\bullet)=\sum_{j=0}^n \dim V_l\cdot\fq^{2n-2j}\cdot\frac{(t;t\fq^{-2})_j}{(t\fq^{-4};t\fq^{-2})_j},
\ee
where we have used the $\fq$-degree of the generators,
\begin{align}
\mathrm{deg}_{\fq} x_i=& \quad 2,\\
\mathrm{deg}_{\fq} a_i=&-2i-2,\\
\mathrm{deg}_{\fq} \theta_i=&-2i+2.
\end{align}
If we shift the overall $\fq$-degree of $H^\bullet$ by $-2n$ units to remove the $\fq^{2n}$ factor in \eqref{EquiEuler2},
what remains is in perfect agreement with the expectation value of Wilson loops in 3d theory $T[M_3]$:
\be
\langle W_{2l}\rangle= (qt)^j\cdot \frac{(1/t;q)_j}{(tq^2;q)_j}=\fq^{-2j}\cdot\frac{(t,t\fq^{-2})_j}{(t\fq^{-4};t\fq^{-2})_j},
\ee
with a typical relation between $q$ and $\fq$ \cite{Fuji:2012pm}:
\be
\fq^2 \; = \; qt \,.
\ee
So, we have verified the conjecture by Rozansky at the level of equivariant Euler characteristics for this link $L_{2n}$,
\be
\chi_{q,t}(\CH_{\text{BPS}}) \; = \; \chi_{q,t}(H_{\text{Rozansky}})
\ee
presenting some evidence for the isomorphism between $H^\bullet_{\text{Rozansky}} (S^1\times S^2,L_{2n}) \{ -2n \}$
and $\CH_{\lambda} \; : = \; \bigoplus_{i,j,\ell\in\Z}\CH_{\lambda}^{0;i,j;\ell}$ with $\lambda = {\square}^{\otimes 2n}$.

As a side remark, positivity also features in the invariants $\hat{Z}_a(M_3; K_{\CR})$
of three manifolds with knots, in a way similar to the case without knot (\ref{block-pos}).
For example, in our case of $M_3 = S^2 \times S^1$,
\begin{multline}
	-\hat{Z}_0(q,-t;W_{6})=
	\left(2 t^3+2 t^2\right) q^3+\left(2 t^4+4 t^3+4 t^2+2 t\right) q^4+\\
	\left(2 t^5+6 t^4+10 t^3+10 t^2+4 t\right) q^5+
	\left(2 t^6+8 t^5+16
	   t^4+22 t^3+18 t^2+8 t+2\right) q^6+
	   \\
	   \left(2 t^7+8 t^6+20 t^5+36 t^4+44 t^3+34 t^2+14 t+2\right) q^7+O\left(q^8\right)
\end{multline}
has only positive coefficients.


\subsection{Links in $L(p,1)$}

For $M_3=L(p,1)$, or more generally $M_3=O(-p)\rightarrow \Sigma_g$, we have $\Lambda_{M_3}= \Z_p/\Z_2$
and the basic Wilson loops in $T[M_3]$ are given by $W_{\lambda}$ with $\lambda=0,\ldots, p$.\footnote{Notice that we have added odd representations according to description in footnote~\ref{ft:Global}.}
These correspond to the ``$\lambda$-cablings'' of the unknot \eqref{Gamma-Lp1} wrapping the Hopf fiber of $L(p,1)$.

More generally, for plumbed $M_3$ (see section \ref{sec:plumbed}), if $(K^{\lambda}, \CR_{\lambda})$
is a $\lambda$-cabling of the unknot wrapping the ``Hopf fiber'' associated with the node $v$ of the plumbing graph,
we have $\Gamma_{K,\la}{=}W_{\lambda_v}$, where $\lambda_v$ is the representation of $\CG$ obtained from
the representation $\la$ of $G$ via the ``evaluation homomorphism'' $e_v: \CG\rightarrow G$ for the node $v$.


\subsubsection{Unrefined index of ${T[L(p,1)]}$ with Wilson loops}
\label{sec:LensWilson}

The unrefined superconformal index --- with contribution of the Cartan component of the adjoint chiral removed, as in \eqref{I-UN-unref} --- with the Wilson line inserted at the north pole reads:
\begin{equation}\label{SU2Int}
\begin{aligned}
\langle W_\la \rangle\equiv 	\CI(q;W_\lambda) & =  \frac{1}{2} \sum_{m \in \mathbb{Z}} \int \frac{dz}{2\pi i z} z^{ p m}\cdot \chi_\lambda(q^{m/2}z)\\
&\ \ \ \times \left( q^{2 \left| m \right|}+q^{-2 \left| m \right|}+4 - 2 \left(q^{ \left| m \right|}+q^{- \left| m \right|} \right) \left( z^2 +\frac{1}{z^2} \right)+\left( z^4+\frac{1}{z^4} \right) \right).
\end{aligned}
\end{equation}
Assuming $\lambda$ is irreducible, we identify it with its highest weight in $\Lambda_{\text{wt},\frak{su}(2)}/\Z_2 \cong \Z_{\geq 0}$.
Our convention is such that
\be
\chi_{\lambda}(z)=\frac{z^{\lambda+1}-z^{-\lambda-1}}{z-z^{-1}}.
\ee
So, the insertion of an operator $W_\lambda$ with odd value of $\lambda$ automatically gives zero,
because of the non-trivial action of the center $\Z_2 \subset SU(2)$.

In the table below we present explicit results for $p=5$ up to $\lambda=38$:
\vspace{0.2cm}
\\
\vspace{0.2cm}
\begin{tabular}{|c|c||c|c||c|c||c|c||c|c|}\hline
$\lambda$ & $\langle W_\lambda\rangle$ & $\lambda$ & $\langle W_\lambda\rangle$ &$\lambda$ & $\langle W_\lambda\rangle$&$\lambda$ & $\langle W_\lambda\rangle$  &$\lambda$ & $\langle W_\lambda\rangle$\\ \hline
0 & 3 & 2 & $-1$ &4 & 0 & 6 &$q^{-3}$ & 8 & $-q^{-3}-2q^{-5}$ \\ \hline
10 & $2q^{-5}+q^{-7}$ & 12 &$-q^{-7} $ &14& 0 &16& $q^{-16}$ &18& $-q^{-16}-2q^{-20}$ \\ \hline
20 & $2q^{-20}+q^{-24}$ & 22 & $-q^{-24}$ &24& 0 &26& $q^{-39}$ &28& $-q^{-39}-2q^{-45}$ \\ \hline
30 & $2q^{-45}+q^{-51}$ & 32 & $-q^{-51}$ &34& 0 &36& $q^{-72}$ &38& $-q^{-72}-2q^{-80}$ \\ \hline
\end{tabular}\ .
\\
This table is almost periodic. This can be understood from the action of Wilson lines on the homological blocks.
For the $D^2\times S^1$ partition function of $T[M_3]$ with $W_\lambda$ inserted at the center of the disk, $O \in D^2$, we have:
\begin{equation}
	\hat{Z}_a(q;W_\lambda) \; = \; \frac{1}{|\CW_a|}\int\frac{dz}{2\pi i z}
	(1-z^{\pm 2})\,\chi_{\lambda}(z)\,\sum_{n\in p\Z+a}q^{n^2/p}\,z^{2n}.
	\label{block-Lp1-knot}
\end{equation}
Wilson loops act in a very simple way on the homological blocks $\hat{Z}_a(q)$. For $L(p,1)$, we have
\be
\hat{Z}_0=1,\quad \hat{Z}_1=-q^{1/p},
\ee
with the rest of the blocks being zero. Let us also formally extend $\hat{Z}_a$ for $a$ outside the range $\{0,1,\ldots,\lfloor\frac{p}{2}\rfloor\}$ by $\hat{Z}_a=0$ and define a ``shift operator''
\begin{equation}
 [j]\hat{Z}_a(q) \; := \; q^{j(2a-j)/p}\hat{Z}_{a-j}(q),\qquad a,j\in \Z.
\end{equation}
Then,
\be
\hat{Z}_a(q;W_{\lambda}) \; =  \sum_{b \, \equiv \, \pm a \pmod p}[\lambda/2] \, \hat{Z}_b(q) ,\qquad a\in \Z_p/\Z_2.
\ee
This equation is not cyclic, and we took $a$ to live in $\Z_{\ge 0}$. Then, one can verify that
\be
\langle W_\lambda \rangle \; = \sum_{a\in \Z_p/\Z_2}|\CW_a|\hat{Z}_a(q;W_\lambda)\hat{Z}_a(q^{-1}).
\ee

One can also deduce the action of $W_\lambda$ on $Z_a=\sum_{b}S_{ab}\hat{Z}_b$ by applying the $S$-transform,
but it won't be very illuminating because $Z_a(q;W_\lambda)$ will be a linear combination of all $Z_a(q)$'s. This difference between $\hat{Z}_a$ and $Z_a$ again demonstrates the advantage of working with the homological blocks $\hat{Z}_a$, rather than $Z_a(q)$.


\subsubsection{Refinement and categorification}

The refined version of (\ref{block-Lp1-knot}) reads
\begin{equation}
	(qt;q)_\infty\hat{Z}_a(q,t;W_\lambda)=
	\frac{1}{|\CW_b|}\left.\int\frac{dz}{2\pi i z}\,
	\frac{(z^2;q)_\infty(z^{-2};q)_\infty}{(z^2tq;q)_\infty(z^{-2}tq;q)_\infty}\,\chi_{\lambda}(z)\sum_{n\in p\Z+b}q^{n^2/p}\,z^{2n}\right. .
	\label{Z-hat-ref-knot}
\end{equation}
One can show that it has the positivity property (\ref{block-pos}) and, therefore, can be interpreted
as the Poincar\'e polynomial of the homological invariant that categorifies $SU(2)$ WRT invariants of
$M_3 = L(p,1)$ with knots wrapping the Hopf fiber.

For example, consider $M_3 = L(5,1)$. With our choice of $G = SU(2)$, it has three abelian flat connections and,
correspondingly, three homological blocks, all tabulated in \cite[sec.6]{Gukov:2016gkn}.
Now, we can see that incorporating knots does not spoil the positivity of \eqref{Z-hat-ref-knot}
and its interpretation as the Poincar\'e polynomial. Yet, the presence of the knot changes all homological blocks
in a non-trivial way, mixing homological invariants of the knot $K$ and the ambient 3-manifold $M_3$ in one combined entity,
{\it e.g.} for $M_3 = L(5,1)$ and $\lambda=2$:
\begin{multline}
	-(-qt;q)_\infty\hat{Z}_0(q,-t;W_2)=
	(t+1) q+\left(t^2+2 t+1\right) q^2+\left(t^3+3 t^2+4 t+2\right) q^3+\\ \left(t^4+4 t^3+8 t^2+8 t+3\right) q^4+\left(t^5+4 t^4+10 t^3+16
	   t^2+14 t+5\right) q^5+
	   \\ \left(t^6+4 t^5+11 t^4+23 t^3+31 t^2+23 t+7\right) q^6+\\
	   \left(t^7+4 t^6+12 t^5+28 t^4+47 t^3+54 t^2+37 t+11\right)
	   q^7+O\left(q^8\right),
\end{multline}
\begin{multline}
	(-qt;q)_\infty\hat{Z}_1(q,-t;W_2)=
	\sqrt[5]{q}+(t+1) q^{6/5}+\left(2 t^2+4 t+2\right) q^{11/5}+\left(2 t^3+6 t^2+8 t+4\right) q^{16/5}+\\
	\left(2 t^4+7 t^3+14 t^2+15 t+6\right)
	   q^{21/5}+\left(2 t^5+8 t^4+19 t^3+29 t^2+25 t+9\right) q^{26/5}+\\
	   \left(2 t^6+8 t^5+22 t^4+43 t^3+55 t^2+41 t+13\right)
	   q^{31/5}+O\left(q^{36/5}\right),
\end{multline}
and
\begin{multline}
	-(-qt;q)_\infty\hat{Z}_2(q,-t;W_2)=
	q^{4/5}+(t+1) q^{9/5}+\left(t^2+2 t+1\right) q^{14/5}+\left(2 t^3+4 t^2+4 t+2\right) q^{19/5}+\\
	\left(2 t^4+5 t^3+8 t^2+8 t+3\right)
	   q^{24/5}+\left(2 t^5+5 t^4+11 t^3+17 t^2+13 t+4\right) q^{29/5}+\\
	   \left(2 t^6+6 t^5+14 t^4+25 t^3+29 t^2+21 t+7\right)
	   q^{34/5}+O\left(q^{36/5}\right).
\end{multline}

Note that, when $p=1$, we have $L(p,1)\cong S^3$ and the unknot wrapping the Hopf fiber becomes
the familiar unknot in $S^3$, yet with a nontrivial framing equal to 1.
Since $H_1(S^3,\Z)=0$, as in section \ref{sec:Roz}, we expect factorization in this case:
\be
W_\lambda=W_0\otimes \CH_{\lambda}^{0;i,j;\ell},
\ee
\begin{equation}
\CH_a[S^3;K^{\lambda},\CR_\lambda]=\bigoplus_{i,j,\ell\in\Z}\CH_{\lambda}^{0;i,j;\ell}\otimes {\CH}_a[S^3]
\end{equation}
Moreover, as in section \ref{sec:Roz}, we expect that $(K^{\lambda},\CR_\lambda)$ is the cabling of the unknot determined by $\lambda$.
In appendix~\ref{app:cabling}, we present evidence for this by comparing it with the ordinary Khovanov homology
of the cabling of the unknot, {\it cf.} \cite{khovanov2005categorifications}.


\subsection{Comparison with refined CS}
\label{sec:refCS-knots}

In this section, we wish to compare the categorification of WRT invariants of knots in 3-manifolds considered
in the previous section with analogous calculations using the tools of refined CS theory and DAHA \cite{Aganagic:2011sg,Cherednik:2011nr}.
To the best of our knowledge, such calculations (that involve both knots and 3-manifolds) were not done in the literature
on refined Chern-Simons theory.

Let us consider the unknot $K$ wrapping the Hopf fiber in $M_3 = L(p,1)$ and colored by an irreducible representation $\CR = \lambda$.
Note, that now the representation $\lambda$ (whose weight we denote by the same letter) does represent the ``color'' of $K \subset M_3$.
The partition function of the refined CS theory with such insertion
can be expressed through $S$ and $T$ matrices (listed in section \ref{sec:refCS}) as follows:
\begin{multline}
	Z_{SU(2)}^\text{ref.~CS}[L(p,1);K,\lambda]=\sum_{n=1}^{k-1} g^{-1}_n\,S_{1n}S_{n,\lambda+1}(T_{nn})^{-p}=\\
	=
	\sum_{n=1}^{k-1}q^{-\frac{pn^2}{4}-\frac{pn\beta}{2}-\frac{p\beta^2}{4}}
	\prod_{j=0}^\beta (q^{-\frac{n+j+\beta}{2}}-q^{\frac{n+j+\beta}{2}})
	(q^{-\frac{n-j+\beta}{2}}-q^{\frac{n-j+\beta}{2}})\,M_{\lambda}(q^{\beta+n}).
\end{multline}
where $M_\lambda(x)$ is the $SU(2)$ Macdonald polynomial, whose coefficients are rational functions of $q$ and $t=q^\beta$.
By repeating the manipulations of section~\ref{sec:refCS}, we obtain (up to the same simple overall factor):
\begin{equation}
	Z_{SU(2)}^\text{ref. CS}[L(p,1);K,\lambda]
	=\sum_{a,b\in \Z_p /\Z_2} e^{2\pi i (k+2\beta)\text{CS}(a)}\cdot
	S_{ab}\cdot \frac{1}{|\CW_b|}\,\hat{Z}^\text{(ref.CS;$\beta$)}_b(q;K,\lambda)
\end{equation}
with
\begin{multline}
	\hat{Z}^\text{(ref.CS;$\beta$)}_a(q;K,\lambda)=\int\frac{dz}{2\pi iz}\,(z^{\pm2};q)_{\beta+1}\,M_\lambda(z^2)\,\sum_{n\in p\Z+a}q^{n^2/p}\,z^{2n}=\\
	=\left.\int\frac{dz}{2\pi iz}\,\left(\frac{(z^{\pm2};q)_\infty}{(z^{\pm2}qt;q)_\infty}\right)
	M_\lambda(z^2)
	\sum_{n\in p\Z+a}q^{n^2/p}\,z^{2n}\right|_{t=q^\beta}
	\label{Z-ref-loop}
\end{multline}
For $\lambda=1$, the Macdonald polynomial coincides with the Schur polynomial, $M_1(z^2)=\chi_1(z)$,
and the expression above agrees with the $D^2\times S^1$ partition function with a Wilson line insertion (\ref{Z-hat-ref-knot}).
However, in order to find an agreement for more general $\lambda$,
we need to make a replacement $\chi_\lambda(z)\rightarrow M_\lambda(z^2)$ in (\ref{Z-hat-ref-knot}).
At the catogorified level, this means that (\ref{Gamma-Lp1}) needs to be replaced by
\begin{equation}
W_{\lambda} \quad \leadsto \quad \bigoplus_{\mu\leq \lambda} W_\mu\otimes \CH_\lambda^\mu
\end{equation}
where $\CH_\lambda^\mu$ are appropriate categorifications of the coefificients $C^\mu_\lambda(q,t)$ in the decomposition $M_\lambda(z^2)=\sum_{\mu\leq \lambda}C^\mu_\lambda(q,t)\chi_\mu(z)$.
This suggests that the insertion of the Macdonald polynomial in the partition function of 3d $\CN=2$ theory $T[M_3]$
corresponds to a $\lambda$-colored unknot wrapping the Hopf fiber of $M_3$, {\it cf.} \eqref{Gamma-Lp1}:
\be
\boxed{\phantom{\int}
M_\lambda(z^2) \quad \leftrightarrow \quad \text{$K$ = unknot along the Hopf fiber colored by $\CR = \lambda$}
\phantom{\int}}
\ee
It would be interesting to test this against many examples of $\lambda$-colored $sl(N)$ homology for various knots
and links \cite{Gukov:2011ry,Cherednik:2011nr,Fuji:2012pm,Itoyama:2012fq,Gukov:2015gmm,Wedrich:2016smm,Kononov:2016cwp}.

Note, that the coefficients in fusion rules of Macdonald polynomials are non-trivial rational functions of $q,t$.
Therefore, the dependence on $\lambda$ in (\ref{Z-ref-loop}) does not agrees with the cabling formula,
unlike the case of Wilson line insertions.
On the other hand, the dependence on framing in the refined CS is simple and is given
by the corresponding power of the matrix element $T_{\lambda+1,\lambda+1}$.
In particular, when $p=1$ the result of (\ref{Z-ref-loop}) is
\begin{equation}
	\frac{\hat{Z}^\text{(ref.CS;$\beta$)}_0(q;K,\lambda)}{\hat{Z}^\text{(ref.CS;$\beta$)}_0(q)}=T_{\lambda+1,\lambda+1}M_\lambda(qt).
\end{equation}
Note that, for $\lambda>1$, it is a nontrivial rational function of $q$ and $t$,
which means that the underlying doubly graded vector space is infinite dimensional,
unlike the finite dimensional vector spaces produced by Wilson line insertions (see Appendix~\ref{app:cabling}).



\acknowledgments{We would like to thank J.~E.~Andersen, M.~Aganagic, F.~Benini, C.~Cordova, A.~Gadde, E.~Gorsky,
K.~Hori, H.~Kim, S.~Nawata, M.~Romo, S.~Shakirov, L.~Rozansky and K.~Ye for useful comments and discussions.
The work of S.G. and D.P. is supported in part by the U.S. Department of Energy, Office of Science, Office of
High Energy Physics, under Award Number DE-SC0011632.
In addition, the work of D.P. is supported by the center of excellence grant ``Center for Quantum Geometry of Moduli Space" from the Danish National Research Foundation (DNRF95).
P.P. gratefully acknowledges the support from Marvin L. Goldberger Fellowship and the DOE Grant DE-SC0009988.
The research of C.V. is supported in part by NSF grant PHY-1067976.
This work was performed in part (by P.P.) at Aspen Center for Physics which is supported by National Science Foundation grant PHY-1066293.
The authors would like to thank Simons Center for Geometry and Physics and the organisers of the Simons Summer Workshop 2016, where the work on the project has begun, for generous hospitality.
