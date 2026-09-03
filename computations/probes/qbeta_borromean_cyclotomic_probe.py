#!/usr/bin/env python3
"""qbeta_borromean_cyclotomic_probe.py — PROBE 3: the Borromean forced
candidate C14 missed (2026-07-11 avenues audit §3.C).

QUESTION.  C14 (qbeta_root_of_unity_probe.py) tested the two forced
knots — 4₁ and the Hopf link — and refuted the forced-knot
root-of-unity/Ohtsuki class.  It never tested the BORROMEAN RINGS,
the framework's own nucleon braid β_Bor = (σ₁σ₂⁻¹)³ (canonical_mass
F_Bor), hence a zero-free-choice forced candidate under C14's own
discipline.  Does the q=1 Taylor SHADOW of the framework-normalised
Borromean invariant reproduce the ladder shadows

    c_2 = −1  (Lean-proved, Taylor-exact)          [registry KC10]
    c_3 → −2  (the c_3 q=1 shadow = J_Hopf(1))     [registry KC10]

parameter-free?

ANTI-FITTING DISCIPLINE (C14 row, 2026-06-04 refuted-class map): ZERO
free choices.  We do NOT scan links, roots, or normalisations.  The
braid is forced (β_Bor is the production nucleon braid); the
normalisations are ONLY those already canonical in the corpus:

    N1  τ_D(q)      — Lean-proved Borromean Markov-trace closed form
                      (BorromeanMarkovTrace.lean; the factor inside
                      canonical_mass.py F_Bor), τ_D(1) = 1.
    N2  τ_C(q)      — the corpus-canonical Jones–Markov z-trace of
                      β_Bor (markov_trace_recursive, convention C =
                      Wenzl bridge; D ≠ C is a DOCUMENTED corpus split,
                      2026-06-09 audit + PR #3261 probe), τ_C(1) = 1.
    N3  F_Bor(q)/6  — the canonical-mass dimensionless Hecke factor
                      F_Bor = |tr_M(β_Bor)|·[3]_q!/q³, divided by its
                      classical limit F_Bor(1) = 6 (division by the
                      q=1 value is forced: a shadow series must start
                      at 1; 6 = 3! is the Poincaré classical limit).
    N4  J_B(t)/4    — the literature Jones polynomial of the Borromean
                      rings (GL2011/Habiro transcription, corpus file
                      habiro_borromean_colored_jones.py, n=2), divided
                      by its classical limit J_B(1) = (−2)² = 4.

Expansion variable: the corpus-canonical shadow variable ℏ = ℏ_q =
(q−1)/q, i.e. q = 1/(1−ℏ) — exactly the C13 bridge convention
(habiro_mode_to_ladder_bridge.py: u = √q = (1−ℏ)^{−1/2}).

TWO-WAY CROSS-CHECK (gate, pre-stated: on failure STOP, exit 2):
  (a) framework Hecke machinery: τ_D (Lean closed form, F_Bor route)
      and τ_C (canonical recursive Markov trace of the signed word
      (1,−2,1,−2,1,−2) in H_3(q));
  (b) literature: the Habiro/GL2011 colored-Jones closed form at n=2
      (already TL₃-cross-checked in-corpus) AND the independent
      external closed form V_{L6a4}(t) = −t⁻³+3t⁻²−2t⁻¹+4−2t+3t²−t³
      (Knot Atlas / LinkInfo L6a4), hardcoded here.
  Exact identities demanded (sympy cancel over ℚ(s), decidable):
      G1:  J_{B,2}(s) == V_{L6a4}(t = s²)          (transcription = lit.)
      G2:  J_{B,2}(s) == [2]² · τ_D  with framework q = s,
           [2] = q + q⁻¹                            (framework = lit.)
  KNOWN split (recorded, NOT a stop): τ_C ≠ τ_D exactly (corpus audit
  2026-06-09; gap ≈ 1.955e-4 at q₀).  τ_D is the convention that (i)
  the production F_Bor uses and (ii) exactly matches the literature
  Jones (G2), so the split is a documented convention fork, not a
  transcription error.

KILL CRITERION (pre-stated): if no canonical normalisation reproduces
c_2 = −1 AND the c_3 shadow −2 parameter-free — in the raw shadow
coefficients (primary gate: a_2 = −1 ∧ a_3 = −2) or through the
already-canonical C13 bridge peel (secondary: even-in-ℏ, G_k =
a_{2k}/b^k, single scale d.o.f. fixed by c_2 = −1, read c_3) — the
verdict is NEGATIVE and this class becomes a new refuted row (C15
candidate: "forced-link Borromean cyclotomic/q=1 shadow"),
scope-limited (a) per AGENTS.md §Before declaring refuted: the
Borromean shadow, ALONE under the corpus's canonical normalisations,
does not reproduce the ladder shadows.  No ingredient exclusion is
asserted.  If any coefficient DOES match parameter-free: report
GATE-PASSED near-match with exact residuals at both anchors — NOT a
derivation, NO wiring proposed.

Anchors (both, per AGENTS.md §q₀ anchor convention):
    proton q₀ — qou_substrate.constants.Q_50_DIGIT_STR (m_p/m_e pin)
    muon   q₀ — 1.1099785955573347198997632204832250266562084087802
                (computations/ canonical q-pinning-50-digit value)
Only b(q₀) and the empirical-c₃ residuals are q₀-dependent; the shadow
coefficients themselves are exact rationals (anchor-independent by
construction — the non-C1-refuted path, as in the C13 bridge).

Empirical c₃ reference values (provenance, all recorded in witness):
    proton-quoted −2.06934257711516783787971951725   (C14 probe target;
                                                      registry §3)
    muon-quoted   −2.0097                             (C13 bridge PR
                                                      #2465; registry
                                                      −2.88% swing)
    cache         −2.02018812814143945582016855395    (qbeta-ck-cache
                                                      at the
                                                      computations/
                                                      canonical q₀ —
                                                      alternate
                                                      extraction)

Audit-only; wires into nothing.  DO NOT use any number here in
production.
"""
from __future__ import annotations

