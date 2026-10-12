#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
α_EM per-loop measure — the count-carrying object probe (sharpened #3889 redirect).

CONTEXT (the exact task #3889 handed forward)
----------------------------------------------
The α_EM per-loop measure factorises as `1/(π·b₁) = 1/(8π)` with
`b₁ = dim H¹(M_Bring) = 2g = 8` (genus-4 Bring surface, `Jac(Bring) ~ E⁴`).

- #3834 proved the bare-count NUMERATOR is area-free and DERIVED:
  `ζ_{Δ₁}(0) = −b₁ = −8`, the Epstein-zeta `−1/s` residue, covolume-independent.
- #3870 / #3882 ruled OUT every flat-torus determinant / Ray–Singer torsion object
  as the reciprocal measure (extensive in b₁, or a covolume — never `1/b₁`).
- #3889 tested the RT/WRT modular-S-matrix total quantum dimension `D = √(Σd_i²)`,
  `S_{00} = 1/D`, as the reciprocal `1/(total-count)` democratic average. The genuine
  Σ(2,3,5) icosahedral / Fibonacci MTC gave `Σd_i² = (5+√5)/2 ≈ 3.618 ≠ 8` (too small,
  only 2 primary fields). It handed forward the SHARPENED redirect:

    "find a count-carrying category whose total quantum dimension Σd_i² = 8, DERIVED
     from the genus-4 Bring topology (b₁ = 8), NOT fitted to 8."

THE DECISIVE QUESTION (per candidate)
-------------------------------------
Is `Σd_i² = 8` a DERIVED consequence of Bring topology, or a MATCH (a level / group /
labelling chosen so |object| = 8)? `Σd_i² = 8` is trivially EASY to fit — any order-8
abelian group, ℤ₂³, U(1)_8, or "8 copies of anything" gives it. The entire value is
whether 8 is FORCED by the topology or hand-picked to match b₁.

Anti-laundering (AGENTS.md §"Axiomatization is NOT a Proof", §"Before declaring
refuted"/(a)-(b) classification, α_EM standing rule, Subgoal-2 "open for all but
anti-fit STILL STANDS"): NO CODATA read; NO convention tuned toward 8; an honest
NEGATIVE (no natural object forces Σd_i² = 8) is a GOOD outcome and is preferred over
a fitted 8. We distinguish `2g = 8` (a genuine topological Betti count) from
`|discriminant group| = 8` (which depends on the lattice/level and is NOT 2g).

CANDIDATES ENUMERATED
---------------------
(A) The abelian anyonic theory of the Jacobian = the discriminant form of
    `(H¹(Bring;ℤ), intersection form)`. For a closed oriented genus-g surface the
    intersection (cup-product) form is UNIMODULAR by Poincaré duality — the standard
    symplectic lattice `⊕^g H`, `H = [[0,1],[-1,0]]`, det = 1. Its discriminant group
    `A_L = L*/L` is TRIVIAL (|A_L| = 1) ⇒ the abelian MTC has ONE simple object,
    `Σd_i² = 1`, NOT 8. FORCED, and forces 1 — kills the naive abelian-Jacobian route.

(B) A finite level-k / U(1)_k lattice (WZW abelian) theory on H¹. `|group| = k` anyons,
    all d_i = 1, `Σd_i² = k`. Reaching 8 needs level k = 8 — but the Jacobian carries a
    PRINCIPAL polarization (unimodular form ⇒ "level 1"), so nothing forces k = 8. FIT.

(C) The 2g = 8 harmonic 1-forms taken directly as a "count" (equivalently the four
    Z₅-isotypical characters χ₁⊕χ₂⊕χ₃⊕χ₄ of H¹, each 2-dim → 8; or 4 complex forms +
    4 conjugates). Declaring "8 objects, each d = 1" gives `Σd_i² = 8` — but this is
    literally b₁ RELABELLED as an object count; there is no fusion / modular structure,
    no new content. REPRODUCES 8 TRIVIALLY = relabelling b₁.

(D) A Drinfeld-double / group-theoretical category from S₅ or 2I (binary icosahedral).
    `D(G)` has `Σd_i² = |G|²`. `Σd_i² = 8` would need e.g. the metric group ℤ₂³
    (8 anyons, Σ = 8), or `D(D₄)` (=64) no, `D(ℤ₂)` (=4) no. S₅ (order 120 = 2³·3·5)
    has NO natural order-8 QUOTIENT; the order-8 Sylow-2 (dihedral D₄) is a SUBGROUP,
    and picking it (or ℤ₂³) to match 8 is a choice, not forced. FIT.

CONTROLS
--------
- unimodularity of the genus-g intersection form ⇒ |disc| = 1 (Smith normal form all 1s);
- 2g = 8 for Bring (g = 4);
- the icosahedral Σd_i² = (5+√5)/2 ≈ 3.618 ≠ 8 (cross-check vs #3889).

PRE-REGISTERED KILL CRITERION
-----------------------------
If every natural object either gives `Σd_i² ≠ 8` (like the unimodular-Jacobian |disc| = 1)
or requires CHOOSING a level/group/labelling to hit 8, then the count-carrying object is
NOT forced ⇒ scope-(a) NEGATIVE: "1/b₁ from a categorical Σd_i² is not derived; b₁ = 8
enters as the Betti number directly (the #3834 ζ(0) = −b₁ count), not through a
quantum-dimension sum."
"""

from __future__ import annotations

import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
# This producer hand-builds its assertion payload and `json.dump`s it, so
# `Assertion.to_dict` -- where the declared-tolerance guard runs -- is never
# reached, and a re-run would re-emit the float literals and undo PR #5910's
# drain for this file alone. `_tol` routes each DECLARED tolerance through
# that guard; it returns a COMPUTED one unchanged, so those stay floats and
# stay counted by the raw-float64 ratchet. Bean qou-9tqx.
from qou_substrate.witness import declared_tolerance as _tol  # noqa: E402

# ----------------------------------------------------------------------------------
# Bring genus-4 data (fixed topological facts; no fit).
# ----------------------------------------------------------------------------------
GENUS = 4                     # Bring's curve has genus 4
# (Bring's curve is NOT the modular curve X(5), which has genus 0. The library
#  places it relative to X_0(5) -- its period-matrix parameter tau_0 is a
#  distinguished point of X_0(5) -- and identifies one quotient with X_0(50):
#  library/s40879-023-00706-0, sec-003 and sec-011 (Braden--Disney-Hogg).
#  Only g = 4 enters any number below; the naming never did.)
B1 = 2 * GENUS               # b₁ = dim H¹(Bring) = 2g = 8  (a Betti number)
TARGET = 8                    # the count the measure needs, = b₁

results: dict[str, object] = {}
candidates: list[dict[str, object]] = []


# ----------------------------------------------------------------------------------
# CONTROL 1 — the intersection form on H¹(Σ_g;ℤ) is UNIMODULAR (Poincaré duality).
#   Gram = ⊕^g [[0,1],[-1,0]]  (symplectic basis a_i,b_i).  det = 1, Smith all 1s.
#   Discriminant group A_L = L*/L is trivial ⇒ |A_L| = 1.
# ----------------------------------------------------------------------------------
def symplectic_gram(g: int) -> sp.Matrix:
    H = sp.Matrix([[0, 1], [-1, 0]])
    M = sp.zeros(2 * g, 2 * g)
    for i in range(g):
        M[2 * i:2 * i + 2, 2 * i:2 * i + 2] = H
    return M


def discriminant_group(gram: sp.Matrix) -> tuple[int, list[int], int]:
    """|A_L| = |det Gram| ; invariant factors via Smith normal form of the Gram matrix.
    A unimodular form has |det|=1 and all Smith invariants 1 ⇒ trivial disc group (order 1).
    """
    det = int(sp.Integer(gram.det()))
    from sympy.matrices.normalforms import smith_normal_form
    snf = smith_normal_form(sp.Matrix(gram), domain=sp.ZZ)
    invariants = [int(abs(snf[i, i])) for i in range(snf.rows)]
    order = 1
    for d in invariants:
        order *= d
    nontrivial = [d for d in invariants if d != 1]
    return abs(det), nontrivial, order


gram = symplectic_gram(GENUS)
det_abs, disc_invariants, disc_order = discriminant_group(gram)
print("=" * 78)
print("CONTROL 1 — genus-g intersection form is unimodular => trivial discriminant")
print(f"  g = {GENUS}, b1 = 2g = {B1}")
print(f"  Gram = (+)^{GENUS} [[0,1],[-1,0]]  (symplectic basis)")
print(f"  |det Gram|               = {det_abs}   (unimodular <=> 1)")
print(f"  nontrivial Smith factors = {disc_invariants}  (empty <=> trivial disc group)")
print(f"  |discriminant group A_L| = {disc_order}")
assert det_abs == 1, "genus-g intersection form must be unimodular (det +/-1)"
assert disc_order == 1, "unimodular => trivial discriminant group, order 1"
results["control_unimodular_det_abs"] = det_abs
results["control_disc_group_order"] = disc_order

# ----------------------------------------------------------------------------------
# CONTROL 2 — 2g = 8 for Bring.
# ----------------------------------------------------------------------------------
print()
print("CONTROL 2 — Betti number 2g = 8 for the genus-4 Bring surface")
print(f"  2*{GENUS} = {2 * GENUS}   (target count b1 = {TARGET})")
assert 2 * GENUS == TARGET
results["control_2g"] = 2 * GENUS

# ----------------------------------------------------------------------------------
# CONTROL 3 — icosahedral / Fibonacci Sd_i^2 = (5+sqrt5)/2 ~ 3.618 != 8  (cross-check #3889).
# ----------------------------------------------------------------------------------
phi = (1 + sp.sqrt(5)) / 2
ico_sum = 1 + phi ** 2                      # d_i in {1, phi}; Sum = 1 + phi^2 = (5+sqrt5)/2
print()
print("CONTROL 3 — icosahedral (Sigma(2,3,5)) total quantum dimension (from #3889)")
print(f"  Sd_i^2 = 1 + phi^2 = {sp.simplify(ico_sum)} = (5+sqrt5)/2 ~ {float(ico_sum):.6f}")
assert sp.simplify(ico_sum - (5 + sp.sqrt(5)) / 2) == 0
assert abs(float(ico_sum) - 8) > 1.0
results["control_icosahedral_sum_d2"] = float(ico_sum)


# ----------------------------------------------------------------------------------
# CANDIDATE ENUMERATION — Sd_i^2 for each, with forced-vs-fitted verdict.
# ----------------------------------------------------------------------------------
def add_candidate(tag, name, sum_d2, forced, verdict, why):
    equals_8 = (sp.nsimplify(sum_d2) == 8)
    row = {
        "tag": tag,
        "name": name,
        "sum_d2": str(sum_d2),
        "sum_d2_float": float(sum_d2),
        "equals_8": bool(equals_8),
        "count_status": forced,        # "forced" | "fitted" | "relabel"
        "verdict": verdict,
        "why": why,
    }
    candidates.append(row)
    return row


print()
print("=" * 78)
print("CANDIDATE Sd_i^2  TABLE   (forced-vs-fitted is the whole point)")
print("=" * 78)

# (A) Abelian anyonic theory of the Jacobian = discriminant form of the unimodular
#     intersection lattice.  |A_L| = 1 anyon (trivial), Sd_i^2 = 1.
add_candidate(
    "A", "Abelian theory of Jac(Bring) = discriminant form of (H1(Z), intersection)",
    sp.Integer(1), "forced", "KILLS the naive abelian-Jacobian route",
    "The genus-g intersection form is UNIMODULAR (Poincare duality) => discriminant "
    "group A_L=L*/L is TRIVIAL (|A_L|=1). The abelian MTC of a lattice has one simple "
    "object per discriminant element, so Sd_i^2=|A_L|=1, NOT 8. The count IS forced by "
    "topology and the topology gives 1. (2g=8 is the Betti number; |disc|=1 is the "
    "lattice invariant -- they are DIFFERENT numbers, and the metric-group anyon count "
    "is the latter.)",
)

# (B) U(1)_k / level-k abelian lattice theory -- k anyons, Sd_i^2=k.  Needs level 8.
add_candidate(
    "B", "Finite level-k / U(1)_k abelian theory on H1 (level chosen)",
    sp.Integer(8), "fitted", "Sd_i^2=8 only by CHOOSING level k=8",
    "A U(1)_k / rescaled-lattice theory has k anyons (d_i=1), Sd_i^2=k. Hitting 8 needs "
    "k=8. But the Jacobian's polarization is PRINCIPAL (the unimodular form = 'level 1'), "
    "so no level is forced -- least of all 8. Choosing k=8 to match b1 is a fit.",
)

# (C) The 2g=8 harmonic 1-forms / Z5-isotypical chi1+chi2+chi3+chi4 (each 2-dim) as a count.
add_candidate(
    "C", "2g=8 harmonic 1-forms (Z5 chi1+chi2+chi3+chi4, each 2-dim) as d=1 'objects'",
    sp.Integer(8), "relabel", "Sd_i^2=8 TRIVIALLY, but = b1 relabelled (no new content)",
    "Declaring the 8 harmonic 1-forms (or 4 complex (+) 4 conjugate; or the four "
    "2-dim Z5 characters summing to 8) as '8 simple objects d=1' gives Sd_i^2=8 -- but "
    "there is no fusion/braiding/modular structure; it is literally the vector space "
    "dim H1=b1=8 wearing an object-count costume. Reproduces 8 with ZERO new categorical "
    "content -- a relabelling of the Betti number, not a derivation of a Sd_i^2.",
)

# (D) Drinfeld double / group-theoretical from S5 or 2I.  D(G): Sd_i^2=|G|^2.
#     Z2^3 metric group -> 8 anyons Sum=8 (chosen); D(D4) -> 64; no order-8 quotient of S5.
add_candidate(
    "D", "Drinfeld-double / group-theoretical from S5 or 2I",
    sp.Integer(8), "fitted", "Sd_i^2=8 only by CHOOSING Z2^3 / an order-8 subgroup",
    "D(G) has Sd_i^2=|G|^2 (D(Z2)=4, D(D4)=64 -- neither 8). The metric group Z2^3 gives 8 "
    "anyons Sum=8, but Z2^3 is not a Bring invariant. S5 (|S5|=120=2^3*3*5) has NO natural "
    "order-8 QUOTIENT; its order-8 Sylow-2 (dihedral D4) is a SUBGROUP -- and it is only "
    "ONE of eight subgroup classes giving genus-1 quotients (S4,A4,D6,D4,S3,C6,C2^2,C4, "
    "per #2701/E4), so picking the |.|=8 one to match b1 is a fit. 2I (|2I|=120) gives "
    "nothing of order 8 naturally.",
)

for c in candidates:
    fv = {"forced": "FORCED", "fitted": "FITTED", "relabel": "RELABEL"}[c["count_status"]]
    print(f"  ({c['tag']}) {c['name'][:54]:<54}")
    print(f"       Sd_i^2 = {c['sum_d2']:<6}  =8? {str(c['equals_8']):<5}  [{fv}]  -> {c['verdict']}")

# ----------------------------------------------------------------------------------
# VERDICT — kill criterion evaluation.
# ----------------------------------------------------------------------------------
forced_and_8 = [c for c in candidates if c["count_status"] == "forced" and c["equals_8"]]
any_forced_8 = len(forced_and_8) > 0

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print(f"  candidates giving Sd_i^2=8 by a FORCED topological count: {len(forced_and_8)}")
print("  -> (A) forced but gives 1 (unimodular => |disc|=1), NOT 8;")
print("  -> (B),(D) give 8 only by CHOOSING a level/group (fit);")
print("  -> (C) gives 8 but it is b1 RELABELLED (no new categorical content).")
print()
if not any_forced_8:
    print("  PRE-REGISTERED KILL CRITERION MET => scope-(a) NEGATIVE.")
    print("  The count-carrying object is NOT forced: 1/b1 from a categorical Sd_i^2 is")
    print("  NOT derived. b1=8 enters as the Betti number directly (the #3834")
    print("  zeta_{Delta1}(0)=-b1 count), not through a quantum-dimension sum.")
    print()
    print("  CONSOLIDATION: the 1/b1 leg is ALREADY DERIVED as the plain Betti count")
    print("  (#3834/#3831, zeta_{Delta1}(0)=-b1, area-free). Re-routing it through Sd_i^2")
    print("  of an MTC is an unnecessary detour that either reproduces 8 trivially")
    print("  (relabel, candidate C) or fails (A) / fits (B,D). Only 1/pi (archimedean")
    print("  1-loop determinant normalization, #3882) remains genuinely open.")
else:
    print("  A forced Sd_i^2=8 was found -- RE-CHECK for a hidden fit before claiming derivation.")

verdict = "scope-a-NEGATIVE-count-not-forced" if not any_forced_8 else "POSITIVE-recheck-for-fit"
results["verdict"] = verdict
results["any_forced_sum_d2_equals_8"] = any_forced_8

# ----------------------------------------------------------------------------------
# WITNESS
# ----------------------------------------------------------------------------------
def git(*args: str) -> str:
    # Fail-loud: never emit a witness with placeholder ('unknown') provenance —
    # a broken commit SHA / script hash must abort, not silently mislabel.
    return subprocess.check_output(["git", *args], cwd=Path(__file__).resolve().parents[2],
                                   stderr=subprocess.DEVNULL).decode().strip()


here = Path(__file__).resolve()
script_hash = git("hash-object", str(here))[:12]
commit_sha = git("rev-parse", "HEAD")

assertions = [
    {
        "name": "control_intersection_form_unimodular",
        "computed": float(det_abs), "expected": 1.0, "passed": det_abs == 1,
        "tolerance": _tol(0.5),
        "source": "|det((+)^4 [[0,1],[-1,0]])|=1 (Poincare duality => genus-g intersection form unimodular); Smith normal form all 1s => discriminant group A_L=L*/L trivial",
    },
    {
        "name": "abelian_jacobian_theory_gives_one_anyon_not_eight",
        "computed": float(disc_order), "expected": 1.0, "passed": disc_order == 1,
        "tolerance": _tol(0.5),
        "source": "|A_L|=1 => the abelian anyonic theory of Jac(Bring) has ONE simple object, Sd_i^2=1 (FORCED by topology, and forces 1 != 8) -- kills candidate (A)",
    },
    {
        "name": "control_2g_equals_8",
        "computed": float(2 * GENUS), "expected": 8.0, "passed": 2 * GENUS == 8,
        "tolerance": _tol(0.5),
        "source": "b1=2g=8 for genus-4 Bring; this is the Betti NUMBER (distinct from |disc|=1)",
    },
    {
        "name": "control_icosahedral_sum_d2_not_eight",
        "computed": float(ico_sum), "expected": float((5 + sp.sqrt(5)) / 2),
        "passed": abs(float(ico_sum) - 8) > 1.0, "tolerance": _tol(1e-9),
        "source": "Sigma(2,3,5) Sd_i^2=1+phi^2=(5+sqrt5)/2~3.618 != 8 (cross-check vs #3889 genuine S-matrix)",
    },
    {
        "name": "no_natural_object_forces_sum_d2_equals_8",
        "computed": 0.0 if not any_forced_8 else 1.0, "expected": 0.0,
        "passed": not any_forced_8, "tolerance": _tol(0.5),
        "source": "(A) forced->1; (B)/(D) fitted (choose level/group); (C) relabels b1 (no categorical content). No candidate FORCES Sd_i^2=8 by topology => scope-(a) NEGATIVE; 1/b1 already derived as the #3834 Betti count zeta_{Delta1}(0)=-b1; only 1/pi remains open.",
    },
]
all_passed = all(a["passed"] for a in assertions)

witness = {
    "engine": "sympy",
    "engineVersion": f"sympy {sp.__version__}",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "commitSha": commit_sha,
    "assertions": assertions,
    "allPassed": all_passed,
    "computation": "alpha-em-count-carrying-object",
    "scriptFile": "alpha_em_count_carrying_object_probe.py",
    "scriptHash": script_hash,
    "scriptCommitSha": commit_sha,
    "candidates": candidates,
    "description": (
        "Sharpened #3889 redirect: does a count-carrying category whose total quantum "
        "dimension Sd_i^2=8 exist DERIVED from the genus-4 Bring topology (b1=2g=8), or is "
        "8 a FIT? Enumerates the natural candidate objects from the Bring Jacobian and "
        "computes Sd_i^2 EXACTLY for each, tagging the count forced/fitted/relabel. "
        "RESULT -- scope-(a) NEGATIVE: (A) the abelian anyonic theory of Jac(Bring) = the "
        "discriminant form of (H1(Z), intersection form) has |A_L|=1 because the genus-g "
        "intersection form is UNIMODULAR by Poincare duality (Sd_i^2=1, FORCED, and forces "
        "1 != 8 -- kills the naive Jacobian route); (B) a level-k/U(1)_k abelian theory hits "
        "8 only by CHOOSING k=8, but the principal polarization is 'level 1' (fit); (C) the "
        "2g=8 harmonic 1-forms (Z5 chi1+chi2+chi3+chi4) as d=1 objects give 8 TRIVIALLY = b1 "
        "relabelled, zero new categorical content; (D) a Drinfeld-double/group-theoretical "
        "object from S5 or 2I needs Z2^3 or an order-8 subgroup CHOSEN (S5 has no natural "
        "order-8 quotient; D(G) gives |G|^2 in {4,64}, never 8) -- a fit. No natural object "
        "FORCES Sd_i^2=8. CONSOLIDATION: 1/b1 is ALREADY DERIVED as the plain Betti count "
        "(#3834 zeta_{Delta1}(0)=-b1, area-free); the categorical Sd_i^2 detour reproduces 8 "
        "trivially (relabel) or fails -- only 1/pi (archimedean 1-loop, #3882) remains open. "
        "Anti-laundering: no CODATA read; no convention tuned to 8; 2g=8 (Betti) distinguished "
        "from |disc|=1 (lattice); an honest NEGATIVE is the preferred outcome. No alpha_k "
        "wired; no fit; 1/(8pi) stays a phase-4 identification."
    ),
    "contentBlock": "prop:alpha-em-categorical-trace",
    "auditOnly": "docs/audits/2026-07-18-alpha-em-count-carrying-object.md",
    "environment": {
        "python": platform.python_version(),
        "sympy": sp.__version__,
    },
}

out = here.parent / "alpha-em-count-carrying-object.witness.json"
# Provenance stamp (bean qou-4un2): this producer writes its
# witness directly, so nothing else records which script made
# it -- and a re-run of an unstamped producer DELETES the
# scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
from qou_substrate.witness import WitnessBuilder as _WB
import os as _os  # noqa: E402 -- provenance stamp
witness.setdefault("scriptFile", _os.path.basename(__file__))
_WB.stamp_staleness_metadata(
    witness, script_path=__file__, engine=None, q0_anchor=False)
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print()
print(f"witness -> {out}")
print(f"allPassed = {all_passed}")
