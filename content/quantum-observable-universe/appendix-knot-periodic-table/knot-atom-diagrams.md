The following table shows the knot structure of each atom with
$Z \leq 4$, with closed sub-Hopf links indicated.

**Visual conventions.**

- **Solid trefoil** (filled): left trefoil $T_{2,3}$ — the
  proton quark constituent.
- **Outline trefoil** (unfilled): right trefoil
  $T_{2,3}^{\sigma}$ — the electron.
- **Circle**: unknot $K_{0_1}$ — the neutron.
- **Dashed circle**: mirror unknot $T_{1,0}^{\sigma}$ — the
  antineutrino ([antineutrino knot](#def:antineutrino-knot)),
  distinguished from the neutrino by orientation, not knot type.
- **Interlocked circles**: Hopf link $\mathcal{L}_H$ — the
  $\oplus$ operation connecting components.
- **Green border**: closed $1s$ sub-link (2 electrons).
- **Blue border**: closed $2s$ sub-link (2 electrons).
- **Brown border**: nuclear sub-link (protons + neutrons).

| $Z$ | Atom | $N$ | Structure | $k_\alpha$ | Shells |
|----:|------|----:|-----------|---:|--------|
| 1 | H | 0 | $[\mathfrak{p}] \oplus T_{2,3}$ | 0 | $1s^1$ |
| 2 | He | 2 | $[\alpha] \oplus [T_{2,3} \oplus T_{2,3}]^*$ | 1 | $1s^2$ ${}^*$ |
| 3 | Li | 4 | $[3\mathfrak{p}4\mathfrak{n}] \oplus [T \oplus T]^* \oplus T$ | 1 | $1s^2 + 2s^1$ |
| 4 | Be | 5 | $[4\mathfrak{p}5\mathfrak{n}] \oplus [T \oplus T]^* \oplus [T \oplus T]^*$ | 2 | $1s^2 + 2s^2$ |

$T = T_{2,3}$ (trefoil). Brackets $[\cdots]^*$ denote a
**closed sub-Hopf link** — a sub-link that splits from the
remaining components.

**Observations.**

1. **Hydrogen** ($Z = 1$): a single proton $\mathfrak{p}$
   linked to a single electron $T_{2,3}$.  No sub-links — the
   shell is open.

2. **Helium** ($Z = 2$): the $\alpha$ particle
   ($2\mathfrak{p} \oplus 2\mathfrak{n}$) linked to two
   electrons forming a **closed Hopf pair**.  This is the first
   closed sub-link.  Both the nuclear and electronic sub-links
   are closed — helium is doubly stable.

3. **Lithium** ($Z = 3$): the $1s^2$ sub-link is closed, but
   the third electron links at a higher level.  The $2s$ shell
   is open — lithium is chemically reactive (one valence
   electron).

4. **Beryllium** ($Z = 4$): two closed electron pairs ($1s^2$
   and $2s^2$), both Hopf-linked.  The $2s$ shell is closed
   but the $2p$ sub-shell has not yet started — beryllium has
   two valence electrons.

**Transfer matrix data for light atoms.**

Each atom's nuclear link is encoded by transfer matrices
([transfer matrix operator](#def:transfer-matrix-operator)) with
crossing coefficients depending on pair type.  For the atoms
above:

| Atom | $A$ | $\binom{A}{2}$ steps | Pair types | $\deg P \leq$ |
|------|:---:|:---:|------------|:---:|
| H | 1 | 0 | — | 0 |
| He | 4 | 6 | 1 pp, 1 nn, 4 mix | 15 |
| Li | 7 | 21 | 3 pp, 6 nn, 12 mix | 48 |
| Be | 9 | 36 | 6 pp, 10 nn, 20 mix | 80 |

The shell structure of these atoms is governed by the
photon-electron transfer matrix eigenvalue $\lambda_+ = 1.1073$
([shell structure eigenvalues](#prop:shell-structure-eigenvalues)).
Hydrogen has one electron-proton junction ($T_{\gamma e}^1$);
helium has a closed $1s$ shell ($T_{\gamma e}^1 \otimes T_{\gamma e}^1$); lithium adds the first $2s$ electron
($T_{\gamma e}^2$ at the third junction).

An interactive version with SVG knot diagrams is available as the
[knot atom diagrams simulator](#sim:knot-atom-diagrams).
