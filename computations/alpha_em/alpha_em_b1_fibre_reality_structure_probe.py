#!/usr/bin/env python3
"""alpha_em_b1_fibre_reality_structure_probe.py

Bean B1 (qou-qcz1) of the tau-correspondence proof plan (milestone qou-b5qg):
the FIBRE REALITY STRUCTURE — where the anti-holomorphic ingredient demanded by
the tau-obstruction (a6d522e0a) actually lives, and the resulting TYPE-CONSISTENT
dictionary.

The obstruction: through the nome q = e^{2 pi i tau}, the channel-swap
q -> -q^{-1} is HOLOMORPHIC (tau -> 1/2 - tau) while Hodge conjugation is
ANTI-holomorphic (tau -> -conj(tau)); a holomorphic tau-functor cannot identify
them. "The anti-holomorphic ingredient must enter through the fibre."

B1 RESULT (exact): the ingredient is the fibre PARAMETER CONJUGATION
rho: q -> conj(q) — an involution NOT in the q-algebra (not algebraic in q):

  R1. rho is ANTI-HOLOMORPHIC of exactly the Hodge type: through the nome,
      q -> conj(q) IS tau -> -conj(tau) (verified symbolically) — the same
      analytic type as Hodge conjugation. The pairing {rho <-> Hodge
      conjugation} has NO type obstruction.
  R2. On the fibre circle |q| = 1, rho coincides POINTWISE with bar
      (q^{-1} = conj(q)) — but differs from bar as a global analytic map
      (bar is holomorphic, rho is not). This resolves why brick 3 saw "bar
      exchanging the degenerate points": on the circle that exchange IS rho,
      seen through its restriction. The Lean-locked geometric realization
      (coordinate conjugation swapping the vertex families, #3942) is rho's
      action — genuinely anti-holomorphic.
  R3. rho FIXES the archimedean point (q0 real => conj(q0) = q0): the reality
      structure is unbroken at the observable point — the conjugation doubling
      is FIBRE-ONLY, consistent with the Im(q) fibre-vs-observable discipline
      and with real masses at q0.
  R4. THE FULL DICTIONARY NOW TYPES CONSISTENTLY (each row same analytic type):
        bar        q -> q^{-1}   (holo)      <->  tau -> -tau        (holo)
        transpose  q -> -q^{-1}  (holo)      <->  tau -> 1/2 - tau   (holo)
        rho        q -> conj(q)  (anti-holo) <->  tau -> -conj(tau)  (anti-holo)
      The obstruction barred only the mis-typed pairing {transpose <-> Hodge
      conjugation}; the conjugation doubling pairs with rho. On the degenerate
      pair {+-i}: rho exchanges the points (rho(i) = -i), the transpose fixes
      them — the two-strata role-swap, now with correct analytic typing.

WHAT B1 LEAVES FOR B2: the functorial statement itself — that tau intertwines
rho with the actual Hodge conjugation of H^1(Bring) (the shadow of which is the
Lean-locked vertex-family swap). B1 supplies the type-consistent dictionary; it
does NOT derive the functor.

Scope guard: exact analytic bookkeeping; derives NO clause; no fit; nothing
wired; 1/(8pi) stays phase-4. Self-contained (sympy).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    tau = sp.symbols('tau')
    th = sp.symbols('theta', real=True)
    qn = sp.exp(2 * sp.pi * sp.I * tau)

    # R1: rho through the nome is tau -> -conj(tau) (anti-holo, the Hodge type)
    r1 = sp.simplify(sp.conjugate(qn)
                     - sp.exp(2 * sp.pi * sp.I * (-sp.conjugate(tau)))) == 0
    check("rho_is_antiholo_hodge_type", r1,
          "conj(e^{2 pi i tau}) = e^{2 pi i (-conj tau)} EXACTLY: the fibre parameter "
          "conjugation rho: q->conj(q) corresponds to tau -> -conj(tau) — the SAME "
          "anti-holomorphic type as Hodge conjugation (obstruction table row 3). The "
          "pairing {rho <-> Hodge conjugation} has NO type obstruction")

    # R2: on |q|=1, rho = bar pointwise (but not as analytic maps)
    qc = sp.exp(sp.I * th)
    r2 = sp.simplify(1 / qc - sp.conjugate(qc)) == 0
    check("rho_restricts_to_bar_on_circle", r2,
          "on |q|=1: q^{-1} = conj(q) — rho coincides POINTWISE with bar on the fibre "
          "circle (while differing globally: bar holo, rho anti-holo). Brick 3's 'bar "
          "exchanges the degenerate points' is rho seen through its circle restriction; "
          "the Lean-locked vertex-family swap (#3942) is rho's geometric action")

    # R3: rho fixes the archimedean point
    q0 = sp.Rational(110998, 100000)
    r3 = sp.conjugate(q0) == q0
    check("rho_fixes_archimedean_point", r3,
          "q0 in R => conj(q0) = q0: the reality structure is UNBROKEN at the observable "
          "point — the conjugation doubling is fibre-only (consistent with the Im(q) "
          "fibre-vs-observable discipline and real masses at q0)")

    # R4: the full dictionary types consistently + degenerate-pair actions
    bar_nome = sp.simplify(1 / qn - sp.exp(2 * sp.pi * sp.I * (-tau))) == 0        # holo
    tr_nome = sp.simplify(-1 / qn - sp.exp(2 * sp.pi * sp.I * (sp.Rational(1, 2) - tau))) == 0  # holo
    rho_i = sp.conjugate(sp.I) == -sp.I          # rho exchanges the degenerate pair
    tr_i = sp.simplify(-1 / sp.I) == sp.I        # transpose fixes it
    r4 = bar_nome and tr_nome and rho_i and tr_i
    check("full_dictionary_types_consistently", r4,
          "bar: q->q^{-1} <-> tau->-tau (holo=holo); transpose: q->-q^{-1} <-> "
          "tau->1/2-tau (holo=holo); rho: q->conj(q) <-> tau->-conj(tau) (anti=anti) — "
          "every row same analytic type; the obstruction barred only the mis-typed "
          "{transpose <-> conjugation}. On {+-i}: rho exchanges (conj(i)=-i), transpose "
          "fixes (-1/i=i) — the two-strata role-swap with correct typing")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "B1 CLOSED AS SCOPED (scope-(a); derives no clause; no fit; nothing wired): the "
        "anti-holomorphic ingredient demanded by the tau-obstruction is the fibre PARAMETER "
        "CONJUGATION rho: q->conj(q) — not in the q-algebra, anti-holomorphic of exactly the "
        "Hodge type (tau->-conj(tau) through the nome), coinciding with bar pointwise on the "
        "fibre circle (resolving brick 3's bar-exchange as rho's restriction), fixing the "
        "archimedean q0 (fibre-only doubling), and completing a TYPE-CONSISTENT dictionary "
        "(bar<->-tau, transpose<->1/2-tau, rho<->-conj tau). The conjugation doubling pairs "
        "with rho, whose geometric shadow is the Lean-locked vertex-family swap. REMAINING "
        "(B2): the functorial statement that tau intertwines rho with the actual Hodge "
        "conjugation of H^1(Bring). NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-b1-fibre-reality-structure",
        "description": "Bean B1 (qou-qcz1): the anti-holomorphic ingredient of the tau-correspondence "
                       "is the fibre parameter conjugation rho: q->conj(q) — Hodge-type through the nome "
                       "(tau->-conj tau), = bar pointwise on |q|=1 (brick 3's exchange was rho's "
                       "restriction), fixes q0 (fibre-only doubling), and completes the type-consistent "
                       "dictionary. Conjugation pairs with rho, not the transpose. B2 = the functorial "
                       "statement. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-b1-fibre-reality-structure.md",
        "tier": "symbolic-exact (sympy; nome analytic types + circle restriction + degenerate actions)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "reality_involution": "rho: q -> conj(q) (anti-holo; not in the q-algebra)",
            "nome_type": "tau -> -conj(tau) = the Hodge-conjugation type (no obstruction)",
            "circle_restriction": "rho = bar pointwise on |q|=1",
            "archimedean": "rho fixes q0 (fibre-only doubling)",
            "dictionary": "bar<->-tau (holo), transpose<->1/2-tau (holo), rho<->-conj tau (anti-holo)",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-qcz1 (B1) of milestone qou-b5qg",
            "resolves": "the a6d522e0a holo/anti-holo obstruction — by re-routing the conjugation "
                        "pairing through rho (the mis-typed {transpose<->conjugation} stays barred)",
            "geometric_shadow": "the Lean-locked vertex-family swap (#3942 SigmaJGeometricCarrier)",
            "next": "B2 (qou-tq20): the functorial statement tau(rho) = Hodge conjugation",
            "scope_guard": "derives NO clause; no fit; nothing wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-b1-fibre-reality-structure.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
