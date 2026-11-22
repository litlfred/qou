---
doc_id: arxiv-math-0611521v1
doc_title: "The q-analogue of the wild fundamental group"
section_id: sec-002-22-filtration-by-the-slopes
section_title: "Filtration by the slopes"
section_number: 2.2
pages: 10-12
source_pdf: 0611521v1.pdf
source_sha256: 65fcd77b7b0a208e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.981
doc_brief: "The q-analogue of the wild fundamental group — We describe an explicit construction of galoisian Stokes operators for irregular linear q-difference equations."
---
[]{#subsection:filtration label="subsection:filtration"}

#### The filtration and the associated graded module.

The module $M$ is said to be pure isoclinic of slope $\mu$ if $S(M) = \{\mu\}$ and fuchsian if moreover $\mu = 0$. Direct sums of pure isoclinic modules are called pure modules [^1]: they are irregular objects without wild monodromy, as follows from [@RSZ] and [@JSSTO]. The tannakian subcategory of ${\mathcal{E}}^{(0)}$ made up of pure modules is called ${\mathcal{E}}^{(0)}_{p}$. Modules with integral slopes also form tannakian subcategories, which we write ${\mathcal{E}}^{(0)}_{1}$ and ${\mathcal{E}}^{(0)}_{p,1}$.\
It was proved in [@JSGAL] that the category ${\mathcal{E}}^{(0)}_{f}$ of fuchsian modules is equivalent to the category of *flat* holomorphic vector bundles over ${\mathbf{E}_{q}}$ and that its Galois group $G_{f}^{(0)}$ is isomorphic to $Hom_{gr}({\mathbf C}^{*}/q^{{\mathbf Z}},{\mathbf C}^{*}) \times {\mathbf C}$ (here, as in the introduction, $Hom_{gr}$ means "morphisms of *abstract* groups"). Since objects of ${\mathcal{E}}^{(0)}_{p,1}$ are essentially ${\mathbf Z}$-graded objects with fuchsian components, the Galois group of ${\mathcal{E}}^{(0)}_{p,1}$ is $G_{p,1}^{(0)} = {\mathbf C}^{*} \times G_{f}^{(0)}$.

::: thm
[@JSFIL] []{#theorem:filtration label="theorem:filtration"} Let the letter $K$ stand for the field ${{\mathbf C}(\{z\})}$ (convergent case) or the field ${{\mathbf C}((z))}$ (formal case). In any case, any object $M$ of ${DiffMod(K,\sigma_q)}$ admits a unique filtration $(F_{\leq \mu}(M))_{\mu \in {\mathbf Q}}$ by subobjects such that each $F_{(\mu)}(M) = \frac{F_{\leq \mu}(M)}{F_{< \mu}(M)}$ is pure of slope $\mu$ (thus of rank $r_{M}(\mu)$). The $F_{(\mu)}$ are endofunctors of ${DiffMod(K,\sigma_q)}$ and ${\text{gr}}= \bigoplus F_{(\mu)}$ is a faithful exact ${\mathbf C}$-linear $\otimes$-compatible functor and a retraction of the inclusion of ${\mathcal{E}}_{p}^{(0)}$ into ${\mathcal{E}}^{(0)}$. In particular, the functor ${\text{gr}}$ retracts ${\mathcal{E}}_{1}^{(0)}$ to ${\mathcal{E}}_{p,1}^{(0)}$.In the formal case, $gr$ is isomorphic to the identity functor.
:::

::: cor
For each $a \in {\mathbf C}^{*}$, the functor $\hat{\omega}_{a}^{(0)} = \omega_{a}^{(0)} \circ {\text{gr}}$ is a fiber functor.
:::

We shall consistently select an arbitrary basepoint $a \in {\mathbf C}^{*}$ and identify the Galois group $G^{(0)}$ as $Aut^{\otimes}\bigl(\hat{\omega}_{a}^{(0)}\bigr)$.

::: cor
The Galois group $G^{(0)}$ of ${\mathcal{E}}^{(0)}$ is the semi-direct product $\mathfrak{St}\rtimes G_{p}^{(0)}$ of the Galois group $G_{p}^{(0)}$ of ${\mathcal{E}}_{p}^{(0)}$ by a prounipotent group, the Stokes group $\mathfrak{St}$.
:::

***From now on, we only consider modules with integral slopes***.\
Further studies would have to be based on the work [@vdPR] by van der Put and Reversat.

#### Description in matrix terms.

We now introduce notational conventions which will be used all along this paper for a module $M$ in ${\mathcal{E}}_{1}^{(0)}$ and its associated graded module $M_{0} = gr(M)$, an object of ${\mathcal{E}}_{p,1}^{(0)}$. The module $M$ may be given the shape $M = ({{\mathbf C}(\{z\})}^{n},\Phi_{A})$, with: $$\label{equation:forme-canonique}
A = A_{U} \underset{def}{=}
\begin{pmatrix}
z^{\mu_{1}} A_{1}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & U_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & z^{\mu_{k}} A_{k}    
\end{pmatrix},$$ where the slopes $\mu_{1} < \cdots < \mu_{k}$ are integers, $r_{i} \in {\mathbf N}^{*}$, $A_{i} \in GL_{r_{i}}({\mathbf C})$ ($i = 1,\ldots,k$) and $$U = (U_{i,j})_{1 \leq i < j \leq k} \in 
\underset{1 \leq i < j \leq k}{\prod} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})}).$$ The associated graded module is then a direct sum $M_{0} = P_{1} \oplus \cdots \oplus P_{k}$, where, for $1 \leq i < j \leq k$, the module $P_{i}$ is pure of rank $r_{i}$ and slope $\mu_{i}$ and can be put into the form $P_{i} = ({{\mathbf C}(\{z\})}^{r_{i}},\Phi_{z^{\mu_{i} A_{i}}})$. Therefore, one has $M_{0} = ({{\mathbf C}(\{z\})}^{n},\Phi_{A_{0}})$, where the matrix $A_{0}$ is block-diagonal (it is the same as $A_{U}$, with all $U_{i,j} = 0$).\
We write ${\mathfrak{G}}\subset GL_{n}$ for the algebraic subgroup and ${\mathfrak{g}}$ for its Lie algebra, made up of matrices of the form: $$\label{equation:automorphisme}
F = 
\begin{pmatrix}
I_{r_{1}} & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & F_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & I_{r_{k}}     
\end{pmatrix}
\quad \text{~and~} \quad
f = 
\begin{pmatrix}
0_{r_{1}} & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & F_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & 0_{r_{k}}     
\end{pmatrix}.$$ For $F$ in ${\mathfrak{G}}$, we shall write $F[A] = \left(\sigma_qF\right) A F^{-1}$ the result of the gauge transformation $F$ on the matrix $A$. Theorem [\[theorem:filtration\]](#theorem:filtration){reference-type="ref" reference="theorem:filtration"} entails: $$\forall (U_{i,j})_{1 \leq i < j \leq k} \in 
\prod_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})}) \;,\;
\exists ! \hat{F} \in {\mathfrak{G}}({{\mathbf C}((z))}) \;:\;
\hat{F} [A_{0}] = A_{U}.$$ This $\hat{F}$ will be written $\hat{F}_{A}$ (where $A = A_{U}$). The blocks $\hat{F}_{i,j}$ are recursively computed as follows. For $j < i$, $\hat{F}_{i,j} = 0$. For $j = i$, $\hat{F}_{i,j} = I_{r_{i}}$. Then, for $j > i$, one must solve the non homogeneous first order equation: $$\label{equation:calculrecursifhat(F)}
\sigma_q\hat{F}_{i,j} z^{\mu_{j}} A_{j} - z^{\mu_{i}} A_{i} \hat{F}_{i,j} =
\sum_{i < k < j} U_{i,k} \hat{F}_{k,j} + U_{i,j}.$$

