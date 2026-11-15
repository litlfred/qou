---
doc_id: arxiv-math-0409393v1
doc_title: "ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR LINEAR q-DIFFERENCE EQUATIONS"
section_id: sec-002-3-algebraic-summation
section_title: "Algebraic summation"
section_number: 3
pages: 15-22
source_pdf: 0409393v1.pdf
source_sha256: 2107d961f6065539
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.976
doc_brief: "ALGEBRAIC CONSTRUCTION OF THE STOKES SHEAF FOR IRREGULAR LINEAR q-DIFFERENCE EQUATIONS — — The local analytic classiﬁcation of irregular linear q-diﬀerence equa- tions has recently been obtained by"
---
## The algorithm

We keep the notations $M_{0}$, $A_{0}$, $A_{U}$ of [\[equation:forme-canonique\]](#equation:forme-canonique){reference-type="ref" reference="equation:forme-canonique"} and [\[equation:forme-canonique-diagonale\]](#equation:forme-canonique-diagonale){reference-type="ref" reference="equation:forme-canonique-diagonale"} and the corresponding conventions from section [\[subsection:devissage\]](#subsection:devissage){reference-type="ref" reference="subsection:devissage"}. Also, we shall, for $1 \leq i < j \leq k$, use the abreviation: $\mu_{i,j} = \mu_{i} - \mu_{j} \in {\mathbf N}^{*}$.

::: defn
\(i\) A summation divisor adapted to $A_{0}$ is a family $(D_{i,j})_{1 \leq i < j \leq k}$ of effective divisors over the elliptic curve ${\mathbf{E}_{q}}$, each $D_{i,j}$ having degree $\mu_{i,j}$, the family satisfying moreover the following compatibility condition: $$\forall i,l,j \text{~such that~} 1 \leq i < l < j \leq k \;,\;
D_{i,j} = D_{i,l} + D_{l,j}.$$ Obviously, it amounts to the same thing to give only the $k-1$ divisors $D_{i,i+1}$, $i = 1,\ldots,k-1$.\
(ii) We say that the adapted summation divisor $(D_{i,j})_{1 \leq i < j \leq k}$ is allowed if it satisfies the following conditions: $$\forall i,j \text{~such that~} 1 \leq i < j \leq k \;,\;
ev_{{\mathbf{E}_{q}}}(D_{i,j}) \not\in 
\overline{(-1)^{\mu_{i,j}} \frac{Sp(A_{i})}{Sp(A_{j})}}.$$ Here, for $S,T \subset {\mathbf C}^{*}$, we put $\frac{S}{T} = \{\frac{s}{t} \;/\; s \in S , t \in T\}$; $\overline{X}$ and $ev_{{\mathbf{E}_{q}}}$ were defined in the introduction.
:::

Note that, for an adapted summation divisor, the condition of being allowed is a generic one.

::: example
A special case is that of an adapted summation divisor concentrated on a point $\alpha \in {\mathbf{E}_{q}}$, that is, each $D_{i,j} = \mu_{i,j} [\alpha]$. Then the condition that $D$ is allowed is equivalent to: $$\forall i,j \text{~such that~} 1 \leq i < j \leq k \;,\;
\mu_{i,j} \; \alpha \not\in \overline{Sp(A_{i})} - \overline{Sp(A_{j})}.$$ It is generically (that is, over a non empty Zariski open subset) satisfied by $\alpha \in {\mathbf{E}_{q}}$.
:::

Now, let $(D_{i,j})_{1 \leq i < j \leq k}$ be a summation divisor adapted to $A_{0}$. We choose points $a_{l} \in {\mathbf C}^{*}$ for $\mu_{k} < l \leq \mu_{1}$ such that, for $1 \leq i < j \leq k$, $$D_{i,j} = \sum_{\mu_{j} < l \leq \mu_{i}} [\overline{a_{l}}].$$ These certainly exist. We then put: $$t_{i} = \theta_{q}^{\mu_{k}} \prod_{\mu_{l} < l \leq \mu_{i}} \theta_{q,-a_{l}}.$$

::: lemma
\(i\) The functions $t_{1},\ldots,t_{k} \in {\mathcal{M}({\mathbf C}^{*})}$ are such that:\
(i1) For $i = 1,\ldots,k$, $\sigma_qt_{i} = \alpha_{i} z^{\mu_{i}} t_{i}$, where $\alpha_{i} \in {\mathbf C}^{*}$.\
(i2) For $1 \leq i < j \leq k$, $div_{{\mathbf{E}_{q}}}(t_{i}) - div_{{\mathbf{E}_{q}}}(t_{j}) = D_{i,j}$ (the notation is explained in the course of the proof).\
(i3) For $1 \leq i < j \leq k$, the function $t_{i,j} = \frac{\sigma_qt_{i}}{t_{j}}$ belongs to $\mathcal{O}({\mathbf C}^{*})$.\
(ii)If the summation divisor $(D_{i,j})_{1 \leq i < j \leq k}$ is moreover allowed, for $1 \leq i < j \leq k$, the spectra of $\alpha_{i} A_{i}$ and $\alpha_{j} A_{j}$ have empty intersection on ${\mathbf{E}_{q}}$: $$\overline{Sp(\alpha_{i} A_{i})} \cap \overline{Sp(\alpha_{j} A_{j})} =
\emptyset.$$
:::

It is an immediate consequence of the properties recalled in the introduction that these functions $t_{i}$ indeed satisfy (i1). Moreover, the functional equation implies that the divisor $div_{{\mathbf C}^{*}}(t_{i})$ of zeroes and poles of $t_{i}$ on ${\mathbf C}^{*}$ is invariant under the action of $q^{{\mathbf Z}}$, so that it makes sense to consider it as a divisor $\text{div}_{{\mathbf{E}_{q}}}(t_{i})$ on ${\mathbf{E}_{q}}$ (alternatively, one can consider $t_{i}$ as a section of a line bundle over ${\mathbf{E}_{q}}$ and the notation is then classical). Again because of the properties of theta-functions, one clearly gets (i2). Assertion (i3) comes from the equalities: $$\begin{aligned}
t_{i,j} & = & \frac{\sigma_qt_{i}}{t_{i}} \times \frac{t_{i}}{t_{j}} \\ 
        & = & \alpha_{i} z^{\mu_{i}} \times 
\text{~a function with positive divisor~}.
\end{aligned}$$ The function $\theta_{q}^{\mu_{i}} \frac{\theta_{q}}{\theta{q,\alpha_{i}}}$ satisfies the same functional equation as $t_{i}$, which means that their quotient is elliptic so that its divisor on ${\mathbf{E}_{q}}$ has trivial evaluation. Therefore: $$div_{{\mathbf{E}_{q}}}(t_{i}) = \overline{\frac{(-1)^{\mu_{i}}}{\alpha_{i}}}.$$ The conclusion (ii) then follows from the definition of an allowed divisor. $\Box$\
We now introduce a temporary and slightly ambiguous notation. For an adapted summation divisor $D = (D_{i,j})_{1 \leq i < j \leq k}$, we write $\Theta_{D}$ for the following block-diagonal matrix: $$\Theta_{D} = 
\begin{pmatrix}
t_{1} I_{r_{1}}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & 0 & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & t_{k} I_{r_{k}}    
\end{pmatrix}.$$ Of course, it does not only depend on $D$, but on a particular choice of the functions $t_{1},\ldots,t_{k}$ whose existence has just been established. However, the summation process that we are defining will produce a result that only depends on $D$. For a family of recangular blocks $U'_{I,j}$, we shall use the following abreviation: $$A'_{U'} =
\begin{pmatrix}
A'_{1}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & U'_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & A'_{k}    
\end{pmatrix},$$

::: lemma
\(i\) The effect of the gauge transformation $\Theta_{D}$ is to \"regularize\" the diagonal blocks of $A = A_{U}$: $\Theta_{D}[A] = A'_{U'}$, where, for $1 \leq i < j \leq k$, $U'_{i,j} = t_{i,j} U_{i,j} \in M_{r_{i},r_{j}}({\mathcal{O}({\mathbf C}^{*},0)})$ and, for $i = 1,\ldots,k$, $A'_{i} = \alpha_{i} A_{i} \in GL_{r_{i}}({\mathbf C})$. If moreover the adapted summation divisor $D$ is allowed, then, for $1 \leq i < j \leq k$, $\overline{Sp(A'_{i})} \cap \overline{Sp(A'_{j})} = \emptyset$.\
(ii) Suppose we started with $A_{U}$ in polynomial normal form. Then we get $A'_{U'}$ such that $U'_{i,j} \in M_{r_{i},r_{j}}({\mathcal{O}({\mathbf C}^{*})})$.
:::

The computations are immediate. $\Box$\
We shall now take two matrices $A_{U}$ and $A_{V}$ in the formal class of $A_{0}$, flatten their slopes through the gauge transformation $\Theta_{D}$, and then link the resulting matrices $A'_{U'}$ and $A'_{V'}$ by an isomorphism defined over ${\mathbf C}^{*}$. This relies on the following

