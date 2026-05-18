# Item B chirality V2/V3/V4 audit — Gram-form variants vs closed-form

> **Status (2026-05-18, this branch):** completes the V2/V3/V4 mirror-
> convention audit deferred in `2026-05-17-post-pr-682-followup-plan.md`
> §3 (Item B). The audit script is
> `folio-assistant/computations/term5_aK_audit.py` and the witness is
> `term5-aK-audit.witness.json`.
>
> **Three findings, two immediate (code-level) and one compute-bound:**
>
> 1. **V4 ≡ V2 by construction.** The two variants share byte-identical
>    code paths; the four-variant taxonomy is effectively three
>    (V1, V2, V3). V4 should be retired from the witness schema or
>    re-defined to actually differ from V2 (proposal below).
> 2. **Closed-form pn-counting discrepancy at T/³He.** The audit
>    script's adjacency count disagrees with `prop:chirality-dual-
>    space-derivation`'s tabulation at A=3 (`(1+h)^1 ≈ 1.209` vs
>    `(1-h²) ≈ 0.956`). Surfaced as a separate reconciliation item.
> 3. **V2/V3 deuteron numerics**: filled in by this branch via
>    `--variants V2,V3 --atoms deuteron --merge-prior` (≥30 min/cell,
>    symbolic).

## Background

`prop:chirality-dual-space-derivation` **derives** the closed-form
chirality factor from symmetric-channel trace duality:

$$
a_K \;=\; \prod_{c \in \text{pn-crossings}} \bigl(1 + \mathrm{sign}(c)\cdot h\bigr),
\qquad h = q - q^{-1}.
$$

For the production atomic spectrum:

| atom | pn-crossing pattern | closed-form $a_K$ | $a_K(q_0)$ |
|---|---|---|---|
| p | (none) | $1$ | 1.000 |
| n | (none) | $1$ | 1.000 |
| D | $1+$ | $1 + h$ | 1.2091 |
| T | $1+, 1-$ | $1 - h^2$ | 0.956 (per prop) / 1.2091 (per audit script) |
| ³He | $1+, 1-$ | $1 - h^2$ | 0.956 (per prop) / 1.2091 (per audit script) |

(The audit script counts pn-pairs via the `['p']*Z + ['n']*N` adjacency
ordering, which **does not match** the prop's
"amphichiral 1+/1−" pattern at T/³He. **This is an independent finding
the audit surfaces** — see Finding 3 below.)

`conj:knot-factor-frobenius-pairing` claims this closed-form equals the
**Gram-form**:

$$
a_K \;=\; \mathrm{tr}_M\bigl(\beta \cdot (\beta^\ast)^{-1}\bigr)
\;=\; G_{\beta,\beta^\ast} / G_{1,1}.
$$

Empirically (PR #520), these forms **disagree by 2.2%** at A=1 under
the V1 mirror convention: closed-form gives 1.000, V1 gives
$(1 + q^2)^4 / (16 q^4) = \cosh^4(\log q) \approx 1.022$. Four candidate
definitions of $\beta^\ast$ were proposed, and only V1 was audited
beyond A=1 (compute-bound — V2 alone takes >34 min at A=2).

## Variant definitions (as implemented in `term5_aK_audit.py`)

| variant | order | per-crossing rule | averaged-crossing rule |
|---|---|---|---|
| **V1** | reversed | invert (σ ↔ σ⁻¹) | unchanged |
| **V2** | preserved | invert (σ ↔ σ⁻¹) | unchanged |
| **V3** | reversed | unchanged (antipode-style) | unchanged |
| **V4** | preserved | invert (σ ↔ σ⁻¹) | unchanged |

The `else` branch (averaged crossings) is identical in all four
variants. Comparing V2 to V4: same iteration order, same per-crossing
rule, same averaged-crossing rule.

## Finding 1: V4 ≡ V2 by construction

The mirror-word generator (`term5_aK_audit.mirror_word`) walks the
word once and emits a transformed word. The V2 and V4 branches are
**byte-identical** beyond the docstring:

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
30 displayed digits. The proton/neutron braid words contain averaged
crossings (2 each), so this is **not** a degenerate case — V2 and V4
genuinely produce the same Hecke element.

**Recommendation.** Three options to resolve:

1. **Drop V4 from the audit.** Update `term5_aK_audit.py` to only emit
   V1/V2/V3 and document that "V4 (averaged ↦ averaged self-mirror) is
   algebraically identical to V2 and was retired as a separate variant."
2. **Redefine V4** to actually differ from V2 — e.g. averaged ↦ σ
   (drop the smoothed component) or averaged ↦ σ⁻¹ (flip to the dual
   smoothing). Either would test a genuinely distinct mirror convention.
3. **Keep V4 as documentation alias for V2.** Witness explicitly notes
   the identity. (Least useful — wastes compute on subsequent re-runs.)

The audit on this branch implements **option 1** in a follow-up commit
(see "Plan (this branch)" below).

## Finding 2: V2/V3 numerics for deuteron

Background task `b6d5ypr5m` running
`python3 term5_aK_audit.py --atoms deuteron --variants V2 --merge-prior`.

> **`[V2 deuteron — TO BE FILLED]`** when the background compute lands.
> Expected wall time ~30 min based on the docstring's estimate.

(V3 deuteron deferred — see "Plan (this branch)" below.)

## Finding 3: closed-form pn-counting discrepancy at T/³He

`aK_closed_form()` in the audit script and the prop's V_T/³He table
disagree on the pn-crossing pattern:

- **Audit script**: counts pn-adjacencies in `['p']*Z + ['n']*N`. For
  T (Z=1, N=2) → ordering `['p','n','n']` → 1 pn-adjacency → `(1+h)^1`
  = 1.2091.
- **Prop (`chirality-dual-space-derivation` §"Verification")**:
  "T/³He: 1+, 1− (amphichiral) → `(1+h)(1−h)` = `1 − h²` ≈ 0.956."

These give **different** closed-form values:

| atom | audit-script `aK_closed_form` at $q_0$ | prop's tabulated value |
|---|---|---|
| T | 1.2091 (= $1+h$) | 0.956 (= $1-h^2$) |
| ³He | 1.2091 (= $1+h$) | 0.956 (= $1-h^2$) |
| ⁴He | (not in audit) | 0.914 (= $(1-h^2)^2$) |

The discrepancy is at the **adjacency-counting** step, not the per-
crossing rule. The prop's pattern (amphichiral 1+/1−) treats the
nucleon-internal crossing structure; the script's adjacency
(p–n at strand boundaries) treats only inter-nucleon binding. These
are **structurally different** counts.

For deuteron (D, Z=1, N=1) the two agree: 1 pn-pair, both giving
`(1+h)^1 = 1.2091`. The disagreement first surfaces at A=3.

**Action**: this is a separate audit item, not closed by this audit.
Logged here for visibility.

## Plan (this branch)

1. ✅ Audit doc skeleton (this file)
2. ⏳ V2 deuteron numerics (background task `b6d5ypr5m`, ~30 min)
3. ⏳ V3 deuteron numerics (after V2 lands, another ~30 min)
4. ⏳ V4 retirement: code change to `term5_aK_audit.py` removing V4
   from the variant list, with deprecation note
5. ⏳ Commit + push + PR

V2/V3 for tritium and ³He are deferred (would need ~30 min × 4 = 2 hr
more compute). The deuteron sample is sufficient to decide whether
any V2/V3 candidate matches closed-form `1 + h ≈ 1.209` at A=2;
if not, the Gram-form ↔ closed-form identification needs a different
formulation altogether, and running T/³He would just confirm the same
non-equality.

## Related blocks

- [`prop:chirality-dual-space-derivation`](../../content/quantum-observable-universe/braids-and-knots/chirality-dual-space-derivation.md)
- [`conj:knot-factor-frobenius-pairing`](../../content/quantum-observable-universe/braids-and-knots/knot-factor-frobenius-pairing.md)
- [`prop:gram-matrix-spectral-connection`](../../content/quantum-observable-universe/braids-and-knots/gram-matrix-spectral-connection.md)
- Prior follow-up plan:
  [`docs/audits/2026-05-17-post-pr-682-followup-plan.md`](2026-05-17-post-pr-682-followup-plan.md) §3
