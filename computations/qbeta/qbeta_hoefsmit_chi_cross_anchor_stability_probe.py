#!/usr/bin/env python3
# ANCHOR NOTE (2026-06-22): q0 = 1.10997858275… occurrences below are the
# RETIRED pre-2026-05-28 proton anchor (old re-pin #1422), kept as this
# probe's historical / cross-anchor / pinned comparison value. The CURRENT
# canonical proton q0 is q_at() ≈ 1.1099785955573347…; the muon anchor is
# q_muon_at() ≈ 1.10997859555418…. This probe is preserved as-is by design.
"""qbeta_hoefsmit_chi_cross_anchor_stability_probe.py — Stage B
opening probe: BLOCKED by infrastructure constraints; documents the
blocker + a partial finding that constrains Stage B's scope.

**Intended test:** cross-anchor (proton vs muon) stability of the
per-Wedderburn-block χ^λ(electron-word trefoil), operator-level
analog of PR #1836's scalar q-stability gate.

**Blocker A — `chi_lambda_braid` Python fallback only supports
q = q₀** (`hecke_characters.py:372`):

    raise ValueError(
        "chi_lambda_braid() Python fallback only supports q_value "
        "== q0; install the Rust kernel (pyhecke_native) for "
        "non-default q_value."
    )

The Rust kernel `tools/pyhecke-native/` is source-only (no prebuilt
wheel; building needs cargo + offline network). pyhecke_native is
not on PyPI. So the cross-anchor numerical test cannot use the
canonical repo infrastructure in this environment.

**Blocker B — hand-built sympy χ values disagree with PR #1851's
pyhecke output by ~24%:**

| λ        | hand-build (sympy)      | PR #1851 pyhecke (q₀)   |
|----------|-------------------------|-------------------------|
| (3,)     | q³ = +1.3676            | +1.1100                 |
| (2,1)    | 0                       | +0.2091                 |
| (1,1,1)  | −q⁻³ = −0.7312          | −0.9009                 |

The mismatch is a sign/normalization convention difference between
the textbook Hoefsmit construction (this probe's hand-build) and
the repo's pyhecke convention. Resolving it requires reading the
exact pyhecke convention from the Rust source, which is out of
scope for this probe.

**Constraint on Stage B scope** — operator-level computation is
convention-sensitive and the canonical repo infrastructure is
gated on the Rust kernel. The cross-anchor stability test (this
probe's intended deliverable) must wait for either (a) Rust
toolchain network access to build pyhecke_native, or (b) a
careful reconciliation of the sympy construction with the
pyhecke convention (matching SYT ordering + sign discipline).

Recording this finding so future sessions don't re-discover the
blocker. The probe reports the hand-built χ values as a reference
and documents the conventions used.
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "hecke"))

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import fmt as _fmt, set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def hoefsmit_sigmas_n3_sympy(p, q):
    """Hand-built Hoefsmit seminormal matrices σ₁, σ₂ for partitions
    of n=3, symbolic in q. Replicates the recipe in
    hecke_characters.build_seminormal_matrices using sympy.

    NOTE: convention differs from the repo's pyhecke output by a
    sign/normalization (~24% mismatch at q₀; see docstring). This
    function is for the blocker-finding record, not production use.
    """
    h = q - 1 / q
    if p == (3,):
        I1 = sp.eye(1)
        return [q * I1, q * I1]
    if p == (1, 1, 1):
        I1 = sp.eye(1)
        return [(-1 / q) * I1, (-1 / q) * I1]
    if p == (2, 1):
        sigma_1 = sp.diag(q, -1 / q)
        rho = -2
        a = h / (1 - q ** (-2 * rho))
        a_prime = h / (1 - q ** (2 * rho))
        b_sq = a * a_prime + 1
        b = sp.sqrt(b_sq)
        sigma_2 = sp.Matrix([[a, b], [b, a_prime]])
        return [sigma_1, sigma_2]
    raise ValueError(
        f"hoefsmit_sigmas_n3_sympy: unsupported partition {p!r}; "
        f"supported set for n=3 is {{(3,), (2,1), (1,1,1)}}."
    )


def main() -> int:
    # NO FLOAT64 (AGENTS.md "PROBES ARE NOT EXEMPT"; bean qou-65qv).
    # These were bare Python FLOAT literals. Python parses a 49-digit literal
    # to binary64 and discards 32 of those digits before anything sees it, so
    # `sp.Float(str(Q_PROTON), 50)` below was padding 17 good digits back out
    # to 50 — and chi was then serialized at 25. Measured: 6.8e-18 relative,
    # i.e. 17 good digits presented as 25.
    #
    # The delta is the worse half. `Q_MUON - Q_PROTON` is ~1.28e-11 from two
    # values that agree to 11 digits — a catastrophic cancellation, which in
    # float64 leaves the probe's own headline cross-anchor quantity with
    # roughly 5 significant digits. Carried as strings and subtracted in
    # mpmath, it is exact.
    Q_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"
    Q_MUON_STR = "1.10997859555"  # cross-anchor (per 569bedda1, PR #1836)
    Q_PROTON = mp.mpf(Q_PROTON_STR)
    Q_MUON = mp.mpf(Q_MUON_STR)

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-hoefsmit-chi-cross-anchor-stability-probe",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Stage B opening: BLOCKED by infrastructure (chi_lambda_braid "
        "Python fallback hard-blocks q ≠ q_0; Rust pyhecke_native "
        "needed for non-default q). Hand-built sympy Hoefsmit also "
        "uses a different convention (~24% off pyhecke). Documents "
        "the blocker + records hand-built χ values + symbolic forms "
        "as a reference for future reconciliation."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Stage B opening — BLOCKED, recording finding")
    print("=" * 78)
    print()
    print(f"  Intended test: cross-anchor (q_p, q_μ) stability of")
    print(f"    χ^λ(electron word) per Wedderburn block.")
    print()
    print(f"  Blocker A: hecke_characters.chi_lambda_braid Python fallback")
    print(f"    hard-blocks q ≠ q_0 (ValueError). Rust pyhecke_native is")
    print(f"    source-only in tools/pyhecke-native/; not on PyPI; build")
    print(f"    needs cargo + offline network access.")
    print()
    print(f"  Blocker B: hand-built sympy Hoefsmit χ values disagree with")
    print(f"    PR #1851's pyhecke output by ~24% — convention/sign")
    print(f"    difference (SYT ordering / sigma normalization).")
    print()
    print(f"  Recording the hand-built symbolic χ values as a reference:")
    print()

    q_sym = sp.Symbol("q", positive=True)
    parts = [(3,), (2, 1), (1, 1, 1)]
    print(f"  {'λ':<10} {'χ(electron) symbolic':<35} {'value at q_p':>16}")
    print(f"  {'-'*10} {'-'*35} {'-'*16}")
    per_block = []
    for p in parts:
        sigmas = hoefsmit_sigmas_n3_sympy(p, q_sym)
        # electron word = σ_0 σ_1 σ_0 (0-indexed) = sigmas[0]·sigmas[1]·sigmas[0]
        M = sigmas[0] * sigmas[1] * sigmas[0]
        chi_sym = sp.simplify(M.trace())
        chi_qp = mp.mpf(str(sp.N(
            chi_sym.subs(q_sym, sp.Float(Q_PROTON_STR, 50)), 50)))
        print(f"  {str(p):<10} {str(chi_sym):<35} {float(chi_qp):>16.10f}")
        per_block.append({
            "lambda": list(p),
            "chi_symbolic_q": str(chi_sym),
            "chi_at_q_proton_handbuild": mp.nstr(chi_qp, 25),
        })
    print()
    print(f"  Compare with PR #1851 pyhecke values at q_p:")
    print(f"    λ=(3,):    +1.1099785828 (pyhecke)  vs  +1.3675518370 (handbuild)")
    print(f"    λ=(2,1):   +0.2090603054 (pyhecke)  vs  +0.0000000000 (handbuild)")
    print(f"    λ=(1,1,1): -0.9009183122 (pyhecke)  vs  -0.7312337076 (handbuild)")
    print(f"    → 24% mismatch on (3,); (2,1) trefoil → 0 in handbuild but")
    print(f"      not in pyhecke (sign convention on σ generator).")
    print()

    # Stage B test cannot run (blocked) — record the gate outcome
    # explicitly in the witness rather than tracking an unused local.
    stage_b_test_ran = False

    print("=" * 78)
    print(" STATUS")
    print("=" * 78)
    print()
    print(f"  Stage B intended test BLOCKED. The cross-anchor stability")
    print(f"  gate cannot run in this environment because:")
    print()
    print(f"    1. chi_lambda_braid Python fallback hard-blocks q ≠ q_0.")
    print(f"    2. Rust pyhecke_native is build-only here (network-blocked).")
    print(f"    3. The hand-built sympy alternative uses a different")
    print(f"       convention (24% mismatch on χ at q_p — convention diff).")
    print()
    print(f"  Productive follow-ups (next session, when one of these")
    print(f"  conditions can be relaxed):")
    print(f"    A. Build pyhecke_native (needs cargo + network).")
    print(f"    B. Reconcile the sympy Hoefsmit construction's SYT-ordering")
    print(f"       and σ-sign convention against the Rust source")
    print(f"       (tools/pyhecke-native/src/), then redo the test.")
    print(f"    C. Patch chi_lambda_braid's Python fallback to accept")
    print(f"       arbitrary q (drop the q == q0 guard if the underlying")
    print(f"       construction supports it).")
    print()
    print(f"  Honest verdict: Stage B is GATED on resolving one of A/B/C.")
    print(f"  This probe documents the blocker so future agents do not")
    print(f"  re-derive it.")
    print()

    builder.add_data("anchors", {
        "q_proton": _fmt(Q_PROTON),
        "q_muon": _fmt(Q_MUON),
        "delta_q": _fmt(Q_MUON - Q_PROTON),
    })
    builder.add_data("per_block_handbuild_chi_symbolic", per_block)
    builder.add_data("blockers", {
        "A_chi_lambda_braid_python_fallback_q0_only": True,
        "B_handbuild_convention_mismatch_pct": 24,
        "C_pyhecke_native_build_requires_cargo_and_network": True,
    })
    builder.add_data("follow_ups_for_unblock", [
        "Build pyhecke_native (needs cargo + network).",
        "Reconcile sympy Hoefsmit convention against Rust source.",
        "Patch Python fallback to accept arbitrary q.",
    ])
    builder.add_data("verdict", {
        "stage_b_status": "BLOCKED — operator-level cross-anchor test "
                           "cannot run in this environment",
        "stage_b_test_ran": stage_b_test_ran,
        "next_session_unblock_paths": "A/B/C above",
    })

    builder.add_assertion(
        "stage_b_blocker_recorded",
        computed=1,
        expected=1,
        tolerance=0,
        source=("Operational record: Stage B cross-anchor stability "
                "test is BLOCKED by three concrete infrastructure "
                "constraints (Python fallback q₀-only, Rust kernel "
                "build needs network, sympy convention mismatch). "
                "This probe documents the blocker + the hand-built "
                "symbolic χ values + the three unblock paths so the "
                "next session can pick this up without re-discovery."),
    )

    builder.save()
    print(f"  Witness: qbeta-hoefsmit-chi-cross-anchor-stability-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
