---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis"
section_id: sec-035-162-asymptotics-and-residues-ii
section_title: "Asymptotics and residues (II)"
section_number: 16.2
pages: 85-94
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.98
---
[]{#subsection:residusII label="subsection:residusII"}

After [@rz], for any $f \in {\mathbb A}_q^{[\lambda]}$, the function $z \mapsto F(z) := \theta(-\frac z\lambda)~f(z)$ is analytic in some punctured disk $0 < \left |z \right |< \left |\lambda q^{-N} \right |$, with (at most) a first order $q$-exponential growth when $z$ goes to $0$, and such that its restriction to the $q$-spiral $[\lambda]$ has at most a growth of $q$-Gevrey order $0$[^1]. In order to extend this result to a general divisor $\Lambda$ (with degree $\nu > 1$), we introduce the following definition.

::: defi
[]{#defi:LambdaF label="defi:LambdaF"} Let $F$ be a function defined and analytic in a neighborhood of each of the points of the support of the divisor $\Lambda$ near $0$.

1.  We call *values of $F$ on $\Lambda$ at $0$*, and write $\Lambda F(0)$, the $\nu$ (germs at infinity of) sequences: $$\label{not73}
    \Lambda F(0) :=
    \left\{\left(F^{(j)}(\lambda_i q^{-n})\right)_{n \gg 0} ~:~
    1\le i\le m, 0\le j<\nu_i\right\},$$ where $F^{(j)}$ is the $j$-th derivative of $F$ (with $F^{(0)} = F$) and where \"$n \gg 0$\" means \"$n$ great enough\".

2.  We say that $F$ has *$q$-Gevrey order $k$ along divisor $\Lambda$ at $0$* if all its values are $q$-Gevrey sequences of order $k$.

3.  We write $F \in {\mathbb E}_0^{\Lambda}$ if $F$ is analytic in a []{#not74 label="not74"} neighborhood of $0$ punctured at $0$, has $q$-Gevrey order $\nu$ at $0$ and $q$-Gevrey order $0$ along $\Lambda$ at $0$.
:::

To simplify, we shall write: $$\label{eqn:thetalambda}
\theta_\Lambda(z) := 
\prod_{j=1}^m\left(\theta\left(-\frac z{\lambda_j}\right)\right)^{\nu_j}~.$$ Thus, if $f\in{\mathbb B}^{\Lambda}$, $\theta_\Lambda f$ represents an analytic function in a punctured disk $0 < \left |z \right |< R$.

::: theo
[]{#theo:fF label="theo:fF"} Let $f \in {\mathbb B}^{\Lambda}$ and $F := \theta_\Lambda f$. Then, $f \in {\mathbb A}_{q}^{\Lambda}$ if, and only if, $F \in {\mathbb E}_0^{\Lambda}$.
:::

::: proof
*Proof.* We prove separately the two implications.\
[**Proof of $f \in {\mathbb A}_q^\Lambda \Rightarrow F \in {\mathbb E}_0^\Lambda$:**]{.underline} It will rest on lemma [\[lemm:theta\'\]](#lemm:theta'){reference-type="ref" reference="lemm:theta'"}.

::: lemm
[]{#lemm:theta' label="lemm:theta'"} Let $\lambda \in {\mathbf C}^*$, $k \in {\mathbf N}^*$ and let $g(z) := (\theta_\lambda(z))^k$ for $z \in {\mathbf C}^*$. For $\ell \geq 0$, consider the $\ell$-th derivative $g^{(\ell)}$ of $g$.

1.  The function $g^{(\ell)}$ has $q$-exponential growth of order $k$ both at $0$ and infinity.

2.  If $\ell <  k$, then $g^{(\ell)}(\lambda q^{-n}) = 0$ for all $n\in{\mathbf N}$; else, $\bigl(g^{(\ell)}(\lambda q^{-n})\bigr)_{n\ge 0}$ is a $q$-Gevrey sequence of order $k$.

3.  Let $n \in {\mathbf Z}$ and put $u(z) := \dfrac{g(z)}{(z-\lambda q^{-n})^k}$ for all $z \in {\mathbf C}^* \setminus \{\lambda q^{-n}\}$. Then $u$ has an analytic continuation at $\lambda q^{-n}$, with: $$\label{eqn:uell}
    u^{(\ell)}(\lambda q^{-n}) = \dfrac{(\ell+k)!}{k!}~g^{(\ell+k)}(\lambda q^{-n}).$$ In particular: $$\label{eqn:u0}
    u(\lambda q^{-n}) =
    (-1)^{(n-1)k}~(q^{-1};q^{-1})_\infty^{3k}~\bigl(\frac1\lambda\bigr)^k~q^{kn(n+1)/2}~,$$ []{#not75 label="not75"} where $(q^{-1};q^{-1})_\infty = \prod\limits_{r\ge 0}(1-q^{-r-1})$ ($q$-Pochhammer symbol).
:::

::: proof
*Proof.* Writing $g^{(\ell)}$ as the sum of a power series in $z$ and one in $\frac{1}{z}$, one draws from lemma [\[lemm:croissanceqexp\]](#lemm:croissanceqexp){reference-type="ref" reference="lemm:croissanceqexp"} assertion (1), because derivation does not affect the $q$-Gevrey character of a series. Assertion (2) is obvious.

The function $u$ can be analytically continuated at $\lambda q^{-n}$, because $\theta_\lambda$ has a simple zero at each point of the $q$-spiral $[\lambda]$; formula [\[eqn:uell\]](#eqn:uell){reference-type="eqref" reference="eqn:uell"} comes by differentiating $(\ell+k)$ times the equality $g(z) = u(z)(z-\lambda q^{-n})^k$, while [\[eqn:u0\]](#eqn:u0){reference-type="eqref" reference="eqn:u0"} follows from a direct evaluation using Jacobi's triple product formula [\[eqn:tripleproduit\]](#eqn:tripleproduit){reference-type="eqref" reference="eqn:tripleproduit"}. ◻
:::

We now come to the proof of the direct implication; that is, we assume condition (ii) of theorem [\[theo:fdecomposition\]](#theo:fdecomposition){reference-type="ref" reference="theo:fdecomposition"}. Since $\theta_\Lambda h\in{\mathbb E}_0^\Lambda$, by linearity, we just have to check that the series $S(z)$ defined by relation [\[eqn:Salpha\]](#eqn:Salpha){reference-type="eqref" reference="eqn:Salpha"} satisfies $\theta_\Lambda S\in{\mathbb E}_0^\Lambda$. To that end, put $T(z) := \theta_\Lambda(z)~S(z)$ for all $t \in {\mathbf C}^* \setminus \lambda q^{-{\mathbf N}}$; this clearly has an analytic continuation to ${\mathbf C}^*$. On the other hand, $T^{(\ell)}(\lambda_{i'}q^{-n}) = 0$ for all $i'\neq i$, $\ell < \nu_{i'}$ and $n\in{\mathbf Z}$.

In order to evaluate $T^{(\ell)}(\lambda q^{-n})$, put $\Lambda' := \Lambda-(j+1)[\lambda]$ and: $$T_0(z) :=
\sum_{n\ge 0}\alpha_n~
\dfrac{(\theta_\lambda(z))^{j+1}}{(z-\lambda q^{-n})^{j+1}};$$ one has $T(z) = \theta_{\Lambda'}(z)~T_0(z)$, where $T_0$ is analytic on ${\mathbf C}^*$. First note that, if $\ell < \nu_i - j - 1$, one has $T^{(\ell)}(\lambda q^{-n}) = 0$ for all $n \in{\mathbf N}$; when $\nu_i - j - 1 \leq \ell < \nu_i$, using relation [\[eqn:uell\]](#eqn:uell){reference-type="eqref" reference="eqn:uell"}, we get: $$T^{(\ell)}(\lambda q^{-n}) = \alpha_n~
\sum_{k=0}^{\ell-\nu_i+j+1} \binom{\ell}k~ \theta_{\Lambda'}^{(\ell-k)}(\lambda q^{-n})~
\dfrac{(k+j+1)!}{(j+1)!}~ g^{(k+j+1)}(\lambda q^{-n}),$$ where $n \in {\mathbf N}$, $g = (\theta_\lambda)^{j+1}$. Taking in account assertions (1) and (2) of lemma [\[lemm:theta\'\]](#lemm:theta'){reference-type="ref" reference="lemm:theta'"}, the sequences $(\theta_{\Lambda'}^{(\ell-k)}(\lambda q^{-n}))_{n\ge 0}$ and $(g^{(k+j+1)}(\lambda q^{-n}))_{n\ge 0}$ respectively have $q$-Gevrey order $(\nu-j-1)$ and $(j+1)$, which implies that $(T^{(\ell)}(\lambda q^{-n}))_{n\ge 0}$ is bounded above by a geometric sequence, for $(\alpha_n)_{n\ge 0}$ has $q$-Gevrey order $(-\nu)$.

Moreover, like $\theta_\Lambda$, the function $T$ has $q$-exponential growth of order $\nu$ at $0$. Indeed, let $a \in (1,\left |q \right |)$ and put $\delta := \min\limits_{\left |z \right |=a}d_q(z,[1])$; one has $\delta>0$, so that: $$\label{eqn:Sbornee}
\max_{\left |z \right |=a|\lambda q^{-k}|}|S(z)| \leq
\dfrac{1}{\delta~\left |\lambda\right |} \sum_{n\ge 0} \left |\alpha_n q^n \right |
< \infty.$$ This shows that $S(z)$ stays uniformly bounded over the family of circles centered at $0$ and such that each one goes through a point of the $q$-spiral with basis $a\lambda$. It follows first that the restriction of function $T$ to the circles has $q$-exponential growth of order $\nu$ at $0$; then that function $T$ itself has such growth. To summarize, we see that $T \in {\mathbb E}_{0}^\Lambda$, whence $F \in {\mathbb E}_0^\Lambda$.\
[**Proof of $F \in {\mathbb E}_0^\Lambda \Rightarrow f \in {\mathbb A}_q^\Lambda$:**]{.underline} It will rest on lemma [\[lemm:thetamin\]](#lemm:thetamin){reference-type="ref" reference="lemm:thetamin"}, which gives a minoration on $\theta$ as in lemma [\[lemm:thetamin0\]](#lemm:thetamin0){reference-type="ref" reference="lemm:thetamin0"}.

::: lemm
[]{#lemm:thetamin label="lemm:thetamin"} Let $a > 0$ and $k \in {\mathbf Z}$. Then: $$\label{eqn:thetamin}
\min_{\left |z \right |=a\left |q \right |^{-k}} \left |\theta(z) \right |\geq  
\dfrac{\left |(q^{-1};q^{-1})_\infty \right |}
{(\left |q \right |^{-1};\left |q \right |^{-1})_\infty}~
\left |\theta(-a;\left |q \right |) \right |~a^{-k}~ \left |q \right |^{k(k-1)/2}.$$
:::

::: proof
*Proof.* Let $z \in {\mathbf C}$ be such that $\left |z \right |=a\left |q \right |^{-k}$. From a minoration of each factor of the triple product formula [\[eqn:tripleproduit\]](#eqn:tripleproduit){reference-type="eqref" reference="eqn:tripleproduit"}, we get:

$$\begin{aligned}
\min_{\left |z \right |=a\left |q \right |^{-k}} \left |\theta(z) \right |& \geq & 
\left |(q^{-1};q^{-1})_\infty \right |
\prod_{n\ge  0} \left |1-a\left |q \right |^{-n-k}\right |
\left\vert1-\dfrac{\left |q \right |^{-n-1}}{a\left |q \right |^{-k}}\right\vert \\ 
& = & 
\dfrac{\left |(q^{-1};q^{-1})_\infty \right |}{(\left |q \right |^{-1};\left |q \right |^{-1})_\infty}~
\left |\theta(-a\left |q \right |^{-k};\left |q \right |) \right |,
\end{aligned}$$ yielding relation [\[eqn:thetamin\]](#eqn:thetamin){reference-type="eqref" reference="eqn:thetamin"}. ◻
:::

Now we assume $F \in {\mathbb E}_0^\Lambda$. We put $f := \dfrac{F}{\theta_\Lambda}$ and keep the notations $R$, $N_0$ introduced at the beginning of the proof of the theorem (page ); also, we choose $a \in \left(\left |\lambda_m \right |,R\right)$. According to relation [\[eqn:thetamin\]](#eqn:thetamin){reference-type="eqref" reference="eqn:thetamin"}, there is $C > 0$ and $\mu > 0$ such that, if $\left |z \right |= a q^{-k}$ and $k \geq N_0$, then $\left |f(z) \right |\leq C \left |z \right |^\mu$; that is, $f$ has moderate growth at $0$ on the circles $\left |z \right |= a \left |q \right |^{-k}$, $k \geq N_0$.

Partial fraction decomposition of $f$ at each point of $\Lambda$ contained in the punctured disk $0 < \left |z\right |< R$, will produce an expression of the form [\[eqn:fLambda\]](#eqn:fLambda){reference-type="eqref" reference="eqn:fLambda"}, in which the coefficients $\alpha_{i,j,n}$ have $q$-Gevrey order $(-\nu)$. Indeed, let: $$F_{i,k,n} := \dfrac{F^{(k)}(\lambda_iq^{-n})}{k!},\quad
\Theta_{i,k,n} := \dfrac{\theta_\Lambda^{k+\nu_i}(\lambda_iq^{-n})}{(k+\nu_i)!};$$ then: $$\alpha_{i,\nu_i-1,n} = \dfrac{F_{i,0,n}}{\Theta_{i,0,n}}~,\quad
\alpha_{i,\nu_i-2,n} = \dfrac{F_{i,1,n}-\alpha_{i,\nu_i-1,n}~\Theta_{i,1,n}}
{\Theta_{i,0,n}}~,\quad \ldots,$$ $$\alpha_{i,0,n} = 
\dfrac{F_{i,\nu_i-1,n}-\sum_{k=1}^{\nu_i-1}\alpha_{i,\nu_i-k,n}~\Theta_{i,\nu_i-k,n}}
{\Theta_{i,0,n}} \cdot$$ According to relation [\[eqn:u0\]](#eqn:u0){reference-type="eqref" reference="eqn:u0"}, one finds: $$\Theta_{i,0,n}=
(q^{-1};q^{-1})_\infty^{3\nu_i}~(-\lambda_iq^{-n})^{-\nu_i}~
\theta_{\Lambda_i'}(\lambda_i)~
\prod_{j=1}^m
\left(-\dfrac{\lambda_j}{\lambda_i}\right)^{n\nu_j}~q^{\nu n(n-1)/2}.$$ Since $(F_{i,0,n})_{n\ge N_0}$ has $q$-Gevrey order $0$, it follows that the sequence $(\alpha_{i,\nu_i-1,n})_{n\ge N_0}$ has $q$-Gevrey order $(-\nu)$. As for the other coefficients $\alpha_{i,j,n}$, $0 \leq j < \nu_i-1$, since the sequences $(\Theta_{i,j,n})_{n\ge N_0}$ all have $q$-Gevrey order $\nu$ (see lemma [\[lemm:theta\'\]](#lemm:theta'){reference-type="ref" reference="lemm:theta'"}), one successively shows that the sequences $(\alpha_{i,\nu_i-2,n})_{n\ge N_0}$, $\ldots$, $(\alpha_{i,0,n})_{n\ge N_0}$ all have $q$-Gevrey order $(-\nu)$.

Last, note that after [\[eqn:Sbornee\]](#eqn:Sbornee){reference-type="eqref" reference="eqn:Sbornee"}, the function $P$ defined by: $$P(z) := \sum_{n\ge N_0} \sum_{1\le i\le m} \sum_{0\le j<\nu_i}
\dfrac{\alpha_{i,j,n}}{(z-\lambda_iq^{-n})^{j+1}}$$ is uniformly bounded over the family of circles $\left |z \right |= a \left |q \right |^{-k}$, $k \in {\mathbf Z}$ if $a \notin \bigcup\limits_{1\le i\le m}[\lambda_i]$. Since $f\in{\mathbb B}^\Lambda$, from proposition [\[prop:BB\]](#prop:BB){reference-type="ref" reference="prop:BB"} we deduce that $h(z) := f(z) - P(z)$ is analytic in some open disk $0 < \left |z \right |< R$ and remains bounded over these circles, which implies that $h$ is holomorphic in a neighborhood of $0$, achieving the proof of the converse implication and of theorem [\[theo:fdecomposition\]](#theo:fdecomposition){reference-type="ref" reference="theo:fdecomposition"}. ◻
:::

# $q$-Gevrey theorem of Borel-Ritt and flat functions {#section:BorelRitt}

The classical theorem of Borel-Ritt [@HS chap. XI, §1] says that any formal power series is the asymptotic expansion, in Poincaré's sense, of some germ of analytical function in a sector of the complex plane with vertex $0$ (the Gevrey version for differential equations is to be found in §2 of the same chapter of *loc. cit.*). We are going to prove a $q$-Gevrey version of that theorem involving the set of functions ${\mathbb A}_q^\Lambda$ and then give a characterization of the corresponding flat functions.

## From a $q$-Gevrey power series to an entire function {#subsection:qGevreytoentire}

As before, let $\Lambda = \sum\limits_{1\le i\le m}\nu_i[\lambda_i]$ be a divisor and let $\theta_\Lambda$ be the associated theta function given by the relation [\[eqn:thetalambda\]](#eqn:thetalambda){reference-type="eqref" reference="eqn:thetalambda"}.

::: lemm
[]{#lemm:thetatronque label="lemm:thetatronque"} Consider the Laurent series expansion $\sum\limits_{n\in{\mathbf Z}} \beta_n~z^n$ of $\theta_\Lambda$.

1.  For all $(k, r) \in {\mathbf Z}^2$, one has: $$\label{eqn:beta}
    \beta_{k\nu+r} = \left(\frac L{q^r}\right)^k~q^{-k(k+1)\nu/2}~\beta_r~.$$ (The constant $L$ is defined at the beginning of the proof.)

2.  For all $n \in {\mathbf Z}$, write $T_n$ the function defined by: $$T_n: = \theta_{\Lambda,n}(z) = \sum_{\ell\le n} \beta_\ell~z^\ell~.$$ If $j\in\{1,\ldots,m\}$, one has: $$\label{eqn:thetatronque}
     K_{n,j} := \sup_{z\in[\lambda_j]} \left |z^{-n}~T_n(z) \right |< +\infty~.$$
:::

::: proof
*Proof.* From the fundamental relation $\theta(qz) = qz\theta(z)$, one draws: $$\theta_\Lambda(qz) = L~z^\nu~\theta_\Lambda(z),\quad
L := \prod_{j=1}^m\left(-\dfrac{q}{\lambda_j}\right)^{\nu_j}~,$$ whence, for all $k \in {\mathbf Z}$: $$\theta_\Lambda(q^kz) = L^k~z^{k\nu}~q^{k(k-1)\nu/2}~\theta_\Lambda(z)~.$$ The relation [\[eqn:beta\]](#eqn:beta){reference-type="eqref" reference="eqn:beta"} follows immediately.

Since $z^{-n}~T_n(z)$ represents an analytic function over ${\mathbf C}^* \cup \{\infty\}$, one obtains [\[eqn:thetatronque\]](#eqn:thetatronque){reference-type="eqref" reference="eqn:thetatronque"} by noticing that, if $z \in [\lambda_j]$, then: $$T_n(z) = -\sum_{\ell>n}\beta_\ell~z^\ell~,$$ which implies that $z^{-n}~T_n(z)$ tends to zero as $z$ tends $0$ along the half-spiral $\lambda_i q^{-{\mathbf N}}$. ◻
:::

Consider a $q$-Gevrey series $\hat f = \sum\limits_{n\ge 0} a_n z^n \in {{\mathbf C}[[z]]}_{q;1/\nu}$ with order $1/\nu$ and, for all $\ell \in {\mathbf Z}$, put $c_\ell := \sum\limits_{n\ge 0}a_n\beta_{\ell-n}$. Set $\ell := k \nu + r$ with $k \in {\mathbf Z}$ and $r \in {\mathbf Z}$, and write: $$c_\ell = \sum_{j=0}^{\nu - 1} \sum_{m \ge 0} a_{m \nu + j}\,\beta_{(k-m)\nu+(r-j)}.$$ As we shall see now, the above infinie series converges when the integer $-\ell$ is large enough. Indeed, using relation [\[eqn:beta\]](#eqn:beta){reference-type="eqref" reference="eqn:beta"}, one gets: $$\beta_{(k-m)\nu+(r-j)} = (Lq^{-r})^{k} \, q^{-k(k+1)\nu/2}\,q^{kj} \,
\left(\frac{q^{r-j+k\nu}}L\right)^m \, q^{-m(m-1)\nu/2}.$$ Since $\hat f$ has $q$-Gevrey order $1/\nu$, there exists $C_1 > 0$, $A_1 > 0$ such that $|a_n| \le C_1\,A_1^n\,|q|^{n(n-1)/(2\nu)}$ for all $n\in{\mathbf N}$. One has: $$\begin{aligned}
\left |a_{m\nu+j}\,\beta_{(k-m)\nu+(r-j)} \right |&\leq \\
C_1 (|L||q|^{-r})^{k} \, & |q|^{-k(k+1)\nu/2} \, (|q|^k A_1)^{j} \,
|q|^{j(j-1)/(2\nu)} \left(\frac{|q|^{r+k\nu+(\nu-1)/2}}{|L|A_1^{-\nu}}\right)^m\,.
\end{aligned}$$ Therefore, if we set: $$C_2 := \sum_{j=0}^{\nu-1} A_1^{j} |q|^{j(j-1)/(2\nu)},$$ then we find ($\ell = k \nu + r$): $$|c_\ell| \leq C_1\,C_2\,(|Lq^{-r}|)^k\,|q|^{-k(k-1)\nu/2}
\sum_{m\geq 0} \left(\frac{|q|^{\ell+(\nu-1)/2}}{|L|A_1^{-\nu}}\right)^m\,.$$ It is easy to see that the last series converges if $|q|^{\ell+(\nu-1)/2} < |L| A_1^{-\nu}$; moreover, when $\ell\to-\infty$, the sequence $(c_\ell)$ is $q$-Gevrey of level $(-\nu)$.

::: prop
[]{#prop:ftheta label="prop:ftheta"} Let $\hat f := \sum\limits_{n\ge 0} a_nz^n \in {{\mathbf C}[[z]]}_{q;1/\nu}$ and let $N_0$ be a negative integer such that any series defining $c_\ell$ converges for $\ell \leq N_0$. Let $F(z) := \sum\limits_{\ell\le N_0}c_\ell z^\ell$. Then, $F\in E_0^\Lambda$.
:::

::: proof
*Proof.* Since $(c_\ell)$ is a $q$-Gevrey sequence of order $(-1/\nu)$ for $\ell \to -\infty$, the sum $F$ represents an analytic function in ${\mathbf C}^* \cup \{\infty\}$, with $q$-exponential growth of order $\nu$ at zero.

We are left to estimate $F(z)$ and its derivatives along the spirals $[\lambda_j]$ belonging to the divisor $\Lambda$. Taking in account relation [\[eqn:beta\]](#eqn:beta){reference-type="eqref" reference="eqn:beta"}, one has: $$T_{-n-k\nu}(z) = (Lz^\nu)^{-k}~q^{-k(k-1)\nu/2}~T_{-n}(q^kz).$$ Therefore, when $z\in [\lambda_j]$, relation [\[eqn:thetatronque\]](#eqn:thetatronque){reference-type="eqref" reference="eqn:thetatronque"} allows writing $F(z)$ in the following form: $$F(z) = \sum_{k\ge
  0}\sum_{n=0}^{\nu-1}a_{k\nu+n}~z^{k\nu+n}~T_{N_0-k\nu-n}(z),$$ and also: $$\label{eqn:FT}
F(z) = \sum_{n=0}^{\nu-1}z^n\sum_{k\ge 0}L^{-k}a_{k\nu+n}~q^{-k(k-1)\nu/2}~T_{N_0-n}(q^kz).$$ One deduces that $F$ has moderate growth when $z \to 0$ along spirals $[\lambda_j]$ belonging to the divisor $\Lambda$.

As for the derivatives $F^{(\ell)}$, along each spiral $[\lambda_j]$, with $\ell<\nu_j$, one may proceed all the same: the function $T_{n}^{(\ell)}$ is indeed bounded over $[\lambda_j]$ for all $\ell < \nu_j$ and one checks that relation [\[eqn:FT\]](#eqn:FT){reference-type="eqref" reference="eqn:FT"} remains true up to order $\ell$, that is, if $z\in[\lambda_j]$: $$F^{(\ell)}(z) =
\sum_{n=0}^{\nu-1} \sum_{k\ge 0}
L^{-k}a_{k\nu+n}~q^{-k(k-1)\nu/2}~\bigl[z^n~T_{N_0-n}(q^kz)\bigr]^{(\ell)}.$$ ◻
:::

## The $q$-Gevrey theorem of Borel-Ritt {#subsection:qGevreyBorelRitt}

The main result of this paragraph is the following[^2].

::: theo
[]{#theo:BorelRitt label="theo:BorelRitt"} The mapping $J$ sending an element $f$ to its asymptotic expansion is a surjective linear map from the ${\mathbf C}$-vector space ${\mathbb A}_{q}^{\Lambda}$ to the ${\mathbf C}$-vector space ${{\mathbf C}[[z]]}_{q;1/\nu}$.
:::

::: proof
*Proof.* Let $\hat f = \sum\limits_{n\ge 0}a_nz^n$ be a $q$-Gevrey series of order $1/\nu$ and let $F$ be the function defined in proposition [\[prop:ftheta\]](#prop:ftheta){reference-type="ref" reference="prop:ftheta"}. Maybe at the cost of taking a smaller $N_0$, we may assume that formula [\[eqn:FT\]](#eqn:FT){reference-type="eqref" reference="eqn:FT"} remains true for all $z \in {\mathbf C}^*$; this being granted, one has: $$\label{eqn:FTa}
F(z) = \sum_{\ell\ge 0}a_\ell~z^\ell~T_{N_0-\ell}(z)~.$$ Put $f := \dfrac{F}{\theta_\Lambda}$, so that $f \in {\mathbb A}_{q}^{\Lambda}$, after theorem [\[theo:fF\]](#theo:fF){reference-type="ref" reference="theo:fF"}. We are going to prove that $f$ admits $\hat f$ as an asymptotic expansion. To that aim, it is enough to show that, if $\lambda \notin \Lambda$, one has: $$\label{eqn:fell}
\lim_{n\to+\infty}f^{(\ell)}(\lambda q^{-n}) = \ell!~a_\ell$$ for any integer $\ell \geq 0$.

Since $\left |T_{N_0-n}(z) \right |\leq e_\Lambda(z)$ and $\left |\theta_\Lambda(z) \right |\sim e_\Lambda(z)$ (see lemma [\[lemm:thetamin\]](#lemm:thetamin){reference-type="ref" reference="lemm:thetamin"}), relation [\[eqn:FTa\]](#eqn:FTa){reference-type="eqref" reference="eqn:FTa"} immediately leads us to the limit [\[eqn:fell\]](#eqn:fell){reference-type="eqref" reference="eqn:fell"} for $\ell =0$. If $\ell \geq
1$, one has: $$f^{(\ell)}(z) = \sum_{n\ge 0} \sum_{j=0}^\ell 
a_n~\binom nj~\frac{j!}{(\ell-j)!}~z^{n-j}~
\left[\dfrac{T_{N_0-n}(z)}{\theta_\Lambda(z)}\right]^{(\ell-j)}~.$$ Through direct estimates, one gets the limit [\[eqn:fell\]](#eqn:fell){reference-type="eqref" reference="eqn:fell"} (omitted details are left to the reader). ◻
:::

The theorem [\[theo:BorelRitt\]](#theo:BorelRitt){reference-type="ref" reference="theo:BorelRitt"} can also be interpreted with help of interpolation of a $q$-Gevrey sequence by entire functions at points in a geometric progression. Indeed, if $f \in {\mathbb A}_q^\Lambda$ is asymptotic to the $q$-Gevrey series $\sum\limits_{k\ge  0}a_kz^k$ of level $\nu$, then, from the decomposition [\[eqn:fLambda\]](#eqn:fLambda){reference-type="eqref" reference="eqn:fLambda"}, one draws: $$a_k = \sum_{n\ge N_0}\sum_{1\le i\le m}\sum_{0\le j<\nu_i}(-1)^{j+1}~
\binom{k+j}j~\dfrac{\alpha_{i,j,n}}{(\lambda_iq^{-n})^{k+j+1}}+h_k~,$$ where $h_k$ denotes the coefficient of $z^k$ in the Taylor series of $h$. Put: $$f_{i,j}(z) := \sum_{n\ge N_0}\alpha_{i,j,n}~z^n~;$$ then: $$\label{eqn:afij}
a_k = \sum_{1\le i\le m}\sum_{0\le j<\nu_i}
\binom{k+j}j~\dfrac{(-1)^{j+1}}{\lambda_i^{k+j+1}}~f_{i,j}(q^{k+j+1})+h_k~.$$

::: coro
[]{#coro:interpol label="coro:interpol"} Let $(a_n)$ be a $q$-Gevrey sequence of order $\nu$ and let $\Lambda = \sum\limits_{1\le i\le m}\nu_i[\lambda_i]$ be a divisor of degree $\nu := \nu_1 + \cdots + \nu_m$. Then, there exists $\nu$ entire functions $A_{i,j}$, $1 \leq i \leq m$, $0 \leq j < \nu_i$ satisfying the following properties:

1.  Each function $A_{i,j}$ has $q$-exponential growth of order (at most) $\nu$ at infinity.

2.  There exists $C>0$, $A>0$ such that, for all $n\in{\mathbf N}$: $$\label{eqn:interpol2}
    \left |a_n - 
    \sum_{1\le i\le m} \sum_{0\le j<\nu_i}
    \binom{n+j}j~\dfrac{(-1)^{j+1}}{\lambda_i^{n+j+1}}~A_{i,j}(q^{n+j+1})\right |< CA^n~.$$
:::

::: proof
*Proof.* The functions $A_{i,j}$ are defined by replacing $N_0$ by $\max(0,N_0)$ in definition [\[eqn:afij\]](#eqn:afij){reference-type="eqref" reference="eqn:afij"}; one then uses relation [\[eqn:afij\]](#eqn:afij){reference-type="eqref" reference="eqn:afij"} to get the bounds [\[eqn:interpol2\]](#eqn:interpol2){reference-type="eqref" reference="eqn:interpol2"}. ◻
:::

Note that if $\Lambda$ is solely made of simple spirals ($\nu_i = 1$), then corollary [\[coro:interpol\]](#coro:interpol){reference-type="ref" reference="coro:interpol"} spells as follows: $$\left |a_n + \sum_{1\le i\le \nu}{\lambda_i^{-n-1}}~A_{i}(q^{n+1}) \right |< C A^n~,$$ where $C>0$, $A>0$ and where the $A_i$ are $\nu$ entire functions with $q$-exponential growth of order at most $\nu$ at infinity. In other words, one can interpolate a $q$-Gevrey sequence of order $\nu$, up to a sequence with at most geometric growth, by $\nu$ entire functions on a half-spiral $\lambda q^{\mathbf N}$.

[^1]: That is, there exists constants $C,A > 0$ such that, for any integer $n \gg 0$, one has $\left |F(q^{-n}\lambda) \right |\leq CA^n$.

[^2]: Theorem [\[theo:BorelRitt\]](#theo:BorelRitt){reference-type="ref" reference="theo:BorelRitt"} is proved with the help of theorem [\[theo:fF\]](#theo:fF){reference-type="ref" reference="theo:fF"}, where we gave conditions for a function to have a certain type Taylor expansion; here, we deal with the *surjectivity* of the "Taylor expansion mapping".
