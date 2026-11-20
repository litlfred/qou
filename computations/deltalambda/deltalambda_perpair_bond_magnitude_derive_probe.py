#!/usr/bin/env python3
"""Δ_λ gate — FORWARD test of the parameter-free per-pair bond magnitude m.

THE ONE REMAINING GATED SCALAR.  Everything AROUND the ≥4-body [1⁴] term is
already DERIVED (merged #3924, b4_slater_antisymmetrizer_exchange_sign.py):
  • ⁴He-locality  C(4,A)=0 for A>4  (exact, q-independent);
  • exchange spectrum eig(S)={±√5,±1} ⇒ det(I+mS)=(1−5m²)(1−m²) (closed form);
  • attractive sign (a negative eigenvalue −√5·m is present for any m);
  • physicality ceiling m < 1/√5 = 0.447214 (= the derived writhe cap).
The single undetermined quantity is the PER-PAIR BOND MAGNITUDE m — the Δ_λ gate.

TARGET (the many-body wall).  The single-trace Δ_λ = (−1)^{n(λ)}·dim binding
B_dim UNDERSHOOTS the AME connected binding; the residual target/|B_dim| is
{²H 5.85, ³H 4.44, ³He 3.29, ⁴He 9.31} (committed
deltalambda-o1-manybody-residual.witness.json — NOT recomputed, consumed as a
derived-elsewhere input, like AME).  The ≥4-body det term b = −ln det(I+G) must
supply the DEFICIT (target − B_dim).

THE ONLY ALLOWED (NON-FIT) METHOD.  Compute m PARAMETER-FREE from the categorical
link data, then CHECK it against the four residuals FORWARD — never invert them.
The corpus supplies exactly two parameter-free per-pair magnitudes:
  • z_naive = 1/[2]_v = 1/(√q+1/√q) ≈ 0.499317  — the Markov-peel bond factor;
  • g_reeb  = 1/√(5+(q₀−1)²/q₀) ≈ 0.446727     — the CWF/sine-normalized value.
(No third exists: the classical ceiling 1/√5 is the det=0 boundary where
−ln det diverges; the tangent/sine relation collapses g = z/√(1+z²).)

THE NON-FIT TEST (forward-only).  For EACH parameter-free m (no tuning), evaluate
the exchange determinant on the complete graph K_A of each isotope
(pp=+1, nn=−1 derived signs; pn=±1 det-invariant by diag(1,1,−1,−1) conjugation,
Lean-proved ReebPnMagnitude.lean) and ask whether ONE m reproduces ALL FOUR
deficits SIMULTANEOUSLY.  A genuine derivation matches four isotopes with zero
free parameters; a miss (the expected outcome after six failed ansätze) is an
honest NEGATIVE — the gate stands.

STRICT (AGENTS.md).  Solving for m from the residuals would be the forbidden
seventh fit-based ansatz.  This probe NEVER does that: m is fixed parameter-free
FIRST, the residual is PREDICTED, and only then compared.  No wiring, no AME
inversion, audit-only.

  -- Ref: b4_slater_antisymmetrizer_exchange_sign.py (locality/sign/ceiling, #3924);
     b4_1four_reeb_flow_magnitude.py (g_reeb at A=2,4);
     deltalambda_o1_manybody_probe.py (B_dim residual {5.9,4.4,3.3,9.3});
     docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md;
     QOU/MassTheory/ReebPnMagnitude.lean (pn-sign det invariance; 1/√5 ceiling).
EXPLORATORY — audit + witness only; no production wiring, no fit, no AME inversion.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from _li_2_q_util import load_q_50dps  # noqa: E402
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.experimental_constants import M_E_MEV  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from codata_constants import AME_B_HE3_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)

set_compute_dps()
COMP = str(_COMP)

# ── Derived-elsewhere inputs (consumed, NOT recomputed, NOT fitted) ──────────
# Single-trace Δ_λ=(−1)^{n(λ)}dim binding |B_dim| and AME target, per isotope,
# from the committed deltalambda-o1-manybody-residual.witness.json (#3542 sign,
# q-hook dim).  Sign convention there is target<0; magnitudes below.
ISO = ["2H", "3H", "3He", "4He"]
A_OF = {"2H": 2, "3H": 3, "3He": 3, "4He": 4}
B_DIM = {  # |B_dim| MeV, single-trace undershoot
    "2H": mp.mpf("0.38007125148431475"),
    "3H": mp.mpf("1.9085327584765543"),
    "3He": mp.mpf("2.3446056813751914"),
    "4He": mp.mpf("3.0381869604868865"),
}
B_AME = {  # AME2020 connected binding MeV
    "2H": AME_B_DEUTERON_MEV_VALIDATION,
    "3H": AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}

# Complete-graph nucleon-type layout per isotope (pp=+1, nn=−1 derived; pn=±1
# det-invariant — we use +1, isospectral to −1 by diag(1,1,−1,−1) conjugation).
TYPES = {"2H": ["p", "n"], "3H": ["p", "n", "n"],
         "3He": ["p", "p", "n"], "4He": ["p", "p", "n", "n"]}


def _det_I_plus_G(types, w_pn, m):
    """det(I + m·S) on the complete graph of `types` (list of 'p'/'n').
    pp=+1, nn=−1 (derived signs); pn = w_pn. Zero diagonal, symmetric."""
    n = len(types)
    S = mp.zeros(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            ti, tj = types[i], types[j]
            if ti == tj:
                s = 1 if ti == "p" else -1
            else:
                s = w_pn
            S[i, j] = S[j, i] = s * m
    return mp.det(mp.eye(n) + S)


def det_term_mev(iso, m, E0):
    """b(iso) = E0·(−ln det(I+G)) on the isotope's complete graph, at magnitude m.
    Returns (det, MeV or None if unphysical det≤0)."""
    d = _det_I_plus_G(TYPES[iso], +1, m)
    if d <= 0:
        return d, None
    return d, E0 * (-mp.log(d))


def main() -> int:
    t0 = time.monotonic()
    q, qi, z = load_q_50dps()
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)                       # substrate energy unit (MeV)

    # ── the two parameter-free per-pair magnitudes (fixed FIRST, no tuning) ──
    z_naive = z                                    # 1/[2]_v Markov bond factor
    g_reeb = mp.mpf(1) / mp.sqrt(mp.mpf(5) + (q - 1) ** 2 / q)
    ceiling = mp.mpf(1) / mp.sqrt(5)
    candidates = {"z_naive": z_naive, "g_reeb": g_reeb}

    # deficit the det term must supply, per isotope
    deficit = {iso: B_AME[iso] - B_DIM[iso] for iso in ISO}

    # ── forward evaluation: one m → four predicted det-terms → four ratios ──
    per_candidate = {}
    for name, m in candidates.items():
        physical_all = True
        rows = []
        ratios_deficit = []
        for iso in ISO:
            d, mev = det_term_mev(iso, m, E0)
            if mev is None:
                physical_all = False
                rows.append({"iso": iso, "A": A_OF[iso], "det_I_plus_G": mp.nstr(d, 8),
                             "det_term_MeV": None, "status": "UNPHYSICAL (det<=0)"})
                ratios_deficit.append(None)
                continue
            r_def = mev / deficit[iso]             # det-term / (target − B_dim)
            r_ame = mev / B_AME[iso]               # det-term / target  (corpus §2i)
            r_tot = (B_DIM[iso] + mev) / B_AME[iso]  # (B_dim + det-term) / target
            ratios_deficit.append(r_def)
            rows.append({
                "iso": iso, "A": A_OF[iso],
                "det_I_plus_G": mp.nstr(d, 8),
                "det_term_MeV": mp.nstr(mev, 8),
                "deficit_MeV": mp.nstr(deficit[iso], 8),
                "det_term/deficit": mp.nstr(r_def, 6),
                "det_term/AME": mp.nstr(r_ame, 6),
                "(B_dim+det)/AME": mp.nstr(r_tot, 6),
            })
        # spread of the deficit-ratio across the four isotopes (1.0 = perfect
        # simultaneous match; a genuine parameter-free derivation gives ≈const).
        if physical_all:
            rd = ratios_deficit
            spread = max(rd) / min(rd)
            const_match = bool(spread < mp.mpf("1.05"))   # ≤5% would be a hit
            # mirror-pair diagnostic: ³H vs ³He share B_dim topology; a per-pair
            # magnitude that "derives" the deficit must give ≈equal deficit-ratios.
            mirror_ratio = rd[1] / rd[2]                  # 3H / 3He
        else:
            spread = None
            const_match = False
            mirror_ratio = None
        per_candidate[name] = {
            "magnitude": mp.nstr(m, 18),
            "below_ceiling_1/sqrt5": bool(m < ceiling),
            "physical_all_four": physical_all,
            "rows": rows,
            "deficit_ratio_spread_max/min": (None if spread is None else mp.nstr(spread, 6)),
            "simultaneous_const_match_le5pct": const_match,
            "mirror_3H/3He_deficit_ratio": (None if mirror_ratio is None else mp.nstr(mirror_ratio, 6)),
        }

    # ── verdict ──────────────────────────────────────────────────────────────
    z_excluded = not per_candidate["z_naive"]["physical_all_four"]
    g_match = per_candidate["g_reeb"]["simultaneous_const_match_le5pct"]
    verdict = (
        "HONEST NEGATIVE — the Delta_lambda per-pair magnitude gate STANDS. "
        "The parameter-free palette is exhausted: z_naive is UNPHYSICAL at A=4 "
        "(det<=0, exceeds the 1/sqrt5 ceiling) so it cannot supply the 4He deficit at "
        "all; g_reeb is physical for all four but does NOT reproduce the four "
        "deficits simultaneously — the det-term/deficit ratios are non-monotone "
        "and spread by ~2.5x (the 3H/3He mirror pair, identical B_dim topology, "
        "splits ~2.3x while their deficits differ only ~1.2x). No single "
        "parameter-free m matches all four; the residual is a collective, "
        "non-additive many-body object, not a per-pair det-term at a fixed "
        "categorical magnitude. NOT a derivation; NOT wired; m NOT solved-for "
        "from the residuals (that would be the forbidden 7th fit)."
    ) if (z_excluded and not g_match) else (
        "UNEXPECTED POSITIVE — a parameter-free magnitude reproduces all four "
        "deficits within 5%. FLAG FOR OWNER REVIEW (do not auto-wire; verify the "
        "match is not coincidental per the entropy-bound discipline)."
    )

    result = {
        "gate": ("the ONE remaining gated Delta_lambda scalar = per-pair bond magnitude m; "
                 "locality/sign/ceiling already DERIVED (#3924)"),
        "constants": {
            "q0": mp.nstr(q, 12),
            "E0_MeV_m_e/(q(q-1))": mp.nstr(E0, 8),
            "z_naive_1/[2]_v": mp.nstr(z_naive, 12),
            "g_reeb_1/sqrt(5+(q0-1)^2/q0)": mp.nstr(g_reeb, 12),
            "ceiling_1/sqrt5": mp.nstr(ceiling, 12),
        },
        "derived_inputs_not_fitted": {
            "B_dim_MeV_single_trace": {k: mp.nstr(v, 8) for k, v in B_DIM.items()},
            "B_AME_MeV": {k: mp.nstr(v, 8) for k, v in B_AME.items()},
            "residual_target_over_Bdim": {k: mp.nstr(B_AME[k] / B_DIM[k], 4) for k in ISO},
            "deficit_MeV_target_minus_Bdim": {k: mp.nstr(deficit[k], 8) for k in ISO},
            "source": "deltalambda-o1-manybody-residual.witness.json (consumed, not recomputed)",
        },
        "forward_test_per_candidate": per_candidate,
        "method_guard": ("m fixed PARAMETER-FREE first; deficit PREDICTED; compared FORWARD. "
                         "No inversion of the residuals (would be the forbidden 7th fit-based ansatz, "
                         "AGENTS.md Delta_lambda gate)."),
        "verdict": verdict,
    }

    payload = {
        "computation": "deltalambda-perpair-bond-magnitude-derive",
        "description": (
            "Forward (non-fit) test of the parameter-free per-pair bond magnitude m "
            "— the one remaining gated Delta_lambda scalar. Both corpus parameter-free "
            "magnitudes (z_naive, g_reeb) evaluated on the complete-graph exchange "
            "determinant of 2H/3H/3He/4He and checked against the four deficits "
            "target-B_dim SIMULTANEOUSLY. z excluded (unphysical at A=4); g_reeb "
            "physical but non-monotone (mirror split) => no single parameter-free m "
            "closes; the Delta_lambda magnitude gate stands. No fit, no wiring, no inversion."
        ),
        "tier": "structural forward-test (parameter-free m -> predicted residual -> compare; no tuning)",
        "result": result,
        "context": {
            "axis": "Delta_lambda Track-A gate — the per-pair [1^4] bond magnitude m",
            "no_fit": True,
            "no_ame_inversion": True,
            "q0_convention": "proton (experimental / Physical-Observations pin; owner directive 2026-08-07). Corrected from 'muon-canonical (computations/ layer)' on 2026-09-04, bean qou-9ugp: the label named a layer this producer does not evaluate at.",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "deltalambda-perpair-bond-magnitude-derive", payload,
        script_path=__file__, engine="python+mpmath",
        output_dir=os.path.join(COMP, "deltalambda"), start_time=t0,
    )
    wb.add_assertion("z_naive_unphysical_at_A4",
                     computed=str(z_excluded), expected="True")
    wb.add_assertion("g_reeb_below_ceiling",
                     computed=str(bool(g_reeb < ceiling)), expected="True")
    wb.add_assertion("g_reeb_physical_all_four",
                     computed=str(per_candidate["g_reeb"]["physical_all_four"]), expected="True")
    wb.add_assertion("g_reeb_no_simultaneous_match",
                     computed=str(not g_match), expected="True")
    out = wb.save(extra={"auditOnly": True})

    # ── console report ──
    print("=== Delta_lambda per-pair bond magnitude — FORWARD (non-fit) test ===")
    print(f"  q0={float(q):.6f}  E0={float(E0):.4f} MeV  ceiling 1/sqrt5={float(ceiling):.6f}")
    print(f"  parameter-free magnitudes: z_naive={float(z_naive):.6f}  g_reeb={float(g_reeb):.6f}")
    print("  residual target/|B_dim| = " +
          "  ".join(f"{iso}:{float(B_AME[iso]/B_DIM[iso]):.2f}" for iso in ISO))
    for name in ("z_naive", "g_reeb"):
        pc = per_candidate[name]
        print(f"\n  --- m = {name} = {pc['magnitude'][:8]} "
              f"(physical all four: {pc['physical_all_four']}) ---")
        print(f"    {'iso':4} {'A':>1}  {'det(I+G)':>12} {'det_term':>10} {'deficit':>9} "
              f"{'det/def':>8} {'det/AME':>8}")
        for r in pc["rows"]:
            if r["det_term_MeV"] is None:
                print(f"    {r['iso']:4} {r['A']:>1}  {r['det_I_plus_G']:>12} "
                      f"{'--':>10} {'--':>9}  UNPHYSICAL (det<=0)")
            else:
                print(f"    {r['iso']:4} {r['A']:>1}  {r['det_I_plus_G']:>12} "
                      f"{float(mp.mpf(r['det_term_MeV'])):>10.3f} "
                      f"{float(mp.mpf(r['deficit_MeV'])):>9.3f} "
                      f"{float(mp.mpf(r['det_term/deficit'])):>8.3f} "
                      f"{float(mp.mpf(r['det_term/AME'])):>8.3f}")
        if pc["physical_all_four"]:
            print(f"    deficit-ratio spread max/min = {pc['deficit_ratio_spread_max/min']}  "
                  f"(≈1.0 required for a parameter-free derivation; "
                  f"3H/3He mirror ratio = {pc['mirror_3H/3He_deficit_ratio']})")
    print("\n  VERDICT:", verdict)
    print("  witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
