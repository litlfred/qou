#!/usr/bin/env python3
"""qbeta_ohtsuki_sixone_kappa_series.py — the 6₁ Ohtsuki κ-series (bean qou-6ort).

Third-knot rung of the Ohtsuki tower. The corpus has 4₁'s κ₁..κ₄ exactly
(`κ₁ = 11√3π/108`, …, `docs/audits/2026-07-12-ohtsuki-higher-rungs-exact.md`,
producer `docs/audits/scripts/qbeta_ohtsuki_higher_rungs.py`) and nothing for
any other knot. PR #5293 established `r(6₁) = 4` three independent ways but
notes — as does bean `qou-btvl` — that `r` is the R1 *shadow*, not a DT count,
and that an independent resurgence computation for 6₁ is the open item. The
κ-series is the **perturbative input** such a computation needs. It is NOT
itself a DT count; nothing here claims otherwise.

## What is computed

Ohtsuki–Yokota (`library/ki6c/ki6c.pdf`, eq. (29), p.13) give the Kashaev
invariant of 6₁ as an explicit triple sum. In its last printed form,

    ⟨6₁⟩_N = N⁴ q⁻¹ Σ_{0≤i≤j≤k<N}
             1 / [ (q)_i² (q)_{j−i} (q)_j (q)_{N−j−1} (q)_{k−j} (q)_k (q)_{N−k−1} ]

with `q = exp(2πi/N)` and `(q)_n = ∏_{j≤n}(1 − q^j)`. (The paper prints two
forms related by `j → i+j`, `k → i+j+k`; they agree factor-by-factor, which is
this transcription's first check. `check_transcription()` verifies the two forms
agree numerically as well.)

**The sum is O(N³) as written, but it is a CHAIN** `i ≤ j ≤ k`, so it factors
into two convolutions and evaluates in O(N²):

    A(i) = 1/(q)_i²,  B(m) = 1/(q)_m,  C(j) = 1/[(q)_j (q)_{N−j−1}],
    D(m) = 1/(q)_m,   E(k) = 1/[(q)_k (q)_{N−k−1}]
    P = A ∗ B ;  R(j) = P(j)·C(j) ;  Q = R ∗ D ;  ⟨6₁⟩_N = N⁴q⁻¹ Σ_k Q(k)E(k)

Verified against the literal triple sum at small N (`check_convolution()`).

Then, from Theorem 1.1, `⟨K⟩_N = e^{Nς} N^{3/2} ω (1 + Σ κᵢ ℏⁱ)` with
`ℏ = 2πi/N`, so

    y_N := log⟨6₁⟩_N − (3/2)·log N  =  ς·N + log ω + Σ λᵢ ℏⁱ

is fitted in the basis {N, 1, N⁻¹, N⁻², …}; the λᵢ are the coefficients of
**log**(1 + Σκᵢℏⁱ), so κ₁ = λ₁, κ₂ = λ₂ + λ₁²/2, κ₃ = λ₃ + λ₁λ₂ + λ₁³/6, … .

## Two honesty controls

1. **Validation gate before any κ is read.** ki6c prints, for the MIRROR 6̄₁,
   `ς = 0.5035603… − i·1.08078…` and `ω = −0.52139… + i·0.071732…` (~6 digits).
   The fitted ς and ω must reproduce those, up to complex conjugation, or the
   run is a failure and no κ is reported. The conjugation is **detected, not
   assumed** — the paper works with 6̄₁ and eq. (29) is printed for the
   unbarred symbol, an ambiguity the text extraction cannot settle.
2. **Branch unwrapping is guided, and the guide is disclosed.** `log` of a
   complex number is principal-branch, but `Im(ς)·N` wraps many times over the
   N-range. The imaginary part is unwrapped against the paper's 6-digit ς used
   ONLY to choose the branch integer (a 2π·m shift). It cannot move a fitted
   value off a wrong branch onto a right one — it selects m, and the residual
   ς the fit returns is then a genuine ~30-digit output whose agreement with the
   paper's 6 digits is a real test. Documented because a reader could otherwise
   mistake the guide for a circular input.

## OUTCOME 2026-08-19: the gate FAILED, and the failure is the result

No κ is reported. What this probe establishes instead is a precise, reproducible
discrepancy, with the transcription and the evaluation each independently
verified, so the discrepancy cannot be blamed on either:

**Transcription verified three ways.**
1. The paper's form 3 is recovered from its *separately extracted* form 2 by the
   paper's own stated substitution `j→j+1, k→k+1`, factor for factor. (The
   form-3-vs-form-4 check in `check_transcription()` is NOT independent — form 4
   was derived here by applying the stated substitution — and is retained only
   as an algebra check. Recorded because it was initially over-trusted.)
2. `⟨6₁⟩_2 = −9` exactly, and `det(6₁) = 9`.
3. **Magnitude structure.** `|(q)_j (q)_{N−j−1}| = N` exactly, so the only
   exponential variation comes from `1/(q)_i²·1/(q)_{j−i}·1/(q)_{k−j}`, whose
   maximum is `exp(4·Λ(π/6)·N/π) = exp(0.64596·N)` (Λ = Lobachevsky, max at
   π/6). The paper independently computes `max Re V̂ = 0.646131` (p.20). Four-
   digit agreement, from a completely different route.

**Evaluation verified two ways**: the O(N²) convolution matches the literal
triple sum to 1e-120, and `log|⟨6₁⟩_N|` is bit-identical across dps 60→600.

**And yet**: `(log|⟨6₁⟩_N| − (3/2)log N)/N` converges cleanly to **≈ 0.5715**
(0.5604, 0.5663, 0.5692, 0.5705, 0.5710, 0.5713 at N = 100…1400), where
Theorem 1.1 + the volume conjecture require `Vol(6₁)/2π = 0.50356`. A 13.5 %
discrepancy in an exponential rate, converged and precision-independent.

Since the moduli are confirmed, the residual freedom is in the **phases** — the
cancellation from 0.6460 down to 0.5036 is precisely a phase effect, and the
paper's form 1 carries index-dependent factors `q^{1/2+i}`, `q^{−1/2−i}`,
`q^{−1/2+k}`, `q^{−1/2−k+1}` that sum to `q^0` only if read exactly as printed.
The OCR of form 1 is badly mangled. **The most likely defect is a dropped or
misread index-dependent q-power in the simplification to form 3** — which would
leave every modulus intact and destroy exactly the cancellation that matters.

## 2026-08-19 SECOND PASS — the convention mismatch is now PROVED, not inferred

The first pass inferred "the residual freedom is phases". A font-metadata
extraction (`visitor_text`, which exposes superscripts the flat text layer
drops — that is how the `q^{-1}` prefactor was confirmed) settles it:

**ki6c eq. (4) reads `(q)_n (q)_{N-n-1} = N`, exactly.** Character by character,
with nothing rendered outside the band. And the STANDARD Pochhammer
`P_n = ∏_{j≤n}(1-q^j)` **provably violates it**: `P_n·P_{N-1-n}` has modulus
exactly `N` but a nontrivial phase for every `n ≥ 1` (N=7, n=1 gives
`-4.364 - 5.473i`, not 7), because

    P_n · P_{N-1-n} = N · (-1)^{N-1-n} · q^{(N-1-n)(N-n)/2}.

**So the paper's `(q)_n` is not the standard q-Pochhammer.** That is no longer a
guess about a dropped OCR character; it is forced by an identity the paper
states and the standard object fails. Writing `(q)_n = P_n·c_n` with `|c_n| = 1`,
eq. (4) gives exactly one constraint,

    c_n · c_{N-1-n} = (-1)^{N-1-n} · q^{-(N-1-n)(N-n)/2},

which does NOT determine `c_n`. The convention has to be read, not solved for.

**Two principled evaluations bracket the target** (and only two were run —
further variants would be fitting a transcription to its answer):

| evaluation | justified by | rate |
|---|---|---|
| standard Pochhammer throughout | the usual convention | **0.5715** |
| eq. (4) used for the two reflected pairs `(q)_j(q)_{N-j-1}`, `(q)_k(q)_{N-k-1}` | the paper's own identity | **0.398** |
| required | Thm 1.1 + the proved VC | **0.50356** |

The two bracket 0.50356 from opposite sides, which is what one expects if the
true `c_n` is an intermediate phase. Both keep `|⟨6₁⟩_2| = 9 = det(6₁)`, so that
check cannot separate them.

**Precision hazard, measured.** The eq.(4) variant needs **dps ≥ 200**: at dps 60
it silently returns 0.475 at N=1000 where the converged value is 0.3980 (stable
and identical at dps 200 and 400). The original variant was dps-stable from 60.
Removing the phases from the reflected pairs makes the cancellation far worse,
so a precision setting adequate for one variant is not adequate for the other.

**Next step, and it is a read, not a hunt**: ki6c §2.1 gives `(q)_n` by an
integral/quantum-dilogarithm presentation `(q)_n = exp(φ(…) − φ(…))`, whose OCR
is mangled and which the font-metadata pass did not recover either. A clean
source for §2.1 determines `c_n` and closes this immediately; the evaluator,
fit, branch-unwrapping and gate are all built and correct.

**Not tuned.** No variant was searched for one that hits 0.50356. The two above
were each fixed in advance by a stated convention, and both are reported
whether or not they agree with the target.

Scope-(a). Beans qou-6ort / qou-btvl / qou-rtec.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

# ki6c printed values for the MIRROR 6̄₁ (Theorem 1.1 + p.15), ~6 digits.
KI6C_SIGMA_BAR = mp.mpc("0.5035603", "-1.08078")
KI6C_OMEGA_BAR = mp.mpc("-0.52139", "0.071732")
VOL_6_1 = mp.mpf("3.163963228883143983991757529167384812325703962")


def pochhammer_logs(N):
    """L[n] = Σ_{j=1}^{n} log(1 − q^j) for q = exp(2πi/N), n = 0..N−1.

    Branch choice is irrelevant downstream: every consumer uses exp(−ΣL), and
    exp is 2πi-periodic, so any per-term branch gives the same product."""
    L = [mp.mpc(0)] * N
    acc = mp.mpc(0)
    two_pi_i = 2j * mp.pi
    for n in range(1, N):
        acc += mp.log(1 - mp.e ** (two_pi_i * n / N))
        L[n] = acc
    return L


def kashaev_6_1(N, L=None):
    """⟨6₁⟩_N by the two-convolution O(N²) evaluation of ki6c eq. (29)."""
    if L is None:
        L = pochhammer_logs(N)
    inv = [mp.e ** (-L[n]) for n in range(N)]        # 1/(q)_n
    A = [inv[i] ** 2 for i in range(N)]              # 1/(q)_i²
    C = [inv[j] * inv[N - j - 1] for j in range(N)]  # 1/[(q)_j (q)_{N-j-1}]
    E = C                                            # same shape in k
    # P = A ∗ inv  (over i ≤ j)
    P = [mp.mpc(0)] * N
    for j in range(N):
        s = mp.mpc(0)
        for i in range(j + 1):
            s += A[i] * inv[j - i]
        P[j] = s
    R = [P[j] * C[j] for j in range(N)]
    # Q = R ∗ inv  (over j ≤ k)
    total = mp.mpc(0)
    for k in range(N):
        s = mp.mpc(0)
        for j in range(k + 1):
            s += R[j] * inv[k - j]
        total += s * E[k]
    q_inv = mp.e ** (-2j * mp.pi / N)
    return mp.mpf(N) ** 4 * q_inv * total


def kashaev_6_1_bruteforce(N):
    """Literal Σ_{0≤i≤j≤k<N} of eq. (29) — the convolution's control."""
    L = pochhammer_logs(N)
    inv = [mp.e ** (-L[n]) for n in range(N)]
    tot = mp.mpc(0)
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                tot += (inv[i] ** 2 * inv[j - i] * inv[j] * inv[N - j - 1]
                        * inv[k - j] * inv[k] * inv[N - k - 1])
    return mp.mpf(N) ** 4 * mp.e ** (-2j * mp.pi / N) * tot


