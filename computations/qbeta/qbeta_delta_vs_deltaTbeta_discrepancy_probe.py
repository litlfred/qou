#!/usr/bin/env python3
"""🛑 SUPERSEDED 2026-08-26 by `qbeta_delta_vs_deltaTbeta_settled_probe.py`.

The MEASUREMENT below stands (chi_(3)(Delta_T_beta)/eps(Delta) -> 1 as q -> 1,
1.3909 at q0; both sides are closed forms, so nothing here was affected by the
`d`-dropping defect fixed on main in e5deb145c).

The READING is WITHDRAWN. This file calls it "two different q-deformations of
one classical object". It is not. Side B is now VERIFIED against the EXHIBITED
nucleon words (chi_block_* reproduces chi_lambda(beta_n - beta_p) exactly, all
three blocks), while side A -- eps(Delta) = epsNPq -- is a BARE Lean `def` with
no Hecke element constructed anywhere. Since the counit IS the lambda=(3) block
and GS normal form is a character-invariant rewriting of the SAME element,
epsNPq is simply not the counit of the exhibited difference.

Read the settled probe instead. Kept for the measurement and the record.
"""

_HISTORICAL_DOC = """FLAG (superseded): two objects called "the neutron-minus-proton element of H_3(q)" differ
by 39% at the substrate, and the corpus carries no disambiguation row.

NOT A BUG REPORT. This probe MEASURES a discrepancy; it does NOT determine which
object is intended, and it must not be cited as showing either one wrong.

THE TWO OBJECTS.

  (A) Delta = NF(n) - NF(p), the GROBNER-SHIRSHOV NORMAL FORM difference.
      nuclear-interactions/qbeta-counit-closed-form.md derives
          eps(Delta)  = h^2/2 - h        tr_M(Delta) = h^2/2 - h*z
      and qou-cds1 verified eps(Delta)*E_0 reproduces the committed Q_A closed
      form exactly. This is the object the ladder's phase is built from
      (eps - tr_M = h(z-1) = 2*alpha).

  (B) Delta_T_beta, whose per-block characters chi_(3)/chi_(2,1)/chi_(1,1,1)
      are the hand-derived closed forms in qbeta_utils.py and in Lean
      (QBetaPerBlockChiClosedForms, -- Ref: [hoefsmit1974]). Their source
      witness qbeta-per-block-paper-closed-forms describes them as
      chi_lambda(BETA_n - BETA_p) -- the RAW BRAID difference, not the normal
      form.

THE TEST. The counit eps is the one-dimensional representation sigma_i -> q,
which is exactly the lambda = (n) block. So for ONE AND THE SAME element X,
chi_(3)(X) = eps(X) identically -- a 1-dim rep's character IS its value. Hence
chi_(3)(Delta_T_beta) / eps(Delta) = 1 iff the two elements agree.

MEASURED (mpmath 50 dps):

    q            chi_(3)/eps
    1+1e-2       1.030454535251763
    1+1e-4       1.000300045004500
    1+1e-8       1.000000030000000
    q -> 1       1               (exact limit)
    q0           1.39090616920312        <- 39% at the substrate

So they AGREE CLASSICALLY and DIVERGE AT THE SUBSTRATE. Both are also linear in
hbar_q at leading order (each -> -2*hbar_q as q -> 1), which is why the
divergence was not visible to a leading-order check.

WHY THIS IS WORTH A FLAG RATHER THAN A SHRUG. Agreeing at q=1 and differing at
q0 is exactly what TWO DIFFERENT q-DEFORMATIONS OF ONE CLASSICAL OBJECT look
like -- a real and common phenomenon, not automatically an error. But the corpus
carries NO registry section-2 disambiguation row for these two, and nothing in
docs/, content/ or computations/ states that they differ. AGENTS.md names this
exact class ("distinct objects sharing a glyph is a recurring root cause"), and
registry section 2 exists for it. Downstream, Delta_tau_M = sum y_lambda
chi_lambda(Delta_T_beta) is NOT tr_M(Delta) in either weighting (measured:
-0.18443 dim-weighted / -0.15802 un-dim-weighted vs -0.10624), so the two feed
different consumers with no note that they are different objects.

WHAT WOULD SETTLE IT (not attempted here): exhibit the two words. If NF(n)-NF(p)
and beta_n - beta_p are genuinely distinct elements of H_3(q), add the
disambiguation row. If they are meant to be the same element, one of the two
closed forms is wrong at O(hbar_q^2) and the ladder or the per-block extraction
inherits it.

Exact mpmath, no float64. NO fit, NO c_k, NO wiring, NO verdict on which is right.
"""
import datetime, hashlib, json, os, subprocess
import mpmath as mp
from mpmath import mpf

