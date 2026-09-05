"""W_λ keystone — Identity I proof-structure scope + W_λ q-Plancherel cyclotomic probe.

Two coupled questions for the s5-so3 W_λ keystone (docs/coordination/s5-so3-keystone.md):

(A)/(B) IDENTITY I  M(n) = (1/n!) Σ_{λ⊢n} (f^λ)² · (Σ_{c∈λ} h_c²) = n(3n−1)/2.
    The W_λ q₀-free defect sub-target 144·C(n) carries Identity I as its ONE
    representation-theoretic input; the ledger flags its proof as "needs SYT-dimension /
    hook-length infrastructure not in Mathlib." This probe SCOPES that: it verifies the
    identity and decomposes the proof to determine whether it reduces to (i) RSK
    `Σ_λ (f^λ)² = n!` + (ii) ELEMENTARY hook/arm/leg/content identities (Lean-feasible), or
    whether it genuinely needs the full hook-length FORMULA `f^λ = n!/∏ h_c` (research-grade).
    Key lever tested: the Plancherel content-moment `E[Σ_c content(c)²] = C(n,2)` (Kerov), and
    whether `E[Σ_c h_c²]` reduces to content moments + RSK.

(C) W_λ  = d_q(λ)²/[n]_q!  (Ocneanu / q-Plancherel measure — the OPEN keystone object).
    TEST the candidate q-Plancherel normalization `Σ_λ d_q(λ)² = [n]_q!` (the would-be q-analog
    of `Σ (f^λ)² = n!`), then extract the cyclotomic / Habiro structure of the W_λ family with
    the PR #2899 method, so the colored-Σ(2,3,5)-WRT ↔ W_λ bridge can be checked at the right
    (λ-resolved) granularity.

    RESULT: the identity is FALSE for every n ≥ 2 — symbolically in q, not merely numerically.
    `sp.simplify(Σ_λ d_q² − [n]_q!) == 0` holds at n = 1 and fails at n = 2..6; the ratio at
    n = 2 is `2q/(q²+1)`, which is 1 only at q = 1. The assertion below therefore FAILS
    (computed False, expected True) and has always been recorded as failing; what was wrong was
    this docstring and the witness description, which said "verified". The q-deformation breaks
    the Burnside identity and no q-integer convention restores it; the correct q-lift replaces
    ONE factor, not both — `Σ_λ f^λ q^{−κ_λ} dim_q(λ) = [n]_q!`, sorry-free in
    `QOU/MathlibExt/NormalizedSumUnconditional.lean`. Consequence: `Σ_λ W_λ = c_n ≠ 1`, with
    c_n = 0.9946/0.9874/0.9822/0.9822/0.9911/1.0124/1.0506/1.1109 at n = 2..9 (proton q₀).
    Bean qou-uk8o; docs/audits/2026-09-04-plancherel-convention-gap.md.

No fit; sympy symbolic in q + exact rationals; (a)/(b)-scoped per AGENTS.md.
"""
import json, os, sys
from fractions import Fraction
from math import comb, factorial

sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp

# Shared cached symmetric quantum-dim machinery (bean z3a2; PR #2952): q, qfact, dim_q.
# The classical SYT/hook combinatorics (f_lambda, hook, conj, …) + list-form partitions stay
# local — different hook/leg arg order, and the W_λ witness keys embed list-form partitions, so
# dim_q (which needs a hashable tuple) is called as dim_q(tuple(lam)).
from young_qdim import q, qfact, dim_q  # noqa: E402,F401


# ---------- Young-diagram combinatorics (classical) ----------
def partitions(n):
    if n == 0:
        yield []
        return
    for first in range(n, 0, -1):
        for rest in partitions(n - first):
            if not rest or rest[0] <= first:
                yield [first] + rest


def conj(lam):
    if not lam:
        return []
    return [sum(1 for r in lam if r > c) for c in range(lam[0])]


def cells(lam):
    return [(i, j) for i, row in enumerate(lam) for j in range(row)]


def arm(lam, i, j):
    return lam[i] - j - 1


def leg(lam, cj, i, j):
    return cj[j] - i - 1


def hook(lam, cj, i, j):
    return arm(lam, i, j) + leg(lam, cj, i, j) + 1


def content(i, j):
    return j - i


def f_lambda(lam):
    """SYT count via the hook-length formula f^λ = n!/∏ h_c (used only to FORM the identity;
    the scoping question is whether the *proof* of Identity I can avoid this)."""
    n = sum(lam)
    cj = conj(lam)
    prod = 1
    for (i, j) in cells(lam):
        prod *= hook(lam, cj, i, j)
    return factorial(n) // prod


# ---------- (A) verify Identity I ----------
def sum_h2(lam):
    cj = conj(lam)
    return sum(hook(lam, cj, i, j) ** 2 for (i, j) in cells(lam))


def two_M(n):
    """(1/n!) Σ_λ (f^λ)² Σ_c h_c²  as an exact Fraction."""
    n_fact = factorial(n)
    tot = Fraction(0)
    for lam in partitions(n):
        tot += Fraction(f_lambda(lam) ** 2 * sum_h2(lam), n_fact)
    return tot


