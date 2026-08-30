#!/usr/bin/env python3
"""Does the Markov-parameter convention put `mass_endomorphism`'s Φ_q tower near
its pole?  The companion question to `tower_vhat_markov_parameter_probe`, for
the producer that actually reads `z_mark` (beans qou-xsue, qou-zloi, qou-dchz).

WHY A SECOND PROBE.  The corpus has two tower producers and they take their
Markov parameter from different places:

  * `mass_at_3A_proper.per_generator_V_hat_3A` — weighted H_{3A} character sum.
    Its effective Markov parameter is pinned at `h/2 = 0.10453014939…` by the
    symmetry of its weight scheme (`QOU.BraidsAndKnots.markov_param_eq_half_h`),
    so no convention reaches it.  That is settled and is NOT this probe.
  * `mass_endomorphism.additive_wedderburn_volumes` — reads `z_mark` directly,
    `z_mark = q³/(q²+1)`, i.e. **convention D**.  For this one the convention is
    live, and bean `qou-dchz` item 1's claim that D moves Φ_q towers toward the
    pole is a claim about producers of this shape.

WHAT IS MEASURED.  `additive_wedderburn_volumes` runs `collapseStep` (line 128,
proved correct by `QOU.BraidsAndKnots.prod_eq_linear`) and then forms

    V̂_full = w_sym·sp + w_std·(z·α + β) + w_alt·ap

where `sp` and `ap` are the σ → q and σ → −q⁻¹ evaluations of the same word and
carry no `z`.  So V̂_full is affine in `z` with slope `w_std·α`
(`QOU.BraidsAndKnots.vHat_sub_vHat`), and `QOU.BraidsAndKnots.vHat_eq_iff` gives
the unique `z` that lands it on the Φ_q pole at `|V̂| = q`.  This probe reports,
per generator: V̂ and |V̂|/q at each of the three parameters (C, D, h/2), the
critical `z*`, and where each convention sits relative to it.

PRECISION.  The producer is float64 by design (its own comment: 18 importers
depend on that, and an mpf there would break `json.dumps` and leave BLAS).  The
recursion is therefore re-run here in mpmath at 50 dps from the same crossing
data, and cross-checked against the producer's f64 output rather than assumed to
agree with it.

SCOPE-(a).  Measures the construction as built.  It does not say which Markov
parameter is right, and excludes no ingredient.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

import _path_bridge  # noqa: F401,E402
from mpmath import mp, mpf  # noqa: E402

mp.dps = 50

import mass_endomorphism as ME  # noqa: E402
from q_parameter import Q_MP as Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

QI = 1 / Q
H = Q - QI

Z_C = mp.sqrt(Q) / (Q + 1)
Z_D = Q ** 3 / (Q ** 2 + 1)
Z_HALF_H = H / 2

PARAMS = {
    "C_sqrt_q_over_q_plus_1": Z_C,
    "D_q3_over_q2_plus_1": Z_D,
    "half_h_from_markov_param_eq_half_h": Z_HALF_H,
}


def _fmt(x) -> str:
    return mp.nstr(mpf(x), 20)


def wedderburn_weights() -> tuple:
    """`w_sym, w_std, w_alt` at n = 3, recomputed exactly.

    The producer builds these in f64; they are normalised to sum to 1, so the
    exact versions are used here and the difference is reported as a check
    rather than ignored.
    """
    def qint(k):
        return (Q ** k - QI ** k) / (Q - QI) if k else mpf(0)

    def qfact(n):
        r = mpf(1)
        for k in range(1, n + 1):
            r *= qint(k)
        return r

    def qdim(part, n):
        hooks = []
        for i, rl in enumerate(part):
            for j in range(rl):
                arm = rl - j - 1
                leg = sum(1 for r2 in range(i + 1, len(part)) if part[r2] > j)
                hooks.append(arm + leg + 1)
        num = qfact(n)
        den = mpf(1)
        for hk in hooks:
            den *= qint(hk)
        return num / den

    nf3 = qfact(3)
    ws = qdim((3,), 3) ** 2 / nf3
    wt_ = qdim((2, 1), 3) ** 2 / nf3
    wa = qdim((1, 1, 1), 3) ** 2 / nf3
    tot = ws + wt_ + wa
    return ws / tot, wt_ / tot, wa / tot


def collapse(word) -> tuple:
    """`(α, β)` for one generator's factor list — `QOU.BraidsAndKnots.collapseFold`."""
    a, b = mpf(0), mpf(1)
    for (c, d) in word:
        cc, dd = mpf(str(c)), mpf(str(d))
        a, b = a * cc * H + a * dd + b * cc, a * cc + b * dd
    return a, b


