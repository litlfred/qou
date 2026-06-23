#!/usr/bin/env python3
"""option_e_probe4_overturning_afunction_sign.py
================================================

PROBE-4 overturning check — is the KL-positivity prune AIRTIGHT, or only scoped
to *positive* (unsigned) multiplicity sums?

Background (`docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md`):
the target per-block binding chirality is

    Δ_λ = sgn(w_0^{S_{λ'}}) · dim(V_λ)        (mixed-sign: n=3 → 1+/2−, n=6 → 6+/5−)

The prune observes that KL/crystal multiplicities n^w_λ ≥ 0 (KL positivity), so an
UNSIGNED sum Σ_w n^w_λ X_w can supply at most the magnitude |Δ_λ| = dim, never the
sign — concluding the sign "must be supplied exogenously."

Agent-C flagged this as SOUND-BUT-SCOPED: it rules out positive multiplicity sums,
NOT a *forced* signed sum Σ_w ε_w n^w_λ X_w with ε_w = ±1 derived from the Hecke /
cell structure (a Type-B fold / bar-involution / a-grading), which is untouched.

## The forced sign this script tests — Lusztig's a-function parity

A two-sided Kazhdan–Lusztig cell of S_n is indexed by a partition λ, and Lusztig's
a-function is **constant on the cell**: a(w) = a_λ for every w in the cell of V_λ.
So for ANY ε_w = (-1)^{a(w)},

    Σ_w ε_w n^w_λ X_w  =  (-1)^{a_λ} · Σ_w n^w_λ X_w  =  (-1)^{a_λ} · |Δ_λ|,

i.e. a cell-constant forced sign factors straight through the (non-negative) sum.
The question is purely: **does (-1)^{a_λ} equal the target chirality sign?**

For S_n every irreducible is special, so a_λ = b_λ (the b-invariant = the lowest
exponent of the fake degree = the minimal major index over SYT(λ)), and the
classical value is

    a_λ = b_λ = n(λ) = Σ_i (i-1) λ_i = Σ_i C(λ'_i, 2).

But the target sign is sgn(w_0^{S_{λ'}}) = Π_i (-1)^{C(λ'_i,2)} = (-1)^{n(λ)}.

So (-1)^{a_λ} = (-1)^{n(λ)} = the target chirality sign — IDENTICALLY.

## What this script verifies (combinatorics only — no KL engine needed)

  (1) sgn(w_0^{S_{λ'}}) (computed directly from the Young subgroup) == (-1)^{n(λ)}.
  (2) The b-invariant computed INDEPENDENTLY as min_{T∈SYT(λ)} maj(T) == n(λ)
      (confirms a_λ = b_λ = n(λ) is really the fake-degree valuation, not asserted).
  (3) Hence the forced cell-constant sign (-1)^{a_λ} reproduces the target sign
      for every λ; sign-counts match the audit anchors (n=3 → 1+/2−, n=6 → 6+/5−).
  (4) The factorization (cell-constant ε_w pulls out of the non-negative sum) — so
      a FORCED signed multiplicity sum hits the exact mixed-sign Δ_λ.

## Honest verdict (no over-claim)

This does NOT close Δ_λ: the MAGNITUDE |Δ_λ| = dim still requires Σ_w n^w_λ X_w =
dim (open — the prune itself noted the unsigned sum "at best re-derives |Δ_λ|=dim").
And a fair skeptic notes (-1)^{a_λ} and sgn(w_0^{S_{λ'}}) are the same partition-level
sign — so this RELOCATES the sign into the Hecke a-grading (the writhe/framing
channel), it does not conjure new content. The payload is a RE-SCOPING of the prune:
the chirality sign is NOT exogenous — it is the a-function (= b-invariant) parity,
an intrinsic cell invariant. The open problem is the MAGNITUDE, not the sign.
"""
from __future__ import annotations

import json
import pathlib
from itertools import product as iproduct

results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ── partition combinatorics ──────────────────────────────────────────────────
def partitions(n: int, m: int | None = None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, m), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0]))


def n_stat(lam: tuple[int, ...]) -> int:
    """n(λ) = Σ_i (i-1) λ_i."""
    return sum(i * p for i, p in enumerate(lam))


