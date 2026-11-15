---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-015-regularity-of-critical-points
section_title: "Regularity of critical points"
section_number: null
pages: 37-38
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.659
latex_coverage_ratio: 0.988
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
\label{sec:Smoothness}
This section is devoted to the proof of \cref{thm:smoothness}, which states that critical points of linear combinations 
\[\TL_{\nu\theta}\ceq\nu\BendingEnergy+\theta\TPp, \quad \nu,\theta\ge 0,\,\,\nu+\theta>0,\]
of bending and tangent-point energies are smooth, including the cases where only one of those energies appears. The case $ \nu>0,\theta=0 $ will be covered by \Cref{thm:elastic-smoothness-new}. For mixed energies, $ \nu,\theta>0 $, the result follows from \Cref{thm:smoothness-T-critical-new}. The pure tangent-point energy is treated in \Cref{thm:smoothness-TP-new}, which covers the case $ \nu=0,\theta>0 $, and thus completes the proof of \Cref{thm:smoothness}. 

Before proceeding to these three scenarios, let us make some general comments. If $ \theta=0 $ we work on the submanifold 
\[\NL^2\subset\OL\ceq H^{2}_{\reg}(\R/\Z,\R^n)\subset H^{2}(\R/\Z,\R^n)\]
of immersed arclength parametrized curves. In all other cases ($ \theta>0 $) we restrict to the submanifolds 
\[\AL^{1+s}\subset \OL\ceq H^{1+s}_{\injreg}(\R/\Z,\R^n)\subset H^{1+s}(\R/\Z,\R^n)\]
of arclength parametrized knots, where $ s=1 $ whenever $ \nu>0 $, and $ s=s(p)=(p-3)/2 $ for $ p\in (4,5) $ if $ \nu=0 $ and $ \theta>0 $. 
For a fixed point $ \bz\in \R^n $ and $ \ML\in \{\NL^{1+s},\AL^{1+s}\} $ we may also consider the submanifolds $ \ML_{\bz}\ceq\{\gamma\in \ML: \gamma(0)=\bz\} $ without changing the regularity statements. Indeed, \cref{cor:critical-points_wo_fixed_point} implies that every $ \EL|_{\ML_{\bz}}  $-critical point for any $ \EL\in \{\TL_{\nu\theta}:\nu,\theta\ge0,\nu+\theta>0\} $, is also $ \EL|_{\ML} $-critical, because $ \EL $ is invariant under translations. 
Finally, recall from \cref{rem:explicit-lagrange-multiplier}, that for arclength-parametrized $ \EL $-critical curves $ \gamma\in\ML $ we have the Euler-Lagrange equation $ \D\EL_{\gamma}-\Lambda\D\Sigma_{\gamma}=0 $ with the explicit Lagrange multiplier 
\[\Lambda=\D\EL_{\gamma}Y_{\gamma}\in \left( H^{s}( \R/\Z) \right)^*\equiv H^{-s}(\R/\Z).\]
Consequently, by \cref{eq:log-strain-differential}, we are going to investigate the criticality equation 
\begin{equation}    \label{eq:CriticalityWithoutLambda}
\begin{aligned}
    \D\EL_{\gamma}h=\D\EL_{\gamma}Y_{\gamma}\left\langle \gamma',h' \right\rangle\quad \Foa h\in H^{1+s}(\R/\Z,\R^n).
\end{aligned}
\end{equation}

\subsection{Bending energy}\label{sec:RegularityBending}

