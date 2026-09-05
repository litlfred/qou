import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)
#!/usr/bin/env python3
"""qou-cds1 branch 3: tau_0 is NOT a CM point, and the jet tower is BLIND to decay.

Two owner-directed questions, both answered negative, both with a proof rather
than a measurement.

======================================================================
PART 1 -- Riera-Rodriguez Theorem 2, decoded by DERIVATION
======================================================================

Step 20 left tau_0 unrecovered: the paper pins it modulo Gamma_0(5) by the pair
j(tau_0), j(5*tau_0), and the library scan garbles the second as "- 293x5" with a
stray "25" on the next line. The owner's judgement was that tau_0, being a
PERIOD-MATRIX parameter rather than Serre's isogeny factor, might be a CM point
where Serre's E is not.

No clean scan was needed. Given j(tau_0) = -25/2, the possible j(5*tau_0) are
exactly the six roots of the modular polynomial Phi_5(-25/2, Y) -- computable as
j(5*tau) and j((tau+k)/5), k = 0..4. Computing them independently gives

    j(5*tau)        -5430596809089.6955      (real, non-integral)
    j((tau+0)/5)     2.8951e10 + 2.2630e11 i
    j((tau+1)/5)    -9126.3809 + 6879.5966 i
    j((tau+2)/5)    -3810.78125              (real, EXACT)
    j((tau+3)/5)    -9126.3809 - 6879.5966 i
    j((tau+4)/5)     2.8951e10 - 2.2630e11 i

and -3810.78125 is EXACTLY -5*29^3/2^5 = -121945/32. So the OCR fragment is
"-29^3 * 5" over "2^5", the exponent having been rendered onto its own line. The
derivation supplies the value; the scan only selects among six candidates.

    THEOREM 2:   j(tau_0) = -5^2/2 = -25/2,    j(5 tau_0) = -5*29^3/2^5

*** AND THE ANSWER TO THE QUESTION IS NO. *** Both invariants are non-integral
rationals: v_2(j(tau_0)) = -1 and v_2(j(5 tau_0)) = -5. A CM j-invariant is an
ALGEBRAIC INTEGER (a rational integer over Q). Negative 2-adic valuation means
potentially MULTIPLICATIVE reduction at 2 -- Tate curves -- which is exactly what
CM forbids (CM => integral j => potentially GOOD reduction everywhere). So tau_0
has no complex multiplication, no closed form, and supplies no derived phase. The
hypothesis is refuted, and branch 3 is out of NAMED candidates.

======================================================================
PART 2 -- the Grobner-Shirshov jet tower is blind to the decay channel
======================================================================

Owner: "make sure you're working on the jet tower. Phase may be hidden there."
It cannot be, and the reason is an exact symmetry.

The tower's channel weights are w_mu(k) = Sum_{lam |- k} W_lam * mult_mu(lam|H_3)
with the q-Plancherel weight W_lam = d_q(lam)^2/[k]_q! and
d_q(lam) = [k]_q!/Prod_cells [h(c)]_q, so

    W_lam = [k]_q! / (Prod_cells [h(c)]_q)^2

depends on lam ONLY through its MULTISET OF HOOK LENGTHS. Transposing a Young
diagram permutes that multiset, so W_{lam'} = W_lam for every lam and every q,
while transposition swaps the trivial and sign branchings. Since lam -> lam' is
an involution of the partitions of k, reindexing gives

    w_sym(k) = w_alt(k)   EXACTLY, for every k and every q.

VERIFIED HERE: hook-multiset invariance under transpose has ZERO counterexamples
over every partition of every k <= 9, and w_sym(k) - w_alt(k) is 0 at 40 dps for
k = 3..9 (exactly 0.0 for k = 3,4,5; <= 7.3e-40 above, i.e. working-precision
roundoff).

WHY THAT ANSWERS IT. The two channels enter the two sectors with OPPOSITE signs:
mass sees y_3 + y_(1^3), decay sees y_3 - y_(1^3) (this bean, Step 9). So the
tower's contribution to the DECAY combination is w_sym - w_alt = 0, identically,
at every level. No phase can hide in the tower because the tower contributes
NOTHING AT ALL to the channel that needs one.

This does not touch the mass sector, where w_sym + w_alt = 2*w_sym is exactly
what the tower's unbounded ~2.5x/level growth feeds
(`wlambda_jet_tower_connected_probe`, whose numbers show the same equality in its
own normalisation: w_sym and w_alt agree to all 8 printed digits at every level).

======================================================================
WHAT IS LEAN-PROVED VS NUMERICALLY CHECKED -- stated so nobody over-reads it
======================================================================

LEAN, sorry-free, axioms [propext, Classical.choice, Quot.sound]:
  * `bring_j_five_tau_zero`             -5*29^3/2^5 = -121945/32
  * `bring_serre_j_invariant`           j from Serre's equation is -25/2
  * `bring_j_five_tau_zero_not_integral`, `not_cm_j_invariant`   neither is an
    integer, hence neither is a CM invariant
  * `sum_eq_of_involution`, `decay_combination_zero`   the reindexing that makes
    the tower blind, stated abstractly so it carries the argument without
    formalising Young diagrams

NUMERICAL, not Lean:
  * that -3810.78125 is among the six roots of Phi_5(-25/2, Y) (root-finding on
    Klein's j)
  * hook-multiset invariance under transpose (a standard combinatorial fact;
    checked exhaustively for k <= 9, not formalised -- Young diagrams and hooks
    are heavy in Lean and the payoff is a known theorem)
  * w_sym(k) = w_alt(k) at 40 dps

So the MECHANISM is proved and the two facts it consumes are checked. That is the
honest division.

SCOPE. Scope-(b) for both exclusions. Nothing derived, proposed, wired or
readmitted; no convention adjudicated. Anchor: experimental (proton) pin.
"""

