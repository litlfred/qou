---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR"
section_id: sec-002-21-irreducible-representations-of-w-and-h
section_title: "Irreducible representations of W and H"
section_number: 2.1
pages: 2-4
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.948
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl group W, deﬁned over a ground ring in which “bad” primes for W are invertible."
---
[]{#sub21 label="sub21"}

It is known that ${\mathbb{Q}}$ is a splitting field for $W$; see, for example, [@GePf 6.3.8]. We will write $${\operatorname{Irr}}(W)=\{E^\lambda \mid \lambda \in \Lambda\}, \qquad  d_\lambda= 
\dim E^\lambda,$$ for the set of irreducible representations of $W$ (up to equivalence), where $\Lambda$ is some finite indexing set.

Now let $K$ be the field of fractions of $A$. By extension of scalars, we obtain a $K$-algebra ${\mathcal{H}}_K=K\otimes_A {\mathcal{H}}$. This algebra is known to be split semisimple; see [@GePf 9.3.5]. (Note the form of the quadratic relations for $T_s$, $s \in S$.) Furthermore, by Tits' Deformation Theorem, the irreducible representations of ${\mathcal{H}}_K$ (up to isomorphism) are in bijection with the irreducible representations of $W$; see [@GePf 8.1.7]. Thus, we can write $${\operatorname{Irr}}({\mathcal{H}}_K)=\{E^\lambda_v \mid \lambda \in \Lambda\}.$$ The correspondence $E^\lambda \leftrightarrow E^\lambda_v$ is uniquely determined by the following condition: $$\mbox{trace}\bigl(w,E^\lambda\bigr)=\mbox{trace}\bigl(
T_w,E^\lambda_v\bigr)\Big|_{v=1} \qquad \mbox{for all $w \in W$};$$ note that $\mbox{trace}\bigl(T_w,E^\lambda_v\bigr) \in A$ for all $w\in W$. See also [@Lusztig03 20.2, 20.3] for a discussion of the above correspondence, but note that this relies on the validity of Lusztig's conjectures (see §[\[sub24\]](#sub24){reference-type="ref" reference="sub24"} below).

## The integers ${\mathbf{a}}_\lambda$ and $f_\lambda$ {#sub22}

The algebra ${\mathcal{H}}$ is *symmetric*, where $\{T_w \mid w \in W\}$ and $\{T_{w^{-1}}\mid w \in W\}$ form a pair of dual bases. Hence we have the following orthogonality relations for the irreducible representations of ${\mathcal{H}}_K$: $$\sum_{w \in W} \mbox{trace}\bigl(T_w,E^\lambda_v\bigr)
\,\mbox{trace}\bigl(T_{w^{-1}},E_v^\mu\bigr)=\left\{\begin{array}{cl}
d_\lambda\,{\mathbf{c}}_\lambda & \quad \mbox{if $\lambda=\mu$},\\ 0 & \quad 
\mbox{if $\lambda \neq\mu$};\end{array}\right.$$ see [@GePf 8.1.7]. Here, $0 \neq {\mathbf{c}}_\lambda \in {{\mathbb{Z}}}[v,v^{-1}]$ and, following Lusztig, we can write $${\mathbf{c}}_\lambda=f_\lambda\, v^{-2{\mathbf{a}}_\lambda}+\mbox{combination of strictly
higher powers of $v$},$$ where ${\mathbf{a}}_\lambda,f_\lambda$ are integers such that ${\mathbf{a}}_\lambda\geqslant 0$ and $f_\lambda>0$; see [@GePf 9.4.7]. Thus, using ${\mathcal{H}}$, we have associated with each $E^\lambda \in {\operatorname{Irr}}(W)$ two integers ${\mathbf{a}}_\lambda$ and $f_\lambda$. These integers are explicitly known for all types of $W$; see Lusztig [@Lusztig03 Chap. 22].

Now let $p$ be a prime number. We say that $p$ is $L$-*bad* for $W$ if $p$ divides $f_\lambda$ for some $\lambda \in \Lambda$. Otherwise, $p$ is called $L$-*good*. If $L$ is a positive multiple of the length function, this corresponds to the familiar definition of "bad" primes; see Lusztig [@Lu4 Chap. 4]. Recall that, in this case, the conditions for being good the various irreducible types of $W$ are as follows:

::: center
$\begin{array}{rl} A_n: & \mbox{no condition}, \\
B_n, C_n, D_n: & p \neq 2, \\
G_2, F_4, E_6, E_7: &  p \neq 2,3, \\
E_8: & p \neq 2,3,5.  \end{array}$
:::

See [@mylaus Example 4.7] and [@GeJa Def. 2.3] for a description of the $L$-bad primes when $L$ is not constant on $S$.
