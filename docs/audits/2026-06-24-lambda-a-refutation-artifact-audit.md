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

## Probe / consumer triage (bean 0voz — "fix research probes")

20 scripts call the deprecated `vol_density_borromean` / `mass_vol_density`.
**Immediate guard (live):** both now emit `DeprecationWarning` → no probe can
*silently* use the wrong density. Per-script disposition:

| Disposition | Scripts | Action |
|---|---|---|
| **Migrate** (production absolute mass) | `mass_table_comprehensive` ✅ done (→ facade) | route to `canonical_mass` |
| **Keep + warn** (subject IS the density / a study) | `vol_density_borromean_h4_probe`, `vol_density_borromean_q_locality_probe`, `option_a_vol_per_knot_light_series`, `gap_a4_{L1,S_K,T2}`, `bring_color_weighted_base_scale_probe`, `casimir_hoefsmit_additivity_probe`, `vol_density_per_block_wiring`, `per_knot_mass_table_demonstration`, `volume_def_reconcile`, `m_p_borromean_verification_50dps` (verifies the Borromean route) | warning is correct — they knowingly use the fit |
| **Keep + warn** (binding/energy scale, not abs nucleon mass) | `entanglement_emitted_energy`, `gamma_gamma_pair_production_decomposition`, `multi_layer_gap_decomposition`, `m_qclt_approx`, `meson_vol_density` (meson, different particle) | scale cancels / different observable |
| **Superseded** (old route, non-production) | `build_proton_mass_50dps_chain` (Borromean→965; imported only by `witness_reproducibility_check`) | leave with warning; supersede when convenient |

**Conclusion:** the only genuine production absolute-mass bad usage was
`mass_table_comprehensive` (fixed). The rest are research probes whose
subject is the density (warning is the right signal) or non-mass/binding
uses. No blind migration — that would break the studies. The Deprecation
warnings are the durable "don't continue to use wrong" guard.

## Next (under x5az)

1. Re-run `rho_k_h3a_co_casimir.py` with `vol_density_per_block` (per-knot
   `tr_M(D)`) substituted for `vol_density_borromean`; record whether the
   −2.30 MeV residual verdict changes. Honest reporting either way.
2. Repeat for the 6 other global-λ_A candidates.
3. Record per-script verdict (artifact / robust) in this table.

This audit does **not** yet claim any refutation is an artifact — it
localizes the 7 candidates and sets the re-run protocol.

## Per-knot re-run results (2026-07-02/03, bean 3xbo — protocol executed)

All 7 candidates re-run with the canonical per-knot `tr_M(K)` base
(`vol_density_per_block`, chi-cache traces, p≠n-distinct) substituted for
λ_A. Rerun scripts + witnesses in `computations/probes/*_perknot_rerun.py`
/ `*-perknot-rerun.witness.json` (all EXPLORATORY, `production_wired:
false`, no new fitted constants; every negative scoped (a)).

| # | Refutation | Per-knot verdict | Key numbers |
|---|---|---|---|
| 1 | co-Casimir Δ_λ = 1/dim_q (#602) | **ROBUST** | density-independent sum +0.14496 unchanged; failure ≥30× under every base (CODATA −30×, λ_A −763×, per-knot +15081×) |
| 2 | color-vs-charge T/³He | **ROBUST** — and the Step-2 "λ_A-bound" classification was overcautious: λ_A enters only as a normalization that **cancels algebraically**; the split is base-independent to 30 dps | split −0.0343 MeV = −4.5 % of needed, any base; T−³He stays CHARGE/Coulomb |
| 3 | L1 light-series multiplicative λ(K) (#1874) | **ROBUST** | per-knot forms fail *harder* on every atom (per-knot density shrinks with A while λ_emp grows); constrains L1a/L1c multiplicative family on both bases |
| 4 | ³He residual λ_A/2 near-match (#1882) | **ROBUST** — λ_A/2 (+3.65 %) confirmed λ_A-family numerology | per-knot analogues do worse than the λ_A-family best. Honest lead: bare p≠n product tr_M(p)²·tr_M(n) lands within 25 % of the residual target with **no** rescaler |
| 5 | additive S(K) (#1876) | **PARTIALLY ARTIFACT** — the refutation's core evidence (S_emp sign-flip across the series) **disappears** on the per-knot base | λ_A base: sign-flip reproduced (refutation stands there). Per-knot base: S_emp > 0 for all six atoms; S/(A·m_e) uniform to ×1.73 (vs unbounded). Caveat: additive term no longer sub-leading (max \|S/m(K)\| = 99 %), so "small correction" framing dies; the live object is a per-knot-base additive family, re-scoped |
| 6 | T2 Vol-convention (#1891) | **ROBUST** | ratio swings persist under all three Vol conventions (2610–7545 %) with the per-knot base |
| 7 | T4 Schur–Weyl derive-λ_A | **ROBUST** (retargeted) | 0/140 parameter-free aggregates MATCH (<0.5 %) tr_M(p/n) or ρ_rt; single NEAR (2.8 % on ρ_rt(n)) is look-elsewhere noise |

**Net verdict on the owner's artifact hypothesis: 1 of 7 confirmed, and
it is the informative one.** The additive-S(K) family's sign-flip was a
λ_A artifact — the p≠n-distinct canonical base is strictly more regular
there — exactly the family the GAP-A-4 scoping note
(`docs/scope/2026-07-02-gap-a4-perknot-density-rule-scoping.md` §4 step 1)
flagged as the most plausible flip. The re-scoped per-knot additive
S(K) family (no longer "small correction"; S is order-of-mass at A ≥ 2)
is the priority numerical thread, gated by the scoping note's I-6
(trace-convention pin) and I-1/I-3 invariants before any scan. The
other six refutations extend to the per-knot base, all scope (a).
