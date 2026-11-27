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
* It does not adopt Δ⁵ as the tau. The generation rule is the owner's call (card in the thread).
* Under the rule, the ring chart cannot make any heavier generation (scope (b), invariant:
  centrality of Δ²). The hierarchy, if the rule holds, must come from the mass map
  (the volume chart v/ℏ_q² vs the trace chart), which is bean `qou-se9w` / `qou-lsp9` territory.
* Genus 0, 3, 6: if the Bring genus ≤ 4 filter applies to the whole link, the rule allows only
  two generations. If it applies per component (T(2,5) has genus 2), all three pass. Open.
* Measured values appear only in the comparison table above, never in a check or a proof.
