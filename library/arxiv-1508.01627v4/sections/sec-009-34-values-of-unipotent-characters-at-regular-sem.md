---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-009-34-values-of-unipotent-characters-at-regular-sem
section_title: "Values of unipotent characters at regular semisimple elements"
section_number: 3.4
pages: 7-9
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.969
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#subsec:MN label="subsec:MN"} We first recall the following result of Asai on the decomposition of Lusztig induction as given in [@FS86 (3.1), (3.2)]. We restate it in terms of the restriction functors ${\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}$ instead of the induction functors ${R_{\mathbf{L}}^{\mathbf{G}}}$ as in the cited reference. This is a summary of results from [@As1 2.8], [@As2 1.5] and [@As3 2.2.3]. Note that there is a sign missing in the formula [@FS86 (3.2)] in the case $D_n$ as can be seen by considering the trivial character.

::: thm
[]{#thm:Asai label="thm:Asai"} Let ${\mathbf{G}}$ be of type $B_n,C_n$ or $D_n$. Let $d\ge1$. Let ${\mathcal{S}}$ be a symbol of a unipotent character of $G={\mathbf{G}}^F$. If ${\mathcal{S}}$ is not degenerate, we write $\rho_{\mathcal{S}}$ for the corresponding character. If ${\mathcal{S}}$ is degenerate we write $\rho_{\mathcal{S}}$ for the sum of the two corresponding characters.

1.  Let ${\mathbf{L}}$ be the centraliser in ${\mathbf{G}}$ of an $F$-stable torus ${\mathbf{T}}_d$ of ${\mathbf{G}}$ with $|{\mathbf{T}}_d^F|=q^d-1$. Then $${\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}(\rho_{\mathcal{S}})=\sum_{h\text{ $d$-hook}}\eps_h\,\rho_{{\mathcal{S}}\setminus h}$$ where $h$ runs over the $d$-hooks of ${\mathcal{S}}$.

2.  Let ${\mathbf{L}}$ be the centraliser in ${\mathbf{G}}$ of an $F$-stable torus ${\mathbf{T}}_d$ of ${\mathbf{G}}$ with $|{\mathbf{T}}_d^F|=q^d+1$. Then $${\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}(\rho_{\mathcal{S}})=(-1)^\delta\sum_{c\text{ $d$-cohook}}
         \eps_c\,\rho_{{\mathcal{S}}\setminus c}$$ where $c$ runs over the $d$-cohooks of ${\mathcal{S}}$, and $\delta=0$ for types $B_n,C_n$, $\delta=1$ for type $D_n$.
:::

With this we can show a Murnaghan--Nakayama formula for values of unipotent characters at regular semisimple elements.

::: thm
[]{#thm:MN label="thm:MN"} Let ${\mathbf{G}}$ be of type $B_n,C_n$ or $D_n$. Let ${\mathcal{S}}$ be a symbol of a unipotent character of $G={\mathbf{G}}^F$. If ${\mathcal{S}}$ is not degenerate, we write $\rho_{\mathcal{S}}$ for the corresponding character. If ${\mathcal{S}}$ is degenerate we write $\rho_{\mathcal{S}}$ for the sum of the two corresponding characters. Let $s\in G$ be regular semisimple lying in an $F$-stable maximal torus ${\mathbf{T}}$ of ${\mathbf{G}}$ parameterised by $(\la,\mu)\vdash n$.

1.  If $\la$ has a part of length $d$ then $$\rho_{\mathcal{S}}(s)=\sum_{h\text{ $d$-hook}}\eps_h\,\rho_{{\mathcal{S}}\setminus h}(s)$$ where $h$ runs over the $d$-hooks of ${\mathcal{S}}$.

2.  If $\mu$ has a part of length $d$ then $$\rho_{\mathcal{S}}(s)=(-1)^\delta\sum_{c\text{ $d$-cohook}}
         \eps_c\,\rho_{{\mathcal{S}}\setminus c}(s)$$ where $c$ runs over the $d$-cohooks of ${\mathcal{S}}$, and $\delta=0$ for types $B_n,C_n$, $\delta=1$ for type $D_n$.

On the right hand side of these formulae the symbols and characters belong to a Levi subgroup of semisimple rank $n-d$ and $s$ lies in a maximal torus of that Levi subgroup corresponding to the pair of partitions $(\lambda \setminus d,\mu) \vdash (n-d)$ in case (a), respectively $(\lambda, \mu\setminus d) \vdash (n-d)$ in case (b).
:::

::: proof
*Proof.* First assume that $\la$ has a part of length $d$. Then the torus ${\mathbf{T}}$ has an $F$-stable subtorus ${\mathbf{T}}_d$ with $|{\mathbf{T}}_d^F|=q^d-1$, see Section [\[subsec:WeylBCD\]](#subsec:WeylBCD){reference-type="ref" reference="subsec:WeylBCD"}. We consider Lusztig restriction of $\rho=\rho_{\mathcal{S}}$ to the $F$-stable Levi subgroup ${\mathbf{L}}:=C_{\mathbf{G}}({\mathbf{T}}_d)\cong{\mathbf{H}}{\mathbf{T}}_d$, with ${\mathbf{H}}$ a group of the same type as ${\mathbf{G}}$ and of rank $n-d$. This is a $d$-split Levi subgroup containing ${\mathbf{T}}$, so $s$, and according to Asai's Theorem [\[thm:Asai\]](#thm:Asai){reference-type="ref" reference="thm:Asai"}(a), the constituents of ${\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}(\rho)$ are, up to the sign $\eps_h$ as given in the statement, precisely those unipotent characters of ${\mathbf{L}}^F$ whose parameterising symbol is obtained from ${\mathcal{S}}$ by removing a $d$-hook. Application of Proposition [\[prop:restr\]](#prop:restr){reference-type="ref" reference="prop:restr"} then gives the claim in (a).

If $\mu$ has a part of length $d$, then ${\mathbf{T}}$ has an $F$-stable subtorus ${\mathbf{T}}_d$ with $|{\mathbf{T}}_d^F|=q^d+1$, and we can argue precisely as before using Theorem [\[thm:Asai\]](#thm:Asai){reference-type="ref" reference="thm:Asai"}(b) for the decomposition of Lusztig restriction to ${\mathbf{L}}:=C_{\mathbf{G}}({\mathbf{T}}_d)\ge{\mathbf{T}}\ni s$. ◻
:::

Note that in the theorem $\rho_{{\mathcal{S}}\sm h}$, respectively $\rho_{{\mathcal{S}}\sm c}$, is a unipotent character of the classical group ${\mathbf{L}}^F$ of rank $n-d$ (of the same type as $G$, except that removing cohooks changes the value of the defect modulo 4, so in type $D_n$ interchanges the twisted and untwisted types), and that $s$ is a fortiori regular in ${\mathbf{L}}$. Thus, the above result gives a recursive algorithm to compute the character values on all regular semisimple elements.

In case of degenerate symbols we only get the values of the sum of two unipotent characters. These unipotent characters form one element Lusztig families and so their values on regular semisimple classes are the values of the corresponding degenerate irreducible characters of the Weyl group, see [@Lu84 (4.6.10)]. The two characters for a degenerate symbol have the same values on non-degenerate classes, but different values on the degenerate classes. See [@PfWeyl] for a definition of unique parameters for the degenerate characters and classes and a formula to compute the missing values on degenerate classes.

The following vanishing result is immediate from the above:

::: cor
[]{#cor:vanish label="cor:vanish"} Let ${\mathbf{G}}$, ${\mathcal{S}}$ and $\rho_{\mathcal{S}}$ be as in Theorem [\[thm:MN\]](#thm:MN){reference-type="ref" reference="thm:MN"}, and let $s\in G$ be a regular semisimple element lying in an $F$-stable maximal torus parameterised by $(\la,\mu)$. Then $\rho_{\mathcal{S}}(s)=0$ in any of the two following cases:

1.  $\la$ has a part of length $d$, but ${\mathcal{S}}$ does not have a $d$-hook; or

2.  $\mu$ has a part of length $d$, but ${\mathcal{S}}$ does not have a $d$-cohook.

Thus, if $\rho_{\mathcal{S}}(s) \neq 0$ and $(\la,\mu) =
 ((\la_1, \ldots, \la_r),(\mu_1,\ldots,\mu_s))$, then it is possible to remove $\la_i$-hooks for $1\leq i \leq r$ and $\mu_i$-cohooks for $1\leq i \leq s$ from ${\mathcal{S}}$ in any chosen order.
:::

We remark that we have computed many character values on semisimple classes for classical groups of rank $\leq 10$ by Deligne--Lusztig theory. These examples helped to find the statements given in the next section. And they also provided an independent check of the Murnaghan--Nakayama formula [\[thm:MN\]](#thm:MN){reference-type="ref" reference="thm:MN"}.
