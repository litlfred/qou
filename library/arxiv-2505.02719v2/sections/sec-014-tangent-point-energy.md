---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-014-tangent-point-energy
section_title: "Tangent-point energy"
section_number: null
pages: 31-37
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.895
latex_coverage_ratio: 0.994
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
\label{sec:tanpoint}

The most difficult case is when the energy is a pure self-avoidance energy,
which naturally has a non-local structure so that now the leading order
terms are of fractional Sobolev regularity. We 
concentrate here on the tangent-point energies $\TP^{(p,2)}$ for
the range $p\in (4,5)$. 
As shown in \cite[Theorem 1.1]{blatt-reiter_2015a},
the underlying energy spaces are the Hilbert
spaces $H^{1+s}(\Circle,\AmbSpace)$ with $s \ceq (p-3)/2$.

A crucial tool will be the following splitting of the differential of $\TP^{(p,2)}$,
which is due to Blatt and Reiter, see \cite{blatt-reiter_2015a}.
Let $\gamma \in H^{1+s}_\injreg(\Circle,\AmbSpace)$ be parametrized by arclength
and let $h \in H^{1+s}(\Circle,\AmbSpace)$.
Then we have
\begin{equation}
    \D(\TP^{(p,2)})_\gamma h 
    =
    2 \, Q^{\TP}(\gamma,h) + R^{\TP}_\gamma h,
    \label{eq:splitting-TP}
\end{equation}
where $Q^{\TP}$ is a symmetric bilinear form (which will soon turn out to encode an elliptic operator), and $R^{\TP}_{\gamma}$ is a ``remainder term'', which is well-defined for all $ h\in \BL=C^1(\R/\Z,\R^n) $.
Blatt and Reiter also characterize $\QL^{\TP}$ as a Fourier multiplier.
More precisely, they show (see \cite[Proposition~4.1 and its proof]{blatt-reiter_2015a}):
\begin{proposition}\label{lem:fourier-Q}
        There are $\varrho_k \in \C$, $k \in \Z$ such that 
        \[
                Q^{\TP}(f,h)
                =
                \sum_{k \in \Z} \varrho_k \inner{ \hat f_k, \hat h_k }_{\C^\AmbDim}
                \quad 
                \text{for all $f,h \in H^{\frac{p-1}{2}}(\Circle,\AmbSpace)$}
                ,
        \]      
        where $\hat{f}_k,\hat{h}_k \in \C^\AmbDim$ are the Fourier coefficients of $f$ and $h$, respectively.
        Moreover, there is a constant $c_{\TP} > 0$ such that 
        \[
                \varrho_k = c_{\TP} \abs{k}^{p-1} + o(\abs{k}^{p-1})
                \quad 
                \text{as $\left| k \right|\to \infty$,}
        \]
        where $ 0=\rho_0<\rho_{k}=\rho_{-k} $ for all $ k\in \N $, and $ \rho_{k} $ is non-decreasing in $ \left|k \right| $. 
\end{proposition}
The asymptotics of $(\varrho_k)_{k \in \N}$ imply that $f \mapsto Q^{\TP}(f,\cdot)$ is an elliptic operator of order $p-1$ in the following sense:

\begin{lemma}[$ Q^{\TP} $ elliptic]\label{lem:EllipticRegularityQTP}
    Let $ f\in L^2(\R/\Z,\R^n) $. Then the following holds. 
    \begin{enumerate}
        \item If $ f\in H^{t}\left( \R/\Z,\R^n \right) $ for some $ t\in \R $, then $ Q^{\TP}(f,\cdot) $ extends to a linear functional in $ H^{t-(p-1)}\left( \R/\Z,\R^n \right)\equiv(H^{(p-1)-t}\left( \R/\Z,\R^n \right)  )^* $, satisfying 
        \begin{equation}\label{eq:46eq1}
            \left\|Q^{\TP}(f,\cdot) \right\|_{H^{t-(p-1)}}\le C_{Q}\left\|f \right\|_{H^t}
        \end{equation}
        for some constant $ C_Q $ independent of f. 
        \item If $ Q^{\TP}(f,\cdot) \in H^{t-(p-1)}(\R/\Z,\R^n)$ for some $ t\in \R $, then $ f\in H^{t}(\R/\Z,\R^n) $. 
        \item Let $ s:=\frac{p-1}{2}-1 $. Then there are constants $ 0<C_1\le C_2<\infty $ such that 
        \begin{equation}\label{eq:46eq2}
            C_1\left\|f \right\|^2_{H^{1+s}}\le \left\|f \right\|_{L^2}^2+Q^{TP}(f,f)\le C_2\left\|f \right\|_{H^{1+s}}^2\,\Foa f\in H^{1+s}(\R/\Z,\R^n).
        \end{equation}
    \end{enumerate}
