---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-012-32-self-duality-and-the-witten-index
section_title: "Self-duality and the Witten index"
section_number: 3.2
pages: 20-22
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.995
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
[]{#s:quantsymm label="s:quantsymm"}

From the above discussion, it is clearly important to determine which CHL models are self-dual under Fricke S-duality. This can be determined simply in terms of the Frame shape $\prod_{a|N} a^{m(a)}$ of $g$, by analyzing the associated Witten index as we now show.

Let $\mathcal{C}$ be a non-linear sigma model on K3 and $g$ be a symmetry of $\mathcal{C}$ of order $N$ preserving the $\mathcal{N}=(4,4)$ superconformal algebra. We will assume that the orbifold of $\mathcal{C}$ by $g$ is a consistent CFT $\mathcal{C}'$; in our previous notation, this means that $\lambda=1$ and $\hat N=N$ (the case $\lambda>1$ is treated in appendix [\[a:quantsymm\]](#a:quantsymm){reference-type="ref" reference="a:quantsymm"}). It follows that the orbifold CFT $\mathcal{C}'$ is either a non-linear sigma model on K3 or on a four dimensional torus $T^4$. Furthermore, $\mathcal{C}'$ has a symmetry $\mathcal{Q}$ of order $N$ (the quantum symmetry) that acts by multiplication by $e^{\frac{2\pi i r}{N}}$ on the $g^r$-twisted states.

Let $\prod_{a|N} a^{m(a)}$, $m(a)\in \mathbb{Z}$, be the cycle shape associated to $g$. By [\[Elevel\]](#Elevel){reference-type="eqref" reference="Elevel"}, the condition that the orbifold is consistent, i.e $\lambda=1$, is equivalent to $$\label{consorbif} \sum_{a|N}m(N/a)a\in 24\mathbb{Z}\ .$$The cycle shape determines the eigenvalues of $g$ on the $24$ dimensional space Ramond-Ramond ground states of $\mathcal{C}$. In this section, we will prove that the cycle shape describing the action of $\mathcal{Q}$ on the RR ground states of the orbifold theory $\mathcal{C}'$ is $\prod_{a|N} a^{m(N/a)}$. This statement needs a refinement when $\mathcal{C}'$ is a torus model; we will be more precise below.

In general, the topology of the target space of a $\mathcal{N}=(4,4)$ superconformal field theory $\mathcal{C}$ with central charge $c=6$ can be distinguished by the Witten index[^1] $$\mathcal{I}^\mathcal{C}(\tau.\bar\tau)=\mathop{\mathrm{Tr}}_{RR}((-1)^{F+\tilde F}q^{L_0-\frac{c}{24}}\bar q^{\bar L_0-\frac{c}{24}})=\begin{cases}24 & \text{if $\mathcal{C}$ is a K3 model}\\ 0 & \text{if $\mathcal{C}$ is a torus model}\ ,\end{cases}$$where $q=e^{2\pi i\tau}$. The Witten index is the specialization to $z=0$ of the elliptic genus $\phi(\tau,z)$. By standard arguments, the only non-vanishing contribution to this trace comes from the RR ground states, i.e. states with conformal weights $(h,\bar h)=(\frac{c}{24},\frac{\bar c}{24})=(\frac{1}{4},\frac{1}{4})$, so that the Witten index is actually a constant and it equals the Euler characteristic of the target space.

If the theory has a symmetry $g$ one can consider a $g$-twined version of the Witten index (the specialization to $z=0$ of the twining elliptic genus $\phi_g(\tau,z)$) $$\mathcal{I}^\mathcal{C}_g:=\mathop{\mathrm{Tr}}_{RR}(g(-1)^{F+\tilde F}q^{L_0-\frac{c}{24}}\bar q^{\bar L_0-\frac{c}{24}})\ ,$$which is again a constant. In the case we are considering, where $\mathcal{C}$ is a K3 model and $g$ has cycle shape $\prod_{a|N} a^{m(a)}$, the twining index $\mathcal{I}^\mathcal{C}_g$ is simply the trace of $g$ on its $24$-dimensional representation (the RR ground states in K3 models have all positive fermion number $(-1)^{F+\tilde F}$), so that $$\label{firstIg} \mathcal{I}^\mathcal{C}_{g}=\sum_{a|N} m(a) \sum_{k=1}^a e^{\frac{2\pi i k}{a}}=m(1)\ ,$$which is just the dimension of the fixed subspace of $g$. More generally, for any power $g^j$ we have

$$\label{secondIg} \mathcal{I}^\mathcal{C}_{g^j}=

\sum_{u|(j,N)} m(u)u\ ,$$where the right hand side is the dimension of the fixed subspace of $g^j$.

Notice that, once the twined indices $\mathcal{I}^\mathcal{C}_{g^j}$ are known for all $j=1,\ldots,N$, using [\[secondIg\]](#secondIg){reference-type="eqref" reference="secondIg"} one can reconstruct the cycle shape of $g$.

Similarly, one can consider the twined Witten indices $\mathcal{I}^{\mathcal{C}'}_{\mathcal{Q}^k}$, $k=1,\ldots,N$, associated with the action of the quantum symmetry $\mathcal{Q}$ on the RR ground states of the orbifold theory $\mathcal{C}'$. Using standard orbifold techniques, this index can be computed in terms of the Frame shape of $g$ (see appendix [\[a:quantsymm\]](#a:quantsymm){reference-type="ref" reference="a:quantsymm"}) $$\label{Qindex} \mathcal{I}^{\mathcal{C}'}_{\mathcal{Q}^k}=\sum_{n|(k,N)}m(N/n)n\ .$$ By specializing to the case $k=N$, we obtain the Witten index of the orbifold theory $\mathcal{C}'$ $$\mathcal{I}^{\mathcal{C}'}=\sum_{n|N}m(N/n)n\ .$$Thus, the condition [\[consorbif\]](#consorbif){reference-type="eqref" reference="consorbif"} of consistency of the orbifold $\mathcal{C}'$ implies that the elliptic genus of the orbifold theory is a multiple of $24$. Now, we see that, if [\[consorbif\]](#consorbif){reference-type="eqref" reference="consorbif"} is satisfied, then the only two possibilities are $\mathcal{I}^{\mathcal{C}'}=0$ for a torus model and $\mathcal{I}^{\mathcal{C}'}=24$ for a K3 model. This can be also verified a posteriori for all possible cycle shapes of Conway elements.

If $\mathcal{I}^{\mathcal{C}'}=24$, then $\mathcal{C}'$ is a K3 model, and by comparing this formula with [\[secondIg\]](#secondIg){reference-type="eqref" reference="secondIg"}, we conclude that $\mathcal{Q}$ must correspond to a cycle shape $\prod_{a|N}a^{m(N/a)}$. In particular, $\mathcal{Q}$ has the same cycle shape as $g$ if and only if the cycle shape is 'balanced' with balancing number $N$, i.e. $$\label{balance} m(a)=m(N/a)\ .$$ If [\[balance\]](#balance){reference-type="eqref" reference="balance"} holds, then [\[consorbif\]](#consorbif){reference-type="eqref" reference="consorbif"} is automatically satisfied and $\mathcal{C}$ is a K3 model.

When $\mathcal{C}'$ is a torus model, i.e. $\mathcal{I}^{\mathcal{C}'}=0$, the cycle shape $\prod_{a|N}a^{m(N/a)}$ determines the eigenvalues of $\mathcal{Q}(-1)^{F+\tilde F}$ on the RR ground states. Notice that, in this case, the fermion number has to be taken into account, as it acts non-trivially on the RR ground states.

To summarise, the above analysis shows that there are three possible cases to take into account:

-   If the Frame shape is *balanced* with balancing number $N$, i.e. if $$m(N/a)=a\ ,$$for all $a|N$, then $$\sum_{a|N}m(N/a)a=24\ ,$$ the orbifold $\mathcal{C}'$ is again a K3 model and the quantum symmetry $\mathcal{Q}$ has the same Frame shape as $g$. Thus, in this case, the CHL model is self-dual and the lattice $\Lambda_m$ is $N$-modular.

-   If the Frame shape is not balanced, but $$\sum_{a|N}m(N/a)a=24\ ,$$then the orbifold $\mathcal{C}'$ is again a K3 model, but Frame shape $\prod_{a|n}a^{m(N/a)}$ of the quantum symmetry $\mathcal{Q}$ is different from $g$. Thus, in this case, S-duality relates two different CHL models. In particular, if $\Lambda_m$ and $\Lambda_m'$ are the lattices of magnetic charges in these two models, we have the relation $$\Lambda_m^*\cong\Lambda'_m(N)\ .$$

-   If $$\sum_{a|N}m(N/a)a=0\ ,$$then the orbifold $\mathcal{C}'$ is a torus model. Thus, the CHL model is dual to type IIA on $(T^4\times S')/\mathbb{Z}_N\times \tilde S'$.

[^1]: Of course, the Witten index can be defined even for theories with a smaller superconformal algebra, in particular for $\mathcal{N}=(2,2)$ theories.
