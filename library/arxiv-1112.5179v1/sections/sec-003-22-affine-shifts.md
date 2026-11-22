---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-003-22-affine-shifts
section_title: "Affine shifts"
section_number: 2.2
pages: 10-11
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.901
latex_coverage_ratio: 1.0
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:aff label="sec:aff"}

As mentioned above, the R-charge used in the index does not need to coincide with the R-charge that appears in the superconformal algebra. We can take $R$ to be any R-symmetry charge. If we redefine the R-charge by a flavor symmetry, then different choices are related by $R \to R -\alpha_e \cdot e$ for some vector $\alpha_e$. Under such a shift, the index varies accordingly as

$$\mathcal{I}_\mathcal{T}(m,e;q) \to q^{-\tfrac{1}{2} \alpha_e \cdot e} \mathcal{I}_\mathcal{T}(m,e;q)\,.$$

There is also a certain degree of latitude in choosing the R-charge of the vacuum in a non-trivial flux sector of the theory. It is thus natural to also consider redefinitions $R \to R +\alpha_m \cdot m$, under which

$$\mathcal{I}_\mathcal{T}(m,e;q) \to q^{\tfrac{1}{2}  \alpha_m \cdot m} \mathcal{I}_\mathcal{T}(m,e;q)\,.$$

Altogether, we can collect

$$\alpha = {\alpha_e \choose \alpha_m}\,,$$

and write

$$\boxed{\phantom{int}
\mathcal{I}_{\sigma^R(\alpha) \circ \mathcal{T}}(\gamma;q) = q^{\frac{1}{2} \langle \alpha, \gamma \rangle} \mathcal{I}_\mathcal{T}(\gamma;q) \phantom{\int}}$$

where $\sigma^R(\alpha) \circ \mathcal{T}$ denotes the theory with the new R-charge $R+\langle \alpha, \gamma \rangle$. Here the symplectic product $\langle \alpha, \gamma \rangle$ equals $\alpha_m \cdot m - \alpha_e \cdot e$.

Similar shifts can happen in the definition of the fermion number charge $F$. This would not be the case if we had defined $(-1)^F = (-1)^{2 j_3}$, as $j_3$ is a generator in a non-Abelian symmetry group. But the symplectic group acts on $(-1)^{e\cdot m}$ in a rather interesting way. Indeed, $s(\gamma) = (-1)^{e \cdot m}$ is a "quadratic refinement of the charge lattice", *i.e.* a $Z_2$-valued function of charges with the property $$s(\gamma) s(\gamma') = s(\gamma + \gamma') (-1)^{\langle \gamma, \gamma' \rangle}\,.$$ Any two such refinements differ by a factor of the form $(-1)^{\langle \alpha, \gamma \rangle}$ for some $\alpha$.

Thus, we will just introduce a fermion-number shift operation

$$\boxed{\phantom{\int} \mathcal{I}_{\sigma^F(\alpha) \circ T}(\gamma;q) = (-1)^{\langle \alpha, \gamma \rangle} \mathcal{I}_\mathcal{T}(\gamma;q) \phantom{\int}}$$

that modifies the choice of quadratic refinement used in $F$. Note that $[\sigma^F(\alpha)]^2=1$ for any $\alpha$. Such shifts in the definition of $R$ and $F$ are often important when comparing mirror descriptions of the same theory. In particular, a symplectic transformation will change the choice of quadratic refinement from $s(\gamma)$ to $s(g \gamma)$, which will have to be brought back to $s(\gamma)$ by a fermion number shift.

In the following, we will often find that $R$ and $F$ shifts happen simultaneously, with the same parameter $\alpha$. This is ultimately due to the fact that the UV description of the theories often have a natural R-charge assignment such that $(-1)^F = (-1)^R$, *i.e.* $(-1)^{R + 2 j_3 + e \cdot m} =1$ when acting on all the chiral fields in the Lagrangian.

[^1]

Mathematically, the shifts in $R$ and $F$ generate an abelian group of translations ${\mathbb Z}^{2N}\times ({\mathbb Z}_2)^{2N}$ that acts on the index. This abelian group can naturally be combined with the symplectic group $Sp(2N,{\mathbb Z})$ to generate an affine symplectic group $Sp(2N,{\mathbb Z}) \ltimes ({\mathbb Z}\times {\mathbb Z}_2)^{2N}$. One can check that the expected group relations are satisfied. For example, taking $N=1$, if we denote the generators of unit electric and magnetic shifts by $\sigma_e^R,\,\sigma_e^F$ and $\sigma_m^R,\,\sigma_m^F$, respectively, then

$$\label{affrels}
\begin{equation}S\sigma_e^R = \sigma_m^R S\,, \quad\qquad
S\sigma_m^R = (\sigma_e^R){}^{-1}S\,,\end{equation}
\begin{equation}T^{-1}(\sigma_e^R)^{-1}T\sigma_e^R = \sigma_m^R\,,\quad\qquad T\sigma_m^R = \sigma_m^R T\,, \end{equation}$$

and similarly for $\sigma^F_{e,m}$. The abelian $({\mathbb Z}\times {\mathbb Z}_2)^{2N}$ subgroup of the affine symplectic group does act in the obvious way by translations on the vector $(m,e)$. However, we will see momentarily that there exists another object, a certain algebra of operators associated with the index, on which this abelian subgroup *is* represented by translations.

[^1]: It is interesting to remark that in the context of four-dimensional ${\cal N}=2$ gauge theory, wall-crossing considerations lead to the conjecture that $(-1)^{R + 2 j_3}$ should always be equal to a quadratic refinement of the charge lattice when acting on BPS states [@GMNIII].
