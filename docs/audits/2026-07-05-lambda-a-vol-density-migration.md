# λ_A / vol_density migration audit — call-site inventory + classification

**Date:** 2026-07-05
**Branch:** `claude/lambda-a-vol-density-migration-2026-07-05`
**Beans:** 0voz (migrate scripts off `vol_density_borromean`), 6xug
(`vol_density` → per-knot density), zeu7 (session: λ_A excision).
**Guardrail read first:** [`docs/canonical-mass-formula-guardrail.md`](../canonical-mass-formula-guardrail.md)
(owner ruling 2026-06-24).

## TL;DR (headline finding)

**The absolute-mass migration off `vol_density_borromean` is already
substantially complete.** Every remaining *call site* (function
invocation) of the deprecated `vol_density_borromean` in `computations/`
is one of:

1. a script that **already routes absolute mass through the
   `canonical_mass` facade** and retains the Borromean value only as a
   *warning-suppressed audit column* (`build_proton_mass_50dps_chain.py`
   — the exemplar), or
2. a **research / audit / probe** that intentionally *studies the λ_A
   fit itself* — explicitly **allowed** by guardrail §3 ("Studying λ_A
   itself (a research probe)? → allowed, but it is a fit … label it
   so"), or
3. **inside the deprecated modules themselves**
   (`_li_2_q_util.py`, `mass_vol_density.py`).

There is **no surviving un-migrated absolute-mass production consumer**
of `vol_density_borromean`, and **zero external callers** of the
deprecated `mass_vol_density()` function.

## Two framing corrections (important)

1. **The "~64 scripts" figure is an overcount.** The grep for
   `vol_density_borromean|mass_vol_density|linking_weight_family_a`
   matches 67 files, but the large majority are **docstring / comment
   mentions**, `*.witness.json` / `*.script-qa.json` sidecars (out of
   scope for `.py` migration), and — crucially — uses of
   **`linking_weight_family_a`, which is NOT deprecated** (see below).
   The genuine *call sites* of the deprecated `vol_density_borromean`
   number ~10, all classified below.

2. **Bean 0voz's literal instruction ("borromean → `vol_density_per_block`")
   is superseded for absolute mass by the 2026-06-24 owner ruling.**
   `vol_density_per_block` as an *absolute mass* gives m_p ≈ 406 MeV
   (−57 %) — it is *worse*, and the guardrail marks it **binding-ratios
   only** (scale cancels). The correct absolute-mass target is the
   **`canonical_mass` facade** (muon-anchored Hecke energy → 938.27),
   not per-block. `vol_density_per_block` remains valid for
   binding/shell ratios. Do **not** mechanically swap borromean →
   per_block for anything computing an absolute mass.

## `linking_weight_family_a` is NOT deprecated

`_li_2_q_util.linking_weight_family_a(q) = (3q²+4+3q⁻²)/4 = 5/2 + (3/4)h²`
is the **PROVED Family-A categorical Wedderburn identity** and the
single source of truth for the production multiplier. It emits **no**
`DeprecationWarning` (only `vol_density_borromean` and
`mass_vol_density` do). It is used legitimately as a diagnostic /
binding-multiplier in many scripts (`mass_table_comprehensive.py`
line 165 explicitly: "reported for diagnostics only"), and in many
symbolic probes as `linking_weight_family_a_sym`. **None of these are
migration targets.** The guardrail's "λ_A is a fit" note is about the
*Borromean absolute-mass reading* `m_e·Vol(𝓑₃)·λ_A/ℏ_q²`, not about the
proved algebraic identity as a multiplier where the scale cancels.

## Call-site inventory (deprecated `vol_density_borromean`)

| Script | Regime | Disposition |
|---|---|---|
| `build_proton_mass_50dps_chain.py` | absolute m_p **chain** | **Already migrated.** Canonical m_p from the substrate-identity witness (facade source); `vol_density_borromean` retained as a **warning-suppressed audit column** only (lines 146–167). No change needed — the exemplar. |
| `m_p_borromean_verification_50dps.py` | audit / **verification of the λ_A route** | Retain (guardrail §3). Its entire purpose is to verify the +2.9 % Borromean route; docstring is honest (966 MeV = provable accuracy, Bring–Bloch = open). |
| `volume_def_reconcile.py` | audit / volume-definition reconciliation | Retain (§3). Explicit "no fit, no fabrication"; studies the two Vol(𝓑₃) definitions. |
| `per_knot_mass_table_demonstration.py` | audit / per-knot demo | Retain (§3). Main compute already uses `vol_density_per_block`; `vol_density_borromean` is the production-comparison column. Explicitly "TRUTH-TRACKING, not a closure". |
| `entanglement_emitted_energy.py` | research probe | Retain (§3). Exploratory γγ̄-emission gap probe; no fit. |
| `vol_density_per_block_wiring.py` | discipline-gate testbed | Retain (§3). Compares per-block vs production global scalar; both used deliberately. |
| `e0_lambda_tryall.py` | research probe (weight search) | Retain (§3). Candidate-weight enumeration; `vol_density_borromean` used to show it has no per-block split. |
| `probes/bring_color_weighted_base_scale_probe.py` | research probe | Retain (§3). Bring-color-weighted base-scale study. |
| `probes/option_a_vol_per_knot_light_series.py` | research probe | Retain (§3). Per-knot light-series option. |
| `probes/vol_density_borromean_q_locality_probe.py` | research probe | Retain (§3). q-locality of the Borromean VolDensity. |
| `_li_2_q_util.py` | **module definition** (+ `vol_density_borromean_spectral` wrapper) | Retain — this is where the deprecated symbol + its `DeprecationWarning` live. |
| `mass_vol_density.py` | **module definition** (+ self-consistency `abs(...)` check) | Retain — deprecated module; no external callers. |

## `mass_vol_density()` — zero external callers

`grep -rn "import mass_vol_density|from mass_vol_density|mass_vol_density("`
(excluding the `def`) returns **nothing**. The deprecated function is
called only inside its own module's self-consistency check. Nothing to
migrate.

## Mechanical fixes made on this branch

| File | Change | Math changed? |
|---|---|---|
| `atom_mass_derived.py` | Docstring redirect: two pointers telling authors to use "the canonical derived mass `m_e·Vol(K)·ρ(K)/ℏ_q²` in `mass_vol_density.py`" now point at the **`canonical_mass` facade** (muon-anchored Hecke energy) per the 2026-06-24 guardrail. This script is already a preserved structural-bug artifact that does **not** call the deprecated functions; only its author-guidance docstring was stale (recommending the deprecated wrong-volume form as "canonical"). | **No** — docstring only. |

## Deferred / left-as-is (with reason)

- **All research/audit/probe call sites above** — deferred *by design*:
  guardrail §3 allows them, they intentionally study the λ_A fit, and
  swapping them to the facade or per-block would destroy their purpose
  (or produce wrong numbers). Not "incomplete work" — correct outcome.
- **Bean 0voz / 6xug** cannot be closed as literally worded
  (borromean → per_block) because that instruction predates and
  conflicts with the 2026-06-24 owner ruling. The *intent* (get
  absolute mass off the λ_A Borromean fit) is **already satisfied** by
  the canonical-facade migration. Recommend the owner re-scope or close
  these beans against this audit.

## Verification status (STRICT honesty)

**Compute-blocked in sandbox.** This worktree has **no `mpmath`** (and
no `pyhecke`), so none of these scripts can be executed here
(`ModuleNotFoundError: No module named 'mpmath'`). All classifications
above are from **static reading** of each script's docstring + call
context. The single code change (`atom_mass_derived.py`) is a
**docstring-only** edit that changes no compute path, so it needs no
run to verify behavior-preservation. No green run is claimed.

## Appendix-sync note

No `alg:` block under
`content/quantum-observable-universe/appendix-mass-binding-algorithms/`
needs updating: the only code change is a docstring redirect that does
not alter any sidecar algorithm's compute (`uses[]`,
`computation.script`, `computation.witness`, or the math). Per the
Mass-and-Binding appendix-sync rule, pure doc/pointer edits with no math
change are exempt.
