#!/usr/bin/env python3
"""
per_irrep_pole_atom.py — Generalised Path A pole-order verification
of `prop:per-nucleon-shift-additive-linearity` for any atom (Z, N).

Same recipe as per_irrep_pole_proton_h3 / per_irrep_pole_deuteron_h6,
parameterised by (Z, N) and parallelised across partitions:

  1. Load cached symbolic y_λ(q) at n = 3(Z+N) from
     `y-lambda-wenzl-bridge-symbolic-witness.json` (n=2-12 cached).
  2. Load (or compute + cache) symbolic χ^λ_q(β_atomic(Z, N)) per
     partition λ ⊢ n.  Cache: chi-{atom}-h{n}.witness.json.  First-
     run uses multiprocessing.Pool over partitions (n=9 has 30
     partitions; n=12 has 77).
  3. Substitute q = u² in both factors per partition; compute
     ord_{u=0}(y_λ · χ^λ).  Take max — when the maximum is uniquely
     achieved (lower-order terms cannot cancel a strict max), the
     full-sum u-pole order equals the per-term max rigorously.

**Predicted shifts** (from `prop:per-nucleon-shift-additive-linearity`):

  - (Z=1, N=2)  T    n=9   shift = 18·1 + 21·2 + 1 = 61
  - (Z=2, N=1)  ³He  n=9   shift = 18·2 + 21·1 + 1 = 58
  - (Z=2, N=2)  ⁴He  n=12  shift = 18·2 + 21·2 + 1 = 79
  - (Z=3, N=2)  ⁵Li  n=15  shift = 18·3 + 21·2 + 1 = 97
  - (Z=3, N=3)  ⁶Li  n=18  shift = 18·3 + 21·3 + 1 = 118

Witness: per-irrep-pole-{atom}-h{n}.witness.json (CI-integrated)
Chi cache: chi-{atom}-h{n}.witness.json

## Provisioning

Set `--workers` to the **number of CPU cores** (`nproc`) and run
**one atom at a time**, sequentially.  Over-provisioning (e.g.
`--workers 8` on a 4-core machine, or running multiple atoms in
parallel) triples per-shape wall time due to scheduler contention
without any throughput benefit.  Profile data: a single shape at
$H_6$ takes ~13 s on a clean core, ~40 s under 3× over-provision.
See `docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md`
§"Performance note" for the full investigation.

The chi cache is permanent (incrementally saved per partition), so a
sequential atom schedule is no slower than a concurrent one.

Audit doc: docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md

@module folio-assistant/computations/per_irrep_pole_atom
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import json
import os
import sys
import time
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from per_irrep_pole_proton_h3 import negative_q_pole_order  # noqa: E402
from q_parameter import Q as Q0_FLOAT  # noqa: E402  authoritative q_0
from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402

Y_LAMBDA_CACHE = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"

# Precision (decimal places) for the per-partition χ-fingerprint
# emitted under `atom_chi_fingerprint`.  Centralised constant per
# Gemini review (PR #607).
FINGERPRINT_PRECISION = 8

ATOMS = {
    "proton":   (1, 0),
    "neutron":  (0, 1),
    "deuteron": (1, 1),
    "tritium":  (1, 2),
    "helium-3": (2, 1),
    "helium-4": (2, 2),
    "lithium-5":(3, 2),
    "lithium-6":(3, 3),
    "lithium-7": (3, 4),
    "beryllium-8": (4, 4),
    "beryllium-9": (4, 5),
}

ATOM_ALIASES = {
    "p": "proton", "n": "neutron", "D": "deuteron", "T": "tritium",
    "3He": "helium-3", "4He": "helium-4", "5Li": "lithium-5",
    "6Li": "lithium-6", "7Li": "lithium-7", "8Be": "beryllium-8",
    "9Be": "beryllium-9",
}


def parts_of(n: int) -> list[tuple[int, ...]]:
    out = []
    def rec(rem: int, cap: int, acc: list[int]) -> None:
        if rem == 0:
            out.append(tuple(acc))
            return
        for k in range(min(cap, rem), 0, -1):
            rec(rem - k, k, acc + [k])
    rec(n, n, [])
    return out


def load_y_lambda_symbolic(n: int, q_sym: sp.Symbol) -> dict[tuple, sp.Expr]:
    """Load cached symbolic y_λ(q) for given n from the Wenzl-bridge witness."""
    d = json.loads(Y_LAMBDA_CACHE.read_text())
    if str(n) not in d["tables_by_n"]:
        raise ValueError(f"y_λ cache has no entry for n = {n}")
    out: dict[tuple, sp.Expr] = {}
    for w in d["tables_by_n"][str(n)]["weights"]:
        lam = tuple(w["partition"])
        expr = sp.sympify(w["y_lambda_symbolic"])
        free = expr.free_symbols
        if free:
            other_q = next(iter(free))
            if other_q is not q_sym:
                expr = expr.subs(other_q, q_sym)
        out[lam] = expr
    return out


# Top-level worker for multiprocessing.Pool — must be picklable.
def _chi_worker(args):
    """Compute chi_lambda_symbolic for one partition; returns (lam, str)."""
    lam, crossings = args
    # Re-import inside worker (multiprocessing fork-safety)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from hoefsmit_symbolic import chi_lambda_symbolic
    chi = chi_lambda_symbolic(lam, crossings)
    return lam, str(chi)


def _write_chi_cache(
    cache_path: Path, atom_name: str, Z: int, N: int, n: int,
    out_str: dict[tuple, str], elapsed: float, workers_eff: int,
    partial: bool,
) -> None:
    """Persist (or update) the chi cache JSON, including partial state."""
    cache_payload = {
        "description": (
            f"Symbolic χ^λ_q(β_atomic({Z}, {N})) — {atom_name} — "
            f"for the canonical atomic braid word at H_{n}, per "
            f"partition λ ⊢ {n}.  Incrementally saved per partition "
            f"so a SIGTERM/timeout mid-loop preserves work done so far."
            + (" PARTIAL — re-run to continue."
               if partial else "")
        ),
        "atom": atom_name,
        "Z": Z,
        "N": N,
        "n": n,
        "n_partitions": len(out_str),
        "n_partitions_total": len(parts_of(n)),
        "partial": partial,
        "compute_time_sec_so_far": elapsed,
        "workers": workers_eff,
        "auditOnly": "docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md",
        "chi_lambda_symbolic": [
            {"partition": list(lam), "chi_q_symbolic": s}
            for lam, s in sorted(out_str.items(),
                                 key=lambda kv: tuple(-x for x in kv[0]))
        ],
    }
    cache_path.write_text(json.dumps(cache_payload, indent=2))


def load_or_build_chi_atom(
    Z: int, N: int, atom_name: str, q_sym: sp.Symbol,
    *, workers: int | None = None,
) -> tuple[dict[tuple, sp.Expr], float]:
    """Load (or compute + cache) symbolic χ^λ_q(β_atomic(Z, N)) for each λ ⊢ 3(Z+N).

    The cache supports **incremental saves**: each completed partition
    is appended and the JSON is rewritten so a SIGTERM/timeout mid-loop
    preserves the work done so far.  Re-running the script on the
    partial cache will skip already-cached partitions and only compute
    the remaining ones.
    """
    n = 3 * (Z + N)
    cache_path = HERE / f"chi-{atom_name}-h{n}.witness.json"
    cached_str: dict[tuple, str] = {}
    cached_was_partial = False
    if cache_path.exists():
        d = json.loads(cache_path.read_text())
        for entry in d["chi_lambda_symbolic"]:
            lam = tuple(entry["partition"])
            cached_str[lam] = entry["chi_q_symbolic"]
        cached_was_partial = bool(d.get("partial", False))
    crossings = atom_canonical_crossings(Z, N)
    shapes = parts_of(n)
    missing = [sh for sh in shapes if sh not in cached_str]
    workers_eff = workers if workers else max(1, os.cpu_count() or 1)
    n_have = len(cached_str)
    if not missing and not cached_was_partial:
        print(f"  (chi cache complete: {n_have}/{len(shapes)} cached)")
    else:
        print(f"  (chi cache: {n_have}/{len(shapes)} cached; "
              f"computing {len(missing)} more, {workers_eff} workers)")
    t0 = time.time()
    if missing:
        if workers_eff > 1 and len(missing) > 1:
            with Pool(processes=workers_eff) as pool:
                for lam, chi_str in pool.imap_unordered(
                    _chi_worker, [(sh, crossings) for sh in missing],
                ):
                    cached_str[lam] = chi_str
                    # incremental save so timeout doesn't lose work
                    _write_chi_cache(
                        cache_path, atom_name, Z, N, n, cached_str,
                        time.time() - t0, workers_eff,
                        partial=(len(cached_str) < len(shapes)),
                    )
                    print(f"    λ={str(lam):24} chi computed "
                          f"({time.time() - t0:.1f}s; "
                          f"{len(cached_str)}/{len(shapes)} done)")
        else:
            for sh in missing:
                lam, chi_str = _chi_worker((sh, crossings))
                cached_str[lam] = chi_str
                _write_chi_cache(
                    cache_path, atom_name, Z, N, n, cached_str,
                    time.time() - t0, workers_eff,
                    partial=(len(cached_str) < len(shapes)),
                )
    elapsed = time.time() - t0
    out: dict[tuple, sp.Expr] = {}
    for lam, s in cached_str.items():
        expr = sp.sympify(s)
        free = expr.free_symbols
        if free:
            other_q = next(iter(free))
            if other_q is not q_sym:
                expr = expr.subs(other_q, q_sym)
        out[lam] = expr
    if elapsed > 0:
        print(f"  chi cache: +{elapsed:.1f}s new compute; "
              f"{len(cached_str)}/{len(shapes)} total")
    # Discard the rest of the original block — replaced by helper above.
    return out, elapsed


def run_atom(Z: int, N: int, *, workers: int | None = None) -> int:
    """Run Path A for the given (Z, N) atom and emit its witness."""
    n = 3 * (Z + N)
    # Resolve atom name
    atom_name = next((k for k, v in ATOMS.items() if v == (Z, N)), None)
    if atom_name is None:
        atom_name = f"z{Z}n{N}"

    q_var = sp.symbols("q", positive=True)
    u_var = sp.symbols("u", positive=True)
    expected_shift = 18 * Z + 21 * N + 1

    print("=" * 80)
    print(f"  Per-irrep pole order — {atom_name} β(Z={Z}, N={N}) at H_{n} (Path A)")
    print("=" * 80)
    print()

    t0 = time.time()
    print(f"  Loading cached symbolic y_λ(q) for n={n} ...")
    y_lams_q = load_y_lambda_symbolic(n, q_var)
    print(f"    loaded {len(y_lams_q)} partitions in {time.time() - t0:.2f} s")

    print()
    print(f"  Loading (or computing) chi_λ(β_{{{Z},{N}}}) ...")
    chi_q, build_time = load_or_build_chi_atom(
        Z, N, atom_name, q_var, workers=workers,
    )
    if build_time == 0.0:
        print(f"    loaded {len(chi_q)} cached chi_λ values (instant)")
    else:
        print(f"    built + cached {len(chi_q)} chi_λ values in {build_time:.1f} s")

    print()
    print(f"  Substituting q = u² and computing per-term u-pole orders ...")
    t0 = time.time()
    term_pole_orders: dict[tuple, int] = {}
    for lam in y_lams_q:
        y_u = y_lams_q[lam].subs(q_var, u_var ** 2)
        chi_u = chi_q[lam].subs(q_var, u_var ** 2)
        term = y_u * chi_u
        ord_u = negative_q_pole_order(term, var=u_var)
        term_pole_orders[lam] = ord_u
    print(f"    per-term loop: {time.time() - t0:.1f} s")

    print()
    print(f"    {'λ':<28}{'ord_u=0(y_λ · χ^λ)':>22}")
    print("    " + "-" * 50)
    for lam in sorted(term_pole_orders, key=lambda L: -term_pole_orders[L]):
        print(f"    {str(lam):<28}{term_pole_orders[lam]:>22}")

    max_lam = max(term_pole_orders, key=term_pole_orders.get)
    max_pole = term_pole_orders[max_lam]
    sorted_orders = sorted(term_pole_orders.values(), reverse=True)
    next_highest = sorted_orders[1] if len(sorted_orders) > 1 else -1
    unique_max = max_pole > next_highest

    print()
    print(f"  Maximizer:    λ = {max_lam}, per-term pole = {max_pole}")
    print(f"  Next-highest pole: {next_highest}  (unique max: {unique_max})")
    print(f"  Predicted shift_NF({atom_name}) = "
          f"18·{Z} + 21·{N} + 1 = {expected_shift}")
    success = unique_max and max_pole == expected_shift
    if success:
        print(f"  ✓ Path A verified: ord_{{u=0}}(tr_M(β_{atom_name})) "
              f"= {max_pole}, matching prop:per-nucleon-shift-additive-"
              f"linearity exactly.")
    else:
        print(f"  ✗ Path A inconclusive at A={Z + N} for {atom_name}")
        if not unique_max:
            print(f"    (max is not unique → cancellation check needed)")
        if max_pole != expected_shift:
            print(f"    (max pole {max_pole} ≠ predicted {expected_shift})")

    builder = (
        WitnessBuilder(name=f"per-irrep-pole-{atom_name}-h{n}", engine="sympy")
        .set_description(
            f"Path A: per-term symbolic u-pole-order analysis of the "
            f"{atom_name}'s tr_M = Σ_λ y_λ(q) · χ^λ_q(β_{{{Z},{N}}}) "
            f"at q = u² (per the D(u) convention).  Loads cached "
            f"symbolic y_λ from y-lambda-wenzl-bridge-symbolic-"
            f"witness.json and cached chi_λ from chi-{atom_name}-h{n}"
            f".witness.json (auto-emit on first run, multiprocessing).  "
            f"Per-term ord_{{u=0}}(y_λ · χ^λ) avoids the sp.together "
            f"bottleneck.  Verifies shift_NF(β_{atom_name}) = "
            f"{expected_shift} = 18·{Z} + 21·{N} + 1, matching "
            f"prop:per-nucleon-shift-additive-linearity."
        )
        .set_audit_only(
            "docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md"
        )
    )
    per_term = []
    for lam in sorted(term_pole_orders, key=lambda L: -term_pole_orders[L]):
        per_term.append({
            "partition": list(lam),
            "ord_u_eq_0_y_lambda_times_chi": int(term_pole_orders[lam]),
        })
    builder.add_data("per_term_u_pole_orders", per_term)
    builder.add_data("max_term_lambda", {
        "partition": list(max_lam),
        "ord_u_eq_0": int(max_pole),
        "unique_max": bool(unique_max),
        "next_highest": int(next_highest),
    })
    builder.add_data("full_tr_M_u_pole_inferred", {
        "value": int(max_pole),
        "rigorous": bool(unique_max),
        "expected": expected_shift,
        "Z": Z,
        "N": N,
        "formula": f"shift_NF(β_{atom_name}) = 18·{Z} + 21·{N} + 1 = {expected_shift}",
    })
    builder.add_assertion(
        name=f"{atom_name}_full_tr_M_u_pole_eq_shift_NF",
        computed=int(max_pole),
        expected=expected_shift,
    )
    builder.add_assertion(
        name=f"{atom_name}_per_term_max_unique",
        computed=int(unique_max),
        expected=1,
    )

    # Per-generator crossing inventory (GAP-C-1 partial closure).
    # The q-integer-mass-formula.md narrative cites empirical counts
    # like "7 crossings on generator 0" without machine-verifiable
    # backing.  Emit the canonical list here so future work can wire
    # per-generator pole-order disaggregation onto a structural
    # baseline.
    crossings = atom_canonical_crossings(Z, N)
    per_gen: dict[int, dict[str, int]] = {}
    for gen_idx, ctype in crossings:
        slot = per_gen.setdefault(int(gen_idx),
                                   {"sigma": 0, "sigma_inv": 0, "averaged": 0})
        slot[ctype] = slot.get(ctype, 0) + 1
    # KLR-canonical-basis enrichment per gen (PR #608 cemetery infra).
    # σ_g^k pure-power sub-words are by construction *cemetery* — they
    # close to identity / unknots.  We tag each generator with its net
    # signed power (σ count − σ⁻¹ count, ignoring "averaged" which is
    # an off-Markov mixed crossing) so the cemetery class is identified
    # without needing a full H_n cemetery enumeration.
    klr_per_gen = []
    for g in sorted(per_gen):
        slot = per_gen[g]
        net_power = slot.get("sigma", 0) - slot.get("sigma_inv", 0)
        avg_count = slot.get("averaged", 0)
        klr_per_gen.append({
            "gen_idx": g,
            "net_signed_power": net_power,
            "averaged_count": avg_count,
            # Cemetery class label: the *signed-power projection* of
            # this generator's sub-word, ignoring averaged crossings.
            # If averaged_count > 0, this label is a projection only.
            "cemetery_class_signed_power_projection": (
                f"σ_{g}^{net_power}" if net_power != 0 else "identity"
            ),
            # Pure-power means the sub-word is exactly σ_g^k with no
            # averaged (mixed / off-Markov) crossings.  Only then is
            # the cemetery-class label a complete invariant of the
            # sub-word.
            "is_pure_power_in_cemetery": avg_count == 0,
        })
    per_gen_emit = [
        {"gen_idx": g, **per_gen[g], "total": sum(per_gen[g].values())}
        for g in sorted(per_gen)
    ]
    builder.add_data("per_generator_crossings", {
        "atom": atom_name,
        "Z": Z,
        "N": N,
        "n_strands": n,
        "total_crossings": len(crossings),
        "by_generator": per_gen_emit,
        "klr_canonical_class_by_generator": klr_per_gen,
        "note": (
            "Canonical crossings from atom_canonical_crossings(Z, N), "
            "aggregated per generator index.  Provides structural "
            "baseline for GAP-C-1 (q-integer counting per generator) "
            "in derivation-audit-report.md.  KLR-canonical-class "
            "enrichment per CLAUDE.md §7b (and PR #608 KLR cemetery "
            "infra): each per-generator sub-word σ_g^k (pure power) "
            "is a cemetery class trivially; the full atom's "
            "canonical class is the per-partition χ-fingerprint at "
            "q_0 (emitted as `atom_chi_fingerprint` below)."
        ),
    })

    # Atom-level KLR canonical-basis fingerprint at q_0.
    # Trace-only χ^λ(β; q_0) tuple — same canonical-basis class iff
    # all per-partition characters agree at the chosen precision
    # (cf. r5_full_canonical_knot_solver.chi_fingerprint, which uses
    # the per-block matrix entries at H_3; here we use trace-only
    # because the per-block matrices are not currently materialised
    # in the Path A pipeline at H_n for n > 3).  Q0_FLOAT is imported
    # at module top from q_parameter (per Gemini review PR #607).
    chi_fp_pairs = []
    for lam in sorted(chi_q, key=lambda L: (-len(L), tuple(-x for x in L))):
        try:
            val = float(chi_q[lam].subs(q_var, Q0_FLOAT))
            chi_fp_pairs.append((list(lam), round(val, FINGERPRINT_PRECISION)))
        except (TypeError, ValueError):
            chi_fp_pairs.append((list(lam), None))
    builder.add_data("atom_chi_fingerprint", {
        "q0": float(Q0_FLOAT),
        "precision": FINGERPRINT_PRECISION,
        "n_partitions": len(chi_fp_pairs),
        "fingerprint": chi_fp_pairs,
        "note": (
            "Per-partition χ^λ(β_atom; q_0) tuple — heuristic "
            "comparison hash for braid/Markov-equivalence at q_0.  "
            "It is a NECESSARY but NOT SUFFICIENT condition for "
            "canonical-basis (KL) equivalence: identical fingerprints "
            "are evidence of equivalence, but two distinct "
            "canonical-basis classes can collide at the rounded-trace "
            "level (no iff guarantee).  Trace-only form because "
            "per-block matrices are not currently materialised at "
            "H_n>3 in Path A — full equivalence requires the per-"
            "block matrix entries (cf. "
            "r5_full_canonical_knot_solver.chi_fingerprint at H_3). "
            "Per Copilot review #r3213426336."
        ),
    })

    builder.add_data("lean_uniqueness_ref", lean_uniqueness_ref("per-nucleus (H_6 deuteron / per-atom)"))
    out_path = builder.save()
    print(f"\n  Witness emitted: {out_path}")
    return 0 if success else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "atoms", nargs="+",
        help=f"Atom names: {sorted(set(ATOMS) | set(ATOM_ALIASES))}",
    )
    parser.add_argument(
        "--workers", type=int, default=None,
        help="multiprocessing.Pool size for chi cache build",
    )
    args = parser.parse_args()
    rc = 0
    for raw in args.atoms:
        atom = ATOM_ALIASES.get(raw, raw)
        if atom not in ATOMS:
            print(f"Unknown atom: {raw}", file=sys.stderr)
            rc = 2
            continue
        Z, N = ATOMS[atom]
        rc |= run_atom(Z, N, workers=args.workers)
        print()
    return rc


if __name__ == "__main__":
    sys.exit(main())
