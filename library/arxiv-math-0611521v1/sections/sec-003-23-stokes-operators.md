---
doc_id: arxiv-math-0611521v1
doc_title: "The q-analogue of the wild fundamental group"
section_id: sec-003-23-stokes-operators
section_title: "Stokes operators"
section_number: 2.3
pages: 12-14
source_pdf: 0611521v1.pdf
source_sha256: 65fcd77b7b0a208e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.946
doc_brief: "The q-analogue of the wild fundamental group — We describe an explicit construction of galoisian Stokes operators for irregular linear q-difference equations."
---
[]{#subsection:Stokesoperators label="subsection:Stokesoperators"}

#### Algebraic summation.

The following computations are extracted from [@JSSTO]. We need the following theta function of Jacobi: $\theta_{q}(z) = \sum_{n \in {\mathbf Z}} q^{-n(n+1)/2} z^{n}$. It is holomorphic in ${\mathbf C}^{*}$ with simple zeroes, all located on the discrete $q$-spiral $[-1;q]$. It satisfies the functional equation: $\sigma_q\theta_{q} = z \theta_{q}$. We then define $\theta_{q,c}(z) = \theta_{q}(z/c)$ (for $c \in {\mathbf C}^{*}$); it is holomorphic in ${\mathbf C}^{*}$ with simple zeroes, all located on the discrete $q$-spiral $[-c;q]$ and satisfies the functional equation: $\sigma_q\theta_{q,c} = \frac{z}{c} \theta_{q,c}$.\
For a given formal class described by $A_{0}$, $\mu_{1},\ldots,\mu_{k}$ and $r_{1},\ldots,r_{k}$ as above, and for any $c \in {\mathbf C}^{*}$, we introduce the matrix $T_{c,A_{0}} \in {\text{Mat}}_{n}({\mathcal{M}({\mathbf C}^{*})})$ which is block-diagonal with blocks $\theta_{c}^{-\mu_{i}} I_{r_{i}}$. Moreover, we shall assume the following normalisation due to Birkhoff and Guenther (see [@RSZ], [@JSSTO]): $$\forall i < j \;,\; \text{~all coefficients of $U_{i,j}$ belong to~}
\sum_{\mu_{i} \leq d < \mu_{j}} {\mathbf C}z^{d}.$$ Then, putting $A'_{i} = c^{\mu_{i}} A_{i} \in GL_{r_{i}}({\mathbf C})$ and $U'_{i,j} = (z/c)^{-\mu_{i}} \theta_{c}^{\mu_{j} -\mu_{i}} U_{i,j}
\in {\text{Mat}}_{r_{i},r_{j}}({\mathcal{O}({\mathbf C}^{*})})$, we have: $$A'_{U'} \underset{def}{=}
T_{c,A_{0}}[A_{U}] = \begin{pmatrix}
A'_{1}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & U'_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & A'_{k}    
\end{pmatrix}.$$ Now, if the images in ${\mathbf{E}_{q}}$ of the spectra $Sp(A'_{i})$ are pairwise disjoint, there is a unique $F' \in {\mathfrak{G}}({\mathcal{O}({\mathbf C}^{*})})$ such that $F'[A'_{0}] = A'_{U'}$. Its coefficients are recursively defined by the equations: $$\sigma_qF'_{i,j} A'_{j} - A'_{i} F'_{i,j} =
\sum_{i < k < j} U'_{i,k} F'_{k,j} + U'_{i,j}.$$ The unique solution of this equation in ${\mathcal{O}({\mathbf C}^{*})}$ is obtained by taking the Laurent series: $$F'_{i,j} = \sum_{p \in {\mathbf Z}} \Phi_{q^{p} A'_{j},A'_{i}}^{-1}(V_{p}) \, z^{p},
\quad \bigl(\sum_{p \in {\mathbf Z}} V_{p} \, z^{p} = 
\sum_{i < k < j} U'_{i,k} F'_{k,j} + U'_{i,j}\bigr),$$ where one writes $\Phi_{B,C}(M) = M B - C M$ (that map is one to one if and only if $Sp(B) \cap Sp(C) = \emptyset$). Note for further use that the condition we have to impose on the spectra is the following: $$\label{equation:nonresonance}
\forall i < j \;,\; 
q^{{\mathbf Z}} c^{\mu_{i}} Sp(A_{i}) \cap q^{{\mathbf Z}} c^{\mu_{j}} Sp(A_{j}) = \emptyset.$$ This is equivalent to requiring that $\overline{c} \not\in \Sigma_{A_{0}}$, where $\Sigma_{A_{0}}$ is some explicit finite subset of ${\mathbf{E}_{q}}$.\
\>From the equalities $A'_{U'} = T_{c,A_{0}}[A_{U}]$, $A'_{0} = T_{c,A_{0}}[A_{0}]$ and $F'[A'_{0}] = A'_{U'}$, we get at last $F[A_{0}] = A_{U}$, where $F = T_{c,A_{0}}^{-1} F' T_{c,A_{0}}$ can be easily computed: it belongs to ${\mathfrak{G}}({\mathcal{M}({\mathbf C}^{*})})$ and $F_{i,j} = \theta_{c}^{\mu_{i} - \mu_{j}} F'_{i,j}$. The condition that the $F'_{i,j}$ are holomorphic over ${\mathbf C}^{*}$ is equivalent to the following condition: $$\label{equation:conditionpolaire}
\forall i < j \;,\; F_{i,j} \text{~has poles only on~} [-c;q], 
\text{~and with multiplicities~} \leq \mu_{j} - \mu_{i}.$$ Then, we get the following conclusion: there is a *unique* $F \in {\mathfrak{G}}({\mathcal{M}({\mathbf C}^{*})})$ such that condition ([\[equation:conditionpolaire\]](#equation:conditionpolaire){reference-type="ref" reference="equation:conditionpolaire"}) holds and $F[A_{0}] = A_{U}$. Note that the condition depends on $\overline{c} \in {\mathbf{E}_{q}}$ rather than $c$. To summarize the discussion:

::: prop
For every $c \in {\mathbf C}^{*}$ satisfying condition ([\[equation:nonresonance\]](#equation:nonresonance){reference-type="ref" reference="equation:nonresonance"}) (*i.e.*, $\overline{c} \not\in \Sigma_{A_{0}}$), there is a unique $F \in {\mathfrak{G}}({\mathcal{M}({\mathbf C}^{*})})$ satisfying condition ([\[equation:conditionpolaire\]](#equation:conditionpolaire){reference-type="ref" reference="equation:conditionpolaire"}) and such that $F[A_{0}] = A_{U}$. We consider this $F$ as obtained by *summation of $\hat{F}_{A}$ in the direction $\overline{c} \in {\mathbf{E}_{q}}$* and, accordingly, write it $S_{\overline{c}} \hat{F}_{A}$.
:::

If we now choose two *$q$-directions of summation* $\overline{c},\overline{d} \in {\mathbf{E}_{q}}$, the ambiguity of summation is expressed by: $$\label{equation:defoperateurStokes}
S_{\overline{c},\overline{d}} \hat{F}_{A} \underset{def}{=}
(S_{\overline{c}} \hat{F}_{A})^{-1} S_{\overline{d}} \hat{F}_{A}.$$ This is a meromorphic automorphism of $A_{0}$. As explained in [@RSZ] and [@JSSTO], it is a *Stokes operator*.

#### Case of one level. {#subsubsection:caseofonelevel}

For further use, we now specialize some of the previous results to the case of two (integral) slopes $\mu < \nu$, and only one "level" $\delta = \nu - \mu \in {\mathbf N}^{*}$. For simplicity, we write our matrices: $$\label{equation:onelevelmatrices}
M_{0} = \begin{pmatrix} z^{\mu} A & 0 \\ 0 & z^{\nu} B \end{pmatrix}
\quad \text{and} \quad
M = \begin{pmatrix} z^{\mu} A & z^{\mu} U B \\ 0 & z^{\nu} B \end{pmatrix},$$ where $A \in GLr({\mathbf C})$, $B \in GL_{s}({\mathbf C})$ and $U \in {\text{Mat}}_{r,s}({\mathbf C}_{\delta-1}[z])$ (polynomials with degree $< \delta$). It is clear that the upper right block can indeed be written in such a way. Then the unique element of ${\mathfrak{G}}({{\mathbf C}((z))})$ which sends $M_{0}$ to $M$ is the matrix $\begin{pmatrix} I_{r} & F \\ 0 & I_{s} \end{pmatrix}$, where $F$ is the unique element of ${\text{Mat}}_{r,s}({{\mathbf C}((z))})$ such that: $$\label{equation:onelevelequation1}
z^{\delta} \sigma_qF - \Lambda(F) = U,$$ Here, we have written $\Lambda(F) = A F B^{-1}$ (thus, an endomorphism of ${\text{Mat}}_{r,s}({\mathbf C})$ and similar spaces). The formal solution $F$ can be computed by identification of coefficients, *i.e.* by solving: $$\label{equation:onelevelequation2}
\forall n \in {\mathbf Z}\;,\; 
q^{n-\delta} F_{n-\delta} - A F_{n} B^{-1} = U_{n}.$$ Similarly, the unique element of ${\mathfrak{G}}({\mathcal{M}({\mathbf C}^{*})})$ such that condition ([\[equation:conditionpolaire\]](#equation:conditionpolaire){reference-type="ref" reference="equation:conditionpolaire"}) holds which sends $M_{0}$ to $M$ is the matrix $\begin{pmatrix} I_{r} & F \\ 0 & I_{s} \end{pmatrix}$, where $F$ is the unique of ${\text{Mat}}_{r,s}({\mathcal{M}({\mathbf C}^{*})})$ with poles only on $[-c;q]$ and with multiplicities $\leq d$ which is solution of equation ([\[equation:onelevelequation1\]](#equation:onelevelequation1){reference-type="ref" reference="equation:onelevelequation1"}). This is solved by putting $F = \theta_{c}^{-\delta} G$, so that $G$ is a solution holomorphic on ${\mathbf C}^{*}$ of the following equation: $$\label{equation:onelevelequation3}
c^{\delta} \sigma_qG - \Lambda(G) = V, \text{~where~} 
G = \theta_{c}^{\delta} F \text{~and~} V = \theta_{c}^{\delta} U.$$ This can be solved by identification of coefficients of the corresponding Laurent series, *i.e.* by solving: $$\label{equation:onelevelequation4}
\forall n \in {\mathbf Z}\;,\; 
c^{\delta} q^{n} G_{n} - A G_{n} B^{-1} = V_{n}.$$ This is possible if $c^{\delta} q^{{\mathbf Z}} \cap Sp(A)/Sp(B) = \emptyset$, which is precisely condition ([\[equation:nonresonance\]](#equation:nonresonance){reference-type="ref" reference="equation:nonresonance"}) specialized to the present setting. Then we can take $G_{n} = (c^{\delta} q^{n} \text{Id}- \Lambda)^{-1} V_{n}$.
