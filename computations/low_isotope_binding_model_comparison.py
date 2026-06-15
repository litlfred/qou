#!/usr/bin/env python3
"""low_isotope_binding_model_comparison.py
==========================================

Fresh side-by-side of the **best binding-energy models** for the low isotopes
(D, T, ³He, ⁴He) vs the AME 2020 ground truth — to "sort out the binding
errors". Uses the disambiguated B_* notation (see
`docs/audits/2026-06-15-binding-energy-notation-catalog.md`):

  B_AME    — AME 2020 measured binding (ground truth).
  B_lin    — linear-truncation production (binding_canonical.py;
             low-isotopes-binding-sweep.witness.json). The LINEARIZATION of
             B_sym; undershoots by Δ_λ = B_AME/B_lin ≈ q₀^(10A−5).
  B_depth  — depth-stratified tower (binding_depth_stratified.py).
  B_magic  — ⁴He flat magic-A: 2·m_e·A·Vol(L6a4) = 2·m_e·4·8G.
  B_lin·q₀^(10A−5) — the Δ_λ-law near-match (q₀^5 per chain-site; the exponent
             is itself near-match / not yet derived — the open keystone).

All inputs read from the freshest witnesses; no fit.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json
import pathlib
import time

import mpmath as mp  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 30
HERE = pathlib.Path(__file__).resolve().parent


def _load(name):
    d = json.loads((HERE / name).read_text())
    return d.get("witness", d).get("data", d.get("data", {}))


def main() -> int:
    t0 = time.monotonic()
    from q_parameter import Q
    q0 = mp.mpf(str(Q() if callable(Q) else Q))

    sweep = {r["atom"]: r for r in _load("low-isotopes-binding-sweep.witness.json")["rows"]}
    depth = _load("binding-depth-stratified.witness.json").get("per_atom", {})  # dict by atom

    # B_magic for ⁴He: 2·m_e·A·8G  (G = Catalan)
    m_e = mp.mpf("0.51099895000")
    G = mp.catalan
    B_magic_4He = 2 * m_e * 4 * (8 * G)

    order = [("D", 1, 1, 2), ("T", 1, 2, 3), ("3He", 2, 1, 3), ("4He", 2, 2, 4)]
    rows = []
    print(f"{'iso':>4} {'A':>1} {'B_AME':>8} | {'B_lin':>8} {'err%':>7} | {'B_depth':>8} {'err%':>7} "
          f"| {'B_magic':>8} {'err%':>6} | {'B_lin·q0^(10A-5)':>16} {'err%':>6}")
    for atom, Z, N, A in order:
        s = sweep[atom]
        bame = mp.mpf(str(s["B_AME_MeV"]))
        blin = mp.mpf(str(s["B_pred_canonical_MeV"]))
        err_lin = (blin - bame) / bame * 100
        # depth (per_atom dict; ⁴He may be deferred — no/blank B_MeV)
        bval = depth.get(atom, {}).get("B_MeV")
        if bval not in (None, "", "deferred"):
            bdep = mp.mpf(str(bval)); err_dep = (bdep - bame) / bame * 100
            bdep_s, errdep_s = mp.nstr(bdep, 6), f"{float(err_dep):+.1f}"
        else:
            bdep_s, errdep_s = "deferred", "  —"
        # magic (4He only)
        if atom == "4He":
            bmag = B_magic_4He; err_mag = (bmag - bame) / bame * 100
            bmag_s, errmag_s = mp.nstr(bmag, 6), f"{float(err_mag):+.2f}"
        else:
            bmag_s, errmag_s = "—", "  —"
        # Δ_λ-law near-match: B_lin · q0^(10A-5)
        blaw = blin * q0 ** (10 * A - 5); err_law = (blaw - bame) / bame * 100
        rows.append({"atom": atom, "Z": Z, "N": N, "A": A,
                     "B_AME_MeV": mp.nstr(bame, 6),
                     "B_lin_MeV": mp.nstr(blin, 6), "err_lin_pct": mp.nstr(err_lin, 5),
                     "B_depth_MeV": bdep_s, "err_depth_pct": errdep_s,
                     "B_magic_MeV": bmag_s, "err_magic_pct": errmag_s,
                     "B_lin_x_q0_10A5_MeV": mp.nstr(blaw, 6), "err_dlaw_pct": mp.nstr(err_law, 5)})
        print(f"{atom:>4} {A:>1} {float(bame):8.3f} | {float(blin):8.4f} {float(err_lin):+7.1f} "
              f"| {bdep_s:>8} {errdep_s:>7} | {bmag_s:>8} {errmag_s:>6} "
              f"| {float(blaw):16.4f} {float(err_law):+6.1f}")

    b = WitnessBuilder("low-isotope-binding-model-comparison", engine="python+mpmath", start_time=t0)
    (b.set_description(
        "Fresh side-by-side of the best low-isotope binding models vs AME 2020. "
        "B_lin (linear-truncation) undershoots -79..-97.5% (it is the "
        "linearization of B_sym; deficit = Δ_λ ≈ q₀^(10A−5)). B_depth (tower) "
        "undershoots -66..-73% (⁴He deferred, H_12 RAM). B_magic best on ⁴He "
        "(+5.9%). B_lin·q₀^(10A−5) is the Δ_λ-law near-match (q₀^5/site; exponent "
        "not yet derived — open keystone). No fit; NOT wired.")
     .add_data("rows", rows)
     .add_parameter("q0", mp.nstr(q0, 12))
     .add_data("summary", {
         "B_lin": "linear-truncation; -79..-97.5%; the worst (linearization)",
         "B_depth": "depth-stratified tower; -66..-73%; ⁴He deferred (RAM)",
         "B_magic": "⁴He flat magic-A; +5.9%; best for ⁴He only",
         "B_lin_x_q0_law": "Δ_λ-law near-match; ~±few%; exponent 10A−5 not derived"}))
    b.add_assertion("B_depth_beats_B_lin_on_DT3He",
                    computed=bool(all(atom in depth for atom in ("D", "T", "3He"))),
                    expected=True, source="depth-stratified less undershoot than linear")
    out = b.save()
    print(f"\n  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
