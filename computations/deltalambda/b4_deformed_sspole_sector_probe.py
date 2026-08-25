#!/usr/bin/env python3
"""b4 scalar m: the derived magnitude sits EXACTLY on the q-DEFORMED A=4 ss-pole,
and the pole lives in the species-SYMMETRIC (non-Pauli) sector.  (Forward, no fit.)

CONTEXT (read first, in order):
  * docs/audits/2026-07-18-deltalambda-attack-vector-map.md  (Vector 2 icosahedral
    1/sqrt5; §1b the magnitude wall = one scalar m in (0,1/sqrt5))
  * docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md
    §2b -- I1 (5+(q0-1)^2/q0 = 1+[2]_v^2), I2 (deformed-criticality:
    g_reeb = 1/sqrt(1+[2]_v^2) is the eigenvalue-criticality of the q-deformed 2x2
    ss-sector exchange [[1,[2]_v],[[2]_v,-1]]).
  * b4_slater_antisymmetrizer_exchange_sign.py (#3924) -- classical K4 (ppnn)
    writhe spectrum {+-sqrt5,+-1}, det(I+mS)=(1-5m^2)(1-m^2), classical ceiling
    m<1/sqrt5.
  * b4_icosahedral_m_ceiling_probe.py (#4xxx, this branch) -- the Sigma(2,3,5)
    vacuum-row entries OVERSHOOT the classical 1/sqrt5 ceiling.

THE FINDING (the "icosahedral overshoot" resolved; two exact structural facts).

  FACT 1 -- the derived magnitude is ON the deformed pole, not below a ceiling.
    The classical A=4 ss-sector eigenvalue sqrt5 = sqrt(1+2^2) reads off the 2x2
    reduction [[1,2],[2,-1]] (pp-nn asymmetry 1, integer pn-degree 2).  Deforming
    the integer pn-degree 2 -> [2]_v (I2) sends the eigenvalue sqrt5 -> sqrt(1+[2]_v^2)
    and the derived magnitude g_reeb = 1/sqrt(1+[2]_v^2) satisfies EXACTLY
        (1 + [2]_v^2) * g_reeb^2 = 1                      (verified to dps)
    i.e. the deformed ss-sector det factor  1 - (1+[2]_v^2) g_reeb^2 = 0.  So g_reeb
    is NOT "just below the 1/sqrt5 ceiling" (the 4.9e-4 gap is the classical-vs-
    deformed artifact: 1-5 g_reeb^2 = 2.17e-3 > 0 only because it uses the q=1
    integer 5); consistently deformed, the physical magnitude sits ON the ss-pole.
    CONSEQUENCE for Vector 2: there is no admissible SUB-ceiling icosahedral entry
    to select as m -- the physical m sits on the (deformed) boundary itself.  The
    "overshoot" the icosahedral probe saw is the classical shadow of an exact pole.

  FACT 2 -- the pole is in the species-SYMMETRIC (non-Pauli) sector; the Pauli
    [1^4] antisymmetric sector is FINITE.  Eigen-decomposing the classical K4 (ppnn)
    writhe matrix S:
        lam = +-sqrt5  <->  species-SYMMETRIC modes (pp-sym (1,1,.,.), nn-sym) --
                            the "ss-sector"; det factor (1-5m^2); carries the pole.
        lam = +-1      <->  species-ANTISYMMETRIC Pauli modes (p1-p2, n1-n2) --
                            det factor (1-m^2); FINITE at m=g_reeb.
    So the divergent factor (1-5m^2 -> deformed 1-(1+[2]_v^2)m^2) is the
    center-of-mass mode of each identical-fermion pair, NOT the Pauli-required
    intra-pair antisymmetric mode.  The full determinant multiplies both, so the
    single-scalar b_4 = -ln det(I+g_reeb S) DIVERGES (species-symmetric condensation
    pole), which is why the single-m det model over-predicts / cannot be fit (the
    #3952 4He 2.6-10.6x overshoot and the bareven-probe rho4-forces-rho3 failure are
    both this pole seen through the classical ceiling).

RE-SCOPING (honest, scope-(a) sharpened by scope-(b)).
  The b_4 SCALAR is not the open object: m = g_reeb (the deformed ss-criticality)
  is forward-derived and pins the deuteron to +0.41% (I2).  What the single-scalar
  determinant construction gets WRONG is the FORM: at m=g_reeb the species-symmetric
  sector is exactly critical, so -ln det = +inf.  The large but FINITE 4He binding
  (rho4=13 >> 6 pair-additive) is a NEAR-pole enhancement of the species-symmetric
  condensation mode; the open b_4 closure is the POLE REGULATOR (what makes the
  near-critical mode finite), NOT the choice of scalar m.  This turns "find m" into
  "m is found; find the regulator of the alpha-condensation pole".

  Scope classification (AGENTS.md "Before declaring refuted"):
   * scope-(b) structural facts (proved invariants): the exact criticality
     (1+[2]_v^2)g^2=1 and the species-symmetric/antisymmetric sector split of the
     K4 writhe spectrum.  These do not depend on any AME number.
   * scope-(a) negative: the single-scalar full-determinant b_4 = -ln det(I+g_reeb S)
     construction, ALONE, diverges at the derived magnitude and cannot reproduce a
     finite 4He binding -- it needs a pole regulator.  This does NOT exclude the
     per-bond factor g_reeb (permanence: it is the derived, deuteron-correct value);
     it measures where the determinant FORM breaks (the ss-condensation threshold).

EXPLORATORY -- audit + witness only; no production wiring, no fit, no AME inversion.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

COMP = str(_COMP)
set_compute_dps()

# muon-canonical q0 (the computations/ layer convention; AGENTS.md q0-convention)
Q0_STR = "1.10997859555733471"

# K4 (ppnn) writhe sign matrix: diag 0, off-diag pp=+1, nn=-1, pn=+1.
_WSGN = {("p", "p"): 1, ("n", "n"): -1, ("p", "n"): 1, ("n", "p"): 1}
_WORD4 = ["p", "p", "n", "n"]


def writhe_S(word):
    n = len(word)
    S = mp.zeros(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                S[i, j] = _WSGN[(word[i], word[j])]
    return S


def rayleigh(S, c):
    cv = mp.matrix(c)
    num = (cv.T * (S * cv))[0]
    den = (cv.T * cv)[0]
    rq = num / den
    res = S * cv - rq * cv
    return rq, mp.norm(res)


def main() -> int:
    q0 = mp.mpf(Q0_STR)
    v = mp.sqrt(q0)
    two_v = v + 1 / v                                  # [2]_v (balanced)
    g_reeb = 1 / mp.sqrt(5 + (q0 - 1) ** 2 / q0)       # landed derived magnitude
    g_alt = 1 / mp.sqrt(1 + two_v ** 2)                # I2 deformed criticality
    ceil_cl = 1 / mp.sqrt(mp.mpf(5))                    # classical ceiling

    # ---- FACT 1: I1 identity + exact deformed criticality --------------------
    I1_equal = abs(g_reeb - g_alt) < mp.mpf(10) ** -40
    lam2_def = 1 + two_v ** 2                           # deformed ss eigenvalue^2
    ss_pole_residual = lam2_def * g_reeb ** 2 - 1       # == 0 exactly
    on_deformed_pole = abs(ss_pole_residual) < mp.mpf(10) ** -40
    classical_ss_factor = 1 - 5 * g_reeb ** 2           # 2.17e-3 (classical, >0)
    deformed_ss_factor = 1 - lam2_def * g_reeb ** 2     # 0 (deformed pole)
    below_classical_ceiling = g_reeb < ceil_cl
    classical_gap = ceil_cl - g_reeb                    # 4.87e-4 artifact

    # ---- FACT 2: sector decomposition of the K4 writhe spectrum --------------
    S = writhe_S(_WORD4)
    E, _V = mp.eig(S)
    eigs = sorted((mp.re(E[k]) for k in range(4)))
    # candidate physical modes
    modes = {
        "p_intrapair_antisym (1,-1,0,0)": [1, -1, 0, 0],   # Pauli, expect lam=-1
        "n_intrapair_antisym (0,0,1,-1)": [0, 0, 1, -1],   # Pauli, expect lam=+1
    }
    sector = {}
    for name, c in modes.items():
        rq, rn = rayleigh(S, c)
        sector[name] = {"rayleigh": mp.nstr(rq, 8), "is_eigenvector": bool(rn < mp.mpf(10) ** -20)}
    # the +-sqrt5 modes are species-SYMMETRIC (verified: their eigenvectors have
    # equal signs within each species -- (a,a,b,b) with |a|,|b| != 0)
    sqrt5_species_symmetric = True
    for k in range(4):
        lam = mp.re(E[k])
        if abs(abs(lam) - mp.sqrt(5)) < mp.mpf("1e-6"):
            vk = [mp.re(_V[r, k]) for r in range(4)]
            # species-symmetric <=> sign(v0)==sign(v1) and sign(v2)==sign(v3)
            same_p = (vk[0] * vk[1] > 0)
            same_n = (vk[2] * vk[3] > 0)
            sqrt5_species_symmetric = sqrt5_species_symmetric and bool(same_p and same_n)

    # Pauli-antisymmetric sub-determinant factor (finite): product over lam=+-1 modes
    pauli_factor = (1 - g_reeb) * (1 + g_reeb)          # = 1 - g_reeb^2 (lam=+-1)
    pauli_b = -mp.log(pauli_factor)                     # finite
    # full single-scalar determinant at m=g_reeb (classical integer-5 form): near 0
    full_det_classical = (1 - 5 * g_reeb ** 2) * (1 - g_reeb ** 2)
    full_b_classical = -mp.log(full_det_classical)      # large (classical shadow)
    # deformed full determinant: ss factor == 0 => -ln = +inf
    full_det_deformed = deformed_ss_factor * (1 - g_reeb ** 2)

    # ---- REGULATOR BATTERY: do any standard forward regulators rescue b4? -----
    # The deformed determinant has an EXACT zero mode (the -sqrt(1+[2]_v^2) mode).
    # Test the standard forward (no-fit) prescriptions for a functional determinant
    # with an exact zero mode, and the ratio to the A=2 reference. Target rho4~13.03.
    Ldef = mp.sqrt(1 + two_v ** 2)                       # deformed ss eigenvalue
    # (1) reduced determinant: drop the vanishing (1 - g*Ldef) factor
    det_reduced = (1 + g_reeb * Ldef) * (1 - g_reeb ** 2)   # = 2*(1-g^2) at the pole
    b_reduced = -mp.log(det_reduced)                     # NEGATIVE (det>1) => repulsive
    # (2) Pauli sector only: ratio to A=2 (same 1-g^2 factor) => trivially 1
    b2_ref = -mp.log(1 - g_reeb ** 2)
    rho4_pauli = pauli_b / b2_ref                        # = 1 (trivial)
    rho4_reduced = b_reduced / b2_ref                    # negative
    rho4_target = mp.mpf("13.03")                        # isospin-corrected strong (context only)
    regulator_battery = {
        "target_rho4_strong_context_only": mp.nstr(rho4_target, 6),
        "reduced_det_drop_zero_mode": mp.nstr(det_reduced, 8),
        "b_reduced": mp.nstr(b_reduced, 8),
        "b_reduced_is_repulsive_negative": bool(b_reduced < 0),
        "rho4_reduced": mp.nstr(rho4_reduced, 6),
        "pauli_sector_b": mp.nstr(pauli_b, 8),
        "rho4_pauli_trivial": mp.nstr(rho4_pauli, 6),
        "verdict": "NO standard forward regulator rescues b_4: the zero-mode-reduced "
                   "determinant is 2(1-g^2)>1 => -ln<0 REPULSIVE (Lean-proved "
                   "he4DetReduced_gt_one_at_pole); the Pauli-sector-only ratio is trivially "
                   "1. Wrong sign / trivial, both far from rho4~13. The -ln det free-energy "
                   "form is refuted as the b_4 magnitude carrier.",
        "redirect": "the exact zero mode (I+g*S annihilates the species-sym eigenvector) is a "
                    "COLLECTIVE COORDINATE; its contribution is the moduli VOLUME of the "
                    "alpha-condensate, i.e. the geometric Vol*rho object of the canonical mass "
                    "formula -- NOT the loop determinant (cf. ReebPnMagnitude.ss_det_no_linear_term). "
                    "This is the forward research direction; it is NOT closed here (no fit).",
        "lean_verified": "QOU.MassTheory.he4DetViaEig_zero_at_pole (det=0 on the pole), "
                         "he4DetReduced_gt_one_at_pole (reduced det>1 => repulsive); "
                         "B4CumulantBarEven.lean, lean-direct exit 0, sorry-free.",
    }

    result = {
        "fact1_derived_magnitude_on_deformed_ss_pole": {
            "q0": mp.nstr(q0, 18),
            "two_v_balanced": mp.nstr(two_v, 18),
            "g_reeb": mp.nstr(g_reeb, 18),
            "g_reeb_eq_deformed_criticality_1_over_sqrt_1p2v2": bool(I1_equal),
            "classical_ceiling_1_over_sqrt5": mp.nstr(ceil_cl, 18),
            "g_below_classical_ceiling": bool(below_classical_ceiling),
            "classical_gap_artifact": mp.nstr(classical_gap, 6),
            "deformed_ss_pole_residual_(1p2v2)g2_minus_1": mp.nstr(ss_pole_residual, 6),
            "on_deformed_pole": bool(on_deformed_pole),
            "classical_ss_factor_1_minus_5g2": mp.nstr(classical_ss_factor, 8),
            "deformed_ss_factor_1_minus_(1p2v2)g2": mp.nstr(deformed_ss_factor, 8),
            "reading": "g_reeb is EXACTLY the deformed A=4 ss-sector eigenvalue-criticality "
                       "(1+[2]_v^2)g^2=1, not merely below the classical 1/sqrt5 ceiling; the "
                       "4.9e-4 sub-ceiling gap is the classical(integer-5)-vs-deformed artifact. "
                       "Hence Vector 2 has no sub-ceiling icosahedral entry to select as m: the "
                       "physical m sits ON the deformed boundary.",
        },
        "fact2_pole_in_species_symmetric_non_pauli_sector": {
            "K4_ppnn_spectrum": [mp.nstr(x, 8) for x in eigs],
            "pauli_intrapair_modes_are_eigenvectors": sector,
            "sqrt5_eigenvectors_are_species_symmetric": bool(sqrt5_species_symmetric),
            "pauli_sector_factor_1_minus_g2": mp.nstr(pauli_factor, 10),
            "pauli_sector_b_finite": mp.nstr(pauli_b, 10),
            "reading": "lam=+-sqrt5 are the species-SYMMETRIC (pp-sym, nn-sym) center-of-mass "
                       "modes (the ss-sector that carries the pole); lam=+-1 are the "
                       "Pauli-required intra-pair antisymmetric modes, FINITE at m=g_reeb. The "
                       "divergent factor is the NON-Pauli species-symmetric (alpha-condensation) "
                       "mode.",
        },
        "regulator_battery_all_fail": regulator_battery,
        "consequence_single_scalar_determinant_diverges": {
            "full_det_classical_integer5": mp.nstr(full_det_classical, 8),
            "full_b_classical_shadow": mp.nstr(full_b_classical, 8),
            "full_det_deformed": mp.nstr(full_det_deformed, 8),
            "full_b_deformed": "+inf (deformed ss factor = 0)",
            "reading": "single-scalar b_4 = -ln det(I+g_reeb S) diverges (deformed) / is a large "
                       "classical shadow -- this IS the #3952 4He overshoot and the bareven-probe "
                       "rho4-forces-rho3 failure. The b_4 SCALAR m=g_reeb is found; the open object "
                       "is the pole REGULATOR of the alpha-condensation mode, not the scalar.",
        },
        "verdict": {
            "classification": "scope-(b) structural facts + scope-(a) construction negative.",
            "scope_b_facts": "(1+[2]_v^2)g_reeb^2 = 1 exactly (deformed ss-criticality); the K4 "
                             "writhe +-sqrt5 modes are species-symmetric and +-1 are Pauli "
                             "intra-pair -- both proved invariants, AME-independent.",
            "scope_a_negative": "the single-scalar full-determinant b_4 = -ln det(I+g_reeb S) "
                                "construction, alone, diverges at the derived magnitude and cannot "
                                "give a finite 4He binding; it needs a pole regulator. Does NOT "
                                "exclude the per-bond factor g_reeb (permanence: deuteron +0.41%).",
            "vector2_rescoped": "icosahedral-entry = m REFUTED: no sub-ceiling entry exists to "
                                "select because m sits on the deformed boundary; the icosahedral "
                                "'overshoot' is the classical shadow of the exact deformed pole.",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "b4-deformed-sspole-sector",
        "description": ("The derived b_4 magnitude g_reeb=1/sqrt(1+[2]_v^2) sits EXACTLY on the "
                        "q-deformed A=4 ss-sector determinant pole ((1+[2]_v^2)g^2=1), and the "
                        "pole lives in the species-SYMMETRIC (non-Pauli, alpha-condensation) "
                        "sector while the Pauli intra-pair sector (lam=+-1) stays finite. Resolves "
                        "'icosahedral lead overshoots the ceiling' (no sub-ceiling entry -- m is on "
                        "the deformed boundary) and re-scopes the open b_4 object from 'the scalar "
                        "m' to 'the pole regulator'. scope-(b) facts + scope-(a) construction "
                        "negative; no fit, audit-only."),
        "audit_only": True,
        "tier": "structural (exact deformed-criticality identity + eigen-sector decomposition; no fit)",
        "result": result,
        "context": {
            "axis": "Delta_lambda magnitude wall -- b_4 scalar m (Vector 2 re-scope)",
            "attack_vector_map": "docs/audits/2026-07-18-deltalambda-attack-vector-map.md",
            "provenance": "docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-deformed-sspole-sector", payload,
        script_path=__file__, engine="mpmath", output_dir=os.path.join(COMP, "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("g_reeb_eq_deformed_criticality", computed=str(bool(I1_equal)), expected="True")
    wb.add_assertion("g_reeb_on_deformed_ss_pole", computed=str(bool(on_deformed_pole)), expected="True")
    wb.add_assertion("g_below_classical_ceiling_artifact", computed=str(bool(below_classical_ceiling)),
                     expected="True")
    wb.add_assertion("sqrt5_modes_species_symmetric", computed=str(bool(sqrt5_species_symmetric)),
                     expected="True")
    wb.add_assertion("pauli_intrapair_p_is_eigenvector",
                     computed=str(sector["p_intrapair_antisym (1,-1,0,0)"]["is_eigenvector"]),
                     expected="True")
    wb.add_assertion("pauli_sector_finite", computed=str(bool(pauli_factor > 0)), expected="True")
    wb.add_assertion("reduced_det_regulator_is_repulsive", computed=str(bool(b_reduced < 0)),
                     expected="True")
    wb.add_assertion("no_forward_regulator_reaches_target", computed=str(bool(rho4_reduced < 0)),
                     expected="True")
    out = wb.save(extra={"auditOnly": True})

    # ---- console report ------------------------------------------------------
    print("=== b_4 scalar m: derived magnitude on the deformed ss-pole (species-symmetric) ===")
    print(f"q0={mp.nstr(q0,12)}  [2]_v={mp.nstr(two_v,12)}")
    print(f"g_reeb = {mp.nstr(g_reeb,15)}  = 1/sqrt(1+[2]_v^2) (I2)? {I1_equal}")
    print(f"classical 1/sqrt5 = {mp.nstr(ceil_cl,15)}  (g below by {mp.nstr(classical_gap,4)} -- artifact)")
    print(f"FACT 1  (1+[2]_v^2)*g^2 - 1 = {mp.nstr(ss_pole_residual,4)}  => ON deformed ss-pole: {on_deformed_pole}")
    print(f"        classical (1-5g^2) = {mp.nstr(classical_ss_factor,6)} > 0 (integer-5 shadow); "
          f"deformed (1-(1+[2]_v^2)g^2) = {mp.nstr(deformed_ss_factor,6)}")
    print(f"FACT 2  K4(ppnn) spectrum = {[mp.nstr(x,6) for x in eigs]}")
    print(f"        +-sqrt5 species-symmetric: {sqrt5_species_symmetric}; +-1 Pauli intra-pair "
          f"(eigenvectors: {all(s['is_eigenvector'] for s in sector.values())})")
    print(f"        Pauli-sector factor (1-g^2) = {mp.nstr(pauli_factor,8)} (finite, b={mp.nstr(pauli_b,6)})")
    print(f"REGULATOR BATTERY (target rho4~13): reduced-det={mp.nstr(det_reduced,6)} => "
          f"b={mp.nstr(b_reduced,5)} (repulsive: {b_reduced<0}); pauli rho4={mp.nstr(rho4_pauli,4)} (trivial)")
    print("   => NO standard forward regulator rescues b_4 (wrong sign / trivial). -ln det form "
          "refuted as the carrier; redirect: zero mode = collective coord = Vol*rho object.")
    print("VERDICT: b_4 scalar m = g_reeb FOUND (deformed ss-criticality); single-scalar det "
          "DIVERGES at the pole; open object = the alpha-condensation POLE REGULATOR. No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
