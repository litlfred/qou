#!/usr/bin/env python3
"""The confinement SDP rejects every gamma-gamma word on THREE strands -- and
on FOUR it selects 5 words out of 8190, by a parity rule that echoes the H_2
gluon vertex exactly. So the qou-ales ruling's two halves have common solutions,
but only from four strands up.

## Why this probe exists

The owner ruling `qou-ales` (2026-09-08) says every canonical braid word is to
be selected **through gamma-gamma pair production AND the confinement SDP at
q_0**, never by census. PR #7295 characterised the gamma-gamma half completely
and used the SDP half not at all. This is the SDP half.

`QOU.Mass.GammaGammaWordSelection.SDPSelected` states the predicate: a word is
selected iff it is a candidate, every Wedderburn projection `pi_lambda(w)` is
`Matrix.PosSemidef`, and its cost is minimal among feasible candidates. The
`H_2` instantiation in that file proves the abstract predicate recovers the
known parity rule -- `sigma_0^k` is PSD-feasible iff `k` is even
(`h2_psdFeasible_iff_even`, sorry-free). So the predicate is the corpus's, not
one invented here, and it is known to discriminate.

## The basis, because PSD is not basis-free

`Matrix.PosSemidef` is invariant under ORTHOGONAL conjugation, not under
general similarity, so the block realisation has to be the orthogonal one.
`computations/hoefsmit_mpmath.seminormal_matrices_mp` builds exactly that: its
off-diagonal entries are `b = sqrt(|a a' + 1|)` placed symmetrically, so every
generator is a symmetric matrix (CHECK 0). The remaining freedom is orthogonal
conjugation within each block, under which PSD-ness is preserved -- so every
verdict below is a statement about the algebra, not about a chart.

## Three strands: the conjunction is EMPTY

In the `(2,1)` block of `H_3`, with `sigma_1 = diag(q, -1/q)` and
`sigma_2 = [[a, b], [b, a']]` at axial distance `-2`:

    a  = -1/(q(q^2+1))          a' = q^3/(q^2+1)  <- exactly z_D
    V  = sigma_1 (sigma_2 - h)  the gamma-gamma vertex
    det V = 1        tr V = -1 - h^2                   (CHECK 3, CHECK 4)

So `V` is an **elliptic** element of `SL_2(R)` for every `q` with `h^2 < 1`:
eigenvalues on the unit circle, at angle `theta` with `2 cos theta = -1 - h^2`.
That is exactly `2 pi / 3` when `h = 0`, and `V^3 = 1` forces `q = 1`
(CHECK 5) -- the classical limit and nowhere else. It is also the mechanism
behind the `k mod 3` banding the sibling probe measured: the gamma-gamma vertex
is a NEAR-order-3 rotation, exactly order 3 only at `q = 1`, so the bands drift
instead of repeating.

`QOU.Mass.PsdDetOneTrace` (sorry-free) proves a real PSD `2x2` of determinant
`1` has trace at least `2`, with equality only for the identity. Every `V^k` has
determinant `1` and CHECK 6 measures `tr(V^k) < 2` throughout, so **no
non-empty gamma-gamma word on three strands is PSD-feasible** -- and the reason
is a theorem about the PSD cone, not a numerical accident. In particular the
Borromean baryon `(sigma_0 sigma_1^-1)^3` is SDP-feasible only as `q -> 1`.

## Four strands: the conjunction is NON-EMPTY, and very selective

🛑 **This is where the first draft of this probe was wrong.** It asserted that
no gamma-gamma word is PSD-feasible at `n = 4` either, on the strength of having
tested only the powers of ONE vertex. Over all `2^k` words the assertion FAILED,
and the failure is the result: of **8190** gamma-gamma words with `1..12`
vertices, exactly **5** are PSD-feasible (CHECK 7).

    (0,1,0,1)                          = (v0 v1)^2
    (0,1,0,1,0,1,0,1)                  = (v0 v1)^4
    (0,1,0,1,0,1,0,1,0,1,0,1)          = (v0 v1)^6
    (0,0,1,1,0,1,1,0,0,1)              sporadic, 10 vertices
    (0,1,1,0,0,1,0,0,1,1)              sporadic, 10 vertices

The alternating word `(v0 v1)^m` is feasible **iff `m` is even** -- `m = 1` and
`m = 3` are not -- which is the SAME parity rule the `H_2` gluon vertex obeys
(`sigma_0^k` PSD iff `k` even, `h2_psdFeasible_iff_even`). The echo is checked
rather than admired (CHECK 8).

So the ruling's two halves are **not** in conflict; they simply have no common
solution on three strands. The smallest derived candidate is `(v0 v1)^2`, four
vertices and eight letters.

## 🛑 What is NOT claimed

  * **The feasible set is not characterised**, only enumerated to 12 vertices.
    The two sporadic 10-vertex words show the answer is not merely "the even
    alternating family", and nothing here explains them.
  * **No cost / minimality is computed.** `SDPSelected` also requires minimal
    cost among feasible candidates, and this probe tests only feasibility. So
    it narrows the candidate set; it does not select a word.
  * **No observable is computed** and no `Q_beta` comparison is made.

Scope-(a). Selects nothing, wires nothing, moves no number in the corpus.
"""

