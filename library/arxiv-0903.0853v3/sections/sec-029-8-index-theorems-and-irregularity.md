---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-029-8-index-theorems-and-irregularity
section_title: "Index theorems and irregularity"
section_number: 8
pages: 38-40
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.952
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:indextheorems label="section:indextheorems"}

We shall now give some complements to the results in [\[subsection:extensionsofqdifferencemodules\]](#subsection:extensionsofqdifferencemodules){reference-type="ref" reference="subsection:extensionsofqdifferencemodules"}, in the form of index theorems. They mostly originate in the works [@Bezivin] of Bézivin[^1] and also in [@RamisGrowth]: the difference here is merely the adaptation to our formalism. Although not strictly necessary for what follows, these results allow for an interpretation of $\dim {\mathcal{F}}(P_{1},\ldots,P_{k})$ (theorem [\[theo:schemadesmodules\]](#theo:schemadesmodules){reference-type="ref" reference="theo:schemadesmodules"}) in terms of "irregularity", as in the paper [@Ma3] of Malgrange.\
In most of this section, we write $K$ for (indifferently) ${{\mathbf C}((z))}$ or ${{\mathbf C}(\{z\})}$ and respectively speak of the *formal* or *convergent* case. We intend to compute the index of an analytic $q$-difference operator $P \in {{\mathcal{D}}_{q}}$ acting upon ${{\mathbf C}((z))}$ and ${{\mathbf C}(\{z\})}$ (and, in the end, upon ${{\mathbf C}((z))}/{{\mathbf C}(\{z\})}$). To begin with, we do not assume $P$ to have analytic coefficients.

## Kernel and cokernel of $\sigma_q- u$

We start with the case $\deg P = 1$. Up to an invertible factor in ${{\mathcal{D}}_{q}}$, we may assume that $P = \sigma_q- u$, where $u = d q^{k} z^{\nu} v$, $v \in K, \; v(0) = 1$, with $k \in {\mathbf Z}$ and $d \in {\mathbf C}^{*}$ such that $1 \leq |d| < \left |q \right |$. We consider $P$ as a ${\mathbf C}$-linear operator on $K$.

::: enonce*
Fact The dimensions over ${\mathbf C}$ of the kernel and cokernel of $P$ depend only of the class of $u \in K^{*}$ modulo the subgroup $\{\frac{\sigma_q(w)}{w} ~ | ~w \in K^{*}\}$ of $K^{*}$. This class is equal to that of a $d z^{\nu}$.
:::

::: proof
*Proof.* Conjugating the ${\mathbf C}$-linear endomorphism $\sigma_q- u$ of $K$ by $w \in K^{*}$ (undestood as the automorphism $\times w$), one finds: $$w \circ (\sigma_q- u) \circ w^{-1} = 
\frac{w}{\sigma_q(w)} \circ (\sigma_q- u'),
\text{~with~} u' = u \frac{\sigma_q(w)}{w},$$ whence the first statement. Then, $q^{k} v = \frac{\sigma_q(w)}{w}$, where $w = z^{k} \underset{i \geq 1}{\prod} \sigma_q^{-i}(v) \in K$ (also well defined in the convergent case), whence the second statement. ◻
:::

So we now set $u := d z^{\nu}$.

::: enonce*
Fact The kernel of $\sigma_q- u : K \rightarrow K$ has dimension $1$ if $(\nu,d) = (0,1)$, and $0$ otherwise.
:::

::: proof
*Proof.* The series $f = \sum f_{n} z^{n}$ belongs to the kernel if, and only if $\forall n \;,\, q^{n} f_{n} = d f_{n - \nu}$. Since we deal with Laurent series having poles, this implies $f = 0$ except maybe if $\nu = 0$. In the latter case, it implies $f = 0$, except maybe if $d \in q^{{\mathbf Z}}$. From the condition on $|d|$, this is only possible if $d = 1$, thus $u = 1$. In that case, the kernel is plainly ${\mathbf C}$. ◻
:::

::: enonce*
Fact The map $\sigma_q- u : K \rightarrow K$ is onto if $\nu >0$ and also if $\nu = 0, \; d \not= 1$.
:::

::: proof
*Proof.* Let $g \in K$. We look for $f$ solving the equation $\sigma_qf - d z^{\nu} f = g$ in $K$. This is equivalent to: $\forall n \;,\, q^{n} f_{n} - d f_{n - \nu} = g_{n}$, that is, $\forall n \;,\, f_{n} = q^{-n} (d f_{n - \nu} + g_{n})$. If $\nu \geq 1$, one computes the coefficients by induction from the $\nu$ first among them. Moreover, in the convergent case, inspection of the denominators show that $f$ converges if $g$ does; and then, the functional equation ensures meromorphy. If $\nu = 0$ and $d \not= 1$ (so that $d \notin q^{{\mathbf Z}}$), one gets rightaway $f_{n} = \frac{g_{n}}{q^{n} - d}$. Convergence (resp. meromorphy) is then immediate in the convergent case. (When $\nu \geq 1$, one can also consider the fixpoint equation $F(f) = f$, where $F(f) := \sigma_q^{-1}(g + d z^{\nu} f)$: it is easy to see that this is a contracting operator as well for the formal topology, *i.e.* for $z$-adic convergence, as for the transcendant topology, *i.e.* for usual convergence.) ◻
:::

::: enonce*
Fact If $(\nu,d) = (0,1)$, the cokernel of $\sigma_q- u : K \rightarrow K$ has dimension $1$.
:::

::: proof
*Proof.* One checks that $\sigma_q- u$ vanishes on ${\mathbf C}$ and induces an automorphism of the subspace $K^{\bullet}$ of $K$ made up of series without constant term. ◻
:::

::: enonce*
Fact Assume $\nu < 0$. Then $\sigma_q- u : K \rightarrow K$ is onto in the formal case.
:::

::: proof
*Proof.* Put $F'(f) = d^{-1} z^{- \nu} (\sigma_q(f) - g)$. Since $\nu > 0$, this is a $z$-adically contracting operator, whence the existence (and unicity) of a fixed point. ◻
:::

::: rema
This is the first place where the formal and convergent cases differ. The operator is (rather strongly) *expanding* for the transcendant topology, it produces Stokes phenomena! So this is where we need an argument from analysis in the convergent case.
:::

::: enonce*
Fact Assume $\nu = - r, r \in {\mathbf N}^{*}$. Then, in the convergent case, the cokernel of $\sigma_q- u : K \rightarrow K$ has dimension $r$.
:::

::: proof
*Proof.* This is a consequence of lemma [\[lemm:dimensiondeuxpentes\]](#lemm:dimensiondeuxpentes){reference-type="ref" reference="lemm:dimensiondeuxpentes"} (and therefore relies on the use of the $q$-Borel transformation). ◻
:::

We now summarize our results:

::: prop
[]{#prop:indices label="prop:indices"} Let $u = d z^{\nu} v$, $v \in K, \; v(0) = 1$, with $d \in {\mathbf C}^{*}$. Write $\overline{d}$ the class of $d$ modulo $q^{{\mathbf Z}}$. The following table shows the ranks of the kernel and cokernel, as well as the index $\chi(P) := \dim \text{Ker~}P - \dim \text{Coker~} P$ of the ${\mathbf C}$-linear operator $P := \sigma_q- u: K \rightarrow K$:\

  $(\nu,\overline{d})$      Kernel   Cokernel                                        Index
  ---------------------- -- -------- ----------------------------------------------- ---------------------------------------------
  $(0,1)$                   $1$      $1$                                             $0$
  $(0,\not=1)$              $0$      $0$                                             $0$
  $(> 0,-)$                 $0$      $0$                                             $0$
  $(< 0,-)$                 $0$      $\begin{cases} 0 \text{ (formal case) } \\      $\begin{cases} 0 \text{ (formal case) } \\ 
                                     - \nu \text{ (convergent case) } \end{cases}$   \nu \text{ (convergent case) } \end{cases}$
:::

[^1]: The index computations in [@Bezivin] are more general in two directions: they apply to "difference" automorphisms that are more general that $z \mapsto q z$; and the equations are not linear.
