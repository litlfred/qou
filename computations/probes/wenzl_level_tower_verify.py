#!/usr/bin/env python3
"""Independent verification of the SU(r) Wenzl level tower.

Claim under test (owner-supplied, PR #5234):

    z_r = q^r / [r]_q ,   [r]_q = (q^r - q^-r)/(q - q^-1)

is the Markov parameter of the level-`r` Wenzl quotient, in THIS repo's
Hecke normalisation (sigma^2 = (q - q^-1) sigma + 1, eigenvalues q, -q^-1).

The corpus already carries the ingredients, in
`docs/audits/2026-08-16-tl-all-n-weight-vanishing.md`:

  * Wenzl/Orellana use g^2 = (Q-1) g + Q, so matching eigenvalues gives
    sigma = g/q and Q = q^2; the Markov parameters differ by that factor,
    z_W = q * z.
  * Wenzl's level-r parameter is  z_W = Q^r (1 - Q) / (1 - Q^r).

What is NOT in the corpus, and is what this probe establishes, is that
eliminating Q and z_W from those two facts collapses to the compact
q-integer form `q^r / [r]_q` -- i.e. the tower is a rearrangement of an
already-established relation, not a new hypothesis.

Three checks:

  A. SYMBOLIC.  Over QQ(q), exactly:  q^r/[r]_q - z_W(r)/q == 0, for
     r = 1..8 and also as a general-r rational-function identity.
  B. TOWER VALUES.  z_r at the proton pin, 50 dps, r = 1..6 plus the
     r -> infinity limit h = q - 1/q.
  C. z_C IS OFF THE INTEGER TOWER.  Solve z_r = z_C for real r.

Convention/pin discipline (AGENTS.md):
  * PROTON pin throughout -- q0 = 1.1099785827513808 via
    `qou_substrate.constants.Q`.  No muon-built cache is read, so there
    is no layer straddle: this probe consumes no cached witness at all.
  * z_D = q^3/(q^2+1) is convention D (canonical, 2026-08-15 ruling R1).
  * z_C = sqrt(q)/(q+1) is convention C (excised as canonical, but
    measured here because the corpus's c_k ladder is C-frame).

No float64 reaches any serialized value: sympy exact rationals for the
symbolic leg, mpmath mpf at 65 dps for the numeric leg.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp
from mpmath import mp

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

mp.dps = 65

# ---------------------------------------------------------------- A. symbolic

qs, rs = sp.symbols("q r", positive=True)


def q_int(r_expr, q=qs):
    """[r]_q = (q^r - q^-r)/(q - q^-1)."""
    return (q**r_expr - q ** (-r_expr)) / (q - q ** (-1))


def z_tower(r_expr, q=qs):
    """Owner's claimed level-r Markov parameter: q^r / [r]_q."""
    return q**r_expr / q_int(r_expr, q)


def z_wenzl_in_repo_convention(r_expr, q=qs):
    """Wenzl's z_W = Q^r (1-Q)/(1-Q^r) at Q = q^2, converted by z = z_W/q."""
    Q = q**2
    z_W = Q**r_expr * (1 - Q) / (1 - Q**r_expr)
    return z_W / q


def symbolic_leg():
    out = {}

    # General-r identity, treating r as a symbol.  Both sides are rational
    # in q^r and q, so `simplify` on the difference is decisive.
    diff_general = sp.simplify(
        sp.together(z_tower(rs) - z_wenzl_in_repo_convention(rs))
    )
    out["general_r_difference"] = str(diff_general)
    out["general_r_identity_holds"] = bool(diff_general == 0)

    # Closed form the algebra collapses to.
    closed = sp.simplify(sp.together(z_tower(rs)))
    out["z_r_closed_form"] = str(closed)

    per_r = {}
    for r in range(1, 9):
        d = sp.cancel(sp.together(z_tower(r) - z_wenzl_in_repo_convention(r)))
        per_r[r] = {
            "z_r_exact": str(sp.cancel(sp.together(z_tower(r)))),
            "matches_wenzl": bool(sp.simplify(d) == 0),
        }
    out["per_r"] = per_r

    # Named anchors, exact.
    out["z_1_exact"] = str(sp.cancel(z_tower(1)))
    out["z_2_exact"] = str(sp.cancel(z_tower(2)))
    # z_D as spelled in the corpus.
    z_D_sym = qs**3 / (qs**2 + 1)
    out["z_2_equals_z_D"] = bool(sp.simplify(sp.cancel(z_tower(2) - z_D_sym)) == 0)
    # r -> infinity, for q > 1.  sympy's gruntz cannot resolve sign(log q)
    # on a bare positive symbol, so substitute T = q^(2r): the closed form is
    # z = q^-1 * T (q^2-1)/(T-1), and r -> inf is T -> inf at q > 1.
    T = sp.Symbol("T", positive=True)
    z_in_T = sp.cancel(z_tower(rs).rewrite(sp.Pow)).subs(qs ** (2 * rs), T)
    z_in_T = sp.cancel(sp.simplify(
        qs ** (-1) * T * (qs**2 - 1) / (T - 1)
    ))
    # confirm the T-substitution really is the same function
    r_check = 5
    out["z_in_T_matches_z_r"] = bool(
        sp.simplify(z_in_T.subs(T, qs ** (2 * r_check)) - z_tower(r_check)) == 0
    )
    lim = sp.limit(z_in_T, T, sp.oo)
    out["z_inf_limit"] = str(sp.simplify(lim))
    out["z_inf_equals_h"] = bool(sp.simplify(lim - (qs - 1 / qs)) == 0)

    return out


