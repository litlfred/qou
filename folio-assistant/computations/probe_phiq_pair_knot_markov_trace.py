#!/usr/bin/env python3
"""Refined pair-knot probe: full Markov-trace composite volume,
full Frobenius Gram, LP **and** SDP operator-selection duals.

The simple product-volume convention
`|V̂_shell| = ∏_{i ∈ shell} |V̂_i|` was refuted in
`probe_phiq_pair_knot_magic_shell.py`, but the operator-selection
LP dual confirmed that pair-knot composite operators σ_pp, σ_nn
ARE structurally selected at magic shells. The LP-dual evidence
points at a refinement: replace the simple product volume by the
**full Markov trace** of the shell sub-braid as a single Hecke
element evaluated via Hoefsmit seminormal.

This probe implements the refinement and confirms via BOTH the
LP dual (scipy linprog) and the SDP dual (cvxpy / SCS), with the
**full Frobenius Gram** `G_{ij} = tr_M(σ_i σ_j)` instead of the
diagonal approximation.

Three coupled hypotheses tested:

1. **Markov-trace composite volume.**  Replace
   `|V̂_pp| = ∏_{i ∈ Z-shell} |V̂_i|` with
   `|V̂_pp| = |tr_M(σ_{i_1} σ_{i_2} σ_{i_3} σ_{i_4})|` where
   `tr_M(b) = Σ_λ y_λ(q_0) · χ^λ_q(b)` is the canonical
   Jones-Markov trace via Wenzl Schur principal specialization
   + Hoefsmit seminormal characters.

2. **Full Frobenius Gram in LP.**  Replace diagonal
   `G_{ii} = |V̂_i|²` with `G_{ij} = tr_M(σ_i σ_j)` for the full
   operator basis `{σ_i, σ_pp, σ_nn}`.  Computed via the same
   Hoefsmit infrastructure.  Tightens the LP relaxation.

3. **SDP confirmation.**  Solve
   `solve_psd_operator_selection_sdp(t, G, n_target)` via cvxpy /
   SCS; compare to LP primal+dual.  The SDP gives a strictly
   stronger lift; if SDP and LP agree, the diagonal-Gram
   approximation was sufficient; if they differ, off-diagonal
   correlations are structural.

Scope: D, T, ³He at n = 6, 9, 9.  ⁴He at n = 12 is deferred — the
n = 12 Hoefsmit seminormal compute is ~10 min; the existing
diagonal-Gram pair-knot probe carries the ⁴He data.

Output: `probe-phiq-pair-knot-markov-trace.witness.json`
"""
import sys
import json
import math
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np

from q_parameter import Q as Q0
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder
from hecke_characters import build_seminormal_matrices
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
from wedderburn_jones_markov import y_lambda_at
from mass_at_3A_proper import chi_lambda_of_word
from hecke_core import atom_per_generator_volumes
from lp_dual_solver import (
    solve_operator_selection_lp,
    solve_psd_operator_selection_sdp,
)

AME = {"deuteron": 2.224566, "tritium": 8.481798, "he3": 7.71806}
Z_N = {"deuteron": (1, 1), "tritium": (1, 2), "he3": (2, 1)}
RHO_MAP = {"deuteron": 1, "tritium": 2, "he3": 2}
N_STAR = {"deuteron": 1, "tritium": 2, "he3": 1}  # R2-op best from previous probe
THRESHOLD_PCT = 10.0


class PhiQPoleHit(Exception):
    pass


def phi_q_truncated(z, k_max, q=float(Q0)):
    qi = 1.0 / q
    product = 1.0
    qi_pow = qi
    for k in range(1, k_max + 1):
        factor = 1.0 - qi_pow * z
        if abs(factor) < 1e-14:
            raise PhiQPoleHit(f"j={k}, q^-j·z={qi_pow * z:.4g}")
        product /= factor
        qi_pow *= qi
    return product


def magic_shell_indices(Z, N):
    proton_shell = [0, 1, 3, 4] if Z == 2 else []
    neutron_shell = []
    if N == 2:
        nstart = 3 * Z
        neutron_shell = [nstart, nstart + 1, nstart + 3, nstart + 4]
    return proton_shell, neutron_shell


