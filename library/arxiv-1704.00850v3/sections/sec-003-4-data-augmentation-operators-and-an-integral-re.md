---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-003-4-data-augmentation-operators-and-an-integral-re
section_title: "Data augmentation operators and an integral representation of sk"
section_number: 4
pages: 7-9
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.976
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
[]{#daint label="daint"}

In order to formally define DA, we require a second measure space. Let $(S_V, \mathcal{V}, \nu)$ be a $\sigma$-finite measure space such that $\mathcal{V}$ is countably generated. Also, rename $S$ and $\pi$, $S_U$ and $\pi_U$, respectively. Consider the random element $(U,V)$ taking values in $S_U
        \times S_V$ with joint pdf $\pi_{U,V}(\cdot,\cdot).$ Suppose the marginal pdf of $U$ is the target, $\pi_U(\cdot)$, and denote the marginal pdf of $V$ by $\pi_V(\cdot).$ We further assume that the conditional densities $\pi_{U|V}(u|v) :=
        \pi_{U,V}(u,v)/\pi_V(v)$ and $\pi_{V|U}(v|u) :=
        \pi_{U,V}(u,v)/\pi_U(u)$ are well defined almost everywhere in $S_U \times S_V.$ Recall that $\Phi$ is a Markov chain on the state space $S_U$ with Mtd $p(u,\cdot),\, u \in S_U.$ We call $\Phi$ a DA chain, and accordingly, $P$ a DA operator, if $p(u,\cdot)$ can be expressed as $$\label{DAmtd} p(u,\cdot) = \int_{S_V}
          \pi_{U|V}(\cdot|v) \pi_{V|U}(v|u) \, \nu(dv) \,.$$ Such a chain is necessarily reversible with respect to $\pi_U(\cdot)$. To simulate it, in each iteration, one first draws the latent element $V$ using $\pi_{V|U}(\cdot|u)$, where $u \in S_U$ is the current state, and then given $V=v$, one updates the current state according to $\pi_{U|V}(\cdot|v)$. A DA operator is non-negative, and thus possesses a positive spectrum [@liu:wong:kong:1994].

Assume that [\[DAmtd\]](#DAmtd){reference-type="eqref" reference="DAmtd"} holds. Given $k \in \mathbb{N}$, the power sum of $P$'s eigenvalues, $s_k,$ if well defined, is closely related to the diagonal components of $p^{(k)}(\cdot,\cdot).$ Just as we can calculate the sum of the eigenvalues of a matrix by summing its diagonals, we can obtain $s_k$ by evaluating $\int_{S_U}
        p^{(k)}(u,u) \, \mu(du)$. Here is a formal statement.

::: theorem
[]{#basic label="basic"} The DA operator $P$ is trace-class if and only if $$\label{traceclass}
        \int_{S_U} p(u,u) \, \mu(du) < \infty \,.$$ If [\[traceclass\]](#traceclass){reference-type="eqref" reference="traceclass"} holds, then for any positive integer $k,$ $$\label{sum=int} s_k :=
                  \sum_{i=0}^{\kappa} \lambda_i^k = \int_{S_U}
                  p^{(k)}(u,u) \, \mu(du) \,.$$
:::

Theorem [\[basic\]](#basic){reference-type="ref" reference="basic"} is a combination of a few standard results in classical functional analysis. It is fairly well-known, but we were unable to find a complete proof in the literature. An elementary proof is given in the appendix for completeness. For a more modern version of the theorem, see [@brislawn1988kernels].

It is often possible to exploit Theorem [\[basic\]](#basic){reference-type="ref" reference="basic"} even when $\Phi$ is *not* a DA Markov chain. Indeed, suppose that $\Phi$ is reversible, but is not a DA chain. Then $P$ is not a DA operator, but $P^2$, in fact, is. (Just take $\pi_{U,V}(u,v) = \pi_U(u)p(u,v)$.) If, in addition, $P$ is Hilbert-Schmidt, which is equivalent to $$\int_{S_U} \int_{S_U} \frac{(p(u,u'))^2 \pi_U(u)}{\pi_U(u')}
        \, \mu(du) \, \mu(du') < \infty \,,$$ then by a simple spectral decomposition [see e.g. @helmberg2014introduction §28 Corollary 2.1] one can show that $P^2$ is trace-class, and its eigenvalues are precisely the squares of the eigenvalues of $P$. In this case, the spectral gap of $P$ can be expressed as $1$ minus the square root of $P^2$'s second largest eigenvalue. Moreover, by Theorem [\[basic\]](#basic){reference-type="ref" reference="basic"}, for $k \in \mathbb{N},$ the sum of the $k$th power of $P^2$'s eigenvalues is equal to $\int_{S_U}
        p^{(2k)}(u,u) \, \mu(du) < \infty$.

We now briefly describe the so-called sandwich algorithm, which is a variant of DA that involves an extra step sandwiched between the two conditional draws of DA [@liu1999parameter; @hobert2008theoretical]. Let $s(v,\cdot), \, v \in S_V$ be a Markov transition function (Mtf) with invariant density $\pi_V(\cdot)$. Then $$\label{sandwich} \tilde{p}(u,\cdot) =
          \int_{S_V}\int_{S_V} \pi_{U|V}(\cdot|v') s(v,dv')
          \pi_{V|U}(v|u) \nu(dv) \,, \; u \in S_U\,,$$ is an Mtd with invariant density $\pi_U(\cdot)$. This Mtd defines a new Markov chain, call it $\tilde{\Phi}$, which we refer to as a sandwich version of the original DA chain, $\Phi$. To simulate $\tilde{\Phi}$, in each iteration, the latent element is first drawn from $\pi_{V|U}(\cdot|u)$, and then updated using $s(v,\cdot)$ before the current state is updated according to $\pi_{U|V}(\cdot|v')$. Sandwich chains often converge much faster than their parent DA chains [see e.g. @khare2011spectral].

Of course, $\tilde{p}(u,\cdot)$ defines a Markov operator on $L^2(\pi_U)$, which we refer to as $\tilde{P}$. It is easy to see that, if the Markov chain corresponding to $s(v,\cdot)$ is reversible with respect to $\pi_V(\cdot)$, then $\tilde{p}(u,\cdot)$ is reversible with respect to $\pi_U(\cdot)$. Thus, when $s(v,\cdot)$ is reversible, $\tilde{P}^2$ is a DA operator. Interestingly, it turns out that $\tilde{p}(u,\cdot)$ can often be re-expressed as the Mtd of a DA chain, in which case $\tilde{P}$ itself is a DA operator. Indeed, a sandwich Mtd $\tilde{p}(u,\cdot)$ is said to be "representable" if there exists a random element $\tilde{V}$ in $S_V$ such that $$\label{representable} \tilde{p}(u,u') =
          \int_{S_V} \pi_{U|\tilde{V}}(u'|v) \pi_{\tilde{V}|U}(v|u) \,
          \nu(dv) \,,$$ where $\pi_{U|\tilde{V}}(u'|v)$ and $\pi_{\tilde{V}|U}(v|u)$ have the apparent meanings [see, e.g. @hobe:2011]. It is shown in Proposition [\[traceclassA\]](#traceclassA){reference-type="ref" reference="traceclassA"} in Section [\[MC\]](#MC){reference-type="ref" reference="MC"} that when $P$ is trace-class and $\tilde{p}(u,\cdot)$ is representable, $\tilde{P}$ is also trace-class. In this case, let $\{\tilde{\lambda}_i\}_{i=0}^{\tilde{\kappa}}$ be the decreasingly ordered positive eigenvalues of $\tilde{P}$ taking into account multiplicity, where $0 \leq \tilde{\kappa} \leq
        \infty$. Then $\tilde{\lambda}_0 = 1$, and $\tilde{\lambda}_1
        \leq \lambda_1 < 1$ [@hobert2008theoretical]. For a positive integer $k,$ we will denote $\sum_{i=0}^{\tilde{\kappa}} \tilde{\lambda}_i^k$ by $\tilde{s}_k$. Henceforth, we assume that $\tilde{p}(u,\cdot)$ is representable and we treat $\tilde{P}$ as a DA operator.

It follows from Theorem [\[basic\]](#basic){reference-type="ref" reference="basic"} that in order to find $s_k$ or $\tilde{s}_k$, all we need to do is evaluate $\int_{S_U} p^{(k)}(u,u) \,\mu(du)$ or $\int_{S_U}
        \tilde{p}^{(k)}(u,u) \,\mu(du),$ where $\tilde{p}^{(k)}(u,\cdot)$ is the $k$-step Mtd of the sandwich chain. Of course, calculating these integrals (in non-toy problems) is nearly always impossible, even for $k=1$. In the next section, we introduce a method of estimating these two integrals using classical Monte Carlo.

Throughout the remainder of the paper, we assume that $P$ is a DA operator with Mtd given by [\[DAmtd\]](#DAmtd){reference-type="eqref" reference="DAmtd"}, and that [\[traceclass\]](#traceclass){reference-type="eqref" reference="traceclass"} holds.
