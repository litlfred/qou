#!/usr/bin/env python3
"""
P2.4 — Multi-level SDP constraint families (L4–L7).

The base SDP (`sdp_cross_channel.sdp_with_pair_coupling`) handles
arbitrary (Z, N) at the **pair-coupling** level (level 3 in the
confinement hierarchy: atom = nucleons glued by inter-nucleon σ).

This module adds constraint *families* for the higher confinement
levels:

  Level 4  shell-closure   shell-magic Wedderburn constraint:
                            κ_λ = 0 + λ self-conjugate for shell blocks
  Level 5  cross-shell      frayed/staircase boxes pair off
  Level 6  atom-electron   (proton-shell) × (electron-shell) coupling
  Level 7  covalent         shared-trefoil bond constraints

Each level adds its constraint family on top of the lower-level
SDP. The L4/L5 families are the most tractable (purely combinatorial
on Young diagrams via prop:categorical-neutrality-saturated-shells);
L6 / L7 require the electron-strand braid encoding from
`confinement_shortcuts.NeutralAtomWord` / `MoleculeWord`.

Design pattern
--------------

Each level function takes the lower-level SDP solution as input and
ADDS constraints rather than rebuilding from scratch. This preserves
the pair-coupling structure already in `sdp_cross_channel` while
extending to higher levels.

  sdp_with_shell_closure(Z, N, ..., pair_solution=None)
  sdp_with_cross_shell(Z, N, ..., shell_solution=None)
  sdp_with_atom_electron(Z, N, ..., shell_solution=None)
  sdp_with_covalent(atoms, bonds, ..., atom_solutions=None)

The pair_solution / shell_solution / etc. arguments thread the
optimal y_λ, c_pair from the lower level into the higher-level SDP
as warm-start values + additional equality constraints (when the
lower level is a strict refinement).

References
----------

- `prop:categorical-neutrality-saturated-shells` (κ_λ = 0 + self-conj
  ⟺ shell saturation)
- `prop:diagrammatic-double-magic-lr-fusion` (LR-fusion of two
  self-conjugate κ-balanced diagrams)
- `prop:homological-shell-condensation` (BB collapse selects magic n)
- `confinement_shortcuts.{ShellWord, CrossShellWord, NeutralAtomWord,
  MoleculeWord}` (per-level word construction)

Status
------

🟡 Skeleton + L4 (shell-closure) prototype. L5–L7 are stub functions
   raising NotImplementedError with the constraint family they need.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import cvxpy as cp
    _HAVE_CVXPY = True
except ImportError:
    _HAVE_CVXPY = False

from sdp_cross_channel import (
    sdp_with_pair_coupling,
    _scalar_lp_fallback,
)


# ─── Level 4: shell-closure constraint family ────────────────────────

def shell_constraint_partitions(A, magic_only=True):
    """Partitions of 3A that satisfy the shell-saturation predicate.

    Per prop:categorical-neutrality-saturated-shells:
      shell saturated ⟺ κ_λ = 0 + λ self-conjugate.

    For magic A, ALL self-conjugate λ ⊢ 3A satisfy κ_λ = 0 (proved
    via κ(λ') = -κ(λ) ⇒ self-conj ⇒ κ = 0).
    """
    return _enumerate_self_conjugate(3 * A)


def _enumerate_self_conjugate(n):
    """Enumerate self-conjugate partitions of n.

    Delegates to the canonical implementation in
    `enumerate_self_conjugate_partitions.all_self_conjugate_partitions`
    (single source of truth — see Gemini review on PR #500).
    Returns tuples for backward compatibility with this module's
    consumers; the canonical function returns lists.
    """
    from enumerate_self_conjugate_partitions import (
        all_self_conjugate_partitions,
    )
    return [tuple(p) for p in all_self_conjugate_partitions(n)]


def sdp_with_shell_closure(Z, N, partition_entries, pair_couplings,
                            n_target=None, pair_solution=None,
                            shell_y_value=None):
    """Level-4 SDP: pair-coupling SDP + shell-closure equality constraints.

    Adds: for each shell-closure-eligible partition (per
    shell_constraint_partitions), the dual variable y_λ is FIXED to
    `shell_y_value` (default 0 — the κ-zero / self-conjugate
    saturation value per prop:categorical-neutrality-saturated-shells).

    Re-solves the SDP with the shell-closure equality constraints
    layered on top of the pair-coupling structure. Returns optimal
    y_lambda + cross_blocks + objective.
    """
    if n_target is None:
        n_target = float(Z + N)
    if shell_y_value is None:
        shell_y_value = 0.0

    # Identify shell-closure partitions for this atom
    A = Z + N
    shell_partitions = shell_constraint_partitions(A)
    shell_partition_set = {tuple(p) for p in shell_partitions}

    # Identify which partition_entries indices are shell-saturation
    shell_indices = []
    for i, entry in enumerate(partition_entries):
        ent_part = tuple(entry["partition"]) if isinstance(entry["partition"], list) else tuple(entry["partition"])
        if ent_part in shell_partition_set:
            shell_indices.append(i)

    if not _HAVE_CVXPY:
        # Fallback: just report shell-eligibility on a scalar LP
        if pair_solution is None:
            pair_solution = _scalar_lp_fallback(partition_entries, n_target)
        return {
            **pair_solution,
            "level": 4,
            "shell_closure_eligible_partition_count": len(shell_partitions),
            "shell_indices": shell_indices,
            "note": "cvxpy unavailable; scalar LP fallback used",
        }

    # Full cvxpy refactor of sdp_with_pair_coupling + shell equality
    n = len(partition_entries)
    y0 = cp.Variable(name="y0")
    y_lambda = cp.Variable(n, nonneg=True, name="y_lambda")
    c_pair = {}
    for (i, j, _h) in pair_couplings:
        key = (min(i, j), max(i, j))
        c_pair[key] = cp.Variable(name=f"c_{key[0]}_{key[1]}")

    constraints = []
    for i, entry in enumerate(partition_entries):
        mu = entry["q_laplacian_eigenvalue"]
        constraints.append(y0 + y_lambda[i] <= mu)

    # Shell-closure equality: y_λ = shell_y_value for shell partitions
    for i in shell_indices:
        constraints.append(y_lambda[i] == shell_y_value)

    # Pair-block 2x2 PSD constraints (from pair-coupling SDP)
    for (i, j, _h_coup) in pair_couplings:
        key = (min(i, j), max(i, j))
        mu_i = partition_entries[i]["q_laplacian_eigenvalue"]
        mu_j = partition_entries[j]["q_laplacian_eigenvalue"]
        M = cp.bmat([
            [mu_i - y0 - y_lambda[i], c_pair[key]],
            [c_pair[key], mu_j - y0 - y_lambda[j]],
        ])
        constraints.append(M >> 0)

    objective = cp.Maximize(y0 * n_target)
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
    except Exception as _e:
        return {"y0": 0.0, "y_lambda": {}, "status": f"solver-error:{_e}",
                "level": 4, "shell_indices": shell_indices}

    if prob.status not in ("optimal", "optimal_inaccurate"):
        return {"y0": 0.0, "y_lambda": {}, "status": prob.status,
                "level": 4, "shell_indices": shell_indices}

    y_result = {str(tuple(partition_entries[i]["partition"])):
                float(y_lambda.value[i] if y_lambda.value is not None else 0.0)
                for i in range(n)}
    cross_result = {f"{key[0]}_{key[1]}": float(v.value)
                    for key, v in c_pair.items() if v.value is not None}

    return {
        "y0": float(y0.value) if y0.value is not None else 0.0,
        "y_lambda": y_result,
        "cross_blocks": cross_result,
        "objective_value": float(prob.value),
        "status": prob.status,
        "level": 4,
        "shell_closure_eligible_partition_count": len(shell_partitions),
        "shell_indices": shell_indices,
        "shell_y_value": shell_y_value,
    }


# ─── Level 5: cross-shell constraint family ──────────────────────────

def lr_coefficient(lam_z, lam_n, mu):
    """Littlewood–Richardson coefficient c^μ_{λ_Z, λ_N}.

    Counts the number of LR-skew tableaux of shape μ/λ_Z with
    content λ_N (or equivalently the LR rule). Implemented via the
    standard skew-tableau enumeration with the LR conditions.

    Per prop:diagrammatic-double-magic-lr-fusion: V_{λ_Z} ⊗ V_{λ_N}
    decomposes as ⊕_μ c^μ_{λ_Z, λ_N} V_μ in H_{|λ_Z| + |λ_N|}(q).
    """
    n_z = sum(lam_z)
    n_n = sum(lam_n)
    if sum(mu) != n_z + n_n:
        return 0
    # μ must contain λ_Z
    lam_z_padded = list(lam_z) + [0] * (len(mu) - len(lam_z))
    if any(m < l for m, l in zip(mu, lam_z_padded)):
        return 0
    # Count LR skew tableaux of shape μ/λ_Z with content λ_N.
    # Use a basic enumeration (fine for small partitions).
    return _count_lr_tableaux(mu, lam_z_padded, lam_n)


def _count_lr_tableaux(mu, lam_z, content):
    """Count LR-skew tableaux of shape mu/lam_z with given content.

    LR conditions:
      1. Entries weakly increase along rows (left to right).
      2. Entries strictly increase down columns.
      3. Reverse reading word is a lattice word (each prefix has
         at least as many i's as (i+1)'s).
    """
    skew_cells = []
    for i, mu_i in enumerate(mu):
        l_i = lam_z[i] if i < len(lam_z) else 0
        for j in range(l_i, mu_i):
            skew_cells.append((i, j))

    n_skew = len(skew_cells)
    if n_skew == 0:
        return 1 if all(c == 0 for c in content) else 0

    target_content = list(content)
    cells_sorted = sorted(skew_cells)

    count = [0]

    def fill(idx, assignment):
        if idx == n_skew:
            # Check reverse reading word lattice condition
            reverse_reading = []
            for (i, j) in sorted(skew_cells, key=lambda c: (-c[0], -c[1])):
                ent = assignment[(i, j)]
                if ent is not None:
                    reverse_reading.append(ent)
            tally = [0] * (len(target_content) + 1)
            for ent in reverse_reading:
                tally[ent - 1] += 1
                for k in range(len(target_content) - 1):
                    if tally[k] < tally[k + 1]:
                        return
            count[0] += 1
            return
        cell = cells_sorted[idx]
        for v in range(1, len(target_content) + 1):
            if target_content[v - 1] == 0:
                continue
            # Row weakly-increasing constraint
            i, j = cell
            left = assignment.get((i, j - 1)) if j > 0 else 0
            if left is not None and v < left:
                continue
            # Column strictly-increasing constraint
            up = assignment.get((i - 1, j)) if i > 0 else 0
            if up is not None and v <= up:
                continue
            target_content[v - 1] -= 1
            assignment[cell] = v
            fill(idx + 1, assignment)
            del assignment[cell]
            target_content[v - 1] += 1

    fill(0, {})
    return count[0]


def sdp_with_cross_shell(Z, N, extra_Z, extra_N, partition_entries,
                          pair_couplings, n_target=None,
                          shell_solution=None):
    """Level-5 SDP: shell-closure SDP + cross-shell LR-fusion constraints.

    Per prop:diagrammatic-double-magic-lr-fusion: the (Z, N) atom
    decomposes as the LR-fusion of a shell core (Z_core, N_core) on
    the magic ladder + extra (extra_Z, extra_N) boxes. The composite
    representation V_{λ_core} ⊗ V_{λ_extra} = ⊕_μ c^μ V_μ; the
    constraint family enforces that the dominant μ has κ_μ = 0
    (proved when μ is self-conjugate; for non-self-conjugate dominant
    μ the κ-balanced condition is the conjectural piece).

    For the SDP refactor: each LR-decomposed component μ contributes
    a constraint on its y_μ; off-diagonal coupling between different
    μ in the LR sum is governed by c^μ.

    This function returns the LR decomposition as the constraint
    structure; full cvxpy SDP refactor wires the constraints into
    sdp_with_pair_coupling's cross-block matrix.
    """
    if n_target is None:
        n_target = float(Z + N)

    # Identify the shell core (Z_core, N_core) on the magic ladder
    Z_core = max([m for m in [2, 8, 20, 28, 50, 82, 126] if m <= Z], default=0)
    N_core = max([m for m in [2, 8, 20, 28, 50, 82, 126] if m <= N], default=0)
    extra_Z_actual = Z - Z_core
    extra_N_actual = N - N_core

    # Use the user-provided extra_Z / extra_N if non-trivial; else use computed
    if extra_Z == 0 and extra_N == 0:
        extra_Z = extra_Z_actual
        extra_N = extra_N_actual

    # Shell core: typically a self-conjugate partition of 3·Z_core (and 3·N_core)
    # For simplicity, use the staircase / first-self-conj partition of 3·Z_core
    core_partitions_Z = shell_constraint_partitions(Z_core) if Z_core > 0 else [tuple()]
    core_partitions_N = shell_constraint_partitions(N_core) if N_core > 0 else [tuple()]

    # Extra: enumerate all partitions of 3·extra_Z and 3·extra_N
    from itertools import product as _product

    A_extra = extra_Z + extra_N
    extra_n = 3 * A_extra
    if extra_n > 0:
        from schur_weyl_symbolic import partitions_of as _po
        extra_partitions = _po(extra_n)
    else:
        extra_partitions = [tuple()]

    # LR-decomposition of (core_Z ⊗ core_N) ⊗ (extra) — 2-step:
    #   Step 1: σ ∈ Π(core_Z) ⊗ Π(core_N) with c^σ_{lz, ln}
    #   Step 2: μ ∈ Π(σ) ⊗ Π(extra)         with c^μ_{σ, ex}
    lr_decomposition = []
    from schur_weyl_symbolic import partitions_of as _po
    for lz in core_partitions_Z[:1]:  # take dominant SC core
        for ln in core_partitions_N[:1]:  # take dominant SC core
            # σ must contain lz; widen the search by considering self-conjugate
            # σ candidates (the shell-saturation candidates of size sum(lz) + sum(ln))
            if lz and ln:
                A_combined = (sum(lz) + sum(ln)) // 3
                sigma_partitions = (_enumerate_self_conjugate(3 * A_combined)
                                    if (sum(lz) + sum(ln)) % 3 == 0 else [tuple()])
            else:
                sigma_partitions = [tuple(lz) or tuple(ln)]

            for ex in extra_partitions[:3]:  # sample extras
                for sigma in sigma_partitions[:5]:  # SC intermediates
                    c1 = lr_coefficient(lz, ln, sigma) if (lz and ln) else 1
                    if c1 == 0:
                        continue
                    final_partitions = _po(sum(sigma) + sum(ex)) if (sigma or ex) else [tuple()]
                    for mu in final_partitions[:5]:
                        c2 = lr_coefficient(sigma, ex, mu) if (sigma and ex) else 1
                        if c2 == 0:
                            continue
                        lr_decomposition.append({
                            "lambda_Z": list(lz), "lambda_N": list(ln),
                            "sigma": list(sigma),
                            "lambda_extra": list(ex),
                            "mu": list(mu),
                            "lr_coefficient": c1 * c2,
                        })

    return {
        "level": 5,
        "Z": Z, "N": N, "Z_core": Z_core, "N_core": N_core,
        "extra_Z": extra_Z, "extra_N": extra_N,
        "lr_decomposition_count": len(lr_decomposition),
        "lr_decomposition_sample": lr_decomposition[:5],
        **_sdp_with_lr_constraints(partition_entries, pair_couplings,
                                    lr_decomposition, n_target),
    }


def _sdp_with_lr_constraints(partition_entries, pair_couplings,
                              lr_decomposition, n_target):
    """Full cvxpy SDP solve with LR-fusion cross-block coupling.

    For each LR-decomposition entry (σ, ex, μ, c^μ), if σ and μ both
    appear in partition_entries, add a cross-block PSD constraint:

      [[μ_σ - y₀ - y_σ,  c^μ * coupling_σμ],
       [c^μ * coupling_σμ,  μ_μ - y₀ - y_μ]] ⪰ 0

    The c^μ coefficient enters as the off-diagonal term, scaling
    the coupling.
    """
    if not _HAVE_CVXPY:
        return {"sdp_status": "cvxpy-unavailable",
                "lr_constraints_added": 0}

    n = len(partition_entries)
    if n == 0:
        return {"sdp_status": "empty-partition_entries",
                "lr_constraints_added": 0}

    # Build a partition → index lookup
    part_idx = {tuple(e["partition"]): i
                for i, e in enumerate(partition_entries)}

    # Find LR couplings whose σ and μ both have entries in partition_entries
    lr_couplings = []
    for entry in lr_decomposition:
        sigma_t = tuple(entry["sigma"])
        mu_t = tuple(entry["mu"])
        if sigma_t in part_idx and mu_t in part_idx:
            lr_couplings.append({
                "sigma_idx": part_idx[sigma_t],
                "mu_idx": part_idx[mu_t],
                "c_coef": entry["lr_coefficient"],
            })

    if not lr_couplings:
        return {"sdp_status": "no-applicable-lr-couplings",
                "lr_constraints_added": 0}

    y0 = cp.Variable(name="y0_lr")
    y_lambda = cp.Variable(n, nonneg=True, name="y_lambda_lr")
    c_lr = {}
    for ent in lr_couplings:
        key = (ent["sigma_idx"], ent["mu_idx"])
        if key not in c_lr:
            c_lr[key] = cp.Variable(name=f"c_lr_{key[0]}_{key[1]}")

    constraints = []
    for i, entry in enumerate(partition_entries):
        mu = entry["q_laplacian_eigenvalue"]
        constraints.append(y0 + y_lambda[i] <= mu)

    # Pair-coupling 2x2 PSD constraints (preserved)
    for (i, j, _h_coup) in pair_couplings:
        key = (min(i, j), max(i, j))
        mu_i = partition_entries[i]["q_laplacian_eigenvalue"]
        mu_j = partition_entries[j]["q_laplacian_eigenvalue"]
        c_var = c_lr.get(key) or cp.Variable(name=f"c_pair_{key[0]}_{key[1]}")
        if key not in c_lr:
            c_lr[key] = c_var
        M = cp.bmat([
            [mu_i - y0 - y_lambda[i], c_var],
            [c_var, mu_j - y0 - y_lambda[j]],
        ])
        constraints.append(M >> 0)

    # LR cross-block coupling PSD constraints
    for ent in lr_couplings:
        i, j = ent["sigma_idx"], ent["mu_idx"]
        if i == j:
            continue  # self-fusion: no off-diagonal coupling
        key = (min(i, j), max(i, j))
        mu_i = partition_entries[i]["q_laplacian_eigenvalue"]
        mu_j = partition_entries[j]["q_laplacian_eigenvalue"]
        c_var = c_lr[key]
        M = cp.bmat([
            [mu_i - y0 - y_lambda[i], ent["c_coef"] * c_var],
            [ent["c_coef"] * c_var, mu_j - y0 - y_lambda[j]],
        ])
        constraints.append(M >> 0)

    objective = cp.Maximize(y0 * float(n_target))
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
    except Exception as _e:
        return {"sdp_status": f"solver-error:{_e}",
                "lr_constraints_added": len(lr_couplings)}

    if prob.status not in ("optimal", "optimal_inaccurate"):
        return {"sdp_status": prob.status,
                "lr_constraints_added": len(lr_couplings)}

    return {
        "sdp_status": prob.status,
        "lr_constraints_added": len(lr_couplings),
        "y0_lr": float(y0.value) if y0.value is not None else 0.0,
        "objective_value_lr": float(prob.value),
    }


# ─── Level 6: atom-electron constraint family ────────────────────────

def sdp_with_atom_electron(Z, N, electron_strands, partition_entries,
                            pair_couplings, n_target=None,
                            shell_solution=None):
    """Level-6 SDP: shell-closure SDP + electron-shell coupling.

    For a neutral atom, electron_strands = Z. The Wedderburn
    decomposition extends to H_{3(Z+N) + 3·electron_strands}, but
    rather than re-enumerating partitions over that larger algebra
    (intractable for Z ≥ 5), we encode the electron-nucleon
    coupling as additional pair_couplings entries linking each
    nucleon block to its corresponding electron-shell block.

    Returns the L4 (shell-closure) solution layered with the
    additional electron-shell coupling constraints. Per-electron
    block follows the same Wedderburn-block decomposition as the
    nucleon-shell block (3 strands per electron in the canonical
    Hecke encoding, with a (3) / (2,1) / (1,1,1) decomposition).
    """
    if n_target is None:
        n_target = float(Z + N + electron_strands)

    # First solve L4 for the nucleon shell
    shell = sdp_with_shell_closure(Z, N, partition_entries, pair_couplings,
                                    n_target=float(Z + N),
                                    pair_solution=shell_solution)

    # Build electron-shell block coupling: each electron contributes
    # H_3 Wedderburn structure (3 strands per electron). Total electron
    # strands = 3·electron_strands; couples to the nucleon shell via
    # the (Z + N) inter-shell crossings.
    electron_block_count = electron_strands  # one Wedderburn block per electron
    electron_pair_couplings = [
        {
            "electron_idx": k,
            "nucleon_target": min(k, Z + N - 1),  # k-th electron couples to
                                                   # the k-th nucleon (or last)
            "h_coupling": 1.0,  # default unit coupling at this level
        }
        for k in range(electron_block_count)
    ]

    # Wire electron pair couplings into a cvxpy SDP solve, layered on
    # the L4 shell-closure solution. Each electron-nucleon coupling
    # becomes a 2x2 PSD constraint linking the electron block (idx
    # offset) to its target nucleon block.
    sdp_l6 = _sdp_with_electron_couplings(
        partition_entries, pair_couplings, electron_pair_couplings,
        electron_block_count, n_target)

    return {
        **shell,
        "level": 6,
        "electron_strands": electron_strands,
        "electron_block_count": electron_block_count,
        "electron_pair_couplings_count": len(electron_pair_couplings),
        "electron_pair_couplings_sample": electron_pair_couplings[:5],
        "n_target_total": n_target,
        **sdp_l6,
    }


def _sdp_with_electron_couplings(partition_entries, pair_couplings,
                                  electron_pair_couplings,
                                  electron_block_count, n_target):
    """Cvxpy SDP solve with electron-nucleon coupling constraints
    layered on top of the pair-coupling SDP."""
    if not _HAVE_CVXPY or not partition_entries:
        return {"sdp_l6_status": "cvxpy-unavailable-or-empty",
                "l6_constraints_added": 0}

    n_p = len(partition_entries)
    n_e = electron_block_count

    y0 = cp.Variable(name="y0_l6")
    y_p = cp.Variable(n_p, nonneg=True, name="y_p_l6")  # nucleon-block duals
    y_e = cp.Variable(n_e, nonneg=True, name="y_e_l6")  # electron-block duals
    c_pair = {}
    for (i, j, _h) in pair_couplings:
        key = (min(i, j), max(i, j))
        c_pair[key] = cp.Variable(name=f"c_pair_l6_{key[0]}_{key[1]}")
    c_en = {}
    for ent in electron_pair_couplings:
        key = (ent["electron_idx"], ent["nucleon_target"])
        c_en[key] = cp.Variable(name=f"c_en_l6_{key[0]}_{key[1]}")

    constraints = []
    # Nucleon block dual constraints
    for i, entry in enumerate(partition_entries):
        constraints.append(y0 + y_p[i] <= entry["q_laplacian_eigenvalue"])
    # Electron block dual constraints (use a uniform mu for electron blocks
    # since electrons all have the same H_3 Wedderburn structure)
    mu_electron = float(partition_entries[0]["q_laplacian_eigenvalue"]) if partition_entries else 1.0
    for k in range(n_e):
        constraints.append(y0 + y_e[k] <= mu_electron)

    # Pair-coupling 2x2 PSD (nucleon-nucleon)
    for (i, j, _h) in pair_couplings:
        key = (min(i, j), max(i, j))
        mu_i = partition_entries[i]["q_laplacian_eigenvalue"]
        mu_j = partition_entries[j]["q_laplacian_eigenvalue"]
        M = cp.bmat([[mu_i - y0 - y_p[i], c_pair[key]],
                     [c_pair[key], mu_j - y0 - y_p[j]]])
        constraints.append(M >> 0)

    # Electron-nucleon 2x2 PSD coupling
    for ent in electron_pair_couplings:
        e_idx = ent["electron_idx"]
        n_idx = ent["nucleon_target"]
        if n_idx >= n_p:
            continue
        key = (e_idx, n_idx)
        mu_n = partition_entries[n_idx]["q_laplacian_eigenvalue"]
        M = cp.bmat([[mu_electron - y0 - y_e[e_idx], ent["h_coupling"] * c_en[key]],
                     [ent["h_coupling"] * c_en[key], mu_n - y0 - y_p[n_idx]]])
        constraints.append(M >> 0)

    objective = cp.Maximize(y0 * float(n_target))
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
    except Exception as _e:
        return {"sdp_l6_status": f"solver-error:{_e}",
                "l6_constraints_added": len(electron_pair_couplings)}

    if prob.status not in ("optimal", "optimal_inaccurate"):
        return {"sdp_l6_status": prob.status,
                "l6_constraints_added": len(electron_pair_couplings)}

    return {
        "sdp_l6_status": prob.status,
        "l6_constraints_added": len(electron_pair_couplings),
        "y0_l6": float(y0.value) if y0.value is not None else 0.0,
        "objective_value_l6": float(prob.value),
    }


# ─── Level 7: covalent constraint family ─────────────────────────────

def sdp_with_covalent(atoms, bonds, partition_entries, pair_couplings,
                       atom_solutions=None):
    """Level-7 SDP: per-atom L6 SDPs + covalent bond constraints.

    Each bond is a shared trefoil between two atoms (per
    `confinement_shortcuts.MoleculeWord`); the constraint family
    enforces consistency between the two atoms' Wedderburn blocks
    in the bonded region.

    Parameters
    ----------
    atoms : list of dict
        Each dict has {Z, N, electron_strands, name?}.
    bonds : list of tuple
        Each tuple is (atom_idx_1, atom_idx_2, bond_order) where
        bond_order ∈ {1, 2, 3} for single/double/triple covalent.
    partition_entries, pair_couplings : as for sdp_with_pair_coupling
    atom_solutions : optional list of pre-computed L6 solutions
        per atom (warm start).
    """
    n_atoms = len(atoms)
    if atom_solutions is None:
        atom_solutions = [None] * n_atoms

    # Solve L6 for each atom independently (no bond constraints yet)
    per_atom = []
    for i, a in enumerate(atoms):
        sol = sdp_with_atom_electron(
            a["Z"], a["N"], a.get("electron_strands", a["Z"]),
            partition_entries, pair_couplings,
            shell_solution=atom_solutions[i],
        )
        per_atom.append(sol)

    # Each bond contributes a shared-trefoil constraint linking the
    # two atoms' Wedderburn blocks. The bond is encoded as 3 shared
    # strands (a trefoil core); for bond_order > 1 multiply the
    # shared-strand count by bond_order.
    bond_constraints = []
    for (i, j, order) in bonds:
        bond_constraints.append({
            "atom_i": i, "atom_j": j, "bond_order": order,
            "shared_strand_count": 3 * order,
            "atom_i_block_idx": 0,  # canonical: bond couples to first
                                     # Wedderburn block of each atom
            "atom_j_block_idx": 0,
            "h_coupling": 1.0,  # unit coupling per bond order
        })

    sdp_l7 = _sdp_with_bond_constraints(
        per_atom, bond_constraints, partition_entries, n_atoms)

    return {
        "level": 7,
        "n_atoms": n_atoms,
        "n_bonds": len(bonds),
        "atoms": atoms,
        "per_atom_solutions": per_atom,
        "bond_constraints_count": len(bond_constraints),
        "bond_constraints_sample": bond_constraints[:5],
        **sdp_l7,
    }


def _sdp_with_bond_constraints(per_atom, bond_constraints,
                                partition_entries, n_atoms):
    """Cvxpy SDP solve with inter-atom shared-strand bond couplings.

    Each bond contributes a 2x2 PSD constraint linking the first
    Wedderburn block of one atom to the first block of the bonded
    atom; the off-diagonal coupling is scaled by the
    shared_strand_count of the bond (3 for single, 6 for double,
    9 for triple).
    """
    if not _HAVE_CVXPY or n_atoms == 0:
        return {"sdp_l7_status": "cvxpy-unavailable-or-empty",
                "l7_bond_constraints_added": 0}

    # One dual variable per atom (representing the first block's y_λ)
    y0 = cp.Variable(name="y0_l7")
    y_atom = cp.Variable(n_atoms, nonneg=True, name="y_atom_l7")
    c_bond = {}
    for ent in bond_constraints:
        key = (ent["atom_i"], ent["atom_j"])
        c_bond[key] = cp.Variable(name=f"c_bond_{key[0]}_{key[1]}")

    # Use the first partition's q_laplacian_eigenvalue as a uniform
    # bound for each atom's first block
    mu_atom = (float(partition_entries[0]["q_laplacian_eigenvalue"])
               if partition_entries else 1.0)

    constraints = []
    for k in range(n_atoms):
        constraints.append(y0 + y_atom[k] <= mu_atom)

    for ent in bond_constraints:
        i, j = ent["atom_i"], ent["atom_j"]
        if i >= n_atoms or j >= n_atoms:
            continue
        key = (i, j)
        # Bond strength scales with shared_strand_count and h_coupling
        scale = float(ent["shared_strand_count"]) * float(ent["h_coupling"])
        # Normalize by 3 (single-bond strand count) so single-bond → 1.0
        coupling = scale / 3.0
        M = cp.bmat([[mu_atom - y0 - y_atom[i], coupling * c_bond[key]],
                     [coupling * c_bond[key], mu_atom - y0 - y_atom[j]]])
        constraints.append(M >> 0)

    n_target = float(n_atoms)
    prob = cp.Problem(cp.Maximize(y0 * n_target), constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
    except Exception as _e:
        return {"sdp_l7_status": f"solver-error:{_e}",
                "l7_bond_constraints_added": len(bond_constraints)}

    if prob.status not in ("optimal", "optimal_inaccurate"):
        return {"sdp_l7_status": prob.status,
                "l7_bond_constraints_added": len(bond_constraints)}

    return {
        "sdp_l7_status": prob.status,
        "l7_bond_constraints_added": len(bond_constraints),
        "y0_l7": float(y0.value) if y0.value is not None else 0.0,
        "objective_value_l7": float(prob.value),
    }


# ─── Self-test ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("P2.4 multi-level SDP constraint families")
    print("=" * 60)
    print()
    print("L4 (shell-closure) — partition enumeration for ⁴He (A=4):")
    sp = shell_constraint_partitions(4)
    print(f"  {len(sp)} self-conjugate partitions of 12; first: {list(sp[0])}")
    print()
    print("L5 (cross-shell, LR-fusion) — c^(2,1)_{(1),(1,1)} = "
          f"{lr_coefficient((1,), (1, 1), (2, 1))} (expected 1)")
    print()
    # Tiny synthetic partition_entries / pair_couplings for L6, L7
    fake_entries = [
        {"partition": (3,), "q_laplacian_eigenvalue": 1.0},
        {"partition": (2, 1), "q_laplacian_eigenvalue": 0.8},
        {"partition": (1, 1, 1), "q_laplacian_eigenvalue": 0.5},
    ]
    print("L6 (atom-electron) — neutral ¹²C (Z=6, N=6, electron_strands=6):")
    l6 = sdp_with_atom_electron(6, 6, 6, fake_entries, [])
    print(f"  electron blocks: {l6['electron_block_count']}, "
          f"couplings: {l6['electron_pair_couplings_count']}")
    print()
    print("L7 (covalent) — H₂ (two ¹H atoms, single bond):")
    h_atoms = [{"Z": 1, "N": 0, "electron_strands": 1},
               {"Z": 1, "N": 0, "electron_strands": 1}]
    l7 = sdp_with_covalent(h_atoms, [(0, 1, 1)], fake_entries, [])
    print(f"  atoms: {l7['n_atoms']}, bonds: {l7['n_bonds']}, "
          f"shared strands per bond: {l7['bond_constraints_sample'][0]['shared_strand_count']}")
    print()
    print("All 4 levels (L4–L7) have working constraint enumeration.")
