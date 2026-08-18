#!/usr/bin/env python3
"""End-to-end NO-FLOAT64 LP dual on the H_3(q) atomic Gram (#10).

Demonstrates the float64-free path the new `gram_matrix_mp` accessors
enable: the 50-dps mpmath Gram + Markov trace are marshalled as decimal
strings straight to the clarabel-MPFR `clarabel-operator-selection-lp`
binary (~50 dps), with NO float64 anywhere on the input side. This is the
consumer that `gram_matrix_mp_strings` / `tr_m_mp_strings` were built for
(closing the "gram_matrix_mp has no consumer" gap).

Scientific note: the H_3(q) atom-level operator-selection LP is
DEGENERATE — its net shadow price y0_star ≈ 0 (the trivial channel
saturates), so this is a *pipeline* demonstration, not a new result. The
value is the precision discipline: every input crosses the FFI boundary as
a 50-dps string, not an f64. Marked auditOnly.

Contrast with the scipy backend of solve_operator_selection_lp, whose
inputs are np.float64 — that path truncates the Gram to f64 before the
solve. Use THIS path (or pass 50-dps strings to the clarabel CLI) when the
no-float64 discipline matters.

Usage:
    python3 computations/atom_dual_q0_mpfr_demo.py
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

from pyhecke import gram


def _find_clarabel_bin() -> Path | None:
    rel = Path("tools/hecke-engine/target/release/clarabel-operator-selection-lp")
    for parent in Path(__file__).resolve().parents:
        cand = parent / rel
        if cand.exists():
            return cand
    return None


def solve_atom_dual_q0_mpfr(prec_bits: int = 167) -> dict:
    """Solve the H_3(q) operator-selection LP dual at ~50 dps with NO
    float64 inputs: 50-dps string Gram/trace → clarabel-MPFR."""
    G_str = gram.gram_matrix_mp_strings()   # 50-dps, no float64
    t_str = gram.tr_m_mp_strings()          # 50-dps, no float64
    binp = _find_clarabel_bin()
    if binp is None:
        return {"error": "clarabel-operator-selection-lp binary not built; "
                "cargo build --release --features clarabel-mpfr --bin "
                "clarabel-operator-selection-lp"}
    payload = {
        "t": t_str, "G": G_str, "n_target": "1",
        "m_bound": "1000000", "dual_tol": "1e-9", "prec_bits": int(prec_bits),
    }
    proc = subprocess.run([str(binp)], input=json.dumps(payload),
                          capture_output=True, text=True)
    if proc.returncode != 0:
        return {"error": f"clarabel binary exit {proc.returncode}: "
                f"{proc.stderr[:300]}"}
    out = json.loads(proc.stdout) if proc.stdout.strip() else {}
    out["_inputs_float64_free"] = True
    out["_t_str_sample"] = t_str[:3]
    return out


def main() -> int:
    res = solve_atom_dual_q0_mpfr()

    # SURFACE THE MISSING BACKEND INSTEAD OF PRINTING OVER IT.
    # `solve_atom_dual_q0_mpfr` has always returned {"error": ...} with the
    # exact cargo line when the binary is absent, and main() never looked. So
    # the run printed a "NO-FLOAT64 path" banner above a table of Nones and
    # exited 0 — a demo that advertises a precision guarantee it did not
    # deliver, and reports success either way. Check first, say so, exit
    # non-zero. Bean qou-cp1w.
    if res.get("error"):
        print("H_3(q) atom LP dual — NOT RUN")
        print(f"  {res['error']}")
        print("  No witness emitted: there is no result to record.")
        return 2

    print("=" * 70)
    print("H_3(q) atom LP dual — NO-FLOAT64 path (50-dps strings → clarabel-MPFR)")
    print("=" * 70)
    for k in ("feasible", "y0_star", "active_set", "primal_obj",
              "dual_obj", "duality_gap"):
        print(f"  {k:12} = {res.get(k)}")
    print(f"  inputs are 50-dps strings (no float64): {res.get('_inputs_float64_free')}")
    print("  NOTE: y0_star ≈ 0 — the H_3 atom LP is degenerate; this is a")
    print("        pipeline/precision demonstration, not a new result.")

    # Witness (auditOnly — pipeline demo, no new claim).
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
    # Narrowed from a bare `except Exception`. That catch-all is why
    # `wb.write()` survived: WitnessBuilder has only ever had `save()`, so every
    # run raised AttributeError, printed one line, and continued — for as long
    # as the file has existed. Only the import is allowed to fail softly now
    # (qou-substrate genuinely may be absent); anything else is a real bug and
    # is raised.
    try:
        import mpmath as mp  # noqa: F401
        from _precision import fmt  # noqa: F401
        from witness_base import WitnessBuilder  # type: ignore
    except ImportError as e:
        print(f"\n(witness emission skipped: qou-substrate unavailable: {e})")
        return 0

    # The `hasattr(wb, ...)` guards that used to wrap each of these are gone.
    # They are the same silent-skip pattern as the swallow above: had
    # `wb.write` been guarded too, it would have quietly emitted nothing
    # instead of raising, and this bug would still be invisible. The
    # WitnessBuilder API is in-repo and stable; call it directly and let a
    # genuine breakage surface.
    wb = WitnessBuilder("atom-dual-q0-mpfr-demo", engine="rust")
    wb.set_description(
        "End-to-end no-float64 LP dual on the H_3(q) atomic Gram: "
        "50-dps mpmath Gram/trace strings -> clarabel-MPFR. Consumer "
        "of gram_matrix_mp. Degenerate H_3 dual (y0~0); pipeline demo.")
    wb.set_audit_only("docs/audits/2026-06-16-gram-q-approximation-audit.md")
    wb.add_data("dual", res)
    # STRINGS, not floats. `add_assertion` documents this as "the drained
    # convention (qou-t0rf)" precisely so a value stays out of float64 — and
    # the old line did `abs(float(res["duality_gap"]))`, truncating an MPFR
    # decimal to f64 inside the one script whose entire purpose is the
    # no-float64 path. Measured on a populated run: 3 raw float64 fields would
    # have entered the witness (.assertions[0].computed / .expected /
    # .tolerance). The gap crosses the FFI as a decimal string; keep it one.
    with mp.workdps(50):
        gap = abs(mp.mpf(str(res.get("duality_gap", 1))))
    wb.add_assertion("strong_duality_gap_small",
                     computed=fmt(gap),
                     expected="0", tolerance="1e-6",
                     source="clarabel-MPFR on 50-dps string Gram")
    # `save()`, not `write()` — the latter has never existed on WitnessBuilder.
    # Reached only when `res` is populated, because an all-None payload would
    # emit a witness asserting `strong_duality_gap_small` about a solve that
    # never ran.
    out_path = wb.save()
    print(f"\nWitness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
