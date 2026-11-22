Closed sub-links govern shell closure, determining both chemical reactivity and nuclear stability. A shell is closed precisely when its components separate as a self-contained Hopf sub-link. The table below provides the knot structure of atoms with $Z \leq 4$.

**Visual conventions.**

- **Solid trefoil** (filled): left trefoil $T_{2,3}$ (proton).
- **Outline trefoil** (unfilled): electron. The electron is the word $\sigma_0\sigma_1\sigma_0$, whose closure is the Hopf link; the figure draws its backup reading, the right trefoil $T_{2,3}^{\sigma}$.
- **Circle**: unknot $K_{0_1}$ (neutron).
- **Dashed circle**: mirror unknot $T_{1,0}^{\sigma}$ (antineutrino, see [antineutrino knot](#def:antineutrino-knot)).
- **Interlocked circles**: Hopf link $\mathcal{L}_H$ (the $\oplus$ binding operation).
- **$\alpha$**: alpha particle $2\mathfrak{p} \oplus 2\mathfrak{n}$ (helium-4 nucleus).
- **Bracket-star $[\cdots]^*$**: closed sub-Hopf link (splits from remaining components).
- **Green border**: closed $1s$ sub-link (2 electrons).
- **Blue border**: closed $2s$ sub-link (2 electrons).
- **Brown border**: nuclear sub-link (protons + neutrons).

| $Z$ | Atom | $N$ | Structure | $k_\alpha$ | Shells |
|----:|------|----:|-----------|---:|--------|
| 1 | H | 0 | $[\mathfrak{p}] \oplus e$ | 0 | $1s^1$ |
| 2 | He | 2 | $[\alpha] \oplus [T_{2,3} \oplus T_{2,3}]^*$ | 1 | $1s^2$ ${}^*$ |
| 3 | Li | 4 | $[3\mathfrak{p}4\mathfrak{n}] \oplus [e \oplus e]^* \oplus e$ | 1 | $1s^2 + 2s^1$ |
| 4 | Be | 5 | $[4\mathfrak{p}5\mathfrak{n}] \oplus [T \oplus T]^* \oplus [e \oplus e]^*$ | 2 | $1s^2 + 2s^2$ |

$e$ is the electron, the closure of $\sigma_0\sigma_1\sigma_0$ (the Hopf link; backup reading the trefoil $T_{2,3}$). Brackets $[\cdots]^*$ denote a closed sub-Hopf link.

**Observations.**

1. **Hydrogen** ($Z = 1$): A single proton $\mathfrak{p}$ links to a single electron $e$. There are no sub-links; the shell is open.
2. **Helium** ($Z = 2$): The $\alpha$ particle links to two electrons forming a closed Hopf pair. Both nuclear and electronic sub-links are closed. Helium is doubly stable.
3. **Lithium** ($Z = 3$): The $1s^2$ sub-link is closed, but the third electron links at a higher level. The $2s$ shell is open, leaving one valence electron.
4. **Beryllium** ($Z = 4$): Two closed electron pairs ($1s^2$ and $2s^2$) are Hopf-linked. The $2s$ shell is closed, but the $2p$ sub-shell has not started.

**Transfer matrix data.**

The nuclear link is encoded by transfer matrices ([transfer matrix operator](#def:transfer-matrix-operator)) with pair-dependent crossing coefficients. For light atoms:

| Atom | $A$ | $\binom{A}{2}$ steps | Pair types | $\deg P \leq$ |
|------|:---:|:---:|------------|:---:|
| H | 1 | 0 | — | 0 |
| He | 4 | 6 | 1 pp, 1 nn, 4 mix | 15 |
| Li | 7 | 21 | 3 pp, 6 nn, 12 mix | 48 |
| Be | 9 | 36 | 6 pp, 10 nn, 20 mix | 80 |

The photon-electron transfer matrix eigenvalue $\lambda_+ = 1.1073$ ([shell structure eigenvalues](#prop:shell-structure-eigenvalues)) governs shell structure. Hydrogen features one electron-proton junction ($T_{\gamma e}^1$); helium closes the $1s$ shell ($T_{\gamma e}^1 \otimes T_{\gamma e}^1$); lithium adds the first $2s$ electron ($T_{\gamma e}^2$) at the third junction.

See the [knot atom diagrams simulator](#sim:knot-atom-diagrams) for an interactive SVG version.
