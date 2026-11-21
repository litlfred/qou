---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-010-31-a-steepest-descent-algorithm
section_title: "A steepest descent algorithm"
section_number: 3.1
pages: 17-19
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
toc_source: outline
text_source: latex
latex_prose_ratio: 0.697
latex_coverage_ratio: 0.964
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜no [9] that perturbative series associated with the hyperbolic knots 41 and 52 are resurgent and"
---
\label{sec:alg}
Fix a critical point $p_0\in\Sigma$ with a lift of the critical value $V_0\in\BC$ and $\vartheta\in\arg(\BC\backslash\calS(V_{0}))\cap(\tfrac{\pi}{2},\tfrac{3\pi}{2})$. This determines the steepest descent contour~$\calC_{p_0,\vartheta}$ and constants $\epsilon,M>0$ so that all points $p\notin W_{\epsilon,M}$ satisfy $[\gamma_{p,\theta}]=0$ (see Corollary~\ref{cor:half.thimb.stateint.zero}). Let $W=W_{\epsilon,M}$ and consider the set
\be
\calZ\;:=\;\{p\in W\;|\;\Re(e^{-i\vartheta}(V_0-V(p)))\in\cos(2\pi\vartheta)\BZ\}\,.
\ee
We can identify $\calZ$ with $\big[e^{-i\vartheta}(V-V_0)\big]^{-1}(i\BR/e^{-i\vartheta}\BZ)\cap W$, thus $\calZ$ has a natural orientation induced by $\BR$. We define 
\be
\begin{aligned}
\calZ_+&\;:=\;\big[e^{-i\vartheta}(V_0-V)\big]^{-1}(i\BR_{\geq 0}/e^{-i\vartheta}\BZ)\cap W\subset\calZ\,,\\
\calP&\;:=\;\{p\in W\cap\calZ_+ \;\vert\; \Re(z(p)e^{-i\vartheta})\in\cos(2\pi\vartheta)\BZ\}\,.
\end{aligned}
\ee
Notice that $\calP$ is a finite set. To each point $p\in\calP\setminus\{p_0\}$ we can associate the cycle $\gamma_{p,\theta}$, which represents a class in $H_1(\Sigma,D_{\infty,\theta})$ as in Corollary~\ref{cor:half.thimb.stateint}. The points $p\in\calP$ partition the set $\calZ_+$ into a set of edges and we define $\calE$ to be the set of edges whose end points lie in $\calP$, i.e. 
\be
\calE\;:=\;\big\{e\in\pi_0(\calZ_+\setminus\calP)\colon \partial e\subseteq\calP\big\}\,.
\ee
We denote the boundary of $e$ by $(p_e, r_e)$, where the order respects the orientation of $\calZ_+$. To each $e\in\calE$ we associate a cycle $\gamma_{e,\theta}$, which represents a class in $H_1(\Sigma,D_{\infty,\theta})$ as shown in Corollary~\ref{cor:half.thimb.stateint}. 
In order to describe the algorithm we need the following lemma:
\begin{lemma}\label{lem:}
Let $p=(z,m)\in\Sigma$ and $e^{i\vartheta}\in\BC\setminus\calS(V_0)$. The sequence of tangent directions to $\Gamma_{(z,m+k),\vartheta}$ at the point $(z,m+k)$ is strictly monotone for $k\in\mathrm{sign}(\Im(z))\BZ_{\geq 0}$.
\end{lemma}
\begin{proof}
From Equation~\eqref{eq:tangent-GGamma_p} in the proof of Lemma~\ref{lem:thimble} and Equation~\eqref{eq:tangent}, the tangent to $\Gamma_{(z,m+k),\vartheta}$ at the point $(z,m+k)$ is $e^{i\vartheta}(iV'(z,m)+ik)^{-1}$. 
\end{proof}
To the data $(p_0,V_0,\vartheta)$ we can define a finite combination of state integrals. To begin the algorithm, in place of step $(\rm I)$, we consider the critical point $p_0$ and the lift $V_0\in\BC$ such that $V_0=V(p_0)\in\BC/\BZ$, and the thimble $\calC_{p_0,\vartheta}$ as in Corollary~\ref{cor:thimble}. Then we go on from step $(\rm II)$. Here is the algorithm:
\begin{itemize}
  \item[$(\rm I)$] Let $p\in\calP$ with a lift of $V(p)$ to $\BC$ and its associated cycle $\gamma_{p,\vartheta}$ (see Definition~\ref{def:gamma_p}).
  \item[$(\rm II)$] The cycle $\gamma_{p,\theta}$ can be decomposed as union of $\gamma_{e,\theta}$ for every $e\subset\gamma_{p,\theta}$ and $\gamma_{r,\theta}$ where $r\in\calP\cap\gamma_{p,\theta}$ is the last point with respect to the order inherited from $\gamma_{p,\theta}$. 
  \item[$(\rm III)$] To each $\gamma_{e,\theta}$ we associate the integral
  \be\label{eq:ge.si}
  \int_{\gamma_{e,\theta}} \e\big(\tfrac{A}{2}z(z+1+\tfrac{1}{\tau})\tau+mz\tau+n\tau\big)\Phi((z-\ell)\tau;\tau)^B\, dz\,,
  \ee 
  where $m$ and $n$ are dictated by the original lift of $V(p)$ and $\ell=\lceil \Re(z(x))+\tan(\vartheta)\Im(z(x))\rceil$ for some $x\in e$, the ceiling of the projection onto the reals parallel to~$e^{-i\vartheta}$. If $\Im(z(p_e))\Im(z(r_e))<0$ then $\gamma_{e,\theta}$ is homotopic to a state integral contour, hence the integral in Equation~\eqref{eq:ge.si} is equal to $q^n\calI_{m,\ell}$. Otherwise, it vanishes. 
  \item[$(\rm IV)$] To each point $(z,m)\in\partial\big(\calE\cap\gamma_{p,\theta}\big)$, we take the collection of points $(z,m\pm k)\in\calP$ where $k=1,\ldots, N$ and $N\leq |\calP|$, and the sign $\pm$ equals the sign of $\Im(z)$.  To these collections we assign the lifts $V((z,m\pm k))=V(z,m)\pm k(z-\ell)$ and take their associated cycles $-\gamma_{(z,m\pm k),\theta}$ weighted by constants $a_{k}\in\BZ$ defined as follows: from Lemma~\ref{lem:} there exists a constant $k_0$ such that 
\begin{itemize}
  \item[$\bullet$]  for $0<k<k_0$,  the tangent\footnote{If the tangent is equal to $\pm i e^{i\vartheta}$, then we consider the direction of higher derivatives.} at $(z,m\pm k)$ to the set $-\gamma_{(z,m\pm k),\theta}$ is in $-i e^{i\vartheta}\mathbb{H}$ if $\Im(z)>0$, and is in $i(A-B) e^{i\vartheta}\mathbb{H}$ if $\Im(z)<0$,
  \item[$\bullet$] for $k\geq k_0$, the tangent at $(z,m\pm k)$ to the set $-\gamma_{(z,m\pm k),\theta}$ is in $i e^{i\vartheta}\mathbb{H}$ if $\Im(z)>0$, and is in $-i(A-B) e^{i\vartheta}\mathbb{H}$ if $\Im(z)<0$,
\end{itemize}
and $a_k$ are the unique constants that satisfy the equation
\be\label{eq:alg-tails}
\begin{aligned}
& \big[\Phi((w-\ell)\tau;\tau)^B-\Phi((w-\ell-1)\tau;\tau)^B\big] \e\Big(\frac{A}{2}w(w+1+\tfrac{1}{\tau})\tau+mw\tau\Big)\\
&\=\sum_{0<k<k_0}a_k \Phi((w-\ell_0)\tau;\tau)^B\e\Big(\frac{A}{2}w(w+1+\tfrac{1}{\tau})\tau+(m\pm k)w\tau\Big)\\
&\quad + \sum_{k\geq k_0}a_k  \Phi((w-\ell_1)\tau;\tau)^B\e\Big(\frac{A}{2}w(w+1+\tfrac{1}{\tau})\tau+(m\pm k)w\tau\Big)\,,
\end{aligned}
\ee
for every $w$ with $\Im(w)=\Im(z)$, and where $\ell_0=\ell+1$ and $\ell_1=\ell$ if $\Im(z)>0$, and $\ell_0=\ell+(1-\mathrm{sign}(A-B))/2$ and $\ell_1=\ell+(1+\mathrm{sign}(A-B))/2$ if $\Im(z)<0$.
\end{itemize}
The algorithm terminates if at step $(\rm IV)$ there are no $(z,m\pm k)\in\calP$.
\begin{corollary}\label{cor:end-algorithm}
This algorithm terminates after finitely many steps producing a function $\calI_{p_0,V_0,\vartheta}(\tau)$ given as a $\BZ$-linear combination of $q^n\calI_{m,\ell}$.
\end{corollary}
\begin{proof}
We can partially order the points $p$ in the set $\calP\cap\BH$ according to the $\Re(z_{+}(p))$ and $m\in \{0,\ldots ,A-1\}$, in particular we use the lexicographic order on $\BR\times\{0,\ldots ,A-1\}$. The new base points appearing at step $(\mathrm{IV})$ of the algorithm always strictly increase with respect to this order. Hence after a finite number of steps all points will move outside $\calP$ (a finite set). A similar argument holds in the lower half-plane. Then from Corollary~\ref{cor:half.thimb.stateint.zero}, all of these points $p$ have trivial associated cycles $[\gamma_{p,\vartheta}]=0$. 
\end{proof}
\begin{lemma}
The function $\calI_{p_0,V_0,\vartheta}(\tau)$ is locally constant as $\vartheta$ varies in $\arg(\BC\backslash\calS(V_{0}))\cap(\tfrac{\pi}{2},\tfrac{3\pi}{2})$.
\end{lemma}
\begin{proof}
For $\vartheta\in\arg(\BC\backslash\calS(V_{0}))\cap(\tfrac{\pi}{2},\tfrac{3\pi}{2})$ contained in a connected component, the sets $\calZ_{+}$ are all homotopic. We can restrict to a compact subinterval and on this compact set of $\vartheta$, we can choose $\epsilon,M>0$ uniformly. Then for small enough variations of $\vartheta$, we can identify $p\in\calP$ while $\vartheta$ varies. Since $p$ can not cross the reals without going through a branch point, which $\calZ_+$ does not intersect, the cycles $\gamma_{p,\vartheta}$ are all homotopic. This implies that the algorithm will generically produce the same $\calI_{p_0,V_0,\vartheta}(\tau)$ for small variations of $\vartheta$. Besides the generic behaviour, there are critical directions across which the set $\calP$ can gain or loose points. Points in $\calP$ either appear and disappear in pairs in the interior of $W$---therefore they will both have the same sign of $\Im(z_\pm)$---or a single point falls outside the boundary of $W$.
If two points appear or disappear inside $W$, given that both points are in the same half plane, the cycle associated to them is trivial and this does not affect the function $\calI_{p_0,V_0,\vartheta}(\tau)$. In the other case, if a point $p\in\calP$ falls outside the boundary of $W$ then $[\gamma_{p,\vartheta}]=0$ by Corollary~\ref{cor:half.thimb.stateint.zero} and therefore, as $[\gamma_{p,\vartheta}]$ is constant for all $\vartheta$ in our compact set, it does not affect $\calI_{p_0,V_0,\vartheta}(\tau)$. 
\end{proof}
If $\rm I$ denotes a connected component of $\BC\backslash\calS(V_{0}))\cap(\tfrac{\pi}{2},\tfrac{3\pi}{2})$, then we denote $\calI_{p_0,V_0,I}(\tau)$ the function $\calI_{p_0,V_0,\vartheta}(\tau)$ for any $\vartheta\in\arg{I}$. 