\end{lemma}

\begin{proof}
    \cref{lem:fourier-Q} implies that there is some $ k_0\in\N $ such that 
    \begin{equation}\label{eq:Qineq}\textstyle
        \frac{c_{\TP}}{2}\left|k \right|^{p-1}\le \rho_k\le 2 c_{\TP}\left|k \right|^{p-1} \quad \Foa \left|k \right|> k_0.
    \end{equation}
    We estimate for $ f,h\in C^\infty(\R/\Z,\R^n) $ by means of \cref{lem:fourier-Q} and \cref{eq:Qineq}: 
    \begin{equation}\label{eq:estimateQelip}
    \begin{aligned}
        Q^{\TP}(f,h)
         &\textstyle\le \sum_{k\in\Z\setminus\{0\}}\rho_{k}\left|\hat{f}_{k} \right|\left|\hat{h}_{k} \right|
        \le\rho_{k_0}\sum_{0<\left|k \right|\le k_0}\left|\hat{f}_{k} \right|\left|\hat{h}_{k} \right|+2c_{\TP}\sum_{\left|k \right|>k_0}\left|k \right|^{t}\left|\hat{f}_{k} \right|\left|\hat{h}_{k} \right|\left|k \right|^{(p-1)-t}\\
        &\textstyle\le C_Q \sum_{k\in\Z\setminus\{0\}}( 1+\left|k \right|^t\left|k \right|^{p-1-t} )\left|\hat{f}_{k} \right|\left|\hat{h}_{k} \right|\\
        &\textstyle\le C_Q \sum_{k\in\Z\setminus\{0\}}\left( 1+\left|k \right|^t \right)\left|\hat{f}_{k} \right|( 1+\left|k \right|^{p-1-t} )\left|\hat{h}_{k} \right|
        \le C_Q \left\|f \right\|_{H^t}\left\|h \right\|_{H^{p-1-t}},
    \end{aligned}
    \end{equation}
    where we have set $ C_Q\ceq\max\{\rho_{k_0},c_{\TP}\} $.
     By density of $ C^\infty(\R/\Z,\R^n) $ in $ H^{\sigma}(\R/\Z,\R^n) $ for all $ \sigma\in \R $ (see, e.g. \cite[Statement 4 in Section 2.3]{AgranovichSobolevSpaces2015}) this estimate extends to all $ f\in H^{t}(\R/\Z,\R^n) $ and $ h\in H^{p-1-t}(\R/\Z,\R^n) $. 
    Hence, $ Q(f,\cdot)\in H^{t-(p-1)} \left( \R/\Z,\R^n \right)$ if $ f\in H^t(\R/\Z,\R^n) $ 
    satisfying \cref{eq:46eq1}. Choosing $ t=\frac{p-1}{2} $ and $ h\ceq f $ in \cref{eq:estimateQelip} yields the upper bound on $ \left\|f \right\|_{L^2} +Q^{\TP}(f,f)$ in \cref{eq:46eq2}. 
    Similarly, as in \cref{eq:estimateQelip} we use \cref{lem:fourier-Q} to estimate  
   \begin{align*}
     2Q^{\TP}(f,f)&\textstyle\ge \frac{2\rho_1}{k_0^{2+2s}}\sum_{0<\left|k \right|\le k_0}\left| k \right|^{2+2s} \left|\hat{f}_{k} \right|^2+c_{\TP}\sum_{\left|k \right|>k_0}\left|k \right|^{2+2s}\left|\hat{f}_{k} \right|^2
        \ge\rho_{*}\sum_{k\in\Z}\left|k \right|^{2+2s}\left|\hat{f}_{k} \right|^2
   \end{align*}
   for $ \rho_{*}\ceq \min\{\frac{2\rho_{1}}{k_0^{2+2s}},c_{\TP}\} >0$. Therefore, the lower bound in \cref{eq:46eq2} follows from the fact that 
   \begin{align*}\textstyle
    \left\|f \right\|_{H^{1+s}}^2=\sum_{k\in\Z}(1+\left|k \right|^2)^{1+s}\left|\hat{f}_{k} \right|^2 \le 2^{1+s}\left( \sum_{k\in\Z} \left|f_k \right|^2+\sum_{k\in \Z}\left|k \right|^{2+2s}\left|\hat{f}_{k} \right|^2\right),
   \end{align*}
   if we set $ C_1=\frac{1}{2^{2+s}}\min\{\rho_{*},2\} $. 

   It remains to show the second statement, which does \emph{not} come with an a priori estimate for $ \left\|f \right\|_{H^{t}} $ in terms of $ \left\|Q^{TP}(f,\cdot) \right\|_{H^{t-(p-1)}} $. Considering only those $ h\in C^\infty(\R/\Z,\R^n) $ with $ \hat{h}_{k}=0 $ for $ \left|k \right|=0,\dots,k_0 $, we infer from \cref{eq:Qineq} 
   \begin{align*}\textstyle
    \frac{c_{\TP}}{2}\sum_{\left|k \right|>0}\left\langle \hat{f}_{k}\left|k \right|^t,\left|k \right|^{p-1-t}\hat{h}_{k} \right\rangle_{\C^n} \le \left\|Q^{\TP}(f,\cdot) \right\|_{H^{t-(p-1)}}\left\|h \right\|_{H^{(p-1)-t}}
   \end{align*}
   for all such $ h $. By density of smooth functions with the first $ 2k_{0}+1 $ Fourier coefficients vanishing we obtain
   \begin{align*}\textstyle
    &\|( \delta_{k,k_0}\hat{f}_{k}\left|k \right|^t )_{k}\|_{\ell^2}\\
    &\textstyle=\sup\left\{\left|\sum_{\left|k \right|>k_0}\left\langle \hat{f}_{k}\left|k \right|^t,\left|k \right|^{p-1-t}\hat{h}_{k} \right\rangle_{\C^n}  \right|: h\in C^\infty,\hat{h}_{k}=0\text{ for } \left|k \right|\le k_0,\left\|h \right\|_{H^{(p-1)-t}}\le 1\right\}\\
    &\le \left\|Q^{\TP}(f,\cdot) \right\|_{H^{t-(p-1)}},
   \end{align*}
   where $ \delta_{k,k_0}$  equals $1 $ if $ \left|k \right|>k_0 $ and $ 0 $ if $ \left|k \right|\le k_0 $. This implies that $ (\hat{f}_{k}\left|k \right|^{t})_{k}\in \ell^2 $, which together with the assumption that $ f\in L^2(\R/\Z,\R^n) $ shows that $ ((1+k^2)^{\frac{t}{2}}\hat{f}_{k})_{k}\in \ell^2 $, or equivalently $ f\in H^{t}(\R/\Z,\R^n).$
