#!/usr/bin/env python3
"""s013 — the q-Bessel value-map gate: derive the colored LR residue character, decompose the
colored Σ(2,3,5) family into per-exponent channels, and screen the narrowed q-Bessel candidates.

Bean s013, step 2 (after the compact screen `keystone_valuemap_screen_s013.py` refuted [e]_q,
sin(πe/30), sinh(ηe) and narrowed the target to the non-compact Hahn–Exton q-Bessel vacuum row).
Network access to the primary sources (Lawrence–Rozansky 1999; Hikami arXiv:1811.05376;
Andersen–Mistegård arXiv:2205.01282) is firewalled in this sandbox (arXiv 403), so this probe
restricts itself to what is DERIVABLE AND MACHINE-VERIFIABLE in-repo — nothing quoted from memory:

(A) DERIVE the colored residue character exactly. With x = e^{−z/30}, the colored sinh-product

        2sinh(z/2)·2sinh(z/3)·2sinh(αz/5) / 2sinh(z)  =  num_α(x) · Σ_{k≥0} x^{60k},

    where num_α(x) = (x^{−15}−x^{15})(x^{−10}−x^{10})(x^{−6α}−x^{6α})·x^{30} is a Laurent
    polynomial with ±1 coefficients — an EXACT rational-function statement (sympy, integer
    coefficients; numerically verified at 50 dps). Folding the expansion coefficients into an
    odd 60-periodic character (with a consistency vote across every window occurrence of each
    residue class) DERIVES: the support R(α), the per-class signs, and — decisively — that
    every residue weight is ±1: **the colored LR residue data is PURE SIGN, carrying no
    magnitude structure.** α=1 must and does reproduce the bare validated character
    ({1,11,19,29}, uniform sign), so the value map bwS0 = d_q/D cannot live in the residue
    weights.

(B) DECOMPOSE the colored family into per-exponent channels: Ψ^{(α)} = Σ_{e∈R(α)} Ψ̃^{(e)},
    where Ψ̃^{(e)}(q) = Σ_{n≡±e mod 60} sgn·q^{n²/120} is the odd false-theta channel at E₈
    exponent e. These 8 channel values at 1/q₀ ARE the per-colour, per-block amplitudes the
    value step needs (validation: the α=1 channel sum must reproduce the bare Ψ(1/q₀)≈2.3296).

(C) SCREEN the channel amplitudes as the value map (targets d_q = 1, 4.110, 5.220, 6.220 on the
    dual-pair representatives e = 1,7,11,13), including pair-sum/difference variants, plus the
    ANALYTIC q→1 gate: lim_{q→1⁻} Ψ̃^{(e)}(q) ∝ L(0,χ_e) = (30−e)/30 (Abel/L-value), which
    DECREASES in e while the targets INCREASE — an anchor-independent structural refutation,
    verified numerically at q = 1−ε.

(D) GATE the narrowed q-Bessel-row hypothesis with one degree of freedom: does ANY argument x
    make the vacuum-row ratios match — ordinary Bessel J_e(x) (the E(2) contraction, q→1
    targets = classical dims 1,4,5,6) and Hahn–Exton q-Bessel J_e(x;q̂), q̂ = q₀^{−2}
    (substrate targets d_q)? For each family: pin x by the first ratio (root-enumerate
    J_7 − t₂J_1 over x), then test the two REMAINING ratios at every root (1 dof, 2 net
    checks). Pair-symmetrized rows J_e + J_{30−e} are screened identically. PASS iff some
    root satisfies both cross-checks to 1e−6 relative; the best residual is reported either
    way. No fit is wired anywhere; a failed gate (a)-prunes the single-argument q-Bessel row
    and leaves the genuine E_q(2) q-Hankel/Plancherel kernel (literature-gated) as the open
    value step.

# Ref: [koelink-swarttouw-1994] https://doi.org/10.1006/jmaa.1994.1330  (Hahn–Exton q-Bessel)
# Ref: [gasper-rahman-2004] https://doi.org/10.1017/CBO9780511526251     (₁φ₁ conventions)
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
import sympy as sp  # noqa: E402
from mpmath import mp, mpf, besselj, qp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
with mp.workdps(50):
    Q0 = mpf("1.1099785955541805")
    INV = +(1 / Q0)          # bar image, |q| < 1: where the false theta converges
    QHAT = +(1 / (Q0 ** 2))  # |q|<1 base for the Hahn–Exton q-Bessel (balanced [m]_{q0} image)
P = 30
E8_EXPONENTS = (1, 7, 11, 13, 17, 19, 23, 29)
DUAL_PAIR_REPS = (1, 7, 11, 13)           # e of each Coxeter pair {e, 30-e}
PAIR_PARTNER = {1: 29, 7: 23, 11: 19, 13: 17}
CLASS_OF_REP = {1: "(5)", 7: "(4,1)", 11: "(3,2)", 13: "(3,1,1)"}
BARE_PSI = mpf("2.3296")  # keystone_habiro_wrt_s3_2i_probe value (validation anchor, 4 dp)


def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


with mp.workdps(50):
    D_Q_TARGETS = {1: mpf(1), 7: +qint(4), 11: +qint(5), 13: +(qint(4) * qint(3) / qint(2))}
CLASSICAL_TARGETS = {1: mpf(1), 7: mpf(4), 11: mpf(5), 13: mpf(6)}


# ────────────────────────────────────────────────────────────────────────────
# (A) derive the colored residue character exactly (sympy Laurent expansion)
# ────────────────────────────────────────────────────────────────────────────
def laurent_num_coeffs(alpha: int) -> dict:
    """Exact integer coefficients of num_α(x) = (x^{−15}−x^{15})(x^{−10}−x^{10})
    (x^{−6α}−x^{6α})·x^{30}, as {exponent: coeff}. Exponents lie in [30−25−6α, 30+25+6α]."""
    x = sp.symbols("x")
    shift = 60  # clear negatives for sp.Poly (min exponent ≥ 30−25−24 = −19 > −60)
    num = sp.expand(
        (x ** -15 - x ** 15) * (x ** -10 - x ** 10)
        * (x ** (-6 * alpha) - x ** (6 * alpha)) * x ** 30 * x ** shift
    )
    poly = sp.Poly(num, x)
    return {m[0] - shift: int(c) for m, c in zip(poly.monoms(), poly.coeffs())}


def expansion_coeff(coeffs: dict, n: int) -> int:
    """Coefficient of x^n in num_α(x)·Σ_{k≥0} x^{60k} (the exact LHS expansion)."""
    return sum(coeffs.get(n - 60 * k, 0) for k in range(0, max(1, n // 60 + 2)))


def fold_character(coeffs: dict, window: int = 240):
    """Fold the exact expansion coefficients into an odd 60-periodic character χ̂ on residues
    1..59: every occurrence c(n) ≠ 0 with n ≡ r (mod 60) votes χ̂(r) = c(n); with n ≡ −r votes
    χ̂(r) = −c(n). Returns (χ̂ dict on 1..59, all_votes_consistent, all_weights_pm1).

    The transient region (small n, before eventual periodicity) is exactly where the odd
    reflection places the |n| class at its negative representative (e.g. the |n|=1 class of
    α=1 sits solely at n=−1); the vote mechanism handles this without hand bookkeeping."""
    votes: dict[int, set] = {}
    lo = min(coeffs) if coeffs else 0
    pm1 = True
    for n in range(lo, window + 1):
        c = expansion_coeff(coeffs, n) if n >= lo else 0
        if not c:
            continue
        if abs(c) != 1:
            pm1 = False
        r = n % 60
        if r == 0:
            votes.setdefault(0, set()).add(c)
            continue
        votes.setdefault(r, set()).add(c)
        votes.setdefault(60 - r, set()).add(-c)
    consistent = all(len(v) == 1 for v in votes.values()) and 0 not in votes
    chi_hat = {r: next(iter(v)) for r, v in votes.items() if r != 0}
    return chi_hat, consistent, pm1


def verify_identity_numeric(coeffs: dict) -> mpf:
    """|LHS − truncated exact expansion| at several z (50 dps)."""
    alpha_deg = (max(coeffs) - 30 - 25) // 6  # recover α from the max exponent 30+25+6α
    worst = mpf(0)
    for zv in (mpf(3), mpf(5), mpf(8)):
        lhs = (2 * mp.sinh(zv / 2) * 2 * mp.sinh(zv / 3)
               * 2 * mp.sinh(alpha_deg * zv / 5) / (2 * mp.sinh(zv)))
        xv = mp.e ** (-zv / 30)
        nmax = int(30 * 80 / float(zv)) + 120  # x^n < 1e−34 beyond
        rhs = mp.fsum(c * xv ** n
                      for n in range(min(coeffs), nmax)
                      if (c := expansion_coeff(coeffs, n)))
        worst = max(worst, abs(lhs - rhs))
    return worst


# ────────────────────────────────────────────────────────────────────────────
# (B) per-exponent channels Ψ̃^{(e)} and the colored decomposition
# ────────────────────────────────────────────────────────────────────────────
def channel_value(e: int, q, nterms: int = 6000) -> mpf:
    """Ψ̃^{(e)}(q) = Σ_{n>0} sgn q^{n²/120}, sgn = +1 for n≡e, −1 for n≡60−e (mod 60)."""
    total = mp.fsum(q ** (mpf(n * n) / 120) for n in range(e, nterms, 60))
    total -= mp.fsum(q ** (mpf(n * n) / 120) for n in range(60 - e, nterms, 60))
    return total


# ────────────────────────────────────────────────────────────────────────────
# (D) Bessel-row gate machinery
# ────────────────────────────────────────────────────────────────────────────
def hahn_exton_J(nu: int, x, q, kmax: int = 400):
    """Hahn–Exton (third Jackson) q-Bessel J_ν(x;q) = x^ν (q^{ν+1};q)_∞/(q;q)_∞ ·
    Σ_k (−1)^k q^{k(k−1)/2}/[(q;q)_k(q^{ν+1};q)_k] (q x²)^k  (corpus convention, validated in
    qbeta_qbessel_contiguity_cfinite.py)."""
    pref = x ** nu * qp(q ** (nu + 1), q) / qp(q, q)
    z = q * x * x
    term = mpf(1)
    s = mpf(1)
    for k in range(1, kmax):
        term *= -q ** (k - 1) * z / ((1 - q ** k) * (1 - q ** (nu + k)))
        s += term
        # the alternating series peaks ~1e20 internally before q^{k(k-1)/2} wins; only stop
        # once well past the peak (k>50) and the term is absolutely negligible
        if k > 50 and abs(term) < mpf("1e-45"):
            break
    return pref * s


def gate_row(row_fn, targets, x_max, grid, tol=mpf("1e-6")):
    """1-dof overdetermined gate. row_fn(e, x) → amplitude. Pin x by
    row(7,x) − t₂·row(1,x) = 0 (grid sign changes + bisection); at each root check the two
    remaining ratios. Returns (pass?, n_roots, best) with best = the root minimizing the max
    relative cross-check error."""
    t2 = targets[7] / targets[1]
    t3 = targets[11] / targets[1]
    t4 = targets[13] / targets[1]

    def g(xv):
        return row_fn(7, xv) - t2 * row_fn(1, xv)

    roots = []
    xv = grid
    prev_x, prev_g = xv, g(xv)
    while xv < x_max:
        xv += grid
        cur = g(xv)
        if prev_g == 0 or (prev_g < 0) != (cur < 0):
            a, b, ga = prev_x, xv, prev_g
            for _ in range(70):
                m2 = (a + b) / 2
                gm = g(m2)
                if gm == 0:
                    a = b = m2
                    break
                if (ga < 0) != (gm < 0):
                    b = m2
                else:
                    a, ga = m2, gm
            roots.append((a + b) / 2)
        prev_x, prev_g = xv, cur
    best = None
    for r in roots:
        r1 = row_fn(1, r)
        if abs(r1) < mpf("1e-25"):
            continue
        e3 = abs(row_fn(11, r) / r1 - t3) / t3
        e4 = abs(row_fn(13, r) / r1 - t4) / t4
        err = max(e3, e4)
        if best is None or err < best["max_rel_err"]:
            best = {"x": float(r), "ratio_11": float(row_fn(11, r) / r1),
                    "ratio_13": float(row_fn(13, r) / r1),
                    "target_11": float(t3), "target_13": float(t4),
                    "max_rel_err": float(err)}
    passed = best is not None and best["max_rel_err"] < float(tol)
    return passed, len(roots), best


def run():
    out = {"q0": float(Q0), "inv_q0": float(INV), "qhat": float(QHAT), "P": P}

    # (A) derive + verify the colored residue character
    chars = {}
    for alpha in (1, 2, 3, 4):
        coeffs = laurent_num_coeffs(alpha)
        chi_hat, consistent, pm1 = fold_character(coeffs)
        support = sorted(r for r in chi_hat if r <= 30 and chi_hat[r])
        resid = verify_identity_numeric(coeffs)
        signs_on_support = {str(r): chi_hat[r] for r in support}
        uniform = len({chi_hat[r] for r in support}) == 1
        chars[alpha] = {
            "support_1_30": support,
            "signs_on_support": signs_on_support,
            "sign_uniform_on_support": uniform,
            "global_sign": chi_hat[support[0]] if uniform and support else 0,
            "fold_consistent_odd_periodic": consistent,
            "all_weights_pm1": pm1,
            "identity_residual": float(resid),
        }
    out["derived_characters"] = chars
    out["alpha1_reproduces_bare_support"] = chars[1]["support_1_30"] == [1, 11, 19, 29]
    out["colored_union_is_E8"] = sorted(
        set(chars[1]["support_1_30"]) | set(chars[2]["support_1_30"])) == sorted(E8_EXPONENTS)
    out["residue_weights_are_pure_signs"] = all(
        c["all_weights_pm1"] and c["fold_consistent_odd_periodic"] for c in chars.values())
    out["global_sign_uniform_across_colors"] = len(
        {c["global_sign"] for c in chars.values()}) == 1 and all(
        c["sign_uniform_on_support"] for c in chars.values())

    # (B) per-exponent channel amplitudes at 1/q0 + bare-sum validation
    channels = {e: channel_value(e, INV) for e in E8_EXPONENTS}
    out["channels_at_inv_q0"] = {str(e): float(v) for e, v in channels.items()}
    bare_sum = mp.fsum(channels[e] for e in (1, 11, 19, 29))
    out["bare_channel_sum"] = float(bare_sum)
    out["bare_sum_matches_bare_invariant"] = bool(abs(bare_sum - BARE_PSI) < mpf("5e-4"))

    # (C) channel value screen vs d_q + analytic q→1 gate
    tgt_ratio = {e: float(D_Q_TARGETS[e] / D_Q_TARGETS[1]) for e in DUAL_PAIR_REPS}
    screen = []
    for e in DUAL_PAIR_REPS:
        ch, pt = channels[e], channels[PAIR_PARTNER[e]]
        screen.append({
            "e": e, "class": CLASS_OF_REP[e], "target_dq_ratio": tgt_ratio[e],
            "channel_ratio": float(ch / channels[1]),
            "pair_sum_ratio": float((ch + pt) / (channels[1] + channels[29])),
            "pair_diff_ratio": float((ch - pt) / (channels[1] - channels[29])),
        })
    out["channel_value_screen"] = screen

    def refuted(key):
        return not all(abs(s[key] - s["target_dq_ratio"]) < 1e-6 for s in screen)

    out["channel_refuted"] = refuted("channel_ratio")
    out["pair_sum_refuted"] = refuted("pair_sum_ratio")
    out["pair_diff_refuted"] = refuted("pair_diff_ratio")

    # analytic q→1 gate: Ψ̃^{(e)}(1−ε) ∝ L(0,χ_e) = (30−e)/30
    q1_gate = []
    for eps_s in ("1e-2", "1e-3", "1e-4"):
        eps = mpf(eps_s)
        qv = 1 - eps
        nmax = int((8280 / float(eps)) ** 0.5) + 200
        vals = {e: channel_value(e, qv, nterms=nmax) for e in DUAL_PAIR_REPS}
        lrat = {e: float(vals[e] / vals[1]) for e in DUAL_PAIR_REPS}
        q1_gate.append({"eps": float(eps), "ratios": {str(e): lrat[e] for e in DUAL_PAIR_REPS}})
    lval = {e: float(mpf(30 - e) / 29) for e in DUAL_PAIR_REPS}  # L(0,χ_e)/L(0,χ_1)
    out["q1_gate"] = {"numeric": q1_gate,
                      "L_value_prediction": {str(e): lval[e] for e in DUAL_PAIR_REPS}}
    last = q1_gate[-1]["ratios"]
    out["q1_matches_L_values"] = all(
        abs(last[str(e)] - lval[e]) < 5e-3 for e in DUAL_PAIR_REPS)
    out["q1_channel_ratios_decrease"] = all(
        last[str(a)] > last[str(b)] for a, b in zip(DUAL_PAIR_REPS, DUAL_PAIR_REPS[1:]))

    # (D) Bessel-row gates (1 dof, 2 net checks each)
    gates = {}

    def ord_row(e, xv):
        return besselj(e, xv)

    def ord_row_pair(e, xv):
        return besselj(e, xv) + besselj(30 - e, xv)

    def he_row(e, xv):
        return hahn_exton_J(e, xv, QHAT)

    def he_row_pair(e, xv):
        return hahn_exton_J(e, xv, QHAT) + hahn_exton_J(30 - e, xv, QHAT)

    for name, fn, tg, xmax, grid, dps in (
        ("ordinary_Je_classical", ord_row, CLASSICAL_TARGETS, 60, mpf("0.02"), 30),
        ("ordinary_Je_pair_classical", ord_row_pair, CLASSICAL_TARGETS, 60, mpf("0.02"), 30),
        # Hahn–Exton at q̂x² ≈ 81 cancels ~1e20 internally: run with guard digits
        ("hahn_exton_Je_dq", he_row, D_Q_TARGETS, 10, mpf("0.01"), 60),
        ("hahn_exton_Je_pair_dq", he_row_pair, D_Q_TARGETS, 10, mpf("0.01"), 60),
    ):
        mp.dps = dps
        passed, nroots, best = gate_row(fn, tg, x_max=xmax, grid=grid)
        gates[name] = {"passed": passed, "n_roots": nroots, "best": best}
    set_compute_dps()
    out["bessel_row_gates"] = gates
    out["any_bessel_row_passed"] = any(g["passed"] for g in gates.values())
    return out


def report(res):
    print("# s013 — q-Bessel value-map gate: derived residue character, channels, row gates\n")
    print(f"q₀ = {res['q0']:.10f}   1/q₀ = {res['inv_q0']:.10f}   "
          f"q̂ = 1/q₀² = {res['qhat']:.10f}\n")

    print("## (A) Colored LR residue character — DERIVED exactly (sympy) + verified (50 dps)\n")
    print("| α | support (1..30) | signs on support | fold consistent (odd, 60-per.) "
          "| weights ±1? | identity residual |")
    print("|--:|---|---|:-:|:-:|--:|")
    for a, c in res["derived_characters"].items():
        sgns = ", ".join(f"{r}:{v:+d}" for r, v in c["signs_on_support"].items())
        print(f"| {a} | {{{', '.join(map(str, c['support_1_30']))}}} | {sgns} | "
              f"{c['fold_consistent_odd_periodic']} | {c['all_weights_pm1']} | "
              f"{c['identity_residual']:.1e} |")
    print(f"\n- α=1 support = bare validated {{1,11,19,29}}: "
          f"**{res['alpha1_reproduces_bare_support']}**")
    print(f"- α=1 ∪ α=2 = E₈ exponents: **{res['colored_union_is_E8']}**")
    print(f"- sign uniform on each support + same global sign across colours: "
          f"**{res['global_sign_uniform_across_colors']}** (a single global orientation/"
          f"framing sign; the prior probes' all-plus convention differs only by it)")
    print(f"- **Every residue weight is ±1 — the colored LR residue data is PURE SIGN, no "
          f"magnitude: {res['residue_weights_are_pure_signs']}.** The value map cannot live "
          f"in the residue weights.\n")

    print("## (B) Per-exponent channel amplitudes Ψ̃^{(e)}(1/q₀)\n")
    print("| e | Ψ̃^{(e)}(1/q₀) |")
    print("|--:|--:|")
    for e in E8_EXPONENTS:
        print(f"| {e} | {res['channels_at_inv_q0'][str(e)]:.8f} |")
    print(f"\n- bare-channel sum Σ_{{e∈{{1,11,19,29}}}} = {res['bare_channel_sum']:.6f} vs "
          f"bare Ψ(1/q₀) ≈ 2.3296: **match = {res['bare_sum_matches_bare_invariant']}** — "
          f"decomposition validated.\n")

    print("## (C) Channel value screen (targets d_q ratios 1, 4.110, 5.220, 6.220)\n")
    print("| e | class | target | channel ratio | pair-sum ratio | pair-diff ratio |")
    print("|--:|---|--:|--:|--:|--:|")
    for s in res["channel_value_screen"]:
        print(f"| {s['e']} | {s['class']} | {s['target_dq_ratio']:.4f} | "
              f"{s['channel_ratio']:.4f} | {s['pair_sum_ratio']:.4f} | "
              f"{s['pair_diff_ratio']:.4f} |")
    print(f"\n- channel REFUTED: {res['channel_refuted']}; pair-sum REFUTED: "
          f"{res['pair_sum_refuted']}; pair-diff REFUTED: {res['pair_diff_refuted']}")
    print("\n### Analytic q→1 gate (anchor-independent)\n")
    print("| ε | ratios (e=1,7,11,13) |")
    print("|--:|---|")
    for row in res["q1_gate"]["numeric"]:
        r = row["ratios"]
        print(f"| {row['eps']:.0e} | {r['1']:.4f}, {r['7']:.4f}, {r['11']:.4f}, "
              f"{r['13']:.4f} |")
    pred = res["q1_gate"]["L_value_prediction"]
    print(f"| L(0,χ_e)/L(0,χ_1) = (30−e)/29 | {pred['1']:.4f}, {pred['7']:.4f}, "
          f"{pred['11']:.4f}, {pred['13']:.4f} |")
    print(f"\n- numeric q→1 ratios match the L-value prediction: "
          f"**{res['q1_matches_L_values']}**")
    print(f"- channel ratios DECREASE in e while targets INCREASE (1→4→5→6): "
          f"**{res['q1_channel_ratios_decrease']}** — the channel amplitude is refuted at "
          f"EVERY anchor, not just q₀.\n")

    print("## (D) q-Bessel row gates (1 dof x, 2 net cross-checks; PASS = both < 1e−6)\n")
    print("| row | targets | roots of first ratio | passed | best root x | "
          "ratios @ best (11, 13) | targets (11, 13) | max rel err |")
    print("|---|---|--:|:-:|--:|---|---|--:|")
    for name, g in res["bessel_row_gates"].items():
        b = g["best"]
        tgt = "1,4,5,6" if "classical" in name else "d_q"
        if b:
            print(f"| {name} | {tgt} | {g['n_roots']} | {g['passed']} | {b['x']:.4f} | "
                  f"{b['ratio_11']:.4f}, {b['ratio_13']:.4f} | "
                  f"{b['target_11']:.4f}, {b['target_13']:.4f} | {b['max_rel_err']:.2e} |")
        else:
            print(f"| {name} | {tgt} | {g['n_roots']} | {g['passed']} | — | — | — | — |")
    print(f"\n- **any single-argument (q-)Bessel row passed: "
          f"{res['any_bessel_row_passed']}**\n")

    print("## Verdict (scope (a) — construction-limited, not structural exclusion)\n")
    print("- (A) The colored LR residue weights are ±1 signs (DERIVED, not quoted): the value")
    print("  map is not in the residue data.")
    print("- (C) The per-exponent channel amplitudes are governed by the L-values (30−e)/30 at")
    print("  q→1 and remain decreasing at q₀ — refuted as the value map at every anchor,")
    print("  ALONE, as-is.")
    print("- (D) See gate table for the single-argument (q-)Bessel vacuum-row family (with the")
    print("  E₈ dual-pair-representative order assignment) under the 1-dof overdetermined")
    print("  test.")
    print("- Remaining open value step: the genuine E_q(2) q-Hankel/Plancherel pairing (per-")
    print("  channel arguments, Koelink–Swarttouw kernel) — literature-gated; primary sources")
    print("  are firewalled in this sandbox (arXiv 403). No fit; nothing wired.")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("keystone-valuemap-qbessel-gate-s013", engine="mpmath+sympy")
    w.set_description(
        "s013 step 2 (q-Bessel gate). (A) DERIVES the colored Lawrence-Rozansky residue "
        "character of Sigma(2,3,5) exactly: 2sinh(z/2)2sinh(z/3)2sinh(alpha z/5)/2sinh(z) = "
        "num_alpha(x)*Sum_{k>=0} x^{60k} (x=e^{-z/30}), sympy-exact + 50dps verification, "
        "folded into an odd 60-periodic character with per-class consistency votes; alpha=1 "
        "reproduces the bare {1,11,19,29} support; ALL residue weights are +-1 (pure sign, no "
        "magnitude) -- the value map cannot live in the residue data. (B) Decomposes the "
        "colored family into the 8 per-exponent false-theta channels Psi~^(e)(1/q0); the "
        "alpha=1 channel sum reproduces the bare invariant 2.3296 (validation). (C) Screens "
        "channels/pair-sums/pair-diffs against the d_q targets and verifies the analytic "
        "q->1 gate: channel ratios -> L(0,chi_e) proportional to (30-e), DECREASING in e "
        "while d_q INCREASES -- the channel amplitude is refuted at every anchor. (D) Gates "
        "the single-argument (q-)Bessel vacuum row (ordinary J_e(x) vs classical dims "
        "1,4,5,6; Hahn-Exton J_e(x;1/q0^2) vs d_q; plus pair-symmetrized variants) with the "
        "1-dof overdetermined test (pin x on the first ratio, 2 net cross-checks at every "
        "root). Scope (a) prunes only; the genuine E_q(2) q-Hankel/Plancherel kernel remains "
        "the open step (primary literature firewalled: arXiv 403 in sandbox). No fit; "
        "nothing wired."
    )
    for key in ("q0", "inv_q0", "qhat", "derived_characters",
                "alpha1_reproduces_bare_support", "colored_union_is_E8",
                "residue_weights_are_pure_signs", "global_sign_uniform_across_colors",
                "channels_at_inv_q0", "bare_channel_sum",
                "bare_sum_matches_bare_invariant", "channel_value_screen",
                "channel_refuted", "pair_sum_refuted", "pair_diff_refuted",
                "q1_gate", "q1_matches_L_values", "q1_channel_ratios_decrease",
                "bessel_row_gates", "any_bessel_row_passed"):
        w.add_data(key, res[key])
    w.add_assertion(
        "colored_residue_character_derived_and_pure_sign",
        computed=1 if (res["alpha1_reproduces_bare_support"]
                       and res["residue_weights_are_pure_signs"]
                       and res["bare_sum_matches_bare_invariant"]) else 0,
        expected=1, tolerance=0,
        source="The colored LR residue character is derived exactly from the sinh-product "
               "rational identity (not quoted): alpha=1 reproduces the validated bare support, "
               "all weights are pure signs +-1 (fold-consistent odd 60-periodic), and the "
               "per-exponent channel decomposition reproduces the bare invariant at 1/q0. "
               "Hence the bwS0=d_q/D value map cannot be realized by the residue weights; "
               "combined with the channel L-value gate and the 1-dof (q-)Bessel row gate this "
               "locates the open value step in the genuine E_q(2) q-Hankel/Plancherel kernel "
               "(literature-gated).",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