from __future__ import annotations

import itertools
import os
import sys
import warnings

import sympy as sp

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "computations/qbeta",
           "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
import hoefsmit_mpmath as hf  # noqa: E402
from pyhecke.wedderburn import partitions_of  # noqa: E402

set_compute_dps(60)
mp.mp.dps = 40

Q0 = Q_MP
H0 = Q0 - 1 / Q0
EPS = mp.mpf("1e-25")

#: how far the powers / words are enumerated. Every "none are feasible" figure
#: below is a statement about this range.
KMAX_POW = 200
KMAX_WORDS = 12

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def blocks(n: int):
    """`{partition: (generator matrices, dim)}` in the orthogonal Hoefsmit
    basis, from the corpus producer -- not re-derived here."""
    out = {}
    for shape in partitions_of(n):
        sig, dim, _ = hf.seminormal_matrices_mp(tuple(shape),
                                                cache=hf.BlockCacheMP(Q0))
        out[tuple(shape)] = (sig, dim)
    return out


def is_symmetric(M, dim) -> bool:
    return all(abs(M[i, j] - M[j, i]) <= EPS
               for i in range(dim) for j in range(dim))


def is_psd(M, dim) -> bool:
    """`Matrix.PosSemidef`: symmetric with non-negative spectrum."""
    if not is_symmetric(M, dim):
        return False
    ev = mp.eigsy(mp.matrix(M), eigvals_only=True)
    return all(e > -EPS for e in ev)


def psd_feasible(word_letters, B) -> bool:
    """Every Wedderburn projection of the word is PSD."""
    for sig, dim in B.values():
        M = mp.eye(dim)
        for i, inv in word_letters:
            g = sig[i] - H0 * mp.eye(dim) if inv else sig[i]
            M = M * g
        if not is_psd(M, dim):
            return False
    return True


def vertex_letters(i: int):
    """`vertex i = sigma_i sigma_{i+1}^{-1}`, 0-based, as (gen, is_inverse)."""
    return [(i, False), (i + 1, True)]


