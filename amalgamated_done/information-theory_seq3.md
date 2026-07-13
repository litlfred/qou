<!-- FILE_START: hausdorff-dimension-recurrence.md -->
$$
  d_{H,q}^{(n+1)} = d_{H,q}^{(n)} + \frac{(2q_n - 1)(3 - 4q_n)(q_n - 1)}{q_n^5}.
$$

This defines a contraction mapping for $q > 3/4$. The iteration $d_{H,q} \to d_{H,q} + \Delta d_{H,q}$ flows monotonically toward $d_{H,q} = 0$. The fractal complexity of the Reeb dynamics decreases with increasing $q$, vanishing at $q \to \infty$ (the Big Bang, where the Julia set collapses to a point). The direction of decreasing $d_{H,q}$ coincides with increasing $q$ — pointing from the classical regime ($q \to 1$, maximal $d_{H,q}$) toward the Big Bang.

**Regime table.**
See [Table 1](#tbl:hausdorff-dimension-recurrence-table1-data).

The $q$-deformed $d_{H,q}$ and the classical Hausdorff dimension $d_H$ of the Julia set over $\mathbb{C}$ are distinct quantities ([classical Hausdorff dimension comparison](#rem:hausdorff-dimension-classical-comparison)).

**Convergence from local $q$.**
The downward iteration $q_{n+1} = q_n - \hbar_{q_n} = (q_n^2 - q_n + 1)/q_n$ flows $q$ toward the classical limit $q = 1$. This is a superattracting fixed point. Starting from our local $q_0$:

See [Table 3](#tbl:hausdorff-dimension-recurrence-table3-data).

It takes three Planck steps from our universe to reach the classical limit. The convergence is superlinear. At the fixed point, $\eta_q = 1$ nat, meaning each Reeb operation carries exactly one natural unit of information.

**Cosmological arrow of time.**
The monotone decrease of $d_{H,q}$ with $q$ defines an information-theoretic arrow. The parameter $q$ flows from the classical limit toward the Big Bang. Reversing time reverses the discrete recurrence. The second law of thermodynamics asserts that the $q$-deformed dimension increases as $q$ decreases.
<!-- FILE_END: hausdorff-dimension-recurrence.md -->

<!-- FILE_START: hausdorff-dimension-classical-comparison.md -->
The $q$-deformed Hausdorff dimension $d_{H,q} = (2q-1)^2/q^3$ ([discrete recurrence](#rem:hausdorff-dimension-recurrence)) differs from the classical Hausdorff dimension $d_H$ of the Julia set $J(f_q)$ over $\mathbb{C}$.

**$d_{H,q}$ vs. $d_H$: comparison with classical Hausdorff dimension.**
For parameters $c(\varTheta)$ on the main cardioid of the Mandelbrot set, the Julia set is a quasicircle. The classical Hausdorff dimension $d_H$ satisfies:

1. **Ruelle perturbative** (valid for $|c| \ll 1$): $d_H = 1 + \frac{|c(\varTheta)|^2}{4 \ln 2} + O(|c|^4)$. At $\varTheta = 0.1097$: $|c| = 0.346$, yielding $d_H \approx 1.043$.
2. **Transfer operator** (numerical, Bowen--Ruelle): $d_H \approx 1.047$ at $N = 800$ grid points.
3. **QOU $q$-deformed**: $d_{H,q} = 1.088$.

The gap $d_{H,q} - d_H \approx 0.041$ arises from differing Manning--McCluskey inputs. See [Table 2](#tbl:hausdorff-dimension-recurrence-table2-data).

The classical $d_H$ arises from conformal dynamics over $\mathbb{C}$. The $q$-deformed $d_{H,q}$ replaces the transcendental $\ln 2$ with the rational $\eta_q$, and the numerical $\chi(c)$ with the algebraic $\chi_q$. We propose that $d_{H,q}$ governs the physical regime.

No closed form exists for the classical $d_H(J_c)$ over the main cardioid parameter $c$. It appears implicitly as the unique zero of the Bowen--Ruelle pressure function $P(-t\log|f_c'|) = 0$.
<!-- FILE_END: hausdorff-dimension-classical-comparison.md -->

<!-- FILE_START: information-causality.md -->
We place the quantum observable universe (QOU) within information-theoretic physics. The mass--energy equivalence $E = mc_q^2$ and the derived speed of light $c_q = 1/(q-1)$ connect the QOU to established information bounds.

**1. The light cone is the Lieb--Robinson cone.**
The causal boundary arises from the $q$-connection decomposition $A_q = q^{-1}A + \hbar_q\iota_\xi A\varTheta$. The boundary at $|Z| = c_q$ in the contact affine coordinate ([contact affine chart](#def:contact-affine-chart)) is the locus where horizontal spatial diffusion matches vertical Reeb advance. Outside this cone, the Lieb--Robinson bound enforces exponential suppression of correlations. Causality follows directly from the ratio of spatial to temporal information flow.

**2. The speed of light varies with $q$.**
The speed of light $c_q = 1/(q-1)$ depends on the substrate parameter. At the Big Bang ($q \to \infty$), $c \to 0$. As the universe classicalises ($q \to 1$), $c \to \infty$. At the present epoch $q = q_0$, $c \approx 9.12$ in Reeb units.

**3. The Margolus--Levitin bound and $c_q$.**
The Margolus--Levitin theorem bounds the operation rate by $2E/\pi\hbar$. We have the crossing energy $E = mc_q^2 = m/(q-1)^2$ and the operation count $n_R(q) = 1/\hbar_q$. The bound is:

$$
  n_R(q)  \leq  \frac{2m}{\pi\hbar_q(q-1)^2}.
$$

The Reeb dynamics saturates this bound up to the factor $2/\pi$.

**4. Bremermann's limit and information bandwidth.**
Bremermann's limit states a system processes at most $mc^2/h$ bits per second. The bandwidth is:

$$
  \mathfrak{B}(q)
  =  \frac{q\eta_q}{(q-1)^2}
  \quad \text{($q$-bits per Planck time)}.
$$

At $q = q_0$, $\mathcal{B} \approx 82$ $q$-bits per Planck time.

**5. Pawlowski's information causality.**
Information causality restricts the accessible information Bob gains from Alice. In the QOU, the Lieb--Robinson bound ensures exponential decay outside the $|Z| = c_q$ cone.

**6. The Bekenstein bound and fibre entropy.**
The Bekenstein bound limits the entropy to $S \leq 2\pi RE / \hbar c$. We bound the QOU fibre entropy by $\eta_q$ per operation:

$$
  S_{\mathrm{fibre}}  \leq  \eta_q
  =  \frac{2q - 1}{q^3}.
$$

**7. Summary.**
See [Table](#tbl:information-causality-table-data).
<!-- FILE_END: information-causality.md -->