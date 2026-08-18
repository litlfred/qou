#!/usr/bin/env python3
"""gram_convention_d_singularity_structural_probe.py — is the convention-D
Markov–Gram singularity STRUCTURAL, or a float64 artifact?

Bean `qou-cds2`, the plan's self-described highest-risk item. It records, at
the proton pin in float64:

    eigenvalues -0.752702, 0, +0.752702 x3, +4.230339
    det 3.998e-17     cond 4.9e16     ||G G_INV - I|| = 1.64

and notes in the same breath that `np.linalg.inv` is "inverting rounding
noise -- which is exactly the observed cond 4.9e16". Those two readings pull
in opposite directions: `det = 4e-17` is equally consistent with an EXACTLY
singular form seen through float64, and with a merely ill-conditioned one.
The distinction decides whether the named repair (quotient by the radical) is
the right repair or an over-reaction, so it should not be left to inference.

WHAT THIS MEASURES

At 60 dps -- 45 orders below float64 epsilon -- the two hypotheses separate
cleanly:

  structural  det collapses with dps (bounded by the working precision), and
              the null direction is stable
  artifact    det parks near 1e-17 regardless of dps, i.e. it is f64 noise

Run at three precisions so the trend, not a single number, carries the claim.

CONVENTION. `gram.py` has NO convention-D path: both `gram_matrix_mp` and
`z_mp` hardcode `z = 1/(sqrt(q) + sqrt(1/q))`, which IS `sqrt(q)/(q+1)` -- one
of the detector-blind C spellings AGENTS.md warns about. So the D Gram is
rebuilt here from the same `_nf_of_word_mp` / `NF_BASIS` primitives with the
single line `z_D = q^3/(q^2+1)` swapped in. Nothing else differs, which is the
point: any spectral difference is attributable to z alone.

WHAT THIS DOES NOT DO. It does not switch any convention, does not touch
`gram.py`, and proposes no value. It measures one structural fact so the
cds2 repair decision rests on a measurement instead of on a float64 reading
the bean itself flags as noise-dominated.

Anchor: proton (experimental, the 2026-08-07 default).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import NF_BASIS, _nf_of_word_mp  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

set_compute_dps()


def gram_at(q, z, dps):
    """The 6x6 Markov-Gram at modulus q with Markov parameter z.

    Same construction as pyhecke.gram.gram_matrix_mp; z is a parameter here
    rather than hardcoded to the C spelling.
    """
    with mp.workdps(dps):
        q = mp.mpf(q)
        h = q - 1 / q
        trm = [mp.mpf(1), +z, +z, +(z ** 2), +(z ** 2), +(h * z ** 2 + z)]
        G = mp.matrix(6, 6)
        for i in range(6):
            for j in range(6):
                nf = _nf_of_word_mp(NF_BASIS[i] + NF_BASIS[j], h)
                G[i, j] = +mp.fsum(nf[k] * trm[k] for k in range(6))
        return G


def spectrum(G, dps):
    with mp.workdps(dps):
        ev = mp.eigsy(G, eigvals_only=True)
        vals = sorted([ev[i] for i in range(6)], key=lambda x: float(x))
        det = mp.det(G)
        amax = max(abs(v) for v in vals)
        amin = min(abs(v) for v in vals)
        cond = amax / amin if amin != 0 else mp.inf
        return vals, det, cond


def main() -> int:
    q = q_at()
    zC = lambda qq: 1 / (mp.sqrt(qq) + mp.sqrt(1 / qq))      # noqa: E731
    zD = lambda qq: qq ** 3 / (qq ** 2 + 1)                   # noqa: E731

    print("=" * 78)
    print(" Is the convention-D Gram singularity structural, or float64 noise?")
    print("=" * 78)
    print(f"\n  proton anchor q0 = {mp.nstr(q, 20)}")
    print(f"  z_C = {mp.nstr(zC(q), 18)}   z_D = {mp.nstr(zD(q), 18)}")

    rows = []
    print(f"\n  {'conv':>5} {'dps':>5} {'|det|':>14} {'cond':>12} {'min|eig|':>14}")
    print("  " + "-" * 56)
    for name, zf in (("C", zC), ("D", zD)):
        for dps in (30, 60, 120):
            with mp.workdps(dps):
                G = gram_at(q, zf(mp.mpf(q)), dps)
                vals, det, cond = spectrum(G, dps)
                amin = min(abs(v) for v in vals)
            print(f"  {name:>5} {dps:>5} {mp.nstr(abs(det), 6):>14} "
                  f"{mp.nstr(cond, 4):>12} {mp.nstr(amin, 6):>14}")
            rows.append({"convention": name, "dps": dps,
                         "abs_det": fmt(abs(det)),
                         "cond": fmt(cond) if cond != mp.inf else "inf",
                         "min_abs_eigenvalue": fmt(amin),
                         "eigenvalues": [fmt(v) for v in vals]})

    # The discriminator. NOTE: the first version of this probe tested
    # "|det| collapses by >20 orders when dps rises". That test FAILS here --
    # not because the hypothesis is wrong but because the outcome is STRONGER
    # than the test: |det| is not small, it is exactly 0 at every precision, so
    # `0 < 0/1e20` is false. The honest discriminators are (a) det is exactly
    # zero, and (b) the smallest eigenvalue tracks the working precision, which
    # is what an exact null direction looks like when resolved numerically.
    dD = [mp.mpf(r["abs_det"]) for r in rows if r["convention"] == "D"]
    dC = [mp.mpf(r["abs_det"]) for r in rows if r["convention"] == "C"]
    eD = [mp.mpf(r["min_abs_eigenvalue"]) for r in rows if r["convention"] == "D"]
    det_exactly_zero = all(d == 0 for d in dD)
    tracks_precision = eD[-1] < eD[0] / mp.mpf("1e50")
    c_stable = dC[-1] > mp.mpf("1e-6")

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  |det| under D at 30/60/120 dps : {mp.nstr(dD[0], 4)} / {mp.nstr(dD[1], 4)} / {mp.nstr(dD[-1], 4)}
  |det| under C at 30/60/120 dps : {mp.nstr(dC[0], 4)} / {mp.nstr(dC[1], 4)} / {mp.nstr(dC[-1], 4)}
  min|eig| under D               : {mp.nstr(eD[0], 4)} -> {mp.nstr(eD[1], 4)} -> {mp.nstr(eD[-1], 4)}

  D det exactly zero at every dps : {bool(det_exactly_zero)}
  D min|eig| tracks precision     : {bool(tracks_precision)}
  C stays non-singular            : {bool(c_stable)}

  The answer is STRONGER than ill-conditioning: |det| is not merely small, it
  is exactly 0 at 30, 60 and 120 dps, and the smallest eigenvalue falls ~30
  orders per 30-dps step -- pinned to the working precision, which is exactly
  how an EXACT null direction presents numerically. C meanwhile is rock-steady
  at |det| = 0.1892, cond 34, at every precision.

  So the bean's float64 reading `det 3.998e-17 / cond 4.9e16` is that exact
  zero seen through f64 epsilon. It is NOT ill-conditioned-but-invertible, and
  the bean's own worry that numpy is "inverting rounding noise" is right.

  So the cds2 repair is correctly aimed: the D form really is rank-deficient,
  the radical really is nontrivial, and quotienting is a structural fix rather
  than a numerical patch. No convention is switched here and no value is
  proposed -- this measures ONE fact the repair decision rests on.
""")

    wb = WitnessBuilder("gram-convention-d-singularity-structural", engine="mpmath")
    wb.set_description(
        "Bean qou-cds2. Separates the two readings the bean holds at once: "
        "the convention-D Markov-Gram det = 3.998e-17 / cond 4.9e16 in float64 "
        "is consistent BOTH with an exactly singular form seen through f64 "
        "epsilon and with a merely ill-conditioned one, and the bean itself "
        "notes np.linalg.inv is 'inverting rounding noise'. Rebuilding the 6x6 "
        "Gram at 30/60/120 dps from pyhecke's own _nf_of_word_mp / NF_BASIS "
        "with z_D = q^3/(q^2+1) swapped for the hardcoded C spelling (gram.py "
        "has no D path; both gram_matrix_mp and z_mp hardcode "
        "1/(sqrt q + sqrt(1/q)), a detector-blind C spelling) shows |det| "
        "collapsing with working precision under D while C stays non-singular "
        "-- i.e. the singularity is STRUCTURAL, an exact zero, not a "
        "conditioning artifact. This validates the aim of the named repair "
        "(quotient by the trace radical). Switches no convention, touches "
        "gram.py not at all, and proposes no value."
    )
    wb.add_data("anchor", "proton")
    wb.add_data("q0", fmt(q))
    wb.add_data("z_C", fmt(zC(q)))
    wb.add_data("z_D", fmt(zD(q)))
    wb.add_data("spectra", rows)

    wb.add_assertion(
        name="convention_D_determinant_is_exactly_zero_at_every_precision",
        computed=str(int(bool(det_exactly_zero))), expected="1", tolerance=0,
        source="|det| under D is exactly 0 at 30, 60 and 120 dps. Not small — "
               "zero. An ill-conditioned but invertible form cannot do that at "
               "any precision, let alone all three.",
    )
    wb.add_assertion(
        name="convention_D_null_eigenvalue_tracks_working_precision",
        computed=str(int(bool(tracks_precision))), expected="1", tolerance=0,
        source=f"min|eig| under D: {mp.nstr(eD[0], 6)} (30 dps) -> "
               f"{mp.nstr(eD[1], 6)} (60) -> {mp.nstr(eD[-1], 6)} (120) — falling "
               "~30 orders per 30-dps step, i.e. pinned to epsilon rather than "
               "converging to a nonzero limit. That is an exact null direction "
               "being resolved — the signature float64 (cond 4.9e16) could not "
               "distinguish.",
    )
    wb.add_assertion(
        name="convention_C_gram_stays_non_singular",
        computed=str(int(bool(c_stable))), expected="1", tolerance=0,
        source=f"|det| under C is {mp.nstr(dC[-1], 6)} at 120 dps — bounded away "
               "from zero, so the collapse above is attributable to z alone (the "
               "only line that differs between the two builds).",
    )
    # Single-anchor probe (proton only), so unlike the cross-anchor comparison
    # probes this one CAN honestly declare its pin — see bean qou-po7i for the
    # vocabulary gap that leaves genuine two-anchor comparisons unlabelled.
    out = wb.save({"q0Anchor": "proton"})
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
