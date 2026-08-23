#!/usr/bin/env python3
# polynomial_q_not_applicable: per-generator volumes are numerical
# scalars at q = q_0, not symbolic-in-q polynomials.
"""MPFR-native per-generator Wedderburn volumes for the atom braid.

Per [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)
lines 162–183, the brane-tower terms T2 and T3 in the unified mass
formula require per-generator additive Wedderburn volumes
$\\hat V_i^{\\text{full}}$ for $i = 0, \\ldots, n_{\\text{gens}} - 1$
of the atom braid word $T_w \\in H_{n_{\\text{strands}}}(R, q_0)$:

  T2  = Σ_i Φ_q(|V̂_i|)
  T3  = z² · Σ_{i<j} Φ_q(|V̂_i · V̂_j|)

These feed `mass_formula_6term_mpfr_50dps.py` (which requires
50-dps strings via `_load_mpfr_native_volumes`).

**Coverage.** This script generates the witness for **A = 1, 2, 3**:
proton (Z=1, N=0), neutron (Z=0, N=1), deuteron (Z=1, N=1),
tritium (Z=1, N=2), helium-3 (Z=2, N=1). PR #671's "Story B
forced m_p chain closure gap analysis" identified Item A as the
A=1 KeyError in `mass_formula_6term_mpfr_50dps.py:181-185`; this
script lifts that gate by including A=1 in the coverage set.

**Precision contract.** The accumulators (a, b, sp, ap) and all
substrate constants (q_0, q_inv, h = q - q^{-1}, z = 1/(q^{1/2} +
q^{-1/2})) are mpmath `mpf` values at 50 decimal digits, loaded
from `q-pinning-50-digit.witness.json`. The chain walker mirrors
`hecke_core.atom_per_generator_volumes` step-for-step but with all
operations in mpmath, satisfying the 50-dps contract.

**Cross-PR context.** Per `rem:brane-tower-z-habiro`, the A=1
brane-tower terms may be **structurally zero** (Habiro
level-selection forbids single-nucleon brane lifts), in which
case T2+T3 → 0 at the proton. Either outcome from this probe is
informative: a non-zero T2+T3 closes the m_p chain Item A
numerically; a zero T2+T3 confirms the missing mass must come
from Items B/C (T5/T6) per Story B.

Output: `terms-2-3-atom-per-gen-mpfr-50dps.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path
from typing import Iterable

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


# ── Atom coverage (PR #671 Item A lifts the A=1 gate) ────────────
ATOMS = [
    ("proton",   1, 0),
    ("neutron",  0, 1),
    ("deuteron", 1, 1),
    ("tritium",  1, 2),
    ("helium3",  2, 1),
]


def _load_q0_50dps(pin: str = "experimental",
                   ) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    """Read q_0, q_inv, h, z at 50 dps for the requested substrate layer.

    `pin` names WHICH q_0 -- the two are 11.5 ppb apart and are not
    interchangeable (AGENTS.md §"q0 anchor convention"):

      "experimental" (DEFAULT)  proton pin, `q_parameter.Q_50_DIGIT_STR`,
                                q0 = 1.1099785827513808...  The standing
                                2026-08-07 owner directive: all new and
                                touched compute defaults here.
      "ideal"                   muon pin, read from
                                `q-pinning-50-digit.witness.json`,
                                q0 = 1.1099785955573347...  The canonical
                                3-CAL derivation layer; keep it only where
                                an existing muon-canonical witness depends
                                on it.

    This took no argument and always returned the MUON value, which made
    the function a silent layer boundary: `atom_per_generator_volumes_mpfr`
    is documented as a "50-dps mpmath analog of
    `hecke_core.atom_per_generator_volumes`", but `hecke_core` (really
    `pyhecke.atom`) evaluates at the PROTON pin. Measured, that alone put
    the two "analogous" implementations 9.44e-08 apart on a single nucleon
    -- eight orders above the float64 floor, and nothing to do with
    precision. Re-pointed at the proton pin they agree to 3.67e-16.

    Say which layer you are on; never mix two in one quantity.
    """
    if pin == "experimental":
        from q_parameter import Q_50_DIGIT_STR
        q0 = mp.mpf(Q_50_DIGIT_STR)
    elif pin == "ideal":
        path = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
        with path.open() as fh:
            d = json.load(fh)
        q0 = mp.mpf(d["derived_50_digit"]["q"])
    else:
        raise ValueError(
            f"pin must be 'experimental' or 'ideal', got {pin!r}")
    qi = 1 / q0
    h = q0 - qi
    z = q0**3 / (q0**2 + 1)
    return q0, qi, h, z


def _nucleon_gen_chains_mpfr(
    quarks: list[str], h: mp.mpf,
) -> tuple[list[tuple[mp.mpf, mp.mpf]], list[tuple[mp.mpf, mp.mpf]]]:
    """Per-generator (c, d) chains for one nucleon at 50 dps.

    Mirrors `hecke_core.nucleon_gen_chains` but with mpmath h.
    """
    one = mp.mpf(1)
    zero = mp.mpf(0)
    minus_h = -h
    minus_h_half = -h / 2

    # B₃ confinement: (σ₀ · σ₁⁻¹)^3
    g0: list[tuple[mp.mpf, mp.mpf]] = [(one, zero)] * 3
    g1: list[tuple[mp.mpf, mp.mpf]] = [(one, minus_h)] * 3

    # Quark pairwise crossings: (qi, qj, gen)
    pairs = [(0, 1, 0), (0, 2, 0), (1, 2, 1)]
    for i, j, gen in pairs:
        qi_f, qj_f = quarks[i], quarks[j]
        if qi_f == qj_f == "u":
            cd = (one, zero)        # σ
        elif qi_f == qj_f == "d":
            cd = (one, minus_h)     # σ⁻¹
        else:
            cd = (one, minus_h_half)  # mixed
        if gen == 0:
            g0.append(cd)
        else:
            g1.append(cd)

    # Gluon self-coupling: 2 σ₀ per nucleon
    g0.extend([(one, zero)] * 2)
    return g0, g1


def _intra_chains_mpfr(
    nuc: str, h: mp.mpf,
) -> tuple[list[tuple[mp.mpf, mp.mpf]], list[tuple[mp.mpf, mp.mpf]]]:
    if nuc == "p":
        return _nucleon_gen_chains_mpfr(["u", "u", "d"], h)
    elif nuc == "n":
        return _nucleon_gen_chains_mpfr(["u", "d", "d"], h)
    else:
        raise ValueError(f"unknown nucleon {nuc!r}")


def _inter_cross_mpfr(
    nuc: str, next_nuc: str, h: mp.mpf,
) -> tuple[mp.mpf, mp.mpf]:
    one = mp.mpf(1)
    if nuc == "p" and next_nuc == "p":
        return (one, mp.mpf(0))        # pp: σ
    elif nuc == "n" and next_nuc == "n":
        return (one, -h)               # nn: σ⁻¹
    else:
        # colour-WEIGHTED p-n interface (qou-gdtb): -h(1/2 - delta/4).
        # -h/2 here was the colour-blind value and dropped the p/n
        # asymmetry that bring_color_weighted supplies.
        from canonical_braid_crossings import _avg_color_delta
        return (one, -h * (1 - _avg_color_delta() / 2) / 2)


def atom_per_generator_volumes_mpfr(
    Z: int, N: int,
    *,
    include_inter: bool = True,
    crossings_per_pair: int = 1,
    m_pp: int | None = None,
    m_pn: int | None = None,
    m_nn: int | None = None,
    pin: str = "experimental",
) -> list[dict[str, mp.mpf]]:
    """50-dps mpmath analog of `hecke_core.atom_per_generator_volumes`.

    Walks the atom braid step-for-step in mpmath, returning per-
    generator dicts ``{std, sym, alt, full}`` of `mpf` values.

    `pin` selects the substrate layer; see `_load_q0_50dps`. Defaults to
    the proton/experimental pin, which is what `hecke_core` uses, so the
    two agree to 3.67e-16 on a single nucleon out of the box.

    HOW THIS DIFFERS FROM `hecke_core` (read before treating it as a
    drop-in). At the proton pin the two still disagree by **2.11e-04** on
    any atom carrying a p-n boundary, and that gap is NOT precision: this
    implementation uses the canonical colour-WEIGHTED interface
    `d = -h(1/2 - δ/4)` (`averaged_weighted`, canonical per AGENTS.md R3),
    while `hecke_core` uses the colour-BLIND `-h/2`. Neither
    implementation is canonical on both axes today -- `hecke_core` has the
    pin right and the interface wrong; this one had the interface right
    and the pin wrong until the `pin` parameter above. Bean `qou-cds4`.
    """
    q0, qi, h, z_mark = _load_q0_50dps(pin)
    A = Z + N
    if A < 1:
        return []

    ordering = ["p"] * Z + ["n"] * N

    if include_inter:
        n_strands = 3 * A
        n_gens_total = n_strands - 1  # 3A − 1
    else:
        n_gens_total = 2 * A

    one = mp.mpf(1)
    zero = mp.mpf(0)
    a_arr = [zero] * n_gens_total
    b_arr = [one]  * n_gens_total
    sp_arr = [one] * n_gens_total
    ap_arr = [one] * n_gens_total

    for k, nuc in enumerate(ordering):
        intra, intra_g1 = _intra_chains_mpfr(nuc, h)
        if include_inter:
            base_g0 = 3 * k
            base_g1 = 3 * k + 1
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

        # Inter-nucleon crossings
        if include_inter and k < A - 1:
            i = 3 * k + 2
            next_nuc = ordering[k + 1]
            base_cross = _inter_cross_mpfr(nuc, next_nuc, h)
            if nuc == "p" and next_nuc == "p":
                m_this = m_pp if m_pp is not None else crossings_per_pair
            elif nuc == "n" and next_nuc == "n":
                m_this = m_nn if m_nn is not None else crossings_per_pair
            else:
                m_this = m_pn if m_pn is not None else crossings_per_pair
            for _ in range(m_this):
                c, d = base_cross
                a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
                b_new = a_arr[i] * c + b_arr[i] * d
                a_arr[i] = a_new
                b_arr[i] = b_new
                sp_arr[i] *= c * q0 + d
                ap_arr[i] *= -c * qi + d

    # Per-generator V̂_full from accumulators (same H_3 Wedderburn
    # weights as `hecke_core.atom_per_generator_volumes`).
    # Normalization recipe (mirrors the f64 sibling):
    #   nf3 = [1]_q · [2]_q · [3]_q with [n]_q = (q^n − q^{-n})/(q − q^{-1})
    #   w_sym = 1/nf3, w_std = [2]_q²/nf3, w_alt = 1/nf3
    #   then normalize so w_sym + w_std + w_alt = 1
    def qint(n: int) -> mp.mpf:
        return (q0 ** n - qi ** n) / (q0 - qi)

    nf3_val = qint(1) * qint(2) * qint(3)
    w_sym = mp.mpf(1) / nf3_val
    w_std = qint(2) ** 2 / nf3_val
    w_alt = mp.mpf(1) / nf3_val
    wt = w_sym + w_std + w_alt
    w_sym /= wt
    w_std /= wt
    w_alt /= wt

    vols: list[dict[str, mp.mpf]] = []
    for i in range(n_gens_total):
        Vs = z_mark * a_arr[i] + b_arr[i]
        Vf = w_sym * sp_arr[i] + w_std * Vs + w_alt * ap_arr[i]
        vols.append({
            "std": Vs,
            "sym": sp_arr[i],
            "alt": ap_arr[i],
            "full": Vf,
        })
    return vols


def _stringify(vols: Iterable[dict[str, mp.mpf]]) -> list[dict[str, str]]:
    """Convert mpf values to full-precision decimal strings for JSON."""
    out: list[dict[str, str]] = []
    for entry in vols:
        out.append({k: mp.nstr(v, 50, strip_zeros=False) for k, v in entry.items()})
    return out


def main() -> int:
    start_time = time.monotonic()
    # This producer's committed witness is muon-canonical and is one of the
    # ~870 tracked by the `qou-1c4y` migration, which needs scoped sign-off.
    # Naming the pin explicitly keeps that witness byte-stable while the
    # DEFAULT for every new caller is the proton pin per the standing
    # directive. Do not drop the argument to "tidy up" -- that would flip a
    # committed witness as a side effect.
    q0, qi, h, z_mark = _load_q0_50dps("ideal")
    print("=" * 78)
    print("MPFR-NATIVE PER-GENERATOR WEDDERBURN VOLUMES (50 dps)")
    print("=" * 78)
    print(f"q_0    = {mp.nstr(q0, 14)}")
    print(f"q_inv  = {mp.nstr(qi, 14)}")
    print(f"h      = {mp.nstr(h, 14)}")
    print(f"z_mark = {mp.nstr(z_mark, 14)}")
    print()

    results: list[dict[str, object]] = []
    for label, Z, N in ATOMS:
        A = Z + N
        n_strands = 3 * A
        n_gens = n_strands - 1
        vols = atom_per_generator_volumes_mpfr(Z, N, include_inter=True,
                                               pin="ideal")
        print(f"  {label:>9} (Z={Z}, N={N}, A={A}, n_gens={n_gens}):")
        for i, entry in enumerate(vols):
            mag = abs(entry["full"])
            print(f"    gen {i}: |V_full| = {mp.nstr(mag, 8)}")
        results.append({
            "atom": label,
            "Z": Z,
            "N": N,
            "A": A,
            "n_strands": n_strands,
            "n_generators": n_gens,
            "wedderburn_vols": _stringify(vols),
        })
        print()

    builder = WitnessBuilder.wrap_legacy(
        "terms-2-3-atom-per-gen-mpfr-50dps",
        {
            "description": (
                "MPFR-native per-generator additive Wedderburn volumes "
                "V̂_i^full at 50 dps for the atom braid at A = 1, 2, 3 "
                "(proton, neutron, deuteron, tritium, helium-3). Feeds "
                "mass_formula_6term_mpfr_50dps.term_23_brane_tower_mp "
                "as the source of T2 and T3 per-generator volumes. PR "
                "#671 Item A: this witness now covers A=1 (was missing); "
                "either the proton T2+T3 yields a non-zero brane-tower "
                "contribution (closes m_p chain Items A/B/C analytically) "
                "or returns ~0 (confirms brane-tower-z-habiro level-"
                "selection structurally forbids A=1, per Story B)."
            ),
            "parameters": {
                "q_0_50dps": mp.nstr(q0, 50, strip_zeros=False),
                "q_inv_50dps": mp.nstr(qi, 50, strip_zeros=False),
                "h_50dps": mp.nstr(h, 50, strip_zeros=False),
                "z_markov_50dps": mp.nstr(z_mark, 50, strip_zeros=False),
                "atoms_covered": [a[0] for a in ATOMS],
                "precision_dps": 50,
            },
            "results": results,
        },
        script_path=__file__,
        engine="mpmath",
        start_time=start_time,
    )
    out = builder.save()
    print(f"  Witness: {Path(out).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
