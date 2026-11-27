#!/usr/bin/env python3
"""
mirror_split_milnor_one_third_probe.py — is the ³H–³He mirror-split factor
split/B_pp ≈ 1/3 DERIVABLE ("one active pair among three Borromean components"),
or a datum? Parameter-free test of the candidate mechanism named by the redirect
audit (docs/audits/2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md).

FORMALIZE-FIRST decomposition (compute-author §3.3) — the mechanism split = B_pp/3
factors into three steps; each is checked against the proved/structural corpus:

  S1 (PROVED, exact).  ³He's link is L6a4 = Borromean: every pairwise linking
      number vanishes and the triple Milnor invariant μ̄(123) = ±1. Recomputed
      here exactly (integer Magnus expansion, the validated machinery of
      computations/binding_mn_milnor_linking.py). Consequence: a pairwise
      linking-mediated EM coupling is STRUCTURALLY ZERO; any linking route to
      the Coulomb split goes through the triple channel.

  S2 (STRUCTURAL, conditional).  The Borromean link is S₃-symmetric under
      component permutation (longitudes ℓᵢ = [x_{i+1}, x_{i+2}] cyclic + the
      standard full symmetry of L6a4), so any component-permutation-equivariant
      weight on its 3 components/pairs is EQUAL = 1/3 each. NOTE this is a
      symmetry of the LINK; it is NOT supplied by the equal-weight coordination
      result (bond-extensivity-equal-weight.witness.json), which shows the
      opposite at the nucleon level: the derived bond energies have a 1.78×
      spread (ε_nn/ε_pp), equal weight FAILS there, and in the exact
      equal-weight limit the mirror split is ZERO (both mirror nuclei get
      3·⟨ε⟩). Recomputed here. So S2 can only be sourced from the S₃ link
      symmetry, and only applies to a functional defined on the LINK
      components, not to the charge-labelled strong bonds.

  S3 (UNPROVED — the gate).  split = B_pp/3 additionally needs the EM-active
      energy per pair-channel to equal the FULL strong per-block bond B_pp
      (unit Coulomb/strong coefficient). The only DERIVED Coulomb/strong ratio
      in the corpus is tanh(ln q₀) ≈ 0.10396 (def:coulomb-charge,
      charge_coulomb_tn3he_derived.py), i.e. 0.104·B_pp = 31.1% of the split —
      NOT 1/3. The two derived/near-match pieces are COMPETING, not additive:
      tanh route 31.1%, 1/3 route 99.8%; both together would give 130.9%.
      No corpus derivation fixes the triple-channel Coulomb/strong coefficient
      at 1 (or replaces the q₀ evaluation); until it exists, 1/3 is a DATUM.

NUMEROLOGY-GUARD datum (reported, not identified): tanh(ln q) = 1/3 exactly at
q = √2 — the derived Coulomb/strong FORM evaluated at q = √2 instead of q₀
reproduces the 1/3, and √2 = 1/x* where x* = 1/√2 is the deuteron Borel-
singularity coupling of target 2 (same redirect audit). A two-coincidence
pattern is still a coincidence pattern; no derivation connects the substrate
evaluation point to √2.

VERDICT (anti-fit discipline, scope-(a)): DATUM ONLY. The 1/3 multiplicity has
a candidate structural origin (S1 + S2: triple-channel-only coupling on an
S₃-symmetric link, one EM-active pair among three), but mechanism step S3 —
a derived unit Coulomb/strong coefficient at the triple channel — is missing
AND in tension with the derived tanh(ln q₀). "split = B_pp/3, alone, is not
derived as-is"; it constrains the missing EM-linking magnitude, it does not
close it. No fit; no wiring; no tier change.

Inputs (all with provenance, nothing hardcoded):
  • B_pp — recomputed from the canonical per-block route: E₀·(tr_M-weighted
    Σ_λ y_λ|Re χ^λ| over the H₆ diproton braid, free minus interacting), the
    exact code path of computations/charge_coulomb_tn3he_derived.py
    (witness charge-coulomb-tn3he-derived.witness.json: 2.28609 MeV).
  • split — AME2020 via codata_constants._ame_binding_mev(1,3) − (2,3).
  • q₀ — Q_50_DIGIT_STR (string, never float-rounded).
mpmath at the production floor (set_compute_dps(), 50 dps).

Audit: docs/audits/2026-07-13-mirror-split-one-third-mechanism-probe.md
EXPLORATORY — audit-only witness; no production wiring.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_COMP, _COMP / "substrate", _COMP / "hecke", _COMP / "habiro"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV, _ame_binding_mev  # noqa: E402
# S1: the validated exact Milnor/Magnus machinery (import, do not re-derive)
from binding_mn_milnor_linking import mu, BORROMEAN  # noqa: E402
from bond_extensivity_equal_weight import f_bonds  # noqa: E402 — convention-D closed forms
# B_pp provenance: the canonical per-block H₆ route of the derived-Coulomb probe
from habiro_coefficients_interpolate import (  # noqa: E402
    chi_lambda_numerical, atomic_braid_to_crossings,
)
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from schur_weyl_symbolic import partitions_of  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
q0 = Q_MP
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))      # 𝔈₀ ≈ 4.186 MeV


def per_block(Z: int, N: int, inter: bool) -> mp.mpf:
    """Σ_λ y_λ |Re χ^λ| over the 2-nucleon braid at H₆ — the exact B_pp code
    path of charge_coulomb_tn3he_derived.py (canonical per-block provenance)."""
    ydict = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
             for k, v in y_lambda_at(6, q0).items()}
    cr = atomic_braid_to_crossings(Z, N, include_inter=inter)
    tot = mp.mpf(0)
    for lam in partitions_of(6):
        chi, d = chi_lambda_numerical(lam, q0, cr)
        if d == 0:
            continue
        y = ydict.get(tuple(lam))
        if y is not None:
            tot += y * abs(mp.re(chi))
    return tot


def eps_bonds():
    """#2089 fibre-derived per-bond energies ε = log(1/f_bond) (E₀=1 units) —
    the bond_extensivity_equal_weight.py closed forms, for the S2 check.

    The factors are now IMPORTED from that module rather than re-spelled here.
    This block held a stale hand-copy: it carried the convention-C EXPANSION

        f_pp = sqrt(q)/(q+1)                                      = z_C
        f_nn = (q^1.5 - q^3 - q^2 + q + 1)/(q(q+1))               = z_C - h
        f_pn = (q^1.5 - (q+1)(q^2-1)/2)/(q(q+1))                  = z_C - h/2

    while the module it names had migrated to convention D — its own comment
    says these lines "previously carried the C-substituted EXPANSION of exactly
    that, which is where the q^{3/2} came from".  The structural kernel
    {z, z-h, z-h/2} was never in dispute; only which z.  Substituting z_D into
    the expansion above would NOT have been the fix (the audit's second tier
    flags exactly that: a half-integer power of q surviving in a migrated
    file), because under D every factor is rational — D never leaves Q(q).
    Importing removes the expansion and the copy at once, so this cannot drift
    a third time.  Same pin on both sides: q0 = mpf(Q_50_DIGIT_STR) here and in
    the source module, so no layer is straddled.
    """
    return {k: mp.log(1 / v) for k, v in f_bonds().items()}


def main() -> int:
    print("=== mirror-split 1/3: derivation chain or datum? (formalize-first) ===\n")

    # ── S1: exact Milnor structure of the Borromean A=3 link ─────────────────
    lk = [mu(BORROMEAN, s) for s in [(1, 2), (1, 3), (2, 3)]]
    mu123 = mu(BORROMEAN, (1, 2, 3))
    s1_ok = (lk == [0, 0, 0] and abs(mu123) == 1)
    print(f"S1 Borromean (exact Magnus): pairwise lk = {lk}, μ̄(123) = {mu123}"
          f"  → pairwise EM-linking channel structurally ZERO "
          f"[{'PASS' if s1_ok else 'FAIL'}]")

    # ── S2: does the equal-weight witness supply per-pair 1/3? (NO — check) ──
    eps = eps_bonds()
    spread = eps["nn"] / eps["pp"]
    # equal-weight limit: both A=3 mirrors get 3·⟨ε⟩ ⇒ split ≡ 0 there
    eqw_split = (2 * eps["pn"] + eps["nn"]) - (eps["pp"] + 2 * eps["pn"]) \
        - (eps["nn"] - eps["pp"])   # identically 0 by construction — shown explicitly
    print(f"S2 nucleon bond spread ε_nn/ε_pp = {float(spread):.4f}× (≠1: equal-weight"
          f" FAILS at nucleon level; bond-extensivity-equal-weight)")
    print("   equal-weight limit ⇒ mirror split ≡ 0 (both mirrors 3·⟨ε⟩): the")
    print("   equal-weight witness does NOT supply 'pp carries 1/3 ⇒ split=B_pp/3'.")
    print("   The only structural 1/3 source is the S₃ symmetry of the LINK itself.\n")

    # ── inputs with provenance ───────────────────────────────────────────────
    B_pp = E0 * (per_block(2, 0, False) - per_block(2, 0, True))
    split = mp.mpf(str(_ame_binding_mev(1, 3))) - mp.mpf(str(_ame_binding_mev(2, 3)))
    print(f"B_pp (per-block H₆ diproton, canonical route) = {float(B_pp):.6f} MeV")
    print(f"AME split B(³H)−B(³He)                        = {float(split):.6f} MeV")

    # ── the two candidate scales ─────────────────────────────────────────────
    r = split / B_pp
    dev_third = 3 * r - 1                       # deviation of split·3/B_pp from 1
    tanh_ratio = mp.tanh(mp.log(q0))
    cover_tanh = tanh_ratio * B_pp / split      # derived route coverage
    cover_third = (B_pp / 3) / split            # 1/3 route coverage
    print(f"\nsplit/B_pp        = {float(r):.6f}   (1/3 = 0.333333…)")
    print(f"split·3/B_pp      = {float(3 * r):.6f}   deviation from 1: "
          f"{float(dev_third) * 100:+.3f}%")
    print(f"tanh(ln q₀)       = {float(tanh_ratio):.6f}")
    print(f"coverage — derived tanh route: {float(cover_tanh) * 100:.2f}%   "
          f"1/3 route: {float(cover_third) * 100:.2f}%")
    both = cover_tanh + cover_third
    print(f"TENSION: the routes are COMPETING, not additive — together "
          f"{float(both) * 100:.1f}% (>100%); they cannot both be the full story.")

    # ── numerology-guard datum: tanh(ln √2) = 1/3 exactly ────────────────────
    tanh_sqrt2 = mp.tanh(mp.log(mp.sqrt(2)))
    id_err = abs(tanh_sqrt2 - mp.mpf(1) / 3)
    print(f"\nDatum (numerology guard): tanh(ln √2) − 1/3 = {mp.nstr(id_err, 3)}"
          f" (exact identity; √2 = 1/x*, the target-2 Borel coupling)")
    print("   → the derived Coulomb/strong FORM at q=√2 gives 1/3; no derivation")
    print("     moves the evaluation point off the substrate q₀. Datum only.\n")

    # ── classification ───────────────────────────────────────────────────────
    print("VERDICT (scope-(a), anti-fit): DATUM ONLY — mechanism step S3 missing.")
    print("  derivable pieces : S1 pairwise-zero/triple-channel (PROVED, exact);")
    print("                     S2 the 1/3 multiplicity from S₃ link symmetry")
    print("                     (structural, conditional on a link-level coupling);")
    print("  missing step S3  : a DERIVED unit Coulomb/strong coefficient at the")
    print("                     triple channel (per active pair = full B_pp). The")
    print("                     only derived ratio is tanh(ln q₀)=0.104 (31.1%),")
    print("                     which the 1/3 route would have to supersede.")
    print("  'split = B_pp/3, alone, is not derived as-is' — it measures the open")
    print("  EM-linking magnitude; a near-match is not a derivation. No wiring.")

    ok = bool(s1_ok and abs(float(dev_third)) < 0.005 and id_err < mp.mpf("1e-40"))

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("mirror-split-milnor-one-third", engine="mpmath")
            wb.set_description(
                "Formalize-first test of the candidate mechanism split=B_pp/3 for the "
                "³H–³He mirror split ('one active pair among three Borromean components'). "
                "S1 PROVED exact: Borromean pairwise lk=(0,0,0), μ̄(123)=±1 — pairwise EM-"
                "linking structurally zero, coupling must be triple-channel. S2 structural-"
                "conditional: the 1/3 multiplicity can come only from the S₃ symmetry of "
                "L6a4 itself; the equal-weight coordination witness does NOT supply it "
                "(nucleon bond spread 1.78×, and the equal-weight limit gives ZERO split). "
                "S3 UNPROVED (the gate): split=B_pp/3 needs a derived UNIT Coulomb/strong "
                "coefficient at the triple channel; the only derived ratio is tanh(ln q₀)="
                "0.10396 covering 31.1%, vs the 1/3 route's 99.77% — COMPETING, not "
                "additive (sum 130.9%). Numerology-guard datum: tanh(ln √2)=1/3 exactly "
                "(√2=1/x*, the target-2 Borel coupling) — reported, not identified. "
                "VERDICT scope-(a): DATUM ONLY, mechanism step S3 missing; no fit, no "
                "wiring, no tier change.")
            wb.set_audit_only(
                "docs/audits/2026-07-13-mirror-split-one-third-mechanism-probe.md")
            wb.add_parameter("compute_dps", mp.mp.dps)
            wb.add_parameter("q_0", Q_50_DIGIT_STR)
            wb.add_data("S1_borromean", {"pairwise_lk": lk, "mu_bar_123": mu123})
            wb.add_data("S2_equal_weight_check", {
                "eps_nn_over_eps_pp": float(spread),
                "equal_weight_limit_split_MeV": float(eqw_split),
                "note": ("equal-weight fails at nucleon level (spread ≠ 1) and its "
                         "limit gives zero split; the 1/3 source is S₃ link symmetry, "
                         "not bond-extensivity-equal-weight")})
            wb.add_data("B_pp_strong_MeV", float(B_pp))
            wb.add_data("B_pp_provenance",
                        "per-block H₆ diproton, free−interacting, the exact code path of "
                        "charge_coulomb_tn3he_derived.py "
                        "(charge-coulomb-tn3he-derived.witness.json)")
            wb.add_data("ame_split_MeV", float(split))
            wb.add_data("split_over_Bpp", float(r))
            wb.add_data("split_times_3_over_Bpp", float(3 * r))
            wb.add_data("one_third_deviation", float(dev_third))
            wb.add_data("tanh_ln_q0", float(tanh_ratio))
            wb.add_data("coverage_tanh_route", float(cover_tanh))
            wb.add_data("coverage_one_third_route", float(cover_third))
            wb.add_data("coverage_sum_if_additive", float(both))
            wb.add_data("tanh_ln_sqrt2_minus_one_third", float(id_err))
            wb.add_data("classification",
                        "DATUM ONLY (scope-(a)): S1 proved, S2 structural-conditional, "
                        "S3 (derived unit Coulomb/strong coefficient at the triple "
                        "channel) missing and in tension with derived tanh(ln q₀)")
            wb.add_assertion(
                name="s1_borromean_pairwise_zero_triple_one",
                computed=str(int(s1_ok)), expected="1", tolerance=0,
                source=("exact Magnus expansion (binding_mn_milnor_linking machinery): "
                        "lk_12=lk_13=lk_23=0, |μ̄(123)|=1 — the pairwise EM-linking "
                        "channel is structurally zero for the Borromean A=3 link"))
            wb.add_assertion(
                name="one_third_datum_within_0p3pct",
                computed=3 * r, expected=1.0, tolerance=0.005,
                source=("split·3/B_pp with B_pp recomputed per-block (H₆) and split "
                        "from AME2020 codata_constants — the guarded datum, 0.23% off"))
            wb.add_assertion(
                name="tanh_and_one_third_routes_competing_not_additive",
                computed=str(int(float(both) > 1.2)), expected="1", tolerance=0,
                source=("derived tanh(ln q₀) route covers 31.1%, 1/3 route 99.77%; "
                        "sum 130.9% > 100% ⇒ they cannot both be the full story — "
                        "the 1/3 route would have to SUPERSEDE the derived ratio"))
            wb.add_assertion(
                name="tanh_ln_sqrt2_equals_one_third_exactly",
                computed=id_err, expected=0.0, tolerance=1e-40,
                source=("numerology-guard datum: tanh(ln √2)=(2−1)/(2+1)=1/3 exact; "
                        "√2 = 1/x* (target-2 Borel coupling). Reported, not identified."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
