"""Does the block-and-bond product reach `c3`? — the direct follow-on to qou-qqm4.

THE QUESTION
------------
`atom_bond_product_closed_form_probe.py` (bean `qou-qqm4`) showed the atom word's
trace is a product over nucleon BLOCKS and interface BONDS, and reproduced `c0`,
`c1` and `c2` at `A = 2..5`, 9/9, no free parameter:

    tr(atom) = PROD_nucleons a(1 + r.e + q.e^2)
             * PROD_bonds  (1/2)(1 + rho_b.e + tau_b.e^2)

It stops at order 2 because each factor is a quadratic. **Does the same structure
carry `c3`?** That matters beyond one more coefficient: it is the direct test of
how far multiplicativity propagates, which is precisely the question I got wrong
in #6966 (retracted in #6983) when I concluded from a failed `(Z, N)`-basis
search that it did not propagate at all.

THE EXTENSION IS THE OBVIOUS ONE, AND THAT IS THE POINT
--------------------------------------------------------
Add a cubic term to every factor and change nothing else:

    nucleon   a(1 + r.e + q.e^2 + s.e^3)
    bond      (1/2)(1 + rho_b.e + tau_b.e^2 + ups_b.e^3)

The two new parameters per object (`s_p, s_n`, `ups_pp, ups_pn, ups_nn`) are
measured exactly where the originals were -- `s` on a ONE-NUCLEON free word at
`n = 3`, `ups_b` on a ONE-INTERFACE word at `A = 3` -- so every multi-interface
prediction stays a real test rather than a restatement of its own input. No
parameter is fitted to any `c3` value.

WHAT WOULD MAKE THIS A NULL RESULT
----------------------------------
If the product needed a cubic term that could not be measured on a smaller
object -- an irreducible three-body term -- the extension would fail and that
failure would be the finding: multiplicativity reaches order 2 and no further.
Both outcomes are written into the verdict below rather than decided afterwards.

THE STRONGEST ROW IS 4He, AND IT IS FREE
-----------------------------------------
`c3(4He) = 1329/256` was measured in bean `qou-yaig` (#6966) by a 352 s exact
series at `P = 5`, entirely independently and before this form was extended.
`4He` contributes nothing to any input here, so it is a pure prediction. `5He`
likewise. The `n <= 9` rows are re-measured live rather than read from a table.

CONVENTIONS -- stated because two are in play and they differ
--------------------------------------------------------------
`a_k` is the raw eps^k coefficient of `Delta = tr(free) - tr(atom)`.
`c_k = a_{k-1} + a_k` is the committed probe's convention, and is what the
`qou-yaig` table records. Both are printed so the rows tie to what is on main.

NO FLOAT: exact `fractions.Fraction` throughout.
"""
from __future__ import annotations

import importlib.util
import sys
import time
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_HERE), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

import canonical_braid_crossings as _CBC  # noqa: E402

# Same expansion engine the qou-qqm4 probe uses, so the two are comparable.
_spec = importlib.util.spec_from_file_location(
    "diag", _HERE / "c2_diagonal_insertion_expansion_probe.py")
_D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_D)
_ORIG = _CBC.atom_canonical_crossings

# Truncation order. 3 by default (the c3 question this file was written for);
# `--order N` raises it, which is how the c4 rung is tested without a second copy
# of the machinery. mul/div/predict are generic in K, so nothing else changes.
K = 4 if "--order=4" in sys.argv else (
    int(next((a.split("=")[1] for a in sys.argv if a.startswith("--order=")), 3)))

ZN = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2), "3p": (3, 0), "T": (1, 2),
      "3He": (2, 1), "3n": (0, 3), "4He": (2, 2), "5He": (2, 3)}
LIVE_OK = ("pp", "pn", "nn", "3p", "T", "3He", "3n")

# c3 measured independently in bean qou-yaig (#6966) — NOT an input here.
C3_RECORDED = {"pp": F(67, 16), "pn": F(43, 8), "nn": F(27, 4),
               "T": F(101, 16), "3He": F(839, 128), "4He": F(1329, 256)}

# c4 measured independently in bean qou-yaig (#6966) — NOT an input here. Only
# A = 2 and A = 3 were measured there; 4He's c4 was never computed, so at
# --order=4 the 4He row becomes a genuine open prediction rather than a check.
C4_RECORDED = {"pp": F(-585, 128), "pn": F(109, 192), "nn": F(27, 32),
               "T": F(743, 384), "3He": F(10001, 1536)}

RECORDED = {3: C3_RECORDED, 4: C4_RECORDED}


def mul(a, b):
    return [sum(a[i] * b[k - i] for i in range(k + 1)) for k in range(K + 1)]


