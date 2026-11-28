# Why the tau has no derived word (2026-11-27)

## Short answer
No lepton word in the corpus is derived. The electron word is an owner ruling
(2026-11-21: σ₀σ₁σ₀ ∈ B₃, Hopf closure; trefoil σ₀³ kept as backup). The muon has no
ruling in the three-strand setting at all. So there is no generation rule to apply a
third time, and every tau attempt so far was a search for a word whose number matched.

## Evidence
1. **The old ladder died with the electron move.** Canon was e = T(2,3), μ = T(2,5),
   τ = T(2,7) in B₂ (`observations/symmetry-preserving-leptons.md`; muon T(2,5) ruled
   2026-06-30). On 2026-11-21 the electron moved to σ₀σ₁σ₀ ∈ B₃. Nobody re-derived μ or τ
   on three strands. Same day the shell rule T(2,n_s) was withdrawn because (σ₀σ₁)²σ₀
   closes to T(2,4), not T(2,5) (owner-rulings row 59).
2. **The muon word is in conflict.** Probes use 4₁ = (σ₀σ₁⁻¹)²
   (`computations/probes/electron_weight/ring_mass_braid_words_probe.py`), while
   `canonical_lepton_braid_words.py` says 4₁ is the Higgs and the muon is T(2,5).
   The muon ratio m_μ/m_e = Vol(4₁)/ℏ_q² is a volume chart, not a word's trace.
3. **The tau T(2,7) has volume 0**, so the volume chart cannot read it.
4. **Every tau-mass route was selection or refuted** (bean `qou-pvu4`, roast 2026-09-03):
   25-knot Vol/ℏ^k search refuted at 1 %; B₃ ≤ 7-crossing census selected nothing
   (`qou-k93c`); every positive linear functional of H₂(q) excluded; the Koide-circulant
   3477.44 (`qou-j96h`) rests on an isolated equipartition hypothesis (a CAL-4-type fit).
   Blocking beans `qou-lsp9`, `qou-se9w` are still todo.

## New structural measurements (this thread, no fitting)
Ring mass m(β) = [2]³ q^{-2w} tr_D(β), U = −q ∂_q log m.

* At q = 1 the ring mass depends only on the permutation: m = 4 + 2χ₂₁ ∈ {8, 4, 2}.
  So at q = 1 no word gives a ratio like 207 or 3477. At q₀ a ratio of 3477 needs a
  writhe of about −78. **The ring chart cannot make the lepton hierarchy with small words.**
* Positive ladders get *lighter* (measured at q₀):

| ladder | e | μ | τ | U(q₀) e/μ/τ |
|---|---|---|---|---|
| Δ^{2k+1} (centre) | 1 | 0.5347 = q₀⁻⁶ | 0.2859 = q₀⁻¹² | 2.485 / 8.485 / 14.485 |
| σ₀^{2n}σ₁ (T(2,2n)) | 1 | 0.7624 | 0.5924 | 2.485 / 4.757 / 6.778 |
| σ₀^{2n+1}σ₁ (knots) | 1 | 0.8707 | 0.7382 | 1.386 / 3.379 / 5.545 |

## Candidate generation rules (for the card)
1. **Universality ladder (derived).** Lepton universality says every generation couples to
   every photon exactly as the electron does. Words with the same photon commutation as
   σ₀σ₁σ₀ differ by the centraliser of {σ₀, σ₁} in B₃, which is the centre ⟨Δ²⟩ (Chow).
   So the generations are Δ^{2k+1}: e = Δ, μ = Δ³, τ = Δ⁵ = σ₀σ₁σ₀(σ₀σ₁)⁶.
   Closure of Δ^{2k+1} = T(2,2k+1) ∪ its core axis, lk = 2k+1: e = Hopf, μ = trefoil ∪ axis,
   τ = cinquefoil ∪ axis. On the ring chart m_k = q^{-6k} m_e exactly and U_k = U_e + 6k,
   so the masses go the wrong way. That is a scope-(b) statement (centrality of Δ²), which
   says the hierarchy must come from the mass map, not the word. Seifert genus 0, 3, 6.
2. **Torus-link ladder.** e = T(2,2), μ = T(2,4), τ = T(2,6). Copies the old pattern; not derived.
3. **Trefoil backup.** Revert to σ₀³ and τ = T(2,7). Reverses the 2026-11-21 ruling.
4. **Mass map first.** Leave the word open and derive the volume-vs-trace link first.

## Formalisation (this PR)
* Lean: `QOU/Observations/LeptonUniversalityLadder.lean`. Proves Δσ₀ = σ₁Δ, Δσ₁ = σ₀Δ, Δ² central
  on the generators, every Δ^{2k+1} couples like Δ (forward direction of the rule), two closure
  components, ρ(Δ) = [[0, −1], [−1, 0]] (independent of q), ring mass of Δ^{2k+1} = [4]/q³ · q^{−6k},
  each rung = previous · q⁻⁶, all rungs = 4 at q = 1, strictly decreasing for q > 1.
  The converse (centraliser of {σ₀, σ₁} in B₃ = ⟨Δ²⟩, Chow 1948) is cited, not formalised.
* Probe: `computations/probes/tau_word/universality_ladder_probe.py`, exact over ℚ(q), 19/19.
  It also checks lk = 2k+1, the {0,2} sublink σ^{2k+1} (T(2,2k+1)), Seifert genus 3k.

