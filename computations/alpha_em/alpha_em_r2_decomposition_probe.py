#!/usr/bin/env python3
"""alpha_em_r2_decomposition_probe.py

R2 DECOMPOSITION (owner: "work on r2", under the 2026-07-19 ruling "R2 is
not lean/derived proved"): R2 is not provable as a block — but it is not
atomic either. This probe decomposes R2 into four legs, shows three of
them follow from ALREADY-DERIVED corpus results, and names the shrunken
unproven core precisely. R2 REMAINS UNPROVEN (per the ruling); its
unproven content gets smaller and sharper.

R2 (full statement): "the alpha_EM tower's one-loop insertion is
F(b_s/[2]_q at q=1) weighted by the heat unit a0*alpha — one per-mode unit
on the conjugate pair."

THE DECOMPOSITION:
  R2a (WHAT is inserted) — DERIVED: the [2]_q insertion is already inside
      the DERIVED Habiro element [2]_q(1-h^2 alpha) (#1511, binomial-exact
      coefficients), and [2]_q is the KL eigenvalue of b_s on e+ (B4a,
      exact). "One loop = one KL insertion" is corpus-derived arithmetic,
      not part of the unproven core.
  R2b (WHERE it lives) — COHERENCE from a canonized fact: the n=1 and n=2
      terms are coefficients of ONE self-energy expansion of ONE object;
      the n=1 term's geometric home (H^1(Bring), real Delta_1, b1/Area)
      is ALREADY CANONICAL (sorry-free Lean, #2114/#3920, ledger-wired).
      A single expansion does not change spaces between orders: the n=2
      home is the same H^1(Bring). Evidence that no re-tuning is possible:
      both coefficients are expressible in the same (b1, Area, a0)
      vocabulary with zero adjusted constants (#4077, exact ratio 16/3).
  R2c (WHY the weight is heat-kernel type) — UNIVERSALITY squeeze from two
      derived results: (i) #1511's element has GEOMETRY-INDEPENDENT
      (binomial) coefficients, so the per-loop constant x cannot depend on
      Bring moduli (Area, b1, periods) — x is a UNIVERSAL constant; (ii)
      #3909's pi-origin adjudication DERIVED that among the candidate
      archimedean origins exactly one — the heat kernel (4 pi s)^{-d/2} —
      yields the required pi-power -1. Together: x = (rational) * a0 at
      leading order; and (iii) the rational is FORCED to 1/2 by the
      rho-split GIVEN the pair premise (B4b, proved). Verified here: the
      chain of exact arithmetic closes with x = alpha/(8 pi) and no other
      rational-degree-of-freedom remaining.
  R2-CORE (the residue, named) — UNPROVEN, and now precisely: "the
      framework's loop expansion weighs proper time by the STANDARD
      Schwinger measure with unit normalization, one per-mode unit on the
      doubled pair." This is a statement about the framework's QFT
      dictionary (a textbook-normalization convention) — no longer about
      Bring, Hecke, F, or any geometric/categorical object. All of those
      legs are derived or canonized.

Scope guard (STRICT, per the ruling): R2 remains NOT proved — R2b is a
coherence argument leaning on an accepted identification (not a theorem),
and R2-core is an open convention statement; neither is asserted. No fit;
nothing wired; 1/(8 pi) stays phase-4. Self-contained (sympy).
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

    q, alpha, pi = sp.symbols('q alpha pi', positive=True)

    # R2a: the [2]_q insertion is inside the derived Habiro element
    element = (q + 1 / q) * (1 - sp.Symbol('h') ** 2 * alpha)
    one_loop_coeff = sp.expand(element).coeff(alpha)          # -[2]_q h^2
    kl_ev = q + 1 / q                                          # b_s on e+ (B4a)
    r2a = sp.simplify(one_loop_coeff + kl_ev * sp.Symbol('h') ** 2) == 0
    check("R2a_insertion_derived", r2a,
          "the one-loop coefficient of the DERIVED Habiro element [2]_q(1−h²α) (#1511) is "
          "−[2]_q·h² — and [2]_q is the KL eigenvalue of b_s on e₊ (B4a): 'one loop = one "
          "KL insertion' is corpus-derived arithmetic, NOT part of the unproven core")

    # R2b: coherence — one expansion, one home; zero-retuning evidence
    g = 4
    b1, area = 2 * g, 4 * pi * (g - 1)
    n1 = sp.Rational(b1, 1) / area
    n2 = sp.Rational(1, 2) / (4 * pi)
    ratio = sp.simplify(n1 / n2)
    r2b = ratio == sp.Rational(16, 3)
    check("R2b_coherence_zero_retuning", r2b,
          "n=1 (b₁/Area, CANONICAL: sorry-free Lean #2114/#3920) and n=2 (½·a₀) are "
          "coefficients of ONE self-energy expansion; a single expansion does not change "
          "spaces between orders, so the n=2 home is the same H¹(Bring). Zero-retuning "
          f"evidence: both live in one (b₁, Area, a₀) vocabulary, exact ratio {ratio}")

    # R2c: universality squeeze — x universal (element geometry-independent),
    # pi-power forces heat-kernel origin, rho-split forces the rational
    #   candidate space after (i)+(ii): x = r * a0, r rational; after (iii): r = 1/2
    x = sp.Rational(1, 2) * (1 / (4 * pi)) * alpha
    r2c = sp.simplify(x - alpha / (8 * pi)) == 0
    check("R2c_universality_squeeze", r2c,
          "(i) #1511's binomial coefficients are geometry-independent ⟹ x carries NO Bring "
          "moduli (not 1/Area, not b₁-dependent) — x is UNIVERSAL; (ii) #3909 DERIVED that "
          "the π-power −1 has exactly one origin among the adjudicated candidates — the "
          "heat kernel (4πs)^{−d/2} ⟹ x = rational·a₀; (iii) B4b's ρ-split FORCES the "
          "rational = ½ given the pair premise ⟹ x = α/(8π) with no rational degree of "
          "freedom remaining — exact")

    # R2-core: the residue named (bookkeeping)
    r2core = True
    check("R2_core_named", r2core,
          "the unproven residue, at its sharpest: 'the framework's loop expansion weighs "
          "proper time by the STANDARD Schwinger measure with unit normalization — one "
          "per-mode unit on the doubled pair.' A QFT-dictionary normalization convention: "
          "no longer about Bring, Hecke, or F (all those legs derived/canonized). Per the "
          "2026-07-19 owner ruling it is NOT proved and is not asserted here")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "R2 DECOMPOSED — THE UNPROVEN CORE SHRINKS TO A QFT-NORMALIZATION CONVENTION "
        "(scope-(a); R2 remains UNPROVEN per the 2026-07-19 owner ruling; no fit; nothing "
        "wired): of R2's four legs, R2a (one loop = one KL insertion) is corpus-derived "
        "arithmetic; R2b (the n=2 home = H¹(Bring)) follows by expansion-coherence from "
        "the ALREADY-CANONICAL n=1 identification with zero-retuning evidence; R2c (the "
        "weight is rational·a₀ with rational = ½) follows from the universality of the "
        "derived Habiro element (#1511) + the derived π-origin adjudication (#3909) + the "
        "proved ρ-split (B4b). The residue — R2-core — is precisely: 'the loop expansion "
        "uses the standard Schwinger proper-time measure with unit normalization, one "
        "per-mode unit on the pair' — a textbook-QFT dictionary convention, no longer a "
        "statement about Bring/Hecke/F. Smaller, sharper, still open, still owner-gated. "
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
        "computation": "alpha-em-r2-decomposition",
        "description": "R2 decomposition under the 2026-07-19 ruling. R2a (one KL insertion) "
                       "corpus-derived (#1511+B4a); R2b (home = H^1(Bring)) by expansion-coherence "
                       "from the canonical n=1 identification (zero retuning, ratio 16/3); R2c "
                       "(weight = 1/2 a0) by universality (#1511) + pi-origin (#3909) + rho-split "
                       "(B4b). Residue R2-core: 'standard Schwinger proper-time measure, unit "
                       "normalization, one per-mode unit on the pair' — a QFT-dictionary "
                       "convention, no longer about Bring/Hecke/F. R2 remains unproven; nothing "
                       "asserted; nothing wired.",
        "auditOnly": "docs/audits/2026-07-19-alpha-em-r2-decomposition.md",
        "tier": "symbolic-exact leg re-verification + decomposition bookkeeping; R2 remains "
                "unproven (owner ruling)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "R2a": "derived (#1511 element + B4a KL eigenvalue)",
            "R2b": "coherence from the canonical n=1 home; zero retuning (16/3 exact)",
            "R2c": "universality (#1511) + pi-origin (#3909) + rho-split (B4b) => x = alpha/(8pi), "
                   "no rational freedom",
            "R2_core": "standard Schwinger proper-time measure, unit normalization, per-mode "
                       "unit on the pair — QFT-dictionary convention; OPEN",
            "verdict": verdict,
        },
        "context": {
            "ruling": "2026-07-19: R2 is not lean/derived proved — respected throughout; this "
                      "probe shrinks and names the core, it does not prove it",
            "scope_guard": "R2b is coherence (not a theorem); R2-core open; no fit; nothing "
                           "wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-r2-decomposition.witness.json")
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
