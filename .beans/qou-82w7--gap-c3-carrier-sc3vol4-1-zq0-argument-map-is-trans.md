---
# qou-82w7
title: 'GAP: c3 carrier S=c3+Vol(4_1) — z(q0) argument map is transcendental, not combinatorial'
status: todo
type: task
created_at: 2026-08-01T01:23:31Z
updated_at: 2026-08-01T01:23:31Z
---


## Status (2026-08-01)

The tetraplectic → combinatorics **structural** reduction of the c₃ Faddeev
integral is DONE and sorry-free (`QOU/QBeta/EkParitySplit.lean`; probe
`computations/qbeta/qbeta_c3_barodd_tetraplectic_reduction_probe.py`). The exact
coefficient closed form is now also pinned: `e_k(q,q³,…) = q^{k²}/(q²;q²)_k`
(Lean backbone `QOU/QBeta/TetraplecticProductRecurrence.lean`; witness
`computations/qbeta/qbeta_ek_qpochhammer_closed_form.witness.json`, k≤6).

**What remains OPEN is NOT combinatorial.** Reproducing the c₃ carrier
`S = c₃ + Vol(4₁)` (muon S=+0.00968, proton S=−0.03946, sign flip, ratio ≈ −4.08)
requires the **argument map z(q₀)** = meridian holonomy m(q₀) that feeds the
combinatorial e_k. Audit `docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md`
proved this link is **near-singular** (`dc₃/dq ≈ 4.7×10⁶`) and a **smooth
deformation is excluded** (predicts ratio ≈ 1.0 vs measured −4.08) — it is a
transcendental root-of-unity accumulation (PR #3458's z→c_k evaluation map), not a
combinatorial/algebraic object. Do NOT attempt to close S via the reduction; the
reduction supplies the *coefficients*, not the *argument*.

> **Wording ground-check (2026-08-15, qou-ppjy, per the qou-arvu sweep).** What
> is *measured* here is the near-singularity (`dc₃/dq ≈ 4.7×10⁶`) and the
> smooth-route exclusion (ratio −4.08 vs ≈1.0) — both stand. The word
> "transcendental" is an *interpretation* of those measurements (the
> root-of-unity-accumulation picture), not a proved classification: a
> near-singular, non-smooth map could in principle still be algebraic with a
> nearby branch point. This is NOT the withdrawn "non-holonomic ⇒ resurgent"
> inference (2026-08-09, D-ladder — that concerned divergence of `D(ũ)`,
> which proved convergent), but it rhymes with it; treat "transcendental" as
> a working hypothesis, not a constraint that prunes algebraic candidates.

> **Premise requalification (2026-08-15, per the O2 negative, PR #5041).**
> The individual `S` targets quoted above carry a ±1.262 CAL-3 propagated
> uncertainty (130×/32× the central values); the canonical witness says the
> sign flip "must not be cited as an established sign flip". The only
> resolved observable is the swing `S(muon) − S(proton) = 0.04914`
> (±7.6×10⁻⁷) = the cross-anchor `c₃` variation (`Vol(4₁)` cancels). Read
> this bean's "sign flip", "ratio ≈ −4.08", and the anchor inversion targets
> as **conditional on a flip the data does not establish**. The swing is the
> one *resolved* number but is NOT an independent target: `qou-6y1p`
> (scrapped) showed it equals the 11.54 ppb μ–p substrate tension × dc₃/dq
> exactly — the known tension amplified by the circular cal-anchored c₃
> extraction — so deriving it requires both a first-principles c₃ (ladder
> coefficient ≡ 0) and the open μ–p tension. See
> `docs/audits/2026-08-14-aomega-to-S-bridge-refuted-O2-negative.md`.

## Update (2026-08-01, PRs #4452 + #4457 merged)

The candidate space for the argument map is further narrowed **by proof**:

- **Real-seed class excluded, scope-(b)** (`QOU/QBeta/NewtonRealityInvariance.lean`,
  sorry-free): real Newton seeds of EITHER sign have all-real iterates and can
  never converge to the cusp `e^{iπ/3}`. Covers the literal Φ_q-pole seed and
  its negative.
- **Pole-sign principal-branch family excluded, scope-(a)**
  (`computations/qbeta/qbeta_c3_pole_sign_complexification_probe.py`, 4/4):
  `u_k = iπ − (2k+1)log q₀` is anchor-blind for every k (sign boundary
  `(2k+1) = π/log q₀ ≈ 30.109` crossed by no odd integer between anchors).
  Near-k=15 magnitude dip is a flagged numerological trap — do not chase it.
- **Surviving constraint composition** (audit
  `docs/audits/2026-08-01-qbeta-c3-pole-sign-reality-exclusion.md`): the phase
  is strictly interior, `0 < |arg m²| < π`, and must cross the diagonal
  `|Re u| = |Im u|` at the root-found `q*_S` (the S-zero point ≈ 1.10998 — NOT
  the KC22 radius zero `q*_ρ ≈ 1.48989`; subscripts per the qou-kp9f glyph
  rule) with the anchor inversion targets
  `(Re²u−Im²u) = +0.0224` (muon) / `−0.0911` (proton). Geometric backbone:
  `docs/scope/2026-08-01-reeb-tetraplectic-cs-threeform-identification.md`
  (Reeb ⌟ tetraplectic → CS face).

## Attack options (2026-08-15 ledger, session qou-gylf follow-up)

- **A1 — complex fibre-seeded Newton** [derivation route; medium; corpus-grep
  first]. Every pole-seed probe used a REAL seed (either sign — both now
  excluded). Derive the seed's PHASE from the root-of-unity accumulation
  itself: the Habiro/Ohtsuki expansion at the nearest ζ_N to q₀ (N from the
  [N]_q = 0 truncation) supplies a derived complex object with no free
  parameter. Gate with A3, honoring the conditional-flip premise.
- **A2 — modular-involution prune** [formalize-first; small]. Lean-constrain
  arg u(q₀) from Φ_b = Φ_{1/b} self-duality (transpose symmetry) before any
  scan; even a weak constraint (e.g. sign or sector of arg u) shrinks A1's
  target space by proof.
- **A3 — swing-difference gate** [gate upgrade; small]. Replace the
  conditional two-sided gate with the RESOLVED constraint
  κ·[(Re²u−Im²u)_μ − (Re²u−Im²u)_p] = 0.04914 ± 7.6e-7 as the primary
  candidate-map filter; the conditional signs become secondary. Uses only
  the resolved observable, so it survives the O2 requalification.
- **A4 — coordinate on W2** [zero-cost]. The theta-valued Birkhoff
  connection-matrix computation (W2 lineage, qou-vkg5) may output the phase
  as connection data; watch that front, do not duplicate it.

## 2026-08-19 Arc review — two premises moved under this bean (both verified here)

**1. "Q_β is the bar-odd sinh partner" is MEASURED FALSE at the level of the
object the framework computes** (`b848d0a12`, sibling `qou-cds1`; I re-read the
commit rather than take the survey's word). For `Q_A = m_e|q²−2q−1|(q+1)/2q³`,
at 40 dps both anchors:

    Q_A/m_e at q = 1.5335566273012 ; at 1/q = 2.5868438911015
    bar(Q_A)/Q_A = 1.686826456258      (bar-odd needs −1; bar-even +1)

Neither, and not marginally. The commit names four corpus sites carrying the
contradicted sentence — **including AGENTS.md's c_k banner**. Scope: this does
NOT refute a bar-odd closed form for c₃; it removes the *premise* that the
computed Q_β supplies one. **This bean may no longer cite "Q_β is bar-odd" as
given.** Correction of the sites is `qou-cds1`'s to land (they enumerated them);
do not duplicate.

Compounding it: registry §9h Correction 2 — the ε-parity is convention-immune
(470× reframing verified) but is **not** evidence for bar-oddness; the chain is
Schwarz reflection, and bar-EVEN Q_A has the identical ε-parity.

**2. The anchor-dependence is in the BRIDGE, and the bridge changes sign**
(`2b9a89d96`, sibling `qou-qiw9`; verified). With `S = h·D(ũ)` as KC21's
schematic identity, both evaluations already committed:

    carrier h·D   −0.003486062405593 / −0.0034860636358261   rel. var 3.53e-7
    empirical S   −0.0394593643      / +0.009682977798       rel. var 1.245
    B := S/(h·D)  +11.319            / −2.778                SIGN CHANGE

The ladder is anchor-blind at 1e-7 while S swings by 1.245. **Any route that
explains the swing FROM the ladder is looking where the signal provably is
not** — and no positive rescaling, normalisation, or scalar convention of the
carrier reaches S at both anchors, because the factor changes sign.

**Convergence with this Arc's own E1/E1b result (recorded because the two
fronts arrived at the same shape independently).** E1 refuted the linear bridge
`u = c·b` at order b⁴; E1b refuted the 2-term odd bridge at b⁶ with zero free
parameters. That is the Ohtsuki-quantum ↔ NZ-geometric bridge; `qou-qiw9`'s is
the ladder-carrier ↔ empirical-S bridge. Different bridges — but the same
finding twice: **a hoped-for simple relation between a well-behaved
fibre-level object and an anchor-dependent observable fails structurally, not
by a small factor.** Both point at the fibre→observable functor content as the
locus, consistent with the standing Im(q) fibre-vs-observable framing. Neither
is evidence for the other; they are independent instances of one shape.

**Ownership**: `qou-qiw9` (sibling, todo, 08-19) now owns the bridge question
and overlaps this bean directly. Coordinate before any bridge-side probe here.
