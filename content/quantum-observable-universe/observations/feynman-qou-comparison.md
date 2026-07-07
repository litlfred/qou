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