\subsection{Proof of Theorem~\ref{thm:main_intro}}\label{sec:proof_main}
We now have all the ingredients we need to prove our main theorem. The main idea is to compute the asymptotics of the function $\calI_{p_0,V_0,\vartheta}(\tau)$ for $\arg(-1/\tau)=\theta\in(-\tfrac{\pi}{2}+\vartheta,\tfrac{\pi}{2}+\vartheta)$. We will state this in the following theorem, which is essentially equivalent to Theorem~\ref{thm:main_intro}.
\begin{theorem}
If $[a,b]\subseteq\arg(\BC\backslash\calS(V_{0}))\cap(\tfrac{\pi}{2},\tfrac{3\pi}{2})$, $\vartheta\in[a,b]$, $\arg(-1/\tau)=\theta\in(a-\tfrac{\pi}{2},b-\tfrac{\pi}{2})$ and $|\tau|\to\infty$, then there exists constants $C=C(a,b),\varepsilon=\varepsilon(a,b)>0$
\be
  |\e(-V_0\tau)
  \calI_{p_0,V_0,\vartheta}(\tau)
  -
  \Phi_{\Xi}^{(K)}(-2\pi i/\tau)|
  <
  C\,\varepsilon^{-K}\,K!\,|\tau|^{-K}\,,
