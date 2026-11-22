---
doc_id: arxiv-1905.06064v1
doc_title: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS"
section_id: sec-001-2-a-new-energy-e
section_title: "A new energy E"
section_number: 2
pages: 4-10
source_pdf: 1905.06064v1.pdf
source_sha256: 3ffe25c8ee62779d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.985
doc_brief: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS — We develop a regularity theory for extremal knots of scale invariant knot ener- gies deﬁned by J. O’hara in 1991."
---
In this section we find a new energy $\mathcal{E}^{\alpha,p}(\solu)$ applied to maps $\solu: \R/\Z \to \S^2$ so that any critical knot (parametrized by arc-length) induces a critical $\S^2$-valued map $\solu$ and vice versa. 

The main result in this section is the following equivalence between an energy $\mathcal{E}^{\alpha,p}$ which will be defined below and the O'hara energy $\mathcal{O}^{\alpha,p}$.

\begin{theorem}\label{th:criticalpointchar}
For $\alpha p = 4$, $p \geq 2$. Let $\sol: \R/\Z \to \R^3$ be a knot parametrized with constant speed with finite energy $\mathcal{O}^{\alpha,p}(\sol) < \infty$. 

Denote with $\solu := c^{-1} \sol': \R/\Z \to \S^2$ its unit tangent field, where $c \equiv |\sol'|$.
Then $(1) \Rightarrow (2)$, where
\begin{enumerate}
 \item $\sol$ is a critical knot for $\mathcal{O}^{\alpha,p}$, that is $\mathcal{O}^{\alpha,p}(\sol) < \infty$ and for any $\varphi \in C^\infty(\R/\Z,\R^3)$ we have
\[
 \delta\mathcal{O}^{\alpha,p}(\sol,\varphi) := \frac{d}{d\eps} \Big |_{\eps = 0} \mathcal{O}^{\alpha,p}(\sol+\eps \varphi) = 0.
\]
 \item $\solu$ is a critical map for $\mathcal{E}^{\alpha,p}$ in the class of maps $\solv: \R/\Z \to \S^2$ with finite energy $\mathcal{E}^{\alpha,p}$, that is for any $\varphi \in C^\infty(\R/\Z,\R^3)$ we have
 \[
  \frac{d}{d\eps} \Big |_{\eps = 0} \mathcal{E}^{\alpha,p}\brac{\frac{\solu+\eps \varphi}{|\solu+\eps \varphi|}} = 0.
 \]

\end{enumerate}

\end{theorem}


Let us remark again that for the convenience of the reader we will refer to critical \emph{knots} when referring to criticality with respect to the O'hara energy $\mathcal{O}^{\alpha,p}$ acting on in isotopy classes, and a critical \emph{map} when we refer to criticality with respect to the energy $\mathcal{E}^{\alpha,p}$ as maps between the manifolds $\R/\Z \to \S^2$. In principle both are of course critical points of the respective energy in a certain domain.

The important advantage of $u$ being a critical map in the above sense for $\mathcal{E}^{\alpha,p}$ is that the class of permissible is independent of the topological constraints of $\sol$, and are exactly the variations permitted for harmonic maps into $\S^2$ -- thus the regularity theory for harmonic maps comes into play.

To define properly the energy $\mathcal{E}^{\alpha,p}$ we first fix some notation for integrating on $\R/\Z$. The reader may decide to skip the following notation and use common sense when interpreting the meaning of respecitve integrals.
\begin{remark}[Technicalities on integration on segments of $\R/\Z$]
\begin{enumerate} 
\item We denote with $\rho(x,y)$ the distance on $\R/\Z$, namely $\rho(x,y) = |x-y| \mod 1$.
 \item For $x,y \in \R/\Z$ there are two geodesics. If $x$ and $y$ are not not antipodal (i.e. $|x-y| \neq \frac{1}{2}$) let $\go{x}{y}$ be the shortest geodesic (with orientation $x$ to $y$), and for this case we define the integral, for $\Z$-periodic $f$,
 \[
  \igo{x}{y} f\ ds:= \int_{x}^{\tilde{y}} f(z)\, dz(z),
\]
where $\tilde{y} \in y + \Z$ such that $|x-\tilde{y}| < \frac{1}{2}$.









Note that this is an integral with orientation

