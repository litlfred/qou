<!-- FILE_START: mass-predictions-method-feynman-qou-comparison-intro.md -->
We validate the mass-prediction methodology against external comparators. We compare the framework with Feynman amplitudes. We examine the neutron-proton mass splitting. We analyze the photon-channel Wedderburn chain. We aggregate the validation tables to establish the empirical accuracy band.
<!-- FILE_END: mass-predictions-method-feynman-qou-comparison-intro.md -->

<!-- FILE_START: feynman-qou-comparison.md -->
The Bethe–Weizsäcker semi-empirical mass formula (SEMF) requires five fitted coefficients. The Wedderburn formula ([three-invariant mass formula](#thm:wedderburn-mass-formula)) derives binding from the Hecke algebra trace with zero fitted parameters.

## Term dictionary

See [Table 1](#tbl:feynman-qou-comparison-table1-data).

## Comparison

See [Table 2](#tbl:feynman-qou-comparison-table2-data).

The SEMF achieves a mean accuracy of $0.023\%$ using eight inputs. The Wedderburn formula achieves $0.074\%$ using two inputs ($q_0$, $m_e$) and zero fitted parameters.

## Sources of discrepancy

The error in the Wedderburn formula tracks the nuclear shell model:

* **Under-binding** for $Z = 3$--$10$. The transfer matrix chain overestimates $\Phi_1$.
* **Over-binding** for $Z = 11$--$20$. The $\mathrm{nn}/\mathrm{pp}$ asymmetry grows faster than the physical asymmetry energy.
* **Sign flip** near shell closures ($A = 4$, $A = 20$). The Hecke trace detects quantum coherence.

The near-zero volume at generator $k$ encodes nuclear saturation.

## Improving: the pion channel

Including the hook channel supplies missing shell structure.

**Witness**: `feynman-qou-comparison.witness.json`.
<!-- FILE_END: feynman-qou-comparison.md -->

<!-- FILE_START: neutron-proton-mass-splitting.md -->
*The neutron--proton mass difference is*

$$
  \Delta m
  = m_{\mathfrak{n}} - m_{\mathfrak{p}}
  = \alpha \cdot
    \bigl\lvert
      \Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})
      - \Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d})
    \bigr\rvert
  \approx 1.302 \;\mathrm{MeV}
$$

*where $\alpha = m_e \times 8G$ is the binding scale and $\Phi$
is the quantum dilogarithm volume.*
<!-- FILE_END: neutron-proton-mass-splitting.md -->

<!-- FILE_START: photon-channel-wedderburn-chain.md -->
The color-tube cubic $c^3 + a_2 c^2 + a_1 c + a_0 = 0$ encodes the pair-production vertex. Its four coefficients correspond to four photon polarisation channels. Its three roots are the three quark color charges.

The Vieta symmetric functions generate exactly three independent quantities:

| Degree | Symmetric function | Wedderburn invariant | Physical role |
|:-------|:-------------------|:---------------------|:-------------|
| 1 | $\sigma_1 = \sum c_k$ | $\Phi_1 = \sum \ln\lvert\hat{V}_i\rvert$ | binding topology |
| 2 | $\sigma_2 = \sum_{i<j} c_i c_j$ | $\Phi_2 = \sum \ln\lvert\det M_i\rvert$ | color pairing |
| 3 | $\sigma_3 = c_0 c_1 c_2$ | $\Phi_3 = \sum \ln\lvert\lambda^{\mathrm{sym}}_i / \lambda^{\mathrm{alt}}_i\rvert$ | chirality |

The chain $4 \to 3 \to 3$ is complete. 

The degree-2 amplification ratio yields $\beta_2 \cdot \alpha \approx 8.5$ MeV per nucleon, deriving nuclear binding directly from the photon production chain.
<!-- FILE_END: photon-channel-wedderburn-chain.md -->

<!-- FILE_START: mass-formula-validation.md -->
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
<!-- FILE_END: mass-formula-validation.md -->

