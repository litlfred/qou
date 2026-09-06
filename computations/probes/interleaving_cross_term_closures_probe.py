#!/usr/bin/env python3
"""
Probe — what the two n = 4 words ARE (route A, step 1) and what their order-zero
cross term COUNTS (route C, step 1). Survey: docs/audits/2026-09-05-binding-gap-
groupoids-derived-categories-full-tower.md §7 items 4–5; beans qou-amw3, qou-8uxw.

ROUTE A — the cross term is a difference of two LINKS.  From the Ocneanu axioms
alone (QOU/MathlibExt/InterleavedWordClosures.lean, sorry-free):

    tr(s0 s1 s0 s2 s1) = z² · tr(σ³)        interleaved = doubly-stabilised σ³  → TREFOIL
    tr(s0² s1² s2)     = z  · tr(σ²)²       sequential  = stabilised Hopf ⊔ Hopf → 3-CHAIN
    Δ                  = z²·tr(σ³) − z·tr(σ²)²

The identities hold with z and h FREE — i.e. at the level of the two-variable
Ocneanu trace (HOMFLY-PT), not merely at convention D.  Each side is the graded
Euler characteristic of a Khovanov–Rozansky homology (of the trefoil and of the
chain), so "Δ is an Euler characteristic" is TRUE in the content-free sense (a
shifted direct sum) and UNSUPPORTED in the interesting sense: the two closures
have different component counts, no braid move relates the words, and the probe
records that no natural chain map between the two complexes is supplied by
anything in the corpus.  Route A step 2 would have to construct one (a cobordism
map), and that is bean-level work, not this probe's.

ROUTE C — the order-zero cross term is a FIXED-POINT COUNT (Burnside).  At q = 1
the Markov trace with z = 1/N on ℚSₙ is the normalised character of the natural
Sₙ-action on V^{⊗n}, dim V = N:  N^{c(w)} / N^n, and the character of a
permutation representation is the number of fixed points — here the number of
w-invariant colourings of the n strands with N colours, which is N^{c(w)}
because an invariant colouring is constant on each cycle.  Groupoidification
(Baez–Hoffnung–Walker) reads exactly this: a span X ← X^w → X degroupoidifies
to the trace of the permutation operator.  Checked exactly for ALL 24
permutations of S₄ at N ∈ {2, 3}, and the 16-dim spin-½ quantum trace of
markov_trace_n4_interleaved_cross_term_probe.py is shown to degenerate at q = 1
to that fixed-point count (R-matrix → swap).  The cross term at q = 1 is
2 − 8 = −6 fixed colourings, which is the T1 probe's [2]_q⁴·Δ|_{q=1} = −6.

So route C's step 1 is POSITIVE and exact: the q = 1 cross term has a
groupoid-cardinality reading.  Its q-deformation is the μ-weighted quantum
trace — a q-count of fixed points — whose radius and order-zero dominance the
T1 probe measured.  Whether that q-count is itself a groupoid cardinality (a
q-groupoid, à la the Hecke-algebra-as-groupoid-algebra of Baez–Hoffnung–Walker
§ Hecke) is the next question and is left open.

SCOPE (a): one word pair, n = 4.  Nothing wired, nothing fitted.  No q₀ is
read anywhere — z, h, q are formal symbols throughout (q0Anchor: independent).

Run: python3 -u computations/probes/interleaving_cross_term_closures_probe.py \\
       2>&1 | tee /tmp/interleaving_closures.log
"""
from __future__ import annotations

import itertools
import os
import sys
import time

import sympy as sp
from sympy.combinatorics import Permutation

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from markov_trace_n4_interleaved_cross_term_probe import route_rep  # noqa: E402

T0 = time.monotonic()
N_STRANDS = 4


def log(msg: str) -> None:
    print(f"  [{time.monotonic() - T0:5.1f}s] {msg}", flush=True)


def perm_of_word(word, n=N_STRANDS):
    p = Permutation(list(range(n)))
    for i in word:
        p = p * Permutation(i, i + 1, size=n)
    return p


def fixed_colourings(p: Permutation, n_colours: int, n=N_STRANDS) -> int:
    """Exact count of colourings c : [n] → [N] with c ∘ p = c."""
    return sum(1 for c in itertools.product(range(n_colours), repeat=n)
               if all(c[p(i)] == c[i] for i in range(n)))


