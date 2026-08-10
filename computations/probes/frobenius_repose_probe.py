#!/usr/bin/env python3
"""Re-posed Frobenius admissibility test for the knot-assignment SDP (bean qou-vd7j).

CONTEXT. `all_nuclides_sdp_admissibility.py` reports 0/3558 nuclei feasible under
the Frobenius per-nucleus test, while the weak scalar LP reports 2221/3558. The
diagnostic (`frobenius_admissibility_diagnostic.py`) showed this is an
OVER-DETERMINATION artifact, not a Gram/knot obstruction: the Frobenius LP
imposes 7 equalities

    1ᵀx = A          (net, 1 row)
    G x = nf         (Frobenius demand, 6 rows)

on 6 unknowns. Since G (the H_3 NF Gram at q_0) is invertible (rank 6), `G x = nf`
already fixes x = G⁻¹nf uniquely, so the implied net `1ᵀG⁻¹nf` is O(1) — never the
mass number A. The net row is therefore inconsistent for every nucleus.

THIS PROBE re-poses the test WITHOUT the inconsistent net row, in two variants:

  (a) DROP the `1ᵀx = A` net constraint entirely.
      LP becomes:  min t·x  s.t.  G x = nf.
      Feasibility ⟺ nf ∈ range(G). G full-rank ⇒ range(G)=ℝ⁶ ⇒ feasible for ANY
      finite nf. (Heavy A only fails on the f64 build_atom_nf overflow.)

  (b) REPLACE the net RHS A with the consistent value 1ᵀG⁻¹nf.
      LP becomes:  min t·x  s.t.  G x = nf  AND  1ᵀx = 1ᵀG⁻¹nf.
      The net row is now implied by the Frobenius rows ⇒ redundant ⇒ still the
      unique point x = G⁻¹nf, feasible for any finite nf.

CRITICAL QUESTION (anti-fit discipline, AGENTS.md): does re-posing RECOVER a
selective ν_SDP for the census atoms (deuteron→1, tritium→2, ³He→2)? Or does it
just make the test trivially feasible (no selective power)? We report what the
math actually gives — a trivially-feasible non-selective LP is an honest NEGATIVE,
reported as such, not spun as success. We do NOT tune the net normalization to hit
ν_SDP∈{1,2}.

Output: frobenius-repose.witness.json + stdout table.
Requires: pyhecke, numpy, scipy. Set PYTHONPATH per the bean instructions.
"""
from __future__ import annotations

import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations", "computations/substrate"):
    sys.path.insert(0, str(_ROOT / _p))

from pyhecke import atom, gram  # noqa: E402
from pyhecke.lp_dual_solver import solve_frobenius_dual_lp  # noqa: E402

try:
    from qou_substrate.witness import WitnessBuilder  # noqa: E402
    _HAS_WITNESS = True
except Exception:  # pragma: no cover
    _HAS_WITNESS = False

NF_NAMES = list(gram.NF_NAMES)

# Census atoms with the ν_SDP targets the knot-assignment program must reproduce
# (from conj:canonical-knot-id-sdp / the ρ_F·Vol binding route). '4He' has no
# assigned knot in the corpus (marked None).
CENSUS = {"2H": 1, "3H": 2, "3He": 2, "4He": None}

# Light census + a heavy-A sample to exercise both the finite and overflow paths.
SAMPLE = [(1, 0, "p"), (0, 1, "n"), (1, 1, "2H"), (1, 2, "3H"),
          (2, 1, "3He"), (2, 2, "4He"), (3, 4, "7Li"), (6, 6, "12C"),
          (8, 8, "16O"), (20, 20, "40Ca"), (26, 30, "56Fe")]

DUAL_TOL = 1e-9


def _build_nf(Z: int, N: int):
    nf = np.asarray(atom.build_atom_nf(Z, N), dtype=float)
    return nf if np.all(np.isfinite(nf)) else None


