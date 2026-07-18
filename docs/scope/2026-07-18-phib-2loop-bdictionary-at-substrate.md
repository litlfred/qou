# Φ_b 2-loop b-dictionary at m=q₀ — the F1 odd-channel unowned input

**Date:** 2026-07-18 · **Branch:** `claude/faddeev-phi-b-construction-wwblhu` ·
**Tier:** scope / plan (defines a decidable compute; no `c_k` wired; no fit; no tier change).

## Why this note

The [07-17 1ppq path reassessment](../audits/2026-07-17-1ppq-path-reassessment.md)
and [#3844's four-front coordination note](../audits/2026-07-17-four-front-gap-close-coordination.md)
converge on **one genuinely-unowned decidable piece** feeding F1 (the odd
D-ladder Écalle acceleration): *"the odd-channel resummation needs the deformed
b-dictionary normalization, which #3596's Φ_b construction supplies once its
saddle expansion is pushed to 2-loop at m = q₀."*

This session's #3902 result **closed the complementary geometric hypothesis** —
the bar-odd swing is carried by no smooth geometric/topological object (median
resummation smooth #3813; classical CS/Stokes anchor-invariant prune; 5₂ quantum
volume anchor-smooth #3902; substrate meridian generic, ~8.6e6× the anchor gap
from any 4₁/5₂ branch point, #3902). So the swing is representational — the 1/u³
inversion of a smooth N_odd — and F1's resurgent-transseries premise is the only
live route. This note scopes the Φ_b 2-loop b-dictionary that F1 needs.

## What the b-dictionary IS — and what it is NOT (anti-duplication)

The 4₁ Φ_b **state integral** has the semiclassical (b→0, ħ=2πb²=it) expansion

```tex
\log Z_{4_1}(m) \;\sim\; \frac{\mathfrak{V}(m)}{2\pi i b^{2}}
   \;+\; \tfrac12\log\!\det{}' \;+\; \sum_{n\ge 1} (2\pi i b^{2})^{n}\, S_{n}(m),
```

where `S_1(m)` is the **2-loop invariant**, `S_2(m)` the 3-loop, etc. The
`{S_n(m)}` at the deformed meridian **are** the b-dictionary coefficients the
odd D-ladder is built from. The leading finite-b correction `i·t·κ_1` already in
the corpus (`qbeta_c3_phib_saddle_state_integral_probe.py`) is the n=1 rung.

**Already on main (do NOT duplicate):**

- `qbeta_phib_saddle_fluctuation_transseries_probe.py` — the exact C6 Wick
  generator κ_1..κ_7 at the **undeformed root-of-unity Kashaev face** (m=1,
  s*=5/6). Real saddle only.
- `qbeta_phib_saddle_fluctuation_complex_meridian_probe.py` — deforms that Wick
  generator via the linear tilt `Φ_μ(s)=Φ(s)+μs`, `2\sin(\pi s^*)=e^{-\mu/2}`,
  validated against the exact ladder at μ=0; emits κ_n(μ) at a **token**
  μ=i·0.01.

**The gap this branch closes** — four things the complex-meridian probe does not
do, which together constitute "the 2-loop b-dictionary at m=q₀":

1. **Substrate-window evaluation.** Evaluate the deformed orders across the
   actual anchor window (both q₀ pins), not a token μ=i·0.01.
2. **Bar-parity decomposition.** Split each fluctuation order into its
   bar-even/bar-odd parts under `m ↔ 1/m` (q ↔ q⁻¹) — the odd part is the
   object F1 resums.
3. **q-Gevrey-order test vs #3861.** #3861 found the odd D-ladder has a single
   mild q-Gevrey order ~0.07–0.09. If the deformed odd b-dictionary orders grow
   at that same rate, the b-dictionary is confirmed as F1's correct generating
   object and its normalization is pinned.
4. **q\*/A′(q\*) consistency.** The investigation pinned two data the odd
   b-dictionary must reproduce: **q\*** (the S=0 point) and **A′(q\*)≈2.37**
   (the smooth-numerator slope, `BarOddLadderShape`). Test the odd order's
   zero/slope against them.

## The ħ ↔ 2πi/N caveat (STRICT — no bridge claim)

The Kashaev (N→∞) κ-ladder and the Φ_b (b→0) state-integral tower relate by
**resummation, not term-by-term reparametrisation** (bridge growth-obstruction
audit). For the **perturbative** invariants `S_n(m)` around the single geometric
saddle the two asymptotic series agree up to the expansion-variable
normalization (quantum modularity, Andersen–Hansen) — that is the *only* content
used here. No non-perturbative sector, no Stokes datum, and **no map from the
physical Q_β observable to a meridian** is claimed: μ is a geometric parameter,
never fixed from QOU data. Anti-laundering: 4₁ geometric facts only; nothing
wired; the meridian↔Q_β map stays the open keystone bridge.

## Deliverables

- **Stage 0** (this branch): `qbeta_phib_2loop_bdictionary_probe.py` — deformed
  fluctuation orders S_n(m) across the substrate window; bar-parity split;
  q-Gevrey-order test vs #3861's ~0.07–0.09; regression to the corpus
  `i·t·κ_1`; q\*/A′(q\*) consistency of the odd order. Witness-backed.
- **Ledger + coordination:** append to `docs/coordination/1ppq-qbeta.md`;
  update #3844 (F1) with the pinned normalization / q-Gevrey match.

## Discipline

No `c_k` wired; registry untouched; scope-(a)/(b) with cited invariants; witness
provenance (script committed before witness); `lean`-direct only for any Lean.
The b-dictionary is a *derived* geometric normalization or it is not wired — the
anti-fit / anti-laundering rules gate *how*, per the 2026-07-11/07-13 general
reversals (which open the *direction*, not the honesty bar).

## Cross-references

- #3844 four-front note: [`2026-07-17-four-front-gap-close-coordination.md`](../audits/2026-07-17-four-front-gap-close-coordination.md)
- Reassessment: [`2026-07-17-1ppq-path-reassessment.md`](../audits/2026-07-17-1ppq-path-reassessment.md)
- Branch-point closure: `docs/coordination/1ppq-qbeta.md` (2026-07-18 entries)
- Existing Wick generators: `qbeta_phib_saddle_fluctuation_{transseries,complex_meridian}_probe.py`
