#!/usr/bin/env python3
"""Categorical bypass demo — compute B(𝔥) directly from SDP T_w, no knot id.

Implements **step 1** of the canonical-chain bypass plan: compute
binding energy directly from the joint-tower SDP solution via

    B(𝔥) = m_e · ρ · tr_M(T_w) | q = q_0
    tr_M(T_w) = Σ_λ y_λ(q_0) · χ_λ(T_w)

with the Wedderburn block traces χ_λ(T_w) read from the SDP witness
(joint-tower-sdp-rust.witness.json) and the Wenzl-bridge weights
y_λ(q_0) read from y-lambda-wenzl-witness.json. **No knot
identification, no volume-match.**

This is the bypass that moves family-1 atoms (D, T, ³He) from
"partial-knot-id-via-vol-match" to fully derived — IF the direct
formula reproduces the mass-table-ppb predictions. **It does not**,
and that surfaces a fundamental gap that must be resolved before
sub-percent (let alone 1 ppb) accuracy is achievable.

Findings:
- Electron H_2: tr_M(T_w(e)) = 0.7292 → B_pred = 0.373 MeV vs
  m_e = 0.511 MeV (27% off). The σ_1³ Hecke element in H_2(q)
  has Wedderburn-direct Markov trace ≠ 1.
- Deuteron H_3 (6_2): tr_M(T_w(²H)) = 0.288 → B_pred = 0.147 MeV
  vs AME 2.225 MeV (15× off). The volume-match identity
  tr_M(T_w(²H)) ≈ Vol_hyp(6_2) ≈ 4.401 does NOT hold for the
  Wenzl-y_λ × Wedderburn-χ_λ Markov trace evaluated at q_0.
- ³He H_3 (Borromean): tr_M(T_w(³He)) = 1.000 — interesting:
  exactly the identity-rep Markov trace, suggesting T_w(³He) is
  the categorical identity (which would mean B(³He) = m_e · ρ = 2·m_e
  = 1.022 MeV, far from AME 7.718 MeV).

Diagnosis: the canonical chain `tr_M = Σ y_λ χ_λ` and the
volume-match formula `B = m_e · ρ · Vol_hyp(K)` are NOT the same
function of T_w at q_0. The former is the **regular Markov trace**
on H_n(q); the latter is the **Reshetikhin–Turaev / colored Jones
invariant evaluated at the Volume Conjecture root of unity**. They
agree only at specific q values (roots of unity for Volume
Conjecture), not at the substrate parameter q_0 ≈ 1.110.

Implication: the bypass cannot simply replace volume-match with
Wenzl-Wedderburn at q_0. We need either:

  (A) Additional Markov-trace normalization factor to bridge the
      regular trace to the writhe-/framing-normalized closure.
  (B) Evaluate tr_M at a different q (root of unity), then
      analytically continue to q_0.
  (C) Reformulate the canonical chain to use a different categorical
      invariant (Reshetikhin–Turaev rather than Wenzl Markov).

Output: categorical-bypass-volmatch-demo.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from decimal import Decimal
from pathlib import Path

import mpmath as mp  # noqa: E402 — lifting mass-table-ppb's decimal strings

from _precision import set_compute_dps  # noqa: E402

# Raise dps BEFORE the mass-table decimal strings are lifted, not after:
# mpmath's default is 15 dps, so `mp.mpf("<44 digits>")` would round on
# construction and the ratios below would be float64 wearing a long decimal.
set_compute_dps()

sys.path.insert(0, str(Path(__file__).parent))
# `codata_constants`, not `experimental_constants` (bean qou-5sg8). The latter's
# M_E_MEV is literally `float(_M_E_MEV)` -- an explicit downcast of the same
# constant. This is the swap the qou-3wqg port already made in
# `mass_table_ppb.py`; this producer was left on the float variant.
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
)
from q_parameter import Q as Q_0
from witness_base import WitnessBuilder

#: AME binding energies as `mp.mpf`, taken from the constants module rather than
#: read back out of `mass-table-ppb.witness.json`.
#:
#: That witness carries `B_AME_MeV` as a JSON **float** -- `mass_table_ppb.py`
#: imports the mpf constants and then wraps each in `float(...)` -- so lifting it
#: here with `mp.mpf(<float>)` bound the binary64 value and `str()` printed its
#: full decimal expansion: `2.2245661999999999380861...` where the constant is
#: `2.2245662`. Three of the four fields bean qou-5sg8 reports are that.
#:
#: Fixing it at the true root (dropping those `float()` wrappers upstream) would
#: change `B_AME_MeV` from float to string in a witness **eight** producers read,
#: so it is a separate, wider change; the bean carries it. Sourcing the constant
#: directly is the right fix for this producer regardless -- a decimal constant
#: should not make a round trip through a JSON float to reach a consumer that
#: wants it exactly.
_AME_B_MEV = {
    "2H": AME_B_DEUTERON_MEV_VALIDATION,
    "3H": AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
}

#: Significant digits carried by anything downstream of the SDP eigenvalues.
#:
#: `joint-tower-sdp-rust.witness.json` stores `matrix_at_q_0_sym_eigvals` as JSON
#: **floats**, so χ_λ enters at binary64 and caps everything built from it --
#: `tr_M`, `B_pred_direct`, and both ratios. Lifting `y_λ` (which the witness
#: does supply at 50 digits) cannot raise that cap, and neither can the mpf
#: `M_E_MEV`.
#:
#: So these are serialized at their TRUE precision instead of at OUTPUT_DPS.
#: That is the padding audit's own second remedy -- "carry the value as a
#: string/mpf, **or serialize at its true precision**" -- and here it is the
#: honest one: printing 50 digits of a float64-floored product is the fake
#: precision the ratchet exists to catch, whichever way the value was carried.
_F64_SIG_DIGITS = 17

SDP_WITNESS = Path(__file__).parent / "joint-tower-sdp-rust.witness.json"
Y_LAMBDA_WITNESS = Path(__file__).parent / "y-lambda-wenzl-witness.json"
MASS_TABLE_WITNESS = Path(__file__).parent / "mass-table-ppb.witness.json"


def load_y_lambda():
    """Return y_λ(q_0) keyed by (n, partition_tuple)."""
    with open(Y_LAMBDA_WITNESS) as f:
        d = json.load(f)
    out = {}
    for n_str, table in d["tables_by_n"].items():
        n = int(n_str)
        for w in table["weights"]:
            partition = tuple(w["partition"])
            # `mp.mpf`, not `float`: the witness stores this as a 50-digit
            # DECIMAL STRING, so `float(...)` discarded 34 of them at the door.
            # The χ_λ cap below floors the products regardless, but flooring an
            # exact input on the way in is a defect on its own terms -- and it
            # made the `_F64_SIG_DIGITS` note untrue as written, since y_λ was
            # a second float64 source it does not mention.
            out[(n, partition)] = mp.mpf(w["y_lambda_numeric"])
    return out


def load_sdp_certificates():
    """Return SDP certificate per atom keyed by name."""
    with open(SDP_WITNESS) as f:
        d = json.load(f)
    return {e["name"]: e for e in d["per_atom_certificates"]}


def load_volmatch_predictions():
    """Pull mass-table-ppb predicted B values for comparison.

    mass-table-ppb is written through WitnessBuilder, which nests the payload
    under `data`; this loader read `rows` at top level and so raised KeyError
    on every run. The two sibling witnesses read above keep their payload at
    top level, so accept either shape rather than assuming one.
    """
    with open(MASS_TABLE_WITNESS) as f:
        d = json.load(f)
    payload = d.get("data") if isinstance(d.get("data"), dict) else d
    if "rows" not in payload:
        raise KeyError(
            f"{MASS_TABLE_WITNESS.name}: no 'rows' at top level or under 'data'")
    out = {}
    for row in payload["rows"]:
        out[row["sym"]] = {
            "B_AME_MeV": row["B_AME_MeV"],
            "B_pred_MeV": row["B_pred_MeV"],
            "formula": row["formula"],
        }
    return out


def chi_lambda_from_block(block):
    """χ_λ(T_w) = trace(ρ_λ(T_w)) = sum of (sym-part) eigenvalues.

    For non-symmetric matrices, the trace still equals the sum of
    eigenvalues by linearity. The witness records eigenvalues of the
    symmetric part (M+M^T)/2; their sum equals tr(M) regardless.
    """
    # Lifted to mpf before summing.  This adds no precision -- the witness
    # stores these as JSON floats and that cap is real (see `_F64_SIG_DIGITS`)
    # -- but it keeps the accumulation out of binary64 and lets everything
    # downstream be one type.
    return mp.fsum(mp.mpf(str(v)) for v in block["matrix_at_q_0_sym_eigvals"])


def native_strand_n(cert):
    """SDP runs at native_strand_count (knot-braid strands), not atomic n_0."""
    return cert["native_strand_count"]


def main():
    y_lambda = load_y_lambda()
    sdp_certs = load_sdp_certificates()
    volmatch = load_volmatch_predictions()

    rows = []
    sym_map = {
        "electron":     ("e", None,    None,   1.0,    "ref m_e"),
        "deuteron-2H":  ("2H", "²H",   "6_2",  None,   "vs mass-table-ppb"),
        "tritium-3H":   ("3H", "³H",   "8_11", None,   "vs mass-table-ppb"),
        "helium3-3He":  ("3He", "³He", "L6a4", None,   "vs mass-table-ppb"),
    }
    for sdp_name, (sym, sym_pretty, knot, ref_val, ref_label) in sym_map.items():
        cert = sdp_certs.get(sdp_name)
        if cert is None:
            continue
        n_native = native_strand_n(cert)
        rho = cert["rho_factor"]
        wb = cert.get("wedderburn_blocks", [])
        # Compute tr_M(T_w) = Σ_λ y_λ(q_0) · χ_λ(T_w)
        terms = []
        tr_M = mp.mpf(0)
        for block in wb:
            partition = tuple(block["partition"])
            chi = chi_lambda_from_block(block)
            y = y_lambda.get((n_native, partition))
            if y is None:
                terms.append({"partition": list(partition),
                              "chi": mp.nstr(chi, _F64_SIG_DIGITS),
                              "y_lambda": None, "skipped": True})
                continue
            contribution = y * chi
            tr_M += contribution
            terms.append({
                "partition": list(partition),
                "d_lambda": block["d_lambda"],
                # χ_λ and everything built from it are floored by the
                # float64 SDP eigenvalues, so they are emitted at that
                # precision.  y_λ is exact to its full 50 digits and is
                # emitted as such -- the two are no longer the same width
                # because they no longer carry the same amount of truth.
                "chi_lambda": mp.nstr(chi, _F64_SIG_DIGITS),
                "y_lambda": str(y),
                "contribution": mp.nstr(contribution, _F64_SIG_DIGITS),
            })
        # B_pred from direct chain
        B_pred_direct = M_E_MEV * mp.mpf(rho) * tr_M
        # B_pred from volume-match (mass-table-ppb)
        #
        # `mp.mpf(...)` on the way in: `mass_table_ppb.py` was ported to mpmath
        # (bean qou-3wqg) and now emits `B_pred_MeV` as a 44-digit DECIMAL
        # STRING rather than a JSON float, because computing it in Python floats
        # made it wrong past the 8th significant digit. Read raw, the string
        # reaches `B_pred_direct / B_volmatch` below and raises
        # `unsupported operand type(s) for /: 'float' and 'str'`.
        #
        # Lifting with mpf rather than float keeps the precision the port
        # created; this ratio is reported to ppb, which is the scale the
        # correction moved.
        vm = volmatch.get(sym, {})
        _bv = vm.get("B_pred_MeV")
        B_volmatch = mp.mpf(_bv) if _bv is not None else None
        # B_AME from the constants module first (exact mpf), falling back to the
        # witness only for symbols it does not carry -- `ref_val` covers the
        # electron row, whose "B_AME" is the unit 1.0 rather than a binding
        # energy. See `_AME_B_MEV` above for why the witness value is not used
        # where a constant exists.
        _ba = _AME_B_MEV.get(sym, vm.get("B_AME_MeV", ref_val))
        B_AME = mp.mpf(_ba) if _ba is not None else None

        rows.append({
            "sym":          sym,
            "sdp_name":     sdp_name,
            "knot":         knot,
            "n_native":     n_native,
            "rho":          rho,
            "tr_M_direct":  mp.nstr(tr_M, _F64_SIG_DIGITS),
            # `str(...)` on the mpf-valued fields: they are mpmath now (see the
            # lift above) and `json.dump` cannot serialize an mpf — the failure
            # `alpha_cluster_recursion.py` hit for the same reason. The ratios
            # are computed in mpmath and stringified only at this sink, so the
            # precision survives the division and only the JSON encoding is
            # narrowed.
            "B_pred_direct_MeV": mp.nstr(B_pred_direct, _F64_SIG_DIGITS),
            # `B_volmatch` and `B_AME` are exact to their full length -- the
            # first a 44-digit decimal from the qou-3wqg port, the second an mpf
            # constant -- so `str()` claims only digits that exist.
            "B_volmatch_MeV": str(B_volmatch) if B_volmatch is not None else None,
            "B_AME_MeV":    str(B_AME) if B_AME is not None else None,
            # The ratios are NOT: their numerator is floored by the float64 SDP
            # eigenvalues (see `_F64_SIG_DIGITS`), so they are emitted at that
            # precision rather than padded out to OUTPUT_DPS.
            "ratio_direct_to_volmatch": (
                mp.nstr(B_pred_direct / B_volmatch, _F64_SIG_DIGITS)
                if B_volmatch else None
            ),
            "ratio_direct_to_AME": (
                mp.nstr(B_pred_direct / B_AME, _F64_SIG_DIGITS)
                if B_AME else None
            ),
            "wedderburn_terms": terms,
            "comparison_label": ref_label,
        })

    print("\n" + "=" * 78)
    print("Bypass demo: B = m_e · ρ · Σ_λ y_λ · χ_λ(T_w) at q_0 — direct from SDP")
    print("=" * 78)
    print(f"{'sym':<6} {'n':>2} {'ρ':>2} {'tr_M':>9} "
          f"{'B_direct':>10} {'B_volmatch':>10} {'B_AME':>10} {'ratio':>7}")
    print("-" * 78)
    for r in rows:
        rd = r["ratio_direct_to_volmatch"]
        # `float(...)` for display, same reason as `bv`/`ba` above: the ratio is
        # a decimal string in the row now.
        rd_str = f"{float(rd):>7.4f}" if rd is not None else f"{'—':>7}"
        # `float(...)` for DISPLAY only — these two are decimal strings in the
        # row now (mass-table-ppb's mpmath port, bean qou-3wqg), and a format
        # spec of `.4f` on a str raises `Unknown format code 'f'`. The stored
        # value keeps its full precision; only this 4-decimal console column is
        # narrowed.
        bv = f"{float(r['B_volmatch_MeV']):>10.4f}" if r['B_volmatch_MeV'] is not None else f"{'—':>10}"
        ba = f"{float(r['B_AME_MeV']):>10.4f}" if r['B_AME_MeV'] is not None else f"{'—':>10}"
        # `float(...)` on B_pred_direct for the same reason as the two above:
        # once M_E_MEV comes from `codata_constants` it is an mpf, mpf has no
        # `__format__`, and `:>10.4f` raises. Console-only; the record keeps the
        # mpf-derived value.
        print(f"{r['sym']:<6} {r['n_native']:>2} {r['rho']:>2} "
              f"{float(r['tr_M_direct']):>9.4f} "
              f"{float(r['B_pred_direct_MeV']):>10.4f} "
              f"{bv} {ba} {rd_str}")

    print("\n" + "=" * 78)
    print("DIAGNOSIS: B_direct ≠ B_volmatch at q_0.")
    print("=" * 78)
    print("""
