#!/usr/bin/env python3
r"""
q0-varies / Im(q) as the c3 anchor-carrier — the FALSIFIABLE test (2026-07-26).

Owner reframe (capstone #4297): q0 is our LOCAL measured substrate value, a field
that VARIES and generically carries Im(q) != 0.  #4293 proved the bar-odd phase
channel S(r,phi) = (sqrt3/2) r^2 sin(2 phi), phi = arg(u), u = 2 log q0, is a
MAXIMAL-leverage DOF (dS/dphi|0 = sqrt3 r^2 != 0) that is FROZEN at strictly real
q0 (arg(u) = 0).  Allow Im(q0) != 0 -> arg(u) != 0 -> the phase UNFREEZES.

THE FALSIFIABLE TEST (this probe): does ONE substrate Im(q0) reproduce the c3
anchor-swing CONSISTENTLY across BOTH anchors (a MEASUREMENT of Im(q0) -> lead),
or does it require a DIFFERENT Im(q) per anchor (a per-anchor FIT / unfalsifiable
knob -> the honesty guardrail fires)?

Method (no fit, nothing inverted to DEFINE Im(q)):
  1. arg(u) <-> Im(q0):  u = 2 log(qr + i*qi).  Compute arg(u) exactly (mpmath)
     and its leading slope  d arg(u)/d qi |_{qi=0} = 1/(qr log qr).
  2. Linear response coefficient  k = dS_phase/d(Im q)|0 = sqrt3 * r^2 / (qr log qr)
     = 4 sqrt3 log(qr) / qr   (r = |u| = 2 log qr at qi=0).  k is anchor-INVARIANT
     to the 22 ppb qr difference -> the (swing)/(Im q0) ratio is the SAME at both
     anchors: the model MEASURES Im(q0) faithfully.  Good news for "measurement".
  3. BUT the two anchors share qr to ~22 ppb, so a SINGLE global Im(q0) gives the
     SAME S at both -> swing driven only by the qr difference:
        swing_global = [k(qr_p) - k(qr_m)] * eps  ~  eps * dk/dqr * Delta_qr .
     Compare to the observed |Sp - Sm|.  This is the #4293 dS/dphi meeting the
     SRigidity 'no_anchor_invariant_realizes_swing' obstruction (dc3/dq ~ 4.6e6).
  4. Per-anchor Im(q) REQUIRED to hit each residual directly:
        eps_p = Sp/k ,  eps_m = Sm/k .  Report their sign + magnitude ratio.
     sign S = sign eps (merged fig8Trace_im_odd) => Sp<0<Sm forces eps_p<0<eps_m.

Verdict logic:
  - global-Im swing / observed swing  ->  ORDER-MISMATCH factor (expect ~1e-6..1e-7).
  - required per-anchor eps  ->  opposite sign, O(1e-2) FREE magnitude (no derived
    scale) => the unfalsifiable-knob / FIT outcome.

NOTHING is wired; NO residual is inverted to define a canonical Im(q).  This probe
MEASURES the gap between the reframe and #4293's proved dS/dphi and returns an
honest verdict.
"""
from __future__ import annotations
import json, hashlib, subprocess, datetime, pathlib
import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# ---- inputs (documented, NOT tuned) -----------------------------------------
# c3 bar-odd residuals S at the two anchors (session brief; capstone #4297).
S_proton = mp.mpf("-0.0395")
S_muon   = mp.mpf("+0.0097")
# substrate q0 real part and the anchor separation (AGENTS.md / coordination doc).
# proton-pin q0 ~ 1.10998 ; muon-pin differs by ~22 ppb.  Exact digits are not
# load-bearing for the order verdict; the 22 ppb separation is.
qr_proton = mp.mpf("1.10998")
ppb = mp.mpf("22e-9")                       # muon<->proton anchor separation
qr_muon   = qr_proton * (1 - ppb)           # muon pin slightly below (sign irrelevant to |order|)

def arg_u(qr, qi):
    """Exact arg(u), u = 2 log(qr + i qi)."""
    q = mp.mpc(qr, qi)
    u = 2 * mp.log(q)
    return mp.arg(u)

def r_of(qr, qi):
    q = mp.mpc(qr, qi)
    return abs(2 * mp.log(q))