mp.mp.dps = 50
Q0 = "1.1099785827513808075916690956107688798744991218736"


def _sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True).strip()
    except Exception:
        return None


def chi3(q):  return -(q**2 - 1)*(q**2 + 1)**2/(4*q)
def chi21(q): return (q**2 - 1)*(-(q**4) - 1)/(4*q**3)
def chi111(q): return -(q**2 - 1)*(q**2 + 1)**2/(4*q**5)
def eps(q):   return (q - 1/q)**2/2 - (q - 1/q)


def main():
    q0 = mpf(Q0)
    assertions, ladder = [], []

    def check(name, passed, note=""):
        assertions.append({"name": name, "passed": bool(passed), "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    for e in ("1e-2", "1e-4", "1e-6", "1e-8"):
        q = 1 + mpf(e)
        ladder.append({"q": f"1+{e}", "ratio": mp.nstr(chi3(q)/eps(q), 18)})
    r0 = chi3(q0)/eps(q0)

    check("classical_limit_is_one",
          abs(chi3(1 + mpf("1e-8"))/eps(1 + mpf("1e-8")) - 1) < mpf("1e-7"),
          "(ratio -> 1 as q -> 1)")
    check("substrate_ratio_differs_from_one_by_more_than_30pct",
          abs(r0 - 1) > mpf("0.30"), f"(ratio at q0 = {mp.nstr(r0, 16)})")
    check("both_linear_in_hbar_q_at_leading_order",
          abs(chi3(1 + mpf("1e-8"))/eps(1 + mpf("1e-8")) - 1) < mpf("1e-6"))
    check("antipode_relation_holds_for_the_hand_derived_forms",
          abs(chi111(q0) - chi3(q0)/q0**4) < mpf("1e-40"))

    # downstream: Delta_tau_M vs tr_M(Delta) under the D weights
    h = q0 - 1/q0
    zD = q0**3/(q0**2 + 1)
    y3, y21 = (q0**4 + 1)/(q0**2 + 1)**2, q0**2/(q0**2 + 1)**2
    dtau_dim = y3*chi3(q0) + 2*y21*chi21(q0)
    dtau_nod = y3*chi3(q0) + y21*chi21(q0)
    trM = h**2/2 - h*zD
    check("delta_tau_M_is_not_trM_of_Delta_in_either_weighting",
          abs(dtau_dim - trM) > mpf("1e-3") and abs(dtau_nod - trM) > mpf("1e-3"),
          f"(dim={mp.nstr(dtau_dim,8)}, nodim={mp.nstr(dtau_nod,8)}, trM={mp.nstr(trM,8)})")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "FLAG, not a verdict. chi_(3)(Delta_T_beta)/eps(Delta) -> 1 as q -> 1 but "
        "is 1.3909 at the substrate. Since the counit IS the lambda=(n) block, "
        "that ratio would be identically 1 for one and the same element, so the "
        "two objects the corpus calls the neutron-minus-proton element of H_3 are "
        "DIFFERENT -- agreeing classically, diverging 39% at q0, and both linear "
        "in hbar_q at leading order (which is why a leading-order check missed "
        "it). That is what two different q-deformations of one classical object "
        "look like, and is NOT automatically an error. What IS a defect is that "
        "no registry section-2 disambiguation row exists and nothing in the "
        "corpus states they differ, while Delta_tau_M and tr_M(Delta) feed "
        "different consumers. Settling it needs the two WORDS exhibited; not "
        "attempted here. Nothing wired."
        if all_passed else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")

    src = open(__file__, "rb").read()
    w = {"computation": "qbeta-delta-vs-deltaTbeta-discrepancy",
         "description": "Two objects called the neutron-minus-proton element of "
                        "H_3(q) agree classically but differ 39% at the substrate, "
                        "with no disambiguation row in the corpus.",
         "engine": "mpmath", "markov_convention": "D",
         "assertions": assertions,
         "data": {"ratio_ladder_toward_q_eq_1": ladder,
                  "ratio_at_q0": mp.nstr(r0, 30),
                  "chi_3_at_q0": mp.nstr(chi3(q0), 30),
                  "eps_Delta_at_q0": mp.nstr(eps(q0), 30)},
         "verdict": verdict,
         "witness": {"scriptPath": "computations/qbeta/" + os.path.basename(__file__),
                     "scriptHash": hashlib.sha256(src).hexdigest()[:12],
                     "commitSha": _sha(),
                     "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat()}}
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qbeta-delta-vs-deltaTbeta-discrepancy.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        w.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            w, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(w, f, indent=2); f.write("\n")
    print(f"\n{verdict}\n\nWitness: {os.path.basename(out)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
