"""Atomic braid NF + per-generator volume primitives.

**M2 inversion (2b Phase B, stacked on #1118 + #1121)**: this module
owns the canonical implementations of the atom-builder cluster
(11 functions + 6 module-level constants), which previously lived in
`hecke_core.py`.

Symbols owned by this module:
  _ID_NF, _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
  PROTON_NF, NEUTRON_NF,
  build_atom_nf_exact, nf_channel_exact, check_frobenius,
  build_atom_nf, vertex_volume, nucleon_gen_chains, atom_gen_chains,
  atom_V_full, _chain_V_full, atom_per_generator_volumes,
  build_nucleon_nf.

This is the heart of the canonical mass-pipeline surface. After this
PR lands, pyhecke owns the full Wedderburn + atom-builder + molecular
canonical surface — only the α-EM / E_MOL / FIG8 constants block
remains in hecke_core (a separate M2 PR will move that into
pyhecke.constants).

`E_MOL`, `alpha_em`, `FIG8_*`, `ALPHA_*`, `V_HAT_ELECTRON` constants
are still owned by hecke_core; the relevant functions here import
them lazily inside function bodies to avoid the circular-import
hazard (see molecular.py for the pattern).
"""

from __future__ import annotations

import math
from fractions import Fraction
import numpy as np
import mpmath as _mp

# Substrate constants + Gram / NF primitives — pyhecke owns these
# (M2b inversion landed earlier; pyhecke.gram is the canonical source).
from pyhecke.gram import (  # type: ignore[import-not-found]
    h, q0, qi, z,
    W_SYM, W_STD, W_ALT,
    NF_BASIS, NF_NAMES,
    hm, hm_exact, nf_tr, nf_net,
    h_mp, hm_mp,
    G,
    # `_TR_M_FRAC` was missing here until 2026-08-31 (bean `t7qv`), which made
    # `nf_channel_exact` raise `NameError` on EVERY call — it is used in the
    # body but was never imported. `gram` defines it and lists it in `__all__`;
    # only this import line was short. Found while building the Phase B LR
    # branching constraint, which needs exactly this channel decomposition.
    _H_FRAC, _Z_FRAC, _SYM_EIG_FRAC, _ALT_EIG_FRAC, _TR_M_FRAC,
    _Q_FRAC, _QI_FRAC,
)
# Wedderburn primitives — pyhecke owns these (PR #1118).
from pyhecke.wedderburn import (  # type: ignore[import-not-found]
    partitions_of, q_dimension, wedderburn_weight, q_factorial,
)

# Canonical p-n interface offset. `D_PN` is the `d` of the (c, d) crossing
# pair for a MIXED (proton-neutron) bond, bound once at the module q0 exactly
# as `h` above is.
#
# It was open-coded as `-h/2` at the three nucleon p-n branches below, which
# is `strict_averaged` -- the COLOUR-BLIND convention. The owner ruling of
# 2026-08-15 (R3), reaffirmed 2026-08-26, makes `bring_color_weighted`
# canonical, and this module is the single largest consumer of the choice:
# 1027 of the 1929 witness-writing producers in `computations/` reach it
# through this file.
#
# NOT the quark u-d mixed crossings further down (`ud -> sigma_0 mixed`).
# Those are a different bond and keep `-h/2`; nothing here establishes what
# convention a u-d crossing should carry.
from pyhecke.constants import (  # type: ignore[import-not-found]
    PN_CONVENTION, pn_interface_offset,
)

D_PN = pn_interface_offset(q0)

# Legacy bridge — keeps the sys.path bootstrap alive in case anything
# we lazy-import below requires it.
from . import _legacy  # noqa: F401

# Constants still owned by hecke_core (`alpha_em`, `E_MOL`,
# `E_HARTREE_EV`, `TWO_Q`, `KAPPA`, `M_E_MEV`, `FIG8_*`, `ALPHA_*`,
# `V_HAT_ELECTRON`) are imported LAZILY inside the functions that
# need them — module-top import would trigger hecke_core load which
# would circle back into this module's still-being-defined namespace
# via the back-compat re-export block.





# NF basis, trace weights, bond operators, hm, hm_exact, nf_tr, nf_net,
# _hm_dict, _reduce_nf, _build_gram, G, G_INV, and the exact-rational
# (_*_FRAC) constants have been moved to pyhecke.gram (M2b inversion).
# They are re-imported at the top of this file so every existing name
# remains accessible at module scope for downstream callers.

# Identity NF: the trivial braid [1, 0, 0, 0, 0, 0]
_ID_NF = np.array([1.0, 0, 0, 0, 0, 0])



