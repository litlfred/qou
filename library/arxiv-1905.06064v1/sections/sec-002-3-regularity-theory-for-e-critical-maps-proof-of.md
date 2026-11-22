---
doc_id: arxiv-1905.06064v1
doc_title: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS"
section_id: sec-002-3-regularity-theory-for-e-critical-maps-proof-of
section_title: "Regularity theory for E-critical maps: Proof of Theorem I"
section_number: 3
pages: 10-17
source_pdf: 1905.06064v1.pdf
source_sha256: 3ffe25c8ee62779d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.977
doc_brief: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS — We develop a regularity theory for extremal knots of scale invariant knot ener- gies deﬁned by J. O’hara in 1991."
---
In view of Theorem~\ref{th:criticalpointchar} the claim of Theorem~\ref{th:regularity} is a consequence of the following theorem.
\begin{theorem}\label{th:eregularity}
For $\alpha p = 4$, $p \geq 2$ consider $\mathcal{E}^{\alpha,p}$ from \eqref{eq:E}.

Let $\solu$ is a critical map for $\mathcal{E}^{\alpha,p}$ in the class of maps $\solv: \R/\Z \to \S^2$ with finite energy $\mathcal{E}^{\alpha,p}$, that is for any $\varphi \in C^\infty(\R/\Z,\R^3)$ we have
 \[
  \frac{d}{d\eps} \Big |_{\eps = 0} \mathcal{E}^{\alpha,p}\brac{\frac{u+\eps \varphi}{|\solu+\eps \varphi|}} = 0.
 \]
Then $\solu \in C^{\sigma}$ for some $\sigma > 0$.
\end{theorem}
We prove this theorem by extending the argument in \cite{SchikorraCPDE14} where $W^{\beta,p}$-harmonic maps into spheres were considered. See also \cite{MS18} for a different proof. 

\begin{remark}
It is a natural question to ask whether it is possible to extend He's argument, \cite{He2000} see also \cite{BRS16}, which shows smoothness of critical knots of the M\"obius energy that have an initial $C^{1,\sigma}$-regularity. But this argument depends heavily on the $L^2$-type of the energy. From the theory of critical harmonic map-type equations one expects that once $C^{1,\sigma}$-regularity is obtained as in Theorem~\ref{th:regularity} the best possible regularity corresponds to the best possible regularity of solutions to the homogeneous pde of the leading order operator (which in the $L^2$-case is the linear fractional Laplacian $\laps{\beta}$, and thus smoothness is to be expected). In our $L^p$-energy setting the corresponding equation involves however the fractional $p$-Laplace equation for which maximal regularity is unknown. The best current results for that operator has been obtained by Brasco and Lindgren, see \cite{BL15,BLS18}. Regarding convergence, observe that there are suitable stability results available for the fractional $p$-Laplacian \cite{SireKuusiMingioneSelfImproving,S16,ABES19} which seem to carry over to our situation.
\end{remark}


\subsection{Euler-Lagrange equations of \texorpdfstring{$\mathcal{E}^{\alpha,p}$}{Eap}}
To compute the Euler-Lagrange equations of $\mathcal{E}^{\alpha,p}$ we introduce
\[
 \mathcal{Q}(\solu,\varphi) := 2\int_{\R/\Z}\int_{\R/\Z} G'(\dmv{\solu}{\solu}(x,y))\ \dmv{\solu}{\varphi}(x,y)\ \frac{dx\ dy}{\rho(x,y)^{\alpha p /2}},
\]
and
\[
 \mathcal{R}_1(\solu,\varphi) = \int_{\R/\Z}\int_{\R/\Z} H(\dmv{\solu}{\solu}(x,y))\ \migo{x}{y} \solu\cdot (\varphi)_{\R/\Z} \frac{dx\ dy}{\rho(x,y)^{\alpha p /2}}.
\]
with
\[
 H(a) = \frac{\alpha p}{2}\brac{\brac{1- \frac{1}{2} a}^{-\frac{\alpha}{2}}   -1}^{\frac{p-2}{2}} \brac{\brac{1- \frac{1}{2} a}^{-\frac{\alpha+2}{2}}   -1}.
\]

Finally we set 
\[
 \mathcal{R}_2(\solu,\varphi) = \int_{\R/\Z}\int_{\R/\Z} G(\dmv{\solu}{\solu}(x,y)) \brac{\solu(x)+\solu(y) } \cdot (\varphi)_{\R/\Z} \frac{dx\ dy}{\rho(x,y)^{\alpha p /2}}.
\]
Note that in view of Lemma~\ref{la:Gpest}.
\begin{equation}\label{eq:HGest}
H(a), G(a) \aeq a^{\frac{p}{2}}\quad \mbox{for $0 \leq a \leq \lambda < 2$}
\end{equation}



