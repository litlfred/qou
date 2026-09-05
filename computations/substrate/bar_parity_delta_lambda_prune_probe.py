"""Bar-parity prune of the recorded Delta_lambda ansatz families (T1 of the
toroidal channel-interpolation follow-on, PR #3445).

The Whipple/ladder probes established that the channel-mixing ladder is
bar-EVEN ([d]_{q^{-1}} = [d]_q, whipple_rotation_involution_probe). This
probe grounds the resulting SELECTION RULE for binding/Delta_lambda
closures and applies it, audit-only, to the six recorded failed ansatze
(docs/audits/2026-05-18-delta-lambda-gating-context.md) plus the PR #619
empirical tabulation. NO new ansatz is proposed (Delta_lambda gate).

The rule needs two exact facts beyond ladder bar-evenness:

(1) q-DIMENSIONS ARE BAR-EVEN: dim_q(lambda) is a product of hook brackets
    [h]_q, each bar-invariant. (Verified on the hook multisets of every
    lambda |- n for n = 2, 3.)

(2) TWISTED PARITY OF HECKE CHARACTERS: the bar involution does NOT fix
    characters — it conjugates the partition with a sign,
        chi_lambda(w; q^{-1}) = (-1)^{l(w)} * chi_{lambda'}(w; q),
    verified here by explicit Hoefsmit representations for every irrep of
    H_2 and H_3 on words up to length 3. So a Frobenius-weighted kernel is
    bar-covariant only when it is lambda <-> lambda'-symmetric (up to the
    sign character); a kernel ASYMMETRIC in lambda <-> lambda' without
    weak-sector routing violates the rule.

(3) CONTENT-SUM ANTISYMMETRY: the content sum n(lambda') - n(lambda) is
    ODD under conjugation — so content-linear kernels are bar-ODD in the
    twisted sense and are PRUNED as binding-sector mixing kernels.

Classification (recorded in the witness verdict; scope (a) throughout —
the rule prunes KERNEL PARITY, it does not resurrect or re-refute any
ansatz numerically):

  A  Occam single-support ......... inapplicable (support selector, no kernel)
  B  Frobenius co-Casimir 1/dim_q . bar-EVEN (passes parity; its failure was
                                    numerical — wrong sign, vortex-blind)
  C  Demazure-fibre y*D_w/D_w0 .... NOT GUARANTEED (Demazure / non-symmetric
                                    objects are not bar-covariant in general;
                                    flagged — witness-case check queued)
  D  LP-Plancherel / d_isotypic ... bar-EVEN (dim_q^2-weights; killed by
                                    underdetermination, not parity)
  D' LP-Frobenius / y_lambda costs  CONSTRAINED: admissible only if the cost
                                    is lambda <-> lambda'-symmetric (twisted
                                    parity (2)); the recorded singleton picks
                                    are asymmetric -> pruned as binding kernels
  c  content-monotonic (PR #619) .. bar-ODD by (3) -> PRUNED
  E  crystal/KL (PROBE 4) ......... already pruned (KL positivity); parity
                                    view consistent: the missing chirality
                                    sign is the bar-odd (weak-sector) datum
  F  augmented Markov ............. rule applies as a constraint on any
                                    concrete instantiation (kernel unspecified)
"""
import json
import os
from itertools import product as iproduct

import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

q = sp.symbols("q", positive=True)


def bkt(x):
    return (q**x - q**(-x)) / (q - 1 / q)


# ---------------------------------------------------- (1) dim_q bar-evenness
HOOKS = {
    "(2)": [2, 1],
    "(1,1)": [2, 1],
    "(3)": [3, 2, 1],
    "(2,1)": [3, 1, 1],
    "(1,1,1)": [3, 2, 1],
}
dimq_bar_even = all(
    sp.simplify(sp.prod([bkt(h) for h in hooks]).subs(q, 1 / q)
                - sp.prod([bkt(h) for h in hooks])) == 0
    for hooks in HOOKS.values()
)

