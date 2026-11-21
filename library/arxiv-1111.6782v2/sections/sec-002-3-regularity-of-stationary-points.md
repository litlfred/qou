---
doc_id: arxiv-1111.6782v2
doc_title: "Stationary Points of O’Hara’s Knot Energies"
section_id: sec-002-3-regularity-of-stationary-points
section_title: "Regularity of stationary points"
section_number: 3
pages: 13-17
source_pdf: 1111.6782v2.pdf
source_sha256: 5acfde49432e59e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.987
doc_brief: "Stationary Points of O’Hara’s Knot Energies — In this article we study the regularity of stationary points of the knot ener- gies E(α) introduced by O’Hara in [14, 15, 16] in the range α ∈(2, 3)."
---
\label{sect:bootstrap}

In this section we prove Theorem~\ref{thm:rsp} so we are
looking at embedded curves $\gamma \in \W[(1+\alpha)/2]$ parametrized by arc-length that satisfy
\begin{equation}\label{eq:ele}
 \delta\E(\gamma;h) + \lambda \int_{\mathbb R / \mathbb Z} \sp{\gamma',h'} =0 \quad \forall h \in \W[(1+\alpha)/2]
  (\mathbb R / \mathbb Z, \mathbb R^n)
\end{equation}
where $\lambda>0$ and
\begin{align*}
 \delta\E(\gamma;h) = \lim_{\varepsilon \searrow 0}  \iint_{U_\eps} \Bigg( &
    (\a-2) \frac{\sp{\dg(u),\dh(u)}}{\abs w^\a}
    + 2 \frac{\sp{\dg(u),\dh(u)}}{\abs{\D\g}^\a} \\
    &{}-\a \frac{\sp{\D\g,\D h}}{\abs{\D\g}^{\a+2}}
    \Bigg) \d w\d u.
\end{align*}
To prove that $\gamma \in C^\infty(\mathbb R / \mathbb Z, \mathbb R^n)$, we first decompose 
\begin{equation}\label{eq:decomposE}
 \delta\E(\g;h) = \a\Q(\g,h) + \RR(\gamma,h)
\end{equation}
where
\begin{equation*}
 \Q (\gamma, h ) := \lim_{\varepsilon \searrow 0} 
  \iint_{U_\varepsilon} 
    \left(\frac {\left\langle \gamma'(u), h'(u) \right\rangle }{|w|^\alpha} 
      -\frac {\left\langle \gamma(u+w)-\gamma(u), h(u+w) - h(u) \right\rangle}{|w|^{\alpha+2}} \right) \d w\d u
\end{equation*}
and $\RR(\gamma,h)$ is given by
\begin{align*}
&\RR(\gamma,h) :=
  2 \lim_{\eps\searrow0}\iint_{U_\eps} \sp{\dg(u),\dh(u)} \br{\frac1{\abs{\D\g}^{\a}} - \frac1{\abs w^{\a}}} \d w\d u \\
   &{}-\a\lim_{\eps\searrow0}\iint_{U_\eps} \sp{\D\g,\D h} \br{\frac1{\abs{\D\g}^{\a+2}} - \frac1{\abs w^{\a+2}}} d wd u.
\end{align*}
Later on, it will become evident that, in contrast to~$\Q$, the integral defining~$\RR$ is not a principle value, i.~e.\@ we may
write~$U_0$ instead of~$U_\eps$.

It was already observed by He in \cite{he:elghf} and the second author in \cite{reiter:rkepdc} that
$\Q(\gamma,h)$ is a lower order perturbation of the $L^2$ product of 
$(-\Delta)^{\frac {\alpha +1} 4} \gamma$ and $(-\Delta)^{\frac {\alpha +1} 4} h$.
To see this, let us first extend $\Q$ to complex valued functions
by exchanging the scalar product on $\mathbb R^n$ to the scalar product on $\mathbb C^n$.
We denote by $\hat f(k)= \int_{\mathbb R / \mathbb Z} f(u) e^{-2\pi i ku} \d u$ the $k$-th Fourier coefficient of $f$.

\begin{proposition}[cf. \protect{\cite[Lemma 2.3]{he:elghf}, \cite[Proposition 1.4]{reiter:rkepdc}}] \label{prop:formOfQ}
 There is a sequence of real numbers $q_k$, $k \in \mathbb Z$, converging to a positive constant
 for $|k| \rightarrow \infty$
 such that for all $\gamma, h \in\W[\br{1+\alpha}/2 ,2](\mathbb R / \mathbb Z, \mathbb R^n)$
 we have
 \begin{equation} \label{eq:formOfQ}
  \Q(\gamma, h ) = \sum_{k\in \mathbb Z} q_k |k|^{\alpha +1}  \hat \gamma(k) \overline{\hat h (k)}.
 \end{equation}