in the sense that
\[
  \igo{x}{y} f\ ds  =  -\igo{y}{x} f\ ds 
\]
\item We define the mean value integral on a segment $S \subset \R/\Z$
\[
 \mvint_{\iv} f := \frac{1}{\mathcal{H}^1(S)} \int_S f\ d\mathcal{H}^1.
\]
(i.e. the mean value is always without taking into account the orientation). In particular,
\[
 (f)_{\R/\Z} =  \int_{\R/\Z} f = \int_{0}^{1} f(z)\ dz.
\]
Moreover we write
\[
 \migo{x}{y} f \equiv \mvint_{|\go{x}{y}|} f = \frac{\sigma(\go{x}{y})}{\rho(x,y)}\ \igo{x}{y} f\ ds,
\]
where
\[
 \sigma(\go{x}{y}) = {\rm sgn} \igo{x}{y} 1,
\]
that is $\sigma(\go{x}{y})$ is $+1$ if $\go{x}{y}$ from $x$ to $y$ is positively oriented, and $-1$ if it is negatively oriented. In particular,
\[
 \migo{x}{y} f= \migo{y}{x} f,
\]
and
\[
 \migo{x}{y} f \geq 0 \quad \mbox{if $f \geq 0$ on $\go{x}{y}$}.
\]
\item We then have the fundamental theorem of calculus in the following form. For any non-antipodal points $x,y \in \R/\Z$ we have
\[
 f(y)-f(x) = \igo{x}{y} f'(z)\ dz,
\]
where $f'$ is the derivative.
\end{enumerate}
\end{remark}
With this notation, we can define the energy $\mathcal{E}^{\alpha,p}$. Firstly for two maps $\solu,\solv: \R/\Z \to \R^3$ we denote 
\begin{equation}\label{eq:bracketdef}
 \dmv{\solu}{\solv}(x,y) :=  \migo{x}{y}\migo{x}{y} \big (\solu(z_1) - \solu(z_2) \big ) \cdot \big (\solv(z_1) - \solv(z_2) \big )\ dz_1\ dz_2.
 \end{equation}
For nonnegative $a,b,c$ we set
\begin{equation}\label{eq:Flagrangian}
 F(a,b,c) := \brac{\brac{b- \frac{1}{2} a}^{-\frac{\alpha}{2}}   -c^{-\alpha}}^{\frac{p}{2}}.
\end{equation}
Also for later use define
\begin{equation}\label{eq:Glagrangian}
 G(a) := F(a,1,1) = \brac{\brac{1- \frac{1}{2} a}^{-\frac{\alpha}{2}}  -1}^{\frac{p}{2}}.
\end{equation}
Now the energy $\mathcal{E}^{\alpha,p}$ is defined as follows.
\begin{equation}\label{eq:E}
 \mathcal{E}^{\alpha,p}(\solu) = \int_{\R/\Z}\int_{\R/\Z} F\brac{\dmv{\solu}{\solu}(x,y), \migo{x}{y} |\solu-(\solu)_{\R/\Z}|^2 , \migo{x}{y} |\solu-(\solu)_{\R/\Z}|}\ |\solu(x)- (\solu)_{\R/\Z}|\, |\solu(y)-(\solu)_{\R/\Z}|\ \frac{dx\ dy}{\rho(x,y)^{\alpha p /2}}.
\end{equation}
We will see later, see Proposition~\ref{la:EOequal}, that $\mathcal{E}^{\alpha,p}$ is comparable to the Gagliardo-norm $[\solu]_{W^{\frac{\alpha}{2}-\frac{1}{p},p}}^p$, so we are formally in the realm of $W^{\beta,p}$-harmonic maps into the sphere, for which regularity theory has been developed by the third-named author \cite{SchikorraCPDE14}, see also \cite{MS18}.


\subsection{Properties of \texorpdfstring{$\mathcal{E}^{\alpha,p}$}{Eap}}
Let $\sol: \R/\Z \to \R^3$ be a constant speed parametrization of a knot. For $c := |\sol'|$ we set $u := c^{-1}  \sol'$. 

In \cite{Blatt12} the first-named author characterized the energy space of knots with finite O'hara energies. Which imply the following properties, Lemma~\ref{la:lambda} and Lemma~\ref{la:Gpest}.

\begin{lemma}\label{la:lambda}
Whenever $\sol$ has finite energy $\mathcal{O}^{\alpha,p}$, $\alpha p = 4$, $p \geq 2$, then there exists $\lambda = \lambda(\solu)$ such that
\begin{equation}\label{eq:ubilipschitz}
 \sup_{x,y \in \R / \Z} \dmv{\solu}{\solu}(x,y) \leq \lambda.