def main() -> int:
    print("=" * 76)
    print(" n = 4 words: closures (route A) and the q = 1 fixed-point count (route C)")
    print("=" * 76)
    checks = []
    z, h = sp.symbols("z h")

    # ---------------- ROUTE A: Markov-move identification, z and h free ------------
    tr_sig = z
    tr_sig2 = h * z + 1                       # Hecke: σ² = hσ + 1
    tr_sig3 = h * tr_sig2 + tr_sig            # σ³ = hσ² + σ
    I_zh = z * (z ** 2 + h * z + h ** 2 * z ** 2)   # tr_interleaved (Lean)
    S_zh = z * (h * z + 1) ** 2                      # tr_sequential  (Lean)
    D_zh = z * (z ** 2 - h * z - 1)                  # interleaved_sub_sequential (Lean)
    chk_A1 = sp.expand(I_zh - z ** 2 * tr_sig3) == 0
    chk_A2 = sp.expand(S_zh - z * tr_sig2 ** 2) == 0
    chk_A3 = sp.expand(D_zh - (z ** 2 * tr_sig3 - z * tr_sig2 ** 2)) == 0
    log(f"free (z,h): interleaved = z²·tr(σ³) {chk_A1}; sequential = z·tr(σ²)² {chk_A2}; "
        f"Δ = z²tr(σ³) − z tr(σ²)² {chk_A3}")

    # the same in the independent 16-dim rep, q formal
    q = sp.symbols("q", positive=True)
    sigma, tr = route_rep(N_STRANDS, q)
    s0, s1, s2 = sigma(0), sigma(1), sigma(2)
    z_D = tr(s0)
    inter_rep = tr(s0 * s1 * s0 * s2 * s1)
    seq_rep = tr(s0 * s0 * s1 * s1 * s2)
    cube_rep = tr(s0 * s0 * s0)
    sq_rep = tr(s0 * s0)
    chk_A4 = sp.simplify(inter_rep - z_D ** 2 * cube_rep) == 0
    chk_A5 = sp.simplify(seq_rep - z_D * sq_rep ** 2) == 0
    log(f"16-dim rep, q formal: interleaved = z_D²·tr(σ³) {chk_A4}; sequential = z_D·tr(σ²)² {chk_A5}")

    # closure component counts from the permutations
    p_int = perm_of_word([0, 1, 0, 2, 1])
    p_seq = perm_of_word([0, 0, 1, 1, 2])
    chk_A6 = (p_int.cycle_structure == {4: 1}) and (p_seq.cycle_structure == {1: 2, 2: 1})
    chk_A7 = p_seq == perm_of_word([2])
    log(f"closures: interleaved permutation {p_int.cyclic_form} (knot), "
        f"sequential {p_seq.cyclic_form} (= s2, three components) {chk_A6 and chk_A7}")

    # ---------------- ROUTE C: Burnside over all of S4 ---------------------------------
    burnside = {}
    all_ok = True
    for N in (2, 3):
        rows = []
        for p in [Permutation(list(t)) for t in itertools.permutations(range(N_STRANDS))]:
            fx = fixed_colourings(p, N)
            expect = N ** p.cycles
            rows.append((str(p.array_form), p.cycles, fx, expect))
            all_ok &= (fx == expect)
        burnside[N] = rows
    chk_C1 = all_ok and len(burnside[2]) == 24
    log(f"Burnside on all 24 elements of S4, N ∈ {{2,3}}: #fixed colourings = N^cycles {chk_C1}")

    fx_int, fx_seq = fixed_colourings(p_int, 2), fixed_colourings(p_seq, 2)
    chk_C2 = (fx_int, fx_seq) == (2, 8)
    chk_C3 = fx_int - fx_seq == -6
    log(f"two words at N = 2: fixed colourings {fx_int} vs {fx_seq}; difference {fx_int - fx_seq}")

    # the 16-dim quantum trace degenerates to the fixed-point count at q = 1
    br2 = q + 1 / q
    unnorm = {"interleaved": sp.simplify(inter_rep * br2 ** N_STRANDS),
              "sequential": sp.simplify(seq_rep * br2 ** N_STRANDS),
              "identity": sp.simplify(tr(sp.eye(16)) * br2 ** N_STRANDS)}
    at1 = {k: v.subs(q, 1) for k, v in unnorm.items()}
    chk_C4 = at1 == {"interleaved": 2, "sequential": 8, "identity": 16}
    R1 = sp.Matrix([[q, 0, 0, 0], [0, q - 1 / q, 1, 0], [0, 1, 0, 0], [0, 0, 0, q]]).subs(q, 1)
    chk_C5 = R1 == sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    chk_C6 = (inter_rep.subs(q, 1) == sp.Rational(1, 8)) and (seq_rep.subs(q, 1) == sp.Rational(1, 2))
    log(f"quantum trace at q = 1: unnormalised {at1} = fixed-point counts {chk_C4}; "
        f"R(1) = swap {chk_C5}; normalised 1/8, 1/2 {chk_C6}")
    # the cross term at q = 1 in the rep equals the T1 probe's [2]^4 Δ(1) = −6
    D_unnorm_1 = sp.simplify((inter_rep - seq_rep) * br2 ** N_STRANDS).subs(q, 1)
    chk_C7 = D_unnorm_1 == -6
    log(f"[2]_q⁴·Δ at q = 1 in the rep = {D_unnorm_1}")

    checks = [
        ("A: interleaved = z²·tr(σ³) with z, h free (trefoil after two stabilisations)", chk_A1),
        ("A: sequential = z·tr(σ²)² with z, h free (stabilised Hopf-chain)", chk_A2),
        ("A: Δ = z²·tr(σ³) − z·tr(σ²)² with z, h free", chk_A3),
        ("A: same two identities in the independent 16-dim rep, q formal", chk_A4 and chk_A5),
        ("A: closure component counts 1 (4-cycle) vs 3 (transposition)", chk_A6),
        ("A: the sequential permutation is s₂ itself", chk_A7),
        ("C: Burnside — #fixed colourings = N^cycles on all 24 of S₄, N = 2, 3", chk_C1),
        ("C: the two words fix 2 and 8 two-colourings", chk_C2),
        ("C: fixed-point difference is −6", chk_C3),
        ("C: 16-dim quantum trace at q = 1 is the fixed-point count (2, 8, 16)", chk_C4),
        ("C: the R-matrix at q = 1 is the swap", chk_C5),
        ("C: normalised traces at q = 1 are 1/8 and 1/2", chk_C6),
        ("C: [2]_q⁴·Δ at q = 1 in the rep is −6 (matches the T1 probe)", chk_C7),
    ]
    print()
    ok = 0
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed   ({time.monotonic() - T0:.1f}s)")

    wb = WitnessBuilder("interleaving-cross-term-closures", engine="sympy", _script_path=__file__)
    wb.set_description(
        "Routes A and C, step 1 (2026-09-05 binding-gap survey §7 items 4–5). A: by the Markov "
        "axioms with z, h free, tr(s0s1s0s2s1) = z²·tr(σ³) (the interleaved word is a doubly-"
        "stabilised σ³, closure the trefoil) and tr(s0²s1²s2) = z·tr(σ²)² (a stabilised Hopf-"
        "chain, three components), so Δ is a difference of two link invariants of two different "
        "links — an Euler characteristic only in the content-free sense; no natural chain map is "
        "supplied. C: at q = 1 the trace is the normalised character of S₄ on V^{⊗4}, i.e. a "
        "Burnside fixed-point count of colourings, verified on all 24 permutations at N = 2, 3; "
        "the words fix 2 and 8 two-colourings, difference −6 = [2]_q⁴·Δ|_{q=1}; the 16-dim "
        "quantum trace degenerates to that count at q = 1 (R → swap). Exact sympy / integers; "
        "no q₀ read. Scope (a).")
    wb.set_content_block("prop:markov-trace-axiomatic-closed-form")
    for name, passed in checks:
        wb.add_assertion(name.replace(" ", "_")[:80], computed="1" if passed else "0",
                         expected="1", tolerance="0.5", source="exact (sympy / integer)")
    wb.add_parameter("words", {"interleaved": "s0 s1 s0 s2 s1", "sequential": "s0^2 s1^2 s2"})
    wb.add_data("closures", {"interleaved": "z^2 * tr(sigma^3): trefoil (1 component)",
                             "sequential": "z * tr(sigma^2)^2: chain of two Hopf links (3 components)",
                             "interleaved_perm": p_int.cyclic_form, "sequential_perm": p_seq.cyclic_form})
    wb.add_data("fixed_colourings", {"N=2": {"interleaved": fx_int, "sequential": fx_seq, "difference": fx_int - fx_seq}})
    wb.add_data("burnside_table_N2", [{"perm": r[0], "cycles": r[1], "fixed": r[2]} for r in burnside[2]])
    wb.add_data("quantum_trace_at_q1_unnormalised", {k: str(v) for k, v in at1.items()})
    wb.add_data("verdict", (
        "Route A step 1: the cross term is trefoil-minus-Hopf-chain, a difference of two different "
        "links' invariants; 'Euler characteristic' holds only trivially — a natural map is not "
        "supplied and is the honest next gap. Route C step 1: POSITIVE and exact — the q = 1 cross "
        "term is a Burnside fixed-point-count difference (2 − 8), a groupoid cardinality in the "
        "Baez–Hoffnung–Walker sense; the q-deformation is the μ-weighted quantum trace, a "
        "q-count of fixed points, whose groupoid reading is the open step 2."))
    wb.add_caveat("Scope (a): one n = 4 word pair. The 16-dim check is the spin-½ representation "
                  "at convention D; the free-(z,h) identities are representation-independent.")
    out = wb.save({"q0Anchor": "independent",
                   "q0AnchorReason": ("z, h and q are formal sympy symbols throughout and the only "
                                      "evaluations are at q = 1; no substrate q₀ is read or substituted, "
                                      "so neither pin can affect any number in this witness.")})
    print(f"  witness -> {os.path.relpath(out, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))}")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