def build_atom_nf_exact(Z, N):
    """Build atom NF using EXACT Fraction arithmetic.

    IDENTICAL algorithm to build_atom_nf but with Fraction arithmetic.
    Crossing order: per-nucleon (B₃ interleaved + quarks + inter-nucleon
    with all previous), then electrons. Matches build_atom_nf exactly.

    Reference: prop:atomic-braid-mass
    """
    A = Z + N
    if A == 0:
        return [Fraction(1), Fraction(0), Fraction(0),
                Fraction(0), Fraction(0), Fraction(0)]

    F0 = Fraction(0)
    F1 = Fraction(1)
    Fh = _H_FRAC
    Fh2 = Fh / 2

    # Ground-state ordering (same as build_atom_nf)
    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p'); pc += 1
        else:
            ordering.append('n'); nc += 1

    nf = [Fraction(0)] * 6
    nf[0] = Fraction(1)

    for k in range(A):
        if ordering[k] == 'p':
            for _ in range(3):
                nf = hm_exact(nf, F1, F0, 0)
                nf = hm_exact(nf, F1, -Fh, 1)
            # Quark: (0,1)=uu→σ₀, (0,2)=ud→mixed, (1,2)=ud→mixed
            nf = hm_exact(nf, F1, F0, 0)      # uu
            nf = hm_exact(nf, F1, -Fh2, 0)    # ud mixed
            nf = hm_exact(nf, F1, -Fh2, 1)    # ud mixed
            # Gluon: 2 σ₀
            nf = hm_exact(nf, F1, F0, 0)
            nf = hm_exact(nf, F1, F0, 0)
        else:
            for _ in range(3):
                nf = hm_exact(nf, F1, F0, 0)
                nf = hm_exact(nf, F1, -Fh, 1)
            # Quark: (0,1)=ud→mixed, (0,2)=ud→mixed, (1,2)=dd→σ⁻¹
            nf = hm_exact(nf, F1, -Fh2, 0)
            nf = hm_exact(nf, F1, -Fh2, 0)
            nf = hm_exact(nf, F1, -Fh, 1)
            # Gluon: 2 σ₀
            nf = hm_exact(nf, F1, F0, 0)
            nf = hm_exact(nf, F1, F0, 0)

        # Inter-nucleon with all PREVIOUS nucleons (on gen 0)
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == 'p' and tj == 'p':
                nf = hm_exact(nf, F1, F0, 0)
            elif ti == 'n' and tj == 'n':
                nf = hm_exact(nf, F1, -Fh, 0)
            else:
                nf = hm_exact(nf, F1, -Fh2, 0)

    # Electrons on gen 1
    for _ in range(Z):
        nf = hm_exact(nf, F1, -Fh, 1)

    return nf



def nf_channel_exact(nf_frac):
    """Exact per-channel characters from Fraction NF.

    Returns (χ_sym, χ_std, χ_alt, tr_M) as Fractions.
    """
    chi_sym = sum(c * e for c, e in zip(nf_frac, _SYM_EIG_FRAC))
    chi_alt = sum(c * e for c, e in zip(nf_frac, _ALT_EIG_FRAC))
    tr_M = sum(c * e for c, e in zip(nf_frac, _TR_M_FRAC))

    # Wedderburn weights (exact)
    q2 = _Q_FRAC ** 2
    D = q2**2 + 4*q2 + 1
    w_sym = q2 / D
    w_std = (q2 + 1)**2 / D
    w_alt = q2 / D

    chi_std = (tr_M - w_sym * chi_sym - w_alt * chi_alt) / w_std
    return chi_sym, chi_std, chi_alt, tr_M



    # ⚠ MEASURED WRONG 2026-08-31 (bean `t7qv`) — do not consume `chi_std`.
    # Against direct seminormal traces at `H_3`, this `chi_std` matches the
    # standard-block character under NO normalisation:
    #
    #     element          chi_std here   direct trace   trace/dim
    #     identity            1.000000       2.000000     1.000000
    #     sigma_0             0.864044       0.209060     0.104530
    #     sigma_0 sigma_1     0.055685      -1.000000    -0.500000
    #
    # and `chi_sym` / `chi_alt` are evaluated at `q = 111/100` (`-1/1.11 =
    # -0.9009009` against `-1/q_0 = -0.9009183`), not at `q_0`. The function
    # raised `NameError` on every call until the `_TR_M_FRAC` import above was
    # fixed in the same change, which is why this was never noticed: it was
    # dead code, so nothing ever compared it to anything.
    #
    # NOT repaired here — the right `chi_std` depends on which Wedderburn
    # weighting convention `W_STD` is meant to pair with, and that is a
    # substrate decision, not a local one. Callers needing block characters
    # should take direct seminormal traces; see
    # `computations/probes/phase_b_lr_branching_constraint_probe.py`.


def check_frobenius(nf):
    """Check Frobenius positivity G·x ≥ 0. Returns (stable, Gx, violations)."""
    x = np.array(nf)
    Gx = G @ x
    violations = [(NF_NAMES[i], Gx[i]) for i in range(6) if Gx[i] < -1e-10]
    return len(violations) == 0, Gx, violations



# ══════════════════════════════════════════════════════════════
# Atom construction
# ══════════════════════════════════════════════════════════════

