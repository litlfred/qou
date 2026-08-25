# Two defects in the c₃ registry: a glyph collision, and an anchor-selective scale claim

**Date:** 2026-08-14 · **Beans:** `qou-kp9f`, `qou-uoo0`, `qou-u5l3` (under `qou-0wj8`);
closes out `qou-qb8f` item **(c)** · **PR:** #5022
· **Tier:** scope-(a) — measurement of what the committed numbers say
· **Discipline:** no producer re-run, no witness written, no `c_k` wired, no fit,
no Lean edited. Read-only against committed artifacts.
· **Check:** [`computations/qbeta/kc21_kc22_glyph_and_anchor_robustness_check.py`](../../computations/qbeta/kc21_kc22_glyph_and_anchor_robustness_check.py)
(exit 0, all assertions pass).

---

## 0. Why this exists

Bean [`qou-qb8f`](../../.beans/qou-qb8f--is-c3-even-derived-to-be-vol41-two-inequivalent-splits.md)
asked three questions about **(H1)** `c₃^even = −Vol(4₁)`. It answered (a) and
(b) across three rounds — twice reversing itself — and explicitly left **(c)**
*("should the registry's c₃ row carry a pointer either way?")* to the registry
maintainers. This is that pointer, plus a second defect found while placing it.

Both findings are about the **registry's summaries**, not about the underlying
compute. The producing witnesses are honest; the summaries generalise them.

---

## 1. Defect 1 — `q*`, `h*`, `ũ(q*)` name two different points (`qou-kp9f`)

Rows **KC21** and **KC22** of
[`ck-dk-canonical-registry.md` §9](../coordination/ck-dk-canonical-registry.md)
are **adjacent** and both used `q*`, `h*` and `ũ(q*)` without qualification.
They are different points:

| glyph | **`q*_S`** (KC21) | **`q*_ρ`** (KC22) | ratio |
|---|---|---|---|
| `q*` | `1.109978593031523288402…` | `1.489894799688365248225…` | 1.342× |
| `h* = q* − 1/q*` | `0.2090603174197` | `0.818706471352` | 3.916× |
| `ũ(q*)` | `0.0094539496177732` | `0.14279999664469` (`= ρ`) | 15.10× |

