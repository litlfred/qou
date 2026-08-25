"""Extend Habiro mass table to the 3 open even-A mirror pairs.

Extracts canonical Phase 5q Habiro coefficients for ⁶He, ¹²N, ¹²B,
¹⁴O, ¹⁴C — the 5 atoms required to test the open even-A predictions
in `docs/audits/2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md`:

  | Pair      | A   | Original A−1 | Refined 2⌊(A−1)/2⌋ |
  |-----------|-----|--------------|---------------------|
  | ⁶He−⁶Be   |  6  |      5       |          4          |
  | ¹²N−¹²B   | 12  |     11       |         10          |
  | ¹⁴O−¹⁴C   | 14  |     13       |         12          |

The extracted Habiro coefficients are composed into the mirror
difference Σ_m Δa_m(X−Y)·(u;u)_m and factored over ℤ[u]; the
cyclotomic multiplicity of Φ_8 = u⁴+1 is read off.

A pass on the refined law (mult = A−2 for these even A) further
corroborates 2⌊(A−1)/2⌋ across A=6, 12, 14.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _habiro_coefficient_extract import (  # noqa: E402
    analyse_atom,
    _load_p_n_symbolic,
    _write_witness,
)
from q_parameter import Q_MP as _Q_CANONICAL  # noqa: E402
from q_parameter import Q_50_DIGIT_STR as _Q_CANONICAL_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()  # idempotent; before any mpf is built from a decimal string
from witness_base import WitnessBuilder  # noqa: E402
from habiro_coefficients_atomic import load_a_m as _load_a_m  # noqa: E402
from habiro_coefficients_atomic import mirror_trace_diff_numerator as _mirror_trace_diff  # noqa: E402 — shared loader; refuses a self-failed witness (qou-s41x)


EVEN_A_OPEN = [
    ("⁶He (helium-6, A=6)",     "helium-6",    2, 4,  96),
    ("¹²N (nitrogen-12, A=12)", "nitrogen-12", 7, 5, 192),
    ("¹²B (boron-12, A=12)",    "boron-12",    5, 7, 192),
    ("¹⁴O (oxygen-14, A=14)",   "oxygen-14",   8, 6, 224),
    ("¹⁴C (carbon-14, A=14)",   "carbon-14",   6, 8, 224),
]


def main() -> int:
    t0 = time.perf_counter()
    q0_float = float(_Q_CANONICAL)
    # Sourced from the canonical 50-digit string, not `str(<mpf>)`, for the
    # reason recorded on the same line of _habiro_coefficient_extract.main:
    # `str()` of an mpf renders at the *live* mp.dps, so the digits kept
    # depended on ambient precision. Importing that module now calls
    # set_compute_dps() as a side effect, which happens to make the old form
    # correct here — which is exactly why it is not left as it was. An
    # invariant that holds because of another module's import order is one
    # edit away from silently not holding (bean qou-j6gb).
    q0_mp = mp.mpf(_Q_CANONICAL_STR)

    print("=" * 78)
    print(" EVEN-A OPEN MIRROR PAIRS — EXTRACT + Φ_8 SCALING TEST")
    print("=" * 78)
    print(f"q_0 = {q0_float:.16f}")

    habiro_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    q = sp.Symbol('q', positive=True, real=True)
    print("\nLoading symbolic τ_p, τ_n …")
    tau_p, tau_n = _load_p_n_symbolic(habiro_path, q)

    reference_blocks = [
        "def:habiro-ring",
        "prop:full-pole-structure-mass-trace",
        "prop:constit-factor-tau-M-proton-identity",
        "prop:interface-knot-markov-z",
        "thm:knot-mass-formula-unified",
    ]
    description_tpl = (
        "Canonical Phase 5q Habiro coefficients for {label}. "
        "Strict-mirror partner for the refined 2⌊(A−1)/2⌋ scaling-law "
        "test on the open even-A pairs (⁶He−⁶Be, ¹²N−¹²B, ¹⁴O−¹⁴C)."
    )

    extracted: dict[tuple[int, int], dict] = {}
    for label, slug, Z, N, max_m in EVEN_A_OPEN:
        t = time.perf_counter()
        try:
            body = analyse_atom(label, Z, N, q, tau_p, tau_n, q0_mp,
                                 max_m=max_m)
            if body is None or "habiro_coefficients" not in body:
                print(f"  ✗ analyse_atom returned empty body for {label}")
                continue
            path = HERE / f"habiro-coefficients-{slug}.witness.json"
            _write_witness(
                path, slug, body, q0_float,
                description=description_tpl.format(label=label),
                reference_blocks=reference_blocks,
            )
            extracted[(Z, N)] = body
            print(f"  ✓ {label}  {time.perf_counter() - t:.1f} s  "
                  f"M={len(body['habiro_coefficients']) - 1}")
        except Exception as e:
            print(f"  ✗ ERR {label}: {type(e).__name__}: {e}")
            continue

    # ─── Mirror-pair tests ─────────────────────────────────────────
    print("\n" + "=" * 78)
    print(" MIRROR-PAIR Φ_8 MULTIPLICITY TEST")
    print("=" * 78)

    u = sp.symbols('u')
    cyc_8 = u**4 + 1
    cyc_1 = u - 1
    cyc_2 = u + 1
    cyc_4 = u**2 + 1

    def load_a_m(slug):
        # Delegates to the shared loader, which REFUSES a witness flagging its
        # own reconstruction_matches false (bean qou-s41x). This was one of
        # three byte-identical copies, none of which consulted that flag.
        return _load_a_m(slug, u, witness_dir=HERE)

    def q_poch(m):
        if m == 0:
            return sp.Integer(1)
        return sp.prod(1 - u**k for k in range(1, m + 1))

    def cyc_mult(poly, cyc):
        mult = 0
        work = poly
        while True:
            q_div, r = sp.div(work, cyc, u)
            if r == 0:
                mult += 1
                work = q_div
            else:
                break
        return mult

    pair_results = []
    pairs_to_test = [
        ("⁶He", "⁶Be", "helium-6",    "beryllium-6",   6),
        ("¹²N", "¹²B", "nitrogen-12", "boron-12",      12),
        ("¹⁴O", "¹⁴C", "oxygen-14",   "carbon-14",     14),
    ]
    for X_lab, Y_lab, X_slug, Y_slug, A in pairs_to_test:
        try:
            ax = load_a_m(X_slug)
            ay = load_a_m(Y_slug)
            M_max = min(max(ax), max(ay))
            print(f"\n--- {X_lab} − {Y_lab} (A={A})  M_max={M_max} ---")
            # Difference the TRACES, not the a_m. Subtracting coefficients
            # builds d_X·t_X − d_Y·t_Y, which is proportional to t_X − t_Y only
            # where the denominators agree. Measured: under convention C they
            # agreed at q=1 on every canonical pair (so the old form was
            # accidentally right and the published C numbers stand); under D
            # they differ by a factor of 4 and every multiplicity collapses to
            # 0. Proved in QOU/Habiro/MirrorPairNormalisation.lean
            # (coeffDiff_at_coincidence, sorry-free). Bean qou-0ndb.
            total = _mirror_trace_diff(X_slug, Y_slug, u, witness_dir=HERE)
            print(f"  total degree: {sp.degree(total, u)}")
            mult_8 = cyc_mult(total, cyc_8)
            mult_1 = cyc_mult(total, cyc_1)
            mult_2 = cyc_mult(total, cyc_2)
            mult_4 = cyc_mult(total, cyc_4)
            orig_pred = A - 1
            refined_pred = 2 * ((A - 1) // 2)
            verdict_orig = "MATCH" if mult_8 == orig_pred else "REFUTES"
            verdict_refined = "MATCH" if mult_8 == refined_pred else "REFUTES"
            print(f"  Φ_8 multiplicity: {mult_8}")
            print(f"    original A−1 = {orig_pred}: {verdict_orig}")
            print(f"    refined 2⌊(A−1)/2⌋ = {refined_pred}: {verdict_refined}")
            print(f"  Φ_1 mult: {mult_1}, Φ_2 mult: {mult_2}, Φ_4 mult: {mult_4}")
            pair_results.append({
                "pair": f"{X_lab} − {Y_lab}",
                "A": A,
                "phi_8_mult": mult_8,
                "phi_1_mult": mult_1,
                "phi_2_mult": mult_2,
                "phi_4_mult": mult_4,
                "predicted_original_A_minus_1": orig_pred,
                "predicted_refined_2_floor_A_minus_1_over_2": refined_pred,
                "original_law_match": mult_8 == orig_pred,
                "refined_law_match": mult_8 == refined_pred,
            })
        except FileNotFoundError as e:
            print(f"  ✗ Missing witness: {e}")
        except Exception as e:
            print(f"  ✗ ERR: {type(e).__name__}: {e}")

    print("\n" + "=" * 78)
    print(" SUMMARY")
    print("=" * 78)
    refined_pass = sum(1 for r in pair_results if r["refined_law_match"])
    original_pass = sum(1 for r in pair_results if r["original_law_match"])
    print(f"  Pairs tested:                {len(pair_results)}")
    print(f"  Refined 2⌊(A−1)/2⌋ matches:  {refined_pass}/{len(pair_results)}")
    print(f"  Original A−1 matches:        {original_pass}/{len(pair_results)}")

    payload = {
        "computation": "even-a-mirror-pair-phi8-scaling-test",
        "description": (
            "Test the refined 2⌊(A−1)/2⌋ Φ_8 multiplicity scaling law "
            "against the now-refuted original A−1 hypothesis on the 3 "
            "open even-A mirror pairs (⁶He−⁶Be, ¹²N−¹²B, ¹⁴O−¹⁴C). "
            "These are the discriminating cases — odd-A pairs collapse "
            "both laws to the same prediction."
        ),
        "reference_blocks": [
            "docs/audits/2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md",
            "PR #1642 (Q_β Wenzl-Habiro keystone)",
            "PR #1625 (Φ_8 mechanism — level-2 SU(2) Wenzl)",
        ],
        "pairs": pair_results,
        "verdict": {
            "refined_law_universal_across_open_even_a":
                refined_pass == len(pair_results) and len(pair_results) > 0,
            "original_law_refuted_at_open_even_a":
                any(not r["original_law_match"] for r in pair_results),
            "n_pairs_tested": len(pair_results),
            "n_refined_matches": refined_pass,
            "n_original_matches": original_pass,
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        name="even-a-mirror-pair-phi8-scaling-test",
        payload=payload,
        script_path=__file__,
        engine="sympy Poly + sequential cyclotomic division",
        output_dir=HERE,
    )
    wb.save()
    elapsed = time.perf_counter() - t0
    print(f"\n  Total elapsed: {elapsed:.1f} s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