def build_atom_nf(Z, N):
    """Build atom NF via Hecke multiplication.

    Construction:
      1. Build each nucleon via build_nucleon_nf (B₃ + quark crossings)
      2. Compose nucleons in ground-state interleaved order
      3. Apply inter-nucleon crossings between each pair (i,j):
           pp: σ₀           (c=1, d=0)    — EM repulsion
           nn: σ₀⁻¹         (c=1, d=-h)   — nuclear attraction
           pn: colour-weighted (c=1, d=D_PN) — mixed nuclear
                            (d = -h/2 only under `strict_averaged`)
      4. Apply pe crossings for electrons (σ₁⁻¹ per electron)

    No separate gluon dressing — B₃ IS the gluon structure.
    Generator 0 for inter-nucleon crossings (strong force channel).
    Generator 1 for pe crossings (EM channel).
    """
    A = Z + N
    if A == 0:
        return [1.0, 0, 0, 0, 0, 0]

    # Build ground-state ordering: interleaved protons and neutrons
    ordering = []  # 'p' or 'n'
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p')
            pc += 1
        else:
            ordering.append('n')
            nc += 1

    # Start with identity
    nf = [1.0, 0, 0, 0, 0, 0]

    # Compose nucleon NFs sequentially
    for k in range(A):
        if ordering[k] == 'p':
            # B₃ confinement (3 interleaved σ₀, σ₁⁻¹)
            for _ in range(3):
                nf = hm(nf, 1, 0, 0)       # σ₀
                nf = hm(nf, 1, -h, 1)       # σ₁⁻¹
            # Quark crossings: (0,1)=uu→σ₀, (0,2)=ud→mixed, (1,2)=ud→mixed
            nf = hm(nf, 1, 0, 0)            # pair(0,1) uu → σ₀
            nf = hm(nf, 1, -h/2, 0)         # pair(0,2) ud → σ₀ mixed
            nf = hm(nf, 1, -h/2, 1)         # pair(1,2) ud → σ₁ mixed
            # Gluon self-coupling: 2 σ₀ (ILP-derived, prop:mass-endomorphism-tower)
            nf = hm(nf, 1, 0, 0)            # gluon 1
            nf = hm(nf, 1, 0, 0)            # gluon 2
        else:
            # B₃ confinement
            for _ in range(3):
                nf = hm(nf, 1, 0, 0)       # σ₀
                nf = hm(nf, 1, -h, 1)       # σ₁⁻¹
            # Quark crossings: (0,1)=ud→mixed, (0,2)=ud→mixed, (1,2)=dd→σ⁻¹
            nf = hm(nf, 1, -h/2, 0)         # pair(0,1) ud → σ₀ mixed
            nf = hm(nf, 1, -h/2, 0)         # pair(0,2) ud → σ₀ mixed
            nf = hm(nf, 1, -h, 1)           # pair(1,2) dd → σ₁⁻¹
            # Gluon self-coupling: 2 σ₀ (same as proton)
            nf = hm(nf, 1, 0, 0)            # gluon 1
            nf = hm(nf, 1, 0, 0)            # gluon 2

        # Inter-nucleon crossing with all PREVIOUS nucleons
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == 'p' and tj == 'p':
                nf = hm(nf, 1, 0, 0)        # pp: σ₀
            elif ti == 'n' and tj == 'n':
                nf = hm(nf, 1, -h, 0)       # nn: σ₀⁻¹
            else:
                nf = hm(nf, 1, D_PN, 0)     # pn/np: mixed (colour-weighted)

    # Electrons: pe crossing (EM channel, gen=1)
    for _ in range(Z):
        nf = hm(nf, 1, -h, 1)               # σ₁⁻¹

    return nf



# ══════════════════════════════════════════════════════════════
# Per-generator vertex volumes (3-channel Wedderburn-Artin)
# ══════════════════════════════════════════════════════════════

def vertex_volume(chain):
    """3-channel Wedderburn-Artin vertex volume from crossing chain.

    Each crossing (c, d) acts on the three irrep channels of H₃(q):
      symmetric:  eigenvalue cq + d
      standard:   traced volume z·a + b (from 2×2 transfer matrix)
      alternating: eigenvalue -cq⁻¹ + d

    Full volume = W_sym × λ_sym + W_std × V_std + W_alt × λ_alt.
    """
    a, b = 0.0, 1.0
    sp, ap = 1.0, 1.0
    for c, d in chain:
        a, b = a*c*h + a*d + b*c, a*c + b*d
        sp *= c*q0 + d
        ap *= -c*qi + d
    V_std = z * a + b
    return W_SYM * sp + W_STD * V_std + W_ALT * ap




def reject_float64_q(q, *, allow_float64: bool = False, where: str = "") -> None:
    """Refuse a float64 q. Owner directive: NO FLOAT64.

    Two shapes, both of which silently cap an otherwise-exact braid word at
    ~17 good digits:

      * a plain Python / numpy float;
      * an mpf whose VALUE is a float64's decimal expansion — the
        `mp.mpf(str(q_parameter.Q))` idiom, which looks like high precision
        and is not. `mass_binding_dashboard` and
        `probes/gram_qtrace_hutchinson_probe` both do exactly that.

    The source now builds crossings exactly when `q is None`, but an explicit
    `q` is used as given, so a caller can undo the whole fix from outside. That
    has to be an error rather than a quiet downgrade.

    `allow_float64=True` is the escape for paths that are legitimately f64 (the
    numpy validation kernels), so the loss is declared at the call site instead
    of hidden.
    """
    if q is None or allow_float64:
        return
    if isinstance(q, float):
        raise TypeError(
            f"{where or 'braid word'}: q is a Python float ({q!r}) — this caps "
            f"every crossing at ~17 digits. Pass the 50-dps value "
            f"(`q_parameter.Q_50_DIGIT_STR` via mpf), not `q_parameter.Q`. "
            f"Use allow_float64=True only if f64 is genuinely intended.")
    try:
        import numpy as _np
        if isinstance(q, _np.floating):
            raise TypeError(
                f"{where or 'braid word'}: q is a numpy float ({q!r}); see "
                f"q_parameter.Q_50_DIGIT_STR. allow_float64=True to override.")
    except ImportError:
        pass
    # An mpf carrying no more information than a float64.
    #
    # `mp.mpf(str(q_parameter.Q))` is the idiom: a high-precision TYPE holding
    # 17 good digits. Detected by round-trip — if the value is reproduced
    # exactly from its own float64, it holds nothing a float64 did not.
    #
    # This also rejects deliberately simple sweep values (q = 1.1 and the
    # like), which are exactly representable from their float64 too. That is
    # the intended trade: `allow_float64=True` declares such a sweep at the
    # call site, and a silent 1e-17 cap in a 50-dps pipeline is the thing this
    # is here to stop.
    try:
        import mpmath as _mp
        if isinstance(q, _mp.mpf) and _mp.mpf(repr(float(q))) == q:
            raise TypeError(
                f"{where or 'braid word'}: q is an mpf holding only float64 "
                f"information (the `mpf(str(q_parameter.Q))` idiom) — ~17 real "
                f"digits in a 50-dps path. Pass q_parameter.Q_50_DIGIT_STR. "
                f"allow_float64=True to declare a deliberately f64 sweep.")
    except ImportError:
        pass


