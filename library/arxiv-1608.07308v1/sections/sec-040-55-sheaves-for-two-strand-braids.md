---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-040-55-sheaves-for-two-strand-braids
section_title: "Sheaves for two-strand braids"
section_number: 5.5
pages: 47-49
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.81
---
[]{#sub:sheaves n=2 label="sub:sheaves n=2"}

To construct the sheaf $\iota_*(M)$ for any object $M \in \mathrm{SBim}_2$, one needs to consider the module $\mathop{\mathrm{Hom}}(\mathbf{1}, M \otimes \overline{\mathbf{FT}}^{\bullet})$ over the graded algebra $A = \mathop{\mathrm{Hom}}(\mathbf{1},\overline{\mathbf{FT}}^{\bullet})$. In the previous subsection, we have studied the case $M = \overline{\mathbf{FT}}^k$ for positive integers $k$, and we found that $\iota_*(M) = \mathcal{O}(k)$. The computation for negative $k$ is more interesting: $$\overline{\mathbf{FT}}^{-k} \cong  \left[t^{-k} \overline{R}\rightarrow \underbrace{q^{-\frac 12} t^{\frac 12-k}  \overline{B}\rightarrow q^{-\frac 12} t^{1-k} \overline{B}\rightarrow q^{-1} t^{\frac 32-k} \overline{B}\rightarrow \dots \rightarrow q^{\frac 12-k} t^{-\frac 12} \overline{B}\rightarrow q^{\frac 12-k} \overline{B}}_{2k}  \right]$$ for any $k\geq 0$, where the maps alternate between $\frac {x \otimes 1 + 1 \otimes x}2$ and $\frac {x \otimes 1 - 1 \otimes x}2$. Therefore, we have: $$\mathop{\mathrm{Hom}}(\mathbf{1},\overline{\mathbf{FT}}^{-k}) \cong \left[t^{-k} \overline{R}\xrightarrow{1} \underbrace{ t^{\frac 12-k} \overline{R}\xrightarrow{0} t^{1-k} \overline{R}\xrightarrow{x}  q^{-1} t^{\frac 32-k} \overline{R}\xrightarrow{0} \dots \xrightarrow{x} q^{1-k} t^{-\frac 12} \overline{R}\xrightarrow{0}  q^{1-k} \overline{R}}_{2k}  \right]$$ $$\label{eqn:negative hom n=2}
\Longrightarrow \quad \mathop{\mathrm{Hom}}(\mathbf{1},\overline{\mathbf{FT}}^{-k}) \cong t^{\frac 12} H^1\left(\overline{\mathrm{FHilb}}_2,\mathcal{O}(-k)\right)$$ according to [\[eqn:coh n=2\]](#eqn:coh n=2){reference-type="eqref" reference="eqn:coh n=2"}. The case of general $a$ follows by analogy with the previous subsection, so we conclude the following formula that extends [\[eqn:volo\]](#eqn:volo){reference-type="eqref" reference="eqn:volo"} to negative integers: $$\label{eqn:formula}
\mathop{\mathrm{{RHom}}}^\bullet_{\mathrm{SBim}_2}(\mathbf{1},\overline{\mathbf{FT}}^{-k}) \cong R\Gamma \left( \overline{\mathrm{FHilb}}_2,\mathcal{O}(-k)\otimes \wedge^{\bullet} \mathcal{O}(-1) \right)$$

::: remark
[]{#rem:different gradings label="rem:different gradings"}

Let us observe the fact that the derived functors in the two sides of the above equation are very different. In the left hand side, we have the derived Hochschild homology functor, whose degree is measured by $a$. In the right hand side, we have derived direct image of sheaves, whose degree is measured by $t^{\frac 12}$, and the $a$ grading comes from $\wedge^\bullet \mathcal{O}(-1)$.
:::

To complete the discussion for $n=2$, let us compute $\mathcal{B}(\sigma) := \iota_*(\sigma)$ where $\sigma$ denotes a single positive crossing. Together with the projection formula [\[eqn:projection\]](#eqn:projection){reference-type="eqref" reference="eqn:projection"}, this implies that: $$\mathcal{B}(\sigma^{2k+1}) := \iota_*(\sigma^{2k+1}) = \iota_*(\sigma\otimes \overline{\mathbf{FT}}^k) = \iota_*(\sigma) \otimes \mathcal{O}(k) = \mathcal{B}(\sigma)\otimes \mathcal{O}(k)$$ for all integers $k$. In fact, we have: $$\mathop{\mathrm{Hom}}(\mathbf{1},\sigma^{2k+1}) \cong \left[\underbrace{q^{k+\frac 12} \overline{R}\xrightarrow{x} \cdots \xrightarrow{0} q^{2} t^{k-1} \overline{R}\xrightarrow{x}  q t^{k-\frac 12} \overline{R}\xrightarrow{0} q t^{k} \overline{R}}_{2k+1} \xrightarrow{x}  t^{k+\frac 12} \overline{R}\right]$$ and therefore: $$\bigoplus_{k\ge 0}\mathop{\mathrm{Hom}}(\mathbf{1}, \sigma \otimes \mathbf{FT}^{k})=\bigoplus_{k\ge 0}\mathop{\mathrm{Hom}}(\mathbf{1}, \sigma^{2k+1})=t^{1/2}\frac{\mathbb{C}[x,z,w]}{x}$$ where recall that $z$ and $w$ are the maps of [\[eqn:eigenmaps2\]](#eqn:eigenmaps2){reference-type="eqref" reference="eqn:eigenmaps2"}. We conclude that $\mathcal{B}(\sigma)$ is the structure sheaf of the subscheme $\{x=0\} \subset \overline{\mathrm{FHilb}}_2$, which is nothing but the connected component $\overline{Z_2} = \mathrm{FHilb}_2(\mathrm{point}) \cong \mathbb{P}^1$ of [\[eqn:z2 n=2\]](#eqn:z2 n=2){reference-type="eqref" reference="eqn:z2 n=2"}. The periodic resolution [\[eq:mf\]](#eq:mf){reference-type="eqref" reference="eq:mf"} takes the form: $$\mathcal{B}(\sigma) \cong \mathcal{O}_{\mathbb{P}_1} \stackrel{\mathrm{q.i.s.}} \cong \left[ ...  \stackrel{w}\longrightarrow q^2t \mathcal{O}(-1) \stackrel{x}\rightarrow qt \mathcal{O}(-1) \stackrel{w}\longrightarrow q \mathcal{O}(-1) \stackrel{x}\rightarrow \mathcal{O}\right]$$ where $\mathcal{O}$ denotes the structure sheaf of $\overline{\mathrm{FHilb}}_2$. In the non-reduced category, one needs to replace $x$ by $x_1-x_2$ everywhere. Finally, let us compute $\iota_*(B)$, where recall that $B = R \otimes_{R^s} R$. Since $z\otimes \mathop{\mathrm{Id}}_B$ is an isomorphism between $B$ and $\mathbf{FT}_2\otimes B$, we have: $$\bigoplus_{k\ge 0}\mathop{\mathrm{Hom}}(\mathbf{1},B\cdot\mathbf{FT}^{k})=\bigoplus_{k\ge 0}z^k\mathop{\mathrm{Hom}}(\mathbf{1},B)=\mathbb{C}[x_1,x_2,z].$$ Therefore $\iota_*(B)$ is the structure sheaf of the irreducible component $Z_1 \subset \mathrm{FHilb}_2$ cut out by the equation $w=0$ (see [\[eqn:z1 n=2\]](#eqn:z1 n=2){reference-type="eqref" reference="eqn:z1 n=2"}), which is isomorphic to $\mathbb{C}^2$ with coordinates $x_1$ and $x_2$.

# Example: the case of three strands {#sec:n=3}

## The geometry of $\mathrm{FHilb}_3$ {#sub:fh 3}

We will now study the variety $\mathrm{FHilb}_3 = \mathrm{FHilb}_3(\mathbb{C})$ and formulate a precise conjecture about the sheaf $\iota_*(\text{figure eight knot})$. Recall the matrix presentation: $$\mathrm{FHilb}_3  = \left\{ X = \left( \begin{array}{ccc}
x_1 & 0 & 0 \\
a & x_2 & 0 \\
\alpha_1 & \alpha_2 & x_{3} \end{array} \right), \ Y = \left( \begin{array}{ccc}
0 & 0 & 0 \\
b & 0 & 0 \\
\beta_1 & \beta_2 & 0 \end{array} \right), \ [X,Y]=0, \right.$$ $$\label{eqn:matrix fh 3}
\left. v = \left( \begin{array}{ccc}
1 \\
0 \\
0 \end{array} \right) \text{ cyclic} \right\} \Big/ \text{conjugation by } g = \left( \begin{array}{ccc}
1 & 0 & 0 \\
0 & c & 0 \\
0 & t & d \end{array} \right)$$ Note that in the presentation above, we fixed the vector $v$ (and this fixes the first column of the conjugating matrix) to eliminate certain coordinates. Note that the map $\mathrm{FHilb}_3 \rightarrow \mathrm{FHilb}_2$ is given by only retaining the top $2 \times 2$ corners of the matrices in question. If one is given the eigenvalues $x_1,x_2,x_3$ and the point $[a:b] \in \mathbb{P}^1$, then the datum one needs to construct a point in $\mathrm{FHilb}_3$ is the vector: $$\label{eqn:dat}
(\alpha_1, \alpha_2, \beta_1, \beta_2) \in \mathcal{T}_2^\vee \oplus \mathcal{T}_2^\vee$$ To ensure that the equation $[X,Y]=0$ is satisfied, we need to ensure that: $$(x_1-x_3)\beta_1 = \alpha_2b - \beta_2 a \quad \text{and} \quad (x_2-x_3)\beta_2 = 0$$ Moreover, the fact that we quotient out by conjugation matrices implies that we must identify: $$(\alpha_1, \alpha_2, \beta_1, \beta_2) \sim (\alpha_1 + ta, \alpha_2+t(x_2-x_3), \beta_1 + tb, \beta_2) \quad \text{and} \quad (\alpha_1,\alpha_2,\beta_1,\beta_2) \sim d(\alpha_1,\alpha_2,\beta_1,\beta_2)$$ for $t \in \mathbb{C}$ and $d\in \mathbb{C}^*$. Unwinding these facts, one sees that the datum [\[eqn:dat\]](#eqn:dat){reference-type="eqref" reference="eqn:dat"} corresponds to a vector in $H^0(\mathcal{E}^\vee_2)$, where $\mathcal{E}_2$ is the complex in [\[eqn:complex\]](#eqn:complex){reference-type="eqref" reference="eqn:complex"} when $* = \mathbb{C}$. It is elementary to prove that $\mathcal{E}_2$ and $\mathcal{E}_2^\vee$ are quasi-isomorphic to their zero-th cohomology, so we conclude that $\mathrm{FHilb}_3 = \mathrm{FHilb}_3^\text{dg}$. The irreducible components of the flag Hilbert scheme $\mathrm{FHilb}_3$ are: $$\mathrm{FHilb}_3(\mathbb{C}) = Z_1 \cup Z_2 \cup Z_3 \cup Z_4 \cup Z_5$$ where $Z_1,\ldots,Z_5$ are determined by which eigenvalues $x_1,x_2,x_3$ are equal to each other: $$Z_1 = \overline{\{x_1 \neq x_2 \neq x_3 \neq x_2\}}, \qquad Z_2 = \{x_1=x_2=x_3\}$$ $$Z_3 = \overline{\{x_1 = x_2 \neq x_3\}}, \ Z_4 = \overline{\{x_3 = x_1 \neq x_2\}}, \ Z_5 = \overline{\{x_2 = x_3 \neq x_1\}}$$ On $Z_1$, because the eigenvalues are generically distinct, the commutation relation $[X,Y]=0$ forces $Y=0$. Then the cyclicity of the vector $v$ implies $a,\alpha \neq 0$, and so conjugation by $g$ allows one to set $a = \alpha = 1$ and $e=0$. We conclude that: $$\label{eqn:z1}
Z_1 = \mathbb{C}^3$$ As for $Z_2$, note that one can always subtract a constant matrix from $X$ without changing any of the other properties of [\[eqn:matrix fh 3\]](#eqn:matrix fh 3){reference-type="eqref" reference="eqn:matrix fh 3"}. By [\[eqn:pt 3\]](#eqn:pt 3){reference-type="eqref" reference="eqn:pt 3"}, we see that: $$\label{eqn:z2}
Z_2 = \mathrm{FHilb}_2(\mathrm{point}) \times \mathbb{C}= \mathbb{P}_{\mathbb{P}^1} \left( \frac {\mathcal{O}(1)}{qt} \oplus \mathcal{O}(-2) \right) \times \mathbb{C}$$
