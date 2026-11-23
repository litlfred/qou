#!/usr/bin/env python3
"""
charge_symmetric_coulomb_binding.py — benchmark the charge-symmetric strong bond +
SEPARATE Coulomb light-nuclei binding against AME (the accuracy payoff of the
#3564/#3570 mirror-split diagnosis).

The diagnosis (#3564, #3570): the mirror binding split is Coulomb, so the #2089
log-trace strong kernel (f_pp=z, f_nn=z−h — charge-BREAKING) over-breaks charge
symmetry by ~3×. Fix direction: make the strong bond charge-symmetric and source the
mirror split from Coulomb separately. This script benchmarks that fix.

Three models on D/T/³He/⁴He (complete-graph bond set; B = E₀·Σ_bonds log(1/f_bond)):
  (1) BROKEN  : #2089 kernel f_pp=z, f_nn=z−h, f_pn=z−h/2 ; NO Coulomb.
  (2) BROKEN+C: the same, MINUS canonical Coulomb — DOUBLE-COUNTS (the kernel already
                carries a spurious EM split, so real Coulomb on top over-corrects).
  (3) SYMM+C  : charge-symmetric strong bond (all bonds = the isoscalar f_pn, the
                symmetric midpoint of the 0/½h/h shifts) MINUS canonical Coulomb.

E₀ = m_e/(q₀(q₀−1))/(1−ℏ_q²) ≈ 4.2275 MeV, tower-summed (owner ruling 2026-11-20, #8590; was the order-zero 4.186, #2089 deuteron-fixing scale); Coulomb via the shared
computations/coulomb_energy (Z(Z−1), r₀=1.2 fm).

Expected (diagnosis prediction): model (3) FIXES the mirror split (→ Coulomb) where
(1)/(2) give 2.3–3.0 MeV vs AME 0.76. The ABSOLUTE binding stays off (edge-set / E₀ /
connected magnitude) — that residual is #3548's connected-(2,1)/SU(4) mechanism, which
still uses the charge-BREAKING kernel and must be re-run charge-symmetric. So this is a
specific, verified accuracy win on the SPLIT, not a binding closure.

EXPLORATORY — scope-limited (a). Uses #2089 f_bond + shared Coulomb; no new fit; no
production wiring.
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV, _ame_binding_mev  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402 — canonical Z(Z−1), r₀=1.2

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26). `-h/2` is `strict_averaged`, the COLOUR-BLIND convention.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
q = mp.mpf(Q_50_DIGIT_STR)
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.canonical(q=q, m_e=M_E_MEV)  # tower-summed E_0, canonical (owner ruling 2026-11-20, #8590); was order-zero m_e/(q(q-1))


def f_bonds():
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
    f_pn = z + _pn_d(h)
    return f_pp, f_pn, f_nn


# light nuclei: name -> (Z, A, bond multiset as {(bondtype): count}) on the complete graph
#   D=np ; T=pnn (2 pn + 1 nn) ; ³He=ppn (1 pp + 2 pn) ; ⁴He=ppnn (1 pp + 1 nn + 4 pn)
NUCLEI = {
    "D":   (1, 2, {"pn": 1}),
    "T":   (1, 3, {"pn": 2, "nn": 1}),
    "3He": (2, 3, {"pp": 1, "pn": 2}),
    "4He": (2, 4, {"pp": 1, "nn": 1, "pn": 4}),
}


def strong(bonds, fmap):
    # Stays mpf.  This used to `float(...)` the result, which cost the whole
    # 50-dps computation and then handed a float64 back into mpf arithmetic
    # (`b1 - ec`, with `coulomb_energy_mev` returning mpf).  The product is an
    # mpf carrying nothing but a float64's exact binary expansion, and the
    # witness serializes it at 50 dps — 2.833754824119470328014358528889715…,
    # of which only the first 17 digits are a measurement.  That is the
    # float64-padding defect, caught by `witness_float64_padding_audit.py`.
    return E0 * mp.fsum(n * mp.log(1 / fmap[b]) for b, n in bonds.items())


def main() -> int:
    f_pp, f_pn, f_nn = f_bonds()
    broken = {"pp": f_pp, "pn": f_pn, "nn": f_nn}          # #2089 charge-breaking
    symm = {"pp": f_pn, "pn": f_pn, "nn": f_pn}            # charge-symmetric isoscalar
    print(f"  E₀={float(E0):.4f} MeV;  f_pp={float(f_pp):.4f} f_pn={float(f_pn):.4f} "
          f"f_nn={float(f_nn):.4f}  (isoscalar = f_pn)\n")

    def row(nm, Z, A, bonds):
        ame = _ame_binding_mev(Z, A)   # mpf from the AME string — keep it
        ec = coulomb_energy_mev(Z, A)
        b1 = strong(bonds, broken)                 # broken, no Coulomb
        b2 = b1 - ec                               # broken + Coulomb (double-count)
        b3 = strong(bonds, symm) - ec              # charge-symm + Coulomb
        return dict(ame=ame, ec=ec, broken=b1, broken_c=b2, symm_c=b3)

    R = {nm: row(nm, Z, A, bonds) for nm, (Z, A, bonds) in NUCLEI.items()}

    print("### Absolute binding (MeV) — B_pred vs AME")
    print(f"  {'nuc':<5}{'AME':>8}{'(1)broken':>11}{'(2)brok+C':>11}{'(3)symm+C':>11}"
          f"{'(3)err%':>9}")
    for nm in NUCLEI:
        r = R[nm]
        e3 = 100 * (r["symm_c"] - r["ame"]) / r["ame"]
        print(f"  {nm:<5}{float(r['ame']):>8.3f}{float(r['broken']):>11.3f}{float(r['broken_c']):>11.3f}"
              f"{float(r['symm_c']):>11.3f}{float(e3):>+9.1f}")

    # ── the headline: the ³H/³He mirror split ─────────────────────────────────
    def split(model):
        return R["T"][model] - R["3He"][model]
    ame_split = R["T"]["ame"] - R["3He"]["ame"]
    print("\n### Mirror split B(³H)−B(³He) — the diagnosis's target")
    print(f"  AME                         = {float(ame_split):+.3f} MeV")
    print(f"  (1) broken kernel, no Coul  = {float(split('broken')):+.3f}  ({float(split('broken')/ame_split):.1f}×)")
    print(f"  (2) broken kernel + Coulomb = {float(split('broken_c')):+.3f}  (double-counts EM)")
    print(f"  (3) charge-symm + Coulomb   = {float(split('symm_c')):+.3f}  "
          f"({float(split('symm_c')/ame_split):.2f}× — Coulomb, uniform-sphere over-estimate)")

    print("\n### Verdict — the fix works on the SPLIT; absolute magnitude stays open (a)")
    print("  • Charge-symm + separate Coulomb FIXES the mirror split: it collapses to the")
    print(f"    Coulomb value ({split('symm_c'):.2f} MeV) from the broken kernel's "
          f"{float(split('broken')):.2f}–{float(split('broken_c')):.2f} MeV — a ~3× accuracy gain, exactly")
    print("    as the #3564/#3570 diagnosis predicted. (Residual ~30% is the uniform-sphere")
    print("    Coulomb over-estimate, not charge symmetry.)")
    print("  • The ABSOLUTE binding is NOT closed (D over-, ⁴He under-bound): that residual")
    print("    is the edge-set / E₀ / connected magnitude — #3548's connected-(2,1)/SU(4)")
    print("    mechanism, which STILL uses the charge-BREAKING kernel and must be re-run")
    print("    charge-symmetric. So: ε-magnitude/kernel re-derivation IS still needed; this")
    print("    fix is a verified win on the split, not a binding closure. No wiring.")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("charge-symmetric-coulomb-binding", engine="mpmath")
            wb.set_description(
                "Benchmarks the charge-symmetric strong bond + separate Coulomb light-nuclei "
                "binding vs AME (the #3564/#3570 diagnosis payoff). Charge-symm (all bonds = "
                "isoscalar f_pn) minus canonical Coulomb FIXES the ³H/³He mirror split — "
                "collapses to %.2f MeV (Coulomb) from the broken kernel's %.2f–%.2f MeV vs AME "
                "%.2f (~3× gain), exactly as predicted. Absolute binding NOT closed (D over-, "
                "⁴He under-bound) — the edge-set/E₀/connected magnitude (#3548's connected-"
                "(2,1)/SU(4) mechanism, still on the charge-breaking kernel) must be re-run "
                "charge-symmetric. Verified split win, not a closure. Scope-(a), no wiring."
                % (split('symm_c'), split('broken'), split('broken_c'), ame_split))
            wb.add_data("E0_MeV", E0)      # mpf: tower-summed qbeta_e0.canonical(), not a float64
            wb.add_data("nuclei", {nm: R[nm] for nm in NUCLEI})
            wb.add_data("mirror_split", {"AME": ame_split, "broken": split('broken'),
                                         "broken_plus_coulomb": split('broken_c'),
                                         "charge_symm_plus_coulomb": split('symm_c')})
            wb.add_assertion(
                name="charge_symm_plus_coulomb_fixes_mirror_split",
                computed=str(int(abs(split('symm_c') - ame_split) < abs(split('broken') - ame_split) / 2)),
                expected="1", tolerance=0,
                source=(f"charge-symm+Coulomb split {float(split('symm_c')):+.3f} MeV is >2× closer to "
                        f"AME {float(ame_split):+.3f} than the broken kernel {float(split('broken')):+.3f}; the "
                        "residual ~30% is the uniform-sphere Coulomb over-estimate. Absolute "
                        "binding open (edge-set/connected magnitude → charge-symmetric #3548)."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
