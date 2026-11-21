#!/usr/bin/env python3
"""per_irrep_pole_atom_crystal.py — crystal-bases Path A pole-order
verifier for **any atom (Z, N)**, including ⁴He at H_12 where the
existing GS-reduction-bound `per_irrep_pole_atom.py` doesn't return.

**Replaces** the symbolic `chi_lambda_symbolic` per-partition compute
with a per-SYT-eigenline u-pole tally, valid in the Kashiwara crystal
limit q → 0:

    χ^λ(β)(q = u²)  =  Σ_{T ∈ SYT(λ)}  Π_{letter ∈ β}  eig_letter,T(u)

Per-letter `eig_letter,T(u)` (q = u², h = q - q⁻¹):

| letter `(c, d, gen)` | eig on T sym (ρ_T(gen) > 0) | eig on T anti (ρ_T(gen) < 0) |
|---|---|---|
| σ        (`d = 0`)    | `q = u²`     | `−q⁻¹ = −u⁻²` |
| σ⁻¹      (`d = −h`)   | `q⁻¹ = u⁻²`  | `−q = −u²`    |
| Δ_I      (`d = −h/2`) | `+½(u² + u⁻²)` | `−½(u² + u⁻²)` |

For each SYT `T`, the eigenvalue product is a Laurent monomial in `u`
(for σ/σ⁻¹) or a sum of two monomials (for Δ_I).  The **dominant
u-pole** at u → 0 picks the most-negative power.  Per-letter
contributions to `ord_{u=0}` of the eigenvalue product on `T`:

| letter | ρ > 0 (sym) | ρ < 0 (anti) | ρ = 0 (degen) |
|---|--:|--:|--:|
| σ        | +2  | −2  | (treated as zero contribution) |
| σ⁻¹      | −2  | +2  | (zero) |
| Δ_I      | −2  | −2  | (zero) |

The leading-coefficient sign factor per letter:

| letter | ρ > 0 sign | ρ < 0 sign |
|---|--:|--:|
| σ        | +1  | −1  |
| σ⁻¹      | +1  | −1  |
| Δ_I      | +½  | −½  |

Per-T `(ord_T, leading_coeff_T)`:
- `ord_T   = Σ per-letter contribution`
- `coeff_T = Π per-letter sign factor` (rational; tracks signed ½ from Δ_I)

Per-λ `(ord_λ, coeff_λ)`:
- `ord_λ   = min over T of ord_T` (most-negative)
- `coeff_λ = Σ over T (with ord_T == ord_λ) of coeff_T`
- if `coeff_λ == 0`: leading-coefficient cancellation; need higher-
  order analysis (here we re-take min over surviving T)

Per-atom `ord_{u=0}(tr_M) = min over λ of (ord_y_λ + ord_χ^λ)` where
`ord_y_λ` is computed symbolically from the cached Wenzl-bridge
`y_λ(q)` after `q → u²` substitution.  Pole order = `−ord` (when
negative), matching the existing `negative_q_pole_order` convention.

Predicted shifts (per `prop:per-nucleon-shift-additive-linearity`):

| atom | (Z, N) | n | shift |
|------|---|---|---|
| p    | (1, 0) | 3  | 19  |
| n    | (0, 1) | 3  | 22  |
| D    | (1, 1) | 6  | 40  |
| T    | (1, 2) | 9  | 61  |
| ³He  | (2, 1) | 9  | 58  |
| ⁴He  | (2, 2) | 12 | 79  |
| ⁵Li  | (3, 2) | 15 | 97  |
| ⁶Li  | (3, 3) | 18 | 118 |

Output: aggregate `per-irrep-pole-atom-crystal.witness.json` with
one row per atom processed (per-partition data nested inside).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp

from witness_base import WitnessBuilder
from canonical_braid_crossings import atom_canonical_crossings
from hecke_characters import standard_young_tableaux, partitions_of


ATOMS = [
    # (label, Z, N, expected_shift, asserted)
    # `asserted=True`  → contributes to the `all_atoms_match...` gate.
    # `asserted=False` → computed and reported, but excluded from the
    #   gate (used for atoms outside the verified scope of the closed
    #   form, e.g. the neutron at A=1 — see rem:crystal-bases-path-a
    #   §"A=1 anomaly").
    ("proton",   1, 0, 18 * 1 + 21 * 0 + 1, True),
    ("neutron",  0, 1, 18 * 0 + 21 * 1 + 1, False),  # A=1 extrap; see remark
    ("deuteron", 1, 1, 18 * 1 + 21 * 1 + 1, True),
    ("tritium",  1, 2, 18 * 1 + 21 * 2 + 1, True),
    ("helium-3", 2, 1, 18 * 2 + 21 * 1 + 1, True),
    ("helium-4", 2, 2, 18 * 2 + 21 * 2 + 1, True),
    ("lithium-5", 3, 2, 18 * 3 + 21 * 2 + 1, True),
    ("lithium-6", 3, 3, 18 * 3 + 21 * 3 + 1, True),
]


# ───────────────────────────────────────────────────────────────────
# Caches (Phase 2: C1, C2)
# ───────────────────────────────────────────────────────────────────

@lru_cache(maxsize=None)
def _syt_for_shape(shape: tuple[int, ...]) -> tuple:
    """C1: cached `(syts, cells, contents)` for a partition shape."""
    return standard_young_tableaux(shape)


@lru_cache(maxsize=None)
def _rho_table_for_shape(
    shape: tuple[int, ...],
    n_strands: int,
) -> tuple[tuple[int, ...], ...]:
    """C2: precompute `ρ_T(gen)` for every (T, gen) pair.

    Returns: tuple-of-tuples `rho[t_idx][gen_idx] = ρ_T(gen_idx)`,
    or `None` if T doesn't have both entries (gen_idx+1, gen_idx+2).

    Encoded ρ-categorisation:
        ρ > 0  → +1   (sym eigenline)
        ρ < 0  → -1   (anti eigenline)
        ρ = 0  → 0    (degenerate; treated as zero contribution)
        N/A    → -2   (vacuum: T missing the entry pair for this gen)
    """
    syts, _cells, contents = _syt_for_shape(shape)
    table = []
    for T in syts:
        row = []
        for gen in range(n_strands - 1):
            e_lo = gen + 1
            e_hi = gen + 2
            if e_lo not in T or e_hi not in T:
                row.append(-2)  # vacuum
                continue
            rho = contents[T[e_hi]] - contents[T[e_lo]]
            if rho > 0:
                row.append(1)
            elif rho < 0:
                row.append(-1)
            else:
                row.append(0)
        table.append(tuple(row))
    return tuple(table)


# ───────────────────────────────────────────────────────────────────
# Per-letter pole / sign contributions (the crystal-limit lookup)
# ───────────────────────────────────────────────────────────────────

# Indexed by (ctype, rho_class) → (ord_delta, sign_factor).
# rho_class: 1 (sym), -1 (anti), 0 (degenerate).  sign_factor is a
# Rational (may be ±½ for Δ_I letters).

_LETTER_CONTRIB: dict[tuple[str, int], tuple[int, sp.Rational]] = {
    ("sigma",     1):  (2, sp.Integer(1)),    # σ on sym:  eig = u²,  +2
    ("sigma",    -1):  (-2, sp.Integer(-1)),  # σ on anti: eig = -u⁻², -2
    ("sigma",     0):  (None, sp.Integer(0)), # degenerate
    ("sigma_inv", 1):  (-2, sp.Integer(1)),   # σ⁻¹ on sym:  eig = u⁻², -2
    ("sigma_inv",-1):  (2, sp.Integer(-1)),   # σ⁻¹ on anti: eig = -u², +2
    ("sigma_inv", 0):  (None, sp.Integer(0)),
    ("averaged",  1):  (-2, sp.Rational(1, 2)),   # Δ_I on sym:  +½ u⁻²
    ("averaged", -1):  (-2, sp.Rational(-1, 2)),  # Δ_I on anti: -½ u⁻²
    ("averaged",  0):  (None, sp.Integer(0)),
    # The colour-weighted p-n interface shares the colour-blind entries, and
    # that is derived rather than convenient:
    #
    #   * its d is -h(1/2 - δ/4) not -h/2, so its exact coefficient would be
    #     (1/2 - δ/4) with δ ≈ 1.376e-3 — which changes neither the u-ORDER
    #     (still -2) nor the SIGN, the two things this table feeds;
    #   * `coeff` is consumed as an EXACT RATIONAL: coeff_λ = Σ_T coeff_T,
    #     and the method's key signal is `coeff_λ == 0`, leading-coefficient
    #     cancellation. Carrying (1/2 - δ/4) as a float would make that sum
    #     essentially never exactly zero and destroy the cancellation test.
    #
    # So the crystal limit resolves order and exact cancellation; the colour
    # weighting is an O(δ) coefficient correction it does not resolve —
    # stated here rather than left silent. Without these rows the lookup
    # raised KeyError on every Z>=1,N>=1 word (qou-8zjd).
    ("averaged_weighted",  1):  (-2, sp.Rational(1, 2)),
    ("averaged_weighted", -1):  (-2, sp.Rational(-1, 2)),
    ("averaged_weighted",  0):  (None, sp.Integer(0)),
}


def _per_T_ord_and_coeff(
    rho_row: tuple[int, ...],
    crossings: tuple[tuple[int, str], ...],
) -> tuple[int | None, sp.Rational]:
    """Compute `(ord_{u=0}(eig_T), leading_coeff_T)` on a single SYT.

    Returns `(None, 0)` if T's contribution vanishes (any zero
    sign-factor or any vacuum letter that should be present).
    """
    ord_u = 0
    coeff = sp.Integer(1)
    for gen, ctype in crossings:
        rho_class = rho_row[gen]
        if rho_class == -2:
            # Vacuum: T doesn't have entries (gen+1, gen+2).
            # Per the existing per_irrep_pole_*.py convention this
            # case never arises for height-≤6 partitions of 3A
            # because every gen ∈ {0, …, 3A-2} is acted on by the
            # canonical word, and the partition has enough cells.
            # If we hit it, treat conservatively as zero.
            return (None, sp.Integer(0))
        delta, sf = _LETTER_CONTRIB[(ctype, rho_class)]
        if delta is None:
            return (None, sp.Integer(0))
        ord_u += delta
        coeff *= sf
        if coeff == 0:
            return (None, sp.Integer(0))
    return (ord_u, coeff)


def chi_pole_order_crystal(
    shape: tuple[int, ...],
    n_strands: int,
    crossings: tuple[tuple[int, str], ...],
) -> tuple[int | None, sp.Rational, int]:
    """Crystal-asymptotic `(ord_χ, coeff_χ, n_T_at_min)` per partition.

    Returns:
      ord_χ        — `ord_{u=0}(χ^λ(β))` (most-negative u-power
                     surviving non-zero leading coefficient), or
                     `None` if the leading coefficients cancel.
      coeff_χ      — leading coefficient at `ord_χ` (sympy Rational).
      n_T_at_min   — number of SYTs achieving `ord_χ` (for unique-max
                     diagnostic).
    """
    rho_table = _rho_table_for_shape(shape, n_strands)
    contributions: list[tuple[int, sp.Rational]] = []
    for rho_row in rho_table:
        ord_T, coeff_T = _per_T_ord_and_coeff(rho_row, crossings)
        if ord_T is not None:
            contributions.append((ord_T, coeff_T))
    if not contributions:
        return (None, sp.Integer(0), 0)
    # Sort ascending by ord_u: most-negative first.
    contributions.sort(key=lambda r: r[0])
    # Walk from the most-negative until we find a non-zero leading
    # coefficient sum (handles cancellation by going to next-higher
    # order).
    i = 0
    while i < len(contributions):
        cur_ord = contributions[i][0]
        j = i
        leading = sp.Integer(0)
        while j < len(contributions) and contributions[j][0] == cur_ord:
            leading += contributions[j][1]
            j += 1
        if leading != 0:
            return (cur_ord, leading, j - i)
        i = j
    # Total cancellation across all T — chi^λ vanishes.
    return (None, sp.Integer(0), 0)


# ───────────────────────────────────────────────────────────────────
# y_λ pole order (Wenzl-bridge symbolic; cached witness on disk)
# ───────────────────────────────────────────────────────────────────

_Q_SYM = sp.Symbol("q")              # match sympify default (no flag)
_U_SYM = sp.Symbol("u", positive=True)  # so sqrt(u²) → u
_Y_LAMBDA_CACHE: dict[int, dict[tuple[int, ...], sp.Expr]] = {}
_Y_POLE_CACHE: dict[int, dict[tuple[int, ...], int | None]] = {}


def _load_y_pole_cache_disk() -> dict[int, dict[tuple[int, ...], int]]:
    """Load the precomputed `ord_{u=0}(y_λ)` cache from
    `y-lambda-pole-order-cache.json` (built once by
    `y_lambda_pole_order_cache.py`).  Returns `{}` if cache file
    missing — caller falls back to the slow sympy path."""
    import json
    here = Path(__file__).parent
    path = here / "y-lambda-pole-order-cache.json"
    if not path.exists():
        return {}
    w = json.loads(path.read_text())
    out: dict[int, dict[tuple[int, ...], int]] = {}
    for n_key, n_data in w.get("by_n", {}).items():
        n = int(n_key)
        out[n] = {}
        for r in n_data.get("partitions", []):
            shape = tuple(r["partition"])
            ord_y = r.get("ord_y_at_u_eq_0")
            if ord_y is not None:
                out[n][shape] = int(ord_y)
    return out


def _load_y_lambda_n(n: int) -> dict[tuple[int, ...], sp.Expr]:
    """Load symbolic `y_λ(q)` for partitions of `n` from the cached
    Wenzl-bridge witness (slow fallback path)."""
    if n in _Y_LAMBDA_CACHE:
        return _Y_LAMBDA_CACHE[n]
    import json
    here = Path(__file__).parent
    path = here / "y-lambda-wenzl-bridge-symbolic-witness.json"
    w = json.loads(path.read_text())
    tables = w["tables_by_n"]
    if str(n) not in tables:
        # Lithium-5 (n=15) and Lithium-6 (n=18) hit this. It used to surface
        # as a bare `KeyError` printed by the caller as `ERROR '15'`, which
        # reads like a crash and is really "the data does not go that far".
        have = sorted(int(k) for k in tables)
        raise KeyError(
            f"no y_lambda table for n={n} in {path.name} (have n={have}); "
            f"and the fast pole-order cache does not cover it either. "
            f"Extend the symbolic witness via y_lambda_wenzl_bridge, or add "
            f"n={n} to y-lambda-pole-order-cache.json via "
            f"y_lambda_pole_order_cache.py, before asking for this atom."
        )
    rows = tables[str(n)]["weights"]
    out: dict[tuple[int, ...], sp.Expr] = {}
    for r in rows:
        shape = tuple(r["partition"])
        out[shape] = sp.sympify(r["y_lambda_symbolic"])
    _Y_LAMBDA_CACHE[n] = out
    return out


def y_lambda_pole_order_in_u(
    shape: tuple[int, ...],
    n: int,
) -> int | None:
    """`ord_{u=0}(y_λ(u²))`.  Looked up from the precomputed pole-
    order cache when available; otherwise falls back to symbolic
    sympy (slow at H_n ≥ 9)."""
    # Fast path: precomputed cache.
    if not _Y_POLE_CACHE:
        _Y_POLE_CACHE.update(_load_y_pole_cache_disk())
    if n in _Y_POLE_CACHE and shape in _Y_POLE_CACHE[n]:
        return _Y_POLE_CACHE[n][shape]
    # Slow fallback: sympy simplify.
    y_lams = _load_y_lambda_n(n)
    if shape not in y_lams:
        return None
    y_q = y_lams[shape]
    y_u = sp.simplify(y_q.subs(_Q_SYM, _U_SYM ** 2))
    if y_u == 0:
        return None
    n_, d_ = sp.fraction(y_u)
    n_poly = sp.Poly(n_, _U_SYM)
    d_poly = sp.Poly(d_, _U_SYM)
    n_low = min(m[0] for m in n_poly.monoms()) if n_poly.monoms() else 0
    d_low = min(m[0] for m in d_poly.monoms()) if d_poly.monoms() else 0
    return n_low - d_low


# ───────────────────────────────────────────────────────────────────
# Per-atom verification
# ───────────────────────────────────────────────────────────────────

def _height_le_6_partitions(n: int) -> list[tuple[int, ...]]:
    return [tuple(p) for p in partitions_of(n) if len(p) <= 6]


def verify_atom(
    label: str,
    Z: int,
    N: int,
    expected_shift: int,
    asserted: bool = True,
    *,
    verbose: bool = True,
) -> dict:
    """Compute crystal-asymptotic `ord_{u=0}(tr_M(β_atom))` and
    compare to the predicted `expected_shift`.

    Returns dict suitable for witness JSON.
    """
    A = Z + N
    n = 3 * A
    crossings = tuple(atom_canonical_crossings(Z, N))
    partitions = _height_le_6_partitions(n)
    if verbose:
        print(f"  {label:<10} (Z={Z}, N={N}, n={n}, "
              f"|word|={len(crossings)}, |partitions|={len(partitions)})",
              flush=True)

    t0 = time.time()
    rows = []
    # Pole order of tr_M = max over λ of pole(y_λ · χ^λ) in pole-
    # order convention (= -ord_{u=0}).  Equivalently min over λ of
    # ord_{u=0}(y_λ · χ^λ).
    min_ord = None
    min_lam = None
    second_min_ord = None
    for shape in partitions:
        ord_chi, coeff_chi, n_T = chi_pole_order_crystal(
            shape, n, crossings)
        ord_y = y_lambda_pole_order_in_u(shape, n)
        if ord_chi is None or ord_y is None:
            total_ord = None
        else:
            total_ord = ord_y + ord_chi
        rows.append({
            "lambda": list(shape),
            "ord_y_at_u_0": ord_y,
            "ord_chi_at_u_0": ord_chi,
            "n_T_at_min": n_T,
            "leading_coeff_chi": str(coeff_chi),
            "total_ord_y_chi": total_ord,
        })
        if total_ord is not None:
            if min_ord is None or total_ord < min_ord:
                second_min_ord = min_ord
                min_ord = total_ord
                min_lam = shape
            elif second_min_ord is None or total_ord < second_min_ord:
                if total_ord != min_ord:
                    second_min_ord = total_ord
    elapsed = time.time() - t0

    pole_order = -min_ord if min_ord is not None and min_ord < 0 else 0
    match = (pole_order == expected_shift)

    if verbose:
        print(f"    ord_min  = {min_ord}    (λ_min = {min_lam})", flush=True)
        print(f"    pole_u   = {pole_order}    expected = {expected_shift}    "
              f"{'MATCH ✓' if match else 'MISMATCH ✗'}", flush=True)
        print(f"    elapsed  = {elapsed:.2f}s", flush=True)
        print(flush=True)

    return {
        "atom": label, "Z": Z, "N": N, "A": A, "n_strands": n,
        "n_partitions": len(partitions),
        "word_length": len(crossings),
        "min_total_ord_u_eq_0": min_ord,
        "min_total_lambda": list(min_lam) if min_lam else None,
        "second_min_total_ord": second_min_ord,
        "u_pole_order_inferred": pole_order,
        "expected_shift": expected_shift,
        "match": match,
        "asserted": asserted,
        # Wall-clock, reported to ms as a string: it is diagnostic timing,
        # never an input to anything, and a bare float64 here trips the
        # precision gate for no benefit (bean qou-g94g).
        "elapsed_sec": f"{elapsed:.3f}",
        "per_partition": rows,
    }


def _selftest() -> int:
    """Fast self-test (bean qou-g94g): verify proton and deuteron crystal
    u-pole orders and the measured 16Z + 20N + 2 vs asserted 18Z + 21N + 1
    gap without overwriting the committed witness."""
    r_p = verify_atom("proton", 1, 0, 19, asserted=True, verbose=False)
    r_d = verify_atom("²H", 1, 1, 40, asserted=True, verbose=False)
    assert r_p["u_pole_order_inferred"] == 16 * 1 + 20 * 0 + 2 == 18, r_p
    assert r_p["expected_shift"] == 18 * 1 + 21 * 0 + 1 == 19, r_p
    assert r_d["u_pole_order_inferred"] == 16 * 1 + 20 * 1 + 2 == 38, r_d
    assert r_d["expected_shift"] == 18 * 1 + 21 * 1 + 1 == 40, r_d
    print("self-test: ok (proton pole_u=18 vs 19; deuteron pole_u=38 vs 40)")
    return 0


def main(argv: list[str]) -> int:
    """Run the crystal-asymptotic Path A pole-order check across
    all listed atoms.  Stops at the first MISMATCH unless
    `--continue-on-mismatch` is passed."""
    if "--self-test" in argv or "--selftest" in argv:
        return _selftest()
    cont = "--continue-on-mismatch" in argv
    only = None
    if "--only" in argv:
        only = argv[argv.index("--only") + 1]

    print("=" * 70, flush=True)
    print(" Per-irrep pole order — crystal-bases (Path A; "
          "GS-reduction-free)", flush=True)
    print("=" * 70, flush=True)

    out = (WitnessBuilder("per-irrep-pole-atom-crystal", engine="sympy")
        .set_content_block("rem:crystal-bases-path-a")
        .set_description(
            "Crystal-bases Path A pole-order verification of "
            "shift_NF(β_K) = 18Z + 21N + 1 for each atom K, "
            "computed via per-SYT-eigenline u-pole tally at q → 0 "
            "(Kashiwara crystal limit) on the canonical Δ_I-coupled "
            "atomic braid word.  Replaces the GS-reduction-bound "
            "per_irrep_pole_atom.py path that doesn't return at H_12. "
            "Per-letter contributions: σ on sym/anti = ±2; σ⁻¹ on "
            "sym/anti = ∓2; Δ_I = -2 always (leading u⁻² term)."
        )
        .add_data("conditional_on", ["conj:crystal-graph-realization"])
        .add_data("inputs", {
            "atom_braid_words":
                "mass_at_3A_proper.atom_braid_word_3A "
                "(canonical Δ_I-coupled (gen, ctype) crossings)",
            "y_lambda":
                "y-lambda-wenzl-bridge-symbolic-witness.json "
                "(symbolic Wenzl-bridge per partition)",
            "chi_lambda_pole_order":
                "per-SYT crystal-limit u-power tally (this script); "
                "no symbolic-q matrix multiplication",
        })
    )

    atoms_results = []
    asserted_match = True       # gate: asserted atoms only (A ≥ 2 + proton)
    full_match = True           # diagnostic: includes A=1 extrapolations
    for atom_entry in ATOMS:
        label, Z, N, expected = atom_entry[0], atom_entry[1], atom_entry[2], atom_entry[3]
        asserted = atom_entry[4] if len(atom_entry) > 4 else True
        if only and label != only:
            continue
        try:
            row = verify_atom(label, Z, N, expected, asserted=asserted)
        except Exception as e:
            print(f"  ✗ {label}: ERROR {e}", flush=True)
            full_match = False
            if asserted:
                asserted_match = False
            if not cont:
                break
            continue
        atoms_results.append(row)
        if not row["match"]:
            full_match = False
            if asserted:
                asserted_match = False
                if not cont:
                    print(f"  Stopping at first ASSERTED mismatch "
                          f"({label}). Pass --continue-on-mismatch to "
                          f"override.", flush=True)
                    break

    asserted_atoms = [r["atom"] for r in atoms_results if r.get("asserted", True)]
    n_asserted = sum(1 for r in atoms_results if r.get("asserted", True))
    out.add_data("atoms", atoms_results)

    # WHAT THE CRYSTAL PATH ACTUALLY MEASURES (bean qou-g94g)
    # ------------------------------------------------------
    # The bean recorded this as "pole_u off by exactly one at the first atom",
    # which reads like an index convention. Running every atom instead of
    # stopping at the first mismatch shows it is not: the gap GROWS.
    #
    #   atom       Z  N  measured  18Z+21N+1  gap
    #   proton     1  0        18         19    1
    #   neutron    0  1        18         22    4      <- A=1 anomaly, not asserted
    #   deuteron   1  1        38         40    2
    #   tritium    1  2        58         61    3
    #   helium-3   2  1        54         58    4
    #   helium-4   2  2        74         79    5
    #
    # Solving the four A>=2 atoms exactly gives `16Z + 20N + 2`, and that law
    # ALSO reproduces the proton (16+0+2 = 18). So five of six atoms fit a
    # single clean linear law that is not the asserted one, and the gap is
    # exactly `2Z + N - 1` on those five. The sixth is the A=1 neutron, which
    # is anomalous under BOTH laws (both predict 22, measured 18) and is
    # already `asserted=False` per rem:crystal-bases-path-a.
    #
    # NOT settled here: which law is right. That is a question about
    # prop:per-nucleon-shift-additive-linearity versus the crystal Path A
    # derivation, not something this probe can adjudicate. Recorded so the
    # next reader starts from the fit rather than from "off by one".
    fit = {"per_Z": 16, "per_N": 20, "const": 2}
    fitted = []
    for r in atoms_results:
        if r.get("u_pole_order_inferred") is None:
            continue
        pred = fit["per_Z"] * r["Z"] + fit["per_N"] * r["N"] + fit["const"]
        fitted.append({
            "atom": r["atom"], "Z": r["Z"], "N": r["N"],
            "measured": r.get("u_pole_order_inferred"),
            "asserted_law_18Z_21N_1": r.get("expected_shift"),
            "fitted_law_16Z_20N_2": pred,
            "fitted_law_matches": pred == r.get("u_pole_order_inferred"),
        })
    out.add_data("measured_law_fit", {
        "form": "16*Z + 20*N + 2",
        "matches": sum(1 for f in fitted if f["fitted_law_matches"]),
        "of": len(fitted),
        "gap_to_asserted_law": "2*Z + N - 1 (on every atom the fit matches)",
        "sole_exception": ("the A=1 neutron, anomalous under BOTH laws "
                           "(both predict 22, measured 18); already "
                           "asserted=False per rem:crystal-bases-path-a"),
        "not_settled": ("which law is correct — this probe cannot adjudicate "
                        "prop:per-nucleon-shift-additive-linearity against the "
                        "crystal Path A derivation"),
        "per_atom": fitted,
    })
    out.add_data("asserted_atoms", asserted_atoms)
    out.add_data("asserted_atoms_match", asserted_match)
    out.add_data("full_atoms_match_including_extrapolations", full_match)
    # Top-level assertion gates only on `asserted` atoms — the A=1
    # neutron extrapolation is reported but excluded so the witness
    # remains green for the verified A ≥ 2 closed-form scope.
    out.add_assertion(
        "asserted_atoms_match_closed_form_shift",
        # 0/1 INDICATOR, not a measurement — carried as a string so the
        # raw-float64 gate is satisfied without pretending to a precision
        # this has none of (bean qou-g94g). Same idiom as `scan_completed`
        # in audits/intra_ordering_value_fingerprint_audit.py.
        computed=str(int(asserted_match)),
        expected="1",
        source=("prop:per-nucleon-shift-additive-linearity (verified "
                "for A ≥ 2 in per-nucleon-shift-derivation.witness.json) "
                "+ crystal-bases Path A (this script)"),
    )

    p = out.save()
    print(f"\n  Witness: {p}", flush=True)
    return 0 if asserted_match else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