\end{proof}

We are now going to verify the assumption of our
abstract result, \Cref{thm:PS-abstract},
guaranteeing the (PS)-condition for the tangent-point energies.

\begin{refproof}[Proof of \Cref{thm:PS-TP}]
Fix $p\in (4,5)$ and $s \ceq s(p) = (p-3)/ 2$. 
Throughout the proof
we abbreviate the energy by $\TP \ceq \TP^{(p,2)}$ and consider the open 
subset $\OL \ceq H^{1+s}_\injreg(\R/\Z,\R^n)$ of the Hilbert space
$\HL \ceq H^{1+s}(\R/\Z,\R^n)$, which compactly embeds into the
Banach space $\BL \ceq C^1(\R/\Z,\R^n)$. Clearly, $\TP$ is non-negative,
and it is of class $C^1(\OL)$ due to \cite[Theorem 1.4 \& subsequent
remark]{blatt-reiter_2015a} and \cite{wings_2018}. Since $s\in (1/2,1)$
and $\bz\in\R^n$ are fixed, we can apply
\Cref{cor:basic-assumptions} to deduce condition \ref{condE} for the 
arclength submanifold $\AL^{1+s}_\bz$. Moreover, the linear projection
\[
        \smash{\pr_\g^{\AL^{1+s}_\bz} \colon T_\g\OL\to T_\g\AL^{1+s}_\bz}
\]
has property \ref{condP}.

Towards condition \ref{condL} we take a (PS)-sequence $(\g_m)_m\subset\AL^{1+s}_\bz$
for $\TP|_{\AL^{1+s}_\bz}$, converging strongly
in the Hilbert space $\HL$ to some curve $\g_\infty\in
\HL$. Since $T \ceq \sup_{m\in\N}\TP(\g_m)<\infty$ we can apply the uniform
bilipschitz estimate \cite[Proposition 2.7]{blatt-reiter_2015a} to deduce
the existence of some constant $b=b(T,p)>0$ such that
\begin{equation}\label{eq:bilip-TP}
|\g_m(u)-\g_m(v)|\ge b|u-v|_{\R/\Z}\quad\Foa u,v\in\R/\Z,\,m\in\N.
\end{equation}
By the compact embedding $\HL\hookrightarrow\BL$ we find a $C^1$-convergent
subsequence $\g_{m_k}\to\g_\infty$ as $k\to\infty$, so that \cref{eq:bilip-TP}
is conserved in the limit; hence $\g_\infty$ is a knot, satisfying in
addition
$$

|\g_\infty'(u)|=\lim_{k\to\infty}|\g_{m_k}'(u)|=1\Foa u\in\R/\Z
\quad\AND\quad \g_\infty(0)=\lim_{k\to\infty}\g_{m_k}(0)=\bz.
$$
Therefore, $\g_\infty\in\AL^{1+s}_\bz$, which proves condition \ref{condL}.

