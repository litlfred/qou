# Δ_λ magnitude: the exchange-determinant family is machine-verified excluded

**Date:** 2026-07-18 · **Axis:** per-isotope binding magnitude
`ρ_A = B_strong(A)/B_strong(D)` · **Tier:** capstone / structural no-go
(scope-(b), three machine-verified Lean lemmas; nothing wired). Consolidates
the 2026-07-18 five-probe Δ_λ campaign.

## Statement

Let `G_A` be any exchange / Gram matrix on the `A`-nucleon complete
coordination graph `K_A` (diagonal `1`, off-diagonal bond `m` up to sign),
and let the binding cumulant be the connected free energy
`b_A = −ln det(I + m·G_A)`, with `ρ_A = b_A/b_2`. **No choice of sign
sector, parity symmetrization, or geometry makes `ρ_A` reach the
isospin-corrected strong targets.** The exchange-determinant cumulant
cannot supply the Δ_λ binding magnitude.

The strong targets (isospin-corrected via the merged Coulomb-mirror result
`docs/audits/2026-07-18-deltalambda-coulomb-mirror-split.md`, on the merged
`IsospinMirrorInvariance` premise): `ρ_strong(3) = B(³H)/B_D = 3.81` (³H is
Coulomb-free, so this is the pure strong ratio — not the naive symmetric
average 3.6), `ρ_strong(4) = (B(⁴He)+E_C(⁴He))/B_D = 13.03`.

## The three machine-verified obstructions (the pincer)

Each is sorry-free, `lean`-direct exit 0, and imported in `QOU.lean`.

| # | Lean lemma | Sector | What it excludes |
|---|-----------|--------|------------------|
| 1 | `QOU.MassTheory.isospinExchange_det_mirror_invariant` (`IsospinMirrorInvariance.lean`, PR #3986) | **signed** graph | The global p↔n mirror `s ↦ −s` fixes every isospin-signed bond, so the strong ³H/³He split is exactly 0. The signed graph gives magnitude but the *wrong* mirror — excluded from the strong (isospin-even) sector. |
| 2 | `QOU.MassTheory.saturation_rho_cap_three` / `saturation_rho_cap_four` (`SaturationRhoCap.lean`, PR #4004) | **unsigned** cumulant | Exact spectrum `{1+(A−1)m, (1−m)^{×(A−1)}}` ⇒ `ρ_A ≤ C(A,2)` for all `m∈[0,1]`. The targets `ρ(³He)≈13 > 6` and `ρ(³H)≈3.8 > 3` **exceed** the cap. The unsigned cumulant saturates but is capped below target. |
| 3 | `QOU.MassTheory.he4WritheDet_bar_even` (`B4CumulantBarEven.lean`, PR #4005) | **bar-even** symmetrization | The A=4 det `(1−5m²)(1−m²)` is even in `m`; the derived bond magnitude (`g_reeb`, `z_naive`) is already bar-even (40-digit). Bar-even symmetrization is a structural no-op — parity is not the missing ingredient. |

Together: the signed determinant is excluded from the strong sector (1),
the unsigned determinant is capped below target (2), and no
parity-symmetrization of either changes the picture (3). Every member of
the exchange-determinant-cumulant family is closed.

## The five probes that motivated it (2026-07-18)

| Probe | PR | Object | Outcome |
|-------|----|--------|---------|
| Per-pair Reeb magnitude | #3943 | additive per-pair `g_reeb` | honest-negative — residual collective |
| K₄ collective graph | #3952 | unsigned graph invariants | honest-negative — overshoot 2.6–10.6×, isospin-blind |
| Icosahedral √5 bridge | #3953 | Σ(2,3,5) S-matrix entry as `m` | honest-negative — over-splits mirror 2.42× |
| Coulomb-mirror reframe | #3990 | EM Coulomb split-off | **PARTIAL** — mirror split is parameter-free Coulomb; magnitude untouched |
| Saturation ceiling | #4004 | det-ceiling cumulant | honest-negative + **Lean cap (obstruction 2)** |
| Bar-even `b₄` | #4005 | parity-symmetrized cumulant | honest-negative + **Lean det-even (obstruction 3)** |

The Coulomb-mirror probe (#3990) is the one **positive** structural result:
it split the problem cleanly. The ³H/³He *mirror split* is pure-EM Coulomb
(parameter-free radius `m_π/A^{1/3}`, derived `α_EM`), leaving the
isospin-even **strong magnitude** as the sole remaining wall — the target
of obstructions 1–3.

## Why this is scope-(b), not scope-(a)

Per the "refuted / ruled out" discipline (AGENTS.md), a durable exclusion
requires a *proved invariant*. Here the invariants are the exact spectrum
`{1+(A−1)m, (1−m)^{×(A−1)}}` (obstruction 2, `ring`-factored and
`nlinarith`-closed), the entry-level mirror fixed-point
`(−sᵢ)(−sⱼ)=sᵢsⱼ` (obstruction 1), and the `m`-evenness of the A=4 det
(obstruction 3) — all machine-checked. This is a structural exclusion of
the *object class*, not a scope-(a) "these numbers missed" from a single
probe.

**Permanence caveat (not over-claimed).** This excludes the exchange-
determinant *cumulant* as the magnitude carrier. It does **not** exclude:
(i) a structurally different object (a graded dimension / jet-filtration
length is not a log-det and is not capped by `C(A,2)` — under active
attack); (ii) the determinant appearing as a *factor* inside a larger
closure (the proved per-bond pieces stand — "insufficient alone" ≠
"excluded"). What is closed is the specific hypothesis "ρ_A is a cumulant
of the K_A exchange determinant."

## Consequence / redirect

The Δ_λ magnitude must come from a **non-determinant** object. The lead
(post-campaign): a graded dimension / jet-filtration length (the
principal-grading jet order `n(λ)=min maj(SYT)` already carries the sign;
its filtration *length* is a candidate magnitude that escapes the
`C(A,2)` cap). This is the first object class not touched by the three
obstructions.

## Cross-references

- Lean obstructions: `IsospinMirrorInvariance.lean` (#3986),
  `SaturationRhoCap.lean` (#4004), `B4CumulantBarEven.lean` (#4005)
- Probes: #3943, #3952, #3953, #3990, #4004, #4005 (all `computations/deltalambda/`)
- Vector map: `docs/audits/2026-07-18-deltalambda-attack-vector-map.md`
- Coulomb split-off: `docs/audits/2026-07-18-deltalambda-coulomb-mirror-split.md`
- Gate status: `docs/coordination/option-e.md`;
  `docs/audits/2026-07-13-delta-lambda-gate-open-for-all.md`