## What this does and does not say
* Owner ruling 2026-11-27 (card 22:37Z): the universality ladder is adopted as a working conjecture, so τ = Δ⁵ = σ₀σ₁σ₀(σ₀σ₁)⁶.
* Under the rule, the ring chart cannot make any heavier generation (scope (b), invariant:
  centrality of Δ²). The hierarchy, if the rule holds, must come from the mass map
  (the volume chart v/ℏ_q² vs the trace chart), which is bean `qou-se9w` / `qou-lsp9` territory.
* Genus 0, 3, 6: if the Bring genus ≤ 4 filter applies to the whole link, the rule allows only
  two generations. If it applies per component (T(2,5) has genus 2), all three pass. Open.
* Measured values appear only in the comparison table above, never in a check or a proof.

## Cross-thread note (electron-weight thread, 2026-11-27 23:00Z; not adopted)
* Δ^{2k+1} are periodic 3-braids: torus-type closures, Vol = 0, Kashaev invariants grow only
  polynomially, so no Vol/ℏ term exists on this ladder.
* Coloured ring masses (U_q(sl₂) spin (N−1)/2, framing by stabilisation, N = 2 equal to [4]/q³) are
  wrong-way at every N: N=3 1/0.263/0.0742, N=4 1/0.139/0.0212, N=5 1/0.0768/0.00627.
* The mirror ladder Δ^{−(2k+1)} is the heavier direction for q > 1 (ratio q^{+6k} on the ring chart).
  Which chirality the electron carries is fixed by the 2026-11-21 ruling (σ₀σ₁σ₀); the mirror is
  recorded here only as an observation.

## Verification
* `scripts/lean-verify.sh` on `LeptonUniversalityLadder.lean`: exit 0, sorry-free.
  `#print axioms`: `propext`, `Classical.choice`, `Quot.sound` only (ladder_swap_left: `propext`).
* Imported in `QOU.lean`.

## Pseudo-Anosov (second part, 2026-11-27 23:29–23:36Z)
The owner reopened the universality ruling after the mass-map thread showed every central-step
ladder is volume-blind (PR #9825: Δ² ↦ −I, same Nielsen–Thurston type at every rung), and wrote
*"Work anosov"*.

**Structure** (`QOU/Observations/LeptonChargeClassTrace.lean`, sorry-free): under
B₃ → SL(2,ℤ), σ₀ ↦ [[1,1],[0,1]], σ₁ ↦ [[1,0],[−1,1]], the image mod 2 is the permutation
(SL(2,𝔽₂) ≅ S₃), so every word of odd length (the electron's charge class: two-component closure)
has even trace. The least-trace pseudo-Anosov σ₀σ₁⁻¹ (trace 3; its square closes to 4₁) is
therefore neutral, consistent with the old canon 4₁ = Higgs.

**Charge class ordered by |tr|** (probe `charge_class_pseudo_anosov_probe.py`, SnapPy high precision,
words ≤ 9, 4/4): 0 Δ periodic; 2 σ₀^odd reducible; 4 σ₀²σ₁⁻¹, closure ∪ axis volume
5.33348956689811958159 (magic manifold), one class; 6 σ₀⁴σ₁⁻¹, 6.35458655720065195270, one class;
8 two classes (8.35550…, 6.75519…). Neutral class for reference: 3 → 4.05977 (= 2 Vol(4₁)).

**Ruling** (owner card 23:35Z): e = Δ, μ = σ₀²σ₁⁻¹, τ = σ₀⁴σ₁⁻¹. Each pseudo-Anosov word is σ₀ⁿ
times the photon's chiral vertex σ₀σ₁⁻¹. The rule "periodic, then pseudo-Anosov by |tr|" re-derives
e = Δ and is unique up to mirror and centre for three generations; a fourth would need a further rule.

**Caveats.** μ closes to the Hopf link, like e, so every closure invariant (ring mass, coloured
masses, U) is equal for e and μ (PR #9832); τ closes to T(2,4). The mass map must read the braid
with its axis. Volume ratio τ/μ = 1.19: volume alone cannot carry the hierarchy.

**Backups kept** (owner: *"keep the alternatives… as a fallback"*): universality ladder Δ, Δ³, Δ⁵
(§above, Lean kept); shared 4₁ carrier; T(2,2n) links; B₂ trefoil ladder.


## Least-crossing ladder (2026-11-28)

PR #9879 showed that def:mass-identity, as written, is the N = 2 ring trace on braid classes and is Markov invariant, so the mass depends only on the closure. Under it the least-trace ladder ties e and μ (both close to the Hopf link): m = [4]/q³ for both. The trace cannot serve as a selector, because one link has 3-braid representatives of many traces.

A selector that is itself a link invariant is the crossing number. SnapPy enumeration of odd 3-braid words up to length 7, keeping two-component, non-split, prime closures, gives, in crossing order:

| lepton | word | closure | crossings | lk | volume |
|---|---|---|---|---|---|
| e | σ₀σ₁σ₀ | Hopf link | 2 | 1 | 0 |
| μ | σ₀⁴σ₁⁻¹ | T(2,4) | 4 | 2 | 0 |
| τ | σ₀²σ₁⁻¹σ₀σ₁⁻¹ | Whitehead link | 5 | 0 | 3.66386 |

At 5 crossings the only other two-component link, Hopf # trefoil (σ₀³σ₁²), is composite. The crossing counts after simplification are upper bounds; they agree with the knot-table values for these links. Owner ruling: *"Keep definition, new words"*. N = 2 ring masses and U(1) = 3·lk = 3, 6, 0 are in PR #9881, unscored. U is not monotone along the ladder because the Whitehead link has lk 0. That is recorded as a consequence, not adjusted.