\begin{theorem}
\label{thm:elastic-smoothness-new}
Fix a point $\bz\in\R^n$ and let $\UL$ be an open subset of $\NL^2$ or $\NL^2_\bz$.
Then every critical point of $\BendingEnergy$ on $\UL$ is of class $C^\infty(\Circle,\AmbSpace)$.
\end{theorem}
\begin{proof}\Cref{cor:critical-points_wo_fixed_point} allows us to assume that $ \gamma $ is $ \BendingEnergy\vert_{\UL} $-critical for $ \UL\subset \NL^2$. 
    We exploit that $\gamma$ is parametrized by arclength and the formulas \cref{eq:Diff_elastic_formula}
    for $\D(\BendingEnergy)_\gamma$.
    Substituting this into \cref{eq:CriticalityWithoutLambda} for $ \EL\ceq\BendingEnergy $, we get the following equation
    \begin{equation*}
        \D(\BendingEnergy)_\gamma h
        =
        Q(\gamma,h)
        +
        R_\gamma h
        =
        F_\gamma  h
        \quad 
        \text{for all $h \in H^2(\Circle,\AmbSpace)$}
        ,
    \end{equation*}
    \\[-5ex]
    where
    \begin{equation*}
        Q(\gamma,h)
        \ceq 
        \textstyle \int_{\Circle} \inner{\gamma'',h''} \dd u
        ,
        \;\;
        
        R_\gamma  h
        \ceq
        \textstyle
        - \tfrac{3}{2} \int_{\Circle} \abs{\gamma''}^2 \inner{\gamma',h'} \dd u
        ,
        \;\;
        F_\gamma  h       
        \ceq 
        D(\BendingEnergy)_\gamma \, Y_\gamma \inner{\gamma',h'}
        .
    \end{equation*}
    This is the weak formulation of the elliptic equation 
    \begin{equation}
        \Delta^2 \gamma = F_\gamma - R_\gamma.
        \label{eq:Bending:EllipticEquation}
    \end{equation}
    Let $\varepsilon >0$ and suppose that we know already that $\gamma \in H^t(\Circle,\AmbSpace)$ for some $t \geq 2$.
    Integration by parts (in the distributional sense) and \cref{cor:gamma''gamma''} reveal that 
    \begin{equation}\label{eq:95A_vdM}
    \begin{aligned}
        R_\gamma 
        = 
        \tfrac{3}{2}  \pars[\big]{ \inner{\gamma'',\gamma''} \, \gamma'}' \in H^{\sigma(t-2,\varepsilon)-1}(\Circle,\AmbSpace)\quad\Foa\varepsilon>0
        ,
    \end{aligned}
    \end{equation}
    where $\sigma(\cdot,\cdot)$ is the function defined in \cref{lem:DEbYisLowerOrderIIII}.
    Moreover, the second part of that lemma also shows that 
    \begin{equation}\label{eq:95B_vdM}
    \begin{aligned}
        F_\gamma \in H^{\sigma(t-2,\varepsilon)-1}(\Circle,\AmbSpace)\quad\Foa\varepsilon>0
        .
    \end{aligned}
    \end{equation}
    So, if $\gamma \in H^t(\Circle,\AmbSpace)$, then equation \cref{eq:Bending:EllipticEquation} implies 
    \[
        \Delta^2 \gamma \in 
        H^{\sigma(t-2,\varepsilon)-1}(\Circle,\AmbSpace).
    \]
    Now, elliptic regularity for the bi-Laplacian, see \cite[Theorem 6.33]{folland_1995}, implies
    \[
        \gamma \in 
        H^{4 + \sigma(t-2,\varepsilon)-1}(\Circle,\AmbSpace)
        \subset 
        H^{t+1/2 - \varepsilon}(\Circle,\AmbSpace), \quad\Foa\varepsilon>0.
    \]
    So, if we fix $0 < \varepsilon <1/2$, say $ \varepsilon=\frac{1}{4} $, then we get the same strict increase in regularity for each $t \geq 2$.
    Starting at $t = 2$ and iterating this, we obtain
    \[
        \gamma \in \bigcap_{t \geq 2} H^{t}(\Circle,\R^n) = C^\infty(\Circle,\R^n).
    \]
\end{proof}
 
\begin{corollary}[$ E_b $ critical curves]
    Let $ \bz\in \R^n $ and $ \ML\in\{\NL^2,\NL^2_{\bz}\} $.
    Any critical curve $ \gamma $ of the restricted bending energy $ E_b\big\vert_{\ML} $ is critical for $ E_b-\lambda\LL $ on the open subset $ H^2_{\mathrm{r}}\left( \R/\Z,\R^n \right)\subset H^2\left( \R/\Z,\R^n \right)$ for $ \lambda=-E_b(\gamma)\le-(2\pi)^2 $. 
\end{corollary}
\begin{proof}
    Since $ \BendingEnergy $ is parameter-invariant and positively $ (-1) $-homogeneous, we may apply \cref{thm:critical-points}, which shows that $ \gamma $ is critical for $ \BendingEnergy-\lambda\LL $ for $ \lambda=-\BendingEnergy(\gamma) $. Fenchel's theorem \cite[Theorem 3, p. 405]{CarmoDifferentialGeometryCurves2016}, on total curvature together with Hölder's inequality gives $ \BendingEnergy(\gamma)\ge (2\pi)^2 $.
\end{proof}
