#!/usr/bin/env python3
"""c2_pair_class_decomposition_probe.py — WHICH letter pairs break the affine shape? (qou-qqm4)

WHERE THIS SITS. `c2_pairwise_shape_holdout_probe` established, by leave-one-out at `A = 3` against
a passing `c₁` control, that `c₂` is **not** affine in `(u, D) = (3Z − 2N, I_pp − I_nn)` and that the
break is entirely in the `|S| = 2` insertion class — the single-insertion class `|S| = 1` is affine,
and is in fact `c₁/2 + k(A)`. This probe opens `|S| = 2` up one level further.

`|S| = 2` is a sum over **ordered letter pairs**, and the letters of the atom word fall into two
kinds with different reach: a **nucleon** letter (generator `g` with `g % 3 ∈ {0,1}`, acting inside
nucleon `g // 3`'s own three strands) and an **interface** letter (`g % 3 == 2`, the single letter
coupling nucleons `g//3` and `g//3 + 1`). So every pair is exactly one of four classes:

    intra    both letters in the SAME nucleon
    cross    two letters in DIFFERENT nucleons
    n-if     one nucleon letter, one interface letter
    if-if    both interface letters

**Why this is the useful cut.** The classes have different `(Z,N)` scaling by construction — `intra`
is a per-nucleon sum (linear in `A`), `cross` is a sum over nucleon pairs (quadratic), `n-if` and
`if-if` are carried by the `A − 1` interfaces. If one class alone is non-affine, that localises what
a closed form has to supply and says which combinatorics to count. Nothing here is fitted: the class
of a pair is read off its two generators.

**And it is also an independent recomputation.** The four class contributions must sum to the
`|S| = 2` value the `[◇]` witness records, on every word — a cross-check of that witness by a
different accumulation.

## MEASURED (2026-09-06) — exact, and the four classes sum to `[◇]`'s `|S| = 2` on **7/7** words

    case   (Z,N)    intra     cross     n-if    if-if      sum = [◇]
    pp     (2,0)     1/2      9/32      −5/8       0         5/32
    pn     (1,1)       0     −3/16       1/8       0        −1/16
    nn     (0,2)    −1/2       1/8      −3/8       0         −3/4
    3p     (3,0)    9/16    81/128      −1/2    −1/8       73/128
    T      (1,2)   −3/16     −3/16      1/32       0       −11/32
    3He    (2,1)    3/16    −9/128     −1/16       0        7/128
    3n     (0,3)   −9/16      9/32     −5/16    −1/8       −23/32

That column agreement is an **independent recomputation** of the `[◇]` witness's `|S| = 2` values by
a different accumulation, not merely a bookkeeping identity.

**Per-class leave-one-out at `A = 3`** — the same test `c₂` failed, one level down:

    intra   AFFINE — 4/4
    cross   NOT affine — 0/4
    n-if    NOT affine — 0/4
    if-if   NOT affine — 0/4

**So the non-affinity is NOT localised to one class** — three of four break it. That is a weaker
answer than the question hoped for, and it is the answer.

### Two class shapes, stated from the table and then checked

- **`intra = (Z − N)·κ(A)`**, with `κ(2) = 1/4`, `κ(3) = 3/16`. Seven species, two constants —
  **five degrees of freedom** of test, exact on all seven, including the `Z = N` species where it
  requires (and gets) exactly `0`. `Z − N` is itself affine in `(u, D)`, which is *why* this class
  passes the leave-one-out.
- **`if-if = −(1/8)·[C(I_pp,2) + C(I_nn,2)]`** — a count of the ways to choose two interfaces **of
  the same kind**. It is `−1/8` for `3p` (two `pp` interfaces) and `3n` (two `nn`), and `0` for `T`
  and `³He`, whose two interfaces are unlike. 🛑 **Read its dof honestly:** at `A = 2` the count is
  `0` for all three species and the class is `0`, so those rows are consistent but carry no
  information; the content is four `A = 3` species against **one** coefficient. What makes it worth
  recording is the *shape*: a like-interface **pair** count is quadratic in `(I_pp, I_nn)`, so no
  affine form in `D` can reach it — a mechanism for this class's MISS rather than a fit to it.

`cross` and `n-if` are left unmodelled on purpose. `cross` runs over pairs of *distinct nucleons*, so
it should be quadratic in content; a full quadratic in `(u, D)` is six parameters, and `A = 5` has
exactly six species, so it is **unfalsifiable at every reachable `A`** (`A = 6` is `n = 18`, out of
reach). Fitting one would be exactly the move this arc has been burned by. Deriving it means counting
pair types, which is what this decomposition is groundwork for.

WHAT THIS IS NOT. It does not derive a closed form for `c₂`. Four classes against four species at
`A = 3` leaves no room for a *second* held-out check per class, so the `intra` AFFINE verdict is one
`A`'s worth of evidence — the `(Z − N)·κ(A)` shape above is the stronger statement about that class,
because it spans two `A` with spare dof.

SCOPE — (a) scope-limited. Exact `Fraction`s. Cost `2^n · C(L,2)`, so `A = 2, 3` are instant and
`A = 4` is minutes. No `q` evaluated, no float, no witness written, nothing wired, no Lean.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
import time
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "diag", _HERE / "c2_diagonal_insertion_expansion_probe.py")
_D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_D)

CLASSES = ("intra", "cross", "n-if", "if-if")


def letter_site(g: int):
    """`('n', j)` for a letter inside nucleon `j`; `('i', j)` for the interface after nucleon `j`.

    A nucleon owns strands `3j … 3j+2`, hence generators `3j` and `3j+1`; generator `3j+2` is the
    single letter straddling nucleons `j` and `j+1`.
    """
    return ("i", g // 3) if g % 3 == 2 else ("n", g // 3)


def pair_class(ga: int, gb: int) -> str:
    (ka, ja), (kb, jb) = letter_site(ga), letter_site(gb)
    if ka == "i" and kb == "i":
        return "if-if"
    if ka == "i" or kb == "i":
        return "n-if"
    return "intra" if ja == jb else "cross"


def s2_by_pair_class(Z: int, N: int, include_inter: bool, *, log=None) -> dict:
    """`[ε²]` of the normalised `|S| = 2` class, split by pair class. Exact.

    Mirrors `[◇]`'s own accumulation — same propagation order, same pattern scalars — but keys the
    accumulator on the pair's class instead of on `|S|`. The `K_b` factor and the normaliser both
    contribute only their `ε⁰` parts here, since the two `Δ`s already carry both powers of `ε`;
    they are kept as full series anyway so the arithmetic is identical to `[◇]`'s.
    """
    K = 2
    n = 3 * (Z + N)
    crossings = atom_canonical_crossings(Z, N, include_inter=include_inter)
    L = len(crossings)
    gens = [g for g, _ in crossings]
    d_ser = [_D.letter_d_series(kind, K) for _, kind in crossings]
    eps = [F(0), F(1)] + [F(0)] * (K - 1)
    h = _D.series_h(K)
    kpow = {}
    for m in range(n + 1):
        s = [F(1)] + [F(0)] * K
        base = [F(1), F(2), F(1)]
        for _ in range(m):
            s = _D.pmul(s, base, K)
        kpow[m] = s
    u = [F(0), F(1), F(1, 2)]
    inv, upow, coef = [F(1)] + [F(0)] * K, [F(1)] + [F(0)] * K, F(1)
    for j in range(1, K + 1):
        upow = _D.pmul(upow, u, K)
        coef = coef * F(-n - j + 1) / j
        inv = _D.padd(inv, [coef * x for x in upow])
    norm = [x / F(2) ** n for x in inv]

    raw = {c: [F(0)] * (K + 1) for c in CLASSES}
    order = list(range(L - 1, -1, -1))
    t0 = time.time()
    for b in range(1 << n):
        kb = kpow[bin(b).count("1")]
        for S in combinations(range(L), 2):
            Sset = set(S)
            state, scal = b, [F(1)] + [F(0)] * K
            for idx in order:
                g = gens[idx]
                if idx in Sset:
                    scal = _D.pmul(scal, _D.pattern_scalar(state, g, eps, h, d_ser[idx], K), K)
                else:
                    if ((state >> g) & 1) != ((state >> (g + 1)) & 1):
                        state ^= ((1 << g) | (1 << (g + 1)))
            if state == b:
                c = pair_class(gens[S[0]], gens[S[1]])
                raw[c] = _D.padd(raw[c], _D.pmul(kb, scal, K))
        if log and b and b % 512 == 0:
            log(f"      {b}/{1 << n} basis states, {time.time()-t0:.0f}s")
    return {c: _D.pmul(raw[c], norm, K) for c in CLASSES}


# Δtr = tr(free) − tr(atom), so each class contributes free-minus-atom. The FREE word has no
# interface letters at all, so its n-if and if-if classes are identically zero and those two rows
# of the difference are pure atom-side data.
CASES = (("pp", 2, 0), ("pn", 1, 1), ("nn", 0, 2),
         ("3p", 3, 0), ("T", 1, 2), ("3He", 2, 1), ("3n", 0, 3))

# What [◇] records for the |S| = 2 class on the canonical word, as the cross-check target. These
# are OUTPUTS of that probe, reproduced here — if this file's four classes do not sum to them, one
# of the two accumulations is wrong and neither number should be quoted.
S2_TARGET = {"pp": F(5, 32), "pn": F(-1, 16), "nn": F(-3, 4),
             "T": F(-11, 32), "3He": F(7, 128),
             "3p": F(73, 128), "3n": F(-23, 32)}

# Two derived-from-(Z,N) quantities the shape checks use. Both are read off the ordering
# `p…p n…n`, never fitted: `Z − N` is the content imbalance, and the like-interface pair count is
# `C(I_pp, 2) + C(I_nn, 2)` — how many WAYS two interfaces of the same kind can be chosen.
_ZMN = {"pp": 2, "pn": 0, "nn": -2, "3p": 3, "T": -1, "3He": 1, "3n": -3}
_LIKE_PAIRS = {"pp": 0, "pn": 0, "nn": 0, "3p": 1, "T": 0, "3He": 0, "3n": 1}


def _coords(Z: int, N: int) -> tuple[int, int]:
    """`(u, D)` — the coordinates `c₁`'s closed form is affine in, same convention as the
    holdout probe: `u = 3Z − 2N` and `D = I_pp − I_nn` for the ordering `p…p n…n`."""
    order = ["p"] * Z + ["n"] * N
    ipp = sum(1 for a, b in zip(order, order[1:]) if a == b == "p")
    inn = sum(1 for a, b in zip(order, order[1:]) if a == b == "n")
    return 3 * Z - 2 * N, ipp - inn


def _solve_affine(pts):
    """Exact solve of `a·u + b·D + c = y` on three points; None if the triple is singular."""
    (u1, d1, y1), (u2, d2, y2), (u3, d3, y3) = pts
    det = u1 * (d2 - d3) - d1 * (u2 - u3) + (u2 * d3 - u3 * d2)
    if det == 0:
        return None
    a = (y1 * (d2 - d3) - d1 * (y2 - y3) + (y2 * d3 - y3 * d2)) / F(det)
    b = (u1 * (y2 - y3) - y1 * (u2 - u3) + (u2 * y3 - u3 * y2)) / F(det)
    c = (u1 * (d2 * y3 - d3 * y2) - d1 * (u2 * y3 - u3 * y2)
         + y1 * (u2 * d3 - u3 * d2)) / F(det)
    return a, b, c


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", nargs="*", default=None, help="subset of case names")
    args = ap.parse_args()
    t0 = time.time()

    print("=" * 96)
    print("  |S| = 2 split by letter-PAIR class — where does the affine shape break?")
    print("=" * 96)
    print("  intra = same nucleon | cross = two nucleons | n-if = nucleon+interface | if-if = two")
    print("  interfaces.  Δtr = free − atom; the free word has NO interface letters, so the n-if")
    print("  and if-if rows are pure atom-side data.\n")

    sel = [c for c in CASES if args.cases is None or c[0] in args.cases]
    print(f"    {'case':<6}{'(Z,N)':>8}{'intra':>12}{'cross':>12}{'n-if':>12}{'if-if':>12}"
          f"{'sum':>12}{'[◇] |S|=2':>12}  ")
    ok, rows = True, []
    for name, Z, N in sel:
        f_ = s2_by_pair_class(Z, N, False)
        a_ = s2_by_pair_class(Z, N, True)
        diff = {c: f_[c][2] - a_[c][2] for c in CLASSES}
        tot = sum(diff.values())
        tgt = S2_TARGET.get(name)
        hit = (tgt is None) or (tot == tgt)
        ok = ok and hit
        uu, dd = _coords(Z, N)
        rows.append({"name": name, "A": Z + N, "u": uu, "D": dd, **diff})
        print(f"    {name:<6}{f'({Z},{N})':>8}"
              + "".join(f"{str(diff[c]):>12}" for c in CLASSES)
              + f"{str(tot):>12}{str(tgt):>12}  {'ok' if hit else 'MISMATCH'}"
              f"   [{time.time()-t0:5.1f}s]")

    print(f"\n  ⇒ {'the four classes sum to [◇]s |S|=2 on every case — the two accumulations agree.' if ok else 'MISMATCH — one of the two accumulations is wrong; quote NEITHER.'}")

    # Per-class leave-one-out at A = 3 — the SAME test c₂ failed, applied one level down. Four
    # species, three parameters: fit on three, predict the fourth, four ways. This is what says
    # WHICH class carries the non-affinity, rather than leaving it to be read off by eye.
    a3 = [r for r in rows if r["A"] == 3]
    if len(a3) == 4:
        print("\n  ── per-class leave-one-out at A = 3 (fit affine in (u, D) on three, predict the 4th) ──")
        for c in CLASSES:
            hits = []
            for i in range(4):
                train = [(r["u"], r["D"], r[c]) for j, r in enumerate(a3) if j != i]
                sol = _solve_affine(train)
                held = a3[i]
                if sol is None:
                    hits.append(None)
                    continue
                a, b, cc = sol
                hits.append(a * held["u"] + b * held["D"] + cc == held[c])
            allhit = all(h is True for h in hits)
            allmiss = all(h is False for h in hits)
            verdict = ("AFFINE — 4/4" if allhit else
                       "NOT affine — 0/4" if allmiss else
                       f"mixed {sum(1 for h in hits if h)}/4")
            print(f"    {c:<7} {verdict}")
        print("    A class that is AFFINE cannot be the source of c₂'s non-affinity; the class(es)")
        print("    that MISS are where a closed form has to supply new (Z,N) structure.")

    # Two shapes read off the table and then TESTED, each with spare degrees of freedom.
    print("\n  ── two class shapes, stated and checked ──")

    # intra: one coefficient per A against (Z − N). 7 species, 2 constants -> 5 dof.
    by_A = {}
    for r in rows:
        by_A.setdefault(r["A"], []).append(r)
    intra_ok, kappas = True, {}
    for A in sorted(by_A):
        ratios = set()
        for r in by_A[A]:
            zmn = _ZMN[r["name"]]
            if zmn == 0:
                if r["intra"] != 0:
                    ratios.add(None)          # Z = N must give 0 if the shape holds
                continue
            ratios.add(F(r["intra"]) / zmn)
        good = len(ratios) == 1 and None not in ratios
        intra_ok = intra_ok and good
        if good:
            kappas[A] = next(iter(ratios))
        print(f"    intra  A = {A}  intra/(Z−N) = "
              f"{sorted(str(x) for x in ratios)}   {'constant' if good else 'NOT constant'}")
    print(f"      ⇒ intra = (Z − N)·κ(A)  {'holds on all 7 species — 2 constants, 5 dof of test.' if intra_ok else 'REFUTED.'}"
          f"{'  κ = ' + ', '.join(f'{a}:{k}' for a, k in kappas.items()) if kappas else ''}")
    print("      (Z − N) is itself affine in (u, D), which is why this class passes the test above.")

    # if-if: like-interface PAIRS. C(I_pp,2) + C(I_nn,2) is quadratic in the interface counts,
    # which is exactly why an affine form in D cannot reach it.
    ifif_ok, coeffs = True, set()
    for r in rows:
        pairs = _LIKE_PAIRS[r["name"]]
        if pairs == 0:
            if r["if-if"] != 0:
                ifif_ok = False
            continue
        coeffs.add(F(r["if-if"]) / pairs)
    ifif_ok = ifif_ok and len(coeffs) == 1
    print(f"    if-if  (if-if)/(C(I_pp,2) + C(I_nn,2)) = {sorted(str(x) for x in coeffs)}"
          f"   zero wherever that count is zero: {'yes' if ifif_ok else 'NO'}")
    print(f"      ⇒ {'if-if = −(1/8)·[C(I_pp,2) + C(I_nn,2)] on all 7 species.' if ifif_ok else 'REFUTED — do not quote it.'}")
    print("      🛑 Read the dof honestly: at A = 2 the count is 0 for all three species and the")
    print("      class is 0, so those rows are consistent but carry no information. The content is")
    print("      the four A = 3 species against ONE coefficient — 3 dof — and the shape is the")
    print("      point: a count of LIKE-INTERFACE PAIRS is quadratic in (I_pp, I_nn), so no affine")
    print("      form in D can reach it. That is a mechanism for this class's MISS, not a fit to it.")

    print("\n  Reading it. This is a DECOMPOSITION plus one test per class. Four classes against")
    print("  four species leaves no room for a SECOND held-out check per class, so a positive")
    print("  (AFFINE) verdict here is one A's worth of evidence, not a closed form.")
    print(f"\n  ({time.time()-t0:.1f}s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
