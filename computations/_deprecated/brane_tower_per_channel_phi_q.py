#!/usr/bin/env python3
"""
T2/T3 brane-tower with per-Wedderburn-channel Φ_q evaluation.

Per the gist framework
(https://gist.github.com/litlfred/b3459bf9143dd03234a9fc55c370f6f4):
"Φ_q resums an infinite series of Markov traces", weighted by
Plancherel measures.  Concretely, for a single Hecke generator
$\sigma_i$ with eigenvalues $\{q, -q^{-1}\}$ in the standard rep:

    \mathrm{tr}_M(\sigma_i^n) = y_{\mathrm{sym}}\cdot q^n
                              + y_{\mathrm{alt}}\cdot(-q^{-1})^n
                              + y_{\mathrm{std}}\cdot \chi^{\mathrm{std}}(\sigma_i^n)

so the Plancherel-weighted resummation

    \sum_n c_n \cdot \mathrm{tr}_M(\sigma_i^n)
        = y_{\mathrm{sym}}\Phi_q(q) + y_{\mathrm{alt}}\Phi_q(-q^{-1}) + \dots

applies $\Phi_q$ to each Wedderburn-channel eigenvalue separately,
then sums with $y_\lambda$ weights.  Each per-channel $\Phi_q$ is a
number (basis-independent), and the $y_\lambda$ sum is a Markov-
invariant trace.  Contrast with the literal $\Phi_q(|\hat
V_i^{\mathrm{full}}|)$ in `paper_six_term_isotope_sweep.py`, which
applies $\Phi_q$ to the $W_\lambda$-weighted **sum** of channels —
that's a basis-dependent evaluation, not a trace.

This script:

  1. For each per-generator chain (proton, neutron, atom (Z, N)),
     compute the Wedderburn-channel volumes $\hat V_{\mathrm{sym}}$,
     $\hat V_{\mathrm{std}}$, $\hat V_{\mathrm{alt}}$ using the
     existing `atom_per_generator_volumes` infrastructure.

  2. Compute T2 in the per-channel trace form:
         T2 = $\sum_i \big[ y_{\mathrm{sym}}\Phi_q(|\hat V_{\mathrm{sym},i}|)
                          + y_{\mathrm{std}}\Phi_q(|\hat V_{\mathrm{std},i}|)
                          + y_{\mathrm{alt}}\Phi_q(|\hat V_{\mathrm{alt},i}|) \big]$
     where $y_\lambda$ are the H_3 Wedderburn weights at $q_0$
     (the same weights `atom_per_generator_volumes` uses to build
     $\hat V_{\mathrm{full}}$).

  3. Compare to the legacy literal-Φ_q form
         T2_legacy = $\sum_i \Phi_q(|\hat V_{\mathrm{full},i}|)$.

  4. Test isospin: with the per-channel form, do mirror nuclei
     T (1p+2n) and ³He (2p+1n) give equal T2's?

If yes, the per-channel reformulation IS the fix for the −737 MeV
isospin pathology.

Output: brane-tower-per-channel-phi-q-probe.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP  # noqa: E402
from hecke_core import (  # noqa: E402
    h as h_val, z as z_mark, W_SYM, W_STD, W_ALT,
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from mass_endomorphism import Phi_q  # noqa: E402

Q0 = Q_MP
QI = Q_INV_MP
H_VAL = mp.mpf(str(float(h_val)))
Z_MARK = mp.mpf(str(float(z_mark)))


def channel_volumes(chain) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Compute (|V̂_sym|, |V̂_std|, |V̂_alt|) for one generator's chain.

    Replays `atom_per_generator_volumes`'s additive Wedderburn loop
    but exposes the three channels separately instead of returning the
    `W`-weighted sum.
    """
    a, b = mp.mpf(0), mp.mpf(1)
    sp, ap = mp.mpf(1), mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        a, b = a * cm * H_VAL + a * dm + b * cm, a * cm + b * dm
        sp = sp * (cm * Q0 + dm)
        ap = ap * (-cm * QI + dm)
    V_std = Z_MARK * a + b
    return abs(sp), abs(V_std), abs(ap)


