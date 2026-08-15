#!/usr/bin/env python3
"""s013 route 1 (owner redirect, 2026-07-03): larger-D Seifert data — Σ(3,4,5) executed, and
the constancy exclusion that closes the route as a class.

After the D=2 golden-row refutation on Σ(2,3,5) (`keystone_valuemap_genuine_smatrix_s013.py`,
merged #3208), the owner directed exploring (1) larger-D Seifert data and (2) colored
Ẑ/GPPV blocks. This probe executes (1) on the count-matching candidate and then closes the
route generically:

Σ(3,4,5) is the minimal Brieskorn sphere whose flat-connection count MATCHES the target:
D(3,4,5) = (2·3·4)/4 = 6 vector-valued components, of which γ(3,4,5) = 4 contribute flat
connections — exactly the 4 conjugation classes of bwS0 = d_q/D at n=5. Hikami
(math-ph/0405028, library/arxiv-math-ph-0405028v2/0405028v2.pdf, §5 example) gives the explicit data; everything
transcribed is machine-validated before use:

  (χ)  χ^{(ℓ)}_{2P} from eq. (3.1) at p=(3,4,5), P=60 — the (1,1,1) table must reproduce the
       paper's printed table (+1 on {13,67,77,83}, −1 on {37,43,53,107} mod 120).
  (Φ̃N) eq. (4.3) with the phase exponent (P/2)(1+Σℓⱼ/pⱼ)² (mod 2): must reproduce the
       printed Φ̃^{(ℓ)}(N) — zero for (1,1,1),(1,1,2) (Σnχ = 0, the eq.-4.10 selection),
       and −2·e^{∓…πiN} phases for the 4 flat components, i.e. CS = 119/240, −49/240,
       −1/60, 11/60. Cross-manifold consistency: the same rule reproduces Σ(2,3,5)'s
       CS = −1/120, −49/120.
  (τ/T9) τ_N from eq. (2.11); φ(3,4,5) from Dedekind sums (2.12); Theorem 9 (its hypothesis
       Σ1/pⱼ < 1 HOLDS for (3,4,5), unlike (2,3,5)):
       e^{2πi(φ/4−1/2)/N}(e^{2πi/N}−1)τ_N = ½Φ̃^{(1,1,1)}(1/N) — EXACT at finite N.
  (S)  The 6×6 S-matrix from eq. (3.8): involution S²=1; the vacuum row's 4 flat entries
       must match the printed Corollary-11 weights (1/√5)(sin π/5, sin 2π/5, √2 sin 2π/5,
       √2 sin π/5) in magnitude.
  (P8) Prop. 8 assembled mechanically (no printed shortcut): Φ̃^{(111)}(1/N) ≈
       −√N e^{−πi/4} Σ_{ℓ'} S^{ℓ'}_{(111)} Φ̃^{(ℓ')}(−N) + L-tail — residuals decrease in N.

VALUE SCREEN (route 1 executed): the 4 flat vacuum-row magnitudes have ratios
(1, √2, φ, √2·φ) ≈ (1, 1.414, 1.618, 2.288) under the canonical magnitude-monotone
assignment — vs bwS0 targets d_q = (1, 4.110, 5.220, 6.220) and classical dims (1,4,5,6):
REFUTED. The 4 flat channel functions Φ̃^{(ℓ)}(1/q₀) are screened identically.

CONSTANCY EXCLUSION (route 1 closed as a class — scope (b) with the invariant cited):
for ANY fixed Seifert/plumbed manifold and any finite colouring, the false-theta S-matrix
(eq. 3.8 and its plumbed generalizations) is a CONSTANT matrix of algebraic numbers
(products of sines at rational angles) — independent of q. The keystone target
bwS0(λ; q) = d_q(λ)/D(q) has ratios that are NONCONSTANT functions of q (invariant:
d_q(4,1)/d_q(5) = [4]_q = q³+q+q⁻¹+q⁻³ is strictly increasing for q > 1 — verified
numerically here at two anchors; trivially provable, Lean follow-up candidate). Hence no
constant geometric vacuum row can realize the fibre-level identity `BWVacuumRowIsHecke`
(stated over the q-family); a single-anchor numerical coincidence would be exactly the
fitted-coincidence failure mode the three-calibration discipline rejects. Route 2 (colored
Ẑ/F_K blocks) survives precisely because those are q-FUNCTIONS, not constants.

# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694  (math-ph/0405028; eqs. 2.11,
#      2.12, 3.1, 3.8, 4.2, 4.3, 5.1, Cor. 11 + §5 Σ(3,4,5) example)
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf, mpc, bernpoly, factorial  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40
I = mpc(0, 1)
Q0 = mpf("1.1099785955541805")

PVEC = (3, 4, 5)
P = 60
TWO_P = 120
# the 6 independent triples (Hikami §5, Σ(3,4,5) example), first two non-flat
TRIPLES = ((1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 1), (1, 2, 2))
FLAT = TRIPLES[2:]
# printed paper table for chi^(111)_120 and Cor-11 weights (validation targets)
PRINTED_CHI111 = {13: 1, 37: -1, 43: -1, 53: -1, 67: 1, 77: 1, 83: 1, 107: -1}
PRINTED_CS = {(1, 1, 3): Fraction(119, 240), (1, 1, 4): Fraction(-49, 240),
              (1, 2, 1): Fraction(-1, 60), (1, 2, 2): Fraction(11, 60)}


def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


D_Q = {"(5)": mpf(1), "(4,1)": qint(4), "(3,2)": qint(5),
       "(3,1,1)": qint(4) * qint(3) / qint(2)}


# ── (χ) eq. (3.1), general (p1,p2,p3) ───────────────────────────────────────
def chi_table(triple, pvec, Pv):
    out: dict[int, int] = {}
    for e1 in (-1, 1):
        for e2 in (-1, 1):
            for e3 in (-1, 1):
                val = Fraction(Pv) * (1 + Fraction(e1 * triple[0], pvec[0])
                                      + Fraction(e2 * triple[1], pvec[1])
                                      + Fraction(e3 * triple[2], pvec[2]))
                assert val.denominator == 1
                r = int(val) % (2 * Pv)
                out[r] = out.get(r, 0) + (1 if e1 * e2 * e3 == -1 else -1)
    return {r: v for r, v in out.items() if v}


def chi_fn(table, Pv):
    def chi(n):
        return table.get(n % (2 * Pv), 0)
    return chi


# ── (Φ̃N) eq. (4.3): Φ̃^{(ℓ)}(N) = −(Σnχ/2P)·e^{πiN·(P/2)(1+Σℓj/pj)² mod 2} ──
def sum_n_chi(table, Pv):
    return sum(n * v for n, v in table.items())


def cs_phase_exponent(triple, pvec, Pv):
    """(P/2)(1+Σℓj/pj)² reduced mod 2 → the e^{πiN·(…)} exponent; CS = exponent/2 − 1 shift
    convention aside, compare directly against printed phases."""
    s = 1 + sum(Fraction(l, p) for l, p in zip(triple, pvec))
    e = Fraction(Pv, 2) * s * s
    # reduce mod 2 into (−1, 1]
    e = e - 2 * ((e + 1) // 2)  # Fraction floor-div by 1 → integer part
    return e


# ── (τ) eq. (2.11) + φ from Dedekind sums ───────────────────────────────────
def dedekind_s(b, a):
    return mp.fsum(mp.cot(mp.pi * k / a) * mp.cot(mp.pi * k * b / a)
                   for k in range(1, a)) / (4 * a)


def phi_seifert(pvec, Pv):
    return (3 - mpf(1) / Pv
            + 12 * (dedekind_s(pvec[1] * pvec[2], pvec[0])
                    + dedekind_s(pvec[0] * pvec[2], pvec[1])
                    + dedekind_s(pvec[0] * pvec[1], pvec[2])))


def tau_N(N, pvec, Pv, phi):
    pref = mp.e ** (2 * mp.pi * I / N * (phi / 4 - mpf(1) / 2)) \
        * (mp.e ** (2 * mp.pi * I / N) - 1)
    total = mpc(0)
    for n in range(2 * Pv * N):
        if n % N == 0:
            continue
        num = mpc(1)
        for pj in pvec:
            num *= (mp.e ** (n * mp.pi * I / (N * pj))
                    - mp.e ** (-n * mp.pi * I / (N * pj)))
        den = mp.e ** (n * mp.pi * I / N) - mp.e ** (-n * mp.pi * I / N)
        total += mp.e ** (-n * n * mp.pi * I / (2 * Pv * N)) * num / den
    rhs = mp.e ** (mp.pi * I / 4) / (2 * mp.sqrt(mpf(2 * Pv * N))) * total
    return rhs / pref


def eichler_at_1_over_N(chi, N, Pv):
    return mp.fsum((chi(n) * (1 - mpf(n) / (Pv * N))
                    * mp.e ** (n * n * mp.pi * I / (2 * Pv * N)))
                   for n in range(Pv * N + 1) if chi(n))


# ── (S) eq. (3.8) ───────────────────────────────────────────────────────────
def s_entry(l, lp, pvec, Pv):
    expo = Fraction(1 + Pv)
    for lj, lpj, pj in zip(l, lp, pvec):
        expo += Fraction(Pv * (lj + lpj), pj)
    cross = (l[1] * lp[2] - l[2] * lp[1]) * pvec[0] \
        + (l[2] * lp[0] - l[0] * lp[2]) * pvec[1] \
        + (l[0] * lp[1] - l[1] * lp[0]) * pvec[2]
    expo += cross
    assert expo.denominator == 1
    sign = (-1) ** (int(expo) % 2)
    prod = mpf(1)
    for lj, lpj, pj in zip(l, lp, pvec):
        prod *= mp.sin(mp.pi * Pv * lj * lpj / (pj * pj))
    return mp.sqrt(mpf(32) / Pv) * sign * prod


def l_value(chi, k, Pv):
    return (-mpf(2 * Pv) ** (2 * k) / (2 * k + 1)
            * mp.fsum(chi(j) * bernpoly(2 * k + 1, mpf(j) / (2 * Pv))
                      for j in range(1, 2 * Pv + 1) if chi(j)))


def run():
    out = {"pvec": list(PVEC), "P": P, "q0": float(Q0)}
    tables = {t: chi_table(t, PVEC, P) for t in TRIPLES}
    chi111 = chi_fn(tables[(1, 1, 1)], P)

    # (χ) printed-table validation + weights pure-sign
    out["chi111_matches_printed_table"] = tables[(1, 1, 1)] == PRINTED_CHI111
    out["all_weights_pm1"] = all(abs(v) == 1 for t in tables.values()
                                 for v in t.values())

    # (Φ̃N) selection + CS phases vs printed
    sums = {t: sum_n_chi(tables[t], P) for t in TRIPLES}
    out["sum_n_chi"] = {str(t): s for t, s in sums.items()}
    out["nonflat_have_zero_sum"] = sums[(1, 1, 1)] == 0 and sums[(1, 1, 2)] == 0
    # Φ̃^{(ℓ)}(N) = −(Σnχ/2P)e^{…} = −2e^{…} (printed) ⇔ Σnχ = 4P
    out["flat_have_sum_4P"] = all(sums[t] == 4 * P for t in FLAT)
    cs_ok = {}
    for t in FLAT:
        e = cs_phase_exponent(t, PVEC, P)
        # Hikami's convention (§5 examples): Φ̃(N) = −2 e^{aπiN} "indicates CS = −a/2"
        # (e.g. Σ(2,3,5): a = 1/60 ↔ CS = −1/120). So a ≡ −2·CS (mod 2).
        target = Fraction(-2) * PRINTED_CS[t]
        cs_ok[str(t)] = (e - target) % 2 == 0
    out["cs_phases_match_printed"] = cs_ok
    out["cs_all_match"] = all(cs_ok.values())
    # cross-manifold consistency: same rule on Σ(2,3,5) gives CS = −1/120, −49/120
    cs235 = {t: cs_phase_exponent(t, (2, 3, 5), 30) for t in ((1, 1, 1), (1, 1, 2))}
    out["cs_235_consistency"] = (
        (cs235[(1, 1, 1)] - Fraction(1, 60)) % 2 == 0
        and (cs235[(1, 1, 2)] - Fraction(49, 60)) % 2 == 0)

    # (τ/T9) Theorem 9 exact (hypothesis Σ1/pj = 47/60 < 1 holds)
    phi = phi_seifert(PVEC, P)
    out["phi_345"] = float(phi)
    out["phi_equals_49_over_60"] = bool(abs(phi - mpf(49) / 60) < mpf("1e-30"))
    t9 = {}
    for N in (3, 5, 7):
        lhs = (mp.e ** (2 * mp.pi * I / N * (phi / 4 - mpf(1) / 2))
               * (mp.e ** (2 * mp.pi * I / N) - 1) * tau_N(N, PVEC, P, phi))
        rhs = eichler_at_1_over_N(chi111, N, P) / 2
        t9[str(N)] = float(abs(lhs - rhs))
    out["theorem9_residuals"] = t9
    out["theorem9_exact"] = all(v < 1e-28 for v in t9.values())

    # (S) 6×6 S-matrix: involution + vacuum-row flat entries vs printed Cor-11 weights
    S = [[s_entry(a, b, PVEC, P) for b in TRIPLES] for a in TRIPLES]
    n_t = len(TRIPLES)
    s2max = max(abs(mp.fsum(S[i][k] * S[k][j] for k in range(n_t))
                    - (1 if i == j else 0))
                for i in range(n_t) for j in range(n_t))
    out["S_squared_is_identity"] = bool(s2max < mpf("1e-30"))
    row = {str(t): float(S[0][j]) for j, t in enumerate(TRIPLES)}
    out["vacuum_row"] = row
    printed_w = {(1, 1, 3): mp.sin(mp.pi / 5) / mp.sqrt(mpf(5)),
                 (1, 1, 4): mp.sin(2 * mp.pi / 5) / mp.sqrt(mpf(5)),
                 (1, 2, 1): mp.sqrt(mpf(2)) * mp.sin(2 * mp.pi / 5) / mp.sqrt(mpf(5)),
                 (1, 2, 2): mp.sqrt(mpf(2)) * mp.sin(mp.pi / 5) / mp.sqrt(mpf(5))}
    out["flat_row_matches_printed_weights"] = all(
        abs(abs(S[0][TRIPLES.index(t)]) - w) < mpf("1e-30")
        for t, w in printed_w.items())

    # (P8) Prop 8 assembled mechanically — residual decreases in N
    def phit_at_minus_N(t, N):
        e = cs_phase_exponent(t, PVEC, P)
        return -(mpf(sums[t]) / (2 * P)) * mp.e ** (-mp.pi * I * N
                                                    * mpf(e.numerator) / e.denominator)
    p8 = {}
    for N in (25, 51, 101):
        lhs = eichler_at_1_over_N(chi111, N, P)
        flat_part = (-mp.sqrt(mpf(N)) * mp.e ** (-mp.pi * I / 4)
                     * mp.fsum(S[0][TRIPLES.index(t)] * phit_at_minus_N(t, N)
                               for t in TRIPLES if sums[t]))
        tail = mp.fsum(l_value(chi111, k, P) / factorial(k)
                       * (mp.pi * I / (2 * P * N)) ** k for k in range(9))
        p8[str(N)] = float(abs(lhs - flat_part - tail))
    out["prop8_residuals"] = p8
    out["prop8_residuals_decrease"] = p8["25"] > p8["51"] > p8["101"]

    # VALUE SCREEN — the count-matching γ=4 row vs the 4 bwS0 classes
    mags = sorted(float(abs(S[0][TRIPLES.index(t)])) for t in FLAT)
    ratios = [m / mags[0] for m in mags]
    dq_sorted = sorted(float(v) for v in D_Q.values())
    dq_ratios = [v / dq_sorted[0] for v in dq_sorted]
    out["flat_row_ratios_sorted"] = ratios
    out["dq_ratios_sorted"] = dq_ratios
    out["classical_ratios"] = [1.0, 4.0, 5.0, 6.0]
    out["value_screen_refuted"] = not all(
        abs(a - b) < 1e-6 for a, b in zip(ratios, dq_ratios))
    out["classical_screen_refuted"] = not all(
        abs(a - b) < 1e-6 for a, b in zip(ratios, [1.0, 4.0, 5.0, 6.0]))

    # channel-function screen: Φ̃^{(ℓ)}(q=1/q₀) for the 4 flat components
    qv = 1 / Q0
    chan = {}
    for t in FLAT:
        chi = chi_fn(tables[t], P)
        chan[str(t)] = float(mp.fsum(chi(n) * qv ** (mpf(n * n) / (4 * P))
                                     for n in range(0, 6000) if chi(n)))
    out["flat_channels_at_inv_q0"] = chan
    cvals = sorted(abs(v) for v in chan.values())
    cratios = [v / cvals[0] for v in cvals]
    out["channel_ratios_sorted"] = cratios
    out["channel_screen_refuted"] = not all(
        abs(a - b) < 1e-6 for a, b in zip(cratios, dq_ratios))

    # CONSTANCY EXCLUSION — the invariant, numerically witnessed at two anchors
    def dq41_ratio(q):
        return float((q ** 4 - q ** -4) / (q - q ** -1))
    out["dq41_at_q0"] = dq41_ratio(Q0)
    out["dq41_at_1p05"] = dq41_ratio(mpf("1.05"))
    out["dq_ratios_nonconstant_in_q"] = abs(
        out["dq41_at_q0"] - out["dq41_at_1p05"]) > 1e-3
    return out


def report(res):
    print("# s013 route 1 — Σ(3,4,5) (γ=4 count-match) executed + constancy exclusion\n")

    print("## Transcription validation (all from library/arxiv-math-ph-0405028v2/0405028v2.pdf)\n")
    print(f"- χ^(111)_120 equals the paper's printed table: "
          f"**{res['chi111_matches_printed_table']}**; all weights ±1: "
          f"**{res['all_weights_pm1']}**")
    print(f"- flat selection: Σnχ = 0 for (1,1,1),(1,1,2) (**{res['nonflat_have_zero_sum']}**); "
          f"= 4P for the 4 flat (**{res['flat_have_sum_4P']}**) — γ(3,4,5)=4")
    print(f"- CS phases from (P/2)(1+Σℓ/p)² mod 2 match printed (119/240, −49/240, −1/60, "
          f"11/60): **{res['cs_all_match']}**; same rule on Σ(2,3,5) gives −1/120, −49/120: "
          f"**{res['cs_235_consistency']}**")
    print(f"- φ(3,4,5) = {res['phi_345']:.10f} = 49/60: **{res['phi_equals_49_over_60']}**")
    print(f"- Theorem 9 EXACT residuals (its hypothesis holds for (3,4,5)): "
          f"{res['theorem9_residuals']} → **{res['theorem9_exact']}**")
    print(f"- S 6×6: S²=1 **{res['S_squared_is_identity']}**; flat vacuum-row entries = "
          f"printed Cor-11 weights (1/√5)(sinπ/5, sin2π/5, √2sin2π/5, √2sinπ/5): "
          f"**{res['flat_row_matches_printed_weights']}**")
    print(f"- Prop 8 assembled mechanically, residuals {res['prop8_residuals']} "
          f"decreasing: **{res['prop8_residuals_decrease']}**\n")

    print("## Value screen — route 1 executed on the count-matching manifold\n")
    print(f"- flat vacuum-row ratios (sorted): "
          f"{[round(r, 4) for r in res['flat_row_ratios_sorted']]}  (= 1, √2, φ, √2φ)")
    print(f"- bwS0 d_q ratios (sorted):        "
          f"{[round(r, 4) for r in res['dq_ratios_sorted']]}")
    print(f"- classical dims:                  {res['classical_ratios']}")
    print(f"- **REFUTED vs d_q: {res['value_screen_refuted']}; vs classical: "
          f"{res['classical_screen_refuted']}** — the γ=4 count match does not extend to"
          f" values.")
    print(f"- flat channel functions Φ̃^(ℓ)(1/q₀): {res['flat_channels_at_inv_q0']}")
    print(f"  ratios {[round(r, 4) for r in res['channel_ratios_sorted']]} vs d_q — "
          f"**REFUTED: {res['channel_screen_refuted']}**\n")

    print("## Constancy exclusion — route 1 closed as a class (scope (b), invariant cited)\n")
    print("- Any fixed Seifert/plumbed false-theta S-matrix entry is a CONSTANT algebraic")
    print("  number (products of sines at rational angles) — q-independent by construction")
    print("  (eq. 3.8 contains no q).")
    print(f"- The bwS0 ratio d_q(4,1)/d_q(5) = [4]_q is nonconstant in q: "
          f"{res['dq41_at_q0']:.6f} at q₀ vs {res['dq41_at_1p05']:.6f} at q=1.05 "
          f"(**{res['dq_ratios_nonconstant_in_q']}**; trivially provable — Lean follow-up).")
    print("- Hence NO constant geometric vacuum row — any Brieskorn/Seifert manifold, any")
    print("  colouring — can realize the fibre-level identity `BWVacuumRowIsHecke` (a")
    print("  q-family statement). A single-anchor numerical match would be the fitted-")
    print("  coincidence failure mode the discipline rejects. Route 1 is CLOSED.")
    print("- Route 2 (colored Ẑ/F_K blocks) survives precisely because homological blocks")
    print("  are q-FUNCTIONS, not constants — the type-correct carrier class.")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("keystone-route1-sigma345-constancy-s013", engine="mpmath")
    w.set_description(
        "s013 route 1 (owner redirect): larger-D Seifert executed on the count-matching "
        "Sigma(3,4,5) (D=6, gamma=4 flat connections = 4 bwS0 classes) and closed as a "
        "class. Transcription from library/arxiv-math-ph-0405028v2/0405028v2.pdf machine-validated: chi^(111)_120 "
        "= printed table; Sum n*chi selection (0 for the two non-flat, 4P for the 4 flat); "
        "CS phases from (P/2)(1+Sum l/p)^2 mod 2 = printed (119/240,-49/240,-1/60,11/60) "
        "and reproduce Sigma(2,3,5)'s -1/120,-49/120; phi(3,4,5)=49/60 from Dedekind sums; "
        "Theorem 9 EXACT to ~1e-30 at N=3,5,7; S(6x6)^2=1; flat vacuum-row entries = "
        "printed Cor-11 weights (1/sqrt5)(sin pi/5, sin 2pi/5, sqrt2 sin 2pi/5, sqrt2 "
        "sin pi/5); Prop 8 assembled mechanically with decreasing residuals. VALUE SCREEN: "
        "flat-row ratios (1, sqrt2, phi, sqrt2*phi) ~ (1,1.414,1.618,2.288) vs d_q "
        "(1,4.110,5.220,6.220) and classical (1,4,5,6): REFUTED — the gamma=4 count match "
        "does not extend to values; flat channel functions at 1/q0 likewise refuted. "
        "CONSTANCY EXCLUSION (scope (b), invariant cited): every fixed Seifert/plumbed "
        "S-matrix entry is a constant algebraic number (no q in eq. 3.8) while "
        "d_q(4,1)/d_q(5)=[4]_q is nonconstant in q (numerically witnessed at two anchors; "
        "trivially provable) — no constant geometric vacuum row can realize the fibre-level "
        "BWVacuumRowIsHecke; single-anchor matches are the fitted-coincidence mode the "
        "discipline rejects. Route 1 CLOSED; route 2 (colored Zhat/F_K blocks, q-functions) "
        "is the surviving type-correct carrier class. No fit; nothing wired."
    )
    for key in ("pvec", "P", "q0", "chi111_matches_printed_table", "all_weights_pm1",
                "sum_n_chi", "nonflat_have_zero_sum", "flat_have_sum_4P",
                "cs_phases_match_printed", "cs_all_match", "cs_235_consistency",
                "phi_345", "phi_equals_49_over_60", "theorem9_residuals",
                "theorem9_exact", "S_squared_is_identity", "vacuum_row",
                "flat_row_matches_printed_weights", "prop8_residuals",
                "prop8_residuals_decrease", "flat_row_ratios_sorted",
                "dq_ratios_sorted", "classical_ratios", "value_screen_refuted",
                "classical_screen_refuted", "flat_channels_at_inv_q0",
                "channel_ratios_sorted", "channel_screen_refuted",
                "dq41_at_q0", "dq41_at_1p05", "dq_ratios_nonconstant_in_q"):
        w.add_data(key, res[key])
    w.add_assertion(
        "route1_sigma345_refuted_and_constancy_exclusion_established",
        computed=1 if (res["chi111_matches_printed_table"] and res["theorem9_exact"]
                       and res["S_squared_is_identity"]
                       and res["flat_row_matches_printed_weights"]
                       and res["prop8_residuals_decrease"]
                       and res["cs_all_match"] and res["cs_235_consistency"]
                       and res["value_screen_refuted"]
                       and res["channel_screen_refuted"]
                       and res["dq_ratios_nonconstant_in_q"]) else 0,
        expected=1, tolerance=0,
        source="Sigma(3,4,5) transcription fully machine-validated (printed chi table, "
               "Theorem 9 exact, S^2=1, printed Cor-11 weights, mechanical Prop 8); the "
               "count-matching gamma=4 vacuum row (ratios 1, sqrt2, phi, sqrt2*phi) and its "
               "channel functions are refuted against the 4-class bwS0=d_q/D targets; and "
               "the constancy exclusion (constant algebraic S-entries vs nonconstant-in-q "
               "d_q ratios) closes route 1 as a class at the fibre level.",
    )
    outp = w.save()
    print(f"\nwitness → {outp.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
