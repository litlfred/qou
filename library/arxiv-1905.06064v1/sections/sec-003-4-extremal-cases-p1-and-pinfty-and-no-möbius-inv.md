---
doc_id: arxiv-1905.06064v1
doc_title: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS"
section_id: sec-003-4-extremal-cases-p1-and-pinfty-and-no-möbius-inv
section_title: "Extremal cases p=1 and p=infty, and no Möbius invariance for p=2"
section_number: 4
pages: 17-22
source_pdf: 1905.06064v1.pdf
source_sha256: 3ffe25c8ee62779d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.743
latex_coverage_ratio: 0.973
doc_brief: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS — We develop a regularity theory for extremal knots of scale invariant knot ener- gies deﬁned by J. O’hara in 1991."
---
\label{s:distortion}
The following definition goes back to Gromov~\cite{G83}, see also
O'hara~\cite{OH92}.

\begin{definition}[distortion]
 For any curve $\g\in C^{0}\rzd$ let
 \[ \distor\g := \sup_{\substack{x,y\in\R/\Z\\x\ne y}}
 \frac{\mathcal{D}_{\g}(x,y)}{\abs{\g(x)-\g(y)}} \]
 if $\g$ is injective and $\distor\g :=\infty$ else.
\end{definition}

\begin{lemma}
 Let $\g\in C^{0,1}\rzd$ be parametrized by arc-length. Then
 \[ \liminf_{\a\searrow0}\tfrac1\a\br{\E(\g)}^{\a/4} \ge\log\distor\g. \]
\end{lemma}

\begin{proof}
 We may assume that $\g$ is injective since otherwise
 $\E(\g)$ would be infinite.
 We compute
 \begin{align*}
  &\frac1\a\br{\frac1{\abs{\D}^{\a}}-\frac1{\mathcal{D}_{\g}(x,y)^{\a}}} \\
  &=\frac1{\a\abs{\D}^{\a}}\br{1-\frac{\abs{\D}^{\a}}{\mathcal{D}_{\g}(x,y)^{\a}}} \\
  &=\frac1{\abs{\D}^{\a}}\int_{\frac{\abs{\D}}{\mathcal{D}_{\g}(x,y)}}^{\a-1}\xi^{-1}\d\xi.
 \end{align*}
 On $|x-y|\ge\delta>0$ the integral uniformly converges,
 \[ \int_{\frac{\abs{\D}}{\mathcal{D}_{\g}(x,y)}}^{1}\xi^{\a-1}\d\xi
 \xrightarrow{\a\searrow0} \int_{\frac{\abs{\D}}{\mathcal{D}_{\g}(x,y)}}^{1}\xi^{-1}\d\xi
 = \log\frac{\mathcal{D}_{\g}(x,y)}{\abs{\D}}, \]
 i.e., for given $\eps>0$ there is some $\a_{0}=\a_{0}(\delta,\eps)>0$ such
 that, for any $\a\in(0,\a_{0})$, these two quantities
 differ at most by $\eps$.
 
 By definition of distortion, for given $\eps>0$ we may choose points $x_{0},y_{0}\in\R/\Z$,
 $x_{0}\ne y_{0}$, such that
 \[ \br{\distor\g\ge}\quad \frac{\mathcal{D}_{\g}(x_{0},y_{0})}{\abs{\g(x_0)-\g(y_{0})}}
 \ge e^{-\eps}\distor\g. \]
 Moreover, we may find some $\delta=\delta(\eps)>0$
 such that the $\delta$-neighborhoods of $x_{0}$ and $y_{0}$
 are disjoint in $\R/\Z$ and
 \[ \frac{\mathcal{D}_{\g}(x,y)}{\abs{\g(x)-\g(y)}}
 \ge e^{-2\eps}\distor\g
 \qquad\text{for all }x\in B_{\delta}(x_{0}), y\in B_{\delta}(y_{0}). \]
 For any $\a\in(0,\a_{0})$ we arrive at
 \begin{align*}
  &\iint_{(\R/\Z)^{2}}\sq{\frac1\a\br{\frac1{\abs{\g(x)-\g(y)}^{\a}}-\frac1{\mathcal{D}_{\g}(x,y)^{\a}}}}^{2/\a}\d x\d y \\
  &\ge\int_{B_\delta(x_{0})}\int_{B_\delta(y_{0})}\sq{\frac1\a\br{\frac1{\abs{\g(x)-\g(y)}^{\a}}-\frac1{\mathcal{D}_{\g}(x,y)^{\a}}}}^{2/\a}\d y\d x \\
  &=\int_{B_\delta(x_{0})}\int_{B_\delta(y_{0})}\frac1{\abs{\g(x)-\g(y)}^{2}}\br{\int_{\frac{\abs{\D}}{\mathcal{D}_{\g}(x,y)}}^{1}\xi^{\a-1}\d\xi}^{2/\a}\d y\d x \\
  &\ge\int_{B_\delta(x_{0})}\int_{B_\delta(y_{0})}\frac1{\abs{\g(x)-\g(y)}^{2}}\br{\log\frac{\mathcal{D}_{\g}(x,y)}{\abs{\g(x)-\g(y)}}-\eps}^{2/\a}\d y\d x \\
  &\ge\int_{B_\delta(x_{0})}\int_{B_\delta(y_{0})}\frac1{\abs{\g(x)-\g(y)}^{2}}\br{\log\distor\g-3\eps}^{2/\a}\d y\d x \\
  &\ge\br{\log\distor\g-3\eps}^{2/\a}\frac{(2\delta)^{2}}{(\abs{x_{0}-y_{0}}_{\R/\Z}+2\delta)^{2}}.
 \end{align*}
 Thus we arrive at
 \[ \liminf_{\a\searrow0}\tfrac1\a\br{\E(\g)}^{\a/4} \ge\log\distor\g-3\eps. \]
