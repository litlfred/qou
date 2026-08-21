# The f-map cannot force `c₃ = J_Hopf(1) = −2` from the D two-row trace — a two-reason fence

**Date:** 2026-08-21 · **Bean:** `qou-cds1` (f-map attack) · **Tier:** scope-(a)+(b)
exclusions, classified below · **Discipline:** no fit, no wiring, no tier change;
the value `−2` stays the skein-derived `J_Hopf(1)` (`JonesHopfSkein.lean`), only
its *identification* as the N3 coupling is at issue.

## What was attempted

Three independent feasibility probes tried to **derive** the c₃ identification
`c₃ = J_Hopf(1) = −2` (currently a 3.47 % near-match, not a derivation) from the
convention-D two-row Temperley–Lieb Markov trace, whose weights are now fully
characterised in Lean (`LadderConventionLocalisation.lean`: `b² = 1 − y₂₁ᴰ`, the
S2 weight solutions, `z_D·[2]_q = q²`):

- **Route A — bar-odd crossing term** (KC18 `tr_M = h²/2 − h·z`).
- **Route B — Z3 carrier** `G·(bar-odd carrier)`, bar-even functional `G` × the
  KC15 bar-odd carrier `D(q)` (or `κ_(2,1)`).
- **Redirect — bar-even channel** (the `b`/`y₃ᴰ` structure, after A showed the
  target is bar-even).

All exact over ℚ(q):
`computations/qbeta/fmap_c3_parity_genericity_exclusion.py` (19/19 assertions).

## The result — three routes, two reasons, one fence

`c₃ = −2 = J_Hopf(1)` is the value at `q = 1` of the Hopf-link Jones polynomial
`−(q²+q⁻²)`, a **bar-EVEN** quantity (`q ↦ q⁻¹` fixes `q²+q⁻²`), nonzero (`−2`).

### Routes A and B — REFUTED, scope-(b), by a proved parity invariant

The bar-odd part of any function vanishes at the bar fixed point `q = 1`
(`barOdd f 1 = (f 1 − f 1)/2 = 0`). Verified: the bar-odd part of the D two-row
trace of every `σ^k` (`k = 1..5`) vanishes at `q = 1`; every `G·(bar-odd carrier)`
Z3 product is bar-odd and vanishes there. So **no bar-odd construction — crossing
term or Z3 carrier — can produce the bar-EVEN value `−2` at `q = 1`.** This is a
proved invariant, formalised sorry-free in
`content/quantum-observable-universe/lean/QOU/QBeta/FMapC3ParityExclusion.lean`
(`barOdd_at_one`, `barOdd_ne_hopf_value_at_one`), so it qualifies as a scope-(b)
structural exclusion. It is the single reason both A and B fail — and it supplies
the *mechanism* for the note already in `dWeights_at_one` ("no forced-c₃ lemma").

### Redirect (bar-even channel) — REFUTED, scope-(a), by genericity

Having established the target is bar-even, the bar-even channel still fails to
*force* `−2`, for two anti-fit reasons:

1. **q=1 genericity.** `−2` at `q = 1` is hit by many natural bar-even
   D-combinations — `−[2]_q`, `−(q²+q⁻²)`, `−y₃/y₂₁`, `−1/(2y₂₁)` all `= −2`
   there. Matching the q=1 value pins nothing (the offset-genericity trap, cf.
   the S_leak sign-flip).
2. **No full q-identity.** The actual Hopf polynomial `V(Hopf)(q) = −(s+s⁵)`
   (`s = √q`, skein-derived) is **not** bar-even, so no bar-even weight object
   equals it as a q-identity — only its q=1 *value* coincides.

This is scope-(a): it excludes the *bar-even-weight-combination* approach, not
every conceivable derivation.

## Net

The **D two-row trace / weight structure cannot force `c₃ = −2` in either
parity** — bar-odd by a proved invariant (scope-b), bar-even by genericity
(scope-a). Three converging routes, one fence. The value `−2` is real; its
identification as the N3 coupling is a q=1-value near-match.

## What remains open — route C only

The single untouched route is the **analytic Φ_b state-integral / Lawrence–
Rozansky amplitude leg** — structurally different from the trace-weight routes
(it is not a bar-parity object). This matches the corpus's own assessment: the
QPlancherel result proved the c_k wall is the *amplitude* leg (not normalisation),
and prior attempts on it (C16 Habiro-integrality, C17 qZeilberger, C18 PSLQ) were
refuted or entropy-blocked. A probe gathered its ingredients (the Faddeev `Φ_b`
semiclassical coefficients `s_n = B_{2n}/(2n)!`; the 4₁ κ-tower `κ₁ = 11√3π/108`,
`κ₂ = 2π²/27`) but the c_k-reduction test was not completed. It is the genuine
deep frontier, not a quick check — and it is where any future f-map attack should
go, since the trace-weight parity/genericity fence is now closed from both sides.
