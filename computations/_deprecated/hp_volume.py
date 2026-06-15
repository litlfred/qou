"""Shared high-precision hyperbolic-volume extraction.

Multiple scripts (atom_link_derivation, jsj_alpha_clustering,
jsj_verification, d_knot_extended_search, atom_knot_search) have
near-identical helper functions for extracting Vol(M) at high
precision via SnapPy's .high_precision() + mpmath.workdps.  This
module centralises the common pattern.

Usage:
    from hp_volume import hp_volume_of_manifold
    hp_str = hp_volume_of_manifold(M, digits=50)

Callers that construct the manifold differently (e.g.
snappy.Link(braid_closure=...) → .exterior()) continue to do so;
this helper only handles the volume extraction step.
"""
from __future__ import annotations

from typing import Optional


def hp_volume_of_manifold(M, digits: int = 50) -> Optional[str]:
    """Return the high-precision volume of a SnapPy manifold as a
    mpmath-formatted string, or None if mpmath or SnapPy's HP mode
    is unavailable.

    The precision change is scoped via mpmath.workdps so it does NOT
    leak into other callers in the same process.
    """
    try:
        Mh = M.high_precision()
    except (AttributeError, RuntimeError):
        return None
    try:
        import mpmath
    except ImportError:
        # Fall back to plain float conversion
        try:
            v = Mh.volume()
            rp = v.real if hasattr(v, "real") else v
            return str(rp)
        except (AttributeError, RuntimeError):
            return None
    try:
        with mpmath.workdps(digits):
            v = Mh.volume()
            rp = v.real if hasattr(v, "real") else v
            return mpmath.nstr(mpmath.mpf(str(rp)), digits)
    except (AttributeError, RuntimeError, ValueError):
        return None


def hp_volume_of_link_closure(braid_word: list[int], digits: int = 50):
    """Close a braid word and return (v_float, hp_str).

    Returns (None, None) if SnapPy is unavailable or the closure fails.
    """
    try:
        import snappy
    except ImportError:
        return None, None
    try:
        L = snappy.Link(braid_closure=braid_word)
        E = L.exterior()
        v_raw = E.volume()
        v_float = float(v_raw.real) if hasattr(v_raw, "real") else float(v_raw)
    except (AttributeError, RuntimeError, ValueError, IndexError) as e:
        return None, None
    hp = hp_volume_of_manifold(E, digits=digits) if v_float > 0.5 else None
    return v_float, hp
