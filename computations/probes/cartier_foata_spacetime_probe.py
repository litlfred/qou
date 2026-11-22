"""Cartier-Foata time/space split of braid words (issue #7895, PR #7896).

Computational time = number of Cartier-Foata layers of a braid word in the
trace monoid where sigma_i and sigma_j commute iff |i - j| >= 2.  Letters in one
layer are simultaneous ("spacelike").  Width = the largest layer.  Lean
QOU.BraidsAndKnots.CommutingGeneratorWidth proves width <= (m+1)/2 for words on
sigma_0..sigma_{m-1}, attained by the even indices.

Pure combinatorics on generator indices (sign of each letter ignored: sigma_i
and sigma_i^-1 have the same commutation pattern).  No q, no physical value.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/qou-substrate/python", "computations"):
    sys.path.insert(0, str(_ROOT / _p))


def foata_layers(word):
    """word: list of generator indices.  Returns the list of layers."""
    height = []
    for pos, g in enumerate(word):
        h = 1
        for prev in range(pos):
            if abs(word[prev] - g) <= 1:
                h = max(h, height[prev] + 1)
        height.append(h)
    depth = max(height) if height else 0
    return [[word[p] for p in range(len(word)) if height[p] == d] for d in range(1, depth + 1)]


def nucleon(offset):
    g0, g1 = offset, offset + 1
    return [g0, g1] * 3 + [g0, g0, g1] + [g0, g0]          # B_3, 3 quark letters, gluon sigma^2


def half_twist(n):
    """Garside Delta_n = (s_0)(s_1 s_0)(s_2 s_1 s_0)..."""
    w = []
    for i in range(n - 1):
        w += list(range(i, -1, -1))
    return w


def main() -> int:
    t0 = time.time()
    rows = []
    words = {
        "nucleon block (H_3)": (nucleon(0), 2),
        "two nucleons + gamma-gamma interface bond (H_6)": (nucleon(0) + nucleon(3) + [2, 3] * 3, 5),
        "two nucleons, no bond (H_6)": (nucleon(0) + nucleon(3), 5),
    }
    for n in range(3, 11):
        words[f"half twist Delta_{n}"] = (half_twist(n), n - 1)
    print(f"{'word':52s} {'len':>4} {'time':>5} {'width':>6} {'bound':>6}")
    for name, (w, m) in words.items():
        L = foata_layers(w)
        width = max(len(set(l)) for l in L)
        bound = (m + 1) // 2
        rows.append({"word": name, "length": len(w), "time_layers": len(L), "width": width,
                     "width_bound": bound, "layers": L})
        print(f"{name:52s} {len(w):4d} {len(L):5d} {width:6d} {bound:6d}")
        assert width <= bound
    print(f"\n  wall {time.time() - t0:.2f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("cartier-foata-spacetime-probe", engine="python", start_time=t0)
    wb.set_description(
        "Issue #7895: Cartier-Foata layers of braid words. Time = number of layers, width = "
        "largest layer of pairwise-commuting generators (|i-j| >= 2). Checks Lean "
        "CommutingGeneratorWidth.card_le_of_far on corpus nucleon words and Garside half twists."
    )
    wb.add_parameter("independence", "sigma_i, sigma_j commute iff |i-j| >= 2")
    wb.add_data("rows", rows)
    wb.add_assertion(name="width_within_lean_bound",
                     computed=str(int(all(r["width"] <= r["width_bound"] for r in rows))),
                     expected="1", tolerance="0",
                     source="Lean CommutingGeneratorWidth.card_le_of_far")
    wb.add_assertion(name="half_twist_width_attains_bound",
                     computed=str(int(all(r["width"] == r["width_bound"] for r in rows if r["word"].startswith("half twist") and int(r["word"].split("_")[1]) >= 4))),
                     expected="1", tolerance="0",
                     source="Lean CommutingGeneratorWidth.exists_far_card")
    out = wb.save(extra={
        "q0Anchor": "independent",
        "q0AnchorReason": "pure combinatorics on braid-generator indices (Cartier-Foata layers); "
                          "no q, no q0, no physical value is read",
    })
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
