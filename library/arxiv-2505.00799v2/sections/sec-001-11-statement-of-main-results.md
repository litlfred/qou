---
doc_id: arxiv-2505.00799v2
doc_title: "Quantum Modular Forms and Resurgence"
section_id: sec-001-11-statement-of-main-results
section_title: "Statement of Main Results"
section_number: 1.1
pages: 3-7
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.869
latex_coverage_ratio: 0.992
doc_brief: "Quantum Modular Forms and Resurgence — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
Before we give the general statement of Theorem [\[thm: Main\]](#thm: Main){reference-type="ref" reference="thm: Main"}, we highlight corollaries in some key special cases which correspond to families of quantum modular forms generalizing Zagier's original examples. We note for the reader that the definitions of various terms from the theory of resurgence are deferred until Section 2.1 for ease of exposition.

The first example we consider originally appeared in work of Lawrence and Zagier [@lawrence-zagier] and was subsequently named Example 4 in [@zagier-quantum]. This example was born out of consideration of the Witten--Reshetikhin--Turaev (WRT) invariants of 3-manifolds. Once a manifold has been fixed, this collection of invariants define a function from roots of unity to $\mathbb{C}$. In the case where the 3-manifold is the Poincaré homology sphere, Lawrence and Zagier showed that this function, after suitable rescaling, is a quantum modular form.

Moreover, they proved that there exists a $q$-series converging for $|q|<1$ which recovers (up to the same rescaling) the associated WRT invariants by taking the limiting values as $q$ tend to roots of unity radially. This function $\widetilde{\Theta}_+(q)$ has coefficients given by $$\chi_+(n) := \begin{cases}
    (-1)^{\lfloor n/30\rfloor} & \text{if } (n, 6) = 1 \text{ and } n \equiv \pm 1 \,\,({\rm mod}\,\,{5}),\\
    0 & \text{otherwise,}
 \end{cases}$$ so that $$\widetilde{\Theta}_+(q) = \sum_{n=1}^\infty \chi_+(n)q^{n^2/120}.$$ This $q$-series bears a strong resemblance to the weight $3/2$ modular form $$\Theta_+(z) := \sum_{n=1}^\infty n\chi_+(n)q^{n^2/120}, \quad \quad (q = e^{2\pi i z}, z \in \mathbb{H}).$$ One can view $\Theta_+(z)$ as essentially a "half $q$-derivative\" of $\widetilde{\Theta}_+$. This relationship was made precise by extending the notion of an Eichler integral (see Section [\[subsec: modular\]](#subsec: modular){reference-type="ref" reference="subsec: modular"} or[@eichler; @shimura; @manin] for more details) of a cusp form to the half-integer weight case.

In [@zagier-quantum], other Eichler integrals of cusp forms were given as Examples 2 and 3 of quantum modular forms on $\mathbb{Q}$, illustrating a more general phenomenon. In [@bringmann-rolen], Bringmann and the second author proved that this procedure produces quantum modular forms when one starts with a half-integral weight cusp form.

Extending work of Bringmann and the second author which established the quantum modularity of Eichler integrals, we use techniques from resurgence to prove that these Eichler integrals are in fact holomorphic quantum modular forms. The definition of an Eichler integral is given in Section [\[subsec: modular\]](#subsec: modular){reference-type="ref" reference="subsec: modular"}, and here $\chi_{-4}(n) := \left( \frac{-4}{n}\right)$ denotes the Kronecker symbol.

::: cor
[]{#cor: eichler label="cor: eichler"} Let $\tilde{f}(z)$ be the Eichler integral of a cusp form of weight $k \in \frac{1}{2} + \mathbb{N}$ for $\Gamma_0(N)$, where $4 \mid N$. For each $\gamma =\begin{psmallmatrix} a & b \\ c & d \end{psmallmatrix} \in \Gamma_0(N)$, define $$\begin{aligned}
    \tilde{h}_\gamma(z):= \tilde{f}(z)  -  \chi_{-4}(d)\tilde{f}|_{2-k}\gamma(z). 
\end{aligned}$$ Then the following are true.

1.  The function $\tilde{h}_\gamma(z)$ has an analytic continuation to $\mathbb{C}_\gamma$.

2.  We have the integral representation $$\displaystyle{\tilde{h}_\gamma(z) = \frac{(-2\pi i)^{k-1}}{\Gamma(k-1)} \int_{-d/c}^{i\infty} f(\tau)\left(\tau-z \right)^{k-2}\;d\tau},$$ where both sides are defined, and the path of integration avoids the branch cut.
:::

We note that this corollary ties the half-integral weight case more directly to the integral weight case; for an Eichler integral of an integral weight cusp form, the expression in *(2)* is the corresponding period polynomial. We show this relationship explicitly in Section [\[sec: corollaries\]](#sec: corollaries){reference-type="ref" reference="sec: corollaries"}.

We also remark that related results were previously attained for specific families of Eichler integrals of weight $1/2$ in [@gukov-marino-putrov; @andersen-mistegard; @3d-modularity; @hanetal; @bringmann-nazaroglu].

Looking at another family of quantum modular forms, we recall Example 1 from [@zagier-quantum]. The starting point is the function $\sigma$ from Ramanujan's Lost Notebook: $$\sigma(q) := \sum_{n=0}^\infty \frac{q^{n(n+1)/2}}{(1+q)(1+q^2)\cdots(1+q^n)}, \quad \quad (|q|<1).$$ This function has a natural "companion\" $\sigma^*$ defined instead for $|q|>1$.

The function $\sigma(q)$ garnered considerable interest following several conjectures of Andrews [@andrews]. Notably, work of Andrews, Dyson, and Hickerson [@andrews-dyson-hickerson] expressed $\sigma$ and $\sigma^*$ as indefinite theta series, and work of Cohen [@cohen] realized coefficients of $\sigma$ and $\sigma^*$ as the Dirichlet coefficients of an Artin $L$-function. Moreover, authors of both papers established that $\sigma$ has a $q$-series expansion that converges not only for $|q|<1$, but is finite whenever $q$ is a root of unity, leading to a natural definition of $\sigma(e^{2\pi i x})$ for $x \in \mathbb{Q}$. With the addition of a phase factor, we define $$f(x) := q^{1/24} \sigma(q), \quad \quad(q = e^{2\pi i x}, x\in \mathbb{Q}).$$ It then turns out that $f$ is a quantum modular form on $\mathbb{Q}$ for $\Gamma_0(2)$.

Work of Lewis and Zagier offered a framework which generalized many of the interesting properties of $\sigma$. In [@lewis-zagier], they showed a correspondence between Maass waveforms $u$, pairs of $L$-functions $(L_0,L_1)$, holomorphic periodic functions $f$, and period functions $\psi$. For the precise definitions and basic results on Maass waveforms are given in Section [\[subsec: maass\]](#subsec: maass){reference-type="ref" reference="subsec: maass"}. This period function appears as the obstruction to modularity of $f$ under $z \mapsto -1/z$ and extends to the cut plane $\mathbb{C}':=\mathbb{C}\backslash (-\infty,0]$, upgrading the first observation of quantum modularity of $\sigma$ to a full holomorphic quantum modularity result. We use resurgence to give a new proof of this.

::: cor
Let $f(z)$ be the periodic function of a Maass waveform $u(z)$ with spectral parameter $s= \frac{1}{2}$ for $\mathrm{SL}_2(\mathbb{Z})$. Define $$\begin{aligned}
    \psi(z):= f(z)  -  z^{-1}f(-1/z). 
\end{aligned}$$ Then the function $\psi$ has an analytic continuation to $\mathbb{C}'$.
:::

We note that [@fantini-rella] also offered a proof of this result using resurgence. However, the main portion of our proof, a median resummation result using Gaussian integration, is distinct. In particular, we show that one does not need to assume any information about the period function proven in [@lewis-zagier].

We mention one last type of quantum modular form, which Zagier labelled as Example 0 in [@zagier-quantum]. To describe this, for real numbers $x$ consider the sawtooth function $((x))$, which takes the value $0$ for integers $x$ and is defined by $((x)):=x-\lfloor x\rfloor-1/2$ for $x\in\mathbb{R}\setminus\mathbb{Z}$. Then the classical Dedekind sum for coprime integers $c,d$ with $c>0$ is defined by $$s(d,c):=\sum_{0<k<c}\left(\left(\frac{k}c\right)\right)\cdot\left(\left(\frac{kd}c\right)\right).$$ These Dedekind sums satisfy well-known relations, in particular, reciprocity. Zagier interpreted these by defining $S\colon\mathbb{Q}\rightarrow\mathbb{Q}$ by $S(d/c):=12s(d,c)$, and then noted that they imply the quantum modular-like transformations $$S(x)-S(x+1)=0,\quad\quad S(x)-S(-1/x)=x+\frac1x\pm 3+\frac{1}{\mathrm{Num}(x)\mathrm{Den}(x)}.$$ Here, the sign above is $+$ if $x<0$, and is $-$ if $x>0$. As these obstructions to modularity depend on numerators and denominators, they are not continuous functions. However, such examples found key applications in work of Bettin and Conrey [@bettin-conrey]. Later, in [@folsom-cotangent-sums] Folsom embedded these examples into an infinite family of twisted versions of Maass--Eisenstein series. Generically, she proved that they are quantum modular forms with smooth errors to modularity. However, when one specializes to the examples of Zagier, or of Bettin and Conrey, these smooth functions "degenerate" to discontinuous functions. Thus, even this example from Zagier's original paper fits into a rich theory of period functions of Maass--Eisenstein series.

With some mild extra considerations specific to the non-cuspidal case, we demonstrate how resurgence connects to Maass--Eisenstein series with the following corollary.

::: cor
Let $f(z)$ be the periodic function of the real-analytic Eisenstein series $E_{1/2}(z)$, defined in Equation $\ref{eqn: maass eisenstein}$. Define $$\begin{aligned}
    \psi(z):= f(z)  -  z^{-1}f(-1/z). 
\end{aligned}$$ Then the function $\psi$ has an analytic continuation to $\mathbb{C}'$.
:::

We remark that our methods are likely generalizable to more general spectral parameter and level for both Maass cases.

As an additional result showing the flexibility of these methods, we reprove the quantum modularity of cusp forms and of Eichler integrals of integer weight cusp forms using a variant of the same framework. We remark that in these cases, resurgence analysis on its face will not apply; see Remark 3.2 of [@fantini-rella]. Our main result is the following:

::: theorem
[]{#thm: Main label="thm: Main"} Suppose $g$ is one of the following:

1.  a cusp form of weight $\kappa \in \mathbb{N}$ for $\Gamma =\Gamma_0(N)$;

2.  a cusp form of weight $\kappa \in \frac{1}{2} + \mathbb{N}_0$ for $\Gamma =\Gamma_0(N)$, $4\mid N$;

3.  the Eichler integral of a cusp form of weight $2-\kappa \in \mathbb{N}$ for $\Gamma =\Gamma_0(N)$;

4.  the Eichler integral of a cusp form of weight $2-\kappa \in \frac{1}{2} + \mathbb{N}_0$ for $\Gamma =\Gamma_0(N)$, $4\mid N$;

5.  the periodic function of a Maass waveform with $s=\frac{1}{2} = \kappa/2$ for $\Gamma =\text{SL}_2(\mathbb{Z})$;

6.  the periodic function of $E_{\kappa/2}(z)$ with $s=\frac{1}{2}=\kappa/2$ for $\Gamma =\text{SL}_2(\mathbb{Z})$.

Then $g$ is a holomorphic quantum modular form of weight $\kappa$ for $\Gamma$. Moreover, for each $\gamma \in \Gamma$, the modular obstruction $h_\gamma$ equals a Borel--Laplace sum of the asymptotic series of $g$ as $z$ approaches $\gamma^{-1}(i\infty)$ along a geodesic, and analytically continues to $\mathbb{C}_\gamma$.
:::

For the remainder of the paper, we will refer to these cases as *Type 1* through *Type 6*. We note that the results above for *Types 1* and *2* are immediate from their definitions. However, the methods developed for the remaining types in this paper can be applied to functions related to those of *Types 1* and *2* to give an interesting resurgence perspective on these functions which themselves have no resurgent structure.

::: remark
Many of the above functions have a natural "companion\" in the lower half-plane like the example of $\sigma$ and $\sigma^*$. Our results can equivalently be proven for the corresponding functions on $\mathbb{C}\backslash\mathbb{R}$.
:::

We note that the quantum modularity of these functions is not new, but the quantum modularity of half-integral weight Eichler integrals has been strengthened to holomorphic quantum modularity, and the relationship of Borel resummation to their quantum modularity across all cases was previously conjectured but unproven.

Theorem [\[thm: Main\]](#thm: Main){reference-type="ref" reference="thm: Main"} and its proof additionally give evidence towards some conjectures of Fantini and Rella [@fantini-rella]:

::: cor
[]{#cor: conj label="cor: conj"} The asymptotic series of Eichler integrals of half-integral weight cusp forms, periodic functions of Maass waveforms with $s=1/2$, and the periodic function of the real-analytic Eisenstein series with $s=1/2$ are modular resurgent series. Moreover, the median resummation of each of these series recovers the original function, which is a holomorphic quantum modular form.
:::

The paper is organized as follows. In Section [\[sec: prelims\]](#sec: prelims){reference-type="ref" reference="sec: prelims"}, we develop the necessary background on resurgence, as well as holomorphic modular and Maass forms. In Section [\[sec: intermediate\]](#sec: intermediate){reference-type="ref" reference="sec: intermediate"}, we collect a variety of intermediate results in service of our main theorem. This will be broken up into three main subsections. Subsection 3.1 will compute the asymptotic expansions of functions of *Types 1* through *6* at the relevant rational points. Subsection 3.2 will use a Gaussian integration identity to relate each function to the median resummation of its asymptotic series. Subsection 3.3 will locate the image of each function under the relevant slash operator in the decomposition coming from Subsection 3.2. In Section [\[sec: main theorem\]](#sec: main theorem){reference-type="ref" reference="sec: main theorem"}, we prove Theorem [\[thm: Main\]](#thm: Main){reference-type="ref" reference="thm: Main"} and in Section [\[sec: corollaries\]](#sec: corollaries){reference-type="ref" reference="sec: corollaries"}, we prove that the obstructions to modularity have the desired properties for the statements of our corollaries. In Section [\[sec: questions\]](#sec: questions){reference-type="ref" reference="sec: questions"}, we offer some future directions and open questions that may be of interest to the reader.