def atom_per_gen_chains(Z: int, N: int, include_inter: bool = True):
    """Per-generator (c, d) chains for atom (Z, N).  Same structure as
    `atom_per_generator_volumes` but yielding raw chains.
    """
    A = Z + N
    if A < 1:
        return []
    ordering = ['p'] * Z + ['n'] * N

    n_gens_total = (3 * A - 1) if include_inter else (2 * A)
    chains = [[] for _ in range(n_gens_total)]

    for k, nuc in enumerate(ordering):
        intra_g0 = _PROTON_G0 if nuc == 'p' else _NEUTRON_G0
        intra_g1 = _PROTON_G1 if nuc == 'p' else _NEUTRON_G1
        if include_inter:
            base_g0 = 3 * k
            base_g1 = 3 * k + 1
        else:
            base_g0 = 2 * k
            base_g1 = 2 * k + 1
        chains[base_g0].extend([(float(c), float(d)) for c, d in intra_g0])
        chains[base_g1].extend([(float(c), float(d)) for c, d in intra_g1])

    if include_inter:
        for k in range(A - 1):
            inter_pos = 3 * k + 2
            pair = (ordering[k], ordering[k + 1])
            if pair == ('p', 'p'):
                chains[inter_pos].append((1.0, 0.0))
            elif pair == ('n', 'n'):
                chains[inter_pos].append((1.0, -float(H_VAL)))
            else:
                chains[inter_pos].append((1.0, -float(H_VAL) / 2))

    return chains


def T2_per_channel(chains) -> mp.mpf:
    """T2 = Σ_i [W_SYM·Φ_q(|V̂_sym|) + W_STD·Φ_q(|V̂_std|) + W_ALT·Φ_q(|V̂_alt|)].

    Each Φ_q is applied to a Wedderburn-channel eigenvalue (a number,
    basis-independent), then summed with the Markov weights y_λ = W_λ.
    The result is a Markov-invariant trace.
    """
    w_sym = mp.mpf(str(W_SYM))
    w_std = mp.mpf(str(W_STD))
    w_alt = mp.mpf(str(W_ALT))
    total = mp.mpf(0)
    for ch in chains:
        if not ch:
            continue
        v_sym, v_std, v_alt = channel_volumes(ch)
        for w, v in [(w_sym, v_sym), (w_std, v_std), (w_alt, v_alt)]:
            try:
                phi = Phi_q(v)
                if not mp.isinf(phi) and not mp.isnan(phi):
                    total += w * phi
            except Exception:
                pass
    return total


def T2_legacy_full(chains) -> mp.mpf:
    """Legacy T2 = Σ_i Φ_q(|W_SYM·V̂_sym + W_STD·V̂_std + W_ALT·V̂_alt|).

    Applies Φ_q to the W-weighted sum (basis-dependent) — the form
    currently in paper_six_term_isotope_sweep.py.
    """
    w_sym = mp.mpf(str(W_SYM))
    w_std = mp.mpf(str(W_STD))
    w_alt = mp.mpf(str(W_ALT))
    total = mp.mpf(0)
    for ch in chains:
        if not ch:
            continue
        a, b = mp.mpf(0), mp.mpf(1)
        sp, ap = mp.mpf(1), mp.mpf(1)
        for c, d in ch:
            cm, dm = mp.mpf(c), mp.mpf(d)
            a, b = a * cm * H_VAL + a * dm + b * cm, a * cm + b * dm
            sp = sp * (cm * Q0 + dm)
            ap = ap * (-cm * QI + dm)
        V_std = Z_MARK * a + b
        V_full = w_sym * sp + w_std * V_std + w_alt * ap
        try:
            phi = Phi_q(abs(V_full))
            if not mp.isinf(phi) and not mp.isnan(phi):
                total += phi
        except Exception:
            pass
    return total


