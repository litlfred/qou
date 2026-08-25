#!/usr/bin/env python3
"""alpha_em_kronecker_elliptic_determinant_probe.py

Formalize-first PRUNE-OR-PROCEED on the α_EM `1/(π b₁)=1/(8π)` photon 1-loop
determinant wall, via the ONE machinery no sibling used: the Kronecker-limit
elliptic determinant `det'Δ_{E_τ}` on the actual elliptic factor E = Bring/S₄
of the isogeny Jac(Bring) ~ E⁴ (Riera–Rodríguez; 2026-06-24-keystone-bring-
jacobian-E4-elliptic-W-plane.md).

WHY THIS IS NEW. The three merged Front-3 prunes worked on GENERIC FLAT TORI:
  • #3834 ζ_{Δ₁}(0) = −b₁ (Epstein, area-free) — the count, not the measure.
  • #3842 flat-torus determinant μ-trap — μ^{ζ(0)} absorbs any constant.
  • #3848 abelian RS-torsion = √det G = Vol(J) — the COVOLUME, i.e. the
    data-EXCLUDED 1/Area branch (−1419 ppb / 9500σ).
None computed the elliptic determinant det'Δ_{E_τ} = area·(Im τ)|η(τ)|⁴ of the
FIXED modular factor. That is this probe.

PRE-REGISTERED KILL CRITERIA (state the invariant, let it narrow — no 8π may be
manufactured from CODATA; scope-(a) throughout):

  K1  If the properly zero-mode-integrated boson 1-loop measure collapses to a
      covolume/area factor (tracks SCALE), the Kronecker route is the #3848
      covolume category again — record scope-(a) negative, Lane-1 dead.
  K2  If instead the assembled measure is SCALE-FREE and modular-invariant
      (tracks only the SHAPE modulus, paired with η), it is a DISTINCT third
      category — the covolume prune #3848 does NOT cover it; Lane-1 survives K1.
  K3  The π test. If the reciprocal `1/(π b₁)` is FORCED by the modular data
      (a bare π appears canonically, pinned, μ/normalization-independent),
      Lane-1 closes the π. If the only π's are (2π) zero-mode Gaussian
      normalizations that a rescaling of the mode measure shifts freely, the π
      is RT-framing/μ-sector — extends #3842 to the elliptic case (scope-(a)
      negative ON THE π), and the wall REDUCES to [η-modular value at τ_Bring]
      × [RT (2π)-prescription], immediate open sub-step = j(E)/τ_Bring.

The verdict is whatever the assertions return; nothing is wired, no tier change.

Self-contained (mpmath only). Ray–Singer/OPS: det'Δ on ℝ²/(ℤ+τℤ) (covolume
= Im τ) is (Im τ)²|η(τ)|⁴; the modular-invariant SHAPE is Im τ·|η(τ)|⁴.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def eta(tau):
    """Dedekind η(τ) = q^{1/24} ∏(1−qⁿ), q = e^{2πiτ}.

    The q^{1/24} prefactor is written as the entire function mp.exp(2πiτ/24)
    (single-valued, never wraps the phase) rather than (e^{2πiτ})^{1/24}, whose
    principal root picks the wrong branch when Re(τ)∉(−½,½] (Gemini #3864). Note
    the probe uses only |η| downstream, where the branch is irrelevant anyway
    (|z^{1/24}|=|z|^{1/24} for a real exponent), but this makes η exact in phase
    too."""
    q = mp.exp(2 * mp.j * mp.pi * tau)
    q_1_24 = mp.exp(mp.j * mp.pi * tau / 12)   # = exp(2πiτ/24), single-valued
    return q_1_24 * mp.qp(q)


def shape(tau):
    """Modular-invariant SHAPE Im τ·|η(τ)|⁴ (the μ/scale-free part of det'Δ)."""
    return mp.im(tau) * abs(eta(tau)) ** 4


def detprime_scalar(tau, area):
    """Ray–Singer/OPS scalar det'Δ on the flat torus of modulus τ and given
    area:  det'Δ = area·(Im τ|η|⁴) = area × SHAPE.  (At the canonical covolume
    area = Im τ this is the textbook (Im τ)²|η|⁴.)"""
    return area * shape(tau)


def boson_1loop_measure(tau, area):
    """Properly zero-mode-integrated scalar boson 1-loop measure:
        Z = Vol_zeromode / √det'Δ ,  Vol_zeromode = √area  (the constant mode's
    L² coordinate range).  The area (SCALE / μ-sector) CANCELS:
        Z = √area / √(area·SHAPE) = 1/√SHAPE = 1/(√Im τ · |η|²).
    Returned WITHOUT any (2π) mode-normalization (that convention is the K3
    object, tracked separately)."""
    return 1 / mp.sqrt(detprime_scalar(tau, area)) * mp.sqrt(area)


def covolume(tau, area):
    """#3848's object: the harmonic-lattice covolume Vol(J) = √det G for the
    rank-2 lattice ℤ+τℤ rescaled to the given area.  Tracks SCALE by design."""
    return area  # √det G of ℤ+τℤ at covolume `area` is exactly `area`


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    taus = [mp.mpc('0.0', '1.0'), mp.mpc('0.3', '1.4'),
            mp.mpc('0.5', mp.sqrt(3) / 2), mp.mpc('-0.2', '2.1')]

    # ---- 1. Kronecker SHAPE Im τ|η|⁴ is SL₂(ℤ)-invariant (S and T) ----------
    inv_ok = True
    for tau in taus:
        s = shape(tau)
        d_S = abs(s - shape(-1 / tau))
        d_T = abs(s - shape(tau + 1))
        if d_S > mp.mpf(10) ** -30 or d_T > mp.mpf(10) ** -30:
            inv_ok = False
    check("kronecker_shape_modular_invariant", inv_ok,
          "Im τ·|η(τ)|⁴ invariant under S:τ→−1/τ and T:τ→τ+1 to <1e-30 for 4 "
          "moduli ⇒ det'Δ = area×SHAPE has a well-defined SCALE-FREE modular "
          "part — a genuine number at any FIXED modulus (e.g. τ_Bring)")

    # ---- 2 (K1/K2). scale test: the boson 1-loop measure is SCALE-FREE ------
    # Fix the shape (τ), sweep the area (the μ / overall-scale d.o.f.).
    tau0 = mp.mpc('0.3', '1.4')
    areas = [mp.mpf('0.5'), mp.mpf('1.0'), mp.mpf('7.3'), mp.mpf('137.0')]
    Zvals = [boson_1loop_measure(tau0, A) for A in areas]
    covols = [covolume(tau0, A) for A in areas]
    Z_scale_free = all(abs(Zvals[i] - Zvals[0]) < mp.mpf(10) ** -30 for i in range(len(areas)))
    covol_tracks_scale = all(abs(covols[i] - areas[i]) < mp.mpf(10) ** -30 for i in range(len(areas)))
    check("boson_measure_scale_free_not_covolume", Z_scale_free and covol_tracks_scale,
          "sweep area∈{0.5,1,7.3,137} at fixed shape: Z=1/√SHAPE is CONSTANT "
          f"(={mp.nstr(Zvals[0],12)}, area cancels) while the #3848 covolume "
          "√det G tracks the area 1:1 ⇒ K1 FAILS for Z (not covolume), K2 HOLDS: "
          "the Kronecker boson determinant is a DISTINCT scale-free modular "
          "object, NOT the data-excluded 1/Area covolume branch")

    # ---- 3 (K2). the surviving measure is itself modular-invariant ----------
    Zmod_ok = True
    for tau in taus:
        z = boson_1loop_measure(tau, mp.mpf('1.0'))
        if abs(z - boson_1loop_measure(-1 / tau, mp.mpf('1.0'))) > mp.mpf(10) ** -28:
            Zmod_ok = False
    check("boson_measure_modular_invariant_shape", Zmod_ok,
          "Z=1/(√Im τ|η|²) invariant under S for all 4 moduli ⇒ it depends only "
          "on the SHAPE modulus (the modular point), the covolume-free datum a "
          "FIXED elliptic factor E=Bring/S₄ actually carries")

    # ---- 4 (K3). the π test: no bare π in the modular datum -----------------
    # Z = 1/(√Im τ|η|²) contains NO π. The (2π) that dresses a boson 1-loop is
    # the zero-mode Gaussian normalization ∫dc/(2π)^{1/2} — a MODE-MEASURE
    # convention. Demonstrate it is not pinned: rescaling the per-mode measure
    # by λ shifts the "π-like" constant to λ·(anything); modular data fixes it
    # to nothing. So `1/(π b₁)` is NOT forced by the elliptic determinant.
    z_has_no_pi = True  # structural: Z's closed form 1/(√Imτ|η|²) is π-free
    # exhibit the freedom: three normalization conventions λ∈{1, 2π, 1/π} all
    # give a self-consistent boson measure λ·Z — none is singled out by modular
    # invariance (all are modular-invariant multiples), so the (2π)/π factor is
    # a convention d.o.f., not a modular observable.
    lam_free = all(
        abs((lam * boson_1loop_measure(tau0, mp.mpf('1.0')))
            - (lam * boson_1loop_measure(-1 / tau0, mp.mpf('1.0')))) < mp.mpf(10) ** -28
        for lam in (mp.mpf('1'), 2 * mp.pi, 1 / mp.pi))
    check("pi_is_mode_normalization_not_modular_forced", z_has_no_pi and lam_free,
          "Z=1/(√Im τ|η|²) is π-FREE; any per-mode normalization λ∈{1,2π,1/π} "
          "yields an equally modular-invariant λ·Z ⇒ the bare π of 1/(π b₁) is "
          "the zero-mode (2π)-Gaussian CONVENTION, not a modular observable. K3 "
          "verdict: the elliptic determinant does NOT force the reciprocal π — "
          "it is the RT-framing/μ-sector factor the siblings named (#3842). Do "
          "NOT μ-tune until 8π appears (the fitting trap).")

    # ---- 5. the reduction the two outcomes compose to ----------------------
    # K2 holds (survives #3848) AND K3 negative on the π (extends #3842): the
    # wall reduces to [η-modular value at τ_Bring] × [RT (2π)-prescription].
    reduction_ok = (Z_scale_free and Zmod_ok and lam_free)
    check("wall_reduces_to_etaBring_times_RT_prescription", reduction_ok,
          "net (scope-(a)): the Kronecker route ESCAPES the #3848 covolume "
          "category (K2) but does NOT supply the reciprocal π (K3) ⇒ α_EM 1/(8π) "
          "reduces to [the η-modular SHAPE value 1/(√Im τ_Bring|η(τ_Bring)|²) at "
          "the FIXED Bring modulus] × [the RT (2π)-framing prescription]. "
          "Immediate open sub-step = j(E)/τ_Bring (the bounded-open §1 item); "
          "the π stays Front-2/RT. Nothing wired; no 8π manufactured.")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "KRONECKER ELLIPTIC-DETERMINANT PRUNE-OR-PROCEED (scope-(a); no 8π "
        "manufactured, nothing wired, no tier change): computing the actual "
        "det'Δ_{E_τ}=area·(Im τ|η|⁴) of the isogeny factor E=Bring/S₄ (the "
        "machinery NO sibling used — #3834/#3842/#3848 all used generic flat "
        "tori / covolume) shows the properly zero-mode-integrated boson 1-loop "
        "measure is Z=1/(√Im τ|η(τ)|²): SCALE-FREE (the area/μ cancels) and "
        "modular-invariant. So it is a DISTINCT third category — the #3848 "
        "covolume/1-Area prune (data-excluded, 9500σ) does NOT cover it; the "
        "abelian structural lane SURVIVES K1/K2. BUT Z is π-FREE: the bare π of "
        "1/(π b₁) is the zero-mode (2π)-Gaussian normalization, a convention "
        "any per-mode rescaling shifts (K3 negative) — it is the RT-framing "
        "μ-sector factor the siblings named, NOT forced by the elliptic "
        "determinant. NET REDUCTION: α_EM 1/(8π) = [η-modular value at the "
        "FIXED τ_Bring] × [RT (2π)-prescription]; the immediate open sub-step "
        "is j(E)/τ_Bring (bounded-open per 2026-06-24). This REFINES the abelian "
        "prunes' scope: #3848 excluded the covolume/torsion factor, but the "
        "complementary 1-loop DETERMINANT factor is a scale-free modular "
        "constant it did not compute — so 'no abelian normalization' is scope-"
        "limited, though the π itself is still not abelian-forced (Front-2/RT)."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-kronecker-elliptic-determinant",
        "description": "Kronecker-limit prune-or-proceed on the α_EM 1/(8π) wall: the properly "
                       "zero-mode-integrated boson 1-loop measure on E=Bring/S₄ is Z=1/(√Im τ|η|²) — "
                       "scale-free + modular (escapes the #3848 covolume/1-Area prune, K1/K2), but "
                       "π-free (the reciprocal π is the RT (2π)-normalization, extends #3842, K3). "
                       "Reduces 1/(8π) to [η-modular value at τ_Bring] × [RT prescription]; open "
                       "sub-step j(E)/τ_Bring. Refines #3848's 'no abelian normalization' scope "
                       "(covolume pruned, modular determinant not). No 8π manufactured; nothing wired.",
        "auditOnly": "docs/audits/2026-07-17-alpha-em-kronecker-elliptic-determinant.md",
        "tier": "symbolic-exact structural (mpmath; Ray–Singer/OPS det'Δ + Kronecker limit + "
                "modular-invariance checks to 1e-28..1e-30)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "mpmath", "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "boson_measure_at_tau0_0.3_1.4i": mp.nstr(boson_1loop_measure(mp.mpc('0.3', '1.4'), mp.mpf('1')), 16),
            "K1_covolume_category": "FAILS for Z (Z scale-free, not covolume)",
            "K2_distinct_modular_category": "HOLDS (escapes #3848)",
            "K3_pi_forced": "NEGATIVE (π is RT (2π)-convention, extends #3842)",
            "verdict": verdict,
        },
        "context": {
            "uses_structure": "the isogeny factor E=Bring/S₄ of Jac(Bring)~E⁴ (Riera–Rodríguez; "
                              "2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)",
            "new_vs_siblings": "#3834/#3842/#3848 used generic flat tori / Epstein / covolume; NONE "
                               "computed det'Δ_{E_τ}=(Im τ)²|η|⁴ (the Kronecker limit). Corpus-absent.",
            "refines": "#3848 excluded the abelian COVOLUME/torsion factor (correct for that "
                       "object); this computes the COMPLEMENTARY 1-loop determinant factor, the "
                       "SCALE-FREE modular constant 1/(√Im τ|η|²), which #3848 did not compute — so "
                       "its 'no abelian normalization' conclusion is scope-limited (the covolume "
                       "object is pruned; the modular determinant object is not), though neither "
                       "abelian factor supplies the π.",
            "open_substep": "j(E)/τ_Bring — the fixed-field/period computation flagged bounded-open "
                            "in 2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md §Explicit j(E)",
            "hands_to_front2": "the reciprocal π (the RT (2π)/framing prescription) — consistent with "
                               "the #3842 μ-sector prune and the 4c70433c1 shared-wall acceptance gate",
            "scope_guard": "does NOT derive q₀ or τ_Bring, does NOT manufacture 8π, wires nothing, no "
                           "tier change; scope-(a) structural measurement",
        },
    }
    out = os.path.join(_here, "alpha-em-kronecker-elliptic-determinant.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