The uniform energy bound $T$ implies by means of 
\cite[Proposition 2.5]{blatt-reiter_2015a} the existence of a constant 
$C=C(T,p)$  such that $\sup_{m\in\N}\lfloor\g_m'\rfloor_{s,2}\le C$,
where $\lfloor\cdot\rfloor_{s,2}$ denotes the seminorm
characterizing the fractional
Sobolev space $H^{1+s}$ as subspace of
the standard Sobolev space~$H^1$. 
In addition,
$$
|\g_m(u)|\le |\g_m(u)-\g_m(0)|+|\bz|\le 1+|\bz|\quad\Foa u\in\R/\Z,\,m\in\N,
$$
since $|\g_m'|=1$ on $\R/\Z$, so that $\sup_{m\in\N}\|\g_m\|_{H^{1+s}}\le
2+|\bz| + C,$ which establishes condition \ref{condB}.

The splitting \cref{eq:splitting-TP} of $\D (\TP)_\g h$ leads us to 
define as quadratic term $\QL$ in condition \ref{condS}
\begin{equation}\label{eq:def-QL}
        \QL(\g,h) \ceq 2 \, Q^{\TP}(\g,h)+2\langle \g,h\rangle_{L^2}.
\end{equation}

By definition, $ \QL $ is a continuous bilinear form and satisfies \ref{condS1} with $\mu(\cdot)\equiv 1$. 
Because of \cref{eq:46eq2} in \cref{lem:EllipticRegularityQTP} the bilinear form $ \QL $ satisfies \ref{condS2}
with coercivity constant $c \ceq 2C_1$.

It remains to verify condition \ref{condS3} for the remainder term $ R^{\TP}_{\gamma}h-2 \left\langle \gamma,h \right\rangle_{L^2}  $
to obtain the full
splitting condition \ref{condS}. The $L^2$-inner product is bounded on bounded sets (and hence on  \Econtrolled{\TPp} sets) since
\begin{equation}\label{eq:L2-term}
\langle\g,h\rangle_{L^2}\le\norm{\g}_{L^2} \norm{h}_{L^2} \le \norm{\g}_\HL \norm{h}_\BL \quad \Fo \gamma\in \AL^{1+s}_{\bz},h\in \BL.
\end{equation}
According to \cite[Lemma 4.2]{blatt-reiter_2015a} the term $R^{\TP}_{\gamma}h$ is the finite sum
of expressions, each of which can be bounded from above by
\begin{equation}\label{eq:bounding-R-TP}
\textstyle
C\int_{\R/\Z}\int_\frac{1}{2}^\frac{1}{2}\int_0^1\int_0^1\frac{|\g'(u+s_1w)-\g'(u+s_2w)|^2}{|w|^{p-2}}\d \theta_1\d\theta_2\d w\d u\cdot \|h\|_{C^1},
\end{equation}
where $s_i\in\{0,\theta_i\}$ for $i=1,2$, and
$C=C(\TP(\g)) $ is a constant that depends non-decreasingly on the energy value $ \TP(\gamma) $ through the bilipschitz constant $ b=b(\TP(\gamma),p)>0 $ again by 
\cite[Proposition 2.7]{blatt-reiter_2015a}.
By inserting $\pm\g'(u)$ in the numerator of the multiple integral in 
\cref{eq:bounding-R-TP} if
$s_i\not= 0$ for $i=1,2$, we bound this integral by means of the triangle
inequality from above by two triple integrals of the form treated in 
\Cref{lem:triple-integrals} in \Cref{sec:arclength-reparam}, 
each of which
are bounded from above by the seminorm $\lfloor\g'\rfloor_{s,2}^2$.
So, $ \RL $ is bounded on \Econtrolled{\TPp} sets, and thus satisfies \ref{condS3}. 

Finally, we are left with verifying condition \ref{condD}. Combining \cref{eq:projection-ALs,eq:projection-ALsz,eq:log-strain-differential} we can write 
\begin{align*}
    ( \Id_{\HL}-\pr^{\AL^{1+s}_{\bz}}_{\gamma})h \overset{\eqref{eq:projection-ALs},\eqref{eq:projection-ALsz}}{=}Y_{\gamma}\D\Sigma_{\gamma}h+\pr^{\AL^{1+s}}_{\gamma}h(0)\overset{\eqref{eq:log-strain-differential}}{=}Y_\gamma \left\langle \gamma',h' \right\rangle +\pr^{\AL^{1+s}}_{\gamma}h(0).
