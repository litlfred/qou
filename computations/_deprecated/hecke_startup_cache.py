#!/usr/bin/env python3
"""
Startup cache for hecke_core expensive computations.

Precomputes and serializes the Gram matrix, Wedderburn-Artin weights,
fine structure constant, BW coefficients, and nucleon NFs so that
downstream scripts can skip the ~50ms hecke_core import-time computation.

The cache is a JSON file keyed by a hash of (q_parameter.py content +
hecke_core.py content). If either file changes, the cache is regenerated.

Usage:
    # Generate / refresh cache
    python3 hecke_startup_cache.py

    # In downstream scripts: import cached values instead of hecke_core
    from hecke_startup_cache import load_cache
    cache = load_cache()
    alpha_em = cache["alpha_em"]
    G = cache["gram_matrix"]  # as list-of-lists; np.array(G) if needed

Architecture:
    q_parameter.py ──┐
                     ├─→ hecke_startup_cache.json (serialized constants)
    hecke_core.py ───┘         │
                               ├─→ downstream script A (reads cache)
                               ├─→ downstream script B (reads cache)
                               └─→ ...

This eliminates redundant hecke_core initialization across 211 scripts.

@module computations/hecke_startup_cache
"""

import hashlib
import json
import sys
import time
from pathlib import Path

COMP_DIR = Path(__file__).resolve().parent
CACHE_FILE = COMP_DIR / "hecke_startup_cache.json"

# Files whose content determines cache validity
SOURCE_FILES = [
    COMP_DIR / "q_parameter.py",
    COMP_DIR / "experimental_constants.py",
    COMP_DIR / "hecke_core.py",
]


def _sources_hash() -> str:
    """SHA-256 of concatenated source file contents."""
    h = hashlib.sha256()
    for f in SOURCE_FILES:
        h.update(f.read_text(encoding="utf-8").encode())
    return h.hexdigest()[:16]


def _is_cache_valid() -> bool:
    """Check if cache exists and matches current source files."""
    if not CACHE_FILE.exists():
        return False
    try:
        cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        return cache.get("sources_hash") == _sources_hash()
    except (json.JSONDecodeError, KeyError):
        return False


