"""α_em substrate Coulomb-channel probe — Item 2 of PR #1708.

`prop:cosh-sinh-q-bridge` (#1417): [n]_q = sinh(nλ)/sinh(λ) where the
sinh channel is the COULOMB channel and cosh is the confinement
channel, with q = e^λ ⟹ λ = ln(q).

The α_em tree term q·[9]_q·[10]_q is ALREADY a pure-sinh (Coulomb)
form. This probe tests whether the Coulomb (sinh) channel, carried to
the NEXT structural order through the Wedderburn decomposition,
produces the open `2/(3π)` shift and/or the `[2]_q/(8π)·(1−h²α)`
self-energy — i.e. whether the canonical chain
`cat action → (sinh Coulomb channel) → Wedderburn` closes α_em.

## The cosh/sinh bridge

  λ = ln(q_0)                     (q_0 ≈ 1.10998 ⟹ λ ≈ 0.10437)
  [n]_q = sinh(nλ)/sinh(λ)        (Coulomb channel)
  cosh(nλ)                        (confinement channel)

## What this probe tests (derive-or-refute)

1. Confirm [n]_q = sinh(nλ)/sinh(λ) numerically (sanity).
2. Test whether the COULOMB-channel self-energy — the natural
   2nd-order sinh correction — reproduces 2/(3π) or the self-energy:
     candidate forms built from sinh/cosh(λ), the Wedderburn dims,
     and the 1-loop QED prefactor 1/π.
3. The Coulomb channel's natural "vacuum polarization" analog: does
   the sinh-channel 2-point function at the 3 H_3 Wedderburn blocks
   give the 2/(3π) coefficient (3 = N_blocks = N_cusps)?

## Pre-stated failure signature

If the sinh-channel higher-order forms do not reproduce 2/(3π) or the
self-energy with a structural (non-fitted) coefficient, the
Coulomb-channel route is refuted — α_em's CORRECTIONS are not pure
Coulomb-channel objects (consistent with the RT-2-loop track treating
the self-energy as a separate fermion-loop primitive).

## Cross-references

- prop:cosh-sinh-q-bridge (#1417)
- prop:em-coupling-bring-zero-mode (tree term)
- alpha_em_multicell_yekutieli_probe.py (Item 1, shift REFUTED)
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Puts the flat computations/ dir + cluster subdirs on sys.path so
# flat-namespace imports resolve from the probes/ subdirectory.
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys  # noqa: E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def qint(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def main() -> int:
    DPS = 50
    set_compute_dps(DPS)
    q = q_at(DPS)
    lam = mp.log(q)  # λ = ln(q_0)

    print("=" * 78)
    print("α_em substrate Coulomb-channel probe (item 2 of PR #1708)")
    print("=" * 78)
    print(f"\nq_0 = {q_str(40)} (display)")
    print(f"λ = ln(q_0) = {mp.nstr(lam, 18)}\n")

    # Sanity: [n]_q = sinh(nλ)/sinh(λ)
    print(f"[Sanity — cosh/sinh bridge: [n]_q = sinh(nλ)/sinh(λ)]")
    ok = True
    for n in [2, 3, 9, 10]:
        bracket = qint(n, q)
        sinh_form = mp.sinh(n * lam) / mp.sinh(lam)
        diff = abs(bracket - sinh_form)
        ok = ok and diff < mp.mpf("1e-40")
        print(f"  [{n}]_q = {mp.nstr(bracket, 12)}  sinh-form = {mp.nstr(sinh_form, 12)}  Δ={mp.nstr(diff, 4)}")
    print(f"  bridge verified: {ok}")

    # Targets
    shift_target = mp.mpf(2) / (3 * mp.pi)
    codata_inv = mp.mpf("137.035999084")
    alpha = 1 / codata_inv
    h = q - 1 / q
    se_target = qint(2, q) / (8 * mp.pi) * (1 - h ** 2 * alpha)
    print(f"\n[Targets]")
    print(f"  shift  2/(3π)              = {mp.nstr(shift_target, 15)}")
    print(f"  self-energy [2]_q/(8π)(1-h²α)= {mp.nstr(se_target, 15)}")

    # ── Coulomb-channel candidate forms for the SHIFT 2/(3π) ──
    # The QED 1-loop vacuum-polarization coefficient is 2/(3π) in the
    # standard Uehling/running-coupling β-function: Δ(α⁻¹) ~ (2/3π)·ln(...).
    # Test whether the sinh-channel reproduces the 2/3 numerator
    # structurally (3 = N_cusps = N_Wedderburn-blocks at H_3).
    print(f"\n[Coulomb-channel candidates for 2/(3π) shift]")
    N_blocks_H3 = 3  # trivial, standard, sign
    candidates_shift = [
        # The QED β-function coefficient is literally 2/(3π) for a single
        # charged fermion — this is the standard result, here interpreted
        # as N_blocks=3.
        ("2/(N_blocks·π), N_blocks=3 [QED β-fn]",
         mp.mpf(2) / (N_blocks_H3 * mp.pi)),
        # sinh-channel: 2·sinh(λ)/(3π·sinh(λ)) — sinh cancels (taut check)
        ("2·sinh(λ)/(3π·sinh(λ)) [sinh cancels]",
         2 * mp.sinh(lam) / (3 * mp.pi * mp.sinh(lam))),
        # genuine sinh: tanh(λ)/(something) — non-tautological
        ("tanh(λ)/(π·λ)·(2/3)·... [genuine λ-form]",
         mp.tanh(lam) / (mp.pi * lam) * mp.mpf(2) / 3),
        # cosh-corrected
        ("(2/3π)·cosh(λ) [confinement-corrected]",
         mp.mpf(2) / (3 * mp.pi) * mp.cosh(lam)),
    ]
    for name, val in candidates_shift:
        rel = (val - shift_target) / shift_target * 100
        mark = " ⭐⭐" if abs(rel) < mp.mpf("0.01") else (" *" if abs(rel) < 5 else "")
        print(f"  {name:<44}{mp.nstr(val, 12):<16}Δ%={mp.nstr(rel, 6)}{mark}")

    # ── Coulomb-channel candidate forms for the SELF-ENERGY ──
    print(f"\n[Coulomb-channel candidates for [2]_q/(8π)·(1−h²α) self-energy]")
    candidates_se = [
        # the form itself (taut)
        ("[2]_q/(8π)·(1−h²α) [target verbatim]",
         qint(2, q) / (8 * mp.pi) * (1 - h ** 2 * alpha)),
        # sinh-channel [2]_q with cosh damping instead of (1-h²α)
        ("[2]_q/(8π)·1/cosh(λ)²",
         qint(2, q) / (8 * mp.pi) / mp.cosh(lam) ** 2),
        # pure sinh self-energy: sinh(2λ)/(8π·sinh(λ))
        ("sinh(2λ)/(8π·sinh λ) = [2]_q/(8π)",
         mp.sinh(2 * lam) / (8 * mp.pi * mp.sinh(lam))),
        # 2-loop alpha-suppressed natural form
        ("α·[2]_q/(8π) [α-suppressed]",
         alpha * qint(2, q) / (8 * mp.pi)),
    ]
    for name, val in candidates_se:
        rel = (val - se_target) / se_target * 100
        mark = " ⭐⭐" if abs(rel) < mp.mpf("0.01") else (" *" if abs(rel) < 5 else "")
        print(f"  {name:<44}{mp.nstr(val, 12):<16}Δ%={mp.nstr(rel, 6)}{mark}")

    # ── Verdict ──
    print(f"\n[Verdict]")
    # The honest finding: 2/(3π) is the STANDARD QED vacuum-polarization
    # β-function coefficient for a single charged fermion. The "3" in the
    # framework reads as N_blocks=3 at H_3 (= N_cusps of Borromean), which
    # is a CONSISTENT interpretation but the 2/(3π) value itself is the
    # textbook QED 1-loop result, not a NEW categorical derivation.
    verdict = (
        "PARTIAL / INTERPRETIVE. The cosh/sinh bridge is verified "
        "([n]_q = sinh(nλ)/sinh(λ) to 1e-40). The tree term IS a pure "
        "Coulomb-channel (sinh) object, confirming the chain "
        "`cat action → sinh channel → Wedderburn` produces the LEADING "
        "α_em⁻¹. For the CORRECTIONS:\n"
        "  • The 2/(3π) shift coincides with the STANDARD QED 1-loop "
        "vacuum-polarization β-function coefficient (2/3π per charged "
        "fermion). The framework's '3' admits a CONSISTENT reading as "
        "N_blocks=3 at H_3 (= N_cusps of the Borromean complement), but "
        "the value 2/(3π) is the textbook QED result, not a NEW "
        "categorical derivation — genuine λ-dependent sinh forms "
        "(tanh(λ)/(πλ)-type) do NOT match.\n"
        "  • The self-energy [2]_q/(8π)·(1−h²α): the [2]_q numerator IS "
        "a Coulomb-channel (sinh(2λ)/sinh(λ)) object, but the (1−h²α) "
        "Schwinger factor is NOT a pure Coulomb-channel form (cosh⁻² "
        "damping misses). This factor is the RT-2-loop track's target.\n"
        "NET: the Coulomb channel structurally explains the TREE term and "
        "the [2]_q numerator of the self-energy, and gives a consistent "
        "N_blocks=3 reading of the 2/(3π) shift — but does NOT "
        "independently DERIVE the 2/(3π) coefficient or the (1−h²α) "
        "factor. Those remain the QED-vacuum-polarization import + the "
        "RT-2-loop Schwinger derivation respectively. Consistent with "
        "Item 1 (multi-cell summed Yekutieli also could not derive the "
        "shift coefficient)."
    )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder("alpha-em-coulomb-channel-probe", engine="python")
    w.set_description(
        "Item 2 of PR #1708: tests whether the sinh (Coulomb) channel of "
        "prop:cosh-sinh-q-bridge, through Wedderburn, derives the α_em "
        "2/(3π) shift and [2]_q/(8π)·(1−h²α) self-energy. Confirms tree "
        "term + [2]_q numerator are Coulomb-channel; shift coeff and "
        "Schwinger factor are not independently derived."
    )
    w.add_parameter("q_50dps", q_str(DPS))
    w.add_parameter("lambda_ln_q", mp.nstr(lam, 25))
    w.add_data("cosh_sinh_bridge_verified", ok)
    w.add_data("shift_target", mp.nstr(shift_target, 25))
    w.add_data("self_energy_target", mp.nstr(se_target, 25))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="cosh_sinh_bridge_verified",
        computed=ok,
        expected=True,
        tolerance=0,
        source="[n]_q = sinh(nλ)/sinh(λ) verified to 1e-40 for n in {2,3,9,10}.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
