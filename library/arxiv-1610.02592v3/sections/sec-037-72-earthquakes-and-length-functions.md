---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-037-72-earthquakes-and-length-functions
section_title: "Earthquakes and length functions"
section_number: 7.2
pages: 202-210
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.983
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
Simple closed geodesics are a formidable tool to study $\Teich(S_g)$: we can use a simple closed geodesic to \emph{twist} a metric (the operation is called an \emph{earthquake}), and by simply looking at the lengths of the other closed geodesics we can measure how the metric varies along this transformation. We introduce these operations here; later on, we will use them to parametrize $\Teich(S_g)$.


\subsection{Earthquakes} \label{earthquakes:subsection}
The hyperbolic, flat, and spherical metrics on surfaces may be twisted along simple closed geodesics: this operation is called an \emph{earthquake}.\index{earthquake} 

Let $m$ be a complete hyperbolic, flat, or elliptic metric on an oriented surface $S$ and $\gamma$ be a simple closed geodesic in $S$. Recall that $\gamma$ is a map $\gamma \colon S^1 \to S$. Fix an angle $\theta \in \matR$. Informally, a new complete hyperbolic, flat, or elliptic metric $m_\theta$ on $S$ is constructed by cutting $S$ along $\gamma$ and regluing with a counterclockwise twist of angle $\theta$. Formally, the new metric is defined as follows.

\begin{figure}
\begin{center}
\includegraphics[width = 10cm] {\iftoggle{BW}{prodotto-BW}{prodotto}}
\nota{A $R$-annulus around a simple closed geodesic $\gamma$ on a hyperbolic surface is the quotient of a $R$-neighbourhood of a line $l$ by a hyperbolic transformation. The orthogonal (\iftoggle{BW}{light grey}{green}) geodesic segments are parametrized by arc length as $[-R,R]$, hence the $R$-annulus is naturally parametrized as $S^1 \times [-R,R]$.}
\label{prodotto:fig}
\end{center}
\end{figure}

In the hyperbolic case, recall from Proposition \ref{tube:prop} that $\gamma$ has a $R$-neighbourhood isometric to a $R$-tube for some $R>0$. A $R$-tube in dimension two is a $R$-annulus as in Figure \ref{prodotto:fig}, defined by quotienting a $R$-neighbourhood of a line $l$ by a hyperbolic transformation. The $R$-annulus is naturally parametrized as $S^1\times [-R,R]$, where $\{e^{it}\}\times [-R,R]$ is the geodesic segment orthogonal to $\gamma$ in $\gamma(e^{it})$ parametrized by arc length.
The flat and elliptic cases are analogous.

\begin{figure}
\begin{center}
\includegraphics[width = 10cm] {\iftoggle{BW}{twist-BW}{twist}}
\nota{To define the earthquake we pick a diffeomorphism of the $R$-annulus that modifies the orthogonal segments as shown here.}
\label{twist:fig}
\end{center}
\end{figure}

We choose a diffeomorphism $\varphi$ of $S^1\times [-R, R]$ that curves the segments left-wise with step $\theta$ as in Figure \ref{twist:fig}-(right).  More precisely, let $f\colon[-R, R] \to \matR$ be a smooth function which is zero on $\left[-R, -\frac R 2\right]$ and is constantly $\theta$ on $\left[\frac R 2,R\right]$. We set $\varphi(e^{it},s) = (e^{i(t+f(s))},s)$.

We define a new metric $m_\theta$ on $S_g$ as follows: the metric tensor $m_\theta$ coincides with $\varphi_* m$ on the $R$-annulus and coincides with $m$ on the complement of the $\frac{R}2$-annulus $S^1\times \left[-\frac R2, \frac R2\right]$.

\begin{prop} The metric tensor $m_\theta$ is well-defined and gives a complete hyperbolic, flat, or elliptic metric to $S_g$. 
\end{prop}
\begin{proof}
It is well-defined because $m$ and $m_\theta$ coincide on $S^1\times \left[\frac R 2, R\right]$, since $(e^{it},s)\mapsto (e^{i(t+\theta)},s)$ is an isometry of the $R$-annulus. It is hyperbolic, flat, or elliptic because both patches $m$ and $\varphi_*m$ are.
\end{proof}

