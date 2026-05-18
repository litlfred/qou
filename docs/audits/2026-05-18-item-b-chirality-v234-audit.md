# Item B chirality V2/V3/V4 audit — closed by upstream restatement of `conj:knot-factor-frobenius-pairing`

> **Status (2026-05-18):** the central question of this audit was
> **closed on main** by [PR #683](https://github.com/litlfred/qou/pull/683)
> commit `46a893f7` (B.1a-rev.3) and the deeper audit
> [`2026-05-18-m-p-item-b-t5-categorical-attribution.md §7c`](2026-05-18-m-p-item-b-t5-categorical-attribution.md).
> Specifically: the conjectural identification
> $a_K = |\mathrm{tr}_M(W_\text{atom})|/|\mathrm{tr}_M(W_\text{free})|$ (Ratio form)
> was empirically refuted at 50 dps across 4 atoms (off by 2–18×) and
> reidentified as the **mass-defect envelope** $\mathcal{B}_\text{bulk}$,
> **not** the chirality factor. The canonical $a_K$ is the
> **closed-form Skein-product** $\prod_c(1 + \mathrm{sign}(c)\cdot h)$,
> now Step 4 of [`conj:knot-factor-frobenius-pairing`](../../content/quantum-observable-universe/braids-and-knots/knot-factor-frobenius-pairing.md).
>
> What survives from this branch's audit:
>
> 1. **V4 retirement** in `term5_aK_audit.py` (V4 was byte-identical
>    to V2 — a code-level finding independent of the framing) —
>    landed in commit [`71234ce1`](https://github.com/litlfred/qou/commit/71234ce1).
> 2. **pn-counting discrepancy at T/³He** between
>    `term5_aK_audit.aK_closed_form` (adjacency count → 1.209) and
>    `prop:chirality-dual-space-derivation`'s tabulation (amphichiral
>    1+/1− → 0.956). Still actionable; logged for a separate audit.
>
> What was **dropped** from this branch's plan:
>
> - V2/V3 deuteron / tritium / ³He Gram-form numerics. The
>   underlying question (which mirror β* makes Gram = closed-form?)
>   is now moot — they're different categorical quantities by
>   construction on main. The background V2-deuteron task was
>   killed at ~1% complete.

## Why this audit closed without filling in V2/V3 numerics

The original premise was: PR #520 surfaced a 2.2% gap at A=1 between
the closed-form $a_K = \prod_c(1+\mathrm{sign}\cdot h) = 1$ and the
Gram-form $\tau(\beta \cdot \beta^{-1}) = \cosh^4(\log q) \approx 1.022$
(V1). Four candidate β* definitions (V1/V2/V3/V4) were proposed in
`term5_aK_audit.py` to test whether a different mirror convention
would close the gap.

While this branch was running V2 deuteron, **upstream
[PR #683](https://github.com/litlfred/qou/pull/683)** ran a
parallel investigation in `aK_via_lp_dual.py`:

| atom | A | $a_K^R$ (Ratio/Gram) | $a_K^C$ (Closed/Skein) | R − C residual |
|------|---|------------------|------------------|----------------|
| proton   | 1 | 1.000 | 1.000 | 0 (trivial) |
| neutron  | 1 | 1.000 | 1.000 | 0 (trivial) |
| deuteron | 2 | **0.395** | 1.209 | −67% |
| tritium  | 3 | 0.115 | 0.956 | −88% |
| ³He      | 3 | 0.197 | 0.956 | −79% |
| ⁴He      | 4 | 0.055 | 0.914 | −94% |

(Source: `a-K-via-lp-dual.witness.json`, `2026-05-18-m-p-item-b-t5-categorical-attribution.md §7c`.)

The gap is **not** 2.2%; it's 67–94% at A ≥ 2. No mirror β* convention
can close that gap by re-permuting σ ↔ σ⁻¹ in the mirror word — the
two forms are different categorical objects. Step 4 of
`conj:knot-factor-frobenius-pairing` on main now states this
explicitly:

> *Historical note (2026-05-18):* an earlier formulation of this
> step proposed
> $a(N) = |\mathrm{tr}_M(W_\text{atom})|/|\mathrm{tr}_M(W_\text{free})|$
> as the ratio form. Empirical verification at 50dps … finds this
> ratio is 6–17× off the Skein values above for A=2,3,4. The ratio
> form measures the **mass-defect envelope** $\mathcal{B}_\text{bulk}$,
> not the chirality factor $a_K$; the closed-form Skein-product
> **is** the canonical $a_K$ …

Running V2 / V3 deuteron + tritium would have produced *more* Gram-form
data — interesting as Gram-matrix structure but **not** chirality data
under the corrected framing. With the central question resolved, the
~30 min × 6 cells (= ~3 hours) of symbolic compute is no longer the
best use of CI time. The task was killed; the witness is left at its
pre-branch state (V1 across the spectrum, V2/V3/V4 for {p, n} only).

## Finding 1: V4 ≡ V2 (retained — code-level cleanup)

The V4 retirement landed in commit
[`71234ce1`](https://github.com/litlfred/qou/commit/71234ce1) and is
independent of the framing change above. The two variants shared
**byte-identical** `mirror_word` branches:

```python
elif variant == "V2":
    # Invert each, keep order (mirror knot K*).
    if kind == "sigma":      out.append((c, -h_num, gen))
    elif kind == "sigma_inv": out.append((c, 0.0, gen))
    else:                     out.append((c, d, gen))   # averaged → unchanged
elif variant == "V4":
    # V2 but explicitly noting averaged is self-mirror.
    if kind == "sigma":      out.append((c, -h_num, gen))
    elif kind == "sigma_inv": out.append((c, 0.0, gen))
    else:                     out.append((c, d, gen))   # averaged → unchanged
```

The existing witness confirms this: V2 = V4 = 1.1471203358935889 at
the proton, and V2 = V4 = 1.2267591396724156 at the neutron — to all
30 displayed digits. Proton/neutron braid words contain averaged
crossings (2 each), so this is not a degeneracy in the input — V2
and V4 produce the same Hecke element on every braid word.

The cleanup:
- `mirror_word()` raises `ValueError` on `V4` with an explanatory
  message pointing at this audit doc.
- `--variants` default reduced to `V1,V2,V3` (was `V1,V2,V3,V4`).
- Passing `--variants V4` exits non-zero with the same explanation.
- V4 entries in the existing witness JSON are preserved for
  provenance; the script just doesn't accept V4 as input any more.

This finding stands on its own — it's a code-cleanup independent of
whether the Gram/closed-form question is resolved.

## Finding 2: pn-counting discrepancy at T/³He (retained — still actionable)

`aK_closed_form()` in the audit script and the verification table in
`prop:chirality-dual-space-derivation` disagree on the pn-crossing
pattern at A=3:

- **Audit script**: counts pn-adjacencies in `['p']*Z + ['n']*N`.
  For T (Z=1, N=2) → ordering `['p','n','n']` → 1 pn-adjacency →
  `(1+h)^1 = 1.2091`.
- **Prop's verification table** ([§"Verification"](../../content/quantum-observable-universe/braids-and-knots/chirality-dual-space-derivation.md)):
  "T/³He: 1+, 1− (amphichiral) → `(1+h)(1-h)` = `1 - h^2` ≈ 0.956".

Numerically:

| atom | audit-script `aK_closed_form` at $q_0$ | prop's tabulated value |
|---|---|---|
| T | 1.2091 (= $1+h$) | 0.956 (= $1-h^2$) |
| ³He | 1.2091 (= $1+h$) | 0.956 (= $1-h^2$) |
| ⁴He | (not in audit) | 0.914 (= $(1-h^2)^2$) |

The discrepancy is at the **adjacency-counting** step, not the per-
crossing rule. For deuteron (A=2) the two agree (1 pn-pair, both
giving $(1+h)^1 = 1.2091$); the disagreement first surfaces at A=3.

This is a real downstream-affecting bug surface: `aK_closed_form` is
used as a reference value in the audit witness, and the wider
`paper_six_term_isotope_sweep.term5_chirality` uses an explicit
`chirality_signs` list whose origin should be checked against
both the audit script and the prop. Resolving requires:

1. Inspect `paper_six_term_isotope_sweep.term5_chirality` and trace
   where `chirality_signs` comes from (literal list vs. derived).
2. Determine the canonical convention for "what counts as a pn
   crossing" — paper text vs. canonical braid topology.
3. Align `term5_aK_audit.aK_closed_form` to whichever is canonical.
4. Re-run T/³He audit cells to confirm the corrected closed-form.

Deferred to a separate audit; this branch only flags it for
visibility.

## What this branch ships

- Audit doc (this file): closes the V2/V3/V4 thread by deferring to
  upstream PR #683's resolution.
- Code change (`term5_aK_audit.py`): V4 retirement
  ([`71234ce1`](https://github.com/litlfred/qou/commit/71234ce1)).
- Witness: unchanged from main (the pre-existing
  `term5-aK-audit.witness.json` covers V1 for the spectrum + V2/V3/V4
  for {p, n}).

## Related blocks / audits

- `conj:knot-factor-frobenius-pairing`
  ([`.md`](../../content/quantum-observable-universe/braids-and-knots/knot-factor-frobenius-pairing.md))
  — Step 4 restated on main by commit `46a893f7`
- `prop:chirality-dual-space-derivation`
  ([`.md`](../../content/quantum-observable-universe/braids-and-knots/chirality-dual-space-derivation.md))
  — the derivation of the closed form, unchanged
- Upstream T5 attribution audit:
  [`2026-05-18-m-p-item-b-t5-categorical-attribution.md`](2026-05-18-m-p-item-b-t5-categorical-attribution.md)
  §7c gives the empirical R-vs-C table that closed the question
- Witness: `a-K-via-lp-dual.witness.json` (added by PR #683)
- Prior follow-up plan:
  [`2026-05-17-post-pr-682-followup-plan.md`](2026-05-17-post-pr-682-followup-plan.md) §3
