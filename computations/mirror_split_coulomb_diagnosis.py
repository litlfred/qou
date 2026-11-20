#!/usr/bin/env python3
"""
mirror_split_coulomb_diagnosis.py — the A=3 mirror binding split is COULOMB, so the
#2089 bond kernel's strong charge-splitting ε_nn−ε_pp = 2.27 MeV is a 3× overshoot.

Follow-up to the merged bond-extensivity work (#3557): that probe noted the DERIVED
A=3 mirror split B(³H)−B(³He) = ε_nn−ε_pp overshoots AME by ~3×. This diagnoses why.

The mirror split from the #2089 log-trace kernel is purely STRONG/categorical
(f_bond are Markov-trace factors, no EM):
    E₀·(ε_nn − ε_pp) = E₀·log(f_pp/f_nn),   E₀ = m_e/(q₀(q₀−1)),
    f_pp = z = q³/(q²+1),   f_nn = z − h = 1/(q³+q)   (convention D).

But the OBSERVED mirror split is essentially all COULOMB: ³He (Z=2) has one pp pair
that ³H (Z=1) lacks, and the pp Coulomb energy e²/(4πε₀·r) at the A=3 proton
separation r≈1.9 fm reproduces the whole 0.76 MeV (the textbook ³He–³H Coulomb
displacement energy). The model-independent strong-CSB residual is the ~0.07 MeV
Nolen–Schiffer anomaly (a realistic Coulomb subtraction leaves ~0.07; this script's
r≈1.9 fm point-charge estimate happens to leave a smaller +0.006). Either scale is
tiny: #2089's 2.27 MeV strong split overshoots by 3× (vs the total split), ~32× (vs
the physical Nolen–Schiffer residual), and ~400× (vs the point-charge residual).

Two readings (NOT decided here — a framework question):
  (A) the kernel's f_pp≠f_nn is spurious strong CSB; the strong bond should be
      charge-symmetric (f_pp≈f_nn) with Coulomb added separately; OR
  (B) the kernel's charge-dependence IS the categorical EM (QOU derives Coulomb from
      the bond structure), and it overshoots the Coulomb displacement energy by 3×.

Either way: light-nuclei binding improves by charge-symmetrising the strong bond and
sourcing the mirror split from Coulomb — and (bonus) f_pp≈f_nn collapses the 1.78×
nucleon ε spread, restoring the equal-weight limit that makes coordination-number
counting valid at the nucleon level (merged #3557).

EXPLORATORY — scope-limited (a). Diagnosis + fix direction, NOT a re-derivation of
the kernel. Uses #2089 f_bond + textbook Coulomb; no new fit; no production wiring.
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV, _ame_binding_mev  # noqa: E402
from coulomb_energy import alpha_em_hbar_c_mev_fm  # noqa: E402 — shared e²/(4πε₀)=α·ħc source
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
q = Q_MP

# e²/(4πε₀) = α·ħc, the shared repo constant (computations/coulomb_energy.py).
# `ALPHA_HBAR_C_MEV_FM` (the hard-coded CODATA 1.43996) was drained from
# coulomb_energy in favour of the DERIVED, parameter-free
# `alpha_em_hbar_c_mev_fm()`, which routes through
# `meson_em_sinh_closed_form._alpha_em_inv_derived`. This probe still imported
# the removed name and so could not run at all -- a pre-existing ImportError
# on main, not a consequence of the convention migration.
E2_OVER_4PIEPS0_MEV_FM = alpha_em_hbar_c_mev_fm()
# physical strong-CSB scale: the ³He–³H Nolen–Schiffer anomaly ≈ 0.07 MeV — the
# model-independent residual after a realistic (not point-charge) Coulomb subtraction.
NOLEN_SCHIFFER_MEV = mp.mpf("0.07")


def main() -> int:
    # ── derived #2089 strong mirror split ─────────────────────────────────────
    # Convention D: z = q^3/(q^2+1). The kernel is STRUCTURAL --
    # f_pp = z, f_nn = z - h, f_pn = z - h/2 (#2089) -- and these lines
    # previously carried the C-substituted EXPANSION of exactly that, which is
    # where the q^{3/2} came from. Writing the structural form instead both
    # migrates the convention and removes the expansion: under D every factor
    # is rational, because D never leaves Q(q).
    #
    #     f_pp = q^3/(q^2+1)      f_nn = 1/(q^3+q)      f_pn = (q^4+1)/(2q(q^2+1))
    z = q ** 3 / (q ** 2 + 1)
    h = q - 1 / q
    f_pp = z
    f_nn = z - h
    f_pn = z - h / 2
    E0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    strong_split = E0 * (mp.log(1 / f_nn) - mp.log(1 / f_pp))   # = E₀(ε_nn−ε_pp)

    # ── observed AME mirror split ─────────────────────────────────────────────
    split_ame = mp.mpf(str(_ame_binding_mev(1, 3))) - mp.mpf(str(_ame_binding_mev(2, 3)))

    # ── Coulomb pp displacement energy (point pair at A=3 proton separation) ───
    #   ³He has one pp pair ³H lacks; r ≈ 1.7–2.2 fm brackets the A=3 charge radius.
    print(f"  q₀={float(q):.5f}   E₀={float(E0):.4f} MeV")
    print(f"  f_pp={float(f_pp):.6f}  f_nn={float(f_nn):.6f}\n")
    print("### Observed A=3 mirror split is COULOMB")
    print(f"  AME  B(³H)−B(³He) = {float(split_ame):.4f} MeV")
    print("  pp Coulomb displacement  e²/(4πε₀·r):")
    coul = {}
    for r in ("1.7", "1.9", "2.0", "2.2"):
        c = E2_OVER_4PIEPS0_MEV_FM / mp.mpf(r)
        coul[r] = float(c)
        print(f"     r={r} fm : {float(c):.4f} MeV")
    coul_best = coul["1.9"]
    strong_residual = float(split_ame) - coul_best
    print(f"  ⇒ Coulomb at r≈1.9 fm ({coul_best:.3f}) reproduces the whole split "
          f"({float(split_ame):.3f}); point-charge residual ≈ {strong_residual:+.3f} MeV")
    print(f"    (model-independent strong-CSB = the ~{float(NOLEN_SCHIFFER_MEV):.2f} MeV "
          "Nolen–Schiffer anomaly; charge symmetry holds to ~1%).\n")

    # ── the overshoot ─────────────────────────────────────────────────────────
    over_total = float(strong_split / split_ame)
    over_ns = float(strong_split / NOLEN_SCHIFFER_MEV)             # vs physical NS residual
    over_pc = abs(float(strong_split) / strong_residual) if strong_residual else float("inf")
    print("### The #2089 kernel STRONG mirror split overshoots")
    print(f"  E₀·(ε_nn−ε_pp) = {float(strong_split):.3f} MeV  (pure strong/categorical)")
    print(f"  ⇒ {over_total:.1f}× the TOTAL observed split;  ~{over_ns:.0f}× the physical "
          f"(Nolen–Schiffer) strong residual;  ~{over_pc:.0f}× the point-charge residual.")
    print("    Either way the kernel over-breaks charge symmetry.")

    print("\n### Reading — two framings (not decided; framework question)")
    print("  (A) f_pp≠f_nn is spurious strong CSB ⇒ charge-symmetrise (f_pp≈f_nn) and add")
    print("      Coulomb separately (Z(Z−1)/2 pairs × e²/(4πε₀r)); OR")
    print("  (B) the kernel's charge-dependence IS the categorical EM, overshooting the")
    print("      Coulomb displacement energy by ~3×.")
    print("  Either way, light-nuclei binding improves by sourcing the mirror split from")
    print("  Coulomb, not the strong kernel. BONUS: f_pp≈f_nn collapses the 1.78× nucleon")
    print("  ε-spread, restoring the equal-weight limit that makes coordination-number")
    print("  counting valid at the nucleon level (merged #3557). Scope-(a) diagnosis.")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("mirror-split-coulomb-diagnosis", engine="mpmath")
            wb.set_description(
                "The A=3 mirror binding split B(³H)−B(³He)=0.764 MeV is reproduced by the pp "
                "Coulomb displacement energy (e²/4πε₀r at r≈1.9 fm = 0.758 MeV), so strong CSB "
                "is ~0 (model-independent strong residual = the ~0.07 MeV Nolen–Schiffer "
                "anomaly). The #2089 log-trace kernel assigns a STRONG mirror split "
                "E₀(ε_nn−ε_pp)=2.27 MeV — 3× the total split, ~32× the Nolen–Schiffer residual "
                "(~400× the point-charge residual) — over-breaking charge symmetry. Fix "
                "direction: charge-symmetric strong bond (f_pp≈f_nn) + separate Coulomb; this "
                "also collapses the 1.78× nucleon ε-spread, restoring equal-weight coordination "
                "counting (#3557). Scope-(a) diagnosis, no re-derivation, no wiring.")
            wb.add_data("q0", float(q))
            wb.add_data("E0_MeV", float(E0))
            wb.add_data("ame_mirror_split_MeV", float(split_ame))
            wb.add_data("coulomb_pp_MeV_by_r", coul)
            wb.add_data("point_charge_residual_MeV", strong_residual)
            wb.add_data("nolen_schiffer_residual_MeV", float(NOLEN_SCHIFFER_MEV))
            wb.add_data("kernel_strong_split_MeV", float(strong_split))
            wb.add_data("overshoot_vs_total", over_total)
            wb.add_data("overshoot_vs_nolen_schiffer", over_ns)
            wb.add_assertion(
                name="mirror_split_is_coulomb_kernel_strong_csb_overshoots_3x",
                computed=str(int(2.5 < over_total < 3.5)), expected="1", tolerance=0,
                source=(f"AME split {float(split_ame):.3f} ≈ pp Coulomb {coul_best:.3f} (r≈1.9 fm) "
                        f"⇒ strong CSB ≈{strong_residual:+.3f}; #2089 strong split "
                        f"{float(strong_split):.3f} = {over_total:.1f}× total ⇒ kernel over-breaks "
                        "charge symmetry. Fix: charge-symmetric strong bond + separate Coulomb."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
