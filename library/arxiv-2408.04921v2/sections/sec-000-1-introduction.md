---
doc_id: arxiv-2408.04921v2
doc_title: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2408.04921v2.pdf
source_sha256: dcfe112640a8adda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.986
doc_brief: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP — The paper studies how to compute irreducible characters of the generalized symmetric group Ck ≀Sn by iterative algorithms."
---
The character theory of the symmetric group $S_n$ plays an important role in representation theory [@JK]. It is well known that the irreducible characters $\chi^\lambda$ of $S_n$ are indexed by partitions $\lambda$ of $n$, and explicit character values are given by the celebrated Frobenius formula, which expresses the character values as the transition coefficients between the Schur symmetric functions and the power-sum symmetric functions [@JK; @Mac]. The character formula can also be formulated using a vertex algebraic method [@J1], where the irreducible character values of $S_n$ are expressed by matrix coefficients of Bernstein vertex operators [@Zel] and products of Heisenberg operators.

The theory of irreducible characters of the wreath product $G\wr S_n$, where $G$ is any finite group, was given by Specht [@S]. Under the Frobenius-type charactersitic, the irreducible characters $\chi^{\boldsymbol{\lambda}}$ of $G\wr S_n$ correspond to the wreath product Schur symmetric functions [@Sta] labelled by partitions $\boldsymbol{\lambda}$ colored by the irreducible characters of $G$. The character values are then given by the transition coefficients between the wreath product Schur symmetric functions and power-sum symmetric functions of partitions colored by the conjugacy classes of $G$.

Zelevinsky also studied the representations of $G\wr S_n$ using the language of PSH-algebras [@Zel]. The Grothendieck group of the category of finite-dimensional complex representations possesses an additional structure of Hopf algebra obeying positivity and self-adjointness axioms.

In [@FJW; @IJS] Frenkel, Wang and the second named author reformulated the Specht character theory using the vertex algebraic method in the context of the McKay correspondence. The character values are given by matrix coefficients of vertex operators of the form $$\langle \prod p_{\rho_i}(c), \prod X_{\gamma}(\lambda_i)\rangle,$$ where $X_{\gamma}(\lambda_i)$ are the components of some vertex operators indexed by irreducible character $\lambda_i$ of $G$ and $p_{\rho_i}(c)$ are power-sum symmetric functions colored by the conjugacy classes of $G$.

It is generally believed that the character theory of *the generalized symmetric group* $C_p\wr S_n$, the wreath product of the cyclic group $C_p$ and $S_n$, is closely related to the modular character theory of the symmetric group $S_{n}$ over characteristic $p$ (cf. [@KOR]). All Weyl groups of classical type are essentially generalized symmetric groups. If $k=1$, the generalized symmetric group reduces to $S_n$; if $k=2$, it is specially called the hyperoctahedral group, which is isomorphic to the Weyl group in type $B$. A character identity relating irreducible character values of the hyperocta-hedral group $C_2\wr S_n$ and those of the symmetric group $S_{2n}$ was recently found [@LP; @AR]. It is natural to study how to effectively compute character values of the generalized symmetric group $C_k\wr S_n$. Pfeiffer has given programs to compute the character tables of the Weyl groups in GAP [@P].

The classical Murnaghan-Nakayama rule is a combinatorial rule for computing the irreducible character $\chi^\lambda$ on conjugacy class $\rho$ of the symmetric group $S_n$ [@Mur; @Nak]. Recall that a *partition* $\lambda$ of $n$ is a decreasing sequence of positive integers $\lambda_i$ whose total sum is $n$, denoted by $\lambda \vdash n$. The number of $\lambda_i$ is the length of $\lambda$, denoted by $l(\lambda)$. If the parts $\lambda_i$ are not ordered, then we call $\lambda$ a *composition* of $n$.

There are several generalizations of the classical Murnaghan-Nakayama rule. Osima [@O] had given a Murnaghan-Nakayama rule in terms of skew representations of the generalized symmetric groups, and Stembridge [@St] rediscovered the rule and studied associated combinatorial formulas. This version of the Murnaghan-Nakayama rule requires information of restricting an irreducible representation of $C_k\wr S_n$ to $C_k\wr S_{n-m}$, so it needs extra work for computer programming. Finally Ariki and Koike [@AK] found the Murnaghan-Nakayama rule for the generalized symmetric group that naturally generalizes the classical one and independent of a priori information of the restriction functor. There are also generalizations of the Murnaghan-Nakayama rule for other related structures [@MRW; @BSZ; @EPW; @HR; @JL].

In this paper, we study the Murnaghan-Nakayama rule for the generalized symmetric groups $C_k\wr S_n$ aiming to compute the characters effectively. We first reformulate the Ariki-Koike version of the Murnaghan-Nakayama rule using the vertex algebraic method. Our treatment relies upon the vertex operator realization of Schur functions [@J2; @J3] to derive the iterative formula for the irreducible characters, which is perhaps a quicker derivation of the rule. Another benefit of the vertex algebraic method is that it also gives a *new iterative rule* or the dual rule for the generalized symmetric group by reducing the partition of the irreducible representation by rows.

Our reformulation of the Murnaghan-Nakayama rule is the following result, which is obtained by splitting the operators corresponding to conjugacy classes. This version gives an iterative formula to compute the irreducible characters that may simplify computational complexity.

