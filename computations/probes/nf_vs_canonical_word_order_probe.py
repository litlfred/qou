#!/usr/bin/env python3
"""Localise the A=1 NF-vs-canonical trace residual (bean `qou-hu1f`).

`qou-hu1f` measured that at hydrogen (A=1) the NF route's Markov trace and
the canonical `tr_M_atom` differ by **5.045e-4**, and named the decisive
next test: run the 2026-05-19 `TR_M[5]` audit's own per-basis-element check
under convention D, so the residual is localised to the `TR_M` weights, the
`y_lambda`, or the reduced-block characters.

THE ANSWER IS: NONE OF THE THREE.  All four checks below are measurements,
not readings.

1. The Markov/Frobenius identity `TR_M[i] == sum_lam y_lam chi^lam(b_i)`
   holds on ALL SIX NF basis elements to ~1e-62 (the arithmetic floor at
   60 dps).  The corpus invariant that caught the 2026-05-19 bug is intact
   in convention D.

2. Feeding `hm_mp` the CANONICAL word reproduces the canonical Frobenius
   pairing to ~1e-62.  So `hm_mp` and `TR_M` compute the pairing correctly
   for whatever word they are given.

3. `build_atom_nf_mp` traces a DIFFERENT WORD from `atom_braid_word_3A`.
   Same 11-letter multiset (6 sigma_0, 1 averaged on gen 0, 3 sigma_1^-1,
   1 averaged on gen 1); different ORDER.  H_3 is non-commutative, so these
   are different algebra elements, and that difference is the whole residual.

       canonical (mass_at_3A_proper.atom_braid_word_3A), grouped by generator:
           s0 s0 s0 s0 A0 s0 s0 | S1 S1 S1 A1
       NF route (compound_shift_nf.build_atom_nf_mp), interleaved:
           s0 S1 s0 S1 s0 S1 s0 A0 A1 s0 s0
       (s = sigma, S = sigma^-1, A = averaged sigma - (h/2)*1; digit = gen.)

4. Both orderings are DELIBERATE and each cites a source. `pyhecke.atom.
   build_atom_nf` -- which `build_atom_nf_mp` says it mirrors -- comments its
   loop "B_3 confinement (3 interleaved sigma_0, sigma_1^-1)".
   `atom_braid_word_3A` says it "Matches the chain-walk convention of
   hecke_core.atom_per_generator_volumes".  Two conventions, two sources,
   one disagreement.

WHY THE ORDER IS NOT COSMETIC.  `(sigma_0 sigma_1^-1)^3` is the standard
braid word for the BORROMEAN RINGS; the interleaved route's intra-nucleon
core is exactly that.  The grouped route contains no such subword.  The
framework's mass law is built on the Borromean braid (`F_Bor =
|tr_M(beta_Bor)|*[3]_q!/q^3`), so which of the two the binding surface
actually traces is a question about the physics, not about formatting.

5. WHICH WORD IS CORRECT IS A MEASUREMENT, NOT A JUDGEMENT CALL.  The mass
   law's Borromean factor has a Lean-proved closed form (BorromeanMarkovTrace
   .lean, used by `m_p_substrate_identity_50dps.trM_borromean`):

       |tr_M(beta_Bor, q)| = (4 + h^2 - 3h^4 - h^6) / (h^2 + 4)

   Tested against both candidate intra-nucleon confinement words:

       (sigma_0 sigma_1^-1)^3   interleaved   agrees to 1.9e-50  <- IS beta_Bor
       sigma_0^3 sigma_1^-3     grouped       off by 82 %

   So the interleaved ordering IS the Borromean braid the framework's own mass
   law names, verified against Lean.  The grouped ordering is a different
   object.  `atom_braid_word_3A` -- the canonical route feeding `tr_m_atom_zn`
   -> `binding_canonical` -> the binding surface -- uses the GROUPED one.

SCOPE.  This localises the A=1 residual, establishes that the two routes trace
different words, and identifies which of the two is the Borromean braid.  It
does NOT show that any binding NUMBER is wrong: binding is not the mass
identity, and whether `binding_canonical` needs beta_Bor at all is a separate
question this probe does not answer.  Framed in bean `qou-hu1f`.

Precision: mpmath end to end, 60 dps, proton pin via `q_at(55)`.  No float64.
Emits no witness: every number here is a property of two source files at one
commit, re-derived in seconds, not a substrate measurement to be cited.
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

from mpmath import mp  # noqa: E402

import q_parameter as qp  # noqa: E402
from compound_shift_nf import (  # noqa: E402
    NF_BASIS, NF_NAMES, build_atom_nf_mp, hm_mp, tr_m_weights_mp,
)
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

SHAPES3 = [(3,), (2, 1), (1, 1, 1)]
FLOOR = mp.mpf("1e-40")


def _trM(word, y, cache):
    """sum_lam y_lam chi^lam(word); word = [(c, d, gen)] meaning c*sigma_g + d*1."""
    tot = mp.mpf(0)
    for shape in SHAPES3:
        y_s = y.get(shape, mp.mpf(0))
        if y_s == 0:
            continue
        sigmas, dim, _ = seminormal_matrices_mp(shape, cache=cache)
        if dim == 0:
            continue
        M = mp.eye(dim)
        for c, d, g in word:
            M = M * (mp.mpf(c) * sigmas[g] + mp.mpf(d) * mp.eye(dim))
        tot += y_s * mp.fsum(M[i, i] for i in range(dim))
    return tot


def _nf_of(word, h):
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for c, d, g in word:
        nf = hm_mp(nf, mp.mpf(c), mp.mpf(d), g, h)
    return nf


def _kind(d, h):
    d = mp.mpf(d)
    if abs(d) < FLOOR:
        return "s"
    if abs(d + h) < FLOOR:
        return "S"
    if abs(d + h / 2) < FLOOR:
        return "A"
    return "?"


def main() -> int:
    mp.dps = 60
    q = qp.q_at(55)
    h = q - 1 / q
    cache = BlockCacheMP(q)
    y3 = y_lambda_su_n(3, q, 2)
    TR = tr_m_weights_mp(60)
    checks = []

    print(f"q (proton pin) = {mp.nstr(q, 30)}\n")

    # 1 -- the identity on the six NF basis elements
    print("1. Markov/Frobenius identity on the NF basis (convention D)")
    worst = mp.mpf(0)
    for i, (name, word) in enumerate(zip(NF_NAMES, NF_BASIS)):
        frob = _trM([(1, 0, g) for g in word], y3, cache)
        rel = abs(TR[i] - frob) / abs(TR[i]) if TR[i] != 0 else abs(TR[i] - frob)
        worst = max(worst, rel)
        print(f"   {name:>3}  TR_M={mp.nstr(TR[i], 22):>26}  "
              f"Frob={mp.nstr(frob, 22):>26}  rel={mp.nstr(rel, 6)}")
    ok1 = worst < mp.mpf("1e-45")
    checks.append(("identity_holds_on_nf_basis", ok1,
                   f"worst rel over 6 basis elements = {mp.nstr(worst, 6)}"))
    print(f"   -> worst {mp.nstr(worst, 6)}  ({'PASS' if ok1 else 'FAIL'})\n")

    # 2 -- hm_mp reproduces the pairing on the canonical word
    canon = atom_braid_word_3A(1, 0, include_inter=True, q=q)
    t_canon = _trM(canon, y3, cache)
    nf_canon = _nf_of(canon, h)
    t_hm = mp.fsum(nf_canon[i] * TR[i] for i in range(6))
    rel2 = abs(t_hm - t_canon) / abs(t_canon)
    ok2 = rel2 < mp.mpf("1e-45")
    checks.append(("hm_mp_reproduces_pairing", ok2, f"rel = {mp.nstr(rel2, 6)}"))
    print("2. hm_mp fed the CANONICAL word vs the Frobenius pairing")
    print(f"   trM(canonical)      = {mp.nstr(t_canon, 25)}")
    print(f"   hm_mp(canonical)    = {mp.nstr(t_hm, 25)}")
    print(f"   -> rel {mp.nstr(rel2, 6)}  ({'PASS' if ok2 else 'FAIL'})\n")

    # 3 -- the two routes trace different words
    nf_route = build_atom_nf_mp(1, 0, dps=55)
    t_nf = mp.fsum(nf_route[i] * TR[i] for i in range(6))
    rel3 = abs(t_nf - t_canon) / abs(t_canon)
    ok3 = mp.mpf("1e-5") < rel3 < mp.mpf("1e-2")
    checks.append(("residual_is_the_known_5e-4", ok3, f"rel = {mp.nstr(rel3, 6)}"))
    print("3. build_atom_nf_mp (its own ordering) vs the canonical word")
    print(f"   build_atom_nf_mp    = {mp.nstr(t_nf, 25)}")
    print(f"   -> rel {mp.nstr(rel3, 6)}   <- the qou-hu1f residual\n")

    # 4 -- same multiset, different order
    canon_seq = [(_kind(d, h), g) for _c, d, g in canon]
    nf_seq = [("s", 0), ("S", 1)] * 3 + [
        ("s", 0), ("A", 0), ("A", 1), ("s", 0), ("s", 0)]
    same_multiset = Counter(canon_seq) == Counter(nf_seq)
    diff_order = canon_seq != nf_seq
    ok4 = same_multiset and diff_order
    checks.append(("same_multiset_different_order", ok4,
                   f"multiset equal={same_multiset}, order differs={diff_order}"))
    print("4. The two words, letter by letter")
    print(f"   canonical : {' '.join(k + str(g) for k, g in canon_seq)}")
    print(f"   NF route  : {' '.join(k + str(g) for k, g in nf_seq)}")
    print(f"   same multiset: {same_multiset}   order differs: {diff_order}\n")

    # 5 -- which word is the Borromean braid? (Lean-proved closed form)
    closed = (4 + h**2 - 3*h**4 - h**6) / (h**2 + 4)
    one, zero = mp.mpf(1), mp.mpf(0)
    inter = [(one, zero, 0), (one, -h, 1)] * 3
    group = [(one, zero, 0)] * 3 + [(one, -h, 1)] * 3
    t_i, t_g = abs(_trM(inter, y3, cache)), abs(_trM(group, y3, cache))
    rel_i = abs(t_i - abs(closed)) / abs(closed)
    rel_g = abs(t_g - abs(closed)) / abs(closed)
    ok5 = rel_i < mp.mpf("1e-45") < rel_g
    checks.append(("interleaved_is_the_borromean_braid", ok5,
                   f"interleaved rel={mp.nstr(rel_i, 6)}, grouped rel={mp.nstr(rel_g, 6)}"))
    print("5. Which word is the Borromean braid? (vs the Lean closed form)")
    print(f"   |tr_M(beta_Bor)| Lean = {mp.nstr(abs(closed), 25)}")
    print(f"   (s0 s1^-1)^3 interleaved = {mp.nstr(t_i, 25)}  rel {mp.nstr(rel_i, 6)}")
    print(f"   s0^3 s1^-3   grouped     = {mp.nstr(t_g, 25)}  rel {mp.nstr(rel_g, 6)}")
    print("   -> the INTERLEAVED word is beta_Bor; the grouped one is not.\n")

    print("=" * 68)
    for name, ok, note in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}")
    n_ok = sum(1 for _n, ok, _t in checks if ok)
    print(f"{n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
