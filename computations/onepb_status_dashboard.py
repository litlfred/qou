#!/usr/bin/env python3
"""1ppb readiness dashboard — single-witness aggregation.

QOU prediction is **structural**, not fitted against CODATA
atomic-mass tables.  The two structural prediction layers are:

  1. **LP dual shadow prices** y_λ* solving the operator-selection
     LP (`prop:operator-selection-lp` and friends).  These ARE
     the binding-energy shadow prices per Wedderburn block.  The
     active set {λ : y_λ* > 0} identifies which Wedderburn blocks
     a compound braid actually saturates.
  2. **Gröbner–Shirshov normal forms** in H_n(R, q).  The
     structural representation of each atomic configuration after
     full GS reduction.

This dashboard pulls headline metrics from both layers plus the
auxiliary audits (Macdonald telescope, BK structural battery,
Markov-axiom cross-checks).

Curve-fitting against AME atomic masses (Δ_binding column in the
additive-baseline audit) is **empirical data**, not a QOU
prediction target — included only for sanity check, not asserted
as a 1ppb gate.

Sources
-------
- `lp-confinement-nf-forcing.witness.json` — LP dual primal/dual
  values, active sets, duality gaps for compound braids.
- `confinement-operator-selection.witness.json` — operator-
  selection LP setup + Gram matrix.
- `cross-check-trM-1ppb.witness.json` — Hoefsmit vs markov_peel
  Markov-trace cross-check at 1ppb (passes for all 5 atoms).
- `codata-reconciliation.witness.json` — Markov axioms, q-integer
  identities, anchor scales.
- `ame-2020-binding-energies.witness.json` /
  `rho-f-volume-binding-gap.witness.json` — empirical AME binding
  (informational; not a QOU prediction).
- `brundan-kleshchev-audit.witness.json` — BK structural battery.
- `alpha-k-macdonald-closed-form.witness.json` — Plancherel
  completeness via Macdonald hook telescope.

Output: `onepb-status-dashboard.witness.json`.
"""

from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from _precision import fmt, set_compute_dps  # noqa: E402
# Idempotent, at module scope: mpmath defaults to dps=15, and this file now
# does mpf arithmetic on 50-digit inputs.  Without it the `max_rel_delta`
# reduction would silently round to float64 precision -- the defect this
# module was just fixed for, one layer down.
set_compute_dps()
from witness_base import WitnessBuilder  # noqa: E402


# LP-dual numeric fields that the clarabel-MPFR backend also emits as
# full-precision decimal STRINGS under `<field>_str`.
_LP_DUAL_PRECISE_FIELDS = (
    "x_star", "y0_star", "y_star", "primal_obj", "dual_obj", "duality_gap",
)


def _promote_lp_full_precision(entry: dict) -> dict:
    """Carry each LP-dual value at the precision its solver actually produced.

    `solve_operator_selection_lp` emits every dual twice: a float64 convenience
    mirror `<field>`, and — ONLY on the clarabel-MPFR backend — the
    full-precision decimal string `<field>_str` (the upstream
    `lp-confinement-nf-forcing` solve ran at `precision_bits = 167`). Copying
    the entry verbatim published the float64 mirror while the real value sat one
    key away: 48 of this witness's raw-float64 fields were that, and they are
    excused corpus-wide by the audit's LP-dual carve-out rather than drained.

    So promote `<field>_str` into the canonical name. The `_str` keys are kept
    so existing readers of either spelling still resolve.

    Where NO `_str` exists (the scipy-highs float64 backend), the float is left
    EXACTLY as it is — deliberately. Serialising it as a 50-digit string would
    manufacture digits the solve never computed, which is the float64-padding
    defect the sibling ratchet exists to catch. `backend` / `precision_bits` on
    the same entry record which case applies.
    """
    out = dict(entry)
    for field in _LP_DUAL_PRECISE_FIELDS:
        if field not in out:
            continue
        precise = entry.get(f"{field}_str")
        if precise is not None:
            out[field] = precise
    return out


