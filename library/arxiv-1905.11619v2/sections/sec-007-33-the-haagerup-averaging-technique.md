---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-007-33-the-haagerup-averaging-technique
section_title: "The Haagerup averaging technique"
section_number: 3.3
pages: 9-10
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.948
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an analysis of quantum Markov semi-groups."
---
We will show that under algebraic conditions gradient-$\mathcal{S}_p$ properties behave well under Haagerup averaging techniques. We believe this result is of independent interest, though we will not use it in the subsequent sections.

Let $\Lambda$ be a discrete group with group algebra $\mathbb{C}[\Lambda]$ and von Neumann algebra $(\mathcal{L}(\Lambda), \tau)$. We will identify $\Lambda$ with its image under the left regular representation. So for $\gamma \in \Lambda$ we will also write $\gamma$ for the associated unitary in $\mathcal{L}(\Lambda)$. Let $(\Phi_t)_{t \geq 0}$ be a quantum Markov semi-group on $\mathcal{L}(\Lambda)$. Consider the map, $$\label{Eqn=Average}
\Psi_t = \mathbb{E} \circ  (\Phi_t \otimes \textrm{id}) \circ \delta_\Lambda$$ where $\delta_\Lambda: \mathcal{L}(\Lambda) \rightarrow  \mathcal{L}(\Lambda) \overline{\otimes}\mathcal{L}(\Lambda)$ is the comultiplication $\delta_\Lambda: \gamma \mapsto \gamma \otimes \gamma$ and $\mathbb{E}$ is the conditional expectation of $\mathcal{L}(\Lambda) \overline{\otimes}\mathcal{L}(\Lambda)$ onto the image of $\delta_\Lambda$ (post-composed with the inverse of $\delta_{\Lambda}$ so that the range is contained in $\mathcal{L}(\Lambda)$). Then $\Psi_t$ is a completely positive Fourier multiplier with symbol $\varphi_t(\gamma) = \tau( \Phi_t(\gamma) \gamma^{-1}), \gamma \in \Gamma$.

