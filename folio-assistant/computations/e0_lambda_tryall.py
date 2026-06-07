#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""e0_lambda_tryall.py — falsification harness for 5 substrate-derived E_0^λ maps.

CONTEXT (read docs/audits/2026-06-01-e0-lambda-tryall-results.md):

The L2-Subgoal-1 gap reduces to ONE missing object: a PARAMETER-FREE map
χ^λ(K) → M_λ(K) giving substrate-derived per-block energies E_0^λ (MeV).
χ^λ is a DIMENSIONLESS trace and does NOT determine M_λ (which carries a
dimensional MeV scale). This harness tests 5 candidate constructions of E_0^λ,
ALL from cached substrate data (q₀, χ^λ, y_λ, dim, contents, ribbon twist,
seminormal eigenphases) — NEVER from B_AME or the deprecated fit.

THE ANCHORS (falsification test, NOT fit target):
  the deprecated `_deprecated/per_block_phi_q.py::fit_three_E0` produces
  per-block scales by LSQ.  We DO NOT try to reproduce those scales (they are
  pathological — E_0^std < 0, 575× ill-conditioned).  Instead the honest PASS
  bar is: does the candidate's substrate-derived per-block weight set {w_λ}
  map the *observed* particle masses with ONE positive global constant C
  (i.e. M(particle) = C · Σ_λ w_λ · mult_λ), zero per-block freedom?

  - PASS       : ONE positive C reproduces all 3 anchors (e⁻, p, n) to within
                 a defensible band (we use 1% — far looser than L2, but any
                 candidate that can't hit 1% with a global scale is dead).
  - LATENT-FIT : needs ≥1 tuned per-block parameter (i.e. 3 independent scales
                 = the original fit; or a per-particle constant).
  - FAIL       : wrong even WITH a global scale (residuals ≫ band, or the
                 weight set cannot distinguish the particles at all).

HARD DISCIPLINE: no tuning to {e⁻,p,n} or B_AME. If all 5 fail, report that —
no 6th fit (the Δ_λ gate already killed six).

@module folio-assistant/computations/e0_lambda_tryall
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from mpmath import mp, mpf, acos  # noqa: E402

# Substrate constants — canonical, B_AME-independent.
from qou_substrate.constants import Q, HA, Q_INV  # noqa: E402
from _li_2_q_util import vol_density_borromean  # noqa: E402

mp.dps = 50

Q0 = mpf(str(Q))
QI0 = mpf(1) / Q0
H = Q0 - QI0  # h = q − q⁻¹
HBAR_Q = 1 - QI0  # ℏ_q
M_E_MEV = mpf("0.51099895069")

# Observed masses (CODATA) — the ANCHORS (falsification targets, not fit data).
ANCHORS_MEV = {
    "electron": mpf("0.51099895069"),
    "proton": mpf("938.27208816"),
    "neutron": mpf("939.56542052"),
}

# ----------------------------------------------------------------------------
# Substrate per-block data for the 3-strand nucleon (H_3, blocks sym/std/alt).
# Loaded from the canonical χ cache (chi-neutron-h3-at-q0-50dps.witness.json):
# the per-block Hoefsmit characters χ^λ(β_nucleon) at q₀, with dim and y_λ.
# These are the χ^λ(K) substrate inputs — NOT from B_AME, NOT from the fit.
# ----------------------------------------------------------------------------
H3_BLOCKS = [(3,), (2, 1), (1, 1, 1)]  # sym, std, alt


def load_nucleon_blocks() -> dict:
    cache = json.loads((_pb.witness_path("chi-neutron-h3-at-q0-50dps.witness.json", HERE)).read_text())
    by = {tuple(e["partition"]): e for e in cache["by_partition"]}
    out = {}
    for lam in H3_BLOCKS:
        e = by[lam]
        out[lam] = {
            "chi": mpf(e["chi_lambda"]),
            "y": mpf(e["y_lambda"]),
            "dim": int(e["dim"]),
        }
    return out


def cells(lam):
    return [(r, c) for r, row in enumerate(lam) for c in range(row)]


def content_sum(lam):
    """Σ_box (col − row) — the quadratic-Casimir / ribbon content."""
    return sum(c - r for (r, c) in cells(lam))


def hook_lengths(lam):
    lam_conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    out = []
    for (r, c) in cells(lam):
        arm = lam[r] - c - 1
        leg = lam_conj[c] - r - 1
        out.append(arm + leg + 1)
    return out


def q_int(n: int) -> mpf:
    """[n]_q = (q^n − q^{-n})/(q − q⁻¹), n integer (may be 0)."""
    if n == 0:
        return mpf(0)
    return (Q0 ** n - QI0 ** n) / H


def qdim_lambda(lam) -> mpf:
    """Quantum dimension dim_q(λ) = ∏_box [hook(box)]_q^{-1} · [n]_q!  ...
    For small H_3 blocks we use the q-hook-content formula:
        dim_q(λ) = ∏_{box} [n + content(box)]_q / [hook(box)]_q
    with n = |λ| (number of strands).  This is the standard q-Weyl dim
    (Stanley / Macdonald); at q→1 it returns the integer dim f^λ."""
    n = sum(lam)
    num = mpf(1)
    den = mpf(1)
    for (r, c) in cells(lam):
        cont = c - r
        num *= q_int(n + cont)
        den *= q_int(hook_lengths_at(lam, r, c))
    return num / den


def hook_lengths_at(lam, r, c):
    lam_conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    arm = lam[r] - c - 1
    leg = lam_conj[c] - r - 1
    return arm + leg + 1


# ----------------------------------------------------------------------------
# Anchor scoring.  Given a candidate's per-block weight w_λ (a substrate
# scalar per block), build the per-PARTICLE prediction and test against the
# 3 observed masses with ONE global positive constant.
#
# Per-particle aggregation: M(particle) = Σ_λ y_λ(particle) · w_λ · dim_λ,
# i.e. the Plancherel-weighted block sum (the SAME structure tr_M uses).
# For the electron (2-strand) we restrict to the 2 blocks of H_2; we reuse the
# nucleon block weights only where they share a partition shape (sym/alt are
# common; std differs).  Where a candidate's w_λ is the SAME function of λ for
# every particle (it must be, to be parameter-free), the ONLY per-particle
# input is the substrate y_λ(particle).  We use the cached y_λ.
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# Genuine per-block STRUCTURAL masses m^λ(particle) — the χ^λ-derived quantities
# that DIFFER by orders of magnitude across e⁻ (H_2), p, n (H_3).  Loaded from
# the deprecated per_block_phi_q.mass_per_block (the SAME structural object the
# deprecated fit_three_E0 fits scales against).  This is the discriminating
# input: the electron's per-block masses are ~1837× different from the nucleons'.
# A candidate's E_0^λ (per-block energy SCALE) maps these onto observed MeV:
#       M(particle) = C · Σ_λ E_0^λ · m^λ(particle).
# A parameter-free map provides E_0^λ from substrate, leaving ONLY the global C.
# ----------------------------------------------------------------------------
def particle_struct_masses() -> dict:
    """{particle: {block_name: m^block (cat units)}} for e⁻, p, n.
    block_name ∈ {sym, std, alt}.  From _deprecated/per_block_phi_q."""
    dep = HERE / "_deprecated"
    if str(dep) not in sys.path:
        sys.path.insert(0, str(dep))
    import per_block_phi_q as pbq  # noqa
    out = {}
    for name in ("electron", "proton", "neutron"):
        p = pbq.particle_braids()[name]
        b = pbq.mass_per_block(p["cross"], p["n_strands"])
        out[name] = {bn: mpf(str(b[bn]["block_mass"])) for bn in ("sym", "std", "alt")}
    return out


# Map H_3 partitions → block names (sym=[3], std=[2,1], alt=[1,1,1]).
LAM_TO_BLOCK = {(3,): "sym", (2, 1): "std", (1, 1, 1): "alt"}


def score_candidate(name: str, weights: dict, notes: str) -> dict:
    """weights: {lam: E_0^λ} per-block energy scale (substrate-derived).
    Prediction per particle: M = C · Σ_λ E_0^λ · m^λ(particle), where
    m^λ is the genuine per-block structural mass (orders-of-magnitude
    different across e⁻/p/n).  ONE global C is allowed (the overall MeV
    unit — NOT a per-block freedom).  We pin C from the proton, then test
    the electron AND neutron residuals.

    PASS       : ONE positive C makes ALL THREE (e⁻, p, n) land within 1%.
    LATENT-FIT : nucleons fit with one C but electron needs a different one
                 (i.e. the cross-scale ratio is wrong) — the map only works
                 within one Hecke order, so it hides a per-order parameter.
    FAIL       : negative C, or even within the nucleons one C fails."""
    sm = particle_struct_masses()

    def struct(particle):
        s = mpf(0)
        for lam in H3_BLOCKS:
            s += weights[lam] * sm[particle][LAM_TO_BLOCK[lam]]
        return s

    s_e = struct("electron")
    s_p = struct("proton")
    s_n = struct("neutron")
    res = {"candidate": name, "notes": notes,
           "weights": {str(k): fmt(v) for k, v in weights.items()},
           "struct_electron": fmt(s_e), "struct_proton": fmt(s_p),
           "struct_neutron": fmt(s_n)}

    # Pin the single global C from the proton anchor.
    if s_p == 0:
        res["verdict"] = "FAIL"
        res["reason"] = "degenerate (proton struct = 0)"
        return res
    C = ANCHORS_MEV["proton"] / s_p
    preds = {"electron": C * s_e, "proton": C * s_p, "neutron": C * s_n}
    resid = {k: float((preds[k] - ANCHORS_MEV[k]) / ANCHORS_MEV[k]) for k in preds}
    res.update({
        "C_global_pinned_from_proton": fmt(C),
        "C_positive": bool(C > 0),
        "pred_MeV": {k: fmt(v) for k, v in preds.items()},
        "resid_rel": resid,
    })
    worst = max(abs(resid["electron"]), abs(resid["neutron"]))  # proton is 0 by pin
    res["worst_resid_rel_excl_proton"] = worst
    if C <= 0:
        res["verdict"] = "FAIL"
        res["reason"] = "global scale C ≤ 0 (non-physical energy)"
    elif worst < 0.01:
        res["verdict"] = "PASS"
        res["reason"] = (f"one positive C fits e⁻,p,n within 1% "
                         f"(worst {worst:.2e})")
    elif abs(resid["neutron"]) < 0.01:
        res["verdict"] = "LATENT-FIT"
        res["reason"] = (f"nucleons fit (n resid {resid['neutron']:.2e}) but "
                         f"electron off by {resid['electron']:.2e} — needs a "
                         "per-Hecke-order scale (hidden parameter)")
    else:
        res["verdict"] = "FAIL"
        res["reason"] = (f"one C fails even on nucleons (n resid "
                         f"{resid['neutron']:.2e}, e resid {resid['electron']:.2e})")
    return res


def fmt(x, dps=20):
    if x is None:
        return None
    return mp.nstr(mpf(x), dps)


# ----------------------------------------------------------------------------
# The 5 candidate weight constructions.  Each returns {lam: w_λ} for H_3 blocks.
# ----------------------------------------------------------------------------
def candidate_1_archimedean() -> tuple[dict, str]:
    """Archimedean per-block: does m_e·VolDensity restricted to block λ give M_λ?

    FINDING (from _li_2_q_util.vol_density_borromean): VolDensity is a SINGLE
    knot-level SCALAR (Vol(𝓑₃)/ℏ_q² × linking_weight), m(K)=m_e·VolDensity.
    It has NO per-block decomposition — the only per-block object in that file
    is the EXPLORATORY spectral correction, which uses χ^(2,1) of ONE block.
    So 'VolDensity restricted to block λ' does not exist as a function of λ.

    The closest substrate per-block weight is the per-block character itself
    scaled by the knot-level VolDensity (i.e. w_λ = VolDensity · χ^λ), which is
    the most charitable reading of 'archimedean per-block'. We test that."""
    nuc = load_nucleon_blocks()
    g = vol_density_borromean(Q0, QI0)
    weights = {lam: g * nuc[lam]["chi"] for lam in H3_BLOCKS}
    return weights, ("VolDensity is a knot-level scalar (no per-block split); "
                     "tested w_λ = VolDensity·χ^λ as the charitable reading")


def candidate_2_qdim() -> tuple[dict, str]:
    """E_0^λ ∝ dim_q(λ) at q₀ (q-Weyl quantum dimension, hook-content formula)."""
    weights = {lam: qdim_lambda(lam) for lam in H3_BLOCKS}
    return weights, "w_λ = dim_q(λ) (q-hook-content) at q₀"


def candidate_2b_qdim_sq() -> tuple[dict, str]:
    weights = {lam: qdim_lambda(lam) ** 2 for lam in H3_BLOCKS}
    return weights, "variant: w_λ = dim_q(λ)²"


def candidate_3_rho_w_energy() -> tuple[dict, str]:
    """Option-E ρ_w at the ENERGY level.

    #1592 proved Σ_w ρ_w = χ^λ at the character level (the plain trace).
    The subtle question: does a per-vertex ENERGY functional of the seminormal
    diagonal eigenphases a_T (NOT the plain sum) carry info χ^λ discards?

    The seminormal diagonal entries a_T = h/(1 − q^{−2ρ_T}) (ρ_T axial
    distance per vertex) ARE the per-vertex data.  The plain trace Σ_T a_T
    (over the IDENTITY word) = χ^λ(1) = f^λ; over β it = χ^λ(β).  An 'energy'
    functional that is NOT the linear trace — e.g. Σ_T |a_T|² (an L² norm of
    the eigenphase spectrum) — is a genuinely DIFFERENT scalar.  We build
    w_λ = Σ_{T∈SYT(λ)} a_T² where a_T uses the axial content of vertex T.
    This is the honest per-vertex energy probe rho_w_crystal_vertex_trace
    deliberately did NOT compute (it summed the linear diagonal = χ^λ)."""
    weights = {}
    for lam in H3_BLOCKS:
        # enumerate SYT(λ) and sum the squared seminormal diagonal a_T over the
        # generators present in the canonical word.  For an energy functional
        # independent of the word we use the content spectrum of each vertex.
        syts = standard_young_tableaux(lam)
        energy = mpf(0)
        for T in syts:
            # per-vertex energy = Σ_i a_{T,i}² over adjacent transpositions s_i
            n = sum(lam)
            for i in range(1, n):
                ci, ci1 = T[i], T[i + 1]
                rho = (ci1[1] - ci1[0]) - (ci[1] - ci[0])
                if rho == 0:
                    continue
                a = H / (mpf(1) - Q0 ** (-2 * rho))
                energy += a * a
        weights[lam] = energy
    return weights, ("w_λ = Σ_{T∈SYT(λ)} Σ_i a_{T,i}²  (L² of seminormal "
                     "eigenphases — a NON-linear per-vertex energy functional, "
                     "distinct from the linear trace Σ_w ρ_w = χ^λ)")


def candidate_4_casimir() -> tuple[dict, str]:
    """E_0^λ from the quadratic Casimir = content-sum Σ_box c(box) on block λ."""
    weights = {lam: mpf(content_sum(lam)) for lam in H3_BLOCKS}
    return weights, "w_λ = Σ_box content(box) (quadratic Casimir eigenvalue)"


def candidate_4b_casimir_exp() -> tuple[dict, str]:
    """variant: E_0^λ ∝ exp/q-power of the content-sum (dimensionally a twist)."""
    weights = {lam: Q0 ** content_sum(lam) for lam in H3_BLOCKS}
    return weights, "variant: w_λ = q^{content-sum} (Casimir as a q-exponential)"


def candidate_5_ribbon() -> tuple[dict, str]:
    """E_0^λ from the ribbon eigenvalue θ_λ = q^{2·content-sum} (twist)."""
    weights = {lam: Q0 ** (2 * content_sum(lam)) for lam in H3_BLOCKS}
    return weights, "w_λ = θ_λ = q^{2·content-sum} (ribbon twist eigenvalue)"


# ---- SYT enumeration (for candidate 3) -------------------------------------
def standard_young_tableaux(lam):
    cs = cells(lam)
    n = len(cs)
    results = []

    def rec(k, placed):
        if k > n:
            inv = {v: cell for cell, v in placed.items()}
            results.append(inv)
            return
        for (r, c) in cs:
            if (r, c) in placed:
                continue
            if c > 0 and (r, c - 1) not in placed:
                continue
            if r > 0 and (r - 1, c) not in placed:
                continue
            placed[(r, c)] = k
            rec(k + 1, placed)
            del placed[(r, c)]

    rec(1, {})
    return results


CANDIDATES = [
    ("1_archimedean_per_block", candidate_1_archimedean),
    ("2_qdim", candidate_2_qdim),
    ("2b_qdim_sq", candidate_2b_qdim_sq),
    ("3_rho_w_energy_functional", candidate_3_rho_w_energy),
    ("4_casimir_content_sum", candidate_4_casimir),
    ("4b_casimir_q_exp", candidate_4b_casimir_exp),
    ("5_ribbon_twist", candidate_5_ribbon),
]


def main() -> int:
    t0 = time.time()
    print("=" * 90)
    print("E_0^λ TRY-ALL — 5 substrate-derived χ^λ→M_λ candidates")
    print(f"q₀ = {fmt(Q0)}  h = {fmt(H)}  m_e = {fmt(M_E_MEV)} MeV")
    print("=" * 90)

    nuc = load_nucleon_blocks()
    print("\nSubstrate per-block data (H_3 nucleon, from chi-neutron-h3 cache):")
    print(f"  {'λ':>10} {'dim':>4} {'χ^λ':>14} {'y_λ':>12} "
          f"{'content-sum':>11} {'dim_q':>14}")
    for lam in H3_BLOCKS:
        print(f"  {str(lam):>10} {nuc[lam]['dim']:>4} "
              f"{fmt(nuc[lam]['chi'], 10):>14} {fmt(nuc[lam]['y'], 8):>12} "
              f"{content_sum(lam):>11} {fmt(qdim_lambda(lam), 10):>14}")

    results = []
    for cname, fn in CANDIDATES:
        weights, notes = fn()
        r = score_candidate(cname, weights, notes)
        results.append(r)
        print(f"\n--- {cname} ---")
        print(f"  {notes}")
        print(f"  E_0^λ: " + ", ".join(f"{lam}={fmt(weights[lam], 6)}"
                                        for lam in H3_BLOCKS))
        if "resid_rel" in r:
            rr = r["resid_rel"]
            print(f"  C(pinned p)={r.get('C_global_pinned_from_proton')}  "
                  f"positive={r.get('C_positive')}")
            print(f"  resid: e⁻={rr['electron']:+.3e}  "
                  f"p={rr['proton']:+.1e}  n={rr['neutron']:+.3e}")
        print(f"  VERDICT: {r['verdict']} — {r.get('reason')}")

    witness = {
        "computation": "e0-lambda-tryall",
        "description": (
            "Falsification harness for 5 substrate-derived χ^λ→M_λ (per-block "
            "energy E_0^λ) maps. Each candidate produces a per-block weight w_λ "
            "from cached substrate data (q₀, χ^λ, y_λ, dim, content-sum, dim_q, "
            "ribbon twist, seminormal eigenphases) — NEVER from B_AME or the "
            "deprecated fit_three_E0. The per-block ENERGY scale E_0^λ maps the "
            "genuine per-block STRUCTURAL masses m^λ(particle) (from "
            "per_block_phi_q.mass_per_block — orders-of-magnitude different "
            "across e⁻ in H_2 vs p,n in H_3) onto observed MeV: "
            "M(particle) = C·Σ_λ E_0^λ·m^λ(particle). ONE global C is pinned "
            "from the proton; the electron AND neutron residuals are the test. "
            "PASS = one positive C fits all three within 1%; LATENT-FIT = "
            "nucleons fit but the electron (different Hecke order) needs a "
            "separate scale (hidden parameter); FAIL = one C fails even on "
            "nucleons or C ≤ 0. The {e⁻,p,n} observed masses are the "
            "falsification test, NOT fit targets. No tuning, no back-solve. If "
            "all fail, that is the reported result — no 6th fit (the Δ_λ gate "
            "already exhausted six ansätze)."
        ),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "q_0_50dps": fmt(Q0, 50),
        "h_50dps": fmt(H, 50),
        "m_e_MeV": fmt(M_E_MEV),
        "dps": mp.dps,
        "anchors_MeV": {k: fmt(v) for k, v in ANCHORS_MEV.items()},
        "anchor_pathology_note": (
            "The deprecated fit_three_E0 anchors are themselves pathological: "
            "3-obs {e,p,n} fit gives E_0^std = -7.09e-9 (negative energy) and "
            "is 575x ill-conditioned between the 3-obs and 5-obs fits. So "
            "'reproduce the fit scales' is the wrong bar; we score on a single "
            "positive global C instead."
        ),
        "substrate_blocks_H3": {
            str(lam): {
                "dim": nuc[lam]["dim"],
                "chi_lambda": fmt(nuc[lam]["chi"]),
                "y_lambda": fmt(nuc[lam]["y"]),
                "content_sum": content_sum(lam),
                "dim_q": fmt(qdim_lambda(lam)),
            } for lam in H3_BLOCKS
        },
        "candidates": results,
        "verdict_summary": {r["candidate"]: r["verdict"] for r in results},
        "any_pass": any(r["verdict"] == "PASS" for r in results),
        "compute_time_sec": round(time.time() - t0, 2),
        "design_note": "docs/audits/2026-06-01-e0-lambda-tryall-results.md",
    }
    out = HERE / "e0-lambda-tryall.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n{'=' * 90}")
    print("SUMMARY: " + "  ".join(f"{r['candidate']}={r['verdict']}"
                                   for r in results))
    print(f"any PASS: {witness['any_pass']}")
    print(f"witness -> {out}")
    print(f"done in {time.time() - t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