# ------------------------------------- (2) twisted parity of Hecke characters
h = q - 1 / q
# Hoefsmit 2x2 block of V_(2,1) in H_3. With sigma_1 = diag(q, -1/q) (first
# tableau has 1,2 in a row), the braid relation fixes the diagonal ORDER of
# the sigma_2 block to (a_{-2}, a_{+2}) — verified numerically before
# committing to the convention (the (a_{+2}, a_{-2}) order fails braid).
a2 = h / (1 - q**(-4))
am2 = h / (1 - q**4)
b = sp.sqrt(a2 * am2 + 1)
M21_s2 = sp.Matrix([[am2, b], [b, a2]])
M21_s1 = sp.diag(q, -1 / q)

hoefsmit_eigen_ok = (
    sp.simplify(M21_s2.trace() - (q - 1 / q)) == 0
    and sp.simplify(M21_s2.det() + 1) == 0
)
braid_ok = sp.simplify(
    M21_s1 * M21_s2 * M21_s1 - M21_s2 * M21_s1 * M21_s2) == sp.zeros(2, 2)

REPS_H3 = {
    "(3)": {1: sp.Matrix([[q]]), 2: sp.Matrix([[q]])},
    "(2,1)": {1: M21_s1, 2: M21_s2},
    "(1,1,1)": {1: sp.Matrix([[-1 / q]]), 2: sp.Matrix([[-1 / q]])},
}
CONJ = {"(3)": "(1,1,1)", "(2,1)": "(2,1)", "(1,1,1)": "(3)"}
WORDS = [[1], [1, 1], [1, 2], [1, 2, 1], [1, 1, 2]]


def char(lam, word, reps):
    m = sp.eye(reps[lam][1].shape[0])
    for i in word:
        m = m * reps[lam][i]
    return sp.simplify(m.trace())


twisted_parity_ok = True
for lam, word in iproduct(REPS_H3.keys(), WORDS):
    lhs = sp.simplify(char(lam, word, REPS_H3).subs(q, 1 / q))
    rhs = sp.simplify((-1) ** len(word) * char(CONJ[lam], word, REPS_H3))
    if sp.simplify(sp.radsimp(lhs - rhs)) != 0:
        twisted_parity_ok = False
        break

# H_2 (lepton level): rho_(2) = [q], rho_(1,1) = [-1/q]
REPS_H2 = {
    "(2)": {1: sp.Matrix([[q]])},
    "(1,1)": {1: sp.Matrix([[-1 / q]])},
}
CONJ2 = {"(2)": "(1,1)", "(1,1)": "(2)"}
twisted_parity_h2_ok = all(
    sp.simplify(char(lam, [1] * k, REPS_H2).subs(q, 1 / q)
                - (-1) ** k * char(CONJ2[lam], [1] * k, REPS_H2)) == 0
    for lam, k in iproduct(REPS_H2.keys(), [1, 2, 3])
)

# --------------------------------------- (3) content-sum antisymmetry
PARTITIONS = {
    "(2)": [(0, 0), (0, 1)],
    "(1,1)": [(0, 0), (1, 0)],
    "(3)": [(0, 0), (0, 1), (0, 2)],
    "(2,1)": [(0, 0), (0, 1), (1, 0)],
    "(1,1,1)": [(0, 0), (1, 0), (2, 0)],
}
CONJ_ALL = {"(2)": "(1,1)", "(1,1)": "(2)", "(3)": "(1,1,1)",
            "(2,1)": "(2,1)", "(1,1,1)": "(3)"}


def content_sum(cells):
    return sum(j - i for (i, j) in cells)


content_antisym_ok = all(
    content_sum(PARTITIONS[lam]) == -content_sum(PARTITIONS[CONJ_ALL[lam]])
    for lam in PARTITIONS
)

