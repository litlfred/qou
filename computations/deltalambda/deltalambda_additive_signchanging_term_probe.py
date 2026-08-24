#!/usr/bin/env python3
"""
Δ_λ magnitude: the additive sign-changing many-body term M(A) the #4307
damping-wall points to — a DERIVATION-vs-FIT discriminator (STRICT anti-fit).

Context (all DERIVED-ELSEWHERE, consumed only as bounds/targets):
  #4300 JetFiltrationTwoAnchorNoGo : single-q [A]_q! can't close A=3 & A=4.
  #4307 DampingNonMonotoneWall     : the whole DAMPING class walled — the residual
        ρ_strong(A) − ρ_grad(A) CHANGES SIGN. So closure is an ADDITIVE term M(A):
        M(A) = ρ_strong(A) − ρ_grad(A),  positive at A=3, negative at A=4.
  ρ_grad(3) = [3]_q,  ρ_grad(4) = [3]_q·[4]_q  (q-integers, q = q₀, muon layer).
  ρ_strong(3) = 3.8128, ρ_strong(4) = 13.0316  (isospin/Coulomb-corrected AME
        ratios B(³H)/B(²H), B(⁴He)/B(²H); #3986/#3990 — targets only, never inverted).

The CRUX (task): does a term M(A) from a DERIVED bond/interface principle
  (a) structurally sign-change (+ at A=3, − at A=4) from the STRUCTURE, and
  (b) LAND both residuals with 0–1 FREE PARAMETERS (a prediction), not 2 (a fit)?

This probe pre-registers a short principled candidate list, evaluates each at the
FIXED canonical q₀, and — the honest discriminator — reports the FREE-PARAMETER
COUNT of each candidate against the 2-point target.  A 0/1-param form that lands
both is a real lead; a 2-param form that lands both is VACUOUS (guaranteed).

No q and no weight is solved from the AME anchors except where explicitly labelled
"FIT" (candidate F), which is computed ONLY to exhibit the identifiability that
makes such a match non-evidential.  Nothing here is wired to production.
"""
import json
import hashlib
import subprocess
from pathlib import Path
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

# ---- fixed canonical substrate (muon-canonical computations layer) ----
Q0 = mp.mpf("1.10997859555733471989976322048322502665620840878015368660798114614493")

def qint(n, q):
    """Unbalanced q-integer [n]_q = 1 + q + ... + q^{n-1} = (q^n - 1)/(q - 1)."""
    return sum(q ** k for k in range(n))

# ρ_grad (the coinvariant graded ratio, from #4300/#4307 Lean defs) ----
rho_grad3 = qint(3, Q0)               # [3]_q
rho_grad4 = qint(3, Q0) * qint(4, Q0) # [3]_q · [4]_q

# ρ_strong: isospin/Coulomb-corrected AME comparison constants (bounds/targets only)
RHO_STRONG3 = mp.mpf("3.8128")
RHO_STRONG4 = mp.mpf("13.0316")

# The additive target M(A) = ρ_strong(A) − ρ_grad(A)
M3 = RHO_STRONG3 - rho_grad3
M4 = RHO_STRONG4 - rho_grad4
ratio_target = M3 / M4  # M(3)/M(4)

results = {}
results["substrate"] = {"q0": mp.nstr(Q0, 40)}
results["target"] = {
    "rho_grad3": mp.nstr(rho_grad3, 12),
    "rho_grad4": mp.nstr(rho_grad4, 12),
    "rho_strong3": mp.nstr(RHO_STRONG3, 12),
    "rho_strong4": mp.nstr(RHO_STRONG4, 12),
    "M3": mp.nstr(M3, 12),
    "M4": mp.nstr(M4, 12),
    "M3_over_M4": mp.nstr(ratio_target, 12),
    "note": "M(A)=rho_strong-rho_grad; sign(+,-) is the #4307 wall requirement",
}

# ---------------------------------------------------------------------------
# Simplex bond / face counts (the DERIVED interface-operator handle).
# A nucleons form a simplex K_A: edges (2-body bonds) = C(A,2),
# triangular faces (frustrated 3-cycles) = C(A,3), tetrahedra = C(A,4).
# ---------------------------------------------------------------------------
def C(n, k):
    if k < 0 or k > n:
        return 0
    num = 1
    for i in range(k):
        num = num * (n - i) // (i + 1)
    return num

