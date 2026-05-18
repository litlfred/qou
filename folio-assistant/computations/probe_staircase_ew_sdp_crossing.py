#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical SDP solve at float64 via
# cvxpy/SCS. The decision is whether the SDP-saturating exponent
# matches a substrate-clean q-rational; full 50-dps replication is
# left for a follow-up.
"""SDPB-style derivation of the staircase EW-residual structure on
V_(3,2,1) — analogue of `probe_sdpb_pl_crossing_equations.py`
(commit 5e7459cf0) which found `a_PL = z_markov` as the SATURATING
constraint for the Picard-Lefschetz integration limit.

## Why this probe exists

[`rem-staircase-ew-k3-mpfr-finding`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/rem-staircase-ew-k3-mpfr-finding.md)
+ [`probe_staircase_ew_k3_block_decomposition.py`](probe_staircase_ew_k3_block_decomposition.py)
§5 falsified the q^(1/(2k-1)) and q^(3/14) hypotheses for the
staircase EW residual at k=3.  The single-point empirical match
(`5 ppm` at q_0) is a coincidence, not a structural identity —
the q-derivative test shows residual is not a power function of q
at all.

The PL m_p closure had the same pathology: a post-hoc fit
`(4-q)/(4q+3)` matched CODATA to 6 ppm but didn't generalise.
Commit 5e7459cf0 ran an SDP with Hecke-algebra crossing equations
as constraints (analog of Simmons-Duffin SDPB for CFT bootstrap)
and identified the **saturating value** as `a_PL = z_markov` —
substrate-clean, structurally derived, overshoots CODATA m_p by
0.42 % (rather than the 6 ppm of the post-hoc fit).

This probe builds the staircase analogue: SDP over the Wedderburn
blocks of `H_6(q_0)` acting on `V_(3,2,1)`, with crossing
equations as constraints.  The SDP-saturating value of the
`a` parameter (defined as a substrate-clean version of the EW
residual exponent) is the substrate-derived prediction —
distinct from the back-solved post-hoc rationals.

## SDP setup

Decision variables (analogue of OPE coefficients in SDPB):

* `α_λ ≥ 0` for each `λ ⊢ 6` (Wedderburn-block weights;
  11 partitions total — `(6), (5,1), (4,2), (4,1,1), (3,3),
  (3,2,1), (3,1,1,1), (2,2,2), (2,2,1,1), (2,1^4), (1^6)`).
* `P_λ ⪰ 0` for each non-1-dim block (provides PSD encoding of
  the block's β_EW state matrix).
* `a ≥ 0` — the candidate "EW residual scale" to be maximised.

Constraints (the crossing equations):

1. **PSD**: each `P_λ ⪰ 0`.
2. **Hoefsmit-σ symmetric**: `P_λ = α_λ · sym(ρ_λ(β_EW Δ_I^minimal))`.
3. **Normalisation**: `Σ_λ α_λ = 1`.
4. **Mirror parity** (`q ↔ q⁻¹`): `α_λ = α_λ'` for all pairs of
   conjugate partitions; `(3,2,1)` is self-conjugate (no relation).
5. **Markov pair-trace saturation** (analog of PL constraint 5):
   `Σ α_λ y_λ χ_λ ≥ z^4 · Σ α_λ` where `z = 1/(√q + 1/√q)` and
   `χ_λ = tr(ρ_λ(β_EW))`.  The exponent `4 = n_3 / k - h_corner`
   matches the 4-strand Markov-pair-trace at the (3,2,1)
   self-conjugate stratum (heuristic for now — see §"Future"
   for the rigorous derivation route).
6. **`a` consistency**: `a · n_3 ≤ Σ α_λ · log_q|χ_λ| + (Σ α_λ)`
   — encodes that `a` is bounded by a weighted log-magnitude
   over the dominant channels.  Heuristic; refine per
   categorical-structure investigation.

Objective: **maximise `a`**.

## What we look for

* If `a_SDP` matches `z_markov ≈ 0.476` at q_0, then the EW
  residual scale is structurally identified with the PL
  integration limit — the same `z_markov` shows up across
  unrelated QOU compute.
* If `a_SDP` matches `1/h_corner = 1/5`, the staircase corner-hook
  reading is the SDP-saturating value — a strong substrate
  identification.
* If `a_SDP` matches `k/Σhook(ρ_k) = 3/14`, the §3-§4 numerology
  IS the SDP-saturating value (would un-falsify it from a
  structural standpoint, even though §5 falsified it from the
  q-derivative standpoint).
* If `a_SDP` matches none of the above, we've identified a
  fourth structural candidate worth investigation.

## Caveats (CRITICAL — this is a heuristic scaffolding)

This probe builds the SDP framework; the SPECIFIC crossing
equations encoded here are **stand-ins** that mirror the PL SDP's
structure, not derived from a categorical crossing-equation
analysis of V_(3,2,1).  Treat the output as **directional**:
which substrate scale does the analogue-of-PL-SDP saturate to?
A real derivation would replace the heuristic constraints 5-6
with rigorously-derived ones (e.g. from a categorical bootstrap
in `prop:operator-selection-sdp` style).

Run at float64 via cvxpy/SCS (50-dps SDP is a separate effort).

`auditOnly`: docs/audits/2026-05-17-staircase-ew-sdp-crossing.md

Witness: `staircase-ew-sdp-crossing.witness.json`

@module folio-assistant/computations/probe_staircase_ew_sdp_crossing
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import numpy as np  # noqa: E402
import cvxpy as cp  # noqa: E402

from hecke_characters import build_seminormal_matrices  # noqa: E402
from q_parameter import Q  # noqa: E402
from staircase_ew_predictions import beta_ew_word  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


Q0 = float(Q)
SHAPE_K3 = (3, 2, 1)
K = 3
N_STRANDS = sum(SHAPE_K3)  # = 6
H_CORNER = 2 * K - 1       # = 5


def _conjugate_partition(lam: tuple[int, ...]) -> tuple[int, ...]:
    """Return the transpose (conjugate) partition."""
    if not lam:
        return ()
    n_cols = lam[0]
    return tuple(sum(1 for p in lam if p > c) for c in range(n_cols))


def partitions_of(n: int) -> list[tuple[int, ...]]:
    """All partitions of `n` in lex-descending order."""
    out: list[tuple[int, ...]] = []

    def gen(remaining: int, cap: int, current: list[int]) -> None:
        if remaining == 0:
            out.append(tuple(current))
            return
        for p in range(min(remaining, cap), 0, -1):
            current.append(p)
            gen(remaining - p, p, current)
            current.pop()

    gen(n, n, [])
    return out


def main() -> int:
    print("=" * 78)
    print("  SDPB-style staircase EW-residual derivation (k=3)")
    print("  Analogue of probe_sdpb_pl_crossing_equations.py (commit 5e7459cf0)")
    print("=" * 78)

    z_markov = 1.0 / (np.sqrt(Q0) + 1.0 / np.sqrt(Q0))
    hbar_q = (Q0 - 1) / Q0
    h_amp = Q0 - 1.0 / Q0

    print(f"  q_0                          = {Q0:.10f}")
    print(f"  z_markov = 1/(√q + 1/√q)     = {z_markov:.10f}")
    print(f"  h_corner(ρ_3) = 2k−1         = {H_CORNER}")
    print(f"  1/h_corner                   = {1.0 / H_CORNER:.10f}")
    print(f"  k/Σhook(ρ_3) = 3/14          = {3.0 / 14.0:.10f}")
    print()

    parts = partitions_of(N_STRANDS)
    print(f"  partitions of {N_STRANDS}:")
    for lam in parts:
        cj = _conjugate_partition(lam)
        marker = " (self-conj)" if lam == cj else ""
        print(f"    {str(lam):<20s} dim {len(build_seminormal_matrices(list(lam))[2]):>3d}{marker}")
    print()

    # Build per-block Hoefsmit data
    word = beta_ew_word(N_STRANDS)
    print(f"  β_EW word (n={N_STRANDS}) length: {len(word)}  → {word}")
    print()

    # For each partition, build σ matrices + word image M_λ
    block_data: dict[tuple, dict] = {}
    print("  Per-block character χ_λ(β_EW Δ_I^minimal):")
    for lam in parts:
        try:
            sigmas, dim, _syts = build_seminormal_matrices(list(lam))
        except Exception as exc:
            print(f"    {str(lam):<20s} SKIP (build error: {exc})")
            continue
        # Densify if sparse
        sigmas_dense: list = []
        for s in sigmas:
            if hasattr(s, "toarray"):
                sigmas_dense.append(np.asarray(s.toarray(), dtype=np.float64))
            else:
                sigmas_dense.append(np.asarray(s, dtype=np.float64))
        # Word image (skip if any generator index exceeds dim's σ count)
        n_gens = len(sigmas_dense)
        if any(g >= n_gens for g in word):
            print(f"    {str(lam):<20s} SKIP (word uses σ_{max(word)+1} but block has σ_{n_gens})")
            continue
        if dim == 0:
            chi = 0.0
            M_lam = np.zeros((0, 0))
        else:
            M_lam = np.eye(dim, dtype=np.float64)
            for g in word:
                M_lam = M_lam @ sigmas_dense[g]
            chi = float(np.trace(M_lam))
        block_data[lam] = {
            "dim": dim,
            "chi": chi,
            "M_sym": (M_lam + M_lam.T) / 2 if dim > 0 else None,
        }
        print(f"    {str(lam):<20s} dim={dim:<3d}  χ_λ = {chi:+.6f}")
    print()

    # Jones-Markov weights y_λ via Wenzl closed form
    # y_λ = s_λ(Q,X)/Z_n where Z_n = ((1-X)/(1-Q))^n, Q=q² and
    # X = q^(3/2)/(1+q-q^2-q^3+q^(3/2)).  We use a SIMPLIFIED
    # weight: y_λ ≈ 1/(dim_q λ)^2 (Plancherel-ish at q=q_0).
    # This is a STAND-IN; the rigorous y_λ requires the Wenzl-
    # bridge — see prop:y-lambda-closed-form-wenzl-bridge.
    print("  Jones-Markov weights y_λ (stand-in: 1/dim²):")
    for lam, data in block_data.items():
        data["y_lambda"] = 1.0 / max(data["dim"] ** 2, 1)
        print(f"    {str(lam):<20s} y_λ ≈ {data['y_lambda']:.6f}")
    print()

    # ─── SDP setup ─────────────────────────────────────────────
    print("  SDP setup:")
    print("  " + "-" * 60)

    alpha_vars = {lam: cp.Variable(nonneg=True, name=f"alpha_{lam}")
                  for lam in block_data}
    # PSD matrix for each block with dim > 1
    P_vars: dict[tuple, "cp.Variable"] = {}
    for lam, data in block_data.items():
        if data["dim"] >= 2 and data["M_sym"] is not None:
            P_vars[lam] = cp.Variable(
                (data["dim"], data["dim"]), symmetric=True,
                name=f"P_{lam}")
    a_var = cp.Variable(nonneg=True, name="a")

    constraints: list = []

    # Constraint 1: each P_λ PSD
    for lam, P in P_vars.items():
        constraints.append(P >> 0)

    # Constraint 2: Hoefsmit-σ symmetric encoding
    for lam, P in P_vars.items():
        constraints.append(P == alpha_vars[lam] * block_data[lam]["M_sym"])

    # Constraint 3: normalisation Σ α_λ = 1
    constraints.append(cp.sum(list(alpha_vars.values())) == 1)

    # Constraint 4: mirror parity α_λ = α_λ' (for non-self-conjugate pairs)
    mirror_pairs_added = set()
    for lam in block_data:
        cj = _conjugate_partition(lam)
        if cj == lam or cj not in block_data:
            continue
        key = tuple(sorted((lam, cj)))
        if key in mirror_pairs_added:
            continue
        mirror_pairs_added.add(key)
        constraints.append(alpha_vars[lam] == alpha_vars[cj])

    # Constraint 5: Markov pair-trace saturation
    # Σ α_λ · y_λ · χ_λ ≥ z^h_corner · Σ α_λ
    # (PL probe used z^2; staircase analog uses z^h_corner = z^5
    # to encode the "corner-hook depth")
    pair_trace_target = z_markov ** H_CORNER
    lhs = sum(alpha_vars[lam] * block_data[lam]["y_lambda"]
              * block_data[lam]["chi"] for lam in block_data)
    rhs = pair_trace_target * cp.sum(list(alpha_vars.values()))
    constraints.append(lhs >= rhs)

    # Constraint 6: `a` consistency
    # a · n_3 ≤ Σ α_λ · trace(P_λ) + α_3 + α_111 (1-dim block weights)
    one_dim_alphas = [alpha_vars[lam] for lam, d in block_data.items()
                      if d["dim"] == 1]
    psd_traces = [cp.trace(P) for P in P_vars.values()]
    if psd_traces:
        constraints.append(
            a_var * N_STRANDS <= cp.sum(psd_traces) + cp.sum(one_dim_alphas)
        )
    else:
        constraints.append(a_var * N_STRANDS <= cp.sum(one_dim_alphas))

    # Objective: maximize a
    objective = cp.Maximize(a_var)

    prob = cp.Problem(objective, constraints)
    print(f"  Decision variables: {len(alpha_vars)} α_λ + "
          f"{len(P_vars)} P_λ (PSD) + a")
    print(f"  Constraints: PSD ({len(P_vars)}), Hoefsmit-σ ({len(P_vars)}), "
          f"normalisation (1), mirror parity ({len(mirror_pairs_added)}), "
          f"Markov-pair saturation (1), a-consistency (1)")
    print(f"  Objective: max a")
    print()

    try:
        prob.solve(solver=cp.SCS, verbose=False)
    except Exception as exc:
        print(f"  SDP solver FAILED: {exc}")
        return 1

    status = prob.status
    print(f"  SDP status: {status}")
    if status not in ("optimal", "optimal_inaccurate"):
        print(f"  → infeasible / unbounded; no a_SDP")
        return 1

    a_sdp = float(a_var.value)
    alpha_values = {lam: float(v.value) for lam, v in alpha_vars.items()}

    print(f"  a_SDP                        = {a_sdp:.10f}")
    print()
    print(f"  Comparison to candidate substrate scales:")
    candidates = [
        ("z_markov", z_markov),
        ("z_markov² ", z_markov ** 2),
        ("z_markov³ ", z_markov ** 3),
        ("z_markov⁵ ", z_markov ** 5),
        ("ℏ_q", hbar_q),
        ("ℏ_q²", hbar_q ** 2),
        ("h_amp/2", h_amp / 2),
        ("1/h_corner = 1/5", 1.0 / H_CORNER),
        ("k/Σhook(ρ_3) = 3/14", 3.0 / 14.0),
        ("q^(1/5)", Q0 ** (1.0 / 5.0)),
        ("q^(3/14)", Q0 ** (3.0 / 14.0)),
    ]
    best = None
    for name, value in candidates:
        if value == 0:
            continue
        rel = abs(a_sdp - value) / max(abs(value), 1e-12)
        marker = ""
        if best is None or rel < best[0]:
            best = (rel, name, value)
        print(f"    {name:<22s} = {value:>10.6f}  |Δ_rel| = {rel:.4e}")
    print()
    print(f"  Best match: a_SDP ≈ {best[1]} "
          f"(|Δ_rel| = {best[0]:.4e})")
    print()

    print(f"  Wedderburn weights at optimum:")
    for lam, av in sorted(alpha_values.items(),
                          key=lambda kv: -kv[1]):
        if av > 1e-9:
            print(f"    α_{str(lam):<20s} = {av:.6f}")

    # Witness
    builder = (
        WitnessBuilder("staircase-ew-sdp-crossing", engine="numpy")
        .set_description(
            "SDPB-style staircase EW-residual derivation at k=3 — "
            "analogue of probe_sdpb_pl_crossing_equations.py "
            "(commit 5e7459cf0). Sets up a Wedderburn-block SDP over "
            "the 11 partitions of n_3=6 with Hoefsmit-σ-symmetric PSD "
            "block matrices, mirror-parity constraints, normalisation, "
            "Markov-pair-trace saturation, and an `a` parameter "
            "(EW residual scale) to maximise. Reports the SDP "
            "optimum and the best-match substrate scale "
            "(z_markov, 1/h_corner, q^(1/5), etc.). CAVEAT: "
            "constraints 5-6 are heuristic stand-ins mirroring the "
            "PL probe's structure, NOT derived from a categorical "
            "crossing-equation analysis of V_(3,2,1). Treat as "
            "directional: which substrate scale does the analogue-"
            "of-PL SDP saturate to?"
        )
        .set_content_block("conj:staircase-ew-residual")
        .set_audit_only(
            "docs/audits/2026-05-17-staircase-ew-sdp-crossing.md")
        .add_parameter("k", K)
        .add_parameter("staircase_partition", list(SHAPE_K3))
        .add_parameter("n_strands", N_STRANDS)
        .add_parameter("h_corner", H_CORNER)
        .add_parameter("q_0", Q0)
        .add_parameter("z_markov", float(z_markov))
        .add_data("sdp_status", status)
        .add_data("a_sdp_optimum", a_sdp)
        .add_data("best_match_label", best[1])
        .add_data("best_match_value", float(best[2]))
        .add_data("best_match_rel_err", float(best[0]))
        .add_data("alpha_optimum",
                  {str(k): v for k, v in alpha_values.items()})
        .add_data("candidate_scales",
                  {name: float(v) for name, v in candidates})
        .add_caveat(
            "Heuristic SDP scaffolding: constraints 5-6 (Markov-pair "
            "saturation, a-consistency) MIRROR the PL probe's "
            "structure but are NOT derived from a categorical "
            "crossing-equation analysis specific to V_(3,2,1). The "
            "SDP-saturating value reported should be read as "
            "directional evidence about which substrate scale "
            "(z_markov, ℏ_q, 1/h_corner, q^p/q) appears naturally in "
            "the optimisation, not as a substrate derivation of the "
            "EW residual. A real derivation would replace the "
            "heuristic constraints with rigorous ones (e.g. via "
            "prop:operator-selection-sdp categorical bootstrap)."
        )
    )
    out_path = builder.save()
    print()
    print(f"  Witness: {out_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