def nz_im_volume(r, phi):
    """#4293 nzImVolume: (sqrt3/2) r^2 sin(2 phi)."""
    return (mp.sqrt(3) / 2) * r**2 * mp.sin(2 * phi)

def S_phase_exact(qr, qi):
    """Full (non-linearized) phase-channel response at complex q0 = qr + i qi."""
    return nz_im_volume(r_of(qr, qi), arg_u(qr, qi))

def k_slope(qr):
    """Analytic linear-response coeff k = dS_phase/d(Im q)|0 = 4 sqrt3 log(qr)/qr."""
    return 4 * mp.sqrt(3) * mp.log(qr) / qr

# ---- 1. arg(u) <-> Im(q0) slope check (exact vs analytic) --------------------
h = mp.mpf("1e-20")
dargu_num = (arg_u(qr_proton, h) - arg_u(qr_proton, -h)) / (2 * h)
dargu_ana = 1 / (qr_proton * mp.log(qr_proton))

# ---- 2. linear response coefficient (analytic) + numeric confirmation --------
k_p = k_slope(qr_proton)
k_m = k_slope(qr_muon)
dSphase_num = (S_phase_exact(qr_proton, h) - S_phase_exact(qr_proton, -h)) / (2 * h)

# ---- 3. single global Im(q0): swing driven only by qr difference -------------
# choose eps = the fitted magnitude scale (|eps_p|) so the comparison is generous.
eps_fit = abs(S_proton) / k_p
swing_global_at_epsfit = (k_p - k_m) * eps_fit          # linear estimate
# exact: same global qi at both anchors, full response
qi_glob = eps_fit
swing_global_exact = S_phase_exact(qr_proton, qi_glob) - S_phase_exact(qr_muon, qi_glob)
swing_observed = S_proton - S_muon
order_mismatch = abs(swing_observed) / abs(swing_global_exact)

# max |S_phase| the channel can supply at fixed r=2 log qr (amplitude ceiling)
amp_ceiling = (mp.sqrt(3) / 2) * (2 * mp.log(qr_proton))**2

# ---- 4. per-anchor Im(q) required (the FIT) ----------------------------------
eps_p = S_proton / k_p
eps_m = S_muon / k_m
sign_opposite = (eps_p < 0) and (eps_m > 0)
mag_ratio = abs(eps_p) / abs(eps_m)
eps_p_rel = eps_p / qr_proton     # Im(q)/Re(q) needed at proton anchor
eps_m_rel = eps_m / qr_muon

# ---- verdict -----------------------------------------------------------------
# single global Im(q0) reproduces the swing consistently?  -> only if order_mismatch ~ 1
global_consistent = order_mismatch < 10
verdict = ("CONSTRAINED-LEAD" if global_consistent
           else "UNFALSIFIABLE-KNOB/FIT + ORDER-MISMATCH-WALL")

def f(x, n=6):
    return mp.nstr(x, n)

print("=" * 74)
print("q0-varies / Im(q) c3 anchor-carrier — FALSIFIABLE TEST")
print("=" * 74)
print(f"[1] d arg(u)/d(Im q)|0   numeric={f(dargu_num)}  analytic 1/(qr log qr)={f(dargu_ana)}")
print(f"[2] k = dS_phase/d(Im q)|0  analytic={f(k_p)}  numeric={f(dSphase_num)}  (k_muon={f(k_m)})")
print(f"    -> (swing)/(Im q0) ratio IDENTICAL across anchors to (k_p-k_m)/k_p = {f((k_p-k_m)/k_p,3)}")
print(f"[3] GLOBAL single Im(q0)=eps_fit={f(eps_fit)}:")
print(f"    swing_global(exact) = {f(swing_global_exact)}   observed |Sp-Sm| = {f(swing_observed)}")
print(f"    ORDER-MISMATCH factor = observed/global = {f(order_mismatch,4)}   (amp ceiling {f(amp_ceiling,4)})")
print(f"[4] PER-ANCHOR Im(q) required:  eps_p={f(eps_p)} ({f(eps_p_rel,3)} of qr)   eps_m={f(eps_m)} ({f(eps_m_rel,3)} of qr)")
print(f"    opposite-sign (fig8 parity) = {sign_opposite}   |eps_p/eps_m| = {f(mag_ratio,4)}")
print("-" * 74)
print(f"VERDICT: {verdict}")
print("  single global Im(q0) is ~{:.2e}x too small (order-mismatch wall);".format(float(order_mismatch)))
print("  reaching the swing needs a DIFFERENT Im(q) per anchor (opposite sign,")
print("  ~{:.1f}x magnitude), a FREE O(1e-2) knob with no derived scale -> FIT.".format(float(mag_ratio)))
print("=" * 74)

