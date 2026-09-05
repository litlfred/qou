#!/usr/bin/env python3
"""alpha_em_reality_consistency_probe.py

Bean qou-tq20 (B2 lift), fourth tranche: the FIRST NUMERICAL CONSISTENCY
CHECK of the Reality-realization premise (the wall's final form, #3999):

  "the alpha_EM loop weight operator on H^1(Bring) is real self-adjoint,
   swap-conjugation-commuting, with H^{1,0}-block equal to the tau-image of
   the canonical Markov channel weight."

The lift-from-reality constructor (#3999) makes the reality half free; the
open half is the tau-IDENTIFICATION of the Markov channel weight with a
geometric (Laplacian/period-derived) operator. This probe compares the two
sides' FIRST comparable invariant — the channel/isotypic multiplicity
structure at the decategorification point:

  CATEGORICAL side (exact, corpus canonical y_lambda_at):
    Markov channel weights at n=2, q=1: (y_[2], y_[1,1]) = (3/4, 1/4)
    => channel dimension vector 4*(y) = (3, 1).
  GEOMETRIC side (exact, Braden-Disney-Hogg Thm 2.12 / Prop 4.6):
    tau_B = tau_0 * M with the principal polarization
    M = [[4,1,-1,1],[1,4,1,-1],[-1,1,4,1],[1,-1,1,4]]:
    spec(M) = {1, 5, 5, 5}, det = 125 — the Jacobian is isogenous to
    E_{5 tau_0}^3 x E_{tau_0}: ISOTYPIC dimension vector (3, 1).

  CONSISTENCY: (3,1) = (3,1) — the tau-image of the canonical Markov
  channel weight at q=1 has EXACTLY the isotypic dimension structure of
  H^{1,0}(Bring)'s canonical splitting.

HONEST SCOPE (STRICT): this is CONSISTENCY, not a derivation — a (3,1)
split of a 4-dim space carries limited entropy (the match could not have
failed in many ways), so it cannot upgrade any tier. Its value: (a) the
identification SURVIVES its first contact with the exact period data; (b)
it produces the next FALSIFIABLE comparison (V4): the identification
predicts the geometric side carries a q-DEFORMATION of the (3,1) weights
whose q=1 value is (3/4,1/4) — the general-q Markov ratio
y_[2]/y_[1,1](q) is recorded as the target the future period-side
computation must reproduce. The multiplier pair (5,1) in spec(M) is
RECORDED, NOT interpreted. No fit; nothing wired; 1/(8pi) stays phase-4.

Self-contained (sympy + corpus wedderburn_jones_markov).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_here))
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # V1: categorical side — canonical Markov channel weights at q=1
    y = y_lambda_at(2)
    y2, y11 = y[(2,)], y[(1, 1)]
    q = sorted(y2.free_symbols, key=str)[0]
    w_q1 = (sp.simplify(y2.subs(q, 1)), sp.simplify(y11.subs(q, 1)))
    dim_vec_cat = (4 * w_q1[0], 4 * w_q1[1])
    v1 = w_q1 == (sp.Rational(3, 4), sp.Rational(1, 4)) and dim_vec_cat == (3, 1)
    check("categorical_channel_dims", v1,
          f"canonical Markov weights at q=1: {w_q1} => channel dimension vector "
          f"4·y = {dim_vec_cat} — the Schur-Weyl (3,1) split of the 4-dim space")

    # V2: geometric side — exact polarization M (Braden-Disney-Hogg Thm 2.12)
    M = sp.Matrix([[4, 1, -1, 1], [1, 4, 1, -1], [-1, 1, 4, 1], [1, -1, 1, 4]])
    ev = M.eigenvals()  # {eigenvalue: multiplicity}
    spec_ok = ev == {sp.Integer(5): 3, sp.Integer(1): 1}
    det_ok = M.det() == 125 and M.trace() == 16
    sym_ok = M.T == M
    dim_vec_geo = (3, 1)  # multiplicities of {5, 1}
    v2 = spec_ok and det_ok and sym_ok
    check("geometric_isotypic_dims", v2,
          "principal polarization M (tau_B = tau_0·M): symmetric, det=125, trace=16, "
          f"spec = {{5:3, 1:1}} — Jac(Bring) ~ E_{{5τ₀}}³ × E_{{τ₀}}: isotypic dimension "
          f"vector {dim_vec_geo}")

    # V3: the consistency match
    v3 = dim_vec_cat == dim_vec_geo
    check("channel_isotypic_match", v3,
          f"categorical channel dims {dim_vec_cat} = geometric isotypic dims {dim_vec_geo} "
          "— the tau-image of the canonical Markov channel weight at the decategorification "
          "point has EXACTLY the isotypic structure of H^{1,0}(Bring)'s canonical splitting. "
          "CONSISTENCY only (a (3,1) split of 4 is low-entropy); the identification survives "
          "its first contact with the exact period data")

    # V4: the next falsifiable target — the q-deformed weight ratio the geometric
    #     side must reproduce if the identification is right
    ratio_sym = sp.simplify(y2 / y11)
    ratio_q1 = sp.simplify(ratio_sym.subs(q, 1))
    ratio_q2 = sp.nsimplify(sp.simplify(ratio_sym.subs(q, 2)))
    v4 = ratio_q1 == 3 and sp.simplify(sp.diff(ratio_sym, q)) != 0
    check("next_falsifiable_target_recorded", v4,
          f"Markov weight ratio y_[2]/y_[1,1]: = 3 exactly at q=1 (matching dim ratio 3/1), "
          f"q-DEPENDENT away from it (e.g. {ratio_q2} at q=2) — the identification predicts "
          "the geometric side carries a q-deformation of the (3,1) weights with this exact "
          "ratio function; the period-side computation of that deformation is the next "
          "falsifiable comparison. The multiplier pair (5,1) in spec(M) is RECORDED, not "
          "interpreted")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "REALITY-REALIZATION CONSISTENCY CHECK 1 PASSES (scope-(a); consistency, NOT a "
        "derivation; no fit; nothing wired): the canonical Markov channel weight at the "
        "decategorification point — dims 4·(3/4,1/4) = (3,1) — matches EXACTLY the isotypic "
        "dimension structure of Jac(Bring) ≅ E_{5τ₀}³ × E_{τ₀} (spec(M) = {5:3, 1:1}, "
        "det 125, Thm 2.12 exact). The tau-identification survives its first contact with "
        "the period data. Low-entropy caveat: a (3,1) split of 4 could not have failed many "
        "ways — no tier change. NEXT falsifiable target recorded: the q-deformed weight "
        "ratio y_[2]/y_[1,1](q) (=3 at q=1) that the geometric side must reproduce. The "
        "wall (the tau-identification itself) remains OPEN."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-reality-consistency",
        "description": "Bean qou-tq20 tranche 4: first numerical consistency check of the "
                       "Reality-realization premise (#3999). Categorical Markov channel dims at "
                       "q=1 (3,1) match the isotypic dims of Jac(Bring) ~ E_{5t0}^3 x E_{t0} "
                       "(spec(M)={5:3,1:1}, det 125) exactly. Consistency only (low entropy); "
                       "next falsifiable target recorded (q-deformed weight ratio). Wall (the "
                       "tau-identification) remains open. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-reality-consistency.md",
        "tier": "symbolic-exact consistency check (corpus y_lambda_at + exact Thm 2.12 "
                "polarization); NOT a derivation",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "categorical_dims": "(3, 1) = 4·(3/4, 1/4) — Markov weights at q=1",
            "geometric_dims": "(3, 1) — isotypic multiplicities of spec(M) = {5:3, 1:1}",
            "match": "exact; consistency only (low-entropy caveat)",
            "next_target": "q-deformed weight ratio y_[2]/y_[1,1](q), = 3 at q=1",
            "recorded_not_interpreted": "multiplier pair (5,1) in spec(M)",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-tq20 (B2 lift) tranche 4; #3985 interface, #3992 C-model, #3999 "
                    "constructor merged",
            "premise_checked": "Reality realization — H^{1,0}-block = tau-image of the "
                               "canonical Markov channel weight",
            "scope_guard": "consistency, not derivation; no fit; nothing wired; 1/(8pi) stays "
                           "phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-reality-consistency.witness.json")
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
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
