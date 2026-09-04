#!/usr/bin/env python3
"""The MIXED chain closes too: five numbers give Delta_tr for every atom.

`qbeta_chain_closed_form_probe.py` solved the homogeneous chain and left the
mixed one open — real atoms have p-p, p-n and n-n interfaces, so a single ratio
cannot serve. This closes it, and the p-p factor turns out to be an object the
framework already has a name for.

*** THE FORM, DERIVED FROM THE CHAIN STRUCTURE ***

`atom_braid_word_3A` builds `ordering = ['p'] * Z + ['n'] * N` and, for each
`k < A - 1`, inserts the pp / pn / nn crossing at generator `3k + 2` (read from
the source, not assumed). So `(Z, N)` carries exactly `Z - 1` p-p bonds, one p-n
bond when both species are present, and `N - 1` n-n bonds.

With `tr_M(beta_free) = t_p^Z t_n^N` already established exactly, the natural
form is one factor per bond:

    tr_M(beta_atom(Z,N)) = t_p^Z . t_n^N . b_pp^(Z-1) . b_pn^[Z,N>=1] . b_nn^(N-1)

*** MEASURED — AND b_pp IS THE MARKOV PARAMETER ***

From the pure-proton chain, `b = tr_atom(A) / t_p^A` is constant in A:

    A = 2   0.61268803714646479409
    A = 3   0.612688037146464828      (taking the (A-1)-th root)
    A = 4   0.61268803714646537953
    z       0.6126880371464652516     <- q^3/(q^2+1), convention D

    b_pp - z = -4.6e-16

**The p-p bond factor IS the Ocneanu parameter `z`.** Not fitted to it — `b_pp`
is one number read off the chain and it lands on a constant the framework
already defines, to sixteen digits.

    b_pn = 0.50822978937673896258     from 2H
    b_nn = 0.40362773835082593617     from 3H

*** HELD OUT: 3He AND 4He ***

    3He   predicted 0.403767036851427869   measured 0.40376703685142817    rel 7.5e-16
    4He   predicted 0.160974145442407262   measured 0.160974145442407382   rel 7.5e-16

Two parameters (`b_pn`, `b_nn`) fixed on two atoms; the other two atoms are
predictions, and the residual is at the float64 floor of the measured inputs.

*** CONSEQUENCE ***

    Delta_tr(Z,N) = t_p^Z t_n^N . (1 - b_pp^(Z-1) b_pn^[Z,N>=1] b_nn^(N-1))

Five numbers — `t_p`, `t_n`, `z`, `b_pn`, `b_nn` — give `Delta_tr` for EVERY
atom. No matrices at any A, so the n >= 15 dimension wall is irrelevant to the
question it was blocking.

It also reconciles with the homogeneous result: there `tr_atom(A) = t_p r^(A-1)`
with `r = 0.70199325701320136`, and `t_p . z = 0.70199325701320...` — so the
earlier symbolic `r(q)` is `t_p(q) . z(q)`, and the two derivations agree.

*** WHAT IS DERIVED AND WHAT IS NOT ***

DERIVED: the form (chain structure plus Ocneanu multiplicativity over disjoint
strand ranges); `t_p`, `t_n` as H_3 traces; `b_pp = z` as an identification that
holds to 4.6e-16 rather than being imposed.

NOT YET DERIVED: `b_pn` and `b_nn` are extracted from 2H and 3H. They should
yield to the same exact-Laurent treatment that produced `r(q)` — that is the
open step, and until it is done they are two measured constants, not closed
forms. Saying otherwise would make this a fit with two knobs.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "computations"))

DPS = 40
mp.mp.dps = DPS
Q0S = "1.1099785827513808075916690956107688798744991218736"
Q0 = mp.mpf(Q0S)
Z_MARKOV = Q0**3 / (Q0**2 + 1)                     # convention D

T_P = mp.mpf("1.1457596924573008697")
T_N = mp.mpf("0.98774368811580957163")
R_HOMOG = mp.mpf("0.7019932570132013577923154")    # derived symbolically earlier

PURE_P = {2: "0.804315578262543954", 3: "0.56462411245097933",
          4: "0.396362319687651834"}
ATOM_WITNESS = {"2H": ("chi-deuteron-h6-at-q0-50dps.witness.json", 1, 1),
                "3H": ("chi-tritium-h9-at-q0-50dps.witness.json", 1, 2),
                "3He": ("chi-helium-3-h9-at-q0-50dps.witness.json", 2, 1),
                "4He": ("chi-helium-4-h12-at-q0-50dps.witness.json", 2, 2)}


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


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
    tr = {}
    for tag, (wf, Z, N) in ATOM_WITNESS.items():
        d = json.loads((ROOT / "computations" / wf).read_text())
        tr[tag] = mp.mpf(d["tr_M_at_q0"])

    print("=" * 74)
    print("1. THE p-p BOND FACTOR IS THE MARKOV PARAMETER z")
    print("=" * 74)
    roots = []
    for A in (2, 3, 4):
        bpow = mp.mpf(PURE_P[A]) / T_P**A
        root = bpow ** (mp.mpf(1) / (A - 1))
        roots.append(root)
        print(f"  A={A}: b^(A-1) = {mp.nstr(bpow,20):>24}   b = {mp.nstr(root,20)}")
    print(f"  Markov z (= q^3/(q^2+1))          = {mp.nstr(Z_MARKOV, 20)}")
    b_pp = mp.mpf(PURE_P[2]) / T_P**2
    print(f"  b_pp - z = {mp.nstr(b_pp - Z_MARKOV, 6)}")
    ok &= chk("b_pp_equals_the_markov_parameter",
              abs(b_pp - Z_MARKOV) < mp.mpf("1e-14"), True,
              "one number read off the chain lands on a constant the framework "
              "already defines, to 16 digits")
    ok &= chk("b_pp_is_A_independent",
              (max(roots) - min(roots)) / min(roots) < mp.mpf("1e-14"), True)

    print("\n" + "=" * 74)
    print("2. THE OTHER TWO BOND FACTORS, FROM 2H AND 3H")
    print("=" * 74)
    b_pn = tr["2H"] / (T_P * T_N)
    b_nn = tr["3H"] / (T_P * T_N**2 * b_pn)
    print(f"  b_pn (from 2H) = {mp.nstr(b_pn, 20)}")
    print(f"  b_nn (from 3H) = {mp.nstr(b_nn, 20)}")

    def predict(Z, N):
        v = T_P**Z * T_N**N * b_pp**(Z - 1) * b_nn**(N - 1)
        if Z >= 1 and N >= 1:
            v *= b_pn
        return v

    print("\n" + "=" * 74)
    print("3. HELD OUT — 3He AND 4He ARE PREDICTIONS")
    print("=" * 74)
    rows, worst = [], mp.mpf(0)
    for tag in ("3He", "4He"):
        _, Z, N = ATOM_WITNESS[tag]
        p, m = predict(Z, N), tr[tag]
        rel = abs(p - m) / abs(m)
        worst = max(worst, rel)
        rows.append({"atom": tag, "Z": Z, "N": N, "predicted": mp.nstr(p, 20),
                     "measured": mp.nstr(m, 20), "rel_err": mp.nstr(rel, 6)})
        print(f"  {tag:<5} predicted {mp.nstr(p,18):>22}  measured "
              f"{mp.nstr(m,18):>22}  rel {mp.nstr(rel,6)}")
    ok &= chk("held_out_atoms_predicted", worst < mp.mpf("1e-13"), True,
              "two parameters fixed on 2H and 3H; 3He and 4He are predictions")

    print("\n" + "=" * 74)
    print("4. CONSISTENCY WITH THE HOMOGENEOUS DERIVATION: r = t_p . z")
    print("=" * 74)
    print(f"  t_p . z  = {mp.nstr(T_P * Z_MARKOV, 20)}")
    print(f"  r        = {mp.nstr(R_HOMOG, 20)}   (derived symbolically)")
    ok &= chk("homogeneous_r_equals_t_p_times_z",
              abs(T_P * Z_MARKOV - R_HOMOG) / R_HOMOG < mp.mpf("1e-14"), True,
              "so the earlier symbolic r(q) is t_p(q).z(q); two derivations agree")

    print("\n" + "=" * 74)
    print("5. Delta_tr FOR EVERY ATOM, FROM FIVE NUMBERS")
    print("=" * 74)
    dt = []
    print(f"  {'atom':<5}{'Z':>2}{'N':>2}{'Delta_tr predicted':>24}{'measured':>22}")
    for tag, (_, Z, N) in ATOM_WITNESS.items():
        free = T_P**Z * T_N**N
        d_pred = free - predict(Z, N)
        d_meas = free - tr[tag]
        dt.append({"atom": tag, "Z": Z, "N": N,
                   "delta_predicted": mp.nstr(d_pred, 20),
                   "delta_measured": mp.nstr(d_meas, 20)})
        print(f"  {tag:<5}{Z:>2}{N:>2}{mp.nstr(d_pred,18):>24}"
              f"{mp.nstr(d_meas,18):>22}")

    print("\n  🛑 b_pn and b_nn are EXTRACTED from 2H and 3H, not yet derived.")
    print("     They should yield to the same exact-Laurent treatment that gave")
    print("     r(q). Until then they are two measured constants.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-mixed-chain-closed-form",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": Q0S, "dps": DPS, "t_p": str(T_P), "t_n": str(T_N),
                       "z_markov": mp.nstr(Z_MARKOV, 25),
                       "b_pp": mp.nstr(b_pp, 25), "b_pn": mp.nstr(b_pn, 25),
                       "b_nn": mp.nstr(b_nn, 25),
                       "ordering": "['p']*Z + ['n']*N, read from "
                                   "mass_at_3A_proper.atom_braid_word_3A",
                       "trace_convention": "D (SU(2)/Temperley-Lieb)"},
        "data": {"pure_proton_b_roots": [mp.nstr(r, 20) for r in roots],
                 "held_out": rows, "delta_tr": dt,
                 "r_homogeneous": mp.nstr(R_HOMOG, 20),
                 "t_p_times_z": mp.nstr(T_P * Z_MARKOV, 20)},
        "context": {
            "axis": "does the mixed p/n chain close in the same way the "
                    "homogeneous one did?",
            "answer": "Yes. One factor per bond, with b_pp equal to the Markov "
                      "parameter z to 4.6e-16. Delta_tr(Z,N) = t_p^Z t_n^N "
                      "(1 - b_pp^(Z-1) b_pn b_nn^(N-1)) — five numbers for "
                      "every atom, no matrices, so the n >= 15 dimension wall "
                      "does not bear on the question it was blocking.",
            "derived_vs_measured": "DERIVED: the form (chain structure plus "
                                   "Ocneanu multiplicativity over disjoint "
                                   "strand ranges); t_p and t_n as H_3 traces; "
                                   "b_pp = z as an identification, not an "
                                   "imposition. NOT DERIVED: b_pn and b_nn are "
                                   "extracted from 2H and 3H and are two "
                                   "measured constants until the exact-Laurent "
                                   "treatment that produced r(q) is applied to "
                                   "them.",
            "scope": "Scope-(a). No content block edited.",
        },
        "gitCommit": _head_sha(),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-mixed-chain-closed-form.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton",
            q0_anchor_reason="experimental pin (Physical-Observations layer): q0 read at the proton m_p/m_e pin", q0_value=Q0S)
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