def div(a, b):
    r = []
    for k in range(K + 1):
        v = a[k] - sum(r[i] * b[k - i] for i in range(k))
        r.append(v / b[0])
    return r


def _series(Z, N, *, inter, **mk):
    if mk:
        _CBC.atom_canonical_crossings = (
            lambda z, n, **kw: _ORIG(z, n, **{**kw, **mk}))
        _D.atom_canonical_crossings = _CBC.atom_canonical_crossings
    try:
        c, _ = _D.trace_expansion(Z, N, inter, K)
    finally:
        _CBC.atom_canonical_crossings = _ORIG
        _D.atom_canonical_crossings = _ORIG
    return list(c)[:K + 1]


# ---------------------------------------------------------------------------
# Measured inputs, recorded so a killed run does not have to re-earn them.
#
# 🛑 THIS IS A RESUME AID, NOT A SOURCE OF TRUTH. Nothing reads it unless
# `--inputs-from-cache` is passed explicitly, and the run says so in its output
# when it does. The default path always MEASURES. That asymmetry is deliberate:
# a cache that is consulted silently is how a stale number becomes a result, and
# this corpus has a documented history of exactly that.
#
# Cost being preserved: at K = 4 the three bonds took 2452 s, 2437 s and ~2400 s
# — about 2.7 h — and the log they were printed to lives in /tmp, which does not
# survive the container. At K = 3 the same three were ~190 s each and hardly
# worth caching; at K = 4 they dominate the run.
#
# Provenance: measured 2026-09-07 by this file at the stated order, one nucleon
# at n = 3 (free word) and one interface at A = 3, exact Fraction throughout.
#
# OBSERVED IN THE BOND ROWS, recorded and NOT built on. Writing each bond as
# (1/2)(1, rho, tau, ups, ...):
#
#     pp   (1,  2, 1/2, -1/2, 1/4)
#     pn   (1,  0, 3/2, -3/2, 31/12)
#     nn   (1, -2, 5/2, -5/2, ?)
#
# rho = p_b - n_b and tau = 1/2 + n_b are qou-qqm4's noted pattern, which that
# author correctly called a DESCRIPTION of three values with one spare dof. The
# cubic adds something that description did not predict: **ups = -tau exactly,
# in all three bonds**. That is three hits with no freedom left, which is more
# than a redescription — but it is still three data points, and the quartic
# column (1/4, 31/12, ?) shows no comparable relation to tau, so nothing here
# says the pattern continues. A derivation would have to produce it; this file
# does not, and does not use it: `predict` reads the MEASURED factors.
_INPUT_CACHE = {
    3: {
        "nuc": {"p": ["1/2", "3/4", "23/8", "75/8"],
                "n": ["1/2", "-1/2", "3/2", "19/2"]},
        "bond": {"pp": ["1/2", "1", "1/4", "-1/4"],
                 "pn": ["1/2", "0", "3/4", "-3/4"],
                 "nn": ["1/2", "-1", "5/4", "-5/4"]},
    },
    4: {
        "nuc": {"p": ["1/2", "3/4", "23/8", "75/8", "-37/4"],
                "n": ["1/2", "-1/2", "3/2", "19/2", "-57/4"]},
        "bond": {"pp": ["1/2", "1", "1/4", "-1/4", "1/8"],
                 "pn": ["1/2", "0", "3/4", "-3/4", "31/24"],
                 "nn": None},
    },
}


def _cached_inputs(log):
    """Load recorded inputs for order K. Returns None unless the table is
    COMPLETE for this order — a partial row is refused rather than silently
    padded, because a missing high-order term is exactly the coefficient the
    question turns on."""
    tab = _INPUT_CACHE.get(K)
    if tab is None:
        log(f"    no recorded inputs for K = {K}; measuring")
        return None
    out = {}
    for kind in ("nuc", "bond"):
        out[kind] = {}
        for key, row in tab[kind].items():
            if row is None or len(row) != K + 1 or any(v is None for v in row):
                log(f"    recorded inputs INCOMPLETE at K = {K} ({kind} {key});"
                    f" measuring instead")
                return None
            out[kind][key] = [F(v) for v in row]
    log(f"    USING RECORDED INPUTS for K = {K} (--inputs-from-cache). These "
        f"were measured by this file on 2026-09-07; nothing here re-derives "
        f"them. Drop the flag to measure.")
    return out["nuc"], out["bond"]