Formally the Euler-Lagrange equations of $\mathcal{E}^{\alpha,p}$ in the class of maps from $\R/\Z$ into $\S^2$ are then 
\begin{equation}\label{eq:formalEL}
 \mathcal{Q}(\solu,\cdot) + \mathcal{R}_1(\solu,\cdot) - \mathcal{R}_2(\solu,\cdot)\perp T_{\solu} \S^2,
\end{equation}

\begin{remark}
We shall see that $\mathcal{R}_i(\solu,\cdot)$ are lower order terms which belong to $(L^1)^\ast$, see Proposition~\ref{pr:loterms}.
Thus, one could interpret \eqref{eq:formalEL} as a fractional, nonlinear version of the harmonic map equation
\[
 \lap \solu \perp T_{\solu} \S^2
\]
up to a lower-order term $\mathcal{R}_i(\solu,\cdot)$.
\end{remark}

More precisely we have the following
\begin{lemma}[Euler-Lagrange equations]\label{la:EL}
Let $\solu$ be a critical point of $\mathcal{E}$ in the class of maps $v: \R/\Z \to \S^2$ and assume $\int_{\R/\Z} \solu = 0$ as well as \eqref{eq:ubilipschitz}. Then 
for any testfunction $\varphi \in W^{\frac{1}{p},p}(\R/\Z, \R^3)$, which is also tangential, $\varphi \in T_{\solu} \S^2$,
\[
 \delta \mathcal{E}^{\alpha,p}(\solu,\varphi) = \mathcal{Q}(\solu,\varphi) + \mathcal{R}_1(\solu,\varphi) - \mathcal{R}_2(\solu,\varphi).
\]
\end{lemma}


\begin{proof}
Of course this only holds almost everywhere, namely whenever $x,y$ are not antipodal. With a cutoff argument we can make the following computations rigorous.

Recall that $G(a) = F(a,1,1)$ where
\[
 F(a,b,c) := \brac{\brac{b- \frac{1}{2} a}^{-\frac{\alpha}{2}}   -c^{-\alpha}}^{\frac{p}{2}}.
\]
Set $\solu_\eps := \solu + \eps \varphi$. We need to compute 
\[
\left. \frac{d}{d\eps} \right |_{\eps = 0} \int_{\R/\Z}\int_{\R/\Z} F\brac{a(\eps), b(\eps) , c(\eps)}\  d(\eps)\, e(\eps) \frac{dx\ dy}{\rho(x,y)^{\frac{\alpha p}{2}}}.
 \]
Here, we set
\[
\begin{split}
 a(\eps) &:= \dmv{\solu_\eps}{\solu_\eps}(x,y)\\
 b(\eps) &:= \migo{x}{y} |\solu_\eps-(\solu_\eps)_{\R/\Z}|^2\\
 c(\eps) &:= \migo{x}{y} |\solu_\eps-(\solu_\eps)_{\R/\Z}|\\
 d(\eps) &:= |\solu_\eps(x)- (\solu_\eps)_{\R/\Z}|\\
e(\eps) &:= |\solu_\eps(y)- (\solu_\eps)_{\R/\Z}|.
 \end{split}
\]
We first observe that $b(0) = c(0) = d(0) = e(0) = 1$ since $(\solu)_{\R/\Z} = 0$ and $|\solu| \equiv 1$. We find,
\[
 a(0) = \dmv{\solu}{\solu}(x,y), \quad a'(0) = 2\dmv{\solu}{\varphi}(x,y)
\]
Next, since $\varphi \cdot \solu \equiv 0$ and $(\solu)_{\R/\Z} = 0$,
\begin{equation}\label{eq:bp2cpeq}
 b'(0) = 2 c'(0) = -2 \migo{x}{y} \solu \cdot (\varphi)_{\R/\Z}
\end{equation}

Also
\[
d'(0) = -\solu(x) \cdot  (\varphi)_{\R/\Z}, \quad e'(0) = -\solu(y)\cdot (\varphi)_{\R/\Z}
\]

Thus, we find by product rule
 \[
\begin{split}
 & \left. \frac{d}{d\eps} \right |_{\eps = 0} \int_{\R/\Z}\int_{\R/\Z} F\brac{a(\eps), b(\eps) , c(\eps)}\  d(\eps)\, e(\eps) \frac{dx\ dy}{\rho(x,y)^{\frac{\alpha p}{2}}}\\
 =& 2\int_{\R/\Z}\int_{\R/\Z} G'(\dmv{\solu}{\solu}(x,y))\ \dmv{\solu}{\varphi}(x,y)\  \frac{dx\ dy}{\rho(x,y)^{\frac{\alpha p}{2}}}\\
  &+\int_{\R/\Z}\int_{\R/\Z} \left.\frac{d}{d\eps} \right |_{\eps = 0} F\brac{\dmv{\solu}{\solu}(x,y), b(\eps) , c(\eps)}  \frac{dx\ dy}{\rho(x,y)^{\frac{\alpha p}{2}}}\\
  &-\int_{\R/\Z}\int_{\R/\Z} G\brac{\dmv{\solu}{\solu}(x,y)}\ \brac{\solu(x)+\solu(y)}\cdot (\varphi)_{\R/\Z}  \frac{dx\ dy}{\rho(x,y)^{\frac{\alpha p}{2}}}\\
  =&\mathcal{Q}(\solu,\varphi) + \mathcal{R}_1(\solu,\varphi) - \mathcal{R}_2(\solu,\varphi).
\end{split}
 \]