def nucleon_gen_chains(quarks, *, q=None, allow_float64: bool = False):
    """Per-generator crossing chains for one nucleon.

    Derives chains from the quark content, matching build_nucleon_nf:
      B₃ = (σ₀σ₁⁻¹)³ contributes to both gen 0 and gen 1
      Quark pairs: (0,1)→gen=0, (0,2)→gen=0, (1,2)→gen=1

    Returns (g0_chain, g1_chain) as lists of (c, d) tuples.

    Every crossing `d` is one of the templates {0 (σ), −h (σ⁻¹), −h/2 (avg)}
    with `h = q − q⁻¹`. The structural pattern (which template at which gen)
    is q-INDEPENDENT; only `h` carries q. Pass `q` to materialise the chains
    at an arbitrary substrate value (q₀⁻¹, or an N-grid of q's for the
    simulators); `q=None` (default) uses the canonical `pyhecke.gram.h` at q₀
    and is byte-identical to the historical output, so every existing caller
    that omits `q` is unaffected. (q-parameterised-braid-word core refactor;
    docs/workplans/2026-06-17-q-parameterised-braid-word-core.md.)
    """
    # NO FLOAT64 (owner directive). `pyhecke.gram.h` is a Python float —
    # 2.61e-16 relative against the 50-dps closed form — and using it here put
    # every INTRA-nucleon crossing into the braid word at ~17 good digits.
    # This sits upstream of `atom_braid_word_3A`, so fixing only the
    # inter-nucleon crossings there still left d = -0.10453014939781968 (−h/2)
    # arriving from these chains.
    #
    # Built at >= 60 dps whatever the caller's ambient precision: an mpf keeps
    # the precision it was CREATED at, and `_PROTON_G0` and friends below are
    # module-level constants materialised at import, when nothing has raised
    # mpmath's default of 15.
    #
    # This breaks the "byte-identical to the historical output" property the
    # docstring claims for `q=None`. That output was the f64-contaminated one.
    # Consumers that genuinely need f64 (the numpy paths) cast at their own
    # boundary, where the loss is visible rather than baked in here.
    reject_float64_q(q, allow_float64=allow_float64, where="nucleon_gen_chains")
    # The three crossing templates, all built inside ONE precision context.
    #
    # Raising the precision only around `h_loc` is not enough: an mpf carries
    # the precision of the OPERATION, not just of its operands, so `-h_loc / 2`
    # evaluated outside the context is rounded to the ambient dps. These
    # constants are materialised at import, when that is mpmath's default of
    # 15 — which is how `-h/2` still arrived at -0.104530149397819654977…
    # against an exact -0.104530149397819657715…, wrong from digit 18, even
    # after h_loc itself was exact.
    if q is None:
        import mpmath as _mpm
        with _mpm.workdps(max(_mpm.mp.dps, 60)):
            from q_parameter import Q_50_DIGIT_STR as _Q50
            _qx = _mpm.mpf(str(_Q50))
            h_loc = _qx - _mpm.mpf(1) / _qx
            _d_sigma, _d_inv, _d_avg = 0, -h_loc, -h_loc / 2
    else:
        h_loc = q - 1 / q
        _d_sigma, _d_inv, _d_avg = 0, -h_loc, -h_loc / 2
    # B₃ confinement: (σ₀·σ₁⁻¹)³
    # gen 0 gets 3× σ₀ = (1, 0)
    # gen 1 gets 3× σ₁⁻¹ = (1, -h)
    g0 = [(1, _d_sigma)] * 3
    g1 = [(1, _d_inv)] * 3

    # Quark pairwise crossings
    pairs = [(0, 1, 0), (0, 2, 0), (1, 2, 1)]  # (qi, qj, gen)
    for i, j, gen in pairs:
        qi_f, qj_f = quarks[i], quarks[j]
        if qi_f == qj_f == 'u':
            cd = (1, _d_sigma)    # σ
        elif qi_f == qj_f == 'd':
            cd = (1, _d_inv)      # σ⁻¹
        else:
            cd = (1, _d_avg)      # mixed
        if gen == 0:
            g0.append(cd)
        else:
            g1.append(cd)

    # Gluon self-coupling: 2 σ₀ per nucleon (ILP-derived)
    g0.append((1, 0))
    g0.append((1, 0))

    return g0, g1



# Precomputed per-generator chains for proton and neutron
_PROTON_G0, _PROTON_G1 = nucleon_gen_chains(['u', 'u', 'd'])

_NEUTRON_G0, _NEUTRON_G1 = nucleon_gen_chains(['u', 'd', 'd'])



