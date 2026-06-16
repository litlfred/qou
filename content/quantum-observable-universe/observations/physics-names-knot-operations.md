**Remark (physics names are q$_{0}$-dependent labels for categorical knot operations).**

*The names that physicists give to phenomena (alpha particle, gluon
condensate, valence shell, isospin, etc.) are convenient labels for
recurring **categorical structures** in the Hecke algebra
$H_n(R, q)$ at the substrate parameter $q_0$.  The categorical structure
is fundamental; the physics naming is a derived mapping that depends on
which value of $q_0$ instantiates the substrate.*

*This table records the current mapping at $q_0 = 1.109978595554181\ldots$ (50 dps).  At
a different substrate value the categorical structures persist but
their physics interpretations may differ — the recurring sub-blocks
identified by the discovery cache
([cite knot-operation-cache.json](#))
acquire different macroscopic meaning when $q_0$ changes.*

See [Table](#tbl:physics-names-knot-operations-table-data).

**How the table is generated.**

*The discovery cache (`computations/knot-operation-cache.json`,
populated by SDP / shadow-price analysis on Hecke Wedderburn blocks)
records each recurring categorical structure as a key.  The lookup
`physics-names.json` maps cache keys to physics names at the current
$q_0$.  Both are version-controlled artifacts; the categorical cache
keys are the source of truth, the physics names are the human-facing
display layer.*

**Substrate dependency.**

*Several entries above carry "Depends on $q_0$" annotations.  These
indicate that:*

- *the `dim_q V_λ` factor evaluates to a $q_0$-dependent number;*
- *the recurring sub-block is identified at the **algebraic level**
  (categorical structure independent of $q_0$) but its **numerical
  weight** depends on $q_0$;*
- *at a different $q_0$, the same sub-block exists but may have
  different Plancherel weight, possibly even vanishing weight (in
  which case the corresponding "physics name" no longer applies).*

*The "alpha particle" identification, for instance, requires
$w_{(3,3,3,3)}(q_0)$ to dominate the depth-3 chirality cells of $H_{12}$
— at $q_0 = 1.109978595554181\ldots$ (50 dps) this weight is $\sim 0.024$, the largest
contribution at depth 3.  At $q_0 = 1$ (classical limit), the weight
becomes the symmetric-group Specht-module dimension squared over
$12!$, with different ranking — the "alpha particle" identification
must be re-derived.*

*Remark.* This table is the **interface** between the categorical machinery
(`prop:em-spectral-completeness`, `prop:gauge-coupling-uniqueness`,
`prop:chirality-residue-mass-term`, etc.) and the physics-language
predictions in this chapter.  It will grow as the discovery cache
identifies further recurring structures.  Every physics name in this
chapter that does **not** appear in this table is either an external
empirical reference (CODATA, AME) or a forward reference to a
later definition.*
