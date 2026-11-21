---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-024-61-a-prototypal-example-and-the-q-borel-transfor
section_title: "A prototypal example and the $q$-Borel transformation"
section_number: 6.1
pages: 28-31
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.979
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:prototypal label="subsection:prototypal"}

To give a feeling of the situation encountered we introduce at once a prototypal example. To begin with, we only assume that $K := {{\mathbf C}(\{z\})}$ or $K := {{\mathbf C}((z))}$ without choosing. This will allow us to treat both the formal and the analytical situations, and to see clearly the difference.\
Let $P_{1} := (K,\Phi_1) = (K,\sigma_q)$ and $P_{2} := (K,\Phi_z) = (K,z^{-1} \sigma_q)$. These pure isoclinic modules of respective slopes $0$ and $1$ correspond to the rank $1$ systems $\sigma_qf = f$ and $\sigma_qf = z f$. The pure module $M_0 := P_1 \oplus P_2$ defines a formal class and we intend to compute the set ${\mathcal{F}}(M_0) = {\mathcal{F}}(P_1,P_2)$ of isoformal analytic classes. We thus consider $q$-difference modules $M$ endowed with a submodule $M_1$ and two isomorphisms: $M_1 \rightarrow P_1$ and $M/M_1 \rightarrow P_2$. Such a module $M$ has the form $M_u = (K^2,\Phi_A)$ for some $u \in K$, where: $$A = A_u := \begin{pmatrix} 1 & u \\ 0 & z \end{pmatrix}.$$ (Thus, setting $u := 0$ indeed yields $M_0$.) Note that this description encompasses the additional structure provided by the isomorphism ${\text{gr}}\ M_u \simeq M_0$. Equivalence of two such objects $M_u$ and $M_v$ is given by an isomorphism described in matricial form as: $$F := \begin{pmatrix} 1 & f \\ 0 & 1 \end{pmatrix}:
\begin{pmatrix} 1 & u \\ 0 & z \end{pmatrix} \simeq
\begin{pmatrix} 1 & v \\ 0 & z \end{pmatrix}
\Longleftrightarrow (\sigma_qF) A_u = A_v F.$$ The fact that $F$ has this precise shape (unipotent and upper triangular) corresponds to the condition $g = g' \circ {\text{gr}}(f)$ in the definition of our equivalence relation (definition [\[defi:analyticisoformalclass\]](#defi:analyticisoformalclass){reference-type="ref" reference="defi:analyticisoformalclass"}).\
The relation $(\sigma_qF) A_u = A_v F$ is in turn equivalent to the first order inhomogeneous $q$-difference equation: $$z \sigma_qf - f = v - u.$$ So we are actually interested in the cokernel of the mapping $\Psi: f \mapsto z \sigma_qf - f$ from $K$ to itself.\
Now, if $K = {{\mathbf C}((z))}$, this mapping is bijective and admits as inverse the mapping $w \mapsto - \sum_{n \geq 0} (z \sigma_q)^n w$ (this is well defined in the $z$-adic topology). Therefore, for all $u,v \in {{\mathbf C}((z))}$, the equation $z \sigma_qf - f = v - u$ admits a unique solution $f$ in ${{\mathbf C}((z))}$, so that there is a unique class in ${\mathcal{F}}(P_{1},P_{2})$, that of the pure module $M_0 = P_1 \oplus P_2$.\
However, if $K = {{\mathbf C}(\{z\})}$, one proves that $\Psi$ is injective (this is obvious) and that its cokernel is isomorphic to ${\mathbf C}$. More precisely, for each $u \in {{\mathbf C}(\{z\})}$, there exists a unique $u_0 \in {\mathbf C}$ such that the equation $z \sigma_qf - f = u - u_0$ admits a solution; and $u_0$ can be explicitly computed, as we shall now see.

