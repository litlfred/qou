#!/usr/bin/env python3
"""qbeta_d_frame_terminus_probe.py — with the cap DERIVED, the missing factor has
exactly three places to live, and all three are measured-negative.

BEAN `qou-cds1`. This is the arc's terminus, stated as a negative rather than
left as an open direction.

WHAT CHANGED. The two-row cap is DERIVED, not a ruling: the mass fibre is
2-dimensional (`lem:feynman-eigenbasis-decomposition` carries the row cap
`l(lambda) <= 2` in its index set), and `FibreDimensionForcesTL.lean` proves
fibre q-dimension -> Ocneanu parameter -> `y_(1^3) = 0`, sorry-free. Bean
`qou-n1dj`, resolved 2026-08-08. So `z = z_D` is FORCED and the earlier reading
of this gap as an artefact of an undecided convention is withdrawn -- the
discrepancy is real.

THE DECOMPOSITION. Q_beta = K * g * chi, exactly three factors:

  g     the block-weight pairing. Under the derived cap, y_(1^3) = 0 and
        z = z_D, so g = y_(3)(z_D) = (q^4+1)/(q^2+1)^2 = 0.5054042265. FORCED,
        with no freedom left. The data wants 0.8891258104 -- short by 1.7592.
  chi   the decay element's block characters. Delta_S has (c, 0, -c)
        (Lean-proved: chi^(2,1)(Delta_S) = 0 exactly). For the cap-forced
        weights to reach the required pairing, an element would need
        a_(2,1)/a_(3) = 1.5516573513.
  K     the trace -> MeV scale, outside the Hecke trace entirely.

🛑 SYMBOL COLLISION — this `K` is NOT the `K(delta)` of entries 10c/12/16.
Two different objects carry the letter in this arc, and their verdicts differ:

  * THIS `K` — the trace -> MeV scale, OUTSIDE the Hecke trace entirely.
    Verdict NEGATIVE (enumerated 2026-08-29, nothing parameter-free within
    6.31 %).
  * `K(delta)` — the multiplicative constant in the N=1 factor
    `F = cos(a - delta/2) * K(delta)`, subject to `K(0) = 1`. Verdict FREE
    (entry 12: bar-parity is vacuous on it), then filtered but not determined
    (entry 16). Numerically it is ~1; this one is a MeV-scale factor.

A reader who takes "K is closed, enumerated negative" from here and applies it
to `K(delta)` closes a question that is open; one who takes "K is free" from
entry 12 and applies it here re-opens a question that is enumerated. Same class
as the `alpha_eff` overload this arc already flags, and as the `markovZ` /
`markovZC` / `markovZc` overload in AGENTS.md.


ALL THREE ARE NEGATIVE.

  g   closed by construction: the cap is derived and z_D is forced, so there is
      nothing left to vary. Not a search that failed -- a degree of freedom that
      does not exist.
  chi 1.5516573513 matches no declared form. Nearest are [3]_q/[2]_q at 2.45 %
      and 3/2 at 3.33 % -- neither isolated, both basket-distance. AND SEARCHING
      FOR AN ELEMENT THAT HITS IT WOULD BE A FIT: the decay element is supposed
      to be DERIVED from the nucleon content, not selected to close a number.
      The ratio is recorded as a TARGET for a future derivation to be checked
      against, never as a criterion to search on.
  K   already enumerated by
      `qbeta_d_frame_admissible_base_correction_search_probe` (2026-08-29):
      no parameter-free object comes within 6.31 % on the tr_M base.

SO: no parameter-free closure of the convention-D Q_beta exists in any of the
three legs. Scope-(a) -- this is an enumeration over declared classes, not a
proved impossibility, and a derived (not searched) decay element with the right
character ratio would still close it.

WHAT IS NOT CLAIMED. That the framework is wrong, that D is wrong, or that no
closure exists. Only that the four correction classes already closed
(2026-08-29 corrections, Step 8 additive/cos, the z=1 wall, Step 9 block
re-weighting) are now joined by the remaining three legs, so the closure is not
findable by any enumeration this corpus has run.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
"""
from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 60

F_REQ_TRM = mp.mpf("1.75923699054610623")


