#!/usr/bin/env python3
"""magnus_a4_crossing_sparse_probe.py — is the hook/two-row reversal a BOUNDARY effect of the
two-row column, or a genuine interior crossing? A=4 via a sparse sector route. (qou-o6ov)

THE QUESTION #6677 LEFT OPEN. The per-dim majorant satisfies hook(b) > two-row(b) at small b and
two-row(b) > hook(b) at large b, at both sizes measured — the relation CHANGES SIGN. But in both
cases the reversal sat at b = ⌊n/2⌋, which is the LAST b at which a two-row shape exists at all
(there (n−b,b) is as square as it can be). Two readings fit two data points:

    (i)  BOUNDARY  — the two-row column simply ends before the hook can overtake it again, and the
                     "reversal" is an artifact of where the column stops;
    (ii) INTERIOR  — the two curves genuinely cross, and it is coincidence that the crossing has
                     landed on the last comparable b twice.

They are separated by a third size. The ratio trajectory already argues for (ii) and the probe
reports it as the primary evidence, because it does not require reaching the last b:

    A=2:  ratio hook/two-row = 1.000, 1.689, 0.882            (b = 1,2,3;  ⌊n/2⌋ = 3)
    A=3:                     = 1.000, 1.245, 1.115, 0.592     (b = 1..4;   ⌊n/2⌋ = 4)

The ratio is 1 at b=1 (forced — (n−1,1) IS both shapes), rises, then falls through 1. If at A=4 it
falls below 1 STRICTLY BEFORE b = ⌊12/2⌋ = 6, reading (i) is dead and no b=6 computation is needed.
Only if it is still above 1 at b=5 does the last sector have to be reached.

WHY A SPARSE ROUTE IS NEEDED, and it is not an optimisation. #6587's sector code stores each
generator as a DENSE D×D mp.matrix and forms ρ by D×D×D products. At A=4 the largest sector is
C(12,6) = 924 and the word has L = 47 letters, so that is ~10¹⁰ mpf multiplications — not slow,
infeasible. But Ř acts on two adjacent strands, so each generator has at most 2 non-zeros per
column; applying it to a vector is O(2D). Computing ‖X|_{W_k}‖_F² = Σ_j ‖X e_j‖² column by column
costs (4(ngen−1) + L) sparse mat-vecs per column instead, which is ~10⁸ — large but reachable.

THE GATE. A rewritten kernel that is only ever run where the old one cannot go is unfalsifiable, so
the sparse route is checked against the DENSE #6587 implementation at A=2 and A=3, every k, before
any A=4 number is printed. It must agree to the arithmetic; a mismatch stops the probe.

PRECISION. mp.dps defaults to 65 here, the corpus compute default (`_precision.py`), rather than
the 140 the smaller probes in this arc used — at ~10⁸ operations the difference is hours. This is
NOT a float64 relaxation: every quantity is mpf end to end. To show the choice does not move the
answer, `--dps-check` re-runs A=3 at both 65 and 140 and reports the agreement.

scope-(a); NO-FLOAT64. No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import math
import os
import sys
import time
from itertools import combinations

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_gauge_hook_closed_form_probe import reflection_generators  # noqa: E402
from magnus_hook_majorant_closed_form_probe import burau_closed_form  # noqa: E402
# Imported at MODULE level deliberately — see _assert_dps below. Every probe in this arc sets
# mp.mp.dps at its own module top, so importing one INSIDE a function silently re-sets global
# precision mid-run. Keeping every such import up here means all of them fire before main() pins
# dps, instead of one of them firing after.
from magnus_tworow_majorant_sector_probe import sector_majorant as _dense_sector_majorant  # noqa: E402

_WANT_DPS = None


def _assert_dps(where):
    """Fail loudly if global precision is not what this run asked for.

    THE TRAP THIS EXISTS FOR, measured 2026-09-05. `mp.mp.dps` is global mutable state, and every
    probe in this arc assigns it at module scope. A function-local (deferred) import of any of them
    therefore RE-SETS the precision of a run already in progress, silently. This probe's `--dps 65`
    was a no-op for exactly that reason: the dense-vs-sparse gate imported #6587 inside a function,
    which snapped dps back to 140 — visible only because the gate then agreed to 1e-140, which 65
    digits cannot produce.

    Note what does NOT protect you: every probe here (this one included) carries the comment "pin
    explicitly (do not rely on an imported side effect)" beside its own `mp.mp.dps = …`. That guards
    against INHERITING a wrong precision at import time. It does nothing about an import that lands
    LATER and changes it underneath you. The assertion is the part that actually holds.
    """
    if _WANT_DPS is not None and mp.mp.dps != _WANT_DPS:
        raise RuntimeError(
            f"mp.mp.dps is {mp.mp.dps}, expected {_WANT_DPS}, at {where} — something re-set global "
            f"precision mid-run (almost certainly a deferred import of a probe that pins dps at "
            f"module scope). Refusing to report numbers computed at an unrequested precision.")


def sector_basis(n, k):
    """n-bit states with exactly k up-spins; strand j is bit (n−1−j). Same convention as #6525."""
    states = sorted(sum(1 << (n - 1 - j) for j in ups) for ups in combinations(range(n), k))
    return states, {s: i for i, s in enumerate(states)}