::: prop
\(i\) Let $$A'_{U'} = \begin{pmatrix}
A'_{1}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & U'_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & A'_{k}    
\end{pmatrix}
\quad \text{~and~} \quad
A'_{V'} = \begin{pmatrix}
A'_{1}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & V'_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & A'_{k}    
\end{pmatrix},$$ where, for $i = 1,\ldots,k$, $A'_{i} \in GL_{r_{i}}({\mathbf C})$ are such that, for $1 \leq i < j \leq k$, $\overline{Sp(A'_{i})} \cap \overline{Sp(A'_{j})} = \emptyset$ and, for $1 \leq i < j \leq k$, $U'_{i,j}, V'_{i,j} \in M_{r_{i},r_{j}}({\mathcal{O}({\mathbf C}^{*},0)})$. Then, there exists a unique $F' \in {\mathfrak{G}}({\mathcal{O}({\mathbf C}^{*},0)})$ such that $F'[A'_{U'}] = A'_{V'}$.\
(ii) If , for $1 \leq i < j \leq k$, $U'_{i,j}, V'_{i,j} \in M_{r_{i},r_{j}}({\mathcal{O}({\mathbf C}^{*})})$, then $F' \in {\mathfrak{G}}({\mathcal{O}({\mathbf C}^{*})})$
:::

We have to solve inductively the system of equations: $$\left(\sigma_qF'_{i,j}\right) - A'_{i} F'_{i,j} =
V'_{i,j} - U'_{i,j} +
\sum_{i < l < j} V'_{i,l} F'_{l,j} - 
\sum_{i < l < j} \left(\sigma_qF'_{i,l}\right) U'_{l,j}.$$ The induction is the same as the one we met when buliding normal polynomial forms. The proposition then follows from the following lemma.

::: lemma
\(i\) Let $B \in GL_{s}({\mathbf C})$ and $C \in GL_{t}({\mathbf C})$ be invertible complex matrices such that $\overline{Sp(B)} \cap \overline{Sp(C)} = \emptyset$. Then, for $Y' \in M_{t,s}({\mathcal{O}({\mathbf C}^{*},0)})$, the equation: $$\left(\sigma_qX'\right) B - C X' = Y'$$ has a unique solution $X' \in M_{t,s}({\mathcal{O}({\mathbf C}^{*},0)})$.\
(ii) If $Y' \in M_{t,s}({\mathcal{O}({\mathbf C}^{*})})$, then $X' \in M_{t,s}({\mathcal{O}({\mathbf C}^{*})})$.
:::

We write the Laurent series: $$X' = \sum_{n \in {\mathbf Z}} X'_{n} z^{n} \quad \text{and} \quad
Y' = \sum_{n \in {\mathbf Z}} Y'_{n} z^{n}.$$ By identification, we obtain $X'_{n} = \Phi_{q^{n} B,C}^{-1}(Y'_{n})$, where $\Phi_{q^{n} B,C}$ is the automorphism $M \mapsto M (q^{n} B) - C M$ of $M_{t,s}({\mathbf C})$; that it is indeed an automorphism comes from the assumption that $q^{n} B$ and $C$ have non intersecting spectra. For $n \to + \infty$, $\Phi_{q^{n} B,C}^{-1} \sim q^{-n} \Phi_{B,0}^{-1}$ and, for $n \to - \infty$, $\Phi_{q^{n} B,C}^{-1} \to \Phi_{0,C}^{-1}$. Taking $]r,R[ \times e^{\imath {\mathbf R}}$ to be the annulus of convergence of $Y'$, we conclude that the annulus of convergence of $X'$ is $]r,|q| R[ \times e^{\imath {\mathbf R}}$. Annuli of definition actually grow, again an illustration of the good regularity properties of the homological equation. $\Box$\
Putting it all together, we now get our first fundamental theorem.

::: thm
[]{#thm:resommation-algebrique label="thm:resommation-algebrique"} (i) Let $A_{U},A_{V}$ be defined as above, in the formal class of $A_{0}$. Then, there exists a unique $F \in {\mathfrak{G}}({\mathcal{M}({\mathbf C}^{*},0)})$ such that $F[A_{U}] = A_{V}$ and, for $1 \leq i < j \leq k$, $\text{div}_{{\mathbf{E}_{q}}}(F_{i,j}) \geq - D_{i,j}$ (the notation is explained in the course of the proof).\
(ii) If $A_{U},A_{V}$ are in polynomial normal form, $F \in {\mathfrak{G}}({\mathcal{M}({\mathbf C}^{*})})$.
:::

We put $A'_{U'} = \Theta_{D}[A_{U}]$ and $A'_{V'} = \Theta_{D}[A_{V}]$, then $F[A_{U}] = A_{V}$ is equivalent to $F'[A'_{U'}] = A'_{V'}$, where $F' = \Theta_{D} F \Theta_{D}^{-1}$. The matrices $F$ and $F'$ together are upper-triangular with diagonal blocks $I_{r_{1}},\ldots,I_{r_{k}}$ and their over-diagonal blocks are related by the relations: $F_{i,j} = \frac{t_{j}}{t_{i}}F'_{i,j}$. This implies the unicity of $F \in {\mathfrak{G}}({\mathcal{M}({\mathbf C}^{*},0)})$ (resp. ${\mathfrak{G}}({\mathcal{M}({\mathbf C}^{*})})$) subject to the constraint that the coefficients of $F_{i,j}$ belong to $\frac{t_{j}}{t_{i}} {\mathcal{O}({\mathbf C}^{*},0)}$ (resp. $\frac{t_{j}}{t_{i}} {\mathcal{O}({\mathbf C}^{*})}$). Since $div_{{\mathbf{E}_{q}}}(t_{i}) - div_{{\mathbf{E}_{q}}}(t_{j}) = D_{i,j}$, this proves (and explains) the given condition. $\Box$\
As a matter of notation, we shall write $F_{D}(U,V)$ for the $F$ obtained in the theorem: it does indeed depend solely on $D$. We see it as the canonical resummation of $\hat{F}(U,V)$ along the "direction" $D$. We shall write in particular $F_{D}(U) = F_{D}(0,U)$.\
Let us call ${\mathfrak{G}}_{D}({\mathcal{M}({\mathbf C}^{*},0)})$ (resp. ${\mathfrak{G}}_{D}({\mathcal{M}({\mathbf C}^{*})})$) the subset of ${\mathfrak{G}}({\mathcal{M}({\mathbf C}^{*},0)})$ (resp. of ${\mathfrak{G}}({\mathcal{M}({\mathbf C}^{*})})$) defined by the constraints: for $1 \leq i < j \leq k$, $\text{div}_{{\mathbf{E}_{q}}}(F_{i,j}) \geq - D_{i,j}$.

::: cor
$F_{D}(U,V) = F_{D}(V) F_{D}(U)^{-1}$.
:::

Actually, ${\mathfrak{G}}_{D}({\mathcal{M}({\mathbf C}^{*},0)}) = \Theta_{D} {\mathfrak{G}}({\mathcal{O}({\mathbf C}^{*},0)}) \Theta_{D}^{-1}$ and ${\mathfrak{G}}_{D}({\mathcal{M}({\mathbf C}^{*})}) = \Theta_{D} {\mathfrak{G}}({\mathcal{O}({\mathbf C}^{*})}) \Theta_{D}^{-1}$, so that these subsets are subgroups. Then the statement follows from the unicity property in the theorem. $\Box$

::: cor
The conclusion of the theorem still holds if one only assumes that $U = (U_{i,j}) \in 
\underset{1 \leq i < j \leq k}{\prod} {\mathcal{M}}_{r_{i},r_{j}}({\mathcal{O}({\mathbf C}^{*},0)})$.
:::

This immediately follows from corollary [\[cor:Rwg=Ka\]](#cor:Rwg=Ka){reference-type="ref" reference="cor:Rwg=Ka"}. $\Box$

::: rmk
It is not difficult to prove that $\hat{F}(U,V)$ is the aymptotic expansion of $F_{D}(U,V)$ in the sense of section [\[subsection:irregular-theory\]](#subsection:irregular-theory){reference-type="ref" reference="subsection:irregular-theory"}. One first has to extend the definitions so as to allow for a pole at $0$.The proof then proceeds in two steps.

1.  First, one proves that, in its domain of definition, $F_{D}(U,V)$ is a section of the sheaf $z^{d} {\mathcal{B}}$ for some $d \in {\mathbf Z}$. This is done using only the functional equation that it satisfies, and studying inductively its upper diagonal blocks $F_{i,j}$.

2.  Then, one proves that the operator $F \mapsto A_{V}^{-1} \left(\sigma_qF\right) A_{U}$, sends ${\mathfrak{G}}(z^{d} {\mathcal{B}})$ to ${\mathfrak{G}}(z^{d+1} {\mathcal{B}})$. Starting from $F_{D}(U,V)$ and iterating yields the conclusion.

Actually, in [@RSZ], a stronger result is proved. It relies on a refined definition of asymptotics taking in account the position of poles; this is essential to get summation by discrete integral formulas.
:::

::: rmk
[]{#rmk:fibre-functor label="rmk:fibre-functor"} To give our theorem its functorial meaning, one should proceed as follows. One generalizes the construction of a vector bundle $F_{M}$ from a $q$-difference module $M$. This defines a fibre functor $\omega$ over ${\mathbf{E}_{q}}$. Then, for each $D$, if one restricts to an appropriate subcategory of ${\mathcal{E}}^{(0)}_{1}$, $M \leadsto F_{D}(M)$ is an isomorphism from the fibre functor $\omega \circ gr$ to $\omega$. On the other hand, endowing $F_{M}$ with the filtration coming from that of $M$, one defines an enriched functor and the underlying principle of all our uses of the homological equation is that this functor is fully faithful. This is exploited in [@JSIRR].
:::

## Applications to classification

### One direction of summation

Let $A_{U},A_{V}$ be defined over ${{\mathbf C}(\{z\})}$. Suppose $A_{U}$ and $A_{V}$ are analytically equivalent. Then the power series $\hat{F}(U,V)$ is convergent and satisfies the conclusion of theorem [\[thm:resommation-algebrique\]](#thm:resommation-algebrique){reference-type="ref" reference="thm:resommation-algebrique"}, so that, by unicity, $F_{D}(U,V) = \hat{F}(U,V)$ for any allowed summation divisor. Conversely:

::: prop
[]{#prop:tout-dans-les-poles label="prop:tout-dans-les-poles"} Suppose $F_{D}(U,V) \in {\mathfrak{G}}({\mathcal{O}({\mathbf C}^{*},0)})$. Then $A_{U}$ and $A_{V}$ are analytically equivalent (and all the above holds).
:::

The gauge transform $F = F_{D}(U,V)$ is obtained by solving the system of equations: $$z^{-\mu_{j}} \left(\sigma_qF_{i,j} \right) A_{j} - z^{-\mu_{i}} A_{i} F_{i,j} =
V_{i,j} - U_{i,j} + \sum_{i < l < j} V_{i,l} F_{l,j} - 
\sum_{i < l < j} \left(\sigma_qF_{i,l}\right) U_{l,j}.$$ By induction, we are reduced to the following lemma:

::: lemma
Let $\mu > \mu'$ in ${\mathbf Z}$, $A \in GL_{r}({\mathbf C})$,$A' \in GL_{r'}({\mathbf C})$ and $Y \in {\mathcal{M}}_{r,r'}({{\mathbf C}(\{z\})})$. Let $X \in {\mathcal{M}}_{r,r'}({\mathcal{O}({\mathbf C}^{*},0)})$ be a solution of the equation: $$\left(\sigma_qX \right) (z^{-\mu'} A') - (z^{-\mu} A) X = Y.$$ Then, one actually has $X \in {\mathcal{M}}_{r,r'}({{\mathbf C}(\{z\})})$.
:::

Going to the Laurent series and identifying coefficients, one finds: $$\forall n \in {\mathbf Z}\;,\; 
q^{n+\mu'} X_{n + \mu'} A' - A X_{n+\mu} = Y_{n}.$$ Since $Y \in {\mathcal{M}}_{r,r'}({{\mathbf C}(\{z\})})$, $Y_{n} = 0$ for $n << 0$. Therefore, for $n << 0$, writing $d = \mu - \mu' \in {\mathbf N}^{*}$, one has $X_{n} = q^{-n} A X_{n+d} {A'}^{-1}.$ Since $|q| > 1$, either $X_{n} = 0$ for $n << 0$, or the coefficients of $X$ are rapidly growing for indices near $- \infty$ prohibiting convergence and contradicting the assumption that $X \in {\mathcal{M}}_{r,r'}({\mathcal{O}({\mathbf C}^{*},0)})$. $\Box$\
In order to make this a statement about classification, we introduce one more notation. We write: $${\mathfrak{G}}_{D}^{A_{0}}({\mathcal{M}({\mathbf C}^{*},0)}) = \{F \in {\mathfrak{G}}_{D}({\mathcal{M}({\mathbf C}^{*},0)}) \;/\; F[A_{0}] \in GL_{n}({{\mathbf C}(\{z\})})\}.$$ Clearly, the subset ${\mathfrak{G}}_{D}^{A_{0}}({\mathcal{M}({\mathbf C}^{*},0)})$ of the group ${\mathfrak{G}}_{D}({\mathcal{M}({\mathbf C}^{*},0)})$ is stable under the action by left translations of the subgroup ${\mathfrak{G}}({\mathcal{O}({\mathbf C}^{*},0)})$. Now, the above proposition immediately entails:

::: prop
Mapping $A_{U}$ to $F_{D}(U)$ yields a bijection: $${\mathcal{F}}(M_{0}) \rightarrow {\mathfrak{G}}({\mathcal{O}({\mathbf C}^{*})}) \diagdown {\mathfrak{G}}_{D}^{A_{0}}({\mathcal{M}({\mathbf C}^{*},0)}).$$
:::

$\Box$\
This is strikingly similar to the corresponding "formal modulo analytic" description in proposition [\[prop:formel-modulo-convergent\]](#prop:formel-modulo-convergent){reference-type="ref" reference="prop:formel-modulo-convergent"}.

### Varying the direction of summation

Let $D = (D_{i,j})_{1 \leq i < j \leq k}$ be an allowed summation divisor for $M_{0}$, $A_{0}$. We consider as its support and write $Supp(D)$ the union $\underset{1 \leq i < j \leq k}{\bigcup} Supp(D_{i,j})$ and define the following Zariski open subset of ${\mathbf{E}_{q}}$: $V_{D} = {\mathbf{E}_{q}}\setminus \text{Supp}(D)$. We also write $U_{D}$ for the preimage of $V_{D}$ in ${\mathbf C}^{*}$. Thus, the elements of ${\mathfrak{G}}_{D}({\mathcal{M}({\mathbf C}^{*},0)})$ are holomorphic germs over $(U_{D},0)$.\
Now let $D'$ be another allowed summation divisor. Then, for any $A_{U}$ in the formal class of $A_{0}$, the gauge transformation $F_{D,D'}(U) \underset{def}{=} F_{D}(U)^{-1} F_{D'}(U)$ sends $A_{0}$ to itself. It is holomorphic on the open subset $(U_{D} \cap U_{D'},0)$. We call $U_{D,D'}$ the sector $U_{D} \cap U_{D'}$, which is the preimage of the open subset $V_{D,D'} = V_{D} \cap V_{D'}$ of ${\mathbf{E}_{q}}$. Note that, if $D$ and $D'$ have non intersecting supports (which is easy to realize), then $U_{D}$ and $U_{D'}$ cover ${\mathbf C}^{*}$ and $V_{D}$ and $V_{D'}$ cover ${\mathbf{E}_{q}}$.

::: lemma
$F_{D,D'}(U)$ is a section of the sheaf $\Lambda_{I}(M_{0})$ over $V_{D,D'}$.
:::

One only has to prove that the upper-diagonal part of $F = F_{D,D'}(U)$ is flat. But its rectangular blocks satisfy: $\left(\sigma_qF_{i,j}\right) (z^{-\mu_{j}} A_{j}) = 
(z^{-\mu_{i}} A_{i}) F_{i,j}$. This is a pure system of slope $\mu_{i,j} > 0$, hence $F_{i,j}$ is indeed flat by lemma [\[lemma:flatness\]](#lemma:flatness){reference-type="ref" reference="lemma:flatness"}. $\Box$\
We now call ${\mathfrak{U}}$ (resp. ${\mathfrak{V}}$) the covering of ${\mathbf C}^{*}$ (resp. of ${\mathbf{E}_{q}}$) by the open subsets $U_{D}$ (resp. $V_{D}$), where $D$ runs among all the allowed summation divisors for $A_{0}$, $M_{0}$. The following is immediate.

::: cor
The family $(F_{D,D'}(U))_{D,D'}$ is a Cech cocycle of the sheaf $\Lambda_{I}(M_{0})$ for the covering ${\mathfrak{V}}$ of ${\mathbf{E}_{q}}$.
:::

$\Box$

::: prop
[]{#prop:cocycles-privilegies label="prop:cocycles-privilegies"} Mapping $A_{U}$ to the cocycle $(F_{D,D'}(U))$ defines a one-to-one mapping: $${\mathcal{F}}(M_{0}) \hookrightarrow Z^{1}({\mathfrak{V}},\Lambda_{I}(M_{0})).$$
:::

If $A_{U}$ is analytically equivalent to $A_{V}$, we have $A_{V} = F[A_{U}]$ for a unique $F \in {\mathfrak{G}}({{\mathbf C}(\{z\})})$ and it is clear (by unicity) that $F_{D}(V) = F F_{D}(U)$ for all allowed divisors $D$, whence $F_{D,D'}(V) = F_{D,D'}(U)$ by immediate computation. This shows that the above mapping is well defined.\
Conversely, just assume that $F_{D,D'}(V) = F_{D,D'}(U)$ for two allowed divisors with non intersecting supports. This equality gives $F_{D}(U,V) = F_{D'}(U,V)$. Hence, both sides are holomorphic over $U_{D} \cup U_{D'} = {\mathbf C}^{*}$ (near $0$), and we already saw in proposition [\[prop:tout-dans-les-poles\]](#prop:tout-dans-les-poles){reference-type="ref" reference="prop:tout-dans-les-poles"} that this implies the analytic equivalence of $A_{U}$ and $A_{V}$. $\Box$\
We now come to the second fundamental result of this paper.

::: thm
[]{#thm:q-Malgrange-Sibuya label="thm:q-Malgrange-Sibuya"} The above mapping yields a bijective correspondance: $${\mathcal{F}}(M_{0}) \simeq H^{1}({\mathbf{E}_{q}},\Lambda_{I}(M_{0})).$$
:::

Let $A_{U}$ and $A_{V}$ have the same image in $H^{1}({\mathbf{E}_{q}},\Lambda_{I}(M_{0})$, hence in $H^{1}({\mathfrak{V}},\Lambda_{I}(M_{0})$ (in Cech cohomology, the $H^{1}$ of a covering embeds into the direct limit). There is, for each allowed divisor $D$, a matrix $G(D) \in {\mathfrak{G}}({\mathcal{O}}(U_{D})) \cap Aut(M_{0})$ in such a way that: $$\forall D,D' \;:\;
F_{D,D'}(U) = \left(G(D)\right)^{-1} F_{D,D'}(V) G(D').$$ One draws that $F_{D}(V) G(D) \left(F_{D}(U)\right)^{-1}$ does not depend on $D$, so that it is holomorphic on $\bigcup U_{D} = {\mathbf C}^{*}$; call $\Phi$ their common value. As a gauge transformation, it sends $A_{U}$ to $A_{V}$. By proposition [\[prop:tout-dans-les-poles\]](#prop:tout-dans-les-poles){reference-type="ref" reference="prop:tout-dans-les-poles"}, $A_{U}$ and $A_{V}$ are analytically equivalent, which proves the injectivity.\
We now prove that our mapping from ${\mathcal{F}}(M_{0})$ to $H^{1}({\mathfrak{V}},\Lambda_{I}(M_{0}))$ is onto. For that, we take $(\Phi_{D,D'})_{D,D'} \in Z^{1}({\mathfrak{V}},\Lambda_{I}(M_{0}))$. By definition of the sheaf $\Lambda_{I}(M_{0})$, each component $\Phi_{D,D'}$ is an element of ${\mathfrak{G}}({\mathcal{O}}(U_{D,D'}))$, so that our cocycle can be considered as describing a vector bundle over ${\mathbf C}^{*}$, trivialized by the covering ${\mathfrak{U}}$ and with structural group in ${\mathfrak{G}}$. By [@Rohrl62], theorem 1.0 (see also [@Rohrl57]) it is trivial in the following sense: there is, for each $D$, a $\Phi_{D} \in {\mathfrak{G}}({\mathcal{O}}(U_{D}))$ in such a way that, for all $D,D'$, $\Phi_{D,D'} = \Phi_{D}^{-1} \Phi_{D'}$. Since the $\Phi_{D,D'}$ are automorphisms of $A_{0}$, the $\Phi_{D}[A_{0}]$ are all equal to a same matrix $A_{U'}$. Moreover, this is holomorphic over ${\mathbf C}^{*}$. By corollary [\[cor:Rwg=Ka\]](#cor:Rwg=Ka){reference-type="ref" reference="cor:Rwg=Ka"}, there is a $\Psi \in {\mathfrak{G}}({\mathcal{O}({\mathbf C}^{*},0)})$ such that $A_{U} = \Psi[A_{U'}]$ is meromorphic at $0$. Then $\Psi \Phi_{D}$ is holomorphic on $(U_{D},0)$ and sends $A_{0}$ to $A_{U}$. Put $G_{D} = F_{D}(U)^{-1} \Psi \Phi_{D}$. This is a section of $\Lambda_{I}(M_{0})$ over $V_{D}$. The equalities $F_{D}(U) G_{D} = \Psi \Phi_{D}$ entail $\Phi_{D}^{-1} \Phi_{D'} = G_{D}^{-1} F_{D,D'}(U) G_{D'}$, that is, the cocycle $(\Phi_{D,D'})_{D,D'}$ is equivalent to the cocycle $(F_{D,D'}(U))_{D,D'}$ which ends the proof of our statement.\
There remains to check that the natural mapping from $H^{1}({\mathfrak{V}},\Lambda_{I}(M_{0}))$ to $H^{1}({\mathbf{E}_{q}},\Lambda_{I}(M_{0}))$ is onto (we already said it was one-to-one). This is the content of proposition [\[prop:bon-recouvrement\]](#prop:bon-recouvrement){reference-type="ref" reference="prop:bon-recouvrement"}, to be proved after the discussion on the $q$-Gevrey filtration of the Stokes sheaf the in next chapter. $\Box$
