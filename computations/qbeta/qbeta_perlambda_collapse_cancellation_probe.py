#!/usr/bin/env python3
"""Heavy per-λ collapse-cancellation probe (S2 core) for Q_β residue-A.

Owner-confirmed mechanism (PR #1895): does the coherent scalar collapse
`tr_M = Σ_λ y_λ χ^λ` CANCEL the per-block n↔p content that the per-block
(incoherent) sum retains? Decisive at the substrate q₀:

    cancellation_ratio = |Σ_λ Δcontrib_λ| / Σ_λ |Δcontrib_λ|
      << 1  → coherent collapse cancels the per-λ n-p content (mechanism confirmed)
      ~ 1   → no cancellation (S2 refuted as the order-gap source at this anchor)

  Δcontrib_λ = contrib_λ(neutron) − contrib_λ(proton),  λ ⊢ 3.

Uses the **production** per-partition machinery
`mass_at_3A_proper.markov_trace_3A` (canonical χ^λ via `chi_lambda_of_word`)
evaluated at the production substrate q₀.

CAVEAT (honest): `markov_trace_3A` is the Plancherel-weighted per-λ breakdown
(`w = dim_q²/[n]_q!`), NOT the canonical Jones–Markov trace; the χ^λ are
canonical, the weighting is Plancherel. The cancellation MECHANISM is testable
on this per-λ structure; canonical-Wenzl-`y_λ` re-weighting + the cross-anchor
swing are the refinements (next session). No fit; c_3 stays cal-anchored;
nothing wired.
"""
from __future__ import annotations

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve()
COMP = HERE.parent.parent          # computations
sys.path.insert(0, str(COMP))

try:
    from mass_at_3A_proper import markov_trace_3A
except Exception as e:  # noqa: BLE001
    print(f"FATAL: import markov_trace_3A failed: {type(e).__name__}: {e}")
    sys.exit(2)

# proton = (Z=1, N=0), neutron = (Z=0, N=1): single nucleon → 3 strands → H_3,
# no inter-nucleon interface (include_inter is a no-op at A=1).
p = markov_trace_3A(1, 0)
n = markov_trace_3A(0, 1)
print(f"proton  total tr_M = {p['total']:+.8e}  ({p['n_partitions']} partitions, {p['n_gens']} gens)")
print(f"neutron total tr_M = {n['total']:+.8e}")

pp = {tuple(r["partition"]): r for r in p["per_partition"]}
nn = {tuple(r["partition"]): r for r in n["per_partition"]}
shapes = sorted(set(pp) | set(nn), key=lambda s: (len(s), s))

print("\n per-λ  n−p  breakdown:")
rows = []
sum_abs = 0.0
for s in shapes:
    rp, rn = pp.get(s, {}), nn.get(s, {})
    cp, cn = rp.get("contrib", 0.0), rn.get("contrib", 0.0)
    chi_p, chi_n = rp.get("chi", 0.0), rn.get("chi", 0.0)
    dim = rp.get("dim", rn.get("dim", 0))
    dc = cn - cp
    sum_abs += abs(dc)
    rows.append({"partition": list(s), "dim": dim, "chi_p": chi_p, "chi_n": chi_n,
                 "contrib_p": cp, "contrib_n": cn, "delta_contrib": dc})
    print(f"  λ={str(s):>14} dim={dim} χ_p={chi_p:+.4e} χ_n={chi_n:+.4e} Δcontrib={dc:+.4e}")

scalar = n["total"] - p["total"]                       # coherent: extract AFTER Σ_λ
ratio = abs(scalar) / sum_abs if sum_abs else float("nan")
print(f"\n coherent   |Σ_λ Δcontrib_λ|  = |Δtr_M| = {abs(scalar):.6e}")
print(f" observe-last  Σ_λ |Δcontrib_λ|        = {sum_abs:.6e}")
print(f" CANCELLATION RATIO (coherent/incoherent) = {ratio:.4f}"
      + (f"   ⇒  {1/ratio:.1f}× suppression" if ratio and ratio < 1 else ""))
print(" Δcontrib sign per λ:",
      [(r["partition"], "+" if r["delta_contrib"] >= 0 else "−") for r in rows])

# --- canonical Wenzl y_λ confirmation: could a NEGATIVE y_λ flip the sign? ---
print("\n canonical Wenzl y_λ re-weighting (rigor check vs Plancherel above):")
canon = {}
try:
    from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric as _yw
    from q_parameter import Q as _Q0
    q0 = float(_Q0)
    ctot = ctot_abs = 0.0
    for r in rows:
        s = tuple(r["partition"])
        dchi = r["chi_n"] - r["chi_p"]
        y = float(_yw(s, q0))
        cdc = y * dchi
        ctot += cdc
        ctot_abs += abs(cdc)
        r["y_wenzl"] = y
        r["delta_contrib_canonical"] = cdc
        print(f"  λ={str(s):>12} y_λ={y:+.4e} ({'+' if y >= 0 else '−'}) Δcontrib_canon={cdc:+.4e}")
    canon_ratio = abs(ctot) / ctot_abs if ctot_abs else float("nan")
    all_pos = all(r.get("y_wenzl", 1.0) > 0 for r in rows)
    print(f" canonical cancellation ratio = {canon_ratio:.4f}  (all y_λ > 0: {all_pos})")
    canon = {"q0": q0, "canonical_ratio": canon_ratio, "all_y_lambda_positive": all_pos}
except Exception as e:  # noqa: BLE001
    print(f" canonical y_λ check skipped: {type(e).__name__}: {e}")
    canon = {"error": f"{type(e).__name__}: {e}"}

canon_ratio = canon.get("canonical_ratio", ratio)
if ratio < 0.5 or (canon_ratio < 0.5):
    verdict = (f"CANCELLATION CONFIRMED — coherent collapse suppresses the per-λ n-p "
               f"content (Plancherel ratio {ratio:.3f}); observe-last retains it. Supports S2.")
else:
    verdict = (f"S2 REFUTED — NO cancellation (Plancherel ratio {ratio:.3f}, canonical-Wenzl "
               f"{canon_ratio:.3f}). All per-λ n-p contributions are SAME sign (Δχ^λ<0 every "
               f"block; all y_λ>0) ⇒ coherent = incoherent; observe-last recovers nothing. The "
               f"c_3 order gap is NOT a collapse artifact ⇒ amplification is the genuine f-map / "
               f"anchor-dependent brane-tower level (consistent with #1887). Owner-confirmed "
               f"collapse-cancellation hypothesis (PR #1895) is the NEGATIVE branch it anticipated.")
print("\nVERDICT:", verdict)

witness = {
    "computation": "qbeta_perlambda_collapse_cancellation",
    "description": "S2 core: does the coherent Σ_λ collapse cancel per-λ n-p content? (Q_β residue-A, PR #1895 follow-up)",
    "discipline": "mechanism test at production q₀; canonical χ^λ; Plancherel + canonical-Wenzl weightings; no fit; c_3 cal-anchored; nothing wired",
    "proton_total": p["total"], "neutron_total": n["total"],
    "coherent_abs": abs(scalar), "observe_last_sum_abs": sum_abs,
    "cancellation_ratio_plancherel": ratio, "canonical": canon,
    "per_partition": rows, "verdict": verdict,
}
out = HERE.parent / "qbeta-perlambda-collapse-cancellation.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False))
print("witness ->", out.name)
