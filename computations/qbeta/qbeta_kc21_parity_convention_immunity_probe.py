#!/usr/bin/env python3
"""
Bean qou-kc21im: is KC21's "structural parity is convention-immune" claim
VERIFIED, or was it ASSERTED?

PR #5107 split the c_3 record into a value layer (C-conditional) and a
structural layer, and added this sentence to the KC21 registry row:

    "the structural parity statement (S(-eps) = -S(eps)) and the 1/u^3
     result are convention-immune"

The 1/u^3 half WAS measured there (swing ratio D/C = 1.0052). The parity half
was not: no probe re-derived the parity under convention D, and no z-free
dependency chain was written out. The claim is non-obvious because c_3(q) is
not a convention-free object -- it is DEFINED BY an extractor whose N=1 rung
consumes the convention-C Markov parameter (alpha = (z-1)h/2,
qbeta_utils.py:124-125), and under D the extractor returns a numerically and
structurally different function (c_3 ~ -974 rather than ~ -2.07).  Parity of
the function f_C does not transfer to f_D merely because both are called c_3.

WHAT THIS PROBE MEASURES (60 dps, proton pin per the 2026-08-07 experimental-
anchor directive; complex q = q0 + i*eps).

  Route 1 -- re-derive the parity under D:
    A1  regression: the complexified extractor at eps = 0 reproduces the
        committed C-frame value c_3(proton) = -2.06934258, so the object
        being tested is the corpus object.
    A2  analytic-continuation branch: qbeta_utils uses |q^2-2q-1|, which is
        NOT holomorphic. Near q0 the sign is negative, so the analytic Q_A is
        the SIGNED form (2q+1-q^2). Recorded because any complex-eps probe
        that keeps the abs() silently tests the wrong function.
    A3  eps-parity under C: Im c_3(q0-i.eps) = -Im c_3(q0+i.eps), and
        Re c_3(q0-i.eps) = +Re c_3(q0+i.eps), over eps in 1e-30 .. 1e-2.
    A4  eps-parity under D: the same, with z_D = q^3/(q^2+1).  <-- the test
        the immunity claim needed.
    A5  non-vacuity: Im c_3^D(q0+i.eps) != 0 for eps != 0, so A4 is not the
        trivial 0 = -0.
    A6  the two frames really are different functions: c_3^D(q0) ~ -974,
        |c_3^D - c_3^C| ~ 972 -- parity survives a change that moves the
        value by 470x its own magnitude.
    A7  Im vanishes at real substrate under both frames (the
        fig8Trace_im_real_zero analogue).

  Route 2 -- exhibit the reduction (why it is immune):
    A8  every ladder ingredient satisfies Schwarz reflection
        f(conj q) = conj f(q): h, hbar, b, u, Q_A(signed), z_C, z_D.  The
        composite therefore does too, and Im(composite) is odd in eps.
    A9  z_D's reflection is EXACT (sympy, a+bi with a,b real): rational
        function with rational coefficients.
    A10 GENERICITY: the parity also holds for a third, arbitrary convention
        z_X = q/(1+q^2) that appears nowhere in the corpus.  So the immunity
        is a property of the CLASS "z real-analytic and real-valued on the
        real q-axis", not a coincidence of C and D.  This is the reduction:
        no z-bearing input can break the parity, because the parity consumes
        only real-valuedness of z on the real axis -- never its formula.

  The mechanism correction (honest finding, not a refutation):
    A11 the SAME eps-parity holds for Q_A alone -- a manifestly bar-EVEN
        ingredient.  So "Im odd in eps" does not single out the bar-odd
        channel; it holds for every real-analytic ingredient regardless of
        bar parity.  KC21 states the derivation as "bar-odd ==> odd in eps";
        what the Lean anchors (fig8Trace_im_odd via fig8TraceC_conj) actually
        prove is "real coefficients ==> Im odd in eps".  The conclusion is
        right and immune; the stated reason is not the operative one, and the
        parity is correspondingly weaker as evidence FOR bar-oddness.
    A12 the literal reading fails: S(-eps) = -S(eps) as a statement about the
        full complex value is FALSE (Re S is even, not odd, and nonzero).
        The true statement -- the one the Lean proves -- is about the
        imaginary part / decay projection only.

SCOPE -- scope-(a) throughout.  This probe adjudicates NO convention for the
Q_beta channel (bean qou-b3nk); it does not revive any C-conditional value;
it does not touch the bar-parity (sigma: q -> 1/q) question, which is a
different involution from complex conjugation and is NOT settled here.  Per
AGENTS.md "Defined residual != derived decomposition", S = c_3 + Vol(4_1)
remains a residual of a C-frame extraction; nothing below upgrades it.
Nothing is wired; no c_k value changes; no tier is flipped on assertion.
"""