\ee
where $\Phi_{\Xi}^{(K)}(\hbar)$ is the truncation of the series $\Phi_{\Xi}(\hbar)$ to $\mathrm{O}(\hbar^{K})$.
\end{theorem}
\begin{proof}
Firstly, as we vary $\arg(-1/\tau)=\theta\in(\vartheta-\tfrac{\pi}{2},\vartheta+\tfrac{\pi}{2})$, we can deform the contours of the state integrals of $\calI_{p_0,V_0,\vartheta}(\tau)$ so that they are contained in $\calZ_{+}$ besides tails based at the set $\{p\in X\cap\calZ_+ \colon \Im(z(p)e^{-i\theta})\in\sin(2\pi\theta)\BZ\}$. Considering this deformation we can now compute the asymptotics.

\medskip

The first iteration of the algorithm gives a collection of state integrals (from step III) whose asymptotics is determined by the saddle point approximation at $p_0$ with the addition of the asymptotics of the tails (from in step II). The tail at $(z,m)$ is 
\be\label{eq:tail}
\int_{z}^{\pm e^{i\theta}\infty} \big[\Phi((w-\ell)\tau;\tau)^B-\Phi((w-\ell-1)\tau;\tau)^B\big] \e\Big(\frac{A}{2}w(w+1+\tfrac{1}{\tau})\tau+mw\tau\Big)\,dw\,.
\ee
Step IV produces a new collection of cycles $\gamma_{(z,m\pm k)}$ (described in Equation~\eqref{eq:alg-tails}) whose asymptotics is equal to the asymptotics of the remaining tails. Therefore, at any iteration of the algorithm, the asymptotics are determined by the asymptotics of a finite collection of tails and the saddle point approximation at $p_0$.