To find the form of $\mathcal{R}_1$ we finally observe that with \eqref{eq:bp2cpeq},
\[
\begin{split}
 &\frac{d}{d\eps}\big|_{\eps =0} F(a(0),b(\eps),c(\eps)) \\
 =& -\frac{\alpha p}{2}\brac{\brac{1- \frac{1}{2} a(0)}^{-\frac{\alpha}{2}}   -1}^{\frac{p-2}{2}} \brac{\brac{1- \frac{1}{2} a(0)}^{-\frac{\alpha+2}{2}}   -1}\, c'(0)\\
 =& H(a(0)) \migo{x}{y} \solu\cdot (\varphi)_{\R/\Z}.
\end{split}
 \]
 \end{proof}

From \eqref{eq:HGest} we readily obtain 
\begin{proposition}\label{pr:loterms}
For $\solu$ satisfying \eqref{eq:ubilipschitz} we have for $i =1,2$.
\[
 |\mathcal{R}_i(\solu,\varphi)| \aleq C(\lambda)\ \|\solu\|_{L^\infty}\ \llbracket \solu \rrbracket_{W^{\beta,p}(\R/\Z)}^p\, \|\varphi\|_{L^1},
\]
\end{proposition}
Observe that by Lemma~\ref{la:lambda} we have $\lambda=\lambda(u)$ is bounded away from $2$, if $\solu=c^{-1} \sol'$ where $\sol$ has finite O'hara energy.


\subsection{Regularity theory: Left-hand side estimates}
Recall that
\[
 \mathcal{Q}(\solu,\varphi) := 2\int_{\R/\Z}\int_{\R/\Z} G'(\dmv{\solu}{\solu}(x,y))\ \dmv{\solu}{\varphi}(x,y)\ \frac{dx\ dy}{\rho(x,y)^{\alpha p /2}},
\]
where
\[
 G(s) := \brac{\brac{1- \frac{1}{2} s}^{-\frac{\alpha}{2}}  -1}^{\frac{p}{2}},
\]
For some interval $\iv$ we denote the version of $\mathcal{Q}$ restricted to $iv$ as $\mathcal{Q}_\iv$, that is
\[
 \mathcal{Q}_\iv(\solu,\varphi) := 2\int_{\iv} \int_{\iv} G'(\dmv{\solu}{\solu}(x,y))\ \dmv{\solu}{\varphi}(x,y)\ \frac{dx\ dy}{\rho(x,y)^{\alpha p /2}},
\]
and as in \cite{SchikorraCPDE14} define the potential $\Gamma_{\beta,\iv}u$ as 
\begin{equation}\label{eq:defGammabetaS}
 \Gamma_{\beta,\iv}\solu(z) := \mathcal{Q}_{\iv}(\solu,|z-\cdot|^{\beta-1}).
\end{equation}
The reason for taking such a potential is that $|z-\dot|^{\beta-1}$ is the kernel of the Riesz potential $\lapms{\beta}$,
\[
 \lapms{\beta} f(x) = \int_{\R} |z-x|^{\beta-1}\, f(z)\, dz.
\]
The Riesz potential of order $\beta$, $\lapms{\beta}$, has as an inverse the fractional Laplacian of order $\beta$, $\laps{\beta}$:
\[
 \lapms{\beta} \laps{\beta} f  = \laps{\beta} \lapms{\beta} f = f \quad \mbox{for $f \in C_c^\infty(\R)$}.
\]
The fractional Laplacian $\laps{\beta}$ is an an elliptic operator of differential order $\beta$ which can be described in different ways. For $\beta \in (0,1)$, it can be represented as an integro-differential operator
\[
 \laps{\beta} f(x) = c \int_{\R} \frac{f(y)-f(x)}{|x-y|^{1+\beta}}\, dy,
\]
or its Fourier symbol is $c |\xi|^\beta$,
\[
 \mathcal{F}\brac{\laps{\beta} f}(\xi)=c |\xi|^\beta\, \mathcal{F}(f)(\xi).
\]
The kernel $|z|^{\beta-1}$ is the fundamental solution of the operator $\laps{\beta}$ (just as $|z|^{2-n}$ is the fundamental solution of $-\Delta = \laps{2}$ in dimension $n\geq 3$), which means
\[
 \laps{\beta} \brac{|z-x|^{\beta-1}} = \delta_{x,z}.
\]
That is,
\[
 \mathcal{Q}_\iv(\solu,\cdot) = \laps{\beta} \Gamma_{\beta,\iv}\solu.
\]
or, by an integration by parts,
\[
 \mathcal{Q}_\iv(\solu,\varphi) = c\int_{\R} \Gamma_{\beta,\iv}\solu(z)\ \laps{\beta} \varphi.
\]
From now on we will assume that $\iv$ is a small interval inside $[0,1]$ and that $\solu$ is extended to $\R \backslash [-1,2]$ as an $W^{\frac{1}{p},p}$-map.