def measure_inputs(log=print):
    nuc = {}
    for key, Z, N in (("p", 1, 0), ("n", 0, 1)):
        c = _series(Z, N, inter=False)
        nuc[key] = c
        co = "  ".join(f"{nm}={c[i]/c[0]}" for i, nm in
                       zip(range(1, K + 1), ("r", "q", "s", "t", "u")))
        log(f"    nucleon {key}:  a={c[0]}  {co}   (one nucleon, n=3, free word)")
    bond = {}
    for wZ, wN, which, mk in ((2, 1, "pp", dict(m_pp=1, m_pn=0, m_nn=0)),
                              (1, 2, "pn", dict(m_pp=0, m_pn=1, m_nn=0)),
                              (1, 2, "nn", dict(m_pp=0, m_pn=0, m_nn=1))):
        free = _series(wZ, wN, inter=True, m_pp=0, m_pn=0, m_nn=0)
        R = div(_series(wZ, wN, inter=True, **mk), free)
        bond[which] = R
        inner = ", ".join(str(R[i] / R[0]) for i in range(1, K + 1))
        log(f"    bond {which}:  (1/2)(1, {inner})   (A=3, ONE interface on)")
    return nuc, bond


def predict(Z, N, nuc, bond):
    free = [F(1)] + [F(0)] * K
    for _ in range(Z):
        free = mul(free, nuc["p"])
    for _ in range(N):
        free = mul(free, nuc["n"])
    atom, order = list(free), ["p"] * Z + ["n"] * N
    for x, y in zip(order, order[1:]):
        atom = mul(atom, bond["pp" if x == y == "p" else
                              "nn" if x == y == "n" else "pn"])
    return free, atom


def main() -> int:
    t0 = time.time()

    def log(m):
        print(f"  [{time.time()-t0:6.1f}s] {m}", flush=True)

    print("=" * 78)
    print(f"  Does the block-and-bond product reach c{K}?")
    print("=" * 78)
    log(f"order K = {K}; inputs (2 nucleons x {K+1}, 3 bonds x {K+1}) …")
    cached = _cached_inputs(log) if "--inputs-from-cache" in sys.argv else None
    nuc, bond = cached if cached else measure_inputs(log)

    rows, failures = [], []
    for name, (Z, N) in ZN.items():
        pf, pa = predict(Z, N, nuc, bond)
        d_pred = [pf[k] - pa[k] for k in range(K + 1)]
        c3_pred = d_pred[2] + d_pred[3]
        src, ok3 = None, None
        if name in LIVE_OK:
            lf = _series(Z, N, inter=False)
            la = _series(Z, N, inter=True)
            d_live = [lf[k] - la[k] for k in range(K + 1)]
            src = "live"
            if d_pred != d_live:
                failures.append(f"{name}: predicted {d_pred} != live {d_live}")
            ok3 = (d_pred[2] + d_pred[3]) == (d_live[2] + d_live[3])
        elif name in RECORDED.get(K, {}):
            src = "recorded (qou-yaig, independent)"
            ok3 = (c3_pred == RECORDED[K][name])
            if not ok3:
                failures.append(f"{name}: c{K} predicted {c3_pred} != "
                                f"recorded {RECORDED[K][name]}")
        else:
            src = "prediction only (no target)"
        rows.append((name, Z + N, d_pred[3], c3_pred, src, ok3))
        log(f"    {name:>4s}  a3={str(d_pred[3]):>14s}  c3={str(c3_pred):>12s}  "
            f"[{src}] {'' if ok3 is None else ('ok' if ok3 else 'MISMATCH')}")

    print()
    print("=" * 78)
    print(f"  {'case':>5s} {'A':>2s} {f'a{K} (raw)':>16s} {f'c{K}':>16s}   source")
    for name, A, a3, c3, src, ok in rows:
        print(f"  {name:>5s} {A:>2d} {str(a3):>16s} {str(c3):>14s}   {src}")
    print("=" * 78)
    checked = [r for r in rows if r[5] is not None]
    print(f"  {sum(1 for r in checked if r[5])}/{len(checked)} checked rows agree")
    print()
    if failures:
        print(f"  VERDICT: the product does NOT reach c{K}. Multiplicativity")
        print(f"  over blocks and bonds holds below order {K} and BREAKS there —")
        print("  an irreducible term appears that no smaller object supplies.")
        for f in failures:
            print(f"    {f}")
        return 1
    print(f"  VERDICT: the product REACHES c{K}. One order-{K} term per nucleon")
    print("  and per bond — each measured on a smaller object, none fitted to any")
    print(f"  c{K} — reproduces every checked row.")
    print()
    print("  SCOPE, inherited from the form and not weakened here: SORTED orderings")
    print("  only; A <= 5; NOT PROVED. 'pnp' remains the discriminating untested")
    print("  case. This extends the order reach, not the ordering reach.")
    print()
    print(f"PASS  {sum(1 for r in checked if r[5])}/{len(checked)} — "
          f"the block-and-bond product carries c{K}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
