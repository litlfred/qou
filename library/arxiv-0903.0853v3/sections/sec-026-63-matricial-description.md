---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-026-63-matricial-description
section_title: "Matricial description"
section_number: 6.3
pages: 32-35
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.95
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:matricialdescriptionofF(P1,...,Pk) label="subsection:matricialdescriptionofF(P1,...,Pk)"}

We now go for a preliminary matricial description, valid without any restriction on the slopes (number or integrity). Details can be found in appendix [\[chapter:ISOGRAD\]](#chapter:ISOGRAD){reference-type="ref" reference="chapter:ISOGRAD"}. From the theorem [\[theo:slopefiltration\]](#theo:slopefiltration){reference-type="ref" reference="theo:slopefiltration"}, we deduce that each analytic $q$-difference module $M$ with $S(M) = \{\mu_{1},\ldots,\mu_{k}\}$, these slopes being indexed in increasing order: $\mu_{1} < \cdots < \mu_{k}$ and having multiplicities $r_{1},\ldots,r_{k} \in {\mathbf N}^{*}$, can be written $M = ({{\mathbf C}(\{z\})}^{n},\Phi_{A})$ with: []{#not28 label="not28"} $$\label{eqn:formestandardtriangulaire}
A = A_{U} := \begin{pmatrix}
B_{1}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & U_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & B_{k}    
\end{pmatrix},$$ where, for $1 \leq i \leq k$, $B_{i} \in {\text{GL}}_{r_{i}}({{\mathbf C}(\{z\})})$ encodes a pure isoclinic module $P_{i} = (K^{r_{i}}, \Phi_{B_{i}})$ of slope $\mu_{i}$ and rank $r_{i}$ and where, for $1 \leq i < j \leq k$, $U_{i,j} \in {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$. Here, $U$ stands short for $(U_{i,j})_{1 \leq i < j \leq k} \in \prod\limits_{1 \leq i < j \leq k}
{\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$. Call $M_{U} = M$ the module thus defined: it is implicitly endowed with an isomorphism from ${\text{gr}}M_{U}$ to $M_{0} := P_{1} \oplus \cdots \oplus P_{k}$, here identified with $(K^{n},\Phi_{A_{0}})$. If moreover the slopes are integral: $S(M) \subset {\mathbf Z}$, then one may take, for $1 \leq i \leq k$, $B_{i} = z^{\mu_{i}} A_{i}$, where $A_{i} \in {\text{GL}}_{r_{i}}({\mathbf C})$.\
Now, a morphism from $M_{U}$ to $M_{V}$ compatible with the graduation (as in definition [\[defi:analyticisoformalclass\]](#defi:analyticisoformalclass){reference-type="ref" reference="defi:analyticisoformalclass"}) is a matrix: $$\label{eqn:isoplat}
F := \begin{pmatrix}
I_{r_{1}}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & F_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & I_{r_{k}}    
\end{pmatrix}, \text{~with~} 
(F_{i,j})_{1 \leq i < j \leq k} \in \prod_{1 \leq i < j \leq k}
{\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})}),$$ such that $(\sigma_qF) A_{U} = B_{U} F$. The corresponding relations for the $F_{i,j},U_{i,j},V_{i,j}$ will be detailed in subsection [\[subsection:BGNF\]](#subsection:BGNF){reference-type="ref" reference="subsection:BGNF"}. Here, we just note that the above form of $F$ characterizes a unipotent algebraic subgroup []{#not29 label="not29"} []{#endroit:introductiondugroupeG label="endroit:introductiondugroupeG"} ${\mathfrak{G}}$ of ${\text{GL}}_{n}$, which is completely determined by the Newton polygon of $M_{0}$. The condition of equivalence of $M_{U}$ and $M_{V}$ reads: []{#not30 label="not30"} $$M_{U} \sim M_{V} \Longleftrightarrow
\exists F \in {\mathfrak{G}}({{\mathbf C}(\{z\})}) ~:\: F[A_{U}] = A_{V}.$$ The set of classes ${\mathcal{F}}(P_{1},\ldots,P_{k})$ may therefore be identified with the quotient of $\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$ by that equivalence relation, *i.e.* by the action of ${\mathfrak{G}}({{\mathbf C}(\{z\})})$.\
For a more formal description, we introduce the block-diagonal part of $A$, *i.e.* the matrix $A_0$ corresponding to the pure module $M_0$: $$\label{eqn:formestandarddiagonale}
A_{0} := \begin{pmatrix}
B_{1}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & 0 & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & B_{k}    
\end{pmatrix},$$ along with the following set: []{#not31 label="not31"} $${\mathfrak{G}}^{A_{0}}({{\mathbf C}((z))}) := 
\{\hat{F} \in {\mathfrak{G}}({{\mathbf C}((z))}) ~ | ~\hat{F}[A_{0}] \in {\text{GL}}_{n}({{\mathbf C}(\{z\})})\}.$$ If $\hat{F} \in {\mathfrak{G}}^{A_{0}}({{\mathbf C}((z))})$ and $F \in {\mathfrak{G}}({{\mathbf C}(\{z\})})$, then $(F \hat{F})[A_{0}] = F\bigl[\hat{F}[A_{0}]\bigr] \in {\text{GL}}_{n}({{\mathbf C}(\{z\})})$, so that $F \hat{F} \in {\mathfrak{G}}^{A_{0}}({{\mathbf C}((z))})$: therefore, the group ${\mathfrak{G}}({{\mathbf C}(\{z\})})$ operates on the set ${\mathfrak{G}}^{A_{0}}({{\mathbf C}((z))})$.

::: prop
[]{#prop:groupeformelsuranalytique label="prop:groupeformelsuranalytique"} The map $\hat{F}\mapsto \hat{F}[A_{0}]$ induces a one-to-one correspondance: $${\mathfrak{G}}^{A_{0}}({{\mathbf C}((z))})/{\mathfrak{G}}({{\mathbf C}(\{z\})}) \rightarrow {\mathcal{F}}(P_{1},\ldots,P_{k}).$$
:::

::: proof
*Proof.* From the formal case in [\[subsection:slopefiltration\]](#subsection:slopefiltration){reference-type="ref" reference="subsection:slopefiltration"}, it follows that, for any $U \in \prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$ there exists a unique $\hat{F} \in {\mathfrak{G}}({{\mathbf C}((z))})$ such that $\hat{F}[A_{0}] = A_{U}$. The equivalence of $\hat{F}[A_{0}]$ with $\hat{F}'[A_{0}]$ is then just the relation $\hat{F}' \hat{F}^{-1} \in {\mathfrak{G}}({{\mathbf C}(\{z\})})$. ◻
:::

::: rema
[]{#not32 label="not32"} Write $\hat{F}_{U}$ for the $\hat{F}$ in the above proof. More generally, for any $U,V \in \prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$ there exists a unique $\hat{F} \in {\mathfrak{G}}({{\mathbf C}((z))})$ such that $\hat{F}[A_{U}] = A_{V}$; write it $\hat{F}_{U,V}$. Then $\hat{F}_{U,V} = \hat{F}_{V} \hat{F}_{U}^{-1}$ and the condition of equivalence of $M_{U}$ and $M_{V}$ reads: $$M_{U} \sim M_{V} \Longleftrightarrow \hat{F}_{U,V} \in {\mathfrak{G}}({{\mathbf C}(\{z\})}).$$ Giving analyticity conditions for a formal object strongly hints towards a resummation problem! (See chapters [\[chapter:qMalgrangeSibuya\]](#chapter:qMalgrangeSibuya){reference-type="ref" reference="chapter:qMalgrangeSibuya"} and [\[chapter:asymptotictheory\]](#chapter:asymptotictheory){reference-type="ref" reference="chapter:asymptotictheory"}.)
:::

# The affine space of isoformal analytic classes {#chapter:isoformalclasses}
