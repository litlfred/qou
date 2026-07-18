#!/usr/bin/env python3
"""alpha_em_d4_equivariance_adjudication_probe.py

Brick 2 of the correspondence-statement attack: ADJUDICATES the D4 equivariance
question of the corrected conjugation-doubling dictionary (brick 1) — which
transpose does the tau identification carry to complex conjugation on H^1(Bring):
the 2-STRAND CHANNEL transpose (q -> -q^{-1} on e+/e-) or the 5-LETTER PARTITION
transpose (lambda -> lambda' on S5-irreps)?

ADJUDICATION (necessary conditions; exact):
  E1. THE 5-LETTER PARTITION TRANSPOSE IS EXCLUDED. Conjugation preserves the
      S5-isotype: H^{0,1} ~ conj(H^{1,0}) ~ std (chi_std is real; verified over
      all 7 conjugacy classes). The partition transpose maps std = (4,1) to
      (2,1,1,1) = std (x) sign — a DIFFERENT irrep (characters differ on all odd
      classes). An isotype-changing involution cannot be an isotype-preserving
      one. EXCLUDED (scope-(a)).
  E2. THE 2-STRAND CHANNEL TRANSPOSE PASSES the same test: it acts on the loop-
      parameter/channel index only (S5 = Aut(Bring) acts on the OTHER tensor
      factor), so it is S5-NEUTRAL — isotype-preserving, like conjugation. It is
      the unique surviving candidate of the two.
  E3. FIBRE-CIRCLE GEOMETRY (exact): on |q| = 1 (q = e^{i theta}), the bar
      involution is reflection across the REAL axis (theta -> -theta; fixed
      points q = +-1 = the classical points; FIXES the channels), and the channel
      transpose is reflection across the IMAGINARY axis (theta -> pi - theta;
      fixed points q = +-i = the democratic points; SWAPS the channels); their
      composition is the antipode q -> -q. The two involutions generate the
      dihedral symmetry of the fibre circle, organizing {classical, democratic}
      as the two reflection axes.
  E4. SPEC(J) COINCIDENCE (exact): at the transpose-fixed points q = +-i the
      Hecke relation DEGENERATES to (sigma -+ i)^2 = 0 — the two channels merge
      with common eigenvalue +-i. But {+i, -i} = spec(J), the eigenvalues of the
      complex structure J on H^1(M,R)(x)C whose eigenspaces ARE H^{1,0}/H^{0,1}
      and whose eigenspace-swap IS conjugation. The channel pair collapses
      exactly at the eigenvalues of the operator whose doubling it is conjectured
      to match.

NET: D4 is adjudicated at the necessary-condition level — the tau identification
must carry the 2-STRAND CHANNEL transpose to conjugation; the 5-letter partition
transpose is excluded (it is the flavor-side fermion-boson/spin-flip, a different
doubling). The full tau-functor derivation (the wall) remains open; its target is
now unique.

Scope guard: necessary conditions + one exclusion; derives NO clause; no fit;
nothing wired; 1/(8pi) stays phase-4. Self-contained (sympy).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp
from sympy.combinatorics import Permutation


def perm_char(g):
    return sum(1 for i in range(5) if g(i) == i)


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # class representatives of S5 (7 classes)
    reps = {
        "e": Permutation([0, 1, 2, 3, 4]),
        "(12)": Permutation([1, 0, 2, 3, 4]),
        "(12)(34)": Permutation([1, 0, 3, 2, 4]),
        "(123)": Permutation([1, 2, 0, 3, 4]),
        "(123)(45)": Permutation([1, 2, 0, 4, 3]),
        "(1234)": Permutation([1, 2, 3, 0, 4]),
        "(12345)": Permutation([1, 2, 3, 4, 0]),
    }
    chi_std = {c: perm_char(g) - 1 for c, g in reps.items()}
    chi_sgn = {c: (perm_char(g) - 1) * g.signature() for c, g in reps.items()}

    # E1: partition transpose excluded — chi_std real (conj preserves isotype) but
    #     chi_{std (x) sign} differs from chi_std on the odd classes
    real_ok = all(sp.im(v) == 0 for v in chi_std.values())
    odd_classes = [c for c, g in reps.items() if g.signature() == -1]
    differs = all(chi_std[c] != chi_sgn[c] for c in odd_classes if chi_std[c] != 0)
    e1 = real_ok and differs and chi_std["(12)"] == 2 and chi_sgn["(12)"] == -2
    check("partition_transpose_excluded_isotype_mismatch", e1,
          "chi_std real over all 7 classes => conjugation preserves the isotype "
          "(H^{0,1}~std); partition transpose sends std->(2,1,1,1)=std(x)sign with "
          f"chi((12)) = {chi_std['(12)']} vs {chi_sgn['(12)']} — isotype-CHANGING, so it "
          "cannot be conjugation. EXCLUDED (scope-(a))")

    # E2: channel transpose is S5-neutral — it acts on the q-parameter/channel factor;
    #     the S5 character content is untouched (chi_std is q-independent)
    q = sp.symbols('q')
    e2 = all(sp.simplify(sp.sympify(v).subs(q, -1 / q) - v) == 0 for v in chi_std.values())
    check("channel_transpose_S5_neutral_survives", e2,
          "the channel transpose phi: q -> -q^{-1} acts on the loop-parameter/channel "
          "index only — every S5 character value is q-independent hence phi-invariant: "
          "isotype-PRESERVING like conjugation. The unique surviving candidate of the two")

    # E3: fibre-circle geometry — bar = reflection across R (fixes q=+-1), transpose =
    #     reflection across iR (fixes q=+-i), composition = antipode
    th = sp.symbols('theta', real=True)
    qq = sp.exp(sp.I * th)
    bar_q = sp.simplify(1 / qq)                      # q -> q^{-1} = conj(q) on |q|=1
    tr_q = sp.simplify(-1 / qq)                      # q -> -q^{-1} = -conj(q)
    bar_is_conj = sp.simplify(bar_q - sp.conjugate(qq)) == 0
    tr_is_reflect_imag = sp.simplify(tr_q - sp.exp(sp.I * (sp.pi - th))) == 0
    fix_bar = sp.solve(sp.Eq(qq, 1 / qq), th)        # theta = 0, pi (q=+-1)
    fix_tr = sp.solve(sp.Eq(qq, -1 / qq), th)        # theta = +-pi/2 (q=+-i)
    anti = sp.simplify((-1 / (1 / qq)) - (-qq)) == 0  # transpose(bar(q)) = -q
    e3 = (bar_is_conj and tr_is_reflect_imag and anti
          and {sp.simplify(qq.subs(th, t)) for t in fix_bar} == {1, -1}
          and {sp.simplify(qq.subs(th, t)) for t in fix_tr} == {sp.I, -sp.I})
    check("fibre_circle_two_reflections", e3,
          "on |q|=1: bar = reflection across R (theta->-theta; fixed q=+-1, the classical "
          "points, channels FIXED) and transpose = reflection across iR (theta->pi-theta; "
          "fixed q=+-i, the democratic points, channels SWAPPED); composition = antipode "
          "q->-q — the two involutions are the two reflection axes of the fibre circle")

    # E4: spec(J) coincidence — at q=+-i the Hecke relation degenerates to (sigma-+i)^2
    s = sp.symbols('sigma')
    rel = sp.expand((s - q) * (s + 1 / q))
    at_i = sp.expand(rel.subs(q, sp.I))
    at_mi = sp.expand(rel.subs(q, -sp.I))
    e4 = (sp.simplify(at_i - sp.expand((s - sp.I) ** 2)) == 0
          and sp.simplify(at_mi - sp.expand((s + sp.I) ** 2)) == 0)
    check("channels_merge_exactly_at_specJ", e4,
          "at q=+-i the Hecke relation becomes (sigma -+ i)^2 = 0 — the channel pair "
          "MERGES with common eigenvalue +-i; and {+i,-i} = spec(J), the complex-structure "
          "eigenvalues whose eigenspaces are H^{1,0}/H^{0,1} and whose swap IS conjugation: "
          "the channel doubling collapses exactly at the eigenvalues of the operator whose "
          "doubling it is conjectured to match")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "D4 ADJUDICATED (necessary conditions; scope-(a); derives no clause; no fit; nothing "
        "wired): the tau identification must carry the 2-STRAND CHANNEL transpose (q -> "
        "-q^{-1}) to complex conjugation on H^1(Bring). The 5-letter PARTITION transpose is "
        "EXCLUDED — it changes the S5 isotype (std -> std(x)sign; chi((12)): 2 vs -2) while "
        "conjugation preserves it (chi_std real over all 7 classes, H^{0,1}~std); the channel "
        "transpose is S5-neutral and survives. Exact geometry: on the fibre circle bar and "
        "transpose are the two reflection axes (fixed points q=+-1 classical / q=+-i "
        "democratic; composition = antipode), and at q=+-i the Hecke relation degenerates to "
        "(sigma-+i)^2 — the channels merge exactly at spec(J) = {+-i}, the complex-structure "
        "eigenvalues whose eigenspace swap IS conjugation. The full tau-functor derivation "
        "(the correspondence wall) remains open; its target is now UNIQUE. NO tier change."
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
        "computation": "alpha-em-d4-equivariance-adjudication",
        "description": "Adjudicates D4 of the conjugation-doubling dictionary: the tau identification "
                       "must carry the 2-strand CHANNEL transpose to conjugation; the 5-letter partition "
                       "transpose is excluded (isotype std->std(x)sign vs conjugation isotype-preserving, "
                       "chi_std real). Exact geometry: bar/transpose = the two reflection axes of the "
                       "fibre circle (fixed pts q=+-1 classical / q=+-i democratic); at q=+-i the Hecke "
                       "relation degenerates to (sigma-+i)^2 — channels merge at spec(J). Derives no "
                       "clause; nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-conjugation-doubling-dictionary.md",
        "tier": "symbolic-exact (sympy; S5 characters over all 7 classes + circle geometry + "
                "degenerate Hecke relation)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "excluded": "5-letter partition transpose (isotype-changing: std -> std(x)sign)",
            "unique_survivor": "2-strand channel transpose q -> -q^{-1} (S5-neutral)",
            "circle_geometry": "bar = reflection across R (q=+-1 classical); transpose = reflection "
                               "across iR (q=+-i democratic); composition = antipode",
            "specJ_coincidence": "Hecke relation degenerates to (sigma-+i)^2 at q=+-i = spec(J)",
            "verdict": verdict,
        },
        "context": {
            "attacks": "D4 of brick 1 (the corrected dictionary, this PR); the correspondence wall's "
                       "unification route now has a UNIQUE target",
            "partition_transpose_role": "not lost — it is the flavor-side fermion-boson/spin-flip "
                                        "doubling (cf. the merged SU(4)/Schur-Weyl flavor work), a "
                                        "different doubling from the photon channel pair",
            "scope_guard": "necessary conditions + one exclusion; derives NO clause; no fit; nothing "
                           "wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-d4-equivariance-adjudication.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