def atom_gen_chains(Z, N):
    """Per-generator crossing chains for atom (Z, N).

    Builds the complete atomic braid crossing chains for generators
    σ₀ and σ₁, including:
      1. Intra-nucleon crossings (B₃ + quark pairs) — from nucleon_gen_chains
      2. Inter-nucleon crossings between ALL nucleon pairs — on gen 0
      3. Electron crossings (pe) — on gen 1

    Nucleon ordering: pp...nn (protons first, then neutrons).

    Inter-nucleon crossings (strong force, gen 0):
      pp: (1, 0)     — positive crossing
      nn: (1, -h)    — inverse crossing
      pn: (1, -h/2)  — mixed crossing

    Returns (g0_chain, g1_chain).
    """
    g0, g1 = [], []

    # Build nucleon ordering (interleaved, matching build_atom_nf)
    A = Z + N
    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p')
            pc += 1
        else:
            ordering.append('n')
            nc += 1

    # 1. Nucleon crossings + inter-nucleon (matching build_atom_nf order)
    # Each nucleon's intra-nucleon crossings, then inter-nucleon with ALL previous
    for k in range(A):
        nuc_type = ordering[k]
        if nuc_type == 'p':
            g0.extend(_PROTON_G0)
            g1.extend(_PROTON_G1)
        else:
            g0.extend(_NEUTRON_G0)
            g1.extend(_NEUTRON_G1)

        # Inter-nucleon crossings with all previous nucleons (gen 0)
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == 'p' and tj == 'p':
                g0.append((1, 0))       # pp: σ₀
            elif ti == 'n' and tj == 'n':
                g0.append((1, -h))      # nn: σ₀⁻¹
            else:
                g0.append((1, D_PN))    # pn: mixed (colour-weighted)

    # 2. Electron crossings: pe = σ⁻¹ on gen 1
    for _ in range(Z):
        g1.append((1, -h))

    return g0, g1



def atom_V_full(Z, N):
    """Quark-level per-generator V̂_i^full for the mass-tower formula.

    Uses atom_gen_chains to get the FULL braid (B₃ × quarks +
    inter-nucleon + electrons), then computes the Wedderburn-weighted
    traced volume per generator:

      V̂_i^full = w_sym·λ_sym + w_std·V_std + w_alt·λ_alt

    For H₃(q), i ∈ {0, 1} (two generators).

    Returns (V0_full, V1_full) as floats.

    Reference: prop:mass-endomorphism-tower, thm:wedderburn-mass-formula
    """
    g0_chain, g1_chain = atom_gen_chains(Z, N)
    return _chain_V_full(g0_chain), _chain_V_full(g1_chain)



def _chain_V_full(chain):
    """Wedderburn-weighted traced volume from a crossing chain.

    chain: list of (c, d) tuples.
    Returns V̂^full = w_sym·λ_sym + w_std·V_std + w_alt·λ_alt.
    """
    lam_sym = 1.0
    for c, d in chain:
        lam_sym *= c * q0 + d

    lam_alt = 1.0
    for c, d in chain:
        lam_alt *= -c * qi + d

    M00, M01, M10, M11 = 1.0, 0.0, 0.0, 1.0
    for c, d in chain:
        t00 = c * h + d; t01 = c; t10 = c; t11 = d
        n00 = M00*t00 + M01*t10; n01 = M00*t01 + M01*t11
        n10 = M10*t00 + M11*t10; n11 = M10*t01 + M11*t11
        M00, M01, M10, M11 = n00, n01, n10, n11
    V_std = z * M10 + M11  # second row: [a,b] = [0,1] × M → (M₁₀, M₁₁)

    return W_SYM * lam_sym + W_STD * V_std + W_ALT * lam_alt