import json
import os
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate")]
import _path_bridge  # noqa: E402, F401

from q_parameter import q_at  # noqa: E402

mp.mp.dps = 40
Q0 = q_at(mp.mp.dps)
J_TAU0 = Fraction(-25, 2)
J_5TAU0 = Fraction(-5 * 29 ** 3, 32)


def v2(fr: Fraction) -> int:
    n, d, v = fr.numerator, fr.denominator, 0
    while d % 2 == 0:
        d //= 2
        v -= 1
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for i in range(min(n, mx), 0, -1):
        for r in parts(n - i, i):
            yield (i,) + r


def transpose(l):
    return tuple(sum(1 for x in l if x > j) for j in range(l[0])) if l else ()


def hooks(l):
    lt = transpose(l)
    return sorted(l[i] - j - 1 + lt[j] - i - 1 + 1
                  for i in range(len(l)) for j in range(l[i]))


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" branch 3 closure: tau_0 is not CM, and the jet tower is blind to decay")
    print("=" * 78)

    # ---- PART 1 --------------------------------------------------------
    j0 = mp.mpf(J_TAU0.numerator) / J_TAU0.denominator
    y0 = mp.findroot(lambda y: 1728 * mp.kleinj(mp.mpc(mp.mpf(1) / 2, y)) - j0,
                     mp.mpf("0.9"))
    tau = mp.mpc(mp.mpf(1) / 2, y0.real)
    roots = [("j(5*tau)", 1728 * mp.kleinj(5 * tau))] + \
            [(f"j((tau+{k})/5)", 1728 * mp.kleinj((tau + k) / 5)) for k in range(5)]
    target = mp.mpf(J_5TAU0.numerator) / J_5TAU0.denominator
    print(f"\n[1] the six roots of Phi_5(-25/2, Y)  (tau = 1/2 + {mp.nstr(tau.imag, 12)} i)")
    hit = None
    for nm, v in roots:
        real = mp.fabs(v.imag) < mp.mpf("1e-20")
        m = real and mp.fabs(v.real - target) < mp.mpf("1e-25")
        if m:
            hit = nm
        print(f"    {nm:16s} {mp.nstr(v, 20):>44s}{'   <== -5*29^3/2^5' if m else ''}")
    print(f"\n    -5*29^3/2^5 = {J_5TAU0} = {mp.nstr(target, 14)}"
          f"   found as {hit}")
    print(f"    THEOREM 2:  j(tau_0) = {J_TAU0} = -5^2/2 ,  j(5 tau_0) = {J_5TAU0} = -5*29^3/2^5")
    print(f"\n    v_2(j(tau_0))  = {v2(J_TAU0)}      integral? {J_TAU0.denominator == 1}")
    print(f"    v_2(j(5tau_0)) = {v2(J_5TAU0)}      integral? {J_5TAU0.denominator == 1}")
    print(f"    => potentially MULTIPLICATIVE reduction at 2 (Tate curves), which CM forbids")
    print(f"    => tau_0 is NOT a CM point. The hypothesis is refuted.")

    # ---- PART 2 --------------------------------------------------------
    qint = lambda n: (Q0 ** n - 1) / (Q0 - 1)  # noqa: E731

    def W(l, k):
        fac = mp.mpf(1)
        for n in range(1, k + 1):
            fac *= qint(n)
        pr = mp.mpf(1)
        for h in hooks(l):
            pr *= qint(h)
        return fac / pr ** 2

    def mult(l, mu):
        if sum(l) == 3:
            return 1 if l == mu else 0
        tot = 0
        for i in range(len(l)):
            if i == len(l) - 1 or l[i] > l[i + 1]:
                sub = list(l)
                sub[i] -= 1
                tot += mult(tuple(x for x in sub if x > 0), mu)
        return tot

    bad = [l for k in range(1, 10) for l in parts(k) if hooks(l) != hooks(transpose(l))]
    print(f"\n[2] hook-multiset invariance under transpose, all partitions k <= 9")
    print(f"    counterexamples: {len(bad)}   => W_lambda = W_lambda' for EVERY q")
    print(f"\n    {'k':>3s}{'w_sym':>22s}{'w_alt':>22s}{'|w_sym - w_alt|':>18s}")
    worst = mp.mpf(0)
    rows = {}
    for k in range(3, 10):
        ws = sum(W(l, k) * mult(l, (3,)) for l in parts(k))
        wa = sum(W(l, k) * mult(l, (1, 1, 1)) for l in parts(k))
        d = mp.fabs(ws - wa)
        worst = max(worst, d)
        rows[k] = (ws, wa, d)
        print(f"    {k:>3d}{mp.nstr(ws, 16):>22s}{mp.nstr(wa, 16):>22s}{mp.nstr(d, 6):>18s}")
    print(f"\n    worst |w_sym - w_alt| = {mp.nstr(worst, 6)}  (working-precision roundoff)")
    print(f"    mass sees y_3 + y_(1^3); decay sees y_3 - y_(1^3).")
    print(f"    => the tower's DECAY contribution w_sym - w_alt is IDENTICALLY ZERO.")
    print(f"       No phase can hide there: the tower contributes nothing to that channel.")

    a = [
        {"name": "j_five_tau_zero_is_minus_5_times_29_cubed_over_32",
         "passed": bool(hit is not None),
         "detail": f"-5*29^3/2^5 = {J_5TAU0} appears among the six roots of Phi_5(-25/2,Y) as "
                   f"{hit}, decoding the OCR fragment '- 293x5' with its '2^5' exponent "
                   "OCR'd onto the next line — derived, with the scan only selecting"},
        {"name": "neither_theorem_2_invariant_is_integral",
         "passed": bool(J_TAU0.denominator != 1 and J_5TAU0.denominator != 1),
         "detail": f"v_2 = {v2(J_TAU0)} and {v2(J_5TAU0)}; a CM j-invariant is an algebraic "
                   "integer, so negative 2-adic valuation (potentially multiplicative "
                   "reduction, Tate curves) rules CM out"},
        {"name": "tau_zero_is_not_a_CM_point",
         "passed": bool(J_TAU0.denominator != 1 and J_5TAU0.denominator != 1),
         "detail": "the owner's hypothesis — that tau_0, a period-matrix parameter, might "
                   "be CM where Serre's isogeny factor is not — is REFUTED. tau_0 has no "
                   "closed form and supplies no derived phase"},
        {"name": "hook_multiset_is_transpose_invariant",
         "passed": bool(len(bad) == 0),
         "detail": f"zero counterexamples over every partition of every k <= 9, so the "
                   "q-Plancherel weight W_lambda = [k]_q!/(prod [h]_q)^2 satisfies "
                   "W_lambda' = W_lambda for every q"},
        {"name": "jet_tower_sym_and_alt_weights_are_equal",
         "passed": bool(worst < mp.mpf("1e-35")),
         "detail": f"worst |w_sym - w_alt| over k=3..9 is {mp.nstr(worst, 6)} at 40 dps "
                   "(exactly 0 for k=3,4,5) — the equality is exact, the residue is roundoff"},
        {"name": "jet_tower_contributes_nothing_to_the_decay_channel",
         "passed": bool(worst < mp.mpf("1e-35")),
         "detail": "mass sees y_3 + y_(1^3), decay sees y_3 - y_(1^3); w_sym - w_alt = 0 "
                   "identically at every level, so no phase can hide in the tower "
                   "(Lean decay_combination_zero)"},
    ]
    all_passed = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {all_passed}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-bring-tau0-and-jet-tower-closure",
        "engine": "mpmath",
        "description": (
            "qou-cds1 branch 3, two owner-directed questions, both negative. (1) "
            "Riera-Rodriguez Theorem 2 decoded by DERIVATION rather than by a clean scan: "
            "given j(tau_0) = -25/2 the possible j(5 tau_0) are the six roots of "
            "Phi_5(-25/2,Y), computed here, and -3810.78125 = -5*29^3/2^5 = -121945/32 is "
            "among them, matching the garbled OCR '- 293x5' with its 2^5 exponent on the "
            "next line. Both invariants are NON-INTEGRAL rationals (v_2 = -1 and -5), i.e. "
            "potentially multiplicative reduction at 2, which CM forbids -- so tau_0 is NOT "
            "a CM point and the hypothesis that it might be where Serre's E is not is "
            "REFUTED. (2) The Grobner-Shirshov jet tower is BLIND to the decay channel: the "
            "q-Plancherel weight depends on a partition only through its hook multiset, "
            "which transpose permutes, and transpose swaps the trivial and sign branchings, "
            "so w_sym(k) = w_alt(k) exactly at every k and every q (verified: zero "
            "counterexamples to hook invariance for k <= 9; |w_sym - w_alt| <= 7.3e-40 at "
            "40 dps). Mass sees y_3 + y_(1^3) and decay sees y_3 - y_(1^3), so the tower "
            "contributes IDENTICALLY ZERO to decay -- no phase can hide there. Lean: "
            "BringEllipticCurveJInvariant.lean and JetTowerBlindToDecay.lean, sorry-free."),
        "contentBlock": "conj:im-q-physical-role",
        "assertions": a,
        "allPassed": all_passed,
        "parameters": {
            "pin": "experimental (proton), per the 2026-08-07 owner directive",
            "dps": 40,
            "source": ("library/pjm-v154-n1-p09-s — Riera & Rodriguez, The period matrix "
                       "of Bring's curve, Pacific J. Math. 154 (1992) 179-200"),
            "lean": ["QOU/QBeta/BringEllipticCurveJInvariant.lean",
                     "QOU/QBeta/JetTowerBlindToDecay.lean"],
            "lean_vs_numeric": (
                "LEAN: the two j-values as rational identities, their non-integrality, and "
                "the involution reindexing that makes the tower blind. NUMERIC: that "
                "-3810.78125 is among the six Phi_5 roots; hook-multiset transpose "
                "invariance (standard, checked exhaustively k<=9, not formalised); "
                "w_sym = w_alt at 40 dps."),
        },
        "data": {
            "q0": mp.nstr(Q0, 20),
            "tau_re": "1/2", "tau_im": mp.nstr(tau.imag, 16),
            "j_tau0": str(J_TAU0), "j_tau0_closed": "-5^2/2", "v2_j_tau0": v2(J_TAU0),
            "j_5tau0": str(J_5TAU0), "j_5tau0_closed": "-5*29^3/2^5",
            "v2_j_5tau0": v2(J_5TAU0),
            "phi5_roots": {nm: mp.nstr(v, 20) for nm, v in roots},
            "matched_root": hit,
            "hook_transpose_counterexamples": len(bad),
            "tower_weights": {str(k): {"w_sym": mp.nstr(v[0], 16),
                                       "w_alt": mp.nstr(v[1], 16),
                                       "abs_diff": mp.nstr(v[2], 8)}
                              for k, v in rows.items()},
            "worst_sym_alt_diff": mp.nstr(worst, 8),
        },
        "context": {
            "axis": "branch 3: is tau_0 CM? can the jet tower hide the phase?",
            "answer": (
                "No and no. tau_0's two j-invariants are non-integral rationals (Tate "
                "curves at 2), so no CM and no closed form. The jet tower's sym and alt "
                "weights are exactly equal at every level by hook-multiset transpose "
                "invariance, so its contribution to the decay combination y_3 - y_(1^3) "
                "vanishes identically -- it contributes nothing to the channel that needs "
                "a phase."),
            "consequence": (
                "branch 3 is out of NAMED candidates: the braid image is excluded, "
                "arbitrary M is circular, constant-residue holonomies fail the doubling "
                "identity, all real-spectrum generators are on the wrong side of 1, Im(q) "
                "cannot supply ellipticity, Bring's E is non-CM, tau_0 is non-CM, and the "
                "jet tower is blind. What remains is unnamed."),
            "scope": ("Scope-(b) for both exclusions. Nothing derived, proposed, wired or "
                      "readmitted; no convention adjudicated."),
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out = HERE / "qbeta-bring-tau0-and-jet-tower-closure.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton", q0_value=mp.nstr(Q0, 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
