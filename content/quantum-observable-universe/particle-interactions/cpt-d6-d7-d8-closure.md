**Conjecture (CPT closure).** The three discrete symmetries close consistently: there exist actions $C$, $P$, $T$ on closed-braid representatives of $H_n(q)$ such that

1. $C$ is the color-sheet flavor-swap $u \leftrightarrow \bar u$, $d \leftrightarrow \bar d$ ([component D6](c-from-color-flavor-swap.md));
2. $P$ is the braid-diagram mirror reflection, or writhe sign flip ([component D7](p-from-braid-mirror.md));
3. $T$ is the Markov-trace word reversal, or trace-cyclicity dual ([component D8](t-from-trace-cyclicity.md)).

The composite $C \cdot P \cdot T$ preserves the Markov trace $\tau_M \colon H_n(q) \to R$. That is, $\tau_M((C \cdot P \cdot T)\beta) = \tau_M(\beta)$ for every closed-braid representative $\beta$.

## Structure

The conjecture is composite. D6, D7, and D8 name specific canonical realisations of the discrete symmetries. The joint statement is that they compose to the CPT theorem at the Markov-trace level. The components are presented in three sibling files to keep the structural claims tight; this file records the unified statement. The three components are not logically independent—they collectively constitute the conjecture.

## Scope

The three components were authored as separate conjecture blocks. Pre-consolidation, each noted that a property becomes a corollary of $C \cdot P \cdot T$ once the components close. This observation is now structural. The audit skill [`local/proposition-consolidation-audit`](../../../.claude/skills/local/proposition-consolidation-audit.md) surfaced this as a consolidation candidate.

## Lean

The conjecture is class-axiomatised per AGENTS.md §3b-cond. Downstream blocks that require CPT closure as an explicit hypothesis take `[CPTD6D7D8Closure]` as a class hypothesis. The component instances reside in their respective `.lean` files.

**Archimedean specialisation (§7c).** This block invokes real- or complex-analytic constructs (observables, bounds, numerical evaluation). Categorical identities remain valid over an abstract coefficient ring; their archimedean realisation is specialised here.