\begin{proposition}[Left-hand side estimate]\label{pr:lhsest}
Let $\iv_r$ be an interval $(x_0-r,x_0+r)$, $r \in (0,\frac{1}{2})$. If $\solu: \R/\Z \to \S^2$ satisfies \eqref{eq:ubilipschitz} then for any $\eps > 0$,
\[
\begin{split}
[\solu]_{W^{\frac{1}{p},p}(\iv_r)}^p \aleq & [\solu]_{W^{\frac{1}{p},p}(\iv_{2^Lr})} \|\chi_{\iv_{2^K r}} \Gamma_{\beta,\iv_{2^L r}} \solu\|_{L^{\frac{1}{1-\beta}}}  + \eps\, [\solu]_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p} + C_\eps\, \brac{[\solu]_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p} - [\solu]_{W^{\frac{1}{p},p}(\iv_{r})}^{p}}
\end{split}
\]
for any $L, K \in \mathbb{N}$ large enough.
\end{proposition}
\begin{proof}
In view of Proposition~\ref{pr:normalunnormalWsp}, it suffices to prove the estimate for $\llbracket \solu \rrbracket_{W^{\frac{1}{p},p}}$. Recall \eqref{eq:bracketdef} and
\[
 \llbracket \solu \rrbracket_{W^{\frac{1}{p},p}(\iv_r)}^{p} = \int_{\iv_r} \int_{\iv_r} \frac{(\dmv{\solu}{\solu}(x,y))^{\frac{p}{2}}}{\rho(x,y)^{2}}\ dx\ dy,
\]
with Lemma~\ref{la:Gpest} (using the condition \eqref{eq:ubilipschitz}),
\[
 \aeq \int_{\iv_r} \int_{\iv_r} G'(\dmv{\solu}{\solu}(x,y))\ \dmv{\solu}{\solu}(x,y) \frac{dx\ dy}{\rho(x,y)^{\frac{\alpha p}{2}}}.
\]
Let $\eta \in C_c^\infty(\iv_{2r})$, $\eta \equiv 1$ on $\iv_{r}$, with $|\nabla^k \eta| \leq C(k) r^{-k}$. Set $(\solu)_{\iv_{2r}} = (2r)^{-1} \int_{\iv_{2r}} \solu$. 
\[
 \psi(x) := \eta(x) (\solu(x)-(\solu)_{\iv_{2r}}),
\]
Observe that for $x,y \in \iv_r$,
\[
 \dmv{\solu}{\solu}(x,y) = \dmv{\psi}{\psi}(x,y).
\]
Thus, for any $L \geq 0$,
\[
  \llbracket \solu \rrbracket_{W^{\frac{1}{p},p}(\iv_r)}^{p} \aleq \int_{\iv_{2^L r}} \int_{\iv_{2^L r}} G'(\dmv{\solu}{\solu}(x,y))\ \dmv{\psi}{\psi}(x,y)\frac{ dx\ dy}{\rho(x,y)^{\frac{\alpha p}{2}}}.
\]
Now we write
\begin{align*}
 \psi(s) - \psi(t) =&(\solu(s)-\solu(t)) - (1-\eta(s)) (\solu(s)-\solu(t))\\
 & + (\eta(s)-\eta(t)) (\solu(t)-(\solu)_{\iv_{2r}}).
\end{align*}
and thus
\[
     \llbracket \solu \rrbracket_{W^{\frac{1}{p},p}(\iv_r)}^{p} \aleq I - II + III
   \]
where
  \[
  I:= \int_{\iv_{2^L r}} \int_{\iv_{2^L r}} G'(\dmv{\solu}{\solu}(x,y)) \dmv{\solu}{\psi}(x,y)\ \frac{dx\ dy}{\rho(x,y)^{\frac{\alpha p}{2}}} 
  \]
  \[
  II:=-\int_{\iv_{2^L r}} \int_{\iv_{2^L r}} G'(\dmv{\solu}{\solu}(x,y)) \frac{\rho(x,y)^{-2} \int_x^y\int_x^y \left \langle (1-\eta(s)) (\solu(s)-\solu(t)) ,\psi(s) - \psi(t) \right \rangle \ ds\ dt}{{\rho(x,y)^{\frac{\alpha p}{2}}}}\ dx\ dy
  \]
   \[III:=\int_{\iv_{2^L r}} \int_{\iv_{2^L r}} G'(\dmv{\solu}{\solu}(x,y)) \frac{\rho(x,y)^{-2} \int_x^y\int_x^y\left \langle \brac{\eta(s)-\eta(t)} \brac{\solu(t)-(\solu)_{\iv_{2r}}},\psi(s) - \psi(t) \right \rangle \ ds\ dt}{{\rho(x,y)^{\frac{\alpha p}{2}}}}\ dx\ dy\\
\]
As for $II$, we have by H\"older $\frac{p-2}{p} + \frac{2}{p} = 1$, and Jensen inequality and using Fubini/Lemma~\ref{la:Ast}-arguments 
\[
 |II| \aleq \llbracket \solu \rrbracket_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p-2}\ [\psi]_{W^{\frac{1}{p},p}(\iv_{2^L r})}\ \brac{\int_{\iv_{2^L r}} \int_{\iv_{2^L r}} (1-\eta(s))^p \frac{|\solu(t)-\solu(s)|^p}{|s-t|^{2}}\ ds\ dt}^{\frac{1}{p}}
