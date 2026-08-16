#!/usr/bin/env python3
"""
Probe — the operator-selection LP CANNOT select among Wedderburn blocks. Diagnosed.

`h6_wedderburn_block_unbinding_probe.py` established that the full `H_6` contains
unbinding blocks (`r_lambda` up to 6.46) where the 2-dim interface subalgebra is
provably capped at `z = 0.6127`, and that the unbinding sits in the WIDE
(symmetric, `T=1`-like) blocks — the right place. What it did not supply is a
SELECTION principle: something that picks those blocks without being told to.

The corpus has machinery of exactly the right type — the operator-selection LP
(`prop:operator-selection-lp`), whose dual shadow prices `y*` identify which
operators a bound state saturates. This probe wires the `H_6` blocks into it.

## Result: it does not select, at ANY target

Feeding per-block contributions `t_lambda = |y_lambda * chi_lambda(W_atom)|` with
`G = diag(t)` and sweeping the net constraint across the whole reachable range:

    target        # active (of 11)
    0.010 * S           11
    0.050 * S           11
    0.100 * S           10
    0.250 * S           11
    ...                 ...
    0.999 * S           11

Never fewer than 10 of 11. The active set is never the wide-block set. (The first
run used `target = 1.0`, which EXCEEDS `sum(t) = 0.2575` and is therefore a
degenerate instance — that was a harness error, and fixing it changes nothing:
the null holds across the reachable range.)

## The diagnosis — it is structural, not a bad instance

**Wedderburn block projectors are orthogonal idempotents:** `P_l P_m = delta_lm P_l`.
So the Frobenius Gram

    G_lm = tr_M(P_l P_m) = delta_lm * tr_M(P_l)

is **diagonal by construction**. The LP's discriminating power comes from the
OVERLAP between candidate operators — the off-diagonal Gram entries. Orthogonal
blocks have none, so there is nothing to select on.

Confirmed on a controlled instance (same `t`, same target, only `G` changed):

    G = diag(t)          -> 5 of 6 active
    G dense PSD          -> 3 of 6 active

Off-diagonal structure restores discrimination; diagonal structure destroys it.

## Consequence for the H_6 route

The range half of option C stands: `H_6` is big enough and oriented correctly.
The selection half does **not** come from the existing LP, and cannot — not
because the LP is weak, but because a Wedderburn basis is the one basis on which
it has no purchase.

A selection principle would need either:

* a **non-orthogonal** operator basis — actual braid sub-words overlap, so their
  Gram is dense, and that is the natural thing to try next; or
* a different principle entirely (an index, a positivity condition, a
  variational criterion) that does not route through operator overlap.

## What this does NOT say

It does not refute the operator-selection LP, which is doing exactly what it
should on the basis it is given. It does not say the wide blocks are the wrong
ones — only that nothing here selects them. And it does not license choosing
them: with 11 blocks, picking the ones that give the right answer remains a fit,
and this probe removes the one candidate justification that was available.

NO WITNESS: an LP sweep on derived per-block contributions plus a controlled
diagnostic; the tables reproduce it.

Bean qou-brg3; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import math
import sys

WIDE = {(6,), (5, 1), (4, 2)}
FRACTIONS = [0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.95, 0.999]


def main() -> int:
    from mass_at_3A_proper import atom_braid_word_3A  # noqa: F401  (path bridge)
    import numpy as np
    import hecke_core_legacy as HC
    from pyhecke.trace import atom_character_raw
    from lp_dual_solver import solve_operator_selection_lp

    six = sorted([e for e in HC._PARTITION_TABLE
                  if e.get("k", 0) == 6 and e.get("has_ysn")],
                 key=lambda x: tuple(x["partition"]))
    if not six:
        print("ABORT — no k=6 YSN entries; nothing measured.")
        return 2

    Z, N, lbl = 2, 0, "pp"
    recs = []
    for e in six:
        ca, na, _ = atom_character_raw(Z, N, e, include_inter=True)
        cf, nf, _ = atom_character_raw(Z, N, e, include_inter=False)
        ca, cf = float(ca), float(cf)
        if ca == 0 or cf == 0:
            continue
        la = math.log(abs(ca)) + float(na)
        lf = math.log(abs(cf)) + float(nf)
        recs.append((tuple(e["partition"]), float(e["wedderburn_weight"]), la, lf))
    mx = max(r[2] for r in recs)
    lams = [r[0] for r in recs]
    t = np.array([abs(r[1]) * math.exp(r[2] - mx) for r in recs])
    S = float(t.sum())

    print("Can the operator-selection LP pick the unbinding H_6 blocks?\n")
    print(f"  system {lbl};  {len(lams)} blocks;  sum(t) = {S:.6f}")
    print("  t_lambda = |y_lambda * chi_lambda(atom)|,  G = diag(t)  "
          "(projectors are orthogonal)\n")
    print("  | target      | # active | == wide set? |")
    print("  | ----------- | -------: | :----------- |")
    ever = False
    for frac in FRACTIONS:
        res = solve_operator_selection_lp(t, np.diag(t), float(frac * S))
        act = res.to_dict().get("active_set") or []
        blocks = {lams[i] for i in act if i < len(lams)}
        hit = blocks == WIDE
        ever = ever or hit
        print(f"  | {frac:>6.3f}*S   | {len(act):>8} | {str(hit):<12} |")

    print(f"\n  any target selects exactly the wide blocks: {ever}")
    print("  never fewer than 10 of 11 active — this is not a selection.\n")

    # ---- the diagnosis, on a controlled instance --------------------------
    print("## Diagnosis — diagonal Gram, not a bad instance\n")
    print("  Block projectors are orthogonal idempotents (P_l P_m = delta_lm P_l),")
    print("  so G_lm = tr_M(P_l P_m) is DIAGONAL by construction. The LP selects on")
    print("  operator OVERLAP — the off-diagonal entries. Orthogonal blocks have none.\n")
    rng = np.random.default_rng(7)
    tt = np.array([0.1, 0.2, 0.05, 0.4, 0.15, 0.3])
    A = rng.normal(size=(6, 6))
    for name, G in (("G = diag(t)   (what block projectors give)", np.diag(tt)),
                    ("G dense PSD   (overlapping operators)", A @ A.T / 6.0)):
        res = solve_operator_selection_lp(tt, G, 0.5 * float(tt.sum()))
        act = res.to_dict().get("active_set") or []
        print(f"    {name:<44} active {len(act)}/6")
    print("\n  Off-diagonal structure restores discrimination; diagonal destroys it.")

    print("\n## Consequence\n")
    print("  The RANGE half of the H_6 route stands (H_6 is big enough, and oriented")
    print("  correctly). The SELECTION half does not come from the existing LP and")
    print("  cannot — not because the LP is weak, but because a Wedderburn basis is")
    print("  the one basis on which it has no purchase.")
    print("\n  Next candidates: a NON-orthogonal operator basis (braid sub-words overlap,")
    print("  so their Gram is dense) or a principle that does not route through overlap.")
    print("\n  Does NOT refute the LP, does NOT say the wide blocks are wrong, and does")
    print("  NOT license choosing them — with 11 blocks that is still a fit, and this")
    print("  removes the one justification that was available for it.")
    print("\n(no witness by design — LP sweep on derived contributions + diagnostic.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