\end{proof}

\begin{lemma}
 Let $\g\in C^{1,\beta}\rzd$ for some $\beta\in(0,1]$
 be parametrized by arc-length. Then
 \[ \limsup_{\a\searrow0}\tfrac1\a\br{\E(\g)}^{\a/4} \le\log\distor\g. \]
\end{lemma}

\begin{proof}
 We may assume that $\g$ is injective since otherwise its distortion
 would be infinite.
 As in the preceding proof we have
 \begin{align}\label{eq:distor-limsup}
  \begin{split}
  &\frac1\a\br{\frac1{\abs{\D}^{\a}}-\frac1{\mathcal{D}_{\g}(x,y)^{\a}}} \\
  &=\frac1{\a\abs{\D}^{\a}}\br{1-\frac{\abs{\D}^{\a}}{\mathcal{D}_{\g}(x,y)^{\a}}} \\
  &=\frac1{\abs{\D}^{\a}}\int_{\frac{\abs{\D}}{\mathcal{D}_{\g}(x,y)}}^{1}\xi^{\a-1}\d\xi \\
  &\le\frac1{\abs{\D}^{\a}}\int_{\frac{\abs{\D}}{\mathcal{D}_{\g}(x,y)}}^{1}\xi^{-1}\d\xi \\
  &=\frac1{\abs{\D}^{\a}} \log\frac{\mathcal{D}_{\g}(x,y)}{\abs{\D}}.
  \end{split}
 \end{align}
 We compute for some constant $C>0$ only depending on $\g$
 \begin{align*}
  1&\ge\frac{\abs{\D}^{2}}{|x-y|^{2}}\\
  &=\abs{\int_{0}^{1}\dg(x+\theta (y-x))\d\theta}^{2} \\
  &=\iint_{[0,1]^{2}}{} \left \langle\dg(x+\theta_{1} (y-x)),\dg(x+\theta_{2} (y-x))\right \rangle\d\theta_{2}\d\theta_{1} \\
  &=1-\tfrac12\iint_{[0,1]^{2}}\abs{\dg(x+\theta_{1} (y-x))-\dg(x+\theta_{2} (y-x))}^{2}\d\theta_{2}\d\theta_{1} \\
  &\geq 1-C\, |x-y|^{2\beta}.
 \end{align*}
 This is bounded below by $\frac12$ provided $|x-y|\le (2C)^{-1/2\beta}$
 (we also assume $|x-y|\le\frac12$).
 In this case, the right-hand side of~\eqref{eq:distor-limsup} is
 majorized by
 \begin{align*}
 &\frac1{\abs{\D}^{\a}} \log\frac{\mathcal{D}_{\g}(x,y)}{\abs{\D}} \\
 &\le \frac1{2|x-y|^{\a}\br{1-C|x-y|^{2\beta}}^{\a}}\log\frac{\mathcal{D}_{\g}(x,y)^{2}}{\abs{\D}^{2}} \\
 &\le \frac1{2^{1-\a}|x-y|^{\a}}\log\frac{|x-y|^{2}}{\abs{\D}^{2}} \\
 &\le \frac1{2^{1-\a}|x-y|^{\a}}\log\frac1{1-C|x-y|^{2\beta}} \\
 &\le 2^{\a-1}\frac{C|x-y|^{2\beta-\a}}{1-C|x-y|^{2\beta}} \\
 &\le 2^{\a} C|x-y|^{2\beta-\a}.
 \end{align*}
 On the other hand, if $|x-y|\ge (2C)^{-1/2\beta}$ we have
 \[ \abs\D\ge c>0\]
 by injectivity.
 Letting $\eps\in\br{0,(2C)^{-1/2\beta}}$ and $\a<4\beta$
 we arrive at
 \begin{align*}
 &\tfrac1\a\br{\E(\g)}^{\a/4} \\
 &=\br{\int_{\R/\Z}\int_{-1/2}^{1/2}\sq{\frac1\a\br{\frac1{\abs{\D}^{\a}}-\frac1{\mathcal{D}_{\g}(x,y)^{\a}}}}^{2/\a}\d w\d u}^{\a/4} \\
 &\le\br{\iint_{|x-y|\ge(2C)^{-1/2\beta}}\cdots}^{\a/4}
 + \br{\iint_{|x-y|\le(2C)^{-1/2\beta}}\cdots}^{\a/4} \\
 &\le\br{\iint_{|x-y|\ge\eps} \frac1{c^{2}}\br{\log\frac{|x-y|}{\abs\D}}^{2/\a}\d w\d u}^{\a/4} \\
 &\qquad{}+ \br{\iint_{|x-y|\le(2C)^{-1/2\beta}}4C^{2/\a}|x-y|^{4\beta/\a-2}\d w\d u}^{\a/4} \\
 &\le \frac1{c^{\a}}\log\distor\g + C\br{\frac{8\eps^{4\beta/\a-1}}{\frac{4\beta}\a-1}}^{\a/4} \\
 &\le \frac1{c^{\a}}\log\distor\g + C\br{\frac{8\a}{{4\beta-\a}}}^{\a/4}\eps^{2\beta-\a/4} \\
 &\xrightarrow{\a\searrow0}\log\distor\g+C\eps^{2\beta}.
 \end{align*}
