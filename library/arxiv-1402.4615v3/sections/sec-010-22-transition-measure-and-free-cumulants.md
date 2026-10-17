---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-010-22-transition-measure-and-free-cumulants
section_title: "Transition measure and free cumulants"
section_number: 2.2
pages: 14-15
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.966
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#subsect:TransMeasure label="subsect:TransMeasure"} Kerov [@KerovTransitionMeasure] introduced the notion of *transition measure* of a Young diagram. This is a probability measure $\mu_\lambda$ on the real line $\mathbb{R}$ associated to $\lambda$ and defined by its Cauchy transform: $$G_{\mu_\lambda}(z) = \int_\mathbb{R}\frac{d\mu_\lambda(x)}{z-x} =
\frac{\prod_{o \in \mathbb{O}_\lambda} z-o}{\prod_{i \in \mathbb{I}_\lambda} z-i}.$$ In particular, transition measure is supported on $\mathbb{I}_\lambda$. Besides, its *moment generating series* is given by $$\sum_{k \ge 0} M^{(1)}_k(\lambda) \, t^k := \frac{1}{t} \, G_{\mu_\lambda}(1/t)
=\frac{\prod_{o \in \mathbb{O}_\lambda} 1-o\, t}{\prod_{i \in \mathbb{I}_\lambda} 1-i\, t},$$ where $M^{(1)}_k(\lambda):= \int_\mathbb{R}x^k d\mu_\lambda(x)$ is the *$k$-th moment* of $\mu_\lambda$. It is easily seen that, for any diagram, $M^{(1)}_0(\lambda)=1$ and $M^{(1)}_1(\lambda)=0$. This generating series can be rewritten as $$\begin{gathered}
    \sum_{k \ge 0} M^{(1)}_k(\lambda) \, t^k = \exp\left( \sum_{i \in \mathbb{I}_\lambda}\sum_{k \ge 1}
\frac{i^k}{k}\, t^k - \sum_{o \in \mathbb{O}_\lambda}\sum_{k \ge 1} \frac{o^k}{k}\, t^k \right) \\
= \exp \left( \sum_{k \ge 1} \frac{1}{k} p_k(\mathbb{I}_\lambda -\mathbb{O}_\lambda)\, t^k \right).
\end{gathered}$$ This implies that $M^{(1)}_k(\lambda)=h_k(\mathbb{I}_\lambda -\mathbb{O}_\lambda)$, where $h_k$ is the complete symmetric function of degree $k$; see [@Macdonald1995 page 25].

::: corollary
The family $(M^{(1)}_k)_{k \geq 2}$ forms an algebraic basis of $\Lambda_{(1)}^\star$.
:::

We will also be interested in free cumulants $R^{(1)}_k(\lambda)$ of the transition measure $\mu_\lambda$. They are defined by their generating series $$K_\lambda(t) =t^{-1} + \sum_{k \ge 1} R^{(1)}_k(\lambda) \, t^{k-1},$$ where $K_\lambda$ is the (formal) compositional inverse of $G_{\mu_\lambda}$. The fact that $M^{(1)}_1(\lambda)=0$ implies that either $R^{(1)}_1(\lambda)=0$ (for all diagrams $\lambda$).

As explained by Lassalle [@Lassalle2009 Section 5], they can be expressed as $$\label{eq:FreeCumulantsLassalle}
R^{(1)}_k(\lambda) = e_k^\star(\mathbb{I}_\lambda -\mathbb{O}_\lambda)$$ for some homogeneous symmetric function $e_k^\star$ of degree $k$. Functions $e_k^\star$ form an algebraic basis of symmetric functions, hence we have the following corollary of Proposition [\[prop:pk_basis\]](#prop:pk_basis){reference-type="ref" reference="prop:pk_basis"}.

::: corollary
$(R^{(1)}_k)_{k \geq 2}$ is an algebraic basis of ring of polynomial functions on the set of Young diagrams.
:::

::: remark
Free cumulants are classical objects in free probability theory [@Voiculescu1986; @SpeicherFreeCumulants], but considering them outside this context may seem strange at first sight. The relevance of free cumulants of the transition measure of Young diagrams first appeared in the work of Biane [@Biane1998] and they have played an important role in asymptotic representation theory since then.
:::
