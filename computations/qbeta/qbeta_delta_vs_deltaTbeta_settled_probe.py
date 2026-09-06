#!/usr/bin/env python3
"""qou-avt5 SETTLED: chi_block_* is VERIFIED; eps(Delta) is an asserted
polynomial with no exhibited element. Scope-(a).

SUPERSEDES `qbeta_delta_vs_deltaTbeta_discrepancy_probe.py`, whose "two
different q-deformations of one classical object" reading is WITHDRAWN.

WHAT THE EARLIER PROBE GOT RIGHT: chi_(3)(Delta_T_beta) != eps(Delta) at q0,
ratio 1.3909. Both sides were closed forms, so that measurement never touched
the buggy path below and it stands.

WHAT IT GOT WRONG: the reading. It is NOT two q-deformations. It is one
VERIFIED element against one ASSERTED polynomial.

--- SIDE B IS NOW VERIFIED --------------------------------------------------

The nucleon words ARE exhibited: `hecke_core._PROTON_G0/G1`, `_NEUTRON_G0/G1`,
as typed-crossing chains (c, d, gen) with d in {0, -h/2, -h}. Evaluating
chi_lambda on them through the d-PRESERVING path
(`chi_monotone_transfer.chi_all_lambda`) reproduces the "paper closed forms"
EXACTLY, all three blocks, at q0:

    lambda      chi(n)-chi(p) from the WORDS      chi_block (paper)     ratio
    (3)              -0.260387641790121      -0.260387641790121          1.0
    (2,1)            -0.106814457651578      -0.106814457651578          1.0
    (1,1,1)          -0.171538643776599      -0.171538643776599          1.0

So `Delta_T_beta` IS `beta_n - beta_p`, the paper forms are CORRECT, and side B
is closed. The `-- Ref: [hoefsmit1974]` transcription checks out.

--- SIDE A HAS NO ELEMENT ---------------------------------------------------

`eps(Delta)` is `QOU.Interactions.QBetaEnergyScale.epsNPq`, a BARE `def`:
a polynomial in q. No Hecke element is constructed anywhere; `Qbeta_closed` is
a ring identity between two closed forms. The content block
`qbeta-counit-closed-form.md` states the closed forms without a word and has NO
`.lean` sibling (`validation: "not_checked"`).

--- WHY THAT MAKES THEM DIFFERENT ELEMENTS, NOT DIFFERENT DEFORMATIONS -------

The Frobenius counit IS the one-dimensional rep sigma_i -> q, i.e. exactly the
lambda = (3) block. And Grobner-Shirshov normal form is a REWRITING to a
canonical representative of the SAME algebra element, so chi is invariant under
it: chi_(3)(NF(n) - NF(p)) = chi_(3)(beta_n - beta_p) necessarily.

Measured at q0:
    chi_(3)(beta_n - beta_p)  = -0.2603876417901208     <- the exhibited element
    epsNPq  ("eps(Delta)")    = -0.1872071945293783     <- the asserted def
    ratio                     =  1.390906169203         (eps/chi = 0.7189557586)

So `epsNPq` is NOT the counit of the exhibited nucleon-word difference. It is
the counit of some OTHER object -- plausibly the "single-wrap" / "N=0"
truncation its own prose names ("the single-wrap normal-form difference",
"the N=0 neutron-proton NF difference"), which is nowhere exhibited.

CONSEQUENCE, and it is why this is worth landing: `Q_A = -E_0 * eps(Delta)` is
built on `epsNPq`. So Q_A -- and therefore the entire Q_beta ladder, whose phase
is `eps - tr_M` -- rests on an ASSERTED polynomial, while the corpus's VERIFIED
element gives a different number at the same q0.

NOT CLAIMED: that either is wrong. A single-wrap truncation is a legitimate
object and may be the intended one. What IS established is that they are
different, that only one of them is exhibited, and that the corpus carries no
disambiguation row. Settling WHICH belongs in Q_A needs the single-wrap element
written down.

NOT MEASURED: the ratio's q-dependence. The words are q0-BAKED (their `d` are
literal -h(q0)/2, -h(q0)), and `word_to_mpfr` classifies `d` against h(q), so a
q-sweep raises rather than re-lifting. Every number here is at q0 only, and no
claim is made about the ratio as a function of q.

Exact mpmath at 50 dps. NO fit, NO c_k, NO wiring.
"""
import datetime, hashlib, json, os, subprocess, sys
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)
# `Path` was used below without ever being imported (bean qou-6inm's own fix,
# 957a8b0da4, 2026-08-31): this module has raised `NameError: name 'Path' is
# not defined` at import ever since, so the probe has not run in six days.
from pathlib import Path
# Repo-root-relative (bean qou-c7g8/qou-6inm). These were absolute paths into a
# DIFFERENT machine's checkout (/home/user/qou), which resolve to nothing in any
# clone not at that exact path. A sys.path insert of a missing directory raises
# NOTHING, so the failure was silent until an unrelated-looking import died.
_QOU_ROOT = Path(__file__).resolve().parents[2]
_COMP = _QOU_ROOT / "computations"
sys.path[:0] = [str(_COMP), str(_COMP / "hecke"), str(_COMP / "substrate")]
import mpmath as mp
mp.mp.dps = 50
from chi_monotone_transfer import chi_all_lambda
from closed_form_tau_M import compute_tau_M_nucleon_H3
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1
from q_parameter import Q as Q0
from q_parameter import Q_MP  # noqa: E402 — exact mpf, not the f64 twin


