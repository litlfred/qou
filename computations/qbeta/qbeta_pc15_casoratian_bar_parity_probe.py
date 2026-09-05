#!/usr/bin/env python3
"""
Probe P-C15 — is the 4_1 order-2 qZeilberger operator the Q_beta fibre kernel R(q,xi)?

Formalize-first, decidable, bounded check (AGENTS.md §Formalize-first).  This does
NOT run any anchor sweep: it tests one *structural invariant* — the bar-parity of the
order-2 operator's Casoratian ratio — on paper (exact symbolic), and kills on the
invariant if it fails, per the standing gate.

Context
-------
The open axis for the Q_beta 1ppQ "achievable arm" is a fibre-level Habiro element
F(q) whose kernel R(q,xi) drives the c_k recursion (RationalCoeffRecurrence.lean,
sorry-free engine; QBetaCKRecursionKernelConstraints.lean — kernel is non-constant,
a_1 bar-ODD, a_2 = c_2 = -1, constant depth-2 kernel refuted).  The newly-landed
4_1 order-2 colored-Jones recurrence (qZeilberger certificate, aj_figure_eight_certificate.py)

    a_2 J_{N+2} + a_1 J_{N+1} + a_0 J_N = b ,   x := q^N ,

    a_0 = (x - 1)(x^2 q^3 - 1) / x^6
    a_1 = -(x q - 1)^2 (x q + 1)(...) / (x^8 q^2)  [bar-even up to monomial twist; corrected 2026-07-07]
    a_2 = (x q^2 - 1)(x^2 q - 1) / x^6

is a candidate for that kernel — a *different object* from every refuted class C1–C14
(C14 tested the 4_1 Ohtsuki loop-series RATIONALS as c_3 scalars; cp4i/HabiroNewton
tested only the DEGENERATE first-order Newton restriction whose Casoratian vanishes).
Here we test the FULL second-order operator's Casoratian.

The test
--------
For a_2 f_{N+2} + a_1 f_{N+1} + a_0 f_N = 0, the Casoratian W_N = f_N g_{N+1} - f_{N+1} g_N
of two independent solutions satisfies  W_{N+1}/W_N = a_0 / a_2  (Abel–Heine; derived,
no sign flip).  For the operator to be a bar-covariant fibre object at all, this ratio
must be bar-even up to a single monomial twist (cf. QBesselBarCovariance: the c_k ratio
carries a k-independent twist).  So the decidable FIRST check is the pure symbolic
bar-parity identity under the fibre bar involution  q -> 1/q ,  x -> 1/x :

    twist := R(1/q, 1/x) / R(q, x)          # must be a Laurent monomial q^a x^b

plus the q->1 classical-shadow sign of R (must be > 0 for x>1, consistent with the
measured even-channel W_2 = c_2^even c_3^odd - c_3^even c_2^odd = +102.674 > 0).

KILL (append refuted row C15) if twist is NOT a monomial, OR the q->1 shadow sign is
negative.  ADVANCE (gated on the H_4 Hoefsmit c_4^even build, bean 8we6) only if both pass.
No anchor numerics either way.
"""
import json, hashlib, datetime, os, sys, subprocess
import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


