---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-095-342-isoformal-q-gevrey-classiﬁcation
section_title: "Isoformal q-Gevrey classiﬁcation. —"
section_number: 3.4.2
pages: 49-49
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
text_source: latex
latex_prose_ratio: 0.602
latex_coverage_ratio: 0.927
---
[]{#subsection:qGevreymoduli label="subsection:qGevreymoduli"}

#### $q$-Gevrey classification for arbitrary slopes

One can state the moduli problem for $q$-Gevrey classification at order $s$, that is, over the field ${{{\mathbf C}((z))}_{q;s}}$ of $q$-Gevrey series of order $s >0$ (see subsection [\[subsection:qGevreyExt\]](#subsection:qGevreyExt){reference-type="ref" reference="subsection:qGevreyExt"}). From proposition [\[prop:dimensiondeuxpentesqGevrey\]](#prop:dimensiondeuxpentesqGevrey){reference-type="ref" reference="prop:dimensiondeuxpentesqGevrey"}, one gets, by the same argument as before:

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
