#!/usr/bin/env python3
"""
Probe — does the framing-triviality conclusion actually bite?

Support for `QOU/BraidKnot/KeystoneFramingTrivialAtRootsOfUnity.lean`, whose
scope-(b) exclusion reads:

    if the de-opaqued gate `bwS0Concrete = d_q/D` holds at EVERY root of unity,
    then `f · c(λ) = 0`; and if some block has `c(λ) ≠ 0`, then `f = 0`.

`f = 0` is the framing `BWVacuumRowConcrete.lean` itself describes as carrying
"zero Σ(2,3,5) data (reduces to the compact datum — a tautology)". So the
exclusion is only meaningful if the premise `c(λ) ≠ 0` is actually met by the
blocks in play. That is what this checks — the Lean cannot, since `c(λ)` is a
combinatorial fact about specific partitions, not a theorem about all of them.

`c(λ) = contentSum λ = Σ_{cells (i,j)} (j − i)` is the ribbon twist's exponent:
`θ_λ = q^{c(λ)}` (`KeystoneModularTwist.theta`, a zpow with INTEGER exponent —
which is what makes the twist a Laurent monomial and the whole reduction apply).

Self-conjugate blocks have `c(λ) = 0` (contents are antisymmetric under
transpose), so they are exactly the blocks the exclusion does NOT constrain.
The question is whether they are all of them. They are not.

NO WITNESS: integer combinatorics on seven partitions, reproduced by the printed
table; nothing feeds production.

Bean qou-zngd.
"""
from __future__ import annotations

import sys


def content_sum(lam: tuple[int, ...]) -> int:
    """c(λ) = Σ over cells (i,j) of (j − i), 0-indexed."""
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def transpose(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for r in lam if r > j) for j in range(max(lam)))


PARTITIONS_5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]


def main() -> int:
    print("Keystone framing-triviality premise check  (bean qou-zngd)\n")
    print("  theta_lambda = q^c(lambda),  c(lambda) = sum over cells of (j - i)")
    print("  Gate at EVERY root of unity  =>  f * c(lambda) = 0.")
    print("  So the exclusion bites exactly on blocks with c(lambda) != 0.\n")
    print("| lambda |- 5      | c(lambda) | self-conjugate |")
    print("| --------------- | --------: | -------------- |")

    nonzero = 0
    for lam in PARTITIONS_5:
        c = content_sum(lam)
        selfconj = transpose(lam) == lam
        if c != 0:
            nonzero += 1
        print(f"| {str(lam):<15} | {c:>9} | {'yes' if selfconj else 'no':<14} |")

    total = len(PARTITIONS_5)
    print(f"\n  blocks with c != 0 : {nonzero} of {total}")

    # Cross-check the structural reason: c(λ') = −c(λ), so c = 0 on self-conjugates.
    anti = all(content_sum(transpose(l)) == -content_sum(l) for l in PARTITIONS_5)
    selfconj_all_zero = all(content_sum(l) == 0 for l in PARTITIONS_5 if transpose(l) == l)
    print(f"  transpose antisymmetry c(lambda') = -c(lambda) holds : {anti}")
    print(f"  every self-conjugate block has c = 0                 : {selfconj_all_zero}")

    bites = nonzero > 0
    print("\n## Verdict\n")
    if bites:
        print(f"- The premise is met by {nonzero}/{total} blocks, so the exclusion BITES: a gate")
        print("  holding at every root of unity forces f = 0, the tautological framing.")
        print("- The one exempt block is the self-conjugate (3,1,1), where c = 0 and the")
        print("  twist contributes nothing for ANY f. That is a genuine carve-out, not a")
        print("  loophole: a single self-conjugate block cannot carry the Sigma(2,3,5)")
        print("  framing data on its own, since f is one integer shared across blocks.")
        print("- Scope-(b), narrow: excludes the CONCRETE RT/Seifert row S_0lambda*theta^f")
        print("  with an integer-power twist. Says nothing about other constructions of the")
        print("  BW vacuum row, nor about bwS0_eq_hecke under such a construction, nor about")
        print("  the Beasley-Witten localization program itself.")
    else:
        print("- Every block is self-conjugate (c = 0), so the exclusion is empty and the")
        print("  framing is unconstrained. Re-derive before acting on the Lean result.")

    print("\n(no witness by design — integer combinatorics.)")
    return 0 if bites else 1


if __name__ == "__main__":
    sys.exit(main())
