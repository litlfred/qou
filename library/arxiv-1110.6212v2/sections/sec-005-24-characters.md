---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem f or affine Hecke algebras James Parkinson ∗"
section_id: sec-005-24-characters
section_title: "Characters"
section_number: 2.4
pages: 14-16
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
doc_brief: "On calibrated representations and the Plancherel Theorem f or affine Hecke algebras James Parkinson ∗ — This paper has two main purposes."
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.937
---
[]{#sect:characters label="sect:characters"}

We conclude this section with some observations about characters that will be used for the Plancherel Theorems. Let $f_t(h)$ be as in ([\[eq:f\]](#eq:f){reference-type="ref" reference="eq:f"}).

::: lemma
[]{#lem:milage label="lem:milage"} Let $\pi$ be an irreducible representation of $\mathscr{H}_L$ with central character $t$, and suppose that the character $\chi$ of $\pi$ satisfies $$\chi(\tau_wx^{\lambda})=\delta_{w,1}\sum_{v\in W_0}k_v(vt)^{\lambda}\qquad\textrm{for all $w\in W_0$ and $\lambda\in L$},$$ for some numbers $k_v\in\mathbb{C}$. Then, with $f_t$ as in ([\[eq:f\]](#eq:f){reference-type="ref" reference="eq:f"}), if $t$ is regular we have $$\chi(h)=\sum_{v\in W_0}k_vf_{vt}(h)\qquad\textrm{for all $h\in\mathscr{H}_L$}.$$
:::

::: proof
*Proof.* Since $t$ is regular each $f_{vt}(h)$ with $v\in W_0$ and $h\in\mathscr{H}_L$ is defined. From Remark [\[rem:explicit\]](#rem:explicit){reference-type="ref" reference="rem:explicit"} and the hypothesis we have $\chi(h)=\sum_{v\in W_0}k_vf_{vt}(h)$ for all $h\in\mathscr{H}_L'$, where $\mathscr{H}_L'$ is the subalgebra of $\mathscr{H}_L$ with basis $\{\tau_w x^{\lambda}\mid w\in W_0,\lambda\in L\}$. Let $\Delta(x)=\prod_{\alpha\in R_0}(1-x^{-\alpha^{\vee}})=d(x)d(x^{-1})$. An induction using the formula $(1-x^{-\alpha_i^{\vee}})T_i=\tau_i+a_i(x)$ shows that $\Delta(x)^{\ell(w)}T_w\in\mathscr{H}_L'$ for all $w\in W_0$. Thus $\Delta(x)^{\ell(w)}T_wx^{\lambda}\in\mathscr{H}_L'$ for all $w\in W_0$ and $\lambda\in L$. Since $\Delta(x)\in\mathbb{C}[L]^{W_0}$ is central and $\chi$ is irreducible we have $$\Delta(t)^{\ell(w)}\chi(T_w x^{\lambda})=\chi(\Delta(x)^{\ell(w)}T_wx^{\lambda})=\sum_{v\in W_0}k_vf_{vt}(\Delta(x)^{\ell(w)}T_wx^{\lambda})=\Delta(t)^{\ell(w)}\sum_{v\in W_0}k_vf_{vt}(T_wx^{\lambda}).$$ We can divide through by $\Delta(t)^{\ell(w)}$ since $t$ is regular. ◻
:::

::: prop
[]{#prop:prelim_main label="prop:prelim_main"} Let $\chi_t$ be the character of the principal series representation $M(t)$ of $\mathscr{H}_L$ with central character $t$. Then $$\begin{aligned}
\label{eq:rg}
\chi_t(h)=\sum_{w\in W_0}f_{wt}(h)\qquad\textrm{for all $h\in\mathscr{H}_L$}
\end{aligned}$$ where the right hand side has an analytic continuation (for fixed $h\in\mathscr{H}_L$) to all $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$.
:::

::: proof
*Proof.* Suppose first that $D(t)=\emptyset$ and that $M(t)$ is irreducible (see Theorem [\[thm:kato\]](#thm:kato){reference-type="ref" reference="thm:kato"}). Since $D(t)=\emptyset$ the module $M(t)$ has basis $\{\tau_w\otimes v_t\mid w\in W_0\}$. To see this note that if $w=s_{i_1}\cdots s_{i_{\ell}}$ is reduced then the Bernstein relation gives $$\begin{aligned}
\tau_w\otimes v_t&=\bigg[\prod_{\alpha\in R(w^{-1})}(1-t^{\alpha^{\vee}})\bigg](T_w\otimes v_t)+\textrm{lower terms},
\end{aligned}$$ where 'lower terms' is a linear combination of terms $T_v\otimes v_t$ with $v<w$ in Bruhat order. Thus if $D(t)=\emptyset$ then each basis element $T_w\otimes v_t$ of $M(t)$ can be written in terms of the elements $\{\tau_{w}\otimes v_t\mid w\in W_0\}$.

From ([\[eq:tausquared\]](#eq:tausquared){reference-type="ref" reference="eq:tausquared"}) we see that the diagonal entries of the matrix for $\tau_w$ are all $0$. The matrix for $x^{\lambda}$ is diagonal with entries $(wt)^{\lambda}$ ($w\in W_0$) on the diagonal. Therefore $$\chi_t(\tau_w x^{\lambda})=\delta_{w,1}\sum_{v\in W_0}(vt)^{\lambda}\qquad\textrm{for all $w\in W_0$ and $\lambda\in L$}.$$ Hence Lemma [\[lem:milage\]](#lem:milage){reference-type="ref" reference="lem:milage"} gives ([\[eq:rg\]](#eq:rg){reference-type="ref" reference="eq:rg"}).

The cases where $D(t)\neq \emptyset$ or $M(t)$ is not irreducible are obtained as follows. For fixed $h\in\mathscr{H}$ the the character $\chi_t(h)$ is, by construction, a linear combination of $\{t^{\lambda}\mid \lambda\in L\}$ and is defined for all $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$. The right hand side of ([\[eq:rg\]](#eq:rg){reference-type="ref" reference="eq:rg"}) is a rational function in $t$. Thus the singularities of this rational function are removable singularities (even though each individual summand may have singularities). ◻
:::

::: prop
[]{#prop:calc label="prop:calc"} Suppose that $t$ is a regular character. Let $J\subseteq N(t)$, and let $M_J(t)$ be the module constructed in Theorem [\[thm:repmain\]](#thm:repmain){reference-type="ref" reference="thm:repmain"}. Then $$\chi(h)=\sum_{w\in F_J(t)}f_{wt}(h)\qquad\textrm{for all $h\in\mathscr{H}$}.$$
:::

::: proof
*Proof.* Since $\tau_i\cdot e_{wt}=q_i^{1/2}n_i(t)\,e_{s_iwt}$ we see that the diagonal entries of the matrix for $\tau_w$ are $0$. Since the matrix representing $x^{\lambda}$ is diagonal it follows that $$\chi(\tau_v x^{\lambda})=\delta_{v,1}\sum_{w\in F_J(t)}(wt)^{\lambda}\qquad\textrm{for all $v\in W_0$ and $\lambda\in L$},$$ and the result follows from Lemma [\[lem:milage\]](#lem:milage){reference-type="ref" reference="lem:milage"}. ◻
:::

::: lemma
[]{#lem:1dim label="lem:1dim"} Let $\pi$ be a $1$-dimensional representation of $\mathscr{H}_L$ with regular central character $t$. Then $$\chi(h)=f_t(h)\qquad\textrm{for all $h\in\mathscr{H}_L$},$$ unless $\mathscr{H}_L$ is of type $\tilde{C}_n$ with $\pi(x^{\alpha_n^{\vee}})=-1$. In this case there is a $1$-dimensional representation $\pi'$ defined by $\pi'(x^{\lambda})=\pi(x^{\lambda})$ for all $\lambda\in L$, $\pi'(T_i)=\pi(T_i)$ for all $i\neq n$, and $\pi'(T_n)=q_n^{1/2}$ (respectively $-q_n^{-1/2}$) if $\pi(T_n)=-q_n^{-1/2}$ (respectively $q_n^{1/2}$). Then $$\frac{\chi(h)+\chi'(h)}{2}=f_t(h)\qquad\textrm{for all $h\in\mathscr{H}_L$}.$$
:::

::: proof
*Proof.* By direct analysis of the defining relations ([\[eq:rel1\]](#eq:rel1){reference-type="ref" reference="eq:rel1"})-([\[eq:rel4\]](#eq:rel4){reference-type="ref" reference="eq:rel4"}) one sees that the central character $t$ of a $1$-dimensional representation necessarily has $n_i(t)n_i(t^{-1})=0$, except in the $\tilde{C}_n$ case with $\pi(x^{\alpha_n^{\vee}})=-1$. Excluding this case for the moment, it follows from ([\[eq:tausquared\]](#eq:tausquared){reference-type="ref" reference="eq:tausquared"}) that $\pi(\tau_i)=0$ and hence $\pi(\tau_wx^{\lambda})=\delta_{w,1}t^{\lambda}$ for all $w\in W_0$ and $\lambda\in L$. Since $t$ is assumed to be regular, Lemma [\[lem:milage\]](#lem:milage){reference-type="ref" reference="lem:milage"} gives $\chi(h)=f_t(h)$ for all $h\in\mathscr{H}_L$.

Now consider the $\tilde{C}_2$ case with $\pi(x^{\alpha_n^{\vee}})=-1$. Let $\pi'$ be the companion representation defined in the statement of the lemma. The proof of Lemma [\[lem:milage\]](#lem:milage){reference-type="ref" reference="lem:milage"} applied to the representation $\pi\oplus\pi'$ proves the result. The fact that $\pi\oplus\pi'$ is not irreducible does not effect the proof of Lemma [\[lem:milage\]](#lem:milage){reference-type="ref" reference="lem:milage"} because the centre $\mathbb{C}[L]^{W_0}$ of $\mathscr{H}_L$ acts by the same scalar on each of $\pi$ and $\pi'$. ◻
:::

::: remark
[]{#rem:regular label="rem:regular"} In Proposition [\[prop:calc\]](#prop:calc){reference-type="ref" reference="prop:calc"} and Lemma [\[lem:1dim\]](#lem:1dim){reference-type="ref" reference="lem:1dim"} we assumed that $t$ is a regular central character. In general these results are false for non-regular central characters, even if each term $f_t(h)$ is defined. For example consider the $\tilde{G}_2$ case with $t\in\mathrm{Hom}(Q,\mathbb{C}^{\times})$ given by $t^{\alpha_1^{\vee}}=q_1$, $t^{\alpha_2^{\vee}}=q_2^{-1}$. If $q_1\neq q_2$ and $q_1\neq q_2^2$ and $q_1^2\neq q_2^3$ and $q_1\neq q_2^3$ then this central character is regular, and by Lemma [\[lem:1dim\]](#lem:1dim){reference-type="ref" reference="lem:1dim"} we have $f_t(h)=\chi^4(h)$ for all $h\in\mathscr{H}$, where $\chi^4$ is the $1$-dimensional representation of $\mathscr{H}$ listed in Section [\[sect:G2\]](#sect:G2){reference-type="ref" reference="sect:G2"}. Suppose that $q_1=q_2=q$. A calculation similar to Remark [\[rem:explicit\]](#rem:explicit){reference-type="ref" reference="rem:explicit"} shows that $f_t(h)$ is defined for all $h\in\mathscr{H}$, and that $f_t(T_1T_2T_1)=q^{1/2}$. But $\chi^4(T_1T_2T_1)=-q^{1/2}$.
:::