\]
We conclude as in \cite[Proof of Lemma 3.2., Proposition D.1, Proposition D.2]{SchikorraCPDE14}. The same way we estimate $III$.
Also $I$ can be estimated as in  \cite[Proof of Lemma 3.2.]{SchikorraCPDE14}.
\end{proof}


\subsection{Estimates of the right-hand side}
Since $|\solu| = 1$ a.e., we have the estimate
\begin{equation}\label{eq:chisplit}
\|\chi_{\iv_{2^K r}} \Gamma_{\beta,\iv_{2^L r}}\solu\|_{L^{\frac{1}{1-\beta}}} \aleq  \|\chi_{\iv_{2^K r}} \solu \cdot \Gamma_{\beta,\iv_{2^L r}}\solu\|_{L^{\frac{1}{1-\beta}}} + \|\chi_{\iv_{2^K r}} \solu\wedge \Gamma_{\beta,\iv_{2^L r}}\solu\|_{L^{\frac{1}{1-\beta}}},
\end{equation}
where $\solu\wedge$ denotes the $\R^3$-cross product with $\solu$.

\begin{lemma}\label{la:ucdotGamma}
For $\beta<\frac{1}{p}$ large enough,
\[
 \|\solu \cdot \Gamma_{\beta,\iv_{2^L r}}\solu\|_{L^{\frac{1}{1-\beta}}} \aleq [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{2L}r})}^{p} + \sum_{k=1}^\infty 2^{-\sigma (L+k)}[\solu]_{W^{\frac{1}{p},p}(\iv_{2^{2L+k}r})}^{p}.
\]
\end{lemma}
\begin{proof}
The fact that $|\solu| = 1$, implies
\[
\begin{split}
 &\solu(z)\cdot \int_x^y \int_x^y (\solu(s)-\solu(t)) (|s-z|^{\beta-1} - |t-z|^{\beta-1})\ ds\ dt\\
 =&-\frac{1}{2}\int_x^y \int_x^y (\solu(s)-\solu(t))(\solu(s)+\solu(t)-2\solu(z)) (|s-z|^{\beta-1} - |t-z|^{\beta-1})\ ds\ dt.
\end{split}
 \]
Thus
\[
\begin{split}
 &|\solu(z) \cdot \Gamma_{\beta,\iv_{2^L r}}\solu(z)|\\
 \aleq &\int_{\iv_{2^L r}} \int_{\iv_{2^L r}} \frac{\dmv{\solu}{\solu}(x,y)^{\frac{p-2}{2}} \brac{\rho(x,y)^{-2} \int_x^y \int_x^y \chi_S(s,t) |\solu(s)-\solu||\solu(s)+\solu-2u(z)| ||s-z|^{\beta-1} - |t-z|^{\beta-1}|\ ds\ dt}}{\rho(x,y)^{2}}\ dx\ dy\\
\aleq &\llbracket \solu \rrbracket_{W^{\frac{1}{p},p}(S)}^{p-2} \brac{\int_{\iv_{2^L r}} \int_{\iv_{2^L r}} \frac{\brac{|\solu(s)-\solu||\solu(s)+\solu-2u(z)| \left ||s-z|^{\beta-1} - |t-z|^{\beta-1} \right |}^{\frac{p}{2}}}{|s-t|^{2}}\ ds\ dt}^{\frac{2}{p}}.
\end{split}
 \]
The arguments in \cite[Lemma 6.5]{SchikorraCPDE14} then imply that if $\beta < \frac{1}{p}$ is large enough, the claim follows.
\end{proof}

\begin{lemma}\label{la:uwedgeGamma}
Let $\solu: \R/\Z \to \S^2$ solve the Euler-Lagrange equation from Lemma~\ref{la:EL}, then for any $K \in \N$ large enough,
\[
\begin{split}
  \|\chi_{\iv_{2^K r}} \solu \wedge \Gamma_{\beta,\iv_{2^{10K} r}} \solu\|_{L^{\frac{1}{1-\beta}}} \aleq& [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{20K} r})}^p + 2^{-\sigma K} [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{20K} r})}^{p-1}\\
  &+ [\solu]_{W^{\frac{1}{p},p}(\R)} \sum_{k=1}^\infty 2^{-\sigma(K+k)} [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{20K+k}r})}^{p-1} + (2^{2K} r)\ \llbracket \solu \rrbracket_{W^{\frac{1}{p},p}(\R/\Z))}.