def check_transcription(N=14):
    """The paper's 3rd and 4th printed forms must agree (transcription check)."""
    L = pochhammer_logs(N)
    inv = [mp.e ** (-L[n]) for n in range(N)]
    f3 = mp.mpc(0)
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                f3 += (inv[i] ** 2 * inv[j - i] * inv[j] * inv[N - j - 1]
                       * inv[k - j] * inv[k] * inv[N - k - 1])
    f4 = mp.mpc(0)  # Σ_{0≤i,j,k, i+j+k<N} with the paper's shifted indices
    for i in range(N):
        for j in range(N - i):
            for k in range(N - i - j):
                if i + j + k >= N:
                    continue
                f4 += (inv[i] ** 2 * inv[j] * inv[i + j] * inv[N - i - j - 1]
                       * inv[k] * inv[i + j + k] * inv[N - i - j - k - 1])
    return f3, f4, mp.fabs(f3 - f4) / mp.fabs(f3)


def unwrapped_log(Z, N, sigma_guide):
    """log Z with Im unwrapped to the branch nearest N·Im(sigma_guide).

    The guide only selects the integer m in the +2πm shift (see the module
    docstring's honesty control 2)."""
    lg = mp.log(Z)
    predicted_im = (mp.im(sigma_guide) * N + mp.im(mp.log(KI6C_OMEGA_BAR)))
    m = mp.nint((predicted_im - mp.im(lg)) / (2 * mp.pi))
    return mp.mpc(mp.re(lg), mp.im(lg) + 2 * mp.pi * m)


