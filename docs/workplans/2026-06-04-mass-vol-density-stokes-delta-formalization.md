# Formalization roadmap — Mass = Vol × Density, δ from non-abelian Stokes

**Goal (owner directive, 2026-06-04).** Replace the `VolDensity(K,q₀)`
black box with a chain of *proper definitions*: derive the nucleon mass as
**Volume × Hecke-energy-density**, and derive the flavor split **δ** as the
**curvature of the categorical connection integrated over the p-n
interface** (Yekutieli non-abelian Stokes), rather than positing it.

If the chain closes, `VolDensity` becomes a *theorem* (P1∘P2) and δ becomes
a *theorem* (P3⇒P4), eliminating both the Geom black box and the
color-weighted-vs-blind convention ambiguity (the weighting is then forced
by the curvature, not chosen).

> **Discipline.** Statements first: write each Lean `def`/`theorem`
> signature with `sorry` (+ `-- Ref:`) before any proof. Where a step is a
> genuine conjecture, axiomatize it as a `class` per AGENTS.md §3b-cond and
> carry it as an explicit `[Instance]` hypothesis downstream — so the
> chain's logical status is auditable (what's proved vs what's assumed).
> NO step may close numerically against Δm_np / CODATA (that is a fit, not
> a derivation — three-calibration discipline).

## The proposition DAG

```
  q₀ (substrate)
    │
    ├─ P1  Mass = Vol × Density           m(K) = m_e · Vol(K) · ρ(q)/ℏ_q²
    │        ├─ Vol(K)  : hyperbolic volume of S³∖K  (Vol(𝓑₃)=8G)
    │        └─ ρ(q)    : energy density  ──────────────┐
    │                                                   │
    ├─ P2  Density = Hecke energy on partitions         │
    │        ρ(q) = Σ_{λ⊢n} y_λ(q)·χ^λ(β_K)  = (3q²+4+3q⁻²)/4 for 𝓑₃
    │        (Markov trace over Wedderburn blocks)      │
    │                                                   │
    ├─ P3  Non-abelian Stokes at the p-n interface  ◄───┘
    │        holonomy f_pn = ½(σ+σ⁻¹) − (h/4)·∮F   [F = categorical curvature 2-form]
    │        the −(h/4)∮F term is the interface curvature defect = the split
    │
    ├─ P4  δ from the curvature integral
    │        ∮_{interface} F  =  δ(q) = (q−1)²(1−q⁻⁴)/3 · (1+ℏ_q³)
    │        structure:  (q−1)²=ℏ²q² [area 2-form] · (1−q⁻⁴)/3 [interface q-number / 3 colors] · (1+ℏ³) [3-loop]
    │
    └─ P5  Flavor split assignment
             m_p = m_avg·(1 − δ/2),   m_n = m_avg·(1 + δ/2),   m_avg = m_e·Geom(𝓑₃)
```

## Statement-by-statement Lean plan

| # | Lean declaration (planned) | Kind | Status target |
|---|----------------------------|------|---------------|
(Lean-robust forms: negative powers as `q ^ (-2 : ℤ)` / `q ^ (-4 : ℤ)`,
not unicode superscripts, so the rows paste straight into `def`/`theorem`
stubs.)

| P1 | `QOU.Mass.mass_eq_vol_times_density : m K = m_e * vol K * density q / ℏ_q q ^ 2` | theorem | proved from defs once `VolDensity` is reassembled, else `sorry` |
| P2 | `QOU.Mass.density_eq_markov_trace : density q = ∑ λ, yWeight q λ * heckeChar q λ (braid K)` | theorem | proved (Wedderburn decomposition) or conditional on existing `tr_M` lemma |
| P2′| `QOU.Mass.density_borromean : density q = (3 * q ^ 2 + 4 + 3 * q ^ (-2 : ℤ)) / 4` | theorem | concrete eval of P2 at 𝓑₃ |
| P3 | `class NonabelianStokesInterface` with field `holonomy = ½(σ+σ⁻¹) − (h/4)·curvatureIntegral` | class (conj) | axiomatized — the categorical-curvature input |
| P4 | `QOU.Flavor.curvature_integral_eq_delta [NonabelianStokesInterface] : curvatureIntegral q = δ q` | theorem (conditional) | proved *from* the class, modulo P3 |
| P4′| `QOU.Flavor.delta_def : δ q = (q - 1) ^ 2 * (1 - q ^ (-4 : ℤ)) / 3 * (1 + ℏ_q q ^ 3)` | def | (likely already exists — see audit) |
| P5 | `QOU.Flavor.proton_neutron_split : m_p = m_avg*(1-δ/2) ∧ m_n = m_avg*(1+δ/2)` | theorem | (likely already exists in FlavorDressing) |

## Open question the build will answer

Is the −(h/4)·∮F holonomy term (P3) a **theorem** of an existing categorical
connection, or does the repo lack the connection/curvature machinery
(greenfield)? If greenfield, P3 stays a `class` (named conjecture) and P4
is *conditional* — a rigorous "δ = (q−1)²(1−q⁻⁴)/3·(1+ℏ³) **given** the
Stokes holonomy form", which is already a real result (it pins the
curvature integral's value). The honest first milestone is the conditional
chain P1∧P2∧P2′ (proved) + P4 conditional-on-P3-class.

## Non-goals (this tranche)
- No numerical fitting of δ. No CODATA/Δm_np tuning.
- Not regenerating the stale color-blind tr_M witnesses (separate; tracked
  in `2026-06-04-peel-exact-nuclei-color-weighted-trm-convention.md`).
- Not dropping `VolDensity` from production until P1∘P2 is proved sorry-free.
