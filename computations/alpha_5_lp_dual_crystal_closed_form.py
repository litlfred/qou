#!/usr/bin/env python3
"""alpha_5_lp_dual_crystal: the LP is an argmin, and its duals are ill-conditioned.

Bean `qou/pin3` step 1 — "confirm the LP is degenerate at these strata
(multiple optimal duals)". It is **not** degenerate. The dual is unique
and available in closed form. The observed regeneration diff has a
different cause, identified below.

Reads the committed witness only. Pure stdlib (`json`), so it runs
without numpy/scipy/pyhecke.

## The LP

`alpha_5_lp_dual_crystal.py` calls `solve_operator_selection_lp(t, G,
n_target)` with **`G = diag(|weight_lambda|)`** (its line 203) and
`n_target = sum |weight_lambda| > 0`. That solver (lp_dual_solver.py
line 358 — not `solve_frobenius_dual_lp`, which is the equality
variant) solves

    min t.x   s.t.  1.x = n_target,  Gx >= 0,  x >= -M

With `G` diagonal and positive, `Gx >= 0` is just `x >= 0`, so the
program is "put all the mass on the cheapest channel":

    x*   = n_target * e_argmin(t)
    y0*  = min_j t_j                        (unique)
    s*_j = (t_j - min_j t_j) / |w_j|        (unique)
    obj  = n_target * min_j t_j

Every one of those is verified against every stratum of the committed
witness below. There is no vertex to choose: the dual optimum is a
point, not a face, so "the solver landed on a different vertex" cannot
be what happened.

## What did happen

`s*_j` divides by `|w_j|`, and in the `ht6` strata `min |w_j|` is
~2e-06 to ~8e-06. So an error `eps` in `y0*` lands in `s*` multiplied
by `1/|w_j|` ~ 1e+05. The three entries `pin3` reports as changed are
exactly the **argmin** channels — the ones whose true `s*` is 0 — and
they correspond to

    3He ht6  y_star.2  0.0 -> 0.020749613956537   => eps = 7.2e-08
    T   ht6  y_star.2  0.0 -> 0.000764070473307   => eps = 3.7e-09
    D   ht6  y_star.0  0.0 -> 0.000097401828163   => eps = 8.2e-10

i.e. `y0*` differing from `min_j t_j` by 1e-09..1e-07 absolute, which
against `t ~ 27` is a relative 1e-09 or less. That is solver
tolerance, and `pin3` records that the two runs used different solver
stacks (scipy HiGHS f64 vs the freshly built clarabel MPFR). The
remaining ~21 entries at 1e-13..1e-17 are the same effect on channels
with larger `|w|`.

So the witness is not carrying a substantive dual change. It is
carrying a quantity with a condition number of ~1e+05 with respect to
a solver-tolerance-level input, in a field consumers read as a shadow
price.

## What that implies for pin3's next steps

Its step 1 is answered: not degenerate. Its step 2 ("do y_star
consumers depend on the specific vertex") is the wrong question — the
vertex is unique. The real question is whether any consumer reads
`y_star` in the `ht6` strata at all, since those coordinates cannot be
pinned to better than ~1e-02 by any solver at f64 and are a division
by a ~1e-06 weight either way. Publishing the residual `t_j - y0*`
alongside would make the conditioning visible instead of hiding it in
a quotient.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WITNESS = HERE / "alpha" / "alpha-5-lp-dual-crystal.witness.json"

#: Relative agreement demanded of the closed form. The witness is f64
#: output of an LP solver; anything tighter would test the solver's
#: tolerance rather than the closed form.
REL_TOL = 1e-6


def close(u, v, tol=REL_TOL):
    return all(abs(a - b) <= tol * max(1.0, abs(b)) for a, b in zip(u, v))


def main() -> int:
    d = json.loads(WITNESS.read_text(encoding="utf-8"))
    rows, ok_all = [], True

    print("closed form:  x* = n_target*e_argmin(t),  y0* = min t,  "
          "s_j = (t_j - min t)/|w_j|\n")
    for sname, s in d["data"]["at_q0_per_stratum"].items():
        for a in (s.get("per_atom") or []):
            t = a["t_cost"]
            w = [abs(x) for x in a["weights"]]
            nt = a["n_target"]
            lp = a["lp"]
            am = min(range(len(t)), key=lambda i: t[i])
            mn = t[am]

            pred_x = [nt if i == am else 0.0 for i in range(len(t))]
            pred_s = [(t[i] - mn) / w[i] for i in range(len(t))]

            chk = {
                "y0_is_min_t": abs(lp["y0_star"] - mn) <= 1e-9 * max(1.0, abs(mn)),
                "x_star_is_all_on_argmin": close(lp["x_star"], pred_x),
                "y_star_is_scaled_residual": close(lp["y_star"], pred_s),
                "obj_is_n_target_times_min_t":
                    abs(lp["primal_obj"] - nt * mn) <= REL_TOL * abs(nt * mn),
            }
            ok = all(chk.values())
            ok_all &= ok

            # Two smallest costs: a near-tie would be the only way a small
            # q0 move could change the argmin. Report the margin.
            srt = sorted(t)
            margin = (srt[1] - srt[0]) / abs(srt[0]) if len(srt) > 1 else None
            amp = 1.0 / min(w)

            print(f"  {'ok  ' if ok else 'FAIL'}  {sname:8s} {a['atom']:4s}  "
                  f"{len(t)} channels")
            for k, vok in chk.items():
                print(f"          {'ok' if vok else 'FAIL'}  {k}")
            print(f"          argmin margin (t_(2)-t_(1))/t_(1) = "
                  f"{'n/a' if margin is None else format(margin, '.3e')}"
                  f"   -> no near-tie, so the argmin cannot flip on an "
                  f"11.5 ppb q0 move" if margin is None or margin > 1e-3 else "")
            print(f"          dual amplification 1/min|w| = {amp:.3e}")
            rows.append({"stratum": sname, "atom": a["atom"],
                         "checks": chk, "argmin_margin": margin,
                         "dual_amplification": amp})

    # The three entries pin3 reports, converted back to an error in y0*.
    reported = [
        ("3He", "ht6", 2, 0.020749613956537),
        ("T", "ht6", 2, 0.000764070473307),
        ("D", "ht6", 0, 0.000097401828163),
    ]
    print("\n  pin3's changed entries, read as an error in y0*:")
    implied = []
    for atom, stratum, idx, newval in reported:
        a = next(x for x in d["data"]["at_q0_per_stratum"][stratum]["per_atom"]
                 if x["atom"] == atom)
        wj = abs(a["weights"][idx])
        t = a["t_cost"]
        am = min(range(len(t)), key=lambda i: t[i])
        eps = newval * wj
        print(f"    {atom:4s} {stratum} y_star[{idx}] 0.0 -> {newval:.12g}"
              f"   (index is argmin: {idx == am})"
              f"   => |y0* - min t| = {eps:.3e}"
              f"   rel {eps / abs(t[am]):.3e}")
        implied.append({"atom": atom, "stratum": stratum, "index": idx,
                        "is_argmin": idx == am, "implied_y0_error": eps,
                        "relative": eps / abs(t[am])})

    out = {
        "computation": "alpha-5-lp-dual-crystal-closed-form",
        "bean": "qou/pin3",
        "reads": WITNESS.name,
        "conclusion": (
            "The LP is NOT degenerate: G is diagonal and positive, so the "
            "primal is an argmin and the dual optimum is a unique point, "
            "not a face. pin3's 'solver landed on a different vertex' is "
            "ruled out. The observed diff is a solver-tolerance error in "
            "y0* amplified by 1/|w| ~ 1e+05 in the ht6 strata."),
        "per_stratum": rows,
        "pin3_entries_as_y0_error": implied,
        "all_passed": ok_all,
    }
    path = HERE / "alpha-5-lp-dual-crystal-closed-form.results.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=False)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {path.name}")
    print("closed form reproduces every LP field"
          if ok_all else "MISMATCH — closed form does not hold")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
