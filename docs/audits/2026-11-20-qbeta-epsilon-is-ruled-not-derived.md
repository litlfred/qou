# Q_β: ε is ruled, not derived — and so are the other two factors

Bean `qou-99qc`. Owner question 2026-11-20: *"Is this true? ε is Markov trace. Don't we need to derive it?"*
This is a status audit. Nothing is wired and no number in the corpus changes. All figures below were measured at the proton pin
(`qou_substrate.constants.q_at()`) at 50 dps, against CODATA Q_β = 0.78233341 MeV.

## 1. Short answer

**ε = Markov trace at z_D is an owner ruling (2026-09-08), not a derivation.** The content block
`nuclear-interactions/neutron-qvalue-symbolic.md` says so in words: *"The functional applied to Δ … is the Markov trace at
z_D (convention D, owner ruling 2026-09-08)."* The ruling picked between admissible options; the 2026-09-05 options doc
(`2026-09-05-qbeta-functional-decision-options.md`, Option C) lists its commitment as *"uniformity of functional across mass
and decay channels — a substantive physical claim, currently unargued."*

ε is not the only posited factor. `Q_β = |ε(Δ)|·E₀` has three, and none is derived:

| factor | status | where it says so |
|---|---|---|
| Δ = net(n) − net(p), from typed crossings uu = σ, dd = σ⁻¹, ud = ½(σ + σ⁻¹) | **definition** | `neutron-qvalue-symbolic.md`: "It is a definition, not a derived result"; Lean `commutant_trace_eq` shows no weight-preserving operator commuting with F₃ separates uud from udd beyond the pivot |
| ε, the functional | **ruling** | as above |
| E₀ = m_e/(q(q−1)) (or the tower-summed /(1−ℏ_q²)) as the MeV-per-unit-trace scale | **posited** | same block: "the derivation of its series is still open"; the dashboard tags α·ln(…) energy forms POSITED (bean qou-mkm8) |

## 2. The grid, re-measured