\end{align*}
Since $ \D(\TPp)_{\gamma}\tilde{h}\, $ contains\footnote{The explicit formula for the differential of $ \TPp $ is restated in \cref{eq:DTP_formula} in the proof of \cref{lem:RegularityTPRemainderII} below.} only differences and derivatives of a general test function $ \tilde{h} $, {(see \cite[(1.11) in Theorem 1.4]{blatt-reiter_2015a} specified to the present case $ q=2 $)} we only need to bound 
$|\D(\TPp)_{\gamma}Y_\gamma \left\langle \gamma',h' \right\rangle |$
from above by $ C\left\|h \right\|_{\BL} $, where the constant $ C=C(\gamma) $ remains controlled on \Econtrolled{\TPp} subsets of $ \AL_{\bz}^{1+s} $. This follows from \cref{eq:regremainderTPcondD} of \cref{lem:RegularityTPRemainderII} below, since $ H^{3/2+\varepsilon}(\R/\Z,\R^n) $ embeds into $ C^1(\R/Z,\R^n) $ for all $ \varepsilon>0 $. Thus, \ref{condD} holds true for $ S_{\gamma}\ceq\D(\TPp)_{\gamma}Y_\gamma \left\langle \gamma',(\cdot)' \right\rangle  $.
\end{refproof}

\begin{refproof}[Proof of \Cref{cor:minimizing-knots-TP} and \Cref{thm:gradient-flow-TP}.]
It was shown in \cite[Theorem 3.5]{steenebruegge_2023} that the 
tangent-point energy $\TP^{(p,2)}$ for any $p\in (4,5)$ is of class
$C^{1,1}_\loc$ on the open subset $\OL \ceq H^{1+s(p)}_\injreg(\R/\Z,\R^n)$
of the Hilbert space $\HL \ceq H^{1+s(p)}(\R/\Z,\R^n)$
for $s(p)$ as in \cref{eq:s-TP}. In fact $ \TPp $ is even smooth on its natural energy space, see \cite[Theorem 4.6]{doehrer-etal_2025}. The (PS)-condition holds according
to \Cref{thm:PS-TP}. Of course, $\TP^{(p,2)}$ is non-negative; hence
satisfies \ref{lower-bound}. For the verification of
condition \ref{condL}  in the proof of
\Cref{thm:PS-TP}  we only needed the uniform boundedness of
the energy along the sequence, which is assumed to converge in $\HL$,
so that \ref{condL**} follows. So, we may apply 
\Cref{thm:gradflow_subconvergence}
and
\Cref{koro:minimizer_existence}
to conclude.
\end{refproof}

\begin{lemma}\label{lem:RegularityTPRemainderII}
    Let $ \gamma\in \AL^{t} $ for some $ t\ge {(p-1)}/{2} $ and $ p\in(4,5) $. Then the mapping $ h\mapsto\D(\TPp)_{\gamma}Y_\gamma \left\langle \gamma',h' \right\rangle  $ is of class $ H^{t-1-\frac{p}{2}-\varepsilon}(\R/\Z,\R^n) $ for every $ \varepsilon>0$. 
    In particular, $ t={(p-1)}/{2} $, then for each $ \varepsilon>0 $ there is a constant $ C_{\varepsilon} =C_{\varepsilon}(\left\|\gamma \right\|_{H^{{(p-1)}/{2}}},\TPp(\gamma))$ depending non-decreasingly on the $ H^{{(p-1)}/{2}} $-norm and on the energy value of $ \gamma $, such that 
    \begin{equation}\label{eq:regremainderTPcondD}
    \begin{aligned}
        |\D(\TPp)_{\gamma}Y_\gamma \left\langle \gamma',h' \right\rangle  |\le C_{\varepsilon}\left\|h \right\|_{H^{\frac{3}{2}+\varepsilon}}\quad \Foa h\in H^{\frac{3}{2}+\varepsilon}(\R/\Z,\R^n).
    \end{aligned}
    \end{equation}
