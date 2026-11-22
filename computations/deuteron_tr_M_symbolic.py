#!/usr/bin/env python3
"""
deuteron_tr_M_symbolic.py — Closed-form symbolic trace of the
internal A=2 (deuteron) braid in the Iwahori–Hecke algebra H_6(q).

**Trace conventions (per docs/audits/2026-05-17-dual-tr-m-discrepancy.md):**
This script's HISTORICAL output (the rational function in q reported
since 2026-05-05) is the **q-Plancherel measure trace** (weights dim_q²/[n]_q!),
NOT the canonical Markov trace. As of 2026-05-17 the script computes
BOTH:

  - tr_q_plancherel_symbolic — historical output, Σ dim_q²/[n]_q!·χ^λ/f^λ
  - tr_Markov_symbolic — canonical Wenzl-Ocneanu y_λ·χ^λ trace
    (matches `thm:jones-markov-trace` in AGENTS.md §7a)

The witness JSON now reports both for downstream comparison.

Continues the proton/neutron closed-form work in
[`hoefsmit_symbolic.py`](hoefsmit_symbolic.py) and the audit doc
[`docs/audits/2026-05-05-symbolic-hoefsmit-fix-proton-tr-m.md`](../../docs/audits/2026-05-05-symbolic-hoefsmit-fix-proton-tr-m.md).

The deuteron internal braid (no inter-nucleon crossings) is a
22-crossing word in B_6, derived from `proton_cross` ⊕ `neutron_cross`
via `atomic_braid_to_crossings(1, 1, include_inter=False)`.

The tr_M closed form is computed as
    tr_M(β) = Σ_{λ ⊢ 6} w_λ · χ^λ(β) / f^λ
with w_λ = dim_q(λ)² / [6]_q! and f^λ = #SYT(λ).

All 11 partitions of 6 contribute; per-partition χ^λ takes 0.1–22.5 s
on this machine (total ~80 s including the partition sum).

Result (PR #547 derivation):
  numerator     : palindromic degree-68 polynomial (35 nonzero terms)
  denominator   : 11520·q^19·(1 + 5q^2 + 14q^4 + 29q^6 + 49q^8 + 71q^10
                                  + 90q^12 + 101q^14 + 101q^16 + 90q^18
                                  + 71q^20 + 49q^22 + 29q^24 + 14q^26
                                  + 5q^28 + q^30)
  pole at q=0   : 19   (matches dp_pole_probe upper bound)
  leading coef  : +1/128 = +1/2^7   (POSITIVE — opposite sign from
                                     proton/neutron −1/8 = −1/2^3)
  value at q_0  : ≈ 0.32110

The change of sign and the larger pole order (19 vs 10/8) refute the
naive "universal −1/(2 n!)" conjecture from the round-1 audit.  The
leading coefficient is still a power of 2 (1/2^7 here, 1/2^3 there),
suggesting a refined conjecture in terms of $\\dim_q$ specializations.

Run:  python3 computations/deuteron_tr_M_symbolic.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hoefsmit_symbolic import (  # noqa: E402
    Q,
    chi_lambda_symbolic,
    dim_q,
    pole_order_at_zero,
    q_fac,
)
from markov_peel import tr_M_atomic  # noqa: E402 — canonical Markov trace via GS + Markov-axiom recursion
from hecke_characters import partitions_of, standard_young_tableaux  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings as atomic_braid_to_crossings  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402  — single source of truth

# Canonical 50-dps q_0 (full precision; matches y-lambda-mpfr-witness.json
# and other round-3 scripts). Defined at module level to avoid duplicated
# magic values across functions.
Q0_CANONICAL = sp.Float(Q_50_DIGIT_STR, 50)


def main() -> int:
    deut = atomic_braid_to_crossings(1, 1, include_inter=False)
    print(f"deuteron internal braid: {len(deut)} crossings (n=6)")

    # Per-partition timing for transparency.
    parts = []
    for shape in partitions_of(6):
        syts, _, _ = standard_young_tableaux(list(shape))
        parts.append((len(syts), tuple(shape)))
    parts.sort()

    def conjugate_partition(shape):
        """Transpose a Young diagram: (4,2) → (2,2,1,1)."""
        if not shape:
            return ()
        m = max(shape)
        return tuple(sum(1 for p in shape if p > j) for j in range(m))

    # Optimization: under the bar involution q → q⁻¹ the symbolic
    # character satisfies χ^{λ'}(β) = χ^λ(β)|_{q→q⁻¹} when β is bar-
    # invariant (writhe-balanced, palindromic in cross-type). For the
    # deuteron internal braid this holds, so χ^{λ'} can be derived
    # from already-computed χ^λ via symbolic subs(Q, 1/Q).

    # Fast path: read symbolic χ^λ from the cached witness
    # chi-deuteron-h6.witness.json (computed once, ~131s; reused in ms).
    # If absent, fall back to direct computation with conjugate-pairing.
    chi_cache_path = _pb.witness_path("chi-deuteron-h6.witness.json", HERE)
    cached_chi: dict[tuple, sp.Expr] = {}
    from canonical_braid_crossings import word_fingerprint  # noqa: E402
    if chi_cache_path.exists():
        cache_doc = json.loads(chi_cache_path.read_text())
        # Serve the cache only if it was built from THIS ordered word. A
        # multiset match is not enough (bean qou-4383): chi-deuteron-h6 kept
        # the superseded intra ordering's characters with a matching multiset.
        if cache_doc.get("word_fingerprint") != word_fingerprint(deut):
            print("  chi-deuteron-h6 cache was built from a different word "
                  "(word_fingerprint mismatch or untagged) — recomputing")
            cache_doc = {}
        for entry in cache_doc.get("chi_lambda_symbolic", []):
            shape_tup = tuple(entry["partition"])
            cached_chi[shape_tup] = sp.sympify(entry["chi_q_symbolic"], locals={"q": Q})
        print(f"  loaded {len(cached_chi)} symbolic χ^λ from chi-deuteron-h6 cache")

    chi_per_lam: dict = {}
    processed: set = set()
    print()
    print("per-partition χ^λ timings (cache + conjugate-pairing):")
    for f, shape in parts:
        if shape in processed:
            continue
        t0 = time.time()
        if shape in cached_chi:
            chi = cached_chi[shape]
            source = "cached"
        else:
            chi = chi_lambda_symbolic(shape, deut)
            source = "computed"
        dt = time.time() - t0
        chi_q0 = sp.N(chi.subs(Q, Q0_CANONICAL), 30)
        chi_per_lam[shape] = {
            "f_lambda": f,
            "chi_at_q0": str(chi_q0),
            "compute_seconds": round(dt, 3),
            "derived_from_conjugate": False,
            "source": source,
        }
        print(f"  {str(shape):<22} f={f:>2}  {dt:6.3f}s  χ(q0)={float(chi_q0):+.4f}  ({source})")
        processed.add(shape)

        conj = conjugate_partition(shape)
        if conj != shape and conj not in processed:
            t1 = time.time()
            if conj in cached_chi:
                chi_conj_expr = cached_chi[conj]
                source_c = "cached"
            else:
                chi_conj_expr = sp.cancel(chi.subs(Q, 1 / Q))
                source_c = "derived q→q⁻¹"
            dt_conj = time.time() - t1
            chi_conj_q0 = sp.N(chi_conj_expr.subs(Q, Q0_CANONICAL), 30)
            f_conj = next(ff for ff, sh in parts if sh == conj)
            chi_per_lam[conj] = {
                "f_lambda": f_conj,
                "chi_at_q0": str(chi_conj_q0),
                "compute_seconds": round(dt_conj, 3),
                "derived_from_conjugate": (source_c == "derived q→q⁻¹"),
                "conjugate_source": str(shape),
                "source": source_c,
            }
            print(f"  {str(conj):<22} f={f_conj:>2}  {dt_conj:6.3f}s  χ(q0)={float(chi_conj_q0):+.4f}  ({source_c})")
            processed.add(conj)

    print()
    print("computing the canonical Markov trace via markov_peel.tr_M_atomic")
    print("(GS reduction + Markov-axiom recursive ascent; no Plancherel fallback)...")
    t0 = time.time()
    trM = tr_M_atomic(1, 1, include_inter=False)
    dt_total = time.time() - t0
    print(f"  canonical Markov trace assembled in {dt_total:.1f}s")
    # markov_peel returns an expression in q with half-integer powers
    # (the Wenzl q^(1/2) Markov-parameter convention). Pole-order
    # analysis would require either substituting r = q^(1/2) or working
    # in a Laurent ring; the script's downstream consumers only need the
    # value at q_0 and (optionally) the rational form for documentation.
    free = list(trM.free_symbols)
    q_used = free[0] if len(free) == 1 else Q
    val_q0 = sp.N(trM.subs(q_used, Q0_CANONICAL), 30)
    # Substitute r = q^(1/2) to recover a polynomial-in-r form for the
    # downstream pole-order analysis. r=q^(1/2) gives q=r².
    # Use the hoefsmit Q symbol for pole_order_at_zero (it Poly's on Q internally);
    # substitute the markov_peel q → Q^2 so the r-coords pole = lowest power in Q.
    trM_in_r = sp.cancel(trM.subs(q_used, Q ** 2))
    pole, leading = pole_order_at_zero(trM_in_r)
    print(f"  canonical Markov pole order at r=q^(1/2)=0 : {pole}")
    print(f"  canonical Markov leading coefficient (r)   : {leading}")
    print(f"  canonical Markov value at q_0              : {val_q0}")

    # Write witness JSON.
    out = HERE / "deuteron_tr_M_symbolic.witness.json"
    witness = {
        "computation": "deuteron-tr_M-symbolic",
        "description": (
            "Closed-form symbolic Markov trace of the internal A=2 "
            "(deuteron) braid in H_6(q), via the canonical Wenzl-"
            "Ocneanu y_λ·χ^λ formula (matches AGENTS.md §7a "
            "`thm:jones-markov-trace`). Migrated from the historical "
            "Plancherel-trace formula on 2026-05-17 per audit doc "
            "2026-05-17-dual-tr-m-discrepancy.md — no fallback."
        ),
        "atom": {"Z": 1, "N": 1, "A": 2, "include_inter": False},
        "n_strands": 6,
        "n_crossings": len(deut),
        "n_partitions": len(parts),
        "trace_convention": "wenzl_ocneanu_markov",
        "tr_M_in_r_coords_numerator": str(sp.numer(trM_in_r)),
        "tr_M_in_r_coords_denominator": str(sp.denom(trM_in_r)),
        "r_coord_note": "r = q^(1/2), the Wenzl Markov-parameter convention",
        "pole_order_at_q0_in_r": (int(pole) if pole is not None else None),
        "leading_coefficient_in_r": str(leading) if leading is not None else None,
        "value_at_q0": str(val_q0),
        "per_partition": {str(k): v for k, v in chi_per_lam.items()},
        "total_compute_seconds": round(dt_total, 2),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        # Lean SDP-uniqueness cross-reference (PR #1537/#1542/#1554).
        "lean_uniqueness_ref": {
            "deuteron": "qou:QOU.BraidKnot.deuteron_uniqueness_closed",
            "framework_doc": (
                "folio/quantum-observable-universe/lean/QOU/BraidKnot/"
                "NucleusEmptySDPUniqueness.lean"
            ),
            "note": (
                "Certifies T_w uniqueness at the abstract empty-"
                "constraint SDP level (PR #1537 parameterised module). "
                "Workplan: docs/workplans/2026-05-31-witness-lean-"
                "uniqueness-ref-wiring.md."
            ),
        },
    }
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2))
    print()
    print(f"witness written: {out.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