def generate_cache() -> dict:
    """Import hecke_core and serialize all expensive computed values."""
    t0 = time.monotonic()

    # Force fresh import
    sys.path.insert(0, str(COMP_DIR))

    from q_parameter import (
        Q, Q_INV, Q_ERR, HBAR_Q, HBAR_Q_SQ,
        VOL_FIGURE_EIGHT, MASS_RATIO_MU_E,
        HA, E_CROSS, S_SKEIN, TWO_Q, TANH_LN_Q, LN_Q,
        Q_RAT_NUM, Q_RAT_DEN,
    )
    from experimental_constants import (
        M_E_MEV, M_P_MEV, M_N_MEV, M_N_MINUS_P_MEV,
        ALPHA_EM_INV, G_F_MEV, HBAR_MEV_S,
    )
    from hecke_core import (
        # Fine structure
        alpha_em, ALPHA_EM_INV_DERIVED,
        # Figure-eight
        FIG8_A_BULK, FIG8_F_COUL, FIG8_F_EXCH,
        # Molecular
        E_HARTREE_EV, E_MOL, KAPPA,
        # NF
        PROTON_NF, NEUTRON_NF,
        # Volumes
        VOL_BORROMEAN, ALPHA_BORROMEAN, ALPHA_FIGURE8,
    )
    # Moved to pyhecke.gram via M2b inversion — import canonically.
    from pyhecke.gram import (
        # Wedderburn-Artin
        W_SYM, W_STD, W_ALT, z,
        # Gram matrix
        G, G_INV,
        # NF basis
        NF_BASIS, NF_NAMES, TR_M,
    )

    duration_ms = int((time.monotonic() - t0) * 1000)

    cache = {
        "sources_hash": _sources_hash(),
        "computedAt": __import__("datetime").datetime.now(
            __import__("datetime").timezone.utc
        ).isoformat(),
        "generation_ms": duration_ms,

        # ── q_parameter ──────────────────────────────────────
        "q": Q,
        "q_inv": Q_INV,
        "q_err": Q_ERR,
        "hbar_q": HBAR_Q,
        "hbar_q_sq": HBAR_Q_SQ,
        "ha": HA,
        "e_cross": E_CROSS,
        "s_skein": S_SKEIN,
        "two_q": TWO_Q,
        "tanh_ln_q": TANH_LN_Q,
        "ln_q": LN_Q,
        "q_rat_num": Q_RAT_NUM,
        "q_rat_den": Q_RAT_DEN,
        "vol_figure_eight": VOL_FIGURE_EIGHT,
        "mass_ratio_mu_e": MASS_RATIO_MU_E,

        # ── experimental_constants ───────────────────────────
        "m_e_mev": M_E_MEV,
        "m_p_mev": M_P_MEV,
        "m_n_mev": M_N_MEV,
        "m_n_minus_p_mev": M_N_MINUS_P_MEV,
        "alpha_em_inv_codata": ALPHA_EM_INV,
        "g_f_mev": G_F_MEV,
        "hbar_mev_s": HBAR_MEV_S,

        # ── Wedderburn-Artin weights ─────────────────────────
        "w_sym": W_SYM,
        "w_std": W_STD,
        "w_alt": W_ALT,
        "z_markov": z,

        # ── Fine structure (derived) ─────────────────────────
        "alpha_em": alpha_em,
        "alpha_em_inv_derived": ALPHA_EM_INV_DERIVED,

        # ── Gram matrix (6x6) ───────────────────────────────
        "gram_matrix": G.tolist(),
        "gram_matrix_inv": G_INV.tolist(),

        # ── Figure-eight BW modification ─────────────────────
        "fig8_a_bulk": FIG8_A_BULK,
        "fig8_f_coul": FIG8_F_COUL,
        "fig8_f_exch": FIG8_F_EXCH,

        # ── Molecular energy scales ──────────────────────────
        "e_hartree_ev": E_HARTREE_EV,
        "e_mol": E_MOL,
        "kappa": KAPPA,

        # ── Knot volumes ─────────────────────────────────────
        "vol_borromean": VOL_BORROMEAN,
        "alpha_borromean": ALPHA_BORROMEAN,
        "alpha_figure8": ALPHA_FIGURE8,

        # ── NF infrastructure ────────────────────────────────
        "nf_basis": [list(b) for b in NF_BASIS],
        "nf_names": NF_NAMES,
        "tr_m": TR_M.tolist(),
        "proton_nf": PROTON_NF,
        "neutron_nf": NEUTRON_NF,
    }

    return cache


def save_cache(cache: dict) -> Path:
    """Write cache to disk."""
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return CACHE_FILE


def load_cache() -> dict:
    """Load cache, regenerating if stale or missing.

    Returns a dict with all precomputed constants. Downstream scripts
    can use this instead of importing hecke_core directly:

        from hecke_startup_cache import load_cache
        C = load_cache()
        alpha_em = C["alpha_em"]
    """
    if _is_cache_valid():
        return json.loads(CACHE_FILE.read_text(encoding="utf-8"))

    # Cache miss: regenerate
    cache = generate_cache()
    save_cache(cache)
    return cache


# ── CLI ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate or check hecke_core startup cache"
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Check if cache is valid (exit 0=valid, 1=stale)"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Force regeneration even if cache is valid"
    )
    args = parser.parse_args()

    if args.check:
        valid = _is_cache_valid()
        if valid:
            print(f"✓ Cache valid: {CACHE_FILE.name}")
        else:
            print(f"✗ Cache stale or missing: {CACHE_FILE.name}")
        sys.exit(0 if valid else 1)

    if args.force or not _is_cache_valid():
        print("Generating hecke_core startup cache...")
        cache = generate_cache()
        save_cache(cache)
        print(f"✓ {CACHE_FILE.name}: {len(cache)} keys, "
              f"generated in {cache['generation_ms']}ms")
        print(f"  sources_hash: {cache['sources_hash']}")
        print(f"  alpha_em = {cache['alpha_em']:.10f}")
        print(f"  1/alpha  = {cache['alpha_em_inv_derived']:.6f}")
        print(f"  Gram det = {__import__('numpy').linalg.det(__import__('numpy').array(cache['gram_matrix'])):.6f}")
    else:
        print(f"✓ Cache already valid: {CACHE_FILE.name}")