[]{#not25 label="not25"}

::: defi
[]{#defi:qBorel label="defi:qBorel"} The *$q$-Borel transform* of $f(z) := \sum f_{n} z^{n} \in {{\mathbf C}(\{z\})}$ is defined as: $${\mathcal{B}_{q,1}}f(\xi) := \sum \dfrac{f_{n}}{q^{n(n-1)/2}} \xi^{n}.$$
:::

::: rema
Actually, this is the transformation at *level $1$*; for general properties of ${\mathcal{B}_{q,1}}$ see [@RamisGrowth]. Also note the customary use of the new variable $\xi$ in the so-called *Borel plane*.
:::

Clearly, the radius of convergence of $f$ being $> 0$, that of ${\mathcal{B}_{q,1}}f$ is infinite (under our general convention that $\left |q \right |> 1$). More precisely, the ${\mathbf C}$-linear mapping ${\mathcal{B}_{q,1}}$ sends ${{\mathbf C}(\{z\})}$ isomorphically to the following subspace of ${\mathcal{O}}({\mathbf C})[\xi^{-1}]$: []{#not26 label="not26"} $${\mathbf C}(\{\xi\})_{q,1} := \left\{\sum \phi_{n} \xi^{n} \in {\mathbf C}((\xi)) 
~ | ~\phi_{n} \prec q^{-n(n-1)/2}\right\}.$$ Here, $u_{n} \prec v_{n}$ means: $u_{n} = O(A^{n} v_{n})$ for some $A > 0$.\
Introduction of the $q$-Borel transform is motivated by the following easily checked property: $$\begin{aligned}
z \sigma_qf - f = g 
& \Longleftrightarrow \forall n ~,~ q^{n-1} f_{n-1} - f_{n} = g_{n} \\
& \Longleftrightarrow \forall n ~,~ 
\dfrac{f_{n-1}}{q^{(n-1)(n-2)/2}} - \dfrac{f_{n}}{q^{n(n-1)/2}} =
\dfrac{g_{n}}{q^{n(n-1)/2}} \\
& \Longleftrightarrow (\xi - 1) {\mathcal{B}_{q,1}}f(\xi) = {\mathcal{B}_{q,1}}g(\xi).
\end{aligned}$$ We therefore get a commutative diagram: $$\begin{CD}
  {{\mathbf C}(\{z\})}@>{1 - z \sigma_q}>>      {{\mathbf C}(\{z\})}\\
@VV{{\mathcal{B}_{q,1}}}V         @VV{{\mathcal{B}_{q,1}}}V        \\
  {\mathbf C}(\{\xi\})_{q,1}  @>{\times(1-\xi)}>>  {\mathbf C}(\{\xi\})_{q,1}  
\end{CD}$$ The vertical arrows are isomorphisms and the right one sends ${\mathbf C}\subset {{\mathbf C}(\{z\})}$ onto ${\mathbf C}\subset {\mathbf C}(\{\xi\})_{q,1}$. (The fact that $\times(1-\xi)$ does send ${\mathbf C}(\{\xi\})_{q,1}$ into itself is easily checked.)

::: lemm
[]{#lemm:qBorel label="lemm:qBorel"} The image of the lower horizontal arrow is the subspace $\{\phi \in {\mathbf C}(\{\xi\})_{q,1} ~ | ~\phi(1) = 0\}$.
:::

::: proof
*Proof.* It is obvious that $\phi(1)$ makes sense for any $\phi \in {\mathbf C}(\{\xi\})_{q,1}$ and so that any $\phi$ in the image satisfies $\phi(1) = 0$. If $\phi(1) = 0$, it is also clear that $\psi := \dfrac{\phi}{1 - \xi} \in {\mathcal{O}}({\mathbf C})[\xi^{-1}]$, and we are left to prove that $\psi \in {\mathbf C}(\{\xi\})_{q,1}$. So we write $\phi = \sum a_{n} \xi^{n}$, $\psi = \sum b_{n} \xi^{n}$, so that we have $\sum a_{n} = 0$ and: $$b_{n} = \sum_{p \leq n} a_{p} = - \sum_{p > n} a_{p}.$$ Suppose that $\left |a_{n} \right |\leq C A^{n} \left |q \right |^{-n(n-1)/2}$ for all $n$, where $C,A > 0$. Then: $$\begin{aligned}
\left |b_{n} \right |\leq C \sum_{p > n} A^{p} \left |q \right |^{-p(p-1)/2} & \leq 
C A^{n} \left |q \right |^{-n(n-1)/2} 
\sum_{\ell > 0} A^{\ell} \left |q \right |^{-\ell(2 n + \ell -1)/2} \\
& \leq C' A^{n} \left |q \right |^{-n(n-1)/2},
\end{aligned}$$ where $C' := \sum\limits_{\ell > 0} A^{\ell} \left |q \right |^{-\ell(\ell -1)/2} < \infty$. ◻
:::

::: prop
[]{#prop:qBorel label="prop:qBorel"} One has a splitting of ${\mathbf C}$-vector spaces: $${{\mathbf C}(\{z\})}= {\mathbf C}\oplus \text{Im~} \Psi.$$ The corresponding projection operators are $u \mapsto {\mathcal{B}_{q,1}}u(1)$ and $u \mapsto u - {\mathcal{B}_{q,1}}u(1)$
:::

::: proof
*Proof.* It follows from the lemma that the image of the upper horizontal arrow in the commutative diagram above is $\{g \in {{\mathbf C}(\{z\})}~ | ~{\mathcal{B}_{q,1}}g(1) = 0\}$. The conclusion follows easily. ◻
:::

Thus, the only *obstruction* in solving $z \sigma_qf - f = g$ analytically is ${\mathcal{B}_{q,1}}g(1)$ (we saw that solving formally is always possible). Therefore, each $u \in {{\mathbf C}(\{z\})}$ is equivalent to a unique $u_0 \in {\mathbf C}$ modulo $\text{Im} \Psi$, and $u_0 = {\mathcal{B}_{q,1}}u(1)$.\
This implies that the map $u \mapsto M_u$ induces a bijection of ${\mathbf C}$ with ${\mathcal{F}}(P_{1},P_{2})$. Moreover, we have representatives in "normal form" $\begin{pmatrix} 1 & u \\ 0 & z \end{pmatrix}$ with $u_0 \in {\mathbf C}$, a particular case of the "Birkhoff-Guenther normal form" (subsection [\[subsection:BGNF\]](#subsection:BGNF){reference-type="ref" reference="subsection:BGNF"}). Note that this normal form rests on a transcendental computation.

::: exem
If we take for instance $u := 1$ and $v := 0$, we see that the unique formal solution of the equation $z \sigma_qf - f = v - u$ is the Tshakaloff series defined in [\[eqn:Tshakaloff\]](#eqn:Tshakaloff){reference-type="eqref" reference="eqn:Tshakaloff"}, page , and considered as a $q$-analogue of the Euler series $\sum n! z^n$. In the same way as the latter is the simplest non trivial object in the analytical classification of complex linear differential equations so is the former for $q$-difference equations. As such, it will follow us, see *e.g.* example [\[exem:archetypal\]](#exem:archetypal){reference-type="ref" reference="exem:archetypal"} page , example [\[exem:Tshakaloff7\]](#exem:Tshakaloff7){reference-type="ref" reference="exem:Tshakaloff7"} page and the more detailed study in section [\[section:qEuler\]](#section:qEuler){reference-type="ref" reference="section:qEuler"} of chapter [\[chapter:examplesStokes\]](#chapter:examplesStokes){reference-type="ref" reference="chapter:examplesStokes"}.
:::

::: rema
[]{#rema:badquotient2 label="rema:badquotient2"} In the notations of remark [\[rema:badquotient1\]](#rema:badquotient1){reference-type="ref" reference="rema:badquotient1"}, it is clear that $\text{Aut}(P_{1}) = \text{Aut}(P_{2}) = {\mathbf C}^{*}$ and it is easy to see that the action of $\text{Aut}(P_{1}) \times \text{Aut}(P_{2}) = {\mathbf C}^{*} \times {\mathbf C}^{*}$ on ${\mathcal{F}}(P_{1},P_{2}) = {\mathbf C}$ is given by $(t_1,t_2).u := (t_1/t_2)u$. Thus one is led to the quotient ${\mathbf C}/{\mathbf C}^{*}$, which is rather badly behaved: it consists of two points $0,\overline{1}$, the second being dense.
:::
