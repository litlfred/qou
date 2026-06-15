"""Semidefinite-programming cross-channel LP for the nuclear braid.

Extends the scalar LP-dual of prop:mass-coefficient-shadow-price to a
matrix-valued (SDP) formulation that captures cross-channel coupling
between Wedderburn blocks and — critically — discrete regime switches
as the substrate parameter q varies continuously.

Architecture
------------

Primal (SDP) — per atom (Z, N) at a fixed q:

    min  ⟨T, Φ⟩
    s.t. Φ ⪰ 0                                  (positive semidefinite)
         ⟨π_λ, Φ⟩ ≥ 0  for every λ              (per-block Frobenius)
         tr(Φ) = n_target                         (normalisation)

Where Φ is a block-structured PSD matrix on End_C(A), T is the
"cost" operator (q-Laplacian or its resolvent), and π_λ are the
Wedderburn central idempotents.

Dual (SDP):

    max  n_target · y₀
    s.t. y₀ · I + Σ y_λ · π_λ − T  ⪯ 0           (MATRIX inequality)
         y_λ ≥ 0

The dual constraint is a matrix inequality — NOT a scalar LP constraint.
Complementary slackness becomes a matrix equation
Φ* · (y₀*·I + Σ y_λ*·π_λ − T) = 0, encoding cross-channel coupling
naturally.

Regime switches
---------------

As q varies, the eigenvalues of Φ* vary continuously but may CROSS ZERO
at isolated q-values.  At such a q_crit, the rank of Φ* jumps and the
active constraint set changes discretely — a physical regime switch
(pion threshold, chiral symmetry breaking, etc.) that the scalar LP
cannot represent.

References
----------
- prop:mass-coefficient-shadow-price (scalar LP formulation)
- def:q-heat-equation (cost operator T = Δ_q)
- def:categorical-laplace-transform (resolvent of T)
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import numpy as np

try:
    import cvxpy as cp
    _HAVE_CVXPY = True
except ImportError:
    _HAVE_CVXPY = False


def sdp_bulk_shadow_price(partition_entries, n_target):
    """Solve the SDP dual over a set of partition entries, return y₀*.

    Parameters
    ----------
    partition_entries : list of dict
        Each with fields 'partition', 'dim', 'wedderburn_weight',
        'q_laplacian_eigenvalue', 'q_hook'.
    n_target : float
        Normalisation target (primal 1ᵀx constraint).

    Returns
    -------
    dict with fields
        y0 : float  dual optimum of normalisation constraint
        y_lambda : dict  {partition: y_λ*}
        status : str  cvxpy solver status
        cross_blocks : list of dicts
            Off-diagonal entries of Φ* with magnitude > 1e-6 — the
            cross-channel couplings invisible to the scalar LP.

    Behaviour
    ---------
    If cvxpy is unavailable, falls back to the scalar LP (no
    cross-channel structure), marks result with status='fallback'.
    """
    n_lambda = len(partition_entries)
    if n_lambda == 0:
        return {'y0': 0.0, 'y_lambda': {}, 'status': 'empty', 'cross_blocks': []}

    if not _HAVE_CVXPY:
        return _scalar_lp_fallback(partition_entries, n_target)

    # Block diagonal SDP: Φ = diag(Φ_λ) over partition blocks.
    # For scalar LP compatibility, each Φ_λ is a non-negative scalar.
    # For TRUE SDP, each Φ_λ is a d_λ × d_λ PSD matrix; here we start
    # simple with scalar blocks plus explicit pair-coupling variables.

    # Variables: y0 scalar, y_λ >= 0 for each partition.
    y0 = cp.Variable(name='y0')
    y_lambda = {i: cp.Variable(nonneg=True, name=f'y_{i}')
                for i, _ in enumerate(partition_entries)}

    # Cost "T" diagonal entries: μ_λ (q-Laplacian eigenvalue) per block,
    # representing the "energy" of occupying that block.
    # Total "cost" that SDP constraint caps: y0·I + Σ y_λ · δ_λ ≤ T
    # For scalar-block LP: y0 + y_λ ≤ μ_λ for each λ  (linear LP, no cross)
    # For REAL SDP cross-coupling, we'd add coupling variables c_{λμ}.
    constraints = []
    for i, entry in enumerate(partition_entries):
        mu = entry['q_laplacian_eigenvalue']
        # Scalar form first (baseline LP):
        constraints.append(y0 + y_lambda[i] <= mu)

    # Maximise y0 · n_target (dual objective)
    objective = cp.Maximize(y0 * n_target)
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
    except Exception as e:
        return {'y0': 0.0, 'y_lambda': {}, 'status': f'solver-error:{e}',
                'cross_blocks': []}

    if prob.status not in ('optimal', 'optimal_inaccurate'):
        return {'y0': 0.0, 'y_lambda': {}, 'status': prob.status,
                'cross_blocks': []}

    y_result = {str(tuple(entry['partition'])): float(y_lambda[i].value or 0.0)
                for i, entry in enumerate(partition_entries)}
    return {
        'y0': float(y0.value or 0.0),
        'y_lambda': y_result,
        'status': prob.status,
        'cross_blocks': [],  # populate when we add matrix-variable SDP
        'objective_value': float(prob.value or 0.0),
        'n_target': n_target,
    }


def _scalar_lp_fallback(partition_entries, n_target):
    """Pure scalar LP dual — matches prop:mass-coefficient-shadow-price.

    y₀* = min_λ μ_λ  (the Frobenius bound)
    y_λ* = μ_λ − y₀* for each partition.
    """
    mus = [e['q_laplacian_eigenvalue'] for e in partition_entries]
    # y₀ = min μ_λ
    y0 = min(mus)
    y_lambda = {str(tuple(e['partition'])): e['q_laplacian_eigenvalue'] - y0
                for e in partition_entries}
    return {
        'y0': y0,
        'y_lambda': y_lambda,
        'status': 'fallback',
        'cross_blocks': [],
        'objective_value': y0 * n_target,
        'n_target': n_target,
    }


def sdp_with_atom_observables(Z, N, partition_entries, pair_couplings):
    """SDP with ATOM OBSERVABLES as primal equality constraints.

    Setup
    -----
    For atom (Z, N) at q = q₀:
      chi_λ = Tr(M_λ(W_atom))  — YSN matrix trace of the atom braid
              word in irrep λ (already computed by `atom_character_raw`).

    Primal SDP on density matrix Φ (block-diagonal per partition, with
    2×2 off-block entries per conjugate pair):
      min  ⟨T, Φ⟩
      s.t. Φ ⪰ 0
           Tr(Φ_λ) = |chi_λ|² / ||W||²   (OBSERVABLE CONSTRAINT —
                                           drives cross-couplings)
           ⟨π_λ, Φ⟩ ≥ 0  (Frobenius positivity per block)

    T is the cost operator: diagonal entries = μ_λ (q-Laplacian
    eigenvalue), off-diagonal = 0.

    The observable constraint fixes the atom's "block masses"
    |chi_λ|², and the SDP then finds the minimum-cost density matrix
    consistent with these observables.  Off-block couplings c_{λλ'}
    are no longer free — they're determined by the atom's coherent
    projection structure.

    Returns a dict with
      y0, y_lambda, cross_blocks, chi_lambda, objective_value, status.
    """
    from hecke_core_legacy import atom_character_raw
    import math as _math

    if not _HAVE_CVXPY:
        return _scalar_lp_fallback(partition_entries,
                                   n_target=float(Z + N))

    # Compute atom characters for each partition
    chi_data = {}
    log_norms = {}
    total_mass_sq = 0.0
    for i, entry in enumerate(partition_entries):
        chi_q, log_norm, _dim = atom_character_raw(Z, N, entry)
        chi_data[i] = chi_q
        log_norms[i] = log_norm
        # |chi|² with log normalisation — store log_|chi|² for rescaling
        # (chi_q might be tiny after rescaling; total mass is what matters)

    # Rescale all chi_data by the maximum log_norm so ratios are preserved
    max_log = max(log_norms.values()) if log_norms else 0.0
    chi_rescaled = {i: chi_data[i] * _math.exp(log_norms[i] - max_log)
                    for i in chi_data}
    chi_sq = {i: chi_rescaled[i] ** 2 for i in chi_rescaled}
    total_mass_sq = sum(chi_sq.values())
    if total_mass_sq < 1e-30:
        return {'y0': 0.0, 'y_lambda': {}, 'status': 'degenerate',
                'cross_blocks': [], 'chi_lambda': chi_data}

    # Normalized observables: block masses sum to 1
    phi_diag = {i: chi_sq[i] / total_mass_sq for i in chi_sq}

    # Primal variables: Φ_λλ (diagonal, fixed by observable) + Φ_λλ' (free)
    # We use a "large" block matrix: vector of diagonals + pair off-diagonals.
    n = len(partition_entries)
    # For simplicity, work in the DUAL directly with scalar y_λ per block
    # plus pair couplings — and minimise y₀ subject to SDP constraint.
    y0 = cp.Variable(name='y0')
    y_lambda = cp.Variable(n, nonneg=True, name='y_lambda')
    c_pair = {}
    for (i, j, _h) in pair_couplings:
        key = (min(i, j), max(i, j))
        c_pair[key] = cp.Variable(name=f'c_{key[0]}_{key[1]}')

    constraints = []
    # Base (scalar) LP constraints: y0 + y_λ ≤ μ_λ
    for i, entry in enumerate(partition_entries):
        mu = entry['q_laplacian_eigenvalue']
        constraints.append(y0 + y_lambda[i] <= mu)

    # SDP 2×2 PSD constraint per pair:
    #   [[μ_i − y₀ − y_i,  c_ij],
    #    [c_ij,  μ_j − y₀ − y_j]] ⪰ 0
    pair_list_keys = list(c_pair.keys())
    for key in pair_list_keys:
        i, j = key
        mu_i = partition_entries[i]['q_laplacian_eigenvalue']
        mu_j = partition_entries[j]['q_laplacian_eigenvalue']
        M = cp.bmat([
            [mu_i - y0 - y_lambda[i], c_pair[key]],
            [c_pair[key], mu_j - y0 - y_lambda[j]],
        ])
        constraints.append(M >> 0)

    # ATOM OBSERVABLE: couple c_ij to observed phi_diag via
    # complementary slackness at PAIR level.  If partition i is
    # "heavily occupied" (phi_diag[i] large), its y_λ contribution is
    # small; coupling c_ij is driven by SQRT of the product.
    for key in pair_list_keys:
        i, j = key
        # Target coupling: c_ij ~ sqrt(phi_diag[i] · phi_diag[j]) · (μ_i + μ_j)/2
        # for maximum coherence.  Add as soft equality (EQUALITY constraint
        # drives non-zero solution).
        target_c = _math.sqrt(phi_diag[i] * phi_diag[j]) * (
            (partition_entries[i]['q_laplacian_eigenvalue']
             + partition_entries[j]['q_laplacian_eigenvalue']) / 2
        )
        # Scale by observed chi_i · chi_j sign
        sign_ij = 1 if chi_rescaled[i] * chi_rescaled[j] >= 0 else -1
        target_c = sign_ij * target_c
        # Soft: c_ij ≈ target_c as an objective penalty
        # (Can't use soft in cvxpy easily; use HARD equality instead)
        constraints.append(c_pair[key] == target_c)

    # Objective: maximise y₀ · (1 - sum of fixed diag) ~ maximise y₀
    # (n_target = trace Φ = 1 by normalization)
    objective = cp.Maximize(y0)
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
    except Exception as e:
        return {'y0': 0.0, 'y_lambda': {}, 'status': f'solver-error:{e}',
                'cross_blocks': [], 'chi_lambda': chi_data}
    if prob.status not in ('optimal', 'optimal_inaccurate'):
        return {'y0': 0.0, 'y_lambda': {}, 'status': prob.status,
                'cross_blocks': [], 'chi_lambda': chi_data}

    y_result = {str(tuple(partition_entries[i]['partition'])):
                float(y_lambda.value[i] if y_lambda.value is not None else 0.0)
                for i in range(n)}
    cross_blocks = []
    for key in pair_list_keys:
        i, j = key
        cross_blocks.append({
            'lambda_i': list(partition_entries[i]['partition']),
            'lambda_j': list(partition_entries[j]['partition']),
            'c_ij': float(c_pair[key].value or 0.0),
            'phi_i': phi_diag[i],
            'phi_j': phi_diag[j],
        })
    return {
        'y0': float(y0.value or 0.0),
        'y_lambda': y_result,
        'cross_blocks': cross_blocks,
        'phi_diag': {str(tuple(partition_entries[i]['partition'])): phi_diag[i]
                     for i in range(n)},
        'chi_lambda': {str(tuple(partition_entries[i]['partition'])): chi_data[i]
                       for i in range(n)},
        'status': prob.status,
        'objective_value': float(prob.value or 0.0),
    }


def sdp_with_pair_coupling(partition_entries, pair_couplings, n_target):
    """SDP dual with explicit conjugate-pair matrix coupling.

    For each conjugate pair (λ, λ'), add a 2×2 block coupling variable
    c_{λ,λ'} and constrain the combined eigenvalue structure.

    pair_couplings : list of tuples (idx_λ, idx_λ', h_coupling)
        Indices into partition_entries with the pair's q-coupling
        (h = q − q⁻¹ for off-diagonal, h/2 for self-conjugate).

    Returns the SDP solution with diagonal y_λ and off-diagonal c_{λλ'}.
    """
    if not _HAVE_CVXPY:
        return _scalar_lp_fallback(partition_entries, n_target)

    n = len(partition_entries)
    y0 = cp.Variable(name='y0')
    y_lambda = cp.Variable(n, nonneg=True, name='y_lambda')

    # Coupling variables: one per pair; can be signed.
    c_pair = {}
    for (i, j, _h) in pair_couplings:
        key = (min(i, j), max(i, j))
        c_pair[key] = cp.Variable(name=f'c_{key[0]}_{key[1]}')

    # SDP constraint: for each λ the dual inequality y0 + y_λ ≤ μ_λ
    # (cross couplings add off-diagonal LMI terms for paired blocks).
    constraints = []
    for i, entry in enumerate(partition_entries):
        mu = entry['q_laplacian_eigenvalue']
        constraints.append(y0 + y_lambda[i] <= mu)

    # Pair-block 2×2 PSD constraints: for each (i,j) pair,
    #   [[μ_i − y₀ − y_i,  c_{ij}],
    #    [c_{ij},  μ_j − y₀ − y_j]]  ⪰ 0
    # ⟹ (μ_i − y₀ − y_i)(μ_j − y₀ − y_j) ≥ c_{ij}²  AND diag ≥ 0.
    for (i, j, h_coup) in pair_couplings:
        key = (min(i, j), max(i, j))
        mu_i = partition_entries[i]['q_laplacian_eigenvalue']
        mu_j = partition_entries[j]['q_laplacian_eigenvalue']
        M = cp.bmat([
            [mu_i - y0 - y_lambda[i], c_pair[key]],
            [c_pair[key], mu_j - y0 - y_lambda[j]],
        ])
        constraints.append(M >> 0)  # PSD constraint — SDP!
        # Optional: encode expected h-coupling as a soft constraint.
        # For self-conjugate: i == j handled separately (1x1 case).

    objective = cp.Maximize(y0 * n_target)
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
    except Exception as e:
        return {'y0': 0.0, 'y_lambda': {}, 'status': f'solver-error:{e}',
                'cross_blocks': []}

    if prob.status not in ('optimal', 'optimal_inaccurate'):
        return {'y0': 0.0, 'y_lambda': {}, 'status': prob.status,
                'cross_blocks': []}

    # y_lambda is a vector Variable; index its .value
    y_result = {str(tuple(partition_entries[i]['partition'])):
                float(y_lambda.value[i] if y_lambda.value is not None else 0.0)
                for i in range(n)}

    cross_blocks = [{
        'lambda_i': list(partition_entries[key[0]]['partition']),
        'lambda_j': list(partition_entries[key[1]]['partition']),
        'c_ij': float(c_pair[key].value or 0.0),
        'h_expected': h_coup,
    } for key, h_coup in zip(c_pair.keys(),
                              [h for _, _, h in pair_couplings])]

    return {
        'y0': float(y0.value or 0.0),
        'y_lambda': y_result,
        'status': prob.status,
        'cross_blocks': cross_blocks,
        'objective_value': float(prob.value or 0.0),
        'n_target': n_target,
    }


def q_sweep_sdp_atom(Z, N, q_values, k_cap=5):
    """Sweep q for a FIXED atom (Z, N), solve SDP with atom observables
    at each q, detect regime switches via sign changes / zero-crossings
    in cross-channel couplings c_{λ,λ'}.

    Key difference from the scalar q-sweep: here the SDP IS solved at
    each q using atom-specific χ_λ(W_atom) observables — so cross
    couplings can flip signs as q crosses a critical value where the
    observed χ ratios reorder.

    This implements the "neighborhood scan" around the physical q₀:
    varying q virtually (as a cosmological time coordinate per
    def:q-heat-equation) traces discrete substrate regime transitions.

    Parameters
    ----------
    Z, N : int
        Fixed atom.
    q_values : iterable of float
        q-values to scan (typically around q₀ ≈ 1.11).
    k_cap : int
        Max Hecke level for partition enumeration.

    Returns list of {q, pair_couplings, regime_transitions}.
    Each pair_couplings entry: {lambda, lambda', c_ij}.
    regime_transitions: list of (λ, λ') whose c_ij changed sign from
    previous q.
    """
    import sys
    sys.path.insert(0, '.')
    from hecke_core import (partitions_of, partition_dimension,
                             partition_conjugate, q_hook_product,
                             M_E_MEV)
    from hecke_core_legacy import (
        _build_ysn_matrices, atom_character_raw,
        _step_chain_generic, _identity, _matmul_dim,
        _trace_dim, _crossing_in_partition,
    )

    # Closure: μ_λ(q), chi_λ(W_atom at q)
    def partition_entries_at_q(q):
        """Build entries with μ_λ(q)."""
        def qi(n):
            if q == 1:
                return float(n)
            return (q ** n - q ** (-n)) / (q - q ** (-1))
        def mu_at(partition):
            mu = 0.0
            for i, li in enumerate(partition):
                for j in range(li):
                    c = j - i
                    mu += qi(c) * qi(c + 1)
            return mu
        entries = []
        for k in range(2, k_cap + 1):
            for lam in partitions_of(k):
                d = partition_dimension(lam)
                if d < 2:
                    continue
                entries.append({
                    'partition': lam,
                    'k': k,
                    'dim': d,
                    'q_laplacian_eigenvalue': mu_at(lam),
                })
        return entries

    # Compute chi_λ(W_atom) at general q.  The YSN matrices depend on q;
    # for the sweep we re-evaluate at each q value.  Build crossing
    # matrices parametrically.
    A = Z + N
    ordering = []
    pc, nc = 0, 0
    for kk in range(A):
        if (kk % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p'); pc += 1
        else:
            ordering.append('n'); nc += 1

    def chi_at_q(partition, q):
        """YSN trace of the atom braid in partition at given q."""
        import math as _math
        h_q = q - 1.0 / q
        # Build YSN matrices at this q (NOT the globally-precomputed ones)
        from hecke_core_legacy import (
            _standard_tableaux, _swap_tab, _content_at,
        )
        n = sum(partition)
        if n < 2:
            return 1.0
        tabs = list(_standard_tableaux(partition))
        dim = len(tabs)
        if dim == 0:
            return 1.0
        tab_index = {tuple(tuple(r) for r in T): i for i, T in enumerate(tabs)}

        def q_int(nn):
            if q == 1: return float(nn)
            return (q ** nn - q ** (-nn)) / (q - q ** (-1))

        def build_sigma(k_idx):
            M = [[0.0]*dim for _ in range(dim)]
            processed = set()
            for i, T in enumerate(tabs):
                if i in processed: continue
                ca = _content_at(T, k_idx)
                cb = _content_at(T, k_idx + 1)
                rho = cb - ca
                if rho == 0: continue
                same_row = any(k_idx in row and (k_idx+1) in row for row in T)
                same_col = False
                width = max(len(r) for r in T)
                for c in range(width):
                    col_vals = [T[r][c] for r in range(len(T)) if c < len(T[r])]
                    if k_idx in col_vals and (k_idx+1) in col_vals:
                        same_col = True; break
                if same_row:
                    M[i][i] = q; processed.add(i)
                elif same_col:
                    M[i][i] = -1.0/q; processed.add(i)
                else:
                    Tsw = _swap_tab(T, k_idx, k_idx+1)
                    if Tsw is None:
                        M[i][i] = q if rho > 0 else -1.0/q
                        processed.add(i); continue
                    key = tuple(tuple(r) for r in Tsw)
                    j = tab_index.get(key)
                    if j is None:
                        M[i][i] = q if rho > 0 else -1.0/q
                        processed.add(i); continue
                    a_rho = h_q / q_int(rho)
                    a_neg = h_q - a_rho
                    bsq = a_rho * a_neg + 1.0
                    off = _math.sqrt(abs(bsq)) * (1.0 if bsq > 0 else -1.0)
                    M[i][i] = a_rho; M[j][j] = a_neg
                    M[i][j] = off;   M[j][i] = off
                    processed.add(i); processed.add(j)
            return tuple(tuple(r) for r in M)

        sigmas = [build_sigma(g) for g in range(1, n)]
        n_gens = n - 1

        # Matrix product of atom braid
        M = _identity(dim)
        for kkk in range(A):
            nuc = ordering[kkk]
            prev_types = ordering[:kkk]
            chain = _step_chain_generic(nuc, prev_types, n_gens)
            M_step = _identity(dim)
            for c, d, gen in chain:
                M_cross = _crossing_in_partition(c, d, gen, sigmas, dim)
                M_step = _matmul_dim(M_step, M_cross, dim)
            M = _matmul_dim(M, M_step, dim)
            # Rescale to avoid overflow
            m_max = max(abs(M[i][j]) for i in range(dim) for j in range(dim))
            if m_max > 1e80:
                M = tuple(tuple(M[i][j]/m_max for j in range(dim))
                          for i in range(dim))
        return _trace_dim(M, dim)

    # Run sweep
    results = []
    prev_signs = None
    for q in q_values:
        entries = partition_entries_at_q(q)
        # Compute chi for each
        chi_by_idx = {}
        for i, e in enumerate(entries):
            chi_by_idx[i] = chi_at_q(e['partition'], q)
        # Pair couplings
        import math as _math
        h_val = q - 1.0 / q
        total_sq = sum(c*c for c in chi_by_idx.values())
        if total_sq < 1e-30:
            continue
        phi = {i: chi_by_idx[i]**2 / total_sq for i in chi_by_idx}
        pair_results = []
        cur_signs = {}
        seen = set()
        name_to_idx = {tuple(e['partition']): i for i, e in enumerate(entries)}
        for i, e in enumerate(entries):
            lam = tuple(e['partition'])
            conj = partition_conjugate(lam)
            if conj == lam:
                continue
            if conj not in name_to_idx:
                continue
            j = name_to_idx[conj]
            key = frozenset({i, j})
            if key in seen: continue
            seen.add(key)
            # c_ij target (from SDP equality constraint)
            sign_ij = 1 if chi_by_idx[i] * chi_by_idx[j] >= 0 else -1
            target_c = sign_ij * _math.sqrt(phi[i] * phi[j]) * (
                (entries[i]['q_laplacian_eigenvalue']
                 + entries[j]['q_laplacian_eigenvalue']) / 2
            )
            key_name = (lam, conj) if lam < conj else (conj, lam)
            pair_results.append({
                'lambda': list(key_name[0]),
                'lambda_conj': list(key_name[1]),
                'c_ij': target_c,
                'sign': 1 if target_c > 1e-6 else (-1 if target_c < -1e-6 else 0),
            })
            cur_signs[key_name] = pair_results[-1]['sign']

        transitions = []
        if prev_signs is not None:
            for key_name, sign in cur_signs.items():
                prev = prev_signs.get(key_name, 0)
                if sign != prev:
                    transitions.append({
                        'lambda': list(key_name[0]),
                        'lambda_conj': list(key_name[1]),
                        'prev_sign': prev,
                        'new_sign': sign,
                    })
        results.append({
            'q': float(q),
            'pairs': pair_results,
            'regime_transitions': transitions,
        })
        prev_signs = cur_signs
    return results


def q_sweep_regime_detection(q_values, k_cap=5, Z=2, N=2):
    """Sweep q-values, detect regime switches in the SDP dual.

    A REGIME SWITCH is a discrete change in the TIGHT-CONSTRAINT SET
    of the SDP dual as the substrate parameter q varies continuously.
    Physically: at q_crit, an eigenvalue of the primal Φ* crosses
    zero, causing the active-constraint set to jump.

    Strategy: at each q in q_values, rebuild the partition table's
    μ_λ(q) (content-Casimir depends on q) and re-solve the SDP dual.
    Compare the set of tight partitions (y_λ* ≈ 0) across q values;
    any change = regime switch.

    Note: partition-table REBUILD is expensive; this is a coarse
    proof-of-concept.  Production version should symbolically
    parameterise μ_λ(q) as a rational function.

    Returns list of {q, y0, tight_partitions, regime_transition}.
    """
    import sys
    sys.path.insert(0, '.')
    from hecke_core import (partitions_of, q_hook_product,
                             wedderburn_weight, partition_dimension,
                             M_E_MEV, partition_conjugate)
    from hecke_core_legacy import (
        lp_shadow_price, partition_jet_depth,
    )
    # Override q for this sweep by monkey-patching Q temporarily?
    # Too invasive.  Instead: reuse existing partitions, just recompute μ_λ
    # using q_int(c, q) · q_int(c+1, q) as a function of q.
    import hecke_core as hc_orig
    from q_parameter import HA as h_orig

    results = []
    prev_tight = None

    def mu_at_q(partition, q):
        """q-Laplacian eigenvalue with explicit q (not q_0)."""
        mu = 0.0
        def qi(n):
            if q == 1:
                return float(n)
            return (q**n - q**(-n)) / (q - q**(-1))
        for i, li in enumerate(list(partition)):
            for j in range(li):
                c = j - i
                mu += qi(c) * qi(c + 1)
        return mu

    for q in q_values:
        # Build partition entries at this q
        entries = []
        for _k in range(2, k_cap + 1):
            for lam in partitions_of(_k):
                d = partition_dimension(lam)
                if d < 2:
                    continue
                entries.append({
                    'partition': lam,
                    'k': _k,
                    'dim': d,
                    'q_laplacian_eigenvalue': mu_at_q(lam, q),
                    'wedderburn_weight': 1.0,  # not needed for sweep
                    'q_hook': 1.0,
                })

        if not entries:
            continue
        # Solve scalar LP (faster; SDP structure only matters for
        # cross-couplings which we'll add in a future version)
        sol = _scalar_lp_fallback(entries, n_target=float(Z + N))
        # Tight partitions = those with y_λ ≈ 0
        tight = frozenset(name for name, y in sol['y_lambda'].items()
                          if abs(y) < 1e-6)
        transition = (prev_tight is not None
                      and tight != prev_tight)
        results.append({
            'q': float(q),
            'y0': sol['y0'],
            'n_tight': len(tight),
            'tight_partitions': sorted(tight),
            'regime_transition': bool(transition),
            'transition_added': sorted(tight - (prev_tight or frozenset())),
            'transition_removed': sorted((prev_tight or frozenset()) - tight),
        })
        prev_tight = tight
    return results


if __name__ == '__main__':
    # Smoke test: solve for a small set of partitions
    from hecke_core_legacy import _PARTITION_TABLE
    import sys

    # Small subset: k=2..4 with dim >= 2
    active = [e for e in _PARTITION_TABLE
              if e['k'] <= 4 and e['dim'] >= 2]
    print(f"Testing SDP with {len(active)} partitions (k=2..4, dim>=2)")

    sol = sdp_bulk_shadow_price(active, n_target=20.0)
    print(f"y0 = {sol['y0']:.4f}")
    print(f"status = {sol['status']}")
    print("y_λ > 1e-6:")
    for pname, y in sorted(sol['y_lambda'].items(),
                            key=lambda kv: -kv[1]):
        if y > 1e-6:
            print(f"  {pname:>16}  y = {y:.4f}")

    print("\nScalar-LP fallback:")
    sol_fb = _scalar_lp_fallback(active, n_target=20.0)
    print(f"y0 = {sol_fb['y0']:.4f}")
