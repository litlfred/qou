The atomic mass formula recombines CODATA nucleon masses and AME2020 binding energies tautologically.

## The ruler: $m_e$ as external scaling parameter

Converting dimensionless mass ratios into physical units requires one external input: $m_e \approx 0.511$ MeV. This fixes the absolute energy scale.

The hadronic scale evaluates to $E_0 = m_e/(q_0(q_0 - 1)) \approx 4.186$ MeV. This agrees with the calibrated scale $E_0^{(\mathrm{cal})} \approx 4.155$ MeV to $0.75\%$. The neutron $Q$-value is a prediction: $\mathfrak{Q}_\beta = |\Delta\mathrm{net}| \times E_0 \approx 0.788$ MeV.

## Genuine predictions of the aether parameter $q$

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

### Scope of the relative splitting ratio $\Delta/M$

The denominator in Table 5 is the **atomic mass**, which is not a quantity
this framework predicts: absolute mass is $m_e$ times a dimensionless ratio,
and $m_e$ fixes the MeV scale by fiat as CAL-1, so a MeV figure carries no
content beyond the ratio. Normalising a residual by it therefore divides a
binding-scale error by a nucleon-scale mass, and the ratio is small for that
reason rather than because the prediction is close.

Against the **binding energy** $B$ — the extensive quantity the framework
does predict — the same residuals of Table 5 read:

| Atom | $\Delta$ (MeV) | $\Delta/M$ | $B_{\mathrm{AME}}$ (MeV) | $|\Delta|/B$ |
|:-----|---------------:|-----------:|-------------------------:|-------------:|
| ${}^4$He | $+0.079$ | $0.002\%$ | $28.296$ | $0.28\%$ |
| ${}^6$Li | $+2.191$ | $0.039\%$ | $31.995$ | $6.85\%$ |
| ${}^7$Li | $+1.740$ | $0.027\%$ | $39.245$ | $4.43\%$ |
| ${}^9$Be | $+1.234$ | $0.015\%$ | $58.165$ | $2.12\%$ |
| ${}^{10}$B | $+0.648$ | $0.007\%$ | $64.751$ | $1.00\%$ |
| ${}^{12}$C | $+0.618$ | $0.006\%$ | $92.162$ | $0.67\%$ |

So ${}^6$Li, the row against which the $0.04\%$ bound is tightest, is
$6.85\%$ of the binding it is meant to reproduce — a factor of $176$ between
the two normalisations. The bound as stated is a statement about the choice
of denominator at least as much as about the accuracy of the formula.

The ${}^1$H row is not an accuracy result at all. Hydrogen is a free
nucleon: it has no binding energy, and Table 1 classifies it as such. Its
agreement to $10^{-6}\%$ is the $m_e$ scale returning the value that was put
in, the same round-trip for which the per-observable dashboard excludes
$m_p$ from scoring.

## Q-value table

See [Table 6](#tbl:mass-formula-validation-table6-data).

## Hecke-engine certificate validation

Exact Gröbner--Shirshov certificates have been computed for 47 isotopes. Each certificate contains $\mathrm{net}(q_0)$, $\mathrm{tr\_alt}(q_0)$, and $F_\mathrm{Pauli}(q_0)$. The fields encode combinatorial crossing structure rather than direct mass.

## Certificate fields and the $6 \times 6$ transfer matrix

The certificate fields evaluate polynomials from the $6 \times 6$ transfer matrix of $H_3(q)$. This matrix captures all three irreps. The adjoint representation requires all three channels to compute $F_\mathrm{Pauli}$.

## Nucleon NF structure and binding receptivity

Negative coefficients indicate a deficit.

**Proton**:

See [Table 7](#tbl:mass-formula-validation-table7-data).

**Neutron**:

See [Table 8](#tbl:mass-formula-validation-table8-data).

Both nucleons demand identity and trefoil content. The neutron demands Hopf link content.

## Unresolved direction: $B/A$ directly from $P(q_0)$

Deriving $B/A$ directly from the certificate polynomial $P(q_0)$ alone is unproved. Current approaches include evaluating the nuclear Skein volume integral, spectral decomposition, identifying a binding operator from normal form receptivity, and exploring certificate polynomial roots.

## Isotope coverage

See [Table 9](#tbl:mass-formula-validation-table9-data).

The Hecke engine scales as $O(A^2)$. Cobalt ($A = 60$) marks the current boundary.