- **`q*_S`** is the `S = 0` point, sitting ~1e-8 from the proton pin.
  ~~a *third, decay-sector determination of q₀*. It carries anchor meaning.~~
  **[WITHDRAWN 2026-08-15 — PR #5074, bean `qou-kh7e`, registry §9f.]** `q*_S`
  is root-found on `S = c₃ + Vol(4₁)` with `c₃` extracted from experimental
  `Q_β`, so it presupposes (H1) and is **not** an independent determination.
  What survives is the **glyph** distinction this document exists to make: the
  two `q*`s are different points and must not be conflated. `q*_S` carries
  anchor meaning only *conditional on (H1)*.
- **`q*_ρ`** is the unique real root > 1 of the irreducible degree-12 factor of
  the `Δ_net` numerator — a `Q_b` zero, hence a logarithmic branch point of
  `log R`, and the D-ladder's radius of convergence. It carries none.

`q*_ρ` is **recomputed** in the check from the degree-12 polynomial rather than
quoted, so the two numbers are independently derived (`h*_ρ` reproduces the
2026-08-09 audit's `0.818706471352` to 1e-11).

This is the overloaded-symbol trap named in AGENTS.md
§"Conditional-proved ≠ premise-established" rule 4 — the same failure class
`qou-qb8f` hit twice on the two `S`s. Nothing downstream is known to have
transferred an attribute across the two `q*`; the risk is prospective, and the
15× separation on `ũ(q*)` makes a silent mis-read cheap to commit and expensive
to catch.

**Fix:** both rows now subscript, and §9a carries the disambiguation table.

---

## 2. Defect 2 — the Φ_b scale claim is anchor-selective (`qou-uoo0`)

KC21 cited the Φ_b state-integral saddle as supplying the `|S|` scale
*"from geometry … smooth + anchor-blind"*, via volume deficit
`0.0094 ≈ |S(muon)| = 0.00968`.

This matters more than a wording nit: it is **(H1)'s sole surviving geometric
backing**. It is the evidence on which `qou-qb8f`'s *second* correction withdrew
the verdict "(H1) is UNDERIVED" and replaced it with "(H1) is motivated".

**The anchor-blindness is the defect, not the virtue.**

| quantity | value | anchor behaviour |
|---|---|---|
| `vol_deficit` | `0.0094025…` (both anchors) | **blind** — spread `2.2e-7` |
| `\|S_leak\|` | `0.00968298` (muon) / `0.03945936` (proton) | **swings 4.075×** |

A quantity that is identical at both anchors cannot reproduce one that differs
by a factor of 4 between them. So the match can hold at **at most one** anchor,
and it does:

| | miss |
|---|---|
| deficit vs `\|S_leak(muon)\|` | **2.896 %** ← the quoted match |
| deficit vs `\|S_leak(proton)\|` | **76.17 %** ← not quoted |
| ratio | **26.3×** |

This is the **same objection the corpus already accepts** one level down. From
`qbeta-c3-qstar-k31-repin.witness.json`, quoted verbatim in `qou-qb8e`:

> *"the carrier is anchor-blind (spread 1.23e-9) and is NOT the swinging
> empirical S, so `S = h·D(ũ)` is schematic, not a tight identity"*

The corpus applied that reasoning to `h·D(ũ)` and correctly declined to call it
an identity. It did **not** apply it to the Φ_b deficit, which fails the same
test for the same reason.

### 2.1 Calibrating the 2.9 %

`qou-qb8f`'s second correction already recorded "~2.9 % SCALE agreement, not an
exact identity". What it did not record is **what else sits inside that window**:

| | separation from the deficit |
|---|---|
| `ũ₀ = 0.0094539…` (the ladder's own expansion variable) | **0.544 %** |
| `\|S_leak(muon)\| = 0.0096830` | **2.896 %** |

The deficit is **5.32× closer to `ũ₀` than to the quantity it is said to
reproduce.** `ũ₀` carries no 4₁-volume content whatsoever — it is the substrate
expansion parameter. At a 2.9 % tolerance the match therefore does not
discriminate a geometric reading from a numerological one.

This is the *scale* analogue of the genericity test the corpus already accepted
for the *sign flip*
([`sleak_offset_genericity_check.py`](../../computations/qbeta/sleak_offset_genericity_check.py):
7/7 unrelated constants in a 0.049-wide window reproduce the same flip). The
sign flip was shown to be offset-generic; the scale match is shown here to be
tolerance-generic.

### 2.2 The witness is not at fault

[`qbeta-c3-phib-saddle-state-integral.witness.json`](../../computations/qbeta/qbeta-c3-phib-saddle-state-integral.witness.json)
records **both** anchors' `S_target`, states `"deficit 0.0094 ~ |S(muon)|"`
explicitly, and its own verdict says the saddle is *"smooth + anchor-blind ⇒
confirms no physical singular map"* — i.e. the producer understood exactly what
it had. The generalisation into "supplies the `|S|` scale" happened in the KC21
summary.

---

## 3. What this does and does not change

**Changed** (documentation only):

1. KC21 / KC22 subscript their `q*`, `h*`, `ũ(q*)`; new **§9a** glyph table.
2. New **§9b** scale caveat on the Φ_b → `|S|` match.
3. New **§9c** — the `qou-qb8f` (c) pointer.
4. §3's phrase *"the `−Vol(4₁)` piece is the solved bar-even part"* re-scoped to
   **motivated, not solved**.

**Not changed, and explicitly not refuted:**

- **c₃'s tier.** Still **EMPIRICAL / REFUTED as real-q**. No rung moved.
- **The Φ_b saddle itself.** `Im 𝔙 = 0` at the real substrate meridian
  (amphichirality) stands; `Vol(4₁)` to 4e-18 stands.
- **`Vol(4₁)` as an ingredient elsewhere**, and 4₁'s amphichirality.
- **Every theorem** in `SLeakZeroCrossing.lean` and
  `SLeakMagnitude{Offset,Taylor}Ratio.lean`. They are stated for a *generic*
  continuous function with the anchor signs as **hypotheses**, and are fine as
  stated — the defect was never in that Lean, it is in the interpretive step
  that `S_leak` *is* c₃'s bar-odd part. Sibling #4734's Lipschitz bound uses the
  **absolute** difference `|S₁ − S₂|`, where the offset cancels identically, and
  is untouched.
- **The 2026-08-09 convergence correction** and everything in KC22's arithmetic.

Scope-(a) throughout: this measures the committed numbers. It names no
invariant forbidding a 4₁-volume ingredient in c₃'s bar-even part, so it is
**not** a scope-(b) exclusion. (H1) is not refuted — it is *unsupported at the
tolerance at which it was asserted*.

---

## 4. The standing answer on (H1)

Consolidating three rounds of `qou-qb8f` plus this pass:

> **(H1) `c₃^even = −Vol(4₁)` is NOT derived.** The bar-split is not
> determinable from anchor data at all (it needs c₃ at `q ≈ 0.901`; both anchors
> sit at `q ≈ 1.10998`), so it must come from an assumed structural form.
> Neither named split is a derivation: `S_leak := c₃ + Vol(4₁)` and
> `S := −c₃/κ_(2,1)` are both **definitions**, and c₃ is recovered exactly from
> either — reparametrisations carrying no information. Its geometric motivation
> (the Φ_b deficit) is real but **muon-only**, and no tighter than the
> substrate's own `ũ₀`.
>
> **c₃'s bar-parity is undetermined by the present corpus.**

That last sentence is the load-bearing one, and it is `qou-qb8g`'s premise.

---

## 5. Method note — what nearly went wrong here too

`qou-qb8f`'s own recorded root cause was skipping corpus-grep checklist item 4
(*"check the relevant coordination ledger"*) — it grepped for its own framing's
strings and could not have found KC21, which is indexed under Φ_b /
volume-deficit vocabulary.

This pass started from the ledger instead, and both defects were found *in* it.
The lesson generalises: for any `c_k` question, read
[`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
first — and when the ledger and a witness disagree in emphasis, the witness is
usually the honest one.
