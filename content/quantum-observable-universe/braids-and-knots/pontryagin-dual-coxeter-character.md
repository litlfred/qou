**Theorem (D20 Pontryagin self-duality on $S_n^{\mathrm{ab}}$).**
*For every $n \geq 2$, the abelianisation
$S_n^{\mathrm{ab}} \cong \mathbb{Z}/2$ of the Coxeter group $S_n$
is canonically Pontryagin self-dual: the character group
$\widehat{S_n^{\mathrm{ab}}} = \mathrm{Hom}(\mathbb{Z}/2, \mathbb{C}^\times)$
is canonically isomorphic to $\mathbb{Z}/2$ itself, via the
identification of the unique non-trivial character with the sign
homomorphism.*

## Lean closure

The structural content is captured by
[`pontryagin_dual_coxeter_character_structural`](pontryagin-dual-coxeter-character.lean)
as a sorry-free Mathlib theorem, conjoining:

- `zmodTwo_pontryagin_self_dual_via_value_at_one` — every character
  $\mathbb{Z}/2 \to \mathbb{Z}/2$ is determined by its value at 1
  (proven by `fin_cases`).
- `signHom_surjective_witness` — `Equiv.swap 0 1 ∈ Equiv.Perm (Fin n)`
  has sign $-1$ for `n ≥ 2`.

A backward-compatible `class PontryaginDualCoxeterCharacter` is
retained with a default instance backed by the structural theorem,
so downstream blocks that previously used it as a §3b-cond
hypothesis continue to compile. New downstream code should cite
`pontryagin_dual_coxeter_character_structural` directly.

## Discussion

This block was previously labelled
[`thm:pontryagin-dual-coxeter-character`](#) and was carried in
the duality tracker as **D20 — open, low priority**. The Phase-1
Tier-A closure
([`docs/workplans/2026-05-30-source-conjecture-closure-plan.md`](../../../docs/workplans/2026-05-30-source-conjecture-closure-plan.md))
discharges it to a `theorem` using existing Mathlib primitives
(`Equiv.Perm.sign`, `ZMod 2` finite-case analysis). The block was
explicitly degenerate / low priority, so the closure carries no
new framework derivation — but it does close the duality-tracker
D20 entry and provides a concrete `Equiv.swap 0 1` witness usable
in any downstream parity argument.

## Why we recorded it (now closed)

D20 was included in the duality tracker for **completeness**: the
13-driver categorical menu mentions "Pontryagin / Cartier /
Kashiwara crystal $q \to 0$ / $q \to \infty$" as a research
direction. The closure establishes that the Pontryagin part of
that menu IS applicable but yields no new information beyond the
sign-of-a-permutation observable — i.e., the same $\mathbb{Z}/2$
that the bar involution (D1) already classifies.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration**: N/A — abelianisation collapses the filtration.
- **Jet order**: $h^0$ — Pontryagin is a parameter-independent
  abelian duality.
- **Bar-symmetry**: identical to bar at the abelianised level.

## Cross-references

- [`docs/duality-tracker.md`](../../../docs/duality-tracker.md) D20
- D1 [`def:bar-involution`](#def:bar-involution) — the non-trivial
  $\mathbb{Z}/2$ that subsumes the abelianised case
- [`docs/workplans/2026-05-30-source-conjecture-closure-plan.md`](../../../docs/workplans/2026-05-30-source-conjecture-closure-plan.md)
  Phase 1 — Tier A discharge
- [Pontryagin 1934; Hewitt–Ross 1979 for locally-compact abelian
  duality]