def main() -> int:
    w = WitnessBuilder("qbeta-gamma-gamma-sdp-feasibility")
    w.set_description(
        "The confinement SDP's PSD-feasibility predicate "
        "(GammaGammaWordSelection.SDPSelected) rejects every non-empty "
        "gamma-gamma word at n=3 -- the H_3 vertex has det 1 and trace "
        "-1-h^2, hence is elliptic, and V^3=1 forces q=1, so the Borromean "
        "baryon is SDP-feasible only in the classical limit; the exclusion "
        "rests on QOU.Mass.PsdDetOneTrace (sorry-free), not on arithmetic. "
        "At n=4 it is NON-empty and very selective: 5 of 8190 words, the "
        "alternating (v0 v1)^m being feasible iff m is even -- the same "
        "parity rule as the H_2 gluon vertex. Controls: the predicate "
        "reproduces the H_2 rule and accepts sigma_0^2 at every n tested. "
        "Feasibility ONLY -- no cost/minimality, no observable. Scope-(a)."
    )

    print("Assertions:")

    B2, B3, B4 = blocks(2), blocks(3), blocks(4)

    # ---------------------------------------------------------------- CHECK 0
    # The basis. PSD is only orthogonally invariant, so this has to hold or
    # every verdict below is about a chart rather than the algebra.
    unsym = []
    for n, B in ((2, B2), (3, B3), (4, B4)):
        for shape, (sig, dim) in B.items():
            for k, M in enumerate(sig):
                if not is_symmetric(M, dim):
                    unsym.append((n, shape, k))
    check("hoefsmit_generators_are_symmetric_so_the_basis_is_orthogonal",
          not unsym,
          f"every generator of every block at n = 2, 3, 4 is a symmetric "
          f"matrix, so the realisation is the ORTHOGONAL one and PSD-ness is "
          f"invariant under the remaining freedom. Non-symmetric: "
          f"{unsym or 'none'}", w)

    # ---------------------------------------------------------------- CHECK 1
    # Control A: the corpus's own H_2 parity rule, from a sorry-free theorem.
    parity = [(k, psd_feasible([(0, False)] * k, B2)) for k in range(9)]
    check("control_reproduces_the_h2_parity_rule",
          all(feas == (k % 2 == 0) for k, feas in parity),
          f"sigma_0^k PSD-feasible iff k even, k = 0..8: {parity} -- this is "
          f"GammaGammaWordSelection.h2_psdFeasible_iff_even (sorry-free), "
          f"recovered by this file's PSD machinery", w)

    # ---------------------------------------------------------------- CHECK 2
    # Control B: the predicate is not vacuous at n = 3 or n = 4 either.
    ctrl = {}
    for n, B in ((2, B2), (3, B3), (4, B4)):
        ctrl[n] = (psd_feasible([(0, False), (0, False)], B),
                   psd_feasible([(0, False)], B))
    check("control_predicate_is_not_vacuous_at_n3_and_n4",
          all(a and not b for a, b in ctrl.values()),
          f"(sigma_0^2 feasible, sigma_0 feasible) per n: {ctrl}. The shipped "
          f"gluon vertex is accepted and the bare crossing is rejected at "
          f"EVERY n tested -- so a rejection below is about the word, not "
          f"about a predicate that refuses everything", w)

    # ---------------------------------------------------------------- CHECK 3
    # The closed form, symbolic and exact.
    q = sp.Symbol("q", positive=True)
    hs = q - 1 / q
    a_s = sp.simplify(hs / (1 - q ** 4))
    ap_s = sp.simplify(hs / (1 - q ** -4))
    b_s = sp.sqrt(sp.simplify(a_s * ap_s + 1))
    s1 = sp.Matrix([[q, 0], [0, -1 / q]])
    s2 = sp.Matrix([[a_s, b_s], [b_s, ap_s]])
    hecke_ok = sp.simplify(sp.expand(s2 * s2 - hs * s2 - sp.eye(2))) == sp.zeros(2, 2)
    braid_ok = sp.simplify(sp.expand(s1 * s2 * s1 - s2 * s1 * s2)) == sp.zeros(2, 2)
    Vs = sp.simplify(s1 * (s2 - hs * sp.eye(2)))
    tr_resid = sp.simplify(sp.trace(Vs) + 1 + hs ** 2)
    det_resid = sp.simplify(sp.det(Vs) - 1)
    check("h3_vertex_has_det_one_and_trace_minus_one_minus_h_squared",
          hecke_ok and braid_ok and tr_resid == 0 and det_resid == 0,
          f"in the (2,1) block: a = {sp.factor(a_s)}, a' = {sp.factor(ap_s)} "
          f"(= z_D exactly); the matrices satisfy the Hecke quadratic "
          f"({hecke_ok}) and the braid relation ({braid_ok}); "
          f"tr(V) + 1 + h^2 = {tr_resid} and det(V) - 1 = {det_resid}", w)

    # ---------------------------------------------------------------- CHECK 4
    # Ellipticity at the substrate pin, and the 1-dim blocks.
    sig3 = {s: g for s, (g, d) in B3.items()}
    one_dim = {}
    for shape, (sig, dim) in B3.items():
        if dim == 1:
            M = sig[0] * (sig[1] - H0 * mp.eye(1))
            one_dim[shape] = mp.nstr(M[0, 0], 20)
    trV = mp.mpf(str(sp.N(sp.trace(Vs).subs(q, sp.Rational(Q_50_DIGIT_STR)), 35)))
    check("one_dim_blocks_are_exactly_one_and_the_2x2_is_elliptic",
          all(abs(mp.mpf(v) - 1) < EPS for v in one_dim.values())
          and abs(trV) < 2,
          f"the two 1-dim H_3 blocks send the gamma-gamma vertex to "
          f"{one_dim} -- exactly 1, independently confirming the character "
          f"result of #7295 from the Hoefsmit matrices; and "
          f"tr(V) = {mp.nstr(trV, 20)} with |tr| < 2, so V is ELLIPTIC and "
          f"every power has eigenvalues on the unit circle", w)

    # ---------------------------------------------------------------- CHECK 5
    # V^3 = 1 forces q = 1.
    roots = sp.solve(sp.Eq(sp.simplify(sp.trace(Vs)), -1), q)
    check("v_cubed_is_the_identity_only_at_q_equals_one",
          roots == [sp.Integer(1)],
          f"for a det-1 2x2, V^3 = 1 iff tr V = -1, i.e. h^2 = 0. Solving "
          f"tr(V) = -1 over q > 0 gives {roots} -- the CLASSICAL LIMIT only. "
          f"So the Borromean baryon (sigma_0 sigma_1^-1)^3 is SDP-feasible "
          f"only as q -> 1, and at q_0 it is not", w)

    # ---------------------------------------------------------------- CHECK 6
    # n = 3: the powers, against the Lean lemma's hypothesis.
    sigA = B3[(2, 1)][0]
    V = sigA[0] * (sigA[1] - H0 * mp.eye(2))
    M, traces, feas3 = mp.eye(2), [], []
    for k in range(1, KMAX_POW + 1):
        M = M * V
        t = M[0, 0] + M[1, 1]
        traces.append(t)
        feas3.append(psd_feasible(vertex_letters(0) * k, B3) if k <= 12 else None)
    max_tr = max(traces)
    detk = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    check("no_gamma_gamma_power_is_psd_feasible_at_n3",
          max_tr < 2 - mp.mpf("1e-6") and not any(f for f in feas3 if f),
          f"k = 1..{KMAX_POW}: max tr(V^k) = {mp.nstr(max_tr, 12)} < 2, and "
          f"det(V^{KMAX_POW}) = {mp.nstr(detk, 12)} = 1 -- so "
          f"PsdDetOneTrace.not_posSemidef_of_trace_lt_two (sorry-free) "
          f"applies to every one of them. Direct PSD test for k <= 12 agrees: "
          f"{[f for f in feas3[:12]]}", w)

    # ---------------------------------------------------------------- CHECK 7
    # n = 4: EVERY gamma-gamma word, not just the powers of one vertex.
    bad4, n_words = [], 0
    for k in range(1, KMAX_WORDS + 1):
        for combo in itertools.product((0, 1), repeat=k):
            n_words += 1
            letters = []
            for i in combo:
                letters += vertex_letters(i)
            if psd_feasible(letters, B4):
                bad4.append(combo)
    alt = [tuple((0, 1) * m) for m in range(1, KMAX_WORDS // 2 + 1)]
    alt_feas = {2 * m: (alt[m - 1] in bad4)
                for m in range(1, KMAX_WORDS // 2 + 1)}
    check("four_strand_feasible_set_is_tiny_and_non_empty",
          0 < len(bad4) < n_words // 100,
          f"{len(bad4)} of {n_words} gamma-gamma words with 1..{KMAX_WORDS} "
          f"vertices on four strands (both indices, every order) are "
          f"PSD-feasible: {[list(c) for c in bad4]}. NON-empty, unlike n = 3, "
          f"and under 1 % of the candidate set -- the SDP is a real selector "
          f"here", w)

    # ---------------------------------------------------------------- CHECK 8
    # The parity echo, checked rather than admired.
    check("alternating_word_is_feasible_iff_its_power_is_even",
          all(feas == (m % 2 == 0) for m, feas in
              ((k // 2, v) for k, v in alt_feas.items())),
          f"(v0 v1)^m PSD-feasible by m: "
          f"{{{', '.join(f'{k // 2}: {v}' for k, v in alt_feas.items())}}} -- "
          f"feasible iff m is EVEN, which is the same parity rule the H_2 "
          f"gluon vertex obeys (sigma_0^k PSD iff k even, "
          f"h2_psdFeasible_iff_even, sorry-free). The smallest derived "
          f"candidate is (v0 v1)^2: four vertices, eight letters", w)

    # ---------------------------------------------------------------- CHECK 9
    # THE MECHANISM, and the discriminator that the feasibility is not trivial.
    # The parity rule is not an analogy with H_2 -- it is the same cause: a
    # NEGATIVE eigenvalue. And (v0 v1)^2 must be PSD because it is positive,
    # not because it is the identity, or "selection" would be vacuous.
    spec = {}
    for shape, (sig, dim) in B4.items():
        M = mp.eye(dim)
        for i in (0, 1):
            M = M * sig[i] * (sig[i + 1] - H0 * mp.eye(dim))
        Msym = mp.matrix([[(M[i, j] + M[j, i]) / 2 for j in range(dim)]
                          for i in range(dim)])
        ev = sorted(mp.eigsy(Msym, eigvals_only=True))
        dev_I = max(abs(M[i, j] - (1 if i == j else 0))
                    for i in range(dim) for j in range(dim))
        spec[shape] = ([mp.nstr(e, 12) for e in ev], mp.nstr(dev_I, 6))
    three = [sh for sh, (sig, dim) in B4.items() if dim == 3]
    expect = sorted([-Q0 ** 2, -Q0 ** -2, mp.mpf(1)])
    ok_spec = True
    for sh in three:
        sig, dim = B4[sh]
        M = mp.eye(dim)
        for i in (0, 1):
            M = M * sig[i] * (sig[i + 1] - H0 * mp.eye(dim))
        Msym = mp.matrix([[(M[i, j] + M[j, i]) / 2 for j in range(dim)]
                          for i in range(dim)])
        got = sorted(mp.eigsy(Msym, eigvals_only=True))
        if any(abs(g - e) > mp.mpf("1e-20") for g, e in zip(got, expect)):
            ok_spec = False
    # (v0 v1)^2 must be genuinely positive, i.e. NOT the identity
    sq_nontrivial = []
    for sh in three:
        sig, dim = B4[sh]
        M = mp.eye(dim)
        for i in (0, 1, 0, 1):
            M = M * sig[i] * (sig[i + 1] - H0 * mp.eye(dim))
        dev = max(abs(M[i, j] - (1 if i == j else 0))
                  for i in range(dim) for j in range(dim))
        sq_nontrivial.append(dev > mp.mpf("1e-3"))
    check("parity_rule_mechanism_is_a_negative_eigenvalue_not_an_analogy",
          ok_spec and all(sq_nontrivial),
          f"in BOTH 3-dimensional blocks {three}, the spectrum of v0 v1 is "
          f"exactly {{-q^2, -q^-2, 1}} = "
          f"{[mp.nstr(e, 12) for e in expect]} -- two NEGATIVE eigenvalues, "
          f"so odd powers cannot be PSD and even powers have spectrum "
          f"{{q^-4, 1, q^4}}. That is the SAME cause as the H_2 rule "
          f"(sigma_0 has eigenvalue -1/q), not an analogy with it. And "
          f"(v0 v1)^2 is NOT the identity in either block "
          f"(max |M - I| > 1e-3), so its feasibility is genuine positivity "
          f"rather than triviality -- without this the 'selection' would be "
          f"vacuous", w)
    w.add_data("mechanism", {
        "spectrum_of_v0v1_per_block": {str(k): v[0] for k, v in spec.items()},
        "max_dev_from_identity_per_block": {str(k): v[1]
                                            for k, v in spec.items()},
        "three_dim_blocks_spectrum": "{-q^2, -q^-2, 1}",
        "even_power_spectrum": "{q^-4, 1, q^4}",
        "note": "the 1-dim and (2,2) blocks send every power to the identity; "
                "all the discrimination lives in the two 3-dim blocks, which "
                "carry identical spectra"})

    # ------------------------------------------------------------------ data
    w.add_data("h3_vertex", {
        "a": str(sp.factor(a_s)), "a_prime": str(sp.factor(ap_s)),
        "a_prime_is_z_D": True,
        "det": "1", "trace": "-1 - h^2",
        "trace_at_q0": mp.nstr(trV, 20),
        "one_dim_blocks": {str(k): v for k, v in one_dim.items()},
        "V_cubed_eq_one_iff": "q = 1 (classical limit)"})
    w.add_data("controls", {
        "h2_parity_rule": [[k, f] for k, f in parity],
        "sigma0_sq_feasible_sigma0_not": {str(k): list(v)
                                          for k, v in ctrl.items()}})
    # 🛑 Derived from the measurement, never written as a literal. The first
    # draft hardcoded `[]` here and "0 of ..." in the printed summary, and the
    # n = 4 run then found TWO feasible words -- so the witness and the screen
    # would both have asserted the opposite of what the file had just measured.
    # The assertion caught it only because it tested `bad4` instead of
    # restating the intent.
    w.add_data("feasibility", {
        "n3_powers_tested": KMAX_POW,
        "n3_feasible": [k for k, f in enumerate(feas3, start=1) if f],
        "n4_words_tested": n_words,
        "n4_feasible": [list(c) for c in bad4],
        "max_trace_n3": mp.nstr(max_tr, 20)})
    w.add_data("lean", [
        "QOU.Mass.PsdDetOneTrace.trace_ge_two -- a real PSD 2x2 of det 1 has "
        "trace >= 2",
        "QOU.Mass.PsdDetOneTrace.eq_one_of_trace_eq_two -- equality only for "
        "the identity",
        "QOU.Mass.PsdDetOneTrace.not_posSemidef_of_trace_lt_two -- the form "
        "used here",
        "QOU.Mass.GammaGammaWordSelection.h2_psdFeasible_iff_even -- the "
        "control this file reproduces"])
    w.add_data("scope", "a")
    w.add_data("qou_ales_two_halves", {
        "n3": "EMPTY -- gamma-gamma production and PSD-feasibility have no "
              "common non-empty solution on three strands at q_0",
        "n4": "NON-EMPTY and selective -- 5 of 8190 words to 12 vertices",
        "smallest_derived_candidate": "(v0 v1)^2, four vertices, eight letters",
        "parity_rule": "(v0 v1)^m feasible iff m even -- the same rule as the "
                       "H_2 gluon vertex sigma_0^k",
        "not_claimed": [
            "the feasible set is NOT characterised, only enumerated to 12 "
            "vertices; the two sporadic 10-vertex words show it is not merely "
            "the even alternating family, and nothing here explains them",
            "no cost / minimality is computed -- SDPSelected also requires "
            "minimal cost among feasible candidates, so this narrows the "
            "candidate set without selecting a word",
            "no observable is computed and no Q_beta comparison is made"]})
    w.add_data("basis", "orthogonal Hoefsmit (symmetric generators, CHECK 0); "
                        "PSD is invariant under the remaining orthogonal "
                        "freedom, so the verdicts are basis-free")
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)

    print()
    print(f"  H_3 gamma-gamma vertex: det = 1, tr = -1 - h^2 = "
          f"{mp.nstr(trV, 16)}  (elliptic)")
    print(f"  1-dim blocks -> {one_dim}")
    print(f"  V^3 = 1 iff q = 1; at q_0 it is not")
    print(f"  n = 3: {sum(1 for f in feas3 if f)} of {KMAX_POW} powers "
          f"PSD-feasible (max tr = {mp.nstr(max_tr, 12)} < 2)")
    print(f"  n = 4: {len(bad4)} of {n_words} gamma-gamma words PSD-feasible")
    for c in bad4:
        print(f"         feasible: {c}")

    w.save()
    print()
    if FAILED:
        print(f"FAILED ({len(FAILED)}): {', '.join(FAILED)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
