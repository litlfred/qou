#!/usr/bin/env python3
"""DERIVATION — per-block binding via the Hecke BAR-pairing (non-archimedean).

Follow-up to the modulus cleanup (PR #1738,
docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md). The per-block
ARCHIMEDEAN realization is

    B_arch(K) = E_0 · Σ_λ y_λ ( |χ^λ(W_free)| − |χ^λ(W_atom)| ) ,

where `|·|` is the archimedean modulus — defined ONLY at the real place. The
framework's general observation is the Hecke BAR-involution q ↦ q⁻¹ (the
Kazhdan–Lusztig bar; §7b "bar-involution invariant by construction"), which is
a ℤ-algebra involution defined over ANY base ring (char p, p-adic, formal q).
The bar-NORM of a channel is the bar-pairing

    ⟨χ^λ⟩ := χ^λ(q) · χ^λ(q⁻¹)            (always real; symmetric under q↔q⁻¹)

and its χ-dimension "length" (the algebraic generalization of |χ| = √(χ·χ̄)) is

    ‖χ^λ‖_bar := √( χ^λ(q) · χ^λ(q⁻¹) ) .

At the real place with real χ, χ^λ(q⁻¹) is the MIRROR (chirality) image of the
Jones character, so ⟨χ^λ⟩ = χ^λ(q)·χ^λ(q⁻¹) pairs the braid with its mirror —
binding-as-bar-norm is intrinsically a chirality pairing; |χ^λ|² is its achiral
archimedean shadow. When ⟨χ^λ⟩ < 0 the bar-length is imaginary: a GROWTH
(non-rotation) channel, consistent with the q-Reeb arccosh decomposition
(binding_reeb_phase_decomposition.py).

The per-block bar binding:

    B_bar(K) = E_0 · Σ_λ y_λ ( ‖χ^λ(W_free)‖_bar − ‖χ^λ(W_atom)‖_bar ) ,

with y_λ the canonical Wenzl weight evaluated symmetrized over q, q⁻¹.

ZERO fit. χ^λ from Hoefsmit (pure-Python, evaluated at q₀ AND q₀⁻¹); y_λ from
the Wenzl bridge. AME used only for the final comparison. Light isotopes
(D n=6, T n=9) — ³He/⁴He are heavier and deferred (same kernel).

FINDING (2026-06-03). The per-block bar-LENGTH does NOT improve the binding —
it underbinds badly:

    D:  B_arch = 2.304 MeV (+3.6%)   vs   B_bar = 0.660 MeV (−70.3%).

The obstruction is structural: ~half the Wedderburn channels are GROWTH channels
where χ^λ(q₀)·χ^λ(q₀⁻¹) < 0 (deuteron: 4/5 free, 5 atom), i.e. the bar-length is
genuinely IMAGINARY (the q-Reeb arccosh / hyperbolic regime). Taking its
magnitude discards that phase, and evaluating χ^λ at the MIRROR point q₀⁻¹ gives
a systematically smaller value than the observation at q₀.  (D is decisive on its
own; T n=9 did not complete in the compute budget — pure-Python χ at two q-points
is minutes-slow — so the finding rests on the deuteron.)

Conclusion — consistent with #1738, NOT a reversal of it: the CATEGORICAL
convention is correctly signed/bar (the fibre object lives over generic q, with
the bar q↦q⁻¹ its natural involution). But the ARCHIMEDEAN OBSERVATION at the
substrate anchor is |χ^λ(q₀)|, NOT the mirror pairing √(χ(q₀)·χ(q₀⁻¹)). The bar
does not "fix" the binding magnitude; the +3.6% archimedean deuteron stands. This
is recorded so a later agent does not naively bar-ify the observation step.
"""
from __future__ import annotations

import os
import sys as _sys
from pathlib import Path as _Path
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_Path(__file__).resolve().parent / _d)
    if _p not in _sys.path:                     # guard: no duplicate / shadowing
        _sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401 — Phase-6 bridge

import mpmath as mp  # noqa: E402