def sparse_gen(n, i, q, states, index):
    """Ř on strands (i, i+1) restricted to the sector, as columns[col] = [(row, coeff), ...].

    Ř in the pair basis: 00 → q·00, 11 → q·11, 01 → (q−q⁻¹)·01 + 10, 10 → 01. Identical to
    #6525's `sector_R`, stored by column instead of densely — at most two entries per column.
    """
    qi = 1 / q
    bi, bj = n - 1 - i, n - 2 - i
    cols = []
    for s in states:
        a, b = (s >> bi) & 1, (s >> bj) & 1
        if a == b:
            cols.append(((index[s], q),))
        elif a == 0 and b == 1:
            t = s ^ (1 << bi) ^ (1 << bj)
            cols.append(((index[s], q - qi), (index[t], mp.mpf(1))))
        else:
            t = s ^ (1 << bi) ^ (1 << bj)
            cols.append(((index[t], mp.mpf(1)),))
    return cols


def apply_gen(cols, v, D):
    """w = M·v for M given by column lists. Skips zero entries — v is sparse early on."""
    w = [mp.mpf(0)] * D
    for col in range(D):
        x = v[col]
        if x:
            for row, c in cols[col]:
                w[row] += c * x
    return w


def sector_majorant_sparse(n, k, gens, q, progress=None):
    """‖X|_{W_k}‖_F² for X = ρ·Ω₂^P, column by column, never forming a dense product."""
    _assert_dps(f"sector_majorant_sparse(n={n}, k={k})")
    states, index = sector_basis(n, k)
    D = len(states)
    ngen = max(gens) + 1
    G = [sparse_gen(n, i, q, states, index) for i in range(ngen)]
    c = 4 / (q + 1 / q) ** 2
    rev = list(reversed(gens))          # ρ = R[g0]···R[gL-1]  ⇒ apply gL-1 first
    total = mp.mpf(0)
    t0 = time.time()
    for j in range(D):
        e = [mp.mpf(0)] * D
        e[j] = mp.mpf(1)
        # Ω₂^P e_j = c·Σ_a (R_a R_{a+1} − R_{a+1} R_a) e_j
        acc = [mp.mpf(0)] * D
        for a in range(ngen - 1):
            u = apply_gen(G[a], apply_gen(G[a + 1], e, D), D)
            w = apply_gen(G[a + 1], apply_gen(G[a], e, D), D)
            for r in range(D):
                acc[r] += u[r] - w[r]
        v = [c * x for x in acc]
        for g in rev:                    # ρ·(Ω₂ e_j)
            v = apply_gen(G[g], v, D)
        for x in v:
            if x:
                total += x * x           # Ř is real symmetric here; verified by the caller's gate
        if progress and (j + 1) % max(1, D // 10) == 0:
            el = time.time() - t0
            print(f"      [k={k}] col {j+1}/{D}  {el:.0f}s elapsed, "
                  f"ETA {el*(D-j-1)/(j+1):.0f}s", flush=True)
    return total, D


def gate_against_dense(A, q):
    """The sparse kernel must reproduce #6587's DENSE sector_majorant, every k, before A=4 runs."""
    dense = _dense_sector_majorant       # module-level import; see _assert_dps
    _assert_dps(f"gate_against_dense(A={A})")
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    worst = mp.mpf(0)
    for k in range(0, n // 2 + 1):
        d, _dW, _asym = dense(n, k, gens, q)
        s, _D = sector_majorant_sparse(n, k, gens, q)
        den = abs(mp.re(d)) if abs(mp.re(d)) > mp.mpf(10) ** -60 else mp.mpf(1)
        worst = max(worst, abs(mp.re(d) - s) / den)
    return worst


def columns(A, max_k, progress=False):
    """(hook per-dim by b, two-row per-dim by b) — hook from the Burau closed form, two-row sparse."""
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    L = len(gens)
    sV, _dimV = reflection_generators(n, ngen, q)
    hook = {b: burau_closed_form(b, gens, q, ngen, sV, L) / math.comb(n - 1, b) for b in range(n)}
    trow, prev = {}, mp.mpf(0)
    for b in range(0, min(max_k, n // 2) + 1):
        sec, _D = sector_majorant_sparse(n, b, gens, q, progress=progress)
        d = math.comb(n, b) - (math.comb(n, b - 1) if b > 0 else 0)
        trow[b] = (sec - prev) / d if d else None
        prev = sec
    return hook, trow, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=4)
    ap.add_argument("--max-k", type=int, default=4, help="highest two-row k to compute")
    ap.add_argument("--dps", type=int, default=65, help="corpus compute default; NOT float64")
    ap.add_argument("--dps-check", action="store_true",
                    help="re-run A=3 at 65 and 140 to show the dps choice does not move the answer")
    ap.add_argument("--progress", action="store_true")
    args = ap.parse_args()
    global _WANT_DPS

    if args.dps_check:
        vals = {}
        for d in (65, 140):
            _WANT_DPS = d
            mp.mp.dps = d
            h, t, _n = columns(3, 4)
            vals[d] = [t[b] for b in sorted(t) if t[b] is not None and b > 0]
        rel = max(abs(a - b) / abs(a) for a, b in zip(vals[65], vals[140]) if a)
        print(f"[dps] A=3 two-row per-dim at dps 65 vs 140: worst |Δ_rel| = {mp.nstr(rel,3)}")
        print(f"[dps] ⇒ the dps choice {'does NOT move' if rel < mp.mpf(10)**-40 else 'MOVES'} "
              f"the answer at this size.\n")

    _WANT_DPS = args.dps
    mp.mp.dps = args.dps
    q = base.Q0

    # ---- GATE: the sparse kernel vs the dense one, at the sizes where both can run ----
    print(f"[gate] sparse sector kernel vs #6587's DENSE sector_majorant (mp.dps = {args.dps}, "
          f"asserted at every compute entry — see _assert_dps)")
    ok = True
    for Ac in (2, 3):
        w = gate_against_dense(Ac, q)
        good = w < mp.mpf(10) ** -40
        ok = ok and good
        print(f"  A={Ac}: worst |Δ_rel| over all k = {mp.nstr(w,3)}   {'✓' if good else '✗'}")
    if not ok:
        print("\n  ⇒ GATE FAILED. The sparse kernel does not reproduce the dense one, so no A=4")
        print("    number is reportable. A rewritten kernel run only where the old one cannot go")
        print("    is unfalsifiable — stopping rather than printing it.")
        return
    print("  ⇒ gate passed; the sparse kernel is the dense one, cheaper.\n")

    hook, trow, n = columns(args.A, args.max_k, progress=args.progress)
    half = n // 2
    print(f"[A={args.A}] n={n}; hook/two-row per-dim ratio.  ⌊n/2⌋ = {half} is the LAST b with a")
    print(f"[A={args.A}] two-row at all. Computed up to k={min(args.max_k, half)}.\n")
    # b ≤ 1 is EXCLUDED from the crossing test, and this is not fastidiousness. At b=1 the hook
    # (n−1,1) and the two-row (n−1,1) are THE SAME PARTITION, so the ratio is 1 by construction —
    # it is the cross-check between the two reductions, not a data point about their ordering.
    # Computed by two different routes it differs by an ulp, and a bare `r < 1` then reports a
    # "crossing" at b=1 from a 1e-65 rounding difference. It did exactly that before this guard,
    # and printed "BOUNDARY refuted" on the strength of it.
    tol = mp.mpf(10) ** -(mp.mp.dps // 2)
    print("    b   hook per-dim     two-row per-dim   ratio hook/two-row   crossed 1?")
    crossed = None
    for b in sorted(trow):
        if b == 0 or trow[b] is None or trow[b] <= 0:
            continue
        r = hook[b] / trow[b]
        same_shape = (b == 1)                       # (n−1,1) is both a hook and a two-row
        is_cross = (not same_shape) and r < 1 - tol
        if crossed is None and is_cross:
            crossed = b
        note = "(same shape — forced 1)" if same_shape else ("← YES" if is_cross else "")
        print(f"   {b:>2}   {mp.nstr(hook[b],8):>14}   {mp.nstr(trow[b],8):>15}   "
              f"{mp.nstr(r,7):>18}   {note}")
    print()
    if crossed is None:
        print(f"  ratio still > 1 at every b computed (up to {min(args.max_k, half)}). This does NOT")
        print(f"  decide between BOUNDARY and INTERIOR — the crossing may be at a higher b. Raise")
        print(f"  --max-k (the cost grows with C(n,k); the last one is C({n},{half}) = "
              f"{math.comb(n, half)}).")
    elif crossed < half:
        print(f"  ⇒ the ratio crosses 1 at b = {crossed}, STRICTLY BEFORE the last comparable")
        print(f"    b = ⌊n/2⌋ = {half}. Reading (i) BOUNDARY is REFUTED: the reversal is a genuine")
        print("    interior crossing of two decaying curves, and its landing on the last b at A=2")
        print("    and A=3 was coincidence of those sizes.")
    else:
        print(f"  ⇒ the ratio crosses 1 exactly at b = {half} = ⌊n/2⌋, the last comparable b — a")
        print("    THIRD size with the reversal at the boundary. That is consistent with reading")
        print("    (i) BOUNDARY and does not yet prove it; three points on a boundary could still")
        print("    be an interior crossing that tracks n/2. Say which, do not merge the two.")


if __name__ == "__main__":
    main()
