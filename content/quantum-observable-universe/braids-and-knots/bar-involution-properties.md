This remark details canonical projections and classifies observable quantities by their behavior under the [bar-involution](#def:bar-involution). 
Companion remarks address algebraic identities, geometric interpretations, and formal bar-grading proofs.

## Canonical projections

The bar-involution satisfies $\overline{\overline x} = x$. Over a field of characteristic distinct from 2, every Hecke-algebra element $x \in H_n(q)$ decomposes uniquely:

$$x \;=\; P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x),$$

where

See [Table 1](#tbl:bar-involution-table1-data).

We identify $P_{\mathrm{avg}}$ as the canonical physical projection. The theory retains the bar-symmetric component of any Hecke-algebra computation as observable content and discards the bar-anti-symmetric component.

> **Note on parity.** $P_{\mathrm{avg}}(x)$ is the bar-symmetric (even) projection, preserving functions like $\cos$, $\cosh$, and $\mathrm{Li}_2^q$. $P_{\mathrm{skew}}(x)$ is the discarded bar-anti-symmetric (odd) component.

## Classification by bar-type

We classify framework quantities by their behavior under the bar involution.

### Bar-symmetric (retained)

See [Table 2](#tbl:bar-involution-table2-data).

### Bar-anti-symmetric (discarded)

See [Table 3](#tbl:bar-involution-table3-data).

### Trivial under bar (rational scalars)

See [Table 4](#tbl:bar-involution-table4-data).

## Cross-references

Subsequent developments rely on this bar-symmetry classification:

- `thm:averaging-resonance-rule`: The symmetric $\sigma_{\mathrm{avg}}$ enforces the level-selection rule.
- [`prop:c5-involution-leibniz-decomposition`](#prop:c5-involution-leibniz-decomposition): Identifies the bar-symmetric closed form for $c_5$.
- [`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null): Locates the $h=2$ root via the anti-symmetric operator $\Delta(\text{net}) = h(h-2)/2$.
- `prop:bar-symmetric-three-layer-synthesis`: Synthesizes series, phase, and gain layers as symmetric projections.
- [`def:categorical-q-reeb-flow`](#def:categorical-q-reeb-flow): Classifies the Reeb field $R$ as bar-anti-symmetric.
- [`prop:chirality-residue-mass-term`](#prop:chirality-residue-mass-term): Classifies chirality residue as bar-anti-symmetric.

## Notation summary

See [Table 8](#tbl:bar-involution-table8-data).