def sym_alt(word) -> tuple:
    """`sp` and `ap`: the σ → q and σ → −q⁻¹ evaluations of the same word.

    These carry no `z`, which is exactly why V̂_full is affine in `z` with slope
    `w_std·α` and nothing else moves when the convention changes.
    """
    sp, ap = mpf(1), mpf(1)
    for (c, d) in word:
        cc, dd = mpf(str(c)), mpf(str(d))
        sp *= cc * Q + dd
        ap *= -cc * QI + dd
    return sp, ap


def phi_q(z_val):
    """Φ_q(z) = Π_k (1 − q^{-k} z)^{-1}; `None` at or beyond the pole.

    Returned as `None` rather than `inf` so the caller has to say which it is;
    `qou-dchz` records the sibling producer serialising `"+inf"` as a string for
    the same reason.
    """
    if abs(z_val) >= Q:
        return None
    prod = mpf(1)
    qi_pow = QI
    for _ in range(4000):
        term = qi_pow * z_val
        factor = 1 - term
        if abs(factor) < mpf("1e-45"):
            return None
        prod /= factor
        if abs(term) < mpf("1e-45"):
            break
        qi_pow *= QI
    return prod


def analyse(label: str, cross: dict, n_strands: int) -> dict:
    w_sym, w_std, w_alt = wedderburn_weights()
    n_gens = n_strands - 1
    gens = []
    for i in range(n_gens):
        word = cross.get(i, [])
        alpha, beta = collapse(word)
        sp, ap = sym_alt(word)
        const = w_sym * sp + w_alt * ap + w_std * beta     # the z-free part
        slope = w_std * alpha                              # dV̂/dz

        row = {
            "gen": i, "n_factors": len(word),
            "alpha": _fmt(alpha), "beta": _fmt(beta),
            "dVhat_dz_eq_w_std_alpha": _fmt(slope),
            "z_free_part": _fmt(const),
            "at": {},
        }
        # vHat_eq_iff: the unique z landing V̂ exactly on the pole.
        if slope != 0:
            row["z_star_pole"] = _fmt((Q - const) / slope)
            row["z_star_pole_negative_branch"] = _fmt((-Q - const) / slope)
        else:
            row["z_star_pole"] = None
            row["z_star_pole_negative_branch"] = None

        for name, z in PARAMS.items():
            V = slope * z + const
            phi = phi_q(V)
            row["at"][name] = {
                "z": _fmt(z),
                "V_hat_full": _fmt(V),
                "abs_V_over_q": _fmt(abs(V) / Q),
                "phi_q": _fmt(phi) if phi is not None else "DIVERGENT",
            }
        gens.append(row)

    # Tower totals at each parameter: |prod V| + sum Phi_q(V) + sum_{i<j} z^2 Phi_q(|Vi Vj|)
    totals = {}
    for name, z in PARAMS.items():
        Vs = [mpf(g["at"][name]["V_hat_full"]) for g in gens]
        desc = abs(mp.fprod(Vs)) if Vs else mpf(0)
        singles = [phi_q(v) for v in Vs]
        crosses = []
        for a in range(len(Vs)):
            for b in range(a + 1, len(Vs)):
                crosses.append(phi_q(abs(Vs[a] * Vs[b])))
        divergent = any(s is None for s in singles) or any(c is None for c in crosses)
        if divergent:
            totals[name] = {"z": _fmt(z), "descended": _fmt(desc),
                            "single": "DIVERGENT" if any(s is None for s in singles) else None,
                            "cross": "DIVERGENT" if any(c is None for c in crosses) else None,
                            "total": "DIVERGENT"}
        else:
            single = sum(singles, mpf(0))
            cross_sum = sum((z * z * c for c in crosses), mpf(0))
            totals[name] = {"z": _fmt(z), "descended": _fmt(desc),
                            "single": _fmt(single), "cross": _fmt(cross_sum),
                            "total": _fmt(desc + single + cross_sum)}

    # Cross-check the mpmath re-run against the producer's own f64 output at D.
    prod_vols = ME.additive_wedderburn_volumes(n_strands, cross)
    prod_full = [mpf(str(float(v["full"]))) for v in prod_vols]
    mine_D = [mpf(g["at"]["D_q3_over_q2_plus_1"]["V_hat_full"]) for g in gens]
    worst = max((abs(a - b) for a, b in zip(prod_full, mine_D)), default=mpf(0))

    return {
        "particle": label, "n_strands": n_strands, "n_generators": n_gens,
        "wedderburn_weights": {"w_sym": _fmt(w_sym), "w_std": _fmt(w_std),
                               "w_alt": _fmt(w_alt)},
        "generators": gens,
        "tower_totals": totals,
        "producer_f64_V_hat_at_D": [_fmt(x) for x in prod_full],
        "worst_abs_diff_vs_producer_f64": _fmt(worst),
    }


