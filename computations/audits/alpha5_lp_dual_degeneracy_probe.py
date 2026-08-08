#!/usr/bin/env python3
"""alpha5_lp_dual_degeneracy_probe.py — is `alpha_5_lp_dual_crystal`'s LP dual
genuinely solver-dependent, or is it determined by the data?

THE QUESTION (bean qou-pin3)
    Regenerating `alpha-5-lp-dual-crystal.witness.json` moved 24 dual entries,
    one from exactly `0.0` to `0.0207`. An ~11.5 ppb q₀ move cannot do that. The
    bean's hypothesis was a **degenerate LP with multiple optimal duals**, where
    a different solver stack (the witness predates `clarabel` + `pyhecke-native`
    being installed here) landed on a different vertex.

    That hypothesis is testable, because this particular LP has a CLOSED FORM.

THE LP, WRITTEN OUT
    `per_atom_lp` builds  G = diag(|weight_λ|)  — **diagonal**, because
    Wedderburn blocks are τ-orthogonal — and solves

        min  t·x     s.t.   Σ x = n_target,   G x >= 0,   x >= -M

    With G diagonal, `Gx >= 0` is just `x_λ >= 0` on every channel with
    `|weight_λ| > 0`. So the feasible set is a scaled simplex and the optimum
    puts all mass on the cheapest channel.

    Stationarity `t = y0·1 + G'y` then gives, componentwise,

        y0*   = min_λ t_λ                    (over channels with |w_λ| > 0)
        y_λ*  = (t_λ − y0*) / |w_λ|          (>= 0 automatically)

    which is a FUNCTION OF THE DATA. Where that holds there is no vertex to
    choose and no solver dependence — a changed `y_star` means changed `t` or
    changed `w`, which is a different and more serious finding than the bean
    supposed.

    The closed form can fail in exactly two places, and the probe reports both:
      * a channel with `|weight_λ| = 0` (`weight_by_shape.get(..., 0.0)`
        defaults missing shapes to zero). Its row of G vanishes, so `x_λ` is
        unconstrained down to `-M` and `y_λ` drops out of stationarity — the
        dual really is undetermined there.
      * a TIE for `min_λ t_λ`. The primal optimum is then a face, not a vertex;
        the dual stays unique here, but the primal `x_star` does not.

WHAT THIS BUYS
    If the closed form reproduces the regenerated duals, the deterministic
    tie-break asked for is simply: compute the dual in closed form and stop
    asking HiGHS. That is stronger than a tie-break rule — it removes the
    solver from the answer.

Read-only. Reports; changes nothing.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent
ALPHA = COMPUTE_DIR / "alpha"
WITNESS = ALPHA / "alpha-5-lp-dual-crystal.witness.json"

for p in (str(ALPHA), str(COMPUTE_DIR), str(COMPUTE_DIR / "substrate"),
          str(REPO / "tools" / "qou-substrate" / "python"),
          str(REPO / "tools" / "pyhecke" / "python")):
    if p not in sys.path:
        sys.path.insert(0, p)

TOL_ZERO = 1e-12


def closed_form_dual(t, w, *, tol=1e-14):
    """(y0, y, notes) from the data alone — no solver."""
    import numpy as np
    t = np.asarray(t, dtype=float)
    w = np.abs(np.asarray(w, dtype=float))
    live = w > tol
    notes = []
    if not live.any():
        return None, None, ["every channel has |weight| = 0"]
    y0 = float(t[live].min())
    ties = int(((t - y0) <= tol).sum())
    if ties > 1:
        notes.append(f"{ties}-way tie for min t -> primal optimum is a FACE")
    dead = int((~live).sum())
    if dead:
        notes.append(f"{dead} channel(s) with |weight| = 0 -> dual undetermined there")
    y = []
    for i in range(len(t)):
        y.append(float((t[i] - y0) / w[i]) if live[i] else float("nan"))
    return y0, y, notes


def _committed(path: Path):
    try:
        raw = subprocess.check_output(
            ["git", "show", f"HEAD:{path.relative_to(REPO)}"], cwd=str(REPO),
            stderr=subprocess.DEVNULL)
        return json.loads(raw)
    except Exception:  # noqa: BLE001
        return None


def _walk_lps(node, trail=()):
    """Yield (path, record) for every per-atom LP record in the witness."""
    if isinstance(node, dict):
        if "lp" in node and "weights" in node and "t_cost" in node:
            yield trail, node
        for k, v in node.items():
            yield from _walk_lps(v, trail + (str(k),))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from _walk_lps(v, trail + (str(i),))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-report", type=int, default=8)
    args = ap.parse_args(argv)

    print("=" * 72)
    print("alpha_5_lp_dual_crystal — is the dual solver-dependent?")
    print("=" * 72)

    if not WITNESS.exists():
        print(f"  witness not found: {WITNESS}")
        return 1
    live = json.loads(WITNESS.read_text(encoding="utf-8"))
    comm = _committed(WITNESS)

    recs = list(_walk_lps(live.get("data", live)))
    print(f"  per-atom LP records in the witness : {len(recs)}")

    agree = disagree = skipped = 0
    face = zeroweight = 0
    shown = 0
    for trail, rec in recs:
        t, w = rec.get("t_cost"), rec.get("weights")
        lp = rec.get("lp") or {}
        y_solver = lp.get("y_star")
        y0_solver = lp.get("y0_star")
        if not (t and w and y_solver):
            skipped += 1
            continue
        y0_cf, y_cf, notes = closed_form_dual(t, w)
        if y0_cf is None:
            skipped += 1
            continue
        if any("FACE" in n for n in notes):
            face += 1
        if any("|weight| = 0" in n for n in notes):
            zeroweight += 1
        worst = 0.0
        for a, b in zip(y_cf, y_solver):
            if a != a:                      # nan -> dual undetermined here
                continue
            worst = max(worst, abs(a - float(b)) / max(1.0, abs(a), abs(float(b))))
        d0 = abs(y0_cf - float(y0_solver)) / max(1.0, abs(y0_cf))
        ok = worst < 1e-9 and d0 < 1e-9
        agree += ok
        disagree += (not ok)
        if (not ok or notes) and shown < args.max_report:
            shown += 1
            print(f"\n  {'/'.join(trail) or '<root>'}")
            print(f"      closed-form y0 = {y0_cf:.12g}   solver y0 = "
                  f"{float(y0_solver):.12g}   |Δrel| = {d0:.2e}")
            print(f"      max |Δrel| over y_star = {worst:.2e}   "
                  f"{'MATCH' if ok else 'MISMATCH'}")
            for n in notes:
                print(f"      note: {n}")

    print("\n" + "-" * 72)
    print(f"  closed form reproduces the solver dual : {agree}/{agree + disagree}")
    print(f"  records with a min-t tie (primal face) : {face}")
    print(f"  records with a zero-weight channel     : {zeroweight}")
    print(f"  skipped (no data)                      : {skipped}")

    if comm is not None:
        print("\n" + "-" * 72)
        print("  COMMITTED witness vs the closed form (the bean's 24 moved entries)")
        print("-" * 72)
        cmap = {"/".join(tr): r for tr, r in _walk_lps(comm.get("data", comm))}
        cagree = cdis = 0
        for trail, rec in recs:
            key = "/".join(trail)
            crec = cmap.get(key)
            if not crec:
                continue
            t, w = crec.get("t_cost"), crec.get("weights")
            yc = (crec.get("lp") or {}).get("y_star")
            if not (t and w and yc):
                continue
            y0_cf, y_cf, _ = closed_form_dual(t, w)
            if y0_cf is None:
                continue
            worst = 0.0
            for a, b in zip(y_cf, yc):
                if a != a:
                    continue
                worst = max(worst, abs(a - float(b)) / max(1.0, abs(a), abs(float(b))))
            cagree += worst < 1e-9
            cdis += worst >= 1e-9
        print(f"  closed form reproduces the COMMITTED dual : {cagree}/{cagree + cdis}")
        print()
        if cdis and not disagree:
            print("  => The regenerated dual satisfies the closed form and the")
            print("     committed one does NOT. The committed witness is wrong on")
            print("     its own data, and the change is a CORRECTION, not a")
            print("     solver-vertex coin flip.")
        elif cdis and disagree:
            print("  => NEITHER matches the closed form. The stationarity")
            print("     assumption is wrong somewhere — read the two notes above")
            print("     before trusting either witness.")
        elif not cdis and not disagree:
            print("  => Both match. The dual is determined by the data and the")
            print("     24 moved entries came from the DATA moving, not the LP.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
