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
import sys
from pathlib import Path

# `pyhecke` lives outside `computations/`, so `_path_bridge` (which only wires
# the computations/ cluster dirs) does not reach it. Same TOOLS idiom the other
# pyhecke consumers in this directory use — without it this module raised
# ModuleNotFoundError on import, which is why it was the one mp-path consumer
# that could not be re-run during the convention-D migration (bean qou-cds2).
_TOOLS = Path(__file__).resolve().parent.parent / "tools" / "pyhecke" / "python"
sys.path.insert(0, str(_TOOLS))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401
# `_path_bridge` must come BEFORE pyhecke: `gram.py` resolves the substrate
# constants as `q_parameter` first (it lives in computations/substrate/, which
# only the bridge puts on sys.path) and falls back to the `qou_substrate`
# package otherwise — and that package is not installed here, so without the
# bridge the fallback raises too.

from pyhecke import gram  # noqa: E402


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


def main():
    res = solve_atom_dual_q0_mpfr()
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
    #
    # This block used to be a wall of `hasattr` guards inside a bare
    # `except Exception`, so every failure printed "(witness emission
    # skipped: …)" and the module exited 0. It had THREE defects at once and
    # reported none of them (bean qou-cds2):
    #
    #   1. `wb.write(name)` does not exist — the API is `wb.save()`, with the
    #      name given to the constructor. Straight API drift.
    #   2. `float(res["duality_gap"])` raises when the solver did not run,
    #      because every field is None then.
    #   3. the `hasattr` guards meant a mistyped method name would silently
    #      no-op rather than fail — the same "cannot fail loudly" shape as
    #      `mp.lu_solve` on the singular D Gram.
    #
    # None of it surfaced because the module could not even be imported
    # (`from pyhecke import gram` with no sys.path wiring), so nobody ran it.
    sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402

    if res.get("duality_gap") is None:
        print("\n  ⛔ NO WITNESS EMITTED — the clarabel-MPFR binary was not found,")
        print("     so every LP field above is None. Build")
        print("     tools/hecke-engine/target/release/clarabel-operator-selection-lp")
        print("     and re-run. Emitting a witness of Nones would record an")
        print("     absent solver as a computed result.")
        return 2

    wb = WitnessBuilder("atom-dual-q0-mpfr-demo", engine="rust")
    wb.set_description(
        "End-to-end no-float64 LP dual on the H_3(q) atomic Gram: "
        "50-dps mpmath Gram/trace strings -> clarabel-MPFR. Consumer "
        "of gram_matrix_mp (convention D since 2026-08-19). Degenerate "
        "H_3 dual (y0~0); pipeline demo.")
    wb.set_audit_only("docs/audits/2026-06-16-gram-q-approximation-audit.md")
    wb.add_data("dual", res)
    wb.add_assertion("strong_duality_gap_small",
                     computed=abs(float(res["duality_gap"])),
                     expected=0.0, tolerance=1e-6,
                     source="clarabel-MPFR on 50-dps string Gram")
    print(f"\nWitness: {wb.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