# ----------------------------------------------------------------- B. numeric


def z_tower_mp(r, q):
    """z_r at real (not necessarily integer) r, in mpmath."""
    r = mp.mpf(r)
    bracket = (q**r - q ** (-r)) / (q - 1 / q)
    return q**r / bracket


def numeric_leg(q):
    rows = {}
    for r in range(1, 7):
        rows[r] = mp.nstr(z_tower_mp(r, q), 30)
    rows["inf"] = mp.nstr(q - 1 / q, 30)
    return rows


# ------------------------------------------------------- C. where does z_C sit


def solve_level(z_target, q, guess=2.5):
    """Solve z_r = z_target for real r."""
    f = lambda r: z_tower_mp(r, q) - z_target
    return mp.findroot(f, mp.mpf(guess))


def main():
    from qou_substrate.constants import Q as Q_PROTON  # noqa: E402

    q = mp.mpf(str(Q_PROTON))

    sym = symbolic_leg()

    print("=" * 72)
    print("A. SYMBOLIC -- is z_r = q^r/[r]_q the Wenzl level-r parameter?")
    print("=" * 72)
    print(f"  general-r difference simplifies to : {sym['general_r_difference']}")
    print(f"  general-r identity holds           : {sym['general_r_identity_holds']}")
    print(f"  z_r closed form                    : {sym['z_r_closed_form']}")
    print(f"  z_1 exact                          : {sym['z_1_exact']}")
    print(f"  z_2 exact                          : {sym['z_2_exact']}")
    print(f"  z_2 == z_D = q^3/(q^2+1)           : {sym['z_2_equals_z_D']}")
    print(f"  lim_{{r->inf}} z_r                    : {sym['z_inf_limit']}")
    print(f"  ... equals h = q - 1/q             : {sym['z_inf_equals_h']}")
    print(f"  per-r match r=1..8                 : "
          f"{all(v['matches_wenzl'] for v in sym['per_r'].values())}")

    z_C = mp.sqrt(q) / (q + 1)
    z_C_alt = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))  # detector-blind spelling
    z_D = q**3 / (q**2 + 1)

    num = numeric_leg(q)
    print()
    print("=" * 72)
    print(f"B. TOWER at the PROTON pin q0 = {mp.nstr(q, 20)}")
    print("=" * 72)
    for r in range(1, 7):
        print(f"  r = {r:<4} z_r = {num[r]}")
    print(f"  r = inf  z   = {num['inf']}   (= h = q - 1/q)")

    r_C = solve_level(z_C, q, guess=2.5)
    r_D = solve_level(z_D, q, guess=2.0)

    print()
    print("=" * 72)
    print("C. WHERE THE TWO CONVENTIONS SIT ON THE TOWER")
    print("=" * 72)
    print(f"  z_D = q^3/(q^2+1)   = {mp.nstr(z_D, 30)}  -> r = {mp.nstr(r_D, 20)}")
    print(f"  z_C = sqrt(q)/(q+1) = {mp.nstr(z_C, 30)}  -> r = {mp.nstr(r_C, 20)}")
    print(f"  z_C alt spelling 1/(sqrt q + 1/sqrt q) = {mp.nstr(z_C_alt, 30)}")
    print(f"  ... the two z_C spellings agree      : "
          f"{mp.almosteq(z_C, z_C_alt, abs_eps=mp.mpf(10) ** -60)}")
    print(f"  z_C strictly between z_3 and z_2     : "
          f"{z_tower_mp(3, q) < z_C < z_tower_mp(2, q)}")

    payload = {
        "symbolic": sym,
        "pin": {
            "name": "proton",
            "q0": mp.nstr(q, 50),
            "source": "qou_substrate.constants.Q",
        },
        "tower": {str(k): v for k, v in num.items()},
        "conventions": {
            "z_D": {"expr": "q^3/(q^2+1)", "value": mp.nstr(z_D, 50),
                    "level_r": mp.nstr(r_D, 30)},
            "z_C": {"expr": "sqrt(q)/(q+1)", "value": mp.nstr(z_C, 50),
                    "level_r": mp.nstr(r_C, 30)},
        },
    }
    out = Path(__file__).with_name("wenzl-level-tower-verify.json")
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"\nwrote {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
