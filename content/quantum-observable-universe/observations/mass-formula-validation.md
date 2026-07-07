The atomic mass formula recombines CODATA nucleon masses and AME2020 binding energies tautologically.

## The ruler: $m_e$ as external scaling parameter

Converting dimensionless mass ratios into physical units requires one external input: $m_e \approx 0.511$ MeV. This fixes the absolute energy scale.

We derive the hadronic scale $E_0 = m_e/(q_0(q_0 - 1)) \approx 4.186$ MeV. This agrees with the calibrated scale $E_0^{(\mathrm{cal})} \approx 4.155$ MeV to $0.75\%$. The neutron $Q$-value is a prediction: $\mathfrak{Q}_\beta = |\Delta\mathrm{net}| \times E_0 \approx 0.788$ MeV.

## Genuine predictions of the substrate parameter $q$

The derivation chain yields:

- **Mass ratios**: $m_\mu/m_e = 206.768$ (definitional).
- **$Q$-values**: mass differences predicting higher-order spectral components.
- **Half-life ratios**: $\log_q(ft)$ values.

**Mass predictions**:

See [Table 1](#tbl:mass-formula-validation-table1-data).

Mean $|\Delta/M| = 0.010\%$ across 15 isotopes.

**Operator dressing**:

See [Table 2](#tbl:mass-formula-validation-table2-data).

**$Q$-values**:

See [Table 3](#tbl:mass-formula-validation-table3-data).

**Genuine predictions summary**:

See [Table 4](#tbl:mass-formula-validation-table4-data).

MAE is $4.4\%$ across all benchmarks.

## BW mass table

See [Table 5](#tbl:mass-formula-validation-table5-data).

All $\beta$-stable nuclei satisfy $|\Delta/M| < 0.04\%$. For $Z = N$ odd-odd nuclei, entanglement imbalance produces a residual $0.05\%$ error.

## Q-value table

See [Table 6](#tbl:mass-formula-validation-table6-data).

## Hecke-engine certificate validation

We compute exact Gröbner--Shirshov certificates for 47 isotopes. Each certificate contains $\mathrm{net}(q_0)$, $\mathrm{tr\_alt}(q_0)$, and $F_\mathrm{Pauli}(q_0)$. The fields encode combinatorial crossing structure, not direct mass.

## Certificate fields and the $6 \times 6$ transfer matrix

The certificate fields evaluate polynomials from the $6 \times 6$ transfer matrix of $H_3(q)$. This matrix captures all three irreps. The adjoint representation requires all three channels to compute $F_\mathrm{Pauli}$.

## Nucleon NF structure and binding receptivity

Negative coefficients indicate a deficit.

**Proton**:

See [Table 7](#tbl:mass-formula-validation-table7-data).

**Neutron**:

See [Table 8](#tbl:mass-formula-validation-table8-data).

Both nucleons demand identity and trefoil content. The neutron demands Hopf link content.

## The open problem: $B/A$ from $q$

Deriving $B/A$ directly from the certificate polynomial $P(q_0)$ remains open. Current approaches include evaluating the nuclear Skein volume integral, spectral decomposition, identifying a binding operator from normal form receptivity, and exploring certificate polynomial roots.

## Isotope coverage

See [Table 9](#tbl:mass-formula-validation-table9-data).

The Hecke engine scales as $O(A^2)$. Cobalt ($A = 60$) marks the current boundary.
