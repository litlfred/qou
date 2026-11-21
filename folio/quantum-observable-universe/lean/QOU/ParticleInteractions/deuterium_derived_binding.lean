import Mathlib.Tactic
import Mathlib.Data.Real.Basic

/-!
# QOU.ParticleInteractions.deuterium_derived_binding

**Canonical declaration** for content block
[`prop:deuterium-derived-binding`](../../../quantum-observable-universe/particle-interactions/deuterium-derived-binding.md): *QOU.ParticleInteractions.deuterium_derived_binding*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.ParticleInteractions


/-- Abstract context for the `deuterium_derived_binding` claim —
    manuscript-themed typed fields below; sub-claims encode the
    deuteron-binding pipeline (proton/neutron NF construction →
    Hecke embedding → factorisation → T_pn definition → binding-
    energy formula → numerical match). -/
class DeuteriumDerivedBindingContext where
  /-- Proton number `Z` (always 1 for deuterium). -/
  Z : ℕ
  /-- Neutron number `N` (always 1 for deuterium). -/
  N : ℕ
  /-- The braid representative type. -/
  Braid : Type
  /-- Hecke algebra type `H_n(q)` indexed by strand count. -/
  HeckeAlgebra : ℕ → Type
  /-- The substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- Electron mass `m_e : ℝ`. -/
  m_e : ℝ
  /-- Borromean baryon volume `Vol(𝓑_3) ≈ 7.32772`. -/
  Vol_B3 : ℝ
  /-- Fine-structure constant `α_EM`. -/
  α_EM : ℝ
  /-- The deuterium binding energy `B(d) : ℝ`. -/
  B_d : ℝ
  /-- The Markov-trace evaluation `tr_M(p) : ℝ` of the proton NF. -/
  tr_M_p : ℝ
  /-- The Markov-trace evaluation `tr_M(n) : ℝ` of the neutron NF. -/
  tr_M_n : ℝ
  /-- The Markov-trace evaluation `tr_M(T_pn · n) : ℝ` of the
      inter-nucleon-coupled neutron. -/
  tr_M_Tpn_n : ℝ
  /-- Proton NF braid word in `H_3(q)` (encoded as a `List ℤ` of
      Hecke-generator indices; negatives denote inverses). -/
  NF_p_braid_word : List ℤ
  /-- Neutron NF braid word in `H_3(q)`. -/
  NF_n_braid_word : List ℤ
  /-- Length of the Borromean baryon braid word `𝓑_3 = σ_0σ_1σ_2σ_0σ_1σ_2`. -/
  braid_length_B3 : ℕ
  /-- Strand count of the H_3 source algebra. -/
  h3_strand_count : ℕ
  /-- Strand count of the H_6 target algebra. -/
  h6_strand_count : ℕ
  /-- Inter-nucleon Hecke generator value `σ_0`. -/
  sigma_0 : ℝ
  /-- Inverse Hecke generator `σ_0⁻¹`. -/
  sigma_0_inv : ℝ
  /-- The time-reversal-symmetric inter-nucleon operator `T_pn`. -/
  T_pn : ℝ
  /-- CODATA deuteron binding energy `B_exp = 2.2246 MeV`. -/
  B_exp : ℝ

/-- **Proposition statement** (from manuscript):