def load(name: str) -> dict | None:
    base = Path(__file__).parent
    path = base / name
    if path.exists():
        return json.loads(path.read_text())
    # Phase-6 subdirectory refactor (2026-06-02): several witnesses were
    # relocated out of the flat `computations/` root into cluster subdirs
    # (e.g. audits/, alpha/).  Their producers still exist and the witness
    # files are current — they are NOT dead inventory.  Fall back to a
    # recursive search for the basename so relocated witnesses resolve and
    # are not misreported as "missing".
    matches = sorted(base.glob(f"**/{name}"))
    if matches:
        return json.loads(matches[0].read_text())
    return None


def main() -> None:
    builder = (
        WitnessBuilder("onepb-status-dashboard", engine="python")
        .set_description(
            "Aggregated 1ppb-readiness dashboard.  Single source of "
            "truth for the headline metric `max_non_anchor_delta_ppb` "
            "across the QOU primary observables (CODATA reconciliation), "
            "structural audits (Brundan–Kleshchev, Macdonald-telescope "
            "Plancherel completeness), and the open atomic-binding "
            "derivation gap (rho_f_volume_binding_gap, sourcing AME "
            "binding directly)."
        )
        .set_audit_only("docs/audits/onepb-status-dashboard.md")
    )

    sources = {
        # Structural prediction layer (LP dual + GB NF)
        "lp_confinement_nf_forcing":
            load("lp-confinement-nf-forcing.witness.json"),
        "confinement_operator_selection":
            load("confinement-operator-selection.witness.json"),
        "cross_check_trM_1ppb":
            load("cross-check-trM-1ppb.witness.json"),
        # Structural-identity audits
        "codata_reconciliation":
            load("codata-reconciliation.witness.json"),
        "brundan_kleshchev_audit":
            load("brundan-kleshchev-audit.witness.json"),
        "alpha_k_macdonald":
            load("alpha-k-macdonald-closed-form.witness.json"),
        "y_lambda_macdonald_telescope":
            load("y-lambda-macdonald-telescope.witness.json"),
        "demazure_markov_trace":
            load("demazure-markov-trace.witness.json"),
        # Empirical AME data (informational; NOT a QOU prediction)
        "rho_f_volume_binding_gap":
            load("rho-f-volume-binding-gap.witness.json"),
    }

    # ── Layer 1: structural prediction (LP dual + GB NF) ───────────
    lp_nf = sources.get("lp_confinement_nf_forcing") or {}
    lp_data = lp_nf.get("data", {}) or {}
    lp_summary = {
        "n_compounds_total": lp_data.get("n_compounds_total"),
        "n_compounds_maximizer_in_active": lp_data.get(
            "n_compounds_maximizer_in_active"
        ),
        "lp_dual_emitted": lp_data.get("lp_dual_emitted"),
        "compounds": [
            {
                "label": c.get("label"),
                "active_set": c.get("active_set_partitions"),
                "active_set_size": c.get("active_set_size"),
                "compound_maximizer_lambda": c.get(
                    "compound_maximizer_lambda"
                ),
                "I_maximizer_lambda": c.get("I_maximizer_lambda"),
                "confinement_holds": c.get("confinement_holds"),
                "delta_within_bound": c.get("delta_within_bound"),
            }
            for c in lp_data.get("compounds", [])
        ],
    }
    # Per-compound LP dual variables (y0_star, y_star, primal/dual obj).
    lp_summary["dual_values"] = [
        _promote_lp_full_precision(entry)
        for entry in lp_data.get("lp_dual_summary", [])
    ]

    # ── Layer 2: Markov-trace consistency (Hoefsmit vs markov_peel) ─
    # cross-check-trM-1ppb was originally hand-rolled (no `data`
    # field); it has since migrated to the standard WitnessBuilder
    # layout where the substantive fields live under `data.*`.
    # Read from both locations so older snapshots remain compatible.
    raw = sources.get("cross_check_trM_1ppb") or {}
    trm = raw.get("data", raw) if isinstance(raw, dict) else {}
    # Tolerance still lives in `parameters.tolerance_relative` on
    # the migrated form; fall back to the field at top level for
    # legacy snapshots.
    tolerance = (
        raw.get("parameters", {}).get("tolerance_relative")
        if isinstance(raw.get("parameters"), dict)
        else None
    ) or trm.get("tolerance_relative", 1e-9)
    # Normalise to float — the witness may store this as a decimal
    # string (parameters.tolerance_relative) or as a numeric literal
    # (legacy top-level); downstream tooling expects float-comparable.
    try:
        tolerance_float = float(tolerance)
    except (TypeError, ValueError):
        tolerance_float = 1e-9
    # Per-atom relative delta.  L1 GATES ON THE COLOR-WEIGHTED EXACT METHODS
    # (`exact_method_rel_delta` = markov_peel vs chi-cache) — the two float-clean
    # methods the 1 ppQ certification explicitly rests on.  It must NOT gate on
    # `rel_delta_max`, the max over ALL method pairs: that includes the
    # color-blind (sign-only) Hoefsmit/Habiro legs, which the cross-check itself
    # declares "informational, not gated" and which diverge by the color
    # weighting (e.g. ⁴He rel_delta_max ≈ 4.6 while its color-weighted delta is
    # ≈ 6e-50, certified). Gating on rel_delta_max held L1 red on a leg that was
    # never part of the certification (qou-wgaw, 2026-08-30).
    #
    # History: this once read `rel_delta`, a key NO delta entry carries, so
    # max_rel_delta was 0.0 by key-miss and the gate could not fail; then it was
    # "fixed" to `rel_delta_max`, which over-corrected onto the informational
    # legs. `exact_method_rel_delta` is the right quantity. Legacy names kept as
    # fallbacks for older cross-check witnesses that predate the exact-method key.
    _DELTA_KEYS = ("exact_method_rel_delta", "rel_delta_max", "rel_delta",
                   "peel_rel_delta")

    def _rel_delta(d: dict):
        """The L1-gated relative delta for one atom, as mpf.

        Returns the FIRST present key in `_DELTA_KEYS` priority order
        (`exact_method_rel_delta` — the color-weighted certification quantity —
        first), NOT the max over keys: a max would re-pick `rel_delta_max`, which
        includes the informational color-blind legs the gate must ignore.

        mpf, not float(): these arrive as 50-digit decimal STRINGS under the
        NO-FLOAT64 discipline, and this value is recorded in the witness and
        asserted against -- an argument, not a display.
        """
        for k in _DELTA_KEYS:
            if d.get(k) is not None:
                return mp.mpf(str(d[k]))
        return None

    _deltas = trm.get("deltas", []) or []
    _rds = [v for v in (_rel_delta(d) for d in _deltas) if v is not None]
    trm_summary = {
        "atoms_compared": trm.get("atoms_compared", 0),
        "any_diverge": trm.get("any_diverge", None),
        # Serialized as decimal strings, not float64. The tolerance is an exact
        # SPEC constant (1e-9), so a decimal string is its faithful form — this
        # is not float64-padding (no measured digits are invented). The float
        # `tolerance_float` is kept for in-process comparison only, never
        # published. Drains 2 of this witness's 5 baselined raw-float64 fields.
        "tolerance_relative": str(tolerance),
        "tolerance_relative_raw": str(tolerance),
        "max_rel_delta": max(_rds) if _rds else None,
        "max_rel_delta_source_key": next(
            (k for k in _DELTA_KEYS
             if any(d.get(k) is not None for d in _deltas)), None),
        "n_atoms_with_rel_delta": len(_rds),
        "all_within_1ppb": all(
            d.get("within_1ppb", False) for d in _deltas
        ) if _deltas else None,
        # L1's target was upgraded from 1 ppb to 1 ppQ (1e-15) on 2026-05-26.
        # `all_within_1ppb` is retained for consumer compatibility but is
        # named for the SUPERSEDED threshold; this is the current target.
        "all_within_1ppQ": all(
            d.get("within_1ppQ", False) for d in _deltas
        ) if _deltas else None,
        "l1_target_note": (
            "L1 target is 1 ppQ (1e-15) since 2026-05-26; the *_1ppb field "
            "names predate that upgrade and are kept for compatibility. "
            "Quote all_within_1ppQ for L1 status."
        ),
    }

    # ── Layer 3: structural identities ─────────────────────────────
    cr = sources.get("codata_reconciliation") or {}
    # LEFT AS A RAW float64, DELIBERATELY — do not "drain" this one.
    #
    # It is `max(delta_ppb)` over `codata-reconciliation`'s non-anchor rows,
    # and the maximiser is the row `α_2 − z² (Markov axiom)`, whose value is
    # `|alpha_2_eq_z_squared_check| · 1e9` read from
    # `alpha/alpha-k-jones-markov-h3.witness.json`.  That residual is produced
    # by `alpha/alpha_k_jones_markov_h3.py` entirely in **numpy float64** — the
    # χ_λ table is `float(np.trace(M))`, the Jones–Markov weights come out of
    # `np.linalg.solve`, and α_2 is a difference of two such numbers.  The
    # committed value 2.7755575615628914e-08 is 2⁻⁵⁵·1e9 and the current
    # upstream is 2⁻⁵⁴·1e9: a LAPACK cancellation residue sitting exactly on
    # the arithmetic floor, i.e. the size of the rounding rather than a
    # measurement of the Markov axiom.
    #
    # There is no exact source to carry, so there is nothing to serialize with
    # `_precision.fmt`.  Rendering it as a 50-dps string would invent ~35
    # digits nothing computed — the float64-padding defect — and would also
    # make a float64 noise floor read as a high-precision structural result,
    # which is the stronger of the two harms.  Draining it honestly means
    # porting the H_3 α_k pipeline off numpy, which moves α_1/α_2/α_3 and the
    # y_λ weights and is a separate change.  Until then this stays a float and
    # stays counted by the raw-float64 ratchet.
    structural_max_ppb = (cr.get("data", {}) or {}).get(
        "max_non_anchor_delta_ppb", None
    )

    bk = sources.get("brundan_kleshchev_audit") or {}
    bk_assertions = bk.get("assertions", [])
    bk_pass = sum(1 for a in bk_assertions if a.get("passed"))
    bk_total = len(bk_assertions)

    macd = sources.get("alpha_k_macdonald") or {}
    macd_assertions = macd.get("assertions", [])
    plancherel_residuals = [
        a.get("computed")
        for a in macd_assertions
        if a.get("name", "").startswith("plancherel_completeness_n")
    ]

    # ── Layer 4: empirical AME data (informational) ────────────────
    # Binding metrics now derive from rho_f_volume_binding_gap, which
    # reads AME2020 binding directly (the additive-constituent baseline
    # was purged 2026-06-09).
    rfb = sources.get("rho_f_volume_binding_gap") or {}
    _brows = (rfb.get("data", {}) or {}).get("rows", []) or []
    # `delta_binding_MeV` now arrives as the AME2020 table's EXACT decimal
    # TEXT (`rho_f_volume_binding_gap.py` carries the vendored decimal
    # verbatim, following `ame_2020_binding_energies.py`).  `Fraction` and
    # `mpf` both accept it, and `str()` keeps this working against an older
    # witness that still stores a float.  rho_f rows always carry A ≥ 2.
    _bstr = [str(r["delta_binding_MeV"]) for r in _brows]

    # The maximum IS one of the AME inputs, so emit that input's own digits
    # verbatim.  Two things this must not do: `max()` over the strings
    # directly (lexical order puts "8.48…" above "39.24…"), and re-serializing
    # the winner through `fmt` (that pads a 9-significant-figure measurement
    # out to OUTPUT_DPS).  Compare as mpf, emit the source string.
    binding_max = (
        max(zip((mp.mpf(s) for s in _bstr), _bstr), key=lambda t: t[0])[1]
        if _brows else None
    )

    # Σ(B_i/A_i)/N is COMPUTED, not read — and it is an exact rational, since
    # every B_i is an exact decimal and every A_i an exact integer.  So its
    # digits past float64 width are genuinely determined by the inputs rather
    # than invented, which is what separates this from the padding defect.
    # Compute it in `Fraction` (exactly), then render at OUTPUT_DPS from the
    # exact numerator/denominator so no binary rounding enters at all.  The
    # exact rational is emitted alongside so a reader can check the digits
    # instead of taking them on trust.
    _avg_exact = (
        sum((Fraction(s) / int(r["A"]) for s, r in zip(_bstr, _brows)),
            Fraction(0)) / len(_brows)
        if _brows else None
    )
    binding_avg = (
        fmt(mp.mpf(_avg_exact.numerator) / mp.mpf(_avg_exact.denominator))
        if _avg_exact is not None else None
    )

    summary = {
        "structural_lp_dual": lp_summary,
        "markov_trace_consistency": trm_summary,
        "structural_max_non_anchor_delta_ppb": structural_max_ppb,
        "brundan_kleshchev": {
            "passed": bk_pass,
            "total": bk_total,
            "tests": [
                "dim H_n = n!",
                "dim Z(H_n) = p(n)",
                "Jucys-Murphy content separation",
                "bar-invariant Plancherel sum",
            ],
        },
        "macdonald_telescope_plancherel_residuals": plancherel_residuals,
        "ame_empirical_data_informational": {
            "max_delta_binding_MeV": binding_max,
            "avg_binding_per_nucleon_MeV": binding_avg,
            "avg_binding_per_nucleon_MeV_exact_rational": (
                f"{_avg_exact.numerator}/{_avg_exact.denominator}"
                if _avg_exact is not None else None
            ),
            "precision_note": (
                "max_delta_binding_MeV is one of the AME2020 table's own "
                "decimals, emitted verbatim — it carries exactly the digits "
                "AME quotes and is not padded.  "
                "avg_binding_per_nucleon_MeV is the exact rational above "
                "rendered at output_dps; every digit is determined by the "
                "exact AME decimals and the integer A, none is invented."
            ),
            "note": (
                "Empirical AME column for sanity-check only.  QOU "
                "predictions come from the LP dual + GB NF layers "
                "above, not from fitting against this column."
            ),
        },
        "witness_inventory": [
            name for name, data in sources.items() if data is not None
        ],
        "missing_witnesses": [
            name for name, data in sources.items() if data is None
        ],
    }
    # Structural-witness inventory presence is a NON-GATING bucket: it is
    # reported here but does NOT contribute to allPassed.  allPassed
    # reflects the L1 compute assertions only (lp_max_duality_gap,
    # markov_trace_max_rel_delta).  The two structural-audit witnesses
    # (Brundan–Kleshchev, Macdonald α_k closed form) are not L1 precision
    # cross-checks, so a relocated/absent one must not masquerade as an L1
    # compute failure — the historical `allPassed:false` artifact this
    # dashboard emitted despite L1 being certified.  See
    # docs/audits/2026-07-20-close-1ppq-attempt.md.
    summary["structural_inventory"] = {
        "present": len(summary["witness_inventory"]),
        "expected": len(sources),
        "complete": not summary["missing_witnesses"],
        "gating": False,
        "note": (
            "Non-gating inventory bucket.  Does NOT affect allPassed, "
            "which reflects the L1 compute assertions only.  A missing "
            "structural-audit witness is an inventory issue, not an L1 "
            "precision failure."
        ),
    }

    print("1ppb-readiness dashboard")
    print("=" * 70)
    print()
    print("Layer 1 — LP dual / GB NF (QOU's structural prediction):")
    print(f"  compounds tested: {lp_summary['n_compounds_total']}")
    print(f"  GB NF maximizer in active set: "
          f"{lp_summary['n_compounds_maximizer_in_active']}/"
          f"{lp_summary['n_compounds_total']}")
    _max_gap_display = max(
        (mp.mpf(str(d.get("duality_gap", 0)))
         for d in lp_summary["dual_values"]), default=mp.mpf(0))
    print(f"  duality gap (max across compounds): {_max_gap_display}")
    print(f"  active sets: "
          f"{[c['active_set_size'] for c in lp_summary['compounds']]}")
    print()
    print("Layer 2 — Markov-trace consistency (Hoefsmit vs markov_peel):")
    print(f"  atoms compared: {trm_summary['atoms_compared']}, "
          f"any_diverge: {trm_summary['any_diverge']}, "
          f"max rel_delta: "
          f"{mp.nstr(trm_summary['max_rel_delta'], 6) if trm_summary['max_rel_delta'] is not None else 'n/a'}, "
          f"all_within_1ppb: {trm_summary['all_within_1ppb']}")
    print()
    print("Layer 3 — Structural identities:")
    print(f"  CODATA max non-anchor Δ: {structural_max_ppb} ppb "
          "(AME publication-rounding floor only)")
    print(f"  BK structural audit: {bk_pass}/{bk_total} passed")
    print(f"  Macdonald Plancherel residuals: "
          f"{len(plancherel_residuals)} entries (each ~10⁻⁵¹)")
    print()
    print("Layer 4 — Empirical AME data (informational, not asserted):")
    # Labels corrected: the rho_f rows are ²H–⁷Li (`_AME_ISOTOPES` in
    # rho_f_volume_binding_gap.py), so the maximiser is ⁷Li and the average
    # runs over A ≥ 2, not ²⁰Ne and A ≥ 4.
    print(f"  max Δ_binding (⁷Li, over ²H–⁷Li): {binding_max} MeV")
    print(f"  avg per nucleon (A ≥ 2): {binding_avg} MeV/A "
          "(SEMF reference: ~7.5 MeV/A)")
    print()
    print(f"Witnesses present: "
          f"{len(summary['witness_inventory'])}/"
          f"{len(sources)}")
    if summary["missing_witnesses"]:
        print(f"Missing: {summary['missing_witnesses']}")

    # NOTE: witness-inventory presence is intentionally NOT a gating
    # assertion.  It is recorded in the non-gating
    # `summary.structural_inventory` bucket instead, so allPassed reflects
    # the L1 compute state (lp gap + Markov-trace consistency) rather than
    # structural-audit inventory bookkeeping.  (Fix 2026-07-20: producerless
    # dead-inventory / relocated structural witnesses were spuriously
    # flipping allPassed to false despite L1 being certified.)
    # LP duality gap (structural): must be exactly 0 across all
    # compounds for strong duality to hold.
    if lp_summary["dual_values"]:
        # `duality_gap` now arrives as the solver's full-precision decimal
        # string (see `_promote_lp_full_precision`), so compare as mpf rather
        # than as float64 -- `max()` over strings would order lexically.
        max_gap = max(mp.mpf(str(d.get("duality_gap", 0)))
                      for d in lp_summary["dual_values"])
        builder.add_assertion(
            name="lp_max_duality_gap",
            # Serialized, not passed raw: `duality_gap` reaches here as a
            # float64 out of the LP-dual block, where `LP_DUAL_F64_FIELDS`
            # excuses it -- but that carve-out is keyed on the field NAME, so
            # copying the value into `computed` re-exposes it and the
            # raw-float64 ratchet counts it. The sibling assertion below is
            # already a string for the same reason. Fixed 2026-08-29; the
            # regression came in with 755ab8a5b7 (0.0 -> 7.31e-50).
            computed=fmt(max_gap),
            expected="0",
            # 1e-15 = the L1 target (1 ppQ) this dashboard reports as
            # `all_within_1ppQ`; until 2026-09-08 the assertion gated at 1e-9
            # while the boolean claimed 1e-15, so a regression to 1e-12 would
            # have passed `allPassed`. Tightened, never widened (C5 of
            # docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §7.3).
            tolerance="1e-15",
            source="prop:operator-selection-lp strong duality",
        )
    # Markov-trace consistency: max relative difference < 1ppb.
    # NOTE: this reads `max_rel_delta`, which until 2026-08-29 was 0.0 by
    # key-miss (see the `_DELTA_KEYS` note above), so this assertion passed
    # unconditionally.  It now carries the measured value and can fail.
    # The tolerance is NOT widened to accommodate the measurement it now
    # sees (AGENTS.md: baselines drain, never grow). It was TIGHTENED 1e-9 ->
    # 1e-15 on 2026-09-08 so the gate matches the 1 ppQ claim it reports.
    if trm_summary["max_rel_delta"] is not None:
        builder.add_assertion(
            name="markov_trace_max_rel_delta",
            # Strings, per `add_assertion`'s drained convention. `expected` and
            # `tolerance` are exact spec constants (0 and 1e-15), so a decimal
            # string is faithful, not float64-padding. `computed` is already an
            # mpf carried from the 50-digit source.
            computed=fmt(trm_summary["max_rel_delta"]),
            expected="0",
            tolerance="1e-15",
            source="cross-check-trM-1ppb (color-weighted exact methods: markov_peel vs chi-cache)",
        )
    builder.add_data("summary", summary)
    builder.add_data("framing_note",
                     "Layers 1–2 are QOU's structural predictions "
                     "(LP dual shadow prices + GB NF Markov-trace "
                     "consistency).  Layer 4 (AME atomic masses) is "
                     "experimental data, not a prediction target — "
                     "QOU does not fit against it.")

    out_path = builder.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
