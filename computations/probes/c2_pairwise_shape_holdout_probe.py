#!/usr/bin/env python3
"""c2_pairwise_shape_holdout_probe.py — does c₂ have c₁'s shape? A leave-one-out test. (qou-qqm4)

THE QUESTION. `c₁` has a closed form on the canonical word (PR #6920):

    c₁(Z,N)  =  u · (2^(−A−1) − 2^(−2A))  −  4·D · 2^(−2A),
                u = (Z·S_p + N·S_n)/2 = 3Z − 2N,     D = I_pp − I_nn

— i.e. at fixed `A` it is **affine in the two coordinates `(u, D)`**: a per-nucleon content term
and an interface term, with no other species dependence. This probe asks whether `c₂` is affine in
the same two coordinates at fixed `A`. It does **not** ask what the `A`-dependence is.

WHY A LEAVE-ONE-OUT AT A = 3, AND NOT A FIT ON THE SIX RECORDED WORDS. An affine form in `(u, D)`
has three parameters, so three points determine it and cannot test it. The six words already
recorded (`pp, pn, nn, T, ³He, ⁴He`) do not fix this either:

- `A = 2` is **degenerate**. Its three species sit at `(u,D) = (6,1), (1,0), (−4,−1)`, and
  `(pp + nn)/2` is exactly `pn`'s coordinates — the design matrix has rank 2, so one parameter
  stays free whatever the values are. Three points, two constraints.
- `A = 3` supplies only two of its four species (`T`, `³He`) among the recorded six.
- `A = 4` supplies one.

So the recorded set has **no `A` at which the form is over-determined**, and any "fit" on it is
unfalsifiable. `A = 3` has four species — `3p, T, ³He, 3n` at `(9,2), (−1,−1), (4,1), (−6,−2)` —
and its design matrix is non-singular (the `1,2,3` minor is `−5`). Four points, three parameters:
fit on three, **predict the fourth**, four ways round. Every point is held out once.

    A PASS is a real result: a two-coordinate affine form survives a held-out species.
    A FAIL is equally a result and is the more likely one — `c₂` has letter-PAIR terms
    (`|S| = 2`) that `c₁` does not, and there is no argument that a pair sum stays affine
    in the same coordinates. Nothing here is tuned either way.

WHAT IS TESTED. Three columns independently, each by the same leave-one-out:
`c₂` itself, and the insertion classes `|S| = 1` and `|S| = 2` separately (the `|S| = 0` class is
constant at fixed `A` — measured, see below — so it is reported and not tested).

THE ONE THING ALREADY ESTABLISHED, and it is not a fit: **the `|S| = 0` class is species-blind.**
From the refreshed `[◇]` witness, all three `A = 2` words give `0`, both `A = 3` words give `5/32`,
and `⁴He` gives `11/64` — six points collapsing to three with no parameter chosen. That is the
second-order shadow of `c₀ = 2^(−A)(1 − 2^(−O))`, which likewise sees only the interface pattern.
The species dependence of `c₂` therefore lives entirely in `|S| = 1` and `|S| = 2`.

## MEASURED RESULT (2026-09-06)

    c₁       CONTROL  4/4 HIT   — and all four training triples return the SAME (a,b,c)
                                  = (3/64, −1/16, 0), which IS the derived closed form at
                                  A = 3. The harness reproduces a known answer.
    |S| = 1           4/4 HIT   — same (a,b,c) = (3/128, −1/32, 61/64) from every triple.
    |S| = 2           4/4 MISS  — every triple gives a different (a,b,c).
    c₂                4/4 MISS  — inherited from |S| = 2.

**So the second order splits cleanly: the single-insertion class keeps `c₁`'s shape, the
letter-pair class breaks it, and that is the whole of why `c₂` has no affine form.** This is the
outcome the docstring above called the more likely one; it is recorded as a finding, not a
disappointment. Any `c₂` closed form must carry a genuinely new `(Z,N)` structure for `|S| = 2` —
looking for an affine one is now excluded at `A = 3` (scope-(a): at this `A`, in these
coordinates).

### And the `|S| = 1` fit is not merely affine — it is `c₁` itself, halved

The fitted `(a, b) = (3/128, −1/32)` is **exactly half** of `c₁`'s `(3/64, −1/16)`. Testing that
against every species already measured, at three values of `A`:

    |S| = 1  −  c₁/2  =  k(A),   species-independent

    A = 2   pp, pn, nn            all  13/16  = 13/2⁴
    A = 3   3p, T, ³He, 3n        all  61/64  = 61/2⁶
    A = 4   ⁴He                        193/256 = 193/2⁸

Eight species, three constants — five degrees of freedom of test, and it holds exactly on all
eight. The `A = 2` row is worth noting: those three species are rank-deficient for an affine *fit*,
but subtracting `c₁/2` and finding the same residual three times is a genuine check even there.

🛑 **The `A`-DEPENDENCE OF `k` IS A ZERO-DOF FIT AND IS UNTESTED.** `m(A) = (3/8)4^A + (15/2)2^A −
23` reproduces `13, 61, 193` — three parameters on three points, so it *cannot* fail, and it is
recorded here as a candidate to be shot at, **not** as a result. The test is one species at
`A = 5` (`n = 15`, ~45 min for the pair of words), which predicts `k(5) = 663/2¹⁰`. Until that
runs, quote the species-independence of `k` (which is measured) and not the formula for it.

SCOPE — (a) scope-limited. One `A` for the leave-one-out, three for the `k` relation, exact
`Fraction` arithmetic through the `[◇]` expansion. The MISS is scope-(a): it says an affine form in
these two coordinates fails at `A = 3`, not that no closed form exists. No `q` is evaluated, no
float, no witness written, nothing wired, no Lean.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
import time
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

_spec = importlib.util.spec_from_file_location(
    "diag", _HERE / "c2_diagonal_insertion_expansion_probe.py")
_D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_D)

# A = 3, all four species. Names are the framework's where it has one.
SPECIES = (("3p", 3, 0), ("T", 1, 2), ("3He", 2, 1), ("3n", 0, 3))


def coords(Z: int, N: int) -> tuple[int, int]:
    """`(u, D)` — the two coordinates c₁'s closed form is affine in.

    `u = 3Z − 2N` is the per-nucleon deletion-sum at the canonical word's `(S_p, S_n) = (6, −4)`;
    `D = I_pp − I_nn` counts the interfaces of the ordering `p…p n…n`, which has `Z−1` pp
    interfaces and `N−1` nn interfaces when both species are present, and `A−1` of one kind when
    only one is.
    """
    order = ["p"] * Z + ["n"] * N
    ipp = sum(1 for a, b in zip(order, order[1:]) if a == b == "p")
    inn = sum(1 for a, b in zip(order, order[1:]) if a == b == "n")
    return 3 * Z - 2 * N, ipp - inn


def solve_affine(pts):
    """Exact solve of `a·u + b·D + c = y` on three points. Returns None if singular."""
    (u1, d1, y1), (u2, d2, y2), (u3, d3, y3) = pts
    det = (u1 * (d2 - d3) - d1 * (u2 - u3) + (u2 * d3 - u3 * d2))
    if det == 0:
        return None
    a = (y1 * (d2 - d3) - d1 * (y2 - y3) + (y2 * d3 - y3 * d2)) / F(det)
    b = (u1 * (y2 - y3) - y1 * (u2 - u3) + (u2 * y3 - u3 * y2)) / F(det)
    c = (u1 * (d2 * y3 - d3 * y2) - d1 * (u2 * y3 - u3 * y2)
         + y1 * (u2 * d3 - u3 * d2)) / F(det)
    return a, b, c


def leave_one_out(rows, key, label):
    """Fit the affine form on every 3-subset and predict the held-out 4th. Returns all-passed."""
    print(f"\n  ── {label} ──")
    ok = True
    for i in range(len(rows)):
        train = [rows[j] for j in range(len(rows)) if j != i]
        held = rows[i]
        sol = solve_affine([(r["u"], r["D"], r[key]) for r in train])
        if sol is None:
            print(f"    hold out {held['name']:<5} SINGULAR on the training triple — no prediction")
            ok = False
            continue
        a, b, c = sol
        pred = a * held["u"] + b * held["D"] + c
        hit = (pred == held[key])
        ok = ok and hit
        print(f"    hold out {held['name']:<5} fit (a,b,c) = ({a}, {b}, {c})"
              f"   predict {pred}   actual {held[key]}   {'HIT' if hit else 'MISS'}")
    print(f"    ⇒ {'4/4 — the affine shape SURVIVES a held-out species at A = 3.' if ok else 'MISS — c₂ is NOT affine in (u, D) at fixed A. That is the finding.'}")
    return ok


def c1_closed(u: int, D: int, A: int) -> F:
    """PR #6920's derived closed form. Used as the CONTROL's known answer and in the k relation."""
    return F(u) * (F(1, 2) ** (A + 1) - F(1, 2) ** (2 * A)) - 4 * F(D) * F(1, 2) ** (2 * A)


