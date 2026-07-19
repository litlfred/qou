# α_EM R1/N3 — the eigenline computation; R1 closes at the semisimplified level (2026-07-19)

**Context:** the named remaining core of R1
([#4070](https://github.com/litlfred/qou/pull/4070) walk, item N3).

**Probe:** [`computations/alpha_em/alpha_em_r1_n3_eigenline_probe.py`](../../computations/alpha_em/alpha_em_r1_n3_eigenline_probe.py)
→ [`alpha-em-r1-n3-eigenline.witness.json`](../../computations/alpha_em/alpha-em-r1-n3-eigenline.witness.json)
— 4/4 PASS, sympy-exact.

**Scope guard (STRICT):** linear/semisimplified level; the unipotent
naturality merges into R2 (phase-4, owner-gated); no fit; nothing wired.

## The unlock

Bring is a canonically embedded genus-4 curve, so
**H^{1,0}(Bring) = the standard 4-dim S₅ representation** (holomorphic
differentials = linear forms; K = O(1) on the canonical curve). The
resolvent-differential basis the walk called for is therefore pure linear
algebra on the permutation representation — no period integrals needed at
this level.

## Results

1. **Canonical model vs Chevalley–Weil (new independent lock).** The deck
   4-cycle's eigenvalues on the standard rep are {1, i, −1, −i} — one per
   deck character, exactly the T1 CW dims, by an entirely independent
   derivation (linear algebra vs branch-point formula).
2. **The corpus's braid twist IS the deck generator up to conjugacy.** The
   spectral twist of `braid-group-action` is realized by `x_j ↦ x_{2j mod 5}`
   — verified to act on resolvents as `w_k ↦ w_{3k}` (the frequency-pair
   4-cycle) — an order-4 element of S₅, with an **explicit conjugator** to
   the deck 4-cycle exhibited.
3. **Same channel structure.** The twist's ±i eigenlines are 1-dim, lie in
   the standard rep, and conjugation carries +i to −i (the T3 theorem
   instance) — identical conjugation-paired structure to F's channel pair,
   with the labeling fixed by the forced shadow (#3960, no freedom).

## R1 status

The naturality square **commutes at the linear/semisimplified level**. The
only invisible piece is the unipotent (Jordan) part of the T2 monodromy —
finite-order automorphisms cannot carry it; its naturality *is* the
framework's τ-assignment on the braiding. **R1's remainder merges into R2**
(phase-4, owner-gated). There is no further computational content in R1.

## Final wall state (end of the arc)

```
1/(8π)  =  ½·a₀,  every factor derived through the merged program,
conditional on ONE owner-gated identification:
  R2 — the framework's τ assigns the T1-cover braid monodromy to the
       substrate braiding, with the tower's one-loop insertion
       F(b_s/[2]_q at q=1) weighted by a₀·α.   [phase-4]
```

---

> **🟧 Ruling update (2026-07-19, owner):** *R2 is NOT Lean/derived-proved.*
> R2 remains an unproven physics identification; `1/(8π)` stays phase-4; the
> program-outcome statement is "derived **conditional on R2**; R2 is open."
> Read-first: [`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md).
