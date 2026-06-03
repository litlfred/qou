The Iwahori–Hecke algebra $H_n(R, q)$ as a unital associative algebra
with generators $\sigma_0, \ldots, \sigma_{n-2}$ modulo the three
defining relations (R1: quadratic, R2: far commute, R3: braid cubic)
is the substantive R&D content for item 2 of the post-PR-#665 open
R&D inventory. The Lean class scaffold (`HeckeGen n`, `HeckeWord n`,
`HeckeRelations n q`, `HeckeWedderburn n q`) follows the
explicit-residual pattern.

**Primary content moved to audits.** See
[`docs/audits/2026-06-03-wip-scaffolding-hecke-algebra-type-scaffold.md`](../../../docs/audits/2026-06-03-wip-scaffolding-hecke-algebra-type-scaffold.md)
for the full type-scaffold rationale, the 4-step path to a full
$H_n(R, q)$ type (free $R$-module → multiplication → relation quotient
→ Wedderburn), and per-$n$ discharge status ($n = 2$ trivial,
$n = 3$ partial via Hoefsmit, $n = 6, 12$ open).

The Lean class scaffolding stays in place at
[`hecke-algebra-type-scaffold.lean`](hecke-algebra-type-scaffold.lean) —
downstream Lean theorems take `[HeckeRelations n q]` and
`[HeckeWedderburn n q]` as hypotheses; per-$n$ instances plug in when
the relation-quotient and Murphy seminormal-form infrastructure
land.

This block is retained in the paper as an interpretive
forward-reference; it makes no logical claim.
