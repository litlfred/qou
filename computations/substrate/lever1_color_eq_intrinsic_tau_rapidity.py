"""Lever-1 (owner-ungated 2026-06-25), follow-up: the curve-INTRINSIC candidate for
theta_binding -- the Tate/multiplicative period 2*pi*Im(tau_E) of the color E_q.

Single PRE-REGISTERED principled candidate (no fishing):
  theta_cand(q) = 2*pi*Im(tau_E^reduced(q)),
calibrated by the substrate torus, where theta_torus = 2 log q0 = 2*pi*Im(tau_torus)
(Tate curve q_Tate = q0^2, tau_torus = log(q0^2)/(2 pi i)).

DECISIVE q-sensitivity test: theta_binding(q) = acosh(tau_binding(q)/2) genuinely moves
with q (0.7714 at q=1 -> 0.7815 at q0). A single-curve intrinsic invariant of the color
E_q is nearly q-independent (j: 128 -> 129.86 over [1,q0]). So we compute theta_cand at
BOTH q=1 and q0 and compare value AND q-slope to theta_binding. If theta_cand barely
moves and/or misses the value, the intrinsic-period reading is ruled out (scope-(a)),
completing the trilemma: theta_binding is neither loop-monodromy, nor path-transport,
nor single-curve intrinsic period -> it is the W_lambda-side localization (MTC matching),
not a color-E_q period.

tau_E via the elliptic modulus m = (e2-e3)/(e1-e3), tau = i K(1-m)/K(m); validated by
kleinj(tau) == j(curve). Reduced to the fundamental domain before taking Im.
"""
import json
import os
import mpmath as mp

mp.mp.dps = 30
# q₀ is READ from the canonical source, never typed here. It was a hardcoded
# literal "1.1099785955573347198997632204832250266562084087802" -- the MUON
# value -- while this producer's witness declared `q0Anchor: proton`. Declared
# anchor and computed value disagreed by 11.54 ppb, which is the mu-p substrate
# tension itself (AGENTS.md: "Never straddle the two layers inside one
# quantity", and the 2026-08-07 owner directive that all production code
# defaults to the experimental/proton anchor). Bean qou-bdkx.
from q_parameter import Q_MP as Q0  # noqa: E402 — canonical proton-pinned q₀

def pr(q):
    s = mp.sqrt(q)
    p = 2*(q**2 - q + 1)/(3*q) + (q - 1)/(3*s)
    r = (20*(q - 1)**3/(27*q**mp.mpf(1.5)) + 5*(q - 1)**2/(9*q)
         + 5*(s - 1/s)/9 + mp.mpf(20)/27)
    return p, r

def j_curve(q):
    p, r = pr(q)
    Delta = -16*(4*p**3 + 27*r**2)
    return -1728*(4*p)**3/Delta, p, r

def reduce_tau(tau):
    """Reduce tau to the fundamental domain (Im>0, Re in [-1/2,1/2], |tau|>=1)."""
    if mp.im(tau) < 0:
        tau = -tau
    for _ in range(200):
        tau = tau - mp.nint(mp.re(tau))           # |Re| <= 1/2
        if abs(tau) < 1 - mp.mpf("1e-30"):
            tau = -1/tau
        else:
            break
    return tau

def tau_E(q):
    p, r = pr(q)
    e1, e2, e3 = mp.polyroots([1, 0, p, r])       # x^3 + p x + r
    # put the real root first
    roots = [e1, e2, e3]
    reals = [z for z in roots if abs(mp.im(z)) < mp.mpf("1e-20")]
    comps = [z for z in roots if abs(mp.im(z)) >= mp.mpf("1e-20")]
    er = reals[0]
    if len(comps) == 2:
        ec1, ec2 = comps
    else:                                          # all real (Delta>0) fallback
        ec1, ec2 = [z for z in roots if z is not er][:2]
    m = (ec1 - ec2)/(er - ec2)
    tau = 1j * mp.ellipk(1 - m)/mp.ellipk(m)
    return reduce_tau(tau)

def report(q, label):
    j, p, r = j_curve(q)
    tau = tau_E(q)
    jchk = 1728*mp.kleinj(tau)            # mpmath.kleinj returns j/1728
    Imt = mp.im(tau)
    theta_cand = 2*mp.pi*Imt
    tau_binding = 3*(3*q**4 + 8*q**2 + 3)/(4*q*(q + 1)**2)
    theta_binding = mp.acosh(tau_binding/2)
    return {
        "label": label, "q": mp.nstr(q, 12),
        "j_curve": mp.nstr(mp.re(j), 8),
        "j_from_tau_kleinj": mp.nstr(mp.re(jchk), 8),
        "j_validates": bool(abs(mp.re(j) - mp.re(jchk)) < mp.mpf("1e-6")*abs(mp.re(j))),
        "tau_E": mp.nstr(tau, 10),
        "Im_tau_E": mp.nstr(Imt, 10),
        "theta_cand_2pi_Im": mp.nstr(theta_cand, 10),
        "theta_binding": mp.nstr(theta_binding, 10),
        "rel_err": float(abs(theta_cand - theta_binding)/abs(theta_binding)),
    }

