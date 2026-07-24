# Correction: the c₃ bar-odd "magnitude derived, only sign open" claim was WRONG — the substrate Borel sum is an anchor-blind floor, not S

**Date:** 2026-07-24 · **Corrects:**
[`2026-07-20-c3-barodd-fork-resolution.md`](2026-07-20-c3-barodd-fork-resolution.md)
§2, §4 · **Bean:** `qou-1dnr` (stays OPEN) · **Tier:** scope-(a) correction; no
fit, no c_k wired, no tier change · **Discipline:** owner-flagged
("what about the discussion which contradicts your premise?"); a durable
over-claim re-scoped to the honest state.

## The two errors

### E1 — `0.00945` is `‖ũ‖`, not `|S|_geom`

The 2026-07-20 audit read the substrate row of the
[`2026-07-18-dladder-fibre-branch-stokes-ambiguity`](2026-07-18-dladder-fibre-branch-stokes-ambiguity.md)
table as `|S|_geom = 0.00945`. That column is **‖ũ‖** — the expansion-variable
magnitude `|ũ_substrate| = |q·b·ℏ_q²| ≈ 0.00945`. It is **not** `|S|`.

A coincidence cluster of three unrelated ~0.0094 numbers caused the conflation:

| quantity | value | what it is |
|---|---|---|
| `‖ũ‖` | 0.00945 | expansion variable at substrate |
| Φ_b saddle deficit | 0.00940 | a geometric handle on the `|S|` scale (≈ \|S(muon)\|) |
| \|S(muon)\| | 0.00968 | one anchor value of the actual bar-odd part |

The **actual** `|S|` is **anchor-dependent**: `S(proton) = −0.03946`,
`S(muon) = +0.00968` (`qbeta-c3-hopf-cubic-residue.witness.json`). Therefore the
derived `|phase| = |S|/|(q;q)_3|` is **≈ 4.2 (proton) / 1.03 (muon)** — *not*
`1.0074`. The "0.74% resurgent correction" is spurious; the phase is not
near-unity, and `|(q;q)_3| = 0.00938` is **not** a 0.74%-accurate magnitude for
`S` (it is only within ~3% of the *muon* anchor and off by ~4× at the proton
anchor).

### E2 — the substrate Borel sum does NOT derive `c₃^odd` (magnitude included)

The 2026-07-20 audit §4 claimed the substrate `D(ũ)` is "Borel-summable to
`~10⁻³⁹`" so `S = h·Σ d_k ũ^k` is "computable to `~10⁻³⁹` — a derivation." This
contradicts a **pre-existing** witness the audit failed to account for,
`qbeta-dladder-ecalle-phib-resummation.witness.json` (from #3818/#3839):

- **M4:** the forward optimal-truncation resummed `D(ũ) ≈ −0.01667` at the
  meridian is **anchor-blind** to ~9 digits, and `h·D ≈ −0.0035` reproduces
  **neither** `S(muon)=+0.0097` **nor** `S(proton)=−0.0395`.
- **M4b:** the substrate `ũ ≈ 0.0095` puts optimal truncation at `k* ~ 10¹³`, so
  the Stokes jump `exp(−ρ/ũ) ~ 10⁻⁷…10⁻²⁷` is **far too small** to be the
  `O(0.01)` anchor-dependent `S`. On the substrate branch the swing is **not** a
  Stokes ambiguity of this ladder.

The `10⁻³⁹` figure was the least-term **δ_np ambiguity** at the k=31 edge (the
*resolution floor* of a 21-term ladder), which I mis-stated as the precision of a
derived value of `S`. It is not: the resummed floor `h·D_opt ≈ −0.0035` is a
small anchor-blind number that is not `S` at all.

## Corrected open state

`c₃^odd`'s dominant, anchor-dependent part is **not derived — neither magnitude
nor sign**. Two candidate mechanisms remain, neither settled:

- **(a)** the `1/ũ³` `c₃`-representational amplification (#3636): the ladder
  inversion `Q_β = ∏(1+c_k u^k)` amplifies tiny `D`-residuals into the dominant
  `c₃` rung; the substrate swing lives here, not in a ladder Stokes jump; or
- **(b)** the **fibre-saddle** (`|q|=1`, `ũ~O(1)`) Stokes datum `A_ω` (#3805 /
  G3 monodromy), where the jump is unsuppressed.

The prior "division of labour" (`#4140` owns a derived magnitude, `#3805` owns
the sign) is **withdrawn**: the magnitude is not derived either. This is
consistent with the **2c-2 bar-pair obstruction** confirmed at block level on
main (`ecdadf24`) and named as frontier #4 in #4146 — the fibre-level bar-odd
resummation is genuinely obstructed, not merely sign-ambiguous.

## What still stands

- The `d_k ∈ ℚ(√3)` are **categorically derived** from the symbolic GB-reduced net
  decay-width (determined triangular solve, no CODATA fit) — unaffected.
- Lean `QOU.Mass.QbetaC3PochhammerPhase` is a **conditional** proof
  (`IF |S| = |(q;q)_3| THEN phase = ±1`) — sound. The error was **asserting its
  antecedent numerically**; the antecedent is false (the phase is not ±1).
- `S = h·D(ũ)` (KC21) is a formal identity; the point is that the *perturbative*
  resummation of that divergent `D` at the substrate captures only the anchor-blind
  floor, not the observable `S`.

L2 count unchanged (2/7). c₃ stays EMPIRICAL, open in magnitude and sign.
