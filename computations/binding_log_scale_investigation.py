#!/usr/bin/env python3
"""
binding_log_scale_investigation.py — can a DERIVED scale close A≥3
binding with the extensive log-observable? (No AME back-fitting.)

Following the error-source diagnosis (binding_error_source.py): Δtr is
intensive (ceiling ~3.74 MeV); -log(tr_atom/tr_free) is extensive.
This script tests whether any DERIVED categorical scale κ makes
B = κ · log(tr_free/tr_atom) match AME — evaluating derived constants
only, never fitting κ to binding data.

RESULT (definitive negative):
  The κ each isotope NEEDS (B_AME / log-ratio) is NOT constant —
  2.39, 3.92, 4.75, 9.89 MeV (313% spread). No single derived scale
  works. The log observable fixes the Δtr CEILING (it grows with A)
  but its GROWTH RATE is too slow.

DEEPER FINDING:
  κ_needed tracks B/A (1.11, 2.83, 2.57, 7.07 — ⁴He is doubly magic),
  while log-ratio/A is nearly flat (~0.5-0.7). So the SCALAR (collapsed)
  Markov trace does not carry the per-nucleon shell variation.

REFINEMENT (2026-05-29, shell review): the earlier wording
"MISSING-STRUCTURE problem, not a scale problem" was too strong on both
counts. (1) Shell structure is NOT missing from the framework — it is
recoverable from the PER-λ Wedderburn decomposition χ^λ(β_K)
(atom-chi-rust-*.witness.json; chi-lambda-he4-full-partition-table:
self_conjugate_count=3, conjugate_pair_count=37), self-conjugate/magic
labels, the staircase λ_shell, and the torus-knot inter-shell q^{2n_s}
gap. The scalar log-ratio collapses that per-λ structure into one number.
(2) It is also partly a scale problem at A=2: sibling PR #1416 finds
E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV closes the DEUTERON to +12% (+0.7% with
1−ℏ_q), and the scalar endomorphism m_e·Vol(𝓑₃)·Δtr closes it to +0.19%.
What stands unchanged: no single DERIVED κ closes the LOG observable
across D/T/³He/⁴He (κ_needed spans 313%) — because the log-ratio is the
collapsed scalar, not the shell-resolved per-λ object.

BOUNDARY: the framework cleanly predicts DEUTERON binding (true 2-body,
+0.19% via the scalar endomorphism). A≥3 binding needs the per-λ /
inter-shell structure the scalar trace discards — an open problem, not a
missing observable. Stated without fitting and without masking.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, log, catalan, clsin, pi

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import (  # noqa: E402
    Q_BETA_MEV, M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION as Bd,
    AME_B_TRITIUM_MEV_VALIDATION as Bt,
    AME_B_HE3_MEV_VALIDATION as B3,
    AME_B_HE4_MEV_VALIDATION as B4,
)
from binding_canonical import binding_canonical  # noqa: E402


def _real(s):
    # Full-precision real part — never via float64 complex() (precision ban).
    s = str(s).strip("()")
    try:
        return mpf(s)
    except (ValueError, TypeError):
        body = s[:-1] if s.endswith("j") else s  # complex repr "a±bj"
        for i in range(len(body) - 1, 0, -1):
            if body[i] in "+-" and body[i - 1] not in "eE":
                return mpf(body[:i] or "0")
        return mpf("0")


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-log-scale-investigation", engine="mpmath")

    q = Q_MP
    m_e = mpf(str(M_E_MEV))
    VOL = 8 * catalan
    hbar = (q - 1) / q
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

    cases = [("D", 1, 1, Bd), ("T", 1, 2, Bt), ("3He", 2, 1, B3), ("4He", 2, 2, B4)]
    data = {}
    for iso, Z, N, ame in cases:
        r = binding_canonical(Z, N, Q_beta_n_mev=float(Q_BETA_MEV),
                              use_closed_form=True, verbose=False)
        tf = fabs(_real(r["tr_M_free"]))
        ta = fabs(_real(r["tr_M_atom"]))
        data[iso] = {"log_ratio": log(tf / ta), "ame": mpf(str(ame)),
                     "A": Z + N}

    # derived scale candidates (NO fit)
    cands = {
        "E0": E0,
        "m_e*Vol(B3)": m_e * VOL,
        "m_e*Vol(4_1)": m_e * 2 * clsin(2, pi / 3),
    }

    print("=" * 70)
    print("LOG-OBSERVABLE SCALE TEST: B = κ·log(tr_free/tr_atom), derived κ")
    print("=" * 70)
    print(f"{'κ':16s} {'MeV':>9s} | " + "  ".join(f"{i:>6s}" for i in data))
    cand_results = {}
    for name, k in cands.items():
        errs = {iso: float((k * d["log_ratio"] - d["ame"]) / d["ame"] * 100)
                for iso, d in data.items()}
        cand_results[name] = {"kappa_MeV": mp.nstr(k, 8), "err_pct": errs}
        print(f"{name:16s} {float(k):>9.4f} | "
              + "  ".join(f"{errs[i]:>+5.0f}%" for i in data))

    # κ needed per isotope — constant ⟹ derivable
    print()
    print("κ needed (B/log) and B/A:")
    needed = {}
    for iso, d in data.items():
        k_need = d["ame"] / d["log_ratio"]
        b_per_a = d["ame"] / d["A"]
        needed[iso] = {"kappa_needed_MeV": mp.nstr(k_need, 8),
                       "B_per_A_MeV": mp.nstr(b_per_a, 6),
                       "log_per_A": mp.nstr(d["log_ratio"] / d["A"], 6)}
        print(f"  {iso:4s}: κ_need={float(k_need):.3f}  "
              f"B/A={float(b_per_a):.2f}  log/A={float(d['log_ratio']/d['A']):.3f}")

    ks = [float(d["ame"] / d["log_ratio"]) for d in data.values()]
    spread = (max(ks) / min(ks) - 1) * 100
    print()
    print(f"κ_needed spread = {min(ks):.2f}–{max(ks):.2f} MeV ({spread:.0f}%).")
    print("NOT constant ⟹ no single derived κ closes the LOG observable.")
    print("κ_need tracks B/A; the SCALAR log-ratio collapses the per-λ shell")
    print("structure (recoverable from per-λ χ^λ). Refinement 2026-05-29:")
    print("not 'missing structure' — the scalar projection discards it; and a")
    print("~4 MeV scale (E₀ / m_e·Vol(𝓑₃)) closes the deuteron (see #1416).")

    wb.set_description(
        "Tests whether a DERIVED scale κ closes A≥3 binding with the "
        "log-observable B = κ·log(tr_free/tr_atom). Negative for this SCALAR "
        f"observable: κ_needed spans {min(ks):.2f}–{max(ks):.2f} MeV ({spread:.0f}% "
        "spread), tracking B/A. Refinement (2026-05-29 shell review): the shell "
        "structure is NOT missing — it is recoverable per-λ (χ^λ Wedderburn, "
        "self-conjugate/magic, staircase λ_shell, torus-knot q^{2n_s} gap); the "
        "scalar log-ratio collapses it. A ~4 MeV scale (E₀ / m_e·Vol(𝓑₃)) closes "
        "the deuteron (sibling PR #1416). A≥3 needs the per-λ / inter-shell "
        "object the scalar trace discards — open, not a missing observable."
    )
    wb.add_data("derived_scale_tests", cand_results)
    wb.add_data("kappa_needed", needed)
    wb.add_data("kappa_spread_pct", spread)
    wb.add_data("conclusion", {
        "scalar_log_scale_derivable": False,
        "reason": "no single κ closes the SCALAR log-observable (313% spread); κ tracks B/A",
        "refinement_2026_05_29": "shell structure NOT missing — recoverable per-λ "
            "(χ^λ Wedderburn); scalar log-ratio collapses it. A ~4 MeV scale closes D (#1416).",
        "boundary": "deuteron closes (+0.19% scalar endomorphism); A≥3 needs the "
                    "per-λ / inter-shell structure the scalar trace discards — open problem",
    })
    wb.add_assertion(
        "no_derived_scale_closes_A3",
        computed=round(spread, 1),
        expected=313.0,
        tolerance=1.0,
        source="κ_needed spread ≫ 0 ⟹ no single derived scale works",
    )
    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
    wb.add_data("lean_uniqueness_ref", {
        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
        "framework_doc":
            "folio/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    wb.save()


if __name__ == "__main__":
    main()
