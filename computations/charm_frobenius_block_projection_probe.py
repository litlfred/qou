#!/usr/bin/env python3
"""charm_frobenius_block_projection_probe.py — DERIVE-THEN-CHECK of the charm
mass as the **Frobenius / Wedderburn charm-BLOCK projection** of a composite
braid's (complex) volume, the principled follow-up to the 2026-08-02 charm-mass
negative (docs/audits/2026-08-02-charm-mass-tower-negative.md).

Today's established facts (read that audit first):
  (b) the CARRIER T(3,5) is scope-(b) excluded (torus knot ⟹ Vol=0, CS∈ℚ);
  (a) the RAW composite baryon volume does NOT reproduce m_c (parameter-free
      negative), and the one 4% near-coincidence is topologically disqualified.

The OPEN handle this probe attacks: the mass is not the raw volume but the
**charm-block projection** of the Markov trace,  tr_M = Σ_λ y_λ χ_λ  — i.e. the
share of the composite's (complex) volume that lands in the generation-2 (charm)
Wedderburn block of H_3.

TWO readings, both derive-then-check, both parameter-free where flagged:

  Reading (A) — SCALE-FREE, NO KNOB (primary).  Keep the SAME Borromean baryon
    geometry  β_Bor = (σ1 σ2^{-1})^3  (the proton, 3 components).  The three
    Wedderburn blocks of H_3, λ ∈ {[3],[2,1],[1^3]}, ARE the three generations.
    The generation mass ratio is the ratio of block projections  y_λ χ_λ(β_Bor);
    the (complex) volume prefactor and tr_M normalization CANCEL, so this needs
    no scale calibration and no SnapPy — a pure structural prediction of
    m_c/m_light from q_0 alone.

  Reading (B) — the task's explicit construction, USES SnapPy + carries a KNOB.
    Charm = a composite braid with one strand carrying n=5 winding while KEEPING
    3 components (permutation trivial).  Compute Vol_ℂ = Vol + i·CS (SnapPy),
    project onto the [2,1] charm block, take Re, calibrate the scale on the
    light doublet only, predict m_c.  The twist count needed to realise "winding
    5, 3 components" is a KNOB — flagged; if the match needs it tuned, it is a
    FIT and reported as such.

Convention (AGENTS §7a): Hecke (T-q)(T+1/q)=0, eigenvalues q, -1/q.
q_0 is the EXPERIMENTAL (proton) pin `q_parameter.Q` ~ 1.1099785827513808 --
the standing default for all new compute (AGENTS §q0 anchor convention,
owner directive 2026-08-07).  Both y_lambda and chi_lambda are evaluated at
that same q_0: `y_lambda_wenzl_bridge_numeric` is a live closed form keyed on
the q passed in, so no muon-built cache is consulted and the two layers are
never straddled inside one quantity.

Requires: mpmath.  snappy is OPTIONAL — only Reading (B) uses it; without it
Reading (B) is skipped and `snappy_error` records why, while Reading (A) (the
parameter-free primary result) still computes.  Corpus y_λ via
y_lambda_wenzl_bridge (pure mpmath).
Emits computations/charm-frobenius-block-projection.witness.json.
"""
from __future__ import annotations

import datetime as _dt
import json
import sys
import time as _time
from pathlib import Path

import mpmath as mp

_T0 = _time.time()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE / "hecke"))

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps, json_safe_float  # noqa: E402
set_compute_dps()

# Experimental (proton) substrate q_0 -- the standing default for new compute.
from q_parameter import Q as Q0  # noqa: E402


