# λ_A-density refutation-artifact audit (bean x5az)

**Date:** 2026-06-24
**Bean:** `x5az` (child of milestone `4f2d` — λ_A excision)
**Hypothesis (owner, 2026-06-24):** "Lots of refutations of binding /
shell quadratic corrections [were reached] bc using the wrong density."
i.e. binding/Δ_λ closures refuted while baselining against the **global**
Family-A scalar λ_A (`vol_density_borromean` / `density_borromean`,
p=n-degenerate, ≈2.533) may be **artifacts** — the canonical density is
the **per-knot Hecke trace** `tr_M(K)` (`vol_density_per_block`), which is
p≠n-distinct (proton 1.0653, neutron 0.9232).

Ledger: [`docs/coordination/2026-06-24-lambda-a-fit-excised-per-knot-density.md`](../coordination/2026-06-24-lambda-a-fit-excised-per-knot-density.md).

## Step 1 — density census of binding/Δ_λ/refutation scripts

Which scripts consume the GLOBAL λ_A density vs the PER-KNOT density:

| Script | Density used | Refutation it backs | Re-examine? |
|---|---|---|---|
| `rho_k_h3a_co_casimir.py` | **global λ_A** | co-Casimir Δ_λ = 1/dim_q (#602, residual −2.30 MeV "wrong sign") | **YES — candidate** |
| `binding_color_vs_charge_tn3he.py` | **global λ_A** | color-vs-charge T/³He binding | YES |
| `probes/gap_a4_He3_residual_probe.py` | **global λ_A** | A=4 ³He residual | YES |
| `probes/gap_a4_L1_light_series_probe.py` | **global λ_A** | light-series L1 | YES |
| `probes/gap_a4_S_K_additive_probe.py` | **global λ_A** | S_K additive | YES |
| `probes/gap_a4_T2_per_knot_vol_probe.py` | **global λ_A** | per-knot Vol T2 | YES |
| `probes/gap_a4_T4_schur_weyl_icosahedral_probe.py` | **global λ_A** | Schur–Weyl icosahedral | YES |
| `binding_canonical.py` | per-knot | trace-canonical baseline | already per-knot ✓ |
| `binding_single_pipeline_comparison.py` | per-knot | single-pipeline forms | already per-knot ✓ |
| `probes/gap_a4_T3_mass_pochhammer_probe.py` | per-knot | T3 mass-pochhammer | already per-knot ✓ |

**7 refuted/probe scripts baseline on the global λ_A density** and are
artifact candidates; 3 already use the per-knot density (their verdicts
are not λ_A-artifacts).

## Step 2 — load-bearing check (in progress)

For `rho_k_h3a_co_casimir.py`: the global λ_A enters the **mass
normalization** `M_pred` against which the residual
`residual_MeV = M_D_MEV − M_pred` is measured (line 288); the residual
sign/magnitude is the refutation verdict. Whether swapping to the
per-knot density flips the −2.30 MeV "wrong sign" verdict requires the
actual re-run.

⚠ **Nuance (do not overclaim):** the binding formula proper,
`B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ`, uses **per-partition χ^λ**, not a single
density scalar — so "swap the density" is well-defined only where a
script uses `vol_density_*` for a mass/normalization baseline. Each
candidate must be checked individually; a global-λ_A *import* is
necessary but not sufficient for the verdict to be a density artifact.

## Step 2 verdicts (per-script re-examination)

| Script / refutation | λ_A load-bearing for the verdict? | Verdict |
|---|---|---|
| `rho_k_h3a_co_casimir.py` (co-Casimir Δ_λ=1/dim_q, #602) | **NO** | **NOT an artifact — refutation robust** |

### co-Casimir (#602) — robust, not a density artifact

Actual run (2026-06-24): `Σ y_λ χ^λ Δ_λ = +0.145` vs `target = −4.353`
→ **wrong sign**, ~30× too small (`rescaler = −30.03`); residual −2.30 MeV
(≈ −B_D). The refutation verdict lives in `Σ y_λ χ^λ Δ_λ`, which is built
from **per-partition Hecke data** (`y_λ`, `χ^λ`, `Δ_λ = 1/dim_q`) — all
q-deformation / partition objects, **independent of the mass density**.
The global λ_A enters only the *constituent* baseline `m_p+m_n` (and the
script already uses the measured-equivalent ≈1877.84, not the λ_A-inflated
1932). Swapping λ_A → per-knot `tr_M` shifts the mass baseline but does
**not** change the sign or 30× magnitude of the closure failure. So the
co-Casimir "wrong sign" verdict is **robust** to the density choice.

**Implication:** the owner's artifact hypothesis does **not** hold for the
co-Casimir Δ_λ refutation. It may still hold for scripts where the density
enters the *closure target* itself (the `gap_a4` probes) — those remain to
be checked individually.

### gap_a4 probe cluster + binding_color_vs_charge — λ_A-family-bound

Inspection (2026-06-24) shows these 6 candidates **build their density
ansätze on λ_A itself** (not on per-partition Hecke data like co-Casimir):

| Script | How λ_A enters | Verdict |
|---|---|---|
| `gap_a4_L1_light_series_probe.py` | L1a = `λ_A`; L1c = `λ_A·[3]_q^{2(Z-1)}·…` (per-atom density rule) | **λ_A-bound — refutation does NOT constrain per-knot density** |
| `gap_a4_He3_residual_probe.py` | tests `λ_A/2`, `(λ_A/[2]_q)^½` ansätze | **λ_A-bound — same** |
| `gap_a4_S_K_additive_probe.py` | `lw_q0 = λ_A` additive base | **λ_A-bound — same** |
| `gap_a4_T2_per_knot_vol_probe.py` | anchors on the `vol_density_borromean` (λ_A) convention | **λ_A-bound — same** |
| `gap_a4_T4_schur_weyl_icosahedral_probe.py` | *tries to derive* λ_A from a weighted A₄-irrep sum | **aimed at the fitted target** — deriving λ_A is deriving a fit |
| `binding_color_vs_charge_tn3he.py` | imports `base_lw = λ_A` as the density base | **λ_A-bound — same** |

**These differ fundamentally from co-Casimir.** co-Casimir's verdict is
in a density-independent per-partition sum (robust). These six instead
make λ_A *the density under test* — so each negative result rules out only
**λ_A-family** forms. The canonical **per-knot `tr_M(K)`** density was
never tried in any of them. Therefore:

- Their refutations do **NOT** refute the per-knot density (untested family).
- `gap_a4_T4`'s effort to *derive* λ_A is misdirected — λ_A is a fit, so
  there is no categorical object to recover; the right target is the
  per-knot density rule.

**This confirms the owner's hypothesis for the gap_a4 cluster** (6 scripts)
while honestly excluding co-Casimir. The productive redo is to re-run the
per-atom closure (L1/S_K/He3-residual) with `vol_density_per_block`
(per-knot `tr_M(K)`, p≠n-distinct) as the density base instead of λ_A.

## Summary verdict (7 candidates)

| Refutation | λ_A-artifact? |
|---|---|
| co-Casimir Δ_λ (#602) | **No** — density-independent, robust |
| gap_a4 L1 / He3 / S_K / T2 / T4 + color-vs-charge (6) | **Yes (family-bound)** — tested λ_A-forms only; per-knot density never tried |

Net: **6 of 7** re-examined refutations are λ_A-family-bound and do not
constrain the canonical per-knot density — they should not be cited as
ruling out the per-knot approach. The honest exception is co-Casimir.

## ⚠ Critical nuance — absolute mass vs binding (do not overclaim "per-knot is the fix")

Per-knot density is **not simply better**. For ABSOLUTE mass it is *worse*:

| density | m_p | m_n | abs-mass error |
|---|--:|--:|---|
| global λ_A (fit) | 966 | 967 | **+2.96%** |
| per-knot tr_M(K) (canonical) | 406 | 352 | **−57% / −62%** |
| round-trip target | 938.3 | 939.6 | (≈ρ 2.46) |

So neither density reproduces the absolute nucleon mass; the true density
sits ≈2.46 between them. **The per-knot fix's leverage is in BINDING, not
absolute mass.** Binding uses trace *ratios* `B = α·ln(tr_free/tr_atom)`
where the absolute density scale cancels, and there the **p≠n distinction**
(tr_M(p)=1.0653 vs tr_M(n)=0.9232) is real structure that the degenerate
global λ_A (one number for both) erases.

**Refined conclusion:** binding / shell quadratic-correction refutations
that baselined on the **p=n-degenerate λ_A** may have missed the per-knot
p≠n structure — that is the precise sense in which they may be artifacts.
This does **not** claim per-knot density rescues absolute masses (it does
not). The productive redo is binding/shell closures re-run with the
p≠n-distinct per-knot traces, not an absolute-mass re-pin.

## Next (under x5az)

1. Re-run `rho_k_h3a_co_casimir.py` with `vol_density_per_block` (per-knot
   `tr_M(D)`) substituted for `vol_density_borromean`; record whether the
   −2.30 MeV residual verdict changes. Honest reporting either way.
2. Repeat for the 6 other global-λ_A candidates.
3. Record per-script verdict (artifact / robust) in this table.

This audit does **not** yet claim any refutation is an artifact — it
localizes the 7 candidates and sets the re-run protocol.