from habiro_coefficients_interpolate import (  # noqa: E402
    chi_lambda_numerical, atomic_braid_to_crossings,
)
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from schur_weyl_symbolic import partitions_of  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402 — CAL-1
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Use the framework compute precision (set_compute_dps() → COMPUTE_DPS) and
# capture it from the setter's return value, so the witness
# precisionMetadata.compute_dps equals the dps the run actually used (per
# Copilot review: the previous deliberate low-dps override desynced the
# metadata, which records COMPUTE_DPS). This exploratory script reports a
# structural ±70 % effect — far above any precision floor — so the framework
# default is more than sufficient; DPS is threaded into the χ/y evaluation.
DPS = set_compute_dps()
q0 = mp.mpf(str(Q0))                          # str(Q0): no float() roundtrip
qi = 1 / q0                                   # bar image q ↦ q⁻¹
M_E = mp.mpf(str(M_E_MEV))
E0 = M_E / (q0 * (q0 - 1))                     # 𝔈₀ ≈ 4.186 MeV (calibration)

# Per-run memo for _channels: each (Z,N,inter,qv) χ/y evaluation is reused
# across the archimedean and bar passes (and across free/atom), so cache it.
_CHANNELS_CACHE: dict = {}

# D (n=6) runs in ~3 s and already establishes the finding. T (n=9, set
# QOU_BAR_INCLUDE_T=1) evaluates χ at q₀ AND q₀⁻¹ over partitions of 9 and
# takes minutes — confirming-only, kept off the default path for CI speed.
ISO = {"D": (1, 1)}
if os.environ.get("QOU_BAR_INCLUDE_T") == "1":
    ISO["T"] = (1, 2)
AME_B = {"D": mp.mpf("2.2245662"), "T": mp.mpf("8.4818")}


def _channels(Z, N, inter, qv):
    """{λ: (y_λ(qv), χ^λ(braid; qv))} over partitions of 3A with non-zero dim.

    Memoized per run (key includes str(qv) since mpf is not a stable dict
    key) — reused across the archimedean/bar passes and free/atom configs."""
    key = (Z, N, inter, str(qv))
    if key in _CHANNELS_CACHE:
        return _CHANNELS_CACHE[key]
    cr = atomic_braid_to_crossings(Z, N, include_inter=inter)
    out = {}
    for lam in partitions_of(3 * (Z + N)):
        chi, d = chi_lambda_numerical(lam, qv, cr)
        if d == 0:
            continue
        y = y_lambda_wenzl_bridge_numeric(lam, qv, dps=DPS)
        out[lam] = (y, chi)
    _CHANNELS_CACHE[key] = out
    return out


def _bar_length(chi_q, chi_qi):
    """‖χ‖_bar = √(χ(q)·χ(q⁻¹)); real on rotation channels, imaginary on
    growth channels (⟨χ⟩ < 0). Returns (value, is_growth).

    The pairing is real at the substrate anchor (Im(q₀)=0); take the real
    part to drop the ~0 mpc imaginary noise before the sign test / sqrt."""
    pairing = mp.re(chi_q * chi_qi)         # mp.re: safe for mpf and mpc
    if pairing >= 0:
        return mp.sqrt(pairing), False
    return mp.sqrt(-pairing), True       # magnitude of the imaginary length


def _per_block_bar(Z, N, inter):
    """Σ_λ y_λ ‖χ^λ‖_bar over the braid, and a growth-channel tally.

    y_λ is bar-symmetrized: (y_λ(q₀)+y_λ(q₀⁻¹))/2 (real, bar-invariant).
    c0 and ci share the same partition keys (dim is q-independent)."""
    c0 = _channels(Z, N, inter, q0)
    ci = _channels(Z, N, inter, qi)
    total = mp.mpf(0)
    n_growth = 0
    for lam, (y0, chi0) in c0.items():
        if lam not in ci:                      # dim is q-independent, but guard
            continue                           # against a channel skipped at qi
        yi, chii = ci[lam]
        y_bar = mp.re((y0 + yi) / 2)           # bar-symmetric weight (real)
        length, growth = _bar_length(chi0, chii)
        n_growth += int(growth)
        total += y_bar * length
    return total, n_growth


def _per_block_arch(Z, N, inter):
    """Σ_λ y_λ |χ^λ(q₀)| — the archimedean per-block realization.

    The observable at q₀ is real (Im(q₀)=0), so this returns the y_λ-weighted
    real-part magnitude  Σ_λ Re(y_λ)·|Re χ^λ(q₀)|  (signed weight times the
    magnitude of the real character), NOT the complex modulus — so the ~0 mpc
    imaginary noise does not bias the sum upward (per Copilot review)."""
    c0 = _channels(Z, N, inter, q0)
    return sum(mp.re(y) * abs(mp.re(chi)) for y, chi in c0.values())