identity_I = {}
for n in range(2, 15):
    val = two_M(n)
    target = Fraction(n * (3 * n - 1), 2)
    identity_I[n] = (val, target, val == target)
identity_I_holds = all(v[2] for v in identity_I.values())

# ---------- (B) proof-structure: is a non-HLF route available? ----------
# Plancherel expectation E[g] := (1/n!) Σ_λ (f^λ)² g(λ).  Test the content-moment lever:
#   E[Σ_c content²] =? C(n,2)   (Kerov; provable from JM-element second moment, NO hook formula)
#   E[Σ_c h_c²]     =  n(3n−1)/2 (Identity I)
# and the elementary single-diagram pieces of Σh² = Σ(a+l+1)².
def sum_content2(lam):
    return sum(content(i, j) ** 2 for (i, j) in cells(lam))


def plancherel_E(n, g):
    nf = factorial(n)
    return sum(Fraction(f_lambda(lam) ** 2 * g(lam), nf) for lam in partitions(n))


E_content2 = {n: plancherel_E(n, sum_content2) for n in range(2, 13)}
E_h2 = {n: plancherel_E(n, sum_h2) for n in range(2, 13)}
content2_eq_binom = all(E_content2[n] == Fraction(comb(n, 2)) for n in E_content2)
# Does E[Σh²] − E[Σcontent²] have a clean closed form?  (n(3n−1)/2 − C(n,2) = n²)
diff_is_n2 = all(E_h2[n] - E_content2[n] == Fraction(n * n) for n in E_content2)

# single-diagram identity (purely elementary, Lean-feasible, NO Plancherel):
#   Σ_c h_c = n + Σ_i C(λ_i,2) + Σ_j C(λ'_j,2)
def sum_h(lam):
    cj = conj(lam)
    return sum(hook(lam, cj, i, j) for (i, j) in cells(lam))


sum_h_elementary_ok = all(
    sum_h(lam) == sum(lam) + sum(comb(r, 2) for r in lam) + sum(comb(c, 2) for c in conj(lam))
    for n in range(1, 11) for lam in partitions(n)
)

# ---------- (C) W_λ = d_q(λ)²/[n]_q! : q-Plancherel + cyclotomic structure ----------
# qint / qfact / dim_q now come from young_qdim (imported above). dim_q is lru_cached and needs
# a hashable partition, so it is called as dim_q(tuple(lam)) on the local list-form partitions.
def W_lambda(lam):
    return sp.cancel(sp.together(dim_q(tuple(lam)) ** 2 / qfact(sum(lam))))


# CANDIDATE q-Plancherel normalization  Σ_λ d_q(λ)² = [n]_q!  (would give Σ_λ W_λ = 1).
# It is FALSE for every n ≥ 2 — symbolically, see the (C) note in the module docstring. The
# flag below is kept and reported as measured; do not "fix" it to True. Bean qou-uk8o.
qplanch = {}
for n in range(1, 7):
    lhs = sp.cancel(sp.together(sum(dim_q(tuple(lam)) ** 2 for lam in partitions(n))))
    qplanch[n] = bool(sp.simplify(lhs - qfact(n)) == 0)
qplanch_ok = all(qplanch.values())

# cyclotomic structure of the per-λ W_λ at small n (denominators → Φ_d, the Habiro habitat)
W_examples = {}
for n in [3, 4]:
    for lam in partitions(n):
        num, den = sp.fraction(sp.together(W_lambda(lam)))
        W_examples[f"n{n}:{lam}"] = {"W": str(sp.factor(W_lambda(lam))),
                                     "den_factored": str(sp.factor(den))}

results = {
    "identity_I": {str(n): {"value": str(v[0]), "target_n(3n-1)/2": str(v[1]), "match": v[2]}
                   for n, v in identity_I.items()},
    "identity_I_holds_n2_14": identity_I_holds,
    "E_content2_eq_binom_n_2": content2_eq_binom,
    "E_h2_minus_E_content2_eq_n_squared": diff_is_n2,
    "sum_h_elementary_decomposition_ok": sum_h_elementary_ok,
    "qplancherel_sum_dq2_eq_qfact": qplanch_ok,
    "W_lambda_examples": W_examples,
}

