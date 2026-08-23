#!/usr/bin/env python3
"""alpha_em_b2_canonical_scale_ratio_probe.py — epic qou-k42c: attempt a
NORMALIZATION-INDEPENDENT restatement of the "25 = deg(5-isogeny)^2"
tau-scale observation (W7 of the merged CM/Weierstrass probe).

Under the standing 2026-07-19 owner ruling (R2 / the per-loop
identification is NOT derived-proved) and the attack-options scope
discipline: no tau-functor constructed, no TauRhoHodgeLift instance,
no fit, no tuning, nothing wired, 1/(8pi) stays phase-4. Conditional
language throughout. Route C's refutation (no convention-free single
scalar c; alpha-em-b2-invariant-c.witness.json) stands and is the
STARTING point, not the target.

THE QUESTION. The route-C canonical representative c_geo =
det(G_M G_H^{-1})^{1/4} = 0.9947074314... has c_geo*(8pi) =
24.9997244717, within 1.1e-5 (relative) of 25 = deg(5-isogeny)^2 —
but that value carries the entry-[0,0]=1 convention on BOTH Grams.
The premise to test: if the Markov side admits a canonical (intrinsic,
non-conventional) normalization AND the Hodge side admits one (Neron
periods), the ratio becomes convention-free and "= 25 exactly?" becomes
well-posed. This probe tests the premise itself, honestly.

WHAT THIS PROBE ESTABLISHES (K1-K7):

  K1  THE GAUGE GROUP HAS THREE SCALES, NOT TWO. The Schur scalar in
      tau(G_Markov) = c * G_Hodge transforms under
        G_M -> lam*G_M,  G_H -> mu*G_H,  P -> s*P   (P = the Schur
      intertwiner, unique up to scalar; Lean-proved covariance
      `invariantForm_pullback_smul`, InvariantFormTransport.lean:
      P |-> s*P rescales the pulled-back Gram by s^2) as
        c -> (lam / (mu * s^2)) * c.
      Machine-verified by direct transform (extends route C's I1,
      which fixed P = id implicitly). CONSEQUENCE: canonically pinning
      BOTH Grams still leaves the intertwiner gauge s^2 — a fully
      normalization-free magnitude is impossible even with two
      canonical pins. The bean-premise's "both sides canonical =>
      convention-free" is FALSE as stated; the third scale is exactly
      the tau-scale gate restated.

  K2  THE SURVIVING INVARIANT RESTATEMENT (the maximum extractable,
      conditional). The merged Weierstrass probe (W6) narrowed the
      residual freedom under Neron normalization to a DISCRETE set:
      isogeny-degree pullbacks, natural support powers of 5 (X0(5) /
      conductor-50 structure). IF all three residual gauges are
      5-power-graded (hypothesis H5 — motivated Hodge/intertwiner-side
      by W6, UNVERIFIED Markov-side), then
        theta_5 := frac( log_5( c * 8pi ) )
      is gauge-invariant, and the normalization-independent restatement
      of "25 = deg^2" is:  theta_5 = 0  (with k = log_5(c*8pi) = 2 the
      selected pullback degree in the route-C gauge). theta_5 computed
      at 50 dps from a fresh route-C-convention recompute.

  K3  MARKOV-SIDE CANONICAL PINS — COMPUTED, AND THE PREMISE'S FIRST
      LEG BREAKS. The corpus has (at least) two intrinsic Hecke-side
      trace normalizations, both canonical, both computed at q0:
        (a) the Jones-Markov weight y_(4,1)(q0)  (canonical producer
            wedderburn_jones_markov.y_lambda_at, witness-pinned);
        (b) the Wedderburn weight w_(4,1)(q0) = d_q(4,1)^2/[5]_q!
            (the scalar_c probe's `_wedderburn_weight` normalization);
        the tr(1)=1 certificate for the canonical Markov trace is
        sum_lam y_lam * f^lam = 1 (certified at 50 dps);
        (c) the cellular/Murphy anchor candidate gamma_{T^lam} =
            [4]_{q^2}! relative to the corpus-STRICT presentation
            (sigma-q)(sigma+q^{-1})=0 via the dictionary T = q*sigma
            ((T-q^2)(T+1)=0 machine-checked exactly) — the one
            candidate that lives at MODULE level; its two unverified
            convention legs are NAMED (tableau-0 = row-reading T^lam;
            Hoefsmit-natural = Murphy-unitriangular seminormal).
      Findings: (F1) the candidates are MUTUALLY INEQUIVALENT modulo
      5-powers (pairwise frac(log_5) differences far from 0) — there
      is no unique canonical Markov 5-class, so H5's Markov leg fails
      for the declared intrinsic pins; (F2) STRUCTURAL: the trace
      pins (a),(b) provably transmit NO scale to the module Gram at
      all — every Markov-trace observable lives on End(V), where the
      module-form scale cancels (G-adjoint is invariant under
      G -> lam*G; tr_M never references G). A canonical ALGEBRA
      scalar is not a canonical MODULE form. Machine row: the
      contravariant solve returns a LINE (nullity 1); no trace datum
      selects a point on it.

  K4  THE 25 DOES NOT SURVIVE THE DECLARED PINS (outcome-(ii) rows,
      per pin, no selection). For each declared pin p, replacing the
      entry-[0,0]=1 Markov convention by p multiplies c by
      lam_p = p / m_00-convention-factor and moves theta_5 by
      frac(log_5 lam_p) != 0. Reported per pin as-is: under (a), (b),
      or (c) the ratio is NOT 25 * 5^Z unless the Hodge-side canonical
      anchor supplies the SAME non-5-power factor. No pin is selected;
      selecting the pin that preserves 25 would be tuning.

  K5  THE EXACT MATCHING CONDITION (what a future tau-derivation must
      satisfy for "25" to be canonical). "25 survives" <=>
        lam_M / (mu_H * s^2)  in  5^Z
      i.e. the canonical Markov anchor and the canonical
      Hodge-times-gauge anchor agree modulo 5-powers. With the
      computed Markov candidates this becomes a sharp, falsifiable
      target for the Hodge side: frac(log_5(mu_H * s^2)) must equal
      frac(log_5 lam_M) — value reported per candidate.

  K6  HODGE-SIDE CANONICAL PIN — BLOCKED, precisely named (no
      fabrication). The curve-integration Hodge form
      h(w,e) = (i/2) int_Bring w wedge conj(e) is genuinely canonical
      (the ONE convention-free scale in the problem), but evaluating
      its scalar against the transported Markov form needs (i) the
      integral-symplectic <-> isogeny-frame dictionary — the
      Riera-Rodriguez period matrix Z, ABSENT from the corpus (named
      open in the attack-options doc); (ii) the per-factor Neron
      period magnitudes |Omega_i|^2 of the four 50a elliptic factors —
      non-CM (CM refuted, W1 of the merged probe), so no
      Chowla-Selberg closed form; the 50a minimal models are also not
      corpus data (only the two j-invariants are). The isogeny-adapted
      frame is not S5-equivariant (c-pin probe V5), so per-factor
      Neron pins cannot be transported to the invariant scalar without
      Z. The task-anticipated obstruction "3 x E_{5tau0} vs 1 x
      E_{tau0} breaking a uniform scale" manifests exactly here: the
      per-factor pullback multiplicities live in the non-equivariant
      frame.

  K7  VERDICT — OUTCOME (iii), scope-(a). The single-ratio question
      "does c*(8pi) = 25 exactly?" CANNOT be made fully
      normalization-free: (O1) the Markov side has no unique intrinsic
      module-scale (trace pins don't transmit; the declared intrinsic
      candidates are mutually inequivalent mod 5^Z); (O2) two pins
      cannot fix the three-scale gauge (Lean-proved s^2 covariance);
      (O3) the Hodge canonical evaluation is gated on the absent Z +
      non-CM periods. What SURVIVES is the conditional restatement
      theta_5 = 0 under H5 (K2) plus the exact matching condition
      (K5). The deg^2 = 25 observation stays an OPEN, owner-level,
      double-gated observation — now with the precise condition a
      legitimate tau-identification must satisfy for it to become a
      derived integer. Scope-(a): this refutes the specific declared
      pin-menu as a route to normalization-freedom, alone, as stated;
      it does NOT structurally exclude a future canonical pin (e.g. a
      verified cellular-Murphy module pin plus the Riera-Rodriguez
      frame) from closing the loop.

Scope guard: no fit; nothing wired; the tau-identification remains the
sole open categorical input; 1/(8pi) stays phase-4. mpmath 50 dps
(+10 guard); exact Fraction arithmetic for the presentation dictionary.

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
-- Ref: [mathas-1999] Iwahori-Hecke algebras and Schur algebras of the
--       symmetric group (cellular/Murphy basis, gamma_{T^lam} = [lam]_Q!)
-- Ref: [orellana1998] https://doi.org/10.1006/jabr.1998.7437
-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-- Ref: [riera-rodriguez-1992] The period matrix of Bring's curve,
--       Pacific J. Math. 154 (1992)
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
sys.path.insert(0, str(_COMP))
import _path_bridge as _bridge  # noqa: E402, F401

from derived_chi_catalogue_matrix_m_mpfr import (  # noqa: E402
    seminormal_matrices_mpfr)
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

try:
    from qou_substrate.constants import q_at
except Exception:
    q_at = None

mp.mp.dps = 60  # 50 target + 10 guard
SHAPE = (4, 1)
N = 5


def q0_val():
    if q_at is not None:
        return q_at(50)
    return mp.mpf("1.10997859555733471989976322048322502665620840878")


# ---------------------------------------------------------------- helpers
def q_int(k: int, q):
    """Balanced q-integer [k]_q = (q^k - q^{-k})/(q - q^{-1})."""
    return (q ** k - q ** (-k)) / (q - 1 / q)


def q_factorial(n: int, q):
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k, q)
    return out


def one_sided_q_int(k: int, Q):
    """One-sided q-integer [k]_Q = 1 + Q + ... + Q^{k-1} (Mathas)."""
    return sum(Q ** j for j in range(k))


def hook_lengths(shape):
    lam = list(shape)
    width = lam[0]
    conj = [sum(1 for p in lam if p > j) for j in range(width)]
    hooks = []
    for i, li in enumerate(lam):
        for j in range(li):
            hooks.append((li - j - 1) + (conj[j] - i - 1) + 1)
    return hooks


def q_dimension(shape, q):
    num = q_factorial(sum(shape), q)
    den = mp.mpf(1)
    for h in hook_lengths(shape):
        den *= q_int(h, q)
    return num / den


def contravariant_diag(q, dim):
    """Diagonal of the contravariant seminormal form (sigma_k^T G =
    G sigma_k), normalized to entry [0,0]=1 (the route-C CONVENTION —
    reproduced here deliberately so the canonical pins can be compared
    against it). Same solve as route C."""
    rho = seminormal_matrices_mpfr(SHAPE, q)
    d2 = dim * dim
    normal = mp.zeros(d2, d2)
    for sig in rho:
        Phi = mp.zeros(d2, d2)
        for a in range(dim):
            for b in range(dim):
                row = a * dim + b
                for r in range(dim):
                    for s in range(dim):
                        col = r * dim + s
                        val = mp.mpf(0)
                        if s == b:
                            val += sig[r, a]
                        if a == r:
                            val -= sig[s, b]
                        if val != 0:
                            Phi[row, col] += val
        normal += Phi.T * Phi
    evals, evecs = mp.eigsy(normal)
    i0 = min(range(d2), key=lambda i: abs(evals[i]))
    g = mp.matrix(dim, dim)
    for a in range(dim):
        for b in range(dim):
            g[a, b] = evecs[a * dim + b, i0]
    g = (g + g.T) / 2
    g = g / g[0, 0]
    return [g[i, i] for i in range(dim)]


def frac_log5(x):
    """Fractional part of log_5|x|, folded to (-1/2, 1/2] (distance to
    the nearest 5-power grading)."""
    t = mp.log(abs(x)) / mp.log(5)
    f = t - mp.floor(t)
    if f > mp.mpf(1) / 2:
        f -= 1
    return t, f


def main() -> int:
    print("=" * 78)
    print(" B2 tau-scale: normalization-independent restatement of "
          "25 = deg(5-isogeny)^2?")
    print("=" * 78)

    assertions = []

    def check(name, passed, detail="", computed=None, expected=None,
              tolerance=None):
        entry = {"name": name, "passed": bool(passed), "detail": detail}
        if computed is not None:
            entry["computed"] = computed
        if expected is not None:
            entry["expected"] = expected
        if tolerance is not None:
            entry["tolerance"] = tolerance
        assertions.append(entry)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    q0 = q0_val()
    rho = seminormal_matrices_mpfr(SHAPE, q0)
    dim = rho[0].rows
    print(f"\nq0 = {mp.nstr(q0, 20)}; shape {SHAPE}, dim {dim}")

    # ---- baseline: fresh route-C-convention recompute at 50 dps -----------
    mM = contravariant_diag(q0, dim)
    wH = contravariant_diag(mp.mpf(1) + mp.mpf("1e-30"), dim)
    ratios = [mM[i] / wH[i] for i in range(dim)]
    c_geo = mp.e ** (mp.fsum([mp.log(r) for r in ratios]) / dim)
    inv8pi = 1 / (8 * mp.pi)
    R_conv = c_geo / inv8pi          # = c_geo * 8pi
    print(f"[baseline] c_geo = {mp.nstr(c_geo, 20)}; "
          f"c_geo*8pi = {mp.nstr(R_conv, 15)} (route-C convention)")

    # ---- K1: the gauge group has THREE scales ------------------------------
    # c^4 = det(G_M) / det(P^T G_H P); transform check with random-fixed
    # lam, mu, s (declared constants, not tuned).
    lam, mu, s = mp.mpf("2.5"), mp.mpf("0.4"), mp.mpf("1.7")
    GM = mp.matrix(dim, dim)
    GH = mp.matrix(dim, dim)
    for i in range(dim):
        GM[i, i] = mM[i]
        GH[i, i] = wH[i]
    P = mp.eye(dim)                   # route-C implicit intertwiner rep

    def c4(GMx, GHx, Px):
        Wt = Px.T * GHx * Px
        return mp.det(GMx) / mp.det(Wt)

    c4_0 = c4(GM, GH, P)
    c4_t = c4(lam * GM, mu * GH, s * P)
    expected_factor = (lam / (mu * s ** 2)) ** dim
    k1_ok = abs(c4_t / c4_0 - expected_factor) < mp.mpf("1e-40")
    check(
        "K1_three_scale_gauge_group", k1_ok,
        f"c^4 transforms by (lam/(mu*s^2))^4 under (G_M,G_H,P) -> "
        f"(lam G_M, mu G_H, s P): measured factor deviation "
        f"{mp.nstr(abs(c4_t / c4_0 - expected_factor), 3)}. Two canonical "
        f"Gram pins still leave the intertwiner gauge s^2 (Lean: "
        f"invariantForm_pullback_smul) — full normalization-freedom of the "
        f"magnitude is impossible with two pins; the third scale IS the "
        f"tau-scale gate",
        computed=float(abs(c4_t / c4_0 - expected_factor)), expected=0.0,
        tolerance=1e-40)

    # ---- K2: theta_5 — the conditional invariant restatement ---------------
    log5R, theta5 = frac_log5(R_conv)
    k_sel = int(mp.nint(log5R))
    k2_ok = abs(theta5) < mp.mpf("5e-5") and k_sel == 2
    check(
        "K2_theta5_conditional_restatement", k2_ok,
        f"log_5(c*8pi) = {mp.nstr(log5R, 15)}; theta_5 = frac = "
        f"{mp.nstr(theta5, 6)} (distance to integer grading), selected "
        f"k = {k_sel}. UNDER hypothesis H5 (all residual gauges "
        f"5-power-graded; Hodge/intertwiner leg motivated by W6's discrete "
        f"narrowing, Markov leg UNVERIFIED) theta_5 is gauge-invariant and "
        f"'25 = deg^2' restates normalization-independently as theta_5 = 0. "
        f"CONDITIONAL, not derived; H5's Markov leg is tested next",
        computed=float(theta5), expected=0.0, tolerance=5e-5)

    # ---- K3: Markov-side canonical pins ------------------------------------
    # (a) Jones-Markov y_(4,1)(q0) — corpus-canonical producer.
    y_all = y_lambda_at(N, q0)
    y41 = mp.mpf(str(y_all[SHAPE]))
    # (b) Wedderburn/Plancherel w_lam = d_q^2/[n]_q!, tr(1)=1 certified.
    from itertools import combinations

    def partitions(n):
        if n == 0:
            yield ()
            return
        for first in range(n, 0, -1):
            for rest in partitions(n - first):
                if not rest or rest[0] <= first:
                    yield (first,) + rest

    from math import factorial as _fact

    def f_lam(shp):
        prod = 1
        for h in hook_lengths(shp):
            prod *= h
        return _fact(sum(shp)) // prod

    w = {}
    tr1 = mp.mpf(0)
    for shp in partitions(N):
        w[shp] = q_dimension(shp, q0) ** 2 / q_factorial(N, q0)
        tr1 += mp.mpf(str(y_all[shp])) * f_lam(shp)
    w41 = w[SHAPE]
    # tr(1)=1 for the canonical Markov trace: sum_lam y_lam * f^lam = 1.
    # (NOT sum_lam w_lam — that equals 1 only at q=1; the Wedderburn
    # weight w_lam is a distinct corpus normalization, reported as-is.)
    tr1_ok = abs(tr1 - 1) < mp.mpf("1e-40")
    # (c) cellular/Murphy anchor: corpus presentation -> Mathas via T = q*sigma.
    #     Dictionary check EXACT (Fraction): T^2 = (q^2-1)T + q^2 given
    #     sigma^2 = (q - q^{-1}) sigma + 1.
    #     Symbolically: T^2 = q^2 sigma^2 = q^2((q-1/q)sigma + 1)
    #                       = (q^2-1)(q sigma) + q^2 = (q^2-1)T + q^2.  QED
    #     Machine-check at an exact rational q:
    qr = Fraction(111, 100)
    lhs_coeff_sigma = qr * qr * (qr - 1 / qr)        # coefficient of sigma
    rhs_coeff_sigma = (qr * qr - 1) * qr             # (q^2-1)*q
    dict_ok = (lhs_coeff_sigma == rhs_coeff_sigma)
    Qsq = q0 ** 2
    gamma_anchor = mp.mpf(1)
    for k in range(1, 5):
        gamma_anchor *= one_sided_q_int(k, Qsq)      # [4]_{q^2}!
    k3_ok = tr1_ok and dict_ok
    check(
        "K3_markov_canonical_pins_computed", k3_ok,
        f"(a) y_(4,1)(q0) = {mp.nstr(y41, 20)} (Jones-Markov, corpus "
        f"producer) with tr(1)=1 certified: sum_lam y_lam*f^lam = 1 to "
        f"{mp.nstr(abs(tr1 - 1), 3)}; (b) w_(4,1)(q0) = d_q^2/[5]_q! = "
        f"{mp.nstr(w41, 20)} (corpus _wedderburn_weight normalization, "
        f"distinct from (a) — reported as-is); (c) cellular anchor "
        f"candidate gamma_(T^lam) = "
        f"[4]_(q^2)! = {mp.nstr(gamma_anchor, 20)} relative to the "
        f"corpus-STRICT presentation, dictionary T = q*sigma exact "
        f"({dict_ok}); its two unverified convention legs NAMED "
        f"(tableau-0 = T^lam; Hoefsmit-natural = Murphy-unitriangular)",
        computed=[float(y41), float(w41), float(gamma_anchor)],
        expected="three declared intrinsic candidates", tolerance=None)

    # F1: mutual 5-class inequivalence
    _, f_y = frac_log5(y41)
    _, f_w = frac_log5(w41)
    _, f_g = frac_log5(gamma_anchor)
    pair_dev = [abs(f_y - f_w), abs(f_y - f_g), abs(f_w - f_g)]
    # fold pairwise differences to distance-from-integer
    pair_dev = [min(d, abs(1 - d)) for d in pair_dev]
    f1_ok = min(pair_dev) > mp.mpf("1e-3")
    check(
        "K3_F1_no_unique_markov_5class", f1_ok,
        f"frac(log_5) of the pins: y = {mp.nstr(f_y, 8)}, w = "
        f"{mp.nstr(f_w, 8)}, gamma = {mp.nstr(f_g, 8)} — pairwise "
        f"5-class differences {[mp.nstr(d, 5) for d in pair_dev]} all "
        f"> 1e-3: the intrinsic Markov candidates are MUTUALLY "
        f"INEQUIVALENT mod 5^Z; there is no unique canonical Markov "
        f"5-class, so H5's Markov leg FAILS for the declared pin menu",
        computed=[float(d) for d in pair_dev], expected="all > 1e-3",
        tolerance=1e-3)

    # F2: structural — trace pins transmit no module scale.
    # Machine content: (i) the contravariant solve returns a LINE
    # (nullity 1 — Schur), so any point on it is a convention; (ii) the
    # G-adjoint that defines every Markov-trace observable is invariant
    # under G -> lam*G (verified on a sample word).
    Ginv = GM ** -1
    X = rho[0] * rho[1]                      # sample block element
    adj1 = Ginv * X.T * GM
    lam2 = mp.mpf("3.7")
    adj2 = (lam2 * GM) ** -1 * X.T * (lam2 * GM)
    adj_dev = max(abs(adj1[i, j] - adj2[i, j])
                  for i in range(dim) for j in range(dim))
    f2_ok = adj_dev < mp.mpf("1e-45")
    check(
        "K3_F2_trace_pins_module_scale_blind", f2_ok,
        f"G-adjoint invariant under G -> lam*G to {mp.nstr(adj_dev, 3)}: "
        f"every Markov-trace observable lives on End(V) where the module-"
        f"form scale cancels — the canonical trace normalizations (a),(b) "
        f"are ALGEBRA scalars and transmit NO canonical scale to the module "
        f"Gram entering c. A trace pin is not a module pin (structural)",
        computed=float(adj_dev), expected=0.0, tolerance=1e-45)

    # ---- K4: does the 25 survive the declared pins? (per-pin rows) ---------
    # Replacing entry-[0,0]=1 by pin p rescales G_M by lam_p = p (the
    # convention had m_00 = 1, so the multiplicative move is p itself,
    # up to the pin's own placement rule — reported as the pure 5-class
    # shift, which is placement-rule-independent for rules of the form
    # G_M = p * (unit-[0,0] form)).
    rows = {}
    for nm, p in (("y_lambda", y41), ("w_wedderburn", w41),
                  ("gamma_cellular", gamma_anchor)):
        Rp = R_conv * p                     # c*8pi under the rescaled pin
        l5, f5 = frac_log5(Rp)
        rows[nm] = {"pin_value": mp.nstr(p, 25),
                    "c_8pi_under_pin": mp.nstr(Rp, 20),
                    "log5": mp.nstr(l5, 15),
                    "frac_log5_folded": mp.nstr(f5, 10)}
        print(f"    [K4] pin {nm}: c*8pi -> {mp.nstr(Rp, 12)}, "
              f"log_5 = {mp.nstr(l5, 10)}, dist to 5^Z grading = "
              f"{mp.nstr(abs(f5), 6)}")
    k4_survives = any(abs(mp.mpf(rows[nm]["frac_log5_folded"]))
                      < mp.mpf("5e-5") for nm in rows)
    check(
        "K4_25_does_not_survive_declared_pins", not k4_survives,
        f"under each declared intrinsic pin the ratio moves OFF the "
        f"5-power grading (all |frac(log_5)| >> 1e-4): the 24.9997 ~ 25 "
        f"match does NOT survive any declared canonical Markov pin alone. "
        f"Scope-(a): refutes these pins as-stated as the route to a "
        f"normalization-free 25; does not exclude a future verified "
        f"module-level pin + Hodge anchor combination",
        computed={nm: rows[nm]["frac_log5_folded"] for nm in rows},
        expected="all far from 0", tolerance=5e-5)

    # ---- K5: the exact matching condition ----------------------------------
    match_targets = {nm: rows[nm]["frac_log5_folded"] for nm in rows}
    check(
        "K5_matching_condition_stated", True,
        f"'25 survives canonically' <=> lam_M/(mu_H*s^2) in 5^Z <=> "
        f"frac(log_5(mu_H*s^2)) equals frac(log_5 lam_M) per pin: "
        f"targets {match_targets}. This is the sharp, falsifiable "
        f"condition a legitimate tau-identification must satisfy for the "
        f"deg^2 = 25 observation to become a derived integer. Stated, "
        f"not adjudicated (owner-level)",
        computed=match_targets, expected="condition recorded")

    # ---- K6: Hodge-side canonical pin — blocked, named ----------------------
    check(
        "K6_hodge_canonical_pin_blocked_named", True,
        "the curve-integration Hodge form is the one genuinely "
        "convention-free scale, but its scalar against the transported "
        "Markov form needs (i) the Riera-Rodriguez integral-symplectic "
        "period matrix Z (ABSENT from corpus — named open in the "
        "attack-options doc), and (ii) the Neron period magnitudes "
        "|Omega_i|^2 of the four 50a factors — non-CM (CM refuted, W1), "
        "no closed form; 50a minimal models not corpus data (only the two "
        "j-invariants). The isogeny frame is not S5-equivariant (c-pin V5), "
        "so per-factor Neron pins do not transport to the invariant scalar "
        "without Z — the anticipated '3 x E_5tau0 vs 1 x E_tau0' "
        "obstruction manifests exactly here. BLOCKED, not fabricated",
        computed="blocked", expected="named obstruction")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "OUTCOME (iii) — the normalization-independent restatement CANNOT "
        "be completed as posed, for precisely-named reasons; a weaker "
        "conditional restatement survives. (1) The gauge group has THREE "
        "scales (Markov, Hodge, intertwiner s^2 — Lean-proved covariance); "
        "two canonical pins cannot fix it (K1). (2) Under hypothesis H5 "
        "(all residual gauges 5-power-graded) the invariant content of "
        "'25 = deg(5-isogeny)^2' is theta_5 := frac(log_5(c*8pi)) = 0, "
        "measured -6.9e-6 in the route-C gauge with k = 2 selected (K2) — "
        "the maximum extractable normalization-independent statement, "
        "CONDITIONAL on H5. (3) H5's Markov leg FAILS for the declared "
        "intrinsic pin menu: the corpus-canonical trace normalizations "
        "y_(4,1)(q0) = 0.1094, w_(4,1)(q0) = d_q^2/[5]_q! = 0.1286, and "
        "the cellular anchor [4]_(q^2)! = 47.05 are mutually inequivalent "
        "mod 5^Z (no unique canonical Markov 5-class), and the trace pins "
        "structurally transmit NO module scale (End(V) blindness) (K3). "
        "(4) Under each declared pin the 24.9997 ~ 25 match moves off the "
        "5-grading — the 25 was a property of the entry-[0,0]=1 "
        "convention, not (yet) of any canonical normalization (K4). "
        "(5) The exact matching condition for a future closure is stated: "
        "frac(log_5(mu_H*s^2)) must equal frac(log_5 lam_M) (K5); the "
        "Hodge-side canonical evaluation is gated on the absent "
        "Riera-Rodriguez Z + non-CM Neron periods (K6). The deg^2 = 25 "
        "observation REMAINS open, owner-level, double-gated; scope-(a) "
        "throughout — the declared pins are refuted as-stated as the "
        "normalization-freedom route, no ingredient is structurally "
        "excluded. Nothing wired; 1/(8pi) stays phase-4."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                      cwd=str(_HERE), text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "alpha-em-b2-canonical-scale-ratio",
        "description": "Normalization-independent restatement attempt for "
                       "the B2 tau-scale '25 = deg(5-isogeny)^2' "
                       "observation. OUTCOME (iii): the gauge group has "
                       "three scales (Markov, Hodge, intertwiner s^2), so "
                       "two canonical pins cannot make the ratio "
                       "convention-free; the surviving conditional "
                       "restatement is theta_5 = frac(log_5(c*8pi)) = 0 "
                       "under the 5-power-grading hypothesis H5, whose "
                       "Markov leg fails for the declared intrinsic pins "
                       "(y_lambda, Wedderburn w_lambda, cellular anchor — "
                       "mutually inequivalent mod 5^Z; trace pins are "
                       "module-scale-blind). Exact matching condition for "
                       "a future tau-derivation stated. Hodge canonical "
                       "pin blocked on absent Riera-Rodriguez Z + non-CM "
                       "periods. Observation stays open/double-gated; "
                       "nothing wired; 1/(8pi) phase-4.",
        "auditOnly": "docs/audits/2026-07-25-alpha-em-b2-canonical-scale-"
                     "ratio.md",
        "tier": "numerical-certified structure rows (50 dps); the theta_5 "
                "restatement is CONDITIONAL (hypothesis H5); K4 rows are "
                "scope-(a) per-pin negatives",
        "computedAt": now, "commitSha": _sha(),
        "engine": "mpmath", "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "precisionMetadata": {"compute_dps": 60, "target_dps": 50,
                              "guard_digits": 10},
        "q0_pin_note": "Grams/w/gamma computed at the package proton-"
                       "pinned q_at(50); y_(4,1) served from the muon-q0 "
                       "witness cache (y-lambda-at-q0.witness.json) by "
                       "y_lambda_at's q0 fast path — cross-pin "
                       "discrepancy ~1e-8 relative, orders below every "
                       "decision threshold here (5-class distances are "
                       "O(0.1); theta_5 is route-C-internal). Recorded "
                       "per the bean-tnjb pin-conflation discipline.",
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "c_geo_routeC_convention": mp.nstr(c_geo, 25),
            "c_8pi_routeC_convention": mp.nstr(R_conv, 20),
            "theta_5": mp.nstr(theta5, 10),
            "k_selected_routeC_gauge": k_sel,
            "markov_pins": {
                "y_lambda_41_q0": mp.nstr(y41, 25),
                "w_wedderburn_41_q0": mp.nstr(w41, 25),
                "gamma_cellular_anchor_q0": mp.nstr(gamma_anchor, 25),
                "frac_log5": {"y": mp.nstr(f_y, 12),
                              "w": mp.nstr(f_w, 12),
                              "gamma": mp.nstr(f_g, 12)}},
            "per_pin_rows": rows,
            "matching_condition": "frac(log5(mu_H*s^2)) == frac(log5 "
                                  "lam_M) per pin (K5 targets above)",
            "hodge_pin_status": "BLOCKED — Riera-Rodriguez Z absent; "
                                "non-CM Neron periods (no closed form); "
                                "isogeny frame not S5-equivariant",
            "verdict": verdict,
        },
        "context": {
            "epic": "qou-k42c",
            "inputs_read_only": [
                "computations/alpha-em-b2-invariant-c.witness.json",
                "computations/alpha_em/alpha-em-b2-cm-weierstrass-scale"
                ".witness.json",
                "computations/y-lambda-at-q0.witness.json"],
            "lean_covariance": "QOU/Archimedean/InvariantFormTransport"
                               ".lean::invariantForm_pullback_smul",
            "ruling": "2026-07-19: the per-loop identification is not "
                      "derived-proved — respected; nothing asserted",
            "scope_guard": "no fit; no TauRhoHodgeLift instance; nothing "
                           "wired; 1/(8pi) phase-4; conditional language "
                           "throughout",
        },
    }
    out = os.path.join(str(_HERE),
                       "alpha-em-b2-canonical-scale-ratio.witness.json")
    with open(out, "w") as f:
        # Provenance envelope. This producer writes its witness as raw JSON, so
        # nothing stamps `scriptHash` — and a witness without one cannot be
        # compared against its producer, so it drops OUT of the self-staleness
        # audit and reads as "not stale" forever. Regenerating it then looks
        # like progress while removing it from the count: a false drain.
        # Full rationale and the detector: computations/witness_drain_audit.py.
        #
        # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
        # fields in place and leaves the on-disk shape untouched, so consumers
        # of legacy `assertions` records (which key on `label`, not `name`) do
        # not have to change. `engine` is passed back from the payload because
        # the helper overwrites it, and a descriptive engine string is worth
        # keeping.
        try:
            from witness_base import WitnessBuilder  # noqa: E402
        except ImportError:  # cluster subdir without the _path_bridge bootstrap
            import sys as _sys
            from pathlib import Path as _Path
            _sys.path.insert(0, str(next(
                _a / "substrate" for _a in _Path(__file__).resolve().parents
                if (_a / "substrate" / "witness_base.py").is_file())))
            from witness_base import WitnessBuilder  # noqa: E402
        WitnessBuilder.stamp_staleness_metadata(
            witness, script_path=__file__,
            engine=witness.get("engine", 'python+mpmath'))
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
