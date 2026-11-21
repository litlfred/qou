#!/usr/bin/env python3
"""Probe — the UIC Pass-2 sign gate is not the operator-selection LP's active set.

`hecke_core_legacy.unified_iterative_correction` Pass 2 (`:2176-2199`) keeps a
Wedderburn block only when `final_tr_sign <= 0`, and returns that gated sum. Its
comment derives the gate from complementary slackness on a primal LP:

    LP duality theorem: on the OPTIMAL primal-dual pair (Phi*, y*),
      y_l* x <Phi*, pi_l>_F = 0  for every partition l.
    So y_l* > 0 only when the Frobenius constraint is TIGHT at the atom's
    FINAL state, i.e. tr(M_l(W_atom)) <= 0.

That LP exists — `prop:operator-selection-lp`, formalised sorry-free in
`QOU.ParticleInteractions.operator_selection_lp`. This probe measures whether
complementary slackness on it produces the gate, by solving the LP on the SAME
ten Wedderburn blocks the gate runs over and comparing its active set
`{l : y_l* > 0}` with the gate's kept set.

## What is measured

* **The gate**, from the producer itself (read-only; this probe does not modify
  `hecke_core_legacy.py`): how many of the ten blocks it keeps at (Z,N)=(1,1)
  and (2,2), the ungated and gated totals, and — by matching subset sums against
  the per-step per-block deltas — which blocks carry a non-zero kept
  contribution.
* **The LP**, through the canonical entry point `lp_dual_solver.
  solve_operator_selection_lp`, so the witness carries `y0_star`, `y_star`,
  `active_set`, `primal_obj`, `dual_obj` and `duality_gap` as AGENTS.md
  "LP / SDP duals - first-class infra" requires.

## Precision

`mp.dps = 70`, proton pin via `q_at()`, convention D `z = q^3/(q^2+1)`. Every
quantity this probe computes is carried as `mpf`; `float()` appears only inside
display f-strings and at the boundary of `solve_operator_selection_lp`, which
takes numpy arrays by signature and is the corpus's mandated canonical solver
(its clarabel backend re-solves at `prec_bits=167`; the backend actually used is
recorded in the payload). That boundary is the solver's, not this probe's.

## Result

The two sets do not coincide, and not marginally: the LP's active set is
essentially every block at every reachable target, while the gate keeps 4 of 10
at A=2 and 2 of 10 at A=4. The reason is structural rather than instance-
specific and is proved in
`QOU.MassTheory.UICGateNotFromComplementarySlackness`: Wedderburn block
projectors are orthogonal idempotents, so the Frobenius Gram
`G_lm = tr_M(P_l P_m) = delta_lm tr_M(P_l)` is diagonal, complementary slackness
decouples to `s_l * G_ll * x_l = 0`, and the atom's traces — the gate's quantity
— do not occur in it at all. Independently reached by
`computations/probes/h6_block_selection_lp_probe.py` on the H_6 blocks.

NO ASSERTION HERE IS A FIT: every number is measured or solved.

Bean qou-8urh; appends to qou-t6be, qou-zlra, qou-brng.
"""
from __future__ import annotations

import itertools
import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _bridge

from mpmath import mp  # noqa: E402

mp.dps = 70

from q_parameter import q_at  # noqa: E402

_Q = q_at(mp.dps)
_Z_D = _Q ** 3 / (_Q ** 2 + 1)          # convention D Markov parameter

_ZERO = mp.mpf(10) ** (-40)


def _as_mpf(v):
    """Coerce a producer value to `mpf` without a float64 round-trip.

    The producer hands back `mpf` for some fields and `float` for others, so
    `repr()` alone is wrong on both counts: it yields `mpf('...')` for the
    first (unparseable) and would be fine but lossy-by-origin for the second.
    Take the `mpf` verbatim where it exists; go through `repr` only for a
    genuine Python float, which has no more precision to lose.
    """
    if isinstance(v, mp.mpf):
        return v
    if isinstance(v, str):
        return mp.mpf(v)
    return mp.mpf(repr(v))


_LP_DUAL_FIELDS = ("x_star", "y0_star", "y_star",
                   "primal_obj", "dual_obj", "duality_gap")


