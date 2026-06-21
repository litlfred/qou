# Lean link-invariant library — toward crossing-minimality of the Borromean confinement operator

**Branch:** `claude/lean-tl3-kauffman-bracket-2026-06-17`
**Picks up:** the last residual of the Brunnian confinement selection (#2455).
After the Brunnian *signature* and *sublink-triviality* were proved in Lean
(`confinement_operator_selection.lean`, `decide`, axiom-free), the one open
piece was **crossing-minimality** — that the Borromean is *the* minimal
nontrivial Brunnian 3-link. That needs recognising **3-link nontriviality**, and
since `B₃` is non-abelian the `B₂ ≅ ℤ` exponent-sum test does not reach it: a
genuine link invariant is required. Author directive: *"worst case, enumerate in
Python to get the answer and assert it in Lean — `B₃` is small enough."* This
library realises that.

## Brick 1 (this PR) — a computable link invariant, Borromean nontriviality proved

[`content/quantum-observable-universe/lean/QOU/Knots/KauffmanTL3.lean`](../../content/quantum-observable-universe/lean/QOU/Knots/KauffmanTL3.lean):

- **`LP`** — integer Laurent polynomials `ℤ[A, A⁻¹]` with normalised
  representation and `DecidableEq` (so polynomial equality is `decide`-able).
- **`TL`** — the Temperley–Lieb algebra `TL₃`, only **5-dimensional**
  (`Catalan 3 = 5`); full multiplication table from `eᵢ² = δeᵢ`, `e₁e₂e₁ = e₁`,
  `e₂e₁e₂ = e₂`.
- **`bracket`** — the Kauffman bracket of a 3-braid closure (`σᵢ ↦ A·1 + A⁻¹·eᵢ`,
  Markov-trace loop counts), an `LP`.
- **`borromean_link_nontrivial`** — proved **by `decide`, axiom-free**: the
  bracket of `(σ₀σ₁⁻¹)³`'s closure (a degree-28 Laurent polynomial) differs from
  the 3-unlink's (`δ³`). Both closures have writhe 0, so the unnormalised bracket
  already separates them. **The Borromean rings are a nontrivial link, machine-
  verified.**

This is the invariant the `B₂`-exponent-sum test could not provide. (`decide`
takes ~45 s on the single degree-28 reduction — acceptable for one theorem;
brick 2's enumeration will need `native_decide`, see below.)

## Brick 2 (DONE, this PR) — crossing-minimality by enumerate-then-assert

`theorem QOU.Knots.TL.borromean_crossing_minimal` in
[`KauffmanTL3.lean`](../../content/quantum-observable-universe/lean/QOU/Knots/KauffmanTL3.lean),
proved by **`native_decide`** (axioms `Lean.ofReduceBool` + `Lean.trustCompiler`).
It enumerates **every** 3-braid word of length `< 6` over `{σ₁^±, σ₂^±}` and asserts:

1. the Borromean `(σ₁σ₂⁻¹)³` is pure, Brunnian, nontrivial and has word-length 6;
2. no word of length `< 6` is simultaneously Brunnian and nontrivial.

Two decidable invariants combine, both already in the library:

- **Brunnian** = every 2-sublink trivial = each deleted-strand 2-braid has
  `B₂ ≅ ℤ` exponent sum `0` (`b2class`, re-implemented from #2455 in the
  `{σ₁,σ₂}` indexing this file uses).
- **Nontrivial** = the **writhe-normalised** Kauffman bracket — the Jones
  invariant `(-A³)^(-w)·⟨·⟩`, a genuine ambient-isotopy invariant — differs from
  the 3-unlink's `δ³`. Normalisation was *essential*: the unnormalised bracket
  (brick 1) shifts by `(-A³)^±1` under R1, so a *trivial* braid of nonzero writhe
  would spuriously read "nontrivial"; only the Borromean (writhe 0) was safe
  unnormalised. Jones-nontrivial ⇒ genuinely nontrivial (the converse can fail,
  which only makes the lower bound safer — it never over-counts).

**Per-length breakdown** (`#eval`, reproducing the Python oracle's table and
proving the theorem is non-vacuous):

| len | pure | pure+Brunnian | nontrivial-Brunnian |
|----:|-----:|--------------:|--------------------:|
| 0 | 1 | 1 | 0 |
| 2 | 8 | 4 | 0 |
| 4 | 96 | 28 | 0 |
| 6 | 1408 | 248 | **4** (the Borromean family) |

The **28 Brunnian-but-trivial** words at length 4 are the load-bearing check: there
*are* Brunnian braids below 6 crossings, but the Jones invariant certifies every
one of them trivial, so none counts. At length 6 exactly **4** words are
nontrivial-Brunnian — `(σ₁σ₂⁻¹)³` and its sign/mirror variants, all
Borromean-signature — matching the oracle. The `native_decide` verdict (minimal
`= 6`) **agrees with** the Python enumeration
(`b3_brunnian_minimality_enumeration.py`); the agreement is the audit.

- **Performance:** ~1365 words below length 6 (+ the length-6 witness check), each
  a Laurent-polynomial bracket — far beyond kernel `decide` (brick 1's *single*
  bracket took ~45 s), so `native_decide` (compiled) is required. It trusts the
  Lean compiler (the same trust class as the Python oracle), documented in the
  theorem docstring and the axiom audit. Whole-file `lean`-direct check: ~36 s.

## Honest scope

- Brick 1 is a **genuine, axiom-free** machine proof that the Borromean rings are
  a nontrivial link — the previously-missing invariant.
- Full crossing-minimality (brick 2) is **`native_decide`-backed** (axioms
  `Lean.ofReduceBool` + `Lean.trustCompiler`), not kernel-`decide` — the finite
  computation is too large for the kernel. This is exactly the author's
  enumerate-then-assert pattern; the verdict cross-checks the Python oracle.
- Scope is **3-braid closures** (the framework's 3-quark setting) and **braid-word
  crossing number**, not full link-theoretic uniqueness over all links; and
  nontriviality is the Jones invariant — a *sufficient* (not complete) certificate,
  which only strengthens the lower bound. The literature uniqueness (Borromean =
  the unique 6-crossing Brunnian link, Rolfsen) is unchanged.
- None of this touches binding *magnitude* (still research-grade). It completes
  the *selection-principle* formalisation: confinement = crossing-minimal
  nontrivial Brunnian, now with both the triviality (B₂) and nontriviality
  (Kauffman/TL₃) invariants in Lean.

## Brick 3 (DONE) — library validation + reuse: the figure-eight knot `4₁`

The Kauffman/`TL₃` bracket is reusable for *any* 3-braid closure. The figure-eight
`4₁ = closure of (σ₁σ₂⁻¹)²` is the natural reuse target — the **q₀-calibration
knot** (`m_μ/m_e = Vol(4₁)/ℏ_q²`, CAL-2). Two new theorems in
[`KauffmanTL3.lean`](../../content/quantum-observable-universe/lean/QOU/Knots/KauffmanTL3.lean),
both **`decide`, AXIOM-FREE**:

- `figure_eight_jones`: `jones (4₁ closure) = δ · V(4₁)` with
  `V(4₁) = A⁸ - A⁴ + 1 - A⁻⁴ + A⁻⁸`. This is an **exact polynomial identity
  against a literature invariant** — a stronger bracket validation than brick 1's
  Borromean nontriviality (which only compared two brackets for inequality). It
  retroactively confirms the brick 1/2 bracket is the genuine Jones invariant
  (`jones (4₁)/δ` is exactly the figure-eight Jones polynomial).
- `figure_eight_knot_nontrivial`: `jones (4₁) ≠ jones (unknot)` (`δ·V(4₁) ≠ δ`).

## Brick 4 (DONE) — library validation: the trefoil knot `3₁` (a chiral knot)

Completing the library's knot ladder (unknot → trefoil → figure-eight → Borromean),
the trefoil `3₁ = T(3,2) = closure of (σ₁σ₂)²` — the all-positive `(3,2)` torus knot,
a 1-component 3-braid closure — is the third validation target. Two new theorems in
[`KauffmanTL3.lean`](../../content/quantum-observable-universe/lean/QOU/Knots/KauffmanTL3.lean),
both **`decide`, AXIOM-FREE**:

- `trefoil_jones`: `jones (3₁ closure) = δ · V(3₁)` with
  `V(3₁) = -A⁻¹⁶ + A⁻¹² + A⁻⁴` (classically `t = A⁻⁴` ↦ `-t⁴ + t³ + t`). A second
  **exact polynomial identity against a literature invariant** — and the first on a
  *chiral* knot: unlike the amphichiral figure-eight, `V(3₁) ≠ V(mirror 3₁)`
  (`-t⁻⁴+t⁻³+t⁻¹`), so the bracket is shown to track handedness. The chirality the
  all-positive `(σ₁σ₂)²` selects in this convention (`σᵢ ↦ A·1 + A⁻¹·eᵢ`, `t = A⁻⁴`)
  is `-t⁴+t³+t`, verified against the `#eval` oracle before asserting.
- `trefoil_knot_nontrivial`: `jones (3₁) ≠ jones (unknot)` (`δ·V(3₁) ≠ δ`).

As with `figure_eight_jones`, the identity is proved by transitivity through two
value lemmas (`jones_trefoil_value`, `delta_mul_jonesTrefoil`) — a single combined
`decide` exceeds the elaboration heartbeat budget.

## Brick 5 (DONE) — library validation: the Hopf link (first multi-component named link)

Bricks 3–4 validated *knots* (1-component); brick 5 extends the bracket to a genuine
multi-component **link** against a literature Jones polynomial. The **Hopf link** —
the closure of `σ₁²` — is the framework's **CAL-3 / `m_π`** object (`Vol(Hopf) = 0`,
the meson scale). Four new theorems in
[`KauffmanTL3.lean`](../../content/quantum-observable-universe/lean/QOU/Knots/KauffmanTL3.lean),
all **`decide`, AXIOM-FREE** (`#print axioms`: *does not depend on any axioms*):

- `hopf_link_jones`: `jones (σ₁² closure) = δ² · V(Hopf)` with `V(Hopf) = -A⁻² - A⁻¹⁰`
  (`t = A⁻⁴`: `-t^{1/2} - t^{5/2}`). The **first named multi-component link** validated
  against a literature invariant — bricks 1–2 only proved the Borromean bracket *differed*
  from the unlink's (`≠`), never reproduced a *known* `V` (`=`).
- `hopf_link_nontrivial`: `jones (hopf) ≠ jones (unlink₃)` (`δ²·V(Hopf) ≠ δ³`).
- value lemmas `jones_hopf_value`, `delta_sq_mul_jonesHopf`.

**Honest scope.** A 3-braid closure always carries the third strand, and `σ₁²` leaves
`σ₂` untouched, so its closure is **Hopf ⊔ split-unknot** (3 components), not the bare
2-component Hopf link — unavoidable in `TL₃`. The split unknot contributes exactly one
`δ`; of the two `δ` factors, one is that split unknot, one the 1-component normalisation,
and the residue `jones (hopf) / δ² = V(Hopf)` is the genuine 2-component Hopf-link Jones
polynomial. The quark–antiquark (2-strand) + spectator reading is the framework-natural
presentation. The Hopf link is also chiral (`V(Hopf) ≠ V(mirror)`); the all-positive
`σ₁²` selects this handedness.

## Brick 6 (DONE) — library validation: the `(3,4)` torus knot `8₁₉`

Completing the ladder with a higher-crossing knot. `8₁₉ = T(3,4) = closure of (σ₁σ₂)⁴`
(permutation a 3-cycle ⇒ single component). At 8 crossings and Jones span `20` it is the
**widest reduction in the ladder** — a stress-test of the kernel-`decide` bracket compute
(~70 s, `maxHeartbeats 2000000`) — and a third *chiral* cross-check. Theorems in
[`KauffmanTL3.lean`](../../content/quantum-observable-universe/lean/QOU/Knots/KauffmanTL3.lean),
all **`decide`, AXIOM-FREE**:

- `torus819_jones`: `jones (8₁₉ closure) = δ · V(8₁₉)` with
  `V(8₁₉) = -A⁻³² + A⁻²⁰ + A⁻¹²` (`t = A⁻⁴`: `-t⁸ + t⁵ + t³`). This is the closed-form
  torus-knot Jones polynomial `V(T(m,n)) = t^{(m-1)(n-1)/2}(1 - t^{m+1} - t^{n+1} + t^{m+n})
  / (1 - t²)` at `(3,4)`, reducing to `t³(1 + t² - t⁵)`.
- `torus819_knot_nontrivial`: `jones (8₁₉) ≠ jones (unknot)` (`δ·V(8₁₉) ≠ δ`).
- value lemmas `jones_torus819_value`, `delta_mul_jonesTorus819`.

The library knot/link ladder is now **unknot → trefoil `3₁` → figure-eight `4₁` →
Hopf link → 8₁₉ → Borromean** — every rung an exact literature cross-check (knots) or
nontriviality + literature `V` (links), all axiom-free `decide`.

## Follow-ups (post-merge)

- **qa-sweep sidecar refresh — `prop:confinement-operator-selection`.** #2455
  changed the block's `.md`/`.ts`/`.lean`; its
  [`confinement-operator-selection.qa.json`](../../content/quantum-observable-universe/particle-interactions/confinement-operator-selection.qa.json)
  sidecar still carries the pre-#2455 `source_hashes`
  (`md a7e748cdc000`, `ts 6c77b7d17276`, `lean f8db5d74c684`, last reviewed
  2026-05-27) and now reads **stale**. Refresh with
  `bun run content/pipeline/qa-sweep.ts content/quantum-observable-universe/particle-interactions/confinement-operator-selection.md`
  (or `/integration-audit voice` to batch the axis). **Could not run in the
  sparse remote checkout** — `content/pipeline/` + `folio-assistant/schemas/` are
  absent here — so this is a full-checkout / CI follow-up.

## Cross-links
- `content/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_operator_selection.lean` — the Brunnian signature + sublink-triviality (`decide`, axiom-free).
- `computations/probes/b3_brunnian_minimality_enumeration.py` — the Python enumeration oracle.
- `docs/audits/2026-06-17-b3-dense-sdp-lever-closed.md` — why the selection is topological, not operator-space.
