---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-007-gradient-flows-on-riemannian-manifolds
section_title: "Gradient flows on Riemannian manifolds"
section_number: null
pages: 12-16
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.996
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
\label{sec:grad_flows}
Let $(\ML,g)$ be a Riemannian manifold without boundary 
of class $C^2$ over a Hilbert 
space $\HL$ with  Riemannian metric $g$ given fibrewise as 
$g_x(\cdot,\cdot)$ 
inducing a norm $\|\cdot\|_{g_x} \ceq \sqrt{g_x(\cdot,\cdot)}$ on 
the tangent space $T_x\ML$. 
For two points $x,y$ 
in the same connected component of $\ML$ we consider
the  set of connecting $C^1$-paths,
\begin{equation}\label{eq:path-space}
	\PS(x,y) 
	\ceq \braces[\big]{c\in C^1([0,1],\ML) : c(0)=x,c(1)=y},
\end{equation}
and define the \emph{path metric} (or \emph{Palais distance})
\begin{equation}\label{eq:path-metric}
\dist_{\ML}(x,y) \ceq \inf_{c\,\in\PS(x,y)}\int_0^1
\|\dot{c}(t)\|_{g_{c(t)}}\d t,
\end{equation}
where $\dot{c}(t) \ceq \D c_t(1)\in T_{c(t)}\ML$
for the differential $\D c_t:T_t[0,1]\simeq\R\to
T_{c(t)}\ML$ of the $C^1$-map $c:[0,1]\to\ML$ (cf.{} \cite[Sections 6 \& 9]{palais_1963}).
Equipped with the path metric $\dist_{\ML}$, every connected
component
of 
$\ML$ is a metric space. This metric is consistent with the
topology of $\ML$ as shown in \cite[Section 9]{palais_1963}
and in the more general setting of Finsler manifolds in
\cite[Theorem 3.3]{palais_1966}. Therefore, every connected
component $\KL$ of $\ML$ is closed with respect to $\dist_{\ML}$;
see, e.g., \cite[Remark after Theorem 25.2]{munkres_2000}.

On this manifold we consider energy functionals $\EL:\ML\to\R$ 
of class $C^{1,1}_\loc$ whose gradient $\nabla \EL$ is
given by $\D\EL_x(h)=g_x(\nabla\EL(x),h)$ for $x\in\ML$ and $h\in
T_x\ML$. We assume that
\begin{enumerate}
	\Item[\rm (e)]\label{lower-bound} 
	({\sc Energy bounded below})
	There is a number $e\in\R$ such that
	$\EL(x)\ge e$ for all $x\in\ML$.
	\Item[\rm (L**)]\label{condL**} 
	({\sc limit in $\ML$}) 
	Every Cauchy sequence
	$(x_k)_{k \in \N}$ in $\ML$ that is bounded under $\EL$
	converges to some 
	$x_\infty\in\ML$ as $k\to\infty$.
\end{enumerate}
Long-time existence for the gradient flow
and subconvergence to critical points can
now be proved by slightly generalizing a classic argument 
that can be found, e.g., in \cite[Theorem 9.1.6]{palais-terng_1988} 
for Riemannian manifolds, in \cite[Theorem 1.1]{browder_1965} 
for Banach manifolds modelled over a uniformly convex Banach space, or 
in \cite[Theorem 5.4]{palais_1966} for general Finsler manifolds.

\begin{theorem}[Gradient flow]
	\label[theorem]{thm:gradflow_subconvergence}
	Let $\EL\in C^{1,1}_\loc(\ML)$ satisfy the Palais--Smale condition
	{\rm (PS)} and conditions \ref{lower-bound} and \ref{condL**}.
	There exists a function $\phi:[0,\infty)\times\ML\to\ML$, such
	that $\phi(\cdot,x)\in C^1([0,\infty),\ML)$ for every $x\in\ML$,
	and
	\begin{equation}\label{eq:gradient-flow}
	\begin{cases}
	\frac{\d}{\d t}\phi(t,x)& =-\nabla\EL(\phi(t,x)) \Foa t\in [0,\infty),\\
		\phi(0,x)&=x.  
	\end{cases}
	\end{equation}
The function $t\mapsto\EL(\phi(t,x))$ is strictly decreasing 
on $[0,\infty)$ unless
$x$ is
	$\EL$-critical.