\end{split}
  \]
\end{lemma}
\begin{proof}
We follow the strategy in \cite[Lemma 3.5]{SchikorraCPDE14}.

Firstly, by duality we find $g \in C_c^\infty(\iv_{2^K r})$ so that $\|g\|_{L^{\frac{1}{\beta}}} \leq 1$ and
\[
 \|\chi_{\iv_{2^K r}} \solu\wedge\Gamma_{\beta,\iv_{2^L r}}\solu\|_{L^{\frac{1}{1-\beta}}} \aleq \int_{\R} \solu(z) \wedge\Gamma_{\beta,\iv_{2^L r}}\solu(z)\ g(z)\ dz = I + \sum_{k=1}^\infty II_k,
\]
with
\[
 I = \int_{\R} \laps{\beta} (\eta_{\iv_{2^{2K}}} \lapms{\beta} g) \solu(z) \wedge \Gamma_{\beta,\iv_{2^L r}}\solu(z)\ \ dz
\]
\[
 II_k = \int_{\R} \laps{2(\frac{1}{p}-\beta)} \brac{\laps{\beta} \brac{\eta_{\iv_{2^{2K+k+1}}\backslash \iv_{2^{2K+k}}} \lapms{\beta} g} \solu(z)\wedge} \cdot \lapms{2(\frac{1}{p}-\beta)}\Gamma_{\beta,\iv_{2^L r}}\solu(z)\ \ dz
\]
for the usual choice of cutoff functions on segment and annuli.

First, we treat $II$. Observe that (for $\varphi := \laps{2(\frac{1}{p}-\beta)} \brac{\laps{\beta} \brac{\eta_{\iv_{2^{2K+k+1}}\backslash \iv_{2^{2K+k}}} \lapms{\beta} g} \solu(z)\wedge}$)
\[
\begin{split}
 &\int \varphi(z)\, \lapms{2(\frac{1}{p}-\beta)}\Gamma_{\beta,\iv_{2^L r}}\solu(z)\, dz \leq \int_{\iv_{2^L r}}\int_{\iv_{2^L r}} \frac{(\dmv{\solu}{\solu}(x,y))^{\frac{p-2}{2}}}{\rho(x,y)^2} \dmv{\solu}{\lapms{\frac{2}{p}-\beta} \varphi}(x,y)\\
 \aleq & \llbracket \solu \rrbracket_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p-1} [\lapms{\frac{2}{p}-\beta} \varphi ]_{W^{\frac{1}{p},p}(\R)}\\
 \aleq & \llbracket \solu \rrbracket_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p-1} \|\varphi \|_{L^{\frac{1}{\frac{2}{p}-\beta}}}.
\end{split}
 \]
In the last step we used Sobolev embedding and that $\beta < \frac{1}{p}$.

This and the estimates of the remaining term of $II$ (see \cite[Proof of Lemma 3.5]{SchikorraCPDE14}) imply the estimate for $II$.