def main() -> int:
    print(f"q       = {_fmt(Q)}")
    for name, z in PARAMS.items():
        print(f"  {name:<38} z = {_fmt(z)}")
    print()

    cases = [
        ("electron", ME.electron_cross, 2),
        ("proton", ME.proton_cross, 3),
        ("neutron", ME.neutron_cross, 3),
    ]
    results = [analyse(lab, cr, ns) for (lab, cr, ns) in cases]

    for r in results:
        print(f"--- {r['particle']} ({r['n_generators']} generators) ---")
        print(f"  mpmath re-run vs producer f64 at D: "
              f"worst |diff| = {r['worst_abs_diff_vs_producer_f64']}")
        for g in r["generators"]:
            print(f"  gen {g['gen']}  dV/dz = {g['dVhat_dz_eq_w_std_alpha']:>24}  "
                  f"z* (pole) = {g['z_star_pole']}")
            for name in PARAMS:
                a = g["at"][name]
                print(f"        {name:<38} V={a['V_hat_full']:>24}  "
                      f"|V|/q={a['abs_V_over_q']:>22}  Phi_q={a['phi_q']}")
        for name in PARAMS:
            t = r["tower_totals"][name]
            print(f"    tower total at {name:<38} = {t['total']}")
        print()

    checks: list[tuple[str, bool, str]] = []

    worst_xcheck = max(mpf(r["worst_abs_diff_vs_producer_f64"]) for r in results)
    checks.append((
        "mpmath re-run reproduces the f64 producer at convention D",
        worst_xcheck < mpf("1e-12"),
        f"worst |diff| = {_fmt(worst_xcheck)}"))

    # The substantive question: is any V̂ at or past the pole under D?
    div_D = [(r["particle"], g["gen"])
             for r in results for g in r["generators"]
             if g["at"]["D_q3_over_q2_plus_1"]["phi_q"] == "DIVERGENT"]
    max_over_q_D = max(
        mpf(g["at"]["D_q3_over_q2_plus_1"]["abs_V_over_q"])
        for r in results for g in r["generators"])
    checks.append((
        "NO generator of this producer is at or past the Phi_q pole under D",
        not div_D,
        f"max |V|/q under D = {_fmt(max_over_q_D)}; divergent generators: "
        f"{div_D or 'none'}"))

    # And how much the convention actually moves the tower here.
    moves = []
    for r in results:
        tC = r["tower_totals"]["C_sqrt_q_over_q_plus_1"]["total"]
        tD = r["tower_totals"]["D_q3_over_q2_plus_1"]["total"]
        if tC not in (None, "DIVERGENT") and tD not in (None, "DIVERGENT"):
            moves.append((r["particle"], mpf(tD) / mpf(tC)))
    checks.append((
        "the C->D change moves this tower by a finite, reportable factor",
        bool(moves) and all(mp.isfinite(m) for _p, m in moves),
        "; ".join(f"{p}: total_D/total_C = {_fmt(m)}" for p, m in moves)))

    # THE CONDITIONING NUMBER. Of the generators whose pole is reachable from
    # positive z (slope of the right sign), how much relative headroom does the
    # canonical convention have?  "Not divergent" and "not close" are different
    # claims and this is the second one.
    headroom = []
    for r in results:
        for g in r["generators"]:
            zs = g["z_star_pole"]
            if zs is None:
                continue
            zsv = mpf(zs)
            if zsv <= 0:
                continue          # unreachable from positive z
            headroom.append((r["particle"], g["gen"], zsv / Z_D - 1))
    worst_headroom = min((v for _p, _g, v in headroom), default=None)
    print("headroom to the Phi_q pole, in the Markov parameter:")
    for p, gi, v in headroom:
        print(f"  {p:<9} gen {gi}: z* / z_D - 1 = {_fmt(v)}  "
              f"({_fmt(v * 100)} % above the canonical convention)")
    print()
    checks.append((
        "REPORT the headroom rather than only 'not divergent'",
        worst_headroom is not None,
        f"tightest: z* is {_fmt(worst_headroom * 100)} % above z_D"
        if worst_headroom is not None else "no reachable pole"))

    # And the direction of the move is not uniform across particles, which a
    # single "D is 22.7 % larger, so towers grow" reading would miss.
    dirs = {p: ("up" if m > 1 else "down") for p, m in moves}
    checks.append((
        "the C->D move is NOT uniform in direction across particles",
        len(set(dirs.values())) > 1,
        f"{dirs} — a generator with negative dV/dz moves the opposite way, so "
        f"'D is larger, so towers grow' is wrong as a general reading"))

    print("checks:")
    ok = True
    for name, passed, detail in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}")
        ok = ok and passed

    payload = {
        "description": (
            "Whether the Markov-parameter convention puts "
            "mass_endomorphism's Phi_q tower near its pole. Companion to "
            "tower-vhat-markov-parameter, for the producer that actually "
            "reads z_mark (convention D) rather than having its Markov "
            "parameter pinned at h/2 by weight symmetry."),
        "scope": (
            "Scope-(a): measures the construction as built. Does not say "
            "which Markov parameter is right; excludes no ingredient."),
        "lean": [
            "qou:QOU.BraidsAndKnots.prod_eq_linear",
            "qou:QOU.BraidsAndKnots.vHat_sub_vHat",
            "qou:QOU.BraidsAndKnots.vHat_eq_iff",
            "qou:QOU.BraidsAndKnots.markov_param_eq_half_h",
        ],
        "q": _fmt(Q),
        "markov_parameters": {k: _fmt(v) for k, v in PARAMS.items()},
        "particles": results,
        "pole_headroom_in_markov_parameter": [
            {"particle": p, "gen": g, "z_star_over_z_D_minus_1": _fmt(v)}
            for (p, g, v) in headroom],
        "tower_total_D_over_C": {p: _fmt(m) for p, m in moves},
        "checks": [{"name": n, "passed": bool(p), "detail": d}
                   for (n, p, d) in checks],
        "all_checks_passed": bool(ok),
    }
    payload.setdefault("scriptFile", os.path.basename(__file__))
    WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine=None, q0_anchor=None)

    out = _HERE.parent / "tower-z-convention-pole-sensitivity.witness.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"\nwrote {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
