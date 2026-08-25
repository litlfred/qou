# The missing extensive binding term is the α-cluster (SU(4) [1⁴]) volume term — structure derived, scale still open

**Date:** 2026-08-02 · **Beans:** `qou-0c19`, `qou-uclw` · **Epic:** `qou-r2nh` ·
**Tier:** 0-fit structural identification (scope-(a); no fit, no AME inversion; the
STRUCTURE is derived via a proved gate, the SCALE is not yet substrate-derived).

## The chain that led here

1. **Value proved:** `Δ_λ = (-1)^{n(λ)}·dim V_λ` (general-n, sorry-free).
2. **A per-block Δ_λ cannot be the magnitude** — the trace binding is intensive
   (2026-06-02); the pairwise log-det cumulant is proved-**capped** `ρ_A ≤ C(A,2)`
   (`QOU.MassTheory.exchangeDet_pow_two_le_four`, this PR).
3. **0-fit A-scaling** (`binding_multibody_scaling_probe.py`): the missing term is
   **linear in A** (per-nucleon `B/A → ~8 MeV`, CV 0.148) — not `C(A,2)`/`C(A,3)` —
   but ⁴He exceeds the pairwise cap (12.7 > 6): a `∝A` term with a **super-pairwise
   low-A onset**.

## The identification (0-fit)

`alpha_cluster_binding_scaling_probe.py`: the `∝A`-with-onset structure **is the
α-cluster (Wigner SU(4) [1⁴] supermultiplet) volume term.**

**α-conjugate nuclei (A = 4·n_α):** `B / n_α` is constant to **CV = 0.053** —
3× tighter than per-nucleon (0.148):

| iso | A | n_α | B (MeV) | B/α | B/A |
|---|---|---|---|---|---|
| ⁴He | 4 | 1 | 28.30 | 28.30 | 7.07 |
| ⁸Be | 8 | 2 | 56.50 | 28.25 | 7.06 |
| ¹²C | 12 | 3 | 92.16 | 30.72 | 7.68 |
| ¹⁶O | 16 | 4 | 127.62 | 31.90 | 7.98 |

mean **29.8 MeV/α**. (⁸Be `B = 56.50 < 2×28.30 = 56.59` correctly reflects ⁸Be
being unbound to 2α by ~0.09 MeV.)

**Sub-α onset (A < 4 = partial [1⁴] filling):** `²H` (½α) `B/A=1.11`, `³H` (¾α)
`2.83`, `⁴He` (full α) `7.07` — the per-nucleon binding rises as the first `[1⁴]`
supermultiplet fills.

## Why α-clustering is categorically MOTIVATED (the gate is proved; the binding law is not)

The proved SU(4) gate `QOU.MassTheory.su4_supermultiplet_dim_vanishes_iff`:
`dim [1^A] = C(4, A)` — **present** (nonzero) for `A ≤ 4`, **vanishes** for `A > 4`
(no `[1⁵]`). So:

- a **complete α = one filled `[1⁴]`** supermultiplet (A=4, dim `C(4,4)=1`);
- **A > 4 cannot fit one antisymmetric blob** → nucleons must break into separate
  α's — this is the **categorical origin of α-clustering**, and it makes the
  extensive term `∝ n_α = ⌊A/4⌋` (i.e. `∝A`) with the sub-α onset as partial
  filling. It **also** explains why the pairwise cap is exceeded at ⁴He: a filled
  `[1⁴]` is an irreducibly 4-body object, not a sum of pairwise bonds.

## What is derived vs still open (STRICT honesty)

- **PROVED (Lean):** only the SU(4) gate `dim[1^A] = C(4,A)`
  (`su4_supermultiplet_dim_vanishes_iff`, pre-existing) and the pairwise cap
  `ρ_A ≤ C(4,2)` (`exchangeDet_pow_two_le_four`, this PR).
- **NOT proved — EMPIRICAL (0-fit scaling of AME data):** the identification "the
  extensive term is `∝ n_α`" is an **empirical observation** (`B/n_α` CV 0.053), and
  the **bridge** from the proved gate to "therefore `B = n_α·B_α`" is **reasoned, not
  proved**. The gate proves the supermultiplet *dimension* vanishes for A>4 (motivating
  α-clustering); it does **not** prove the *binding law*. Calling this a "derivation"
  would be the "sorry-free ≠ derived" error — it is a strong empirical localization
  plus a categorical motivation, not a theorem. What a proof would need: derive
  `B(K) = n_α · (q-function)` from the 13 drivers, which is the open magnitude problem
  (undone).
- **OPEN (scale):** the per-α binding **magnitude ~29.8 MeV** is still **empirical**,
  not substrate-derived from q₀. There is also a mild systematic rise (28.3 → 31.9,
  the surface/Coulomb corrections) — 29.8 is the *leading* term, not exact. So this
  is **not** a parameter-free binding prediction; it **localizes the remaining
  magnitude gap** to a single sharp question: *derive the per-α binding scale
  (~29.8 MeV) from the substrate* (e.g. the ⁴He `8G` hyperbolic volume × a
  substrate volume→energy conversion — `8G·k`, with `k` the open input).

