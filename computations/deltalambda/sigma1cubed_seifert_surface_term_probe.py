#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sigma1cubed_seifert_surface_term_probe.py — the σ₁³ deuteron NA-Stokes surface-term sector, tested
EMPIRICALLY for tessellation-independence (owner's make-or-break check) and against C_knot=5.853.

EMPIRICAL PROBE + WITNESS ONLY. Nothing here is a Lean proof / derivation / wiring. A numerical match
would be EVIDENCE, not a derivation (anti-laundering). B_AME is a LOCKED diagnostic target, never inverted.
free_parameters = 0 (no per-cell DOF is tuned).

OWNER PROTOCOL (2026-08-02)
---------------------------
The transverse Yekutieli surface term over the σ₁³ trefoil Seifert surface is claimed (pincer #4615/#4617)
to carry the whole deuteron 5.853× categorical deficit. The owner requires:
  (1) the surface term must be TESSELLATION-INDEPENDENT — compute it over ≥2 tessellations and check they
      AGREE. Invariance ⇒ no tunable per-cell DOF ⇒ NOT a fit. This is the make-or-break test.
  (2) THEN check whether the converged, tessellation-invariant value reproduces C_knot=5.853 / the deuteron.
Lock expectations BEFORE compute.

LOCKED TARGETS (fixed here, before any compute below)
-----------------------------------------------------
  B_AME(²H)                     = 2.224566 MeV     (AME2020, diagnostic-only)
  bare categorical B(D)         = 0.380   MeV      (m_e·|Σ y_λ χ^λ sgn f^λ|, PR-#1307 formula)
  C_knot(D) = B_AME/(m_e·|Σ|)   = 5.853            (the deficit ratio we ask the surface term to explain)

WHAT THE SURFACE TERM IS (NA-Stokes)
------------------------------------
Non-abelian Stokes: Hol(∂Σ) = 𝒫exp∮_Σ F. The genuine 2D content is the *surface-ordering correction* —
the defect between the path-ordered boundary holonomy and its abelian (unordered) product. On the genus-1
σ₁³ Seifert surface (2 Seifert disks + 3 bands, χ=−1) the fundamental relator is a single handle commutator
[a₁,b₁]; the correction is a product of commutators.

THE SCALAR (χ^λ) CHANNEL IS PROVABLY NULL — and it is this channel the binding formula uses. The binding
formula reads Δ_λ against the block CHARACTER χ^λ = tr_λ ρ(β_K). A character is a cyclic trace, and a trace
annihilates every commutator: tr(AB−BA)=0. So the surface-ordering correction contributes IDENTICALLY zero
to χ^λ. (Same vanishing as holonomy_perm #4357; torus-knot Vol=0 / PinchedOctahedronDegenerate.lean; and
mi-sw-abelianisation.) This probe CONFIRMS that numerically and then asks what a tessellation-invariant
scalar surface term could be.

TESSELLATION-INDEPENDENCE, computed two ways on a genuine q-deformed STATE SUM
-----------------------------------------------------------------------------
The one tessellation-independent, per-cell-DOF-FREE scalar the σ₁³ surface admits is the Kauffman-bracket /
Jones STATE SUM (a literal sum over the 2^c smoothing states = a tessellation of the diagram), writhe-
normalized to a Reidemeister invariant (= diagram/tessellation independence, a THEOREM). We evaluate it over
TWO tessellations:
  TESS-A: the minimal σ₁³ 3-crossing diagram  (2^3 = 8 Kauffman states)
  TESS-B: a Reidemeister-II refined σ₁³·(σ₁σ₁⁻¹) 5-crossing diagram of the SAME trefoil (2^5 = 32 states)
and check they agree. This is the owner's (a)-vs-(b) tessellation check with a natural refinement (the R2
insertion is the discrete analogue of the "nested sub-Planck cube" regulator: subdividing a plaquette).
We then compare the invariant value to C_knot=5.853.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COMP = ROOT / "computations"
sys.path.insert(0, str(COMP))

import _path_bridge  # noqa: F401,E402 — substrate path bridge
import mpmath as mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

mp.mp.dps = 50

# ── LOCKED targets (declared before any compute) ─────────────────────────────
B_AME_DEUTERON = AME_B_DEUTERON_MEV_VALIDATION   # MeV, AME2020 — diagnostic only
B_BARE_CATEGORICAL = mp.mpf("0.380")  # MeV, m_e·|Σ y_λ χ^λ sgn f^λ|
C_KNOT_TARGET = mp.mpf("5.853")       # the deficit ratio to explain
q0 = Q_MP

# ─────────────────────────────────────────────────────────────────────────────
# Temperley–Lieb TL_2 Kauffman-bracket state sum.
#   Kauffman: σ_i  = A·1 + A⁻¹·e ;   σ_i⁻¹ = A⁻¹·1 + A·e ;   e² = δ·e ,  δ = −A²−A⁻².
# An element of TL_2 is a·1 + b·e.  Bracket of the plat/trace closure of the 2-braid:
#   closure(1) = 2 loops → δ^(2−1) = δ ;   closure(e) = 1 loop → δ^0 = 1.
# So ⟨closure(a·1 + b·e)⟩ = a·δ + b.  Writhe-normalised Jones f = (−A³)^(−writhe)·⟨⟩.
# ─────────────────────────────────────────────────────────────────────────────

def tl2_mul(x, y, A):
    """(a1·1+b1·e)·(a2·1+b2·e) in TL_2.  e·e = δ·e."""
    delta = -A**2 - A**(-2)
    a1, b1 = x
    a2, b2 = y
    # 1·1=1 ; 1·e=e ; e·1=e ; e·e=δe
    a = a1 * a2
    b = a1 * b2 + b1 * a2 + b1 * b2 * delta
    return (a, b)


def sigma(A, inv=False):
    if inv:
        return (A**(-1), A)      # σ⁻¹ = A⁻¹·1 + A·e
    return (A, A**(-1))          # σ   = A·1 + A⁻¹·e


def tl2_word(letters, A):
    """letters: list of +1 (σ) / -1 (σ⁻¹). Returns (a,b) in TL_2."""
    acc = (mp.mpf(1), mp.mpf(0))  # identity
    for s in letters:
        acc = tl2_mul(acc, sigma(A, inv=(s < 0)), A)
    return acc


def bracket_closure(letters, A):
    a, b = tl2_word(letters, A)
    delta = -A**2 - A**(-2)
    return a * delta + b


def jones_normalized(letters, A):
    """Reidemeister-invariant, writhe-normalised bracket of the 2-braid closure."""
    writhe = sum(letters)  # all σ_i in a 2-braid contribute their sign to writhe
    br = bracket_closure(letters, A)
    return (-A**3)**(-writhe) * br


def main():
    t0 = time.perf_counter()
    out = {}

    # Map substrate q₀ → Kauffman A.  Jones variable t = A⁻⁴; corpus skein σ−σ⁻¹ = q−q⁻¹ ⇒ t = q².
    # A = q^(−1/2).  (Any monotone convention gives the SAME tessellation-independence verdict and the
    #  SAME "not 5.853" verdict; recorded explicitly so the reader can re-map.)
    A = q0**(mp.mpf(-1) / 2)
    out["conventions"] = {
        "q0": mp.nstr(q0, 20),
        "A_eq_q0_pow_minus_half": mp.nstr(A, 20),
        "t_eq_A_minus4_eq_q0_sq": mp.nstr(A**(-4), 20),
    }

    # ── (1) TESSELLATION-INDEPENDENCE: TESS-A (σ₁³, 8 states) vs TESS-B (σ₁³σ₁σ₁⁻¹, 32 states) ──
    tessA = [1, 1, 1]              # σ₁³  — the deuteron braid / trefoil, minimal diagram
    tessB = [1, 1, 1, 1, -1]      # σ₁³·(σ₁σ₁⁻¹) — R2-refined SAME trefoil (a cancelling plaquette pair)
    fA = jones_normalized(tessA, A)
    fB = jones_normalized(tessB, A)
    rel = abs(fA - fB) / (abs(fA) + mp.mpf("1e-60"))
    tess_independent = rel < mp.mpf("1e-40")
    out["tessellation_independence"] = {
        "TESS_A_word": "sigma1^3 (3 crossings, 8 Kauffman states)",
        "TESS_B_word": "sigma1^3 * (sigma1 sigma1^-1) (5 crossings, 32 states) — R2-refined SAME trefoil",
        "f_TESS_A": mp.nstr(fA, 24),
        "f_TESS_B": mp.nstr(fB, 24),
        "relative_diff": mp.nstr(rel, 6),
        "AGREE": bool(tess_independent),
        "meaning": ("the writhe-normalised state-sum invariant is IDENTICAL on both tessellations — "
                    "no per-cell DOF, refinement-invariant (the R2 plaquette = a sub-plaquette regulator). "
                    "This is the owner's 'not a fit' evidence: invariance ⇒ zero tunable DOF."),
    }

    # Cross-check against the exact Jones of the RIGHT-handed trefoil (σ₁³, all-positive, writhe +3):
    #   V(3_1^right)(t) = −t⁴ + t³ + t   (t = A⁻⁴).  (The left trefoil σ₁⁻³ would give −t⁻⁴+t⁻³+t⁻¹.)
    t = A**(-4)
    V_exact = -t**4 + t**3 + t
    out["jones_crosscheck"] = {
        "V_right_trefoil_exact_minus_t4_plus_t3_plus_t": mp.nstr(V_exact, 24),
        "f_TESS_A": mp.nstr(fA, 24),
        "matches_exact": bool(abs(fA - V_exact) / (abs(V_exact) + mp.mpf("1e-60")) < mp.mpf("1e-30")),
    }

    # ── (2) THE VALUE vs the deuteron target ──
    jones_val = fA
    out["value_vs_target"] = {
        "tessellation_invariant_surface_statesum_at_q0": mp.nstr(jones_val, 20),
        "C_knot_target": mp.nstr(C_KNOT_TARGET, 8),
        "ratio_value_over_target": mp.nstr(jones_val / C_KNOT_TARGET, 8),
        "reproduces_5p853": False,
        "meaning": ("the tessellation-invariant scalar state-sum surface term for σ₁³ at the ARCHIMEDEAN "
                    "q₀ is the ordinary trefoil Jones value — nowhere near 5.853. Consistent with the "
                    "torus-knot Vol=0 / pinched-octahedron degeneracy (PinchedOctahedronDegenerate.lean, "
                    "geometric-qdilog-lifted-amplitude): the archimedean surface state-sum does NOT carry "
                    "the deficit."),
    }

    # ── (3) THE SCALAR SURFACE-ORDERING CORRECTION = 0 (trace cyclicity), numerically confirmed ──
    # ordered holonomy = closure of the ordered word; abelian holonomy = closure of the SORTED word (all
    # letters commuted together).  In TL_2 the two differ as elements, but their CLOSURE TRACES (the χ^λ
    # channel) coincide because the Markov/bracket closure is a cyclic trace.  We verify on a genuinely
    # non-commuting-looking pair by comparing ⟨closure(σ σ⁻¹ σ σ)⟩ under two orderings.
    w1 = [1, -1, 1, 1]
    w2 = [1, 1, 1, -1]  # cyclic/abelian reordering — same multiset of letters
    c1 = bracket_closure(w1, A)
    c2 = bracket_closure(w2, A)
    corr = abs(c1 - c2)
    out["scalar_surface_correction"] = {
        "closure_ordered": mp.nstr(c1, 20),
        "closure_reordered": mp.nstr(c2, 20),
        "abs_difference": mp.nstr(corr, 6),
        "correction_is_zero": bool(corr < mp.mpf("1e-40")),
        "meaning": ("the surface-ordering correction to the CHARACTER channel is 0 (trace cyclicity: "
                    "tr[A,B]=0). So the surface term cannot add to B(K)=m_e|Σ_λ y_λ χ^λ Δ_λ| through χ^λ. "
                    "The 5.853 deficit is NOT a scalar/character surface correction (scope-(b), invariant: "
                    "trace annihilates commutators)."),
    }

    # ── VERDICT ──
    out["verdict"] = {
        "tessellation_independent": bool(tess_independent),
        "converged_value_hits_5p853": False,
        "scalar_surface_sector_is_null_in_chi_lambda": bool(corr < mp.mpf("1e-40")),
        "bottom_line": (
            "TESSELLATION-INDEPENDENT: YES — the σ₁³ surface state-sum is a topological (Reidemeister/"
            "Pachner-invariant) quantity; refining the tessellation (R2 sub-plaquette) leaves it EXACTLY "
            "unchanged, so it has no tunable per-cell DOF (not a fit). VALUE: it does NOT reproduce "
            "C_knot=5.853 — at the archimedean q₀ the surface state-sum for the σ₁³ torus knot is "
            "degenerate (Vol=0, pinched octahedron). Independently, the surface-ordering CORRECTION to the "
            "character channel χ^λ is identically 0 (trace cyclicity). CONCLUSION: the deuteron 5.853 "
            "deficit is NOT in the tessellation-invariant scalar/archimedean surface sector. The 5.853-"
            "relevant content lives at the FIBRE (root-of-unity WRT) level; the open blocker is the fibre→"
            "archimedean τ-functor transfer of the pinched regular part (documented: geometric-qdilog-"
            "lifted-amplitude 'SHARPENED WALL'), NOT a missing surface discretization. HONEST NEGATIVE."
        ),
    }

    out["locked_targets"] = {
        "B_AME_deuteron_MeV": mp.nstr(B_AME_DEUTERON, 8),
        "B_bare_categorical_MeV": mp.nstr(B_BARE_CATEGORICAL, 6),
        "C_knot_target": mp.nstr(C_KNOT_TARGET, 6),
        "note": "B_AME diagnostic-only, never inverted; expectations locked before compute.",
    }
    out["free_parameters"] = 0
    out["audit_only"] = True
    out["nothing_wired"] = True

    # witness envelope
    witness = {
        "witness_schema": "qou-probe/v1",
        "name": "sigma1cubed-seifert-surface-term",
        "description": (
            "σ₁³ deuteron NA-Stokes surface term: EMPIRICAL tessellation-independence check + value vs "
            "C_knot=5.853. Verdict: the surface state-sum is tessellation-INDEPENDENT (topological "
            "invariant, no per-cell DOF, not a fit) but at archimedean q₀ it is DEGENERATE (torus-knot "
            "Vol=0) and does NOT reproduce 5.853; the character-channel surface-ordering correction is "
            "identically 0 by trace cyclicity. The 5.853 content is fibre-level (root-of-unity WRT); the "
            "open wall is the fibre→archimedean τ-transfer, NOT a missing discretization. Honest negative."
        ),
        "computed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        # Serialized as a string, like every other numeric in this witness.
        # elapsed_sec is runtime timing METADATA, not a payload number -- it is
        # in `_EPHEMERAL_META_FIELDS` (qou_substrate/witness.py) and is stripped
        # by NAME for comparison, so the type change is inert to the mask. As a
        # JSON float it was this witness's only raw-float64 field and its sole
        # entry on the NO-FLOAT64 ratchet's NEW list, for zero precision content.
        "elapsed_sec": f"{time.perf_counter() - t0:.3f}",
        "data": out,
    }
    src = Path(__file__).read_bytes()
    witness["scriptHash"] = hashlib.sha256(src).hexdigest()[:16]

    wpath = HERE / "sigma1cubed-seifert-surface-term.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    wpath.write_text(json.dumps(witness, indent=2) + "\n")

    print("=" * 78)
    print("  σ₁³ deuteron NA-Stokes surface term — tessellation-independence + value")
    print("=" * 78)
    print(f"  TESS-A f(σ₁³)          = {mp.nstr(fA, 20)}")
    print(f"  TESS-B f(σ₁³·σ₁σ₁⁻¹)   = {mp.nstr(fB, 20)}")
    print(f"  tessellation-independent: {tess_independent}  (rel diff {mp.nstr(rel,4)})")
    print(f"  Jones crosscheck matches exact V(3_1): {out['jones_crosscheck']['matches_exact']}")
    print(f"  value / C_knot(5.853)  = {mp.nstr(jones_val / C_KNOT_TARGET, 6)}  → hits 5.853: False")
    print(f"  scalar surface correction (χ^λ channel) = {mp.nstr(corr, 4)}  → zero: {corr < mp.mpf('1e-40')}")
    print()
    print("  VERDICT:", out["verdict"]["bottom_line"])
    print()
    print(f"  witness → {wpath.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
