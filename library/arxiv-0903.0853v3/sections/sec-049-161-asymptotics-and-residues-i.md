---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-049-161-asymptotics-and-residues-i
section_title: "Asymptotics and residues (I)"
section_number: 16.1
pages: 80-85
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.972
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:residusI label="subsection:residusI"}

When $\nu=1$, divisor $\Lambda$ reduces to $[\lambda]$ and the above definition coincides with the definition of ${\mathbb A}_{q;1}^{[\lambda;q]}$ in []{#not69 label="not69"} [@zh3], [@rz]. After [@rz], one has $f \in {\mathbb A}_q^{[\lambda]}$ if, and only if, there exists an integer $N \in {\mathbf N}$, a $q$-Gevrey sequence $(c_n)_{n\ge N}$ of order $(-1)$ and a function $h$ holomorphic near $z=0$ such that, for any $z\in S([\lambda],0;|\lambda q^{-N}|)$: $$f(z) = \sum_{n\ge N} ~ \dfrac{c_n}{z-q^{-n}\lambda} + h(z).$$

In the sequel, we shall give a caracterisation of all elements of ${\mathbb A}_{q}^{\Lambda}$ with help of its partial fraction decomposition along divisor $\Lambda$.

::: theo
[]{#theo:fdecomposition label="theo:fdecomposition"} Let $f\in{\mathbb B}^{\Lambda}$. The following assertions are equivalent:

\(i\)

:   One has $f \in {\mathbb A}_{q}^{\Lambda}$.

\(ii\)

:   There exists an integer $N_0$ and $\nu$ sequences $(\alpha_{i,j,n})_{n\ge N_0}$ ($1 \leq i \leq m$, $0 \leq j< \nu_i$) of $q$-Gevrey level $(-\nu)$ and a function $h$ holomorphic at $0 \in {\mathbf C}$ such that the following equality holds over the sector $S(\Lambda,0;|q^{-N_0}\lambda_m|)$: $$\label{eqn:fLambda}
    f(z) = \sum_{n\ge N_0} \sum_{1\le i\le m} \sum_{0\le j<\nu_i}
    \dfrac{\alpha_{i,j,n}}{(z-\lambda_i q^{-n})^{j+1}} + h(z).$$
:::

::: proof
*Proof.* Recall that $\nu := \left |\Lambda \right |\in {\mathbf N}^{*}$. Let $f \in {\mathbb B}^{\Lambda}$. Under assumption [\[hypothese:lambdas\]](#hypothese:lambdas){reference-type="eqref" reference="hypothese:lambdas"}, page about the $\lambda_i$, we can choose []{#pourrefplusloin label="pourrefplusloin"} a real $R>0$ and an integer $N_0$ such that, on the one hand, one has $\left |q^{-N_0}\lambda_m \right |< R < \left |q^{-N_0+1}\lambda_1 \right |$ and, on the other hand, $f$ is defined and analytic in the open sector $S(\Lambda,0;R)$. Therefore, the only possible singularities of $f$ in the punctured disc $0 < \left |z \right |< R$ belong to the half $q$-spirals $\lambda_i q^{-N_0-{\mathbf N}}$, $1 \le i \le m$.\
[**Proof of (i) $\Rightarrow$ (ii):**]{.underline} It will rest on lemmas [\[lemm:poles\]](#lemm:poles){reference-type="ref" reference="lemm:poles"}, [\[lemm:eta\]](#lemm:eta){reference-type="ref" reference="lemm:eta"} and [\[lemm:h\]](#lemm:h){reference-type="ref" reference="lemm:h"}.

::: lemm
[]{#lemm:poles label="lemm:poles"} We keep the above notations $R$, $N_0$, and moreover assume that $f \in {\mathbb A}_q^\Lambda$. Then $f$ has a pole with multiplicity at most $\nu_i$ at each point of the half $q$-spiral $\lambda_i q^{-N_0-{\mathbf N}}$.
:::

::: proof
*Proof.* Let $n \geq N_0$ be an integer. When $z$ tends to $z_{i,n} := \lambda_i q^{-n}$, one has $d_q(z,\Lambda) = \left |1- \dfrac{z}{z_{i,n}} \right |^{\nu_i} \to 0$. Taking $\epsilon := \dfrac{d_q(z,\Lambda)}{2}$ and $N := 0$ in relation [\[eqn:fN\]](#eqn:fN){reference-type="eqref" reference="eqn:fN"}, definition [\[defi:ALambda\]](#defi:ALambda){reference-type="ref" reference="defi:ALambda"}, one finds: $$\left |f(z) \right |< \dfrac{2C}{\left |1-\frac z{z_{i,n}}\right |^{\nu_i}},$$ which allows one to conclude. ◻
:::

Write $P_{i,n}$ the polar part of $f$ at point $\lambda_i q^{-n}$: $$\label{eqn:polaire}
P_{i,n}(z) = \sum_{0\le j<\nu_i} 
\dfrac{\alpha_{i,j,n}}{(z-\lambda_{i} q^{-n})^{j+1}} \cdot$$ We are going to study the growth of coefficients with respect to index $n$ when $n$ goes to infinity. For that, we choose some small $\eta \in \left(0,\frac {\left |q \right |}{1+\left |q \right |}\right)$ so that, putting $r_{i,n} := \left |\lambda_i q^{-n} \right |\eta$, all the open disks []{#not70 label="not70"} $D^\eta_{i,n} := \{z\in{\mathbf C}~ | ~\left |z - \lambda_i q^{-n} \right |<r_{i,n}\}$ ($1 \leq i \leq m$, $n \geq N_0$) are pairwise disjoint. Also write ${{\mathcal C}}^\eta_{i,n} = \partial^+ D^\eta_{i,n}$ the boundary of disk $D^\eta_{i,n}$, with positive orientation.

::: lemm
[]{#lemm:eta label="lemm:eta"} Let ${{\mathcal R}}_N := f(z) - \sum\limits_{k=0}^{N-1} a_n z^n$, the $N$-th remainder of $f$. For all $z \in {{\mathcal C}}^\eta_{i,n}$, one has: $$\label{eqn:RN}
\left |{{\mathcal R}}_N(z) \right |< 
\dfrac{2C}{\eta^\nu}~\left(2A \left |\lambda_i q^{-n} \right |\right)^N
\left |q \right |^{N^2/(2\nu)}~,$$ where $C$ and $A$ are the constants in relation [\[eqn:fN\]](#eqn:fN){reference-type="eqref" reference="eqn:fN"} of definition [\[defi:ALambda\]](#defi:ALambda){reference-type="ref" reference="defi:ALambda"}.
:::

::: proof
*Proof.* Since $\eta < \frac {\left |q \right |}{1+\left |q \right |}$, one has $d_q(z,[\lambda_i]) = \eta$ and $d_q(z,[\lambda_j]) \geq \eta$ for $j \neq i$. One deduces that $d_q(z,\Lambda) \geq \eta^{\max(\nu_1,\ldots,\nu_m)} \geq \eta^\nu$, which allows one to write, taking $\epsilon := \dfrac{\eta^\nu}{2}$ in [\[eqn:fN\]](#eqn:fN){reference-type="eqref" reference="eqn:fN"}: $$\left |{{\mathcal R}}_N(z) \right |< 
\dfrac{2C}{\eta^\nu}~A^N~ \left |q \right |^{N^2/(2\nu)}~ \left |z\right |^N.$$ Relation [\[eqn:RN\]](#eqn:RN){reference-type="eqref" reference="eqn:RN"} follows, using the fact that $\left |z \right |\leq (1+\eta) \left |\lambda_i q^{-n} \right |<
2 \left |\lambda_i q^{-n} \right |$. ◻
:::

We now express the coefficients $\alpha_{i,j,n}$ in [\[eqn:polaire\]](#eqn:polaire){reference-type="eqref" reference="eqn:polaire"} with the help of Cauchy formula in the following way: $$\alpha_{i,j,n} = 
\dfrac{1}{2 {\text{i}}\pi} \oint_{{{\mathcal C}}_{i,n}^\eta} f(z)~(z-\lambda_i q^{-n})^j ~dz,$$ that is, for any integer $N \geq 0$: $$\alpha_{i,j,n}=
\frac1{2{\text{i}}\pi} 
\oint_{{{\mathcal C}}_{i,n}^\eta}{{\mathcal R}}_N(z)~(z-\lambda_i q^{-n})^j ~dz.$$ Taking in account estimation [\[eqn:RN\]](#eqn:RN){reference-type="eqref" reference="eqn:RN"} above entails: $$\left |\alpha_{i,j,n} \right |\leq 
2 C~\eta^{j+1-\nu}~\left |\lambda_i q^{-n} \right |^{j+1}~X^N~Q^{N^2/2},$$ where $X := 2A \left |\lambda_iq^{-n} \right |$ and $Q := \left |q \right |^{1/\nu}$. Relation [\[eqn:minqgevrey\]](#eqn:minqgevrey){reference-type="eqref" reference="eqn:minqgevrey"} implies that, if $X < 1$, then: $$\min_{N\in{\mathbf N}} \bigl(X^N~Q^{N^2/2}\bigr) \leq ~Q^{1/8}~e^{-\frac{\ln^2X}{2\ln Q}},$$ which implies that: $$\left |\alpha_{i,j,n} \right |
\leq 2 C \eta^{j+1-\nu} \,\left |\lambda_i \right |^{j+1}\,
\left |q \right |^{1/(8\nu)-(j+1)n}\,
e^{-\frac{\nu \ln^2 (2 A |\lambda_i q^{-n}|)}{2\ln |q|}},$$ so that all the sequences $(\alpha_{i,j,n})_{n\ge N_0}$ are $q$-Gevrey of level $(-\nu)$. Thus, for each pair $(i,j)$ of indexes, the series: $$S_{i,j}(z) :=\sum_{n\ge N_0} \dfrac{\alpha_{i,j,n}}{(z-\lambda_iq^{-n})^{j+1}}$$ converges normally on each compact subset of the sector $S(\Lambda,0)$.

Last, if $0 < \left |z \right |< R$ and if $z \notin \bigcup\limits_{1\le i\le m}\lambda_iq^{-N_0+{\mathbf N}}$, let us put: $$h(z) := f(z) - \sum_{1\le i\le m} \sum_{0\le j<\nu_i} S_{i,j}(z).$$ From normal convergence of the series $S_{i,j}(z)$ on every compact subset of $S(\Lambda,0)$, we draw: $$\label{eqn:hP}
h(z) = f(z) - \sum_{n\ge N_0} \sum_{1\le i\le m} P_{i,n}(z).$$

::: lemm
[]{#lemm:h label="lemm:h"} The function $h$ represents the germ of an analytic function at $z=0$.
:::

::: proof
*Proof.* Since all non zero singularities of $f$ in the disk $\left |z \right |< R$ are necessarily situated on the union of half $q$-spirals $\bigcup\limits_{1\le i\le m}\lambda_i q^{-N_0+{\mathbf N}}$ and each $P_{i,n}(z)$ represents its polar part at each point $\lambda_iq^{-n}$ of the latter, the function $h$ has an analytic continuation to the punctured disk $0 < \left |z \right |< R$. Moreover, if $\Omega := \bigcup\limits_{n>N_0}{{\mathcal C}}(0;R\left |q \right |^{-n})$ denotes the union of the circles centered at $z=0$ and with respective radii $R\left |q \right |^{-n}$ with $n > N_0$, all the series $S_{i,j}(z)$ converge normally over $\Omega$, and therefore remain bounded on that family of circles. Besides, from proposition [\[prop:BB\]](#prop:BB){reference-type="ref" reference="prop:BB"}, $f$ is also bounded on $\Omega$ because $f\in{\mathbb B}^\Lambda$. It follows that $h$ is bounded on $\Omega$, which entails the analyticity of $h$ at $z=0$. ◻
:::

Combining relations [\[eqn:polaire\]](#eqn:polaire){reference-type="eqref" reference="eqn:polaire"} and [\[eqn:hP\]](#eqn:hP){reference-type="eqref" reference="eqn:hP"}, we get decomposition [\[eqn:fLambda\]](#eqn:fLambda){reference-type="eqref" reference="eqn:fLambda"} of $f$, thus achieving the proof of (i) $\Rightarrow$ (ii).\
[**Proof of (ii) $\Rightarrow$ (i):**]{.underline} It will rest on lemma [\[lemm:reste\]](#lemm:reste){reference-type="ref" reference="lemm:reste"}.

[]{#not71 label="not71"}

::: lemm
[]{#lemm:reste label="lemm:reste"} Let $j\in{\mathbf N}$, $N\in{\mathbf N}$ and write ${{\mathcal R}}_{j,N}$ the rational fraction defined by relation: $$\label{eqn:resteN}
\dfrac{1}{(1-t)^{j+1}} =
\sum_{n=0}^{N-1} \binom{n+j}n ~ t^n + {{\mathcal R}}_{j,N}(t).$$ Let $\delta>0$. If $t\in{\mathbf C}$ satisfies $\left |1-t \right |\geq \delta$, then: []{#not72 label="not72"} $$\label{eqn:RjN}
\left |{{\mathcal R}}_{j,N}(t) \right |< 
C_{j,N}^{\delta,r}~ \dfrac{\left |t \right |^N}{\delta^{j+1}},
\quad 
C_{j,N}^{\delta,r} =
\dfrac{1}{2-r}~
\bigl(\frac{1+r\delta}{r-1}\bigr)^j~
\bigl(\frac{1+r\delta}{1+\delta}\bigr)^N$$ for all $r\in(1,2)$.
:::

::: proof
*Proof.* The relation [\[eqn:RjN\]](#eqn:RjN){reference-type="eqref" reference="eqn:RjN"} being trivially satisfied at point $t = 0$, we assume that $t \neq 0$. Taking the $j$-th derivative for each side of relation $\dfrac{1}{1-t} = \sum\limits_{n=0}^{N+j-1} t^n + \dfrac{t^{N+j}}{1-t}$, one finds: $${{\mathcal R}}_{j,N}(t) =\dfrac{1}{j!}~\bigl(\frac{t^{N+j}}{1-t}\bigr)^{(j)} =
\dfrac{1}{2{\text{i}}\pi}~\oint_{{{\mathcal C}}(t,\rho)}\frac{s^{N+j}}{1-s}~\frac{ds}{(s-t)^{j+1}}~,$$ where ${{\mathcal C}}(t,\rho)$ denotes the positively oriented boundary of the circle centered at $s = t$ and with radius $\rho \left |t\right |$, with $\rho < \left |1 - \dfrac{1}{t} \right |$. One deduces that: $$\label{eqn:Rrho}
\left |{{\mathcal R}}_{j,N}(t) \right |\leq 
\dfrac{(1+\rho)^{N+j}~\left |t \right |^N}
{\bigl(\left |1-t \right |-\rho \left |t\right |\bigr)~\rho^j},$$ where $\rho$ denotes a real number located between $0$ and $\left |1-\dfrac{1}{t} \right |$.

If $\left |1 - t \right |> \delta$, with $t = 1 + Re^{i\alpha}$ ($\alpha\in{\mathbf R}$), one gets: $\left |1-\dfrac{1}{t} \right |\geq 
\dfrac{R}{1+R} > \dfrac{\delta}{1+\delta}$. Choose $\rho := \dfrac{r'\delta}{1+\delta}$ with $r' \in (0,1)$, so that $\left |1-t \right |- \rho \left |t \right |\geq
 \left |1-t \right |(1-r') > (1-r')~\delta$; relation [\[eqn:RjN\]](#eqn:RjN){reference-type="eqref" reference="eqn:RjN"} follows at once (along with lemma [\[lemm:reste\]](#lemm:reste){reference-type="ref" reference="lemm:reste"}) with the help of [\[eqn:Rrho\]](#eqn:Rrho){reference-type="eqref" reference="eqn:Rrho"}, with $\rho := \dfrac{(r-1)~\delta}{1+\delta}$ and $r := r'+1 \in (1,2)$. ◻
:::

We shall now use lemma [\[lemm:reste\]](#lemm:reste){reference-type="ref" reference="lemm:reste"} to prove that (ii) $\Rightarrow$ (i); by linearity, it suffices to check that a series of the form: $$\label{eqn:Salpha}
S(z) := \sum_{n\ge 0}\dfrac{\alpha_n}{(z-\lambda q^{-n})^{j+1}}$$ defines a function in space $A_q^\Lambda$, where $\lambda = \lambda_i$ for some $i\in\{1,2,\ldots,m\}$, $0 \leq j < \nu_i$ and where $(\alpha_n)$ denotes a $q$-Gevrey sequence of order $(-\nu)$: there are $C$, $A > 0$ such that: $$\label{eqn:alphan}
\forall n \in {\mathbf N}~,~
\left |\alpha_n \right |\leq C A^n \left |q\right |^{-\nu n(n-1)/2}.$$

Let $z\in{\mathbf C}^*$ such that $d_q(z,\Lambda) > \epsilon$; we have $d_q(z,[\lambda])^{\nu_i} >\epsilon$, hence $\left |1-\dfrac{z}{\lambda q^{-n}} \right |> \sqrt[\nu_i]\epsilon$. Let $N \in {\mathbf N}$ and apply to each term of the series $S(z)$ formula [\[eqn:resteN\]](#eqn:resteN){reference-type="eqref" reference="eqn:resteN"} with $t = \dfrac{z}{\lambda q^{-n}}$ to obtain formally $S(z) = S_N(z) + R_N(z)$, where one puts: $$S_N(z) :=
\sum_{n\ge 0} \sum_{k=0}^{N-1} \alpha_n \binom{k+j}{k}~
(-\lambda q^{-n})^{-j-1}~\left(\dfrac{z}{\lambda q^{-n}}\right)^k$$ and: $$R_N(z) := \sum_{n\ge 0} \alpha_n~(-\lambda q^{-n})^{-j-1}~
{{\mathcal R}}_{j,N}(\dfrac{z}{\lambda q^{-n}}).$$ Since $(\alpha_n)$ has $q$-Gevrey decay of order $\nu$ (see [\[eqn:alphan\]](#eqn:alphan){reference-type="eqref" reference="eqn:alphan"}), we see that $S_N(z)$ and $R_N(z)$ are normally convergent series on any domain $\Omega$ such that $\inf\limits_{z\in\Omega} d_q(z,[\lambda]) > 0$.

Define: $$\label{eqn:Az}
{{{\mathcal A}}}(z) := \sum_{n\ge 0} \alpha_n~z^n,
\quad
\tilde {{{\mathcal A}}}(z) := \sum_{n\ge 0} \left |\alpha_n \right |~z^n.$$ From relation [\[eqn:alphan\]](#eqn:alphan){reference-type="eqref" reference="eqn:alphan"}, one gets: $$\left |{{{\mathcal A}}}(z) \right |\leq \tilde {{{\mathcal A}}}(\left |z \right |) \leq 
C~\sum_{n\ge 0} \left |q\right |^{-\nu n(n-1)/2}~\left |Az \right |^n <
C~e(Az;{\left |q \right |}^\nu).$$ On the other hand, one can express the series $S_N(z)$ in the following way: $$\label{eqn:an}
S_N(z) = \sum_{n=0}^{N-1} a_n z^n,\quad
a_n := (-\lambda)^{-j-1}\binom{n+j}n~{{{\mathcal A}}}(q^{j+1+n})~\lambda^{-n}~;$$ besides, the relation [\[eqn:RjN\]](#eqn:RjN){reference-type="eqref" reference="eqn:RjN"} implies that, putting $\delta := \sqrt[\nu_i]\epsilon$: $$\label{eqn:RNz}
\left |R_N(z) \right |\leq K_{j,N}^{\delta,r}~\left |z\right |^N,\quad
K_{j,N}^{\delta,r} :=
\dfrac{C_{j,N}^{\delta,r}}{\left |\lambda \right |^{j+1+N}~\delta^{j+1}}~
\tilde{{{\mathcal A}}}(\left |q\right |^{j+1+N})~,$$ with $\tilde{{{\mathcal A}}}(z)$ as in [\[eqn:Az\]](#eqn:Az){reference-type="eqref" reference="eqn:Az"} and $r \in (1,2)$.

To sum up, we have seen that, if $d_q(z,\Lambda) > \epsilon > 0$ and $\delta = \sqrt[\nu_i]\epsilon$, then: $$\left |S(z) - \sum_{n=0}^{N-1} a_n~z^n \right |\leq K_{j,N}^{\delta,r}~\left |z \right |^N,$$ the coefficients $a_n$ and $K_{j,N}^{\delta,r}$ being defined as in [\[eqn:an\]](#eqn:an){reference-type="eqref" reference="eqn:an"} and [\[eqn:RNz\]](#eqn:RNz){reference-type="eqref" reference="eqn:RNz"} respectively. To conclude that $S(z)$ admits $\sum\limits_{n\ge 0} a_n z^n$ as a $q$-Gevrey asymptotic expansion of level $\nu$ in $\Lambda$ at $0$, it only remains to be checked that one can find $C_0>0$, $A_0>0$ with: $$\label{eqn:CA}
\min_{r\in(1,2)} K_{j,N}^{\delta,r} \leq 
\dfrac{C_0}{\epsilon}~A_0^N~\left |q \right |^{N^2/(2\nu)}$$ for all $N\in{\mathbf N}$ and $j=0,\ldots,\nu_i-1$. To do that, note that, after lemma [\[lemm:croissanceqexp\]](#lemm:croissanceqexp){reference-type="ref" reference="lemm:croissanceqexp"} and relation [\[eqn:minqgevrey\]](#eqn:minqgevrey){reference-type="eqref" reference="eqn:minqgevrey"}, one finds: $$\tilde{{{\mathcal A}}}\left(\left |q \right |^{j+1+N}\right) \leq 
C'~\left(\left |q \right |^{\frac{j+1}\nu-\frac12}~A^{\frac1\nu}\right)^N~q^{N^2/(2\nu)}~,$$ where $C'$ denotes a constant independant of $N$; this, along with definition [\[eqn:RNz\]](#eqn:RNz){reference-type="eqref" reference="eqn:RNz"} of $K_{j,N}^{\delta,r}$, entails [\[eqn:CA\]](#eqn:CA){reference-type="eqref" reference="eqn:CA"} and we leave the details to the reader. The proof of theorem [\[theo:fdecomposition\]](#theo:fdecomposition){reference-type="ref" reference="theo:fdecomposition"} is now complete. ◻
:::