def main() -> int:
    print(f"E_0 = {float(E0):.4f} MeV   q₀ = {float(q0):.6f}   "
          f"q₀⁻¹ = {float(qi):.6f}   dps = {DPS}")
    print("per-block BAR-pairing ‖χ‖_bar = √(χ(q₀)·χ(q₀⁻¹))  vs  "
          "archimedean |χ(q₀)|\n")
    print(f"{'iso':<5}{'B_arch':<10}{'B_bar':<10}{'AME':<9}"
          f"{'arch err%':<11}{'bar err%':<11}{'growth ch':<10}")
    results = {}
    for name, (Z, N) in ISO.items():
        # The Hoefsmit kernel carries mpc with ~0 imaginary noise at real q;
        # the archimedean observable is the real part (Im(q₀)=0).
        Ba = mp.re(E0 * (_per_block_arch(Z, N, False)
                         - _per_block_arch(Z, N, True)))
        bar_free, g_f = _per_block_bar(Z, N, False)
        bar_atom, g_a = _per_block_bar(Z, N, True)
        Bb = mp.re(E0 * (bar_free - bar_atom))
        ea = (Ba - AME_B[name]) / AME_B[name]
        eb = (Bb - AME_B[name]) / AME_B[name]
        results[name] = {
            "B_arch_MeV": float(Ba), "B_bar_MeV": float(Bb),
            "AME_MeV": float(AME_B[name]),
            "err_arch": float(ea), "err_bar": float(eb),
            "growth_channels_free": g_f, "growth_channels_atom": g_a,
        }
        print(f"{name:<5}{float(Ba):<10.4f}{float(Bb):<10.4f}"
              f"{float(AME_B[name]):<9.4f}{float(ea)*100:<+11.1f}"
              f"{float(eb)*100:<+11.1f}{g_f}/{g_a}")

    wb = WitnessBuilder("derive-binding-bar-pairing", engine="mpmath")
    wb.set_description(
        "DERIVATION (0 fit): per-block binding via the Hecke BAR-pairing "
        "‖χ^λ‖_bar = √(χ^λ(q₀)·χ^λ(q₀⁻¹)) (bar-involution q↦q⁻¹; "
        "non-archimedean, defined over any base ring) vs the archimedean "
        "per-block |χ^λ(q₀)|. y_λ Wenzl (bar-symmetrized), χ^λ Hoefsmit at "
        "q₀ and q₀⁻¹. E_0=m_e/(q₀(q₀−1)) calibration. Light isotopes D, T; "
        "AME comparison only. Growth-channel tally records λ with χ(q₀)·"
        "χ(q₀⁻¹) < 0 (imaginary bar-length — q-Reeb arccosh channels)."
    )
    wb.add_parameter("E0_MeV", float(E0))
    wb.add_parameter("q0", float(q0))
    wb.add_parameter("q0_inv", float(qi))
    wb.add_parameter("dps", DPS)            # actual compute precision used
    wb.add_data("per_atom", results)
    # Honest finding: the per-block bar-LENGTH underbinds; the archimedean
    # observation must stay |χ(q₀)|. The assertion records that the
    # archimedean per-block beats the bar-length at the real anchor (NOT a
    # claim that the bar improves binding — it does not).
    arch_better = all(
        abs(results[k]["err_arch"]) < abs(results[k]["err_bar"]) for k in results
    )
    wb.add_assertion(
        name="archimedean_per_block_beats_bar_length_at_q0",
        computed=str(int(arch_better)), expected="1", tolerance=0,
        source=("At the substrate anchor q₀ the archimedean per-block "
                "Σ y_λ|χ(q₀)| lands closer to AME than the bar-length "
                "Σ y_λ√(χ(q₀)·χ(q₀⁻¹)) for every tested isotope (D: +3.6% vs "
                "−70.3%). The bar is the correct CATEGORICAL/fibre norm "
                "(per #1738) but its archimedean realization is |χ(q₀)|, not "
                "the mirror pairing — the growth channels (χ(q₀)·χ(q₀⁻¹)<0, "
                "imaginary bar-length) are the obstruction. Recorded so the "
                "observation step is not naively bar-ified."),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
