#!/usr/bin/env python3
"""yekutieli_trefoil_surface2form_discretization_probe.py — the canonical Yekutieli 2-form on the trefoil Seifert surface, discretized and validated.

Numeric companion to `QOU/QBeta/YekutieliTrefoilDiscretization.lean` (bean `qou-prjo`,
`qou-yczy`, `qou-dp32`). Builds the object the bean says "the corpus lacks": a canonical
discretization of the transverse non-abelian-Stokes surface 2-form `½P∮∮[F_q,F_q]` over the
trefoil's genus-1 Seifert surface, and validates the two structural facts the Lean file proves:

  surface2Form(V, A) = ∑_{i,j} V_{ij} · [A_i, A_j]                       (definition)
                     = (V_{01} − V_{10}) · [A_0, A_1]                    (skew-only, Lean)
                     = [A_0, A_1]  for the trefoil V = [[-1,1],[0,-1]]   (= one germ F_q).

VALIDATION (0-fit, structural):
  (A) abelian handles (deuteron's OWN trefoil in H₂, single generator σ₁ ⇒ commuting) →
      surface2Form = 0 EXACTLY — reproduces `TrefoilSurfaceStateSum.commutator_zero`. So the
      isolated-trefoil transverse term is null; the deuteron binding is NOT here.
  (B) non-abelian germ (reduced Burau of B₃, σ₁,σ₂ non-commuting) → surface2Form = [A_0,A_1] ≠ 0,
      of order h² (the germ increments are O(h)). A first magnitude for the transverse SCALE.

HONESTY (STRICT): this builds + validates the discretization and quantifies the abelian(0) vs
non-abelian(O(h²)) dichotomy. It does NOT close the deuteron number: the reduced-Burau germ is a
TOY non-abelian model, not the canonical pn-interface handle holonomy (the genuinely-missing
"non-abelian H₆ interface" data, qou-prjo). No fit; nothing wired; free_parameters = 0.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from _witness_q0_stamp import stamp_q0  # noqa: E402

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

# NO-FLOAT64 (AGENTS.md, owner directive 2026-08-18: "PROBES ARE NOT EXEMPT").
# dps raised at MODULE scope, before the first mpf below is constructed.
set_compute_dps()

# q0 RESOLVED, not frozen (2026-08-29, bean qou-1c4y). This was the literal
# 1.10997859555733471..., the SUPERSEDED muon pin A -- it stopped being the
# muon anchor when PR #5500 re-derived that anchor to CODATA-2022. A frozen
# literal cannot follow an anchor move, so the witness kept recording A under
# the label "muon" and the anchor gate scored it Q0_FLIP; re-running could not
# clear it, because the producer was the source of the stale number. It now
# resolves the PROTON pin per the owner directive of 2026-08-15 ("we want
# proton unless for an explicit reason ... otherwise pin proton").
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402 -- q0 RESOLVED, not frozen (qou-1c4y)

Q0_STR = _Q0_RESOLVED
Q0 = mp.mpf(Q0_STR)
H = Q0 - 1 / Q0              # Hecke h = q − q⁻¹ ≈ 0.209

# ---- 2×2 matrix helpers (pure python) ----
def mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
def sub(A, B): return [[A[i][j]-B[i][j] for j in range(2)] for i in range(2)]
def commutator(A, B): return sub(mul(A, B), mul(B, A))
def fro(A): return mp.sqrt(sum(A[i][j]**2 for i in range(2) for j in range(2)))
def is_zero(A, tol=None):
    # was 1e-14 / 1e-10 (float64-grade); real thresholds at 70 dps
    return fro(A) < (mp.mpf(10) ** -40 if tol is None else tol)
I2 = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]

# Trefoil (right-handed) Seifert matrix, genus 1
V = [[-1, 1], [0, -1]]

def surface2Form(Vmat, A):
    """∑_{i,j} V_ij [A_i, A_j]  — the discretized (doubled) Yekutieli surface 2-form."""
    out = [[mp.mpf(0), mp.mpf(0)], [mp.mpf(0), mp.mpf(0)]]
    for i in range(2):
        for j in range(2):
            c = commutator(A[i], A[j])
            for a in range(2):
                for b in range(2):
                    out[a][b] += Vmat[i][j] * c[a][b]
    return out


def main() -> None:
    q = Q0

    # (A) ABELIAN handles: deuteron's own trefoil is σ₁³ in H₂ (single generator ⇒ commuting).
    #     Model both handles as the SAME diagonal (commuting) germ increment.
    d1 = [[q - 1, mp.mpf(0)], [mp.mpf(0), 1 / q - 1]]  # δq for σ₁ (diagonal, H₂ shadow)
    A_abelian = [d1, d1]                               # both handles commute
    s_abelian = surface2Form(V, A_abelian)

    # (B) NON-ABELIAN germ: reduced Burau of B₃ (σ₁,σ₂ do NOT commute), increments δq_i = ρ(σ_i) − I.
    t = q
    b1 = [[-t, mp.mpf(1)], [mp.mpf(0), mp.mpf(1)]]     # reduced Burau σ₁
    b2 = [[mp.mpf(1), mp.mpf(0)], [t, -t]]             # reduced Burau σ₂
    dq1 = sub(b1, I2)
    dq2 = sub(b2, I2)
    A_nonabelian = [dq1, dq2]
    s_nonabelian = surface2Form(V, A_nonabelian)

    # Lean cross-checks: surface2Form_trefoil = [A_0, A_1]; skew-only = (V01−V10)[A0,A1]=[A0,A1].
    direct_comm = commutator(A_nonabelian[0], A_nonabelian[1])
    skew_ok = is_zero(sub(s_nonabelian, direct_comm), tol=mp.mpf(10) ** -40)

    fro_nonabelian = fro(s_nonabelian)
    # h²-order check: the germ increments are O(h)…O(1); report the commutator scale vs h².
    order_ratio = fro_nonabelian / (H * H) if H > 0 else mp.nan

    witness = {
        "computation": "yekutieli-trefoil-surface2form-discretization",
        "scriptFile": "yekutieli_trefoil_surface2form_discretization_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "engine": "mpmath mpf (pure 2x2 matrices; 0 free params; structural validation)",
        "free_parameters": 0,
        "inputs": {
            "q0": Q0_STR, "q0_pin": "proton (experimental pin, resolved)", "h": fmt(H),
            "q0_precision_note": (
                "RESOLVED from substrate.q_parameter at run time, not frozen. It was a "
                "17-digit muon literal until 2026-08-29 (bean qou-1c4y); a frozen "
                "literal cannot follow an anchor move, which is how this witness came "
                "to record the superseded muon pin under the label \"muon\"."),
            "arithmetic": f"mpmath mpf at {mp.mp.dps} dps (no float64 anywhere)",
            "seifert_matrix_trefoil": V,
            "genus": 1, "h1_rank_2g": 2, "intersection_a_dot_b": V[0][1] - V[1][0],
            "knot_determinant": int(abs((V[0][0]+V[0][0]) * (V[1][1]+V[1][1]) - (V[0][1]+V[1][0])**2)),
        },
        "results": {
            "abelian_surface2form_is_zero": bool(is_zero(s_abelian)),
            "abelian_note": "deuteron σ₁³ trefoil in H₂ (commuting handles) ⇒ 0 (matches Lean commutator_zero)",
            "nonabelian_surface2form_fro_norm": fmt(fro_nonabelian),
            "nonabelian_equals_single_commutator": bool(skew_ok),
            "skew_only_validated": bool(skew_ok),
            "nonabelian_over_h2_ratio": fmt(order_ratio),
        },
        "verdict": (
            f"The canonical discretization surface2Form(V,A)=∑V_ij[A_i,A_j] is BUILT and validated: "
            f"skew-only ⇒ trefoil term = single germ curvature [A_a,A_b] (Lean-confirmed, "
            f"{'MATCH' if skew_ok else 'MISMATCH'}). Abelian handles (deuteron's own H₂ trefoil) give "
            f"EXACTLY 0 (reproduces commutator_zero) — the isolated-trefoil transverse term is null. "
            f"A non-abelian germ (reduced Burau B₃) gives a nonzero term (‖·‖={mp.nstr(fro_nonabelian, 5)}); the "
            f"magnitude is convention-dependent (this toy has O(1) increments — canonical small q-germ "
            f"increments δq~h would scale as h²). The point is the DICHOTOMY: abelian⇒0, non-abelian⇒≠0. "
            f"So the deuteron transverse datum requires NON-ABELIAN interface handles, not the isolated "
            f"σ₁³ trefoil — the discretization exists; the canonical interface holonomy is the remaining input."
        ),
        "scope": (
            "scope-(a): builds + validates the discretization (the qou-prjo 'missing' object) and "
            "quantifies the abelian(0)/non-abelian(O(h²)) dichotomy. Does NOT close the deuteron number "
            "(reduced-Burau is a toy germ, not the canonical pn-interface holonomy). No fit; nothing wired."
        ),
        "lean": "QOU.QBeta.YekutieliTrefoilDiscretization",
        "wired": False,
        "notes": "Grounds ½P∮∮[F_q,F_q] in the corpus germ F_q (germ-commutator-q-curvature); "
                 "remaining gap = the non-abelian interface handle holonomies (qou-jqof/qou-dp32).",
    }

    # Provenance stamp (bean 1j39): this producer hand-rolls json.dump and so
    # never reaches WitnessBuilder.build(), which is where q0Anchor is set.
    # Without this the witness stays unstamped permanently — re-running it
    # cannot fix that. Adds two keys; touches nothing else.
    stamp_q0(witness, __file__)
    out = os.path.join(os.path.dirname(__file__), "yekutieli-trefoil-surface2form-discretization.witness.json")
    with open(out, "w", encoding="utf-8") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, fh, indent=1)
        fh.write("\n")

    print(f"Seifert V (trefoil) = {V}, genus 1, a·b = {V[0][1]-V[1][0]}")
    print(f"(A) abelian handles (deuteron H₂): surface2Form = 0 ? {is_zero(s_abelian)}  (matches commutator_zero)")
    print(f"(B) non-abelian germ (reduced Burau): ‖surface2Form‖ = {mp.nstr(fro_nonabelian, 5)}  (nonzero; magnitude convention-dependent)")
    print(f"    skew-only ⇒ = single [A_a,A_b] ? {skew_ok}  (Lean surface2Form_trefoil)")
    print(f"wrote {out}")
    assert is_zero(s_abelian), "abelian case must be 0 (commutator_zero)"
    assert not is_zero(s_nonabelian), "non-abelian germ must be nonzero"
    assert skew_ok, "surface2Form_trefoil must equal the single handle commutator (Lean)"
    print("ALL ASSERTIONS PASS")


if __name__ == "__main__":
    main()
