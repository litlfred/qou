#!/usr/bin/env python3
"""Strand-end merge ceiling: the closed form of the trivial-block binding (rule 3-infinity) at every A.

Thread "Find the missing half of strong binding" (2026-11-27), epic qou-myts, gap G5.
Audit: docs/audits/2026-11-27-strand-end-merge-ceiling.md.
Lean: QOU/MassTheory/StrandEndMergeCeiling.lean (generic field, no numbers).

Rule (3-infinity) of docs/audits/2026-11-27-bond-rules-and-length-cutoff.md (PR #9659) is the
weight-free, cutoff-free limit of the uniform average over bond words: r_inf = y_(n) / tr(x),
y_(n) = [n+1]_q / [2]_q^n, n = 3A strands, x = the free word (one V^3 = (s0 s1^-1)^3 per nucleon).
That audit evaluated it at A = 2, 3 only. This probe checks two exact facts that give it at every A:

  K1  tr(x) is multiplicative over nucleons: tr_{3A}(x) = t1^A, t1 = tr_3(V^3)
      (Schur-Weyl trace, measured at A = 1, 2, 3).
  K2  y_(n) = (1 - q^{-2(n+1)}) / ((1 - q^{-2}) (1 + q^{-2})^n)  (Lean y_closed_form), checked at
      n = 1..240 against the [n+1]/[2]^n definition.
  K3  the closed form reproduces the committed (3-infinity) witness values at A = 2, 3.

So  -ln r_inf(A) = 3A ln(1 + q^-2) + A ln t1 + ln(1 - q^-2) - ln(1 - q^{-6A-2}),
an exact bulk-plus-constant law. Its q -> 1 limit is the classical reading-3 merge ceiling
n ln 2 - ln(n+1) (ClassicalReading3MergeBound): about one merge per strand, i.e. one join per strand
END, against one join per quark (T3, half as many).

Convention D, proton pin (cf.Q through the binding_ceiling_q0 helpers), mpmath 40 dps, no float
arithmetic. AME is not read here (compare_ame.py does the comparison, separately labelled).
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE.parent / "binding_ceiling_q0"))
sys.path.insert(0, str(ROOT / "computations"))
sys.argv = [sys.argv[0], "1", "1"]          # helper module reads (L, A) from argv; A is reset below
import binding_ceiling_q0_probe as bc  # noqa: E402

mp = bc.mp
Q = bc.Q
ONE = mp.mpf(1)
E0 = mp.mpf("4.2274833556290305503")       # tower E0, same parameter as the (3-inf) witness


def qint(n):
    return (Q ** n - Q ** (-n)) / (Q - 1 / Q)


def y_def(n):
    return qint(n + 1) / (Q + 1 / Q) ** n


def y_closed(n):
    u = Q ** -2
    return (1 - u ** (n + 1)) / ((1 - u) * (1 + u) ** n)


def free_trace(A):
    bc.N = 3 * A
    word = []
    for j in range(A):
        word += bc.V(3 * j) * 3
    return bc.sw_trace(word)


def minus_ln_r(A, lnt1):
    u = Q ** -2
    return 3 * A * mp.log(1 + u) + A * lnt1 + mp.log(1 - u) - mp.log(1 - u ** (3 * A + 1))


def main() -> int:
    t0 = time.time()
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(("PASS " if ok else "FAIL ") + name + ": " + detail)

    t = {A: free_trace(A) for A in (1, 2, 3)}
    t1 = t[1]
    dev = max(abs(t[A] - t1 ** A) for A in (2, 3))
    check("K1_free_trace_multiplicative", dev < mp.mpf("1e-35"),
          f"t1 = {mp.nstr(t1, 30)}, max |tr_A - t1^A| (A=2,3) = {mp.nstr(dev, 3)}")
    dev2 = max(abs(y_def(n) - y_closed(n)) / y_def(n) for n in range(1, 241))
    check("K2_y_closed_form", dev2 < mp.mpf("1e-35"), f"max rel dev n=1..240: {mp.nstr(dev2, 3)}")
    lnt1 = mp.log(t1)
    wit = {}
    for A in (2, 3):
        w = json.loads((ROOT / f"computations/probes/bond_rules_length_bound/bond-rules-length-bound-A{A}.witness.json").read_text())
        wit[A] = w
    ref = {2: mp.mpf("2.1571300"), 3: mp.mpf("3.8068536")}   # audit table, 8 digits
    dev3 = max(abs(minus_ln_r(A, lnt1) - ref[A]) for A in (2, 3))
    check("K3_reproduces_3inf_A2_A3", dev3 < mp.mpf("1e-6"),
          f"A=2 {mp.nstr(minus_ln_r(2, lnt1), 12)}, A=3 {mp.nstr(minus_ln_r(3, lnt1), 12)} (audit 2.1571300, 3.8068536)")

    u = Q ** -2
    per_strand = mp.log(1 + u) + lnt1 / 3
    table = []
    for A in (1, 2, 3, 4, 6, 12, 16, 40, 56, 120, 208, 238):
        m = minus_ln_r(A, lnt1)
        table.append({"A": A, "minus_ln_r": mp.nstr(m, 20), "B_MeV_tower": mp.nstr(E0 * m, 15),
                      "B_per_A_MeV": mp.nstr(E0 * m / A, 12)})
    out = {
        "producer": "computations/probes/strand_end_merge_ceiling/strand_end_merge_ceiling_probe.py",
        "q0Anchor": "proton", "q0Value": mp.nstr(Q, 40),
        "q0AnchorReason": "q0 enters through cf.Q (binding_ceiling_q0 helpers, proton pin)",
        "parameters": {"E0_tower_MeV": mp.nstr(E0, 20)},
        "data": {
            "t1_free_nucleon_trace": mp.nstr(t1, 40),
            "ln_t1": mp.nstr(lnt1, 40),
            "per_strand_ln_1_plus_q_minus2": mp.nstr(mp.log(1 + u), 40),
            "per_strand_bulk_with_t1": mp.nstr(per_strand, 40),
            "per_nucleon_bulk_MeV": mp.nstr(3 * E0 * per_strand, 20),
            "constant_term_ln_1_minus_q_minus2": mp.nstr(mp.log(1 - u), 40),
            "classical_per_strand_ln2": mp.nstr(mp.log(2), 40),
            "ruled_bond_minus_ln_z_minus_h_over_2": "0.676963077 (nucleus-bond-valence witness)",
            "table": table,
        },
        "assertions": checks, "allPassed": all(c["passed"] for c in checks),
        "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
    }
    (HERE / "strand-end-merge-ceiling.witness.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out["data"], indent=1))
    return 0 if out["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
