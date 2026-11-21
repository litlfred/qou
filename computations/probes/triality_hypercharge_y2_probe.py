"""ε-Y2: what does "integer charge ⟺ triality zero" force on the quark hypercharge Y?

Pre-registered on bean qou-99qc (ε-Y2). Exact Fraction arithmetic, no floats.
Reverse of QuarkStrandConsequences Result 2: there the SM charges are imported and the
equivalence is proved; here the equivalence is the INPUT and Y is the unknown.
Strands: u, d (T3 = ±1/2, charge T3 + Y/2) and ū, d̄ (negated). Lists of length <= 6.
Scan Y = k/36, |Y| <= 4, and report every Y for which, for every list,
    total charge ∈ ℤ  ⟺  (n_q − n_q̄) ≡ 0 mod 3.
"""
import itertools, json, pathlib
from fractions import Fraction as F

T3 = {"u": F(1, 2), "d": F(-1, 2)}
STRANDS = ["u", "d", "ub", "db"]


def charge(s, Y):
    if s in T3:
        return T3[s] + Y / 2
    return -(T3[s[0]] + Y / 2)


def ok(Y, maxlen=6):
    for n in range(1, maxlen + 1):
        for l in itertools.combinations_with_replacement(STRANDS, n):
            Q = sum(charge(s, Y) for s in l)
            tri = sum(1 if s in T3 else -1 for s in l) % 3 == 0
            if (Q.denominator == 1) != tri:
                return False
    return True


sols = [F(k, 36) for k in range(-144, 145) if ok(F(k, 36))]
closed = [Y for Y in sols if not ((Y - F(1, 3)) % 2 == 0 or (Y + F(1, 3)) % 2 == 0)]
out = {
    "probe": "triality_hypercharge_y2_probe", "bean": "qou-99qc", "id": "ε-Y2",
    "q0Anchor": "independent",
    "q0AnchorReason": "no q at all: exact Fraction arithmetic over rational hypercharges and integer strand counts",
    "scan": "Y = k/36, |Y| <= 4, strand lists up to length 6",
    "solutions": [str(y) for y in sols],
    "all_of_form_pm1/3_plus_2Z": len(closed) == 0,
    "residual_freedom": "sign of Y/2 mod 1 (±1/6) and an integer shift Y -> Y + 2k",
    "consequence_eps_EM1_asymmetry_2Y": {str(y): str(2 * y) for y in sols if abs(y) <= 1},
}
p = pathlib.Path(__file__).with_name("triality-hypercharge-y2.witness.json")
p.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(out, indent=2, ensure_ascii=False))
