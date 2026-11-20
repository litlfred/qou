#!/usr/bin/env python3
"""
The NA-Stokes transverse-pairing gauge IS fixed — and the determined value is ZERO.

Bean `qou-prjo`. Answers the single question left open by PR #4798
(`nastokes_surface_curvature_trefoil_probe.py`, audit
`docs/audits/2026-08-08-nastokes-surface-curvature-trefoil-negative.md`):

    "Is there a DERIVED principle that fixes the germ normalization and the two
     H₁ handle holonomies?"

#4798 measured `c₂ = ‖Ω₂^⊥‖/h² ∈ [0, 897]` across six "natural" germ/handle
combinations and read the spread as O(100×) *gauge freedom the corpus does not
fix*. This probe shows the spread is an artefact of admitting choices the corpus
already excludes, and that once the corpus's own two conventions are applied the
answer is unique and equal to **zero**.

THE TWO CONVENTIONS (both pre-existing in the corpus — see §Phase 0 of the audit)

  G. GERM.  `def:germ-commutator-q-curvature` (folio/quantum-observable-universe/
     quantum-observable-universes/germ-commutator-q-curvature.md) defines δq_i as a
     *germ-level increment of the substrate parameter q* in A/𝔪_p², i.e. the
     logarithmic q-derivative  δq_i = q·(∂_q σ_i)·σ_i⁻¹.  The competing "log σ"
     object of #4798 is NOT a q-germ: log σ is the braid-direction connection
     1-form A, whose commutator is the *inter-crossing Magnus* term — a different
     object, already proved identically zero on σ₁³ (eunit_magnus_order2_probe N2).

  T. TRANSPORT.  Yekutieli path-ordering (QOU.MathlibExt.YekutieliIntegration:
     `holonomy = List.prod` in path order, `holonomy_append` the composition law)
     makes the transport to a band the ORDERED PARTIAL PRODUCT along the word.
     Seifert's algorithm on a braid closure puts discs ↔ strands and bands ↔
     crossings (b₁ = c − s + 1, Lean `seifertBettiOne`).  For the deuteron word
     σ₁³ every partial product is therefore a power of ρ(σ₁): the generator σ₂
     never occurs in the word, so #4798's `s1,s2` (c₂=897) and `s2,s1s2` (c₂=617)
     transports are INADMISSIBLE, not alternative gauges.

WHAT THIS PROBE ESTABLISHES (all exact / symbolic; sympy + mpmath cross-check)

  A1  δq₁ = q·(∂_q σ₁)·σ₁⁻¹ = [[1,−2],[0,−1]] = H − 2E   — q-INDEPENDENT, exactly.
  A2  δq₂ = q·(∂_q σ₂)·σ₂⁻¹ = [[−1,0],[0,1]] = −H        — q-INDEPENDENT, exactly.
  A3  F_q = [δq₁, δq₂] = [[0,−4],[0,0]] = −4E            — a PURE ROOT VECTOR of the
      ρ(σ₁) torus; traceless and NILPOTENT (F² = 0), q-free.
  A4  Ad(σ₁) F_q = σ₁ F_q σ₁⁻¹ = (−q²)·F_q               — the root-vector identity;
      −q² = q/(−q⁻¹) is exactly the ratio of σ₁'s Hecke eigenvalues.
  A5  ⇒ every transported curvature 𝓕_k = σ₁^{−k} F_q σ₁^{k} = (−q²)^{−k}·F_q is a
      SCALAR MULTIPLE of one and the same element, so [𝓕_i, 𝓕_j] = 0 for ALL i,j.
  A6  ⇒ Ω₂^⊥ = Σ_{ij} J_ij [𝓕_i, 𝓕_j] = 0 for EVERY Seifert intersection form J,
      EVERY H₁ basis / spanning tree, and EVERY handle-exponent assignment.
      Checked here exhaustively over all handle-exponent pairs in 0..6.
  A7  Robustness: the vanishing survives any transport in the Borel containing
      ρ(σ₁) — which is every element the word σ₁³ can build.  Only a transport
      using ρ(σ₂) escapes it, and σ₂ is not in the word.

DETERMINED VALUE:  c₂ = 0.  The target that would close the deuteron is
g₂ ≈ 1.0087.  g₂ is used ONLY for the final comparison, AFTER the value is fixed
by the principle — never as an input, never inverted.  free_parameters = 0.

SCOPE (AGENTS.md §"Before declaring refuted"): scope-(b) STRUCTURAL EXCLUSION,
restricted to single-generator (2,L)-torus channels (the deuteron pn channel).
Cited invariant: the Ad(ρ(σ₁))-eigenvector (root-vector) property of the germ
q-curvature, Lean-proved sorry-free in
QOU/MassTheory/GermRootVectorGaugeFixing.lean.  It does NOT exclude the
transverse pairing for multi-generator words (A ≥ 3), where transports involve
both generators and the eigenvector property fails — that remains scope-(a) open.

q₀: EXPERIMENTAL PROTON ANCHOR (qou_substrate.constants) per the 2026-08-07 owner
directive.  Note every symbolic result above is q-INDEPENDENT, so the pin is
immaterial to the conclusion; it is reported for layer-purity bookkeeping only.

Audit-only. No fit, no AME inversion, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # computations/probes
_COMP = HERE.parent                              # computations
for p in (str(_COMP), str(HERE), str(_COMP / "substrate")):
    if p not in sys.path:
        sys.path.insert(0, p)

import mpmath as mp                              # noqa: E402
import sympy as sp                               # noqa: E402

from eunit_magnus_order2_probe import hecke_rep, mat_log_hecke, commutator  # noqa: E402
from witness_base import WitnessBuilder          # noqa: E402

# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

Q0 = Q_MP

# The deuteron bar-even near-match coefficient (2026-07-24-eunit-magnus-order2 §F3).
# COMPARISON TARGET ONLY — never an input to anything computed below.
G2_TARGET = mp.mpf("1.0087")


# --------------------------------------------------------------------------
# Symbolic layer (exact, over ℚ(q)) — the derivation
# --------------------------------------------------------------------------
def symbolic_layer() -> dict:
    q = sp.symbols("q", nonzero=True)
    s1 = sp.Matrix([[q, -1 / q], [0, -1 / q]])
    s2 = sp.Matrix([[-1 / q, 0], [-q, q]])

    # rep sanity: braid + Hecke relations (certifies these ARE the Hecke generators)
    braid_ok = sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(2, 2)
    hecke_ok = sp.simplify((s1 - q * sp.eye(2)) * (s1 + sp.Rational(1, 1) / q * sp.eye(2))) \
        == sp.zeros(2, 2)

    # A1/A2 — the corpus germ: logarithmic q-derivative of each generator
    g1 = sp.simplify(q * sp.diff(s1, q) * s1.inv())
    g2 = sp.simplify(q * sp.diff(s2, q) * s2.inv())
    g1_const = (g1 == sp.Matrix([[1, -2], [0, -1]]))
    g2_const = (g2 == sp.Matrix([[-1, 0], [0, 1]]))

    # A3 — the germ q-curvature
    F = sp.simplify(g1 * g2 - g2 * g1)
    F_is_rootvec = (F == sp.Matrix([[0, -4], [0, 0]]))
    F_nilpotent = (sp.simplify(F * F) == sp.zeros(2, 2))
    F_traceless = (sp.simplify(sp.trace(F)) == 0)

    # A4 — the root-vector identity Ad(σ₁) F = (−q²) F
    AdF = sp.simplify(s1 * F * s1.inv())
    root_eigval = sp.simplify(AdF[0, 1] / F[0, 1]) if F[0, 1] != 0 else None
    root_ok = (sp.simplify(AdF - (-q ** 2) * F) == sp.zeros(2, 2))

    return dict(
        braid_ok=bool(braid_ok), hecke_ok=bool(hecke_ok),
        germ1=g1, germ2=g2, germ1_q_independent=bool(g1_const),
        germ2_q_independent=bool(g2_const),
        F=F, F_is_root_vector=bool(F_is_rootvec), F_nilpotent=bool(F_nilpotent),
        F_traceless=bool(F_traceless),
        root_eigenvalue=sp.simplify(root_eigval), root_identity_ok=bool(root_ok),
    )


# --------------------------------------------------------------------------
# Numeric layer (mpmath at the experimental proton anchor) — the exhaustive check
# --------------------------------------------------------------------------
def numeric_layer(q) -> dict:
    s1, s2 = hecke_rep(q)
    ds1 = mp.matrix([[1, 1 / q ** 2], [0, 1 / q ** 2]])   # ∂_q σ₁ (by hand, see docstring)
    ds2 = mp.matrix([[1 / q ** 2, 0], [-1, 1]])           # ∂_q σ₂
    dq1 = q * ds1 * s1 ** -1
    dq2 = q * ds2 * s2 ** -1
    F = commutator(dq1, dq2)
    h = q - 1 / q
    h2 = h * h

    # cross-check the symbolic constants numerically
    dev1 = mp.norm(dq1 - mp.matrix([[1, -2], [0, -1]]))
    dev2 = mp.norm(dq2 - mp.matrix([[-1, 0], [0, 1]]))
    devF = mp.norm(F - mp.matrix([[0, -4], [0, 0]]))
    devRoot = mp.norm(s1 * F * s1 ** -1 - (-q ** 2) * F)

    # A6 — exhaustive over handle-exponent pairs: EVERY admissible transport of σ₁³
    # (and beyond: exponents 0..6 cover any word length up to 6 on one generator).
    def transported(k):
        U = s1 ** k
        return U ** -1 * F * U

    worst = mp.mpf(0)
    worst_pair = None
    for a in range(7):
        for b in range(7):
            nrm = mp.norm(commutator(transported(a), transported(b)))
            if nrm > worst:
                worst, worst_pair = nrm, (a, b)
    c2_determined = worst / h2

    # the derived trefoil reading: genus-1, J = V − Vᵀ = [[0,1],[-1,0]], handles at
    # the partial products before bands 2 and 3 of σ₁³, i.e. exponents 1 and 2.
    J01 = mp.mpf(1)
    Om_trefoil = mp.mpf("0.5") * (J01 * commutator(transported(1), transported(2))
                                  - J01 * commutator(transported(2), transported(1)))
    c2_trefoil = mp.norm(Om_trefoil) / h2

    # the INADMISSIBLE #4798 entries, recomputed here only to attribute them
    def conj(U, M):
        return U ** -1 * M * U

    def pairing(Ua, Ub):
        return mp.mpf("0.5") * (commutator(conj(Ua, F), conj(Ub, F))
                                - commutator(conj(Ub, F), conj(Ua, F)))

    inadmissible = {
        "qderiv;s1,s2 (uses sigma_2, absent from the word)":
            mp.norm(pairing(s1, s2)) / h2,
        "qderiv;s2,s1s2 (uses sigma_2, absent from the word)":
            mp.norm(pairing(s2, s1 * s2)) / h2,
    }
    # the "log" germ is not a q-germ at all — it is the connection 1-form
    F_log = commutator(mat_log_hecke(s1, q), mat_log_hecke(s2, q))

    def pairing_log(Ua, Ub):
        return mp.mpf("0.5") * (commutator(conj(Ua, F_log), conj(Ub, F_log))
                                - commutator(conj(Ub, F_log), conj(Ua, F_log)))

    wrong_germ = {
        "log-germ;s1,s1^2 (log sigma is the connection, not a q-germ)":
            mp.norm(pairing_log(s1, s1 ** 2)) / h2,
    }
    # why the wrong germ fails to vanish: it is NOT a root vector
    log_root_defect = mp.norm(s1 * F_log * s1 ** -1
                              - (mp.norm(s1 * F_log * s1 ** -1) / mp.norm(F_log)) * F_log)

    return dict(h=h, h2=h2, dev1=dev1, dev2=dev2, devF=devF, devRoot=devRoot,
                worst=worst, worst_pair=worst_pair, c2_determined=c2_determined,
                c2_trefoil=c2_trefoil, inadmissible=inadmissible,
                wrong_germ=wrong_germ, log_root_defect=log_root_defect)


def main() -> int:
    W = 88
    print("=" * W)
    print("  NA-Stokes transverse pairing — the gauge IS fixed; determined value = 0")
    print("=" * W)

    S = symbolic_layer()
    print("\n  [SYMBOLIC, exact over ℚ(q)]")
    print(f"    braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂            : {S['braid_ok']}")
    print(f"    Hecke relation (σ₁−q)(σ₁+q⁻¹) = 0         : {S['hecke_ok']}")
    print(f"    A1  δq₁ = q(∂_qσ₁)σ₁⁻¹ = {str(S['germ1'].tolist()):<28}"
          f" q-independent: {S['germ1_q_independent']}")
    print(f"    A2  δq₂ = q(∂_qσ₂)σ₂⁻¹ = {str(S['germ2'].tolist()):<28}"
          f" q-independent: {S['germ2_q_independent']}")
    print(f"    A3  F_q = [δq₁,δq₂]    = {str(S['F'].tolist()):<28}"
          f" root vector: {S['F_is_root_vector']}")
    print(f"        traceless: {S['F_traceless']}   nilpotent (F²=0): {S['F_nilpotent']}")
    print(f"    A4  Ad(σ₁) F_q = ({S['root_eigenvalue']})·F_q        "
          f" identity holds: {S['root_identity_ok']}")

    N = numeric_layer(Q0)
    print("\n  [NUMERIC, experimental proton anchor q₀ = "
          f"{mp.nstr(Q0, 18)}, h² = {mp.nstr(N['h2'], 8)}]")
    print(f"    symbolic↔numeric agreement: ‖δq₁−const‖={mp.nstr(N['dev1'], 3)}  "
          f"‖δq₂−const‖={mp.nstr(N['dev2'], 3)}  ‖F+4E‖={mp.nstr(N['devF'], 3)}")
    print(f"    root identity residual ‖σ₁Fσ₁⁻¹ + q²F‖ = {mp.nstr(N['devRoot'], 3)}")
    print("\n  [A6 — EXHAUSTIVE over handle-exponent pairs (a,b) ∈ {0..6}²]")
    print(f"    max over ALL 49 pairs of ‖[𝓕_a, 𝓕_b]‖ = {mp.nstr(N['worst'], 6)}"
          f"   (attained at {N['worst_pair']})")
    print(f"    ⇒ DETERMINED c₂ = max‖Ω₂^⊥‖/h² = {mp.nstr(N['c2_determined'], 6)}")
    print(f"    derived trefoil reading (J=V−Vᵀ, handles at exponents 1,2): "
          f"c₂ = {mp.nstr(N['c2_trefoil'], 6)}")

    print("\n  [WHY #4798 SAW 0…897 — every nonzero entry is inadmissible]")
    for k, v in N["inadmissible"].items():
        print(f"    {k:<58} c₂ = {mp.nstr(v, 6)}")
    print("      (the second is 0 anyway — its two transports differ by ρ(σ₁), so the")
    print("       root-vector mechanism applies to it too; it is still inadmissible.)")
    for k, v in N["wrong_germ"].items():
        print(f"    {k:<58} c₂ = {mp.nstr(v, 6)}")
    print(f"    log-germ root-vector defect ‖Ad(σ₁)F_log − λF_log‖ = "
          f"{mp.nstr(N['log_root_defect'], 6)}  (≠0 ⇒ not a root vector)")

    print("\n  [COMPARISON — made only AFTER the value is fixed by the principle]")
    print(f"    determined c₂ = {mp.nstr(N['c2_determined'], 6)}   "
          f"target g₂ = {mp.nstr(G2_TARGET, 6)}   ⇒ the pairing supplies NOTHING at O(h²).")

    print("\n" + "=" * W)
    print("  VERDICT — scope-(b) STRUCTURAL EXCLUSION on single-generator (2,L) channels.")
    print("  Invariant: F_q is an Ad(ρ(σ₁))-eigenvector (Lean, sorry-free,")
    print("  QOU/MassTheory/GermRootVectorGaugeFixing.lean). Every transport the σ₁³ word")
    print("  can build is a power of ρ(σ₁); all transported curvatures are then scalar")
    print("  multiples of one element, so EVERY intersection form and EVERY handle")
    print("  assignment gives Ω₂^⊥ = 0. The 0…897 spread of #4798 is not gauge freedom —")
    print("  its nonzero entries use ρ(σ₂) (absent from the word) or log σ (the connection")
    print("  1-form, not a q-germ). Together with the already-proved vanishing of the")
    print("  LONGITUDINAL inter-crossing Magnus tower on σ₁³, the deuteron channel is")
    print("  order-2 STERILE in both directions: the −9.2% h² gap is not an order-2")
    print("  NA-Stokes effect at all. A ≥ 3 (multi-generator) is untouched — scope-(a) open.")
    print("=" * W)

    ok = (S["braid_ok"] and S["hecke_ok"] and S["germ1_q_independent"]
          and S["germ2_q_independent"] and S["F_is_root_vector"] and S["F_nilpotent"]
          and S["root_identity_ok"])

    # ---------------- witness ----------------
    w = WitnessBuilder("nastokes-germ-root-vector-gauge", engine="sympy+mpmath",
                       output_dir=HERE)
    w.set_description(
        "Bean qou-prjo. Resolves the gauge under-determination reported by PR #4798 for "
        "the transverse NA-Stokes surface-curvature pairing on the deuteron (σ₁³/trefoil) "
        "Seifert surface. Two corpus conventions — the germ (def:germ-commutator-q-curvature: "
        "δq is a germ-level increment of q, i.e. the logarithmic q-derivative) and the "
        "transport (Yekutieli path-ordering + Seifert bands↔letters) — fix both gauges. "
        "The q-derivative germs are q-independent constants (H−2E, −H); their commutator "
        "F_q = −4E is a pure root vector of the ρ(σ₁) torus with Ad(σ₁)F_q = −q²F_q, so "
        "every transported curvature is a scalar multiple of one element and the pairing "
        "vanishes for EVERY intersection form and EVERY handle-exponent assignment "
        "(checked exhaustively over 49 pairs). Determined c₂ = 0, not the g₂ ≈ 1.0087 that "
        "would close the deuteron. scope-(b) structural exclusion restricted to "
        "single-generator (2,L)-torus channels; A ≥ 3 multi-generator remains scope-(a) open. "
        "Lean (sorry-free): QOU/MassTheory/GermRootVectorGaugeFixing.lean. "
        "0 free parameters; g₂ used only for the post-hoc comparison, never inverted."
    )
    w.set_audit_only(True)
    w.add_parameter("q0_experimental_proton_anchor", mp.nstr(Q0, 30))
    w.add_parameter("q0_pin", "experimental/proton (qou_substrate.constants)")
    w.add_parameter("free_parameters", 0)
    w.add_parameter("channel_word", "sigma_1^3 (deuteron pn / trefoil, single generator)")
    w.add_parameter("germ_convention", "logarithmic q-derivative q*(d_q sigma)*sigma^-1")
    w.add_parameter("transport_convention",
                    "Yekutieli ordered partial product along the braid word")
    w.add_data("germ1", str(S["germ1"].tolist()))
    w.add_data("germ2", str(S["germ2"].tolist()))
    w.add_data("germ_curvature", str(S["F"].tolist()))
    w.add_data("root_eigenvalue", str(S["root_eigenvalue"]))
    w.add_data("h_squared_at_q0", mp.nstr(N["h2"], 20))
    w.add_data("c2_determined", mp.nstr(N["c2_determined"], 12))
    w.add_data("c2_trefoil_derived_reading", mp.nstr(N["c2_trefoil"], 12))
    w.add_data("max_pairing_norm_over_49_handle_pairs", mp.nstr(N["worst"], 12))
    w.add_data("g2_comparison_target_not_an_input", mp.nstr(G2_TARGET, 8))
    w.add_data("inadmissible_choices_from_pr4798",
               {k: mp.nstr(v, 8) for k, v in N["inadmissible"].items()})
    w.add_data("wrong_germ_choices_from_pr4798",
               {k: mp.nstr(v, 8) for k, v in N["wrong_germ"].items()})
    w.add_assertion("braid_relation_holds", 1 if S["braid_ok"] else 0, 1)
    w.add_assertion("hecke_relation_holds", 1 if S["hecke_ok"] else 0, 1)
    w.add_assertion("germs_are_q_independent",
                    1 if (S["germ1_q_independent"] and S["germ2_q_independent"]) else 0, 1)
    w.add_assertion("germ_curvature_is_pure_root_vector",
                    1 if S["F_is_root_vector"] else 0, 1)
    w.add_assertion("germ_curvature_nilpotent", 1 if S["F_nilpotent"] else 0, 1)
    w.add_assertion("ad_sigma1_eigenvector_identity", 1 if S["root_identity_ok"] else 0, 1)
    w.add_assertion("pairing_vanishes_all_49_handle_pairs",
                    1 if N["worst"] < mp.mpf("1e-40") else 0, 1)
    w.add_caveat("scope-(b) STRUCTURAL EXCLUSION restricted to single-generator (2,L)-torus "
                 "channels. Cited invariant: the Ad(rho(sigma_1))-eigenvector property of the "
                 "germ q-curvature. Multi-generator words (A >= 3) are NOT excluded — there "
                 "the transports involve both generators and the eigenvector property fails; "
                 "that case remains scope-(a) open.")
    w.add_caveat("'sorry-free != derived' seam: the step d_q sigma_i = ds_i is entrywise "
                 "differentiation done by hand (sympy checks it here; Lean takes ds_i as "
                 "supplied data). Everything downstream of it is machine-checked.")
    w.add_caveat("Every symbolic result is q-INDEPENDENT, so the q0 pin does not affect the "
                 "conclusion; the experimental proton anchor is recorded for layer purity.")
    w.save()
    print("\nwitness -> nastokes-germ-root-vector-gauge.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
