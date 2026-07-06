The electromagnetic coupling ([EM coupling projection](#prop:em-coupling-projection)) predicts $\alpha_{\mathrm{EM}}$ directly from the substrate parameter $q$, requiring zero free parameters.

**Bare formula (base holonomy).**

$$
  \alpha_{\mathrm{EM}}^{-1}(q)
  = 
  q \cdot [9]_q \cdot [10]_q
  = 136.823.
$$

The force-carrier generators $T_{2,9}$ and $T_{3,5}$ ([force identification](#rem:force-knot-identification)) dictate the crossing numbers $9$ and $10$. The Descartes substrate parameter fixes the $q$-integers.

**Derived correction (additive photon zero-mode).**

The leading correction to the bare formula is additive, derived from the photon infrared zero-mode on Bring's surface ([photon IR zero-mode](#prop:photon-ir-zero-mode-bring)):

$$
  \alpha_{\mathrm{EM}}^{-1}(q) = q \cdot [9]_q \cdot [10]_q + \frac{2}{3\pi},
  \qquad \frac{2}{3\pi} = \frac{b_1(M_{\mathrm{Bring}})}{\mathrm{Area}(M_{\mathrm{Bring}})}
  = \frac{2g}{4\pi(g-1)}\Big|_{g=4}.
$$

The genus-$4$ topology fixes $b_1 = 2g = 8$ and the Gauss–Bonnet area. The corrected value is $137.0354$. This leaves a $-4.2\;\mathrm{ppm}$ residual against the CODATA value of $137.035999$. This additive correction improves the bare form by a factor of $370$. Both the tree term and the additive zero-mode are Lean-formalised.

**Order of validity.**

The remaining $-4.2\;\mathrm{ppm}$ represents a next-order Schwinger-type effect $\sim \alpha/(4\pi)$. The denominator $8\pi = \pi\,b_1$ is derived. The exact coefficient is an $O(\alpha^2)$ Bloch-group normalisation in $B_3(\mathbb{C})$ over the ideal hyperbolic tetrahedra of Bring's surface. This coefficient is not yet closed ([α_EM derivation open problems](#rem:alpha-em-derivation-open-problems)). The parameter-free prediction thus holds to $\approx 4\;\mathrm{ppm}$ via the additive correction. The $O(\alpha)$ self-energy coefficient remains open.

**Numerical comparison with CODATA.**

See [Table 1](#tbl:fine-structure-observation-table1-data).

**Inversion: $q$ from $\alpha_{\mathrm{EM}}$.**

Fixing $\alpha^{-1} \approx 137.036$ and solving for $q$ yields:

$$
  q_{\mathrm{CODATA}} = 1.11023.
$$

This value matches the substrate parameter extracted independently from mass predictions and half-life calculations ([half-life as $q$-probe](#rem:half-life-as-q-probe)). This provides a rigid cross-check between the electromagnetic and strong sectors.

**Sensitivity.**

The coupling depends steeply on $q$:

$$
  \frac{\partial \ln \alpha_{\mathrm{EM}}}{\partial \ln q}
  =  -1 - 
  \frac{9  q^9 [10]_q + 10  q^{10} [9]_q}
       {[9]_q [10]_q (q - q^{-1})}.
$$

At $q = q_0$, this derivative is approximately $-20$. A $1\%$ shift in $q$ drives a $\sim 20\%$ shift in $\alpha_{\mathrm{EM}}$. The empirical agreement tightly bounds $q$ around $q_0$.

**Comparison with other $q$-predictions.**

See [Table 2](#tbl:fine-structure-observation-table2-data).

The substrate parameter $q_0$ is overdetermined. Three independent observables (electromagnetic coupling, mass ratios, decay rates) converge on the identical value.