::: thm
Given colored partitions $\boldsymbol{\lambda}=(\lambda^{(0)},\lambda^{(1)},\cdots,\lambda^{(k-1)})$ and $\boldsymbol{\rho}=(\rho^{(0)},\rho^{(1)},\cdots,\rho^{(k-1)})$ of $n$, where $\rho^{(s)}=(\rho^{(s)}_1,\cdots,\rho^{(s)}_m,\cdots,\rho^{(s)}_{l(s)})$. Then the value of the irreducible character $\chi^{\boldsymbol{\lambda}}$ of $C_k\wr S_n$ at the class $\boldsymbol{\rho}$ is given by $$\begin{aligned}
        \chi^{\boldsymbol{\lambda}}_{\boldsymbol{\rho}}=\sum_{j=0}^{k-1}\sum_{\boldsymbol{\xi_j}}(-1)^{\mathrm{ht}(\boldsymbol{\lambda_j})}\omega^{-sj}\chi^{\boldsymbol{\lambda}\backslash\boldsymbol{\xi_j}}_{\boldsymbol{\rho}\setminus\rho^{(s)}_m},
    
\end{aligned}$$ where ${\boldsymbol{\xi_j}}$ runs through all colored $\rho^{(s)}_m$-rim hooks contained in ${\boldsymbol{\lambda}}$ that are supported at the j-th constituent.
:::

Moreover, we can also break down the irreducible characters into lower rank ones using a dual procedure, which leads to a new iterative rule for the generalized symmetric group. Our rule at $k=1$ seems to be a new combinatorial formula for the irreducible character values of the symmetric group $S_n$ as well.

::: thm
(New iterative rule) Given colored partitions $\boldsymbol{\lambda}=(\lambda^{(0)},\lambda^{(1)},\\
 \cdots,\lambda^{(k-1)})$ and $\boldsymbol{\rho}=(\rho^{(0)},\rho^{(1)},\cdots,\rho^{(k-1)})$ of $n$. For any fixed color $j$, the irreducible character value of $C_k\wr S_n$ is given by $$\begin{aligned}
        \chi^{\boldsymbol{\lambda}}_{\boldsymbol{\rho}}=\sum_{\substack{\boldsymbol{\mu}\vartriangleleft\boldsymbol{\rho},\|\boldsymbol{\mu}\|\geq\lambda^{(j)}_1\\\boldsymbol{\tau}\vdash \|\boldsymbol{\mu}\|-\lambda^{(j)}_1}}\omega^{(\eta(\boldsymbol{\tau})-\eta(\boldsymbol{\mu}))j}\frac{{(-1)}^{l(\boldsymbol{\tau})}}{k^{l(\boldsymbol{\tau})}z_{\tau}}\chi^{\boldsymbol{\lambda}\setminus \lambda^{(j)}_1}_{(\boldsymbol{\rho}\backslash\boldsymbol{\mu})\cup\boldsymbol{\tau}}
    
\end{aligned}$$ summed over colored partitions $\boldsymbol{\mu}$ and $\boldsymbol{\tau}$ such that $\boldsymbol{\mu}\vartriangleleft\boldsymbol{\rho}$ with weight bigger than $\lambda^{(j)}_1$ and $\boldsymbol{\tau}$ of weight $\|\boldsymbol{\mu}\|-\lambda^{(j)}_1$. Here $z_{\tau}$ is defined below [\[e:innerprod\]](#e:innerprod){reference-type="eqref" reference="e:innerprod"}, $\tau$ is the rearrangement of $\boldsymbol{\tau}$, and $\eta(\boldsymbol{\tau})$, $\eta(\boldsymbol{\mu})$ are the weighted lengths $\sum_iil(\tau^{(i)})$, $\sum_i il(\mu^{(i)})$ respectively.
:::

We point it out that the dual Murnaghan-Nakayama rule for the generalized symmetric group gives a different iteration procedure. The former one given by Ariki and Koike simplifies the indexing colored-partition by removing all rim-hooks in each constituent, while our new rule simply removes the largest part in a fixed constituent. This reveals a different relation between representations of the generalized symmetric groups.

We also show how to use the Sagemath program [@Zim] to implement the algorithm. In theory, any irreducible character value of the generalized symmetric group can be iterated once according to our program pending on computer's CPU. The source code for this program can be found in the appendix. As applications, we also find a numerical relation between the irreducible character values of $C_k \wr S_n$ and those of modular $S_{kn}$ mod $k$.

The paper is organized into three parts. In section 2, we recall the basic notions about generalized symmetric groups $C_k\wr S_n$ and the construction of the irreducible character value [@FJW]. In section 3, we derive the analog of the Murnaghan-Nakayama rule and another iterative formula for the generalized symmetric groups, using the technique of vertex operators. The dual Maunaghan-Nakayama rule for the symmetric group is also obtained as a consequence. In section 4, we discuss some examples and properties of irreducible character values based on our main results. In the end, we formulate a numerical relation between the irreducible character values of $C_k\wr S_n$ and those of modular $S_{kn}$. The character tables of $C_3\wr S_1$, $C_3\wr S_2$, $C_3\wr S_3$ are attached in the end.