# Path bridge (cluster-subdirectory flat-namespace imports).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import os  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

os.environ.setdefault("QOU_COMPUTE_DPS", "60")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(60)

from witness_base import WitnessBuilder, q0_comparison  # noqa: E402
from markov_trace_recursive import (  # noqa: E402
    markov_trace_of_word, q as HECKE_Q)
from habiro_borromean_colored_jones import (  # noqa: E402
    habiro_borromean, s as GL_S)

HERE = Path(__file__).resolve().parent

sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))
from q_parameter import Q_50_DIGIT_STR as Q0_PROTON_STR, q_muon_at  # noqa: E402

# q₀ anchors read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03).
# The muon leg was the literal 1.1099785955573… — the RETIRED self-certified
# muon pin A, superseded 2026-08-22 by the live CODATA-2022 lepton-ratio
# derivation q_muon_at() (+0.0769 ppb). `q_parameter` rather than
# `qou_substrate.constants` so the witness gets its anchor stamp.
Q0_MUON_STR = mp.nstr(q_muon_at(50), 50, strip_zeros=False)

# targets (registry KC10 shadows + empirical c₃ provenance, see docstring)
C2_SHADOW = sp.Integer(-1)
C3_SHADOW = sp.Integer(-2)
C3_EMP = {
    "proton_quoted": mp.mpf("-2.06934257711516783787971951725"),
    "muon_quoted": mp.mpf("-2.0097"),
    "cache_computations_q0": mp.mpf("-2.02018812814143945582016855395"),
}

BETA_BOR = (1, -2, 1, -2, 1, -2)   # (σ₁σ₂⁻¹)³, signed 1-indexed
ORDER = 10                         # ℏ-series order (→ u_L^4 via a_8; C13 value)

# symbols: framework q; s = the SAME framework q inside the GL2011
# transcription (whose Jones variable is t = s²); ℏ shadow variable
qs = sp.Symbol("q", positive=True)
hb = sp.Symbol("hbar")
bsym = sp.Symbol("b", positive=True)


# ===========================================================================
# Step 1 — the invariant two ways (framework Hecke vs literature)
# ===========================================================================