r1 = report(mp.mpf(1), "classical q=1")
r0 = report(Q0, "substrate q0")

# q-slope decisiveness: how much does each move from q=1 to q0?
dtheta_binding = float(mp.mpf(r0["theta_binding"]) - mp.mpf(r1["theta_binding"]))
dtheta_cand = float(mp.mpf(r0["theta_cand_2pi_Im"]) - mp.mpf(r1["theta_cand_2pi_Im"]))

results = {"classical_q1": r1, "substrate_q0": r0,
           "dtheta_binding_q1_to_q0": dtheta_binding,
           "dtheta_cand_q1_to_q0": dtheta_cand,
           "theta_binding_q0": r0["theta_binding"], "theta_cand_q0": r0["theta_cand_2pi_Im"]}

hit_value = r0["rel_err"] < 0.01
# does the candidate track the q-dependence (same sign + within 3x magnitude)?
tracks_q = bool(dtheta_binding != 0 and dtheta_cand != 0
                and (dtheta_binding*dtheta_cand > 0)
                and (1/3 < abs(dtheta_cand/dtheta_binding) < 3))
assertions = {
    "tau_E_validated_by_kleinj_q1": r1["j_validates"],
    "tau_E_validated_by_kleinj_q0": r0["j_validates"],
    "theta_cand_matches_binding_value_1pct_q0": bool(hit_value),
    "theta_cand_tracks_binding_q_dependence": tracks_q,
}
solid = r1["j_validates"] and r0["j_validates"]
hit = hit_value and tracks_q
witness = {
    "computation": "lever1_color_eq_intrinsic_tau_rapidity",
    "description": (
        "Single pre-registered curve-intrinsic candidate for theta_binding: the Tate/"
        "multiplicative period theta_cand = 2 pi Im(tau_E) of the color E_q (torus-"
        "calibrated: theta_torus = 2 log q0 = 2 pi Im(tau_torus)). Decisive q-sensitivity "
        "test at q=1 vs q0: theta_binding(q) moves with q but a single-curve invariant of "
        "the barely-deformed color E_q (j: 128->129.86) does not. tau_E via m=(e2-e3)/"
        "(e1-e3), validated by kleinj(tau)=j."
    ),
    "discipline": (
        "no fit; mpmath 30dps; ONE pre-registered principled candidate (2 pi Im tau_E), "
        "reported hit/miss; tau_E independently validated by the Klein j-function. Decisive "
        "q-slope comparison rather than a single-point coincidence."
    ),
    "auditOnly": "docs/audits/2026-06-25-lever1-color-eq-lambda-sw-rapidity.md",
    "results": results, "assertions": assertions, "allPassed": bool(solid),
}
witness["verdict"] = (
    ("INTRINSIC MATCH: 2 pi Im(tau_E) reproduces theta_binding in value AND q-slope -- a "
     "curve-intrinsic candidate derivation (requires independent confirmation, tier near-match)."
     if hit else
     "INTRINSIC MISS (scope-(a) on the principled candidate): tau_E is validated (kleinj*1728=j "
     "to <1e-6), but the torus-calibrated candidate theta_cand = 2 pi Im(tau_E) = " +
     r0["theta_cand_2pi_Im"] + " misses theta_binding = " + r0["theta_binding"] +
     f" at q0 (6.5x), and its q-slope ({dtheta_cand:.2e}) is ~6x flatter than theta_binding's "
     f"({dtheta_binding:.2e}). Reason: Im(tau_E)~0.93 -> the color E_q is GENERIC, not near the "
     "Tate/cusp regime where the torus calibration (theta_torus=2 pi Im tau_torus, Im~0.03) lives. "
     "Scope (a): rules out THIS principled candidate, not every intrinsic invariant (a j-tuned one "
     "would be fishing). With the monodromy (integer-trace) and transport (too-small) negatives, "
     "the geometric origin of theta_binding is NOT a color-E_q period -- it points to the W_lambda-"
     "side Plancherel/MTC localization (keystone residual i, the already-open frontier).")
    + " No fit; nothing wired."
)
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
# Flat `assertions` payload → stamp (not wrap_legacy) preserves it.
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__), "lever1-color-eq-intrinsic-tau-rapidity.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, default=str)

for r in (r1, r0):
    print(f"[{r['label']}] j={r['j_curve']} (kleinj {r['j_from_tau_kleinj']}, ok={r['j_validates']})")
    print(f"    tau_E={r['tau_E']}  Im={r['Im_tau_E']}")
    print(f"    theta_cand(2pi Im)={r['theta_cand_2pi_Im']}   theta_binding={r['theta_binding']}   rel={r['rel_err']:.4f}")
print(f"\nq-slope: dtheta_binding={dtheta_binding:.3e}  dtheta_cand={dtheta_cand:.3e}")
for k, v in assertions.items():
    print(f"  [{'PASS' if v else '----'}] {k}")
print(f"\nverdict: {witness['verdict']}\nwitness -> {out}")
