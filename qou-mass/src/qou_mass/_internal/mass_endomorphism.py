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

🛑 STALE RESULT CLAIM, CORRECTED 2026-09-06 (bean `qou-oots`).  This docstring
read:

    Result: m_p/m_e ≈ 1870 (CODATA: 1836, error 1.8%).
    Zero fitted parameters.  Inputs: q₀ and m_e only.

**That is contradicted by this module's own committed witness and by its own
live run.**  `mass-endomorphism.witness.json` records

    ratio      = 9310.32782814957
    codata     = 1836.152
    error_pct  = 407.0564870527914

and a fresh run reproduces it, additionally printing `m_n/m_p = 0.014601`
(CODATA 1.001378, error 98.54 %) and `Δm = -4688.11 MeV` against CODATA's
+1.293 MeV — a sign error as well as a magnitude one.  So the true figure is
**407 %, not 1.8 %**: stale by 5× on the value and by 226× on the error.

This was already visible and not acted on:
`docs/audits/2026-05-25-t6-f-ell-derivation-attempt.md` tabulates
`m_p/m_e via per-braid tower = 2.4845` beside "paper claims 1870", i.e. a prior
agent found the docstring did not reproduce and recorded a THIRD number rather
than correcting the source.  `docs/audits/2026-05-17-...-mass-endo.md` still
repeats "m_p/m_e ≈ 1870" in a heading.

Why it matters more than an ordinary stale number: the deleted line paired the
figure with **"Zero fitted parameters"**, which is exactly the kind of claim
that gets quoted onward, and this module has eight importers.

The route is **not** a working prediction of `m_p/m_e`.  What the module is
still good for is the structure it exhibits — the tower shape, the z²-weighted
cross-term from the Markov factorization, and the atomic `tr_M` ascent it prints
— none of which depends on the ratio landing anywhere near CODATA.

Inputs remain q₀ and m_e only; no parameter is fitted.  That half of the
deleted claim stands, and is worth keeping precisely because the number is bad:
an honest parameter-free miss is a result, and it is the fitted kind of
agreement the corpus forbids.

Usage:
    python3 computations/mass_endomorphism.py
