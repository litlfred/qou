# The bar-parity prune on the HH¹ outer class does not exist — it is normalization, not an invariant

**Date:** 2026-08-08 · **Bean:** `qou-qb8b` · **Probe:**
[`computations/hh1_outer_class_cocenter_bar_parity.py`](../../computations/hh1_outer_class_cocenter_bar_parity.py)
· **Witness:** `hh1-outer-class-cocenter-bar-parity.witness.json`
· **Tier:** symbolic-exact (exact cyclotomic linear algebra, no fit, nothing wired)

## What was asked

Bean `qou-qb8b` proposed a cheap decisive prune for the one surviving
fibre-level c₃ carrier:

> Read the bar-parity of the outer class's action on the cocenter at the
> Bring root of unity. Bar-even kills the route to the same invariant that
> killed the real resolvent.

## Answer: the quantity is not well-defined, so the prune cannot exist

**The bar-parity of the HH¹ outer class acting on HH₀ is a choice of
normalization, not an invariant of the class.** Both parities are always
available. Bar-parity therefore cannot prune this route — and cannot confirm
it either.

This is a **scope-(a) negative about the test**, not a refutation of the
carrier. The route is left exactly where it was: open.

## The computation

`H₃(q)`, dim 6, basis `[e, s₁, s₂, s₁s₂, s₂s₁, s₁s₂s₁]`, relation
`sᵢ² = a sᵢ + 1` with `a = q − q⁻¹` (AGENTS.md §7a). Inherits the
multiplication tables from the merged PROBE A
(`hh1_hecke_outer_derivations.py`).

| point | dim HH₀ | dim Der | dim Inn | dim HH¹ | Δ^bar ∝ Δ? | λ | raw parity |
|---|---|---|---|---|---|---|---|
| `q = i` (`[2]_q = 0`) | 3 | 4 | 3 | **1** | yes | `+1` | bar-EVEN |
| `q = ζ₆` (`[3]_q = 0`) | 3 | 4 | 3 | **1** | yes | `−1` | bar-ODD |
| `q = 2` (semisimple control) | 3 | 3 | 3 | **0** | — | — | n/a |

### Why the test is canonical at all — and where it stops being so

A derivation descends to the cocenter, since
`D(ab − ba) = [D(a), b] + [a, D(b)] ∈ [A,A]`. An **inner** derivation
descends to **zero**, because `ad_x(y) = xy − yx` *is* a commutator. So the
induced map `Δ : HH₀ → HH₀` depends only on the HH¹ **class** — the map
`HH¹ → End(HH₀)` is well defined.

*Asserted, not assumed:* `inner_acts_as_zero_on_cocenter` (all 6 `ad_x`
induce zero) and `delta_is_class_canonical` (6 alternative representatives
`outer + ad_x` each reproduce Δ **exactly**).

But class-canonicity is only **up to a scalar**: `dim HH¹ = 1`, so the
representative is fixed only modulo `D ↦ cD`. And that is precisely where the
parity leaks away.

### The normalization-dependence, demonstrated constructively

Under `D ↦ cD`: `Δ ↦ cΔ` and `Δ^bar ↦ bar(c)·Δ^bar`, so the parity is
multiplied by `bar(c)/c`. The involutivity `β² = id` forces
`λ·bar(λ) = 1` — checked (`lambda_has_norm_one`) — which is exactly the
**Hilbert 90** hypothesis for the quadratic extension `ℚ(ζ)/ℚ(ζ)⁺` (the
bar-fixed field). `H¹` of that extension vanishes, so `λ = bar(c)/c` is
*always* solvable.

Rather than lean on the theorem, the probe exhibits the flip:

```
q = i    : rescale by bar-ODD c = 2i                        bar-EVEN -> bar-ODD   FLIPPED
q = ζ₆   : rescale by bar-ODD c = (√3+3i)/(√3−i)            bar-ODD  -> bar-EVEN  FLIPPED
```

`ζ − ζ⁻¹` is bar-odd by construction (`bar(ζ−ζ⁻¹) = ζ⁻¹−ζ`), and `ℚ(ζ)`
always contains it. So a bar-odd rescaling is always available and the parity
always flips.

The two points landing on *opposite* raw parities (`λ = +1` vs `λ = −1`) is
itself the symptom: nothing canonical distinguishes them.

## Why the real-resolvent prune worked and this one cannot

This is the part worth carrying forward.

The real Gram resolvent lived over **ℝ**, where the bar involution acts
**trivially**. Its parity was therefore *rigid*, and the bar-odd target `S`
was genuinely unreachable — a real prune
([`2026-07-19-c3-q0-real-routes-closed-fibre-phase-survives.md`](2026-07-19-c3-q0-real-routes-closed-fibre-phase-survives.md)).

At a root of unity, bar acts as the **nontrivial** Galois map `ζ ↦ ζ⁻¹`, and
`ℚ(ζ)` contains bar-odd scalars. Both parities are available for free.

**That is precisely why the fibre-level route survived the real-route
exclusion chain in the first place.** The same feature that let it survive is
the feature that makes bar-parity uninformative about it. Expecting bar-parity
to prune it was expecting the fibre route to have the rigidity whose *absence*
defines it.

## Operational consequence — do not spend the H₅ computation on this

Bean `qou-jcmw` (dim HH¹(H₅(ζ₅)) at the Bring root) remains worth doing **for
its dimension count**. But its *parity* leg should not be run expecting a
prune: the normalization-dependence argument above is **field-theoretic**
(Hilbert 90 over `ℚ(ζ)/ℚ(ζ)⁺`) and does not depend on `n`. `H₅` is dim 120 —
14 400 unknowns and ~1.7M Leibniz equations — so this is a real saving, and it
is exactly the formalize-first discipline paying off: the structural argument
pruned the expensive search rather than the search pruning the hypothesis.

## What would make a parity test meaningful

Bar-parity regains content only against a **pinned normalization**. Candidates,
none attempted here:

1. **An integrality / Habiro-lattice normalization** — fix the representative
   by requiring it to preserve a `ℤ[q,q⁻¹]`-lattice, so only units `±qᵏ`
   remain and the residual scaling group is small enough to carry an invariant.
2. **A pinned pairing against `tr_M`** — the c₃ swing is a *number*, not a
   class. Pin the whole construction `S = ⟨tr_M, Δ(x)⟩` for a canonical
   generator `x ∈ HH₀`, and read the parity of that number.
3. **A finer invariant than parity** — e.g. the class of the induced operator
   in a bar-equivariant K-group, where Hilbert 90 does not trivialize it.

Route (2) is the closest to what the c₃ front actually needs, since it is the
only one that produces a scalar comparable to `S`.

## Discipline

Nothing wired. No fit. The `cal-anchored` c₃ is untouched. Per AGENTS.md
§"Before declaring refuted", this is recorded as **scope-(a)**: a negative
about the readout, with no proved invariant excluding the HH¹ carrier itself.
The c₃/Q_β derivation gap is unchanged and remains open.
