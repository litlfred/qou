#!/usr/bin/env python3
"""Convention-D Markov trace of the v9 nucleus element (bean qou-m7py).

WHAT THIS REPLACES
------------------
`tools/hecke-engine/src/bin/v9.rs` records `tr_markov_f64` as
``Σ_w c_w · z^len(w)`` with ``z = 1/(√q + 1/√q)``. That is wrong twice:
the z is convention C (excised 2026-08-15), and the Markov trace is not
``z^len`` -- ``tr(σ₀σ₁σ₀) = h·z² + z``, not ``z³``.

THE OBJECT
----------
The v9 nucleus element for (Z, N) is the ordered crossing product

    E = Π_{k=1}^{A-1} Π_{i=0}^{k-1} X(type_i, type_k)(σ_i)

with types p…p n…n and, in v9's current (fixed) normalisation,
``X_pp = σ``, ``X_nn = σ − h = σ⁻¹``, ``2·X_pn = 2σ − h`` (doubled to stay
integral; ``pn`` counts these), ``h = q − q⁻¹``, ``σ² = hσ + 1``.

E is built exactly in the T_w (permutation) basis of H_A(q), coefficients in
ℤ[q^{±1/2}] with z formal, and its Ocneanu trace is taken by the recursion
``tr(x T_{A-1} y) = z·tr(xy)``. Only then is ``z = z_D = q³/(q²+1)``
substituted, and the result is evaluated at the proton pin, divided by
``2^pn`` (the same normalisation as v9's `*_f64` fields).

No stripping: this is the full product. v9 strips words mid-construction
whenever an element exceeds its word threshold (10B, 10Be, 12B and every
A > 12 certificate), and a stripped object is not a product, so its "trace"
is not defined by this probe. A = 12 exceeded this container's memory in
the T_w basis and is not computed.

Independent check, done when this probe was written (2026-10-11): for 4H,
5He, 5Li, 8Be and 8Li the element built here equals v9's own per-word dump
(`V9_DUMP_ELEM`) mapped to the T_w basis, coefficient for coefficient.
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import random
import time
from collections import defaultdict
from functools import lru_cache

import mpmath as mp

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 70

# Coefficients: {(z_power, t_power): int}, t = q^(1/2).
ONE = {(0, 0): 1}
H = {(0, 2): 1, (0, -2): -1}          # h = q - q^-1 = t^2 - t^-2


def cadd_into(r, c, s=1):
    for k, v in c.items():
        nv = r.get(k, 0) + s * v
        if nv:
            r[k] = nv
        else:
            r.pop(k, None)


def cmul(a, b):
    r = defaultdict(int)
    for (z1, t1), v1 in a.items():
        for (z2, t2), v2 in b.items():
            r[(z1 + z2, t1 + t2)] += v1 * v2
    return {k: v for k, v in r.items() if v}


def mul_s(elem, i):
    """elem · T_{s_i}; ws > w iff w(i) < w(i+1)."""
    out = {}
    for w, c in elem.items():
        l = list(w)
        l[i], l[i + 1] = l[i + 1], l[i]
        ws = tuple(l)
        cadd_into(out.setdefault(ws, {}), c)
        if w[i] > w[i + 1]:                    # T_w T_s = T_ws + h T_w
            cadd_into(out.setdefault(w, {}), cmul(c, H))
    return {w: c for w, c in out.items() if c}


def word_to_elem(word, n):
    e = {tuple(range(n)): dict(ONE)}
    for g in word:
        e = mul_s(e, g)
    return e


@lru_cache(maxsize=None)
def tr_perm(w):
    n = len(w)
    if n == 0:
        return frozenset(ONE.items())
    if w[-1] == n - 1:
        return tr_perm(w[:-1])
    j = w.index(n - 1)
    x = w[:j] + w[j + 1:]                      # w = x · s_{n-2} … s_j, x ∈ S_{n-1}
    e = {x: dict(ONE)}
    for i in range(n - 3, j - 1, -1):
        e = mul_s(e, i)
    acc = {}
    for u, c in e.items():
        cadd_into(acc, cmul(c, dict(tr_perm(u))))
    return frozenset(((zp + 1, tp), v) for (zp, tp), v in acc.items())


def trace(elem):
    acc = {}
    for w, c in elem.items():
        cadd_into(acc, cmul(c, dict(tr_perm(w))))
    return acc


def nucleus_element(z, n):
    a = z + n
    types = ["p"] * z + ["n"] * n
    e = {tuple(range(a)): dict(ONE)}
    pn = 0
    for k in range(1, a):
        for i in range(k):
            if types[i] == types[k] == "p":
                c, d = {(0, 0): 1}, {}
            elif types[i] == types[k] == "n":
                c, d = {(0, 0): 1}, {(0, 2): -1, (0, -2): 1}
            else:
                c, d = {(0, 0): 2}, {(0, 2): -1, (0, -2): 1}
                pn += 1
            s = mul_s(e, i)
            new = {}
            for w, cc in s.items():
                cadd_into(new.setdefault(w, {}), cmul(cc, c))
            if d:
                for w, cc in e.items():
                    cadd_into(new.setdefault(w, {}), cmul(cc, d))
            e = {w: cc for w, cc in new.items() if cc}
    return e, pn


def evaluate(tr, zv, tv):
    return mp.fsum(v * zv ** zp * tv ** tp for (zp, tp), v in tr.items())


NUCLEI = [("4H", 1, 3), ("5He", 2, 3), ("5Li", 3, 2), ("8Be", 4, 4),
          ("8Li", 3, 5), ("10B", 5, 5), ("10Be", 4, 6)]


def main() -> int:
    q0 = Q_MP
    t0 = mp.sqrt(q0)
    z_d = q0 ** 3 / (q0 ** 2 + 1)
    z_c = 1 / (t0 + 1 / t0)

    # Trace sanity: the gram.rs TR_M[5] identity, cyclicity, Markov property.
    s010 = trace(word_to_elem((0, 1, 0), 3))
    rng = random.Random(20261011)
    cyc_fail = mar_fail = 0
    for _ in range(200):
        a = tuple(rng.randrange(4) for _ in range(rng.randrange(7)))
        b = tuple(rng.randrange(4) for _ in range(rng.randrange(7)))
        if trace(word_to_elem(a + b, 5)) != trace(word_to_elem(b + a, 5)):
            cyc_fail += 1
        x = tuple(g for g in a if g < 3)
        lhs = trace(word_to_elem(x + (3,), 5))
        rhs = {(zp + 1, tp): v for (zp, tp), v in trace(word_to_elem(x, 5)).items()}
        if lhs != rhs:
            mar_fail += 1

    rows = []
    for name, z, n in NUCLEI:
        t_start = time.time()
        e, pn = nucleus_element(z, n)
        tr = trace(e)
        den = mp.mpf(2) ** pn
        rows.append({
            "nucleus": name, "Z": z, "N": n, "pn_count": pn,
            "n_permutations": len(e),
            "tr_markov_D": mp.nstr(evaluate(tr, z_d, t0) / den, 40),
            "tr_markov_C_correct_trace": mp.nstr(evaluate(tr, z_c, t0) / den, 40),
            "trace_zh_exact": [[zp, tp, str(v)] for (zp, tp), v in sorted(tr.items())],
            "seconds": f"{time.time() - t_start:.2f}",
        })
        print(f"  {name:5s} pn={pn:3d} perms={len(e):6d} "
              f"tr_D={rows[-1]['tr_markov_D'][:22]}  ({rows[-1]['seconds']}s)", flush=True)

    w = WitnessBuilder("v9-markov-trace-convention-d", engine="python-exact")
    w.set_description(
        "Exact Ocneanu/Markov trace of the v9 nucleus crossing product at "
        "convention D, z = q^3/(q^2+1), proton pin, divided by 2^pn. Replaces "
        "v9's tr_markov_f64, which weights words by z^len with convention-C z "
        "and is not a Markov trace. Full product only (no stripping)."
    )
    w.set_audit_only("beans/defs/qou-m7py (2026-10-11 entry)")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("z_convention", "D: q^3/(q^2+1)")
    w.add_data("rows", rows)
    w.add_data("not_computed", {
        "12B": "T_w-basis product exceeded container memory at A = 12",
        "A>12 certificates": "v9 strips mid-construction; the stored object is not a product",
    })
    w.add_assertion(name="tr_s0s1s0_is_hz2_plus_z", computed=sorted(s010.items()),
                    expected=sorted({(1, 0): 1, (2, 2): 1, (2, -2): -1}.items()),
                    source="gram.rs TR_M[5] = h z^2 + z")
    w.add_assertion(name="trace_cyclic_on_200_random_pairs", computed=cyc_fail, expected=0,
                    source="tr(ab) = tr(ba)")
    w.add_assertion(name="markov_property_on_200_random_words", computed=mar_fail, expected=0,
                    source="tr(x T_{n-1}) = z tr(x)")
    w.save()
    return 0 if (cyc_fail == 0 and mar_fail == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
