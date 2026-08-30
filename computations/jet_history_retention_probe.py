#!/usr/bin/env python3
"""Where does interaction history actually get lost -- the trace, or earlier?

The hypothesis under test (owner, 2026-08-28)
---------------------------------------------
"Say we've just gone through one knot-particle interaction that leaves some
entanglement energy ... that previous entanglement data will be shifted to a
higher order upon subsequent particle interactions. It's still retained in all
of the history when we're looking at the full filtration and jet order. We are
not losing any of the history, except for when we look at the trace."

There are THREE distinct objects here, and the claim is only true of some of
them. This probe separates them and measures which:

  L1  the JET-ORDER LOG -- the ordered sequence of reduction events
  L2  the GS NORMAL FORM / filtration profile -- {grade -> coefficients}
  L3  the MARKOV TRACE -- one scalar

L3 is obviously lossy. The question this probe exists to settle is whether L2
is *also* lossy, because the GS normal form is a CANONICAL form: it depends
only on the algebra element, not on the path taken to reach it. If two
production histories land on the same element of H_n(q), their L2 profiles are
identical by construction, and the history was already gone one level before
the trace.

That would not refute the hypothesis -- it would relocate it. The physical
state is not only an algebra element: an interaction ADDS STRANDS, so the
composite lives in a LARGER algebra H_m, and prior structure enters through
the tower embedding H_n -> H_m rather than being overwritten. Grade promotion
under that embedding is the thing that could carry entanglement history
forward, and it is measurable.

So the probe answers, in order:

  Q1  Do two different histories reaching the SAME element have the same L2?
      (If yes: the normal form is lossy, not just the trace.)
  Q2  Under the tower embedding H_n -> H_{n+1}, does the filtration mass of a
      prior state move UP in grade?
  Q3  Where do NEGATIVE coefficients come from, and do they behave like a
      conserved "entanglement" quantity or like a bookkeeping sign?

Scope
-----
This is a measurement, not a closure. It does not derive the missing n=3
body-order term of `conj:binding-manybody-eq-jet-filtration`; it tests a
structural precondition for the owner's proposed mechanism for it.

Exact throughout: symbolic q over QQ(q) via sympy. No floats, no substrate
anchor -- the questions are algebraic and q stays a free variable.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

q = sp.symbols("q", positive=True)
#: The Hecke structure constant. sigma_i^2 = A*sigma_i + 1.
A = q - 1 / q


# ---------------------------------------------------------------- permutations
def perm_apply_s(perm: tuple, i: int) -> tuple:
    """Right action of the adjacent transposition s_i (1-indexed)."""
    p = list(perm)
    p[i - 1], p[i] = p[i], p[i - 1]
    return tuple(p)


def coxeter_length(perm: tuple) -> int:
    """Inversion count = Coxeter length = GS filtration grade."""
    n = len(perm)
    return sum(1 for a in range(n) for b in range(a + 1, n) if perm[a] > perm[b])


class HeckeElem:
    """An element of H_n(q) as {permutation -> coefficient in QQ(q)}.

    Basis is {T_w}. Multiplication uses the standard right-action rule

        T_w * T_i =  T_{w s_i}                     if l(w s_i) > l(w)
                  =  A * T_w + T_{w s_i}           otherwise

    which is exactly the GS reduction rule for shortlex order. The second
    branch is the only place a term can move DOWN in grade -- and note it
    leaves a copy at the OLD grade too. That asymmetry is the whole subject
    of this probe.
    """

    __slots__ = ("n", "terms")

    def __init__(self, n: int, terms: dict | None = None):
        self.n = n
        self.terms = dict(terms) if terms else {}

    @staticmethod
    def one(n: int) -> "HeckeElem":
        return HeckeElem(n, {tuple(range(1, n + 1)): sp.Integer(1)})

    def _add(self, w, c):
        cur = self.terms.get(w, sp.Integer(0)) + c
        cur = sp.simplify(sp.expand(cur))
        if cur == 0:
            self.terms.pop(w, None)
        else:
            self.terms[w] = cur

    def mul_gen(self, i: int, inverse: bool = False) -> "HeckeElem":
        """Right-multiply by T_i, or by T_i^{-1} = T_i - A."""
        out = HeckeElem(self.n)
        for w, c in self.terms.items():
            wsi = perm_apply_s(w, i)
            if coxeter_length(wsi) > coxeter_length(w):
                out._add(wsi, c)                      # grade UP by 1
            else:
                out._add(w, c * A)                    # stays at grade l(w)
                out._add(wsi, c)                      # grade DOWN by 1
            if inverse:
                out._add(w, -c * A)                   # T_i^{-1} = T_i - A
        return out

    def profile(self) -> dict:
        """L2: filtration profile {grade -> {perm: coeff}}."""
        prof: dict = {}
        for w, c in self.terms.items():
            prof.setdefault(coxeter_length(w), {})[w] = c
        return prof

    def grade_mass(self) -> dict:
        """Coefficient mass per grade, evaluated symbolically."""
        return {g: sp.simplify(sum(v.values()))
                for g, v in sorted(self.profile().items())}

    def embed(self, m: int) -> "HeckeElem":
        """The tower embedding H_n -> H_m (m > n): pad each permutation with
        fixed points. Grades are UNCHANGED by this map -- inversions among the
        new fixed points are zero -- which is itself a finding, see Q2."""
        out = HeckeElem(m)
        for w, c in self.terms.items():
            out._add(tuple(w) + tuple(range(self.n + 1, m + 1)), c)
        return out


def word_to_elem(n: int, word) -> tuple["HeckeElem", list]:
    """Reduce a signed braid word, logging L1 (the jet-order event log).

    `word` is a list of signed ints: +i = sigma_i, -i = sigma_i^{-1}.
    Returns (element, log) where log[k] records the grade profile AFTER the
    k-th letter -- i.e. the history the hypothesis says is retained.
    """
    E = HeckeElem.one(n)
    log = []
    for step, g in enumerate(word, 1):
        before = {k: len(v) for k, v in sorted(E.profile().items())}
        E = E.mul_gen(abs(g), inverse=(g < 0))
        after = {k: len(v) for k, v in sorted(E.profile().items())}
        log.append({
            "step": step,
            "letter": ("sigma_%d" % g) if g > 0 else ("sigma_%d^-1" % -g),
            "grades_before": before,
            "grades_after": after,
            "top_grade_before": max(before) if before else None,
            "top_grade_after": max(after) if after else None,
        })
    return E, log


# ============================================================ Q1: is NF lossy?
def q1_same_element_two_histories():
    """Two production histories reaching the SAME element: is L2 the same?

    Braid relation sigma_1 sigma_2 sigma_1 = sigma_2 sigma_1 sigma_2 gives two
    genuinely different reduction paths to one element. If the L2 profiles
    agree, the normal form has already discarded the path -- one level BEFORE
    the trace.
    """
    print("=" * 74)
    print("Q1  Two histories, same element: does the normal form keep the path?")
    print("=" * 74)
    # Both reach the same element. B does two extra interactions that cancel
    # (sigma_2 then sigma_2^-1), so its log is strictly longer and fires the
    # Hecke relation. The braid-relation pair (s1s2s1 vs s2s1s2) is NOT usable
    # here: every step is length-increasing in both, so the two logs are
    # identical in shape and the test would be vacuous.
    wA, wB = [1, 2, 1], [1, 2, 1, 2, -2]
    EA, logA = word_to_elem(3, wA)
    EB, logB = word_to_elem(3, wB)

    print("\n  history A: sigma_1 sigma_2 sigma_1")
    for e in logA:
        print(f"    step {e['step']}  {e['letter']:<12} grades {e['grades_before']}"
              f" -> {e['grades_after']}")
    print("  history B: sigma_1 sigma_2 sigma_1 sigma_2 sigma_2^-1  (same element, longer path)")
    for e in logB:
        print(f"    step {e['step']}  {e['letter']:<12} grades {e['grades_before']}"
              f" -> {e['grades_after']}")

    same_elem = EA.terms == EB.terms
    same_prof = ({g: sorted(v) for g, v in EA.profile().items()}
                 == {g: sorted(v) for g, v in EB.profile().items()})
    same_log = ([e["grades_after"] for e in logA]
                == [e["grades_after"] for e in logB])
    print(f"\n  same ELEMENT (L2 normal form)?  {same_elem}")
    print(f"  same FILTRATION PROFILE (L2)?  {same_prof}")
    print(f"  same JET LOG (L1)?             {same_log}")
    if same_elem and same_prof and not same_log:
        verdict = ("the normal form is ALREADY history-free: same element and same "
                   "L2 profile from two different paths, so the path survives only in L1")
    elif not same_elem:
        verdict = "the two words are NOT the same element -- test is invalid, fix the pair"
    else:
        verdict = ("same element but DIFFERENT L2 profile -- impossible for a canonical "
                   "form; indicates a bug in the reduction")
    print(f"\n  => {verdict}")
    return {"same_element": bool(same_elem), "same_profile": bool(same_prof),
            "same_jet_log": bool(same_log), "verdict": verdict}


# ================================================== Q2: grade under the tower
def q2_tower_promotion():
    """Does a prior state's filtration mass move UP when a strand is added?

    Take the electron word sigma_1^3 in H_2, embed into H_3, then interact
    (multiply by the new generator sigma_2). Report the grade profile at each
    stage. The hypothesis predicts prior content is PROMOTED, not collapsed.
    """
    print("\n" + "=" * 74)
    print("Q2  Tower embedding H_2 -> H_3 -> interact: is prior mass promoted?")
    print("=" * 74)
    E2, _ = word_to_elem(2, [1, 1, 1])            # electron: trefoil sigma_1^3
    print("\n  stage 1  electron sigma_1^3 in H_2")
    for g, m in E2.grade_mass().items():
        print(f"           grade {g}: {sp.factor(m)}")

    E3 = E2.embed(3)
    print("  stage 2  embedded into H_3 (pad with a fixed point)")
    for g, m in E3.grade_mass().items():
        print(f"           grade {g}: {sp.factor(m)}")
    embed_shifts = (E2.grade_mass().keys() != E3.grade_mass().keys())

    E3b = E3.mul_gen(2)
    print("  stage 3  interact with the new strand (right-multiply sigma_2)")
    for g, m in E3b.grade_mass().items():
        print(f"           grade {g}: {sp.factor(m)}")

    top_before = max(E3.grade_mass())
    top_after = max(E3b.grade_mass())
    print(f"\n  top grade: {max(E2.grade_mass())} (H_2) -> {top_before} (embedded)"
          f" -> {top_after} (after interaction)")
    print(f"  embedding alone shifts grades? {embed_shifts}")
    print(f"  interaction promotes the top grade? {top_after > top_before}")
    return {"top_h2": int(max(E2.grade_mass())), "top_embedded": int(top_before),
            "top_after_interaction": int(top_after),
            "embedding_shifts_grade": bool(embed_shifts),
            "interaction_promotes": bool(top_after > top_before)}


# ============================================ Q3: where do negatives come from
def q3_negative_provenance():
    """Are negative coefficients an inverse-crossing artifact or intrinsic?

    Compare a positive word against the same word with inverted letters. The
    reduction rule introduces -A only via T_i^{-1} = T_i - A, so if negatives
    track inverse crossings exactly, "negative = entanglement" is a statement
    about NEGATIVE CROSSINGS (chirality), not about a separate quantity.
    """
    print("\n" + "=" * 74)
    print("Q3  Provenance of negative coefficients")
    print("=" * 74)
    cases = [("all-positive  sigma_1^3", 2, [1, 1, 1]),
             ("all-negative  sigma_1^-3", 2, [-1, -1, -1]),
             ("proton  (s1 s2^-1)^3", 3, [1, -2, 1, -2, 1, -2]),
             ("neutron (s1^-1 s2)^3", 3, [-1, 2, -1, 2, -1, 2])]
    rows = []
    for label, n, word in cases:
        E, _ = word_to_elem(n, word)
        n_inv = sum(1 for g in word if g < 0)
        # Evaluate at an exact rational q > 1 (the physical regime) and read the
        # SIGN OF THE VALUE. Reading signs off polynomial coefficients instead
        # is wrong: (q-1)(q+1)/q has a negative coefficient at every q, which
        # made the all-positive word report negatives.
        q_eval = sp.Rational(11, 10)
        negs = []
        for g, terms in sorted(E.profile().items()):
            for w, c in terms.items():
                if sp.simplify(c.subs(q, q_eval)) < 0:
                    negs.append(g)
        print(f"\n  {label:<24} inverse letters = {n_inv}")
        print(f"    grades with a NEGATIVE coefficient at q=11/10: "
              f"{sorted(set(negs)) if negs else 'none'}")
        rows.append({"case": label, "inverse_letters": n_inv,
                     "grades_with_negative": sorted(set(int(x) for x in negs))})
    return rows


def main():
    print("Interaction history in the GS filtration -- three levels\n")
    r1 = q1_same_element_two_histories()
    r2 = q2_tower_promotion()
    r3 = q3_negative_provenance()
    r4 = q4_promotion_universality()
    print("\n" + "=" * 74)
    print("SUMMARY")
    print("=" * 74)
    print(f"  Q1 normal form history-free : {r1['same_profile'] and not r1['same_jet_log']}")
    print(f"  Q2 interaction promotes     : {r2['interaction_promotes']}")
    print(f"  Q2 embedding alone promotes : {r2['embedding_shifts_grade']}")
    print(f"  Q4 promotion universal      : {r4['universal']}")
    return {"q1": r1, "q2": r2, "q3": r3, "q4": r4}



# ===================================== Q4: is the +1 promotion universal?
def q4_promotion_universality():
    """Is Q2's rigid grade-shift a coincidence of one word, or a theorem?

    Claim: for ANY E in H_n embedded in H_{n+1}, right-multiplying by the NEW
    generator T_n shifts every grade up by exactly 1, with coefficients
    preserved exactly -- the profile is rigidly translated, nothing splits and
    nothing collapses.

    Reason it should hold: a permutation w in S_n fixes n+1, so w(n) < n+1 =
    w(n+1). Applying s_n therefore creates exactly one new inversion and can
    destroy none, so l(w s_n) = l(w) + 1 for every w in the support. The
    length-decreasing branch of the Hecke rule -- the only branch that splits a
    term across two grades -- is never reached.

    If this holds universally it is the mechanism the hypothesis needs: prior
    interaction content is carried forward INTACT at higher jet order, rather
    than collapsed into the zeroth order.
    """
    print("\n" + "=" * 74)
    print("Q4  Is the +1 promotion universal, or a one-word coincidence?")
    print("=" * 74)
    words = [("electron  s1^3", 2, [1, 1, 1]),
             ("s1^-3", 2, [-1, -1, -1]),
             ("proton  (s1 s2^-1)^3", 3, [1, -2, 1, -2, 1, -2]),
             ("neutron (s1^-1 s2)^3", 3, [-1, 2, -1, 2, -1, 2]),
             ("fig8  (s1 s2^-1)^2", 3, [1, -2, 1, -2]),
             ("mixed  s1 s2 s1 s2^-1", 3, [1, 2, 1, -2]),
             ("Hopf  s1^2", 2, [1, 1]),
             ("trivial  s1 s1^-1", 2, [1, -1])]
    rows, all_rigid = [], True
    for label, n, word in words:
        E, _ = word_to_elem(n, word)
        before = E.grade_mass()
        Eup = E.embed(n + 1).mul_gen(n)          # interact with the new strand
        after = Eup.grade_mass()
        shifted = {g + 1: m for g, m in before.items()}
        rigid = (set(after) == set(shifted)
                 and all(sp.simplify(after[g] - shifted[g]) == 0 for g in after))
        all_rigid &= rigid
        print(f"  {label:<24} grades {sorted(before)} -> {sorted(after)}   "
              f"rigid +1 with coefficients intact: {rigid}")
        rows.append({"case": label, "grades_before": sorted(int(g) for g in before),
                     "grades_after": sorted(int(g) for g in after),
                     "rigid_shift": bool(rigid)})
    print(f"\n  => universal over {len(words)} words: {all_rigid}")
    print("     Nothing splits, nothing collapses: the length-decreasing branch")
    print("     of the Hecke rule is never reached when the generator is new.")
    return {"cases": rows, "universal": bool(all_rigid)}

if __name__ == "__main__":
    main()
