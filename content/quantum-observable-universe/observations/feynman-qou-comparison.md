The Bethe–Weizsäcker semi-empirical mass formula (SEMF) requires five fitted coefficients to compute nuclear binding energy. The Wedderburn formula ([three-invariant mass formula](#thm:wedderburn-mass-formula)) derives the same binding from the Hecke algebra trace with zero fitted parameters.

## Term dictionary

See [Table 1](#tbl:feynman-qou-comparison-table1-data).

The SEMF separates five physical effects using five fitted parameters ($a_V \approx 15.56$, $a_S \approx 17.23$, $a_C \approx 0.697$, $a_A \approx 23.29$, $\delta \approx 12$ MeV). The Wedderburn formula uses three channels ($\Phi_1$, $\Phi_2$, $\Phi_3$). Each channel mixes multiple SEMF effects through the transfer matrix chain.

## Comparison

See [Table 2](#tbl:feynman-qou-comparison-table2-data).

The SEMF achieves a mean accuracy of $0.023\%$ using eight inputs (five fitted, three CODATA). The Wedderburn formula achieves $0.074\%$ using two inputs ($q_0$, $m_e$) and zero fitted parameters. The Wedderburn formula outperforms the SEMF on 3 of the 20 atoms. The SEMF is $3.2\times$ more accurate, but requires $4\times$ more parameters.

## Sources of discrepancy

The error in the Wedderburn formula tracks the nuclear shell model via a characteristic sign pattern:

* **Under-binding** (predicted mass too light) for $Z = 3$--$10$ (p-shell). The transfer matrix chain overestimates $\Phi_1$ because the near-zero generator ($\hat{V} \approx 0.0015$) dominates.
* **Over-binding** (predicted mass too heavy) for $Z = 11$--$20$ (sd-shell). The $\mathrm{nn}/\mathrm{pp}$ asymmetry ($\Phi_2$ channel) grows faster than the physical asymmetry energy.
* **Sign flip** near shell closures ($A = 4$, $A = 20$). The Hecke trace detects quantum coherence near magic numbers. The SEMF smooth $A^{2/3}$ scaling misses this coherence entirely.

The near-zero volume at generator $k$ ($\hat{V}_k \approx 0.0015$, contributing $\ln\lvert\hat{V}_k\rvert \approx -6.50$ to $\Phi_1$) is universal for alternating $\mathfrak{p}\mathfrak{n}$ orderings with $A \geq 4$. It encodes nuclear saturation: each nucleon interacts only with its nearest neighbors. The effective range corresponds directly to the transfer matrix chain length.

## Improving: the pion channel

The $3\times$ accuracy gap between the SEMF and Wedderburn formulas corresponds to $O(10\;\mathrm{MeV})$ in binding energy. This is the scale of the shell correction. The $[n{-}2,2]$ hook representation (pion channel) vanishes exactly at magic numbers ([shell-transition knot](#conj:shell-transition-knot)). This creates discrete stability gaps that the three extremal channels miss. Including the hook channel supplies the missing shell structure.

**Witness**: `feynman-qou-comparison.witness.json`.