\end{proposition}


Apart from this observation, the proof of Theorem~\ref{thm:rsp}  relies on the following estimate regarding the 
term $\RR(\gamma,h)$. Basically it lets us treat this term like a lower order perturbation.

\begin{proposition}\label{prop:RR}
 Let $\g\in\Wir[(\a+1)/2+\sigma]$ be parametrized by arc-length, $\sigma \geq 0$.
 \begin{enumerate}
  \item In the case $\sigma = 0$ we have $\RR(\gamma, \cdot)\in\br{H^{3/2+\eps ,2}}^*$ for any $\eps>0$.
  \item If $\sigma >0 $ we have $\RR(\gamma, \cdot)\in\br{H^{3/2- \hat \sigma,2}}^*$
  for all $\hat \sigma < \sigma$.	
 \end{enumerate}
\end{proposition}

We will prove  Proposition~\ref{prop:RR} using Sobolev embeddings and the fractional Leibniz rule 
for Bessel potential spaces (cf. Lemma~\ref{lem:product}).

First we will show, that the two summands building $\RR$ can be brought into a common form 
and can thus be dealt with simultaneously. For that we use the fundamental theorem of calculus
to get
\begin{align*}
 &\sp{\D\g,\D h} \br{\frac1{\abs{\D\g}^{\a+2}} - \frac1{\abs w^{\a+2}}} \\
 &= w^2\int_0^1 \int_0^1 \sp{\dg (u+s_1 w),\dh(u+s_2 w)} \br{\frac1{\abs{\D\g}^{\a+2}} - \frac1{\abs w^{\a+2}}}
  \d s_1 \d s_2.
\end{align*}
Furthermore, for $\beta>0$,
\begin{multline*}
 \frac 1 {|\gamma(u+w) - \gamma(u)|^\beta} - \frac 1 {|w|^\beta} 
  = \frac {|w|^\beta}{|\gamma(u+w)-\gamma(u)|^\beta} \cdot
     \frac {1- \frac {|\gamma(u+w)-\gamma(u)|^\beta}{|w|^\beta}} {|w|^\beta} \\
  = G^{(\beta)}\left(\frac {\gamma(u+w)-\gamma(u)}{w}\right)
     \frac {2-2\frac {|\gamma(u+w)-\gamma(u)|^2}{w^2}} {|w|^\beta} \\
  = \int_{0}^1 \int_{0}^1 G^{(\beta)}\left(\frac {\gamma(u+w)-\gamma(u)}{w}\right)
  \frac {|\gamma'(u+\tau_1 w) - \gamma'(u+\tau_2 w)|^2}{|w|^\beta} d\tau_1 d \tau_2
\end{multline*}
where
\begin{align*}
 G^{(\beta)}(z) := \frac 1 {2|z|^\beta} \cdot \frac {1- |z|^\beta}{1 - |z|^2}