\end{lemma}
\begin{proof}
    Abbreviate $ \TP\ceq\TPp $ for some fixed $ p\in(4,5) $. It suffices to prove that\\
    $ \D(\TP)_{\gamma}Y_\gamma \left\langle \gamma',h' \right\rangle  $ is a finite sum of expressions of type\footnote{We follow the convention of \cite{blatt-reiter_2015a} that $ \bigoasterisk $ denotes any kind of product.}
    \begin{equation}\label{eq:Rgpsi-structure}
        \textstyle
        \int_{\R/\Z}\int_{-\frac{1}{2}}^{\frac{1}{2}}\idotsint_{[0,1]^K}g^{(p)}(u,w,s_1,\dots,s_{K})\bigoasterisk
        \psi(u+s_Kw)\d \theta_1\cdots\d\theta_K\d w\d u,
    \end{equation}
    where 
    \begin{equation}\label{eq:g-formstructure}\textstyle
        g^{(p)}(u,w,s_1,\dots,s_{K})\ceq\GL\left( \left|\frac{\triangle \gamma}{w} \right| \right)\frac{|\gamma'(u+s_1w)-\gamma'(u+s_2w)|^2}{\left|w \right|^{p-2}}\bigoasterisk\limits_{i=1}^{K-1}\gamma'(u+s_iw),
    \end{equation}
    $ \GL^{(p)} $ is analytic on $ (0,\infty) $, $ s_i\in\{0,\theta_i\} $ for $ i=1,\dots,K $, $ K\ge3 $. 
    Here, either $ \psi=h' $, or $ \psi\equiv V_{\gamma}f $, for $ f\ceq \left\langle \gamma',h' \right\rangle  $, where $ V_\gamma f $ is the vector defining the right-inverse $ Y_\gamma $ in \cref{eq:right-inverse-Y}:
    \begin{equation}\label{eq:right-inverse-formula-again}
    \begin{aligned}
          Y_\g f(x)&=\textstyle
	    \int_0^x  f(u) \, \g'(u) \d u+ \int_0^x \P_{\g'(u)}^\perp V_{\gamma} f \d u\\
        &\qec\textstyle \Upsilon^{1}f(x)+\Upsilon^2f(x)\quad \Foa f\in H^{s}(\R/\Z,\R^n).
    \end{aligned}
    \end{equation}
    Indeed, once $ \D(\TP)_\gamma Y_\gamma \left\langle \gamma',h' \right\rangle  $ is shown to have that specific structure, one can check that the proof of \cite[Proposition 4.3]{blatt-reiter_2015a} can be adopted without any changes to show that each expression of the form \cref{eq:Rgpsi-structure} as a function of $ h $ in case $ \psi=h' $, is of class $ H^{t-1-\frac{p}{2}-\varepsilon}(\R/\Z,\R^n) $ for every $ \varepsilon>0 $. If, however, $ \psi=V_\gamma f $, then recall that $ \gamma $ has bilipschitz constant $b_{\gamma}>0$ depending merely on the energy value $ \TP(\gamma) $, by \cite[Proposition 2.7]{blatt-reiter_2015a} (cf \cref{eq:bilip-TP}), so that we simply estimate by means of $ \left|\gamma' \right|=1 $, 
    \begin{align*}\textstyle
        |g^{(p)}(u,w,s_1,\dots,s_K)|\le C(\TP(\gamma))\frac{|\gamma'(u+s_1w)-\gamma'(u+s_2w)|^2}{\left|w \right|^{p-2}}\,\,\Foa u\in\R/\Z,\, \left|w \right|\le \frac{1}{2},
    \end{align*}
    and for $  s_1,\dots,s_K $.
    Inserting $ \pm \gamma'(u) $ in the numerator on the right-hand side allows us to apply \cref{lem:triple-integrals} to conclude 
\begin{equation}\label{eq:Vf-estimate}
\begin{aligned}\textstyle
    &\textstyle|\int_{\R/\Z}\int_{-\frac{1}{2}}^{\frac{1}{2}}\idotsint_{[0,1]^K}g^{(p)}(u,w,s_1,\dots,s_K)\bigoasterisk V_\gamma f \theta_1\cdots\d\theta_K\d w\d u|
    \le 4C(\TP(\gamma))\lfloor\g'\rfloor_{s,2}^2\left|V_\gamma f \right|.
\end{aligned}
\end{equation}
Apply \cref{lem:DEbYisLowerOrderIIII} \textrm{(i)} for $ f=\left\langle \gamma',h' \right\rangle  $ and \cref{lem:ProductRuleAsDistributionII} for $ \tau=\sigma(t-1,\varepsilon)=t-1 $ to conclude that this is bounded by $ \tilde{C}\left\|h \right\|_{H^{1-t}} $ with a constant $ \tilde{C} $ depending non-decreasingly on $ \left\|\gamma \right\|_{H^t} $ and $ \TP(\gamma) $. Since $ H^{t-1}\subset H^{t-1-\frac{p}{2}-\varepsilon} (\R/\Z,\R^n)$ for all $ \varepsilon>0 $, this proves the claim. In addition, combining \cref{eq:Vf-estimate} for $ t=(p-1)/2$, with an analogous estimate in the case $ \psi=h' $ leads to 
\cref{eq:regremainderTPcondD}. 

