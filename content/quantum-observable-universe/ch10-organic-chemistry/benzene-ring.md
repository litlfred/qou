Benzene ($\mathrm{C}_6\mathrm{H}_6$) is the prototypical molecular
Hopf ring: the linear $\mathrm{C}_6$ chain
([linear C₆](#ex:carbon-chain-c6)) with the final link closed.

**Construction.**
The six carbon atoms form the ring $\mathcal{R}_6^{(k)}$
([molecular Hopf ring](#def:molecular-hopf-ring)) with the
circulant linking matrix:

$$
  L^{\mathrm{ring}}
  \;=\;
  \begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 1 \\
    1 & 0 & 1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1 & 0 & 1 \\
    1 & 0 & 0 & 0 & 1 & 0
  \end{pmatrix}.
$$

The difference from the chain matrix is the $(1,6)$ and $(6,1)$
entries — the closing bond.

**Bond order delocalisation.**
Each carbon uses 2 of its 4 sites for backbone bonds and 1 for a
C–H bond, leaving 1 site per atom.  These 6 remaining sites form
a **secondary Hopf ring** of bond order $k = 1$ superimposed on
the primary backbone — the topological picture of the $\pi$
electron cloud.  In the Skein module, this secondary ring
evaluates to a Jones polynomial whose $q$-weighting distributes
the extra bonding evenly around the hexagon:

$$
  \frac{3}{2} \text{ effective bonds per edge}
  \quad\text{(alternating single/double → uniform } 1.5\text{)}.
$$

This is the QOU derivation of benzene's bond-order equalisation:
the six delocalised trefoils form a closed sub-Hopf link that
cannot be localised to any three edges without increasing crossing
energy.

**Rigidity.**
With no free endpoints, the ring has no soft spring modes.  Every
deformation requires a global braid rearrangement — the ring is
topologically rigid.  This explains benzene's remarkable thermal
stability and resistance to addition reactions (which would open
the ring and break the closed secondary Hopf link).

**Aromaticity as topological closure.**
The concept of aromaticity in organic chemistry corresponds
precisely to the **closure of the secondary Hopf ring**: a
molecule is aromatic when its $\pi$ electrons form a closed
sub-Hopf link that would cost more crossing energy to open than
to maintain.  Hückel's rule ($4n + 2$ electrons for aromaticity)
should emerge from the shell capacity constraint on closed
sub-Hopf links at the molecular scale.
