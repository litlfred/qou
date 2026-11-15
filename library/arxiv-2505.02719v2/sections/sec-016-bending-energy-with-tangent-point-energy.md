---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais–Smale condition in geometric knot theory"
section_id: sec-016-bending-energy-with-tangent-point-energy
section_title: "Bending energy with tangent-point energy"
section_number: null
pages: 39-41
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
doc_brief: "On the Palais–Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy"
text_source: latex
latex_prose_ratio: 0.883
latex_coverage_ratio: 0.838
---
\label{sec:RegularityMixed}


\begin{theorem}\label{thm:smoothness-T-critical-new}
Let $\theta>0,p \in \intervaloo{4,5},\bz\in\R^n$, and let $\UL$ be an open subset of $\AL^2$ or $\AL^2_\bz$.
Then every critical point of $\MixedEnergy=\BendingEnergy+\theta\TPp$ on $\UL$ is of class $C^\infty(\Circle,\AmbSpace)$.
\end{theorem}
\begin{proof}As in the proof of \cref{thm:elastic-smoothness-new} we may focus on $ \MixedEnergy\vert_{\UL} $-critical knots $ \gamma $ for $ \UL\subset\AL^{2} $. 
    The criticality equation is a minor modification of \cref{eq:Bending:EllipticEquation}:
    \begin{equation}
        \Delta^2 \gamma = F_\gamma - R_\gamma - \theta \, \D(\TP^{(p,2)})_\gamma.
        \label{eq:Mixed:EllipticEquation}
    \end{equation}
    For $ t\ge 2>{(p-1)}/{2} $ and $ \gamma\in \AL^{t} $ \cite[Proposition 4.3]{blatt-reiter_2015a} implies $ R^{\TP}_{\gamma}\in H^{t-1-p/2-\varepsilon}(\R/\Z,\R^n) $ for all $ \varepsilon>0 $, where $ R^{\TP}_{\gamma} $ appears as a remainder term in \cref{eq:splitting-TP}.
    Combining this for $ \varepsilon\in(0,(p-4)/2] $ with the first part of \cref{lem:EllipticRegularityQTP} and \cref{eq:splitting-TP} leads to    
    \[
        \D(\TP^{(p,2)})_\gamma  \in H^{t-(p-1)}(\Circle,\AmbSpace).
    \]
    Together with \cref{eq:95A_vdM,eq:95B_vdM}, we obtain
    \[
        \Delta^2 \gamma \in H^{\sigma(t-2,\varepsilon)-1}(\Circle,\AmbSpace) \cap H^{t-(p-1)}(\Circle,\AmbSpace)
        \quad\Foa\varepsilon>0.
    \]
    By elliptic regularity, \cite[Theorem 6.33]{folland_1995}, we arrive at
    \[
        \gamma 
        \in
        H^{\sigma(t-2,\varepsilon)+3}(\Circle,\AmbSpace) \cap H^{t-(p-1)+4}(\Circle,\AmbSpace).
    \]
    Since $p-1 < 4$ and by choice of, say $ \varepsilon=\frac{1}{4} $ as in the proof of \cref{thm:elastic-smoothness-new},
    we gain the fixed amount $ \min\{4-(p-1),\frac{1}{4}\} >0$ in regularity for each $ t\ge2 $, and therefore conclude that $ \gamma $ is smooth.
\end{proof}

The previous result in combination with \cref{thm:critical-points} and \cref{cor:critical-points_wo_fixed_point} yields the following corollary.  
\begin{corollary}[Critical knots under length constraint]
    Let $ \bz\in \R^n $ and $ \ML\in\{\AL^2_\bz,\AL^2\} $.
    For any fixed $ \theta>0$ and $p\in(4,5) $ every critical knot $ \gamma $ of the restricted energy $ \TL\big\vert_{\ML} $ is critical for $ \TL-\lambda \, \LL $ on the open subset $ H^2_{\mathrm{ir}}\left( \R/\Z,\R^n \right)\subset H^2\left( \R/\Z,\R^n \right)$ for some $ \lambda\in \R $.     
\end{corollary}


\begin{remark}[Homogeneous total energies]
\label{rem:homogeneous-eneriges}
One could add a different power of the knot energy (depending on its scaling
behavior) to obtain a positively homogeneous total energy as was done
in \cite[(1.4)]{gilsbach-etal_2023}. Here, for example, one could consider
$\SL \ceq \BendingEnergy + \theta \, (\TP^{(p,2)}\circ\iota)^{4-p}$ as a positively $(-1)$-homogeneous
total energy, which implies by means of \Cref{thm:critical-points}
that $\lambda=-\SL(\g)\le -\BendingEnergy(\g)\le -(2\pi)^2.$ If
$\g$ is non-trivially knotted, one even has $\lambda< -(4\pi)^2$
due to the Far\'y-Milnor theorem \cite[Corollary 4.6]{milnor_1950}.
Very recently, the sharp lower bound 
\begin{equation}\label{eq:TPmin}
\begin{aligned}
    \TP_\textnormal{min} \ceq 