def atom_per_generator_volumes(Z, N, include_inter=True, crossings_per_pair=1,
                                m_pp=None, m_pn=None, m_nn=None):
    """Per-generator additive Wedderburn volumes V̂_i^full for the atom braid.

    ⚠️  KNOWN BUG (audit 2026-05-25, PR #1238):
    This function uses HARDCODED H_3 Wedderburn weights regardless of
    atom size A. For A > 1 (deuteron, ⁴He, ⁶Li, ...), the braid lives
    in H_{3A}(q), not H_3(q), and the H_3 weights are systematically
    wrong. See docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md.

    The CANONICAL replacement is:
        computations/mass_at_3A_proper.py
            per_generator_V_hat_3A(Z, N)
    which sums over all partitions of 3A with proper Wedderburn weights.

    NO WEIGHT SCHEME HERE IS KNOWN-GOOD, and this warning should not be read as
    endorsing one (bean qou-2tuv):
      - `normalized_plancherel` (the default) sums to 1 as the Markov identity
        requires, but puts max|V_hat| at 1.08837 against a phi_q_safe cap of
        1.087779 — AT the pole — so `binding_3A_tower` returns ~1e7 MeV. It was
        marked DEPRECATED by docs/audits/2026-05-11-plancherel-usage-audit.md.
      - `jones_wenzl` keeps V_hat small, but only because its weights DO NOT
        SUM TO 1: measured -0.8230 at A=1, +0.0547 at A=2, -0.0009 at A=3. It
        buys a finite tower by driving the volumes toward zero.
    Migrating for the weights alone therefore trades one defect for another.

    Migration is a PACKAGE swap, not a drop-in function substitution. The
    H_{3A} volumes come with (a) the jones_wenzl weights, (b) a free-baseline
    subtraction B ~ (free - atom), and (c) the alpha = m_e * Vol_q(B_3) scale
    from prop:binding-scale-catalan feeding the Phi_q tower, NOT the
    `sum ln|V|` proxy. Swapping only the function and keeping the old consumer
    measures -1650% on the deuteron; the full package measures -30.1% against
    production's +81.6%.

    Feasibility caveat: the H_{3A} sum runs over p(3A) — 77 at A=4, 17,977 at
    A=12, 1.8e9 at A=40 — and mass_at_3A_proper's own header says it "fails for
    3A >~ 35". Callers that scan heavy nuclei CANNOT migrate; they must declare
    the H_3 approximation instead.

    Migration is NOT YET DONE for the 15+ callers (mass_formula_6term.py,
    tower_isotope_absolute.py, paper_six_term_isotope_sweep.py, ...).
    Per-call migration is required because the return shape differs:
        legacy:  [{"std": Vs, "sym": sp, "alt": ap, "full": Vf}, ...]
        proper:  [{"full": V̂_i, "gen_word": [...]}, ...]
    A separate dedicated PR is queued for the migration sweep.

    If m_pp, m_pn, m_nn are given (ILP solution), use them per pair type.
    Otherwise fall back to uniform crossings_per_pair.

    Returns a list of length n_strands - 1 = 3A - 1 (atom case) or
    n_strands - 1 = 2A (free case) of dicts:
        [{"std": Vs, "sym": sp, "alt": ap, "full": Vf}, ...]
    indexed by generator position i = 0, 1, ..., len-1.

    These are the V̂_i^full feeding the tower formula
    (prop:mass-endomorphism-tower):
        𝔪(W) = |Π V̂_i| + Σ Φ_q(|V̂_i|)
              + z² Σ_{|i-j|=1} Φ_q(|V̂_i V̂_j|).

    Implementation: replays _step_chain_generic for each nucleon, but
    instead of tracking a single accumulated YSN matrix, accumulates
    per-generator (a, b, sp, ap) — the additive Wedderburn channel
    state.  Mirrors mass_endomorphism.additive_wedderburn_volumes
    extended to A-nucleon atoms.

    Parameters
    ----------
    Z, N : int
        Proton and neutron counts.
    include_inter : bool
        If True: full atom braid with pp/nn/pn inter-nucleon crossings.
        If False: free disconnected-tensor baseline.

    Returns
    -------
    list of dict, one per generator.
    """
    A = Z + N
    if A < 1:
        return []

    # H_3 vs H_{3A} legacy bug warning (audit 2026-05-25, PR #1238).
    # For A > 1 the H_3 Wedderburn weights used below are systematically
    # wrong. Callers should migrate to mass_at_3A_proper.per_generator_V_hat_3A.
    if A > 1:
        import warnings
        warnings.warn(
            f"atom_per_generator_volumes uses H_3 Wedderburn weights for "
            f"A={A} atom (Z={Z}, N={N}); H_{{3A}}={3*A} weights are correct. "
            "See docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md. "
            "Migrate to mass_at_3A_proper.per_generator_V_hat_3A.",
            DeprecationWarning,
            stacklevel=2,
        )

    # Nucleon ordering (Z protons then N neutrons) — matches
    # atom_character_raw convention.
    ordering = ['p'] * Z + ['n'] * N

    # n_gens for the joint braid
    if include_inter:
        n_strands = 3 * A
        n_gens_total = n_strands - 1  # 3A - 1
    else:
        # Free baseline: per-nucleon disjoint blocks of 2 generators each
        n_gens_total = 2 * A

    # Per-generator accumulators (a, b for std; sp for sym; ap for alt)
    a_arr  = [0.0] * n_gens_total
    b_arr  = [1.0] * n_gens_total
    sp_arr = [1.0] * n_gens_total
    ap_arr = [1.0] * n_gens_total

    # Build the atom braid by walking the nucleon chain.  For each
    # nucleon k, the intra-nucleon crossings live on local gens; for
    # the joint braid, these are mapped to global gens 3k, 3k+1.
    # Inter-nucleon crossings (when include_inter) live on gen 3k+2,
    # connecting nucleon k with nucleon k+1.
    for k, nuc in enumerate(ordering):
        intra    = _PROTON_G0 if nuc == 'p' else _NEUTRON_G0
        intra_g1 = _PROTON_G1 if nuc == 'p' else _NEUTRON_G1
        if include_inter:
            base_g0 = 3 * k       # global gen for first intra slot
            base_g1 = 3 * k + 1   # global gen for second intra slot
        else:
            base_g0 = 2 * k
            base_g1 = 2 * k + 1
        # Intra-nucleon, first generator slot
        for c, d in intra:
            i = base_g0
            a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i] = a_new
            b_arr[i] = b_new
            sp_arr[i] *= c * q0 + d
            ap_arr[i] *= -c * qi + d
        # Intra-nucleon, second generator slot
        for c, d in intra_g1:
            i = base_g1
            a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i] = a_new
            b_arr[i] = b_new
            sp_arr[i] *= c * q0 + d
            ap_arr[i] *= -c * qi + d
        # Inter-nucleon crossings (only when include_inter and k < A-1)
        # crossings_per_pair: number of repetitions of the basic pair
        # crossing.  For ILP-stable pairs, this should be derived from
        # Frobenius positivity (currently a parameter; see witness).
        if include_inter and k < A - 1:
            i = 3 * k + 2  # global gen for inter-nucleon between k and k+1
            next_nuc = ordering[k + 1]
            if nuc == 'p' and next_nuc == 'p':
                base_cross = (1.0, 0.0)      # pp: σ
                m_this = m_pp if m_pp is not None else crossings_per_pair
            elif nuc == 'n' and next_nuc == 'n':
                base_cross = (1.0, -h)       # nn: σ⁻¹
                m_this = m_nn if m_nn is not None else crossings_per_pair
            else:
                base_cross = (1.0, D_PN)     # pn: colour-weighted mixed
                m_this = m_pn if m_pn is not None else crossings_per_pair
            pair_cross = [base_cross] * m_this
            for c, d in pair_cross:
                a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
                b_new = a_arr[i] * c + b_arr[i] * d
                a_arr[i] = a_new
                b_arr[i] = b_new
                sp_arr[i] *= c * q0 + d
                ap_arr[i] *= -c * qi + d

    # Build per-generator V̂_full from accumulators.
    #
    # `z` and `W_SYM/W_STD/W_ALT` come from `pyhecke.gram` — the module this
    # file already imports them from at the top. They used to be SHADOWED here
    # by a local recomputation, and the two had diverged:
    #
    #   local  z_mark = 1/(q^½ + q^-½) = 0.4993203  ← convention **C**
    #   gram   z      = q³/(q²+1)      = 0.6126880  ← convention **D**
    #
    # The owner ruling of 2026-08-09 excised C repo-wide (`33a6c7aa4`, "the
    # trace is now D everywhere") and `gram.py` moved to D on 2026-08-15, but
    # this local copy was never registered as a C implementation
    # (docs/coordination/trace-convention-registry.json lists only the two
    # `_HISTORICAL` sites in schur_principal_mpmath and `gram.py::z`), so the
    # migration never visited it. Every one of the callers of this function was
    # still getting C.
    #
    # The weights were NOT divergent — the local recomputation reproduced
    # gram's W_SYM/W_STD/W_ALT to the last f64 digit — but recomputing a
    # constant that is imported three lines above is how the `z` fork happened
    # in the first place, so both now come from the single source.
    #
    # NOTE: these remain the H_3 weights, which are wrong for A > 1 — see the
    # DeprecationWarning above. Fixing the convention does not fix that.
    vols = []
    for i in range(n_gens_total):
        Vs = z * a_arr[i] + b_arr[i]
        Vf = W_SYM * sp_arr[i] + W_STD * Vs + W_ALT * ap_arr[i]
        vols.append({"std": Vs, "sym": sp_arr[i], "alt": ap_arr[i], "full": Vf})
    return vols



