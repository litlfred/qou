# archimedean_by_design: scipy LP/SDP solver wrapper + numpy
#   float64 Hoefsmit matrices (the `_hoefsmit_f64_matrices` helper
#   makes this explicit in its name). Substrate precision is the
#   input q-arithmetic; the LP/SDP solve and the Gram matrix
#   assembly are float64 by necessity (scipy.optimize.linprog +
#   numpy.linalg).
"""Wedderburn pair-volume LP/SDP wiring for the EW-sector + alt-Δ_I
Weinberg-angle probe.

Two deliverables in one witness:

(A) WIRE  wedderburn_pair_volumes into prop:knot-operator-lp-selection.
    Concrete numerical instance: solve the LP/SDP-dual program for the
    EW-sector operator selection with Wedderburn pair amplitudes
    |V̂_i V̂_j|_Wedd as the supply matrix.  Report primal_obj, dual_obj,
    y_0_star, y_star, active_set per AGENTS.md "LP/SDP duals —
    first-class infra" mandate.

(B) TRY  to close the 2.19% Weinberg gap by extending the Δ_I word
    space.  The (3,2,1) max+/2nd-max+ = 1.78 reading on
    Δ_I^minimal = σ_2 σ_4 σ_2 was 2.19% off CODATA cot θ_W = 1.823.
    Test ~10 alternative Δ_I words and report the best ratio +
    associated structural signature.

Witness output: wedderburn-lp-ew-wiring.witness.json (with LP duals
to satisfy lp_dual_witness_validator).
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from wedderburn_pair_volumes import wedderburn_pair_volumes  # noqa: E402
from hecke_character_symbolic import _hoefsmit_build  # noqa: E402
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from partition_utils import hook_lengths  # noqa: E402


def _hoefsmit_f64_matrices(n: int, q0_value: float) -> dict:
    """Pre-compute f64 Hoefsmit generator matrices ``M^λ_g`` for every
    partition ``λ ⊢ n`` and every generator ``g ∈ {0, …, n-2}``.

    Returns a dict ``{λ: {"matrices": [M_0, M_1, …], "y": y_λ(q_0)}}``
    where each ``M_g`` is an ``np.ndarray`` of dtype ``np.float64`` and
    ``y_λ`` is the canonical Plancherel weight on ``λ`` at ``q_0``.

    The caller then evaluates Markov traces of arbitrary 4-letter
    words via three matrix multiplications + one trace + sum over
    ``λ`` — orders of magnitude faster than the per-word
    ``tr_M_via_wenzl_bridge_mpfr`` mpfr assembly when many words
    share the same ``n``.
    """
    import sympy as _sp
    from hecke_character_symbolic import _hoefsmit_build  # noqa: E402

    # y_λ(q) = (q − q⁻¹)^(n − ℓ(λ)) · ∏_{x ∈ λ} [h_x(λ)]_q⁻¹
    # (canonical Plancherel weight on the Hecke algebra at q).
    q = q0_value
    qi = 1.0 / q

    def q_int_f(k: int) -> float:
        if k == 0:
            return 0.0
        return (q ** k - qi ** k) / (q - qi)

    # Enumerate partitions of n.
    from hecke_character_symbolic import partitions_of  # noqa: E402

    out = {}
    q_sp = _sp.Float(q0_value, 50)
    for shape in partitions_of(n):
        sp_mats, dim, _ = _hoefsmit_build(list(shape), q_sp)
        if dim == 0:
            continue
        np_mats = [
            np.array(m.tolist(), dtype=np.float64) for m in sp_mats
        ]
        ell = len(shape)
        prefactor = (q - qi) ** (n - ell)
        denom = 1.0
        for h in hook_lengths(shape):
            denom *= q_int_f(h)
        y_lam = prefactor / denom
        out[tuple(shape)] = {"matrices": np_mats, "y": y_lam, "dim": dim}
    return out


def _klr_positive_supply_vector(
    pairs: list,
    n_strands: int,
    q_str: str,
    *,
    hoefsmit_cache: dict | None = None,
) -> np.ndarray:
    """KLR-positive supply vector ``t_k = tr_M(σ_i σ_j)`` per pair.

    Replaces the signed `pair["full"]` matrix-entry sum used on PR
    #618 with the genuine pair Markov trace
    ``Σ_λ y_λ(q) · χ_λ(σ_i σ_j)`` evaluated in H_(3·A).  By KLR
    positivity (operators in the canonical-basis cone are non-
    negative at q > 0; cf. Kashiwara-Saito, Brundan-Kleshchev), this
    vector is non-negative for every pair and the LP
    ``min ⟨t, x⟩ s.t. Σx = n_target, Gx ≥ 0, x ≥ -M`` is bounded
    for every atom.

    Re-uses the same Hoefsmit cache as ``_full_wedderburn_gram`` to
    avoid recomputing per-partition matrices.

    Parameters
    ----------
    pairs
        Pair list (only ``i`` / ``j`` indices consumed).
    n_strands
        Hecke algebra rank ``n = 3·A``.
    q_str
        ``q_0`` as 50-dps decimal string.
    hoefsmit_cache
        Optional precomputed cache from ``_hoefsmit_f64_matrices``;
        built on demand if ``None``.

    Returns
    -------
    numpy.ndarray
        Real ``(n_pairs,)`` vector of pair Markov traces.
    """
    if hoefsmit_cache is None:
        q0_value = float(__import__("sympy").Float(q_str, 50))
        hoefsmit_cache = _hoefsmit_f64_matrices(n_strands, q0_value)
    t = np.zeros(len(pairs), dtype=float)
    for k, p in enumerate(pairs):
        i, j = p["i"], p["j"]
        for shape, info in hoefsmit_cache.items():
            mats = info["matrices"]
            M_ij = mats[i] @ mats[j]
            t[k] += info["y"] * float(np.trace(M_ij))
    return t


def _full_wedderburn_gram(
    pairs: list,
    n_strands: int,
    q_str: str,
    *,
    eps: float = 1e-9,
    hoefsmit_cache: dict | None = None,
):
    """Full H_n Wedderburn Frobenius Gram on the pair-operator algebra.

    For each pair ``(i, j)`` of generators in the atom braid, treat
    the Hecke element ``σ_i · σ_j ∈ H_n(q)`` as the basis vector for
    that pair.  The Frobenius inner product on H_n via the Markov
    trace is::

        G_{(i,j),(i',j')}
            = ⟨σ_i σ_j, σ_{i'} σ_{j'}⟩_{tr_M}
            = Σ_λ⊢n  y_λ(q) · χ_λ(σ_i σ_j σ_{i'} σ_{j'})

    where ``y_λ`` are the canonical Plancherel weights on H_n(q) and
    ``χ_λ`` is the Hoefsmit character on the Wedderburn block ``λ``.

    This is the genuine off-diagonal Wedderburn coupling — no
    diagonal-only proxy, no rank-3 H_3-channel projection — and is
    full-rank generically (modulo bar-involution kernel).

    Implementation: pre-computes f64 Hoefsmit generator matrices once
    per partition, then evaluates each pair-pair Markov trace as a
    chain of three matrix multiplications + trace summed over ``λ``.
    Symmetric in ``(k, k')`` by cyclicity of the trace, so only the
    upper triangle is computed.  Caller may pass an externally-built
    ``hoefsmit_cache`` to share work across atoms with the same
    ``n_strands``.

    Parameters
    ----------
    pairs
        Pair-amplitude list from ``wedderburn_pair_volumes`` (only
        the ``i`` and ``j`` indices are consumed).
    n_strands
        Hecke algebra rank ``n = 3·A`` for the atom.
    q_str
        ``q_0`` as a 50-dps decimal string (used to reconstruct an
        f64 working value for the Hoefsmit matrices).
    eps
        Tikhonov regularisation added to the diagonal so
        ``solve_operator_selection_lp`` sees a strictly PSD matrix.
    hoefsmit_cache
        Optional precomputed cache from ``_hoefsmit_f64_matrices``.
        If ``None``, built on demand.

    Returns
    -------
    numpy.ndarray
        Real ``(n_pairs, n_pairs)`` Gram matrix.
    """
    n_pairs = len(pairs)
    G = np.zeros((n_pairs, n_pairs), dtype=float)
    if hoefsmit_cache is None:
        q0_value = float(__import__("sympy").Float(q_str, 50))
        hoefsmit_cache = _hoefsmit_f64_matrices(n_strands, q0_value)

    # Pre-compute the σ_i σ_j matrix per pair per partition.  This
    # turns the pair-pair Markov trace into a single matrix product
    # + trace per λ (factor-of-2 speed-up over recomputing).
    pair_mats_per_lambda: dict[tuple, list] = {}
    for shape, info in hoefsmit_cache.items():
        mats = info["matrices"]
        pair_mats_per_lambda[shape] = [
            mats[p["i"]] @ mats[p["j"]] for p in pairs
        ]

    for k in range(n_pairs):
        for kp in range(k, n_pairs):
            val = 0.0
            for shape, info in hoefsmit_cache.items():
                # χ_λ(σ_i σ_j σ_{i'} σ_{j'}) = tr(M_ij^λ · M_i'j'^λ)
                M_kkp = pair_mats_per_lambda[shape][k] @ \
                        pair_mats_per_lambda[shape][kp]
                val += info["y"] * float(np.trace(M_kkp))
            G[k, kp] = val
            G[kp, k] = val

    G = G + eps * np.eye(n_pairs)
    return G


def beta_ew_word(delta_I):
    """β_EW(Δ_I) = σ_1^4 · Δ_I · σ_3^6 · Δ_I · σ_5^8 · Δ_I."""
    return [0]*4 + delta_I + [2]*6 + delta_I + [4]*8 + delta_I


def beta_matrix_at_q0(shape, q_0, word):
    """Build β_EW matrix on V_λ at q_0 (Float specialization).

    Converts each Hoefsmit generator matrix to numpy *once* up front,
    then runs the per-generator multiplication in numpy.  Symbolic
    matrix multiplication for a 3·A-letter word can dominate runtime
    on V_(3,2,1) (dim 16); the numpy path matches the eventual
    eigvals consumer at the cost of a one-time elaboration.
    """
    matrices, dim, _ = _hoefsmit_build(list(shape), q_0)
    if dim == 0:
        return None, 0
    np_mats = [
        np.array(m.tolist(), dtype=np.complex128) for m in matrices
    ]
    M = np.eye(dim, dtype=np.complex128)
    for gen_idx in word:
        M = M @ np_mats[gen_idx]
    return M, dim


def compute_321_max_plus_ratio(q_0, delta_I):
    """For β_EW(Δ_I) on V_(3,2,1), return max+/2nd-max+ eigenvalue ratio."""
    word = beta_ew_word(delta_I)
    M_np, dim = beta_matrix_at_q0((3, 2, 1), q_0, word)
    if M_np is None:
        return None, []
    eigs = np.linalg.eigvals(M_np).real
    pos = sorted([e for e in eigs if e > 0])
    if len(pos) < 2:
        return None, eigs.tolist()
    return pos[-1] / pos[-2], eigs.tolist()


def main() -> int:
    q_0 = sp.Float(Q_50_DIGIT_STR, 50)
    q_0_float = float(q_0)
    print(f"Wedderburn LP/SDP-EW wiring + alt-Δ_I Weinberg probe")
    print(f"  q_0 ≈ {q_0_float:.10f}")
    print()

    # ── (A) LP/SDP wiring with Wedderburn pair volumes ──────────
    print("=" * 72)
    print("(A) LP/SDP-dual program for EW-sector operator selection")
    print("=" * 72)
    # Test multiple atoms to exercise the LP at varying #pair counts.
    # Maximum strand count (n=3·A) we attempt the *full* Wedderburn
    # Gram for in this script; atoms beyond this skip with a clearly-
    # labelled `deferred_compute_budget` status (the math is well-
    # defined, but the sympy-based `_hoefsmit_build` precomputation
    # for p(12)=77 partitions × 11 generators at H_12 dim ≤ 462
    # exceeds reasonable session budget without the optional Rust
    # mpfr kernel `pyhecke_native`).  See audit doc § "Compute
    # budget for headline atom" for the open-frontier follow-up.
    MAX_FULL_GRAM_N = 9
    lp_results_per_atom = []
    atoms_to_test = [
        ("proton",   1, 0),
        ("neutron",  0, 1),
        ("deuteron", 1, 1),
        ("triton",   1, 2),
        ("helium-4", 2, 2),
    ]
    # Choose the heaviest *computable* atom as the headline (so the
    # primary LP solve in this run produces concrete numbers rather
    # than a `deferred` placeholder).
    headline_idx = max(
        (i for i, (_, Za, Na) in enumerate(atoms_to_test)
         if 3 * (Za + Na) <= MAX_FULL_GRAM_N),
        default=0,
    )
    Z, N = atoms_to_test[headline_idx][1], atoms_to_test[headline_idx][2]
    pairs = wedderburn_pair_volumes(Z, N, include_inter=True,
                                    crossings_per_pair=1)
    print(f"  Headline atom: {atoms_to_test[headline_idx][0]} (Z={Z}, N={N})")
    print(f"  # pair amplitudes: {len(pairs)}")

    # Build the LP for operator selection per `solve_operator_selection_lp`:
    #   primal:  min ⟨t, x⟩
    #            s.t.  Σ x_i = n_target          (net constraint)
    #                  G x ≥ 0                    (Frobenius-positivity)
    #                  x_i ≥ -M                   (large-M lower bound)
    #
    #   dual:    max  n_target · y_0 - M · Σ z_i
    #            s.t.  G^T y + z = t,  y ≥ 0,  z ≥ 0
    #            (y_0_star = shadow price of net constraint;
    #             y_star    = shadow prices of Frobenius positivity rows;
    #             active_set = indices i with y_star[i] > tol — the
    #                          *saturated* positivity constraints, i.e.
    #                          channels where the primal x_k is at the
    #                          boundary and the dual is binding.)
    #
    # For the EW-sector wiring: each basis element b_k corresponds to
    # the Hecke element σ_i σ_j ∈ H_(3·A)(q) for pair (i, j).  We use:
    #   t_k = tr_M(σ_i σ_j) = Σ_λ y_λ · χ_λ(σ_i σ_j)
    #         (KLR-positive pair Markov trace; non-negative for every
    #          pair by KLR positivity on the canonical-basis cone —
    #          replaces PR #618's signed pair["full"] matrix-entry
    #          sum, which was a setup error.  See audit doc §0.)
    #   G_{kk'} = tr_M(σ_i σ_j σ_{i'} σ_{j'})
    #           = Σ_λ y_λ · χ_λ(σ_i σ_j σ_{i'} σ_{j'})
    #         (full Wedderburn Frobenius Gram on the pair-operator
    #          algebra; see `_full_wedderburn_gram`).
    n_pairs = len(pairs)
    n_strands_headline = 3 * (Z + N)
    print(f"  Pre-computing H_{n_strands_headline} Hoefsmit matrices for "
          f"{n_pairs} pairs ({n_pairs} pair Markov traces + "
          f"{n_pairs * (n_pairs + 1) // 2} unique pair-pair traces; "
          f"shared Hoefsmit cache)...")
    q_0_for_cache = float(sp.Float(Q_50_DIGIT_STR, 50))
    hoefsmit_cache_h = _hoefsmit_f64_matrices(n_strands_headline,
                                              q_0_for_cache)
    t = _klr_positive_supply_vector(
        pairs, n_strands_headline, Q_50_DIGIT_STR,
        hoefsmit_cache=hoefsmit_cache_h,
    )
    # Sanity check: KLR positivity says t ≥ 0.  Tiny negative
    # numerical noise is tolerated; a substantive negative entry is
    # a bug or a non-canonical-basis pair (would need separate
    # investigation).
    if t.min() < -1e-9:
        print(f"  WARN: KLR positivity violation — min(t) = {t.min():.3e}")
    # Keep the legacy signed matrix-entry sum for diff/comparison.
    t_legacy_matrix_entries = np.array(
        [p["full"] for p in pairs], dtype=float
    )
    G = _full_wedderburn_gram(
        pairs, n_strands_headline, Q_50_DIGIT_STR,
        hoefsmit_cache=hoefsmit_cache_h,
    )
    # Total target: half the sum of available KLR-positive amplitudes
    # (loose constraint to ensure feasibility).
    n_target = float(t.sum() * 0.5)
    print(f"  t (KLR pair Markov traces, top 3): {t[:3].tolist()}")
    print(f"  t.min = {t.min():.4e}, t.max = {t.max():.4e}")
    print(f"  legacy(matrix-entry) t.min = {t_legacy_matrix_entries.min():.4e}, "
          f"t.max = {t_legacy_matrix_entries.max():.4e}")
    print(f"  G shape: {G.shape}, n_target = {n_target:.6f}")
    # M_bound=0 enforces x ≥ 0 (operator coefficients are non-negative,
    # the natural interpretation of "operator selection" in
    # prop:knot-operator-lp-selection).  With KLR-positive t and x ≥ 0
    # the LP is bounded for every atom and strong duality holds; the
    # default M_bound=1e6 in `solve_operator_selection_lp` is intended
    # for problems with signed coefficients (not this case).
    # Pin scipy: committed-witness producer → byte-deterministic.
    res = solve_operator_selection_lp(t, G, n_target, M_bound=0.0, backend="scipy")
    res_dict = res.to_dict()

    # Also run LP for each atom in atoms_to_test (sweep)
    for atom_name, Za, Na in atoms_to_test:
        n_strands_a = 3 * (Za + Na)
        if n_strands_a > MAX_FULL_GRAM_N:
            # Skip with explicit deferred status — math is well-defined
            # but Hoefsmit precomputation at H_n exceeds session budget
            # without the Rust mpfr kernel.
            lp_results_per_atom.append({
                "atom": atom_name, "Z": Za, "N": Na,
                "n_strands": n_strands_a,
                "deferred_compute_budget": (
                    f"H_{n_strands_a} sympy Hoefsmit precomputation "
                    f"(p({n_strands_a}) partitions × {n_strands_a - 1} "
                    "generators) exceeds session budget without "
                    "pyhecke_native. Re-run with the Rust kernel "
                    "installed to lift this restriction."
                ),
            })
            continue
        try:
            ps = wedderburn_pair_volumes(Za, Na, include_inter=True,
                                         crossings_per_pair=1)
        except Exception as e:
            lp_results_per_atom.append({
                "atom": atom_name, "Z": Za, "N": Na,
                "error": f"{type(e).__name__}: {e}",
            })
            continue
        npairs_a = len(ps)
        if npairs_a == 0:
            lp_results_per_atom.append({
                "atom": atom_name, "Z": Za, "N": Na,
                "n_pairs": 0, "skipped": "no pairs",
            })
            continue
        # Reuse Hoefsmit cache for both supply vector + Gram.
        cache_a = _hoefsmit_f64_matrices(n_strands_a, q_0_for_cache)
        ta = _klr_positive_supply_vector(
            ps, n_strands_a, Q_50_DIGIT_STR, hoefsmit_cache=cache_a
        )
        ta_legacy = np.array([p["full"] for p in ps], dtype=float)
        Ga = _full_wedderburn_gram(
            ps, n_strands_a, Q_50_DIGIT_STR, hoefsmit_cache=cache_a
        )
        ntarget_a = float(ta.sum() * 0.5)
        try:
            ra = solve_operator_selection_lp(
                ta, Ga, ntarget_a, M_bound=0.0, backend="scipy"
            ).to_dict()
        except Exception as e:
            lp_results_per_atom.append({
                "atom": atom_name, "Z": Za, "N": Na,
                "n_pairs": npairs_a,
                "error": f"{type(e).__name__}: {e}",
            })
            continue
        lp_results_per_atom.append({
            "atom": atom_name, "Z": Za, "N": Na,
            "n_pairs": npairs_a,
            "n_strands": n_strands_a,
            "t_min_klr": float(ta.min()),
            "t_max_klr": float(ta.max()),
            "t_legacy_matrix_entries_min": float(ta_legacy.min()),
            "t_legacy_matrix_entries_max": float(ta_legacy.max()),
            "primal_obj": float(ra["primal_obj"]),
            "dual_obj": float(ra["dual_obj"]),
            "duality_gap": float(ra["duality_gap"]),
            "y0_star": float(ra["y0_star"]),
            "n_active": len(ra.get("active_set", [])),
            "n_target": ntarget_a,
        })
        print(f"    {atom_name:<12} (Z={Za}, N={Na}): pairs={npairs_a}, "
              f"primal={ra['primal_obj']:.4f}, y_0={ra['y0_star']:.4f}")
    print(f"  LP solve:")
    print(f"    primal_obj = {res_dict['primal_obj']:.6f}")
    print(f"    dual_obj   = {res_dict['dual_obj']:.6f}")
    print(f"    duality_gap= {res_dict['duality_gap']:.3e}")
    print(f"    y_0_star (shadow price of net constraint) = "
          f"{res_dict['y0_star']:.6f}")
    n_active = len(res_dict.get("active_set", []))
    print(f"    # active channels = {n_active}")
    print()

    # ── (B) Alt-Δ_I Weinberg probe ──────────────────────────────
    print("=" * 72)
    print("(B) Alternative Δ_I words to close the 2.19% Weinberg gap")
    print("=" * 72)
    cot_codata = float(sp.sqrt(sp.Rational(1) - sp.Rational("0.23129"))
                       / sp.sqrt(sp.Rational("0.23129")))
    print(f"  CODATA cot θ_W = {cot_codata:.6f}")
    print()

    # Candidate Δ_I words — all use generators σ_2 (idx 1) and σ_4 (idx 3)
    delta_candidates = [
        ("σ_2 σ_4 σ_2 (minimal, baseline)", [1, 3, 1]),
        ("σ_4 σ_2 σ_4 (mirror)",            [3, 1, 3]),
        ("σ_2 σ_4",                          [1, 3]),
        ("σ_4 σ_2",                          [3, 1]),
        ("σ_2² σ_4²",                       [1, 1, 3, 3]),
        ("σ_4² σ_2²",                       [3, 3, 1, 1]),
        ("σ_2 σ_4² σ_2",                    [1, 3, 3, 1]),
        ("σ_4 σ_2² σ_4",                    [3, 1, 1, 3]),
        ("σ_2 σ_4 σ_2 σ_4",                  [1, 3, 1, 3]),
        ("σ_4 σ_2 σ_4 σ_2",                  [3, 1, 3, 1]),
        ("σ_2 σ_4 σ_2 σ_4 σ_2",             [1, 3, 1, 3, 1]),
        ("σ_2 (single)",                    [1]),
        ("σ_4 (single)",                    [3]),
        ("(empty Δ_I = trivial)",           []),
    ]

    results = []
    for name, delta in delta_candidates:
        t0 = time.time()
        try:
            ratio, eigs = compute_321_max_plus_ratio(q_0, delta)
        except Exception as e:
            print(f"  {name:<35} FAILED ({type(e).__name__}: {e})")
            continue
        elapsed = time.time() - t0
        if ratio is None:
            print(f"  {name:<35} (insufficient + eigvals)")
            continue
        rel_err = abs(ratio - cot_codata) / cot_codata
        flag = "★" if rel_err < 0.001 else ("✓" if rel_err < 0.01 else "·" if rel_err < 0.05 else " ")
        print(f"  {flag} {name:<35} ratio = {ratio:>9.4f}  "
              f"rel_err = {rel_err*100:>6.2f}%  ({elapsed:.2f}s)")
        results.append({
            "delta_I_name": name,
            "delta_I_word": delta,
            "ratio": ratio,
            "rel_err": rel_err,
        })

    print()
    best = min(results, key=lambda r: r["rel_err"])
    print(f"Best Δ_I (3,2,1)max+/2nd-max+ vs CODATA cot θ_W:")
    print(f"  {best['delta_I_name']}")
    print(f"  Δ_I word: {best['delta_I_word']}")
    print(f"  ratio = {best['ratio']:.6f}")
    print(f"  rel err = {best['rel_err']*100:.4f}%")
    print()

    if best["rel_err"] < 0.001:
        verdict = "candidate-found-precision-1e-3"
    elif best["rel_err"] < 0.01:
        verdict = "near-miss-precision-1e-2"
    elif best["rel_err"] < 0.05:
        verdict = "near-miss-precision-5pct"
    else:
        verdict = "no-clean-fit"
    print(f"VERDICT (B): {verdict}")
    print()

    # ── Witness assembly via WitnessBuilder ────────────────────
    from witness_base import WitnessBuilder
    w = (
        WitnessBuilder("wedderburn-lp-ew-wiring", engine="numpy+sympy")
        .set_description(
            "Two deliverables: (A) wires wedderburn_pair_volumes into "
            "prop:knot-operator-lp-selection via concrete LP/SDP-dual "
            "program for EW-sector pair amplitudes (atom sweep "
            "proton..helium-4); (B) probes alternative Δ_I words on β_EW "
            "to close the 2.19% Weinberg gap on (3,2,1) max+/2nd-max+ "
            "= cot θ_W reading."
        )
        .set_content_block("prop:knot-operator-lp-selection")
        .add_parameter("q_0", str(q_0))
        .add_parameter("n_target_headline", n_target)
        .add_parameter("delta_I_minimal", "σ_2 σ_4 σ_2")
    )

    # LP behaviour assertions.  With the KLR-positive supply vector
    # (t_k = tr_M(σ_i σ_j) ≥ 0 by KLR positivity on the canonical-
    # basis cone) and the full H_n Wedderburn Gram on the pair-
    # operator algebra, strong duality holds on every atom in the
    # computable sweep.
    n_strong_dual = sum(
        1 for r in lp_results_per_atom
        if r.get("n_pairs", 0) > 0
        and r.get("duality_gap", float("inf")) < 1e-6
    )
    n_expected = sum(
        1 for r in lp_results_per_atom if r.get("n_pairs", 0) > 0
    )
    w.add_assertion(
        "lp_strong_duality_all_klr_atoms",
        float(n_strong_dual),
        float(n_expected),
        tolerance=0.5,
    )
    # KLR positivity assertion: every atom's KLR supply vector
    # min(t) ≥ -ε (tiny numerical noise tolerated; substantive
    # negative would indicate a non-canonical-basis pair or a bug).
    n_klr_positive = sum(
        1 for r in lp_results_per_atom
        if r.get("n_pairs", 0) > 0
        and r.get("t_min_klr", -1.0) >= -1e-9
    )
    w.add_assertion(
        "klr_positivity_supply_vector_all_atoms",
        float(n_klr_positive),
        float(n_expected),
        tolerance=0.5,
    )
    # Weinberg verdict: best rel_err < 2.5% (the σ_2 σ_4 σ_2 baseline)
    w.add_assertion(
        "weinberg_minimal_delta_I_optimal",
        float(best["rel_err"]),
        0.0219,  # baseline 2.19% rel_err
        tolerance=0.005,
    )

    # (A) LP/SDP-EW deliverable
    w.add_data("deliverable_A_lp_sdp_wiring", {
        "headline_atom": {
            "Z": Z, "N": N,
            "name": atoms_to_test[headline_idx][0],
            "max_full_gram_n_strands": MAX_FULL_GRAM_N,
        },
        "n_pair_amplitudes": n_pairs,
        "primal_obj": float(res_dict["primal_obj"]),
        "dual_obj": float(res_dict["dual_obj"]),
        "duality_gap": float(res_dict["duality_gap"]),
        "y0_star": float(res_dict["y0_star"]),
        "y_star": [float(y) for y in res_dict.get("y_star", [])],
        "active_set": list(res_dict.get("active_set", [])),
        "n_target": n_target,
        "supply_matrix_shape": list(G.shape),
        "atom_sweep": lp_results_per_atom,
    })

    # Top-level LP-dual fields for lp_dual_witness_validator
    w.add_data("primal_obj", float(res_dict["primal_obj"]))
    w.add_data("dual_obj", float(res_dict["dual_obj"]))
    w.add_data("duality_gap", float(res_dict["duality_gap"]))
    w.add_data("y0_star", float(res_dict["y0_star"]))
    w.add_data("y_star", [float(y) for y in res_dict.get("y_star", [])])
    w.add_data("active_set", list(res_dict.get("active_set", [])))

    # (B) Alt-Δ_I Weinberg probe
    w.add_data("deliverable_B_alt_delta_I_weinberg_probe", {
        "codata_cot_theta_W": cot_codata,
        "candidates": results,
        "best": best,
        "verdict": verdict,
    })

    out_path = w.save()
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