::: lem
[]{#Lem=Average label="Lem=Average"} Let $\Psi_t: \mathcal{L}(\Lambda) \rightarrow \mathcal{L}(\Lambda), t \geq 0$ be unital completely positive Fourier multipliers (not necessarily a semi-group) and suppose that for every $\gamma \in \Lambda$ the limit $\Delta_0^\Psi(\gamma) :=  \lim_{t \searrow 0} \frac{1}{t} (\gamma -  \Psi_t(\gamma))$ exists. Then $\Delta_0^\Psi$ defines a preclosed (unbounded) operator on $\ell_2(\Gamma)$ with closure $\Delta^\Psi$. Moreover, $\exp(-t \Delta^\Psi)$ is a quantum Markov semi-group.
:::

::: proof
*Proof.* Since $\Delta_0^\Psi$ acts diagonally on $\ell_2(\Lambda)$ with respect to the basis $\gamma \in \Lambda$ it is preclosed. The remaining statements follow by following the constructions in [@JolissaintMartin] and [@CaspersSkalskiCMP Proposition 5.5]. Alternatively, there is the following short proof. Let $\varphi_t$ be the symbol of the Fourier multiplier $\Psi_t$ which is positive definite and $\varphi_t(e) = 1$. Consider the state $\mu_t$ on $\mathbb{C}[\Lambda]$ that maps $\gamma \in \Lambda$ to $\varphi_t(\gamma)$. Then $\Delta_0(\gamma) := \lim_{t \searrow 0} \frac{1}{t} ( \mu_t - \varepsilon )$ defines a generating functional on $\mathbb{C}[\Lambda]$ where $\varepsilon(\gamma) = 1, \gamma \in \Lambda$ is the counit (see [@DFSW Section 6.2] for generating functionals). Therefore $\nu_t := \exp(-t \Delta_0)$ defines a convolution semi-group of states on $\mathbb{C}[\Lambda]$. Since the Fourier multiplier $\Psi_t =   (\textrm{id}\otimes \nu_t)\circ \delta_\Lambda$ is a trace preserving ucp map it extends from $\mathbb{C}[\Lambda]$ to a quantum Markov semi-group on $\mathcal{L}(\Lambda)$ with generator $\Delta^{\Psi}$. ◻
:::

::: lem
Let $(\Phi_t)_{t \geq 0}$ be a quantum Markov semi-group on $\mathcal{L}(\Gamma)$ with generator $\Delta$ and assume $\mathbb{C}[\Gamma]$ is in the domain of $\Delta$. Consider $\Psi_t$ as in [\[Eqn=Average\]](#Eqn=Average){reference-type="eqref" reference="Eqn=Average"} and let $\Delta^\Psi$ be as in Lemma [\[Lem=Average\]](#Lem=Average){reference-type="ref" reference="Lem=Average"}. We have, $$\Delta^\Psi(\gamma)   =  \frac{d}{dt}\vert_{t = 0} \langle \Phi_t(\gamma) , \gamma \rangle  \gamma = \langle \Delta(\gamma), \gamma \rangle  \gamma, \qquad \gamma \in \Gamma \subseteq \mathbb{C}[\Gamma].$$
:::

::: proof
*Proof.* This is clear from the definitions. ◻
:::

The following theorem shows that under a domain condition on $\Delta$ we may average a quantum Markov semi-group to a semi-group of Fourier multipliers while retaining the property of being gradient-$\mathcal{S}_p$.

::: thm
Let $(\Phi_t)_{t \geq 0}$ be a quantum Markov semi-group on $\mathcal{L}(\Gamma)$ with generator $\Delta$ and assume $\mathbb{C}[\Gamma]$ is in the domain of $\Delta$. If $(\Phi_t)_{t \geq 0}$ is gradient-$\mathcal{S}_p$ then so is $\exp(-t \Delta^\Psi)$.
:::

::: proof
*Proof.* Take $\mu_1, \mu_2 \in \Gamma$ fixed. Since $(\Phi_t)_{t \geq 0}$ is gradient-$\mathcal{S}_p$ we have that the assignment $$\Psi^{\mu_1, \mu_2}: \gamma \mapsto \Delta(\mu_1 \gamma \mu_2) +  \mu_1 \Delta( \gamma ) \mu_2 - \mu_1 \Delta(\gamma \mu_2) -  \Delta(\mu_1 \gamma  ) \mu_2$$ is in $\mathcal{S}_p$ as an operator on $\ell_2(\Gamma)$. Therefore, also $$\mu_1^{-1} \Psi^{\mu_1, \mu_2}(\:\cdot \:) \mu_2^{-1}:  \gamma \mapsto \mu_1^{-1} \Delta(\mu_1 \gamma \mu_2) \mu_2^{-1} +   \Delta( \gamma )   -   \Delta(\gamma \mu_2) \mu_2^{-1} -  \mu_1^{-1} \Delta(\mu_1 \gamma  )$$ is in $\mathcal{S}_p$. Let $\mathbb{D}$ be the conditional expectation of $B(\ell_2(\Gamma))$ onto the diagonal operators in $B(\ell_2(\Gamma))$. Certainly $\mathbb{D}(\mu_1^{-1} \Psi^{\mu_1, \mu_2}(\: \cdot \:) \mu_2^{-1})$ is in $\mathcal{S}_p$ and, further, $$\mathbb{D}(\mu_1^{-1} \Psi^{\mu_1, \mu_2}(\:\cdot \:) \mu_2^{-1})(    \gamma) = \mu_1^{-1} \Delta^{\Psi}(\mu_1 \gamma \mu_2) \mu_2^{-1} +   \Delta^{\Psi}( \gamma )   -   \Delta^{\Psi}(\gamma \mu_2) \mu_2^{-1} -  \mu_1^{-1} \Delta^{\Psi}(\mu_1 \gamma  ).$$ Multiplying again with $\mu_1$ and $\mu_2$ shows that the assignment $$\gamma \mapsto \Delta^\Psi(\mu_1 \gamma \mu_2) +  \mu_1 \Delta^\Psi( \gamma ) \mu_2 - \mu_1 \Delta^\Psi(\gamma \mu_2) -  \Delta^\Psi(\mu_1 \gamma  ) \mu_2$$ is in $\mathcal{S}_p$. ◻
:::
