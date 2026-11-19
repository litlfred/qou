The electromagnetic coupling ([EM coupling projection](#prop:em-coupling-projection)) predicts $\alpha_{\mathrm{EM}}$ directly from the substrate parameter $q$. It requires zero free parameters.

**Bare formula.**
$$
  \alpha_{\mathrm{EM}}^{-1}(q)
  = 
  q \cdot [9]_q \cdot [10]_q
  = 136.823.
$$

The force-carrier generators $T_{2,9}$ and $T_{3,5}$ ([force identification](#rem:force-knot-identification)) dictate the crossing numbers $9$ and $10$. The Descartes substrate parameter fixes the $q$-integers.

**Derived correction.**
The leading correction to the bare formula is additive. It derives from the photon infrared zero-mode on Bring's surface ([photon IR zero-mode](#prop:photon-ir-zero-mode-bring)):

$$
  \alpha_{\mathrm{EM}}^{-1}(q) = q \cdot [9]_q \cdot [10]_q + \frac{2}{3\pi},
  \qquad \frac{2}{3\pi} = \frac{b_1(M_{\mathrm{Bring}})}{\mathrm{Area}(M_{\mathrm{Bring}})}
  = \frac{2g}{4\pi(g-1)}\Big|_{g=4}.
$$

The genus-$4$ topology fixes $b_1 = 2g = 8$ and the Gauss–Bonnet area. The corrected value is $137.0354$. This leaves a $-4.2\;\mathrm{ppm}$ residual against the CODATA value of $137.035999$. This additive correction improves the bare form by a factor of $370$.

**Self-energy correction.**
The remaining $-4.2\;\mathrm{ppm}$ is a Schwinger-type self-energy effect, and its coefficient is not an unknown: it is $H = [2]_q/(8\pi)$, whose denominator $8\pi = \pi\,b_1$ is fixed by the same genus-$4$ topology as the zero mode. Because $[2]_q/2 = 1.00545$ at the substrate value, $H$ is the $q$-deformation of the classical Schwinger coefficient $1/(4\pi)$, exceeding it by $0.545\%$. Retaining it, together with the cubic factor $(1 - h^2\alpha)$ where $h = q - q^{-1}$ is the Hecke structure constant, gives

$$
  \alpha_{\mathrm{EM}}^{-1}(q)
  = q\,[9]_q\,[10]_q + \frac{2}{3\pi} + \alpha H (1 - h^2 \alpha) + \Delta_2 .
$$

Since $\alpha$ stands on both sides, this is solved as a fixed point rather than evaluated as a series. The result is $137.035999127$, a residual of $+0.313$ parts per billion — roughly $2.1$ times the CODATA uncertainty, and about $13{,}600$ times closer than the additive form quoted above.

What remains genuinely open is $\Delta_2$, the archimedean two-loop term: a weight-three, $\zeta(3)$-type Bloch-group normalisation in $B_3(\mathbb{C})$ over the ideal hyperbolic tetrahedra of Bring's surface ([α_EM derivation open problems](#rem:alpha-em-derivation-open-problems)). It is distinct from the weight-one $-h^2H\alpha^2$ term already carried in the form. The underlying genus-4 Bring geometry — the cohomological genus $g = 4$ ($b_1 = 2g = 8$, Gauss–Bonnet ratio $2/(3\pi)$), the Jacobian $E^4$ Hodge zero-mode decomposition, the gerbe $40$-prefactor, and the equivariant Hurwitz homology — is proved, and the Form-B Bring–Schwinger cubic fixed point reaches $\alpha_{\mathrm{EM}}^{-1} \approx 137.036009$ ($+71\;\mathrm{ppb}$ at bare level, or $\sim 16\;\mathrm{ppb}$ with the one-loop Schwinger shift, down from $-468\;\mathrm{ppb}$ for the multiplicative Chern–Simons resummation); what remains conditional is the analytic continuum identification of the higher-loop QED / Bloch-group term $\Delta_2$.

**Numerical comparison.**
See [Table 1](#tbl:fine-structure-observation-table1-data).

**Inversion: $q$ from $\alpha_{\mathrm{EM}}$.**
Fixing $\alpha^{-1}$ at the CODATA value and solving for $q$ yields

$$
  q_\alpha = 1.10997858247973714 .
$$

The inversion must be run on the full form above; inverting the additive form alone returns $1.11023$, which is $226\;\mathrm{ppm}$ away and reflects the missing self-energy term rather than any property of the substrate.

Against the substrate parameter $q_0 = 1.109978582751\ldots$ pinned on the proton ratio, $q_\alpha$ sits $0.245$ parts per billion away; against the muon pin it sits $11.8$ ppb away. The electromagnetic sector therefore agrees with the proton anchor to sub-ppb and identifies the muon as the outlier, which is the same muon–proton substrate tension that appears in the mass sector, seen here in a third independent observable ([half-life as $q$-probe](#rem:half-life-as-q-probe)). The agreement is a genuine cross-check rather than a fit: no coefficient was adjusted, only $q$ solved for.

**Sensitivity.**
The coupling depends steeply on $q$:

$$
  \frac{\partial \ln \alpha_{\mathrm{EM}}}{\partial \ln q}
  =  -1 - 
  \frac{9  q^9 [10]_q + 10  q^{10} [9]_q}
       {[9]_q [10]_q (q - q^{-1})}.
$$

At $q = q_0$, this derivative is approximately $-20$. A $1\%$ shift in $q$ drives a $\sim 20\%$ shift in $\alpha_{\mathrm{EM}}$. The empirical agreement bounds $q$ around $q_0$.

**Comparison.**
See [Table 2](#tbl:fine-structure-observation-table2-data).

The substrate parameter $q_0$ is overdetermined: the electromagnetic coupling, the mass ratios and the decay rates each determine it independently. They do not converge on an identical value, and the residual spread is informative rather than noise. The electromagnetic and proton-mass determinations agree to sub-ppb, while the muon ratio sits some $11.5$ ppb away — a discrepancy far larger than either determination's own precision, and the reason the experimental pin is taken on the proton.
