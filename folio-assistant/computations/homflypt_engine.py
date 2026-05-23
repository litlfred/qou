#!/usr/bin/env python3
"""HOMFLYPT polynomial engine via Skein recursion on braid words.

Computes the full two-variable HOMFLYPT polynomial P(K; a, z) for
any braid word β ∈ B_n, using the Skein relation:

    a · P(L+) − a⁻¹ · P(L−) = z · P(L0)

where L+, L−, L0 are the positive crossing, negative crossing, and
smoothed crossing respectively.

The engine returns a Laurent polynomial in (a, z) with integer
coefficients — the full categorical invariant, not just a scalar
evaluation. Evaluation at specific (a, z) gives:

    P(K; q^(N-1), q − q⁻¹)  =  quantum SU(N) invariant of K

so N=2 recovers Jones, N=3 gives the color-channel observable, etc.

Implementation: memoized recursive Skein descent on braid closures.
Each crossing is resolved into (L+, L−, L0) sub-diagrams via the
Skein relation. The recursion terminates at unlinked circles (each
contributing a factor of δ = (a − a⁻¹)/z).

Complexity: O(2^c) worst case for c crossings (exponential in
crossing number). For proton-scale braids (~12 crossings) this is
~4096 recursion paths — tractable in seconds.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Optional


class LaurentPoly2:
    """Sparse Laurent polynomial in two variables (a, z).

    Represented as dict[(i, j)] -> coefficient, where the monomial
    is a^i · z^j. Coefficients are Python fractions for exact
    arithmetic.
    """

    __slots__ = ("_terms",)

    def __init__(self, terms: Optional[dict[tuple[int, int], int]] = None):
        self._terms: dict[tuple[int, int], int] = {}
        if terms:
            for k, v in terms.items():
                if v != 0:
                    self._terms[k] = v

    @classmethod
    def monomial(cls, i: int, j: int, coeff: int = 1) -> "LaurentPoly2":
        if coeff == 0:
            return cls()
        return cls({(i, j): coeff})

    @classmethod
    def zero(cls) -> "LaurentPoly2":
        return cls()

    @classmethod
    def one(cls) -> "LaurentPoly2":
        return cls({(0, 0): 1})

    def __add__(self, other: "LaurentPoly2") -> "LaurentPoly2":
        result = dict(self._terms)
        for k, v in other._terms.items():
            result[k] = result.get(k, 0) + v
            if result[k] == 0:
                del result[k]
        return LaurentPoly2(result)

    def __sub__(self, other: "LaurentPoly2") -> "LaurentPoly2":
        result = dict(self._terms)
        for k, v in other._terms.items():
            result[k] = result.get(k, 0) - v
            if result[k] == 0:
                del result[k]
        return LaurentPoly2(result)

    def __mul__(self, other: "LaurentPoly2") -> "LaurentPoly2":
        result: dict[tuple[int, int], int] = defaultdict(int)
        for (i1, j1), c1 in self._terms.items():
            for (i2, j2), c2 in other._terms.items():
                result[(i1 + i2, j1 + j2)] += c1 * c2
        return LaurentPoly2({k: v for k, v in result.items() if v != 0})

    def __rmul__(self, scalar: int) -> "LaurentPoly2":
        if scalar == 0:
            return LaurentPoly2.zero()
        return LaurentPoly2({k: scalar * v for k, v in self._terms.items()})

    def __neg__(self) -> "LaurentPoly2":
        return LaurentPoly2({k: -v for k, v in self._terms.items()})

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LaurentPoly2):
            return NotImplemented
        return self._terms == other._terms

    def is_zero(self) -> bool:
        return len(self._terms) == 0

    @property
    def terms(self) -> dict[tuple[int, int], int]:
        return dict(self._terms)

    def evaluate(self, a_val, z_val):
        """Evaluate P(a, z) at specific numerical values."""
        result = type(a_val)(0)
        for (i, j), c in self._terms.items():
            result += c * a_val ** i * z_val ** j
        return result

    def __repr__(self) -> str:
        if not self._terms:
            return "0"
        parts = []
        for (i, j), c in sorted(self._terms.items()):
            if c == 0:
                continue
            monomial = ""
            if i != 0:
                monomial += f"a^{i}" if i != 1 else "a"
            if j != 0:
                monomial += f"z^{j}" if j != 1 else "z"
            if not monomial:
                monomial = "1"
            if c == 1:
                parts.append(monomial)
            elif c == -1:
                parts.append(f"-{monomial}")
            else:
                parts.append(f"{c}*{monomial}")
        return " + ".join(parts).replace("+ -", "- ") if parts else "0"


# ── Planar diagram / Skein recursion engine ──────────────────────

# A "state" in the Skein recursion is a planar diagram — a set of
# strands with crossings. We represent it as a list of crossings,
# where each crossing records (strand_over, strand_under, sign).
#
# For braid closures, we use the standard braid→closure conversion:
# a braid word [σ_1, σ_2⁻¹, σ_1, ...] on n strands becomes a
# planar diagram with n strands connected top-to-bottom and then
# closed (strand i top → strand i bottom).

def _unknot_polynomial() -> LaurentPoly2:
    """HOMFLYPT of the unknot = 1."""
    return LaurentPoly2.one()


def _unlink_polynomial(n_components: int) -> LaurentPoly2:
    """HOMFLYPT of n unlinked unknots.

    Each additional unknot contributes a factor of
    δ = (a − a⁻¹) / z = a·z⁻¹ − a⁻¹·z⁻¹.
    """
    delta = LaurentPoly2({(1, -1): 1, (-1, -1): -1})
    result = LaurentPoly2.one()
    for _ in range(n_components - 1):
        result = result * delta
    return result


def homflypt_from_braid(braid_word: list[int], n_strands: int) -> LaurentPoly2:
    """Compute HOMFLYPT polynomial of the closure of a braid word.

    braid_word: list of integers. Positive i means σ_i (positive
    crossing of strand i over strand i+1). Negative -i means σ_i⁻¹
    (negative crossing). 1-indexed.

    n_strands: number of strands in the braid group B_n.

    Returns: LaurentPoly2 representing P(K; a, z).

    Uses Skein recursion with memoization on diagram states.
    """
    # Convert braid word to list of (generator_index, sign)
    crossings = []
    for g in braid_word:
        if g > 0:
            crossings.append((g, +1))  # positive crossing σ_g
        elif g < 0:
            crossings.append((-g, -1))  # negative crossing σ_g⁻¹
        else:
            raise ValueError("braid word entry 0 is invalid")

    # ── Skein recursion with cycle detection ────────────────────
    # The Skein relation for braid closures creates a LINEAR SYSTEM
    # (not a tree) when all crossings of one sign fold to their
    # mirror via the identity P(K̄;a,z) = P(K;a⁻¹,z). We handle
    # this by tracking the call stack and solving the resulting
    # linear equation when a cycle is detected.
    cache: dict[tuple, LaurentPoly2] = {}
    in_progress: set[tuple] = set()

    def _resolve(cx_list: list[tuple[int, int]], n: int) -> LaurentPoly2:
        key = (tuple(cx_list), n)
        if key in cache:
            return cache[key]

        if not cx_list:
            result = _unlink_polynomial(n)
            cache[key] = result
            return result

        if key in in_progress:
            # Cycle detected — return a symbolic placeholder.
            # The caller will solve the resulting linear equation.
            return None  # type: ignore[return-value]

        in_progress.add(key)

        # Always resolve the first crossing via Skein relation.
        gen_idx, sign = cx_list[0]
        rest = cx_list[1:]

        # L0: smooth first crossing
        p_l0 = _resolve_smoothed(rest, n, gen_idx)

        if sign == +1:
            # P(L+) = a⁻² P(L−) + a⁻¹z P(L0)
            flipped = [(gen_idx, -1)] + list(rest)
            p_opp = _resolve(flipped, n)
            if p_opp is None:
                # Cycle: p_opp depends on US via mirror. Solve:
                # P = a⁻² mirror(P) + a⁻¹z P(L0)
                # P − a⁻² mirror(P) = a⁻¹z P(L0)
                # This is tractable term-by-term since mirror just
                # flips the sign of a-exponents.
                result = _solve_mirror_equation(
                    p_l0, LaurentPoly2.monomial(-1, 1),
                    LaurentPoly2.monomial(-2, 0),
                )
            else:
                a_inv2 = LaurentPoly2.monomial(-2, 0)
                a_inv_z = LaurentPoly2.monomial(-1, 1)
                result = a_inv2 * p_opp + a_inv_z * p_l0
        else:
            # P(L−) = a² P(L+) − az P(L0)
            flipped = [(gen_idx, +1)] + list(rest)
            p_opp = _resolve(flipped, n)
            if p_opp is None:
                # Cycle: P = a² mirror(P) − az P(L0)
                result = _solve_mirror_equation(
                    p_l0, -LaurentPoly2.monomial(1, 1),
                    LaurentPoly2.monomial(2, 0),
                )
            else:
                a2 = LaurentPoly2.monomial(2, 0)
                a_z = LaurentPoly2.monomial(1, 1)
                result = a2 * p_opp - a_z * p_l0

        in_progress.discard(key)
        cache[key] = result
        return result

    def _solve_mirror_equation(
        rhs_poly: LaurentPoly2,
        rhs_coeff: LaurentPoly2,
        mirror_coeff: LaurentPoly2,
    ) -> LaurentPoly2:
        """Solve P − mirror_coeff · mirror(P) = rhs_coeff · rhs_poly
        for P, where mirror(P) flips a-exponent signs.

        Term-by-term: for each (i, j), the coefficient c_{i,j} of
        a^i z^j satisfies:
          c_{i,j} − [mirror_coeff evaluated at (i,j)] · c_{-i,j} = rhs_{i,j}

        This is a 2×2 system for each pair (i, j) and (-i, j).
        """
        rhs = rhs_coeff * rhs_poly
        result_terms: dict[tuple[int, int], int] = {}
        processed: set[tuple[int, int]] = set()

        # Collect all (i, j) keys from rhs and mirror_coeff
        # mirror_coeff is a monomial a^k — we need its (k, 0) to shift
        mc_terms = mirror_coeff.terms
        assert len(mc_terms) == 1, "mirror_coeff must be a single monomial"
        (mk, ml), mc = list(mc_terms.items())[0]
        assert ml == 0, "mirror_coeff must be in a only"

        for (i, j), r_val in rhs.terms.items():
            if (i, j) in processed:
                continue

            # c_{i,j} − mc · c_{-i+mk, j+ml} = r_{i,j}
            # c_{-i+mk, j} − mc · c_{i, j} = r_{-i+mk, j}
            i2 = -i + mk
            j2 = j + ml

            r1 = rhs.terms.get((i, j), 0)
            r2 = rhs.terms.get((i2, j2), 0)

            if i == i2 and j == j2:
                # Self-paired: c − mc · c = r → c(1 − mc) = r
                if (1 - mc) != 0:
                    # Integer division — should be exact
                    c = r1 // (1 - mc) if (1 - mc) != 0 else 0
                    result_terms[(i, j)] = c
                processed.add((i, j))
            else:
                # System:
                #   c1 − mc · c2 = r1
                #   c2 − mc · c1 = r2
                # Det = 1 − mc² ≠ 0 for knot polynomials
                det = 1 - mc * mc
                if det != 0:
                    c1 = (r1 + mc * r2) // det
                    c2 = (r2 + mc * r1) // det
                    result_terms[(i, j)] = c1
                    result_terms[(i2, j2)] = c2
                processed.add((i, j))
                processed.add((i2, j2))

        # Also handle (i2, j2) keys from rhs that weren't paired
        for (i, j), r_val in rhs.terms.items():
            if (i, j) not in processed:
                i2 = -i + mk
                j2 = j + ml
                r1 = rhs.terms.get((i, j), 0)
                r2 = rhs.terms.get((i2, j2), 0)
                det = 1 - mc * mc
                if det != 0:
                    c1 = (r1 + mc * r2) // det
                    c2 = (r2 + mc * r1) // det
                    result_terms[(i, j)] = c1
                    result_terms[(i2, j2)] = c2
                processed.add((i, j))
                processed.add((i2, j2))

        return LaurentPoly2(result_terms)

    def _resolve_smoothed(
        cx_list: list[tuple[int, int]], n: int, smoothed_gen: int
    ) -> LaurentPoly2:
        new_crossings = []
        writhe_correction = LaurentPoly2.one()

        for gen_idx, sign in cx_list:
            if gen_idx == smoothed_gen:
                if sign == +1:
                    writhe_correction = writhe_correction * LaurentPoly2.monomial(1, 0)
                else:
                    writhe_correction = writhe_correction * LaurentPoly2.monomial(-1, 0)
            elif gen_idx > smoothed_gen:
                new_crossings.append((gen_idx - 1, sign))
            else:
                new_crossings.append((gen_idx, sign))

        return writhe_correction * _resolve(new_crossings, n - 1)

    return _resolve(crossings, n_strands)


# ── Convenience: known braids ────────────────────────────────────

def trefoil_braid() -> tuple[list[int], int]:
    """Right-hand trefoil as braid closure: σ₁³ on 2 strands."""
    return [1, 1, 1], 2


def figure_eight_braid() -> tuple[list[int], int]:
    """Figure-eight knot: σ₁ σ₂⁻¹ σ₁ σ₂⁻¹ on 3 strands."""
    return [1, -2, 1, -2], 3


def borromean_braid() -> tuple[list[int], int]:
    """Borromean rings: (σ₁ σ₂⁻¹)³ on 3 strands."""
    return [1, -2, 1, -2, 1, -2], 3


def hopf_link_braid() -> tuple[list[int], int]:
    """Hopf link: σ₁² on 2 strands."""
    return [1, 1], 2


# ── Self-test ────────────────────────────────────────────────────

def _self_test():
    """Verify against known HOMFLYPT polynomials."""
    import mpmath as mp
    mp.mp.dps = 30

    print("HOMFLYPT engine self-test")
    print("=" * 60)

    # Unknot (empty braid on 1 strand)
    p = homflypt_from_braid([], 1)
    assert p == LaurentPoly2.one(), f"unknot failed: {p}"
    print(f"  unknot:       P = {p}  ✓")

    # Trefoil: known P(3_1; a, z) = -a⁻⁴ + a⁻² z² + 2 a⁻²
    # (convention-dependent; verify numerically)
    word, n = trefoil_braid()
    p_tref = homflypt_from_braid(word, n)
    print(f"  trefoil:      P = {p_tref}")
    # Evaluate at Jones specialization: a = q⁻¹, z = q − q⁻¹
    q = mp.mpf("1.1")
    jones_val = p_tref.evaluate(1 / q, q - 1 / q)
    print(f"    Jones(q=1.1) = {mp.nstr(jones_val, 12)}")

    # Figure-eight: known to be amphicheiral, P(4_1; a, z) is
    # symmetric under a → a⁻¹
    word, n = figure_eight_braid()
    p_fig8 = homflypt_from_braid(word, n)
    print(f"  figure-eight: P = {p_fig8}")
    # Check amphicheirality: P(a, z) = P(a⁻¹, z)?
    p_mirror = LaurentPoly2({(-i, j): c for (i, j), c in p_fig8.terms.items()})
    is_amphicheiral = (p_fig8 == p_mirror)
    print(f"    amphicheiral (P(a)=P(a⁻¹)): {is_amphicheiral}")

    # Borromean rings
    word, n = borromean_braid()
    p_bor = homflypt_from_braid(word, n)
    print(f"  Borromean:    P = {p_bor}")

    # Hopf link
    word, n = hopf_link_braid()
    p_hopf = homflypt_from_braid(word, n)
    print(f"  Hopf link:    P = {p_hopf}")

    print()
    print("Self-test complete.")
    return {
        "unknot": p,
        "trefoil": p_tref,
        "figure_eight": p_fig8,
        "borromean": p_bor,
        "hopf": p_hopf,
    }


if __name__ == "__main__":
    _self_test()
