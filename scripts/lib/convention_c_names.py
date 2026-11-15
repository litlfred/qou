"""Is an identifier DECLARING itself convention C?

The single definition behind the `DELIBERATE` check that
`convention-c-producer-audit.py` and `convention-c-producer-migrate.py` used to
carry as two copies of one regex, and that `convention-c-triage.py` consumes
through `migrate._file_has_c_reference` to reach a B3 "deliberate comparison --
leave it" verdict.

## Why this is not a regex any more

The copies read

    DELIBERATE = re.compile(r"(_c\\b|_C\\b|C_|_c_|zc$|z_c)", re.I)

and `re.I` folds the `C_` alternative into `c_`, so the pattern matched the
substring `c_` **inside ordinary identifiers**. Not a corner case: it fired on
`c_k` (the Q_beta truncation-ladder coefficients, 128 occurrences), on
`q_fac_n` and `qfac_3` (quantum factorials), on `c_mp`, `c_sigma1`, `c_4`,
`desc_tr_M` -- and on `__doc__`, `exec_module`, `spec_from_file_location`,
`cyclotomic_poly`, `basic_edges` and `MAGIC_NUMBERS`, none of which is a
mathematical object at all.

Measured on `main` 2026-08-25, over every identifier in `computations/`,
`qou-mass/` and `tools/`: **1112 distinct names, 5316 occurrences**, matched
only through that collision.

The failure is asymmetric in the dangerous direction. A *false* "deliberate"
tells an agent working the drain that a site is intentional comparison code and
may be skipped, so a genuine defect survives the sweep wearing an excuse.
`computations/audits/weight_factor_audit.py` was classed B3 on `__doc__` and
`q_fac_n` and is a real defect -- it asserted `z_C` AS THE SPECIFICATION, so a
correctly-migrated consumer would have failed against it. It was found only
because a human read the site instead of trusting the verdict (PR #5738).

## What replaces it

Three case-aware patterns instead of one case-folded blob. The corpus
CAPITALISES the convention label (`z_C`, `pin_C`, `Z_C`), and it is the
lowercase `c` that is ambiguous -- `c` is colour in the notation register, and
`c_k` is a ladder coefficient. So a lowercase `c` counts only when anchored to
`z`, the Markov parameter itself, or spelled out as the word "convention".

Deliberately NOT matched, each verified against the corpus rather than assumed:

* **A bare `C`.** 598 occurrences across 162 files, and it is a Wedderburn
  block label (`A, C, D = 1.0, 1.0, 1.0`) or the multiplicative Jucys-Murphy
  Casimir `C = sum_k L_k`, never a convention. The old regex did not match it
  either, so excluding it is not a regression.
* **A trailing camelCase `C` on an arbitrary name** -- `detC`, `okC`, `aC`,
  `rC`, `yC`. This looks like the obvious widening and was measured before
  being rejected: of the 50 distinct names it would add, hand-classification
  put roughly 22 genuine against 26 false, **~45 % precision**. The false half
  is not marginal -- `CShR4` is a free cumulant, `SL2C` is SL(2,C),
  `coefsC`/`rootsC`/`real_rootsC` are polynomial-variant names, `worstC` and
  `numC`/`denC` are the third term in an A/B/C series. A detector at 45 %
  precision trains its readers to ignore it, which is worse than the gap it
  closes. The genuine members of that set (`detC` on `GC.det()`, `redC` from
  `run("convention C (excised)", Z_C)`) live in files that already carry a real
  `z_C`, so the verdict is unchanged in every case measured.

  **This is a known blind spot, stated rather than closed.** A file whose ONLY
  convention-C marker is a camelCase name like `zPrimeC`, with no underscored
  `_C` and no `z`+`c` adjacency anywhere, is invisible here.

* **A site whose deliberateness is in the GUARD, not in any name.** Measured
  2026-10-10 on `main` `ac111c1814`, and it is the first observed instance of
  the trade above being paid: `convention-c-triage.py` reports
  `computations/qbeta/qbeta_ck_cache.py:140` as `deliberate=False`, bucket
  "computations -- live producers". It is the canonical `c_k` producer, the file
  AGENTS.md's own `c_k` banner names -- and the site is correct. Its target is a
  bare ``z``::

      # Convention C, reached ONLY via the explicit --historical-convention-C
      # flag. C was excised by owner ruling (2026-08-09, re-affirmed 2026-08-15
      # and 2026-08-26); this path exists solely so the committed witness stays
      # machine-reproducible, and it is never the default.
      z = sqrt(q) / (1 + q)

  The deliberateness lives in a ``convention != "C"`` raise, a function
  parameter and a CLI flag; the D path prints REFUSING TO RUN and exits 2, and
  the whole site is adjudicated `completed` under bean ``qou-ckwt``. **No
  name-keyed check can see any of that**, however the patterns are widened --
  there is no identifier to widen onto.

  Recorded rather than fixed, because the DIRECTION is the acceptable one. This
  under-blocks: a false "actionable" costs a reader one site visit. The `re.I`
  bug this module replaced over-blocked, and a false "deliberate" told an agent
  to skip a real defect (bean ``qou-4bq3``). Entry 52 in
  ``docs/audits/2026-08-15-detector-blindness-taxonomy.md``.

Net effect, measured the same day: 1112 distinct names dropped, **2 gained**
(`zc1`, `zC0`, both genuine, reached by the digit lookahead), and **0 genuine
convention-C labels lost** -- the only dropped names that even look relevant,
`c_Z` and `c_z`, are polynomial coefficients (`c_Z = mpf(str(coeffs_Z[j]))`,
`n_z, c_z = vanishing_order(...)`), not labels.
"""

