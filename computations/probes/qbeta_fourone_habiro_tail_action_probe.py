#!/usr/bin/env python3
"""qbeta_fourone_habiro_tail_action_probe.py — b3ix distinct route: the 4₁
Habiro cyclotomic tail is bar-even and its resurgent action is EXACTLY π²/5
(golden-ratio dilogarithm), distinct from the geometric Vol/π — the ħ↔2πi/N wall
made exact.

CONTEXT (bean qou-dku0; distinct-route contribution to #3966's b3ix "residue ↔
Habiro cyclotomic-tail identity", overlap authorized). The 4₁ Kashaev/Habiro
invariant is the cyclotomic sum J = Σ_n (q;q)_n (q⁻¹;q⁻¹)_n. Evaluated at REAL
q = e^t near the substrate (the archimedean ρ_∞ face, not a root of unity), the
tail S(q) = Σ_n ∏_{j=1}^n (1−q^j)(1−q⁻^j) is an ALTERNATING asymptotic series
(each factor (1−q^j)(1−q⁻ʲ) = −(q^{j/2}−q^{−j/2})² < 0, so the terms alternate
and |t_n| = ∏ 4 sinh²(jt/2) first decreases then grows — optimal-truncation /
resurgent structure). b3ix asks what the resurgent "residue" of this tail is.

TWO EXACT FINDINGS:

  (1) BAR-EVEN. The factor (1−q^j)(1−q⁻ʲ) is invariant under q↔q⁻¹, so S(q) =
      S(q⁻¹) exactly. The 4₁ Habiro tail carries NO bar-odd datum — consistent
      with 4₁ amphichirality and the #3923 odd-phase null. ⇒ the ODD-channel
      b3ix (the c₃/N_odd datum) must use the CHIRAL 5₂ Habiro tail, not 4₁.

  (2) ACTION = π²/5 EXACTLY (golden-ratio dilog). The optimal truncation sits at
      the minimal term n* where 2 sinh(n*t/2) = 1, i.e. n*t/2 = arcsinh(½) =
      ln φ (golden ratio, exact). The t→0 resurgent action is
        A₀ = −t·ln|t_min| → −4 ∫₀^{ln φ} ln(2 sinh s) ds = π²/5,
      via ∫₀^{ln φ} ln(2 sinh s) ds = −π²/20 (using the Landen value
      Li₂(φ⁻²) = π²/15 − ln²φ). So the ARCHIMEDEAN Habiro-tail action is π²/5 —
      a Rogers-dilogarithm / golden-ratio constant — DISTINCT from the geometric
      (root-of-unity / state-integral) action Vol(4₁)/π ≈ 0.6461. This is the
      ħ↔2πi/N wall (#3938) made exact: the Habiro object and its archimedean
      evaluation ρ_∞ carry different resurgent actions.

IMPLICATION for b3ix. The "residue = cyclotomic factor" identity must be stated
with respect to a FIXED evaluation: the archimedean ρ_∞ Habiro tail resums at
action π²/5, not the geometric Vol/π. A residue↔tail identity that silently
mixes the two faces is a category error (the wall). For the odd channel the same
programme runs on the 5₂ chiral tail (flagged to #3966).

SCOPE (scope-(a)/(b)). (b): the bar-even-ness is a proved q↔q⁻¹ symmetry (cited
invariant: amphichirality). (b): A₀ = π²/5 is an exact closed form (Li₂ Landen
identity), a structural distinctness from Vol/π. No fit; NO c_k wired; μ never
fixed from QOU data.

Run: python3 -u computations/probes/qbeta_fourone_habiro_tail_action_probe.py \\
       2>&1 | tee /tmp/qbeta_habiro_tail.log
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess

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


def _repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _head_sha():
    for ev in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip():
            return v.strip()
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def habiro_term(q, n):
    p = mp.mpf(1)
    for j in range(1, n + 1):
        p *= (1 - q ** j) * (1 - q ** -j)
    return p


def habiro_tail_opt(q):
    """Optimal-truncation (minimal-term) partial sum of the 4₁ Habiro tail."""
    t = abs(mp.log(q))
    K = int(4 / t) + 30
    ab = [abs(habiro_term(q, n)) for n in range(K)]
    nmin = min(range(1, K), key=lambda n: ab[n])
    S = sum(habiro_term(q, n) for n in range(nmin + 1))
    return S, nmin, ab[nmin]


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" 4₁ Habiro cyclotomic tail — bar-even + action = π²/5 (b3ix)")
    print("=" * 78)

    phi = (1 + mp.sqrt(5)) / 2
    q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
    vol = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    vol_over_pi = vol / mp.pi

    # (1) bar-even
    S0, nmin, tmin = habiro_tail_opt(q0)
    Sinv, _, _ = habiro_tail_opt(1 / q0)
    bar_even = abs(S0 - Sinv) < mp.mpf(10) ** (-20)
    print(f"\n  S(q₀) = {mp.nstr(S0,10)}   S(1/q₀) = {mp.nstr(Sinv,10)}   "
          f"bar-even: {bar_even}")
    check("fourone_habiro_tail_is_bar_even", bar_even,
          source="S(q)=Σ_n (q;q)_n(q⁻¹;q⁻¹)_n is invariant under q↔q⁻¹ (each "
                 "factor is) — the 4₁ Habiro tail carries no bar-odd datum "
                 "(amphichirality; #3923 null). Odd b3ix needs the 5₂ tail")

    # (2) action = π²/5 exactly
    #   arcsinh(1/2) = ln φ
    asinh_half = mp.asinh(mp.mpf(1) / 2)
    golden_ok = abs(asinh_half - mp.log(phi)) < mp.mpf(10) ** (-30)
    #   A₀ = -4 ∫₀^{ln φ} ln(2 sinh s) ds = π²/5
    A0 = -4 * mp.quad(lambda s: mp.log(2 * mp.sinh(s)), [0, mp.log(phi)])
    pi2_5 = mp.pi ** 2 / 5
    a0_ok = abs(A0 - pi2_5) < mp.mpf(10) ** (-25)
    #   Landen value used in the closed form
    li2_ok = abs(mp.polylog(2, phi ** -2) - (mp.pi ** 2 / 15 - mp.log(phi) ** 2)) \
        < mp.mpf(10) ** (-25)
    print(f"\n  arcsinh(½) = ln φ : {golden_ok}  (= {mp.nstr(asinh_half,12)})")
    print(f"  Li₂(φ⁻²) = π²/15 − ln²φ : {li2_ok}")
    print(f"  A₀ = −4∫₀^{{ln φ}} ln(2 sinh s) ds = {mp.nstr(A0,15)}")
    print(f"  π²/5 = {mp.nstr(pi2_5,15)}   A₀ = π²/5 : {a0_ok}")
    check("habiro_tail_action_is_pi2_over_5_exact", a0_ok and golden_ok and li2_ok,
          computed=f"A₀={mp.nstr(A0,12)}", expected=f"π²/5={mp.nstr(pi2_5,12)}",
          source="the 4₁ archimedean Habiro-tail optimal-truncation action is "
                 "exactly π²/5 (golden-ratio dilog: arcsinh½=ln φ, Landen "
                 "Li₂(φ⁻²)=π²/15−ln²φ, ∫₀^{ln φ}ln(2 sinh s)ds=−π²/20)")

    # (3) distinct from the geometric Vol/π (the ħ↔2πi/N wall, exact)
    distinct = abs(pi2_5 - vol_over_pi) > mp.mpf("0.5")
    print(f"\n  geometric action Vol/π = {mp.nstr(vol_over_pi,10)}  vs Habiro "
          f"π²/5 = {mp.nstr(pi2_5,10)}  (distinct by {mp.nstr(pi2_5-vol_over_pi,6)})")
    check("habiro_action_distinct_from_geometric_vol", distinct,
          computed=f"π²/5={mp.nstr(pi2_5,6)} vs Vol/π={mp.nstr(vol_over_pi,6)}",
          source="the archimedean ρ_∞ Habiro-tail action π²/5 differs from the "
                 "geometric (root-of-unity/state-integral) action Vol(4₁)/π — "
                 "the ħ↔2πi/N wall (#3938) made exact; a residue↔tail identity "
                 "must fix which evaluation face it is on")

    # (4) t→0 convergence of the discrete action to π²/5 (sanity)
    disc = []
    for t in ("0.05", "0.02", "0.01"):
        q = mp.e ** mp.mpf(t)
        _, _, tm = habiro_tail_opt(q)
        disc.append(-mp.mpf(t) * mp.log(tm))
    monotone_up = disc[0] < disc[1] < disc[2] < pi2_5
    print(f"\n  discrete action → π²/5: t=0.05,0.02,0.01 → "
          f"{[mp.nstr(x,6) for x in disc]}  (↑ toward {mp.nstr(pi2_5,6)})")
    check("discrete_action_converges_to_pi2_5", monotone_up,
          source="the finite-t minimal-term action increases monotonically "
                 "toward π²/5 as t→0 — confirming π²/5 is the resurgent action")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        ("b3ix DISTINCT-ROUTE RESULT: the 4₁ Habiro cyclotomic tail "
         "S(q)=Σ_n (q;q)_n(q⁻¹;q⁻¹)_n, at real q (the archimedean ρ_∞ face), is "
         "(1) BAR-EVEN (S(q)=S(q⁻¹) exactly — no bar-odd datum, so the odd b3ix "
         "needs the chiral 5₂ tail), and (2) a resurgent asymptotic series whose "
         "optimal-truncation action is EXACTLY π²/5 (golden-ratio dilog: "
         "arcsinh½=ln φ, Li₂(φ⁻²)=π²/15−ln²φ), DISTINCT from the geometric "
         "Vol(4₁)/π≈0.6461. So the archimedean Habiro-tail resums at action π²/5, "
         "not Vol/π — the ħ↔2πi/N wall (#3938) made exact. The residue↔tail "
         "identity (b3ix) must therefore fix its evaluation face; for the odd "
         "channel the same programme runs on the 5₂ chiral tail. "
         if all_passed else
         "PARTIAL: a check failed — see the per-check table. ")
        + "scope-(b): bar-even is a proved q↔q⁻¹ symmetry; A₀=π²/5 is an exact "
        "closed form (Landen identity). NO fit; NO c_k wired; μ never fixed from "
        "QOU data."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-fourone-habiro-tail-action",
        "description": "b3ix distinct route: the 4₁ Habiro cyclotomic tail is "
                       "bar-even (no odd datum) and its archimedean resurgent "
                       "action is exactly π²/5 (golden-ratio dilog), distinct "
                       "from the geometric Vol/π — the ħ↔2πi/N wall made exact. "
                       "Odd b3ix needs the 5₂ chiral tail. scope-(b).",
        "audit_only": True,
        "tier": "symbolic-exact + numerical (resurgent action closed form)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "habiro_tail_bar_even": bool(bar_even),
            "S_opt_at_q0": mp.nstr(S0, 12),
            "minimal_term_n": int(nmin),
            "action_A0": mp.nstr(A0, 15),
            "pi2_over_5": mp.nstr(pi2_5, 15),
            "action_is_pi2_over_5": bool(a0_ok),
            "geometric_vol_over_pi": mp.nstr(vol_over_pi, 12),
            "discrete_action_t_005_002_001": [mp.nstr(x, 8) for x in disc],
            "verdict": verdict,
        },
        "context": {
            "axis": "b3ix Habiro residue↔tail (distinct route; bean qou-dku0)",
            "supports": "#3966 deep-dive 2 (b3ix)",
            "closed_form": "A₀ = −4∫₀^{ln φ} ln(2 sinh s) ds = π²/5; "
                           "arcsinh½=ln φ; Li₂(φ⁻²)=π²/15−ln²φ",
            "wall_ref": "#3938 ħ↔2πi/N (Habiro object vs archimedean ρ_∞ eval)",
            "odd_channel_note": "4₁ tail bar-even ⇒ odd b3ix needs 5₂ chiral tail",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-fourone-habiro-tail-action.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
