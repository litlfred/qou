"""Hyperbolic knot → braid word database for the QOU framework.

Provides canonical braid representatives for every knot/link used in
the framework's mass formula, atom→knot assignments, and torus-knot
work.

## Knots / links catalogued

| Name | Braid word (B_n) | n | Volume | Use |
|------|------------------|---|--------|-----|
| 4_1 (figure-eight) | σ₁ σ₂⁻¹ σ₁ σ₂⁻¹ | 3 | 2.0299 | µ knot (m_μ/m_e calibration) |
| 5_2 | σ₁⁻¹ σ₂ σ₁⁻¹ σ₂² | 3 | 2.8281 | (literature ref) |
| 6_2 | σ₁⁻¹ σ₂ σ₁⁻¹ σ₂² σ₁⁻¹ σ₂ | 3 | 4.4015 | 2H (deuteron, EXPLORATORY) |
| 7²_1 (Whitehead-like 2-link) | σ₁⁻¹ σ₂ σ₁⁻¹ σ₂² σ₁⁻¹ σ₂² | 3 | 4.7495 | c_αα factor (α-cluster coupling) |
| 8_11 | σ₁² σ₂⁻¹ σ₁ σ₂⁻¹ σ₁ σ₂⁻² | 3 | 6.5511 | 3H (tritium, EXPLORATORY) |
| L6a4 (Borromean rings) | (σ₁ σ₂⁻¹)³ | 3 | 7.3277 (= 8G) | Proton, 4·𝓑₃ tower for ⁴He |

## Torus knots / links T(p, k)

For torus knots T(p, k) on p strands (p-1 generators):
  β_{T(p,k)} = (σ_1 σ_2 ... σ_{p-1})^k

Examples:
- T(2,3) trefoil: σ₁³ in B_2
- T(2,4) Hopf-derived: σ₁⁴ in B_2 (= W± in lepton tower)
- T(2,6): σ₁⁶ (= Z)
- T(2,8): σ₁⁸ (= Higgs)
- T(3,2) = T(2,3) trefoil
- T(3,4): (σ₁ σ₂)^4 in B_3

## Format

Each braid word is a list of (sign, gen_1based) tuples per
pyhecke_native.chi_lambda_braid convention:
  sign ∈ {+1, -1, 0}: positive crossing / negative crossing / averaged
  gen_1based ∈ {1, 2, ..., n-1}: 1-indexed braid generator σ_i

## References

- SnapPy census + KnotInfo database for hyperbolic-knot braid words
- Sibling commit 5418678c8 — T(2,k) torus link family for W±/Z/Higgs
- Borromean braid per `pm_qm_pythagorean_identity.py`: (σ₁ σ₂⁻¹)³
"""
from __future__ import annotations


def borromean_on_strand_triple(base_strand: int) -> list[tuple[int, int]]:
    """(σ_a σ_{a+1}⁻¹)³ where a = base_strand (1-based).

    Used for atom braids: A disjoint Borromean copies on
    strands {3k+1, 3k+2, 3k+3} for k = 0, 1, ..., A-1.
    """
    s1, s2 = base_strand, base_strand + 1
    word = []
    for _ in range(3):
        word.append((1, s1))
        word.append((-1, s2))
    return word


def torus_knot_braid(p: int, k: int) -> list[tuple[int, int]]:
    """Braid word for torus knot/link T(p, k) on p strands.

    β = (σ_1 σ_2 ... σ_{p-1})^k

    Returns list of (sign=+1, gen_1based) tuples, length k(p-1).

    Raises ValueError on p < 2 (no generators in B_1) or k < 0
    (the inverse braid is not implemented; use the inverse manually).
    k == 0 returns the empty braid (identity in B_p, = unknot/unlink).
    """
    if p < 2:
        raise ValueError(f"torus_knot_braid: need p >= 2, got p={p}")
    if k < 0:
        raise ValueError(
            f"torus_knot_braid: k >= 0 required, got k={k}. "
            "Negative k is the inverse braid; build it manually by "
            "negating crossings and repeating |k| times."
        )
    base = [(1, i + 1) for i in range(p - 1)]
    return base * k