\medskip

By construction, after a finite number of steps, the starting points of these tails will be outside $W$ (see Corollary~\ref{cor:end-algorithm}). Notice that the volumes of the tails' base points are always decreasing, and therefore eventually they leave the finite set $\calP$. If a tail starts outside $W$ its asymptotics are exponentially smaller than the asymptotics coming from the saddle point approximation at $p_0$. This can be seen from the proof of Corollary~\ref{cor:half.thimb.stateint.zero}.

\medskip

Therefore, the tails in $\calI_{p_0,V_0,\vartheta}(\tau)$ only make exponentially small contributions and the asymptotics are determined by the integral along the set $\calZ_+$. For $(\vartheta-\tfrac{\pi}{2},\vartheta+\tfrac{\pi}{2})$, the set $\calZ_+$ is contained in the region where $\Im(V(p)\tau)>0$ for the local lift of $V(p)\in\BC$. We therefore see that $\calI_{p_0,V_0,\vartheta}(\tau)$ has asymptotics determined by the stationary phase approximation at $p_0$ (see for example~\cite[Chap.~9, Sec.~2.2, Theorem~2.1]{Olver}). This was exactly how $\Phi_{\Xi}$ was defined in Equation~\eqref{eq:def.phi} and therefore this completes the proof.
\end{proof}
\begin{proof}[Proof of Theorem~\ref{thm:main_intro}]
To transfer this result to a proof of the main theorem, we simply follow the same proof as in Corollary~\ref{cor:fad.resum}. Given these asymptotics we can apply Nevanlinna's theorem~\cite{nevanlinna} or simply just take Mordell's inverse Laplace transform to define the analytic continuation of the Borel transform in the cone $\theta\in(a,b)$. This proves the Borel summability. We can run exactly the same construction and proof for $\Re(\tau)<0$ using the functions given in Remark~\ref{rem:neg.rt} to give the full result including $\Re(\tau)<0$.
\end{proof}
\begin{proof}[Proof of Theorem~\ref{thm:4152}]
The result follows immediately by specialising Theorem~\ref{thm:main_intro} to the cases of $(A,B)$ equal to $(1,2)$ for $4_1$ and $(2,3)$ for $5_2$. 
\end{proof}