For $x\in\ML$ and $t\to\infty$ the solution $\phi(t,x)$ subconverges  
to a critical point of $\EL$, which lies in the same
connected component of $\ML$ as the initial point $x$.
In particular, in each connected component
of $\ML$ the energy $\EL$ possesses at least one
critical point. 
\end{theorem}

\begin{proof}
	For $x\in\ML$ we obtain
	the function $\phi$ as the solution to the 
	initial value problem
	\begin{equation} 
		\begin{aligned}
			\label{eq:cauchy_problem}
		\textstyle
		\frac{\d}{\d t}\xi(t) &=-\nabla \EL(\xi(t)), &\hspace{10pt}\xi(0)&=x.
		\end{aligned}
	\end{equation}
	Such a solution exists and is unique on an 
	interval $(t^-,t^{+})$ containing $t=0$
	by the Picard--Lindelöf Theorem 
	(see, e.g., \cite[Chapter IV.2]{lang_2002}). 
	Here $t^{+}\in (0,\infty]$ 
	denotes the maximal positive existence time, 
	and for $t\in (t^-,t^+)$ we compute by means of 
	\cref{eq:cauchy_problem}
	\begin{align}
	\textstyle
	\frac{\d}{\d t}\EL(\xi(t)) &
=\D\EL_{\xi(t)}(\dot{\xi}(t))= g_{\xi(t)}\big(\nabla \EL(\xi(t)),
	\dot{\xi}(t)\big)\label{eq:decreasing-energy}\\
		&\overset{\cref{eq:cauchy_problem}}{=}  
- g_{\xi(t)}\big(\nabla \EL(\xi(t)),\nabla \EL(\xi(t))\big)
=-\|\nabla\EL(\xi(t))\|^2_{g_{\xi(t)}}\le 0.\notag
	\end{align}
Hence, $\phi(\cdot,x) \ceq \xi(\cdot)$ 
solves 
\cref{eq:gradient-flow} on the positive maximal time interval $[0,t^+)$, 
and the energy is strictly decreasing along the flow unless $\D\EL_x=0$,
or equivalently, $\nabla\EL(x)=0$, in which case $\xi(t)=x$ and therefore
$\EL(\xi(t))=\EL(x)$ for all $t\in
[0,t^+)$ by uniqeness of the solution to \cref{eq:cauchy_problem}.

To show that $t^+=\infty$ we assume to the contrary that $t^+<\infty$,
and show below
that in that case the one-sided limit
$\xi(t^+) \ceq \lim_{t\nearrow t^+}\xi(t)$ exists, so that 
we could find a solution of \cref{eq:cauchy_problem} with $x$ replaced
by $\xi(t^+)$ on an
open
 time interval containing $t^+$, which contradicts the 
maximality of $t^+$ by uniqueness of the solution.

Towards the existence of the limit point
$\xi(t^+)\in\ML$ for some finite maximal time $t^+\in
	(0,\infty)$
consider 
a strictly increasing
sequence $(t_k)_k\subset[0,t^+)$ with $t_k\to t^+$ as $k\to\infty$,
and define 
the sequence of points
$x_k=\xi(t_k)\in\ML$. We first show that $x_k$ is a Cauchy 
sequence in $\ML$, so that by condition
\ref{condL**} we find $x_\infty\in\ML$ such that $x_k\to x_\infty$ as
$k\to\infty$, since we know  that
$\EL(x_k)\le\EL(x)$ for all $k\in\N$ by \cref{eq:decreasing-energy}. Going back
to an arbitrary sequence $s_m\nearrow t^+$ we will then show that also 
$y_m \ceq \xi(s_m)\to x_\infty$ as $m\to\infty$, so that $\xi(t^+)$ indeed exists.

We have by \cref{eq:decreasing-energy} 
\begin{align}
	\EL(\xi(t))-\EL(\xi(s))\overset{\cref{eq:decreasing-energy}}{=}
	\textstyle
	-\int_s^t \norm{ \nabla \EL(\xi(\tau))}^2_{g_{\xi(\tau)}}\d \tau
	\Fo 0\le s< t<t^+,\label{eq:energy-identity}
