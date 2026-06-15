"""Operator-valued Wenzl branching combiner — |tr_M(β_atom)| via
recursive per-nucleon ρ_μ + per-interface A^λ_{ξν}(I).

## Recursion

For an A-nucleon atom with canonical braid

    β_atom = β_p^Z · I_{1,2} · β_n^N · I_{2,3} · ... · I_{A-1,A} · β_block_A

the operator-valued Wenzl 1988 branching identity peels one nucleon
at a time:

    χ^λ(W_inner · I · β_block) = Σ_{ξ ⊢ n-3, ν ⊢ 3} c^λ_{ξν}
        · Tr_{V_ξ ⊗ V_ν}( A^λ_{ξν}(I) · (ρ_ξ(W_inner) ⊗ ρ_ν(β_block)) )

Recursively unwound: for each (ξ_outer, ν_outer) pair at the outer
peel level, ρ_ξ(W_inner) is itself a Wenzl branching of the (A-1)-
nucleon prefix. At the base case (A=2), W_inner is the leftmost
nucleon's intra-block at H_3, computed directly.

## Cost

Per atom A with interfaces at levels {n_2, n_3, ..., n_A}:

    Σ_{level k} Σ_{(ξ, ν)} cost(A^λ_{ξν}) · dim(ξ) · dim(ν)

A^λ_{ξν}(I) extracts are pre-cached on disk (this branch's
`A-operator-extract-h{n}-{iface}.witness.json`). Per-nucleon ρ_μ
at H_3 is dim ≤ 2 (instant). Total wall: ~seconds per atom once
all extracts are available.

Compare to direct Hoefsmit:
  - ⁴He H_12: 12s (Hoefsmit f64) → < 1s (branching) expected
  - ⁵Li H_15: timeout >1500s → ~seconds (branching) expected
  - ⁶Li H_18: 22 min (markov_peel)  → ~seconds (branching) expected

## Status

Extracts present (this branch):
  - H_6 pn  (deuteron)
  - H_9 pp / pn / nn  (full trio)
  - H_12 pp / pn / nn  IN FLIGHT (background task b1pwlz1gf)

A=2 (deuteron) runs via the operator-valued branching end-to-end. A≥3
tr_M is computed via the fine-Bratteli transfer matrix
(tr_m_atom_via_transfer.tr_m_atom_zn → chi_monotone_transfer): a lossless
Σ_{λ⊢3A} y_λ χ^λ over ALL p(3A) partitions at 50 dps in one sweep, with
no d_λ wall and no pyhecke_native dependency. This replaced the earlier
native-Hoefsmit-kernel delegation (which required the Rust wheel and
formed χ per-partition); same canonical color-weighted p-n convention, so
the value is identical (transfer ≡ char_fast to 4.7e-15). ~5000× the
markov_peel symbolic path — ⁶Li in ~0.16 s vs ~17 min. The operator-
valued branching recursion above (compute_chi_lambda_via_branching) is
retained as the A=2 path and as a structural cross-check; see
compute_tr_m_via_branching.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _precision import set_compute_dps, fmt  # noqa: E402
from char_fast import _compiled_sigmas  # noqa: E402
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from q_parameter import Q as Q_FLOAT  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

set_compute_dps()

# Extract lookup: (n_outer, interface) → witness filename
EXTRACT_FILENAMES = {
    (6, "pn"): "sublemma-2-1-A-operator-extract.witness.json",     # deuteron
    (9, "nn"): "sublemma-2-1-A-operator-extract-h9-nn.witness.json",
    (9, "pp"): "A-operator-extract-h9-pp.witness.json",
    (9, "pn"): "A-operator-extract-h9-pn.witness.json",
    (12, "pp"): "A-operator-extract-h12-pp.witness.json",
    (12, "pn"): "A-operator-extract-h12-pn.witness.json",
    (12, "nn"): "A-operator-extract-h12-nn.witness.json",
    (15, "pp"): "A-operator-extract-h15-pp.witness.json",
    (15, "pn"): "A-operator-extract-h15-pn.witness.json",
    (15, "nn"): "A-operator-extract-h15-nn.witness.json",
    (18, "pp"): "A-operator-extract-h18-pp.witness.json",
    (18, "pn"): "A-operator-extract-h18-pn.witness.json",
    (18, "nn"): "A-operator-extract-h18-nn.witness.json",
}


def load_A_extract(n_outer: int, interface: str) -> dict | None:
    """Load the A^λ_{ξν}(I) extract for (n_outer, interface). Returns
    None if not yet cached."""
    fname = EXTRACT_FILENAMES.get((n_outer, interface))
    if fname is None:
        return None
    path = HERE / fname
    if not path.exists():
        return None
    return json.loads(path.read_text())


def evaluate_word_matrix_np(shape: tuple, word: list,
                            q_val: float = None) -> np.ndarray:
    """ρ_shape(W) at q_val as a NumPy complex matrix."""
    if q_val is None:
        q_val = float(Q_FLOAT)
    sigmas, dim = _compiled_sigmas(shape, "double")
    sigma_mats = [np.asarray(fn(q_val), dtype=complex) for fn in sigmas]
    M = np.eye(dim, dtype=complex)
    Iden = np.eye(dim, dtype=complex)
    for (c, d, g) in word:
        if g >= len(sigma_mats):
            raise ValueError(f"gen {g} out of range for shape {shape}")
        M = M @ (complex(c) * sigma_mats[g] + complex(d) * Iden)
    return M


def per_nucleon_intra_word(nucleon_type: str) -> list[tuple]:
    """Return the H_3 intra-block braid word for a single nucleon.

    Matches the convention used in mass_at_3A_proper.atom_braid_word_3A
    for the per-nucleon block at base 3k, 3k+1:
      - proton:   σ_0 σ_1   (with sign +1)
      - neutron:  σ_0⁻¹ σ_1⁻¹  (Hecke negative: (1, -h, g))
    """
    from canonical_braid_crossings import atom_canonical_crossings
    # Inspect a single-nucleon atom (Z=1,N=0) or (Z=0,N=1) to extract
    # the canonical intra-block — its full word IS the intra block at H_3.
    if nucleon_type == "p":
        ops = atom_canonical_crossings(1, 0)
    elif nucleon_type == "n":
        ops = atom_canonical_crossings(0, 1)
    else:
        raise ValueError(f"unknown nucleon {nucleon_type!r}")
    # Convert to (c, d, gen_idx) tuples
    from hecke_core import h as h_val
    word = []
    for gen, ctype in ops:
        if ctype == "sigma":
            word.append((1.0, 0.0, int(gen)))
        elif ctype == "sigma_inv":
            word.append((1.0, -float(h_val), int(gen)))
        elif ctype == "averaged":
            word.append((1.0, -float(h_val) / 2, int(gen)))
        else:
            raise ValueError(f"unknown crossing type {ctype!r}")
    return word


def interface_type_for_pair(nuc_a: str, nuc_b: str) -> str:
    if nuc_a == "p" and nuc_b == "p":
        return "pp"
    if nuc_a == "n" and nuc_b == "n":
        return "nn"
    return "pn"


def compute_chi_lambda_via_branching(
    Z: int, N: int, lam: tuple[int, ...],
    extract_cache: dict[tuple[int, str], dict],
    q_val: float = None,
    rho_cache_h3: dict[tuple, dict[str, np.ndarray]] | None = None,
) -> complex | None:
    """Compute χ^λ(β_atom) at q=q_val via recursive Wenzl branching.

    Returns the complex χ^λ value, or None if any required extract
    is missing.

    Algorithm (peel-from-right):

      Given β_atom of A nucleons at H_{3A}, the outermost interface I_A
      connects nucleons (A-1) → A. So:

        χ^λ(β_atom) = Σ_{(ξ, ν)} c^λ_{ξν}
                       · Tr( A^λ_{ξν}(I_A) · (ρ_ξ(β_{atom-A}) ⊗ ρ_ν(β_block_A)) )

      where β_{atom-A} is the (A-1)-nucleon prefix at H_{3(A-1)} and
      β_block_A is the A-th nucleon's intra at H_3.

      ρ_ξ(β_{atom-A}) is itself a Wenzl branching of the (A-1) atom.
      Base case A=1: ρ_ξ(β_intra) at H_3 directly.
    """
    if q_val is None:
        q_val = float(Q_FLOAT)
    if rho_cache_h3 is None:
        rho_cache_h3 = {}

    A = Z + N
    n = 3 * A
    if A < 2:
        return None  # branching needs at least 2 nucleons

    ordering = ["p"] * Z + ["n"] * N

    # Per-nucleon ρ_μ(β_intra) at H_3 — small (dim ≤ 2). Cache.
    def get_rho_h3(nuc: str, mu: tuple) -> np.ndarray:
        key = (nuc, mu)
        if key not in rho_cache_h3:
            rho_cache_h3[key] = evaluate_word_matrix_np(
                mu, per_nucleon_intra_word(nuc), q_val
            )
        return rho_cache_h3[key]

    # rho_xi(β_{A-1 atom}) for each ξ ⊢ 3(A-1):
    #   - If A=2: ξ ⊢ 3, ρ_ξ(β_intra_first) at H_3 directly
    #   - If A>2: recurse — ρ_ξ is computed by another branching layer.
    #     For now we use the SIMPLE base case: only A=2 implemented
    #     end-to-end; for A>2 we recurse into _build_rho_recursive.
    n_inner = 3 * (A - 1)
    rho_xi: dict[tuple, np.ndarray] = {}
    if A == 2:
        # β_inner is the first nucleon's intra block at H_3
        first_nuc = ordering[0]
        for xi in partitions_of(3):
            rho_xi[xi] = get_rho_h3(first_nuc, xi)
    else:
        # A ≥ 3: ρ_ξ(β_inner) for the (A-1)-nucleon prefix.
        #
        # NAIVE direct-eval at H_{n_inner} (evaluate_word_matrix_np on
        # atom_braid_word_3A(Z_inner, N_inner)) does NOT work with the
        # current A^λ_{ξν}(I_A) extracts at H_9 / H_12 / H_15 / H_18.
        #
        # ROOT CAUSE: the H_9+ extracts are produced by least-squares
        # fitting over a small set of H_3 test words for the inner
        # family. For every partition λ ⊢ 9 with d_λ > 1 the bilinear
        # system is RANK-DEFICIENT (e.g. λ=[8,1] has n_unknowns=30,
        # n_equations=144, rank=14; λ=[4,3,1,1] has n_unknowns=3390,
        # rank=66). The fitted A matrix is the min-norm solution for
        # H_3 inner-test-words, NOT a universal interface operator.
        # When the inner braid is a 2-nucleon deuteron at H_6 instead
        # of a single nucleon at H_3, the same A matrix gives wrong
        # χ^λ. Empirically: A=2 deuteron matches markov_peel at 7e-15
        # (H_6 extract IS full-rank); A=3 tritium/³He differ from
        # markov_peel by 21-42 % (H_9 extracts are under-fitted).
        #
        # CLOSURE PATHS (documented for follow-up):
        #
        #   (a) Regenerate H_9 / H_12 / H_15 / H_18 extracts with a
        #       test-word set large enough to make rank ≥ n_unknowns
        #       for every λ. For H_9 [4,3,1,1] this requires
        #       ≥ 3390 test words; for H_18 [3,3,3,3,3,3] it explodes.
        #
        #   (b) Build a TRULY recursive ρ_ξ via the matrix-form Wenzl
        #       branching identity (requires the operator-form A^λ
        #       reconstruction, not just the trace form).
        #
        #   (c) Fall back to canonical markov_peel.tr_M_atomic for the
        #       inner — gives the correct |tr_M| symbolically at any q,
        #       at the cost of bypassing the branching combiner's
        #       speedup.
        #
        # For now, return None with a clear diagnostic so callers
        # don't get silently-wrong A=3 values.
        return None

    # Outer interface: between nucleon (A-1) (=first nucleon for A=2)
    # and nucleon A (=second)
    outer_iface = interface_type_for_pair(ordering[-2], ordering[-1])
    A_extract = extract_cache.get((n, outer_iface))
    if A_extract is None:
        return None  # extract missing

    data = A_extract.get("data", A_extract)
    results = data.get("results_per_lambda", {})
    # The extract files use two key conventions:
    #   - deuteron (sublemma_2_1): str(tuple(lam))  → '(6,)' or '(3, 2, 1)'
    #   - H_9+ (A_operator_extract_*): str(list(lam))  → '[9]' or '[3, 2, 1]'
    # Try both.
    candidates = [str(list(lam)), str(tuple(lam))]
    lam_data = None
    for key in candidates:
        if key in results:
            lam_data = results[key]
            break
    if lam_data is None:
        return None

    # Per-block ρ_ν at H_3 for the last nucleon
    last_nuc = ordering[-1]
    rho_nu_h3: dict[tuple, np.ndarray] = {}
    for nu in partitions_of(3):
        rho_nu_h3[nu] = get_rho_h3(last_nuc, nu)

    # Apply the branching sum
    # Pre-parse pair keys ONCE before the loop (Gemini review #708 —
    # ast.literal_eval inside a hot inner loop was a measurable cost).
    import ast
    a_per_pair = lam_data.get("A_per_pair", {})
    parsed_pairs: list[tuple[tuple, tuple, dict]] = []
    for pair_key, pair_info in a_per_pair.items():
        try:
            parsed = ast.literal_eval(pair_key)
            xi, nu = parsed[0], parsed[1]
            if not isinstance(xi, tuple):
                xi = tuple(xi)
            if not isinstance(nu, tuple):
                nu = tuple(nu)
            parsed_pairs.append((xi, nu, pair_info))
        except (ValueError, SyntaxError):
            continue

    chi_total = 0.0 + 0.0j
    for xi, nu, pair_info in parsed_pairs:

        # Field-name compat: deuteron extract uses d_mu/d_nu;
        # H_9+ extracts use d_xi/d_nu.
        d_xi = pair_info.get("d_xi", pair_info.get("d_mu"))
        d_nu = pair_info["d_nu"]
        c_lr = pair_info["c_lr"]

        # A matrix
        re = np.array(pair_info["matrix_re"])
        im = np.array(pair_info["matrix_im"])
        A_mat = re + 1j * im   # shape (d_xi*d_nu, d_xi*d_nu)

        # ρ_ξ ⊗ ρ_ν
        rho_x = rho_xi.get(xi)
        rho_n = rho_nu_h3.get(nu)
        if rho_x is None or rho_n is None:
            continue
        rho_kron = np.kron(rho_x, rho_n)

        # Tr( A · (ρ_ξ ⊗ ρ_ν) )
        # Note: c_lr is already absorbed into the extracted A matrix
        # (the bilinear-system M does NOT multiply by c_lr, so the
        # least-squares A absorbs the c_lr factor). Do NOT multiply
        # by c_lr here — verified by per-λ cross-check against
        # chi_lambda_fast on the deuteron.
        prod = A_mat @ rho_kron
        chi_total += np.trace(prod)
    return complex(chi_total)


def compute_tr_m_via_branching(
    Z: int, N: int, q_val: float = None,
) -> tuple[mp.mpf | None, float, str | None]:
    """Compute |tr_M(β_atom, q_0)| at the canonical color-weighted p-n
    convention.

    For A=2 (deuteron) this runs the operator-valued Wenzl branching
    end-to-end (H_6 extract). For A ≥ 3 the value is computed via the
    fine-Bratteli transfer matrix (tr_m_atom_via_transfer.tr_m_atom_zn):
    a lossless Σ_{λ⊢3A} y_λ χ^λ over ALL p(3A) partitions at 50 dps in
    one sweep — no d_λ wall, no pyhecke_native dependency. This replaced
    the earlier native-kernel delegation; the value is identical (same
    convention and y_λ; transfer ≡ char_fast full Hoefsmit to 4.7e-15)
    while running ~5000× faster than the markov_peel symbolic path.
    """
    if q_val is None:
        q_val = float(Q_FLOAT)
    A = Z + N
    n = 3 * A
    if A < 2:
        # Return None rather than 0 — branching combiner doesn't apply to
        # single-nucleon (no inter-nucleon interface). Caller should use
        # the H_3 Hoefsmit direct path. Copilot review #708.
        return None, 0.0, "A < 2: branching combiner inapplicable (use direct H_3 path)"
    if A >= 3:
        # A≥3 via the fine-Bratteli transfer matrix (chi_monotone_transfer
        # → tr_m_atom_via_transfer.tr_m_atom_zn): lossless Σ_{λ⊢3A} y_λ χ^λ
        # over ALL p(3A) partitions at 50 dps, computed in ONE sweep — no
        # d_λ wall and NO pyhecke_native (Rust wheel) dependency.
        #
        # This replaces the former native path
        # (pyhecke_native.chi_lambda_all_partitions_mpfr per signed word),
        # which required the wheel and formed χ per-partition. The transfer
        # gives every χ^λ at once via the monotone-word seminormal transfer
        # (Cayley–Hamilton per generator, content-gap weights), so the
        # color-weighted p-n identity-term split the native path did by hand
        # is handled internally by chi_monotone_transfer.word_to_mpfr.
        #
        # Same canonical color-weighted p-n convention (atom_braid_word_3A
        # default include_inter=True, pn_convention="bring_color_weighted")
        # and same y_λ Jones–Markov weights, so the value is identical:
        # transfer ≡ char_fast (full Hoefsmit) to 4.7e-15, and
        # tr_M_atom(D)=0.388357 matches this combiner's own A=2 value.
        # ~5000× the markov_peel symbolic path (⁶Li 0.16 s vs ~17 min).
        #
        # Honours the no-truncation precision ruling — ALL partitions kept
        # (the active-set truncation is a ~10⁻³ error, rejected for 1-ppQ);
        # the speedup is the transfer sweep, not dropping partitions. See
        # docs/audits/2026-06-10-binding-active-set-compute-optimization.md.
        from tr_m_atom_via_transfer import tr_m_atom_zn
        t0 = time.time()
        tr_atom_mp, _tr_free, _chi, _wall = tr_m_atom_zn(Z, N, dps=mp.mp.dps)
        return abs(tr_atom_mp), time.time() - t0, None

    # Load required extracts
    ordering = ["p"] * Z + ["n"] * N
    extract_cache: dict[tuple[int, str], dict] = {}
    iface = interface_type_for_pair(ordering[-2], ordering[-1])
    extract = load_A_extract(n, iface)
    if extract is None:
        return None, 0.0, (
            f"Missing A^λ_{{ξν}}(I_{iface}) extract at H_{n}. "
            f"Generate via: python3 A_operator_extract_at_level.py "
            f"--n-outer {n} --interface {iface}"
        )
    extract_cache[(n, iface)] = extract

    # Loop over λ ⊢ n
    t0 = time.time()
    y_table = y_lambda_at(n, q_val)
    tr_m = mp.mpf(0)
    rho_cache: dict = {}
    for lam in partitions_of(n):
        chi = compute_chi_lambda_via_branching(
            Z, N, lam, extract_cache, q_val=q_val, rho_cache_h3=rho_cache
        )
        if chi is None:
            continue
        y = mp.mpf(str(y_table.get(lam, 0)))
        chi_mp = mp.mpf(str(chi.real)) + mp.mpc(0, str(chi.imag))
        tr_m += y * chi_mp.real
    wall = time.time() - t0
    return abs(tr_m), wall, None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--atoms", default="D",
        help="Comma-separated atoms (default: D). A=2 via operator-valued "
             "branching; A>=3 via the fine-Bratteli transfer matrix.",
    )
    parser.add_argument(
        "--verify-against-markov-peel", action="store_true",
        help="Cross-check vs markov_peel.tr_M_atomic (only valid for the "
             "strict_averaged convention; markov_peel cannot represent the "
             "color-weighted p-n default, so this reports 'verify failed' "
             "for the production atoms — A>=3 is cross-checked against an "
             "independent native Σ y_λ χ^λ in the verify witnesses instead).",
    )
    args = parser.parse_args()

    label_to_ZN = {
        "p": (1, 0), "n": (0, 1), "D": (1, 1), "T": (1, 2),
        "3He": (2, 1), "4He": (2, 2),
        "5Li": (3, 2), "6Li": (3, 3), "7Li": (3, 4),
    }

    print("=" * 80)
    print("  Operator-valued Wenzl branching combiner")
    print("=" * 80)
    print()
    print(f"  {'atom':<6} {'A':>2} {'n':>3} {'|tr_M|_branching':<22} "
          f"{'wall (s)':>10} {'status':<30}")
    print("  " + "-" * 90)

    for atom_str in args.atoms.split(","):
        atom_str = atom_str.strip()
        if atom_str not in label_to_ZN:
            print(f"  {atom_str:<6} (unknown)")
            continue
        Z, N = label_to_ZN[atom_str]
        A = Z + N
        n = 3 * A
        tr_m, wall, err = compute_tr_m_via_branching(Z, N)
        if err:
            print(f"  {atom_str:<6} {A:>2} {n:>3} {'—':<22} {wall:>10.2f} {err[:30]}")
            continue
        tr_str = fmt(tr_m, dps=15)
        verdict = "OK"
        if args.verify_against_markov_peel:
            try:
                import sympy as sp
                from markov_peel import tr_M_atomic
                ref_sym = tr_M_atomic(Z, N)
                q_sym = sp.Symbol("q", positive=True)
                for f in ref_sym.free_symbols:
                    if f.name == "q":
                        q_sym = f; break
                ref = mp.mpf(str(sp.N(ref_sym.subs(q_sym, sp.Float(str(Q_FLOAT), 50)), 50)))
                rel = abs(tr_m - abs(ref)) / abs(ref) if abs(ref) > 0 else mp.mpf(0)
                verdict = f"vs markov_peel rel_err={float(rel):.2e}"
            except Exception as e:  # noqa: BLE001
                verdict = f"verify failed: {type(e).__name__}"
        print(f"  {atom_str:<6} {A:>2} {n:>3} {tr_str:<22} {wall:>10.2f} {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