from __future__ import annotations

import re

#: A capital ``C`` delimited by underscores or the ends of the name: the
#: corpus capitalises the convention label. ``z_C``, ``pin_C``,
#: ``census_hopf_C``, ``r_C``, ``C_LABEL``, ``z_C_expr``. CASE-SENSITIVE,
#: which is the entire point -- ``c_k`` and ``q_fac_n`` must not match.
_C_TOKEN = re.compile(r"(?:^|_)C(?:_|$)")

#: ``z``-anchored, EITHER case, with the camelCase run-together spelling
#: allowed. The Markov parameter is ``z``, so ``z`` followed by ``c`` is
#: unambiguous where a bare ``c`` is not: ``z_c``, ``z_C``, ``zC``, ``zc``,
#: ``zc_s``, ``zc1``, ``zC0``, ``Z_C``. The trailing alternative accepts a
#: separator, the end of the name, or a capital/digit boundary -- but NOT a
#: lowercase letter, so ``zcd_ratio`` and ``zeta_c`` stay clear.
_Z_C = re.compile(r"(?:^|_)[zZ]_?[cC](?:_|$|(?=[A-Z0-9]))")

#: The convention spelled as a word: ``convention_c``, ``conv_C``,
#: ``check_convention_c``, ``y_lambda_at_q0_mpmath_convention_C_HISTORICAL``.
_CONV_C = re.compile(r"(?:^|_)(?:conv|convention)_?[cC](?:_|$)", re.I)


def deliberate_c_kind(name: str):
    """Which convention-C spelling `name` declares, or None.

    Returns a short tag naming the pattern that fired -- ``"z_C"``, ``"_C_"``
    or ``"convention_C"`` -- so a caller can report the BASIS of a verdict
    rather than a bare boolean. That is not cosmetic: the whole cost of the old
    regex was that "this file references a C-named symbol" gave a reader no way
    to see the symbol was `__doc__`.
    """
    if not name or name == "C":
        return None
    for rx, kind in ((_Z_C, "z_C"), (_C_TOKEN, "_C_"), (_CONV_C, "convention_C")):
        if rx.search(name):
            return kind
    return None


def is_deliberate_c_name(name: str) -> bool:
    """Boolean form of :func:`deliberate_c_kind`."""
    return deliberate_c_kind(name) is not None


#: Fixtures shared by both scripts' ``--selftest``. Kept here so the two
#: cannot drift apart the way the two regex copies did.
#:
#: The MUST_NOT half is the regression lock for the ``re.I`` collision: every
#: entry below matched the old pattern, and seven of them are named in bean
#: ``qou-4bq3`` as the basis of a false B3 verdict.
SELFTEST_MUST_MATCH = (
    "z_C", "z_c", "zC", "zc", "Z_C", "zc_s", "zc1", "zC0",
    "z_C_expr", "z_C_num", "z_C_of_t", "z_C_alt", "z_C_s",
    "pin_C", "census_hopf_C", "trM_C", "W2_C", "r_C", "C_LABEL",
    "convention_c", "conv_C", "check_convention_c",
    "y_lambda_at_q0_mpmath_convention_C_HISTORICAL",
)

SELFTEST_MUST_NOT_MATCH = (
    # bean qou-4bq3: the seven false-B3 bases, measured on main
    "q_fac_n", "qfac_3", "c_mp", "c_Lminus", "c_Lplus", "c_e_minus",
    "c_sigma1", "c_4", "__doc__",
    # found here 2026-08-25, NOT in the bean: an eighth false B3
    "desc_tr_M",
    # the ladder coefficients, 128 occurrences and the most-matched name of all
    "c_k", "c_k_ladder",
    # plain Python and unrelated maths the old regex also swept up
    "exec_module", "spec_from_file_location", "cyclotomic_poly",
    "MAGIC_NUMBERS", "basic_edges", "abc_",
    # polynomial coefficients that merely LOOK convention-relevant
    "c_Z", "c_z",
    # a bare C is a Wedderburn block / the Jucys-Murphy Casimir, 598 uses
    "C",
    # near misses that must stay clear of the z-anchor
    "z", "z_mark", "z_markov", "Z_MARK", "markovZ_prime", "zeta_c",
    "zcd_ratio",
)


def selftest_rows():
    """Yield ``(label, ok)`` rows for a caller's ``--selftest`` output."""
    for n in SELFTEST_MUST_MATCH:
        yield (f"deliberate-C name is recognised: {n}", is_deliberate_c_name(n))
    for n in SELFTEST_MUST_NOT_MATCH:
        yield (f"ordinary identifier is NOT convention C: {n}",
               not is_deliberate_c_name(n))