def _prefer_str_fields(d):
    """Carry the solver's full-precision decimals under the mandated key names.

    `solve_operator_selection_lp` returns each LP-dual field twice: once as an
    f64 (for consumers that do arithmetic on it) and once as a `<field>_str`
    decimal, when the clarabel-MPFR backend supplied one. Writing the f64 copy
    into a witness is exactly the raw-float64 defect the precision ratchet
    exists to catch, and stringifying it would be worse — it would dress 53
    bits up as 50 digits.

    So where a `_str` companion exists, it BECOMES the value of the mandated
    key (`y0_star`, `y_star`, `primal_obj`, `dual_obj`, `duality_gap`,
    `x_star`), which is what `lp_dual_witness_validator.py` looks for. The f64
    duplicate is dropped. `active_set` is a list of indices and stays as-is.

    If a `_str` companion is missing the field is dropped rather than
    down-converted, and `lp_dual_fields_downgraded` records that — a witness
    should not silently carry a less precise number under a key a reader will
    assume is canonical.
    """
    out = dict(d)
    missing = []
    for f in _LP_DUAL_FIELDS:
        key = f + "_str"
        if key in out and out[key] is not None:
            out[f] = out[key]
        elif f in out:
            missing.append(f)
            out.pop(f)
    if missing:
        out["lp_dual_fields_downgraded"] = missing
    return out


def _gate_measurement(Z, N, k_exact=4):
    """Run the producer read-only and recover its gate's behaviour."""
    import hecke_core_legacy as HC

    returned, per_step = HC.unified_iterative_correction(
        Z, N, return_per_step=True, k_exact=k_exact)
    last = per_step[-1]

    # Per-block cumulative contribution = sum of that block's per-step deltas.
    cumul = {}
    for row in per_step:
        for lam, rec in row.get("partitions", {}).items():
            cumul[lam] = cumul.get(lam, mp.mpf(0)) + _as_mpf(rec["delta_MeV"])

    gated = _as_mpf(last["gated_total_DISPROVED_SELECTION_MeV"])
    raw = _as_mpf(last["raw_total_MeV"])
    n_keep = int(last["n_tight_final"])
    n_blocks = int(last["n_active_exact"])

    # Which blocks are kept? The gate's per-block sign is internal, but the kept
    # set is the size-`n_keep` subset whose contributions sum to `gated`. Blocks
    # contributing ~0 are indistinguishable by this test, so report the
    # NON-ZERO members, which is what the comparison turns on.
    keys = sorted(cumul)
    matches = [c for c in itertools.combinations(keys, n_keep)
               if abs(sum((cumul[k] for k in c), mp.mpf(0)) - gated) < _ZERO]
    nonzero_kept = None
    if matches:
        # Intersect over all matching subsets, keeping only non-zero blocks:
        # those are pinned regardless of which zero-blocks fill the rest.
        common = set(matches[0])
        for m in matches[1:]:
            common &= set(m)
        nonzero_kept = sorted(k for k in common if abs(cumul[k]) > _ZERO)

    return {
        "Z": Z, "N": N, "k_exact": k_exact,
        "returned_MeV": mp.nstr(_as_mpf(returned), 17),
        "n_blocks": n_blocks,
        "n_kept_by_gate": n_keep,
        "ungated_total_MeV": mp.nstr(raw, 17),
        "gated_total_MeV": mp.nstr(gated, 17),
        "gated_over_ungated": mp.nstr(gated / raw, 12) if raw != 0 else None,
        "per_block_cumul_MeV": {k: mp.nstr(v, 17) for k, v in sorted(cumul.items())},
        "n_subset_matches": len(matches),
        "nonzero_kept_blocks": nonzero_kept,
    }


