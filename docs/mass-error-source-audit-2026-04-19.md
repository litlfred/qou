# Where the mass-prediction error comes from — breakdown audit

Post-electron-inclusion mass predictions (2026-04-19):

| Atom | B_pred (MeV) | B_AME (MeV) | Gap (MeV) | Error % |
|------|-------------:|------------:|----------:|--------:|
| D    | 1.4373       | 2.2245      | 0.787     | 0.0420% |
| T    | 6.3600       | 8.4818      | 2.122     | 0.0754% |
| 3He  | 7.6547       | 7.7180      | 0.063     | 0.0023% |

The error comes from multiple sources; this note separates
**deterministic approximations** (known-size truncations) from
**guesses / modelling choices** (could be wrong by O(1)).

## 1. Deterministic approximations (bounded)

| Source | Expected size on D | Bound type |
|--------|-------------------:|------------|
| Kähler order-0 truncation | `ε ~ ℏ_q³ · tower_1 ≈ 0.14 MeV` | Taylor remainder |
| Brane-tower single-level | `ℏ_q² · tower_2 ≈ 0.014 MeV` | geometric series |
| Plancherel vs canonical weight | up to ~30% × tower term | weight-convention difference at q ≠ 1 |
| Partition-sum numerical | ~10⁻⁶ relative | numpy precision |

**Sum of known approximations for D: ~0.2 MeV bound.**  Gap is
0.787 MeV — so ~0.6 MeV is UNACCOUNTED FOR by these.

## 2. Guesses / modelling choices

**Each of these is a choice that could be wrong by O(1).**

| Choice | Value | Derived? | Fallback risk |
|--------|-------|:--------:|---------------|
| q₀ | 1.1099785955541805 | fit to m_μ/m_e | single free parameter; all else derives |
| gluon per nucleon | 1·σ₀ | atom-level SDP search (K=5) | K=5 LP-dual-correct set; still small |
| inter-nucleon m_pp, m_pn, m_nn | (1, 1, 1) | confinement-level-walk ILP | integer-LP, H_3-local |
| nucleon ordering | ppp...nnn | convention | shell-model says pnpn... |
| quark content | uud (p), udd (n) | standard | universal |
| B₃ per nucleon | (σ₀σ₁⁻¹)³ | Borromean conjecture | paper-level |
| electron placement | Z × σ₁⁻¹ at end | hecke_core convention | not derived |
| E_0 archimedean | 0.782 MeV = m_n − m_p − m_e | β-decay Q | single calibration |

**Most fragile (session evidence):**

- **nucleon ordering** — canonical trace on D collapses from
  `+0.47` (no electrons, ppnn) to `+0.0017` (electrons included,
  ppnn) while 3He barely changes.  This asymmetry under swap
  between D (odd Z, odd N) and 3He (even Z, odd N) hints the
  ordering convention matters; shell-model pnpn interleaving
  could dissolve the D collapse.
- **electron placement** — putting all Z σ₁⁻¹ at the end creates
  a pile-up of the same generator that doesn't correspond to
  physical electron structure.  Distributing electrons differently
  (e.g., one per proton, inserted at that proton's position) might
  remove the D collapse.
- **gluon count** — atom-level SDP says 1·σ₀ is universal among 5
  candidates; but a broader search over length-2+ combinations
  hasn't been done.

## 3. Breakdown by contribution

For D (Z=1, N=1) after electron inclusion:

```
B_canon  = +0.0017 MeV   canonical Ocneanu tr_M(|W_free| − |W_atom|)
B_tower  = +1.4356 MeV   ℏ_q² · (m_free − m_atom) at level 1
B_pred   = +1.4373 MeV   total
AME      = +2.2245 MeV
gap      = +0.7872 MeV
```

- **Canonical term is nearly zero on D.** This is the B/M
  cancellation effect from
  [rem:atom-trM-cancellation-ratio](#rem:atom-trM-cancellation-ratio):
  tr_M_atom ≈ tr_M_free after electron inclusion, leaving
  canonical ≈ 0.  For 3He the free/atom traces differ more, so
  canonical = +1.17 MeV stays large.
- **Tower term is the main prediction** (~1.44 MeV on D).  Gap
  to AME 2.22 is 0.78 MeV = 35% of the tower value.

**Where is the 0.78 MeV gap?**  Consistent with:

- Tower uses scalar pair V̂_i · V̂_j (known to drop content
  correlation) — maybe 20–30%
- Single-generator volume uses a fixed Wedderburn weight
  convention (sym / std / alt channels with fixed W_SYM, W_STD,
  W_ALT) that hasn't been systematically audited at the atom
  level
- Electron contribution: Z × σ₁⁻¹ sits as a block at the end;
  its contribution to the per-generator V̂_i decomposition
  concentrates on gen 1 (first nucleon's slot) creating a
  possibly-mismodelled single-channel value

## 4. Where to look next

Ordered by session-impact likelihood:

1. **Nucleon ordering** — test pnpn vs ppnn on D.  If D's canonical
   jumps from 0.0017 back to ~0.5 MeV under pnpn, ordering IS the
   main issue.
2. **Electron distribution** — test 1 electron per proton, placed
   at the proton's location, vs Z electrons at the end.
3. **Broader gluon search** — K=9 (include length-2) at Plancherel
   level with electrons.
4. **Kähler order 1 with symbolic Padé** — tighten the ε bound on
   the tower Taylor truncation.
5. **Audit Wedderburn weights** — verify W_SYM / W_STD / W_ALT are
   the correct choice at the atom level.

## 5. What is NOT the error

Things I've verified are NOT rate-limiting:

- **Frobenius positivity** — all real Hecke products have xᵀGx ≥ 0
  (v_hat_gram_projection_probe); the 6D LP-SDP gap is real but for
  LP minimizers, not for actual atom NFs.
- **Jet-level truncation** — converges at level 3 with ℏ_q² damping
  (prop:jet-tower-convergence).
- **Seminormal numerical precision** — dominant partitions
  computed to 10⁻¹⁰ or better.
- **Bibliography / Lean references** — audit-clean, 0 errors.

## Summary

**Deterministic approximations account for < 0.3 MeV of the 0.79 MeV
gap on D.**  The remaining ~0.5 MeV is in the modelling choices —
most likely ordering convention and electron placement, per the
asymmetric D/3He behaviour under electron inclusion.