def build_nucleon_nf(quarks):
    """Build a single nucleon NF from quark content.

    quarks: list of 'u' or 'd' characters, e.g. ['u','u','d'] for proton.

    Construction: nucleon = B₃ · crossings(quarks)
    where B₃ = (σ₀σ₁⁻¹)³ is the gluon field (Borromean confinement),
    and crossings encode flavor:
      uu → σ_gen (c=1, d=0)
      dd → σ_gen⁻¹ (c=1, d=-h)
      ud → ½(σ_gen + σ_gen⁻¹) (c=1, d=-h/2)

    Generator assignment: pair (i,j) uses gen = i (the lower quark index).
    For 3 quarks: (0,1)→gen=0, (0,2)→gen=0, (1,2)→gen=1.

    ⚠️  NO GLUON TERM — and this is a DEFECT, not a convention.

    This builder stops at B₃ + quarks = 9 crossings. The line that used to
    stand here, "No separate gluon dressing — B₃ IS the gluon structure",
    asserted that omission was deliberate. Nothing backs it: it cites no
    proposition, no ILP, no SDP, and it contradicts the framework it sits in.
    `computations/sdp_gamma_gamma_to_qqbar.py` decomposes the proton into FOUR
    SDP components — H₃ for the Borromean B₃, H₃ per quark pair, **H₂ for the
    2·σ₀ gluon self-coupling**, then LR cross-level embedding — so the gluon
    term is a separate derived component, not something B₃ already contains.
    `prop:mass-endomorphism-tower` carries the ILP derivation, cited at the
    gluon lines of `build_atom_nf`.

    6 (B₃) + 3 (quarks) + 2 (gluon) = 11 is the SDP-consistent budget. Use
    `build_atom_nf` / `build_atom_nf_exact`, which build it in braid order.

    Kept for the consumers that already read `PROTON_NF` / `NEUTRON_NF`;
    do not build anything new on it. Bean qou-1qsw.
    """
    nf = [1.0, 0, 0, 0, 0, 0]
    # B₃ confinement: (σ₀·σ₁⁻¹)³
    for _ in range(3):
        nf = hm(nf, 1, 0, 0)       # σ₀
        nf = hm(nf, 1, -h, 1)      # σ₁⁻¹
    # Quark pairwise crossings: (0,1), (0,2), (1,2)
    pairs = [(0, 1), (0, 2), (1, 2)]
    for i, j in pairs:
        qi, qj = quarks[i], quarks[j]
        gen = i  # generator = lower index
        if qi == qj == 'u':
            nf = hm(nf, 1, 0, gen)       # σ_gen
        elif qi == qj == 'd':
            nf = hm(nf, 1, -h, gen)      # σ_gen⁻¹
        else:  # mixed u-d
            nf = hm(nf, 1, -h/2, gen)    # ½(σ + σ⁻¹)
    return nf