import datetime
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

mp.mp.dps = 60

# Same source the ladder producer uses (qbeta_ck_cache.py:69,78) -- NOT
# qou_substrate.constants, which carries no Q_beta.
ME = mp.mpf(str(M_E_MEV))
QCOD = mp.mpf(str(Q_BETA_MEV))
C2 = mp.mpf("-1")  # Lean-proved Taylor-exact rung (C-frame object, PR #5107)

# Committed corpus value for the C-frame extraction at the proton pin
# (registry section 9f window endpoint; qbeta-c3-barodd-sleak.witness.json).
CORPUS_C3_PROTON = mp.mpf("-2.06934258")

# eps ladder: six decades, so a parity that held only at linear order in eps
# would be caught at the large end.
EPS_LADDER = ["1e-30", "1e-24", "1e-18", "1e-12", "1e-8", "1e-5", "1e-3", "1e-2"]

PARITY_TOL = mp.mpf("1e-45")  # relative; 60 dps working precision


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def z_of(q, conv: str):
    """Markov parameter under trace convention C, D, or the control X.

    C (full-Hecke Ocneanu/Wenzl):   sqrt(q)/(1+q)
    D (SU(2)/Temperley-Lieb Jones): q^3/(q^2+1)      -- owner ruling 2026-08-09
    X (control, in no channel):     q/(1+q^2)        -- genericity probe only
    """
    if conv == "C":
        return mp.sqrt(q) / (1 + q)
    if conv == "D":
        return q ** 3 / (q ** 2 + 1)
    if conv == "X":
        return q / (1 + q ** 2)
    raise ValueError(f"unknown convention {conv!r}")


def q_a_signed(q):
    """Q_A/m_e with the ANALYTIC (signed) branch of |q^2 - 2q - 1|.

    qbeta_utils writes mpfabs(q**2 - 2*q - 1); at q0 ~ 1.11 that argument is
    ~ -1.99 < 0, so the holomorphic continuation is -(q^2-2q-1) = 2q+1-q^2 --
    the same form the exact-series ladder uses
    (qbeta_ck_sseries_exact_rational.py:241).  abs() is real-valued and not
    holomorphic; using it under complex eps would test a different function.
    """
    return (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)


def ladder(q, conv: str) -> dict:
    """Q_beta precision ladder at (possibly complex) q, N=1 phase on z(conv).

    Mirrors qbeta_utils.substrate_ladder_quantities + c3_target_at, with two
    deliberate differences, both required for a complex-argument evaluation
    and both asserted below: z is parameterised by convention (A3/A4/A10), and
    Q_A takes the signed branch (A2).
    """
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    z = z_of(q, conv)
    alpha = (z - 1) * h / 2
    qa = q_a_signed(q)
    q_n1 = ME * qa * mp.cos(alpha - b * hbar ** 2 / 2)
    q_n2 = q_n1 * (1 + C2 * u ** 2)
    c3 = (QCOD / q_n2 - 1) / u ** 3
    return {"h": h, "hbar": hbar, "b": b, "u": u, "z": z, "alpha": alpha,
            "q_a": qa, "q_n2": q_n2, "c3": c3}


def c3_at(q, conv: str):
    return ladder(q, conv)["c3"]


def _relerr(a, b):
    """Relative error |a-b|/max(1,|b|), as an mpf."""
    d = abs(a - b)
    scale = max(mp.mpf(1), abs(b))
    return d / scale


