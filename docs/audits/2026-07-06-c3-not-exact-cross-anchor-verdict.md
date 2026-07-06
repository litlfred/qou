# c_3 is NOT exact −2 — cross-anchor exactness verdict (2026-07-06)

**Status:** VERDICT (settles the flip-flop for the 6th time — same
direction as the authoritative registry).
**Probe:** [`computations/qbeta/qbeta_c3_cross_anchor_exactness_probe.py`](../../computations/qbeta/qbeta_c3_cross_anchor_exactness_probe.py)
(reproducible, self-contained, 60 dps).
**Registry it confirms:** [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) §3
(c_3 tier = empirical / cal-anchored / not anchor-stable).

---

## What was claimed

A 2026-07-06 **docs-only** commit on `main` (`0d5243a0`) asserted that
the Q_β precision-ladder coefficient **c_3 = −2 exactly, for all q**,
coming from a fixed "standard block (2,1) trace `Δχ = −2.0`", and that
the previously-recorded ~2.4% cross-anchor **swing** was an artifact of a
**0-indexed generator bug `(0,1,0)`** in the Python Hecke/Hoefsmit
infrastructure. It edited three audit/scope docs but did **not** touch the
authoritative registry, the Lean, the extraction compute, or the
dashboards — so the corpus became internally contradictory.

## The verdict — (B) c_3 is q-dependent / anchor-swinging

Extracting c_3 on the **current, post-bug-fix** compute
(`c_3 = (Q_codata / Q_N2 − 1) / u³`, the exact production routine in
`qbeta_ck_cache.py:145` / `qbeta_utils.c3_target_at`) at both anchors:

| anchor | q₀ | c_3 |
|---|---|---|
| **proton-pinned** | 1.10997858275138… | **−2.06934257711516784** |
| **muon-pinned** | 1.10997859555733… | **−2.02018812814143946** |

- **Swing = −0.04915 ≈ 2.375% of c_3** — the two anchors agree to only
  ~1 significant digit. Neither is −2; `c_3 − (−2)` = −0.0693 (proton),
  −0.0202 (muon). (c_2 = −1 comes out identically at both anchors, as
  expected — that rung *is* exact.)
- The proton value reproduces the registry's recorded −2.0693 exactly,
  and the ~1.3×10⁻⁸ difference in q between the anchors moving c_3 by
  0.049 matches the registry's `dc_3/dq ≈ 4.6×10⁶`.

**Symbolic confirmation.** The *fixed theoretical* base ladder through
N=2 is `Q_theory/Q_base − 1 = c_2·u²` exactly, so its `[u³]` coefficient
is **identically 0**. There is no first-principles c_3. The −2ish number
only appears by dividing the **fixed experimental** `Q_codata` by the
**moving theoretical** `Q_base(q)` — i.e. the cal-anchored, circular
extraction (`qbeta_ck_cache.py` labels this tier `"cal-anchored"`,
`"circular"`, `q0_dependent: True`).

## The "(0,1,0) generator-index bug" narrative is a misdiagnosis

- Generators **are** 0-indexed in the current code (`σ_0, σ_1` for H_3's
  two generators ≡ 1-indexed `σ_1, σ_2`); `(0,1,0) ≡ σ₁σ₂σ₁` is the
  correct trefoil-type 3-braid word. **Not a bug.**
- The one **real** historical bug ([`2026-05-19-trm5-markov-bug.md`](2026-05-19-trm5-markov-bug.md))
  was the Markov *trace value* `TR_M[5]` (`z³` → `h·z²+z`); the current
  `pyhecke.gram.TR_M` already carries the **fixed** value.
- The extraction above runs on this **post-fix** code and c_3 **still
  swings 2.375%**. The "post-bug-fix" witness line in
  `qbeta_per_block_symbolic.py:219` refers only to that `TR_M[5]` fix.

## The "recursion for all c_k" and the "Toroidal/Weber" reframe

A recurrence circulated as *the* recursion for all c_k:

```
4(n+1)·b_{n+1} + 6n·b_n + (2(n−1) + k)·b_{n−1} = 0,   b₀ = (1/2)^k, b₁ = 0
```

This is **real and Lean-proved** (`MarkovParameterRecursion.lean`, PR
#1739) — but it is the recursion for the **Markov parameter `z(q) =
√q/(1+q)` and its powers `z^k`**, *not* for the c_k. Per
[`2026-06-02-qbeta-prearchimedean-recursion-status.md`](2026-06-02-qbeta-prearchimedean-recursion-status.md):
`τ_M(T_β) = A(q) + B(q)·z(q)` with `A, B ∈ ℚ(q)`, so `τ_M`'s recursion is
**higher-order** than z's (`a₁ ≠ 0` for τ_M vs `a₁ = 0` for bare z); the
c_k live in the `A, B` structure and the **f-map** bridging z → c_k is
the **open** problem. Three reasons this recurrence does not give the c_k:

1. **Wrong object.** It generates the (fixed, rational-derived) Taylor
   coefficients of `z(q)`, not the coefficients of `Q_β/Q_base`.
2. **A fixed recurrence yields a fixed sequence; the c_k are not fixed.**
   c_3 swings 2.375% between anchors, so no single `(k, seeds)` can equal
   both −2.0693 and −2.0202.
3. **The `k` is a knob, not a derivation.** The proved case is the
   specific `k = 1` / `(2n−1)` rung for z; generalizing `(2n−1) → (2n−2+k)`
   and choosing `k` (or the Weber `A=2, C=−22`) to hit target coefficients
   is fitting. The circulated Weber-ODE fit is itself telling: with three
   free knobs `A, B, C` it "matches" three coefficients by construction,
   and its own `c_3 ≈ −2.02` (non-integer) **confirms** the swing rather
   than an exact −2.

The **toroidal-harmonics basis** direction (a torus-knot Habiro trace
whose continuum limit lands in toroidal harmonics) is a legitimate
*structural* conjecture, but it does **not** close the f-map or make c_3
exact, and nothing based on it may be wired to production or the
dashboard until it produces an **anchor-independent** c_3.

## Consequences / discipline

- **No production change.** Q_β stays c_2-only (the honest prediction,
  ≈1279 ppb); m_n and Δ_pn inherit it. Wiring c_3 to "beat 100×" is
  **circular** — c_3 is extracted from the very `Q_codata` it would be
  compared against (`qbeta_ck_cache.py:168-171`). There is currently **no
  non-circular** route under the 100× target for Q_β.
- **Do not re-wire `q_beta_toroidal_mev` into `canonical_mass.py`** or
  clear the 50-dps proton witness on the strength of this claim — that is a
  fitted-tower / cache-clear regression against the
  [canonical-mass guardrail](../canonical-mass-formula-guardrail.md).
- Only **c_2 = −1** is Taylor-exact and Lean-proved
  (`q-beta-c-2-eq-neg-one-structural.lean`).

## Flip-flop ledger

This is the 6th settle of the c_3 direction; it agrees with the registry
and the [truncation-order framing](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).
The registry §8 flip-flop guard stands: any future wiring of a c_k≥3
requires owner approval **and** a passing proton+muon cross-anchor swing
test — which c_3 **fails** (2.375% swing).
