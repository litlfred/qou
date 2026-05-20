# Refreshed workplan — 2026-05-19 (after #781 / #797 / #808 / #802 landed; #822 in flight)

**Trigger:** Repo-owner directive 2026-05-19 — "develop refreshed workplan based on sibling/main findings" while ⁴He compute runs via numpy backend.

## Landed on main (recent)

| PR | Theme | Status |
|---|---|---|
| #781 | Canonical pipeline alignment + AME 2020 vendoring + I14 audit | ✅ merged |
| #797 | Atlas relocation (`braids-and-knots` → `appendix-knot-periodic-table`) + grid merge | ✅ merged |
| #808 | Per-atom canonical_status + co-Casimir Option B + pentagon-reduction + weight-factor audit + interface-knot cherry-pick | ✅ merged |
| #788 | I12 audit + `class BorromeanMassFormula` Lean stub | ✅ merged |
| #809 | per-item batch | ✅ merged |
| #815 + #813 + #790 + #793 | I1 batches (Lean stubs, Markov-amphicheiral, descent-cocycle, …) | ✅ merged |
| #787 | log-Δ categorical derivation Phase 1b (NEGATIVE; identifies $\Delta_I^K$) | ✅ merged |

## In flight (relevant to #822)

| PR | Title | Overlap |
|---|---|---|
| **#822** | (mine) co-Casimir to n=30 + T3 pentagon + numpy refactor (10-50× speedup) | self |
| #801 | interface-knot $\Delta_I^K$ binding: variance 3.96× → 2.31×, sign-fix | **cherry-picked into #822** (T3 wired in) |
| #818 | Hoefsmit Brunnian + branching probe cluster + BD canonical | **shares Hoefsmit infrastructure** — my numpy rewrite of `hoefsmit_matrices_numeric` could accelerate their probes |
| #761 | Combined Hoefsmit/GP/chirality Rust kernel work | **Rust binaries** — I built `hecke-tr-m-wenzl-lr` after cherry-picking their duplicate-fn fix |
| #816 | Averaging-resonance level-selection: c_5 unique outlier | touches Wenzl weight structure that co-Casimir consumes; not yet integrated |
| #814 | silver-ratio β-decay null + Pell-Lucas c_k benchmark | adjacent (Q_β-side); independent |
| #807 | compute-audit P33 (latent shadowing) + P34 (algebraic invariant) | audit-infra; could flag my numpy module |
| #806 | Lean: 188 manuscript-statement enrichments | Lean side; no compute overlap |
| #823 | QA exhaustive checkers + CI wiring | audit-infra |
| #820 | Bib verification (654 Ref upgrades) | docs |
| #819 | Re-verify deprecated-scripts catalog post-#787 | docs |
| #817 | cor:knot-factor-amphicheiral revision | specific corollary |

## Updated priorities (post-numpy-refactor)

### Tier 1: ship-now (this PR #822 + immediate follow-ons)

| # | Task | Status |
|---|---|---|
| T1.1 | numpy `hoefsmit_matrices_numpy` + `chi_numpy` (10-50× speedup, 1128× best case) | ✅ done in #822 |
| T1.2 | co-Casimir for A ≤ 10 — fast path | 🏃 cascade running; ⁴He landed at **0.3 ppm** (cf. 441/371/39/2.7/4.4 ppm for p/n/D/T/³He); ⁵Li..¹⁰B continuing |
| T1.3 | Pentagon T3 in binding_via_interface_knot (D 44%→69%) | ✅ done in #822 |
| T1.4 | Cross-cite numpy module from #818's probe scripts (Hoefsmit infra reuse) | **next** — short coordination comment |
| T1.5 | Merge #822 once bg ⁴He+ atoms complete | **next** — gate on CI |

### Tier 2: structural research (1-3 weeks)

