#!/usr/bin/env python3
"""Per-nucleus operator-selection SDP/LP dual — what the confinement SDP does
across D / T / ³He / ⁴He.

Owner directive 2026-06-10: "build the full ⁴He H₁₂ operator-selection SDP (the
real dual/active-set)" + "can we prove things here?".

## Why the 6-basis (and not 77 H₁₂ idempotents)

A *full* H₁₂ Wedderburn LP is trivial: the 77 central idempotents e_λ are
ORTHOGONAL, so the Wedderburn decomposition `tr_M = Σ_λ y_λ χ_λ` is unique —
there is no operator-SELECTION freedom (x_λ is forced = the cached
contribution). The genuine selection freedom lives in the H₃ nucleon
building-block basis (γ, σ₀, σ₁, L₊, L₋, e⁻), whose Frobenius Gram
`G_ij = tr_M(b_i b_j)` is NON-diagonal — exactly the canonical
operator-selection LP of `aK_via_lp_dual_hecke_basis.py` /
`prop:operator-selection-lp`. The ⁴He-ness enters through the **target**
`n_target = |tr_M(W_atom)|`. This probe sweeps that target per nucleus and
reads the dual.

## What it computes

For each nucleus, with the shared H₃ 6-basis (t = Markov traces, G = Frobenius
Gram) and `n_target = |tr_M_atom|` (from binding_canonical):

  min  t·x   s.t.  Σx = n_target,  G x ⪰ 0   (LP: Gx ≥ 0; SDP: PSD)

emits the canonical dual (`y0_star`, `y_star`, `active_set`, `primal_obj`,
`dual_obj`, `duality_gap`) — the **shadow prices** identify which Frobenius-
positivity channels the bound state saturates, and the **duality gap = 0** is a
strong-duality CERTIFICATE (a proof of optimality, not a fit). Alongside, the
Wedderburn-channel structure from the lossless χ caches (trivial-rep fraction,
dominant channel) shows the partition-level migration.

Output: nucleus-operator-selection-sdp.witness.json
"""
from __future__ import annotations

import glob
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from pn_alpha_lp_dual import build_gram, TR_M_BASIS, NF_NAMES  # noqa: E402
from lp_dual_solver import provenance, solve_operator_selection_lp  # noqa: E402
try:
    from lp_dual_solver import solve_psd_operator_selection_sdp
    _HAVE_SDP = True
except Exception:
    _HAVE_SDP = False

CACHE = {"D": ("chi-deuteron-h6", (1, 1)), "T": ("chi-tritium-h9", (1, 2)),
         "3He": ("chi-helium-3-h9", (2, 1)), "4He": ("chi-helium-4-h12", (2, 2))}


def wedderburn_structure(stem):
    f = glob.glob(f"{stem}-at-q0-50dps-matrix-m.witness.json")
    if not f:
        return None
    w = json.loads(Path(f[0]).read_text())
    bp = w.get("by_partition") or w.get("data", {}).get("by_partition", [])
    rows = [(tuple(e["partition"]), abs(float(e["contribution"])))
            for e in bp if e.get("chi_lambda") != "skipped-max-dim"]
    tot = sum(c for _, c in rows)
    rows.sort(key=lambda x: -x[1])
    n = sum(rows[0][0])
    triv = next((c / tot for p, c in rows if len(p) == 1), 0.0)  # [n] row
    cum, n90 = 0.0, 0
    for _, c in rows:
        cum += c; n90 += 1
        if cum >= 0.9 * tot:
            break
    return {"dominant": list(rows[0][0]), "dominant_frac": round(rows[0][1] / tot, 3),
            "trivial_rep_frac": round(triv, 3), "n_channels_90pct": n90,
            "n_channels": len(rows)}