\end{align}
which yields the following by means of \ref{lower-bound}:
\begin{align*}
\textstyle
\int_{s}^{t} \norm{\nabla \EL(\xi(\tau))}_{g_{\xi(\tau)}}
\d \tau 
&\textstyle
	\le 
	\pars{t-s}^{1/2} 
	\pars[\big]{ \int_s^t
		\norm{\nabla \EL(\xi(\tau))}^2_{g_{\xi(\tau)}}\d \tau 
	}^{1/2}\\
&\overset{\ref{lower-bound}}{\le}(t-s)^{\frac{1}{2}}(\EL(x)-e)^{\frac{1}{2}}
\quad\Foa 0\le s<t<t^+.
	\end{align*}
	Hence, by definition \cref{eq:path-metric} of the path metric,
	and by the differential equation \cref{eq:cauchy_problem},
	\begin{align}
		\dist_\ML(x_j,x_k)&\overset{\cref{eq:path-metric}}{\le}
		\textstyle
		\int_{t_j}^{t_k}\|\dot{\xi}(\tau)\|_{g_{\xi(\tau)}}\d
		\tau \overset{\cref{eq:cauchy_problem}}{=}
		\int_{t_j}^{t_k}\|\nabla \EL(\xi(\tau)) \|_{g_{\xi(\tau)}}
		\d 
		\tau\notag\\
		&\le (t_k-t_j)^{\frac{1}{2}}(\EL(x)-e)
		\longrightarrow 0 \As j,k\to\infty;\label{eq:cauchy-estimate}
	\end{align}
hence $(x_k)_k$ is indeed a Cauchy sequence so that $x_k\to x_\infty$
for some $x_\infty\in\ML$. For any other sequence $s_m\nearrow t^+$ repeat
the argument in \cref{eq:cauchy-estimate} with $y_m \ceq \xi(s_m)$ instead of
$x_j$ to find
\begin{align*}
	\dist_\ML(y_m,x_\infty)
	=
	\lim_{k\to\infty} \dist_\ML(y_m,x_k)
	&\le
	\lim_{k\to\infty} \pars{t_k-s_m}^{1/2} \pars{\EL(x)-e}^{1/2}
	\\
	& = 
	\pars{t^+-s_m}^{1/2} \pars{\EL(x)-e}^{1/2}
	\to 
	0
	\As m\to\infty,
\end{align*}
so that the one-sided limit $\xi(t^+)$ indeed exists.
Therefore, 
	the solution $\phi(\cdot,x)$ exists on $[0,\infty)$.

