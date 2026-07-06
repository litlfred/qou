This remark develops the canonical projections and the classification of
QOU quantities by bar-type for the [bar-involution](#def:bar-involution).
The key algebraic identities, the geometric / Kac–Sunada readings, and the
$\mathbb{Z}/2\mathbb{Z}$ bar-grading proofs are developed in the companion
remarks
[bar-symmetric algebraic identities](#rem:bar-involution-c5-algebraic-identities),
[geometric and Kac–Sunada readings](#rem:bar-involution-geometric-kac-sunada),
and [the bar-grading Lean bridge](#rem:bar-involution-grading-lean-proofs).

## The two canonical projections

The bar-involution is an involution: $\overline{\overline x} = x$.
Every Hecke-algebra element $x \in H_n(q)$ over a field of
characteristic $\ne$ 2 decomposes uniquely as

$$x \;=\; P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x),$$

where

See [Table 1](#tbl:bar-involution-table1-data).

The framework's empirical content is that **$P_{\mathrm{avg}}$ is
the canonical projection** — the bar-symmetric part of every
Hecke-algebra computation is the physical/observable content; the
bar-anti-symmetric part is projected away.

> **Antiskew-vs-symmetric clarification.** $P_{\mathrm{avg}}(x)$
> is the bar-**even** (= bar-**symmetric**) projection. The
> framework retains $P_{\mathrm{avg}}$ ($\cos, \cosh, \mathrm{Li}_2^q$)
> and discards $P_{\mathrm{skew}}$ ($\sin, \sinh, \Phi_q$ alone).
> "Anti-skew" is only accurate in the discarding sense — the
> kept residual is symmetric/even.

## Classification of QOU quantities by bar-type

The canonical reference. Every quantity in the paper that has a
well-defined bar-action falls in one of these rows:

### Bar-symmetric (bar-even, $P_{\mathrm{avg}}$ image, retained)

See [Table 2](#tbl:bar-involution-table2-data).

### Bar-anti-symmetric (bar-odd, $P_{\mathrm{skew}}$ image, discarded)

See [Table 3](#tbl:bar-involution-table3-data).

### Trivial under bar (rational scalars)

See [Table 4](#tbl:bar-involution-table4-data).

## Cross-references

This definition is the canonical reference for bar-symmetry. Other
blocks that consume it (with their primary bar-classification):

- `thm:averaging-resonance-rule` — $\sigma_{\mathrm{avg}}$ bar-symmetric; level-selection rule at half-fill rung.
- [`prop:c5-involution-leibniz-decomposition`](#prop:c5-involution-leibniz-decomposition) — $c_5$ bar-symmetric closed form; Hoefsmit-Quantum-2 identity proved here.
- [`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null) — $\Delta(\text{net}) = h(h-2)/2$ bar-anti-symmetric in $h$; $h = 2$ root at silver.
- `prop:bar-symmetric-three-layer-synthesis` — series / phase / gain layers, all bar-symmetric projections (conjecturally of one universal kernel).
- [`def:categorical-q-reeb-flow`](#def:categorical-q-reeb-flow) — Reeb field $R$ bar-anti-symmetric.
- [`prop:chirality-residue-mass-term`](#prop:chirality-residue-mass-term) — chirality residue bar-anti-symmetric.

## Notation summary

See [Table 8](#tbl:bar-involution-table8-data).