edges = {A: C(A, 2) for A in (3, 4)}      # {3:3, 4:6}
tri   = {A: C(A, 3) for A in (3, 4)}      # {3:1, 4:4}
tet   = {A: C(A, 4) for A in (3, 4)}      # {3:0, 4:1}
results["simplex_counts"] = {"edges": edges, "triangles": tri, "tetrahedra": tet}

# ===========================================================================
# CANDIDATE SET.  Each records: form, free-parameter count vs the 2-pt target,
# whether it structurally sign-changes, and (for scale-only forms) whether the
# predicted ratio lands the target ratio.
# ===========================================================================
candidates = []

def scale_only_prediction(name, g3, g4, description, derived_note):
    """A 0-SHAPE-PARAM structural form M(A)=s·g(A): 1 free param (scale s) against
    2 targets ⇒ predicts the RATIO g(3)/g(4). Lands both iff ratio matches."""
    if g4 == 0:
        pred_ratio = None
        sign_ok = (g3 > 0)  # can't判定 A=4 sign
    else:
        pred_ratio = mp.mpf(g3) / mp.mpf(g4)
        sign_ok = (g3 > 0) and (g4 < 0)
    # best scale s minimising residual (least squares on 2 pts) — but the honest
    # metric is: does the fixed ratio match? report ratio error.
    lands = False
    ratio_err = None
    if pred_ratio is not None:
        ratio_err = abs(pred_ratio - ratio_target) / abs(ratio_target)
        lands = sign_ok and ratio_err < mp.mpf("0.02")  # 2% ratio tolerance
    candidates.append({
        "name": name,
        "form": description,
        "free_params_vs_2pt_target": 1,   # scale only
        "shape_params": 0,
        "g3": mp.nstr(mp.mpf(g3), 8), "g4": mp.nstr(mp.mpf(g4), 8),
        "structural_sign_change": bool(sign_ok),
        "predicted_ratio_g3_over_g4": (mp.nstr(pred_ratio, 8) if pred_ratio is not None else None),
        "target_ratio": mp.nstr(ratio_target, 8),
        "ratio_rel_err": (mp.nstr(ratio_err, 6) if ratio_err is not None else None),
        "lands_both_residuals": bool(lands),
        "derived_note": derived_note,
        "verdict": ("DERIVATION-LEAD" if lands else
                    ("sign-ok-magnitude-miss" if sign_ok else "sign-wrong")),
    })

# --- C1: pure edges (attractive bonds only). Cannot sign-change. -----------
scale_only_prediction(
    "C1_edges_only", edges[3], edges[4],
    "M(A) = s·C(A,2)  (bonds only, attractive)",
    "0 shape params; monotone-increasing in A ⇒ cannot be negative at A=4",
)

# --- C2: edges − triangles (bonds minus frustrated faces), κ=1 fixed. ------
scale_only_prediction(
    "C2_edges_minus_tri_k1", edges[3] - tri[3], edges[4] - tri[4],
    "M(A) = s·(C(A,2) − C(A,3))  (edge attraction − 1·frustrated-triangle)",
    "0 shape params (κ=1 fixed); both positive ⇒ no sign change",
)

# --- C3: edges − 2·triangles (κ=2, the 'each frustrated pair double-counts')
scale_only_prediction(
    "C3_edges_minus_2tri", edges[3] - 2*tri[3], edges[4] - 2*tri[4],
    "M(A) = s·(C(A,2) − 2·C(A,3))",
    "0 shape params (κ=2 fixed); sign(+,-)? checked",
)

# --- C4: edges − 3·triangles (κ=3, 'a frustrated triangle cancels its 3 bonds')
scale_only_prediction(
    "C4_edges_minus_3tri", edges[3] - 3*tri[3], edges[4] - 3*tri[4],
    "M(A) = s·(C(A,2) − 3·C(A,3))",
    "0 shape params (κ=3 fixed)",
)

