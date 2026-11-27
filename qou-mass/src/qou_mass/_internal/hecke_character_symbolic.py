#!/usr/bin/env python3

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
del _sys, _Path

# DEPRECATION-CANDIDATE: witness was moved to fsh-guts/deprecated/computations/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
q-deformed Hecke character χ^λ_q(T_w) — SYMBOLIC in q.

The Hoefsmit seminormal form gives explicit matrix representations
ρ_λ: H_n(q) → End(S^λ) for each partition λ ⊢ n. With q kept
symbolic (sympy.Symbol), multiplying crossing matrices through an
atomic braid word and tracing gives the exact q-character χ^λ_q(T_w)
as a rational function of q.

Compared to hecke_characters.py (numerical at q = q_0) and
murnaghan_nakayama.py (classical q = 1), this module gives the
**full q-dependent** character, distinguishing σ from σ^{-1} that
the classical MN character collapses.

Hoefsmit formulas:
  For SYT T with entries i, i+1 in cells c_i, c_{i+1}:
    ρ = content(c_{i+1}) - content(c_i)  (axial distance)

  If i, i+1 in same row (ρ = 1):
    ρ_λ(T_i) T = q · T                    (eigenvalue q)

  If i, i+1 in same column (ρ = -1):
    ρ_λ(T_i) T = -q^{-1} · T              (eigenvalue -q^{-1})

  Otherwise (ρ ≠ ±1):
    2×2 block on {T, T'} where T' swaps i, i+1:
    [[ a,    b  ],
     [ b,    a' ]]
    with a = h/(1-q^{-2ρ}), a' = h/(1-q^{2ρ}), b² = a·a'+1, h=q-q^{-1}

Scope of this module:
  - A=1 (proton, neutron): 3 partitions, max dim 2.  Fast.
  - A=2: 11 partitions, max dim 9.  Minutes symbolically.
  - A=3: 30 partitions, max dim 42.  Heavy; use with caution.
  - A=4: 77 partitions, max dim 132.  Do NOT run symbolically.
    (For A ≥ 3 use numerical hecke_characters.py with q → q_0.)

Witness: hecke-character-symbolic.witness.json
"""
import functools
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import mpmath as mp
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from sympy import Symbol, Rational, Integer, Matrix, simplify, sqrt, together

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL, Q_50_DIGIT_STR as _Q_50_DIGIT_STR
from murnaghan_nakayama import (
    partitions_of, dim_specht, hook_lengths,
    atomic_braid_word,
)


def young_diagram_cells(shape):
    cells = []
    for i, r in enumerate(shape):
        for j in range(r):
            cells.append((i, j))
    return cells


def standard_young_tableaux(shape):
    """Enumerate all SYT of given shape as a list of dicts
    {entry: cell_index}.  Returns (syts, cells, contents).
    """
    n = sum(shape)
    cells = young_diagram_cells(shape)
    contents = [c - r for r, c in cells]

    def _gen(filling, used, next_entry):
        if next_entry > n:
            yield dict(filling)
            return
        for idx, cell in enumerate(cells):
            if idx in used:
                continue
            r, c = cell
            # Check SYT validity: entry above (r-1, c) and left (r, c-1)
            # must be filled with smaller numbers.
            ok = True
            if r > 0:
                # entry above must already be filled (smaller value)
                try:
                    above = cells.index((r - 1, c))
                    if above not in used:
                        ok = False
                except ValueError:
                    pass
            if c > 0:
                try:
                    left = cells.index((r, c - 1))
                    if left not in used:
                        ok = False
                except ValueError:
                    pass
            if not ok:
                continue
            filling[next_entry] = idx
            used.add(idx)
            yield from _gen(filling, used, next_entry + 1)
            del filling[next_entry]
            used.remove(idx)

    syts = list(_gen({}, set(), 1))
    return syts, cells, contents


@functools.lru_cache(maxsize=None)
def _hoefsmit_cached(shape_key, q_name):
    """Internal cache for Hoefsmit construction keyed by (shape, q symbol name).
    `shape_key` must be a hashable tuple; `q_name` identifies the symbol so
    calls with the same `q` share the cached matrices."""
    q = sp.Symbol(q_name, positive=True, real=True)
    return _hoefsmit_build(list(shape_key), q)


def _hoefsmit_build(shape, q):
    """Uncached Hoefsmit build (used by the cached wrapper and for
    tests where q is not a named Symbol)."""
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0, []

    h = q - q ** (-1)

    matrices = []
    for k in range(1, n):
        M = sp.zeros(dim, dim)
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]

            # Diagonal entry a — `cancel` reduces the rational quickly.
            a = sp.cancel(h / (1 - q ** (-2 * rho)))

            # Find swap partner
            swap_map = dict(syts[i])
            swap_map[k], swap_map[k + 1] = ci_k1, ci_k
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap_map:
                    j = jj
                    break

            if j is None:
                # 1×1 block: eigenvalue q (same row, rho=1) or -q^{-1}
                # (same column, rho=-1).
                M[i, i] = a
                processed.add(i)
            else:
                # 2×2 block
                a_prime = sp.cancel(h / (1 - q ** (2 * rho)))
                b_sq = sp.cancel(a * a_prime + 1)
                b = sp.sqrt(b_sq)
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed.add(i)
                processed.add(j)
        matrices.append(M)
    return matrices, dim, syts


def hoefsmit_matrices_symbolic(shape, q):
    """Build symbolic Hoefsmit matrices ρ_λ(T_1), ..., ρ_λ(T_{n-1})
    for partition `shape`.  Entries are rational functions of q.

    Cached when `q` is a named sympy Symbol; falls back to an uncached
    build otherwise (e.g. when `q` is a concrete Rational for evaluation).
    """
    if isinstance(q, sp.Symbol):
        return _hoefsmit_cached(tuple(shape), q.name)
    return _hoefsmit_build(shape, q)


# In-memory cache for χ^λ_q(T_w) keyed by (shape, frozen braid word, q symbol).
# Avoids recomputing the Hoefsmit-matrix-product trace when the same
# (partition, braid_word) pair is queried twice in a single process —
# e.g. when habiro_coefficients_atomic evaluates atoms p, n, D in
# sequence and several share generator-index sub-words.
@functools.lru_cache(maxsize=None)
def _q_character_cached_impl(shape_key: tuple, braid_key: tuple,
                              q_name: str) -> "sp.Expr":
    """Cached inner implementation; called via q_character_on_braid_word
    when q is a sympy Symbol whose name fully identifies it."""
    q = sp.Symbol(q_name, positive=True, real=True) if q_name else sp.Symbol("q")
    return _q_character_compute(list(shape_key), list(braid_key), q)


def _q_character_compute(shape, braid_crossings, q):
    """Pure compute path (no caching).  Multiplies Hoefsmit matrices
    through the braid word and returns the trace."""
    matrices, dim, _ = hoefsmit_matrices_symbolic(shape, q)
    if dim == 0:
        return Integer(0)
    h = q - q ** (-1)
    M = sp.eye(dim)
    for gen_idx, cross_d in braid_crossings:
        if gen_idx < 0 or gen_idx >= len(matrices):
            raise IndexError(f"gen_idx {gen_idx} out of range for shape {shape}")
        sigma = matrices[gen_idx]
        from canonical_braid_crossings import d_for_ctype
        from _li_2_q_util import flavor_split_leading
        # was an inline {sigma, sigma_inv, averaged} map; averaged
        # swallowed the colour-weighted p-n interface.
        #
        # `delta=` is REQUIRED here, not optional. This function's `q` is
        # always symbolic — it is the symbolic path — so it is exactly the
        # "q-symbolic caller" `d_for_ctype`'s docstring adds the parameter
        # for. Taking the default evaluates `_avg_color_delta()` at the
        # numeric `q_parameter.Q`, so an `averaged_weighted` crossing came
        # back as `-0.499656072298243*q + 0.499656072298243/q` — two Float
        # atoms — and every symbolic χ^λ for a word with a p-n interface
        # (A >= 2: deuteron, tritium, helium-3, ...) silently carried a
        # q0-pinned coefficient while presenting as a function of q.
        # Evaluating such a χ at any other q returned a wrong number, which
        # is the ideal/experimental straddle AGENTS.md rules out regardless
        # of size.
        #
        # `markov_peel.crossing_from_cd` has always done this correctly,
        # substituting the closed form symbolically; that is why the peel's
        # tr_M is Float-free and this path's χ was not.
        d_val = d_for_ctype(cross_d, h, delta=flavor_split_leading(q))

        cross = sigma + d_val * sp.eye(dim)
        M = M * cross
        # `cancel` — polynomial-division on rationals — is 5–10×
        # faster than `simplify` and sufficient to keep entry
        # complexity bounded for Hecke-algebra traces.
        M = M.applyfunc(sp.cancel)
    return sp.cancel(M.trace())


# Lazy χ^λ map: (atom_label, partition tuple) → sympy-string, parsed on
# first request only.  Backed by chi-{atom}-h{n}.witness.json caches that
# already exist for atoms whose Hoefsmit-matrix products are too
# expensive to recompute (n ≥ 6).
_CHI_WITNESS_STRINGS: dict[str, dict[tuple, str]] = {}


def _load_chi_witness(atom_label: str) -> dict[tuple, str]:
    """Read chi-{atom_label}-h{n}.witness.json (n implied by atom_label)
    and return {partition_tuple: chi_q_symbolic_string}.  Cached per
    atom_label; lazy on first request."""
    if atom_label in _CHI_WITNESS_STRINGS:
        return _CHI_WITNESS_STRINGS[atom_label]
    out: dict[tuple, str] = {}
    here = Path(__file__).parent
    # Try canonical naming patterns.  chi-deuteron-h6, chi-tritium-h9,
    # chi-helium-3-h9, etc.
    for pattern in (
        f"chi-{atom_label}-h*.witness.json",
        f"chi-{atom_label}.witness.json",
    ):
        for path in sorted(here.glob(pattern)):
            try:
                with path.open() as f:
                    doc = json.load(f)
                entries = doc.get("chi_lambda_symbolic")
                if not isinstance(entries, list):
                    continue
                for w in entries:
                    try:
                        lam = tuple(w["partition"])
                        out[lam] = w["chi_q_symbolic"]
                    except (KeyError, TypeError):
                        continue
            except Exception:
                continue
            if out:
                break
        if out:
            break
    _CHI_WITNESS_STRINGS[atom_label] = out
    return out


def q_character_on_braid_word(shape, braid_crossings, q,
                                *, atom_cache_label: str | None = None):
    """Compute χ^λ_q(T_w) symbolically for a braid word represented as
    a list of (gen_index, (c, d)) pairs.  Each crossing contributes
    c · ρ_λ(T_gen) + d · I_dim to the product; the final trace is the
    q-character.

    For the atomic braid: c = 1, d ∈ {0, -h, -h/2} depending on
    crossing type (σ, σ^{-1}, averaged).

    Optimizations:

    - **Witness-cache lookup** (preferred for n ≥ 6): if
      `atom_cache_label` is supplied (e.g. ``"deuteron"``,
      ``"tritium"``, ``"helium-3"``) the function consults the
      committed `chi-{label}-h{n}.witness.json` cache for the
      requested partition.  These caches store the closed-form
      symbolic χ^λ_q(β_atom) values (155+ s first-run compute) and
      let downstream consumers skip the Hoefsmit-matrix-product
      recomputation.  Returns the cached value when present.
    - **In-memory lru_cache** (always on for sympy.Symbol q):
      caches the final trace by `(shape, tuple(braid_crossings),
      q.name)` so repeated calls in a single process hit the
      previous result.

    Returns sympy expression for χ^λ_q(T_w).
    """
    # 1. Witness-cache hit — most expensive computations skipped.
    if atom_cache_label is not None:
        cache = _load_chi_witness(atom_cache_label)
        lam = tuple(shape)
        if lam in cache:
            try:
                # Bind q-string to the caller's q symbol.  The cached
                # strings always use the bare name "q"; sympify via
                # `locals={"q": q}` ensures the returned expression
                # composes with downstream callers' q.
                return sp.sympify(cache[lam], locals={"q": q})
            except (sp.SympifyError, SyntaxError, ValueError):
                pass  # fall through to recompute

    # 2. In-memory lru_cache for pure-Symbol q (Symbols are cheap to key
    # by name; non-Symbol q goes straight to compute since cache keys
    # would be unstable).
    if isinstance(q, sp.Symbol):
        return _q_character_cached_impl(
            tuple(shape), tuple(braid_crossings), q.name
        )

    # 3. Fall through: pure compute (no caching available).
    return _q_character_compute(shape, braid_crossings, q)


# `atomic_braid_to_crossings` was REMOVED in PR #572 commit
# (this file's most recent edit).  The function used a non-canonical
# disjoint-product convention that did NOT reproduce the canonical
# Markov-trace reducer's |tr_M(β)| values for multi-nucleon atoms
# (per #564 commit c068550c "P3' canonical word fix" + #572 audit
# `docs/audits/2026-05-08-q-hecke-character-gap-closure.md`).
#
# Use `canonical_braid_crossings.atom_canonical_crossings(Z, N)`
# instead — bridges `mass_at_3A_proper.atom_braid_word_3A` (canonical
# convention) → (gen_idx, ctype) format consumable by
# `q_character_on_braid_word` and `chi_lambda_symbolic`.
#
# For backward-compatibility imports `from hecke_character_symbolic
# import atomic_braid_to_crossings` we re-export the canonical
# function under the old name; the underlying convention is now
# correct (operator-valued interface I = σ_{n_1} − h/2·1 instead of
# disjoint product).
from canonical_braid_crossings import (
    atom_canonical_crossings as atomic_braid_to_crossings,  # noqa: F401
)


# ─── Main: prove q-character distinguishes proton from neutron ──────────

# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

if __name__ == "__main__":
    print("HECKE q-CHARACTER SYMBOLIC — closes the parity-blind gap")
    print("=" * 80)

    q = sp.Symbol('q', positive=True, real=True)
    q0 = Rational(_Q_50_DIGIT_STR)  # was a 16-digit truncation of float Q (F64_CAST, 2026-11-21)

    # A = 1 full test: proton and neutron
    print("\n── A = 1 q-character across all 3 partitions ──")
    results = {}
    for label, Z, N in [("p", 1, 0), ("n", 0, 1)]:
        crossings = atomic_braid_to_crossings(Z, N, include_inter=False)
        print(f"\n  {label}: braid length = {len(crossings)}")
        per_lambda = {}
        for lam in partitions_of(3):
            chi = q_character_on_braid_word(lam, crossings, q)
            # Keep substrate precision via mp.mpf (numeric — supports
            # :+.6e format AND WitnessBuilder default=str serialization,
            # per compute_no_mpf_to_float_cast + Copilot #2050 pattern).
            chi_at_q0 = mp.mpf(str(chi.subs(q, q0).evalf(50)))
            chi_at_q0_polynomial_q = expose_polynomial(chi, q)
            per_lambda[str(lam)] = {
                "symbolic": str(sp.nsimplify(chi)),
                "at_q0": chi_at_q0,
            }
            print(f"    λ = {lam!s:<12}  χ^λ_q(T_w) @ q_0 = "
                  f"{chi_at_q0:+.6e}")
        results[label] = per_lambda

    # Verify p and n differ at q_0
    print("\n── Proton vs Neutron comparison ──")
    p_chars = results["p"]
    n_chars = results["n"]
    for lam_str in p_chars:
        p_val = p_chars[lam_str]["at_q0"]
        n_val = n_chars[lam_str]["at_q0"]
        diff = p_val - n_val
        print(f"  λ = {lam_str:<12}  χ^λ_q(p) - χ^λ_q(n) @ q_0 = "
              f"{diff:+.6e}  "
              f"[{'SAME' if abs(diff) < 1e-9 else 'DIFFER'}]")

    # Schur-Weyl sum for p and n at A=1
    print("\n── Schur-Weyl mass trace at A = 1 ──")
    from schur_weyl_symbolic import schur_weyl_weight
    for label in ["p", "n"]:
        total = Integer(0)
        for lam in partitions_of(3):
            w = schur_weyl_weight(lam, q)
            chi = q_character_on_braid_word(
                lam, atomic_braid_to_crossings(
                    {"p": 1, "n": 0}[label], {"p": 0, "n": 1}[label],
                    include_inter=False),
                q,
            )
            total += w * chi
        total = sp.simplify(total)
        total_q0 = mp.mpf(str(total.subs(q, q0).evalf(50)))
        total_q0_polynomial_q = expose_polynomial(total, q)
        print(f"  |tr_M({label})| @ q_0 = {abs(total_q0):+.6e}")
        results[f"{label}_total"] = {
            "symbolic": str(sp.nsimplify(total)),
            "at_q0": total_q0,
        }

    # Proton-neutron splitting
    if "p_total" in results and "n_total" in results:
        Q_cat = results["n_total"]["at_q0"] - results["p_total"]["at_q0"]
        print(f"\n  Q_cat = tr_M(n) - tr_M(p) = {Q_cat:+.6e}")
        if abs(Q_cat) > 1e-12:
            from experimental_constants import Q_NEUTRON_MEV
            E_0 = float(Q_NEUTRON_MEV) / abs(Q_cat)
            print(f"  E_0 = Q_β(n) / |Q_cat| = {E_0:+.6e} MeV/cat.unit "
                  f"(Q_β = {float(Q_NEUTRON_MEV):.8f} MeV)")
            print(f"  [CALIBRATION SUCCEEDS — q-character distinguishes p/n]")
        else:
            print(f"  [Q_cat = 0: q-character STILL parity-blind for this "
                  f"crossing structure]")

    witness = {
        "computation": "hecke-character-symbolic",
        "description": (
            "q-deformed Hecke character χ^λ_q(T_w) symbolic in q via "
            "Hoefsmit seminormal matrices.  Replaces the classical "
            "Murnaghan-Nakayama character (parity-blind at q=1) for A=1. "
            "For A ≥ 2 the symbolic matrix product is costly; use "
            "numerical hecke_characters.py instead."
        ),
        "reference_blocks": [
            "prop:schur-weyl-mass-decomposition",
            "rem:mn-classical-parity-blind",
        ],
        "scope": "A = 1 only (p, n) — demonstrates q-character distinguishes.",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": _Q_50_DIGIT_STR,
            "engine": "sympy Matrix (exact in q)",
        },
        "results": results,
    }
    out = Path(__file__).parent / "hecke-character-symbolic.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