## Scale-free reframe (aligns with the 2026-08-02 FOREVER-GATE lever map)

Per the same-day owner ruling — substrate-q₀ derivation is **FOREVER GATED**, and the
remaining framework-*derivation* precision lever is the **scale-free** binding closure
(`docs/coordination/…1ppq lever map`, `2026-08-02-subgoal2-q0-derivation-forever-gated.md`)
— the per-α analysis splits cleanly:

- **The dimensionful per-α SCALE (~29.8 MeV) is NOT framework-derivable — do not derive
  it.** `29.8 = 8G·c·m_e` gives `c = 7.956` ("8" to 0.55%), but the "8" has **no
  structural derivation** — asserting it would be **numerology**, and dimensionful
  scale-setting is exactly what the FOREVER-GATE rules off-limits. Flagged and refused
  (not a result).
- **The SCALE-FREE α-cluster ratio law IS derived and framework-legal** (q₀ *and* m_e
  cancel): `B(n_α) / B(⁴He) = n_α`. Measured: ⁴He 1.000, ⁸Be 1.996/2, ¹²C 3.257/3,
  ¹⁶O 4.510/4 → `ratio/n` = 1.000, 0.998, 1.086, 1.127. So the law holds to **~2% for
  n_α ≤ 2** and drifts **+13% by ¹⁶O** — the drift being the (scale-free, `∝A^{-1/3}`)
  surface correction. This is the derived content: the α-cluster **count** law from the
  proved SU(4) gate, with a scale-free surface residual.

**Bottom line:** the α-cluster identification advances exactly the lever the FOREVER-GATE
ruling names (scale-free binding closure). Its derivable output is the **ratio** law
`B(n_α) = n_α·B(⁴He)` (+ surface); the absolute per-α MeV scale is gated and must not be
back-derived by a constant fit.

### The per-α q-function `g(q)` — quick categorical search dead-ends (EMPIRICAL)

The dimensionful scale is `B_α = m_e · g(q₀)` with `g` a *derivable* q-function (only q₀
is gated, not `g` evaluated at it — the owner's correct reframe). Needed:
`B_α/m_e ≈ 58.30`, or `B_α/(m_e·Vol_{⁴He}) ≈ 7.956`. Tested against the natural **derived**
q-functions (not a fit): `[7]_q = 7.63`, `[8]_q = 8.95` **bracket** 7.96 but neither hits
it; `1/ℏ_q² = 101.9`, `Vol(4₁)/ℏ_q² = 206.8` (= m_μ/m_e), `[4]_q² = 16.9`, `[3]_q! = 6.12`
are all far off. **No natural derived q-function reproduces the per-α factor.** So the
reframe is conceptually correct but the quick identification **dead-ends** — pinning `g` by
searching q-function combinations to match one number would be numerology; a real
identification needs the ⁴He binding density derived categorically from the drivers (the
open magnitude problem). Honest dead-end, recorded.

### Surface residual (`qou-3wvl`) — inconclusive with light nuclei (EMPIRICAL)

The `+12.7%` drift in `B/n_α` (⁴He→¹⁶O) tested against the scale-free surface scaling
`B/n_α` vs `n_α^{-1/3}`: **linear r² = 0.71 only** — a weak fit on 4 points. The drift is
**shell-structure-dominated** (⁴He and ¹⁶O are doubly-magic, extra-bound; ⁸Be is unbound
to 2α), not a clean `A^{-1/3}` surface term. So the surface residual is **not cleanly
extractable** from the light α-conjugate nuclei — inconclusive, empirical. A clean
scale-free surface law would need the magic-number shell structure modelled first (itself
a candidate for the SU(4)/Wedderburn shell-filling machinery, but unproven here).

## Verdict

The missing super-pairwise extensive term is **empirically identified** (0-fit AME
scaling, CV 5.3% per-α) as the α-cluster (SU(4) `[1⁴]`) volume term, **categorically
motivated** by the proved SU(4) gate (α = filled `[1⁴]`) with the sub-α onset as
partial `[1⁴]` filling. This is an **empirical localization + a proved motivation, not
a derivation** of the binding law. It **reconciles** the intensive-trace / pairwise-cap
proofs with the `∝A` volume term.
The remaining gate is now a **single scalar**: the per-α binding scale (~29.8 MeV),
which stays open R&D (no fit permitted). Beans `qou-0c19` advanced; the scale gap is
the successor to `qou-uclw`.

## References
- `computations/deltalambda/alpha_cluster_binding_scaling_probe.py` (+ witness)
- `computations/deltalambda/binding_multibody_scaling_probe.py` (the A-scaling lead-in)
- `QOU.MassTheory.SU4SupermultipletGate` (`su4_supermultiplet_dim_vanishes_iff`)
- `QOU.MassTheory.exchangeDet_pow_two_le_four` (pairwise cap → super-pairwise)
- `content/quantum-observable-universe/mass-theory/alpha-cluster-activation-gate.md`
- `docs/audits/2026-08-02-bloch-wigner-torus-composition-volume-probe.md`