Combining the energy identity \cref{eq:energy-identity} for 
$t \ceq t_k\nearrow\infty$ and 
$s \ceq 0$ with condition \ref{lower-bound}
we obtain
$$
\textstyle
\int_0^\infty\|\nabla\EL(\xi(\tau))\|^2_{g_{\xi(\tau)}}\d \tau=
\lim_{k\to\infty}\int_0^{t_k}\|\nabla\EL(\xi(\tau))\|^2_{g_{\xi(\tau)}}\d \tau
\le \EL(x)-e.
$$
Therefore, there exists a sequence $s_l\nearrow\infty$ such that
for the points $z_l \ceq \xi(s_l)\in\ML$ one has
$\|\nabla\EL(z_l)\|_{g_{z_l}}\to 0$ 
as $l\to\infty$. Together with 
$\EL(z_l)\le\EL(x)$ for all $l\in\N$ this shows that
$(z_l)_l\subset\ML$ is a (PS)-sequence, which by means of the (PS)-condition
implies
that there is a subsequence $(z_{l_i})_i\subset (z_l)_l$ 
converging to some point
$z_\infty\in\ML$ as $i\to\infty$. Since $\EL$ is of class $C^1$ we find
$$
\|\D\EL_{z_\infty}\|_{(T_{z_\infty}\ML)^*}=\lim_{i\to\infty}
\|\D\EL_{z_{l_i}}\|_{(T_{z_{l_i}}\ML)^*}=\lim_{i\to\infty}
\|\nabla\EL(z_{l_i})\|_{g_{z_{l_i}}}=0,
$$
that is, $z_\infty$ is $\EL$-critical. 
All points $z_{l_i}$ are connected to the initial point $x$ by
the continuous path $\xi|_{[0,s_{l_i}]}$, so they lie in the same
connected component $\KL$ of $\ML$ as $x$. Since $\KL$ is closed,
one also has $z_\infty\in\KL$.
\end{proof}
Palais considers in \cite[Section 2]{palais_1979} a group $G$ of
isometries of a Riemannian manifold and a $G$-invariant energy $\EL:\ML\to
\R$ to provide an exemplary simple setting where his
principle of symmetric criticality holds true. It turns out that in this
situation the gradient flow \cref{eq:cauchy_problem} is symmetry
preserving.
\begin{proposition}[Symmetry-preserving gradient flow]
\label{prop:symmetry-preserving-grad-flow}
Let $G$ be a group of $C^1$-isometries of the Riemannian manifold $(\ML,g)$. 
Suppose
that $\EL\in C^{1,1}_\textnormal{loc}(\ML)$ is invariant under $G$, i.e.,
$\EL=\EL\circ\G$ for all $\G\in G$, and satisfies the assumptions of
\Cref{thm:gradflow_subconvergence}. Then the gradient flow 
\cref{eq:cauchy_problem} preserves the $G$-symmetry, that is,
for every initial point $x\in\ML$ that satisfies $\G x=x$ for all $\G\in G$, the solution
$\xi$ of \cref{eq:cauchy_problem}  satisfies $\G \xi(t)=\xi(t)$ for all
$\G \in G$ and $t\in [0,\infty)$. In addition, $\xi$ subconverges to a 
$G$-symmetric critical point $x_\infty$, i.e., with $\G x_\infty = x_\infty$
for all $\G\in G$.
In particular, in any connected component $\KL$ of $\ML$ that contains
a $G$-symmetric point $x$ there is a $G$-symmetric $\EL$-critical point.
\end{proposition}
\begin{proof}
Palais showed in \cite[Section 2]{palais_1979} that 
$\nabla\EL(\G x)=
\D\G_x(\nabla\EL(x))$ for all $\G\in G$ and $x\in\ML$. 
This implies for any $G$-symmetric
initial point $x\in\ML$ and any fixed group element $\G\in G$ that
the solution $\xi$ of \cref{eq:cauchy_problem}
generates the
function $\varXi(t) \ceq \G\xi(t)$, which satisfies $\varXi(0)=\G\xi(0)=
\G x=x$ and
$$
\dot{\varXi}(t)=\D\G_{\xi(t)}(\dot\xi(t))\overset{\cref{eq:cauchy_problem}}{=}
-\D\G_{\xi(t)}\nabla\EL(\xi(t))=-\nabla\EL\G\xi(t)=-\nabla\EL\varXi(t)
$$
for all $t\in [0,\infty)$. 
In other words, $\varXi$ solves the same initial
value problem as $\xi$ does, so that $\varXi=\xi$ by uniqueness of the solution.
Since $\G\in G$ was chosen arbitrarily, we have shown that \cref{eq:cauchy_problem} is 
symmetry-preserving. If $x_\infty\in\ML$ is an $\EL$-critical limit point of 
$\xi$ then there is a sequence 
$t_i\to\infty$ such that 
$$
\G x_\infty=\G \lim_{i\to\infty}\xi(t_i)=\lim_{i\to\infty}\G\xi(t_i)=
\lim_{i\to\infty}\xi(t_i)=x_\infty,
$$
so $x_\infty $ is $G$-symmetric as well. Finally, to find a $G$-symmetric
$\EL$-critical point in a component $\KL$ of $\ML$ containing a $G$-symmetric
point $x\in\KL$, we simply start the gradient flow \cref{eq:cauchy_problem}
in that point $x$. This flow subconverges to a 
$G$-symmetric $\EL$-critical point
in that same component $\KL$.
\end{proof}
\begin{corollary}[Critical points of lower energy]
{\cite[Corollary 9.1.8]{palais-terng_1988}}
	\label[corollary]{koro:critpoint_lowerenergy}
