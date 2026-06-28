**Three-context behaviour (downstream realisations).** The series
$\mathrm{Li}_2^q(x) = \sum x^n / (n [n]_q)$ carries an *extra* factor
of $n$ in the denominator, so its convergence in char $p$ and $p$-adic
settings is slightly worse than that of $\exp_q$:

* **$\mathbb{F}_p$.** Fails at $n = p$ (because $p = 0$) and at
 $n = \mathrm{ord}_{\mathbb{F}_p^\times}(q)$; replaced by the
 polynomial truncation $\mathrm{Li}_2^{q,(p)}(x) = \sum_{n=1}^{p-1} x^n / (n [n]_q)$,
 which retains the pentagon identity modulo $x^p = 0$. The
 **Kontsevich--Zagier mod $p$ dilogarithm** is the corresponding
 object at $q = 1$; $\mathrm{Li}_2^{q,(p)}$ is its $q$-deformation.
* **$\mathbb{Q}_p$.** For $q \in 1 + p\mathbb{Z}_p$ and
 $v_p(x) \ge 1$, converges with valuation
 $v_p(x^n / (n[n]_q)) \ge n - 2 v_p(n) - v_p(n!)/(p-1)$. The pentagon
 identity holds identically in $\mathbb{Q}_p[\![x,y]\!]$ restricted to
 $p\mathbb{Z}_p \times p\mathbb{Z}_p$. This is Coleman's $p$-adic
 dilogarithm in the $q$-deformed form.
* **$\mathbb{C}_p$.** Converges on $v_p(x) > 1/(p-1)$ (same radius as
 $\exp_q$; the extra $n$ in the denominator shifts the boundary
 slightly inward at the cutoff $n = p$ but does not change the
 asymptotic). Beyond the disc, $\mathrm{Li}_2^q$ extends to
 $\mathbb{C}_p$ via the pentagon identity and an Iwasawa-style branch
 choice.