# --- C5: tetrahedra-driven damping − edges? (the α-cluster closure at A=4) --
# M(A) = s·(edges − λ·tetrahedra) : tetra=0 at A=3 (no sign change source at A=3)
scale_only_prediction(
    "C5_edges_minus_tet", edges[3] - tet[3], edges[4] - 4*tet[4],
    "M(A) = s·(C(A,2) − 4·C(A,4))  (α-cluster tetra penalty)",
    "0 shape params; tetra=0 at A=3 so M(3)=s·3>0, M(4)=s·(6-4)=2s>0 ⇒ no change",
)

# --- C6: q-deformed frustration — edges − [3]_q·triangles (q-weighted face) -
# a 'natural' q-object: each frustrated triangle weighted by its q-integer [3]_q.
k_q = qint(3, Q0)  # [3]_q ≈ 3.342 — NOT tuned, it is the triangle's own q-dim
scale_only_prediction(
    "C6_edges_minus_q3tri",
    mp.mpf(edges[3]) - k_q*tri[3], mp.mpf(edges[4]) - k_q*tri[4],
    "M(A) = s·(C(A,2) − [3]_q·C(A,3))  (frustration weighted by triangle q-dim)",
    "0 shape params; κ=[3]_q≈3.342 is the triangle's own q-integer, not tuned",
)

# ===========================================================================
# CANDIDATE F (the FIT — computed ONLY to exhibit non-evidential identifiability)
# M(A) = s·edges(A) − t·triangles(A), TWO free weights (s,t) vs TWO targets.
# The linear map (s,t) ↦ (M3,M4) = (3s−t, 6s−4t) has det = 3·(−4) − (−1)·6 = −6 ≠ 0,
# so ANY target pair is hit by a UNIQUE (s,t). Matching both residuals is therefore
# GUARANTEED and carries zero predictive content — the anti-fit certificate.
# ===========================================================================
# Solve (3s − t = M3 ; 6s − 4t = M4):
det = mp.mpf(3)*(-4) - (mp.mpf(-1))*6   # = -6
s_fit = (M3*(-4) - (-1)*M4) / det
t_fit = (mp.mpf(3)*M4 - 6*M3) / det
candidates.append({
    "name": "F_edges_and_tri_FIT",
    "form": "M(A) = s·C(A,2) − t·C(A,3)  (TWO free weights)",
    "free_params_vs_2pt_target": 2,
    "shape_params": 1,  # κ = t/s free
    "structural_sign_change": True,   # trivially, since fitted
    "s_fit": mp.nstr(s_fit, 10), "t_fit": mp.nstr(t_fit, 10),
    "kappa_fit_t_over_s": mp.nstr(t_fit/s_fit, 10),
    "lands_both_residuals": True,
    "det_of_2x2_map": mp.nstr(det, 6),
    "derived_note": "FIT: 2 params, 2 points, invertible 2×2 ⇒ exact match GUARANTEED, "
                    "non-evidential. s,t NOT canonical Markov factors. NEVER wired.",
    "verdict": "FIT (vacuous match) — labelled, not a derivation, not wired",
})

# ---- The structural sign-change WINDOW (parameter-free existence statement) ----
# For M(A)=s·(C(A,2) − κ·C(A,3)), s>0:  M(3)=s(3−κ), M(4)=s(6−4κ).
#   M(3)>0 ↔ κ<3 ;  M(4)<0 ↔ κ>3/2.  So the bond−frustration term is sign-changing
#   (+ at A=3, − at A=4) EXACTLY for κ ∈ (3/2, 3). This is a real, 0-parameter
#   structural fact: the mechanism CAN match the #4307 sign pattern. The fitted
#   κ = t/s falls inside this window (checked), confirming the mechanism is capable
#   — but capability of the sign, at a fitted magnitude, is not a magnitude derivation.
kappa_window = (mp.mpf(3)/2, mp.mpf(3))
kappa_fit = t_fit / s_fit
results["sign_change_window"] = {
    "form": "M(A)=s·(edges − κ·triangles), s>0",
    "window_kappa": ["3/2", "3"],
    "statement": "sign(+,-) at (A=3,A=4) iff 3/2 < κ < 3 — parameter-free structural window",
    "kappa_fit": mp.nstr(kappa_fit, 8),
    "kappa_fit_in_window": bool(kappa_window[0] < kappa_fit < kappa_window[1]),
    "reading": "mechanism structurally CAPABLE of the sign change; magnitude match is a "
               "2-param fit (candidate F), hence non-evidential.",
}

