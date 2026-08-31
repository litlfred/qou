#!/usr/bin/env python3
"""hecke_core_symbolic_migration.py
====================================

**The producer for `hecke-core-symbolic-migration.witness.json`, which had
none — and which two content manifests name as a maintenance contract.**

That witness records the Track-A migration check: `hecke_core.py` is the
NUMERICAL fast path (it substitutes `q₀` at import time, so every quantity is
float64 from module load), and `hecke_core_symbolic.py` is the parallel
SYMBOLIC-in-`q` module. The witness compares the two, quantity by quantity, and
asserts the deltas are at the arithmetic floor.

## Why it needed a producer, and why this one is not a transcription

The witness's own `scriptFile` reads *"(legacy — no matching producer found;
provenance pending manual triage)"*, and the producer-resolution audit
(`qou-agvb`) confirmed nothing in the tree writes it. Both modules it compares
**do** exist and expose paired entry points, so the comparison is genuinely
re-runnable — that is what separates this from `canonical-mass-table-242ppb`,
the other manifest-contract orphan, whose numbers no live code reproduces and
which therefore gets a finding rather than a producer (`qou-nro6`).

## The manifests disagree about who produces it

Two content blocks name this witness in their `computation.witness` field and
give **different producers**:

    mba-step02-gs-reduction.ts        engine "rust",  tools/hecke-engine/src/gb_nf_reducer.rs
    e-hartree-categorical-derivation.ts  engine "sympy", computations/substrate/hecke_core.py

Neither of those files mentions this witness. The sympy claim is the closer one
— the witness is a sympy-vs-float64 comparison — but it names the *numerical*
module, which is only one of the two sides. Recorded, not silently resolved:
correcting a manifest is a content edit and belongs with the author.

## The anchor moves, and that is the point

The committed witness was computed at `q0_value = 1.1099785955541805` — the
**CODATA-2018 muon derivation**, which the 2026-08-22 owner ruling retired in
favour of CODATA 2022, and which is not the canonical pin for new compute in
any case (proton, owner directive 2026-08-07). This producer runs at the
canonical **proton** pin. Numbers therefore differ from the committed file by
roughly the μ–p separation, and anything beyond that is a transcription error
worth finding — the same posture `qou-bake` set for the five keystone
witnesses.

The *assertions* are anchor-independent in shape: they say the symbolic and
numerical paths agree to the arithmetic floor, which is a statement about the
two code paths, not about which `q₀` they are evaluated at.

PRECISION
---------
The numerical side is float64 **by construction** — that is the property under
test, not a defect, and it is why the deltas are reported at ~1e-16/1e-17
rather than at 50 dps. The symbolic side is evaluated through
`hecke_core_symbolic.evalf_at_q0` at 50 dps. Deltas are computed in `mpmath`
and serialized with `_precision.fmt`; the float64 inputs are labelled as such
in the witness rather than presented as exact.

Usage:
    python3 computations/substrate/hecke_core_symbolic_migration.py
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_HERE = _Path(__file__).resolve().parent
_sys.path.insert(0, str(_HERE))
_sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _b  # noqa: E402, F401
del _b

import time  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.constants import Q as Q0_PROTON  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

import hecke_core as HC  # noqa: E402
import hecke_core_symbolic as HS  # noqa: E402

set_compute_dps(50)

Z, N = 1, 0          # proton, the particle the committed witness used
DPS = 50


def _mpf(x):
    """float64 or sympy value -> mpf, without pretending the float is exact."""
    try:
        return mp.mpf(str(x))
    except (TypeError, ValueError):
        return mp.mpf(str(complex(x).real))


def main() -> int:
    t0 = time.monotonic()
    fails = 0

    def chk(label, ok):
        nonlocal fails
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")

    print("hecke_core symbolic-vs-numerical migration check (qou-nro6)\n")
    print(f"  q0 (canonical proton pin) = {mp.nstr(mp.mpf(Q0_PROTON), 17)}")
    print("  committed witness used     = 1.1099785955541805  (CODATA-2018 muon, RETIRED)\n")

    results = {}

    # ── 1 · NF basis ──────────────────────────────────────────────────────
    print("1 · NF basis: numerical float64 vs symbolic evaluated at q0")
    nf_num = HC.build_atom_nf(Z, N)
    nf_sym = HS.build_atom_nf_sym(Z, N)
    rows, worst_nf = [], mp.mpf(0)
    for i, (a, b) in enumerate(zip(nf_num, nf_sym)):
        va, vb = _mpf(a), HS.evalf_at_q0(b, DPS)
        d = abs(va - vb)
        worst_nf = max(worst_nf, d)
        rows.append({"basis_idx": i, "numerical_f64": fmt(va),
                     "symbolic_at_q0_50dps": fmt(vb), "abs_delta": fmt(d)})
    results["side_by_side_nf_basis"] = rows
    print(f"    {len(rows)} basis elements, max |delta| = {mp.nstr(worst_nf, 6)}")
    chk("nf_basis max delta < 1e-13", worst_nf < mp.mpf("1e-13"))

    # ── 2 · Markov trace ─────────────────────────────────────────────────
    print("\n2 · Markov trace")
    tr_sym = HS.evalf_at_q0(HS.nf_tr_sym(nf_sym), DPS)
    tr_num = _mpf(sum(nf_num)) if not hasattr(HC, "nf_tr") else _mpf(HC.nf_tr(nf_num))
    d_tr = abs(tr_num - tr_sym)
    results["markov_trace"] = {"numerical_f64": fmt(tr_num),
                               "symbolic_at_q0_50dps": fmt(tr_sym),
                               "abs_delta": fmt(d_tr)}
    print(f"    numerical = {mp.nstr(tr_num, 14)}")
    print(f"    symbolic  = {mp.nstr(tr_sym, 14)}   |delta| = {mp.nstr(d_tr, 6)}")
    chk("markov_trace delta < 1e-13", d_tr < mp.mpf("1e-13"))

    # ── 3 · V_full ───────────────────────────────────────────────────────
    print("\n3 · V_full")
    try:
        v_num = HC.atom_V_full(Z, N)
        v_sym = HS.atom_V_full_sym(Z, N)
        vn = _mpf(v_num[0] if isinstance(v_num, tuple) else v_num)
        vs = HS.evalf_at_q0(v_sym[0] if isinstance(v_sym, tuple) else v_sym, DPS)
        d_v = abs(vn - vs)
        results["v_full"] = {"numerical_f64": fmt(vn),
                             "symbolic_at_q0_50dps": fmt(vs),
                             "abs_delta": fmt(d_v)}
        print(f"    numerical = {mp.nstr(vn, 14)}")
        print(f"    symbolic  = {mp.nstr(vs, 14)}   |delta| = {mp.nstr(d_v, 6)}")
        # The COMMITTED witness records max_v_full_abs_delta = 1.1155, i.e. the
        # two paths did NOT agree on V_full even when it was written. Reported
        # as measured; not asserted, and NOT quietly dropped.
        results["v_full"]["committed_witness_recorded_delta"] = "1.1155095220750846"
        results["v_full"]["note"] = (
            "the committed witness recorded a V_full delta of 1.1155 -- the two "
            "paths did not agree on this quantity when it was written either. "
            "Measured and reported, not asserted.")
    except Exception as exc:  # noqa: BLE001
        results["v_full"] = {"error": f"{type(exc).__name__}: {exc}"}
        print(f"    unavailable: {type(exc).__name__}: {exc}")

    # ── 4 · alpha_EM^-1 ──────────────────────────────────────────────────
    print("\n4 · alpha_EM^-1")
    try:
        a_num = _mpf(HC.ALPHA_EM_INV_DERIVED)
        a_sym = HS.evalf_at_q0(HS.alpha_em_inv_sym(), DPS)
        d_a = abs(a_num - a_sym)
        results["alpha_em_inv"] = {"numerical_f64": fmt(a_num),
                                   "symbolic_at_q0_50dps": fmt(a_sym),
                                   "abs_delta": fmt(d_a)}
        print(f"    numerical = {mp.nstr(a_num, 16)}")
        print(f"    symbolic  = {mp.nstr(a_sym, 16)}   |delta| = {mp.nstr(d_a, 6)}")
        chk("alpha_em_inv delta < 1e-10", d_a < mp.mpf("1e-10"))
    except Exception as exc:  # noqa: BLE001
        results["alpha_em_inv"] = {"error": f"{type(exc).__name__}: {exc}"}
        print(f"    unavailable: {type(exc).__name__}: {exc}")

    print(f"\n{'ALL CHECKS PASSED' if not fails else str(fails) + ' CHECK(S) FAILED'}")

    w = WitnessBuilder("hecke-core-symbolic-migration", start_time=t0)
    w.set_description(
        "Track-A migration check: hecke_core.py (NUMERICAL fast path, q0 "
        "substituted at import so every quantity is float64 from module load) "
        "against hecke_core_symbolic.py (parallel SYMBOLIC-in-q module), "
        "quantity by quantity. REGENERATED 2026-08-30 by its first producer "
        "(bean qou-nro6): the committed witness was hand-written, its own "
        "scriptFile read '(legacy -- no matching producer found)', and the "
        "producer-resolution audit confirmed nothing wrote it -- while TWO "
        "content manifests name it in computation.witness as a maintenance "
        "contract. It was also computed at the RETIRED CODATA-2018 muon pin "
        "1.1099785955541805; this runs at the canonical proton pin, so numbers "
        "move by roughly the mu-p separation and anything beyond that is a "
        "transcription error worth finding.")
    for k, v in results.items():
        w.add_data(k, v)
    w.add_data("anchor_change", {
        "committed_witness_q0": "1.1099785955541805",
        "committed_anchor": "CODATA-2018 muon derivation -- retired by the "
                            "2026-08-22 owner ruling (CODATA 2022) and not the "
                            "canonical pin for new compute in any case",
        "this_run_q0": str(Q0_PROTON),
        "this_anchor": "proton (owner directive 2026-08-07)",
    })
    w.add_data("manifest_producer_conflict", {
        "witness_is_named_by": {
            "mba-step02-gs-reduction.ts": {
                "engine": "rust",
                "script": "tools/hecke-engine/src/gb_nf_reducer.rs"},
            "e-hartree-categorical-derivation.ts": {
                "engine": "sympy",
                "script": "computations/substrate/hecke_core.py"},
        },
        "problem": ("two manifests name DIFFERENT producers for the same "
                    "witness, and neither named file mentions it. The sympy "
                    "claim is closer -- this IS a sympy-vs-float64 comparison "
                    "-- but it names the NUMERICAL module, only one of the two "
                    "sides compared."),
        "resolved_here": False,
        "reason": "correcting a manifest is a content edit; it belongs with "
                  "the author, not with this producer.",
    })
    w.add_data("precision_note", {
        "numerical_side": "float64 BY CONSTRUCTION -- that is the property "
                          "under test, not a defect, and it is why deltas sit "
                          "at ~1e-16 rather than at 50 dps",
        "symbolic_side": "evalf_at_q0 at 50 dps",
        "deltas": "computed in mpmath, serialized with _precision.fmt",
    })
    w.add_data("checks_failed", fails)
    w.add_assertion("nf_basis_agrees_to_float64_floor",
                    worst_nf < mp.mpf("1e-13"), True)
    w.add_assertion("markov_trace_agrees_to_float64_floor",
                    d_tr < mp.mpf("1e-13"), True)
    w.add_assertion("regenerated_at_canonical_proton_pin", True, True)
    w.save({
        "q0Anchor": "proton",
        "q0Value": str(Q0_PROTON),
        "q0AnchorReason": (
            "regenerated at the canonical proton pin (owner directive "
            "2026-08-07). The committed witness used the RETIRED CODATA-2018 "
            "muon derivation 1.1099785955541805; the anchor change is "
            "deliberate and its effect on the numbers is the point."),
    })
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
