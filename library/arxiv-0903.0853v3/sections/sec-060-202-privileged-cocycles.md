---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-060-202-privileged-cocycles
section_title: "Privileged cocycles"
section_number: 20.2
pages: 107-110
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.763
latex_coverage_ratio: 0.948
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:privilegedcocycles label="section:privilegedcocycles"}

In \"applications\", it is sometimes desirable to have explicit cocycles to work with instead of cohomology classes. We shall now describe cocycles with nice properties, that can be explicitly computed from a matrix in standard form. Most of the proofs of what follows are consequences of theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"}. However, they can also be obtained through the more elementary approach of [@JSStokes], which we shall briefly summarize here in subsection [0.1](#subsection:algebraicsummation){reference-type="ref" reference="subsection:algebraicsummation"}.\
Fix $A_{0}$ as in [\[eqn:formestandarddiagonaleentiere\]](#eqn:formestandarddiagonaleentiere){reference-type="eqref" reference="eqn:formestandarddiagonaleentiere"} page and let $M_{0}$ be the corresponding pure module. *All notations that follow are relative to this $A_{0}$ and $M_{0}$*. Recall from section [\[section:generalnotations\]](#section:generalnotations){reference-type="ref" reference="section:generalnotations"} at the end of the introduction the notations $\overline{a} \in {\mathbf{E}_{q}}$ for the class of $a \in {\mathbf C}^{*}$ and $[a;q] := a q^{{\mathbf Z}}$ for the corresponding $q$-spiral. Also recall from paragraph [\[subsection:thetafunctions\]](#subsection:thetafunctions){reference-type="ref" reference="subsection:thetafunctions"} the function ${\theta_{q}}$, holomorphic over ${\mathbf C}^{*}$ with simple zeroes on $[-1;q]$ and satisfying the functional equation $\sigma_q{\theta_{q}}= z {\theta_{q}}$.

## "Algebraic summation" {#subsection:algebraicsummation}

To construct cocycles encoding the analytic class of $A \in {\text{GL}}_{n}({{\mathbf C}(\{z\})})$, we use "meromorphic sums" of $\hat{F}_{A}$. These can be obtained either by the summation process of theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"}, or by the "algebraic summation process" of [@JSStokes]. We now summarize this process. We restrict to the case of divisors supported by a point, since it is sufficient for classification.\
Let $A$ as in [\[eqn:formestandardtriangulaireentiere\]](#eqn:formestandardtriangulaireentiere){reference-type="eqref" reference="eqn:formestandardtriangulaireentiere"} (we do not assume from start that it is in Birkhoff-Guenther normal form). We want to solve the equation $\sigma_qF = A F A_{0}^{-1}$ with $F \in {\mathfrak{G}}_{A_{0}}$ meromorphic in some punctured neighborhood of $0$ in ${\mathbf C}^{*}$. Since $A,A_{0},A^{-1},A_{0}^{-1}$ are all holomorphic in some punctured neighborhood of $0$ in ${\mathbf C}^{*}$, the singular locus[^1] of $F$ near $0$ is invariant under $q^{-{\mathbf N}}$: it is therefore a finite union of germs of half $q$-spirals $a q^{-{\mathbf N}}$ (the finiteness flows from the meromorphy of $F$). If we take $A$ in Birkhoff-Guenther normal form (definition [\[defi:BirkhoffGuenthernormalform\]](#defi:BirkhoffGuenthernormalform){reference-type="ref" reference="defi:BirkhoffGuenthernormalform"}), the functional equation $\sigma_qF = A F A_{0}^{-1}$ actually allows us to extend $F$ to a meromorphic matrix on the whole of ${\mathbf C}^{*}$ and its singular locus is a finite union of discrete logarithmic $q$-spirals $[a;q]$.\
To illustrate the process, we start with an example.

::: exem
[]{#exem:Tshakaloff7 label="exem:Tshakaloff7"} Setting $A_{u} := \begin{pmatrix} z^{-1} & z^{-1} u \\ 0 & 1 \end{pmatrix}$, with $u \in {{\mathbf C}(\{z\})}$, and $F = \begin{pmatrix} 1 & f \\ 0 & 1 \end{pmatrix}$, we saw that $A_{u} = F[A_{0}] \Longleftrightarrow z \sigma_qf - f = u$. This admits a unique formal solution $\hat{f}$, which can be computed by iterating the $z$-adically contracting operator $f \mapsto - u + z \sigma_qf$. If $A$ is in Birkhoff-Guenther normal form, $u \in {\mathbf C}$ and $\hat{f} = - u \; \text{\tencyr\cyracc Ch}$ (the Tshakaloff series). We want $f$ to be meromorphic on some punctured neighborhood of $0$ in ${\mathbf C}^{*}$, which we write $f \in {\mathcal{M}}({\mathbf C}^{*},0)$, and to have (in germ) half $q$-spirals of poles. For simplicity, we shall assume that $u$ is holomorphic on ${\mathbf C}^{*}$, so that $f$ will have to be meromorphic on the whole of ${\mathbf C}^{*}$ with complete $q$-spirals of poles. []{#not84 label="not84"} We set ${\theta_{q,c}}(z) := {\theta_{q}}(z/c)$, which is holomorphic on ${\mathbf C}^{*}$, with simple zeroes on the $q$-spiral $[-c;q]$ and satisfies the functional equation $\sigma_q{\theta_{q,c}}= (z/c) {\theta_{q,c}}$. We look for $f$ with simple poles on $[-c;q]$ by writing it $f = g/{\theta_{q,c}}$ and looking for $g$ holomorphic on ${\mathbf C}^{*}$ and satisfying the functional equation: $$\begin{aligned}
z \sigma_q(g/{\theta_{q,c}}) - (g/{\theta_{q,c}}) = u &\Longleftrightarrow c \sigma_qg - g = u {\theta_{q,c}}\\
&\Longleftrightarrow \forall n \in {\mathbf Z}\;,\; (c q^{n} - 1) g_{n} = [u {\theta_{q,c}}]_{n},
\end{aligned}$$ where we have introduced the Laurent series expansions $g = \sum\limits_{n \in {\mathbf Z}} g_{n} z^{n}$ and $u {\theta_{q,c}}= \sum\limits_{n \in {\mathbf Z}} [u {\theta_{q,c}}]_{n} z^{n}$. If $c \not\in q^{{\mathbf Z}}$, we get the solution: []{#not85 label="not85"} $$f_{\overline{c}} := 
\dfrac{1}{{\theta_{q,c}}} \, \sum_{n \in {\mathbf Z}} \dfrac{[u {\theta_{q,c}}]_{n}}{c q^{n} - 1} z^{n}.$$ This is clearly the unique solution of $z \sigma_qf - f = u$ with only simple poles on $[-c;q]$, a condition that depends on $\overline{c}$ only and justifies the notation $f_{\overline{c}}$. We consider it as *the summation of the formal solution $\hat{f}$ in the "authorized direction of summation" $\overline{c} \in {\mathbf{E}_{q}}$*. Accordingly, we write it $S_{\overline{c}} \hat{f}$. The sum $S_{\overline{c}} \hat{f}$ is asymptotic to $\hat{f}$ (see further below). Note that the "directions of summation" are elements of ${\mathbf{E}_{q}}= {\mathbf C}^{*}/q^{{\mathbf Z}}$ which plays here the role of the circle of directions $S^{1} := {\mathbf C}^{*}/{\mathbf R}_{+}^{*}$ of the classical theory. Also note that all "directions of summations" $\overline{c} \in {\mathbf{E}_{q}}$ are authorized, except for one.
:::

Returning to the general equation $F[A_{0}] = A \Leftrightarrow \sigma_qF = A F A_{0}^{-1}$, we want to look for solutions $F$ that are meromorphic on some punctured neighborhood of $0$ in ${\mathbf C}^{*}$, and we want to have unicity by imposing conditions on the half $q$-spirals of poles: position and multiplicity. Thus, for $f \in {\mathcal{M}}({\mathbf C}^{*},0)$, and for a finite family $(a_{i})$ of points of ${\mathbf C}^{*}$ and $(n_{i})$ of integers, we shall translate the condition: "The germ $f$ at $0$ has all its poles on $\bigcup [a_{i};q]$, the poles on $[a_{i};q]$ having at most multiplicity $n_{i}$" by an inequality of divisors on ${\mathbf{E}_{q}}$: []{#not86 label="not86"} $${\text{div}}_{{\mathbf{E}_{q}}}(f) \geq - \sum n_{i} [\overline{a_{i}}].$$ We introduce a finite subset of ${\mathbf{E}_{q}}$ defined by resonancy conditions: $$\Sigma_{A_{0}} := \bigcup_{1 \leq i < j \leq k} S_{i,j}, \text{~where~}
S_{i,j} := \{p(-a) \in {\mathbf{E}_{q}}~ | ~
q^{{\mathbf Z}} a^{\mu_{i}} \text{Sp}(A_{i}) \cap q^{{\mathbf Z}} a^{\mu_{j}} \text{Sp}(A_{j})
\neq \emptyset\}.$$ Here, $\text{Sp}$ denotes the spectrum of a matrix.

::: theo
[]{#theo:algebraicsummation label="theo:algebraicsummation"} For any matrix $A$ in form [\[eqn:formestandardtriangulaireentiere\]](#eqn:formestandardtriangulaireentiere){reference-type="eqref" reference="eqn:formestandardtriangulaireentiere"}, and for any "authorized direction of summation" $\overline{c} \in {\mathbf{E}_{q}}\setminus \Sigma_{A_{0}}$, there exists a unique meromorphic gauge transform $F \in {\mathfrak{G}}_{A_{0}}\bigl({\mathcal{M}}({\mathbf C}^{*},0)\bigr)$ satisfying: $$F[A_{0}] = A \text{~and~} 
{\text{div}}_{{\mathbf{E}_{q}}}(F_{i,j}) \geq - (\mu_{j} - \mu_{i}) [\overline{-c}]
\text{~for~} 1 \leq i < j \leq k.$$
:::

::: proof
*Proof.* See [@JSStokes theorem 3.7]. ◻
:::

Of course, ${\text{div}}_{{\mathbf{E}_{q}}}(F_{i,j}) \geq - (\mu_{j} - \mu_{i}) [\overline{-c}]$ means that all coefficients $f$ of the rectangular block $F_{i,j}$ are such that ${\text{div}}_{{\mathbf{E}_{q}}}(f) \geq - (\mu_{j} - \mu_{i}) [\overline{-c}]$. The matrix $F$ of the theorem is considered as *the summation of $\hat{F}_{A}$ in the authorized direction of summation $\overline{c} \in {\mathbf{E}_{q}}$* and we write it $S_{\overline{c}} \hat{F}_{A}$.\
It is actually the very same sum as that obtained in theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"}. Indeed, using notations from subsection [\[subsection:sommabilite\]](#subsection:sommabilite){reference-type="ref" reference="subsection:sommabilite"}, if one requires the divisors $\Lambda_{i}$ to be supported by a single point $\overline{c} \in {\mathbf{E}_{q}}$, the genericity condition of definition [\[defi:compatible\]](#defi:compatible){reference-type="ref" reference="defi:compatible"} translates here to: $\overline{c} \in {\mathbf{E}_{q}}\setminus \Sigma_{A_{0}}$, as one sees by using the dictionary provided in remark [\[rema:dictionnary\]](#rema:dictionnary){reference-type="ref" reference="rema:dictionnary"}. Then, from the same dictionary, one draws that the conditions on the sum guaranteed by the conclusion of theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"} immediately imply the conditions on $S_{\overline{c}} \hat{F}_{A}$ guaranteed by the above theorem, and the unicity in the above theorem allows one to conclude. As a consequence of subsection [\[subsection:sommabilite\]](#subsection:sommabilite){reference-type="ref" reference="subsection:sommabilite"}, the sum $S_{\overline{c}} \hat{F}_{A}$ is asymptotic to $\hat{F}_{A}$.\
The algorithm to compute $F := S_{\overline{c}} \hat{F}_{A}$ is the following. We introduce the gauge transform: $$\label{not87}
T_{A_{0},c} :=
\begin{pmatrix}
{\theta_{q,c}}^{-\mu_{1}} I_{r_{1}}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & 0 & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots &  {\theta_{q,c}}^{-\mu_{k}} I_{r_{k}}
\end{pmatrix}.
\quad \text{(Recall that~} {\theta_{q,c}}(z) = {\theta_{q}}(z/c).)$$ Then $F[A_{0}] = A$ , is equivalent to $G[B_{0}] = B$, where $B = T_{A_{0},c}[A]$, $B_{0} = T_{A_{0},c}[A_{0}]$, and $G = T_{A_{0},c} F T_{A_{0},c}^{-1}$. Now, $B_{0}$ is block-diagonal with blocks $c^{\mu_{i}} A_{i} \in {\text{GL}}_{r_{i}}({\mathbf C})$, and we can solve for $G[B_{0}] = B$ with $G \in {\mathfrak{G}}_{A_{0}}\bigl({\mathcal{O}}({\mathbf C}^{*},0)\bigr)$, because this boils down to a system of matricial equations: $$(\sigma_qX) c^{\mu_{j}} A_{j} - c^{\mu_{i}} A_{i} X = \text{~some r.h.s.~} Y.$$ Expanding in Laurent series $X = \sum X_{p} z^{p}$, $Y = \sum Y_{p} z^{p}$, we are led to: $$q^{p} X_{p} c^{\mu_{j}} A_{j} - c^{\mu_{i}} A_{i} X_{p} = Y_{p}.$$ Since the spectra of $c^{\mu_{i}} A_{i}$ and $c^{\mu_{i}} A_{i}$ are non resonant modulo $q^{{\mathbf Z}}$, the spectra of $q^{p} c^{\mu_{i}} A_{i}$ and $c^{\mu_{i}} A_{i}$ are disjoint and the endomorphism $V \mapsto q^{p} V c^{\mu_{j}} A_{j} - c^{\mu_{i}} A_{i} V$ of ${\text{Mat}}_{r_{i},r_{j}}({\mathbf C})$ is actually an automorphism. There is therefore a unique formal solution $X$, and convergence in $({\mathbf C}^{*},0)$ is not hard to prove, so we indeed get $G$ with the required properties. Last, putting $F := T_{A_{0},c}^{-1} G T_{A_{0},c}$ gives $S_{\overline{c}} \hat{F}_{A}$ in the desired form.

## Privileged cocycles {#subsection:privilegedcocycles}

We have three ways of constructing a cocycle encoding the analytic isoformal class of $A$ in the formal class defined by $A_{0}$: the map $\lambda$ defined in the first part of the proof of theorem [\[theo:secondqMalgrangeSibuya\]](#theo:secondqMalgrangeSibuya){reference-type="ref" reference="theo:secondqMalgrangeSibuya"}; the construction of theorem [\[theo:Stokes\]](#theo:Stokes){reference-type="ref" reference="theo:Stokes"}; and the one of [@JSStokes], based on theorem [\[theo:algebraicsummation\]](#theo:algebraicsummation){reference-type="ref" reference="theo:algebraicsummation"} above. Because of what was said just after this theorem, the last two ways give the same *privileged* cocycle, which we shall now describe more precisely.

::: rema
The construction in theorem [\[theo:secondqMalgrangeSibuya\]](#theo:secondqMalgrangeSibuya){reference-type="ref" reference="theo:secondqMalgrangeSibuya"} is not deterministic, since it involves the choice of a good covering and of functions $g_i$ asymptotic to $\hat{F}$. However, among the possible choices, there is the possibility to take the sums defined by theorems [\[theo:Stokes\]](#theo:Stokes){reference-type="ref" reference="theo:Stokes"} and [\[theo:algebraicsummation\]](#theo:algebraicsummation){reference-type="ref" reference="theo:algebraicsummation"}. Thus, among the possible cocycles constructed in theorem [\[theo:secondqMalgrangeSibuya\]](#theo:secondqMalgrangeSibuya){reference-type="ref" reference="theo:secondqMalgrangeSibuya"}, there is our privileged cocycle.
:::

If $M_{0}$ is the pure module with matrix $A_{0}$, recall from section [\[section:fundamentalisomorphism\]](#section:fundamentalisomorphism){reference-type="ref" reference="section:fundamentalisomorphism"} the sheaf $\Lambda_I(M_0)$ of automorphisms of $A_{0}$ infinitely tangent to the identity. We shall also denote ${\mathfrak{U}}$ the covering of ${\mathbf{E}_{q}}$ consisting of the Zariski open subsets $U_{c} := {\mathbf{E}_{q}}\setminus \{c\}$ []{#not88 label="not88"} such that $c \not\in \Sigma_{A_{0}}$ (thus, we drop the upper bar denoting classes in ${\mathbf{E}_{q}}$). For any $c \in {\mathbf{E}_{q}}\setminus \Sigma_{A_{0}}$ an authorized direction of summation, write for short $F_{c} := S_{c} \hat{F}_{A}$. Then $F_{c}$ is holomorphic invertible over the preimage $p^{-1}(U_{c}) \subset {\mathbf C}^{*}$. If $c,d \in {\mathbf{E}_{q}}\setminus \Sigma_{A_{0}}$, $F_{c,d} := F_{c}^{-1} F_{d}$ is in ${\mathfrak{G}}\bigl({\mathcal{O}}(p^{-1}(U_{c} \cap U_{d}))\bigr)$ and it is an automorphism of $A_{0}$ infinitely tangent to the identity: $$F_{c,d} \in \Lambda_I(M_0)(U_{c} \cap U_{d}).$$ The cocycle $(F_{c,d}) \in Z^{1}({\mathfrak{U}},\Lambda_I(M_0))$ involves rectangular blocks $(F_{c,d})_{i,j}$ (for $1 \leq i < j \leq k$) belonging to the space $E_{i,j}$ of solutions of the equation $(\sigma_qX) z^{\mu_{j}} A_{j} = z^{\mu_{i}} A_{i} X$. For $X \in E_{i,j}$, it makes sense to speak of its poles on ${\mathbf{E}_{q}}$, and of their multiplicities. For $c,d \in {\mathbf{E}_{q}}\setminus \Sigma_{A_{0}}$ []{#not89 label="not89"} distinct, we write $E_{i,j,c,d}$ the space of those $X \in E_{i,j}$ that have at worst poles in $c,d$ and with multiplicities $\mu_{j} - \mu_{i}$.

::: lemm
[]{#lemm:dimensionEijcd label="lemm:dimensionEijcd"} The space $E_{i,j,c,d}$ has dimension $r_{i} r_{j} (\mu_{j} - \mu_{i})$.
:::

::: proof
*Proof.* Writing again $\theta_{q,a}(z) := {\theta_{q}}(z/a)$, any $X \in E_{i,j,c,d}$ can be written $(\theta_{q,a} \theta_{q,b})^{-(\mu_{j} - \mu_{i})} Y$, where $p(-a) = c$, $p(-b) = d$ and $Y$ is holomorphic on ${\mathbf C}^{*}$ and satisfies the equation: $$\sigma_qY = \left(\dfrac{z}{ab}\right)^{\mu_{j} - \mu_{i}} A_{i} Y A_{j}^{-1}.$$ Taking $Y$ as a Laurent series, one sees that $(\mu_{j} - \mu_{i})$ consecutive terms in ${\text{Mat}}_{r_{i},r_{j}}({\mathbf C})$ can be chosen at will. ◻
:::

::: defi
[]{#defi:cocycleprivilegie label="defi:cocycleprivilegie"} The cocycle $(F_{c,d}) \in Z^{1}({\mathfrak{U}},\Lambda_I(M_0))$ is said to be *privileged* if $(F_{c,d})_{i,j} \in E_{i,j,c,d}$ for all distinct $c,d \in {\mathbf{E}_{q}}\setminus \Sigma_{A_{0}}$ and all $1 \leq i < j \leq k$. The space of privileged cocycles is denoted $Z^{1}_{pr}({\mathfrak{U}},\Lambda_I(M_0))$. []{#not90 label="not90"}
:::

It is not hard to see that, $i,j$ being fixed, the corresponding component $(c,d) \mapsto (F_{c,d})_{i,j}$ of a cocycle is totally determined by its value at any particular choice of $c,d$. That is, fixing distinct $c,d \in {\mathbf{E}_{q}}\setminus \Sigma_{A_{0}}$ gives an isomorphism: $$Z^{1}_{pr}({\mathfrak{U}},\Lambda_I(M_0)) \rightarrow 
\bigoplus_{1 \leq i < j \leq k} E_{i,j,c,d}.$$ Thus, the space of privileged cocycles has the same dimension as ${\mathcal{F}}(M_{0})$. Actually, one has two bijections:

::: theo
The following natural maps are bijections: $${\mathcal{F}}(M_{0}) \rightarrow Z^{1}_{pr}({\mathfrak{U}},\Lambda_I(M_0)) \rightarrow
H^{1}({\mathbf{E}_{q}},\Lambda_I(M_0)).$$
:::

::: proof
*Proof.* See [@JSStokes prop. 3.17, th. 3.18]. The second map is the natural one. ◻
:::

## $q$-Gevrey interpolation {#subsection:qGevreyinterpolationbis}

The results found in section [\[section:qGevreyinterpolation\]](#section:qGevreyinterpolation){reference-type="ref" reference="section:qGevreyinterpolation"} can be adapted here *mutatis mutandis*: the two classification problems tackled there lead to the following spaces of classes: $\bigoplus\limits_{\mu_{j} - \mu_{i} < 1/s} E_{i,j,c,d}$ and $\bigoplus\limits_{\mu_{j} - \mu_{i} \geq 1/s} E_{i,j,c,d}$, which have exactly the desired dimensions. This can be most easily checked using the devissage arguments from section [\[section:devissageqGevrey\]](#section:devissageqGevrey){reference-type="ref" reference="section:devissageqGevrey"} below.

[^1]: In the context of $q$-difference equations, the singular locus of a matrix of functions $P$ is made of the poles of $P$ as well as those of $P^{-1}$. For a unipotent matrix, like $F$, these are all poles of $F$ since $F^{-1}$ is a polynomial in $F$.
