---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-022-027-actions-of-c-quantum-groupoids-on-von-neuman
section_title: "Actions of $C^*$-quantum groupoids on von Neumann algebras"
section_number: 0.27
pages: 32-33
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.667
latex_coverage_ratio: 0.959
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
Let a von Neumann algebra $M$ be a left $H$-module algebra in the sense of Definition [\[module algebra\]](#module algebra){reference-type="ref" reference="module algebra"} via a weakly continuous action of a $C^*$-quantum groupoid $$H\otimes_\mathbb{C} M \ni  x\otimes m \mapsto (x\triangleright m)\in M$$ such that $(x\triangleright m)^* = S(x)^* \triangleright m^*$ and $x\triangleright 1 =0$ iff $\varepsilon_t(t)=0.$

Then one can show ([@NSzW], 3.4.2) that the smash product algebra (now we call it *crossed product algebra* and denote by $M{>\!\!\!\triangleleft}H$), equipped with an involution $[m\otimes x]^* = [(x_{(1)}^*\triangleright m^*) \otimes  x_{(2)}^*]$, is a von Neumann algebra.

The collection $M^H =\{ m\in M \mid x\triangleright m = \varepsilon_t(x)\triangleright m,\ \forall x\in H\}$ is a von Neumann subalgebra of $M$, called a *fixed point subalgebra*. The centralizer $M^\prime \cap M {>\!\!\!\triangleleft}H$ always contains a the source counital subalgebra $H_s$. Indeed, if $y\in H_s$, then $\Delta(y) =1_{(1)}\otimes 1_{(2)} y$, therefore $$\begin{aligned}
&=& [(y_{(1)}\triangleright m)\otimes y_{(2)}]=[(1_{(1)}\triangleright m)\otimes  1_{(2)} y] \\
&=& [m\otimes y]=[m\otimes 1][1\otimes y],
\end{aligned}$$ for any $m\in M$, and $H_s\subset M^\prime \cap M {>\!\!\!\triangleleft}H$. An action of $H$ is called *minimal* if $H_s = M^\prime \cap M{>\!\!\!\triangleleft}H$.

One can define the dual action of $\widehat H$ on the von Neumann algebra $M{>\!\!\!\triangleleft}H$ as in ([\[dual action\]](#dual action){reference-type="ref" reference="dual action"}) and construct the von Neumann algebra $(M{>\!\!\!\triangleleft}H) {>\!\!\!\triangleleft}\widehat H$.

::: remark
The following results hold true if $S^2=\mbox{id}$, i.e., if $H$ is involutive ([@N1], 4.6, 4.7).

1.  $M\subset M{>\!\!\!\triangleleft}H\subset (M{>\!\!\!\triangleleft}H)
    {>\!\!\!\triangleleft}\widehat H$ is a basic construction;

2.  $M{>\!\!\!\triangleleft}H$ is free as a left $M$-module;

3.  $(M{>\!\!\!\triangleleft}H){>\!\!\!\triangleleft}\widehat H \cong M\otimes_\mathbb{C}
    M_n(\mathbb{C})$ for some integer $n$.
:::

::: example
[]{#Weyl algebra label="Weyl algebra"} For a trivial action of $H$ on $H_t$ and the corresponding dual action of $\widehat H$ on $H\cong H_t{>\!\!\!\triangleleft}H$ (see Example [\[examples of actions\]](#examples of actions){reference-type="ref" reference="examples of actions"} (i) and (ii)), $H_t\subset H\subset H{>\!\!\!\triangleleft}\widehat H$ is the basic construction of finite-dimensional $C^*$-algebras with respect to the Haar conditional expectation $E_t$ ([@BSz2], 4.2).
:::

If $H$ is a connected $C^*$-quantum groupoid having a minimal action on a II${}_1$ factor $M$ then one can show ([@NSzW], 4.2.5, 4.3.5) that $\widehat H$ is also connected and that $$N=M^H\subset M\subset M_1=M {>\!\!\!\triangleleft}H\subset M_2=(M{>\!\!\!\triangleleft}H){>\!\!\!\triangleleft}\widehat H
\subset \cdots$$ is the Jones tower of factors of finite index with *the derived tower* $$N'\cap N=\mathbb{C}\subset N'\cap M=H_t\subset N'\cap M_1=H\subset N'\cap M_2=
H{>\!\!\!\triangleleft}\widehat H\subset  \cdots$$ The fact that the last triple of finite-dimensional $C^*$-algebras is a basic construction, means exactly that the subfactor $N\subset M$ has depth 2. Moreover, the finite-dimensional $C^*$-algebras $$\label{square}
\begin{array}{ccc}
H^* & \subset & H^* {>\!\!\!\triangleleft}H  \\
\cup&         & \cup        \\   
H_t= H_s^* & \subset & H,
\end{array}$$ form *a canonical commuting square*, which completely determines the equivalence class of the initial subfactor. This implies that any biconnected $C^*$-quantum groupoid has at most one minimal action on a given II$_1$ factor and thus corresponds to no more than one (up to equivalence) finite index depth 2 subfactor.

::: remark
It was shown in ([@N1], 5) that any biconnected involutive $C^*$-quantum groupoid has a minimal action on the hyperfinite II$_1$ factor. This action is constructed by iterating the basic construction for the square ([\[square\]](#square){reference-type="ref" reference="square"}) in the horizontal direction, see [@N1] for details.
:::
