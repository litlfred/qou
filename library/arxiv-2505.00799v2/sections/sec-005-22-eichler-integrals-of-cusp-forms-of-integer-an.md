---
doc_id: arxiv-2505.00799v2
doc_title: "Quantum Modular Forms and Resurgence"
section_id: sec-005-22-eichler-integrals-of-cusp-forms-of-integer-an
section_title: "Eichler Integrals of Cusp Forms of Integer and Half-Integer Weight"
section_number: 2.2
pages: 11-13
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.951
doc_brief: "Quantum Modular Forms and Resurgence — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
[]{#subsec: modular label="subsec: modular"}

We begin with a brief recollection of the required definitions and properties of modular forms.

To start, for functions $f \colon \mathbb{H} \to \mathbb{C}$, we recall the action of the Petersson slash operator of weight $k \in \frac{1}{2}\mathbb{Z}$ associated to $\gamma = \begin{psmallmatrix} a & b \\ c& d \end{psmallmatrix} \in \Gamma_0(N)$ (where $4 \mid N$ if $k \in \frac{1}{2} + \mathbb{Z}$): $$\label{eqn: slash}
f|_k\gamma(z):= \begin{cases} (cz+d)^{-k}f\left(\frac{az+b}{cz+d}\right) & \text{for } k \in \mathbb{Z},\\
 \varepsilon_d^{2k}\left(\frac{c}{d}\right) (cz+d)^{-k}     f\left(\frac{az+b}{cz+d}\right) & \text{for } k \in \frac{1}{2}+ \mathbb{Z}.
 \end{cases}$$ Here, $\left(\frac{\cdot}{\cdot}\right)$ denotes the Kronecker symbol and for odd $d$, $$\varepsilon_d:= \begin{cases}
 1 & \text{if } d \equiv 1 \,\,({\rm mod}\,\,{4}),\\
 i & \text{if } d \equiv 3 \,\,({\rm mod}\,\,{4}).
 \end{cases}$$ We will consider modular forms on congruence subgroups $$\Gamma_0(N) :=\left\{ \begin{pmatrix} a & b \\ c& d \end{pmatrix} \in \text{SL}_2(\mathbb{Z}) : c \equiv 0 \,\,({\rm mod}\,\,{N})\right\}.$$ We are now able to define the spaces of modular forms we will consider.

::: definition
Let $k \in \frac{1}{2}\mathbb{N}$ and $N \in \mathbb{N}$ (where $4 \mid N$ when $k$ is a half-integer). We say a holomorphic function $f\colon \mathbb{H} \to \mathbb{C}$ is a cusp form of weight $k$ for $\Gamma_0(N)$ if:

1.  For all $\gamma = \begin{psmallmatrix} a & b \\ c& d \end{psmallmatrix} \in \Gamma_0(N)$, we have $f(z) = f|_{k}\gamma(z)$ for all $z \in \mathbb{H}$;

2.  As $z$ approaches any cusp of $\Gamma_0(N)$, $f$ decays exponentially.
:::

Such functions necessarily admit Fourier expansions at infinity without constant term. We will often define our function $f$ by such an expansion.

We will not only consider cusp forms themselves, but also their Eichler integrals. Miraculously, in the case where $k \in \mathbb{N}$, there is a canonical differential operator $D^{k-1}$, where $D = \frac{1}{2\pi i }\frac{\partial}{\partial z}$, which sends modular forms of weight $2-k$ to modular forms of weight $k$, and so it is natural to consider the $(k-1)$-fold primitive of a cusp form $f$, defined by $$\tilde{f}(z) := \frac{(-2\pi i z)^{k-1}}{\Gamma(k-1)}\int_z^{i\infty} f(\tau) (\tau-z)^{k-2}\;d\tau,$$ for $z$ in $\mathbb{H}$. If $f$ has a Fourier expansion $f(z) = \sum_{n=1}^\infty a_n q^n$, where $q =e^{2\pi i z}$, then $\tilde{f}$ has the Fourier expansion $$\tilde{f}(z) = \sum_{n=1}^\infty a_n n^{1-k} q^n. \label{eqn: eichler}$$

Such a function $\tilde{f}$ is nearly a modular form of weight $2-k$; its obstruction to modularity is a polynomial of degree at most $k-2$. For $\gamma \in \Gamma_0(N)$, one can write the difference $$\tilde{f} (z) - \tilde{f}|_{2-k}\gamma(z)=\frac{(-2\pi i z)^{k-1}}{\Gamma(k-1)}\int_{\gamma^{-1}(i\infty)}^{i\infty} f(\tau) (\tau - z)^{k-2}\;d\tau.$$

The half-integer analogue was first considered in [@lawrence-zagier]. In the case where $k \in \frac{1}{2}+\mathbb{N}_0$, the integral definition is no longer sensible, but the definition on the level of Fourier expansions is still reasonable. The obstruction to modularity is much more interesting in this case.

It was first shown for a family of examples of false theta functions [@lawrence-zagier], and then extended to the general case in [@bringmann-rolen], that if one considers the limiting values of $\tilde{f}$ as $z$ approaches $x \in \mathbb{Q}$ along a geodesic, then the resulting function (still denoted by $\tilde{f}$) from $\mathbb{Q}$ to $\mathbb{C}$ forms a quantum modular form. Namely, the obstructions to modularity $$h_\gamma(x) := \tilde{f}(x) - \chi_{-4}(\gamma)\tilde{f}|_{2-k}(x),$$ extend to real analytic functions on $\mathbb{R}\backslash \{\gamma^{-1}(i\infty)\}$ for all $\gamma \in \Gamma_0(N)$. We defined $\chi_{-4}(n)$ in Section 1.1.

This result was proven by considering a companion function $f^*$ which acts as a non-holomorphic Eichler integral on the lower half-plane. This function has the same asymptotics as $\tilde{f}$ as one approaches the same rational number. This function can be shown to have the obstruction to modularity $$f^*(z) - \chi_{-4}(\gamma) f^*|_{2-k}\gamma(z) = \frac{(-2\pi i z)^{k-1}}{\Gamma(k-1)}\int_{\gamma^{-1}(i\infty)}^{i\infty} f(\tau) (\tau - z)^{k-2}\;d\tau$$ in the lower half-plane, which $\tilde{f}$ inherits on $\mathbb{Q}$. We recall its explicit form here because this function appears again in our results.

To conclude this section, we recall the relevant functional equations for $L$-functions associated to modular forms. Suppose that $f$ is a cusp form of weight $k \in \frac{1}{2}\mathbb{N}$ on $\Gamma_0(N)$ for $N \in \mathbb{N}$ (where $4\mid N$ in the half-integer weight case) which has Fourier expansion $f(z) = \sum_{n=1}^\infty a_n q^n$. For $-d/c \in \mathbb{Q}$, define $\zeta_c^{-d} := e^{2\pi i (-d/c)}$ and $$L(f, \zeta_c^{-d};\rho) := \sum_{m = 1}^\infty \frac{a_m \zeta_c^{-dm}}{m^\rho}, \quad \quad \Re(\rho)\gg 0.$$ Using the Mellin transform of $f$, we define the completed $L$-function by $$\Lambda(f, \zeta_c^{-d}; \rho) := \left( \frac{c}{2\pi}\right)^\rho \Gamma(\rho) L(f, \zeta_c^{-d}; \rho) = c^\rho \int_0^\infty f(it-d/c) t^{\rho-1}\;dt.$$

::: prop
Suppose $f$ is as above. Then the following are true.

1.  If $k \in \mathbb{N}$ and $\gamma = \begin{psmallmatrix} a & b \\ c & d\end{psmallmatrix} \in \Gamma_0(N)$, then $\Lambda(f, \zeta_c^{-d}; \rho)$ analytically continues to $\mathbb{C}$ and satisfies $$\Lambda(f, \zeta_c^{-d}; \rho) = i^{-k} \Lambda(f, \zeta_c^a;  k-\rho).$$

2.  If $k \in \frac{1}{2} + \mathbb{N}$ and $\gamma = \begin{psmallmatrix} a & b \\ c & d\end{psmallmatrix} \in \Gamma_0(N)$, then then $\Lambda(f, \zeta_c^{-d}; \rho)$ analytically continues to $\mathbb{C}$ and satisfies $$\Lambda(f, \zeta_c^{-d}; \rho) = i^{-k} \varepsilon_d^{2k} \left( \frac{c}{d}\right) \Lambda(f, \zeta_c^a; k-\rho).$$
:::

::: proof
*Proof.* Both of the claims are routinely proven, but we offer a proof of the second claim as it appears less frequently in the literature. We first write $$c^\rho \int_0^\infty f(it-d/c) t^{\rho-1}\;dt = c^\rho \int_0^{1/c} f(it-d/c) t^{\rho-1}\;dt + c^\rho \int_{1/c}^{\infty} f(it-d/c) t^{\rho-1}\;dt.$$ Under the change of variables $t \mapsto 1/c^2t$, the first integral becomes $$\begin{aligned}
c^\rho \int_0^{1/c} f(it-d/c) t^{\rho-1}\;dt &= c^\rho \int_\infty^{1/c} f(-d/c+i/c^2t)(c^2)^{1-\rho}t^{1-\rho} \frac{-1}{c^2t^2}\;dt \\
&= c^{-\rho} \int_{1/c}^\infty f(-d/c+i/c^2t)t^{-\rho-1} \;dt
\end{aligned}$$ Then recognizing that if $\gamma = \begin{psmallmatrix} a & b \\ c & d\end{psmallmatrix}$, then $\gamma(-d/c+i/c^2t) = a/c + it$, we have $$\begin{aligned}
c^{-\rho} \int_{1/c}^\infty f(-d/c+i/c^2t)t^{-\rho-1} \;dt 
&= c^{-\rho} \int_{1/c}^\infty f(-d/c+i/c^2t)t^{-\rho-1}\;dt\\ 
&= c^{-\rho} \int_{1/c}^\infty  f|_{k}\gamma(-d/c+i/c^2t)t^{-\rho-1} \;dt \\ 

&= i^{-k}  \varepsilon_d^{2k} \left( \frac{c}{d}\right)  c^{k-\rho} \int_{1/c}^\infty f(a/c+it) t^{k-\rho-1}\;dt.
\end{aligned}$$ Above, we used that $\gamma \in \Gamma_0(N)$. The above calculation gives a presentation for $\Lambda(f, \zeta_{c}^{-d};\rho)$ which immediately implies both the desired analytic continuation to $\mathbb{C}$ and the stated functional equation. ◻
:::