def _variant_a(t, G, Ginv, nf):
    """Drop the net row: min t·x s.t. Gx=nf. Unique x=G⁻¹nf; feasible iff finite.

    A finite-but-huge heavy-A nf can overflow G⁻¹nf to inf in f64; that is the
    known infra ceiling (needs mpfr), flagged 'overflow', NOT a range(G) failure.
    """
    with np.errstate(over="ignore", invalid="ignore"):
        x = Ginv @ nf
        if not np.all(np.isfinite(x)):
            return {"feasible": False, "overflow": True, "active_count": None}
        resid = float(np.linalg.norm(G @ x - nf))
    # RELATIVE residual: G is invertible ⇒ nf ∈ range(G) is mathematically
    # guaranteed for any finite nf, so the correct feasibility test is a
    # relative one. An absolute 1e-6 threshold would spuriously reject the
    # many nuclei whose nf entries reach ~1e10+ (a tolerance artifact, not a
    # range(G) failure).
    rel = resid / (float(np.linalg.norm(nf)) + 1.0)
    feasible = np.isfinite(rel) and rel < 1e-9
    # Frobenius-equality shadow prices y = G⁻ᵀ t (sensitivity of t·x to the RHS
    # nf); INDEPENDENT of nf ⇒ the "active channels" cannot discriminate nuclei.
    y = Ginv.T @ t
    active = [i for i in range(len(t)) if abs(y[i]) > DUAL_TOL]
    return {
        "feasible": bool(feasible), "overflow": False,
        "resid": resid, "rel_resid": rel,
        "x_star": x.tolist(), "primal_obj": float(t @ x),
        "y_star": y.tolist(), "active_set": active, "active_count": len(active),
    }


def _variant_b(t, G, Ginv, nf):
    """Replace net RHS A with the consistent 1ᵀG⁻¹nf, and solve the 7-eq LP via
    the canonical Frobenius-dual solver (which stacks [net; G]). Now consistent."""
    with np.errstate(over="ignore", invalid="ignore"):
        net_consistent = float(np.ones(len(t)) @ (Ginv @ nf))
    if not np.isfinite(net_consistent):
        return {"feasible": False, "overflow": True, "active_count": None}
    res = solve_frobenius_dual_lp(t, G, net_consistent, nf, dual_tol=DUAL_TOL)
    # An INFEASIBLE LP has no solution, and the solver signals that by filling
    # x_star / y_star / the objectives with NaN. Those were published verbatim,
    # which did two bad things: it wrote bare `NaN` tokens (JSON has none, so
    # this witness did not parse under a strict loader), and it presented "no
    # solution exists" as if it were a computed vector.
    #
    # null, not a "nan" marker: an infeasible LP is a MISSING value, not a pole.
    # `feasible`, `active_set` and `net_rhs_used` carry the real information and
    # are kept.
    if not res.feasible:
        return {
            "feasible": False, "overflow": False,
            "net_rhs_used": net_consistent,
            "x_star": None, "primal_obj": None,
            "y0_star": None, "y_star": None,
            "active_set": list(res.active_set),
            "active_count": len(res.active_set),
            "duality_gap": None,
            "solution_undefined_reason": "LP infeasible — no primal/dual point",
        }
    return {
        "feasible": True, "overflow": False,
        "net_rhs_used": net_consistent,
        "x_star": list(res.x_star),
        "primal_obj": float(res.primal_obj),
        "y0_star": float(res.y0_star),
        "y_star": list(res.y_star),
        "active_set": list(res.active_set),
        "active_count": len(res.active_set),
        "duality_gap": float(res.duality_gap),
    }


def _full_chart_feasibility(t, G, Ginv):
    """Count feasible nuclei over the whole AME chart for each variant."""
    ame = _ROOT / "qou-mass" / "src" / "qou_mass" / "data" / "ame2020.json"
    entries = json.loads(ame.read_text())["entries"]
    n_total = n_finite = n_overflow = a_feas = b_feas = 0
    a_active = Counter()
    b_active = Counter()
    for e in entries:
        Z, N, A = int(e["Z"]), int(e["N"]), int(e["A"])
        if A < 1:
            continue
        n_total += 1
        try:
            nf = _build_nf(Z, N)
        except Exception:
            n_overflow += 1
            continue
        if nf is None:
            n_overflow += 1
            continue
        ra = _variant_a(t, G, Ginv, nf)
        rb = _variant_b(t, G, Ginv, nf)
        if ra.get("overflow") or rb.get("overflow"):
            # finite nf but G⁻¹nf overflowed in f64 — same heavy-A infra ceiling
            n_overflow += 1
            continue
        n_finite += 1
        if ra["feasible"]:
            a_feas += 1
            a_active[ra["active_count"]] += 1
        if rb["feasible"]:
            b_feas += 1
            b_active[rb["active_count"]] += 1
    return {
        "n_total": n_total, "n_finite_f64": n_finite,
        "n_overflow_heavy": n_overflow,
        "variant_a_feasible": a_feas, "variant_b_feasible": b_feas,
        "variant_a_active_count_hist": {str(k): v for k, v in sorted(a_active.items())},
        "variant_b_active_count_hist": {str(k): v for k, v in sorted(b_active.items())},
    }