Let $\EL$ satisfy the assumptions of \Cref{thm:gradflow_subconvergence}.
Then, for any point $x\in\ML$ with $\D\EL_x\not=0$ there
exists a critical point $x_{\text{c}}$ of $\EL$ in the connected component
of $\ML$ that contains $x$, such that $\EL(x_{\text{c}})<\EL(x)$.
If $x$ is $G$-symmetric and $\EL$ is $G$-invariant under a group
$G$ of $C^1$-isometries of $(\ML,g)$ then $x_c$ is $G$-symmetric as well.
\end{corollary}
\begin{proof}
	Choose $x_{\text{c}}\in\ML$ as any limit point of $\phi(t,x)$
	as $t\to\infty$, 
	which is contained in the same connected
	component $\KL\subset\ML$ as the initial point $x$ according
	to \Cref{thm:gradflow_subconvergence}. 
	Since $x$ is not a critical point we have $\EL(x_\text{c})<\EL(x)$
	because of the strict energy decay along the flow. The last
	statement follows from \Cref{prop:symmetry-preserving-grad-flow}.
\end{proof}
\begin{corollary}[Energy minimizers]{\cite[Theorem 9.1.9]{palais-terng_1988}}
	\label[corollary]{koro:minimizer_existence}
	Under the assumptions of \Cref{thm:gradflow_subconvergence}
	 the energy $\EL$ attains its infimum on $\ML$, and additionally on 
 every connected component of $\ML$. Moreover, on $\ML$, and also
 in each of its connected components
 there exists a minimizing {\rm (PS)}-sequence. 
 If a connected component
 $\KL$ of $\ML$ contains a $G$-symmetric point $x$ and $\EL$ is $G$-invariant
 under a group $G$ of $C^1$-isometries 
 of $(\ML,g)$, then there is a $G$-symmetric
 element $x_s\in\KL$ with $\EL(x_s)=\inf\{\EL(y):y\in\KL,\,\textnormal{$y$
 is $G$-symmetric}\}$, and a corresponding {\rm (PS)}-sequence of
 $G$-symmetric elements in $\KL$.
\end{corollary}
\begin{proof}
Let $x_k$ be a minimizing sequence for $\EL$ on $\ML$, i.e.,
$\lim_{k\to\infty}\EL(x_k)=\inf(\EL)$. 
Without loss of generality we can assume, that each $x_k$ is a critical point, since otherwise we just replace $x_k$ 
by a critical point of lower energy by \cref{koro:critpoint_lowerenergy}. Then, since $\EL$ satisfies the (PS)-condition, 
there exists a subsequence $(x_{k_i})_i\subset (x_k)_k$ 
converging to a critical point 
$x_{\text{c}}$ as $i\to\infty$, and by continuity of $\EL$ one has
$
\EL(x_{\text{c}})=\lim_{i\to\infty}\EL(x_{k_i})=\inf(\EL).
$
We can repeat the same argument on each connected component of $\ML$ instead
of $\ML$, since each such component is closed.
Finally, if we consider a minimizing sequence of $G$-symmetric
elements $x_k\in\KL$, then the same reasoning is valid due to the last
statement of \cref{koro:critpoint_lowerenergy} and because of the fact
that $G$-symmetry is a closed condition since each $\G\in G$ is a
continuous mapping from $\ML$ onto $\ML$.
\end{proof}


Even if the energy is only in $C^1$, we can use Ekeland's variational
principle to obtain energy-minimizing
Palais--Smale sequences subconverging to
energy minimizers. 

\begin{corollary}[Minimizers]
\label{cor:critical+minimizers}
Let $\EL\in C^1(\ML)$ satisfy the Palais--Smale condition {\rm (PS)} and conditions \ref{lower-bound} and \ref{condL**}.
Let $\KL$ be a connected component of $\ML$.
Then there are a minimizing {\rm (PS)}-sequence and a minimizer of $\EL |_{\KL}$.

If  $\KL$ contains a $G$-symmetric element and if
 $\EL$ is $G$-invariant, then
there exists a (not necessarily $G$-symmetric) {\rm (PS)}-sequence for $\EL|_\KL$ that converges to
a $G$-symmetric element in $\KL$ that realizes $\inf\{\EL(y):y\in\KL,\,\textnormal{$y$
is $G$-symmetric}\}$.
These statements hold true also for $\KL = \ML$.
\end{corollary}
\begin{proof}
We  choose a minimizing sequence $(x_k)_{k \in \N}$ of $\EL |_{\KL}$ such that $\EL(x_k) \le \inf(\EL|_{\KL}) + 1/k^2$.
The function $\EL$ is continuous and the set $\KL$ is closed.
Hence, condition \ref{condL**} implies that the sublevel set 
$
	\mathcal{U} \ceq \braces[\big]{x \in \KL : \EL(x) \leq \inf (\EL|_\KL) + 2}
