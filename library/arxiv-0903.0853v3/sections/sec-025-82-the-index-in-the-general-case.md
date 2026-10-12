---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis"
section_id: sec-025-82-the-index-in-the-general-case
section_title: "The index in the general case"
section_number: 8.2
pages: 40-51
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.978
---
Generally speaking, there is no simple formula for the dimensions of the kernel and cokernel of a $q$-difference operator $P$. However, if $P$ has integral slopes[^1], we can factor it into operators of degree $1$, and then use proposition [\[prop:indices\]](#prop:indices){reference-type="ref" reference="prop:indices"} and linear algebra to deduce:

1.  The ${\mathbf C}$-linear map $P: f \mapsto P.f$ from $K$ to itself has an index, that is finite dimensional kernel and cokernel.

2.  The index of $P$, that is the integer $\chi(P) := \dim \text{Ker~}P - \dim \text{Coker~} P$ is the sum of indices of factors of $P$.

Note that $\chi(P)$ is the Euler-Poincaré characteristic of the complex of solutions of $P$.

::: coro
Let $P$ be an operator of order $n$ and pure of slope $\mu \neq 0$.\
(i) In the formal case, $\dim \text{Ker~}P = \dim \text{Coker~} P = 0$.\
(ii) In the convergent case $\dim \text{Ker~}P = 0$ and $\dim \text{Coker~} P = n \max(0,\mu)$.
:::

::: proof
*Proof.* If $\mu \in {\mathbf Z}$, all the factors of $P$ have the form $(z^{\mu} \sigma_q-c).u$. If $\mu \neq 0$, they are all bijective in the formal case, whence the first statement. They are also all injective in the convergent case, and onto if $\mu < 0$, whence the second statement in this case. If $\mu > 0$, they all have index $\mu$ (in the convergent case), whence the second statement in this case by additivity of the index.\
The case of an arbitrary slope is easily reduced to this case by ramification. ◻
:::

By similar arguments:

::: coro
Let $P$ be an operator pure of slope $0$. Then, the index of $P$ (in the formal or convergent case) is $0$.
:::

Now, using the additivity of the index:

::: coro
The index of an arbitrary operator $P$ is $0$ in the formal case and $- \sum\limits_{\mu > 0} r_{P}(\mu) \mu$ in the convergent case.
:::

::: coro
Let $P \in {{\mathcal{D}}_{q}}$ be an analytic $q$-difference operator. The index of $P$ acting as a ${\mathbf C}$-linear endomorphism of ${{\mathbf C}((z))}/{{\mathbf C}(\{z\})}$ is equal to $\sum\limits_{\mu > 0} r_{P}(\mu) \mu$.
:::

Of course, $r_{P}$ denotes here the Newton function of $P$ introduced in subsection [\[subsection:Newtonpolygon\]](#subsection:Newtonpolygon){reference-type="ref" reference="subsection:Newtonpolygon"}.

### Irregularity and the dimension of ${\mathcal{F}}(P_{1},\ldots,P_{k})$ {#subsection:algebraicirregularity}

The following definition is inspired by that of [@Ma3].

::: defi
[]{#defi:irregularity label="defi:irregularity"} The *irregularity* of a $q$-difference operator $P$, resp. of $q$-difference module $M$, is defined by the formulas: []{#not33 label="not33"} $$\text{Irr~}(P) := \sum\limits_{\mu > 0} r_{P}(\mu) \mu, \quad
\text{Irr~}(M) := \sum\limits_{\mu > 0} r_{M}(\mu) \mu.$$
:::

Graphically, this is the height of the right part of the Newton polygon, from the bottom to the upper right end. It is clearly a formal invariant. From its interpretation as an index in ${{\mathbf C}((z))}/{{\mathbf C}(\{z\})}$, the irregularity of operators is additive with respect to the product. From theorem [\[theo:Newtonpolygon\]](#theo:Newtonpolygon){reference-type="ref" reference="theo:Newtonpolygon"}, the irregularity of modules is additive with respect to exact sequences. Moreover, with the notations of [\[theo:slopefiltration\]](#theo:slopefiltration){reference-type="ref" reference="theo:slopefiltration"}, writing $$M^{>0} := M/M_{\leq 0}$$ the "positive part" of $M$, one has: $$\text{Irr~}(M) = \text{Irr~}(M^{>0}).$$

[]{#not34 label="not34"} Write $M_{0} := P_{1} \oplus \cdots \oplus P_{k}$. Then the "internal End" $E := \underline{\text{End}}(M_{0}) = M_{0}^{\vee} \otimes M_{0}$ of this module (subsection [\[subsection:generalitiesdiffmods\]](#subsection:generalitiesdiffmods){reference-type="ref" reference="subsection:generalitiesdiffmods"}) has as Newton function: $$r_{E}(\mu) = \sum_{\mu_{j} - \mu_{i} = \mu} r_{i} r_{j}.$$ (This follows from theorem [\[theo:Newtonpolygon\]](#theo:Newtonpolygon){reference-type="ref" reference="theo:Newtonpolygon"}.) From theorem [\[theo:schemadesmodules\]](#theo:schemadesmodules){reference-type="ref" reference="theo:schemadesmodules"} and definition [\[defi:irregularity\]](#defi:irregularity){reference-type="ref" reference="defi:irregularity"}, we therefore get the equality: $$\dim {\mathcal{F}}(P_{1},\ldots,P_{k}) = 
\text{Irr~} \left(\underline{\text{End}}(M_{0})\right).$$ In subsection [\[subsection:sheaftheoreticirregularity\]](#subsection:sheaftheoreticirregularity){reference-type="ref" reference="subsection:sheaftheoreticirregularity"}, we shall give a sheaf theoretical interpretation of this formula.

## Explicit description of ${\mathcal{F}}(P_{1},\ldots,P_{k})$ in the case of integral slopes {#section:explicitdescription}

***FROM NOW ON, WE ASSUME THAT THE SLOPES ARE INTEGRAL:*** $\mu_{1},\ldots,\mu_{k} \in {\mathbf Z}$.\
It is then possible to make the results of sections [\[section:isoformalclasses\]](#section:isoformalclasses){reference-type="ref" reference="section:isoformalclasses"} and [\[section:indextheorems\]](#section:indextheorems){reference-type="ref" reference="section:indextheorems"} more algorithmic by using the matricial description of paragraph [\[subsection:matricialdescriptionofF(P1,\...,Pk)\]](#subsection:matricialdescriptionofF(P1,...,Pk)){reference-type="ref" reference="subsection:matricialdescriptionofF(P1,...,Pk)"}. Indeed, as explained in paragraph [\[subsubsection:integralslopes\]](#subsubsection:integralslopes){reference-type="ref" reference="subsubsection:integralslopes"}, our construction of normal forms and of explicit Stokes operators depends on the normal form [\[eqn:formestandardtriangulaireentiere\]](#eqn:formestandardtriangulaireentiere){reference-type="eqref" reference="eqn:formestandardtriangulaireentiere"} given herebelow for pure modules.\
For $i = 1,\ldots,k$, we thus write $P_{i} = ({{\mathbf C}(\{z\})}^{r_{i}},\Phi_{z^{\mu_{i}} A_{i}})$, with $A_{i} \in {\text{GL}}_{r_{i}}({\mathbf C})$. Then, putting $n := r_{1} + \cdots + r_{k}$, we have $M_{0} := P_{1} \oplus \cdots \oplus P_{k} = (K^{n},\Phi_{A_{0}})$, with $A_{0}$ as in equation [\[eqn:formestandarddiagonale\]](#eqn:formestandarddiagonale){reference-type="eqref" reference="eqn:formestandarddiagonale"} page from paragraph [\[subsection:matricialdescriptionofF(P1,\...,Pk)\]](#subsection:matricialdescriptionofF(P1,...,Pk)){reference-type="ref" reference="subsection:matricialdescriptionofF(P1,...,Pk)"}: $$\label{eqn:formestandarddiagonaleentiere}
A_{0} := \begin{pmatrix}
z^{\mu_{1}} A_{1}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & 0 & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & z^{\mu_{k}} A_{k}    
\end{pmatrix}.$$ Any class in ${\mathcal{F}}(P_{1},\ldots,P_{k})$ can be represented by a module []{#not35 label="not35"} $M_{U} := (K^{n},\Phi_{A_{U}})$ for some $U := (U_{i,j})_{1 \leq i < j \leq k} \in 
\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$, with, $A_{U}$ as in equation ([\[eqn:formestandardtriangulaire\]](#eqn:formestandardtriangulaire){reference-type="ref" reference="eqn:formestandardtriangulaire"}): $$\label{eqn:formestandardtriangulaireentiere}
A_{U} := \begin{pmatrix}
z^{\mu_{1}} A_{1} & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & U_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & z^{\mu_{k}} A_{k} 
\end{pmatrix},$$ and $M_{U},M_{V}$ represent the same class if, and only if, the equation $(\sigma_qF) A_{V} = A_{U} F$ can be solved with $F \in {\mathfrak{G}}({{\mathbf C}(\{z\})})$. Such an $F$ is then unique.

### Analytic classification with $2$ integral slopes {#subsection:twointegralslopes}

From the results of [\[subsection:extensionsofqdifferencemodules\]](#subsection:extensionsofqdifferencemodules){reference-type="ref" reference="subsection:extensionsofqdifferencemodules"}, we get the following result for the case of two slopes. Here, and after, we write, for $\mu < \nu \in {\mathbf Z}$: $$\label{not36}
K_{\mu,\nu} := \sum_{i=0}^{\nu - \mu - 1} {\mathbf C}z^{i} \text{~or, at will:~}
K_{\mu,\nu} := \sum_{i=\mu}^{\nu - 1} {\mathbf C}z^{i}.$$ (The second choice is motivated by good tensor properties, see for instance [@RS1].) Then, for $r,s \in {\mathbf N}^{*}$, we denote ${\text{Mat}}_{r,s}(K_{\mu,\nu})$ the space of $r \times s$ matrices with coefficients in $K_{\mu,\nu}$.

::: prop
[]{#prop:espaceadeuxpentes label="prop:espaceadeuxpentes"} Let $U \in {\text{Mat}}_{r_{1},r_{2}}({{\mathbf C}(\{z\})})$. Then, there exists a unique pair: $$\label{not37}
Red(\mu_{1},A_{1},\mu_{2},A_{2},U) := 
(F_{1,2},V) \in {\text{Mat}}_{r_{1},r_{2}}({{\mathbf C}(\{z\})}) \times {\text{Mat}}_{r_{1},r_{2}}(K_{\mu_{1},\mu_{2}})$$ such that: $$(\sigma_qF_{1,2}) z^{\mu_{2}} A_{2} - z^{\mu_{1}} A_{1} F_{1,2} = U - V,$$ that is: $$\begin{pmatrix} I_{r_{1}} & F_{1,2} \\ 0 & I_{r_{2}} \end{pmatrix}:
\begin{pmatrix}
z^{\mu_{1}} A_{1} &  V            \\
0              & z^{\mu_{2}} A_{2} 
\end{pmatrix} \simeq
\begin{pmatrix}
z^{\mu_{1}} A_{1} &  U            \\
0              & z^{\mu_{2}} A_{2} 
\end{pmatrix}.$$
:::

::: proof
*Proof.* Using the reductions of lemma [\[lemm:dimensiondeuxpentes\]](#lemm:dimensiondeuxpentes){reference-type="ref" reference="lemm:dimensiondeuxpentes"}, this is just a rephrasing of lemma [\[lemm:supplementairedeuxpentes\]](#lemm:supplementairedeuxpentes){reference-type="ref" reference="lemm:supplementairedeuxpentes"}. ◻
:::

We consider $V$ as a *polynomial normal form* for the class of $M_{U}$ and $F_{1,2}$ as the corresponding reduction datum. Of course, they depend on the choice of the space of coefficients $K_{\mu_{1},\mu_{2} }$.\

::: exem
[]{#exem:archetypal label="exem:archetypal"} This is the archetypal example (and strongly related to the prototypal example of subsection [\[subsection:prototypal\]](#subsection:prototypal){reference-type="ref" reference="subsection:prototypal"}), from which much of the theory is built. Fix $c \in {\mathbf C}^{*}$. For any $f,u,v \in {{\mathbf C}(\{z\})}$, the isomorphism: $\begin{pmatrix}1 & f \\ 0 & 1 \end{pmatrix}:
\begin{pmatrix} 1 & v \\ 0 & cz \end{pmatrix} \simeq
\begin{pmatrix} 1 & u \\ 0 & cz \end{pmatrix}$ is equivalent to the inhomogeneous $q$-difference equation: $c z \sigma_qf - f = u - v$. Writing $f = \sum f_{n} z^{n}$, etc, we find the conditions: $$c q^{n-1} f_{n-1} - f_{n} = u_{n} - v_{n} \Longleftrightarrow
\dfrac{f_{n-1}}{c^{n-1} q^{(n-1)(n-2)/2}} - \dfrac{f_{n}}{c^{n} q^{n(n-1)/2}} = 
\dfrac{u_{n} - v_{n}}{c^{n} q^{n(n-1)/2}},$$ which admit an analytic solution $f$ if, and only if, ${\mathcal{B}_{q,1}}u(c^{-1}) = {\mathcal{B}_{q,1}}v(c^{-1})$ (recall that the $q$-Borel transform ${\mathcal{B}_{q,1}}$ was defined in definition [\[defi:qBorel\]](#defi:qBorel){reference-type="ref" reference="defi:qBorel"} page ). The analytic class of the module with matrix $\begin{pmatrix} 1 & u \\ 0 & cz \end{pmatrix}$ within the formal class $\begin{pmatrix} 1 & 0 \\ 0 & cz \end{pmatrix}$ is therefore ${\mathcal{B}_{q,1}}u(c^{-1}) \in {\mathbf C}$. Writing $f_{u}$ the unique solution in ${{\mathbf C}(\{z\})}$ of the equation $c z \sigma_qf - f = u - {\mathcal{B}_{q,1}}u(c^{-1})$, we have $Red(0,1,1,c,u) = \bigl(f_{u},{\mathcal{B}_{q,1}}u(c^{-1})\bigr)$.\
Note that equation $c z \sigma_qf - f = u$ always admits a unique formal solution $\hat{f}_{u}$. For instance, for $u \in {\mathbf C}$, we find that $\hat{f}_{u} = - u \text{\tencyr\cyracc Ch}(c z)$, where $\text{\tencyr\cyracc Ch}$ is the Tshakaloff series []{#not38 label="not38"} defined by [\[eqn:Tshakaloff\]](#eqn:Tshakaloff){reference-type="eqref" reference="eqn:Tshakaloff"} page . We infer that, for a general $u \in {{\mathbf C}(\{z\})}$, one has $\hat{f}_{u} = f_{u} - {\mathcal{B}_{q,1}}u(c^{-1}) \text{\tencyr\cyracc Ch}(c z)$.
:::

::: exem
In proposition [\[prop:espaceadeuxpentes\]](#prop:espaceadeuxpentes){reference-type="ref" reference="prop:espaceadeuxpentes"}, we meet the equation $(\sigma_qF_{1,2}) z^{\mu_{2}} A_{2} - z^{\mu_{1}} A_{1} F_{1,2} = U - V$. Here is an explicit resolution that does not go through all the reductions of [\[subsection:extensionsofqdifferencemodules\]](#subsection:extensionsofqdifferencemodules){reference-type="ref" reference="subsection:extensionsofqdifferencemodules"}. We write $X = \sum X_{n} z^{n}$ for $F_{1,2}$ and $Y = \sum Y_{n} z^{n}$ for $U - V$. We have: $$\begin{aligned}
(\sigma_qX) z^{\mu_{2}} A_{2} - z^{\mu_{1}} A_{1} X = Y & \Longleftrightarrow
\forall n ~,~ 
q^{n - \mu_{2}} X_{n - \mu_{2}} A_{2} - A_{1} X_{n - \mu_{1}} = Y_{n} \\
& \Longleftrightarrow
\forall n ~,~ q^{n - d} X_{n - d} A_{2} - A_1 X_{n} = 
Y_{n + \mu_{1}}, \\
& \Longleftrightarrow
\forall n ~,~ q^{n - d} A_{1}^{-1} X_{n - d} A_{2} - X_{n} = 
Z_{n} := A_{1}^{-1} Y_{n + \mu_{1}},
\end{aligned}$$ where we denote $d := \mu_{2} - \mu_{1} \in {\mathbf N}^{*}$ the *level* of the above inhomogeneous equation. (The second equivalence is obtained by a mere translation of indices.) It follows from [@Bezivin], [@RamisGrowth] that, for any analytic $Y$, this has a formal solution of $g$-Gevrey level $d$ (this was defined in paragraph [\[subsection:qGevreylevels\]](#subsection:qGevreylevels){reference-type="ref" reference="subsection:qGevreylevels"} of the general notations, in the introduction); it also follows from *loc.cit* that, if there is a solution of $q$-Gevrey level $d' > d$ (which is a stronger condition), then, there is an analytic solution. To solve our equation, we introduce a $q$-Borel transform of level $d$. This depends on an arbitrary family $(t_{n})_{n \in {\mathbf Z}}$ in ${\mathbf C}^{*}$, subject to the condition: $$\forall n ~,~ t_{n} = q^{n-d} t_{n-d}.$$ For $d = 1$, the natural choice is $t_{n} := q^{n(n-1)/2}$. In general, such a family can be built from Jacobi theta functions as in [@RS1]. At any rate, $t_{n}$ has the order of growth of $q^{n^{2}/2 d}$. The $q$-Borel transform is then defined by: $$\label{not39}
{\mathcal{B}}_{q,d} \left(\sum f_{n} z^{n}\right) := \sum \dfrac{f_{n}}{t_{n}} \xi^{n}.$$ We must also choose $d^{th}$ roots $B_{1},B_{2}$ of $A_{1},A_{2}$. Then, writing ${\mathcal{B}}_{q,d} X = \sum \tilde{X}_{n} z^{n}$, etc, we find the relations: $$\forall n ~,~ 
B_{1}^{-d} \tilde{X}_{n-d} B_{2}^{d} - \tilde{X}_{n} = \tilde{Z}_{n} 
\Longleftrightarrow
\forall n ~,~ B_{1}^{n-d} \tilde{X}_{n-d} B_{2}^{-(n-d)} - 
B_{1}^{n} \tilde{X}_{n}  B_{2}^{-n} = B_{1}^{n} \tilde{Z}_{n} B_{2}^{-n}.$$ Thus, a necessary condition for the existence of an analytic solution $X$ is that, for all $i$ in a set of representatives modulo $d$, one has: $$\sum_{n \equiv i \pmod{d}} B_{1}^{n} \tilde{Z}_{n} B_{2}^{-n} = 0.$$ This provides us with $d$ obstructions in ${\text{Mat}}_{r_{1},r_{2}}({\mathbf C})$ and it is not hard to prove, along the same lines as what has been done, that these form a complete set of invariants. More precisely, the map which sends $U$ to the $d$-uple of matrices $\sum\limits_{n \equiv i \pmod{d}} \dfrac{1}{t_{n}} B_{1}^{n-d} U_{n + \mu_{1}} B_{2}^{-n}$ yields an isomorphism of ${\mathcal{F}}(P_{1},P_{2})$ with ${\text{Mat}}_{r_{1},r_{2}}({\mathbf C})^{d}$. Different choices of the family $(t_{n})$ and the matrices $B_{1},B_{2}$ induce different isomorphisms.
:::

### The Birkhoff-Guenther normal form {#subsection:BGNF}

Going from two slopes to general case rests on the following remark. The functor $M \leadsto M' := M_{\leq \mu_{k-1}}$ induces an onto mapping ${\mathcal{F}}(P_{1},\ldots,P_{k}) \rightarrow {\mathcal{F}}(P_{1},\ldots,P_{k-1})$. The inverse image in ${\mathcal{F}}(P_{1},\ldots,P_{k})$ of the class of $M'$ in ${\mathcal{F}}(P_{1},\ldots,P_{k-1})$ is in natural one-to-one correspondance with the space $\text{Ext}^{1}(P_{k},M')$. The latter is a ${\mathbf C}$-vector space of dimension $\sum\limits_{1 \leq j < k} r_{j} r_{k} (\mu_{k} - \mu_{j})$. This follows from the slope filtration $0 = M_{0} \subset \cdots \subset M_{k-1} = M'$ and the resulting exact sequences, for $1 \leq j < k$: $$0 \rightarrow M_{j-1} \rightarrow M_{j} \rightarrow P_{j} \rightarrow 0
\Longrightarrow$$ $$0 \rightarrow \text{Ext}^{1}(P_{k},M_{j-1}) \rightarrow \text{Ext}^{1}(P_{k},M_{j}) 
\rightarrow \text{Ext}^{1}(P_{k},P_{j}) \rightarrow 0.$$ (Recall that $\text{Hom}(P_{k},P_{j}) = 0$.) Actually, there is a non canonical ${\mathbf C}$-linear isomorphism $\text{Ext}^{1}(P_{k},M') \simeq \bigoplus_{1 \leq j < k} \text{Ext}^{1}(P_{k},P_{j})$. One can go further using the matricial description of paragraph [\[subsection:matricialdescriptionofF(P1,\...,Pk)\]](#subsection:matricialdescriptionofF(P1,...,Pk)){reference-type="ref" reference="subsection:matricialdescriptionofF(P1,...,Pk)"}. We keep the notations recalled at the beginning of subsection [1.1](#subsection:twointegralslopes){reference-type="ref" reference="subsection:twointegralslopes"} and moreover denote []{#not40 label="not40"} $\overline{M_{U}}$ the class in ${\mathcal{F}}(P_{1},\ldots,P_{k})$ of the module $M_{U} := (K^{n},\Phi_{A_{U}})$ for $U := (U_{i,j})_{1 \leq i < j \leq k} \in 
\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$.

::: prop
[]{#prop:kintegralslopesspace label="prop:kintegralslopesspace"} The map $U \mapsto \overline{M_{U}}$ from $\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j} })$ to ${\mathcal{F}}(P_{1},\ldots,P_{k})$ is one-to-one.
:::

::: proof
*Proof.* We already now that the map is onto and the conclusion will follow from the following fact: for all $U \in \prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$, there exists a unique pair $(F,V) \in {\mathfrak{G}}({{\mathbf C}(\{z\})}) \times 
\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j}})$ such that $F[A_{V}] = A_{U}$. Writing $F$ as in equation ([\[eqn:isoplat\]](#eqn:isoplat){reference-type="ref" reference="eqn:isoplat"}) and $V = (V_{i,j})$, this is equivalent to the following system: $$\forall (i,j), 1 \leq i < j \leq k ~,~
V_{i,j} + \sum_{\ell = i+1}^{j-1} (\sigma_qF_{i,\ell}) V_{\ell,j} + 
(\sigma_qF_{i,j}) (z^{\mu_{j}} A_{j}) =
(z^{\mu_{i}} A_{i}) F_{i,j} + \sum_{\ell = i+1}^{j-1} U_{i,\ell} F_{\ell,j} + U_{i,j}.$$ It is understood that an empty sum vanishes: if $(t_{\ell})$ is any sequence, $\sum\limits_{\ell = i+1}^{j-1} t_{\ell} = 0$ when $j = i+1$. Then, $U$ being given, the system is (uniquely) solved by induction on $j - i$ by the following formulas: $$(F_{i,j},V_{i,j}) := Red\left(\mu_{i},A_{i},\mu_{j},A_{j},U_{i,j} +
\sum_{\ell = i+1}^{j-1} U_{i,\ell} F_{\ell,j} - 
\sum_{\ell = i+1}^{j-1} (\sigma_qF_{i,\ell}) V_{\ell,j}\right).$$ ◻
:::

The following is a particular case of theorem [\[theo:schemadesmodules\]](#theo:schemadesmodules){reference-type="ref" reference="theo:schemadesmodules"}, page (itself a particular case of corollary [\[coro:themodulispaceabstract\]](#coro:themodulispaceabstract){reference-type="ref" reference="coro:themodulispaceabstract"}, page ): the only novelty being that, in the case of integral slopes, we obtain an explicit coordinate system.

::: theo
[]{#theo:kintegralslopesspace label="theo:kintegralslopesspace"} The set ${\mathcal{F}}(P_{1},\ldots,P_{k})$ is an affine space of dimension $\sum\limits_{1 \leq i < j \leq k} r_{i} r_{j} (\mu_{j} - \mu_{i})$.
:::

::: proof
*Proof.* This is an immediate consequence of the proposition. ◻
:::

Note that this is the area contained in the lower finite part of the Newton polygon. This result is the natural continuation of a normalisation process found by Birkhoff and Guenther in [@Birkhoff3].

::: defi
[]{#defi:BirkhoffGuenthernormalform label="defi:BirkhoffGuenthernormalform"} A matrix $A_{U}$ such that $U := (U_{i,j})_{1 \leq i < j \leq k} \in 
\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j} })$ will be said to be in *Birkhoff-Guenther normal form*.
:::

Now, using the argument that follows theorem [\[theo:schemadesmodules\]](#theo:schemadesmodules){reference-type="ref" reference="theo:schemadesmodules"}, we draw from corollary [\[coro:themodulispaceabstract\]](#coro:themodulispaceabstract){reference-type="ref" reference="coro:themodulispaceabstract"}:

::: coro
[]{#coro:schemadesmodules label="coro:schemadesmodules"} The components of the matrices $(U_{i,j})_{1 \leq i < j \leq k}$ make up a complete system of coordinates on the space ${\mathcal{F}}(P_{1},\ldots,P_{k})$.
:::

A generalisation of Birkhoff-Guenther normal form to the case of arbitrary slopes has recently been obtained by Virginie Bugeaud [@VB].

### Computational consequences of the Birkhoff-Guenther normal form {#subsection:computnormalform}

Let $A_{0}$ be as in [\[eqn:formestandarddiagonaleentiere\]](#eqn:formestandarddiagonaleentiere){reference-type="eqref" reference="eqn:formestandarddiagonaleentiere"} and $A_{U} = A$ as in [\[eqn:formestandardtriangulaireentiere\]](#eqn:formestandardtriangulaireentiere){reference-type="eqref" reference="eqn:formestandardtriangulaireentiere"}. Looking for $\hat{F} \in {\mathfrak{G}}({{\mathbf C}((z))})$ such that $\hat{F}[A_{0}] = A$ amounts, with notation [\[eqn:isoplat\]](#eqn:isoplat){reference-type="eqref" reference="eqn:isoplat"}, to solving the system: $$\forall (i,j), 1 \leq i < j \leq k ~,~
(\sigma_qF_{i,j}) (z^{\mu_{j}} A_{j}) =
(z^{\mu_{i}} A_{i}) F_{i,j} + \sum_{\ell = i+1}^{j-1} U_{i,\ell} F_{\ell,j} + U_{i,j}.$$ This is triangular in the sense that the equation in $F_{i,j}$ depends on previously found $F_{\ell,j}$ with $\ell > i$.\
Assume that $A$ is in Birkhoff-Guenther normal form (definition [\[defi:BirkhoffGuenthernormalform\]](#defi:BirkhoffGuenthernormalform){reference-type="ref" reference="defi:BirkhoffGuenthernormalform"}). Then we can write $U_{i,j} = z^{\mu_{i}} U'_{i,j}$, where $U'_{i,j}$ has coefficients in ${\mathbf C}[z]$. The previous equation becomes: $$(\sigma_qF_{i,j}) (z^{\mu_{j} - \mu_{i}} A_{j}) =
A_{i} F_{i,j} + \sum_{\ell = i+1}^{j-1} U'_{i,\ell} F_{\ell,j} + U'_{i,j}.$$ Assume by induction that all $F_{\ell,j}$ have coefficients in ${{\mathbf C}[[z]]}$. Then one may write the above equation as: $$F_{i,j} = U'' + z^{\delta} A_{i}^{-1} (\sigma_qF_{i,j}) A_{j},$$ where $U''$ has coefficients in ${{\mathbf C}[[z]]}$ and $\delta \in {\mathbf N}^{*}$. This is a fixpoint equation for an operator that is contracting in the $z$-adic topology of ${{\mathbf C}[[z]]}$ and so it admits a unique formal solution. Therefore we find a unique $\hat{F} \in {\mathfrak{G}}({{\mathbf C}[[z]]})$ such that $\hat{F}[A_{0}] = A$.\
A noteworthy consequence is that the inclusions ${{\mathbf C}\{z\}}\subset {{\mathbf C}(\{z\})}$ and ${{\mathbf C}[[z]]}\subset {{\mathbf C}((z))}$ induce a natural identification: $${\mathfrak{G}}^{A_{0}}({{\mathbf C}[[z]]})/{\mathfrak{G}}({{\mathbf C}\{z\}}) \simeq {\mathfrak{G}}^{A_{0}}({{\mathbf C}((z))})/{\mathfrak{G}}({{\mathbf C}(\{z\})}),$$ and, as a corollary, a bijection: $${\mathfrak{G}}^{A_{0}}({{\mathbf C}[[z]]})/{\mathfrak{G}}({{\mathbf C}\{z\}}) \rightarrow {\mathcal{F}}(P_{1},\ldots,P_{k}).$$

## Interpolation by $q$-Gevrey classes {#section:qGevreyinterpolation}

We shall now extend the previous results to $q$-Gevrey classification. We use here notations from paragraph [\[subsection:qGevreylevels\]](#subsection:qGevreylevels){reference-type="ref" reference="subsection:qGevreylevels"} of the general notations in the introduction.

### $q$-Gevrey extension spaces {#subsection:qGevreyExt}

#### $q$-Gevrey extensions for arbitrary slopes

If one repaces the field ${{\mathbf C}(\{z\})}$ by the field ${{{\mathbf C}((z))}_{q;s}}$ of $q$-Gevrey series of level $s >0$ and ${{\mathcal{D}}_{q}}$ by ${{\mathcal{D}}_{q,s}}:= {{{\mathbf C}((z))}_{q;s}}\langle T,T^{-1} \rangle$, one gets the abelian category ${DiffMod({{{\mathbf C}((z))}_{q;s}},\sigma_q)}$ and the following extension of the results of [\[subsection:extensionsofqdifferencemodules\]](#subsection:extensionsofqdifferencemodules){reference-type="ref" reference="subsection:extensionsofqdifferencemodules"}.

::: prop
[]{#prop:dimensiondeuxpentesqGevrey label="prop:dimensiondeuxpentesqGevrey"} Let $M,N$ be pure modules of ranks $r,s \in {\mathbf N}^{*}$ and slopes $\mu < \nu \in {\mathbf Q}$ in ${DiffMod({{{\mathbf C}((z))}_{q;s}},\sigma_q)}$. Then one has: $$\dim_{{\mathbf C}} \text{Ext}^{1}(M,N) = \begin{cases}
0 \text{~if~} \nu - \mu \geq 1/s, \\
r s (\nu - \mu) \text{~if~} \nu - \mu < 1/s.
\end{cases}$$
:::

::: proof
*Proof.* This follows indeed, by the same arguments as before, from propositions 3.2 and 3.3 of [@Bezivin]. ◻
:::

This remains true in the extreme case that $s = \infty$, since, over the field ${{\mathbf C}((z))}$, the slope filtration splits and $\text{Ext}^{1}(M,N) = 0$; and also in the extreme case that $s = 0$, by theorem [\[theo:dimensiondeuxpentes\]](#theo:dimensiondeuxpentes){reference-type="ref" reference="theo:dimensiondeuxpentes"}. Therefore, the above proposition is an interpolation between the analytic and formal settings.

#### $q$-Gevrey extensions for integral slopes

Here, we extend the results of [1.1](#subsection:twointegralslopes){reference-type="ref" reference="subsection:twointegralslopes"}. If one replaces ${{\mathbf C}(\{z\})}$ by ${{\mathbf C}((z))}$, one gets $V = 0$ in all relations $(F,V) = Red(\mu_{1},A_{1},\mu_{2},A_{2},U)$ and the corresponding space of classes has dimension $0$. The previous algorithm then produces $F = \hat{F}_{U}$ and the "formal normal form" $A_{0}$ of $A$. If one replaces ${{\mathbf C}(\{z\})}$ by ${{{\mathbf C}((z))}_{q;s}}$, one gets $V = 0$ and a matrix $F$ of $g$-Gevrey level $\mu_{2} - \mu_{1}$ if $\mu_{2} - \mu_{1} \geq 1/s$, and the same $Red(\mu_{1},A_{1},\mu_{2},A_{2},U)$ as before otherwise.

### Isoformal $q$-Gevrey classification {#subsection:qGevreymoduli}

#### $q$-Gevrey classification for arbitrary slopes

One can state the moduli problem for $q$-Gevrey classification at order $s$, that is, over the field ${{{\mathbf C}((z))}_{q;s}}$ of $q$-Gevrey series of order $s >0$ (see subsection [2.1](#subsection:qGevreyExt){reference-type="ref" reference="subsection:qGevreyExt"}). From proposition [\[prop:dimensiondeuxpentesqGevrey\]](#prop:dimensiondeuxpentesqGevrey){reference-type="ref" reference="prop:dimensiondeuxpentesqGevrey"}, one gets, by the same argument as before:

::: prop
[]{#prop:schemadesmodulesqGevrey label="prop:schemadesmodulesqGevrey"} Over ${{{\mathbf C}((z))}_{q;s}}$, the functor $F$ is representable and the corresponding affine scheme is an affine space over ${\mathbf C}$ with dimension $\sum\limits_{1 \leq i < j \leq k \atop \mu_{j} - \mu_{i} < 1/s} 
r_{i} r_{j} (\mu_{j} - \mu_{i})$.
:::

This remains true for $s = \infty$ (formal setting, the space of moduli is a point) and for $s = 0$ (analytic setting, this is theorem [\[theo:schemadesmodules\]](#theo:schemadesmodules){reference-type="ref" reference="theo:schemadesmodules"}).

#### $q$-Gevrey classification for integral slopes

We fix $s > 0$ and write for short $q$-Gevrey for $q$-Gevrey of order $s$. Every matrix is $q$-Gevrey equivalent to a matrix $A_{U}$ such that $U_{i,j} = 0$ for $\mu_{j} - \mu_{i} \geq 1/s$. The slopes being assumed to be integral, there is moreover a unique normal form with $U_{i,j} = 0$ for $\mu_{j} - \mu_{i} \geq 1/s$ and $U_{i,j} \in {\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j} })$ for $\mu_{j} - \mu_{i} < 1/s$.

### Another kind of $q$-Gevrey interpolation

A somewhat symmetric problem is to describe the space of analytic classes within a fixed $q$-Gevrey class. This can be done in a similar way. We fix a matrix $A_{U_{0}}$ where $U_{0} \in 
\prod\limits_{1 \leq i < j \leq k}{\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j} })$ is such that $U_{i,j} = 0$ for $\mu_{j} - \mu_{i} \geq 1/s$ (any $q$-Gevrey class contains such a matrix). This characterizes a well defined $q$-Gevrey class and the space of analytic classes within this $q$-Gevrey class is an affine space of dimension $\sum\limits_{1 \leq i < j \leq k \atop \mu_{j} - \mu_{i} \geq 1/s} 
r_{i} r_{j} (\mu_{j} - \mu_{i})$. If the slopes are integral, one can assume that $U_{0}$ is in normal form, *i.e.* each component $U_{i,j}$ such that $\mu_{j} - \mu_{i} < 1/s$ belongs to ${\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j} })$. Then each analytic class admits a unique normal form $A_{U}$ where $U$ is in normal form and its components such that $\mu_{j} - \mu_{i} < 1/s$ are the same as those of $U_{0}$.

# The $q$-analogs of Birkhoff-Malgrange-Sibuya theorems {#chapter:qMalgrangeSibuya}

[^1]: This assumption will be dropped in the four next corollaries.
