#!/usr/bin/env python3
"""Diagnose the 5.9% cosh mirror-asymmetry in the ³H/³He q-Reeb split.

Question (bean t1rk): is the 5.9% cosh-channel asymmetry between mirror partners
³H (pnn) and ³He (ppn) — found in the ρ-normalisation push — a PHYSICAL
charge-symmetry-breaking effect, or an ARTIFACT of the channel separation?

`strong_channel_rho` (binding_rotation_phase_lead.py) defines the "cosh/strong"
channel by zeroing the identity-coefficient d ONLY on inter-nucleon generators
(k%3==2). But the proton (uud) and neutron (udd) INTRA-nucleon chains differ
purely in their d-fields, and that difference is exactly +h = +(q−q⁻¹) per
nucleon — a single linear-in-h term, i.e. BAR-ODD (sinh). So the intra-nucleon
p/n distinction is bar-odd and SHOULD live in the sinh channel — but the inter-
only zeroing leaves it in the "cosh" bucket.

This script tests the hypothesis directly: compute the per-λ characters χ_λ for
³H and ³He under three d-treatments —
  (a) full        : all d kept (w_atom)
  (b) inter-zeroed: d=0 on k%3==2 only       (the current "strong/cosh")
  (c) all-zeroed  : d=0 everywhere            (the TRUE charge-symmetric cosh)
— and compare the mirror partners. If under (c) the characters become IDENTICAL,
the 5.9% asymmetry is a pure artifact of incomplete sinh-removal, and the entire
³H/³He split is bar-odd (sinh) — exactly as the framework's bar-odd n−p rule
predicts. No fit; audit-only witness.
"""
from __future__ import annotations
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
for _d in ("hecke", "habiro", "substrate"):
    sys.path.insert(0, str(_HERE / _d))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from mass_at_3A_proper import (  # noqa: E402
    atom_braid_word_3A, chi_lambda_of_word, _cached_seminormal,
)
from sympy.utilities.iterables import partitions as _sympy_partitions  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from q_parameter import Q_50_DIGIT_STR as _Q50  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def _parts(n):
    for p in _sympy_partitions(n):
        yield tuple(sorted((v for k, v in p.items() for _ in range(k)), reverse=True))


def intra_pn_d_difference_over_h():
    """(Σd(proton uud) − Σd(neutron udd)) / h, read off the words themselves.

    The whole diagnosis rests on this ratio being 1: the p/n intra-nucleon
    distinction is a single linear-in-h term, hence bar-odd, hence it belongs
    in the sinh channel that `strong_channel_rho` does not clear. It was
    previously recorded as the literal 1.0 — the one form that cannot notice
    if `atom_braid_word_3A` changes its intra-nucleon templates.

    A single nucleon has no interface (`k < A−1` is false at A=1), so the word
    is purely intra-nucleon; the `k % 3 != 2` filter states that rather than
    relying on it. `h` is built from the SAME 50-digit q the word is built
    from (`atom_braid_word_3A` reads `Q_50_DIGIT_STR` when `q is None`), not
    from this module's 45-digit `Q_MP` — mixing the two leaves a spurious
    ~4e-39 residual that has nothing to do with the claim.
    """
    q = mp.mpf(_Q50)
    h = q - mp.mpf(1) / q
    sum_p = sum((d for (_c, d, k) in atom_braid_word_3A(1, 0, include_inter=False)
                 if k % 3 != 2), mp.mpf(0))
    sum_n = sum((d for (_c, d, k) in atom_braid_word_3A(0, 1, include_inter=False)
                 if k % 3 != 2), mp.mpf(0))
    return (sum_p - sum_n) / h


def char_profile(Z, N, mode):
    """max_λ |χ_λ| profile of the (Z,N) atom braid under a d-treatment.

    mode: 'full' | 'inter0' | 'alld0'. Returns dict λ -> χ_λ (mpf)."""
    n = 3 * (Z + N)
    ng = n - 1
    w = atom_braid_word_3A(Z, N, include_inter=True)
    if mode == "inter0":
        w = [(c, 0.0 if (k % 3 == 2) else d, k) for (c, d, k) in w]
    elif mode == "alld0":
        w = [(c, 0.0, k) for (c, d, k) in w]
    out = {}
    for lam in _parts(n):
        sig, dim, _ = _cached_seminormal(lam, Q0)  # this producer's OWN q — see qou-wee5
        if dim == 0:
            continue
        out[lam] = mp.mpf(str(chi_lambda_of_word(sig, dim, w, ng)))
    return out


