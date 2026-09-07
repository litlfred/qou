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

K = 3   # truncation order: we need a3

ZN = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2), "3p": (3, 0), "T": (1, 2),
      "3He": (2, 1), "3n": (0, 3), "4He": (2, 2), "5He": (2, 3)}
LIVE_OK = ("pp", "pn", "nn", "3p", "T", "3He", "3n")

# c3 measured independently in bean qou-yaig (#6966) — NOT an input here.
C3_RECORDED = {"pp": F(67, 16), "pn": F(43, 8), "nn": F(27, 4),
               "T": F(101, 16), "3He": F(839, 128), "4He": F(1329, 256)}


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


def measure_inputs(log=print):
    nuc = {}
    for key, Z, N in (("p", 1, 0), ("n", 0, 1)):
        c = _series(Z, N, inter=False)
        nuc[key] = c
        log(f"    nucleon {key}:  a={c[0]}  r={c[1]/c[0]}  q={c[2]/c[0]}  "
            f"s={c[3]/c[0]}   (one nucleon, n=3, free word)")
    bond = {}
    for wZ, wN, which, mk in ((2, 1, "pp", dict(m_pp=1, m_pn=0, m_nn=0)),
                              (1, 2, "pn", dict(m_pp=0, m_pn=1, m_nn=0)),
                              (1, 2, "nn", dict(m_pp=0, m_pn=0, m_nn=1))):
        free = _series(wZ, wN, inter=True, m_pp=0, m_pn=0, m_nn=0)
        R = div(_series(wZ, wN, inter=True, **mk), free)
        bond[which] = R
        log(f"    bond {which}:  (1/2)(1, {R[1]/R[0]}, {R[2]/R[0]}, {R[3]/R[0]})"
            f"   (A=3, ONE interface on)")
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
    print("  Does the block-and-bond product reach c3?")
    print("=" * 78)
    log("measuring the seven inputs (2 nucleons x 4 coeffs, 3 bonds x 4) …")
    nuc, bond = measure_inputs(log)

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
        elif name in C3_RECORDED:
            src = "recorded (qou-yaig, independent)"
            ok3 = (c3_pred == C3_RECORDED[name])
            if not ok3:
                failures.append(f"{name}: c3 predicted {c3_pred} != "
                                f"recorded {C3_RECORDED[name]}")
        else:
            src = "prediction only (no target)"
        rows.append((name, Z + N, d_pred[3], c3_pred, src, ok3))
        log(f"    {name:>4s}  a3={str(d_pred[3]):>14s}  c3={str(c3_pred):>12s}  "
            f"[{src}] {'' if ok3 is None else ('ok' if ok3 else 'MISMATCH')}")

    print()
    print("=" * 78)
    print(f"  {'case':>5s} {'A':>2s} {'a3 (raw)':>16s} {'c3 = a2+a3':>14s}   source")
    for name, A, a3, c3, src, ok in rows:
        print(f"  {name:>5s} {A:>2d} {str(a3):>16s} {str(c3):>14s}   {src}")
    print("=" * 78)
    checked = [r for r in rows if r[5] is not None]
    print(f"  {sum(1 for r in checked if r[5])}/{len(checked)} checked rows agree")
    print()
    if failures:
        print("  VERDICT: the product does NOT reach c3. Multiplicativity over")
        print("  blocks and bonds holds to order 2 and breaks at order 3 — an")
        print("  irreducible term appears that no smaller object supplies.")
        for f in failures:
            print(f"    {f}")
        return 1
    print("  VERDICT: the product REACHES c3. Adding one cubic term per nucleon")
    print("  and per bond — each measured on a smaller object, none fitted to any")
    print("  c3 — reproduces every checked c3, including 4He's 1329/256, which was")
    print("  measured independently at P = 5 and contributes to no input here.")
    print()
    print("  SCOPE, inherited from the form and not weakened here: SORTED orderings")
    print("  only; A <= 5; NOT PROVED. 'pnp' remains the discriminating untested")
    print("  case. This extends the order reach, not the ordering reach.")
    print()
    print(f"PASS  {sum(1 for r in checked if r[5])}/{len(checked)} — "
          f"the block-and-bond product carries c3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
