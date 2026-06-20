"""
Convergence-safe brane tower for the DERIVED per-crossing V̂_i — four
candidate functionals, each justified from categorical structure FIRST,
convergence/finiteness checked SECOND.

Context
-------
The DERIVED standard-channel Markov-trace per-crossing factor
V̂_i = z·a_i + b_i (the "std" channel, ∏V̂ = tr_M to 4e-6, carries the
p/n isospin signal) DIVERGES the brane tower:

    T2 = Σ_i Li_2^q(|V̂_i|)        (Rogers q-dilog, radius |z| < q₀)

because the genuine proton σ₀ factor |V̂_0| = 1.1461 > q₀ = 1.10998, so
Li_2^q(|V̂_0|) = +∞.  See:
  - docs/audits/2026-06-01-vhat-per-crossing-transfer-chain.md (#1631)
  - docs/audits/2026-06-01-vhat-std-channel-fix.md (#1635)

This probe evaluates four DERIVATION-MOTIVATED candidates for a tower
functional F(V̂_i) that (a) accepts |V̂_i| > q₀, (b) converges, (c)
reduces to the working tower in overlap, (d) preserves the p/n signal,
with ZERO free parameters:

  1. Faddeev Φ_q (the bar-ASYMMETRIC mass-channel dilog).
  2. Analytic continuation of Li_2^q past |z| = q₀ (pole vs series-boundary).
  3. Bar-symmetrization (q ↔ q⁻¹) of the argument.
  4. Reciprocal/inversion V̂ ↦ 1/V̂ for |V̂| > 1 (Hecke σ ↔ σ⁻¹ antipode).

DISCIPLINE (AGENTS.md production-vs-exploratory): a functional chosen
BECAUSE it converges/fits is a FIT (RED). Each candidate's categorical
justification is stated, THEN finiteness is checked. The {e-, p, n}
masses are the FALSIFICATION TEST, never fit targets. All values RAW.

The canonical mass tower per prop:mass-endomorphism-tower uses
−Li_2^q(−|V̂_i|) (NEGATIVE argument); the production
compute_t2_t3_from_vols uses +|V̂_i|. Both have radius |z| < q₀, so the
proton σ₀ divergence is sign-independent for finiteness; we report both.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
set_compute_dps()

from _li_2_q_util import li_2_q, load_q_50dps  # noqa: E402
from _phi_q_util import phi_q  # noqa: E402


# ── Genuine derived per-crossing V̂_i (std channel) ────────────────────


def _std_vhat(chain, q, qi, z, h):
    """Std-channel Markov-trace factor V̂ = z·a + b for one crossing chain.

    (a, b) evolves by left-mult by the 2×2 std-rep matrix of c·σ+d:
        a ← a·c·h + a·d + b·c ;  b ← a·c + b·d   (init (a,b)=(0,1))
    Standard (2,1) Hoefsmit seminormal recurrence (thm:markov-trace-product).
    z = 1/(q^{1/2}+q^{-1/2}) Markov parameter, h = q − q⁻¹.
    """
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


# ── Candidate 2 helpers: q-log closed form + Li_2^q analytic structure ─


def q_log_lambert(z, q, qi, m_terms=6000):
    """ln_q(1−z) = −Σ_{n≥1} z^n/[n]_q  via its Lambert-series closed form.

    Exact:  1/[n]_q = (q−q⁻¹)·Σ_{m≥0} q^{-(2m+1)n}, so
        Σ_n z^n/[n]_q = (q−q⁻¹)·Σ_{m≥0} (z q^{-(2m+1)})/(1 − z q^{-(2m+1)}).
    Each m-term has a SIMPLE POLE at z = q^{2m+1}; nearest z=q. The OUTER
    sum over m converges off {q,q³,q⁵,…}. ⇒ ln_q(1−z) is MEROMORPHIC with
    simple poles at z=q^{2m+1}. Returns −Σ z^n/[n]_q.
    """
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


def li_2_q_continued(z, q, qi):
    """Analytic continuation of Li_2^q(z) past |z|=q via path integration of
    d/dz Li_2^q = −ln_q(1−z)/z, deforming the contour around the pole at u=q.

    Li_2^q(z) = −∫_0^z ln_q(1−u)/u du (prop:mass-endomorphism-tower proof).
    For real z>q the segment [0,z] crosses the simple pole of ln_q at u=q;
    we deform into the UPPER half plane (semicircle radius eps) — the +i0
    principal-branch prescription standard for the dilogarithm. ZERO free
    parameters (deformation side fixed by +i0). Returns complex value.
    """
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

    part_arc = mp.quad(arc, [mp.pi, 0])
    part3 = mp.quad(integrand, [q + eps, z])
    return part1 + part_arc + part3


# ── Candidates as per-generator functionals F(|V̂|) ───────────────────


def cand1_phi_q(v, q, qi):
    """Candidate 1: Faddeev Φ_q(|V̂|). cheat-sheet §4 sorts Φ_q=MASS channel."""
    return phi_q(mp.fabs(v), qi)


def cand2_li2q_continued(v, q, qi):
    """Candidate 2: analytically continued Li_2^q(|V̂|) (probe core)."""
    return li_2_q_continued(mp.fabs(v), q, qi)


def cand4_reciprocal(v, q, qi):
    """Candidate 4: reciprocal V̂↦1/V̂ for |V̂|>1 (Hecke σ↔σ⁻¹ antipode test)."""
    a = mp.fabs(v)
    arg = a if a <= 1 else 1 / a
    return li_2_q(arg, q, qi)


def main():
    mp.mp.dps = 60
    q, qi, z = load_q_50dps()
    h = q - qi
    out = {
        "description": "Convergence-safe brane tower for derived per-crossing V̂_i: "
        "4 derivation-motivated candidates, raw, zero free parameters.",
        "computation": "convergence_safe_vhat_tower",
        "q0": str(q),
        "q0_inv": str(qi),
        "z_markov": str(z),
        "h": str(h),
        "radius_li2q": str(q),
        "generated": datetime.now(timezone.utc).isoformat(),
    }

    pg0, pg1 = nucleon_chains(("u", "u", "d"), h)
    ng0, ng1 = nucleon_chains(("u", "d", "d"), h)
    vhat = {
        "proton": {"g0": _std_vhat(pg0, q, qi, z, h), "g1": _std_vhat(pg1, q, qi, z, h)},
        "neutron": {"g0": _std_vhat(ng0, q, qi, z, h), "g1": _std_vhat(ng1, q, qi, z, h)},
    }
    z_bar = mp.mpf(1) / (mp.sqrt(qi) + mp.sqrt(q))  # = z (bar-symmetric)
    vhat_bar = {
        "proton": {
            "g0": _std_vhat(pg0, qi, q, z_bar, qi - q),
            "g1": _std_vhat(pg1, qi, q, z_bar, qi - q),
        },
        "neutron": {
            "g0": _std_vhat(ng0, qi, q, z_bar, qi - q),
            "g1": _std_vhat(ng1, qi, q, z_bar, qi - q),
        },
    }
    out["vhat_std_derived"] = {n: {g: str(v) for g, v in d.items()} for n, d in vhat.items()}
    out["vhat_std_bar_image_q_to_qinv"] = {
        n: {g: str(v) for g, v in d.items()} for n, d in vhat_bar.items()
    }
    out["prod_vhat_tr_m_check"] = {n: str(d["g0"] * d["g1"]) for n, d in vhat.items()}
    out["pn_signal_g0_relative"] = str(
        (vhat["proton"]["g0"] - vhat["neutron"]["g0"]) / vhat["neutron"]["g0"]
    )

    # === CANDIDATE 2 (CORE): analytic structure of Li_2^q past |z|=q ====
    analytic = {}
    for frac in ["0.5", "0.9", "0.99", "0.999"]:
        u = mp.mpf(frac) * q
        lg = q_log_lambert(u, q, qi)
        analytic[f"q_log_at_{frac}q"] = str(lg)
        analytic[f"li2q_integrand_at_{frac}q"] = str(-lg / u)
    for frac in ["0.5", "0.9"]:
        u = mp.mpf(frac) * q
        series_val = li_2_q(u, q, qi)
        cont_val = li_2_q_continued(u, q, qi)
        analytic[f"li2q_series_at_{frac}q"] = str(series_val)
        analytic[f"li2q_continued_at_{frac}q"] = str(mp.re(cont_val))
        analytic[f"overlap_match_at_{frac}q"] = str(mp.fabs(series_val - mp.re(cont_val)))
    # continued value at the genuine proton σ₀ factor |V̂_0|=1.1461 > q₀
    v0p = mp.fabs(vhat["proton"]["g0"])
    cont_v0 = li_2_q_continued(v0p, q, qi)
    analytic["proton_g0_vhat"] = str(v0p)
    analytic["proton_g0_over_q0"] = str(v0p / q)
    analytic["li2q_continued_at_proton_g0"] = str(cont_v0)
    analytic["li2q_continued_at_proton_g0_re"] = str(mp.re(cont_v0))
    analytic["li2q_continued_at_proton_g0_im"] = str(mp.im(cont_v0))
    analytic["singularity_class"] = (
        "ln_q(1−z) has a SIMPLE POLE at z=q (Lambert closed form); the "
        "integrand −ln_q(1−u)/u ~ (h/q)/(1−u/q)/u diverges like 1/(q−u). "
        "Li_2^q = −∫ of it ⇒ ∫du/(1−u/q) = −q·ln(1−u/q) → LOGARITHMIC "
        "singularity (branch point), INTEGRABLE. So z=q is NOT a pole of "
        "Li_2^q itself; Li_2^q is continuable past z=q with a branch cut on "
        "[q,∞). The +i0 continuation yields a finite complex value with a "
        "nonzero imaginary part for z>q."
    )
    out["candidate2_analytic_structure"] = analytic

    # === evaluate 4 candidates per generator (raw, incl |V̂|>q₀) ========
    cands = {}
    for cname, fn in [
        ("cand1_phi_q", cand1_phi_q),
        ("cand2_li2q_continued", cand2_li2q_continued),
        ("cand4_reciprocal", cand4_reciprocal),
    ]:
        cands[cname] = {}
        for nuc in ("proton", "neutron"):
            cands[cname][nuc] = {}
            for g in ("g0", "g1"):
                v = vhat[nuc][g]
                try:
                    val = fn(v, q, qi)
                    valr = mp.re(val) if mp.im(val) != 0 else val
                    cands[cname][nuc][g] = {
                        "vhat": str(v),
                        "F": str(valr),
                        "F_imag": str(mp.im(val)) if mp.im(val) != 0 else "0",
                        "finite": bool(mp.isfinite(valr)),
                    }
                except Exception as e:  # noqa: BLE001
                    cands[cname][nuc][g] = {"vhat": str(v), "F": "ERROR", "err": str(e)}

    cands["cand3_bar_sym"] = {}
    for nuc in ("proton", "neutron"):
        cands["cand3_bar_sym"][nuc] = {}
        for g in ("g0", "g1"):
            v = vhat[nuc][g]
            vb = vhat_bar[nuc][g]
            gm = mp.sqrt(mp.fabs(v) * mp.fabs(vb))
            cands["cand3_bar_sym"][nuc][g] = {
                "vhat": str(v),
                "vhat_bar": str(vb),
                "geom_mean_arg": str(gm),
                "F_on_bar_image": str(li_2_q(mp.fabs(vb), q, qi)),
                "F_on_geom_mean": str(li_2_q(gm, q, qi)),
                "bar_image_inside_radius": bool(mp.fabs(vb) < q),
                "geom_mean_inside_radius": bool(gm < q),
            }
    out["candidates"] = cands

    # === resulting raw dimensionless tower per candidate ===============
    def tower_dimensionless(nuc, Ffn):
        v0 = vhat[nuc]["g0"]
        v1 = vhat[nuc]["g1"]
        t1 = mp.fabs(v0 * v1)
        try:
            f0 = Ffn(v0, q, qi)
            f1 = Ffn(v1, q, qi)
            f01 = Ffn(v0 * v1, q, qi)
            f0, f1, f01 = (mp.re(x) for x in (f0, f1, f01))
            t2 = f0 + f1
            t3 = (z ** 2) * f01
            tot = t1 + t2 + t3
            return {
                "T1": str(t1), "T2": str(t2), "T3": str(t3),
                "tower_total": str(tot), "finite": bool(mp.isfinite(tot)),
            }
        except Exception as e:  # noqa: BLE001
            return {"error": str(e), "finite": False}

    towers = {}
    for cname, fn in [
        ("cand1_phi_q", cand1_phi_q),
        ("cand2_li2q_continued", cand2_li2q_continued),
        ("cand4_reciprocal", cand4_reciprocal),
        ("baseline_std_li2q", lambda v, q, qi: li_2_q(mp.fabs(v), q, qi)),
    ]:
        towers[cname] = {
            nuc: tower_dimensionless(nuc, fn) for nuc in ("proton", "neutron")
        }
    out["raw_towers_dimensionless"] = towers

    # candidate 3 tower (geom-mean argument, inside radius)
    def tower_bar_gm(nuc):
        v0 = vhat[nuc]["g0"]; v1 = vhat[nuc]["g1"]
        vb0 = vhat_bar[nuc]["g0"]; vb1 = vhat_bar[nuc]["g1"]
        gm0 = mp.sqrt(mp.fabs(v0) * mp.fabs(vb0))
        gm1 = mp.sqrt(mp.fabs(v1) * mp.fabs(vb1))
        gm01 = mp.sqrt(mp.fabs(v0 * v1) * mp.fabs(vb0 * vb1))
        t1 = mp.fabs(v0 * v1)
        t2 = li_2_q(gm0, q, qi) + li_2_q(gm1, q, qi)
        t3 = (z ** 2) * li_2_q(gm01, q, qi)
        tot = t1 + t2 + t3
        return {"T1": str(t1), "T2": str(t2), "T3": str(t3),
                "tower_total": str(tot), "finite": bool(mp.isfinite(tot))}
    towers["cand3_bar_sym"] = {nuc: tower_bar_gm(nuc) for nuc in ("proton", "neutron")}

    # p/n signal preservation per finite candidate
    out["pn_signal_per_candidate"] = {}
    for cname, d in towers.items():
        pp, nn = d["proton"], d["neutron"]
        if pp.get("finite") and nn.get("finite"):
            tp = mp.mpf(pp["tower_total"]); tn = mp.mpf(nn["tower_total"])
            out["pn_signal_per_candidate"][cname] = {
                "proton_tower": pp["tower_total"],
                "neutron_tower": nn["tower_total"],
                "pn_relative": str((tp - tn) / tn) if tn != 0 else "div0",
            }
        else:
            out["pn_signal_per_candidate"][cname] = {"finite": False}

    wpath = WitnessBuilder.wrap_legacy(
        "convergence-safe-vhat-tower",
        out,
        script_path=__file__,
        engine="mpmath",
    ).save()
    print(f"Wrote {wpath}")

    print("\n=== genuine derived V̂_i (std) ===")
    for n, d in vhat.items():
        print(f"  {n}: g0={float(d['g0']):.6f}  g1={float(d['g1']):.6f}  "
              f"∏={float(d['g0']*d['g1']):.6f}  (q₀={float(q):.5f})")
    print(f"  p/n g0 signal: {float(out['pn_signal_g0_relative'])*100:.2f}%")
    print("\n=== candidate 2 singularity class ===")
    print(" ", analytic["singularity_class"])
    print(f"  Li_2^q continued at proton g0 (|V̂|={float(v0p):.4f}>q₀): "
          f"re={float(mp.re(cont_v0)):.6f} im={float(mp.im(cont_v0)):.6f}")
    print("\n=== raw dimensionless towers (T1+T2+T3) ===")
    for cname, d in towers.items():
        for nuc in ("proton", "neutron"):
            r = d[nuc]
            tot = r.get("tower_total", r.get("error", "—"))
            print(f"  {cname:22s} {nuc:8s} total={str(tot)[:16]:>16}  finite={r.get('finite')}")
    print("\n=== p/n signal per candidate ===")
    for cname, d in out["pn_signal_per_candidate"].items():
        if "pn_relative" in d:
            print(f"  {cname:22s} p/n={float(d['pn_relative'])*100:+.3f}%")
        else:
            print(f"  {cname:22s} (divergent)")


if __name__ == "__main__":
    main()
