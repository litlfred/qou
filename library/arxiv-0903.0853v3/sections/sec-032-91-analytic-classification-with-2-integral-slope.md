---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-032-91-analytic-classification-with-2-integral-slope
section_title: "Analytic classification with $2$ integral slopes"
section_number: 9.1
pages: 43-45
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.946
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:twointegralslopes label="subsection:twointegralslopes"}

From the results of [\[subsection:extensionsofqdifferencemodules\]](#subsection:extensionsofqdifferencemodules){reference-type="ref" reference="subsection:extensionsofqdifferencemodules"}, we get the following result for the case of two slopes. Here, and after, we write, for $\mu < \nu \in {\mathbf Z}$: $$\label{not36}
K_{\mu,\nu} := \sum_{i=0}^{\nu - \mu - 1} {\mathbf C}z^{i} \text{~or, at will:~}
K_{\mu,\nu} := \sum_{i=\mu}^{\nu - 1} {\mathbf C}z^{i}.$$ (The second choice is motivated by good tensor properties, see for instance [@RS1].) Then, for $r,s \in {\mathbf N}^{*}$, we denote ${\text{Mat}}_{r,s}(K_{\mu,\nu})$ the space of $r \times s$ matrices with coefficients in $K_{\mu,\nu}$.

::: prop
[]{#prop:espaceadeuxpentes label="prop:espaceadeuxpentes"} Let $U \in {\text{Mat}}_{r_{1},r_{2}}({{\mathbf C}(\{z\})})$. Then, there exists a unique pair: $$\label{not37}
Red(\mu_{1},A_{1},\mu_{2},A_{2},U) := 
(F_{1,2},V) \in {\text{Mat}}_{r_{1},r_{2}}({{\mathbf C}(\{z\})}) \times {\text{Mat}}_{r_{1},r_{2}}(K_{\mu_{1},\mu_{2}})$$ such that: $$(\sigma_qF_{1,2}) z^{\mu_{2}} A_{2} - z^{\mu_{1}} A_{1} F_{1,2} = U - V,$$ that is: $$\begin{pmatrix} I_{r_{1}} & F_{1,2} \\ 0 & I_{r_{2}} \end{pmatrix}:
\begin{pmatrix}
z^{\mu_{1}} A_{1} &  V            \\
0              & z^{\mu_{2}} A_{2} 
\end{pmatrix} \simeq
\begin{pmatrix}
z^{\mu_{1}} A_{1} &  U            \\
0              & z^{\mu_{2}} A_{2} 
\end{pmatrix}.$$
:::

::: proof
*Proof.* Using the reductions of lemma [\[lemm:dimensiondeuxpentes\]](#lemm:dimensiondeuxpentes){reference-type="ref" reference="lemm:dimensiondeuxpentes"}, this is just a rephrasing of lemma [\[lemm:supplementairedeuxpentes\]](#lemm:supplementairedeuxpentes){reference-type="ref" reference="lemm:supplementairedeuxpentes"}. ◻
:::

We consider $V$ as a *polynomial normal form* for the class of $M_{U}$ and $F_{1,2}$ as the corresponding reduction datum. Of course, they depend on the choice of the space of coefficients $K_{\mu_{1},\mu_{2} }$.\

::: exem
[]{#exem:archetypal label="exem:archetypal"} This is the archetypal example (and strongly related to the prototypal example of subsection [\[subsection:prototypal\]](#subsection:prototypal){reference-type="ref" reference="subsection:prototypal"}), from which much of the theory is built. Fix $c \in {\mathbf C}^{*}$. For any $f,u,v \in {{\mathbf C}(\{z\})}$, the isomorphism: $\begin{pmatrix}1 & f \\ 0 & 1 \end{pmatrix}:
\begin{pmatrix} 1 & v \\ 0 & cz \end{pmatrix} \simeq
\begin{pmatrix} 1 & u \\ 0 & cz \end{pmatrix}$ is equivalent to the inhomogeneous $q$-difference equation: $c z \sigma_qf - f = u - v$. Writing $f = \sum f_{n} z^{n}$, etc, we find the conditions: $$c q^{n-1} f_{n-1} - f_{n} = u_{n} - v_{n} \Longleftrightarrow
\dfrac{f_{n-1}}{c^{n-1} q^{(n-1)(n-2)/2}} - \dfrac{f_{n}}{c^{n} q^{n(n-1)/2}} = 
\dfrac{u_{n} - v_{n}}{c^{n} q^{n(n-1)/2}},$$ which admit an analytic solution $f$ if, and only if, ${\mathcal{B}_{q,1}}u(c^{-1}) = {\mathcal{B}_{q,1}}v(c^{-1})$ (recall that the $q$-Borel transform ${\mathcal{B}_{q,1}}$ was defined in definition [\[defi:qBorel\]](#defi:qBorel){reference-type="ref" reference="defi:qBorel"} page ). The analytic class of the module with matrix $\begin{pmatrix} 1 & u \\ 0 & cz \end{pmatrix}$ within the formal class $\begin{pmatrix} 1 & 0 \\ 0 & cz \end{pmatrix}$ is therefore ${\mathcal{B}_{q,1}}u(c^{-1}) \in {\mathbf C}$. Writing $f_{u}$ the unique solution in ${{\mathbf C}(\{z\})}$ of the equation $c z \sigma_qf - f = u - {\mathcal{B}_{q,1}}u(c^{-1})$, we have $Red(0,1,1,c,u) = \bigl(f_{u},{\mathcal{B}_{q,1}}u(c^{-1})\bigr)$.\
Note that equation $c z \sigma_qf - f = u$ always admits a unique formal solution $\hat{f}_{u}$. For instance, for $u \in {\mathbf C}$, we find that $\hat{f}_{u} = - u \text{\tencyr\cyracc Ch}(c z)$, where $\text{\tencyr\cyracc Ch}$ is the Tshakaloff series []{#not38 label="not38"} defined by [\[eqn:Tshakaloff\]](#eqn:Tshakaloff){reference-type="eqref" reference="eqn:Tshakaloff"} page . We infer that, for a general $u \in {{\mathbf C}(\{z\})}$, one has $\hat{f}_{u} = f_{u} - {\mathcal{B}_{q,1}}u(c^{-1}) \text{\tencyr\cyracc Ch}(c z)$.
:::

::: exem
In proposition [\[prop:espaceadeuxpentes\]](#prop:espaceadeuxpentes){reference-type="ref" reference="prop:espaceadeuxpentes"}, we meet the equation $(\sigma_qF_{1,2}) z^{\mu_{2}} A_{2} - z^{\mu_{1}} A_{1} F_{1,2} = U - V$. Here is an explicit resolution that does not go through all the reductions of [\[subsection:extensionsofqdifferencemodules\]](#subsection:extensionsofqdifferencemodules){reference-type="ref" reference="subsection:extensionsofqdifferencemodules"}. We write $X = \sum X_{n} z^{n}$ for $F_{1,2}$ and $Y = \sum Y_{n} z^{n}$ for $U - V$. We have: $$\begin{aligned}
(\sigma_qX) z^{\mu_{2}} A_{2} - z^{\mu_{1}} A_{1} X = Y & \Longleftrightarrow
\forall n ~,~ 
q^{n - \mu_{2}} X_{n - \mu_{2}} A_{2} - A_{1} X_{n - \mu_{1}} = Y_{n} \\
& \Longleftrightarrow
\forall n ~,~ q^{n - d} X_{n - d} A_{2} - A_1 X_{n} = 
Y_{n + \mu_{1}}, \\
& \Longleftrightarrow
\forall n ~,~ q^{n - d} A_{1}^{-1} X_{n - d} A_{2} - X_{n} = 
Z_{n} := A_{1}^{-1} Y_{n + \mu_{1}},
\end{aligned}$$ where we denote $d := \mu_{2} - \mu_{1} \in {\mathbf N}^{*}$ the *level* of the above inhomogeneous equation. (The second equivalence is obtained by a mere translation of indices.) It follows from [@Bezivin], [@RamisGrowth] that, for any analytic $Y$, this has a formal solution of $g$-Gevrey level $d$ (this was defined in paragraph [\[subsection:qGevreylevels\]](#subsection:qGevreylevels){reference-type="ref" reference="subsection:qGevreylevels"} of the general notations, in the introduction); it also follows from *loc.cit* that, if there is a solution of $q$-Gevrey level $d' > d$ (which is a stronger condition), then, there is an analytic solution. To solve our equation, we introduce a $q$-Borel transform of level $d$. This depends on an arbitrary family $(t_{n})_{n \in {\mathbf Z}}$ in ${\mathbf C}^{*}$, subject to the condition: $$\forall n ~,~ t_{n} = q^{n-d} t_{n-d}.$$ For $d = 1$, the natural choice is $t_{n} := q^{n(n-1)/2}$. In general, such a family can be built from Jacobi theta functions as in [@RS1]. At any rate, $t_{n}$ has the order of growth of $q^{n^{2}/2 d}$. The $q$-Borel transform is then defined by: $$\label{not39}
{\mathcal{B}}_{q,d} \left(\sum f_{n} z^{n}\right) := \sum \dfrac{f_{n}}{t_{n}} \xi^{n}.$$ We must also choose $d^{th}$ roots $B_{1},B_{2}$ of $A_{1},A_{2}$. Then, writing ${\mathcal{B}}_{q,d} X = \sum \tilde{X}_{n} z^{n}$, etc, we find the relations: $$\forall n ~,~ 
B_{1}^{-d} \tilde{X}_{n-d} B_{2}^{d} - \tilde{X}_{n} = \tilde{Z}_{n} 
\Longleftrightarrow
\forall n ~,~ B_{1}^{n-d} \tilde{X}_{n-d} B_{2}^{-(n-d)} - 
B_{1}^{n} \tilde{X}_{n}  B_{2}^{-n} = B_{1}^{n} \tilde{Z}_{n} B_{2}^{-n}.$$ Thus, a necessary condition for the existence of an analytic solution $X$ is that, for all $i$ in a set of representatives modulo $d$, one has: $$\sum_{n \equiv i \pmod{d}} B_{1}^{n} \tilde{Z}_{n} B_{2}^{-n} = 0.$$ This provides us with $d$ obstructions in ${\text{Mat}}_{r_{1},r_{2}}({\mathbf C})$ and it is not hard to prove, along the same lines as what has been done, that these form a complete set of invariants. More precisely, the map which sends $U$ to the $d$-uple of matrices $\sum\limits_{n \equiv i \pmod{d}} \dfrac{1}{t_{n}} B_{1}^{n-d} U_{n + \mu_{1}} B_{2}^{-n}$ yields an isomorphism of ${\mathcal{F}}(P_{1},P_{2})$ with ${\text{Mat}}_{r_{1},r_{2}}({\mathbf C})^{d}$. Different choices of the family $(t_{n})$ and the matrices $B_{1},B_{2}$ induce different isomorphisms.
:::
