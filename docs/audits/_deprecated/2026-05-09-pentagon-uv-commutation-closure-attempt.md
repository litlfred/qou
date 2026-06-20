> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# Pentagon-UV-commutation closure attempt — 2026-05-09

**Date:** 2026-05-09 (this session)
**Branch:** local probes only (per `ci=billing`)
**Subject:** [`conj:pentagon-uv-commutation`](../../content/quantum-observable-universe/braids-and-knots/pentagon-uv-commutation.md)

## Goal

Close the conjecture so that the production mass tower can include
all-orders subset sums (triples, quads, …) without divergence, by
absorbing them into level-(n+1) corrections via the Faddeev–Kashaev
pentagon identity for Φ_q.

## What I found (this session, no pushes per ci=billing)

### Finding 1 — `vhat-pair-commutation-trace` is *insufficient* to close the conjecture

The existing Lean lemma proves `V̂_i · V̂_j = V̂_j · V̂_i` (scalars in the
commutative ring `ℤ[q^{±½}, z]`). Its narrative MD claims this closes
the pentagon-ascension argument because:

> "the same conclusion (singletons + pairs + jet ascension) follows
> from Markov-trace factorization without any q-commutation input."

This claim is **mathematically incorrect as a closure** of
`pentagon-uv-commutation`. Numerical test (this session): pick scalar
u, v ∈ (−1, 1) with `uv = vu` (commutative) and check the pentagon
identity:

| u | v | LHS = Φ_q(v)·Φ_q(u) | RHS = Φ_q(u)·Φ_q(uv)·Φ_q(v) | \|LHS − RHS\| |
|---|---|---:|---:|---:|
| 0.1 | 0.2 | 17.20 | 20.64 | 3.45 |
| 0.3 | 0.4 | 1104.7 | 3398.7 | 2293 |
| 0.5 | 0.3 | 3616.7 | 14898.5 | 11281 |
| 0.6 | 0.6 | 4.68×10⁵ | 1.72×10⁷ | 1.67×10⁷ |

LHS ≠ RHS by orders of magnitude in the commutative scalar case. **The
pentagon identity is genuinely non-commutative; it requires `uv = q·vu`
(not `uv = vu`).** The level-internal scalars-commute lemma is
therefore NOT load-bearing on triple-absorption — it proves a different,
strictly weaker statement.

### Finding 2 — what's actually needed

To close `conj:pentagon-uv-commutation` rigorously, the inter-level
operator pair (Û, V̂) at adjacent jet levels n, n+1 must satisfy the
quantum-torus relation `Û · V̂ = q · V̂ · Û` on the transient summand
`ker τ̂_n`. The MD says this is "expected from the descent involution's
quantization".

Concretely:

1. The brane tower is built via jet prolongation
   `A_{n+1} = J^1(A_n) ≅ A_n ⊗ Ω¹(A_n)`
   ([recursive-brane-tower](../../content/quantum-observable-universe/lifting-and-descent/recursive-brane-tower.md)).
2. The descent involution `τ̂_n: A_{n+1} → A_{n+1}` separates the
   *descended* part `im τ̂_n` (where the Markov-trace lives at level n)
   from the *transient* part `ker τ̂_n` (where the level-(n+1)
   contribution lives).
3. **Open ingredient:** an explicit construction of operators
   `Û_i ∈ End(A_{n+1})` (lift of `V̂_i^(n)` via the inclusion
   `A_n ↪ A_{n+1}`) and `V̂_j ∈ End(A_{n+1})` (genuine level-(n+1)
   volume) such that `Û · V̂ = q · V̂ · Û` on `ker τ̂_n`.

In q-deformed noncommutative geometry the canonical pair would come
from a q-deformed differential calculus on `A_n` (e.g. Woronowicz
calculus, where `da · a = q · a · da` on a left covariant 1-form). The
QOU paper does **not** yet specify which q-calculus the brane tower
uses.

### Finding 3 — testing the closure empirically requires level-(n+1) volumes

To verify `triple_at_level_n = pair+single_at_level_n + ascension_to_level_(n+1)`,
one needs the level-(n+1) traced volumes `V̂_i^(n+1)`. The current
codebase has only `V̂_i^(0)` (= `additive_wedderburn_volumes` per
`mass_endomorphism.py`). The level-1 ascension would come from the
jet prolongation `J^1`, which is structurally defined but not
computationally instantiated.

**Empirical test deferred** — requires implementing
`additive_wedderburn_volumes_at_jet_level(n)` for `n ≥ 1`.

## Lean class scaffold for the open piece

