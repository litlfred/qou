#!/usr/bin/env python3
"""qbeta_g3_annihilator_certification.py — A_ω step 1, tranche 3: certify the
4₁ total-index assembly by the QUANTUM A-POLYNOMIAL annihilator (DGG eq C.7),
with operator conventions pinned analytically by the trefoil calibrator (C.9).

Why this closes the certification gap. Tranche 2 (merged #3826) left the
assembly open: candidate readings of eq (4.18) either diverge or near-miss the
single printed anchor (4.20). Appendix C supplies an anchor-independent
certificate: (C.7) is the quantum A-polynomial L̂₄₁ that ANNIHILATES the true
index I₄₁(m,e) at every charge, and (C.9) + the trefoil δ-index is a built-in
calibrator for how the operators act.

Glyph-decoded (C.7) (coordinate-aware extraction, minus/superscript rows
individually placed):

  L̂₄₁ = (q^{1/2}M̂ − q^{−1/2}M̂⁻¹)·ℓ̂⁻¹
        − (M̂ − M̂⁻¹)(M̂² + M̂⁻² − M̂ − M̂⁻¹ − q − q⁻¹)
        + (q^{−1/2}M̂ − q^{1/2}M̂⁻¹)·ℓ̂

Calibrator (analytic, from (C.9) L̂₃₁ = ℓ̂ + q^{3/2}M̂³ annihilating the
trefoil index δ_{e,3m}): writing M̂f = q^{a·m}f(m, e+s_M), ℓ̂f = σ·q^{e/2}
f(m+s_L, e), annihilation for ALL (m,e) forces uniquely

  M̂ f(m,e) = q^{m/2}·f(m, e−1),    ℓ̂ f(m,e) = −q^{e/2}·f(m+1, e)
  (⇒ ℓ̂⁻¹ f(m,e) = −q^{−e/2}·f(m−1, e)),

(support match ⇒ s_L = −s_M = +1; magnitude match ⇒ a = +1/2; cancellation ⇒
σ = −1). The probe re-verifies this symbolically on a grid rather than
asserting it.

Certification protocol: for each convergent candidate assembly (the tranche-2
survivors + charge-rescaled variants), compute R(m,e) = L̂₄₁·I over the grid
(m,e) ∈ [−2,2]², exact series arithmetic; CERTIFIED ⟺ R ≡ 0 through the valid
order at every grid point. The single printed anchor then only fixes the
overall monomial normalization — it is no longer load-bearing for structure.

Scope-(a); exact integer/monomial arithmetic; no fit; no c_k wired; the GGM
Stokes reading (step 2) starts only from a certified index.


## REDUCED 2026-10-10 — the annihilator half is RETIRED; only the calibrator remains

Owner ruling (relayed 2026-10-10): this script keeps `trefoil_calibrate()` and
nothing else, and its superseded FAIL is dropped. No port of the missing names.

WHAT WAS REMOVED, and why restoring it was declined. The file imported
`tet_norm` and `_dense_mul` from `qbeta_g3_fourone_index_assembly`; neither
exists there any more, so the whole annihilator path had been UN-IMPORTABLE
while its witness sat `scriptHash`-in-sync. Three corpus artifacts adjudicate
those names rather than merely losing them:

  - `docs/coordination/1ppq-qbeta.md` (#3813, 2026-07-18) records `tet_norm` as
    a NUMERICAL BUG and `tet_abs` as its fix;
  - the `_corrected` producer's docstring says "NOT the buggy `tet_norm`";
  - `qbeta-g3-fourone-index-assembly.witness.json` names the mechanism --
    rebasing each tetrahedron factor to its un-cancelled minimum exponent,
    versus computing I_Delta at ABSOLUTE DEGREE.

So "abs" in `tet_abs` means absolute DEGREE, not absolute value, and the two
have different return contracts that would mis-unpack silently. Rewriting the
missing helpers would have resurrected the bug in order to re-derive a verdict
the corpus had already reversed: this script's own witness published
`assembly_certified_by_annihilator` = FAIL with "candidate non-convergent at
grid point" -- literally the `return None` of the rejection guard that ledger
entry overturned -- while the PROVIDER's `main()` step [5] already performs the
certification and records PASS.

WHAT SURVIVES, and it is not superseded. `trefoil_calibrate()` verifies that
(l-hat + q^(3/2) M-hat^3) annihilates delta(e,3m) for the pinned action
convention and for NO other of the 16 combinations. It is self-contained --
it calls none of the removed helpers and needs neither missing name -- and the
provider does NOT re-verify that uniqueness. Dropping it would have lost the one
result here that nothing else computes.

The witness is REGENERATED rather than deleted, so the calibrator's record
survives and only the superseded assertions go. Beans qou-2cz1 (the import) and
qou-3kni (the dead-citation surface that found it).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def trefoil_calibrate():
    """Verify (ℓ̂ + q^{3/2}M̂³)·δ_{e,3m} = 0 on a grid with the pinned actions,
    and that the 15 other action-convention combinations FAIL."""
    def delta(m, e):
        return 1 if e == 3 * m else 0

    def check(aM2, sM, sL, sig):
        # aM2 = 2a (so q^{aM2·m/2}); returns True if annihilated on grid
        for m in range(-4, 5):
            for e in range(-13, 14):
                # ℓ̂δ = σ q^{e/2} δ(m+sL, e); q^{3/2}M̂³δ = q^{3/2+3aM2·m/2}δ(m, e+3sM)
                # accumulate as (xpow, coeff) monomials — must cancel exactly
                acc = {}
                t1 = (e, sig * delta(m + sL, e))           # x^e = q^{e/2}
                t2 = (3 + 3 * aM2 * m, delta(m, e + 3 * sM))
                for xp, c in (t1, t2):
                    if c:
                        acc[xp] = acc.get(xp, 0) + c
                if any(v != 0 for v in acc.values()):
                    return False
        return True

    pinned = check(1, -1, 1, -1)
    others_fail = True
    n_pass = 0
    for aM2 in (1, -1):
        for sM in (1, -1):
            for sL in (1, -1):
                for sig in (1, -1):
                    if check(aM2, sM, sL, sig):
                        n_pass += 1
                        if (aM2, sM, sL, sig) != (1, -1, 1, -1):
                            others_fail = False
    return pinned, others_fail, n_pass


def main() -> int:
    print("=" * 78)
    print(" A_omega step 1, tranche 3 — trefoil calibrator (annihilator half retired)")
    print("=" * 78)

    pinned, others_fail, n_pass = trefoil_calibrate()
    print(f"\n[1] trefoil calibrator: pinned actions annihilate delta(e,3m): "
          f"{pinned}; conventions passing: {n_pass} (uniqueness: {others_fail})")

    verdict = (
        f"Trefoil calibrator pins the operator actions "
        f"(Mf=q^(m/2)f(m,e-1), lf=-q^(e/2)f(m+1,e)); it annihilates delta(e,3m) "
        f"for that convention and for no other of the 16 combinations "
        f"(passing: {n_pass}, unique: {others_fail}). The annihilator-certification "
        f"half of this probe is RETIRED -- see the module docstring: its two "
        f"missing helpers are a corpus-adjudicated numerical bug, and the "
        f"provider's own main() step [5] already certifies the assembly and "
        f"records PASS. Exact integer arithmetic; scope-(a); no fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-annihilator-certification", engine="python-int")
    wb.set_description(
        "A_omega step 1 tranche 3, REDUCED 2026-10-10: the trefoil calibrator "
        "(C.9) alone. It pins the operator action convention analytically and "
        "shows it unique among the 16 combinations. The annihilator-certification "
        "half is retired -- its helpers are a corpus-adjudicated numerical bug "
        "(1ppq-qbeta.md #3813) and the provider already certifies the assembly.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("actions", "Mf = q^(m/2) f(m,e-1); lf = -q^(e/2) f(m+1,e) "
                           "(trefoil-calibrated, unique)")
    wb.add_data("calibrator", {"pinned_ok": bool(pinned),
                               "unique": bool(others_fail),
                               "n_conventions_passing": n_pass})
    wb.add_data("retired", {
        "what": "annihilator_residual + the assemble/_assemble/sadd/smono/"
                "struncate_top helper chain, and the two assertions "
                "assembly_certified_by_annihilator and certified_candidate_unique",
        "why": "imported tet_norm and _dense_mul, which no longer exist; the "
               "corpus adjudicates tet_norm as a numerical bug and the provider's "
               "main() step [5] already certifies the assembly and records PASS",
        "ruling": "owner, relayed 2026-10-10: keep only trefoil_calibrate(), "
                  "drop the superseded FAIL, do not port",
    })
    wb.add_data("verdict", verdict)
    # mpf, not float: the raw-float64 ratchet counts an assertion's `computed`
    # and `expected`, and a regenerated witness is the regenerator's dirt even
    # when the float literals were inherited. Baselines drain, never grow.
    wb.add_assertion("trefoil_calibrator_pins_actions",
                     computed=mp.mpf(1) if (pinned and others_fail) else mp.mpf(0),
                     expected=mp.mpf(1), tolerance=mp.mpf("0.5"),
                     source="(C.9) annihilates delta(e,3m) only for the pinned "
                            "action convention")
    wb.save()
    return 0 if (pinned and others_fail) else 1


if __name__ == "__main__":
    raise SystemExit(main())
