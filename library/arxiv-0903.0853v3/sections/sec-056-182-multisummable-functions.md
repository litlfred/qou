---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-056-182-multisummable-functions
section_title: "Multisummable functions"
section_number: 18.2
pages: 96-99
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.8
latex_coverage_ratio: 0.967
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:multisummable label="subsection:multisummable"}

More generally, let $$\Lambda_1 < \Lambda_1 + \Lambda_2 < \cdots <
\Lambda_1 + \Lambda_2 + \cdots + \Lambda_m= \Lambda.$$ For $i$ from $1$ to $m+1$, put []{#not77 label="not77"} $$\begin{aligned}
\Lambda_{\ge i} &:= \sum\limits_{j\ge i}\Lambda_j \\
\text{and~}
\Lambda_{\le i} &:= \sum\limits_{j\le i}\Lambda_j.
\end{aligned}$$ Also, we will write $\Lambda_{\ge m+1} = \Lambda_{\le 0} = {\bf O}$, where ${\bf O}$ stands for the null divisor, and $\Lambda_{\ge 0} = \Lambda_{\le m} = \Lambda$. For short, we shall call $(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)$ an *ordered partition of $\Lambda$*.

::: theo
[]{#theo:mniveaux label="theo:mniveaux"} Let $(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)$ be an ordered partition of $\Lambda$ and define ${\mathbb E}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda}$ as []{#not78 label="not78"} the set of functions that are analytic in a punctured neighborhood of $0$, have $q$-Gevrey order $|\Lambda|$ at $0$ and, for $i$ from $1$ to $m$, having $q$-Gevrey order $|\Lambda_{\ge i+1}|$ over $\Lambda_{\ge i}/\Lambda_{\ge i+1}$ at $0$. Then, one has: $${\mathbb E}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda} =
{\mathbb E}_0^{\Lambda_m} + \theta_{\Lambda_{\ge m}} {\mathbb E}_0^{\Lambda_{m-1}} +
\cdots + \theta_{\Lambda_{\ge 2}}{\mathbb E}_0^{\Lambda_1}.$$ In other words, writing ${\mathbb O}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda} := 
\left(\dfrac{1}{\theta_\Lambda}{\mathbb E}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda}\right)
\cap {\mathbb B}^{\Lambda}$, one has: $${\mathbb O}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda} =
{\mathbb A}_{q}^{\Lambda_1} + \dfrac{1}{\theta_{\Lambda_{\le 1}}} {\mathbb A}_{q}^{\Lambda_2} + \cdots +
\dfrac{1}{\theta_{\Lambda_{\le m-1}}}{\mathbb A}_{q}^{\Lambda_m} \cdot$$
:::

::: proof
*Proof.* One proceeds by induction on the length $m$ of the partition of divisor $\Lambda$: the cass $m = 1$ is theorem [\[theo:fF\]](#theo:fF){reference-type="ref" reference="theo:fF"} while the case $m = 2$ is dealt with in proposition [\[prop:deuxniveaux\]](#prop:deuxniveaux){reference-type="ref" reference="prop:deuxniveaux"}. The other cases follow directly from the next lemma. ◻
:::

::: lemm
[]{#lemm:m-1 label="lemm:m-1"} Let $m \ge 2$. Then: $${\mathbb E}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda} =
{\mathbb E}_0^{\Lambda_m} + 
\theta_{\Lambda_{m}} 
{\mathbb E}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_{m-1})}^{\Lambda_{\leq m-1}}~.$$
:::

::: proof
*Proof.* Let $F\in {\mathbb E}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda}$. As in equation [\[eqn:FTaylor\]](#eqn:FTaylor){reference-type="eqref" reference="eqn:FTaylor"} in the course of the proof of proposition [\[prop:deuxniveaux\]](#prop:deuxniveaux){reference-type="ref" reference="prop:deuxniveaux"}, one considers the Taylor expansion of $F$ along the divisor $\Lambda_m$, thereby finding that $F \in {\mathbb E}_0^{\Lambda_m} +
\theta_{\Lambda_{m}} 
{\mathbb E}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_{m-1})}^{\Lambda_{\leq m-1}}$. ◻
:::

