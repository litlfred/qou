# Constant-consistency audit — coverage record (2026-06-21, axis-2: CLEAN)

Second pass of the constant-consistency sweep (after the q₀ census #2569 and the
cluster-D/vol(4₁) fixes #2576). This axis came back **clean in live compute** —
recorded so future agents don't re-scan these.

## Axes verified consistent

| Quantity | Canonical | Verdict |
|---|---|---|
| **m_μ/m_e** | `206.7682830` (CODATA) | ✅ canonical in all compute; the only variants (`206.7683`, `206.768`) are **display/docstring strings** (`canonical_script_input_audit.py`, `kaon_pion_ratio_7_8_probe.py` print lines), not inputs |
| **m_μ (MeV)** | `105.6583755` | ✅ consistent |
| **Vol(Hopf)** | `0` (non-hyperbolic) | ✅ not hard-coded anywhere — computed/asserted, no nonzero literal |
| **q-bracket `[n]_q`** | balanced `(qⁿ−q⁻ⁿ)/(q−q⁻¹)` | ✅ every `q_int`/`qint` def uses the balanced form — **no** balanced-vs-unbalanced mixing |
| **Vol(Borromean) = 8·G** | `7.327724753417752120…` | ⚠ **SEE CORRECTION BELOW — this ✅ was wrong.** live compute uses the full-precision value; `7.327724753846269` survives only as a *comment* in `experimental_constants.py:136` ("previous f64 value", already centralised), wrong-tail variants only in `_deprecated/` |
| **Catalan G** | `0.9159655941772190150…` | ✅ consistent to the precision tier each consumer needs (sub-floor tail differences only) |

## Standing item (unchanged)

The one real systemic inconsistency remains the **q₀ hardcode staleness** —
**cluster A** (61 live files on the stale pre-re-pin `1.1099785827513808…`),
documented in [`2026-06-21-q0-hardcoded-constant-census.md`](2026-06-21-q0-hardcoded-constant-census.md).
That is the owner-sequenced, witness-regenerating sweep (route q₀ through
`q_parameter.Q`); it is **not** a quick fix and would collide with the active
binding/qbeta work, so it stays deferred.

## Conclusion

Outside the known q₀ cluster-A staleness, the framework's hardcoded constants
are **consistent**. The genuine divergence bugs found this sweep —
`hoefsmit_b` (bar-parity, #2558), cluster-D q₀ in 5 qbeta probes (#2576), and
the 1e-16-wrong vol(4₁) in `t6_tau_h5_embedding_probe.py` (#2576) — are fixed.
The consistency-scan well is dry pending the cluster-A migration.


---

## ⚠ CORRECTION 2026-08-30 — the Vol(Borromean) row's ✅ was FALSE

Bean `qou-f8lit`.

This document certifies `Vol(Borromean) = 8·G` as consistent, on the ground that the bad
value `7.327724753846269` *"survives only as a comment in `experimental_constants.py:136`
… wrong-tail variants only in `_deprecated/`"*.

**It was live in executable Lean.**
`content/quantum-observable-universe/mass-theory/nuclear-knot-classification.lean`
lines 28 and 30 carried

    bindingScale .satellite = m_e * 7.327724753846269
    bindingScale .borromean = m_e * 7.327724753846269

inside a **mass formula** — wrong from digit 11, abs err `4.3e-10` against
`8·G = 7.327724753417752120…`. Every other Lean carrier
(`building-block-knots.vol_borromean`, `categorical-neutron`, `categorical-proton`)
already used `7.32772475341775`, so that file was the outlier rather than an alternative
convention. Corrected on 2026-08-30.

### Why the miss, and what to change about audits like this one

This audit's evidence is entirely about `computations/` — `experimental_constants.py`,
`_deprecated/`. It appears never to have walked `content/**/*.lean`, and **it does not
say which surface it searched**. A reader takes the ✅ as a statement about the corpus;
it was a statement about one directory.

**A "clean" verdict is only as wide as the surface the detector walked.** An audit that
does not record its search surface cannot be re-checked, and its ✅ silently widens over
time into a claim it never made. Future consistency audits should state the globs they
ran, verbatim.

Found by [`scripts/known-constant-literal-audit.py`](../../scripts/known-constant-literal-audit.py),
which compares literals to **computed** constants by value instead of grepping for
known-bad digit strings — the relevant property here being that the same wrong number is
spelled several different ways across the corpus, so a grep for any one of them misses
the others.

**Not re-verified by this correction:** the other five ✅ rows in the table above. They
were audited with the same `computations/`-scoped method and carry the same blind spot;
none has been re-run against `content/`.

---

## RE-VERIFICATION 2026-08-30 — the other five rows, and my own flag was wrong

Bean `qou-f8lit`, same session as the correction above.

The correction closed by saying of the remaining five ✅ rows: *"none has been
re-run against `content/`."* **That was an unmeasured absence — the same defect
the correction is about, one paragraph later.** I asserted a scope claim without
running the check. Measured, four of the five *had* been re-verified against
`content/`, by arcs that landed weeks before I wrote the flag.

Per row, with the surface each verdict rests on stated verbatim:

| row | status 2026-08-30 | who established it |
|---|---|---|
| **m_μ/m_e** | drained, gated | `qou-7ot6` |
| **m_μ (MeV)** | drained, gated | `qou-7ot6` |
| **Vol(Hopf) = 0** | ✅ **holds** — re-measured here | this note |
| **q-bracket balanced** | ❌ **the ✅ was FALSE** | `qou-qint`, 2026-08-08 |
| **Catalan G** | ✅ holds | `known-constant-literal-audit.py` |

### Rows 1–2 — drained by a wider arc, and the certified value has since gone stale

`qou-7ot6` (closed 2026-08-22) drained stale-CODATA literals corpus-wide, and
`qou-wn1w` wired `computations/codata_corpus_literal_scan.py --strict` into
`scripts/precision-gates.sh` as **blocking** — deliberately widening its
`--changed` predicate to `content/**/*.{lean,ts}`, because 20 of the last 30
executable sites were `.lean`. Re-run on `main` 2026-08-30 with
`PYTHONPATH=computations:computations/substrate:tools/qou-substrate/python:tools/pyhecke/python`:
**CODE 0**, PROSE 422, ADJUDICATED 26, RECORD 1602. Its constant table includes
both `muon-electron mass ratio` and `muon mass energy equivalent in MeV`.

**But the row's *canonical column* is now itself stale.** This audit certifies
`206.7682830` as canonical. That is **CODATA-2018**; PR #4860 / #5149 moved the
registry to CODATA-2022 `206.7682827` on 2026-08-09. The ✅ was right in June and
the defect is drained — yet a reader taking the table's canonical column at face
value today would re-introduce the very literal the later arc removed.

*An audit's "canonical" column ages as fast as the corpus it certifies.* Record
the edition, not just the digits.

### Row 3 — Vol(Hopf) = 0: re-measured against `content/`, and it holds

Surface searched, verbatim: `grep -rn --include=*.lean --include=*.py
--include=*.ts --include=*.md -iE "hopf"` over `content/ computations/ tools/`,
filtered to lines also naming `vol|volume`, then a second pass for any *nonzero*
literal bound to a Hopf-volume name.

Every executable carrier is literally `0`:

    observations/building-block-knots.lean:63          vol_hopf_link : ℝ := 0
    observations/hopf-diquark.lean:78                  hopf_link_volume : ℝ := 0
    knots-particles-confinement/meson-scale-independence.lean:21
                                                       hopfComplementVolume : ℝ := 0

The one `≈ 0` is `knot-volumes-verification-table1-data.md`, a comparison table
carrying its own `10⁻⁶` tolerance. **No nonzero literal anywhere claims to be
Vol(Hopf).** This row's ✅ now rests on a stated, wider surface than it did.

### Row 4 — the q-bracket ✅ was FALSE, and the corpus already knew

This audit certifies *"every `q_int`/`qint` def uses the balanced form — **no**
balanced-vs-unbalanced mixing."*

`qou-qint` censused it on **2026-08-08**: **55 q-integer definitions under ~15
aliases — 43 balanced, 10 geometric, 1 geometric-in-`q²`, 1 ℤ-polynomial**, and
the finding that matters:

> the bare name `qInt` is defined locally in **18 files and means BOTH
> conventions**, so reading a call site tells you nothing.

Two unambiguous single-line witnesses, either of which falsifies the row on its
own:

    lean/QOU/MathlibExt/QIntegerFactorial.lean:37
      def qInt (q : K) (n : ℕ) : K := ∑ i ∈ range n, q ^ i          -- GEOMETRIC
    mass-theory/degree-two-baryon-weight.lean:22
      abbrev qInt (q : ℝ) (n : ℕ) : ℝ := QOU.QInteger.qIntBal q n   -- BALANCED

This is not cosmetic: `qIntBal` is bar-even (`[n]_{q⁻¹} = [n]_q`) and the
geometric form is not — it transforms with weight `−(n−1)`, so a geometric `[n]`
inside a bar-even quantity breaks the parity bookkeeping **silently**. The fix
landed as `lean/QOU/MathlibExt/QIntegerCanonical.lean` ("**Use this module. Do
not define another `qInt`**"), which names both conventions explicitly and
collects the bridge theorems. `qou-qint` remains `todo` at its stated
consolidation ceiling: the residue is guarded / ℤ-indexed / ring-indexed
variants that are *different functions*, not duplicates.

**Why this audit missed it is the same reason it missed the Borromean row**, and
it is not the search surface this time — it is the *predicate*. A grep for
"unbalanced q-bracket" finds nothing, because nothing is spelled that way. The
defect is a **name meaning two functions**, which is only visible if you classify
definitions by *body* and then group by *name*. This is the `markovZ` overload
pattern AGENTS.md documents, one symbol over.

### Row 5 — Catalan G

Re-verified by [`scripts/known-constant-literal-audit.py`](../../scripts/known-constant-literal-audit.py)
(this PR), which **computes** `mp.catalan` and walks the whole tree including
`content/**/*.lean` — the surface this audit did not walk. No wrong-digit carrier
of `G` or `8·G` survives beyond the one corrected above.

### A defect in the measurement itself, recorded rather than quietly fixed

My first classifier read 8 lines past each definition to capture its body. Every
migrated site carries a **bridge lemma** immediately after it (`theorem
qInt_eq_qIntBal …`), so the window swallowed the bridge and inherited *its*
convention. It reported `QCollatz.lean:46` — body `(q^k − 1)/(q − 1)`, and whose
own docstring says *"Bridge to the canonical **GEOMETRIC** bracket"* — as
BALANCED, and reported 22 of 82 unclassifiable. **The tell was that it disagreed
with docstrings written by the people who did the migration.** The two witnesses
quoted above are single-line bodies chosen precisely because no window can
contaminate them.

### What to carry forward

The correction above says *a "clean" verdict is only as wide as the surface the
detector walked*. This pass adds two:

- **A verdict is also only as sharp as the predicate.** Row 4's surface was fine;
  its question ("is any def unbalanced?") could not see "is any *name* both?".
- **State the edition, not only the value.** Row 1's ✅ decayed without anyone
  touching the row, because the canonical moved underneath it.

And the finding about this note itself: **1 of 5 rows was false, and the corpus
had found it three weeks before I flagged the five as unchecked.** Running the
six-path corpus-grep first would have cost minutes and replaced a wrong claim
with a right one — which is the whole argument for the checklist, arrived at the
expensive way.
