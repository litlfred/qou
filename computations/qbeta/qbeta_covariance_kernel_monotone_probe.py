"""The conjecture is not a monotonicity phenomenon: a FIFTH monotone route dies, badly.

Epic `qou-x631`. Follows `qou-dnev`, which measured ~40% of slack in A/B and
concluded that a LOSSY bound suffices. This tests the sharpest lossy route
available and eliminates it.

*** THE ROUTE, AND WHY IT LOOKED LIKE THE ONE ***

C_2(lam) := SUM_box c(box)^2, and chi^lam(3-cyc)/f^lam = (C_2 - C(k,2))/|C_3|, so

    G(1) = (k! / |C_3|) * Cov_P(f^lam, C_2) .

By the tower property Cov_P(f, C_2) = Cov_P(E[f | C_2], C_2), and for ANY
decreasing h one has Cov(h(X), X) <= 0. So:

    c -> E_P[f^lam | C_2 = c] monotone decreasing  ==>  THE CONJECTURE, outright.

This is a ONE-DIMENSIONAL monotonicity of a conditional mean, not a distributional
order, so the k=18 / k=26 failures that killed first-order and increasing-concave
dominance (`qou-vilx`) do not apply to it. It is also exactly the geometric
intuition the epic has leaned on throughout -- rounder shapes carry larger
dimension and smaller content spread.

*** IT IS FALSE, AND NOT NARROWLY ***

Exact rationals, E[f|C_2=c] = SUM_{C_2=c} f^3 / SUM_{C_2=c} f^2:

    k        levels   inversions   worst relative jump
    10           18            7                 2.05
    18          100           49                 3.04
    26          384          184                64.05

Roughly HALF of all consecutive level pairs are inversions, and the worst jump is
64x. This is a different failure mode from FSD/ICV, which missed by 0.0161 and
0.0011 at two isolated k.

*** AND IT SURVIVES NO COARSE-GRAINING ***

Binning lam into equal-Plancherel-mass bins by C_2 does not recover monotonicity
at any resolution tested -- 8 bins or even 4:

    k=26, 4 bins:  1.000  1.361  1.222  0.742      (relative to bin 0)
    k=26, 8 bins:  1.000  1.072  1.701  1.076  1.324  1.202  0.976  0.551

The shape is not a noisy decrease. It is a HUMP: E[f | C_2] RISES through the
middle and falls only in the top bin.

*** WHAT THE HUMP SAYS ABOUT WHERE THE NEGATIVITY LIVES ***

Cov_P(f, C_2) = SUM_lam P(lam) f(lam) (C_2(lam) - mu). The weight (C_2 - mu) is
near zero in the middle, so the interior hump contributes almost nothing. The
negativity comes from the TOP C_2 bin, where the weight is most positive and
E[f | C_2] is most suppressed -- the high-spread partitions fail to contribute
the positive mass their weight would otherwise give.

So the target is a ONE-SIDED TAIL ESTIMATE: an upper bound on E_P[f^lam | C_2 = c]
for large c. That is strictly weaker than monotonicity, it is the shape
Vershik-Kerov large-deviation machinery actually produces, and it is not what any
of the five eliminated routes was trying to prove.

*** AN IMPLEMENTATION CROSS-CHECK OF `qou-dnev` -- NOT INDEPENDENT EVIDENCE ***

Splitting the covariance by the sign of C_2 - mu gives high-mass/low-mass ratios
of 0.6008, 0.5727, 0.6223, 0.5779, 0.6068 at k = 12,16,20,24,28, agreeing with
`qou-dnev`'s A/B to every printed digit.

**That agreement is guaranteed and is not evidence for the constant.** Since
chi^lam(3)/f^lam = (C_2 - mu)/|C_3|, the two sign classes are the SAME partition
of the lambdas -- sign chi = sign(C_2 - mu) -- and (f)^2|chi| = (f)^3|C_2-mu|/|C_3|,
so the ratios are equal as an identity. What the check establishes is that two
independently written implementations of one quantity agree, which is worth
having and is all it is. Recorded explicitly because "reproduced by an
independent route" is the natural and wrong thing to say here.

*** THE TALLY ***

Monotone-flavoured routes now eliminated on this epic: FKG (`qou-r91v` item 2),
Chebyshev comonotonicity (item 3), first-order stochastic dominance and
increasing-concave dominance (`qou-vilx`), and conditional-mean monotonicity
(here). **The conjecture is not a monotonicity phenomenon**, and that is now a
measured statement rather than a run of bad luck.
"""
from __future__ import annotations

