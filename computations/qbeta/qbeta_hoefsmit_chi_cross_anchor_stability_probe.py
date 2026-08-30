#!/usr/bin/env python3
# ANCHOR NOTE — CORRECTED 2026-08-23. The 2026-06-22 boilerplate that stood
# here had the two anchors INVERTED, in all 13 files carrying it. Measured:
#   • 1.10997858275… is NOT "the RETIRED pre-2026-05-28 proton anchor" — it is
#     the CURRENT proton pin. q_at() returns 1.10997858275138…
#   • "the CURRENT canonical proton q0 is ≈ 1.1099785955573347" named the MUON
#     value; q_at() never returns it.
#   • "q_muon_at() ≈ 1.10997859555418" named the SUPERSEDED (CODATA-2018) muon
#     value; q_muon_at() returns 1.10997859564274… See
#     computations/audits/muon_pin_three_values_probe.py for the three values.
# An agent trusting it would read the two-layer discipline backwards.
#
# What is true: the 1.10997858275… occurrences below ARE the current proton
# pin, and this probe is preserved as-is by design — its cross-anchor
# comparison is the point, so it must NOT be migrated.
"""qbeta_hoefsmit_chi_cross_anchor_stability_probe.py — Stage B:
cross-anchor (proton vs muon) stability of the per-Wedderburn-block
χ^λ(electron-word trefoil), the operator-level analog of PR #1836's
scalar q-stability gate.

BLOCKER RECORD SUPERSEDED — 2026-08-30
======================================

This probe used to end at a single assertion, `stage_b_blocker_recorded
= 1`, expecting 1: it recorded three infrastructure blockers as fact
and then asserted that it had recorded them. That assertion passes at
every possible value of every blocker, so it could not notice when the
blockers stopped being true. They have. **All three are re-tested at
run time now, and the numbers below are measured, not recalled.**

**Blocker A — "`chi_lambda_braid` Python fallback only supports
q = q₀ (`hecke_characters.py:372` raises ValueError)". STALE.** That
guard is gone: the fallback forwards `q_value` into
`build_seminormal_matrices(..., q=q_f)` precisely so cross-anchor
q-stability probes can run (see the comment at its call site, PR
#1861). `probe_blocker_a` below calls it at the muon anchor with the
Rust kernel forced off and reports whether it raises.

**Blocker B — "hand-built sympy χ disagrees with PR #1851's pyhecke
output by ~24%". FALSE — the two columns are different braid words.**
The recorded "pyhecke" numbers are χ_λ of a SINGLE crossing σ₁, not of
the electron word σ₁σ₂σ₁:

| λ        | hand-build, σ₁σ₂σ₁ | recorded "pyhecke" | χ_λ(σ₁) exactly |
|----------|--------------------|--------------------|-----------------|
| (3,)     | q³   = +1.36755    | +1.1099785828      | q      = q₀     |
| (2,1)    | 0                  | +0.2090603054      | q − 1/q = h     |
| (1,1,1)  | −q⁻³ = −0.73123    | −0.9009183122      | −1/q            |

Each recorded value matches χ_λ(σ₁) to ~3e-8 relative. There is no
convention mismatch to reconcile: run against the SAME word, the
hand-build and the repo's own `chi_lambda_braid` agree exactly —
symbolically (q³, 0, −q⁻³) and numerically through the Rust mpfr
kernel. `probe_blocker_b` asserts that identification.

**Blocker C — "pyhecke_native is source-only, not on PyPI, build needs
cargo + network". STALE in this environment.** pyhecke_native 0.9.0 is
installed and `chi_lambda_braid_mpfr` answers at 50 dps.
`probe_blocker_c` reports the live import state; when it is absent the
probe still runs, through the Python fallback that Blocker A wrongly
declared closed.

**So Stage B runs.** The cross-anchor test compares χ^λ at the proton
and muon anchors by two routes: direct subtraction of two mpfr-kernel
evaluations, and quadrature of the exact symbolic dχ^λ/dq across the
interval. What remains genuinely open is not infrastructure but
interpretation — what a per-block Δχ of ~5e-8 means for the scalar
gate.
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import importlib.util
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

import hecke_characters as hc  # noqa: E402 — the canonical repo route
from witness_base import WitnessBuilder  # noqa: E402

# The electron word (trefoil closure) and the single crossing the
# PR #1851 reference column turns out to have been computed on.
W_ELECTRON = [(1, 1), (1, 2), (1, 1)]   # σ₁ σ₂ σ₁
W_SINGLE_CROSSING = [(1, 1)]            # σ₁

# The three numbers this module's docstring recorded as "PR #1851
# pyhecke output at q₀", kept verbatim so `probe_blocker_b` can say
# what they actually are instead of asserting a 24% mismatch.
PR1851_REFERENCE_AT_Q0 = {
    (3,): "1.1099785828",
    (2, 1): "0.2090603054",
    (1, 1, 1): "-0.9009183122",
}


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


def probe_blocker_a(q_muon_str):
    """Does the Python fallback still refuse q ≠ q₀?  MEASURED.

    Blocker A was recorded as a `ValueError` raised by
    `chi_lambda_braid`'s Python fallback for any non-default
    `q_value`. The Rust kernel is bypassed here on purpose — with it
    installed the fallback would never be reached and the question
    would go untested. `_RUST_CHI_AVAILABLE` is restored in `finally`.

    Returns (raised: bool, detail: str, values: dict|None).
    """
    saved = hc._RUST_CHI_AVAILABLE
    hc._RUST_CHI_AVAILABLE = False
    try:
        values = {}
        for p in ((3,), (2, 1), (1, 1, 1)):
            values[p] = hc.chi_lambda_braid(
                list(p), W_ELECTRON, q_value=q_muon_str)
        return False, "fallback accepted q ≠ q₀", values
    except Exception as exc:            # noqa: BLE001 — the blocker IS the exception
        return True, f"{type(exc).__name__}: {exc}", None
    finally:
        hc._RUST_CHI_AVAILABLE = saved


def probe_blocker_c():
    """Is pyhecke_native importable, and is the mpfr path live? MEASURED."""
    spec = importlib.util.find_spec("pyhecke_native")
    version = None
    if spec is not None:
        try:
            import importlib.metadata as _md
            version = _md.version("pyhecke-native")
        except Exception:               # noqa: BLE001
            version = "unknown"
    return {
        "pyhecke_native_importable": spec is not None,
        "pyhecke_native_version": version,
        "rust_chi_available_in_hecke_characters": bool(
            hc._RUST_CHI_AVAILABLE),
    }


def chi_repo_symbolic(shape, word):
    """χ_λ(word) as an EXACT rational function of q, via the repo's
    own `hecke_characters_symbolic` path — a code route this module
    shares nothing with beyond the partition and the word."""
    return sp.simplify(hc.chi_lambda_braid(shape, word, precision="symbolic_q"))


def chi_repo_mpfr(shape, word, q_str, dps=50):
    """χ_λ(word) at `q_str` through the canonical repo route.

    Uses the Rust mpfr kernel when it is present (exact at `dps`), and
    the Python fallback otherwise, tagging which answered so the
    witness never presents an f64 number as a 50-dps one.
    """
    if hc._RUST_CHI_AVAILABLE:
        return mp.mpf(hc.chi_lambda_braid(
            list(shape), word, q_value=q_str, precision=f"mpfr_{dps}dps")), \
            f"mpfr_{dps}dps"
    return mp.mpf(hc.chi_lambda_braid(
        list(shape), word, q_value=q_str)), "f64_numeric_fallback"


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
        "Stage B: cross-anchor (proton vs muon) stability of the "
        "per-Wedderburn-block χ^λ(electron word). The three "
        "infrastructure blockers this probe used to record as fact are "
        "re-tested at run time — the Python fallback's q ≠ q₀ guard is "
        "gone, pyhecke_native is importable, and the '24% convention "
        "mismatch' was the recorded reference column being χ_λ(σ₁) "
        "rather than χ_λ(σ₁σ₂σ₁). The test therefore runs, by two "
        "independent routes at each anchor."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Stage B — re-testing the recorded blockers, then running")
    print("=" * 78)
    print()
    print(f"  Test: cross-anchor (q_p, q_μ) stability of")
    print(f"    χ^λ(electron word) per Wedderburn block.")
    print()

    # ── Blockers, measured ────────────────────────────────────────────
    blocker_a_raised, blocker_a_detail, blocker_a_values = probe_blocker_a(
        Q_MUON_STR)
    blocker_c = probe_blocker_c()
    print(f"  [Blocker A — Python fallback rejects q ≠ q₀?]")
    print(f"    recorded: YES (ValueError at hecke_characters.py:372)")
    print(f"    measured: {'YES' if blocker_a_raised else 'NO'} — "
          f"{blocker_a_detail}")
    print()
    print(f"  [Blocker C — pyhecke_native unavailable?]")
    print(f"    recorded: YES (source-only, not on PyPI)")
    print(f"    measured: importable="
          f"{blocker_c['pyhecke_native_importable']} "
          f"version={blocker_c['pyhecke_native_version']} "
          f"rust_path_live="
          f"{blocker_c['rust_chi_available_in_hecke_characters']}")
    print()

    q_sym = sp.Symbol("q", positive=True)
    parts = [(3,), (2, 1), (1, 1, 1)]

    # ── Blocker B — the '24% convention mismatch', identified ─────────
    # Route A: this module's hand-built Hoefsmit matrices, traced.
    # Route B: the repo's own hecke_characters_symbolic path.
    # Same word, same q: if these disagree there IS a convention
    # problem. They do not. The recorded reference column is then
    # checked against χ_λ of a SINGLE crossing, which is what it is.
    print(f"  [Blocker B — hand-build vs repo, same braid word]")
    print(f"  {'λ':<10} {'handbuild χ(σ₁σ₂σ₁)':<24} "
          f"{'repo symbolic':<24} {'χ(σ₁)':<12}")
    print(f"  {'-'*10} {'-'*24} {'-'*24} {'-'*12}")
    per_block = []
    handbuild_matches_repo = 0
    reference_is_single_crossing = 0
    q_proton_sp = sp.Float(Q_PROTON_STR, 60)
    for p in parts:
        sigmas = hoefsmit_sigmas_n3_sympy(p, q_sym)
        # electron word = σ_0 σ_1 σ_0 (0-indexed) = sigmas[0]·sigmas[1]·sigmas[0]
        M = sigmas[0] * sigmas[1] * sigmas[0]
        chi_sym = sp.simplify(M.trace())
        chi_qp = mp.mpf(str(sp.N(chi_sym.subs(q_sym, q_proton_sp), 50)))

        chi_repo_sym = chi_repo_symbolic(list(p), W_ELECTRON)
        agrees = bool(sp.simplify(chi_sym - chi_repo_sym) == 0)
        handbuild_matches_repo += int(agrees)

        chi_single_sym = chi_repo_symbolic(list(p), W_SINGLE_CROSSING)
        chi_single_qp = mp.mpf(str(sp.N(
            chi_single_sym.subs(q_sym, q_proton_sp), 50)))
        recorded = mp.mpf(PR1851_REFERENCE_AT_Q0[p])
        scale = mp.fabs(chi_single_qp) if chi_single_qp != 0 else mp.mpf(1)
        matches_single = mp.fabs(recorded - chi_single_qp) / scale < mp.mpf("1e-6")
        reference_is_single_crossing += int(matches_single)

        print(f"  {str(p):<10} {str(chi_sym):<24} {str(chi_repo_sym):<24} "
              f"{str(chi_single_sym):<12}")
        per_block.append({
            "lambda": list(p),
            "chi_symbolic_q": str(chi_sym),
            "chi_at_q_proton_handbuild": mp.nstr(chi_qp, 25),
            "chi_symbolic_repo_route": str(chi_repo_sym),
            "handbuild_matches_repo_symbolic": agrees,
            "chi_single_crossing_symbolic": str(chi_single_sym),
            "chi_single_crossing_at_q_proton": mp.nstr(chi_single_qp, 25),
            "pr1851_recorded_reference": PR1851_REFERENCE_AT_Q0[p],
            "recorded_reference_is_single_crossing": bool(matches_single),
        })
    print()
    print(f"    hand-build == repo symbolic, same word: "
          f"{handbuild_matches_repo}/{len(parts)} blocks")
    print(f"    recorded 'pyhecke' column == χ_λ(σ₁): "
          f"{reference_is_single_crossing}/{len(parts)} blocks")
    print(f"    → the '~24% mismatch' was a different braid word, not a "
          f"convention.")
    print()

    # ── The braid and Hecke relations the hand-build must satisfy ─────
    # Independent of everything above: σ₁σ₂σ₁ = σ₂σ₁σ₂ is the braid
    # relation (two different matrix products of the same three
    # factors), and σ² = h·σ + I is the Hecke quadratic relation
    # ((σ − q)(σ + 1/q) = 0). Together they are what makes these
    # matrices a Hecke representation at all; neither was checked.
    braid_ok = 0
    quadratic_ok = 0
    quadratic_total = 0
    for p in parts:
        s1, s2 = hoefsmit_sigmas_n3_sympy(p, q_sym)
        braid_ok += int(sp.simplify(sp.expand(s1 * s2 * s1 - s2 * s1 * s2))
                        .is_zero_matrix is True)
        eye = sp.eye(s1.shape[0])
        h_sym = q_sym - 1 / q_sym
        for s in (s1, s2):
            quadratic_total += 1
            quadratic_ok += int(
                sp.simplify(sp.expand(s * s - h_sym * s - eye))
                .is_zero_matrix is True)
    print(f"  [Hecke representation self-check]")
    print(f"    braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂: {braid_ok}/{len(parts)} blocks")
    print(f"    quadratic σ² = h·σ + I: {quadratic_ok}/{quadratic_total} generators")
    print()

    # ── Stage B, run ──────────────────────────────────────────────────
    # Route A: the canonical repo route at each anchor (Rust mpfr kernel
    #          at 50 dps when present, Python fallback otherwise).
    # Route B: the exact symbolic χ^λ(q) from the hand-build, with the
    #          anchor difference obtained by QUADRATURE of dχ/dq across
    #          [q_p, q_μ] rather than by subtracting two nearly equal
    #          numbers — the cancellation this module's own comment
    #          warns about, avoided by construction.
    print(f"  [Stage B — cross-anchor χ^λ stability]")
    precision_tags = set()
    delta_direct_total = mp.mpf(0)
    delta_quadrature_total = mp.mpf(0)
    cross_anchor = []
    print(f"  {'λ':<10} {'χ(q_p)':<26} {'χ(q_μ)':<26} {'Δ direct':<16}"
          f"{'Δ quadrature':<16}")
    print(f"  {'-'*10} {'-'*26} {'-'*26} {'-'*16}{'-'*16}")
    for p, block in zip(parts, per_block):
        chi_p, tag_p = chi_repo_mpfr(p, W_ELECTRON, Q_PROTON_STR)
        chi_m, tag_m = chi_repo_mpfr(p, W_ELECTRON, Q_MUON_STR)
        precision_tags.update({tag_p, tag_m})
        delta_direct = chi_m - chi_p

        # `locals=` is load-bearing: a bare sympify("q**3") mints a
        # fresh Symbol("q") with no assumptions, which is NOT `q_sym`,
        # and sp.diff would then return 0 for every block. Route B
        # silently reported Δ = 0 until this two-route comparison
        # caught it.
        chi_sym = sp.sympify(block["chi_symbolic_q"], locals={"q": q_sym})
        dchi = sp.diff(chi_sym, q_sym)
        dchi_fn = sp.lambdify(q_sym, dchi, modules="mpmath")
        delta_quad = (mp.mpf(0) if dchi == 0
                      else mp.quad(dchi_fn, [Q_PROTON, Q_MUON]))

        delta_direct_total += mp.fabs(delta_direct)
        delta_quadrature_total += mp.fabs(delta_quad)
        print(f"  {str(p):<10} {mp.nstr(chi_p, 20):<26} "
              f"{mp.nstr(chi_m, 20):<26} {mp.nstr(delta_direct, 8):<16}"
              f"{mp.nstr(delta_quad, 8):<16}")
        cross_anchor.append({
            "lambda": list(p),
            "chi_at_q_proton": _fmt(chi_p),
            "chi_at_q_muon": _fmt(chi_m),
            "delta_direct_subtraction": _fmt(delta_direct),
            "delta_derivative_quadrature": _fmt(delta_quad),
            "relative_delta": _fmt(
                delta_direct / chi_p if chi_p != 0 else mp.mpf(0)),
            "precision_tag": tag_p,
        })
    print()
    stage_b_test_ran = True

    delta_q = Q_MUON - Q_PROTON
    print("=" * 78)
    print(" STATUS")
    print("=" * 78)
    print()
    print(f"  Stage B RAN. Every recorded blocker was re-tested:")
    print()
    print(f"    A. Python fallback rejects q ≠ q_0: "
          f"{'STILL TRUE' if blocker_a_raised else 'STALE — it accepts'}")
    print(f"       ({blocker_a_detail})")
    print(f"    B. '24% convention mismatch': STALE — the recorded "
          f"reference")
    print(f"       column is χ_λ(σ₁), matched on "
          f"{reference_is_single_crossing}/{len(parts)} blocks; against the "
          f"same word")
    print(f"       the hand-build and the repo agree on "
          f"{handbuild_matches_repo}/{len(parts)}.")
    print(f"    C. pyhecke_native unavailable: "
          f"{'STILL TRUE' if not blocker_c['pyhecke_native_importable'] else 'STALE — version ' + str(blocker_c['pyhecke_native_version'])}")
    print()
    print(f"  Anchors: Δq = q_μ − q_p = {mp.nstr(delta_q, 12)} "
          f"(relative {mp.nstr(delta_q / Q_PROTON, 8)})")
    print(f"  Σ|Δχ^λ| direct     = {mp.nstr(delta_direct_total, 20)}")
    print(f"  Σ|Δχ^λ| quadrature = {mp.nstr(delta_quadrature_total, 20)}")
    print(f"  χ precision route(s): {sorted(precision_tags)}")
    print()
    print(f"  What is still open is interpretation, not infrastructure:")
    print(f"    - the (2,1) block's χ vanishes identically, so it carries")
    print(f"      no cross-anchor signal at all;")
    print(f"    - the (3,) and (1,1,1) blocks move by ~5e-8 and ~3e-8,")
    print(f"      i.e. ~3·Δq/q — pure first-order q-sensitivity of q^±3,")
    print(f"      not a structural instability. Whether that clears the")
    print(f"      PR #1836 scalar gate is a threshold question this probe")
    print(f"      does not answer.")
    print()

    builder.add_data("anchors", {
        "q_proton": _fmt(Q_PROTON),
        "q_muon": _fmt(Q_MUON),
        "delta_q": _fmt(delta_q),
        "delta_q_relative": _fmt(delta_q / Q_PROTON),
    })
    builder.add_data("per_block_handbuild_chi_symbolic", per_block)
    builder.add_data("cross_anchor_chi", cross_anchor)
    builder.add_data("chi_precision_tags", sorted(precision_tags))
    builder.add_data("blockers_measured", {
        "A_python_fallback_rejects_non_q0": {
            "recorded": True,
            "measured": blocker_a_raised,
            "detail": blocker_a_detail,
        },
        "B_handbuild_convention_mismatch": {
            "recorded_pct": 24,
            "measured": (
                "no mismatch — the recorded reference column is "
                "chi_lambda(sigma_1), not chi_lambda(sigma_1 sigma_2 "
                "sigma_1); against the same word the hand-build and the "
                "repo route agree exactly"),
            "handbuild_matches_repo_symbolic_blocks":
                f"{handbuild_matches_repo}/{len(parts)}",
            "reference_matches_single_crossing_blocks":
                f"{reference_is_single_crossing}/{len(parts)}",
        },
        "C_pyhecke_native_unavailable": {
            "recorded": True,
            "measured": blocker_c,
        },
    })
    builder.add_data("hecke_representation_self_check", {
        "braid_relation_blocks": f"{braid_ok}/{len(parts)}",
        "quadratic_relation_generators":
            f"{quadratic_ok}/{quadratic_total}",
    })
    builder.add_data("verdict", {
        "stage_b_status": (
            "RAN — every recorded blocker re-tested; A and C stale, B a "
            "braid-word misattribution rather than a convention conflict"),
        "stage_b_test_ran": stage_b_test_ran,
        "open_question": (
            "interpretation: (2,1) carries no signal (χ ≡ 0), (3,) and "
            "(1,1,1) move at first order in Δq/q. Whether that clears "
            "the PR #1836 scalar gate is a threshold question."),
    })

    # ── Assertions ────────────────────────────────────────────────────

    # (1) Blocker B, identified rather than recorded.
    #   Route A: this module's hand-built Hoefsmit seminormal matrices,
    #            traced on σ₁σ₂σ₁ and simplified in sympy.
    #   Route B: hecke_characters.chi_lambda_braid(precision='symbolic_q'),
    #            the repo's own symbolic character path — different
    #            code, same partition and word.
    # Recorded as a 24% convention mismatch; measured, they are equal.
    builder.add_assertion(
        "handbuild_chi_matches_repo_symbolic_route",
        computed=handbuild_matches_repo,
        expected=len(parts),
        tolerance=0,
        source=(
            "Route A: trace of σ₁σ₂σ₁ from the hand-built Hoefsmit "
            "matrices in this module. Route B: "
            "chi_lambda_braid(..., precision='symbolic_q') from "
            "hecke_characters_symbolic. Exact rational functions of q, "
            "compared symbolically — the reconciliation the recorded "
            "Blocker B called out of scope."
        ),
    )

    # (2) What the recorded 'PR #1851 pyhecke' column actually is.
    #   Route A: the three numbers as written into this module's
    #            docstring, kept verbatim in PR1851_REFERENCE_AT_Q0.
    #   Route B: χ_λ(σ₁) — a SINGLE crossing — evaluated at q_p from the
    #            repo's symbolic route: q, q − 1/q, −1/q.
    # They agree to ~3e-8 relative on all three blocks, while against
    # the electron word they differ by 19%, ∞ and 23%. The '24%
    # convention mismatch' was a braid-word misattribution.
    builder.add_assertion(
        "pr1851_reference_column_is_single_crossing_character",
        computed=reference_is_single_crossing,
        expected=len(parts),
        tolerance=0,
        source=(
            "Route A: the three reference numbers recorded in this "
            "module's docstring as PR #1851 pyhecke output at q₀. "
            "Route B: χ_λ(σ₁) at q₀ from the repo symbolic route "
            "(= q, q−1/q, −1/q). Match band 1e-6 relative — three "
            "orders tighter than the alleged 24% and eight orders "
            "looser than exact, so it distinguishes 'same quantity' "
            "from 'same to transcription precision'."
        ),
    )

    # (3) Blocker A, refuted by being unable to hold.
    #   Route A: `chi_lambda_braid` at the MUON anchor with the Rust
    #            kernel forced off — the exact call the recorded blocker
    #            says raises ValueError.
    #   Route B: the same character through the mpfr kernel (or, if
    #            pyhecke_native is absent, the hand-built symbolic form
    #            substituted at 65 dps).
    # If the fallback still rejected q ≠ q₀ there would be no Route A
    # value to compare, and this assertion could not be formed at all.
    if blocker_a_values is not None:
        fallback_gaps = []
        for p in parts:
            reference, _ = chi_repo_mpfr(p, W_ELECTRON, Q_MUON_STR)
            fallback_gaps.append(
                mp.fabs(mp.mpf(blocker_a_values[p]) - reference))
        builder.add_data("blocker_a_fallback_vs_reference", {
            str(p): _fmt(g) for p, g in zip(parts, fallback_gaps)
        })
        builder.add_assertion(
            "python_fallback_chi_at_muon_anchor_matches_kernel",
            computed=mp.nstr(max(fallback_gaps), 20),
            expected="0",
            tolerance="1e-12",
            source=(
                "Route A: chi_lambda_braid at q_μ with "
                "_RUST_CHI_AVAILABLE forced False — the Python "
                "seminormal fallback the recorded Blocker A says "
                "raises ValueError for q ≠ q₀. Route B: the same "
                "character from the mpfr kernel. Tolerance 1e-12 is "
                "the f64 grade of Route A, not a precision claim. This "
                "assertion is unformable if Blocker A holds."
            ),
        )

    # (4) The hand-build really is a Hecke representation.
    #   Route A: the matrix product σ₁σ₂σ₁.
    #   Route B: the matrix product σ₂σ₁σ₂ — same three factors, other
    #            association. Equality is the braid relation, and it is
    #            what makes χ a braid-word invariant at all.
    builder.add_assertion(
        "braid_relation_holds_for_handbuilt_sigmas",
        computed=braid_ok,
        expected=len(parts),
        tolerance=0,
        source=(
            "Route A: σ₁σ₂σ₁ from the hand-built Hoefsmit matrices. "
            "Route B: σ₂σ₁σ₂ from the same matrices. Symbolic in q, "
            "over all three Wedderburn blocks of H_3."
        ),
    )

    # (5) And satisfies the Hecke quadratic relation.
    #   Route A: σ·σ by matrix multiplication.
    #   Route B: h·σ + I, i.e. (σ − q)(σ + 1/q) = 0 — the defining
    #            relation of H_n(q), assembled from σ without squaring.
    builder.add_assertion(
        "hecke_quadratic_relation_holds_for_handbuilt_sigmas",
        computed=quadratic_ok,
        expected=quadratic_total,
        source=(
            "Route A: σ² by matrix multiplication. Route B: h·σ + I "
            "with h = q − 1/q, the Hecke quadratic relation "
            "(σ − q)(σ + 1/q) = 0. Both generators of all three "
            "blocks, symbolic in q."
        ),
        tolerance=0,
    )

    # (6) STAGE B'S DELIVERABLE.
    #   Route A: χ^λ evaluated at each anchor through the canonical repo
    #            route and SUBTRACTED — the cancellation-prone route.
    #   Route B: ∫_{q_p}^{q_μ} dχ^λ/dq dq by mpmath quadrature of the
    #            exact symbolic derivative, which never forms a
    #            difference of two nearly equal numbers.
    # Agreement says the measured cross-anchor drift is the first-order
    # q-sensitivity of the character and nothing else; disagreement
    # would mean the anchors' 8-digit agreement had eaten the signal.
    builder.add_assertion(
        "cross_anchor_chi_delta_matches_derivative_quadrature",
        computed=mp.nstr(delta_direct_total, 30),
        expected=mp.nstr(delta_quadrature_total, 30),
        tolerance="1e-30",
        source=(
            "Route A: Σ_λ |χ^λ(q_μ) − χ^λ(q_p)| by direct subtraction of "
            f"two {sorted(precision_tags)} evaluations. Route B: "
            "Σ_λ |∫ dχ^λ/dq dq| across the anchor interval by mpmath "
            "quadrature of the exact symbolic derivative — no "
            "subtraction of nearly equal numbers anywhere."
        ),
    )

    # A real defect in this module's own comment, recorded not repaired.
    if mp.fabs(delta_q) > mp.mpf("1e-10"):
        builder.add_caveat(
            f"The comment above Q_PROTON_STR says 'Q_MUON - Q_PROTON is "
            f"~1.28e-11 from two values that agree to 11 digits'. "
            f"Measured: Δq = {mp.nstr(delta_q, 10)} ≈ 1.28e-8, and the "
            f"two anchors agree to 8 significant digits, not 11. The "
            f"mantissa is right and the exponent is three orders out. "
            f"The comment's conclusion still holds in direction — "
            f"float64 subtraction of these two anchors loses about half "
            f"its digits — but the severity it states is overstated, and "
            f"the '5 significant digits' figure that follows from 1.28e-11 "
            f"is not what this anchor pair actually costs."
        )

    builder.save()
    print(f"  Witness: qbeta-hoefsmit-chi-cross-anchor-stability-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
