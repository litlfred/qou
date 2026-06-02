# α_EM multi-cell Yekutieli + substrate Coulomb channel — 2026-06-02

Branch: `claude/yekutieli-multicell-and-coulomb-channel-2026-06-02`

Per author 2026-06-02: revisit deriving α_EM (the fine-structure
constant) from the canonical chain `categorical action → non-abelian
Stokes → Wedderburn`, via two specific routes the author flagged as
"I thought we did this":

  1. **Multi-cell summed Yekutieli** — non-abelian Stokes integral
     SUMMED over the 8-ideal-octahedron tessellation (prior probes
     used individual torus knots or per-cell, never the explicit sum)
  2. **Substrate Coulomb channel** — the sinh (Coulomb) channel of
     `prop:cosh-sinh-q-bridge` projected through Wedderburn

## Target structure (the genuinely-open pieces)

```
α_EM⁻¹ = q·[9]_q·[10]_q   +  2/(3π)        +  [2]_q/(8π)·(1−h²α)  + O(α³)
         ↑ tree (Coulomb-     ↑ shift          ↑ 2-loop self-energy
           channel sinh)        (4.3 ppm)        (0.31 ppb residual)
       ≈ 136.8232089       = +0.2122066     = +0.0005837
```

(Values are rounded for display. The tree term to full precision is
`136.82320885358…`; tree + shift + self-energy = `137.03599912695…`,
vs CODATA `137.035999084`, a residual of `+0.31 ppb` — the rounded
display sum `≈ 137.0359932` undershoots only because each term is
truncated to 7 figures. `h ≔ q − q⁻¹` is the Hecke crossing scale and
`h² ≈ 0.0437` at q₀; `α ≔ α_EM`.)

- **Tree term** `q·[9]_q·[10]_q` ≈ 136.8232089 — ALREADY a
  Coulomb-channel (sinh = `[n]_q`) form per `prop:cosh-sinh-q-bridge`.
  This part is the existing `prop:em-coupling-bring-zero-mode`.
- **Shift** `2/(3π)` — believed to be Bring-surface Hodge / cohomology
  data (audit `em-coupling-bring-zero-mode.md`). The "3" candidate:
  N_cusps = 3 (Borromean is a 3-component link).
- **Self-energy** `[2]_q/(8π)·(1−h²α)` — the RT-2-loop EMPIRICAL target
  (PRs #1463/#1487/#1527/#1538/#1549). The "8" candidate: 8 ideal
  octahedra in the 𝓑_3 tessellation.

## Prior art (refuted / null)

| Probe | Verdict |
|---|---|
| `alpha_em_yekutieli_h2_extraction.py` (torus-knot product) | REFUTED — `q·tr_M(T(2,9))·tr_M(T(3,5))` = 0.8, not 137 |
| PR #1466 H_3 matter-insertion + Wedderburn | REFUTED −445% |
| PR #1471 Bring-surface integration | REFUTED −67% |
| sibling `yekutieli-A q-Lambert per-cell` | NULL |

These tried INDIVIDUAL cells / torus knots. The SUMMED multi-cell
form + the Coulomb-channel route are the two not-yet-cleanly-tested
variants.

## Status

| Item | Tier | Status |
|---|---|---|
| 1. Multi-cell summed Yekutieli (α_EM shift) | REFUTED | genuine hyperbolic-volume sums miss 2/(3π) by 12–126%; only tautological rewrites hit |
| 2. Substrate Coulomb channel (α_EM) | PARTIAL | cosh/sinh bridge verified; tree + [2]_q-numerator ARE Coulomb-channel; 2/(3π) coeff + (1−h²α) NOT independently derived |

## Findings

**Item 1 (multi-cell summed Yekutieli) — REFUTED for genuine forms.**
`probes/alpha_em_multicell_yekutieli_probe.py`: the only summed-cell forms
that hit 2/(3π) are tautological rewrites (`2/(N_cusps·π)` with
N_cusps=3; `Σ_3·(2/9π)`; and `2·V_oct/(Vol_𝓑·π)·(2/3)` where
`V_oct/Vol_𝓑 = 1/2` cancels exactly — all ASSUME the answer). Genuine
hyperbolic-volume sums miss: best `V_oct/(2π²)` at −12.5%, then
`Vol_𝓑/(N_cusps²·π)` at +22%. The N_cusps=3 reading of the "3" is a
plausible INTERPRETATION but the coefficient "2" and the 1/π are not
derived. Consistent with the prior individual-cell refutations.

**Item 2 (substrate Coulomb channel) — PARTIAL / interpretive.**
`probes/alpha_em_coulomb_channel_probe.py`: the cosh/sinh bridge
`[n]_q = sinh(nλ)/sinh(λ)` is verified to 1e-40. The tree term IS a
pure Coulomb-channel (sinh) object, and the self-energy's `[2]_q`
numerator IS `sinh(2λ)/sinh(λ)`. BUT:
- The `2/(3π)` shift coincides with the STANDARD QED 1-loop
  vacuum-polarization β-function coefficient (textbook, not a new
  categorical derivation). Genuine λ-forms bracket it: `tanh(λ)/(πλ)·(2/3)`
  at −0.36%, `(2/3π)·cosh(λ)` at +0.54% — suggesting `2/(3π)` is the
  λ→0 limit, but no clean closed form.
- The `(1−h²α)` Schwinger factor is NOT a pure Coulomb-channel object
  (cosh⁻² damping misses by 1%); it is the RT-2-loop track's target.

**Net:** the canonical chain `cat action → sinh (Coulomb) channel →
Wedderburn` structurally produces the α_EM⁻¹ TREE term and the
self-energy `[2]_q` numerator, and gives a consistent N_blocks=3
reading of the shift's denominator — but does NOT independently
derive the `2/(3π)` coefficient (QED-vacpol import) or the `(1−h²α)`
Schwinger factor (RT-2-loop target). This sharpens, but does not
close, the α_EM derivation.

## Anti-pattern guards (per scaffolding audit 2026-06-01)

- ❌ NO fitted formula matching 2/(3π) or the self-energy numerically
  without a structural mechanism (8th-ansatz trap)
- ❌ Do NOT assume the 8 octahedra contribute equally — Borel descent
  may group them into unequal orbits
- ✓ DO report derive-or-refute honestly with a pre-stated failure sig

## Cross-references

- merged PR #1442 (m_K/m_π Bring-zero-mode closure — Coulomb-channel template)
- merged PR #1581 (m_p (α_EM/π)/dim H_3)
- `prop:em-coupling-bring-zero-mode`, `prop:cosh-sinh-q-bridge`
- audit `2026-06-01-yekutieli-mp-substrate-derivation-scaffolding.md`
- `alpha_em_yekutieli_h2_extraction.py` (prior torus-knot refutation)
