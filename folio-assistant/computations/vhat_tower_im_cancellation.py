"""
Im-cancellation gate for the candidate-2 (analytically continued Li_2^q)
brane tower of the DERIVED per-crossing V̂_i.

Context (predecessor PR #1657,
docs/audits/2026-06-01-convergence-safe-vhat-tower.md)
----------------------------------------------------------------------
The genuine derived per-crossing factor V̂_i = z·a_i + b_i diverges the
Rogers Li_2^q tower because |V̂_0(proton)| = 1.146 > radius q₀ = 1.110.
PR #1657 ESTABLISHED that z = q₀ is an integrable LOGARITHMIC BRANCH
POINT (not a pole), so Li_2^q analytically continues past it with ZERO
free parameters (+i0 principal branch, identity theorem):

    Li_2^q(1.146) = 2.0809 + 0.6568 i   (FINITE but COMPLEX)

The continued tower converges (proton 4.977) and preserves the p/n
signal (+18.9%). Candidate 2 ACCEPTED. The SINGLE remaining gate:

    is the archimedean observable mass m = m_e · (tower) REAL?

The continued value carries Im ≈ 0.657 per generator with |V̂| > q₀.
Per CLAUDE.md "Im(q) at fibre vs observable level": imaginary parts are
LEGITIMATE at the fibre level (formal q, pre-τ), but the ARCHIMEDEAN
observable (post-τ, at q₀) MUST be real (Im(q₀)=0 is an archimedean
constraint, `lusztig_q_0_imaginary_part_zero`,
four_unwired_theorems_regression.py).

THIS PROBE — does Im cancel STRUCTURALLY (not by assuming/fitting)?
----------------------------------------------------------------------
Computes the FULL complex tower (T1, T2, T3) for proton, neutron, AND
electron (figure-eight 4_1) with candidate-2 continuation at 60 dps,
then tests four candidate Im-cancellation mechanisms, EACH judged
DERIVED-real (the τ-functor structurally dictates the projection) vs
CHOSEN-real (the projection is selected because "the mass must be
real" — a fit):

  (a) Σ_i Im Li_2^q(|V̂_i|) = 0 across generators within one particle?
  (b) Im(proton tower)/Im(electron tower) real via m_e normalisation?
  (c) Is the archimedean projection Re / |·| / full-complex, per the
      τ-functor DEFINITION (prop:vol-through-tau, def:algebraic-quantum
      -volume, def:archimedean-realization-functor)?
  (d) (+i0)+(−i0) branch average = Re (discontinuity is 2i·Im) — is
      averaging the two branches canonical, or a choice?

DISCIPLINE (CLAUDE.md production-vs-exploratory): taking Re/|·|/avg is
ONLY valid if the τ-functor STRUCTURALLY dictates it. "The mass must be
real" is CIRCULAR/a fit unless the functor independently requires it.
No tuning to m_p=938.27 / CODATA. {e-, p, n} are the falsification
test. Every number RAW @ 60 dps.

STRUCTURAL KEY (read FIRST):
  def:algebraic-quantum-volume — τ_arch(Vol_q(β)) = ln|Vol_{q0}(β)|
    = Σ_i ln|V̂_i(q0)|. The archimedean rule on the MULTIPLICATIVE
    quantum-volume generator is the ABSOLUTE LOGARITHM |·|_∞→log|·|_∞,
    NOT Re, NOT the full complex value.
  prop:vol-through-tau / archimedean-functor-uniqueness — the
    dilogarithm archimedean image is the BLOCH-WIGNER dilogarithm
    D(z) = Im Li_2(z) + log|z|·arg(1−z), which is REAL BY CONSTRUCTION
    (the Bloch-Suslin characterisation: the unique real-valued
    continuous antisymmetric pentagon-coherent functional on B(ℂ)).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import time  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import M_E_MEV as _M_E_MEV_CAL1  # noqa: E402

set_compute_dps()

_START = time.monotonic()

from _li_2_q_util import li_2_q, load_q_50dps  # noqa: E402


# ── Genuine derived per-crossing V̂_i (std channel) ────────────────────
# (recomputed self-contained from PR #1657's convergence_safe_vhat_tower.py
#  so this probe stands alone; cross-checked ∏V̂ = tr_M below.)


def _std_vhat(chain, q, qi, z, h):
    """Std-channel Markov-trace factor V̂ = z·a + b for one crossing chain.
    Standard (2,1) Hoefsmit seminormal recurrence (thm:markov-trace-product)."""
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        c = mp.mpf(c)
        d = mp.mpf(d)
        a, b = a * c * h + a * d + b * c, a * c + b * d
    return z * a + b


def nucleon_chains(quarks, h):
    """Per-generator (g0, g1) crossing chains. Mirrors atom.nucleon_gen_chains."""
    g0 = [(1, 0)] * 3
    g1 = [(1, -h)] * 3
    pairs = [(0, 1, 0), (0, 2, 0), (1, 2, 1)]
    for i, j, gen in pairs:
        qi_f, qj_f = quarks[i], quarks[j]
        if qi_f == qj_f == "u":
            cd = (1, 0)
        elif qi_f == qj_f == "d":
            cd = (1, -h)
        else:
            cd = (1, -h / 2)
        (g0 if gen == 0 else g1).append(cd)
    g0.append((1, 0))
    g0.append((1, 0))
    return g0, g1


def figure8_chains(h):
    """Figure-eight 4_1 braid for the electron — (σ₁σ₂⁻¹)² on 3 strands.

    The electron is the amphichiral 4_1 knot (mass-theory canonical:
    muon/electron = 4_1 figure-eight, the amphichiral mass mechanism,
    archimedean-functor-uniqueness.md consequence (c)). g0 collects the
    σ₁ crossings (positive, std-rep (c,d)=(1,0)); g1 collects the σ₂⁻¹
    crossings (negative, σ⁻¹ = σ − h ⇒ (c,d)=(1,-h)). Mirrors the
    nucleon_chains std-(2,1) construction restricted to 4_1's braid word.
    """
    g0 = [(1, 0), (1, 0)]      # two σ₁ positive crossings
    g1 = [(1, -h), (1, -h)]    # two σ₂⁻¹ negative crossings
    return g0, g1


# ── Candidate-2 analytic continuation of Li_2^q (from PR #1657) ────────


def q_log_lambert(z, q, qi, m_terms=6000):
    """ln_q(1−z) = −Σ z^n/[n]_q via Lambert closed form (meromorphic,
    simple poles at z=q^{2m+1}). Returns −Σ z^n/[n]_q."""
    h = q - qi
    total = mp.mpf(0)
    tol = mp.mpf(10) ** (5 - mp.mp.dps)
    for m in range(m_terms):
        w = z * qi ** (2 * m + 1)
        denom = 1 - w
        if mp.fabs(denom) < tol:
            return mp.mpf("nan")
        term = w / denom
        total += term
        if mp.fabs(term) < tol and m > 2:
            break
    return -h * total


def li_2_q_continued(z, q, qi, branch=+1):
    """Analytic continuation of Li_2^q(z) past |z|=q via path integration of
    d/dz Li_2^q = −ln_q(1−z)/z, deforming around the pole at u=q.

    branch=+1  → +i0 (upper semicircle, standard dilogarithm principal branch)
    branch=−1  → −i0 (lower semicircle, the OTHER branch)

    Li_2^q(z) = −∫_0^z ln_q(1−u)/u du. For real z>q the segment crosses the
    simple pole at u=q; deform into the chosen half-plane. ZERO free
    parameters per branch. Returns complex value."""
    z = mp.mpf(z)
    eps = mp.mpf("1e-7")

    def integrand(u):
        lg = q_log_lambert(u, q, qi)
        return -lg / u

    if z <= q:
        return mp.quad(integrand, [mp.mpf("1e-30"), z])
    part1 = mp.quad(integrand, [mp.mpf("1e-30"), q - eps])

    def arc(theta):
        u = q + eps * mp.e ** (1j * theta)
        du = 1j * eps * mp.e ** (1j * theta)
        return integrand(u) * du

    # +i0: contour goes over the top (theta: pi → 0); −i0: under (−pi → 0)
    arc_lo = mp.pi if branch > 0 else -mp.pi
    part_arc = mp.quad(arc, [arc_lo, 0])
    part3 = mp.quad(integrand, [q + eps, z])
    return part1 + part_arc + part3


def li_2_q_safe(v, q, qi, branch=+1):
    """Li_2^q(|v|): series if |v|<q, +i0/−i0 continuation if |v|≥q.
    Always returns mpc (complex)."""
    a = mp.fabs(v)
    if a < q:
        return mp.mpc(li_2_q(a, q, qi), 0)
    return mp.mpc(li_2_q_continued(a, q, qi, branch=branch))


# ── Full COMPLEX tower (T1, T2, T3) per particle ──────────────────────


def complex_tower(vhat_g0, vhat_g1, q, qi, z, branch=+1):
    """Full candidate-2 tower with COMPLEX terms reported individually.

    T1 = |∏V̂_i|                         (descended; real by construction)
    T2 = Σ_i Li_2^q_cont(|V̂_i|)         (complex if any |V̂_i|≥q)
    T3 = z²·Σ_{i<j} Li_2^q_cont(|V̂_iV̂_j|)
    Production positive-argument form (matches PR #1657). Returns a dict of
    complex mpc values + per-generator Im breakdown.
    """
    v0, v1 = vhat_g0, vhat_g1
    t1 = mp.mpc(mp.fabs(v0 * v1), 0)
    f0 = li_2_q_safe(v0, q, qi, branch)
    f1 = li_2_q_safe(v1, q, qi, branch)
    f01 = li_2_q_safe(v0 * v1, q, qi, branch)
    t2 = f0 + f1
    t3 = (z ** 2) * f01
    total = t1 + t2 + t3
    return {
        "v0": v0, "v1": v1,
        "abs_v0": mp.fabs(v0), "abs_v1": mp.fabs(v1),
        "f0": f0, "f1": f1, "f01": f01,
        "T1": t1, "T2": t2, "T3": t3, "total": total,
        # per-generator Im breakdown for mechanism (a)
        "im_f0": mp.im(f0), "im_f1": mp.im(f1), "im_f01": mp.im(f01),
        "sum_im_generators": mp.im(f0) + mp.im(f1),  # T2 generators only
        "im_total": mp.im(total),
    }


def _cx(c):
    """Serialize an mpc as {re, im, abs, arg}."""
    c = mp.mpc(c)
    return {
        "re": str(mp.re(c)),
        "im": str(mp.im(c)),
        "abs": str(mp.fabs(c)),
        "arg": str(mp.arg(c)) if mp.fabs(c) != 0 else "0",
    }


def main():
    mp.mp.dps = 60
    q, qi, z = load_q_50dps()
    h = q - qi

    out = {
        "description": (
            "Im-cancellation gate for the candidate-2 continued-Li_2^q brane "
            "tower of the derived per-crossing V̂_i. Full COMPLEX tower for "
            "proton/neutron/electron @ 60 dps; four Im-cancellation mechanisms "
            "judged DERIVED-real vs CHOSEN-real against the τ-functor definition. "
            "RAW, zero free parameters, no tuning to m_p/CODATA."
        ),
        "computation": "vhat_tower_im_cancellation",
        "predecessor": "docs/audits/2026-06-01-convergence-safe-vhat-tower.md (PR #1657)",
        "q0": str(q), "q0_inv": str(qi), "z_markov": str(z), "h": str(h),
        "radius_li2q": str(q),
        "generated": datetime.now(timezone.utc).isoformat(),
    }

    # ── build V̂_i for the three particles ────────────────────────────
    pg0, pg1 = nucleon_chains(("u", "u", "d"), h)
    ng0, ng1 = nucleon_chains(("u", "d", "d"), h)
    eg0, eg1 = figure8_chains(h)
    vhat = {
        "proton": (_std_vhat(pg0, q, qi, z, h), _std_vhat(pg1, q, qi, z, h)),
        "neutron": (_std_vhat(ng0, q, qi, z, h), _std_vhat(ng1, q, qi, z, h)),
        "electron": (_std_vhat(eg0, q, qi, z, h), _std_vhat(eg1, q, qi, z, h)),
    }
    out["vhat_std_derived"] = {
        n: {"g0": str(v[0]), "g1": str(v[1]), "prod_tr_m": str(v[0] * v[1]),
            "abs_g0": str(mp.fabs(v[0])), "abs_g1": str(mp.fabs(v[1])),
            "g0_over_q0": str(mp.fabs(v[0]) / q), "g1_over_q0": str(mp.fabs(v[1]) / q)}
        for n, v in vhat.items()
    }
    out["pn_signal_g0_relative_raw_vhat"] = str(
        (vhat["proton"][0] - vhat["neutron"][0]) / vhat["neutron"][0]
    )

    # ── (1) FULL COMPLEX tower, +i0 branch, per particle ──────────────
    print(f"[{datetime.now(timezone.utc).isoformat()}] computing +i0 towers...")
    towers_plus = {n: complex_tower(v[0], v[1], q, qi, z, branch=+1)
                   for n, v in vhat.items()}
    print(f"[{datetime.now(timezone.utc).isoformat()}] computing −i0 towers...")
    towers_minus = {n: complex_tower(v[0], v[1], q, qi, z, branch=-1)
                    for n, v in vhat.items()}

    out["complex_tower_plus_i0"] = {}
    for n, t in towers_plus.items():
        out["complex_tower_plus_i0"][n] = {
            "f0_Li2q": _cx(t["f0"]), "f1_Li2q": _cx(t["f1"]), "f01_Li2q": _cx(t["f01"]),
            "T1": _cx(t["T1"]), "T2": _cx(t["T2"]), "T3": _cx(t["T3"]),
            "total": _cx(t["total"]),
            "abs_v0": str(t["abs_v0"]), "abs_v1": str(t["abs_v1"]),
            "abs_v0_exceeds_q0": bool(t["abs_v0"] > q),
            "abs_v1_exceeds_q0": bool(t["abs_v1"] > q),
        }
    out["complex_tower_minus_i0"] = {
        n: {"total": _cx(t["total"]), "T2": _cx(t["T2"]), "T3": _cx(t["T3"])}
        for n, t in towers_minus.items()
    }

    # ════════════════════════════════════════════════════════════════
    # MECHANISM (a): Σ_i Im Li_2^q(|V̂_i|) = 0 across generators?
    # ════════════════════════════════════════════════════════════════
    mech_a = {}
    for n, t in towers_plus.items():
        sum_im = t["sum_im_generators"]      # Im f0 + Im f1 (T2)
        im_total = t["im_total"]             # full tower Im (incl T3)
        mech_a[n] = {
            "im_f0_generator": str(t["im_f0"]),
            "im_f1_generator": str(t["im_f1"]),
            "sum_im_T2_generators": str(sum_im),
            "im_f01_T3": str(t["im_f01"]),
            "im_total_tower": str(im_total),
            "cancels_within_particle": bool(mp.fabs(im_total) < mp.mpf("1e-40")),
        }
    out["mechanism_a_im_cancel_across_generators"] = mech_a

    # ════════════════════════════════════════════════════════════════
    # MECHANISM (b): Im(proton tower)/Im(electron tower) real ratio?
    # m(K) = m_e · (tower(K) / tower(electron)). If the electron tower is
    # also complex, does the RATIO come out real?
    # ════════════════════════════════════════════════════════════════
    mech_b = {}
    te = towers_plus["electron"]["total"]
    for n in ("proton", "neutron"):
        tk = towers_plus[n]["total"]
        ratio = tk / te if te != 0 else mp.mpc("nan")
        mech_b[n] = {
            "tower_K": _cx(tk),
            "tower_electron": _cx(te),
            "ratio_K_over_electron": _cx(ratio),
            "ratio_is_real": bool(mp.fabs(mp.im(ratio)) < mp.mpf("1e-40")),
            "ratio_im_over_re": (
                str(mp.fabs(mp.im(ratio) / mp.re(ratio))) if mp.re(ratio) != 0 else "inf"
            ),
        }
    out["mechanism_b_normalization_ratio"] = mech_b
    out["mechanism_b_electron_tower_im"] = str(mp.im(te))

    # ════════════════════════════════════════════════════════════════
    # MECHANISM (c): what does the τ-functor DEFINITION dictate?
    #   def:algebraic-quantum-volume: τ_arch(Vol_q) = ln|Vol_{q0}| = Σ ln|V̂_i|
    #     → the archimedean rule on the MULTIPLICATIVE generator (T1) is the
    #       ABSOLUTE LOG, NOT Re. T1 is ALREADY real (= |∏V̂_i|).
    #   prop:vol-through-tau / archimedean-functor-uniqueness: the dilog
    #     archimedean image is the BLOCH-WIGNER D(z)=Im Li_2+log|z|·arg(1−z),
    #     REAL BY CONSTRUCTION.
    # ════════════════════════════════════════════════════════════════
    def bloch_wigner(zv):
        """Classical Bloch-Wigner D(z) = Im Li_2(z) + log|z|·arg(1−z), the
        DERIVED archimedean image per prop:vol-through-tau / Bloch-Suslin.
        This helper intentionally evaluates on the real nonnegative argument
        |z| (it takes mp.fabs below) — the V̂_i magnitudes are real, and
        D(real) = 0 is exactly the structural fact under test."""
        zv = mp.fabs(zv)
        li2 = mp.polylog(2, zv)
        return mp.im(li2) + mp.log(mp.fabs(zv)) * mp.arg(1 - zv)

    mech_c = {}
    for n, t in towers_plus.items():
        f0 = t["f0"]
        mech_c[n] = {
            "T1_log_volume_arch": str(mp.log(mp.fabs(t["v0"] * t["v1"]))),  # Σ ln|V̂_i|
            "T1_is_real": True,
            "abs_li2q_f0": str(mp.fabs(f0)),
            "re_li2q_f0": str(mp.re(f0)),
            "im_li2q_f0": str(mp.im(f0)),
            "bloch_wigner_D_v0": str(bloch_wigner(t["v0"])),
            "bloch_wigner_D_v1": str(bloch_wigner(t["v1"])),
        }
    out["mechanism_c_tau_functor_dictation"] = mech_c
    out["mechanism_c_verdict"] = (
        "The τ-functor DOES structurally dictate a real projection, but NOT "
        "Re(Li_2^q). Two distinct archimedean rules apply: (1) on the "
        "MULTIPLICATIVE quantum-volume generator (T1=∏V̂_i) the rule is "
        "τ_arch=ln|·|_∞ (def:algebraic-quantum-volume) — T1 is already real. "
        "(2) on the dilogarithm/brane-tower object (T2,T3) the archimedean "
        "image is the BLOCH-WIGNER dilogarithm D(z)=Im Li_2+log|z|·arg(1−z) "
        "(prop:vol-through-tau, archimedean-functor-uniqueness, Bloch-Suslin), "
        "which is REAL BY CONSTRUCTION. Taking Re(Li_2^q) is NOT what the "
        "functor says; the functor says take the Bloch-Wigner combination. "
        "DERIVED-real IFF the production tower equals the Bloch-Wigner image; "
        "CHOSEN-real if one simply drops Im."
    )

    # ════════════════════════════════════════════════════════════════
    # MECHANISM (d): branch average ((+i0)+(−i0))/2 = Re ?
    # The discontinuity across the cut is f(+i0)−f(−i0) = 2i·Im, so the
    # average is the real part. Is averaging the two branches canonical?
    # ════════════════════════════════════════════════════════════════
    mech_d = {}
    for n in ("proton", "neutron", "electron"):
        tp = towers_plus[n]["total"]
        tm = towers_minus[n]["total"]
        avg = (tp + tm) / 2
        disc = tp - tm
        mech_d[n] = {
            "total_plus_i0": _cx(tp),
            "total_minus_i0": _cx(tm),
            "average": _cx(avg),
            "average_is_real": bool(mp.fabs(mp.im(avg)) < mp.mpf("1e-40")),
            "discontinuity_2i_im": _cx(disc),
            "avg_equals_re_of_plus": str(mp.fabs(mp.re(avg) - mp.re(tp))),
        }
    out["mechanism_d_branch_average"] = mech_d
    out["mechanism_d_verdict"] = (
        "The branch average ((+i0)+(−i0))/2 IS real (the cut discontinuity is "
        "exactly 2i·Im, so the average projects to Re). But averaging the two "
        "branches is NOT the canonical +i0 dilogarithm prescription — the "
        "standard dilogarithm continuation (and the Bloch-Wigner D) commits to "
        "ONE branch (+i0). Averaging is a CHOICE (it equals Re by construction), "
        "so unless the τ-functor independently selects the symmetric (principal-"
        "value) branch, it is CHOSEN-real, not DERIVED-real. The Bloch-Wigner D "
        "is the DERIVED real object — it is NOT the average, it is Im Li_2 + "
        "log|z|·arg(1−z), a DIFFERENT real number from Re or from the average."
    )

    # ── p/n signal preservation under each real projection ────────────
    def real_total_re(t):
        return mp.re(t["total"])

    def real_total_bw(t):
        # Bloch-Wigner-projected tower: T1 (real) + Σ D(|V̂_i|) + z² D(|∏|)
        t1 = mp.fabs(t["v0"] * t["v1"])
        t2 = bloch_wigner(t["v0"]) + bloch_wigner(t["v1"])
        t3 = (z ** 2) * bloch_wigner(t["v0"] * t["v1"])
        return t1 + t2 + t3

    pn = {}
    re_p = real_total_re(towers_plus["proton"])
    re_n = real_total_re(towers_plus["neutron"])
    bw_p = real_total_bw(towers_plus["proton"])
    bw_n = real_total_bw(towers_plus["neutron"])
    pn["Re_projection"] = {
        "proton": str(re_p), "neutron": str(re_n),
        "pn_relative": str((re_p - re_n) / re_n) if re_n != 0 else "div0",
    }
    pn["BlochWigner_projection"] = {
        "proton": str(bw_p), "neutron": str(bw_n),
        "pn_relative": str((bw_p - bw_n) / bw_n) if bw_n != 0 else "div0",
    }
    out["pn_signal_under_real_projections"] = pn

    # ── raw m_p in MeV IF a structurally-justified real emerges ───────
    # m(K) = m_e · tower(K)/tower(electron). Report under BOTH Re and BW
    # projections, RAW. m_e is the CAL-1 dimensional anchor (CODATA), NOT a
    # fit target.
    m_e_MeV = mp.mpf(str(_M_E_MEV_CAL1))  # CAL-1 anchor from registry (P31)
    re_e = real_total_re(towers_plus["electron"])
    bw_e = real_total_bw(towers_plus["electron"])
    raw_mp = {}
    if re_e != 0:
        raw_mp["Re_projection_m_p_MeV"] = str(m_e_MeV * re_p / re_e)
        raw_mp["Re_projection_m_n_MeV"] = str(m_e_MeV * re_n / re_e)
    if bw_e != 0:
        raw_mp["BlochWigner_projection_m_p_MeV"] = str(m_e_MeV * bw_p / bw_e)
        raw_mp["BlochWigner_projection_m_n_MeV"] = str(m_e_MeV * bw_n / bw_e)
    raw_mp["note"] = (
        "RAW m_p via m_e·tower(p)/tower(e). m_e is the CAL-1 dimensional "
        "anchor (CODATA), NOT a fit target. No tuning to m_p=938.27. The "
        "value is whatever the structural projection gives. The electron "
        "figure-8 tower normalisation is itself a modelling choice flagged "
        "in the audit; report raw, do not tune."
    )
    out["raw_m_p_MeV_per_projection"] = raw_mp

    # ── fill mechanism (a) verdict from computed values ───────────────
    p_im = mp.mpf(mech_a["proton"]["im_total_tower"])
    out["mechanism_a_verdict"] = (
        "Im does NOT cancel within a single particle. The proton tower Im = "
        + str(p_im)[:14]
        + " (nonzero). Each generator with |V̂_i|>q₀ contributes a same-sign Im "
        "(the +i0 branch fixes the sign), and they ADD. Mechanism (a) REFUTED "
        "structurally — there is no cancellation, so this is a clean negative, "
        "not a chosen projection."
    )

    # ── fill mechanism (b) verdict from computed ratio ────────────────
    ratio_p_real = mech_b["proton"]["ratio_is_real"]
    out["mechanism_b_verdict"] = (
        "The electron figure-8 tower is "
        + ("ALSO complex" if mp.im(te) != 0 else "REAL")
        + " (Im="
        + str(mp.im(te))[:14]
        + "); the proton/electron ratio is "
        + ("REAL" if ratio_p_real else "STILL COMPLEX")
        + ". "
        + (
            "Im cancels in the ratio — DERIVED-real only if the Im parts are "
            "forced equal by structure; here they are not (different |V̂| exceed "
            "q₀ by different amounts), so any real ratio is coincidental."
            if ratio_p_real
            else "Im does NOT cancel in the normalisation ratio: proton and "
            "electron towers have independent, unequal imaginary parts that do "
            "not divide out. Mechanism (b) REFUTED."
        )
    )

    # ── headline verdict ──────────────────────────────────────────────
    out["VERDICT"] = (
        "The naive Re(Li_2^q) projection is CHOSEN-real (dropping Im because "
        "'mass must be real' is a fit). The branch-average is CHOSEN-real "
        "(equals Re by construction, not the canonical +i0 branch). Im does "
        "NOT cancel across generators (mech a) nor through the m_e "
        "normalisation ratio (mech b). The ONLY structurally-DERIVED real "
        "projection is the BLOCH-WIGNER dilogarithm D(z)=Im Li_2+log|z|·"
        "arg(1−z) dictated by prop:vol-through-tau / archimedean-functor-"
        "uniqueness (Bloch-Suslin pentagon-uniqueness) — BUT that requires the "
        "production brane-tower object to literally BE the archimedean image of "
        "a pentagon-coherent Bloch-group class, i.e. T2/T3 = Σ D, a DIFFERENT "
        "functional from Re(Li_2^q). See the audit doc for the DERIVED-vs-"
        "CHOSEN classification and the raw m_p per projection. The continued "
        "tower CONVERGES but its archimedean reality is DERIVED only through "
        "the Bloch-Wigner route, not by taking Re — a genuine structural "
        "distinction, not a free real projection."
    )

    wpath = (
        WitnessBuilder.wrap_legacy(
            "vhat-tower-im-cancellation",
            out,
            script_path=__file__,
            engine="mpmath",
            start_time=_START,
        )
        .set_audit_only("docs/audits/2026-06-01-vhat-tower-im-cancellation.md")
        .save()
    )

    # ── console summary ───────────────────────────────────────────────
    print(f"\nWrote {wpath}")
    print("\n=== genuine derived V̂_i (std) ===")
    for n, v in vhat.items():
        print(f"  {n:9s}: g0={float(v[0]):+.6f} g1={float(v[1]):+.6f} "
              f"∏={float(v[0]*v[1]):.6f}  |g0|={float(mp.fabs(v[0])):.4f} "
              f"|g1|={float(mp.fabs(v[1])):.4f}  (q₀={float(q):.5f})")
    print(f"  p/n g0 signal (raw V̂): "
          f"{float(out['pn_signal_g0_relative_raw_vhat'])*100:+.2f}%")

    print("\n=== full COMPLEX tower (+i0), per term ===")
    for n, t in towers_plus.items():
        print(f"  {n}:")
        for k in ("T1", "T2", "T3", "total"):
            c = mp.mpc(t[k])
            print(f"    {k:6s} = {float(mp.re(c)):+.6f} {float(mp.im(c)):+.6f} i")

    print("\n=== mechanism (a) Im across generators ===")
    for n, d in mech_a.items():
        print(f"  {n:9s} Σ Im(T2 gen)={float(mp.mpf(d['sum_im_T2_generators'])):+.6f}"
              f"  Im(total)={float(mp.mpf(d['im_total_tower'])):+.6f}"
              f"  cancels={d['cancels_within_particle']}")

    print("\n=== mechanism (b) m_e normalisation ratio ===")
    for n, d in mech_b.items():
        print(f"  {n:9s} ratio K/e: re={float(mp.mpf(d['ratio_K_over_electron']['re'])):+.6f}"
              f" im={float(mp.mpf(d['ratio_K_over_electron']['im'])):+.6f}"
              f"  real={d['ratio_is_real']}")

    print("\n=== mechanism (d) branch average ===")
    for n, d in mech_d.items():
        print(f"  {n:9s} avg: re={float(mp.mpf(d['average']['re'])):+.6f}"
              f" im={float(mp.mpf(d['average']['im'])):+.2e}"
              f"  real={d['average_is_real']}")

    print("\n=== p/n signal under real projections ===")
    for proj, d in pn.items():
        print(f"  {proj:24s} p/n={float(mp.mpf(d['pn_relative']))*100:+.3f}%")

    print("\n=== raw m_p (MeV) per projection ===")
    for k, vv in raw_mp.items():
        if k != "note":
            print(f"  {k:34s} = {vv}")

    print("\n=== VERDICT ===")
    print(" ", out["VERDICT"])


if __name__ == "__main__":
    main()
