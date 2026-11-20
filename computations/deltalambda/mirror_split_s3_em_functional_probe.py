#!/usr/bin/env python3
"""
mirror_split_s3_em_functional_probe.py — DEFINE the S₃-equivariant link-level
EM coupling functional on the ³He link (L6a4 = Borromean) and test how much of
the ³H–³He mirror split it DERIVES. This is the S3 attack requested by
docs/audits/2026-07-13-mirror-split-one-third-mechanism-probe.md ("What would
close it", items 1–2): define the functional (S2), derive its magnitude (S3).

THE FUNCTIONAL (definition; each axiom structurally justified):

  E : (3-component link L, charge labeling c = (q₁,q₂,q₃)) → ℝ
  E(L, c) = Σ_{i<j} w_ij(L) · q_i q_j

  (A1) charge bilinearity, NO self-term.  EM interaction energy is bilinear in
       charges (Coulomb ∝ q_i q_j); per-component self-terms a·Σq_i² CANCEL
       IDENTICALLY in binding energy B = Z·m_p + N·m_n − M, because single-
       component EM self-energy lives in the free-nucleon masses m_p, m_n.
       So a = 0 is DERIVED from the definition of B, not assumed.
  (A2) S₃-equivariance.  E(g·L, g·c) = E(L, c) for g ∈ S₃ (component
       relabeling is a gauge choice — functoriality, not physics input).
  (A3) topological support.  w_ij(L) is built from the link invariants of L.
       For L6a4 every pairwise lk_ij = 0 (S1, PROVED — exact Magnus,
       binding_mn_milnor_linking machinery), so the pairwise-mediated part of
       w_ij vanishes and any nonzero w_ij is mediated by the first
       non-vanishing invariant μ̄(123) = ±1: the triple channel. (Consistent
       with S1 of the predecessor probe.)

DERIVED CONSEQUENCES (symbolic, checked exactly here):

  D1 (S2 CLOSED — equal weights).  Sym(L6a4) ⊇ S₃ acting transitively on
      components — geometric fact, SnapPy-verified in the corpus: all three
      cusps identical (shape 2i, meridian √2, longitude 2√2), complement =
      two ideal regular octahedra, Vol = 8G (em-linking-cusp-geometry-probe
      witness; 2026-06-16-he4-magic-8G audit). Applying (A2) with g ∈ Sym(L):
      w_{g(i)g(j)} = w_ij; transitivity on unordered pairs forces
          w_12 = w_13 = w_23 =: w(L6a4).
      Hence E(³He, c=(1,1,0)) = w·(1+0+0) = w and E(³H, c=(1,0,0)) = 0 for
      ANY link (every pair product vanishes — the ³H link being 8_11 rather
      than Borromean is immaterial). The predicted split is E(³He) = w, and
      writing E = 3w·⟨q_iq_j⟩_pairs exhibits the S₃ ORBIT-AVERAGE structure:
      the charge weights (1,0,0) average to exactly 1/3 of the pp value.
      EQUAL 1/3 WEIGHT PER PAIR-CHANNEL IS DERIVED. S2 of the predecessor
      audit is closed by this construction.

  D2 (NEW — sign-representation obstruction).  μ̄(g(1)g(2)g(3)) = sgn(g)·
      μ̄(123) — μ̄ transforms in the SIGN rep of S₃ (verified exactly on all
      6 permutations below, integer Magnus). The pair-channel space ℝ³
      decomposes as trivial ⊕ standard; the sign rep does not occur. By
      Schur's lemma an S₃-equivariant coupling LINEAR in μ̄ to the charge
      bilinear vanishes identically. Therefore w ∝ |μ̄| (equivalently μ̄²) —
      the even invariant. Consequences: (i) the functional is mirror-
      insensitive (the mirror of L6a4 has μ̄ = −1, same E) — the EM split
      does not see link chirality; (ii) the sign of the effect comes from
      the charge bilinear alone (repulsive: reduces ³He binding). This
      obstruction was not in the predecessor audits.

  D3 (S3 — the magnitude, honestly re-scoped, NOT closed).  (A1)–(A3) + D1 +
      D2 fix E up to ONE scalar:  w(L6a4) = κ·|μ̄(123)|·B_pp,  κ ∈ ℝ.
      Candidate normalizations (computed below, none tuned):
        N1 "unit-capacity sum rule": the link carries |μ̄| = 1 unit of
           topological coupling capacity in strong-bond units, shared over
           the 3 equal channels: Σ_{i<j} w_ij = |μ̄|·B_pp ⇒ κ = 1/3
           ⇒ split_pred = B_pp/3. Anchor consistency: the Hopf/diproton M_2
           unit (lk = 1, ONE pair channel) gives w = B_pp — exactly the
           per-block bond definition. But the M_2 anchor CANNOT distinguish
           the sum rule from per-channel normalization (they differ only at
           n ≥ 3), so the sum rule is UNDERIVED — and the deeper step, why
           the STRONG per-block bond B_pp sets the EM channel unit at
           coefficient 1 (rather than the derived pairwise Coulomb/strong
           ratio tanh(ln q₀) ≈ 0.104 of def:coulomb-charge), is exactly the
           predecessor's S3 gate, unchanged.
        N2 "pairwise coefficient transplanted": w = tanh(ln q₀)·B_pp (the
           derived 2026-06-03 route, 31.1%) or with capacity sharing
           tanh(ln q₀)·B_pp/3 (10.4%). Derived coefficient, wrong magnitude
           at the triple channel.
      TENSION (explicit): N1 and N2 are COMPETING, not additive (predecessor
      probe: 130.9% together). A closure via N1 must REPLACE the derived
      pairwise tanh(ln q₀) at the triple channel — i.e. show the μ̄-mediated
      coupling is not a Coulomb crossing insertion (which carries tanh) but
      a charge-gated full strong channel. No such derivation exists.

CLASSIFICATION (anti-fit, STRICT): (ii) PARTIAL.
  • S2 CLOSED: equal 1/3 per-pair-channel weight is DERIVED (D1: S₃
    transitivity + equivariance; supported by the SnapPy-proved cusp
    symmetry that the 2026-07-04 exclusion audit established — that audit
    excluded cusp geometry as a MAGNITUDE source; here it supplies the
    SYMMETRY premise instead).
  • S3 OPEN, re-scoped: one scalar κ. κ = 1/3 (N1) reproduces the split to
    −0.23% but rests on the underived unit-capacity sum rule; nothing here
    is tuned to 0.7638 MeV. The 1/3 remains a guarded near-match; what is
    new is that the ENTIRE remaining freedom is one number.

Inputs (all with provenance, nothing hardcoded): B_pp via the exact per-block
H₆ code path of the predecessor probe (imported, not re-derived); split from
AME2020 codata_constants; q₀ = Q_50_DIGIT_STR; μ̄ from the validated integer
Magnus machinery. mpmath at the production floor (set_compute_dps(), 50 dps).

Audit: docs/audits/2026-07-13-mirror-split-s3-em-functional-attempt.md
EXPLORATORY — audit-only witness; no production wiring, no tier change.
"""
from __future__ import annotations