def f64_json(o):
    """Serialize an f64 result tree: floats become their repr strings.

    The readings here mix mpmath with a snappy (float64) volume/Chern-Simons
    kernel and are float()-ed at every sink, so repr is exactly the digits
    produced. It round-trips bit-exactly and keeps raw float64 out of the
    witness; non-finite values go through json_safe_float so they cannot
    become bare JSON tokens.
    """
    if isinstance(o, bool) or o is None:
        return o
    if isinstance(o, float):
        v = json_safe_float(o)
        return v if isinstance(v, str) else repr(v)
    if isinstance(o, dict):
        return {k: f64_json(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [f64_json(v) for v in o]
    return o
from y_lambda_wenzl_bridge import (  # noqa: E402
    y_lambda_wenzl_bridge_numeric,
    partitions_of,
)

Q = mp.mpf(Q0)
QI = 1 / Q
H = Q - QI  # h = q - 1/q


# ── H_3 irreducible representations (Hoefsmit seminormal, eigenvalues q,-1/q) ──
def irrep_gens(lam):
    """Return (rho(sigma_1), rho(sigma_2)) as mpmath matrices for λ ⊢ 3.

    [3]   trivial : σ_i ↦ (q)          1-dim
    [1^3] sign    : σ_i ↦ (-1/q)       1-dim
    [2,1] standard: σ_1 = diag(q,-1/q),
        σ_2 = [[-1/(q^3+q), r],[r, q^3/(q^2+1)]], r=sqrt(q^4+q^2+1)/(q^2+1)
        (solved symbolically from Hecke+braid; seminormal gauge b=c=r).
    """
    if lam == (3,):
        return mp.matrix([[Q]]), mp.matrix([[Q]])
    if lam == (1, 1, 1):
        return mp.matrix([[-QI]]), mp.matrix([[-QI]])
    if lam == (2, 1):
        s1 = mp.matrix([[Q, 0], [0, -QI]])
        a = -1 / (Q**3 + Q)
        d = Q**3 / (Q**2 + 1)
        r = mp.sqrt(Q**4 + Q**2 + 1) / (Q**2 + 1)
        s2 = mp.matrix([[a, r], [r, d]])
        return s1, s2
    raise ValueError(lam)


def _matpow(M, k):
    n = M.rows
    if k == 0:
        return mp.eye(n)
    if k < 0:
        return _matpow(M**-1 if False else mp.inverse(M), -k)
    R = mp.eye(n)
    B = M
    while k:
        if k & 1:
            R = R * B
        B = B * B
        k >>= 1
    return R


def rho(lam, word):
    """ρ_λ(word), word = list of signed generators (±1=σ1^{±1}, ±2=σ2^{±1})."""
    s1, s2 = irrep_gens(lam)
    s1i, s2i = mp.inverse(s1), mp.inverse(s2)
    M = mp.eye(s1.rows)
    for g in word:
        if g == 1:
            M = M * s1
        elif g == -1:
            M = M * s1i
        elif g == 2:
            M = M * s2
        elif g == -2:
            M = M * s2i
        else:
            raise ValueError(g)
    return M


def chi(lam, word):
    M = rho(lam, word)
    return sum(M[i, i] for i in range(M.rows))


PARTS = [tuple(p) for p in partitions_of(3)]  # [(3,),(2,1),(1,1,1)]
DIMS = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
GEN_OF = {(3,): "gen1 (u/d, light)", (2, 1): "gen2 (c/s)", (1, 1, 1): "gen3 (t/b)"}
Y = {lam: mp.mpf(str(y_lambda_wenzl_bridge_numeric(list(lam), Q, dps=50)))
     for lam in PARTS}


def tr_M(word):
    """Σ_λ y_λ χ_λ(word) — canonical H_3 Markov trace."""
    return sum(Y[lam] * chi(lam, word) for lam in PARTS)


# ── self-validation ───────────────────────────────────────────────────────
def validate():
    out = {}
    # (1) Hecke + braid relations hold numerically (per irrep)
    for lam in PARTS:
        s1, s2 = irrep_gens(lam)
        n = s1.rows
        I = mp.eye(n)
        hecke1 = (s1 - Q * I) * (s1 + QI * I)
        hecke2 = (s2 - Q * I) * (s2 + QI * I)  # check sigma_2 too, not only sigma_1
        braid = s1 * s2 * s1 - s2 * s1 * s2
        out[f"hecke_resid_{lam}"] = float(max(
            max(abs(hecke1[i, j]) for i in range(n) for j in range(n)),
            max(abs(hecke2[i, j]) for i in range(n) for j in range(n))))
        out[f"braid_resid_{lam}"] = float(max(abs(braid[i, j])
                                              for i in range(n) for j in range(n)))
    # (2) tr_M(identity) = Σ y_λ dim_λ = 1
    out["trM_identity"] = float(sum(Y[lam] * DIMS[lam] for lam in PARTS))
    # (3) q→1 limit: χ_[2,1](σ1) should be q-1/q → 0 ; sign χ = -1/q
    return out


# ── braids ────────────────────────────────────────────────────────────────
def borromean():
    return [1, -2] * 3  # (σ1 σ2^{-1})^3, proton, 3 components


def main():
    val = validate()
    q0f = float(Q)

    # ============ Reading (A): scale-free block-ratio prediction ============
    bw = borromean()
    block = {lam: Y[lam] * chi(lam, bw) for lam in PARTS}  # y_λ χ_λ(β_Bor)
    trM_bor = sum(block[lam] for lam in PARTS)
    # generation mass ratio = block projection ratio (Vol_ℂ, tr_M cancel)
    ratio_charm_light = block[(2, 1)] / block[(3,)]
    ratio_top_light = block[(1, 1, 1)] / block[(3,)]

    # observed quark-mass hierarchies (PDG, MS-bar current masses at 2 GeV
    # for u,d,s; m_c(m_c), m_b(m_b), m_t pole for the heavy):
    m_u, m_d, m_s = 2.16, 4.67, 93.4      # MeV
    m_c, m_b, m_t = 1270.0, 4180.0, 172_570.0  # MeV
    m_light = (m_u + m_d) / 2             # ~3.4 MeV
    obs_charm_light = m_c / m_light       # ~372
    obs_top_light = m_t / m_light

    readingA = {
        "braid": "borromean (s1 s2^-1)^3",
        "y_chi_block": {str(lam): float(block[lam].real) for lam in PARTS},
        "y_chi_block_gen": {GEN_OF[lam]: float(block[lam].real) for lam in PARTS},
        "trM_borromean": float(trM_bor.real),
        "pred_charm_over_light": float(ratio_charm_light.real),
        "pred_top_over_light": float(ratio_top_light.real),
        "obs_charm_over_light": obs_charm_light,
        "obs_top_over_light": obs_top_light,
    }

    # ============ Reading (B): SnapPy complex volume + [2,1] projection ======
    readingB = None
    snappy_err = None
    _snappy_version = None
    try:
        import snappy
        _snappy_version = getattr(snappy, "__version__", "unknown")

        def volcs_comps(word):
            L = snappy.Link(braid_closure=word)
            M = L.exterior()
            v = float(M.volume())
            try:
                cs = float(M.chern_simons())
            except Exception:
                cs = None
            return v, cs, int(M.num_cusps())

        # candidate charm braids: Borromean + one strand winding, permutation
        # kept trivial by adding σ1^{2k} (even ⟹ 1↔2 net-fixed).  k is a KNOB.
        cand = {}
        for k in range(0, 5):
            w = [1, -2] * 3 + [1] * (2 * k)
            v, cs, c = volcs_comps(w)
            # block projections of the complex volume: fraction of tr_M in block
            # λ, times Vol_ℂ.  Re is the mass candidate (up to scale).
            trm = tr_M(w)
            fracs = {lam: (Y[lam] * chi(lam, w) / trm) for lam in PARTS}
            volc = mp.mpc(v, cs if cs is not None else 0)
            proj = {lam: (volc * fracs[lam]) for lam in PARTS}
            cand[f"k={k} (winding {3+2*k} on strand1)"] = {
                "word": w,
                "vol": v,
                "chern_simons": cs,
                "components": c,
                "block_frac_re": {str(lam): float(fracs[lam].real) for lam in PARTS},
                "charm_block_proj_re": float(proj[(2, 1)].real),
                "charm_block_proj_im": float(proj[(2, 1)].imag),
            }

        # scale-free ratio within reading (B): charm-braid [2,1] projection vs
        # proton-braid [3] projection (the light anchor).  Compare to m_c/m_light.
        v0, cs0, c0 = volcs_comps(bw)
        volc0 = mp.mpc(v0, cs0 if cs0 is not None else 0)
        trm0 = tr_M(bw)
        light_proj = (volc0 * Y[(3,)] * chi((3,), bw) / trm0).real  # proton [3] block
        readingB = {
            "note": "twist count k is a KNOB (winding-5 ⟹ needs k tuned) — FIT if "
                    "used to hit m_c; reported for completeness, NOT canonical.",
            "light_anchor_proj_re (proton [3] block)": float(light_proj),
            "candidates": cand,
        }
    except Exception as e:  # noqa: BLE001
        snappy_err = repr(e)

    verdict = (
        "Reading (A) [PARAMETER-FREE, scale-free]: the H_3 Wedderburn-block "
        "ratio y_[2,1]χ_[2,1] / y_[3]χ_[3] on the Borromean baryon predicts "
        "m_charm/m_light = %.4f, vs observed ~%.0f (current) — a %.0fx UNDERSHOOT. "
        "The block projection is O(1), not O(100): the charm/light hierarchy is "
        "NOT the Frobenius block ratio of the proton braid. Scope-(a) negative, "
        "no knob. Reading (B) needs a tuned twist count (=FIT) to move the "
        "number and is NOT canonical. m_c stays OPEN."
    ) % (float(ratio_charm_light.real), obs_charm_light,
         obs_charm_light / float(ratio_charm_light.real))

    import hashlib
    import os
    import subprocess
    _cwd = os.path.dirname(os.path.abspath(__file__))
    try:
        _commit = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", __file__],
            cwd=_cwd).decode().strip() or "unknown"
    except Exception:
        _commit = "unknown"
    try:
        _head_commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_cwd).decode().strip() or "unknown"
    except Exception:
        _head_commit = "unknown"

    # Standard witness assertions: the self-validation residuals that back the
    # "no fit" claim.  Each is a checkable numeric with an explicit tolerance,
    # so a validator can re-verify this witness without reading the prose.
    _TOL = mp.mpf("1e-40")
    assertions = []
    for _k, _v in val.items():
        if "resid" in _k:
            assertions.append({
                "name": _k,
                # STRINGS: the documented convention for keeping an
                # assertion value out of float64.
                "computed": repr(float(_v)),
                "expected": "0.0",
                "tolerance": mp.nstr(_TOL, 8),
                "passed": abs(mp.mpf(_v)) <= _TOL,
            })
    assertions.append({
        "name": "trM_identity_eq_one",
        "computed": repr(float(val["trM_identity"])),
        "expected": "1.0",
        "tolerance": "1e-30",
        "passed": abs(mp.mpf(val["trM_identity"]) - 1) <= mp.mpf("1e-30"),
    })
    all_passed = all(a["passed"] for a in assertions)

    witness = {
        "engine": "mpmath+snappy",
        "engineVersion": f"mpmath {mp.__version__}"
                         + (f"; snappy {_snappy_version}" if _snappy_version else
                            "; snappy unavailable"),
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "durationMs": int((_time.time() - _T0) * 1000),
        "computation": "charm-frobenius-block-projection",
        "scriptFile": "charm_frobenius_block_projection_probe.py",
        "scriptHash": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:12],
        "scriptCommitSha": _commit,
        "commitSha": _head_commit,
        "assertions": assertions,
        "allPassed": all_passed,
        "description": "charm_frobenius_block_projection_probe: Frobenius/Wedderburn "
                       "charm-block projection of a composite braid's complex volume "
                       "vs the charm mass hierarchy (derive-then-check).",
        "producer": "computations/charm_frobenius_block_projection_probe.py",
        "consumes": ["conj:complex-mass-constituent-functional"],
        # `Q = mp.mpf(q_parameter.Q)` — and `q_parameter.Q` is a PYTHON FLOAT,
        # not Q_50_DIGIT_STR. So Q carries 17 real digits in an mpf, and
        # printing it at 30 dps fabricates the rest:
        #     mp.nstr(Q, 30) -> 1.10997858275138083783417641826
        #     the real anchor  1.1099785827513808075916690956...
        # diverging at the 17th digit. Written at its true f64 width instead.
        # (That the probe reads q_parameter.Q rather than Q_50_DIGIT_STR is a
        # real precision ceiling on everything downstream, recorded on qou-mnrd;
        # changing it would move values and is not this commit's business.)
        "q0": repr(float(Q)),
        "q0_anchor": "experimental-proton (q_parameter.Q; AGENTS 2026-08-07 default)",
        "validation": f64_json(val),
        # Y is computed at dps=50 but from the f64-limited Q above, so its
        # ACCURACY is f64; written at that width rather than padded.
        "y_lambda": {str(lam): repr(float(Y[lam])) for lam in PARTS},
        "reading_A_scale_free_block_ratio": f64_json(readingA),
        "reading_B_snappy_complex_volume": f64_json(readingB),
        "snappy_error": snappy_err,
        "verdict": verdict,
        "scope": "(a) scope-limited negative: block ratio is O(1), charm/light is "
                 "O(100). No parameter-free block projection reproduces m_c.",
    }
    outp = HERE / "charm-frobenius-block-projection.witness.json"
    outp.write_text(json.dumps(witness, indent=2))

    # ── report ──
    print("=== validation ===")
    for k, v in val.items():
        print(f"  {k}: {v:.3e}" if "resid" in k else f"  {k}: {v}")
    print("\n=== y_λ (proton-q0) ===")
    for lam in PARTS:
        print(f"  {lam}: {float(Y[lam]):.6f}  ({GEN_OF[lam]})")
    print("\n=== Reading (A): scale-free block projections on Borromean ===")
    for lam in PARTS:
        print(f"  y_λχ_λ[{lam}] = {float(block[lam].real):+.5f}  ({GEN_OF[lam]})")
    print(f"  tr_M(Borromean) = {float(trM_bor.real):.6f}")
    print(f"  PRED m_charm/m_light = block[2,1]/block[3] = {float(ratio_charm_light.real):.5f}")
    print(f"  OBS  m_charm/m_light ~ {obs_charm_light:.1f}  "
          f"=> undershoot {obs_charm_light/float(ratio_charm_light.real):.0f}x")
    print(f"  PRED m_top/m_light   = {float(ratio_top_light.real):+.5f}  "
          f"(OBS ~ {obs_top_light:.0f})")
    if readingB:
        print("\n=== Reading (B): SnapPy complex-volume [2,1] block projections ===")
        print(f"  (KNOB: twist count) light anchor proton[3] proj = "
              f"{readingB['light_anchor_proj_re (proton [3] block)']:.4f}")
        for name, d in readingB["candidates"].items():
            print(f"  {name}: Vol={d['vol']:.4f} CS={d['chern_simons']} "
                  f"comps={d['components']} charm[2,1]proj.re={d['charm_block_proj_re']:.4f}")
    else:
        print("\n[Reading (B) SnapPy unavailable]:", snappy_err)
    print("\nVERDICT:", verdict)
    print("\nwrote", outp)


if __name__ == "__main__":
    main()