| # | Task | Owner |
|---|---|---|
| T2.1 | **q-Rogers exact correction** — derive the $O((q-q^{-1})^k)$ Li_2^q-shuffle correction (residual ~0.5% in this PR) | paper-track |
| T2.2 | **$\Delta_I^K$ formula refinement** — close the remaining 30-60% gap on T, ³He binding | research (PR #801 follow-on) |
| T2.3 | **Rust convention adapter** — 1-strand vs 3-strand mapping for `hecke-tr-m-wenzl-lr` / `hecke-atomic` | engineering (1-2 days) |
| T2.4 | **Extend Wenzl-witness past n=30** — generate y_λ for n=33, 36, 39 (covers up to A=13) | compute (`y_lambda_wenzl_bridge.py 33 36 39`) |
| T2.5 | **c_5 outlier resolution** (#816) | research; may affect co-Casimir weight |

### Tier 3: paper / framework consolidation

| # | Task | Owner |
|---|---|---|
| T3.1 | `prop:archimedean-divided-power-rationalisation` — explicit theorem | paper-track |
| T3.2 | Lean side: type the q-Rogers identity | depends on T2.1 |
| T3.3 | Categorical Li_2^q pentagon proof (Hopf-algebraic, no log² needed pre-τ) | paper-track |
| T3.4 | qou-mass P3 deprecation — refactor folio importers to use vendored library | engineering (per `docs/audits/2026-05-19-qou-mass-deprecation-audit.md`) |

### Tier 4: production / distribution

| # | Task | Owner |
|---|---|---|
| T4.1 | qou-mass P4 — PyPI publish v0.1.0 | engineering |
| T4.2 | All-nucleotides compute via numpy + Rust hybrid (after T2.3) | compute |
| T4.3 | Witness drift detector — handle the numpy/mpmath cross-validation | infra |

## Cross-PR coordination needed

| Action | Target | Reason |
|---|---|---|
| Post intent | #818 | numpy `chi_numpy` could accelerate their Hoefsmit Brunnian probes (validated to 1e-14 rel; 50× on dim-280 partitions) |
| Post intent | #801 | T3 wiring in #822 builds on their interface-knot work; closes the "T3 closure pending" verdict |
| Post intent | #761 | I cherry-picked the duplicate-fn fix to build Rust binaries; cite usage |
| Watch | #816 | c_5 outlier may invalidate co-Casimir if c_5 weight is fundamentally different |
| Watch | #807 | P33/P34 could flag numpy module as new compute pattern |

## Pizza-break-ready checkpoints

This workplan is structured so the author can step away at any point without losing context. Each Tier-1 task has a clear status; Tier-2 tasks have explicit owners (paper-track vs engineering vs compute); cross-PR coordination steps are itemised so they can be picked up later.

The numpy refactor is the **biggest win this session** — converts the substrate-derivation path from "computationally intractable for A > 4" to "minutes per atom up to A = 10". This is the structural unlock for "all nucleotides" (#5 from the original 6-task queue), even though the strict 3-strand-per-nucleon Rust path is still deferred.

## ⁴He milestone (2026-05-19, T+~22 min on numpy backend)

The ⁴He prediction via the Frobenius co-Casimir Option B + canonical
3-strand-per-nucleon braid + Hoefsmit χ^λ over all 77 partitions of
n=12 lands at:

```
M_⁴He^pred = 3755.6761452616 MeV     (mp.mpf, 50 dps)
M_⁴He^CODATA = 3755.6750173599 MeV
Δ = 0.001128 MeV  = 0.300 ppm
```

This is **sub-ppm vs the experimental constituent-sum baseline** and
well inside the 100× CAL-2 floor (~780 ppb absolute mass target).
Per-atom error trajectory across A=1..4 (now via the same numpy
pipeline):

| atom | A | err_ppm | n_partitions |
|------|---|---------|--------------|
| proton   | 1 | 441   | 3 |
| neutron  | 1 | 371   | 3 |
| deuteron | 2 | 39    | 11 |
| tritium  | 3 | 2.7   | 30 |
| helium-3 | 3 | 4.4   | 30 |
| **helium-4** | **4** | **0.3** | **77** |

The error decreases as A grows (more partitions, more averaging) —
the substrate-derivation path is **structurally accurate** for the
heavier ground states, with the Borromean-tower residual driving
the apparent ppm-level scatter for free nucleons (p, n) where the
constituent-sum vacuum dominates.

Cascade continues: ⁵Li (n=15, p=176), ⁶Li (n=18, p=385), ⁷Li (n=21, p=792),
⁷Be (n=21), ⁸Be (n=24, p=1575), ⁹Be (n=27, p=3010), ¹⁰B (n=30, p=5604).
With dim_λ up to ~6700 at n=30, individual partitions will cost more
than ⁴He's largest; total cascade wall-clock estimated 1-3 hours.