\begin{oss} \label{R:oss}
In the new metric $m_\theta$ the curve $\gamma$ is still a simple closed geodesic of the same length as before, and its $R$-neighbourhood is also unchanged. 
\end{oss}

Of course by deforming an elliptic metric in this way we get nothing new, because all the elliptic metrics on $S^2$ are isometric. Earthquakes are interesting only in the flat and hyperbolic geometries.


\subsection{The earthquake map}
We consider the surface $S_g$ with $g\geqslant 1$ and show that earthquakes define nice actions on the Teichm\"uller space $\Teich(S_g)$. 

If $m$ is any flat or hyperbolic metric and $\gamma$ is a non-trivial simple closed curve in $S_g$, we define $m_\theta^\gamma$ to be the flat or hyperbolic metric obtained from $m$ via an earthquake of angle $\theta$ performed along the unique (up to translations if $g=1$) simple closed geodesic homotopic to $\gamma$ in the metric $m$.\index{earthquake map}

\begin{prop}
The \emph{earthquake map}
\begin{align*}
E_\gamma\colon \matR \times \Teich(S_g) & \longrightarrow \Teich(S_g) \\
 (\theta, m) & \longmapsto m_\theta^{\gamma} 
\end{align*}
is a well-defined action of $\matR$ on $\Teich(S_g)$. The map $E_\gamma$ depends only on the homotopy class of $\gamma$.
\end{prop}
\begin{proof}
The only ambiguity in the definition of $m_\theta^\gamma$ is the choice of the function $f\colon [-R,R] \to \matR$. If we use another function $f'$ the resulting metric $(m_\theta^\gamma)'$ changes only by an isotopy: the diffeomorphism of $S_g$ which is the identity outside the $R$-annulus and sends $(e^{it},s)$ to $(e^{i(t+f(s)-f'(s))},s)$ is an isometry between $m_\theta^\gamma$ and $(m_\theta^\gamma)'$, and is clearly isotopic to the identity.

To prove that $E_\gamma$ is an action we need to check that 
$$m_{\theta+\theta'}^{\gamma} = \left(m_{\theta'}^\gamma\right)_\theta^\gamma.$$
By Remark \ref{R:oss} we can take the same $R$-annulus to compose two earthquakes and the equality follows.
\end{proof}

Like the Dehn twists $T_\gamma$ defined in Section \ref{Dehn:twist:subsection}, the action $E_\gamma$ depends on the orientation of $S_g$ but not on the orientation of $\gamma$. There is indeed a strong relation between earthquakes and Dehn twists on $\gamma$: as objects acting on Theichm\"uller space, the first generalise the second.

\begin{prop} \label{root:prop}
We have $T_\gamma(m) = E_\gamma(2\pi,m)$.
\end{prop}
\begin{proof}
It follows directly from the definitions.
\end{proof}

We now want to study the Teichm\"uller space and the action of $E_\gamma$ on it. In mathematics a space is often beautifully described by some natural functions defined on it: this role is played here by the length functions of closed curves.


\subsection{Length functions}
A homotopically nontrivial (possibly non simple) closed curve $\gamma$ in $S_g$ defines a \emph{length function}\index{length function}
$$\ell^\gamma\colon \Teich(S_g) \to \matR_{>0}$$
which assigns to a metric $m\in\Teich(S_g)$ the length $\ell^\gamma(m)$ of the unique closed geodesic homotopic to $\gamma$. 

When $g=1$ we must actually specify a couple of things in the definition: the closed geodesic $\gamma$ is unique only up to translations, which do not affect its length; 
on the other hand rescaling \emph{does} affect lengths, so to get a well-defined length function we always rescale the metric $m$ to have unit area. 

We want to study these length functions, and as usual we start by analysing the simpler torus flat world, where everything can be described explicitly.


\subsection{Length functions on the torus} \label{length:torus:subsection}
We denote every (isotopy class of) non-trivial simple closed curve on $T$ with a coprime pair $(p,q)$ of integers and we identify the Teichm\"uller space $\Teich(T)$ with $H^2\subset\matC$, see Propositions \ref{mn:prop} and \ref{Teich:T:prop}. The length functions may be written explicitly.

\begin{prop} \label{lunghezza:toro:prop}
The formula holds:
$$\ell^{(p,q)}(z) = \frac{|p+qz|}{\sqrt{\Im z }}$$
for every simple closed curve $(p,q)$ and every metric $z\in H^2$.
\end{prop}
\begin{proof}
Up to rescaling we have $T=\matR^2/_{\Gamma}$ with $\Gamma = \langle 1,z \rangle $. The translation in $\Gamma$ corresponding to $(p,q)$ is $p\cdot 1 + q\cdot z$ and the closed geodesic it produces has length $|p+qz|$. The area of the torus $T$ is $\Im z$ (see a fundamental domain in Figure \ref{toro_dominio:fig}) and hence we must rescale it by $1/\sqrt{\Im z}$.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 9cm] {\iftoggle{BW}{toro_terremoto-BW}{toro_terremoto}}
\nota{A torus with metric $z$ (left) twisted along the horizontal curve $\gamma$ (right). The curve $\alpha$ is a closed geodesic in the new metric.}
\label{toro_terremoto:fig}
\end{center}
\end{figure}

We can also write the earthquake action on the meridian $m=(1,0)$ of $T$.

\begin{ex} \label{terremoto:toro:ex}
We have:
$$E_m(\theta, z) = z+\frac {\theta}{2\pi}.$$
\end{ex}
\begin{proof}[Hint]
Look at the closed geodesic $\alpha$ in Figure \ref{toro_terremoto:fig}.
\end{proof}

We have discovered in particular that $E_m$ is a parabolic isometry of $H^2$, and we can now consider the earthquake action along a generic curve $(p,q)$.

\begin{cor} 
The earthquake action $E_{(p,q)}$ is the 1-parameter family of parabolic transformations with fixed point $-\frac pq \in \partial H^2$. 
\end{cor}
\begin{proof}
We know this when $(p,q)=(1,0)=m$. In general, we send $(1,0)$ to $(p,q)$ via some element of the mapping class group: this element acts by isometries of $H^2$ by Proposition \ref{toro:azione:prop} and sends $\infty$ to $-\frac pq$. 
\end{proof}

The orbits of $E_{(p,q)}$ are the horospheres centred at $-\frac pq$. 
We have discovered that, quite unexpectedly, the hyperbolic geometry of the plane $H^2$ is well designed to model the Teichm\"uller space of the flat torus $T$. 

It is now natural to identify the \emph{unoriented} simple closed curve $\pm (p,q)$ with the rational point $-\frac pq$ in $\matR\cup\{\infty\} \subset \partial H^2$. We get the following convexity property.

\begin{cor} \label{convex:cor}
Let $\gamma$ and $\eta$ be two simple closed curves on $T$.
If $i(\gamma, \eta)>0$ then the length function $\ell^\eta$ is strictly convex on the orbits of $E_{\gamma}$.
\end{cor}
\begin{proof}
We may suppose $\gamma=m=(1,0)$ and note that the condition $i(\gamma,\eta)>0$ translates into $\eta = (p,q) \neq (\pm 1,0)$. The function in Proposition \ref{lunghezza:toro:prop} is strictly convex on the horospheres $\Im z = k$ when $(p,q)\neq (\pm 1,0)$.
\end{proof}

Summing up, the torus picture is the following: 
\begin{itemize}
\item the mapping class group acts on the Teichm\"uller space roughly like $\PSLZ$ acts isometrically on the hyperbolic plane $H^2$, 
\item the unoriented simple closed curves are in 1-1 correspondence with the rational points in $\partial H^2 = \matR\cup \infty$, 
\item earthquakes act like parabolic transformations centred at these rational points, \item the length function $\ell^\gamma$ is constant at the horospheres centred at $\gamma$ but strictly convex at the horospheres centred at all the other curves.
\end{itemize}

The main goal of Chapters \ref{Teichmuller:chapter} and \ref{automorfismi:chapter} is to draw a similar picture for surfaces $S_g$ of higher genus $g\geqslant 2$. Everything is more difficult in the hyperbolic world, because there are no nice explicit formulas describing the length functions, the action of the mapping class group, the simple closed curves, and the earthquakes. We now start by generalising the last point: the strict convexity of length functions.


\subsection{Convexity of the length functions} \label{convexity:lengths:subsection}
We consider $S_g$ with $g\geqslant 2$. Our aim now is to generalise Corollary \ref{convex:cor} to the hyperbolic setting and then later use this convexity property to parametrize $\Teich(S_g)$. We need a preliminary result.\index{convexity of the length functions}

\begin{ex} \label{convessa:ex}
Let $f\colon \matR^m \times \matR^n \to \matR_{\geqslant 0}$ be strictly convex and proper. The function
\begin{align*}
F\colon \matR^n & \longrightarrow \matR_{\geqslant 0} \\
y & \longmapsto \min \left\{f(x,y)\ \big| \ x \in \matR^m \right\}
\end{align*}
is well-defined, strictly convex, and proper. 
\end{ex}

The following generalisation of Corollary \ref{convex:cor} says that length functions are convex on the earthquakes orbits, and very often they are strictly convex and proper.

\begin{prop} \label{strettamente:convessa:prop}
Let $\eta$ and $\gamma$ be two homotopically non-trivial simple closed curves in $S_g$ and $m$ be a hyperbolic metric on $S_g$. The function 
\begin{align*}
\matR & \longrightarrow \matR_{\geqslant 0} \\
\theta & \longmapsto \ell^\eta(m_\theta^\gamma)
\end{align*}
is
\begin{itemize}
\item constant if $i(\eta,\gamma)=0$,
\item strictly convex and proper if $i(\eta, \gamma)>0$.
\end{itemize}
\end{prop}
\begin{proof}
The metric $m_\theta^\gamma$ is obtained by twisting $m$ of an angle $\theta$ along the simple closed geodesic $\gamma$. If $i(\eta,\gamma)=0$ the curves $\eta$ and $\gamma$ are disjoint geodesics in $m$ and $\eta$ is not affected by the earthquakes that we perform near $\gamma$, hence the function $\ell^\eta(m_\theta^\gamma)$ is constant.

Consider the case $n=i(\eta,\gamma)>0$. Denote by $\bar{\eta}^\theta$ the geodesic representative of $\eta$ in the twisted metric $m_\theta^\gamma$: it intersects $\gamma$ transversely in $n$ points. 

\begin{figure}
\begin{center}
\includegraphics[width = 10cm] {\iftoggle{BW}{spezza_new-BW}{spezza_new}}
\nota{A geodesic in $m_\theta^\gamma$ can be seen on the original metric $m$ as follows: it is a geodesic outside the annulus and deviates on the left by an angle $\theta$ every time it crosses it (centre). We may simplify the picture by describing it as a broken geodesic line that makes a left $\theta$-jump each time that it crosses $\gamma$ (right).}
\label{spezza:fig}
\end{center}
\end{figure}

Fix a sufficiently small $R$-annulus around $\gamma$ and note that the geodesics in $m_\theta^\gamma$ can be seen in the original metric $m$ as follows: these are curves that are geodesic outside the $R$-annulus and deviate smoothly on the left each time they cross it as in Figure \ref{spezza:fig}-(centre).
We may substitute each smooth deviation with a broken jump as shown in Figure \ref{spezza:fig}-(right) and get a bijection
$$\left\{\begin{array}{c} {\rm closed\ geodesics} \\ {\rm with\ respect\ to\ } m_\theta^\gamma \end{array} \right\}
\longleftrightarrow \left\{\begin{array}{c} {\rm broken\ geodesics} \\ {\rm with\ respect\ to\ } m \end{array}\right\}$$
where a \emph{broken geodesic} is a geodesic that at every crossing of $\gamma$ jumps to the left at distance $\frac{\theta L(\gamma)}{2\pi}$ and then keeps going on, leaving $\gamma$ with the same incidence angle (here $L(\gamma)$ is the length of $\gamma$). This correspondence is useful because it preserves the lengths: the length of the closed geodesic for $m_\theta^\gamma$ is equal to the length of the corresponding broken geodesic (which is the sum of the lengths of its components), because the segments in Figure \ref{spezza:fig}-(left) and (right) are isometric.

\begin{figure}
\begin{center}
\includegraphics[width = 6cm] {\iftoggle{BW}{spezza_su-BW}{spezza_su}}
\nota{The \iftoggle{BW}{}{(blue) }line $l$ is a lift of $\bar \eta$. Consider $n$ consecutive intersections with lifts $r_1,\ldots, r_{n+1}$ of $\gamma$\iftoggle{BW}{}{ (in red)}, with $\tau(r_1) = r_{n+1}$, and parametrize each $r_i$ with $\matR$ via arc-length. We set $\theta' = \theta L(\gamma)/2pi$.}
\label{spezza_su:fig}
\end{center}
\end{figure}

We lift this description to the universal cover $\matH^2$. We fix a lift $l$ of $\bar \eta = \bar{\eta}^0$ and pick $n+1$ consecutive intersections $r_1,\ldots, r_{n+1}$ of $l$ with the lifts of $\gamma$ as in Figure \ref{spezza_su:fig}. The hyperbolic transformation $\tau$ with axis $l$ corresponding to $\eta$ sends $r_1$ to $r_{n+1}$. We parametrise each $r_i$ with $\matR$ via arc length.

The closed geodesic $\bar{\eta}^\theta$, represented as a broken geodesic, lifts to a broken geodesic which starts at some point $x_1-\theta L(\gamma)/2\pi\in r_1$ and arrives at some other point $x_2\in r_2$, then jumps on the left at distance $\theta L(\gamma)/2\pi$ and starts again from $x_2-\theta L(\gamma)/2\pi$, and so on until it reaches the point $\tau(x_1)\in \tau(r_1) = r_{n+1}$. If we make the points $x_1\in r_1, \ldots, x_n \in r_n$ vary we get various broken paths in this way, but only one arrives and exits from each line $r_i$ with the same incidence angles and thus represents $\bar{\eta}^\theta$. The other broken paths represent piecewise-geodesic curves homotopic to $\bar{\eta}^\theta$ and are therefore longer than $\bar{\eta}^\theta$. Hence
$$\ell^\eta(m_\theta^\gamma) = \min \left\{\sum_{i=1}^n d\bigg(x_i-\frac{\theta L(\gamma)}{2\pi}, x_{i+1}\bigg) \ \Bigg|\ (x_1,\ldots, x_n) \in \matR^n \right\}$$
where $x_{n+1} = \tau(x_1)$.
We can now prove that the function $\theta \mapsto \ell^\eta(m_\theta^\gamma)$ is proper and strictly convex. The function
\begin{align*}
\psi\colon \matR^{2n} & \longrightarrow \matR \\
(x_1,y_1, \ldots, x_n,y_n) & \longmapsto \sum_{i=1}^n d(y_i,x_{i+1})
\end{align*}
where $x_{n+1}=\tau(x_1)$ is strictly convex and proper by Proposition \ref{distanza:convessa:prop}. The auxiliary function
\begin{align*}
\phi\colon \matR^{2n}\times \matR & \longrightarrow \matR \\
(x,\theta) & \longmapsto \psi(x)
\end{align*}
is only convex, but its restriction to the subspace
$$H = \bigg\{y_i = x_i - \frac{\theta l(\gamma)}{2\pi} \bigg\}$$
is strictly convex and proper, because the subspace $H$ is not parallel to the direction $(0,\ldots,0,1)$. The coordinates $x_i$ and $\theta$ identify $H$ with $\matR^n \times \matR$. The restriction $f = \phi|_H$ is hence a function $f\colon \matR^n \times \matR \to \matR$ and we obtain
$$\ell^\eta(m_\theta^\gamma) = \min \left\{f(x,\theta) \ \big| \ x \in \matR^n \right\}.$$
By Exercise \ref{convessa:ex} the function $\theta \mapsto \ell^\eta(m_\theta^\gamma)$ is strictly convex and proper. 
\end{proof}

We now employ this convexity property to prove some facts on the earthquakes and the Teichm\"uller space.


\subsection{Earthquakes on essential multicurves}
We use the convexity of the length functions to prove the following. We suppose again that $g\geqslant 2$.

\begin{cor} \label{distinti:cor}
For every simple closed curve $\gamma$, the earthquake action $E_\gamma$ on $\Teich(S_g)$ is free.
\end{cor}
\begin{proof}
Suppose by contradiction that $m = m_{\theta_0}^\gamma$ for some $\theta_0>0$. Then $m= m_{n\theta_0}^\gamma$ for every $n\in\matZ$. Let $\eta$ be a simple closed curve with $i(\eta,\gamma)>0$, which exists by Exercise \ref{eta:prop}; the function $\theta \mapsto \ell^\eta(m_\theta^\gamma)$ is strictly convex and constant on $\{n\theta_0, n \in \matZ\}$, a contradiction.
\end{proof}

The earthquake action is defined more generally for essential multicurves. An essential multicurve $\mu = \gamma_1\sqcup \cdots \sqcup \gamma_k$ of $S_g$ determines an action
\begin{align*}
E_\mu\colon \matR^{k} \times \Teich(S_g) & \longrightarrow \Teich(S_g) \\
 (\theta, m) & \longmapsto m_\theta^{\mu}
\end{align*}
where $\theta = (\theta_1,\ldots, \theta_{k})$ and $m_\theta^\mu = m_{\theta_1}^{\gamma_1} \circ \cdots \circ m_{\theta_{k}}^{\gamma_{k}}$. Note that the actions on disjoint curves commute.

\begin{figure}
\begin{center}
\includegraphics[width = 9cm] {\iftoggle{BW}{dual_curves-BW}{dual_curves}}
\nota{Choose for each component $\gamma_i$ of a pants decomposition $\mu$ a curve $\gamma_i'$ that intersects $\gamma_i$ in one or two points and is disjoint from the other components of $\mu$. There are two cases to consider, depending on whether the two pants adjacent to $\gamma_i$ are distinct (left) or not (right). }
\label{dual_curves:fig}
\end{center}
\end{figure}

\begin{cor}
For every essential multicurve $\mu$, the earthquake action $E_\mu$ on $\Teich(S_g)$ is free. 
\end{cor}
\begin{proof}
We may complete $\mu$ to a pants-decomposition $\mu=\gamma_1\sqcup \ldots \sqcup \gamma_{3g-3}$. Pick for every $i=1,\ldots, 3g-3$ a curve $\gamma_i'$ as in Figure \ref{dual_curves:fig} such that $i(\gamma_i,\gamma_i') > 0$ for all $i$ and $i(\gamma_i, \gamma_j')=0$ for all $i\neq j$. 

Suppose by contradiction that $m=m_\theta^\mu$ for some $\theta\neq 0$: hence $m_{n\theta}^\mu = m$ for all $n\in\matZ$. There is an $i$ such that $\theta_i\neq 0$. The length function $\ell^{\gamma_i'}(m_\theta^\mu)$ depends only on $\theta_i$ and not on the other coordinates of $\theta$: therefore it equals $\ell^{\gamma_i'}(m_{\theta_i}^{\gamma_i})$ which is strictly convex, a contradiction.
\end{proof}