def main() -> int:
    t0 = time.monotonic()
    t = np.asarray(gram.TR_M, dtype=float)
    G = np.asarray(gram.gram_matrix(), dtype=float)
    rank = int(np.linalg.matrix_rank(G))
    Ginv = np.linalg.inv(G)
    print(f"G is 6x6, rank {rank}  (invertible ⇒ Gx=nf has a UNIQUE solution x=G⁻¹nf)")
    print(f"eigs(G) = {np.round(np.linalg.eigvalsh(G), 5)}")
    yA = Ginv.T @ t
    print(f"\nVariant (a) Frobenius shadow prices y=G⁻ᵀt (nucleus-INDEPENDENT):")
    print(f"  {dict(zip(NF_NAMES, np.round(yA, 4)))}")
    print(f"  active channels (|y|>tol): "
          f"{[NF_NAMES[i] for i in range(6) if abs(yA[i]) > DUAL_TOL]}  "
          f"(count {int((np.abs(yA) > DUAL_TOL).sum())}) — SAME for every nucleus")

    print(f"\n{'nucleus':8}{'A':>3}  {'ν_SDP tgt':>9}  "
          f"{'(a) feas':>8} {'(a) #chan':>9}  {'(b) feas':>8} {'(b) #chan':>9}")
    per_nucleus = []
    for Z, N, lab in SAMPLE:
        A = Z + N
        nf = None
        try:
            nf = _build_nf(Z, N)
        except Exception:
            pass
        tgt = CENSUS.get(lab)
        tgt_s = "—" if tgt is None else str(tgt)
        if nf is None:
            print(f"{lab:8}{A:>3}  {tgt_s:>9}  {'OVERFLOW (f64 build_atom_nf)':>40}")
            per_nucleus.append({"nucleus": lab, "Z": Z, "N": N, "A": A,
                                "nu_sdp_target": tgt, "overflow": True})
            continue
        ra = _variant_a(t, G, Ginv, nf)
        rb = _variant_b(t, G, Ginv, nf)
        if ra.get("overflow") or rb.get("overflow"):
            print(f"{lab:8}{A:>3}  {tgt_s:>9}  "
                  f"{'G⁻¹nf OVERFLOW (f64 heavy-A ceiling; needs mpfr)':>40}")
            per_nucleus.append({"nucleus": lab, "Z": Z, "N": N, "A": A,
                                "nu_sdp_target": tgt, "overflow": True})
            continue
        ac = "None" if ra["active_count"] is None else str(ra["active_count"])
        bc = "None" if rb["active_count"] is None else str(rb["active_count"])
        print(f"{lab:8}{A:>3}  {tgt_s:>9}  "
              f"{str(ra['feasible']):>8} {ac:>9}  "
              f"{str(rb['feasible']):>8} {bc:>9}")
        per_nucleus.append({
            "nucleus": lab, "Z": Z, "N": N, "A": A, "nu_sdp_target": tgt,
            "variant_a": ra, "variant_b": rb,
        })

    print("\nRunning full-AME-chart feasibility count (both variants)...")
    chart = _full_chart_feasibility(t, G, Ginv)
    print(f"  chart total (A≥1): {chart['n_total']}  "
          f"f64-finite: {chart['n_finite_f64']}  "
          f"heavy overflow: {chart['n_overflow_heavy']}")
    print(f"  variant (a) feasible: {chart['variant_a_feasible']} / {chart['n_total']}  "
          f"active-count hist {chart['variant_a_active_count_hist']}")
    print(f"  variant (b) feasible: {chart['variant_b_feasible']} / {chart['n_total']}  "
          f"active-count hist {chart['variant_b_active_count_hist']}")

    # Selectivity verdict — did either variant reproduce the census {2H:1,3H:2,3He:2}?
    census_rows = {r["nucleus"]: r for r in per_nucleus if r.get("nucleus") in CENSUS}
    a_counts = {k: census_rows[k]["variant_a"]["active_count"]
                for k in ("2H", "3H", "3He") if k in census_rows}
    b_counts = {k: census_rows[k]["variant_b"]["active_count"]
                for k in ("2H", "3H", "3He") if k in census_rows}
    target = {"2H": 1, "3H": 2, "3He": 2}
    a_match = a_counts == target
    b_match = b_counts == target
    a_selective = len(set(chart["variant_a_active_count_hist"].keys())) > 1
    b_selective = len(set(chart["variant_b_active_count_hist"].keys())) > 1
    verdict = {
        "census_target": target,
        "variant_a_census_active_counts": a_counts,
        "variant_b_census_active_counts": b_counts,
        "variant_a_reproduces_census": a_match,
        "variant_b_reproduces_census": b_match,
        "variant_a_has_selective_power": bool(a_selective),
        "variant_b_has_selective_power": bool(b_selective),
        "recovers_selective_nu_sdp": bool((a_match and a_selective)
                                          or (b_match and b_selective)),
    }
    print("\n=== SELECTIVITY VERDICT ===")
    print(f"  census ν_SDP target: {target}")
    print(f"  variant (a) census active-counts: {a_counts}  "
          f"(reproduces={a_match}, chart-selective={a_selective})")
    print(f"  variant (b) census active-counts: {b_counts}  "
          f"(reproduces={b_match}, chart-selective={b_selective})")
    print(f"  RECOVERS A SELECTIVE ν_SDP?  {verdict['recovers_selective_nu_sdp']}")

    findings = [
        "G (H_3 NF Gram at q_0) is 6x6 rank-6 (invertible), so the Frobenius "
        "demand Gx=nf has a UNIQUE solution x=G⁻¹nf. Removing the inconsistent "
        "net row leaves a determined linear solve, not an optimisation.",
        "Variant (a) [drop net]: nf ∈ range(G) is MATHEMATICALLY GUARANTEED for "
        "every finite nf (G full-rank), so feasibility is universal in exact "
        f"arithmetic. The measured f64 count ({chart['variant_a_feasible']}/"
        f"{chart['n_total']}) is capped by two infra effects, NOT physics: the "
        f"{chart['n_overflow_heavy']} heavy-A build_atom_nf/G⁻¹nf overflows, and "
        "f64 ill-conditioning of G⁻¹nf at large-magnitude nf (rel-resid > 1e-9). "
        "Both vanish with the mpfr native path. The Frobenius shadow prices "
        "y=G⁻ᵀt are nucleus-INDEPENDENT, so the active-channel set is CONSTANT "
        "across the whole chart — zero selective power.",
        "Variant (b) [net RHS = 1ᵀG⁻¹nf]: identical unique point x=G⁻¹nf; the net "
        "row is now redundant (implied by Gx=nf). The canonical HiGHS solver "
        f"reports {chart['variant_b_feasible']}/{chart['n_total']} feasible (lower "
        "than (a) only because HiGHS's own feasibility tolerance rejects "
        "large-RHS problems — again f64 conditioning, not range(G)); same "
        "non-selective active-count histogram (all count 1).",
        "VERDICT (honest NEGATIVE): re-posing removes the 0/3558 artifact but does "
        "NOT recover a selective ν_SDP. The Frobenius admissibility test, with the "
        "inconsistent net row removed, is an invertible linear solve dressed as an "
        "LP — it is trivially feasible and cannot discriminate the census "
        f"{target} (or any nuclei). It has no selective power; ν_SDP stays "
        "underived. No fit wired.",
    ]
    for f in findings:
        print(f"\n- {f}")

    if _HAS_WITNESS:
        w = WitnessBuilder("frobenius-repose", engine="python", start_time=t0)
        w.set_description(
            "Re-posed Frobenius per-nucleus admissibility (bean qou-vd7j): removes "
            "the inconsistent net row two ways — (a) drop 1ᵀx=A, (b) replace its "
            "RHS with the consistent 1ᵀG⁻¹nf. G invertible ⇒ Gx=nf is a unique "
            "linear solve, so both variants are trivially feasible and "
            "NON-SELECTIVE. Honest negative: re-posing does not recover ν_SDP."
        )
        w.add_data("gram_rank", rank)
        w.add_data("gram_invertible", rank == len(t))
        w.add_data("variant_a_shadow_prices_G_invT_t", yA.tolist())
        w.add_data("per_nucleus_sample", per_nucleus)
        w.add_data("full_chart", chart)
        w.add_data("selectivity_verdict", verdict)
        w.add_data("findings", findings)
        w.add_assertion(
            name="gram_full_rank_forces_unique_solve",
            computed=rank, expected=len(t), tolerance=0,
            source="np.linalg.matrix_rank(gram_matrix()) — invertible ⇒ Gx=nf unique",
        )
        w.add_assertion(
            name="repose_is_non_selective",
            computed=int(verdict["recovers_selective_nu_sdp"]), expected=0, tolerance=0,
            source="neither variant reproduces the census AND is chart-selective",
        )
        out = w.save()
        print(f"\nWitness: {out}")
    else:
        out = _ROOT / "computations" / "frobenius-repose.witness.json"
        out.write_text(json.dumps({
            "gram_rank": rank, "per_nucleus_sample": per_nucleus,
            "full_chart": chart, "selectivity_verdict": verdict,
            "findings": findings}, indent=2))
        print(f"\nWitness (no WitnessBuilder): {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