def _lp_on_the_same_blocks(Z, N, k_exact=4):
    """Solve prop:operator-selection-lp on the ten Wedderburn blocks the gate runs over.

    Construction follows `h6_block_selection_lp_probe.py`: per-block contribution
    `t_l = |y_l * chi_l(W_atom)|`, Gram `G = diag(t)` — diagonal because
    Wedderburn block projectors are orthogonal idempotents.
    """
    import numpy as np
    import hecke_core_legacy as HC
    from pyhecke.trace import atom_character_raw
    from lp_dual_solver import solve_operator_selection_lp

    entries = sorted(
        [e for e in HC._PARTITION_TABLE
         if 2 <= e.get("k", 0) <= k_exact and e.get("has_ysn")],
        key=lambda x: (x["k"], tuple(x["partition"])))

    lams, tvals = [], []
    for e in entries:
        ca, na, _ = atom_character_raw(Z, N, e, include_inter=True)
        ca = _as_mpf(ca)
        if ca == 0:
            continue
        w = _as_mpf(e["wedderburn_weight"])
        lams.append(tuple(e["partition"]))
        # |y_l * chi_l| with the log-scale carried in mpf throughout
        tvals.append(abs(w) * mp.e ** (mp.log(abs(ca)) + _as_mpf(na)))

    if not tvals:
        return None
    mx = max(tvals)
    tvals = [v / mx for v in tvals]                 # scale-free; the LP is homogeneous
    total = sum(tvals, mp.mpf(0))

    # float64 ONLY at the canonical solver's own signature boundary.
    t_np = np.array([float(v) for v in tvals], dtype=float)
    G_np = np.diag(t_np)

    solves = []
    for frac in (mp.mpf("0.05"), mp.mpf("0.25"), mp.mpf("0.50"),
                 mp.mpf("0.75"), mp.mpf("0.95")):
        n_target = float(frac * total)
        r = solve_operator_selection_lp(t_np, G_np, n_target)
        d = _prefer_str_fields(r.to_dict())
        d["n_target_fraction_of_sum_t"] = mp.nstr(frac, 4)
        d["n_active"] = len(d["active_set"])
        d["active_partitions"] = [list(lams[i]) for i in d["active_set"]
                                  if i < len(lams)]
        solves.append(d)

    return {
        "blocks": [list(l) for l in lams],
        "n_blocks": len(lams),
        "gram_is_diagonal": True,
        "cost_is_not_a_gram_row": all(
            any(i != j and tvals[j] != 0 for j in range(len(tvals)))
            for i in range(len(tvals))) and len(tvals) > 1,
        "cost_is_not_a_gram_row_note":
            "A diagonal Gram has row lambda = (0,...,t_lambda,...,0), which is "
            "not the cost vector t unless d = 1. So the NF-basis degeneracy "
            "(t = G row 0, forcing optimal value 0 and y0* = 0) does NOT carry "
            "over to the Wedderburn-block instance -- measured y0* != 0 here.",
        "gram_diagonal_reason":
            "Wedderburn block projectors are orthogonal idempotents: "
            "G_lm = tr_M(P_l P_m) = delta_lm tr_M(P_l).",
        "t_normalised": [mp.nstr(v, 17) for v in tvals],
        "solves": solves,
    }


