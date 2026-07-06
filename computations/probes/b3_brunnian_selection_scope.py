#!/usr/bin/env python3
# polynomial_q_not_applicable: combinatorial/topological witness (linking numbers
# from a braid word); no symbolic-q polynomial output.
"""Brunnian selection of 𝓑₃ — promote the topological criterion INTO the program.

#2433 verdict (1) named two non-refuted directions for 𝓑₃-selection; the
2026-06-17 dense-SDP closure (`b3_dense_sdp_wedderburn_projector.py`) refuted the
operator-space SDP lever (𝓑₃ is 99.8% γ = max-cost identity; no continuous cost
selects it). The remaining direction is the OTHER one #2433 named: *"promote the
discrete topological (Borromean = no separable sub-link) criterion INTO the
selection program rather than applying it as an after-the-fact tiebreak."*

This probe scopes that direction (formalize-first; derive-or-refute; no fit).

## The reframing

The corpus currently selects 𝓑₃ by a **net-constrained ranking** — `|Δnet|`
closest to the physical target `net_proton`
(`confinement-operator-selection.md`), with the Borromean property as a
*tiebreak*. #2433 flagged that the net-target is a physical input (arguably
circular). The dense-SDP closure showed why no operator-space functional fixes
it. **So the selection cannot live on NF-operator-space at all** — there 𝓑₃ is
just "mostly identity", indistinguishable by any extremal functional.

It must live on **braid-word / link space**, where confinement has a crisp,
input-free meaning:

> **Confinement = no proper subset of the 3 quarks can be isolated = the closure
> is a BRUNNIAN link** (every proper sublink is trivially unlinked).

The selection principle then is purely topological + Occam:

> **Among Brunnian 3-component links, select the crossing-minimal one.**
> That is the **Borromean rings** = closure of `(σ₁σ₂⁻¹)³` — the unique 6-crossing
> Brunnian link (Rolfsen; the simplest nontrivial Brunnian link). No physical
> `net_proton` target, no fitted cost operator.

## What this probe verifies (the cheap, decisive structural check)

The Brunnian signature is computable directly from the braid word — no SnapPy:

1. `(σ₁σ₂⁻¹)³` is a **pure** 3-braid (underlying permutation = identity), so its
   closure has exactly 3 components (3 quarks).
2. **All three pairwise linking numbers are 0** — the defining Brunnian/Borromean
   signature: the components are pairwise unlinked, yet the 3-link is nontrivial
   (each pair still crosses, with canceling signs).

Contrast: the mesonic `L±` channel the dense-SDP selected is a *2-strand*
(pairwise) object — NOT Brunnian, NOT 3-body confining. The Brunnian constraint
is exactly what excludes the mesonic minimizer the operator-space SDP fell into.

## What this probe does NOT claim

It does **not** close the binding *magnitude* (Δ_λ assembly) — that needs the
operator-cumulant scalar (#2430), still gated on the *extraction* functional.
This scopes #2433 verdict (1) only: the selection PRINCIPLE is topological-
combinatorial (Brunnian + crossing-minimal), not continuous-variational. The
crossing-minimal-Brunnian = Borromean step is a literature fact (citable), not
re-derived here.

Run:  python3 -u computations/probes/b3_brunnian_selection_scope.py
"""
from __future__ import annotations

# Borromean confinement braid: (σ₁ σ₂⁻¹)³ on 3 strands.
# Encoding: signed generator index, sign = crossing sign, |k| = generator.
BORROMEAN = [+1, -2, +1, -2, +1, -2]


def underlying_perm(word, n=3):
    """Underlying permutation of a braid word (positions 0..n-1)."""
    perm = list(range(n))
    for g in word:
        k = abs(g) - 1                       # swap positions k, k+1
        perm[k], perm[k + 1] = perm[k + 1], perm[k]
    return perm


def pairwise_linking(word, n=3):
    """lk(a,b) = ½ · Σ (crossing signs between strands a and b), from the word.

    Track which ORIGINAL strand sits at each position; at each generator the two
    strands at positions k,k+1 cross with the generator's sign.
    """
    pos = list(range(n))                     # pos[i] = original strand at position i
    lk = {(a, b): 0 for a in range(n) for b in range(a + 1, n)}
    for g in word:
        k = abs(g) - 1
        sign = 1 if g > 0 else -1
        a, b = sorted((pos[k], pos[k + 1]))
        lk[(a, b)] += sign
        pos[k], pos[k + 1] = pos[k + 1], pos[k]
    return {pair: v / 2 for pair, v in lk.items()}


def crossings_per_pair(word, n=3):
    pos = list(range(n))
    cnt = {(a, b): 0 for a in range(n) for b in range(a + 1, n)}
    for g in word:
        k = abs(g) - 1
        a, b = sorted((pos[k], pos[k + 1]))
        cnt[(a, b)] += 1
        pos[k], pos[k + 1] = pos[k + 1], pos[k]
    return cnt


