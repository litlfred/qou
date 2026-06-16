#!/usr/bin/env python3
"""
MASS ENDOMORPHISM: proton-electron mass ratio from Li_2^q tower.

    𝔪(β) = |∏ V̂_i| + Σ_i Li_2^q(|V̂_i|) + Σ_{i<j} z² · Li_2^q(|V̂_i V̂_j|)

where Li_2^q(z) = ∏_{k≥1} (1 - q⁻ᵏz)⁻¹ is the Rogers quantum
dilogarithm (per canonical cheat-sheet: Li_2^q for binding context,
Φ_q for convergence/analytic continuation).  The pair weight z² = tr_M(σ_i σ_j) holds
for every pair i<j by the Markov-trace factorization theorem
(thm:markov-trace-factorization): adjacent pairs reduce via the
Hecke braid relation + one Markov-property peel; non-adjacent
pairs far-commute so σ_j is rightmost, and two successive
Markov-property peels each contribute a factor z.  The earlier
adjacent-only form (prop:mass-endomorphism-tower) empirically
undercounts blow-up centres for A ≥ 3 atoms; see
adjacent-vs-full-probe.witness.json.

Electron (trefoil σ₁³, 2 strands, 1 generator):
  V̂_e ≈ 0.594, Φ_q ≈ 630.  No cross-term.

Proton (B₃ × uud + 2 gluon, 3 strands, 2 generators):
  V̂₀ ≈ 0.989, V̂₁ ≈ 0.971.
  11 crossings from 4-channel γγ→qq̄ production.
  Cross-term z² · Φ_q(V̂₀V̂₁) ≈ 82,000  (one pair for n = 2).

Result: m_p/m_e ≈ 1870 (CODATA: 1836, error 1.8%).
Zero fitted parameters.  Inputs: q₀ and m_e only.

Usage:
    python3 computations/mass_endomorphism.py
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as HA_val
from witness_base import WitnessBuilder

Q0 = q0  # alias for mass_from_tower
HA = HA_val
z_mark = 1.0 / (q0**0.5 + qi0**0.5)
hbar_q = (q0 - 1) / q0

def qint(k):
    return (q0**k - qi0**k) / (q0 - qi0) if k else 0.0

def qfact(n):
    r = 1.0
    for k in range(1, n + 1):
        r *= qint(k)
    return r

def qdim(part, n):
    hooks = []
    for i, rl in enumerate(part):
        for j in range(rl):
            arm = rl - j - 1
            leg = sum(1 for r2 in range(i + 1, len(part)) if part[r2] > j)
            hooks.append(arm + leg + 1)
    num = qfact(n)
    den = 1.0
    for h in hooks:
        den *= qint(h)
    return num / den if abs(den) > 1e-30 else 0

# Wedderburn weights at baryon level n=3
nf3 = qfact(3)
w_sym = qdim((3,), 3) ** 2 / nf3
w_std = qdim((2, 1), 3) ** 2 / nf3
w_alt = qdim((1, 1, 1), 3) ** 2 / nf3
wt = w_sym + w_std + w_alt
w_sym /= wt
w_std /= wt
w_alt /= wt


@lru_cache(maxsize=4096)
def Phi_q(z_val, max_k=2000):
    """Non-perturbative quantum dilogarithm Φ_q(z) = ∏ (1-q⁻ᵏz)⁻¹."""
    if abs(z_val) >= q0:
        return float("inf")
    product = 1.0
    qi_pow = qi0
    for _ in range(max_k):
        term = qi_pow * z_val
        factor = 1.0 - term
        if abs(factor) < 1e-300:
            return float("inf")
        product /= factor
        if abs(term) < 1e-15:
            break
        qi_pow *= qi0
    return product


def additive_wedderburn_volumes(n_strands, crossings_per_gen):
    """Compute V̂_full per generator using additive Wedderburn."""
    vols = []
    for gen in range(n_strands - 1):
        a, b = 0.0, 1.0
        sp, ap = 1.0, 1.0
        for c, d in crossings_per_gen.get(gen, []):
            a, b = a * c * HA + a * d + b * c, a * c + b * d
            sp *= c * q0 + d
            ap *= -c * qi0 + d
        Vs = z_mark * a + b
        Vf = w_sym * sp + w_std * Vs + w_alt * ap
        vols.append({"std": Vs, "sym": sp, "alt": ap, "full": Vf})
    return vols


def mass_from_tower(vols):
    """𝔪 = |Π V̂_full| + Σ Φ_q(|V̂_full|) + Σ_{i<j} z² Φ_q(|V̂_i V̂_j|).

    The three terms correspond to:
    1. Descended (base-level Markov trace product).
    2. Single-generator blow-up centres (weight 1 per generator).
    3. Pair blow-up centres over all distinct generator pairs (i, j),
       weighted by z² = tr_M(σ_i σ_j).

    The cross-term weight z² is the Markov trace of σ_i σ_j,
    z² = tr_M(σ_i σ_j), by the Markov-trace factorization theorem
    (thm:markov-trace-factorization).  For adjacent pairs (|i−j|=1)
    the Hecke braid relation reduces the pair and one Markov-peel
    applies; for non-adjacent pairs (|i−j|≥2) far-commutativity
    makes σ_j rightmost and two successive Markov-peels each
    contribute a factor z.  The earlier adjacent-only restriction
    (prop:mass-endomorphism-tower) was empirically refuted by the
    adjacent-vs-full-probe witness: including non-adjacent pairs
    closes the 2–3% heavy-atom bias (A ≥ 6) and is required for
    consistency with the Wedderburn blow-up count of the brane
    tower.
    """
    n = len(vols)
    z_mark = 1.0 / (Q0 ** 0.5 + (1.0 / Q0) ** 0.5)

    desc = 1.0
    for v in vols:
        desc *= v["full"]
    desc = abs(desc)

    single = sum(Phi_q(v["full"]) for v in vols)

    cross = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            cross += z_mark ** 2 * Phi_q(
                abs(vols[i]["full"] * vols[j]["full"])
            )

    return desc, single, cross, desc + single + cross


# === PARTICLES ===

# Electron = trefoil σ₁³ on 2 strands
electron_cross = {0: [(1.0, 0.0)] * 3}

# Proton = B₃ × uud × gluon on 3 strands (4-channel budget)
# Channel 3 (σ₃, confinement): 3σ₀ + 3σ₁⁻¹
# Channel 2 (σ₂, color pairing): 1σ₀(uu) + 1½(ud, gen 0) + 1½(ud, gen 1)
# Channel 1 (σ₁, gluon): 2σ₀ (dim(adj SU(3))−2dim(fund) = 8−6 = 2)
proton_cross = {
    0: [(1.0, 0.0)] * 3          # B₃: 3 × σ₀
       + [(1.0, 0.0)]            # uu quark pair
       + [(1.0, -HA / 2)]        # ud quark pair
       + [(1.0, 0.0)] * 2,       # 2 gluon self-coupling modes
    1: [(1.0, -HA)] * 3          # B₃: 3 × σ₁⁻¹
       + [(1.0, -HA / 2)],       # ud quark pair
}

# Neutron = B₃ × udd × gluon on 3 strands (4-channel budget)
# Same B₃ + gluon structure, but udd quark content:
#   dd pair: σ⁻¹ (instead of uu: σ)
#   ud pairs: same ½(σ + σ⁻¹) as proton
neutron_cross = {
    0: [(1.0, 0.0)] * 3          # B₃: 3 × σ₀
       + [(1.0, -HA)]            # dd quark pair (σ⁻¹)
       + [(1.0, -HA / 2)]        # ud quark pair
       + [(1.0, 0.0)] * 2,       # 2 gluon self-coupling modes
    1: [(1.0, -HA)] * 3          # B₃: 3 × σ₁⁻¹
       + [(1.0, -HA / 2)],       # ud quark pair
}

# The heavy per-particle tower + print + WitnessBuilder below is demo
# output for `python mass_endomorphism.py`. Guarding under __main__
# so that importing this module (e.g. from sigma_shell_characterization,
# multi_level_sdp, misdp_cross_channel, pyhecke.sdp, crt_markov,
# tower_binding_symbolic, or any of the 30+ other scripts that do
# `from mass_endomorphism import proton_cross, Phi_q, …`) does NOT
# trigger the 30+ second recomputation or overwrite
# mass-endomorphism.witness.json as a side effect.


# === Atomic Markov-trace via recursive ascent (#508) ===

def tr_M_atomic_at_q0(Z: int, N: int) -> float:
    """Canonical Jones–Markov trace `tr_M(β_atom)` evaluated at q = q₀.

    Builds the production atomic braid `β_atom` for atom (Z, N) via
    `mass_at_3A_proper.atom_braid_word_3A` and evaluates the canonical
    trace via the Markov-axiom recursive-ascent path
    (`markov_peel.tr_M_atomic`).

    This is the **production** atomic Markov trace — for `A ≥ 4` it
    completes in seconds–minutes, vs. the Hoefsmit per-Wedderburn-block
    sum which would take ~30 minutes per atom (see #508).

    The returned float matches `atomic-tr-m-mpfr-50dps.witness.json`
    (Hoefsmit + Wenzl bridge) to ~1e-15 at q = q₀.

    Parameters
    ----------
    Z, N : int
        Proton and neutron counts.

    Returns
    -------
    float
        `tr_M(β_atom)` at q = q₀, IEEE-double precision.
    """
    # Local import — markov_peel pulls in sympy, which we keep optional
    # for callers that only need the (c, d) crossing tables.
    from markov_peel import tr_M_atomic
    from hecke_symbolic import q as q_sym
    sym = tr_M_atomic(Z, N)
    # `subs(...).evalf(30)` evaluates symbolically at 30-digit precision
    # before truncating to IEEE double — sufficient for all downstream
    # mass computations.  `tr_M_atomic` always returns a sympy expression,
    # so no `sp.sympify` shim is needed.
    return float(sym.subs(q_sym, q0).evalf(30))


if __name__ == "__main__":

    electron_vols = additive_wedderburn_volumes(2, electron_cross)
    e_desc, e_single, e_cross, e_total = mass_from_tower(electron_vols)
    proton_vols = additive_wedderburn_volumes(3, proton_cross)
    p_desc, p_single, p_cross, p_total = mass_from_tower(proton_vols)
    neutron_vols = additive_wedderburn_volumes(3, neutron_cross)
    n_desc, n_single, n_cross, n_total = mass_from_tower(neutron_vols)

    # === OUTPUT ===

    print("MASS ENDOMORPHISM: non-perturbative Φ_q tower")
    print("=" * 60)
    print(f"q₀ = {q0}")
    print(f"Wedderburn weights: w_sym={w_sym:.4f}, w_std={w_std:.4f}, w_alt={w_alt:.4f}")
    print()
    print(f"ELECTRON (trefoil σ₁³, 1 generator):")
    for i, v in enumerate(electron_vols):
        phi = Phi_q(v["full"])
        print(f"  Gen {i}: V̂_full={v['full']:.6f}, Φ_q={phi:.4f}")
    print(f"  Descended: {e_desc:.6f}")
    print(f"  Single:    {e_single:.4f}")
    print(f"  Cross:     {e_cross:.4f}")
    print(f"  Total:     {e_total:.4f}")
    print()
    print(f"PROTON (B₃ × uud + gluon, 2 generators):")
    for i, v in enumerate(proton_vols):
        phi = Phi_q(v["full"])
        print(f"  Gen {i}: V̂_full={v['full']:.6f}, Φ_q={phi:.4f}")
    print(f"  Descended: {p_desc:.6f}")
    print(f"  Single:    {p_single:.4f}")
    print(f"  Cross:     {p_cross:.4f}  (z²·Φ_q(V₀V₁), z²={z_mark**2:.6f})")
    print(f"  Total:     {p_total:.4f}")
    print()
    print(f"NEUTRON (B₃ × udd + gluon, 2 generators):")
    for i, v in enumerate(neutron_vols):
        phi = Phi_q(v["full"])
        print(f"  Gen {i}: V̂_full={v['full']:.6f}, Φ_q={phi:.4f}")
    print(f"  Descended: {n_desc:.6f}")
    print(f"  Single:    {n_single:.4f}")
    print(f"  Cross:     {n_cross:.4f}")
    print(f"  Total:     {n_total:.4f}")
    print()
    print(f"m_p/m_e = {p_total / e_total:.4f}  (CODATA: 1836.152, error {abs(p_total/e_total - 1836.152)/1836.152*100:.2f}%)")
    print(f"m_n/m_e = {n_total / e_total:.4f}  (CODATA: 1838.684, error {abs(n_total/e_total - 1838.684)/1838.684*100:.2f}%)")
    print(f"m_n/m_p = {n_total / p_total:.6f}  (CODATA: 1.001378, error {abs(n_total/p_total - 1.001378)/1.001378*100:.4f}%)")
    print(f"m_n - m_p (units of m_e) = {(n_total - p_total)/e_total:.4f}  (CODATA: 2.531)")
    print(f"Δm (MeV) = {(n_total - p_total)/e_total * 0.51100:.4f}  (CODATA: 1.293 MeV)")

    # === Atomic Markov trace via recursive ascent (#508) ===
    print()
    print("ATOMIC tr_M(β) via Markov-axiom recursive ascent (#508):")
    print(f"{'atom':10s} {'Z':>2s} {'N':>2s} {'A':>2s}  {'tr_M(q₀)':>20s}")
    atomic_tr_m_at_q0 = {}
    for label, (Z_, N_) in [
        ("proton",   (1, 0)),
        ("neutron",  (0, 1)),
        ("deuteron", (1, 1)),
        ("tritium",  (1, 2)),
        ("helium-3", (2, 1)),
        ("helium-4", (2, 2)),
    ]:
        try:
            tr = tr_M_atomic_at_q0(Z_, N_)
            atomic_tr_m_at_q0[label] = tr
            print(f"  {label:10s} {Z_:>2d} {N_:>2d} {Z_+N_:>2d}  {tr:+.16e}")
        except Exception as exc:  # noqa: BLE001
            print(f"  {label:10s} {Z_:>2d} {N_:>2d} {Z_+N_:>2d}  FAILED: {exc!r}")

    # === WITNESS ===
    w = WitnessBuilder("mass-endomorphism", engine="python")
    w.set_description(
        "Mass endomorphism via Φ_q tower with z²-weighted cross-term. "
        f"m_p/m_e = {p_total / e_total:.4f} (CODATA: 1836.152, "
        f"error {abs(p_total / e_total - 1836.152) / 1836.152 * 100:.2f}%). "
        "Cross-term weight z² = tr_M(σ₀σ₁) derived from Hecke algebra."
    )
    w.add_parameter("q0", str(q0))
    w.add_parameter("w_sym", str(w_sym))
    w.add_parameter("w_std", str(w_std))
    w.add_parameter("w_alt", str(w_alt))
    w.add_parameter("z_markov", str(z_mark))
    w.add_parameter("z_squared", str(z_mark**2))
    w.add_data(
        "electron",
        {
            "vols": [{"std": v["std"], "full": v["full"]} for v in electron_vols],
            "n_generators": 1,
            "descended": e_desc,
            "single": e_single,
            "cross": e_cross,
            "total": e_total,
        },
    )
    w.add_data(
        "proton",
        {
            "vols": [{"std": v["std"], "full": v["full"]} for v in proton_vols],
            "n_generators": 2,
            "crossings": "3σ(B₃)+1σ(uu)+1½(ud)+2σ(gluon) | 3σ⁻¹(B₃)+1½(ud)",
            "descended": p_desc,
            "single": p_single,
            "cross": p_cross,
            "total": p_total,
        },
    )
    w.add_data("ratio", p_total / e_total)
    w.add_data("codata", 1836.152)
    w.add_data("error_pct", abs(p_total / e_total - 1836.152) / 1836.152 * 100)
    # Production atomic Markov trace via recursive ascent (#508).
    # Cross-checked against `atomic-tr-m-mpfr-50dps.witness.json`
    # (Hoefsmit + Wenzl bridge) to ~1e-15 at q₀.
    if atomic_tr_m_at_q0:
        w.add_data(
            "atomic_tr_m_recursive_ascent_at_q0",
            {k: f"{v:+.16e}" for k, v in atomic_tr_m_at_q0.items()},
        )
    w.save()