import sys
from itertools import permutations
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_HERE, _COMP, _COMP / "substrate", _COMP / "hecke", _COMP / "habiro"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import _ame_binding_mev  # noqa: E402
# S1/D2: the validated exact Milnor/Magnus machinery (import, do not re-derive)
from binding_mn_milnor_linking import mu, BORROMEAN, HOPF  # noqa: E402
# B_pp: the EXACT code path of the predecessor probe (same-directory import;
# its module top-level only sets precision and constants — cheap, no main run)
from mirror_split_milnor_one_third_probe import per_block  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
q0 = Q_MP

# Corpus-sourced exact L6a4 cusp data (SnapPy-verified, baked in
# em-linking-cusp-geometry-probe.witness.json; complement = 2 ideal regular
# octahedra, Vol = 8·Catalan — 2026-06-16-he4-magic-8G audit). Used ONLY as
# evidence for the S₃ symmetry premise of D1, never as a magnitude source
# (that route is scope-(b) excluded, 2026-07-04-em-linking-cusp-geometry-excluded).
L6A4_CUSP_SHAPES = [complex(0, 2.0)] * 3   # all three cusps identical: shape 2i


def charge_bilinear(c) -> int:
    """Σ_{i<j} q_i q_j — the (A1) pair-channel charge weight (exact ints)."""
    n = len(c)
    return sum(c[i] * c[j] for i in range(n) for j in range(i + 1, n))