#### Description of the Stokes group.

To go further, we choose to fix an arbitrary basepoint $a \in {\mathbf C}^{*}$ (see the corollary to theorem [\[theorem:filtration\]](#theorem:filtration){reference-type="ref" reference="theorem:filtration"}) and we identify the Galois groups accordingly: $$G_{1}^{(0)} \underset{def}{=} Gal({\mathcal{E}}_{1}^{(0)}) = 
Aut^{\otimes}(\hat{\omega}^{(0)}_{a}).$$ Recall from the quoted papers the action of the pure component $G_{p,1}^{(0)} = {\mathbf C}^{*} \times Hom_{gr}({\mathbf C}^{*}/q^{{\mathbf Z}},{\mathbf C}^{*}) \times {\mathbf C}$. We keep the notations above. For any $A$ with graded part $A_{0}$, an element $(\alpha,\gamma,\lambda) \in G_{p,1}^{(0)}$ yields the automorphism of $\hat{\omega}^{(0)}_{a}(A) = \omega^{(0)}_{a}(A_{0}) = {\mathbf C}^{n}$ given by the matrix: $$\begin{pmatrix}
\alpha^{\mu_{1}} \gamma(A_{s,1}) A_{u,1}^{\lambda}  
                                        & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & 0 & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & 
                           \alpha^{\mu_{k}} \gamma(A_{s,k}) A_{u,k}^{\lambda}
\end{pmatrix},$$ where we have written $A_{i} = A_{s,i} A_{u,i}$ the multiplicative Dunford decomposition (into a semi-simple and a unipotent factor that commute) and $\gamma$ acts on a semi-simple matrix through its eigenvalues. These matrices generate the group $G_{p,1}^{(0)}(A) \subset GL_{n}({\mathbf C})$.\
We then have a semi-direct decomposition: $G_{1}^{(0)} = \mathfrak{St}\rtimes G_{p,1}^{(0)}$, where the Stokes group $\mathfrak{St}$ is the kernel of the morphism $G_{1}^{(0)} \rightarrow G_{p,1}^{(0)}$. The group $\mathfrak{St}(A)$ is an algebraic subgroup of ${\mathfrak{G}}({\mathbf C})$. The above matrix of $G_{p,1}^{(0)}(A)$ acts by conjugation on the matrix described by ([\[equation:automorphisme\]](#equation:automorphisme){reference-type="ref" reference="equation:automorphisme"}): the $F_{i,j}$ block is sent to $\alpha^{\mu_{i} - \mu_{j}} \gamma(A_{s,i}) A_{u,i}^{\lambda}
F_{i,j} \bigl(\gamma(A_{s,j}) A_{u,j}^{\lambda}\bigr)^{-1}$. In particular, the group ${\mathbf C}^{*}$ acts on the "level $\delta$" upper diagonal $\mu_{j} - \mu_{i} = \delta$ (where $\delta \in {\mathbf N}$) by multiplication by $\alpha^{-d}$. The group $\mathfrak{St}(A)$ is *filtered* by the *normal* subgroups $\mathfrak{St}_{\delta}(A)$ defined by: $\mu_{j} - \mu_{i} \geq \delta$ (meaning that all blocks such that $0 < \mu_{j} - \mu_{i} < \delta$ vanish).\
Likewise, the Lie algebra $\mathfrak{st}(A) = Lie\bigl(\mathfrak{St}(A)\bigr)$, which is a subalgebra of ${\mathfrak{g}}({\mathbf C})$, admits an adjoint action described by the same formulas (this is because $\log P F P^{-1} = P \log F P^{-1}$). The algebra $\mathfrak{st}(A)$ is *graded* by its "level $\delta$" upper diagonals $\mathfrak{st}_{\delta}(A)$, defined by $\mu_{j} - \mu_{i} = \delta$. As noted in [@JSSTO], the algebra $\mathfrak{st}_{\delta}(A)$ can be identified with the (group) kernel of the central extension $\mathfrak{St}(A)/\mathfrak{St}_{\delta+1}(A) \rightarrow \mathfrak{St}(A)/\mathfrak{St}_{\delta}(A)$.

[^1]: It should be noted that we call in the present paper a pure isoclinic (resp. pure) module what was called a pure (resp. tamely irregular) module in previous papers.
