---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-010-10-the-rational-daha
section_title: "The Rational DAHA"
section_number: 10
pages: 64-71
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.978
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the Weyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
[]{#sec:daha label="sec:daha"}

## 

As in the previous section, *we do not assume that $W$ is crystallographic*. Let $\mathrm{Ref}(W) \subseteq W$ be the subset of elements that act on $\bb{V}$ by reflections, *cf.* §[\[subsec:families\]](#subsec:families){reference-type="ref" reference="subsec:families"}. We continue to assume that $\bb{V}^W = 0$.

We write $\langle-, -\rangle : \bb{V} \times \bb{V}^\vee \to \bb{Q}_W$ for the evaluation pairing. For each reflection $t \in \mathrm{Ref}(W)$, we fix nonzero vectors $\alpha_t \in \bb{V}$ and $\alpha_t^\vee \in \bb{V}^\vee$ such that

1.  $\langle\alpha_t, -\rangle = 0$ is the hyperplane of $\bb{V}^\vee$ fixed by $t$.

2.  $\langle-, \alpha_t^\vee\rangle = 0$ is the hyperplane of $\bb{V}$ fixed by $t$.

3.  $\langle\alpha_t, \alpha_t^\vee\rangle = 2$.

In the literature, the vectors $\alpha_t$ and $\alpha_t^\vee$ are called roots and coroots even when $W$ is not crystallographic. Condition (3) will ensure that in what follows, our constructions do not depend on the exact choices of $\alpha_t, \alpha_t^\vee$.

For any $\nu\in \bb{C}$, the **rational Cherednik algebra** or **rational DAHA of slope $\nu$** is the $\bb{C}$-algebra $$\begin{aligned}
\bb{D}_\nu^\mathit{rat}
=   \frac{\bb{C}[W] \ltimes (\Sym(\bb{V}) \otimes \Sym(\bb{V}^\vee))}{\left\langle 
yx - xy - \langle x, y\rangle + \nu\displaystyle\sum_{t \in \mathrm{Ref}(W)} \langle x, \alpha^\vee\rangle\langle\alpha, y\rangle t
: x \in \bb{V},\,y \in \bb{V}^\vee
\right\rangle}.
\end{aligned}$$ Note that $\bb{D}_\nu^\mathit{rat}$ contains $\bb{A}_W = \bb{C}[W] \ltimes \Sym(\bb{V})$ as a subalgebra, regardless of $\nu$.

::: rem
If $\nu= 0$, then the defining relations of $\bb{D}_\nu^\mathit{rat}$ simplify to $[x, y] = \langle x, y\rangle$ for all $x$ and $y$. This shows that $\bb{D}_0^\mathit{rat}$ is isomorphic to $\bb{C}[W] \ltimes \cal{D}(\bb{V})$, the semidirect product of $\bb{C}[W]$ with the Weyl algebra of $\bb{V}$.
:::

## 

Like the universal enveloping algebra of a semisimple Lie algebra, $\bb{D}_\nu^\mathit{rat}$ admits a triangular decomposition in the sense of Poincaré--Birkhoff--Witt. It therefore admits an analogue of the Bernstein--Gelfand--Gelfand category $\sf{O}$, which we will denote by $\sf{O}_\nu$ [@ggor].

Any $\bb{D}_\nu^\mathit{rat}$-module $M \in \sf{O}_\nu$ can be viewed as a $W$-equivariant quasicoherent sheaf on $\bb{V}^\vee = \Spec \Sym(\bb{V})$. The **support** of $M$ is the $W$-stable subvariety of $\bb{V}^\vee$ that forms its support as a sheaf. Let $\sf{O}_\nu^\tor \subseteq \sf{O}_\nu$ be the Serre subcategory of modules that are torsion over $\Sym(\bb{V}^\vee) \subseteq \bb{D}_\nu^\mathit{rat}$. By [@ggor Lem. 5.1], $\sf{O}_\nu^\tor$ is also the full subcategory of $\sf{O}_\nu$ of modules supported on the discriminant locus of $\bb{V}^\vee$, *i.e.*, the common complement of the reflection hyperplanes of the $W$-action.

The Verma modules in $\sf{O}_\nu$ are indexed by the set $\hat{W}$. For all $\phi \in \hat{W}$, we write $\Delta_\nu(\phi)$ for the corresponding Verma module of $\bb{D}_\nu^\mathit{rat}$, and we write $L_\nu(\phi)$ for its simple quotient. Explicitly, $\Delta_\nu(\phi)$ can be constructed by inflating $\phi$ from $\bb{C}[W]$ up to $\bb{A}_W$, then tensoring up to $\bb{D}_\nu^\mathit{rat}$. In the literature, $\Delta_\nu(1)$ is known as the polynomial module and $L_\nu(1)$ as the simple spherical module.

Like the Weyl algebra of $\bb{V}$, the rational Cherednik algebra contains a canonical "Euler element" $\bm{h}$. For the precise definition, see [@etingof_2007 Ch. 11]. It commutes with the subalgebra $\bb{C}[W] \subseteq \bb{D}_\nu^\mathit{rat}$, and its action on any object of $\sf{O}_\nu$ is locally finite. Thus, each object $M \in \sf{O}$ is endowed with a decomposition into finite-dimensional, $W$-stable $\bm{h}$-eigenspaces. On all $\bb{D}_\nu^\mathit{rat}$-modules that we will need, the eigenvalues will be half-integers. We define the **$\bm{q}$-graded character** of such a module $M$ to be $$\begin{aligned}
_{\bm{q}} 
=   \sum_n {\bm{q}^{\frac{n}{2}}} M_{\frac{n}{2}} \in R(W)(\!(\bm{q}^{\frac{1}{2}})\!)
\end{aligned}$$ where $M_{\frac{n}{2}} \subseteq M$ is the $\bm{h}$-eigenspace of eigenvalue $\frac{n}{2}$. By [@etingof_2007 Ch. 11], $$\begin{aligned}
\label{eq:verma}
[\Delta_\nu(\phi)]_{\bm{q}}
=   \bm{q}^{\frac{r}{2} - \nu\bb{c}(\phi)} \phi \cdot [\Sym(\bb{V})]_{\bm{q}}
\end{aligned}$$ for all $\phi \in \hat{W}$, where we set $[\Sym(\bb{V})]_{\bm{q}} = \sum_i {\bm{q}^i} \Sym^i(\bb{V})$ as in Sections [\[sec:decat\]](#sec:decat){reference-type="ref" reference="sec:decat"}-[\[sec:dl\]](#sec:dl){reference-type="ref" reference="sec:dl"} and §[\[subsec:realization\]](#subsec:realization){reference-type="ref" reference="subsec:realization"} of Appendix [\[sec:coxeter\]](#sec:coxeter){reference-type="ref" reference="sec:coxeter"}.

The basic problem in the representation theory of $\bb{D}_\nu^\mathit{rat}$ is to understand how the graded characters $[\Delta_\nu(\phi)]_{\bm{q}}$, which are explicit, can be used to express the graded characters $[L_\nu(\phi)]_{\bm{q}}$, which are initially mysterious. The problem is highly sensitive to the value of $\nu$. When $\nu\notin \bb{Q}$, category $\sf{O}$ is semisimple and $[L_\nu(\phi)]_{\bm{q}} = [\Delta_\nu(\phi)]_{\bm{q}}$. When $\nu\in \bb{Q}$, category $\sf{O}$ is no longer semisimple: It grows more complex as the denominator of $\nu$ grows smaller.

## 

Let $\zeta^{\frac{1}{2}} = e^{\pi i\nu}$. We draw freely upon the notation in §[\[subsec:cyclotomic\]](#subsec:cyclotomic){reference-type="ref" reference="subsec:cyclotomic"}, so that $$\begin{aligned}
H_W(\zeta^{\frac{1}{2}}) = H_W \otimes_{\bb{Z}[\bm{q}^{\pm\frac{1}{2}}]} \bb{Q}_W(\zeta^{\frac{1}{2}})
\end{aligned}$$ and $\bm{d}_\zeta : R^+(H_W(\bm{q}^{\frac{1}{2}})) \to R^+(H_W(\zeta^{\frac{1}{2}}))$ is the decomposition map that corresponds to the specialization $\bm{q}^{\frac{1}{2}} \mapsto \zeta^{\frac{1}{2}}$. Let $\sf{Mod}(H_W(\zeta^{\frac{1}{2}}))$ be the category of $H_W(\zeta^{\frac{1}{2}})$-modules, and for each $\phi \in \hat{W}$, let $$\begin{aligned}
\phi_\zeta = \bm{d}_\zeta(\phi_{\bm{q}}) \in \sf{Mod}(H_W(\zeta^{\frac{1}{2}})).
\end{aligned}$$ In [@ggor], Ginzburg, Guay, Opdam, and Rouquier introduced the **Knizhnik--Zamolodchikov (KZ) functor**, an exact monoidal functor $$\begin{aligned}
\sf{KZ} : \sf{O}_\nu\to \sf{Mod}(H_W(\zeta^{\frac{1}{2}})).
\end{aligned}$$ The following facts comprise [@ggor Thm. 5.14, Cor. 5.18, Thm. 6.8]:

::: thm
[]{#thm:ggor label="thm:ggor"} For all $\nu\in \bb{C}$,

1.  $\sf{KZ}$ induces an equivalence $\sf{O}_\nu/\sf{O}_\nu^\tor \simeq \sf{Mod}(H_W(\zeta^{\frac{1}{2}}))$.

2.  $\sf{KZ}$ induces an isomorphism between the (vertical) center of $\sf{O}_\nu$, *i.e.*, the algebra of endomorphisms of its unit object, and the center of $H_W(\zeta^{\frac{1}{2}})$.

3.  $\sf{KZ}(\Delta_\nu(\phi)) = \phi_\zeta$.
:::

## 

As preparation for the proofs of Corollary [\[cor:periodic\]](#cor:periodic){reference-type="ref" reference="cor:periodic"} and Theorem [\[thm:slopes\]](#thm:slopes){reference-type="ref" reference="thm:slopes"}, we introduce some subsets of $\bb{Q}$ depending on $\nu$. It will be convenient to write $\{d_i\}_{i \in I(W)}$ for the multiset of invariant degrees of $W$. For any slope $\nu\in \bb{C}$, let $$\begin{aligned}
I_\nu(W) = \{i \in I(W) : \nu\in \tfrac{1}{d_i}\bb{Z}\}.
\end{aligned}$$ Concretely, if $n$ is the denominator of $\nu$ in lowest terms, then $I_\nu(W)$ is the set of indices $i$ such that $n$ divides the invariant degree $d_i$.

::: df
If $\nu\in \bb{Q}$ and $\zeta = e^{2\pi i\nu}$, then we say that $\nu$ is:

1.  A **singular slope** iff $|I_\nu(W)| \geq 1$.

2.  A **regular slope** iff $W$ contains a $\zeta$-regular element.

3.  A **regular elliptic slope** iff $W$ contains a $\zeta$-regular element $w$ such that $\bb{V}^w = 0$. (Recall that we assume $\bb{V}^W = 0$.)

4.  A **cuspidal slope** iff $|I_\nu(W)| = 1$.

We say that an integer $n > 0$ is a **singular number**, etc., iff it is the denominator in lowest terms of a singular slope, etc.
:::

::: lem
[]{#lem:implication label="lem:implication"} There is a chain of implications: $$\begin{aligned}
\text{cuspidal}
\implies \text{regular elliptic}
\implies \text{regular}
\implies \text{singular}.
\end{aligned}$$
:::

::: proof
*Proof.* It is tautological that regular elliptic implies regular. That regular implies singular follows from [@springer_1974 Thm. 4.2(iii)]. That cuspidal implies regular elliptic is [@be Rem. 3.28]. ◻
:::

::: ex
In type $A_r$, the invariant degrees are $2, 3, 4, \ldots, r + 1$. An integer is regular if and only if it is a divisor of either $r$ or $r + 1$ [@springer_1974 §5.1]. The only regular elliptic number is the Coxeter number $r + 1$ [@vv Ex. 1.1.2].
:::

::: ex
In type $BC_r$, the invariant degrees are $2, 4, 6, \ldots, 2r$. An integer is regular, *resp.* regular elliptic, if and only if it is a divisor of $2r$ [@springer_1974 §5.2], *resp.* an even divisor of $2r$ [@vv Ex. 1.1.2]. To demonstrate: In type $BC_5$:

-   The singular numbers are $1, 2, 3, 4, 5, 6, 8, 10$.

-   The regular numbers are $1, 2, 5, 10$.

-   The regular elliptic numbers are $2, 10$.

-   The only cuspidal number is $10$, the Coxeter number.

This is a minimal example where each implication in Lemma [\[lem:implication\]](#lem:implication){reference-type="ref" reference="lem:implication"} is strict.
:::

Throughout the rest of this section, we assume $\nu\in \bb{Q}$ and set $\zeta^{\frac{1}{2}} = e^{\pi i\nu}$. We form the virtual $\bb{D}_\nu^\mathit{rat}$-module $$\begin{aligned}
\Omega_\nu= \bigoplus_{\phi \in \hat{W}} \mathrm{Deg}_\phi(e^{2\pi i\nu})\Delta_\nu(\phi).
\end{aligned}$$ We can immediately prove part (1) of Theorem [\[thm:slopes\]](#thm:slopes){reference-type="ref" reference="thm:slopes"}, stating that $L_\nu(1)$ occurs in $\Omega_\nu$ with multiplicity one. Indeed, we have $D_1(\bm{q}) = 1$, and for any $\nu$, the only Verma module that contains $L_\nu(1)$ as a constituent is $\Delta_\nu(1)$.

## Singular Slopes

We prove part (2) of Theorem [\[thm:slopes\]](#thm:slopes){reference-type="ref" reference="thm:slopes"}, stating that if $\nu$ is singular, then $\Omega_\nu\in \sf{O}_\nu^\tor$.

::: lem
[]{#lem:principal-series label="lem:principal-series"} We have $$\begin{aligned}
\sum_{\phi \in \hat{W}}
D_\phi(\bm{q})\phi_{\bm{q}}(\sigma_w) = \left\{\begin{array}{ll}
\bm{s}(1_{\bm{q}})  &w = 1\\
0               &w \neq 1
\end{array}\right.
\end{aligned}$$ in $\bb{Q}_W(\bm{q}^{\frac{1}{2}})$.
:::

::: proof
*Proof.* If $W \simeq W_1 \times W_2$, then $D_{\phi_1 \times \phi_2}(\bm{q}) = D_{\phi_1}(\bm{q}) \cdot D_{\phi_2}(\bm{q})$ for all $\phi_i \in \hat{W}_i$. So we can assume that $W$ is irreducible. After checking the non-crystallographic types by hand, we can further assume that $W$ is crystallographic.

Henceforth, we will use the notations and hypotheses of Section [\[sec:dl\]](#sec:dl){reference-type="ref" reference="sec:dl"}. Recall that by [\[eq:double-centralizer\]](#eq:double-centralizer){reference-type="eqref" reference="eq:double-centralizer"}, we have $$\begin{aligned}
R_1 \simeq \bigoplus_{\phi \in \hat{W}}
V_{\phi, q}^{\oplus \mathrm{Deg}_\phi(q)}
\end{aligned}$$ as $H_W(q^{\frac{1}{2}})$-modules, where $V_{\phi, q}$ is a free $H_W(q^{\frac{1}{2}})$-module that admits the character $\phi_q$. From [\[eq:hecke-operator\]](#eq:hecke-operator){reference-type="eqref" reference="eq:hecke-operator"}, we deduce that:

1.  $\sigma_1$ acts on $R_1$ by the identity operator. Its trace is $|\cal{B}^F|$.

2.  If $w \neq 1$, then $\sigma_w$ acts on $R_1$ by an operator with zeros along the diagonal.

Since $|\cal{B}^F| = \bm{s}(1_{\bm{q}})|_{\bm{q}= q}$, we are done. ◻
:::

By Theorem [\[thm:ggor\]](#thm:ggor){reference-type="ref" reference="thm:ggor"}(1), it remains to show that the $H_W(\zeta^{\frac{1}{2}})$-module $\sf{KZ}(\Omega_\nu)$ is the zero module. By Theorem [\[thm:ggor\]](#thm:ggor){reference-type="ref" reference="thm:ggor"}(3), we have $$\begin{aligned}
\sf{KZ}(\Omega_\nu) = \sum_{\phi \in \hat{W}}
\mathrm{Deg}_\phi(\zeta)\phi_\zeta.
\end{aligned}$$ This coincides with the image of the virtual $H_W(\bm{q}^{\frac{1}{2}})$-module $\sum_\phi \mathrm{Deg}_\phi(\bm{q})\phi_{\bm{q}}$ under the decomposition map from §[\[subsec:cyclotomic\]](#subsec:cyclotomic){reference-type="ref" reference="subsec:cyclotomic"}. So by Lemma [\[lem:principal-series\]](#lem:principal-series){reference-type="ref" reference="lem:principal-series"}, it remains to show $$\begin{aligned}
\bm{s}(1_{\bm{q}})|_{\bm{q}^{1/2} = \zeta^{1/2}} = 0.
\end{aligned}$$ This follows from the Bott--Solomon formula [@solomon] $$\begin{aligned}
\label{eq:bott-solomon}
\bm{s}(1_{\bm{q}}) = \prod_{i \in I(W)} 
\frac{1 - \bm{q}^{d_i}}{1 - \bm{q}}
\end{aligned}$$ together with the definition of singular slope.

## Regular Slopes

We prove Corollary [\[cor:periodic\]](#cor:periodic){reference-type="ref" reference="cor:periodic"}, stating that if $\beta$ is periodic of slope $\nu$, then $[\Omega_\nu] = (\bm{q}^{\frac{1}{2}})^{r - |\beta|} \cdot \langle{\beta}\rangle_{\bm{q}}^0$. On the one hand, $$\begin{aligned}
\begin{split}
(-\bm{q}^{-\frac{1}{2}})^{|\beta|} \langle{\beta}\rangle_{\bm{q}}^0
&=  
    \langle{\beta}\rangle_{\bm{q}} \cdot \varepsilon [\Sym(\bb{V})]_{\bm{q}}\\
&=  
    \varepsilon \sum_{\phi \in \hat{W}}
    {\bm{q}^{\nu\bb{c}(\phi)}} 
    \mathrm{Deg}_\phi(\zeta) \phi \cdot [\Sym(\bb{V})]_{\bm{q}}
\end{split}
\end{aligned}$$ by Theorems [\[thm:decat\]](#thm:decat){reference-type="ref" reference="thm:decat"} and [\[thm:periodic\]](#thm:periodic){reference-type="ref" reference="thm:periodic"}. On the other hand, $$\begin{aligned}
\begin{split}
\sum_{\phi \in \hat{W}}
\mathrm{Deg}_\phi(\zeta) [\Delta_\nu(\phi)]_{\bm{q}}
&=  \bm{q}^{\frac{r}{2}}
    \sum_{\phi \in \hat{W}}
    {\bm{q}^{-\nu\bb{c}(\phi)}}
    \mathrm{Deg}_\phi(\zeta)
    \phi \cdot [\Sym(\bb{V})]_{\bm{q}}\\
&=  \bm{q}^{\frac{r}{2}}\varepsilon
    \sum_{\phi \in \hat{W}}
    {\bm{q}^{\nu\bb{c}(\phi)}}
    \mathrm{Deg}_{\varepsilon\phi}(\zeta)
    \phi \cdot [\Sym(\bb{V})]_{\bm{q}}
\end{split}
\end{aligned}$$ by [\[eq:verma\]](#eq:verma){reference-type="eqref" reference="eq:verma"} and the identity $\bb{c}(\varepsilon\phi) = -\bb{c}(\phi)$. Since $|\beta| = \nu|\pi|$, it remains to check:

::: lem
If $\nu\in \bb{Q}$ is a regular slope and $\zeta = e^{2\pi i\nu}$, then $$\begin{aligned}
\mathrm{Deg}_{\varepsilon\psi}(\zeta) = (-1)^{\nu|\pi|} \mathrm{Deg}_\psi(\zeta)
\end{aligned}$$ for all $\psi \in \hat{W}$.
:::

::: proof
*Proof.* Pick a $\zeta$-regular element $w \in W$. By the discussion in Section [\[sec:periodic\]](#sec:periodic){reference-type="ref" reference="sec:periodic"} and Lemma-Postulate [\[lempost:fourier\]](#lempost:fourier){reference-type="ref" reference="lempost:fourier"}(3), $$\begin{aligned}
\begin{split}
\mathrm{Deg}_{\varepsilon\psi}(\zeta)
&=  \sum_{\phi \in \hat{W}}
    {\{\phi, \varepsilon\psi\}}
    \phi(w)\\
&=  \sum_{\phi \in \hat{W}}
    {\{\phi, \psi\}}
    (\varepsilon\phi)(w)\\
&=  \varepsilon(w) \mathrm{Deg}_\psi(\zeta).
\end{split}
\end{aligned}$$ Finally, $\varepsilon(w) = (-1)^{\nu|\pi|}$ because $|w| = |\sigma_w| = (\nu- \lfloor \nu\rfloor)|\pi|$. ◻
:::

## Regular Elliptic Slopes

We prove part (3) of Theorem [\[thm:slopes\]](#thm:slopes){reference-type="ref" reference="thm:slopes"}, stating that if $\nu$ is regular elliptic, $\nu> 0$, and $W$ is a Weyl group, then $[\Omega_\nu]_{\bm{q}} \in R(W)[\bm{q}^{\pm\frac{1}{2}}]$.

Write $\nu= \frac{m}{n}$, where $m, n > 0$. Since $\frac{1}{n}$ is also a regular elliptic slope, we can pick a $e^{\frac{2\pi i}{n}}$-regular element $w \in W$ such that $\bb{V}^w = 0$. By Proposition [\[prop:broue-michel\]](#prop:broue-michel){reference-type="ref" reference="prop:broue-michel"}, $\sigma_w^m$ is periodic of slope $\nu$, so by Corollary [\[cor:periodic\]](#cor:periodic){reference-type="ref" reference="cor:periodic"}, $$\begin{aligned}
_{\bm{q}}
\in \langle{\sigma_w}\rangle_{\bm{q}}^0 \cdot R(W)[\bm{q}^{\pm\frac{1}{2}}].
\end{aligned}$$ But $W$ is a Weyl group, so by Theorem [\[thm:pole\]](#thm:pole){reference-type="ref" reference="thm:pole"}, the condition $\bb{V}^w = 0$ implies that $\langle{\sigma_w}\rangle_{\bm{q}}^0 \in R(W)[\bm{q}]$.

## Cuspidal Slopes

We prove part (4) of Theorem [\[thm:slopes\]](#thm:slopes){reference-type="ref" reference="thm:slopes"}, stating that if $\nu$ is cuspidal and positive, then $$\begin{aligned}
{[\Omega_\nu]_{\bm{q}}}
=   \sum_{\psi \in \hat{W}_1}
    {[L_\nu(\psi)]_{\bm{q}}},
\end{aligned}$$ where $\hat{W}_1 \subseteq \hat{W}$ is the set of elements of greatest $\bb{a}$-value within their $\zeta$-blocks, among the $\zeta$-blocks of $H_W$ of defect $1$ in the sense of §[\[subsec:cyclotomic\]](#subsec:cyclotomic){reference-type="ref" reference="subsec:cyclotomic"}.

::: lem
[]{#lem:defect-invariants-principal label="lem:defect-invariants-principal"} If $\zeta^{\frac{1}{2}} = e^{\pi i\nu}$, then the $\zeta$-defect of the principal $\zeta$-block of $H_W(\bm{q}^{\frac{1}{2}})$ equals $|I_\nu(W)|$.
:::

::: proof
*Proof.* The Bott--Solomon formula [\[eq:bott-solomon\]](#eq:bott-solomon){reference-type="eqref" reference="eq:bott-solomon"} can be rewritten $$\begin{aligned}
\bm{s}(1_{\bm{q}}) = \prod_{n \geq 1}
\Phi_n(\bm{q})^{|\{i \in I(W)\,:\,\text{$n$ divides $d_i$}\}|},
\end{aligned}$$ where $\Phi_n$ is the minimal polynomial of $e^{\frac{2\pi i}{n}}$ over $\bb{Q}_W$. ◻
:::

::: lem
[]{#lem:defect-invariants label="lem:defect-invariants"} The $\zeta$-defect of any $\zeta$-block of $H_W(\bm{q}^{\frac{1}{2}})$ is bounded above by $I_\nu(W)$. Equality holds if and only if $\mathrm{Deg}_\phi(\zeta) \neq 0$. Moreover, if $|I_\nu(W)| \leq 1$, then there are two kinds of blocks:

1.  Any block of defect $0$ is a singleton. For $\phi$ in such a block, $\mathrm{Deg}_\phi(\zeta) = 0$.

2.  Any block of defect $1$ is a line of characters ordered by $\bb{a}$-value. If $$\begin{aligned}
            \{\phi_0 > \phi_1 > \cdots > \phi_{n - 1}\}
            
    \end{aligned}$$ is such a block, then $\mathrm{Deg}_{\phi_k}(\zeta) = (-1)^k$ for all $k$.
:::

::: proof
*Proof.* The only claim that does not follow from Theorem [\[thm:geck\]](#thm:geck){reference-type="ref" reference="thm:geck"} and Lemma [\[lem:defect-invariants-principal\]](#lem:defect-invariants-principal){reference-type="ref" reference="lem:defect-invariants-principal"} is the claim about generic degrees in case (2). Recall that, by definition, $$\begin{aligned}
\mathrm{Deg}_{\phi_k}(\zeta) 
=
    \left.\frac{\bm{s}(1_{\bm{q}})}{\bm{s}(\phi_{k, \bm{q}})}\right|_{\bm{q}^{1/2} \to \zeta^{1/2}}.
\end{aligned}$$ By work of Broué, such ratios of Schur elements at roots of unity are Morita invariants of the block ideal [@broue §3.7]. (Strictly speaking, Broué worked with group algebras, not Iwahori--Hecke algebras, but see the footnote on [@cm 286].) Thus, by Theorem [\[thm:geck\]](#thm:geck){reference-type="ref" reference="thm:geck"}(2), these ratios match the corresponding ratios for the Brauer tree algebra of type $A_{n - 1}$. In this way, we reduce to the setting where $W = S_n$ and $\nu= \frac{1}{n}$. Here, we have $\phi_k = \mathop{\mathrm{\text{$\Lambda$}}}^k(\bb{V})$, so it remains to show that $$\begin{aligned}
\mathrm{Deg}_{\mathop{\mathrm{\text{$\Lambda$}}}^k(\bb{V})}(e^{\frac{2\pi i}{n}}) = (-1)^k.
\end{aligned}$$ Let $w$ be an $e^{\frac{2\pi i}{n}}$-regular element of $W$. By [@jones Rem. 3.7], the right-hand side above equals $\tr(w \mid \mathop{\mathrm{\text{$\Lambda$}}}^k(V))$. By Lemma-Postulate [\[lempost:fourier\]](#lempost:fourier){reference-type="ref" reference="lempost:fourier"}(2) and Theorem [\[thm:fake-deg\]](#thm:fake-deg){reference-type="ref" reference="thm:fake-deg"}, the left-hand side also equals $\tr(w \mid \mathop{\mathrm{\text{$\Lambda$}}}^k(V))$. ◻
:::

We return to the proof of Theorem [\[thm:slopes\]](#thm:slopes){reference-type="ref" reference="thm:slopes"}(5). Since $\nu$ is cuspidal, Theorem [\[thm:slopes\]](#thm:slopes){reference-type="ref" reference="thm:slopes"}(3) and Lemma [\[lem:defect-invariants\]](#lem:defect-invariants){reference-type="ref" reference="lem:defect-invariants"} together imply: $$\begin{aligned}
_{\bm{q}} 
=
    \sum_{\Gamma = \{\phi_k^\Gamma\}_k} 
    \sum_k
    (-1)^k
    [\Delta_\nu(\phi_k^\Gamma)]_{\bm{q}},
\end{aligned}$$ where the outer sum runs over $\zeta$-blocks of $H_W(\bm{q}^{\frac{1}{2}})$ of defect $1$. To conclude, we claim that the inner sum on the right-hand side simplifies to $[L_\nu(\phi_0^\Gamma)]_{\bm{q}}$, where $\phi_0^\Gamma$ is the element of greatest $\bb{a}$-value in the block $\Gamma$. Indeed, this follows from the theorem below, itself a corollary of Theorem [\[thm:ggor\]](#thm:ggor){reference-type="ref" reference="thm:ggor"}(2).

::: thm
[]{#thm:bgg label="thm:bgg"} Suppose that $\{\phi_0 > \phi_1 > \cdots > \phi_{n - 1}\}$ is a $\zeta$-block of $H_W(\bm{q}^{\frac{1}{2}})$, ordered by $\bb{a}$-value. Then, in $\sf{O}_\nu$, there is a "Bernstein--Gelfand--Gelfand" resolution of $L_\nu(\phi_0)$ of the form $$\begin{aligned}
\Delta_\nu(\phi_{n - 1}) \to \cdots \to \Delta_\nu(\phi_1) \to \Delta_\nu(\phi_0) \to L_\nu(\phi_0) \to 0.
\end{aligned}$$ In particular, we have $$\begin{aligned}
_{\bm{q}} = \sum_{0 \leq k \leq n - 1} {(-1)^k} [\Delta_\nu(\phi_k)]_{\bm{q}}
\end{aligned}$$ in $R(W)[\![\bm{q}]\!]$.
:::

::: rem
We believe that the first appearance of this theorem in the literature is [@rouquier_2008 Thm. 5.15]. The type $A$ case was used much earlier, in [@beg_imrn].
:::

## Cuspidal Slopes, *cont.*

We prove Corollary [\[cor:cuspidal\]](#cor:cuspidal){reference-type="ref" reference="cor:cuspidal"}.

There are only two cases where $W$ is an irreducible Coxeter group, $\nu$ is a cuspidal slope, and there is a $\zeta$-block of $H_W(\bm{q}^{\frac{1}{2}})$ of defect $1$ besides the principal block. Namely, $W$ must be of type $E_8$ or type $H_4$ and the denominator of $\nu$ in lowest terms must be $15$.

In these cases, there is one other $\zeta$-block of defect $1$ and its element of greatest $\bb{a}$-value is the character of $\bb{V}$, assuming as before that $\bb{V}^W = 0$. We refer to these as the two **exceptional** cases for $(W, \nu)$. Parts (3)-(4) of Theorem [\[thm:slopes\]](#thm:slopes){reference-type="ref" reference="thm:slopes"} now imply the following stronger form of Corollary [\[cor:cuspidal\]](#cor:cuspidal){reference-type="ref" reference="cor:cuspidal"}:

::: cor
If $W$ is irreducible and $\nu$ is cuspidal, then: $$\begin{aligned}
\label{eq:cuspidal}
[\Omega_\nu]_{\bm{q}} 
= 
    \left\{\begin{array}{ll}
    {[L_\nu(1)]_{\bm{q}} + [L_\nu(\bb{V})]_{\bm{q}}}
        &\text{$(W, \nu)$ is exceptional}\\
    {[L_\nu(1)]_{\bm{q}}}
        &\text{else}
    \end{array}\right.
\end{aligned}$$ in $R(W)[\bm{q}]$. In particular, the right-hand side is finite-dimensional.
:::

::: rem
This statement also recovers the observation of Bezrukavnikov--Etingof [@be Rem. 3.31] that for irreducible $W$ and cuspidal $\nu$, the only finite-dimensional simple $\bb{D}_\nu^\mathit{rat}$-modules are those appearing on the right-hand side of [\[eq:cuspidal\]](#eq:cuspidal){reference-type="eqref" reference="eq:cuspidal"}.
:::

::: rem
If $W \simeq W_1 \times W_2$ and $\bb{V} \simeq \bb{V}_1 \oplus \bb{V}_2$, such that $\bb{V}_i$ is a realization of $W_i$ for $i = 1, 2$, then:

-   $|I_\nu(W)| = |I_\nu(W_1)| + |I_\nu(W_2)|$, where the right-hand side is defined in terms of $\bb{V}_1$ and $\bb{V}_2$ rather than $\bb{V}$.

-   Category $\sf{O}$ for the rational Cherednik algebra of $W$ is the tensor product of the corresponding categories for $W_1$ and $W_2$.

So the above result can be generalized to any pair $(W, \nu)$ such that $\nu$ is cuspidal with respect to each irredcible factor of $W$.
:::

## 

To conclude this section, we explain how to deduce [@gors Thm. 1.1] from Corollaries [\[cor:cuspidal\]](#cor:cuspidal){reference-type="ref" reference="cor:cuspidal"} and [\[cor:homfly\]](#cor:homfly){reference-type="ref" reference="cor:homfly"}.

For $W = S_n$, we have $r = n - 1$ and $|\pi| = n(n - 1)$. Let $s_i \in S_n$ be the transposition $(i~i + 1)$. Then the (positive) $(m, n)$ torus knot is the link closure of $$\begin{aligned}
\beta = (\sigma_{s_1} \cdots \sigma_{s_{n - 1}})^m \in \mathit{Br}_W^+,
\end{aligned}$$ a periodic braid of slope $\frac{m}{n}$. Since $n$ is the Coxeter number of $S_n$, it is a cuspidal number for $S_n$. Corollary [\[cor:cuspidal\]](#cor:cuspidal){reference-type="ref" reference="cor:cuspidal"} gives $$\begin{aligned}
\begin{split}
{[L_\nu(1)]_{\bm{q}}}
    = {[\Omega_\nu]_{\bm{q}}}
    &= (\bm{q}^{\frac{1}{2}})^{r - |\beta|} \cdot \langle{\beta}\rangle_{\bm{q}}^0.
\end{split}
\end{aligned}$$ Since $|\beta| - n + 1 = \frac{m}{n}|\pi| - (n - 1) = (m - 1)(n - 1)$, Corollary [\[cor:homfly\]](#cor:homfly){reference-type="ref" reference="cor:homfly"} gives $$\begin{aligned}
{[\hat{\beta}]_{a, \bm{q}}}
=   a^{(m - 1)(n - 1)}
    \sum_{0 \leq i \leq n - 1}
    {(-a^2)^i}
    (\mathop{\mathrm{\text{$\Lambda$}}}^i(\bb{V}), {[L_\nu(1)]_{\bm{q}}})_W.
\end{aligned}$$ This is [@gors Thm. 1.1].