\end{equation}
 \end{lemma}
\begin{proof}
In \cite[Lemma 2.1]{Blatt12} the first-named author showed that whenever $\sol$ has finite energy $\mathcal{O}^{\alpha,p}$ then there exists a bilipschitz constant $L = L(\sol) > 0$ such that
\[
 L \leq \frac{\sol(x)-\sol(y)}{|x-y|}.
\]
Consequently, since $\solu = c^{-1} \sol'$,
\[
\begin{split}
 \dmv{\solu}{\solu}(x,y)= &\igo{x}{y} \igo{x}{y} |\solu(s)-\solu(t)|^2\, ds\, dt\\
 =& c^{-2} \igo{x}{y} \igo{x}{y} |\sol'(s)-\sol'(t)|^2\, ds\, dt\\
 =& \igo{x}{y} \igo{x}{y} 2-\frac{2}{c^2} \langle \sol'(s), \sol'(t)\rangle \, ds\, dt\\
=&\brac{ 2-2 c^{-2}\frac{|\sol(y)-\sol(x)|^2}{|x-y|^2}}\\
\leq& 2-2 c^{-2}L^2 =: \lambda.
\end{split}
 \]
\end{proof}

\begin{lemma}\label{la:Gpest}
For $s \in [0,\lambda]$ for some $\lambda < 2$,
\[
 |G(s)| \aeq s^{\frac{p}{2}}.
\]
the derivative
\[
 |G'(s)| \aeq s^{\frac{p-2}{2}}.
\]
The constants depend on $\lambda$.
\end{lemma}
\begin{proof}
Firstly, for $s \in [0,\lambda]$ with L'hopital one obtains
\[
 \brac{1- \frac{1}{2} s}^{-\frac{\alpha}{2}}  -1 \aeq s.
\]
Also for all $s \in [0,\lambda]$,
\[
 (1- \frac{1}{2} s) \aeq 1.
\]
Finally compute and conclude with
\[
 G'(s) := \frac{\alpha p}{8} \brac{\brac{1- \frac{1}{2} s}^{-\frac{\alpha}{2}}  -1}^{\frac{p-2}{2}}\ \brac{1- \frac{1}{2} s}^{-\frac{\alpha+2}{2}}.
\]
\end{proof}

For $\solu: \R/\Z \to \S^2$ satisfying \eqref{eq:ubilipschitz} and $\int_{\R/\Z} \solu = 0$, the energy $\mathcal{E}^{\alpha,p}(\solu)$ is comparable to the following $W^{\frac{\alpha}{2}-\frac{1}{p},p}$-seminorm $\llbracket f \rrbracket_{W^{\beta,p}(\R)}$ which for an interval $\iv$ is defined as
\[
 \llbracket f \rrbracket_{W^{\beta,p}(\iv)} = \brac{\int_{\iv}\int_{\iv} \frac{\dmv{f}{f}(x,y)^{\frac{p}{2}}}{\rho(x,y)^{1+\beta p}}\ dx\ dy}^{\frac{1}{p}}.
\]
The notion $W^{\beta,p}(\iv)$ is justified, since for $\beta$ sufficiently large in terms of $p$ we have the following equivalence to the usual $W^{\beta,p}$-norm,
\[
 [f]_{W^{\beta,p}(\iv)} = \brac{\int_{\iv}\int_{\iv} \frac{|f(x)-f(y)|^p}{\rho(x,y)^{1+\beta p}}\ dx\ dy}^{\frac{1}{p}}.
\]
For
\begin{proposition}\label{pr:Wspequivalence}
For $p \in (1,\infty)$, $\beta \in (0,1)$ such that $1 > \beta > \frac{1}{p}-\frac{1}{2}$ we have (with constants depeding on $p$, $\beta$)
\[
 \llbracket \solu \rrbracket_{W^{\beta,p}(\R/\Z)} \aeq [\solu]_{W^{\beta,p}(\R/\Z)}.
 \]
\end{proposition}
The proof is given in the appendix, see Proposition~\ref{pr:normalunnormalWsp}. 


