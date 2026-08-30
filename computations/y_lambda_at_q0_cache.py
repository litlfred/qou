#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; symbolic y_λ
# polynomials live upstream in y-lambda-wenzl-bridge-symbolic-witness.json.
"""One-shot cache of y_λ(q_0) numeric values for n ∈ {2, ..., 12}.

The Wenzl-bridge symbolic y_λ(q) polynomials in
[`y-lambda-wenzl-bridge-symbolic-witness.json`](y-lambda-wenzl-bridge-symbolic-witness.json)
have raw lengths up to 45k characters per partition for n = 12,
making `evalf(50)` evaluation slow (~10 seconds per partition for
n = 12, so ~13 minutes for all 77 partitions of 12 in series).

This script does the symbolic → numeric evaluation **once**,
parallelised across CPU cores via `multiprocessing.Pool`, and
writes the 50-dps decimal strings to
`y-lambda-at-q0.witness.json` for fast downstream reuse by
`delta_lambda_empirical_tabulation.py` and any other ρ_K consumer.

Output: `y-lambda-at-q0.witness.json` keyed by n → list of
{partition, y_at_q0_50dps}.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from multiprocessing import Pool, cpu_count
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

mp.mp.dps = 60   # eval headroom; we serialise the leading 50 dps

from q_parameter import Q_MP  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402

Q_MP_STR = str(Q_MP)


def _eval_one(args: tuple) -> dict:
    """Worker: evaluate y_λ at q = q_0 to 50 dps, from the LIVE formula.

    CONVENTION (2026-08-10, bean `qou-eea0` pass 2).  This used to
    `sp.sympify` the `y_lambda_symbolic` strings out of
    `y-lambda-wenzl-bridge-symbolic-witness.json` and evaluate those.  That
    witness was written under convention C — its entries carry `sqrt(q)` /
    `q**(3/2)`, the half-argument variable of `z = 1/(q^{1/2}+q^{-1/2})`,
    which convention D never produces because D stays inside ℚ(q).

    `y_lambda_wenzl_bridge` already guards against exactly this: its
    `_cached_symbolic_agrees` gate (bean `qou-wgta` item 3) re-checks the
    cached string against the module's live numeric y_λ and falls back to
    recompute when they disagree.  But that gate lives on the module's
    symbolic entry point, and this script never called it — it opened the
    JSON and parsed the strings itself, so the gate never ran and convention
    C was served intact.

    That mattered out of proportion to one file.  `y-lambda-at-q0` is the
    root of the nuclear layer: `rho_k_h3a_*`, the per-irrep pole atoms and
    the H₆/H₉/H₁₂ chi witnesses all read it, directly or transitively.  Every
    one of those producers had been migrated to D and re-run, and every one
    faithfully reproduced C, because their input did.  That is why pass 2's
    first sweep cleared 2 of 54 witnesses while reporting 90 producers "ok" —
    the re-runs were correct and the number they were given was not.

    So take the number from the formula, not from a cache: call the module's
    numeric entry point, which IS convention D (verified at n=3 — λ=[1,1,1]
    evaluates to exactly 0, the structural collapse of the 3+-row blocks that
    D exists to produce, against C's 0.0227449425773...).
    """
    n, partition = args
    mp.mp.dps = 60
    q0 = mp.mpf(Q_MP_STR)
    with mp.workdps(60):
        val = y_lambda_wenzl_bridge_numeric(list(partition), q0, dps=50)
    # Per Copilot PR #619 review: trim to exactly 50 dps so the field
    # name ("y_at_q0_50dps") matches the stored precision (was ~60 dps).
    s = mp.nstr(val, 50, strip_zeros=False)
    return {"n": n, "partition": list(partition), "y_at_q0_50dps": s}


def main() -> int:
    # Construct WitnessBuilder up front to capture full durationMs
    # (Copilot PR #619 review).
    from witness_base import WitnessBuilder
    w = (WitnessBuilder("y-lambda-at-q0", engine="mpmath")
         .set_description(
            "Numeric cache of y_λ(q_0) at 50 dps for n ∈ {2, ..., 12}, "
            "evaluated from y-lambda-wenzl-bridge-symbolic-witness.json "
            "in parallel via multiprocessing.Pool. Pre-computes the "
            "expensive symbolic-to-numeric step so downstream consumers "
            "(delta_lambda_empirical_tabulation.py and other ρ_K "
            "Wedderburn-weighted formulas) can load instantly. "
            "Output strings trimmed to exactly 50 dps via mp.nstr."
         )
         .set_content_block("prop:y-lambda-closed-form-wenzl-bridge"))

    print("=" * 96)
    print("  y_λ(q_0) numeric cache builder (parallel)")
    print("=" * 96)

    src = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
    if not src.exists():
        print(f"  ERROR: missing source witness {src}")
        return 1
    d = json.loads(src.read_text())
    tab = d["tables_by_n"]

    # Build worker tasks: (n, partition_tuple, sym_str)
    tasks = []
    for n_str, entry in sorted(tab.items(), key=lambda kv: int(kv[0])):
        n = int(n_str)
        # Don't shadow the WitnessBuilder `w` defined above with the
        # loop variable (Copilot PR #619 review pre-emptively dodged).
        for wt in entry["weights"]:
            # STRUCTURE ONLY from the source witness — which λ, at which n,
            # in which order. The `y_lambda_symbolic` value beside it is
            # convention C and is deliberately NOT read; see `_eval_one`.
            # A partition of n is combinatorics, not a convention, so taking
            # the index from a C-era file preserves coverage and ordering
            # without importing one of its numbers.
            tasks.append((n, tuple(wt["partition"])))
    print(f"  Tasks: {len(tasks)} y_λ evaluations across n ∈ "
          f"{[int(k) for k in tab.keys()]}")
    nproc = max(1, cpu_count() - 1)
    print(f"  Parallel pool: {nproc} workers")

    with Pool(nproc) as pool:
        results = pool.map(_eval_one, tasks)

    # Group by n
    by_n: dict[int, list[dict]] = {}
    for r in results:
        by_n.setdefault(r["n"], []).append({
            "partition": r["partition"],
            "y_at_q0_50dps": r["y_at_q0_50dps"],
        })

    print(f"\n  Per-n summary:")
    for n in sorted(by_n.keys()):
        print(f"    n = {n:>2}: {len(by_n[n])} partitions cached")

    # Sanity-check a few values against existing per-atom witnesses.
    sanity = {}
    spot_files = {
        "deuteron": ("chi-deuteron-h6.witness.json", 6),
        "tritium": ("chi-tritium-h9.witness.json", 9),
        "helium-3": ("chi-helium-3-h9.witness.json", 9),
        "helium-4": ("chi-helium-4-h12-at-q0-50dps.witness.json", 12),
    }
    for atom, (fname, n) in spot_files.items():
        path = HERE / fname
        if not path.exists():
            continue
        try:
            ad = json.loads(path.read_text())
            # 4He carries a per-λ y table; the others are chi-only. Two
            # spellings exist: the legacy `per_partition`/`y_at_q0`, and the
            # `-at-q0-50dps` family's `by_partition`/`y_lambda`, which 4He now
            # uses since chi-helium-4-h12-numeric had no producer and sat at
            # the superseded muon-anchored q_0.
            ref = None
            for key, yfield in (("per_partition", "y_at_q0"),
                                ("by_partition", "y_lambda")):
                if key not in ad:
                    continue
                # take the first non-zero contribution
                for entry in ad[key]:
                    if abs(float(entry.get(yfield, "0"))) > 1e-30:
                        ref = (tuple(entry["partition"]),
                               mp.mpf(entry[yfield]))
                        break
                if ref is not None:
                    break
            if ref is None:
                continue
            ref_lam, ref_val = ref
            cached = next((r for r in by_n[n]
                          if tuple(r["partition"]) == ref_lam), None)
            if cached is None:
                continue
            cached_val = mp.mpf(cached["y_at_q0_50dps"])
            rel_err = abs(cached_val - ref_val) / abs(ref_val)
            sanity[atom] = {
                "lambda": list(ref_lam),
                "ref_y_at_q0": str(ref_val),
                "cached_y_at_q0": str(cached_val),
                "rel_err": str(rel_err),
                # Compared in mpmath, not float64. `rel_err` is computed at
                # mp.dps = 50 and the bar sits at 1e-15; round-tripping it
                # through binary64 to make the comparison narrows a 50-digit
                # quantity to ~16 digits for no reason (bean qou-srvu, riding
                # on the assertion drain). The emitted boolean is unchanged.
                "agrees_to_1e_minus_15": bool(rel_err < mp.mpf("1e-15")),
            }
            tag = "✓" if rel_err < mp.mpf("1e-15") else "✗"
            print(f"    {tag} {atom} λ={list(ref_lam)}: rel_err = {mp.nstr(rel_err, 6)}")
        except Exception as exc:
            sanity[atom] = {"error": f"{type(exc).__name__}: {exc}"}

    # WitnessBuilder constructed at start of main(); now populate.
    w.parameters.update({
        "q_0": Q_MP_STR,
        "precision_dps": 50,
        "n_values": sorted(by_n.keys()),
        "n_total_partitions": len(tasks),
    })
    w.add_data("by_n", {str(n): by_n[n] for n in sorted(by_n.keys())})
    w.add_data("sanity_check", sanity)
    # Assertions (bean qou-srvu). This witness carried none, so `allPassed:
    # true` was vacuous. The check already existed: each entry of
    # `sanity_check` compares this cache's `y_at_q0_50dps` against an
    # INDEPENDENTLY computed reference for the same partition and records
    # `rel_err` + `agrees_to_1e_minus_15`. It was stored as data and never
    # asserted. Nothing new is claimed.
    #
    # THRESHOLD PROVENANCE: 1e-15 is this file's own declared bar AND the
    # framework's L1 target (1 ppQ, see AGENTS.md "Precision goals"). It is
    # not fitted -- the measured margin is ~35 orders of magnitude
    # (helium-4 rel_err 5.04e-50 against a 1e-15 bar), and the arithmetic is
    # mpmath at 50 dps, so the bar sits far above the arithmetic floor rather
    # than at it.
    _scored = {k: v for k, v in sanity.items() if "rel_err" in v}
    if _scored:
        w.add_assertion(
            "cached_y_lambda_agrees_with_independent_reference_count",
            computed=str(sum(1 for v in _scored.values()
                             if v["agrees_to_1e_minus_15"])),
            expected=str(len(_scored)),
            source="per-atom |cached - ref|/|ref| against the L1 1 ppQ target "
                   "1e-15; expected is the number of atoms with a reference, "
                   "not a number matched to the result",
        )
        _worst = max(_scored.values(), key=lambda v: mp.mpf(v["rel_err"]))
        w.add_assertion(
            "cached_y_lambda_worst_relative_error",
            computed=_worst["rel_err"],
            expected="0",
            tolerance="1e-15",
            source="largest per-atom relative error across `sanity_check`; "
                   "computed at mp.dps = 50, so the 1e-15 bar is well above "
                   "the arithmetic floor rather than at it",
        )
    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