def main() -> int:
    from witness_base import WitnessBuilder

    print(f"q0 (proton pin, {mp.dps} dps) = {mp.nstr(_Q, 25)}", flush=True)
    print(f"z_D = q^3/(q^2+1)            = {mp.nstr(_Z_D, 25)}", flush=True)

    gate = {}
    for (Z, N), label in (((1, 1), "2H"), ((2, 2), "4He")):
        print(f"[gate] running producer for {label} ...", flush=True)
        gate[label] = _gate_measurement(Z, N)
        g = gate[label]
        print(f"[gate] {label}: keeps {g['n_kept_by_gate']} of {g['n_blocks']}; "
              f"ungated {g['ungated_total_MeV']} -> gated {g['gated_total_MeV']}; "
              f"non-zero kept blocks {g['nonzero_kept_blocks']}", flush=True)

    lp = {}
    for (Z, N), label in (((1, 1), "2H"), ((2, 2), "4He")):
        print(f"[lp] solving operator-selection LP on the same blocks for {label} ...",
              flush=True)
        lp[label] = _lp_on_the_same_blocks(Z, N)
        if lp[label]:
            for s in lp[label]["solves"]:
                print(f"[lp] {label}: target {s['n_target_fraction_of_sum_t']}*S -> "
                      f"active {s['n_active']} of {lp[label]['n_blocks']}, "
                      f"y0*={mp.nstr(mp.mpf(s['y0_star']), 6)}, "
                      f"gap={mp.nstr(mp.mpf(s['duality_gap']), 6)}", flush=True)

    w = WitnessBuilder("uic-gate-vs-lp-complementary-slackness", engine="mpmath")
    w.set_description(
        "The UIC Pass-2 sign gate is not the operator-selection LP's active set. "
        "The gate's comment derives it from complementary slackness on "
        "prop:operator-selection-lp; solved on the same ten Wedderburn blocks, "
        "the LP's active set is essentially every block at every reachable "
        "target while the gate keeps 4 of 10 (A=2) and 2 of 10 (A=4). "
        "Structural reason: orthogonal Wedderburn projectors make the Frobenius "
        "Gram diagonal, so complementary slackness decouples to s_l*G_ll*x_l=0 "
        "and never mentions the atom traces the gate reads. Proved sorry-free in "
        "QOU.MassTheory.UICGateNotFromComplementarySlackness."
    )

    ok = True

    # 1. The gate is a strict, non-trivial restriction: it drops blocks.
    for label in ("2H", "4He"):
        g = gate[label]
        strict = 1 if 0 < g["n_kept_by_gate"] < g["n_blocks"] else 0
        w.add_assertion(f"gate keeps a proper non-empty subset [{label}]",
                        str(strict), "1")
        ok &= bool(strict)

    # 2. The LP's active set is strictly larger than the gate's kept set at
    #    every solved target — so the two cannot be the same selection.
    for label in ("2H", "4He"):
        if not lp[label]:
            continue
        g = gate[label]
        bigger = 1 if all(s["n_active"] > g["n_kept_by_gate"]
                          for s in lp[label]["solves"]) else 0
        w.add_assertion(
            f"LP active set exceeds the gate's kept set at every target [{label}]",
            str(bigger), "1")
        ok &= bool(bigger)

    # 3. The block instance's net-constraint shadow price is NOT zero -- and
    #    that is correct, not a defect. `y_0_eq_zero_of_radical` and the
    #    block's own degeneracy argument both need the cost vector to BE a row
    #    of the Gram (the NF basis contains the identity, so row 0 is `t`).
    #    A diagonal Wedderburn Gram has row `lambda` equal to
    #    `(0,...,t_lambda,...,0)`, so that hypothesis fails and y0* is free.
    #    Asserting it here was MY error; the measurement corrected it.
    for label in ("2H", "4He"):
        if not lp[label]:
            continue
        nz = 1 if all(mp.mpf(s["y0_star"]) != 0 for s in lp[label]["solves"]) else 0
        w.add_assertion(
            f"block-instance y0* is NON-zero (cost is not a Gram row) [{label}]",
            str(nz), "1")
        ok &= bool(nz)
        notrow = 1 if lp[label]["cost_is_not_a_gram_row"] else 0
        w.add_assertion(
            f"diagonal Gram: no row equals the cost vector [{label}]",
            str(notrow), "1")
        ok &= bool(notrow)

    # 4. Strong duality actually held on the solves we are reading.
    for label in ("2H", "4He"):
        if not lp[label]:
            continue
        # `duality_gap` is a 50-dps decimal STRING (see `_prefer_str_fields`),
        # so compare as mpf against an mpf bound -- not `abs()` on the str, and
        # not `float()` on it either.
        tight = 1 if all(abs(mp.mpf(s["duality_gap"])) < mp.mpf("1e-30")
                         for s in lp[label]["solves"]) else 0
        w.add_assertion(f"LP duality gap vanishes on every solve [{label}]",
                        str(tight), "1")
        ok &= bool(tight)

    # 5. The gate changes the answer materially, so it is load-bearing.
    for label in ("2H", "4He"):
        g = gate[label]
        moved = 1 if abs(mp.mpf(g["gated_total_MeV"])
                         - mp.mpf(g["ungated_total_MeV"])) > mp.mpf("1e-6") else 0
        w.add_assertion(f"gate materially changes the returned value [{label}]",
                        str(moved), "1")
        ok &= bool(moved)

    w.save(extra={
        "q0Anchor": "proton",
        "q0Value": mp.nstr(_Q, 50),
        "q0AnchorReason": "q = q_parameter.q_at(), the proton pin, used for every evaluation here",
        "q0_proton_pin": mp.nstr(_Q, 50),
        "z_D_convention_D": mp.nstr(_Z_D, 50),
        "compute_dps": mp.dps,
        "gate_measurement": gate,
        "operator_selection_lp": lp,
        "verdict": "case (b): the LP exists; complementary slackness on it does "
                   "not yield the sign gate",
        "lean": "QOU.MassTheory.UICGateNotFromComplementarySlackness "
                "(8 declarations, lean-direct exit 0, sorry-free)",
        "producer_untouched": "hecke_core_legacy.py is read only by this probe",
    })
    print("PASS" if ok else "FAIL", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
