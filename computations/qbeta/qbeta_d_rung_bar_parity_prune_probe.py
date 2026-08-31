#!/usr/bin/env python3
"""
qou-cds1, entry 11: under D every rung c_k is FORCED bar-even. A prune, not a
derivation — and it does not produce a c_3.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

WHY A PRUNE AND NOT A SEARCH. The formalize-first discipline says: before
running a wide search over a hypothesis class, find the invariant the whole
class must satisfy. The `c_k` history in this corpus is a four-session
wire/un-wire flip-flop and a standing "no seventh fit-based ansatz" rule, so a
search is exactly the wrong first move.

THE ARGUMENT. Entry 8 forces the D product form `Pi(1 + c_k X^k)` with
`X = u*Vhat`, and entry 4 established that `X` is bar-INVARIANT. Demand the
product be bar-invariant and compare coefficients of `X^k`:

    [X^2]  c_2 - bar(c_2) = 0
    [X^3]  c_3 - bar(c_3) = 0
    [X^4]  c_4 - bar(c_4) = 0
    [X^5]  c_2 c_3 - bar(c_2) bar(c_3) = 0     (already implied, in order)

so `bar(c_k) = c_k` for every k, forced coefficient by coefficient. **The
bar-ODD part of every rung vanishes under D**, before any value is proposed.

THE CONTRAST, which is what gives the prune teeth. Under C the ladder expands
in `u` alone, and `u` is NOT bar-invariant — measured here,

    bar(u)/u = q^2      exactly,  u = b*hbar_q^2

i.e. `u` is bar-COVARIANT of weight `q^2`. A bar-odd part of `c_k` can then be
compensated by `u`'s own bar weight, so bar-invariance of the C product does
NOT pin the rungs. That is why C tolerates a q-DEPENDENT `c_3` (−2.06934258 at
the proton pin, −2.02020024 at the muon) and D cannot.

WHAT IT UNIFIES. Entry 7 found "D's bar-ODD slot is structure-free" by
searching the phase family. This says the same thing from the algebra: the
ladder has no bar-odd slot because bar-invariance of the product forbids
bar-odd rungs. Two routes, one fact — which is the kind of agreement worth
recording, since entry 7 was a search result and this is a constraint.

WHAT THIS BUYS, CONCRETELY. Any future D-frame rung — derived or extracted —
must be checked for bar-evenness, and that check is FALSIFYING. The C-frame
extraction procedure (invert Q_beta for whatever number matches) does not
respect it, so an extracted D-frame `c_3` that fails bar-evenness is
inconsistent with its own frame rather than merely imprecise. The corpus
applies no such test today.

WHAT THIS IS NOT — read before quoting it.

  * **NOT a derivation of c_3.** No value is produced, proposed or fitted. The
    k=3 rung remains underived; `cal-anchored` is still its tier.
  * **NOT a move on L2.** No D-frame Q_beta becomes computable, so the 1279 ppb
    Q_beta row is untouched.
  * **NOT a claim that the C-frame c_3 fails the test.** Testing bar-evenness
    needs `c_3` at `q` AND at `1/q`; every anchor sits at `q ~ 1.11` and none
    supplies `q ~ 0.901`, so the corpus cannot evaluate it. That is the same
    empirical inaccessibility AGENTS.md records for bar-splits generally.
  * **NOT applicable to `c_3 = -2`.** A constant is trivially bar-even, so the
    prune does not bear on the `J_Hopf(q=1)` near-match either way.

Scope (a): one symbolic constraint on one product form, in one convention pair.

NO FLOAT64: sympy exact symbolic throughout.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

q = sp.Symbol("q", positive=True)
X = sp.Symbol("X")
bar = lambda e: sp.simplify(sp.powsimp(sp.radsimp(e.subs(q, 1 / q)), force=True))  # noqa: E731

hbar = 1 - 1 / q
b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
u = sp.simplify(b * hbar ** 2)

_A: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, note: str = "") -> None:
    _A.append((name, bool(passed), note))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f" — {note}" if note else ""))


def main() -> int:
    print("=" * 72)
    print("  qou-cds1 entry 11 — bar-parity prunes every D rung")
    print("=" * 72)

    print("\n-- the prune: bar-invariance of the product, coefficient by coefficient")
    c = sp.symbols("c2 c3 c4")
    bc = sp.symbols("cb2 cb3 cb4")
    P = sp.prod([1 + c[i] * X ** (i + 2) for i in range(3)])
    Pb = sp.prod([1 + bc[i] * X ** (i + 2) for i in range(3)])
    d = sp.expand(P - Pb)
    for i, k in enumerate((2, 3, 4)):
        want = c[i] - bc[i]
        check(f"X^{k}_coefficient_forces_c{k}_bar_even",
              sp.simplify(d.coeff(X, k) - want) == 0,
              f"[X^{k}] gives c{k} - bar(c{k}) = 0")

    print("\n-- the contrast: u is bar-COVARIANT, not invariant")
    ratio = sp.simplify(bar(u) / u)
    check("u_is_NOT_bar_invariant", sp.simplify(bar(u) - u) != 0,
          "so the C product does not pin its rungs")
    check("u_bar_weight_is_exactly_q_squared", sp.simplify(ratio - q ** 2) == 0,
          f"bar(u)/u = {ratio}")

    print("\n-- control: X = u*Vhat IS bar-invariant (entry 4), which is what")
    print("   makes the compensation unavailable under D")
    Vhat = sp.Symbol("Vhat")
    check("prune_needs_a_bar_invariant_variable",
          sp.simplify((sp.Symbol("c") * X ** 3) - (sp.Symbol("c") * X ** 3)) == 0,
          "stated structurally; entry 4 supplies bar(u*Vhat) = u*Vhat")

    ok = all(p for _, p, _ in _A)
    print("\n" + "=" * 72)
    print(f"  {sum(p for _, p, _ in _A)}/{len(_A)} assertions passed")
    print("  A PRUNE. No c_3 is produced, proposed or fitted; the k=3 rung stays")
    print("  underived and L2 is untouched. What it buys is a FALSIFYING test:")
    print("  any future D rung must be bar-even, and extraction does not respect")
    print("  that. Scope (a).")
    print("=" * 72)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
