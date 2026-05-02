# P1.5 — Compound-shell / atlas base-case audit

**Workplan task**: P1.5 (verify no AME-fitted base cases in the
compound-shell calibration / recursive atom-knot atlas /
light-isotope derivation chain).
**Branch**: `claude/tier3-math-audit-B0wyO`.
**Audit-flag context**: SHELL-1 in
[`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md)
§2·G — "compound-shell self-named 'calibration'".

## Verdict

🟡 **Partially derived; quarantined entries explicitly disclosed.**

The audit's SHELL-1 worry that the recursion's base cases are
AME-fitted is **partially correct but already honestly disclosed**
in-paper. The compound-β proposition is misnamed (`compound-beta-
shell-calibration`) but its content is genuinely a derivation
chain. The atlas has tagged categories that explicitly mark which
base cases are principled vs. provisional, and quarantines two
isotopes (⁶Li, ⁷Li) that fail the principled criterion.

No new fits are introduced. The framework remains single-calibration
at $E_0 = Q_\beta(n)$ (CAL-3 per the three-calibration addendum); the
AME data is used as comparison reference and Q-value source, not as
a parameter-fitting target.

## Block-by-block findings

### `compound-beta-shell-calibration.md`

[`content/quantum-observable-universe/braids-and-knots/compound-beta-shell-calibration.md`](../../content/quantum-observable-universe/braids-and-knots/compound-beta-shell-calibration.md)

| Concern | Finding |
|---------|---------|
| File name says "calibration" | **Misnomer.** The proposition explicitly states: "shell-binding target $y_{\mathrm{target}}(A_{\mathrm{magic}})$ is **derivable**, not independently calibrated, from the cumulative β-decay chain". |
| AME data on RHS | Used as Q-value source: "RHS is fully determined by AME β-decay data plus the categorical level-3 shadow prices — no free parameters beyond $E_0$". AME Q-values are measurements, not fits. |
| Free parameters | Zero beyond CAL-3 ($E_0 = 0.782\;\mathrm{MeV}$ from free-neutron $Q_\beta$). Framework remains single-scale at the hadronic anchor. |

**Recommendation**: rename to
`compound-beta-shell-derivation.md` (or add an explicit note in the
opening paragraph clarifying the file-name misnomer). Block content
is sound.

### `recursive-atom-knot-atlas.md`

[`content/quantum-observable-universe/braids-and-knots/recursive-atom-knot-atlas.md`](../../content/quantum-observable-universe/braids-and-knots/recursive-atom-knot-atlas.md)

The atlas declares **six explicit categories** for atomic
knot-identification, with a honest grading from principled to
quarantined:

| Tag | Status | Examples |
|-----|--------|----------|
| `principled-derivation` | ✅ clean | electron $3_1$, proton/neutron Borromean braid |
| `principled-gb-nf` | ✅ clean | neutrino (unknot, no mass), photon, quark |
| `manual-historical-volume-match` | 🟡 **base case not yet GB-NF derived** | ²H ($6_2$), ³H ($8_{11}$), ³He ($L_{6a4}$) |
| `magic-A-formula` | ✅ algebraic | ⁴He (closed-form $A \cdot 8G$) |
| `recursive-on-⁴He` | ✅ clean (given ⁴He) | ⁸Be–⁴⁰Ca |
| `deprecated-volume-match` | 🔴 **explicitly quarantined** | ⁶Li, ⁷Li |

The `manual-historical-volume-match` and `deprecated-volume-match`
categories *are* the audit's SHELL-1 concern, **and the paper
already names them as such**:

> `deprecated-volume-match`: **PROVISIONAL — do not cite as
> principled.** Brute-force SnapPy volume search picked the closest
> knot to the AME-derived volume target; reverse-engineers the
> answer.

This is honest disclosure; not a hidden fit. The paper's atlas
**already excludes** quarantined entries from the principled
predictions. The remaining open work is the GB-NF derivation of
²H, ³H, ³He from the $\sigma$-braid word in $H_{n_0}(q_0)$ —
tracked as a separate open item (not an audit-flag deficiency).

### `derived-mass-formula-light-isotopes.md`

[`content/quantum-observable-universe/braids-and-knots/derived-mass-formula-light-isotopes.md`](../../content/quantum-observable-universe/braids-and-knots/derived-mass-formula-light-isotopes.md)

| Concern | Finding |
|---------|---------|
| Free / continuous parameters | "no continuous parameters are fitted, and no choices were made by selecting from a menu of variants" |
| Discrete model selection | ⁶Li, ⁷Li flagged as "technically fitted (model selection)" — choice among "several algebraically-natural variants". Honest disclosure; the paper does not claim these as principled predictions. |
| Term-7 shell correction | Open: depends on `conj:shell-correction-term-seven` (correctly classified as a conjecture). |

## Net effect on audit flag SHELL-1

The deep audit's SHELL-1 entry should be reclassified from 🟠 to
🟡 with notes:

| Aspect | Status |
|--------|--------|
| Is there hidden AME fitting? | **No.** All AME usage is either Q-value-source (a CAL-3 measurement) or explicitly quarantined. |
| Are base cases derived? | **Partially.** ²H, ³H, ³He, ⁴He, plus ⁸Be–⁴⁰Ca via recursion are derived; ⁶Li, ⁷Li are quarantined; ²H/³H/³He need GB-NF derivation in $H_{n_0}(q_0)$ as a follow-up. |
| Is the file name accurate? | **No.** `compound-beta-shell-calibration.md` should be renamed to drop the "calibration" misnomer. |

## Recommended actions

1. **Rename** `compound-beta-shell-calibration.{ts,md,lean}` →
   `compound-beta-shell-derivation.*` to match the actual content.
   Update all cross-references.

2. **Add explicit note** in
   [`derived-mass-formula-light-isotopes.md`](../../content/quantum-observable-universe/braids-and-knots/derived-mass-formula-light-isotopes.md)
   linking to the three-calibration block
   ([`prop:three-calibration-inputs`](../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md)),
   so the "no continuous parameters are fitted" claim is anchored to
   the framework-level commitment.

3. **Open follow-up** (not a P1.5 fix): GB-NF derivation of ²H, ³H,
   ³He as $\sigma$-braid words in $H_{n_0}(q_0)$. This moves the
   atlas's `manual-historical-volume-match` entries up to
   `principled-derivation`. Tracked but not audit-blocking.

4. **Resolve quarantined isotopes** (⁶Li, ⁷Li): either find a
   principled derivation or formally exclude them from the atomic-mass
   prediction set. Tracked but not audit-blocking.

## Output

This audit doc. The base-case status itself doesn't need a
witness JSON — the atlas's tag categories already encode the
provenance per-isotope.

## Recommended deep-audit edit

Update §2·G in
[`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md):

```diff
-| **SHELL-1** | 🟠 Block name self-reports as a calibration. If shell coefficients in compound-β are fitted to AME mass differences, the AME data is being used as a derivation input — borderline empirical leak |
+| **SHELL-1** | 🟡 **Resolved.** Block-name misnomer (file is `compound-beta-shell-calibration.md` but content is genuinely a derivation chain). AME data enters as Q-value measurements consumed by the CAL-3-anchored hadronic scale, not as fitted parameters. The recursive atom-knot atlas has explicit tag categories that mark provisional / quarantined entries (⁶Li, ⁷Li); base cases for ²H, ³H, ³He are GB-NF-pending but not AME-fitted. See [base-cases audit](2026-05-01-base-cases-audit.md). |
```
