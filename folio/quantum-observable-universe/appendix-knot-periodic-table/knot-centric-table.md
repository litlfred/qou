Whereas the chemical periodic table arranges elements by electronic $(n, \ell)$ shells, a **knot-centric periodic table** arranges all $118$ elements ($Z = 1\text{--}118$) by nuclear Borromean shell closures and electronic trefoil resonance modes. Under this organization, nuclear magic numbers and sub-shell capacities arise directly from three-strand Borromean spin--orbit coupling and photon--electron transfer-matrix eigenvalues.

**Organizing principles.**

1. **Rows (nuclear major closures)**: Nuclear harmonic-oscillator levels $N_{\mathrm{osc}}$ and high-$j$ spin--orbit intruder shells ([shell-transition knot](#conj:shell-transition-knot)), terminating at proton closures $Z \in \{2, 8, 20, 28, 50, 82, 126\}$ ([Table 1](#tbl:knot-centric-table-table1-data)). Rows 1--3 close at isotropic harmonic-oscillator boundaries ($N_{\mathrm{osc}} = 0, 1, 2$); Rows 4--7 incorporate the high-$j$ intruder orbital ($1f_{7/2}$, $1g_{9/2}$, $1h_{11/2}$, $1i_{13/2}$) lowered by three-strand Borromean spin--orbit coupling, with known elements spanning up to oganesson ($Z = 118$) inside Row 7.
2. **Columns (Mayer--Jensen proton sub-shells)**: Left-to-right filling of proton $(nl_j)$ sub-shells of multiplicity $2j + 1$ ([Table 2](#tbl:knot-centric-table-table2-data)). Within each row, the leftmost cell opens the shell immediately past the preceding magic closure (the magic-receptive entry), and the rightmost cell completes the magic closure. Electronic shell energies follow the dominant eigenvalue $\lambda_+ = q_0 \approx 1.109979$ of the photon--electron transfer matrix $T_{\gamma e}(q_0)$ at the aether parameter $q_0$ ([shell structure eigenvalues](#prop:shell-structure-eigenvalues)).
3. **Topological invariants per cell**: Tetrahedral $\alpha$-cluster count $k_\alpha = \min(\lfloor Z/2 \rfloor, \lfloor N/2 \rfloor)$, seniority pairing parity, and magic-closure membership ($\diamond$ for proton closures, $\star$ for neutron closures).

**Transfer-matrix backbone and skein completeness.**

Pairwise nuclear crossings evaluate the factored nuclear skein product $P_{\mathcal{N}}(q_0) = \prod_{i=0}^{A-2} \hat{V}_i(q_0)$ ([Skein polynomial](#prop:skein-polynomial-transfer-matrix)) across $\binom{A}{2}$ $2 \times 2$ transfer matrices ([transfer matrix operator](#def:transfer-matrix-operator)) governed by the three isospin-pair channel weights in [Table 3](#tbl:knot-centric-table-table3-data). Isobaric beta transitions apply the universal perturbation $\Delta_\beta(q_0)$ ([beta decay matrix](#prop:beta-decay-transfer-matrix)) at the converting nucleon. Every constituent knot has Seifert genus at most $4$ and is generated from the torus basis ([generation completeness](#thm:generation-completeness)), with irreducible summands detected via Alexander surjectivity and Markov non-degeneracy ([knot exhaustiveness](#rem:knot-exhaustiveness)).

**Cell data summary.**

Each element cell $(Z, N)$ records:

- **Element symbol**, atomic number $Z$, reference mass number $A$, and neutron count $N$;
- **Nuclear cluster decomposition** $k_\alpha \alpha \oplus (Z - 2k_\alpha)\mathfrak{p} \oplus (N - 2k_\alpha)\mathfrak{n}$;
- **Proton $(nl_j)$ sub-shell** and electronic trefoil shell configuration;
- **Pairwise skein complexity**: $\binom{A}{2}$ transfer steps and polynomial degree bound $A^2 - 1$;
- **Derived binding and mass**: $B_{\mathrm{QOU}}(Z, N)/A$ and $M_{\mathrm{QOU}}(Z, N)$ from [knot-periodic table of the elements](#prose:knot-periodic-table).