So, it remains to establish the structure \cref{eq:Rgpsi-structure} for all summands of $ \D(\TP)_{\gamma}Y_\gamma \left\langle \gamma',h' \right\rangle  $. To that extent we specify the formula for the first variation $ \delta \TPpq[](\gamma,h) $ given in \cite[Theorem 1.4]{blatt-reiter_2015a} to the present case $ q=2,\,p\in(4,5) $ to obtain for general $ h\in H^{1+s}(\R/\Z,\R^n) $, $ s=(p-3)/2 $, (using the abbreviation $ \triangle F=F(u+w)-F(u) $, for $ F:\R/\Z\to\R^n $)
\begin{equation}
\begin{aligned}
    \label{eq:DTP_formula}
        &\textstyle\D(\TP)_{\gamma}h=\int_{\R/\Z}\int_{-\frac{1}{2}}^{\frac{1}{2}}
		2\frac{\langle \P^\perp_{\gamma'(u)}(\triangle\gamma),\triangle h -\left\langle \triangle \gamma,\gamma'(u) \right\rangle h'(u) \rangle }{\left|\triangle \gamma \right|^p}\dd u \dd w\\
		&\textstyle\hspace{12pt}+\int_{\R/\Z}\int_{-\frac{1}{2}}^{\frac{1}{2}}|\P^\perp_{\gamma'(u)}(\triangle \gamma) |^2\big(-p\frac{\left\langle \triangle \gamma,\triangle h \right\rangle}{\left|\triangle \gamma \right|^{p+2}}
		+\frac{(\left\langle \gamma'(u),h'(u) \right\rangle+\left\langle \gamma'(u+w),h'(u+w) \right\rangle  )}{\left|\triangle \gamma \right|^{p}}\big)\dd u \dd w\\
        &\textstyle\hspace{12pt}\qec\widetilde{Q}_{\gamma}h+\widetilde{R}_3h+\widetilde{R}_4h.
\end{aligned}
\end{equation}
Notice that for the last two summands $ \widetilde{R}_3h=R_3^{(p)} $ and $ \widetilde{R}_4h=R_4^{(p)} $, where $ R_i^{(p)} $ are defined in \cite[(4.3)]{blatt-reiter_2015a}. In the present context we have to replace $ h $ by the more specific function $ Y_\gamma f $ given in \cref{eq:right-inverse-formula-again} for $ f=\left\langle \gamma',h' \right\rangle  $, satisfying \cref{eq:derivative-right-inverse}
and therefore \cref{eq:first_derivative_rightInverse}. Consequently, $ \tilde{R}_{4}Y_{\gamma}\left\langle \gamma',h' \right\rangle=\tilde{R}_{4}h =R_4^{(p)} $, and the structure of that term has been shown in \cite[Lemma 4.2]{blatt-reiter_2015a} to be of the form \cref{eq:Rgpsi-structure} for $ \psi=h' $ if one artificially adds the factors $ \gamma'(u+s_1w) $ and $ \gamma'(u+s_2w) $ to the last product in \cref{eq:g-formstructure}. 

The term $ \widetilde{R}_{3}\gamma $ has the {same form \cref{eq:Rgpsi-structure} for $ \psi=h' $,} which translates via \cref{eq:derivative-right-inverse} directly to one summand of the form \cref{eq:Rgpsi-structure} with $ \psi:=f\gamma'=\left\langle \gamma',h' \right\rangle \gamma' $, and a second summand of the form \cref{eq:Rgpsi-structure} with $ \psi\ceq \P^{\perp}_{\gamma'}V_\gamma f=V_\gamma f-\langle V_\gamma f,\gamma' \rangle \gamma'$. In both summands we can absorb the $ \gamma' $-terms of the respective $ \psi $ into the extended product to obtain $ \bigoasterisk_{i=1}^{K+1}\gamma'(u+s_i w) $, with $ s_K=s_{K+1} $, and end up with terms that are again of the form \cref{eq:Rgpsi-structure} with either $ \psi=h' $ or $ \psi=V_{\gamma}f$. As shown, the first term is treated as in \cite[Proposition 4.3]{blatt-reiter_2015a}, and the second by direct estimates as in \cref{eq:Vf-estimate} above. 

Finally, we need to investigate $ \widetilde{Q}_{\gamma}h $ in \cref{eq:DTP_formula} for $ h\ceq Y_{\gamma}f $, $ f=\left\langle \gamma',h' \right\rangle  $. By means of 
\[\textstyle\triangle\gamma=w\int_{0}^{1}\gamma'(t_1)\d \theta_1, \text{ and }\triangle(Y_\gamma f)=w\int_{0}^{1}(Y_\gamma f)'(t_2)\d \theta_2,\]
for $ t_i=u+\theta_i w,\,i=1,2$, we rewrite the numerator of $ \widetilde{Q}_{\gamma}Y_\gamma f $  as 
\begin{equation}\label{eq:ABsplitting}
\begin{aligned}\textstyle
            2\inner[\big]{ 
                \P^\perp_{\gamma'(u)} \Delta\gamma, \Delta (Y f)
                -
                \inner{ \Delta \gamma,\gamma'(u) } \pars{Y f }'(u) 
            }
            =
            2w^2 \! \int_0^1\int_0^1 
                \!\pars{\mathbf{A} + \mathbf{B}}
            \d \theta_1 \d \theta_2,
\end{aligned}
\end{equation}
where - according to the splitting \cref{eq:right-inverse-formula-again} - 
\begin{equation}\label{eq:splitting-A-part}
\begin{aligned}
    \mathbf{A} 
            &\ceq 
            \inner[\big]{
                 \P^\perp_{\gamma'(u)} \gamma'(t_1)
                 , 
                 (\Upsilon^1f)'(t_2)
                 {-
                 \inner{ \gamma'(t_2),\gamma'(u) } (\Upsilon^1f)'(u)}
            }\\
            &\overset{\cref{eq:right-inverse-formula-again}}{=}\inner[\big]{
                 \P^\perp_{\gamma'(u)} \gamma'(t_1)
                 , 
                 \gamma'(t_2)
            }f(t_2),
\end{aligned}
\end{equation}
and, with the abbreviation $ V\ceq V_{\gamma}f $,
\begin{equation}\label{eq:splitting-B-part}
\begin{aligned}
    \mathbf{B} 
            &\ceq 
            \inner[\big]{
                 \P^\perp_{\gamma'(u)} \gamma'(t_1)
                 , 
                 (\Upsilon^2f)'(t_2)
                 -
                 \inner{ \gamma'(t_2),\gamma'(u) } (\Upsilon^2 f)'(u) 
            }
            \\
             &=
            \inner[\big]{ 
                P^\perp_{\gamma'(u)} \gamma'(t_1)
                ,
                V 
                - \gamma'(t_2) \inner{\gamma'(t_2),V} 
                - \inner{\gamma'(t_2),\gamma'(u)} (V-\left\langle V,\gamma'(u) \right\rangle \gamma'(u))
            }\\
            &\overset{\cref{eq:right-inverse-formula-again}}{=}
            \inner[\big]{
                 \P^\perp_{\gamma'(u)} \gamma'(t_1)
                 , V
            }(1-\left\langle \gamma'(t_2),\gamma'(u) \right\rangle )-
            \inner[\big]{
                 \P^\perp_{\gamma'(u)} \gamma'(t_1)
                 , 
                \gamma'(t_2)               
            }
            \left\langle V,\gamma'(t_2) \right\rangle.
\end{aligned}
\end{equation}
We expand the prefactor of $ f(t_2) $ in \cref{eq:splitting-A-part}, which also appears in \cref{eq:splitting-B-part}, by means of the identity $ 1-\left\langle a,b \right\rangle=\frac{1}{2}\left|a-b \right|^2  $ for $ a,b\in \mathbb{S}^{n-1} $, as 
\begin{equation}\label{eq:vdMscan-C}
\begin{aligned}
    &\left\langle \gamma'(t_1)-\left\langle \gamma'(t_1),\gamma'(u) \right\rangle\gamma'(u),\gamma'(t_2)  \right\rangle \\
    =&\left[\left\langle \gamma'(t_1),\gamma'(t_2) \right\rangle -1
    +1-\left\langle \gamma'(t_1),\gamma'(u) \right\rangle 
    +\left\langle \gamma'(t_1),\gamma'(u) \right\rangle (1-\left\langle \gamma'(u),\gamma'(t_2) \right\rangle )
    \right]\\
    =&\textstyle\frac{1}{2}\left[-\left|\gamma'(t_1)-\gamma'(t_2) \right|^2+\left|\gamma'(t_1)-\gamma'(u) \right|^2+\left\langle \gamma'(t_1),\gamma'(u) \right\rangle\left|\gamma'(u)-\gamma'(t_2) \right|^2 \right],
\end{aligned}
\end{equation}
whereas the first summand of $ \mathbf{B} $ equals 
\begin{equation}\label{eq:vdMscan-D}
\begin{aligned}\textstyle
    \frac12 \left\langle \gamma'(t_1)-\left\langle \gamma'(t_1),\gamma'(u) \right\rangle\gamma'(u),V  \right\rangle \left|\gamma'(t_2)-\gamma'(u) \right|^2.
\end{aligned}
\end{equation}
Combining \eqref{eq:ABsplitting}--\eqref{eq:splitting-B-part} with \cref{eq:vdMscan-C,eq:vdMscan-D}, every summand constituting $ \widetilde{Q}_{\gamma}Y_\gamma f $ for $ f=\left\langle \gamma',h' \right\rangle  $ has indeed the form \cref{eq:Rgpsi-structure,eq:g-formstructure}, for $ \psi=h' $ or $ \psi =V_\gamma f $.
\end{proof}
