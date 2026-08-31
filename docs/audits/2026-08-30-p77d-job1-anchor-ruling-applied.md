# `qou-p77d` job 1 — the anchor ruling applied, and the blocker was a misdiagnosis

**Date:** 2026-08-30 · **Bean:** `qou-p77d` (STILL OPEN, job 1) · **Branch:** `claude/p77d-anchor-ruling-2026-08-30`

## Summary

Bean `qou-p77d` held 32 q-dependent producers for months on the ground that

> "Fixing them means `Q` → `q_at(dps)` per producer, which forces a PROTON-VS-MUON
> ANCHOR CHOICE each time — the layer straddle AGENTS.md singles out.
> **Owner decision, 32 times. Not guessable.**"

**That premise is false, and this document measures it.** `Q` and `q_at()` are two
*precisions of one anchor*, both bound after the same manifest lookup. The edit
cannot move a producer between pins. Separately, **none of the 32 is in
`ideal_muon`** — all 32 already resolve to proton today.

The owner ruling ("proton unless an explicit comparison, or the ideal CAL-1/2/3
mathematical layer") therefore does not have to adjudicate 32 decisions. It
confirms 29 producers on the default they already have, and names the 3 that
carry a real exception.

## Measurement 1 — the population is 32 producers / **197** fields, not 209

Re-derived independently by replicating `assertion_value_float64_triage.py`'s
classifier and intersecting bucket B with producers that read `q_parameter`:

```
bucket B producers: 53   fields: 270
  q-dependent:      32   fields: 197
  q-independent:    21   fields:  73
```

The producer count reproduces the bean's 32 exactly. **The field count is 197,
not 209** — the bean's figure predates drains that have since landed. Per the
bean's own standing instruction ("Re-measure; do not quote this figure"), quote
197 with this date.

## Measurement 2 — `Q` → `q_at(dps)` is anchor-PRESERVING

`computations/substrate/q_parameter.py` resolves the anchor **once, at import**,
from `QOU_Q0_ANCHOR` or from the running producer's stem (`:101-111`):

```python
_stem = _MP(_sys.argv[0]).stem if (_sys.argv and _sys.argv[0]) else ""
if _stem in _man.get("ideal_muon", []):
    _anchor = "ideal"
```

Both `Q` and `q_at` are then bound *inside the branch that decision selects* —
`Q = float(_d["q"])` at `:157` and `def q_at(...)` at `:230` for muon; both
imported from `qou_substrate.constants` for proton. There is no path on which
they disagree.

Measured directly, by running one probe script under two `argv[0]` stems so the
manifest lookup selects differently:

| stem | manifest | `Q` (float) | `q_at(50)` | `q_at − mpf(Q)` |
|---|---|---|---|---|
| `channel_product_mass` | `physical_proton` | `1.1099785827513808` | `1.109978582751380807591669095610768879874499121873578736` | `-3.0242507e-17` |
| `hadron_knot_table` | `ideal_muon` | `1.109978595642739` | `1.109978595642739046681795129380001752700065561029011557` | `5.6989347e-18` |

Both rows stay in their own anchor's basin (`…82751…` vs `…95642…`). **The swap
changes precision only.** It is also a *real* gain on the proton side: the
50-digit value diverges from the float64 at the 17th digit.

## Measurement 3 — none of the 32 is muon-pinned

Against `computations/q0_anchor_manifest.json` (`ideal_muon` = 19 stems,
`physical_proton` = 719, `ambiguous` = 16):

```
physical_proton  20
unlisted         11   -> proton, by q_parameter.py:108 (only ideal_muon diverts)
ambiguous         1   -> mass-from-q-symbolic
ideal_muon        0
```

## Classification under the ruling

**Proton is the default; the burden is on the exception.** 29 of 32 carry no
exception — the word "muon" does not occur in 26 of them at all.

### E1 — explicit proton-vs-muon comparison (2)

| producer | evidence |
|---|---|
| `mass-from-q-symbolic.py` | `:489` *"DELIBERATE MUON READ — do NOT reroute through q_parameter. This producer computes at the proton pin throughout; the muon pin is read here, and only here"*; `:452` *"the genuine substrate tension (proton pin vs muon pin)"*. Already listed `ambiguous`; the per-process muon read is the override the ruling prescribes. |
| `deuteron_from_scratch_ledger.py` | `:112-113` solves both pins live (`q_at(DPS)` / `q_muon_at(DPS)`), emits `anchor_tension_rel` + `anchor_tension_ppb`, and attributes S2 nucleon-mass error **per anchor** (`:222`, `:420`). Measuring the difference between the pins *is* its subject. Already uses the accessors, not `Q`. |

### E2 — the ideal CAL-1/2/3 mathematical layer (1)

| producer | evidence |
|---|---|
| `knot-volumes.py` | Declares `q0Anchor: "independent"` with the reason *"the CAL-2 definition run as that assertion's subject … in the muon basin BY CONSTRUCTION and cannot track the proton pin"*. It computes `q₀` from `Vol(4₁)` and `m_μ/m_e` — the CAL-2 proxy relation itself, as mathematics, not an observable evaluated at a pin. |

### Proton (29)

`channel_product_mass`, `unified-mass-molecular`, `probe_9b_laurent_degree_10a5`,
`atom_mass_derived`, `molecular-trefoil-scan`, `tau-lepton-nf`,
`binding_single_pipeline_comparison`, `orbit_trace_identity_proof`,
`staircase_ew_predictions`, `confined_knot_binding`,
`delta_lambda_energy_scale_extensivity_probe`, `orbit_reduction_crosscheck`,
`neutron_error_diagnostic`, `tr_m_algebraic_q`, `crystal_alpha_shift_pole_orders`,
`borromean-axial-coupling`, `d_density_derivation`, `delta_lambda_canonical_residual`,
`gram_norm_binding_probe`, `homflypt_operator_valued_probe`,
`lp_confinement_nf_forcing`, `derived_bond_graph_binding`, `path_b_evacuation`,
`h2-molecular-binding`, `option_b_proton_mass_full_chain`, `chirality_braid_average`,
`log_ratio_binding_prototype`, `gap_a1_binding_k_sdp_feasibility`,
`probe_d_qbeta_h_invariant`.

### Four E1/E2 signals examined and REJECTED

A keyword scan is not a classification. Each of these tripped the scan and is
**not** an exception:

- `atom_mass_derived.py` — "muon" occurs only as *"the **muon-anchored** Hecke
  energy via the `canonical_mass` facade"*. That names the **mass formula**
  (`m_p = 2·(m_μ·F_Bor − 6·m_e)`, owner ruling 2026-06-24), not a q₀ pin.
- `tau-lepton-nf.py` — "muon" is a **particle label** in the lepton tower
  (`n = 5`, `T_{2,5}`). No pin content.
- `binding_single_pipeline_comparison.py` — the "comparison" is of **binding
  models** (`B_lin` / `B_sym` / `B_qCLT`) on one trace, not of pins.
- `unified-mass-molecular.py`, `neutron_error_diagnostic.py` — *"CAL-3-ish
  acknowledged inputs"* names an **input class**; the producers evaluate
  observables (molecular masses, neutron error), which is what E2 excludes.

## What remains genuinely open

The blocker is dissolved but the *work* is not free, and the reason is the bean's
own trap, not the anchor:

> **The flip alone is necessary but NOT sufficient.** mpmath defaults to
> `mp.dps = 15`, so mpf constants still compute at float64 grade until the
> producer raises dps. Removing casts without raising dps is WORSE than
> nothing — it serializes a 53-bit value at full width.

All 32 are **bucket B** — they never raise `mp.dps`. So `Q` → `q_at(50)` alone
buys nothing: the mpf is immediately truncated to ~53 bits by the surrounding
arithmetic. Each producer needs `set_compute_dps()` **and** the accessor swap
**and** its float casts removed, then a re-run and a witness diff. That is real
per-producer work — but it is **precision work with no owner decision in it**,
which is the point of this document.

## Gate baseline

`computations/audits/q0_anchor_consistency_audit.py` before any change:
`Q0_OK 1126`, `Q0_FLIP 1`, `Q0_ANCHOR_MISSING 1645`, exit 0. The single
`Q0_FLIP` is the known `hadron-knot-table.witness.json` survivor carrying the
retired A-anchor (AGENTS.md §"q₀ anchor convention").

## Scoping the follow-on work (measured, same session)

Since the anchor question is settled, the useful remaining question is *what
would the fix actually be*. Split the 32 by whether the prescribed `Q` →
`q_at(dps)` swap is even applicable:

| group | producers | fields | what the swap would do |
|---|---:|---:|---|
| **no mpmath at all** | 21 | 72 | inject one `mpf` into float64 arithmetic; every downstream `float()` kills it |
| **imports mpmath, never raises dps** | 8 | 121 | plausible — needs `set_compute_dps()` in the same edit |
| **already calls `q_at`** | 3 | 4 | nothing; the swap is already done |

### The 3 that already call `q_at` were never anchor decisions

- `lp_confinement_nf_forcing.py:119` — `q0 = q_at(50)`, no cast. Fully correct
  at the q₀ read already; its one float64 field originates elsewhere.
- `delta_lambda_canonical_residual.py:59` — `q0 = float(q_at(30))`. The accessor
  swap is *done*; the defect is the cast one call out, a purely local repair
  with no anchor content whatsoever.
- `deuteron_from_scratch_ledger.py` — uses `q_at` / `q_muon_at` (the E1 producer).

### The 21 without mpmath are the bean's own "43" class

`d_density_derivation.py` is representative: `import math` at `:43`, `from
q_parameter import Q as Q0` at `:54`, and `float(...)` on every emitted quantity
(`:105-107`, `:233-262`). There is no mpf anywhere for a 50-digit `q_at` to flow
into. Same shape in `tr_m_algebraic_q.py`, which evaluates through sympy
`.subs(q, q0)` and casts at `:169`, `:182-183`.

This is exactly the class the bean already characterised and already ruled out
of a drain:

> "43 producers **NO MPMATH AT ALL** — float64 end to end. → not a serialization
> or dps problem. 'Fixing' one means RE-DERIVING the computation in mpmath, per
> producer, changing values that feed real claims."

So the honest residue of job 1 is **8 producers / 121 fields**, not 32 / 197 —
and the other 24 belong to the bucket-B port that the bean says "wants its own
bean", on precision grounds with no anchor content.
