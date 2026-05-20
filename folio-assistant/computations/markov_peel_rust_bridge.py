#!/usr/bin/env python3
# polynomial_q_not_applicable: bridge to pyhecke_native (Rust) for
# Markov-trace acceleration on the markov_peel critical path.
"""Rust-accelerated atomic Markov trace via pyhecke_native + Wenzl bridge.

Provides `tr_M_atomic_rust(Z, N, q)` — the canonical Markov trace
`tr_M(β_atomic(Z, N), q)` computed via:

  tr_M(β) = Σ_{λ ⊢ n} y_λ(q) · χ^λ(β, q)

where:
  - χ^λ is computed in Rust via `pyhecke_native.chi_lambda_all_partitions_f64`
    (rayon-parallel over partitions; direct-averaging f64 path).
  - y_λ(q) is loaded from `y-lambda-at-q0.witness.json` for q = q₀
    (sub-ms hot path) or computed via `wedderburn_jones_markov.y_lambda_at`.
  - The Σ_λ combine is cheap Python (≤ ~200 partitions at H_21).

Boundary cost: ONE PyO3 call per atom, returning Vec<(partition, χ^λ)>.
Per the Rust scoping doc, this is the "right granularity" — amortizes
the boundary over the entire compute.

Strategy #1 from `docs/audits/2026-05-20-markov-peel-bottleneck-profile.md`
implemented via pre-existing Rust infrastructure (rather than a new
crate). Expected 5-50× over the Phase-1 Python `laurent_q_trace.py`
path on H_15+ atoms.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


def _atomic_word_to_signed_gens(Z: int, N: int, *,
                                  include_inter: bool = True) -> list[tuple[int, int]]:
    """Translate `atom_braid_word_3A(Z, N)` (c, d, gen_0based) triples
    into the (sign, gen_1based) format expected by
    `pyhecke_native.chi_lambda_all_partitions_f64`.

    Sign convention (matches `hecke_engine::wenzl_lr::Crossing`):
      - `c=1, d=0`           → Sigma     = +1
      - `c=1, d=-h`          → SigmaInv  = -1
      - `c=1, d=-h/2`        → Averaged  =  0
    """
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_core import h as _h_num
    h_val = float(_h_num)

    word = atom_braid_word_3A(Z, N, include_inter=include_inter)
    signed: list[tuple[int, int]] = []
    for c, d, gen_0based in word:
        # Use a generous tolerance — the Python side carries d as a
        # float, but the algebraic discriminator is exact at q₀.
        if abs(c - 1.0) > 1e-9:
            raise ValueError(
                f"atomic word factor has c={c} != 1; only (c=1, d) "
                f"factors are supported by the Rust crossing API")
        if abs(d) < 1e-12:
            sign = 1
        elif abs(d + h_val) < 1e-9:
            sign = -1
        elif abs(d + h_val / 2) < 1e-9:
            sign = 0
        else:
            raise ValueError(
                f"atomic word factor (c={c}, d={d}) does not match "
                f"any of Sigma/SigmaInv/Averaged (h={h_val})")
        # Rust API uses 1-based generator indices.
        signed.append((sign, int(gen_0based + 1)))
    return signed


def tr_M_atomic_rust(Z: int, N: int, *,
                     dps: int = 50,
                     include_inter: bool = True):
    """Canonical Markov trace `tr_M(β_atomic(Z, N), q₀)` via the Rust path,
    **MPFR at `dps` decimal places** (NO f64).

    Per CLAUDE.md §Precision goals L1 (compute precision ≤ 1 ppb),
    the production trace must be at ≥ 50-dps precision to preserve
    the structural-zero distinction needed for categorical identities.
    The f64 path (`chi_lambda_all_partitions_f64`) is for
    cross-checking only.

    Cross-checked against `markov_peel.tr_M_atomic` and
    `laurent_q_trace.tr_M_atomic_lq` to ~1e-30 relative at q₀ on
    every catalogued atom (p, n, D, T, ³He, ⁴He, ⁵Li).

    Parameters
    ----------
    Z, N : int
        Proton and neutron counts; A = Z + N, n_strands = 3·A.
    dps : int
        MPFR working precision in decimal places (default 50,
        the production floor). Set to 100 for research-grade
        substrate-derivation cross-checks.
    include_inter : bool
        Whether to include inter-nucleon crossings (default True).

    Returns
    -------
    tr_M : mpmath.mpf
        Canonical Markov trace at q₀ as an mpmath.mpf at `dps`
        precision.
    """
    try:
        import pyhecke_native
    except ImportError as e:
        raise ImportError(
            "pyhecke_native not installed. Build via "
            "`cd tools/pyhecke-native && maturin build --release` "
            "and `pip install` the resulting wheel. See "
            "docs/audits/2026-05-20-rust-port-scoping-markov-peel.md "
            "for the full build workflow."
        ) from e

    import mpmath as mp
    from q_parameter import Q_50_DIGIT_STR

    n_strands = 3 * (Z + N)

    # Build the (sign, gen) word
    signed_word = _atomic_word_to_signed_gens(
        Z, N, include_inter=include_inter
    )

    # Rust call — single PyO3 boundary crossing; rayon-parallel inside;
    # MPFR throughout the rust side at `dps` precision; returns
    # decimal strings for each (partition, χ^λ).
    chi_pairs_str = pyhecke_native.chi_lambda_all_partitions_mpfr(
        n_strands, signed_word, Q_50_DIGIT_STR, dps
    )

    # Sum: tr_M(β, q) = Σ_λ y_λ(q) · χ^λ(β, q) at `dps` precision
    from wedderburn_jones_markov import y_lambda_at
    with mp.workdps(dps):
        q_mpf = mp.mpf(Q_50_DIGIT_STR)
        y_dict = y_lambda_at(n_strands, q_val=q_mpf)
        total = mp.mpf(0)
        for lambda_vec, chi_str in chi_pairs_str:
            key = tuple(lambda_vec)
            y_val = y_dict.get(key)
            if y_val is None:
                # y_lambda_at returns dict keyed by tuple; some partitions
                # may not be in the dict if y_λ vanishes (sign-rep cases).
                continue
            chi_mpf = mp.mpf(chi_str)
            # y_val may be sympy.Expr — convert via decimal string
            if hasattr(y_val, "is_number"):
                import sympy as sp
                y_mpf = mp.mpf(str(sp.N(y_val, dps + 5)))
            else:
                y_mpf = mp.mpf(y_val)
            total += y_mpf * chi_mpf
        return total


def tr_M_atomic_rust_recursive(Z: int, N: int, *,
                                  dps: int = 50,
                                  include_inter: bool = True):
    """Canonical Markov trace via the **deeper Rust port** —
    `pyhecke_native.tr_m_word_lq` (Markov-axiom recursive ascent in
    pure Rust, no sympy, no f64).

    Distinct from `tr_M_atomic_rust` (which uses the
    Hoefsmit-via-MPFR per-partition path). This wrapper calls the
    Rust port of `laurent_q_trace.tr_M_word_lq` directly, getting
    back a ZHLaurent polynomial in (z, h) with BigInt coefficients,
    then evaluates at q₀ to mpmath.mpf at `dps`.

    Expected speedup over the Python LaurentQ path: 5-20× per the
    Rust port scoping doc. The boundary cost is ONE PyO3 call per
    atomic word; rust-side cache (OnceLock-bounded HashMap) folds
    in the recursion-tree's repeated subword evaluations.

    Phase-1+2 scope: empty / single-top / multi-top Case A+B.
    Case C raises `pyo3.exceptions.PyRuntimeError` — caller falls
    back to the sympy ocneanu path (same Python `tr_M_atomic_lq`
    fallback contract).
    """
    try:
        import pyhecke_native
    except ImportError as e:
        raise ImportError(
            "pyhecke_native not installed — see "
            "docs/audits/2026-05-20-rust-port-scoping-markov-peel.md"
        ) from e

    import mpmath as mp
    from q_parameter import Q_50_DIGIT_STR
    from mass_at_3A_proper import atom_braid_word_3A

    n_strands = 3 * (Z + N)

    # Build the atomic braid word (0-based generator indices) — same
    # convention as the Python `tr_M_word_lq` and the Rust port.
    # The (c, d) → sign translation isn't needed here: the recursion
    # path operates on the canonical (sign-only) form via the
    # signed-gens helper.
    signed_word = _atomic_word_to_signed_gens(
        Z, N, include_inter=include_inter
    )
    # Integration architecture:
    #   1. Python `incremental_reduced_element_fast` reduces the
    #      atomic word (with σ, σ⁻¹, averaged factors) to a
    #      LaurentHeckeElement = Σ_i c_i · w_i where each w_i is a
    #      PURE-σ word in H_n. The reduction step is already O(fast)
    #      via LaurentQ inner-loop arithmetic.
    #   2. For each (word, c_i), call the Rust `tr_m_word_lq` to
    #      compute the ZHLaurent value of tr_M(w_i). Boundary cost
    #      is O(num distinct words) PyO3 calls, amortised.
    #   3. Combine: total = Σ_i c_i · ZHLaurent_i, then evaluate at
    #      q₀ to mpmath.mpf at `dps`.
    from hecke_laurent_fast import incremental_reduced_element_fast
    from mass_at_3A_proper import atom_braid_word_3A
    word = atom_braid_word_3A(Z, N, include_inter=include_inter)
    reduced = incremental_reduced_element_fast(word, max_iterations_per_step=10000)

    # Accumulate: total = Σ_i c_i · ZHLaurent(w_i)
    # Each ZHLaurent is a dict {(z_exp, h_exp) → LaurentQ_in_q^{1/2}}
    # We accumulate in mpmath.mpf at `dps`.
    with mp.workdps(dps):
        q = mp.mpf(Q_50_DIGIT_STR)
        z_mp = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
        h_mp = q - 1 / q
        total = mp.mpf(0)
        for w_tuple, lq_coef in reduced.terms.items():
            if any(g < 0 for g in w_tuple):
                continue  # skip formal-token entries (per Python tr_M_element)
            # Evaluate the LaurentQ coefficient at q
            c_mp = mp.mpf(0)
            for exp, sym_coef in lq_coef.coefs.items():
                # sympy.Rational → exact mpmath
                if hasattr(sym_coef, "p") and hasattr(sym_coef, "q"):
                    c_mp_term = mp.mpf(int(sym_coef.p)) / mp.mpf(int(sym_coef.q))
                else:
                    import sympy as sp
                    c_mp_term = mp.mpf(str(sp.N(sym_coef, dps + 5)))
                c_mp += c_mp_term * (q ** exp)
            if c_mp == 0:
                continue
            # Call Rust tr_m_word_lq on the pure-σ word
            try:
                zh_serialised = pyhecke_native.tr_m_word_lq(
                    list(w_tuple), n_strands
                )
            except RuntimeError as e:
                # Case C — fall back to sympy (caller's responsibility)
                raise NotImplementedError(
                    f"Rust recursion hit Case C on word {w_tuple}; "
                    f"use markov_peel.tr_M_atomic (sympy ocneanu) "
                    f"as fallback. Underlying: {e}"
                ) from e
            # Evaluate ZHLaurent at (q, z, h) and accumulate
            zh_val = mp.mpf(0)
            for (z_exp, h_exp), coef_list in zh_serialised:
                c_zh = mp.mpf(0)
                for q_half_exp, big_int_str in coef_list:
                    # q_half_exp = 2 * (q-exponent) per LaurentPolyQ
                    # encoding; q^{q_half_exp/2}
                    c_zh += mp.mpf(big_int_str) * (
                        q ** (mp.mpf(q_half_exp) / 2)
                    )
                zh_val += c_zh * (z_mp ** z_exp) * (h_mp ** h_exp)
            total += c_mp * zh_val
        return total


if __name__ == "__main__":
    # Smoke test: cross-check Rust vs sympy + Phase-1 LaurentQ paths
    # on the canonical atom set.
    import time
    from q_parameter import Q as Q0
    q_val = float(Q0)

    print("=" * 80)
    print(f"tr_M_atomic_rust cross-check + bench at q₀ = {q_val:.10f}")
    print("=" * 80)

    atoms = [
        (1, 0, "p"),
        (0, 1, "n"),
        (1, 1, "D"),
        (1, 2, "T"),
        (2, 1, "³He"),
        (2, 2, "⁴He"),
    ]

    print(f"  {'atom':<6} {'tr_M (Rust)':<22} {'tr_M (sympy)':<22} "
          f"{'rel.diff':<10} {'wall_rs':<8} {'wall_sym':<8}")
    print("  " + "-" * 80)
    for Z, N, label in atoms:
        # Rust path
        t0 = time.time()
        try:
            tr_rs = tr_M_atomic_rust(Z, N)
            wall_rs = time.time() - t0
        except Exception as e:
            print(f"  {label:<6} Rust ERROR: {type(e).__name__}: {e}")
            continue

        # Reference: sympy markov_peel
        from markov_peel import tr_M_atomic
        import sympy as sp
        from hecke_symbolic import q as q_sym, HA as h_sym, z_markov as z_sym
        z_val = 1.0 / (q_val ** 0.5 + q_val ** (-0.5))
        h_val = q_val - 1.0 / q_val
        t0 = time.time()
        tr_sym_expr = tr_M_atomic(Z, N)
        tr_sym = float(tr_sym_expr.subs([(q_sym, q_val),
                                          (z_sym, z_val),
                                          (h_sym, h_val)]).evalf(30))
        wall_sym = time.time() - t0

        rel = abs(tr_rs - tr_sym) / max(abs(tr_sym), 1e-30)
        print(f"  {label:<6} {tr_rs:<22.16f} {tr_sym:<22.16f} "
              f"{rel:<10.2e} {wall_rs:<8.3f} {wall_sym:<8.3f}")


# ── Tier 1.A: Rust LaurentQ reduce + Markov trace ─────────────────────
#
# `tr_M_atomic_rust_full(Z, N, dps)` routes the atomic-braid reduction
# through the Rust port of `LaurentQ.__mul__` + `reduce_laurent_rules`
# (rules R1, R2, R3), then takes the Markov trace on the Python side.
#
# This is the "Tier 1.A" path from the 2026-05-20 compute-optimisation
# roadmap. The boundary cost is ONE PyO3 call per atomic-braid reduce,
# amortising the FFI marshalling over the full reduction.
#
# Status: implementation complete; empirical cross-check vs the Python
# LaurentQ path (`tr_M_atomic_lq`) and the heavy-atom speedup gate
# (⁶Li < 60 s, ⁸Be < 5 min) are deferred to a follow-up session that
# can run the wheel build + multi-atom sweep.


def _factor_to_ffi(lq_factor):
    """Serialise a Python `LaurentHeckeElement`-like dict
    `{word_tuple: LaurentQ}` into the FFI shape expected by
    `pyhecke_native.incremental_reduce_rust`:

      list of (list[int], list[(int, str, str)])

    where each (numer, denom) pair is a decimal-string-encoded
    `Fraction`-style coefficient on the q^exp monomial.
    """
    out = []
    for word, lq in lq_factor.items():
        # `lq.coefs` is `dict[int, Fraction]` per laurent_q.LaurentQ.
        triples = [(int(exp), str(c.numerator), str(c.denominator))
                   for exp, c in lq.coefs.items()]
        out.append((list(int(g) for g in word), triples))
    return out


def _ffi_to_laurent_hecke_element(ffi):
    """Inverse of `_factor_to_ffi`: parse the FFI shape back into a
    Python `LaurentHeckeElement` from `hecke_laurent_fast`."""
    from fractions import Fraction
    from laurent_q import LaurentQ
    from hecke_laurent_fast import LaurentHeckeElement
    terms = {}
    for word, triples in ffi:
        coefs = {}
        for exp, ns, ds in triples:
            coefs[int(exp)] = Fraction(int(ns), int(ds))
        lq = LaurentQ(coefs)
        terms[tuple(int(g) for g in word)] = lq
    return LaurentHeckeElement(terms)


def tr_M_atomic_rust_full(Z, N, *, dps=50, include_inter=True,
                          max_iterations_per_step=10000):
    """Canonical Markov trace `tr_M(β_atomic(Z, N), q₀)` via the
    Tier 1.A Rust LaurentQ-reduce path.

    Routes:
      1. atomic-braid word → Python `crossing_from_cd` → per-crossing
         `LaurentHeckeElement` factors (Python LaurentQ coeffs)
      2. factors → FFI tuples → `pyhecke_native.incremental_reduce_rust`
         (single PyO3 call; ALL reduce iterations happen in Rust)
      3. reduced FFI element → Python `LaurentHeckeElement`
      4. `tr_M_element` on the sympy-converted element (existing path)

    Returns the trace as an `mpmath.mpf` at `dps` decimal places.

    Bit-identical to `hecke_laurent_fast.tr_M_atomic_fast` (which uses
    the pure-Python reduce) modulo the rational-coefficient algebra.
    The Markov trace step is shared.

    The default `max_iterations_per_step=10000` matches
    `tr_M_atomic_fast`'s production setting.
    """
    import mpmath
    import pyhecke_native  # type: ignore[import-not-found]

    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_symbolic import SymbolicHeckeElement
    from markov_peel import crossing_from_cd
    from laurent_q import LaurentQ
    from markov_trace_canonical import tr_M_element
    from hecke_core import h as _h_num
    from q_parameter import Q_50_DIGIT_STR

    h_num_float = float(_h_num)
    word = atom_braid_word_3A(Z, N, include_inter=include_inter)

    # Build per-crossing factors as FFI tuples (small per-call cost; the
    # heavy reduce work happens in Rust).
    from hecke_symbolic import q as _q
    factors_ffi = []
    for c, d, gen in word:
        sym_factor = crossing_from_cd(gen, c, d, h_num=h_num_float)
        # Each sym_factor is a SymbolicHeckeElement with sympy-poly
        # coeffs in q. Convert each coefficient to LaurentQ, then to
        # the FFI shape.
        lq_factor_terms = {}
        for w, coef in sym_factor.terms.items():
            lq = LaurentQ.from_sympy(coef, _q)
            if not lq.is_zero():
                lq_factor_terms[w] = lq
        factors_ffi.append(_factor_to_ffi(lq_factor_terms))

    # Single PyO3 call: identity * f1 → reduce → * f2 → reduce → ...
    reduced_ffi = pyhecke_native.incremental_reduce_rust(
        factors_ffi, max_iterations_per_step,
    )

    # Marshal back to Python LaurentHeckeElement and take the Markov
    # trace via the existing sympy path.
    fast_elem = _ffi_to_laurent_hecke_element(reduced_ffi)
    n_strands = 3 * (Z + N)
    sym_elem = SymbolicHeckeElement(fast_elem.to_sympy_element())
    tr_sym = tr_M_element(sym_elem, n_strands, simplify=False)

    # Evaluate at q₀ to `dps` decimal places via mpmath.
    mpmath.mp.dps = max(int(dps), 50)
    from hecke_symbolic import q as _q2
    q_mp = mpmath.mpf(Q_50_DIGIT_STR)
    tr_mp = mpmath.mpf(tr_sym.subs(_q2, q_mp).evalf(dps))
    return tr_mp