Let $\mathrm{NF}(\mathfrak{p})$ and $\mathrm{NF}(\mathfrak{n})$
be the [proton](#def:categorical-proton) and
[neutron](#def:categorical-neutron) normal forms in $H_3(q)$,
each constructed as $\mathcal{B}_3 \cdot \mathrm{crossings}(quarks)$
([confinement selection](#prop:confinement-operator-selection))
with $\mathcal{B}_3 = \sigma_0\sigma_1\sigma_2\sigma_0\sigma_1\sigma_2$.
The full canonical deuteron braid word
$\beta_D = \mathtt{atom\_braid\_word\_3A}(1, 1) \in H_6(q)$
([`mass_at_3A_proper.atom_braid_word_3A`](https://github.com/litlfred/qou/blob/main/computations/mass_at_3A_proper.py))
factors as $\mathrm{NF}(\mathfrak{p}) \cdot T_{pn} \cdot \mathrm{NF}(\mathfrak{n})$
under the H_3 → H_6 Hecke embedding, where
$T_{pn} = \frac{1}{2}(\sigma_0 + \sigma_0^{-1})$ is the time-reversal
symmetric crossing operator at the inter-nucleon site (the unique
generator of $\beta_D$ that crosses a proton strand with a neutron
strand). Then the deuterium binding energy is*

$$
  B(d) = \bigl[\mathrm{tr}_M(\mathfrak{p})
       + \mathrm{tr}_M(\mathfrak{n})
       - \mathrm{tr}_M(T_{pn} \cdot \mathfrak{n})\bigr]
       \times m_e \cdot \mathrm{Vol}(\mathcal{B}_3)
       \times (1 - \alpha_{\mathrm{EM}}/2).
$$

## Derivation

Deuterium has exactly one inter-nucleon crossing site (the $p$-$n$
pair).

    The Lean encoding **names** the conditional conjecture as a `Prop`
    (pattern C of the vacuity-fix playbook): the context class is the
    carrier of the deuteron-binding-pipeline data, and
    `deuterium_derived_binding` is the proposition that the six
    manuscript sub-claims hold for that data.  It is *not* asserted
    (no `theorem … := ⟨ctx.claim_*⟩` self-assuming projection); a
    discharging instance is the open conditional claim. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/deuterium-derived-binding.ts
def deuterium_derived_binding (ctx : DeuteriumDerivedBindingContext) : Prop :=
    (ctx.NF_p_braid_word ≠ [] ∧ ctx.NF_n_braid_word ≠ []) ∧
    ctx.braid_length_B3 = 6 ∧
    (ctx.h3_strand_count = 3 ∧
     ctx.h6_strand_count = 2 * ctx.h3_strand_count) ∧
    ctx.T_pn = (ctx.sigma_0 + ctx.sigma_0_inv) / 2 ∧
    (ctx.B_d
      = (ctx.tr_M_p + ctx.tr_M_n - ctx.tr_M_Tpn_n) * ctx.m_e * ctx.Vol_B3
        * (1 - ctx.α_EM / 2)) ∧
    (ctx.B_exp = 2.2246 ∧ |ctx.B_d - ctx.B_exp| < 0.001)

/-! ## Mass–binding endomorphism analogy (2026-05-28)

The binding-energy formula is the structural analogue of the mass
endomorphism. Where the nucleon mass is

    m(K) = m_e · (Vol(𝓑_3) / ℏ_q²) · lw(K, q_0),

the binding energy of a composite nucleus is

    B(K) = m_e · Vol(K_bind) · Δtr,    Δtr = |tr_free| − |tr_atom|,

with K_bind the inter-nucleon **binding link** (Hopf for the deuteron,
8₁₁-class for ³H, L6a4 for ³He — identified by the binding-K SDP
solver). The deuteron uses Vol(𝓑_3) = 8G because both nucleons are
Borromean and the Hopf inter-nucleon link is Seifert-fibred (volume 0).

The analogy is recorded as a structural correspondence between the
two endomorphism shapes. -/
class BindingEndomorphismAnalogy where
  m_e : ℝ
  /-- Borromean volume Vol(𝓑_3) = 8G (mass side — nucleons are Borromean). -/
  Vol_B3 : ℝ
  /-- Binding-link volume Vol(K_bind) (binding side — atom-specific:
      Hopf for ²H, 8₁₁-class for ³H, L6a4 for ³He). For the deuteron
      this equals Vol(𝓑_3); for A≥3 it differs. -/
  Vol_Kbind : ℝ
  /-- Substrate ℏ_q² appearing in the mass formula denominator. -/
  hbar_q_sq : ℝ
  /-- Mass linking weight lw(K, q_0). -/
  lw : ℝ
  /-- Trace difference Δtr = |tr_free| − |tr_atom|. -/
  delta_tr : ℝ
  /-- Predicted nucleon mass. -/
  m_pred : ℝ
  /-- Predicted binding energy. -/
  B_pred : ℝ
  hbar_q_sq_ne : hbar_q_sq ≠ 0
  lw_ne : lw ≠ 0
  delta_tr_ne : delta_tr ≠ 0
  /-- Mass endomorphism shape (always Borromean Vol_B3). -/
  mass_shape : m_pred = m_e * (Vol_B3 / hbar_q_sq) * lw
  /-- Binding endomorphism shape (general binding-link volume). -/
  binding_shape : B_pred = m_e * Vol_Kbind * delta_tr

/-- The mass and binding endomorphisms share the same structural
    template: stripping the structural factor (lw/ℏ_q² for mass,
    Δtr for binding) leaves `m_e · Vol(·)` — the Borromean volume on
    the mass side, the binding-link volume on the binding side.

    For the **deuteron** these coincide (Vol(K_bind) = Vol(𝓑_3) = 8G,
    the Hopf inter-nucleon link being Seifert-fibred), so both
    prefactors equal `m_e · Vol(𝓑_3)`; for A≥3 they differ by the
    binding-link volume ratio. -/
-- Ref: [leitner2026] docs/audits/2026-05-28-binding-endomorphism-analogy.md
theorem mass_binding_share_prefactor [a : BindingEndomorphismAnalogy] :
    a.m_pred / (a.lw / a.hbar_q_sq) = a.m_e * a.Vol_B3
    ∧ a.B_pred / a.delta_tr = a.m_e * a.Vol_Kbind := by
  refine ⟨?_, ?_⟩
  · rw [a.mass_shape]
    field_simp [a.hbar_q_sq_ne, a.lw_ne] <;> ring
  · rw [a.binding_shape]
    field_simp [a.delta_tr_ne] <;> ring

/-- Deuteron specialization: when the binding link has Borromean
    volume (Vol(K_bind) = Vol(𝓑_3)), the two endomorphisms share the
    identical `m_e · Vol(𝓑_3)` prefactor. -/
-- Ref: [leitner2026] docs/audits/2026-05-28-binding-endomorphism-analogy.md
theorem mass_binding_prefactor_deuteron [a : BindingEndomorphismAnalogy]
    (h : a.Vol_Kbind = a.Vol_B3) :
    a.m_pred / (a.lw / a.hbar_q_sq) = a.B_pred / a.delta_tr := by
  obtain ⟨h1, h2⟩ := mass_binding_share_prefactor (a := a)
  rw [h1, h2, h]