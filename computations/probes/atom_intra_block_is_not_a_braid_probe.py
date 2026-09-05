#!/usr/bin/env python3
"""The atom word's intra-nucleon block is NOT a braid, so it is not beta_Bor.

Bean `qou-hu1f`. This probe answers that bean's own named-but-unrun next
measurement, and in answering it RETRACTS the framing the question was asked
in -- which was mine, written into `qou-hu1f` and into PR #6712 on 2026-09-05.

WHAT THE BEAN ASKED
    "does anything downstream of `atom_braid_word_3A` depend on its
     intra-nucleon block *being* beta_Bor?"

    That question presupposes the block is a braid, and offers two candidates:
    interleaved `(s0 s1^-1)^3` (which IS beta_Bor) and grouped `s0^3 s1^-3`
    (which is 82 % away). The bean asserts the canonical route "uses the
    grouped one".

WHAT IS ACTUALLY TRUE (checks 1-3 below)
    The production intra-nucleon block is ELEVEN letters, two of which are
    AVERAGED -- `sigma - (h/2)*1 = (sigma + sigma^-1)/2`, which is provably
    outside the image of `rho : B_n -> H_n(q)`. So the block:

      * is not `s0^3 s1^-3`               (that is 6 letters, all braid)
      * is not `(s0 s1^-1)^3` = beta_Bor  (likewise 6 letters, all braid)
      * is NOT A BRAID AT ALL, hence cannot be beta_Bor even in principle

    and its |tr_M| is 14.7 % from the Lean closed form, not 82 %.

    This is not a defect and not a discovery: `atom_braid_word_3A`'s own
    docstring says it in as many words ("the returned object lies in H_n(q)
    and is NOT in the image of rho"), carries the `2A + 1` count of averaged
    letters, and warns the NAME IS A MISNOMER. I read the two candidate braid
    words off a reading of the construction instead of off the object, which
    is the same defect this corpus recorded one day earlier as
    "a source-reading of a word ordering is not evidence about the word" --
    committed, and then repeated.

WHAT THE ANSWER TO THE BEAN'S QUESTION IS (check 4)
    Nothing downstream can depend on the block being beta_Bor, because the
    two routes are DISJOINT. The mass law reaches beta_Bor through the
    Lean-proved closed form, never through the word builder:

      canonical_mass -> m_p_substrate_identity_50dps.F_Bor
                     -> _h4_substrate.trM_borromean_closed(q)
                     =  (4 + h^2 - 3h^4 - h^6)/(h^2 + 4)

    All three of those files contain ZERO references to `atom_braid_word_3A`
    (check 4 asserts this by reading them). The word builder feeds the OTHER
    route -- `tr_m_atom_zn` -> `binding_canonical`, and `derived_masses`'
    `M(h) = rho*[|tr_M(T_w)| + tower(T_w) + tr_M(C_dim_q)]` with
    `T_w = atom_braid_word_3A(Z, N)`.

SCOPE -- what this does and does not establish
    Establishes: the block is not a braid; the mass law does not consume it;
    the "grouped vs interleaved" dichotomy was a false one.
    Does NOT establish: that the 14.7 % gap is acceptable, or that the
    binding route SHOULD be using a non-braid object. Those are live
    questions and this probe does not touch them. In particular the
    averaging is what makes the object non-topological -- by the producer's
    own docstring `tr_M` of it is a weighted sum of 2^(2A+1) link
    invariants, so no volume, crossing number or genus may be read off it.

Precision: mpmath end-to-end at 60 dps. No float64 anywhere -- there is no
builtin-float coercion in this file, not even for display, and no numpy /
statistics / math import. (This sentence deliberately avoids naming the
builtin with its parenthesis: the first draft asserted its own absence in a
form that a grep for the coercion matched, so the file refuted its own claim
to any checker cheap enough to run. Same class as the detector-blindness
taxonomy in docs/audits/2026-08-15-detector-blindness-taxonomy.md.)
Emits no witness: it records a structural fact about code, not a derived
physical number.

Run:
    PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python \
      python3 -u computations/probes/atom_intra_block_is_not_a_braid_probe.py
"""

from __future__ import annotations

import pathlib
import sys

import mpmath as mp

mp.mp.dps = 60

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from compound_shift_nf import hm_mp  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[2]
TOL = mp.mpf("1e-40")

Q = q_at(55)
H = Q - 1 / Q
# Convention D (owner ruling 2026-08-15): z = q^3/(q^2 + 1).
Z_D = Q**3 / (Q**2 + 1)
# tr_M on the six H_3 normal-form basis elements, convention D.
TR_M = [mp.mpf(1), Z_D, Z_D, Z_D**2, Z_D**2, H * Z_D**2 + Z_D]

# The Lean-proved closed form, QOU.BraidsAndKnots.trM_borromean:
#     |tr_M(beta_Bor, q)| = (4 + h^2 - 3h^4 - h^6) / (h^2 + 4)
LEAN_BOR = abs((4 + H**2 - 3 * H**4 - H**6) / (H**2 + 4))