assertions = {
    "dimq_bar_even_n2_n3": bool(dimq_bar_even),
    "hoefsmit_block_eigen_trace_det": bool(hoefsmit_eigen_ok),
    "hoefsmit_braid_relation": bool(braid_ok),
    "twisted_parity_H3_all_irreps_words_len_le3": bool(twisted_parity_ok),
    "twisted_parity_H2": bool(twisted_parity_h2_ok),
    "content_sum_antisymmetric_under_conjugation": bool(content_antisym_ok),
}

classification = {
    "A_occam_single_support": "inapplicable — support selector, no mixing kernel",
    "B_frobenius_co_casimir": "bar-EVEN (dim_q hook product) — parity passes; failure was numerical (wrong sign), not parity",
    "C_demazure_fibre": "NOT GUARANTEED — Demazure/non-symmetric objects not bar-covariant in general; flagged, witness-case check queued",
    "D_lp_plancherel_and_d_isotypic": "bar-EVEN (dim_q^2 weights) — parity passes; killed by underdetermination",
    "D_lp_frobenius_costs": "CONSTRAINED — twisted parity chi_l(q^-1)=(-1)^l(w) chi_l'(q) demands lambda<->lambda'-symmetric costs; recorded singleton picks are asymmetric -> pruned as binding kernels",
    "c_content_monotonic_pr619": "bar-ODD (content-sum antisymmetry) -> PRUNED as a binding-sector kernel",
    "E_crystal_kl_probe4": "already pruned (KL positivity); parity-consistent: the chirality sign is the bar-odd weak-sector datum",
    "F_augmented_markov": "constraint on any concrete instantiation (kernel unspecified)",
}

verdict = (
    "BAR-PARITY SELECTION RULE GROUNDED AND APPLIED (audit-only): the "
    "binding/mixing ladder is bar-even, q-dimensions are bar-even, Hecke "
    "characters obey the TWISTED parity chi_lambda(w;q^-1) = (-1)^l(w) "
    "chi_lambda'(w;q) (verified via explicit Hoefsmit reps for all H_2/H_3 "
    "irreps, words to length 3), and content sums are conjugation-odd. "
    "Consequences: content-linear kernels are bar-odd -> pruned; "
    "lambda<->lambda'-asymmetric Frobenius-cost kernels are pruned unless "
    "the asymmetry routes to the weak sector; dim_q-built kernels pass "
    "parity (their failures were numerical, unchanged). SCOPE (a): this "
    "prunes KERNEL PARITY CLASSES for future candidates; it does not "
    "re-litigate any recorded numerical refutation and proposes no new "
    "ansatz (Delta_lambda gate respected)."
)

witness = {
    "computation": "bar_parity_delta_lambda_prune_probe",
    "description": (
        "T1 audit-only sweep: grounds the bar-parity selection rule (ladder "
        "bar-even + twisted character parity + content antisymmetry) and "
        "classifies the recorded Delta_lambda ansatz families by mixing-"
        "kernel bar-parity."
    ),
    "discipline": "no fit; sympy symbolic exact; audit-only classification; (a)-scoped; no new ansatz.",
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "results": {"classification": classification},
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__), "bar-parity-delta-lambda-prune-probe.witness.json")
# Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
# `os.replace` it into position. `open(..., "w")` TRUNCATES before the
# dump runs, so any exception in between leaves the committed witness
# empty or partial -- the shape that emptied 22 witnesses to zero bytes
# in one `producer_importability_audit` run. `os.replace` is atomic on
# POSIX within a filesystem, hence a SIBLING temp file.
_wpath_sidu = out
_wtmp_sidu = str(_wpath_sidu) + ".tmp"
with open(_wtmp_sidu, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

_os_sidu.replace(_wtmp_sidu, _wpath_sidu)
for k, v in assertions.items():
    print(f"  {k}: {'PASS' if v else 'FAIL'}")
print(f"\nallPassed: {witness['allPassed']}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