tr_z(Δ) = h²/2 − h·z (Δ's γ coefficient h²/2, σ₀ and σ₁ coefficients −h/2 each).

| z | tr_z(Δ) | × E₀ (order zero) | × E₀ (tower-summed, canonical since 2026-09-03) |
|---|---|---|---|
| 1 (Form A, inadmissible under D) | −0.187207 | 0.78365 (+0.17 %) | 0.79142 (+1.16 %) |
| q (augmentation) | −0.210199 | 0.87989 (+12.5 %) | 0.88861 (+13.6 %) |
| z_D (ruled) | −0.106236 | 0.44470 (−43.2 %) | 0.44911 (−42.6 %) |

So the remembered 0.17 % needs **two** superseded choices at once: z = 1 *and* the order-zero E₀. With the canonical
tower-summed E₀ the same Form A is +1.16 %.

## 3. The decisive check: Δ is not the difference of the mass-channel objects

If ε and the scale were derived, they would follow from energy conservation, Q_β = m_n − m_p − m_e, with each nucleon mass
from the mass channel. The canonical nucleon mass is m = 2(m_μ·F_Bor − 6 m_e), F_Bor = |tr_M(β)|·[3]_q!/q³, so the
mass-channel scale per unit trace is 2 m_μ [3]_q!/q³ = **945.76 MeV**, against E₀ = 4.186 MeV. Applied to this Δ:

| z | 945.76·\|tr_z(Δ)\| − m_e |
|---|---|
| 1 | 176.5 MeV |
| z_D | 99.96 MeV |

Two to three orders of magnitude off. **The Δ in the Q_β formula is not the difference of the objects whose traces give the
nucleon masses**, and E₀ is not the mass channel's scale. The decay formula is a separate construction that shares q₀ and
H₃(q) with the mass channel but no derivation step. Energy conservation therefore cannot currently be used to *derive* ε:
there is no independently computed neutron mass to subtract — production defines m_n = m_p + Q_β + m_e
(`m_p_substrate_identity_50dps.py:10`), which is circular for this purpose.

## 4. The other corpus route is fitted

`prop:flavor-split-substrate` gives (m_n − m_p)/M_N ≈ (q−1)²(1−q⁻⁴)/3 and hence Q_β = **0.78068 MeV (−0.21 %)** with no ε.
Its own proof, Step 2, labels the per-quark split h²·ℏ_q/√q *"a phenomenological ansatz … selection against the target"*, and
Steps 1 and 3 hold only for the excised convention-C weight. Not a derivation either.

## 5. What a derivation would have to supply

1. **The u/d distinction inside the braid** — the step currently a definition (typed crossings). Without it p and n are the
   same Borromean word and Q_β = −m_e. This is the isospin problem, not a Q_β-specific one.
2. **One functional and one scale for masses and decay.** If (1) gives nucleon words β_p, β_n, energy conservation *derives*
   Q_β = 2 m_μ [3]_q!/q³·(|tr_M(β_n)| − |tr_M(β_p)|) − m_e, with ε = the mass channel's tr_M at z_D. The 2026-09-08 ruling would
   then become a theorem — but the scale would be 945.76 MeV per unit, not E₀, so the trace difference must be ~10⁻³, not ~0.1.
3. **Or** a derivation that the decay channel is a different object (a width functional, per the CAL-2 ruling Q_β = ℏ/𝔇_β),
   with its own functional and scale argued, not chosen.

Route 2 is the one that would make the decay sector parameter-free. It reduces to the u/d problem.

## 6. Reproduce

```python
q = qou_substrate.constants.q_at(); h = q - 1/q; zD = q**3/(q**2+1)
t = h**2/2 - h*z                      # tr_z(Delta)
E0 = m_e/(q*(q-1));  E0_tower = E0/(1-((q-1)/q)**2)
S = 2*m_mu*(q+1/q)*(q**2+1+q**-2)/q**3   # mass-channel scale, m_mu = m_e*Vol(4_1)/hbar_q^2
X = (q-1)**2*(1-q**-4)/3;  Q_fs = m_p*X/(1-X/2) - m_e
```

## 7. Addendum: do γγ / Breit–Wheeler give u and d separately? (owner question, same day)

Corpus search: content, computations (live and `fsh-guts/deprecated`) and witnesses for Breit–Wheeler and γγ, plus every witness carrying a Q_β value.

**7.1 The April Breit–Wheeler nucleon run was calibrated on Q_β.** `fsh-guts/deprecated/computations/breit-wheeler-nucleon-nf.py`
(witness computed 2026-04-15) builds p = B₃·(u,u,d) and n = B₃·(u,d,d) with typed crossings and gets
net(p) = 0.999125, net(n) = 0.810835, Δnet = −0.188291. Its E₀ = 4.154925 MeV is read from
`beta-decay-energy-scale.witness.json` field `E0_from_net_MeV`, and 0.78233341 / 0.18829062 = 4.1549250300084 — the same to
1e-13. So E₀ there **is Q_β divided by Δnet**. The Q_β it reproduces (0.7823334100) is its input returned, not a prediction.
Its u/d distinction is the typed-crossing definition, not something γγ produced.

**7.2 In the corpus u and d are one representation with opposite orientation.** `up-quark.md`: the up quark "is not a
distinct knot type … it is the unknot distinguished by its environment", ν|_{B₃,+}. `down-quark.md`: ν|_{B₃,−}, differing
"only by crossing orientation". Its charge note records a proved obstruction (`QOU.Braiding.mirror_odd_neutral_neutron_forces_zero`):
a mirror-odd charge gives Q(d) = −Q(u), so a neutral neutron forces every quark charge to zero. The Standard Model ratio
|Q_u| = 2|Q_d| is an asymmetry that **a pure mirror cannot supply**. `quark-antiquark-production-reduction.md` derives a
quark crossing from γγ (L₊·e⁻ → σ₁ + …) but states "the quark type is determined by the crossing orientation", i.e. again
by the mirror.

**7.3 What γγ-selected words do to Q_β (all ε = tr at z_D, tower E₀, proton pin):**

| witness | finding |
|---|---|
| `qbeta-gamma-gamma-admissible-family-h3` | in H₃ every γγ word is (σ₀σ₁⁻¹)^k; the derived member k = 3 (Borromean) misses by +440 % |
| `qbeta-gamma-gamma-qbeta-prediction` | n = 4: all five γγ + SDP admissible words +458 % to +620 %; the near-hit at 0.11 % appears only with the SDP dropped and is worse than chance |
| `qbeta-gamma-gamma-ruling-selects-ordering` | the γγ-ruled interleaved 11-letter element: −16.68 % (the current scorecard) |
| `qbeta-pn-asymmetry-has-one-home-under-the-ruling` | **the γγ core and the gluon pair are byte-identical between p and n**; the corpus separates the nucleons only in the 3-letter typed quark block, and every γγ word has alternating character exactly 1 (`altChar_eq_one`), so γγ cannot see the separation |
| `qbeta-gamma-gamma-selected-delta` | at γγ level 1 the n − p difference vanishes identically (`GammaGammaSelectedDeltaVanishes`, Lean) |

**7.4 Reading.** Nothing in the corpus derives u and d from γγ as distinct representations; the γγ words are proved blind
to the p/n difference. The owner's position (u and d carry *separate representations*) is therefore not yet implemented
anywhere, and it is exactly what the proved obstruction in 7.2 asks for: a u/d asymmetry that is not a mirror. That is the
research target: assign u and d to distinct H_n(q) representations (or idempotents) whose γγ production differs, then
re-run Q_β through energy conservation (§5, route 2).

## 8. Correction to §7.2 — the corpus does carry u and d as separate lines, via the γγ vertex on four strands

§7.2 read only the definition blocks. The `QOU/QuarkState/` Lean cluster (beans `qou-wkcd`, `qou-a1hh`, `qou-hlx7`; 2026-11-15/16)
goes further, and it is what the owner is pointing at:

* `FlavourDoubletFourStrands.lean`: in the (3,1) representation of H₄(q) the left line of σ₁ is a **doublet**. Two flavour labels
  sit side by side (owner choice 2026-11-15, "both"): **A** u/d = the σ₃ eigenlines; **B** u/d = the J₄ eigenlines,
  J₄ = σ₃σ₂σ₁²σ₂σ₃ (strand 4 looping once around strands 1–3). Each comes with an sl₂ pair whose Cartan coupling is
  cS = 2(q⁴+1)/(q²+1)² (A) and cJ = 2(q²+1)²(q⁴+1)/(q⁴+q²+1)² (B).
* **The γγ vertex carries the flavour flip**: `L_u(σ₁σ₂⁻¹)L_d = q·eS` (A), and for B only the γγ vertex that reaches strand 4
  does it: `Ja(σ₂σ₃⁻¹)Jb = q·eJ` (`three_strand_word_no_mix`: no three-strand word mixes the J₄ flavour).
* Scoping on record: J₄ is the three-strand isospin multiplicity (3/2 vs 1/2), **not** T³, so it is not literally n ↔ p.

`QBetaChiralityReduction.lean` (sorry-free) reduces the choice of ε on Δ_S to **one number**: for every block-weighted trace,
τ(Δ_S) = −(h[2]/2)·y₃ with y₃ = τ(J), the trace's chirality expectation. So Q_β = (h[2]/2)·y₃·E₀.

**Measured (proton pin, 50 dps), y₃ needed for CODATA: 0.889126 (order-zero E₀), 0.880397 (tower E₀).**

| y₃ from | y₃ | Q_β order-zero E₀ | Q_β tower E₀ |
|---|---|---|---|
| augmentation / left-line support (`normalised_eq_augmentation`) | 1 | +12.47 % | +13.59 % |
| Markov at z_D, = cS/2 exactly (label A) | 0.505404 | −43.16 % | −42.59 % |
| **cJ/2, the J₄ coupling (label B, the strand-4 γγ flavour)** | **0.892057** | **+0.33 %** | **+1.32 %** |

The identity cS/2 = τ_{z_D}(J) is exact, so "label A ↔ Markov z_D" is an existing correspondence. **cJ/2 is its label-B analogue,
and it lands within 0.33 %.**

🛑 **This is a LEAD, not a result, and it must not be wired.** Under §NO FITTING it is selection against the target until a
derivation exists: three candidates were evaluated here and the one near CODATA is reported. Three trials is a small
look-elsewhere factor, but it is not zero. The +0.33 % also uses the order-zero E₀; with the canonical tower-summed E₀ it is
+1.32 %. What would turn it into a derivation: a proof that the decay channel's trace has chirality expectation τ(J) = cJ/2,
i.e. a trace on the γγ-produced four-strand sector whose (3)-block weight is cJ/2. In q-integers, cJ/2 = [2]²·[2]_{q²}/[3]².
Bean `qou-99qc`.
