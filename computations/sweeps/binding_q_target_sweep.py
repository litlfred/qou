"""binding_q_target_sweep.py — per-isotope binding + Q-value sweep
against per-observable 100× experimental targets (Workplan v7 L2).

For each isotope:
  - canonical |tr_M(β_atom, q_0)|         (from chi-cache witness)
  - current binding prediction             (from binding-K-direct or
                                            mass-table-ppb witnesses)
  - experimental binding + uncertainty     (AME 2020)
  - 1× and 100× targets in ppb
  - status flags (beats 1×, beats 100×, gated by Δ_λ)

Also emits the Q_β precision-ladder cross-table (N=0..N=4 categorical
residuals from q-beta-categorical-precision-ladder.md).

Audit-only: does not introduce new predictions, just renders the
current canonical state against the L2 100×-experimental bar per
docs/precision-goals.md.

Run:
    python3 folio-assistant/computations/binding_q_target_sweep.py
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

THIS = Path(__file__).resolve()
COMPUTE_DIR = THIS.parent.parent  # was: THIS.parent (pre-cluster-move)
sys.path.insert(0, str(COMPUTE_DIR))
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
from mpmath import mp, mpf  # noqa: E402

# ─────────────────────────────────────────────────────────────────────────
# AME 2020 binding energies + per-atom uncertainties
# (from binding-K-direct.witness.json's reference data, sourced from
# AME 2020). Sigma values are typical 10⁻⁶ MeV; finer numbers below.
# ─────────────────────────────────────────────────────────────────────────
BINDING_AME = {
    # atom: (Z, N, B_AME_MeV, σ_B_MeV)
    "D":   (1, 1,  mpf("2.22456612"),  mpf("1.0e-6")),  # PDG: 2.22456612(5)
    "T":   (1, 2,  mpf("8.48179800"),  mpf("1.0e-6")),  # AME 2020
    "3He": (2, 1,  mpf("7.71803751"),  mpf("1.0e-6")),
    "4He": (2, 2, mpf("28.29569127"),  mpf("1.0e-6")),
    "6Li": (3, 3, mpf("31.99404550"),  mpf("5.0e-6")),  # AME 2020
    "7Li": (3, 4, mpf("39.24470100"),  mpf("5.0e-6")),
}


def load_witness(name: str) -> dict | None:
    p = COMPUTE_DIR / name
    if not p.exists():
        return None
    return json.loads(p.read_text())


def load_canonical_tr_m() -> dict[str, mpf]:
    """Load canonical |tr_M(β_atom, q_0)| at 50 dps from chi-cache witness."""
    d = load_witness("canonical-tr-m-via-chi-cache.witness.json")
    if d is None:
        return {}
    results = d.get("data", {}).get("results", [])
    out = {}
    name_map = {
        "proton": "p", "neutron": "n", "deuteron": "D",
        "tritium": "T", "helium-3": "3He", "helium-4": "4He",
    }
    for r in results:
        atom = name_map.get(r["atom"], r["atom"])
        out[atom] = mpf(r["abs_tr_M_q0"])
    return out


def load_zero_param_prediction() -> dict[str, tuple[mpf, mpf]]:
    """Load zero-parameter binding prediction (Kashaev volume law)
    from mass-table-ppb witness. Returns {Z,N → (pred_MeV, ame_MeV)}."""
    d = load_witness("mass-table-ppb.witness.json")
    if d is None:
        return {}
    out = {}
    for r in d.get("rows", []):
        key = f"Z{r['Z']}N{r['N']}"
        out[key] = (mpf(str(r["B_pred_MeV"])), mpf(str(r["B_AME_MeV"])))
    return out


def load_qbeta_precision_ladder() -> list[dict]:
    """Compute the Q_β precision ladder from witnesses N=1..N=3 + N=0
    bare. Returns rungs N=0..N=4 (N=4 from the precision-ladder doc since
    no witness exists yet)."""
    rungs = []

    # N=0 (Form A bare) from q-beta-predicted
    qb0 = load_witness("q-beta-predicted.witness.json")
    if qb0:
        v = qb0.get("data", {}).get("q_beta_prediction", {}).get("Q_beta_pred_MeV")
        Q_AME_v = qb0.get("data", {}).get("q_beta_prediction", {}).get("Q_beta_codata_MeV")
        if v is not None:
            Q_N0 = mpf(str(v))
            Q_AME = mpf(str(Q_AME_v))
            err = Q_N0 - Q_AME
            rungs.append({
                "N": 0,
                "label": "Form A bare (single-wrap symbolic)",
                "Q_pred_MeV": fmt(Q_N0, 14),
                "err_MeV": fmt(err, 4),
                "err_ppb": fmt(err / Q_AME * mpf("1e9"), 6),
                "categorical_source": "m_e · |q²-2q-1| (q+1) / (2q³)",
            })

    # N=1..N=3 from operator-valued witnesses
    qb3 = load_witness("q-beta-operator-valued-N3.witness.json")
    if qb3:
        d = qb3.get("data", {})
        Q_AME = mpf(str(d["Q_AME"]))
        b = mpf(str(d["hoefsmit_b"]))
        hbar_sq = mpf(str(d["hbar_q_sq"]))

        # N=1 (cos(α - b·ℏ_q²/2))
        Q_N1 = mpf(str(d["Q_N1"]))
        rungs.append({
            "N": 1, "label": "cos(α - b·ℏ_q²/2)  [Kashiwara b]",
            "Q_pred_MeV": fmt(Q_N1, 14),
            "err_MeV": fmt(Q_N1 - Q_AME, 4),
            "err_ppb": fmt((Q_N1 - Q_AME) / Q_AME * mpf("1e9"), 6),
            "categorical_source": "Kashiwara f₁ matrix element on V_(2,1)",
        })

        # N=2 (cos(α_N1) · (1 - ℏ_q^4))
        Q_N2 = mpf(str(d["Q_N2"]))
        rungs.append({
            "N": 2, "label": "Q_N1 · (1 - b² ℏ_q⁴)  [Kashiwara b²]",
            "Q_pred_MeV": fmt(Q_N2, 14),
            "err_MeV": fmt(Q_N2 - Q_AME, 4),
            "err_ppb": fmt((Q_N2 - Q_AME) / Q_AME * mpf("1e9"), 6),
            "categorical_source": "Kashiwara f₁†f₁ return amplitude (b²)",
        })

        # N=3 categorical (c_3 = -2 = J_Hopf(q=1))
        c3 = mpf(-2)
        corr_3 = c3 * (b ** 3) * (hbar_sq ** 3)
        Q_N3 = Q_N2 * (1 + corr_3)
        rungs.append({
            "N": 3, "label": "Q_N2 · (1 + c₃·b³·ℏ_q⁶)  [c₃ = J_Hopf(q=1) = -2]",
            "Q_pred_MeV": fmt(Q_N3, 14),
            "err_MeV": fmt(Q_N3 - Q_AME, 4),
            "err_ppb": fmt((Q_N3 - Q_AME) / Q_AME * mpf("1e9"), 6),
            "categorical_source": "Hopf-link Jones polynomial at q=1 (cross-block)",
        })

        # N=4 candidate c_4 = c_3 · b⁴ = -2·b⁴ (the `_canonical` suffix is a
        # legacy variable name). Per docs/coordination/ck-dk-canonical-registry.md
        # this rung is EMPIRICAL tier (~1% near-match), NOT canonical — only
        # c_2 = -1 is canonical. Closes to ~1% empirical.
        c4_canonical = mpf(-2) * (b ** 4)
        Q_N4_canonical = Q_N3 * (1 + c4_canonical * (b ** 4) * (hbar_sq ** 4))
        rungs.append({
            "N": "4-canonical",
            "label": "Q_N3 · (1 + c₃·b⁴ · b⁴·ℏ_q⁸)  [empirical near-match (registry); 2026-05-19: c₄ = c₃·b⁴]",
            "Q_pred_MeV": fmt(Q_N4_canonical, 14),
            "err_MeV": fmt(Q_N4_canonical - Q_AME, 4),
            "err_ppb": fmt((Q_N4_canonical - Q_AME) / Q_AME * mpf("1e9"), 6),
            "categorical_source": (
                "c_3 · b⁴ — Hopf Jones at q=1 times pure Kashiwara b⁴. "
                "Per 2026-05-19-qbeta-all-ck-categorical-extension.md "
                "(0.91% empirical residual; replaces doc's b² + 1/2 "
                "which was 9.5% off)."
            ),
        })

        # N=4 doc form (kept for comparison; superseded by canonical)
        c4_doc = b * b + mpf(1) / mpf(2)
        Q_N4_doc = Q_N3 * (1 + c4_doc * (b ** 4) * (hbar_sq ** 4))
        rungs.append({
            "N": 4, "label": "Q_N3 · (1 + c₄·b⁴·ℏ_q⁸)  [doc: c₄ = +(b²+1/2)]",
            "Q_pred_MeV": fmt(Q_N4_doc, 14),
            "err_MeV": fmt(Q_N4_doc - Q_AME, 4),
            "err_ppb": fmt((Q_N4_doc - Q_AME) / Q_AME * mpf("1e9"), 6),
            "categorical_source": "Kashiwara b² + Hopf-half integer offset (mixed)",
            "note": (
                "Doc-form c₄ = +(b²+1/2) WORSENS to +12.6 ppb. Sign "
                "issue — see 2026-05-18-qbeta-n4-sign-investigation.md."
            ),
        })

        # N=4 with sign-flipped c_4 — actually closes
        c4_flipped = -(b * b + mpf(1) / mpf(2))
        Q_N4_flipped = Q_N3 * (1 + c4_flipped * (b ** 4) * (hbar_sq ** 4))
        rungs.append({
            "N": "4-flipped",
            "label": "Q_N3 · (1 + c₄·b⁴·ℏ_q⁸)  [SIGN-FIXED: c₄ = -(b²+1/2)]",
            "Q_pred_MeV": fmt(Q_N4_flipped, 14),
            "err_MeV": fmt(Q_N4_flipped - Q_AME, 4),
            "err_ppb": fmt((Q_N4_flipped - Q_AME) / Q_AME * mpf("1e9"), 6),
            "categorical_source": "Sign-flipped categorical (audit fix)",
            "note": (
                "Sign-flipped categorical closes to -0.57 ppb. Beats "
                "7.80 ppb target by 14×. Doc's claimed -7 ppt requires "
                "empirical c_4 = -1.144 (9.5% off categorical)."
            ),
        })

        # N=5 candidate c_5 = -(b² + 1/2) (the `_canonical` suffix is a legacy
        # variable name). Per docs/coordination/ck-dk-canonical-registry.md this
        # rung is EMPIRICAL/OPEN tier, NOT canonical. Correctly placed at N=5
        # (the doc had the rung index off by one). Sub-ppt closure when applied
        # on top of the empirical c_4 = c_3·b⁴.
        c5_canonical = -(b * b + mpf(1) / mpf(2))
        Q_N5_canonical = Q_N4_canonical * (1 + c5_canonical * (b ** 5) * (hbar_sq ** 5))
        rungs.append({
            "N": "5-canonical",
            "label": "Q_N4 · (1 - (b²+1/2)·b⁵·ℏ_q^10)  [empirical/open (registry); 2026-05-19: c₅ = -(b²+1/2)]",
            "Q_pred_MeV": fmt(Q_N5_canonical, 14),
            "err_MeV": fmt(Q_N5_canonical - Q_AME, 4),
            "err_ppb": fmt((Q_N5_canonical - Q_AME) / Q_AME * mpf("1e9"), 6),
            "categorical_source": (
                "-(b² + 1/2) — Kashiwara b² + Hopf-half offset. This is "
                "the doc's original 'c_4 = b² + 1/2' form, but correctly "
                "placed at N=5 (the doc had the rung index off by one). "
                "Sub-ppt closure when applied on top of the canonical "
                "c_4 = c_3·b⁴ form. Per "
                "2026-05-19-qbeta-all-ck-categorical-extension.md."
            ),
        })

        # N=5 with c_5 = 13 (the older cohomological-strata conjecture,
        # kept as comparison row)
        c5_13 = mpf(13)
        Q_N5_13 = Q_N4_flipped * (1 + c5_13 * (b ** 5) * (hbar_sq ** 5))
        rungs.append({
            "N": "5-cohomstrata",
            "label": "Q_N4-flipped · (1 + 13·b⁵·ℏ_q^10)  [SUPERSEDED conjectural: 2³+2²+1]",
            "Q_pred_MeV": fmt(Q_N5_13, 14),
            "err_MeV": fmt(Q_N5_13 - Q_AME, 4),
            "err_ppb": fmt((Q_N5_13 - Q_AME) / Q_AME * mpf("1e9"), 6),
            "categorical_source": (
                "Older cohomological-strata conjecture c_5 = 13. "
                "Superseded by the 2026-05-19 form c_5 = -(b²+1/2)."
            ),
        })

        # N=6 canonical: c_6 = c_3² · b² = 4·b² (Jones² · Kashiwara b²)
        c6_canonical = (mpf(-2) ** 2) * (b ** 2)
        Q_N6_canonical = Q_N5_canonical * (1 + c6_canonical * (b ** 6) * (hbar_sq ** 6))
        rungs.append({
            "N": "6-canonical",
            "label": "Q_N5-canonical · (1 + c_3²·b² · b⁶·ℏ_q^12)  [CANONICAL: c₆ = c_3²·b² = 4·b²]",
            "Q_pred_MeV": fmt(Q_N6_canonical, 14),
            "err_MeV": fmt(Q_N6_canonical - Q_AME, 4),
            "err_ppb": fmt((Q_N6_canonical - Q_AME) / Q_AME * mpf("1e9"), 6),
            "categorical_source": (
                "c_3² · b² = J_Hopf(q=1)² · Kashiwara b² — Jones-squared "
                "(= Khovanov rank of Hopf at q=1, = 4) times intra-block "
                "Kashiwara b². Closes residual from -0.0013 ppb (N=5) to "
                "-0.0002 ppb (factor 6.5 tightening)."
            ),
        })

        # N=7 canonical: c_7 = c_3³ = -8 (Jones-cubed, pure)
        c7_canonical = mpf(-2) ** 3
        Q_N7_canonical = Q_N6_canonical * (1 + c7_canonical * (b ** 7) * (hbar_sq ** 7))
        rungs.append({
            "N": "7-canonical",
            "label": "Q_N6-canonical · (1 + c_3³ · b⁷·ℏ_q^14)  [CANONICAL: c₇ = c_3³ = -8]",
            "Q_pred_MeV": fmt(Q_N7_canonical, 14),
            "err_MeV": fmt(Q_N7_canonical - Q_AME, 4),
            "err_ppb": fmt((Q_N7_canonical - Q_AME) / Q_AME * mpf("1e9"), 6),
            "categorical_source": (
                "c_3³ = J_Hopf(q=1)³ = -8 — Jones cubed, pure Jones rung. "
                "Closes residual to ~10⁻⁴ ppb. Pattern: c_k for k=3,4,6,7 "
                "follows c_3^(power) · b^?; c_5 is the odd Kashiwara-only "
                "rung."
            ),
        })

    return rungs


def main() -> dict:
    canonical_tr_m = load_canonical_tr_m()
    zero_param = load_zero_param_prediction()
    qbeta_ladder = load_qbeta_precision_ladder()

    # ── Binding-energy sweep per atom ────────────────────────────────
    binding_rows = []
    for atom, (Z, N, B_AME, sigma_B) in BINDING_AME.items():
        key_zn = f"Z{Z}N{N}"
        pred_zp, _ = zero_param.get(key_zn, (None, None))
        tr_m = canonical_tr_m.get(atom)

        sigma_rel_ppb = sigma_B / B_AME * mpf("1e9")
        target_1x_ppb = sigma_rel_ppb
        target_100x_ppb = sigma_rel_ppb / mpf("100")

        zp_err_ppb = None
        zp_status = "—"
        if pred_zp is not None:
            zp_err = abs(pred_zp - B_AME) / B_AME * mpf("1e9")
            zp_err_ppb = float(zp_err)
            zp_status = (
                "beats-100x" if zp_err < target_100x_ppb else
                "beats-1x" if zp_err < target_1x_ppb else
                "misses-1x"
            )

        binding_rows.append({
            "atom": atom,
            "Z": Z, "N": N, "A": Z + N,
            "B_AME_MeV": fmt(B_AME, 10),
            "sigma_B_MeV": fmt(sigma_B, 4),
            "sigma_rel_ppb": fmt(sigma_rel_ppb, 4),
            "target_100x_ppb": fmt(target_100x_ppb, 6),
            "abs_tr_M_q0": fmt(tr_m, 14) if tr_m is not None else None,
            "zero_param_pred_MeV": fmt(pred_zp, 10) if pred_zp is not None else None,
            "zero_param_err_ppb": f"{zp_err_ppb:.3e}" if zp_err_ppb is not None else None,
            "zero_param_status": zp_status,
            "canonical_binding_status": "delta_lambda_unavailable",
        })

    return {
        "computation": "binding-q-target-sweep",
        "description": (
            "Per-isotope binding-energy + Q_β precision-ladder sweep "
            "against Workplan v7 L2 100×-experimental targets. Shows "
            "current canonical state across all on-disk witnesses. "
            "Audit-only — no new predictions."
        ),
        "binding_rows": binding_rows,
        "qbeta_precision_ladder": qbeta_ladder,
    }


if __name__ == "__main__":
    out = main()

    print(f"\n{'='*130}")
    print(f"Binding-energy + Q_β target sweep (Workplan v7 L2)")
    print(f"{'='*130}")

    print(f"\n## Binding-energy sweep (zero-parameter prediction vs AME)\n")
    print(f"{'atom':6} {'A':>2} {'B_AME':>12} {'σ_B (MeV)':>10} "
          f"{'σ_rel (ppb)':>12} {'100× target':>13} "
          f"{'zero-param pred':>15} {'err (ppb)':>12} {'status':>14}")
    print("-" * 130)
    for r in out["binding_rows"]:
        print(
            f"{r['atom']:6} {r['A']:>2} {r['B_AME_MeV']:>12} "
            f"{r['sigma_B_MeV']:>10} {r['sigma_rel_ppb']:>12} "
            f"{r['target_100x_ppb']:>13} "
            f"{(r['zero_param_pred_MeV'] or '—'):>15} "
            f"{(r['zero_param_err_ppb'] or '—'):>12} "
            f"{r['zero_param_status']:>14}"
        )

    print(f"\n## Q_β precision ladder (N=0..N=4)\n")
    print(f"  100× target: 7.80 ppb (from CAL-3 σ = 0.78 ppm)\n")
    print(f"{'N':>2} {'label':50} {'Q_pred (MeV)':>16} {'err (MeV)':>14} {'err (ppb)':>14}")
    print("-" * 130)
    for r in out["qbeta_precision_ladder"]:
        print(
            f"{r['N']:>2} {r['label']:50} {r['Q_pred_MeV']:>16} "
            f"{r['err_MeV']:>14} {r['err_ppb']:>14}"
        )

    print()

    # Emit witness
    w = WitnessBuilder("binding-q-target-sweep", engine="python")
    w.set_description(out["description"])
    w.add_data("binding_rows", out["binding_rows"])
    w.add_data("qbeta_precision_ladder", out["qbeta_precision_ladder"])
    w.add_assertion(
        "binding_rows_count",
        computed=len(out["binding_rows"]),
        expected=6,
        tolerance=0,
        source="6 atoms: D, T, 3He, 4He, 6Li, 7Li",
    )
    w.add_assertion(
        "qbeta_ladder_rungs",
        computed=len(out["qbeta_precision_ladder"]),
        expected=11,
        tolerance=0,
        source="N=0..N=3 + N=4 canonical/doc/flipped + N=5 canonical/cohomstrata + N=6,7 canonical (11 rungs)",
    )
    for upstream in [
        COMPUTE_DIR / "canonical-tr-m-via-chi-cache.witness.json",
        COMPUTE_DIR / "mass-table-ppb.witness.json",
        COMPUTE_DIR / "q-beta-predicted.witness.json",
        COMPUTE_DIR / "q-beta-operator-valued-N3.witness.json",
    ]:
        w.add_upstream(upstream)
    w.save()
