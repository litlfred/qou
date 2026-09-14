"""The operator-selection LP's active set has cardinality d-1, whatever the basis.

Bean `qou-brng` (the linking-vs-self-energy amplitude assignment).

## Why this exists

The bean's 2026-09-12 entry (PR #7251, `qou-8urh`) excluded the LP's active set as
the binding multiplier for an ORTHOGONAL basis -- Wedderburn block projectors give
a diagonal Frobenius Gram, complementary slackness decouples to
`s_l * G_ll * x_l = 0`, the atom's traces never appear -- and named an escape:

    "What it does NOT exclude, and this is the live direction: a NON-ORTHOGONAL
     operator basis.  Actual braid sub-words overlap, so their Gram is dense and
     the LP recovers discriminating power.  That is the natural next thing to try
     for this bean, and nothing here touches it."

**The escape does not exist, and the diagnosis that produced it was the wrong
reason for a right conclusion.**  The active set is pinned by a DIMENSION COUNT,
not by the Gram's sparsity, so a dense Gram changes nothing.

## The theorem (section 2), which needs no numerics

In the solver's own constraint form (`pyhecke/lp_dual_solver.py:1147-1152`):

    max  t^T x    s.t.   1^T x = n_target   (dual y_0)
                         G x >= 0           (dual y >= 0)
                         x >= -M

Complementary slackness is `y_i * (G x)_i = 0`, and with `G_ij = tr_M(e_i e_j)`,

    (G x*)_i = sum_j tr_M(e_i e_j) x*_j = tr_M(e_i . Phi*) = <e_i, Phi*>_F,
    Phi* := sum_j x*_j e_j   (the selected operator)

so `active_set ⊆ { i : <e_i, Phi*>_F = 0 }`.  Then:

    **If G is invertible and n_target != 0, at most d-1 constraints can be tight.**
    If all d were tight then G x = 0, so x = 0, so 1^T x = 0 != n_target.

And a basic optimum in R^d needs d independent active constraints; the equality
supplies one, the box supplies none at an interior optimum, so d-1 come from
`G x >= 0`.  Hence **|active| = d-1 exactly**, for every well-posed instance.

`d` is the SIZE OF THE BASIS.  The active set therefore does not depend on the
atom's traces, the target, or the Gram's density -- it counts the basis.  A
binding multiplier must depend on the nucleus; this cannot.

## Scope

**Scope (b), structural exclusion.**  Invariant: invertibility of the Frobenius
Gram together with a non-zero net constraint.  Holds for every n, q, trace
convention, basis and target.  It excludes the LP's ACTIVE SET as a binding
multiplier; it does not touch the LP's optimal VALUE, its `y_0*`, or any other
route.

## The two escapes are the two degenerate cases, and the corpus is in both

* **Singular G** -- then `G x = 0` has a kernel and all `d` can be tight.  But a
  singular Gram means the operators are linearly dependent, i.e. not a basis.
  `h6_block_selection_lp_probe.py` records the production interface templates
  (`c*sigma_g + d*1`, convention D) at **rank 6 of 11**.
* **Indefinite G** -- then the LP is unbounded and the solver returns a corner of
  its box.  The same file records the braid sub-word basis -- the bean's named
  escape route -- with eigenvalues `[-1.579, -1.140, 0.441, 8.43, ...]`, and
  RETRACTED (2026-08-16) a "stable 7 of 11" read off it as a box artifact.

So the sub-word basis has already been tried and retracted; the bean's "nothing
here touches it" is stale with respect to the very file its own entry cites.

## A number in the bean that should not be quoted (section 4)

That entry reports "a controlled diagnostic changing only `G` gives 5-of-6 active
for `G = diag(t)` against **3-of-6** for a dense PSD `G`", and reads the 3 as the
dense Gram recovering discriminating power.  Reproduced exactly here (same seed,
same matrices), the 3-of-6 solve is **the same box artifact** the file retracts
one screen below:

    max|x*| = 3.7135e+06   against M_bound = 1e6
    primal_obj = -357264.02          (negative, for a MAXIMisation)
    duality_gap = 3.5726e+05         (well-posed solves here give ~1e-42)

A well-posed dense PSD instance gives **5 of 6 = d-1**, like every other.

NO ASSERTION HERE IS A FIT: every number is measured or solved.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_ROOT = _Path(__file__).resolve().parents[2]
for _p in (_ROOT / "computations", _ROOT / "tools" / "qou-substrate" / "python"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import _path_bridge as _bridge  # noqa: E402, F401

import math  # noqa: E402

GAP_OK = 1e-20          # a well-posed solve's duality gap; artifacts are ~1e5


def hdr(s: str) -> None:
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


def main() -> int:
    from mass_at_3A_proper import atom_braid_word_3A  # noqa: F401  (path bridge)
    import numpy as np
    import hecke_core_legacy as HC
    from pyhecke.trace import atom_character_raw
    from lp_dual_solver import solve_operator_selection_lp

    def solve(tv, Gm, target):
        r = solve_operator_selection_lp(np.asarray(tv, float),
                                        np.asarray(Gm, float), float(target))
        dd = r.to_dict()
        x = np.asarray(dd.get("x_star", dd.get("primal_x")), float)
        act = sorted(dd.get("active_set") or [])
        gap = abs(float(dd.get("duality_gap", float("nan"))))
        return x, act, gap, dd

    # ---------------------------------------------------------- corpus data
    six = sorted([e for e in HC._PARTITION_TABLE
                  if e.get("k", 0) == 6 and e.get("has_ysn")],
                 key=lambda x: tuple(x["partition"]))
    if not six:
        print("ABORT — no k=6 YSN entries; nothing measured.")
        return 2
    recs = []
    for e in six:
        ca, na, _ = atom_character_raw(2, 0, e, include_inter=True)
        ca = float(ca)
        if ca == 0:
            continue
        recs.append((float(e["wedderburn_weight"]), math.log(abs(ca)) + float(na)))
    mx = max(r[1] for r in recs)
    t = np.array([abs(r[0]) * math.exp(r[1] - mx) for r in recs])
    d = len(t)
    S = float(t.sum())

    # ------------------------------------------------------------ section 1
    hdr("[1] active_set = { i : <e_i, Phi*>_F = 0 }  — complementary slackness")

    G_diag = np.diag(t)
    print(f"  H_6 Wedderburn blocks: d = {d}, sum(t) = {S:.6f}, G = diag(t)\n")
    for frac in (0.10, 0.25, 0.50, 0.75, 0.99):
        x, act, gap, _ = solve(t, G_diag, frac * S)
        gx = G_diag @ x
        scale = max(1.0, float(abs(gx).max()))
        orth = sorted(i for i in range(d) if abs(gx[i]) < 1e-9 * scale)
        assert set(act).issubset(set(orth)), (frac, act, orth)
        print(f"   target {frac:.2f}*S : active {len(act):2d}   "
              f"|{{i : <e_i,Phi*>=0}}| {len(orth):2d}   gap {gap:.2e}")
    print("\n  VERIFIED: every active index is Frobenius-orthogonal to Phi*.")

    # ------------------------------------------------------------ section 2
    hdr("[2] |active| = d - 1, and it does NOT move with the Gram's density")

    print("  Non-orthogonal basis from corpus data, no new Markov traces:")
    print("  e_S := sum_{l in S} P_l over cyclic windows S of width w, so")
    print("  <e_S,e_T> = sum_{l in S^T} tr_M(P_l) — dense exactly as windows overlap.\n")
    print("     w   off-diag frac   rank(G)   |active| @ 0.25/0.50/0.75 * S   max gap")
    seen = []
    for w in range(1, 7):
        wins = [set((i + k) % d for k in range(w)) for i in range(d)]
        Gw = np.array([[sum(t[l] for l in a & b) for b in wins] for a in wins])
        tw = np.array([sum(t[l] for l in a) for a in wins])
        Sw = float(tw.sum())
        offd = float((np.count_nonzero(Gw) - d) / (d * d - d))
        rk = int(np.linalg.matrix_rank(Gw))
        acts, gaps = [], []
        for frac in (0.25, 0.50, 0.75):
            _, act, gap, _ = solve(tw, Gw, frac * Sw)
            acts.append(len(act))
            gaps.append(gap)
        print(f"     {w}   {offd:11.3f}   {rk:7d}   {acts[0]:5d} /{acts[1]:5d} /{acts[2]:5d}"
              f"            {max(gaps):.1e}")
        assert rk == d, (w, rk)
        assert max(gaps) < GAP_OK, (w, gaps)          # well-posed
        assert all(a == d - 1 for a in acts), (w, acts)
        seen.append((w, offd, acts))
    print(f"\n  Off-diagonal fraction 0.000 -> 1.000; |active| = {d - 1} = d-1 throughout.")
    print("  Density is not the variable.  The dimension count is.")

    # ------------------------------------------------------------ section 3
    hdr("[3] Why d-1, from the constraints alone")

    print(f"""  max t^T x  s.t.  1^T x = n_target,  G x >= 0,  x >= -M,  in R^{d}.

  UPPER BOUND.  G invertible and n_target != 0  =>  at most d-1 tight:
    all d tight  =>  G x = 0  =>  x = 0  =>  1^T x = 0 != n_target.
  LOWER BOUND.  A basic optimum needs d independent active constraints; the
    equality gives 1 and the box gives 0 at an interior optimum, so d-1 come
    from G x >= 0.

  Hence |active| = d-1: A FUNCTION OF THE BASIS SIZE ALONE.  It is independent
  of the atom's traces t, of n_target, and of the Gram's density — all three
  measured above.  A binding multiplier must depend on the NUCLEUS.  This
  cannot, under any basis.  Scope (b); invariant = invertibility of G plus a
  non-zero net constraint.""")

    # ------------------------------------------------------------ section 4
    hdr("[4] The bean's '3-of-6 for a dense PSD G' is a box artifact")

    rng = np.random.default_rng(7)                 # h6_block_selection_lp_probe.py:145
    tt = np.array([0.1, 0.2, 0.05, 0.4, 0.15, 0.3])
    A = rng.normal(size=(6, 6))
    G_w = A @ A.T / 6.0                            # its exact dense PSD matrix
    print("  Exact reproduction of h6_block_selection_lp_probe.py:145-150.\n")
    print("    Gram                       rank  eig_min    |active|   max|x*|    primal        gap")
    for name, G in (("diag(t)", np.diag(tt)), ("dense PSD (seed-7 Wishart)", G_w)):
        x, act, gap, dd = solve(tt, G, 0.5 * float(tt.sum()))
        ev = float(np.linalg.eigvalsh(G).min())
        print(f"    {name:<26s} {int(np.linalg.matrix_rank(G)):4d}  {ev:8.2e}   "
              f"{len(act):6d}   {abs(x).max():.2e}  {float(dd.get('primal_obj')):11.4g}  {gap:.2e}")
    x_w, act_w, gap_w, dd_w = solve(tt, G_w, 0.5 * float(tt.sum()))
    assert len(act_w) == 3, act_w                  # the bean's number, reproduced
    assert gap_w > 1.0, gap_w                      # and it is not a valid solve
    assert abs(x_w).max() > 1e6, abs(x_w).max()    # it exceeds M_bound = 1e6
    print(f"""
  The 3 is reproduced exactly — and the solve that produces it is invalid:
  max|x*| = {abs(x_w).max():.4e} exceeds M_bound = 1e6, the objective of a
  MAXIMisation is {float(dd_w.get('primal_obj')):.6g}, and the duality gap is
  {gap_w:.4e} where every well-posed solve above gives < {GAP_OK:.0e}.

  This is the SAME failure mode `h6_block_selection_lp_probe.py` retracts one
  screen below (2026-08-16) for the braid sub-word basis: "max|x*| = 3.57e6
  against M_bound = 1e6 ... The 'stability across targets' was the corner not
  moving."  The retraction was applied to the sub-word half of that file and not
  to the controlled-diagnostic half, and the bean then quoted the un-retracted
  half as evidence that a dense Gram "recovers discriminating power".

  A WELL-POSED dense PSD instance gives d-1, like everything else in section 2.
  Do not quote 3-of-6.""")

    # ------------------------------------------------------------ section 5
    hdr("[5] What this closes, and what it leaves alone")

    print("""  CLOSED — the bean's named escape route.  A non-orthogonal operator basis
  does not make the LP's active set a binding multiplier.  The prior diagnosis
  (diagonal Gram => decoupling) was a correct conclusion from the wrong reason,
  and the wrong reason is what generated an escape that is not there.

  NOT TOUCHED, and still qou-brng's real target:
    * the extensive term itself (a bulk, not a surface);
    * the LP's optimal VALUE and y_0* — this is about the ACTIVE SET only;
    * the gamma-gamma-selected-word follow-up (blocked on qou-ales step 2);
    * escape classes B and D of PR #7181.""")

    print("\nPROBE OK — all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