def _mpf(x):
    """Coerce a word coefficient to mpf without ever passing through float."""
    return x if isinstance(x, mp.mpf) else mp.mpf(str(x))


def letter_kind(d) -> str:
    """Classify a letter by its `d` coefficient in `c*sigma_g + d*1`.

    d == 0    -> sigma        (a braid generator)
    d == -h   -> sigma^-1     (a braid generator, since sigma^-1 = sigma - h)
    otherwise -> AVERAGED     (NOT in the image of rho)
    """
    dm = _mpf(d)
    if dm == 0:
        return "sigma"
    if abs(dm + H) < TOL:
        return "sigma^-1"
    return "averaged"


def trm_of(word) -> mp.mpf:
    """tr_M of a word given as (c, d, gen) triples, via the H_3 normal form."""
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for c, d, g in word:
        nf = hm_mp(nf, _mpf(c), _mpf(d), g, H)
    return mp.fsum(nf[i] * TR_M[i] for i in range(6))


BETA_BOR = [(mp.mpf(1), mp.mpf(0), 0), (mp.mpf(1), -H, 1)] * 3
GROUPED = [(mp.mpf(1), mp.mpf(0), 0)] * 3 + [(mp.mpf(1), -H, 1)] * 3

MASS_LAW_CONE = [
    "computations/canonical_mass.py",
    "computations/m_p_substrate_identity_50dps.py",
    "computations/_h4_substrate.py",
]


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # ---- 1. the production block is 11 letters, 2 of them averaged --------
    block = atom_braid_word_3A(1, 0, q=Q, include_inter=False)
    kinds = [letter_kind(d) for _, d, _ in block]
    n_avg = kinds.count("averaged")
    print(f"[1] production intra-nucleon block (proton, include_inter=False)")
    print(f"    letters               : {len(block)}")
    print(f"    sigma / sigma^-1 / avg: "
          f"{kinds.count('sigma')} / {kinds.count('sigma^-1')} / {n_avg}")
    ok1 = len(block) == 11 and n_avg == 2
    checks.append(("block is 11 letters with 2 averaged", ok1,
                   f"len={len(block)} averaged={n_avg}"))

    # ---- 2. therefore it is NOT a braid ----------------------------------
    #        The producer's own docstring states this; we assert it against
    #        the object rather than trusting the docstring.
    ok2 = n_avg > 0
    print(f"[2] block is outside the image of rho : B_n -> H_n(q): {ok2}")
    print(f"    an averaged letter is (sigma + sigma^-1)/2, not a generator")
    checks.append(("block is NOT a braid word", ok2,
                   f"{n_avg} non-braid letters"))

    # ---- 3. the three |tr_M| values, and the two gaps that matter --------
    v_block = abs(trm_of(block))
    v_bor = abs(trm_of(BETA_BOR))
    v_grouped = abs(trm_of(GROUPED))
    gap_block = abs(v_block - LEAN_BOR) / LEAN_BOR
    gap_bor = abs(v_bor - LEAN_BOR) / LEAN_BOR
    gap_grouped = abs(v_grouped - LEAN_BOR) / LEAN_BOR
    print(f"[3] |tr_M| against the Lean closed form "
          f"{mp.nstr(LEAN_BOR, 25)}")
    for nm, v, g in (
        ("REAL production block", v_block, gap_block),
        ("interleaved (s0 s1^-1)^3 = beta_Bor", v_bor, gap_bor),
        ("grouped s0^3 s1^-3", v_grouped, gap_grouped),
    ):
        print(f"    {nm:38s} {mp.nstr(v, 25):28s} rel {mp.nstr(g, 6)}")
    # interleaved reproduces the Lean form at the arithmetic floor
    ok3a = gap_bor < mp.mpf("1e-50")
    # the production block is ~14.7 %, NOT the 82 % the bean claimed
    ok3b = mp.mpf("0.14") < gap_block < mp.mpf("0.16")
    checks.append(("interleaved IS beta_Bor (Lean closed form)", ok3a,
                   f"rel {mp.nstr(gap_bor, 6)}"))
    checks.append(("production block is ~14.7% off, not 82%", ok3b,
                   f"rel {mp.nstr(gap_block, 6)}"))

    # ---- 4. the mass-law route never touches the word builder ------------
    print("[4] mass-law cone vs the word builder")
    hits = {}
    for rel in MASS_LAW_CONE:
        p = REPO / rel
        n = p.read_text(encoding="utf-8").count("atom_braid_word_3A") if p.exists() else -1
        hits[rel] = n
        print(f"    {rel:52s} atom_braid_word_3A x{n}")
    ok4 = all(v == 0 for v in hits.values())
    checks.append(("mass-law cone has ZERO word-builder references", ok4,
                   repr(hits)))

    print()
    n_ok = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}  ({detail})")
    print(f"\n{n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