\pi^{p-3}\int_0^\pi \sin^{4-p}z\d z
\end{aligned}
\end{equation}
for $\TP^{(p,2)}$ has been established
in \cite{doehrer-dohmen_2025}, which leads to the improved upper bound
$-(2\pi)^2 - \theta \, \TP_\textnormal{min}^{1/(p-4)}$ on $\lambda$, or
even the strict upper bound $-(4\pi)^2 - \theta \, \TP_\textnormal{min}^{1/(p-4)}$,
if $\g$ is non-trivially knotted.
\end{remark}

\subsection{Tangent-point energy}\label{sec:RegularityTP}

\begin{theorem}\label{thm:smoothness-TP-new}
    Let $p\in (4,5)$, $s=s(p) = (p-3)/2$, and  $\bz\in\R^n$. 
    Let $\UL$ be an open subset of the manifolds $\AL^{1+s}$ or $\AL^{1+s}_\bz$.
    Then every critical knot $\g$ of $\TP^{(p,2)}$ on $\UL$ is of class $C^\infty(\Circle,\AmbSpace)$. 
\end{theorem}
\begin{proof}
    By substituting the splitting \cref{eq:splitting-TP} into \cref{eq:CriticalityWithoutLambda} for $ \EL=\TPp $, we 
    get the following criticality equation:
    \[
        2Q^{\TP}(\gamma,h)
        =
        F_\gamma h
        - 
        R^{\TP}_\gamma h
        \quad
        \text{for all $h \in H^{1+s}(\Circle,\AmbSpace)$}
        ,
    \]
    where 
    \[
        F_\gamma  h \ceq \D(\TP^{(p,2)})_\gamma \, Y_\gamma \inner{\gamma',h'}.
    \]
    Now suppose that we know already that $\gamma \in H^t(\Circle,\R^n)$ for some $t \geq 1 + s$.
    Then \cite[Proposition 4.3]{blatt-reiter_2015a} shows that 
    \[
        R^{\TP}_\gamma \in H^{t-1-p/2-\varepsilon}(\Circle,\R^n)\quad\Foa\varepsilon>0.
    \]
    Moreover, by \cref{lem:RegularityTPRemainderII}, 
    
    \[
        F_\gamma \in
        H^{t-1-p/2-\varepsilon}(\Circle,\R^n) \quad\Foa\varepsilon>0
        .
    \]
    Combining this, we see that 
    \[
        Q^{\TP}(\gamma,\cdot) \in H^{t-1-p/2-\varepsilon}(\Circle,\R^n) \Foa \varepsilon>0.
    \]
    By elliptic regularity (see the second part of \cref{lem:EllipticRegularityQTP}), $\gamma$ must have $p-1$ derivatives more than $\QL^{\TP}(\gamma,\cdot)$, thus
    \[
        \gamma \in 
        H^{t-1-p/2-\varepsilon + (p-1)}(\Circle,\R^n)
        =
        H^{t+(p-4)/2 - \varepsilon}(\Circle,\R^n)\quad\Foa\varepsilon>0
        .
    \]
    Since $p \in \intervaloo{4,5}$, we may fix $\varepsilon$ such that $0 < \varepsilon < (p-4)/2$, e.g., $ \varepsilon=(p-4)/{4}$, and get a strict increase in regularity.
    Starting at $t = 1 + s$ and iterating this, we obtain
    \[
        \gamma \in \bigcap_{t \geq 1+s} H^{t}(\Circle,\R^n) = C^\infty(\Circle,\R^n).
    \]
\end{proof}
Since $ \TPp $ is positively $ (4-p) $-homogeneous we obtain length-constrained critical knots as before, with an explicit bound on the scalar Lagrange multiplier. 
\begin{corollary}[$ \TPp $ critical knots]\label{cor:TP_critical_knots}
    Let $ \bz\in\R^n $ and $ \ML\in\{\AL^{1+s},\AL^{1+s}_\bz\} $. 
    Any critical knot $ \gamma $ of the restricted energy $ \TPp\big\vert_{\ML} $ is critical for $ \TPp-\lambda\,\LL $ on the open subset $ H^{1+s}_{\mathrm{ir}}\left( \R/\Z,\R^n \right)\subset H^{1+s}\left( \R/\Z,\R^n \right)$ for $ \lambda=(4-p)\TPp(\gamma)\le(4-p)\TP_{\min} $, where $ \TP_{\min} $ is defined in \cref{eq:TPmin}.
\end{corollary}

\begin{remark}
    In \cite[Corollary 1.3]{steenebruegge-vorderobermeier_2022} it was shown that critical points of integral Menger curvature $ \Mpz $ for $ p\in( \tfrac{3}{7},\tfrac{8}{7} ) $ under a fixed-length constraint are even real-analytic. The technique of that proof, however, does not seem to carry over to arclength-constrained critical knots, but it relies on a splitting of the differential $ \D\Mpz $ provided in \cite[Section 4]{blatt-reiter_2015b}. This splitting is of the same kind as that of $ \D\TPp $, $ p\in(4,5) $, see \cref{eq:splitting-TP}, that we frequently used in the present paper. Thus, the same method applies to the tangent-point energies. As a consequence, length constrained $ \TPp $-critical knots, and therefore by \cref{cor:TP_critical_knots} \textit{also $ \TPp|_{\ML} $-critical knots, are real-analytic for $ \ML\in \{\AL^{1+s},\AL^{1+s}_{\bz}\} $ for any $ \bz\in \R^n $, where $ s=s(p)={(p-3)}/{2} $ $ p\in(4,5) $. }
\end{remark}