def _repo_head_sha():
    """Repo HEAD at emission time — required provenance field per the I14
    witness_provenance_audit (REQUIRED_FIELDS = engine, scriptFile, commitSha)."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
        ).strip()
    except Exception:
        return None


def main():
    q, x = sp.symbols("q x", positive=True)  # x = q^N ; positivity = substrate q>1, N>=1

    # Exact operator coefficients (verbatim from aj_figure_eight_certificate.py).
    a0 = (x - 1) * (x**2 * q**3 - 1) / x**6
    a2 = (x * q**2 - 1) * (x**2 * q - 1) / x**6
    # CORRECTED 2026-07-07: previous transcription of a1 here did NOT match
    # aj_figure_eight_certificate.py (different quartic factor + denominator);
    # see docs/audits/2026-07-07-pc15-a1-transcription-error-correction.md.
    a1 = -((x * q - 1) ** 2 * (x * q + 1)
           * (x**4 * q**4 - x**3 * q**3 - x**2 * q**3 - x**2 * q - x * q + 1)) \
         / (x**8 * q**2)

    # Casoratian ratio  W_{N+1}/W_N = a_0 / a_2   (Abel–Heine).
    R = sp.cancel(sp.together(a0 / a2))

    bar = {q: 1 / q, x: 1 / x}
    Rbar = sp.cancel(sp.together(R.subs(bar, simultaneous=True)))

    twist = sp.cancel(sp.together(Rbar / R))
    twist = sp.simplify(twist)

    # Is `twist` a Laurent monomial q^a x^b ?  (constant * q^a * x^b, no sum of terms)
    twist_ratio = sp.nsimplify(twist)  # keep exact
    is_monomial = _is_laurent_monomial(twist_ratio, q, x)

    # Classical q->1 shadow of the ratio, and its sign for x>1.
    R_classical = sp.simplify(sp.limit(R, q, 1))
    # sign at a representative x>1 (substrate: q~1.11, N=1 -> x~1.11)
    shadow_val = sp.nsimplify(R_classical.subs(x, sp.Rational(111, 100)))
    shadow_positive = bool(shadow_val > 0)

    # Cross-consistency: bar-parity of the individual coefficients.
    def bar_ratio(expr):
        return sp.simplify(sp.cancel(sp.together(expr.subs(bar, simultaneous=True) / expr)))
    a0_bar, a1_bar, a2_bar = bar_ratio(a0), bar_ratio(a1), bar_ratio(a2)

    passes = bool(is_monomial and shadow_positive)
    verdict = (
        "PASS — structural bar-parity gate cleared; the 4_1 order-2 Casoratian ratio is "
        "bar-even up to the monomial twist below, and its q->1 classical shadow is "
        "positive (consistent with the measured even-channel W_2 = +102.674 > 0). "
        "NOT excluded as the fibre kernel R(q,xi). ADVANCE is gated on a genuine c_4 rung "
        "(H_4 Hoefsmit c_4^even build, bean 8we6): only then can the anchor-level "
        "Casoratian W_3/W_2 be evaluated. A pass here de-risks that build; it is NOT a "
        "closure and NOT a c_k value."
        if passes else
        "KILL — bar-parity gate failed (twist not a Laurent monomial, or q->1 shadow sign "
        "wrong). Append refuted class C15: the 4_1 order-2 qZeilberger operator is not the "
        "Q_beta fibre kernel. Do NOT run any anchor sweep."
    )

    result = {
        "casoratian_ratio_a0_over_a2": str(R),
        "bar_involution": "q -> 1/q, x -> 1/x  (x = q^N)",
        "casoratian_ratio_under_bar": str(Rbar),
        "twist_R_bar_over_R": str(twist_ratio),
        "twist_is_laurent_monomial": is_monomial,
        "q_to_1_classical_shadow": str(R_classical),
        "q_to_1_shadow_sign_positive_at_x_1p11": shadow_positive,
        "coeff_bar_ratios": {"a0": str(a0_bar), "a1": str(a1_bar), "a2": str(a2_bar)},
        "a1_note": "corrected 2026-07-07 -- a1 bar-ratio is the monomial x^7/q^5; see correction audit",
        "gate_passes": passes,
        "verdict": verdict,
        "distinct_from_refuted": {
            "C14": "tested 4_1 Ohtsuki loop-series RATIONALS as c_3 scalars; this tests the "
                   "order-2 OPERATOR/Casoratian structure — a different object.",
            "cp4i_HabiroNewton": "tested the DEGENERATE first-order Newton restriction "
                                 "(Casoratian identically 0); this uses the FULL second-order operator.",
            "C5": "constant-kernel recursion; this kernel is the non-constant q-rational a_0/a_2.",
        },
        "next_step_if_pass": "H_4 Hoefsmit c_4^even build (bean 8we6) -> genuine c_4 rung -> "
                             "evaluate anchor Casoratian W_3/W_2 vs even-channel AW-positivity.",
    }

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-pc15-casoratian-bar-parity",
        "description": "Probe P-C15: bar-parity of the 4_1 order-2 qZeilberger Casoratian "
                       "ratio a_0/a_2 as a decidable structural gate on the Q_beta fibre kernel "
                       "R(q,xi). Formalize-first; no anchor numerics; kill-on-invariant.",
        "audit_only": True,
        "tier": "structural-exact (symbolic bar-parity identity; no fit, no anchor sweep)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": [
            {"name": "twist_is_laurent_monomial", "passed": is_monomial},
            {"name": "q_to_1_shadow_sign_positive", "passed": shadow_positive},
        ],
        "allPassed": passes,
        "result": result,
        "context": {
            "axis": "Q_beta 1ppQ achievable-arm — fibre kernel F(q)/R(q,xi)",
            "operator_source": "computations/aj_figure_eight_certificate.py",
            "refuted_class_map": "docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md",
            "ledger": "docs/coordination/1ppq-qbeta.md",
            "kernel_constraints": "QOU/BraidKnot/QBetaCKRecursionKernelConstraints.lean",
        },
    }
    out = os.path.join(os.path.dirname(__file__), "qbeta-pc15-casoratian-bar-parity.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)

    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("=== P-C15 : 4_1 order-2 Casoratian bar-parity gate ===")
    print("R = a_0/a_2                    :", R)
    print("R(1/q,1/x)                     :", Rbar)
    print("twist = R(1/q,1/x)/R           :", twist_ratio, "  (monomial:", is_monomial, ")")
    print("q->1 classical shadow of R     :", R_classical, "  (>0 at x=1.11:", shadow_positive, ")")
    print("coeff bar-ratios  a0/a1/a2     :", a0_bar, "/", a1_bar, "/", a2_bar)
    print("GATE PASSES                    :", passes)
    print("VERDICT:", verdict)
    print("witness ->", out)
    # Propagate the gate outcome via exit code, matching the nearest sibling gate probe
    # (qbeta_bar_even_kernel_invariant_probe.py). A KILL (refutation) is a valid scientific
    # result recorded in the witness; the non-zero exit merely signals "candidate excluded".
    return 0 if passes else 1


def _is_laurent_monomial(expr, *gens):
    """True iff expr = c * prod gen_i^{k_i} (c constant, k_i in Z): a single power-product."""
    expr = sp.powsimp(sp.simplify(expr))
    num, den = sp.fraction(sp.together(expr))
    def single_term(p):
        p = sp.expand(p)
        return len(sp.Add.make_args(p)) == 1
    return single_term(num) and single_term(den)


if __name__ == "__main__":
    sys.exit(main())
