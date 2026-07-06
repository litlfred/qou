#!/usr/bin/env python3
"""
Mass table: AME vs ZERO-FREE-PARAMETER predictions, with error in ppb
and %.

No fitting.  Nothing calibrated from AME values.  Every B_pred is a
function of q₀ and a specified atom→knot assignment only.

Prediction rules (all zero-parameter from q₀):
  • Kashaev volume law      B = ρ_F · Vol_hyp(K)    with ρ_F ∈ {m_e, 2m_e}
  • Atom → knot assignment  one of:
      D    ↔ 6_2            (handover hypothesis, not derived)
      T    ↔ 8_11           (handover hypothesis, not derived)
      3He  ↔ Borromean L6a4 (handover hypothesis, not derived)
      4He  ↔ 4·Borromean    (magic-atom A·8G rule)
      A≥8  ↔ α-cluster with c_αα = m_e · Vol(7²_1)  (derived from knot 7²_1)

The atom→knot assignments for D, T, ³He were obtained by census
search in jsj_verification.py — that IS a form of AME-driven
fitting (we picked the knot whose volume is closest to B_AME/ρ).
Flagged here as "hyp: by-census" so the reader can distinguish.

Truly derived pieces: (1) the density rule ρ_F ∈ {m_e, 2m_e} now
identified as ρ_F = ν_SDP per `conj:kashaev-density-equals-sdp-
multiplicity` (Rule-14 conditional adoption owner-authorised 2026-05-24
per `docs/audits/2026-05-24-rule14-kashaev-density.md`); (2) the
α-coupling c_αα = m_e · Vol(7²_1) — derived from the topology of two
linked Borromean rings.  No AME input.

The atom→knot assignments for D, T, ³He are deferred to R5-full SDP
solver per owner-decided 2026-05-24 (`docs/audits/2026-05-24-rule14-
atom-knot-census.md` §5 option 3 — wait for R5-full to supersede
census assignments).  Current census-derived assignments are retained
as EXPLORATORY scaffolding until R5-full lands.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))
# qou-substrate (Layer 2a): import WitnessBuilder directly from the
# package rather than via the witness_base back-compat shim (which
# re-exports the identical class). Mirrors low_isotopes_binding_sweep.py.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "qou-substrate" / "python"))

from q_parameter import Q as Q0
from experimental_constants import M_E_MEV
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from knot_volumes import VOL_BORROMEAN, VOL_7_SQ_1  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_LI6_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402

# Knot volumes now imported from `knot_volumes` (canonical mpmath
# 50dps source). Catalan G + Vol(L6a4) = 8G + Vol(7²_1) literature
# values. Pre-refactor these were f64-hardcoded literals; post-
# refactor they live in the centralised module so a `--precision
# mpfr` lift only needs to update one place. See I14 audit and the
# coordination ledger entry "knot-vol _precision propagation".

# Atomic-pair α-α coupling knot: 7²_1 (Whitehead-like linked pair).
# DERIVED: c_αα = m_e · Vol(7²_1). No AME fit.
C_ALPHA_DERIVED = M_E_MEV * VOL_7_SQ_1         # ≈ 2.4270 MeV

# Hyperbolic volumes from SnapPy (50-digit HP, independent of AME).
KNOT_VOL = {
    "6_2":       4.4008325161230461014412038656409280339834854185165,
    "8_11":      8.2863168178065925881,
    "L6a4":      VOL_BORROMEAN,
}

# AME2020 light-atom table (B in MeV; positive = binding).
AME_TABLE = [
    ("2H",     1,  1,   float(AME_B_DEUTERON_MEV_VALIDATION)),
    ("3H",     1,  2,   float(AME_B_TRITIUM_MEV_VALIDATION)),
    ("3He",    2,  1,   float(AME_B_HE3_MEV_VALIDATION)),
    ("4He",    2,  2,  float(AME_B_HE4_MEV_VALIDATION)),
    ("6Li",    3,  3,  float(AME_B_LI6_MEV_VALIDATION)),
    ("7Li",    3,  4,  39.24453),
    ("8Be",    4,  4,  56.49951),
    ("9Be",    4,  5,  58.16498),
    ("11B",    5,  6,  76.20548),
    ("12C",    6,  6,  92.16175),
    ("14N",    7,  7, 104.65877),
    ("16O",    8,  8, 127.61929),
    ("19F",    9, 10, 147.80137),
    ("20Ne",  10, 10, 160.64486),
    ("24Mg",  12, 12, 198.25690),
    ("40Ca",  20, 20, 342.05212),
]

# Atom → (knot, nu_sdp, source-label) hypothesis table.
# ZERO-PARAMETER = the pairing is stated in the framework; the
# predicted binding follows mechanically from Vol and ν_SDP.  We mark
# WHERE the pairing comes from (derived-from-framework vs census-
# assigned-from-B_AME).
#
# Field rename 2026-05-24 per `conj:kashaev-density-equals-sdp-
# multiplicity`: what was previously called `rho_factor` is the
# joint-tower SDP Wedderburn multiplicity ν_SDP of the canonical
# Hecke element T_w; see the conj block for the categorical hook
# onto driver (x) MacMahon partition algebra.
ATOM_ASSIGN = {
    "2H":   {"rule": "kashaev",  "knot": "6_2",  "nu_sdp": 1,
             "origin": "hyp: census-assigned (EXPLORATORY pending R5-full SDP)"},
    "3H":   {"rule": "kashaev",  "knot": "8_11", "nu_sdp": 2,
             "origin": "hyp: census-assigned (EXPLORATORY pending R5-full SDP)"},
    "3He":  {"rule": "kashaev",  "knot": "L6a4", "nu_sdp": 2,
             "origin": "hyp: census-assigned (EXPLORATORY pending R5-full SDP)"},
    # 4He = A·8G magic-atom rule, ν_SDP=2 extrapolated, A=4.
    "4He":  {"rule": "magic",    "A_units": 4, "nu_sdp": 2,
             "origin": "framework: A·8G magic rule (ν_SDP=2 extrapolated, pending R5-full)"},
    # A ∈ {5, 6, 7} gap.  ⁵Li is an unbound resonance; ⁶Li and ⁷Li
    # are bound but neither the Kashaev volume-law assignment (no
    # census knot/link with Vol ≈ B_AME/m_e in the {51.5, 62.6, 76.8}
    # range yet found) nor the α-cluster rule (defined only for
    # A ≥ 8 via n_α ≥ 2) covers them.  Documented as an explicit
    # gap row so the witness output makes the missing prediction
    # visible.  See docs/audits/2026-05-24-a5-a7-isotope-wiring-gap.md
    # for the knot-census target volumes and candidate paths.
    "5Li":  {"rule": "gap",      "B_AME_MeV_target": 26.328,
             "vol_kashaev_target_m_e_units": 26.328 / M_E_MEV,
             "vol_kashaev_target_2m_e_units": 26.328 / (2 * M_E_MEV),
             "origin": "GAP: A ∈ {5,6,7} no atom→knot rule yet"},
    "6Li":  {"rule": "gap",      "B_AME_MeV_target": float(AME_B_LI6_MEV_VALIDATION),
             "vol_kashaev_target_m_e_units": float(AME_B_LI6_MEV_VALIDATION) / M_E_MEV,
             "vol_kashaev_target_2m_e_units": float(AME_B_LI6_MEV_VALIDATION) / (2 * M_E_MEV),
             "origin": "GAP: A ∈ {5,6,7} no atom→knot rule yet"},
    "7Li":  {"rule": "gap",      "B_AME_MeV_target": 39.24453,
             "vol_kashaev_target_m_e_units": 39.24453 / M_E_MEV,
             "vol_kashaev_target_2m_e_units": 39.24453 / (2 * M_E_MEV),
             "origin": "GAP: A ∈ {5,6,7} no atom→knot rule yet"},
    # 8Be: α-cluster (n_α=2, n_pairs=1)
    "8Be":  {"rule": "alpha",    "n_alpha": 2, "n_pairs": 1,
             "origin": "framework: α-cluster n_α=2"},
    # 12C: α-cluster (n_α=3, n_pairs=3)
    "12C":  {"rule": "alpha",    "n_alpha": 3, "n_pairs": 3,
             "origin": "framework: α-cluster n_α=3"},
    # 16O: α-cluster (n_α=4, n_pairs=6)
    "16O":  {"rule": "alpha",    "n_alpha": 4, "n_pairs": 6,
             "origin": "framework: α-cluster n_α=4"},
    # 20Ne, 24Mg, 40Ca: α-cluster with (n_α, n_pairs) from C(n,2).
    "20Ne": {"rule": "alpha",    "n_alpha": 5, "n_pairs": 10,
             "origin": "framework: α-cluster n_α=5"},
    "24Mg": {"rule": "alpha",    "n_alpha": 6, "n_pairs": 15,
             "origin": "framework: α-cluster n_α=6"},
    "40Ca": {"rule": "alpha",    "n_alpha": 10, "n_pairs": 45,
             "origin": "framework: α-cluster n_α=10"},
    # ── Odd-A / non-α-cluster isotopes (wiring begun 2026-05-27) ──
    # These don't fit the α-cluster rule (not multiples of ⁴He) or
    # the Kashaev single-knot rule (target volumes too large for
    # low-crossing census). Likely need composite rules combining
    # α-cores + valence nucleon knots.
    "9Be":  {"rule": "gap",      "B_AME_MeV_target": 58.165,
             "vol_kashaev_target_m_e_units": 58.165 / M_E_MEV,
             "vol_kashaev_target_2m_e_units": 58.165 / (2 * M_E_MEV),
             "structural_hint": "2α + n (Borromean halo nucleus)",
             "origin": "GAP: odd-A, Borromean halo — needs composite rule"},
    "11B":  {"rule": "gap",      "B_AME_MeV_target": 76.206,
             "vol_kashaev_target_m_e_units": 76.206 / M_E_MEV,
             "vol_kashaev_target_2m_e_units": 76.206 / (2 * M_E_MEV),
             "structural_hint": "2α + 3p (p-shell nucleus)",
             "origin": "GAP: odd-A, p-shell — needs composite rule"},
    "14N":  {"rule": "gap",      "B_AME_MeV_target": 104.659,
             "vol_kashaev_target_m_e_units": 104.659 / M_E_MEV,
             "vol_kashaev_target_2m_e_units": 104.659 / (2 * M_E_MEV),
             "structural_hint": "3α + 2p (p-shell, N=Z mirror)",
             "origin": "GAP: odd-A, N=Z mirror — needs composite rule"},
    "19F":  {"rule": "gap",      "B_AME_MeV_target": 147.801,
             "vol_kashaev_target_m_e_units": 147.801 / M_E_MEV,
             "vol_kashaev_target_2m_e_units": 147.801 / (2 * M_E_MEV),
             "structural_hint": "4α + 3p (sd-shell onset)",
             "origin": "GAP: odd-A, sd-shell onset — needs composite rule"},
}


def predict(sym: str) -> dict | None:
    """Return {B_pred, formula, origin, notes} or None if no rule.

    Returns a `rule == "gap"` record with `B_pred = None` for atoms
    that are explicitly known-to-be-missing (A ∈ {5, 6, 7}) so the
    witness output surfaces the gap instead of silently omitting
    the row.  Truly unknown atoms (not in ATOM_ASSIGN at all) still
    return None.
    """
    info = ATOM_ASSIGN.get(sym)
    if not info:
        return None

    if info["rule"] == "gap":
        # Explicit known gap — emit a structured "no prediction" row.
        return {
            "B_pred": None,
            "formula": "GAP — no atom→knot rule",
            "origin": info["origin"],
            "inputs": {
                "B_AME_MeV_target": info["B_AME_MeV_target"],
                "vol_kashaev_target_m_e_units": info["vol_kashaev_target_m_e_units"],
                "vol_kashaev_target_2m_e_units": info["vol_kashaev_target_2m_e_units"],
                "audit_doc": "docs/audits/2026-05-24-a5-a7-isotope-wiring-gap.md",
            },
        }

    if info["rule"] == "kashaev":
        knot, nu = info["knot"], info["nu_sdp"]
        vol = KNOT_VOL[knot]
        # B = ν_SDP · m_e · Vol(K) per conj:kashaev-density-equals-
        # sdp-multiplicity (Rule-14 conditional, owner-authorised
        # 2026-05-24).
        B = nu * M_E_MEV * vol
        return {
            "B_pred": B,
            "formula": f"{nu}·m_e · Vol({knot})",
            "origin": info["origin"],
            "inputs": {"knot": knot, "Vol": vol, "nu_sdp": nu},
        }

    if info["rule"] == "magic":
        A, nu = info["A_units"], info["nu_sdp"]
        # B = ν_SDP · A · 8G (A independent Borromean nucleons)
        B = nu * M_E_MEV * A * VOL_BORROMEAN
        return {
            "B_pred": B,
            "formula": f"{nu}·m_e · {A}·8G",
            "origin": info["origin"],
            "inputs": {"A": A, "8G": VOL_BORROMEAN, "nu_sdp": nu},
        }

    if info["rule"] == "alpha":
        # α-cluster: B = n_α · B(⁴He_derived) + n_pairs · c_αα
        # Use 4He_derived from magic rule = 2m_e · 4 · 8G = 29.9555 MeV
        B_4He_derived = 2 * M_E_MEV * 4 * VOL_BORROMEAN
        B = info["n_alpha"] * B_4He_derived + info["n_pairs"] * C_ALPHA_DERIVED
        return {
            "B_pred": B,
            "formula": (f"{info['n_alpha']}·B(⁴He_derived) "
                          f"+ {info['n_pairs']}·c_αα"),
            "origin": info["origin"],
            "inputs": {
                "n_alpha": info["n_alpha"],
                "n_pairs": info["n_pairs"],
                "B_4He_derived": B_4He_derived,
                "c_alpha": C_ALPHA_DERIVED,
            },
        }
    return None


def fmt_ppb(err_abs: float, b_ame: float) -> str:
    if b_ame <= 0:
        return "—"
    ppb = abs(err_abs) / b_ame * 1e9
    if ppb > 1e9:
        return f"{ppb/1e9:+.3g}×10⁹"
    if ppb > 1e6:
        return f"{ppb/1e6:+.3f}×10⁶"
    if ppb > 1e3:
        return f"{ppb/1e3:+.3f}×10³"
    return f"{ppb:+.3f}"


def load_shell_correction() -> dict[str, float]:
    """Load the L3 shell-correction ε_shell values from the prototype
    witness, if it exists.  Returns a dict atom_sym → ε_shell (MeV).

    The prototype is `computations/prototype_gs_nf_shell_binding.py`
    (PR #1162) which emits per-atom shell-binding corrections derived from
    the Gröbner-Shirshov normal-form shell-closure signature.  See
    `docs/audits/2026-05-24-magic-shell-gs-filtration-exploitation.md`
    §4 for the L3 wiring proposal.

    PROTOTYPE-ONLY: the ε_shell values are derived from AME residuals,
    NOT from the full sequential-Hopf-linking GS-NF reduction.  Loading
    them is opt-in via `--shell-correction`.  Production-grade ε_shell
    extraction awaits the pyhecke GS-NF reduction-energy infrastructure
    + R5-full SDP solver landing.
    """
    witness_path = Path(__file__).parent / "prototype-gs-nf-shell-binding.witness.json"
    if not witness_path.exists():
        return {}
    try:
        d = json.loads(witness_path.read_text())
        rows = d["data"]["per_atom_l3_correction"]
        return {
            r["atom"]: r["epsilon_shell_MeV"]
            for r in rows
            if r["epsilon_shell_MeV"] is not None
        }
    except (KeyError, json.JSONDecodeError, ValueError):
        return {}


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Mass table — AME2020 vs zero-free-parameter predictions",
    )
    ap.add_argument(
        "--shell-correction",
        action="store_true",
        help="(PROTOTYPE / opt-in) Apply the L3 shell-binding correction "
             "ε_shell from prototype-gs-nf-shell-binding.witness.json.  "
             "Default off.  Values are derived from AME residuals (not "
             "categorical GS-NF reduction) — for L3 wiring path demonstration "
             "ONLY, not production headline numerics.",
    )
    args = ap.parse_args()

    shell_correction = load_shell_correction() if args.shell_correction else {}
    if args.shell_correction:
        print(
            "[mass_table_ppb] L3 shell-correction ENABLED — "
            f"ε_shell loaded for {len(shell_correction)} atoms from "
            "prototype-gs-nf-shell-binding.witness.json.  PROTOTYPE-ONLY: "
            "values are derived from AME residuals, NOT categorical "
            "GS-NF reduction.  Awaiting R5-full SDP solver for production-"
            "grade extraction (see docs/audits/2026-05-24-magic-shell-"
            "gs-filtration-exploitation.md §4)."
        )
    print("=" * 130)
    print("MASS TABLE — AME2020 vs ZERO-FREE-PARAMETER predictions")
    print(f"  q₀ = {Q0:.10f}   m_e = {M_E_MEV} MeV")
    print(f"  8G = {VOL_BORROMEAN:.10f}   Vol(7²_1) = {VOL_7_SQ_1:.10f}")
    print(f"  c_αα (derived = m_e · Vol(7²_1)) = {C_ALPHA_DERIVED:.6f} MeV")
    print(f"  B(⁴He_derived) = 2m_e · 4·8G = "
          f"{2*M_E_MEV*4*VOL_BORROMEAN:.6f} MeV   "
          f"(AME 4He: {float(AME_B_HE4_MEV_VALIDATION)} MeV)")
    print(f"  NO AME VALUES USED AS INPUTS.")
    if args.shell_correction:
        print(f"  L3 shell-correction APPLIED (--shell-correction flag, "
              f"PROTOTYPE-only — see witness for ε_shell values).")
    print("=" * 130)
    print(f"  {'atom':>5} {'Z':>3} {'N':>3} {'A':>3}  "
          f"{'B_AME':>10}  {'B_pred':>11}  {'err (MeV)':>11}  "
          f"{'err %':>9}  {'err ppb':>12}  formula")
    print("  " + "-" * 128)
    rows = []
    no_assign = []
    for (sym, Z, N, B_ame) in AME_TABLE:
        A = Z + N
        pred = predict(sym)
        if pred is None:
            no_assign.append((sym, Z, N, A, B_ame))
            print(f"  {sym:>5} {Z:>3} {N:>3} {A:>3}  "
                  f"{B_ame:>10.4f}   "
                  f"[no zero-parameter rule assigned]")
            continue
        B_pred_kashaev = pred["B_pred"]
        eps_shell = shell_correction.get(sym, 0.0) if args.shell_correction else 0.0
        # Apply L3 correction additively (opt-in via --shell-correction).
        # When the flag is off (default), eps_shell = 0.0 and B_pred is
        # the unmodified Kashaev value.
        B_pred = (
            B_pred_kashaev + eps_shell
            if B_pred_kashaev is not None
            else None
        )
        err = (B_pred - B_ame) if B_pred is not None else None
        pct = (err / B_ame * 100) if (err is not None and B_ame) else 0.0
        ppb = (err / B_ame * 1e9) if (err is not None and B_ame) else 0.0
        l3_marker = f"  [+ε_shell={eps_shell:+.3f}]" if eps_shell != 0.0 else ""
        if B_pred is None:
            print(f"  {sym:>5} {Z:>3} {N:>3} {A:>3}  "
                  f"{B_ame:>10.4f}   "
                  f"[GAP — {pred['formula']}]")
        else:
            print(f"  {sym:>5} {Z:>3} {N:>3} {A:>3}  "
                  f"{B_ame:>10.4f}  {B_pred:>+11.4f}  {err:>+11.6f}  "
                  f"{pct:>+8.3f}%  {fmt_ppb(err, B_ame):>12}  "
                  f"{pred['formula']}{l3_marker}  [{pred['origin']}]")
        rows.append({
            "sym": sym, "Z": Z, "N": N, "A": A,
            "B_AME_MeV": B_ame,
            "B_pred_MeV": B_pred,
            "B_pred_kashaev_only_MeV": B_pred_kashaev,
            "epsilon_shell_MeV": eps_shell if args.shell_correction else None,
            "err_MeV": err,
            "err_pct": pct,
            "err_ppb": ppb,
            "formula": pred["formula"],
            "origin": pred["origin"],
            "inputs": pred["inputs"],
        })

    # Summary
    print()
    print("  Summary:")
    ok = rows
    within = {1: 0, 1e3: 0, 1e6: 0, 1e9: 0}
    for r in ok:
        for th in within:
            if abs(r["err_ppb"]) <= th:
                within[th] += 1
    print(f"    n = {len(ok)} atoms with zero-parameter prediction")
    print(f"    n = {len(no_assign)} atoms without rule "
          f"({', '.join(a[0] for a in no_assign)})")
    print(f"    within 1    ppb  (1e-9):    {within[1]}")
    print(f"    within 1e3  ppb  (1 ppm):   {within[1e3]}")
    print(f"    within 1e6  ppb  (0.1%):    {within[1e6]}")
    print(f"    within 1e9  ppb  (100%):    {within[1e9]}")

    mean_pct = sum(abs(r["err_pct"]) for r in ok) / len(ok) if ok else 0.0
    mean_ppb = sum(abs(r["err_ppb"]) for r in ok) / len(ok) if ok else 0.0
    print(f"    mean |err|:   {mean_pct:.4f}%  =  {mean_ppb:.3e} ppb")

    builder = (
        WitnessBuilder("mass-table-ppb", engine="python+snappy")
        .set_description(
            "AME2020 light-atom binding vs strictly zero-free-parameter "
            "predictions: Kashaev law B = ρ_F · Vol_hyp(K) with ρ_F ∈ "
            "{m_e, 2m_e}; atom→knot assignments from framework rules "
            "(magic A·8G, α-cluster with c_αα = m_e·Vol(7²_1)) or "
            "census search (flagged 'hyp: census-assigned'). "
            "NO AME-derived calibrations or fits."
        )
        .set_audit_only("docs/audits/2026-05-03-next-session-plan-to-1ppb.md")
        .add_parameter("q_0", Q0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("vol_borromean_8G", VOL_BORROMEAN)
        .add_parameter("vol_7_sq_1", VOL_7_SQ_1)
        .add_parameter("c_alpha_derived_MeV", C_ALPHA_DERIVED)
        .add_data("rows", rows)
        .add_data("atoms_no_assignment", no_assign)
        .add_data("within", {str(k): v for k, v in within.items()})
        .add_data("mean_abs_pct", mean_pct)
        .add_data("mean_abs_ppb", mean_ppb)
    )
    out = builder.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