def tau_D(qv):
    """Lean-proved Borromean Markov-trace closed form (convention D,
    BorromeanMarkovTrace.lean; the SIGNED form — no abs(): near q=1 it
    is positive, and the shadow expansion needs the analytic branch).

        τ_D(q) = (4 + h² − 3h⁴ − h⁶)/(h² + 4),  h = q − q⁻¹.
    """
    h = qv - 1 / qv
    return (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)


def qfact3(qv):
    """[3]_q! = [3]_q·[2]_q (balanced) — YLambdaQSchur.lean closed form."""
    return (qv**2 + 1 + qv**-2) * (qv + 1 / qv)


def F_Bor_expr(qv):
    """canonical_mass / m_p_substrate_identity F_Bor = τ·[3]_q!/q³
    (signed τ_D; |·| is a no-op near q = 1 where τ_D > 0)."""
    return tau_D(qv) * qfact3(qv) / qv**3


def literature_jones_L6a4(t):
    """External literature closed form: Jones polynomial of the
    Borromean rings L6a4 (Knot Atlas / LinkInfo; 3-component, integer
    powers, amphichiral ⇒ palindromic)."""
    return (-t**-3 + 3 * t**-2 - 2 * t**-1 + 4
            - 2 * t + 3 * t**2 - t**3)


def cross_check_gate():
    """G1 + G2 exact identities (STOP on failure), plus the recorded
    D≠C split. Returns (checks, tau_C_in_s, JB2)."""
    checks = []

    # literature object: GL2011/Habiro colored Jones at n=2 (Laurent in
    # the transcription's s = t^{1/2}); TL₃-verified in-corpus.
    JB2 = sp.expand(habiro_borromean(2))

    # G1: transcription == external literature closed form (t = s²)
    g1 = sp.cancel(sp.together(
        JB2 - literature_jones_L6a4(GL_S**2))) == 0
    checks.append(("G1_transcription_eq_literature_L6a4", g1))

    # G2: framework (Lean closed form) == literature, exact:
    #     J_B(s) = [2]² · τ_D  with framework q = s, [2] = q + q⁻¹
    #     (framework variable q ↔ √t of the Jones variable t = s²)
    two_sq = (GL_S + 1 / GL_S) ** 2
    g2 = sp.cancel(sp.together(
        JB2 - two_sq * tau_D(GL_S))) == 0
    checks.append(("G2_framework_tauD_eq_literature_jones", g2))

    # framework canonical z-trace (convention C) of the signed word —
    # the corpus's own Hecke machinery evaluation of β_Bor.
    trC = markov_trace_of_word(3, list(BETA_BOR))
    s_ = sp.Symbol("s", positive=True)
    tau_C_s = sp.cancel(sp.together(trC.subs(HECKE_Q, s_**2)))  # q = s²

    # recorded (NOT a stop): D ≠ C exactly — the documented corpus
    # convention split (2026-06-09 audit; PR #3261 probe).
    d_minus_c = sp.cancel(sp.together(tau_D(s_**2) - tau_C_s))
    d_eq_c = sp.simplify(d_minus_c) == 0
    checks.append(("recorded_D_eq_C_split_expected_False", d_eq_c))

    # classical-limit sanities
    checks.append(("tauD_at_q1_eq_1", sp.simplify(tau_D(qs).subs(qs, 1)) == 1))
    checks.append(("JB2_at_q1_eq_4", sp.simplify(JB2.subs(GL_S, 1)) == 4))
    checks.append(("FBor_at_q1_eq_6",
                   sp.simplify(F_Bor_expr(qs).subs(qs, 1)) == 6))

    return checks, tau_C_s, s_, JB2


# ===========================================================================
# Step 2 — q=1 shadow expansions (exact rationals; ℏ = 1 − 1/q)
# ===========================================================================

def shadow_series_in_q(X_of_q, classical, order=ORDER):
    """Exact ℏ-Taylor of X(q)/X(1) with q = 1/(1−ℏ) (C13 convention)."""
    ser = sp.series((X_of_q / classical).subs(qs, 1 / (1 - hb)),
                    hb, 0, order).removeO()
    return [sp.nsimplify(sp.expand(ser).coeff(hb, n)) for n in range(order)]


