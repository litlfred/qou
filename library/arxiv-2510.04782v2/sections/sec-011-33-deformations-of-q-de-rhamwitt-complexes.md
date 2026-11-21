---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-011-33-deformations-of-q-de-rhamwitt-complexes
section_title: "Deformations of q-de Rham–Witt complexes"
section_number: 3.3
pages: 28-32
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.979
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
[]{#subsec:TwistedqDeRham label="subsec:TwistedqDeRham"} We fix a perfectly covered $\Lambda$-ring $A$ as before. We let $\psi^m$ denote its Adams operations, which we extend to a map $\psi^m\colon A[q]\rightarrow A[q]$ via $\psi^m(q)\coloneqq q^m$. We'll also frequently use the Berthelot--Ogus décalage functor $\L\eta_{[m]_q}$ (see [@BMS1 §] or [@Stacks]).

In this subsection, we'll study *twisted $q$-de Rham complexes*: For $S$ smooth over $A$, these are certain $(q^m-1)$-complete $\IE_\infty$-$A[q]$-algebras $\qOmega_{S/A}^{(m)}$, refining the $(q-1)$-complete $\IE_\infty$-$A[q]$-algebras $\L\eta_{[m]_q}\qOmega_{S/A}$ for all $m\in\IN$. The rationale behind our notation and the name *twisted $q$-de Rham complexes* is as follows: If the global $q$-de Rham complex would admit Adams operations $\psi^m$ inducing equivalences $$\psi^m\colon \left(\qOmega_{S/A}\lotimes_{A[q],\psi^m}A[q]\right)_{(q-1)}^\complete\overset{\simeq}{\longrightarrow}\L\eta_{[m]_q}\qOmega_{S/A}\,,$$ then the corresponding twisted $q$-de Rham complex could simply be constructed as the $(q^m-1)$-completion of the "Adams-twist" $\qOmega_{S/A}\lotimes_{A[q],\psi^m}A[q]$.

[^1]

However, such global Adams operations don't exist in general (this already fails if $S$ is étale over $A$, as $\Lambda$-structures usually don't extend along étale maps). The best we have is, for every prime $p$, a Frobenius $\phi_p$ on the $p$-completion $(\qOmega_{S/A})_p^\complete$. Still, these $p$-adic Frobenii are enough to construct $\qOmega_{S/A}^{(m)}$.

