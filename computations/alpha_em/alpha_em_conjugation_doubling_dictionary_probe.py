#!/usr/bin/env python3
"""alpha_em_conjugation_doubling_dictionary_probe.py

First brick of the correspondence-statement attack (the remaining 1/pi wall,
stated in the merged conjecture-statement PR): the UNIFICATION HYPOTHESIS said
the Hecke channel pair e+/e- and the Hodge pair H^{1,0}/H^{0,1} are "the same
conjugation doubling", with the naive dictionary {bar involution <-> complex
conjugation}. This probe tests the dictionary EXACTLY — and corrects it.

FINDINGS (exact, sympy):
  D1. NAIVE DICTIONARY REFUTED: the bar involution (q -> q^{-1}, sigma ->
      sigma^{-1}) FIXES each channel individually — bar(e+) = e+, bar(e-) = e-
      (exact mod the Hecke relation) — while complex conjugation SWAPS
      H^{1,0} <-> H^{0,1}. A channel-fixing involution cannot correspond to a
      channel-swapping one. Scope-(a) exclusion of {bar <-> conjugation}.
  D2. THE CORRECT CHANNEL-SWAPPER IS THE TRANSPOSE DUALITY phi: q -> -q^{-1}
      (sigma fixed): it preserves the Hecke relation ((sigma-q)(sigma+q^{-1})
      is phi-invariant) and SWAPS e+ <-> e- exactly. (This is the eigenvalue
      swap q <-> -q^{-1}, i.e. the symmetric/antisymmetric = partition-transpose
      duality.) Corrected dictionary: {transpose <-> complex conjugation}.
  D3. FIXED-LOCUS COINCIDENCE (exact): the transpose-fixed locus is q^2 = -1 —
      IDENTICAL to the equal-channel-weight locus of the resummed tower
      (w+ = w- = 1/2 iff q^2 = -1, the merged F2). Channel democracy occurs
      exactly at the transpose-symmetric point; the classical limit q = 1 is
      bar-fixed instead. The two involutions organize the two special loci.
  D4. EQUIVARIANCE TENSION (recorded as the sharp open sub-question): on the
      Hodge side conjugation is S5-EQUIVARIANT with H^{0,1} ~ H^{1,0} = std
      (chi_std is real); on the partition side the transpose maps std = (4,1)
      to (2,1,1,1) = std (x) sign, a DIFFERENT irrep (characters differ, e.g.
      chi((12)) = 2 vs -2). So the corrected dictionary matches the two
      2-element channel sets with involution, but is NOT (yet) S5-equivariant
      as stated — the tau-functor identification must resolve which symmetry
      (2-strand channel transpose vs 5-letter partition transpose) is the one
      carried to conjugation. This is the precise next question.

Scope guard: exact structural facts + one exclusion; derives NO clause of the
per-loop conjecture; no fit; nothing wired; 1/(8pi) stays phase-4.
Self-contained (sympy).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    q, s = sp.symbols('q sigma')
    hecke = sp.expand((s - q) * (s + 1 / q))
    h = q + 1 / q
    ep = (s + 1 / q) / h
    em = (q - s) / h
    sinv = s - q + 1 / q          # sigma^{-1} = sigma - (q - q^{-1}) mod Hecke

    def red(e):
        return sp.simplify(sp.rem(sp.expand(sp.together(e) * sp.denom(sp.together(e))), hecke, s)
                           / sp.denom(sp.together(e))) if False else sp.simplify(sp.rem(sp.expand(e), hecke, s))

    # D1: bar fixes the channels
    bar_ep = (sinv + q) / (1 / q + q)
    bar_em = (1 / q - sinv) / (1 / q + q)
    d1 = red(sp.simplify(bar_ep - ep)) == 0 and red(sp.simplify(bar_em - em)) == 0
    check("naive_bar_conjugation_dictionary_refuted", d1,
          "bar(e+) = e+ and bar(e-) = e- EXACTLY (bar: q->q^{-1}, sigma->sigma^{-1}) — the "
          "bar involution FIXES each channel, while complex conjugation SWAPS "
          "H^{1,0}<->H^{0,1}; the naive dictionary {bar <-> conjugation} is EXCLUDED "
          "(scope-(a))")

    # D2: transpose swaps the channels and preserves the relation
    t_ep = (s - q) / (-1 / q - q)          # e+ evaluated at q -> -q^{-1}
    t_em = (-1 / q - s) / (-1 / q - q)     # e- evaluated at q -> -q^{-1}
    hecke_t = sp.expand((s + 1 / q) * (s - q))
    d2 = (red(sp.simplify(t_ep - em)) == 0 and red(sp.simplify(t_em - ep)) == 0
          and sp.simplify(hecke_t - hecke) == 0)
    check("transpose_is_the_channel_swapper", d2,
          "phi: q -> -q^{-1} preserves the Hecke relation and swaps e+ <-> e- EXACTLY — "
          "the eigenvalue swap q <-> -q^{-1} (symmetric/antisymmetric = partition-transpose "
          "duality). Corrected dictionary: {transpose <-> complex conjugation}")

    # D3: transpose-fixed locus == equal-weight locus (q^2 = -1)
    fixed = sp.solve(sp.Eq(q, -1 / q), q)
    wp = q ** 2 / (q ** 2 - 1)
    equal = sp.solve(sp.Eq(wp, sp.Rational(1, 2)), q)
    d3 = set(fixed) == set(equal) == {sp.I, -sp.I}
    check("transpose_fixed_locus_equals_equal_weight_locus", d3,
          f"transpose-fixed locus {fixed} == equal-channel-weight locus {equal} == q^2=-1 "
          "EXACTLY: channel democracy (w+=w-=1/2, merged F2) occurs precisely at the "
          "transpose-symmetric point; the classical limit q=1 is bar-fixed — the two "
          "involutions organize the two special loci")

    # D4: equivariance tension — chi_std real (conjugation S5-equivariant on Hodge) but
    #     partition transpose maps std to std(x)sign (different irrep)
    def perm_char(g):
        return sum(1 for i in range(5) if g(i) == i)
    S5 = SymmetricGroup(5)
    els = list(S5.generate())
    chi_std_real = all(sp.im(perm_char(g) - 1) == 0 for g in els)   # trivially real, recorded
    t12 = Permutation([1, 0, 2, 3, 4])
    chi_std_t12 = perm_char(t12) - 1
    chi_sgn_t12 = (perm_char(t12) - 1) * t12.signature()
    d4 = chi_std_real and chi_std_t12 == 2 and chi_sgn_t12 == -2
    check("equivariance_tension_recorded", d4,
          "chi_std is real => H^{0,1} ~ H^{1,0} = std as S5-reps (conjugation IS "
          "S5-equivariant on the Hodge side), but the PARTITION transpose maps std=(4,1) to "
          "(2,1,1,1)=std(x)sign — distinct irrep (chi((12)): 2 vs -2). The corrected "
          "dictionary matches the 2-element channel sets, but the S5-equivariant content of "
          "the tau identification (2-strand channel transpose vs 5-letter partition "
          "transpose vs conjugation) is the precise remaining question")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "CONJUGATION-DOUBLING DICTIONARY — CORRECTED (scope-(a); derives no clause; no fit; "
        "nothing wired): the naive {bar <-> complex conjugation} dictionary of the unification "
        "hypothesis is REFUTED — bar FIXES both Hecke channels (bar(e±)=e± exact) while "
        "conjugation swaps the Hodge pair. The genuine channel-swapper is the TRANSPOSE "
        "duality phi: q -> -q^{-1} (preserves the Hecke relation, swaps e+<->e- exactly), so "
        "the corrected dictionary is {transpose <-> conjugation}. Exact bonus: the "
        "transpose-fixed locus q^2=-1 IS the equal-channel-weight locus (F2) — democracy at "
        "the transpose-symmetric point, classical limit at the bar-fixed point. Open sharp "
        "sub-question (recorded): the S5-equivariant content — conjugation is equivariant "
        "with H^{0,1}~std, but partition transpose maps std to std(x)sign. The correspondence "
        "statement remains open; this narrows its dictionary. NO tier change."
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
        "computation": "alpha-em-conjugation-doubling-dictionary",
        "description": "Corrects the unification-hypothesis dictionary for the 1/pi correspondence "
                       "statement: bar FIXES both Hecke channels (naive {bar<->conjugation} refuted); "
                       "the channel-swapper is the transpose duality q->-q^{-1} ({transpose<->conjugation} "
                       "corrected dictionary); transpose-fixed locus q^2=-1 == equal-weight locus (F2); "
                       "S5-equivariance tension recorded (std vs std(x)sign). Derives no clause; nothing "
                       "wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-conjugation-doubling-dictionary.md",
        "tier": "symbolic-exact (sympy; quotient-ring involution identities + character values)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "bar_action": "fixes e+ and e- individually (exact)",
            "transpose_action": "swaps e+ <-> e- (exact); preserves the Hecke relation",
            "corrected_dictionary": "{transpose duality q->-q^{-1}} <-> {complex conjugation on H^1}",
            "fixed_locus_coincidence": "q^2=-1 (transpose-fixed) == equal-weight locus (F2)",
            "open_subquestion": "S5-equivariant content: conjugation equivariant (H^{0,1}~std) vs "
                                "partition transpose (std -> std(x)sign)",
            "verdict": verdict,
        },
        "context": {
            "attacks": "the correspondence statement (the single remaining 1/pi wall, merged "
                       "conjecture-statement PR) via its unification hypothesis",
            "builds_on": "merged F1-F3 (channel count derived, weights excluded, classical-limit "
                         "normalization) + #3920 (Hodge doubling) + ba606720e (GB form)",
            "scope_guard": "exact structural facts + one exclusion; derives NO clause; no fit; "
                           "nothing wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-conjugation-doubling-dictionary.witness.json")
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