def hook_dim(lam: tuple[int, ...]) -> int:
    """f^λ via the hook-length formula."""
    n = sum(lam)
    conj = conjugate(lam)
    num = 1
    for x in range(2, n + 1):
        num *= x
    denom = 1
    for i, row in enumerate(lam):
        for j in range(row):
            hook = (row - j - 1) + (conj[j] - i - 1) + 1
            denom *= hook
    return num // denom


def sgn_w0_young(lam: tuple[int, ...]) -> int:
    """sgn(w_0^{S_{λ'}}) = Π_i (-1)^{C(λ'_i, 2)} over parts of the conjugate λ'."""
    s = 1
    for part in conjugate(lam):
        if (part * (part - 1) // 2) % 2 == 1:
            s = -s
    return s


# ── independent b-invariant: min major index over SYT(λ) ─────────────────────
def syt_of_shape(lam: tuple[int, ...]):
    """Generate all standard Young tableaux of shape λ as row-tuples of entries."""
    n = sum(lam)
    rows = [[0] * r for r in lam]

    def place(k: int):
        if k > n:
            yield tuple(tuple(r) for r in rows)
            return
        for i, r in enumerate(lam):
            for j in range(r):
                if rows[i][j] != 0:
                    continue
                # cell (i,j) fillable iff left & up neighbours already filled
                if j > 0 and rows[i][j - 1] == 0:
                    continue
                if i > 0 and rows[i - 1][j] == 0:
                    continue
                rows[i][j] = k
                yield from place(k + 1)
                rows[i][j] = 0
                break  # only the first empty cell in this row is a valid corner
    yield from place(1)


def maj(tab) -> int:
    """maj(T) = Σ_{i ∈ Des(T)} i, Des = {i : i+1 is in a strictly lower row}."""
    rowof = {}
    for ri, row in enumerate(tab):
        for v in row:
            rowof[v] = ri
    n = sum(len(r) for r in tab)
    return sum(i for i in range(1, n) if rowof[i + 1] > rowof[i])


def min_maj(lam: tuple[int, ...]) -> int:
    return min(maj(T) for T in syt_of_shape(lam))


# ── (1) target sign identity  sgn(w_0^{S_λ'}) == (-1)^{n(λ)} ──────────────────
print("(1) sgn(w_0^{S_{λ'}}) == (-1)^{n(λ)}  for all λ ⊢ n, n=2..8")
ok1 = True
for n in range(2, 9):
    for lam in partitions(n):
        if sgn_w0_young(lam) != (-1) ** (n_stat(lam) % 2):
            ok1 = False
check("(1) target chirality sign == (-1)^{n(λ)} (n≤8)", ok1)
results["target_sign_is_n_stat_parity"] = ok1


# ── (2) b-invariant: min major index over SYT == n(λ) (independent of n_stat) ─
print("\n(2) b_λ = min_{T∈SYT(λ)} maj(T) == n(λ)   (confirms a_λ = b_λ = n(λ))")
ok2 = True
detail2 = []
for n in range(2, 8):  # SYT enumeration; n≤7 is cheap
    for lam in partitions(n):
        b = min_maj(lam)
        ns = n_stat(lam)
        if b != ns:
            ok2 = False
            detail2.append({"lambda": lam, "min_maj": b, "n_stat": ns})
check("(2) min-maj(SYT) == n(λ) for all λ ⊢ n≤7 (b-invariant verified)", ok2)
results["b_invariant_eq_n_stat"] = {"ok": ok2, "mismatches": detail2}


# ── (3) forced a-function parity reproduces target; sign-counts vs audit ──────
print("\n(3) forced sign (-1)^{a_λ} = (-1)^{n(λ)} reproduces target Δ_λ sign; counts:")
counts = {}
ok3 = True
for n in range(2, 9):
    npos = nneg = 0
    for lam in partitions(n):
        target = sgn_w0_young(lam)
        forced = (-1) ** (n_stat(lam) % 2)   # (-1)^{a_λ}, a_λ = n(λ)
        if target != forced:
            ok3 = False
        if target > 0:
            npos += 1
        else:
            nneg += 1
    counts[n] = (npos, nneg)
    print(f"    n={n}: {npos}+ / {nneg}-")
results["sign_counts"] = {str(k): list(v) for k, v in counts.items()}
check("(3) forced a-parity == target for every λ (n≤8)", ok3)
check("(3) n=3 sign-count is 1+/2- (audit anchor)", counts[3] == (1, 2))
check("(3) n=6 sign-count is 6+/5- (audit anchor)", counts[6] == (6, 5))


# ── (4) factorization demonstration: ε_w cell-constant ⇒ pulls out of the sum ─
print("\n(4) cell-constant ε_w ⇒ Σ_w ε_w n^w_λ X_w = (-1)^{a_λ}·Σ_w n^w_λ X_w")
# Numeric illustration with arbitrary NON-NEGATIVE multiplicities + traces:
#   the signed sum equals the forced sign times the unsigned (magnitude) sum.
import random
random.seed(20260623)
ok4 = True
for n in [3, 6]:
    for lam in partitions(n):
        # toy non-negative multiplicities n^w and traces X_w over a fake cell of size m
        m = hook_dim(lam)  # any positive count of cell elements
        nw = [random.randint(0, 5) for _ in range(m)]
        Xw = [random.uniform(0.1, 3.0) for _ in range(m)]
        eps = (-1) ** (n_stat(lam) % 2)        # cell-constant forced sign
        signed = sum(eps * a * b for a, b in zip(nw, Xw))
        unsigned = sum(a * b for a, b in zip(nw, Xw))
        if abs(signed - eps * unsigned) > 1e-9:
            ok4 = False
check("(4) cell-constant forced sign factors through the non-negative sum", ok4)
results["factorization_holds"] = ok4


all_passed = all(ok for _, ok in asserts)
verdict = (
    "PROBE-4 IS SCOPED, NOT AIRTIGHT (re-scoping, no closure). The Δ_λ chirality "
    "sign sgn(w_0^{S_{λ'}}) equals (-1)^{n(λ)}, and n(λ) is the b-invariant (min "
    "major index over SYT, verified independently) = the Lusztig a-function value "
    "a_λ on the two-sided cell of V_λ (a_λ=b_λ in type A, all irreps special). "
    "Since the a-function is CONSTANT on cells, the FORCED signed multiplicity sum "
    "Σ_w (-1)^{a(w)} n^w_λ X_w = (-1)^{a_λ}·Σ_w n^w_λ X_w reproduces the exact "
    "mixed-sign target (n=3→1+/2-, n=6→6+/5-). So the prune correctly kills "
    "POSITIVE (unsigned) sums but NOT a forced a-graded signed sum: the chirality "
    "sign is the a-function/b-invariant parity, an intrinsic Hecke-cell invariant, "
    "NOT exogenous. CAVEATS (no over-claim): (a) this does NOT close Δ_λ — the "
    "MAGNITUDE Σ_w n^w_λ X_w = dim is still open; (b) (-1)^{a_λ} and sgn(w_0^{S_λ'}) "
    "are the same partition-level sign, so this RELOCATES the sign into the a-grading "
    "(writhe/framing channel), giving a derivation target rather than new content. "
    "Net: re-scope the prune from 'the sign must be exogenous' to 'the sign IS the "
    "a-function parity; the open problem is the magnitude, not the sign.'"
)
print("\n" + ("ALL PASSED" if all_passed else "SOME FAILED"))
print("VERDICT:", verdict)

witness = {
    "computation": "option_e_probe4_overturning_afunction_sign",
    "description": (
        "PROBE-4 overturning check: tests whether the KL-positivity prune is airtight "
        "or only scoped to unsigned multiplicity sums. Finds the Δ_λ chirality sign = "
        "(-1)^{n(λ)} = Lusztig a-function / b-invariant parity (verified via min-maj "
        "over SYT), a cell-constant Hecke invariant that factors through the "
        "non-negative multiplicity sum — so a FORCED signed sum reproduces the mixed-sign "
        "target. Re-scopes the prune; does NOT close Δ_λ (magnitude still open)."
    ),
    "discipline": "formalize-first; no fit; exploratory probe; audit-only; does NOT wire; magnitude stays open",
    "auditOnly": "docs/audits/2026-06-23-option-e-probe4-overturning-afunction-sign.md",
    "results": results,
    "assertions": {name: ok for name, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
out = pathlib.Path(__file__).resolve().parents[3] / "computations" / "probes" / "option-e-probe4-overturning-afunction-sign.witness.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
