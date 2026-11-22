---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR"
section_id: sec-005-25-representations-of-j
section_title: "Representations of J"
section_number: 2.5
pages: 5-7
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.95
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl group W, deﬁned over a ground ring in which “bad” primes for W are invertible."
---
[]{#sub25 label="sub25"}

Until the end of this section, we will assume that $R={\mathbb{Q}}$. Upon substituting $v\mapsto 1 \in {\mathbb{Q}}$, the algebra ${\mathcal{H}}$ specialises to ${{\mathbb{Q}}}[W]$. Hence, we obtain a homomorphism of ${\mathbb{Q}}$-algebras $$\phi_1\colon {{\mathbb{Q}}}[W]  \rightarrow J_{{\mathbb{Q}}}, \qquad \mbox{where $J_{{\mathbb{Q}}}=
{{\mathbb{Q}}} \otimes_{{\mathbb{Z}}} J$}.$$ This is an isomorphism by the argument in [@Lusztig03 20.1]. Since ${{\mathbb{Q}}}[W]$ is split semisimple, we can conclude that $J_{{\mathbb{Q}}}$ also is split semisimple. Via the isomorphism $\phi_1 \colon {{\mathbb{Q}}}[W]\rightarrow 
J_{\mathbb{Q}}$, the set $\Lambda$ can be used to parametrize the irreducible representations of $J_{\mathbb{Q}}$ (up to isomorphism). As in [@Lusztig03 20.2], we write $${\operatorname{Irr}}(J_{{\mathbb{Q}}})=\{E_\spadesuit^\lambda \mid \lambda \in \Lambda\},$$ where $E_\spadesuit^\lambda$ coincides with $E^\lambda$ as ${\mathbb{Q}}$-vector space and the action of $j \in J_{\mathbb{Q}}$ on $E_\spadesuit^\lambda$ is the same as the action of $\phi_1^{-1}(j)$ on $E^\lambda$. Now, by [@Lusztig03 20.1(b)], the algebra $J$ is symmetric where $\{t_w \mid w \in W\}$ and $\{t_{w^{-1}} 
\mid w \in W\}$ form a pair of dual bases. Thus, we have the following orthogonality relations: $$\sum_{w \in W} \mbox{trace}\bigl(t_w,E_\spadesuit^\lambda\bigr)
\,\mbox{trace}\bigl(t_{w^{-1}},E_\spadesuit^\mu\bigr)= \left\{
\begin{array}{cl} d_\lambda\,f_\lambda & \quad \mbox{if $\lambda=\mu$},\\ 
0 & \quad \mbox{if $\lambda \neq\mu$}.\end{array}\right.$$ (The fact that $f_\lambda$ appears on the right hand side is shown in [@Lusztig03 20.11].) Choosing a vector space basis of $E^\lambda$, we obtain a matrix representation $$\rho^\lambda \colon J_{{\mathbb{Q}}} \rightarrow M_{d_\lambda}({\mathbb{Q}}), \qquad
t_w \mapsto \bigl(\rho_{{\mathfrak{s}}{\mathfrak{t}}}^\lambda(t_w)\bigr)_{{\mathfrak{s}},{\mathfrak{t}}\in M(\lambda)},$$ where $M(\lambda)=\{1,\ldots,d_\lambda\}$. Then the following *Schur relations* hold; see [@GePf §7.2]. For $\lambda, \mu \in 
\Lambda$, ${\mathfrak{s}},{\mathfrak{t}}\in M(\lambda)$ and ${\mathfrak{u}},{\mathfrak{v}}\in M(\mu)$, we have: $$\sum_{w \in W} \rho_{{\mathfrak{s}}{\mathfrak{t}}}^\lambda(t_{w})\,\rho^\mu_{{\mathfrak{u}}{\mathfrak{v}}}(
t_{w^{-1}})= \left\{\begin{array}{cl} f_\lambda & \quad \mbox{if 
$(\lambda,{\mathfrak{s}},{\mathfrak{t}})= (\mu,{\mathfrak{v}},{\mathfrak{u}})$},\\ 0 & \quad \mbox{otherwise}.
\end{array}\right.$$ These equations can be inverted and this yields the "second" Schur relations: $$\sum_{\lambda \in \Lambda} \sum_{{\mathfrak{s}},{\mathfrak{t}}\in M(\lambda)}
\frac{1}{f_\lambda}\rho_{{\mathfrak{s}}{\mathfrak{t}}}^\lambda(t_x)\,\rho_{{\mathfrak{t}}{\mathfrak{s}}}^\lambda(
t_{y^{-1}})= \left\{\begin{array}{cl} 1 & \quad \mbox{if $x=y$},\\ 0 & 
\quad \mbox{otherwise}.\end{array}\right.$$ By a general argument, every irreducible representation of $J_{\mathbb{Q}}$ leaves a positive-definite quadratic form invariant. More precisely, we have the following result.

::: proposition
[]{#lem1 label="lem1"} Let $\lambda \in \Lambda$. Then a basis of $E^\lambda$ can be chosen such that

-   $\rho^\lambda_{{\mathfrak{s}}{\mathfrak{t}}}(t_w) \in {\mathbb{Z}}$ for all $w\in W$ and ${\mathfrak{s}},{\mathfrak{t}}\in M(\lambda)$.

Furthermore, there exists a symmetric, positive-definite matrix $$B^\lambda=(\beta_{{\mathfrak{s}}{\mathfrak{t}}}^\lambda)_{{\mathfrak{s}},{\mathfrak{t}}\in M(\lambda)} \qquad 
\mbox{where} \qquad\beta_{{\mathfrak{s}}{\mathfrak{t}}}^\lambda\in {\mathbb{Z}}\mbox{ for all ${\mathfrak{s}},{\mathfrak{t}}
\in M_{d_\lambda}$},$$ such that the following two conditions hold:

-   $B^\lambda\cdot \rho^\lambda(t_{w^{-1}})=\rho^\lambda
    (t_w)^{\operatorname{tr}}\cdot B^\lambda$ for all $w \in W$;

-   Any prime which divides $\det(B^\lambda)\neq 0$ is $L$-bad for $W$.
:::

(For any matrix $M$, we denote by $M^{\text{tr}}$ the transpose of $M$.)

::: proof
*Proof.* To simplify the notation, write $E=E^\lambda$, $d=d_\lambda$ and $\rho=\rho^\lambda$ so that we can omit a subscript or superscript $\lambda$ in the subsequent formulas. Since $J$ is defined over ${\mathbb{Z}}$, the statement in (a) follows by a general argument; see, for example, [@GePf 7.3.7]. Now let $$B_1=\sum_{y\in W} \rho(t_y)^{\operatorname{tr}}\cdot\rho(t_y)\in 
M_d({\mathbb{Z}}).$$ This matrix clearly is symmetric. Now let $0\neq e=(e_1,\ldots,e_d)
\in {\mathbb{Z}}^d$. Since $\rho$ is irreducible, there exists some $y \in W$ such that $e\rho(t_y)^{\operatorname{tr}}\neq 0$ and, hence, the standard scalar product of this vector with itself will be strictly positive. Consequently, we have $eB_1e^{\operatorname{tr}}>0$. Thus, $B_1$ is positive-definite and, in particular, $\det(B_1)\neq 0$. For any $x\in W$, we have $$B_1\cdot \rho(t_{x^{-1}})=\sum_{y \in W} \rho(t_y)^{\operatorname{tr}}
\cdot \rho(t_yt_{x^{-1}})= \sum_{y,z\in W} \gamma_{y,x^{-1},z^{-1}}\,
\rho(t_y)^{\operatorname{tr}}\cdot\rho(t_z).$$ Now $\gamma_{y,x^{-1},z^{-1}}=\gamma_{x^{-1},z^{-1},y}$ by **(P7)** in [@Lusztig03 14.2], and $\gamma_{x^{-1},z^{-1},y}=\gamma_{z,x,y^{-1}}$ by [@Lusztig03 Prop. 13.9]. Hence, the right hand side of the above identity equals $$\sum_{y,z\in W} \gamma_{z,x,y^{-1}} \rho(t_y)^{\operatorname{tr}} 
\cdot \rho(t_z)=\sum_{z\in W} \rho(t_zt_x)^{\operatorname{tr}} 
\cdot \rho(t_z)= \rho(t_x)^{\operatorname{tr}}\cdot B_1.$$ Let $0 \neq n \in {\mathbb{Z}}$ be the greatest common divisor of all non-zero coefficients of $B_1$ and $B=n^{-1}B_1\in M_d({\mathbb{Z}})$. Then $B$ is a symmetric, positive-definite matrix such that (b) holds. It remains to prove (c). Let $p$ be a prime number and denote by $\bar{B}$ the matrix obtained by reducing all coefficents modulo $p$. By reduction modulo $p$, we also obtain an ${\mathbb{F}}_p$-algebra $J_p={\mathbb{F}}_p \otimes_{\mathbb{Z}}J$ and a corresponding matrix representation $\bar{\rho}\colon J_p \rightarrow 
M_{d}({\mathbb{F}}_p)$. Hence we have $$\bar{B}\neq 0 \qquad \mbox{and}\qquad \bar{B}\cdot\bar{\rho}(t_w)=
\bar{\rho}(t_{w^{-1}})^{\text{tr}}\cdot \bar{B}\quad\mbox{for all $w\in W$}.$$ By [@Lusztig03 13.9], the map $t_w\mapsto t_{w^{-1}}$ defines an involutory anti-automorphism of $J$. Hence the assignment $t_w \mapsto 
\bar{\rho}(t_{w^{-1}})^{\text{tr}}$ also defines a representation of $J_p$. The above identity now shows that $\bar{B}\neq 0$ is an "intertwining operator". Hence, if we knew that $\bar{\rho}$ was irreducible, then Schur's Lemma would imply that $\bar{B}$ were invertible and so $p$ could not divide $\det(B)$.

Thus, it remains to show that $\bar{\rho}$ is an irreducible representation of $J_p$ whenever $p$ is $L$-good. But this follows from a general argument about symmetric algebras. Indeed, as already noted in §[\[sub25\]](#sub25){reference-type="ref" reference="sub25"}, $J$ is symmetric and we have the Schur relations for the matrix coefficients of $\rho=\rho^\lambda$. Reducing these relations modulo $p$, we obtain: $$\sum_{w \in W} \bar{\rho}_{{\mathfrak{s}}{\mathfrak{t}}}^\lambda(t_w) \, 
\bar{\rho}^\lambda_{{\mathfrak{u}}{\mathfrak{v}}} (t_{w^{-1}})= \left\{\begin{array}{cl} 
f_\lambda\bmod p & \quad \mbox{if ${\mathfrak{s}}={\mathfrak{v}}$, ${\mathfrak{u}}={\mathfrak{t}}$},\\ 0 & \quad 
\mbox{otherwise}.\end{array}\right.$$ Since $f_\lambda \not \equiv 0 \bmod p$, one easily deduces from this that $\bar{\rho}^\lambda$ is (absolutely) irreducible; see [@GePf Remark 7.2.3]. ◻
:::
