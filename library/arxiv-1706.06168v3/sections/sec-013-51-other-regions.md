---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-013-51-other-regions
section_title: "Other Regions"
section_number: 5.1
pages: 15-16
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
We now generalize the above theorem to other regions via $\mathop{\mathrm{SL}}_2(\mathbb{C})$ action and topological considerations. Theorem [\[grace_pairs_thm\]](#grace_pairs_thm){reference-type="ref" reference="grace_pairs_thm"} can then be considered our most general form of Grace's theorem. First though, we define two new notions in order to simplify the rest of this section.

::: definition
[]{#grace_pair_def label="grace_pair_def"} Fix $m \in \mathbb{N}_0$ and any sets $S_1,S_2 \subseteq (\mathbb{CP}^1)^m$. We call $(S_1,S_2)$ a *Grace pair* if: for all $\lambda \in \mathbb{N}_0^m$ and $p,q \in V(\lambda)$ such that $p$ is $S_1$-stable and $q$ is $S_2$-stable, we have that $D^\lambda(p \otimes q) \neq 0$. That is, if Grace's theorem holds for $S_1$ and $S_2$.
:::

::: definition
We say that a Grace pair is *disjoint* if it is of the form $(C_1 \times \cdots \times C_m, B_1 \times \cdots \times B_m)$ and $C_k$ and $B_k$ are disjoint for all $k \in [m]$.
:::

This yields the following restatement of the above theorem.

::: corollary
For any $m \in \mathbb{N}_0$, $((\mathcal{H}_+\cup \overline{\mathbb{R}_+})^m, (\mathcal{H}_-\cup \overline{\mathbb{R}_-})^m)$ is a Grace pair.
:::

The sets considered above intersect at 2 points ($0$ and $\infty$), and this ends up being crucial to the proof. So, in order to extend to the full generality of Grace's theorem, we will need to find such points even when the stability sets of two polynomials $p$ and $q$ do not a priori intersect at all. To this end, we give the following lemmas.

::: lemma
[]{#stability_closed_to_open label="stability_closed_to_open"} Fix $\lambda \in \mathbb{N}_0^m$ and any closed circular regions $C_1,\ldots,C_m \subset \mathbb{CP}^1$. Let $p \in V(\lambda)$ be $(C_1 \times \cdots \times C_m)$-stable. There exist open circular regions $U_1,\ldots,U_m$ such that $C_k \subset U_k$ for all $k \in [m]$ and $p$ is $(U_1 \times \cdots \times U_m)$-stable.
:::

::: proof
*Proof.* Follows from compactness of $\mathbb{CP}^1$ and closedness of $C_1 \times \ldots \times C_m$ and of the zero set of $p$. ◻
:::

For the next lemma, note that the boundary of any circular region $C$ is topologically equivalent to the unit circle in $\mathbb{C}$ (i.e., the boundary of the unit disc). With this, we call a portion of the boundary of $C$ *open* if it is open when considered as a subset of the unit circle. Further recall the characterization of projectively convex regions given by Proposition [\[proj_conv_characterization\]](#proj_conv_characterization){reference-type="ref" reference="proj_conv_characterization"}.

::: lemma
[]{#proj_conv_open_boundary label="proj_conv_open_boundary"} Fix $n \in \mathbb{N}_0$ and any projectively convex $C \equiv C^\circ \cup \gamma \subset \mathbb{CP}^1$, where $C^\circ$ is an open circular region and $\gamma$ is a connected portion of its boundary. Let $p \in V(n)$ be $C$-stable. There is an open connected subset $\Gamma$ of the boundary of $C^\circ$ such that $\gamma \subseteq \Gamma$ and $p$ is $(C^\circ \cup \Gamma)$-stable.
:::

::: proof
*Proof.* Let $\partial C^\circ$ denote the boundary of (the closure of) $C^\circ$, and let $S \subseteq \mathbb{CP}^1$ be the intersection of $\partial C^\circ$ and the zero set of $p$. Since the zero set of $p$ is closed, we have that $S$ is closed in $\partial C^\circ$. And further, $\gamma \cap S = \varnothing$ by assumption. Defining $\Gamma$ to be the connected component of $\partial C^\circ \setminus S$ containing $\gamma$ then gives the result. ◻
:::

Using these lemmas and the $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariance of the apolarity form, we obtain the following generalization of Grace's theorem. Here, $(ii)$ and $(iii)$ give the multivariate Grace's theorem proven in [@bb2].

::: theorem
[]{#grace_pairs_thm label="grace_pairs_thm"} For $m \in \mathbb{N}_0$ and $C_1,\ldots,C_m,B_1,\ldots,B_m \subseteq \mathbb{CP}^1$, we have that $(C_1 \times \cdots \times C_m, B_1 \times \cdots \times B_m)$ is a Grace pair for the following regions.

1.  For all $k \in [m]$, $C_k$ and $B_k$ are projectively convex, $C_k \cup B_k = \mathbb{CP}^1$, and $C_k \cap B_k$ is exactly two points.

2.  For all $k \in [m]$, $C_k$ is a closed circular region, $B_k$ is an open circular region, and $C_k \cup B_k = \mathbb{CP}^1$.

3.  For all $k \in [m]$, $C_k$ is an open circular region, $B_k$ is a closed circular region, and $C_k \cup B_k = \mathbb{CP}^1$.

4.  For $m = 1$, $C_1$ and $B_1$ are projectively convex and $C_1 \cup B_1 = \mathbb{CP}^1$.
:::

::: proof
*Proof.* $(i)$. By Proposition [\[proj_conv_characterization\]](#proj_conv_characterization){reference-type="ref" reference="proj_conv_characterization"}, every projectively convex region in $\mathbb{CP}^1$ is the union of an open circular region and a portion of its boundary. Since $C_k \cup B_k = \mathbb{CP}^1$ and $C_k \cap B_k$ is exactly two points, we then must have that $C_k = \phi_k \cdot (\mathcal{H}_+\cup \overline{\mathbb{R}_+})$ and $B_k = \phi_k \cdot (\mathcal{H}_-\cup \overline{\mathbb{R}_-})$ for some $\phi_k \in \mathop{\mathrm{SL}}_2(\mathbb{C})$. Since $D^\lambda$ is $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$-invariant, the result follows from Theorem [\[graces_thm\]](#graces_thm){reference-type="ref" reference="graces_thm"}.

$(ii)$. Fix $p,q \in V(\lambda)$. If $p$ is $(C_1 \times \cdots \times C_m)$-stable and $q$ is $(B_1 \times \cdots \times B_m)$-stable, then Lemma [\[stability_closed_to_open\]](#stability_closed_to_open){reference-type="ref" reference="stability_closed_to_open"} implies $p$ is $(U_1 \times \cdots \times U_m)$-stable for some open circular regions $U_1,\ldots,U_m$ such that $C_k \subset U_k$ for all $k \in [m]$. Since $C_k \cup B_k = \mathbb{CP}^1$, we then have that $U_k \cap B_k$ is open and nonempty. Since $U_k$ and $B_k$ are circular regions, their intersection in fact contains an open annulus or open strip in $\mathbb{C}$. Therefore we may slightly shrink $U_k$ and $B_k$ to get closed circular regions $U_k'$ and $B_k'$ such that $U_k' \cup B_k' = \mathbb{CP}^1$ and $U_k' \cap B_k' = \partial U_k' = \partial B_k'$, where $\partial B_k'$ denotes the boundary of $B_k'$. We can then further remove portions of the respective boundaries of $U_k'$ and $B_k'$ to get projectively convex regions $U_k''$ and $B_k''$ such that $U_k'' \cup B_k'' = \mathbb{CP}^1$ and $U_k' \cap B_k'$ is exactly two points. Since $U_k'' \subset U_k$ and $B_k'' \subset B_k$, we have that $p$ is $(U_1'' \times \cdots \times U_m'')$-stable and $q$ is $(B_1'' \times \cdots \times B_m'')$-stable. Therefore $(i)$ implies $D^\lambda(p \otimes q) \neq 0$, and this implies $(ii)$.

$(iii)$. Same argument as $(ii)$.

$(iv)$. Let $p,q \in V(n)$ be such that $p$ is $C_1$-stable and $q$ is $B_1$-stable. Defining $B_1' := \mathbb{CP}^1 \setminus C_1 \subseteq B_1$, we further have that $q$ is $B_1'$-stable. So WLOG we may assume that $B_1 = B_1'$. Note that this implies $\partial C_1^\circ = \partial B_1^\circ$; that is, the boundaries coincide. If $C_1$ is a circular region then so is $B_1$, and therefore $D^n(p \otimes q) \neq 0$ by $(ii)$ or $(iii)$. This implies $(iv)$ in this case.

Otherwise by Proposition [\[proj_conv_characterization\]](#proj_conv_characterization){reference-type="ref" reference="proj_conv_characterization"}, we have that $C_1 = C_1^\circ \cup \gamma_1$ where $C_1^\circ$ is an open circular region and $\varnothing \neq \gamma_1 \subseteq \partial C_1^\circ$. Analogously we have $B_1 = B_1^\circ \cup \psi_1$ with $\varnothing \neq \psi_1 \subseteq \partial B_1^\circ = \partial C_1^\circ$. Lemma [\[proj_conv_open_boundary\]](#proj_conv_open_boundary){reference-type="ref" reference="proj_conv_open_boundary"} then implies there exist $\Gamma_1$ and $\Psi_1$, which are open portions of the boundary of $C_1^\circ$, such that $\gamma_1 \subseteq \Gamma_1$, $\psi_1 \subseteq \Psi_1$, $p$ is $(C_1^\circ \cup \Gamma_1)$-stable, and $q$ is $(B_1^\circ \cup \Psi_1)$-stable. Since $\Gamma_1 \cup \Psi_1 = \partial C_1^\circ$, we then further can find closed subsets $\Gamma_1' \subset \Gamma_1$ and $\Psi_1' \subset \Psi_1$ such that $\Gamma_1' \cup \Psi_1' = \partial C_1^\circ$ and $\Gamma' \cap \Psi'$ is exactly two points. Therefore $D^n(p \otimes q) \neq 0$ by $(i)$, and this implies $(iv)$. ◻
:::

Notice that $(ii)$ and $(iii)$ in this result do not allow for mixed open and closed stability regions. That is, all of the $C_k$ must be open and all of the $B_k$ closed, or vice versa. We show that this particular point cannot be ignored, using the following example.

::: example
Let $\lambda = (1,1,1)$, denote $E := \mathbb{CP}^1 \setminus \overline{\mathbb{D}}$, and consider the polynomial $p := x_1x_2x_3 - y_1y_2y_3 = \mathop{\mathrm{Hmg}}_\lambda(x_1x_2x_3 - 1)$. First, it is easy to see that $D^\lambda(p \otimes p) = 0$. Also, $p$ is $\mathbb{D}^3$-stable and $E^3$-stable, but it is not $\overline{\mathbb{D}}^3$-stable nor $\overline{E}^3$-stable (zero at $(x_k,y_k) = (1,1)$ for $k \in [3]$). That is, the fact that $D^\lambda(p \otimes p) = 0$ does not contradict $(ii)$ or $(iii)$ of the previous theorem.

On the other hand, $p$ is both $(\overline{\mathbb{D}} \times \mathbb{D}\times \mathbb{D})$-stable and $(E \times \overline{E} \times \overline{E})$-stable. This shows that $(\overline{\mathbb{D}} \times \mathbb{D}\times \mathbb{D}, E \times \overline{E} \times \overline{E})$ is not a Grace pair. That is, mixed open and closed stability regions cannot be included in $(ii)$ and $(iii)$ of the previous theorem.
:::

As for whether or not the two-point intersection condition can be removed from $(i)$ seems to be a more subtle point. It would be quite nice if this condition could be removed, but it is unclear whether or not it is possible.
