**Remark (physics names are $q_0$-dependent labels for categorical knot operations).**
Physics names (alpha particle, gluon condensate, valence shell, isospin) are labels for recurring categorical structures in the Hecke algebra $H_n(R, q)$ at the aether parameter $q_0$. The categorical structure is fundamental. The physics naming is a derived mapping that depends on the value of $q_0$.

This table records the current mapping at $q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps). At a different aether value, the categorical structures persist but their physics interpretations may differ. The recurring sub-blocks identified by the discovery cache acquire different macroscopic meaning when $q_0$ changes.

See [Table](#tbl:physics-names-knot-operations-table-data).

**Generation of the table.**
A discovery cache is populated by SDP shadow-price analysis on Hecke Wedderburn blocks. It records each recurring categorical structure as a key. A naming map associates each structural key with its physics label at $q_0$. The categorical keys are fundamental, whereas the physics names serve as the macroscopic display layer.

**Aether dependency.**
Several entries carry "Depends on $q_0$" annotations. These indicate:
- The $\dim_q V_\lambda$ factor evaluates to a $q_0$-dependent number.
- The recurring sub-block is identified at the algebraic level (categorical structure independent of $q_0$), but its numerical weight depends on $q_0$.
- At a different $q_0$, the same sub-block exists but may have a different Plancherel weight, possibly vanishing. If the weight vanishes, the physics name no longer applies.

The "alpha particle" identification requires $w_{(3,3,3,3)}(q_0)$ to dominate the depth-3 chirality cells of $H_{12}$. At $q_0 = 1.109978595642739\ldots$ (under the muon calibration), this weight is $\sim 0.024$. It is the largest contribution at depth 3. At $q_0 = 1$ (classical limit), the weight becomes the symmetric-group Specht-module dimension squared over $12!$. The ranking changes. The "alpha particle" identification must be re-derived.

**Remark.** This table forms the interface between the categorical spectral, gauge-coupling, and chirality-residue results and the physics-language predictions in this chapter. Every physics name in this chapter that does not appear in this table is either an external empirical reference (CODATA, AME) or a forward reference to a later definition.
