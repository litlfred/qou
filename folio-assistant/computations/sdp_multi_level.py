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

def sdp_with_cross_shell(Z, N, extra_Z, extra_N, partition_entries,
                          pair_couplings, n_target=None,
                          shell_solution=None):
    """Level-5 SDP: shell-closure SDP + cross-shell pairing constraints.

    Constraint family: frayed boxes (the extra_Z + extra_N boxes
    beyond the magic shell core) must pair off in the LR-fusion sense
    (prop:diagrammatic-double-magic-lr-fusion).

    Status: stub. Requires implementing the LR-fusion constraint
    on the extra-box block. The mathematical content is in
    `prop:diagrammatic-double-magic-lr-fusion` (cherry-picked from
    PR #500).
    """
    raise NotImplementedError(
        "L5 cross-shell SDP: requires LR-fusion constraint family "
        "for extra (non-magic) boxes. See "
        "prop:diagrammatic-double-magic-lr-fusion. Tracked as "
        "P2.4.b follow-up.")


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
