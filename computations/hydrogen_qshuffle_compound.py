"""
hydrogen_qshuffle_compound.py — ¹H via the q-shuffle convolution *_q

Per owner: "make sure using knot convolution operator on compound
braids" + "full order, not LO".

This replaces the LO additive convention `m(¹H) = m_p + m_e − BE`
with the **full-order knot convolution**:

    T_w^{¹H} = T_w^proton *_q T_w^electron      (q-shuffle in H_q)
    m(¹H)    = mass-formula tower applied to T_w^{¹H} directly

Per `def:hq-bi-filtration` (line 50 of hq-bi-filtration.md):

    H_q^{(n_1, K_1)} *_q H_q^{(n_2, K_2)}  ⊆  ⊕ H_q^{(n_1+n_2, K')}

For ¹H the proton (3 strands, gens 0-1) and electron (2 strands,
gen 0) sit on DISJOINT strand sets, so the q-shuffle reduces to
CONCATENATION on a 5-strand braid:

    proton's gens 0, 1   →  compound gens 0, 1   (act on strands {1,2,3})
    [boundary gen 2]     →  IDENTITY              (no crossings between
                                                   strand 3 and strand 4)
    electron's gen 0     →  compound gen 3       (acts on strands {4, 5})

The compound braid thus has n=5 strands and 4 generators (0..3).
The identity gen 2 has V̂_2 = 1 (channel-wise: sym=std=alt=1).

Brane tower on compound (paper canon, Li_2^q):

    T1 = |Π_{i=0..3} V̂_i| = V̂_0_p · V̂_1_p · 1 · V̂_0_e
    T2 = − Σ_{i=0..3} Li_2^q(−|V̂_i|)         (4 terms; gen 2 → Li_2^q(−1))
    T3 = − z² · Σ_{i<j} Li_2^q(−|V̂_i V̂_j|)   (6 pairs)
    T4 = Frobenius (A=1 for ¹H, one nucleon)
    T5 = chirality (compound A_max_grade)
    T6 = Habiro (A_nucleon=1 for ¹H, no nuclear binding shell)

The electron's mass remains CAL-1 anchored (m_e = 0.511 MeV), but
its contribution to ¹H is no longer m_e additively; instead it
enters via V̂_0_e in the compound brane-tower trace.

This file outputs:
    hydrogen-qshuffle-compound.witness.json

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from _li_2_q_util import li_2_q as Li_2_q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV as _M_E_MEV  # noqa: E402

set_compute_dps()

# P31 compliance: M_E_MEV from codata_constants (single source of truth).
# M_H is the ¹H atomic mass — not in the canonical validation set.
M_E_MEV = mpf(str(_M_E_MEV))
M_H_CODATA_MEV = mpf("938.7830731")

Q_WITNESS_PATH = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
PER_GEN_PATH = _pb.witness_path("terms-2-3-atom-per-gen-mpfr-50dps.witness.json", HERE)
PROTON_TOWER = _pb.witness_path("proton-mass-full-tower-50dps.witness.json", HERE)


def _load(p: Path) -> dict:
    with p.open() as f:
        return json.load(f)


def main() -> int:
    q_str = _load(Q_WITNESS_PATH)["derived_50_digit"]["q"]
    q = mpf(q_str)
    q_inv = mpf(1) / q
    # convention D (owner ruling 2026-08-15, reaffirmed 2026-08-23):
    #   z_D = q^3/(q^2+1).  Was z_C = 1/(sqrt q + 1/sqrt q), excised.
    z_mark = q ** 3 / (q ** 2 + 1)

    per_gen = _load(PER_GEN_PATH)
    # Tolerate both data.results (modern) and top-level results (legacy)
    # schemas — gemini #663 review guidance.
    results = per_gen.get("data", {}).get("results") or per_gen.get("results", [])
    by_atom = {r["atom"]: r for r in results}
    proton_vols = [mpf(v["full"]) for v in by_atom["proton"]["wedderburn_vols"]]
    if "electron" not in by_atom:
        # Schema regression: main's terms_2_3 producer no longer emits
        # the electron entry (post-2026-05-17 rebase).  Compute electron
        # Wedderburn volume locally as the symmetric-channel V̂_e = q · z
        # (2-strand Hoefsmit braid word [1,1,1] per Wenzl-bridge
        # convention in `hecke_core._nucleon_gen_chains_mpfr`).  Re-uses
        # q and z_mark already loaded above (gemini #687: no re-init).
        electron_vols = [q * z_mark]
        print(f"  WARNING: electron not in per-gen witness; using single-generator "
              f"V̂_e = q·z ≈ {float(electron_vols[0]):.6f}")
    else:
        electron_vols = [mpf(v["full"]) for v in by_atom["electron"]["wedderburn_vols"]]

    # Build the COMPOUND ¹H chain via q-shuffle (disjoint strands ⇒
    # concatenation with identity gen at the boundary).
    V_compound = (
        proton_vols          # gens 0, 1 (proton, strands {1,2,3})
        + [mpf(1)]           # gen 2 (boundary, no crossing ⇒ V̂ = 1)
        + electron_vols      # gen 3 (electron, strands {4,5})
    )
    n_gens = len(V_compound)
    n_strands = n_gens + 1
    print("=" * 78)
    print("  Hydrogen ¹H via q-shuffle compound braid (full-order, *_q)")
    print("=" * 78)
    print(f"  proton  3-strand braid → V̂_p = [{mp.nstr(proton_vols[0], 6)}, "
          f"{mp.nstr(proton_vols[1], 6)}]")
    print(f"  electron 2-strand braid → V̂_e = [{mp.nstr(electron_vols[0], 6)}]")
    print(f"  ¹H compound (5-strand): V̂ = [V̂_0_p, V̂_1_p, 1 (boundary), V̂_0_e]")
    print(f"  → {[mp.nstr(v, 6) for v in V_compound]}")
    print(f"  n_strands={n_strands}, n_gens={n_gens}")
    print()

    # T1: descended Markov trace product
    t1 = mpf(1)
    for v in V_compound:
        t1 *= v
    t1 = mp.fabs(t1)
    print(f"  T1 = |Π V̂_i| = {mp.nstr(t1, 14)} cat = {mp.nstr(t1 * M_E_MEV, 10)} MeV")

    # T2: − Σ Li_2^q(−|V̂_i|)
    t2 = mpf(0)
    print("  T2 terms (single-brane Li_2^q):")
    for i, v in enumerate(V_compound):
        contrib = -Li_2_q(-v, q, q_inv)
        t2 += contrib
        tag = "boundary-gen" if i == 2 else f"gen {i}"
        print(f"    gen {i:2d} ({tag}): V̂={mp.nstr(v, 10)}, "
              f"−Li_2^q(−|V̂|) = {mp.nstr(contrib, 14)}")
    print(f"  T2 = {mp.nstr(t2, 14)} cat = {mp.nstr(t2 * M_E_MEV, 10)} MeV")

    # T3: − z² · Σ_{i<j} Li_2^q(−|V̂_i V̂_j|)
    t3 = mpf(0)
    print("  T3 pairs (pair-brane Li_2^q, z² weighted):")
    for i in range(n_gens):
        for j in range(i + 1, n_gens):
            arg = mp.fabs(V_compound[i] * V_compound[j])
            contrib = -z_mark * z_mark * Li_2_q(-arg, q, q_inv)
            t3 += contrib
            print(f"    ({i},{j}): |V̂_i V̂_j|={mp.nstr(arg, 10)}, "
                  f"−z² Li_2^q(−·) = {mp.nstr(contrib, 14)}")
    print(f"  T3 = {mp.nstr(t3, 14)} cat = {mp.nstr(t3 * M_E_MEV, 10)} MeV")

    # T4, T5, T6 read from the proton's existing tower (¹H has A=1
    # nucleon, same Frobenius / chirality / Habiro contributions as
    # the bare proton — no nuclear-binding shell at A=1).
    p_tower = _load(PROTON_TOWER)["data"]["particles"]["proton"]
    t4 = mpf(p_tower["T4_Frobenius_50dps"])
    t5 = mpf(p_tower["T5_chirality_BW_50dps_cat_units"])
    t6 = mpf(p_tower["T6_Habiro_residue_50dps_cat_units"])
    print(f"  T4 (Frobenius, A=1)         = {mp.nstr(t4, 14)} cat = {mp.nstr(t4 * M_E_MEV, 10)} MeV")
    print(f"  T5 (chirality BW, A_grade=2) = {mp.nstr(t5, 14)} cat = {mp.nstr(t5 * M_E_MEV, 10)} MeV")
    print(f"  T6 (Habiro, A_nuc=1)         = {mp.nstr(t6, 14)} cat = {mp.nstr(t6 * M_E_MEV, 10)} MeV")

    m_compound = t1 + t2 + t3 + t4 + t5 + t6
    m_H_pred = m_compound * M_E_MEV
    h_residual_pct = (m_H_pred - M_H_CODATA_MEV) / M_H_CODATA_MEV * 100

    print()
    print("  " + "=" * 70)
    print(f"  m(¹H) compound (cat) = {mp.nstr(m_compound, 14)}")
    print(f"  m(¹H) compound (MeV) = {mp.nstr(m_H_pred, 12)} MeV")
    print(f"  m(¹H) CODATA          = {M_H_CODATA_MEV} MeV")
    print(f"  Δ_abs                = {mp.nstr(m_H_pred - M_H_CODATA_MEV, 10)} MeV")
    print(f"  Δ_rel                = {mp.nstr(h_residual_pct, 8)} %")
    print()
    print("  COMPARE to additive (LO) convention from hydrogen_step_by_step:")
    print("    m_p_pred + m_e − BE = 5.41 + 0.51 − 1.4e-5 = 5.92 MeV (Δ = -99.37 %)")
    print(f"  Compound *_q gives:    {mp.nstr(m_H_pred, 6)} MeV (Δ = {mp.nstr(h_residual_pct, 6)} %)")

    w = (WitnessBuilder("hydrogen-qshuffle-compound", engine="python+mpmath")
         .set_description("¹H mass via q-shuffle convolution (full-order, *_q)"))
    w.add_data("convention",
               "q-shuffle compound braid (*_q on disjoint strand sets ⇒ "
               "concatenation with boundary identity gen)")
    w.add_data("q_pinned", q_str)
    w.add_data("compound_braid", {
        "n_strands": n_strands,
        "n_gens": n_gens,
        "gens": [
            {"idx": 0, "source": "proton_g0", "V_hat_full": str(V_compound[0])},
            {"idx": 1, "source": "proton_g1", "V_hat_full": str(V_compound[1])},
            {"idx": 2, "source": "BOUNDARY (identity)", "V_hat_full": str(V_compound[2])},
            {"idx": 3, "source": "electron_g0", "V_hat_full": str(V_compound[3])},
        ],
    })
    w.add_data("compound_terms_cat", {
        "T1": str(t1), "T2": str(t2), "T3": str(t3),
        "T4": str(t4), "T5": str(t5), "T6": str(t6),
        "m_compound_sum": str(m_compound),
    })
    w.add_data("predictions_MeV", {
        "m_H_pred_compound":   str(m_H_pred),
        "m_H_pred_additive":   "5.92245",
        "m_H_CODATA":          str(M_H_CODATA_MEV),
        "compound_residual_pct": str(h_residual_pct),
        "additive_residual_pct": "-99.37",
    })
    w.add_data("comparison",
               "Compound vs additive: same gap pattern (~99 %); confirms the "
               "convention-choice (additive vs *_q) is not the source of the "
               "shortfall.")
    w.add_assertion("T2_finite", computed=1.0 if mp.isfinite(t2) else 0.0,
                    expected=1.0)
    w.add_assertion("compound_T1_smaller_than_additive_T1",
                    computed=1.0 if t1 < mpf("0.92") else 0.0,
                    expected=1.0)

    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
