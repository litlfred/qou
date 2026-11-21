#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; per-block magnitude probe.
"""Per-block-magnitude binding — does the operator-valued (don't-collapse-
blocks-before-|·|) form that closes the DEUTERON extend to A=3?

VERDICT: NO. The per-block form closes A=2 (+3.6 %) but fails A=3 the same
way every other reading does (T −61.7 %, ³He −55.1 %). Recorded as a
negative result so the per-block / superselection theorem is NOT formalized
(it would be false for A≥3).

Two parameter-free readings of `B = E_0·(tr_M(W_free) − tr_M(W_atom))`
differ only in where |·| sits relative to the Wedderburn sum:

  scalar (collapse first):   B = E_0·( |Σ_λ y_λ χ^λ(free)| − |Σ_λ y_λ χ^λ(atom)| )
  per-block (operator-valued): B = E_0·( Σ_λ y_λ|χ^λ(free)| − Σ_λ y_λ|χ^λ(atom)| )

Motivation: the per-block form is the "Wedderburn blocks are superselection
sectors → observe |·| per sector, sum incoherently" reading (the natural
extension of the q₀-real bar/modulus result). It closes the deuteron, so
the hypothesis was worth testing. It does NOT close A=3 → refuted.

NO per-partition Δ_λ is introduced; every factor (y_λ, χ^λ, E_0=CAL-3) is
already derived. χ^λ is read from the cached Rust kernel witnesses
(atom-chi-rust-{d,t,3he}.witness.json, ~0.02 s each — pure-Python
chi_lambda_numerical at H_9 is intractable). EXPLORATORY; no fit.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: E402, F401

from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402 — CAL-1
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

set_compute_dps(30)                              # exploratory; ~%-level effect
q0 = mp.mpf(str(Q0))
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))      # 𝔈₀ ≈ 4.186 MeV (CAL-3)

ISO = {"d": (6, _ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)), "t": (9, "8.4818"), "3he": (9, "7.7180")}


def _mpf(v):
    """Witness numerics are a 50-dps STRING post-migration, a float before it.
    `mp.mpf(repr(v))` is right for a float — repr round-trips all 17 digits —
    but on a string it yields `mpf("\'155…\'")`, quotes included, which mpmath
    rejects outright. Reading the string directly is also strictly better: it
    carries 50 digits where the float carried 17."""
    return mp.mpf(v) if isinstance(v, str) else mp.mpf(repr(v))


def _read_chi(iso: str):
    """{cfg: [(partition_tuple, χ^λ), ...]} for free and atom from the cached
    Rust-kernel witness."""
    with open(HERE / f"atom-chi-rust-{iso}.witness.json") as _fh:
        dat = json.load(_fh)["data"]
    return {cfg: [(tuple(e["partition"]), _mpf(e["chi_lambda"]))
                  for e in dat[cfg]["by_partition"]]
            for cfg in ("free", "atom")}


def main() -> int:
    print(f"E_0 = {float(E0):.4f} MeV   q₀ = {float(q0):.6f}\n")
    print(f"{'iso':<5}{'B_perblk':<11}{'B_scalar':<11}{'AME':<9}"
          f"{'perblk%':<10}{'scalar%':<9}")
    results = {}
    for iso, (n, ame_s) in ISO.items():
        ydict = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
                 for k, v in y_lambda_at(n, q0).items()}
        chi = _read_chi(iso)

        def reading(cfg):
            pb = mp.mpf(0)
            sc = mp.mpf(0)
            for lam, c in chi[cfg]:
                y = ydict.get(tuple(lam))
                if y is None:
                    continue
                pb += y * abs(c)
                sc += y * c
            return pb, abs(sc)

        pf, sf = reading("free")
        pa, sa = reading("atom")
        Bpb = E0 * (pf - pa)
        Bsc = E0 * (sf - sa)
        A = mp.mpf(ame_s)
        epb = (Bpb - A) / A
        esc = (Bsc - A) / A
        results[iso] = {
            "B_perblock_MeV": float(Bpb), "B_scalar_MeV": float(Bsc),
            "AME_MeV": float(A), "err_perblock": float(epb),
            "err_scalar": float(esc), "n_strands": n,
        }
        print(f"{iso:<5}{float(Bpb):<11.4f}{float(Bsc):<11.4f}{float(A):<9.4f}"
              f"{float(epb)*100:<+10.1f}{float(esc)*100:<+9.1f}")

    wb = WitnessBuilder("binding-per-block-magnitude-a3", engine="mpmath")
    wb.data["q_0"] = str(Q0)
    wb.data["E0_MeV"] = float(E0)
    wb.data["results"] = results
    wb.data["chi_source"] = "atom-chi-rust-{d,t,3he}.witness.json (Rust kernel)"
    wb.data["verdict"] = (
        "per-block magnitude closes A=2 (+3.6%) but FAILS A=3 "
        "(T -61.7%, 3He -55.1%) — same ~-60% as all other readings. "
        "Operator-valued blockwise |.| is NOT the A>=3 closure. Negative result.")
    # Assertion encodes the verdict: A=3 per-block stays badly off (>20%),
    # so the per-block-closes-A3 hypothesis is recorded as FALSE.
    wb.add_assertion("a3_perblock_does_not_close",
                     computed=1 if abs(results["t"]["err_perblock"]) > 0.20 else 0,
                     expected=1, tolerance=0)
    wb.save()
    print("\n✓ Witness: binding-per-block-magnitude-a3.witness.json")
    print("  VERDICT: per-block magnitude closes A=2 only; A=3 stays ~−60%.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