def _parse_torus_name(knot_name: str) -> tuple[int, int] | None:
    """Parse 'T(p,k)' → (p, k); return None if not torus-shaped.

    Raises ValueError on torus-shaped but malformed (non-int components,
    wrong arity).
    """
    if not (knot_name.startswith("T(") and knot_name.endswith(")")):
        return None
    inner = knot_name[2:-1]
    parts = inner.split(",")
    if len(parts) != 2:
        raise ValueError(
            f"Malformed torus-knot name {knot_name!r}: expected 'T(p,k)' "
            f"with exactly 2 comma-separated integers, got {len(parts)}."
        )
    try:
        p = int(parts[0].strip())
        k = int(parts[1].strip())
    except ValueError as e:
        raise ValueError(
            f"Malformed torus-knot name {knot_name!r}: components "
            f"must be integers ({e})."
        ) from e
    return p, k


# Hyperbolic knot / link braid words (B_3, all 3-strand)
HYPERBOLIC_BRAIDS: dict[str, list[tuple[int, int]]] = {
    # Figure-eight knot — the muon's hyperbolic knot
    "4_1": [(1, 1), (-1, 2), (1, 1), (-1, 2)],
    # 5_2 knot
    "5_2": [(-1, 1), (1, 2), (-1, 1), (1, 2), (1, 2)],
    # 6_2 — deuteron (EXPLORATORY)
    "6_2": [(-1, 1), (1, 2), (-1, 1), (1, 2), (1, 2), (-1, 1), (1, 2)],
    # 7²_1 (Whitehead-like 2-link) — c_αα factor
    "7^2_1": [(-1, 1), (1, 2), (-1, 1), (1, 2), (1, 2), (-1, 1), (1, 2), (1, 2)],
    # 8_11 — tritium (EXPLORATORY)
    "8_11": [(1, 1), (1, 1), (-1, 2), (1, 1), (-1, 2), (1, 1), (-1, 2), (-1, 2)],
    # Borromean rings L6a4 — proton / atom tower base
    "Borromean": [(1, 1), (-1, 2), (1, 1), (-1, 2), (1, 1), (-1, 2)],
    "L6a4": [(1, 1), (-1, 2), (1, 1), (-1, 2), (1, 1), (-1, 2)],  # alias
}

# Number of strands per knot/link
HYPERBOLIC_NSTRANDS: dict[str, int] = {
    "4_1": 3,
    "5_2": 3,
    "6_2": 3,
    "7^2_1": 3,
    "8_11": 3,
    "Borromean": 3,
    "L6a4": 3,
}


def braid_word_for_knot(knot_name: str) -> list[tuple[int, int]]:
    """Get the canonical braid word for a named knot/link.

    Supports:
    - Hyperbolic: '4_1', '5_2', '6_2', '7^2_1', '8_11', 'Borromean', 'L6a4'
    - Torus: 'T(p,k)' string, e.g., 'T(2,3)' for trefoil

    Raises KeyError if knot_name is not recognised; ValueError if
    knot_name parses as torus but with invalid components.
    """
    if knot_name in HYPERBOLIC_BRAIDS:
        return HYPERBOLIC_BRAIDS[knot_name]
    torus = _parse_torus_name(knot_name)
    if torus is not None:
        p, k = torus
        return torus_knot_braid(p, k)
    raise KeyError(
        f"Unknown knot: {knot_name!r}. Supported: "
        f"{list(HYPERBOLIC_BRAIDS.keys())} + T(p,k) torus knots."
    )


def n_strands_for_knot(knot_name: str) -> int:
    """Number of strands in the canonical braid representative.

    Raises KeyError if knot_name is not recognised; ValueError if
    knot_name parses as torus but with invalid components.
    """
    if knot_name in HYPERBOLIC_NSTRANDS:
        return HYPERBOLIC_NSTRANDS[knot_name]
    torus = _parse_torus_name(knot_name)
    if torus is not None:
        p, _k = torus
        if p < 2:
            raise ValueError(
                f"n_strands_for_knot: torus knot needs p >= 2, got "
                f"p={p} from {knot_name!r}"
            )
        return p
    raise KeyError(
        f"Unknown knot: {knot_name!r}. Supported: "
        f"{list(HYPERBOLIC_NSTRANDS.keys())} + T(p,k) torus knots."
    )


def list_known_knots() -> list[str]:
    """All knot names this database recognises (excluding parametric T(p,k))."""
    return sorted(HYPERBOLIC_BRAIDS.keys())
