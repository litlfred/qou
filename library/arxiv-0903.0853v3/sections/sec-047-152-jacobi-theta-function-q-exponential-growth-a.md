---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-047-152-jacobi-theta-function-q-exponential-growth-a
section_title: "Jacobi Theta function, $q$-exponential growth and $q$-Gevrey series"
section_number: 15.2
pages: 77-79
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.828
latex_coverage_ratio: 0.931
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:JacobiTheta label="subsection:JacobiTheta"}

Jacobi's theta function $\theta(z;q) = \theta(z)$ was defined by equation [\[eqn:tripleproduit\]](#eqn:tripleproduit){reference-type="eqref" reference="eqn:tripleproduit"} page . From its functional equation, one draws: $$\forall (z,n) \in {\mathbf C}^* \times {\mathbf Z}~,~
\theta(q^nz)=q^{n(n+1)/2}~z^{n}~\theta(z).$$ Moreover, for all $z\in{\mathbf C}^*$, one has: $$\label{not65}
\left |\theta(z) \right |\leq 
e(z) := e(z;q) :=\theta\left(\left |z\right |;\left |q \right |\right).$$

::: lemm
[]{#lemm:thetamin0 label="lemm:thetamin0"} There exists a constant $C>0$, depending on $q$ only, such that, for all $\epsilon>0$: $$\left |\theta(z) \right |\geq {C}~ {\epsilon} ~ e(z),$$ as long as $d_q(z,[-1])>\epsilon$.
:::

::: proof
*Proof.* It is enough to see that the function $z \mapsto \left |\theta(z) \right |/e(z)$ is $q$-invariant, which allows one to restrict the problem to the (compact) closure of a fundamental annulus, for instance $\{z \in {\mathbf C}~ | ~1\leq \left |z \right |\leq \left |q \right |\}$. See [@zh3 Lemma 1.3.1] for more details. ◻
:::

Recall that $\theta(z) = \theta\left(\dfrac{1}{qz}\right)$; one draws from this that $e(z) = e\left(\dfrac{1}{qz}\right)$. To each subset $W$ of ${\mathbf C}$, one associates two sets $W_{(\infty)}$, $W_{(0)}$ as follows: []{#not66 label="not66"} $$W_{(\infty)} := \bigcup_{n\ge 0} q^n~ W~,\quad
W_{(0)} := \bigcup_{n\le 0}q^n~ W~.$$

::: defi
[]{#defi:croissanceqexp label="defi:croissanceqexp"} Let $f$ be a function analytic over an open subset $\Omega$ of ${\mathbf C}^*$ and let $k \geq 0$.

1.  We say that *$f$ has $q$-exponential growth of order (at most) $k$ at infinity (resp. at $0$) over $\Omega$* if, for any compact $W \subset {\mathbf C}$ such that $W_{(\infty)} \subset \Omega$ (resp. such that $W_{(0)} \subset \Omega$), there exists $C > 0$ and $\mu > 0$ such that $\left |f(z) \right |\leq C \bigl(e(\mu z)\bigr)^k$ for all $z \in W_{(\infty)}$ (resp. $z\in W_{(0)}$).

2.  We say that *$f$ has $q$-exponential decay of order (at least) $k$ at infinity (resp. at $0$) over $\Omega$* if, for any compact $W \subset {\mathbf C}$ such that $W_{(\infty)} \subset \Omega$ (resp. such that $W_{(0)} \subset \Omega$), there exists $C> 0$ and $\mu > 0$ such that $\left |f(z) \right |\leq C \bigl(e(\mu z)\bigr)^{-k}$ for all $z \in W_{(\infty)}$ (resp. $z \in W_{(0)}$).
:::

::: lemm
[]{#lemm:croissanceqexp label="lemm:croissanceqexp"} Let $k > 0$ and $f$ an entire function with Taylor expansion $f(z) = \sum\limits_{n\ge 0}a_nz^n$ at $0$. Then $f$ has $q$-exponential growth of order (at most) $k$ at infinity over ${\mathbf C}$, if, and only if, the sequence $(a_n)$ is $q$-Gevrey of order $(-1/k)$.
:::

::: proof
*Proof.* The $q$-Gevrey order of a sequence was defined in paragraph [\[subsection:qGevreylevels\]](#subsection:qGevreylevels){reference-type="ref" reference="subsection:qGevreylevels"} of the general notations, in the introduction. A variant of this result was given in [@RamisGrowth Proposition 2.1]. The proof shown below rests on the functional equation $\theta(qz) = q~ z~ \theta(z)$.

If $(a_n)$ is $q$-Gevrey of order $(-k)$, one has $\left |f(z) \right |\leq C~\theta(\mu \left |z \right |; \left |q \right |^{1/k})$, which shows that $f$ has $q$-exponential growth of order (at most) $k$ at infinity over ${\mathbf C}$.

On the other hand, by Cauchy formula, one has: $$\left |a_n \right |\leq 
\min_{m\in{\mathbf Z}} 
\left(\max_{\left |z \right |=\mu \left |q \right |^m} \left |f(z)\right |(\mu ~ \left |q \right |^{m})^{-n}\right),$$ where $\mu > 0$ is an arbitrary parameter. If $f$ is an entire function with $q$-exponential growth of order (at most) $k$ at infinity, one has $\left |f(z) \right |\leq C~\bigl(e(z)\bigr)^k$ for all $z\in{\mathbf C}^*$. From relation $e(q^mz)=\left |q \right |^{m(m+1)/2}~\left |z\right |^m~e(z)$, one draws, for all integers $n \geq 0$: $$\left |a_n \right |\leq C~e^k(\mu)~\mu^{-n}~
\bigl(\mu^k~\left |q \right |^{-n+k/2}\bigr)^m~\left |q \right |^{km^2/2}.$$

Last, we note that the function $t\mapsto A^t \left |q \right |^{kt^2/2}$ reaches its minimum at $t = -\dfrac{\ln A}{k\ln \left |q \right |}$, with: $$\min_{t\in{\mathbf R}} A^t \left |q \right |^{kt^2/2} = e^{-\frac{\ln^2A}{2k\ln \left |q \right |}}.$$ From this, one deduces: $$\label{eqn:minqgevrey}
\min_{m\in{\mathbf Z}} A^m \left |q\right |^{km^2/2} \leq 
\left |q \right |^{\frac k{8}}~e^{-\frac{\ln^2A}{2k\ln \left |q \right |}}$$ for all $A > 0$. Therefore, if we set $A=\mu^k |q|^{-n+k/2}$, we get the wanted $q$-Gevrey estimates for $|a_n|$, which concludes the proof. ◻
:::
