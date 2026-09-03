# Covariance-kernel epic (`qou-x631`) — M₁ genus route: source UNBLOCKED (my prior blocker was premature)

**Date:** 2026-08-23 · **Branch:** `claude/m1-genus-source-unblock-2026-08-23` · **Tier:** tooling
correction + clean primary-source extraction (retracts a premature env-blocker; no order/sign claimed)
· **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap
`qou-k5r5`.

## Retraction of my own env-blocker (recorded earlier today)

Earlier today I recorded (bean `qou-k5r5`, and
[`2026-08-23-...-correction-bulk-not-edge.md` §"Honest scope"](2026-08-23-covariance-kernel-M1-correction-bulk-not-edge.md))
that executing the Śniady §4.4/§4.5 genus-1 computation was **blocked in this sandbox** because
"arxiv firewalled, local OCR garbled, PDF tooling broken." **The PDF-tooling half was premature and
is wrong.** `pypdf` and `pdfminer.six` fail on a broken container-wide `cryptography` /
`_cffi_backend`, but **`pymupdf` (`import pymupdf`) does not depend on `cryptography` and works.** It
extracts the *local* `library/arxiv-math-0411647v2/0411647v2.pdf` cleanly — arxiv egress was never
needed; the source is in-repo. Giving up after two extractors hit one shared broken dep, rather than
trying a third with different deps, is exactly the premature-blocker failure mode the disciplines warn
against. The frontier is **executable in this environment**, not blocked.

## The clean genus-1 machinery (now in hand, verbatim from the primary source)

Śniady, *Asymptotics of characters of symmetric groups, genus expansion and free probability*
(`arxiv-math-0411647v2`), §4.5, pp. 40–42:

- **Theorem 4.13** (`R^JM_n` in central characters `Σ`, genus-1):
  `R^JM_n = Σ_{n−1} − (n(n−1)(n−2)/24)·Σ_{2m₂+3m₃+···=n−2} multinom(m₂+m₃+···; m₂,m₃,…)·∏_{s≥2}((s−1)Σ_{1^{m₂}2^{m₃}…}) + (deg ≤ n−4)`.
- **Theorem 4.14** (second-order expansion of characters in free cumulants; conjectured by Biane
  `[Bia03]`): for `n ≥ 2`,
  `Σ_{n−1} = R^JM_n + (n(n−1)(n−2)/24)·Σ_{2m₂+3m₃+···=n−2} multinom(m₂+m₃+···; m₂,m₃,…)·∏_{s≥2}((s−1)R^JM_s)^{m_s} + (deg ≤ n−4)`.

The gradation is `deg R_k = k`; the leading term is genus 0 (`R_n`), the displayed sum is genus 1
(degree `n−2`, i.e. two below leading), and `deg ≤ n−4` is genus ≥ 2. **Verified reproduces the known
Kerov polynomial**: at `n = 4` the genus-1 constraint `2m₂+3m₃+···=2` forces `m₂=1`, coefficient
`4·3·2/24 = 1`, factor `((2−1)R₂)^1 = R₂`, giving `Σ₃ = R₄ + R₂`.