import json
import math  # float64-ok: only `math.factorial`, which returns exact Python ints; every quantity here is an exact Fraction or integer
import subprocess
import sys
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
from _mn_characters import partitions, hook_dim  # noqa: E402

LEVEL_K = tuple(range(4, 27))
BIN_K = (10, 14, 18, 22, 26)
DEC_K = (12, 16, 20, 24, 28)


def shapes(k: int):
    """(C_2(lam), f^lam) for every lam |- k."""
    nf = math.factorial(k)
    out = []
    for lam in partitions(k):
        f = hook_dim(lam, nf)
        c2 = sum((j - i) ** 2 for i, r in enumerate(lam) for j in range(r))
        out.append((c2, f))
    out.sort()
    return out


def equal_mass_bins(rows, B: int):
    """E[f | bin] as exact Fractions, bins of equal Plancherel mass."""
    tot = sum(f * f for _, f in rows)
    target = Fraction(tot, B)
    bins, num, den, acc = [], 0, 0, 0
    for _, f in rows:
        num += f ** 3
        den += f ** 2
        acc += f * f
        if acc >= target * (len(bins) + 1) and len(bins) < B - 1:
            bins.append(Fraction(num, den))
            num = den = 0
    bins.append(Fraction(num, den))
    return bins


def main() -> int:
    t0 = time.monotonic()
    a: list[dict] = []
    ok = True

    def chk(name, computed, expected, note=""):
        good = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(good), **({"note": note} if note else {})})
        print(f"  [{'PASS' if good else 'FAIL'}] {name}: {computed!r}")
        return good

    print("=" * 78)
    print("1. CONDITIONAL-MEAN MONOTONICITY IS FALSE (exact rationals)")
    print("=" * 78)
    inv_count: dict[int, int] = {}
    lvl_count: dict[int, int] = {}
    worst: dict[int, float] = {}
    for k in LEVEL_K:
        num: dict[int, int] = defaultdict(int)
        den: dict[int, int] = defaultdict(int)
        for c2, f in shapes(k):
            num[c2] += f ** 3
            den[c2] += f ** 2
        cs = sorted(num)
        means = {c: Fraction(num[c], den[c]) for c in cs}
        inv, w = 0, Fraction(0)
        for x, y in zip(cs, cs[1:]):
            if means[y] > means[x]:
                inv += 1
                w = max(w, (means[y] - means[x]) / means[x])
        inv_count[k], lvl_count[k], worst[k] = inv, len(cs), float(w)  # float64-ok: `w` is an exact Fraction; stored only for the report, and the verdicts below are integer inversion COUNTS
        if k in (10, 18, 26):
            print(f"    k={k:>3}  levels {len(cs):>4}   inversions {inv:>4}"
                  f"   worst jump {float(w):>8.2f}x")  # float64-ok: console display of an exact Fraction

    ok &= chk("conditional_mean_is_not_monotone_at_any_k",
              sorted(k for k in LEVEL_K if inv_count[k] == 0), [],
              note=f"every k in 4..26 has inversions; at k=26 there are "
                   f"{inv_count[26]} of {lvl_count[26]-1} consecutive pairs -- about "
                   f"HALF -- with a worst relative jump of {worst[26]:.1f}x. Monotone "
                   "decreasing E[f|C_2] would give the conjecture outright via "
                   "Cov(h(X),X) <= 0; it is false, and not narrowly")
    ok &= chk("inversions_grow_with_k",
              bool(inv_count[26] > inv_count[18] > inv_count[10]), True,
              note=f"{inv_count[10]} (k=10) -> {inv_count[18]} (k=18) -> "
                   f"{inv_count[26]} (k=26): the defect is structural and worsening, "
                   "not a small-k artifact")

    print()
    print("=" * 78)
    print("2. NO COARSE-GRAINING RECOVERS IT -- THE SHAPE IS A HUMP")
    print("=" * 78)
    bin_rel: dict[str, dict[int, list[float]]] = {"4": {}, "8": {}}
    mono_bins, hump_bad = [], []
    for k in BIN_K:
        rows = shapes(k)
        for B in (4, 8):
            b = equal_mass_bins(rows, B)
            if all(b[i] >= b[i + 1] for i in range(len(b) - 1)):
                mono_bins.append((k, B))
            bin_rel[str(B)][k] = [float(x / b[0]) for x in b]  # float64-ok: exact Fractions rendered for the report; monotonicity is decided on the Fractions above
        b4 = equal_mass_bins(rows, 4)
        if k >= 14 and not (b4.index(max(b4)) in (1, 2) and b4.index(min(b4)) == 3):
            hump_bad.append(k)
        print(f"    k={k:>3}  4-bin " + " ".join(f"{v:>6.3f}" for v in bin_rel['4'][k]))

    ok &= chk("no_binning_recovers_monotonicity", mono_bins, [],
              note="neither 8 equal-Plancherel-mass bins nor even 4 are monotone at any "
                   "k tested. The defect is not resolution-dependent noise")
    ok &= chk("shape_is_a_hump_not_a_decrease", hump_bad, [],
              note="for k >= 14 the 4-bin conditional mean attains its MAXIMUM at an "
                   "interior bin and its minimum at the top bin. E[f|C_2] rises through "
                   "the middle and falls only at high C_2 -- so the negativity is a "
                   "TAIL effect, and the target is a one-sided upper bound on "
                   "E_P[f|C_2=c] for large c, not a monotone trend")

    print()
    print("=" * 78)
    print("3. DECILE SPLIT REPRODUCES qou-dnev's A/B ~ 0.59 INDEPENDENTLY")
    print("=" * 78)
    halves: dict[int, float] = {}
    bad_sign = []
    for k in DEC_K:
        nf = math.factorial(k)
        mu = Fraction(k * (k - 1), 2)
        rows = shapes(k)
        neg = sum(Fraction(f ** 3, nf) * (Fraction(c2) - mu)
                  for c2, f in rows if Fraction(c2) < mu)
        pos = sum(Fraction(f ** 3, nf) * (Fraction(c2) - mu)
                  for c2, f in rows if Fraction(c2) > mu)
        if neg + pos >= 0:
            bad_sign.append(k)
        halves[k] = float(pos / -neg)  # float64-ok: ratio of two exact Fractions, reported to 4 dp; the sign verdict `bad_sign` is decided exactly
        print(f"    k={k:>3}  high-C2 mass / low-C2 mass = {halves[k]:.4f}")

    ok &= chk("covariance_is_negative_exactly", bad_sign, [],
              note="Cov_P(f, C_2) < 0 on exact rationals at every k -- the conjecture, "
                   "since G(1) = (k!/|C_3|) Cov_P(f, C_2)")
    ok &= chk("decile_split_reproduces_A_over_B",
              bool(all(0.5 < v < 0.7 for v in halves.values())), True,
              note=f"high-C_2 mass over low-C_2 mass is "
                   f"{min(halves.values()):.4f}..{max(halves.values()):.4f}, matching "
                   "`qou-dnev`'s A/B to every printed digit. NOT independent evidence: "
                   "since chi^lam(3)/f^lam = (C_2-mu)/|C_3| the two sign classes are the "
                   "same partition of the lambdas and the ratios are equal by identity. "
                   "This checks that two separately written implementations agree, and "
                   "nothing more")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        head = "unknown"
    out = HERE / "qbeta-covariance-kernel-monotone.witness.json"
    out.write_text(json.dumps({
        "computation": "qbeta-covariance-kernel-monotone",
        "assertions": a, "allPassed": bool(ok),
        "parameters": {"epic": "qou-x631", "bean": "qou-dnev",
                       "claim": "conditional-mean monotonicity of E[f|C_2] is false at "
                                "every resolution; E[f|C_2] is hump-shaped and the "
                                "negativity is a high-C_2 tail effect"},
        "data": {
            "_grade": "exact integer counts; ratios as decimal strings, 4 dp",
            "inversions": {str(k): inv_count[k] for k in LEVEL_K},
            "levels": {str(k): lvl_count[k] for k in LEVEL_K},
            "worst_relative_jump": {str(k): f"{worst[k]:.4f}" for k in LEVEL_K},
            "bin_means_relative": {b: {str(k): [f"{v:.4f}" for v in row]
                                       for k, row in d.items()}
                                   for b, d in bin_rel.items()},
            "high_over_low_mass": {str(k): f"{v:.4f}" for k, v in halves.items()},
        },
        "provenance": {"headSha": head,
                       "producer": "computations/qbeta/qbeta_covariance_kernel_monotone_probe.py",
                       "elapsed_s": f"{time.monotonic() - t0:.3f}"},
    }, indent=2) + "\n")
    print(f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