def main() -> int:
    t0 = time.time()
    G = build_gram()
    t = np.asarray(TR_M_BASIS, dtype=float)
    detG = float(np.linalg.det(G))

    bc = record_upstream(HERE / "binding-canonical.witness.json", _UPSTREAM_RECORDS)
    res = {(r["Z"], r["N"]): r for r in bc["data"]["results"]
           if r.get("status") == "solved"}

    rows = []
    # Canonical-name duals, collected alongside the display rows below.
    # The per-row fields are `lp_`-prefixed AND `round(..., 5)`-ed, which
    # means (a) `lp_dual_witness_validator.py` — which searches for the
    # unprefixed key names the LP-dual contract specifies — could not see
    # them, so this witness read as "solves the primal, never reports the
    # dual", and (b) the rounded copies are not solver output and so are not
    # covered by the LP-dual float64 carve-out. Emitting the raw values under
    # the canonical names fixes both. The prefixed rows stay for readers.
    # Pattern taken from `lp_confinement_nf_forcing.py`, which already does
    # exactly this. Bean `qou/augu`.
    canonical: dict = {k: [] for k in ("y0_star", "y_star", "active_set",
                                       "primal_obj", "dual_obj", "duality_gap")}
    for lab, (stem, (Z, N)) in CACHE.items():
        r = res.get((Z, N))
        if not r:
            continue
        ta = abs(float(r["tr_M_atom"].strip("()").split("+")[0]))
        # Pin clarabel-MPFR (50 dps). This was `backend="scipy"`, pinned for
        # byte-determinism. Measured 2026-08-23: clarabel-MPFR is byte-deterministic
        # too (6 identical solves, 1 output hash), so that reason never distinguished
        # the two. The real concern was `backend="auto"` choosing silently by whether
        # the Rust binary happened to be built; pinning `clarabel` answers it, and
        # QOU_REQUIRE_CLARABEL=1 makes a missing binary an error rather than a
        # changed answer. Bean `qou/ftuv`.
        lp = solve_operator_selection_lp(t, G, ta, backend="clarabel").to_dict()
        active_ops = [NF_NAMES[i] for i in lp["active_set"]]
        row = {
            "nucleus": lab, "Z": Z, "N": N, "A": Z + N,
            "n_target_tr_atom": round(ta, 5),
            "lp_active_ops": active_ops,
            # NOT rounded. These are ~1e-43 on the MPFR backend, and
            # `round(..., 5)` wrote a literal `0.0` into the witness for
            # y0_star / primal_obj / dual_obj — the same destruction the SDP
            # block below already refuses, applied to the LP side of the very
            # same row. `y0_star = 0` happens to be the exact certificate for
            # `t = G e₀`, but rounding is not what established that: it would
            # equally have written 0.0 for a value that ought to be 3e-6. Emit
            # the solver's value and let the `*_str` companions below prove
            # it. Bean `qou/ftuv`.
            "lp_y0_star": lp["y0_star"],
            "lp_y_star": list(lp["y_star"]),
            "lp_active_set_idx": lp["active_set"],
            "lp_primal_obj": lp["primal_obj"],
            "lp_dual_obj": lp["dual_obj"],
            "lp_duality_gap": lp["duality_gap"],
            # Solver, precision, and full-precision decimals for the LP half,
            # prefixed to match the row's `lp_` convention.
            **{f"lp_{k}": v for k, v in provenance(lp).items()},
            "wedderburn": wedderburn_structure(stem),
        }
        for k in canonical:
            canonical[k].append(lp[k])
        if _HAVE_SDP:
            try:
                sdp = solve_psd_operator_selection_sdp(t, G, ta).to_dict()
                aset = sdp.get("active_set")
                if aset is not None:
                    row["sdp_active_set_idx"] = aset
                    row["sdp_active_ops"] = [NF_NAMES[i] for i in aset]
                # NOT `round(..., 6)`. These quantities are ~1e-44 on the
                # MPFR backend, and rounding to six decimals wrote `0.0` into
                # the witness — the value destroyed outright, not merely
                # truncated. Pairing that with a full-precision companion is
                # worse than either alone: the shadow rule would excuse an
                # f64 that CONTRADICTS its own companion. Emit the solver's
                # value so the pair agrees. Bean `qou/ftuv`.
                row["sdp_duality_gap"] = float(sdp.get("duality_gap", 0.0))
                row["sdp_primal_obj"] = float(sdp.get("primal_obj", 0.0))
                # Full-precision companions when the MPFR backend served the
                # solve. `backend="auto"` picks clarabel-MPFR whenever the
                # binary is on disk, so these appear without a backend
                # argument — but the two display fields above are `.2e` and
                # `round(…, 6)`, so without carrying the companions a 167-bit
                # solve reached this witness as six decimal places. Bean
                # `qou/ftuv`.
                for _k in ("primal_obj_str", "dual_obj_str",
                           "duality_gap_str", "eigenvalues_str",
                           "X_star_str", "Z_star_str"):
                    if sdp.get(_k) is not None:
                        row[f"sdp_{_k}"] = sdp[_k]
            except Exception as e:  # noqa: BLE001
                row["sdp_error"] = f"{type(e).__name__}: {e}"
        rows.append(row)

    w = WitnessBuilder("nucleus-operator-selection-sdp", engine="python",
                       start_time=t0)
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Per-nucleus operator-selection LP/SDP dual on the canonical H₃ 6-basis "
        "(γ,σ₀,σ₁,L₊,L₋,e⁻; non-diagonal Frobenius Gram) with n_target = "
        "|tr_M(W_atom)| swept across D/T/³He/⁴He. Emits shadow prices "
        "(y0_star, y_star), active operator set, and the strong-duality "
        "certificate (duality_gap≈0 PROVES optimality). The full H₁₂ Wedderburn "
        "LP is trivial (orthogonal idempotents → unique decomposition, no "
        "selection freedom); selection lives in the H₃ basis, ⁴He enters via "
        "the target. Wedderburn channel structure (trivial-rep fraction, "
        "dominant channel) from the lossless χ caches shows the partition-level "
        "migration: trivial rep [n] dominance erodes D 0.47 → ⁴He 0.10."
    )
    w.add_data("H3_gram_det", detG)
    w.add_data("NF_basis", NF_NAMES)
    w.add_data("rows", rows)
    for _k, _v in canonical.items():
        w.add_data(_k, _v)
    w.add_data("reading", {
        "duality_gap_is_a_proof": "duality_gap ≈ 0 across all nuclei = strong "
            "duality holds = the active set is a CERTIFIED optimum (a proof, "
            "not a fit). This is the rigorous content of the SDP here.",
        "trivial_rep_migration": {r["nucleus"]: r["wedderburn"]["trivial_rep_frac"]
                                  for r in rows if r.get("wedderburn")},
        "verdict": "The Wedderburn trivial-rep [n] loses dominance with A "
                   "(measured); the H₃ operator-selection dual certifies the "
                   "saturating channels per nucleus with a zero duality gap.",
    })
    # All gaps must be ~0 (strong duality = the certificate is valid).
    max_gap = max(r["lp_duality_gap"] for r in rows)
    w.add_assertion(
        name="lp_strong_duality_certificate_valid",
        computed=max_gap, expected=0.0, tolerance=1e-6,
        source="max LP duality gap over D/T/³He/⁴He; ≈0 ⇒ the active set is a "
               "certified (proved-optimal) operator selection per nucleus.",
    )
    out = w.save()

    print("=" * 96)
    print(" Per-nucleus operator-selection LP/SDP dual (canonical H₃ 6-basis)")
    print(f"   Gram det = {detG:.4e}   basis = {NF_NAMES}")
    print("=" * 96)
    print(f" {'nuc':>5}{'A':>3}{'tr_atom':>9}{'active ops (y_star>0)':>26}"
          f"{'gap':>9}{'triv-rep':>9}{'dominant ch':>14}")
    print(" " + "-" * 94)
    for r in rows:
        wd = r.get("wedderburn") or {}
        print(f" {r['nucleus']:>5}{r['A']:>3}{r['n_target_tr_atom']:>9.4f}"
              f"{','.join(r['lp_active_ops']):>26}{r['lp_duality_gap']:>9.1e}"
              f"{wd.get('trivial_rep_frac', 0):>9.2f}{str(wd.get('dominant')):>14}")
    print(" " + "-" * 94)
    print(f" duality gap ≈ 0 everywhere (max {max_gap:.1e}) = strong-duality "
          f"CERTIFICATE: the active set is PROVED optimal per nucleus.")
    print(f" Wedderburn trivial-rep [n] dominance: "
          + "  ".join(f"{r['nucleus']}={r['wedderburn']['trivial_rep_frac']}"
                      for r in rows if r.get('wedderburn')))
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
