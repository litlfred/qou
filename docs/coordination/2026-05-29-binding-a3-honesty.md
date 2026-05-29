# A≥3 binding honesty — per-λ overclaim + shell review

**Created:** 2026-05-29
**Owner branch:** `claude/binding-log-scale-2026-05-28` → **PR #1417**
**Context:** Shell review ("shell is extractable in canonical braid-word
witness data; review paper on shells") surfaced that the per-λ Δ_λ
binding formula does **not** close the deuteron and a merged doc
overclaims closure via a fitted `C_knot`. Coordinated against the
in-flight binding-scale sibling so the two angles don't collide or
duplicate.

## Scope map

| PR | Branch | Angle | Relationship |
|----|--------|-------|--------------|
| **#1417** (mine) | `binding-log-scale-2026-05-28` | per-λ overclaim retraction + shell review + log-κ probe | — |
| **#1416** | `binding-habiro-dashboard-2026-05-28` | scalar binding-scale de-fit (E₀ probe, transfer-matrix unfold, dashboard) | **high overlap, complementary** |
| #1396 | `meson-tower-derivation-2026-05-28` | meson m_K/m_π is fitted (audit) | thematic only (same derived-vs-fitted rigor; different files) |

**No file overlap** between #1417 and #1416 (checked against #1416's 14
files). The per-λ files (gating doc, `deuteron-binding-interface-closure`,
`binding_energy_categorical_deuteron.py`) are mine; the scalar-scale files
(`shell_binding_transfer_matrix.py`, `binding-energy-scale-probe`,
`per_observable_100x_status.py`) are #1416's.

## Scope split posted on #1416
[comment](https://github.com/litlfred/qou/pull/1416#issuecomment-4575497037):
I take the per-λ overclaim correction; I will **not** duplicate #1416's
`shell_binding_transfer_matrix.py` / `binding-energy-scale-probe`. Offered
to fold #1417 into #1416 if a single de-fit PR is preferred (awaiting
response).

## Findings (this branch)

1. **Per-λ Δ_λ formula does NOT close binding.** Live 50 dps:
   `B = m_e·|Σ_λ y_λ·χ^λ·sgn·f^λ|` gives D −82.9 / T −77.5 / ³He −69.6 /
   ⁴He −89.3 %. The "Δ_λ CLOSURE ACHIEVED, zero free params" doc update
   (2026-05-26) is retracted; closure relied on `C_knot = 5.852 =
   B_AME/(m_e·|sum|)` — a fit.
2. **Shell is per-λ, not missing.** Recoverable from `atom-chi-rust-*`,
   `chi-lambda-he4-full-partition-table`, self-conjugate/magic labels,
   staircase λ_shell, torus-knot q^{2n_s} gap. The scalar Δtr / log-ratio
   collapses it.
3. **Two ~4 MeV scales close the deuteron only:** `m_e·Vol(𝓑₃)` (+0.19%,
   mine) and #1416's `E₀ = m_e/(q₀(q₀−1))` (+12%). Neither extends to A≥3.
   C_knot 5.85 (per-λ deficit) ≈ #1416's E₀/Q_β 5.34.

## Review comments addressed (#1417)
- Gemini HIGH (float64 `complex()` in `_real`): **accept-with-modification**
  (07efba0e2) — literal `mp.mpc(s)` ValueErrors on `a±bj`; used a
  float64-free real-part parse. Thread resolved.

## Update (2026-05-29 PM) — sibling state + derivation result

**Sibling state.** #1416 **confirmed the scope split** (keep separate, no
file overlap; my finding corroborates its de-fit). New overlapping siblings,
intent posted: **#1420** (meson 290 ppm → "EM is the lead"; ruled out
`R=1+4u²` as a fit, c=4.03≠4 — I heed this, won't wire it) and **#1421**
(low-mass sweep → D/T/³He census-knots = AME fit + "no derived atom→knot
rule" — same root cause as my `mass-volume-factorization` caveat). #1422
(q₀ re-pin −11.5 ppb) negligible for my %-level binding numbers.

**Derivation result (the open problem, advanced).** The A≥3 deficit is the
**linear truncation** `tr ~ exp(Vol)` ⇒ `Δtr` is the linearisation. The
extensive structure is the **complex-q / q-Reeb rotation** (per-rep:
rotation on (2,1), growth on outer). The **Markov-weighted q-Reeb phase**
closes the **A=3 mirror pair (³H, ³He) to 2% with no fit** (ρ≈18.5
MeV/rad); D (2-body) and ⁴He (doubly-magic + Coulomb=sinh channel) are the
special cases. Full write-up in
[`2026-05-28-binding-endomorphism-analogy.md`](../audits/2026-05-28-binding-endomorphism-analogy.md)
§"A≥3 derivation campaign".

## Next concrete task
- `/prepare-merge` #1417 in progress (rebased onto main, witness drift
  refreshed, docs added). Then reviews + merge per owner.
- Open lead (derive-or-refute, no fit): tighten the rotation-phase ρ by
  isolating the (2,1)-only Reeb phase and removing the ⁴He Coulomb (sinh)
  term; check whether D's 2-body case unifies. **#1416's scalar-scale lane
  is complementary — do not duplicate.**