def main() -> int:
    print("=" * 90)
    print("  T2 brane-tower — per-channel Φ_q (trace form) vs literal Φ_q (legacy)")
    print(f"  q_0 = {float(Q0):.10f}")
    print(f"  Wedderburn weights: W_SYM = {float(W_SYM):.6f},  "
          f"W_STD = {float(W_STD):.6f},  W_ALT = {float(W_ALT):.6f}")
    print("=" * 90)

    atoms = [
        ("p", 1, 0, False),
        ("n", 0, 1, False),
        ("D", 1, 1, True),
        ("T", 1, 2, True),
        ("3He", 2, 1, True),
        ("4He", 2, 2, True),
    ]

    print(f"\n  {'iso':<5} {'A':>3}  {'T2_per_channel':>18}  "
          f"{'T2_legacy_full':>18}  {'ratio':>10}")
    print("  " + "-" * 70)
    rows = []
    for iso, Z, N, inter in atoms:
        chains = atom_per_gen_chains(Z, N, include_inter=inter)
        T2_pc = T2_per_channel(chains)
        T2_lg = T2_legacy_full(chains)
        ratio = float(T2_pc / T2_lg) if T2_lg != 0 else float("nan")
        print(f"  {iso:<5} {Z + N:>3}  {float(T2_pc):>+18.4e}  "
              f"{float(T2_lg):>+18.4e}  {ratio:>10.6f}")
        rows.append({
            "iso": iso, "Z": Z, "N": N, "A": Z + N,
            "T2_per_channel": float(T2_pc),
            "T2_legacy_full": float(T2_lg),
            "ratio": ratio,
        })

    # Isospin check (T vs ³He)
    rT = next(r for r in rows if r["iso"] == "T")
    r3 = next(r for r in rows if r["iso"] == "3He")
    print("\n  Isospin (T vs ³He):")
    print(f"  {'form':<22}  {'T':>14}  {'³He':>14}  {'ΔT2':>14}  {'×E_0 (MeV)':>14}")
    print("  " + "-" * 80)
    E_0 = 7.95e-4  # rough (proton calibration from paper_six_term_isotope_sweep)
    for form, key in [("per-channel (trace)", "T2_per_channel"),
                       ("legacy full (literal)", "T2_legacy_full")]:
        delta = r3[key] - rT[key]
        print(f"  {form:<22}  {rT[key]:>+14.4e}  {r3[key]:>+14.4e}  "
              f"{delta:>+14.4e}  {delta * E_0:>+14.4f}")

    print(f"\n  CODATA T - ³He = +0.019 MeV  (Coulomb + m_n - m_p)")
    print(f"  Legacy T2 alone contributes ~+465 MeV to (³He - T) — see PR #524 diagnosis.")

    # Verdict
    delta_pc = (rT["T2_per_channel"] - r3["T2_per_channel"]) * E_0
    delta_lg = (rT["T2_legacy_full"] - r3["T2_legacy_full"]) * E_0
    print("\n  Verdict:")
    print(f"    Legacy form contribution to T - ³He prediction: {delta_lg:+.2f} MeV")
    print(f"    Per-channel form contribution:                  {delta_pc:+.2f} MeV")
    if abs(delta_pc) < 10:
        print(f"    ✓ Per-channel form recovers isospin within 10 MeV")
    elif abs(delta_pc) < abs(delta_lg) / 5:
        print(f"    ✓ Per-channel form reduces isospin violation by 5× or more")
    else:
        print(f"    ✗ Per-channel form does not resolve isospin pathology;")
        print(f"      structural fix needs more than per-channel Φ_q application.")

    witness = {
        "computation": "brane-tower-per-channel-phi-q-probe",
        "description": (
            "Tests whether applying Phi_q per Wedderburn channel (sym/std/alt) "
            "and summing with Markov weights y_lambda restores trace-invariance "
            "to the T2 brane-tower.  Compares to the legacy literal "
            "Phi_q(|V_full|) form that currently produces the -737 MeV T-3He "
            "isospin pathology in paper_six_term_isotope_sweep.py."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "rows": rows,
        "isospin_T_minus_3He_per_channel_MeV": delta_pc,
        "isospin_T_minus_3He_legacy_MeV": delta_lg,
        "codata_T_minus_3He_MeV": 0.019,
    }
    out = HERE / "brane-tower-per-channel-phi-q-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
