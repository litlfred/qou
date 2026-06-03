# WIP scaffolding — Markov-trace operator construction (open R&D item 4)

> **Provenance.** Primary content of the former content block
> [`rem:markov-trace-operator-construction`](../../content/quantum-observable-universe/mass-endomorphism/markov-trace-operator-construction.md),
> moved here in PR #1767 per the
> `canonical-no-negative-result-in-paper` discipline criterion
> (PR #1766 refinement: `["scaffolding", "open-rd-item-*"]` tag
> pair → audit-class content). The chapter block is retained as a
> forward-reference; the Lean class scaffolding stays in place at
> [`mass-endomorphism/markov-trace-operator-construction.lean`](../../content/quantum-observable-universe/mass-endomorphism/markov-trace-operator-construction.lean).

The Jones–Wenzl Markov trace $\tau_M : \mathbf{B}_\infty \to \mathbb{R}$
on the inductive limit of braid groups is uniquely characterised by the
M1–M4 axioms (Jones 1985 / Wenzl 1988). Its existence as a single
operator on the von Neumann inductive limit hyperfinite $\mathrm{II}_1$
factor is the **substantive content of item 4** of the post-PR-#665 open
R&D inventory; this audit records the type-level scaffolding for that
construction.

## Scaffolding components (Lean classes)

| Lean class | Substantive content |
|---|---|
| `HnHilbertRep n q` | Per-$n$ regular representation $V_n$ of $H_n(q)$ with $\dim V_n \geq 1$ |
| `HnInductiveEmbedding n q` | Connecting morphism $\iota_n : V_n \hookrightarrow V_{n+1}$ |
| `MarkovTraceVNFactor q` | GNS construction + bicommutant von Neumann factor hosting $\tau_M$ |

Each class follows the **explicit-residual pattern** (scalar deviation +
equation asserting it vanishes) — non-vacuous content per prior review
feedback.

## Construction outline (substantive R&D)

1. **Per-$n$ Hilbert space**: $V_n$ is the regular representation
   $H_n(q) \cdot v_\emptyset$ with inner product
   $\langle x v, y v \rangle = \tau_M(y^* x)$.
2. **Inductive embedding**: $\iota_n : V_n \to V_{n+1}$ sends
   $x \cdot v_\emptyset \mapsto (\iota_n x) \cdot v_\emptyset$ where
   $\iota_n : H_n \hookrightarrow H_{n+1}$ is the algebra inclusion
   (adding one strand).
3. **Inductive limit**: $V_\infty = \varinjlim V_n$, a separable
   Hilbert space.
4. **Trace state**: $\tau_M$ extends to a positive linear functional
   on the inductive-limit algebra $\bigcup_n H_n$, restricting
   compatibly per the M3 axiom.
5. **Bicommutant closure**: $\mathcal{M} := (\bigcup_n H_n)''$ is the
   hyperfinite $\mathrm{II}_1$ factor; $\tau_M$ is its unique faithful
   normal trace (up to scaling).

## Why scaffold rather than full construction

Steps 1–3 are Mathlib-routine modulo $H_n(q)$ type infrastructure
(item 2 of the inventory — see
[`hecke-algebra-type-scaffold` audit](2026-06-03-wip-scaffolding-hecke-algebra-type-scaffold.md)).
Steps 4–5 are substantively new: GNS for the Markov state +
bicommutant of an inductive limit of finite-dim algebras. Both require
operator-algebra infrastructure not in Mathlib's core.

The scaffold lets downstream consumers of the operator construction
take `[MarkovTraceVNFactor q]` as a hypothesis without implementing the
full construction immediately.

## Status

**Scaffolding-tier Lean infrastructure.** Per-$n$ discharges open for
$n \geq 3$. The inductive-limit and bicommutant closure are the
substantive items remaining; chapter empirical predictions are
independent of this discharge (they use only scalar invariants of
$\tau_M$).

## See also

- [`rem:post-pr665-open-rd-inventory`](../../content/quantum-observable-universe/mass-endomorphism/post-pr665-open-rd-inventory.md) — parent R&D inventory; item 4 is this construction
- [`hecke-algebra-type-scaffold` audit](2026-06-03-wip-scaffolding-hecke-algebra-type-scaffold.md) — item 2 (Hecke type scaffold) companion
- [`markov-trace-operator-construction.lean`](../../content/quantum-observable-universe/mass-endomorphism/markov-trace-operator-construction.lean) — Lean class scaffolding (stays in place; imported by downstream Lean files)
- Jones 1985 / Wenzl 1988 — Markov trace axioms M1–M4 and uniqueness
