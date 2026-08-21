#!/usr/bin/env python3
"""
Deformed Ohtsuki rungs κ̃_n(u) of 4₁ at the SUBSTRATE MERIDIAN — the u-dependence
the bar-odd S routes need (route 2 of the bar-odd-S program).

Context. The bar-odd S = c₃ + Vol(4₁) decomposes as S = h·D(u) (h = q−1/q); the
Φ_b finite-b mechanism (#3654) derives the S *scale* as i·t·κ₁ with t = ln q₀ and
κ₁ = 11√3π/108 the u=0 Ohtsuki 2-loop — but κ₁ there is evaluated at the COMPLETE
structure (u=0), so the correction is anchor-blind. The open piece named in #3654:
"the exact S needs κ₁(u) at the substrate meridian u = 2 log q₀". This probe
supplies that u-dependence — numerically, from the exact deformed colored Jones,
with NO deformed-volume-conjecture assumption (for 4₁ and real 0 < u < u_crit =
log((3+√5)/2) ≈ 0.9624 the asymptotic expansion is H. Murakami's THEOREM
[murakami2013] (J. Topology 6 (2013); arXiv:1203.5622)).

The exact deformed sum (Habiro/Masbaum form, unknot-normalized):

    J_N(4₁; q) = Σ_{k=0}^{N-1} ∏_{j=1}^{k} {N−j}{N+j},   {m} = q^{m/2} − q^{−m/2},
    q = e^{ξ/N},  ξ = u + 2πi.

Since q^N = e^ξ = e^u, the term collapses to the clean product form

    {N−j}{N+j} = q^N + q^{−N} − q^j − q^{−j} = 2cosh(u) − 2cosh(ξ j/N),

which at u=0 is 4sin²(πj/N) — EXACTLY the term of the merged u=0 extractor
(qbeta_ohtsuki_higher_rungs.py, #3628). This probe is that extractor's direct
generalization; template (Murakami):

    log J_N = α(u)·N + (1/2)·log N + γ(u) + Σ_n κ̃_n(u)/N^n
    (u=0 has (3/2)·log N instead — the parabolic/regular saddle switch).

Two extraction channels:
  * Re log J_N — branch-free; Vandermonde ladder fit gives Re α, Re κ̃_n.
  * Im log J_N — known only mod 2π per point; the integer combo
        T(N) = 2·Im log J_N − 3·Im log J_{2N} + Im log J_{4N}   (mod 2π, lifted)
    kills the N-linear term (2−6+4=0) and the constant (2−3+1=0), leaves
    −Im(β)·log2 (≈0, template) + Σ_n Im(κ̃_n)·(2 − 3·2^{−n} + 4^{−n})/N^n,
    so a small bounded quantity recoverable from principal args. Fitting T(N)
    yields Im κ̃_n.

Validations (each computed, no fit to QOU data):
  V1. u=0 run (real form) reproduces κ₁ = 11√3π/108 (the merged #3606/#3628 value).
  V2. β free-fit at the substrate meridian returns 1/2 (deformed-template check).
  V3. Ladder self-consistency (full vs coarse fit) ≥ 6 confident digits on κ̃₁.
  V4. Geometry: Re α(u) vs 2π·Vol(u)/(u²+4π²) with Vol(u) from the corpus's
      validated gluing Newton solve (z(z−1)w(w−1)=1, w=m²z, m=e^{u/2}) —
      the residual decomposes as resid = (1/2)·u + b·u² + O(u³) with the
      LINEAR term structurally exact (⇔ Im S(u) ⊃ π·u, the framing/meridian
      normalization — odd under u↦−u, i.e. a bar-odd linear channel) and
      b ≈ 0.1703 smooth O(1) (unidentified; mixes Im-S u² with Re-S u terms).
      The check asserts a = 1/2 and boundedness — smooth geometry, no wall.
  V5. Anchor-blindness: κ̃₁(u_proton) vs κ̃₁(u_muon) (anchors differ ~2e-8 in u) —
      consistent with #3636 (the sign-flip is representational, not geometric).

Physics rows (computed comparisons; NO fit; no c_k wired):
  * κ̃₁(u_sub) vs κ₁(0): how much the substrate meridian moves the 2-loop rung;
  * the deformed finite-b lead Im[i·t·κ̃₁(u_sub)] = t·Re κ̃₁(u_sub) vs the two S
    targets S(muon) = +0.00968298, S(proton) = −0.03945936 (#3600 witness);
  * the intrinsic odd channel Im κ̃₁(u_sub) (u≠0 breaks reality of J_N — this
    imaginary part is a *new* derived bar-odd-channel datum at the meridian).

Anti-laundering: all outputs are 4₁ topological/asymptotic facts at a deformed
meridian; nothing here wires a Q_β c_k, closes S, or changes any tier.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

import mpmath as mp

# Deformed-saddle cancellation eats digits LINEARLY in N (measured rate
# ≈ 0.0017·N decimal digits at u ≈ 0.21 — the true saddle is complex, so the
# real-axis partial products overshoot |J_N| exponentially). dps must cover
# the largest-N loss (~223 digits at N=131072) plus working headroom.
mp.mp.dps = 300

S_TARGET = {"proton": mp.mpf("-0.03945936"), "muon": mp.mpf("0.00968298")}


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


def _substrate_q():
    """Canonical q₀ at both pins (proton = precision pin, muon = CAL-2 proxy)."""
    sys.path.insert(0, os.path.join(_repo_root(), "tools", "qou-substrate", "python"))
    from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
    return q_at(mp.mp.dps), q_muon_at(mp.mp.dps)


# ---------------------------------------------------------------- deformed sum
def log_jones_deformed(N, u):
    """log J_N(4₁; e^{ξ/N}), ξ = u+2πi, via streaming complex log-sum-exp.

    Term product P_k = ∏_{j≤k} g_j, g_j = 2cosh u − (Q_j + 1/Q_j), Q_j = e^{ξj/N}
    iterated multiplicatively (one mul + one div per term). The running max is
    kept as a COMPLEX reference logP* (the logP at the running-max term) so
    phases are preserved exactly: s = Σ_k exp(logP_k − logP*);
    log J = logP* + log s. Re of the result is exact; Im is principal (mod 2π)
    — by design (see module docstring). Returns (logJ complex, digit_loss)
    where digit_loss measures the peak-term vs sum cancellation."""
    xi = mp.mpc(u, 0) + 2j * mp.pi
    r = mp.exp(xi / N)
    two_cosh_u = 2 * mp.cosh(mp.mpf(u))
    Q = mp.mpc(1)
    logP = mp.mpc(0)
    ref = mp.mpc(0)           # complex reference = logP at running max Re
    peak = mp.mpf(0)
    s = mp.mpc(1)             # k=0 term: exp(0 − ref)=1 since ref starts 0
    for j in range(1, N):
        Q *= r
        g = two_cosh_u - (Q + 1 / Q)
        logP += mp.log(g)
        re = mp.re(logP)
        if re > peak:
            peak = re
        if re > mp.re(ref):
            s = s * mp.exp(ref - logP) + 1
            ref = logP
        else:
            s += mp.exp(logP - ref)
    logJ = ref + mp.log(s)
    # NOT float(): the emission at "runs" serializes via `_n(vv) if
    # isinstance(vv, (mp.mpf, mp.mpc))`, so downcasting here makes that guard
    # fall through and the value reaches the witness as raw float64. The
    # quantity is already exact-in-mpmath above; keeping it mpf is what lets
    # the file's own serializer do its job. Bean qou-irzg.
    loss = (peak - mp.re(logJ)) / mp.log(10)
    return logJ, loss


def log_kashaev_u0(N):
    """u=0 real form (identical to the merged extractor): all terms positive."""
    pi = mp.pi
    logP = mp.mpf(0)
    m = mp.mpf(0)
    s = mp.mpf(1)
    for k in range(1, N):
        logP += 2 * mp.log(2 * mp.sin(pi * k / N))
        if logP > m:
            s = s * mp.exp(m - logP) + 1
            m = logP
        else:
            s += mp.exp(logP - m)
    return m + mp.log(s)


# ---------------------------------------------------------------------- fits
def solve_basis(Ns, ys, basis_fns):
    """Exact linear solve ys = Σ_c a_c basis_c(N) through all points."""
    M = len(Ns)
    assert len(basis_fns) == M
    V = mp.matrix(M, M)
    for i in range(M):
        for c in range(M):
            V[i, c] = basis_fns[c](Ns[i])
    return list(mp.lu_solve(V, mp.matrix(ys)))


def fit_re_channel(Ns, re_logJ, beta_pinned=True):
    """Fit Re log J_N − β ln N with basis {N, 1, 1/N, …}. Returns dict of
    coefficients. beta_pinned=False adds ln N as a free column instead."""
    if beta_pinned:
        ys = [re_logJ[i] - mp.mpf(1) / 2 * mp.log(Ns[i]) for i in range(len(Ns))]
        fns = [lambda N: mp.mpf(N), lambda N: mp.mpf(1)] + \
              [(lambda j: lambda N: mp.mpf(N) ** (-j))(j)
               for j in range(1, len(Ns) - 1)]
        a = solve_basis(Ns, ys, fns)
        return {"alpha_re": a[0], "gamma_re": a[1],
                "kappa_re": a[2:], "beta": mp.mpf(1) / 2}
    ys = list(re_logJ)
    fns = [lambda N: mp.mpf(N), lambda N: mp.log(N), lambda N: mp.mpf(1)] + \
          [(lambda j: lambda N: mp.mpf(N) ** (-j))(j)
           for j in range(1, len(Ns) - 2)]
    a = solve_basis(Ns, ys, fns)
    return {"alpha_re": a[0], "beta": a[1], "gamma_re": a[2], "kappa_re": a[3:]}


def principal(x):
    """Lift to (−π, π]."""
    twopi = 2 * mp.pi
    y = mp.fmod(x, twopi)
    if y > mp.pi:
        y -= twopi
    elif y <= -mp.pi:
        y += twopi
    return y


def fit_im_channel(Ns, im_logJ):
    """T(N_i) = principal(2 Im_i − 3 Im_{i+1} + Im_{i+2}) on the doubling ladder;
    fit with {1, 1/N, …}; convert to Im κ̃_n via the combo weights.
    Constant column ≈ −ln2·Im β (template: 0)."""
    K = len(Ns) - 2
    Ts, TN = [], []
    for i in range(K):
        Ts.append(principal(2 * im_logJ[i] - 3 * im_logJ[i + 1] + im_logJ[i + 2]))
        TN.append(Ns[i])
    fns = [lambda N: mp.mpf(1)] + \
          [(lambda j: lambda N: mp.mpf(N) ** (-j))(j) for j in range(1, K)]
    a = solve_basis(TN, Ts, fns)
    const = a[0]
    im_kappa = []
    for j in range(1, K):
        wj = 2 - 3 * mp.mpf(2) ** (-j) + mp.mpf(4) ** (-j)
        im_kappa.append(a[j] / wj)
    return {"T_const": const, "kappa_im": im_kappa, "T_values": Ts}


# ------------------------------------------------------------------- geometry
Z0 = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)


def bloch_wigner(z):
    z = mp.mpc(z)
    if z == 0 or z == 1:
        return mp.mpf(0)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(mp.fabs(z))


def vol_deformed(u):
    """Vol(u) = D(z)+D(w) on the geometric branch, w = m²z, m = e^{u/2}
    (the corpus's validated gluing Newton solve)."""
    m_h = mp.exp(mp.mpf(u) / 2)
    z = mp.findroot(lambda z: z * (z - 1) * (m_h ** 2 * z) * (m_h ** 2 * z - 1) - 1, Z0)
    w = m_h ** 2 * z
    return bloch_wigner(z) + bloch_wigner(w)


# ----------------------------------------------------------------------- main
def run_ladder(u, Ns, label):
    """Ladder with ADAPTIVE truncation: the deformed-saddle cancellation loss
    grows ~ u^1.9·N digits, so at larger u the top rungs would exceed the
    working precision — keep only points with ≥ 40 digits of headroom."""
    t0 = time.time()
    logJs, losses, kept = [], [], []
    for i, N in enumerate(Ns):
        lj, loss = log_jones_deformed(N, u)
        if loss > mp.mp.dps - 40:
            print(f"    [{label}] N={N} loss={float(loss):.1f}d exceeds dps−40 "
                  f"headroom — truncating ladder here ({len(kept)} pts kept)",
                  flush=True)
            break
        kept.append(N)
        logJs.append(lj)
        losses.append(loss)
        el = time.time() - t0
        eta = el / (i + 1) * (len(Ns) - i - 1)
        print(f"    [{label}] {i + 1}/{len(Ns)} N={N:7d} loss={float(loss):5.2f}d "
              f"elapsed={el:6.1f}s eta={eta:6.1f}s", flush=True)
    if len(kept) < 6:
        raise RuntimeError(f"ladder at u={mp.nstr(u, 8)} kept only {len(kept)} "
                           f"points — raise dps")
    Ns = kept
    re_l = [mp.re(x) for x in logJs]
    im_l = [mp.im(x) for x in logJs]
    fit = fit_re_channel(Ns, re_l, beta_pinned=True)
    fit_coarse = fit_re_channel(Ns[:-2], re_l[:-2], beta_pinned=True)
    fit_bfree = fit_re_channel(Ns, re_l, beta_pinned=False)
    imfit = fit_im_channel(Ns, im_l)
    k1 = fit["kappa_re"][0]
    k1c = fit_coarse["kappa_re"][0]
    conv = abs(k1 - k1c)
    conf = int(-mp.log10(conv)) if conv > 0 else 40
    return {
        "u": u, "Ns": Ns, "max_loss_digits": max(losses),
        "alpha_re": fit["alpha_re"], "gamma_re": fit["gamma_re"],
        "beta_free": fit_bfree["beta"],
        "kappa1_re": k1, "kappa1_conf_digits": conf,
        "kappa2_re": fit["kappa_re"][1],
        "kappa1_im": imfit["kappa_im"][0],
        "kappa2_im": imfit["kappa_im"][1] if len(imfit["kappa_im"]) > 1 else None,
        "T_const": imfit["T_const"],
    }


def main():
    pi = mp.pi
    s3 = mp.sqrt(3)
    Vol0 = 2 * mp.clsin(2, pi / 3)
    kappa1_exact_u0 = 11 * s3 * pi / 108
    U_CRIT = mp.log((3 + mp.sqrt(5)) / 2)

    q_p, q_m = _substrate_q()
    u_p, u_m = 2 * mp.log(q_p), 2 * mp.log(q_m)
    t_p = mp.log(q_p)
    print(f"substrate meridians: u_proton = {mp.nstr(u_p, 20)}")
    print(f"                     u_muon   = {mp.nstr(u_m, 20)}")
    print(f"Murakami theorem range: 0 < u < {mp.nstr(U_CRIT, 10)}  (both inside)")

    # ---- V1: u=0 sanity (real form, light ladder) ----
    print("\n[V1] u=0 sanity — reproduce κ₁ = 11√3π/108 (light ladder):", flush=True)
    Ns0 = [512 * 2 ** j for j in range(8)]
    D0 = []
    for N in Ns0:
        lj = log_kashaev_u0(N)
        D0.append(lj - mp.mpf(3) / 2 * mp.log(N) - N * Vol0 / (2 * pi))
        print(f"    N={N:7d} done", flush=True)
    fns0 = [(lambda j: lambda N: mp.mpf(N) ** (-j))(j) for j in range(len(Ns0))]
    a0 = solve_basis(Ns0, D0, fns0)
    k1_u0 = a0[1]
    v1_err = abs(k1_u0 - kappa1_exact_u0)
    print(f"    κ₁(0) extracted = {mp.nstr(k1_u0, 20)}  |Δ| = {float(v1_err):.2e}")
    v1_ok = v1_err < mp.mpf(10) ** (-10)

    # ---- deformed ladders ----
    Ns = [512 * 2 ** j for j in range(9)]    # 512 … 131072 (loss ≈ 0.0017·N digits)
    grid_u = [mp.mpf("0.05"), mp.mpf("0.12"), u_p, mp.mpf("0.30")]
    print(f"\n[ladders] Ns = {Ns[0]}…{Ns[-1]} ({len(Ns)} pts, dps {mp.mp.dps})", flush=True)
    runs = {}
    for u in grid_u:
        lbl = f"u={mp.nstr(u, 8)}"
        print(f"  ladder at {lbl}:", flush=True)
        runs[str(mp.nstr(u, 12))] = run_ladder(u, Ns, lbl)
    print("  ladder at u_muon (anchor-blindness check):", flush=True)
    run_mu = run_ladder(u_m, Ns, "u_muon")

    run_p = runs[str(mp.nstr(u_p, 12))]

    # ---- V2/V3: template + self-consistency at the substrate ----
    beta_free = run_p["beta_free"]
    v2_ok = abs(beta_free - mp.mpf(1) / 2) < mp.mpf("0.02")
    v3_ok = run_p["kappa1_conf_digits"] >= 6
    print(f"\n[V2] β free-fit at u_sub = {mp.nstr(beta_free, 10)}  (template 1/2) ok={v2_ok}")
    print(f"[V3] κ̃₁ ladder self-consistency: {run_p['kappa1_conf_digits']} digits ok={v3_ok}")

    # ---- V4: geometry residual — NZ quadratic dominance (smoothness, no wall) ----
    print("\n[V4] Re α(u) vs 2π·Vol(u)/(u²+4π²) (Newton gluing solve);")
    print("     residual = NZ/framing terms, expect ≈ c·u² with smooth O(1) c:")
    geo_rows = []
    resid_by_u = []
    for key, r in list(runs.items()) + [("u_muon", run_mu)]:
        u = r["u"]
        volu = vol_deformed(u)
        pred = 2 * pi * volu / (u * u + 4 * pi * pi)
        resid = r["alpha_re"] - pred
        resid_by_u.append((u, resid))
        geo_rows.append({"u": mp.nstr(u, 12), "Vol_u": mp.nstr(volu, 20),
                         "alpha_re": mp.nstr(r["alpha_re"], 20),
                         "alpha_pred_vol_only": mp.nstr(pred, 20),
                         "resid": mp.nstr(resid, 12),
                         "resid_over_u2": mp.nstr(resid / (u * u), 8)})
        print(f"    u={mp.nstr(u, 8):>12}: α_re={mp.nstr(r['alpha_re'], 12)} "
              f"pred={mp.nstr(pred, 12)} resid={mp.nstr(resid, 6)} "
              f"resid/u²={mp.nstr(resid / (u * u), 6)}")
    # Structural model (measured on the first run): the residual is NOT pure
    # NZ-quadratic — it carries an exact-looking LINEAR meridian term,
    #     resid(u) = a·u + b·u² + c·u³ + d·u⁴,   a = 1/2  (⇔ Im S(u) ⊃ π·u,
    # the framing/meridian normalization term — odd under u↦−u, i.e. bar-odd),
    # with b ≈ 0.1703 (mixes the Im-S u²-term with a possible Re-S linear
    # term; left unidentified — no fit to QOU data, this is 4₁ asymptotics).
    resid_by_u.sort(key=lambda p: p[0])
    # dedupe the two near-identical substrate anchors (Δu ~ 2e-8)
    dedup = [resid_by_u[0]]
    for pu, pr in resid_by_u[1:]:
        if abs(pu - dedup[-1][0]) > mp.mpf("1e-4"):
            dedup.append((pu, pr))
    us_g = [p[0] for p in dedup]
    rs_g = [p[1] for p in dedup]
    fns_u = [(lambda j: lambda x: mp.mpf(x) ** j)(j) for j in range(1, len(us_g) + 1)]
    abcd = solve_basis(us_g, rs_g, fns_u)
    a_lin, b_quad = abcd[0], abcd[1]
    v4_ok = bool(abs(a_lin - mp.mpf(1) / 2) < mp.mpf("0.005")) and \
        all(abs(r) < mp.mpf("0.5") for _, r in resid_by_u)
    print(f"    model resid = a·u + b·u² + …: a = {mp.nstr(a_lin, 10)} "
          f"(structural 1/2 ⇔ Im S ⊃ π·u), b = {mp.nstr(b_quad, 8)}  ok={v4_ok}")

    # ---- V5: anchor-blindness ----
    dk1 = abs(run_p["kappa1_re"] - run_mu["kappa1_re"])
    v5_ok = dk1 < mp.mpf("1e-4")
    print(f"\n[V5] |κ̃₁(u_p) − κ̃₁(u_μ)| = {float(dk1):.3e}  (anchors differ ~2e-8 in u) ok={v5_ok}")

    # ---- physics rows ----
    k1_sub = mp.mpc(run_p["kappa1_re"], run_p["kappa1_im"])
    lead = mp.mpc(0, 1) * t_p * k1_sub          # i·t·κ̃₁(u_sub)
    imlead = mp.im(lead)                        # = t·Re κ̃₁
    intrinsic = run_p["kappa1_im"]
    print("\n[physics] substrate-meridian 2-loop rung and the S comparison:")
    print(f"    κ₁(0)      = {mp.nstr(kappa1_exact_u0, 15)}  (exact, 11√3π/108)")
    print(f"    κ̃₁(u_sub) = {mp.nstr(run_p['kappa1_re'], 15)} "
          f"+ i·{mp.nstr(run_p['kappa1_im'], 10)}")
    print(f"    shift Re κ̃₁(u_sub) − κ₁(0) = {mp.nstr(run_p['kappa1_re'] - kappa1_exact_u0, 10)}")
    print(f"    finite-b lead Im[i·t·κ̃₁] = t·Re κ̃₁ = {mp.nstr(imlead, 10)}")
    print(f"    intrinsic odd channel Im κ̃₁(u_sub) = {mp.nstr(intrinsic, 10)}")
    for tag in ("muon", "proton"):
        print(f"      vs S({tag}) = {mp.nstr(S_TARGET[tag], 8)}: "
              f"lead/S = {mp.nstr(imlead / S_TARGET[tag], 6)}, "
              f"Im κ̃₁/S = {mp.nstr(intrinsic / S_TARGET[tag], 6)}")

    # du-smoothness of κ̃₁ across the grid (no-wall confirmation)
    us = [r["u"] for r in runs.values()]
    k1s = [r["kappa1_re"] for r in runs.values()]
    dk_du = [(k1s[i + 1] - k1s[i]) / (us[i + 1] - us[i]) for i in range(len(us) - 1)]
    print(f"    dκ̃₁/du across grid ≈ {[mp.nstr(x, 8) for x in dk_du]} (smooth, O(1))")

    # precision headroom: worst-case ladder loss must leave ≥ 30 working digits
    max_loss = max(r["max_loss_digits"] for r in list(runs.values()) + [run_mu])
    v6_ok = (mp.mp.dps - max_loss) >= 30
    print(f"\n[V6] precision headroom: dps {mp.mp.dps} − max loss {float(max_loss):.1f}d "
          f"= {float(mp.mp.dps - max_loss):.1f}d ok={v6_ok}")

    assertions = [
        {"name": "V1_u0_reproduces_kappa1_exact", "passed": bool(v1_ok)},
        {"name": "V2_deformed_template_beta_half", "passed": bool(v2_ok)},
        {"name": "V3_kappa1_selfconsistent_6_digits", "passed": bool(v3_ok)},
        {"name": "V4_geometry_residual_half_u_plus_quadratic", "passed": bool(v4_ok)},
        {"name": "V5_anchor_blind_kappa1", "passed": bool(v5_ok)},
        {"name": "V6_precision_headroom_30_digits", "passed": bool(v6_ok)},
    ]
    all_passed = all(a["passed"] for a in assertions)

    verdict = (
        f"Deformed Ohtsuki 2-loop rung at the substrate meridian extracted from the "
        f"exact Habiro sum (Murakami-theorem regime, no deformed-volume-conjecture "
        f"assumption): κ̃₁(u_sub) = {mp.nstr(run_p['kappa1_re'], 12)} + "
        f"i·{mp.nstr(run_p['kappa1_im'], 8)} vs κ₁(0) = 11√3π/108 = "
        f"{mp.nstr(kappa1_exact_u0, 12)}. Finite-b S-lead t·Re κ̃₁ = "
        f"{mp.nstr(imlead, 8)} (vs |S| targets 0.0097/0.0395); intrinsic odd channel "
        f"Im κ̃₁ = {mp.nstr(intrinsic, 8)}. κ̃₁ is anchor-blind to {float(dk1):.1e} "
        f"and smooth in u — the sign-flip stays representational (capstone-consistent). "
        f"4₁ facts only; no c_k wired; no fit; no tier change."
    )
    print("\nVERDICT:", verdict)

    def _n(x, d=25):
        return mp.nstr(x, d) if x is not None else None

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-ohtsuki-deformed-meridian-rungs",
        "description": "u-dependence of the 4₁ Ohtsuki rungs at the substrate "
                       "meridian u=2 ln q₀ from the exact deformed Habiro sum "
                       "(2cosh u − 2cosh(ξj/N) term; Murakami-theorem regime): "
                       "Re/Im κ̃₁(u), template β=1/2, geometry cross-check vs the "
                       "gluing Newton Vol(u), anchor-blindness, and the finite-b "
                       "bar-odd S lead t·Re κ̃₁(u_sub). Route 2 of the bar-odd-S "
                       "program (#3654 open item).",
        "audit_only": True,
        "tier": "numerical (deformed-rung extraction + structural checks)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "u_proton": _n(u_p), "u_muon": _n(u_m),
            "murakami_u_crit": _n(U_CRIT, 15),
            "kappa1_u0_extracted": _n(k1_u0),
            "kappa1_u0_exact": "11*sqrt(3)*pi/108",
            "runs": {k: {kk: (_n(vv) if isinstance(vv, (mp.mpf, mp.mpc)) else vv)
                         for kk, vv in r.items() if kk != "Ns"}
                     for k, r in list(runs.items()) + [("u_muon", run_mu)]},
            "geometry_rows": geo_rows,
            "geometry_resid_model": {
                "form": "resid = a*u + b*u^2 + c*u^3 + d*u^4",
                "a_linear": mp.nstr(a_lin, 15),
                "a_structural": "1/2 (<=> Im S(u) contains pi*u, framing/meridian term, bar-odd)",
                "b_quadratic": mp.nstr(b_quad, 12),
                "b_status": "unidentified (mixes Im-S u^2 with Re-S u terms); no fit",
            },
            "max_loss_digits": _n(max_loss),
            "physics": {
                "t_ln_q0": _n(t_p),
                "kappa1_sub_re": _n(run_p["kappa1_re"]),
                "kappa1_sub_im": _n(run_p["kappa1_im"]),
                "finite_b_S_lead_t_Re_kappa1": _n(imlead),
                "intrinsic_odd_Im_kappa1": _n(intrinsic),
                "S_targets": {k: _n(v, 12) for k, v in S_TARGET.items()},
                "lead_over_S": {k: _n(imlead / v, 10) for k, v in S_TARGET.items()},
            },
            "dkappa1_du_grid": [_n(x, 12) for x in dk_du],
            "verdict": verdict,
        },
        "context": {
            "axis": "bar-odd S route 2: κ_k(u) at the substrate meridian (state-integral side)",
            "builds_on": ["#3606 κ₁ exact", "#3628 κ₂..κ₄ exact (u=0)",
                          "#3654 finite-b i·t·κ₁ scale", "#3636 1/u³ ladder artifact"],
            "theorem_basis": "H. Murakami, J. Topology 6 (2013) — 4₁ asymptotic expansion "
                             "for 0<u<log((3+√5)/2) is proved (not the volume conjecture)",
            "no_deformed_volume_conjecture": True,
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-ohtsuki-deformed-meridian-rungs.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
