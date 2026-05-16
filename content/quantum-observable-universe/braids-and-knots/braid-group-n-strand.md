**$n$-strand braid group + Markov closure + Hecke quotient scaffolding.**

Generalises the 2-strand foundation in
[`rem:braid-link-types`](#rem:braid-link-types) and the 3-strand
typed-$\mathbf{B}_3$ infrastructure in
[`rem:typed-b3-sub-braid-extraction`](#rem:typed-b3-sub-braid-extraction)
to an arbitrary number of strands $n \in \mathbb{N}$.

## What's defined

| Lean object | Role |
|---|---|
| `TypedCrossing n` | A single typed crossing: generator index $i \in \mathrm{Fin}(n-1)$ + sign $\pm 1$ |
| `BraidWord n` | List of typed crossings (the empty word is the identity braid) |
| `BraidWord.writhe` | Net signed crossing count (algebraic) |
| `closureN` | Markov closure to a `Link`, **opaque at general $n$**, concrete at $n=2$ via `closure2` |
| `HeckeQuotient n q` | Class encoding the Hecke quadratic relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ |
| `MarkovTraceN n q` | Generalised Markov-trace axioms M1-M4 (Jones 1985), inherits the 2-strand `MarkovTraceAxioms` |

## Specialisations

| $n$ | Recovers | Status |
|---:|---|---|
| 2 | `Braid2 := ℤ` and `closure2` | Already proved (Atom 1 + 2 from `rem:markov-closure-map-axiomatic`) |
| 3 | `TypedBraidWord3` with `averaged` crossings | Cherry-picked from `rem:typed-b3-sub-braid-extraction` |
| 4 | Borromean baryon braids | Open R&D — links into the deuteron/nuclear physics regime |
| 6 | Di-baryon (deuteron) braids | Open R&D — needed for $\Delta S$ (n−p) at higher precision |
| 12 | $\alpha$-particle braids | Open R&D — Wedderburn block sum $\sum \tilde w_\lambda$ at $n=12$ is on the open conjecture list |

## Why this matters

The categorical-derivation chain through $N=4$ in
[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)
sits on the 3-strand typed-$\mathbf{B}_3$ infrastructure. Validating
the **two convergence mechanisms** documented in
[`prop:categorical-chain-convergence-mechanisms`](#prop:categorical-chain-convergence-mechanisms)
— per-knot $c(K)$ brane-tower bound + inter-knot linking-number
locality — requires at minimum $n = 6$ infrastructure (to test
$\tau_M(K_1 \sqcup K_2) = \tau_M(K_1) \cdot \tau_M(K_2) \cdot z^k$
on a concrete 2-baryon disjoint braid via Markov axiom M3).

The Lean class system makes the scaffolding **per-$n$ extensible**:
each new $n$ adds an `instance HeckeQuotient n q_0` and
`instance MarkovTraceN n q_0`, and downstream theorems
auto-specialise.

## Open R&D

- Define `BraidWord.toBraid3 : BraidWord 3 → TypedBraidWord3`.
- Define `closureN_eq_closure2` linking the opaque `closureN` at $n=2$
  to the concrete `closure2` (1-line `rfl`-style identification once
  the opaque function is replaced by a concrete construction at $n=2$).
- Per-$n$ discharge of `MarkovTraceN n q` from a fixed Markov-trace
  operator on the inductive limit $\bigcup_n \mathbf{B}_n$.

## Status

**Scaffolding only.** This block defines the n-strand types and
classes; substantive theorems (specific closures, sub-braid
extractions at higher $n$) plug in as separate per-$n$ blocks.

`Braid2_writhe_eq` is **closed** by structural recursion mirroring
the `toBraidWord` construction — no `sorry`s remain in this module.