def parity_scan(q0, conv: str) -> dict:
    """Test Im c_3(q0-i.eps) = -Im c_3(q0+i.eps) and Re even, over EPS_LADDER."""
    worst_im = mp.mpf(0)
    worst_re = mp.mpf(0)
    rows = []
    for e in EPS_LADDER:
        eps = mp.mpf(e)
        cp = c3_at(mp.mpc(q0, eps), conv)
        cm = c3_at(mp.mpc(q0, -eps), conv)
        # odd in the imaginary part, even in the real part
        eim = _relerr(cm.imag, -cp.imag)
        ere = _relerr(cm.real, cp.real)
        worst_im = max(worst_im, eim)
        worst_re = max(worst_re, ere)
        rows.append({"eps": e,
                     "im_plus": mp.nstr(cp.imag, 12),
                     "re_plus": mp.nstr(cp.real, 12),
                     "odd_relerr": mp.nstr(eim, 4),
                     "even_relerr": mp.nstr(ere, 4)})
    return {"worst_odd_relerr": worst_im, "worst_even_relerr": worst_re,
            "rows": rows}


def reflection_relerr(fn, q0) -> mp.mpf:
    """Worst |f(conj q) - conj f(q)| / max(1,|f(q)|) over a grid of complex q.

    This is the Schwarz-reflection property.  A function holomorphic on a
    conjugate-symmetric neighbourhood of a real interval and real-valued on
    that interval satisfies it; that -- and nothing about the function's
    formula -- is what makes Im f odd in eps.
    """
    worst = mp.mpf(0)
    for e in ("1e-20", "1e-10", "1e-4", "1e-2"):
        for dq in ("0", "1e-3", "-1e-3"):
            q = mp.mpc(q0 + mp.mpf(dq), mp.mpf(e))
            lhs = fn(mp.conj(q))
            rhs = mp.conj(fn(q))
            worst = max(worst, _relerr(lhs, rhs))
    return worst