results["candidates"] = candidates

# ---- honest summary ----
lead = [c for c in candidates if c.get("lands_both_residuals")
        and c.get("free_params_vs_2pt_target", 9) <= 1]
sign_capable = [c for c in candidates if c.get("structural_sign_change")]
results["summary"] = {
    "any_0or1_param_derivation_lands_both": len(lead) > 0,
    "derivation_leads": [c["name"] for c in lead],
    "structural_sign_change_available": len(sign_capable) > 0,
    "sign_capable_forms": [c["name"] for c in sign_capable if c["name"] != "F_edges_and_tri_FIT"],
    "verdict": (
        "REAL LEAD: a 0/1-param derived M(A) sign-changes AND lands both residuals"
        if len(lead) > 0 else
        "NEGATIVE/PARTIAL: bond−frustration structurally CAN sign-change (window κ∈(3/2,3)), "
        "but NO 0/1-param derived M(A) lands both magnitudes; matching both requires the "
        "2-param edge/triangle FIT (candidate F, non-evidential). Sign is derived; "
        "magnitude is a fit. Nothing wired."
    ),
}

# ---- assertions (probe self-checks; none uses AME to solve a weight) ----
assert M3 > 0, "M(3) must be positive (graded undershoots A=3)"
assert M4 < 0, "M(4) must be negative (graded overshoots A=4)"
assert kappa_window[0] < kappa_fit < kappa_window[1], "fitted κ must lie in sign window"
assert abs((s_fit*3 - t_fit) - M3) < mp.mpf("1e-40"), "fit must reproduce M3"
assert abs((s_fit*6 - t_fit*4) - M4) < mp.mpf("1e-40"), "fit must reproduce M4"
# C6 (q-weighted, 0 shape param) is the sharpest honest test — record its miss/hit:
print("=== Δ_λ additive sign-changing term M(A) — derivation-vs-fit ===")
print(f"q0 = {mp.nstr(Q0,30)}")
print(f"rho_grad(3)=[3]_q      = {mp.nstr(rho_grad3,10)}")
print(f"rho_grad(4)=[3][4]_q   = {mp.nstr(rho_grad4,10)}")
print(f"M(3)=rho_strong-rho_grad = +{mp.nstr(M3,8)}   M(4)= {mp.nstr(M4,8)}")
print(f"target ratio M(3)/M(4) = {mp.nstr(ratio_target,8)}")
print(f"sign-change window: bond-frustration term sign(+,-) iff 3/2 < κ < 3")
print(f"fitted κ = t/s = {mp.nstr(kappa_fit,8)}  (in window: {kappa_window[0]<kappa_fit<kappa_window[1]})")
print()
for c in candidates:
    print(f"[{c['name']}]  params={c.get('free_params_vs_2pt_target')}  "
          f"sign_change={c.get('structural_sign_change')}  "
          f"lands={c.get('lands_both_residuals')}  -> {c['verdict']}")
print()
print("VERDICT:", results["summary"]["verdict"])

# ---- witness ----
out = Path(__file__).resolve().parent / "deltalambda-additive-signchanging-term.witness.json"
this = Path(__file__).resolve()
witness = {
    "schema": "witness/v1",
    "producer": str(this.relative_to(this.parents[2])),
    "description": "Δ_λ additive sign-changing many-body term M(A)=ρ_strong−ρ_grad "
                   "(#4307 damping-wall follow-up): derivation-vs-fit discriminator. "
                   "Bond−frustration simplex term structurally sign-changes (window "
                   "κ∈(3/2,3)) but no 0/1-param derived form lands both residuals; the "
                   "2-param edge/triangle match is a non-evidential FIT. Anti-fit STRICT: "
                   "AME ρ_strong used only as targets, never inverted into a canonical weight.",
    "scriptHash": hashlib.sha256(this.read_bytes()).hexdigest()[:16],
    "results": results,
}
try:
    witness["scriptCommitSha"] = subprocess.check_output(
        ["git", "log", "-1", "--format=%H", "--", str(this)],
        cwd=this.parent, text=True).strip() or "uncommitted"
except Exception:
    witness["scriptCommitSha"] = "uncommitted"
out.write_text(json.dumps(witness, indent=2) + "\n")
print(f"\nwitness -> {out.name}")
