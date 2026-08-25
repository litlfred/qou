#!/usr/bin/env python3
"""deuteron_coupling_s00_probe.py

Derive-or-refute for an INDEPENDENT deuteron entanglement coupling x ~ 1/sqrt(2)
(Target 2 of 2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md).
The full trans-series probe (deuteron_wall_full_transseries_probe.py) showed the
level-1/2 Borel-Laplace median resummation of the Gevrey-1/2 binding period
undershoots B_D ~37x at every substrate coupling, and flagged that pinning
x = 1/sqrt(2) (the Borel radius) by fiat would be circular. This probe asks:
does the corpus supply a DERIVED quantity equal to 1/sqrt(2) that could serve as
the entanglement coupling of the Hopf (two-nucleon) bipartition?

SYMBOLIC candidates (checked exactly before any numerics — formalize-first):

  (C2) S-matrix / Verlinde amplitude of the n=2 bipartition. The corpus keystone
       object bwS0(lambda) = d_q(lambda)/D (KeystoneVerlindeSMatrixBridge.lean;
       W_lambda = d_q^2/D^2 the MTC Plancherel measure). At n = 2 the two
       Wedderburn blocks (2), (1,1) both have d_q = 1 at EVERY q (Lean-witnessed:
       WLambdaMTCLocalizationObligation.lean non-vacuity witness), so D = sqrt(2)
       and  S_00(n=2) = 1/sqrt(2)  EXACTLY, q-independent. Equivalently the
       Hopf-pair reduced density matrix eigenvalues are W_lambda = (1/2, 1/2)
       (maximally-entangled two-block bipartition, Schmidt amplitudes 1/sqrt(2),
       entanglement entropy ln 2). This is the SU(2)_1-style exact match.
  (C1) Hopf-link Jones / Markov trace: J_Hopf(q) = -(q + 1/q) = -[2]_q, so
       J_Hopf(1) = -2 exactly and |J_Hopf(1)|^(-1/2) = 1/sqrt(2) exactly;
       at q0: 1/sqrt([2]_{q0}) = 0.70519 (-0.27% from 1/sqrt(2)). The inverse-
       square-root transform is unmotivated -> relabel, kept for the record.
  (C4) Canonical Markov trace parameter z = 1/[2]_v, v = sqrt(q0): z(q=1) = 1/2
       exactly, sqrt(z(1)) = 1/sqrt(2) exactly; sqrt(z(q0)) = 0.70663 (-0.07%).
       Same unmotivated-square-root objection. Fusion-frame g = 1/sqrt(1+[2]_v^2)
       = 1/sqrt(5) at q=1 (0.447) — NOT 1/sqrt(2). Bare substrate constants
       (hbar_q, hbar_q^2, t = ln q0, E0 = (q-1/q)/2, mu0/m_e) are all far from
       0.707 (no combination hits it without tuning).
  (C3) Geometric/cusp route: the Hopf link is NOT hyperbolic (Vol = 0, Seifert
       fibered) — no cusp moduli exist; the geometric route is structurally empty.
  (C5) Bridge Stokes datum A_omega = 4*sqrt(2)*e^(-3/8): its sqrt(2) IS the
       period's own singularity data — circular by construction, not independent.

NUMERIC refutation (the decisive part). Even GRANTING the best candidate
x = S_00 = 1/sqrt(2), the median Borel-Laplace sum gives m_e*ReP = 0.44 MeV at
eps = 0.02 (20% of B_D; the value is eps-prescription-sensitive because the
coupling sits exactly ON the singularity: 0.38 -> 0.92 MeV over eps = 0.1 ->
0.002, the jump at eps <= 0.005 being the contour slipping past a Pade pole —
still <= 41% of B_D). Moreover a scan over the WHOLE coupling axis shows the
median sum PLATEAUS: global max ~0.46 MeV ~ 21% of B_D near x ~ 0.6, then
decreases. So the premise of Target 2 — "the resummation reaches B_D as
x -> 1/sqrt(2)" (extrapolated in #3736 from an x <= 0.5 table) — is CORRECTED:
the median resummation never reaches B_D at ANY coupling. No derived x can
close this route; the gate dissolves.

VERDICT (scope-(a), no fit): the corpus DOES supply an exact, independent,
q-independent 1/sqrt(2) — the Verlinde/bwS0 vacuum amplitude S_00 = d_q/D of the
n=2 (Hopf) bipartition, with Hopf-pair reduced-density eigenvalues (1/2,1/2) —
but (i) identifying the trans-series coupling with the bipartition amplitude is
currently a RELABEL (no derivation that the Borel-Laplace expansion variable is
the Schmidt/S-matrix amplitude; S_00 lives at the fibre root-of-unity level
while the coupling is archimedean — exactly the standing bwS0_eq_hecke
archimedean-continuation open), and (ii) even granting it, the resummation at
x = 1/sqrt(2) undershoots B_D by 2.4-5x, and undershoots at every other x too.
The two sqrt(2)'s share an origin (the Borel radius 1/sqrt(2) comes from the
2-cycle term x^2/2 of the involution EGF e^{x+x^2/2}; S_00's sqrt(2) from the 2
blocks of n=2 — both are "the 2 of the two-body system"), which explains the
coincidence without supplying a closure. The deuteron resummation route stays
closed; the working channel remains the q-rotational mu0*hbar_q*J_q^2 (-9%,
0 params). No wiring; no tier change.
"""
import sys
import json
import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "qou-substrate" / "python"))
import mpmath as mp  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def main() -> int:
    q0 = q_at(30)
    me = mp.mpf('0.51099895069')
    B_D = mp.mpf('2.22452')
    s2 = 1 / mp.sqrt(2)

    # ---------- symbolic candidate checks (exact, before numerics) ----------
    # C2: S_00(n=2) = d_q/D with d_q((2)) = d_q((1,1)) = 1 for every q, D^2 = 2.
    dq_blocks_n2 = [mp.mpf(1), mp.mpf(1)]            # Lean-witnessed (all d_q = 1)
    D2 = sum(d ** 2 for d in dq_blocks_n2)           # = 2 exactly
    S00 = dq_blocks_n2[0] / mp.sqrt(D2)
    c2_exact = abs(2 * S00 ** 2 - 1) < mp.mpf('1e-25')
    W_lam = [float(d ** 2 / D2) for d in dq_blocks_n2]   # (1/2, 1/2)

    # C1: J_Hopf(q) = -(q + 1/q); classical value and substrate transform.
    J1 = -(mp.mpf(1) + 1 / mp.mpf(1))
    c1_exact = (J1 == -2)
    x_c1 = 1 / mp.sqrt(q0 + 1 / q0)                  # 1/sqrt([2]_{q0})

    # C4: Markov trace parameter z = 1/[2]_v, v = sqrt(q0); fusion g; constants.
    v = mp.sqrt(q0)
    z = 1 / (v + 1 / v)
    x_c4 = mp.sqrt(z)
    g_fusion = 1 / mp.sqrt(1 + (v + 1 / v) ** 2)     # = 1/sqrt(5) at q=1
    hbar = 1 - 1 / q0
    t = mp.log(q0)
    E0 = (q0 - 1 / q0) / 2
    mu0_over_me = 2 / (3 * (q0 - 1 / q0))

    sym_rows = {
        "C2_S00_n2": {"value": mp.nstr(S00, 10), "dev_from_inv_sqrt2": "0 (exact, q-independent)",
                      "source": "bwS0 = d_q/D at n=2; WLambdaMTCLocalizationObligation.lean (all d_q = 1)"},
        "C1_inv_sqrt_J_Hopf_q0": {"value": mp.nstr(x_c1, 10),
                                  "dev_from_inv_sqrt2": mp.nstr((x_c1 / s2 - 1) * 100, 4) + " %",
                                  "source": "J_Hopf(q) = -[2]_q; unmotivated ^(-1/2) transform"},
        "C4_sqrt_z_markov": {"value": mp.nstr(x_c4, 10),
                             "dev_from_inv_sqrt2": mp.nstr((x_c4 / s2 - 1) * 100, 4) + " %",
                             "source": "z = 1/[2]_v canonical Markov parameter; unmotivated sqrt"},
        "C4_fusion_g": {"value": mp.nstr(g_fusion, 10),
                        "dev_from_inv_sqrt2": mp.nstr((g_fusion / s2 - 1) * 100, 4) + " %",
                        "source": "1/sqrt(1+[2]_v^2) = 1/sqrt(5) at q=1 — not 1/sqrt(2)"},
        "substrate_constants": {"hbar_q": mp.nstr(hbar, 8), "hbar_q^2": mp.nstr(hbar ** 2, 8),
                                "t=ln q0": mp.nstr(t, 8), "E0": mp.nstr(E0, 8),
                                "mu0/m_e": mp.nstr(mu0_over_me, 8),
                                "note": "none near 0.707 without tuning"},
        "C3_geometric": "empty — Hopf link non-hyperbolic (Vol = 0, Seifert fibered), no cusp moduli",
        "C5_A_omega": "4*sqrt(2)*e^(-3/8) = 3.888 — the period's own Stokes datum, circular",
    }

    # ---------- trans-series machinery (identical to the full probe) ----------
    N = 42
    I = [mp.mpf(1), mp.mpf(1)]
    for n in range(2, N + 1):
        I.append(I[-1] + (n - 1) * I[-2])              # involution numbers
    b = [mp.mpf(0)] + [(I[n] / n) / mp.gamma(mp.mpf(n) / 2 + 1) for n in range(1, N + 1)]
    p, qd = mp.pade(b, N // 2, N // 2)

    def Bhat(xi):
        return mp.polyval(p[::-1], xi) / mp.polyval(qd[::-1], xi)

    def P(x, eps):
        return mp.quad(lambda u: mp.e ** (-u) * Bhat(x * mp.sqrt(u) * mp.e ** (1j * eps)),
                       [0, 1, 4, 12, 40])

    def med(x, eps):
        Pp, Pm = P(x, eps), P(x, -eps)
        return mp.re((Pp + Pm) / 2), abs(mp.im((Pp - Pm) / 2))

    print("=" * 74)
    print(" deuteron entanglement coupling x ~ 1/sqrt(2): derive-or-refute")
    print("=" * 74)
    for k, r in sym_rows.items():
        print(f"  {k}: {r}")

    # eps-prescription sensitivity AT the derived coupling (on-singularity)
    eps_rows = {}
    for eps in ('0.1', '0.05', '0.02', '0.01', '0.005', '0.002'):
        m, j = med(s2, mp.mpf(eps))
        eps_rows[eps] = {"m_e_ReP_MeV": mp.nstr(me * m, 6), "pct_of_B_D": mp.nstr(me * m / B_D * 100, 4),
                         "m_e_jump_MeV": mp.nstr(me * j, 5)}
        print(f"  x=1/sqrt2, eps={eps:>5}: m_e*ReP={mp.nstr(me*m,6):>9} MeV "
              f"({mp.nstr(me*m/B_D*100,4)}% of B_D)  jump={mp.nstr(me*j,4)}")
    at_s00_eps02 = me * med(s2, mp.mpf('0.02'))[0]

    # whole-axis plateau scan (corrects the #3736 "reaches B_D as x->1/sqrt2" extrapolation)
    scan_rows = {}
    gmax = mp.mpf(0)
    gmax_x = None
    for xv in ('0.40', '0.50', '0.55', '0.58', '0.60', '0.62', '0.65', '0.70',
               '0.7071', '0.75', '0.85', '1.0', '1.5', '2.0'):
        m, j = med(mp.mpf(xv), mp.mpf('0.02'))
        Bv = me * m
        scan_rows[xv] = {"m_e_ReP_MeV": mp.nstr(Bv, 6), "pct_of_B_D": mp.nstr(Bv / B_D * 100, 4)}
        if Bv > gmax:
            gmax, gmax_x = Bv, xv
        print(f"  scan x={xv:<7} m_e*ReP={mp.nstr(Bv,6):>9} MeV ({mp.nstr(Bv/B_D*100,4)}% of B_D)")
    print(f"\n  global max of median over coupling axis: {mp.nstr(gmax,5)} MeV "
          f"= {mp.nstr(gmax/B_D*100,4)}% of B_D at x = {gmax_x}")

    verdict = (
        "Scope-(a) NEGATIVE, with one exact symbolic survivor that still fails numerically. "
        "The corpus supplies an independent, derived, q-independent 1/sqrt(2): the Verlinde/bwS0 "
        "vacuum amplitude S_00 = d_q/D of the n=2 (Hopf) bipartition — both blocks have d_q = 1 "
        "(Lean-witnessed), D = sqrt(2), reduced-density eigenvalues (1/2, 1/2), Schmidt amplitude "
        "1/sqrt(2), entanglement entropy ln 2. But identifying the Borel-Laplace coupling with this "
        "bipartition amplitude is a relabel (no derivation; and S_00 is a fibre root-of-unity object "
        "while the coupling is archimedean — the standing bwS0_eq_hecke continuation open). "
        "Decisively: even granting x = 1/sqrt(2), the median resummation gives 0.44 MeV at eps=0.02 "
        "(20% of B_D; eps-sensitive 0.38-0.92 MeV, <= 41%, because the coupling sits ON the "
        "singularity), and the median sum's global max over the WHOLE coupling axis is ~0.46 MeV "
        "~ 21% of B_D (plateau near x ~ 0.6) — it never reaches B_D at any coupling. This corrects "
        "the #3736 extrapolation ('reaches B_D as x -> 1/sqrt2') and dissolves Target 2's gate: no "
        "coupling derivation can close the resummation route. The two sqrt(2)'s share an origin "
        "(pair structure: the x^2/2 2-cycle term of the involution EGF vs the 2 blocks of n=2) — "
        "a shared origin, not an identification. Working deuteron channel remains the q-rotational "
        "mu0*hbar_q*J_q^2 (-9%, 0 params). No fit; no wiring; no tier change."
    )
    print("\nVERDICT:", verdict)

    wit = {
        "computation": "deuteron-coupling-s00-derive-or-refute",
        "description": "Derive-or-refute of an independent deuteron entanglement coupling "
                       "x ~ 1/sqrt(2) for the Gevrey-1/2 trans-series route. Symbolic survivor: "
                       "S_00(n=2) = d_q/D = 1/sqrt(2) exact (bwS0 at n=2, all d_q = 1, "
                       "Lean-witnessed). Numeric refutation: median Borel-Laplace at x=1/sqrt(2) "
                       "gives <= 41% of B_D (eps-prescription-sensitive, on-singularity) and the "
                       "median sum plateaus at ~21% of B_D over the whole coupling axis — the "
                       "resummation never reaches B_D at any coupling. Scope-(a); no fit.",
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath", "engineVersion": mp.__version__,
        "target_B_D_MeV": mp.nstr(B_D, 6),
        "symbolic_candidates": sym_rows,
        "W_lambda_n2": W_lam,
        "resummation_at_inv_sqrt2_by_eps": eps_rows,
        "coupling_axis_scan_eps_0p02": scan_rows,
        "global_max_median_MeV": mp.nstr(gmax, 6),
        "global_max_median_pct_of_B_D": mp.nstr(gmax / B_D * 100, 4),
        "verdict": verdict,
        "scope": "(a) — exact symbolic 1/sqrt(2) exists (S_00 at n=2) but its identification with "
                 "the trans-series coupling is underived (relabel; fibre-vs-archimedean gap), and "
                 "even granted it the resummation undershoots 2.4-5x; the median sum never reaches "
                 "B_D at any coupling (plateau ~21%)",
        "assertions": [
            {"label": "S_00(n=2) = 1/sqrt(2) exactly (2*S00^2 = 1)", "passed": bool(c2_exact)},
            {"label": "J_Hopf(q=1) = -2 exactly", "passed": bool(c1_exact)},
            {"label": "median at derived x=1/sqrt(2), eps=0.02 undershoots (< B_D/2)",
             "passed": bool(at_s00_eps02 < B_D / 2)},
            {"label": "median plateau: global max over coupling axis < B_D/3",
             "passed": bool(gmax < B_D / 3)},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(wit, script_path=__file__, engine="mpmath")
    wit["scriptFile"] = Path(__file__).name
    out = Path(__file__).resolve().parent / "deuteron-coupling-s00-derive-or-refute.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    print("\nwitness ->", out.name, " allPassed:", wit["allPassed"])
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