\subsection{Proof of Theorem~\ref{th:criticalpointchar}}
We introduce an auxiliary energy $\tilde{\mathcal{E}}^{\alpha,p}$ which is the same as $\mathcal{E}^{\alpha,p}$ only that the third component in $F$, namely $\migo{x}{y} |\solu-(\solu)_{\R/\Z}|$, is replaced by 
\[
 d_{\solu}(x,y) := \min \left \{ \rho(x,y)\migo{x}{y} |\solu(z)-(\solu)_{\R/\Z}|, (1-\rho(x,y)) \mvint_{\R/\Z \backslash \go{x}{y}}  |\solu(z)-(\solu)_{\R/\Z}| \right \}.
\]
Observe that when $\solu = \sol'$ then $d_{\solu}(x,y)$ simplifies to
\[
 d_{\solu}(x,y) \equiv \mathcal{D}_{\sol}(x,y):= \min \left \{ \rho(x,y)\migo{x}{y} |\solu(z)|, (1-\rho(x,y)) \mvint_{\R/\Z \backslash \go{x}{y}} |\solu(z)| \right \},
\]
i.e. the intrinsic distance of $\sol(x)$ to $\sol(y)$ along $\sol$.

That is,
\[
\tilde{\mathcal{E}}^{\alpha,p}(\solu) = \int_{\R/\Z}\int_{\R/\Z} F\brac{\dmv{\solu}{\solu}(x,y), \migo{x}{y} |\solu-(\solu)_{\R/\Z}|^2 , \frac{d_{\solu}(x,y)}{\rho(x,y)}}\ |\solu(x)- (\solu)_{\R/\Z}|\, |\solu(y)-(\solu)_{\R/\Z}|\ \frac{dx\ dy}{\rho(x,y)^{\alpha p /2}}.
\]
Then we have
\begin{lemma} \label{la:EOequal}
For any knot $\sol$ with finite energy $\mathcal{O}^{\alpha,p}$ we have
\[\tilde{\mathcal{E}}^{\alpha,p}(\sol') = \mathcal{O}^{\alpha,p}(\sol).\] 
If the knot $\sol$ is moreover \emph{arclength-parametrized} or more generally \emph{constant speed},
\[\mathcal{E}^{\alpha,p}(\sol') = \mathcal{O}^{\alpha,p}(\sol).\] 
\end{lemma}
\begin{proof}
Firstly, $(\sol')_{\R/\Z} = 0$. Thus $\mathcal{D}_{\sol}(x,y) = d_{\sol'}(x,y)$, and we have
\[
\tilde{\mathcal{E}}^{\alpha,p}(\sol') = \int_{\R/\Z}\int_{\R/\Z} F\brac{\dmv{\sol'}{\sol'}(x,y), \migo{x}{y} |\sol'|^2 , \frac{\mathcal{D}_{\sol}(x,y)}{\rho(x,y)}}\ |\sol'(x)|\, |\sol'(y)|\ \frac{dx\ dy}{\rho(x,y)^{\alpha p /2}}.
\]
We have
\[
 F\brac{\dmv{\sol'}{\sol'}(x,y), \migo{x}{y} |\sol'|^2 , \frac{\mathcal{D}_{\sol}(x,y)}{\rho(x,y)}}
 =\brac{\brac{\migo{x}{y}|\sol'|^2- \frac{1}{2}\dmv{\sol'}{\sol'}}^{-\frac{\alpha}{2}}-\brac{\frac{\rho(x,y)}{\mathcal{D}_{\sol}(x,y)}}^{\alpha}}^{\frac{p}{2}}
 \]
We recall $\dmv{\sol'}{\sol'}$ defined in \eqref{eq:bracketdef}. Then we have (the orientation cancels),
\[
 \frac{|\sol(x)-\sol(y)|^2}{\rho(x,y)^2} =  \migo{x}{y} |\sol'|^2-\frac{1}{2}\migo{x}{y}\migo{x}{y} |\sol'(s)-\sol'(t)|^2  = \migo{x}{y} |\sol'|^2 - \frac{1}{2} \dmv{\sol'}{\sol'}(x,y).
 \]
Thus,
\[
\frac{F\brac{\dmv{\sol'}{\sol'}(x,y), \migo{x}{y} |\sol'|^2 , \mathcal{D}_{\sol}(x,y)}}{\rho(x,y)^{\frac{\alpha p}{2}}}\\
 =\brac{\frac{1}{|\sol(x)-\sol(y)|^{\alpha}}-\frac{1}{\mathcal{D}_{\sol}(x,y)^{\alpha}}}^{\frac{p}{2}}\\
 \]
This shows $\tilde{\mathcal{E}}^{\alpha,p}(\sol') = \tilde{O}^{\alpha,p}(\sol')$.


If $\sol$ is arclength-parametrized,
\[
 \frac{\mathcal{D}_{\sol}(x,y)}{\rho(x,y)} = 1 = \migo{x}{y} |\solu-(\solu)_{\R/\Z}|.
\]
Thus, $\mathcal{E}^{\alpha,p}(\sol') = \tilde{\mathcal{E}}^{\alpha,p}(\sol')$ for arclength parametrized $\sol$.
\end{proof}



Now we are ready to show

\begin{proof}[Proof of Theorem~\ref{th:criticalpointchar}: (1) $\Rightarrow$ (2)]
Observe for any $c > 0$,
\[
 \mathcal{E}^{\alpha,p}(c^{-1}\sol') = c^{\alpha p-2}\mathcal{E}^{\alpha,p}(\sol'),
\]
and
\[
 \tilde{\mathcal{E}}^{\alpha,p}(c^{-1}\sol') = c^{\alpha p-2}\tilde{\mathcal{E}}^{\alpha,p}(\sol').
\]
Thus, we shall assume w.l.o.g. $\sol' = u$ (i.e. $c \equiv 1$) without changing anything about the criticality.

For $\vp \in C^\infty(\R/\Z ,\R^3)$ let
\[
 \solu_\eps := \frac{\solu+\eps \vp}{|\solu+\eps \vp|},
\]
and 
\[
 \sol_\eps(x) := \sol(0) + \igo{0}{x} \brac{\solu_\eps -(\solu_\eps)_{\R/\Z}}.
 \]
Then, since $\solu_\eps-\sol_\eps'   = (\solu_\eps)_{\R/\Z}$ is constant, we find
\[
 \tilde{\mathcal{E}}^{\alpha,p}(\solu_\eps) = \tilde{\mathcal{E}}^{\alpha,p}(\solu_\eps-(\solu_\eps)_{\R/\Z})= \tilde{\mathcal{E}}^{\alpha,p}(\sol_\eps').
\]
On the other hand, by Lemma~\ref{la:EOequal}, for all small $\eps$ (so that the energies are finite),
\[
 \mathcal{O}^{\alpha,p}(\sol_\eps) = \tilde{\mathcal{E}}^{\alpha,p}(\sol_\eps').
\]
Moreover, we observe that
\begin{equation}\label{eq:soluepsexpansion}
 \solu_\eps  = \solu + \eps \Pi(\solu) \vp  + O(\eps^2),f
\end{equation}
where $\Pi(\solu)$ is the orthogonal projection onto $T_\solu \S^2$,
\[
 \Pi(\solu)\solv = \solv-\langle \solv,\solu\rangle \solu
\]
and
\[
 \sol_\eps(x) = \sol(x) + \eps\igo{0}{x} \brac{\Pi(\solu)\vp-(\Pi(\solu)\vp)_{\R/\Z}} + O(\eps^2).
 \]
Thus $\sol_\eps$ is a variation of $\sol$, so because of $\sol$ being by (i) a critical knot of $\mathcal{O}^{\alpha,p}$ we have
\begin{equation}
\label{eq:OtE}
\frac{d}{d\eps}\Big |_{\eps = 0} \tilde{\mathcal{E}}^{\alpha,p}(\solu_\eps) = \frac{d}{d\eps}\Big |_{\eps = 0}\mathcal{O}^{\alpha,p}(\sol_\eps) = 0.
\end{equation}


In order to make the step from $\tilde{\mathcal{E}}$ to $\mathcal{E}$, recall that the $\tilde{\mathcal{E}}$ is $\mathcal{E}$ only replacing $\frac{d_{\solu_\eps}(x,y)}{\rho(x,y)}$ by $\migo{x}{y} |\solu_\eps(z)-(\solu_\eps)_{\R/\Z}|$. We show that this does not change the derivative $\frac{d}{d\eps} \Big|_{\eps = 0}$, by Lebesgue theorem:

Firstly, by definition
\[
 \frac{d_{\solu_\eps}(x,y)}{\rho(x,y)} = \min \left \{ \migo{x}{y} |\solu_\eps(z)-(\solu_\eps)_{\R/\Z}|, \frac{(1-\rho(x,y))}{\rho(x,y)} \mvint_{\R/\Z \backslash \go{x}{y}} |\solu_\eps(z)-(\solu_\eps)_{\R/\Z}| \right \}.
\]
Since $|\solu| = 1$ and $(\solu)_{\R/\Z} = 0$, for any $x,y$ not antipodal,
\[
 \migo{x}{y} |\solu_\eps(z)-(\solu_\eps)_{\R/\Z}| = 1+O(\eps).
\]
Also, $\rho(x,y) \leq 1$ and thus
\[
 \frac{(1-\rho(x,y))}{\rho(x,y)} \mvint_{\R/\Z \backslash \go{x}{y}} |\solu_\eps(z)-(\solu_\eps)_{\R/\Z}| = \frac{(1-\rho(x,y))}{\rho(x,y)} + O(\eps) \geq 1 - O(\eps).
\]
Thus we have for any $x,y$ not antipodal.
\[
 1 - O(\eps) \leq \frac{d_{\solu_\eps}(x,y)}{\rho(x,y)} \leq 1 + O(\eps).
\]
Moreover,
\[
 \sup_{\delta \in (0,\eps)} \left |\frac{\frac{d_{\solu_\eps}(x,y)}{\rho(x,y)} - \frac{d_{\solu_\delta}(x,y)}{\rho(x,y)}}{\delta-\eps}  \right | = O(1).
\]
On the other hand, pointwise almost everywhere,
\[
 \frac{d}{d\eps} \Big |_{\eps = 0}\frac{d_{\solu_\eps}(x,y)}{\rho(x,y)} =  \frac{d}{d\eps} \Big |_{\eps = 0} \migo{x}{y} |\solu_\eps(z)-(\solu_\eps)_{\R/\Z}|
\]
and so by the Lebesgue convergence theorem we conclude
\[
 \frac{d}{d\eps} \Big|_{\eps = 0}\mathcal{E}^{\alpha,p}(\solu_\eps) = \frac{d}{d\eps} \Big|_{\eps = 0}\tilde{\mathcal{E}}^{\alpha,p}(\solu_\eps).
\]
With \eqref{eq:OtE} we conclude 
\[
 \frac{d}{d\eps} \Big|_{\eps = 0}\mathcal{E}^{\alpha,p}(\solu_\eps) = 0.
\]
Thus if $\sol$ is an arclength-parametrized critical knot of $\mathcal{O}^{\alpha,p}$, then $c^{-1} \sol'$ is a critical map of $\mathcal{E}^{\alpha,p}$ in the class of maps $v: \R/\Z \to \S^2$.
\end{proof}

\begin{remark}
We found the relation between $\mathcal{E}^{\alpha,p}$ and $\mathcal{O}^{\alpha,p}$ quite intriguing. 

For example: to us it did not seem obious that (2) $\Rightarrow$ (1) in Theorem~\ref{th:criticalpointchar}. By an argument due to He \cite{He2000} any $\mathcal{O}^{\alpha,p}$-variation of $\sol$ (constant-speed parmetrized) into the direction of $\solu=\sol'$ is trivial even if $\sol$ is not a critical knot. Indeed, this is a consequence of the parametrization invariance of $\mathcal{O}^{\alpha,p}$. 
Moroever, $\mathcal{O}^{\alpha,p}$-variations of $\sol$ in direction $\solu \wedge \solu'$ essentially correspond to $\mathcal{E}^{\alpha,p}$-variations of $\solu$ in direction of $T_\solu \S^2$, and thus vanish if $\solu$ is a critical map for $\mathcal{E}^{\alpha,p}$.
However, $\mathcal{O}^{\alpha,p}$-variations of $\sol$ in the direction of $\solu' = \sol''$ seem to correspond neither to reparametrizations of $\sol$ nor to tangential variations of $\mathcal{E}^{\alpha,p}$. However, as our arguments shows, $\mathcal{O}^{\alpha,p}$-criticality with respect to this class of variations is not necessary to obtain the regularity theory for knots -- so in principle one could weaken theorem~\ref{th:regularity} to critical knots with variations in fewer directions.

It also seems not fully clear to us what geometrical implication it is for a map $\solu: \R /\Z \to \S^2$ to have finite energy $\mathcal{E}$, in particular with respect to the (possibly not closed!) corresponding curve $\sol(x) := \int_0^x \solu(z)\, dz$. (e.g. it seems not obvious that $\sol$ is injective).
\end{remark}
