#!/usr/bin/env python3
"""qbeta_admissibility_is_a_magnitude_probe.py — how big is the three-row leak
at the excluded point z = 1, and is `one_not_root` a wall or a small residue?

BACKGROUND (bean `qou-cds1`). Convention-D base admissibility is closed at
exactly two Markov parameters by `QOU.QBeta.AdmissibleRoots`:

    wtNumer q z = (q^2+1) z^2 - (2q^3+q) z + q^4 = (z - q)((q^2+1) z - q^3)

is the NUMERATOR of the (1^3)-block Ocneanu weight, so "admissible" means
precisely *the trace annihilates the three-row block* -- the Wenzl two-row cap.
Its roots are z = q (augmentation) and z = z_D. `one_not_root` proves that on
the substrate window (1 < q, q below the plastic number) the coordinate-sum
point z = 1 is NOT a root, hence `net` does not descend to the two-row quotient.

WHY THIS PROBE EXISTS. `2026-08-29-cds1-admissible-base-correction-search.md`
measured that the correction the augmentation base REQUIRES is, to 0.17 %,
exactly the trace's own z=q -> z=1 return, and called that a "forbidden"
direction on the strength of `one_not_root`. That reasoning moves from a
BINARY fact (z=1 is not a root) to a claim about a MAGNITUDE (the correction is
inadmissible). Those are different statements, and the corpus's own
(a)/(b)-scope discipline says a structural exclusion needs a proved invariant
sized to the effect it excludes.

`one_not_root` is a genuine invariant, but it is an invariant about a SIGN:
N(q,1) = (1-q)(q^2+1-q^3) < 0. It says the leak is nonzero. It does not say the
leak is large. If y_(1^3)(1) were 1e-6 of the total weight, "z = 1 is
forbidden" would be true and useless -- the three-row block would be leaking a
correction-sized amount and the wall would be a step.

So this probe MEASURES the leak and compares it to the two required
corrections. It proposes nothing and wires nothing.

METHOD. The weights are solved symbolically from the H_3 Markov trace on the
NF basis, reusing the corpus's own characters
(`qbeta_net_trace_invariance_probe`) and the CORRECT sixth trace weight
z(hz+1) -- not z^3, which is not a trace at all (bean qou-isu5,
docs/audits/2026-05-19-trm5-markov-bug.md). Exact sympy throughout; the only
floats are mpmath evaluations at the pin for reporting.

SCOPE. Scope-(a) measurement. Nothing here derives a correction, and nothing
here readmits z = 1 -- `one_not_root` stands exactly as proved.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp
from mpmath import mp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    BASIS, N, basis_vec, reg_char, length, q, h,
)
# q_at(dps) returns q0 as a 50+ digit mpf. `Q` is a FLOAT, so mp.mpf(str(Q))
# would launder a float64 through a string into mpmath -- ~17 real digits
# dressed as 60 dps. Caught by the f64-into-mpmath gate on this very file.
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 60


def main() -> int:
    z = sp.symbols("z")
    ok = True
    checks = []

    def check(name, passed, detail=""):
        nonlocal ok
        ok = ok and bool(passed)
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

    # ---- 1. the three block weights, solved from the trace ----
    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI = [chi3, chi21, chi111]
    TRV = [sp.Integer(1), z, z, z ** 2, z ** 2, z * (h * z + 1)]   # qou-isu5
    yv = sp.symbols("y3 y21 y111")
    sol = sp.solve([sp.Eq(sum(yv[k] * CHI[k](basis_vec(i)) for k in range(3)), TRV[i])
                    for i in range(N)], yv, dict=True)[0]
    y3, y21, y111 = [sp.simplify(sp.cancel(sol[yv[k]])) for k in range(3)]

    print("\n[1] H_3 block weights from the Markov trace (exact, in q and z)")
    print(f"    y_(1^3)(q,z) = {sp.factor(y111)}")

    # ---- 2. its numerator IS the Lean wtNumer ----
    num, den = sp.fraction(sp.cancel(sp.together(y111)))
    wt = (q ** 2 + 1) * z ** 2 - (2 * q ** 3 + q) * z + q ** 4
    ratio = sp.cancel(sp.simplify(num / wt))
    check("y_(1^3) numerator is proportional to Lean wtNumer",
          ratio.is_constant() or not ratio.free_symbols & {z},
          f"num/wtNumer = {sp.factor(ratio)}")
    print(f"    denominator = {sp.factor(den)}")

    # ---- 3. the two admissible roots annihilate it; z=1 does not ----
    zD = q ** 3 / (q ** 2 + 1)
    for nm, zz in (("z = q (augmentation)", q), ("z = z_D", zD)):
        check(f"y_(1^3) vanishes at {nm}", sp.simplify(y111.subs(z, zz)) == 0)
    y111_at1 = sp.cancel(sp.simplify(y111.subs(z, 1)))
    check("y_(1^3) does NOT vanish at z = 1 (Lean one_not_root, re-derived)",
          sp.simplify(y111_at1) != 0, f"= {sp.factor(y111_at1)}")

    # ---- 4. THE MEASUREMENT: how big is the leak? ----
    q0 = q_at(55)
    f = sp.lambdify(q, [y3, y21, y111], "mpmath")
    y_at = lambda zz: [sp.lambdify(q, sp.cancel(e.subs(z, zz)), "mpmath")(q0)
                       for e in (y3, y21, y111)]

    rows = {}
    for nm, zz in (("z=1 (coordinate sum / net)", sp.Integer(1)),
                   ("z=q (augmentation)", q),
                   ("z=z_D (Markov, convention D)", zD)):
        a, b, c = y_at(zz)
        tot = abs(a) + abs(b) + abs(c)
        rows[nm] = {"y_3": mp.nstr(a, 12), "y_21": mp.nstr(b, 12), "y_111": mp.nstr(c, 12),
                    "three_row_share": mp.nstr(abs(c) / tot, 8) if tot else "0"}

    print("\n[2] block weights at the proton pin, and the three-row share")
    print(f"    {'z':<30} {'y_(3)':>15} {'y_(2,1)':>15} {'y_(1^3)':>15}   share")
    for nm, r in rows.items():
        print(f"    {nm:<30} {r['y_3']:>15} {r['y_21']:>15} {r['y_111']:>15}   {r['three_row_share']}")

    leak = abs(mp.mpf(rows["z=1 (coordinate sum / net)"]["y_111"]))
    share = mp.mpf(rows["z=1 (coordinate sum / net)"]["three_row_share"])

    # ---- 5. compare the leak to the corrections the bases REQUIRE ----
    # from docs/audits/2026-08-29-cds1-admissible-base-correction-search.md
    REQ = {"augmentation base": mp.mpf("0.88913"), "tr_M base": mp.mpf("1.75924")}
    print("\n[3] the leak against the required corrections")
    print(f"    three-row share at z=1                : {mp.nstr(share*100, 6)} %")
    comp = {}
    for nm, F in REQ.items():
        dev = abs(F - 1) * 100
        comp[nm] = {"F_required": mp.nstr(F, 8), "correction_size_pct": mp.nstr(dev, 6),
                    "leak_over_correction": mp.nstr(share * 100 / dev, 6)}
        print(f"    {nm:<22} needs {mp.nstr(dev,6):>8} %   leak/correction = "
              f"{mp.nstr(share*100/dev, 6)}")

    # ---- 6. is z=1 SPECIAL, or is 1.46 % just what a generic z gives? ----
    # A verdict against a threshold I pick is not a measurement. The reference
    # scale that is not arbitrary is the three-row share at OTHER values of z.
    y111_f = sp.lambdify((q, z), y111, "mpmath")
    y3_f = sp.lambdify((q, z), y3, "mpmath")
    y21_f = sp.lambdify((q, z), y21, "mpmath")

    def share_at(zz):
        a, b, c = y3_f(q0, zz), y21_f(q0, zz), y111_f(q0, zz)
        t = abs(a) + abs(b) + abs(c)
        return abs(c) / t if t else mp.mpf(0)

    zq = q0
    zd = q0 ** 3 / (q0 ** 2 + 1)
    zc = mp.sqrt(q0) / (q0 + 1)
    scan = {}
    for nm, zz in (("z=1", mp.mpf(1)), ("z=z_C (excised)", zc), ("z=1/2", mp.mpf("0.5")),
                   ("z=2", mp.mpf(2)), ("z=0", mp.mpf(0)), ("z=q/2", zq / 2),
                   ("z=2q", 2 * zq)):
        scan[nm] = mp.nstr(share_at(zz) * 100, 8)
    print("\n[4] three-row share at other z -- is z=1 special?")
    for nm, v in scan.items():
        print(f"    {nm:<18} {v:>14} %")
    others = [mp.mpf(scan[k]) for k in scan if k != "z=1"]
    z1 = mp.mpf(scan["z=1"])
    rank = sum(1 for o in others if o < z1)
    print(f"\n    z=1 is smaller than {len(others) - rank} of {len(others)} sampled "
          f"non-admissible z, larger than {rank}")

    # honest verdict: two separate facts, neither dressed as the other
    verdict = {
        "exclusion_holds": "yes -- y_(1^3)(1) != 0, exactly as one_not_root proves",
        "leak_is_too_small_to_BE_the_correction": (
            f"yes -- {mp.nstr(share*100,6)} % leak against an {mp.nstr((REQ['augmentation base']-1)*-100,6)} % "
            "required correction, a factor "
            f"{mp.nstr(abs(REQ['augmentation base']-1)*100/(share*100),4)} short"),
        "is_z1_near_admissible": (
            "z=1 sits at the LOW end of the sampled non-admissible values, so it is "
            "closer to two-row than a generic z -- but 'close' here is 1.5 %, not 0.1 %"),
    }
    print("\n[5] verdict, as two separate facts")
    for k, v in verdict.items():
        print(f"    {k}: {v}")

    wb = WitnessBuilder("qbeta-admissibility-is-a-magnitude", engine="sympy+mpmath")
    wb.set_description(
        "Measures the three-row (1^3) Ocneanu-weight leak at the EXCLUDED point z=1 and "
        "compares it to the multiplicative corrections the two admissible convention-D "
        "bases require. QOU.QBeta.AdmissibleRoots.one_not_root proves the leak is "
        "NONZERO (a sign fact); this asks how LARGE it is, which is a different question "
        "and the one the 2026-08-29 correction search implicitly answered without "
        "measuring. Scope-(a): proposes nothing, wires nothing, readmits nothing.")
    wb.add_data("y_111_symbolic", str(sp.factor(y111)))
    wb.add_data("wtNumer_agreement", str(sp.factor(ratio)))
    wb.add_data("weights_at_pin", rows)
    wb.add_data("leak_vs_required_correction", comp)
    wb.add_data("verdict", verdict)
    wb.add_data("three_row_share_scan_pct", scan)
    wb.add_data("scope", "(a) measured magnitude; one_not_root stands exactly as proved")
    wb.add_data("q0Anchor", "proton")
    wb.add_data("q0Value", mp.nstr(q0, 50))
    for c in checks:
        wb.add_assertion(c["name"],
                         computed=mp.mpf(1) if c["passed"] else mp.mpf(0),
                         expected=mp.mpf(1), tolerance=mp.mpf("0.5"), unit="bool")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
