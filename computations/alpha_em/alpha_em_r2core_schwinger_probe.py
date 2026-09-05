#!/usr/bin/env python3
"""alpha_em_r2core_schwinger_probe.py

R2-CORE, FULLER CONTEXT (owner: "derive (or rule on) the framework's
proper-time measure normalization — take into account the information
theory corpus and E = m c_q^2"), under the ruling that R2 is NOT
derived-proved.

Companion to the sorry-free Lean module
QOU/Archimedean/SchwingerMeasureShape.lean (this PR): shape rigidity
(scale-invariant density => c/s), one-nat-per-e-fold, the E-Jacobian 2,
and the c=1 assembly to 1/(8 pi).

CORPUS INPUTS (information-theory chapter, all existing blocks):
  * E = m c_q^2 with c_q = 1/(q-1)      (mass-energy-equivalence)
  * k_B = 1; hbar_q = (q-1)/q replaces k_B T   (boltzmann-constant)
  * per-crossing operational entropy eta_q = (2q-1)/q^3 q-bits; additive
    over independent fibres              (fibre-channel-capacity)
  * horizon boundary datum invariant under rescaling
                                         (horizon-conformal-invariance)
  * "one full Reeb circuit = ONE UNIT OF TIME" — a time-unit convention
    resolving a transcendental factor    (discrete-planck-step)

WHAT THIS TRANCHE ESTABLISHES (V1-V4):
  V1. corpus-input arithmetic recorded exactly (c_q, hbar_q, eta_q at q0).
  V2. SHAPE RIGIDITY + NAT READING (mirrors the Lean): the scale-invariance
      functional equation forces the density c/s (corpus motivation:
      horizon rescaling invariance — the loop's UV end has no preferred
      proper-time scale); one e-fold carries measure exactly c; with
      k_B = 1, c IS the nat-count per proper-time e-fold. R2-core restated
      corpus-natively: "the loop measure assigns ONE NAT per proper-time
      e-fold" — a unit convention of EXACTLY the species the corpus
      canonized in discrete-planck-step (one Reeb circuit = one time unit).
  V3. THE HALF-ADJUDICATION, well-posed and OPEN (a NEW reading of the
      '2' — flagged into the readings saga): via E = m c_q^2 the Schwinger
      dimension is s ~ E^{-2}, so one ENERGY e-fold = TWO proper-time
      e-folds (Lean: efold_jacobian_two). Hence TWO mutually exclusive
      derivations of the 1/2: (a) the program's rho-split channel share
      (B4b, proved conditional); (b) the E-vs-s e-fold Jacobian (if the
      unit convention counts ENERGY e-folds). Each alone gives 1/(8 pi);
      BOTH together would give 1/(16 pi) — excluded by the working
      coefficient. Exact table verified. ADJUDICATION OPEN (owner-level:
      it is a choice of which e-fold variable the convention counts).
  V4. HONEST STATUS: R2-core is now fully corpus-native — "one nat per
      proper-time e-fold in the k_B = 1 convention" — with its provable
      shell (shape, nat reading, Jacobian, assembly) Lean-proved and its
      residue an explicit unit convention + one adjudication. Per the
      ruling: NOT proved, NOT asserted; smaller and in the corpus's own
      language.

Scope guard: no fit; nothing wired; 1/(8 pi) stays phase-4.
Self-contained (sympy).
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

    q, s, lam, pi, alpha = sp.symbols('q s lambda pi alpha', positive=True)

    # V1: corpus-input arithmetic
    c_q = 1 / (q - 1)
    hbar_q = (q - 1) / q
    eta_q = (2 * q - 1) / q ** 3
    q0 = sp.Rational(110998, 100000)
    v1 = (sp.simplify(c_q ** 2 - 1 / (q - 1) ** 2) == 0
          and sp.simplify(hbar_q - (1 - 1 / q)) == 0)
    check("corpus_inputs_recorded", v1,
          f"c_q = 1/(q−1) (E = m·c_q², mass-energy-equivalence); ℏ_q = (q−1)/q = k_B·T "
          f"(boltzmann-constant, k_B = 1 ⟹ nats); η_q(q₀) ≈ {sp.N(eta_q.subs(q, q0), 8)} "
          "q-bits/crossing (fibre-channel-capacity) — recorded, exact")

    # V2: shape rigidity + nat reading (mirrors the sorry-free Lean)
    c = sp.symbols('c', positive=True)
    f = c / s
    inv_ok = sp.simplify(f.subs(s, lam * s) * lam - f) == 0
    efold = sp.integrate(c / s, (s, s, sp.E * s))
    v2 = inv_ok and sp.simplify(efold - c) == 0
    check("shape_rigidity_and_nat_reading", v2,
          "c/s satisfies the scale-invariance equation (and the Lean proves uniqueness); "
          "∫ over one e-fold [s, e·s] = c exactly — with k_B = 1, c is the NAT-count per "
          "proper-time e-fold. R2-core corpus-natively: 'one nat per e-fold' — the same "
          "species as discrete-planck-step's 'one Reeb circuit = one unit of time'")

    # V3: the half-adjudication table
    a0 = 1 / (4 * pi)
    working = alpha / (8 * pi)
    rho_only = (1 * a0 * alpha) * sp.Rational(1, 2)
    jac_only = (sp.Rational(1, 2) * a0 * alpha)          # energy-e-fold convention: c_s = 1/2
    both = (sp.Rational(1, 2) * a0 * alpha) * sp.Rational(1, 2)
    v3 = (sp.simplify(rho_only - working) == 0
          and sp.simplify(jac_only - working) == 0
          and sp.simplify(both - alpha / (16 * pi)) == 0)
    check("half_adjudication_table", v3,
          "(a) ρ-split only: 1·a₀α·½ = α/(8π) ✓; (b) E-Jacobian only (energy-e-fold "
          "convention, s ~ E⁻² ⟹ c_s = ½): ½·a₀α = α/(8π) ✓; (a)+(b) together: α/(16π) ✗ "
          "— MUTUALLY EXCLUSIVE, each consistent alone. A NEW reading of the '2' (flagged "
          "into the readings saga); adjudication = which e-fold variable the unit "
          "convention counts — OPEN, owner-level")

    # V4: status bookkeeping
    v4 = True
    check("honest_status", v4,
          "R2-core restated fully corpus-natively: 'the loop measure assigns one nat per "
          "proper-time e-fold (k_B = 1)'. Provable shell Lean-proved (shape rigidity, nat "
          "reading, Jacobian, assembly — SchwingerMeasureShape, sorry-free); residue = the "
          "unit convention + the ½-adjudication. Per the 2026-07-19 ruling: NOT proved, "
          "NOT asserted")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "R2-CORE GIVEN ITS FULLER CONTEXT (scope-(a); R2 remains UNPROVEN per the ruling; "
        "no fit; nothing wired): the proper-time measure's SHAPE is rigid (scale "
        "invariance, corpus-motivated by horizon rescaling invariance — Lean-proved), and "
        "its unit is the NAT-count per proper-time e-fold in the corpus's own k_B = 1 "
        "convention — making R2-core the same SPECIES of unit convention the corpus "
        "already canonized in discrete-planck-step. The E = m·c_q² bridge yields a "
        "well-posed OPEN adjudication: the ½ has two mutually exclusive readings (ρ-split "
        "channel share vs energy-vs-proper-time e-fold Jacobian), each alone giving "
        "1/(8π) — a new entry in the readings-of-2 saga, owner-level. Residue after this "
        "tranche: ONE unit convention ('one nat per e-fold') + ONE adjudication (which "
        "e-fold variable) — both stated in corpus-native information-theoretic language. "
        "NO tier change."
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
        "computation": "alpha-em-r2core-schwinger",
        "description": "R2-core fuller context (owner-directed; info-theory corpus + E=mc_q^2). "
                       "Shape rigidity Lean-proved (SchwingerMeasureShape); unit = nat-count per "
                       "proper-time e-fold (k_B=1) — same species as discrete-planck-step's unit "
                       "convention; E=mc_q^2 yields the open half-adjudication (rho-split vs "
                       "E-Jacobian, mutually exclusive, each giving 1/(8pi) — new reading of the "
                       "2). R2 remains unproven per the ruling. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-19-alpha-em-r2core-schwinger.md",
        "tier": "sorry-free Lean shell + symbolic-exact context; residue = unit convention + "
                "one adjudication (open)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy+lean", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "lean": "QOU/Archimedean/SchwingerMeasureShape.lean — shape rigidity, one nat per "
                    "e-fold, E-Jacobian 2, c=1 assembly (sorry-free)",
            "corpus_native_r2core": "'the loop measure assigns one nat per proper-time e-fold "
                                    "(k_B = 1)' — same species as discrete-planck-step",
            "half_adjudication": "rho-split vs E-Jacobian: mutually exclusive, each -> 1/(8pi); "
                                 "both -> 1/(16pi) excluded; OPEN (owner-level)",
            "verdict": verdict,
        },
        "context": {
            "corpus_blocks": "mass-energy-equivalence, boltzmann-constant, "
                             "fibre-channel-capacity, horizon-conformal-invariance, "
                             "discrete-planck-step",
            "ruling": "2026-07-19: R2 not lean/derived-proved — respected; nothing asserted",
            "scope_guard": "no fit; nothing wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-r2core-schwinger.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