::: defi
[]{#defi:msommabilite label="defi:msommabilite"} We call ${\mathbb O}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda}$ the set of *multisummable functions at $0$ with respect to partition $(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)$ of divisor $\Lambda$*.
:::

[]{#not79 label="not79"} By convention, we will set ${\mathbb O}_{(\bf O)}^{\bf O} := {\mathbf C}\{z\}$, the ring of all germs of analytic functions at $z=0$.

::: prop
[]{#prop:OOmodule label="prop:OOmodule"} The sets ${\mathbb E}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda}$ and ${\mathbb O}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda}$ have a structure of module over ${{\mathbf C}\{z\}}$ and are stable under the $q$-difference operator $\sigma_q$.
:::

::: proof
*Proof.* Immediate. ◻
:::

If $m \ge 2$, an element $f \in {\mathbb O}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda}$ generally has no asymptotic expansion in the sense of definition [\[defi:ALambda\]](#defi:ALambda){reference-type="ref" reference="defi:ALambda"}. Nonetheless, according to theorem [\[theo:mniveaux\]](#theo:mniveaux){reference-type="ref" reference="theo:mniveaux"}, there exists a $f_1 \in {\mathbb A}_q^{\Lambda_1}$ such that $f(z)-f_1(z) = O\left(\dfrac{1}{\theta_{\Lambda_1}(z)}\right)$ as $z \to 0$ outside of $\Lambda$, which allows one to prove the following.

::: theo
[]{#theo:masymptotique label="theo:masymptotique"} To each $f \in {\mathbb O}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda}$ there corresponds a unique power series $\hat f = \sum\limits_{n\ge 0}a_n~z^n\in{{\mathbf C}[[z]]}_{q;1/|\Lambda_1|}$ satisfying the following property: for all $R > 0$ near enough $0$, there are constants $C$, $A > 0$ such that, for all $\epsilon > 0$ and all $z\in S(\Lambda,\epsilon;R)$: $$\label{eqn:masymptotique}
\left |f(z) - \sum_{\ell=0}^{n-1}a_\ell~ z^\ell \right |<
\dfrac{C}{\epsilon}~A^n~\left |q \right |^{n^2/(2|\Lambda_1|)}~\left |z \right |^n~.$$
:::

::: proof
*Proof.* Applying theorem [\[theo:mniveaux\]](#theo:mniveaux){reference-type="ref" reference="theo:mniveaux"} to the function $f$, one gets: $$f = f_1 +\dfrac{f_2}{\theta_{\Lambda_1}} + \cdots +
\dfrac{f_m}{\theta_{\Lambda_{\le m-1}}},$$ where $f_i \in {\mathbb A}_q^{\Lambda_i}$ for all indexes $i$ from $1$ to $m$. Choose $R > 0$ in such a way that the $f_i~\theta_{\Lambda_i}$ have an analytic continuation to the punctured disk $0 < \left |z \right |< 2 R$; from the definition of each space ${\mathbb A}_q^{\Lambda_i}$, one has: $$d_q(z,\Lambda_i) > \epsilon \Longrightarrow
\left |f_i(z) \right |< \dfrac{C_i}{\epsilon}$$ for all $z$ such that $0 < \left |z \right |< R$, where $C_i$ is some positive constant. On the other hand, from lemma [\[lemm:thetamin0\]](#lemm:thetamin0){reference-type="ref" reference="lemm:thetamin0"} and relation [\[eqn:e-1\]](#eqn:e-1){reference-type="eqref" reference="eqn:e-1"}, one has, for any divisor $\Lambda' = \Lambda_1,\ldots,\Lambda_{\le m-1}$: $$d_q(z,\Lambda') > \epsilon \Longrightarrow
\left |\dfrac{1}{\theta_{\Lambda'}(z)} \right |<
\dfrac {C'}{\epsilon}~{A'}^n~\left |q \right |^{n^2/(2|\Lambda'|)}~\left |z \right |^n$$ for all integers $n \ge 0$, where $C'$ and $A'$ are positive constants depending only on the divisor $\Lambda'$. Noting that $d_q(z,\Lambda) \le d_q(z,\Lambda_i)~d_q(z,\Lambda_{\le i-1})$ for $i=2,\ldots,m$, one gets that, for all integers $n \ge 0$: $$\label{eqn:ff1}
d_q(z,\Lambda > \epsilon \Longrightarrow
\left |f(z)-f_1(z) \right |<
\dfrac {C_1}{\epsilon}~{A_1}^n~\left |q \right |^{n^2/(2|\Lambda_1|)}~\left |z \right |^n$$ as long as $0 < \left |z \right |< R$.

Relation [\[eqn:ff1\]](#eqn:ff1){reference-type="eqref" reference="eqn:ff1"} implies that both $f$ and $f_1$ have $\hat f$ as an asymptotic expansion in the classical sense (Poincaré) at $0$, outside of divisor $\Lambda$. Since $f_1$ is asymptotic to $\hat f$ in the frame of space ${\mathbb A}_q^{\Lambda_1}$, one has $\hat f \in {{\mathbf C}[[z]]}_{q;1/|\Lambda_1|}$. The bounds [\[eqn:masymptotique\]](#eqn:masymptotique){reference-type="eqref" reference="eqn:masymptotique"} are directly obtained from [\[eqn:fN\]](#eqn:fN){reference-type="eqref" reference="eqn:fN"} and [\[eqn:ff1\]](#eqn:ff1){reference-type="eqref" reference="eqn:ff1"}, using the obvious relation $d_q(z,\Lambda) \le d_q(z,\Lambda_1)$. ◻
:::

It is clear that a function $f$ satisfying [\[eqn:masymptotique\]](#eqn:masymptotique){reference-type="eqref" reference="eqn:masymptotique"} does not necessarily belong to the space ${\mathbb O}_{(\Lambda_1,\Lambda_2,\ldots,\Lambda_m)}^{\Lambda}$. To simplify, we shall adopt the following definition.

::: defi
[]{#defi:Lambda1Lambda label="defi:Lambda1Lambda"} When $f$ and $\hat f$ satisfy condition [\[eqn:masymptotique\]](#eqn:masymptotique){reference-type="eqref" reference="eqn:masymptotique"}, we shall say that *$f$ admits $\hat f$ as an asymptotic expansion at $0$ along the divisors $(\Lambda_1,\Lambda)$.* If moreover $\hat f$ is the null series, we shall say that *$f$ is flat at $0$ along divisors $(\Lambda_1,\Lambda)$.*
:::

The following result is straightforward from definitions [\[defi:ALambda\]](#defi:ALambda){reference-type="ref" reference="defi:ALambda"} (page ) and [\[defi:Lambda1Lambda\]](#defi:Lambda1Lambda){reference-type="ref" reference="defi:Lambda1Lambda"}.

::: prop
[]{#prop:3Lambda label="prop:3Lambda"} Let $\Lambda_1$, $\Lambda'$ and $\Lambda$ be divisors such that $\Lambda_1 < \Lambda' < \Lambda$. If $f \in {\mathbb A}_q^{\Lambda'}$, then its expansion along $\Lambda'$ is also the expansion of $f$ along $(\Lambda_1,\Lambda)$.
:::

::: proof
*Proof.* Immediate. ◻
:::
