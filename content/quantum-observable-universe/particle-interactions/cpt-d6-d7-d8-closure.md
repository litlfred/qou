**Conjecture (CPT closure from D6 + D7 + D8).**
*Within the QOU framework, the three discrete symmetries close
consistently: there exist actions $C$, $P$, $T$ on closed-braid
representatives of $H_n(q)$ such that*

1. *$C$ is the color-sheet flavor-swap $u \leftrightarrow \bar u$,
   $d \leftrightarrow \bar d$ ([component D6](c-from-color-flavor-swap.md));*
2. *$P$ is the braid-diagram mirror reflection (writhe sign flip)
   ([component D7](p-from-braid-mirror.md));*
3. *$T$ is the Markov-trace word reversal (trace-cyclicity dual)
   ([component D8](t-from-trace-cyclicity.md));*

*and the composite $C \cdot P \cdot T$ preserves the Markov trace
$\tau_M \colon H_n(q) \to R$, i.e.
$\tau_M((C \cdot P \cdot T)\beta) = \tau_M(\beta)$ for every
closed-braid representative $\beta$.*

## Structure

The conjecture is composite: each of D6 / D7 / D8 names a specific
QOU-canonical realisation of one discrete symmetry, and the
**joint** statement is that they compose to the CPT theorem at
the Markov-trace level. Components are stated in the three sibling
files; this file is the unified parent.

The three components are not logically independent — D6 + D7 + D8
collectively constitute the conjecture. They are presented
separately to keep the structural-claim narrative tight per
symmetry channel; the parent block records the unified statement.

## Provenance / scope

- The three components were authored as three separate "Conjecture"
  blocks (labeled D6 / D7 / D8). Pre-consolidation, each block's
  narrative noted that "$X$ becomes a corollary of
  $C \cdot P \cdot T$ once D6 / D7 / D8 close" — that
  observation is now made structural by the present parent
  conjecture.
- The audit skill
  [`local/proposition-consolidation-audit`](../../../.claude/skills/local/proposition-consolidation-audit.md)
  surfaced this as an H1 (explicit "becomes a corollary of CPT"
  wording) + H4 (shared cites: `wigner1937`, `jones1987`,
  `kassel1995`) consolidation candidate.

## Lean

Class-axiomatised per AGENTS.md §3b-cond. Downstream blocks that
need CPT-closure as an explicit hypothesis take
`[CPTD6D7D8Closure]` as a class hypothesis; the three
component-instances live in their respective `.lean` files.
