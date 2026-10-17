---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-004-5-classical-monte-carlo
section_title: "Classical Monte Carlo"
section_number: 5
pages: 9-15
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.981
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
[]{#MC label="MC"} Consider the Mtd given by $$\label{a} a(u, \cdot) = \int_{S_V}\int_{S_V}
          \pi_{U|V}(\cdot|v') r(v,dv') \pi_{V|U}(v|u) \, \nu(dv) \,, \; u \in S_U \,,$$ where $r(v,\cdot), \, v \in S_V$ is an Mtf on $S_V$ with invariant pdf $\pi_V(\cdot).$ We will show in this section that this form has utility beyond constructing sandwich algorithms. Indeed, the $k$-step Mtd of a DA algorithm (or a sandwich algorithm) can be re-expressed in the form [\[a\]](#a){reference-type="eqref" reference="a"}. This motivates the development of a general method for estimating the integral $\int_{S_U} a(u,u) \,
        \mu(du)$, which is the main topic of this section.

We begin by showing how $p^{(k)}(u,\cdot), \, u \in S_U$ can be written in the form [\[a\]](#a){reference-type="eqref" reference="a"}. The case $k=1$ is trivial. Indeed, if $r(v,\cdot)$ is taken to be the kernel of the identity operator, then $a(u,\cdot) = p(u,\cdot)$. Define an Mtd $q(v,\cdot), \, v\in S_V$ by $$q(v,\cdot) = \int_{S_U} \pi_{V|U}(\cdot|u) \pi_{U|V}(u|v) \, \mu(du),$$ and let $q^{(k)}(v,\cdot), \, k \geq 1$ denote the corresponding $k$-step Mtd. If we let $$r(v,dv')= q^{(k-1)}(v,v') \, \nu(dv'), \, v \in S_V$$ for $k \geq 2,$ then $a(u,\cdot) = p^{(k)}(u,\cdot)$. Next, consider the sandwich Mtd $\tilde{p}^{(k)}(u,\cdot), \, u \in
        S_U$. Again, the $k=1$ case is easy. Taking $$r(v,\cdot) = s(v,\cdot)$$ yields $a(u,\cdot) = \tilde{p}(u,\cdot)$. Now let $$\tilde{q}(v,\cdot) = \int_{S_U} \int_{S_V} s(v',\cdot)
        \pi_{V|U}(v'|u) \pi_{U|V}(u|v)\, \nu(dv')\, \mu(du) \,,$$ and denote the corresponding $k$-step transition function by $\tilde{q}^{(k)}(v,\cdot)$. Then taking $$r(v,\cdot) = \int_{S_V} \tilde{q}^{(k-1)}(v',\cdot) s(v,dv')$$ when $k \geq 2$ yields $a(u,\cdot) = \tilde{p}^{(k)}(u,\cdot).$

The following proposition shows that, when $P$ is trace-class, $\int_{S_U} a(u,u) \, \mu(du)$ is finite.

::: proposition
[]{#traceclassA label="traceclassA"} $\int_{S_U} a(u,u) \, \mu(du) < \infty.$
:::

::: proof
*Proof.* That $\int_{S_U} a(u,u) \, \mu(du) < \infty$ is equivalent to $$\label{atraceclass0}
        \int_{S_U} \int_{S_V} \bigg( \int_{S_V} \frac{\pi_{U,V}(u,v')}{\pi_U(u)\pi_V(v')} r(v,dv') \bigg) \bigg( \frac{\pi_{U,V}(u,v)}{\pi_U(u)\pi_V(v)} \bigg) \pi_U(u) \pi_V(v) \, \nu(dv) \, \mu(du) < \infty \,.$$ Note that $$\label{atraceclass1}
        \int_{S_U} \bigg( \frac{\pi_{U,V}(u,v)}{\pi_U(u)\pi_V(v)} \bigg)^2 \pi_U(u) \pi_V(v) \, \mu(du)\nu(dv) = \int_{S_U} p(u,u) \, \mu(du) < \infty \,,$$ and by Jensen's inequality, $$\label{atraceclass2}
        \begin{aligned}
        &\int_{S_U} \int_{S_V} \bigg( \int_{S_V} \frac{\pi_{U,V}(u,v')}{\pi_U(u)\pi_V(v')} r(v,dv') \bigg)^2 \pi_U(u) \pi_V(v) \,\nu(dv) \, \mu(du) \\
        &\leq \int_{S_U} \int_{S_V} \int_{S_V} \bigg( \frac{\pi_{U,V}(u,v')}{\pi_U(u)\pi_V(v')} \bigg)^2 r(v,dv') \pi_U(u) \pi_V(v) \,\nu(dv) \, \mu(du) \\
        &= \int_{S_U} \int_{S_V} \bigg( \frac{\pi_{U,V}(u,v')}{\pi_U(u)\pi_V(v')} \bigg)^2 \pi_U(u) \pi_V(v') \,\nu(dv') \, \mu(du) \\
        &= \int_{S_U} p(u,u) \, \mu(du) \\
        & < \infty \,.
        \end{aligned}$$ The inequality [\[atraceclass0\]](#atraceclass0){reference-type="eqref" reference="atraceclass0"} follows from [\[atraceclass1\]](#atraceclass1){reference-type="eqref" reference="atraceclass1"}, [\[atraceclass2\]](#atraceclass2){reference-type="eqref" reference="atraceclass2"}, and the Cauchy-Schwarz inequality. ◻
:::

Combining Proposition [\[traceclassA\]](#traceclassA){reference-type="ref" reference="traceclassA"} and Theorem [\[basic\]](#basic){reference-type="ref" reference="basic"} leads to the following result: If $P$ is trace-class and $\tilde{p}(u,\cdot)$ is representable, then $\tilde{P}$ is also trace-class. This is a generalization of @khare2011spectral's [-@khare2011spectral] Theorem 1, which states that, under a condition on $s(v,dv')$ that implies representability, the trace-class-ness of $P$ implies that of $\tilde{P}$.

We now develop a classical Monte Carlo estimator of $\int_{S_U} a(u,u) \, \mu(du)$. Let $\omega:S_V \to
        [0,\infty)$ be a pdf that is almost everywhere positive. We will exploit the following representation of the integral of interest: $$\label{rep}
          \int_{S_U} a(u,u) \, \mu(du) = \int_{S_V} \int_{S_U} \bigg(\frac{\pi_{V|U}(v|u)}{\omega(v)}\bigg) \Big(\int_{S_V} \pi_{U|V}(u|v') r(v,dv') \Big) \omega(v) \, \mu(du) \,\nu(dv) \,.$$ Clearly, $$\eta(u,v) := \Big(\int_{S_V} \pi_{U|V}(u|v') r(v,dv') \Big)
        \omega(v)$$ defines a pdf on $S_U \times S_V$, and if $(U^*,V^*)$ has joint pdf $\eta(\cdot,\cdot)$, then $$\int_{S_U} a(u,u) \, \mu(du) = \mathbb{E} \bigg(
        \frac{\pi_{V|U}(V^*|U^*)}{\omega(V^*)} \bigg) \,.$$ Therefore, if $\{(U^*_i,V^*_i)\}_{i=1}^{N}$ are iid random elements from $\eta(\cdot,\cdot)$, then $$\label{estimator}
           \frac{1}{N} \sum_{i=1}^{N} \frac{\pi_{V|U}(V^*_i|U^*_i)}{\omega(V^*_i)}$$ is a strongly consistent and unbiased estimator of $\int_{S_U}
        a(u,u) \, \mu(du)$. This is the Monte Carlo formula that is central to our discussion.

Of course, we are mainly interested in the cases $a(u,\cdot) =
        p^{(k)}(u,\cdot)$ or $a(u,\cdot) = \tilde{p}^{(k)}(u,\cdot)$. We now develop algorithms for drawing from $\eta(\cdot,\cdot)$ in these two situations. First, assume $a(u,\cdot) =
        p^{(k)}(u,\cdot)$. If $k=1$, then $r(u,\cdot)$ is the kernel of the identity operator, and $$\eta(u,v) = \pi_{U|V}(u|v) \omega(v) \,.$$ If $k \ge 2$, then $r(v,dv') = q^{(k-1)}(v,v') \, dv'$, and $$\eta(u,v) = \Big( \int_{S_V} \pi_{U|V}(u|v') q^{(k-1)}(v,v')
          \, \nu(dv') \Big) \omega(v) = \Big( \int_{S_U} p^{(k-1)}(u',u)
          \pi_{U|V}(u'|v) \, \mu(du') \Big) \omega(v) \,.$$ Thus, when $k \ge 2$, we can draw from $\eta(u,v)$ as follows: Draw $V^* \sim \omega(\cdot)$, then draw $U' \sim
        \pi_{U|V}(\cdot|v^*)$, then draw $U^* \sim
        p^{(k-1)}(u',\cdot)$, and return $(u^*,v^*)$. Of course, we can draw from $p^{(k-1)}(u',\cdot)$ by simply running $k-1$ iterations of the original DA algorithm from starting value $u'$. We formalize all of this in Algorithm 1.

.2truecm

------------------------------------------------------------------------

height.5pt .2truecm

1.  Draw $V^*$ from $\omega(\cdot)$.

2.  Given $V^*=v^*,$ draw $U'$ from $\pi_{U|V}(\cdot|v^*)$.

3.  If $k=1$, set $U^*=U'$. If $k \geq 2$, given $U'=u'$, draw $U^*$ from $p^{(k-1)}(u', \cdot)$ by running $k-1$ iterations of the DA algorithm.

-.1truecm

------------------------------------------------------------------------

height.5pt .4truecm

Similar arguments lead to the following algorithm for the sandwich algorithm

.2truecm

------------------------------------------------------------------------

height.5pt .2truecm

1.  Draw $V^*$ from $\omega(\cdot)$.

2.  Given $V^*=v^*$, draw $V'$ from $s(v^*,\cdot)$.

3.  Given $V'=v'$ draw $U'$ from $\pi_{U|V}(\cdot|v')$.

4.  If $k=1$, set $U^*=U'$. If $k \geq 2$, given $U'=u'$, draw $U^*$ from $\tilde{p}^{(k-1)}(u',
                      \cdot)$ by running $k-1$ iterations of the sandwich algorithm.

-.1truecm

------------------------------------------------------------------------

height.5pt .4truecm It is important to note that we do not need to know the representing conditionals $\pi_{U|\tilde{V}}(\cdot|v)$ and $\pi_{\tilde{V}|U}(\cdot|u)$ from [\[representable\]](#representable){reference-type="eqref" reference="representable"} in order to run Algorithm 1S.

As with all classical Monte Carlo techniques, a key element in successful implementation is a finite variance. Define $$D^2 = \mathrm{var} \bigg(
        \frac{\pi_{V|U}(V^*|U^*)}{\omega(V^*)} \bigg) \,.$$ Of course, $D^2 < \infty$ if and only if $$\label{moment2} \int_{S_V} \int_{S_U}
          \bigg(\frac{\pi_{V|U}(v|u)}{\omega(v)}\bigg)^2 \eta(u,v) \,
          \mu(du) \,\nu(dv) < \infty \,.$$ The following theorem provides a sufficient condition for finite variance.

::: theorem
[]{#secondmoment label="secondmoment"} The variance, $D^2$, is finite if $$\label{momentcond}
        \int_{S_V} \int_{S_U} \frac{\pi_{V|U}^3(v|u) \pi_{U|V}(u|v)} {\omega^2(v)} \, \mu(du) \,\nu(dv) < \infty.$$
:::

::: proof
*Proof.* First, note that [\[moment2\]](#moment2){reference-type="eqref" reference="moment2"} is equivalent to $$\int_{S_V} \int_{S_U} \bigg(\frac{\pi^2_{V|U}(v|u)}{\pi_V(v)\omega(v)}\bigg) \bigg( \frac{\int_{S_V} \pi_{U|V}(u|v') r(v,dv')}{\pi_U(u)} \bigg) \pi_U(u)\pi_V(v) \, \mu(du)\,\nu(dv) < \infty.$$ Now, it follows from [\[momentcond\]](#momentcond){reference-type="eqref" reference="momentcond"} that $$\label{moment2.1}
        \int_{S_V} \int_{S_U} \bigg(\frac{\pi^2_{V|U}(v|u)}{\pi_V(v)\omega(v)}\bigg)^2 \pi_U(u)\pi_V(v) \, \mu(du)\,\nu(dv) < \infty.$$ Moreover, by Jensen's inequality, $$\label{moment2.2}
        \begin{aligned}
        &\int_{S_V} \int_{S_U} \bigg( \frac{\int_{S_V} \pi_{U|V}(u|v') r(v,dv')}{\pi_U(u)} \bigg)^2 \pi_U(u)\pi_V(v) \, \mu(du)\,\nu(dv) \\
        & \leq \int_{S_V} \int_{S_U} \int_{S_V} \bigg( \frac{\pi_{U|V}(u|v')}{\pi_U(u)} \bigg)^2 r(v,dv') \pi_U(u)\pi_V(v) \, \mu(du)\,\nu(dv) \\
        &= \int_{S_V} \int_{S_U} \bigg( \frac{\pi_{U|V}(u|v')}{\pi_U(u)} \bigg)^2 \pi_U(u)\pi_V(v') \, \mu(du)\,\nu(dv') \\
        &= \int_{S_U} p(u,u) \, \mu(du) \\
        & < \infty.
        \end{aligned}$$ The conclusion now follows from [\[moment2.1\]](#moment2.1){reference-type="eqref" reference="moment2.1"}, [\[moment2.2\]](#moment2.2){reference-type="eqref" reference="moment2.2"}, and Cauchy-Schwarz. ◻
:::

Theorem [\[secondmoment\]](#secondmoment){reference-type="ref" reference="secondmoment"} implies that an $\omega(\cdot)$ with heavy tails is more likely to result in finite variance (which is not surprising). It might seem natural to take $\omega(\cdot) = \pi_V(\cdot)$. However, in practice, we are never able to draw from $\pi_V(\cdot)$. (If we could do that, we would not need MCMC.) Moreover, setting $\omega(\cdot)$ to be $\pi_V(\cdot)$ does not always result in a finite variance. On the other hand, it can be beneficial to use $\omega(\cdot)$s resembling $\pi_V(\cdot)$, as we argue in Section [\[efficiency\]](#efficiency){reference-type="ref" reference="efficiency"}.

When an appropriate $\omega(\cdot)$ is difficult to find, one can construct an alternative Monte Carlo estimator as follows. Let $\psi:S_U \to [0,\infty)$ be a pdf that is positive almost everywhere. The following dual of [\[rep\]](#rep){reference-type="eqref" reference="rep"} may also be used to represent $\int_{S_U}a(u,u) \, \mu(du)$: $$\int_{S_U} a(u,u) \, \mu(du) = \int_{S_U}
          \int_{S_V} \int_{S_V} \frac{\pi_{U|V}(u|v)}{\psi(u)}
          r(v',dv) \pi_{V|U}(v'|u) \psi(u) \, \nu(dv') \, \mu(du) \,.$$ Now suppose that $\{(U^*_i,V^*_i)\}_{i=1}^N$ are iid from $$\zeta(u,v) \, \mu(du) \, \nu(dv) = \bigg( \int_{S_V} r(v',dv)
        \pi_{V|U}(v'|u) \, \nu(dv') \bigg) \psi(u) \, \mu(du) \,.$$ The analogue of [\[estimator\]](#estimator){reference-type="eqref" reference="estimator"} is the following classical Monte Carlo estimator of $\int_{S_U} a(u,u) \, \mu(du)$: $$\label{estimator2} \frac{1}{N} \sum_{i=1}^{N}
          \frac{\pi_{U|V}(U^*_i|V^*_i)}{\psi(U^*_i)} \,.$$ We now state the obvious analogues of Algorithms 1 and 1S.

.2truecm

------------------------------------------------------------------------

height.5pt .2truecm

1.  Draw $U^*$ from $\psi(\cdot)$.

2.  If $k=1$, set $U'=U^*$. If $k \geq 2$, given $U^*=u^*$, draw $U'$ from $p^{(k-1)}(u^*, \cdot)$.

3.  Given $U'=u'$, draw $V^*$ from $\pi_{V|U}(\cdot|u')$.

-.1truecm

------------------------------------------------------------------------

height.5pt .4truecm

.2truecm

------------------------------------------------------------------------

height.5pt .2truecm

1.  Draw $U^*$ from $\psi(\cdot)$.

2.  If $k=1$, set $U'=U^*$. If $k \geq 2$, given $U^*=u^*$, draw $U'$ from $\tilde{p}^{(k-1)}(u^*, \cdot)$.

3.  Given $U'=u'$, draw $V'$ from $\pi_{V|U}(\cdot|u')$.

4.  Given $V'=v'$, draw $V^*$ from $s(v',\cdot)$.

-.1truecm

------------------------------------------------------------------------

height.5pt .4truecm

Let $D'^2$ be the variance of $\pi_{U|V}(U^*|V^*)/\psi(U^*)$ under $\zeta$. To ensure that it's finite, we only need $$\label{moment2dual} \int_{S_U} \int_{S_V}
          \int_{S_V} \bigg(\frac{\pi_{U|V}(u|v)}{\psi(u)}\bigg)^2
          r(v',dv) \pi_{V|U}(v'|u) \psi(u) \,\nu(dv') \, \mu(du) <
          \infty \,.$$ The following result is the analogue of Theorem [\[secondmoment\]](#secondmoment){reference-type="ref" reference="secondmoment"}.

::: corollary
[]{#secondmomentdual label="secondmomentdual"} The variance, $D'^2$, is finite if $$\label{momentconddual} \int_{S_U}
            \int_{S_V} \frac{\pi_{U|V}^3(u|v) \pi_{V|U}(v|u)}
            {\psi^2(u)} \,\nu(dv) \, \mu(du) < \infty \,.$$
:::

::: proof
*Proof.* Note that the left hand side of [\[moment2dual\]](#moment2dual){reference-type="eqref" reference="moment2dual"} is equal to $$\int_{S_U} \int_{S_V} \bigg(\int_{S_V}
                \frac{\pi_{U|V}^2(u|v)}{\psi(u)\pi_U(u)} r(v',dv)
                \bigg) \bigg( \frac{\pi_{V|U}(v'|u)}{\pi_V(v')} \bigg)
                \pi_U(u)\pi_V(v') \,\nu(dv') \, \mu(du) \,.$$ Apply the Cauchy-Schwarz inequality, then utilize Jensen's inequality to get rid of $r(v',dv),$ and finally make use of [\[momentconddual\]](#momentconddual){reference-type="eqref" reference="momentconddual"} and the fact that $P$ is trace-class. ◻
:::

Typically, it's easy to select a good sampling density $\omega(\cdot)$ for Algorithm 1 when $S_V$ is low dimensional, or to select a good $\psi(\cdot)$ for Algorithm 2 when $S_U$ is low dimensional. For DA algorithms used in Bayesian models, it's often the case that $\mbox{dim} (S_U) = p$, and $\mbox{dim} (S_V) = n$, where $p$ and $n$ are, respectively, the number of unknown parameters in the model and the number of observations. When this is the case, the estimator [\[estimator\]](#estimator){reference-type="eqref" reference="estimator"} is likely to be efficient when $n$ is small, while [\[estimator2\]](#estimator2){reference-type="eqref" reference="estimator2"} is likely to be efficient when $p$ is small.

Suppose that we have obtained estimates of $s_k$ and $s_{k-1}$ based on [\[estimator\]](#estimator){reference-type="eqref" reference="estimator"} or [\[estimator2\]](#estimator2){reference-type="eqref" reference="estimator2"}, call them $s^*_k$ and $s^*_{k-1}$. Then $u^*_k = (s^*_k-1)^{1/k}$ and $l^*_k = (s^*_k-1)/(s^*_{k-1}-1)$ serve as point estimates of $u_k$ and $l_k$, respectively. When our estimators have finite variances, we can acquire, via the delta method, confidence intervals for $u_k$ and $l_k$. Assume that a confidence interval for $l_k$ is $(a_k,b_k)$ and a confidence interval for $u_k$ is $(c_k, d_k)$, then $(a_k, d_k)$ is an interval estimate for $\lambda_1$. Interval estimates of $\tilde{\lambda}_1$ can be derived in a similar fashion.

It's worth pointing out that $u_k$ is a nontrivial upper bound on $\lambda_1 \in [0,1)$ only if $s_k < 2$. The parameter $k$ can be determined sequentially. Take Algorithm 1 for example. Suppose that we have drawn $N$ iid copies of $(U^*, V^*)$ from $\eta(\cdot,\cdot)$ with $a(\cdot, \cdot) = p^{(k)}(\cdot,\cdot)$, but find that $s^*_k$ is not small enough for our purposes. Since $s_k$ is decreasing in $k$, we wish to increase $k$ by a positive integer $j$. To draw $(U^{**}, V^{**})$ from $\eta(\cdot,\cdot)$ with $a(\cdot, \cdot) = p^{(k+j)}(\cdot,\cdot)$, we only need to set $V^{**} = V^*$, and draw $U^{**}$ from $p^{(j)}(U^*, \cdot)$. This procedure can be repeated until the estimated power sum $s^*_{k+j}$ is decreased to a satisfactory value. More guidance on the choice of $k$ can be found in the next section.
