#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical QA harness; reference-value gate.
"""Reference-value QA for the HOMFLYPT engine — CORRECTNESS, not consistency.

The existing `cross_check_trM_1ppb.py` proves that four internal `tr_M`
methods AGREE; it never checks any of them against a knot invariant
computed by an INDEPENDENT method. That is the "verification gap"
documented in
`docs/audits/2026-06-04-hidden-fitting-verification-gap-mass-binding-walkthrough.md`.

This module closes the gap for the HOMFLYPT `n≥3` path. The independent
reference is the **defining skein relation itself**, evaluated at the
engine's own specialisation point — no Hecke algebra, no Markov trace.

## The independent reference (rigorous, no Hecke)

HOMFLYPT in the Lickorish (v, z) convention satisfies

    v⁻¹·P(L₊) − v·P(L₋) = z·P(L₀),     P(unknot) = 1.

For the 2-strand torus family `closure(σ₁^k)` this gives a closed
three-term recurrence (derived in `_torus_homfly` below):

    P(σ₁^k) = v²·P(σ₁^{k-2}) + v·z·P(σ₁^{k-1})
    P(σ₁^0) = δ = (v⁻¹ − v)/z        (2-component unlink)
    P(σ₁^1) = 1                       (unknot)

Verified by hand:
    P(σ₁^2) = v·z + (v − v³)/z                 (Hopf link)
    P(σ₁^3) = 2v² − v⁴ + v²z²                  (right trefoil 3₁)

These are the textbook HOMFLY polynomials — derived here from the skein
relation alone, so they are an honest external check.

## Testing the n≥3 code path with 2-strand reference values

The buggy path is `_homflypt_nstrand_numerical` (n_strands ≥ 3). To
exercise it with rigorously-known reference values we use **Markov
stabilisation**: for `w ∈ B₂` (only σ₁), the 3-strand closure of
`w·σ₂` is the SAME link as the 2-strand closure of `w`, with the SAME
HOMFLY (it is an unframed invariant). So:

    3-strand [1]*k + [2]  ≅  2-strand σ₁^k   (same HOMFLY)

Engine output at SU(2) (v = q^{1/2}, z = q^{1/2} − q^{-1/2}) is compared
to `_torus_homfly(k, v, z)` at the SAME numerical v, z. If the engine is
a correct HOMFLY evaluator the two match; if it is ratio-only /
mis-normalised (dropped writhe framing) they do not.

History: this gate was first pointed at the LEGACY n≥3 path
(`homflypt_engine._homflypt_nstrand_numerical`), which failed 0/5 (its
ratio-only normalisation is not a knot invariant). It now drives the
reworked engine `homfly_ocneanu_trace.homfly_signed_su2`, which passes
**5/5** at full mpmath precision (the character eval uses the mpfr Rust
kernel — see the precision note in `homfly_ocneanu_trace.py`; deltas
~1e-40 at the gate's working dps). Re-point `eng3` at the legacy
`homflypt_at_su_n` to reproduce the 0/5 baseline.

Usage:
    python3 homflypt_reference_qa.py            # report
    python3 homflypt_reference_qa.py --strict   # exit 1 on any mismatch
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from homflypt_engine import homflypt_at_su_n  # noqa: E402 (legacy ratio-only path)
from homfly_ocneanu_trace import homfly_signed_su2  # noqa: E402 (reworked correct engine)

# Substrate q₀ (50-digit). Fall back to a literal if q_parameter shape drifts.
try:
    from q_parameter import Q_50_DIGIT_STR as _Q0_STR  # noqa: E402
except Exception:  # pragma: no cover
    try:
        from q_parameter import Q as _Q0  # noqa: E402
        _Q0_STR = str(_Q0)
    except Exception:
        _Q0_STR = "1.1097"


def _torus_homfly(k: int, v, z):
    """Independent HOMFLY of `closure(σ₁^k)` via the defining skein
    recurrence (Lickorish v⁻¹P₊ − vP₋ = zP₀). No Hecke, no Markov.

    P(σ₁^k) = v²·P(σ₁^{k-2}) + v·z·P(σ₁^{k-1}),
    seeded by the 2-unlink (k=0) and the unknot (k=1)."""
    if k < 0:
        raise ValueError("torus reference defined for k ≥ 0")
    delta = (1 / v - v) / z
    p_prev2 = delta          # P(σ₁^0): 2-component unlink
    p_prev1 = mp.mpf(1)      # P(σ₁^1): unknot
    if k == 0:
        return p_prev2
    if k == 1:
        return p_prev1
    p = None
    for _ in range(2, k + 1):
        p = v * v * p_prev2 + v * z * p_prev1
        p_prev2, p_prev1 = p_prev1, p
    return p


def _self_test_reference():
    """Confirm the reference recurrence reproduces the textbook Hopf and
    trefoil polynomials symbolically (convention lock-in)."""
    import sympy as sp
    v, z = sp.symbols("v z")
    delta = (1 / v - v) / z

    def torus(k):
        a, b = delta, sp.Integer(1)
        if k == 0:
            return a
        if k == 1:
            return b
        for _ in range(2, k + 1):
            a, b = b, sp.expand(v**2 * a + v * z * b)
        return b

    hopf = sp.simplify(torus(2) - (v * z + (v - v**3) / z))
    tref = sp.simplify(torus(3) - (2 * v**2 - v**4 + v**2 * z**2))
    return hopf == 0 and tref == 0


# Reference test cases: (label, k, n_component_link?)
# k = exponent of σ₁; the 3-strand word is [1]*k + [2] (Markov stabilised).
_CASES = [
    ("unknot        (σ₁)",          1),
    ("Hopf link     (σ₁²)",         2),
    ("trefoil 3₁    (σ₁³)",         3),
    ("Solomon 4²₁   (σ₁⁴)",         4),
    ("cinquefoil 5₁ (σ₁⁵)",        5),
]

TOL = mp.mpf("1e-6")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any case mismatches the reference")
    ap.add_argument("--dps", type=int, default=40)
    args = ap.parse_args()
    mp.mp.dps = args.dps

    q0 = mp.mpf(_Q0_STR)
    # SU(2) point, CORRECTED exponent v = q^{N/2} = q (N=2). The old engine
    # exponent q^{(N-1)/2}=q^{1/2} gave δ≡−1 (degenerate); see the audit doc
    # §2e. We evaluate the reference at the SAME (v,z) the fixed engine uses.
    v = q0                                # SU(2): v = q^{N/2} = q
    z = mp.sqrt(q0) - 1 / mp.sqrt(q0)     # z = q^{1/2} − q^{-1/2}; δ = −[2]_s

    print(f"HOMFLYPT reference-value QA   q₀ = {mp.nstr(q0, 12)}")
    print(f"SU(2) point:  v = {mp.nstr(v, 10)}   z = {mp.nstr(z, 10)}")
    sym_ok = _self_test_reference()
    print(f"reference recurrence vs textbook Hopf+trefoil (symbolic): "
          f"{'PASS' if sym_ok else 'FAIL'}")
    print("=" * 78)
    print("  (engine n=3 shown writhe-corrected: framed·a^{-w}; writhe KEPT in output)")
    print(f"  {'knot':<22}{'ref(unframed)':>16}{'eng n3 unfr':>16}"
          f"{'engine n=2':>16}{'  Δ(n3)':>10}")
    print("-" * 78)

    n_fail = 0
    rows = []
    for label, k in _CASES:
        ref = _torus_homfly(k, v, z)
        word3 = [1] * k + [2]            # 3-strand Markov stabilisation
        word2 = [1] * k                  # 2-strand original
        # KEEP-THE-WRITHE gate (see docs/homfly-markov-convention-discipline.md
        # §2): the engine output is the FRAMED invariant (writhe retained as
        # physical EM-phase content). To check the knot-TYPE part we divide the
        # known framing a^{−w} back out before comparing to the unframed skein
        # reference. a = v = s^N (framing base); w = braid exponent sum.
        a = v
        w3 = sum(1 if g > 0 else -1 for g in word3)
        w2 = sum(1 if g > 0 else -1 for g in word2)
        # Reworked engine: signed Ocneanu trace, writhe KEPT. framed=False
        # gives the unframed (ambient-isotopy) value directly = output·a^{−w}.
        try:
            eng3_unfr = homfly_signed_su2(word3, 3, q0, framed=False)
            eng3_framed = homfly_signed_su2(word3, 3, q0, framed=True)
        except Exception as e:           # noqa: BLE001
            eng3_unfr = None
            eng3_framed = None
            eng3_err = repr(e)
        try:
            eng2 = homflypt_at_su_n(word2, 2, 2, q0)  # legacy 2-strand path
        except Exception:                # noqa: BLE001
            eng2 = None
        d3 = (abs(eng3_unfr - ref) if eng3_unfr is not None else None)
        ok3 = (d3 is not None and d3 < TOL)
        if not ok3:
            n_fail += 1
        # show the writhe-corrected (unframed) engine value — that is what the
        # gate compares; the framed value is recorded in the witness.
        e3s = mp.nstr(eng3_unfr, 10) if eng3_unfr is not None else "ERR"
        e2s = mp.nstr(mp.mpf(eng2), 10) if eng2 is not None else "ERR"
        d3s = mp.nstr(d3, 3) if d3 is not None else "—"
        flag = "" if ok3 else "  ✗"
        print(f"  {label:<22}{mp.nstr(ref,10):>16}{e3s:>16}{e2s:>16}"
              f"{d3s:>10}{flag}")
        rows.append({
            "knot": label, "k": k, "writhe_n3": w3,
            "reference_unframed": mp.nstr(ref, 16),
            "engine_n3_framed": (mp.nstr(eng3_framed, 16) if eng3_framed is not None else None),
            "engine_n3_unframed": (mp.nstr(eng3_unfr, 16) if eng3_unfr is not None else None),
            "engine_n2": (mp.nstr(mp.mpf(eng2), 16) if eng2 is not None else None),
            "abs_delta_n3": (mp.nstr(d3, 6) if d3 is not None else None),
            "pass_n3": bool(ok3),
        })

    # Extend coverage to the n=4 and n=5 engine paths (Task A). The SAME
    # torus references, Markov-stabilised onto 4 / 5 strands (append σ₂σ₃
    # resp. σ₂σ₃σ₄ once each — a stabilisation chain leaves the closure and
    # hence the unframed HOMFLY unchanged), must still match the skein
    # reference. This exercises the freshly-wired n∈{4,5} Ocneanu weights.
    print("-" * 78)
    print("  n=4..9 paths (same torus refs, Markov-stabilised):")
    multi_fail = 0
    multi_total = 0
    # Markov-stabilise each 2-strand torus reference up to n strands by
    # appending σ₂σ₃…σ_{n-1}; `tail` is generated, not tabulated.
    for n_strands in range(4, 10):
        tail = list(range(2, n_strands))
        for label, k in _CASES:
            ref = _torus_homfly(k, v, z)
            word = [1] * k + tail
            # No try/except: the engine self-validates on import for any n,
            # so a raise here is a genuine bug and SHOULD abort loudly with a
            # full traceback rather than being masked as a silent "ERR" row.
            eng_unfr = homfly_signed_su2(word, n_strands, q0, framed=False)
            eng_framed = homfly_signed_su2(word, n_strands, q0, framed=True)
            d = abs(eng_unfr - ref)
            ok = d < TOL
            multi_total += 1
            if not ok:
                multi_fail += 1
                n_fail += 1
            print(f"  n={n_strands} {label:<18}{mp.nstr(ref,10):>16}"
                  f"{mp.nstr(eng_unfr,10):>16}{mp.nstr(d,3):>12}{'' if ok else '  ✗'}")
            rows.append({
                "knot": label, "k": k, "n_strands": n_strands,
                "writhe": sum(1 if g > 0 else -1 for g in word),
                "reference_unframed": mp.nstr(ref, 16),
                "engine_framed": mp.nstr(eng_framed, 16),
                "engine_unframed": mp.nstr(eng_unfr, 16),
                "abs_delta": mp.nstr(d, 6),
                "pass": bool(ok),
            })

    print("=" * 78)
    n3_total = len(_CASES)
    n3_fail = n_fail - multi_fail
    total = n3_total + multi_total
    print(f"  n=3 path:     {n3_total - n3_fail}/{n3_total} match reference")
    print(f"  n=4..9 paths: {multi_total - multi_fail}/{multi_total} match reference")
    print(f"  all paths:   {total - n_fail}/{total} match reference "
          f"(tol {mp.nstr(TOL,1)})")
    if n_fail:
        print("  ✗ A HOMFLYPT n≥3 path is NOT a correct invariant evaluator.")
        print("    See docs/audits/2026-06-04-hidden-fitting-verification-gap-"
              "mass-binding-walkthrough.md")

    # Emit a witness so the result is auditable / dashboard-visible.
    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("homflypt-reference-qa", engine="mpmath")
        w.set_audit_only(
            "docs/audits/2026-06-04-hidden-fitting-verification-gap-"
            "mass-binding-walkthrough.md")
        w.add_parameter("q_0", _Q0_STR)
        w.add_parameter("tolerance", mp.nstr(TOL, 2))
        w.add_data("reference_symbolic_ok", bool(sym_ok))
        w.add_data("cases", rows)
        w.add_data("n_paths_checked", sorted({3} | {r.get("n_strands", 3) for r in rows}))
        w.add_assertion(
            "all_paths_match_reference",
            computed=0 if n_fail else 1, expected=1,
            source=("HOMFLYPT n∈{3,4,5} engine output must equal the skein-"
                    "relation reference at the SU(2) point (Markov-stabilised "
                    "torus links)"))
        out = w.save()
        print(f"  Witness: {out.name}")
    except Exception as e:               # noqa: BLE001
        print(f"  (witness skipped: {e!r})")

    if args.strict and n_fail:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