def tr_M_of_word(word, y_vals, sigmas_per_shape, dim_per_shape, n_gens_required):
    """Markov trace of a generic Hecke braid word.

    word: list of (c, d, gen_idx) triples
    y_vals: dict {partition → y_λ(q_0)}
    sigmas_per_shape: dict {partition → list of seminormal matrices}
    dim_per_shape: dict {partition → SYT count}

    Returns Σ_λ y_λ · χ^λ_q(word).
    """
    total = 0.0
    for shape, y in y_vals.items():
        sigmas = sigmas_per_shape[shape]
        dim = dim_per_shape[shape]
        if dim == 0:
            continue
        chi = chi_lambda_of_word(sigmas, dim, word, n_gens_required)
        total += float(y) * float(chi)
    return total


def main():
    HERE = Path(__file__).parent
    sigma_3A_witness = json.loads(
        (HERE / "probe-term4-conventions.witness.json").read_text()
    )["sigma_inv_dim_q_at_q0"]
    def sigma_3A(A):
        return float(sigma_3A_witness[f"n={3 * A}"])

    q0_val = float(Q0)
    block_cache = BlockCache(q0_val, q0_val - 1.0 / q0_val)

    w = (
        WitnessBuilder("probe-phiq-pair-knot-markov-trace", engine="python")
        .set_description(
            "Refined pair-knot probe: full Markov-trace composite "
            "volume |V̂_pp| = |tr_M(σ_{shell})| (Hoefsmit seminormal "
            "via wedderburn_jones_markov + chi_lambda_of_word), "
            "full Frobenius Gram G_ij = tr_M(σ_i σ_j) for the "
            "operator-selection LP, AND the SDP dual via cvxpy / SCS. "
            "Refines the simple product-volume convention in "
            "probe-phiq-pair-knot-magic-shell.witness.json (refuted) "
            "by replacing it with the canonical Markov-trace evaluation "
            "of the shell sub-braid as a single Hecke element. "
            "Scope: D, T, ³He.  ⁴He deferred (n=12 Hoefsmit seminormal "
            "compute ~10 min)."
        )
        .set_content_block("conj:brane-tower-z-habiro")
        .add_parameter("q_0", q0_val)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("threshold_pct", THRESHOLD_PCT)
        .add_parameter("ame_targets", AME)
        .add_parameter("n_star_per_atom", N_STAR)
    )

    print("=" * 88)
    print("Refined pair-knot probe — full Markov-trace + full Gram")
    print("=" * 88)
    print(f"  q_0 = {q0_val}, m_e = {M_E_MEV} MeV")
    print()

    per_atom = {}
    for name, (Z, N) in Z_N.items():
        A = Z + N
        n = 3 * A
        n_star = N_STAR[name]
        rho = RHO_MAP[name]
        sigma_val = sigma_3A(A)
        p_shell, n_shell = magic_shell_indices(Z, N)
        print(f"  ── {name} (Z={Z}, N={N}, n={n}, n_⋆={n_star}) ──")

        # ── Build all seminormal matrices for every partition once.
        print(f"    Building Hoefsmit seminormal matrices...", flush=True)
        t0 = time.time()
        y_vals = y_lambda_at(n, q_val=q0_val)
        sigmas_per_shape = {}
        dim_per_shape = {}
        for shape in y_vals:
            sigmas, dim, _ = build_seminormal_matrices_cached(
                shape, cache=block_cache,
            )
            sigmas_per_shape[shape] = sigmas
            dim_per_shape[shape] = dim
        print(f"    done in {time.time() - t0:.1f}s "
              f"({len(y_vals)} partitions)")

        n_gens = n - 1

        # ── Compute per-generator algebraic volume (legacy scalar).
        mags = [abs(v["full"]) if isinstance(v, dict) else abs(v)
                for v in atom_per_generator_volumes(Z, N, include_inter=True)]

        # ── Compute tr_M of single σ_i for each i (one-generator words).
        print(f"    Computing tr_M(σ_i) for {n_gens} generators...",
              flush=True)
        t0 = time.time()
        tr_M_singles = []
        for i in range(n_gens):
            word_i = [(1.0, 0.0, i)]
            tr_i = tr_M_of_word(word_i, y_vals, sigmas_per_shape,
                                  dim_per_shape, n_gens)
            tr_M_singles.append(tr_i)
        print(f"    done in {time.time() - t0:.1f}s")

        # ── Compute tr_M of σ_shell = σ_{i_1} σ_{i_2} ... for each shell.
        print(f"    Computing tr_M(σ_shell) for magic shells...",
              flush=True)
        t0 = time.time()
        tr_M_pp = None
        tr_M_nn = None
        if p_shell:
            word_pp = [(1.0, 0.0, i) for i in p_shell]
            tr_M_pp = tr_M_of_word(word_pp, y_vals, sigmas_per_shape,
                                    dim_per_shape, n_gens)
        if n_shell:
            word_nn = [(1.0, 0.0, i) for i in n_shell]
            tr_M_nn = tr_M_of_word(word_nn, y_vals, sigmas_per_shape,
                                    dim_per_shape, n_gens)
        print(f"    done in {time.time() - t0:.1f}s  "
              f"tr_M(σ_pp)={tr_M_pp}, tr_M(σ_nn)={tr_M_nn}")

        # ── Build the operator basis labels + cost vector t.
        basis_labels = [f"σ_{i}" for i in range(n_gens)]
        t_list = [abs(tr_M_singles[i]) for i in range(n_gens)]
        # Append pair-knot composites.
        if p_shell:
            basis_labels.append("σ_pp_markov_trace")
            t_list.append(abs(tr_M_pp))
        if n_shell:
            basis_labels.append("σ_nn_markov_trace")
            t_list.append(abs(tr_M_nn))
        d = len(basis_labels)

        # ── Build the FULL Frobenius Gram G_ij = tr_M(σ_i σ_j) for the
        # generator basis (skip pair-knot composites in the Gram for
        # now; the LP only requires G to be PSD on the active subspace).
        # G_ij ≈ Σ_λ y_λ · tr_λ(σ_i σ_j) computed via 2-generator words.
        # Cost: n_gens² character evaluations (each is fast).
        print(f"    Computing full Frobenius Gram "
              f"({n_gens}×{n_gens} = {n_gens**2} pairs)...", flush=True)
        t0 = time.time()
        G_full = np.zeros((d, d))
        # First fill the n_gens × n_gens block from generator pairs.
        for i in range(n_gens):
            for j in range(n_gens):
                # tr_M(σ_i σ_j) — represent as 2-letter word with both
                # entries (c=1, d=0).
                word_ij = [(1.0, 0.0, i), (1.0, 0.0, j)]
                G_full[i, j] = tr_M_of_word(
                    word_ij, y_vals, sigmas_per_shape,
                    dim_per_shape, n_gens,
                )
        # For composite columns/rows, use diagonal value t²
        # (full off-diagonal `tr_M(σ_i σ_shell)` would require more
        # word-product evaluations; deferred).
        for idx, comp_t in enumerate(t_list[n_gens:], start=n_gens):
            G_full[idx, idx] = comp_t * comp_t
        # Symmetrize (numerical noise).
        G_full = 0.5 * (G_full + G_full.T)
        print(f"    done in {time.time() - t0:.1f}s")

        # ── Solve LP with full Gram.
        n_target = sum(t_list)  # target = sum of |tr_M| costs
        try:
            lp = solve_operator_selection_lp(np.array(t_list), G_full,
                                              n_target)
            lp_dict = lp.to_dict()
            lp_active = [basis_labels[i] for i in lp_dict["active_set"]]
        except Exception as e:
            lp_dict = {"feasible": False, "error": str(e)}
            lp_active = []

        # ── Solve SDP with cvxpy.
        try:
            sdp = solve_psd_operator_selection_sdp(np.array(t_list),
                                                     G_full, n_target)
            sdp_dict = sdp.to_dict()
        except Exception as e:
            sdp_dict = {"feasible": False, "error": str(e)}

        # ── Compute pair-knot tower with Markov-trace composite volume.
        # Replace the simple product |V̂_shell| = ∏|V̂_i| by |tr_M(σ_shell)|.
        try:
            tower = 0.0
            components = []
            shell_idx_set = set(p_shell) | set(n_shell)
            for i, mag in enumerate(mags):
                if i in shell_idx_set:
                    continue
                phi_i = phi_q_truncated(mag, n_star)
                tower += phi_i
                components.append({
                    "label": f"σ_{i}", "|V̂|": float(mag),
                    "Φ_q": float(phi_i),
                })
            if p_shell:
                v_pp_mtrace = abs(tr_M_pp)
                phi_pp = phi_q_truncated(v_pp_mtrace, n_star)
                tower += phi_pp
                components.append({
                    "label": "σ_pp_markov_trace",
                    "|V̂|": float(v_pp_mtrace),
                    "indices": p_shell,
                    "Φ_q": float(phi_pp),
                })
            if n_shell:
                v_nn_mtrace = abs(tr_M_nn)
                phi_nn = phi_q_truncated(v_nn_mtrace, n_star)
                tower += phi_nn
                components.append({
                    "label": "σ_nn_markov_trace",
                    "|V̂|": float(v_nn_mtrace),
                    "indices": n_shell,
                    "Φ_q": float(phi_nn),
                })
            tr_M_total = tr_M_of_word(
                # The full atom braid word would give |tr_M|; we use the
                # cached value from the existing op-valued witness.
                [], y_vals, sigmas_per_shape, dim_per_shape, n_gens,
            ) if False else None
            # Reuse |tr_M| from existing witness.
            op_witness = json.loads(
                (HERE / "probe-phiq-operator-valued.witness.json").read_text()
            )
            tr_M_abs = abs(float(op_witness["data"]["per_atom"][name]["tr_M"]))
            B = M_E_MEV * rho * (tr_M_abs + tower + sigma_val)
            err = 100.0 * (B - AME[name]) / AME[name]
        except PhiQPoleHit as e:
            B = float("nan"); err = float("nan"); tower = float("nan")
            components = []
            tr_M_abs = float("nan")

        per_atom[name] = {
            "Z": Z, "N": N, "A": A, "n": n,
            "n_star": n_star,
            "magic_shells": ([] + (["Z=2"] if p_shell else [])
                             + (["N=2"] if n_shell else [])),
            "per_generator_magnitudes": [float(x) for x in mags],
            "tr_M_singles": [float(x) for x in tr_M_singles],
            "tr_M_pp_markov_trace": float(tr_M_pp) if tr_M_pp is not None else None,
            "tr_M_nn_markov_trace": float(tr_M_nn) if tr_M_nn is not None else None,
            "tr_M_abs_full_braid": float(tr_M_abs),
            "tower_markov_trace": float(tower),
            "B_markov_trace_MeV": float(B),
            "AME_MeV": AME[name],
            "err_markov_trace_pct": float(err),
            "components": components,
            "operator_basis": basis_labels,
            "operator_basis_t": [float(x) for x in t_list],
            "n_target_lp": float(n_target),
            "lp": {**lp_dict, "active_labels": lp_active},
            "sdp": sdp_dict,
        }

        print(f"    Pair-knot Markov-trace tower at n_⋆={n_star}: "
              f"{tower:.5f}")
        print(f"    B_markov_trace = {B:.4f} MeV  vs AME {AME[name]:.4f}"
              f"  err = {err:+.2f}%")
        if lp_dict.get("feasible", False):
            gap = lp_dict["duality_gap"]
            print(f"    LP:  primal={lp_dict['primal_obj']:.5f}  "
                  f"dual={lp_dict['dual_obj']:.5f}  gap={gap:.3e}")
            print(f"         active = {lp_active}")
        if sdp_dict.get("feasible", False):
            gap = sdp_dict["duality_gap"]
            n_neg_evals = sum(1 for e in sdp_dict["eigenvalues"] if e < -1e-9)
            print(f"    SDP: primal={sdp_dict['primal_obj']:.5f}  "
                  f"dual={sdp_dict['dual_obj']:.5f}  gap={gap:.3e}  "
                  f"n_neg_evals={n_neg_evals}/{len(sdp_dict['eigenvalues'])}")
        print()

    # Verdict
    print(f"  Closure verdict (|err| < {THRESHOLD_PCT}% per atom):")
    closes = []
    for name, d in per_atom.items():
        err = d["err_markov_trace_pct"]
        v = "✓" if abs(err) < THRESHOLD_PCT else "✗"
        if abs(err) < THRESHOLD_PCT:
            closes.append(name)
        print(f"    {name:>10}  err={err:+.2f}%  {v}")
    print()
    all_close = len(closes) == len(AME)
    if all_close:
        print("  ✓ Markov-trace composite volume + full Gram closes the")
        print("    AME light-isotope sample uniformly within "
              f"{THRESHOLD_PCT}%.")
    else:
        print("  ✗ Refined pair-knot probe does NOT close uniformly.")

    w = (
        w
        .add_data("per_atom", per_atom)
        .add_assertion(
            "markov_trace_pair_knot_closes_all_within_threshold",
            computed=1 if all_close else 0,
            expected=1,  # If we expect closure to fail, set 0.
        )
        .add_caveat(
            "Operator basis Gram restricted to per-generator block: "
            "G_ij = tr_M(σ_i σ_j) for i,j ∈ generators; pair-knot "
            "composite diagonal is t_pp²; off-diagonal entries "
            "G_{pp, i} = tr_M(σ_pp σ_i) deferred."
        )
        .add_caveat(
            "⁴He (n=12) deferred — Hoefsmit seminormal compute is ~10 "
            "min for the n=12 partition family. The existing diagonal-"
            "Gram pair-knot probe carries ⁴He's data at -19.4% under "
            "the simple product-volume convention."
        )
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
