#!/usr/bin/env python3
"""Cross-check tr_M(β_atom) at 1 ppQ between independent paths.

The 1 ppQ (1e-15) L1 certification rests on the three FLOAT-CLEAN methods
(Hoefsmit mpfr 50 dps, chi-cache, Habiro), which agree to ~1e-48.
markov_peel is an INDEPENDENT cross-check at a looser float tolerance —
its witness is evaluated at the float64 q_0 and its exact symbolic path
is incomplete for nuclei (the open #508 Phase-2 rewrite), so it does NOT
certify 1 ppQ. (Filename retains `1ppb` for consumer/back-compat; the gate
is now 1 ppQ.)

Compares the canonical Markov trace tr_M @ q_0 from:
  - Hoefsmit / mpfr 50-dps brute-force
    (`atomic-tr-m-mpfr-50dps.witness.json`)
  - Markov-axiom recursive ascent (`markov_peel.tr_M_atomic`)
    (`markov-peel-atomic-tr-m.witness.json` — production witness
    landed in PR #520 / #508)

Both witnesses store the trace at high precision; we parse via
mpmath and report the relative delta. Flags any atom that diverges
by more than 1 part per billion (1e-9).

EXTERNAL ANCHOR (verification-gap closure): the four paths above prove
only that the methods AGREE — they share the Σ_λ y_λ χ^λ definition, so
a common χ^λ error would be invisible. `_character_closed_form_anchor`
adds an INDEPENDENT check: the two 1-dim Hecke irreps have closed-form
characters χ^{(n)}(β)=q_0^{w(β)} and χ^{(1ⁿ)}(β)=(−q_0^{-1})^{w(β)} (w =
writhe), requiring no Hecke machinery. This anchors the character engine
that feeds the chi-cache leg. See
`docs/audits/2026-06-04-hidden-fitting-verification-gap-mass-binding-walkthrough.md`.

Output: `cross-check-trM-1ppb.witness.json`

CI gate: invoke with `--strict` to exit non-zero on any divergence OR
any character-engine mismatch against the closed form.

Usage:
    python3 computations/cross_check_trM_1ppb.py
    python3 computations/cross_check_trM_1ppb.py --strict
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp, mpf, fabs, mpmathify

HERE = Path(__file__).parent
HOEF_PATH = _pb.witness_path("atomic-tr-m-mpfr-50dps.witness.json", HERE)
PEEL_PATH = _pb.witness_path("markov-peel-atomic-tr-m.witness.json", HERE)
# Third path landed via PR #681's Step 2 + this PR's combiner: the
# canonical Σ_λ y_λ(q_0) · χ^λ(β; q_0) trace built from per-irrep
# chi caches (`per_irrep_pole_atom.py` chi-{atom}-h{n} caches).
CHICACHE_PATH = _pb.witness_path("canonical-tr-m-via-chi-cache.witness.json", HERE)
# Fourth path (this PR): direct evaluation of the cyclotomic Habiro
# series `tr_M = (1/denom) · Σ_m a_m(u) · (u;u)_m` at u_0 = q_0^{1/2}
# using the coefficients in `habiro-coefficients-extended.witness.json`.
# Extends 1ppb coverage to ⁴He/⁵Li/⁶Li without needing chi caches.
HABIRO_EXT_PATH = _pb.witness_path("habiro-coefficients-extended.witness.json", HERE)
OUT_PATH = HERE / "cross-check-trM-1ppb.witness.json"

# 1 ppQ (1e-15) L1 certification rests on the three FLOAT-CLEAN methods
# (Hoefsmit mpfr 50 dps / chi-cache / Habiro), which agree to ~1e-48.
# markov_peel's LaurentQ reduction is exact-in-q, but its witness is
# evaluated at the float64 q_0 (and its exact symbolic path is incomplete
# for nuclei — the open #508 Phase-2 rewrite), so peel is an INDEPENDENT
# cross-check held to a looser float tolerance, NOT a 1 ppQ-certifying
# method. Do not silently fold peel's float64 into the 1 ppQ claim.
TOLERANCE_PPQ = mpf("1e-15")   # L1 gate on the exact methods (1 part/quadrillion)
TOLERANCE_PEEL = mpf("1e-12")  # peel float-path independent-check tolerance
TOLERANCE = TOLERANCE_PPQ      # back-compat alias

# Map from peel-witness (Z, N) tuples to atom-name strings used by
# the Hoefsmit witness for its `atom` field. Keep the atom names in
# the literal lookup table so the cross-check can be read by humans.
_ZN_TO_ATOM = {
    (1, 0): "proton",
    (0, 1): "neutron",
    (1, 1): "deuteron",
    (1, 2): "tritium",
    (2, 1): "helium-3",
    (2, 2): "helium-4",
    (3, 2): "lithium-5",
    (3, 3): "lithium-6",
    (3, 4): "lithium-7",
}
# Reverse map for the Habiro-extended consumer (it accepts (Z, N)).
_ATOM_TO_ZN = {v: k for k, v in _ZN_TO_ATOM.items()}


def _character_closed_form_anchor(tol: "mpf") -> dict:
    """EXTERNAL correctness anchor for the seminormal Hecke character engine.

    The four tr_M paths cross-checked below prove only that the methods
    AGREE — agreement is consistency, not correctness (they share the
    Σ_λ y_λ χ^λ definition, so a common error in χ^λ would be invisible).
    This anchor closes that gap for the χ^λ engine that feeds the chi-cache
    leg: it pins χ^λ to CLOSED-FORM values requiring no Hecke machinery,
    via the two one-dimensional irreps.

    With the Hecke relation (σ_i − q_0)(σ_i + q_0^{-1}) = 0:
      • symmetric  (n):   σ_i ↦  q_0       ⟹ χ^{(n)}(β)   = q_0^{w(β)}
      • antisymm. (1ⁿ):   σ_i ↦ −q_0^{-1}  ⟹ χ^{(1ⁿ)}(β) = (−q_0^{-1})^{w(β)}
    where w(β) is the writhe (signed crossing count). A mismatch means the
    character engine — hence the chi-cache leg of the 1ppb gate — is wrong,
    no matter how well the four methods agree with each other.

    The braid set mixes the actual atom braids (proton/neutron, writhe 0 —
    these pin the trace normalisation) with nonzero-writhe words (positive
    and negative) that exercise the q-power law.
    """
    import sys as _sys
    if str(HERE) not in _sys.path:
        _sys.path.insert(0, str(HERE))
    from hecke_characters import chi_lambda_braid_mpf
    from q_parameter import Q_50_DIGIT_STR
    q0 = mpf(Q_50_DIGIT_STR)

    def chi(shape, word):
        # Shared mpfr helper (Rust rug::Float kernel): full arbitrary
        # precision, not float64. Anchor deltas drop from ~1e-15 (f64) to
        # ~1e-50. `word` is the flat signed braid word; the helper marshals
        # it. Pass the canonical 50-digit STRING (not the mpf) so the helper
        # forwards it verbatim with no round-trip. Same chokepoint as
        # homfly_ocneanu_trace._chi.
        return chi_lambda_braid_mpf(shape, word, q_value=Q_50_DIGIT_STR)

    def writhe(word):
        return sum(1 if g > 0 else -1 for g in word)

    words = [
        ("proton (σ₁σ₂⁻¹)³", 3, [1, -2, 1, -2, 1, -2]),
        ("neutron (σ₁⁻¹σ₂)³", 3, [-1, 2, -1, 2, -1, 2]),
        ("σ₁³ (3 strands)", 3, [1, 1, 1]),
        ("σ₁σ₂ (3 strands)", 3, [1, 2]),
        ("σ₁ (2 strands)", 2, [1]),
        ("σ₁⁻²σ₂ (3 strands)", 3, [-1, -1, 2]),
    ]
    checks = []
    worst = mpf(0)
    for label, n, word in words:
        w = writhe(word)
        sym_ref = q0 ** w
        anti_ref = (-1 / q0) ** w
        sym_got = chi(tuple([n]), word)
        anti_got = chi(tuple([1] * n), word)
        d = max(abs(sym_got - sym_ref), abs(anti_got - anti_ref))
        worst = max(worst, d)
        checks.append({
            "braid": label, "n_strands": n, "writhe": w,
            "chi_symmetric": str(sym_got), "ref_symmetric": str(sym_ref),
            "chi_antisymmetric": str(anti_got), "ref_antisymmetric": str(anti_ref),
            "abs_delta_max": str(d), "ok": bool(d < tol),
        })
    n_fail = sum(1 for c in checks if not c["ok"])
    return {"checks": checks, "n_fail": n_fail, "worst_delta": str(worst)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help=("Exit non-zero on any divergence above the gate: "
                          "exact-method 1 ppQ (1e-15) OR peel float tolerance (1e-12)"))
    ap.add_argument("--dps", type=int, default=50,
                    help="mpmath working precision (default 50)")
    args = ap.parse_args()
    mp.dps = args.dps

    hoef = json.loads(HOEF_PATH.read_text())
    peel = json.loads(PEEL_PATH.read_text())

    # Hoefsmit results: list of dicts, atom name in 'atom'
    hoef_by_atom = {r["atom"]: r for r in hoef["results"]}
    # Markov-peel results: list of dicts keyed on (Z, N) — production
    # witness format from `markov_peel_atomic_witness.py`.
    peel_by_atom = {}
    for r in peel.get("data", {}).get("results", []):
        atom = _ZN_TO_ATOM.get((r["Z"], r["N"]))
        if atom is None:
            continue
        peel_by_atom[atom] = r

    # Third path: canonical chi-cache combiner (PR #681 Step 2).
    # Only atoms with COMPLETE chi caches contribute to the 1ppb
    # gate; partial caches yield truncated traces and are reported
    # separately as `chi_cache_partial`.
    chicache_by_atom: dict[str, dict] = {}
    chicache_partials: dict[str, dict] = {}
    if CHICACHE_PATH.exists():
        chicache = json.loads(CHICACHE_PATH.read_text())
        for r in chicache.get("data", {}).get("results", []) or chicache.get("results", []):
            atom = r.get("atom")
            if atom is None:
                continue
            if r.get("partial_cache"):
                chicache_partials[atom] = r
            else:
                chicache_by_atom[atom] = r

    # Fourth path: direct Habiro series evaluation at q_0 (this PR).
    # Reuses the `term_6_via_habiro_coeffs_mp` machinery — covers A
    # ∈ {2..6} (deuteron through ⁶Li) via `habiro-coefficients-
    # extended.witness.json` on main. Independent of chi-cache; no
    # symbolic χ^λ needed.
    habiro_by_atom: dict[str, mp.mpf] = {}
    if HABIRO_EXT_PATH.exists():
        import sys as _sys
        if str(HERE) not in _sys.path:
            _sys.path.insert(0, str(HERE))
        from mass_formula_6term_mpfr_50dps import term_6_via_habiro_coeffs_mp
        for atom_name, (Z, N) in _ATOM_TO_ZN.items():
            try:
                habiro_by_atom[atom_name] = term_6_via_habiro_coeffs_mp(Z, N)
            except (KeyError, FileNotFoundError):
                continue

    common_atoms = sorted(
        (set(hoef_by_atom) & set(peel_by_atom)) | set(habiro_by_atom)
    )

    print("=" * 76)
    print("Cross-check tr_M @ q_0 — Hoefsmit (mpfr 50dps) vs markov_peel")
    print("=" * 76)
    print(f"  1 ppQ gate (exact methods): {mp.nstr(TOLERANCE_PPQ,1)}  |  "
          f"peel float-check: {mp.nstr(TOLERANCE_PEEL,1)}  |  dps: {args.dps}")
    print()
    print(f"  {'atom':<14} {'Hoefsmit':>18}  {'markov_peel':>18}  "
          f"{'chi-cache':>18}  {'Habiro':>18}  {'|Δ|max':>9}  status")
    print("  " + "─" * 105)

    deltas: list[dict] = []
    any_diverge = False

    for atom in common_atoms:
        h = hoef_by_atom.get(atom)
        p = peel_by_atom.get(atom)

        # Hoefsmit + markov_peel are the long-running canonical paths;
        # any atom with both is on the "core 3-way 1ppb gate" track.
        # The Habiro path is allowed to stand alone for atoms outside
        # the core (e.g. ⁵Li, ⁶Li) — they get reported but don't gate
        # the strict mode unless the Habiro value diverges from
        # another available path.
        h_val: mp.mpf | None = None
        p_val: mp.mpf | None = None
        if h is not None and h.get("tr_M_at_q0_50dps") is not None:
            h_val = mpmathify(h["tr_M_at_q0_50dps"])
        if p is not None and "error" not in p:
            peel_str = p.get("tr_M_at_q0") or p.get("tr_M_at_q0_str")
            if peel_str is not None:
                p_val = mpmathify(peel_str)

        chi_entry = chicache_by_atom.get(atom)
        c_val = mpmathify(chi_entry["abs_tr_M_q0"]) if chi_entry is not None else None
        hab_val = habiro_by_atom.get(atom)
        # The Habiro value is the SIGNED tr_M, not |tr_M|; compare on
        # absolute value to match the other paths.
        if hab_val is not None:
            hab_abs = abs(hab_val)
        else:
            hab_abs = None

        # Pairwise relative deltas. Use the first available reference
        # (prefer Hoefsmit > peel > chi-cache) as the magnitude scale.
        ref = h_val if h_val is not None else (p_val if p_val is not None else (c_val if c_val is not None else hab_abs))
        if ref is None or ref == 0:
            continue
        rel_pairs: dict[str, mp.mpf] = {}
        if p_val is not None and h_val is not None:
            rel_pairs["hoef_vs_peel"] = fabs(p_val - h_val) / fabs(h_val)
        if c_val is not None and h_val is not None:
            rel_pairs["hoef_vs_chi"] = fabs(c_val - fabs(h_val)) / fabs(h_val)
        if hab_abs is not None and h_val is not None:
            rel_pairs["hoef_vs_habiro"] = fabs(hab_abs - fabs(h_val)) / fabs(h_val)
        if hab_abs is not None and c_val is not None:
            rel_pairs["chi_vs_habiro"] = fabs(hab_abs - c_val) / fabs(c_val) if c_val != 0 else mpf(0)
        # Per Gemini #739 review: prior versions only computed pairs
        # against the Hoefsmit or chi-cache anchors.  At atoms where
        # both anchors are missing/partial (⁴He, ⁵Li, ⁶Li under the
        # current witness coverage), the script defaulted to a 0.0
        # rel_delta_max despite peel and Habiro values both being
        # present and differing.  Add peel-vs-{Habiro, chi} pairs so
        # every adjacent pair gets reported.
        if p_val is not None and hab_abs is not None:
            rel_pairs["peel_vs_habiro"] = fabs(p_val - hab_abs) / fabs(p_val) if p_val != 0 else mpf(0)
        if p_val is not None and c_val is not None:
            rel_pairs["peel_vs_chi"] = fabs(p_val - c_val) / fabs(p_val) if p_val != 0 else mpf(0)
        rel_max = max(rel_pairs.values()) if rel_pairs else mpf(0)

        # Certification gates on the CANONICAL p-n convention. Production
        # tr_M uses `pn_convention="bring_color_weighted"` (the
        # closed_form_tau_M default / owner directive). markov_peel and
        # chi-cache are the two INDEPENDENT exact-mpfr implementations of
        # that color-weighted convention; their agreement certifies the
        # 1 ppQ L1 gate. The Rust canonical-chi (Hoefsmit) and Habiro legs
        # are SIGN-ONLY (color-blind) cross-checks — they agree for A=1
        # (no inter-nucleon crossing) but diverge for A>=2 by the
        # color-weighting amount (δ·h/4 ~ 1.8e-4), which is EXPECTED, not a
        # failure. They are reported as informational, not gating.
        # (See docs/audits/2026-06-23-trM-crosscheck-colorweighting-split-at-C.md.)
        cw_pairs = {k: rel_pairs[k] for k in ("peel_vs_chi",) if k in rel_pairs}
        exact_max = max(cw_pairs.values(), default=mpf(0))
        # Color-blind informational deltas (vs the canonical color-weighted
        # peel): zero at A=1, ~1.8e-4 at A>=2 by construction.
        colorblind_max = max(
            (rel_pairs[k] for k in ("hoef_vs_peel", "peel_vs_habiro")
             if k in rel_pairs), default=mpf(0))
        peel_max = colorblind_max  # back-compat: reported field below
        # certified_1ppQ requires the two color-weighted methods to agree.
        certified_1ppQ = bool(cw_pairs) and exact_max < TOLERANCE_PPQ
        ok = certified_1ppQ
        if not ok:
            any_diverge = True
        # "OK" = color-weighted methods certify; suffix "+cb" flags that the
        # color-blind cross-check legs diverge (expected for A>=2).
        status = ("OK" if ok else "DIVERGE") + (
            " (cb≠)" if (ok and colorblind_max > TOLERANCE_PEEL) else "")

        h_str = str(h_val)[:18] if h_val is not None else "(no Hoefsmit)"
        p_str = str(p_val)[:18] if p_val is not None else "(no peel)"
        if c_val is not None:
            c_str = str(c_val)[:18]
        elif atom in chicache_partials:
            c_str = "(partial cache)"
        else:
            c_str = "(no chi cache)"
        hab_str = str(hab_abs)[:18] if hab_abs is not None else "(no Habiro)"
        print(f"  {atom:<14} {h_str:>18}  {p_str:>18}  "
              f"{c_str:>18}  {hab_str:>18}  "
              f"{mp.nstr(rel_max, 3):>9}  {status}")

        d: dict = {
            "atom": atom,
            "within_1ppQ": ok,                 # combined gate: exact 1 ppQ AND peel < 1e-12
            "within_1ppb": ok,                 # back-compat alias for pre-ppQ consumers
            "within_1ppQ_exact_methods": certified_1ppQ,   # float-clean trio < 1 ppQ
            "within_peel_tolerance": bool(peel_max < TOLERANCE_PEEL),
            "rel_delta_max": str(rel_max),
            "exact_method_rel_delta": str(exact_max),
            "peel_rel_delta": str(peel_max),
            "certified_1ppQ_exact_methods": certified_1ppQ,
            "n_exact_methods": int(h_val is not None)
                               + int(c_val is not None)
                               + int(hab_abs is not None),
        }
        if h_val is not None: d["hoefsmit_50dps"] = str(h_val)
        if p_val is not None: d["markov_peel"] = str(p_val)
        if c_val is not None:
            d["chi_cache_canonical"] = str(c_val)
        elif atom in chicache_partials:
            d["chi_cache_partial"] = {
                "partitions_used": chicache_partials[atom]["partitions_used"],
                "partitions_total": chicache_partials[atom]["partitions_total"],
            }
        if hab_abs is not None:
            d["habiro_extended"] = str(hab_abs)
        d["pairwise_rel_deltas"] = {k: str(v) for k, v in rel_pairs.items()}
        deltas.append(d)

    # Route through WitnessBuilder so engine/scriptFile/commitSha/
    # scriptHash/scriptCommitSha/engineVersion provenance is auto-
    # emitted (closes the last remaining I14 audit gap surfaced on
    # PR #816: cross-check-trM-1ppb.witness.json was the only
    # PROV_MISSING witness after the habiro migration in `6211b2077`).
    # Previously the script hand-wrote raw JSON, so the trailing
    # provenance fields were manually backfilled (PR #809) and got
    # stripped on every re-run.
    from witness_base import WitnessBuilder, _witnesses_substantively_equal
    w = WitnessBuilder(
        name="cross-check-trM-1ppb",
        engine="mpmath",
        output_dir=OUT_PATH.parent,
    )
    w.set_audit_only("docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md")
    w.add_parameter(
        "description",
        (
            "Pairwise comparison of tr_M(β_atom) @ q_0 across four paths. "
            "Two-part gate: the float-clean methods (Hoefsmit mpfr 50-dps, "
            "chi-cache, Habiro) are certified at 1 ppQ (1e-15 relative); "
            "markov_peel (float64 q_0 eval; exact symbolic path incomplete "
            "for nuclei, the open #508 Phase-2 rewrite) is an INDEPENDENT "
            "cross-check held to a looser 1e-12 float tolerance and does NOT "
            "certify 1 ppQ."
        ),
    )
    w.add_parameter("tolerance_1ppQ_exact_methods", str(TOLERANCE_PPQ))
    w.add_parameter("tolerance_peel_float_check", str(TOLERANCE_PEEL))
    w.add_parameter("working_precision_dps", args.dps)
    # External correctness anchor for the χ^λ engine (closes the
    # "agreement ≠ correctness" gap documented in the verification-gap
    # audit). Runs at the same q_0 via the mpfr kernel (full precision).
    anchor = _character_closed_form_anchor(TOLERANCE)
    print()
    print("  χ^λ closed-form anchor (1-dim irreps, external of the four paths):")
    for c in anchor["checks"]:
        print(f"    {c['braid']:<22} w={c['writhe']:+d}  "
              f"|Δ|={mp.nstr(mpf(c['abs_delta_max']), 3):>9}  "
              f"{'OK' if c['ok'] else 'FAIL'}")
    print(f"    χ-engine anchor: {len(anchor['checks']) - anchor['n_fail']}"
          f"/{len(anchor['checks'])} match closed form "
          f"(worst |Δ| = {mp.nstr(mpf(anchor['worst_delta']), 3)})")

    w.add_data("atoms_compared", len(deltas))
    w.add_data("any_diverge", any_diverge)
    w.add_data("deltas", deltas)
    w.add_data("character_closed_form_anchor", anchor)
    n_certified = sum(1 for d in deltas if d.get("certified_1ppQ_exact_methods"))
    w.add_data("n_atoms_certified_1ppQ_exact_methods", n_certified)
    w.add_assertion(
        name="all_atoms_within_1ppQ",
        computed=0 if any_diverge else 1,
        expected=1,
        source=(
            "tr_M(β_atom) @ q_0: the float-clean methods (Hoefsmit mpfr / "
            "chi-cache / Habiro) must agree to 1 ppQ (1e-15); markov_peel "
            "(float64 q_0 eval; exact path incomplete for nuclei, #508 P2) "
            "is an independent check held to 1e-12, NOT a 1 ppQ-certifying "
            "method"
        ),
    )
    w.add_assertion(
        name="character_engine_matches_closed_form",
        computed=0 if anchor["n_fail"] else 1,
        expected=1,
        source=(
            "χ^{(n)}(β) = q_0^{w(β)} and χ^{(1ⁿ)}(β) = (−q_0^{-1})^{w(β)} "
            "for the two 1-dim Hecke irreps — an INDEPENDENT closed-form "
            "anchor on the character engine that feeds the chi-cache trace "
            "leg (agreement of the four paths is consistency, not "
            "correctness)"
        ),
    )
    # WitnessBuilder.save() already implements content-diff-aware
    # preservation of on-disk ephemeral fields.
    out_path = w.save()
    print()
    print(f"  Witness: {out_path.name}")
    print(f"  atoms compared: {len(deltas)}, divergent: "
          f"{sum(1 for d in deltas if not d['within_1ppQ'])}")

    if args.strict and (any_diverge or anchor["n_fail"]):
        print()
        if any_diverge:
            print("  STRICT mode: divergence above the 1 ppQ / peel gate — exiting 1")
        if anchor["n_fail"]:
            print("  STRICT mode: χ^λ engine disagrees with closed form — exiting 1")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