def main() -> int:
    t0 = time.monotonic()
    q0 = mp.mpf(str(q_at()))  # proton pin (2026-08-07 experimental-anchor directive)

    assertions = []

    def record(name, passed, detail):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}: {detail}")

    print(f"KC21 parity convention-immunity audit (bean qou-kc21im)")
    print(f"  q0 (proton pin) = {mp.nstr(q0, 25)}   dps = {mp.mp.dps}\n")

    # ---- A1 regression: the complexified extractor IS the corpus object ----
    c3_c_real = c3_at(mp.mpc(q0, 0), "C").real
    c3_util = c3_target_at(q0, QCOD, ME)
    reg_vs_util = _relerr(c3_c_real, mp.mpf(str(c3_util)))
    reg_vs_corpus = abs(c3_c_real - CORPUS_C3_PROTON)
    record("A1-regression-reproduces-corpus-c3",
           reg_vs_util < mp.mpf("1e-40") and reg_vs_corpus < mp.mpf("1e-7"),
           f"c3^C(q0) = {mp.nstr(c3_c_real, 12)}; vs qbeta_utils relerr "
           f"{mp.nstr(reg_vs_util, 4)}; vs committed {mp.nstr(CORPUS_C3_PROTON, 10)} "
           f"absdiff {mp.nstr(reg_vs_corpus, 4)}")

    # ---- A2 the analytic branch of Q_A ----
    abs_form = abs(q0 ** 2 - 2 * q0 - 1) * (q0 + 1) / (2 * q0 ** 3)
    signed_form = q_a_signed(q0)
    arg_sign = q0 ** 2 - 2 * q0 - 1
    record("A2-QA-analytic-branch-is-signed-form",
           _relerr(abs_form, signed_form) < mp.mpf("1e-50") and arg_sign < 0,
           f"q^2-2q-1 = {mp.nstr(arg_sign, 8)} < 0 at q0, so |.| continues as "
           f"(2q+1-q^2); abs vs signed relerr {mp.nstr(_relerr(abs_form, signed_form), 4)}")

    # ---- A3 / A4 / A10 the parity scans ----
    scans = {conv: parity_scan(q0, conv) for conv in ("C", "D", "X")}

    record("A3-eps-parity-holds-under-convention-C",
           scans["C"]["worst_odd_relerr"] < PARITY_TOL
           and scans["C"]["worst_even_relerr"] < PARITY_TOL,
           f"worst odd relerr {mp.nstr(scans['C']['worst_odd_relerr'], 4)}, "
           f"worst even relerr {mp.nstr(scans['C']['worst_even_relerr'], 4)} "
           f"over eps in [{EPS_LADDER[0]}, {EPS_LADDER[-1]}]")

    record("A4-eps-parity-holds-under-convention-D",
           scans["D"]["worst_odd_relerr"] < PARITY_TOL
           and scans["D"]["worst_even_relerr"] < PARITY_TOL,
           f"worst odd relerr {mp.nstr(scans['D']['worst_odd_relerr'], 4)}, "
           f"worst even relerr {mp.nstr(scans['D']['worst_even_relerr'], 4)} "
           f"-- the immunity claim's missing test")

    record("A10-eps-parity-holds-under-a-control-convention-X",
           scans["X"]["worst_odd_relerr"] < PARITY_TOL,
           f"z_X = q/(1+q^2) (in no channel): worst odd relerr "
           f"{mp.nstr(scans['X']['worst_odd_relerr'], 4)} -- immunity is a class "
           f"property, not a C/D coincidence")

    # ---- A5 non-vacuity ----
    im_probe = c3_at(mp.mpc(q0, mp.mpf("1e-8")), "D").imag
    record("A5-parity-under-D-is-non-vacuous",
           abs(im_probe) > mp.mpf("1e-20"),
           f"Im c3^D(q0 + 1e-8i) = {mp.nstr(im_probe, 12)} != 0, so A4 is not 0 = -0")

    # ---- A6 the two frames are genuinely different functions ----
    c3_d_real = c3_at(mp.mpc(q0, 0), "D").real
    frame_gap = abs(c3_d_real - c3_c_real)
    record("A6-D-frame-is-a-different-function",
           frame_gap > mp.mpf("900"),
           f"c3^D(q0) = {mp.nstr(c3_d_real, 12)} vs c3^C(q0) = "
           f"{mp.nstr(c3_c_real, 12)}; gap {mp.nstr(frame_gap, 10)} "
           f"(~{mp.nstr(frame_gap / abs(c3_c_real), 5)}x |c3^C|) -- parity survives it")

    # ---- A7 Im vanishes at real substrate (fig8Trace_im_real_zero analogue) ----
    im0 = {conv: abs(c3_at(mp.mpc(q0, 0), conv).imag) for conv in ("C", "D")}
    record("A7-Im-vanishes-at-real-substrate-both-frames",
           im0["C"] < mp.mpf("1e-50") and im0["D"] < mp.mpf("1e-50"),
           f"|Im c3^C(q0)| = {mp.nstr(im0['C'], 4)}, |Im c3^D(q0)| = "
           f"{mp.nstr(im0['D'], 4)}")

    # ---- A8 the reduction: every ingredient is Schwarz-reflective ----
    ingredients = {
        "h": lambda q: q - 1 / q,
        "hbar": lambda q: (q - 1) / q,
        "b": lambda q: mp.sqrt(((q - 1 / q) ** 2 + 3) / ((q - 1 / q) ** 2 + 4)),
        "u": lambda q: mp.sqrt(((q - 1 / q) ** 2 + 3) / ((q - 1 / q) ** 2 + 4))
        * ((q - 1) / q) ** 2,
        "Q_A_signed": q_a_signed,
        "z_C": lambda q: z_of(q, "C"),
        "z_D": lambda q: z_of(q, "D"),
        "z_X": lambda q: z_of(q, "X"),
        "cos": mp.cos,
    }
    refl = {k: reflection_relerr(f, q0) for k, f in ingredients.items()}
    worst_refl = max(refl.values())
    record("A8-every-ladder-ingredient-is-Schwarz-reflective",
           worst_refl < mp.mpf("1e-45"),
           "f(conj q) = conj f(q) for " + ", ".join(sorted(ingredients))
           + f"; worst relerr {mp.nstr(worst_refl, 4)} "
             f"(worst at '{max(refl, key=lambda k: refl[k])}')")

    # ---- A9 z_D's reflection is exact (sympy) ----
    a, bb = sp.symbols("a b", real=True)
    qs = a + sp.I * bb
    zd = qs ** 3 / (qs ** 2 + 1)
    zd_refl = sp.simplify(sp.expand(
        (zd.subs({bb: -bb}) - sp.conjugate(zd).rewrite(sp.conjugate)).rewrite(sp.I)))
    zd_refl = sp.simplify(sp.together(sp.expand_complex(
        zd.subs({bb: -bb}) - sp.conjugate(zd))))
    record("A9-z_D-reflection-exact-symbolic",
           zd_refl == 0,
           f"sympy: z_D(conj q) - conj(z_D(q)) = {zd_refl} (exact zero); z_D is a "
           f"rational function with rational coefficients")

    # ---- A11 the mechanism correction: bar-EVEN ingredients have it too ----
    qa_scan_odd = mp.mpf(0)
    for e in ("1e-20", "1e-8", "1e-3"):
        eps = mp.mpf(e)
        p = q_a_signed(mp.mpc(q0, eps))
        m = q_a_signed(mp.mpc(q0, -eps))
        qa_scan_odd = max(qa_scan_odd, _relerr(m.imag, -p.imag))
    record("A11-eps-parity-does-not-single-out-the-bar-odd-channel",
           qa_scan_odd < mp.mpf("1e-45"),
           f"Q_A (bar-even) has the SAME Im-odd-in-eps property, worst relerr "
           f"{mp.nstr(qa_scan_odd, 4)}: the operative hypothesis is real "
           f"coefficients, not bar-oddness")

    # ---- A12 the literal reading of "S(-eps) = -S(eps)" is false ----
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
    eps = mp.mpf("1e-8")
    s_p = c3_at(mp.mpc(q0, eps), "C") + VOL41
    s_m = c3_at(mp.mpc(q0, -eps), "C") + VOL41
    literal_gap = abs(s_m - (-s_p))
    record("A12-literal-full-value-oddness-is-false",
           literal_gap > mp.mpf("1e-3"),
           f"|S(-eps) - (-S(eps))| = {mp.nstr(literal_gap, 10)} (Re S is EVEN and "
           f"nonzero, Re S = {mp.nstr(s_p.real, 10)}); the true statement is about "
           f"the imaginary part / decay projection only")

    all_passed = all(x["passed"] for x in assertions)

    src = Path(__file__).read_bytes()
    witness = {
        "computation": "qbeta-kc21-parity-convention-immunity",
        "description": (
            "Audit of KC21's 'the structural parity statement (S(-eps) = "
            "-S(eps)) ... is convention-immune' sentence (registry section 9g, "
            "PR #5107), which was asserted rather than measured. Route 1: the "
            "c_3 extractor is complexified (with the signed analytic branch of "
            "Q_A) and the parity re-derived under convention D -- it HOLDS, to "
            "1e-45 relative over eight decades of eps, even though the D frame "
            "moves the value by ~972 (470x |c3^C|). Route 2: the reduction -- "
            "every ladder ingredient (h, hbar, b, u, Q_A, z_C, z_D, cos) is "
            "Schwarz-reflective, so the composite is, so Im is odd in eps; the "
            "parity consumes only real-valuedness of z on the real q-axis, "
            "never its formula, and a control convention z_X in no channel has "
            "it too. VERDICT: the immunity claim is VERIFIED. Two corrections "
            "recorded: (i) the operative hypothesis is real coefficients, not "
            "bar-oddness -- the bar-EVEN Q_A has the same property, so the "
            "parity is not evidence for the bar-odd channel; (ii) the literal "
            "full-value reading S(-eps) = -S(eps) is false (Re S is even and "
            "nonzero) -- the statement is about the imaginary part only. "
            "Scope-(a): no convention adjudicated for the Q_beta channel "
            "(qou-b3nk), no C-conditional value revived, the bar involution "
            "q -> 1/q is a different question and is NOT settled here."),
        "audit_only": True,
        "tier": "structural-parity provenance audit (60-dps measurement + exact "
                "symbolic reflection; no fit; no wiring)",
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q0, 25),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath+sympy",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "verdict": "VERIFIED-immune (eps-parity); mechanism restated",
            "c3_at_q0": {"C": mp.nstr(c3_c_real, 16), "D": mp.nstr(c3_d_real, 16)},
            "frame_gap_D_minus_C": mp.nstr(c3_d_real - c3_c_real, 12),
            "parity_worst_odd_relerr": {
                k: mp.nstr(v["worst_odd_relerr"], 6) for k, v in scans.items()},
            "parity_worst_even_relerr": {
                k: mp.nstr(v["worst_even_relerr"], 6) for k, v in scans.items()},
            "parity_scan_C": scans["C"]["rows"],
            "parity_scan_D": scans["D"]["rows"],
            "schwarz_reflection_relerr": {
                k: mp.nstr(v, 6) for k, v in refl.items()},
            "z_D_reflection_exact_symbolic": str(zd_refl),
            "eps_ladder": EPS_LADDER,
            "parity_tolerance": "1e-45",
        },
        "context": {
            "axis": "KC21 structural parity -- convention immunity (verified vs asserted)",
            "bean": "qou-kc21im",
            "claim_audited": (
                "docs/coordination/ck-dk-canonical-registry.md KC21 row + section 9g: "
                "'the structural parity statement (S(-eps)=-S(eps)) and the 1/u^3 "
                "result are convention-immune' (added PR #5107)"),
            "lean_anchors": [
                "QOU.QBeta.fig8TraceC_conj -- real coefficients => conjugation "
                "commutes with evaluation (this is the operative lemma)",
                "QOU.QBeta.fig8Trace_im_odd -- Im T(q0-i.eps) = -Im T(q0+i.eps)",
                "QOU.QBeta.fig8Trace_im_real_zero -- Im T(q0) = 0 at real substrate",
                "QOU.QBeta.ladderParity_im_odd_of_reflective -- the generalisation "
                "this audit adds: reflection alone gives the parity",
            ],
            "the_reduction": (
                "Schwarz reflection. Each ingredient is holomorphic on a "
                "conjugate-symmetric neighbourhood of the real q-interval around "
                "q0 and real-valued on it, hence f(conj q) = conj f(q); the "
                "property is closed under +, -, *, /, composition, sqrt on the "
                "principal branch away from the cut, and cos. The Markov "
                "parameter enters as ONE such ingredient, and z_C, z_D (and the "
                "control z_X) are all real-valued at real q > 0. The parity "
                "therefore never reads z's formula -- which is exactly why it is "
                "convention-immune, and why the immunity extends past the two "
                "registered conventions."),
            "hypothesis_that_could_break_it": (
                "A convention whose z is NOT real-valued on the real q-axis near "
                "q0 (e.g. one carrying an explicit i), or one introducing a branch "
                "point / pole inside the conjugate-symmetric disc used. Neither C "
                "nor D nor X does; z_C's sqrt branch point sits at q = 0 and z_D's "
                "poles at q = +-i, both far from q0 ~ 1.11."),
            "corrections_recorded": [
                "KC21 states 'bar-odd ==> odd in eps'; the Lean chain proves 'real "
                "coefficients ==> Im odd in eps' (fig8TraceC_conj). A11 shows the "
                "bar-EVEN Q_A has the same property, so the parity does not "
                "single out the bar-odd channel and is not evidence for it.",
                "The literal reading S(-eps) = -S(eps) of the full complex value "
                "is false (A12): Re S is even and nonzero. The registry sentence "
                "should read Im S, or 'the decay projection'.",
            ],
            "scope": (
                "Scope-(a). Adjudicates no convention for the Q_beta channel "
                "(open, bean qou-b3nk). Revives no C-conditional value: c_3, "
                "(H1), [3]_q/25, J-hbar^2, S_leak and q*_S stay C-conditional per "
                "registry section 9g. The bar involution sigma: q -> 1/q is a "
                "DIFFERENT involution from complex conjugation and is not touched "
                "here -- in particular bar(z_D) = q^-4 z_D (PR #5107 A2) and the "
                "z_C full-bar-condition failure (PR #5111) remain open as stated. "
                "Per 'Defined residual != derived decomposition', S = c_3 + "
                "Vol(4_1) remains a residual of a C-frame extraction."),
        },
        # int ms, not a float and not a seconds-string. A bare round() here is a
        # raw float64 and trips the NO-FLOAT64 ratchet
        # (scripts/precision-gates.sh); serializing seconds as a string dodges
        # that ratchet but creates a second problem, because only `durationMs`
        # is in `_EPHEMERAL_META_FIELDS`
        # (tools/qou-substrate/python/qou_substrate/witness.py). A `durationSec`
        # is therefore compared as SUBSTANTIVE content, so every re-run of this
        # probe reports drift on a wall-clock number that means nothing. Integer
        # `durationMs` is the WitnessBuilder convention (55 producers vs 2) and
        # is masked.
        "durationMs": int((time.monotonic() - t0) * 1000),
    }

    out = HERE / "qbeta-kc21-parity-convention-immunity.witness.json"
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n  verdict: {witness['result']['verdict']}")
    print(f"  witness -> {out.relative_to(ROOT)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