\end{align*}
is an analytic function away from the origin. Defining
\[ g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(u,w) :=  G^{(\beta)} 
\left(\frac {\gamma(u+w) - \gamma(u)}{w} \right) \frac {|\gamma'(u+\tau_1 w) -\gamma'(u+\tau_2 w)|^2}{|w|^\alpha} 
\gamma'(u+s_1 w) \]
we thus get








\begin{equation}\label{eq:DecompositionOfR}
\begin{aligned}
 \RR(\gamma,h)
 &= \lim_{\eps \searrow 0} \Bigg\{2\iint\limits_{U_\eps}\iint\limits_{[0,1]^2} \left\langle g^{(\alpha,\alpha)}_{0,\tau_1,\tau_2}(u,w), 
  h'(u) \right\rangle \d\tau_1 \d\tau_2\d w\d u \\
 & \quad - \alpha \iint\limits_{U_\eps}\iiiint\limits_{[0,1]^4} \left\langle g^{(\alpha,\alpha+2)}_{s_1,\tau_1,\tau_2}(u,w), 
  h'(u+s_2 w) \right\rangle \d s_1 \d s_2 \d\tau_1 \d\tau_2\d w\d u \Bigg\}.
 \end{aligned}
\end{equation}



Thus using H\"older's inequality we get the estimate 
\begin{equation} \label{eq:estL1}
\begin{split}
 \RR(\gamma,h) \leq C \|h'\|_{L^\infty} \sup_{\substack{\beta\in\set{\a,\a+2},\\s_1,\tau_1,\tau_2\in[0,1]}}
 \int_{-1/2}^{1/2}\norm{g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(\cdot,w)}_{L^1}\d w
 \\ \leq  C \|h\|_{\W[3/2 + \varepsilon, 2]} \sup_{\substack{\beta\in\set{\a,\a+2},\\s_1,\tau_1,\tau_2\in[0,1]}}
 \int_{-1/2}^{1/2}\norm{g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(\cdot,w)}_{L^1}\d w
\end{split}
\end{equation}
for any $\eps>0$.

For $\s \in\R$ let
\begin{equation}\label{eq:Ds}
 D^\s := (-\Delta)^{\s/2}.
\end{equation}
By partial integration we infer for $\ts \in \mathbb R$
\[ \int\limits_{\R/\Z}
 \sp{g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(u,w),h'(u+s_2w)}
 \d u
 =\int\limits_{\R/\Z}
 \sp{D^\ts g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(u,w),D^{-\ts}h'(u+s_2w)}
 \d u \]
and we can estimate the absolute value by
\[ \norm{D^{-\ts}h'}_{\Lp[\infty]}\int\limits_{\R/\Z}
 \abs{D^\ts g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(u,w)}
 \d u
 \le C\norm{h}_{\W[3/2-\ts+\eps,2]}
 \norm{g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(\cdot,w)}_{\W[\ts,1]} \]
 for any $\eps>0$.
Combining this with Equation~\eqref{eq:DecompositionOfR} we get
\begin{equation*} 
 \abs{\RR(\g,h)}
 \le C\norm{h}_{\W[3/2-\ts+\eps,2]}\sup_{\substack{\beta\in\set{\a,\a+2},\\s_1,\tau_1,\tau_2\in[0,1]}}
 \int_{-1/2}^{1/2}\norm{g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(\cdot,w)}_{\W[\ts,1]}\d w
\end{equation*}
for all $\ts$ and $\varepsilon >0$.
To prove Proposition~\ref{prop:RR}, given $\sigma > \hat \sigma $
we set $\ts = (\s + \hat \s)/2 > \hat \s$  and $\varepsilon = \ts-\hat \s$ in the calculations above,
to get
\begin{equation} \label{eq:estHsigma}
 \abs{\RR(\g,h)}
 \le C\norm{h}_{\W[3/2-\hat \s,2]}\sup_{\substack{\beta\in\set{\a,\a+2},\\s_1,\tau_1,\tau_2\in[0,1]}}
 \int_{-1/2}^{1/2}\norm{g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(\cdot,w)}_{\W[\ts,1]}\d w.
\end{equation}
Proposition~\ref{prop:RR} now immediately follows from Estimate~\eqref{eq:estL1},
Estimate~\eqref{eq:estHsigma} and the succeding lemma.

\begin{lemma}\label{lem:basicEstimate}
 Let $\gamma \in\W[(\alpha+1)/2+\s,2] (\mathbb R / \mathbb Z, \mathbb R^n)$ with $\s\ge0$ and $\beta>0$.
\begin{enumerate}
 \item If $\s=0$ then $g^{(\a,\beta)}_{s_1, \tau_1, \tau_2} \in L^1(\R/\Z\times(-\tfrac12,\tfrac12),\R^n)$.
  Furthermore, there is a constant $C<\infty$
  independent of $\tau_1$, $\tau_2$, and $s_1$ such that
  \[ \norm{g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}}_{\Lp[1]}\le C. \]
 \item If $\sigma> 0$ then $g^{(\a,\beta)}_{s_1, \tau_1, \tau_2,\cdot,\cdot} \in L^1((-\tfrac12,\tfrac12),H^{ \tilde \sigma,1}(\R/\Z,\R^n))$
 for all $\tilde \sigma < \sigma$
  and there is a constant $C<\infty$
  independent of $\tau_1$, $\tau_2$, and $s_1$ such that
  \[ \int_{-1/2}^{1/2}\norm{g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(\cdot,w)}_{\W[\tilde\sigma,1]}\d w \le C. \]
\end{enumerate}
\end{lemma}

\begin{proof}
 Let us first deal with the case $\sigma =0$. We get
 \begin{align*}
  &\|g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}\|_{L^1 (\mathbb R / \mathbb Z\times(-\frac12,\frac12), \mathbb R^n)} \\
  &\leq 
  \int_{\mathbb R, \mathbb Z}  \int_{-1/2}^{1/2} G^{(\beta)}\left(\frac {\gamma(u+w) - \gamma(u)}{w} \right) 
  \frac{|\gamma'(u+\tau_1 w) - \gamma'(u+\tau_2 w)|^2}{|w|^\alpha} \abs{\gamma'(u+s_1 w)}  dw du 
  \\
  & \leq C \|\gamma'\|_{\Lp[\infty]} \int_{\mathbb R / \mathbb Z} \int_{-1/2}^{1/2}
     \frac{|\gamma'(u+\tau_1 w) - \gamma'(u+\tau_2 w)|^2}{|w|^\alpha}
    dw du
  \\
  & \leq C \|\gamma'\|_{\Lp[\infty]} \|\gamma\|_{\W[(\a+1)/2,2]}^2
 \end{align*}
  which proves the statement for $\sigma =0$.

 Since there is no suitable 
 product rule for $p=1$, we will
 estimate $\norm{g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(\cdot,w)}_{\W[\tilde \sigma,p]}$ for $p>1$ sufficiently small.
 For this we will use a small $\tilde p > p$ and let $q$
 be such that 
 \begin{equation*}
  \frac 1 p = \frac 1 {2\tilde p} +  \frac 1 {2\tilde p} + \frac 1 q + \frac 1 q,
 \end{equation*}
 i.~e.\@ we set
 \begin{equation*}
  q = 2 \frac {\tilde p p} {\tilde p -p}.
 \end{equation*}
Using that
\begin{equation*}
 \frac {\gamma(u+w)-\gamma(u)} {w} = \int_{0}^1 \gamma'(u+\tau w) d\tau,
\end{equation*}
that $\gamma$ is bi-Lipschitz, and that $G^{(\beta)}$ is analytic away from the origin, 
we get that
\begin{equation*}
 \left\|G^{(\beta)}\left(\frac {\gamma(\cdot +w)-\gamma(\cdot)}{w}\right)\right\|_{\W[\tilde\sigma,q]}
 \leq C \|\gamma\|_{\W[ \tilde \sigma +1,q]}
  \leq C
\end{equation*}
by the Sobolev embedding.

Using the fractional Leibniz rule (Lemma~\ref{lem:product}) three times, we derive for $\tilde\s\in(0,\s)$
\begin{align*}
  \|g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}&(\cdot,w)\|_{\W[\tilde \sigma,p]} \\
 &\leq C 
 \left\|G^{(\beta)}\left(\frac {\gamma(\cdot +w)-\gamma(\cdot)}{w}\right) \right\|_{\W[ \tilde \sigma,q]}
 \|\gamma'\|_{\W[\tilde \sigma,q]}
\frac{\|\gamma'(\cdot + \tau_1 w) - \gamma'(\cdot + \tau_2 w )\|^2_{\W[\tilde\sigma,2\tilde p]}}{\abs w^\a}
 \\
 &\leq C \frac{\|\gamma'(\cdot + \tau_1 w) - \gamma'(\cdot + \tau_2 w )\|^2_{\W[\tilde\sigma,2\tilde p]}}{\abs w^\a}.
\end{align*}
We now choose $\tilde p>1$ so small that $H^{\sigma ,2}$ embeds into $H^{\tilde \sigma, 2 \tilde p}$
and hence
\begin{equation*}
 \|g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(\cdot, w)\|_{\W[\tilde \sigma,p]} 
  \leq  C \frac{\|\gamma'(\cdot + \tau_1 w) - \gamma'(\cdot + \tau_2 w )\|^2_{\W[\sigma,2]}}{\abs w^\a}.
\end{equation*}
Thus, recalling~\eqref{eq:Ds},
\begin{align*}
  \int_{-1/2}^{1/2}\|g^{(\a,\beta)}_{s_1, \tau_1, \tau_2}(\cdot,w)\|_{\W[\tilde \sigma,p]} \d w&\leq C
  \int_{-1/2}^{1/2} \frac{\|\gamma'(\cdot + \tau_1 w) - \gamma'(\cdot + \tau_2 w )\|^2_{\Lp[2]} }{\abs w^\alpha} dw
  \\
  & \quad + C
  \int_{-1/2}^{1/2} \frac {\|D^{\sigma+1}\gamma(\cdot + \tau_1 w) - D^{\sigma+1}\gamma(\cdot + \tau_2 w )\|^2_{\Lp[2]} 
   }{\abs w^\alpha} dw
  \\
&\leq C
\int_{-1/2}^{1/2} \frac{\|\gamma'(\cdot) - \gamma'(\cdot + (\tau_2 - \tau_1) w )\|^2_{\Lp[2]} }{\abs w^\alpha} dw
 \\
& \quad + C
  \int_{-1/2}^{1/2} \frac {\|D^{\sigma+1}\gamma(\cdot) 
- D^{\sigma+1} \gamma(\cdot + (\tau_2 - \tau_1) w )\|^2_{\Lp[2]} }{\abs w^\alpha} dw
\\
&\leq C |\tau_2 - \tau_1|
\int_{-1}^{1} \frac{\|\gamma'(\cdot) - \gamma'(\cdot +  w )\|^2_{\Lp[2]} }{\abs w^\alpha} dw
 \\
& \quad + C |\tau_2-\tau_1|
  \int_{-1}^{1} \frac {\|D^{\sigma+1}\gamma(\cdot) - D^{\sigma+1} \gamma(\cdot +  w )\|^2_{\Lp[2]} }{\abs w^\alpha} dw
\\
& \leq C \|\gamma'\|_{\W[(\a-1)/2,2]}^2 
 + C \|D^{\sigma+1}\gamma\|_{\W[(\a-1)/2,2]}^2 \leq C.
\end{align*}
This proves Lemma~\ref{lem:basicEstimate}.
\end{proof}

\begin{proof}[Theorem~\ref{thm:rsp}]
 Recall that any finite-energy curve belongs to $\W[(\a+1)/2,2]$ by~\cite{blatt:bre}.
 
 Let us assume that $\gamma \in H^{\frac {\alpha + 1} 2 + \sigma,2} (\mathbb R / \mathbb Z, \mathbb R^n)$
 for $\sigma \geq 0$ is a stationary point of the energy $\E + \lambda\length$.
 As the first variation of the length functional gives rise to a linear lower order term,
 Proposition~\ref{prop:formOfQ} also applies to
 \[ \tQ(\g,h) := \a\Q(\g,h)+\lambda\int_{\R/\Z}\sp{\dg,\dh}. \]
 In the case that $\sigma=0$ we get from the Euler-Lagrange Equation~\eqref{eq:ele} using the decomposition~\eqref{eq:decomposE} and Proposition~\ref{prop:RR} 
 \begin{equation*}
  \tQ( \gamma, \cdot)
  \in \left( H^{{3}/2+\eps,2} \right)^{\ast}
 \end{equation*}
 for any $\eps>0$.
 Using Proposition~\ref{prop:formOfQ} we hence get
 \begin{equation*}
   (q_k |k|^{\alpha+1-3/2-\eps} \hat \gamma (k))_{k\in \mathbb Z} \in \ell^2.
 \end{equation*}
 Together with the fact that $q_k$ converge to a positive constant as $k \rightarrow \infty$
 we get $ \left(|k|^{\alpha+1-3/2-\eps} \hat \gamma (k)\right)_{k \in \mathbb Z} \in \ell^2$
 and hence
  \begin{equation*}
    \gamma \in H^{\tfrac {\alpha +1 } 2 + \tfrac {\alpha -2 } 2 -\eps,2}
    (\mathbb R / \mathbb Z, \mathbb R^n).
  \end{equation*}
 For $\sigma >0$ we get using Proposition~\ref{prop:RR} 
 \begin{equation*}
  \tQ( \gamma, \cdot)
  \in \left( H^{\frac {3}2 - \hat \sigma } \right)^*\qquad\text{for all }\hat\sigma<\sigma
 \end{equation*} 
and arguing as above
\begin{equation*}
 \gamma \in H^{\br{\tfrac {\alpha +1 } 2 + \hat \s}+ \tfrac {\alpha -2 } 2,2}
  (\mathbb R / \mathbb Z, \mathbb R^n)
\end{equation*}
for all $\hat \s < \sigma$.

If we now initially assume that $\gamma \in H^{\frac {\alpha +1} 2 ,2}$ we deduce by induction
and since $\tfrac {\alpha-2} 2 >0$ that
 \begin{equation*}
  \gamma \in H^{s,2}(\mathbb R / \mathbb Z, \mathbb R^n)
 \end{equation*}
for all $s \in \mathbb R$ and thus $\gamma \in C^{\infty}(\mathbb R / \mathbb Z, \mathbb R^n)$.
This proves Theorem~\ref{thm:rsp}
\end{proof}

\begin{appendix}
