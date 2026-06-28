# Calibration canon — the decay-width triple is the ideal-math canonical (READ FIRST)

**Date:** 2026-06-28
**Status:** CANONICAL — owner ruling 2026-06-26, corpus-complete via
PRs #2832 / #2866 / #2878, with the L2-dashboard data-integrity tail in
#2897 / #2902. This doc is the **anti-flip-flop "read first"** record for
the calibration framing; it supersedes the 2026-06-16 muon/lepton-ratio
convention.

## The ruling (one line)

The **ideal *mathematical* canonical** calibration triple is the three
**weak-sector observables** — a leptonic mass scale and two decay widths
— **not** three masses:

| CAL | Canonical observable | order | DOF of H¹(Bring)=2W | Numerical proxy |
|-----|----------------------|-------|---------------------|-----------------|
| CAL-1 | `m_e` (leptonic mass scale) | h⁰ | W-plane scale | `m_e` (CODATA) |
| CAL-2 | `𝔇_β` (neutron β-decay width) | h² | W-plane modulus `q₀` | `Q_β = ℏ/𝔇_β`; modulus overdetermined, pinned most precisely by `m_μ/m_e` |
| CAL-3 | `𝔇_π` (pion decay width) | h³ | orthogonal meson class | `m_π` (PDG) |

The masses `(m_e, m_μ/m_e, m_π)` and the Q-value `Q_β` are the **numerical
proxies**. **`Q_β` is the proxy for CAL-2 (`𝔇_β`) — NOT "derived, not a
calibration".** Same three H¹ DOF throughout: this is a *relabel* of which
observable is canonical (the principled decay widths) vs which is the
precisely-measured proxy (the masses), **not** a structural change. The Lean
witness `QOU.Mass.calibrations_eq_cohomology` is a count/alignment claim
(3 calibrations = 3 H¹ DOF) and is unchanged.

## Why this kept flip-flopping (the history)

1. The **pre-#2832 introduction** already stated the decay-width triple
   (`m_e`, `𝔇_β` CAL-2, `𝔇_π` CAL-3, with `m_e`/`Q_β`/`m_π` as proxies).
2. **2026-06-16** ([`q-anchor-drift-and-local-q-routes.md`](2026-06-16-q-anchor-drift-and-local-q-routes.md))
   "reconciled" the corpus the *other* way — making the **mass / lepton-ratio**
   form (`CAL-2 = m_μ/m_e`, `Q_β` *derived*) canonical. This is the framing
   now superseded.
3. **PR #2832** (intro cleanup) doubled down on the mass form and explicitly
   demoted `Q_β` to "derived rather than measured."
4. **Owner ruling 2026-06-26** reversed it back to decay-widths; **PR #2866**
   propagated it corpus-wide (both Propositions + their `.ts`/`.lean`,
   `epistemic-status-of-calibrations`, the AGENTS.md cheat-sheet + q₀-anchor
   §); **PR #2878** swept the last two content stragglers.

If you are tempted to "fix" the corpus back to three-masses / "Q_β derived",
**stop** — that is the reverted direction. The decay-width form is canonical.

## Ideal vs experimental m_μ (the recurring confusion)

The substrate modulus `q₀` has one value but two documented pins. The m_μ
**number you get depends on which** — and only the experimental one is an
accuracy result:

| layer | q₀ | m_μ = m_e·Vol(4₁)/ℏ_q² | meaning |
|---|---|---|---|
| **Ideal / canonical CAL-2** | muon-anchored `1.10997859555…` | **~0 ppb** | exact *by construction* — you used `m_μ/m_e` to pin `q₀`, so `m_μ` returns CODATA. This is the **calibration tautology**, NOT an accuracy win. |
| **Experimental / Physical-Observations** | proton-anchored ≈`1.10998` | **209.8 ppb / 963.6× FAIL** | the genuine 9.5σ prediction — the μ–p substrate tension. |

**The L2 100× dashboard reports the EXPERIMENTAL value** (209.8 ppb FAIL,
L2 = 3/7). Reporting the ideal ~0 ppb as "m_μ MET" is the recurring bug
(AGENTS.md §"q₀ anchor convention" STRICT rule 1; bean `tnjb`).

## L2-dashboard data integrity (bean `tnjb`, resolved)

- **m_μ pinned (#2897).** `computations/per_observable_100x_status.py` read
  m_μ from the upstream Borromean witness's `muon_check.m_mu_pred_MeV`, which
  commit `768d9ddf` flipped to the **muon** q₀ — so a regen silently
  substituted the ideal tautology (~0 ppb MET) for the experimental
  prediction. m_μ is now **PINNED** to `105.658397811` MeV (209.8 ppb / 963.6×)
  in both code paths, decoupled from `muon_check`. The pin is witness-
  independent **by design** — do **not** re-gate it on `muon_check` existence
  (a reviewer suggested this; it re-introduces the exact coupling the fix
  removes).
- **Q_β/m_n/Δ_pn refreshed (#2902).** Canonical-env regen (Python 3.11.15,
  mpmath 1.3.0, numpy 2.4.6, sympy 1.14.0 — exact match, zero engine churn)
  refreshing the stale upstream rows: Q_β 164.0×→160.1×, m_n 185.4×→181.0×,
  Δ_pn 163.3×→159.4×. Summary unchanged 3/7.

## Caveat — the proton-q₀ solver embeds a purged fit

`qou_substrate.constants._solve_q_proton_f64(mp_me, vol)` solves for the
proton-anchored `q₀`, but its closed form **embeds the fitted Habiro ratio**
`(1+46u⁴)(1+4u⁵)(1−29u⁶)…` — the CODATA fit that the production mass pipeline
explicitly **purged** per the canonical-derivation discipline. In the current
checkout the package constants `Q` *and* `Q_MP` are **both** the muon value
(`1.10997859555…`), so the proton `q₀` (≈1.10998) is **not** available as a
clean constant. Therefore canonical proton-anchored values (e.g. the m_μ
dashboard row) are **PINNED**, not recomputed through the fitted solver.

## Authoritative artifacts (where the canon lives now)

- [`AGENTS.md` §"Canonical derivation chain — cheat sheet"](../../AGENTS.md) —
  the CAL table + owner-ruling banner + the q₀-anchor STRICT section.
- [`content/.../mass-theory/three-calibration-inputs.md`](../../content/quantum-observable-universe/mass-theory/three-calibration-inputs.md)
  and [`.../observations/three-calibration-discipline.md`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md)
  — the two Propositions (+ their `.ts`/`.lean` siblings).
- [`content/.../observations/epistemic-status-of-calibrations.md`](../../content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md).
- `computations/per_observable_100x_status.py` — the pinned m_μ dashboard row.
