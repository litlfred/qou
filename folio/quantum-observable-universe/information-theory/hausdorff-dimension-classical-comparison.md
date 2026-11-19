The $q$-deformed Hausdorff dimension $d_{H,q} = (2q-1)^2/q^3$ ([discrete recurrence](#rem:hausdorff-dimension-recurrence)) differs from the classical Hausdorff dimension $d_H$ of the Julia set $J(f_q)$ over $\mathbb{C}$.

**$d_{H,q}$ vs. $d_H$: comparison with classical Hausdorff dimension.**
For parameters $c(\varTheta)$ on the main cardioid of the Mandelbrot set, the Julia set is a quasicircle. The classical Hausdorff dimension $d_H$ satisfies:

1. **Ruelle perturbative** (valid for $|c| \ll 1$): $d_H = 1 + \frac{|c(\varTheta)|^2}{4 \ln 2} + O(|c|^4)$. At $\varTheta = 0.1097$: $|c| = 0.346$, yielding $d_H \approx 1.043$.
2. **Transfer operator** (numerical, Bowen--Ruelle): $d_H \approx 1.047$ at $N = 800$ grid points.
3. **QOU $q$-deformed**: $d_{H,q} = 1.088$.

The gap $d_{H,q} - d_H \approx 0.041$ arises from differing Manning--McCluskey inputs. See [Table 2](#tbl:hausdorff-dimension-recurrence-table2-data).

The classical $d_H$ arises from conformal dynamics over $\mathbb{C}$. The $q$-deformed $d_{H,q}$ replaces the transcendental $\ln 2$ with the rational $\eta_q$, and the numerical $\chi(c)$ with the algebraic $\chi_q$. In the QOU framework, $d_{H,q}$ governs the physical regime.

No closed form exists for the classical $d_H(J_c)$ over the main cardioid parameter $c$. It appears implicitly as the unique zero of the Bowen--Ruelle pressure function $P(-t\log|f_c'|) = 0$.
