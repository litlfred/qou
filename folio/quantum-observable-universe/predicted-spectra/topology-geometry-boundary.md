The categorical action $\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$ evaluated on a nuclear link $\mathcal{N}(Z, N)$ produces observables at two levels.

**Observables determined by $q$ alone.**

These derive from the Iwahori--Hecke algebra $H_A(q)$ evaluated at the substrate $q$, subject to the Descartes condition $\chi_{\mathrm{eu}}(M_0) = -6$:

See [Table](#tbl:topology-geometry-boundary-table-data).

**Observables not yet computed from $q$ alone.**

The $Q$-value for nuclei beyond the deuteron is the mass difference $M(\text{parent}) - M(\text{daughter}) - m_e$. It requires the terminal resolution of the full composite link $L_{3A}$. The pair Skein mass formula must be applied to all crossings with Hecke compounding. This computation is configured (braid registry, SnapPy, Singular/Hecke engine) but un-evaluated for $A > 2$.

The hadron mass formula $\mathfrak{m} = \mathrm{Vol}(K) / \hbar_q^2$ provides masses for the electron, muon, proton, and neutron. For multi-nucleon satellite links, the volume scales as $\mathrm{Vol} = A \times \mathrm{Vol}(\mathcal{B}_3)$. The nuclear binding energy emerges from the pair Skein mass $\mathcal{S}_{ab}(q) = (q\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$ evaluated at inter-nucleon crossings.

The $Q$-value represents a minute mass difference ($\sim 0.1$--$1$ MeV on a $\sim 10{,}000$--$200{,}000$ MeV background). Computing it demands high precision composite pair Skein weights. However, the framework already determines the structural properties of the $Q$-value (decay direction, shell blocking, and sensitivity) strictly from $q$.