# ---- witness -----------------------------------------------------------------
def git(*a):
    try:
        return subprocess.check_output(["git", *a], cwd=pathlib.Path(__file__).resolve().parents[2]).decode().strip()
    except Exception:
        return None

src = pathlib.Path(__file__).read_bytes()
witness = {
    "schema": "witness/v1",
    "name": "qbeta-imq-anchor-carrier",
    "description": "Falsifiable test of the q0-varies/Im(q) reframe against #4293's proved dS/dphi: "
                   "single global Im(q0) vs per-anchor Im(q) for the c3 bar-odd anchor-swing. "
                   "No fit; nothing inverted to define Im(q); MEASURES the gap and returns an honest verdict.",
    "computation": {"script": "computations/qbeta/qbeta_imq_anchor_carrier_probe.py"},
    "witness": {
        "scriptCommitSha": git("log", "-1", "--format=%H", "--", "computations/qbeta/qbeta_imq_anchor_carrier_probe.py"),
        "scriptHash": hashlib.sha256(src).hexdigest()[:16],
    },
    "inputs": {
        "S_proton": str(S_proton), "S_muon": str(S_muon),
        "qr_proton": str(qr_proton), "anchor_sep_ppb": str(ppb),
        "note": "S residuals + qr from capstone #4297 / AGENTS.md; NOT tuned; NOT inverted.",
    },
    "results": {
        "dargu_dImq_slope": f(dargu_ana, 12),
        "dargu_dImq_slope_numeric_check": f(dargu_num, 12),
        "k_linear_response": f(k_p, 12),
        "k_linear_response_numeric_check": f(dSphase_num, 12),
        "k_muon": f(k_m, 12),
        "k_anchor_relative_diff": f((k_p - k_m) / k_p, 6),
        "global_Im_eps_used": f(eps_fit, 12),
        "swing_global_exact": f(swing_global_exact, 12),
        "swing_observed": f(swing_observed, 12),
        "order_mismatch_factor": f(order_mismatch, 6),
        "amplitude_ceiling_fixed_r": f(amp_ceiling, 6),
        "eps_proton_required": f(eps_p, 12),
        "eps_muon_required": f(eps_m, 12),
        "eps_proton_rel_to_qr": f(eps_p_rel, 6),
        "eps_muon_rel_to_qr": f(eps_m_rel, 6),
        "required_opposite_sign": sign_opposite,
        "required_magnitude_ratio": f(mag_ratio, 6),
    },
    "verdict": verdict,
    "verdict_detail": {
        "single_global_Im_reproduces_swing_consistently": bool(global_consistent),
        "global_Im_order_mismatch": f(order_mismatch, 6),
        "per_anchor_Im_required": True,
        "per_anchor_Im_is_free_scale": True,
        "Im_scale_derived_or_bounded": False,
        "scope": "(a) scope-limited negative: the Im(q) phase channel ALONE, with a single "
                 "substrate Im(q0), does not reproduce the c3 swing (order-mismatch ~1e6-1e7); "
                 "reproducing it requires per-anchor Im(q) = a FIT. No structural-(b) exclusion "
                 "of Im(q) as an INGREDIENT is claimed.",
    },
    "discipline": "no fit; no residual inverted to define Im(q); nothing wired; "
                  "conj:algebraic-geometric-dilog-equivalence stays OPEN.",
    "refs": [
        "QOU.QBeta.ArgUPhaseBranchSelection (#4293, sorry-free): dS/dphi|0 = sqrt3 r^2, arg(u)=0 real",
        "QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing (scope-(b)): anchor-invariant datum cannot swing",
        "QOU.QBeta.fig8Trace_im_odd (#3600): sign S = sign Im(q)",
        "docs/audits/2026-07-25-c3-categorical-exclusion-capstone.md",
    ],
    "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
}
out = pathlib.Path(__file__).with_name("qbeta_imq_anchor_carrier.witness.json")
out.write_text(json.dumps(witness, indent=2) + "\n")
print(f"witness -> {out}")
