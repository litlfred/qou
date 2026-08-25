"""Test the shell-closure / Φ_8 multiplicity correlation hypothesis.

The mirror-pair Φ_8 anomalies at A=6 and A=14 both occur at pairs
where each half carries a closed shell (Z=2 magic + N=4 partner at
A=6; Z=8 magic + N=6 1p_{3/2} closed at A=14).

The HYPOTHESIS:

  Φ_8 multiplicity in mirror-pair Habiro elements is suppressed
  when nucleon shell closures (standard nuclear magic numbers
  Z, N ∈ {2, 8, 20, ...}) reduce the active partitions in the
  canonical Hecke braid representation.

  Categorical interpretation: closed shells = fully-saturated
  Wedderburn-block representations effectively "frozen", causing
  the canonical Hecke braid to factor through a smaller
  subalgebra with fewer level-2 SU(2) Wenzl-annihilator
  constraints, hence lower mult(Φ_8).

Falsifiable predictions:

  TEST 1 (near magic-8):
    A=16  ¹⁶N (Z=7,N=9) ↔ ¹⁶F (Z=9,N=7)
      one-hole/one-extra around Z=8/N=8 doubly magic
      Refined formula: mult(Φ_8) = 14
      Prediction:      SUPPRESSED (< 14)

    A=18  ¹⁸O (Z=8,N=10) ↔ ¹⁸Ne (Z=10,N=8)
      Z=8 magic on one side ↔ N=8 magic on the other
      Refined formula: mult(Φ_8) = 16
      Prediction:      SUPPRESSED (< 16)

  TEST 2 (mid-shell, OBEYS refined formula):
    A=22  ²²Ne (Z=10,N=12) ↔ ²²Mg (Z=12,N=10)
      mid 1d/2s shell, no nearby magic
      Refined formula: mult(Φ_8) = 20
      Prediction:      ≈ 20 (matches refined)

  TEST 3 (near magic-20):
    A=28  ²⁸Al (Z=13,N=15) ↔ ²⁸P (Z=15,N=13)
      approaching 2s_{1/2} closure (magic 20) and 1d_{3/2}
      Refined formula: mult(Φ_8) = 26
      Prediction:      SUPPRESSED (< 26)

If TEST 1 and TEST 3 show SUPPRESSED mult and TEST 2 MATCHES, the
shell-closure correlation is structurally supported. If TEST 2 also
suppresses, the categorical interpretation is more subtle than
"shell closure suppression alone".
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
from witness_base import WitnessBuilder  # noqa: E402
from habiro_coefficients_atomic import load_a_m as _load_a_m  # noqa: E402
from habiro_coefficients_atomic import mirror_trace_diff_numerator as _mirror_trace_diff  # noqa: E402 — shared loader; refuses a self-failed witness (qou-s41x)


# Shell-closure test atoms (Z, N)
SHELL_TEST_ATOMS = [
    # A=16 — near doubly magic ¹⁶O (8,8)
    ("¹⁶N (nitrogen-16, A=16)",   "nitrogen-16",  7,  9, 256),
    ("¹⁶F (fluorine-16, A=16)",   "fluorine-16",  9,  7, 256),
    # A=18 — Z=8 ↔ N=8 cross magic
    ("¹⁸O (oxygen-18, A=18)",     "oxygen-18",    8, 10, 288),
    ("¹⁸Ne (neon-18, A=18)",      "neon-18",     10,  8, 288),
    # A=22 — mid-shell control
    ("²²Ne (neon-22, A=22)",      "neon-22-mirror", 10, 12, 352),
    ("²²Mg (magnesium-22, A=22)", "magnesium-22", 12, 10, 352),
    # A=28 — near magic-20 + 1d_{3/2}
    ("²⁸Al (aluminium-28, A=28)", "aluminium-28", 13, 15, 448),
    ("²⁸P (phosphorus-28, A=28)", "phosphorus-28", 15, 13, 448),
]


def main() -> int:
    t0 = time.perf_counter()
    q0_float = float(_Q_CANONICAL)
    q0_mp = mp.mpf(str(_Q_CANONICAL))

    print("=" * 78)
    print(" SHELL-CLOSURE / Φ_8 MULTIPLICITY CORRELATION TEST")
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
    desc_tpl = ("Canonical Phase 5q Habiro coefficients for {label}. "
                "Shell-closure / Φ_8 multiplicity correlation test "
                "(near magic Z=8, magic Z=20).")

    extracted: dict[tuple[int, int], dict] = {}
    for label, slug, Z, N, max_m in SHELL_TEST_ATOMS:
        t = time.perf_counter()
        path = HERE / f"habiro-coefficients-{slug}.witness.json"
        if path.exists():
            print(f"\n--- {label}: already extracted, skipping. ---")
            continue
        try:
            body = analyse_atom(label, Z, N, q, tau_p, tau_n, q0_mp,
                                 max_m=max_m)
            if body is None or "habiro_coefficients" not in body:
                print(f"  ✗ analyse_atom returned empty body for {label}")
                continue
            _write_witness(
                path, slug, body, q0_float,
                description=desc_tpl.format(label=label),
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
    print(" MIRROR-PAIR Φ_8 MULTIPLICITY TEST (SHELL CORRELATION)")
    print("=" * 78)

    u = sp.symbols('u')

    def load_a_m(slug):
        # Delegates to the shared loader, which REFUSES a witness flagging its
        # own reconstruction_matches false (bean qou-s41x). This was one of
        # three byte-identical copies, none of which consulted that flag.
        return _load_a_m(slug, u, witness_dir=HERE)

    def q_poch(m):
        if m == 0: return sp.Integer(1)
        return sp.prod(1 - u**k for k in range(1, m + 1))

    def cyc_mult(p, c):
        m = 0
        w = p
        while True:
            q_div, r = sp.div(w, c, u)
            if r == 0:
                m += 1
                w = q_div
            else:
                break
        return m

    pairs_to_test = [
        # (X_lab, Y_lab, X_slug, Y_slug, A, shell_class, predicted_refined)
        ("¹⁶F", "¹⁶N", "fluorine-16", "nitrogen-16", 16, "near-magic-8", 14),
        ("¹⁸Ne", "¹⁸O", "neon-18", "oxygen-18", 18, "magic-8-cross", 16),
        ("²²Mg", "²²Ne", "magnesium-22", "neon-22-mirror", 22, "mid-shell", 20),
        ("²⁸P", "²⁸Al", "phosphorus-28", "aluminium-28", 28, "near-magic-20", 26),
    ]
    pair_results = []
    for X_lab, Y_lab, X_slug, Y_slug, A, shell_class, refined_pred in pairs_to_test:
        try:
            ax = load_a_m(X_slug)
            ay = load_a_m(Y_slug)
            M_max = min(max(ax), max(ay))
            print(f"\n--- {X_lab} − {Y_lab} (A={A}, {shell_class}) "
                  f"M_max={M_max} ---")
            # Difference the TRACES, not the a_m. Sum_m (a_m^X - a_m^Y)(u;u)_m
            # reconstructs d_X*t_X - d_Y*t_Y, because each witness's
            # coefficients expand its own DENOMINATOR-CLEARED numerator. That is
            # proportional to t_X - t_Y only where the two denominators agree at
            # the evaluation point; proved sorry-free in
            # QOU/Habiro/MirrorPairNormalisation.lean (coeffDiff_at_coincidence).
            # Under convention C they agreed on every canonical pair, so the
            # shortcut was accidentally valid; under D they differ by a factor of
            # 4 and every multiplicity collapses to 0 (bean qou-0ndb).
            total = _mirror_trace_diff(X_slug, Y_slug, u, witness_dir=HERE)
            print(f"  total degree: {sp.degree(total, u)}")
            mult_8 = cyc_mult(total, u**4 + 1)
            mult_1 = cyc_mult(total, u - 1)
            mult_2 = cyc_mult(total, u + 1)
            mult_4 = cyc_mult(total, u**2 + 1)
            print(f"  Φ_8 multiplicity: {mult_8}")
            print(f"  Refined prediction: {refined_pred}")
            verdict = "MATCHES_REFINED" if mult_8 == refined_pred else (
                "SUPPRESSED" if mult_8 < refined_pred else "EXCEEDS")
            print(f"  Verdict: {verdict}")
            print(f"  Φ_1: {mult_1}, Φ_2: {mult_2}, Φ_4: {mult_4}")
            pair_results.append({
                "pair": f"{X_lab} − {Y_lab}",
                "A": A,
                "shell_class": shell_class,
                "phi_8_mult": mult_8,
                "phi_1_mult": mult_1,
                "phi_2_mult": mult_2,
                "phi_4_mult": mult_4,
                "refined_predicted": refined_pred,
                "verdict": verdict,
                "suppression_amount": refined_pred - mult_8,
            })
        except FileNotFoundError as e:
            print(f"  ✗ Missing witness: {e}")
            pair_results.append({
                "pair": f"{X_lab} − {Y_lab}",
                "A": A,
                "shell_class": shell_class,
                "error": f"Missing witness: {e}",
            })
        except Exception as e:
            print(f"  ✗ ERR: {type(e).__name__}: {e}")
            pair_results.append({
                "pair": f"{X_lab} − {Y_lab}",
                "A": A,
                "shell_class": shell_class,
                "error": str(e),
            })

    # ─── Summary ────────────────────────────────────────────────────
    print("\n" + "=" * 78)
    print(" SHELL-CLOSURE CORRELATION VERDICT")
    print("=" * 78)
    suppressed_near_magic = sum(
        1 for r in pair_results
        if "verdict" in r and r["shell_class"] != "mid-shell"
        and r["verdict"] == "SUPPRESSED")
    mid_shell_matches = sum(
        1 for r in pair_results
        if "verdict" in r and r["shell_class"] == "mid-shell"
        and r["verdict"] == "MATCHES_REFINED")
    n_near = sum(1 for r in pair_results if r.get("shell_class") != "mid-shell")
    n_mid = sum(1 for r in pair_results if r.get("shell_class") == "mid-shell")
    print(f"  Near-magic pairs SUPPRESSED:  {suppressed_near_magic}/{n_near}")
    print(f"  Mid-shell pairs MATCH refined: {mid_shell_matches}/{n_mid}")

    hypothesis_supported = (
        suppressed_near_magic == n_near and mid_shell_matches == n_mid
    )
    if hypothesis_supported:
        print("\n  ✓ HYPOTHESIS SUPPORTED — shell-closure suppression observed.")
    else:
        print("\n  Verdict more nuanced — see per-pair results.")

    payload = {
        "computation": "shell-closure-phi8-correlation-test",
        "description": (
            "Test the conjecture that mirror-pair Φ_8 multiplicity "
            "anomalies (A=6, A=14) correlate with standard nuclear "
            "shell closures. The conjecture predicts SUPPRESSED "
            "mult(Φ_8) near magic Z, N ∈ {2, 8, 20} and MATCHES with "
            "refined 2⌊(A-1)/2⌋ at mid-shell positions."
        ),
        "reference_blocks": [
            "docs/audits/2026-06-01-qbeta-habiro-a6-refutes-refined-scaling-law.md",
            "docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md",
            "PR #1625 (Wenzl mechanism)",
            "PR #1642 (mass-table Habiro)",
            "PR #1649 (this branch)",
        ],
        "test_pairs": pair_results,
        "verdict": {
            "near_magic_suppressed": f"{suppressed_near_magic}/{n_near}",
            "mid_shell_matches": f"{mid_shell_matches}/{n_mid}",
            "hypothesis_supported": hypothesis_supported,
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        name="shell-closure-phi8-correlation-test",
        payload=payload,
        script_path=__file__,
        engine="sympy Poly + sequential cyclotomic division",
        output_dir=HERE,
    )
    wb.save()
    elapsed = time.perf_counter() - t0
    print(f"\n  Total elapsed: {elapsed:.1f} s")
    print(f"  Witness: shell-closure-phi8-correlation-test.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