As for $I$, we set (some other) $\varphi :=(\eta_{\iv_{2^{2K}}} \lapms{\beta} g)$, and have
\[
 \|\laps{\beta} \varphi \|_{L^{\frac{1}{\beta}}} \leq 1.
\]
Up to a three-commutator estimate which can be treated exactly as in \cite[Proof of Lemma 3.5]{SchikorraCPDE14}, we have to deal with
\[
 I_1 := \int \laps{\beta} (\varphi \solu \wedge)\ \Gamma_{\beta,\iv_{2^{10 K}r}} \solu,
\]
\[
 I_2 := \int \varphi \laps{\beta} (\solu \wedge) \ \Gamma_{\beta,\iv_{2^{10 K}r}} \solu,
\]
Regarding $I_1$, we have.
\[
\begin{split}
 I_1 =& \int_{\iv_{2^L r}}\int_{\iv_{2^L r}} G'(\dmv{\solu}{\solu}) \frac{\dmv{\solu}{(\varphi \solu \wedge)}(x,y)}{\rho(x,y)^{\frac{\alpha p}{2}}}\ dx\ dy\\
 =& \int_{\R/\Z}\int_{\R/\Z} G'(\dmv{\solu}{\solu}) \frac{\dmv{\solu}{(\varphi \solu \wedge)}(x,y)}{\rho(x,y)^{\frac{\alpha p}{2}}}\ dx\ dy\\
 &+ 2\int_{[0,1] \backslash \iv_{2^L r}}\int_{\iv_{2^L r}} G'(\dmv{\solu}{\solu}) \frac{\dmv{\solu}{(\varphi \solu \wedge)}(x,y)}{\rho(x,y)^{\frac{\alpha p}{2}}}\ dx\ dy\\
 &+ \int_{[0,1]\backslash \iv_{2^L r}}\int_{[0,1]\backslash \iv_{2^L r}} G'(\dmv{\solu}{\solu}) \frac{\dmv{\solu}{(\varphi \solu \wedge)}(x,y)}{\rho(x,y)^{\frac{\alpha p}{2}}}\ dx\ dy.
 \end{split}
\]
The first term is the Euler-Lagrange operator $\mathcal{Q}(\solu, \varphi \solu\wedge)$. With the Euler-Lagrange equation for $\mathcal{E}^{\alpha,p}$, (note that $\solu\wedge \varphi \in T_{\solu} \S^2$), Lemma~\ref{la:EL},
\[
  |\mathcal{Q}(\solu, \sol \wedge\varphi )| = |\mathcal{R}(\solu,\varphi)| \aleq \mathcal{E}^{\alpha,p}(\solu)\ \|\varphi \|_{L^1} \aleq (2^{2K} r)\ \mathcal{E}^{\alpha,p}(\solu).
\]
As for the second term of $I_1$,
\[
\int_{\iv_{2^L r}} \int_{\R/\Z \backslash \iv_{2^L r}} \brac{\dmv{\solu}{\solu}(x,y)}^{\frac{p}{2}-2} \dmv{\solu}{(\varphi\solu \wedge) }(x,y)\ \frac{dx\ dy}{\rho(x,y)^{\frac{\alpha p}{2}}}.
\]
can be estimated  with Lemma~\ref{la:disjointest1}.
As for the third term we observe that for large enough $L \ageq K$, for $x,y \in [0,1] \backslash \iv_{2^L r}$, either
\[
 \rho(x,y) \ageq 2^{K}r,
\]
or by the support of $\varphi$,
\[
 \dmv{\solu}{(\varphi\solu \wedge) }(x,y) = 0.
\]
Thus,
\[
 \int_{[0,1]\backslash \iv_{2^L r}}\int_{[0,1]\backslash \iv_{2^L r}} G'(\dmv{\solu}{\solu}) \frac{\dmv{\solu}{(\varphi \solu \wedge)}(x,y)}{\rho(x,y)^{\frac{\alpha p}{2}}}\ dx\ dy \aleq 2^{-\sigma K} [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{20K}r})}.
\]
This estimates $I_1$.

To estimate $I_2$, we use the definition of $\Gamma_{\beta,I}$, \eqref{eq:defGammabetaS}, and have
\[
 I_2 = \int_{\iv_{2^{10 K}r}}\int_{\iv_{2^{10 K}r}} G'(\dmv{\solu}{\solu}(x,y) )\ \dmv{\solu}{\lapms{\beta} (\varphi \laps{\beta} \solu\wedge)} \rangle\ \frac{dx\ dy}{\rho(x,y)^{\frac{\alpha p}{2}}}
\]
Now, as in \cite[(3.13)]{SchikorraCPDE14}, since $\solu\wedge \solu = 0$,
\[
\begin{split}
 \dmv{\solu}{(\lapms{\beta} (\varphi \laps{\beta} \solu \wedge)} = \rho(x,y)^{-2} \int_x^y \int_x^y (\solu(s)-\solu(t))\cdot \theta(s,t)\ ds\ dt,
 \end{split}
\]
where
\[
 \theta(s,t) = (\lapms{\beta} (\varphi \laps{\beta} \solu \wedge)(s) - \lapms{\beta} (\varphi \laps{\beta} \solu \wedge)(t) - \frac{1}{2} (\solu \wedge(s) - \solu \wedge(t))(\varphi(s)+\varphi(t))
\]
Now we can argue as in \cite[Lemma 6.6]{SchikorraCPDE14} to obtain the claim.

\end{proof}



\subsection{Proof of Theorem~\ref{th:eregularity}}
As usual for the regularity theory of harmonic maps, one needs to obtain a decay estimate of the localized energy (or the respective norm), from which the H\"older continuity of the solution follows from an iteration argument. The decay estimate is the following.
\begin{proposition}[Decay estimate]\label{pr:decay}
Let $\solu$ be a critical point of $\mathcal{E}^{\alpha,p}$ for $p \geq 2$, $\alpha p = 4$.

There exist $\eps > 0$ and $\tau < 1$ and $L_0 > 0$ such that whenever for $L \geq L_0$ and $[\solu]_{W^{\frac{1}{p},p}(\iv_{2^Lr})} < \eps$ then
\[
\begin{split}
[\solu]_{W^{\frac{1}{p},p}(\iv_r)}^p \aleq & \tau [\solu]_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p}

+ \sum_{k=1}^\infty 2^{-\sigma(L+k)} [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{20L+k}r})}^{p}
\end{split}
\]
\end{proposition}
\begin{proof}
From Proposition~\ref{pr:lhsest} we have for any $\eps > 0$, and all $L,K$ large enough
\[
\begin{split}
[\solu]_{W^{\frac{1}{p},p}(\iv_r)}^p \aleq & [\solu]_{W^{\frac{1}{p},p}(\iv_{2^Lr})} \|\chi_{\iv_{2^K r}} \Gamma_{\beta,\iv_{2^L r}} \solu\|_{L^{\frac{1}{1-\beta}}}  + \eps [\solu]_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p} + C_\eps \brac{[\solu]_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p} - [\solu]_{W^{\frac{1}{p},p}(\iv_{r})}^{p}}.
\end{split}
\]
From \eqref{eq:chisplit}
\[
\|\chi_{\iv_{2^K r}} \Gamma_{\beta,\iv_{2^L r}}\solu\|_{L^{\frac{1}{1-\beta}}} \aleq  \|\chi_{\iv_{2^K r}} \solu \cdot \Gamma_{\iv_{2^L r}}\solu\|_{L^{\frac{1}{1-\beta}}} + \|\chi_{\iv_{2^K r}} \solu \wedge \Gamma_{\beta,\iv_{2^L r}}\solu\|_{L^{\frac{1}{1-\beta}}}.
\]
For Lemma~\ref{la:ucdotGamma} for $\beta<\frac{1}{p}$ large enough,
\[
 \|\solu \cdot \Gamma_{\beta,\iv_{2^L r}}\solu\|_{L^{\frac{1}{1-\beta}}} \aleq [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{2L}r})}^{p} + \sum_{k=1}^\infty 2^{-\sigma (L+l)}[\solu]_{W^{\frac{1}{p},p}(\iv_{2^{2L+\ell}r})}^{p}.