::: numpar
[]{#con:TwistedqDeRham label="con:TwistedqDeRham"} Let $S$ be a smooth $A$-algebra. We'll construct a $(q^m-1)$-complete $\IE_\infty$-$A[q]$-algebra using [\[cor:CompleteDescent\]](#cor:CompleteDescent){reference-type="ref" reference="cor:CompleteDescent"}. In the notation of that corollary, take $$E_d\coloneqq \left(\L\eta_{[m/d]_q}\qOmega_{S/A}\lotimes_{A[q],\psi^d}A[q]\right)_{\Phi_d(q)}^\complete\,.$$ We must also provide $p$-adic gluing equivalences. For $p$ a prime such that $pd\mid m$, the required gluing equivalence $(E_{pd})_p^\complete\simeq (E_d)_p^\complete$ should be of the form $$\left(\L\eta_{[m/pd]_q}\qOmega_{S/A}\lotimes_{A[q],\psi^{pd}}A[q]\right)_{(p,\Phi_{pd}(q))}^\complete\overset{\simeq}{\longrightarrow}\left(\L\eta_{[m/d]_q}\qOmega_{S/A}\lotimes_{A[q],\psi^d}A[q]\right)_{(p,\Phi_d(q))}^\complete\,.$$ To construct this, we may replace $\L\eta_{[m/pd]_q}$ and $\L\eta_{[m/d]_q}$ by $\L\eta_{[p^\alpha]_q}$ and $\L\eta_{[p^{\alpha+1}]_q}$, where $\alpha\coloneqq v_p(m/pd)$, because the factor $[m/pd]_q/[p^\alpha]_q$ will be invertible on either side. It will thus be enough to construct an equivalence $$\left(\L\eta_{[p^\alpha]_q}\qOmega_{S/A}\lotimes_{A[q],\psi^p}A[q]\right)_{(p,q-1)}^\complete\overset{\simeq}{\longrightarrow} \Bigl(\L\eta_{[p^{\alpha+1}]_q}\qOmega_{S/A}\Bigr)_{(p,q-1)}^\complete$$ Now $(\L\eta_{[p^\alpha]_q}\qOmega_{S/A})_p^\complete\simeq \L\eta_{[p^\alpha]_q}(\qOmega_{S/A})_p^\complete$. Indeed, $\qOmega_{S/A}$ is $(q-1)$-complete, so $p$-completion agrees with $[p^\alpha]_q$-completion, which always commutes with $\L\eta_{[p^\alpha]_q}$ (see [@BMS1 Lemma ]). Thus, we may replace $\qOmega_{S/A}$ by its $p$-completion on the left-hand side; the same argument applies to the right-hand side as well.

Finally, if $(B,J)$ denotes the prism $(\widehat{A}_p\qpower,[p]_q)$ and $T\coloneqq \widehat{S}_p[\zeta_p]$, then $(\qOmega_{S/A})_p^\complete\simeq \Prism_{T/B}$, and so the desired gluing equivalence can be constructed using the general fact that the relative Frobenius induces an equivalence (see [@Prismatic Theorem ]) $$\phi_{/B}\colon\Prism_{T/B}\clotimes_{B,\phi_B}B\overset{\simeq}{\longrightarrow} \L\eta_J\Prism_{T/B}\,.$$ According to [\[cor:CompleteDescent\]](#cor:CompleteDescent){reference-type="ref" reference="cor:CompleteDescent"}, we can glue the $E_d$ for all $d\mid m$ to a $(q^m-1)$-complete $\IE_\infty$-$A[q]$-algebra $\qOmega_{S/A}^{(m)}$. This is the *$m$^th^ twisted $q$-de Rham complex of $S$ over $A$*. Via animation, we can then define a functor $$\qdeRham_{-/A}^{(m)}\colon \cat{AniAlg}_A\longrightarrow \CAlg\left(\widehat{\Dd}_{(q^m-1)}\bigl(A[q]\bigr)\right)\,,$$ which agrees with $\qOmega_{-/A}^{(m)}$ on polynomial-$A$-algebras (but not on all smooth $A$-algebras, due to the usual issues in characteristic $0$).
:::

The arithmetic fracture square for $\qOmega_{S/A}^{(m)}$ (in the sense of [\[par:Notations\]](#par:Notations){reference-type="ref" reference="par:Notations"}) can be read off from the construction.

::: lem
[]{#lem:TwistedqDeRhamFractureSquare label="lem:TwistedqDeRhamFractureSquare"} Fix $m\in\IN$ and $N\neq 0$ divisible by $m$. For any prime $p\mid N$ and any divisor $d\mid m$ write $m=p^{v_p(m)}m_p$ and $d=p^{v_p(d)}d_p$, where $m_p$ and $d_p$ are coprime to $p$. Let also $$\phi_{p/A[q]}\colon \qOmega_{S/A}\lotimes_{A[q],\psi^p}A[q]\longrightarrow \left(\qOmega_{S/A}\right)_p^\complete$$ denote the relative Frobenius coming from the identification with prismatic cohomology. Then we have a functorial pullback square $$\begin{tikzcd}
                \qOmega_{S/A}^{(m)}\rar\dar\drar[pullback] & \prod_{p\mid N}\prod_{d_p\mid m_p}\left(\qOmega_{S/A}\lotimes_{A[q],\psi^{p^{\smash{v_p(m)}}d_p}}A[q]\right)_{(p,\Phi_{d_p}(q))}^\complete\dar["\left(\phi_{p/A[q]}^{v_p(m/d)}\right)_{p\mid N,\,d\mid m}"]\\
                \prod_{d\mid m}\left(\qOmega_{S/A}\lotimes_{A[q],\psi^d}A\bigl[\localise{N},q\bigr]\right)_{\Phi_d(q)}^\complete\rar & \prod_{p\mid N}\prod_{d \mid m}\Bigl(\qOmega_{S/A}\lotimes_{A[q],\psi^{d}}A[q]\Bigr)_p^\complete\bigl[\localise{p}\bigr]_{\Phi_d(q)}^\complete
            \end{tikzcd}$$
:::

::: proof
*Proof.* Using [\[rem:GluingCompletions\]](#rem:GluingCompletions){reference-type="ref" reference="rem:GluingCompletions"}, the desired pullback square can be identified with the $(q^m-1)$-completed arithmetic fracture square $$\begin{tikzcd}
                \qOmega_{S/A}^{(m)}\rar\dar\drar[pullback] & \prod_{p\mid N}\bigl(\qOmega_{S/A}^{(m)}\bigr)_p^\complete\dar\\
                \qOmega_{S/A}^{(m)}\bigl[\localise{N}\bigr]_{(q^m-1)}^\complete\rar & \prod_{p\mid N}\bigl(\qOmega_{S/A}^{(m)}\bigr)_p^\complete\bigl[\localise{p}\bigr]_{(q^m-1)}^\complete
            \end{tikzcd}$$ Here we also use that $[m/d]_q$ is mapped to a unit under $\psi^d\colon A[q]\rightarrow A[1/N,q]_{\Phi_d(q)}^\complete$, so we may ignore $\L\eta_{[m/d]_q}$ for any $d\mid m$ in the bottom left corner. Similarly, we may ignore any $\L\eta_{[m/p^{v_p(m)} d]_q}$ in the top or bottom right corner. ◻
:::

::: numpar
[]{#con:TwistedqDeRhamFunctoriality label="con:TwistedqDeRhamFunctoriality"} Whenever $n\mid m$, there's a map of $\IE_\infty$-$A[q]$-algebras $$\bigl(\qOmega_{S/A}^{(m)}\bigr)_{(q^n-1)}^\complete\longrightarrow \qOmega_{S/A}^{(n)}\,,$$ functorial in $S$. To construct this map, we once again appeal to the gluing procedure of [\[cor:CompleteDescent\]](#cor:CompleteDescent){reference-type="ref" reference="cor:CompleteDescent"}. On $\Phi_{d}$-completions, where $d\mid n$, the desired map is induced by the symmetric monoidal natural transformation $\L\eta_{[m/d]_q}\Rightarrow \L\eta_{[n/d]_q}$. It's straightforward to check that this is compatible with the $p$-adic gluings from [\[con:TwistedqDeRham\]](#con:TwistedqDeRham){reference-type="ref" reference="con:TwistedqDeRham"}. Alternatively, we can use the pullback square from [\[lem:TwistedqDeRhamFractureSquare\]](#lem:TwistedqDeRhamFractureSquare){reference-type="ref" reference="lem:TwistedqDeRhamFractureSquare"}: On the bottom part of the diagram, $\bigl(\qOmega_{S/A}^{(m)}\bigr)_{(q^n-1)}^\complete\rightarrow \qOmega_{S/A}^{(n)}$ is induced by projection to those factors where $d\mid n$. In the top right corner, we also need to apply the relative Frobenius $\phi_{p/A[q]}^{v_p(m/n)}$ in any factor where $d_p\mid n_p$.

These maps can be assembled into a functor $\qOmega_{S/A}^{(-)}\colon \IN\rightarrow \CAlg(\widehat{\Dd}_\Hh(A[q]))$, where $\IN$ denotes the category of natural numbers partially ordered by divisibility. Furthermore, this functor is itself functorial in $S$. We'll refrain from spelling out the argument, as it would just add one more layer of technicalities. To construct the Habiro descent eventually, we only need the individual maps, not the whole functor with all its higher coherences, since any $\limit_{m\in\IN}$ can be replaced by the limit over the sequential subdiagram given by $\{n!\}_{n\geqslant 1}$.
:::

::: rem
The maps $\bigl(\qOmega_{S/A}^{(m)}\bigr)_{(q^n-1)}^\complete\rightarrow \qOmega_{S/A}^{(n)}$ are usually quite far from being equivalences, as can be seen from the discrepancy between $\L\eta_{[m/d]_q}$ and $\L\eta_{[n/d]_q}$. Thus, we can form the limit $$\limit_{m\in\IN}\qOmega_{S/A}^{(m)}\,,$$ but it will usually be a pathological object (unless $S$ is étale over $A$, in which case we recover [\[con:RelativeHabiroRing\]](#con:RelativeHabiroRing){reference-type="ref" reference="con:RelativeHabiroRing"}). In particular, it won't be a Habiro descent of $\qOmega_{S/A}$.
:::

::: rem
[]{#rem:qOmegaHabiroDescent label="rem:qOmegaHabiroDescent"} To get $\bigl(\qOmega_{S/A}^{(m)}\bigr)_{(q^n-1)}^\complete\rightarrow \qOmega_{S/A}^{(n)}$ closer to being an equivalence, a natural idea goes as follows: The Berthelot--Ogus décalage functors $\L\eta_{[m/d]_q}$ and $\L\eta_{[n/d]_q}$ come equipped with canonical filtrations (see [@BMS2 Proposition ]). If these filtrations would glue to give filtrations on $\qOmega_{S/A}^{(m)}$ and $\qOmega_{S/A}^{(n)}$, we could modify $\qOmega_{S/A}^{(m)}$ and $\qOmega_{S/A}^{(n)}$ by "making elements in each filtration degree $i$ divisible by $[m]_q^i$ and $[n]_q^i$, respectively". It is then reasonable to hope that the map between the modifications is an equivalence after $(q^n-1)$-completion, so that in the limit we get a Habiro descent of $\qOmega_{S/A}$.

However, the filtrations on $\L\eta_{[m/d]_q}$ *do not* glue. To make the idea work, we need the additional datum of a $q$-Hodge filtration on $\qOmega_{S/A}$; and, we won't get a Habiro descent of $\qOmega_{S/A}$, but of $\qHodge_{S/A}$. This is precisely how we'll prove [\[thm:HabiroDescent\]](#thm:HabiroDescent){reference-type="ref" reference="thm:HabiroDescent"}. See the outline at the end of [\[subsec:MainResult\]](#subsec:MainResult){reference-type="ref" reference="subsec:MainResult"}. Also see [\[subsec:qdeRhamHabiroDescent\]](#subsec:qdeRhamHabiroDescent){reference-type="ref" reference="subsec:qdeRhamHabiroDescent"} for a discussion of Habiro descent for $\qOmega_{S/A}$.
:::

Let us now explain the relationship between $\qOmega_{S/A}^{(m)}$ and the $q$-de Rham--Witt complexes. To this end, recall from [@qWitt Proposition ] that we have a map of graded $A[q]/(q^m-1)$-algebras $F_{m/d}\colon \qIW_m\Omega_{S/A}^*\rightarrow \qIW_d\Omega_{S/A}^*$ for all divisors $d\mid m$ (the *Frobenius* on $q$-de Rham--Witt complexes). This satisfies $\d \circ F_{m/d}=(m/d)\circ F_{m/d}$. Therefore, if $\overtilde{F}_{m/d}$ is given by $(m/d)^nF_{m/d}$ in degree $n$, then $$\overtilde{F}_{m/d}\colon \qIW_m\Omega_{S/A}^*\longrightarrow \qIW_d\Omega_{S/A}^*$$ is a map of differential-graded $A[q]/(q^m-1)$-algebras.

::: prop
[]{#prop:TwistedqDeRhamDeformsqDRW label="prop:TwistedqDeRhamDeformsqDRW"} Let $A$ be a perfectly covered $\Lambda$-ring and let $S$ be a smooth $A$-algebra. There's a functorial equivalence of $\IE_\infty$-$A[q]/(q^m-1)$-algebras $$\qOmega_{S/A}^{(m)}/(q^m-1)\overset{\simeq}{\longrightarrow}\qIW_m\Omega_{S/A}\,.$$ Under this identification, the map $\qOmega_{S/A}^{(m)}/(q^m-1)\rightarrow \qOmega_{S/A}^{(d)}/(q^d-1)$ induced by [\[con:TwistedqDeRhamFunctoriality\]](#con:TwistedqDeRhamFunctoriality){reference-type="ref" reference="con:TwistedqDeRhamFunctoriality"} agrees with the map $\overtilde{F}_{m/d}$ above.
:::

::: proof
*Proof sketch.* By [@qWitt Corollary ], for any $N\neq 0$ divisible by $m$ the arithmetic fracture square for $\qIW_m\Omega_{S/A}$ has the the following form: $$\begin{tikzcd}[column sep=0em]
                \qIW_m\Omega_{S/A}\rar\dar["(\gh_{m/d})_{d\mid m}"']\drar[pullback] & \prod_{p\mid N}\prod_{d_p\mid m_p}\left(\Omega_{S/A}\lotimes_{A,\psi^{p^{\smash{v_p(m)}}d_p}}A[q]\right)_p^\complete/\Phi_{d_p}(q^{v_p(m)})\dar["\left(\phi_{p/A}^{v_p(m/d)}\right)_{p\mid N,\,d\mid m}"]\\
                \prod_{d\mid m}\left(\Omega_{S/A}\lotimes_{A,\psi^d}A\bigl[\localise{N},q\bigr]\right)/\Phi_d(q)\rar& \displaystyle\prod_{p\mid N}\prod_{d\mid m}\left(\Omega_{S/A}\lotimes_{A,\psi^d}A[q]\right)_p^\complete\bigl[\localise{p}\bigr]/\Phi_d(q)
            \end{tikzcd}$$ This agrees with the reduction modulo $(q^m-1)$ of the arithmetic fracture square from [\[lem:TwistedqDeRhamFractureSquare\]](#lem:TwistedqDeRhamFractureSquare){reference-type="ref" reference="lem:TwistedqDeRhamFractureSquare"}. Here we note that upon reduction modulo $(q^m-1)$, every occurence of the $q$-de Rham complex $\qOmega_{S/A}$ in [\[lem:TwistedqDeRhamFractureSquare\]](#lem:TwistedqDeRhamFractureSquare){reference-type="ref" reference="lem:TwistedqDeRhamFractureSquare"} can be replaced by $\Omega_{S/A}$. For example, for the $d$^th^ factor in the bottom left corner, reduction modulo $(q^m-1)$ is the same as reduction modulo $\Phi_d(q)$, as $(q^m-1)$ and $\Phi_d(q)$ only differ by a unit in $A[1/N,q]_{\Phi_d(q)}^\complete$. Now $(q-1)$ maps to $0$ under $\psi^d\colon A[q]\rightarrow A[1/N,q]/\Phi_d(q)$, so indeed $\qOmega_{S/A}$ can be replaced by $\Omega_{S/A}$ in that corner. Similar arguments apply to the other corners.

This yields the desired equivalence $\qOmega_{S/A}^{(m)}/(q^m-1)\simeq\qIW_m\Omega_{S/A}$. It's straightforward to check that this equivalence doesn't depend on the choice of $N$ (compare [\[con:TwistedqHodgeFiltration\]](#con:TwistedqHodgeFiltration){reference-type="ref" reference="con:TwistedqHodgeFiltration"} below).

The additional assertion about $\qOmega_{S/A}^{(m)}/(q^m-1)\rightarrow \qOmega_{S/A}^{(d)}/(q^d-1)$ follows similarly by a comparison of arithmetic fracture squares (where we may now choose the same $N$). The only non-trivial step is to check that under the equivalence $(\qIW_{p^\alpha}\Omega_{S/A})_p^\complete\simeq (\Omega_{S/A}\lotimes_{A,\psi^{p^{\alpha}}}A[q]/(q^{p^\alpha}-1))_p^\complete$ the maps $\overtilde{F}_p$ and $\phi_{p/A}$ get identified. This is explained in [@qWitt Corollary ]. ◻
:::

[^1]: If $\psi^m$ is finite (for example, this holds if $A=\IZ$ or more generally if $A$ is a polynomial ring), then $\qOmega_{S/A}\lotimes_{A[q],\psi^m}A[q]$ is already $(q^m-1)$-complete.
