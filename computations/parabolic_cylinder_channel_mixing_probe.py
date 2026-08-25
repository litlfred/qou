"""Parabolic-cylinder channel-mixing probe: does a Weber index nu organize B_odd/B_even?

Audit-only shape probe (2026-07-03 audit
docs/audits/2026-07-03-parabolic-cylinder-channel-interpolation.md, follow-up 3).

The classical parabolic cylinder connection formula mixes the even/odd Weber
solutions with coefficients 1/Gamma((1-nu)/2) and sqrt(2)/Gamma(-nu/2); the
dimensionless mixing ratio

    R(nu) = sqrt(2) * |Gamma((1-nu)/2) / Gamma(-nu/2)|

runs 0 -> infinity on nu in (0, 1) (pure even at nu = 0, pure odd at nu = 1).
The 2026-06-30 bar-even/odd probe (binding-bar-even-odd-probe.witness.json)
gives a per-isotope channel-mixing observable rho = B_odd/B_even. This probe
inverts R(nu) = rho for nu per isotope, both classically and with the
q-deformed Gamma_q at the substrate q_0 (poles at the same lattice), and asks
ONE structural question: are the extracted nu values organized (e.g. by
neutron number N, as B_odd itself is)?

Discipline: no fit, no wiring, no production claim. The extracted nu is a
per-isotope reparametrization of rho; the only content is whether the nu
pattern is *structured*. Tier: shape-probe (exploratory).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

DPS = 50
Q0_KEY = "q_0"
WITNESS_IN = Path(__file__).with_name("binding-bar-even-odd-probe.witness.json")

# neutron numbers of the probed isotopes (2026-06-30 finding: B_odd = f(N))
NEUTRONS = {"2H": 1, "3H": 2, "3He": 1, "4He": 2}


def gamma_q(x: mp.mpf, q: mp.mpf) -> mp.mpf:
    """Jackson q-gamma for 0 < q < 1: (1-q)^(1-x) * (q;q)_inf / (q^x;q)_inf."""
    return (1 - q) ** (1 - x) * mp.qp(q, q) / mp.qp(q**x, q)


def gamma_q_gt1(x: mp.mpf, q: mp.mpf) -> mp.mpf:
    """Standard q > 1 extension: Gamma_q(x) = q^((x-1)(x-2)/2) * Gamma_{1/q}(x)."""
    return q ** ((x - 1) * (x - 2) / 2) * gamma_q(x, 1 / q)


def weber_ratio(nu: mp.mpf, gamma) -> mp.mpf:
    """R(nu) = sqrt(2) |Gamma((1-nu)/2) / Gamma(-nu/2)| for the given gamma."""
    return mp.sqrt(2) * abs(gamma((1 - nu) / 2) / gamma(-nu / 2))


def invert_ratio(rho: mp.mpf, gamma) -> mp.mpf:
    """Solve R(nu) = rho for nu in (0, 1); R is monotone increasing there."""
    return mp.findroot(lambda nu: weber_ratio(nu, gamma) - rho,
                       (mp.mpf("1e-6"), mp.mpf("1") - mp.mpf("1e-6")),
                       solver="anderson", tol=mp.mpf(10) ** (-(DPS - 10)))


def main() -> int:
    mp.mp.dps = DPS
    src = json.loads(WITNESS_IN.read_text())
    q0 = mp.mpf(src["constants"][Q0_KEY])

    rows = []
    unsolvable = []
    for iso, d in src["isotopes"].items():
        rho = mp.mpf(d["B_odd_sinh_MeV"]) / mp.mpf(d["B_even_cosh_MeV"])
        # R(nu) = sqrt(2)*|Gamma(..)/Gamma(..)| is an ABSOLUTE VALUE, so it is
        # non-negative for every nu.  A negative rho therefore has no solution
        # AT ALL -- not "none in (0,1)", and not a bracketing or starting-point
        # problem.  mp.findroot bottomed out at residual 0.023 against a 1e-40
        # tolerance and raised "Try another starting point or tweak arguments",
        # which is exactly the wrong instinct here: no argument makes an
        # absolute value equal a negative number.
        #
        # The sign is PHYSICAL, not noise: 3H and 3He are mirror nuclei and
        # their odd (sinh) channels have opposite sign (+0.15173766 vs
        # -0.15171379).  Whether the right reading is to invert |rho| and carry
        # the sign separately is a question about what this probe CLAIMS, so it
        # is left to the owner rather than decided here (bean qou-n7ue).
        if rho < 0:
            unsolvable.append((iso, NEUTRONS[iso], rho))
            print(f"  {iso:4s} N={NEUTRONS[iso]}  rho={mp.nstr(rho, 8):>12s}  "
                  f"NO SOLUTION — R(nu) >= 0 for all nu, rho < 0")
            continue
        nu_cl = invert_ratio(rho, mp.gamma)
        nu_q = invert_ratio(rho, lambda x: gamma_q_gt1(x, q0))
        rows.append((iso, NEUTRONS[iso], rho, nu_cl, nu_q))
        print(f"  {iso:4s} N={NEUTRONS[iso]}  rho={mp.nstr(rho, 8):>12s}  "
              f"nu_classical={mp.nstr(nu_cl, 8):>12s}  nu_q={mp.nstr(nu_q, 8):>12s}")

    # structural checks (booleans, not fits)
    by_n: dict[int, list[mp.mpf]] = {}
    for _, n, _, nu_cl, _ in rows:
        by_n.setdefault(n, []).append(nu_cl)
    # B_odd is exactly N-organized; nu inherits that ONLY if B_even were too —
    # measure the spread of nu within each N class vs across classes.
    spread_within = max((max(v) - min(v)) for v in by_n.values())
    means = {n: mp.fsum(v) / len(v) for n, v in by_n.items()}
    spread_across = max(means.values()) - min(means.values())
    n_organized = bool(spread_within < spread_across / 10)
    # WITHHELD when any isotope was unsolvable.  Dropping one is not neutral
    # for this verdict: with 3He removed the N=1 class is a SINGLETON, so
    # `spread_within` for that class is identically 0 and the comparison is
    # degenerate.  Reporting the same verdict on a reduced sample would be a
    # weaker claim wearing the stronger claim's name.
    if unsolvable:
        n_organized = None

    if unsolvable:
        names = ", ".join(i for i, _n, _r in unsolvable)
        print(f"\n  ** n_organized WITHHELD: {names} unsolvable (rho < 0). "
              f"Dropping it leaves an N-class singleton, so the within-class "
              f"spread is degenerate and the verdict is not comparable. **")
    print(f"\n  nu spread within N-classes : {mp.nstr(spread_within, 6)}")
    print(f"  nu spread across N-classes : {mp.nstr(spread_across, 6)}")
    print(f"  nu N-organized (within << across)? {n_organized}")

    witness = {
        "description": ("Weber/parabolic-cylinder channel-mixing index nu extracted "
                        "from B_odd/B_even per isotope (classical Gamma and Gamma_q "
                        "at substrate q_0); structural question: is nu N-organized?"),
        "audit_only": True,
        "tier": "shape-probe (exploratory; no fit, no production wiring)",
        "precision_dps": DPS,
        "source_witness": WITNESS_IN.name,
        "constants": {"q_0": mp.nstr(q0, 20)},
        "isotopes": {
            iso: {"N": n, "mixing_ratio_rho": mp.nstr(r, DPS),
                  "nu_classical": mp.nstr(ncl, DPS), "nu_q_deformed": mp.nstr(nq, DPS)}
            for iso, n, r, ncl, nq in rows
        },
        "structure": {
            "nu_spread_within_N_classes": mp.nstr(spread_within, 20),
            "nu_spread_across_N_classes": mp.nstr(spread_across, 20),
            "nu_is_N_organized": n_organized,
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "parabolic-cylinder-channel-mixing-probe", witness,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
