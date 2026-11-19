Closed sub-links govern shell closure, determining both chemical reactivity and nuclear stability. A shell is closed precisely when its constituent components separate as a self-contained sub-link within the composite atomic diagram. For the lightest elements ($Z \leq 4$), the interplay between nuclear $\alpha$-clustering and electronic $1s/2s$ shell closure already exhibits the full topological grammar of the periodic table.

**Topological and visual conventions.**

- **Proton** $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$: three-strand flavored Borromean baryon, the Markov closure $\widehat{(\sigma_1 \sigma_2^{-1})^3}$ in $B_3$ ([Borromean baryon](#def:borromean-baryon)).
- **Neutron** $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}\mathfrak{d}\mathfrak{d})$: three-strand flavored Borromean baryon $\widehat{(\sigma_1 \sigma_2^{-1})^3}$ with down-flavored crossing replacement.
- **Electron** $e^- = T_{2,3} = 3_1$: trefoil fermion $\widehat{\sigma_1^3}$ in $B_2$ (mirror trefoil $T_{2,3}^{\sigma}$ for the positron $e^+$).
- **Neutrino and antineutrino**: unknot $0_1 = T_{1,0}$ and mirror unknot $T_{1,0}^{\sigma}$ ([antineutrino knot](#def:antineutrino-knot)).
- **Hopf link** $\mathcal{L}_H = \widehat{\sigma_1^2}$: pairwise linking operation $\oplus$ coupling nuclear and electronic sectors.
- **Alpha cluster** $\alpha = 2\mathfrak{p} \oplus 2\mathfrak{n}$: closed tetrahedral $K_4$ four-nucleon singlet (${}^{4}\mathrm{He}$ core).
- **Bracket-star $[\cdots]^*$**: closed sub-Hopf shell splitting cleanly from outer valence components (green border $= 1s^2$, blue border $= 2s^2$, brown border $=$ nuclear core).

| $Z$ | Atom | $N$ | Composite knot formula | $k_\alpha$ | Electron shells |
|----:|:----:|----:|:-----------------------|---:|:----------------|
| 1 | ${}^{1}\mathrm{H}$ | 0 | $[\mathfrak{p}] \oplus T_{2,3}$ | 0 | $1s^1$ |
| 2 | ${}^{4}\mathrm{He}$ | 2 | $[\alpha]^* \oplus [T_{2,3} \oplus T_{2,3}]^*$ | 1 | $1s^2\,{}^*$ |
| 3 | ${}^{7}\mathrm{Li}$ | 4 | $[\alpha \oplus \mathfrak{p} \oplus 2\mathfrak{n}] \oplus [T_{2,3} \oplus T_{2,3}]^* \oplus T_{2,3}$ | 1 | $1s^2\,2s^1$ |
| 4 | ${}^{9}\mathrm{Be}$ | 5 | $[2\alpha \oplus \mathfrak{n}] \oplus [T_{2,3} \oplus T_{2,3}]^* \oplus [T_{2,3} \oplus T_{2,3}]^*$ | 2 | $1s^2\,2s^2$ |

**Shell-closure patterns ($Z \leq 4$).**

1. **Hydrogen** ($Z = 1$, ${}^{1}\mathrm{H}$): A single Borromean proton $\mathfrak{p}$ links to one trefoil electron $T_{2,3}$; no paired sub-link closes, leaving an open $1s^1$ valence shell.
2. **Helium** ($Z = 2$, ${}^{4}\mathrm{He}$): Four Borromean nucleons close into a Wigner-singlet $\alpha$ tetrahedron while two trefoil electrons form a closed $1s^2$ Hopf pair, rendering ${}^{4}\mathrm{He}$ doubly closed in both nuclear and electronic sectors.
3. **Lithium** ($Z = 3$, ${}^{7}\mathrm{Li}$): Beyond the closed $\alpha$ core and closed $1s^2$ pair, one unpaired valence proton and two neutrons occupy the $1p_{3/2}$ nuclear subshell while a third trefoil electron opens the $2s^1$ shell.
4. **Beryllium** ($Z = 4$, ${}^{9}\mathrm{Be}$): Two $\alpha$ clusters stabilized by one valence neutron bind to two closed electronic Hopf pairs ($1s^2$ and $2s^2$) prior to opening the $2p$ subshell.

**Transfer-matrix complexity on light nuclei.**

Pairwise nuclear crossings are evaluated by $2 \times 2$ transfer matrices ([transfer matrix operator](#def:transfer-matrix-operator)) over the $\binom{A}{2}$ nucleon pairs:

| Nuclide | $A$ | $\binom{A}{2}$ steps | Nucleon-pair decomposition | $\deg P_{\mathcal{N}} \leq$ |
|:-------:|:---:|:---:|:---------------------------|:---:|
| ${}^{1}\mathrm{H}$ | 1 | 0 | — | 0 |
| ${}^{4}\mathrm{He}$ | 4 | 6 | $1\,\mathfrak{p}\mathfrak{p},\; 1\,\mathfrak{n}\mathfrak{n},\; 4\,\mathfrak{p}\mathfrak{n}$ | 15 |
| ${}^{7}\mathrm{Li}$ | 7 | 21 | $3\,\mathfrak{p}\mathfrak{p},\; 6\,\mathfrak{n}\mathfrak{n},\; 12\,\mathfrak{p}\mathfrak{n}$ | 48 |
| ${}^{9}\mathrm{Be}$ | 9 | 36 | $6\,\mathfrak{p}\mathfrak{p},\; 10\,\mathfrak{n}\mathfrak{n},\; 20\,\mathfrak{p}\mathfrak{n}$ | 80 |

At the aether parameter $q_0$, the dominant photon--electron transfer-matrix eigenvalue $\lambda_+ = q_0 \approx 1.109979$ ([shell structure eigenvalues](#prop:shell-structure-eigenvalues)) governs electronic shell scaling: hydrogen exercises a single electron--proton junction ($T_{\gamma e}^1$), helium closes the $1s^2$ tensor pair ($T_{\gamma e}^1 \otimes T_{\gamma e}^1$), and lithium opens the $2s$ level ($T_{\gamma e}^2$). Interactive SVG diagrams appear in the [light-atom knot simulator](#sim:knot-atom-diagrams).
