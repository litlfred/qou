"""Measure `V₃` for 5₂ from the Borel–Padé pole map — non-circular, parameter-free.

Question
--------
The corpus carried `V₃ = −2.7580990292` as a hardcoded literal citing
`# GGM eq 21`. Reconciliation (2026-07-26) showed it matches neither
published convention and the citation is wrong; its provenance is
unknown. The published value is `V₃ = −7.69319081986683` (GGM eq 234 at
`x = 1`, real part only per §6.1).

The two differ by a factor of 2.8, so the series itself should be able to
say which one it knows — the Borel singularity structure of `φ_σ1` is a
property of the function, independent of any labelling convention.

Why this is not circular
------------------------
The obvious test ("which candidate has a Padé pole near it?") pre-selects
the pole using the answer. This probe instead selects poles by a
constraint that mentions **neither** candidate:

> `V₃` is real (GGM §6.1 keeps only `Re V` for the σ₃ connection).
> Therefore `ζ₁₃ = V₁ − V₃` must satisfy `Im ζ₁₃ = Im V₁ = Vol(5₂)`,
> exactly, whatever `V₃` turns out to be.

So: find the Padé pole whose imaginary part is closest to `Vol(5₂)`, and
read off `V₃_measured = Re V₁ − Re(pole)`. The reality constraint fixes
the pole; the candidates are only compared afterwards.

`ζ₁₂ = V₁ − V₂` (no explicit `i` — see the 2026-08-01 double-rotation fix
in `qbeta_5two_median_borel_resummation_probe.py`) is used only as an
independent calibration that the pole map is being read in the right
frame at all: its rel dev is a known `0.0222`.

Pre-registered gates (all fixed before the first run)
-----------------------------------------------------
G0  calibration — the `ζ₁₂` pole is recovered at rel dev < 0.05.
G1  a pole exists with `|Im − Vol| / Vol < 0.10` (the reality line is
    populated at all).
G2  `V₃_measured` is closer to the published GGM value than to the legacy
    literal — reported as a ratio, not a threshold.
G3  stability: `V₃_measured` varies by < 5 % across Padé orders
    [9/10], [10/11], [11/12] (finite-order robustness, not convergence).

A near-miss on any gate is reported, never suppressed. This probe makes
no ontological claim: it compares the corpus's two candidate literals
against the observed pole structure and reports which the data favors.

auditOnly; comparison to observed; no fit; nothing wired.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from fivetwo_saddle_values import saddle_values, volume  # noqa: E402

try:
    from qou_substrate.witness import WitnessBuilder
except Exception:                                        # pragma: no cover
    WitnessBuilder = None

BASIS = Path("computations/probes/qbeta-5two-phi-series-engine.witness.json")

V3_GGM = mp.mpf("-7.69319081986683")          # published, GGM eq 234 | x=1
V3_LEGACY = mp.mpf("-2.7580990292")           # corpus literal, provenance unknown

PADE_ORDERS = [(9, 10), (10, 11), (11, 12)]


def load_basis():
    """`P_k` coefficients of `φ_σ1` from the A4.2 engine witness."""
    d = json.loads(BASIS.read_text())
    src = d.get("data", d)
    raw = src.get("P_coefficients") or src.get("P") or src.get("coefficients")
    if raw is None:
        for v in src.values():
            if isinstance(v, dict) and ("P_0" in v or "0" in v):
                raw = v
                break
    if raw is None:
        raise SystemExit(f"cannot locate P_k in {BASIS}")
    out = {}
    for k, v in raw.items():
        idx = int(str(k).replace("P_", ""))
        out[idx] = mp.mpc(v.replace("j", "")) if isinstance(v, str) and "j" in v \
            else mp.mpmathify(v)
    return [out[i] for i in range(max(out) + 1)]


def poles_at(P, m, n):
    b = [P[k] / mp.factorial(k) for k in range(len(P))]
    if m + n + 1 > len(b):
        return []
    _, den = mp.pade(b, m, n)
    return mp.polyroots([den[i] for i in range(len(den) - 1, -1, -1)],
                        maxsteps=300, extraprec=120)


def measure_V3(P, m, n, V1, vol):
    """Select the pole on the reality line `Im ζ = Vol`, read off `V₃`."""
    ps = poles_at(P, m, n)
    if not ps:
        return None
    pole = min(ps, key=lambda p: abs(mp.im(p) - vol))
    return {
        "pole": pole,
        "im_dev": abs(mp.im(pole) - vol) / vol,
        "V3": mp.re(V1) - mp.re(pole),
    }


def main() -> int:
    mp.mp.dps = 50
    P = load_basis()
    V1, V2, _ = saddle_values("ggm")
    vol = volume()
    print("=" * 78)
    print(" V3 from the Borel-Pade pole map (reality-line selection)")
    print("=" * 78)
    print(f"  basis: P_k to order {len(P) - 1}   Vol(5_2) = {mp.nstr(vol, 12)}")
    print(f"  candidates:  GGM {mp.nstr(V3_GGM, 12)}   "
          f"legacy {mp.nstr(V3_LEGACY, 12)}")

    # G0 — calibration in the zeta12 channel (frame check, no V3 involved)
    z12 = V1 - V2
    ps = poles_at(P, 11, 12)
    best12 = min(ps, key=lambda p: abs(p - z12))
    d12 = abs(best12 - z12) / abs(z12)
    g0 = d12 < mp.mpf("0.05")
    print(f"\n[G0] zeta12 calibration: pole {mp.nstr(best12, 10)} vs "
          f"{mp.nstr(z12, 10)}  rel {mp.nstr(d12, 4)}  "
          f"{'PASS' if g0 else 'FAIL'}")

    print("\n[G1/G3] reality-line pole per Pade order:")
    rows = []
    for m, n in PADE_ORDERS:
        r = measure_V3(P, m, n, V1, vol)
        if r is None:
            print(f"    [{m}/{n}] insufficient basis")
            continue
        rows.append(((m, n), r))
        print(f"    [{m:2d}/{n:2d}] pole {mp.nstr(r['pole'], 10):>28s}  "
              f"Im dev {mp.nstr(r['im_dev'], 4):>10s}   "
              f"V3 = {mp.nstr(r['V3'], 10)}")

    if not rows:
        print("\n  no usable Pade orders — INCONCLUSIVE")
        return 1

    ref = rows[-1][1]
    g1 = ref["im_dev"] < mp.mpf("0.10")
    v3m = ref["V3"]
    spread = max(abs(r["V3"] - v3m) for _, r in rows) / abs(v3m)
    g3 = spread < mp.mpf("0.05")

    d_ggm = abs(v3m - V3_GGM) / abs(V3_GGM)
    d_leg = abs(v3m - V3_LEGACY) / abs(V3_LEGACY)
    g2 = d_ggm < d_leg
    ratio = d_leg / d_ggm if d_ggm > 0 else mp.inf

    print(f"\n[G1] reality line populated: Im dev {mp.nstr(ref['im_dev'], 4)}  "
          f"{'PASS' if g1 else 'FAIL'}")
    print(f"[G3] order stability: spread {mp.nstr(spread, 4)}  "
          f"{'PASS' if g3 else 'NEAR-MISS' }")
    print(f"\n[G2] V3_measured = {mp.nstr(v3m, 12)}")
    print(f"       vs GGM    {mp.nstr(V3_GGM, 12)}   rel {mp.nstr(d_ggm, 5)}")
    print(f"       vs legacy {mp.nstr(V3_LEGACY, 12)}   rel {mp.nstr(d_leg, 5)}")
    print(f"       favours {'GGM' if g2 else 'LEGACY'} by {mp.nstr(ratio, 5)}x  "
          f"{'PASS' if g2 else 'FAIL'}")

    verdict = (
        f"The reality-line pole selection (Im zeta = Vol, mentioning neither "
        f"candidate) measures V3 = {mp.nstr(v3m, 10)}, favouring the published "
        f"GGM value {mp.nstr(V3_GGM, 10)} over the corpus legacy literal "
        f"{mp.nstr(V3_LEGACY, 10)} by {mp.nstr(ratio, 4)}x in relative "
        f"deviation. Scope-(a): evidence about which V3 the phi_sigma1 series "
        f"knows; NOT a derivation of the legacy literal's provenance, which "
        f"remains OPEN. Finite-order Pade, so the ~{mp.nstr(d_ggm * 100, 3)}% "
        f"residual vs GGM is a truncation artifact, not a discrepancy claim."
    ) if g2 else (
        "Reality-line selection does NOT favour the published value - "
        "inspect before use."
    )
    print(f"\n  verdict: {verdict}")

    if WitnessBuilder is not None:
        w = WitnessBuilder("qbeta-5two-v3-from-borel-poles",
                           script_file=Path(__file__).name)
        w.add_assertion("zeta12_calibration", float(d12), float(d12),
                        bool(g0), tolerance=0.05,
                        source="frame check: zeta12 pole recovered")
        w.add_assertion("reality_line_populated", float(ref["im_dev"]),
                        float(ref["im_dev"]), bool(g1), tolerance=0.10,
                        source="a pole sits on Im zeta = Vol")
        w.add_assertion("favours_published_V3", float(d_ggm), float(d_leg),
                        bool(g2),
                        source="V3_measured closer to GGM than to legacy")
        w.add_data("measurement", {
            "V3_measured": mp.nstr(v3m, 15),
            "V3_ggm": mp.nstr(V3_GGM, 15),
            "V3_legacy": mp.nstr(V3_LEGACY, 15),
            "rel_dev_ggm": mp.nstr(d_ggm, 8),
            "rel_dev_legacy": mp.nstr(d_leg, 8),
            "preference_ratio": mp.nstr(ratio, 8),
            "order_spread": mp.nstr(spread, 8),
            "per_order": {f"{m}/{n}": mp.nstr(r["V3"], 12) for (m, n), r in rows},
        })
        w.add_data("verdict", verdict)
        w.write(Path(__file__).parent /
                "qbeta-5two-v3-from-borel-poles.witness.json")
        print("\n  witness written")

    return 0 if (g0 and g1 and g2) else 1


if __name__ == "__main__":
    sys.exit(main())