def measure(Z: int, N: int) -> dict:
    """One species: c₁, c₂ and the |S| = 0,1,2 split of c₂, exact."""
    u, D = coords(Z, N)
    cf, cls_f = _D.trace_expansion(Z, N, False, 2)
    ca, cls_a = _D.trace_expansion(Z, N, True, 2)
    d = [x - y for x, y in zip(cf, ca)]
    cls = {s: [x - y for x, y in zip(cls_f[s], cls_a[s])] for s in cls_f}
    by = {s: cls[s][1] + cls[s][2] for s in cls}
    return {"Z": Z, "N": N, "A": Z + N, "u": u, "D": D, "c1": d[1], "c2": d[1] + d[2],
            "S0": by[0], "S1": by[1], "S2": by[2]}


def k_relation(rows) -> bool:
    """`|S| = 1 − c₁/2` must be one constant per A, independent of species. Prints the table."""
    print("\n  ── |S| = 1 − c₁/2 : one constant per A, species-independent? ──")
    by_A = {}
    ok = True
    for r in rows:
        by_A.setdefault(r["A"], []).append((r["name"], r["S1"] - r["c1"] / 2))
    for A in sorted(by_A):
        vals = by_A[A]
        distinct = {v for _, v in vals}
        good = len(distinct) == 1
        ok = ok and good
        names = ", ".join(n for n, _ in vals)
        shown = sorted(str(v) for v in distinct)
        extra = (f"  = {list(distinct)[0] * 2 ** (2 * A)}/2^{2 * A}" if good else "")
        print(f"    A = {A}  ({len(vals)} species: {names:<22}) {shown}{extra}"
              f"   {'constant' if good else 'NOT CONSTANT — the relation is refuted'}")
    print(f"    ⇒ {'species-independent at every A measured — |S|=1 = c₁/2 + k(A).' if ok else 'REFUTED — do not quote the k(A) relation.'}")
    print("    🛑 The A-DEPENDENCE of k is a separate question and is NOT tested here. The candidate")
    print("    m(A) = (3/8)4^A + (15/2)2^A − 23 fits 13, 61, 193 with three parameters on three")
    print("    points — it cannot fail. It predicts k(5) = 663/2^10; that is the test.")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--with-a4", action="store_true",
                    help="add ⁴He to the k-relation table (n = 12, ~4 min)")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    t0 = time.time()

    print("=" * 78)
    print("  Is c₂ affine in (u, D) at fixed A, as c₁ is?  Leave-one-out at A = 3.")
    print("=" * 78)
    print("  Four species, three parameters: fit on three, predict the fourth, four ways.")
    print("  The six recorded words CANNOT test this — A=2 is rank-deficient (pp+nn ≡ 2·pn in")
    print("  (u,D)), A=3 contributes only T and ³He, A=4 only ⁴He. Hence 3p and 3n.\n")

    rows = []
    for name, Z, N in SPECIES:
        r = measure(Z, N)
        r["name"] = name
        rows.append(r)
        print(f"  {name:<5} (Z={Z},N={N})  u={r['u']:>3}  D={r['D']:>3}   "
              f"c₁={str(r['c1']):>9}  c₂={str(r['c2']):>10}   "
              f"|S|=0 {str(r['S0']):>6}  |S|=1 {str(r['S1']):>10}  "
              f"|S|=2 {str(r['S2']):>10}   [{time.time()-t0:5.1f}s]")

    s0 = {r["S0"] for r in rows}
    print(f"\n  |S| = 0 across all four A = 3 species: {sorted(str(x) for x in s0)}"
          f"  →  {'species-blind, as at A = 2 and A = 4' if len(s0) == 1 else 'NOT constant — the species-blindness claim is refuted at A = 3'}")

    # c₁ is the CONTROL: its closed form is already derived, so it must pass. A c₁ miss means the
    # harness is wrong, not that c₁'s form is — check that before reading any c₂ verdict.
    ctrl = leave_one_out(rows, "c1", "c₁  — CONTROL, must pass (its closed form is derived)")
    if not ctrl:
        print("\n  🛑 THE CONTROL FAILED. The coordinates or the solver are wrong; the c₂ verdicts")
        print("  below say nothing. Do not read them.")

    r2 = leave_one_out(rows, "c2", "c₂  — the question")
    r1 = leave_one_out(rows, "S1", "|S| = 1  (single insertions)")
    rr = leave_one_out(rows, "S2", "|S| = 2  (letter pairs)")

    # The k relation spans A, so it needs the other sizes. A=2 is three species at n=6 (instant);
    # ⁴He is n=12 and opt-in. Both are recomputed here, never read from a witness.
    krows = list(rows)
    for nm, (zz, nn_) in (("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2))):
        r = measure(zz, nn_)
        r["name"] = nm
        krows.append(r)
    if args.with_a4:
        print(f"\n  ⁴He (n = 12) for the k table — this is the slow one …")
        r = measure(2, 2)
        r["name"] = "4He"
        krows.append(r)
    kok = k_relation(krows)

    print(f"\n  SUMMARY at A = 3:  c₁ {'ok' if ctrl else 'BROKEN HARNESS'}   "
          f"c₂ {'affine' if r2 else 'NOT affine'}   "
          f"|S|=1 {'affine' if r1 else 'NOT affine'}   |S|=2 {'affine' if rr else 'NOT affine'}"
          f"   k(A) {'species-independent' if kok else 'REFUTED'}")
    print("\n  Scope. The leave-one-out is at ONE value of A: the |S|=1 pass says that shape")
    print("  survives a held-out species at A = 3, and the |S|=2 MISS is scope-(a) — an affine")
    print("  form in THESE two coordinates fails at THIS A, which is not 'no closed form exists'.")
    if not args.with_a4:
        print("  The k table above covers A = 2 and 3 only; --with-a4 adds ⁴He (n = 12, ~4 min),")
        print("  which gives 193/2^8. The A-dependence of k is untested either way — that needs")
        print("  A = 5 (n = 15).")
    print(f"\n  ({time.time()-t0:.1f}s)")
    # Exit 1 only if a CONTROL fails — a c₂/|S|=2 MISS is the finding, not an error.
    return 0 if (ctrl and kok) else 1


if __name__ == "__main__":
    sys.exit(main())