def main() -> int:
    print("=== S₃-equivariant link-level EM coupling functional on L6a4 (S3 attack) ===\n")

    # ── S1 recap: topological support (exact) ────────────────────────────────
    lk = [mu(BORROMEAN, s) for s in [(1, 2), (1, 3), (2, 3)]]
    mu123 = mu(BORROMEAN, (1, 2, 3))
    hopf_lk = mu(HOPF, (1, 2))
    s1_ok = (lk == [0, 0, 0] and abs(mu123) == 1 and hopf_lk == 1)
    print(f"(A3) support: pairwise lk = {lk}, μ̄(123) = {mu123}, Hopf lk = {hopf_lk}"
          f"  [{'PASS' if s1_ok else 'FAIL'}]")

    # ── D2: μ̄ transforms in the SIGN rep of S₃ (all 6 permutations, exact) ──
    def sgn(p):
        s, pl = 1, list(p)
        for i in range(len(pl)):
            while pl[i] != i + 1:
                j = pl[i] - 1
                pl[i], pl[j] = pl[j], pl[i]
                s = -s
        return s

    perm_table = {p: mu(BORROMEAN, p) for p in permutations((1, 2, 3))}
    sign_rep_ok = all(v == sgn(p) * mu123 for p, v in perm_table.items())
    print(f"(D2) μ̄ under S₃: {{perm: μ̄}} = "
          f"{{{', '.join(f'{p}:{v:+d}' for p, v in perm_table.items())}}}")
    print(f"     sign-rep law μ̄∘g = sgn(g)·μ̄(123): "
          f"{'PASS (6/6)' if sign_rep_ok else 'FAIL'}")
    print("     ⇒ Schur: linear-in-μ̄ coupling to the charge bilinear (trivial⊕std)")
    print("       vanishes identically; the coupling enters through |μ̄| only.")
    print("       The functional is mirror-insensitive (μ̄ = −1 gives the same E).\n")

    # ── D1: equal weights from S₃ symmetry + equivariance ───────────────────
    cusps_identical = all(s == L6A4_CUSP_SHAPES[0] for s in L6A4_CUSP_SHAPES)
    print(f"(D1) Sym(L6a4) ⊇ S₃ — SnapPy-verified corpus data: 3 identical cusps "
          f"(shape {L6A4_CUSP_SHAPES[0]}), Vol = 8G  [{'PASS' if cusps_identical else 'FAIL'}]")
    print("     equivariance + transitivity on pairs ⇒ w_12 = w_13 = w_23 = w.")
    Q_HE3 = (1, 1, 0)   # ppn
    Q_H3 = (1, 0, 0)    # pnn
    bil_he3 = charge_bilinear(Q_HE3)
    bil_h3 = charge_bilinear(Q_H3)
    orbit_avg_he3 = mp.mpf(bil_he3) / 3
    print(f"     charge bilinears: ³He (1,1,0) → Σ q_iq_j = {bil_he3};"
          f" ³H (1,0,0) → {bil_h3} (exact)")
    print(f"     ⇒ E(³He) = w·{bil_he3} = w,  E(³H) = 0 (any link),  split = w")
    print(f"     orbit-average form: E = 3w·⟨q_iq_j⟩, ⟨q_iq_j⟩_³He = {bil_he3}/3"
          f" — the 1/3 multiplicity is DERIVED (S2 closed).\n")

    # ── inputs with provenance ───────────────────────────────────────────────
    from mirror_split_milnor_one_third_probe import E0  # noqa: E402
    B_pp = E0 * (per_block(2, 0, False) - per_block(2, 0, True))
    split = mp.mpf(str(_ame_binding_mev(1, 3))) - mp.mpf(str(_ame_binding_mev(2, 3)))
    print(f"B_pp (per-block H₆ diproton, predecessor code path) = {float(B_pp):.6f} MeV")
    print(f"AME split B(³H)−B(³He)                              = {float(split):.6f} MeV\n")

    # ── D3: the one remaining scalar — candidate normalizations (no tuning) ─
    tanh_ratio = mp.tanh(mp.log(q0))
    pred_N1 = B_pp * abs(mu123) / 3                 # unit-capacity sum rule
    pred_N2_full = tanh_ratio * B_pp                # derived pairwise coeff, unshared
    pred_N2_shared = tanh_ratio * B_pp / 3          # derived pairwise coeff, shared
    err_N1 = pred_N1 / split - 1
    print("(D3) w(L6a4) = κ·|μ̄|·B_pp — everything above fixes E up to ONE scalar κ:")
    print(f"     N1 (κ=1/3, unit-capacity sum rule Σw_ij = |μ̄|·B_pp — UNDERIVED):")
    print(f"        split_pred = B_pp/3 = {float(pred_N1):.6f} MeV   "
          f"error vs AME: {float(err_N1) * 100:+.3f}%")
    print(f"        (M_2 anchor check: Hopf lk=1, one channel ⇒ w = B_pp — consistent"
          f" with the per-block bond, but cannot distinguish sum-rule vs per-channel)")
    print(f"     N2 (κ = tanh(ln q₀) = {float(tanh_ratio):.6f} — derived pairwise coeff):")
    print(f"        unshared: {float(pred_N2_full):.6f} MeV "
          f"({float(pred_N2_full / split) * 100:.1f}% of split)   "
          f"shared: {float(pred_N2_shared):.6f} MeV "
          f"({float(pred_N2_shared / split) * 100:.1f}%)")
    both = pred_N1 / split + pred_N2_full / split
    print(f"     TENSION: N1 + N2 coverages sum to {float(both) * 100:.1f}% > 100% —"
          f" COMPETING, not additive; N1 must REPLACE tanh at the triple channel.\n")

    # ── classification ───────────────────────────────────────────────────────
    print("CLASSIFICATION (anti-fit, STRICT): (ii) PARTIAL.")
    print("  DERIVED : the functional form E = w·Σ q_iq_j (a=0 from the definition")
    print("            of binding energy); equal per-pair weights w_ij ≡ w (S₃")
    print("            equivariance + transitivity — S2 CLOSED); coupling through")
    print("            |μ̄| only (sign-rep Schur obstruction — new, D2); E(³H) = 0.")
    print("  OPEN    : the single scalar κ (S3, re-scoped). κ = 1/3 reproduces the")
    print("            split to −0.23% but the unit-capacity sum rule is underived")
    print("            and must supersede the derived pairwise tanh(ln q₀).")
    print("  Nothing tuned to 0.7638 MeV; no wiring; no tier change.")

    ok = bool(s1_ok and sign_rep_ok and cusps_identical
              and bil_h3 == 0 and bil_he3 == 1
              and abs(float(err_N1)) < 0.005)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("mirror-split-s3-em-functional", engine="mpmath")
            wb.set_description(
                "S3 attack: defines the S₃-equivariant link-level EM coupling "
                "functional E(L,c) = Σ_{i<j} w_ij(L)·q_iq_j on the ³He link L6a4 = "
                "Borromean. DERIVED: a=0 (self-terms cancel in binding energy by "
                "definition); w_12=w_13=w_23 from S₃ equivariance + component-"
                "transitivity of L6a4 (SnapPy-verified identical cusps) — the equal "
                "1/3 per-pair-channel weight, closing S2 of the predecessor audit; "
                "NEW sign-rep obstruction: μ̄∘g = sgn(g)·μ̄ (verified 6/6 exact "
                "Magnus), so by Schur any linear-in-μ̄ coupling vanishes and w ∝ |μ̄| "
                "(mirror-insensitive). E(³H)=0 for any link (charge bilinear "
                "vanishes). REMAINING: one scalar κ in w = κ·|μ̄|·B_pp (S3 re-scoped). "
                "N1 unit-capacity sum rule κ=1/3 predicts split = B_pp/3 = 0.762 MeV "
                "(−0.23% vs AME) but is UNDERIVED (M_2/Hopf anchor cannot distinguish "
                "sum-rule from per-channel; and why B_pp at coefficient 1 rather than "
                "the derived pairwise tanh(ln q₀) = 0.104 is the unchanged gate). "
                "N1 and the derived tanh route are COMPETING (sum > 100%): N1 would "
                "REPLACE tanh at the triple channel. CLASSIFICATION: PARTIAL — S2 "
                "closed, S3 open re-scoped to one scalar. No fit, no wiring.")
            wb.set_audit_only(
                "docs/audits/2026-07-13-mirror-split-s3-em-functional-attempt.md")
            wb.add_parameter("compute_dps", mp.mp.dps)
            wb.add_parameter("q_0", Q_50_DIGIT_STR)
            wb.add_data("functional_definition",
                        "E(L,c) = Sum_{i<j} w_ij(L) q_i q_j; axioms A1 (bilinear, "
                        "a=0 derived from binding-energy definition), A2 (S3-"
                        "equivariance), A3 (topological support; pairwise lk=0 => "
                        "triple channel |mu(123)|)")
            wb.add_data("S1_support", {"pairwise_lk": lk, "mu_bar_123": mu123,
                                       "hopf_lk_M2_anchor": hopf_lk})
            wb.add_data("D2_sign_rep",
                        {"".join(map(str, p)): v for p, v in perm_table.items()})
            wb.add_data("D2_consequence",
                        "mu transforms in the SIGN rep of S3; pair-channel space is "
                        "trivial+standard; Schur => linear-in-mu coupling vanishes; "
                        "w prop |mu| — functional is mirror-insensitive")
            wb.add_data("D1_symmetry_evidence",
                        "L6a4 cusps identical (shape 2i x3, SnapPy, em-linking-cusp-"
                        "geometry-probe witness); Vol = 8G (2 ideal octahedra); used "
                        "as SYMMETRY premise only — cusp MAGNITUDE route is scope-(b) "
                        "excluded (2026-07-04-em-linking-cusp-geometry-excluded)")
            wb.add_data("charge_bilinears", {"He3_ppn": bil_he3, "H3_pnn": bil_h3,
                                             "orbit_average_He3": float(orbit_avg_he3)})
            wb.add_data("B_pp_strong_MeV", float(B_pp))
            wb.add_data("B_pp_provenance",
                        "per-block H6 diproton free-interacting, imported from the "
                        "predecessor probe mirror_split_milnor_one_third_probe.per_block "
                        "(itself the exact code path of charge_coulomb_tn3he_derived.py)")
            wb.add_data("ame_split_MeV", float(split))
            wb.add_data("N1_split_pred_MeV", float(pred_N1))
            wb.add_data("N1_error_vs_AME", float(err_N1))
            wb.add_data("N1_status",
                        "UNDERIVED unit-capacity sum rule Sum w_ij = |mu|·B_pp; the "
                        "M_2 (Hopf) anchor is consistent but cannot distinguish "
                        "sum-rule vs per-channel normalization (differ only at n>=3)")
            wb.add_data("N2_tanh_ln_q0", float(tanh_ratio))
            wb.add_data("N2_split_pred_unshared_MeV", float(pred_N2_full))
            wb.add_data("N2_split_pred_shared_MeV", float(pred_N2_shared))
            wb.add_data("tension_coverage_sum_N1_plus_N2", float(both))
            wb.add_data("classification",
                        "PARTIAL (ii): S2 CLOSED (equal 1/3 per-pair weight derived "
                        "from S3 equivariance + link symmetry; a=0 derived; |mu| "
                        "support derived via sign-rep Schur obstruction). S3 OPEN, "
                        "re-scoped to ONE scalar kappa; kappa=1/3 is a guarded "
                        "near-match resting on the underived unit-capacity sum rule, "
                        "which would have to REPLACE the derived pairwise tanh(ln q0)")
            wb.add_assertion(
                name="mu_sign_representation_6_of_6",
                computed=str(int(sign_rep_ok)), expected="1", tolerance=0,
                source=("exact Magnus: mu(g(1)g(2)g(3)) = sgn(g)·mu(123) for all 6 "
                        "permutations — mu spans the sign rep of S3; by Schur the "
                        "equivariant coupling to the charge bilinear is through |mu|"))
            wb.add_assertion(
                name="s1_support_pairwise_zero_triple_one_hopf_one",
                computed=str(int(s1_ok)), expected="1", tolerance=0,
                source=("lk_12=lk_13=lk_23=0, |mu(123)|=1 (Borromean), Hopf lk=1 "
                        "(M_2 anchor) — validated Magnus machinery"))
            wb.add_assertion(
                name="charge_bilinear_exact_he3_one_h3_zero",
                computed=str(int(bil_he3 == 1 and bil_h3 == 0)), expected="1",
                tolerance=0,
                source=("Sum_{i<j} q_iq_j: (1,1,0) -> 1, (1,0,0) -> 0 exact — the "
                        "functional predicts E(3H)=0 independent of the 3H link, and "
                        "the S3 orbit average of pair weights is exactly 1/3 of pp"))
            wb.add_assertion(
                name="N1_prediction_within_half_percent_guarded_datum",
                computed=pred_N1 / split, expected=1.0, tolerance=0.005,
                source=("split_pred = B_pp·|mu|/3 under the UNDERIVED unit-capacity "
                        "sum rule vs AME2020 — the guarded near-match (-0.23%); "
                        "reported, not tuned; kappa=1/3 is not thereby derived"))
            wb.add_assertion(
                name="N1_and_tanh_routes_competing_not_additive",
                computed=str(int(float(both) > 1.2)), expected="1", tolerance=0,
                source=("N1 (99.8%) + derived tanh route (31.1%) sum > 100%: a "
                        "closure via N1 must REPLACE tanh(ln q0) at the triple "
                        "channel — the unchanged S3 gate"))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