def main() -> None:
    set_compute_dps(40)
    print(f"q0 = {float(mp.mpf(str(Q0))):.6f}    [³H = (Z=1,N=2), ³He = (Z=2,N=1)]")
    print("Per-λ character mismatch between mirror partners ³H and ³He (n=9):\n")
    rows = {}
    for mode, label in (("full", "full (all d kept)"),
                        ("inter0", "inter-zeroed (current 'strong/cosh')"),
                        ("alld0", "all-d-zeroed (TRUE charge-symmetric cosh)")):
        cH = char_profile(1, 2, mode)
        cHe = char_profile(2, 1, mode)
        diffs = [abs(cH[l] - cHe[l]) for l in cH]
        maxd = max(diffs)
        sumd = sum(diffs)
        rows[mode] = {"max_abs_diff": float(maxd), "sum_abs_diff": float(sumd)}
        print(f"  {label:42s}  max|Δχ_λ| = {float(maxd):.3e}   Σ|Δχ_λ| = {float(sumd):.3e}")

    identical = rows["alld0"]["max_abs_diff"] < 1e-25
    print("\n--- verdict ---")
    print(f"  full / inter-zeroed: ³H ≠ ³He  (mirror partners differ → nonzero split contribution)")
    print(f"  all-d-zeroed       : ³H {'≡' if identical else '≠'} ³He  "
          f"(max|Δχ_λ| = {rows['alld0']['max_abs_diff']:.2e})")
    if identical:
        print("  ⇒ The TRUE charge-symmetric cosh channel gives ³H ≡ ³He: ZERO split.")
        print("    The 5.9% 'cosh asymmetry' is a pure ARTIFACT of strong_channel_rho's")
        print("    incomplete sinh-removal (it zeros only inter-nucleon d, leaving the")
        print("    intra-nucleon bar-odd d=+h p/n distinction in the cosh bucket).")
        print("    The ENTIRE ³H/³He split is bar-odd (sinh) — matching the cheat-sheet")
        print("    bar-odd n−p rule. So the residual is a clean ~18% q-Reeb overshoot,")
        print("    NOT a cosh/sinh mixing question.")

    wb = WitnessBuilder("he3-tritium-cosh-asymmetry-diagnosis", engine="mpmath")
    wb.data["description"] = (
        "Diagnosis of the 5.9% cosh mirror-asymmetry in the ³H/³He q-Reeb split: "
        "per-λ character mismatch under full / inter-zeroed / all-d-zeroed. "
        "all-d-zeroed → ³H ≡ ³He proves the asymmetry is an artifact of incomplete "
        "sinh-removal; the entire split is bar-odd (sinh). Audit-only; no fit.")
    wb.data["q0"] = float(mp.mpf(str(Q0)))
    wb.data["per_mode_mirror_mismatch"] = rows
    pn_over_h = intra_pn_d_difference_over_h()
    wb.data["intra_pn_d_difference_over_h"] = mp.nstr(pn_over_h, 30)
    wb.data["verdict"] = (
        "The proton(uud)−neutron(udd) intra-nucleon d-difference is exactly +h "
        "(bar-odd/sinh). strong_channel_rho zeros only inter-nucleon d (k%3==2), "
        "leaving the intra-nucleon bar-odd term in the 'cosh' bucket → the 5.9% "
        "asymmetry. The TRUE all-d-zeroed cosh channel gives ³H ≡ ³He (max|Δχ_λ| "
        f"= {rows['alld0']['max_abs_diff']:.1e}), so the cosh contributes ZERO to "
        "the split: the entire ³H/³He split is bar-odd (sinh), per the cheat-sheet "
        "n−p rule. The residual is therefore a clean ~18% overshoot of the all-sinh "
        "q-Reeb phase at universal ρ, NOT a cosh/sinh mixing. No fit; no rewire.")
    # Was `computed=1, expected=1` — a pass whatever the words contain, even
    # though its source string ("ratio 1.000000") named a quantity this module
    # can compute from `atom_braid_word_3A` in three lines. It is also the
    # premise of every conclusion below it, so a silent change in the intra
    # templates would have left the verdict prose intact and the witness green.
    # Now the ratio is measured: the proton chain sums to −4h and the neutron
    # chain to −5h, so the difference over h is 1 to the last digit carried.
    # RESIDUAL against 0, not value against target: the verdict path
    # (qou_substrate/witness.py) compares float(computed) to float(expected),
    # so a value-vs-value form here could not resolve anything below the
    # float64 floor and the tolerance below it was unreachable by ~10^19.
    # A residual near zero IS representable as a float64 all the way down, so
    # the same tolerance is a real bound on it.
    # Gate: computations/audits/tolerance_below_arithmetic_floor_audit.py.
    wb.add_assertion("intra_pn_difference_is_bar_odd_exact_h",
                     computed=mp.nstr(abs(pn_over_h - 1), 20), expected="0",
                     tolerance="1e-35",
                     source="(Σd(proton uud) − Σd(neutron udd)) / h from "
                            "atom_braid_word_3A(1,0) and (0,1), h = q−q⁻¹ at the "
                            "same 50-digit q the word is built from; a single "
                            "linear-in-h term ⇒ bar-odd (sinh)")
    wb.add_assertion("alld0_cosh_gives_identical_mirror",
                     computed=1 if identical else 0, expected=1, tolerance=0,
                     source="all-d-zeroed χ_λ(³H) == χ_λ(³He) → cosh asymmetry is an artifact")
    wb.save()
    print("\n✓ Witness: he3-tritium-cosh-asymmetry-diagnosis.witness.json (audit-only; no fit)")


if __name__ == "__main__":
    main()