\]
From Lemma~\ref{la:uwedgeGamma}, since the energy is finite,
\[
  \|\chi_{\iv_{2^K r}} \solu \wedge \Gamma_{\beta,\iv_{2^{10K} r}} \solu\|_{L^{\frac{1}{1-\beta}}} \aleq [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{20K} r})}^p + 2^{-\sigma K} [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{20K} r})}^{p-1} + \sum_{k=1}^\infty 2^{-\sigma(K+k)} [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{20K+k}r})}^{p-1} + (2^{2K} r).
\]
Plugging this together, we obtain for all $L$ large enough, 
\[
\begin{split}
[\solu]_{W^{\frac{1}{p},p}(\iv_r)}^p \aleq & 
\brac{[\solu]_{W^{\frac{1}{p},p}(\iv_{2^Lr})} + \eps + 2^{-\sigma L}} [\solu]_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p}

+ C_\eps \brac{[\solu]_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p} - [\solu]_{W^{\frac{1}{p},p}(\iv_{r})}^{p}}
+ \sum_{k=1}^\infty 2^{-\sigma(L+k)} [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{20L+k}r})}^{p}
\end{split}
\]
Using the hole-filling technique, adding $C_\eps [\solu]_{W^{\frac{1}{p},p}(\iv_{r})}^{p}$ to both sides, for small enough $\eps$ and large enough $L$, whenever $[\solu]_{W^{\frac{1}{p},p}(\iv_{2^Lr})} < \eps$, for some $\tau < 1$
\[
\begin{split}
[\solu]_{W^{\frac{1}{p},p}(\iv_r)}^p \aleq & \tau [\solu]_{W^{\frac{1}{p},p}(\iv_{2^L r})}^{p}

+ \sum_{k=1}^\infty 2^{-\sigma(L+k)} [\solu]_{W^{\frac{1}{p},p}(\iv_{2^{20L+k}r})}^{p}
\end{split}
\]
\end{proof}


\begin{proof}[Proof of Theorem~\ref{th:eregularity}]
Iterating the estimate from Proposition~\ref{pr:decay} on small balls, cf. \cite[Lemma A.8]{BRS16}, we find $\sigma > 0$ such that
\[
\sup_{r > 0,x \in \R /\Z} r^{-\sigma}\, [\solu]_{W^{\frac{1}{p},p}(\iv_r(x))} \aleq C(\solu).
\]
From Sobolev embedding on Morrey spaces, \cite{Adams75} we obtain that $\solu \in C^{\tilde{\sigma}}$ for any $\tilde{\sigma} < \sigma$.
\end{proof}

\renewcommand{\a}{\ensuremath{\alpha}}
\renewcommand{\b}{\ensuremath{\beta}}
\newcommand{\br}[1]{\ensuremath{\left(#1\right)}}
\renewcommand{\d}{\ensuremath{\,d}}
\newcommand{\dg}{\ensuremath{\g'}}
\newcommand{\D}[1][\g]{{#1(x)-#1(y)}}
\newcommand{\E}[1][\a,4/\a]{\ensuremath{\mathcal{O}^{#1}}}
\newcommand{\g}{\sol}
\newcommand{\sett}[2]{\ensuremath{\left\{#1\,\middle|\,#2\right\}}}
\newcommand{\sq}[1]{\ensuremath{\left[#1\right]}}
\newcommand{\rzd}{(\R/\Z,\R^{d})}
