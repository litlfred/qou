# Q_β KLR tranche 2 — Composite-4 (Wenzl × q-Pochhammer) parity preflight scope

**Status:** focused sub-scope of the cont. 9 KLR/crystal infra roadmap
([`2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md §Composite 4`](2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md#composite-4-wenzl-projector-tower-with-q-pochhammer-modulation),
"5-6 session" Option B). **This doc adds a one-session formalize-first
preflight gate** that the cont. 9 scope did not specify, using the three
structural constraints established **after** that scope was written
(#1900 / #1907 / #1911, all merged 2026-06-05/06). Scope only — no compute.

**Owner direction (2026-06-06):** "pick up KLR", then (after merging tranche 1)
proceed to the KLR program's next sub-goal. Sibling to merged PR #1911
(KLR tranche 1).

**Disciplines:** *formalize-first* (AGENTS.md §formalize-first: narrow the
hypothesis class with a structural argument before any expensive search),
*corpus-grep* (the cont. 9 scope is the upstream source of truth for
infra cost / composite menu — do not duplicate), *Δ_λ gate* (no fits),
*fibre-vs-observable* (bar lives at the fibre level).

---

## 1. The cont. 9 scope's frame

[`2026-06-03-...klr-crystal-infra-scope.md`](2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md)
records four composite candidates after the 28-candidate single-formula
bracket SATURATED + the 1281-candidate 2-factor sweep SATURATED. **Composite 4
is the cheapest** (5-6 sessions of infra) and combines Family α (Wenzl JW
projector Markov trace, NEGATIVE alone, cont. 5) with Family β (Kashaev
q-Pochhammer, NEGATIVE alone, cont. 5):

```
F(u) = Π_{k≥2} (1 + tr_M(p_k^JW) · (q;q)_k · u^k)
```

The cont. 9 scope **did not** specify a structural gate; it would have authorised
infra build immediately on Option B selection. Three structural results landed
after that scope was written.

## 2. The three new structural constraints any composite must satisfy

| constraint | source | parity / locus |
|---|---|---|
| `a_1 = −c_3 = √2·Φ₂` **bar-odd** | merged PR #1900 (c_k-recursion kernel) | bar-ODD |
| on-main `α_eff = (z−1)·h/2`, `h = q−q⁻¹` **bar-odd** | merged PR #1907 (Hoefsmit) | bar-ODD |
| residue numerator `N = h·(1−h²α)` **bar-odd** with **ζ₄ pole** (`F = N/[2]_q`) | merged PR #1911 (Habiro dual of α_EM) | bar-ODD, ζ₄ pole |
| cross-anchor Φ₂ targets | cont. 14 ledger | proton `1.46324616887618`, muon `1.42849728553818`; swing `0.0347` |

Three independent routes pin **bar-odd**; #1911 adds the ζ₄ pole.

## 3. The preflight gate (one focused session)

Composite 4 is worth 5-6 sessions of infra *only if* its predicted c_3 / Φ₂
**can satisfy all three** constraints. The preflight asks this analytically,
**without** building the Wenzl-projector Lean infra or the `pyhecke` linear
`tr_M` extension. Three sub-checks:

### 3a. Bar parity of `(q;q)_k` under `q ↦ q⁻¹`

The finite q-Pochhammer satisfies the identity (corpus check at
[`tools/pyhecke/...`](../../tools/pyhecke/) — verify in preflight):

```
(q⁻¹; q⁻¹)_k = Π_{i=1}^k (1 − q⁻ⁱ) = (−1)^k · q^{−k(k+1)/2} · (q;q)_k
```

So `(q;q)_k` is **not** a bar eigenvector — it carries a `(−1)^k · q^{−k(k+1)/2}`
prefactor under bar. **Implication**: in the Composite 4 product, the bar
behaviour of the `k`-factor is `tr_M(p_k^JW)`-parity ⊗ `(−1)^k·q^{−k(k+1)/2}`,
not pure bar-symmetric.

### 3b. Bar parity of `tr_M(p_k^JW)`

The Jones–Wenzl projector has known Markov trace (Kauffman bracket /
Kazhdan-Lusztig sources): `tr_M(p_k^JW) = (−1)^k / [k+1]_q` (in one common
normalisation; verify in preflight). Since `[k+1]_q = (q^{k+1} − q^{−(k+1)})/(q − q⁻¹)`
is **bar-even** for the symmetric `q − q⁻¹` definition, `tr_M(p_k^JW)` itself is
**bar-even**.

### 3c. Combined parity at the `c_3 / Φ₂` rung (k=3)

For Composite 4 to source a **bar-odd** `c_3 / Φ₂` (constraint from §2), the
`u^3` coefficient of `F(u)` itself must be bar-odd. **Crucially: since the
product starts at `k ≥ 2`, the `u^3` coefficient of `F` is exactly `A_3 =
tr_M(p_3^JW)·(q;q)_3`** — the first mixing term is `A_2 A_3 u^5` (degree 5);
there is no k=2,3 mixing at u^3. So the preflight verdict at the c_3 rung
reduces to the parity of `A_3` alone — there is no product-expansion rescue.

**Naive form** (using bare `(q;q)_3`): from §3a–b, `A_3` is `(bar-even
tr_M(p_3^JW)) · (q-prefactored bare (q;q)_3)`, which under bar carries the
`(−1)^3·q^{−6} = −q^{−6}` rescaling — **not** a clean bar-flip. So with the
bare q-Pochhammer, **Composite 4 fails the bar-odd gate at u^3**.

**Renormalisation rescue (CONDITIONAL pass).** Setting
`Y_k := q^{−k(k+1)/4} · (q;q)_k`,

```
bar(Y_k) = q^{+k(k+1)/4} · (−1)^k · q^{−k(k+1)/2} · (q;q)_k
         = (−1)^k · q^{−k(k+1)/4} · (q;q)_k = (−1)^k · Y_k
```

so `Y_k` IS a bar-eigenvector with eigenvalue `(−1)^k`: **bar-even for even k,
bar-ODD for odd k**. At k=3: `Y_3` is bar-odd. Combined with the bar-even
`tr_M(p_3^JW) = (−1)^3/[4]_q = −1/[4]_q`, the renormalised
`A_3^{ren} := tr_M(p_3^JW)·Y_3` is **(bar-even) × (bar-odd) = bar-ODD**,
satisfying §2's constraint at the c_3 rung.

So Composite 4 (with `(q;q)_k` replaced by the bar-eigenvector renormalisation
`Y_k`) **PASSES bar-odd at u^3** — but only conditionally on a categorical
justification for the `q^{−k(k+1)/4}` rescaling. The renormalisation choice
becomes the decisive scope item for cont. 9 Option B build.

**Preflight verdict at the c_3 rung (this scope's bottom line)**: §3c above
already does the analytical work. Composite 4 with **bare `(q;q)_k`** is
**REFUTED at parity** at u^3; with the **bar-eigenvector renormalisation**
`Y_k = q^{−k(k+1)/4} · (q;q)_k` it **PASSES** at u^3 (bar-odd via `Y_3`
bar-odd × `tr_M(p_3^JW)` bar-even). So the verdict is **CONDITIONAL** — and
the live preflight question is now reduced to:

> **Is `Y_k = q^{−k(k+1)/4} · (q;q)_k` the categorically natural object** in
> the Wenzl/JW × q-Pochhammer composite (e.g. via the Hoefsmit / Markov
> normalisation, or the KL canonical-basis grading)?

If yes: proceed to cont. 9 Option B (5-6 sessions). If no: the bare form is
refuted and Composite 4 is dropped (redirect to Composite 1 or 2). The
preflight RUN (next focused session) settles that yes/no by reading the
known Hoefsmit / Markov-trace normalisations in `pyhecke` and
`MarkovTraceOnHecke.lean`.

| verdict | action |
|---|---|
| **PASS** — `Y_k` is the categorically natural object | proceed to cont. 9 Option B (5-6 session infra build) |
| **REFUTED** — bare `(q;q)_k` is the only natural form; no renormalisation justified | drop Composite 4; redirect to Composite 1 (Demazure × q-Poch) or 2 (KLR canonical basis) |
| **CONDITIONAL-pending-norm-source** — neither outcome above is decisive after one session | flag the renormalisation as a separate scope item before infra build |

## 4. Cost & ROI

**Preflight cost**: one focused session of symbolic analysis (Python sympy +
the established bar identities). No Wenzl-projector infra, no `pyhecke`
extensions, no Lean modules.

**ROI**: refutes or constrains 5-6 sessions of infra build cost — strict
formalize-first dominance over the cont. 9 scope's "build first, test later"
implicit ordering.

## 5. Out of scope (this doc)

- The preflight itself (one session of work; **this is the scope, not the run**).
- Composite 1 / 2 / 3 preflights — same template would apply, but each merits
  its own focused preflight scope using the §2 constraints.
- Any production wiring of `c_3` (Δ_λ gate held; cont. 9 acceptance permanent
  until a *derivation* lands).
- Substrate-derivation of `q_0` (owner declined 2026-05-08; permanently out of
  the KLR program's scope).

## 6. Cross-refs

- Master KLR-infra scope (cont. 9): [`2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md).
- KLR program master scope (kickoff): [`2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`](2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md).
- KLR tranche 1 (merged): [`2026-06-06-qbeta-residue-habiro-dual-tau-eval.md`](2026-06-06-qbeta-residue-habiro-dual-tau-eval.md), PR #1911 `fbbba406165dc9cf3f7b8df71d295b737ef1aa0b`.
- Φ₂ targets (cont. 14): [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md), `qbeta-cosh-phase-series-reframe-probe.witness.json`.
- Wenzl chain α NEGATIVE (cont. 5): [`qbeta-wenzl-habiro-chain-alpha.witness.json`](../../computations/qbeta-wenzl-habiro-chain-alpha.witness.json), [`qbeta_wenzl_habiro_chain_alpha.py`](../../computations/qbeta/qbeta_wenzl_habiro_chain_alpha.py).
- 4-search acceptance: [`2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md`](../audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md).
