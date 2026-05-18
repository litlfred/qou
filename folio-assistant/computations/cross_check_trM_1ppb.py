#!/usr/bin/env python3
"""Cross-check tr_M(β_atom) at 1ppb between two independent paths.

Compares the canonical Markov trace tr_M @ q_0 from:
  - Hoefsmit / mpfr 50-dps brute-force
    (`atomic-tr-m-mpfr-50dps.witness.json`)
  - Markov-axiom recursive ascent (`markov_peel.tr_M_atomic`)
    (`markov-peel-atomic-tr-m.witness.json` — production witness
    landed in PR #520 / #508)

Both witnesses store the trace at high precision; we parse via
mpmath and report the relative delta. Flags any atom that diverges
by more than 1 part per billion (1e-9).

Output: `cross-check-trM-1ppb.witness.json`

CI gate: invoke with `--strict` to exit non-zero on any divergence.

Usage:
    python3 folio-assistant/computations/cross_check_trM_1ppb.py
    python3 folio-assistant/computations/cross_check_trM_1ppb.py --strict
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp, mpf, fabs, mpmathify

HERE = Path(__file__).parent
HOEF_PATH = HERE / "atomic-tr-m-mpfr-50dps.witness.json"
PEEL_PATH = HERE / "markov-peel-atomic-tr-m.witness.json"
# Third path landed via PR #681's Step 2 + this PR's combiner: the
# canonical Σ_λ y_λ(q_0) · χ^λ(β; q_0) trace built from per-irrep
# chi caches (`per_irrep_pole_atom.py` chi-{atom}-h{n} caches).
CHICACHE_PATH = HERE / "canonical-tr-m-via-chi-cache.witness.json"
# Fourth path (this PR): direct evaluation of the cyclotomic Habiro
# series `tr_M = (1/denom) · Σ_m a_m(u) · (u;u)_m` at u_0 = q_0^{1/2}
# using the coefficients in `habiro-coefficients-extended.witness.json`.
# Extends 1ppb coverage to ⁴He/⁵Li/⁶Li without needing chi caches.
HABIRO_EXT_PATH = HERE / "habiro-coefficients-extended.witness.json"
OUT_PATH = HERE / "cross-check-trM-1ppb.witness.json"

TOLERANCE = mpf("1e-9")  # 1 ppb relative

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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="Exit non-zero on any > 1ppb divergence")
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
    print(f"  tolerance: {TOLERANCE} (1 ppb)  |  dps: {args.dps}")
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

        ok = rel_max < TOLERANCE
        if not ok:
            any_diverge = True
        status = "OK" if ok else "DIVERGE"

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
            "within_1ppb": ok,
            "rel_delta_max": str(rel_max),
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

    out = {
        "auditOnly": "docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md",
        "computation": "cross-check-trM-1ppb",
        "description": (
            "Pairwise comparison of tr_M(β_atom) @ q_0 between the "
            "Hoefsmit/mpfr 50-dps brute-force path and the Markov-"
            "axiom recursive ascent (markov_peel, production "
            "witness from PR #520). Tolerance is 1 ppb (1e-9 "
            "relative)."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "tolerance_relative": str(TOLERANCE),
        "working_precision_dps": args.dps,
        "atoms_compared": len(deltas),
        "any_diverge": any_diverge,
        "deltas": deltas,
    }
    # Content-diff-aware write: preserve on-disk file if the new witness
    # differs only in ephemeral meta fields (commitSha, computedAt,
    # durationMs, scriptCommitSha). See witness_base._witnesses_substantively_equal.
    from witness_base import _witnesses_substantively_equal
    new_bytes = json.dumps(out, indent=2, ensure_ascii=False)
    if OUT_PATH.exists():
        try:
            existing = json.loads(OUT_PATH.read_text())
            if not _witnesses_substantively_equal(existing, out):
                OUT_PATH.write_text(new_bytes)
        except (json.JSONDecodeError, OSError):
            OUT_PATH.write_text(new_bytes)
    else:
        OUT_PATH.write_text(new_bytes)
    print()
    print(f"  Witness: {OUT_PATH.name}")
    print(f"  atoms compared: {len(deltas)}, divergent: "
          f"{sum(1 for d in deltas if not d['within_1ppb'])}")

    if args.strict and any_diverge:
        print()
        print("  STRICT mode: divergence above 1ppb — exiting 1")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
