#!/usr/bin/env python3
"""deltalambda_kappa_interface_residual_simplex_probe.py — the frustration weight
κ of the #4316 bond−frustration term: DERIVE it, or wall it.

Context (all proved elsewhere; consumed only as structure/targets)
------------------------------------------------------------------
#4316 (`QOU.MassTheory.AdditiveSignChangingTerm`, sorry-free): the #4307
damping-wall residual `M(A) = ρ_strong(A) − ρ_grad(A)` is closed by an ADDITIVE
term modelled on the A-nucleon coordination simplex `K_A`:

    M(A) = s · (C(A,2) − κ · C(A,3)),   s > 0.               (#4316 model)

#4316 established: the SIGN is derived (`signChange_iff_window`: (+,−) at
(A=3,A=4) iff κ ∈ (3/2,3), 0 params) but the MAGNITUDE is a proven non-evidential
FIT — the 2-weight map (s,t=κs) ↦ (M(3),M(4)) is an isomorphism (det=−6), so any
target pair is hit; the fitted κ = 2.385 lands the residual ratio −0.1738 with no
predictive content.  The open step this session attacks: pin κ from 0–1 DERIVED
parameters (interface operator ρ_F / s5-so3 W_λ), NOT a 2-point fit.

STRICT anti-fit (AGENTS.md "no seventh fit-based ansatz", PROBE-4 KL-prune stand):
a κ read from derived structure is a derivation; a κ tuned to land −0.1738 is a
FIT.  AME ρ_strong enters ONLY as targets; never inverted into a canonical weight.

The derived structural input that changes the picture (formalize-first §3.3)
------------------------------------------------------------------------------
The #4316 model was pinned on the two points A=3,4 alone.  But the graded
reference supplies a THIRD, fully-DERIVED point at the deuteron A=2:

    ρ_grad(A) = [A]_q! / [2]_q!   (so ρ_grad(2) = [2]!/[2]! = 1, DERIVED),
    ρ_strong(2) = B(²H)/B(²H) = 1  (the deuteron is the reference of the ρ_strong
                                    ratios — its self-ratio is 1 by definition),
    ⇒  M(2) = ρ_strong(2) − ρ_grad(2) = 1 − 1 = 0.               (DERIVED, no AME fit)

M(2)=0 is not an AME datum: it is forced by the deuteron self-reference that
DEFINES the graded ladder.  It is the load-bearing derived constraint here.

Two consequences, both structural (0 free parameters):

  (1) THE #4316 MODEL IS REFUTED AT THE DEUTERON.  The model M(A)=s·C(A,2)−t·C(A,3)
      predicts M(2)=s·C(2,2)−t·C(2,3)=s·1−t·0 = s.  With s>0 (required for the sign
      window) this gives M(2)=s>0, contradicting the derived M(2)=0.  So no s>0
      instance of the bond−frustration model fits once the deuteron point is
      included — the A=3,4-only fit that produced κ=2.385 silently dropped the
      third (derived, zero) point.  The residual has NO 2-body/edge component, so
      κ = t/s (a triangle-to-EDGE ratio) is structurally ill-posed: its
      denominator s is forced to 0.

  (2) THE CORRECT DERIVED BASIS IS THE FULL SIMPLEX (MAYER) EXPANSION.  On a
      simplex K_A the exact energy decomposition is
          M(A) = μ₂·C(A,2) + μ₃·C(A,3) + μ₄·C(A,4)
      with the DERIVED coordination-graph counts C(A,k) as basis (edges,
      triangles, tetrahedra).  Three points A=2,3,4 → three coefficients → an
      EXACT 0-free-parameter solve (no fit freedom):
          μ₂ = M(2)              (edge / 2-body)
          μ₃ = M(3) − 3·μ₂       (triangle / 3-body)
          μ₄ = M(4) − 6·μ₂ − 4·μ₃ (tetrahedron / 4-body)
      This is the SAME AME residual data #4316 uses, re-expressed in the derived
      simplex basis; the CONTENT is which coefficients are non-zero.

DERIVED cross-checks (interface operator ρ_F handles, from the corpus)
---------------------------------------------------------------------
  * full-binding Mayer decomposition (`binding_mayer_linked_cluster_probe.py`,
    audit 2026-06-23): b₃/b₂=0.64, b₄/b₂=4.16 — the 4-body (tetrahedron) term
    DOMINATES, coincident with the closed [1⁴] SU(4) supermultiplet (e_A[h₃]
    vanishes for A>4). The residual μ₄ ≪ 0 found here is the SAME tetrahedron
    dominance in the graded-subtracted ladder.
  * connected 3-body cluster (`binding_cluster_operator_vs_mayer_probe.py`):
    the ρ_F Ursell/joint-H₉ 3-body cluster gives |b₃|≈1.5 MeV magnitude matching
    the empirical Mayer b₃, SIGN-OPPOSED in the chain-adjacent realisation — the
    derived 3-body handle exists but its sign/normalisation is not yet pinned.

VERDICT (pre-registered, honest): if μ₂=0 (deuteron), the κ=t/s object is
ill-posed and the #4316 edges−κ·triangles model is walled at A=2; the residual is
a PURE ≥3-body (triangle+tetrahedron) object whose derivation target is μ₄ (the
4-body α-cluster residual), reachable via the ρ_F cluster integrals (pyhecke_native
present) but requiring the residual-cluster-integral compute — an identified,
infra-scoped step, not a κ fit.  Nothing wired.
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
    """Unbalanced q-integer [n]_q = 1 + q + ... + q^{n-1}."""
    return sum(q ** k for k in range(n))


def C(n, k):
    from math import comb
    return comb(n, k)


# --- ρ_grad(A) = [A]_q!/[2]_q! : ρ_grad(2)=1, ρ_grad(3)=[3]_q, ρ_grad(4)=[3][4] --
def qfac_over_2(A, q):
    r = mp.mpf(1)
    for k in range(3, A + 1):
        r *= qint(k, q)
    return r


rho_grad = {A: qfac_over_2(A, Q0) for A in (2, 3, 4)}

# ρ_strong: isospin/Coulomb-corrected AME comparison constants (TARGETS only).
#   ρ_strong(2)=1 is the deuteron self-reference (the denominator of the ratios),
#   NOT an independent AME datum — it is DERIVED (=1 by construction).
rho_strong = {2: mp.mpf(1), 3: mp.mpf("3.8128"), 4: mp.mpf("13.0316")}

# The additive residual M(A) = ρ_strong(A) − ρ_grad(A) at A = 2, 3, 4.
M = {A: rho_strong[A] - rho_grad[A] for A in (2, 3, 4)}

# =========================================================================
# (1) The #4316 model prediction at the deuteron, and its refutation.
# =========================================================================
# A=3,4-only fit (reproduces #4316's κ=2.385): solve (3s−t=M3 ; 6s−4t=M4).
det = mp.mpf(3) * (-4) - (mp.mpf(-1)) * 6            # = -6
s_fit = (M[3] * (-4) - (-1) * M[4]) / det
t_fit = (mp.mpf(3) * M[4] - 6 * M[3]) / det
kappa_fit = t_fit / s_fit
# The model's own prediction at A=2 (the third, derived point it never used):
M2_model = s_fit * C(2, 2) - t_fit * C(2, 3)         # = s_fit
model_refuted_at_deuteron = abs(M2_model - M[2]) > mp.mpf("1e-6")

# =========================================================================
# (2) Exact 0-free-parameter simplex (Mayer) decomposition over C(A,k).
# =========================================================================
mu2 = M[2]                       # edge / 2-body   (C(2,2)=1)
mu3 = M[3] - 3 * mu2             # triangle / 3-body (C(3,2)=3, C(3,3)=1)
mu4 = M[4] - 6 * mu2 - 4 * mu3   # tetrahedron / 4-body (C(4,2)=6,C(4,3)=4,C(4,4)=1)

# self-check: the decomposition reproduces every M(A) exactly (it is a solve).
for A in (2, 3, 4):
    recon = mu2 * C(A, 2) + mu3 * C(A, 3) + mu4 * C(A, 4)
    assert abs(recon - M[A]) < mp.mpf("1e-40"), f"simplex decomposition must reproduce M({A})"

# The residual is a PURE ≥3-body object iff μ₂ = 0 (to full precision).
residual_pure_ge3body = abs(mu2) < mp.mpf("1e-40")

# =========================================================================
# Honest derivation-vs-fit ledger.
# =========================================================================
results = {
    "substrate": {"q0": mp.nstr(Q0, 40)},
    "graded_ladder": {
        "rho_grad_formula": "[A]_q! / [2]_q!",
        "rho_grad": {str(A): mp.nstr(rho_grad[A], 12) for A in (2, 3, 4)},
        "rho_strong": {str(A): mp.nstr(rho_strong[A], 12) for A in (2, 3, 4)},
        "M": {str(A): mp.nstr(M[A], 12) for A in (2, 3, 4)},
        "note": "M(2)=0 is DERIVED (deuteron self-reference), not an AME datum; "
                "it is the third, structural point #4316's A=3,4-only fit omitted.",
    },
    "kappa_4316_fit": {
        "s_fit": mp.nstr(s_fit, 10),
        "t_fit": mp.nstr(t_fit, 10),
        "kappa_fit_t_over_s": mp.nstr(kappa_fit, 10),
        "kappa_in_window_3half_3": bool(mp.mpf(3) / 2 < kappa_fit < mp.mpf(3)),
        "model_M2_prediction": mp.nstr(M2_model, 10),
        "actual_M2_derived": mp.nstr(M[2], 10),
        "model_refuted_at_deuteron": bool(model_refuted_at_deuteron),
        "verdict": "FIT κ=2.385 is an A=3,4-only artefact; the model predicts "
                   "M(2)=s>0 but the DERIVED M(2)=0 refutes it. κ=t/s ill-posed "
                   "(edge coefficient forced to 0).",
    },
    "exact_simplex_decomposition": {
        "basis": "C(A,2) edges, C(A,3) triangles, C(A,4) tetrahedra (derived "
                 "coordination-graph counts)",
        "free_parameters": 0,
        "mu2_edge_2body": mp.nstr(mu2, 10),
        "mu3_triangle_3body": mp.nstr(mu3, 10),
        "mu4_tetra_4body": mp.nstr(mu4, 10),
        "mu4_over_mu3": mp.nstr(mu4 / mu3, 10),
        "residual_pure_ge3body_mu2_zero": bool(residual_pure_ge3body),
        "reading": "Residual is a PURE ≥3-body object: NO edge/2-body component "
                   "(μ₂=0, forced by deuteron), a POSITIVE 3-body triangle μ₃, and "
                   "a large NEGATIVE 4-body tetrahedron μ₄ that dominates and drives "
                   "the sign change at A=4. The #4316 'edges−κ·triangles' form omits "
                   "the tetrahedron AND mis-assigns an edge term that is structurally "
                   "absent.",
    },
    "derived_rho_F_crosschecks": {
        "full_binding_mayer": {
            "b3_over_b2": "0.64", "b4_over_b2": "4.16",
            "note": "audit 2026-06-23; 4-body (tetra) DOMINATES, coincident with "
                    "closed [1⁴] SU(4) supermultiplet (e_A[h₃] vanishes A>4). "
                    "Same tetrahedron dominance as μ₄≪0 here.",
        },
        "connected_3body_cluster": {
            "note": "cluster-operator-vs-mayer-b3: ρ_F Ursell/joint-H₉ 3-body "
                    "cluster |b₃|≈1.5 MeV matches empirical Mayer b₃ magnitude, "
                    "SIGN-OPPOSED — derived 3-body handle exists, sign/norm unpinned.",
        },
    },
    "verdict": {
        "kappa_derived": False,
        "classification": "WALL for κ (edges−κ·triangles) + REDIRECT to derived "
                          "≥3-body simplex object μ₄",
        "scope": "(a) scope-limited: the specific bond−frustration parametrisation "
                 "with an edge term and s>0 is refuted at the deuteron (M(2)=0); "
                 "the residual is derived to be pure ≥3-body (μ₂=0). NOT a "
                 "structural exclusion of a many-body closure — μ₃>0 and μ₄<0 are "
                 "legitimate derived (triangle+tetrahedron) contributions.",
        "derivation_target": "μ₄ — the 4-body/tetrahedron α-cluster residual — "
                             "reachable via the ρ_F cluster integrals (pyhecke_native "
                             "present); requires the residual (graded-subtracted) "
                             "cluster-integral compute. Identified, infra-scoped; "
                             "NOT a κ fit. μ₃ handle = the sign-opposed 3-body Ursell "
                             "cluster (needs sign/normalisation pin).",
        "anti_fit": "κ=2.385 explicitly labelled a FIT (A=3,4-only, refuted at A=2). "
                    "μ₂,μ₃,μ₄ are the SAME AME residuals in the derived simplex basis; "
                    "μ₂=0 is the derived, AME-independent fact. Nothing wired.",
    },
}

# ---- probe self-checks (none inverts AME to solve a canonical weight) ----
assert M[2] == 0, "deuteron self-reference must give M(2)=0"
assert residual_pure_ge3body, "residual must have zero edge component (μ₂=0)"
assert model_refuted_at_deuteron, "#4316 s>0 model must be refuted at the deuteron"
assert mu3 > 0 and mu4 < 0, "triangle positive, tetrahedron negative"
assert mp.mpf(3) / 2 < kappa_fit < mp.mpf(3), "fitted κ (documented) lies in the sign window"

# ---- console report ----
print("=== Δ_λ κ: interface-operator / residual-simplex derivation-vs-fit ===")
print(f"q0 = {mp.nstr(Q0, 30)}")
print(f"ρ_grad = [A]!/[2]!:  ρ_grad(2)={mp.nstr(rho_grad[2],6)}  "
      f"ρ_grad(3)={mp.nstr(rho_grad[3],8)}  ρ_grad(4)={mp.nstr(rho_grad[4],8)}")
print(f"M(2)={mp.nstr(M[2],6)} (DERIVED, deuteron)   M(3)=+{mp.nstr(M[3],6)}   M(4)={mp.nstr(M[4],6)}")
print()
print("[#4316 fit, A=3,4 only]  κ=t/s =", mp.nstr(kappa_fit, 8),
      "(in window 3/2<κ<3:", bool(mp.mpf(3)/2 < kappa_fit < mp.mpf(3)), ")")
print(f"  → model predicts M(2)=s={mp.nstr(M2_model,6)}, actual M(2)={mp.nstr(M[2],4)} "
      f"⇒ REFUTED at the deuteron (κ=t/s ill-posed, s must be 0)")
print()
print("[exact 0-param simplex decomposition over derived C(A,k)]")
print(f"  μ₂(edge)    = {mp.nstr(mu2,8)}   ← ZERO: no 2-body component")
print(f"  μ₃(triangle)= +{mp.nstr(mu3,8)}")
print(f"  μ₄(tetra)   = {mp.nstr(mu4,8)}   ← dominant, negative (⁴He α-cluster)")
print(f"  μ₄/μ₃       = {mp.nstr(mu4/mu3,8)}")
print()
print("VERDICT:", results["verdict"]["classification"])
print("  →", results["verdict"]["derivation_target"])

# ---- witness ----
out = Path(__file__).resolve().parent / "deltalambda-kappa-interface-residual-simplex.witness.json"
this = Path(__file__).resolve()
witness = {
    "schema": "witness/v1",
    "producer": str(this.relative_to(this.parents[2])),
    "description": "Δ_λ frustration weight κ: the #4316 bond−frustration model "
                   "(M(A)=s(edges−κ·triangles), s>0) is REFUTED at the deuteron — the "
                   "DERIVED third point M(2)=0 (graded self-reference) forces its edge "
                   "coefficient s=0, so κ=t/s is ill-posed and the fitted κ=2.385 is an "
                   "A=3,4-only artefact. The exact 0-parameter simplex (Mayer) "
                   "decomposition over the derived C(A,k) basis gives μ₂(edge)=0, "
                   "μ₃(triangle)=+0.4708, μ₄(tetra)=−4.591 — a PURE ≥3-body residual, "
                   "tetrahedron-dominant-negative, matching the ρ_F full-binding Mayer "
                   "b₄/b₂=4.16 dominance. VERDICT: WALL for κ + redirect; derivation "
                   "target is μ₄ (4-body α-cluster residual), reachable via ρ_F cluster "
                   "integrals (pyhecke_native present) but requiring the residual "
                   "cluster-integral compute. Anti-fit STRICT: κ=2.385 labelled a FIT; "
                   "μ₂=0 is the AME-independent derived fact; nothing wired.",
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