$ 
equipped with the restriction of $\dist_\ML$ is a complete metric space.
Now we apply Ekeland's variational principle (see, e.g., \cite[Chapter~1,Theorem~5.1]{struwe_2008a}) to find $y_k \in \mathcal{U}$
such that 
$
	\EL(y_k) \le \EL(x_k)
$,
$
	\dist_\ML(x_k,y_k) \le 1/k
$,
and
\begin{equation}
	\label{eq:ekeland-ineq}
	\EL(y_k) \leq \EL(z) + \tfrac{1}{k} \dist_\ML(y_k,z) \quad \Foa z\in\mathcal{U}
	.
\end{equation}
We have $\EL(y_k) \leq \EL(x_k) \leq \inf(\EL|_{\KL}) + 1 < \inf(\EL|_\KL) + 2$.
Because $\EL$ is continuous and because $\KL$ is open, $ y_k $ is contained in the interior of $ \UL $.
So, for every tangent vector $h\in T_{y_k}\ML$ 
there is a $\sigma > 0$ and a $C^1$-path $c \colon \intervaloo{-\sigma,\sigma} \to \mathcal{U}$ satisfying $c(0)=y_k$ and $\dot c(0) = h$.
By continuity, we can take $\sigma$ so small that
\begin{equation}\label{eq:tangent-small}
	\textstyle
	\norm{\dot c(t)}_{g_{c(t)}}\le 2\norm{h}_{g_{c(0)}} = 2 \norm{h}_{T_{y_k}\ML}
\quad\Foa t\in (-\sigma,\sigma).
\end{equation}
Applying \cref{eq:ekeland-ineq} to the point
$z \ceq c(t)$ for any $t\in (0,\sigma)$
we obtain
\begin{equation}\label{eq:PS-weg}
\textstyle
	\EL(y_k)-\EL(c(t))
	\overset{\cref{eq:ekeland-ineq}}{\le}
	\frac1{k}\dist_\ML(y_k,c(t)) \le \frac1{k}\int_0^t
	\norm{c'(\tau)}_{g_{c(\tau)}}\d \tau\le \frac2{k}\norm{h}_{T_{y_k}\ML}\cdot t
	.
\end{equation}
Dividing by $t>0$ and taking the limit $t\searrow 0$,
we arrive at
$\D \EL_{y_k} h \le \frac{2}{k} \norm{h}_{T_{y_k}\ML}$, hence
\[ 
	\norm{\D\EL_{y_k}}_{(T_{y_k}\ML)^*} \le \tfrac{2}{k}\to 0
	\quad  \text{as} \quad  k \to\infty
	.
\] 
Thus, $(y_k)_k$ is a minimizing (PS)-sequence for $\EL|_{\KL}$.
In particular, it is a (PS)-sequence for $\EL$.
Because $\EL$ satisfies the (PS)-condition, the sequence subconverges to some $y_\infty \in \ML$: $y_{k_i}\to y_\infty$ as $i\to\infty$.
Since $\mathcal{U}$ is closed, we have $y_\infty \in \mathcal{U} \subset \KL$, hence
\[
	\inf(\EL|_{\KL})
	\leq 
	\EL(y_\infty)
	=
	\lim_{i\to\infty} \EL(y_{k_i})
	\le
	\lim_{i\to\infty} \EL(x_{k_i})
	=
	\inf(\EL|_{\KL})
	. 
\]
Thus, $y_\infty$ is the desired minimizer.

If $\EL$ is $G$-invariant,
we can start with a minimizing sequence $(x_k)_k\subset\KL$ of $G$-symmetric
elements, and then follow the same line of arguments to show
that a subsequence $(x_{k_i})_i\subset (x_k)_k$ 
converges to some $y_\infty\in \KL$ as $i\to\infty$. Because $G$-symmetry is a closed condition, we see that the limit point $y_\infty$ is $G$-symmetric, too. Finally, we notice that the above argument goes through, too, if we replace $\KL$ by $\ML$.
\end{proof}
