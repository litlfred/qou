The Bethe--Weizsäcker semi-empirical mass formula (SEMF) decomposes
nuclear binding into five independent physical effects, each with a
fitted coefficient.  The QOU three-channel Wedderburn formula
([three-invariant mass formula](#thm:wedderburn-mass-formula))
produces binding from the Hecke algebra trace alone, with zero
fitted parameters.

## SEMF vs QOU term-by-term comparison

### Term dictionary

See [Table 1](#tbl:feynman-qou-comparison-table1-data).

The SEMF separates five physically distinct effects with five
fitted coefficients ($a_V \approx 15.56$, $a_S \approx 17.23$,
$a_C \approx 0.697$, $a_A \approx 23.29$, $\delta \approx 12$ MeV).
The QOU formula has three channels ($\Phi_1$, $\Phi_2$, $\Phi_3$),
each mixing multiple SEMF effects through the transfer matrix chain.

### Comparison

See [Table 2](#tbl:feynman-qou-comparison-table2-data).

SEMF mean: $0.023\%$ (5 fitted + 3 CODATA = 8 inputs).
QOU mean: $0.074\%$ (0 fitted, 2 inputs: $q_0$, $m_e$).
QOU wins 3/20 atoms.  Accuracy ratio: SEMF is $3.2\times$ better
with $4\times$ more parameters.

### Sources of discrepancy

The QOU error has a characteristic sign pattern that tracks
the **nuclear shell model**:

- **Under-binding** (QOU lighter) for $Z = 3$--$10$ (p-shell):
  the transfer matrix chain overestimates $\Phi_1$ because the
  near-zero generator ($\hat{V} \approx 0.0015$) dominates.
- **Over-binding** (QOU heavier) for $Z = 11$--$20$ (sd-shell):
  the increasing nn/pp asymmetry ($\Phi_2$ channel) grows faster
  than the actual asymmetry energy.
- **Sign flip** near shell closures ($A = 4$, $A = 20$): the
  Hecke trace detects quantum coherence near magic numbers that
  the SEMF's smooth $A^{2/3}$ scaling misses.

The near-zero volume at generator $k$ (where $\hat{V}_k \approx
0.0015$, contributing $\ln\lvert\hat{V}_k\rvert \approx -6.50$
to $\Phi_1$) is a universal feature of alternating $\mathfrak{p}\mathfrak{n}$ orderings
with $A \geq 4$.  It encodes **nuclear saturation**: each nucleon
interacts only with its nearest neighbors, and the effective range
is encoded in the transfer matrix chain length.

### Improving: the pion channel

The $3\times$ accuracy gap corresponds to $O(10\;\mathrm{MeV})$
in binding energy — the shell correction.  The $[n{-}2,2]$ hook
representation (pion channel) vanishes exactly at magic numbers
([shell-transition knot](#conj:shell-transition-knot)), creating
discrete stability gaps that the three extremal channels miss.
Including the hook channel would provide the missing shell structure.

**Witness**: `feynman-qou-comparison.witness.json`.