# ---- proof-route verdict for the Lean infra scope ----
if content2_eq_binom and diff_is_n2:
    route = (
        "NON-HLF ROUTE EXISTS (Lean-feasible). Identity I = E[Σ_c h_c²] = n(3n−1)/2 DECOMPOSES as "
        "E[Σ_c content²] + n²  with  E[Σ_c content²] = C(n,2)  (Kerov content second moment, "
        "provable from the Jucys–Murphy element Σ X_i² in Z(ℂ[S_n]) — RSK + center-of-group-algebra, "
        "NO hook-length FORMULA). The residual E[Σ h² − Σ content²] = n² is the Plancherel mean of "
        "an elementary arm/leg/content combination. So the infra needed is: (1) RSK `Σ(f^λ)²=n!` "
        "(note: its q-form `Σ d_q²=[n]_q!` is FALSE for n ≥ 2, measured here symbolically, so "
        "only the CLASSICAL RSK identity is available), (2) the JM/content second-moment, (3) the "
        "single-diagram elementary hook identity `Σ_c h_c = n + Σ_i C(λ_i,2) + Σ_j C(λ'_j,2)` "
        f"(verified elementary: {sum_h_elementary_ok}) extended to the squared form. The full "
        "hook-length FORMULA is NOT required for Identity I — the ledger's 'needs HLF' scope can be "
        "narrowed to the content-moment + elementary-hook infra."
    )
else:
    route = (
        "HLF-dependent (or richer): the clean content-moment decomposition did NOT close "
        f"(E[Σcontent²]=C(n,2)? {content2_eq_binom}; E[Σh²]−E[Σcontent²]=n²? {diff_is_n2}). "
        "Identity I likely needs the full hook-length formula or a deeper Plancherel argument; "
        "formalize conditionally (§3b-cond) on an HLF class."
    )

witness = {
    # "computation" is derived by wrap_legacy from the name argument (Copilot review)
    "description": (
        "Scopes the Lean infra for Identity I (the one RT input of the W_λ 144·C(n) defect "
        "sub-target): verifies M(n)=n(3n−1)/2 (n=2..14) and tests whether the proof reduces to "
        "RSK + content-moment + elementary hook identities (no hook-length FORMULA). Also verifies "
        "TESTS the candidate q-Plancherel normalization Σ_λ d_q²=[n]_q! — which is FALSE for "
        "every n ≥ 2, symbolically in q (the assertion is recorded as failing) — and extracts "
        "the W_λ cyclotomic/Habiro structure for the colored-Σ(2,3,5)-WRT bridge. Bean qou-uk8o."
    ),
    "discipline": "no fit; exact rationals + sympy symbolic in q; (a)/(b)-scoped.",
    "auditOnly": "docs/coordination/s5-so3-keystone.md",
    "results": results,
    "leanInfraRouteVerdict": route,
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
# bean qou-srvu. Every flag below is an EXACT sympy identity
# (`sp.simplify(lhs - rhs) == 0`), computed and printed and left in `data`, so
# `save()` emitted `allPassed: true` over an EMPTY assertions list -- green
# while asserting nothing. No threshold is introduced: these are symbolic
# zeros over Q(q) and exact combinatorial equalities, not tolerances, so
# nothing here is a float64 comparison.
_b = WitnessBuilder.wrap_legacy(
    "wlambda-identity-i-structure-probe", witness, script_path=__file__, engine="sympy",
)
_b.add_assertion("identity_I_holds_n2_14",
                 computed=bool(identity_I_holds), expected=True,
                 source="Identity I: M(n) = n(3n-1)/2 for every n = 2..14")
_b.add_assertion("E_content2_eq_binom_n_2",
                 computed=bool(content2_eq_binom), expected=True,
                 source="E[sum content^2] = C(n,2), exactly")
_b.add_assertion("E_h2_minus_E_content2_eq_n_squared",
                 computed=bool(diff_is_n2), expected=True,
                 source="E[sum h^2] - E[sum content^2] = n^2, exactly")
_b.add_assertion("sum_h_elementary_decomposition_ok",
                 computed=bool(sum_h_elementary_ok), expected=True,
                 source="the hook-length sum admits the stated elementary decomposition")
_b.add_assertion("qplancherel_sum_dq2_eq_qfact",
                 computed=bool(qplanch_ok), expected=True,
                 source=("CANDIDATE q-Plancherel normalisation sum_lambda "
                         "d_q(lambda)^2 = [n]_q! for n = 1..6, tested as a "
                         "symbolic identity in q. It HOLDS at n=1 and FAILS "
                         "for every n >= 2 (ratio at n=2 is 2q/(q^2+1)), so "
                         "sum_lambda W_lambda = c_n != 1. This assertion is "
                         "EXPECTED-TRUE and measured FALSE on purpose: it is "
                         "the corpus's own detector for the defect recorded "
                         "in docs/audits/2026-09-04-plancherel-convention-"
                         "gap.md. Do not 'fix' it by lowering expected."))
out = _b.save()

print(f"(A) Identity I  M(n)=n(3n−1)/2  for n=2..14: {identity_I_holds}")
print(f"(B) E[Σ content²] = C(n,2): {content2_eq_binom}")
print(f"    E[Σ h²] − E[Σ content²] = n²: {diff_is_n2}")
print(f"    Σ_c h_c = n + Σ C(λ_i,2) + Σ C(λ'_j,2) (elementary): {sum_h_elementary_ok}")
print(f"(C) q-Plancherel  Σ_λ d_q² = [n]_q!: {qplanch_ok}")
print(f"\nLEAN INFRA ROUTE:\n  {route}")
print(f"\nwitness -> {out}")
