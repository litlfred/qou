#!/usr/bin/env python3
"""There is no coincidence to explain: the substrate lies on the critical face
at *every* `q`, by an identity — and binding is a p/n dual-vertex hysteresis.

THE QUESTION, AND WHY IT WAS THE WRONG ONE
---------------------------------------------
Last turn I found the aggregation gap is zero at `q_0` and that the Markov cost
sits exactly on the boundary of the no-gap region, and asked: **why does the
substrate sit exactly on that critical face?** That framing conflated two
different boundaries, and once they are separated the question dissolves.

  * **In cost space** the Markov cost does lie on the boundary — and it does so
    at **every** `q`, because the condition is an algebraic identity. There is
    no fine-tuning of `q_0` in it whatsoever.
  * **In `q`** the thing that actually turns binding on and off is a pair of
    dual-vertex transitions, and `q_0` is nowhere near them — a factor 2.28 away.

**I withdraw the "why does the substrate sit exactly there" framing.** It sits
there always; and the boundary it sits on is not the boundary that matters.

WHAT PUTS IT ON THE COST-SPACE FACE: THE MARKOV PROPERTY
----------------------------------------------------------
The dual is `phi(v) = max { y . (Gv) : G y <= t, y >= 0 }` (`G` symmetric). The
scaled vertex `y = lam e_2` has `lam = min_i t_i / G[i,2]`, and at `q_0`:

    i   name      t_i / G[i,2]
    0   gamma     1.6321519915   \  2-fold tie
    1   s0        1.6321519915   /
    2   s1        0.5431204241   \
    3   L+        0.5431204241    >  3-FOLD TIE  <- the argmin
    4   L-        0.5431204241   /
    5   e-        1.3294677323

A 3-fold argmin means the vertex carries 5 nonnegativity constraints plus
**3** tight dual rows: 8 active constraints in `R^6`, two more than a vertex
needs. That degeneracy is what makes the cost critical.

And it is **not** special to `q_0`. The `2<->3` leg of the tie is the identity

    G[3,2]  =  z . G[2,2]                 (residual 1.2e-31 at 40 dps, four q)

which is the Markov property `tr(x . T_n) = z . tr(x)` written in the Gram; the
`3<->4` leg is the `L+ / L-` symmetry. Sweeping `h` from 0.05 to 2.5 the argmin
set is `{2,3,4}` at every single point, inside the binding window and out.

**So the substrate lies on that face for the same reason the trace is a link
invariant.** It is an identity, not a coincidence — which is exactly the
resolution the question was asking for, in the opposite direction from the one
the framing implied.

THE TWO COMPETING VERTICES, AND WHAT `t = G e_1` ACTUALLY DOES
-----------------------------------------------------------------
    e_0      :  G e_0 - t  =  0 exactly, ALL SIX dual rows tight
    lam e_2  :  tight rows {2, 3, 4} only

`e_0` is dual-feasible with every constraint at equality precisely *because*
`t = G e_1` (`h3a_frobenius_gram_offdiagonal_probe`). So `t = G e_1` is what
puts a second, maximally degenerate vertex into the problem — that is its real
role here.

But `t = G e_1` is **not** what produces the zero, and my earlier reading of it
as the blanket obstruction is too strong. Costs that are also rows of `G` split
both ways: rows 0, 2, 4 give no gap; rows **1, 3, 5 open gaps** of 9.5e-3,
2.1e-2 and 5.2e-3. And of 150 random costs of the form `c = G w`, `w >= 0`,
**150 of 150** open a gap. Being a row of the Gram is neither necessary nor
sufficient.

BINDING IS A HYSTERESIS BETWEEN THE PROTON'S AND NEUTRON'S TRANSITIONS
------------------------------------------------------------------------
Each nucleon independently switches which dual vertex is optimal for it, as `h`
grows, from `lam e_2` to `e_0`:

    proton  switches at   h = 0.47718474189158
    neutron switches at   h = 0.56984033

Between those two values the proton has switched and the neutron has not, so
they no longer share a dual vertex and `phi` is no longer linear along the ray.
**That interval is the binding window** — and it matches, to `4e-15` and
`4.4e-8`, the window edges bisected independently in
`nfold_ip_coupling_duality_gap_probe.py` from the gap itself. Outside it both
nucleons sit on the same vertex and the gap is an exact zero.

So the whole phenomenon has one sentence: **binding is the split between the
proton's and the neutron's dual-vertex transition points.**

WHERE `q_0` SITS
------------------
Not close. `h(q_0) = 0.20906` against a proton transition at `0.47718` — a
factor of **2.283**. And the margin by which each nucleon prefers `lam e_2`
over `e_0` at `q_0`, i.e. `lam (Gv)_2 - (Gv)_0`:

    proton    +0.064728052   ( +9.33 % )
    neutron   +0.144249088   ( +23.29 % )

Both comfortably positive, with the proton nearer to switching — which is why
it is the proton that switches first. `q_0` is deep in the interior of the
shared-vertex region, not on any knife edge in `q`.

WHAT THIS SETTLES FOR L2 1PPQ
--------------------------------
The zero at `q_0` is robust, structural and now fully explained. It is not
fine-tuning, not a cost-functional artefact, and not repairable by moving `q` a
little. Binding in this construction requires the two nucleons to straddle a
dual-vertex transition, and at `q_0` they are on the same side of it by 9 % and
23 % margins.

That relocates the problem, precisely: the transition points are properties of
`v_p` and `v_n` — of the **nucleon chains**, not of `q`. Whatever is supposed to
bind light isotopes has to come from something that separates the proton and
neutron objectives far more than the present flavour split does, or from
constraints not in `{G x >= G v, x >= 0}` at all. Both are now well-posed;
neither is a search over cost functionals.

DISCIPLINE
----------
No fit; no `B_AME`; nothing wired. The tie identity is checked at 40 dps against
the corpus's `gram_matrix_mp`; the argmin sweep and the two transitions are
float64 LP with 50-step bisections; the margins are exact linear-algebra, no LP.
The transition-vs-window agreement is a genuine cross-check: the two numbers are
produced by different computations (dual support here, primal gap there).

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] nfold_ip_coupling_duality_gap_probe.py (window edges, independently)
-- Ref: [probe] which_functional_the_substrate_extremises_probe.py (the rank-one dual)
-- Ref: [probe] h3a_frobenius_gram_offdiagonal_probe.py (t = G e_1)
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from scipy.optimize import linprog  # noqa: E402

from pyhecke.gram import _hm_mp, gram_matrix_mp  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
NAMES = ["gamma", "s0", "s1", "L+", "L-", "e-"]
H_Q0 = float(mp.mpf(str(Q0)) - 1 / mp.mpf(str(Q0)))
# window edges bisected independently from the gap, previous probe
WIN_LO, WIN_HI = 0.47718474189158, 0.56984029056366


def q_of_h(hv):
    hv = mp.mpf(hv)
    return hv / 2 + mp.sqrt(hv * hv + 4) / 2


def build(hv):
    q = q_of_h(hv)
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    gram = np.array([[float(x) for x in row] for row in gram_matrix_mp(30, q=q)])
    cost = np.array([float(x) for x in
                     [mp.mpf(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]])

    def nucleon(kind):
        nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
        for _ in range(3):
            nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
            nf = _hm_mp(nf, mp.mpf(1), -h, 1, h)
        if kind == "p":
            nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
            nf = _hm_mp(nf, mp.mpf(1), -h / 2, 0, h)
            nf = _hm_mp(nf, mp.mpf(1), -h / 2, 1, h)
        else:
            nf = _hm_mp(nf, mp.mpf(1), -h / 2, 0, h)
            nf = _hm_mp(nf, mp.mpf(1), -h / 2, 0, h)
            nf = _hm_mp(nf, mp.mpf(1), -h, 1, h)
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, h)
        return np.array([float(x) for x in nf])

    return gram, cost, nucleon("p"), nucleon("n")


def ratios(gram, cost):
    return [cost[i] / gram[i, 2] if abs(gram[i, 2]) > 1e-14 else float("inf")
            for i in range(6)]


def argmin_set(rat):
    lam = min(rat)
    return lam, [i for i, r in enumerate(rat)
                 if abs(r - lam) < 1e-9 * max(1.0, abs(lam))]


def dual_y(gram, cost, v):
    r = linprog(cost, A_ub=-gram, b_ub=-(gram @ v),
                bounds=[(0, None)] * 6, method="highs")
    return (float(r.fun), -r.ineqlin.marginals) if r.success else (None, None)


def on_e0(hv, kind):
    gram, cost, vp, vn = build(hv)
    _, y = dual_y(gram, cost, vp if kind == "p" else vn)
    return y is not None and abs(y[0]) > 1e-9


def bisect(kind, a, b):
    fa = on_e0(a, kind)
    for _ in range(50):
        m = 0.5 * (a + b)
        if on_e0(m, kind) == fa:
            a = m
        else:
            b = m
    return 0.5 * (a + b)


def main() -> int:
    assertions = []
    print("t7qv — the binding window is a p/n dual-vertex hysteresis")
    gram0, cost0, vp0, vn0 = build(H_Q0)

    # ── A1. the 3-fold tie is an identity in q ────────────────────────
    print("\n  1. the 3-fold argmin tie holds at EVERY q — it is an identity")
    rat0 = ratios(gram0, cost0)
    lam0, arg0 = argmin_set(rat0)
    print(f"     at q_0:  " + "  ".join(f"{NAMES[i]}={rat0[i]:.9f}"
                                        for i in range(6)))
    print(f"     argmin = {arg0}  (lam = {lam0:.12f})")
    sweep_ok = True
    seen = set()
    for hv in (0.05, 0.15, H_Q0, 0.35, 0.45, 0.50, 0.535, 0.57, 0.65,
               0.90, 1.5, 2.5):
        g, c, _, _ = build(hv)
        _, a = argmin_set(ratios(g, c))
        seen.add(tuple(a))
        sweep_ok &= (tuple(a) == (2, 3, 4))
    # the underlying identity, at high precision
    ident = 0.0
    for qv in ("1.1099785827513808", "1.3", "1.7", "2.5"):
        q = mp.mpf(qv)
        z = q ** 3 / (q ** 2 + 1)
        gm = gram_matrix_mp(30, q=q)
        row3 = gm[3] if isinstance(gm[3], list) else gm[3]
        row2 = gm[2] if isinstance(gm[2], list) else gm[2]
        ident = max(ident, float(abs(row3[2] - z * row2[2])))
    ok = bool(sweep_ok and arg0 == [2, 3, 4] and ident < 1e-25)
    print(f"     argmin sets seen over h in [0.05, 2.5]: {sorted(seen)}")
    print(f"     identity G[3,2] = z G[2,2]: max residual {ident:.2e} "
          f"over four q at 40 dps")
    print(f"     -> the Markov property puts the cost on the face, at all q")
    assertions.append(("A1_three_fold_tie_is_an_identity_in_q", ok,
                       f"argmin = (2,3,4) at 12 values of h; "
                       f"G[3,2]=z G[2,2] residual {ident:.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the two competing vertices ────────────────────────────────
    print("\n  2. the two competing dual vertices")
    res_e0 = gram0 @ np.eye(6)[0] - cost0
    tight_e0 = [i for i in range(6) if abs(res_e0[i]) < 1e-12]
    res_l2 = lam0 * gram0[:, 2] - cost0
    tight_l2 = [i for i in range(6) if abs(res_l2[i]) < 1e-9]
    ok = len(tight_e0) == 6 and tight_l2 == [2, 3, 4]
    print(f"     e_0      : G e_0 - t = {np.round(res_e0, 12)}")
    print(f"                tight rows {tight_e0}  -> ALL SIX (this is t = G e_1)")
    print(f"     lam e_2  : tight rows {tight_l2}  -> the 3-fold Markov tie")
    assertions.append(("A2_two_competing_degenerate_vertices", ok,
                       f"e_0 has all 6 dual rows tight; lam e_2 has {tight_l2}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. t = G e_1 is neither necessary nor sufficient ─────────────
    print("\n  3. being a row of G is neither necessary nor sufficient")

    def relgap(gram, c, vp, vn):
        a, _ = dual_y(gram, c, vp)
        b, _ = dual_y(gram, c, vn)
        ab, _ = dual_y(gram, c, vp + vn)
        if None in (a, b, ab):
            return None
        return (a + b - ab) / max(abs(a + b), 1e-30)

    rows_gap = {}
    for k in range(6):
        g = relgap(gram0, gram0[k], vp0, vn0)
        rows_gap[k] = g
        print(f"     cost = row {k} ({NAMES[k]:<7s}): relgap = "
              f"{'INFEASIBLE' if g is None else f'{g:+.3e}'}")
    rng = np.random.default_rng(3)
    pos = tot = 0
    for _ in range(150):
        w = rng.random(6)
        c = gram0 @ w
        if np.any(c <= 0):
            continue
        tot += 1
        g = relgap(gram0, c, vp0, vn0)
        if g is not None and g > 1e-8:
            pos += 1
    opened = [k for k, g in rows_gap.items() if g is not None and g > 1e-8]
    ok = bool(len(opened) >= 2 and pos == tot and tot > 100)
    print(f"     rows of G that DO open a gap: {opened}")
    print(f"     random costs c = G w, w >= 0: {pos}/{tot} open a gap")
    print(f"     -> my earlier 't = G e_1 is the obstruction' reading was too "
          f"strong")
    assertions.append(("A3_row_of_gram_neither_necessary_nor_sufficient", ok,
                       f"rows {opened} open gaps; {pos}/{tot} random Gw open "
                       f"gaps"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. each nucleon has its own transition ───────────────────────
    print("\n  4. each nucleon switches vertex at its own h")
    hp = bisect("p", 0.40, 0.55)
    hn = bisect("n", 0.50, 0.65)
    dp, dn = abs(hp - WIN_LO), abs(hn - WIN_HI)
    ok = dp < 1e-10 and dn < 1e-6
    print(f"     proton  lam e_2 -> e_0 at h = {hp:.14f}")
    print(f"     neutron lam e_2 -> e_0 at h = {hn:.14f}")
    print(f"     window edges from the GAP (previous probe): "
          f"{WIN_LO:.14f}, {WIN_HI:.14f}")
    print(f"     agreement: {dp:.2e} and {dn:.2e}  — different computations")
    assertions.append(("A4_transitions_equal_the_window_edges", ok,
                       f"proton {hp:.12f} vs {WIN_LO:.12f} ({dp:.1e}); "
                       f"neutron {hn:.12f} vs {WIN_HI:.12f} ({dn:.1e})"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. binding = the hysteresis interval ─────────────────────────
    print("\n  5. binding is exactly the interval where they disagree")
    print(f"     {'h':>8s}  {'y*_p':<10s} {'y*_n':<10s} {'share?':<7s} "
          f"{'relgap':>11s}")
    rows = []
    for hv in (0.30, 0.45, 0.49, 0.535, 0.56, 0.60, 0.80):
        g, c, a, b = build(hv)
        _, yp = dual_y(g, c, a)
        _, yn = dual_y(g, c, b)
        sp_ = "e_0" if abs(yp[0]) > 1e-9 else "lam e_2"
        sn = "e_0" if abs(yn[0]) > 1e-9 else "lam e_2"
        share = np.allclose(yp, yn, atol=1e-9)
        rg = relgap(g, c, a, b)
        rows.append((share, rg))
        print(f"     {hv:8.3f}  {sp_:<10s} {sn:<10s} {str(share):<7s} "
              f"{rg:+11.3e}")
    ok = all((abs(rg) < 1e-9) == share for share, rg in rows)
    print(f"     -> gap is nonzero EXACTLY when they do not share a vertex")
    assertions.append(("A5_gap_iff_vertices_differ", ok,
                       "share-vertex <=> zero gap holds at all 7 sampled h"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. q_0 is far from the transition ────────────────────────────
    print("\n  6. q_0 is not near any transition")
    margins = {}
    for nm, v in (("proton", vp0), ("neutron", vn0)):
        a = lam0 * float((gram0 @ v)[2])
        b = float((gram0 @ v)[0])
        margins[nm] = (a - b, 100 * (a - b) / max(a, b))
        print(f"     {nm:<8s} lam(Gv)_2 = {a:.9f}  (Gv)_0 = {b:.9f}  "
              f"margin {a - b:+.9f} ({margins[nm][1]:+.2f}%)")
    factor = hp / H_Q0
    ok = bool(all(m > 0 for m, _ in margins.values()) and factor > 2)
    print(f"     h(q_0) = {H_Q0:.12f} vs proton transition {hp:.6f}: "
          f"factor {factor:.3f}")
    print(f"     q_0 = {float(q_of_h(H_Q0)):.12f}; window opens at "
          f"q = {float(q_of_h(hp)):.12f}")
    assertions.append(("A6_q0_deep_inside_shared_vertex_region", ok,
                       f"margins +{margins['proton'][1]:.2f}% and "
                       f"+{margins['neutron'][1]:.2f}%; transition is "
                       f"{factor:.2f}x h(q_0)"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  There is no coincidence to explain, and I withdraw the framing")
    print("  that there was. The Markov cost lies on the critical face at")
    print("  EVERY q, because the 3-fold argmin tie is the identity")
    print("  G[3,2] = z G[2,2] — the Markov property in the Gram. And that")
    print("  face is not what controls binding. What controls it is that the")
    print("  proton and the neutron each switch dual vertex (lam e_2 -> e_0)")
    print("  at their own h, 0.47718 and 0.56984, and the binding window is")
    print("  exactly the interval between — verified against the window edges")
    print("  bisected independently from the gap itself. Binding is the split")
    print("  between the two nucleons' transitions.")
    print("  q_0 sits at h = 0.20906, a factor 2.28 below the first")
    print("  transition, with margins of +9.33% and +23.29%. The zero is")
    print("  robust, and it relocates the problem onto the nucleon chains:")
    print("  binding needs something that separates v_p from v_n far more")
    print("  than the present flavour split, or constraints outside")
    print("  {Gx >= Gv, x >= 0} altogether.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="scipy")
        wb.set_description(
            "Dissolves the question of why the substrate sits on the critical "
            "face of the binding LP. Two boundaries were conflated. In cost "
            "space the Markov cost lies on the boundary at EVERY q, because "
            "the argmin of t_i/G[i,2] is 3-fold tied on {s1, L+, L-} by the "
            "identity G[3,2] = z G[2,2] (residual 1.2e-31 at 40 dps) — the "
            "Markov property written in the Gram — so there is no fine-tuning "
            "of q_0. In q, what turns binding on is that the proton and "
            "neutron each switch dual vertex from lam e_2 to e_0 at their own "
            "h (0.47718474189158 and 0.56984033), and the binding window is "
            "exactly the interval between, matching to 4e-15 and 4.4e-8 the "
            "edges bisected independently from the gap in "
            "nfold_ip_coupling_duality_gap_probe. Binding is the split between "
            "the two nucleons' transitions. q_0 sits a factor 2.28 below the "
            "first one with margins of +9.33% and +23.29%, so the zero is "
            "robust. Also corrects an earlier over-reading: t = G e_1 is "
            "neither necessary nor sufficient for the zero — rows 1, 3, 5 of G "
            "open gaps and 150/150 random costs Gw do too; its actual role is "
            "to make e_0 a dual vertex with all six rows tight.")
        wb.add_data("ratio_vector_at_q0",
                    {NAMES[i]: f"{rat0[i]:.12f}" for i in range(6)})
        wb.add_data("argmin_set", arg0)
        wb.add_data("tie_identity_residual", f"{ident:.3e}")
        wb.add_data("transitions", {"proton_h": f"{hp:.14f}",
                                    "neutron_h": f"{hn:.14f}"})
        wb.add_data("window_edges_from_gap", {"lo": f"{WIN_LO:.14f}",
                                              "hi": f"{WIN_HI:.14f}"})
        wb.add_data("margins_at_q0",
                    {k: f"{v[0]:+.9f} ({v[1]:+.2f}%)"
                     for k, v in margins.items()})
        wb.add_data("h_q0", f"{H_Q0:.12f}")
        wb.add_data("transition_over_h_q0", f"{factor:.4f}")
        wb.add_data("gram_rows_that_open_a_gap", opened)
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "WITHDRAWAL OF MY OWN FRAMING. The previous probe asked 'why does "
            "the substrate sit exactly on that critical face', treating it as "
            "a coincidence needing explanation. It is not one: the face is "
            "occupied at every q by an identity. The genuinely contingent "
            "quantities are the two nucleon transition points, and they are "
            "properties of the nucleon chains v_p, v_n rather than of q.")
        wb.add_caveat(
            "CORRECTION to the earlier reading of t = G e_1 as the blanket "
            "obstruction (h3a_frobenius_gram_offdiagonal_probe, carried "
            "forward in later probes). It is neither necessary nor sufficient "
            "for the no-gap property: rows 1, 3 and 5 of G open gaps of "
            "9.5e-3, 2.1e-2 and 5.2e-3, and 150 of 150 random costs of the "
            "form Gw with w >= 0 open gaps. Its real role is to make e_0 "
            "dual-feasible with all six rows tight, i.e. to supply the second "
            "competing degenerate vertex.")
        wb.add_caveat(
            "The neutron transition agrees with the independently bisected "
            "window edge to 4.4e-8, which is the bisection tolerance of the "
            "two runs rather than an exact match; the proton agrees to 4e-15. "
            "Both are cross-checks between a dual-support computation here and "
            "a primal-gap computation in the earlier probe, so the agreement "
            "is meaningful, but the neutron figure should be quoted to about "
            "seven digits, not fourteen.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
