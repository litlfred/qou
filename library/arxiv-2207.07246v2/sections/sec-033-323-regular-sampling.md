---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-033-323-regular-sampling
section_title: "Regular Sampling"
section_number: 3.2.3
pages: 77-80
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secregularsampling label="secregularsampling"}

In section [\[Sample1bead\]](#Sample1bead){reference-type="ref" reference="Sample1bead"} and section [\[secMultibeadSample\]](#secMultibeadSample){reference-type="ref" reference="secMultibeadSample"}, we showed how to sample the free particle propagator for single bead and multiple beads. We proposed the transition probabilities $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$ according to the free particle propagator part $g^F(\mathcal{R}')$, so we have Eq.([\[gtnewgtold\]](#gtnewgtold){reference-type="ref" reference="gtnewgtold"}) which is $g^F(\mathcal{R}') T_{lr}(\mathcal{R}' \rightarrow \mathcal{R}) = g^F(\mathcal{R}) T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$, therefore we can use a simple version of acceptance rate $A(s\rightarrow s')$ which is Eq.([\[Accptequationsimp\]](#Accptequationsimp){reference-type="ref" reference="Accptequationsimp"}), to judge if we accept the new state $s'$ or not. Those moves can simplify the acceptance rate $A(s\rightarrow s')$, but they can make the spatial configurations of involved beads more or less correlated.

So, In order to make the algorithm more robust, we can add some moves such that the new configuration of each bead does not depend on other beads. For example, as is used in most Monte Carlo simulations, we can add moves with proposed transition probabilities obeying Eq.([\[tlrnewtlrold\]](#tlrnewtlrold){reference-type="ref" reference="tlrnewtlrold"}) which is $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') = T_{lr}(\mathcal{R}' \rightarrow \mathcal{R})$, and use Eq.([\[Accptequationsimp2\]](#Accptequationsimp2){reference-type="ref" reference="Accptequationsimp2"}) to judge if we accept the new state $s'$ or not. In these cases, the common choices for $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$ can be a constant over an interval or independent gaussian functions. We can randomly select $m$ beads from bead $0$ to bead $N$, $m$ can be at least $1$ and at most $N+1$, we put the label of the $m$ beads into a group call it $\mathcal{M}$, e.g., if we select bead $0$, $2$, $4$, then $\mathcal{M}=\{ 0,2,4 \}$, etc.

The proposed transition probability $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$ can be written as, $$T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') = \prod_{I  \in \mathcal{M} } \left( \prod_{i=1}^A  T_{I}(\bm{r}_i \rightarrow \bm{r}_i') \right) ,
 \label{}$$ where $T_{I}(\bm{r}_i \rightarrow \bm{r}_i')$ is the proposed transition probability for particle $i$ in bead $I$, and it is normalized to 1, $$\int d \bm{r}_i'  T_{I}(\bm{r}_i \rightarrow \bm{r}_i') =1 .
 \label{}$$ There can usually be two choices.

Choice 1

:   For constant $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$, we can choose $T_{I}(\bm{r}_i \rightarrow \bm{r}_i')$ as, $$T_{I}(\bm{r}_i \rightarrow \bm{r}_i') = \frac{1}{ (2 \alpha)^3}.
     \label{}$$ In this case the new position ${\bm{r}'}_i$ of particle $i$ in a bead can be proposed from its current position ${\bm{r}}_i$ by, $${\bm{r}}'_i =
       {\bm{r}}_i
      + \alpha \bm{u}_i  ,
     \label{uniformmove}$$ where $\bm{u}_i=(u_x,u_y,u_z)$ is a 3 dimensional random number and each of its components $u_x$, $u_y$, $u_z$ ranges from $-1$ to $1$ uniformly. $\alpha$ is a number which controls the step size of proposed move, it can be chosen to make the correspondingly acceptance rate $A(s\rightarrow s')$ around $20 \sim 80\%$.

Choice 2

:   For independent gaussian function $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$, we can choose $T_{I}(\bm{r}_i \rightarrow \bm{r}_i')$ as, $$T_{I}(\bm{r}_i \rightarrow \bm{r}_i') = \left(\frac{1}{\sqrt{2\pi \sigma^2}}\right)^3 e^{ - \frac{( \bm{r}_i' - \bm{r}_i )^2 }{2 \sigma^2} }.
     \label{}$$ In this case the new position ${\bm{r}'}_i$ of particle $i$ in a bead can be proposed from its current position ${\bm{r}}_i$ by, $${\bm{r}}'_i =
       {\bm{r}}_i
      + \sigma \bm{g}_i  ,
     \label{gaussmove}$$ where $\bm{g}_i$ is the gaussian random number defined in Eq.([\[gaussgi\]](#gaussgi){reference-type="ref" reference="gaussgi"}), and $\sigma$ is the standard deviation of the gaussian function, which can control the corresponding acceptance rate $A(s\rightarrow s')$.

In the above two choices, $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') = T_{lr}(\mathcal{R}' \rightarrow \mathcal{R})$, and the new configuration $R'_I$ is proposed from the current $R_I$, with a $3A$ dimensional vector $\Lambda_I$ which can be either composed of $\bm{u}_i$ or $\bm{g}_i$ for each particle, $$R'_I=R_I+\Lambda_I.
 \label{regsampling1}$$

If we propose new configurations for all the beads with the same $3A$ dimensional random vector $\Lambda$ at the same time, namely, $$R'_I=R_I+\Lambda,
 \label{shiftmove}$$ it will still obey Eq.([\[tlrnewtlrold\]](#tlrnewtlrold){reference-type="ref" reference="tlrnewtlrold"}), $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') = T_{lr}(\mathcal{R}' \rightarrow \mathcal{R})$. We can this kind of move as a 'shift'.

The regular sampling methods mentioned in this section are useful to guarantee uncorrelated samples but we do not perform them very often. This is because they are not as efficient as the multi-level sampling. If we just move few beads a time, it is not computationally efficient since we need to update the whole path anyway. If we move the same number of or more beads than the multi-level sampling method, we need to use very small $\alpha$, $\sigma$ or $\Lambda$ values in order to achieve similar acceptance rates as the multi-level sampling. This means they are not able to explore the configuration space as efficiently as multi-level sampling does.
