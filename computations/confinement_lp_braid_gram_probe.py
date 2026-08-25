#!/usr/bin/env python3
"""Can the braid enter t or G and break the confinement-LP degeneracy?

Bean `qou/ndsa`. It names three candidates and says to check the
cheapest first. This checks the first two **exactly**, in ℚ(q), and
rules out both — for the same structural reason, which also says what
a surviving candidate has to do.

Builds on `operator_selection_lp_symbolic_qq.py` (bean `qou/k4f8`),
which established for `H₃(q)`:

- `t` is row 0 of the Gram, since `tⱼ = tr_M(b₀bⱼ)` and `b₀ = 1`;
- `det G = 0` identically, radical `v ∼ (−1/q)^len(wᵢ)`;
- `⟨𝟙,v⟩ = −(q−1)(q²−q+1) ≠ 0` for `q ≠ 1`;
- hence `y₀ = 0` for every dual-feasible pair.

Pure stdlib, exact rational functions, no floating point.

## Candidate 1 — `solve_frobenius_dual_lp` with a knot-derived `u_demand`

`ndsa` calls this "the cheapest, CHECK THIS FIRST". That solver
(lp_dual_solver.py:114) uses **equality** on the Gram:

    min t·x   s.t.  1·x = n_target,   Gx = u_demand

Because `tⱼ = G₀ⱼ`, for *any* feasible `x`

    t·x = Σⱼ G₀ⱼ xⱼ = (Gx)₀ = u₀ .

The objective is **constant on the entire feasible set**. Not "the
optimum is degenerate" — there is nothing to optimise: every feasible
point scores `u₀`, the first component of the demand vector the caller
supplied. Making `u_demand` knot-dependent makes the LP's answer
knot-dependent by simply reading back one coordinate of its own input.

Worse for feasibility: `G` is singular, so `Gx = u` is solvable only
when `u ⊥ v`. A knot-derived demand profile has to satisfy that linear
constraint before the program is even feasible.

## Candidate 2 — a Gram built from the braid word

`ndsa` proposes `G^w_ij = tr_M(w bᵢ bⱼ)` (or `tr_M(bᵢ w bⱼ)`) in place
of the bare NF Gram. The check below computes both, exactly, for a
range of braid words `w`, and asks whether the radical survives.

It does, every time. The reason is representation-theoretic and does
not depend on which `w` is chosen: `V = Σⱼ vⱼbⱼ` is the
q-antisymmetriser, which spans a **two-sided ideal** (the sign block),
so `bᵢ w V ∈ span(bᵢ V)` and

    (G^w v)ᵢ = tr_M(bᵢ w V) = 0 .

Meanwhile `⟨t,v⟩ = tr_M(V) = 0` holds for the *cost* vector no matter
what Gram is used — it says only that `V` is in the radical of the
trace form. So all three hypotheses of `y_0_eq_zero_of_radical`
survive and `y₀ = 0` stays forced.

## What that leaves

Decorating the Gram cannot work. The degeneracy is not a property of
`G` — it is the conjunction

    (a) the cost vector is the Markov trace vector,  and
    (b) the form's radical is annihilated by whatever Gram is used.

(b) is automatic for anything of the form `tr_M(bᵢ w bⱼ)`. So a
surviving formulation has to break **(a)**: change the objective, not
the Gram. That is the same conclusion `ndsa` reached for the
angle-structure LP by a different route — "an informative offset needs
a symmetry-breaking objective".
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from operator_selection_lp_symbolic_qq import (  # noqa: E402
    ONE, ZERO, q, NF_BASIS, NF_NAMES, TR_M,
    nf_of_word, nf_tr, gram_h3, kernel, matvec, dot, det, rref,
)

#: Braid words to decorate the Gram with. `()` reproduces the bare NF
#: Gram (control); the rest are the words this corpus actually uses —
#: generators, the two Garside-ish products, the trefoil σ₀³, and the
#: figure-eight-shaped alternating word on two strands' worth of H₃.
BRAID_WORDS = {
    "identity (control)": (),
    "sigma_0": (0,),
    "sigma_1": (1,),
    "L+ = s0 s1": (0, 1),
    "e- = s0 s1 s0": (0, 1, 0),
    "trefoil s0^3": (0, 0, 0),
    "alternating s0 s1 s0 s1": (0, 1, 0, 1),
    "s1 s0 s1 s0 s1": (1, 0, 1, 0, 1),
    "long s0^2 s1^2 s0": (0, 0, 1, 1, 0),
}


def gram_with(word, *, side="left"):
    """G^w_ij = tr_M(w b_i b_j)  (side='left')
             or tr_M(b_i w b_j)  (side='mid').

    Both are computed by word concatenation and GB reduction — no
    representation theory is assumed, so this is an independent check
    of the ideal argument in the docstring.
    """
    n = len(NF_BASIS)
    out = []
    for i in range(n):
        row = []
        for j in range(n):
            if side == "left":
                w = tuple(word) + NF_BASIS[i] + NF_BASIS[j]
            else:
                w = NF_BASIS[i] + tuple(word) + NF_BASIS[j]
            row.append(nf_tr(nf_of_word(w)))
        out.append(row)
    return out


def main() -> int:
    G = gram_h3()
    t = TR_M
    v = kernel(G)[0]
    one_v = sum((v[i] for i in range(6)), ZERO)

    checks, ok_all = [], True

    def record(key, ok, detail):
        nonlocal ok_all
        ok_all &= bool(ok)
        checks.append({"key": key, "ok": bool(ok), "detail": detail})
        print(f"  {'ok  ' if ok else 'FAIL'}  {key}")
        print(f"          {detail}")

    print("Baseline (from k4f8), re-derived here rather than assumed\n")
    record("radical_exists", det(G).is_zero() and len(kernel(G)) == 1,
           f"det G = 0, nullity 1, v = ({', '.join(repr(x) for x in v)})")
    record("one_dot_v_nonzero", not one_v.is_zero(), f"<1,v> = {one_v}")

    # <t,v> = tr_M(V): a property of the COST vector and the radical,
    # independent of whichever Gram is in play.
    record("cost_orthogonal_to_radical", dot(t, v).is_zero(),
           "<t,v> = tr_M(V) = 0 — V is in the radical of the trace form, "
           "so this holds whatever Gram is used")

    # ── Candidate 1: equality formulation, objective is constant ──
    print("\nCandidate 1 — solve_frobenius_dual_lp, Gx = u_demand\n")
    record("cost_is_gram_row", all(t[j] == G[0][j] for j in range(6)),
           "t_j = G_0j, so t.x = (Gx)_0 = u_0 for EVERY feasible x")

    # Exhibit it: two different feasible points, same objective.
    # Take any x, set u := Gx; then any x' with Gx' = u scores the same.
    x_a = [ONE, q, -ONE, ZERO, q ** 2, ONE]
    u = matvec(G, x_a)
    x_b = [x_a[i] + v[i] for i in range(6)]      # differs by the radical
    record("feasible_set_has_constant_objective",
           (dot(t, x_a) - dot(t, x_b)).is_zero() and (dot(t, x_a) - u[0]).is_zero(),
           f"x and x+v both satisfy Gx = u and both score u_0 = {u[0]}"
           " — the program has nothing to optimise")

    # Feasibility side-condition the caller must satisfy.
    record("u_demand_must_be_orthogonal_to_radical",
           all((dot(matvec(G, xx), v)).is_zero() for xx in (x_a, x_b)),
           "Gx = u is solvable only for u ⊥ v, so a knot-derived demand "
           "profile is constrained before the LP is even feasible")

    # ── Candidate 2: braid-decorated Gram ──
    print("\nCandidate 2 — Gram built from the braid word\n")
    per_word = []
    for label, word in BRAID_WORDS.items():
        row = {"word": label, "generators": list(word)}
        for side in ("left", "mid"):
            Gw = gram_with(word, side=side)
            Gwv = matvec(Gw, v)
            annihilates = all(x.is_zero() for x in Gwv)
            _, _, rank = rref(Gw)
            row[side] = {"annihilates_radical": annihilates, "rank": rank,
                         "det_zero": det(Gw).is_zero()}
            ok = annihilates
            record(f"radical_survives[{side}]  w = {label}", ok,
                   f"G^w v = 0: {annihilates}   rank {rank}/6   "
                   f"det G^w = 0: {det(Gw).is_zero()}")
        per_word.append(row)

    print("\n  => every braid-decorated Gram annihilates the radical, and")
    print("     <t,v> = 0 regardless of the Gram. All three hypotheses of")
    print("     `y_0_eq_zero_of_radical` survive, so y_0 = 0 stays forced.")
    print("     Decorating G cannot break the degeneracy — only changing t can.\n")

    out = {
        "computation": "confinement-lp-braid-gram-probe",
        "bean": "qou/ndsa",
        "field": "Q(q) — exact, no floating point",
        "conclusion": (
            "Candidates 1 and 2 both fail. Candidate 1's objective is "
            "constant on its feasible set (t.x = u_0), so it optimises "
            "nothing and merely reads back a coordinate of its own input. "
            "Candidate 2 leaves the radical intact for every braid word "
            "tried, on both sides, because V spans a two-sided ideal; with "
            "<t,v> = tr_M(V) = 0 holding for any Gram, y_0 = 0 remains "
            "forced. A surviving formulation must change the COST vector, "
            "not the Gram."),
        "radical": [repr(x) for x in v],
        "one_dot_radical": repr(one_v),
        "per_braid_word": per_word,
        "checks": checks,
        "all_passed": ok_all,
    }
    path = HERE / "confinement-lp-braid-gram-probe.results.json"
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {path.name}")
    print(f"{sum(1 for c in checks if c['ok'])}/{len(checks)} checks passed")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
