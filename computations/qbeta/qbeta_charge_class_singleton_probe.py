#!/usr/bin/env python3
"""The charge-type menu is a singleton too — and six of seven coefficients are
not hook products at all.

`qou-ld2a` showed the Wigner coefficient is selected rather than fitted: at the
quartet level the isospin class `c(lambda) = 0` has exactly one member, `(2,2)`.
The natural next question is whether that principle generalises. This probe
tests it on the Coulomb row and finds two things — the principle DOES transfer,
and the coefficients do not. Bean `qou-orjl`; instantiates the second half of
`QOU/Hecke/IsospinClassSingleton.lean`.

*** 1. THE PRINCIPLE TRANSFERS: THE CHARGE CLASS IS A SINGLETON ***

For a two-row shape `(a,b)` with `b <= a`, `2.c(a,b) = a(a-1) + b(b-3)`. The
second row can never drag that below `-2` (since `(b-1)(b-2) >= 0`), and
`a >= 2` already contributes `+2` — so `c < 0` needs `a <= 1`, leaving `(1,1)`
alone. Under the row cap `ell <= 2` that is the ENTIRE charge-type class.

So the three content-sum classes under convention D are:

    c < 0   charge    {(1,1)}                  ONE member
    c = 0   isospin   {(1), (2,1), (2,2)}      THREE
    c > 0   volume    everything else          infinitely many

*** 2. BUT THE SINGLETON GIVES THE WRONG NUMBER ***

    m_e . H_q((1,1)) = m_e [2]_q = 1.0276 MeV      vs  a_C ~ 0.711    44 % off
    corpus lambda_C  = h [6]_q m_e = 0.68244 MeV   vs  a_C ~ 0.711     4 % off

The corpus's Coulomb coefficient is a DIFFERENT object from what the block's own
form and its own selection rule produce.

*** 3. AND THE FORM CLAIM FAILS ON SIX OF SEVEN ROWS ***

`unified-iterative-correction-proof.md` states `C_lambda = m_e . H_q(lambda)` —
the q-hook product — as "the universal constant determined by the partition
algebra", with no restriction to a family. Checked against every partition with
`n <= 14` (507 of them), only ONE of the seven coefficients in
`mass-formula-regime-switching-table1-data` is a hook product:

    lambda_V   2[2][7]     NO
    lambda_S   2[4]^2      NO
    lambda_C   h[6]        NO
    a_asym     3[2][7]     NO
    delta_P    [3][7]      NO
    lambda_ex  [3]/[2]     NO
    delta_S    [2]^2[3]    YES -- H_q((2,2)), the Wigner row

The six carry integer prefactors (2, 2, 3), a bare `h = q - 1/q`, or a quotient.
None is a product of `[h]_q`: `2` is not a q-integer (`[2]_q = 2.0109`), `h` is
not a `[h]_q`, and no hook product is a quotient.

*** 🛑 A GAP, NOT A REFUTATION ***

The same block's `(2,1) |- 3` clause says the volume / surface / Coulomb
coefficients arise "through their image under the Wedderburn embedding" — an
unspecified transformation that could in principle carry one `C_lambda` to
several table entries. So the universal form claim and the table cannot both be
read at face value, but **the bridge between them is unspecified rather than
contradicted.** Recorded as a gap.

What it does settle: `(2,2)` was not fortunate-but-typical. It is the one row
that actually has the shape the block claims for all of them — which sharpens
the fit-shape QA note rather than answering it.
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 30
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
M_E = mp.mpf("0.51099895069")
H = Q0 - 1/Q0
NMAX = 14
A_C_SEMF = mp.mpf("0.711")   # EXTERNAL SEMF reference


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def qi(n):
    n = mp.mpf(n)
    return (Q0**n - Q0**(-n))/(Q0 - 1/Q0)


def conj(lam):
    return [sum(1 for x in lam if x > j) for j in range(lam[0])] if lam else []


def hooks(lam):
    c = conj(lam)
    return [lam[i] - j + c[j] - i - 1
            for i, row in enumerate(lam) for j in range(row)]


def content_sum(lam):
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def Hq(lam):
    v = mp.mpf(1)
    for h in hooks(lam):
        v *= qi(h)
    return v


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield []
        return
    for f in range(min(n, mx), 0, -1):
        for rest in partitions(n - f, f):
            yield [f] + rest


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    print("=" * 78)
    print("1. THE CHARGE-TYPE CLASS THE ROW CAP ADMITS")
    print("=" * 78)
    charge, iso = [], []
    for n in range(1, NMAX + 1):
        for b in range(0, n//2 + 1):
            aa = n - b
            if b > aa:
                continue
            lam = [aa, b] if b > 0 else [aa]
            c = content_sum(lam)
            if c < 0:
                charge.append({"lambda": tuple(lam), "n": n, "c": c})
            elif c == 0:
                iso.append({"lambda": tuple(lam), "n": n, "c": c})
    print(f"    charge-type (c < 0), ell <= 2, n <= {NMAX}: "
          f"{[x['lambda'] for x in charge]}")
    print(f"    isospin-type (c = 0), ell <= 2:            "
          f"{[x['lambda'] for x in iso]}")
    ok &= chk("the_charge_class_is_the_singleton_one_one",
              [x["lambda"] for x in charge], [(1, 1)],
              note="2.c(a,b) = a(a-1) + b(b-3); the second row never goes below "
                   "-2 and a >= 2 already gives +2, so c < 0 forces a <= 1. "
                   "Lean: contentDoubled_neg_iff")

    print()
    print("=" * 78)
    print("2. THE SINGLETON'S VALUE AGAINST THE CORPUS'S COULOMB COEFFICIENT")
    print("=" * 78)
    v11 = M_E*Hq([1, 1])
    lam_c = H*qi(6)*M_E
    print(f"    m_e H_q((1,1)) = m_e [2]_q     = {mp.nstr(v11, 10)} MeV"
          f"   vs a_C ~ {mp.nstr(A_C_SEMF, 4)}"
          f"   ({mp.nstr((v11/A_C_SEMF - 1)*100, 4)} %)")
    print(f"    corpus lambda_C = h [6]_q m_e  = {mp.nstr(lam_c, 10)} MeV"
          f"   vs a_C ~ {mp.nstr(A_C_SEMF, 4)}"
          f"   ({mp.nstr((lam_c/A_C_SEMF - 1)*100, 4)} %)")
    ok &= chk("the_selected_singleton_misses_the_coulomb_coefficient",
              abs(v11/A_C_SEMF - 1) > mp.mpf("0.3"), True,
              note=f"the row cap's unique charge-type shape gives "
                   f"{mp.nstr(v11, 8)} MeV, {mp.nstr((v11/A_C_SEMF - 1)*100, 4)} % "
                   "off. The selection principle transfers; the number does not")

    print()
    print("=" * 78)
    print(f"3. ARE THE SEVEN COEFFICIENTS HOOK PRODUCTS? (all p, n <= {NMAX})")
    print("=" * 78)
    allH = {}
    npart = 0
    for n in range(1, NMAX + 1):
        for p in partitions(n):
            allH[tuple(p)] = Hq(p)
            npart += 1
    print(f"    enumerated {npart} partitions")
    table = [("lambda_V", "2[2][7]", 2*qi(2)*qi(7)),
             ("lambda_S", "2[4]^2", 2*qi(4)**2),
             ("lambda_C", "h[6]", H*qi(6)),
             ("a_asym", "3[2][7]", 3*qi(2)*qi(7)),
             ("delta_P", "[3][7]", qi(3)*qi(7)),
             ("lambda_ex", "[3]/[2]", qi(3)/qi(2)),
             ("delta_S", "[2]^2[3]", qi(2)**2*qi(3))]
    print(f"    {'row':>10}{'form':>10}{'value':>16}   hook product of?")
    rows = []
    for name, form, val in table:
        m = [k for k, v in allH.items() if abs(v - val) < mp.mpf("1e-10")]
        rows.append({"row": name, "form": form, "value": mp.nstr(val, 14),
                     "hook_product_of": [list(x) for x in m]})
        print(f"    {name:>10}{form:>10}{mp.nstr(val, 12):>16}   "
              f"{m if m else 'NOT a hook product'}")
    ok &= chk("only_the_wigner_row_is_a_hook_product",
              [r["row"] for r in rows if r["hook_product_of"]], ["delta_S"],
              note="the other six carry integer prefactors (2, 2, 3), a bare "
                   "h = q - 1/q, or a quotient -- none of which a product of "
                   "[h]_q yields. unified-iterative-correction-proof.md states "
                   "C_lambda = m_e H_q(lambda) as THE universal constant, with "
                   "no restriction to a family")
    ok &= chk("and_two_is_not_a_q_integer",
              all(abs(qi(n) - 2) > mp.mpf("1e-3") for n in range(1, 20)), True,
              note=f"[2]_q = {mp.nstr(qi(2), 12)}, the nearest; so an integer "
                   "prefactor 2 cannot come from a hook")

    print()
    print("=" * 78)
    print("4. A GAP, NOT A REFUTATION")
    print("=" * 78)
    print("  The same block's (2,1) |- 3 clause says the volume / surface /")
    print("  Coulomb coefficients arise 'through their image under the")
    print("  Wedderburn embedding' -- an unspecified transformation that could")
    print("  in principle carry one C_lambda to several table entries. So the")
    print("  universal form claim and the table cannot both be read at face")
    print("  value, but the BRIDGE between them is unspecified rather than")
    print("  contradicted. Recorded as a gap.")
    print()
    print("  What it does settle: (2,2) was not fortunate-but-typical. It is")
    print("  the one row that actually has the shape the block claims for all")
    print("  of them -- which sharpens the fit-shape QA note, not answers it.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-charge-class-singleton",
        "q0Anchor": "proton",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS, "n_max": NMAX,
                       "m_e_MeV": str(M_E), "a_C_SEMF_MeV": str(A_C_SEMF),
                       "a_C_provenance": "EXTERNAL SEMF reference constant",
                       "lean": "QOU/Hecke/IsospinClassSingleton.lean"},
        "data": {"charge_class": charge, "isospin_class": iso,
                 "m_e_H_q_one_one": mp.nstr(v11, 16),
                 "corpus_lambda_C": mp.nstr(lam_c, 16),
                 "partitions_swept": npart, "table_rows": rows},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_charge_class_singleton_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-charge-class-singleton.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