"""
import math
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from mpmath import mp  # noqa: E402 — the exact layer; see the _mp block below
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q as q0, Q_INV as qi0, HA as HA_val
from q_parameter import Q_MP as _Q_MP, Q_INV_MP as _QI_MP
from witness_base import WitnessBuilder

# Raise dps BEFORE the _mp constants below are built. A module-level mpf
# constructed at the mpmath default (dps 15) truncates and then never recovers,
# which is what module_const_precision_audit exists to catch.
set_compute_dps()

Q0 = q0  # alias for mass_from_tower
HA = HA_val
z_mark = q0**3 / (q0**2 + 1)
hbar_q = (q0 - 1) / q0

# ── mpmath parallel, mirroring q_parameter's own Q / Q_MP split ──────
#
# `q0` above is f64 BY DESIGN and must stay that way: it is what 18 importers
# read, and `q_parameter` keeps the same split deliberately ("Don't change
# them — downstream f64 callers depend on stability"). Flipping it to mpf is
# not a precision fix, it is two regressions — `json.dumps` raises TypeError on
# mpf, and a numpy array of mpf gets `dtype=object`, silently leaving BLAS
# (measured: that is the same dtype leak that cost a 4000x slowdown in
# hoefsmit_numpy, bean qou-5qwb).
#
# So the exact values live BESIDE the f64 ones. A producer that writes a
# witness should read these; a producer doing bulk f64 linear algebra keeps
# the ones above. `Q_MP` is `q_at(50)` and is bit-identical to
# `Q_50_DIGIT_STR` at 50 digits (checked, not assumed).
q0_mp = _Q_MP
qi0_mp = _QI_MP
HA_mp = q0_mp - qi0_mp
z_mark_mp = q0_mp ** 3 / (q0_mp ** 2 + 1)
hbar_q_mp = (q0_mp - 1) / q0_mp

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

# OWNER RULING 2026-11-20 (PR #8590): this V-hat deliberately keeps the
# pre-convention-D W_sym/W_std/W_alt (q-Plancherel) mixture. The 11-18 ruling
# moved pyhecke.atom to the convention-D Markov trace z*a+b, but here that puts
# the proton V-hat (1.2824) past the Phi_q pole at q0 and m_p/m_e = inf
# (qou-2tuv). Kept, labelled, until the pole is resolved. No number moves.
VHAT_WEIGHTS_LABEL = (
    "pre-convention-D mixture (q-Plancherel W_sym/W_std/W_alt), kept by owner "
    "ruling 2026-11-20 until the Phi_q pole (qou-2tuv) is resolved; "
    "convention-D z*a+b gives m_p/m_e = inf (PR #8590)"
)
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
    z_mark = Q0**3 / (Q0**2 + 1)

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


# ── the mp tower: the half of this module's own policy that was never wired ──
#
# Lines 95-98 state the rule: "A producer that writes a witness should read
# these [the _mp constants]; a producer doing bulk f64 linear algebra keeps the
# ones above." The `_mp` constants were then defined and used NOWHERE -- five
# names, zero consumers -- so the witness has always been written from the f64
# side, against the module's own rule. The raw-float64 ratchet reports 17 fields
# against a baseline of 16, i.e. it has grown.
#
# WHY THIS IS A DUPLICATE RATHER THAN A CONVERSION, and the reasoning is the
# module's own: `q0` is f64 BY DESIGN because 18 importers read it, and flipping
# it is "two regressions" -- json.dumps raises TypeError on mpf, and a numpy
# array of mpf gets dtype=object, which cost a 4000x slowdown in hoefsmit_numpy
# (bean qou-5qwb). So the f64 path below is left EXACTLY as it is and the exact
# path runs beside it, which is what "live BESIDE the f64 ones" was for.
#
# THE EXEMPTION DOES NOT APPLY HERE, which is why the duplication is worth its
# cost: there is no bulk linear algebra in this file at all. The only numpy
# mention is the comment above explaining why numpy is NOT used. These are
# scalar loops over a handful of crossings, so "bulk f64 linear algebra keeps
# the ones above" describes a case this module does not contain.


def qint_mp(k):
    return (q0_mp ** k - qi0_mp ** k) / (q0_mp - qi0_mp) if k else mp.mpf(0)


def qfact_mp(n):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= qint_mp(k)
    return r


def qdim_mp(part, n):
    hooks = []
    for i, rl in enumerate(part):
        for j in range(rl):
            arm = rl - j - 1
            leg = sum(1 for r2 in range(i + 1, len(part)) if part[r2] > j)
            hooks.append(arm + leg + 1)
    num = qfact_mp(n)
    den = mp.mpf(1)
    for h in hooks:
        den *= qint_mp(h)
    return num / den if den != 0 else mp.mpf(0)


_nf3_mp = qfact_mp(3)
w_sym_mp = qdim_mp((3,), 3) ** 2 / _nf3_mp
w_std_mp = qdim_mp((2, 1), 3) ** 2 / _nf3_mp
w_alt_mp = qdim_mp((1, 1, 1), 3) ** 2 / _nf3_mp
_wt_mp = w_sym_mp + w_std_mp + w_alt_mp
w_sym_mp /= _wt_mp
w_std_mp /= _wt_mp
w_alt_mp /= _wt_mp


def Phi_q_mp(z_val, max_k=2000):
    """Φ_q(z) = ∏ (1-q⁻ᵏz)⁻¹, exactly as Phi_q but carrying mpf.

    The f64 version's early exits are kept but re-expressed: `1e-300` was an
    f64-underflow guard and `1e-15` an f64-resolution break, neither of which
    means anything at 50 dps. They become mp-scaled thresholds so the loop
    terminates on the same MATHEMATICAL condition rather than on the old
    arithmetic's floor.
    """
    z_val = mp.mpf(z_val)
    if abs(z_val) >= q0_mp:
        return mp.inf
    product = mp.mpf(1)
    qi_pow = qi0_mp
    tiny = mp.mpf(10) ** (-(mp.dps + 5))
    for _ in range(max_k):
        term = qi_pow * z_val
        factor = 1 - term
        if abs(factor) < tiny:
            return mp.inf
        product /= factor
        if abs(term) < tiny:
            break
        qi_pow *= qi0_mp
    return product


def additive_wedderburn_volumes_mp(n_strands, crossings_per_gen):
    """Exact mirror of additive_wedderburn_volumes on the mp layer."""
    vols = []
    for gen in range(n_strands - 1):
        a, b = mp.mpf(0), mp.mpf(1)
        sp, ap = mp.mpf(1), mp.mpf(1)
        for c, d in crossings_per_gen.get(gen, []):
            c, d = mp.mpf(str(c)), mp.mpf(str(d))
            a, b = a * c * HA_mp + a * d + b * c, a * c + b * d
            sp *= c * q0_mp + d
            ap *= -c * qi0_mp + d
        Vs = z_mark_mp * a + b
        Vf = w_sym_mp * sp + w_std_mp * Vs + w_alt_mp * ap
        vols.append({"std": Vs, "sym": sp, "alt": ap, "full": Vf})
    return vols


def mass_from_tower_mp(vols):
    """Exact mirror of mass_from_tower on the mp layer."""
    n = len(vols)
    desc = mp.mpf(1)
    for v in vols:
        desc *= v["full"]
    desc = abs(desc)
    single = mp.fsum(Phi_q_mp(v["full"]) for v in vols)
    cross = mp.mpf(0)
    for i in range(n):
        for j in range(i + 1, n):
            cross += z_mark_mp ** 2 * Phi_q_mp(
                abs(vols[i]["full"] * vols[j]["full"]))
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

    # The same tower on the exact layer, for the WITNESS only. The f64 results
    # above are what the printed report and the 18 importers see and are left
    # untouched; these are what gets serialized, per this module's own rule
    # that "a producer that writes a witness should read these".
    #
    # Cross-checked, not assumed: the two towers agree to 2.89e-15 relative on
    # m_p/m_e, which is f64 resolution -- so the mp path is a faithful mirror
    # AND float64 was never the source of the 407% miss. Recording that here
    # because "we made it exact" invites the reading that the number might
    # move, and it does not.
    e_vols_mp = additive_wedderburn_volumes_mp(2, electron_cross)
    e_desc_x, e_single_x, e_cross_x, e_total_x = mass_from_tower_mp(e_vols_mp)
    p_vols_mp = additive_wedderburn_volumes_mp(3, proton_cross)
    p_desc_x, p_single_x, p_cross_x, p_total_x = mass_from_tower_mp(p_vols_mp)
    n_vols_mp = additive_wedderburn_volumes_mp(3, neutron_cross)
    n_desc_x, n_single_x, n_cross_x, n_total_x = mass_from_tower_mp(n_vols_mp)

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
    from qou_substrate.codata import codata as _codata
    _np = float(_codata("neutron-proton mass ratio").value_str)  # float64-ok: display-only % error in a report line
    print(f"m_n/m_p = {n_total / p_total:.6f}  (CODATA: {_np:.6f}, error {abs(n_total/p_total - _np)/_np*100:.4f}%)")
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
    w.add_parameter("q0", fmt(q0_mp))
    w.add_parameter("vhat_weights", VHAT_WEIGHTS_LABEL)
    w.add_parameter("w_sym", fmt(w_sym_mp))
    w.add_parameter("w_std", fmt(w_std_mp))
    w.add_parameter("w_alt", fmt(w_alt_mp))
    w.add_parameter("z_markov", fmt(z_mark_mp))
    w.add_parameter("z_squared", fmt(z_mark_mp**2))
    w.add_data(
        "electron",
        {
            "vols": [{"std": fmt(v["std"]), "full": fmt(v["full"])}
                     for v in e_vols_mp],
            "n_generators": 1,
            "descended": fmt(e_desc_x),
            "single": fmt(e_single_x),
            "cross": fmt(e_cross_x),
            "total": fmt(e_total_x),
        },
    )
    w.add_data(
        "proton",
        {
            "vols": [{"std": fmt(v["std"]), "full": fmt(v["full"])}
                     for v in p_vols_mp],
            "n_generators": 2,
            "crossings": "3σ(B₃)+1σ(uu)+1½(ud)+2σ(gluon) | 3σ⁻¹(B₃)+1½(ud)",
            "descended": fmt(p_desc_x),
            "single": fmt(p_single_x),
            "cross": fmt(p_cross_x),
            "total": fmt(p_total_x),
        },
    )
    _ratio_x = p_total_x / e_total_x
    _codata = mp.mpf("1836.152")
    w.add_data("ratio", fmt(_ratio_x))
    w.add_data("codata", str(_codata))
    w.add_data("error_pct", fmt(abs(_ratio_x - _codata) / _codata * 100))
    # Production atomic Markov trace via recursive ascent (#508).
    # Cross-checked against `atomic-tr-m-mpfr-50dps.witness.json`
    # (Hoefsmit + Wenzl bridge) to ~1e-15 at q₀.
    if atomic_tr_m_at_q0:
        w.add_data(
            "atomic_tr_m_recursive_ascent_at_q0",
            {k: f"{v:+.16e}" for k, v in atomic_tr_m_at_q0.items()},
        )
    w.save()
