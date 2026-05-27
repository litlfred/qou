**Operator-theoretic construction of the Markov trace on $\mathbf{B}_\infty$ (Item 4 of `rem:post-pr665-open-rd-inventory`).**

The Jones-Wenzl Markov trace $\tau_M : \mathbf{B}_\infty \to \mathbb{R}$
on the inductive limit of braid groups is uniquely characterised by the
M1-M4 axioms (Jones 1985 / Wenzl 1988). Its existence as a single
operator on the von Neumann inductive limit hyperfinite II_1 factor
is the **substantive content of item 4**; this block records the
type-level scaffolding for that construction.

## Scaffolding components

| Lean class | Substantive content |
|---|---|
| `HnHilbertRep n q` | Per-$n$ regular representation $V_n$ of $H_n(q)$ with $\dim V_n \geq 1$ |
| `HnInductiveEmbedding n q` | Connecting morphism $\iota_n : V_n \hookrightarrow V_{n+1}$ |
| `MarkovTraceVNFactor q` | GNS construction + bicommutant von Neumann factor hosting $\tau_M$ |

Each class follows the **explicit-residual pattern** (scalar
deviation + equation asserting it vanishes) — non-vacuous content
per the Gemini reviews on PR #665/#672.

## Construction outline (substantive R&D)

1. **Per-$n$ Hilbert space**: $V_n$ is the regular representation
   $H_n(q) \cdot v_\emptyset$ with inner product $\langle x v, y v \rangle = \tau_M(y^* x)$.
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
   hyperfinite II_1 factor; $\tau_M$ is its unique faithful normal
   trace (up to scaling).

## Why scaffold rather than full construction

Steps 1-3 are Mathlib-routine modulo $H_n(q)$ type infrastructure
(item 2 of the inventory — see `rem:hecke-algebra-type-scaffold`).
Steps 4-5 are substantively new: GNS for the Markov state +
bicommutant of an inductive limit of finite-dim algebras. Both
require operator-algebra infrastructure not in Mathlib's core.

The scaffold here lets downstream consumers of the operator
construction take `[MarkovTraceVNFactor q]` as a hypothesis without
implementing the full construction immediately.

## Status

**Scaffolding-tier Lean infrastructure.** Per-$n$ discharges open
for $n \geq 3$. The inductive-limit and bicommutant closure are
the substantive items remaining; chapter empirical predictions
are independent of this discharge (they use only scalar invariants
of $\tau_M$).