> **🛑 CORRECTION (2026-08-28, exact-verified — the ×3 normalisation).** An earlier draft of this
> section wrote *"`ω₃ = Σ₃ = R₄ + R₂`"* and hence *"`M₁ = Cov(Σh, ω₃) = Cov(Σh, R₄)` exactly."* The
> character `Σ₃` and the content-spread `ω₃ = Σ_□c² − C(n,2)` are **NOT equal — they differ by a factor
> of 3**: `Σ₃ = R₄ + R₂ = 3ω₃`, i.e. **`ω₃ = (R₄ + R₂)/3`**, equivalently `R₄ = 3ω₃ − n`. This is the
> normalisation the Lean file already carried (`r4Value := 3·omega3 − k`); my prose contradicted it.
> Verified exactly on every `λ ⊢ n`, `n ≤ 8`, by building the transition measure and its free cumulants
> over `ℚ` ([`wlambda_covariance_epic_M1_A1_sigmah_in_free_cumulants.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_A1_sigmah_in_free_cumulants.py)):
> `R₂ = n` and `R₄ = 3ω₃ − n` hold identically; `R₄ = ω₃ − n` is false. Consequence: `R₂ = n`
> deterministic still gives
>
> > **`M₁ = Cov_Planch(Σh, ω₃) = (1/3)·Cov_Planch(Σh, R₄)`** — the factor is `1/3`, not `1`. The
> > **sign is unaffected** (positive scalar), so every sign/positivity conclusion in this arc stands;
> > only the constant was wrong.

## The reduction it hands us — and the obstruction it then hits

`ω₃ = (R₄ + R₂)/3` (exact-verified) and `R₂ = |λ| = n` deterministic give
`M₁ = (1/3)·Cov_Planch(Σh, R₄)` (sign unchanged). This isolates the target, **but a second exact check
then obstructs the naive genus route** — see the companion audit
[`2026-08-28-covariance-kernel-M1-sigmah-not-in-free-cumulant-algebra.md`](2026-08-28-covariance-kernel-M1-sigmah-not-in-free-cumulant-algebra.md):
`Σh = ½(p₂+p₂')` is **NOT** a polynomial in the free cumulants (transpose-invariant but with **odd**
leading gradation degree, `E_Planch[Σh] ~ n^{3/2}`; a transpose-invariant `R`-polynomial has only
**even**-degree monomials). Its antisymmetric partner `½(p₂−p₂') = ½R₃` **is** in `A`, but `Σh` is not.
Śniady Thm 4.14 expands `A`-elements (the characters `Σ_k`), so it does **not** directly deliver the
second-order correction to `Cov(Σh, ω₃)`. The claim two paragraphs below — that `Σh ∈ A` — is
**wrong** and is retracted there; the genus route needs a handle on `Σh` that Thm 4.14 does not give
(the shape-linear-statistic second-order theory, or Track D). Original (now-corrected) reasoning kept
below for the record. (see
[the correction-order audit's "Concrete route" section](2026-08-23-covariance-kernel-M1-correction-bulk-not-edge.md)).

## Honest status — executable, NOT executed

What remains is the actual computation, now with clean formulas in hand and no environmental blocker:

1. Express `Σh = ½(p₂+p₂')` in free cumulants `R_k` (a polynomial-function-on-Young-diagrams
   expansion; `p₂` is degree-3-scaling under the `√n` law).
2. Assemble the joint second-order Plancherel structure of the relevant `R_k` (Ivanov–Olshanski Kerov
   CLT gives genus-0 = the derived `κ n^{5/2}`; Śniady Th 4.14 + the Plancherel averaging give the
   genus-1 correction).
3. Read off the **order and sign** of `κ_n − κ` from the genus-1 term.

**No order or sign is claimed here.** This note (a) retracts the false "PDF tooling broken" blocker,
(b) records the clean primary-source formulas, and (c) fixes the target as `Cov(Σh, R₄)`. Executing
steps 1–3 is the next honest step and is now unobstructed. Gap `qou-k5r5` stays **OPEN**.

## Method note (for the next agent)

Extract the primary source with **`pymupdf`**, not `pypdf`/`pdfminer` (both are dead on this
container's broken `cryptography`). `pip install --quiet pymupdf`, then
`pymupdf.open('library/arxiv-math-0411647v2/0411647v2.pdf')[i].get_text()`. §4.5 is pp. 40–42.

## Cross-references

- Correction-order audit (genus-applicability + the eliminated dim-tilt distinction):
  [`2026-08-23-covariance-kernel-M1-correction-bulk-not-edge.md`](2026-08-23-covariance-kernel-M1-correction-bulk-not-edge.md)
- Genus route eliminated for the *dim-tilt* kernel (why it does not apply to `M₁`):
  [`2026-07-25-covariance-kernel-A5-genus-eliminated-A4-lean.md`](2026-07-25-covariance-kernel-A5-genus-eliminated-A4-lean.md)
- κ derivation: [`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)
- Gap bean `qou-k5r5`.