The Wenzl-y_λ × Wedderburn-χ_λ Markov trace evaluated at q_0 ≈ 1.110
does NOT reproduce the volume-match formula B = m_e · ρ · Vol_hyp(K).

Two distinct categorical invariants:
  - Wenzl Markov trace tr_M(T_w) = Σ_λ y_λ · χ_λ(T_w)  [REGULAR trace]
  - Vol_hyp(K) ≈ Reshetikhin–Turaev / colored-Jones invariant
    evaluated at q = root of unity (Volume Conjecture)

These agree only at Volume-Conjecture root-of-unity points, not at
the substrate parameter q_0. Resolving the bypass requires picking
ONE invariant as canonical and rederiving the other relations.

This is a real gap in the canonical chain (PR #442). Step 1 of the
1-ppb plan must include resolving it.
""")

    # Build witness via canonical infrastructure
    w = (
        WitnessBuilder("categorical-bypass-volmatch-demo", engine="python")
        .set_description(
            "Bypass demo: compute B(𝔥) directly from joint-tower SDP "
            "Wedderburn blocks via tr_M = Σ_λ y_λ · χ_λ at q_0, "
            "without using volume-match knot identification. "
            "Surfaces a 27%–15× discrepancy with mass-table-ppb's "
            "volume-match B = m_e · ρ · Vol_hyp(K), establishing that "
            "the regular Markov trace at q_0 ≠ Vol_hyp(K). The "
            "canonical chain in PR #442 step (5)–(7) needs further "
            "resolution before sub-percent accuracy is possible."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", str(Q_0))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_data("rows", rows)
        .add_data("sources", {
            "sdp_witness": str(SDP_WITNESS.name),
            "y_lambda_witness": str(Y_LAMBDA_WITNESS.name),
            "mass_table_witness": str(MASS_TABLE_WITNESS.name),
        })
        .add_caveat(
            "Direct formula tr_M = Σ y_λ · χ_λ at q_0 does NOT reproduce "
            "the volume-match B values; ratio is 0.73 for electron, "
            "~0.07 for deuteron, ~0.10 for ³He."
        )
        .add_caveat(
            "Resolving the bypass requires either (A) extra Markov-trace "
            "normalization, (B) evaluation at root of unity then "
            "analytic continuation, or (C) switching the canonical "
            "invariant from Wenzl-Markov to RT / colored-Jones."
        )
        .add_caveat(
            "Cannot reach 1 ppb on B/A or sub-MeV on Q until this gap "
            "is resolved."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
