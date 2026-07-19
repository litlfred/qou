# The bar-odd 5₂ Stokes datum is majority non-abelian — why every scalar closed-form search fails

**Date:** 2026-07-19 · **Axis:** c₃ / Q_β bar-odd swing / 1ppQ (5₂ chiral channel) ·
**Tier:** numerical scope-(a) structural finding · **Discipline:** no fit, no c_k
wired, nothing to production, no tier change.

## The question (owner)

Two linked owner prompts: *"are we doing na-Stokes where we should?"* and *"analogue
of resurgent for na-Stokes?"* — i.e. is the bar-odd resurgence being done with the
**non-abelian** (matrix) Stokes machinery the resurgence↔character-variety story
demands, and what is the non-abelian analogue of Écalle's resurgent apparatus?

## The dictionary — resurgence and its non-abelian analogue

Écalle's resurgence is the **abelian** theory. Its non-abelian analogue is the
**Stokes-matrix / Riemann–Hilbert** structure (Deligne–Malgrange–Mochizuki); on the
physics side, **Kontsevich–Soibelman wall-crossing**:

| Écalle (abelian / scalar) | Non-abelian analogue |
|---|---|
| Borel transform (scalar function on the ζ-plane) | flat sections + **Stokes filtration** of the connection |
| Stokes automorphism `exp(Σ Sω Δω)` | **Stokes matrices** `Sω` |
| scalar Stokes constant `Sω` | **off-diagonal Stokes-matrix entry** (= DT invariant) |
| alien derivative `Δω` | **KS wall-crossing operator** |
| Borel singularities = periods of `log y·dx/x` | those periods are the **diagonal** (formal monodromy); the Stokes data is **off-diagonal** |

## What the corpus already has (and where the gap is)

- **Non-abelian, extraction level — PRESENT.** `qbeta_5two_stokes_barodd_index_probe.py`
  implements the Garoufalidis–Gu–Mariño 5₂ **Stokes matrix** `S±(q)` (3×3, SL(3),
  inversion `S⁺ᵀS⁻ = 1`, `uploads/2007.10190v2.pdf`). Its bar-EVEN part is the scalar
  rotated 3d index `Ind^rot` (eq 124); its bar-ODD part is the full matrix
  `O = ½(S⁺ − S⁻)`. So we **are** doing na-Stokes at extraction.
- **Non-abelian, mass side — PRESENT but different.** The Yekutieli surface
  non-abelian Stokes (`𝓜∫∂Σ A = exp(𝓜∫∫_Σ F)`) is used for `linking_weight`/ρ_K
  (`2026-05-25-non-abelian-stokes-reading-a-exploration.md`) — categorical holonomy,
  not the resurgent Stokes matrix.
- **The gap — downstream scalar collapse.** The bar-odd carriers that feed c₃/Q_β —
  the scalar φ_odd (σ1/σ2 arg-sum), the 5₂ Habiro-tail action, the swing carriers —
  are all **scalar reductions** of `O`.

## Result — the datum is majority non-abelian

[`qbeta_5two_barodd_stokes_nonabelian_share_probe.py`](../../computations/probes/qbeta_5two_barodd_stokes_nonabelian_share_probe.py)
(4/4, reading the GGM producer's witness). Decompose `O` into its **diagonal**
(abelian / formal-monodromy — what a scalar can see) and **off-diagonal**
(non-abelian / Stokes) parts:

| quantity | value (muon anchor) |
|---|---|
| `‖O‖_F` | 2.107 |
| `‖diag O‖_F` (abelian) | 1.448 |
| `‖offdiag O‖_F` (non-abelian) | 1.530 |
| off/diag ratio | **1.057** |
| **non-abelian share** `‖offdiag‖²/‖O‖²` | **52.8%** |
| `‖O − Oᵀ‖_F` (non-normality) | 1.71 ≠ 0 |
| `trace(O)` (the one clean scalar) | −0.026 |

- **The off-diagonal dominates** — 52.8% of `‖O‖²`, more than the diagonal.
- **`O` is genuinely non-normal** (`‖O−Oᵀ‖ ≠ 0`): no basis diagonalizes it by scalars,
  so the datum is irreducibly matrix-valued.
- **Anchor-stable**: identical to 4 sig figs at the proton anchor.

## Conclusion

**A scalar reduction sees at most the diagonal — it discards the majority (52.8%) of
the bar-odd datum.** This is the structural diagnosis of why every scalar
closed-form search fails:

- φ_odd σ1/σ2 arg-sum → a single phase,
- the 5₂ Habiro-tail "no π²/5-analog" ([`2026-07-19-5two-habiro-tail-barodd-not-pi2-5.md`](2026-07-19-5two-habiro-tail-barodd-not-pi2-5.md)),
- the c₃ swing carriers,

are all scalar projections of an object 52.8% of which is off-diagonal and
scalar-invisible. The correct bar-odd carrier is the **matrix `O`** (or its
non-abelian invariants — off-diagonal entries / non-normal spectral data), not a
scalar phase.

**Honest scope.** This does **not** close c₃: the GGM probe already established `O` is
smooth in `q₀` (slope ~10², the swing needs ~3.8·10⁶ — SRigidityPrune binds), so `O`
is the *derived odd ingredient the capstone dresses*, not the swing. What this finding
does: it **reframes where the bar-odd datum lives** and gives a proved-structural
reason (majority off-diagonal + non-normal) that scalar routes cannot reach it — a
scope-(a) narrowing of the whole bar-odd front, not an ingredient exclusion.

## Next (concrete)

Feed the c₃/Q_β combiner the **matrix** `O` (or a non-abelian invariant that survives
the SRigidityPrune) instead of the scalar φ_odd — the first bar-odd probe to consume
the off-diagonal rather than project it away.

## Scope (anti-laundering)

Reads the GGM producer's witness; decomposes; reports the non-abelian share.
Does **not** manufacture a bar-odd value, does not close c₃. No fit; no c_k; no tier change.

## Cross-references

- GGM Stokes matrix producer: `qbeta_5two_stokes_barodd_index_probe.py` (bean `qou-ls2y`)
- 5₂ Habiro-tail scalar failure: [`2026-07-19-5two-habiro-tail-barodd-not-pi2-5.md`](2026-07-19-5two-habiro-tail-barodd-not-pi2-5.md)
- φ_odd is full-Z (scalar 1-loop + 2-loop both vanish): [`2026-07-18-5two-phi-odd-purely-2loop.md`](2026-07-18-5two-phi-odd-purely-2loop.md)
- Yekutieli surface non-abelian Stokes (mass side): [`2026-05-25-non-abelian-stokes-reading-a-exploration.md`](2026-05-25-non-abelian-stokes-reading-a-exploration.md)
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
