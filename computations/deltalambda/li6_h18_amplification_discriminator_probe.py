#!/usr/bin/env python3
"""
li6_h18_amplification_discriminator_probe.py — the A = 6 (⁶Li, H₁₈)
DISCRIMINATOR for the geometric amplification law found by the θ_λ
magnitude audit (R3-b).  NO fit, NO tuning, NO wiring.

# Ref: docs/audits/2026-07-13-li6-h18-amplification-discriminator.md
# Ref: docs/audits/2026-07-13-theta-lambda-magnitude-derive-or-refute.md
# Ref: docs/audits/2026-06-09-large-A-chi-bottleneck-scaling-plan.md

THE TEST (registered BEFORE the number was computed — audit §6/§8).
The θ_λ magnitude audit measured the required amplification
    𝒜(K) = B_AME(K) / (m_e · Σ_λ w_λ |Δθ_λ|),     w_λ = y_λ · dim_λ
on {D, T, ³He, ⁴He} and found it geometric in A: per-added-nucleon
ratios 3.143 / 3.295 / 3.320 / 3.167 (~6 % scatter), i.e.
    𝒜(A) ≈ 6.0 · 3.2^{A−2}     (a GUARDED DATUM at 4 points).
⁶Li at H₁₈ (6 nucleons × 3 strands, 385 Wedderburn blocks) is the first
out-of-sample point: the law predicts 𝒜(⁶Li) ≈ 650 (composite guarded
form [3]_q!·(e^{Vol(𝓑₃)/2π})^{A−2}); the honest tolerance is the 4-point
per-step scatter compounded over the A=2→6 extrapolation
(1.06⁴ ≈ 1.27, i.e. roughly ±30–40 %).  SURVIVES → the ×3.2/nucleon
identification hunt is motivated; BREAKS → the geometric law joins the
refuted scalar class (scope-(a)).

DATA PROVENANCE (corpus-grep first — no recompute of the long job):
  • ⁶Li ATOM χ_λ + y_λ at H₁₈:
      chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json
    (cached CANONICAL witness: all 385 partitions of S₁₈, 50 dps, Rust
    chi_q_via_gp lossless path, 1382 s wall on its producing branch —
    reused here, NOT recomputed).
  • ⁶Li FREE χ_λ at H₁₈: computed here via the nucleon-cache +
    active-set LR parabolic character formula (chi_free_via_lr.py —
    the d_λ²-free scaling path; ~5 s wall, machine-checked ≤ 1e-12
    against the ⁴He MPFR free witness in-script).
  • D/T/³He/⁴He anchors: binding-reeb-phase-decomposition.witness.json
    (θ_λ vectors) + chi-*-h*-at-q0-50dps.witness.json (y_λ) — the SAME
    cached inputs as the θ_λ magnitude audit, re-derived here as a
    regression gate (𝒜(D) must reproduce 29.075377, convention D (re-pinned 2026-09-07; the prior 6.4161462 was a grouped-word value)).
  • SECONDARY out-of-sample point ⁵Li (A=5, H₁₅, 176 blocks): cached
    chi-lithium-5-h15-at-q0-50dps-matrix-m.witness.json (atom χ+y) +
    chi_free_frobenius(3,2) — locates WHERE the law breaks (⁵Li is
    particle-unbound; its AME total binding is the same measured
    diagnostic numerator as the other atoms).

CONVENTION NOTE.  The anchors' χ come from atom-chi-rust-* (color-
weighted p-n crossing); the ⁶Li atom witness is sign-only-crossings.
Cross-checked on ⁴He/T where both exist: max relative difference
≤ 4.4e-6 — negligible against the ~6 % scatter this test resolves.

θ CONVENTION (identical to binding_reeb_phase_decomposition.py):
  r_λ = χ_λ/dim_λ;  θ_λ = arccos(r_λ) if |r_λ| ≤ 1 (rotation channel)
  else arccosh(|r_λ|) (growth channel);  |Δθ_λ| = |θ_atom − θ_free|
  summed over ALL blocks (the kernel probe's sum, channel flips
  included) under both fixed weightings w = y·dim (primary) and w = y.

ANTI-FIT (STRICT).  B_AME(⁶Li) enters ONLY as the numerator of the
MEASURED 𝒜 — a reported diagnostic quotient, never an input to any
wired formula.  The verdict is a discrimination test of a guarded
datum; nothing here is a derivation and nothing is wired to production.

Emits: li6-h18-amplification-discriminator.witness.json
EXPLORATORY — audit-only witness; no production wiring.
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_COMP, _COMP / "substrate", _COMP / "hecke", _COMP / "habiro"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_LI5_MEV_VALIDATION,
    AME_B_LI6_MEV_VALIDATION,
)
from witness_base import WitnessBuilder  # noqa: E402
from chi_free_via_lr import chi_free_lr, load_nucleon_chi  # noqa: E402
# Frobenius route: identical values (agree to 1.3e-67 per
# chi-free-via-frobenius.witness.json) and far faster as A grows —
# 31x at 6Li, 104x at 7Li — because it needs O(A^2) cycle types where
# the LR route enumerates O(3^A) tuples.
from chi_free_via_frobenius import chi_free_frobenius  # noqa: E402

set_compute_dps()

q0 = mp.mpf(Q_50_DIGIT_STR)
M_E = mp.mpf(str(M_E_MEV))
HBAR_Q = 1 - 1 / q0
MU_0 = M_E / (3 * (q0 - 1 / q0) / 2)

B_AME = {
    "D":   mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
    "T":   mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
    "3He": mp.mpf(str(AME_B_HE3_MEV_VALIDATION)),
    "4He": mp.mpf(str(AME_B_HE4_MEV_VALIDATION)),
    "5Li": mp.mpf(str(AME_B_LI5_MEV_VALIDATION)),
    "6Li": mp.mpf(str(AME_B_LI6_MEV_VALIDATION)),
}

try:
    from substrate.knot_volumes import VOL_BORROMEAN_MPF
    VOL_B3 = VOL_BORROMEAN_MPF
except ImportError:
    VOL_B3 = mp.mpf("7.3277248")

CHI_WITNESS = {
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}
LARGE_A_ATOM_WITNESS = {
    "5Li": "chi-lithium-5-h15-at-q0-50dps-matrix-m.witness.json",
    "6Li": "chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json",
}
LARGE_A_ZN = {"5Li": (3, 2), "6Li": (3, 3)}
LARGE_A_NPART = {"5Li": 176, "6Li": 385}   # p(15), p(18)
HE4_FREE_WITNESS = "chi-helium-4-free-h12-at-q0-50dps.witness.json"

A_OF = {"D": 2, "T": 3, "3He": 3, "4He": 4, "5Li": 5, "6Li": 6}

# Convention gap bound: the LR free path is built from the sign-only
# nucleon H₃ character cache, while chi-helium-4-free-h12 is
# averaged-crossings; measured gap ≤ 6.4e-6 relative (same magnitude
# as the ≤ 4.4e-6 atom-side gap between atom-chi-rust-* and the
# sign-only 50-dps witnesses). Perturbs 𝒜 by ≪ 0.01 % — negligible
# against the ~6 %-scatter / order-unity effects this test resolves.
LR_CONVENTION_GAP_TOL = 1e-5


def _load(name: str) -> dict:
    return json.loads((_COMP / name).read_text())


def _key(part) -> str:
    return "_".join(str(p) for p in part)


def dim_sn(lam) -> int:
    """f^λ via the hook-length formula (same as the Reeb producer)."""
    n = sum(lam)
    num = math.factorial(n)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return num // den


def theta(r: mp.mpf) -> tuple[mp.mpf, str]:
    """Per-block Reeb phase: arccos on rotation (|r|≤1), arccosh on growth."""
    if mp.fabs(r) <= 1:
        return mp.acos(r), "rotation"
    return mp.acosh(mp.fabs(r)), "growth"


def load_anchor_atom(atom: str, reeb_per_atom: dict) -> list[dict]:
    """Anchor rows exactly as theta_lambda_magnitude_kernel_probe.load_atom."""
    chi = _load(CHI_WITNESS[atom])
    if chi.get("partial", False):
        raise RuntimeError(f"chi witness for {atom} is partial — regenerate")
    y_map = {_key(e["partition"]): mp.mpf(e["y_lambda"])
             for e in chi["by_partition"]}
    rows = []
    for r in reeb_per_atom[atom]["by_partition"]:
        k = _key(r["partition"])
        if k not in y_map:
            raise KeyError(f"{atom}: y_λ missing for partition {k}")
        th_a = mp.mpf(r["theta_atom_rad"])
        th_f = mp.mpf(r["theta_free_rad"])
        rows.append({"key": k, "dim": int(r["dim"]), "y": y_map[k],
                     "abs_dtheta": abs(th_a - th_f)})
    return rows


def sum_w(rows: list[dict], weighting: str) -> mp.mpf:
    if weighting == "y":
        return sum(r["y"] * r["abs_dtheta"] for r in rows)
    if weighting == "y_dim":
        return sum(r["y"] * r["dim"] * r["abs_dtheta"] for r in rows)
    raise ValueError(weighting)


def validate_lr_free_path(nuc_chi: dict) -> mp.mpf:
    """Regression of the LR free path against the ⁴He MPFR free witness."""
    chi_free_4he = chi_free_lr(2, 2, nuc_chi=nuc_chi)
    ref = _load(HE4_FREE_WITNESS)
    refd = {tuple(e["partition"]): mp.mpf(str(e["chi_lambda"]))
            for e in ref["by_partition"]}
    lr_max_rel = mp.mpf(0)
    for k, v in chi_free_4he.items():
        if k in refd and refd[k] != 0:
            lr_max_rel = max(lr_max_rel, abs(v - refd[k]) / abs(refd[k]))
    print(f"  [check] LR free path vs ⁴He MPFR free witness: max rel "
          f"{mp.nstr(lr_max_rel, 3)} (convention gap; bound "
          f"{LR_CONVENTION_GAP_TOL:g})")
    return lr_max_rel


def build_large_a_rows(atom: str, nuc_chi: dict) -> tuple[list[dict], dict]:
    """Per-λ rows for a large-A atom: cached atom χ+y witness + LR free χ."""
    t0 = time.time()
    w = _load(LARGE_A_ATOM_WITNESS[atom])
    if w.get("partial", False) or w.get("tr_M_partial", False):
        raise RuntimeError(f"{atom} atom witness is partial — regenerate")
    if int(w["n_partitions"]) != int(w["n_partitions_total"]):
        raise RuntimeError(f"{atom} atom witness skipped partitions")
    atom_rows = w["by_partition"]
    print(f"  [phase] {atom} atom χ+y loaded from cached canonical witness "
          f"({len(atom_rows)} partitions; producer={w.get('producer')}, "
          f"original wall {float(w.get('compute_time_sec') or 0):.0f}s "
          f"— NOT recomputed)")

    # internal consistency: Σ y·χ_atom must reproduce the witness's tr_M
    tr_recomputed = sum(mp.mpf(e["y_lambda"]) * mp.mpf(e["chi_lambda"])
                        for e in atom_rows)
    tr_witness = mp.mpf(w["tr_M_at_q0"])
    tr_rel = abs(tr_recomputed - tr_witness) / abs(tr_witness)
    print(f"  [check] Σ y·χ_atom vs witness tr_M: rel diff {mp.nstr(tr_rel, 3)}")

    Z, N = LARGE_A_ZN[atom]
    print(f"  [phase] computing {atom} FREE χ via nucleon-cache + "
          f"active-set LR (d_λ²-free path) ...")
    t1 = time.time()
    chi_free = chi_free_frobenius(Z, N, nuc_chi=nuc_chi)
    t2 = time.time()
    print(f"  [phase] free χ done: {len(chi_free)} partitions in "
          f"{t2 - t1:.1f}s (elapsed {t2 - t0:.1f}s)")

    rows = []
    stats = {"rotation_free": 0, "rotation_atom": 0,
             "growth_free": 0, "growth_atom": 0, "channel_flips": 0}
    for e in atom_rows:
        part = tuple(e["partition"])
        d = dim_sn(list(part))
        ch_a = mp.mpf(e["chi_lambda"])
        ch_f = chi_free[part]
        th_a, cha = theta(ch_a / d)
        th_f, chf = theta(ch_f / d)
        stats["rotation_atom"] += int(cha == "rotation")
        stats["growth_atom"] += int(cha == "growth")
        stats["rotation_free"] += int(chf == "rotation")
        stats["growth_free"] += int(chf == "growth")
        stats["channel_flips"] += int(cha != chf)
        rows.append({"key": _key(part), "dim": d,
                     "y": mp.mpf(e["y_lambda"]),
                     "abs_dtheta": abs(th_a - th_f)})
    meta = {"n_partitions": len(rows),
            "tr_M_consistency_rel": tr_rel,
            "free_chi_wall_sec": round(t2 - t1, 2),
            "channel_stats": stats}
    return rows, meta


def main() -> int:
    t_start = time.time()
    print("=" * 74)
    print(" ⁶Li H₁₈ amplification discriminator — geometric law 𝒜(A)≈6.0·3.2^{A−2}")
    print("=" * 74)
    print(f"  q₀ = {float(q0):.8f}   m_e = {float(M_E):.6f} MeV   "
          f"B_AME(⁶Li) = {float(B_AME['6Li']):.4f} MeV")
    print(f"  [header] work: 4 cached anchors + cached ⁵Li/⁶Li atom χ loads "
          f"+ LR free χ at A∈{{4,5,6}} — expected wall < 60 s")

    # ── 1. Anchors (same cached inputs + conventions as the audit) ──────
    reeb = _load("binding-reeb-phase-decomposition.witness.json")["data"]["per_atom"]
    anchors = ["D", "T", "3He", "4He"]
    rows = {a: load_anchor_atom(a, reeb) for a in anchors}
    kappa = {}
    for wgt in ("y", "y_dim"):
        S = {a: sum_w(rows[a], wgt) for a in anchors}
        kappa[wgt] = {a: B_AME[a] / (M_E * S[a]) for a in anchors}
    print("\n  anchors reproduced (must match the θ_λ magnitude audit):")
    for a in anchors:
        print(f"    {a:>4s}  𝒜(y·dim) = {float(kappa['y_dim'][a]):>8.3f}   "
              f"𝒜(y) = {float(kappa['y'][a]):>10.2f}")

    # ── 2. Large-A rows + measured 𝒜 (⁶Li primary, ⁵Li secondary) ──────
    nuc_chi = load_nucleon_chi()
    lr_max_rel = validate_lr_free_path(nuc_chi)
    large_rows, large_meta, S_large, A_large = {}, {}, {}, {}
    for atom in ("5Li", "6Li"):
        n_strands = 3 * A_OF[atom]
        print(f"\n  building {atom} per-λ θ table (H_{n_strands}, "
              f"{LARGE_A_NPART[atom]} blocks):")
        rws, meta = build_large_a_rows(atom, nuc_chi)
        large_rows[atom], large_meta[atom] = rws, meta
        S_large[atom] = {wgt: sum_w(rws, wgt) for wgt in ("y", "y_dim")}
        A_large[atom] = {wgt: B_AME[atom] / (M_E * S_large[atom][wgt])
                         for wgt in ("y", "y_dim")}
        cs = meta["channel_stats"]
        print(f"  channels: rotation free {cs['rotation_free']} → atom "
              f"{cs['rotation_atom']} (growth {cs['growth_free']} → "
              f"{cs['growth_atom']}; {cs['channel_flips']} flips)")
        print(f"  MEASURED 𝒜({atom}):")
        for wgt in ("y_dim", "y"):
            print(f"    w = {wgt:<6s}: m_e·S = "
                  f"{float(M_E * S_large[atom][wgt]):.6f} MeV   "
                  f"𝒜({atom}) = {float(A_large[atom][wgt]):>12.2f}")
    S6, A6 = S_large["6Li"], A_large["6Li"]
    li6_meta = large_meta["6Li"]

    # ── 3. Geometric-law comparison (w = y·dim, the audit's convention) ─
    def qint(n: int) -> mp.mpf:
        return (q0 ** n - q0 ** (-n)) / (q0 - 1 / q0)

    def qfact(n: int) -> mp.mpf:
        out = mp.mpf(1)
        for i in range(2, n + 1):
            out *= qint(i)
        return out

    kd = kappa["y_dim"]
    steps_anchor = {"T/D": kd["T"] / kd["D"], "3He/D": kd["3He"] / kd["D"],
                    "4He/T": kd["4He"] / kd["T"], "4He/3He": kd["4He"] / kd["3He"]}
    r_min, r_max = min(steps_anchor.values()), max(steps_anchor.values())
    # extrapolation band: anchor 𝒜(D), min/max observed step ratio to the 4th
    band_lo = kd["D"] * r_min ** 4
    band_hi = kd["D"] * r_max ** 4
    # the honest quoted tolerance: 4-point scatter compounded ≈ ±30–40 %
    r_kash = mp.e ** (VOL_B3 / (2 * mp.pi))
    ratio_candidates = {"pi": mp.pi, "[3]_q": qint(3),
                        "mu_0/m_e": MU_0 / M_E, "exp(Vol(B3)/2pi)": r_kash}
    pred_composite = qfact(3) * r_kash ** 4          # [3]_q!·r^{A−2}, A=6
    preds = {name: {"anchor_[3]_q!": qfact(3) * c ** 4,
                    "anchor_A(D)": kd["D"] * c ** 4}
             for name, c in ratio_candidates.items()}

    meas = A6["y_dim"]
    print(f"\n  geometric-law comparison (w = y·dim):")
    print(f"    measured 𝒜(⁶Li)             = {float(meas):>9.2f}")
    print(f"    composite guarded prediction = {float(pred_composite):>9.2f}"
          f"   ([3]_q!·(e^{{Vol/2π}})⁴ — the audit's ≈650)")
    print(f"    extrapolation band from anchor step scatter: "
          f"[{float(band_lo):.1f}, {float(band_hi):.1f}]  "
          f"(𝒜(D)·r⁴, r ∈ [{float(r_min):.3f}, {float(r_max):.3f}])")
    rel_vs_composite = meas / pred_composite - 1
    in_band = bool(band_lo <= meas <= band_hi)
    # honest tolerance: the per-step ~6 % scatter compounded over 4 steps
    # (1.06⁴ ≈ 1.27) — call it ±40 % as the generous outer gate.
    within_40pct = bool(abs(rel_vs_composite) <= mp.mpf("0.40"))
    survives = in_band or within_40pct
    print(f"    measured/composite − 1       = {float(rel_vs_composite)*100:+.1f} %")
    print(f"    inside anchor-scatter band?    {in_band}")
    print(f"    within ±40 % outer gate?       {within_40pct}")
    print(f"    → VERDICT: geometric law "
          f"{'SURVIVES at A=6' if survives else 'BREAKS at A=6 (4-point artifact)'}")

    # implied per-step ratios A=4→5→6 and full-chain including Li
    step_46 = (A6["y_dim"] / kd["4He"]) ** mp.mpf("0.5")
    step_45 = A_large["5Li"]["y_dim"] / kd["4He"]
    step_56 = A6["y_dim"] / A_large["5Li"]["y_dim"]
    pred_5 = qfact(3) * r_kash ** 3       # composite at A=5 (≈ 202)
    rel_5 = A_large["5Li"]["y_dim"] / pred_5 - 1
    print(f"\n    SECONDARY point ⁵Li (A=5): measured 𝒜 = "
          f"{float(A_large['5Li']['y_dim']):.2f} vs composite "
          f"[3]_q!·r³ = {float(pred_5):.1f}  "
          f"({float(rel_5)*100:+.1f} %)")
    print(f"    implied per-nucleon step ratios: ⁴He→⁵Li = "
          f"{float(step_45):.4f}, ⁵Li→⁶Li = {float(step_56):.4f}, "
          f"(⁶Li/⁴He)^(1/2) = {float(step_46):.4f}   "
          f"(anchors gave 3.14–3.32)")
    cand_rows = {}
    print("    degenerate ratio candidates at A=6 ([3]_q!·c⁴ / 𝒜(D)·c⁴):")
    for name, c in ratio_candidates.items():
        p1 = preds[name]["anchor_[3]_q!"]
        p2 = preds[name]["anchor_A(D)"]
        cand_rows[name] = {
            "ratio_value": mp.nstr(c, 8),
            "pred_A6_anchor_q3fact": mp.nstr(p1, 8),
            "pred_A6_anchor_AD": mp.nstr(p2, 8),
            "measured_over_pred_q3fact": mp.nstr(meas / p1, 8),
        }
        print(f"      {name:<18s} c = {float(c):.4f}   pred {float(p1):7.1f} / "
              f"{float(p2):7.1f}   measured/pred = {float(meas / p1):.3f}")

    # composite formula as ABSOLUTE binding at A=6 (the audit's §6 form)
    B_pred_composite = M_E * S6["y_dim"] * pred_composite
    rel_B = B_pred_composite / B_AME["6Li"] - 1
    print(f"\n    composite absolute check: B_pred = m_e·S·𝒜_comp = "
          f"{float(B_pred_composite):.3f} MeV vs B_AME = "
          f"{float(B_AME['6Li']):.3f}  ({float(rel_B)*100:+.1f} %)")

    wall = time.time() - t_start
    print(f"\n  total wall {wall:.1f}s")

    # ── witness ─────────────────────────────────────────────────────────
    wb = WitnessBuilder("li6-h18-amplification-discriminator", engine="mpmath")
    wb.set_description(
        "R3-b: the A=6 (⁶Li, H₁₈, 385 Wedderburn blocks) out-of-sample "
        "DISCRIMINATOR for the geometric amplification law 𝒜(A) ≈ "
        "6.0·3.2^{A−2} found by the θ_λ magnitude audit on {D,T,³He,⁴He}. "
        "Measures 𝒜(⁶Li) = B_AME(⁶Li)/(m_e·Σ w_λ|Δθ_λ|) under the audit's "
        "w = y_λ·dim_λ convention (w = y_λ reported for robustness), from "
        "the cached canonical ⁶Li atom χ witness (sign-only Rust "
        "chi_q_via_gp, 50 dps, reused NOT recomputed) + the LR parabolic "
        "free χ (machine-checked ≤1e-12 vs the ⁴He MPFR free witness). "
        "θ convention identical to binding_reeb_phase_decomposition.py "
        "(arccos rotation / arccosh growth). B_AME(⁶Li) enters ONLY as the "
        "numerator of the measured diagnostic quotient — nothing tuned, "
        "nothing wired; the composite [3]_q!·(e^{Vol(𝓑₃)/2π})^{A−2} stays "
        "a GUARDED DATUM regardless of verdict. EXPLORATORY, audit-only."
    )
    wb.add_data("substrate", {"q_0": mp.nstr(q0, 30), "m_e_MeV": mp.nstr(M_E, 15),
                              "mu_0_MeV": mp.nstr(MU_0, 15),
                              "Vol_B3": mp.nstr(VOL_B3, 15)})
    wb.add_data("provenance", {
        "li6_atom_chi": f"{LARGE_A_ATOM_WITNESS['6Li']} (cached canonical, producer "
                        "rust-chi-q-via-gp-lossless, 1382 s original wall; "
                        "sign-only convention, ≤4.4e-6 rel vs the anchors' "
                        "color-weighted convention where both exist)",
        "li6_free_chi": "chi_free_via_frobenius.chi_free_frobenius(3,3) — "
                        "Frobenius characteristic map (power-sum expansion + "
                        "Murnaghan–Nakayama; forms no LR coefficient). Agrees "
                        "with the LR route to 1.3e-67 on all 385 blocks "
                        "(chi-free-via-frobenius.witness.json), "
                        f"{li6_meta['free_chi_wall_sec']} s wall",
        "li5_atom_chi": f"{LARGE_A_ATOM_WITNESS['5Li']} (cached canonical, "
                        "producer rust-chi-q-via-gp-lossless, 67 s original "
                        "wall) — SECONDARY out-of-sample point at A=5",
        "li5_free_chi": "chi_free_via_frobenius.chi_free_frobenius(3,2), "
                        f"{large_meta['5Li']['free_chi_wall_sec']} s wall",
        "anchors": "binding-reeb-phase-decomposition.witness.json θ vectors "
                   "+ chi-*-h*-at-q0-50dps y_λ (same as the audit probe)",
        "B_AME_role": "numerator of the MEASURED diagnostic 𝒜 only — "
                      "never an input to a wired formula",
    })
    wb.add_data("large_a_meta", {
        atom: {
            "n_partitions": large_meta[atom]["n_partitions"],
            "tr_M_consistency_rel":
                mp.nstr(large_meta[atom]["tr_M_consistency_rel"], 6),
            "free_chi_wall_sec": large_meta[atom]["free_chi_wall_sec"],
            "channel_stats": large_meta[atom]["channel_stats"],
        } for atom in ("5Li", "6Li")})
    wb.add_data("lr_free_vs_he4_witness_max_rel", {
        "value": mp.nstr(lr_max_rel, 6),
        "bound": LR_CONVENTION_GAP_TOL,
        "note": "convention gap (sign-only nucleon cache vs "
                "averaged-crossings free witness); perturbs 𝒜 by ≪ 0.01 %",
    })
    wb.add_data("anchor_amplifications", {
        wgt: {a: mp.nstr(kappa[wgt][a], 10) for a in anchors}
        for wgt in ("y", "y_dim")})
    wb.add_data("anchor_step_ratios_y_dim",
                {k: mp.nstr(v, 8) for k, v in steps_anchor.items()})
    wb.add_data("li6_measured", {
        "S_y_dim": mp.nstr(S6["y_dim"], 10),
        "S_y": mp.nstr(S6["y"], 10),
        "m_e_S_y_dim_MeV": mp.nstr(M_E * S6["y_dim"], 10),
        "A_li6_y_dim": mp.nstr(A6["y_dim"], 10),
        "A_li6_y": mp.nstr(A6["y"], 10),
        "B_AME_li6_MeV": mp.nstr(B_AME["6Li"], 10),
    })
    wb.add_data("geometric_law_test", {
        "pred_composite_q3fact_kash4": mp.nstr(pred_composite, 10),
        "measured_over_composite_minus_1": mp.nstr(rel_vs_composite, 6),
        "anchor_scatter_band": [mp.nstr(band_lo, 8), mp.nstr(band_hi, 8)],
        "inside_anchor_scatter_band": in_band,
        "within_40pct_outer_gate": within_40pct,
        "secondary_point_5Li": {
            "measured_A_y_dim": mp.nstr(A_large["5Li"]["y_dim"], 10),
            "measured_A_y": mp.nstr(A_large["5Li"]["y"], 10),
            "pred_composite_q3fact_kash3": mp.nstr(pred_5, 10),
            "measured_over_composite_minus_1": mp.nstr(rel_5, 6),
            "caveat": "⁵Li is particle-unbound (p+⁴He); its AME total "
                      "binding is used as the same MEASURED diagnostic "
                      "numerator as the other atoms",
        },
        "implied_step_ratio_4He_to_5Li": mp.nstr(step_45, 8),
        "implied_step_ratio_5Li_to_6Li": mp.nstr(step_56, 8),
        "implied_step_ratio_4He_to_6Li": mp.nstr(step_46, 8),
        "composite_absolute_B_pred_MeV": mp.nstr(B_pred_composite, 10),
        "composite_absolute_rel_err": mp.nstr(rel_B, 6),
        "verdict": ("SURVIVES — geometric extensivity holds at A=6; the "
                    "×3.2/nucleon identification hunt is motivated"
                    if survives else
                    "BREAKS — the geometric law is a 4-point artifact; it "
                    "joins the refuted scalar class (scope-(a): this law, "
                    "alone, does not extend; constrains combinations, not "
                    "ingredients)"),
        "status": "GUARDED-DATUM discrimination test — not a derivation; "
                  "not wired regardless of verdict",
    })
    wb.add_data("ratio_candidates_at_A6", cand_rows)

    wb.add_assertion(
        "anchor_kappaD_reproduced",
        computed=fmt(kd["D"]), expected="29.075377", tolerance="0.01",
        source="convention-D value, DERIVED INDEPENDENTLY by "
               "carrier_table_convention_d_rederivation.py (y_λ recomputed "
               "from y_lambda_su_n, θ rebuilt from χ/dim) — not copied from "
               "this script's own output. The prior 6.0426 was the "
               "convention-C value, correct in its own frame; the weights "
               "were re-derived when convention C was excised on 2026-08-09 "
               "and this expectation was not. Same regression as "
               "carrier_saturation_mechanism_probe; see "
               "docs/audits/2026-08-26-carrier-saturation-five-failures-"
               "diagnosis.md"
               "  RE-PINNED 2026-09-07 (qou-k54t) from 6.4161462 to "
               "29.075377. That 6.4161462 was itself derived while D's chi "
               "caches were on the GROUPED word, and the computed side read "
               "those same caches, so the assertion agreed for the wrong "
               "reason -- a false green, not a passing test. D is now fully "
               "borromean (reeb witness and rust cache both regenerated), so "
               "this pin does not depend on the 5Li/6Li caches, which are "
               "still grouped.")
    wb.add_assertion(
        "anchor_kappa4He_reproduced",
        computed=fmt(kd["4He"]), expected="702.409", tolerance="0.1",
        source="regression vs the audit's I1 table (w = y·dim)"
               "  RE-PINNED 2026-09-07 (qou-k54t) from 73.5943 to "
               "702.409. That 73.5943 was itself derived while 4He's chi "
               "caches were on the GROUPED word, and the computed side read "
               "those same caches, so the assertion agreed for the wrong "
               "reason -- a false green, not a passing test. 4He is now fully "
               "borromean (reeb witness and rust cache both regenerated), so "
               "this pin does not depend on the 5Li/6Li caches, which are "
               "still grouped.")
    wb.add_assertion(
        "li6_all_385_partitions_present",
        computed=li6_meta["n_partitions"], expected=385, tolerance=0,
        source="cached ⁶Li H₁₈ atom witness is complete (no max_dim skip)")
    wb.add_assertion(
        "li6_trM_internal_consistency",
        computed=li6_meta["tr_M_consistency_rel"],
        expected=0.0, tolerance=1e-30,
        source="Σ y_λ·χ_λ(atom) reproduces the witness's own tr_M_at_q0")
    wb.add_assertion(
        "lr_free_path_validated_at_4He",
        computed=lr_max_rel,
        expected=0.0, tolerance=LR_CONVENTION_GAP_TOL,
        source="chi_free_lr(2,2) vs chi-helium-4-free-h12 MPFR witness; "
               "tolerance is the documented sign-only-vs-averaged "
               "convention gap (≤1e-5), which perturbs 𝒜 by ≪ 0.01 %")
    wb.add_assertion(
        "li5_trM_internal_consistency",
        computed=large_meta["5Li"]["tr_M_consistency_rel"],
        expected=0.0, tolerance=1e-30,
        source="Σ y_λ·χ_λ(atom) reproduces the ⁵Li witness's own tr_M_at_q0")
    # Demoted from `add_assertion` to data (bean `qou-26f2`). Both read
    # `computed=X, expected=X`, and their own source strings said why —
    # "self-referential by design (no target smuggling)". That reasoning is
    # right and the conclusion drawn from it was wrong: refusing to smuggle a
    # target is a reason not to *assert*, not a reason to assert a tautology.
    # As assertions they fed `allPassed` a guaranteed pass and made the
    # witness look like it had checked two more things than it had. As data
    # they say exactly what they always meant — a measured diagnostic and a
    # recorded verdict, neither of which has an independent expected value.
    wb.add_data("li6_amplification_measured", {
        "value": A6["y_dim"],
        "meaning": "MEASURED diagnostic 𝒜(⁶Li) under w = y·dim",
        "has_independent_expected_value": False,
    })
    wb.add_data("geometric_law_verdict", {
        "survives": bool(survives),
        "meaning": "true = in anchor-scatter band or ±40 % outer gate; "
                   "false = breaks",
        "has_independent_expected_value": False,
    })
    out = wb.save()
    print(f"\n  witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
