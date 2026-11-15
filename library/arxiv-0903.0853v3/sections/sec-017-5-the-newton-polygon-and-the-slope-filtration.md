---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-017-5-the-newton-polygon-and-the-slope-filtration
section_title: "The Newton polygon and the slope filtration"
section_number: 5
pages: 22-24
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.983
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:Newtonetfiltration label="section:Newtonetfiltration"}

We summarize results from [@JSFIL][^1].

## The Newton polygon {#subsection:Newtonpolygon}

The contents of this section are valid as well in the analytic as in the formal setting. To the (analytic or formal) $q$-difference operator $P = \sum a_{i} \sigma_q^{i} \in {{\mathcal{D}}_{q}}$, we associate the *Newton polygon* []{#not19 label="not19"} $N(P)$, defined as the convex hull of $\{(i,j) \in {\mathbf Z}^{2} ~ | ~j \geq v_{0}(a_{i})\}$, where $v_{0}$ denotes the $z$-adic valuation in ${{\mathbf C}(\{z\})},{{\mathbf C}((z))}$. Multiplying $P$ by a unit $a \sigma_q^{k}$ of ${{\mathcal{D}}_{q}}$ just translates the Newton polygon by a vector of ${\mathbf Z}^{2}$, and we shall actually consider $N(P)$ as defined up to such a translation (or, which amounts to the same, choose a unitary entire $P$). The relevant information therefore consists in the lower part of the boundary of $N(P)$, made up of vectors $(r_{1},d_{1}),\ldots,(r_{k},d_{k})$, $r_{i} \in {\mathbf N}^{*}$, $d_{i} \in{\mathbf Z}$. Going from left to right, the *slopes* $\mu_{i} := \dfrac{d_{i}}{r_{i}}$ are rational numbers such that $\mu_{1} < \cdots < \mu_{k}$. Their set is written $S(P)$ and $r_{i}$ is the *multiplicity* of $\mu_{i} \in S(P)$. The most convenient object is however the *Newton function* $r_{P}: {\mathbf Q}\rightarrow {\mathbf N}$, such that $\mu_{i} \mapsto r_{i}$ and null out of $S(P)$.

[]{#not20 label="not20"}

::: theo
[]{#theo:Newtonpolygon label="theo:Newtonpolygon"} (i) For a given $q$-difference module $M$, all unitary entire $P$ such that $M \simeq {{\mathcal{D}}_{q}}/ {{\mathcal{D}}_{q}}P$ have the same Newton polygon; the *Newton polygon* of $M$ is defined as $N(M) := N(P)$, and we put $S(M) := S(P)$, $r_{M} := r_{P}$.\
(ii) The Newton polygon is additive: for any exact sequence, $$0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0
\Longrightarrow r_{M} = r_{M'} + r_{M''}.$$ (iii) The Newton polygon is multiplicative: $$\forall \mu \in {\mathbf Q}~,~ r_{M_{1} \otimes M_{1}}(\mu) = 
\sum_{\mu_{1} + \mu_{2} = \mu} r_{M_{1}}(\mu_{1}) r_{M_{2}}(\mu_{2}).
\text{Also:~} r_{M^{\vee}}(\mu) = r_{M}(- \mu).$$ (iv) Let $\ell \in {\mathbf N}^{*}$, introduce a new variable $z' := z^{1/\ell}$ (ramification) and make $K' := {{\mathbf C}((z))}[z'] = {\mathbf C}((z'))$ or ${{\mathbf C}(\{z\})}[z'] = {\mathbf C}(\{z'\})$ a difference field extension by putting $\sigma'(z') = q' z'$, where $q'$ is any $\ell^{\text{th}}$ root of $q$. The Newton polygon of the $q'$-difference module $M' := K' \otimes M$ (computed w.r.t. variable $z'$) is given by the formula: $$r_{M}(\mu) = r_{M'}(\ell \mu).$$
:::

To follow the next example, recall from paragraph [\[subsubsection:functorofsolutions\]](#subsubsection:functorofsolutions){reference-type="ref" reference="subsubsection:functorofsolutions"} how we vectorialize a scalar $q$-difference equation $P.f = 0$, $P \in {{\mathcal{D}}_{q}}$, by a $q$-difference system $\sigma_qX = A X$, and then associate to this system a $q$-difference module $({{\mathbf C}(\{z\})}^n,\Phi_A)$. Remember that the latter is isomorphic to some ${{\mathcal{D}}_{q}}/{{\mathcal{D}}_{q}}Q$ (by the cyclic vector lemma and left euclideanity of ${{\mathcal{D}}_{q}}$), but that $Q$ is not equal to $P$, it is dual to $P$.

::: exem
[]{#exem:Tshakaloff label="exem:Tshakaloff"} Vectorializing an analytic equation of order two yields: $$\sigma_q^{2} f + a_{1} \sigma_qf + a_{2} f = 0 \Longleftrightarrow \sigma_qX = A X, 
\text{~with~} X = \begin{pmatrix} f \\ \sigma_qf \end{pmatrix} \text{~and~} 
A = \begin{pmatrix} 0 & 1 \\ -a_{2} & - a_{1} \end{pmatrix}.$$ The associated module is $({{\mathbf C}(\{z\})}^{2},\Phi_{A})$. Putting $e := \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, one has $\Phi_{A}(e) = \begin{pmatrix} -a_{1}/a_{2} \\ 1 \end{pmatrix}$ and: $$\Phi_{A}^{2}(e) = \dfrac{-1}{a_{2}} e + \dfrac{- \sigma_qa_{1}}{\sigma_qa_{2}} \Phi_{A}(e)
\Longrightarrow M \simeq {{\mathcal{D}}_{q}}/ {{\mathcal{D}}_{q}}\hat{L}, \text{~where~}
\hat{L} := \sigma_q^{2} + \dfrac{\sigma_qa_{1}}{\sigma_qa_{2}} \sigma_q+ \dfrac{1}{a_{2}},$$ $\hat{L}$ thus being a dual of $L := \sigma_q^{2} + a_{1} \sigma_q+ a_{2} \in {{\mathcal{D}}_{q}}$.\
Note that if we started from vector $e' := \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, we would compute likewise: $$\Phi_{A}^{2}(e') = 
\dfrac{-1}{\sigma_qa_{2}} e' + \dfrac{- a_{1}}{\sigma_qa_{2}} \Phi_{A}(e')
\Longrightarrow M \simeq {{\mathcal{D}}_{q}}/ {{\mathcal{D}}_{q}}\hat{L'}, \text{~where~}
\hat{L'} := \sigma_q^{2} + \dfrac{a_{1}}{\sigma_qa_{2}} \sigma_q+ \dfrac{1}{\sigma_qa_{2}},$$ another dual of $L$. However, they give the same Newton polygon, since $v_{0}(a_{1}/\sigma_qa_{2}) = v_{0}(\sigma_qa_{1}/\sigma_qa_{2})$ and $v_{0}(1/\sigma_qa_{2}) = v_{0}(1/a_{2})$.\
We now specialize to the equation satisfied by a $q$-analogue of the Euler series, the so-called *Tshakaloff[^2]series*: []{#not21 label="not21"} $$\label{eqn:Tshakaloff}
\text{\tencyr\cyracc Ch}(z) := \sum_{n \geq 0} q^{n(n-1)/2} z^{n}.$$ Then $\hat{\phi} := \text{\tencyr\cyracc Ch}$ satisfies: $$\hat{\phi} = 1 + z \sigma_q\hat{\phi} \Longrightarrow L.\hat{\phi} = 0,$$ where: $$q z L := (\sigma_q- 1)(z \sigma_q- 1) = q z \sigma_q^{2} - (1+z) \sigma_q+ 1.$$ By our previous definitions, $S(L) = \{0,1\}$ (both multiplicities equal $1$). The second computation of a dual above implies that: $$M \simeq {{\mathcal{D}}_{q}}/{{\mathcal{D}}_{q}}\hat{L}, \text{~where~}
\hat{L} := \sigma_q^{2} - q(1+z) \sigma_q+ q^{2} z = (\sigma_q- q z) (\sigma_q- q),$$ whence $S(M) = S(\hat{L}) = \{-1,0\}$ (both multiplicities equal $1$).\
This computation relies on the obvious vectorialisation with matrix $A = \begin{pmatrix} 0 & 1 \\ -1/qz & (1+z)/qz \end{pmatrix}$. However, we also have: $$L.f = 0 \Longleftrightarrow \sigma_qY = B Y,
\text{~with~} Y = \begin{pmatrix} f \\ z \sigma_qf - f \end{pmatrix} 
\text{~and~} B = \begin{pmatrix} z^{-1} & z^{-1} \\ 0 & 1 \end{pmatrix}.$$ The fact that matrix $A$ is analytically equivalent to an upper triangular matrix comes from the analytic factorisation of $\hat{L}$; the exponents of $z$ on the diagonal are the slopes: this, as we shall see, is a general fact when the slopes are integral.
:::

[^1]: Note however that, from [@RS1], we changed our terminology: the slopes of a $q$-difference module are the *opposites* of what they used to be (see herebelow subsection [0.1](#subsection:Newtonpolygon){reference-type="ref" reference="subsection:Newtonpolygon"}); and what we call a pure isoclinic, resp. pure module was previously called pure, resp. tamely irregular (see herebelow subsection [\[subsection:puremodules\]](#subsection:puremodules){reference-type="ref" reference="subsection:puremodules"}).

[^2]: We use the cyrillic letter $\text{\tencyr\cyracc Ch}$ ("tsh") to denote it.
