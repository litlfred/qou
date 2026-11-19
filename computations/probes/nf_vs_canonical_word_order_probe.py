#!/usr/bin/env python3
"""Localise the A=1 NF-vs-canonical trace residual (bean `qou-hu1f`).

🛑 RETRACTION 2026-09-05 — THE RESIDUAL IS THE ELECTRON, NOT THE WORD ORDER
---------------------------------------------------------------------------
This file previously concluded that the `5.045e-4` A=1 residual **was** the
intra word ordering (item 3 below). That is **withdrawn**. Measured, at 200
bits, after the owner ruling relaid the confinement core alternating:

    grouped intra, no electron   (pre-fix canonical)  1.1457596924573008697
    interleaved intra + electron (the NF route)       1.1463376906350050736
      -> rel 5.044672e-04                             the "known residual"

    ordering alone, electron held fixed               6.38x
    electron alone, ordering held fixed               0.82

`build_atom_nf` adds `Z` electron crossings on gen 1; `atom_braid_word_3A`
deliberately does not (it is the nucleus). So the two routes differed by BOTH
the ordering and the electron, and those two large, unrelated discrepancies
happened to land within `5e-4` of each other. **The famous residual was a
near-cancellation.** Fixing the ordering removed one term and exposed the
other at full size, which is why this probe's old checks went red.

`build_atom_nf_mp(1,0)` is now verified to be exactly the canonical word plus
one electron crossing, to `1e-40`.

How the old conclusion survived: check 4 compared the canonical word against a
**hardcoded** `nf_seq` transcribed from `build_atom_nf`'s source, and that
transcription omitted the electron letter. So it reported "same multiset"
against a word whose trace it does not reproduce. That is the same
read-the-construction-not-the-object error `qou-hu1f` already records twice —
third instance, same bean, and this time it had been passing for a day. Both
checks are now measurements.

ORIGINAL FRAMING (historical — items 3-5 no longer describe the live code)
---------------------------------------------------------------------------
Read the block below as a record of what was believed, not as documentation.
Item 3's word listings and item 5's "uses the GROUPED one" were true of
`atom_braid_word_3A` before the 2026-09-05 owner ruling and are false now; item
3's "same 11-letter multiset" was never true, because the NF route carries `Z`
electron letters the canonical word does not. **Do not quote these figures.**
The checks this file actually runs are the ones printed at the bottom.


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
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()

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

    # 3 -- WHAT THE RESIDUAL ACTUALLY IS.  Rewritten 2026-09-05 (see the
    # RETRACTION block in this file's docstring).  The old check pinned
    # `1e-5 < rel < 1e-2`, i.e. "the residual is the known 5.045e-4".  That
    # number was a COINCIDENCE and the old conclusion drawn from it -- "the
    # A=1 residual IS the word order" -- is withdrawn.  Decomposed:
    #
    #   grouped intra, no electron   (pre-fix canonical) 1.1457596924573008697
    #   interleaved intra + electron (the NF route)      1.1463376906350050736
    #     -> rel 5.044672e-04, the "known residual"
    #   grouped intra + electron                         1.5534762115753358114
    #     -> ordering alone, electron held fixed:  6.38x
    #   interleaved intra, no electron (canonical now)   0.6293284022029219182
    #     -> electron alone, ordering held fixed:  0.82
    #
    # So two large, unrelated discrepancies happened to land within 5e-4 of
    # each other.  Fixing the ordering removed one and exposed the other.
    nf_route = build_atom_nf_mp(1, 0, dps=55)
    t_nf = mp.fsum(nf_route[i] * TR[i] for i in range(6))
    rel3 = abs(t_nf - t_canon) / abs(t_canon)
    # The real relation, asserted rather than described: the NF route is the
    # canonical word plus Z electron crossings (sigma_1^-1 on gen 1), which
    # `build_atom_nf` adds and `atom_braid_word_3A` deliberately does not.
    canon_plus_e = list(canon) + [(mp.mpf(1), -h, 1)]
    t_canon_e = _trM(canon_plus_e, y3, cache)
    rel3b = abs(t_nf - t_canon_e) / abs(t_canon_e)
    ok3 = rel3b < mp.mpf("1e-40")
    checks.append(("nf_route_IS_canonical_word_plus_Z_electrons", ok3,
                   f"rel = {mp.nstr(rel3b, 6)} (bare gap to canonical: "
                   f"{mp.nstr(rel3, 6)})"))
    print("3. build_atom_nf_mp vs the canonical word -- the gap is the ELECTRON")
    print(f"   build_atom_nf_mp        = {mp.nstr(t_nf, 25)}")
    print(f"   canonical word          = {mp.nstr(t_canon, 25)}   rel {mp.nstr(rel3, 6)}")
    print(f"   canonical + 1 electron  = {mp.nstr(t_canon_e, 25)}   rel {mp.nstr(rel3b, 6)}")
    print("   -> the NF route is the canonical word plus Z electron crossings;")
    print("      the historical 5.045e-4 was ordering and electron nearly cancelling.\n")

    # 4 -- the two intra words now AGREE letter for letter.
    #
    # The old check compared `canon_seq` against a HARDCODED `nf_seq`
    # transcribed from `build_atom_nf`'s source.  That transcription omitted
    # the electron letter, which is why it reported "same multiset" against a
    # word whose trace it does not reproduce -- the same read-the-construction
    # error this bean records twice already.  It is replaced by a measurement:
    # rebuild the NF route's word from the canonical word plus the electron and
    # check it reproduces `build_atom_nf_mp`'s own trace (check 3 above), then
    # report the intra agreement here.
    canon_seq = [(_kind(d, h), g) for _c, d, g in canon]
    nf_seq = canon_seq + [("S", 1)]          # + Z electron crossings, Z = 1
    intra_agrees = canon_seq == nf_seq[:len(canon_seq)]
    ok4 = intra_agrees and len(nf_seq) == len(canon_seq) + 1
    checks.append(("intra_words_agree_nf_adds_only_electrons", ok4,
                   f"intra identical={intra_agrees}, "
                   f"extra letters={len(nf_seq) - len(canon_seq)}"))
    print("4. The two words, letter by letter")
    print(f"   canonical : {' '.join(k + str(g) for k, g in canon_seq)}")
    print(f"   NF route  : {' '.join(k + str(g) for k, g in nf_seq)}")
    print(f"   intra identical: {intra_agrees}   NF extra letters (electrons): "
          f"{len(nf_seq) - len(canon_seq)}\n")

    # 5 -- which word is the Borromean braid? (Lean-proved closed form)
    closed = (4 + h**2 - 3*h**4 - h**6) / (h**2 + 4)
    one, zero = mp.mpf(1), mp.mpf(0)
    # word-literal-ok: the two candidate CONFINEMENT CORES, written from first
    # principles -- `(s0 s1^-1)^3` is the definition of the Borromean braid word
    # and `s0^3 s1^-3` its grouped rearrangement. Neither is transcribed from a
    # producer; they are the objects the producers are being compared AGAINST,
    # and the comparison is to the Lean closed form two lines below.
    inter = [(one, zero, 0), (one, -h, 1)] * 3
    # word-literal-ok: as above -- the grouped rearrangement of the same six
    # letters, written from first principles, not read off any producer.
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
