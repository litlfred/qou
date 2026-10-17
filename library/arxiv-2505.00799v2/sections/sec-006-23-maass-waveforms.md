---
doc_id: arxiv-2505.00799v2
doc_title: "Quantum Modular Forms and Resurgence"
section_id: sec-006-23-maass-waveforms
section_title: "Maass Waveforms"
section_number: 2.3
pages: 13-15
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.95
doc_brief: "Quantum Modular Forms and Resurgence — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
[]{#subsec: maass label="subsec: maass"}

We now recall the basic definitions and properties of Maass waveforms for $\text{SL}_2(\mathbb{Z})$. We also refer the reader to [@bump; @iwaniec] for a more thorough introduction to the theory.

We begin with a smooth function $u \colon \mathbb{H} \to \mathbb{C}$ satisfying the following.

1.  For all $\gamma = \begin{psmallmatrix} a & b \\ c& d \end{psmallmatrix} \in \Gamma_0(N)$ and for all $z \in \mathbb{H}$, we have $u(\gamma z)=u(z)$;

2.  If $\Delta := -y^2\left( \frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}\right)$ is the hyperbolic Laplacian, then $\Delta u = \lambda u$ for some $\lambda \in \mathbb{C}$.

Such a function necessarily admits a Fourier--Whittaker expansion. If the zeroth Fourier--Whittaker coefficient vanishes and $u$ is square-integrable on a fundamental domain of $\text{SL}_2(\mathbb{Z})$ with respect to the hyperbolic measure, then we say that $u$ is a Maass waveform.

We call $\lambda$ the eigenvalue of $u$ and if $\lambda = s(1-s)$, then $s$ is called its spectral parameter. Such a function $u(z)$ has an expansion of the form $$\label{eqn: maass} u(z) = \sqrt{y}\sum_{n \in \mathbb{Z}_{\neq 0}} A_n K_{s-1/2}(2\pi |n| y) e^{2\pi i nx}, \quad \quad (z = x+iy \in \mathbb{H}),$$ where $K_\nu(x)$ is the $K$-Bessel function of order $\nu$.

In the central result of [@lewis-zagier], Lewis and Zagier gave a correspondence between Maass waveforms and three different classes of functions. While all show up in our results, we will only recall two of them here. Let $u(z)$ be a Maass waveform with spectral parameter $s$, where $\Re(s)>0$. Then associated to $u$ are a pair of Dirichlet $L$-series $L_\varepsilon(\rho)$, $\varepsilon = \{0, 1\}$, convergent in some right half-plane, such that the functions $\Lambda_{\varepsilon}(\rho) :=  \gamma_s(\rho+\varepsilon)L_\varepsilon(\rho)$, where $$\gamma_s(\rho) := \frac{1}{4\pi^\rho}\Gamma\left(\frac{\rho-s+1/2}{2}\right) \Gamma\left(\frac{\rho+s-1/2}{2}\right),$$ are entire functions of finite order and satisfy $$\Lambda_\varepsilon(1-\rho) = (-1)^\varepsilon \Lambda_\varepsilon(\rho).$$ From the coefficients in the expansion of $u$ in ([\[eqn: maass\]](#eqn: maass){reference-type="ref" reference="eqn: maass"}), their Dirichlet series take the form $$L_\varepsilon(\rho) := \sum_{m=1}^\infty \frac{A_m + (-1)^\varepsilon A_{-m}}{m^\rho}, \quad \quad (\varepsilon \in \{0,1\}).$$ Moreoever, there is also a corresponding holomorphic periodic function $f\colon \mathbb{C}\backslash \mathbb{R} \to \mathbb{C}$, defined by $$f(z) := \begin{cases} \sum_{n>0}^\infty A_n n^{s-1/2} q^n, & \text{if } z \in \mathbb{H},\\
    -\sum_{n<0}^\infty A_{n} |n|^{s-1/2} q^n, & \text{if } z \in \mathbb{H}^-,
 \end{cases}$$ where $\mathbb{H}^-$ denotes the lower half-plane. From this point on, we will abuse notation and use $f$ to refer to the restriction of $f$ to the upper half-plane. Throughout, we will prove results for $f$ in the upper half-plane, but the corresponding results for $f$ in the lower half-plane are completely analogous, and in fact $f$ on $\mathbb{C} \backslash\mathbb{R}$ is really a single holomorphic quantum modular form.

We will also consider one non-cuspidal case in our work. We will define the non-holomorphic Eisenstein series with spectral parameter $s$ by

$$\begin{aligned} \label{eqn: maass eisenstein}
E_s(z) &:= \zeta(2s)y^s + \frac{\pi^{1/2}\Gamma(s-\frac{1}{2})}{\Gamma(s)}\zeta(2s-1)y^{1-s} \\&+ \frac{4\pi^s}{\Gamma(s)}\sqrt{y}\sum_{n=1}^\infty n^{1/2-s}\sigma_{2s-1}(n) K_{s-1/2}(2\pi ny) \cos(2\pi nx), 
\end{aligned}$$ where $\sigma_\nu(n) := \sum_{d\mid n} d^\nu$ is the $\nu$-th sum of divisors function. We will specifically analyze the case where $s=1/2$. As is standard, we will write $d(n)$ for $\sigma_0(n).$ For the associated holomorphic periodic function in this case, we pick the normalization $$f(z):= 1-4\sum_{n=1}^\infty d(n)q^n.$$

Above, we gave the functional equations for the pair of $L$-functions associated to a Maass waveform. Here, we state the analogous result for our Eisenstein series of interest. The corresponding $L$-function is proportional to $$\zeta^2(\rho) = \sum_{m=1}^\infty \frac{d(m)}{m^\rho}, \quad \quad \Re(\rho)>1,$$ where $\zeta(\rho)$ is the Riemann zeta function. The completion of the function $\zeta^2(\rho)$ has meromorphic continuation to $\mathbb{C}$ with a pole at $s=1$ and satisfies the functional equation $$\pi^{-\rho} \Gamma\left(\frac{\rho}{2}\right)^2 \zeta^2(\rho) = \pi^{-(1-\rho)} \Gamma\left(\frac{1-\rho}{2}\right)^2 \zeta ^2(1-\rho).$$