def shadow_series_in_s(X_of_s, s_, classical, order=ORDER):
    """Same, for an expression in s = √q: s = (1−ℏ)^{−1/2}."""
    ser = sp.series((X_of_s / classical).subs(s_, (1 - hb) ** sp.Rational(-1, 2)),
                    hb, 0, order).removeO()
    return [sp.nsimplify(sp.expand(ser).coeff(hb, n)) for n in range(order)]


# ===========================================================================
# Step 3 — the canonical C13 bridge peel (secondary gate)
# ===========================================================================

def bridge_peel(a):
    """C13 bridge (habiro_mode_to_ladder_bridge.py) applied verbatim:
    even-in-ℏ rungs are the integer-u_L ladder G_k = a_{2k}/b^k
    (u_L = b·ℏ²); seed 1 + N·Σ_{k≥2} G_k u_L^k; the single scale
    d.o.f. N is fixed by the proved c_2 = −1; read c_3, c_4 off the
    log-series.  Returns symbolic {2,3,4} in b, or None if the scale
    fix is unsolvable (G_2 = 0)."""
    G = {k: a[2 * k] / bsym**k for k in range(0, ORDER // 2)}
    uL, N = sp.symbols("u_L N", positive=True)
    seed = sp.expand(1 + N * sum(G[k] * uL**k for k in range(2, ORDER // 2)))
    logseed = sp.series(sp.log(seed), uL, 0, ORDER // 2).removeO()
    L = {k: sp.nsimplify(sp.expand(logseed).coeff(uL, k))
         for k in range(2, ORDER // 2)}
    Nsol = sp.solve(sp.Eq(L[2], -1), N)
    if not Nsol:
        return None
    Nv = Nsol[0]
    return {
        2: sp.simplify(L[2].subs(N, Nv)),
        3: sp.simplify(L[3].subs(N, Nv)),
        4: sp.simplify((L[4] + sp.Rational(1, 2) * L[2] ** 2).subs(N, Nv)),
    }


def b_of_q(q_mpf):
    """Hoefsmit ladder constant b(q) = √((h²+3)/(h²+4)), h = q − 1/q —
    the C14 probe's canonical definition (matches the
    q-beta-operator-valued-N3 witness hoefsmit_b at the muon q₀)."""
    h = q_mpf - 1 / q_mpf
    return mp.sqrt((h**2 + 3) / (h**2 + 4))


# ===========================================================================
def main() -> int:
    t0 = time.monotonic()
    print("=" * 76)
    print(" Q_β PROBE 3 — Borromean forced-candidate cyclotomic / q=1 shadow")
    print("=" * 76)

    qp = mp.mpf(Q0_PROTON_STR)
    qm = mp.mpf(Q0_MUON_STR)
    print(f"  proton q₀ = {mp.nstr(qp, 30)}")
    print(f"  muon   q₀ = {mp.nstr(qm, 30)}")
    print(f"  targets: c_2 shadow = {C2_SHADOW}, c_3 shadow = {C3_SHADOW}")

    # ---- Step 1: two-way cross-check gate -----------------------------
    print("\n" + "-" * 76)
    print(" Step 1: invariant two ways (framework Hecke vs literature) — GATE")
    print("-" * 76)
    checks, tau_C_s, s_, JB2 = cross_check_gate()
    for name, ok in checks:
        print(f"  [{'PASS' if ok else ('ok(split)' if name.startswith('recorded') else 'FAIL')}] {name} = {ok}")
    gate_ok = (dict(checks)["G1_transcription_eq_literature_L6a4"]
               and dict(checks)["G2_framework_tauD_eq_literature_jones"]
               and dict(checks)["tauD_at_q1_eq_1"]
               and dict(checks)["JB2_at_q1_eq_4"]
               and dict(checks)["FBor_at_q1_eq_6"])
    d_eq_c = dict(checks)["recorded_D_eq_C_split_expected_False"]
    if not gate_ok:
        print("\n  !! CROSS-CHECK GATE FAILED — framework and literature "
              "invariants disagree.  STOP; no downstream numbers trusted.")
        return 2
    # numeric size of the documented D−C split at both anchors
    split = {}
    for tag, qv in (("proton", qp), ("muon", qm)):
        tD = tau_D(mp.mpf(1) * qv)
        # τ_C numeric: substitute s = √q at 60 dps via decimal string
        tC = mp.mpf(str(sp.N(tau_C_s.subs(s_, sp.sqrt(sp.Rational(str(qv)))), 55)))
        split[tag] = mp.nstr(tD - tC, 10)
        print(f"  D−C split at {tag} q₀: {split[tag]}  (documented corpus "
              f"convention fork; D = F_Bor production convention, D = literature Jones)")

    # ---- Step 2: shadow expansions ------------------------------------
    print("\n" + "-" * 76)
    print(" Step 2: q=1 shadow expansions (exact; ℏ = 1 − 1/q)")
    print("-" * 76)
    series = {
        "N1_tau_D": shadow_series_in_q(tau_D(qs), sp.Integer(1)),
        "N2_tau_C": shadow_series_in_s(tau_C_s, s_, sp.Integer(1)),
        "N3_F_Bor_over_6": shadow_series_in_q(F_Bor_expr(qs), sp.Integer(6)),
        # N4: literature Jones in the FRAMEWORK variable — per the exact
        # identity G2, J_B at framework q is [2]²·τ_D(q) (Jones t = q²),
        # so the framework shadow of J_B/4 expands that expression in
        # the same ℏ = 1 − 1/q as N1/N3.  (Expanding in the Jones
        # variable's own ℏ would be a SECOND, non-framework convention —
        # excluded by the zero-free-choice discipline.)
        "N4_J_B_over_4": shadow_series_in_q(
            (qs + 1 / qs) ** 2 * tau_D(qs), sp.Integer(4)),
    }
    for name, a in series.items():
        print(f"\n  {name}: a_n (n=0..{ORDER - 1}) = {a}")
        print(f"      a_2 = {a[2]}  (target −1)   a_3 = {a[3]}  (target −2)")

    raw_hit = {
        name: bool(a[2] == C2_SHADOW and a[3] == C3_SHADOW)
        for name, a in series.items()
    }
    any_raw = any(raw_hit.values())
    print(f"\n  PRIMARY GATE (a_2 = −1 ∧ a_3 = −2, parameter-free): "
          f"{'HIT: ' + str(raw_hit) if any_raw else 'NO normalisation hits'}")

    # ---- Step 3: canonical C13 bridge peel (secondary) ----------------
    print("\n" + "-" * 76)
    print(" Step 3: C13 bridge peel (even-in-ℏ → u_L ladder; c_2 = −1 scale fix)")
    print("-" * 76)
    b_p, b_m = b_of_q(qp), b_of_q(qm)
    print(f"  b(proton q₀) = {mp.nstr(b_p, 25)}   b(muon q₀) = {mp.nstr(b_m, 25)}")
    peel = {}
    peel_c3_num = {}
    for name, a in series.items():
        res = bridge_peel(a)
        if res is None:
            print(f"\n  [{name}] scale fix c_2 = −1 UNSOLVABLE (a_4 = {a[4]})")
            peel[name] = {"solvable": False, "a_4": str(a[4])}
            continue
        c3_p = mp.mpf(str(sp.N(res[3].subs(bsym, sp.Rational(str(b_p))), 50)))
        c3_m = mp.mpf(str(sp.N(res[3].subs(bsym, sp.Rational(str(b_m))), 50)))
        peel[name] = {
            "solvable": True,
            "c_3_symbolic": str(res[3]),
            "c_4_symbolic": str(res[4]),
            "c_3_at_proton_b": mp.nstr(c3_p, 30),
            "c_3_at_muon_b": mp.nstr(c3_m, 30),
        }
        peel_c3_num[name] = (c3_p, c3_m)
        print(f"\n  [{name}] c_3 = {res[3]}   c_4 = {res[4]}")
        print(f"      c_3(b_proton) = {mp.nstr(c3_p, 20)}   "
              f"c_3(b_muon) = {mp.nstr(c3_m, 20)}")
        print(f"      vs shadow −2: rel resid "
              f"{mp.nstr(abs(c3_p + 2) / 2, 8)} (p) / "
              f"{mp.nstr(abs(c3_m + 2) / 2, 8)} (μ)")
        for tag, emp in C3_EMP.items():
            print(f"      vs empirical {tag} {mp.nstr(emp, 12)}: rel resid "
                  f"{mp.nstr(abs(c3_p - emp) / abs(emp), 8)} (p) / "
                  f"{mp.nstr(abs(c3_m - emp) / abs(emp), 8)} (μ)")

    # secondary gate: peel c_3 within 0.1% of the −2 shadow at BOTH
    # anchors (same tolerance the C14 probe pre-stated; a structural
    # match should be exact, 0.1% allows convention slack only)
    TOL = mp.mpf("0.001")
    peel_hit = {
        name: bool(abs(c3p + 2) / 2 < TOL and abs(c3m + 2) / 2 < TOL)
        for name, (c3p, c3m) in peel_c3_num.items()
    }
    any_peel = any(peel_hit.values())
    print(f"\n  SECONDARY GATE (bridge-peel c_3 → −2 within 0.1% at both "
          f"anchors): {'HIT: ' + str(peel_hit) if any_peel else 'NO normalisation hits'}")

    # ---- Verdict -------------------------------------------------------
    print("\n" + "-" * 76)
    print(" Verdict")
    print("-" * 76)
    passed_gate = any_raw or any_peel
    if passed_gate:
        verdict = "GATE-PASSED near-match — NOT a derivation; NO wiring proposed"
        summary = (
            "A canonical Borromean normalisation reproduces the ladder "
            "shadows parameter-free; residuals at both anchors recorded. "
            "Escalate for structural analysis; do NOT wire.")
    else:
        verdict = "NEGATIVE"
        summary = (
            "No canonical framework normalisation of the Borromean "
            "invariant (τ_D Lean closed form; τ_C canonical z-trace; "
            "F_Bor/6; literature Jones/4) reproduces c_2 = −1 AND the "
            "c_3 q=1 shadow −2 parameter-free, in the raw ℏ-shadow "
            "(τ_D vanishes to order ℏ³ — Brunnian (q−1)-adic vanishing "
            "— so a_2 = a_3 = 0; F_Bor/6 gives 29/6, −14/3; J_B/4 gives "
            "1, 1) or through the canonical C13 bridge peel (c_3 = "
            "−23/(6b) ≈ −4.42 (τ_D), −83/(12b) ≈ −7.97 (τ_C), "
            "−191/(55b) ≈ −4.00 (F_Bor/6), −225/(43b) ≈ −6.03 (J_B/4) "
            "— none −2 within 0.1%).  Scope-limited (a): the Borromean q=1 "
            "shadow ALONE, under the corpus's canonical normalisations, "
            "does not carry the ladder shadows.  New refuted row (C15 "
            "candidate: forced-link Borromean cyclotomic/q=1 shadow). "
            "NOT a structural exclusion of the Borromean data from any "
            "multi-term closure.  No scan was run; no fit was made.")
    print(f"  VERDICT: {verdict}")
    print(f"  {summary}")

    # ---- Witness --------------------------------------------------------
    builder = WitnessBuilder(
        "qbeta-borromean-cyclotomic", engine="sympy", start_time=t0)
    builder.set_description(
        "PROBE 3 (2026-07-11 avenues audit §3.C): q=1 Taylor shadow of the "
        "framework-normalised Borromean-rings invariant — the forced "
        "candidate C14 missed — tested parameter-free against the ladder "
        "shadows c_2=−1 and c_3→−2 (registry KC10). Invariant obtained two "
        "ways and cross-checked exactly: framework Hecke (Lean "
        "BorromeanMarkovTrace closed form τ_D used by canonical_mass F_Bor; "
        "canonical recursive z-trace τ_C of the signed word (1,−2,1,−2,1,−2)) "
        "vs literature (GL2011/Habiro colored Jones n=2 == Knot Atlas L6a4 "
        "closed form; exact identity J_B(s)=[2]²·τ_D at framework q=s). "
        "Shadow expansions in ℏ=1−1/q (C13 bridge convention) for the four "
        "corpus-canonical normalisations only; secondary gate via the "
        "canonical C13 bridge peel with the single c_2=−1 scale d.o.f. "
        "Zero free choices: no link/root/normalisation scan. Audit-only.")
    builder.set_audit_only(
        "docs/audits/2026-07-11-qbeta-ck-untested-avenues-and-literature.md")
    builder.add_parameter("compute_dps", 60)
    builder.add_parameter("q0_proton", Q0_PROTON_STR)
    builder.add_parameter("q0_muon", Q0_MUON_STR)
    builder.add_parameter("beta_borromean_word", list(BETA_BOR))
    builder.add_parameter("hbar_series_order", ORDER)
    builder.add_data("cross_check_gate", {name: bool(ok) for name, ok in checks})
    builder.add_data("D_minus_C_split_at_anchors", split)
    builder.add_data("shadow_series_exact",
                     {name: [str(c) for c in a] for name, a in series.items()})
    builder.add_data("raw_shadow_gate",
                     {"targets": {"a_2": "-1", "a_3": "-2"}, "hits": raw_hit})
    builder.add_data("bridge_peel", peel)
    builder.add_data("bridge_peel_gate", peel_hit)
    builder.add_data("hoefsmit_b_at_anchors", {
        "proton": mp.nstr(b_p, 40), "muon": mp.nstr(b_m, 40)})
    builder.add_data("empirical_c3_reference",
                     {k: mp.nstr(v, 30) for k, v in C3_EMP.items()})
    builder.add_data("verdict", {"overall": verdict, "summary": summary})
    builder.add_caveat(
        "τ_C ≠ τ_D is the documented corpus trace-convention split "
        "(docs/audits/2026-06-09-binding-trace-convention-split.md, "
        "PR #3261 probe); both are reported. τ_D is the production F_Bor "
        "convention and equals the literature Jones exactly (G2).")
    builder.add_caveat(
        "Scope-limited (a) refutation only: constrains the Borromean q=1 "
        "shadow AS SOLE MECHANISM under canonical normalisations; does not "
        "exclude Borromean data from a multi-term closure.")
    builder.add_assertion(
        "two_way_cross_check_exact",
        computed=str(int(bool(gate_ok))), expected="1.0", tolerance="0.0",
        source="G1: GL2011 transcription == Knot Atlas L6a4 closed form "
               "(t=s², exact); G2: J_B(s) == [2]²·τ_D(q=s) (exact, sympy "
               "cancel over ℚ(s)); classical limits τ_D(1)=1, J_B(1)=4, "
               "F_Bor(1)=6.")
    builder.add_assertion(
        "documented_D_neq_C_split_reproduced",
        computed=0.0 if not d_eq_c else 1.0, expected="0.0", tolerance="0.0",
        source="Convention D (Lean closed form) ≠ convention C (canonical "
               "z-trace) exactly, per the 2026-06-09 audit — reproduced here.")
    builder.add_assertion(
        "forced_borromean_reproduces_c2_and_c3_shadow_param_free",
        computed=str(int(bool(passed_gate))),
        expected="0.0",  # honest expected outcome is NEGATIVE
        tolerance="0.0",
        source="Kill criterion (pre-stated): PASS only if a canonical "
               "normalisation reproduces a_2=−1 ∧ a_3=−2 raw, or the C13 "
               "bridge-peel c_3 = −2 within 0.1% at both anchors, with "
               "zero free choices.")
    builder.save(q0_comparison(
        muon=Q0_MUON_STR, proton=Q0_PROTON_STR,
        reason="b(q₀) and the empirical-c₃ residuals are evaluated at BOTH pins; the cyclotomic shadow coefficients are exact rationals and anchor-independent"))
    print("\n  witness → qbeta-borromean-cyclotomic.witness.json")
    print(f"  wall: {round(time.monotonic() - t0, 1)} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
