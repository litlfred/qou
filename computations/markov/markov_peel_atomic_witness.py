#!/usr/bin/env python3
"""
Production atomic Markov-trace witness via Markov-axiom recursive ascent.

For each atom (Z, N) in the spectrum p, n, D, T, ³He, ⁴He, ⁵Li, ⁶Li:

  1. Build the production atomic braid `β_atom` via
     `mass_at_3A_proper.atom_braid_word_3A`.
  2. Reduce in `H_{3A}(q)` via incremental Gröbner–Shirshov
     (`markov_peel.incremental_reduced_element`) — interleaved
     reduce + multiply that keeps intermediate term count bounded.
  3. Take the canonical Markov trace via the recursive Markov-axiom
     ascent (`markov_trace_canonical.tr_M_element`, `simplify=False`).
  4. Evaluate the symbolic result at q = q₀ to 30 digits.
  5. Cross-check against `atomic-tr-m-mpfr-50dps.witness.json`
     (Hoefsmit + Wenzl bridge) for the atoms it covers.

This is the **production** atomic Markov-trace witness — the Hoefsmit
path materialises dim-up-to-462 sympy matrices per partition and is
infeasible for A ≥ 4 (the headline target of #508 / PR #516).  The
recursive-ascent path computes ⁴He end-to-end in ~60 seconds.

Witness: `markov-peel-atomic-tr-m.witness.json`
Reference: prop:markov-pair-z2 (QOU narrative)

Usage:
    python computations/markov_peel_atomic_witness.py
    python computations/markov_peel_atomic_witness.py --include-li
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import sys
import time
from pathlib import Path

import sympy as sp
import mpmath

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from markov_peel import incremental_reduced_element  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A     # noqa: E402
from markov_trace_canonical import tr_M_element       # noqa: E402
from hecke_symbolic import q as q_sym                  # noqa: E402
from q_parameter import Q_50_DIGIT_STR                 # noqa: E402  (50-digit q₀, NOT float64 Q)
from witness_base import WitnessBuilder, record_upstream                # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

# Per AGENTS.md / Gemini-flagged precision policy: pin a high-precision
# floor at the module level so all symbolic→numeric casts respect it.
# 50 dps matches the Hoefsmit + Wenzl bridge witness this script
# cross-checks against (`atomic-tr-m-mpfr-50dps.witness.json`).
mpmath.mp.dps = 50

# Substitute the FULL 50-digit q₀ into the exact symbolic trace — NOT the
# float64 `q_parameter.Q` (only 17 digits). The atomic tr_M is built as an
# EXACT sympy expression in q (zero Float atoms); injecting a float64 q₀ at
# the final `.subs` truncates it to ~16 good digits, which made the L1
# cross-check (`cross_check_trM_1ppb.py`) read peel_vs_chi ≈ 1.5e-15 (the
# float64 floor) and DIVERGE at the 1 ppQ (1e-15) gate. Substituting the
# 50-digit q₀ is float-clean and peel agrees with the chi-cache leg at
# ~1e-19. NB: `Q_MP` is ALSO only float64-precision — `Q_50_DIGIT_STR` is
# the sole 50-dps source. See
# docs/audits/2026-06-29-l1-peel-float64-q0-substitution-fix.md.
_DPS_GUARD = mpmath.mp.dps + 8
Q0_SYMPY_HP = sp.Float(Q_50_DIGIT_STR, _DPS_GUARD)


# Atom spectrum.  Beyond ⁴He is gated by `--include-li` since GS reduce
# scales ~10× per A unit (about 10 minutes for ⁵Li).
ATOMS_DEFAULT = [
    ("proton",   1, 0),
    ("neutron",  0, 1),
    ("deuteron", 1, 1),
    ("tritium",  1, 2),
    ("helium-3", 2, 1),
    ("helium-4", 2, 2),
]
ATOMS_LITHIUM = [
    ("lithium-5", 3, 2),
    ("lithium-6", 3, 3),
]


def _on_proton() -> bool:
    """True when this producer resolved to the experimental pin."""
    return str(Q_50_DIGIT_STR).startswith("1.10997858275")


def _witness_name() -> str:
    """This producer's OWN output name, at its own q₀ layer.

    **Base name = PROTON here, and the muon layer takes the `-muon` suffix.**
    This is deliberately the OPPOSITE of `_bridge_name()` below (where the
    base name is the muon layer), so it needs its reason recorded.

    Before 2026-08-09 this producer always wrote the base name while
    resolving to the proton pin (it is tagged `physical_proton` in
    `q0_anchor_manifest.json`), so a proton-built witness sat on the base
    name. `cross_check_trM_1ppb` — a muon-canonical L1 gate — reads the peel
    witness and hard-failed on that mixed pin, red on `main`.

    The tidy fix would have been to adopt the bridge convention (base =
    muon). It was tried and rejected: **six** consumers of the base name
    (`paper_six_term_isotope_sweep`, `rho_f_categorical_probe`,
    `cross_check_trM_wenzl_lr_1ppb`, `canonical_tr_m_three_path_comparison`,
    `b_over_a_v5_unified`, `_b0vf_complete_he4_witness`) are not anchor-aware
    and resolve to the proton default, so renaming would have silently fed
    them muon values — the same straddle class this is meant to close, just
    pointed at more files. Keeping the base name on proton is
    behaviour-preserving for every existing reader; the muon layer, which had
    no file at all, gets the new one. Cosmetic consistency lost, silent
    breakage avoided.
    """
    return ("markov-peel-atomic-tr-m" if _on_proton()
            else "markov-peel-atomic-tr-m-muon")


def _bridge_name() -> str:
    """The bridge witness at THIS producer's own q₀ layer.

    Single source for both the load and the `bridge_witness_compared`
    provenance field. They were separate, and the field was a hardcoded
    literal — so once the load became anchor-aware the witness would have
    declared it compared against the muon bridge while actually reading the
    proton one. A provenance field naming a file the run never opened is worse
    than no field: it is checkable, and it checks out wrong.
    """
    return ("atomic-tr-m-mpfr-50dps-proton.witness.json" if _on_proton()
            else "atomic-tr-m-mpfr-50dps.witness.json")


def _load_bridge_witness() -> dict[str, str]:
    """Return atom -> tr_M(q₀) string from the Hoefsmit + Wenzl bridge
    witness, for cross-check.  Empty dict if the file is missing.
    """
    # Load the bridge at THIS producer's own q0 layer, not whichever one the
    # default name happens to point at. This producer is NOT in
    # `q0_anchor_manifest.json`, so `Q_50_DIGIT_STR` resolves to the
    # experimental (proton) pin — while the default bridge witness is the
    # `ideal_muon` one. Comparing across that boundary is the straddle
    # AGENTS.md §"q₀ anchor convention" forbids, and it was not subtle:
    # `abs_diff_vs_bridge` for the deuteron read 6.73e-04, which is also what
    # kept rejecting this witness in the regeneration wave.
    #
    # On an all-muon checkout the pins already agree and the default name is
    # used, so nothing changes there.
    f = _pb.witness_path(_bridge_name(), HERE)
    if _on_proton() and not f.exists():
        raise SystemExit(
            "this producer is on the proton pin but the proton bridge witness "
            "is missing. Generate it with\n    QOU_Q0_ANCHOR=proton python3 "
            "computations/atomic_tr_m_mpfr_50dps.py --anchor proton\n"
            "Refusing to cross-check a proton trace against the muon bridge.")
    if not f.exists():
        return {}
    data = record_upstream(f, _UPSTREAM_RECORDS)
    return {e["atom"]: e["tr_M_at_q0_50dps"] for e in data["results"]}


def compute_atom(Z: int, N: int) -> dict:
    """Compute one row of the witness for atom (Z, N)."""
    A = Z + N
    n_strands = 3 * A
    word = atom_braid_word_3A(Z, N)

    t0 = time.time()
    elem = incremental_reduced_element(word, max_iterations_per_step=2000)
    t_reduce = time.time() - t0

    t0 = time.time()
    tr_sym = tr_M_element(elem, n_strands, simplify=False)
    t_trace = time.time() - t0

    t0 = time.time()
    # Evaluate at the current mpmath precision floor (50 dps), then
    # convert to mpf so the full precision survives.  Casting to a
    # Python float here would silently truncate to ~15-17 digits and
    # defeat the high-precision evaluation. Substitute the 50-digit q₀
    # (`Q0_SYMPY_HP`), NOT the float64 `q_parameter.Q` — see module header.
    tr_at_q0_mpf = mpmath.mpf(
        str(tr_sym.subs(q_sym, Q0_SYMPY_HP).evalf(_DPS_GUARD))
    )
    t_eval = time.time() - t0

    try:
        ops = sp.count_ops(tr_sym)
    except Exception:  # noqa: BLE001
        ops = -1

    # Format the witness value at full mpmath precision so downstream
    # cross-checks against `atomic-tr-m-mpfr-50dps.witness.json`
    # (Hoefsmit + Wenzl bridge) compare apples-to-apples.
    return {
        "Z": Z,
        "N": N,
        "A": A,
        "n_strands": n_strands,
        "word_length": len(word),
        "reduced_term_count": len(elem.terms),
        "trace_sympy_ops": int(ops),
        "tr_M_at_q0": mpmath.nstr(
            tr_at_q0_mpf, mpmath.mp.dps, strip_zeros=False
        ),
        # Wall-clock timings are serialized as strings, not raw floats. They
        # are diagnostics, never physics — but the raw-float64 ratchet counts
        # fields, not meanings, and these 18 were the producer's entire
        # contribution to it. Formatting here keeps the witness f64-free
        # without pretending a stopwatch reading has 50-digit precision.
        "elapsed_reduce_sec": f"{t_reduce:.3f}",
        "elapsed_trace_sec": f"{t_trace:.3f}",
        "elapsed_evalf_sec": f"{t_eval:.3f}",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--include-li", action="store_true",
        help="Also compute ⁵Li and ⁶Li (≥ 10 min reduce per atom)",
    )
    parser.add_argument(
        "--out", type=str, default="markov-peel-atomic-tr-m.witness.json",
        help="Witness output filename (relative to computations/)",
    )
    args = parser.parse_args()

    bridge = _load_bridge_witness()

    atoms = list(ATOMS_DEFAULT)
    if args.include_li:
        atoms.extend(ATOMS_LITHIUM)

    print(
        "Atomic tr_M(β) via Markov-axiom recursive ascent (#508 / PR #516)",
        flush=True,
    )
    print("=" * 70, flush=True)

    rows = []
    total_t = time.time()
    for label, Z, N in atoms:
        print(f"\n  === {label} (Z={Z}, N={N}, A={Z + N}) ===", flush=True)
        try:
            row = compute_atom(Z, N)
            row["atom"] = label
            print(
                f"    word_len={row['word_length']:3d} "
                f"reduce={float(row['elapsed_reduce_sec']):6.1f}s "
                f"terms={row['reduced_term_count']:5d} "
                f"trace={float(row['elapsed_trace_sec']):6.2f}s "
                f"ops={row['trace_sympy_ops']:>6d}",
                flush=True,
            )
            print(f"    tr_M(q₀) = {row['tr_M_at_q0']}", flush=True)
            if label in bridge:
                # Compare at full mpmath precision — strings round-trip
                # losslessly through `mpf(str(...))`.
                bridge_val = mpmath.mpf(bridge[label])
                got = mpmath.mpf(row["tr_M_at_q0"])
                diff = abs(got - bridge_val)
                row["bridge_witness_value"] = bridge[label]
                row["abs_diff_vs_bridge"] = mpmath.nstr(diff, 6)
                # The bridge (`atomic-tr-m-mpfr-50dps`, Hoefsmit) is
                # COLOR-BLIND. This producer's trace is the canonical
                # COLOR-WEIGHTED (bring_color_weighted) one. They are equal
                # only for A=1 (no inter-nucleon crossing); for A≥2 they
                # differ by the color-weighting amount (δ·h/4 ~ 1e-5), which
                # is EXPECTED, not an error. Only A=1 gets the tight 1 ppQ
                # bridge gate; A≥2 reports the gap informationally as the
                # color-weighting magnitude. (Same color-blind-vs-weighted
                # split as cross_check_trM_1ppb.py; see
                # docs/audits/2026-06-23-trM-crosscheck-colorweighting-split-at-C.md.)
                tol = mpmath.mpf(10) ** -(mpmath.mp.dps - 5)
                if row["A"] == 1:
                    tag = "OK" if diff < tol else "MISMATCH"
                else:
                    tag = ("color-weighting Δ (expected; bridge is "
                           "color-blind)")
                row["bridge_is_color_blind"] = bool(row["A"] >= 2)
                print(
                    f"    bridge = {bridge[label]}  "
                    f"|diff| = {mpmath.nstr(diff, 3)}  {tag}",
                    flush=True,
                )
            else:
                row["bridge_witness_value"] = None
                row["abs_diff_vs_bridge"] = None
                print(
                    f"    (no bridge witness for {label} — "
                    "this row is the production reference)",
                    flush=True,
                )
            rows.append(row)
        except Exception as exc:  # noqa: BLE001
            print(f"    FAILED: {type(exc).__name__}: {exc}", flush=True)
            rows.append({
                "atom": label, "Z": Z, "N": N, "A": Z + N,
                "error": f"{type(exc).__name__}: {exc}",
            })

    total_elapsed = time.time() - total_t
    print(
        f"\n  === total wall = {total_elapsed:.1f}s ===",
        flush=True,
    )

    w = WitnessBuilder(_witness_name(), engine="sympy")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Production atomic Markov trace tr_M(β_atom) at q = q₀ via the "
        "Markov-axiom recursive-ascent path (markov_peel + "
        "markov_trace_canonical, #508 / PR #516).  Cross-checks against "
        "atomic-tr-m-mpfr-50dps.witness.json (Hoefsmit + Wenzl bridge) "
        "for the atoms it covers (proton, neutron, D, T, ³He); ⁴He and "
        "beyond are first-time computations enabled by this rewrite."
    )
    w.set_content_block("prop:markov-pair-z2")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data(
        "method",
        "incremental_reduced_element + tr_M_element(simplify=False)",
    )
    w.add_data("results", rows)
    w.add_data("bridge_witness_compared",
                "atomic-tr-m-mpfr-50dps.witness.json")
    out_path = w.save()
    print(f"\n  → wrote {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