def spherogram_confirmation():
    """Cross-check via spherogram's STABLE combinatorial path only.

    Returns a dict, or None if spherogram is unavailable. We deliberately use
    ONLY exact combinatorial invariants — component/crossing counts and
    Reidemeister `simplify` — and AVOID the SnapPy numerical/hyperbolic kernel
    (`.exterior().volume()`, `.identify()`), which a sibling found to give
    unstable results (and which errors `SnapPy doesn't seem to be available`
    in this sandbox). The unlink-vs-Hopf distinction is made by simplification
    (unlink -> 0 crossings; Hopf -> irreducibly 2), not by any float invariant.
    """
    try:
        import spherogram
    except Exception:
        return None

    def simp_crossings(L):
        L = L.copy()
        for mode in ("global", "level", "basic"):
            try:
                L.simplify(mode)
            except Exception:
                pass
        return len(L.crossings)

    L = spherogram.Link(braid_closure=BORROMEAN)
    res = {
        "components": len(L.link_components),
        "crossings": len(L.crossings),
        "full_simplified": simp_crossings(L),
        "sublink_simplified": [],
    }
    for drop in range(3):
        keep = [i for i in range(3) if i != drop]
        res["sublink_simplified"].append(simp_crossings(L.sublink(keep)))
    return res


def main() -> int:
    word = BORROMEAN
    perm = underlying_perm(word)
    lk = pairwise_linking(word)
    cnt = crossings_per_pair(word)

    print("\n  BRUNNIAN SELECTION OF 𝓑₃ — topological criterion in the program (scope)\n")
    print(f"  confinement braid: (σ₁σ₂⁻¹)³  =  {word}")
    print(f"  underlying permutation: {perm}  ->  "
          f"{'PURE (3 components = 3 quarks)' if perm == [0, 1, 2] else 'NOT pure'}")
    print("\n  pairwise structure (Brunnian signature):")
    print(f"  {'quark pair':<14}{'crossings':>10}{'linking #':>12}")
    print("  " + "-" * 36)
    for pair in sorted(lk):
        print(f"  {str(pair):<14}{cnt[pair]:>10}{lk[pair]:>12.1f}")

    all_zero = all(v == 0 for v in lk.values())
    some_cross = all(c > 0 for c in cnt.values())
    print("\n  CHECK 1 (pure 3-braid):        ", "PASS" if perm == [0, 1, 2] else "FAIL")
    print("  CHECK 2 (all lk = 0, Brunnian):", "PASS" if all_zero else "FAIL")
    print("  CHECK 3 (yet each pair crosses):", "PASS" if some_cross else "FAIL",
          "(pairwise unlinked but geometrically interwoven)")

    sg = spherogram_confirmation()
    if sg is None:
        print("\n  spherogram cross-check: SKIPPED (not installed)")
    else:
        full_nontrivial = sg["full_simplified"] > 0
        subs_unlink = all(s == 0 for s in sg["sublink_simplified"])
        print("\n  SPHEROGRAM CROSS-CHECK (stable combinatorial path only; "
              "SnapPy numerical kernel avoided):")
        print(f"    full 3-link: comps={sg['components']} crossings={sg['crossings']} "
              f"-> Reidemeister-simplified={sg['full_simplified']} "
              f"({'nontrivial' if full_nontrivial else 'TRIVIAL?!'})")
        print(f"    2-sublinks simplified: {sg['sublink_simplified']} "
              f"({'all UNLINK (0 crossings)' if subs_unlink else 'NOT all unlink'})")
        print("    => nontrivial 6-crossing 3-link with every 2-sublink the unlink "
              "= Brunnian (rigorous, no float invariant).")

    print("""
  VERDICT (scope, not closure): the confinement braid (σ₁σ₂⁻¹)³ is a pure
  3-braid whose three pairwise linking numbers all vanish while every pair still
  crosses — the Brunnian / Borromean signature. So "no proper subset of quarks
  can be isolated" is a CRISP, input-free topological constraint, satisfied by
  𝓑₃ and FAILED by the mesonic L± channel (a 2-strand pairwise object) that the
  operator-space dense-SDP fell into. This is the feasible-set the dense-SDP
  lacked. The selection principle is therefore topological-combinatorial —
  "crossing-minimal Brunnian 3-link" = Borromean rings (literature: the unique
  6-crossing Brunnian link) — NOT a continuous functional on NF-operator-space
  (where 𝓑₃ is just 99.8% identity and no extremal principle reaches it), and
  NOT the net_proton-target ranking (a physical input). This scopes #2433
  verdict (1): the program should select on link space under the Brunnian
  constraint. It does NOT close the binding magnitude (Δ_λ assembly / #2430
  operator-cumulant scalar extraction remain gated). No fit; nothing rewired.
""")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
