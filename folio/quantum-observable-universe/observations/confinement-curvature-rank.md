**Remark (curvature-rank as confinement layer).**
By [confinement-categorical](#prop:confinement-categorical), the collapse of the GB-filtration spectral sequence provides the categorical content of color confinement. Translating this algebraic statement into QCD vocabulary yields the following dictionary.

**Confinement layers.**
The GB filtration $J^0 \supset J^1 \supset \cdots$ stratifies $A = H_n(R, q)$ by curvature-rank $k = \mathrm{depth}(\lambda) - 1$. Each stratum $J^k / J^{k+1}$ acts as a confinement layer:
- $k = 0$ (centre): elements are gauge-invariant. This forms the observable hadron content.
- $k \geq 1$: extracting an element requires energy proportional to the curvature 2-cocycle $F$ (the combined Hecke and Yang-Baxter obstruction). This is categorically the **string tension**.

**String tension = curvature 2-cocycle.**
The Hecke relation $T^2 = (q - q^{-1}) T + 1$ and Yang-Baxter relations define a 2-cocycle $F$ on the GB filtration. $F$ obstructs the extraction of a non-central element along the filtration. It matches how QCD string tension obstructs the extraction of an isolated colored quark. The QCD "string" corresponds to the chain of commutators $[a, b]$ required to move an element through the layers $J^k$.

**Gluon condensate = chirality channel.**
The chirality cells $D_q^2 = 0$ in the q-Dirac cell scanner ($\lambda = (2, 1)$ for $H_3$ and higher-$n$ analogues) coincide with the S-fixed central elements of $A$. They produce a persistent gauge-invariant background. This is the categorical analogue of the **gluon condensate** in QCD. The volume match $\mathrm{Vol}(B_3) = 8 G$ with the gluon octet dimension $\dim \mathfrak{su}(3) = 8$ provides the operator-side identification.

**Hadron mass = sum of confinement layers.**
The unified mass formula ([unified mass formula](#conj:unified-curvature-rank-mass-formula)) reads physical hadron mass as a sum over confinement layers:

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \sum_{k = 0}^{n - 1} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(1).
$$

Each layer contributes its q-deformed Wedderburn-weighted log-character content (cf. $w_\lambda(q)$ in [`prop:plancherel-term-7-formulation`](../mass-theory/plancherel-term-7-formulation.md)).

| Stratum | Confinement layer | Physical content |
|---|---|---|
| $k = 0$ | centre / vacuum | photon-like / unconfined |
| $k = 1, 2$ | low-tower | specific hyperbolic-knot ideals (named knots) |
| $k = 3$ | chirality layer | $D_q^2 = 0$, gluon-condensate background |
| $k \geq 4$ | universal residue | Frobenius co-Casimir tail (no specific knot) |

**Predictive consequence.**
Confinement is structurally built into the spectral-sequence collapse. Every prediction ([universal residue](#prop:plancherel-term-7-formulation), $\mathfrak{Q}_\beta$ structural derivation) is gauge-invariant because the spectral-sequence projection forces all results through $Z(A)$. The rank-3 chirality residue $\mathrm{Vol}(6_1) \cdot |(q;q)_3|$ in the $\mathfrak{Q}_\beta$ formula acts as a **gluon-condensate background term**. The rank-$\geq 4$ universal Pochhammer tail $|(q;q)_4|$ serves as the **Frobenius co-Casimir**. Both are necessary confinement residues, not free parameters.
