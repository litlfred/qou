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
    """Enumerate self-conjugate partitions of n via Frobenius coords.

    Inlined from magic-numbers-numerical-witness.py to avoid the
    hyphenated module name (Python imports prefer underscores).
    """
    out = []

    def search(remaining, max_a, partial):
        if remaining == 0:
            arms = sorted(partial, reverse=True)
            k = len(arms)
            lam_dict = {}
            for i, a in enumerate(arms, start=1):
                lam_dict[i] = max(lam_dict.get(i, 0), i + a)
                for off in range(1, a + 1):
                    lam_dict[i + off] = max(lam_dict.get(i + off, 0), i)
            lam = tuple(sorted(lam_dict.values(), reverse=True))
            out.append(lam)
            return
        for a in range(min(max_a, (remaining - 1) // 2), -1, -1):
            cost = 2 * a + 1
            if cost <= remaining:
                search(remaining - cost, a - 1, partial + [a])

    search(n, n, [])
    return out


def sdp_with_shell_closure(Z, N, partition_entries, pair_couplings,
                            n_target=None, pair_solution=None):
    """Level-4 SDP: pair-coupling SDP + shell-closure constraints.

    Adds: for each shell-closure-eligible partition (per
    shell_constraint_partitions), the dual variable y_λ is FIXED to
    the shell-saturation value (κ-zero / self-conjugate weight).

    pair_solution
        Optional dict from sdp_with_pair_coupling — used as warm
        start. If provided, reuses its y_lambda values for non-shell
        partitions.
    """
    if n_target is None:
        n_target = float(Z + N)

    # First solve the pair-level SDP to get baseline y_lambda
    if pair_solution is None:
        pair_solution = sdp_with_pair_coupling(
            partition_entries, pair_couplings, n_target)

    # Identify shell-closure partitions for this atom
    A = Z + N
    shell_partitions = shell_constraint_partitions(A)

    # For now: report the shell partitions and overlay the pair
    # solution. Full shell-closure SDP requires re-solving with
    # fixed y_λ for shell partitions — implementation left as a
    # follow-up step (the constraint family is well-defined; the
    # cvxpy refactor to add equality constraints on a subset of
    # y_λ variables is the mechanical piece).
    return {
        **pair_solution,
        "level": 4,
        "shell_closure_eligible_partition_count": len(shell_partitions),
        "shell_partitions_sample": [list(lam) for lam in shell_partitions[:3]],
        "note": "Skeleton: pair-level SDP returned with shell-partition tagging. "
                "Full shell-closure SDP (fix y_λ on shell partitions) is a "
                "cvxpy refactor follow-up.",
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
        "note": "LR-fusion constraint family enumerated. cvxpy SDP refactor"
                " wires c^μ into cross-block coupling matrix; that's the"
                " mechanical follow-up step.",
    }


# ─── Level 6: atom-electron constraint family ────────────────────────

def sdp_with_atom_electron(Z, N, electron_strands, partition_entries,
                            pair_couplings, n_target=None,
                            shell_solution=None):
    """Level-6 SDP: shell-closure SDP + electron-shell coupling.

    Constraint family: the (Z + N) nucleon strands and the
    electron_strands (= Z for neutral atom) interact via electron-
    shell crossings. The Wedderburn decomposition extends to the
    larger H_{3(Z + N) + 3·electron_strands} algebra.

    Status: stub. Requires extending partition_entries to the
    larger algebra and adding electron-nucleon coupling constraints.
    """
    raise NotImplementedError(
        "L6 atom-electron SDP: requires electron-strand block "
        "extension of the H_{3A} Wedderburn decomposition. "
        "Tracked as P2.4.c follow-up.")


# ─── Level 7: covalent constraint family ─────────────────────────────

def sdp_with_covalent(atoms, bonds, partition_entries, pair_couplings,
                       atom_solutions=None):
    """Level-7 SDP: per-atom L6 SDPs + covalent bond constraints.

    Each bond is a shared trefoil between two atoms (per
    `confinement_shortcuts.MoleculeWord`); the constraint family
    enforces consistency between the two atoms' Wedderburn blocks
    in the bonded region.

    Status: stub. Requires multi-atom constraint linking through
    shared-trefoil bond strands.
    """
    raise NotImplementedError(
        "L7 covalent SDP: requires inter-atom shared-trefoil bond "
        "constraint family. Tracked as P2.4.d follow-up.")


# ─── Self-test ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("P2.4 multi-level SDP constraint families")
    print("=" * 60)
    print()
    print("Level 4 prototype: shell-closure for ⁴He (Z=N=2, A=4):")
    # Skip full SDP solve; just exercise the shell-partition path.
    sp = shell_constraint_partitions(4)
    print(f"  Self-conjugate partitions of 3A=12: {len(sp)}")
    print(f"  First 3: {[list(lam) for lam in sp[:3]]}")
    print()
    print("Levels 5, 6, 7: stubs raising NotImplementedError")
    print()
    print("Status: skeleton + L4 prototype + L5/L6/L7 stubs.")
    print("Per-level constraint families documented in module docstring.")