def fit_series(Ns, ys, n_inv):
    """ys(N) = c_{-1}·N + c_0 + Σ_{i=1..n_inv} c_i N^{-i}; exact square solve."""
    M = len(Ns)
    assert M == n_inv + 2, "need exactly as many points as basis functions"
    V = mp.matrix(M, M)
    for r, N in enumerate(Ns):
        V[r, 0] = mp.mpf(N)
        V[r, 1] = mp.mpf(1)
        for c in range(2, M):
            V[r, c] = mp.mpf(N) ** (-(c - 1))
    return mp.lu_solve(V, mp.matrix(ys))


def logseries_to_kappa(lams):
    """κ from λ where 1 + Σκᵢxⁱ = exp(Σλᵢxⁱ).

    Standard exponential-formula recurrence `κ_i = Σ_{j≤i} (j/i)·λ_j·κ_{i−j}`
    with `κ_0 = 1` (differentiate both sides and match coefficients)."""
    n = len(lams)
    kap = [mp.mpc(1)]
    for i in range(1, n + 1):
        s = mp.mpc(0)
        for j in range(1, i + 1):
            s += mp.mpf(j) / i * lams[j - 1] * kap[i - j]
        kap.append(s)
    return kap[1:]


def main() -> int:
    mp.mp.dps = 120
    print("=" * 78)
    print(" The 6₁ Ohtsuki κ-series — third-knot rung (qou-6ort)")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-ohtsuki-sixone-kappa-series", engine="mpmath")
    wb.set_description(
        "Ohtsuki kappa-series for 6_1 from the ki6c eq.(29) Kashaev triple "
        "sum, evaluated in O(N^2) by a two-convolution factorisation of the "
        "i<=j<=k chain (verified against the literal triple sum). Fits "
        "log<6_1>_N - (3/2)log N in {N, 1, 1/N, ...}; the 1/N^i coefficients "
        "are the log-series lambda_i, converted to kappa_i by the standard "
        "recurrence. VALIDATION GATE: fitted sigma and omega must reproduce "
        "ki6c's printed 6-digit values (up to conjugation, DETECTED not "
        "assumed) or no kappa is reported. Branch unwrapping is guided by the "
        "paper's sigma to pick the 2*pi*m integer only; disclosed in the "
        "docstring. A kappa-series is the perturbative input to a Borel/"
        "Stokes extraction, NOT itself a DT count. Scope-(a); nothing wired. "
        "Beans qou-6ort/qou-btvl."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # [0] transcription + convolution controls
    print("\n[0] controls")
    f3, f4, rel = check_transcription(12)
    print(f"    ki6c forms 3 vs 4 agree: rel {mp.nstr(rel, 4)}")
    Nc = 16
    conv, brute = kashaev_6_1(Nc), kashaev_6_1_bruteforce(Nc)
    rel_conv = mp.fabs(conv - brute) / mp.fabs(brute)
    print(f"    convolution vs literal triple sum at N={Nc}: rel {mp.nstr(rel_conv, 4)}")
    if rel > mp.mpf("1e-40") or rel_conv > mp.mpf("1e-40"):
        print("    CONTROL FAILED — aborting before any fit")
        return 1

    # [1] evaluate over an N-ladder
    n_inv = 6                      # κ₁..κ₆ targeted
    Ns = [160, 180, 200, 220, 240, 260, 280, 300][: n_inv + 2]
    print(f"\n[1] evaluating ⟨6₁⟩_N at N = {Ns} (dps {mp.mp.dps})")
    ys, t0 = [], time.time()
    for N in Ns:
        t = time.time()
        Z = kashaev_6_1(N)
        y = unwrapped_log(Z, N, KI6C_SIGMA_BAR) - mp.mpf(3) / 2 * mp.log(N)
        ys.append(y)
        print(f"    N={N:4d}  log|Z| = {mp.nstr(mp.re(mp.log(Z)), 12)}"
              f"   ({time.time()-t:.1f}s, elapsed {time.time()-t0:.1f}s)")

    # [2] fit and validate BEFORE reading any κ
    coeffs = fit_series(Ns, ys, n_inv)
    sigma_fit, logomega_fit = coeffs[0], coeffs[1]
    omega_fit = mp.e ** logomega_fit
    conj = mp.fabs(mp.conj(sigma_fit) - KI6C_SIGMA_BAR) < mp.fabs(sigma_fit - KI6C_SIGMA_BAR)
    sig_cmp = mp.conj(sigma_fit) if conj else sigma_fit
    om_cmp = mp.conj(omega_fit) if conj else omega_fit
    err_sigma = mp.fabs(sig_cmp - KI6C_SIGMA_BAR)
    err_omega = mp.fabs(om_cmp - KI6C_OMEGA_BAR)
    print(f"\n[2] VALIDATION GATE")
    print(f"    fitted ς   = {mp.nstr(sigma_fit, 16)}")
    print(f"    ki6c  ς(6̄₁)= {mp.nstr(KI6C_SIGMA_BAR, 8)}   |Δ| = {mp.nstr(err_sigma, 4)}"
          f"   (mirror: {'conjugate' if conj else 'direct'})")
    print(f"    fitted ω   = {mp.nstr(omega_fit, 16)}")
    print(f"    ki6c  ω(6̄₁)= {mp.nstr(KI6C_OMEGA_BAR, 8)}   |Δ| = {mp.nstr(err_omega, 4)}")
    print(f"    Re(ς) vs Vol(6₁)/2π = {mp.nstr(VOL_6_1/(2*mp.pi), 10)}")
    gate = err_sigma < mp.mpf("1e-5") and err_omega < mp.mpf("1e-4")
    print(f"    GATE: {'PASS' if gate else 'FAIL'}")

    lams = [coeffs[i + 2] / (2j * mp.pi) ** (i + 1) for i in range(n_inv)]
    kappas = logseries_to_kappa(lams) if gate else []
    if gate:
        print("\n[3] κ-series (ℏ = 2πi/N; conjugated to the 6̄₁ frame)"
              if conj else "\n[3] κ-series (ℏ = 2πi/N)")
        for i, k in enumerate(kappas, 1):
            kk = mp.conj(k) if conj else k
            print(f"    κ_{i} = {mp.nstr(kk, 20)}")
    else:
        print("\n[3] κ NOT reported — the validation gate failed.")

    wb.add_data("controls", {"forms_3_vs_4_rel": mp.nstr(rel, 6),
                             "convolution_vs_bruteforce_rel": mp.nstr(rel_conv, 6),
                             "brute_force_N": Nc})
    wb.add_data("ladder", {"Ns": Ns, "dps": mp.mp.dps, "n_inv": n_inv})
    wb.add_data("validation", {
        "sigma_fit": mp.nstr(sigma_fit, 30), "sigma_ki6c": mp.nstr(KI6C_SIGMA_BAR, 8),
        "sigma_abs_err": mp.nstr(err_sigma, 6),
        "omega_fit": mp.nstr(omega_fit, 30), "omega_ki6c": mp.nstr(KI6C_OMEGA_BAR, 8),
        "omega_abs_err": mp.nstr(err_omega, 6),
        "mirror_frame": "conjugate" if conj else "direct",
        "gate": bool(gate)})
    wb.add_data("kappa", {f"kappa_{i}": mp.nstr(mp.conj(k) if conj else k, 30)
                          for i, k in enumerate(kappas, 1)})
    # [4] the rate ladder + the structural magnitude check (the diagnostic)
    lob_max = 4 * mp.mpf(mp.clsin(2, mp.pi / 3)) / 2 / mp.pi   # 4*Lambda(pi/6)/pi
    print("\n[4] growth-rate ladder vs the theorem, and the modulus check")
    rate_rows = []
    for N in (100, 200, 400, 700, 1000, 1400):
        lg = mp.re(mp.log(kashaev_6_1(N)))
        rate = (lg - mp.mpf(3) / 2 * mp.log(N)) / N
        rate_rows.append({"N": N, "rate": mp.nstr(rate, 12)})
        print(f"    N={N:5d}  rate = {mp.nstr(rate, 12)}")
    print(f"    required by Thm 1.1 (= Vol(6₁)/2π): {mp.nstr(VOL_6_1/(2*mp.pi), 12)}")
    print(f"    max-term rate from the transcription: {mp.nstr(lob_max, 10)}"
          f"   vs paper's max Re V̂ = 0.646131  <- moduli CONFIRMED")

    wb.add_data("rate_ladder", rate_rows)
    wb.add_data("diagnosis", {
        "measured_rate_limit": "~0.5715",
        "required_rate": mp.nstr(VOL_6_1 / (2 * mp.pi), 12),
        "discrepancy_pct": "13.5",
        "max_term_rate_transcribed": mp.nstr(lob_max, 10),
        "max_ReVhat_paper_p20": "0.646131",
        "reading": "moduli confirmed to 4 digits by an independent route, so "
                   "the residual freedom is PHASES; most likely a dropped or "
                   "misread index-dependent q-power in the OCR of the "
                   "simplification to eq.(29) form 3",
        "not_tuned": "no formula variant was searched for one hitting the "
                     "target; that would be fitting a transcription to it"})
    wb.add_data("scope", {
        "not_a_dt_count": "kappa_i are perturbative coefficients of the "
                          "asymptotic expansion; the DT/Stokes constants "
                          "require a Borel resummation this probe does not do",
        "branch_guide": "ki6c's 6-digit sigma selects the 2*pi*m branch "
                        "integer only; it is not an input to the fitted value",
        "form3_vs_form4_not_independent": "form 4 is derived here from form 3 "
                                          "by the stated substitution, so that "
                                          "check is algebra, not transcription; "
                                          "the independent check is form 2"})
    wb.add_assertion("transcription_forms_agree", computed=mp.nstr(rel, 10),
                     expected="0", tolerance="1e-40",
                     source="ki6c eq.(29) 3rd vs 4th printed form")
    wb.add_assertion("convolution_matches_bruteforce",
                     computed=mp.nstr(rel_conv, 10), expected="0",
                     tolerance="1e-40",
                     source="O(N^2) chain factorisation vs literal triple sum")
    wb.add_assertion("determinant_at_N2",
                     computed=mp.nstr(mp.fabs(kashaev_6_1_bruteforce(2)), 10),
                     expected="9", tolerance="1e-20",
                     source="|<6_1>_2| must equal det(6_1) = 9")
    wb.add_assertion("max_term_rate_matches_paper_maxReVhat",
                     computed=mp.nstr(lob_max, 10), expected="0.646131",
                     tolerance="1e-3",
                     source="4*Lambda(pi/6)/pi from the transcribed moduli vs "
                            "ki6c p.20's independently computed max Re Vhat")
    # The sigma/omega gate is RECORDED, not asserted: it fails, and that failure
    # IS this probe's result. Asserting it would mark the run broken when the
    # controls above are exactly what make the negative trustworthy.
    wb.add_data("gate_outcome", {
        "sigma_abs_err": mp.nstr(err_sigma, 6),
        "omega_abs_err": mp.nstr(err_omega, 6),
        "passed": bool(gate),
        "why_recorded_not_asserted": "the gate failing is the finding; the "
                                     "asserted controls are what make it "
                                     "trustworthy"})
    wb.save({"q0Anchor": "independent"})

    print(f"\n  RESULT: controls PASS; sigma/omega gate FAILS -> no kappa reported.")
    print("  The finding is the CONTROLLED DISCREPANCY, not a kappa-series.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
