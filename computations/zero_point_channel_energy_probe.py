"""Zero-point channel-energy probe: does a free-vs-bound channel-measure shift match binding residuals?

Audit-only decisive probe (2026-07-03/04 audit
docs/audits/2026-07-04-zero-point-channel-energy-and-information.md; owner-approved
follow-up to PR #3258: "the D_nu interpolation has an energy — a natural quadratic
energy metric — is it missing from mass/binding?").

Constraint already established (the confinement invariant, Lean
QOU.Mass.AdditiveCorrectionConfinement): canonical absolute masses match CODATA, so any
new energy term is confined to the BINDING (defect) sector. This probe tests the two
parameter-free zero-point candidates there:

  (a) INFORMATION candidate ("no oscillation = no information = no energy"):
      E_info(n) = (E0/2) * sum_lam w-hat_lam * ln dim_q(lam)
      — the mean channel log-capacity under the normalized quadratic (Plancherel-type)
      measure w-hat_lam = dim_q^2 / sum dim_q^2. Zero iff the measure sits on a
      one-dimensional channel (no oscillation).
  (b) JM/CASIMIR candidate (quadratic energy metric):
      E_cas(n)  = (E0/2) * sum_lam w-hat_lam * |c(lam)|
      — c(lam) = content sum (the transposition-class / Jucys-Murphy eigenvalue, the
      S_n face of the quadratic Casimir; the corpus H_2 Schur weight exponent).

Free-vs-bound: a nucleon is 3 strands; an A-nucleon bound system is n = 3A strands.
  Delta_E(iso) = E(3A) - A * E(3)
compared per isotope (2H, 3H, 3He, 4He) against the binding residuals
  r_raw = B_AME - B(q0)   and   r_even = B_AME - B_even
from the committed 2026-06-30 witness (binding-bar-even-odd-probe.witness.json).

No fit: E0 is the canonical CAL-1+CAL-2 scale, the factor 1/2 is the oscillator
zero-point convention, both candidates are fully determined. Tier: shape-probe;
verdicts reported scope-(a) either way.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

from phase5_n8_dim_q_table import hook_lengths, partitions_of  # noqa: E402

DPS = 50
WITNESS_IN = Path(__file__).with_name("binding-bar-even-odd-probe.witness.json")
ISOTOPES = {"2H": 2, "3H": 3, "3He": 3, "4He": 4}  # iso -> A


def dim_q_numeric(lam: tuple[int, ...], q0: mp.mpf) -> mp.mpf:
    """Symmetric-convention q-hook quantum dimension at q0 (canonical helper's convention)."""
    def qi(h: int) -> mp.mpf:
        return (q0**h - q0**(-h)) / (q0 - q0**(-1))
    val = mp.mpf(1)
    for k in range(1, sum(lam) + 1):
        val *= qi(k)
    for h in hook_lengths(lam):
        val /= qi(h)
    return val


def content_sum(lam: tuple[int, ...]) -> int:
    """c(lam) = sum over cells (j - i), 0-indexed — the JM/transposition eigenvalue."""
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def channel_energies(n: int, q0: mp.mpf, e0: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """(E_info, E_cas) at strand count n under the normalized quadratic measure."""
    parts = partitions_of(n)
    dims = [(lam, dim_q_numeric(lam, q0)) for lam in parts]
    z = mp.fsum(d * d for _, d in dims)
    e_info = (e0 / 2) * mp.fsum((d * d) / z * mp.log(d) for _, d in dims)
    e_cas = (e0 / 2) * mp.fsum((d * d) / z * abs(content_sum(lam)) for lam, d in dims)
    return e_info, e_cas


def main() -> int:
    mp.mp.dps = DPS
    src = json.loads(WITNESS_IN.read_text())
    q0 = mp.mpf(src["constants"]["q_0"])
    e0 = mp.mpf(src["constants"]["E0_MeV"])

    cache: dict[int, tuple[mp.mpf, mp.mpf]] = {}
    for n in {3} | {3 * a for a in ISOTOPES.values()}:
        cache[n] = channel_energies(n, q0, e0)
        print(f"  n={n:2d}: E_info={mp.nstr(cache[n][0], 8):>12s} MeV   "
              f"E_cas={mp.nstr(cache[n][1], 8):>12s} MeV")

    rows = {}
    print("\n  iso |  dE_info    dE_cas  |  r_raw = B_AME-B(q0)   r_even = B_AME-B_even")
    for iso, a in ISOTOPES.items():
        d = src["isotopes"][iso]
        r_raw = mp.mpf(d["B_AME_MeV"]) - mp.mpf(d["B_q0_MeV"])
        r_even = mp.mpf(d["B_AME_MeV"]) - mp.mpf(d["B_even_cosh_MeV"])
        de_info = cache[3 * a][0] - a * cache[3][0]
        de_cas = cache[3 * a][1] - a * cache[3][1]
        rows[iso] = {
            "A": a,
            "dE_info_MeV": mp.nstr(de_info, DPS), "dE_cas_MeV": mp.nstr(de_cas, DPS),
            "residual_raw_MeV": mp.nstr(r_raw, DPS),
            "residual_even_MeV": mp.nstr(r_even, DPS),
            "ratio_info_over_raw": mp.nstr(de_info / r_raw, 12) if r_raw != 0 else None,
            "ratio_cas_over_raw": mp.nstr(de_cas / r_raw, 12) if r_raw != 0 else None,
        }
        print(f"  {iso:4s}| {float(de_info):8.3f}  {float(de_cas):9.3f} | "
              f"{float(r_raw):10.3f}          {float(r_even):10.3f}")

    # structural verdict: does either candidate track the residual (sign AND ~scale,
    # ratio within a factor 2 across all four isotopes)?
    def tracks(key: str) -> bool:
        ratios = [mp.mpf(rows[i][key]) for i in rows if rows[i][key] is not None]
        return bool(ratios and all(mp.mpf("0.5") <= r <= mp.mpf(2) for r in ratios))

    v_info = tracks("ratio_info_over_raw")
    v_cas = tracks("ratio_cas_over_raw")
    print(f"\n  info candidate tracks raw residual (all ratios in [0.5, 2]): {v_info}")
    print(f"  casimir candidate tracks raw residual (all ratios in [0.5, 2]): {v_cas}")

    witness = {
        "description": ("Zero-point channel-energy probe: parameter-free free-vs-bound "
                        "shift of (a) mean channel log-capacity and (b) mean |content| "
                        "JM/Casimir under the normalized quadratic (Plancherel-type) "
                        "channel measure, at scale E0/2, vs per-isotope binding "
                        "residuals from the 2026-06-30 witness."),
        "audit_only": True,
        "tier": "shape-probe (parameter-free; no fit, no wiring)",
        "precision_dps": DPS,
        "source_witness": WITNESS_IN.name,
        "constants": {"q_0": mp.nstr(q0, 20), "E0_MeV": mp.nstr(e0, 20)},
        "per_strand_energies": {
            str(n): {"E_info_MeV": mp.nstr(v[0], 20), "E_cas_MeV": mp.nstr(v[1], 20)}
            for n, v in cache.items()},
        "isotopes": rows,
        "verdict": {
            "info_candidate_tracks_raw_residual": v_info,
            "casimir_candidate_tracks_raw_residual": v_cas,
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "zero-point-channel-energy-probe", witness,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
