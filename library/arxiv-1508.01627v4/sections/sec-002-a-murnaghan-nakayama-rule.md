---
doc_id: arxiv-1508.01627v4
doc_title: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups"
section_id: sec-002-a-murnaghan-nakayama-rule
section_title: "A Murnaghan\u2013Nakayama rule"
section_number: 3
pages: 5-9
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.982
doc_brief: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups — 7 sections: Introduction; Maximal tori in classical groups; A Murnaghan–Nakayama rule"
---
[]{#sec:MNrule label="sec:MNrule"}

In this section we derive a Murnaghan--Nakayama type formula for the values of unipotent characters of classical groups of Lie type on regular semisimple elements. It relies on a result of Asai on the decomposition of Lusztig restriction.

## Lusztig restriction {#subsec:*RLG}

We consider the following setup: ${\mathbf{G}}$ is a connected reductive algebraic group over an algebraic closure of the finite field ${\mathbb{F}}_p$, and $F:{\mathbf{G}}\rightarrow{\mathbf{G}}$ is a Steinberg endomorphism of ${\mathbf{G}}$, with finite group of fixed points ${\mathbf{G}}^F$. For an $F$-stable Levi subgroup ${\mathbf{L}}\le{\mathbf{G}}$ of ${\mathbf{G}}$ Lusztig defined, via certain $\ell$-adic cohomology constructions, induction and restriction functors $${R_{\mathbf{L}}^{\mathbf{G}}}:{\mathbb{Z}}{\operatorname{Irr}}({\mathbf{L}}^F)\rightarrow{\mathbb{Z}}{\operatorname{Irr}}({\mathbf{G}}^F)\quad\text{ and }\quad
  {\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}:{\mathbb{Z}}{\operatorname{Irr}}({\mathbf{G}}^F)\rightarrow{\mathbb{Z}}{\operatorname{Irr}}({\mathbf{L}}^F)$$ between the respective groups of virtual characters. These are adjoint to one another with respect to the usual scalar product of characters. We need the following connection between Lusztig restriction and ordinary restriction on regular semisimple conjugacy classes:

::: prop
[]{#prop:restr label="prop:restr"} Let ${\mathbf{L}}\le{\mathbf{G}}$ be an $F$-stable Levi subgroup. Let $\chi\in{\operatorname{Irr}}({\mathbf{G}}^F)$ and $s\in {\mathbf{L}}^F$ be regular semisimple. Then ${\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}(\chi)(s)=\chi(s)$.
:::

::: proof
*Proof.* According to the character formula in [@DM Prop. 12.2(ii)] we have $${\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}(\chi)(s)=\frac{|C_{\mathbf{L}}^\circ(s)^F|}{|C_{\mathbf{G}}^\circ(s)^F|}
   \sum_{u\in C_{\mathbf{G}}^\circ(s)^F_u}Q_{C_{\mathbf{L}}^\circ(s)}^{C_{\mathbf{G}}^\circ(s)}(u,1)
   \,\chi(s),$$ where the sum runs over unipotent elements in $C_{\mathbf{G}}^\circ(s)^F$, and $Q_{C_{\mathbf{L}}^\circ(s)}^{C_{\mathbf{G}}^\circ(s)}$ is a certain 2-parameter Green function. Since $s$ is assumed to be regular semisimple, ${\mathbf{T}}:=C_{\mathbf{G}}^\circ(s)=C_{\mathbf{L}}^\circ(s)$ is a torus. Hence the only term in the sum is the one for $u=1$, and by [@DM p. 98] the Green function takes the value $$Q_{C_{\mathbf{L}}^\circ(s)}^{C_{\mathbf{G}}^\circ(s)}(1,1)=Q_{{\mathbf{T}}}^{{\mathbf{T}}}(1,1) =1$$ (again using that $C_{\mathbf{G}}^\circ(s)$ contains no non-trivial unipotent elements). The claim follows. ◻
:::

## Symbols {#subsec:symb}

We now specialise to simple groups of classical type. By Lusztig's results their unipotent characters are parameterised by so-called *symbols*. Here, a symbol is an unordered pair of finite sets of non-negative integers, usually denoted as $${\mathcal{S}}=\binom{X}{Y}=\begin{pmatrix} \la_1& \la_2& \ldots& \la_r\\
  \mu_1& \mu_2& \ldots& \mu_s\end{pmatrix}$$ with $\la_1<\la_2<\ldots<\la_r$ and $\mu_1<\mu_2<\ldots<\mu_s$ where $r,s\ge0$. Two symbols are said to be *equivalent* if one can be obtained from the other by a sequence of shift operations $${\mathcal{S}}\mapsto \begin{pmatrix} 0& \la_1+1& \la_2+1& \ldots& \la_r+1\\
  0& \mu_1+1& \mu_2+1& \ldots& \mu_s+1\end{pmatrix}$$ or by interchanging the rows $X$ and $Y$ of ${\mathcal{S}}$. The *rank* of ${\mathcal{S}}$ is by definition $${\operatorname{rk}}({\mathcal{S}})=\sum_{i=1}^r \la_i+\sum_{i=1}^s\mu_i
  -\Big\lfloor\left(\frac{r+s-1}{2}\right)^2\Big\rfloor.$$ The *defect* of ${\mathcal{S}}$ is ${\operatorname{def}}({\mathcal{S}}):=|r-s|$. Note that the rank and the defect are well-defined on equivalence classes. We will use the following notation to describe explicit symbols: $\underline{n} := \{0,1,\ldots,n\}$ and for a set $X$, a $k\in X$ and $l\notin X$ we write $X \sm k \cup l := X \sm\{k\} \cup \{l\}$.

Let $d$ be a positive integer. We say that ${\mathcal{S}}$ has a *$d$-hook* $h$ at $x\in X$ if $0\le x-d\notin X$, and similarly at $x\in Y$. Removing that $d$-hook leads to the symbol ${\mathcal{S}}\sm{h}:=\binom{X'}{Y}$ with $X'=X\sm x\cup(x-d)$ (respectively ${\mathcal{S}}\sm{h}:=\binom{X}{Y'}$ with $Y'=Y\sm x\cup(x-d)$). Attached to the hook $h$ is the sign $\eps_h:=(-1)^m$ where $m:=|\{y\in X\mid x-d<y<x\}|$ (respectively $m:=|\{y\in Y\mid x-d<y<x\}|$). We say that ${\mathcal{S}}$ has a *$d$-cohook* $c$ at $x\in X$ if $0\le x-d\notin Y$, and similarly at $x\in Y$. Removing that $d$-cohook leads to the symbol ${\mathcal{S}}\sm{c}:=\binom{X'}{Y'}$ with $X'=X\sm\{x\},Y'=Y\cup\{x-d\}$ (respectively $Y'=Y\sm\{x\},
X'=X\cup\{x-d\}$). Attached to the cohook $c$ is the sign $\eps_c:=(-1)^m$, where $m:=|\{y\in X\mid y<x\}|+|\{y\in Y\mid y<x-d\}|$ (respectively $m:=|\{y\in Y\mid y<x\}|+|\{y\in X\mid y<x-d\}|$), see [@FS86 §3] for example. Note that removing a $d$-hook or a $d$-cohook from a symbol of rank $n$ yields a symbol of rank $n-d$.

For a symbol ${\mathcal{S}}=(X,Y)$ with all entries of $X,Y$ not larger than $m$ we define the *dual symbol* ${\mathcal{S}}^\vee=(X',Y')$ where $$X'= \underline{m} \setminus \{m-x\mid x\in X\}\mbox{ and }
  Y'= \underline{m} \setminus \{m-y\mid y\in Y\}.$$

The hooks and cohooks of $S$ and $S^\vee$ are each in natural bijection such that removing hooks or cohooks commutes with the duality operation. This observation will allow us to simplify some of the later statements and proofs.

## Unipotent characters of symplectic and orthogonal groups {#subsec:uniBCD}

Now assume that ${\mathbf{G}}$ is simple of type $B_n$, $C_n$ or $D_n$, and $F$ does not induce the triality automorphism when ${\mathbf{G}}$ is of type $D_4$ nor the exceptional graph automorphism in type $B_2$ or $C_2$. According to Lusztig [@Lu84] the unipotent characters of $G:={\mathbf{G}}^F$ are then parameterised by (equivalence classes of) symbols of rank $n$. More precisely, if ${\mathbf{G}}$ is of type $B_n$ or $C_n$, the unipotent characters of $G$ are parameterised by symbols of rank $n$ and odd defect. Now assume that ${\mathbf{G}}$ is of type $D_n$. If the Steinberg endomorphism $F$ is untwisted, then the unipotent characters of $G$ are parameterised by symbols ${\mathcal{S}}$ of rank $n$ and defect ${\operatorname{def}}({\mathcal{S}})\equiv0\pmod4$, where symbols with two equal rows stand for two characters each. These are the so-called *degenerate* symbols. If ${\mathbf{G}}^F$ is of twisted type, then the unipotent characters of $G$ are parameterised by symbols ${\mathcal{S}}$ of rank $n$ and defect ${\operatorname{def}}({\mathcal{S}})\equiv2\pmod4$.

If ${\mathcal{S}}$ is a symbol parameterising a unipotent character $\rho$ of a classical group then the Alvis--Curtis dual $\rho^\vee$ of $\rho$ is parameterised by the dual symbol ${\mathcal{S}}^\vee$ which has the same rank, the same defect and the same hook and cohook lengths (see [@Lu84 4.5.5, 4.6.8]). (In fact, the degree $\rho^\vee(1)$ differs by a power of the underlying characteristic of ${\mathbf{G}}$ from the degree $\rho(1)$.)

## Values of unipotent characters at regular semisimple elements {#subsec:MN}

We first recall the following result of Asai on the decomposition of Lusztig induction as given in [@FS86 (3.1), (3.2)]. We restate it in terms of the restriction functors ${\,{}^*R_{\mathbf{L}}^{\mathbf{G}}}$ instead of the induction functors ${R_{\mathbf{L}}^{\mathbf{G}}}$ as in the cited reference. This is a summary of results from [@As1 2.8], [@As2 1.5] and [@As3 2.2.3]. Note that there is a sign missing in the formula [@FS86 (3.2)] in the case $D_n$ as can be seen by considering the trivial character.

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
