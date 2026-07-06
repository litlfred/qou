The electromagnetic coupling
([EM coupling projection](#prop:em-coupling-projection)) predicts
$\alpha_{\mathrm{EM}}$ as a function of the substrate parameter $q$
alone, with no free parameters.

**Bare formula (base holonomy):**

$$
  \alpha_{\mathrm{EM}}^{-1}(q)
  = 
  q \cdot [9]_q \cdot [10]_q
  = 136.823.
$$

The crossing numbers $9$ and $10$ are determined by the force-carrier
generators $T_{2,9}$ and $T_{3,5}$
([force identification](#rem:force-knot-identification)); the
$q$-integers are fixed by the Descartes substrate parameter.

**Derived correction (additive photon zero-mode).**
The leading correction to the bare formula is *additive*, not
multiplicative, and is derived from the photon infrared zero-mode on
Bring's surface ([photon IR zero-mode](#prop:photon-ir-zero-mode-bring)):

$$
  \alpha_{\mathrm{EM}}^{-1}(q) = q \cdot [9]_q \cdot [10]_q + \frac{2}{3\pi},
  \qquad \frac{2}{3\pi} = \frac{b_1(M_{\mathrm{Bring}})}{\mathrm{Area}(M_{\mathrm{Bring}})}
  = \frac{2g}{4\pi(g-1)}\Big|_{g=4}.
$$

With $b_1 = 2g = 8$ and the Gauss–Bonnet area fixed by the genus-$4$
topology, this lands at $137.0354$ — a residual of $-4.2\;\mathrm{ppm}$
against CODATA $137.035999$, a factor-$370$ improvement over the bare
form with no free parameters. Both the tree term and this additive
zero-mode are Lean-formalised.

**Order of validity.**
The tree term and the additive $2/(3\pi)$ zero-mode are the derived
content, both Lean-formalised. The remaining $-4.2\;\mathrm{ppm}$ is a
next-order, Schwinger-type effect $\sim \alpha/(4\pi)$ whose denominator
$8\pi = \pi\,b_1$ is derived, but whose exact coefficient — an
$O(\alpha^2)$ Bloch-group normalisation in $B_3(\mathbb{C})$ over Bring's
ideal hyperbolic tetrahedra — is not yet closed; the higher-order forms
and their status are treated in
[α_EM derivation open problems](#rem:alpha-em-derivation-open-problems).
The fine-structure constant is therefore predicted parameter-free to
$\approx 4\;\mathrm{ppm}$ through the additive correction; the $O(\alpha)$
self-energy coefficient and everything beyond it remain open.

**Numerical comparison with CODATA.**

See [Table 1](#tbl:fine-structure-observation-table1-data).

**Inversion: $q$ from $\alpha_{\mathrm{EM}}$.**
Conversely, fixing $\alpha^{-1} \approx 137.036$ and solving for $q$
gives

$$
  q_{\mathrm{CODATA}} = 1.11023.
$$

This is consistent with the substrate parameter determined
independently from mass ratios
(mass predictions) and half-life
calculations ([half-life as $q$-probe](#rem:half-life-as-q-probe)),
providing a cross-check between the electromagnetic and strong
sectors.

**Sensitivity.**
The coupling is sensitive to $q$:

$$
  \frac{\partial \ln \alpha_{\mathrm{EM}}}{\partial \ln q}
  =  -1 - 
  \frac{9  q^9 [10]_q + 10  q^{10} [9]_q}
       {[9]_q [10]_q (q - q^{-1})}.
$$

At $q = q_0$ this evaluates to approximately $-20$: a $1\%$ shift
in $q$ produces a $\sim 20\%$ shift in $\alpha_{\mathrm{EM}}$.  The
tight agreement with experiment therefore constrains $q$ to a narrow
window around $q_0$.

**Comparison with other $q$-predictions.**

See [Table 2](#tbl:fine-structure-observation-table2-data).

The substrate parameter $q_0$ is overdetermined: three
independent classes of observables (electromagnetic coupling, mass
ratios, decay rates) all point to the same value.
