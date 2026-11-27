#!/usr/bin/env python3
"""The EM (Coulomb) channel of binding on the nucleus block: ranks 0, 1, 2 — gap G3.

Bean qou-tcl3. Ledger: docs/audits/2026-11-27-term-completeness-ledger.md (PR #9658), gap G3.
Lean: folio/quantum-observable-universe/lean/QOU/Nuclear/CoulombIsospinChannel.lean.
Audit: docs/audits/2026-11-27-coulomb-isospin-channel.md.

The ledger's cap table puts the EM channel at the two-body charge operator Σ_{i<j} Q_i Q_j,
ranks r ≤ 2, so a multiplet's T_z dependence is a + b·T_z + c·T_z². This module supplies
that term with its OWN scale:

    E_EM(Z, A) = ε · Z(Z − 1)/2 = ε·a(A) + ε·b(A)·T_z + ε·c·T_z²,   T_z = (Z − N)/2,
    a(A) = A(A − 2)/8,  b(A) = (A − 1)/2,  c = 1/2                (exact, Lean `chargePairs_imme`)
    ε    = 2 f · αħc / r_rms                                       (one proton-pair weight)

What each factor is, and its status:

* a, b, c — DERIVED, exact rationals (Lean, generic field). No measured input.
* f       — the q-Hankel (Hahn–Exton) shape factor 0.520011, pre-registered and scale-free
            (PR #9665, bean qou-usft). DERIVED, not selected against any target. Until #9665
            merges the value is carried here as a 60-digit string with its provenance; the
            uniform ball f = (3/5)^{3/2} is kept for comparison only.
* αħc     — α DERIVED from q₀ (conditional on the Witten-κ Gram `sorry`); ħc is a unit.
* r_rms   — OPEN. The corpus has no derived energy-to-length map (beans qou-mbfv, qou-usft).
            The only length available is the CAL-3 one used by `coulomb_energy.py`,
            R = λ̄_π·A^{1/3} with coefficient 1 SELECTED and A^{1/3} ASSUMED. It is passed in
            explicitly and every number that uses it is tagged CONDITIONAL. Nothing here
            chooses a length to match a target.

The ratios b/c = A − 1 and a/c = A(A − 2)/4 hold for ANY length: they are the part of the EM
channel that the length cannot move. That is what this module adds that `coulomb_energy.py`
did not state: the charge structure of all three entries, separated from the one open scale.

Hartree reading (named, not hidden): one pair weight for every proton pair. Exchange and
correlation give the three ranks separate weights; that is a named residual (the Nolen–Schiffer
direction), not a parameter here.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()

# ── shape factor f = E_C · r_rms / Q² ─────────────────────────────────────────
# Primary row `primary_nu_half_p_1_over_q0` of
# computations/probes/coulomb-shape-factor-qbessel-probe.witness.json (PR #9665, branch
# claude/coulomb-shape-qbessel-2026-11-27, commit dd01a5fbd4af), computed at 70 dps.
# Pre-registered before its first run; scale-free (E_q(2) has a q^Z dilation symmetry).
F_QHANKEL = mp.mpf("0.520010562994850862465840107226616923677672899831771179340096")
F_QHANKEL_PROVENANCE = ("q-Hankel J_{1/2}(p^k; p^2), p = 1/q0, full Jackson lattice; "
                        "PR #9665 witness, primary row (pre-registered)")
# Uniform ball: E = (3/5) Q²/R and r_rms = sqrt(3/5) R, so f = (3/5)^{3/2}. Comparison only.
F_UNIFORM_BALL = (mp.mpf(3) / 5) ** mp.mpf("1.5")


# ── exact charge structure (Lean: chargePairs_imme, emA/emB/emC) ──────────────
def em_coefficients(A: int) -> tuple[Fraction, Fraction, Fraction]:
    """(a, b, c) with Z(Z − 1)/2 = a + b·T_z + c·T_z², T_z = (Z − N)/2. Exact."""
    A = Fraction(A)
    return A * (A - 2) / 8, (A - 1) / 2, Fraction(1, 2)


def charge_pairs(Z: int) -> Fraction:
    """Number of unordered proton pairs, Z(Z − 1)/2."""
    return Fraction(Z * (Z - 1), 2)


def t_z(Z: int, A: int) -> Fraction:
    """Isospin projection, proton +1/2."""
    return Fraction(Z - (A - Z), 2)


def em_rank_split(A: int, T: Fraction, Tz: Fraction) -> dict[str, Fraction]:
    """Rank-0/1/2 pieces of the charge structure inside a multiplet of isospin T
    (Lean: imme_rank_split, em_rank_zero). Sum equals Z(Z − 1)/2."""
    a, b, c = em_coefficients(A)
    tt = T * (T + 1)
    return {"rank0": a + c * tt / 3, "rank1": b * Tz, "rank2": c * (Tz * Tz - tt / 3)}


# ── the one EM scale ───────────────────────────────────────────────────────────
def alpha_hbar_c() -> "mp.mpf":
    from coulomb_energy import alpha_em_hbar_c_mev_fm
    return alpha_em_hbar_c_mev_fm()


def pair_weight_mev(r_rms_fm, f=None) -> "mp.mpf":
    """ε = 2 f αħc / r_rms (MeV): the proton-pair weight. r_rms is the OPEN length."""
    f = F_QHANKEL if f is None else f
    return 2 * f * alpha_hbar_c() / mp.mpf(r_rms_fm)


def r_rms_cal3_conditional(A: int) -> "mp.mpf":
    """CONDITIONAL length: r_rms = sqrt(3/5)·λ̄_π·A^{1/3}, the rms radius of the uniform
    ball that `coulomb_energy.nuclear_radius_fm` uses (coefficient 1 on ħc/m_π selected,
    A^{1/3} assumed). Not derived; carried only so a number can be printed."""
    from coulomb_energy import nuclear_radius_fm
    return mp.sqrt(mp.mpf(3) / 5) * nuclear_radius_fm(A)


def em_energy_mev(Z: int, A: int, r_rms_fm, f=None) -> "mp.mpf":
    """E_EM = ε · Z(Z − 1)/2 (MeV). Subtract from a strong-only binding."""
    cp = charge_pairs(Z)
    return pair_weight_mev(r_rms_fm, f) * mp.mpf(cp.numerator) / cp.denominator


def em_energy_times_length(Z: int, f=None) -> "mp.mpf":
    """E_EM · r_rms (MeV·fm): the length-free content of the EM entry."""
    f = F_QHANKEL if f is None else f
    cp = charge_pairs(Z)
    return 2 * f * alpha_hbar_c() * mp.mpf(cp.numerator) / cp.denominator


if __name__ == "__main__":
    for A in (3, 4, 6, 7, 12, 40, 208):
        print(A, *em_coefficients(A))
