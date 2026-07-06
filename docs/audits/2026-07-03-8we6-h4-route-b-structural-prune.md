# 8we6 — H₄ route B (λ⊢4 re-decomposition) structurally pruned; route A requirements sharpened

**Date:** 2026-07-03
**Bean:** `8we6` (u-rung tie decision: genuine c₄ rungs → Casoratian W₃ sign test)
**Owner directive:** routes B + A + C authorized (in that order) for the missing
c₄ rungs. This audit records the formalize-first analysis of route B *before*
any build (compute-author §3.3), and what it forces on route A.

## Route B as posed

Keep the exact, validated H₃ transition element
`Δ(net)(q) = NF(neutron) − NF(proton)` (words in σ₀, σ₁ only;
`free-neutron-decay.py`), include it in `H₄(q)` under the standard inclusion,
and read its b-graded λ⊢4 Hoefsmit block levels as the N=4 rung — "no new
physical object, so no ansatz risk".

## The prune (one-line structural argument, no compute needed)

Both functionals that could read an H₄-level rung off the **unchanged** element
are determined by H₃ data already in hand:

1. **Markov-trace consistency.** The normalized Markov trace is compatible
   with inclusions — `τ_M^{(n+1)}|_{H_n} = τ_M^{(n)}` is the *defining* Markov
   property. So `τ_M^{H₄}(Δ(net)) = τ_M^{H₃}(Δ(net))` identically in q:
   the trace route yields nothing new.
2. **Branching rules.** The λ⊢4 characters of an element of `H₃ ⊂ H₄` are
   fixed sums of λ⊢3 characters:
   `χ_{(4)} = χ_{(3)}`, `χ_{(3,1)} = χ_{(3)} + χ_{(2,1)}`,
   `χ_{(2,2)} = χ_{(2,1)}`, `χ_{(2,1,1)} = χ_{(2,1)} + χ_{(1,1,1)}`,
   `χ_{(1,1,1,1)} = χ_{(1,1,1)}`. Every per-block reading (b-graded or not)
   of the unchanged element is a **linear function of the H₃ block data** —
   it cannot contain an independent N=4 level.
3. The "net" functional (coefficient sum on the NF basis, the object the
   c₂/c₃^even s-series actually used) is likewise invariant: the GB reduction
   of σ₀σ₁-words is identical in H₃ and H₄ (no new relations apply).

**Scope (a):** route B — *re-decomposing the unchanged H₃ element at λ⊢4,
alone, in any of the three functional readings* — cannot produce a genuine
c₄^even rung. This is a scope-limited structural exclusion with the invariant
cited (Markov consistency + branching); it does not exclude H₄ objects with
genuine σ₂-support.

**Consistency check.** This is the same reason the C12 trace-level
`Ind_{H₃}^{H₄}` Markov-stabilization failed (PR #1850) and why the Stage-B
verdict's H₄ prescription says "**longer braid words**": the H₄ content must
enter through the *object*, not the *decomposition*.

## What this forces on route A (the surviving H₄ route)

The H₄ object **must have σ₂-support** (words touching the 4th strand).
Sharpened requirements, recorded for the build:

- **Gate (stability):** in whatever limit/normalization removes the 4th
  strand's coupling, the object's ladder must reproduce the trusted
  `c₂^even = −8.00641`, `c₃^even = +86.66116` exactly. If lower rungs move,
  the object is wrong (honest gate-fail, not a reinterpretation).
- **Design choices needed (new framework content — owner call, NOT agent
  ansatz):** (i) the 4-strand confinement braid replacing
  `B₃ = (σ₀σ₁⁻¹)³` — the corpus has **no** canonical 4-strand Brunnian
  braid (`KnotTheory/Brunnian.lean` is Borromean-only); (ii) the 4th
  strand's type and crossing rule (`crossing()` knows u-u / d-d / u-d;
  the brane/Hopf `else`-branch returns bare `σ_gen`). Candidate framings
  to put to the owner: brane-tower strand (bare σ₂ Hopf coupling), lepton
  strand (the e⁻ = σ₀σ₁σ₀ already lives in H₃ — a 4th strand could carry
  the emitted lepton), or a 4-component Brunnian confinement extension.
- The GB reducer (`reduce_verbose`) is n-agnostic (adjacent braid +
  distant-commute + quadratic Hecke rules on integer-indexed words), so the
  mechanical cost is H₄'s 24-word NF basis with symbolic q — feasible.

## Route C status (unchanged)

`c₄^odd` beyond CAL-anchor is the fibre-level Habiro element `F(q)` — the
registry's named open keystone (decay-side only, per the refuted-class map
post-C12). No new attack surface identified this session; W₃ built on the
CAL-anchored `c₄^odd ≈ −0.97` stays **conditional on that tier** even once
c₄^even exists.

## Cross-references

- [`2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md`](2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md) (the gated test)
- [`2026-07-02-1jrh-c3even-exact-measurement.md`](2026-07-02-1jrh-c3even-exact-measurement.md) (c₂/c₃^even exact)
- [`2026-06-16-hoefsmit-stage-b-attempt-verdict.md`](2026-06-16-hoefsmit-stage-b-attempt-verdict.md) (H₃ basis exhaustion; "longer braid words")
- [`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md) row C12