```lean
namespace QOU.BraidKnot.PentagonUVCommutation

/-- The brane-tower q-commutation HYPOTHESIS at adjacent jet levels.

    Encodes the open content of `conj:pentagon-uv-commutation` as a
    type class so downstream theorems (the explicit triple-absorption
    rule, the all-orders mass tower closure) can be stated as
    *conditional* theorems per AGENTS.md §3b-cond.

    To CLOSE the conjecture, an instance must be constructed showing
    that at every jet level n there exist operators Û_i, V̂_j on
    A_{n+1} with Û · V̂ = q · V̂ · Û on ker τ̂_n. -/
class BraneTowerQCommutation (R : Type*) [CommRing R] (q : R) where
  /-- The brane-tower jet algebras. -/
  jetAlgebra : ℕ → Type*
  [jet_ring : ∀ n, Ring (jetAlgebra n)]
  /-- Level-shift inclusion A_n ↪ A_{n+1}. -/
  shift : ∀ n, jetAlgebra n →+* jetAlgebra (n + 1)
  /-- Descent involution. -/
  tau_hat : ∀ n, jetAlgebra (n + 1) → jetAlgebra (n + 1)
  /-- Operator lifts (level-n V̂ to A_{n+1}). -/
  Uhat : ∀ n, jetAlgebra n → jetAlgebra (n + 1)
  /-- Genuine level-(n+1) operators. -/
  Vhat : ∀ n, jetAlgebra (n + 1) → jetAlgebra (n + 1)
  /-- The transient summand (ker τ̂_n). -/
  transient : ∀ n, Set (jetAlgebra (n + 1))
  /-- The quantum-torus relation on transient — THIS IS THE OPEN
      CONJECTURE'S CORE. -/
  q_commute :
    ∀ n (x : jetAlgebra n) (y : jetAlgebra (n + 1)),
      y ∈ transient n →
      (Uhat n x) * (Vhat n y) = q • ((Vhat n y) * (Uhat n x))

/-- Conditional theorem: under the q-commutation hypothesis, the
    Faddeev–Kashaev pentagon identity for Φ_q reduces a triple
    product at level n to a pair+single at level n plus a residual
    that is well-defined on ker τ̂_n at level n+1.

    This is the algebraic content of the "ascension rule" claimed
    informally in `mass-endomorphism-jet-tower.md`. The theorem is
    `conditional` per AGENTS.md §3b-cond: provable from the class
    instance + the unconditional pentagon identity for q-commuting
    operators. -/
theorem triple_absorption_under_q_commutation
    {R : Type*} [CommRing R] (q : R) [BraneTowerQCommutation R q]
    (n : ℕ) (i j k : ℕ) :
    -- "triple at level n = pair + single at level n + residual at level n+1"
    -- Concrete statement deferred until brane-tower jet-prolongation
    -- machinery is in place; the form follows directly by iterating
    -- the Faddeev–Kashaev pentagon `Φ(v)·Φ(u) = Φ(u)·Φ(uv)·Φ(v)`
    -- under `BraneTowerQCommutation.q_commute`.
    True := trivial -- placeholder
```

## Status

**Conditional skeleton sketched.** The class `BraneTowerQCommutation`
is the canonical encapsulation of what's open. Instantiating it
requires:

1. Concrete construction of the jet prolongation `J^1(A_n)` as a
   Frobenius–Hopf object (open: needs an explicit q-deformed
   differential calculus on `A_n`).
2. Concrete construction of `τ̂_n`, the descent involution (partially
   present in the brane-tower MD; not yet a Lean structure).
3. Construction of `Û_i, V̂_j` operators with the q-commutation
   property (open).

**Conclusion:** `conj:pentagon-uv-commutation` is **structurally open**
and not closable from existing infrastructure. Closing it requires
new categorical/algebraic content (a q-deformed differential calculus
on the brane-tower algebras) that is not currently in the paper.

The best we can do today: make the conditional dependency explicit via
the class hypothesis above, and route any all-orders mass-tower
extension through it (per AGENTS.md §3b-cond).

## Implications for the all-orders mass tower

Per the experimental probe earlier this session, naively extending
the mass tower beyond pairs **diverges** (Φ_q saturates at
`|Π V_i| → q`). So we cannot just "add triples" — the pentagon
ascension is needed to:

- Re-express the divergent triple `Φ_q(|V_i V_j V_k|)` as `Φ_q(|U V|)`
  for some U, V at the *next* jet level where convergence is restored.
- The geometric tail bound `prop:jet-tower-convergence` then controls
  the residual.

Without the pentagon ascension this redirection isn't available, so
the production code's pair-only formula is the **best one can do
without closing the conjecture**. The pair-only formula was already
shown today to fail on the deuteron (predicts M(D) ≈ 5107 MeV vs AME
1875.6 MeV — off by 3×), so closing this conjecture is genuinely
load-bearing on the binding-energy prediction for A ≥ 2.

## Cross-references

- [`conj:pentagon-uv-commutation`](../../content/quantum-observable-universe/braids-and-knots/pentagon-uv-commutation.md) — the conjecture
- [`lem:vhat-pair-commutation-trace`](../../content/quantum-observable-universe/braids-and-knots/vhat-pair-commutation-trace.md) — proven, but proves a different statement
- [`rem:mass-endomorphism-jet-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-jet-tower.md) — uses the conjecture
- [`def:recursive-brane-tower`](../../content/quantum-observable-universe/lifting-and-descent/recursive-brane-tower.md) — the J^1 jet structure
- [`docs/audits/2026-05-09-mass-table-fitting-audit.md`](2026-05-09-mass-table-fitting-audit.md) — broader audit
