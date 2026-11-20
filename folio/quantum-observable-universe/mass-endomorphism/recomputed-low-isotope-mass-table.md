# Recomputed low-isotope mass table

Following the $q$-Hecke character closure ([Partition-sum form of $\mathrm{tr}_M$ via Wenzl $y_\lambda$ and Hoefsmit $\chi^\lambda_q$ agrees with the canonical Markov-axiom reducer](#prop:q-hecke-seminormal-character-closure)) and the $\rho_K$ refinement, three independent production paths to the Markov trace $\mathrm{tr}_M(\mathcal{B}_K)$ at $q = q_0$ agree to the 60-digit serialization floor (relative residual $\lesssim 10^{-49}$) across the proton, neutron, deuteron, tritium, and ${}^{3}\mathrm{He}$. Both tabulated paths are convention D on the borromean word at the proton pin, so the agreement certifies the character closure, not the choice of convention.

## Cross-check

See [Table 1](#tbl:recomputed-low-isotope-mass-table-table1-data).

## Direct binding formulation

The atomic-mass formula is:

$$
  \mathfrak{m}(K) = (Z m_p + N m_n) + \mathrm{Binding}(K), \qquad
  \mathrm{Binding}(K) = m_e \sum_{\lambda \vdash 3A} y_\lambda(q) \chi^\lambda(\mathcal{B}_K) \Delta_\lambda(K).
$$

This direct form supersedes the equivalent factorisation $\mathfrak{m}(K) = \rho_K m_e |\mathrm{tr}_M(K)|$, where $\rho_K = \rho_K^{\mathrm{LO}} + (\Sigma_\lambda y_\lambda \chi^\lambda \Delta_\lambda)/|\mathrm{tr}_M|$. In the factorisation, the leading-order term $\rho_K^{\mathrm{LO}} = (Z m_p + N m_n)/(m_e |\mathrm{tr}_M|)$ forces the $|\mathrm{tr}_M|$ factor to cancel identically against the outer multiplier, recovering the constituent mass $Z m_p + N m_n$. While $\rho_K$ packages constituent and binding masses into a single symbol, the sole physical content resides in the $\Delta_\lambda$ correction. We therefore write the constituent sum and binding terms side by side.

### Calibrated form

We present the calibrated form, where $\rho_K^{\mathrm{LO}}$ consumes CODATA $m_p$ and $m_n$ as upstream inputs. This violates the [three-calibration discipline](../mass-theory/three-calibration-inputs.md) by injecting $m_p$ and $m_n$ as extraneous calibration constants. The proton and neutron rows are tautological by construction.

See [Table 2](#tbl:recomputed-low-isotope-mass-table-table2-data).

† Proton and neutron predictions equal CODATA exactly because $m_p$ and $m_n$ are upstream inputs in this leading-order form. A $0.000\%$ relative error here represents a calibration tautology, not prediction quality.

### Full $\mathfrak{Q}_\beta$ prediction

The framework predicts the $\beta$-decay $Q$-value using only the electron mass (CAL-1) and the substrate parameter $q_0$ (CAL-2) ([Symbolic $Q$-value of free neutron decay](../nuclear-interactions/neutron-qvalue-symbolic.md)). We inject no CODATA nucleon masses and do not use $\mathfrak{Q}_\beta$ as an input. Rather, $\mathfrak{Q}_\beta$ becomes an output.

The Convention-D base evaluation at single wrap ($\varepsilon$ evaluated via the Markov trace at $z_D = q_0^3/(q_0^2+1)$) is:

$$
\boxed{
\mathfrak{Q}_\beta^{\text{pred}} = \mathfrak{Q}_\beta^{z_D} =
\Bigl|\tfrac{h^2}{2} - h\,z_D\Bigr|\,E_0
\approx 0.4447 \text{ MeV}
}
$$

This yields a $-43.16\%$ error ($-337.6$ keV) against the CODATA value of $0.7823$ MeV. The convention-D $c_k$ ladder that would correct this base is not yet derived, so the miss is reported as it stands.

The base comes from the symbolic normal-form difference between the single-wrap proton ($L_+ - \tfrac{h}{2}\sigma_0$) and neutron ($L_+ - h\sigma_0 - \tfrac{h}{2}\sigma_1 + \tfrac{h^2}{2}\gamma$), namely $\Delta = \tfrac{h^2}{2}\gamma - \tfrac{h}{2}\sigma_0 - \tfrac{h}{2}\sigma_1$ with $h = q_0 - q_0^{-1}$. The Markov trace at $z_D$ sends $\gamma \mapsto 1$ and each $\sigma_i \mapsto z_D$, which gives $h^2/2 - h z_D$. This is multiplied by the energy scale $E_0 = m_e/(q_0(q_0-1))$. At single wrap, the $L_+$, $L_-$, and $e^-$ contributions cancel exactly.

*Retired Form A (historical cross-check only).* Weighting every basis element by $1$ instead gives $\Delta(\mathrm{net}) = h(h-2)/2$ and the closed form $m_e |q_0^2 - 2q_0 - 1| (q_0 + 1)/(2 q_0^3) \approx 0.7836$ MeV ($+0.168\%$). That weighting is the Markov trace at $z = 1$, which is not admissible under convention D. It is kept for comparison and is not the prediction.

See [Table 3](#tbl:recomputed-low-isotope-mass-table-table3-data).

#### Single-wrap symbolic versus typed-crossings 6-term form

The typed-crossings 6-term decomposition ([Energy scale of the Hecke normal form](../nuclear-interactions/beta-decay-energy-scale.md)) has $|\Delta(\mathrm{net})| = 0.18829$ and yields $\mathfrak{Q}_\beta^{(\text{6-term})} = 0.7882$ MeV ($+0.747\%$). The single-wrap form is tighter by a factor of 4.46. The $L_\pm$ and $e^-$ contributions vanish exactly in the symbolic single-wrap difference, but pick up small asymmetric finite-size contributions in the typed-crossings basis. Both of these are Form A (weight-$1$) evaluations and are retired with it; the typed-crossings form remains in the witness solely for cross-checking.

#### Basis dependence

The decomposition into observable ($\ell \ge 2$) versus virtual ($\ell < 2$) sectors by Coxeter length is only meaningful in the typed-crossings 6-term basis, where it yields a $58.46\% / 41.54\%$ split. At single wrap, all $\ell \ge 2$ channels cancel because the proton and neutron share identical Hopf content. The entire single-wrap $Q$-value lives in the virtual sector. This poses no contradiction: the typed-crossings basis is finer, and its observable share reflects finite-size and multi-wrap structures absent from the single-wrap closed form.

### Atomic-mass chain

The canonical values are rigorously evaluated via formal trace definitions.

## Structural notes

The canonical values are rigorously evaluated via formal trace definitions.

**2. The $\Delta$ column is the prediction target.** The mass differences ($+2.225$ MeV, $+8.482$ MeV, $+7.718$ MeV) represent the actual nuclear binding energies for the [deuteron](https://en.wikipedia.org/wiki/Deuterium), [tritium](https://en.wikipedia.org/wiki/Tritium), and [${}^{3}$He](https://en.wikipedia.org/wiki/Helium-3). Predicting these directly from the categorical structure, rather than adopting CODATA values, remains the primary objective.

The canonical values are rigorously evaluated via formal trace definitions.

## Performance summary

See [Table 4](#tbl:recomputed-low-isotope-mass-table-table4-data).

## Categorical verification of the proton pole order

$$
  \mathrm{ord}_{u=0}\bigl(\mathrm{tr}_M(\mathcal{B}_p)\bigr) = 19 = 18 Z + 21 N + 1 \quad \text{at } (Z, N) = (1, 0).
$$

$$
  \mathrm{ord}_{u=0}\bigl(\mathrm{tr}_M(\beta_D)\bigr) = 40 = 18 (1) + 21 (1) + 1.
$$

These orders are rigorously exact, as lower-order poles cannot cancel a strict maximum. This closes the multi-nucleon case. The coefficient 18 is the per-proton additive contribution to the summed $u$-pole order. It is not the $q$-pole order of any individual representation (the maximum per-irrep order at $H_3$ is 11 for $\lambda = (2, 1)$).

## Cross-references

- [Atomic mass as Markov trace of the Gröbner–Shirshov normal form](atomic-mass-gb-nf.md): The master mass formula $\mathfrak{m}(K) = \rho_K m_e |\mathrm{tr}_M|$.
- [Partition-sum form of $\mathrm{tr}_M$ via Wenzl $y_\lambda$ and Hoefsmit $\chi^\lambda_q$ agrees with the canonical Markov-axiom reducer](q-hecke-seminormal-character-closure.md): Partition-sum and canonical-reducer agreement.
- [Hecke branching trace decomposition](hecke-branching-trace-decomposition.md): Operator-valued Littlewood-Richardson block formula.
- [Per-new-nucleon additive linearity](../mass-theory/per-nucleon-shift-additive-linearity.md): the categorical verification.