def nucleon_braid_word(quarks, dps: int = 50):
    """The nucleon's 11 crossings as a `(c, d, gen)` word in **BRAID ORDER**.

    This is `build_atom_nf`'s per-nucleon block expressed as a word rather
    than folded into an NF, so a trace routine can consume it directly:

        B_3 = (sigma_0 . sigma_1^-1)^3        6 crossings, ALTERNATING
        quark pairs (0,1)@0 (0,2)@0 (1,2)@1   3
        gluon self-coupling 2 . sigma_0@0     2   (ILP, prop:mass-endomorphism-tower)

    **Why the order is not free.** `sigma_0` and `sigma_1` do not commute, so
    re-sorting the crossings by generator is a different element of `H_3(q)` --
    not a re-parameterisation. It matters most exactly where it looks most
    innocuous: on `B_3` alone, at the substrate q_0,

        (s0 s1^-1)^3  tr_M = 0.99856216383678726595     the Borromean braid
        s0^3 s1^-3    tr_M = 0.18006453953550109830     its monotone re-sort

    an 81.97 % difference, and essentially the whole 82.06 % gap seen on the
    full nucleon. The alternation IS the Borromean structure that `B_3` is
    named for, so flattening it substitutes a different link rather than
    perturbing the intended one.

    ⚠️  DO NOT SWAP THIS IN FOR THE MONOTONE WORD. It is provided for
    comparison and for callers who genuinely want the literal per-nucleon
    braid; it is NOT established as the correct H_3 reduction, and measurement
    currently points the other way.

    The independent Markov-peel route
    (`binding_combiner_markov_peel_fallback.py`) builds from
    `atom_braid_word_3A` — the 3A-strand word, which never passes through
    `nucleon_gen_chains` and so shares no ordering assumption with it — and its
    committed deuteron value `0.575172243917771870826535` matches what the
    MONOTONE H_3 word gives, not what this braid-order word gives (0.151968…).
    So the monotone form appears to be the correct H_3 *reduction* of the 3A
    braid, even though it is not the literal sub-braid, and the fact that its
    shape was originally chosen to satisfy `chi_all_lambda` (a fine-Bratteli
    transfer matrix that applies `O_g` once per generator in increasing order
    and raises on a non-monotone word) does not by itself make it wrong.

    What remains established: the two orderings are different elements, 82 %
    apart on tr_M, essentially all of it from `B_3`. What is NOT established is
    which is the right reduction. Bean qou-1qsw.
    """
    hv = h_mp(dps)
    one, zero = _mp.mpf(1), _mp.mpf(0)
    w = []
    for _ in range(3):                       # B_3, alternating
        w.append((one, zero, 0))             # sigma_0
        w.append((one, -hv, 1))              # sigma_1^-1
    for i, j, gen in [(0, 1, 0), (0, 2, 0), (1, 2, 1)]:
        a, b = quarks[i], quarks[j]
        if a == b == 'u':
            w.append((one, zero, gen))
        elif a == b == 'd':
            w.append((one, -hv, gen))
        else:
            w.append((one, -hv / 2, gen))
    w.append((one, zero, 0))                 # gluon 1
    w.append((one, zero, 0))                 # gluon 2
    return w


def build_nucleon_nf_mp(quarks, dps: int = 50):
    """float64-free twin of `build_nucleon_nf`, at the TRUE substrate q_0.

    Same construction, same crossing order, same generator assignment — only
    the arithmetic differs. Every coefficient is `mpmath.mpf` and `h` comes
    from `gram.h_mp(dps)`, i.e. `q_0 - q_0**-1` at the 50-dps substrate
    string.

    **Why not `hm_exact`.** The module's Fraction path is exact arithmetic at
    the RATIONAL MODEL `q = 111/100`, which differs from the substrate
    `q_0 = 1.1099785827513808` by 1.93e-5 relative (gram.py says so at
    `_Z_FRAC`). Measured on this builder's own output, that propagates to a
    **1.66e-5 relative deviation** — 16.6 ppm — so routing it through the
    Fraction path would be float-free and eleven orders of magnitude WORSE
    than the float64 it replaced. Exactness of the arithmetic and correctness
    of the anchor are separate properties, and only the mp path has both.

    Measured agreement with the float64 builder: max relative difference
    1.4e-16 (proton) and 6.0e-17 (neutron), i.e. the float path was already
    correct to its own precision — this twin extends the precision, it does
    not correct a value.

    **What this does not change.** `build_nucleon_nf`, `PROTON_NF` and
    `NEUTRON_NF` are untouched, so no existing consumer moves. This is the
    additive twin the module already uses elsewhere (`build_atom_nf` /
    `build_atom_nf_exact`); callers who need more than float64 opt in.
    """
    hv = h_mp(dps)
    nf = [_mp.mpf(1)] + [_mp.mpf(0)] * 5
    one, zero = _mp.mpf(1), _mp.mpf(0)
    # B_3 confinement: (sigma_0 . sigma_1^-1)^3
    for _ in range(3):
        nf = hm_mp(nf, one, zero, 0, dps)        # sigma_0
        nf = hm_mp(nf, one, -hv, 1, dps)         # sigma_1^-1
    # Quark pairwise crossings: (0,1), (0,2), (1,2); generator = lower index
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        qi_, qj_ = quarks[i], quarks[j]
        gen = i
        if qi_ == qj_ == 'u':
            nf = hm_mp(nf, one, zero, gen, dps)      # sigma_gen
        elif qi_ == qj_ == 'd':
            nf = hm_mp(nf, one, -hv, gen, dps)       # sigma_gen^-1
        else:
            nf = hm_mp(nf, one, -hv / 2, gen, dps)   # (sigma + sigma^-1)/2
    return nf


# Precomputed nucleon NFs
PROTON_NF = build_nucleon_nf(['u', 'u', 'd'])

NEUTRON_NF = build_nucleon_nf(['u', 'd', 'd'])


__all__ = [
    "_ID_NF",
    "build_nucleon_nf_mp",
    "nucleon_braid_word",
    "_PROTON_G0", "_PROTON_G1", "_NEUTRON_G0", "_NEUTRON_G1",
    "PROTON_NF", "NEUTRON_NF",
    "build_atom_nf_exact", "nf_channel_exact", "check_frobenius",
    "build_atom_nf", "vertex_volume", "nucleon_gen_chains",
    "atom_gen_chains", "atom_V_full", "_chain_V_full",
    "atom_per_generator_volumes", "build_nucleon_nf",
]
