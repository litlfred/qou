---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-046-151-divisors-and-sectors-on-the-elliptic-curve-m
section_title: "Divisors and sectors on the elliptic curve ${\mathbf{E}_{q}} = {\mathbf C}^*/q^{\mathbf Z}$"
section_number: 15.1
pages: 73-77
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.871
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:divisorsonEq label="subsection:divisorsonEq"}

The projection $p: {\mathbf C}^{*} \rightarrow {\mathbf{E}_{q}}$ and the discrete logarithmic $q$-spiral $[\lambda;q]$ were defined in the general notations, section [\[section:generalnotations\]](#section:generalnotations){reference-type="ref" reference="section:generalnotations"}. In this chapter, we shall usually shorten the latter notation into $[\lambda] := [\lambda;q]$. We call *divisor* a finite formal sum of weighted such $q$-spirals: []{#not57 label="not57"} $$\Lambda = \nu_1 [\lambda_1] + \cdots + \nu_m [\lambda_m], 
\text{~where~} \nu_i\in {\mathbf N}^* \text{~and~}
[\lambda_i] \neq [\lambda_j] \text{~if~} i \neq j.$$ This can be identified with the *effective* divisor $\sum \nu_{i} \left[\overline{\lambda_{i}}\right]$ on ${\mathbf{E}_{q}}$ and, to simplify notations, we shall also write $\sum \nu_i [\lambda_i]$ that divisor on ${\mathbf{E}_{q}}$. The *support* of $\Lambda$ is the union of the $q$-spirals $[\lambda_1],\ldots,[\lambda_m]$. We write: []{#not58 label="not58"} $$\left |\Lambda \right |:= \nu_1  + \cdots + \nu_m$$ the *degree* of $\Lambda$ (an integer) and: $$\Vert \Lambda \Vert := 
(-1)^{|\Lambda|}\lambda_1^{\nu_1} \cdots \lambda_m^{\nu_m} \pmod{q^{\mathbf Z}}$$ the *weight* of $\Lambda$, an element of ${\mathbf{E}_{q}}$. It is equal, in additive notation, to $\sum \nu_{i} p(- \lambda_{i})$ evaluated in ${\mathbf{E}_{q}}$.\
[]{#not59 label="not59"} For any two non zero complex numbers $z$ and $\lambda$, we put: $$d_q(z,[\lambda]) := \inf_{\xi \in [\lambda]} \left |1-\frac z\xi \right |.$$ This is a kind of "distance" from $z$ to the $q$-spiral $[\lambda]$: one has $d_q(z,[\lambda]) = 0$ if, and only if $z \in [\lambda]$.

::: lemm
[]{#lemm:a1 label="lemm:a1"} Let $\Vert q \Vert_1 := \inf\limits_{n\in{\mathbf Z}^*}|1-q^n|$ and $M_q := \frac{\Vert q\Vert_1}{2+\Vert q\Vert_1}$. Let $a \in {\mathbf C}$ be such that $\left |1-a \right |\leq M_q$. Then: $$d_q(a;[1]) = \left |1 - a \right |.$$
:::

::: proof
*Proof.* This follows at once from the inequalities: $$\left |1-aq^n \right |\geq 
\left |a \right |~ \left |1-q^{n} \right |- \left |1-a \right |\geq 
(1-M_q) \Vert q\Vert_1 - \left |1-a \right |\ \geq \left |1 - a  \right |.$$ ◻
:::

For $\rho > 0$, we put: []{#not60 label="not60"} $$\begin{aligned}
D([\lambda];\rho) &:= \{z\in{\mathbf C}^* ~ | ~d_q(z,[\lambda])\leq \rho\}, \\
D^c([\lambda];\rho) &:= {\mathbf C}^*\setminus D([\lambda];\rho),
\end{aligned}$$ so that $D([\lambda];1)={\mathbf C}^*$ and $D^c([\lambda];1) = \emptyset$. From lemma [\[lemm:a1\]](#lemm:a1){reference-type="ref" reference="lemm:a1"}, it follows that for any $\rho < M_q$: $$D([\lambda];\rho) = \bigcup_{n\in{\mathbf Z}} q^n D(\lambda;|\lambda|\rho),$$ where $D(\lambda;|\lambda|\rho)$ denotes the closed disk with center $\lambda$ and radius $|\lambda|\rho$.\
Let $\lambda,\mu\in{\mathbf C}^*$; since: $$\left |1 - \dfrac z\mu q^n \right |\geq 
\left |\dfrac{z}{\lambda} \right |~ \left |1-\dfrac{\lambda}{\mu} q^n \right |
- \left |1- \dfrac{z}{\lambda} \right |,$$ one gets: $$\label{eqn:lambdamuz}
d_q(z,[\mu]) \geq d_q(\lambda,[\mu]) - \rho \bigl(1+d_q(\lambda,[\mu])\bigr)$$ when $z\in D([\lambda];\rho)$ and $\rho < M_q$.

::: prop
[]{#prop:lambdamu label="prop:lambdamu"} Given two distinct $q$-spirals $[\lambda]$ and $[\mu]$, there exists a constant $N > 1$ such that, for all $\rho > 0$ near enough from $0$, if $d_q(z,[\lambda]) > \rho$ and $d_q(z,[\mu]) > \rho$, then: $$d_q(z,[\lambda]) \, d_q(z,[\mu]) > \dfrac\rho N \cdot$$
:::

::: proof
*Proof.* By contradiction, assume that, for all $N > 1$, there exists $\rho_N > 0$ and $z \in {\mathbf C}^*$ such that $d_q(z,[\lambda]) > \rho_N$ and $d_q(z,[\mu]) > \rho_N$ but $d_q(z,[\lambda]) \, d_q(z,[\mu]) \leq \dfrac{\rho_N}{N}$; this would entail: $$\rho_N < d_q(z,[\lambda]) < \dfrac{1}{N},$$ whence, after [\[eqn:lambdamuz\]](#eqn:lambdamuz){reference-type="eqref" reference="eqn:lambdamuz"}: $$d_q(z,[\mu])\geq d_q(\lambda,[\mu])-\bigl(1+d_q(\lambda,[\mu])\bigr)/N.$$ In other words, when $N\to \infty$, one would get: $$d_q(z,[\lambda]) \, d_q(z,[\mu]) \gtrsim d_q(\lambda,[\mu])~\rho_N$$ (*i.e.* there is an inequality up to an $o(1)$ term), contradicting the assumption $d_q(z,[\lambda])~d_q(z,[\mu]) < \frac{\rho_N} N$. ◻
:::

Let $\Lambda := \nu_1[\lambda_1] + \cdots + \nu_m[\lambda_m]$ be a divisor and let $\rho>0$. We put: []{#not61 label="not61"} $$\label{eqn:dzLambda}
d_q(z,\Lambda) := \prod_{1\le j\le m}\left(d_q(z,[\lambda_j])\right)^{\nu_j}$$ and $$D(\Lambda;\rho) := \{z\in{\mathbf C}^* ~ | ~d_q(z,\Lambda)\le \rho\}~,\quad
D^c(\Lambda;\rho) := {\mathbf C}^* \setminus D(\Lambda;\rho).$$

Proposition [\[prop:lambdamu\]](#prop:lambdamu){reference-type="ref" reference="prop:lambdamu"} implies that, if $\Lambda = [\lambda] + [\mu]$ with $[\lambda] \neq [\mu]$, one has: $$D^c([\lambda];\rho) \cap D^c([\mu];\rho)
\subset D^c\left(\Lambda;\dfrac{\rho}{N}\right)$$ as long as $\rho$ is near enough from $0$.

::: prop
[]{#prop:Lambdad label="prop:Lambdad"} Let $\Lambda := \nu_1[\lambda_1] + \cdots + \nu_m[\lambda_m]$ be a divisor such that $[\lambda_i] \neq [\lambda_j]$ for $i \neq j$. There exists a constant $N>1$ such that, for all $\rho>0$ near enough from $0$, one has: $$\label{eqn:Dc}
D^c(\Lambda;\rho) \subset
\bigcap_{1\le j\le m} D^c([\lambda_j];\rho^{1/\nu_j}) \subset 
D^c\left(\Lambda;\dfrac{\rho}{N}\right).$$
:::

::: proof
*Proof.* The first inclusion comes from the fact that, if $d_q(z,[\lambda_j]) \leq \epsilon^{1/\nu_j}$ for some index $j$, then $d_q(z,\Lambda) \leq \epsilon$, because $d_q(z,[\lambda])\leq 1$ for all $\lambda \in {\mathbf C}^*$.

To prove the second inclusion, we use [\[eqn:lambdamuz\]](#eqn:lambdamuz){reference-type="eqref" reference="eqn:lambdamuz"} in the same way as in the proof of proposition [\[prop:lambdamu\]](#prop:lambdamu){reference-type="ref" reference="prop:lambdamu"}; details are left to the reader. ◻
:::

Taking the complementaries in [\[eqn:Dc\]](#eqn:Dc){reference-type="eqref" reference="eqn:Dc"}, one gets: $$\label{eqn:D}
D\left(\Lambda;\frac\rho N\right) \subset
\bigcup_{1\le j\le m} D\left([\lambda_j];\rho^{1/\nu_j}\right) 
\subset D(\Lambda;\rho).$$ Modifying the definition [\[eqn:dzLambda\]](#eqn:dzLambda){reference-type="eqref" reference="eqn:dzLambda"} of $d_q(z,\Lambda)$ as follows: $$\label{not62}
\delta(z,\Lambda) := \min_{1\le j\le m}\{d_q(z,[\lambda_j])\}^{\nu_j},$$ one gets, for all small enough $\rho$: $$D_\delta(\Lambda;\rho) := \{z\in{\mathbf C}^*: \delta(z,\Lambda)\le\rho\} =
\bigcup_{1\le j\le m} D([\lambda_j];\rho^{1/\nu_j})$$ Relation [\[eqn:D\]](#eqn:D){reference-type="eqref" reference="eqn:D"} shows that the maps $z \mapsto d_q(z,\Lambda)$ and $z\mapsto \delta(z,\Lambda)$ define equivalent systems of small neighborhoods relative to the divisor $\Lambda$; precisely, for $\rho \to 0$: $$D\left(\Lambda; \dfrac{\rho}{N}\right) \subset 
D_\delta(\Lambda;\rho) \subset D(\Lambda;\rho).$$

::: defi
[]{#defi:secteur label="defi:secteur"} Let $\epsilon \geq 0$. We call *germ of sector within distance $\epsilon$ from divisor $\Lambda$* any set: $$\label{not63}
S(\Lambda,\epsilon;R) =
\{z\in{\mathbf C}^*: d_q(z,\Lambda)>\epsilon, \left |z \right |< R\},
\text{~where~} R > 0.$$ When $R = +\infty$, we write $S(\Lambda,\epsilon)$ instead of $S(\Lambda,\epsilon;+\infty)$.
:::

Note that $S(\Lambda,0;R)$ is the punctured open disk $\{0 < \left |z \right |< R\}$ deprived of the $q$-spirals pertaining to divisor $\Lambda$. Since $d_q(z,\Lambda) \leq 1$ for all $z\in{\mathbf C}^*$, one has $S(\Lambda,1;R) = \emptyset$; that is why we shall assume that $\epsilon\in]0,1[$. Last, each sector within a short enough distance to $\Lambda$ represents, on the elliptic curve ${\mathbf{E}_{q}}= {\mathbf C}^*/q^{\mathbf Z}$, the curve ${\mathbf{E}_{q}}$ deprived of a family of ovals centered on the $\lambda_j$ with sizes varying like $\epsilon^{1/\nu_{j}}$.\
By a *(germ of) analytic function in $0$ out of $\Lambda$*, we shall mean any function defined and analytic in some germ of sector $S(\Lambda,0;R)$ with $R>0$. Such a function $f$ is said to be *bounded* (at $0$) if, for all $\epsilon >0$ and all $r \in ]0,R[$, one has: $$\sup_{z\in S(\Lambda,\epsilon;r)} |f(z)| < \infty.$$ []{#not64 label="not64"} We write ${\mathbb B}^{\Lambda}$ the set of such functions.

::: prop
[]{#prop:BB label="prop:BB"} If $f \in {\mathbb B}^\Lambda$, then for any $R > 0$ small enough and for all $a \in S(\Lambda,0;R)$ such that $\left |a \right |\notin 
\bigcup\limits_{n\in{\mathbf N}} \left |\lambda_i \right |\left |q^{-n} \right |$, there exists $K > 0$ such that $$\sup_{n\in{\mathbf N}} ~ \max_{\left |z \right |=|aq^{-n}|} \left |f(z) \right |< K.$$
:::

::: proof
*Proof.* From the assumption on $a$, it follows that: $$\epsilon := \frac{\max_{\tau\in[0,2\pi]}d_q(ae^{i\tau},\Lambda)}2 > 0,$$ whence all circles centered at $0$ and with respective radii $|a q^{-n}|$, $n \in {\mathbf N}$ are contained in the sector $S(\Lambda,\epsilon;R)$, which concludes the proof. ◻
:::