def main() -> int:
    ok = True
    checks = []

    def check(name, passed, detail=""):
        nonlocal ok
        ok = ok and bool(passed)
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

    q = q_at(55)
    y3D = (q ** 4 + 1) / (q ** 2 + 1) ** 2
    y21D = q ** 2 / (q ** 2 + 1) ** 2
    check("normalisation y_3 + 2 y_21 = 1 at z_D (the cap leg is closed)",
          abs(y3D + 2 * y21D - 1) < mp.mpf(10) ** -45)

    a21_over_c = (y3D * F_REQ_TRM - y3D) / y21D
    print(f"\n[1] the three legs")
    print(f"    g   = y_(3)(z_D)      = {mp.nstr(y3D, 14)}   FORCED by the derived cap")
    print(f"          required          {mp.nstr(y3D * F_REQ_TRM, 14)}   short by "
          f"{mp.nstr(F_REQ_TRM, 10)}")
    print(f"    chi = a_(2,1)/a_(3)   = {mp.nstr(a21_over_c, 14)}   would be needed")
    print(f"    K   = trace -> MeV    enumerated 2026-08-29: nothing within 6.31 %")

    # DECLARED before evaluating, and the point is that none of them lands
    CANDS = {
        "[2]_q": q + 1 / q,
        "[3]_q": q ** 2 + 1 + 1 / q ** 2,
        "[3]_q/[2]_q": (q ** 2 + 1 + 1 / q ** 2) / (q + 1 / q),
        "h = q - 1/q": q - 1 / q,
        "1/z_D": (q ** 2 + 1) / q ** 3,
        "q^2": q ** 2,
        "3/2": mp.mpf(3) / 2,
        "2 - 1/q": 2 - 1 / q,
        "[2]_q - h/2": q + 1 / q - (q - 1 / q) / 2,
    }
    ranked = sorted(((abs(v - a21_over_c) / a21_over_c, k, v) for k, v in CANDS.items()))
    print(f"\n[2] nearest DECLARED forms to the needed character ratio")
    for rel, k, v in ranked[:4]:
        print(f"    {k:<14} {mp.nstr(v, 12):>16}   rel {mp.nstr(rel * 100, 5)} %")
    best, second = ranked[0], ranked[1]
    isolated = second[0] > 10 * best[0]
    check("the needed character ratio matches NO declared form (not isolated)",
          not (isolated and best[0] < mp.mpf("1e-3")),
          f"nearest {best[1]} at {mp.nstr(best[0] * 100, 4)} %, "
          f"next {second[1]} at {mp.nstr(second[0] * 100, 4)} % -> isolated={isolated}")

    verdict = (
        "SCOPE-(a) TERMINUS. With the two-row cap DERIVED (2-dim mass fibre; "
        "FibreDimensionForcesTL, bean qou-n1dj), z = z_D is forced and the "
        "block-weight leg has NO remaining freedom -- g = 0.5054042265 against a "
        "required 0.8891258104. The other two legs are measured-negative: the "
        "character ratio an element would need, 1.5516573513, matches no declared "
        "form (nearest [3]_q/[2]_q at 2.45 %, next 3/2 at 3.33 % -- basket distance, "
        "not isolation), and the trace->MeV scale was enumerated on 2026-08-29 with "
        "nothing within 6.31 %. So no parameter-free closure of the convention-D "
        "Q_beta exists in any of the three legs, joining the four correction classes "
        "already closed. NOT a proved impossibility: this is an enumeration over "
        "declared classes, and a DERIVED (not searched) decay element with the right "
        "character ratio would still close it. Searching for such an element on the "
        "number would be a fit, so the ratio is recorded as a target to check a "
        "future derivation against, never as a search criterion.")
    print(f"\n[3] {verdict}")

    wb = WitnessBuilder("qbeta-d-frame-terminus", engine="mpmath")
    wb.set_description(
        "With the two-row cap derived rather than ruled, the missing convention-D "
        "Q_beta factor has exactly three places to live -- the block-weight pairing, "
        "the decay element's character ratio, and the trace->MeV scale -- and all "
        "three are measured-negative. Records the needed character ratio as a target "
        "for a future DERIVATION, explicitly not as a search criterion.")
    wb.add_data("g_forced", mp.nstr(y3D, 20))
    wb.add_data("g_required", mp.nstr(y3D * F_REQ_TRM, 20))
    wb.add_data("shortfall_factor", mp.nstr(F_REQ_TRM, 20))
    wb.add_data("needed_character_ratio_a21_over_a3", mp.nstr(a21_over_c, 20))
    wb.add_data("nearest_declared", {k: mp.nstr(rel * 100, 6) for rel, k, _ in ranked[:5]})
    wb.add_data("legs", {
        "g (block weights)": "CLOSED — the cap is derived, z_D forced, no freedom left",
        "chi (element characters)": "NEGATIVE — needed ratio matches no declared form",
        "K (trace->MeV scale)": "NEGATIVE — enumerated 2026-08-29, nothing within 6.31%",
    })
    wb.add_data("not_claimed",
                "that the framework or convention D is wrong, or that no closure "
                "exists; only that none is findable by any enumeration this corpus "
                "has run")
    wb.add_data("free_parameters", 0)
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) enumeration over declared classes, NOT a proved impossibility")
    wb.add_data("q0Anchor", "proton")
    wb.add_data("q0Value", mp.nstr(q, 50))
    for c in checks:
        wb.add_assertion(c["name"],
                         computed=mp.mpf(1) if c["passed"] else mp.mpf(0),
                         expected=mp.mpf(1), tolerance=mp.mpf("0.5"), unit="bool")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