\end{proof}

Subsuming the past two results we obtain

\begin{corollary}
 Let $\g\in C^{1,\beta}\rzd$ for some $\beta\in(0,1]$
 be parametrized by arc-length. Then
 \[ \tfrac1\a\br{\E(\g)}^{\a/4}\xrightarrow{\a\searrow0}\log\distor\g. \]
\end{corollary}

\begin{corollary}\label{cor:alpha0}
 There is some $\a_{0}\in(0,2]$ such that
 $\E$ is \emph{not} M\"obius invariant for any $\a\in(0,\a_{0})$.
\end{corollary}

The preceding statement immediately follows from

\begin{example}[Distortion is not M\"obius invariant]
 We consider the square
 \[ Q = \sett{(x,y)\in\R^{2}}{\max\br{\abs x,\abs y}\le 1} \]
 which we identify with an arbitrary (injective) arc-length parametrization.
 In order to see $\distor Q = 2$ we consider the quotient
 $\frac{\mathcal{D}_{\g}(x,y)}{\abs{\g(x)-\g(y)}}$
 for different configurations of $x,y\in\R/\Z$, $x\ne y$.
 If $x,y$ belong to the same edge of Q it clearly amounts to~$1$
 while we arrive at~$\sqrt 2$ in case of $x,y$ belonging to neighboring edges.
 For opposite edges we evaluate the quotient at points
 $(\xi,-1)$ and $(\eta,1)$, $\xi,\eta\in[-1,1]$.
 Without loss of generality we may assume $\xi+\eta\ge0$, thus
 $\frac{d_{Q}(x,y)}{\abs{Q(x)-Q(y)}} = \frac{4-\xi-\eta}{\sqrt{2^{2}+(\xi-\eta)^{2}}} \le 2$
 with equality if $\xi=\eta=0$.
 
 Now we perform an inversion on the unit circle $x^{2}+y^{2}=1$.
 It maps the edges of $Q$ onto segments of the circles
 passing to the origin and tangentially meeting the
 intersection of $Q$ with the axes, see Figure~\ref{fig:distor} (left).
 The points $\pm(1,1)$ are mapped to $\pm\br{\frac12,\frac12}$
 while the length of the two arcs joining them
 now amounts to~$\pi$.
 The distortion of the inversion of $Q$ is therefore bounded below by
 $\frac\pi{\sqrt 2} > \frac3{\sqrt 2} > 2$.
\end{example}

\begin{figure}
 \includegraphics[height=4cm]{square}\quad
 \includegraphics[height=4cm]{stadion.pdf}
 \caption{The square $Q$ (left) and a station curve $\sigma$ (right) inverted on the unit circle.}\label{fig:distor}
\end{figure}

Conjecture~\ref{conj} means that we have $\a_{0}=2$ in Corollary~\ref{cor:alpha0}.

Rather than providing a rigorous proof of the preceding statement by suitably
decomposing the integration domain and carefully estimating
based on techniques from~\cite{blatt-reiter-2008},
we illustrate the situation by providing a numerical experiment that supports the latter conjecture (and which we believe should be possible to be made rigorous with a careful, lengthy computation).

To this end, we consider the stadion curve $\sigma$ depicted in Figure~\ref{fig:distor} (right)
which is constructed by vertically cutting the unit circle into two half
circles and horizontally delating the left one by $\pi$.
This gives $\distor\sigma=\pi$.

Now we approximate the energy values $\tfrac1\alpha\br{\E}^{\a/4}$,
$\a\in(0,2]$, for
the (unit) circle, the stadion curve $\sigma$ and its inversion on the
unit circle.
We employ a straightforward mid-point based quadrature.
Let $\br{x_{j}}_{j=1,\dots,N}\subset\R^{2}$
denote a set of vertices which form a polygonal approximation of the curve.
As it is assumed to be closed, we set $x_{j\pm N}=x_{j}$ for all $j=1,\dots,N$.
So the approximative length $L = \sum_{\ell=1}^{N}\abs{x_{j+1}-x_{j}}$ is well-defined.
For any $j,k\in\{1,\dots,N\}$, $j\le k$, we let
$d_{j,k} = d_{k,j} = \min\br{\sum_{\ell=j}^{k-1}\abs{x_{j+1}-x_{j}},
L-\sum_{\ell=j}^{k-1}\abs{x_{j+1}-x_{j}}}$.
Furthermore, we set
$\Delta_{j} = \tfrac12\br{\abs{x_{j+1}-x_{j}}+\abs{x_{j}-x_{j-1}}}$.
In order to avoid cancellation effects for $\alpha\searrow0$
which occur when evaluating the approximative energy value
\[  \frac1\a\br{\sum_{j,k=1}^{N}\br{\frac1{\abs{x_{j+1}-x_{j}}^{\a}}-\frac1{d_{j,k}^{\a}}}^{2/\a}\Delta_{j}\Delta_{k}}^{\a/4}, \]
we use the (algebraically equal) term
\[ \log\beta \br{\sum_{j,k=1}^{N}\frac1{\abs{x_{j+1}-x_{j}}^{2}}\br{\frac{1-\br{\frac{\abs{x_{j+1}-x_{j}}}{d_{j,k}}}^{\a}}{\a\log\beta}}^{2/\a}\Delta_{j}\Delta_{k}}^{\a/4} \]
where $\beta = \max_{j,k=1,\dots,N}\frac{d_{j,k}}{\abs{x_{j}-x_{k}}}$
approximates the distortion.

The results presented in Figure~\ref{fig:energy-plot} suggest
that $\E$ is not M\"obius invariant unless $\a=2$.
In this experiment we have chosen $N=1000$.
We find that our values for the circle agree
with those obtained using the integral formula derived by
Abrams et al.~\cite[(24)]{Abrams2003} up to
a relative error of about $10^{-3}$.

\begin{figure}
 \includegraphics[scale=.8]{plot.pdf}
 \caption{Plot of $\alpha\mapsto\tfrac1\alpha\br{\E}^{\a/4}$
 for the circle and the curves depicted in Figure~\ref{fig:distor} (right).}\label{fig:energy-plot}
\end{figure}

When $\alpha \to 4$ (or $p \to 1$) we converge to the total curvature functional.
\begin{proposition}
If $\sol: \R/\Z \to \R^3$ is a constant speed, bilipschitz parametrization of a knot then
\[
 \lim_{\alpha \to 4^-} \frac{4-\alpha}{4} \mathcal{O}^{\alpha,\frac{4}{\alpha}}(\sol) = c \int_{\R / \Z} |\sol''|.
\]
\end{proposition}
\begin{proof}
We have by Lemma~\ref{la:EOequal},
\[
 \mathcal{O}^{\alpha,\frac{4}{\alpha}}(\sol) = \mathcal{E}^{\alpha,\frac{4}{\alpha}} (\sol').
\]
From Lemma~\ref{la:Gpest} 

\[
 \mathcal{E}^{\alpha,\frac{4}{\alpha}} (\sol') \aeq \llbracket u \rrbracket_{W^{\frac{\alpha}{4},\frac{4}{\alpha}}(\R/\Z)}^p
\]
In view of Proposition~\ref{pr:Wspequivalence}
\[
 \llbracket \sol' \rrbracket_{W^{\frac{\alpha}{4},\frac{4}{\alpha}}(\R/\Z)}^{\frac{4}{\alpha}} \aeq [\sol']_{W^{\frac{\alpha}{4},\frac{4}{\alpha}}(\R/\Z)}^{\frac{4}{\alpha}}.
\]
From \cite{BBM01} we know that
\[
 \lim_{\alpha \to 4^-} \brac{1-\frac{4}{\alpha}} [\sol' ]_{W^{\frac{\alpha}{4},\frac{4}{\alpha}}(\R/\Z)}^{\frac{4}{\alpha}} \aeq \int_{\R/\Z}|\sol''|
\]
The claim follows.
\end{proof}


\begin{appendix}

\section{A new norm for \texorpdfstring{$W^{\beta,p}$}{W(s,p)}}
Let
\[
\begin{split}
 \dmv{u}{v}(x,y) :=& \int_0^1\int_0^1 \big (u(x+s(y-x)) - u(x+t(y-x)) \big ) \cdot \big (v(x+s(y-x)) - v(x+t(y-x)) \big )\ ds\ dt\\
 =&  \rho(x,y)^{-2} \int_x^y\int_x^y \big (u(s) - u \big ) \cdot \big (v(s) - v(t) \big )\ ds\ dt
\end{split}
 \]
We set 
\[
  \llbracket u \rrbracket_{W^{\beta,p}(S)} := \brac{\int_{\iv}\int_{\iv} \frac{\brac{\dmv{u}{u}(x,y)}^{\frac{p}{2}}}{\rho(x,y)^{1+\beta p}}\ dx\ dy}^{\frac{1}{p}}.
\]
The semi-norm $\llbracket u \rrbracket_{W^{\beta,p}(S)}$ is equivalent to the usual $W^{\beta,p}$-seminorm for $\beta$ large enough -- note that in particular for our situation where $p = \frac{1}{s}$ this equivalence holds. Here
\[
  [u ]_{W^{\beta,p}(S)} := \brac{\int_{\iv}\int_{\iv} \frac{\left | u(x)-u(y)\right |^{\frac{p}{2}}}{\rho(x,y)^{1+\beta p}}\ dx\ dy}^{\frac{1}{p}}.
\]



\begin{proposition}\label{pr:normalunnormalWsp}
For $p \in (1,\infty)$, $\beta \in (0,1)$ so that $\beta > \frac{1}{p}-\frac{1}{2}$ we have for any $u \in C_c^\infty(\R)$, for any interval $\iv \subseteq \R$,
\begin{equation}\label{eq:unnormalnormalWsp}
 \llbracket u \rrbracket_{W^{\beta,p}(S)} \aleq [u]_{W^{\beta,p}(S)}.
\end{equation}
The constant is independent of $u$ and $I$.

For $p \in (1,\infty)$, $\beta \in (0,1)$ so that $\beta > \frac{1}{p}-\frac{1}{2(p-1)}$ we have for any $u \in C_c^\infty(\R)$,
\begin{equation}\label{eq:normalunnormalWsp}
 [u]_{W^{\beta,p}(\R)} \aleq \llbracket u \rrbracket_{W^{\beta,p}(\R)}.
\end{equation}
There is a fixed number $L \in \mathbb{N}$ so that for any compact interval $\iv_\rho \subset \R$ of sidelength $\rho$ denoting with $\iv_{2^L \rho}$ the concentric interval with sidelength $2^L \rho$, we have for a fixed 
\begin{equation}\label{eq:normalunnormalWspI}
 [u]_{W^{\beta,p}(\iv_\rho)} \aleq \llbracket u \rrbracket_{W^{\beta,p}(\iv_{2^L \rho})}.
\end{equation}


\end{proposition}
To see this we need the following two Lemmata.

\begin{lemma}\label{la:Ast}
Let $A(s,t) \subset \R^2$ be the set
\begin{equation}\label{eq:Ast}
 (x,y) \in A(s,t) \Leftrightarrow \min \{x,y\} < s,t < \max \{x,y\}.
\end{equation}
Then for any $\mu > 0$, and any $s \neq t$
\begin{equation}\label{eq:intast}
 \int_{A(s,t)} \rho(x,y)^{-2-\mu} d(x,y)= \frac{2}{\mu(1+\mu)} |t-s|^{-\mu}.
\end{equation}
\end{lemma}
\begin{proof}
W.l.o.g. $s < t$. Then by symmetry we have
\[
\begin{split}
 &\int_{A(s,t)} \rho(x,y)^{-2-\mu} dy\ dx\\
 =& 2\int_{x=-\infty}^{s} \int_{y=t}^\infty \rho(x,y)^{-2-\mu} dy\ dx\\
 =& 2\int_{x=-\infty}^{s} \int_{y=t-x}^\infty |y|^{-2-\mu} dy\ dx\\
 =& \frac{2}{1+\mu}\int_{x=-\infty}^{s} (t-x)^{-1-\mu} dx\\
 =& \frac{2}{1+\mu}\int_{\rho=t-s}^{\infty} (\rho)^{-1-\mu} d\rho\\
 =& \frac{2}{\mu(1+\mu)} (t-s)^{-\mu}.
\end{split}
 \]
\end{proof}

\begin{lemma}\label{la:meanvalueintest}
Let $p >0$, $\beta \in (0,1)$, $q \in (1,\infty)$ so that  $\beta > \frac{1}{pq}-\frac{1}{q}$ then for any $u \in C_c^\infty(\R)$ and any interval $\iv \subseteq \R$,
\begin{equation}\label{eq:dualest2}
 \int_{\iv} \int_{\iv} \frac{\brac{\rho(x,y)^{-2} \int_x^y\int_x^y |u(s)-u(t)|^{q}\ ds\ dt}^{p}}{\rho(x,y)^{1+\beta p q}}\ dx\ dy \aleq [u]_{W^{\beta,pq}(S)}^{pq}.
\end{equation}
Also for $I \subseteq \R$ an interval,
\begin{equation}\label{eq:dualest3}
 \int_{\R} \int_{\R} \frac{\brac{\rho(x,y)^{-2} \int_x^y\int_x^y \chi_S(s,t)|u(s)-u(t)|^{q}\ ds\ dt}^{p}}{\rho(x,y)^{1+\beta p q}}\ dx\ dy \aleq [u]_{W^{\beta,pq}(S)}^{pq}.
\end{equation}

\end{lemma}
\begin{proof}
The \eqref{eq:dualest3} follows the same way as \eqref{eq:dualest2}. We just prove the latter one.

If $p \geq 2$, with Jensen's inequality
\[
 \frac{\brac{\rho(x,y)^{-2} \int_x^y\int_x^y |u(s)-u(t)|^{q}\ ds\ dt}^{p}}{\rho(x,y)^{1+\beta p q}} \leq \rho(x,y)^{-3-\beta p q}\ \int_x^y\int_x^y |u(s)-u(t)|^{pq}\ ds\ dt.
\]
With Fubini (note that $s,t \in I$ if $x,y \in I$), setting $A(s,t)$ as in \eqref{eq:Ast} and using \eqref{eq:intast},
\[
\begin{split}
 &\int_{\iv} \int_{\iv} \frac{\brac{\rho(x,y)^{-2} \int_x^y\int_x^y |u(s)-u(t)|^{q}\ ds\ dt}^{p}}{\rho(x,y)^{1+\beta p q}}\ dx\ dy\\
 \aleq &\int_{\iv} \int_{\iv} |u(s)-u(t)|^{pq} \int_{A(s,t)} \rho(x,y)^{-3-\beta p q}\ d(x,y)\ ds\ dt\\
 =&c\int_{\iv} \int_{\iv} |u(s)-u(t)|^{pq} |s-t|^{-1-\beta p q}\ ds\ dt\\
 =&[u]_{W^{\beta,pq}(S)}^{pq}.
\end{split}
 \]
Now assume $0 < p <2$, then Jensen's inequality fails. We use instead Poincar\`e-Sobolev inequality $W^{\alpha,pq} ((x,y)) \subset L^q((x,y))$ for $\alpha \in (0,1)$ satisfying $\alpha \geq \frac{1}{pq}-\frac{1}{q}$. More precisely we have the estimate
\[
\begin{split}
 &\rho(x,y)^{-2} \int_x^y\int_x^y \chi_S(s,t) |u(s)-u(t)|^{q}\ ds\ dt\\
 \aleq & \rho(x,y)^{\alpha q-\frac{1}{p}} \brac{\int_x^y\int_x^y \chi_S(s,t) \frac{|u(s)-u(t)|^{pq}}{|s-t|^{1+\alpha pq}}\ ds\ dt}^{\frac{1}{p}}\\
\end{split}
 \]
Observe that this estimate would have followed from directly H\"older's inequality for $p \geq 1$. We need it however for $p > 0$.

We arrive at
\[
 \frac{\brac{\rho(x,y)^{-2} \int_x^y\int_x^y |u(s)-u(t)|^{q}\ ds\ dt}^{p}}{\rho(x,y)^{1+\beta p q}} \leq \rho(x,y)^{-2-(s-\alpha)pq}\int_x^y\int_x^y \frac{|u(s)-u(t)|^{pq}}{|s-t|^{1+\alpha pq}}\ ds\ dt
\]
Our assumption on $s$ implies that we may pick $\alpha < s$. Then we may employ again Fubini, again having $A(s,t)$ as in \eqref{eq:Ast} and using \eqref{eq:intast},
\[
\begin{split}
 &\int_{\iv} \int_{\iv} \frac{\brac{\rho(x,y)^{-2} \int_x^y\int_x^y |u(s)-u(t)|^{q}\ ds\ dt}^{p}}{\rho(x,y)^{1+\beta p q}}\ dx\ dy\\
 \aleq &\int_{\iv} \int_{\iv} \frac{|u(s)-u(t)|^{pq}}{|s-t|^{1+\alpha pq}} \int_{A(s,t)} \rho(x,y)^{-2-(s-\alpha)pq}\ d(x,y)\ ds\ dt\\
 \overset{\eqref{eq:intast}}{=}&c\int_{\iv} \int_{\iv} |u(s)-u(t)|^{pq} |s-t|^{-1-\beta p q}\ ds\ dt =[u]_{W^{\beta,pq}(S)}^{pq}.
\end{split}
 \]

\end{proof}

From Lemma~\ref{la:meanvalueintest} follows Proposition~\ref{pr:normalunnormalWsp}.
\begin{proof}[Proof of Proposition~\ref{pr:normalunnormalWsp}]
The estimate \eqref{eq:unnormalnormalWsp} follows directly from Proposition~\ref{pr:normalunnormalWsp}.

For \eqref{eq:normalunnormalWsp} we employ a duality argument. We have
\[
\begin{split}
&[u ]_{W^{\beta,p}(S)}^p\\
=&\int_{\iv}\int_{\iv} \frac{|u(s)-u(t)|^{p-2} (u(s)-u(t)) \cdot (u(s)-u(t))}{|s-t|^{1+\beta p}}\ ds\ dt\\
=&c\int_{\iv}\int_{\iv} |u(s)-u(t)|^{p-2} (u(s)-u(t)) \cdot (u(s)-u(t)) \int_{A(s,t)} \rho(x,y)^{-(3+\beta p)}\ d(x,y)\ ds\ dt,
\end{split}
\]
where $A(s,t) \subset \R^2$ is defined as in \eqref{eq:Ast}.

With Fubini's theorem we then have
\[
\begin{split}
&[u ]_{W^{\beta,p}(S)}^p\\
=&c\int_{\R} \int_{\R} \frac{\rho(x,y)^{-2} \int_x^y\int_x^y \chi_{I}(s,t) |u(s)-u(t)|^{p-2} (u(s)-u(t)) \cdot (u(s)-u(t)) ds\ dt}{\rho(x,y)^{1+\beta p}}\ dx\ dy,
\end{split}
\]
Let us for now assume that $I = \R$, then simply with H\"older's inequality,
\[
\begin{split}
\leq&c\int_{\R} \int_{\R} \frac{\brac{\rho(x,y)^{-2} \int_x^y\int_x^y \chi_{I}(s,t)|u(s)-u(t)|^{(p-1)2}\ ds\ dt}^{\frac{1}{2}} \brac{\rho(x,y)^{-2} \int_x^y\int_x^y \chi_{I}(s,t)|u(s)-u(t)|^{2}\ ds\ dt}^{\frac{1}{2}}}{\rho(x,y)^{1+\beta p}}\ dx\ dy\\
\leq&c\brac{\int_{\R} \int_{\R} \frac{\brac{\rho(x,y)^{-2} \int_x^y\int_x^y |u(s)-u(t)|^{(p-1)2}\ ds\ dt}^{\frac{p'}{2}} }{\rho(x,y)^{1+\beta p}}\ dx\ dy}^{\frac{1}{p'}}\ \llbracket u \rrbracket_{W^{\beta,p}(\R)}
\end{split}
\]
Because of  $s > \frac{1}{p}-\frac{1}{2(p-1)}$, from Lemma~\ref{la:meanvalueintest}  we obtain
\[
 \brac{\int_{\R} \int_{\R} \frac{\brac{\rho(x,y)^{-2} \int_x^y\int_x^y |u(s)-u(t)|^{(p-1)2}\ ds\ dt}^{\frac{p'}{2}} }{\rho(x,y)^{1+\beta p}}\ dx\ dy}^{\frac{1}{p'}} \aleq [u]_{W^{\beta,p}(\R)}^{\frac{p}{p'}}.
\]
This proves \eqref{eq:normalunnormalWsp}.

If $\iv$ is a compact interval, we have by the above estimates
\[
\begin{split}
&[u ]_{W^{\beta,p}(\iv_\rho)}^p\\
\aleq &[u]_{W^{\beta,p}(\iv_\rho)}^{p-1}\ \llbracket u \rrbracket_{W^{\beta,p}(\iv_{2^L \rho})}\\
&+\int_{\R} \int_{\R} \chi_{\R \backslash \iv_{2^L \rho}}(x,y) \frac{\rho(x,y)^{-2} \int_x^y\int_x^y \chi_{\iv_\rho}(s,t) |u(s)-u(t)|^{p-2} (u(s)-u(t)) \cdot (u(s)-u(t)) ds\ dt}{\rho(x,y)^{1+\beta p}}\ dx\ dy\\
\end{split}
\]
Since we have disjoint support, we can be rough and estimate
\[
\begin{split}
 &\int_{\R} \int_{\R} \chi_{\R \backslash \iv_{2^L \rho}}(x,y) \frac{\rho(x,y)^{-2} \int_x^y\int_x^y \chi_{\iv_\rho}(s,t) |u(s)-u(t)|^{p-2} (u(s)-u(t)) \cdot (u(s)-u(t)) ds\ dt}{\rho(x,y)^{1+\beta p}}\ dx\ dy\\
 \aleq &\int_{\iv_\rho} \int_{\iv_\rho} |u(s)-u(t)|^p\ ds\ dt\ \int_{x < \iv_\rho} \int_{y > \iv_{2^L\rho}} \frac{\rho(x,y)^{-2} }{\rho(x,y)^{1+\beta p}}\ dx\ dy\\
 \aleq& 2^{L(-1-\beta p)} [u]_{W^{\beta,p}(\iv_\rho)}^p.
\end{split}
 \]
Having $L$ be chosen large enough, we can absorb and finished proving \eqref{eq:normalunnormalWspI}.
\end{proof}



\section{Computations}

\begin{lemma}\label{la:disjointest1}
For $\varphi \in C_c^\infty(\iv_\rho)$, $L \in \N$, $k \in \N$, we have the estimate
\[
\begin{split}
 &\brac{\int_{\iv_{2^L \rho}}\int_{\iv_{2^{L+k} \rho} \backslash \iv_{2^{L+k-1}}} \frac{1}{\rho(x,y)^{2}} \brac{\rho(x,y)^{-2} \int_x^y \int_x^y |\solu(s)-\solu(t)||\varphi(s) v(s) - \varphi(t) v(t)|\ ds\ dt}^{\frac{p}{2}}\ dx\ dy}^{\frac{2}{p}}\\
 \aleq& 2^{-s(L+k)} \ \|v\|_\infty\ [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{L+k}\rho })}\ \|\laps{\frac{1}{p}}\varphi\|_{L^{p}}\\
\end{split}.
\]
\end{lemma}
\begin{proof}
W.l.o.g. $\iv_\rho$ is centered around $0$. 

Note that the support of $\varphi$ tells us that whenever $x,y > \rho$ or $x,y < -\rho$,
\[
\frac{1}{\rho(x,y)^{2}} \brac{\rho(x,y)^{-2} \int_x^y \int_x^y |\solu(s)-\solu(t)||\varphi(s) v(s) - \varphi(t) v(t)|\ ds\ dt}^{\frac{p}{2}} \equiv 0.
\]
Thus, it suffices to estimate 
\[
\begin{split}
 &\int_{-2^L \rho}^{\rho}\int_{2^{L+k-1} \rho}^{2^{L+k}\rho} \frac{1}{\rho(x,y)^{1+\frac{1}{p}}} \brac{\rho(x,y)^{-2} \int_x^y \int_x^y |\solu(s)-\solu(t)||\varphi(s) v(s) - \varphi(t) v(t)|\ ds\ dt}^{\frac{p}{2}}\ dx\ dy\\
 \aleq& (2^{L+k} \rho)^{-2-p} (2^L \rho) (2^{L+k} \rho) \brac{\int_{\iv_{2^{L+k}\rho}} \int_{\iv_{2^{L+k}\rho}} |\solu(s)-\solu(t)||\varphi(s) v(s) - \varphi(t) v(t)|\ ds\ dt}^{\frac{p}{2}}\\
 \aleq& (2^{L+k} \rho)^{-1-p} (2^L \rho)\ \|v\|_\infty^{\frac{p}{2}} (2^{L+k} \rho)^{p-2} \int_{\iv_{2^{L+k}\rho}} \int_{\iv_{2^{L+k}\rho}} |\solu(s)-\solu(t)|^{\frac{p}{2}}\ |\varphi(s) - \varphi(t) |^{\frac{p}{2}}\ ds\ dt\\
 &+ (2^{L+k} \rho)^{-1-p} (2^L \rho)  (2^{L+k} \rho)^{p-2} \int_{\iv_{2^{L+k}\rho}} \int_{\iv_{2^{L+k}\rho}} |\solu(s)-\solu(t)|^{\frac{p}{2}}\ |\varphi(t)|^{\frac{p}{2}} |v(t)-v(s)|^{\frac{p}{2}}\ ds\ dt\\
 =& (2^{L+k} \rho)^{-3} (2^L \rho)\ \|v\|_\infty^{\frac{p}{2}} \int_{\iv_{2^{L+k}\rho}} \int_{\iv_{2^{L+k}\rho}} |\solu(s)-\solu(t)|^{\frac{p}{2}}\ |\varphi(s) - \varphi(t) |^{\frac{p}{2}}\ ds\ dt\\
 &+ (2^{L+k} \rho)^{-3} (2^L \rho)   \int_{\iv_{2^{L+k}\rho}} \int_{\iv_{2^{L+k}\rho}} |\solu(s)-\solu(t)|^{\frac{p}{2}}\ |\varphi(t)|^{\frac{p}{2}} |v(t)-v(s)|^{\frac{p}{2}}\ ds\ dt\\
 \aleq& (2^{L+k} \rho)^{-3} (2^L \rho)\ \|v\|_\infty^{\frac{p}{2}} \brac{\int_{\iv_{2^{L+k}\rho}} \int_{\iv_{2^{L+k}\rho}} |\solu(s)-\solu(t)|^{p}\ ds\ dt}^{\frac{1}{2}}\ \brac{2^{L+k} \rho\ \|\varphi\|^p_{L^p}}^{\frac{1}{2}}\\
 \aleq& (2^{L+k} \rho)^{-\frac{5}{2}} (2^L \rho)\ \|v\|_\infty^{\frac{p}{2}}\ \brac{(2^{L+k} \rho )^{1+1} [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{L+k}\rho }) }^p}^{\frac{1}{2}}\ \brac{\rho^{1} \|\laps{\frac{1}{p}}\varphi\|_{L^{p}}^p }^{\frac{1}{2}}\\
  =& (2^{L+k} )^{-\frac{3}{2}} (2^L )\ \|v\|_\infty^{\frac{p}{2}}\ \brac{[\solu]_{W^{\frac{1}{p},p}(\iv_{2^{L+k}\rho }) }^p}^{\frac{1}{2}}\ \brac{ \|\laps{\frac{1}{p}}\varphi\|_{L^{p}}^p }^{\frac{1}{2}}\\
 \end{split}
 \]

\end{proof}


\end{appendix}


\bibliographystyle{abbrv}
