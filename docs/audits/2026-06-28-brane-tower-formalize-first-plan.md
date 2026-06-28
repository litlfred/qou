# 2026-06-28 — Brane-tower m_can: formalize-first plan (single pipeline, conventions derived)

**Branch:** `claude/deuteron-m-sym-error-rf9i4u` · **PR:** #3016 · **Bean:** `km42`

Owner directives (this turn): **single pipeline, no special-casing** (no
`m_e·Vol(𝓑₃)`, no magic-A); **derive the conventions from the formalism**
(Frobenius pairing / categorical action), not numerically; **formalize-first**
(prove the convergence bound before the wide build). This doc records the
derivations and the Lean gates that must close before any A≥3 compute.

## 1. The single pipeline = the unified curvature-rank mass formula

No special-casing means one functional for every nucleus:

    𝔪_q,𝒦(𝒯) = Σ_{k=0}^{n-1} α_k · Φ_k(𝒦, 𝒯)      (prop:unified-curvature-rank-mass-formula)

with `α_{k≥4} = m_e·8G` **uniform** (`prop:plancherel-term-7-formulation`).
`m_can⁰ = m_unbnd,can − E₀·Δtr` (shipped, PR #3016) is the **k=0 descended
term** of this formula. The per-braid brane tower (`prop:per-braid-mass-tower`)
is the explicit jet-stratified content of the same Σ_k.

**No-special-casing corollary (the deep target).** A true single pipeline emits
the *nucleon* masses from the SAME functional — i.e. `m_p, m_n` as the k=0 term
on their own braids, not via the `canonical_mass` muon-anchored facade. That
requires the absolute-mass normaliser (`F_Bor = |tr_M|·[3]_q!/q³`) to be the
brane tower's own k≥1 content rather than a separate factor — this is exactly
bean **`ovud`** ("wire Li₂^q brane-tower into production F_Bor, replace /q³").
Until `ovud` lands, `m_can⁰` uses the facade nucleon masses; flagged here as the
one remaining special-case to excise for a literal single pipeline.

## 2. Convention Q2 (Li₂^q sign) — DERIVED from the categorical action

`bar-parity-split.md` (`prop:bar-parity-split`, Lean `QOU.Mass.evenPart_*`,
sorry-free): the bar-involution σ (q↦q⁻¹) splits every element; **binding is the
bar-EVEN (cosh) part**, β-decay the bar-odd (sinh) part.

- `Li₂^q(z) = Σ zⁿ/(n[n]_q)` is **bar-symmetric** (`[n]_q` is q↦q⁻¹-invariant),
  so it already lies in the binding (bar-even) channel. ✓
- The **argument sign** is the Hecke **antisymmetric eigenvalue −q⁻¹** (antipode
  `S(σᵢ)=σᵢ⁻¹`; Hecke `(σ−q)(σ+q⁻¹)=0`). The antisymmetric channel carries −q⁻¹,
  so the canonical brane-tower term is

      g(x) = −Li₂^q(−x)         (= `_li_2_q_util` doc lines 34–41)

The bare `+Li₂^q(+x)` (`compute_t2_t3_from_vols`) is an unnormalised helper, **not**
the binding projection. **Q2 resolved: `g = −Li₂^q(−x)`.**

## 3. Convention Q1 (A=2 pair stratum) — DERIVED from the strata

Per-braid strata: ℓ=0 = {W} (descended, functional `|tr_M(W)|`); ℓ=2 = pairs
(functional `z²·g(|tr_M(ξξ')|)`). For A=2 the single pair *braid* coincides with
W, but the two **functionals** differ (`|·|` vs `z²·g(·)`). The prop's
double-count carve-out forbids repeating the **descended product** `|tr_M|` per
jet level — it does **not** forbid the dilog pair term. **Q1 resolved: the A=2
pair IS included.** Consequence (honest): the deuteron tower is `+33%`
(`g=−Li₂^q(−·)`), worse than the `+12%` k=0 term — the tower **adds** binding;
it does not close the over-bound deuteron (that gap is not a truncation error).

## 4. Convention Q3 (formalize-first gate) — REFUTED as stated, RESOLVED by the Borromean nucleon

**The gate fired and the bound is FALSE as stated.** The prop's standing claim
`|tr_M(ξ)| < q₀` is **refuted** for the free same-species proton pair:

    tr_M(proton, atom-word) = 1.065306 > 1   ⇒   tr_M(pp, free) = tr_p² = 1.134877 > q₀ = 1.109979

(by Markov disjoint-multiplicativity, Wenzl §1.7 — the ambient H_{3A} path gives
the *same* product, verified at ⁴He H₁₂: `1.134877`). This is a **(b) structural
exclusion** with cited invariant: the Li₂^q radius is `|z| < q` (proved in
`li_2_q`, returns ∞ at `|z|≥q`), and `tr_p² > q₀` is exact. So the Li₂^q tower
**diverges on the free pp pair for every nucleus with Z ≥ 2**; Z≤1 (D, T)
converge. The Lean lemma as originally scoped is **not authorable** (false).

**Root cause + resolution (ties to §6 / the Borromean question).** The
divergence is driven entirely by the *binding pipeline's* proton word —
`atom_braid_word_3A(1,0)`, colour-weighted — whose trace `1.0653 > 1`. The
**canonical Borromean nucleon** `β_Bor` (the one `F_Bor` / bean `ovud` use) has

    |tr_M(β_Bor)| = (4+h²−3h⁴−h⁶)/(h²+4) = 0.998562 < 1   (Lean: BorromeanMarkovTrace)

so the Borromean free pairs are **pp 0.9971, pn 0.9219, nn 0.8524 — ALL < q₀**.
With the Borromean nucleon the Li₂^q tower **converges for all Z**.

**Revised Q3 / Lean target:** not "prove `|tr_M(ξ)|<q₀` for the atom-word" (false)
but **(i)** the bound `|tr_M(β_Bor^{⊗Z}·β_n^{⊗N})| < q₀ for Z,N` IN the Borromean
representation (true, gated on `|tr_M(β_Bor)|<1`, which is the Lean-proved closed
form), and **(ii)** a `convergence-requires-Borromean-nucleon` finding: the
binding tower must use `β_Bor`, not the colour-weighted atom word. **Caveat:**
switching changes every binding number (deuteron pn pair `0.984 → 0.922`), so it
must be re-validated against AME — a hypothesis, not a free fix.

## 6. The Borromean question (owner): why `β_Bor`, not per-knot? — ANSWERED

**`β_Bor` is the nucleon's OWN knot, not a global assumption.** A baryon is
`B = 𝓑₃(K₀₁,K₀₁,K₀₁)` (`def:borromean-baryon`) — three unknotted colour tubes
in a **Borromean** link. The Borromean property (cut any one ring ⇒ the other two
fall apart) **is confinement**: no single colour tube / quark can be isolated. So
at the *nucleon (proton/neutron) confinement level* — exactly the owner's reading
— the knot IS Borromean, and `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³` is the **per-knot**
factor *for the nucleon*.

- **When is Bor a global assumption (a bug)?** Only when `Vol(𝓑₃)` is applied
  *uniformly to A≥2 nuclei* (the 9a uniform-Vol issue: 64 scripts use
  `vol_density_borromean` for all atoms). That collapses each nucleus's own knot
  to the proton's — the special-casing the owner wants gone.
- **Why not volume-per-knot?** It **should** be per-knot. The single pipeline is
  per-knot for *every* nucleus, with `β_Bor` the **A=1 (nucleon) instance** — not
  a special case, just the smallest knot. The owner's instinct is the correct
  design.
- **Bonus (the §4 link):** the Borromean (per-knot-consistent) nucleon is *also*
  what makes the Li₂^q tower converge. Per-knot + Borromean unifies the
  no-special-casing principle with the convergence gate.
- **Critical caveat:** the absolute-mass `m_e·Vol(K)/ℏ_q²` per-knot form gives
  wrong numbers (966 / 406, see `canonical_mass.py`); the canonical absolute mass
  is the **muon-anchored** `F_Bor`. So a per-knot single pipeline needs the
  muon-anchored normaliser generalised per-knot — the combined 9a + `ovud` open.

## 5. Status / gates

| Item | State |
|---|---|
| `m_can⁰ = m_unbnd,can − E₀·Δtr` (k=0) | ✅ shipped (PR #3016) |
| Q2 sign `g = −Li₂^q(−x)` | ✅ derived (§2), locked in `per_braid_tower.py` |
| Q1 A=2 pair inclusion | ✅ derived (§3), deuteron tower `+33%` (honest) |
| Q3 bound `|tr_M(ξ)|<q₀` (atom-word) | 🔴 **REFUTED** — `tr_p²=1.135>q₀`; tower diverges for Z≥2 |
| Q3 resolution: Borromean nucleon | 🟢 `|tr_M(β_Bor)|=0.9986<1` ⇒ all free pairs <q₀, converges ∀Z |
| Single-pipeline = per-knot Borromean | 🟡 design fixed (§6); validation + ovud-normaliser open |

**Next action (revised by the §4 refutation):** do NOT author the false bound.
Instead **(1)** re-express the binding tower over the **Borromean nucleon**
`β_Bor` (converges ∀Z) and re-validate the deuteron/³He/⁴He binding against AME
(switching changes the numbers); **(2)** Lean the *true* bound
`|tr_M(β_Bor)|<1 ⇒ pair traces <q₀`. The per-knot Borromean tower is the single
pipeline; absolute masses still need the muon-anchored normaliser per-knot
(9a + `ovud`).
