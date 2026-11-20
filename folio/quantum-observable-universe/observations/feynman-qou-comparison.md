The Bethe–Weizsäcker semi-empirical mass formula (SEMF) requires five fitted coefficients. The Wedderburn formula ([three-invariant mass formula](#thm:wedderburn-mass-formula)) derives binding from the Hecke algebra trace with zero fitted parameters. The SEMF is not the only external benchmark: modern nuclear theory is organised as a sequence of effective field theories (chiral, pionless, halo/cluster), each an expansion around a different low-energy limit of QCD with its own range of validity in energy and in nucleon number \cite{hammer2019}.

## Term dictionary

See [Table 1](#tbl:feynman-qou-comparison-table1-data).

## Comparison

See [Table 2](#tbl:feynman-qou-comparison-table2-data).

The $\mathfrak{m}_{\mathrm{QOU}}$ column of that table is the superseded convention-C table, not the adopted one: it gives $938.910$ for ${}^{1}\mathrm{H}$ and $3734.624$ for ${}^{4}\mathrm{He}$, where the adopted convention-D values are $935.352$ and $3740.383$. The per-$Z$ rows and the Winner column are therefore convention-C throughout. They are not recomputed here because the table declares no producer — it carries no `computation` block, so there is nothing to re-run, and the SEMF column has no derivation in the corpus either. Regenerating it needs a producer first.

The SEMF achieves a mean accuracy of $0.023\%$ using eight inputs and five fitted coefficients. The Wedderburn formula achieves $0.183\%$ using two inputs ($q_0$, $m_e$) and zero fitted parameters — about $7.9\times$ the SEMF error, against $3.2\times$ under the figure this supersedes.

That superseded figure was $0.074\%$, and it was a **convention-C** number. The canonical Markov convention is $z = q^{3}/(q^{2}+1)$ (convention D); recomputing $\Phi_1$ in it moves the mean to $0.183\%$ and the maximum to $0.321\%$. The convention was not chosen on accuracy, and a table fitting better in the superseded convention is what one expects of a table built in it. The zero-fitted-parameter claim is unaffected: convention D introduces no parameter.

## Sources of discrepancy

The error in the Wedderburn formula tracks the nuclear shell model:

* **Under-binding** for $Z = 3$--$10$. The transfer matrix chain overestimates $\Phi_1$.
* **Over-binding** for $Z = 11$--$20$. The $\mathrm{nn}/\mathrm{pp}$ asymmetry grows faster than the physical asymmetry energy.
* **Sign flip** near shell closures ($A = 4$, $A = 20$). The Hecke trace detects quantum coherence.

The near-zero volume at generator $k$ encodes nuclear saturation.

## Improving: the pion channel

Including the hook channel supplies missing shell structure.