def _sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True).strip()
    except Exception:
        return None


def _word(g0, g1):
    return ([(mp.mpf(str(c)), mp.mpf(str(d)), 0) for c, d in g0]
            + [(mp.mpf(str(c)), mp.mpf(str(d)), 1) for c, d in g1])


def main():
    q = Q_MP; h = q - 1/q
    assertions = []

    def check(name, passed, note=""):
        assertions.append({"name": name, "passed": bool(passed), "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    cp = chi_all_lambda(_word(_PROTON_G0, _PROTON_G1), 3, dps=50, q=q)
    cn = chi_all_lambda(_word(_NEUTRON_G0, _NEUTRON_G1), 3, dps=50, q=q)

    # CALIBRATION against the FIXED producer -- mandatory here, because the
    # first attempt at this probe calibrated against the PRE-FIX version and
    # "matched exactly" while both were wrong by 15.3 % / 27.3 %.
    for nm, c in (("p", cp), ("n", cn)):
        mine = sum(y_lambda_wenzl_bridge_numeric(l, q, dps=50) * c.get(tuple(l), mp.mpf(0))
                   for l in [(3,), (2, 1), (1, 1, 1)])
        check(f"calibrates_against_fixed_compute_tau_M_nucleon_H3_{nm}",
              abs(compute_tau_M_nucleon_H3(nm, q, dps=50) - mine) < mp.mpf("1e-40"))
    # and pin that it is the POST-fix value, not the pre-fix one
    check("post_fix_tau_p_not_the_pre_fix_value",
          abs(compute_tau_M_nucleon_H3("p", q, dps=50) - mp.mpf("1.14575969245730087")) < mp.mpf("1e-15"))

    paper = {(3,): -(q**2 - 1)*(q**2 + 1)**2/(4*q),
             (2, 1): (q**2 - 1)*(-(q**4) - 1)/(4*q**3),
             (1, 1, 1): -(q**2 - 1)*(q**2 + 1)**2/(4*q**5)}
    rows = []
    for k in [(3,), (2, 1), (1, 1, 1)]:
        d = cn.get(k, mp.mpf(0)) - cp.get(k, mp.mpf(0))
        rows.append({"lambda": str(k), "from_words": mp.nstr(d, 30),
                     "paper_closed_form": mp.nstr(paper[k], 30)})
        check(f"paper_closed_form_reproduced_from_words_{k}",
              abs(d - paper[k]) < mp.mpf("1e-40"))

    d3 = cn[(3,)] - cp[(3,)]
    eps = h**2/2 - h
    check("epsNPq_does_NOT_equal_chi_3_of_the_exhibited_element",
          abs(eps - d3) > mp.mpf("1e-3"),
          f"(ratio {mp.nstr(eps/d3, 12)})")

    verdict = (
        "SETTLED (scope-(a)). Side B is VERIFIED: chi_block_* reproduces "
        "chi_lambda(beta_n - beta_p) from the EXHIBITED nucleon words exactly, "
        "all three blocks at q0, so Delta_T_beta = beta_n - beta_p and the paper "
        "forms are correct. Side A has NO ELEMENT: epsNPq is a bare Lean def, a "
        "polynomial in q, with no Hecke element constructed anywhere. Since the "
        "counit IS the lambda=(3) block and GS normal form is a character-"
        "invariant rewriting of the SAME element, epsNPq is therefore NOT the "
        "counit of the exhibited difference -- it is the counit of some other, "
        "never-exhibited object, plausibly the 'single-wrap'/'N=0' truncation "
        "its own prose names. Q_A = -E_0*eps(Delta), and hence the whole Q_beta "
        "ladder whose phase is eps - tr_M, rests on that asserted polynomial. "
        "NOT claimed: that either is wrong. Settling which belongs in Q_A needs "
        "the single-wrap element written down. The earlier probe's 'two "
        "q-deformations' reading is WITHDRAWN."
        if all(a["passed"] for a in assertions) else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")

    src = open(__file__, "rb").read()
    w = {"computation": "qbeta-delta-vs-deltaTbeta-settled",
         "description": "chi_block_* verified against the exhibited nucleon "
                        "words; eps(Delta) is an asserted polynomial with no "
                        "element, and differs from chi_(3) of that element.",
         "engine": "mpmath", "markov_convention": "D",
         "assertions": assertions,
         "data": {"per_block": rows,
                  "chi_3_of_exhibited_element": mp.nstr(d3, 30),
                  "epsNPq_asserted": mp.nstr(eps, 30),
                  "ratio_eps_over_chi3": mp.nstr(eps/d3, 30),
                  "q0_baked_words_no_q_sweep": True},
         "verdict": verdict,
         "witness": {"scriptPath": "computations/qbeta/" + os.path.basename(__file__),
                     "scriptHash": hashlib.sha256(src).hexdigest()[:12],
                     "commitSha": _sha(),
                     "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat()}}
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qbeta-delta-vs-deltaTbeta-settled.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
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
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        w.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            w, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(w, f, indent=2); f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n{verdict}\n\nWitness: {os.path.basename(out)}")
    return 0 if all(a["passed"] for a in assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
