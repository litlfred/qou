The Bethe–Weizsäcker semi-empirical mass formula (SEMF) requires five fitted coefficients. The Wedderburn formula ([three-invariant mass formula](#thm:wedderburn-mass-formula)) derives binding from the Hecke algebra trace with zero fitted parameters. The SEMF is not the only external benchmark: modern nuclear theory is organised as a sequence of effective field theories (chiral, pionless, halo/cluster), each an expansion around a different low-energy limit of QCD with its own range of validity in energy and in nucleon number \cite{hammer2019}.

## Term dictionary

See [Table 1](#tbl:feynman-qou-comparison-table1-data).

The table pairs each SEMF term with a channel of the Wedderburn formula term by term. The Coulomb row is such a pairing, not a derivation: the determinant channel $\Phi_2$ is not shown to be a Coulomb pair term, and on two nucleon blocks no braid insertion or invariant pair coupling gives one at $n = 6$ (see [the Coulomb-charge definition](#def:coulomb-charge)).

## Comparison

See [Table 2](#tbl:feynman-qou-comparison-table2-data).

The $\mathfrak{m}_{\mathrm{QOU}}$ column in Table 2 records an unregenerated evaluation at the auxiliary loop parameter $z_{\mathrm{aux}} = 1/(q^{1/2}+q^{-1/2})$ ($938.910$ MeV for ${}^{1}\mathrm{H}$ and $3734.624$ MeV for ${}^{4}\mathrm{He}$, mean error $0.074\%$), whereas evaluating $\Phi_1$ at the canonical Markov parameter $z = q^{3}/(q^{2}+1)$ yields $935.352$ MeV for ${}^{1}\mathrm{H}$ and $3740.383$ MeV for ${}^{4}\mathrm{He}$, with mean error $0.183\%$ and maximum error $0.321\%$.

Across $Z = 1\text{--}20$, the five-parameter SEMF achieves a mean error of $0.023\%$ using eight inputs and five fitted coefficients, while the Wedderburn formula at $z = q^3/(q^2+1)$ achieves $0.183\%$ (about $7.9\times$ the SEMF mean error) using two inputs ($q_0$, $m_e$) and zero fitted parameters.

## Sources of discrepancy

The error in the Wedderburn formula tracks the nuclear shell model:

* **Under-binding** for $Z = 3$--$10$. The transfer matrix chain overestimates $\Phi_1$.
* **Over-binding** for $Z = 11$--$20$. The $\mathrm{nn}/\mathrm{pp}$ asymmetry grows faster than the physical asymmetry energy.
* **Sign flip** near shell closures ($A = 4$, $A = 20$). The Hecke trace detects quantum coherence.

The near-zero volume at generator $k$ encodes nuclear saturation.

## Improving: the pion channel

Including the hook channel supplies missing shell structure.
