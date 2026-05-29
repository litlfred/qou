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

## Next concrete (non-overlapping) task
- Await #1416 / owner decision on fold-vs-sibling.
- The genuine open problem (Δ_λ gate / A≥3 per-λ + inter-shell scale) is
  **#1416's scalar-scale lane** — do not duplicate. If asked to push the
  per-λ angle further: the honest direction is whether the torus-knot
  inter-shell q^{2n_s} gap (per-λ, derived) supplies the A-dependence —
  derive-or-refute, **no AME fitting** (CLAUDE.md Δ_λ gate: no 7th ansatz).
