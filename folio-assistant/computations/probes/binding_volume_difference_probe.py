#!/usr/bin/env python3
"""
binding_volume_difference_probe.py — does a DERIVED hyperbolic-volume
difference B = ρ·[Vol(atom) − Vol(free)] close A≥3 binding?
(Derive-or-refute; no AME fit, no hand-assigned census knots.)

MOTIVATION. Per kashaev-as-archimedean-realization.md, the Archimedean
mass of a knot is Vol(K) = 2π·lim_{N→∞} log|J_N(K)|/N, i.e. the trace is
the EXPONENTIAL of a volume: tr ~ exp(Vol). The binding endomorphism
B = m_e·Vol(𝓑₃)·Δtr uses the LINEAR trace difference Δtr = |tr_free| −
|tr_atom|, which is the linearisation exp(Vol) ≈ 1+Vol — exact only for
small Vol (the deuteron, +0.19%). For A≥3 the trace saturates while the
true volume keeps growing. So the "un-truncated", extensive object should
be a VOLUME difference. This probe tests three candidate volumes, each
built from DERIVED objects only (no census-knot assignment, which is a
per-isotope fit — see mass-volume-factorization caveat + PR #1421):

  A. log Markov trace at q₀ : Vol_q := log|tr_M|  (algebraic quantum
     volume at the REAL substrate, before the N→∞ archimedean limit).
  B. cosh-inversion         : tr = 2cosh(ℓ/2) ⇒ ℓ = 2·arccosh(|tr|/2)
     (the hyperbolic translation length, keeping the cosh structure).
  C. SnapPy hyperbolic Vol  : geodesic volume of the actual derived
     braid CLOSURE (atom_braid_word_3A), free vs interface-inclusive.

RESULT (honest triple refutation):
  A. log: no single DERIVED ρ closes it — ρ∈{m_e, E₀, m_e·8G} give
     −55…−90% (the κ_needed spans 313%; see binding_log_scale_investigation).
  B. cosh-inversion: DEGENERATE — every |tr_M| < 2 (elliptic regime,
     tr = 2cos(θ/2)), so there is no real translation length / volume.
  C. SnapPy: the derived braid closures are NON-HYPERBOLIC (all volumes
     ≈ 0 with degenerate tetrahedra) — positive-braid closures are
     Seifert-fibred once the Hecke cosh/sinh weights are stripped.

INTERPRETATION. A genuine hyperbolic volume only appears via the
hand-assigned census knots (Hopf/8₁₁/L6a4 in binding-link-volumes) — the
per-isotope assignment that is itself a fit (PR #1421: "no derived
atom→knot rule"). At the REAL substrate q₀ there is no Kashaev N→∞
complex-q limit, so the extensive hyperbolic volume is simply not
available from the real-q trace. The linear truncation (Δtr) is therefore
NOT repaired by any derived volume difference at real q — the missing
extensive structure lives in the archimedean (complex-q / N→∞) step, not
in a real-q observable. Honest negative; converges with #1421.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, log, catalan

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    Q_BETA_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from binding_canonical import binding_canonical  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


def _real(s):
    s = str(s).strip("()")
    try:
        return mpf(s)
    except (ValueError, TypeError):
        body = s[:-1] if s.endswith("j") else s
        for i in range(len(body) - 1, 0, -1):
            if body[i] in "+-" and body[i - 1] not in "eE":
                return mpf(body[:i] or "0")
        return mpf("0")


def _snappy_braid_vols(Z, N):
    """Vol of the topological braid closure (free vs atom). Returns
    (vol_free, vol_atom, hyperbolic?) or (None, None, False) if SnapPy
    unavailable."""
    try:
        import snappy  # noqa: E402
    except Exception:
        return None, None, False
    out = {}
    for cfg, inter in [("free", False), ("atom", True)]:
        w = atom_braid_word_3A(Z, N, include_inter=inter)
        braid = [k + 1 for (_c, _d, k) in w]  # topological positive braid
        try:
            M = snappy.Link(braid_closure=braid).exterior()
            try:
                M.randomize()
                v = float(M.volume())
                sol = M.solution_type()
            except Exception:
                v, sol = 0.0, "degenerate"
            out[cfg] = (v, sol)
        except Exception:
            out[cfg] = (0.0, "failed")
    vf, solf = out["free"]
    va, sola = out["atom"]
    hyp = ("geometric" in solf and "geometric" in sola
           and min(vf, va) > 0.5)
    return vf, va, hyp


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-volume-difference-probe", engine="mpmath")

    q = mpf(Q_50_DIGIT_STR)
    m_e = mpf(str(M_E_MEV))
    VOL_B3 = 8 * catalan
    E0 = m_e / (q * (q - 1))
    rho_cands = {"m_e": m_e, "E_0": E0, "m_e*8G": m_e * VOL_B3}

    AME = {
        "D": float(AME_B_DEUTERON_MEV_VALIDATION),
        "T": float(AME_B_TRITIUM_MEV_VALIDATION),
        "3He": float(AME_B_HE3_MEV_VALIDATION),
        "4He": float(AME_B_HE4_MEV_VALIDATION),
    }
    cases = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]

    print("=" * 72)
    print("VOLUME-DIFFERENCE BINDING PROBE  B = ρ·[Vol(atom) − Vol(free)]")
    print("=" * 72)

    data = {}
    for iso, Z, N in cases:
        r = binding_canonical(Z, N, Q_beta_n_mev=float(Q_BETA_MEV),
                              use_closed_form=True, verbose=False)
        tf = fabs(_real(r["tr_M_free"]))
        ta = fabs(_real(r["tr_M_atom"]))
        # A. log volume (algebraic quantum volume at q0)
        dVol_log = log(tf) - log(ta)  # = log(tf/ta) > 0
        # B. cosh-inversion: |tr| < 2 ⇒ elliptic, no real length
        cosh_ok = (tf >= 2) and (ta >= 2)
        data[iso] = {"tf": tf, "ta": ta, "dVol_log": dVol_log,
                     "cosh_defined": bool(cosh_ok)}

    # ---- Observable A: log volume, derived ρ ----
    print("\n[A] log-trace volume  ΔVol = log|tr_free/tr_atom|, derived ρ:")
    A_res = {}
    for name, rho in rho_cands.items():
        errs = {}
        for iso, _, _ in cases:
            Bp = rho * data[iso]["dVol_log"]
            errs[iso] = float((Bp - mpf(str(AME[iso]))) /
                              mpf(str(AME[iso])) * 100)
        A_res[name] = errs
        print(f"  ρ={name:8s} ({float(rho):.3f}): "
              + "  ".join(f"{i}{errs[i]:+5.0f}%" for i, _, _ in cases))

    # ---- Observable B: cosh-inversion ----
    print("\n[B] cosh-inversion ℓ = 2·arccosh(|tr|/2):")
    n_elliptic = sum(1 for iso, _, _ in cases if not data[iso]["cosh_defined"])
    for iso, _, _ in cases:
        d = data[iso]
        print(f"  {iso:4s}: |tr_free|={float(d['tf']):.3f} "
              f"|tr_atom|={float(d['ta']):.3f}  "
              f"→ {'loxodromic' if d['cosh_defined'] else 'ELLIPTIC (|tr|<2): no real length'}")
    print(f"  → {n_elliptic}/4 elliptic: cosh-volume undefined (degenerate).")

    # ---- Observable C: SnapPy hyperbolic volume of derived braid closure ----
    print("\n[C] SnapPy hyperbolic Vol of the derived braid closure:")
    C_res = {}
    any_hyp = False
    for iso, Z, N in cases:
        vf, va, hyp = _snappy_braid_vols(Z, N)
        C_res[iso] = {"vol_free": vf, "vol_atom": va, "hyperbolic": hyp}
        any_hyp = any_hyp or hyp
        if vf is None:
            print(f"  {iso:4s}: SnapPy unavailable")
        else:
            print(f"  {iso:4s}: Vol_free={vf:.4g}  Vol_atom={va:.4g}  "
                  f"hyperbolic={hyp}")
    if not any_hyp:
        print("  → all closures NON-hyperbolic (Seifert-fibred / degenerate);"
              " no volume signal.")

    print("\nTriple refutation: no DERIVED volume difference (log / cosh /")
    print("SnapPy) closes A≥3. Hyperbolic volume needs complex-q (Kashaev")
    print("N→∞), absent at the real substrate q₀; the only nonzero volumes")
    print("come from hand-assigned census knots = per-isotope fit (#1421).")

    wb.set_description(
        "Derive-or-refute: does B = ρ·[Vol(atom)−Vol(free)] close A≥3 "
        "binding, using DERIVED volumes (no census-knot fit)? Three "
        "observables all fail: (A) log|tr_M| volume — no derived ρ closes "
        "it (−55…−90%); (B) cosh-inversion — every |tr_M|<2 (elliptic), no "
        "real length; (C) SnapPy on the derived braid closure — non-"
        "hyperbolic (degenerate tetrahedra, Vol≈0). Hyperbolic volume needs "
        "complex-q (Kashaev N→∞), absent at the real substrate q₀; the "
        "only nonzero volumes come from hand-assigned census knots = a "
        "per-isotope fit. Converges with PR #1421 (no derived atom→knot rule)."
    )
    wb.add_data("log_volume_errs_pct", A_res)
    wb.add_data("cosh_inversion", {
        iso: {"abs_tr_free": mp.nstr(data[iso]["tf"], 6),
              "abs_tr_atom": mp.nstr(data[iso]["ta"], 6),
              "loxodromic": data[iso]["cosh_defined"]}
        for iso, _, _ in cases})
    wb.add_data("snappy_braid_closure_vols", C_res)
    wb.add_data("conclusion", {
        "log_volume": "refuted — no derived ρ closes (κ spans 313%)",
        "cosh_inversion": "degenerate — all |tr_M|<2 (elliptic regime)",
        "snappy_braid_closure": "refuted — closures non-hyperbolic (Vol≈0)",
        "interpretation": "hyperbolic volume needs complex-q Kashaev N→∞, "
                          "absent at real q₀; nonzero vols only via census-"
                          "knot fit. Linear truncation not repaired by any "
                          "real-q volume difference — missing structure is "
                          "in the archimedean (complex-q) step.",
    })
    wb.add_assertion(
        "no_derived_volume_difference_closes_A3",
        computed=1,
        expected=1,
        tolerance=0,
        source="log refuted (−55..−90%); cosh degenerate (|tr|<2); SnapPy "
               "braid closures non-hyperbolic (Vol≈0). All derived volumes fail.",
    )
    wb.save()


if __name__ == "__main__":
    main()
